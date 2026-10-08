"""Phase-2 frozen causal simulator cohorts; arbitrary training geometry."""
import argparse
import hashlib
import json
import resource
from pathlib import Path

import numpy as np

from causal_population_simulator import simulate_population, _json_default
from dense_response_phase2 import ROOT, setup


def run(n,seed,case,dt=.4,mode='full'):
    name=f'causal_{case}_N{n}_s{seed}_dt{dt}_{mode}'
    dest=ROOT/name
    dest.mkdir(parents=True,exist_ok=False)
    paths=[Path(__file__),Path(__file__).with_name('causal_population_simulator.py'),
           Path(__file__).with_name('dense_response_phase2.py')]
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    v,y,coef=setup(case)
    config=dict(population_size=n,seed=seed,labels=y.tolist(),input_vectors=v.T.tolist(),
                dt=dt,steps=round(24/dt),reciprocal_correction=mode!='no_reciprocal',
                rank_rtol=1e-12,memory_limit_mb=3072)
    (dest/'requested.json').write_text(json.dumps(config,indent=2)+'\n')
    result=simulate_population(**config)
    assert hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    i=np.arange(config['steps']+1)
    u=np.concatenate([np.zeros((1,2)),dt*np.cumsum(result['c'][:-1],axis=0)])
    ordered=np.concatenate([np.zeros((1,2,2)),
                            dt*np.cumsum(result['c'][:-1,:,None]*u[:-1,None,:],axis=0)])
    np.savez_compressed(dest/'trajectory.npz',time=result['time'],f=result['f'],c=result['c'],
                        c1=result['C']['layer1'][i,i],c2=result['C']['layer2'][i,i],
                        C1=result['C']['layer1'],C2=result['C']['layer2'],
                        D1=result['D']['layer1'],D2=result['D']['layer2'],
                        Rh=result['R']['h'],Rdelta=result['R']['delta'],
                        u=u,ordered=ordered,area=ordered[:,0,1]-ordered[:,1,0],
                        passive_defect=result['f'][:,2]-result['f'][:,:2]@coef,
                        loss=np.mean(result['c']**2,axis=1),
                        vectors=v.T,labels=y,passive_coefficients=coef)
    record=dict(config=config,source_sha256=hashes,numpy=np.__version__,
                wall_seconds=result['diagnostics']['timing']['total_seconds'],
                peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                diagnostics=result['diagnostics'])
    (dest/'record.json').write_text(json.dumps(record,default=_json_default,indent=2)+'\n')
    print(json.dumps(dict(run=name,seconds=record['wall_seconds'],
                          final_f=result['f'][-1].tolist(),area=float(ordered[-1,0,1]-ordered[-1,1,0]),
                          dc1=float(result['C']['layer1'][-1,-1,0,1]-result['C']['layer1'][0,0,0,1]),
                          dc2=float(result['C']['layer2'][-1,-1,0,1]-result['C']['layer2'][0,0,0,1]))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('cohort',choices=('main','refine','ablate'))
    args=p.parse_args()
    if args.cohort=='main':
        for case in ('A','B'):
            for seed in (1701,1702,1703):run(4096,seed,case)
    elif args.cohort=='refine':
        for case in ('A','B'):
            for dt in (.4,.2):
                for seed in (1701,1702):run(1024,seed,case,dt=dt)
    else:
        for seed in (1701,1702):run(4096,seed,'B',mode='no_reciprocal')
