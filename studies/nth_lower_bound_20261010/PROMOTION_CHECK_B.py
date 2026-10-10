from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import factorial, log, exp

def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for a, c in p.items(): out[a] += c
    return {a:c for a,c in out.items() if c}

def mul(p,q):
    out = defaultdict(F)
    for a,c in p.items():
        for b,d in q.items(): out[tuple(x+y for x,y in zip(a,b))] += c*d
    return {a:c for a,c in out.items() if c}

def deriv(p,i):
    out = {}
    for a,c in p.items():
        if a[i]:
            b=list(a);b[i]-=1;out[tuple(b)]=c*a[i]
    return out

def var(i,d):
    a=[0]*d;a[i]=1
    return {tuple(a):F(1)}

def ev(p,x):
    return sum(c*prod(xi**ai for xi,ai in zip(x,a)) for a,c in p.items())

def prod(xs):
    out=F(1)
    for x in xs:out*=x
    return out

def direction(p,V):
    return add(*(mul(deriv(p,i),v) for i,v in enumerate(V)))

def smul(a,b,N):
    return [sum(a[i]*b[k-i] for i in range(k+1)) for k in range(N+1)]

def sadd(a,b):return [x+y for x,y in zip(a,b)]

N=9
B,W,c=[var(i,3) for i in range(3)]
f=mul(mul(B,W),c)
V=[mul(W,c),mul(B,c),mul(B,W)]
Kinit={}
K=f
for r in range(1,12):
    Kinit[r]=ev(K,[1,1,0]);K=direction(K,V)
print('Scalar initialized ranks:',Kinit)

state=[[F(1)]+[F(0)]*N,[F(1)]+[F(0)]*N,[F(0)]*(N+1)]
for k in range(N):
    B,W,c=state
    output=smul(smul(B,W,N),c,N)
    drive=[-z for z in output];drive[0]+=1
    rhs=[smul(smul(W,c,N),drive,N),smul(smul(B,c,N),drive,N),smul(smul(B,W,N),drive,N)]
    for i in range(3):state[i][k+1]=rhs[i][k]/(k+1)
dense=smul(smul(state[0],state[1],N),state[2],N)
predictions={}
for q in range(2,8):
    arrays=[[Kinit[r]]+[F(0)]*N for r in range(1,q+1)]
    for k in range(N):
        drive=[-z for z in arrays[0]];drive[0]+=1
        rhs=[smul(drive,arrays[r+1],N) for r in range(q-1)]
        for r in range(q-1):arrays[r][k+1]=rhs[r][k]/(k+1)
    predictions[q]=arrays[0]
    j=2*(q//2)+1
    diff=[x-y for x,y in zip(dense,arrays[0])]
    assert all(z==0 for z in diff[:j])
    assert diff[j]==Kinit[j+1]/factorial(j)
    print('Scalar q =',q,'first error coefficient at j =',j,':',diff[j])
for q in [3,5,7]:assert predictions[q]==predictions[q-1]
print('Odd/even neighboring predictions agree exactly through degree',N)

# A nonconstant source path tests chronological ordering independently of feedback.
# theta=(B1,B2,W,c), initial=(1,2,1,0), source a(t)=e1+t e2.
N=7
B1,B2,W,c=[var(i,4) for i in range(4)]
V1=[mul(W,c),{},mul(c,B1),mul(W,B1)]
V2=[{},mul(W,c),mul(c,B2),mul(W,B2)]
K0=mul(mul(B1,W),c)
series=[F(0)]*(N+1)
reverse=[F(0)]*(N+1)
asymmetric=None
for k in range(1,N+1):
    for slots in product([0,1],repeat=k):
        power=k+sum(slots)
        if power>N:continue
        K=K0
        for bit in slots:K=direction(K,[V1,V2][bit])
        val=ev(K,[1,2,1,0])
        denom=prod(k-j+sum(slots[j:]) for j in range(k))
        series[power]+=val/denom
        reverse_denom=prod(k-j+sum(slots[::-1][j:]) for j in range(k))
        reverse[power]+=val/reverse_denom
        if k==3 and slots==(0,0,1):
            K_rev=K0
            for bit in slots[::-1]:K_rev=direction(K_rev,[V1,V2][bit])
            asymmetric=(val,ev(K_rev,[1,2,1,0]))
state=[[F(x)]+[F(0)]*N for x in [1,2,1,0]]
for k in range(N):
    B1,B2,W,c=state
    xi=sadd(B1,[F(0)]+B2[:-1])
    wc=smul(W,c,N)
    rhs=[wc,[F(0)]+wc[:-1],smul(c,xi,N),smul(W,xi,N)]
    for i in range(4):state[i][k+1]=rhs[i][k]/(k+1)
actual=smul(smul(state[0],state[2],N),state[3],N)
assert series==actual
assert reverse!=actual
print('Ordered source expansion matches exact ODE through degree',N)
print('Tensor K4(e1,e1,e1,e2), K4(e1,e2,e1,e1):',asymmetric)
print('Actual coefficients:',actual)
print('Reversed-order coefficients:',reverse)

x=1/4096
L=96*x/(1-x)**4
print('Numeric constants: c_star =',4-1.5*log(9))
print('Complex ball map bound =',64*((1-1/512)**-3-1))
print('Complex ball Lipschitz bound =',96*(1/512)/(1-1/512)**4)
print('Real ball map/b bound =',64*((1-x)**-3-1))
print('Real ball Lipschitz bound =',L)
print('Tail multiplier =',(1+x)/((1-x)**3*(1-L)))
print('Picard mapping/contraction constants =',3150/4096,3135/4096)
print('Dense growth factor =',exp(1875/4096)-1)
print('All assertions passed.')
