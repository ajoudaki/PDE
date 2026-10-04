"""Bounded historical-pairing interventions; see HISTORY_PROTOCOL.md.

Observer histories are recorded along baseline dense Euler training. They are
not supplied to an autonomous closure. Prefix-free temporal means are deliberate.
"""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import torch
from baseline_compact_flow import Flow

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
torch.set_num_threads(1)
torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.allow_tf32 = False


def teacher(angle):
    return np.sin(angle) + .5*np.sin(3*angle)


def make_data(m=12, test_count=512):
    angle = np.arange(m)*2*np.pi/m+.13
    query_angle = (np.arange(test_count)+.5)*2*np.pi/test_count
    x = np.stack((np.cos(angle), np.sin(angle)), 1)
    query = np.stack((np.cos(query_angle), np.sin(query_angle)), 1)
    return x, teacher(angle), query, teacher(query_angle)


def new_flow(x, y, n, seed, device):
    model = Flow(x, y, width=n, depth=2, activation='tanh', order=None,
                 seed=seed, device=device, dtype=torch.float64,
                 hidden_gain=1., readout_std=1.)
    model.c.zero_()
    return model


@torch.no_grad()
def train_record(model, horizon, dt):
    count = round(horizon/dt)
    if abs(count*dt-horizon)>1e-10:
        raise ValueError('Horizon must be a whole number of steps')
    initial = model.matrices[0].clone()
    hs, bs, masses = [], [], []
    # Scaled power moments are an invertible coordinate representation of the
    # first eight Legendre moments. Exact interval insertion avoids recording
    # a trajectory for the eventual repair; saved histories are an audit only.
    online_h=model.w.new_zeros((8,model.n,model.M))
    online_b=torch.zeros_like(online_h)
    degree=torch.arange(8,device=model.device,dtype=model.dtype)[:,None,None]
    activity=0.
    per_sample = model.w.new_zeros((model.M, model.n, model.n))
    begin = time.perf_counter()
    for _ in range(count):
        hidden, delta, r = model._fields()
        rho = r.square().mean().sqrt()
        value = float(rho)
        if not math.isfinite(value):
            raise RuntimeError('Nonfinite trajectory')
        h, write = hidden[0], delta[1]*r
        hs.append(h.clone())
        b=write/rho if value>0 else torch.zeros_like(write)
        bs.append(b)
        masses.append(value*dt)
        next_activity=activity+value*dt
        if next_activity>0:
            scale=activity/next_activity
            transport=scale**degree
            insertion=next_activity*(1-scale**(degree+1))/(degree+1)
            online_h.mul_(transport).add_(insertion*h)
            online_b.mul_(transport).add_(insertion*b)
        activity=next_activity
        per_sample.add_(torch.einsum('ia,ja->aij',write,h), alpha=-2*dt/(model.M*model.n))
        # Source step is retained exactly; the observer never changes its RHS.
        model.step(dt)
    elapsed = time.perf_counter()-begin
    exact = model.matrices[0]-initial
    parity = float((per_sample.sum(0)-exact).norm()/exact.norm().clamp_min(1e-30))
    if parity>1e-10:
        raise AssertionError(('Discrete update observer mismatch',parity))
    conversion=np.zeros((8,8))
    for k in range(8):
        polynomial=np.polynomial.Legendre.basis(k).convert(kind=np.polynomial.Polynomial)
        shifted=polynomial(np.polynomial.Polynomial([-1,2]))
        conversion[k,:len(shifted.coef)]=shifted.coef
    conversion=torch.as_tensor(conversion,device=model.device,dtype=model.dtype)
    normalization=((2*degree+1)/activity).sqrt()
    online_h=torch.einsum('kj,jia->kia',conversion,online_h)*normalization
    online_b=torch.einsum('kj,jia->kia',conversion,online_b)*normalization
    return dict(h=torch.stack(hs), b=torch.stack(bs), mass=np.asarray(masses),
                online_h=online_h,online_b=online_b,
                per_sample=per_sample, initial=initial, parity=parity, seconds=elapsed)


def interval_coefficients(mass, q):
    """Exact integrals of normalized Legendre modes over activity intervals."""
    total = mass.sum()
    if total<=0:
        raise ValueError('No learning interval')
    edges = np.r_[0.,np.cumsum(mass)]/total
    z=2*edges-1
    polynomials=np.polynomial.legendre.legvander(z,q)
    integrals=np.empty((q,len(mass)),dtype=np.float64)
    integrals[0]=mass
    for k in range(1,q):
        primitive=(polynomials[:,k+1]-polynomials[:,k-1])/(2*(2*k+1))
        integrals[k]=total*np.diff(primitive)
    return np.sqrt((2*np.arange(q)+1)/total)[:,None]*integrals


