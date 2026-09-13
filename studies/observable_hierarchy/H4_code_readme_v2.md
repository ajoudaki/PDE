# Finite dynamics, moving jets and exact calculus

This NumPy-only package implements the finite equal-width network in
[the notation contract](../docs/NOTATION.md) and
[the finite-dynamics chapter](../docs/finite_dynamics.md).
It supports any positive number of hidden layers and any nonempty fixed batch.
It is a finite reference implementation; numerical tests do not establish an
infinite-width limit. Separate small modules provide exact rational Gaussian
moments, a two-hidden-layer one-sample physical-flow jet through order three,
colored-forest keys, finite rational certificates and Euler pullback weights.
A separate module evaluates finite quadratic/identity and differentiated RMS
models. Their narrower contracts
are stated below; they are not a general symbolic population compiler.

## Model and normalization

Inputs `X` have shape `(d,m)` with samples in columns. `Parameters.weights`
contains `W1,...,WL`: shapes `(n,d)`, then `(n,n)` for every hidden matrix.
`Parameters.readout` has shape `(n,)`. The equations are

```text
z1 = W1 @ X / sqrt(d)
zl = Wl @ h(l-1)              for l >= 2
hl = activation_l(zl)
f  = readout @ hL / n
loss = mean((f - labels)**2)
```

There is no additional `1/sqrt(n)` in the hidden forward passes: hidden
weights are already stored in the scaled convention. Initialization draws
independent Gaussian first weights with variance `1`, hidden entries with
variance `1/n`, and stored readout entries with variance `1/n²`. Draw order
is first matrix, hidden matrices in layer order, then readout. Every call
requires an explicit seed and leaves the global random generator unchanged.

`X.T @ X / d` is the input Gram. Samples with unit RMS have unit Gram diagonal,
but the implementation also accepts arbitrary finite inputs, including zero,
correlated, duplicated, opposite and linearly dependent samples. It never
whitens, rescales or inverts their Gram. Unequal hidden widths are rejected.

## API

`forward` returns per-layer preactivations, hidden activations and the output.
`backward` returns the residual-free arrays
`delta_l = n * partial f / partial z_l`. `loss_gradients` returns ordinary
Euclidean/Frobenius mean-squared-loss gradients in the `Parameters` structure.

`flow_velocity` returns `-D grad(loss)`, with block mobilities
`n*kappa_1, kappa_2,...,kappa_L, n*kappa_(L+1)`. Supply `kappas` as a length
`L+1` positive vector; the default is all ones. `gd_step` adds `eta` times
that velocity to every block simultaneously using the original state. It
returns new arrays, leaving the original parameters unchanged. It is an exact
GD update, not an exact finite-time flow solution; an arbitrary GD step need
not decrease the loss. No clipping or transformed-coordinate Euler step is used.

`kernel_blocks` returns shape `(L+1,m,m)`, and `kernel` sums those blocks.
Neither includes the residual or the loss factor `2/m`. Along the flow,

```text
f_dot    = -(2/m) * K @ (f-y)
loss_dot = -(4/m²) * (f-y).T @ K @ (f-y)
         = -sum_blocks ||velocity_block||² / mobility_block
```

Activations may be a single `Activation` or one per hidden layer. `TANH`
(default), `ARCTAN` and `IDENTITY` are provided. A custom
`Activation(name, value, derivative)` must return real, finite arrays with
the same shape as its input. It must apply a scalar function coordinatewise,
and supply that function's actual derivative, consistently across calls;
C2 regularity is the caller's responsibility.
Finite shapes, numeric values, block multipliers and step sizes are checked.
Parameters accept array-like input and store float64 arrays; those arrays
remain mutable and may share memory with arrays passed to the constructor.
They are revalidated before evaluation.

Each activation callback receives a private input copy, and its returned array
is copied before reuse. In-place callbacks and reusable output buffers are
supported; callbacks must not mutate unrelated external state used by the
calculation. Built-in derivatives avoid cancellation in saturated tanh and
premature overflow in arctangent. Loss evaluation uses a scaled mean square.
Unrepresentable losses and total kernels raise `ValueError`. This is still
float64 arithmetic: it does not promise correct rounding or immunity from
intermediate overflow or underflow in arbitrary matrix products.
Scalar/elementwise mobility and kernel factors are combined in mantissa/exponent
form before restoring their magnitude. GD likewise combines the step with the
gradient directly; it need not construct a representable unscaled velocity.
Flow and GD use raw derivative contractions, without requiring a separately
representable normalized `loss_gradients` result. Gram normalization is likewise
combined with the block multipliers. First-layer input normalization follows
the raw matrix product. The raw contractions themselves remain float64 operations.
A zero step validates parameter and argument structure and returns independent
copies without evaluating unused activation callbacks.

## Example

Run Python with `code/` on its import path:

```python
import numpy as np
from pde import ARCTAN, forward, gd_step, initialize, kernel, loss

X = np.sqrt(2.0) * np.array([[1.0, 0.6, -1.0], [0.0, 0.8, 0.0]])
y = np.array([1.0, -0.5, -1.0])
theta = initialize(width=8, depth=3, input_dimension=2, seed=42)
print(forward(theta, X, ARCTAN).output)
print(kernel(theta, X, ARCTAN))
next_theta = gd_step(theta, X, y, eta=0.01, activation=ARCTAN)
print(loss(theta, X, y, ARCTAN), loss(next_theta, X, y, ARCTAN))
```

