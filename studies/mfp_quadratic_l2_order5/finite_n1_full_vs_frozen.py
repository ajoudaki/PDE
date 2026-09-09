#!/usr/bin/env python3
"""Exact n=1 full/frozen paired defect for a numeric polynomial activation."""

from collections import defaultdict
from fractions import Fraction as Q


def add(*ps):
    out=defaultdict(Q)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return {m:c for m,c in out.items() if c}


def scale(p,c):return {m:Q(c)*x for m,x in p.items() if c*x}


def mul(*ps):
    out={(0,0,0,0):Q(1)}
    for p in ps:
        nxt=defaultdict(Q)
        for a,c in out.items():
            for b,d in p.items():nxt[tuple(x+y for x,y in zip(a,b))]+=c*d
        out={m:c for m,c in nxt.items() if c}
    return out


def power(p,k):
    out={(0,0,0,0):Q(1)}
    for _ in range(k):out=mul(out,p)
    return out


H={(1,0,0,0):Q(1)};A={(0,1,0,0):Q(1)}
W={(0,0,1,0):Q(1)};U={(0,0,0,1):Q(1)}


def activate(x,c):
    return add(*(scale(power(x,k),v) for k,v in enumerate(c) if v))


def derivative(x,c):
    return add(*(scale(power(x,k-1),k*v) for k,v in enumerate(c) if k and v))


def step(state,c,frozen=False,step_scale=1):
    a,w,u=state
    feature=activate(u,c);z=mul(w,feature)
    top=activate(z,c);resp=mul(a,derivative(z,c))
    hs=scale(H,step_scale)
    na=add(a,mul(hs,top))
    nw=add(w,mul(hs,resp,feature))
    nu=u if frozen else add(u,mul(hs,w,resp,derivative(u,c)))
    return na,nw,nu


def output(state,c):
    a,w,u=state
    return mul(a,activate(mul(w,activate(u,c)),c))


def horizon(n,c,frozen=False,step_scale=1):
    state=(A,W,U)
    for _ in range(n):state=step(state,c,frozen,step_scale)
    return output(state,c)


def gmoment(k):
    if k%2:return 0
    ans=1
    for j in range(1,k,2):ans*=j
    return ans


def expect(p):
    out=defaultdict(Q)
    for (h,a,w,u),c in p.items():
        v=c*gmoment(a)*gmoment(w)*gmoment(u)
        if v:out[h]+=v
    return dict(out)


def paired(c,frozen=False):
    return expect(add(horizon(2,c,frozen,1),scale(horizon(1,c,frozen,2),-1)))


if __name__=="__main__":
    for c in ((Q(-3),Q(0),Q(1)),(Q(-11,9),Q(0),Q(10,27)),
              (Q(-1,4),Q(-1,4),Q(-1,4),Q(1,4))):
        f=paired(c);r=paired(c,True)
        diff={k:f.get(k,0)-r.get(k,0) for k in set(f)|set(r)}
        print("activation",c)
        print("negative full-frozen coefficients",[(k,v) for k,v in sorted(diff.items()) if v<0][:20])
        # Exact values at a few rational h.
        for h in (Q(1,100),Q(1,10),Q(1,2),Q(1)):
            val=sum(v*h**k for k,v in diff.items())
            print("h",h,"difference sign",(val>0)-(val<0))
