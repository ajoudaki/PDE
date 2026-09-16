"""Small reproducible example: explicit input NPZ or fixed synthetic finite law.

Default d=3,m=9,seed=101,n=P=16,10 Heun steps of .005. This demonstrates
operation only. A supplied NPZ must contain inputs U=x/sqrt(d), labels, IDs.
"""
import argparse
import hashlib
import json
import os
import platform
import resource
import signal
import time
from pathlib import Path
# This command owns its process; the reusable modules do not set global policy.
for variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[variable]='1'
import numpy as np
import torch
from pde.observable_torch_p1 import initialize_p1
from pde.finite_torch import NetworkEngine
from pde.closure_comparison import prediction_metrics, gram_metrics


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--inputs',type=Path)
    parser.add_argument('--device',default='cpu')
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    try:
        run(args)
    except BaseException as error:
        path=args.output/'status.json'
        status=json.loads(path.read_text()) if path.exists() else {}
        status.update(status='failed',error=repr(error))
        path.write_text(json.dumps(status,indent=2)+'\n')
        raise
    finally:
        signal.alarm(0)


def run(args):
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    torch.use_deterministic_algorithms(True)
    if args.device.startswith('cuda'):
        torch.cuda.set_per_process_memory_fraction(.15,device=args.device)
        torch.cuda.reset_peak_memory_stats(args.device)
    def sync():
        if args.device.startswith('cuda'):torch.cuda.synchronize(args.device)
    def measure(name,operation):
        sync(); tick=time.perf_counter()
        value=operation()
        sync(); timings[name]=time.perf_counter()-tick
        return value
    limits=dict(wall_seconds=120,threads=1,cuda_allocator_fraction=.15,
                scope='fixed finite operation example; supplied inputs may increase resource demand')
    (args.output/'status.json').write_text(json.dumps(dict(status='running',limits=limits),indent=2)+'\n')
    def timed_out(signum,frame):
        (args.output/'status.json').write_text(json.dumps(dict(status='timeout',limits=limits),indent=2)+'\n')
        raise TimeoutError('finite example exceeded 120-second work limit')
    signal.signal(signal.SIGALRM,timed_out)
    signal.alarm(120)
    sync(); work_began=time.perf_counter();timings={}
    rng=np.random.default_rng(101)
    if args.inputs:
        with np.load(args.inputs,allow_pickle=False) as data:
            U,y,ids = (data[k].copy() for k in ('inputs','labels','ids'))
    else:
        U=rng.normal(size=(9,3));U[0]=0;U[2]=U[1]
        y=np.tanh(U[:,0]-U[:,1]);ids=np.arange(len(U))
    # Validate identity semantics before producing comparison outputs.
    prediction_metrics(y,y,ids=ids,reference_ids=ids)
    if U.ndim != 2 or len(U)!=len(y):raise ValueError('input rows must match labels')
    timings['input_preparation_seconds']=time.perf_counter()-work_began
    closure,state=measure('closure_initialization_transfer_seconds',lambda:initialize_p1(U.shape[1],16,101,device=args.device,population_rule='antithetic',folded=True,block_size=4))
    network=measure('network_initialization_transfer_seconds',lambda:NetworkEngine(U.shape[1],16,101,device=args.device,block_size=4))
    sync(); tick=time.perf_counter()
    netstate=network.initial_state()
    data=closure.prepare_data(U,y);netdata=network.prepare_data(U,y)
    sync();timings['data_and_working_state_seconds']=time.perf_counter()-tick
    state=measure('closure_integration_seconds',lambda:closure.evolve(state,data,steps=10,step_size=.005))
    netstate=measure('network_integration_seconds',lambda:network.evolve(netstate,netdata,steps=10,step_size=.005))
    elapsed=timings['closure_integration_seconds']+timings['network_integration_seconds']
    sync();tick=time.perf_counter()
    closure.save_restart(args.output/'closure.npz',state,data,metadata={'time':.05,'steps':10,'step_size':.005})
    co=closure.observations(state,data,include_pairs=True);no=network.observations(netstate,U)
    to_np=lambda x:x.detach().cpu().numpy().copy()
    arrays=dict(inputs=U,labels=y,ids=ids,probabilities=to_np(data.probabilities),
                closure_prediction=to_np(co['prediction']),network_prediction=to_np(no['prediction']))
    for prefix,engine,current in (('closure',closure,state),('network',network,netstate)):
        for key in ('w','c','M'):arrays[prefix+'_'+key]=to_np(getattr(current,key))
    for key in ('b1','b2','p1','p2','D','g'):arrays['closure_'+key]=to_np(getattr(closure,key))
    for key in ('w','c','M'):arrays['network_initial_'+key]=to_np(getattr(network.initial,key))
    metrics=prediction_metrics(arrays['closure_prediction'],arrays['network_prediction'],ids=ids,reference_ids=ids)
    for layer in (1,2):
        for prefix,obs in (('closure',co),('network',no)):
            arrays[f'{prefix}_gram{layer}']=to_np(obs[f'gram{layer}_current'])
        metrics[f'gram{layer}']=gram_metrics(arrays[f'closure_gram{layer}'],arrays[f'network_gram{layer}'],ids=ids,reference_ids=ids)
    np.savez(args.output/'observations.npz',**arrays)
    sync();timings['observation_analysis_checkpoint_array_write_seconds']=time.perf_counter()-tick
    source_root=Path(__file__).resolve().parents[1]
    paths=[Path(__file__),*(source_root/'pde'/name for name in ('observable_p1_initialization.py','observable_torch_p1.py','finite_torch.py','finite_network.py','closure_comparison.py'))]
    record=dict(scope='finite synthetic/supplied-input operation only; no accuracy or speed claim',seed=101,
                width=16,nominal_population_nodes=16,stored_population_nodes=8,closure_order=1,
                dimension=U.shape[1],samples=len(U),time=.05,step=.005,steps=10,device=args.device,
                dtype='float64',python=platform.python_version(),numpy=np.__version__,torch=str(torch.__version__),
                policy=closure.arithmetic_policy(),threads=1,elapsed_integration_seconds=elapsed,
                timings=timings,resource_limits=limits,
                process_peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                retained_tensor_bytes=dict(closure=closure.retained_bytes(state),network=network.retained_bytes(netstate)),
                source_sha256={str(p.relative_to(source_root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                input_sha256=hashlib.sha256(args.inputs.read_bytes()).hexdigest() if args.inputs else None,
                output_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (args.output/'observations.npz',args.output/'closure.npz')},
                metrics=metrics)
    if args.device.startswith('cuda'):
        record['gpu_name']=torch.cuda.get_device_name(args.device)
        record['peak_allocated_bytes']=torch.cuda.max_memory_allocated(args.device)
        record['peak_reserved_bytes']=torch.cuda.max_memory_reserved(args.device)
    sync()
    record['validation_work_seconds']=time.perf_counter()-work_began
    record['timing_scope']='work timer includes input preparation through source/output hashing; excludes interpreter/import, device/policy setup, final record/status writes; CUDA phase boundaries synchronized'
    record['memory_scope']='process peaks with both systems retained; not isolated per-system allocator peaks; tensor counts are separate'
    (args.output/'record.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    (args.output/'status.json').write_text(json.dumps(dict(status='complete',limits=limits),indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'integration_seconds':elapsed}))

if __name__=='__main__':main()
