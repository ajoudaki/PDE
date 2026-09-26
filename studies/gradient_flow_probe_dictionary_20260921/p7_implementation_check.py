"""Independent CPU evaluation of the p6/p7 frozen dictionary implementation.

Scalar formal labels are algebra test inputs, never task labels used to
construct fields. Population moments remain fixed deterministic constants.
"""
import argparse
import hashlib
import importlib
import json
import math
from pathlib import Path
import sys
from functools import lru_cache
import numpy as np
import torch

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'code'))
sys.path.insert(0,str(HERE))
from pde.observable_torch_p1 import TensorState
import new_dictionary_p45 as previous
from p7_gaussian_check import population_contractions


def monomials(y,degree):
    return np.array([y[0]**(degree-j)*y[1]**j for j in range(degree+1)])


@lru_cache(maxsize=1)
def beta_constants():
    """Independent one-dimensional symmetry reduction of the output cubic."""
    z,w=np.polynomial.hermite_e.hermegauss(256)
    w=w/np.sqrt(2*np.pi)
    h=np.tanh(z);ell=1-h*h
    v=previous.previous._variance_rules()[1]
    H=np.tanh(np.sqrt(v)*z);d=1-H*H
    mean_ell2=w@(ell*ell)
    mu=w@(d*d-2*H*H*d)
    same=(v+mean_ell2)*(w@(H*H*d*d))+(w@(h*h*ell*ell))*mu*mu
    other=(v+mean_ell2)*(w@(H*H))*(w@(d*d))+v*mean_ell2*(w@d)**4
    return 2*np.array([same,other])/3


