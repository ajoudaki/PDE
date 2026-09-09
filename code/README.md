# Finite networks and exact Gaussian moments

This NumPy-only package implements the finite equal-width network in
[the notation contract](../docs/NOTATION.md) and
[the finite-dynamics chapter](../docs/finite_dynamics.md).
It supports any positive number of hidden layers and any nonempty fixed batch.
It is a finite reference implementation; numerical tests do not establish an
infinite-width limit. A separate small rational Wick evaluator supplies exact
centered Gaussian monomial moments without a symbolic compiler.

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
