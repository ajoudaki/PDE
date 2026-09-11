"""Independent supplied-state algebra; no optimizer trajectory or parameter sweep."""
import json, hashlib, platform
from pathlib import Path
import numpy as np
from decimal import Decimal as Dec, localcontext
import decimal

# One fixed finite state; the reference first atom is split into duplicate slots.
n=4
w=np.array([[.2,-.4],[1.1,.3],[-.8,.6],[4.,-3.]])
A=np.array([[.2,-.1,.4,.1],[.3,.7,-.2,.4],[-.5,.1,.6,-.2],[.1,-.3,.2,.5]])
c=np.array([.25,-.4,.15,.31])
e=np.array([.7,-.2,.4,.1]); h=.037
u=np.array([1.,0.]); y=1.
h1=np.tanh(w@u); z=A@h1; H=np.tanh(z)
gate=lambda q:1/np.cosh(q)**2
curv=lambda q:-2*np.tanh(q)*gate(q)
delta=c*gate(z); Q=A.T@delta; r=c@H/n-y

def forced_increment(eps,p):
    zz=z+eps*e; HH=np.tanh(zz); dd=c*gate(zz)
    rr=c@HH/n-y; QQ=A.T@dd
    X=np.zeros((n,2),dtype=np.result_type(eps,float)); X[:,0]=-2*h*p*rr*QQ
    return X, -2*h*p*np.outer(dd,h1)*rr/n, -2*h*p*rr*HH

def directional(p):
    dH=gate(z)*e; dr=c@dH/n; ddelta=c*curv(z)*e; dQ=A.T@ddelta
    X=np.zeros((n,2)); X[:,0]=-2*h*p*(dr*Q+r*dQ)
    return X,-2*h*p*np.outer(dr*delta+r*ddelta,h1)/n,-2*h*p*(dr*H+r*dH)

flat=lambda v:np.concatenate([a.ravel() for a in v])
complex_step=1e-25
actual=tuple(q.imag/complex_step for q in forced_increment(1j*complex_step,.2))
exact=directional(.2)
forcing_error=float(np.max(np.abs(flat(actual)-flat(exact))))
assert forcing_error<1e-13
split_error=float(np.max(np.abs(flat(directional(.2))+flat(directional(.3))-flat(directional(.5)))))
assert split_error<1e-15
# Deliberately suppressing residual feedback must change this nondegenerate test.
no_feedback=(np.column_stack((-2*h*.2*r*(A.T@(c*curv(z)*e)),np.zeros(n))),
             -2*h*.2*r*np.outer(c*curv(z)*e,h1)/n,
             -2*h*.2*r*gate(z)*e)
residual_feedback_signal=float(np.linalg.norm(flat(exact)-flat(no_feedback)))
assert residual_feedback_signal>1e-6

# Three specifically chosen clock boundary cases, at high precision.
decimal.getcontext().prec=70
sinh=lambda x:(x.exp()-(-x).exp())/2
cosh=lambda x:(x.exp()+(-x).exp())/2
F=lambda x:x/2+sinh(2*x)/4
D=lambda x:1/cosh(x)**2
Fp=lambda x:cosh(x)**2
Dp=lambda x:-2*sinh(x)/cosh(x)*D(x)
clock=[]
for ww,bb,hh in [('0','1.7','.03'),('1.5','-0.9','.04'),('6','-1.3','.03')]:
    W,B,Hh=map(Dec,(ww,bb,hh)); th=Hh*B*D(W)
    defect=F(W+th)-F(W)-Hh*B
    # Independent cancellation through the hyperbolic addition identity.
    alternate=(sinh(2*W)*(cosh(2*th)-1)+cosh(2*W)*(sinh(2*th)-2*th))/4
    dw=Fp(W+th)*(1+Hh*B*Dp(W))-Fp(W)
    db=Hh*(D(W)*Fp(W+th)-1)
    dstep=Dec('1e-20')
    funw=lambda x:F(x+Hh*B*D(x))-F(x)-Hh*B
    funb=lambda b:F(W+Hh*b*D(W))-F(W)-Hh*b
    dwn=(funw(W+dstep)-funw(W-dstep))/(2*dstep)
    dbn=(funb(B+dstep)-funb(B-dstep))/(2*dstep)
    err=max(abs(defect-alternate),abs(dw-dwn),abs(db-dbn))
    assert err<Dec('1e-32')
    clock.append(dict(w=ww,b=bb,h=hh,identity_error=str(err),defect=str(defect)))
result=dict(status='PASS',scope='one supplied finite state and three declared scalar boundary cases; no training',
            forward_forcing_complex_step_error=forcing_error,duplicate_mass_splitting_error=split_error,
            omitted_residual_feedback_negative_control=residual_feedback_signal,clock=clock,
            python=platform.python_version(),numpy=np.__version__,decimal_precision=decimal.getcontext().prec,
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
