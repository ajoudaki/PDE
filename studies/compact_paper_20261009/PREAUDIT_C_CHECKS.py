import math
import numpy as np
from decimal import Decimal, getcontext
getcontext().prec = 60
class MP:
    mpf=Decimal
    e=Decimal(1).exp()
    sqrt=staticmethod(lambda x: Decimal(x).sqrt())
    log=staticmethod(lambda x: Decimal(x).ln())
mp=MP()
failures = []
tested = 0
def check(name, actual, bound, context):
    global tested
    tested += 1
    if actual > bound * (1 + mp.mpf('1e-45')):
        failures.append((name, context, str(actual / bound)))

for beta_int in (10, 11, 20, 100):
    beta = mp.mpf(beta_int)
    b, s, t2 = beta - 1, beta, beta
    for L in range(2, 21):
        ctx = (beta_int, L)
        H, P = [mp.mpf(0)] * (L+1), [mp.mpf(0)] * (L+1)
        H[1], P[1] = b + 20*s, mp.mpf(3)
        for j in range(2,L+1):
            H[j] = b + 10*s*H[j-1]
            P[j] = H[j-1] + 10*s*P[j-1] + 1
        k = [0] + [H[L]*(10*s)**(L-j) for j in range(1,L+1)]
        tau, f = [s*v for v in k], [s*v for v in P]
        A = 2*s*P[L] + 2*s*s*sum(k[j]*P[j-1] for j in range(2,L+1))
        D = t2*sum(v*v for v in P)
        HH = A + t2*sum(P[j]**2*k[j] for j in range(1,L+1))
        EE = t2*sum((10*s)**(2*(j-1))*k[j] for j in range(1,L+1))
        TT = 2*HH**2+4*A**2*(mp.e**2-1)
        D0 = (1+b+s)*(1+TT+EE+s*s*max(k)**2)
        D1 = 576*mp.e**3*(1+b+s)*D**3
        CF = s*(8*max(f)**2+max(H)**2+1)
        Cabs = 8*(D0+1)
        V0 = [0, tau[1]]
        for j in range(2,L+1):
            V0.append(tau[j]*H[j-1]**2 + 10*s*V0[j-1])
        G0 = [mp.mpf(0)]*(L+1)
        G0[L]=s*H[L]+14*t2*V0[L]+s
        for j in range(L-1,0,-1):
            G0[j]=10*s*G0[j+1]+s**3*k[j+1]**2*H[j]+14*t2*V0[j]+s
        WG=128*(1+max(H)+s*max(V0)+max(G0))
        eta=1/(1024*Cabs*WG)
        B=1024*mp.e**2*L
        Lambda=mp.log(mp.e+B)+mp.log(1/eta)
        allowance=min(1,1/(4*A),mp.sqrt(eta/(4000*D)),
            mp.sqrt(eta/(16*mp.e*D*mp.sqrt(2*B))),mp.sqrt(eta/Lambda),
            (eta**3/(D1*B))**mp.mpf('.25'),1/mp.sqrt(8*D0*CF))
        for j in range(1,L+1):
            check('H',H[j],3*beta**(2*j),ctx+(j,))
            check('P',P[j],beta**(3*j-2),ctx+(j,))
            check('k',k[j],3*beta**(4*L-2*j),ctx+(j,))
            check('V0',V0[j],27*j*beta**(4*L+2*j-3),ctx+(j,))
            check('G0',G0[j],66*L*beta**(8*L-2*j-1),ctx+(j,))
        for name,val,exponent in [('A',A,5*L-2),('D',D,6*L-2),
            ('HH',HH,8*L-2),('EE',EE,6*L-2),('TT',TT,16*L-3),
            ('D0',D0,16*L-2),('D1',D1,18*L-2),('CF',CF,6*L),
            ('Cabs',Cabs,16*L-1),('WG',WG,9*L+1),('eta_inv',1/eta,25*L+4),
            ('B',B,L+3),('Lambda',Lambda,2*L)]:
            check(name,val,beta**exponent,ctx)
        check('allowance',beta**(-26*L),allowance,ctx)

print('POWER_CHECKS', tested, 'FAILURES', failures)

rng=np.random.default_rng(20261009)
metric_err=0
for n,r in [(11,3),(30,5),(7,7)]:
    E=np.column_stack([np.ones(n),rng.normal(size=(n,r-1))])
    U=np.linalg.qr(E)[0]*np.sqrt(n)
    # Use all coordinates with deliberately nonuniform positive weights.
    D=np.diag(rng.uniform(1,4,n)/n)
    P=U
    G=P.T@D@P
    Z=np.sqrt(D)@P
    Gi=np.linalg.inv(G)
    M=np.sqrt(D)@(Z@Gi@Gi@Z.T+np.eye(n)-Z@Gi@Z.T)@np.sqrt(D)
    metric_err=max(metric_err,np.max(abs(P.T@M@P-np.eye(r))))
    assert np.linalg.eigvalsh(M-D/4).min()>-1e-12
    assert np.linalg.eigvalsh(D-M).min()>-1e-12
    assert abs(np.ones(n)@M@np.ones(n)-1)<1e-12
