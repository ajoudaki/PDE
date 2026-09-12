"""Independent deterministic static attacks. No trajectory or accuracy sweep.

Precommit: analytic correlated-source quantities must agree within 2e-10;
singular contracted answers within 1e-12; finite named-source derivative
differences within 2e-8. One fixed GH order 15, at most 100000 nodes,
at most 4 Gaussian coordinates per population. Failures are code concerns
only if their floating validity gates are satisfied. No training is run.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import re
import sys

import numpy as np
from pde import observable_closure as c

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).resolve().parent
results = {}

# Exact source correspondence, including packets omitted by the supplied check.
guides = (ROOT / 'studies/observable_hierarchy/H2_guides_v1.md').read_text()
guide_count = 0
for part in guides.split('\n---\n'):
    if part.lstrip().startswith('Source:'):
        header, body = part.strip().split('\n\n', 1)
        source = header.split('`')[1]
        assert body.strip() == (ROOT / source).read_text().strip(), source
        guide_count += 1
obstructions = (ROOT / 'studies/observable_hierarchy/H2_obstructions_v1.md').read_text()
gaussian_lines = (ROOT / 'docs/gaussian_calculus.md').read_text().splitlines()
obstruction_count = 0
for part in obstructions.split('\n---\n'):
    match = re.match(r'\s*Source lines (\d+)–(\d+)\n\n(.*)', part, re.S)
    if match:
        start, end = map(int, match.group(1, 2))
        assert match.group(3).strip() == '\n'.join(gaussian_lines[start-1:end]).strip()
        obstruction_count += 1
assert guide_count == 5 and obstruction_count == 3
results['source_correspondence'] = dict(guides=guide_count, obstruction_bodies=obstruction_count)

# Concrete coding is causal, nested and finite, including high rational marks.
previous1 = previous2 = []
for order in range(1, 161):
    first, second, _ = c.initial_dictionary(order)
    assert first[:len(previous1)] == previous1 and second[:len(previous2)] == previous2
    assert len(first)+len(second) <= order+15
    previous1, previous2 = first, second
for a in range(15):
    for b in range(15):
        k = c.pair(a,b)
        for j in range(4,8):
            assert max(a,b) < 4+8*k+j
assert {c.rational_code(i) for i in range(1000)} >= {Fraction(3,7),Fraction(-5,3),Fraction(0)}
results['dictionary'] = dict(prefixes_checked=160, last_dimensions=[len(previous1),len(previous2)])

# Nonzero means must not be centered out of the source Gram.
limits = c.QuadratureLimits(order=15, max_nodes=100000, max_innovation_dimension=4)
h1 = c.unary('sin',c.seed('g1'))
h2 = c.scale(Fraction(1,2),c.add(h1,c.unary('cos',c.seed('g2'))))
z1,z2 = c.action(h1),c.action(h2)
d = c.add(c.unary('sin',z2),c.unary('cos',z1))
p = c.action(d)
program = c.GaussianProgram(limits).compile([z1,z2,p])
v1=(1-math.exp(-2))/2
v2=0.25
target_cov=v1/2
target_response=math.exp(-v2/2)
target_variance=(1-math.exp(-2*v2))/2+(1+math.exp(-2*v1))/2
observed = dict(var1=program.diagnostics[0]['variance'],
                var2=program.diagnostics[1]['variance'],
                covariance=program.diagnostics[1]['covariance'][0],
                reverse_variance=program.diagnostics[2]['variance'],
                response=program.diagnostics[2]['response'])
assert abs(observed['var1']-v1)<2e-10
assert abs(observed['var2']-v2)<2e-10
assert abs(observed['covariance']-target_cov)<2e-10
assert abs(observed['reverse_variance']-target_variance)<2e-10
assert abs(observed['response'][0])<2e-10
assert abs(observed['response'][1]-target_response)<2e-10
results['correlated_uncentered_source'] = observed

# Singular support does not erase the two frozen formal derivatives.
z=c.action(c.constant(1))
z_twice=c.action(c.scale(2,c.constant(1)))
zero=c.unary('sin',c.add(z_twice,c.scale(-2,z)))
reverse=c.action(zero)
singular=c.GaussianProgram(limits).compile([z,z_twice,reverse])
_,gradient=singular.evaluate(zero,derivative=True)
assert np.max(abs(gradient[:,0]+2))<1e-12
assert np.max(abs(gradient[:,1]-1))<1e-12
assert np.max(abs(singular.evaluate(reverse)))<1e-12
results['singular_formal_derivative'] = dict(response=singular.diagnostics[-1]['response'],
                                           reverse_max=float(np.max(abs(singular.evaluate(reverse)))))

# A second reverse call differentiates through the previous forward response.
pilot=c.pilot_words()
deep=c.GaussianProgram(limits).compile([pilot['p1']])
t=c.unary('sin',pilot['p1'])
new_z=c.action(t)
new_d=c.unary('sin',new_z)
new_p=c.action(new_d)
deep.compile([new_p])
upper=deep.carriers[2]
_,gradient=deep.evaluate(new_d,derivative=True)
original=upper.gaussian.copy()
errors=[]
epsilon=1e-6
for j in range(len(upper.sources)):
    upper.gaussian=original.copy(); upper.gaussian[:,j]+=epsilon
    plus=deep.evaluate(new_d)
    upper.gaussian=original.copy(); upper.gaussian[:,j]-=epsilon
    minus=deep.evaluate(new_d)
    errors.append(float(np.max(abs((plus-minus)/(2*epsilon)-gradient[:,j]))))
upper.gaussian=original
assert max(errors)<2e-8
expected=upper.weights @ gradient
actual=np.array(deep.diagnostics[-1]['response'])
assert np.max(abs(expected-actual))<1e-12
assert abs(actual[0])>0.01 and abs(actual[1])>0.01
results['deep_reuse_frozen_AD'] = dict(max_errors=errors,response=actual.tolist())

# Atom splitting and reordering must preserve all three current velocities.
state,_=c.initialize(1)
state.first.w += 0.05*np.column_stack([np.sin(state.first.g[:,1]),np.cos(state.first.g[:,0])])
state.second.c=0.1*np.sin(state.second.b[:,0])+0.04
state.M+=0.02*np.arange(state.M.size).reshape(state.M.shape)/state.M.size
data=c.DataLaw([[1,0],[0.6,0.8]],[1,-0.5],[0.25,0.75])
split=c.DataLaw([[0.6,0.8],[1,0],[0.6,0.8]],[-0.5,1,-0.5],[0.25,0.25,0.5])
v,vs=c.rhs(state,data),c.rhs(state,split)
atom_errors={name:float(np.max(abs(getattr(v,name)-getattr(vs,name)))) for name in ['w','c','M']}
assert max(atom_errors.values())<2e-14
results['weighted_data_splitting'] = atom_errors

# Complete state restoration remains sufficient without any compiler/metadata detail.
state.metadata={'format':'C-H2-quadrature-v1'}
c.save_restart(OUT/'adversarial_restart.npz',state,data)
restored,restored_data=c.load_restart(OUT/'adversarial_restart.npz')
restored_v=c.rhs(restored,restored_data)
for name in ['w','c','M']:
    np.testing.assert_array_equal(getattr(v,name),getattr(restored_v,name))
results['no_program_restart'] = 'bitwise equal RHS after stripping optional diagnostic metadata'

results['module_path'] = c.__file__
results['status'] = 'PASS'
(OUT/'adversarial_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
