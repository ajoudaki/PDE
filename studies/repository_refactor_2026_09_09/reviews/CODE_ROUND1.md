# Isolated adversarial code and mathematical contract audit

Date: 2026-09-09. Verdict: **NOT CLEAN — precise repairs required.**

The exact finite-network algebra and the Gaussian moment/PSD mathematics are
correct. All 26 supplied tests pass. Nevertheless, the current activation
callback contract permits ordinary implementations that silently corrupt
gradients, built-in derivatives can silently return incorrect zeros, and two
public numerical reductions bypass finite-result validation. Nine independent
repair regressions reproduce these issues. No implementation or supplied test
was changed.

## Scope, isolation, and reproducibility

Read in full: all six files under `code/`, plus `docs/NOTATION.md`,
`docs/finite_dynamics.md`, and `docs/gaussian_calculus.md`: nine input files,
1,533 lines. Input SHA-256 hashes are recorded below and were rechecked after
testing. No other project files, histories, previous audits, external sources,
Git commands, dependency installations, agents, or large experiments were used.
The permitted Python/NumPy runtime necessarily supplies its installed runtime
modules; no out-of-scope project content was consulted.

All commands ran in `/tmp/pde-established-code-review.Ssin9e/`. The runtime was
Python **3.10.12**, NumPy **1.26.4**, with bytecode writing disabled and numerical
thread counts set to one. The only new artifacts are this report and the
reproducible, bounded `audit_checks.py`; supplied inputs remain read-only.

Run the supplied suite:

```sh
cd /tmp/pde-established-code-review.Ssin9e
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.10 -B -m unittest discover -s code/tests -p 'test_*.py' -v
```

Run the combined audit suite:

```sh
cd /tmp/pde-established-code-review.Ssin9e
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.10 -B audit_checks.py
```

The audit harness marks known repair regressions `expectedFailure` so that it
can finish and report all evidence. Its `OK (expected failures=9)` is **not**
an acceptance result. Remove those decorators when adopting the regressions as
repair acceptance tests; repaired behavior must pass them normally.

**Standalone execution:** yes, with the documented Python/NumPy dependencies
and `code/` on the import path, the library requires no other project files.
An additional `python3.10 -I -B` smoke run explicitly inserted only this private
`code/` directory, imported the 16 public exports, and executed the computations
and assertions in both README examples successfully. All three loaded `pde`
module paths resolved inside this copy. There is no packaging/install manifest;
plain `import pde` without making `code/` importable is not the advertised usage.
This execution result does not remove the correctness findings below.

## Required repairs

### R1 — P1: custom callbacks can overwrite saved state and corrupt derivatives

Locations: `code/pde/finite_network.py:150–165, 179–189, 227–229`;
contract: `code/README.md:61–68`, `Activation` at lines 31–47.

The documented requirements are real finite shape-preserving outputs and the
appropriate differentiability. There is no requirement forbidding in-place
evaluation or reuse of an output buffer. `_evaluate` passes the actual cached
preactivation to a callback and retains its returned array without copying.
Consequently valid numerical implementations of smooth functions invalidate
the saved fields used for differentiation.

Minimal reproduction, with all dimensions one and ordinary-sized values:

```python
import numpy as np
from pde import Activation, Parameters, forward, loss_gradients
act = Activation("inplace_tanh", lambda z: np.tanh(z, out=z),
                 lambda z: 1 - np.tanh(z)**2)
p = Parameters(([[2.]],), [1.])
fields = forward(p, [[1.]], act)
g = loss_gradients(p, [[1.]], [0.], act).weights[0][0, 0]
```

The network is `f=tanh(2)`. Its preactivation must be 2, but the returned
preactivation is `0.9640275800758169`. Its loss gradient must be
`2*tanh(2)*(1-tanh(2)**2) = 0.13621868742711296`; the library returns about
`0.854866`, having evaluated the derivative at the activation value.

Two related independently reproduced cases matter for the repair:

