"""Score saved fitted closure endpoints against preserved width-2048 dense runs."""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import zipfile

import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def difference(x, y):
    d = x-y
    return dict(rms=float(np.sqrt(np.mean(d*d))), maximum=float(abs(d).max()))


def predictions(run):
    with np.load(Path(run)/'predictions.npz') as f:
        return {k:f[k] for k in f.files}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--campaign', required=True)
    p.add_argument('--out', required=True)
    a=p.parse_args()
    campaign=Path(a.campaign).resolve()
    out=Path(a.out).resolve(); out.mkdir(parents=True,exist_ok=False)
    os.environ.setdefault('MPLCONFIGDIR',str(out/'mplconfig'))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    progress=json.loads((campaign/'progress.json').read_text())
    inventory_path=Path(progress['inputs'])/'inventory.json'
    inventory=json.loads(inventory_path.read_text())
    rows=[]; allruns=[]; pairs=[]; invalid=[]; unscored=[]
    grouped={}
    for attempt in progress['attempts']:
        grouped.setdefault(tuple(attempt['cell']),[]).append(attempt)
    for cell, attempts in grouped.items():
        activation,task,P=cell; key=activation+'__'+task
        ref=inventory['cases'][key]
        for reference in ('finest','previous'):
            directory=Path(ref[reference]['path'])
            for name,h in ref[reference]['files_sha256'].items():
                assert sha(directory/name)==h,'Dense reference hash: '+str(directory/name)
                if name.endswith('.npz'):
                    with zipfile.ZipFile(directory/name) as z:assert z.testzip() is None
        fine=predictions(ref['finest']['path']); prev=predictions(ref['previous']['path'])
        for field in ('circle_angles','circle_inputs','train_inputs','train_labels'):
            assert np.array_equal(fine[field],prev[field]),'Dense reference grids: '+field
        target=fine['circle_predictions']
        valid=[]
        for attempt in sorted(attempts,key=lambda r:r['level']):
            run=Path(attempt['run'])
            if not (run/'summary.json').exists():
                unscored.append(dict(run=str(run),reason=attempt['status']))
                continue
            try:
                summary=json.loads((run/'summary.json').read_text())
                assert attempt['summary_sha256']==sha(run/'summary.json')
                assert summary['initialization_sha256']==ref['finest']['initialization_sha256']
                for name,h in summary['artifact_sha256'].items():
                    assert sha(run/name)==h, name+' hash'
                    if name.endswith('.npz'):
                        with zipfile.ZipFile(run/name) as z:assert z.testzip() is None
                if (not summary['state_finite'] or not summary['predictions_finite']
                    or summary.get('stop_reason','').startswith('nonfinite')):
                    assert summary['status']=='diverged'
                    unscored.append(dict(run=str(run),reason='nonfinite_divergence'))
                    continue
                pred=predictions(run)
                for field in ('circle_angles','circle_inputs','train_inputs','train_labels'):
                    assert np.array_equal(pred[field],fine[field]),field
                x=pred['circle_predictions'];assert np.isfinite(x).all()
                err=difference(x,target); prev_err=difference(x,prev['circle_predictions'])
                mse=float(np.mean((pred['train_predictions']-pred['train_labels'])**2))
                assert abs(mse-summary['training_mse'])<=1e-13*max(1,mse)
                assert summary['physical_time']==summary['steps']*summary['step']
                assert (mse<=1e-8)==summary['fitted']
                grid=abs(err['rms']-difference(x[::2],target[::2])['rms'])
                row=dict(activation=activation,task=task,P=P,level=attempt['level'],
                    run=str(run),status=summary['status'],fitted=summary['fitted'],
                    step=summary['step'],training_mse=mse,physical_time=summary['physical_time'],
                    steps=summary['steps'],integration_seconds=summary['integration_seconds'],
                    rms=err['rms'],maximum=err['maximum'],
                    relative_rms=err['rms']/float(np.sqrt(np.mean(target**2))),
                    rms_against_previous_dense=prev_err['rms'],
                    dense_sensitivity_rms=ref['dense_sensitivity_rms'],
                    grid_sensitivity_rms=grid,grid_pass=grid<=1e-5)
                allruns.append(row);valid.append((row,x))
            except Exception as e:
                invalid.append(dict(run=str(run),reason=repr(e)))
        if not valid:continue
        localpairs=[]
        for i in range(len(valid)):
            for j in range(i+1,len(valid)):
                c,cx=valid[i];f,fx=valid[j]; diff=difference(cx,fx)
                pair=dict(activation=activation,task=task,P=P,
                    coarse_level=c['level'],fine_level=f['level'],**diff,
                    adjacent=f['level']==c['level']+1,both_fitted=c['fitted'] and f['fitted'])
                pair['screen_pass']=pair['adjacent'] and pair['both_fitted'] and diff['rms']<=.01 and diff['maximum']<=.05
                pairs.append(pair);localpairs.append(pair)
        fitted=[r for r,x in valid if r['fitted']]
        chosen=dict(fitted[-1] if fitted else valid[-1][0])
        terminal=max(attempts,key=lambda r:r['level'])
        lastlevel=terminal['level']
        finalpair=next((r for r in localpairs if r['fine_level']==lastlevel and r['adjacent']),None)
        fittedpairs=[r for r in localpairs if r['adjacent'] and r['both_fitted']]
        fitpair=max(fittedpairs,key=lambda r:r['fine_level']) if fittedpairs else None
        chosen.update(last_attempt_level=lastlevel,last_attempt_status=terminal['status'],
            fitted_pair_coarse_level=fitpair['coarse_level'] if fitpair else None,
            fitted_pair_fine_level=fitpair['fine_level'] if fitpair else None,
            closure_sensitivity_rms=fitpair['rms'] if fitpair else None,
            closure_sensitivity_max=fitpair['maximum'] if fitpair else None,
            terminal_pair_rms=finalpair['rms'] if finalpair else None,
            refinement_pass=bool(finalpair and finalpair['screen_pass']),
            precision_pass=bool(fitpair and fitpair['rms']<=.1*chosen['rms'] and
                ref['dense_sensitivity_rms']<=.1*chosen['rms']),
            descriptive_close=chosen['rms']<=.1)
        rows.append(chosen)
    result=dict(campaign=str(campaign),campaign_status=progress['status'],
        progress_sha256=sha(campaign/'progress.json'),inventory_sha256=sha(inventory_path),
        analyzer_sha256=sha(__file__),rows=rows,all_runs=allruns,pairs=pairs,invalid=invalid,unscored=unscored,
        integration_seconds=progress['integration_seconds'],
        qualifications=['All scores compare saved endpoints, not exact continuous flows.',
            'A fitted score uses each model own first MSE<=1e-8 discrete state.',
            'Unfitted rows use the final finite capped state and are descriptive only.',
            'Dense and closure halving sensitivities are observed differences, not rigorous error bounds.',
            'One seed, n=2048, three hidden layers, original residual-activity closure.'])
    (out/'analysis.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    for name,records in [('rms_table.csv',rows),('all_runs.csv',allruns),('halving_pairs.csv',pairs)]:
        if records:
            with (out/name).open('w') as f:
                writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
    colors={'relu':'#2563eb','gelu':'#d97706','selu':'#8b5cf6'}
    labels={'relu':'ReLU','gelu':'GELU','selu':'SELU'}
    fig,axes=plt.subplots(1,2,figsize=(10.8,4.5),sharey=True)
    for ax,task,title in zip(axes,['two_outliers_alternating','quadrant_alternating'],['Two outliers','Quadrant']):
        for activation in colors:
            rr=sorted([r for r in rows if r['task']==task and r['activation']==activation],key=lambda r:r['P'])
            if not rr:continue
            ax.plot([r['P'] for r in rr],[r['rms'] for r in rr],color=colors[activation],label=labels[activation],lw=1.7)
            for r in rr:
                ax.plot(r['P'],r['rms'],marker='o' if r['fitted'] else 'x',ms=7,
                    color=colors[activation],mfc=colors[activation] if r['refinement_pass'] else 'white')
        ax.axhline(.1,color='#64748b',ls=':',lw=1)
        ax.set_xticks([1,2,3]);ax.set_xlabel('Closure order P');ax.set_title(title)
        ax.set_yscale('log');ax.grid(True,alpha=.18);ax.legend(frameon=False)
    axes[0].set_ylabel('Circle RMS difference from fitted dense network')
    fig.suptitle('Width 2048 · ReLU, GELU, SELU · Three hidden layers')
    note='Filled circles: closure step check passed. Open circles: unresolved.'
    note+=(' All shown endpoints have training MSE ≤ 10⁻⁸.' if all(r['fitted'] for r in rows)
           else ' Crosses: training target not reached.')
    fig.text(.5,.015,note+'\nDense reference step sensitivity is reported separately.',ha='center',fontsize=9)
    fig.tight_layout(rect=[0,.055,1,.95])
    for ext in ('png','pdf'):fig.savefig(out/f'rms_vs_P.{ext}',dpi=190,bbox_inches='tight')
    plt.close(fig)
    print(json.dumps(dict(rows=rows,invalid=invalid),indent=2))


if __name__=='__main__':main()
