from fractions import Fraction as F
import itertools, json, math
import numpy as np
from pde.mfp_compiler import Program, ProgramError
from pde.mfp_finite import evaluate_finite
from pde import mfp_expr as ex

results={}
def record(name,value):
 results[name]=value;print(name, value)

# Cyclic type graph and two named matrices: independently integrate the
# finite polynomial ||W V W 1||^2/n by raw-entry Wick pairing.
p=Program();a=p.vector_type('a');b=p.vector_type('b')
w=p.matrix('W',a,b);v=p.matrix('V',b,a);one=p.one(a)
out=p.inner(w@(v@(w@one)),w@(v@(w@one)))
limit=p.compile(out).output
exact=[]
for n in (1,2,3):
 value=F(0)
 for i,j,k,l,J,K,L in itertools.product(range(n),repeat=7):
  factors=[('W',i,j),('V',j,k),('W',k,l),('W',i,J),('V',J,K),('W',K,L)]
  counts={f:factors.count(f) for f in set(factors)}
  term=F(1,n)
  for count in counts.values():
   if count%2:term=0;break
   term*=F(math.prod(range(1,count,2)),n**(count//2))
  value+=term
 expected=1+F(2,n*n);assert value==expected
 exact.append(str(value))
assert limit==ex.const(1)
record('cyclic_graph_raw_entry_Wick',dict(limit=str(limit),finite=exact,formula='1+2/n^2'))

# Exact singular duplicate and zero cancellation; a frozen value still carries
# its source paths in the Gaussian calculus.
p=Program();a=p.vector_type('a');b=p.vector_type('b');w=p.matrix('W',a,b)
x=p.root('x',a);y1=w@x;y2=w@x
zero=w.T@(y1**3-y2**3)
assert p.compile(p.inner(zero,zero)).output==ex.const(0)
y=p.freeze(y1**3);assert p.compile(p.inner(x,w.T@y)).output==ex.const(3)
assert p.compile(p.directional(p.mean(y),{x:p.one(a)})).output==ex.const(0)
record('singular_and_frozen_source_paths','PASS')

# Independent dense tanh network on the cycle a -> b -> a -> b.
# Central coordinate finite differences do not use builder AD.
p=Program();a=p.vector_type('a');b=p.vector_type('b');x=p.root('x',a);u=p.root('u',b)
w=p.matrix('W',a,b);v=p.matrix('V',b,a);s=p.parameter('s')
z=w@(v@p.phi(w@x))+u
back=w.T@p.phi(z)
output=p.mean(p.phi(back*p.mean(back**2)+s))
grad=p.gradient(output,vectors=[x,u],matrices=[w,v],scalars=[s])
state={'x':np.array([.2,-.4]),'u':np.array([.3,.1]),'W':np.array([[.6,-.2],[.4,.7]]),'V':np.array([[-.1,.5],[.3,-.2]]),'s':.2}
def direct(d):
 z=d['W']@(d['V']@np.tanh(d['W']@d['x']))+d['u']
 back=d['W'].T@np.tanh(z)
 return np.mean(np.tanh(back*np.mean(back**2)+d['s']))
def activation(r,t):
 if r==0:return math.tanh(float(t))
 if r==1:return 1-math.tanh(float(t))**2
 raise ValueError(r)
def ev(node):return evaluate_finite(node,2,{x:state['x'].tolist(),u:state['u'].tolist()},{w:state['W'].tolist(),v:state['V'].tolist()},{s:state['s']},activation)
def dense(rank):
 arr=np.zeros((2,2))
 for c,l,r in rank.terms:arr+=float(ev(c))*np.outer(ev(l),ev(r)).astype(float)/2
 return arr
errors={}
for name,node,mob in [('x',x,2),('u',u,2),('W',w,1),('V',v,1),('s',s,1)]:
 actual=np.array(dense(grad[node]) if name in ('W','V') else ev(grad[node]),dtype=float)
 indices=list(np.ndindex(actual.shape)) if actual.shape else [()]
 expected=np.zeros_like(actual)
 for index in indices:
  plus={k:np.array(val,copy=True) if isinstance(val,np.ndarray) else val for k,val in state.items()};minus={k:np.array(val,copy=True) if isinstance(val,np.ndarray) else val for k,val in state.items()}
  if index:plus[name][index]+=1e-6;minus[name][index]-=1e-6
  else:plus[name]+=1e-6;minus[name]-=1e-6
  expected[index]=mob*(direct(plus)-direct(minus))/2e-6
 errors[name]=float(np.max(np.abs(actual-expected)))
 assert errors[name]<1e-8
record('cyclic_tanh_scalar_feedback_finite_AD',errors)

# Frozen seed semantics on an enlarged parameter space: seed b=x0 is held
# fixed, so L(x;b)=mean(x*b) and x_(k+1)=x_k-eta*b.
p=Program();a=p.vector_type('a');x=p.root('x',a);seed=p.freeze(x)
loss=p.mean(x*seed);eta=F(1,10)
states=p.gradient_descent(loss,vectors=[x],steps=2,step_size=eta)
actual=evaluate_finite(states[x],2,{x:[F(1),F(2)]},{})
expected=tuple((1-2*eta)*z for z in (F(1),F(2)))
record('frozen_seed_two_updates',dict(actual=list(map(str,actual)),expected=list(map(str,expected)),matches=actual==expected))
# at() also changes the saved seed value after state substitution.
replaced=p.at(seed,{x:2*x})
record('frozen_seed_substitution',dict(actual=list(map(str,evaluate_finite(replaced,2,{x:[1,2]},{}))),fixed_seed=['1','2']))

# Current matrix gradients vs history pullbacks; independent scalar n=1 check.
p=Program();a=p.vector_type('a');b=p.vector_type('b');w=p.matrix('W',a,b);e=p.one(a)
loss=p.mean((w@e)**2)/2;state=p.gradient_descent(loss,matrices=[w],step_size=F(1,10))
g=p.gradient(loss,matrices=[w])[w]
current=p.at(g@e,state);pullback=p.gradient(p.at(loss,state),matrices=[w])[w]@e
assert evaluate_finite(current,1,{}, {w:[[2]]})[0]==F(9,5)
assert evaluate_finite(pullback,1,{}, {w:[[2]]})[0]==F(81,50)
record('ambient_matrix_vs_pullback','PASS')

# Core input validation boundaries, including exact near-PSD rejection.
errors=[]
for covariance in ([[0,1],[1,0]],[[1,F(1000001,1000000)],[F(1000001,1000000),1]],[[float('nan')]]):
 q=Program();t=q.vector_type('t')
 try:q.roots(t,['r'+str(i) for i in range(len(covariance))],covariance)
 except (ProgramError,ex.UnsupportedExpression):errors.append('rejected')
 else:errors.append('ACCEPTED')
assert errors==['rejected']*3
record('invalid_covariance_boundaries',errors)
print(json.dumps(results,indent=2))