- An identity value callback returning `z`, with an identity derivative callback
  writing ones into `z`, changes the saved hidden value. At `W=2, readout=1,
  x=1, y=0`, the readout gradient is returned as 4 instead of 8.
- A shape-preserving identity callback returning a reusable scratch array makes
  hidden fields from different layers share that buffer. For weights 2 then 3,
  the first hidden field becomes 6 instead of 2 after the second call. The
  forward prediction remains 6, concealing the corrupted derivative source.

**Repair request:** preserve each layer's original preactivation and own the
stored callback results. A concrete implementation is to call each callback on
a private copy of its input, validate the result against the original shape,
then copy the result before retaining it. Apply this to value and derivative
callbacks. Alternatively, explicitly narrow the public callback contract to
non-mutating callbacks whose returned arrays remain stable throughout the
operation; that is a contract change, and the present broader contract cannot
be certified. Arbitrary callbacks that mutate unrelated external state are not
something an array-copy policy can generally prevent.

Required regressions: `test_inplace_activation_preserves_preactivation`,
`test_inplace_activation_gradient`,
`test_inplace_derivative_does_not_overwrite_hidden_state`, and
`test_reusable_activation_buffer_does_not_alias_layers`.

### R2 — P2: built-in derivatives silently lose representable values

Location: `code/pde/finite_network.py:50–51`. This affects `backward`, loss
gradients, flow, GD, and the hidden-parameter kernel blocks.

`ARCTAN.derivative` computes `1/(1+z*z)`. At `z=1e155`, `z*z` overflows and the
derivative becomes zero, although the correct derivative is approximately
`1e-310`, a representable subnormal. This is amplified to an ordinary-sized
gradient in a fully finite example:

```python
p = Parameters(([[1e155]],), [1e153])
g = loss_gradients(p, [[1.]], [0.], ARCTAN).weights[0][0, 0]
# observed: 0.0
# stable reference: 0.00031415926535897833
```

Here `f≈1.5708e153` and the squared loss is approximately `2.4674e306`, both
representable. Thus this is not merely a request to handle an unrepresentable
final loss. `_array` cannot detect the error: the incorrect zero is finite.

`TANH.derivative` uses `1-tanh(z)**2`. At `z=20`, rounded `tanh(z)` equals one,
but the true derivative is about `1.6993417021166355e-17`. For
`Parameters(([[20.]],), [1e10])`, `x=1`, `y=0`, the first-weight loss gradient
is returned as zero instead of approximately **3398.683404233271**. This
cancellation example emits no overflow warning.

**Repair request:** use numerically stable derivative formulas. For tanh,
`e=exp(-2*abs(z))`, `4*e/(1+e)**2` avoids subtracting nearly equal numbers.
For arctan, use a small/large-argument split: for `abs(z)>1`, let `u=1/abs(z)`
and compute `u*u/(1+u*u)`; use the original formula for smaller arguments.
Evaluate only the selected branch, so eager evaluation does not reintroduce
overflow. Add the two large/saturated finite-gradient regressions and values
on both sides of the branch boundary. These fixes do not promise arbitrary
relative accuracy after a derivative itself falls below float64 range.

Required regressions: `test_arctan_finite_large_gradient` and
`test_tanh_finite_saturated_gradient`.

### R3 — P2: the loss reduction can overflow despite a representable mean

Location: `code/pde/finite_network.py:213–217`.

```python
p = Parameters(([[0.]],), [0.])
loss(p, [[0., 0.]], [1e154, 1e154])  # observed: inf
```

Both predictions are zero. The correct mean squared loss is approximately
`1e308`, within float64 range, but `r @ r` forms approximately `2e308` before
division by the batch size. The final value is not validated. Even the
mathematical invariance of mean loss under duplicating a batch is broken at
this scale: the one-sample calculation is finite and the duplicated one is not.
Separately, a zero prediction with label `1e308` returns infinity rather than
rejecting an unrepresentable squared loss.

