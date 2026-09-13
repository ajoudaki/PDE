"""F predeclared manufactured attacks; no research initialization or trajectory."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import os,sys,json,resource,time
ROOT=Path('/home/amir/Codes/PDE');ED=ROOT/'data/generated/observable_hierarchy/H4_candidate_v3';OUT=ROOT/'data/generated/observable_hierarchy/H4_scientific_F_v3'
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1');sys.dont_write_bytecode=True
resource.setrlimit(resource.RLIMIT_AS,(4*2**30,)*2);resource.setrlimit(resource.RLIMIT_CPU,(50,)*2);sys.path.insert(0,str(ED/'code'));sys.path.insert(0,str(ED/'code/tests'))
import numpy as np
from pde import observable_solver as s
from pde.observable_arithmetic import Arithmetic
from pde.observable_laws import *
from pde.observable_laws import _working_fraction,_fraction_from_record
from scripts import validate_observable_horizon as worker
from test_observable_horizon_validation import fixture
start=time.process_time();out={};checks=[]
def check(v,name):
 assert v,name
 checks.append(name)
state,data=fixture();state.p1*=1+2e-13;state.p2*=1-3e-13;data.probabilities*=1+1e-13
original=[a.copy() for a in (state.p1,state.p2,data.probabilities)];v=s.rhs(state,data,block_size=1);errors=[]
for key,vel,metric in [('w',v[0],state.p1[:,None]),('c',v[1],state.p2),('M',v[2],1)]:
 expected=-vel*metric
 for ij in np.ndindex(getattr(state,key).shape):
  plus,minus=state.copy(),state.copy();getattr(plus,key)[ij]+=1e-6;getattr(minus,key)[ij]-=1e-6
  diff=float((s.loss(plus,data)-s.loss(minus,data))/2e-6);errors.append(abs(diff-expected[ij]))
check(max(errors)<1e-7,'all dynamic coordinate gradients with nonunit literal masses');out['maximum_coordinate_gradient_error']=max(errors)
for a,b in zip(original,(state.p1,state.p2,data.probabilities)):check(np.array_equal(a,b),'no mass normalization')
# Independent direct output and all RHS entries from elementwise population sums.
b1,g,w,p1,b2,c,p2,M,D=[getattr(state,k) for k in worker.STATE_KEYS];u,y,dp=data.inputs,data.labels,data.probabilities
h=np.tanh(w@u.T);a=np.einsum('pj,p,pa->ja',b1,p1,h);z=np.einsum('qi,ij,ja->qa',b2,M,a);H=np.tanh(z);f=np.einsum('q,q,qa->a',p2,c,H)
d=np.einsum('qi,q,q,qa->ia',b2,p2,c,1-H*H);q=np.einsum('pj,ij,ia->pa',b1,M,d);r=dp*(f-y)
vv=(-2*np.einsum('pa,pa,a,ad->pd',1-h*h,q,r,u),-2*np.einsum('qa,a->q',H,r),-2*np.einsum('ia,a,ja->ij',d,r,a))
err=max(float(np.max(abs(x-y))) for x,y in zip(v,vv));check(err<1e-11,'all RHS entries independently contracted');out['direct_rhs_error']=err
for ar in (Arithmetic(),Arithmetic(40),Arithmetic(24,'rational')):
 st,da=fixture(ar);one=s.evolve(st,da,steps=1,step_size=F(1,100),block_size=1);p=OUT/('manufactured_restart_'+str(ar.digits)+ar.backend+'.json');s.save_restart(p,one,da);loaded,ld=s.load_restart(p)
 check(worker.exact_restart_comparison(one,da,loaded,ld)['all_exact'],'exact all-backend own-state serialization')
 left=s.evolve(one,da,steps=1,step_size=F(1,100),block_size=1);right=s.evolve(loaded,ld,steps=1,step_size=F(1,100),block_size=1)
 check(worker.exact_restart_comparison(left,da,right,ld)['all_exact'],'exact all-backend next-step continuation')
# Same fixed positive radius: deliberate replacement, coordinate rounding, then resolution.
rows=[]
for digits in (20,40,80):
 law=OrthogonalArcLaw(DyadicRadius(200),a='-1/3',b='1/2',c='-1',d='1');rule=law.quadrature(3,Arithmetic(digits,'rational'))
 rows.append(dict(digits=digits,replacement=rule.metadata['radius_replaced_by_zero'],roundingcollapse=rule.metadata['exact_midpoint_rule_collapsed_by_rounding'],allreference=rule.metadata['all_working_inputs_are_reference']))
check(rows[0]['replacement'] and rows[1]['replacement'] and not rows[2]['allreference'],'fixed radius eventually resolves');out['collapse_refinement']=rows
# Exact noncollapsed small rational rule versus independent rational circle map.
ar=Arithmetic(60,'rational');law=OrthogonalArcLaw(RationalRadius('2/7'),a='-3/4',b='2/3',c='-1/5',d='4/5');rule=law.quadrature(5,ar);rounderr=F(0)
for group,(lo,hi) in enumerate(((law.a,law.b),(law.c,law.d))):
 for j in range(5):
  x=F(2,7)*(lo+(hi-lo)*F(2*j+1,10));U=((1-x*x)/(1+x*x),2*x/(1+x*x));U=U if group==0 else (-U[1],U[0]);actual=rule.inputs[group*5+j];rounderr=max(rounderr,sum(abs(_working_fraction(a)-b) for a,b in zip(actual,U)))
check(rounderr==_fraction_from_record(rule.metadata['maximum_coordinate_rounding_l1']),'independent rational law rounding certificate');out['law_max_rounding_l1']=str(rounderr)
# Provenance label cannot change the worker's certified radius.
plan=dict(supported_radius=supported_radius().to_record(),common=dict(law_limits={}),law_parameters={'x':dict(radius=DyadicRadius(4).to_record(),scope_tag='H4_explicit_supported_T40')})
try:worker.build_law(plan,{'law':'x'})
except ValueError:checks.append('forged supported radius rejected')
else:raise AssertionError('forged supported radius accepted')
# Precise scalar edges; independent Decimal exp/ln/sqrt references.
primitive=[]
for digits in (24,40):
 ar=Arithmetic(digits,'rational')
 with localcontext() as ctx:
  ctx.prec=digits+40
  for name,values in [('exp',['-20','0','20']),('ln',['0.00000000000000000001','0.5','20']),('sqrt',['0','0.00000000000000000001','20'])]:
   for x in values:
    got=getattr(ar.real(x),name)();ref=getattr(Decimal(x),name)();err=abs(Decimal(got.units)/Decimal(got.scale)-ref);primitive.append(float(err));check(err<Decimal(10)**(-digits+2),'rational '+name+' edge '+x)
out['maximum_primitive_absolute_error']=max(primitive);out.update(checks=checks,cpu_seconds=time.process_time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,status='PASS');(OUT/'attack_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
