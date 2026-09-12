"""Independent bounded static review checks; no trajectories or random samples.

Precommitted discriminators: analytic biased Gaussian Grams/Stein coefficient
(3e-11 tolerance), singular named-partial cancellation (2e-13), explicit weighted
kernel and gradient (3e-9 finite differences), exact excerpt correspondence.
One execution, no parameter search or accuracy campaign.
"""
from pathlib import Path
import hashlib
import json
import math
import re
import sys

import numpy as np

ROOT = Path('/home/amir/Codes/PDE')
OUT = ROOT/'data/generated/observable_hierarchy/H2_review_v3_b'
sys.path.insert(0, str(OUT/'edition/code'))
from pde import observable_closure as c

checks = {}
# Bias must contribute its square to the Gaussian source variance.
one = c.constant(1)
h = c.add(one, c.unary('sin', c.seed('g1')))
z = c.action(h)
reverse = c.action(c.unary('sin', z))
program = c.GaussianProgram(c.QuadratureLimits(order=15, max_innovation_dimension=3)).compile([c.action(one), z, reverse])
var = 1+(1-math.exp(-2))/2
alpha = math.exp(-var/2)
assert abs(program.diagnostics[1]['variance']-var) < 3e-11
assert abs(program.diagnostics[1]['covariance'][0]-1) < 3e-11
response = dict((w,co) for w,co in program.sources[reverse].response)
assert abs(response[h]-alpha) < 3e-11
assert abs(response[one]) < 3e-11
checks['biased_correlated_source'] = dict(variance=program.diagnostics[1]['variance'], expected_variance=var, covariance=program.diagnostics[1]['covariance'], response=response[h], expected_response=alpha)

# Same-support expression zero still has two nonzero frozen named partials;
# contracting these with the corresponding source inputs cancels exactly.
f1, f2 = c.action(one), c.action(c.scale(2, one))
cancel = c.unary('sin', c.add(f2, c.scale(-2, f1)))
back = c.action(cancel)
p = c.GaussianProgram(c.QuadratureLimits(order=2, max_innovation_dimension=4)).compile([f1,f2,back])
values, derivatives = p.evaluate(cancel, derivative=True)
assert np.max(np.abs(values)) < 2e-13
assert np.max(np.abs(derivatives[:,0]+2)) < 2e-13
assert np.max(np.abs(derivatives[:,1]-1)) < 2e-13
assert np.max(np.abs(p.evaluate(back))) < 2e-13
checks['singular_named_partial_cancellation'] = dict(value_max=float(np.max(np.abs(values))), partials=derivatives[0].tolist(), response=[v for _,v in p.sources[back].response], reverse_max=float(np.max(np.abs(p.evaluate(back)))))

# Rectangular populations and deliberately nonorthonormal feature lists.
s = c.State(c.Population1([[1.,.2],[1.,-.4],[1.,.7]], [[0.,0.],[.2,.8],[-.5,.3]], [[.1,.2],[.4,-.3],[-.7,.6]], [.2,.3,.5]), c.Population2([[1.,-.6,.3],[1.,.1,-.2]], [.4,-.2], [.65,.35]), [[.3,-.1],[.2,.4],[-.2,.15]], [[.1,.2],[.3,.1],[-.1,.4]])
law = c.DataLaw([[1.,0.],[.6,.8],[1.,0.]], [1.,-.4,7.], [.4,.6,0.])
kernel = s.second.b @ s.M @ s.first.b.T
x = np.array([.2,-.7,.4]); y = np.array([.8,-.3])
forward = kernel @ (s.first.probabilities*x)
reverse_v = kernel.T @ (s.second.probabilities*y)
assert np.max(np.abs(c.apply_action(s,1,x)-forward)) < 2e-14
assert np.max(np.abs(c.apply_action(s,2,y)-reverse_v)) < 2e-14
v = c.rhs(s,law)
eps=1e-6
errs=[]
for idx in np.ndindex(s.M.shape):
    a,b=s.copy(),s.copy(); a.M[idx]+=eps; b.M[idx]-=eps
    errs.append(abs((c.loss(a,law)-c.loss(b,law))/(2*eps)+v.M[idx]))
assert max(errs) < 3e-9
paired,weights=c.joint_observe(s,[c.seed('w1'),c.seed('g1')])
assert np.array_equal(paired[:,0],s.first.w[:,0])
assert np.array_equal(paired[:,1],s.first.g[:,0])
assert np.array_equal(weights,s.first.probabilities)
checks['nonorthonormal_weighted_state'] = dict(matrix_gradient_error_max=max(errs), adjoint_pairing_error=float(abs(y @ (s.second.probabilities*forward)-x @ (s.first.probabilities*reverse_v))))

guides=[]
for part in (ROOT/'studies/observable_hierarchy/H2_guides_v1.md').read_text().split('\n---\n'):
    if not part.lstrip().startswith('Source:'):
        continue
    header,body=part.strip().split('\n\n',1)
    name=header.split('`')[1]
    assert body.strip()==(ROOT/name).read_text().strip(), name
    guides.append(name)
obs=[]
source=(ROOT/'docs/gaussian_calculus.md').read_text().splitlines()
for part in (ROOT/'studies/observable_hierarchy/H2_obstructions_v1.md').read_text().split('\n---\n'):
    if not part.lstrip().startswith('Source lines '):
        continue
    header,body=part.strip().split('\n\n',1)
    a,b=map(int,re.findall(r'\d+',header))
    assert body.strip()=='\n'.join(source[a-1:b]).strip(), header
    obs.append([a,b])
checks['exact_correspondence'] = dict(full_guides=guides, obstruction_ranges=obs)

# The relocated test's entire body differs only by the specified import/docstring.
old=(ROOT/'studies/observable_hierarchy/H2_test_prototype_v3.py').read_text()
expected=old.replace('os.environ.get("H2_PROTOTYPE_MODULE", "H2_prototype_v3")','os.environ.get("H2_PROTOTYPE_MODULE", "pde.observable_closure")').replace('Set H2_PROTOTYPE_MODULE=pde.observable_closure after a reviewed relocation.\nThe default imports the study-owned prototype beside this file.','The default imports pde.observable_closure from the installed package.\nH2_PROTOTYPE_MODULE may override that import for isolated checks.')
assert expected==(OUT/'edition/code/tests/test_observable_closure.py').read_text()
checks['relocated_test_exact'] = True
checks['numpy_version']=np.__version__
result=dict(status='PASS',checks=checks)
(OUT/'adversarial_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
