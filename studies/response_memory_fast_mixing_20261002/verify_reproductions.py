"""Artifact-level checks, independent of trajectory aggregation code."""
import argparse,json
from pathlib import Path
import numpy as np


def compare(first,second,shared_only=False):
    files=sorted(first.glob('*_dt*.npz'))
    largest=0.;count=0
    for a in files:
        b=second/a.name
        with np.load(a) as x,np.load(b) as y:
            keys=set(x.files)&set(y.files) if shared_only else set(x.files)
            if not shared_only and keys!=set(y.files):raise AssertionError((a,'different fields'))
            for key in keys:
                if x[key].shape!=y[key].shape:raise AssertionError((a,key,'shape'))
                delta=float(np.max(np.abs(x[key]-y[key])))
                largest=max(largest,delta);count+=1
    with np.load(first/'data.npz') as x,np.load(second/'data.npz') as y:
        for key in x.files:
            if not np.array_equal(x[key],y[key]):raise AssertionError(('different data',key))
    if largest>1e-6:raise AssertionError(('reproduction tolerance',largest))
    return dict(trajectories=len(files),array_fields=count,max_absolute_difference=largest)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--first',type=Path,required=True)
    p.add_argument('--second',type=Path,required=True);p.add_argument('--shared-only',action='store_true')
    a=p.parse_args();report=compare(a.first,a.second,a.shared_only)
    (a.second/'reproduction_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
