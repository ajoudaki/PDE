"""Rescore all stress endpoints and retain failed/capped comparison statuses."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import numpy as np


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path);a=parser.parse_args()
    rows=[];workers={};here=Path(__file__).resolve().parent
    def rms(v):
        value=float(np.sqrt(np.mean(np.asarray(v,dtype=np.float64)**2)))
        return value if np.isfinite(value) else None
    for task in ['circle_full','circle_patch','sphere_full','sphere_patch']:
        folder=a.root/task;record=json.loads((folder/'results.json').read_text())
        assert record['status']=='complete'
        assert len(record['rows'])==(25 if task.endswith('patch') else 16)
        workers[task]=record['total_seconds']
        for name,value in record['source_sha256'].items():
            assert hashlib.sha256((here/name).read_bytes()).hexdigest()==value
        assert hashlib.sha256((folder/'data.npz').read_bytes()).hexdigest()==record['data_sha256']
        with np.load(folder/'data.npz') as d:
            labels,truth,region=d['labels'].copy(),d['test_labels'].copy(),d['region'].copy()
        group={(r['depth'],r['normalization'],r['activation'],r['model']):r for r in record['rows']}
        for r in record['rows']:
            key=(r['depth'],r['normalization'],r['activation'])
            prefix=f'd{key[0]}_{key[1]}_{key[2]}_'
            with np.load(folder/(prefix+'dense.npz')) as d: dense=d['test_prediction'].copy()
            with np.load(folder/(prefix+r['model']+'.npz')) as d:
                train=d['prediction'].copy();pred=d['test_prediction'].copy()
            values=dict(train_rms=rms(train-labels),test_rms_vs_dense=rms(pred-dense),
                        test_rms_vs_target=rms(pred-truth),
                        region_rms_vs_dense=rms((pred-dense)[region]),
                        outside_rms_vs_dense=rms((pred-dense)[~region]),
                        region_rms_vs_target=rms((pred-truth)[region]),
                        outside_rms_vs_target=rms((pred-truth)[~region]))
            for k,v in values.items():
                assert (v is None and r[k] is None) or (v is not None and r[k] is not None and abs(v-r[k])<1e-12)
            reference=group[(*key,'dense')]
            fitted=all(v is not None and v<=.05 for v in [r['train_rms'],reference['train_rms']])
            motions=r['feature_change_rms']
            rows.append(dict(task=task,depth=key[0],normalization=key[1],activation=key[2],
                             model=r['model'],**values,status=r['status'],dense_train_rms=reference['train_rms'],
                             fitted_pair=fitted,steps=r['steps'],physical_time=r['physical_time'],
                             seconds=r['total_seconds'],feature_motion_first=motions[0],
                             feature_motion_middle=motions[len(motions)//2],feature_motion_last=motions[-1]))
    with (a.root/'stress_rms.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    fmt=lambda v:'—' if v is None else f'{v:.4f}'
    table=['| Task | Depth | Norm | Activation | Dense train | P1 test | P2 test | P3 test | P3 train | Dense target | P3 target |',
           '|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|']
    keys=list(dict.fromkeys((r['task'],r['depth'],r['normalization'],r['activation']) for r in rows))
    for key in keys:
        g={r['model']:r for r in rows if (r['task'],r['depth'],r['normalization'],r['activation'])==key}
        if 'P3' not in g: continue
        def score(name):return fmt(g[name]['test_rms_vs_dense'])+('†' if not g[name]['fitted_pair'] else '')
        values=[key[0],str(key[1]),key[2],key[3],fmt(g['dense']['train_rms']),
                *[score(f'P{p}') for p in [1,2,3]],fmt(g['P3']['train_rms']),
                fmt(g['dense']['test_rms_vs_target']),fmt(g['P3']['test_rms_vs_target'])]
        table.append('| '+' | '.join(values)+' |')
    (a.root/'table.md').write_text('\n'.join(table)+'\n')
    stats=dict(fits=len(rows),target_reached=sum(r['status']=='target_rms' for r in rows),
               below_005=sum(r['train_rms'] is not None and r['train_rms']<=.05 for r in rows),
               workers_seconds=workers,
               nonfinite=sum(r['train_rms'] is None for r in rows))
    (a.root/'summary.json').write_text(json.dumps(stats,indent=2)+'\n')
    print('\n'.join(table));print(json.dumps(stats,indent=2))


if __name__=='__main__':main()
