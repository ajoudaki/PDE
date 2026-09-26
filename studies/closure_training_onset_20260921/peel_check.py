"""Deterministic checks of the p=1 Gaussian-moment reduction; no training."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import pathlib
import platform
import time
import numpy as np
import scipy
from scipy.special import roots_legendre


def gaussian_rule(n: int):
    x, w = roots_legendre(n)
    x = 10 * x
    w = 10 * w * np.exp(-x*x/2) / math.sqrt(2*math.pi)
    return x, w / w.sum()


def direct_setup(n: int):
    x, w = gaussian_rule(n)
    h = np.tanh(x)
    v = float(w @ (h*h))
    upper = np.tanh(math.sqrt(v)*x)
    tau = float(w @ (upper*upper))
    alpha = 1-tau
    kk = np.tanh(alpha*h[:, None] + math.sqrt(tau)*x[None, :])
    j = kk @ w
    beta = float(w @ (h*j))
    s = float(w @ ((kk*kk) @ w))
    gamma = 1-s
    eta = 1/4096
    delta = (v+eta)*(s+eta)-beta*beta
    ca = (alpha*(v*(s+eta)-beta*beta)-beta*tau*gamma)/((tau+eta)*delta)
    cb = (alpha*beta*eta+tau*gamma*(v+eta))/((tau+eta)*delta)
    def lam(rho):
        yy = np.tanh(rho*x[:, None]+math.sqrt(max(0, 1-rho*rho))*x[None, :])
        conditional = yy @ w
        aa = float(w @ (h*conditional))
        bb = float(w @ (j*conditional))
        return ca*aa+cb*bb
    return x,w,h,upper,j,lam,dict(v=v,tau=tau,alpha=alpha,beta=beta,s=s,gamma=gamma,eta=eta,q_A=ca,q_B=cb)


def normalization(v,tau,beta,s):
    alpha=1-tau
    gamma=1-s
    eta=1/4096
    delta=(v+eta)*(s+eta)-beta*beta
    ca=(alpha*(v*(s+eta)-beta*beta)-beta*tau*gamma)/((tau+eta)*delta)
    cb=(alpha*beta*eta+tau*gamma*(v+eta))/((tau+eta)*delta)
    kappa=ca*ca*v+2*ca*cb*beta+cb*cb*s
    return ca,cb,math.sqrt(2*v*kappa)


def derivative_coefficients(x,tau,max_degree):
    # Cauchy's coefficient formula evaluates sigma^(j)/j! stably at
    # Gaussian preactivations. No nonlinear random shift is evaluated.
    radius=1.15
    fft_nodes=512
    phase=2*math.pi*np.arange(fft_nodes)/fft_nodes
    values=np.tanh(math.sqrt(tau)*x[None,:]+radius*np.exp(1j*phase[:,None]))
    coeff=np.fft.fft(values,axis=0)/fft_nodes
    result=coeff[:max_degree+1].real / radius**np.arange(max_degree+1)[:,None]
    return result


def upper_atomic_kernel(coefficients,upper,w,radius,degree):
    # A Chebyshev interpolant is an explicit polynomial in the preactivation.
    # Its bivariate coefficients are evaluated without neuron populations.
    count=degree+1
    phase=math.pi*(np.arange(count)+0.5)/count
    nodes=np.cos(phase)
    transform=(2/count)*np.cos(np.arange(count)[:,None]*phase[None,:])
    transform[0]*=0.5
    univariate=transform@np.tanh(radius*nodes)
    polynomials=[]
    for a,b in coefficients:
        values=np.polynomial.chebyshev.chebval((a*nodes[:,None]+b*nodes[None,:])/radius,univariate)
        polynomials.append(transform@values@transform.T)
    polynomials=np.array(polynomials)
    # T_j(H) is a finite polynomial in H=sigma(sqrt(v)G), hence these
    # are finite linear combinations of the permitted activation-power atoms.
    # Evaluate polynomial recurrences rather than ill-conditioned monomials.
    moments=np.empty(2*degree+1)
    t0=np.ones_like(upper)
    moments[0]=w@t0
    if degree:
        t1=upper.copy()
        moments[1]=w@t1
        for j in range(2,2*degree+1):
            t0,t1=t1,2*upper*t1-t0
            moments[j]=w@t1
    indices=np.arange(count)
    gram=(moments[indices[:,None]+indices[None,:]]+moments[np.abs(indices[:,None]-indices[None,:])])/2
    contracted=np.array([gram@p@gram for p in polynomials])
    kernel=np.einsum('iab,jab->ij',contracted,polynomials)
    rho=(1+math.sqrt(1+radius*radius))/radius
    interpolation_bound=4*math.tan(1)*rho**(-degree)/(rho-1)
    kernel_bound=2*interpolation_bound+interpolation_bound**2
    return kernel,kernel_bound


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--nodes',type=int,nargs='+',default=[128,192])
    parser.add_argument('--atomic',action='store_true')
    args=parser.parse_args()
    out=pathlib.Path(args.output)
    out.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    rows=[]
    for n in args.nodes:
        x,w,h,upper,j,lam,constants=direct_setup(n)
        angles=np.array([0.,math.pi/12,math.pi/6,math.pi/4,math.pi/3,math.pi/2,2*math.pi/3,math.pi,7*math.pi/6])
        coefficients=np.array([[lam(math.cos(t)),lam(math.sin(t))] for t in angles])
        fields=np.array([np.tanh(a*upper[:,None]+b*upper[None,:]) for a,b in coefficients])
        weights=(w[:,None]*w[None,:]).reshape(-1)
        flat=fields.reshape(len(angles),-1)
        kernel=(flat*weights)@flat.T
        row=dict(nodes=n,constants=constants,angles=angles.tolist(),coefficients=coefficients.tolist(),max_panel_preactivation_bound=float(np.max(np.abs(coefficients).sum(axis=1))),kernel=kernel.tolist())
        if args.atomic:
            derivative=derivative_coefficients(x,constants['tau'],64)
            atomic=[]
            mixed=[]
            for angle in angles:
                pair=[]
                for rho in (math.cos(angle),math.sin(angle)):
                    yy=np.tanh(rho*x[:,None]+math.sqrt(max(0,1-rho*rho))*x[None,:])
                    pair.append(yy@w)
                mixed.append(pair)
            for lower_degree in (8,16,32,48,64):
                powers=(constants['alpha']*h[:,None])**np.arange(lower_degree+1)[None,:]
                truncated_k=powers@derivative[:lower_degree+1]
                beta=float(w@(h*(truncated_k@w)))
                s=float(w@((truncated_k*truncated_k)@w))
                ca,cb,radius=normalization(constants['v'],constants['tau'],beta,s)
                jj=truncated_k@w
                lower_coeff=np.array([[float(w@((ca*h+cb*jj)*conditional)) for conditional in pair] for pair in mixed])
                f_lower=np.array([np.tanh(a*upper[:,None]+b*upper[None,:]) for a,b in lower_coeff]).reshape(len(angles),-1)
                k_lower=(f_lower*weights)@f_lower.T
                for degree in (8,16,32,48,64):
                    k_atomic,bound=upper_atomic_kernel(lower_coeff,upper,w,radius,degree)
                    atomic.append(dict(lower_degree=lower_degree,upper_degree=degree,beta_error=abs(beta-constants['beta']),s_error=abs(s-constants['s']),lambda_max_error=float(np.max(np.abs(lower_coeff-coefficients))),uniform_radius=radius,upper_kernel_bound_exact_arithmetic=bound,upper_polynomial_error=float(np.max(np.abs(k_atomic-k_lower))),total_kernel_error=float(np.max(np.abs(k_atomic-kernel))),kernel=k_atomic.tolist() if (lower_degree,degree)==(64,64) else None))
            row['atomic']=atomic
        rows.append(row)
    result=dict(source_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),numpy=np.__version__,scipy=scipy.__version__,python=platform.python_version(),dtype='float64',cutoff=10,scalar_tail_mass=math.erfc(10/math.sqrt(2)),command_nodes=args.nodes,elapsed_seconds=time.monotonic()-start,rows=rows)
    if len(rows)>1:
        result['max_kernel_refinement_change']=float(np.max(np.abs(np.array(rows[-1]['kernel'])-np.array(rows[-2]['kernel']))))
    (out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'peel_check.py').write_bytes(pathlib.Path(__file__).read_bytes())
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
    for row in rows:
        print(json.dumps({k:v for k,v in row.items() if k not in ('kernel','angles','atomic')},indent=2))
        if args.atomic:
            print(json.dumps([{k:v for k,v in check.items() if k!='kernel'} for check in row['atomic'] if check['lower_degree']==check['upper_degree']],indent=2))


if __name__=='__main__':
    main()
