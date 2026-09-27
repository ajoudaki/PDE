"""Two preregistered complete-feedback dependency tests; no rescue sweeps."""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import json
from pathlib import Path
import pickle
import signal
import time
import numpy as np
from circle_tasks import directions
from geometry_tasks import TASKS
from next_dependency_closure import DependencyClosure
from run_selective_all_tasks import reference_comparison, resource_estimate
from run_true_aggregate_selective import BudgetReached, integrate
from selective_initialization_fast import initialize_shared_fast
from selective_runtime_fast import FastSharedQueryClosure
from true_aggregate_references import digest, initial_block_pool, write_json

SOURCE=Path(__file__).resolve().parent
ROOT=SOURCE.parent.parent
DEST=ROOT/'data/generated/structured_full_rank_scalar_20260926/next_dependency_20260927'
REFS=DEST.parent/'all_tasks_j2_20260927/references'

def alarm(signum,frame):
    raise BudgetReached('Preregistered stage wall cap')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task',required=True,choices=('pair_cos3','pair_orthogonal_cos1'))
    args=parser.parse_args()
    task={v.name:v for v in TASKS}[args.task]
    DEST.mkdir(parents=True,exist_ok=True)
    report_path=DEST/f'{task.name}.json'
    data_path=report_path.with_suffix('.npz')
    if report_path.exists() or data_path.exists():
        raise FileExistsError('No repeated training or overwritten result')
    report={'task':task.name,'method':'complete_feedback_dependency_depth1',
        'k':4,'P':1,'dependency_depth':1,'initial_width':1024,'seed':1,
        'mark_bound':3.,'target_mse':.001,'circle_grid':64,'train_angles':list(task.angles),
        'runtime_state':'aggregate contractions and clock; no initial blocks retained',
        'solver':{'rtol':1e-5,'atol':1e-7,'first_step':.01,'max_step':1.,'training_wall_cap':45.},
        'sources':{name:digest(SOURCE/name) for name in (
            'run_next_dependency.py','next_dependency_closure.py','NEXT_AGGREGATE_PROTOCOL.md',
            'true_aggregate_selective_fast.py','true_aggregate_selective.py','true_aggregate_ode.py',
            'selective_runtime_fast.py','selective_initialization_fast.py',
            'run_true_aggregate_selective.py','true_aggregate_references.py')}}
    started=time.monotonic()
    u,labels=task.data()
    report['train_labels']=labels.tolist()
    angles=2*np.pi*np.arange(64)/64
    queries=np.r_[angles,task.angles]
    previous=signal.signal(signal.SIGALRM,alarm)
    template=None
    compile_start=time.monotonic()
    signal.setitimer(signal.ITIMER_REAL,30.)
    try:
        template=DependencyClosure(u,labels,k=4,order=1,queries=np.vstack((u,directions([.123])[0])),
            mark_bound=3.,depth=1)
        template.compile(seconds=max(.001,30.-(time.monotonic()-compile_start)),
                         max_states=50000,max_terms=1000000)
        report['compile']=template.report
    except BudgetReached:
        report['compile']={'complete':False,'status':'wall_cap',
                           'states':len(getattr(template,'trees',()))}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0.)
    report['compile_seconds']=time.monotonic()-compile_start
    if not report['compile']['complete']:
        report.update(fitted=False,stop_reason='compile_cap',training_seconds=0.)
        write_json(report_path,report)
        print(json.dumps(report),flush=True)
        return
    resources=resource_estimate(template,len(queries))
    report['resources']=resources
    if resources['total_dynamic_scalars']>500000 or not resources['passed']:
        report.update(fitted=False,stop_reason='state_memory_cap',training_seconds=0.)
        write_json(report_path,report)
        print(json.dumps(report),flush=True)
        return
    with (DEST/f'{task.name}.pkl').open('xb') as handle:
        pickle.dump(template,handle,pickle.HIGHEST_PROTOCOL)
    report['template_sha256']=digest(DEST/f'{task.name}.pkl')
    model=FastSharedQueryClosure(template,queries)
    report['state_counts']={'shared_core':model.ncore,'passive_per_query':model.npassive,
                            'total_dynamic_scalars':model.size}
    report['passive_independence']=model.check_independence()
    report['vectorization']=model.check_vectorization()
    print(json.dumps({'phase':'compiled','task':task.name,**report['state_counts']}),flush=True)
    signal.setitimer(signal.ITIMER_REAL,60.)
    try:
        pool=initial_block_pool(1024,4,1,3.)
        initial,report['initialization']=initialize_shared_fast(model,pool)
        report['initial_pool_entry_redraws']=pool['entry_redraws']
        del pool
    except BudgetReached:
        report.update(fitted=False,stop_reason='initialization_cap',training_seconds=0.)
        write_json(report_path,report)
        print(json.dumps(report),flush=True)
        return
    finally:
        signal.setitimer(signal.ITIMER_REAL,0.)
        signal.signal(signal.SIGALRM,previous)
    report['initial_alias_max_gap']=float(np.max(np.abs(model.circle_prediction(initial)[64:]-model.prediction(initial))))
    print(json.dumps({'phase':'initialized','task':task.name,
                      'seconds':report['initialization']['seconds']}),flush=True)
    state,history,info=integrate(model,initial,labels,45.,target=.001)
    report.update(info)
    pred=model.prediction(state)
    passive=model.circle_prediction(state)
    gap=passive[64:]-pred
    report.update(train_mse=float(np.mean((pred-labels)**2)),
        passive_train_mse=float(np.mean((passive[64:]-labels)**2)),
        train_prediction=pred.tolist(),alias_gap_max=float(np.max(np.abs(gap))),
        alias_gap_rms=float(np.sqrt(np.mean(gap**2))),
        endpoint_status='fitted' if report['fitted'] else 'partial versus fitted controls')
    for name,suffix in [('block','block_k4_P1_canonical'),('gaussian','gaussian')]:
        report[name+'_comparison']=reference_comparison(REFS/f'{task.name}__{suffix}.npz',
            angles,passive[:64],pred,passive[64:],report['fitted'])
    np.savez_compressed(data_path,state=state,initial_state=initial,history=history,
        angles=angles,prediction=passive[:64],all_query_angles=queries,
        all_passive_prediction=passive,train_prediction=pred,alias_gap=gap,
        train_labels=labels,core_ids=model.core_ids,passive_ids=model.passive_ids,
        template_Fids=template.Fids)
    report.update(data_file=str(data_path),data_sha256=digest(data_path),
                  total_seconds=time.monotonic()-started)
    write_json(report_path,report)
    print(json.dumps(report,allow_nan=False),flush=True)

if __name__=='__main__':
    main()
