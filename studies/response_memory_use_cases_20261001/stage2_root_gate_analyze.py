"""Recompute the root safeguard and mechanism diagnostics from frozen outputs."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser();p.add_argument('--base',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    base=args.base
    rows=json.loads((base/'stage2_root_gate01/results.json').read_text())
    summary={'source_sha256':sha(Path(__file__)),'input_sha256':sha(base/'stage2_root_gate01/results.json'),
             'fits':len(rows),'seconds':sum(r['seconds'] for r in rows),'domains':{},'refinements':[]}
    for domain in ['fashion','har','housing']:
        original=[r for r in rows if r['domain']==domain and r['dt']==1/32]
        by={(r['seed'],r['kind']):r for r in original}
        entry={'methods':{}}
        for method in ['field','gated','factor']:
            group=[r for r in original if r['kind']==method]
            entry['methods'][method]={'median_test_rmse':float(np.median([r['selected']['test'] for r in group])),
                'median_train_rmse':float(np.median([r['selected']['train'] for r in group])),
                'per_seed_test_rmse':[r['selected']['test'] for r in group]}
            if method!='factor':
                entry['methods'][method]['hidden_ascent_fractions']=[r['diagnostics']['sampled_hidden_ascent_fraction'] for r in group]
                entry['methods'][method]['actual_loss_ascent_fractions']=[r['diagnostics']['sampled_actual_loss_ascent_fraction'] for r in group]
                entry['methods'][method]['mean_gate']=[r['diagnostics']['mean_gate'] for r in group]
        for other in ['field','factor']:
            ratios=[by[(s,'gated')]['selected']['test']/by[(s,other)]['selected']['test'] for s in [4101,4102,4103]]
            entry['gated_to_'+other]={'ratios':ratios,'median':float(np.median(ratios)),'wins':int(sum(v<1 for v in ratios))}
        entry['practical_domain_pass']=all(entry['gated_to_'+other]['median']<=.95 and entry['gated_to_'+other]['wins']==3 for other in ['field','factor'])
        summary['domains'][domain]=entry
        for method in ['field','gated']:
            old=by[(4101,method)]
            new=next(r for r in rows if r['domain']==domain and r['kind']==method and r['dt']==1/64)
            summary['refinements'].append({'domain':domain,'kind':method,'old_selected_time':old['selected']['time'],
                'new_selected_time':new['selected']['time'],'test_rmse_change':abs(old['selected']['test']-new['selected']['test'])})
    summary['practical_gate_pass']=sum(v['practical_domain_pass'] for v in summary['domains'].values())>=2 and all(
        max(v['gated_to_field']['median'],v['gated_to_factor']['median'])<=1.05 for v in summary['domains'].values())
    summary['decomposition']={}
    fig,axes=plt.subplots(1,3,figsize=(12,3.6),constrained_layout=True)
    for ax,domain in zip(axes,['fashion','har','housing']):
        path=next(p for p in (base/'stage2_root_gate_diagnostics01').glob('fit_*/result.json') if json.loads(p.read_text())['domain']==domain)
        arraypath=path.with_name('arrays.npz');arr=np.load(arraypath)['metrics']
        summary['decomposition'][domain]={'arrays_sha256':sha(arraypath),'positive_hidden_fraction':float(np.mean(arr[:,3]>0)),
            'positive_spatial_fraction':float(np.mean(arr[:,7]>0)),'positive_lag_fraction':float(np.mean(arr[:,8]>0)),
            'max_identity_error':float(np.max(abs(arr[:,9]))),'final_relative_commutator_block':float(arr[-1,10]),
            'sampled_sum_total_spatial_lag':arr[:,[3,7,8]].sum(axis=0).tolist()}
        ax.plot(arr[:,0],arr[:,7],label='Current input projection',color='#b64a38',lw=1.8)
        ax.plot(arr[:,0],arr[:,8],label='Temporal lag',color='#3977a8',lw=1.5)
        ax.axhline(0,color='black',lw=.7);ax.set_yscale('symlog',linthresh=1e-5)
        ax.set_title({'fashion':'Fashion: T-shirt vs shirt','har':'HAR: moving vs stationary','housing':'Housing: bounded value'}[domain])
        ax.set_xlabel('Training time');ax.grid(alpha=.2)
    axes[0].set_ylabel('Hidden contribution to loss derivative\npositive = locally opposes fitting')
    axes[0].legend(fontsize=8,loc='lower right')
    fig.savefig(args.out/'stage2_hidden_loss_contributions.png',dpi=180)
    fig.savefig(args.out/'stage2_hidden_loss_contributions.pdf')
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