The library and example write no files. Matrix storage grows as
`n*d + (L-1)*n² + n`; forward/backward states use `O(L*n*m)` memory, and the
kernel blocks additionally use `O((L+1)*m²)`.

## Tests

From the repository root, using Python 3.10+ and NumPy:

```sh
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_*.py' -v
```

The tests use depths 1, 2 and 3, general finite states and tiny seeded
initializations, correlated/opposite/conflicting labels, and layer-dependent
activations. Every raw parameter block is checked against coordinate finite
differences of the loss; independent output-Jacobian differences verify each
kernel block. Directional differences check flow dissipation, and a hand
calculation checks simultaneous GD. Shape/domain validation, batch invariance,
zero residuals, initialization scaling and input normalization are covered.
The suite uses NumPy and Python's standard `unittest` only, with no experiments
or generated-data dependencies.

## Exact Gaussian moments

`gaussian_moment(covariance, powers)` returns a `fractions.Fraction` equal to
`E[prod_i X_i**powers[i]]` for a centered Gaussian vector. Covariance must be
a nonempty, square, symmetric positive-semidefinite matrix with integer or
`Fraction` entries. Powers must be nonnegative integers of matching length.
Use finite lists or tuples; floats and booleans are rejected. Singular and
zero covariance are accepted. No rounding or PSD tolerance is used.

```python
from fractions import Fraction
from pde import gaussian_moment

sigma = [[2, Fraction(1, 3)], [Fraction(1, 3), 3]]
assert gaussian_moment(sigma, [2, 2]) == Fraction(56, 9)
assert gaussian_moment([[1, 1], [1, 1]], [2, 2]) == 3
```

Validation uses exact rational Schur complements. A positive pivot reduces
to its Schur complement; a zero pivot requires a zero corresponding row.
The moment recurrence removes one leg, pairs it with each remaining coordinate
with its multiplicity and covariance factor, and recurses. Odd total degree
returns zero; all zero powers return one, after validation. Its cache is local
to a call and is cleared on return, including when evaluation raises.

Validation costs `O(d³)` rational operations. The recurrence visits at most
`prod_i(powers[i]+1)` exponent states, with `O(d)` transitions per state and
depth at most `1 + sum(powers)/2`. Both state count and rational bit sizes can
grow rapidly; this API is intended for small exact moments. It performs no
numerical quadrature and claims no population-limit theorem. The module uses
only the standard library; the public `pde` package also imports the NumPy
finite-network API.

Moment tests check known uni-/bi-/trivariate formulas, negative correlations,
independent coordinates, singular/zero covariances, exact near-boundary PSD
rejection, input types/shapes/degrees, and absence of input mutation or shared
cross-call caches.

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
problem or establish failure of a positive-time population limit. Section 10
separately proves persistence of its witness for some strictly positive first
mobilities, by an explicit forest argument and continuity; this API does not
calculate that interval or positive-metric jets. Its initialization-jet proof is
separate from verification of its exact arithmetic. No training experiment,
historical campaign output, or empirical figure is incorporated by these tests.

## Finite quadratic and RMS reductions

`pde.finite_reductions` evaluates three small, exactly specified finite
models from Sections 5–7 of the finite-dynamics chapter. All calls require
the existing `Parameters` structure with two hidden layers and input
dimension one. The datum is fixed to `x=1`; `label` is a finite real scalar.
The first and readout mobilities are `n`, and the middle mobility is one.
These APIs evaluate a state; they do not integrate a trajectory.

```python
from pde import Parameters
from pde.finite_reductions import mixed_lax, mixed_quadratic, rms_quadratic

theta = Parameters(([[0.5], [1.0]], [[0.2, -0.1], [0.3, 0.4]]), [0.5, -0.2])
mixed = mixed_quadratic(theta, 1.0, model="QI")
lax = mixed_lax(theta, model="QI")
normalized = rms_quadratic(theta, 1.0, epsilon=0.2)
print(mixed.kernel_blocks, normalized.kernel_blocks)
```

`mixed_quadratic` accepts `QI`, `IQ` or `QQ`, naming the first and second
activations in order: `Q(z)=z²`, `I(z)=z`. Its default is `QQ`.
`rms_quadratic` squares and then normalizes each hidden vector by
`sqrt(mean(squared_vector**2)+epsilon)`, with required `epsilon>0`.
Both normalization denominators are differentiated. This widthwise operation
is a separate architecture and cannot be supplied as a scalar `Activation`.
No initialization distribution or readout scaling is imposed by either call.

Both return a `ReductionEvaluation` with `output`, `residual`, `loss`,
`kernel`, and `kernel_blocks` in first/middle/readout order. The three blocks
exclude residual and loss factors. `ascent` is the output metric gradient,
and `velocity` is the physical mean-square-loss velocity `-2*residual*ascent`;
both use raw `Parameters` storage. `output_velocity=-2*residual*kernel` and
`loss_velocity=-4*residual**2*kernel` use that same physical clock.

`fields` contains the current hidden and backward vectors. For mixed models,
its keys are `h,z,v,b,q`, with `h` the first feature, `z` the second
preactivation, `v` the second feature, `b=a` for `QI` and `b=a*z` otherwise,
and `q=B.T@b`; here `B` is the stored middle matrix and `a` the stored
readout. The RMS result additionally includes `p=u²`, `alpha`, `w=z²`,
`beta`, `c=a-output*v`, and `q_tilde=q-h*(h@q/n)`, with `b=2*z*c/beta`.
All vector fields have shape `(n,)`. `field_ascent` gives derivatives of
`h,z,v` in the mixed models, and `p,alpha,h,z,w,beta,v` in the RMS model,
in unit feature ascent. Scalars `alpha,beta` and their derivatives are floats.

