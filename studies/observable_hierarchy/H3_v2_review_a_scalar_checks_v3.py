import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[key] = '1'
import sys, resource, json, time, pathlib, math
resource.setrlimit(resource.RLIMIT_CPU, (180,180))
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3,4*1024**3))
start=time.process_time()
root=pathlib.Path('/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2')
out=pathlib.Path(__file__).parent
sys.path.insert(0,str(root/'code'))
from fractions import Fraction as F
from decimal import Decimal, localcontext
import numpy as np
from pde.observable_fixed import Fixed, nearest

result={}
T,C,R,B=F(1,200),F(101,10000),F(10101,10000),F(1,32)
D=B+2*R*C*C*T
exponent=6*R*D*T+8*R*R*T*T*C*C
d0=2*R*T+2*C
ab=4*R/(1-exponent)
psi=d0/(1-d0*T*(ab+2*R))
checks={'readout_upper':F(60401,59800)<R,'D':D<F(1,31), 'A_exponent':exponent<F(1,1000), 'A_B':ab<F(41,10), 'A_plus_2R':ab+2*R<F(31,5), 'outer_exponent':d0*T*F(31,5)<F(1,1000), 'Psi':psi<B, 'rank_HS':2*T*R*C<F(1,1000), 'action_op':2+2*T*R*C<F(201,100),'speed':2*R*((2+2*T*R*C)*C+C+1)<3}
assert all(checks.values())
result['constants']={'checks':checks,'D':str(D),'A_exponent':str(exponent),'A_B_upper':float(ab),'Psi_upper':float(psi),'B_minus_Psi_upper':float(B-psi),'readout_margin':float(R-F(60401,59800))}

arithmetic=[]
with localcontext() as ctx:
    ctx.prec=90
    for p in (20,36):
        for value in ('0.0001','0.5','1','2','19'):
            a=Fixed(value,p); x=Decimal(value)
            for name,got,oracle in [('sqrt',a.sqrt(),x.sqrt()),('log',a.ln(),x.ln())]:
                error=abs(Decimal(got.units)/Decimal(got.scale)-oracle)*Decimal(10)**p
                assert error <= 2,(p,value,name,str(error))
                arithmetic.append([p,value,name,str(error)])
        for value in ('-3','-0.01','0','0.01','3'):
            a=Fixed(value,p); got=a.exp(); oracle=Decimal(value).exp()
            error=abs(Decimal(got.units)/Decimal(got.scale)-oracle)*Decimal(10)**p
            assert error<=2,(p,value,'exp',str(error))
            arithmetic.append([p,value,'exp',str(error)])
ties={str(F(n,2)):nearest(F(n,2)) for n in range(-9,10,2)}
assert list(ties.values())==[-4,-4,-2,-2,0,0,2,2,4,4]
result['arithmetic']={'unit_errors':arithmetic,'signed_ties':ties}

# Distinct probability spaces with weighted raw features, one duplicate and zero.
p=np.array([.1,.2,.3,.4]); q=np.array([.2,.3,.5])
S1=np.array([[1,0,1,0],[1,1,1,0],[1,-1,1,0],[1,2,1,0]],float)
S2=np.array([[1,2,0],[1,-1,0],[1,.5,0]],float)
A=np.array([[.4,-.2,.1,.7],[-.5,.8,.2,.1],[.9,.3,-.6,.2]])
G1=S1.T@(p[:,None]*S1); G2=S2.T@(q[:,None]*S2)
eta=.03125
L1=np.linalg.cholesky(G1+eta*np.eye(4));L2=np.linalg.cholesky(G2+eta*np.eye(3))
b1=np.linalg.solve(L1,S1.T).T;b2=np.linalg.solve(L2,S2.T).T
Craw=S2.T@(q[:,None]*(A@S1))
Dmat=np.linalg.solve(L2,np.linalg.solve(L1,Craw.T).T)
kernel=b2@Dmat@b1.T@np.diag(p)
raw=S2@np.linalg.solve(G2+eta*np.eye(3),Craw)@np.linalg.solve(G1+eta*np.eye(4),S1.T)@np.diag(p)
adj=b1@Dmat.T@b2.T@np.diag(q)
oracle_adj=np.diag(1/p)@kernel.T@np.diag(q)
Q1=b1@b1.T@np.diag(p)
Qe=np.sqrt(p)[:,None]*Q1/np.sqrt(p)[None,:]
a=np.array([1,-2,3,.5]); v=S1@a
lhs=float(np.sum(p*((np.eye(4)-Q1)@v)**2)); rhs=eta*float(a@a)/4
err=float(np.max(np.abs(kernel-raw))); adjerr=float(np.max(np.abs(adj-oracle_adj)))
assert err<1e-11 and adjerr<1e-11
assert np.linalg.eigvalsh(Qe).min()>-1e-11 and np.linalg.eigvalsh(Qe).max()<=1+1e-11 and lhs<=rhs+1e-11
result['ridge']={'kernel_error':err,'adjoint_error':adjerr,'spectrum':np.linalg.eigvalsh(Qe).tolist(),'residual_squared':lhs,'residual_bound':rhs,'raw_feature_counts':[4,3]}

couplings=[]
for count in (100,160):
    x,weight=np.polynomial.hermite.hermgauss(count); weight/=np.sqrt(np.pi)
    g=np.sqrt(2)*x; variance=float(weight@(np.tanh(g)**2)); xi=np.sqrt(variance)*g; h=np.tanh(xi)
    for k in (3,5):
        powers=np.column_stack([h**j for j in range(k)])
        coeff=np.linalg.solve(powers.T@(weight[:,None]*powers),powers.T@(weight*h**k))
        poly=h**k-powers@coeff; coupling=float(weight@(poly*xi)); residual=float(np.max(np.abs(powers.T@(weight*poly))))
        assert coupling>0 and residual<1e-11
        couplings.append({'nodes':count,'degree':k,'variance':variance,'coupling':coupling,'orthogonality_error':residual})
result['odd_enrichment']=couplings

def u(s): return ((1-s*s)/(1+s*s),2*s/(1+s*s))
def rot(x): return ((3*x[0]-4*x[1])/5,(4*x[0]+3*x[1])/5)
dots=[]
for s in (-F(1,20),F(0),F(1,20)):
    for t in (-F(1,20),F(0),F(1,20)):
        x,y=u(s),rot(u(t));dot=x[0]*y[0]+x[1]*y[1]
        assert sum(z*z for z in x)==1 and sum(z*z for z in y)==1 and F(2,5)<=dot<=F(4,5)
        dots.append(str(dot))
quadratures=[]
for a,b in [(-F(1,20),F(1,20)),(F(1,20),F(1,20)),(-F(1,20),F(0))]:
    for m in (1,3,8):
        # derivative norm <=2; integral average |s-midpoint| = interval/(4m).
        upper=(b-a)/(2*m)
        assert upper<=F(1,20*m)
        quadratures.append([str(a),str(b),m,str(upper)])
result['law']={'exact_dot_values':dots,'W1_bounds':quadratures}

def radical(i,base):
    value,den=F(0),1
    while i:
        i,digit=divmod(i,base);den*=base;value+=F(digit,den)
    return value
prefix=[]
for base in (2,3,5,7):
    for n in (1,2,3,7,31,257):
        vals=[radical(i,base) for i in range(1,n+1)]
        assert min(vals)>=F(1,base*n) and max(vals)<=1-F(1,base*n)
        prefix.append([base,n,str(min(vals)),str(max(vals))])
result['halton_endpoints']=prefix
result['cpu_seconds']=time.process_time()-start
result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
result['status']='pass'
(out/'scalar_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
