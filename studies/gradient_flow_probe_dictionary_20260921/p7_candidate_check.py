"""Independent candidate coefficient reconstruction against the frozen oracle.

All pairings here are explicitly empirical and therefore are not a
population-dictionary implementation. Polynomial labels are never fitted.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

import p7_jet_oracle as oracle


class P:
    """Small sparse polynomial wrapper; ndarray operations act coefficientwise."""
    __array_priority__ = 10000

    def __init__(self, value):
        self.p = value.p if isinstance(value,P) else value if isinstance(value,dict) else {(0,0):np.asarray(value,dtype=float)}

    def __add__(self, other):
        return P(oracle._p_add(self.p,P(other).p))

    __radd__ = __add__

    def __neg__(self):
        return P(oracle._p_scale(self.p,-1))

    def __sub__(self, other):
        return self+-P(other)

    def __rsub__(self, other):
        return P(other)+-self

    def __mul__(self, other):
        return P(oracle._p_product(self.p,P(other).p))

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return P(oracle._p_scale(self.p,1/scalar))

    def __matmul__(self, other):
        return P(oracle._p_product(self.p,P(other).p,np.matmul))

    def __pow__(self, power):
        if not isinstance(power,int) or power < 0:
            raise ValueError('only nonnegative integer polynomial powers')
        result = P(1)
        for _ in range(power):
            result = result*self
        return result

    @property
    def T(self):
        return P(oracle._p_map(self.p,np.transpose))


def outer(u,v,n):
    return P(oracle._p_product(P(u).p,P(v).p,lambda a,b:np.outer(a,b)/n))


def pairing(u,v,n):
    return P(oracle._p_product(P(u).p,P(v).p,lambda a,b:np.asarray(np.sum(a*b)/n)))


def stack_polys(values):
    keys = set().union(*(value.p for value in values))
    shape = next(iter(next(value for value in values if value.p).p.values())).shape
    return P({key:np.stack([value.p.get(key,np.zeros(shape)) for value in values],axis=-1)
              for key in keys})


def lower_generators(w0,a0):
    """P3/p5 identities with exact empirical contractions, before p7 formulas."""
    n = len(w0)
    h0 = np.tanh(w0)
    z0 = a0@h0
    H0 = np.tanh(z0)
    v,tau = float(np.mean(h0[:,0]**2)),float(np.mean(H0[:,0]**2))
    h,H = [P(h0[:,a]) for a in range(2)],[P(H0[:,a]) for a in range(2)]
    ell,d = [1-q*q for q in h],[1-q*q for q in H]
    m,e = [-2*q*g for q,g in zip(h,ell)],[-2*q*g for q,g in zip(H,d)]
    third = [(6*q*q-2)*g for q,g in zip(H,d)]
    y = [P({(1,0):np.array(1.)}),P({(0,1):np.array(1.)})]
    A0 = P(a0)
    S = sum(y[a]*H[a] for a in range(2))
    U1 = [S*d[a] for a in range(2)]
    D = sum(y[a]*outer(U1[a],h[a],n) for a in range(2))
    B2 = D/2
    q = [y[a]*ell[a]*(A0.T@U1[a])/2 for a in range(2)]
    V = [ell[a]*q[a] for a in range(2)]
    R = [A0@V[a]+B2@h[a] for a in range(2)]
    J = sum(y[a]*d[a]*R[a] for a in range(2))
    K3 = [d[a]*J/3+S*e[a]*R[a] for a in range(2)]
    F = sum(y[a]*(outer(K3[a],h[a],n)+outer(U1[a],V[a],n)) for a in range(2))
    beta = [pairing(J,H[a],n)/3+pairing(S,d[a]*R[a],n) for a in range(2)]
    B = sum(beta[a]*H[a] for a in range(2))
    T = [y[a]*ell[a]**2*(A0.T@K3[a])/4
         +y[a]*ell[a]**2*(B2.T@U1[a])/4+m[a]*q[a]**2 for a in range(2)]
    E = [A0@T[a]+B2@V[a]+F@h[a]/4 for a in range(2)]
    N = sum(y[a]*(d[a]*E[a]+e[a]*R[a]**2/2) for a in range(2))
    K5 = [d[a]*N/5+J*e[a]*R[a]/3+S*e[a]*E[a]+S*third[a]*R[a]**2/2
          for a in range(2)]
    G = sum(y[a]*(outer(K5[a],h[a],n)+outer(K3[a],V[a],n)+outer(U1[a],T[a],n))
            for a in range(2))
    return locals()


def fixture_generic():
    previous = oracle._load_file('p45_jet_check')
    w,a,v,tau = previous.ideal_initial(8201)
    return 'generic_exact_grams',w,a,v,tau


def fixture_symmetric():
    signs = np.array([[1.,1.],[1.,-1.],[-1.,1.],[-1.,-1.]])
    h = np.concatenate([r*signs for r in (.2,.35,.5,.65)])
    a = np.diag(np.repeat([.8,1.,1.2,1.4],4))
    H = np.tanh(a@h)
    return 'sign_swap_exact_grams',np.arctanh(h),a,float(np.mean(h[:,0]**2)),float(np.mean(H[:,0]**2))


def candidate_coefficients(w0,a0):
    """Literal Eq. (2)--(14) from frozen P7_DERIVATION, empirical pairings."""
    base = lower_generators(w0,a0)
    n,A0,h,H,ell,m,d,e,third,y,S,U1,B2,q,V,R,J,K3,F,beta,B,T,E,N,K5,G,v,tau = (
        base[name] for name in ('n','A0','h','H','ell','m','d','e','third','y','S',
                               'U1','B2','q','V','R','J','K3','F','beta','B','T','E',
                               'N','K5','G','v','tau'))
    L = [[ell[a]**2*(A0.T@(d[a]*H[b])) for b in range(2)] for a in range(2)]
    Ffield = [[v*d[a]*H[b]+A0@L[a][b] for b in range(2)] for a in range(2)]
    P4 = [ell[a]*(y[a]*(A0.T@K3[a])+B2.T@(y[a]*U1[a]))/4
          +m[a]*q[a]*(A0.T@(y[a]*U1[a]))/4 for a in range(2)]
    X = [d[a]*(y[a]*B/20+beta[a]*S/5) for a in range(2)]
    A = [-ell[a]**2*(A0.T@X[a]) for a in range(2)]
    Z = [A0@A[a]-v*X[a] for a in range(2)]
    Aplus = [sum((y[a]*beta[b]/10+3*beta[a]*y[b]/8)*L[a][b]
                 for b in range(2)) for a in range(2)]
    Zplus = [sum((y[a]*beta[b]/10+3*beta[a]*y[b]/8)*Ffield[a][b]
                 for b in range(2)) for a in range(2)]
    feedback = sum(y[a]*d[a]*Z[a]-beta[a]*d[a]*R[a] for a in range(2))
    M = [d[a]*feedback/6-B*e[a]*R[a]/4+S*e[a]*Z[a] for a in range(2)]
    feedback_next = sum(y[a]*d[a]*(Zplus[a]-Z[a])+11*beta[a]*d[a]*R[a]/4
                        for a in range(2))
    P5 = [d[a]*feedback_next/7+3*B*e[a]*R[a]/5+S*e[a]*(Zplus[a]-Z[a]/2)
          for a in range(2)]
    J3 = [y[a]*(A0.T@K3[a])+B2.T@(y[a]*U1[a]) for a in range(2)]
    lower_third = [(6*h[a]**2-2)*ell[a] for a in range(2)]
    fourth = [8*H[a]*(2-3*H[a]**2)*d[a] for a in range(2)]
    T6 = [ell[a]**2*(y[a]*(A0.T@K5[a])+B2.T@(y[a]*K3[a])
                     +F.T@(y[a]*U1[a])/4)/6
          +ell[a]*m[a]*q[a]*J3[a]/6+4*m[a]*q[a]*P4[a]/3
          +lower_third[a]*q[a]**3/3 for a in range(2)]
    E6 = [A0@T6[a]+B2@T[a]+F@V[a]/4+G@h[a]/6 for a in range(2)]
    O = sum(y[a]*(d[a]*E6[a]+e[a]*R[a]*E[a]+third[a]*R[a]**3/6)
            for a in range(2))
    K7 = [d[a]*O/7+N*e[a]*R[a]/5
          +J*(e[a]*E[a]+third[a]*R[a]**2/2)/3
          +S*(e[a]*E6[a]+third[a]*R[a]*E[a]+fourth[a]*R[a]**3/6)
          for a in range(2)]
    Q = [d[a]*E[a]+e[a]*R[a]**2/2 for a in range(2)]
    gamma = [pairing(N,H[a],n)/5+pairing(J,d[a]*R[a],n)/3+pairing(S,Q[a],n)
             for a in range(2)]
    C = sum(gamma[a]*H[a] for a in range(2))
    delta = [pairing(feedback,H[a],n)/6-pairing(B,d[a]*R[a],n)/4
             +pairing(S,d[a]*Z[a],n) for a in range(2)]
    Ddelta = sum(delta[a]*H[a] for a in range(2))
    kappa,rho,sigma = 7*tau**2/12,31*tau**4/360,13*tau**2/6
    hcoeff = [[h[a],P({}),V[a],-tau*V[a],kappa*V[a]+T[a],
               -tau**3*V[a]/4-2*tau*T[a]+A[a],
               rho*V[a]+sigma*T[a]+tau*Aplus[a]+T6[a]] for a in range(2)]
    zcoeff = [[base['z0'][:,a],P({}),R[a],-tau*R[a],kappa*R[a]+E[a],
               -tau**3*R[a]/4-2*tau*E[a]+Z[a],
               rho*R[a]+sigma*E[a]+tau*Zplus[a]+E6[a]] for a in range(2)]
    zcoeff = [[P(value) for value in series] for series in zcoeff]
    bcoeff = [[y[a],-tau*y[a],tau**2*y[a]/2,-tau**3*y[a]/6-beta[a],
               tau**4*y[a]/24+7*tau*beta[a]/4,
               -tau**5*y[a]/120-8*tau**2*beta[a]/5-gamma[a],
               tau**6*y[a]/720+61*tau**3*beta[a]/60+8*tau*gamma[a]/3-delta[a]]
              for a in range(2)]
    ucoeff = [[P({}),U1[a],-tau*U1[a]/2,tau**2*U1[a]/6+K3[a],
               -tau**3*U1[a]/24-3*tau*K3[a]/2-B*d[a]/4,
               tau**4*U1[a]/120+5*tau**2*K3[a]/4+7*tau*B*d[a]/20+K5[a],
               -tau**5*U1[a]/720-3*tau**3*K3[a]/4-5*tau*K5[a]/2
                   -4*tau**2*B*d[a]/15-C*d[a]/6+M[a],
               tau**6*U1[a]/5040+43*tau**4*K3[a]/120+10*tau**2*K5[a]/3
                   +61*tau**3*B*d[a]/420+8*tau*C*d[a]/21-Ddelta*d[a]/7
                   +tau*P5[a]+K7[a]] for a in range(2)]
    middle = [A0,P({})]+[sum(bcoeff[a][i]*outer(ucoeff[a][j],hcoeff[a][k],n)
                             for a in range(2) for i in range(power-1)
                             for j in range(1,power-i) for k in [power-1-i-j])/power
                           for power in range(2,9)]
    coefficients = dict(a=middle,
                        h=[stack_polys([hcoeff[a][k] for a in range(2)]) if k != 1 else P({})
                           for k in range(7)],
                        z=[stack_polys([zcoeff[a][k] for a in range(2)]) if k != 1 else P({})
                           for k in range(7)],
                        b=[stack_polys([bcoeff[a][k] for a in range(2)]) for k in range(7)],
                        cgate=[stack_polys([ucoeff[a][k] for a in range(2)]) if k != 0 else P({})
                               for k in range(8)])
    return coefficients,locals()


def _coefficient_error(candidate,reference,shape):
    keys = sorted(set(candidate)|set(reference))
    by_degree = {}
    for i,j in keys:
        left,right = candidate.get((i,j),np.zeros(shape)),reference.get((i,j),np.zeros(shape))
        value = oracle._error(left,right)
        key = str(i+j)
        by_degree[key] = max(by_degree.get(key,0),value)
    return by_degree


def check_fixture(fixture):
    name,w0,a0,v,tau = fixture
    n = len(w0)
    h,H = np.tanh(w0),np.tanh(a0@np.tanh(w0))
    gram_errors = dict(lower=oracle._error(h.T@h/n,v*np.eye(2)),
                       upper=oracle._error(H.T@H/n,tau*np.eye(2)))
    expected = oracle.full_polynomial_jet(w0,a0)
    candidate,fields = candidate_coefficients(w0,a0)
    errors = {name:{str(k):_coefficient_error(value.p,expected[name][k],oracle._field_shape(expected,name))
                   for k,value in enumerate(series)} for name,series in candidate.items()}
    evaluation_errors = {}
    for labels in ((.7,-1.1),(-.6,.9)):
        numeric = oracle.full_jet(w0,a0,labels)
        evaluation_errors[str(labels)] = {
            f'{name}_{k}':oracle._error(sum((labels[0]**i*labels[1]**j*value
                                            for (i,j),value in p.p.items()),
                                           np.zeros(numeric[name][k].shape)),numeric[name][k])
            for name,series in candidate.items() for k,p in enumerate(series)}
    maximum = max([*gram_errors.values()]+[error for series in errors.values()
                                          for degrees in series.values() for error in degrees.values()]
                  +[error for group in evaluation_errors.values() for error in group.values()])
    # Report every discrepancy before enforcing the fixed threshold.
    beta = [{f'{i},{j}':float(value) for (i,j),value in p.p.items()} for p in fields['beta']]
    norms = {f'{name}_{k}':{str(degree):float(np.linalg.norm(oracle.label_degree(expected,name,k,degree)))
                            for degree in sorted({i+j for i,j in expected[name][k]})}
             for name,k in (('a',7),('a',8),('h',6),('cgate',7))}
    return dict(fixture=name,width=n,v=v,tau=tau,gram_errors=gram_errors,
                beta_coefficients=beta,errors=errors,nonzero_degree_norms=norms,
                numeric_evaluation_errors=evaluation_errors,
                maximum_normalized_absolute_error=maximum,
                status='PASS' if maximum < 3e-12 else 'FAIL')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    result_path = args.output_dir/'results.json'
    if result_path.exists():
        raise FileExistsError('candidate check results are frozen')
    cases = [check_fixture(fixture_generic()),check_fixture(fixture_symmetric())]
    source = Path(__file__)
    payload = dict(status='PASS' if all(case['status']=='PASS' for case in cases) else 'FAIL',
                   purpose='Full finite algebra check with empirical pairings, not population substitutions',
                   source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                   oracle_sha256=hashlib.sha256(source.with_name('p7_jet_oracle.py').read_bytes()).hexdigest(),
                   candidate_sha256=hashlib.sha256(source.with_name('P7_DERIVATION.md').read_bytes()).hexdigest(),
                   tolerance=3e-12,cases=cases)
    with result_path.open('x') as stream:
        json.dump(payload,stream,indent=2,allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(status=payload['status'],results=str(result_path),
                          maximum_normalized_absolute_error=max(case['maximum_normalized_absolute_error'] for case in cases))))
    if payload['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
