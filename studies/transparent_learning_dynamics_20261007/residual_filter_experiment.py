"""Fixed numerical-repair campaign; no changed data, model, or fitted parameter."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
import numpy as np
from multisample_experiment import dataset,initialize,fields,observe,step,json_default
from causal_filtered_integrator import simulate_population,filter_deficit

ROOT=Path('data/generated/transparent_learning_dynamics_20261007/residual_filter_v1')
STUDY=Path(__file__).resolve().parent


def filtered_dense_step(state,vectors,labels,h):
    p=fields(state,vectors);m=len(labels);n=len(state[2])
    c=labels-p['f'][:m]
    c1=p['h1'][:,:m].T@p['h1'][:,:m]/n
    c2=p['h2'][:,:m].T@p['h2'][:,:m]/n
    d1=p['d1'][:,:m].T@p['d1'][:,:m]/n
    d2=p['d2'][:,:m].T@p['d2'][:,:m]/n
    kernel=c2+c1*d2+(vectors[:m]@vectors[:m].T)*d1
    write,defect=filter_deficit(kernel,c,h)
    velocity=(p['d1'][:,:m]*write)@vectors[:m]
    matrix_velocity=(p['d2'][:,:m]*write)@p['h1'][:,:m].T/n
    w_velocity=p['h2'][:,:m]@write
    updated=tuple(x+h*v for x,v in zip(state,(velocity,matrix_velocity,w_velocity)))
    return updated,write,defect


def dense(n,seed,h,method):
    m=16;vectors,labels=dataset(m);state=initialize(n,8,seed);p0=fields(state,vectors)
    steps=round(19.2/h);records=[];writes=[];defects=[]
    for k in range(steps+1):
        records.append(observe(state,vectors,labels,p0,'full',None))
        if k<steps:
            if method=='filtered':
                state,write,defect=filtered_dense_step(state,vectors,labels,h)
                writes.append(write);defects.append(defect)
            elif method=='rk4':state=step(state,vectors,labels,h*m/2,'rk4','full',None)
            else:raise ValueError('Unsupported method')
            if not all(np.isfinite(x).all() for x in state):raise FloatingPointError(f'Nonfinite step {k}')
    arrays={key:np.array([r[key] for r in records]) for key in records[0]}
    arrays.update(time=np.arange(steps+1)*h*m/2,normalized_time=np.arange(steps+1)*h,
                  vectors=vectors,labels=labels,write_deficit=np.array(writes))
    return arrays,dict(maximum_solve_defect=max(defects,default=0.))


def causal(n,seed,h,method):
    if method!='filtered':raise ValueError('Only the filtered full law is in this campaign')
    m=16;vectors,labels=dataset(m);steps=round(19.2/h)
    result=simulate_population(labels,dt=h*m/2,steps=steps,population_size=n,
        seed=seed,input_vectors=vectors,memory_limit_mb=11500)
    i=np.arange(steps+1)
    arrays=dict(time=result['time'],normalized_time=np.arange(steps+1)*h,
        f=result['f'],c=result['c'],write_deficit=result['write_deficit'],
        loss=np.mean(result['c']**2,axis=1),c1=result['C']['layer1'][i,i],
        c2=result['C']['layer2'][i,i],kernel=result['kernel_diagnostic'],
        C1=result['C']['layer1'],C2=result['C']['layer2'],
        D1=result['D']['layer1'],D2=result['D']['layer2'],
        Rh=result['R']['h'],Rdelta=result['R']['delta'],vectors=vectors,labels=labels)
    for layer in (1,2):
        history=result['C'][f'layer{layer}']
        arrays[f'motion{layer}']=np.diagonal(history[i,i],axis1=1,axis2=2)+np.diag(history[0,0])[None,:]-2*np.diagonal(history[:,0],axis1=1,axis2=2)
    return arrays,result['diagnostics']


def selftest():
    from multisample_experiment import rhs,add
    vectors,labels=dataset(16);state=initialize(23,8,91)
    state=(state[0],state[1],np.linspace(-.2,.3,23))
    p=fields(state,vectors);h=.01
    out,write,_=filtered_dense_step(state,vectors,labels,h)
    vel=tuple((a-b)/h for a,b in zip(out,state))
    eps=1e-5
    deriv=(fields(add(state,vel,eps),vectors)['f']-fields(add(state,vel,-eps),vectors)['f'])/(2*eps)
    contraction_error=float(np.max(abs((labels-p['f'][:16])-h*deriv[:16]-write)))
    errors=[]
    normalized_rhs=tuple(v*8 for v in rhs(state,vectors,labels))
    for size in (1e-3,5e-4,2.5e-4):
        updated,_,_=filtered_dense_step(state,vectors,labels,size)
        errors.append(max(float(np.max(abs((a-b)/size-v))) for a,b,v in zip(updated,state,normalized_rhs)))
    altered=vectors.copy();altered[16:]=np.roll(altered[16:],1,axis=1)
    passive=filtered_dense_step(state,altered,labels,h)[0]
    passive_error=max(float(np.max(abs(a-b))) for a,b in zip(out,passive))
    assert contraction_error<1e-8 and passive_error==0 and .45<errors[1]/errors[0]<.55 and .45<errors[2]/errors[1]<.55
    return dict(linearized_residual_error=contraction_error,consistency_velocity_errors=errors,
                passive_exclusion_error=passive_error)


def run(kind,n,seed,h,method,replicate=False):
    records=[json.loads(p.read_text()) for p in ROOT.glob('*/record.json')]
    used=sum(r['wall_seconds'] for r in records)
    if used>=1800:raise RuntimeError('30-minute numerical budget exhausted')
    if sum(r['config']['kind']==kind for r in records)>=(16 if kind=='dense' else 8):
        raise RuntimeError('Scientific run budget exhausted')
    config=dict(kind=kind,m=16,n=n,seed=seed,normalized_step=h,method=method,replicate=replicate)
    name=f'{kind}_m16_n{n}_s{seed}_h{h}_{method}'+('_replicate' if replicate else '')
    dest=ROOT/name;dest.mkdir(parents=True,exist_ok=False)
    source_names=['residual_filter_experiment.py','multisample_experiment.py','causal_filtered_integrator.py',
                  'causal_panel_simulator.py','causal_population_simulator.py']
    hashes={name:hashlib.sha256((STUDY/name).read_bytes()).hexdigest() for name in source_names}
    requested=dict(config=config,command=sys.argv,cwd=str(Path.cwd()),source_sha256=hashes,
                   numpy=np.__version__,threads=1,precision='float64')
    (dest/'requested.json').write_text(json.dumps(requested,indent=2)+'\n')
    def timeout(signum,frame):raise TimeoutError('Remaining campaign wall budget reached')
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,1800-used)
    started=time.perf_counter()
    try:
        arrays,diagnostics=(dense if kind=='dense' else causal)(n,seed,h,method)
        elapsed=time.perf_counter()-started
        signal.setitimer(signal.ITIMER_REAL,0)
        assert hashes=={name:hashlib.sha256((STUDY/name).read_bytes()).hexdigest() for name in source_names}
        relative=arrays['loss']/arrays['loss'][0]
        increase=max(0.,float(np.max(np.diff(relative))))
        np.savez_compressed(dest/'trajectory.npz',**arrays)
        record=dict(**requested,wall_seconds=elapsed,exit_status=0,diagnostics=diagnostics,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            maximum_relative_loss_increase=increase,loss_increasing_steps=int(np.sum(np.diff(relative)>1e-12)),
            final_relative_loss=float(relative[-1]),numerically_unstable=increase>.001)
        (dest/'record.json').write_text(json.dumps(record,default=json_default,indent=2)+'\n')
        print(json.dumps({k:record[k] for k in ('config','wall_seconds','final_relative_loss','maximum_relative_loss_increase','peak_rss_kib')}),flush=True)
    except Exception as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        record=dict(**requested,wall_seconds=time.perf_counter()-started,exit_status=1,error=repr(exc),
                    peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (dest/'record.json').write_text(json.dumps(record,indent=2)+'\n')
        raise


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('kind',choices=('dense','causal','selftest'))
    p.add_argument('--n',type=int,default=512);p.add_argument('--seed',type=int,default=101)
    p.add_argument('--h',type=float,default=.2);p.add_argument('--method',choices=('filtered','rk4'),default='filtered')
    p.add_argument('--replicate',action='store_true');args=p.parse_args()
    if args.kind=='selftest':print(json.dumps(selftest(),indent=2))
    else:run(args.kind,args.n,args.seed,args.h,args.method,args.replicate)
