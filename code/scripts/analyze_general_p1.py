"""Independent NumPy replay of a finite example and optional identical rerun."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from pde.closure_comparison import prediction_metrics,gram_metrics


def analyze(run,repeat=None):
    record=json.loads((run/'record.json').read_text())
    for name,digest in record['output_sha256'].items():
        if hashlib.sha256((run/name).read_bytes()).hexdigest()!=digest:raise ValueError('output hash mismatch')
    with np.load(run/'observations.npz',allow_pickle=False) as saved:
        a={k:saved[k].copy() for k in saved.files}
    U=a['inputs'];ids=a['ids'];prediction_metrics(a['labels'],a['labels'],ids=ids,reference_ids=ids)
    h1=np.tanh(a['closure_w']@U.T)
    h2=np.tanh(a['closure_b2']@a['closure_M']@(a['closure_b1'].T@(a['closure_p1'][:,None]*h1)))
    closure=(a['closure_p2']*a['closure_c'])@h2
    n=len(a['network_c']);g1=np.tanh(a['network_w']@U.T);g2=np.tanh(a['network_M']@g1)
    network=a['network_c']@g2/n
    np.testing.assert_allclose(closure,a['closure_prediction'],atol=2e-12,rtol=2e-11)
    np.testing.assert_allclose(network,a['network_prediction'],atol=2e-12,rtol=2e-11)
    metrics=prediction_metrics(a['closure_prediction'],a['network_prediction'],ids=ids,reference_ids=ids)
    max_error=max(float(np.max(abs(closure-a['closure_prediction']))),float(np.max(abs(network-a['network_prediction']))))
    for layer,lower,upper in ((1,h1,g1),(2,h2,g2)):
        expected=(lower.T@(a[f'closure_p{layer}'][:,None]*lower),upper.T@upper/n)
        for prefix,target in zip(('closure','network'),expected):
            actual=a[f'{prefix}_gram{layer}'];np.testing.assert_allclose(actual,target,atol=2e-12,rtol=2e-11)
            max_error=max(max_error,float(np.max(abs(actual-target))))
        metrics[f'gram{layer}']=gram_metrics(a[f'closure_gram{layer}'],a[f'network_gram{layer}'],ids=ids,reference_ids=ids)
    if metrics!=record['metrics']:raise ValueError('recorded comparison metrics mismatch')
    if repeat:
        with np.load(repeat/'observations.npz',allow_pickle=False) as other:
            if set(a)!=set(other.files):raise ValueError('repeat fields differ')
            for k,v in a.items():
                if not np.array_equal(v,other[k]):raise ValueError('repeat array differs: '+k)
    return dict(passed=True,replay_max_absolute_error=max_error,exact_repeat_arrays=repeat is not None,
                scope='finite example replay, no closure approximation conclusion',metrics=metrics)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--run',required=True,type=Path)
    parser.add_argument('--repeat',type=Path);parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args();result=analyze(args.run,args.repeat)
    with args.output.open('x') as f:json.dump(result,f,indent=2,allow_nan=False)
    print(json.dumps({'passed':result['passed'],'output':str(args.output)}))
