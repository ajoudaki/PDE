#!/usr/bin/env python3
"""Independent finite-horizon audit of the frozen quadratic obstruction.

This does not import either order-five compiler.  It expands the scalar
frozen recursion exactly in Q[h,A0,Z0] for psi(x)=x+x^2 and integrates
the two independent Gaussian marks by double factorials.
"""

from fractions import Fraction as Q


Poly = dict[tuple[int,int,int],Q]  # powers of (h,A0,Z0)


def add(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=out.get(m,Q(0))+c
    return {m:c for m,c in out.items() if c}


def scale(c,p):
    return {m:Q(c)*x for m,x in p.items() if Q(c)*x}


def mul(p,q):
    out={}
    for (i,j,k),c in p.items():
        for (r,s,t),d in q.items():
            m=(i+r,j+s,k+t)
            out[m]=out.get(m,Q(0))+c*d
    return {m:c for m,c in out.items() if c}


H={(1,0,0):Q(1)}
ONE={(0,0,0):Q(1)}


def psi(x): return add(x,mul(x,x))
def dpsi(x): return add(ONE,scale(2,x))


def gm(k):
    if k%2: return 0
    out=1
    for odd in range(1,k,2): out*=odd
    return out


def expected_output(N):
    A={(0,1,0):Q(1)}
    Z={(0,0,1):Q(1)}
    for _ in range(N):
        oldA,oldZ=A,Z
        A=add(oldA,mul(H,psi(oldZ)))
        Z=add(oldZ,mul(H,mul(oldA,dpsi(oldZ))))
    raw=mul(A,psi(Z))
    out={}
    for (h,a,z),c in raw.items():
        value=c*gm(a)*gm(z)
        if value: out[h]=out.get(h,Q(0))+value
    return {k:v for k,v in out.items() if v}


def paired(t,outputs):
    fine=outputs[2*t]
    coarse=outputs[t]
    degrees=set(fine)|set(coarse)
    return {k:fine.get(k,Q(0))-Q(2)**k*coarse.get(k,Q(0))
            for k in degrees
            if fine.get(k,Q(0))-Q(2)**k*coarse.get(k,Q(0))}


if __name__ == "__main__":
    outputs=[expected_output(N) for N in range(5)]
    for N,value in enumerate(outputs[1:],1):
        expected_degree=3*(2**N-1)
        assert max(value)==expected_degree,(N,max(value),expected_degree)
        assert value[expected_degree]>0
    for t in (1,2):
        defect=paired(t,outputs)
        assert defect and all(c>=0 for c in defect.values()),(t,defect)
        assert max(defect)==3*(2**(2*t)-1)
    print("PASS: frozen exact degrees, positive leading moments, and paired coefficient positivity through t=2")
