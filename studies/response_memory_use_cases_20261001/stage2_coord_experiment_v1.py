"""Exact physical-time history interventions. Frozen design: STAGE2_COORD_PROTOCOL.md."""
import argparse
import copy
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import shutil
import sys
import time

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('MKL_NUM_THREADS', '1')
import numpy as np
import torch
from baseline_compact_flow import Flow
from history_probe import interval_coefficients

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
torch.set_num_threads(1)
torch.backends.cuda.matmul.allow_tf32=False
torch.backends.cudnn.allow_tf32=False


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path,value): Path(path).write_text(json.dumps(value,indent=2)+'\n')
def scalar(x): return float(x.detach().cpu())
def rel(x,y): return scalar((x-y).norm()/y.norm().clamp_min(1e-30))

def new_model(data,n,seed,device):
    f=Flow(data['X_train'][:512],data['y_train'][:512],width=n,depth=2,
           activation='tanh',order=None,seed=seed,device=device,dtype=torch.float64,
           hidden_gain=1.,readout_std=1.)
    f.c.zero_()
    return f


def fields(f):
    h=(f.w@f.inputs.T).tanh()
    z=f.matrices[0]@h
    h2=z.tanh()
    r=f.c@h2/f.n-f.labels
    b=(f.c[:,None]*(1-h2.square()))*r
    v1=(-2/f.M)*((f.matrices[0].T@b)*(1-h.square()))@f.inputs
    v2=(-2/(f.M*f.n))*b@h.T
    vc=(-2/f.M)*h2@r
    return h,b,(v1,v2,vc)


@torch.no_grad()
def advance(f,T,dt,record=False):
    count=round(T/dt)
    if abs(count*dt-T)>1e-10: raise ValueError('Nonintegral steps')
    initial=f.matrices[0].clone()
    hs=f.w.new_empty((count,f.n,f.M)) if record else None
    bs=torch.empty_like(hs) if record else None
    for i in range(count):
        h,b,v=fields(f)
        if record: hs[i].copy_(h);bs[i].copy_(b)
        for p,g in zip(f.state,v):p.add_(g,alpha=dt)
    if not all(bool(torch.isfinite(p).all()) for p in f.state):
        raise RuntimeError('Nonfinite model')
    if not record:return None
    exact=f.matrices[0]-initial
    paired=interaction(hs,bs,dt,f.n,f.M)
    err=rel(paired,exact)
    if err>1e-9: raise RuntimeError(('observer parity',err))
    return dict(h=hs,b=bs,exact=exact,parity=err)


def interaction(h,b,dt,n,m):
    # Time and sample indices contract together; neuron indices are retained.
    H=h.permute(1,0,2).reshape(n,-1)
    B=b.permute(1,0,2).reshape(n,-1)
    return (-2*dt/(n*m))*(B@H.T)


def mean_write(hist,dt,n,m):
    N=hist['h'].shape[0]
    return (-2*dt*N/(n*m))*(hist['b'].mean(0)@hist['h'].mean(0).T)


def permutation_write(hist,perm,dt,n,m):
    return interaction(hist['h'],hist['b'][perm],dt,n,m)


def controls(E,seed):
    U,s,Vh=torch.linalg.svd(E,full_matrices=False)
    gen=torch.Generator(device=E.device).manual_seed(seed)
    signs=torch.randint(0,2,(len(s),),generator=gen,device=E.device,dtype=torch.int64)*2-1
    signed=(U*(s*signs))@Vh
    A=torch.linalg.qr(torch.randn(E.shape,generator=gen,device=E.device,dtype=E.dtype)).Q
    B=torch.linalg.qr(torch.randn(E.shape,generator=gen,device=E.device,dtype=E.dtype)).Q
    isotropic=(A*s)@B.T
    gates=dict(left_gram=rel(signed@signed.T,E@E.T),right_gram=rel(signed.T@signed,E.T@E),
               isotropic_spectrum=rel(torch.linalg.svdvals(isotropic),s))
    if max(gates.values())>1e-9:raise RuntimeError(('matched controls',gates))
    return signed,isotropic,gates


def gradient_edit(f,norm):
    v=fields(f)[2][1]
    if scalar(v.norm())==0:return torch.zeros_like(v)
    return v*(norm/v.norm())


