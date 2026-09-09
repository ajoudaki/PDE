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
