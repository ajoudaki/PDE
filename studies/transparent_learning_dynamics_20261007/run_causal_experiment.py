"""Frozen bounded population cohort; save raw arrays and execution provenance."""
import argparse
import hashlib
import json
import resource
from pathlib import Path

import numpy as np
from causal_population_simulator import simulate_population, _json_default


ROOT=Path('data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1')


def run(n,seed,amplitude,dt=.4,mode='full',rank_rtol=1e-12):
    tag={.15:'015',.6:'06'}[amplitude]
    name=f'causal_N{n}_s{seed}_a{tag}_dt{dt}_{mode}'
    if rank_rtol!=1e-12:name+=f'_rtol{rank_rtol}'
    dest=ROOT/name
    dest.mkdir(parents=True,exist_ok=False)
    source=Path(__file__).with_name('causal_population_simulator.py')
    source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
    config=dict(population_size=n,seed=seed,labels=[amplitude,-amplitude],
                dt=dt,steps=round(24/dt),reciprocal_correction=mode!='no_reciprocal',
                learned_middle_memory=mode!='no_middle',rank_rtol=rank_rtol)
    (dest/'requested.json').write_text(json.dumps(config,indent=2)+'\n')
    result=simulate_population(**config)
    if hashlib.sha256(source.read_bytes()).hexdigest()!=source_hash:
        raise RuntimeError('Source changed during run')
    i=np.arange(config['steps']+1)
    np.savez_compressed(dest/'trajectory.npz',time=result['time'],f=result['f'],c=result['c'],
                        c1=result['C']['layer1'][i,i],c2=result['C']['layer2'][i,i],
                        C1=result['C']['layer1'],C2=result['C']['layer2'],
                        D1=result['D']['layer1'],D2=result['D']['layer2'],
                        Rh=result['R']['h'],Rdelta=result['R']['delta'],
                        loss=np.mean(result['c']**2,axis=1))
    record=dict(config=config,source_sha256=source_hash,numpy=np.__version__,
                wall_seconds=result['diagnostics']['timing']['total_seconds'],
                peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                diagnostics=result['diagnostics'])
    (dest/'record.json').write_text(json.dumps(record,default=_json_default,indent=2)+'\n')
    print(json.dumps(dict(run=name,seconds=record['wall_seconds'],
                          final_f=result['f'][-1].tolist(),
                          dc1=float(result['C']['layer1'][-1,-1,0,1]-result['C']['layer1'][0,0,0,1]),
                          dc2=float(result['C']['layer2'][-1,-1,0,1]-result['C']['layer2'][0,0,0,1]),
                          covariance_error=max(record['diagnostics'][v]['maximum_covariance_error'] for v in ('eta','xi')))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('cohort',choices=('full','refine','ablate','rank'))
    args=p.parse_args()
    if args.cohort=='full':
        for a in (.15,.6):
            for n,seeds in ((1024,(1701,1702)),(4096,(1701,1702,1703))):
                for seed in seeds:run(n,seed,a)
    elif args.cohort=='refine':
        for a in (.15,.6):
            for seed in (1701,1702):run(1024,seed,a,dt=.2)
    elif args.cohort=='ablate':
        for mode in ('no_reciprocal','no_middle'):
            for seed in (1701,1702,1703):run(4096,seed,.6,mode=mode)
    else:run(4096,1701,.6,rank_rtol=1e-14)