For `QQ` and RMS, `row_balance_ascent` and `column_balance_ascent` return
the unit-ascent derivatives of `n*sum_j(B_ij²)-2*a_i²` and
`n*sum_i(B_ij²)-u_j²/2`. Both vanish for `QQ`. RMS has the signed drifts
derived in the chapter; its row drift generally persists at zero
regularization where the denominators are nonzero. The API itself requires
positive regularization. Multiply these returned derivatives by `-2*residual`
for the physical clock. They are `None` for `QI` and `IQ`.

`mixed_lax` accepts only `QI` or `IQ` and returns the ordinary Euclidean
isometric block `factor`, `factor_ascent`, `gram`, `signature`, `operator`,
`generator`, and `ascent`. The operator is `signature @ gram`; its
unit-ascent derivative is the commutator with `generator`. For `IQ` the
generator already includes the factor two. These matrices retain neuron
orientation and have size `n+1`; the API does not evolve spectra alone.

All returned arrays are fresh float64 arrays and inputs are unchanged.
The dataclass fields are fixed, but contained arrays and dictionaries are
mutable. The evaluators reject nonfinite evaluated fields, kernels and
velocities, including unrepresentable required intermediates. Arithmetic
here uses ordinary float64 operations; it has no certified rounding bound
or universal extreme-range guarantee. Underflow can occur. It does not
inherit the core network's specialized scaled-product treatment.
The two state evaluators use `O(n²)` work and storage; the explicit dense
Lax products use `O(n³)` work and `O(n²)` storage.

Tests compare the mixed models with the independent layerwise core,
differentiate every RMS parameter block from the output definition, and
check kernel blocks, feature derivatives, physical energy, the Lax chain
rule, an orientation witness, balance drifts, zero coordinates, sign
invariance and array ownership. No training run or generated dataset is used.

## Exact Euler pullback words

`pde.exact_calculus` also supplies the finite operator weights proved in
Section 9 of the Gaussian/flow-calculus chapter:

```python
from fractions import Fraction
from pde.exact_calculus import euler_pullback_words, paired_euler_weights

assert euler_pullback_words(2, 2) == {(2,): Fraction(2), (1, 1): Fraction(1)}
assert paired_euler_weights(2) == ((Fraction(0), Fraction(-2)),
                                   (Fraction(0), Fraction(1)))
```

`euler_pullback_words(order, steps)` maps each positive composition
`(k1,...,kq)` of the requested degree to `Fraction(binomial(steps,q))`,
omitting zero weights. The tuple denotes `T_k1 ... T_kq` acting from right
to left, where `T_k u = D^k u[v,...,v]/k!`. An outer operator differentiates
the state-dependent vector field in each inner expression. Degree zero
returns the identity word `{(): Fraction(1)}`; positive degree with zero
steps returns `{}`.

`paired_euler_weights(order)` returns `order` immutable rational rows.
Row `q-1` gives the coefficients in increasing powers of the update count
`N` of `binomial(2*N,q)-2**order*binomial(N,q)`. Every row has length
`order`, since its possible highest-degree term cancels. Degree zero
returns `()` and degree one returns `((Fraction(0),),)`.

Inputs must be nonnegative Python integers; booleans, floats and `Fraction`
inputs are rejected. The operations evaluate neither derivatives nor neural
moments. Their output is combinatorial, with no state, data or history input.
Word enumeration uses at most `O(j*2**j)` work and storage at degree `j`;
paired weights use `O(j²)` rational operations and storage. Integer bit
lengths can grow. These are finite exact primitives, with no cache, files
or random sampling. The tests independently enumerate update slots and
compare the assembled differential words with direct nonlinear scalar
Euler composition through degree six.

Fixed-order coefficients alone supply no bound uniform in update count,
no positive-time Taylor convergence and no neural width limit. The chapter
separately proves a finite-dimensional comparison bound under explicit
convex-region hypotheses containing every required intermediate state.

## Frozen-bottom quadratic step

The separate frozen-bottom model in Section 8 of the finite-dynamics chapter
holds the first feature vector `h` fixed and trains only the connector and
stored readout, with mobilities one and `n`. Its top activation is
`z**2/sqrt(3)` and its loss is **half** the squared residual. The two functions
below take the current readout `a`, preactivation `z=B@h`, and fixed second
moment `Q=h@h/n`. No initialization or first-layer update occurs.

```python
from pde.finite_reductions import frozen_quadratic, frozen_quadratic_step

a, z, Q = [0.3, -0.8], [0.4, -0.2], 0.7
state = frozen_quadratic(a, z, Q, label=1.0)
next_a, next_z = frozen_quadratic_step(a, z, Q, eta=0.01, label=1.0)
assert len(next_a) == len(next_z) == 2
assert state.loss == 0.5 * state.residual**2
```

`FrozenQuadraticEvaluation` contains `output`, `residual`, `loss`, the two
`kernel_blocks` in connector/readout order, `output_velocity`, `loss_velocity`,
`readout_velocity`, and `preactivation_velocity`. With `K=sum(kernel_blocks)`,
the half-loss convention gives `output_velocity=-residual*K` and
`loss_velocity=-residual**2*K`. Both increments in `frozen_quadratic_step`
use the old state and the same physical step `eta`; these are exactly the
coordinates induced by simultaneous raw connector/readout GD.

