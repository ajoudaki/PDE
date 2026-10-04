"""Frozen distances plus leave-one-seed-out controls; no tuned aggregates."""
import argparse,json
from pathlib import Path
import numpy as np


def features(path,kind,seed):
    tag=f'{kind}_n8192_s{seed}_dt0.02'
    with np.load(path/f'{tag}.npz') as a:
        pred=a['predictions'].astype(np.float64);grams=[]
        for layer in ('train_first','train_second'):
            h=a[layer].astype(np.float64);grams.append(h@h.transpose(0,2,1)/8192)
    rec=json.loads((path/f'{tag}.json').read_text())
    return [pred,*grams,*[np.array([r[key] for r in rec['metrics']])
                         for key in ('first_motion','second_motion')]]


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);a=p.parse_args()
    kinds=('gaussian','quarter_circle','two_point','bad_right');seeds=list(range(7501,7506))
    values={k:[features(a.data/('confirmation01' if k in kinds[:2] else 'mechanism01'),k,s) for s in seeds]
            for k in kinds}
    def compare(keep):
        means={k:[np.mean([values[k][i][j] for i in keep],axis=0) for j in range(5)] for k in kinds}
        ds={k:[float(np.sqrt(np.mean((v-w)**2))) for v,w in zip(means[k],means['gaussian'])] for k in kinds[1:]}
        initial={k:[float(np.sqrt(np.mean((means[k][j][0]-means['gaussian'][j][0])**2))) for j in (1,2)] for k in kinds[1:]}
        return ds,initial
    ds,initial=compare(list(range(5)));loo=[compare([i for i in range(5) if i!=omit])[0] for omit in range(5)]
    decisions={k:bool(all(d[k][j]>2*d['quarter_circle'][j] for d in [ds,*loo] for j in (0,2))) for k in kinds[2:]}
    report=dict(distances=ds,initial_gram_distances=initial,leave_one_out=loo,discrimination_gates=decisions)
    (a.data/'mechanism01'/'analysis.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='leave_one_out'},indent=2))


if __name__=='__main__':main()
