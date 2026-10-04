"""Independent float64 identities and autograd checks; no training campaign."""
import argparse
import json
from pathlib import Path
import numpy as np
import torch
from stage2_index_experiment import pca, make, sha


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
    rng=np.random.default_rng(90771);errors={}
    def close(name,a,b,tol=1e-10):
        aa=np.asarray(a);bb=np.asarray(b);error=float(np.max(np.abs(aa-bb)))
        errors[name]=error
        if error>tol:raise AssertionError((name,error))
    h=torch.tensor(rng.normal(size=(11,37)))
    b=torch.tensor(rng.normal(size=(11,37)))
    psi,v,lam,_=pca(h,5)
    close('adaptive_gradient_identity',(b@psi/37)@(h@psi/37).T,(b@h.T/37)@v@v.T)
    close('pca_orthogonality',psi.T@psi/37,np.eye(5))
    # Nonlinear backward propagation and the canonical mobility are checked
    # against autograd, independently of inherited hand-coded RHS routines.
    x=rng.normal(size=(40,7));x/=np.linalg.norm(x,axis=1,keepdims=True)
    data=dict(X_train=x,y_train=rng.normal(size=40))
    for config in [dict(kind='dense'),dict(kind='factor',rate=4.),dict(kind='projected')]:
        config['seed']=90771
        model=make(config,data,'cpu',torch.float64)
        model.c.copy_(torch.tensor(rng.normal(size=128)))
        if config['kind']=='factor':model.factors[0][0].copy_(torch.tensor(rng.normal(size=(128,24))*.01))
        params=[s.detach().clone().requires_grad_(True) for s in model.state]
        if config['kind']=='dense':w,W,c=params
        elif config['kind']=='factor':
            w,c,a,bb=params;W=model.matrices[0]+a@bb
        else:
            w,c,a=params;W=model.matrices[0]+a@model.V.T
        pred=c@torch.tanh(W@torch.tanh(w@model.inputs.T))/128
        loss=(pred-model.labels).square().mean()
        grads=torch.autograd.grad(loss,params)
        rates=[128,1,128] if config['kind']=='dense' else [128,128]+[config.get('rate',1.)]*(len(params)-2)
        for i,(got,g,rate) in enumerate(zip(model.rhs(),grads,rates)):
            close(f'{config["kind"]}_autograd_{i}',got,-rate*g.detach())
    # An input mode outside the retained span is invisible to every old mode.
    q,_=np.linalg.qr(rng.normal(size=(17,17)))
    old=q[:,:4];new=q[:,4:8];g=new[:,0]
    close('old_indistinguishability',old.T@g,np.zeros(4))
    close('new_distinguishability',new.T@g,np.array([1,0,0,0]))
    # Continuously moving write-time bases: exact quadrature of the joint
    # projection and independent reconstruction/tail decomposition.
    nodes,weights=np.polynomial.legendre.leggauss(80);t=(nodes+1)/2;weights/=2
    m=17;c=4;order=3
    base=q[:,:c]*np.sqrt(m)
    moving=[]
    for z in t:
        rotation=np.eye(c);ang=2*np.pi*z
        rotation[:2,:2]=[[np.cos(ang),-np.sin(ang)],[np.sin(ang),np.cos(ang)]]
        moving.append(base@rotation)
    moving=np.asarray(moving)
    poly=np.polynomial.legendre.legvander(2*t-1,order-1)
    basis=np.einsum('tmc,tj->tmcj',moving,poly).reshape(len(t),m,c*order)
    mass=weights[:,None]/m
    gram=np.einsum('tmk,tml,tm->kl',basis,basis,np.broadcast_to(mass,(len(t),m)))
    norm=np.tile(1/(2*np.arange(order)+1),c)
    close('write_time_joint_orthogonality',gram,np.diag(norm))
    hh=rng.normal(size=(len(t),m,3));bb=rng.normal(size=(len(t),m,2))
    hc=np.einsum('tmi,tmk,tm->ik',hh,basis,np.broadcast_to(mass,(len(t),m)))
    bc=np.einsum('tmi,tmk,tm->ik',bb,basis,np.broadcast_to(mass,(len(t),m)))
    hp=np.einsum('ik,tmk->tmi',hc/norm,basis)
    bp=np.einsum('ik,tmk->tmi',bc/norm,basis)
    true=np.einsum('tmi,tmj,tm->ij',bb,hh,np.broadcast_to(mass,(len(t),m)))
    tail=np.einsum('tmi,tmj,tm->ij',bb-bp,hh-hp,np.broadcast_to(mass,(len(t),m)))
    close('write_time_product_tail',true,(bc/norm)@hc.T+tail)
    # Pure gauge motion can erase q=1 coefficients in a constant spatial span.
    coeff=np.einsum('t,tmc,m->c',weights,moving,base[:,0])/m
    close('rotating_gauge_zero_coefficients',coeff,np.zeros(c))
    # Exact reindexing can only recover old spatial projection.
    eta=base*.7+q[:,4:8]*np.sqrt(m)*np.sqrt(1-.7**2)
    source=rng.normal(size=(6,m))
    oldc=source@base/m;R=base.T@eta/m
    close('overlap_transport_error',source@eta/m-oldc@R,
          (source-oldc@base.T)@eta/m)
    out=dict(status='pass',checks=len(errors),maximum_error=max(errors.values()),errors=errors,
             sources={p.name:sha(p) for p in [Path(__file__),Path(__file__).with_name('stage2_index_experiment.py'),
                       Path(__file__).with_name('STAGE2_INDEX_THEORY.md')]})
    (args.out/'checks.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
