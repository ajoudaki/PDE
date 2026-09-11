"""Independent fixed deterministic algebra/boundary audit; no training."""
import json, math, platform
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.linalg import expm

out={}
phi=np.tanh
def gate(z): return 1/np.cosh(z)**2
def curv(z): return -2*phi(z)*gate(z)
def third(z): return 4*phi(z)**2*gate(z)-2*gate(z)**2
w=np.array([[.35,-.7],[1.2,.25]])
A=np.array([[.6,-.2],[.35,.8]])
c=np.array([.4,-.3])
xi=np.array([[.3,-.2],[-.4,.5]])
B=np.array([[.15,.2],[-.25,.1]])
d=np.array([-.2,.3])
e1,e2=np.eye(2)
ref=[(.5,e1,1.),(.5,e2,-1.)]
nu=[(.4,np.array([-.6,.8]),1.5),(.6,np.array([.8,-.6]),-.5)]
sigma=nu+[(-p,u,y) for p,u,y in ref]
n=2

def vals(w,A,c,u):
 h=phi(w@u); z=A@h; H=phi(z); delta=c*gate(z); Q=A.T@delta
 return h,z,H,delta,Q,c@H/n

def raw(w,A,c,law):
 dtype=np.result_type(w,A,c,*[p for p,u,y in law])
 fw=np.zeros(w.shape,dtype=dtype); fA=np.zeros(A.shape,dtype=dtype); fc=np.zeros(c.shape,dtype=dtype)
 for p,u,y in law:
  h,z,H,delta,Q,f=vals(w,A,c,u); r=f-y
  fw-=2*p*r*(gate(w@u)*Q)[:,None]*u
  fA-=2*p*r*np.outer(delta,h)/n
  fc-=2*p*r*H
 return fw,fA,fc

def source(w,A,c,law):
 q=raw(w,A,c,law)
 return q[0]/gate(w),q[1],q[2]

def flat(v):return np.concatenate([x.ravel() for x in v])

def directional(w,A,c,u):
 h,z,H,delta,Q,f=vals(w,A,c,u)
 dh=gate(w@u)*((gate(w)*xi)@u)
 dz=B@h+A@dh
 ddelta=d*gate(z)+c*curv(z)*dz
 dQ=B.T@delta+A.T@ddelta
 df=(d@H+delta@dz)/n
 return dh,dz,ddelta,dQ,df

# Assemble clock tangent directly from cancellation at the two training directions.
expected=[np.zeros_like(w),np.zeros_like(A),np.zeros_like(c)]
for a,(p,u,y) in enumerate(ref):
 h,z,H,delta,Q,f=vals(w,A,c,u); dh,dz,ddelta,dQ,df=directional(w,A,c,u); r=f-y
 expected[0][:,a]-=2*p*(df*Q+r*dQ)
 expected[1]-=2*p*(df*np.outer(delta,h)+r*np.outer(ddelta,h)+r*np.outer(delta,dh))/n
 expected[2]-=2*p*(df*H+r*gate(z)*dz)
expected=[v+b for v,b in zip(expected,source(w,A,c,sigma))]
cs=1e-25
raw0=raw(w,A,c,ref)
law_eps=ref+[(1j*cs*p,u,y) for p,u,y in sigma]
raw_der=[np.imag(v)/cs for v in raw(w+1j*cs*gate(w)*xi,A+1j*cs*B,c+1j*cs*d,law_eps)]
clock_correction=curv(w)*raw0[0]*xi/gate(w)
converted=[raw_der[0]/gate(w)-clock_correction,raw_der[1],raw_der[2]]
err=float(np.max(np.abs(flat(converted)-flat(expected))))
wrong=float(np.max(np.abs(flat([raw_der[0]/gate(w),raw_der[1],raw_der[2]])-flat(expected))))
assert err<2e-12 and wrong>1e-5
out['raw_variational_equation_to_clock']={'max_error':err,'error_if_clock_time_correction_omitted':wrong}

# Passive scalar derivative and full angular Riesz-field derivative.
alpha=.73
u0=np.array([np.cos(alpha),np.sin(alpha)])
uprime=np.array([-np.sin(alpha),np.cos(alpha)])
_,_,_,_,_,f=vals(w,A,c,u0)
manual_df=directional(w,A,c,u0)[-1]
cs_df=np.imag(vals(w+1j*cs*gate(w)*xi,A+1j*cs*B,c+1j*cs*d,u0)[-1])/cs
assert abs(manual_df-cs_df)<2e-12

def riesz(angle):
 u=np.array([np.cos(angle),np.sin(angle)])
 h,z,H,delta,Q,f=vals(w,A,c,u)
 row=gate(w)*(gate(w@u)*Q)[:,None]*u
 return row,np.outer(delta,h)/n,H
h,z,H,delta,Q,f=vals(w,A,c,u0)
ha=gate(w@u0)*(w@uprime); za=A@ha
deltaa=c*curv(z)*za; Qa=A.T@deltaa
ra=gate(w)*(uprime[None,:]*(gate(w@u0)*Q)[:,None]+u0[None,:]*(curv(w@u0)*(w@uprime)*Q+gate(w@u0)*Qa)[:,None])
manual_ra=[ra,(np.outer(deltaa,h)+np.outer(delta,ha))/n,gate(z)*za]
cs_ra=[np.imag(v)/cs for v in riesz(alpha+1j*cs)]
ra_err=float(np.max(np.abs(flat(cs_ra)-flat(manual_ra))))
assert ra_err<2e-12
out['passive_observation']={'directional_prediction_error':float(abs(manual_df-cs_df)),'angular_riesz_error':ra_err}