def direct_fields(w,W,y,constants):
    """Equations (2)--(9) evaluated at one scalar formal-label pair.

    No homogeneous-polynomial helper or candidate implementation is used.
    All learned-operator actions are explicit sums of their scalar pairings.
    """
    y=np.asarray(y)
    v=constants['v']
    h=np.tanh(w);H=np.tanh(W@h)
    ell=1-h*h;lm=-2*h*ell;ln=-2+8*h*h-6*h**4
    d=1-H*H;e=-2*H*d;f=-2+8*H*H-6*H**4
    fourth=16*H-40*H**3+24*H**5
    S=H@y
    U=d[:,:,None]*H[:,None,:]
    Q=(W.T@U.reshape(len(w),4)).reshape(len(w),2,2)
    L=ell[:,:,None]**2*Q
    F=v*U+(W@L.reshape(len(w),4)).reshape(len(w),2,2)
    Uy=[S*d[:,a] for a in range(2)]
    q=[y[a]*ell[:,a]*(W.T@Uy[a])/2 for a in range(2)]
    V=[ell[:,a]*q[a] for a in range(2)]
    R=[v*y[a]*Uy[a]/2+W@V[a] for a in range(2)]
    J=sum(y[b]*d[:,b]*R[b] for b in range(2))
    K3=[d[:,a]*J/3+S*e[:,a]*R[a] for a in range(2)]
    C=constants['C'].reshape(2,2,2,2)
    hv=constants['hV']@monomials(y,2)
    ht=constants['hT']@monomials(y,4)
    vv=constants['VV']@monomials(y,4)
    uk=constants['UK']@monomials(y,3)
    uu=np.einsum('c,k,b c a k->b a',y,y,C)
    B2U=[sum(y[b]*h[:,b]*uu[b,a]/2 for b in range(2)) for a in range(2)]
    P4=[y[a]*ell[:,a]*(W.T@K3[a]+B2U[a])/4
        +y[a]*lm[:,a]*q[a]*(W.T@Uy[a])/4 for a in range(2)]
    T=[ell[:,a]*P4[a]+lm[:,a]*q[a]**2/2 for a in range(2)]
    E=[]
    for a in range(2):
        B2V=sum(y[b]*Uy[b]*hv[b,a]/2 for b in range(2))
        B4h=sum(y[b]*(K3[b]*(v if a==b else 0)+Uy[b]*hv[a,b])/4 for b in range(2))
        E.append(W@T[a]+B2V+B4h)
    N=sum(y[b]*(d[:,b]*E[b]+e[:,b]*R[b]**2/2) for b in range(2))
    K5=[d[:,a]*N/5+J*e[:,a]*R[a]/3+S*e[:,a]*E[a]+S*f[:,a]*R[a]**2/2 for a in range(2)]
    T6=[]
    for a in range(2):
        B2K=sum(y[b]*h[:,b]*sum(y[c]*uk[b,c,a] for c in range(2))/2 for b in range(2))
        Fadj=sum(y[b]*(h[:,b]*sum(y[c]*uk[a,c,b] for c in range(2))+V[b]*uu[b,a]) for b in range(2))
        J3=y[a]*(W.T@K3[a]+B2U[a])
        T6.append(ell[:,a]**2*y[a]*(W.T@K5[a]+B2K+Fadj/4)/6
                  +ell[:,a]*lm[:,a]*q[a]*J3/6
                  +4*lm[:,a]*q[a]*P4[a]/3+ln[:,a]*q[a]**3/3)
    E6=[]
    for a in range(2):
        B2T=sum(y[b]*Uy[b]*ht[b,a]/2 for b in range(2))
        B4V=sum(y[b]*(K3[b]*hv[b,a]+Uy[b]*vv[b,a])/4 for b in range(2))
        B6h=sum(y[b]*(K5[b]*(v if b==a else 0)+K3[b]*hv[a,b]+Uy[b]*ht[a,b])/6 for b in range(2))
        E6.append(W@T6[a]+B2T+B4V+B6h)
    O=sum(y[b]*(d[:,b]*E6[b]+e[:,b]*R[b]*E[b]+f[:,b]*R[b]**3/6) for b in range(2))
    K7=[d[:,a]*O/7+N*e[:,a]*R[a]/5
        +J*(e[:,a]*E[a]+f[:,a]*R[a]**2/2)/3
        +S*(e[:,a]*E6[a]+f[:,a]*R[a]*E[a]+fourth[:,a]*R[a]**3/6) for a in range(2)]
    bs,bc=beta_constants()
    beta=np.array([y[0]*(bs*y[0]**2+bc*y[1]**2),y[1]*(bc*y[0]**2+bs*y[1]**2)])
    B=H@beta
    Z=[-sum((y[a]*beta[b]/20+beta[a]*y[b]/5)*F[:,a,b] for b in range(2)) for a in range(2)]
    Zp=[sum((y[a]*beta[b]/10+3*beta[a]*y[b]/8)*F[:,a,b] for b in range(2)) for a in range(2)]
    M=[d[:,a]*sum(y[b]*d[:,b]*Z[b]-beta[b]*d[:,b]*R[b] for b in range(2))/6
       -B*e[:,a]*R[a]/4+S*e[:,a]*Z[a] for a in range(2)]
    P=[d[:,a]*sum(y[b]*d[:,b]*(Zp[b]-Z[b])+11*beta[b]*d[:,b]*R[b]/4 for b in range(2))/7
       +3*B*e[:,a]*R[a]/5+S*e[:,a]*(Zp[a]-Z[a]/2) for a in range(2)]
    return dict(T6=np.array(T6),K7=np.array(K7),M=np.array(M),P=np.array(P),T=np.array(T),K5=np.array(K5))


def fourier_coefficients(w,W,constants):
    """Exact degree<8 Fourier extraction, up to floating-point arithmetic.

    Eight roots of unity avoid ill-conditioned real-label interpolation.
    This is only an independent algebra oracle, never dictionary fitting.
    """
    values=[direct_fields(w,W,np.array([1.,np.exp(2j*np.pi*k/8)]),constants) for k in range(8)]
    return {key:np.fft.fft(np.stack([value[key] for value in values]),axis=0).transpose(1,2,0)/8 for key in values[0]}


