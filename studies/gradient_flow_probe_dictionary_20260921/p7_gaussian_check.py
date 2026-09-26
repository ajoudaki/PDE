"""Deterministic population contractions for the p7 formal increment graph.

No trajectory, finite Gaussian carrier, or task labels enter this module.
Binary polynomial slot j is y1**(degree-j)*y2**j.  Gaussian innovations
are integrated analytically before the two-dimensional Hermite rule.
"""
from pathlib import Path
from functools import lru_cache
import argparse
import hashlib
import json
import math
import numpy as np


def mul(a, b):
    out = np.zeros((a.shape[0], a.shape[1]+b.shape[1]-1))
    for i in range(a.shape[1]):
        for j in range(b.shape[1]):
            out[:, i+j] += a[:, i]*b[:, j]
    return out


def ytimes(a, axis):
    out = np.zeros((a.shape[0], a.shape[1]+1))
    out[:, axis:axis+a.shape[1]] = a
    return out


def gaussian_rule(order):
    z, w = np.polynomial.hermite.hermgauss(order)
    return np.sqrt(2)*z, w/np.sqrt(np.pi)


@lru_cache(maxsize=3)
def population_contractions(order=256):
    """All scalars needed by the label-leading W(t) coefficient through t8.

    UK[a,b,c,j] = <U_ab,[y1^(3-j)y2^j] K3_c>.
    hT[i,a,j] = <h_i,[y1^(4-j)y2^j] T_a>.
    VV[a,b,j] = [y1^(4-j)y2^j] <V_a,V_b>.
    beta[a,j] = [y1^(3-j)y2^j] beta_a.
    """
    fixed_z, fixed_w = np.polynomial.hermite.hermgauss(256)
    # Preserve the previous builder's arithmetic order and exact stored v.
    v = float(fixed_w @ np.tanh(np.sqrt(2)*fixed_z)**2/np.sqrt(np.pi))
    z, w = gaussian_rule(order)
    grid = np.array(np.meshgrid(z, z, indexing='ij')).reshape(2,-1).T
    weights = np.outer(w,w).ravel()
    n = len(weights)
    def avg(x):
        return np.einsum('n,n...->...',weights,x)
    h = np.tanh(grid)
    ell = 1-h*h
    lower_second = -2*h*ell
    Y = np.sqrt(v)*grid
    H = np.tanh(Y)
    d = 1-H*H
    e = -2*H*d
    U = (d[:,:,None]*H[:,None,:]).reshape(n,4)
    pairs = [(a,b) for a in range(2) for b in range(2)]
    DU = np.zeros((n,4,2))
    for i,(a,b) in enumerate(pairs):
        DU[:,i,b] += d[:,a]*d[:,b]
        DU[:,i,a] += e[:,a]*H[:,b]
    A = avg(DU)
    C = avg(U[:,:,None]*U[:,None,:])
    mu = h @ A.T
    gates = np.stack([ell[:,a]**2 for a,b in pairs],1)
    # Q_i = zeta_i + mu_i; covariance(zeta)=C, independent of g.
    Lmean = gates*mu
    LL = avg(gates[:,:,None]*gates[:,None,:]*(C[None]+mu[:,:,None]*mu[:,None,:]))
    P = avg(Lmean[:,:,None]*h[:,None,:])
    kappa = float(w @ (1-np.tanh(z)**2)**2)
    # W L_i = xi_i + kappa U_i, with E[xi_i | Y]=P_i Y/v.
    ximean = Y @ P.T/v
    Fmean = ximean + (v+kappa)*U
    S = H
    R = [ytimes(Fmean[:,2*a:2*a+2],a)/2 for a in range(2)]
    J = sum(ytimes(d[:,b:b+1]*R[b],b) for b in range(2))
    K = [d[:,a:a+1]*J/3+e[:,a:a+1]*mul(S,R[a]) for a in range(2)]
    # Formal derivative in named xi coordinates: Y and all coefficients frozen.
    KR = np.zeros((2,4,n,4))
    for i,(c,b) in enumerate(pairs):
        Ri = [np.zeros((n,3)),np.zeros((n,3))]
        Ri[c][:,c+b] = .5
        Ji = sum(ytimes(d[:,a:a+1]*Ri[a],a) for a in range(2))
        for a in range(2):
            KR[a,i] = d[:,a:a+1]*Ji/3+e[:,a:a+1]*mul(S,Ri[a])
    # An independent adjoint evaluation uses the reverse response rule,
    # differentiating in the named Y,xi coordinates before conditioning.
    KY = np.zeros((2,2,n,4))
    upper_third=(6*H*H-2)*d
    for j in range(2):
        Rj=[ytimes((v+kappa)*DU[:,2*a:2*a+2,j],a)/2 for a in range(2)]
        Jj=sum(ytimes(d[:,b:b+1]*Rj[b]+(e[:,b:b+1]*R[b] if j==b else 0),b) for b in range(2))
        Sj=np.zeros_like(S)
        Sj[:,j]=d[:,j]
        for a in range(2):
            KY[a,j]=(d[:,a:a+1]*Jj+(e[:,a:a+1]*J if a==j else 0))/3
            KY[a,j]+=e[:,a:a+1]*(mul(Sj,R[a])+mul(S,Rj[a]))
            if a==j:
                KY[a,j]+=upper_third[:,a:a+1]*mul(S,R[a])
    UK = np.empty((2,2,2,4))
    for i,(a,b) in enumerate(pairs):
        for c in range(2):
            UK[a,b,c] = avg(U[:,i:i+1]*K[c])
    beta = np.array([avg(H[:,a:a+1]*J/3+mul(S,d[:,a:a+1]*R[a])) for a in range(2)])
    VV = np.zeros((2,2,5))
    hT = np.zeros((2,2,5))
    hV = np.zeros((2,2,3))
    adjoint_response_error=0.
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for k in range(2):
                    ia,ib=2*a+c,2*b+k
                    VV[a,b,a+b+c+k] += avg(gates[:,ia]*gates[:,ib]*(C[ia,ib]+mu[:,ia]*mu[:,ib]))/4
        for i in range(2):
            for b in range(2):
                hV[i,a,a+b] += avg(h[:,i]*Lmean[:,2*a+b])/2
            # f=h_i ell_a², W f is a forward Gaussian with no response.
            f = h[:,i]*ell[:,a]**2
            fY = avg(f[:,None]*h)
            fxi = avg(f[:,None]*Lmean)
            conditional_cov = fxi-fY@P.T/v
            fmean = Y@fY/v
            fK = avg(fmean[:,None]*K[a])
            for j in range(4):
                fK += conditional_cov[j]*avg(KR[a,j])
            reverse_fK=np.zeros(4)
            for j in range(2):
                reverse_fK+=fY[j]*avg(KY[a,j])
            for j in range(4):
                reverse_fK+=fxi[j]*avg(KR[a,j])
            adjoint_response_error=max(adjoint_response_error,float(np.max(np.abs(reverse_fK-fK))))
            hT[i,a,a:a+4] += fK/4
            # y_a/4 <h_i ell_a², B2* (S d_a)>.
            for b in range(2):
                lower = avg(f*h[:,b])/8
                for c in range(2):
                    for k in range(2):
                        hT[i,a,a+b+c+k] += lower*C[2*b+c,2*a+k]
            # <h_i m_a q_a²>, with conditional second moment of zeta exact.
            for b in range(2):
                for c in range(2):
                    i1,i2=2*a+b,2*a+c
                    value=avg(h[:,i]*lower_second[:,a]*ell[:,a]**2*(C[i1,i2]+mu[:,i1]*mu[:,i2]))/4
                    hT[i,a,2*a+b+c] += value
    joint = np.block([[v*np.eye(2),P.T],[P,LL]])
    return dict(order=order,v=v,tau=float(w@np.tanh(np.sqrt(v)*z)**2),kappa=kappa,
                A=A,C=C,P=P,LL=LL,UK=UK,hT=hT,VV=VV,hV=hV,beta=beta,
                adjoint_response_error=adjoint_response_error,
                source_covariance_minimum_eigenvalue=float(np.linalg.eigvalsh(joint).min()))


