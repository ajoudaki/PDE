"""Fixed 4/8/16-sample tests of the unchanged causal feature-response law.

Every scientific run has fresh outputs and a frozen configuration. Population
particle count is separate from dense width. Passive rows never supply labels.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
import numpy as np

ROOT=Path('data/generated/transparent_learning_dynamics_20261007/multisample_v1')
STUDY=Path(__file__).resolve().parent


def dataset(m):
    if m not in (4,8,16):raise ValueError('Only predeclared training sizes')
    centers=np.zeros((4,8))
    centers[0,0]=1
    centers[1,:2]=[.55,np.sqrt(1-.55**2)]
    centers[2,:3]=[-.35,.45,np.sqrt(1-.35**2-.45**2)]
    centers[3,:4]=[.2,-.4,.5,np.sqrt(1-.2**2-.4**2-.5**2)]
    rng=np.random.default_rng(6201)
    noise=rng.normal(size=(16,8));noise/=np.linalg.norm(noise,axis=1,keepdims=True)
    training=centers[np.arange(16)%4]+.65*noise
    training/=np.linalg.norm(training,axis=1,keepdims=True)
    signs=np.array([[1,-1,1,-1],[1,1,-1,-1],[-1,-1,1,1],[1,-1,-1,1]]).ravel()
    labels=signs[:m]*(.25+.075*((5*np.arange(m))%7))
    passive=np.array([training[0]+training[1],training[0]-.6*training[1],
                      training[2]+training[3],np.array([0.,0.,0.,0.,1.,1.,-1.,0.])])
    passive/=np.linalg.norm(passive,axis=1,keepdims=True)
    return np.concatenate([training[:m],passive]),labels


def initialize(n,d,seed):
    rng=np.random.default_rng(seed)
    return rng.normal(size=(n,d)),rng.normal(size=(n,n))/np.sqrt(n),np.zeros(n)


def fields(state,vectors,frozen=None):
    a,matrix,w=state
    z1=a@vectors.T
    if frozen is None:h1=np.tanh(z1);g1=1-h1*h1
    else:h1=frozen['h1']+frozen['g1']*(z1-frozen['z1']);g1=frozen['g1']
    z2=matrix@h1
    if frozen is None:h2=np.tanh(z2);g2=1-h2*h2
    else:h2=frozen['h2']+frozen['g2']*(z2-frozen['z2']);g2=frozen['g2']
    d2=w[:,None]*g2;d1=g1*(matrix.T@d2)
    return dict(z1=z1,h1=h1,g1=g1,z2=z2,h2=h2,g2=g2,d1=d1,d2=d2,f=w@h2/len(w))


def rhs(state,vectors,labels,mode='full',frozen=None):
    p=fields(state,vectors,frozen);m=len(labels);n=len(state[2]);c=labels-p['f'][:m]
    scale=2/m
    da=scale*((p['d1'][:,:m]*c)@vectors[:m])
    dwmat=(scale/n)*(p['d2'][:,:m]*c)@p['h1'][:,:m].T
    dw=scale*p['h2'][:,:m]@c
    if mode=='frozen_middle':dwmat.fill(0)
    return da,dwmat,dw


def add(state,velocity,dt):return tuple(x+dt*y for x,y in zip(state,velocity))


def step(state,vectors,labels,dt,method,mode,frozen):
    args=(vectors,labels,mode,frozen)
    k1=rhs(state,*args)
    if method=='euler':return add(state,k1,dt)
    k2=rhs(add(state,k1,dt/2),*args);k3=rhs(add(state,k2,dt/2),*args)
    k4=rhs(add(state,k3,dt),*args)
    return tuple(x+dt*(a+2*b+2*c+d)/6 for x,a,b,c,d in zip(state,k1,k2,k3,k4))


def initial_curvature(state,vectors,labels,mode='full'):
    p=fields(state,vectors);m=len(labels);n=len(state[2]);scale=2/m
    q=scale*p['h2'][:,:m]@labels
    top=p['g2'][:,:m]*q[:,None]
    lower=p['g1'][:,:m]*(state[1].T@top)
    aacc=scale*(lower*labels)@vectors[:m]
    j1=p['g1']*(aacc@vectors.T)
    middle=(scale/n)*(top*labels)@(p['h1'][:,:m].T@p['h1'])
    if mode=='frozen_middle':middle.fill(0)
    j2=p['g2']*(middle+state[1]@j1)
    return np.array([(j.T@p[f'h{l}']+p[f'h{l}'].T@j)/n for l,j in ((1,j1),(2,j2))])


def observe(state,vectors,labels,p0,mode,frozen):
    p=fields(state,vectors,frozen);n=len(state[2]);m=len(labels);c=labels-p['f'][:m]
    c1=p['h1'].T@p['h1']/n;c2=p['h2'].T@p['h2']/n
    d1=p['d1'].T@p['d1']/n;d2=p['d2'].T@p['d2']/n
    kb=np.array([c2,c1*d2,(vectors@vectors.T)*d1])
    if mode=='frozen_middle':kb[1]=0
    return dict(f=p['f'],c1=c1,c2=c2,loss=np.mean(c*c),kernel_blocks=kb,
                motion1=np.mean((p['h1']-p0['h1'])**2,axis=0),
                motion2=np.mean((p['h2']-p0['h2'])**2,axis=0),
                gate_change1=np.mean((p['g1']-p0['g1'])**2,axis=0),
                gate_change2=np.mean((p['g2']-p0['g2'])**2,axis=0),
                loss_derivative=-4/(m*m)*float(c@kb[:,:m,:m].sum(0)@c))


def dense(m,n,seed,normalized_step=.4,method='euler',mode='full'):
    vectors,labels=dataset(m);dt=normalized_step*m/2;steps=round(19.2/normalized_step)
    state=initialize(n,vectors.shape[1],seed);p0=fields(state,vectors)
    frozen=p0 if mode=='affine_gates' else None
    curvature=initial_curvature(state,vectors,labels,mode)
    records=[]
    for k in range(steps+1):
        records.append(observe(state,vectors,labels,p0,mode,frozen))
        if k<steps:
            state=step(state,vectors,labels,dt,method,mode,frozen)
            if not all(np.isfinite(x).all() for x in state):raise FloatingPointError(f'Nonfinite step{k}')
    arrays={key:np.array([r[key] for r in records]) for key in records[0]}
    arrays.update(time=np.arange(steps+1)*dt,normalized_time=np.arange(steps+1)*normalized_step,
                  initial_curvature=curvature,vectors=vectors,labels=labels)
    return arrays,{}


def causal(m,n,seed,normalized_step=.4,method='euler',mode='full'):
    from causal_panel_simulator import simulate_population
    vectors,labels=dataset(m);dt=normalized_step*m/2;steps=round(19.2/normalized_step)
    if method!='euler':raise ValueError('Causal implementation uses Euler')
    result=simulate_population(labels,dt=dt,steps=steps,population_size=n,seed=seed,
        input_vectors=vectors,learned_middle_memory=mode!='no_middle',
        reciprocal_correction=mode!='no_reciprocal',memory_limit_mb=11500)
    i=np.arange(steps+1)
    arrays=dict(time=result['time'],normalized_time=np.arange(steps+1)*normalized_step,
                f=result['f'],loss=np.mean(result['c']**2,axis=1),c=result['c'],
                c1=result['C']['layer1'][i,i],c2=result['C']['layer2'][i,i],
                C1=result['C']['layer1'],C2=result['C']['layer2'],
                D1=result['D']['layer1'],D2=result['D']['layer2'],
                Rh=result['R']['h'],Rdelta=result['R']['delta'],vectors=vectors,labels=labels)
    for layer in (1,2):
        history=result['C'][f'layer{layer}']
        arrays[f'motion{layer}']=np.diagonal(history[i,i],axis1=1,axis2=2)+np.diag(history[0,0])[None,:]-2*np.diagonal(history[:,0],axis1=1,axis2=2)
    return arrays,result['diagnostics']


def self_test():
    m=4;v,y=dataset(m);state=initialize(19,8,71)
    state=(state[0],state[1],np.linspace(-.15,.2,19))
    p=fields(state,v);vel=rhs(state,v,y);eps=1e-5
    plus=fields(add(state,vel,eps),v)['f'];minus=fields(add(state,vel,-eps),v)['f']
    obs=observe(state,v,y,p,'full',None)
    fdot=(2/m)*obs['kernel_blocks'].sum(0)[:,:m]@(y-p['f'][:m])
    derivative_error=float(np.max(abs((plus-minus)/(2*eps)-fdot)))
    loss_derivative=(np.mean((plus[:m]-y)**2)-np.mean((minus[:m]-y)**2))/(2*eps)
    loss_error=abs(loss_derivative-obs['loss_derivative'])
    initial=initialize(19,8,71);p0=fields(initial,v);q=(2/m)*p0['h2'][:,:m]@y
    sp=(initial[0],initial[1],eps*q);sm=(initial[0],initial[1],-eps*q)
    # Residual derivative is nonzero, but multiplies zero initial hidden force;
    # the hidden velocity derivative below therefore gives its exact acceleration.
    vp=rhs(sp,v,y);vm=rhs(sm,v,y)
    aacc=(vp[0]-vm[0])/(2*eps);wacc=(vp[1]-vm[1])/(2*eps)
    j1=p0['g1']*(aacc@v.T);j2=p0['g2']*(wacc@p0['h1']+initial[1]@j1)
    numeric=np.array([(j.T@p0[f'h{l}']+p0[f'h{l}'].T@j)/19 for l,j in ((1,j1),(2,j2))])
    curvature_error=float(np.max(abs(numeric-initial_curvature(initial,v,y))))
    # Changing passive input cannot change finite dense training updates.
    vv=v.copy();vv[m:]=np.roll(vv[m:],1,axis=1)
    passive_error=max(float(np.max(abs(a-b))) for a,b in zip(rhs(state,v,y),rhs(state,vv,y)))
    assert derivative_error<1e-8 and loss_error<1e-8 and curvature_error<1e-8 and passive_error<1e-12
    return dict(fdot_error=derivative_error,loss_derivative_error=loss_error,
                initial_curvature_error=curvature_error,passive_exclusion_error=passive_error)


def json_default(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,np.generic):return value.item()
    raise TypeError(type(value).__name__)


def run(kind,m,n,seed,normalized_step=.4,method='euler',mode='full'):
    if ROOT.exists():
        records=[json.loads(p.read_text()) for p in ROOT.glob('*/record.json')]
        if sum(r['wall_seconds'] for r in records)>=2700:raise RuntimeError('Campaign wall budget exhausted')
        count=sum(r['config']['kind']==kind for r in records)
        if count>=(30 if kind=='dense' else 22):raise RuntimeError('Campaign run budget exhausted')
    name=f'{kind}_m{m}_n{n}_s{seed}_h{normalized_step}_{method}_{mode}'
    dest=ROOT/name;dest.mkdir(parents=True,exist_ok=False)
    config=dict(kind=kind,m=m,n=n,seed=seed,normalized_step=normalized_step,method=method,mode=mode)
    sources=[Path(__file__)]
    if kind=='causal':sources += [STUDY/'causal_panel_simulator.py',STUDY/'causal_population_simulator.py']
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    requested=dict(config=config,command=sys.argv,cwd=str(Path.cwd()),source_sha256=hashes,
                   numpy=np.__version__,threads=1,precision='float64')
    (dest/'requested.json').write_text(json.dumps(requested,indent=2)+'\n')
    started=time.perf_counter()
    try:
        arrays,diagnostics=(dense if kind=='dense' else causal)(m,n,seed,normalized_step,method,mode)
        elapsed=time.perf_counter()-started
        assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
        np.savez_compressed(dest/'trajectory.npz',**arrays)
        record=dict(**requested,wall_seconds=elapsed,diagnostics=diagnostics,exit_status=0,
                    peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (dest/'record.json').write_text(json.dumps(record,default=json_default,indent=2)+'\n')
        print(json.dumps(dict(run=name,seconds=elapsed,peak_mib=record['peak_rss_kib']/1024,
            final_relative_loss=float(arrays['loss'][-1]/arrays['loss'][0]),
            layer1_drift=float(np.max(abs(arrays['c1']-arrays['c1'][0]))),
            layer2_drift=float(np.max(abs(arrays['c2']-arrays['c2'][0]))))),flush=True)
    except Exception as exc:
        record=dict(**requested,wall_seconds=time.perf_counter()-started,exit_status=1,error=repr(exc),
                    peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        (dest/'record.json').write_text(json.dumps(record,indent=2)+'\n')
        raise


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('kind',choices=('dense','causal','selftest'))
    p.add_argument('--m',type=int,default=4);p.add_argument('--n',type=int,default=512)
    p.add_argument('--seed',type=int,default=101);p.add_argument('--h',type=float,default=.4)
    p.add_argument('--method',choices=('euler','rk4'),default='euler')
    p.add_argument('--mode',choices=('full','no_reciprocal','no_middle','frozen_middle','affine_gates'),default='full')
    args=p.parse_args()
    if args.kind=='selftest':print(json.dumps(self_test(),indent=2))
    else:run(args.kind,args.m,args.n,args.seed,args.h,args.method,args.mode)
