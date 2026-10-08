"""Initialization-direction continuation and non-predictive direction diagnostics.

Phase 3: all predictors use only initial arrays and an autonomous cubic clock.
Measured-clock and best-projection outputs are explicitly oracle diagnostics.
Frozen earlier simulators are imported, never modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import time

for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))

import numpy as np
from numpy.polynomial.hermite import hermgauss
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp
import scipy

from dense_learning_experiment import initialize,fields,V,rhs as prior_rhs


ROOT=Path('data/generated/transparent_learning_dynamics_20261007/gate_continuation_v1')
MIX=np.array([2.,1.])/np.sqrt(5)
RULES={k:leggauss(k) for k in (32,64)}


def contrast(h):return h[...,2]-h[...,:2]@MIX


def population_constants():
    x,p=hermgauss(160);x=x*np.sqrt(2);p=p/np.sqrt(np.pi)
    hx=np.tanh(x);gx=1-hx*hx
    sigma2=p@(hx*hx);qx=p@(gx*gx);taux=p@(hx*hx*gx*gx)
    h=np.tanh(np.sqrt(sigma2)*x);g=1-h*h
    nu=p@(h*h);alpha=p@g;beta=p@(g*g);tau=p@(h*h*g*g)
    lam=(sigma2+qx)*tau+(3*beta-2*alpha)**2*taux
    mu=(sigma2+qx)*nu*beta+sigma2*qx*alpha**4
    return float(nu),float(2*(lam+mu)/3)


def initial_directions(initial,sign):
    p=fields(initial);n=len(initial[2]);ell=np.array([1.,float(sign)])
    q=p['h2'][:,:2]@ell
    upper_return=q[:,None]*p['g2'][:,:2]
    lower_return=p['g1'][:,:2]*(initial[1].T@upper_return)
    aacc=(lower_return*ell)@V[:,:2].T
    wacc=(upper_return*ell)@p['h1'][:,:2].T/n
    z1acc=aacc@V
    j1=p['g1']*z1acc
    middle=(upper_return*ell)@(p['h1'][:,:2].T@p['h1']/n)
    lower=initial[1]@j1
    z2acc=middle+lower
    j2=p['g2']*z2acc
    r=j2[:,:2]@ell
    defect0=contrast(p['h2']);defectj=contrast(j2)
    e1=float(q@defect0/n)
    e3=float(q@defectj/(2*n)+r@defect0/(6*n))
    e5=float(r@defectj/(12*n))
    finite_nu=float(q@q/(2*n));finite_kappa=float(q@r/(3*n))
    energy=float((np.sum(aacc*aacc)/n+np.sum(wacc*wacc))/3)
    return dict(p=p,z1acc=z1acc,z2acc=z2acc,middle=middle,lower=lower,
                j1=j1,j2=j2,Q=q,R=r,e1=e1,e3=e3,e5=e5,
                finite_nu=finite_nu,finite_kappa=finite_kappa,
                acceleration_energy=energy,aacc=aacc,wacc=wacc)


def continued_fields(u,initial,sign,order=32):
    z=initial['p']['z2'];acc=initial['z2acc']
    h=np.tanh(z+.5*u*u*acc)
    nodes,weights=RULES[order]
    coordinate=u*(nodes+1)/2
    hh=np.tanh(z[:,:2,None]+.5*acc[:,:2,None]*coordinate[None,None,:]**2)
    w=(u/2)*(hh[:,0,:]+sign*hh[:,1,:])@weights
    return h,w


def predictions(u,initial,sign,nu,kappa,order=32):
    h,w=continued_fields(u,initial,sign,order)
    defect=float(w@contrast(h)/len(w))
    cubic=initial['e1']*u+initial['e3']*u**3
    product=cubic+initial['e5']*u**5
    geometric=(2+sign)/np.sqrt(5)*(nu*u+kappa*u**3)
    return np.array([geometric+cubic,geometric+product,geometric+defect]),h,w


def augmented_rhs(state,labels):
    p=fields(state[:3]);c=labels-p['f'][:2];n=len(state[2])
    return ((p['d1'][:,:2]*c)@V[:,:2].T,
            (p['d2'][:,:2]*c)@p['h1'][:,:2].T/n,
            p['h2'][:,:2]@c,c)


def add(state,derivative,scale):return tuple(x+scale*y for x,y in zip(state,derivative))


def step(state,labels,dt):
    k1=augmented_rhs(state,labels)
    k2=augmented_rhs(add(state,k1,dt/2),labels)
    k3=augmented_rhs(add(state,k2,dt/2),labels)
    k4=augmented_rhs(add(state,k3,dt),labels)
    return tuple(x+dt*(a+2*b+2*c+d)/6 for x,a,b,c,d in zip(state,k1,k2,k3,k4))


def displacement_diagnostics(displacement,direction,u):
    norm2=np.mean(displacement*displacement,axis=0)
    direction2=np.mean(direction*direction,axis=0)
    cross=np.mean(displacement*direction,axis=0)
    coefficient=np.divide(cross,direction2,out=np.zeros_like(cross),where=direction2>0)
    projected=direction*coefficient
    orthogonal=displacement-projected
    quadratic=.5*u*u*direction
    return dict(rms=np.sqrt(norm2),projection=coefficient,
                orthogonal_rms=np.sqrt(np.mean(orthogonal*orthogonal,axis=0)),
                quadratic_error_rms=np.sqrt(np.mean((displacement-quadratic)**2,axis=0)),
                cosine=np.divide(cross,np.sqrt(norm2*direction2),
                                 out=np.zeros_like(cross),where=norm2*direction2>0)),projected


def observe(state,initial,sign,nu,kappa,amplitude):
    p=fields(state[:3]);n=len(state[2]);ell=np.array([1.,float(sign)])
    u=float(state[3]@ell/2)
    mismatch=float((state[3][0]-sign*state[3][1])/2)
    pred,hhat,what=predictions(u,initial,sign,nu,kappa)
    fine,_,_=predictions(u,initial,sign,nu,kappa,64)
    hpoly=initial['p']['h2']+.5*u*u*initial['j2']
    wpoly=u*initial['Q']+u**3*initial['R']/6
    arrays={}
    for layer in (1,2):
        diag,projected=displacement_diagnostics(p[f'z{layer}']-initial['p'][f'z{layer}'],
                                                initial[f'z{layer}acc'],u)
        arrays.update({f'layer{layer}_{key}':value for key,value in diag.items()})
        if layer==2:oracle_h=np.tanh(initial['p']['z2']+projected)
    fhat=what@hhat/n
    defecthat=float(what@contrast(hhat)/n)
    split_f=np.array([state[2]@(p['h2']-hhat)/n,(state[2]-what)@hhat/n])
    split_e=np.array([state[2]@(contrast(p['h2'])-contrast(hhat))/n,
                       (state[2]-what)@contrast(hhat)/n])
    actualdefect=float(contrast(p['f']))
    fpoly=wpoly@hpoly/n
    return dict(f=p['f'],u=state[3],mode_clock=u,asymmetric_clock=mismatch,
                prediction_measured_clock=pred,quadrature_error=float(max(abs(fine-pred))),
                raw_continuation_f=fhat,raw_continuation_defect=defecthat,
                raw_polynomial_f=fpoly,raw_polynomial_defect=float(contrast(fpoly)),
                actual_defect=actualdefect,error_split_f=split_f,error_split_defect=split_e,
                actual_readout_feature_error=state[2]@(p['h2']-hhat)/n,
                actual_readout_projected_feature_error=state[2]@(p['h2']-oracle_h)/n,
                actual_readout_polynomial_feature_error=state[2]@(p['h2']-hpoly)/n,
                actual_readout_defect_error=float(state[2]@(contrast(p['h2'])-contrast(hhat))/n),
                actual_readout_projected_defect_error=float(state[2]@(contrast(p['h2'])-contrast(oracle_h))/n),
                readout_rms=np.sqrt(np.mean(state[2]**2)),
                readout_error_rms=np.sqrt(np.mean((state[2]-what)**2)),
                loss=np.mean((np.array([1.,sign])*amplitude-p['f'][:2])**2),
                identity_error=max(float(np.max(abs(split_f.sum(0)-(p['f']-fhat)))),
                    abs(float(split_e.sum())-(actualdefect-defecthat)),
                    abs(float(contrast(fpoly))-(initial['e1']*u+initial['e3']*u**3+initial['e5']*u**5))),
                **arrays)


def simulate(n,seed,amplitude=.6,sign=-1,dt=.1,horizon=24.):
    initial=initialize(n,seed);fixed=initial_directions(initial,sign)
    labels=amplitude*np.array([1.,float(sign)])
    nu,kappa=population_constants();times=np.arange(round(horizon/dt)+1)*dt
    sol=solve_ivp(lambda t,u:amplitude-nu*u-kappa*u**3,(0,horizon),[0.],t_eval=times,
                  rtol=1e-11,atol=1e-13)
    assert sol.success
    autonomous_u=sol.y[0]
    # Both independent predictions are generated BEFORE dense training.
    autonomous=np.array([predictions(float(u),fixed,sign,nu,kappa)[0] for u in autonomous_u])
    refined=np.array([predictions(float(u),fixed,sign,nu,kappa,64)[0] for u in autonomous_u])
    state=(*initial,np.zeros(2));records=[]
    for k in range(len(times)):
        records.append(observe(state,fixed,sign,nu,kappa,amplitude))
        if k<len(times)-1:
            state=step(state,labels,dt)
            if not all(np.isfinite(x).all() for x in state):raise FloatingPointError('nonfinite dense state')
    arrays={key:np.array([r[key] for r in records]) for key in records[0]}
    arrays.update(time=times,autonomous_clock=autonomous_u,prediction_autonomous=autonomous,
                  autonomous_quadrature_error=abs(refined-autonomous).max(1))
    scalar={key:float(fixed[key]) for key in ('e1','e3','e5','finite_nu','finite_kappa','acceleration_energy')}
    scalar.update(nu=nu,kappa=kappa)
    return arrays,scalar


def self_test():
    maximum=0.;kappa_error=0.
    for sign in (-1,1):
        state=initialize(19,71);fixed=initial_directions(state,sign)
        ell=np.array([1.,float(sign)]);eps=1e-4
        plus=(state[0],state[1],eps*fixed['Q'])
        minus=(state[0],state[1],-eps*fixed['Q'])
        vp=prior_rhs(plus,fields(plus)['f'][:2]+ell)
        vm=prior_rhs(minus,fields(minus)['f'][:2]+ell)
        maximum=max(maximum,float(np.max(abs((vp[0]-vm[0])/(2*eps)-fixed['aacc']))),
                    float(np.max(abs((vp[1]-vm[1])/(2*eps)-fixed['wacc']))))
        kappa_error=max(kappa_error,abs(fixed['finite_kappa']-fixed['acceleration_energy']))
        for u in (.001,.1,.7):
            h= fixed['p']['h2']+.5*u*u*fixed['j2'];w=u*fixed['Q']+u**3*fixed['R']/6
            maximum=max(maximum,abs(float(w@contrast(h)/19)-(fixed['e1']*u+fixed['e3']*u**3+fixed['e5']*u**5)))
    assert maximum<1e-10 and kappa_error<1e-10
    return dict(initial_acceleration_and_polynomial_error=maximum,
                positive_cubic_energy_identity_error=kappa_error)


def run(n,seed,amplitude=.6,sign=-1,dt=.1,replication=False):
    tag=f'a{amplitude}_s{sign}'
    name=f'n{n}_seed{seed}_{tag}_dt{dt}'+('_reproduce' if replication else '')
    dest=ROOT/name;dest.mkdir(parents=True,exist_ok=False)
    files=[Path(__file__),Path(__file__).with_name('dense_learning_experiment.py')]
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    config=dict(n=n,seed=seed,amplitude=amplitude,sign=sign,dt=dt,horizon=24.)
    requested=dict(config=config,command=' '.join(os.sys.argv),cwd=str(Path.cwd()),
                   source_sha256=hashes,threads=1,precision='float64')
    (dest/'requested.json').write_text(json.dumps(requested,indent=2)+'\n')
    started=time.perf_counter();arrays,constants=simulate(**config);elapsed=time.perf_counter()-started
    assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    np.savez_compressed(dest/'trajectory.npz',**arrays)
    errors=np.max(abs(arrays['prediction_autonomous']-arrays['f'][:,2,None]),axis=0)
    record=dict(**requested,constants=constants,wall_seconds=elapsed,
                peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                numpy=np.__version__,scipy=scipy.__version__,exit_status=0,
                max_passive_error=errors.tolist(),max_identity_error=float(max(arrays['identity_error'])),
                max_quadrature_error=float(max(np.max(arrays['autonomous_quadrature_error']),np.max(arrays['quadrature_error']))))
    (dest/'record.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(run=name,seconds=elapsed,passive=float(arrays['f'][-1,2]),
                         predictions=arrays['prediction_autonomous'][-1].tolist(),
                         max_passive_errors=errors.tolist(),
                         upper_cosine=arrays['layer2_cosine'][-1].tolist(),
                         quadrature_error=record['max_quadrature_error'])),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('cohort',choices=('selftest','main','refine','reproduce'))
    args=parser.parse_args()
    if args.cohort=='selftest':print(json.dumps(self_test(),indent=2))
    elif args.cohort=='main':
        for amplitude,sign in ((.15,-1),(.6,-1),(.6,1)):
            for seed in (101,202,303):run(512,seed,amplitude,sign)
        for seed in (101,202):run(1024,seed)
    elif args.cohort=='refine':run(1024,101,dt=.05)
    else:run(512,101,replication=True)