def independent_lower_pairing_check(order=32):
    """Direct product quadrature in two roots plus four zeta coordinates.

    A degree-three Hermite rule in zeta exactly integrates every conditional
    quadratic expression. This checks the analytic Wick reduction separately.
    """
    constants=population_contractions(order)
    z,w=gaussian_rule(order)
    root=np.array(np.meshgrid(z,z,indexing='ij')).reshape(2,-1).T
    wr=np.outer(w,w).ravel()
    q,wq=gaussian_rule(3)
    normals=np.array(np.meshgrid(q,q,q,q,indexing='ij')).reshape(4,-1).T
    wz=np.einsum('a,b,c,d->abcd',wq,wq,wq,wq).ravel()
    eigenvalues,eigenvectors=np.linalg.eigh(constants['C'])
    zeta=normals@(eigenvectors*np.sqrt(np.maximum(eigenvalues,0))).T
    h=np.tanh(root);ell=1-h*h
    mu=h@constants['A'].T
    direct=np.zeros((2,2,5))
    for iz,noise in enumerate(zeta):
        Q=mu+noise
        V=[ytimes(ell[:,a:a+1]**2*Q[:,2*a:2*a+2],a)/2 for a in range(2)]
        for a in range(2):
            for b in range(2):
                direct[a,b]+=wz[iz]*(wr@mul(V[a],V[b]))
    return float(np.max(np.abs(direct-constants['VV'])))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    preliminary=population_contractions(128)
    coarse=population_contractions(192)
    fine=population_contractions(256)
    keys=('v','tau','kappa','A','C','P','LL','UK','hT','VV','hV','beta')
    errors={key:float(np.max(np.abs(np.asarray(coarse[key])-np.asarray(fine[key])))) for key in keys}
    preliminary_errors={key:float(np.max(np.abs(np.asarray(preliminary[key])-np.asarray(fine[key])))) for key in keys}
    wick_error=independent_lower_pairing_check()
    # Parity: beta1 has only y1³,y1*y2², with swapped beta2 coefficients.
    parity_error=max(abs(fine['beta'][0,1]),abs(fine['beta'][0,3]),abs(fine['beta'][1,0]),abs(fine['beta'][1,2]),
                     float(np.max(np.abs(fine['beta'][0]-fine['beta'][1,::-1]))))
    passed=max(errors.values())<1e-9 and wick_error<2e-13 and parity_error<2e-13 and fine['adjoint_response_error']<2e-13 and fine['source_covariance_minimum_eigenvalue']>-2e-13
    output=dict(status='PASS' if passed else 'FAIL',purpose='Initialized population moment algebra only; no training and no empirical Gaussian carrier contractions',
                resolution_comparison=errors,maximum_resolution_discrepancy=max(errors.values()),discrepancy_is_error_bound=False,
                resolution_orders=[192,256],preliminary_128_256_discrepancies=preliminary_errors,
                preliminary_gate_status='FAIL' if max(preliminary_errors.values())>=1e-9 else 'PASS',
                independent_wick_error=wick_error,parity_error=parity_error,
                beta_radial_difference=float(fine['beta'][0,0]-fine['beta'][0,2]),
                working={key:np.asarray(value).tolist() for key,value in fine.items()},
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),numpy=np.__version__,
                convention='ordinary homogeneous binary polynomial coefficients; no derivative factorial rescaling')
    args.out.mkdir(parents=True,exist_ok=False)
    (args.out/'contractions.json').write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:output[key] for key in ('status','maximum_resolution_discrepancy','independent_wick_error','parity_error','beta_radial_difference')}))
    if not passed:
        raise SystemExit(1)


if __name__=='__main__':
    main()
