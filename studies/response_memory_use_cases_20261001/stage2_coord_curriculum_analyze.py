"""Registered support-shift contrast and fixed curve summaries."""
import argparse
import json
from pathlib import Path
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from stage2_coord_experiment import sha,dump


def C(r):
    e=r['edits'];base=r['base']['test_mse']
    raw=e['swap']['test_mse']-e['within']['test_mse']
    nuisance=np.median([e['swap_sign_'+str(j)]['test_mse'] for j in range(5)])-np.median([e['within_sign_'+str(j)]['test_mse'] for j in range(5)])
    return (raw-nuisance)/base


def main():
    p=argparse.ArgumentParser();p.add_argument('--main',type=Path,required=True);p.add_argument('--refine',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    rows=json.loads((a.main/'results.json').read_text());fine=json.loads((a.refine/'results.json').read_text())
    result={};refinement=[];hashes={str(a.main/'results.json'):sha(a.main/'results.json'),str(a.refine/'results.json'):sha(a.refine/'results.json')}
    for domain in ('fashion','housing','har'):
        rr=[r for r in rows if r['domain']==domain];seeds=sorted({r['seed'] for r in rr});lookup={(r['seed'],r['schedule']):r for r in rr}
        F=[];centered=[];q1_ratios=[]
        for seed in seeds:
            F.append((C(lookup[seed,'AB'])+C(lookup[seed,'BA']))/2-C(lookup[seed,'joint']))
            centered.append(np.mean([lookup[seed,s]['edits']['swap_centered']['test_mse']/lookup[seed,s]['base']['test_mse']-1 for s in ('AB','BA')]))
            for s in ('AB','BA'):
                r=lookup[seed,s];b=r['base']['test_mse'];q1_ratios.append(abs(r['edits']['swap_q1']['test_mse']-b)/max(abs(r['edits']['swap']['test_mse']-b),1e-30))
        schedules={}
        for s in ('joint','AB','BA','alternating'):
            sr=[r for r in rr if r['schedule']==s]
            schedules[s]=dict(base_test_mse=float(np.median([r['base']['test_mse'] for r in sr])),
                A_test_mse=float(np.median([r['base']['test_A_mse'] for r in sr])),
                B_test_mse=float(np.median([r['base']['test_B_mse'] for r in sr])),
                median_C=float(np.median([C(r) for r in sr])),
                edit_relative_changes={k:float(np.median([r['edits'][k]['test_mse']/r['base']['test_mse']-1 for r in sr])) for k in
                    ('swap','within','swap_q1','swap_q4','swap_q8','swap_q16','swap_centered','q1_global','gradient_joint_descent','gradient_last_descent')},
                swap_q_errors={str(q):max(r['compression'][str(q)]['relative_edit_error'] for r in sr) for q in (1,4,8,16)})
        passed=all(v>0 for v in F) and np.median(F)>=.05 and np.median(centered)>=.02 and np.median(q1_ratios)<.5
        result[domain]=dict(F=F,median_F=float(np.median(F)),centered_damage=centered,
                median_centered_damage=float(np.median(centered)),phase_q1_loss_ratio=q1_ratios,
                median_phase_q1_loss_ratio=float(np.median(q1_ratios)),registered_pass=bool(passed),schedules=schedules,
                max_invariant_error=max(max(r['invariants'].values()) for r in rr),
                feature_motion_range=[min(r['feature_motion'] for r in rr),max(r['feature_motion'] for r in rr)],grouping=rr[0]['grouping'])
        frows=[r for r in fine if r['domain']==domain];seed=seeds[0]
        fc={r['schedule']:r for r in frows}
        change=abs((C(fc['AB'])-C(fc['joint']))-(C(lookup[seed,'AB'])-C(lookup[seed,'joint'])))
        checks=[]
        for s in ('joint','AB'):
            paths=[folder/f'{domain}_seed{seed}_{s}.npz' for folder in (a.main,a.refine)]
            zs=[np.load(p) for p in paths]
            for path in paths:hashes[str(path)]=sha(path)
            checks.append(dict(schedule=s,prediction_rms=float(np.sqrt(np.mean((zs[0]['test_baseline']-zs[1]['test_baseline'])**2)))))
        effect=abs(C(lookup[seed,'AB'])-C(lookup[seed,'joint']))
        refinement.append(dict(domain=domain,checks=checks,contrast_effect=effect,contrast_step_change=change,
                         resolved=bool(max(v['prediction_rms'] for v in checks)<=.02 and effect>2*change)))
    fig,axes=plt.subplots(2,3,figsize=(14,8),constrained_layout=True)
    colors={'joint':'black','AB':'#c94638','BA':'#316aa4','alternating':'#1b926c'}
    for col,domain in enumerate(('fashion','housing','har')):
        for s,color in colors.items():
            sr=[r for r in rows if r['domain']==domain and r['schedule']==s]
            times=np.array([z['t'] for z in sr[0]['curves']]);vals=np.array([[z['test_mse'] for z in r['curves']] for r in sr])
            axes[0,col].plot(times,np.median(vals,axis=0),label=s,color=color)
            axes[0,col].fill_between(times,vals.min(0),vals.max(0),alpha=.12,color=color)
        axes[0,col].set(title=domain,xlabel='Physical training time',ylabel='Held-out MSE',yscale='log')
        axes[0,col].legend(fontsize=8)
        names=('swap','within','swap_q1','swap_centered');xx=np.arange(4)
        for i,s in enumerate(colors):
            vals=[100*result[domain]['schedules'][s]['edit_relative_changes'][k] for k in names]
            axes[1,col].bar(xx+(i-1.5)*.18,vals,width=.18,color=colors[s],label=s)
        axes[1,col].axhline(0,color='.4',linewidth=.6)
        axes[1,col].set_xticks(xx,names,rotation=20);axes[1,col].set_ylabel('Median test-MSE change (%)')
        axes[1,col].set_title('Fixed endpoint interventions')
    fig.savefig(a.out/'curriculum.png',dpi=180);fig.savefig(a.out/'curriculum.pdf');plt.close(fig)
    completions=[json.loads((p/'completion.json').read_text()) for p in (a.main,a.refine)]
    summary=dict(domains=result,refinement=refinement,solves=sum(r['solves'] for r in completions),
                 producer_seconds=sum(r['seconds'] for r in completions),source_hash=sha(__file__),input_hashes=hashes)
    dump(a.out/'summary.json',summary);print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
