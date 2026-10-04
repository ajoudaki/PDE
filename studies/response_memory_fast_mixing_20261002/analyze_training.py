"""Fixed five-metric ensemble comparison; no fitted metric weights."""
import argparse,json
from pathlib import Path
import numpy as np


def summarize(path):
    raw=json.loads((path/'summary.json').read_text())
    report={}
    for n in sorted({r['n'] for r in raw['rows']}):
        quantities={};performance={}
        for kind in ('gaussian','flat','quarter_circle','gaussian_diagonal'):
            rows=[r for r in raw['rows'] if r['n']==n and r['kind']==kind]
            if not rows: continue
            ensemble=[]
            for r in rows:
                z=np.load(path/f'{kind}_n{n}_s{r["seed"]}_dt{r["dt"]:g}.npz')
                grams=[]
                for layer in ('train_first','train_second'):
                    h=z[layer].astype(np.float64)
                    grams.append(h@h.transpose(0,2,1)/n)
                ensemble.append([z['predictions'].astype(np.float64),*grams,
                    np.array([v['first_motion'] for v in r['metrics']]),
                    np.array([v['second_motion'] for v in r['metrics']])])
            quantities[kind]=[np.mean([e[j] for e in ensemble],axis=0) for j in range(5)]
            performance[kind]=dict(seeds=[r['seed'] for r in rows],
                terminal=[r['metrics'][-1] for r in rows],
                training_seconds=[r['training_seconds'] for r in rows],
                peak_bytes=[r['peak_allocated_bytes'] for r in rows])
        distances={k:[float(np.sqrt(np.mean((a-b)**2))) for a,b in zip(v,quantities['gaussian'])]
                   for k,v in quantities.items() if k!='gaussian'}
        names=['predictions','first_gram','second_gram','first_motion','second_motion']
        qc=distances.get('quarter_circle')
        if qc is not None and all(k in distances for k in ('flat','gaussian_diagonal')):
            better=all(qc[j]<min(distances['flat'][j],distances['gaussian_diagonal'][j]) for j in range(5))
            useful=sum(v['first_motion']>=.03 and v['test_mse']<=.95*v['frozen_test_mse']
                       for v in performance['quarter_circle']['terminal'])
            gate=bool(better and qc[0]<=.01 and useful>=4)
        else:gate=None
        report[str(n)]=dict(metric_names=names,distances=distances,performance=performance,
                            confirmation_gate=gate)
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('path',type=Path);args=p.parse_args()
    report=summarize(args.path)
    (args.path/'five_metric_analysis.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({n:{k:v for k,v in r.items() if k!='performance'} for n,r in report.items()},indent=2))
