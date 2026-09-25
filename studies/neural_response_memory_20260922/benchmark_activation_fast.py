"""Complete-trial GPU benchmark and short evolution equivalence; GPU0 only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import numpy as np
import torch
from activation_moment_engine import ActivationMomentEngine, controlled_error
from activation_fast_engine import FastActivationTrial, FastActivationMomentEngine
from activation_circle_run import heun_trial, training_loss
from deep_moment_engine import DeepMomentState, tensor_rms


def base_trial(engine,state,step,rtol,atol):
    first,second,euler,candidate=heun_trial(engine,state,step)
    engine.validate_state(candidate)
    error=controlled_error(engine,state,euler,candidate,rtol,atol)
    loss=training_loss(engine,candidate)
    return first,second,euler,candidate,error,loss,True


def error_components(engine,state,euler,candidate,rtol,atol):
    ratios={}
    for name in state.names():
        a,b,c=(getattr(x,name) for x in (state,euler,candidate))
        scale=torch.maximum(tensor_rms(a),tensor_rms(c)).clamp_min(1)
        ratios[name]=float((tensor_rms(c-b)/(atol+rtol*scale)).cpu())
    for layer in (2,3):
        scale=torch.maximum(engine.hidden_increment_norm(state,layer),engine.hidden_increment_norm(candidate,layer))/(engine.n**.5)
        error=engine.hidden_difference_norm(candidate,euler,layer)/(engine.n**.5)
        ratios['physical_W'+str(layer)]=float((error/(atol+rtol*scale.clamp_min(1))).cpu())
    return ratios


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True);parser.add_argument('--steps',type=int,default=100)
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    started=time.perf_counter();torch.set_num_threads(1);torch.cuda.set_device(0)
    torch.use_deterministic_algorithms(True);torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    cfg=json.loads((args.run/'config.json').read_text())
    common=dict(seed=cfg['seed'],activation=cfg['activation'],device='cuda:0',dtype=torch.float64)
    base=ActivationMomentEngine(2,cfg['width'],cfg['order'],cfg['inputs'],cfg['labels'],**common)
    batched=FastActivationMomentEngine(2,cfg['width'],cfg['order'],cfg['inputs'],cfg['labels'],**common)
    with np.load(args.run/'arrays.npz') as saved:
        state=DeepMomentState(*(torch.as_tensor(saved[k],device='cuda:0') for k in base.initial.names()))
        step=float(saved['accepted_steps'][-1])
    rtol,atol=cfg['rtol'],cfg['atol'];methods={};setup={}
    methods['reference']=lambda s,h:base_trial(base,s,h,rtol,atol)
    for name,engine,graph in [('packed',base,False),('graphs',base,True),('batched_graphs',batched,True)]:
        start=time.perf_counter();obj=FastActivationTrial(engine,cuda_graph=graph,rtol=rtol,atol=atol)
        torch.cuda.synchronize();setup[name]=time.perf_counter()-start
        methods[name]=lambda s,h,obj=obj:obj.trial(s,h,rtol,atol)
    reference=methods['reference'](state,step);comparisons={};timings={}
    for name,call in methods.items():
        result=call(state,step)
        diffs=[float((a-b).abs().max().cpu()) for sa,sb in zip(result[:4],reference[:4])
               for a,b in zip(sa.tensors(),sb.tensors())]
        comparisons[name]=dict(max_tensor_difference=max(diffs),error_difference=abs(result[4]-reference[4]),
            loss_difference=abs(result[5]-reference[5]),valid=result[6],bitwise_tensors=all(d==0 for d in diffs))
        for _ in range(3):call(state,step)
        reps=[]
        for _ in range(3):
            torch.cuda.synchronize();start=time.perf_counter()
            for _ in range(20):call(state,step)
            torch.cuda.synchronize();reps.append((time.perf_counter()-start)/20)
        timings[name]=dict(median_seconds=float(np.median(reps)),replicates=reps)
    # Same prescribed evolving step sequence isolates implementation changes.
    evolution={};states={name:state.clone() for name in methods};errors={name:[] for name in methods}
    for i in range(args.steps):
        h=step*(.75 if i%2 else 1.)
        for name,call in methods.items():
            result=call(states[name],h);states[name]=result[3];errors[name].append(result[4])
    base_pred=base.predict(states['reference'],base.inputs)
    for name,s in states.items():
        evolution[name]=dict(max_state_difference=max(float((a-b).abs().max().cpu())
            for a,b in zip(s.tensors(),states['reference'].tensors())),
            train_prediction_rms=float(tensor_rms(base.predict(s,base.inputs)-base_pred).cpu()),
            max_error_ratio_difference=float(np.max(np.abs(np.asarray(errors[name])-errors['reference']))))
    result=dict(run=str(args.run.resolve()),activation=cfg['activation'],P=cfg['order'],width=cfg['width'],
        source_sha256={n:hashlib.sha256((Path(__file__).parent/n).read_bytes()).hexdigest()
            for n in [Path(__file__).name,'activation_fast_engine.py']},
        dtype='float64',device='cuda:0',step=step,setup_seconds=setup,timings=timings,
        single_trial=comparisons,prescribed_evolution_steps=args.steps,evolution=evolution,
        reference_error_components=error_components(base,state,reference[2],reference[3],rtol,atol),
        elapsed_seconds=time.perf_counter()-started,
        scope='Execution benchmark at a retained state and fixed-step equivalence; not a new scientific training comparison.')
    (args.out/'benchmark.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['timings','single_trial','evolution','reference_error_components','elapsed_seconds']},indent=2))


if __name__=='__main__':main()
