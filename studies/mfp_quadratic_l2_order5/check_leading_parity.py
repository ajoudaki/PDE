#!/usr/bin/env python3
"""Parity-sector audit for the leading homogeneous finite-width network."""

from collections import defaultdict


def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for e,c in p.items(): out[e] += c
    return {e:c for e,c in out.items() if c}


def mul(*ps):
    out = {(0,)*len(next(iter(ps[0]))): 1}
    for p in ps:
        nxt=defaultdict(int)
        for a,c in out.items():
            for b,k in p.items():
                nxt[tuple(x+y for x,y in zip(a,b))]+=c*k
        out=dict(nxt)
    return out


def power(p,k):
    dim=len(next(iter(p)))
    out={(0,)*dim:1}
    for _ in range(k): out=mul(out,p)
    return out


def var(dim,k):
    e=[0]*dim;e[k]=1
    return {tuple(e):1}


def deriv(p,k):
    out={}
    for e,c in p.items():
        if e[k]:
            q=list(e);q[k]-=1
            out[tuple(q)]=c*e[k]
    return out


def compose(p, values):
    dim=len(next(iter(values[0])))
    ans={}
    for e,c in p.items():
        term={(0,)*dim:c}
        for k,r in enumerate(e):
            if r: term=mul(term,power(values[k],r))
        ans=add(ans,term)
    return ans


def leading_objective(n,d):
    dim=n+n*n+n
    av=[var(dim,i) for i in range(n)]
    w=[[var(dim,n+i*n+j) for j in range(n)] for i in range(n)]
    u=[var(dim,n+n*n+j) for j in range(n)]
    P={}
    for i in range(n):
        s={}
        for j in range(n):s=add(s,mul(w[i][j],power(u[j],d)))
        P=add(P,mul(av[i],power(s,d)))
    return P


def main():
    for n,d in ((2,2),(2,3)):
        p=leading_objective(n,d)
        g=[deriv(p,k) for k in range(n+n*n+n)]
        pg=compose(p,g)
        bad=[e for e in pg if any(x%2 for x in e)]
        print("n",n,"d",d,"P terms",len(p),"P(grad P) terms",len(pg),
              "non-even monomials",len(bad),"sample",bad[:3])


if __name__=="__main__":main()