@torch.no_grad()
def scores(f,data,reference=None):
    result={};preds={}
    for name in ('train','val','test'):
        x=f.inputs if name=='train' else data['X_'+name]
        target=f.labels if name=='train' else torch.as_tensor(data['y_'+name],device=f.device,dtype=f.dtype)
        pred=f.predict(x)
        preds[name]=pred.detach().cpu().numpy()
        result[name+'_mse']=scalar((pred-target).square().mean())
        labels=np.asarray(data['y_'+name])[:f.M] if name=='train' else np.asarray(data['y_'+name])
        if set(np.unique(labels)).issubset({-1.,1.}):
            result[name+'_accuracy']=scalar(((pred>=0)==(target>=0)).double().mean())
        if reference is not None:
            ref=torch.as_tensor(reference[name],device=f.device,dtype=f.dtype)
            result[name+'_prediction_rms']=scalar((pred-ref).square().mean().sqrt())
    return result,preds


@torch.no_grad()
def endpoint_case(data,n,seed,device,T,dt,continue_five=False):
    f=new_model(data,n,seed,device)
    h0=(f.w@f.inputs.T).tanh()
    hist=advance(f,T,dt,True)
    h1=(f.w@f.inputs.T).tanh();z=f.w@f.inputs.T
    base,preds=scores(f,data)
    N=hist['h'].shape[0];idx=torch.arange(N,device=device)
    reverse=idx.flip(0)
    allwrite=hist['exact'];rev=permutation_write(hist,reverse,dt,n,f.M)-allwrite
    edits={'none':torch.zeros_like(rev),'reverse':rev,'opposite_reverse':-rev,
           'q1':mean_write(hist,dt,n,f.M)-allwrite}
    for j in range(2):
        g=torch.Generator(device=device).manual_seed(81000+seed*10+j)
        perm=torch.randperm(N,generator=g,device=device)
        edits['time_shuffle_'+str(j)]=permutation_write(hist,perm,dt,n,f.M)-allwrite
    for j in range(3):
        perm=idx.clone();lo=j*N//3;hi=(j+1)*N//3
        perm[lo:hi]=perm[lo:hi].flip(0)
        edits['window_'+str(j)]=permutation_write(hist,perm,dt,n,f.M)-allwrite
    coeff_arrays={};projection={}
    mass=np.full(N,dt)
    for q in (4,8,16,32):
        C=torch.as_tensor(interval_coefficients(mass,q),device=device,dtype=f.dtype)
        hc=(C@hist['h'].flatten(1)).reshape(q,n,f.M)
        bc=(C@hist['b'].flatten(1)).reshape(q,n,f.M)
        projected=interaction(hc,bc,1.,n,f.M)
        edits['q'+str(q)]=projected-allwrite
        projection[str(q)]=rel(projected,allwrite)
        if q in (4,8):
            coeff_arrays['h_q'+str(q)]=hc.cpu().numpy();coeff_arrays['b_q'+str(q)]=bc.cpu().numpy()
    invariants={}
    invariants['simultaneous']=rel(interaction(hist['h'][reverse],hist['b'][reverse],dt,n,f.M),allwrite)
    invariants['backward_mean']=rel(hist['b'][reverse].mean(0),hist['b'].mean(0))
    # Distribution equality is exact because reverse is a bijection; check two Grams on sample0.
    b0=hist['b'][:,:,0]
    invariants['backward_sample_gram']=rel(b0[reverse].T@b0[reverse],b0.T@b0)
    for j in range(5):
        signed,iso,gates=controls(rev,91000+seed*10+j)
        edits['sign_'+str(j)]=signed;edits['spectral_'+str(j)]=iso
        invariants.update({str(j)+'_'+k:v for k,v in gates.items()})
    edits['gradient_descent']=gradient_edit(f,rev.norm())
    edits['gradient_ascent']=-edits['gradient_descent']
    if max(invariants.values())>1e-9:raise RuntimeError(('invariants',invariants))
    grad=-fields(f)[2][1]
    rows={};arrays={
        'first':f.w.cpu().numpy(),'hidden':f.matrices[0].cpu().numpy(),'readout':f.c.cpu().numpy(),
        'exact_write':allwrite.cpu().numpy(),**coeff_arrays,
        **{'baseline_pred_'+k:v for k,v in preds.items()}}
    # Release full histories after all fixed edits are constructed.
    del hist
    initial=f.matrices[0].clone()
    for name,E in edits.items():
        f.matrices[0].copy_(initial+E)
        row,p=scores(f,data,preds)
        row['edit_norm']=scalar(E.norm())
        linear=scalar((grad*E).sum())
        change=row['train_mse']-base['train_mse']
        row.update(train_linear_change=linear,train_nonlinear_remainder=change-linear)
        rows[name]=row
        arrays['edit_'+name]=E.cpu().numpy()
        arrays['test_pred_'+name]=p['test']
    f.matrices[0].copy_(initial)
    continuations={}
    if continue_five:
        for name in ('none','q1','reverse','sign_0','gradient_descent'):
            c=copy.deepcopy(f);c.matrices[0].add_(edits[name]);advance(c,4.,dt)
            continuations[name]=scores(c,data,preds)[0]
    return dict(seed=seed,n=n,m=f.M,T=T,dt=dt,base=base,edits=rows,
                feature_motion=scalar((h1-h0).norm()/h0.norm()),
                nonlinearity=scalar((z-h1).norm()/z.norm()),
                projection_errors=projection,invariants=invariants,continuations=continuations),arrays


