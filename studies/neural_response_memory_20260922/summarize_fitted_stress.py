"""Whole-manifold dense/closure RMS from the focused fit-first batch."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('root',type=Path);a=p.parse_args()
    rows=[];table=['| Task | Dense train | P1 train | P2 train | P3 train | P1 test | P2 test | P3 test |',
                   '|---|---:|---:|---:|---:|---:|---:|---:|']
    rms=lambda x:float(np.sqrt(np.mean(np.asarray(x,dtype=np.float64)**2)))
    for task in ['circle_full','circle_patch','sphere_full','sphere_patch']:
        with np.load(a.root/task/'dense/arrays.npz') as d:
            reference={k:d[k].copy() for k in d.files}
        dense_record=json.loads((a.root/task/'dense/result.json').read_text())
        group={}
        for name in ['dense','P1','P2','P3']:
            folder=a.root/task/name;r=json.loads((folder/'result.json').read_text())
            for key in ['width','depth','activation','normalization','step','seed']:
                assert r[key]==dense_record[key]
            assert r.get('readout_std',1/r['width'])==dense_record.get('readout_std',1/dense_record['width'])
            assert r.get('step_schedule','constant')==dense_record.get('step_schedule','constant')
            assert r['width']==2048
            assert hashlib.sha256((folder/'arrays.npz').read_bytes()).hexdigest()==r['arrays_sha256']
            with np.load(folder/'arrays.npz') as d:
                for k in ['inputs','labels','test_inputs','test_labels','region']:
                    assert np.array_equal(d[k],reference[k])
                pred,curve=d['prediction'].copy(),d['test_prediction'].copy()
            train=rms(pred-reference['labels']);target=rms(curve-reference['test_labels'])
            assert np.isfinite(train+target)
            assert abs(train-r['train_rms'])<1e-12 and abs(target-r['test_rms_vs_target'])<1e-12
            difference=curve-reference['test_prediction'];region=reference['region']
            row=dict(task=task,model=name,train_rms=train,test_rms_vs_dense=rms(difference),
                     region_rms_vs_dense=rms(difference[region]),outside_rms_vs_dense=rms(difference[~region]),
                     test_rms_vs_target=target,status=r['fit']['status'],steps=r['fit']['steps'],
                     physical_time=r['fit']['physical_time'],seconds=r['total_seconds'])
            group[name]=row;rows.append(row)
        values=[*[group[n]['train_rms'] for n in ['dense','P1','P2','P3']],
                *[group[n]['test_rms_vs_dense'] for n in ['P1','P2','P3']]]
        table.append('| '+task+' | '+' | '.join(f'{v:.5f}' for v in values)+' |')
    with (a.root/'rms.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (a.root/'table.md').write_text('\n'.join(table)+'\n')
    summary=dict(fits=len(rows),maximum_train_rms=max(r['train_rms'] for r in rows),
                 target_reached=sum(r['status']=='target_rms' for r in rows),
                 model_seconds_range=[min(r['seconds'] for r in rows),max(r['seconds'] for r in rows)])
    (a.root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('\n'.join(table));print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
