#!/usr/bin/env python3
"""No-training CPU/CUDA comparison of production GD against frozen independent gradients."""
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import torch
import gd_benchmark as producer
import gd_check as independent


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    if args.output.exists(): raise ValueError('Output must be fresh')
    producer.configure_torch()
    started=time.monotonic()
    records=[]
    for case in independent.make_cases()+independent.highgain_cases():
        grad,pred,loss=independent.explicit_gradients(case)
        n=len(case['c'])
        expected=(grad[0],grad[1],grad[2]/n)
        Q=n*np.sum(expected[0]**2)+np.sum(expected[1]**2)+n*np.sum(expected[2]**2)
        for device in ('cpu','cuda:0','cuda:1'):
            model=producer.GDModel('network' if case['kind']=='dense' else 'closure',n,
                                   case.get('b1'),case.get('b2'),device=device)
            state=model.state(case['w'],case['middle'],case['c'])
            u=torch.tensor(case['inputs'],device=device)
            y=torch.tensor(case['labels'],device=device)
            fields=model.fields(state,u)
            actual=model.gradients(state,u,y,fields)
            observed=(actual.W.cpu().numpy(),actual.middle.cpu().numpy(),actual.c.cpu().numpy())
            errors=[]
            for got,want in zip(observed,expected):
                np.testing.assert_allclose(got,want,rtol=2e-10,atol=2e-12)
                errors.append(float(np.max(np.abs(got-want))))
            np.testing.assert_allclose(fields[-1].cpu().numpy(),pred,rtol=2e-10,atol=2e-12)
            q=model.gradient_metrics(actual)['physical_Q']
            np.testing.assert_allclose(q,Q,rtol=2e-10,atol=2e-12)
            after=model.step(state,actual,.25)
            step_errors=[]
            for got,start,g,mob in zip((after.W,after.middle,after.c),
                                       (case['w'],case['middle'],case['c']),expected,(n,1,n)):
                want=start-.25*mob*g
                np.testing.assert_allclose(got.cpu().numpy(),want,rtol=2e-10,atol=2e-12)
                step_errors.append(float(np.max(np.abs(got.cpu().numpy()-want))))
            for got,start in zip((state.W,state.middle,state.c),(case['w'],case['middle'],case['c'])):
                assert np.array_equal(got.cpu().numpy(),start)
            records.append(dict(case=case['name'],device=device,gradient_errors=errors,
                                step_errors=step_errors,Q=q,passed=True))
    files=(Path(__file__),Path(producer.__file__),Path(independent.__file__))
    out=dict(training_performed=False,passed=True,checks=records,elapsed_seconds=time.monotonic()-started,
             source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(passed=True,checks=len(records),elapsed_seconds=out['elapsed_seconds'])))


if __name__=='__main__': main()
