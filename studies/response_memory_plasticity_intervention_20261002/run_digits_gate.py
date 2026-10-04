"""One frozen digits concept-drift gate; see PROTOCOL.md."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np
import torch
from sklearn.datasets import load_digits

PARTITIONS = [(0,2,5,8,9),(0,2,3,4,8),(0,2,4,6,8),(0,1,5,6,7),
              (1,3,4,6,9),(2,3,4,5,9),(0,2,4,8,9),(0,1,2,4,5),
              (1,2,4,6,7),(0,2,3,4,5),(1,3,4,7,9),(1,3,4,5,8),
              (2,3,4,5,8),(0,1,2,3,9)]

def clone(state):
    return {k: v.clone() for k, v in state.items()}

def matrix(state, kind, W0, m):
    if kind == 'closure':
        return W0 - (2 / (len(W0) * m * state['tau'])) * (state['D'] @ state['H'].T)
    if kind == 'factor':
        return W0 + state['U'] @ state['V'].T
    return state['B']

def forward(state, B, X):
    h = torch.tanh(state['A'] @ X)
    g = torch.tanh(B @ h)
    return state['w'] @ g / len(B), h, g

def rhs(state, kind, W0, X, y):
    n, m = len(W0), X.shape[1]
    B = matrix(state, kind, W0, m)
    f, h, g = forward(state, B, X)
    r = f - y
    rho = torch.sqrt(torch.mean(r*r))
    delta = state['w'][:,None] * (1-g*g)
    credit = delta * r[None,:]
    ell = (1-h*h) * (B.T @ delta)
    common = {'A': -2/m * ((ell*r[None,:]) @ X.T),
              'w': -2/m * (g @ r)}
    G = 2/(n*m) * (credit @ h.T)
    if kind == 'closure':
        common.update(H=rho*h, D=credit, tau=rho)
    elif kind == 'dense':
        common.update(B=-G)
    else:
        dU = -(G @ state['V'])
        dV = -(G.T @ state['U'])
        raw = dU @ state['V'].T + state['U'] @ dV.T
        den = torch.linalg.vector_norm(raw)
        eta = torch.linalg.vector_norm(G) / torch.clamp(den, min=1e-300)
        common.update(U=eta*dU, V=eta*dV)
    return common

def gauge(state, X, orthogonal=False):
    h = torch.tanh(state['A'] @ X)
    hb = state['H'] / state['tau']
    eye = torch.eye(X.shape[1], dtype=X.dtype, device=X.device)
    gram = hb.T @ hb
    lam = .1 * torch.trace(gram) / len(gram)
    if orthogonal:
        u, _, vh = torch.linalg.svd(hb.T @ h)
        R = u @ vh
    else:
        R = torch.linalg.solve(gram+lam*eye, hb.T @ h+lam*eye)
        u, s, vh = torch.linalg.svd(R)
        R = (u * s.clamp(.5,2)[None,:]) @ vh
    out = clone(state)
    out['H'] = state['H'] @ R
    out['D'] = torch.linalg.solve(R, state['D'].T).T
    return out, R

def make_arm(checkpoint, arm, X, W0):
    state = clone(checkpoint)
    if arm in ('aligned', 'factor_aligned'):
        state, _ = gauge(state, X)
    if arm in ('orthogonal', 'factor_orthogonal'):
        state, _ = gauge(state, X, orthogonal=True)
    if arm == 'clock':
        state['H'] = state['H'] / state['tau']
        state['tau'] = torch.ones_like(state['tau'])
    if arm == 'balanced':
        c = torch.sqrt(torch.linalg.vector_norm(state['D']) /
                       torch.linalg.vector_norm(state['H'])).clamp(.5,2)
        state['H'] *= c
        state['D'] /= c
    if arm.startswith('factor'):
        state = {'A': state['A'], 'w':state['w'],
                 'U': -2*state['D']/(len(W0)*X.shape[1]*state['tau']), 'V':state['H']}
        if arm == 'factor_balanced':
            q, sigma, pt = torch.linalg.svd(state['U'] @ state['V'].T)
            rank = X.shape[1]
            roots = sigma[:rank].clamp(min=0).sqrt()
            state['U'] = q[:,:rank] * roots[None,:]
            state['V'] = pt[:rank,:].T * roots[None,:]
        return state, 'factor'
    if arm == 'dense':
        return {'A':state['A'], 'w':state['w'],
                'B':matrix(state,'closure',W0,X.shape[1])}, 'dense'
    return state, 'closure'

def exact_checks():
    torch.manual_seed(187)
    dtype = torch.float64
    n,m,d=7,5,3
    X=torch.randn(d,m,dtype=dtype)/math.sqrt(d)
    y=torch.randn(m,dtype=dtype)
    W0=torch.randn(n,n,dtype=dtype)/math.sqrt(n)
    state={'A':torch.randn(n,d,dtype=dtype),'w':torch.randn(n,dtype=dtype),
           'H':torch.randn(n,m,dtype=dtype),'D':torch.randn(n,m,dtype=dtype),
           'tau':torch.tensor(3.7,dtype=dtype)}
    B=matrix(state,'closure',W0,m)
    A=state['A'].clone().requires_grad_(); b=B.clone().requires_grad_()
    w=state['w'].clone().requires_grad_()
    loss=((w @ torch.tanh(b @ torch.tanh(A @ X))/n-y)**2).mean()
    gradA,gradB,gradw=torch.autograd.grad(loss,(A,b,w))
    vel=rhs(state,'closure',W0,X,y)
    errors={'A_scaling':float((vel['A']+n*gradA).abs().max()),
            'w_scaling':float((vel['w']+n*gradw).abs().max())}
    fs,_=make_arm(state,'factor',X,W0)
    U=fs['U'].clone().requires_grad_(); V=fs['V'].clone().requires_grad_()
    loss=((state['w'] @ torch.tanh((W0+U@V.T) @ torch.tanh(state['A']@X))/n-y)**2).mean()
    gu,gv=torch.autograd.grad(loss,(U,V))
    errors['factor_U']=float((gu-gradB@V).detach().abs().max())
    errors['factor_V']=float((gv-gradB.T@U).detach().abs().max())
    for arm in ['aligned','orthogonal','clock','balanced','factor','factor_aligned','factor_orthogonal','factor_balanced','dense']:
        s,kind=make_arm(state,arm,X,W0)
        errors['invariance_'+arm]=float((matrix(s,kind,W0,m)-B).abs().max())
    dotB=-2/(n*m*state['tau'])*(vel['D']@state['H'].T+state['D']@vel['H'].T-
                              vel['tau']/state['tau']*(state['D']@state['H'].T))
    f,h,g=forward(state,B,X); r=f-y; rho=r.square().mean().sqrt()
    credit=(state['w'][:,None]*(1-g*g))*r[None,:]
    defect=-2/(n*m)*((credit-rho*state['D']/state['tau'])@(state['H']/state['tau']-h).T)
    errors['velocity_identity']=float((dotB+gradB-defect).abs().max())
    errors['max_error']=max(errors.values())
    assert errors['max_error']<1e-10, errors
    return errors

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--device',default='cuda:0')
    parser.add_argument('--out',required=True)
    parser.add_argument('--seed',type=int,default=0)
    parser.add_argument('--dt',type=float,default=.1)
    parser.add_argument('--max-seconds',type=float,default=1130)
    parser.add_argument('--checks-only',action='store_true')
    args=parser.parse_args()
    torch.set_num_threads(1)
    torch.set_default_dtype(torch.float64)
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    checks=exact_checks()
    (out/'exact_checks.json').write_text(json.dumps(checks,indent=2))
    print('exact checks',checks,flush=True)
    if args.checks_only:return
    start=time.monotonic()
    device=torch.device(args.device)
    digits=load_digits(); rng=np.random.default_rng(20261002)
    train=[]; test=[]
    for c in range(10):
        ix=rng.permutation(np.flatnonzero(digits.target==c))
        train.extend(ix[:8].tolist()); test.extend(ix[8:48].tolist())
    raw=digits.data/16
    mean=raw[train].mean(0); scale=np.sqrt(np.mean((raw[train]-mean)**2))
    X=torch.as_tensor(((raw[train]-mean)/scale/math.sqrt(64)).T,device=device)
    Q=torch.as_tensor(((raw[test]-mean)/scale/math.sqrt(64)).T,device=device)
    def labels(k,indices):
        return torch.as_tensor(np.where(np.isin(digits.target[indices],PARTITIONS[k]),1.,-1.),device=device)
    torch.manual_seed(args.seed)
    A=torch.randn(256,64,device='cpu').to(device)
    W0=(torch.randn(256,256,device='cpu')/16).to(device)
    state={'A':A,'w':torch.zeros(256,device=device),'H':torch.tanh(A@X),
           'D':torch.zeros(256,80,device=device),'tau':torch.ones((),device=device)}
    hinit=state['H'].clone()
    source=Path(__file__)
    config={'args':vars(args),'partitions':PARTITIONS,'train_indices':train,'test_indices':test,
            'width':256,'duration':64,'torch':torch.__version__,'device':str(device),
            'gpu_name':torch.cuda.get_device_name(device) if device.type=='cuda' else None,
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'protocol_sha256':hashlib.sha256(source.with_name('PROTOCOL.md').read_bytes()).hexdigest()}
    (out/'config.json').write_text(json.dumps(config,indent=2))
    rows=[]
    def integrate(s,kind,k,speed,name):
        y=labels(k,train); yt=labels(k,test); rec=[]
        steps=round(64/args.dt); every=max(1,round(1/args.dt))
        dissB=dissAll=0.
        for step in range(steps+1):
            if step%every==0 or step==steps:
                B=matrix(s,kind,W0,80); f,_,_=forward(s,B,X); fq,_,_=forward(s,B,Q)
                rec.append([step*args.dt,float((f-y).square().mean()),
                            float((fq-yt).square().mean()),float(((fq>=0)==(yt>=0)).double().mean())])
                if not all(math.isfinite(z) for z in rec[-1]):raise FloatingPointError('nonfinite metrics')
                if time.monotonic()-start>args.max_seconds:raise TimeoutError('frozen process budget')
            if step==steps:break
            v=rhs(s,kind,W0,X,y)
            if kind=='dense' and step%every==0:
                middle=float(v['B'].square().sum()); total=middle+float(v['A'].square().sum()+v['w'].square().sum())/256
                dissB+=middle; dissAll+=total
            mid={key:val+.5*args.dt*speed*v[key] for key,val in s.items()}
            vm=rhs(mid,kind,W0,X,y)
            s={key:val+args.dt*speed*vm[key] for key,val in s.items()}
        ar=np.asarray(rec); np.save(out/(name+'.npy'),ar)
        return s,{'auc':float(np.trapz(ar[:,2],ar[:,0])),
                  'train_mse':float(ar[-1,1]),'test_mse':float(ar[-1,2]),'accuracy':float(ar[-1,3]),
                  'dense_middle_share':dissB/dissAll if dissAll else None}
    for k in range(12):
        state,metric=integrate(state,'closure',k,1,f'warmup_{k:02d}')
        rows.append({'phase':'warmup','block':k,**metric})
        print('warmup',k,metric,'seconds',round(time.monotonic()-start,1),flush=True)
    checkpoint=clone(state); B0=matrix(checkpoint,'closure',W0,80)
    f0,_,_=forward(checkpoint,B0,Q)
    metadata={'tau':float(state['tau']),
              'relative_h_movement':float(torch.linalg.vector_norm(torch.tanh(state['A']@X)-hinit)/torch.linalg.vector_norm(hinit)),
              'warmup_final_mse':rows[-1]['train_mse']}
    torch.save({'state':{k:v.cpu() for k,v in state.items()},'W0':W0.cpu(),'X':X.cpu(),'Q':Q.cpu()},out/'checkpoint.pt')
    (out/'checkpoint_metadata.json').write_text(json.dumps(metadata,indent=2))
    arms=[('aligned',1),('orthogonal',1),('untouched',1),('clock',1),('factor',1),('factor_aligned',1),('factor_orthogonal',1),
          ('factor_balanced',1),('dense',1),('balanced',1)]
    arms += [(arm,speed) for arm in ('untouched','clock','factor','factor_aligned','factor_balanced','dense') for speed in (.25,4)]
    for arm,speed in arms:
        name=f'{arm}_speed{speed:g}'; s,kind=make_arm(checkpoint,arm,X,W0)
        B=matrix(s,kind,W0,80); fj,_,_=forward(s,B,Q)
        jump=float((fj-f0).abs().max()); assert jump<1e-10,(arm,jump)
        try:
            s,first=integrate(s,kind,12,speed,name+'_probe1')
            s,second=integrate(s,kind,13,speed,name+'_probe2')
            row={'phase':'probe','arm':arm,'speed':speed,'function_jump':jump,
                 'probe1':first,'probe2':second,'status':'ok'}
        except (FloatingPointError,TimeoutError) as exc:
            row={'phase':'probe','arm':arm,'speed':speed,'status':type(exc).__name__,'error':str(exc)}
        rows.append(row)
        (out/'results.json').write_text(json.dumps({'metadata':metadata,'rows':rows,
            'elapsed_seconds':time.monotonic()-start},indent=2))
        print(name,json.dumps(row),'seconds',round(time.monotonic()-start,1),flush=True)
        if row['status']=='TimeoutError':break
    print('DONE',round(time.monotonic()-start,1),flush=True)

if __name__=='__main__':
    main()