@torch.no_grad()
def causal_case(data,n,seed,device,T,dt,arm):
    f=new_model(data,n,seed,device)
    traces=[]
    for j in range(4):
        hist=advance(f,T/4,dt,True)
        N=hist['h'].shape[0]
        rev=permutation_write(hist,torch.arange(N-1,-1,-1,device=device),dt,n,f.M)-hist['exact']
        if arm=='none':E=torch.zeros_like(rev)
        elif arm=='q1':E=mean_write(hist,dt,n,f.M)-hist['exact']
        elif arm=='reverse':E=rev
        elif arm=='sign':E=controls(rev,101000+seed*10+j)[0]
        elif arm=='gradient':E=gradient_edit(f,rev.norm())
        else:raise ValueError(arm)
        f.matrices[0].add_(E)
        traces.append(dict(block=j,edit_norm=scalar(E.norm()),train_mse=scores(f,data)[0]['train_mse']))
        del hist
    return dict(seed=seed,n=n,m=f.M,T=T,dt=dt,arm=arm,trace=traces,final=scores(f,data)[0])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--data',type=Path,nargs='+',required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--seeds',type=int,nargs='+',required=True)
    p.add_argument('--width',type=int,default=256)
    p.add_argument('--horizon',type=float,default=32.)
    p.add_argument('--dt',type=float,default=1/16)
    p.add_argument('--device',default='cuda:1')
    p.add_argument('--continue-five',action='store_true')
    p.add_argument('--causal',action='store_true')
    p.add_argument('--max-seconds',type=float,default=4500)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    sources=['stage2_coord_experiment.py','baseline_compact_flow.py','history_probe.py',
             'STAGE2_COORD_PROTOCOL.md','STAGE2_COORD_THEORY.md']
    for name in sources:shutil.copy2(HERE/name,a.out/name)
    manifest=dict(command=sys.argv,python=sys.executable,torch=torch.__version__,numpy=np.__version__,
                  platform=platform.platform(),device=a.device,threads=torch.get_num_threads(),dtype='float64',tf32=False,
                  source_hashes={s:sha(HERE/s) for s in sources},input_hashes={str(s):sha(s) for s in a.data},
                  started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    dump(a.out/'manifest.json',manifest);start=time.perf_counter();rows=[];solves=0
    try:
        for path in a.data:
            data=dict(np.load(path));domain=path.stem
            for split in ('train','val','test'):
                x=data['X_'+split]
                if not np.allclose(np.linalg.norm(x,axis=1),1,atol=1e-7):raise ValueError('Input row norms')
            for seed in a.seeds:
                if time.perf_counter()-start>a.max_seconds:raise RuntimeError('Wall-time cap')
                arms=('none','q1','reverse','sign','gradient') if a.causal else ('endpoint',)
                for arm in arms:
                    begin=time.perf_counter()
                    if a.causal:
                        result=causal_case(data,a.width,seed,a.device,a.horizon,a.dt,arm);arrays={};solves+=1
                    else:
                        result,arrays=endpoint_case(data,a.width,seed,a.device,a.horizon,a.dt,a.continue_five)
                        solves+=6 if a.continue_five else 1
                    result.update(domain=domain,seconds=time.perf_counter()-begin)
                    name=f'{domain}_seed{seed}_{arm}'
                    dump(a.out/(name+'.json'),result)
                    if arrays:np.savez_compressed(a.out/(name+'.npz'),**arrays)
                    rows.append(result)
                    dump(a.out/'results.json',rows)
                    print(json.dumps(dict(case=name,seconds=result['seconds'],solves=solves,
                              base=result.get('base',result.get('final')),feature_motion=result.get('feature_motion'),
                              reverse=result.get('edits',{}).get('reverse'))),flush=True)
        dump(a.out/'completion.json',dict(exit_status=0,seconds=time.perf_counter()-start,solves=solves,
             output_hashes={s.name:sha(s) for s in a.out.glob('*.npz')}))
    except Exception as exc:
        dump(a.out/'failure.json',dict(error=repr(exc),seconds=time.perf_counter()-start,solves=solves));raise


if __name__=='__main__':main()
