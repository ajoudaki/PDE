"""Unequal-residual experiments with same-path passive source attribution.

Own phase-2 implementation; phase-1 source is frozen. All arrays float64.
Companion residual integrals and source attributions use the same RK stages.
Attributions partition instantaneous velocities, not counterfactual effects.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import resource
import time
from pathlib import Path

import numpy as np

from dense_learning_experiment import initialize


ROOT = Path('data/generated/transparent_learning_dynamics_20261007/unequal_residuals_v1')


def setup(case):
    vectors = np.array([[1., 0.], [.6, .8] if case == 'B' else [0., 1.],
                        [2 / np.sqrt(5), 1 / np.sqrt(5)]])
    labels = np.array([.6, -.6 if case == 'symmetric' else -.3])
    coefficients = np.linalg.solve(vectors[:2].T, vectors[2])
    return vectors.T, labels, coefficients


def fields(state, v, frozen=None):
    a, matrix, w = state[:3]
    z1 = a @ v
    if frozen is None:
        h1 = np.tanh(z1)
        g1 = 1 - h1*h1
    else:
        h1 = frozen['h1'] + frozen['g1']*(z1-frozen['z1'])
        g1 = frozen['g1']
    z2 = matrix @ h1
    if frozen is None:
        h2 = np.tanh(z2)
        g2 = 1 - h2*h2
    else:
        h2 = frozen['h2'] + frozen['g2']*(z2-frozen['z2'])
        g2 = frozen['g2']
    d2 = w[:, None]*g2
    b1 = matrix.T @ d2
    d1 = g1*b1
    return dict(z1=z1, h1=h1, g1=g1, z2=z2, h2=h2, g2=g2,
                d1=d1, d2=d2, b1=b1, f=w@h2/len(w))


def contrast(value, coefficients):
    return value[..., 2] - value[..., :2] @ coefficients


def velocities(state, v, labels, coefficients, initial_fields, mode):
    frozen = initial_fields if mode == 'affine_gates' else None
    p = fields(state, v, frozen)
    n = len(state[2])
    c = labels - p['f'][:2]
    da = (p['d1'][:, :2]*c) @ v[:, :2].T
    dwmat = (p['d2'][:, :2]*c) @ p['h1'][:, :2].T/n
    dw = p['h2'][:, :2] @ c
    if mode in ('frozen_middle', 'frozen_features'):
        dwmat.fill(0)
    if mode == 'frozen_features':
        da.fill(0)
    dh1 = p['g1']*(da@v)
    middle = ((p['d2'][:, :2]*c) @ (p['h1'][:, :2].T@p['h1']/n)
              if mode not in ('frozen_middle', 'frozen_features')
              else np.zeros_like(p['h1']))
    lower = state[1] @ dh1
    block_fdot = np.array([dw@p['h2']/n,
                           state[2]@(p['g2']*middle)/n,
                           state[2]@(p['g2']*lower)/n])
    gate_drift = p['g2']-initial_fields['g2']
    gate_rates = np.array([state[2]@(gate_drift*middle)/n,
                            state[2]@(gate_drift*lower)/n])
    source_rates = contrast(block_fdot, coefficients)
    original_readout = dw@contrast(initial_fields['h2'], coefficients)/n
    derivative = (da, dwmat, dw, c, np.outer(c, state[3]),
                  source_rates, contrast(gate_rates, coefficients),
                  np.array([original_readout]))
    return derivative, p, dict(dh1=dh1, middle=middle, lower=lower,
                               block_fdot=block_fdot, source_rates=source_rates)


def add(state, velocity, factor):
    return tuple(x+factor*y for x, y in zip(state, velocity))


def step(state, dt, method, *args):
    k1 = velocities(state, *args)[0]
    if method == 'euler':
        return add(state, k1, dt)
    k2 = velocities(add(state, k1, dt/2), *args)[0]
    k3 = velocities(add(state, k2, dt/2), *args)[0]
    k4 = velocities(add(state, k3, dt), *args)[0]
    return tuple(x+dt*(a+2*b+2*c+d)/6
                 for x,a,b,c,d in zip(state,k1,k2,k3,k4))


def observe(state, args):
    v, labels, coefficients, initial_fields, mode = args
    velocity, p, extra = velocities(state, *args)
    n = len(state[2])
    c1, c2 = (p['h1'].T@p['h1']/n, p['h2'].T@p['h2']/n)
    d1, d2 = (p['d1'].T@p['d1']/n, p['d2'].T@p['d2']/n)
    blocks = np.array([c2, c1*d2, (v.T@v)*d1])
    if mode in ('frozen_middle','frozen_features'):
        blocks[1] = 0
    if mode == 'frozen_features':
        blocks[2] = 0
    c = labels-p['f'][:2]
    q1, q2 = contrast(p['h1'], coefficients), contrast(p['h2'], coefficients)
    passive_split = np.array([state[2]@initial_fields['h2'][:,2]/n,
                              state[2]@(p['h2'][:,2]-initial_fields['h2'][:,2])/n])
    upper_velocities = np.array([p['g2']*extra['middle'],p['g2']*extra['lower']])
    gram2_rates = np.array([(z.T@p['h2']+p['h2'].T@z)/n
                            for z in upper_velocities])
    kernel_rate = blocks[:, :, :2]@c
    u, ordered = state[3:5]
    # q1 can also be differentiated by subtracting the three feature velocities.
    lower_defect_rate = contrast(extra['dh1'], coefficients)
    direct_lower = sum(coefficients[b]*(p['g1'][:,2]-p['g1'][:,b])*
                       (velocity[0]@v[:,b]) for b in range(2))
    return dict(f=p['f'],c1=c1,c2=c2,kernel_blocks=blocks,
                loss=np.mean(c*c),u=u,ordered=ordered,
                area=ordered[0,1]-ordered[1,0],
                source_integrals=state[5],gate_drift_integrals=state[6],
                initial_readout_integral=state[7][0],
                source_rates=extra['source_rates'],block_fdot=extra['block_fdot'],
                passive_defect=contrast(p['f'],coefficients),passive_split=passive_split,
                defect_rms=np.sqrt([np.mean(q1*q1),np.mean(q2*q2)]),
                gram2_rates=gram2_rates,
                motion1=np.mean((p['h1']-initial_fields['h1'])**2,axis=0),
                motion2=np.mean((p['h2']-initial_fields['h2'])**2,axis=0),
                gate_change=np.array([np.mean((p[k]-initial_fields[k])**2,axis=0)
                                       for k in ('g1','g2')]),
                identities=np.array([np.max(abs(kernel_rate-extra['block_fdot'])),
                                      abs(contrast(p['f'],coefficients)-state[2]@q2/n),
                                      np.max(abs(direct_lower-lower_defect_rate))]),
                integrated_source_defect=contrast(p['f'],coefficients)-sum(state[5]),
                ordered_identity_error=np.max(abs(ordered+ordered.T-np.outer(u,u))))


def simulate(n, seed, case='A',dt=.1,method='rk4',mode='full',horizon=24.):
    v,labels,coefficients=setup(case)
    initial=initialize(n,seed)
    p0=fields(initial,v)
    state=(*initial,np.zeros(2),np.zeros((2,2)),np.zeros(3),np.zeros(2),np.zeros(1))
    args=(v,labels,coefficients,p0,mode)
    count=round(horizon/dt)
    assert abs(count*dt-horizon)<1e-10
    observations=[]
    for k in range(count+1):
        observations.append(observe(state,args))
        if k<count:
            state=step(state,dt,method,*args)
            if not all(np.isfinite(x).all() for x in state):
                raise FloatingPointError(f'nonfinite state at step {k}')
    arrays={key:np.array([o[key] for o in observations]) for key in observations[0]}
    arrays['time']=np.arange(count+1)*dt
    arrays['vectors']=v.T
    arrays['labels']=labels
    arrays['passive_coefficients']=coefficients
    return arrays


def self_test():
    import dense_learning_experiment as old
    maximum=0.
    finite_difference=0.
    for case in ('A','B','symmetric'):
        v,y,coef=setup(case)
        initial=initialize(17,71)
        p0=fields(initial,v)
        state=(*initial,np.zeros(2),np.zeros((2,2)),np.zeros(3),np.zeros(2),np.zeros(1))
        for mode in ('full','frozen_middle','affine_gates'):
            args=(v,y,coef,p0,mode)
            for _ in range(3):
                state=step(state,.07,'rk4',*args)
            obs=observe(state,args)
            maximum=max(maximum,float(max(obs['identities'])))
            vel=velocities(state,*args)[0]
            frozen=p0 if mode=='affine_gates' else None
            eps=1e-5
            plus=fields(add(state,vel,eps),v,frozen)['f']
            minus=fields(add(state,vel,-eps),v,frozen)['f']
            finite_difference=max(finite_difference,float(np.max(abs(
                (plus-minus)/(2*eps)-obs['block_fdot'].sum(0)))))
    a=simulate(17,91,'symmetric',.1,horizon=.5)
    b=old.simulate(17,91,.6,-1,.5,.1)
    old_error=max(float(np.max(abs(a[k]-b[k]))) for k in ('f','c1','c2','kernel_blocks'))
    assert maximum<1e-12 and finite_difference<1e-9 and old_error<1e-12
    return dict(identity_error=maximum,fdot_centered_difference=finite_difference,
                phase1_implementation_match=old_error)


def run(n,seed,case,dt=.1,method='rk4',mode='full'):
    name=f'dense_{case}_n{n}_s{seed}_dt{dt}_{method}_{mode}'
    dest=ROOT/name
    dest.mkdir(parents=True,exist_ok=False)
    paths=[Path(__file__),Path(__file__).with_name('dense_learning_experiment.py')]
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    config=dict(n=n,seed=seed,case=case,dt=dt,method=method,mode=mode,horizon=24.)
    (dest/'requested.json').write_text(json.dumps(config,indent=2)+'\n')
    started=time.perf_counter()
    arrays=simulate(**config)
    elapsed=time.perf_counter()-started
    assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    np.savez_compressed(dest/'trajectory.npz',**arrays)
    record=dict(config=config,source_sha256=hashes,wall_seconds=elapsed,
                peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                numpy=np.__version__,identity_max=float(np.max(arrays['identities'])))
    (dest/'record.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(run=name,seconds=elapsed,final_f=arrays['f'][-1].tolist(),
                          area=float(arrays['area'][-1]),
                          sources=arrays['source_integrals'][-1].tolist(),
                          source_integration_error=float(max(abs(arrays['integrated_source_defect']))))),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('cohort',choices=('selftest','main','refine','euler','passive'))
    args=parser.parse_args()
    if args.cohort=='selftest':
        print(json.dumps(self_test(),indent=2))
    elif args.cohort=='main':
        for case in ('A','B'):
            for n in (512,1024):
                for seed in (101,202,303):run(n,seed,case)
    elif args.cohort=='refine':
        for case in ('A','B'):run(1024,101,case,dt=.05)
    elif args.cohort=='euler':
        for case in ('A','B'):
            for seed in (101,202,303):run(1024,seed,case,dt=.4,method='euler')
    else:
        for mode in ('full','frozen_middle','affine_gates'):
            for seed in (101,202):run(512,seed,'symmetric',mode=mode)