def dense_prediction(w,c,M,b1,b2,inputs):
    dense=b2@M@b1.T/len(w)
    return torch.tanh(dense@torch.tanh(w@inputs.T)).T@c/len(c)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--candidate',default='new_dictionary_p7')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    candidate=importlib.import_module(args.candidate)
    args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1)
    constants=population_contractions()
    checks=[]
    def check(name,actual,expected=0.,tolerance=3e-11,relative=True):
        actual=np.asarray(actual.detach().cpu() if isinstance(actual,torch.Tensor) else actual)
        expected=np.asarray(expected.detach().cpu() if isinstance(expected,torch.Tensor) else expected)
        absolute=float(np.max(np.abs(actual-expected)))
        scale=max(1.,float(np.max(np.abs(expected)))) if relative else 1.
        passed=math.isfinite(absolute) and absolute/scale<=tolerance
        checks.append(dict(name=name,maximum_absolute_error=absolute,scale=scale,scaled_error=absolute/scale,tolerance=tolerance,passed=passed))
        if not passed:
            print(json.dumps(checks[-1]),flush=True)
    same,other=beta_constants()
    check('independent one-dimensional beta reduction',constants['beta'],[[same,0,other,0],[0,other,0,same]],2e-13)
    labels=[(0.,0.),(1.,0.),(0.,1.),(1.,1.),(1.,-1.),(.7,-1.3),(-1.4,.2),(2.1,.35)]
    cases=[]
    for seed,n in ((19,61),(53,79)):
        gen=torch.Generator(device='cpu').manual_seed(seed)
        w=torch.randn(n,2,generator=gen,dtype=torch.float64)
        W=torch.randn(n,n,generator=gen,dtype=torch.float64)/np.sqrt(n)
        c=torch.randn(n,generator=gen,dtype=torch.float64)/n
        initial=TensorState(w,c,W)
        originals=[value.clone() for value in (w,c,W)]
        p5=previous.raw_features(initial,5)
        p6=candidate.raw_features(initial,6)
        p7=candidate.raw_features(initial,7)
        graph=candidate._graph(initial,p5[0],p5[1],through_p7=True)
        check(f'seed{seed} dimensions p6',[p6[0].shape[1],p6[1].shape[1]],[14,28],0)
        check(f'seed{seed} dimensions p7',[p7[0].shape[1],p7[1].shape[1]],[26,46],0)
        for layer in (0,1):
            check(f'seed{seed} p6 unchanged p5 layer{layer}',p6[layer][:,:p5[layer].shape[1]],p5[layer],0)
            check(f'seed{seed} p7 unchanged p6 layer{layer}',p7[layer][:,:p6[layer].shape[1]],p6[layer],0)
        coeff=fourier_coefficients(w.numpy(),W.numpy(),constants)
        for key in coeff:
            check(f'seed{seed} real Fourier coefficients {key}',coeff[key].imag,tolerance=3e-12)
        for i,(a,j) in enumerate(((0,1),(0,2),(1,3),(1,4))):
            check(f'seed{seed} selected M{a+1} coefficient{j}',p6[1][:,24+i]/math.factorial(6),coeff['M'][a,:,j].real)
        for i,(a,j) in enumerate(((0,1),(1,4))):
            check(f'seed{seed} selected tau P{a+1} coefficient{j}',p7[1][:,28+i]/math.factorial(7),constants['tau']*coeff['P'][a,:,j].real)
        for label in labels:
            y=np.array(label)
            fields=direct_fields(w.numpy(),W.numpy(),y,constants)
            for a in range(2):
                from_lower=p7[0][:,14+6*a:20+6*a].numpy()@monomials(y,6)[a:a+6]/math.factorial(6)
                from_upper=p7[1][:,30+8*a:38+8*a].numpy()@monomials(y,7)/math.factorial(7)
                check(f'seed{seed} label{label} T6{a+1}',from_lower,fields['T6'][a])
                check(f'seed{seed} label{label} K7{a+1}',from_upper,fields['K7'][a])
                check(f'seed{seed} label{label} inherited T{a+1}',p5[0][:,6+4*a:10+4*a].numpy()@monomials(y,4)[a:a+4]/24,fields['T'][a])
                check(f'seed{seed} label{label} inherited K5{a+1}',p5[1][:,12+6*a:18+6*a].numpy()@monomials(y,5)/120,fields['K5'][a])
                for key,degree in (('M',5),('P',5),('T6',6),('K7',7)):
                    check(f'seed{seed} label{label} full graph {key}{a+1}',graph[key][a].numpy()@monomials(y,degree),fields[key][a])
                    check(f'seed{seed} label{label} independent Fourier {key}{a+1}',coeff[key][a,:,:degree+1]@monomials(y,degree),fields[key][a])
        for p in (6,7):
            engine,state,metadata=candidate.build(initial,p,block_size=3)
            raw=p6 if p==6 else p7
            check(f'seed{seed} p{p} retained readin',state.w,w,0)
            check(f'seed{seed} p{p} retained nonzero readout',state.c,c,0)
            check(f'seed{seed} p{p} projected middle initialization',state.M,engine.b2.T@(W@engine.b1)/n)
            eta=1/(1024*(p+1)**2)
            for layer,basis in enumerate((engine.b1,engine.b2)):
                psi=raw[layer].numpy()
                factor=np.linalg.cholesky(psi.T@psi/n+eta*np.eye(psi.shape[1]))
                expected=np.linalg.solve(factor,psi.T).T
                check(f'seed{seed} p{p} independently normalized layer{layer}',basis,expected,3e-8)
            moved=engine.state(w+.1*torch.randn(w.shape,generator=gen,dtype=w.dtype),
                               c+.25*torch.randn(c.shape,generator=gen,dtype=c.dtype),
                               state.M+.1*torch.randn(state.M.shape,generator=gen,dtype=state.M.dtype))
            angle=torch.arange(11,dtype=torch.float64)*(2*math.pi/11)+.13
            inputs=torch.stack([angle.cos(),angle.sin()],1)
            targets=torch.linspace(-1.2,.8,11,dtype=torch.float64)
            data=engine.prepare_data(inputs,targets)
            rhs=engine.rhs(moved,data)
            aw,ac,am=[value.clone().requires_grad_(True) for value in (moved.w,moved.c,moved.M)]
            prediction=dense_prediction(aw,ac,am,engine.b1,engine.b2,inputs)
            gradients=torch.autograd.grad((prediction-targets).square().mean(),(aw,ac,am))
            check(f'seed{seed} p{p} dense compressed prediction',engine.predict(moved,inputs),prediction.detach())
            for name,value,gradient,mobility in zip(('w','c','M'),(rhs.w,rhs.c,rhs.M),gradients,(n,n,1)):
                check(f'seed{seed} p{p} full-batch gradient {name}',value,-mobility*gradient,3e-10)
            cases.append(dict(seed=seed,p=p,width=n,K1=metadata['K1'],K2=metadata['K2'],ridge=eta,
                lower_condition=metadata['lower']['ridge_condition'],upper_condition=metadata['upper']['ridge_condition']))
        for name,value,original in zip(('w','c','M'),(initial.w,initial.c,initial.M),originals):
            check(f'seed{seed} untouched initial {name}',value,original,0)
    paths=[Path(__file__),Path(candidate.__file__),HERE/'new_dictionary_p45.py',HERE/'new_dictionary.py',HERE/'p7_gaussian_check.py',HERE/'P7_DERIVATION.md']
    output=dict(status='PASS' if all(item['passed'] for item in checks) else 'FAIL',checks=checks,total_checks=len(checks),
                maximum_scaled_error=max(item['scaled_error'] for item in checks),cases=cases,
                dtype='float64',device='cpu',torch=str(torch.__version__),numpy=np.__version__,
                source_hashes={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
                scientific_scope='Prescribed population-derived frozen fields evaluated on finite Gaussian carriers; no finite-width population-jet identity or training test')
    (args.out/'validation.json').write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:output[key] for key in ('status','total_checks','maximum_scaled_error')}),flush=True)
    if output['status']!='PASS':
        raise SystemExit(1)


if __name__=='__main__':
    main()
