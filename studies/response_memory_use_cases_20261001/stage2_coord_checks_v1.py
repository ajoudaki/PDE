"""Independent small algebra/source oracles; no scientific fits."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import time
import numpy as np
import torch
from stage2_coord_experiment import (Flow,advance,controls,fields,interaction,mean_write,
                                    new_model,permutation_write,rel)
from history_probe import interval_coefficients


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.parent.mkdir(parents=True,exist_ok=True)
    start=time.perf_counter();torch.manual_seed(27183);errors={}
    x=torch.randn(5,3,dtype=torch.float64);x/=x.norm(dim=1,keepdim=True)
    data=dict(X_train=x.numpy(),y_train=np.linspace(-1,1,5))
    f=new_model(data,7,281,'cpu');f.c.copy_(torch.randn(7,dtype=torch.float64))
    own=fields(f)[2];source=f.rhs()
    errors['source_velocity']=max(rel(u,v) for u,v in zip(own,source))
    params=[p.detach().clone().requires_grad_() for p in f.state]
    h=(params[0]@f.inputs.T).tanh();h2=(params[1]@h).tanh()
    loss=(params[2]@h2/7-f.labels).square().mean()
    grads=torch.autograd.grad(loss,params)
    errors['autograd_mobility']=max(rel(v,-mob*g) for v,g,mob in zip(own,grads,(7,1,7)))
    before=[v.clone() for v in f.state];f.step(.015625)
    errors['source_one_step']=max(rel(u,v+.015625*g) for u,v,g in zip(f.state,before,own))
    hist=advance(f,.25,.015625,True);errors['accumulated_update']=hist['parity']
    # Whole zero-residual trajectory is handled without activity division.
    z=new_model(dict(X_train=x.numpy(),y_train=np.zeros(5)),7,282,'cpu')
    zh=advance(z,.125,.015625,True)
    errors['stationary_zero']=float(zh['b'].abs().max()+zh['exact'].abs().max())
    # Enumerate all permutations, using multiple samples and unrelated h,b.
    N,n,m=4,3,2;dt=.125
    H=torch.randn(N,n,m,dtype=torch.float64);B=torch.randn_like(H)
    hist=dict(h=H,b=B)
    writes=torch.stack([permutation_write(hist,torch.tensor(pi),dt,n,m)
                        for pi in itertools.permutations(range(N))])
    mean=mean_write(hist,dt,n,m)
    errors['permutation_mean']=rel(writes.mean(0),mean)
    HC=H-H.mean(0);BC=B-B.mean(0)
    predicted=sum(float((bj@hi.T).square().sum()) for bj in BC for hi in HC)/(N-1)*(2*dt/(n*m))**2
    observed=float((writes-mean).square().sum((1,2)).mean())
    errors['permutation_variance']=abs(observed-predicted)/predicted
    E=writes[0]-writes[1];_,_,gates=controls(E,19);errors.update(gates)
    # Analytic Legendre interval integrals versus independent Gauss quadrature.
    masses=np.array([.03,.27,0.,.13,.57]);C=interval_coefficients(masses,12)
    nodes,weights=np.polynomial.legendre.leggauss(32);edges=np.r_[0,np.cumsum(masses)]
    oracle=np.zeros_like(C)
    for i,(lo,hi) in enumerate(zip(edges[:-1],edges[1:])):
        t=(hi+lo)/2+(hi-lo)*nodes/2
        for j in range(12):
            oracle[j,i]=np.sqrt((2*j+1)/edges[-1])*(hi-lo)/2*np.dot(weights,
                          np.polynomial.legendre.Legendre.basis(j)(2*t/edges[-1]-1))
    errors['interval_quadrature']=float(np.max(np.abs(C-oracle)))
    if max(errors.values())>1e-9:raise AssertionError(errors)
    result=dict(errors=errors,seconds=time.perf_counter()-start,passed=True,
                source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                 [Path(__file__),Path(__file__).with_name('stage2_coord_experiment.py')]})
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
