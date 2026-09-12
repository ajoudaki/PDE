"""Independent static review checks: no flow or training trajectory.

Precommitted gates: source/Stein 2e-9; singular cancellation 1e-10;
rank-filter and adjoint identities 3e-13; gradient direction 3e-10.
Only these prescribed tests, one run, GH order 15 with <= 100000 nodes.
"""
from fractions import Fraction
import json
import math
import numpy as np
from pde import observable_closure as c

results = {}
one = c.constant(1)
h1 = c.add(one, c.scale(Fraction(1, 2), c.unary('sin', c.seed('g1'))))
h2 = c.add(c.scale(2, h1), c.scale(Fraction(1, 3), c.unary('sin', c.seed('g2'))))
z1, z2 = c.action(h1), c.action(h2)
d = c.unary('sin', c.add(z1, c.scale(Fraction(1, 2), z2)))
reverse = c.action(d)
p = c.GaussianProgram(c.QuadratureLimits(order=15, max_innovation_dimension=4)).compile([reverse])
s = (1 - math.exp(-2)) / 2
C11, C12, C22 = 1 + s / 4, 2 + s / 2, 4 + s + s / 9
alpha = math.exp(-(C11 + C12 + C22 / 4) / 2)
co = dict((word, value) for word, value in p.sources[reverse].response)
assert abs(p.diagnostics[0]['variance'] - C11) < 2e-9
assert abs(p.diagnostics[1]['covariance'][0] - C12) < 2e-9
assert abs(co[h1] - alpha) < 2e-9
assert abs(co[h2] - alpha / 2) < 2e-9
lhs = p.carriers[1].weights @ (p.evaluate(h1) * p.evaluate(reverse))
rhs = p.carriers[2].weights @ (p.evaluate(z1) * p.evaluate(d))
truth = alpha * (C11 + C12 / 2)
assert max(abs(lhs - truth), abs(rhs - truth)) < 2e-9
results['correlated_noncentered'] = dict(gram=[[C11, C12], [C12, C22]],
    response=alpha, left=float(lhs), right=float(rhs), truth=truth,
    max_error=float(max(abs(lhs - truth), abs(rhs - truth))))

# Different formal names coincide on a singular Gaussian support. The
# derivatives must remain (2,-1), and only their response contraction cancels.
z = c.action(one)
twice = c.action(c.scale(2, one))
zero_gate = c.unary('sin', c.add(c.scale(2, z), c.scale(-1, twice)))
zero_reverse = c.action(zero_gate)
q = c.GaussianProgram(c.QuadratureLimits(order=5, max_innovation_dimension=4)).compile([zero_reverse])
value, deriv = q.evaluate(zero_gate, derivative=True)
assert np.max(np.abs(value)) < 1e-10
np.testing.assert_allclose(deriv, np.tile([2., -1.], (len(value), 1)), atol=1e-10, rtol=0)
assert np.max(np.abs(q.evaluate(zero_reverse))) < 1e-10
results['singular_formal_coordinates'] = dict(derivative=deriv[0].tolist(),
    response=[v for _, v in q.sources[zero_reverse].response],
    output_max=float(np.max(np.abs(q.evaluate(zero_reverse)))))

# A finite weighted carrier gives an independently assembled operator
# representation. This does not initialize or evolve a neural network.
p1 = np.array([.2, .3, .5])
p2 = np.array([.4, .6])
raw1 = np.array([[1., 1., -.3], [1., 1., .5], [1., 1., .9]])
raw2 = np.array([[1., -.7], [1., .8]])
b1, _, G1 = c.ridge_features(raw1, p1, 3)
b2, _, G2 = c.ridge_features(raw2, p2, 3)
D = np.array([[.5, -.2, .1], [-.1, .3, -.4]])
state = c.State(c.Population1(b1, [[.2, .4], [-.7, .1], [.6, -.8]],
    [[.3, .2], [-.6, .4], [.1, -.5]], p1),
    c.Population2(b2, [.3, -.2], p2), D + .07, D,
    {'format': 'C-H2-quadrature-v1'})
data = c.DataLaw([[1., 0.], [.6, .8]], [1., -.4], [.35, .65])
v = c.rhs(state, data)
field = c.fields(state, data.inputs)
U1 = np.sqrt(p1)[:, None] * b1
U2 = np.sqrt(p2)[:, None] * b2
Q1, Q2 = U1 @ U1.T, U2 @ U2.T
H = np.sqrt(p1)[:, None] * field['h1']
Delta = np.sqrt(p2)[:, None] * field['delta2']
F = -2 * (Delta * (data.probabilities * (field['f'] - data.labels))) @ H.T
actual = U2 @ v.M @ U1.T
expected = Q2 @ F @ Q1
rank_error = np.max(np.abs(actual - expected))
assert rank_error < 3e-13
assert np.linalg.norm(Q1 @ Q1 - Q1) > .01
step = 2e-6
plus, minus = state.copy(), state.copy()
for sign, changed in [(1, plus), (-1, minus)]:
    changed.first.w += sign * step * v.w
    changed.second.c += sign * step * v.c
    changed.M += sign * step * v.M
derivative = (c.loss(plus, data) - c.loss(minus, data)) / (2 * step)
energy_error = abs(derivative + c.velocity_squared_norm(state, v))
assert energy_error < 3e-10
results['positive_filters_and_metric'] = dict(rank_error=float(rank_error),
    energy_error=float(energy_error), nonprojection_defect=float(np.linalg.norm(Q1 @ Q1 - Q1)))

last = ([], [])
for order in range(1, 151):
    first, second, _ = c.initial_dictionary(order)
    assert first[:len(last[0])] == last[0]
    assert second[:len(last[1])] == last[1]
    assert len(first) + len(second) <= order + 15
    last = first, second
results['finite_prefix_structure'] = dict(max_order=150, feature_counts=[len(x) for x in last])
print(json.dumps(results, indent=2))