@torch.no_grad()
def project(history, q):
    matrix=torch.as_tensor(interval_coefficients(history['mass'],q),
                           device=history['h'].device,dtype=history['h'].dtype)
    shape=(q,*history['h'].shape[1:])
    h=(matrix@history['h'].flatten(1)).reshape(shape)
    b=(matrix@history['b'].flatten(1)).reshape(shape)
    return h,b


def interaction(h,b,n,m):
    return (-2/(n*m))*torch.einsum('kia,kja->ij',b,h)


def metrics(model, query, truth):
    train=float(((model.predict(model.inputs)-model.labels)**2).mean())
    pred=model.predict(query)
    target=torch.as_tensor(truth,device=model.device,dtype=model.dtype)
    return dict(train_mse=train,test_mse=float(((pred-target)**2).mean()))


def rotated(b, seed):
    g=torch.Generator(device=b.device).manual_seed(seed)
    q=b.shape[0]-1
    rotation=torch.linalg.qr(torch.randn((q,q),generator=g,device=b.device,dtype=b.dtype)).Q
    return torch.cat((b[:1],torch.einsum('kj,jia->kia',rotation,b[1:]))),rotation


def singular_matched(delta, seed):
    g=torch.Generator(device=delta.device).manual_seed(seed)
    left=torch.linalg.qr(torch.randn(delta.shape,generator=g,device=delta.device,dtype=delta.dtype)).Q
    right=torch.linalg.qr(torch.randn(delta.shape,generator=g,device=delta.device,dtype=delta.dtype)).Q
    singular=torch.linalg.svdvals(delta)
    return (left*singular)@right.T


@torch.no_grad()
def edit_score(model, delta, query, truth, clean_y=None, clean_horizon=0.,dt=1/64):
    edited=copy.deepcopy(model)
    edited.matrices[0].add_(delta)
    if clean_y is not None:
        edited.labels.copy_(torch.as_tensor(clean_y,device=edited.device,dtype=edited.dtype))
    immediate=metrics(edited,query,truth)
    for _ in range(round(clean_horizon/dt)):
        edited.step(dt)
    return dict(immediate=immediate,after_clean=metrics(edited,query,truth),
                edit_norm=float(delta.norm()))


