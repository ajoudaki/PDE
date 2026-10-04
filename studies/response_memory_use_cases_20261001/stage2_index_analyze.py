"""Deterministic analysis of every preregistered indexing fit."""
import argparse
import json
from pathlib import Path
import numpy as np


def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    batches={s:json.loads((args.root/f'stage2_index_{s}_v1'/'results.json').read_text())
             for s in ['pilot','confirm','adapt','refine']}
    allresults=[r for rows in batches.values() for r in rows]
    assert len(allresults)==99 and all(r['status']=='complete' and r['finite'] for r in allresults)
    rows={}
    for domain in ['fashion','har','housing']:
        subset=[r for r in batches['confirm']+batches['adapt'] if r['config']['domain']==domain]
        factor={r['config']['seed']:r for r in subset if r['config']['kind']=='factor'}
        for kind in ['field','factor','projected','dense','retro','write']:
            selected=[r for r in subset if r['config'].get('refresh',r['config']['kind'])==kind]
            errors=np.array([r['selected']['test'] for r in selected]);seeds=[r['config']['seed'] for r in selected]
            ratios=errors/np.array([factor[s]['selected']['test'] for s in seeds])
            rows[domain,kind]=dict(domain=domain,method=kind,median_test_rmse=float(np.median(errors)),
                                 median_paired_factor_ratio=float(np.median(ratios)),
                                 factor_wins=int(sum(ratios<1)),test_rmse=errors.tolist(),
                                 seeds=seeds,median_seconds=float(np.median([r['seconds'] for r in selected])),
                                 selected_times=[r['selected']['time'] for r in selected],
                                 median_feature_movement=np.median([r['feature_movement'] for r in selected],axis=0).tolist(),
                                 moving_scalars=selected[0]['moving_scalars'],fixed_base_scalars=selected[0]['fixed_base_scalars'],
                                 dictionary_scalars=selected[0]['dictionary_scalars'],cached_basis_scalars=selected[0]['cached_basis_scalars'])
    gates={}
    for kind in ['field','retro','write']:
        rr=[rows[d,kind] for d in ['fashion','har','housing']]
        passes=[r['median_paired_factor_ratio']<=.95 and r['factor_wins']>=3 for r in rr]
        gates[kind]=dict(pass_practical=sum(passes)>=2 and all(r['median_paired_factor_ratio']<=1.05 for r in rr),
                         domains_passing_5pct=[r['domain'] for r,p in zip(rr,passes) if p])
    refinements=[]
    for r in batches['refine']:
        config=r['config'];base=next(v for v in batches['confirm'] if all(v['config'][k]==config[k] for k in ['domain','seed','kind']))
        change=abs(r['selected']['test']-base['selected']['test'])
        domain=config['domain'];field=next(v for v in batches['confirm'] if v['config']['domain']==domain and v['config']['seed']==201 and v['config']['kind']=='field')
        factor=next(v for v in batches['confirm'] if v['config']['domain']==domain and v['config']['seed']==201 and v['config']['kind']=='factor')
        advantage=abs(field['selected']['test']-factor['selected']['test'])
        refinements.append(dict(domain=domain,kind=config['kind'],rmse_change=change,absolute_gap=advantage,
                                below_third_gap=change<advantage/3,selected_time_same=r['selected']['time']==base['selected']['time']))
    summary=dict(fits=99,fit_seconds=sum(r['seconds'] for r in allresults),rows=list(rows.values()),
                 practical_gates=gates,refinements=refinements,
                 capture_checks={s:json.loads((args.root/f'stage2_index_{s}_v1'/'capture_checks.json').read_text()) for s in batches})
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,3,figsize=(11,3.5),layout='constrained')
    methods=['field','retro','write','projected','dense']
    for ax,domain in zip(axes,['fashion','har','housing']):
        for j,kind in enumerate(methods):
            r=rows[domain,kind];ratios=np.array(r['test_rmse'])/np.array(rows[domain,'factor']['test_rmse'])
            ax.scatter(np.full(4,j)+np.linspace(-.12,.12,4),ratios,s=20)
            ax.plot([j-.24,j+.24],[np.median(ratios)]*2,color='black',lw=2)
        ax.axhline(1,color='gray',lw=1);ax.axhline(.95,color='gray',lw=.8,ls='--')
        ax.set_xticks(range(5),['Fixed','Transport','Write-time','Projected','Dense'],rotation=35,ha='right')
        ax.set_title(domain);ax.set_ylabel('Test RMSE / tuned factors')
    fig.savefig(args.out/'stage2_index_comparison.png',dpi=180)


if __name__=='__main__':main()
