
## General finite jets and typed preactivation curvature

`finite_jets.finite_flow_jets` extends the supplied-state calculation to any
fixed finite depth and batch, through ordinary order five. It uses the same
`Parameters` storage, input factor `1/sqrt(d)`, output factor `1/n`, full mean
squared loss and block mobilities `(n*k1,k2,...,kL,n*kout)` as `finite_network`.
All parameter blocks, residuals and reused transposes move. It draws no
initialization and computes no time trajectory.

```python
import numpy as np
from pde.finite_network import Parameters
from pde.finite_jets import (
    finite_flow_jets, hidden_gram_jet, preactivation_hessians,
    preactivation_hessian_words,
)

state = Parameters((np.array([[0.2], [-0.3]]), np.eye(2)/3),
                   np.array([0.4, -0.1]))
def polynomial_derivative(j, z):
    if j == 0:
        return z + z*z/5
    if j == 1:
        return 1 + 2*z/5
    return np.full_like(z, 2/5 if j == 2 else 0)

activations = (polynomial_derivative,)*2
inputs = np.array([[1.0, -0.5]])
jet = finite_flow_jets(state, inputs, [1.0, -1.0], activations,
                       order=4, kappas=[1.0, 0.7, 1.0])
gram = hidden_gram_jet(jet, 2, kind="activation")
assert jet.clock == "physical_full_mean_loss"
assert gram.shape == (5, 2, 2)
curvature = preactivation_hessians(state, inputs, activations)
words = preactivation_hessian_words([2, 2], affine_flags=[False, False])
assert curvature.hessians[0].shape == (2, 2, 2)
assert len(words) == 2
```

For requested order `q`, each layer callback supplies derivatives `0..q` at
that layer's initial preactivation; for `q=0`, only values are needed.
Consistency with a componentwise `C^(q+1)` activation near the supplied state
is the caller's obligation. Each callback receives a private array and its
returned buffer is copied. Parameters, data, and returned arrays are owned
independently. Nonfinite outputs are rejected; roundoff, underflow and
intermediate overflow limit float64 evaluation.

`FiniteFlowJet` holds parameter coefficients `0..q`, one preactivation and
activation array of shape `(q+1,n,m)` per layer, output coefficients of shape
`(q+1,m)`, and backward coefficients `0..q-1` of shape `(q,n,m)` per layer.
Coefficients are derivatives divided by factorials. The backward arrays have
an empty degree axis at order zero. `hidden_gram_jet` uses a one-based layer
index and explicitly selected `activation` or `preactivation`, and returns
ordinary coefficients of the same-layer matrix `X.T@X/n`.

The curvature evaluator instead returns `n*Hess_(z_l) f` while all downstream
weights and the readout are held fixed. Its local source is
`diag(phi''(z_l)*incoming_backprop)`. The returned backward vectors have
shape `(n,m)` and Hessian/source arrays have shape `(m,n,n)`. It is not the
full parameter Hessian or a material derivative. `preactivation_hessian_words`
allows unequal supplied hidden widths; every factor carries its role, layer,
and matrix shape. An identically affine source may be removed, but its slope
factors in other source terms remain. The numeric evaluator uses the existing
common-width `Parameters` contract and derivatives zero through two.

These bounded computations have polynomial arithmetic cost in the supplied
finite sizes and requested order. Dense Hessians require quadratic storage
in width and dense matrix products. No population covariance, analytic time
series, or fitting claim is inferred from finite coefficients. Deterministic
tests compare raw gradient blocks and second variations, a closed shallow
identity series, the existing two-layer oracle, independently differentiated
downstream polynomials, typed word evaluation, and callback ownership.

## Exact Gaussian forests, polynomial heads and certificates

The additional operations in `exact_calculus` implement the contained
finite-contraction proofs in the Gaussian-calculus chapter. Rational scalar
inputs use Python `int` or `Fraction`; boolean and floating inputs are rejected.
Count inputs use Python integers. The operations neither draw samples nor
load coefficients, run training, retain caches, mutate inputs, or write files.

