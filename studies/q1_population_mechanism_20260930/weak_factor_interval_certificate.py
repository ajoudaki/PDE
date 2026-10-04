"""Outward interval Simpson certificate for Gaussian sech moments.

Standard-library only. Decimal exp/sqrt are correctly rounded to nearest;
one adjacent representable number on each side encloses their exact values.
All arithmetic operations otherwise round outward. The mathematical error
bounds and resulting coefficient formulas are recorded in the study proof.
"""
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import platform
import time

PREC=42
LO=Context(prec=PREC,rounding=ROUND_FLOOR)
HI=Context(prec=PREC,rounding=ROUND_CEILING)
NEAR=Context(prec=PREC,rounding=ROUND_HALF_EVEN)


class I:
    def __init__(self,lo,hi=None):
        self.lo=Decimal(lo);self.hi=Decimal(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def fraction(x):
        return I(LO.divide(Decimal(x.numerator),Decimal(x.denominator)),
                 HI.divide(Decimal(x.numerator),Decimal(x.denominator)))
    def __add__(self,b):
        b=as_i(b);return I(LO.add(self.lo,b.lo),HI.add(self.hi,b.hi))
    __radd__=__add__
    def __neg__(self):return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self,b):return self+-as_i(b)
    def __rsub__(self,b):return as_i(b)+-self
    def __mul__(self,b):
        b=as_i(b);return I(min(LO.multiply(a,c) for a in (self.lo,self.hi) for c in (b.lo,b.hi)),
                           max(HI.multiply(a,c) for a in (self.lo,self.hi) for c in (b.lo,b.hi)))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=as_i(b);assert b.lo>0 or b.hi<0
        return self*I(LO.divide(Decimal(1),b.hi),HI.divide(Decimal(1),b.lo))
    def __pow__(self,n):
        assert n>=0;out=I(1)
        for _ in range(n):out=out*self
        return out
    def exp(self):
        return I(NEAR.next_minus(NEAR.exp(self.lo)),NEAR.next_plus(NEAR.exp(self.hi)))
    def sqrt(self):
        assert self.lo>=0
        return I(NEAR.next_minus(NEAR.sqrt(self.lo)),NEAR.next_plus(NEAR.sqrt(self.hi)))
    def pair(self):return [str(self.lo),str(self.hi)]


def as_i(x):return x if isinstance(x,I) else I(x)


def atan_bounds(inv,n=60):
    x=Fraction(1,inv)
    val=sum(((-1)**k*x**(2*k+1)/ (2*k+1) for k in range(n)),Fraction(0))
    nxt=(-1)**n*x**(2*n+1)/(2*n+1)
    return min(val,val+nxt),max(val,val+nxt)


def pi_interval():
    a,b=atan_bounds(5);c,d=atan_bounds(239)
    return I(I.fraction(16*a-4*d).lo,I.fraction(16*b-4*c).hi)


def derivative_bound(n):
    # P(t)=(1-t²)^n; D P=(1-t²)P'(t), t=tanh(x).
    p=[0]*(2*n+1)
    for k in range(n+1):p[2*k]=(-1)**k*comb(n,k)
    norms=[]
    for _ in range(5):
        norms.append(sum(abs(v) for v in p))
        d=[(k+1)*p[k+1] for k in range(len(p)-1)]
        p=[0]*(len(d)+2)
        for k,v in enumerate(d):p[k]+=v;p[k+2]-=v
    # Each derivative of the standard Gaussian density up to order4 is <10.
    return 10*sum(comb(4,k)*norms[k] for k in range(5))


def moments(variance,step_den=2000,radius=10):
    assert variance.lo>0 and variance.hi<=1
    h=I.fraction(Fraction(1,step_den));N=radius*step_den
    assert N%2==0
    sigma=variance.sqrt();normalizer=(2*pi_interval()).sqrt()
    total=[I(0) for _ in range(7)]
    for j in range(N+1):
        x=I.fraction(Fraction(j,step_den))
        density=(-(x*x)/2).exp()/normalizer
        e=(-2*sigma*x).exp()
        p=4*e/((1+e)**2)
        weight=1 if j in (0,N) else (4 if j%2 else 2)
        power=I(1)
        for k in range(7):
            power=power*p
            total[k]=total[k]+weight*density*power
    tail=2*I(-radius*radius).exp().sqrt()/normalizer/radius
    values=[];errors=[]
    for n,summation in enumerate(total,1):
        simpson=2*h*summation/3
        # Twice the error on [0,R]; sigma<=1, so no derivative inflation.
        error=I.fraction(Fraction(2*radius*derivative_bound(n),180*step_den**4))
        enclosure=I(LO.subtract(simpson.lo,error.hi),HI.add(HI.add(simpson.hi,error.hi),tail.hi))
        assert enclosure.lo>0 and enclosure.hi<1
        values.append(enclosure);errors.append(error)
    return values,errors,tail


def first_coefficients(ins,outs):
    A=[I(0)]+ins;B=[I(0)]+outs
    a1=A[2];a2=4*(A[2]-A[3]);B1=B[2];B2=4*(B[2]-B[3])
    C=(8*B[2]-10*B[3])*a2+(32*B[2]-112*B[3]+84*B[4])*a1*a1
    P=13*A[4]-31*A[5]+18*A[6]
    R=2*A[3]-5*A[4]+3*A[5]
    T=14*A[4]-52*A[5]+65*A[6]-27*A[7]
    latent=(16*B1*P+4*B2*a1*(17*A[4]-16*A[5])-8*C*(A[3]-A[4]))/2
    context=(-16*B1*R-16*B2*a1*(A[3]-A[4])+4*C*(A[2]-A[3]))/2
    target=(192*B1*T+32*B2*a1*P-16*C*R)/2
    weight=2*(B1*a2+B2*a1*a1)
    return {k:v.pair() for k,v in dict(latent=latent,context=context,target=target,latent_readin_weight=weight,
                                      outer_response_context=C,target_signal=B1*a2+B2*a1*a1).items()}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    start=time.time()
    inner,err,tail=moments(I(1))
    variance=1-inner[0]
    outer,err2,tail2=moments(variance)
    result=dict(precision=PREC,step='1/2000',radius=10,python=platform.python_version(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                pi=pi_interval().pair(),variance=variance.pair(),
                inner=[v.pair() for v in inner],outer=[v.pair() for v in outer],
                absolute_simpson_errors=[v.pair() for v in err],tail=tail.pair(),
                first_coefficients=first_coefficients(inner,outer),elapsed_seconds=time.time()-start)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
