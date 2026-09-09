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
