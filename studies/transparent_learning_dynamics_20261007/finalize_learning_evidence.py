"""Final manifest and the predeclared additional population-size check."""
import hashlib
import json
from pathlib import Path
import numpy as np
from compare_causal_experiment import ROOT,load,obs,mean_sem


def main():
    large=load('causal_N8192_s{seed}_a06_dt0.4_full',(1701,1702))
    previous=load('causal_N4096_s{seed}_a06_dt0.4_full',(1701,1702))
    dense=load('euler_n1024_s{seed}_a06_dt0.4',(101,202,303,404))
    lm,ls=mean_sem(np.array([obs(r) for r in large]))
    pm=np.mean([obs(r) for r in previous],0)
    dm=np.mean([obs(r) for r in dense],0)
    metadata=[json.loads(p.read_text()) for p in ROOT.glob('*/record.json')]
    result=dict(population8192_endpoint=lm[-1].tolist(),population8192_endpoint_sem=ls[-1].tolist(),
                max_population4096_to8192_change=abs(lm-pm).max(0).tolist(),
                max_dense_mean_discrepancy=abs(lm-dm).max(0).tolist(),
                max_prediction_mean_discrepancy=float(np.max(abs(np.mean([r['f'] for r in large],0)-np.mean([r['f'] for r in dense],0)))),
                dense_runs=sum('width' in x for x in metadata),causal_runs=sum('config' in x for x in metadata),
                trajectory_wall_seconds=sum(r['wall_seconds'] for r in metadata),
                maximum_peak_rss_kib=max(r['peak_rss_kib'] for r in metadata),
                interpretation='Two-run refinement; not a bias or convergence-rate certificate.')
    dest=ROOT/'final_manifest';dest.mkdir(exist_ok=False)
    (dest/'refinement.json').write_text(json.dumps(result,indent=2)+'\n')
    files=sorted(ROOT.glob('*/record.json'))+sorted(ROOT.glob('*/trajectory.npz'))
    files+=list(ROOT.glob('*/summary.json'))+[ROOT/'passive_quadrature'/'coefficients.json',dest/'refinement.json']
    source=Path(__file__).parent
    files+=list(source.glob('*experiment*.py'))+[source/'causal_population_simulator.py',source/'passive_clock_quadrature.py',source/'compare_passive_clock.py',Path(__file__)]
    manifest={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (dest/'sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
