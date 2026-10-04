"""Independent weighted-flow and phase-exchange checks, no scientific training."""
import argparse
import json
from pathlib import Path
import time
import numpy as np
import torch
from stage2_coord_curriculum import phase_weights,schedule_weights,weighted_fields,groups
from stage2_coord_experiment import new_model,interaction,rel,sha,dump
from history_probe import interval_coefficients


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);p.add_argument('--data',type=Path,required=True)
    a=p.parse_args();a.out.parent.mkdir(parents=True,exist_ok=True);torch.manual_seed(311);start=time.perf_counter()
    x=torch.randn(7,3,dtype=torch.float64);x/=x.norm(dim=1,keepdim=True)
    f=new_model(dict(X_train=x.numpy(),y_train=np.linspace(-1,1,7)),5,189,'cpu')
    f.c.copy_(torch.randn_like(f.c));wa,wb=phase_weights(np.arange(7)<3,'cpu');lam=wa
    params=[v.detach().clone().requires_grad_() for v in f.state]
    h=(params[0]@f.inputs.T).tanh();h2=(params[1]@h).tanh();r=params[2]@h2/5-f.labels
    grads=torch.autograd.grad((lam*r.square()).sum(),params)
    observed=weighted_fields(f,lam)[2]
    errors=dict(weighted_autograd=max(rel(v,-s*g) for v,g,s in zip(observed,grads,(5,1,5))))
    errors['uniform_source']=max(rel(v,w) for v,w in zip(weighted_fields(f,torch.ones(7,dtype=torch.float64)/7)[2],f.rhs()))
    for name in ('joint','AB','BA','alternating'):
        W=schedule_weights(name,32,wa,wb);errors['exposure_'+name]=rel(W.sum(0),16*(wa+wb))
    N,n,m,dt=16,3,2,.125;H=torch.randn(N,n,m,dtype=torch.float64);B=torch.randn_like(H)
    idx=(torch.arange(N)+N//2)%N
    actual=interaction(H,B[idx],dt,n,m)-interaction(H,B,dt,n,m)
    dh=H[:N//2]-H[N//2:];db=B[:N//2]-B[N//2:]
    direct=-interaction(dh,db,dt,n,m);errors['phase_exchange_identity']=rel(actual,direct)
    C=torch.tensor(interval_coefficients(np.full(N//2,dt),4),dtype=torch.float64)
    hc=(C@dh.flatten(1)).reshape(4,n,m);bc=(C@db.flatten(1)).reshape(4,n,m)
    projected=-interaction(hc,bc,1.,n,m)
    ht=(dt*dh.square().sum((0,1))-hc.square().sum((0,1))).clamp_min(0)
    bt=(dt*db.square().sum((0,1))-bc.square().sum((0,1))).clamp_min(0)
    bound=float(2/(n*m)*(ht*bt).sqrt().sum());error=float((projected-actual).norm())
    if error>bound+1e-12:raise AssertionError('tail bound')
    if max(errors.values())>1e-10:raise AssertionError(errors)
    metadata={d:groups(dict(np.load(a.data/(d+'.npz'))),d)[1] for d in ('fashion','housing','har')}
    result=dict(passed=True,errors=errors,bound=bound,observed_error=error,grouping=metadata,
        source_hashes={n:sha(Path(__file__).with_name(n)) for n in ('stage2_coord_curriculum.py','stage2_coord_curriculum_checks.py')},
        seconds=time.perf_counter()-start)
    dump(a.out,result);print(json.dumps(result,indent=2))


if __name__=='__main__':main()