Vectors must be nonempty, finite real numeric vectors of the same length.
`Q` is nonnegative, with `Q=0` requiring `z=0`. Every `Q>0` permits every
finite `z` through a suitable raw connector. `label` is a finite real scalar;
`eta` is finite and nonnegative. Booleans are rejected. Defaults use label one.
All returned arrays are fresh; calls take `O(n)` work and storage. Both
evaluated quantities (including the kernel) and updated coordinates must be
representable in ordinary float64. Underflow and rounding remain possible.

The code supplies a state evaluator and one update, without a step-size
stability guarantee or a population solver. The chapter's initial-layer
theorem separately requires its stated frozen Gaussian initialization and
joint vanishing-step limit. The four tests differentiate the raw unreduced
loss and output, verify both kernel blocks and the half-loss energy identity,
compare the simultaneous raw update and interpolation, and check degenerate
states, input validation and ownership. No training experiment is used.


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

## Certified fixed-model test-risk comparison

The opt-in [two-layer risk certificate tool](tools/two_layer_risk/README.md)
supports the computer-assisted sign proof in
[global-nonlinear C.5](../docs/global_nonlinear.md). It certifies one fixed
coefficient for exactly two tanh hidden layers, the canonical Gaussian
initialization and mobilities, three correlated training inputs, and the
uniform-circle teacher `cos(3 alpha)`. It includes the training-loss clock
subtraction. It is not a training solver or a general-purpose quadrature API.

From the repository root, on the supported arithmetic platform, choose an
output directory that does not already exist:

```sh
python -B code/tools/two_layer_risk/certificate.py --target 26 --output data/established/two_layer_risk_01
```

The tool regenerates every Gaussian-rule input and enclosure, compiles its
private C++ kernel, and saves exact rational bounds and execution provenance.
It requires Python 3.10+, NumPy and the C++17/IEEE arithmetic contract in
its guide; ordinary package imports do not require a compiler. The guide
also supplies an API example and independent exact-arithmetic and supplied-rule
checks. No archived arrays, study files or Git metadata are runtime inputs.

The theorem proves a small strictly positive risk improvement at equal
training loss on a width-independent initial interval. It does not evaluate
that interval numerically, supply a width rate, or assert a universal or
later-time benefit. The complete analytic error proof and finite calculation
are both necessary for the sign; a floating positive estimate is insufficient.

## Finite autonomous observable population closure