**Repair request:** compute the mean square with scaled arithmetic, check
residuals and the final scalar, and raise a clear `ValueError` when the result
cannot be represented. For example, normalize finite residuals by their maximum
absolute value, handle the all-zero case, and multiply the normalized mean back
in an order that avoids squaring the scale before multiplying by the mean.
Merely adding a final finite check detects the problem but still rejects the
representable duplicated-batch example. Test both representable intermediate
overflow and an actually unrepresentable result.

Required regressions: `test_loss_representable_mean_avoids_intermediate_overflow`
and `test_loss_unrepresentable_result_rejected`.

### R4 — P2: the total kernel bypasses the finite check applied to its blocks

Location: `code/pde/finite_network.py:273–278`.

```python
p = Parameters(([[1.]],), [1.])
kernel_blocks(p, [[1.]], IDENTITY, kappas=[1e308, 1e308])
# two finite scalar blocks, each 1e308
kernel(p, [[1.]], IDENTITY, kappas=[1e308, 1e308])
# observed: array([[inf]])
```

The true total `2e308` is outside float64 range. This is not an algebraic kernel
error or a demand to represent that number in float64; it is inconsistent
overflow handling at the public API boundary. `kernel_blocks` validates its
return, whereas `kernel` performs a further unchecked reduction.

**Repair request:** pass the final sum through finite-array validation and raise
`ValueError` on an unrepresentable total, matching the existing block/parameter
policy. If infinity is deliberately permitted, document that exceptional
contract explicitly; the current checked-finite presentation is insufficient.

Required regression: `test_kernel_final_sum_revalidated`.

## Finite-network mathematics and implementation correspondence

No missing width, dimension, sample-count, residual, mobility, or factor-two
normalization was found in the algebra. These are exact real-arithmetic
statements; floating-point failure modes are listed above.

Let `s_a^(1)=x_a/sqrt(d)` and `s_a^(ell)=h_a^(ell-1)` for later layers.
Writing `a=W^(L+1)`, differentiation of `f_a=a^T h_a^(L)/n` gives
`delta_a^(L)=a*phi_L'(z_a^(L))`. Backward propagation gives
`delta_a^(ell)=phi_ell'(z_a^(ell))*(W^(ell+1))^T delta_a^(ell+1)`.
Consequently

\[
\nabla_{W^{(\ell)}}f_a=\frac{\delta_a^{(\ell)}(s_a^{(\ell)})^T}{n},
\qquad \nabla_a f_a=\frac{h_a^{(L)}}n.
\]

For residuals `r_a=f_a-y_a`, the loss gradient is `(2/m) sum_a r_a grad f_a`.
This is precisely the factor `2/(m*n)` and the sources used at code lines
220–229. Residuals are not embedded in `delta`.

| Contract | Finding |
| --- | --- |
| Forward scaling | `x/sqrt(d)`, stored hidden matrices with no extra width factor, readout divided by `n`; correct at lines 157–166. |
| Initialization | First Gaussian standard deviation 1, middle `1/sqrt(n)`, stored readout `1/n`; variances match NOTATION. Local seeded generator and draw order agree. |
| Mobility | First/readout blocks have `n*kappa`; middle blocks `kappa`. The two endpoint blocks remain distinct at `L=1`. |
| First kernel block | `kappa_1*(x_a^T x_b/d)*(delta_a^T delta_b/n)`; correct. |
| Middle kernel block | `kappa_ell*(h_a^T h_b/n)*(delta_a^T delta_b/n)`; correct. |
| Readout kernel | `kappa_(L+1)*(h_a^T h_b/n)`; correct. |
| Simultaneous GD | All gradients use the old state, then every block is updated into a new array. No sequential recomputation or exact-flow claim. |

Each block is a Gram matrix of `sqrt(D_ell) grad_(theta_ell) f_a`, hence PSD
over the reals. Summing the chain rule gives

