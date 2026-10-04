"""Bounded staged input-field campaign; all outcomes and sources are retained."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import sys
import time
import traceback
import numpy as np
import torch
from input_field import make_model, grid, circle, teacher, set_batch, InputFieldFlow, internal_matrix

HERE=Path(__file__).resolve().parent


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False))


@torch.no_grad()
def gpu_sanity(device):
    """Fresh-batch captured/eager parity and paired PRNG consumption."""
    maximum=0.;fingerprints=[]
    for kind in ['field','dense']:
        kw=dict(n=16,seed=731,device=device,dtype=torch.float32,theta=grid(8,device,torch.float32),
                name='A',count=9,order=3,prefix_nodes=32)
        captured=make_model(kind,**kw); eager=make_model(kind,**kw)
        saved=[v.clone() for v in captured.state]
        generator=torch.Generator(device=device).manual_seed(771)
        def step(model, rng):
            theta=2*math.pi*torch.rand(8,device=device,generator=rng)
            set_batch(model,theta,teacher(theta,'A'));model.step(1/64)
        stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
        with torch.cuda.stream(stream):
            for _ in range(2):step(captured,generator)
        torch.cuda.current_stream(device).wait_stream(stream)
        for a,b in zip(captured.state,saved):a.copy_(b)
        torch.cuda.synchronize(device)
        graph=torch.cuda.CUDAGraph();graph.register_generator_state(generator)
        with torch.cuda.graph(graph,stream=stream):
            for _ in range(8):step(captured,generator)
        for a,b in zip(captured.state,saved):a.copy_(b)
        generator.manual_seed(771)
        other_generator=torch.Generator(device=device).manual_seed(771)
        for _ in range(8):graph.replay()
        for _ in range(64):step(eager,other_generator)
        for a,b in zip(captured.state,eager.state):
            maximum=max(maximum,float((a-b).abs().max()))
            torch.testing.assert_close(a,b,atol=2e-6,rtol=2e-6)
        torch.testing.assert_close(captured.inputs,eager.inputs,atol=0,rtol=0)
        fingerprints.append(captured.inputs.cpu().numpy().tolist())
    assert fingerprints[0]==fingerprints[1]
    return dict(status='pass',maximum_error=maximum,batch_fingerprint=fingerprints[0])


@torch.no_grad()
def run_one(config, output, device):
    started=time.perf_counter(); dtype=torch.float32
    theta=grid(config['nodes'], device, dtype)
    model=make_model(config['kind'], n=128, seed=config['seed'], device=device,
                     dtype=dtype, theta=theta, name=config['teacher'], count=config['C'],
                     order=config['q'], prefix_nodes=config.get('prefix_nodes',256))
    query=grid(2048,device,dtype); xq=circle(query); yq=teacher(query,config['teacher'])
    h0=model._forward(xq,model._factors())[0]
    h0=[v.clone() for v in h0]; w0=model.w.clone(); W0=internal_matrix(model)
    initial_state=[v.clone() for v in model.state]
    generator=torch.Generator(device=device).manual_seed(config['seed']+600000)
    dt=config['dt']; count=round(config['T']/dt); block=32
    assert count%block == 0
    def step():
        if config['stream']:
            theta=2*math.pi*torch.rand(config['nodes'],device=device,dtype=dtype,generator=generator)
            set_batch(model,theta,teacher(theta,config['teacher']))
        model.step(dt)
    # Captured allocations and PRNG are replayed in order. Each algorithm starts
    # the batch generator at the same seed after capture, consuming exactly B
    # angles at each Euler step. No bank of permanent samples is allocated.
    torch.cuda.synchronize(device); torch.cuda.reset_peak_memory_stats(device)
    stream=torch.cuda.Stream(device=device); stream.wait_stream(torch.cuda.current_stream(device))
    with torch.cuda.stream(stream):
        for _ in range(2): step()
    torch.cuda.current_stream(device).wait_stream(stream)
    for a,b in zip(model.state,initial_state): a.copy_(b)
    torch.cuda.synchronize(device)
    graph=torch.cuda.CUDAGraph(); graph.register_generator_state(generator)
    with torch.cuda.graph(graph,stream=stream):
        for _ in range(block): step()
    for a,b in zip(model.state,initial_state): a.copy_(b)
    generator.manual_seed(config['seed']+600000)
    del initial_state
    torch.cuda.synchronize(device); capture_seconds=time.perf_counter()-started
    snapshots=[]; predictions=[]; status='complete'; actual=0
    checkpoints={count//4,count//2,count}
    for actual in range(block,count+1,block):
        graph.replay()
        if actual%256==0 or actual==count:
            pred=model.predict(xq); mse=float((pred-yq).square().mean())
            if not math.isfinite(mse) or mse > 100*float(yq.square().mean()):
                status='diverged'; break
            if time.perf_counter()-started>90:
                status='wall_limit'; break
        if actual in checkpoints:
            predictions.append(model.predict(xq).cpu().numpy())
            snapshots.append(dict(time=actual*dt,target_rmse=float((model.predict(xq)-yq).square().mean().sqrt())))
    pred=model.predict(xq); hidden=model._forward(xq,model._factors())[0]
    final_state_finite=all(bool(torch.isfinite(v).all()) for v in model.state)
    if not final_state_finite: status='nonfinite_state'
    torch.cuda.synchronize(device)
    memory_count=sum(v.numel() for v in getattr(model,'moments',[]))
    state_count=sum(v.numel() for v in model.state)
    moving_count=state_count
    if config['kind']=='readout': moving_count=model.c.numel()
    elif config['kind']=='frozen_internal': moving_count=model.c.numel()+model.w.numel()
    result=dict(config=config,status=status,final_state_finite=final_state_finite,
                maximum_state_abs=max(float(v.abs().max()) for v in model.state),
                seconds=time.perf_counter()-started,capture_seconds=capture_seconds,
                steps=actual,physical_time=actual*dt,teacher_rms=float(yq.square().mean().sqrt()),
                target_rmse=float((pred-yq).square().mean().sqrt()),
                feature_movement=[float((h-hinit).square().mean().sqrt()) for h,hinit in zip(hidden,h0)],
                first_weight_movement=float((model.w-w0).norm()/math.sqrt(model.n)),
                internal_weight_movement=float((internal_matrix(model)-W0).norm()),
                moving_scalar_count=moving_count,listed_state_scalars=state_count,
                memory_scalars=memory_count,fixed_internal_scalars=128*128 if config['kind']!='dense' else 0,
                peak_cuda_allocated_bytes=torch.cuda.max_memory_allocated(device),
                cuda_allocated_bytes=torch.cuda.memory_allocated(device),snapshots=snapshots,
                state_shapes=[list(v.shape) for v in model.state],
                tau=float(1+model.s) if getattr(model,'order',None) else None,
                batch_seed=config['seed']+600000,
                final_batch_fingerprint=model.inputs[:4].cpu().numpy().tolist())
    if not math.isfinite(result['target_rmse']): result['target_rmse']=None
    np.savez_compressed(output.with_suffix('.npz'),theta=query.cpu().numpy(),teacher=yq.cpu().numpy(),
                        prediction=pred.cpu().numpy(),trajectory=np.stack(predictions) if predictions else np.zeros((0,2048)))
    write_json(output.with_suffix('.json'),result)
    return result


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    p.add_argument('--device',default='cuda:0');p.add_argument('--stage',choices=['deterministic','stream','refine'],required=True)
    p.add_argument('--teacher',choices=['A','B'],default='A');p.add_argument('--C',type=int,default=9)
    p.add_argument('--seeds',default='101,102,103');args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    torch.cuda.set_device(args.device)
    hashes={}
    for name in ['input_field.py','input_field_experiment.py','baseline_compact_flow.py','INPUT_FIELD_PROTOCOL.md']:
        src=HERE/name;shutil.copy2(src,args.out/name);hashes[name]=hashlib.sha256(src.read_bytes()).hexdigest()
    write_json(args.out/'manifest.json',dict(command=sys.argv,source_hashes=hashes,torch=torch.__version__,
               numpy=np.__version__,device=args.device,gpu=torch.cuda.get_device_name(args.device),
               dtype='float32',tf32=False,stage=args.stage,started_unix=time.time()))
    write_json(args.out/'gpu_sanity.json',gpu_sanity(args.device))
    configurations=[]
    seeds=[int(v) for v in args.seeds.split(',')]
    base=dict(dt=1/32,T=64,nodes=128,stream=False,q=3,prefix_nodes=256)
    if args.stage=='deterministic':
        for seed in seeds:
            for name in ['A','B']:
                for kind,C in [('dense',17),('sample',17),('field',5),('field',9),('field',17)]:
                    configurations.append(dict(base,seed=seed,teacher=name,kind=kind,C=C))
        if 101 in seeds:
            for name in ['A','B']:
                for q in [1,5]: configurations.append(dict(base,seed=101,teacher=name,kind='field',C=17,q=q))
                configurations.append(dict(base,seed=101,teacher=name,kind='field',C=17,nodes=256))
    else:
        for seed in seeds:
            kinds=['field','dense','readout','frozen_internal','low_rank'] if args.stage=='stream' else ['field','dense']
            for kind in kinds:
                configurations.append(dict(base,seed=seed,teacher=args.teacher,kind=kind,C=args.C,
                                           dt=1/32 if args.stage=='stream' else 1/64,T=128,nodes=64,stream=True))
        if args.stage=='refine':
            configurations.append(dict(base,seed=seeds[0],teacher=args.teacher,kind='field',C=args.C,
                                       T=128,nodes=64,stream=True,prefix_nodes=512))
    write_json(args.out/'configurations.json',configurations)
    results=[];started=time.perf_counter()
    for index,config in enumerate(configurations):
        stem=args.out/f'run_{index:03d}_{config["kind"]}_{config["teacher"]}_s{config["seed"]}_C{config["C"]}_q{config["q"]}'
        print(json.dumps(dict(event='start',index=index,config=config)),flush=True)
        try: result=run_one(config,stem,args.device)
        except Exception as exc:
            result=dict(config=config,status='exception',error=repr(exc),traceback=traceback.format_exc())
            write_json(stem.with_suffix('.json'),result)
        results.append(result);write_json(args.out/'results.json',results)
        print(json.dumps(dict(event='end',index=index,**result)),flush=True)
        if time.perf_counter()-started>20*60:
            print('STAGE HARD WALL STOP',flush=True);break
    write_json(args.out/'completion.json',dict(seconds=time.perf_counter()-started,attempts=len(results),planned=len(configurations)))


if __name__=='__main__':main()
