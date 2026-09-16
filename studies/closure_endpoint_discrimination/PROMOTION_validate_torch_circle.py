"""Fixed small circle backend parity/restart example; no archived inputs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

# This opt-in producer owns its process; constrain numerical thread pools
# before importing their runtimes. The library itself sets no global policy.
for variable in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[variable]='1'

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'code'))
from pde import observable_solver as cpu
from pde import observable_torch_circle as backend


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--device',default='cpu')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    out=Path(args.output)
    out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    device=torch.device(args.device)
    if device.type not in ('cpu','cuda'): raise ValueError('CPU or CUDA required')
    if device.type=='cuda':
        torch.cuda.set_device(device)
        torch.cuda.reset_peak_memory_stats(device)
    def sync():
        if device.type=='cuda': torch.cuda.synchronize(device)
    record=dict(status='running',configuration=dict(orders=[1,3,5],Q=64,P=32,steps=4,h=.005,
               block_size=2,unit_angles=[.1,.5,1.2,2.],labels=[1.,-.3,.2,-.7],weights=[.1,.2,.3,.4],
               purpose='finite backend agreement and own-state restart',wall_limit_seconds=120,
               tensor_limit_bytes=1073741824,tolerance=2e-11,threads=1),
               environment=dict(python=sys.version,numpy=np.__version__,torch=torch.__version__,
               device=str(device),cuda=torch.version.cuda,tf32=False,
               cublas_workspace_config=os.environ.get('CUBLAS_WORKSPACE_CONFIG'),
               device_name=torch.cuda.get_device_name(device) if device.type=='cuda' else 'CPU'),runs=[])
    sources=[Path(__file__),*sorted((ROOT/'code/pde').glob('*.py'))]
    record['sources']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    (out/'record.json').write_text(json.dumps(record,indent=2)+'\n')
    began=time.monotonic()
    def timeout_handler(signum,frame):
        raise TimeoutError('120-second validation work budget exceeded')
    signal.signal(signal.SIGALRM,timeout_handler)
    signal.alarm(120)
    try:
        angles=np.array(record['configuration']['unit_angles'])
        u=np.column_stack((np.cos(angles),np.sin(angles)))
        y=np.array(record['configuration']['labels']); weights=np.array(record['configuration']['weights'])
        for order in (1,3,5):
            sync(); start=time.monotonic()
            s=backend.initialize(order,initialization_nodes=64,population_nodes=32,device=device)
            data=backend.data_law(u,y,weights,device=device)
            sync(); initialized=time.monotonic()
            final=backend.evolve(s,data,steps=4,step_size=.005,block_size=2)
            sync(); evolved=time.monotonic()
            obs=backend.observe(final,data,include_pairs=True)
            sync(); observed=time.monotonic()
            half=backend.evolve(s,data,steps=2,step_size=.005,block_size=2)
            checkpoint=out/f'p{order}.json'
            backend.save_restart(checkpoint,half,data)
            restored,law=backend.load_restart(checkpoint,device=device)
            continued=backend.evolve(restored,law,steps=2,step_size=.005,block_size=2)
            exact=all(torch.equal(getattr(final,k),getattr(continued,k)) for k in backend.KEYS)
            reference=cpu.evolve(backend.to_cpu(s),cpu.DataLaw(u,y,weights),steps=4,step_size=.005,block_size=2)
            errors={k:float(np.max(np.abs(getattr(reference,k)-getattr(final,k).cpu().numpy()))) for k in backend.KEYS}
            np.savez(out/f'p{order}_observations.npz',**{k:v.cpu().numpy() for k,v in obs.items() if v is not None})
            run=dict(order=order,initialization_transfer_seconds=initialized-start,
                     evolution_seconds=evolved-initialized,observation_seconds=observed-evolved,
                     check_restart_reference_seconds=time.monotonic()-observed,reference_errors=errors,
                     restart_exact=exact,state_bytes=backend.state_bytes(final))
            record['runs'].append(run)
            if not exact or max(errors.values())>2e-11: raise AssertionError('backend parity/restart failed')
            if device.type=='cuda' and torch.cuda.max_memory_allocated(device)>1073741824:
                raise RuntimeError('tensor allocation cap exceeded')
            if time.monotonic()-began>120: raise TimeoutError('wall budget exceeded')
        record['status']='complete'
    except BaseException as error:
        record.update(status='failed',error=repr(error))
        raise
    finally:
        signal.alarm(0)
        sync()
        record.update(validation_work_seconds=time.monotonic()-began,
                      process_peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                      cuda_peak_allocated_bytes=torch.cuda.max_memory_allocated(device) if device.type=='cuda' else None,
                      cuda_peak_reserved_bytes=torch.cuda.max_memory_reserved(device) if device.type=='cuda' else None)
        record['outputs']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.name!='record.json'}
        (out/'record.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'status':record['status'],'output':str(out),'seconds':record['validation_work_seconds']}))

if __name__=='__main__': main()