\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr
=-\sum_\ell\frac{\|\dot\theta_\ell\|^2}{D_\ell}.
\]

The supplied hand-computed GD values are correct: for `W=(1,2)^T`,
`a=(3,4)^T`, `x=y=1`, `f=5.5`, `r=4.5`, the velocity blocks are
`(-27,-36)^T` and `(-9,-18)^T`. Step 0.1 gives the stated
`(-1.7,-1.6)^T` and `(2.1,2.2)^T`.

The global finite-width flow proof in `finite_dynamics.md:111–153` is valid.
For globally defined C2 activations, the nonnegative C2 loss has a locally
Lipschitz gradient field. Energy dissipation bounds the squared velocity in the
fixed positive mobility metric. Cauchy–Schwarz gives a square-root modulus in
time, hence a finite state limit at any putative finite maximal endpoint.
Local existence at that state extends the solution. This does not require
bounded activations and does not imply unconditional GD stability.

The width-uniform bounds in Section 4 are valid under its additional bounded
first-derivative, initial-norm, initial-loss, and fixed-depth assumptions.
The forward RMS induction uses `|phi(z)|<=|phi(0)|+sup|phi'|*|z|`; the reverse
induction uses the same derivative bounds and middle operator norms. No
coordinatewise bound or unbounded population multiplication bound follows.
The Gaussian initialization argument is consistent: the first squared
Frobenius norm divided by `n` tends to `d`, readout squared RMS tends to zero,
and the sphere-net estimate `2*9^(2n)*exp(-n*M^2/8)` follows from the stated
net sizes, factor-two approximation, and Gaussian tail bound.

## Gaussian chapter and exact evaluator

### Sections 1–3

Section 1 correctly retains the finite random response
`a_n=mean(y_i*g(y_i))`. Projecting each isotropic Gaussian row onto the span of
ones gives the stated conditional matrix mean; the complementary row component
is independent. Transposing against fixed conditional `g(y)` gives covariance
`sigma_n^2*P`. The RMS coupling bound, including `sigma=0`, is valid. Polynomial
growth provides the moments and vanishing boundary terms used for the laws of
large numbers and Gaussian integration by parts. Empirical-law convergence
does not imply independent finite-width transpose coordinates.

Section 2's mean satisfies `MV=Y` and `M^T U=R` using `U^T Y=R^T V`. The
unobserved subspace is exactly `A=(I-P_U)A(I-P_V)`, and the stated mean is
orthogonal to it. Thus conditioning an isotropic Gaussian matrix yields the
claimed mean and complementary Gaussian covariance. The adaptive extension
properly requires independent recorded roots and each query to be measurable
from earlier answers before its own answer is observed. Formula (7) applies to
a fixed/known next query under this conditioning; it is not valid for an
arbitrary additional query secretly depending on unrevealed matrix entries.
The empty/full-span cases also agree with an independent stacked linear
conditioning calculation in 16 bounded checks.

Section 3's identities are correct for C3 `F`. Differentiating
`2<g,Hg>` in direction `g` contributes `2T[g,g,g]` from the Hessian and
`4||Hg||^2` from the two gradient factors. The coordinate change
`theta=D^(1/2)q` correctly converts a constant positive definite mobility to
Euclidean flow. One wording clarification is advisable: a scalar residual
multiplies the predictor gradient for a single squared-error term; the general
batch velocity is a sum of residual-weighted predictor gradients. If `F` itself
is the total loss, physical descent is simply `-D grad F`. No incorrect
displayed derivative formula was found.

### Section 4: self-contained Wick proof, including degenerate covariance

The newly added section at `gaussian_calculus.md:193–251` is correct. The
following spells out its proof obligations and their implementation mapping.

Let `Sigma` be symmetric PSD of finite dimension `p`. Finite-dimensional
spectral decomposition supplies a real matrix `A` with `AA^T=Sigma`, even
when eigenvalues vanish. Take a standard Gaussian vector `G` of the matching
dimension and set `X=AG`. Gaussian tails make all polynomials of `G`
integrable. For any polynomial `P`, one-dimensional integration by parts in
each `G_k`, followed by the chain rule, gives