zero=source(w,A,np.zeros_like(c),sigma)
assert np.max(np.abs(flat(zero[:2])))==0
assert np.linalg.norm(zero[2])>1e-5
actual=source(w,A,c,sigma)
assert np.linalg.norm(actual[0])>1e-5 and np.linalg.norm(actual[1])>1e-5
zerosigma=ref+[(-p,u,y) for p,u,y in ref]
assert np.max(np.abs(flat(source(w,A,c,zerosigma))))<2e-12
split=[(.2,nu[0][1],nu[0][2]),(.2,nu[0][1],nu[0][2]),nu[1]]+[(-p,u,y) for p,u,y in ref]
spliterr=float(np.max(np.abs(flat(source(w,A,c,split))-flat(actual))))
assert spliterr<2e-12
out['source_boundaries']={'zero_readout_hidden_middle_exactly_zero':True,'zero_readout_source_norm':float(np.linalg.norm(zero[2])),'actual_readout_hidden_norm':float(np.linalg.norm(actual[0])),'actual_readout_middle_norm':float(np.linalg.norm(actual[1])),'zero_measure_source':True,'atom_splitting_error':spliterr}

# L2([0,1]), D=x, S(alpha)=alpha_1+2alpha_2. Polynomial basis (1,x).
H=np.array([[F(1),F(1,2)],[F(1,2),F(1,3)]],dtype=object)
SE=np.array([[F(5,2),F(5,3)],[F(0),F(0)]],dtype=object)
P=np.array([[F(0),F(-2,3)],[F(0),F(1)]],dtype=object)
I=np.array([[F(1),F(0)],[F(0),F(1)]],dtype=object)
assert np.array_equal(P@P,P)
assert np.array_equal(SE@P,np.zeros((2,2),dtype=object))
assert np.array_equal(P@SE,np.zeros((2,2),dtype=object))
Gram=F(1,2)*np.array([[F(1),F(2)],[F(2),F(4)]],dtype=object)
assert np.array_equal(Gram@np.array([F(-2),F(1)]),np.zeros(2,dtype=object))
t=.7
formula=np.asarray(P,dtype=float)+math.exp(-5*t)*np.asarray(I-P,dtype=float)
semerr=float(np.max(np.abs(expm(-2*t*np.asarray(SE,dtype=float))-formula)))
assert semerr<2e-12
badS=np.array([[1.],[0.]])
badE=np.array([[0.,1.]])
assert np.array_equal(badE@badS,np.zeros((1,1)))
assert np.max(np.abs(expm(-2*t*badS@badE)-(np.eye(2)-2*t*badS@badE)))<2e-12
out['singular_noncoercive_population_boundary']={'exact_rational_projector_identities':True,'singular_gram_kernel':[-2,1],'semigroup_error':semerr,'D_injective_not_coercive':'D=x on [0,1]; unit L2 vectors supported on [0,1/k] have ||Dv|| <= 1/k','nilpotent_without_compatibility':'exp(-2tSE)=I-2tSE grows linearly when ES=0 but SE !=0'}

# F'(z)=cosh^2 z and d_X cosh^2(j)=2tanh(j).
def primitive(z):return z/2+np.sinh(2*z)/4
clockchecks=[]
for g,X in [(0.,0.),(2.,-.4),(-1.,.7),(20.,0.)]:
 j=g if X==0 else brentq(lambda z:primitive(z)-primitive(g)-X,g-abs(X)-1,g+abs(X)+1,xtol=1e-14)
 identity=np.sinh(2*j)*gate(j)-2*phi(j)
 envelope=np.cosh(g)**2+2*abs(X)-np.cosh(j)**2
 assert abs(identity)<2e-12 and envelope>=-2e-12
 clockchecks.append({'g':g,'X':X,'j':float(j),'identity_error':float(abs(identity)),'envelope_slack':float(envelope)})
out['clock_envelope']=clockchecks

# Independent scalar numerical quadrature with a certified negligible truncation tail.
def expectation(fun):return quad(lambda x:2/math.sqrt(2*math.pi)*math.exp(-x*x/2)*fun(x),0,8,epsabs=2e-12,epsrel=2e-12,limit=100)
q,qe=expectation(lambda x:math.tanh(x)**2)
v,ve=expectation(lambda x:math.tanh(math.sqrt(q)*x)**2)
a,ae=expectation(lambda x:1/math.cosh(x)**8)
r,re=expectation(lambda x:1/math.cosh(math.sqrt(q)*x)**4)
assert .39<q<.4 and v>.2 and a>.3 and r>.6
out['independent_reference_quadrature']={'q':q,'v':v,'a0':a,'r0':r,'reported_quad_errors':[qe,ve,ae,re],'elementary_tail_bound':2*math.exp(-32)/(8*math.sqrt(2*math.pi)),'uses_exact_q_for_scaled_integrals':False,'scope':'quadrature uses numerical q with error reported; exact supplied rational certificate provides the rigorous margins'}
M=2+math.sqrt(10); L0=math.sqrt(1+10*(1+M*M))
assert L0<17
out['constants']={'L0':L0,'integral_exp_minus_t_over_5':5,'integral_exp_minus_t_over_10':10,'population_weighted_gram_rank':1}
out['status']='PASS'
out['environment']={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
