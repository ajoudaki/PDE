"""Independent bounded static audit; no integration or sampling.

Precommitted checks: (1) an uncentered constant-containing correlated source
Gram and analytic sine response; (2) singular formal-source invariance;
(3) all-coordinate weighted gradient via independent nested-loop loss;
(4) ridge filter bound on a degenerate rectangular feature array.
Numerical gates are explicit below. One run; no accuracy search or training.
"""
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import math
import sys
import numpy as np

ROOT = Path('/home/amir/Codes/PDE')
spec = importlib.util.spec_from_file_location('review_core', ROOT/'studies/observable_hierarchy/H2_prototype_v3.py')
core = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = core
spec.loader.exec_module(core)
results = {}

# h=sin(g), k=1+sin(g) have E h=0, Gram [[v,v],[v,1+v]].
# z=A h, z'=A k. For d=sin(z+z'), Var(z+z')=1+4v and
# E partial_z d = E partial_z' d = exp(-(1+4v)/2).
h = core.unary('sin',core.seed('g1'))
k = core.add(core.constant(1),h)
z, zz = core.action(h),core.action(k)
d = core.unary('sin',core.add(z,zz))
p = core.action(d)
limits = core.QuadratureLimits(order=15,max_nodes=1000000,max_innovation_dimension=5)
program = core.GaussianProgram(limits).compile([z,zz,p])
v=(1-math.exp(-2))/2
alpha=math.exp(-(1+4*v)/2)
gram=np.array([[program.diagnostics[0]['variance'],program.diagnostics[1]['covariance'][0]],
               [program.diagnostics[1]['covariance'][0],program.diagnostics[1]['variance']]])
expected=np.array([[v,v],[v,1+v]])
responses=np.array(program.diagnostics[2]['response'])
gram_error=float(np.max(np.abs(gram-expected)))
response_error=float(np.max(np.abs(responses-alpha)))
assert gram_error < 1e-10 and response_error < 1e-9
lhs=float(program.carriers[1].weights @ (program.evaluate(h)*program.evaluate(p)))
rhs=float(program.carriers[2].weights @ (program.evaluate(z)*program.evaluate(d)))
assert abs(lhs-2*v*alpha)<1e-9 and abs(rhs-lhs)<1e-9
results['correlated_uncentered_source']={'gram_error':gram_error,'response_error':response_error,'adjoint_gap':abs(lhs-rhs),'pairing':lhs}

# Distinct formal inputs with identical values must agree after contraction.
z2=core.action(core.scale(2,h))
da=core.unary('sin',z2)
db=core.unary('sin',core.scale(2,z))
pa,pb=core.action(da),core.action(db)
singular=core.GaussianProgram(limits).compile([z,z2,pa,pb])
gap=float(np.sqrt(singular.carriers[1].weights @ ((singular.evaluate(pa)-singular.evaluate(pb))**2)))
assert gap<1e-6
ra=np.array([x[1] for x in singular.sources[pa].response])
rb=np.array([x[1] for x in singular.sources[pb].response])
assert abs(ra[0])<1e-12 and abs(rb[1])<1e-12
assert abs(2*ra[1]-rb[0])<1e-10
results['singular_named_source']={'value_RMS_gap':gap,'response_a':ra.tolist(),'response_b':rb.tolist()}

first=core.Population1([[1.,.2],[.5,-.3]],[[.1,.2],[-.2,.4]],[[.3,-.4],[-.7,.2]],[.3,.7])
second=core.Population2([[.8,-.1],[.4,.6],[-.3,.7]],[.2,-.1,.5],[.2,.3,.5])
state=core.State(first,second,[[.4,-.2],[.1,.3]],[[.4,-.2],[.1,.3]])
data=core.DataLaw([[1.,0.],[.6,.8]], [1.,-.2],[.4,.6])

def scalar_loss(s):
    total=0.
    for a,u in enumerate(data.inputs):
        prediction=0.
        for i in range(3):
            pre=0.
            for j in range(2):
                kernel=sum(s.second.b[i,b]*s.M[b,c]*s.first.b[j,c] for b in range(2) for c in range(2))
                pre+=s.first.probabilities[j]*kernel*math.tanh(sum(s.first.w[j,c]*u[c] for c in range(2)))
            prediction+=s.second.probabilities[i]*s.second.c[i]*math.tanh(pre)
        total+=data.probabilities[a]*(prediction-data.labels[a])**2
    return total

assert abs(scalar_loss(state)-core.loss(state,data))<1e-14
velocity=core.rhs(state,data)
errors=[]
eps=1e-6
for block in ('w','c','M'):
    original=state.first.w if block=='w' else state.second.c if block=='c' else state.M
    for index in np.ndindex(original.shape):
        plus,minus=state.copy(),state.copy()
        for copy,sign in ((plus,1),(minus,-1)):
            array=copy.first.w if block=='w' else copy.second.c if block=='c' else copy.M
            array[index]+=sign*eps
        derivative=(scalar_loss(plus)-scalar_loss(minus))/(2*eps)
        weight=state.first.probabilities[index[0]] if block=='w' else state.second.probabilities[index[0]] if block=='c' else 1.
        errors.append(abs(derivative+weight*getattr(velocity,block)[index]))
assert max(errors)<2e-10
results['independent_scalar_loss_gradient']={'coordinates':len(errors),'maximum_error':max(errors),'loss':scalar_loss(state)}

raw=np.array([[1.,1.,0.,2.],[1.,1.,0.,-1.],[1.,1.,0.,.5]])
prob=np.array([.2,.3,.5]); order=5
b,transform,gram=core.ridge_features(raw,prob,order)
S=np.sqrt(prob)[:,None]*raw
Q=np.sqrt(prob)[:,None]*b @ (np.sqrt(prob)[:,None]*b).T
coeff=np.array([.1,-.4,.2,.7]); residual=np.linalg.norm((np.eye(3)-Q)@S@coeff)
bound=math.sqrt(2**(-order))*np.linalg.norm(coeff)/2
assert residual<=bound+1e-14
assert np.linalg.eigvalsh(Q).min()>-1e-13 and np.linalg.eigvalsh(Q).max()<1+1e-13
results['ridge_filter']={'residual':float(residual),'bound':bound,'eigenvalues':np.linalg.eigvalsh(Q).tolist()}
print(json.dumps(results,indent=2))