print('VARIABLE_DIMENSION_METRIC_MAX_ERROR',metric_err)

# Non-diagonal metrics and unequal widths test the exact selected energy.
m,d,q1,q2=3,2,5,7
def spd(q):
    A=rng.normal(size=(q,q)); return A@A.T+np.eye(q)
M1,M2=spd(q1),spd(q2)
v=rng.normal(size=(d,m));v/=np.linalg.norm(v,axis=0)
W=rng.normal(size=(q1,d))*.1
B=rng.normal(size=(q2,q1))*.1
w=rng.normal(size=q2)*.1
y=rng.normal(size=m)*.1;c=rng.normal(size=m)*.1
h1=np.tanh(W@v);h2=np.tanh(B@h1)
V=h2/np.sqrt(m);Q=V.T@M2@V
T=V@np.linalg.inv(Q)
wc=w+T@((y-c)/np.sqrt(m)-V.T@M2@w)
d2=(1-h2*h2)*wc[:,None]
d1=(1-h1*h1)*(np.linalg.solve(M1,B.T@M2)@d2)
K=h2.T@M2@h2+(d1.T@M1@d1)*(v.T@v)+(d2.T@M2@d2)*(h1.T@M1@h1)
Wdot=2/m*(d1*c)@v.T
Bdot=2/m*(d2*c)@h1.T@M1
wdot=2/m*h2@c
en=np.trace(Wdot.T@M1@Wdot)+np.trace(Bdot.T@M2@Bdot@np.linalg.inv(M1))+wdot@M2@wdot
rhs=4/m**2*c@K@c
print('READOUT_TRAIN_ERROR',np.max(abs(wc@M2@h2-(y-c))))
print('SELECTED_ENERGY_REL_ERROR',abs(en-rhs)/max(abs(rhs),1e-30))
assert abs(en-rhs)/max(abs(rhs),1e-30)<1e-10

# Exact quadratic-history Legendre identities via polynomial arithmetic.
from numpy.polynomial import Polynomial,Legendre
def projection(g,A,q):
    p=Polynomial([0.])
    for j in range(q):
        lj=Legendre.basis(j).convert(kind=Polynomial)(Polynomial([-1,2/A]))
        gg=(g*lj).integ()
        p=p+(2*j+1)/A*(gg(A)-gg(0))*lj
    return p
legerr=0
for q in range(1,6):
    A=1.3
    g=Polynomial(rng.normal(size=8))
    h=Polynomial(rng.normal(size=7))
    eps=1e-6
    def pairing(a):
        z=(projection(g,a,q)*projection(h,a,q)).integ()
        return z(a)-z(0)
    num=(pairing(A+eps)-pairing(A-eps))/(2*eps)
    want=g(A)*h(A)-(g(A)-projection(g,A,q)(A))*(h(A)-projection(h,A,q)(A))
    legerr=max(legerr,abs(num-want)/max(1,abs(want)))
print('LEGENDRE_BILINEAR_DERIVATIVE_MAX_REL_ERROR',legerr)
assert legerr<1e-5

# Check the innovation inequality in the exactly tractable linear-activation case.
innovation_margin=float('inf')
for m in range(2,13):
    for trial in range(20):
        A=rng.normal(size=(m,m))
        Q=A@A.T+np.eye(m)
        diag=np.sqrt(np.diag(Q))
        Q=Q/diag[:,None]/diag[None,:]
        y=rng.normal(size=m)
        gamma=np.linalg.eigvalsh(Q).min()
        rowvars=np.diag(Q)*(y@Q@y)+(Q@y)**2
        lower=gamma**3*np.dot(y,y)/(48*m)
        innovation_margin=min(innovation_margin,rowvars.max()/lower)
        assert rowvars.max()>=lower
print('LINEAR_INNOVATION_MIN_MARGIN',innovation_margin)

Phi=lambda x:(1+math.erf(x/math.sqrt(2)))/2
for u in (0.001,.1,1,3):
    for shift in np.linspace(-10,10,201):
        assert Phi(u-shift)-Phi(-u-shift)<=2*Phi(u)-1+1e-14
print('GAUSSIAN_SHIFT_SMALL_BALL_CHECKS',4*201)
for d in range(2,101):
    loglhs=d*math.log(d+3)-2*math.lgamma(d+1)
    logrhs=d*math.log(8*math.e**2)-(d+1)*math.log(d)
    assert loglhs<=logrhs
print('HARMONIC_FACTORIAL_COUNT_CHECKS',99)
print('NUMPY',np.__version__,'DECIMAL_PRECISION',getcontext().prec)
