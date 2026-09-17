"""Compare validation fidelity across widths at exactly shared recorded times."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np
from VALIDATION_ANALYSIS import error_metrics

BASE=Path(__file__).resolve().parents[2]/'data/generated/first_order_dimension_mnist'

def compare(small,large,output):
    destination=BASE/output;destination.mkdir(parents=True,exist_ok=False)
    archives={2048:np.load(BASE/small/'sample_predictions.npz',allow_pickle=False),
              4096:np.load(BASE/large/'sample_predictions.npz',allow_pickle=False)}
    for width,name,group in ((2048,small,'main'),(4096,large,'main4096')):
        summary=json.loads((BASE/name/'summary.json').read_text())
        assert summary['width']==width and summary['run_group']==group
    assert np.array_equal(archives[2048]['official_train_ids'],archives[4096]['official_train_ids'])
    assert np.array_equal(archives[2048]['labels'],archives[4096]['labels'])
    times=np.intersect1d(archives[2048]['times'],archives[4096]['times']);assert len(times)>1
    report={'common_final_time':float(times[-1]),'validation_count':len(archives[2048]['labels']),
            'comparison':'Raw closure-to-own-width-network prediction errors at identical times; seed ranges are not confidence intervals',
            'trajectory':[],'provenance':{str(w):hashlib.sha256((BASE/name/'sample_predictions.npz').read_bytes()).hexdigest() for w,name in ((2048,small),(4096,large))}}
    for t in times:
        row={'time':float(t),'widths':{}}
        for width,a in archives.items():
            i=np.flatnonzero(a['times']==t)[0];n=a['network'][:,i];c=a['closure'][:,i];reference=n.mean(axis=0)
            individual=[error_metrics(p,reference) for p in c]
            row['widths'][str(width)]={'individual_closures':individual,
                  'mean_closure_vs_mean_network':error_metrics(c.mean(axis=0),reference),
                  'mean_individual_rms':float(np.mean([p['rms'] for p in individual])),
                  'mean_individual_relative_rms':float(np.mean([p['relative_rms'] for p in individual])),
                  'network_pairwise_rms':[error_metrics(n[j],n[k])['rms'] for j,k in itertools.combinations(range(3),2)],
                  'within_class':{str(sign):[error_metrics(p[a['labels']==sign],reference[a['labels']==sign]) for p in c] for sign in (1,-1)}}
        report['trajectory'].append(row)
    report['final']=report['trajectory'][-1]
    first=report['final']['widths']['2048']['mean_individual_rms'];second=report['final']['widths']['4096']['mean_individual_rms']
    report['relative_reduction_mean_individual_rms']=float(1-second/first)
    report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (destination/'summary.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'common_final_time':report['common_final_time'],'relative_reduction_mean_individual_rms':report['relative_reduction_mean_individual_rms'],'final':report['final']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--small',default='analysis_generalization_check_001');p.add_argument('--large',default='validation4096_001');p.add_argument('--output',default='width_comparison_001')
    a=p.parse_args();compare(a.small,a.large,a.output)
