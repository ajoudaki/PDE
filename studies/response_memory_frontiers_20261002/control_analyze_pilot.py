"""Read-only scientific reduction of the frozen control pilot outputs."""
from __future__ import annotations
import argparse
import json
import pathlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    p = argparse.ArgumentParser()
    p.add_argument('run', type=pathlib.Path)
    a = p.parse_args()
    status = json.loads((a.run/'status.json').read_text())
    avg = np.load(a.run/'dense_average.npz')
    rows = []
    errors = {}
    for frequency in [2,8,32]:
        dense = np.load(a.run/f'dense_N{frequency}.npz')
        times,truth = dense['time'],dense['predictions']
        # Compare the averaged control only at exact shared saved times.
        # This is a lower bound on its maximum over the full observation mesh;
        # it avoids giving interpolation error to the averaging baseline.
        common,ia,ib = np.intersect1d(times,avg['time'],return_indices=True)
        avg_error = np.sqrt(np.mean((truth[ia]-avg['predictions'][ib])**2,axis=1))
        for q in [3,7]:
            pred = np.load(a.run/f'q{q}_N{frequency}.npz')
            metrics = json.loads((a.run/f'q{q}_N{frequency}.json').read_text())
            err = np.sqrt(np.mean((pred['predictions']-truth)**2,axis=1))
            row = dict(frequency=frequency,q=q,
                max_prediction_error=float(err.max()),
                terminal_prediction_error=float(err[-1]),
                terminal_credit_error=metrics['metrics'][-1]['backward_error'],
                terminal_feature_error=metrics['metrics'][-1]['forward_error'],
                terminal_source_bound=metrics['metrics'][-1]['source_bound'],
                feature_motion=max(t.get('feature_motion',0) for t in metrics['metrics']),
                averaged_error_exact_common_times=float(avg_error.max()),
                elapsed=metrics['elapsed'],accepted=metrics['accepted'])
            rows.append(row)
            errors[frequency,q]=(times,err)
        ntk=np.load(a.run/f'ntk_N{frequency}.npz')
        errors[frequency,0]=(times,np.sqrt(np.mean((ntk['predictions']-truth)**2,axis=1)))
    q7=[r for r in rows if r['q']==7]
    sensitivity=status.get('numerical_sensitivity',{}).get('max_prediction_rms',float('inf'))
    gates=dict(completed=status['completed'],feature_motion=max(r['feature_motion'] for r in rows)>=.1,
               credit_roughness_terminal=max(r['terminal_credit_error'] for r in rows if r['frequency']==32)>=.3,
               numerical_refinement=sensitivity<=.005)
    positive_accuracy=all(r['max_prediction_error']<=.02 for r in q7)
    nonaveraging=any(r['averaged_error_exact_common_times']>=max(.02,2*r['max_prediction_error']) for r in q7 if r['frequency'] in [2,8])
    base=next(r['max_prediction_error'] for r in q7 if r['frequency']==2)
    failure=any(r['max_prediction_error']>.05 or (r['max_prediction_error']>4*base and r['max_prediction_error']>.02) for r in q7 if r['frequency'] in [8,32])
    verdict='PASS' if all(gates.values()) and positive_accuracy and nonaveraging else ('FAIL' if all(gates.values()) and failure else 'INCONCLUSIVE')
    result=dict(verdict=verdict,gates=gates,positive_accuracy=positive_accuracy,
                nonaveraging=nonaveraging,rows=rows,status=status,
                limits=['one seed and one problem','no policy-ranking test','only one closure refinement; no independent dense refinement',
                        'averaged-control maximum uses exact common saved times, hence a conservative lower bound on full-grid maximum'])
    (a.run/'analysis.json').write_text(json.dumps(result,indent=2))
    fig,axes=plt.subplots(1,3,figsize=(12,3.7),constrained_layout=True)
    for n,ax in zip([2,8,32],axes):
        for q,color,label in [(3,'#2563eb','memory q=3'),(7,'#16a34a','memory q=7'),(0,'#6b7280','checkpoint NTK')]:
            t,e=errors[n,q]
            ax.semilogy(t[1:],np.maximum(e[1:],1e-12),color=color,label=label)
        ax.set(title=f'{n} burst periods per half',xlabel='Adaptation time',ylabel='Prediction RMS error')
        ax.grid(alpha=.2)
    axes[0].legend(fontsize=8)
    fig.savefig(a.run/'prediction_errors.png',dpi=180)
    plt.close(fig)
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
