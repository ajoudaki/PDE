"""Matched-mesh empirical comparison; envelopes are diagnostics, not CIs."""
import json
from pathlib import Path
import numpy as np

ROOT=Path('data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1')


def load(template,seeds):
    return [dict(np.load(ROOT/template.format(seed=s)/'trajectory.npz')) for s in seeds]


def obs(r):
    return np.column_stack((r['c1'][:,0,1]-r['c1'][0,0,1],
                            r['c2'][:,0,1]-r['c2'][0,0,1],r['f'][:,2]))


def mean_sem(arr):
    return arr.mean(0),arr.std(0,ddof=1)/np.sqrt(len(arr))


def main():
    summary={}
    for tag in ('015','06'):
        dense=load(f'euler_n1024_s{{seed}}_a{tag}_dt0.4',(101,202,303,404))
        lower=load(f'euler_n512_s{{seed}}_a{tag}_dt0.4',(101,202,303,404))
        pop=load(f'causal_N4096_s{{seed}}_a{tag}_dt0.4_full',(1701,1702,1703))
        popsmall=load(f'causal_N1024_s{{seed}}_a{tag}_dt0.4_full',(1701,1702))
        popfine=load(f'causal_N1024_s{{seed}}_a{tag}_dt0.2_full',(1701,1702))
        dm,ds=mean_sem(np.array([obs(r) for r in dense]))
        pm,ps=mean_sem(np.array([obs(r) for r in pop]))
        low=np.mean([obs(r) for r in lower],0)
        small=np.mean([obs(r) for r in popsmall],0)
        fine=np.mean([obs(r)[::2] for r in popfine],0)
        discrepancy=np.abs(pm-dm)
        # Predeclared sampling/refinement/width envelope, not simultaneous
        # statistical coverage and not a bound on unknown population bias.
        envelope=3*np.sqrt(ds*ds+ps*ps)+abs(small-pm)+abs(low-dm)
        densef=np.array([r['f'] for r in dense]);popf=np.array([r['f'] for r in pop])
        pairs=[float(np.max(abs(densef[i]-densef[j]))) for i in range(4) for j in range(i)]
        summary[tag]=dict(dense_endpoint=dm[-1].tolist(),dense_endpoint_sem=ds[-1].tolist(),
                          population_endpoint=pm[-1].tolist(),population_endpoint_sem=ps[-1].tolist(),
                          max_mean_discrepancy=discrepancy.max(0).tolist(),
                          maximum_envelope_excess=np.maximum(discrepancy-envelope,0).max(0).tolist(),
                          population_refinement_max_change=abs(small-pm).max(0).tolist(),
                          dense_width_refinement_max_change=abs(low-dm).max(0).tolist(),
                          population_step_refinement_max_change=abs(fine-small).max(0).tolist(),
                          prediction_grid_max_mean_discrepancy=float(np.max(abs(densef.mean(0)-popf.mean(0)))),
                          dense_pairwise_prediction_grid_max_errors=pairs,
                          dense_pairwise_mean=float(np.mean(pairs)))
    full=load('causal_N4096_s{seed}_a06_dt0.4_full',(1701,1702,1703))
    fullarr=np.array([obs(r) for r in full])
    for mode in ('no_reciprocal','no_middle'):
        runs=load(f'causal_N4096_s{{seed}}_a06_dt0.4_{mode}',(1701,1702,1703))
        data=np.array([obs(r) for r in runs]);mean,sem=mean_sem(data)
        diff=data-fullarr;diffm,diffs=mean_sem(diff)
        summary[mode]=dict(endpoint=mean[-1].tolist(),endpoint_sem=sem[-1].tolist(),
                           paired_difference=diffm[-1].tolist(),paired_difference_sem=diffs[-1].tolist(),
                           final_training_residual_max=float(max(np.max(abs(r['c'][-1])) for r in runs)))
    densefreeze=load('euler_frozen_middle_n512_s{seed}_a06_dt0.4',(101,202,303,404))
    summary['frozen_middle_dense_endpoint']=np.mean([obs(r)[-1] for r in densefreeze],0).tolist()
    base=full[0]
    refined=dict(np.load(ROOT/'causal_N4096_s1701_a06_dt0.4_full_rtol1e-14'/'trajectory.npz'))
    summary['rank_tolerance_change']={key:float(np.max(abs(base[key]-refined[key]))) for key in ('f','c1','c2')}
    records=[json.loads(p.read_text()) for p in ROOT.glob('*/record.json')]
    causal=[r for r in records if 'config' in r]
    summary['execution']=dict(dense_count=sum('width' in r for r in records),causal_count=len(causal),
                              wall_seconds=sum(r['wall_seconds'] for r in records),
                              maximum_peak_rss_kib=max(r['peak_rss_kib'] for r in records),
                              max_covariance_error=max(r['diagnostics'][family]['maximum_covariance_error'] for r in causal for family in ('eta','xi')),
                              max_discarded_variance=max(r['diagnostics'][family]['maximum_discarded_variance'] for r in causal for family in ('eta','xi')))
    dest=ROOT/'comparison_v1';dest.mkdir(exist_ok=False)
    (dest/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