\[
\begin{aligned}
\mathbb E[X_iP(X)]
&=\sum_k A_{ik}\mathbb E[G_kP(AG)]\\
&=\sum_{k,j}A_{ik}A_{jk}\mathbb E[(\partial_jP)(AG)]\\
&=\sum_j\Sigma_{ij}\mathbb E[\partial_jP(X)].
\end{aligned}
\]

Every integration boundary term vanishes because it is a polynomial times a
Gaussian density; finite sums and expectations may be interchanged. A density
for `X` itself and an inverse of `Sigma` are not needed.

Define `M(alpha)=E[prod_j X_j^(alpha_j)]`, with nonnegative integer powers and
the usual empty-product convention. Then `M(0)=1`, including at zero
covariance. Centered symmetry `X` and `-X` gives zero for odd total degree.
If `alpha_i>0`, apply the preceding identity to
`P(x)=prod_j x_j^(alpha_j-1_(j=i))` to obtain

\[
M(\alpha)=\sum_{j:\,\alpha_j-\mathbf1_{j=i}>0}
(\alpha_j-\mathbf1_{j=i})\Sigma_{ij}
M(\alpha-e_i-e_j).
\]

Omitting zero coefficients prevents negative exponents, including the case
`j=i, alpha_i=1`. Every recursive call decreases degree by two. Induction on
degree proves termination of the mathematical recurrence and correctness for
all finite exponents. Its coefficient counts exactly the possible remaining
legs of coordinate `j`; iterating is Wick's pairing formula. No independence
between the coordinates of `X` is assumed. Rational covariance makes every
recurrence operation rational, and rational linearity evaluates any finite
polynomial with rational coefficients.

Code lines 93–109 implement exactly this recurrence: choose one positive
coordinate, remove a leg, enumerate the remaining multiplicities, skip zero
covariances, and recurse. Each result is a `Fraction`. Covariance/type/degree
validation occurs before either the constant or odd-degree shortcut. The cache
is local to the call, and `finally: moment.cache_clear()` also clears it if
evaluation raises. Mathematical termination does not remove Python's recursion
and memory limits; the documented small-order scope is relevant here.

### Section 4: necessary and sufficient covariance validation

After checking square shape and symmetry, write the current matrix as

\[
S=\begin{pmatrix}a&b^T\\b&C\end{pmatrix}.
\]

If `a<0`, its quadratic form at the first basis vector is negative. If `a=0`
and `b!=0`, choose `v=b`; the form at `(t,v)` is
`2t||b||^2+b^T Cb`, which is negative for sufficiently negative `t`.
Therefore a PSD matrix with a zero pivot must have an entirely zero
corresponding row/column. With `a=b=0`, PSD is exactly PSD of `C`.

For `a>0`, completing the square gives

\[
(t,v)^TS(t,v)
=a\left(t+\frac{b^Tv}{a}\right)^2
+v^T\left(C-\frac{bb^T}{a}\right)v.
\]

If the Schur complement is PSD, the whole form is nonnegative. Conversely,
set `t=-b^Tv/a` to see that PSD of the whole matrix forces PSD of the Schur
complement. Each step removes one row and column, with the empty matrix the
vacuously PSD terminal case. This proves necessity and sufficiency, including
zero pivots created after earlier positive-pivot elimination. Division occurs
only at a strictly positive rational pivot, so the code introduces neither
rounding nor a hidden nonsingularity assumption.

`_validate_psd`, lines 23–43, implements precisely these cases. Symmetry is
already established before it is called, so checking the zero row suffices
for the zero column too. The independent principal-minor oracle found no
disagreement on 729 symmetric 3-by-3 integer matrices, tested with constant,
odd, and even moments. An additional matrix
`[[1,1,1],[1,1,2],[1,2,5]]` creates the Schur complement `[[0,1],[1,4]]`;
all six coordinate permutations were correctly rejected for all three degrees.

