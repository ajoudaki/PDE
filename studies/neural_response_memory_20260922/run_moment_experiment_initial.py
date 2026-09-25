"""Bounded study-local experiments; never writes archived references."""
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import torch
from moment_engine import MomentEngine, linear_combination, factor_frobenius

REFERENCES = {
    'two_outliers_alternating': 'scaling_discovery_refined01/two_outliers_alternating_full',
    'quadrant_alternating': 'diverse_fine_early01/quadrant_alternating_full',
    'quadrant_pairs': 'scaling_discovery_refined01/quadrant_pairs_full',
}
ROOT = Path(__file__).resolve().parents[2]

def number(t):
    return float(t.detach().cpu())

def rms(t):
    return t.square().mean().sqrt()

def loss(engine, state):
    prediction = state.c @ state.h2 / engine.n if state.lifted else engine.predict(state, engine.inputs)
    return number((prediction-engine.labels).square().mean())

def error_ratio(engine, current, euler, candidate, rtol, atol):
    ratios = []
    for name in current.names():
        a,b,c = (getattr(state,name) for state in (current,euler,candidate))
        scale = torch.maximum(rms(a),rms(c)).clamp_min(1.)
        ratios.append(rms(c-b)/(atol+rtol*scale))
    lc,rc = engine.delta_factors(candidate)
    le,re = engine.delta_factors(euler)
    l0,r0 = engine.delta_factors(current)
    numerator = factor_frobenius(torch.cat((lc-le,le),1),torch.cat((rc,rc-re),1))
    scale = torch.maximum(factor_frobenius(l0,r0),factor_frobenius(lc,rc)).clamp_min(1.)
    ratios.append(numerator/(atol+rtol*scale))
    return number(torch.stack(ratios).max())

def panel_predict(engine,state,inputs,block=512):
    return np.concatenate([engine.predict(state,inputs[k:k+block]).cpu().numpy() for k in range(0,len(inputs),block)])

