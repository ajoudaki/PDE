"""Deterministic static checks of C-H1 (7)-(8); no training trajectory.

All finite population pairings are means and rank actions are outer/n.
The graph has shared nodes, both action orientations, a bounded product,
nonlinear gates, moving readout, and a frozen initial-observation analogue.
"""
import json
from pathlib import Path
import sys
import numpy as np

n = 5
w = np.array([[.2,-.3],[-.4,.7],[.9,.1],[-.8,-.6],[.5,-.2]])
A = np.array([[.1,.4,-.3,.2,-.1],[.5,-.2,.1,.3,.2],[-.4,.2,.7,-.1,.3],
              [.2,-.1,.3,.6,-.5],[-.3,.5,-.2,.4,.1]])
c = np.array([.5,-.4,.3,.1,-.2])
g = np.array([.2,-.1,.6,-.3,.4])
us = np.array([[1.,0.],[.6,.8],[-.8,.6]])
ys = np.array([1.,-.7,.2])
weights = np.array([.25,.5,.25])
mean = np.mean

def fields(w,A,c,u):
    h1=np.tanh(w@u);z2=A@h1;h2=np.tanh(z2)
    d2=c*(1-h2*h2);q=A.T@d2
    return h1,h2,d2,q

fw=np.zeros_like(w);fA=np.zeros_like(A);fc=np.zeros_like(c)
physical=[]
for weight,u,y in zip(weights,us,ys):
    h1,h2,d2,q=fields(w,A,c,u);r=mean(c*h2)-y
    fw += -2*weight*r*np.outer((1-h1*h1)*q,u)
    fA += -2*weight*r*np.outer(d2,h1)/n
    fc += -2*weight*r*h2
    physical.append((weight,u,r,h1,h2,d2,q))

# layer, operation, parent indices, optional scalar parameters
spec=[(1,'w',(),0),(1,'w',(),1),(2,'c',()),(1,'fixed',()),
      (1,'aff',(0,1),(.7,-.2,.1)),(1,'tanh',(4,)),
      (2,'A',(5,)),(2,'sin',(6,)),(2,'mul',(2,7)),
      (1,'AT',(8,)),(1,'aff',(9,3),(1.,.3,0.)),
      (1,'cos',(10,)),(2,'A',(11,)),(2,'tanh',(12,)),(2,'mul',(13,7)),
      (2,'aff',(14,8),(.6,-.4,.2)),(2,'cos',(15,))]

def evaluate(w,A,c):
    vals=[]
    for layer,op,parents,*args in spec:
        if op=='w': v=w[:,args[0]]
        elif op=='c':v=c
        elif op=='fixed':v=g
        elif op=='aff':
            a,b,d=args[0];v=a*vals[parents[0]]+b*vals[parents[1]]+d
        elif op=='tanh':v=np.tanh(vals[parents[0]])
        elif op=='sin':v=np.sin(vals[parents[0]])
        elif op=='cos':v=np.cos(vals[parents[0]])
        elif op=='mul':v=vals[parents[0]]*vals[parents[1]]
        elif op=='A':v=A@vals[parents[0]]
        elif op=='AT':v=A.T@vals[parents[0]]
        vals.append(v)
    return vals

vals=evaluate(w,A,c)
def reverse(R=None):
    p=[np.zeros(n) for _ in vals];p[-1]=np.ones(n);occ=[]
    clip=(lambda x:x) if R is None else lambda x:R*np.tanh(x/R)
    for k in reversed(range(len(spec))):
        _,op,par,*args=spec[k];v=vals[k]
        if op=='aff':
            a,b,_=args[0];p[par[0]]+=a*p[k];p[par[1]]+=b*p[k]
        elif op in ('tanh','sin','cos'):
            u=vals[par[0]]
            gate=(1-v*v) if op=='tanh' else np.cos(u) if op=='sin' else -np.sin(u)
            p[par[0]]+=gate*clip(p[k])
        elif op=='mul':
            p[par[0]]+=vals[par[1]]*clip(p[k]);p[par[1]]+=vals[par[0]]*clip(p[k])
        elif op=='A':
            occ.append(('+',p[k].copy(),vals[par[0]]));p[par[0]]+=A.T@clip(p[k])
        elif op=='AT':
            occ.append(('-',p[k].copy(),vals[par[0]]));p[par[0]]+=A@clip(p[k])
    return p,occ

p,occ=reverse()
raw=mean(p[0]*fw[:,0])+mean(p[1]*fw[:,1])+mean(p[2]*fc)
raw+=sum(mean(pv*((fA if orient=='+' else fA.T)@b)) for orient,pv,b in occ)

def rhs(R=None):
    p,occ=reverse(R);out=0.
    for weight,u,r,h1,h2,d2,q in physical:
        term=mean((u[0]*p[0]+u[1]*p[1])*(1-h1*h1)*q)+mean(p[2]*h2)
        for orient,pv,b in occ:
            term+=mean(pv*d2)*mean(b*h1) if orient=='+' else mean(pv*h1)*mean(b*d2)
        out+=-2*weight*r*term
    return out

# Forward tangent pass is independent of the reverse recursion.
dv=[]
for k,(_,op,par,*args) in enumerate(spec):
    if op=='w':v=fw[:,args[0]]
    elif op=='c':v=fc
    elif op=='fixed':v=np.zeros(n)
    elif op=='aff':
        a,b,_=args[0];v=a*dv[par[0]]+b*dv[par[1]]
    elif op=='mul':v=dv[par[0]]*vals[par[1]]+vals[par[0]]*dv[par[1]]
    elif op=='A':v=fA@vals[par[0]]+A@dv[par[0]]
    elif op=='AT':v=fA.T@vals[par[0]]+A.T@dv[par[0]]
    else:
        z=vals[par[0]];gate=(1-vals[k]**2) if op=='tanh' else np.cos(z) if op=='sin' else -np.sin(z)
        v=gate*dv[par[0]]
    dv.append(v)
forward=mean(dv[-1]);eps=1e-5
fd=(mean(evaluate(w+eps*fw,A+eps*fA,c+eps*fc)[-1])-
    mean(evaluate(w-eps*fw,A-eps*fA,c-eps*fc)[-1]))/(2*eps)
exact=rhs()
assert abs(exact-raw)<1e-13 and abs(exact-forward)<1e-13
assert abs(exact-fd)<1e-8
cutoffs=[1.,4.,16.,64.,256.,1024.]
errors=[abs(rhs(R)-exact) for R in cutoffs]
assert errors[-1]<1e-6
result={'kind':'static deterministic identity check, no training',
        'weak_rhs':float(exact),'raw_pairing':float(raw),'forward_tangent':float(forward),
        'central_difference':float(fd),'cutoffs':cutoffs,'cutoff_errors':errors,
        'numpy':np.__version__,'python':sys.version,'status':'PASS'}
output=Path(sys.argv[1]);output.mkdir(parents=True,exist_ok=True)
(output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