@torch.no_grad()
def run_case(n,seed,horizon,dt,device,corrupt):
    x,y,query,truth=make_data()
    labels=y.copy()
    bad=[1,7]
    if corrupt: labels[bad]*=-1
    model=new_flow(x,labels,n,seed,device)
    initial_h=model._forward(model.inputs,None)[0]
    history=train_record(model,horizon,dt)
    whole=history['per_sample'].sum(0)
    bad_exact=history['per_sample'][bad].sum(0)
    projections={}
    quality=[]
    for q in (1,4,8,16,32,64):
        h,b=project(history,q)
        projections[q]=(h,b)
        approx=interaction(h,b,n,model.M)
        bad_approx=interaction(h[:,:,bad],b[:,:,bad],n,model.M)
        quality.append(dict(q=q,total_relative_error=float((approx-whole).norm()/whole.norm()),
                            bad_relative_error=float((bad_approx-bad_exact).norm()/bad_exact.norm())))
        if q==32 and quality[-1]['total_relative_error']<=.02 and quality[-1]['bad_relative_error']<=.02:
            break
    final_h=model._forward(model.inputs,None)[0]
    online_error=max(float((history['online_h']-projections[8][0]).norm()/projections[8][0].norm()),
                     float((history['online_b']-projections[8][1]).norm()/projections[8][1].norm()))
    if online_error>1e-6:
        raise AssertionError(('Online/offline memory mismatch',online_error))
    result=dict(seed=seed,n=n,horizon=horizon,dt=dt,corrupt=corrupt,
                baseline=metrics(model,query,truth),projection=quality,
                update_parity=history['parity'],training_seconds=history['seconds'],
                online_offline_memory_relative_error=online_error,
                hidden_increment_norm_over_n=float(whole.norm()/n),
                feature_motion=[float((v-u).norm()/u.norm()) for u,v in zip(initial_h,final_h)])
    if corrupt:
        zero=torch.zeros_like(whole)
        edits={'no_edit':zero,'exact_history':-bad_exact}
        for q in (1,4,8):
            h,b=history['online_h'][:q],history['online_b'][:q]
            edits['moment_q'+str(q)]=-interaction(h[:,:,bad],b[:,:,bad],n,model.M)
        clean=copy.deepcopy(model)
        clean.labels.copy_(torch.as_tensor(y,device=model.device,dtype=model.dtype))
        clean_gradient=clean.rhs()[1]
        edits['current_gradient']=clean_gradient*(bad_exact.norm()/clean_gradient.norm())
        result['repair']={name:edit_score(model,delta,query,truth,y,2.,dt)
                          for name,delta in edits.items()}
    else:
        q=quality[-1]['q']; h,b=projections[q]
        approximation=interaction(h,b,n,model.M)
        covariance=interaction(h[1:],b[1:],n,model.M)
        result['coordination_q']=q
        result['covariance_fraction']=float(covariance.norm()/whole.norm())
        result['coordination']={
            'remove_centered':edit_score(model,-covariance,query,truth),
            'half_centered':edit_score(model,-.5*covariance,query,truth)}
        invariant=[]; second_moment=[]
        for j in range(5):
            b_new,rotation=rotated(b,7000+seed*10+j)
            h_new=torch.cat((h[:1],torch.einsum('kj,jia->kia',rotation,h[1:])))
            invariant.append(float((interaction(h_new,b_new,n,model.M)-approximation).norm()/whole.norm()))
            old=b[1:].flatten(1); new=b_new[1:].flatten(1)
            # Frobenius norm plus one fixed sample's neuron second moment.
            old_sample=b[1:,:,0];new_sample=b_new[1:,:,0]
            second_moment.append(float((old_sample.T@old_sample-new_sample.T@new_sample).norm()/
                                       (old_sample.T@old_sample).norm()))
            delta=interaction(h,b_new,n,model.M)-approximation
            result['coordination']['rotate_'+str(j)]=edit_score(model,delta,query,truth)
            random_delta=singular_matched(delta,9000+seed*10+j)
            result['coordination']['random_'+str(j)]=edit_score(model,random_delta,query,truth)
        result['simultaneous_rotation_relative_error']=max(invariant)
        result['preserved_second_moment_relative_error']=max(second_moment)
        if max(invariant)>1e-10 or max(second_moment)>1e-10:
            raise AssertionError('Temporal rotation invariant failed')
    arrays={key:value.detach().cpu().numpy() for key,value in
            dict(first=model.w,hidden=model.matrices[0],readout=model.c,
                 exact_per_sample=history['per_sample']).items()}
    arrays.update(x=x,labels=labels,clean_labels=y,query=query,truth=truth,
                  mass=history['mass'])
    for q,(h,b) in projections.items():
        arrays['h_coeff_'+str(q)]=h.cpu().numpy();arrays['b_coeff_'+str(q)]=b.cpu().numpy()
    return result,arrays


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--seeds',type=int,nargs='+',default=[101,102,103])
    p.add_argument('--width',type=int,default=128)
    p.add_argument('--horizon',type=float,default=32.)
    p.add_argument('--dt',type=float,default=1/64)
    p.add_argument('--device',default='cpu')
    p.add_argument('--panel',choices=['both','coordination','repair'],default='both')
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    manifest=dict(command=sys.argv,python=sys.executable,torch=torch.__version__,numpy=np.__version__,
                  platform=platform.platform(),device=a.device,threads=torch.get_num_threads(),
                  tf32=False,head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                  source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                 for name in ['history_probe.py','baseline_compact_flow.py','HISTORY_PROTOCOL.md']},
                  started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),config=vars(a)|{'out':str(a.out)})
    (a.out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    results=[];start=time.perf_counter()
    try:
        for seed in a.seeds:
            for corrupt in ([False,True] if a.panel=='both' else [a.panel=='repair']):
                result,arrays=run_case(a.width,seed,a.horizon,a.dt,a.device,corrupt)
                results.append(result)
                name=f'seed{seed}_'+('repair' if corrupt else 'coordination')
                np.savez_compressed(a.out/(name+'.npz'),**arrays)
                (a.out/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
                print(json.dumps(result),flush=True)
                if time.perf_counter()-start>600 and a.device=='cpu':
                    raise RuntimeError('CPU screen cap reached')
        (a.out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
        (a.out/'completion.json').write_text(json.dumps(dict(exit_status=0,seconds=time.perf_counter()-start,
             hashes={v.name:hashlib.sha256(v.read_bytes()).hexdigest() for v in a.out.glob('*.npz')}),indent=2)+'\n')
    except Exception as e:
        (a.out/'failure.json').write_text(json.dumps(dict(error=repr(e),seconds=time.perf_counter()-start),indent=2)+'\n')
        raise


if __name__=='__main__':main()