No incorrect claimed small Gaussian value was found. In particular, with
variances 2 and 3 and covariance `1/3`, the supplied values `56/9`, `164/9`,
and `116/3` for powers `(2,2)`, `(3,3)`, and `(4,2)` are correct. The
trivariate `(2,2,2)` value 28 and the rank-one values 60 and -24 are also
correct. An independent polynomial expansion in latent independent Gaussians
verified 243 moments, including negative correlations, rational coefficients,
zero rows, all-zero covariance, and rank-deficient maps.

## Validation and mutation: supported behavior versus optional improvements

The supplied shape, type, seed, positive-mobility, activation-count, and
nonnegative-step checks work on their tested domains. Supplemental tests cover
the three previously unexecuted validation statements: empty/non-string
activation names, a non-`Parameters` argument, and a non-activation sequence
element. Gaussian floats, booleans (including NumPy booleans), malformed
sequences, wrong lengths, negative powers, asymmetry, and indefinite matrices
are rejected; NumPy integral values are accepted as integers.

The constructor's documented aliasing is real and is **not a bug**: float64
arrays may be retained and remain mutable despite the frozen dataclass.
Changing the owner's array changes the parameters. Evaluation rechecks their
current values/shapes. Sixteen checks verify NaN rejection after weight or
readout mutation through each of the eight computational entry points.
Reshaping a first matrix incompatibly is also rejected. Overlapping weight
and readout storage remains unchanged during GD, and all returned GD blocks
are independent of old storage and of each other. Read-only parameter/input/
label/mobility arrays and strided input views also work.

The following are optional ergonomics or scope clarifications, separate from
the required repairs:

- A returned `ForwardPass` is mutable. With `IDENTITY`, its hidden field and
  preactivation share memory; editing one changes the other while the already
  computed output stays unchanged. No independent immutable-snapshot contract
  is promised. Documenting that fact or offering defensive snapshots is useful.
  This differs from R1, where corruption occurs inside an unmodified API call.
- NumPy covariance matrices/generators are not required inputs to
  `gaussian_moment`: the documentation explicitly requests finite lists or
  tuples. Broader container support is optional.
- High-order exact moments can hit Python recursion limits or consume large
  rational storage. A stated degree limit or iterative evaluator could improve
  usability, but the API already disclaims high-order enumeration. No high-order
  performance or scalability test was run or claimed.
- No algorithm using float64 can promise accurate evaluation of every
  real-arithmetic expression for every finite input magnitude. State the
  representability/error policy clearly, distinguish raw-coordinate "exact GD"
  from exact floating-point arithmetic, and do not infer numerical stability
  from the global real-ODE theorem. A global arbitrary-magnitude stable network
  evaluator is outside this audit's repair request.
- Cross-block array sharing does not declare tied model parameters. An optional
  tied-weight API would need different derivative semantics; the current
  independent-block model and fresh simultaneous updates are consistent.

## Test counts, coverage, and missing tests

Supplied suite: **26 test methods, 26 passed**, comprising 15 finite-network
tests and 11 Gaussian tests. Its direct run took 0.112 seconds in this runtime.
Final instrumented combined run: **44 methods = 26 supplied + 9 independent
passing groups + 9 expected-failing repair regressions**. Thus **35 methods
passed normally**, 9 reproduced repair failures, with no unexpected failure
or error. Runtime was 1.649 seconds. These are local bounded runtimes, not
performance guarantees. Intermediate development runs are not added to these
counts as though they were distinct tests.

The final combined run recorded **2,532 `unittest` subtest contexts**, with no
failed subtest contexts; the nine expected failures are ordinary test-method
failures, not subtests. Loops and individual assertions are not misreported as
additional test methods.

