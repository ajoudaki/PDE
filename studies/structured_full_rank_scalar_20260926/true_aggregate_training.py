"""One bounded scalar-contraction training smoke; no passive-circle claim."""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_key]='1'
import hashlib
import json
from pathlib import Path
import signal
import sys
import time
import numpy as np
from scipy.integrate import RK45
from scipy.optimize import brentq
from circle_tasks import BY_NAME
from true_aggregate_ode import compile_closure
from true_aggregate_references import initial_block_pool

class BudgetReached(Exception):pass

def main():
    output=Path('data/generated/structured_full_rank_scalar_20260926/true_aggregate_quick_20260927/compiler')
    output.mkdir(parents=True,exist_ok=True)
    report_path=output/'train_pair_d9.json'
    if report_path.exists():raise FileExistsError('No reruns: smoke report already exists')
    task=BY_NAME['pair_cos1'];u,labels=task.data()
    all_start=time.monotonic()
    model=compile_closure(u,labels,k=4,order=1,degree=9,mark_bound=3.,seconds=60.,max_states=100000,max_terms=1000000)
    if not model.compiled:
        report_path.write_text(json.dumps({'stop_reason':'compile_limit','compile':model.report},indent=2)+'\n');return
    pool=initial_block_pool(1024,4,1,3.)
    pool_modifications={'entry_redraws':pool['entry_redraws'],'mark_bound':pool['mark_bound']}
    state,initialization=model.initialize_from_pool(pool)
    del pool
    prediction=model.prediction(state);mse=float(np.mean((prediction-labels)**2))
    initial_prediction=prediction.copy();initial_mse=mse
    bench=time.monotonic();model.rhs(0.,state);rhs_seconds=time.monotonic()-bench
    print(json.dumps({'phase':'initialized','compile':model.report,'initialization':initialization,'initial_mse':mse,'rhs_seconds':rhs_seconds}),flush=True)
    history=[[0.,mse,float(state[-1]),float(np.max(np.abs(state[:-1]))),float(np.mean(np.abs(state[:-1])>1))]]
    t=0.;nsteps=0;nfev=0;max_rise=0.;max_q=history[0][3];max_clip_rate=history[0][4];bracket=None;reason='time_cap'
    solver=None;start=time.monotonic();next_update=start+10
    def rhs(at,y):
        nonlocal nfev
        nfev+=1
        if time.monotonic()-start>=45.:raise BudgetReached()
        return model.rhs(at,y)
    def alarm(signum,frame):raise BudgetReached()
    old=signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,45.)
    try:
        if rhs_seconds>1.:
            reason='rhs_cost_gate'
        elif mse<=.01:
            reason='target'
        else:
            solver=RK45(rhs,0.,state,3000.,rtol=1e-5,atol=1e-7,first_step=.01,max_step=1.)
            while solver.status=='running':
                old_t=t;old_mse=mse
                solver.step()
                if solver.status=='failed':reason='solver_failed';break
                candidate=solver.y.copy();trial_prediction=model.prediction(candidate)
                trial_mse=float(np.mean((trial_prediction-labels)**2))
                if not np.all(np.isfinite(candidate)) or not np.isfinite(trial_mse):reason='nonfinite';break
                qmax=float(np.max(np.abs(candidate[:-1])))
                if qmax>2.0001:reason='moment_box_violation';break
                if trial_mse<=.01:
                    dense=solver.dense_output();bracket=[old_t,float(solver.t)]
                    root=brentq(lambda tau:float(np.mean((model.prediction(dense(tau))-labels)**2))-.01,*bracket,xtol=1e-12)
                    root=min(float(solver.t),root+1e-11*max(1.,root))
                    candidate=dense(root);trial_mse=float(np.mean((model.prediction(candidate)-labels)**2));t=float(root);reason='target'
                else:t=float(solver.t)
                state=candidate;mse=trial_mse;nsteps+=1
                max_rise=max(max_rise,mse-old_mse);qmax=float(np.max(np.abs(state[:-1])));max_q=max(max_q,qmax)
                clip_rate=float(np.mean(np.abs(state[:-1])>1.));max_clip_rate=max(max_clip_rate,clip_rate)
                history.append([t,mse,float(state[-1]),qmax,clip_rate])
                if time.monotonic()>=next_update:
                    print(json.dumps({'phase':'training','seconds':time.monotonic()-start,'physical_time':t,'mse':mse,'steps':nsteps,'nfev':nfev,'L':float(state[-1]),'max_q':qmax,'clipped_fraction':clip_rate}),flush=True)
                    next_update=time.monotonic()+10
                if reason=='target':break
    except BudgetReached:reason='training_wall_limit'
    except (FloatingPointError,OverflowError) as exc:reason=type(exc).__name__
    finally:
        signal.setitimer(signal.ITIMER_REAL,0.);signal.signal(signal.SIGALRM,old)
    train_seconds=time.monotonic()-start;prediction=model.prediction(state)
    reference_root=output.parent/'references';reference_info=json.loads((reference_root/'pair_cos1__gaussian.json').read_text())
    with np.load(reference_root/'pair_cos1__gaussian.npz',allow_pickle=False) as ref:
        gaussian_prediction=np.array(ref['train_prediction'])
    np.savez_compressed(output/'train_pair_d9.npz',state=state,history=np.asarray(history),train_prediction=prediction,train_labels=labels,initial_train_prediction=initial_prediction,gaussian_train_prediction=gaussian_prediction)
    report={'task':'pair_cos1','method':'genuine scalar tree contraction ODE','width_initial_pool':1024,'k':4,'order':1,'degree':9,'seed':1,'target_mse':.01,'compile':model.report,'initialization':initialization,'pool_modifications':pool_modifications,'rhs_seconds_single_benchmark':rhs_seconds,'initial_mse':initial_mse,'initial_prediction':initial_prediction.tolist(),'stop_reason':reason,'fitted':reason=='target' and mse<=.01*(1+1e-7),'physical_time':t,'train_mse':mse,'prediction':prediction.tolist(),'labels':labels.tolist(),'training_seconds':train_seconds,'nsteps':nsteps,'nfev':nfev,'max_loss_rise':max_rise,'target_bracket':bracket,'L':float(state[-1]),'final_max_abs_q':float(np.max(np.abs(state[:-1]))),'max_abs_q_accepted':max_q,'final_clipped_fraction':float(np.mean(np.abs(state[:-1])>1.)),'max_clipped_fraction_accepted':max_clip_rate,'history_columns':['physical_time','MSE','L','max_abs_q','fraction_outside_unit_box'],'history':history,'gaussian_train_prediction':gaussian_prediction.tolist(),'gaussian_train_mse':reference_info['train_mse'],'gaussian_physical_time':reference_info['physical_time'],'train_prediction_rms_vs_gaussian':float(np.sqrt(np.mean((prediction-gaussian_prediction)**2))),'comparison_scope':'Training inputs only; each endpoint has its own stop status. No circle result.','solver':{'method':'SciPy RK45','rtol':1e-5,'atol':1e-7,'first_step':.01,'max_step':1.,'time_cap':3000.,'wall_cap':45.,'error_norm':'RMS across all scalar states','dtype':'float64','blas_threads':1},'state_file':'train_pair_d9.npz','runtime_state':'normalized scalar contractions plus L; initial pool discarded','penalty_mode':model.penalty_mode,'total_seconds':time.monotonic()-all_start,'command':sys.argv,'sources':{name:hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() for name in ('true_aggregate_training.py','true_aggregate_ode.py','true_aggregate_references.py')}}
    report_path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:value for key,value in report.items() if key not in ('history','compile','sources')},indent=2),flush=True)

if __name__=='__main__':main()
