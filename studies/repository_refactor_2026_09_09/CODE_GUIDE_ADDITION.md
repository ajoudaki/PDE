## Moving physical-flow jets

`from pde.finite_jets import flow_jet` supplies a bounded derivative oracle
for exactly two hidden layers and one sample. It takes an existing finite
`Parameters` state, `(d,1)` inputs, one label, positive block multipliers,
and one shared C3 activation's derivative callback. It supports ordinary
Taylor coefficients through order three, at any supplied state. No Gaussian
initialization or population replacement is performed.

```python
import numpy as np
from pde import Parameters
from pde.finite_jets import flow_jet

theta = Parameters(([[0.2]], [[0.3]]), [0.4])
def derivative(j, z):
    return (0.4 + np.sin(z), np.cos(z), -np.sin(z), -np.cos(z))[j]

jet = flow_jet(theta, [[1.0]], [1.0], derivative, order=3)
print(jet.output_coefficients[:, 0])  # f^(k)(0)/k!
print(jet.output_derivatives[:, 0])   # physical-time derivatives
```

Every weight block, the reused transpose, and the residual move in this
recurrence. Its coefficients are not obtained by evaluating along the straight
line defined by the initial gradient, or by multiplying feature-time derivatives
by powers of an initial residual clock. The calculus chapter gives the complete
recurrence and physical-clock chain rule.

`parameter_coefficients[k]` uses the existing raw storage. Each of the two
`preactivation_coefficients` and `hidden_coefficients` arrays has shape
`(order+1,n,1)`; tuple positions zero and one denote hidden layers one and two.
`output_coefficients` and its factorial conversion have shape `(order+1,1)`.
Only derivative orders zero through the requested order are evaluated, at
initial preactivations. The unused terminal backward derivative is not computed.
Order zero evaluates only the predictor, after validating the arguments.

The callback receives a private array and must return the true coordinatewise
derivative of the same scalar activation, with the same shape and real finite
values. Its result is copied immediately. In-place callbacks and reusable
buffers are supported; semantic consistency and C3 regularity are caller
obligations. Returned arrays are mutable but do not alias the user's inputs.
The existing numerical range contract applies. In particular this is float64
evaluation of an exact real-arithmetic recurrence, not exact arithmetic or a
certified rounding bound. Nonfinite evaluated coefficients and nonrepresentable
requested derivative conversions are rejected. Intermediate products may still
overflow or underflow. For degree at most three, work and storage are
`O(n*d+n²)`, apart from callback costs.

Tests include hand-solvable linear, cubic and constant-activation flows;
independent derivative checks against the existing physical RHS; neuron
relabeling; callback ownership; zero residual/input; degree prefixes; and
selected numerical-range failures. These are finite deterministic checks,
not an infinite-width identification or positive-time Taylor error theorem.

## Forest keys and exact finite certificates

Import `forest_key`, `revert_series`, `determinant`, and
`quadratic_axis_certificate` from `pde.exact_calculus`. These operations draw
no random numbers and write no files.

`forest_key(colors, edges)` accepts a finite simple bipartite forest. A vertex
color is `(layer, decoration)`, where the layer is one or two and the decoration
is a nonnegative integer. Edges join vertices from different layers. The
immutable result preserves colors and component multiplicities while ignoring
vertex numbering, edge orientation and edge ordering. Duplicates, cycles and
invalid indices are rejected. The calculus chapter proves the key's exact
isomorphism property and, separately, the leading Gaussian expectation
factorization that motivates component reuse. The key itself is not a general
coefficient compiler. Its transparent all-roots recursion is intended for small
forests and is subject to Python's recursion limit.

`revert_series(a)` accepts ordinary coefficients of a truncated series with
zero constant and nonzero linear term. It returns the equally truncated inverse
under composition, using only coefficient matching. `determinant(M)` computes
the exact rational determinant of a square matrix, with the empty determinant
equal to one. Their inputs are finite lists or tuples of Python integers or
`fractions.Fraction`; floats and booleans are rejected. Neither mutates its
input. Reversion uses at most `O(N⁴)` rational operations in this transparent
implementation, and elimination uses `O(N³)`. Rational bit sizes can grow.

The fixed certificate can be regenerated from the repository root by:

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 python -B -c 'from pde.exact_calculus import quadratic_axis_certificate; c = quadratic_axis_certificate(); print(c["shifted_determinant"]); print(c["witness_value"])'
```

It prints the two negative rational quantities proved in the calculus chapter.
The function independently regenerates the order-thirteen jet, six coefficients,
and polynomial witness; it does not load historical arrays. The returned fresh
dictionary also contains the derivative list, inverse series and kernel series.
The standard established test command checks every displayed fraction, both
directions of series reversion, and a separate permutation determinant and
polynomial quadratic-form calculation.

The certificate concerns the quadratic network with order-one stored readout,
feature ascent and zero first-block mobility, all explicitly specified in the
proof. It rejects a moment representation demanded uniformly over metrics
including that one. It does not resolve the canonical unit-metric all-order
problem, extend to strictly positive first mobility, or establish failure of
a positive-time population limit. Its initialization-jet probability proof is
separate from verification of its exact arithmetic. No training experiment,
historical campaign output, or empirical figure is incorporated by these tests.
