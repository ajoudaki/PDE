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