def run(args,case,order):
    directory=Path(args.out)/f'{case}_{args.variant}_P{order}_level{args.level}'
    directory.mkdir(parents=True,exist_ok=False)
    archive_path=ROOT/'data/generated/random_dictionary_learned_circle_20260920'/REFERENCES[case]/'arrays.npz'
    archive=np.load(archive_path)
    inputs,labels=archive['training_inputs'],archive['labels']
    if args.variant=='bins':
        engine_cls=MomentEngine
    else:
        from orthogonal_moment_engine import OrthogonalMomentEngine
        engine_cls=OrthogonalMomentEngine
    engine=engine_cls(2,2048,order,inputs,labels,device=args.device,lifted=not args.direct)
    state=engine.initial_state()
    initial_match={
        'w':np.array_equal(state.w.cpu().numpy(),archive['w'][0]),
        'c':np.array_equal(state.c.cpu().numpy(),archive['c'][0]),
        'W0':np.array_equal(engine.W0.cpu().numpy(),archive['M'][0]),
    }
    if not all(initial_match.values()):
        raise RuntimeError('archived initialization mismatch')
    angles,panel=archive['endpoint_angles'],archive['endpoint_inputs']
    snapshot_inputs=archive['circle_inputs']
    reference_times=archive['snapshot_times']
    reference_predictions=archive['circle_predictions']
    reference_endpoint=archive['endpoint_prediction']
    rtol,atol=6.25e-5/4**args.level,6.25e-7/4**args.level
    t,step=0.,.05
    current_loss=loss(engine,state)
    times,losses,errors,steps=[t],[current_loss],[],[]
    snapshot_times=[0.]
    snapshot_predictions=[panel_predict(engine,state,snapshot_inputs)]
    matched_rms=[float(np.sqrt(np.mean((snapshot_predictions[0]-reference_predictions[0])**2)))]
    diagnostics=[]
    rejected=loss_increases=0
    start=last_report=time.monotonic()
    next_reference=1
    initial_defect=number(engine.defect_frobenius(state))
    while True:
        if current_loss<=.001*(1+1e-10):
            final_status='fit'; break
        if time.monotonic()-start>args.run_seconds:
            final_status='wall_limit'; break
        if len(steps)>=30000 or t>=10000:
            final_status='step_or_time_limit'; break
        proposed=min(step,2.,10000-t)
        if next_reference<len(reference_times):
            proposed=min(proposed,float(reference_times[next_reference])-t)
        if proposed<1e-9:
            final_status='step_underflow'; break
        try:
            first=engine.rhs(state)
            euler=state.add_scaled(first,proposed)
            second=engine.rhs(euler)
            candidate=linear_combination((1.,proposed/2,proposed/2),(state,first,second))
            err=error_ratio(engine,state,euler,candidate,rtol,atol)
            candidate_loss=loss(engine,candidate)
            valid=np.isfinite(err) and np.isfinite(candidate_loss)
        except (ValueError,FloatingPointError):
            err,valid=float('inf'),False
        if not valid or err>1:
            rejected+=1
            step=proposed*(max(.1,min(.5,.9/np.sqrt(err))) if np.isfinite(err) else .1)
            continue
        if candidate_loss<=.001:
            low,high=0.,1.
            for _ in range(32):
                fraction=(low+high)/2
                middle=linear_combination((1-fraction,fraction),(state,candidate))
                if loss(engine,middle)>.001: low=fraction
                else: high=fraction
            fraction=(low+high)/2
            candidate=linear_combination((1-fraction,fraction),(state,candidate))
            candidate_loss=loss(engine,candidate)
            proposed*=fraction
        loss_increases+=candidate_loss>current_loss+1e-12
        state,current_loss=candidate,candidate_loss
        t+=proposed
        times.append(t); losses.append(current_loss); errors.append(err); steps.append(proposed)
        step=proposed*max(.5,min(2.,.9/np.sqrt(max(err,1e-16))))
        if next_reference<len(reference_times) and abs(t-reference_times[next_reference])<1e-8:
            pred=panel_predict(engine,state,snapshot_inputs)
            snapshot_times.append(t); snapshot_predictions.append(pred)
            matched_rms.append(float(np.sqrt(np.mean((pred-reference_predictions[next_reference])**2))))
            next_reference+=1
        if len(steps)%25==0:
            diag={k:number(v) for k,v in engine.lift_diagnostics(state).items()}
            diag.update(time=t,activity=number(state.s),loss=current_loss,
                        defect_frobenius=number(engine.defect_frobenius(state)),residual_rms=np.sqrt(current_loss))
            diagnostics.append(diag)
        if time.monotonic()-last_report>=20:
            print(json.dumps(dict(event='progress',case=case,variant=args.variant,P=order,level=args.level,
                                  time=t,loss=current_loss,steps=len(steps),wall_seconds=time.monotonic()-start)),flush=True)
            last_report=time.monotonic()
    prediction=panel_predict(engine,state,panel)
    difference=prediction-reference_endpoint
    diag={k:number(v) for k,v in engine.lift_diagnostics(state).items()}
    diag.update(time=t,activity=number(state.s),loss=current_loss,
                defect_frobenius=number(engine.defect_frobenius(state)),residual_rms=np.sqrt(current_loss))
    diagnostics.append(diag)
    source_names=['run_moment_experiment.py','moment_engine.py']
    if args.variant=='orthogonal': source_names.append('orthogonal_moment_engine.py')
    summary=dict(case=case,variant=args.variant,P=order,level=args.level,lifted=state.lifted,width=2048,
                 sample_count=len(labels),status=final_status,time=t,training_mse=current_loss,
                 circle_rms=float(np.sqrt(np.mean(difference**2))),
                 circle_rms_4096=float(np.sqrt(np.mean(difference[::2]**2))),circle_max=float(np.max(np.abs(difference))),
                 activity=number(state.s),initial_defect=initial_defect,initial_match=initial_match,
                 diagnostics_final=diag,accepted=len(steps),rejected=rejected,loss_increases=int(loss_increases),
                 rtol=rtol,atol=atol,wall_seconds=time.monotonic()-start,
                 moving_scalars=sum(x.numel() for x in state.tensors()),fixed_W0_scalars=engine.W0.numel(),
                 history_rank_bound=order*len(labels),history_vectors=2*order*len(labels),
                 reference=str(archive_path.relative_to(ROOT)),
                 source_sha256={name:hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() for name in source_names})
    payload={name:value.cpu().numpy() for name,value in zip(state.names(),state.tensors())}
    np.savez_compressed(directory/'arrays.npz',**payload,training_inputs=inputs,labels=labels,
                        endpoint_angles=angles,endpoint_inputs=panel,endpoint_prediction=prediction,
                        times=np.asarray(times),losses=np.asarray(losses),local_error_ratios=np.asarray(errors),
                        accepted_steps=np.asarray(steps),snapshot_times=np.asarray(snapshot_times),
                        circle_predictions=np.asarray(snapshot_predictions),matched_time_rms=np.asarray(matched_rms))
    (directory/'diagnostics.json').write_text(json.dumps(diagnostics,indent=2)+'\n')
    (directory/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='complete',**summary)),flush=True)
    del engine,archive,state
    torch.cuda.empty_cache()

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',required=True)
    parser.add_argument('--cases',nargs='+',choices=list(REFERENCES),required=True)
    parser.add_argument('--orders',nargs='+',type=int,default=[1,3,7])
    parser.add_argument('--device',required=True)
    parser.add_argument('--level',type=int,default=0)
    parser.add_argument('--variant',choices=['bins','orthogonal'],default='orthogonal')
    parser.add_argument('--direct',action='store_true')
    parser.add_argument('--run-seconds',type=float,default=240)
    args=parser.parse_args()
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    for case in args.cases:
        for order in args.orders: run(args,case,order)

if __name__=='__main__': main()