`pde.observable_closure` exposes the finite population/action construction in
[Global nonlinear learning, C.4.7.9](../docs/global_nonlinear.md#c479-finite-autonomous-observable-closure).
Its exact-real population theorem is qualitative. This module is a minimal
float64 quadrature prototype, with a finite weighted data-law API and static
checks; it provides no trajectory solver or certified numerical accuracy.

The model is bias-free two-hidden-layer tanh, with normalized directions
`u=x/sqrt(2)`, stored Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`,
residual `f-y`, and physical unhalved mean-square loss. Population `c=0` is the
limit of the actual random finite readout. No finite network is constructed.

`State` retains two joint quadrature populations: `(b,g,w)` with two-dimensional
`g,w`, and `(b,c)` with scalar readout `c`. Its `M` and fixed `D` are matrices
indexed by initialized observable features. All node probabilities and frozen
marks are saved. The moving `w,c` values are unrestricted characteristic values
at quadrature nodes, not expansions in the features. Arrays are copied by state
constructors; they remain mutable for supplied-state work and are revalidated
on evaluation. Changing a frozen mark changes the model.

`initialize(order, limits)` builds the explicit word prefix and fixed two-orientation
pilot, retaining duplicate bounded dictionary outputs. It computes uncentered
Gaussian input Grams and every earlier opposite-source response coefficient,
with derivatives in frozen named Gaussian coordinates. Both forward and reverse
calls reuse that joint source program. It compiles the raw forward contractions
before extracting either population, then uses the prescribed ridge `2**(-N)`.
The returned `GaussianProgram` and fixed diagnostic metadata expose this producer.
The operational RHS never calls it.

`fields(state, inputs)` returns `h1,a,z2,h2,delta2,d,q,f` for a nonempty `(m,2)`
direction array. `DataLaw` takes a nonempty `(m,2)` array of unit directions,
finite labels, and nonnegative probabilities summing to one. This discrete data
API does not cover all nonatomic laws of the exact theorem. `loss` and `rhs` use
those probabilities; `rhs` returns the moving `w,c,M` velocities. The only action
is the finite feature contraction

```text
b2 @ M @ (b1.T @ (probability1[:,None] * values)).
```

Its reverse uses the same `M.T` and the other population weights.
`apply_action` accepts values on the declared retained quadrature population;
it is a finite contraction, not an arbitrary Gaussian-action oracle.
`observe` evaluates finite typed words with `g1,g2,w1,w2,c`, rational scalings,
addition, bounded products, `sin,cos,tanh` and both action orientations.
`frozen_z20(v)` uses `D` and frozen `g`. `joint_observe` returns a same-population
coordinate matrix with its probabilities, preserving current/frozen correlations.
This rational-mark API is a subset of the real-mark mathematical observation
language. Evaluating a fixed finite input batch does not certify a circle supremum.

`save_restart` and `load_restart` preserve the entire current state, fixed data
law and an optional metadata dictionary with string keys and JSON-serializable
values, without time or history. The writer
sets the reserved `format` tag automatically, without mutating caller metadata;
a supplied `State` with the default empty metadata round-trips without an
initializer or private tag. Other metadata fields are preserved. Archives use no pickle.
`algebraic_update` makes one simultaneous `state + step*velocity` map on `w,c,M`;
it is not an exact flow solution or a guarantee of loss decrease.

From the repository root with `PYTHONPATH=code`:

```python
from pde import observable_closure as closure

state, initialization_program = closure.initialize(
    1, closure.QuadratureLimits(order=5, max_nodes=100000)
)
data = closure.DataLaw([[1., 0.], [0., 1.]], [1., -1.], [0.5, 0.5])
velocity = closure.rhs(state, data)
values = closure.fields(state, data.inputs)
paired, probabilities = closure.joint_observe(
    state,
    [closure.frozen_z20((1., 0.)),
     closure.action(closure.unary("tanh", closure.seed("w1")))],
)
assert values["f"].shape == (2,)
assert paired.shape[1] == 2
```

The initializer uses deterministic tensor Gauss–Hermite quadrature. Defaults are
order 5, at most 100000 nodes per population, total independent Gaussian dimension
at most 7 (including lower `g`), at most 32 named action sources, and covariance
roundoff allowance `2e-11` times the declared local scale. The word decoder's
prefix limit is 10000. Orders above 1074 are rejected for float64 ridge underflow;
conditioning and tensor limits can stop much smaller orders. `ResourceLimit`
reports a requested allocation beyond these caps. A failed compile may leave a
partial compiler object, which must not be used as a completed initialization.

At hierarchy order 1 the defaults yield 6 and 4 features, a `4 x 6` action block,
and 625 and 3125 quadrature nodes. These are integration node counts, not widths.
The default quadrature is coarse: it approximates `E sin(g)^2` by about `0.425679`,
versus the analytic value `(1-exp(-2))/2`, about `0.432332`. The analytic source
checks use quadrature order 15. No useful accuracy is claimed for the defaults.

All positive Gaussian innovations and regularized Gram modes are retained.
Exactly zero innovation adds a named derivative coordinate without an independent
Gaussian coordinate. A slightly negative Schur complement within the explicit
allowance is set to zero and recorded in diagnostics; a larger negative value or
unresolved covariance range raises `NumericalInitializationError`. Small positive
roundoff innovations can increase tensor cost. Nonpositive regularized eigenvalues,
nonfinite results and unrepresentable ridges are rejected without mode removal or
substituted schedules. The floating square root is not an interval certificate.
Numerical `||D||` is reported, not rescaled to enforce the exact operator bound.

There is no quadrature-error certificate, extreme-range guarantee, monotonic
accuracy claim, or convergence theorem when N grows with a fixed quadrature rule.
Exact hierarchy-order convergence and approximation of any fixed order's integrals
are distinct limits. Practical conditioning, quadrature and resource certification
and a longer-time solver remain outside this module’s claims.

The deterministic checks use analytic source/Stein identities, singular sources,
named partials and forward-after-reverse reuse, ridge duplicates, actual transpose
contractions, all matrix-coordinate and selected population-coordinate finite
differences, the independent energy directional identity, paired observations,
and one algebraic update followed by bitwise-equal restart. No training run is
part of these checks. Run only this suite with:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
PYTHONPATH=code python -B code/tests/test_observable_closure.py
```

`H2_TEST_SCRATCH` selects the temporary archive directory; no retained output is
an input to these tests. `H2_PROTOTYPE_MODULE` can override the import for isolated
checks; its installed default is `pde.observable_closure`.


## Finite numerical observable closure

The solver integrates the autonomous nonlinear two-hidden-layer tanh closure
of C.4.7.10. It uses the bias-free model, Gaussian initialization, mobilities
(n,1,n), unhalved squared loss, and physical time. Population integration
points represent joint laws. The middle matrix indexes retained features;
there is no neural width argument or neuron-by-neuron middle matrix.

The library requires Python and NumPy. The optional bounded validation
supervisor additionally uses psutil on Linux. No external data, trained
surrogate, target trajectory, Gaussian-action service, or cached experiment
is needed for initialization or evolution.

### Supported laws and initialization

`ArcLaw(p,a,b,c,d)` accepts exact rational strings, integers or `Fraction`
parameters. It represents the mixture described in C.4.7.10: normalized input
U(s)=((1-s²)/(1+s²),2s/(1+s²)), labels +1 and -1, and a 3/5,4/5 rotation
for the second arc. Required ranges are 1/3<=p<=2/3 and
-1/20<=a<=b<=1/20, -1/20<=c<=d<=1/20. Degenerate intervals are atoms.
The mathematical model uses x=sqrt(2)u; all library input arrays contain u.
The proved numerical and population convergence scope is 0<=t<=1/200.
The family and this horizon are independent of every resolution parameter.

```python
from fractions import Fraction
from pde.observable_solver import (
    initialize, ArcLaw, evolve, predict, circle_inputs,
    paired_observations, save_restart, load_restart,
)

state = initialize(order=3, initialization_nodes=2048, population_nodes=1024)
data = ArcLaw().quadrature(nodes_per_arc=8, arithmetic=state.arithmetic)
final = evolve(state, data, steps=32, step_size=Fraction(1, 6400))
directions = circle_inputs(128, final.arithmetic)
prediction = predict(final, directions)
observations = paired_observations(final, data)
print(observations['rms1'], observations['rms2'])
```

`initialize` retains b1,g,w,p1 and b2,c,p2, one evolving matrix M and its
frozen initialization D, arithmetic settings and small metadata. Initially
w=g,c=0,M=D. All joint marks needed by the declared observations are retained.
It discards the Gaussian compiler and integration coefficient tables after
forming these arrays. Q=`initialization_nodes` determines coefficient/Gram
integration; P=`population_nodes` separately discretizes each full joint
mark law. It does not sample a Gaussian coordinate independently of the
other coordinates on its population.

Orders 1,3,5 have retained feature dimensions (5,3),(35,10),(128,21), with
strictly larger exact polynomial spans and new nonzero initialized action
couplings at each transition. Order 5 includes two redundant constant tail
words in addition to its 126 first-population polynomial features; the
declared syntax rule retains them. Odd degree choices avoid relying solely
on new even directions in an odd tanh trajectory. The polynomial core uses only four
and two independent Gaussian integration dimensions. Its initialized matrix
contains the reverse-to-forward response term. Higher orders also append an
exhaustive bounded-word prefix. Once that prefix introduces new actions,
initialization dispatches to the full joint Gaussian compiler; its cost may
grow substantially. Practical computation at every order is not promised.

`InitializationLimits` from `pde.observable_initialization` controls feature,
word, integration point, estimated work and estimated memory allowances.
`CompilerLimits` from `pde.observable_compiler` additionally controls generic
source-program resources. Pass an `InitializationLimits` instance through
`initialize(limits=...)`. Exceeding a limit raises an error without changing
the dictionary. Limits may be raised explicitly; they are resource controls,
not definitions of a capped hierarchy. Estimated bytes do not replace an
operating-system resource limit.

### Evolution and observations

`evolve` uses simultaneous explicit Heun updates of w,c,M and returns a fresh
state. The state has no absolute clock or growing history. Input blocks bound
temporary storage; set `block_size` on evolution, prediction and observation
calls. For a non-node time, `interpolate_state(left,right,fraction)` interpolates
the endpoints of one step on their identical frozen joint marks. This supplies
the continuous within-step convention used by the numerical theorem.

`predict(state, inputs)` evaluates any supplied circle directions directly
from the evolving nonlinear state. Its meaning is not restricted to an output
grid. A finite circle panel is a diagnostic, not a certified supremum estimate.

`paired_observations` returns `first_pairs` and `second_pairs`, each of shape
(population_nodes,input_nodes,2), with the last coordinate ordered as
(initial,current). The upper initial field is reconstructed using g and D
on the same frozen marks. The probability of a pair entry is the product
of its returned population weight and input weight. The returned `rms1,rms2`
are the square roots of the training-averaged squared paired displacements.
Use `include_pairs=False` to compute RMS values without retaining pair arrays.
`loss` and `rhs` expose the unhalved loss and complete nonlinear vector field
for diagnostics. Both directions use M and its actual transpose.

### Own-state restart

```python
from fractions import Fraction
from tempfile import TemporaryDirectory
from pathlib import Path

half = evolve(state, data, steps=16, step_size=Fraction(1, 6400))
with TemporaryDirectory() as directory:
    checkpoint = Path(directory) / 'observable_restart.json'
    save_restart(checkpoint, half, data)
    restored, restored_data = load_restart(checkpoint)
    continued = evolve(restored, restored_data,
                       steps=16, step_size=Fraction(1, 6400))
```

The JSON checkpoint contains all frozen/current joint arrays, both matrices,
the represented finite input rule and arithmetic metadata. It contains no
source program or history. Floats use hexadecimal values; Decimal values
use exact decimal strings; rational fixed-point values use hexadecimal integer
units. Loading does not redraw initialization. Continuing with identical
steps and arithmetic reproduces the working state exactly. This is own-state
restart, with convergence to the population restart proved separately.

### Precision and convergence

The default is float64. `digits=40` selects the practical Decimal backend.
`digits=36, backend='rational'` selects a slower integer/rational fixed-point
algorithm with no fixed library precision ceiling. The latter rounds every
basic operation to a multiple of 10^-digits and evaluates elementary functions
by finite rational series. Precision is retained in checkpoints. To avoid
freezing binary-float input errors during precision refinement, declare exact
parameters with integers, rational strings or `Fraction`.

Feature normalization uses the fixed positive ridge
eta_N=1/[1024(N+1)^2] and inverse Cholesky factors. No singular direction is
deleted. The generic source compiler additionally uses `epsilon_cov>0`;
this is an approximation removed in its own limit. The core initializer
does not need this source regularizer, and marks it unused. An unresolved
positive pivot, nonfinite state, invalid probability/input or exceeded
resource allowance raises an error. Increase declared precision or resources
explicitly; no automatic tolerance selection or convergence certificate is
provided.

At each fixed order, the proved numerical refinement removes arithmetic error
first, then time step, input quadrature, population quadrature, initialization
quadrature, and finally generic source regularization. Closure order is taken
to infinity after those limits. This is an iterated limit, not permission to
choose an arbitrary diagonal. Convergence is uniform in physical time and the
whole input circle, and includes the declared joint pairs and RMS motions.
Agreement between finite runs provides operational evidence only.

`DataLaw(inputs,labels,probabilities)` also permits exploratory finite circle
laws with finite labels; validate them with the state's arithmetic. Evolution
at other horizons or on broader inputs uses the same equations, but those uses
are outside the represented-family guarantee unless separately proved. There
is no implied general Borel-integration oracle.

### Bounded validation recipe

From the repository root, run the deterministic tests and the supplied
predeclared validation plan into fresh directories:

```text
mkdir -p data/established
observable_test_scratch=$(mktemp -d "$PWD/data/established/observable_tests.XXXXXX")
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 H4_LAW_TEST_SCRATCH="$observable_test_scratch" H4_VALIDATION_TEST_SCRATCH="$observable_test_scratch" TMPDIR="$observable_test_scratch" python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_solver_plan.json --output-dir data/established/observable_solver_check
PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/scripts/analyze_observable_solver.py --plan code/validation/observable_solver_plan.json --runs data/established/observable_solver_check --output data/established/observable_solver_analysis --recount-state
```

The twelve configurations cover two supported laws, odd orders 1,3,5,
a time-step refinement, a joint integration/time refinement, and a small
four-backend-resolution comparison. They use deterministic joint integration
points, so no random seed is needed. Each configuration includes a disk
restart and final paired observations. The plan fixes T=1/200, a 128-direction
output panel, one numerical thread, a 4 GiB process memory allowance,
20 CPU/wall minutes per configuration and one CPU hour for all workers.
The supervisor stops budget breaches and records failures without searching
for replacement parameters. Allow ten CPU minutes for deterministic tests.

Records include source hashes, configurations, environment, initialization,
evolution and observation timings, operating-system peak memory, retained-state
bytes, and diagnostics of the retained population-point feature Grams. These
condition diagnostics describe that particular finite rule; they are not
the raw initialization Grams or a conditioning guarantee. Observation archives
are rounded to float64 for analysis; exact working values remain in the JSON
checkpoints. The analysis verifies output hashes and reports all comparable
declared pairs. It does not compare with a supplied reference trajectory.

These checks establish operation at declared resolutions. Their differences
do not bound true prediction or hidden-motion error, do not demonstrate a
monotone convergence rate, and do not select a resolution for a tolerance.

## Observable computation through physical time 40

C.4.7.10 part D extends the same `observable_solver` and initialized-word
hierarchy through physical time 40 on a separate fixed supported family. The
bias-free two-hidden-layer tanh model, stored Gaussian variances
`(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved squared loss and actual adjoint
are unchanged. Only the law module and time-40 validation/analysis interface
are added; the initializer, compiler, arithmetic, dictionary and integrator
are unchanged.

### Exact supported laws and integration

`pde.observable_laws` supplies `supported_radius()`, `supported_law()`,
`OrthogonalArcLaw`, `DyadicRadius`, `RationalRadius`, `IntegerExpression`
and `LawLimits`. The class name refers to the two reference axes, not to
orthogonality of its current support. Directions are normalized `u=x/sqrt(2)`.
The exact family uses equal label masses and rational intervals in `[-1,1]`,
mapped by `U(rho*s)=((1-(rho*s)^2)/(1+(rho*s)^2),2*rho*s/(1+(rho*s)^2))`
and its quarter-turn. A degenerate interval is an atom. The fixed exponent is
`E0=8192, E(j+1)=2**Ej` for ten steps and `rho=2**(-E10)`.

This example constructs a supported nonatomic law and its numerical input
rule without initialization or training:

```python
from pde.observable_arithmetic import Arithmetic
from pde.observable_laws import supported_law, OrthogonalArcLaw

law = supported_law(a="-1", b="1", c="-1/2", d="1")
description = law.exact_description()
assert OrthogonalArcLaw.from_description(description).exact_description() == description
data = law.quadrature(8, Arithmetic())
assert len(data.labels) == 16
```

`supported_law(a=0,b=0,c=1,d=1)` is a nonorthogonal two-atom law.
`quadrature(m, arithmetic, limits=..., allow_collapse=...)` uses `m` equal
midpoint nodes per nondegenerate interval and one per degenerate interval.
Input integration is separate from the initialized joint-population rule.
Its exact transport error is at most `rho/m`. `data.metadata` retains the exact
descriptor, quadrature, scope, rounding errors and collapse information.

The exponent has an eleven-node exact expression. At decimal precision `p`
the law routine may replace its radius by zero if `E10>4*(p+8)+2`; float64
uses `p=17` for this decision. Each input then changes by at most
`2*rho<10**(-p-8)`. This is an explicit numerical approximation, saved in
metadata. At the declared validation precisions the supported perturbations
all collapse: these runs demonstrate operation, not resolved perturbed-law
behavior. Their positive exact law description is retained.

`LawLimits` bounds expression size/depth, literal bits, exact scalar bits and
rule nodes. Requests that cannot be represented under supplied allowances
raise `LawResourceLimit`; `allow_collapse=False` rejects an unresolved radius.
For a fixed exact law, increasing precision eventually disables collapse, but
the denominator alone then needs `E10+1` bits. The convergence theorem permits
allowances to increase to admit each requested finite computation. Default
limits do not promise practical resolution of this extremely small radius.
Direct coordinate/weight rounding and any resulting collapse are recorded
separately; operational weights are not silently normalized.

`OrthogonalArcLaw(RationalRadius("1/20"), ...)` uses the same integration and
solver interface for wider arcs. It is exploratory; the time-40 theorem
does not apply simply because a run finishes. A user-supplied scope tag is
descriptive. The supported validation worker verifies the exact radius against
`supported_radius()` before assigning its supported scope.

### Qualitative limit and storage contract

For each fixed represented law and order, remove rational arithmetic error,
time mesh, input quadrature, population replay, initializer quadrature, then
generic source regularization, in that order. Finally let closure order tend
to infinity. The source regularizer is unused on the optimized core branch.
Part D proves uniform convergence on `[0,40]` and the full input circle,
uniform-time training-averaged initial/current pair laws in `W2`, their RMS
motions and risks. Finite-precision query outputs use the supremum norm;
exact limiting predictions are continuous. The method is deterministic.
Finite-network identification is separately in probability and retains the
actual finite random initial readout. An arbitrary simultaneous refinement or
tolerance-to-resolution rule is not asserted.

The same solver evolves `w,c,M`, retaining complete joint `b1,g,w` and
`b2,c` populations, both probability vectors and fixed contraction `D`.
For populations `P1,P2`, feature dimensions `d1,d2`, and `A` input nodes,
the retained numerical state has
`P1*(d1+5)+P2*(d2+2)+2*d1*d2` scalars and the finite law has `4*A`.
Part D.5 accounts separately for initialization tables/source programs,
coefficient contractions, Heun stages, input blocks, precision, exact law
descriptions and total runtime. Neither source programs nor observations
are fed into later dynamics. Stage storage stays bounded at a fixed
resolution; step counters require only their predeclared integer width.

### Maintained bounded recipe

Run from the repository or standalone edition root, into fresh directories:

```text
mkdir -p data/established
observable_test_scratch=$(mktemp -d "$PWD/data/established/observable_tests.XXXXXX")
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 H4_LAW_TEST_SCRATCH="$observable_test_scratch" H4_VALIDATION_TEST_SCRATCH="$observable_test_scratch" TMPDIR="$observable_test_scratch" python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v
python -B code/scripts/run_observable_validation.py --plan code/validation/observable_horizon_plan.json --worker validate_observable_horizon.py --output-dir data/established/observable_horizon_check
python -B code/scripts/analyze_observable_horizon.py --plan code/validation/observable_horizon_plan.json --runs data/established/observable_horizon_check --output data/established/observable_horizon_analysis
```

The setup creates fresh scratch inside this edition and supplies both required
test scratch settings and TMPDIR. Keep the resulting directory with the check
records. Allow 600 CPU seconds for deterministic tests. The time-40 plan fixes 14
configurations before execution: supported atomic and nonatomic cases at
orders 1,3,5; separate time, initialization, population and input-law
refinements; two resolved exploratory arc rules; and a small rational
24/36-digit comparison. It fixes one worker/thread, 1200 CPU/wall seconds
per configuration, 7200 cumulative CPU seconds, and 4 GiB process memory.
No random seed is needed for the deterministic joint integration. The
supervisor records and stops exceeded limits without parameter replacement.
Its optional `--worker` selects the new producer; omitting it preserves the
H3 default worker and original plan protocol. Sampled RSS monitoring is not
an operating-system memory reservation.

Each configuration starts from its prescribed initializer and completes its
own steps to time 40. The six observation times are `0,1/200,1,10,20,40` and
the output circle has 128 directions. At off-mesh times the worker observes
an affine interpolation of adjacent states and continues from the actual
right node. At 20 it saves its own complete current state and finite law,
continues to 40, then loads the checkpoint and repeats the remaining identical
steps. It compares all nine state arrays, three data arrays, metadata,
arithmetic and final prediction by exact scalar encoding. Plan and record
retain physical time, intended step, remaining steps and block size alongside
the serializer's complete state. Exact restart assumes the same backend and
reduction environment; no new initializer is called.

Records contain exact source/configuration hashes, environment, initialization,
evolution, observation, checkpoint and restart timings, peak RSS, retained
state/data bytes, exact law-description bytes and structural stage allowances.
Phase timings need not sum to total process time. Stage allowances and current
per-scalar byte estimates are distinct from measured RSS and temporary rational
arithmetic storage. Conditioning diagnostics concern retained P-node feature
Grams, which may be singular because no redundant feature is deleted. Their
null/status values disclose unresolved/infinite estimates; they are not
normalization-Gram or conditioning certificates.

Each saved NPZ contains float64 views of both `(initial,current)` pair arrays,
their population/data weights, input and circle directions, predictions,
labels, loss and RMS. A companion JSON preserves every working value: float
hexadecimal strings, exact Decimal strings, or hexadecimal fixed-point integer
units with the saved decimal scale. The analysis verifies hashes and independently
recomputes loss, paired RMS and moments. It reports all comparable declared
configurations. Agreement in a float64 view is not exact high-precision
agreement. These fixed panels/times do not certify whole-circle or time-uniform
accuracy, monotone order convergence or a target learning threshold.

### Recorded operation

The declared 14-configuration run completed with exact own-state restart in
every case. The worker CPU sum was 506.291 seconds; maximum process peak RSS
was 56,119,296 bytes (53.520 MiB). The full deterministic observable suite
contained 67 passing tests; the inherited exact rational check of the reference
learning constants also passed. These are operational and algebraic results.

Orders 1,3,5 use dimensions `(5,3)`, `(35,10)`, `(128,21)`. The baseline
supported runs used 1024 initializer nodes, 512 population nodes, 8000 steps
and float64; supported arc rules used eight nodes per component. The recorded
maximum prediction differences over saved times and the 128-direction panel
were `1.205e-6` on doubling the step count, `0.003274` on doubling initializer
nodes, and `0.01240` on doubling population nodes at order 3. The supported
input-rule refinement differs only at rounding level because the perturbation
collapses. Resolved radius-1/20 exploratory arc rules with eight and sixteen
nodes per component differed by `0.0002252` on that panel; no supported-flow
theorem is attached to this wider radius. The 24/36-digit tiny rational runs
agree in the reported float64 view; exact working observations are retained.

The maintained producer and analyzer regenerate the full configuration tables,
losses, paired observations, timing, memory and conditioning records. Their
numbers are empirical diagnostics, separate from part D's qualitative proof
and target substantial-learning conclusions.
