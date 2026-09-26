"""Independent small-CPU checks of the frozen p4/p5 formulas; no training.

The expected fields are evaluated directly at numerical symbolic-label values
from P45_DERIVATION_ROUTE.md, without the builder's polynomial operations.
Population scalar moments stay population moments at finite carrier size.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np
import torch

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"code"))
sys.path.insert(0,str(HERE))
from pde.observable_torch_p1 import TensorState
import new_dictionary as old
import new_dictionary_p45 as candidate


def moments():
    # Probabilists' Hermite rule: independent normalization and 2D contractions.
    nodes,weight=np.polynomial.hermite_e.hermegauss(256)
    weight=weight/np.sqrt(2*np.pi)
    h=np.tanh(nodes); lower_gate=1-h*h
    v=float(weight@(h*h))
    H=np.tanh(np.sqrt(v)*nodes); d=1-H*H
    second=-2*H*d
    lam_same=float(weight@(h*h*lower_gate**2))*float(weight@(d*d+H*second))
    lam_cross=v*float(weight@lower_gate**2)*float(weight@d)**2
    lam=np.array([[lam_same,lam_cross],[lam_cross,lam_same]])
    Hxy=np.broadcast_arrays(H[:,None],H[None,:])
    dxy=np.broadcast_arrays(d[:,None],d[None,:])
    product_weights=weight[:,None]*weight[None,:]
    gram=np.empty((2,2,2))
    for a in range(2):
        for b in range(2):
            for k in range(2):
                gram[a,b,k]=np.sum(product_weights*Hxy[k]**2*dxy[a]*dxy[b])
    return dict(v=v,tau=float(weight@(H*H)),mean_d=float(weight@d),
                mean_d2=float(weight@(d*d)),mean_H2d=float(weight@(H*H*d)),
                mean_H2d2=float(weight@(H*H*d*d)),lam=lam,g=gram)


@torch.no_grad()
def direct_fields(initial,y,constants):
    """Direct numerical-label equations (2), (7), (9), (14), (17)."""
    W=initial.M
    h=torch.tanh(initial.w);H=torch.tanh(W@h)
    ell=1-h*h;lower_second=-2*h*ell
    d=1-H*H;second=-2*H*d
    # Different expression for tanh''' from the builder's factored form.
    third=-2+8*H*H-6*H**4
    S=H@y
    q=[];V=[];R=[]
    for a in range(2):
        q.append(y[a]*ell[:,a]*(W.T@(S*d[:,a]))/2)
        V.append(ell[:,a]*q[a])
        R.append(constants['v']*y[a]*S*d[:,a]/2+W@V[a])
    J=sum(y[b]*d[:,b]*R[b] for b in range(2))
    K3=[d[:,a]*J/3+S*second[:,a]*R[a] for a in range(2)]
    T=[];E=[]
    for a in range(2):
        B2adj=sum(y[b]*h[:,b]*sum(y[k]**2*constants['g'][a,b,k] for k in range(2))/2
                  for b in range(2))
        T.append(y[a]*ell[:,a]**2*(W.T@K3[a]+B2adj)/4+lower_second[:,a]*q[a]**2)
    for a in range(2):
        correction=sum(y[b]**2*constants['lam'][a,b]*S*d[:,b] for b in range(2))
        E.append(W@T[a]+constants['v']*y[a]*K3[a]/4+3*y[a]*correction/8)
    N=sum(y[b]*(d[:,b]*E[b]+second[:,b]*R[b]**2/2) for b in range(2))
    K5=[d[:,a]*N/5+J*second[:,a]*R[a]/3+S*second[:,a]*E[a]+S*third[:,a]*R[a]**2/2
        for a in range(2)]
    return T,K5


def compressed_prediction(w,c,M,b1,b2,inputs):
    dense=b2@M@b1.T/len(w)
    return torch.tanh(dense@torch.tanh(w@inputs.T)).T@c/len(c)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,default=ROOT/'data/generated/gradient_flow_probe_dictionary_20260921/p45_implementation_check01')
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1)
    constants=moments();recorded=candidate.population_moments()['working']
    checks=[]
    def check(name,observed,expected=0.,tolerance=1e-10):
        observed=torch.as_tensor(observed,dtype=torch.float64)
        expected=torch.as_tensor(expected,dtype=torch.float64)
        error=float((observed-expected).abs().max())
        passed=math.isfinite(error) and error<=tolerance
        checks.append(dict(name=name,maximum_absolute_error=error,tolerance=tolerance,passed=passed))
        if not passed:
            print(json.dumps(checks[-1]),flush=True)
        return error
    for key,value in constants.items():
        check('independent Gaussian moment '+key,recorded[key],value,2e-13)
    labels=[(0.,0.),(1.,0.),(0.,1.),(1.,1.),(1.,-1.),(.7,-1.3),(-1.4,.2),(2.1,.35)]
    cases=[]
    for seed in (9,41):
        generator=torch.Generator(device='cpu').manual_seed(seed)
        n=37
        w=torch.randn(n,2,generator=generator,dtype=torch.float64)
        W=torch.randn(n,n,generator=generator,dtype=torch.float64)/math.sqrt(n)
        c=torch.randn(n,generator=generator,dtype=torch.float64)/n
        initial=TensorState(w,c,W)
        initial_copy=[x.clone() for x in (w,c,W)]
        base=old.raw_features(initial,3)
        p4=candidate.raw_features(initial,4)
        p5=candidate.raw_features(initial,5)
        for layer in (0,1):
            check(f'seed{seed} p4 exact raw p3 layer{layer}',p4[layer],base[layer],0)
            check(f'seed{seed} p5 preserved p3 layer{layer}',p5[layer][:,:base[layer].shape[1]],base[layer],0)
        check(f'seed{seed} p4 dimensions',[p4[0].shape[1],p4[1].shape[1]],[6,12],0)
        check(f'seed{seed} p5 dimensions',[p5[0].shape[1],p5[1].shape[1]],[14,24],0)
        for label in labels:
            y=torch.tensor(label,dtype=torch.float64)
            lower,upper=direct_fields(initial,y,constants)
            for a in range(2):
                lower_monomials=torch.tensor([y[0]**(4-j)*y[1]**j for j in range(a,a+4)])
                upper_monomials=torch.tensor([y[0]**(5-j)*y[1]**j for j in range(6)])
                # Remove the builder's declared raw derivative factorials.
                from_lower=p5[0][:,6+4*a:10+4*a]@lower_monomials/24
                from_upper=p5[1][:,12+6*a:18+6*a]@upper_monomials/120
                check(f'seed{seed} labels{label} T{a+1}',from_lower,lower[a])
                check(f'seed{seed} labels{label} K5_{a+1}',from_upper,upper[a])
        for p in (4,5):
            engine,state,metadata=candidate.build(initial,p,block_size=3)
            raw=p4 if p==4 else p5
            check(f'seed{seed} p{p} initial readin',state.w,w,0)
            check(f'seed{seed} p{p} retained nonzero readout',state.c,c,0)
            check(f'seed{seed} p{p} projected coefficient initialization',state.M,engine.b2.T@(W@engine.b1)/n)
            filtered=(engine.b2@engine.b2.T/n)@W@(engine.b1@engine.b1.T/n)
            check(f'seed{seed} p{p} two-sided filtered initialization',engine.b2@state.M@engine.b1.T/n,filtered)
            eta=1/(1024*(p+1)**2)
            for layer,basis in enumerate((engine.b1,engine.b2)):
                psi=raw[layer]
                factor=torch.linalg.cholesky(psi.T@psi/n+eta*torch.eye(psi.shape[1],dtype=torch.float64))
                independently_normalized=torch.linalg.solve_triangular(factor,psi.T,upper=False).T
                check(f'seed{seed} p{p} ridge basis layer{layer}',basis,independently_normalized)
            # A nontrivial moving state checks all three gradients, rather than
            # relying on the near-zero finite initialized readout.
            moved=engine.state(w+.1*torch.randn(w.shape,generator=generator,dtype=w.dtype),
                               c+.25*torch.randn(c.shape,generator=generator,dtype=c.dtype),
                               state.M+.1*torch.randn(state.M.shape,generator=generator,dtype=state.M.dtype))
            angles=torch.arange(11,dtype=torch.float64)*(2*math.pi/11)+.13
            inputs=torch.stack([angles.cos(),angles.sin()],1)
            target=torch.linspace(-1.2,.8,11,dtype=torch.float64)
            data=engine.prepare_data(inputs,target)
            rhs=engine.rhs(moved,data)
            aw,ac,am=[x.clone().requires_grad_(True) for x in (moved.w,moved.c,moved.M)]
            predicted=compressed_prediction(aw,ac,am,engine.b1,engine.b2,inputs)
            loss=(predicted-target).square().mean()
            gradients=torch.autograd.grad(loss,(aw,ac,am))
            check(f'seed{seed} p{p} independent dense prediction',engine.predict(moved,inputs),predicted.detach())
            for name,value,gradient,mobility in zip(('w','c','M'),(rhs.w,rhs.c,rhs.M),gradients,(n,n,1)):
                check(f'seed{seed} p{p} full-batch autograd {name}',value,-mobility*gradient)
            cases.append(dict(seed=seed,p=p,width=n,K1=metadata['K1'],K2=metadata['K2'],
                ridge=eta,lower_condition=metadata['lower']['ridge_condition'],
                upper_condition=metadata['upper']['ridge_condition']))
        for name,value,original in zip(('w','c','M'),(initial.w,initial.c,initial.M),initial_copy):
            check(f'seed{seed} untouched supplied {name}',value,original,0)
    paths=[HERE/'new_dictionary_p45.py',HERE/'new_dictionary.py',HERE/'P45_DERIVATION_ROUTE.md',
           HERE/'P45_PROTOCOL.md',Path(__file__),ROOT/'code/pde/observable_torch_p1.py']
    output=dict(passed=all(x['passed'] for x in checks),checks=checks,total_checks=len(checks),
        maximum_error=max(x['maximum_absolute_error'] for x in checks),
        cases=cases,device='cpu',dtype='float64',torch=str(torch.__version__),numpy=np.__version__,
        independent_moments={k:np.asarray(v).tolist() for k,v in constants.items()},
        candidate_quadrature_discrepancy=candidate.population_moments()['maximum_discrepancy'],
        source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        scientific_scope='Direct finite-carrier evaluation of prescribed population-derived frozen fields; no claim of empirical finite-network jet matching.')
    (args.out/'validation.json').write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:output[k] for k in ('passed','total_checks','maximum_error','candidate_quadrature_discrepancy')}),flush=True)


if __name__=='__main__':
    main()