| Independent check | Exact bounded coverage |
| --- | --- |
| Rational neuron-path expansion | 18 linear networks: width 1/2/3, input dimension 1/4, depth 1/2/4, three samples including zero/opposite samples. |
| Derivatives/flow/GD from path monomials | 238 scalar coordinates, each checked for loss gradient, mobility-scaled velocity, and simultaneous GD. |
| Kernel from exact path Jacobians | 60 separate parameter-block kernels, each a 3-by-3 matrix. |
| Gaussian latent-polynomial oracle | 243 moments, dimensions 1–3, total degree at most 6, five latent linear maps. |
| PSD via independent principal determinants | 729 matrices: 195 PSD, 534 non-PSD; 2,187 calls across total degrees 0/1/2. |
| Created zero Schur pivot | 18 additional rejection calls: six permutations times three degrees. |
| Gaussian conditioning geometry | 16 cases, dimension 3, both observation ranks independently 0–3. |
| Mutable-array revalidation | 16 NaN rejection checks across eight APIs and two parameter locations; additional alias, shape, striding and read-only checks. |

Coverage was measured without installing a coverage dependency. The harness
uses Python line tracing and reports **distinct AST statement-start lines
inside function bodies**, excluding imports/class/function declarations and
docstrings. This is a precisely defined, limited line metric, not branch,
condition, path, NumPy-internal, mathematical, or `coverage.py` coverage. Import
initialization and the activation lambdas declared at module scope are outside
this denominator; they were separately exercised by import and functional
checks. The combined measurement includes repair-regression execution.

| Source | Supplied suite | Combined audit | Supplied omissions |
| --- | --- | --- | --- |
| `code/pde/finite_network.py` | 120/123 statement-start lines (97.56%) | 123/123 (100%) | Lines 45, 132, 146. |
| `code/pde/gaussian_moments.py` | 58/58 (100%) | 58/58 (100%) | None under this metric. |
| `code/pde/__init__.py` | 0/0, not applicable | 0/0, not applicable | No function bodies; isolated import separately passed. |
| Total function-body statement starts | 178/181 (98.34%) | 181/181 (100%) | Three validation statements. |

The supplied tests already provide meaningful nonlinear coordinate finite
differences at depths 1–3, output-Jacobian kernel checks, output-flow and
weighted-energy directional checks, batch invariance, zero residual/step,
initialization scaling, and exact small moments. The audit's path expansion
and latent-polynomial expansion add independent algebraic oracles rather than
reusing the library's recurrence/backpropagation as the reference answer.

**Missing acceptance tests that matter:** the nine repair regressions above;
boundary tests for the repaired built-in derivative formulas; explicit finite
loss behavior under duplicating a very large-residual batch; and the in-place
and reusable-buffer callback cases at multiple layers. Retain the new PSD
post-elimination-zero-pivot and exact latent-oracle cases as stronger Gaussian
regressions. Numerical line coverage alone missed every substantive defect.

No flow integrator, long-time numerical trajectory, figure, large-output,
population-limit, broad performance, or infinite-width claim was tested or
certified. The finite-flow existence and new Section 4 results were checked as
proofs, not inferred from these numerical tests.

## Exact input manifest

All nine input hashes matched before and after the audit checks:

```text
bb57ccecdd1633cb3604256a0f49d70642c8995455b2adc03e88bb401ad9aaaa  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
7ea8474b484dee66cb7bcf0918e17fd7571b228105dc2be56aa6245811bf3fbd  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
6f2917573f0d55faa47c3652a3ccac1c72dbfead68c3931e0b90baba629ba550  docs/gaussian_calculus.md
```

New reproducibility artifact (not an audited input):

```text
154fc81b2ec81286b76d5ebb0b35e31fa84e06883a8b0f68d3f2ac2ef07a5d13  audit_checks.py
```

Acceptance requires resolving R1–R4 under an explicit numerical and callback
contract, then rerunning the original suite and the repair regressions as normal
passing tests. This audit requests those repairs; it does not modify the library.