```python
from fractions import Fraction
from pde.exact_calculus import (
    GaussianForest, forest_expectation, quadratic_forest_derivatives,
    quadratic_euler_pullback, gradient_tree_terms, identity_shallow_step,
    next_hankel_threshold, bernstein_coefficients,
)

root = GaussianForest(((1, 1), (2, 2), (2, 2)), ((0, 1), (0, 2)))
derivatives = quadratic_forest_derivatives(root, 1)
first = sum(weight*forest_expectation(tree)
            for tree, weight in derivatives[1].items())
assert first > 0
pullback = quadratic_euler_pullback(root, Fraction(1, 100), loss=True, label=1)
assert sum(weight for weight, _ in gradient_tree_terms(3).values()) == 6
assert identity_shallow_step(0, 2, 0, 1, 1, Fraction(1, 10)) == (
    Fraction(2, 5), Fraction(52, 25), Fraction(0))
assert next_hankel_threshold([[1, 0], [0, 0]], [2, 0]) == 4
assert bernstein_coefficients([-1, 0, 1], 0, 1) == (-1, -1, 0)
```

`GaussianForest` owns canonical immutable row/column colors `(population,
nonnegative_integer_power)` and simple bipartite acyclic edges, including
isolated vertices and the empty forest. `forest_expectation` returns its exact
normalized Gaussian expectation at a supplied positive `width`, or its
leading value when width is omitted. Normalization is `n^(-edges/2-components)`;
row, column and edge arrays are independent standard Gaussians. Finite-width
evaluation sums all equality partitions. Leading evaluation uses paired
quotient trees, with no binary-rank or zero-prefix pruning.

`quadratic_forest_derivatives` returns a tuple of newly owned forest
polynomials, starting with order zero. It requires even column decorations,
raw square activation, one input, two hidden layers, and feature-ascent
mobilities `(n*alpha,beta,n)` for nonnegative rational `alpha,beta`.
`quadratic_euler_pullback` uses raw squares and unit block multipliers. Its
signed rational step gives one simultaneous feature update, or a full squared
loss update with `loss=True` and an explicit rational label. It retains the
moving residual in that update. Normalized squares with a different activation
constant require the separately stated scaling in the proof.

`gradient_tree_terms(k)` returns canonical parameter-contraction trees with
integer weights and typed-by-edges vertex indices; the weights sum to `k!`.
This constant-metric differentiation compiler is distinct from Gaussian
neuron forests. `identity_shallow_step` gives the exact scalar closure for
one-input shallow identity, full squared loss and equal block mobilities
`n*mobility`, from any feasible supplied `(f,q,d)`.

`gaussian_hidden_head(covariance,responses,activation)` evaluates the explicit
local fourth-order Bell/product graph using an ordinary rational polynomial
activation. Coordinates are `(Z,U1,U2,U3,U4,V0,V1,V2,V3)`. Supply the complete
rational positive semidefinite covariance, `Var(Z)=1`, independent first-five
and last-four blocks, and exactly the response keys `lambda1`, `lambda2`,
`lambda30`, `lambda32`, `lambda41`, `lambda43`, `c10`, `d21`, `d30`, `d32`.
Singular blocks are valid. The returned exact scalars are `gamma`, `A41`,
`A43`, `gram13`, `gram22`, and `squared_rms_fourth`. The last is the fourth
**derivative**, `2*gamma+8*gram13+6*gram22`. Response partials hold every other
coordinate and supplied constant fixed before expectation. The implementation
forms activation derivatives zero through four and expands polynomials;
it offers no nonpolynomial-integral or formal-symbolic mode and supplies no
neural interpretation of input covariances.

`next_hankel_threshold` validates rational positive semidefinite `A`, including
a singular range condition for `b`, and returns the exact lower bound on the
new diagonal entry. `bernstein_coefficients` supports an explicit degree at
least the supplied polynomial degree and exact interval endpoints. Signs
certify that supplied polynomial only. Forest enumeration, polynomial heads,
canonicalization, and Wick recursions may have rapidly growing cost; no
large-order efficiency guarantee is made. Python recursion limits and rational
bit growth still apply. Tests use unrestricted finite index sums, raw updates,
independent polynomial contractions, exact Gaussian quadrature, singular
matrix examples, and rational polynomial identities.
