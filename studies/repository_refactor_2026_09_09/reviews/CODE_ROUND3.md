# Fresh isolated adversarial review

Verdict: **NOTCLEAN**

Four required fixes remain in the finite-network implementation. The supplied
47 tests and structural checker pass, but independent tests reproduce 15 failing
cases across these four findings. The exact rational Wick evaluator, its PSD
validation, and the mathematical arguments in the supplied chapters have no
identified correctness defect under their stated hypotheses.

## Scope and method

The sole review input was `/tmp/pde-code-round3.HFZHf0`: all of `code/`, all of
`docs/`, `Makefile`, and `requirements.txt`. All 14 input files were read in full,
including every supplied test and the structural checker. No repository,
history, previous review, web source, agent, or external skill file was consulted.
Standard Python/NumPy runtime imports were used to execute the permitted tests;
there were no installs or network requests.

No input was edited. SHA-256 checks after testing matched all 14 initial hashes.
The two persistent additions are this report and `review_checks.py`, which is a
reproducible independent test artifact, not part of the reviewed input. Test
temporary files were confined to the input directory by setting `TMPDIR` there;
bytecode generation was disabled. No filesystem output was directed elsewhere.

The numerical standard is the README's float64 contract, particularly
`code/README.md:75–80`. This review does not require arbitrary precision, exact
rounding, or rescue of arbitrary overflowing/underflowing matrix contractions.
The normalization findings below isolate scalar operations that discard useful
magnitude before or after a representable contraction. Their expected values
are derived with powers of two and need no high-precision numerical package.

## Required fixes

### R1 — P1: unsigned NumPy step sizes produce incorrect, positive GD increments

Location: `code/pde/finite_network.py:303–317`, especially both uses of `-eta`.

The validator accepts nonnegative finite `numbers.Real` values. NumPy unsigned
integer scalars satisfy that check. Unary negation is then performed in the
unsigned dtype before `_scaled_product` converts its argument to float64.
It wraps to a large positive integer, changing both the sign and magnitude of
the update.

Minimal reproducer:

```python
import numpy as np
from pde import IDENTITY, Parameters, gd_step

state = Parameters(([[1.0]],), [1.0])
new = gd_step(state, [[1.0]], [0.0], np.uint8(1), IDENTITY)
print(new.weights[0], new.readout)  # [[511.]] [511.]
```

Here `n=m=d=L=1`, `f=1`, the residual is 1, and both loss gradients are 2.
A simultaneous step of size 1 must return weight and readout equal to `-1`.
The accepted unsigned scalar instead yields:

| Step | Actual value of both updated blocks | Expected |
| --- | ---: | ---: |
| `np.uint8(1)` | `511.0` | `-1.0` |
| `np.uint16(1)` | `131071.0` | `-1.0` |
| `np.uint32(1)` | `8589934591.0` | `-1.0` |
| `np.uint64(1)` | `3.6893488147419103e19` | `-1.0` |

Each call also emitted two `overflow encountered in scalar negative` warnings.
Python int/float and the tested signed/floating NumPy scalars returned `-1`.

Required change: canonicalize the accepted step into the validated real
float64 domain before arithmetic, or supply `-1` as a separate scaling factor
without applying unary minus to an unsigned scalar. Keep rejection of booleans,
negative/nonfinite steps, and zero-step copy behavior. Add regression coverage
for all four unsigned types. This is a normal-scale API correctness error.

### R2 — P2: kernel normalization underflows before protected factor assembly

Location: `code/pde/finite_network.py:328–334`.

`_scaled_product` receives already-divided Grams: `x.T @ x / d`,
`delta.T @ delta / n`, and `h.T @ h / n`. A representable raw Gram can round
to zero at this division, although combining it with the supplied mobility
would give a normal, exactly representable float64 kernel entry.

For the simplest readout example, set `n=2`, `d=m=L=1`,
`W1=[[2**-537], [0]]`, readout `[0,0]`, input `[[1]]`, identity activation,
and `kappas=[1, 2**1023]`. Then

```text
h.T @ h       = 2**-1074                 (representable, tested)
(h.T @ h) / n = 2**-1075 -> 0            (the premature loss)
K_readout     = 2**1023 * 2**-1074 / 2
              = 2**-52                  (normal, exactly representable)
```

The implementation returns `0.0`. Four independently exercised locations fail:

| Normalized quantity | Actual selected block entry | Exact expected entry |
| --- | ---: | ---: |
| Readout activation Gram, `n=2` | `0.0` | `2**-52` |
| Input Gram, `d=4` | `0.0` | `2**-53` |
| First-layer delta Gram, `n=2` | `0.0` | `2**-52` |
| Middle-layer activation Gram, `n=2` | `0.0` | `2**-53` |

Complete fixtures are in `normalized_kernel` in `review_checks.py`. In each
case the relevant raw Gram is representable; its division causes the failure.

Required change: pass raw Grams, mobility, and the reciprocal dimension/width
factors together into protected scalar/elementwise assembly. Do not restore
the magnitude of an individual normalized Gram first. Apply this to all block
types and preserve negative off-diagonal entries. This request leaves the
README's limitation on the raw matrix products intact.

### R3 — P2: flow/GD prematurely materialize a lossy normalized gradient

Location: `code/pde/finite_network.py:279–282`, `287–292`, and `310–317`.

`loss_gradients` first multiplies raw contractions by `2/(m*n)` and constructs
a finite `Parameters` object. `flow_velocity` and nonzero `gd_step` call it
before combining mobility and step factors. The later `_scaled_product` calls
cannot recover a gradient rounded to zero and are never reached if the
standalone gradient overflows. The defect is the premature loss-normalization
boundary; constructing an unscaled velocity has already been avoided correctly.

Underflow reproducer: `n=4`, `d=m=L=1`, zero first weights, readout all ones,
input `2**-1074`, label `-1`, identity activation, and first-block multiplier
`2**1023`. The output is zero, residual one, and every delta is one. For each
first-weight entry:

```text
raw contraction = 2**-1074               (exactly representable)
stored gradient = (2/4) * 2**-1074 -> 0
physical velocity = -4 * 2**1023 * (2/4) * 2**-1074
                  = -2**-50
```

The flow returns negative zero; a GD step of size one returns unchanged zero
weights. A separate fixture puts `2**-1074` in each first weight with zero
readout, unit input and readout multiplier `2**1023`; the same error occurs in
the readout block. All four actual results were zero, against expected
`-8.881784197001252e-16`.

Overflow reproducer: `n=d=m=L=1`, first weight zero, readout one, unit input,
label `-2**1023`, identity activation. The first raw contraction is `2**1023`,
which is finite. Multiplication by the loss factor 2 overflows. Nevertheless,
either a flow with first multiplier `1/4`, or a GD step of `1/4` with default
multipliers, has finite first-block result `-2**1022`. Both calls instead raise
`ValueError('weight 1 must be finite')`. The readout gradient is zero. These
APIs do not require the loss itself to be representable; the README explicitly
allows finite GD without a loss-decrease guarantee.

Required change: share the evaluation/raw contractions while allowing flow and
GD to combine loss normalization, block mobility, step, and the GD addend
before restoring magnitude. They should not depend on an independently
representable normalized `loss_gradients` result. The standalone gradient API
can still return its correctly rounded underflow or reject an unrepresentable
gradient. No wider exponent range for the underlying contractions is required.

### R4 — P2: first-layer input predivision erases a representable prediction

Location: `code/pde/finite_network.py:204–206`; the same early source
normalization also appears at line 280.

The documented first-layer equation is `(W1 @ X)/sqrt(d)`. The implementation
first computes `X/sqrt(d)`. This can erase a tiny, valid input before its large
weight produces an entirely normal matrix-product result.

Use `n=m=L=1`, `d=4`, identity activation, readout `[1]`,

```python
W1 = [[2.0**1023, 0.0, 0.0, 0.0]]
X = [[2.0**-1074], [0.0], [0.0], [0.0]]
```

Direct float64 checks give `W1 @ X = 2**-51` and `(W1 @ X)/2 = 2**-52`.
Both are normal, exactly representable results, with no cancellation or
overflowing product. The implementation computes `2**-1074 / 2 -> 0` first
and returns output `0.0`. With label zero it also reports loss `0.0`, instead
of `2**-104 = 4.930380657631324e-32`.

Required change: preserve the first-layer normalizer until after the
representable contraction, or use an equivalent range-aware evaluation. Keep
the matching first-gradient normalizer in its scalar assembly rather than
discarding subnormal source entries. An ordinary float64 post-contraction
normalization suffices for this counterexample; a universal overflow-proof
matrix product is not requested.

## Optional improvements, not conditions for the verdict

1. Make custom activation obligations explicit in the README: `value` applies
   a scalar function coordinatewise, `derivative` is that function's actual
   coordinatewise derivative, and its values should be consistent across
   calls. Shape/finiteness and C2 regularity alone do not describe an arbitrary
   array map's Jacobian. The mathematical chapters and `Activation` docstring
   already indicate a scalar activation, so this is a documentation clarification,
   not an additional demonstrated implementation defect.
2. If the structural checker is expanded, cover optional Markdown link titles
   and `from . import submodule`. Its current AST logic checks the containing
   package for that relative-import form, not whether each imported name exists;
   dynamic imports and general runtime behavior are also outside its checks.
   No such missing dependency was found in the actual input. A full Markdown
   parser, security sandbox, or mathematical verifier is not required for this
   deliberately limited tool.

## Mathematical proof checks

These are reviews of the real-arithmetic arguments. Passing floating tests is
supporting evidence, not their proof.

| Source / claim | Check and conclusion |
| --- | --- |
| `docs/NOTATION.md`, forward model and initialization | Shapes and conventions agree across docs/API: `L` hidden matrices, first input factor `1/sqrt(d)`, stored hidden weights with no extra forward factor, readout `1/n`. Initial entry variances are `1`, `1/n`, `1/n^2`. Gaussian draw order and explicit private RNG agree with the implementation and tests. R4 concerns floating evaluation order, not the algebraic formula. |
| `docs/finite_dynamics.md`, equations (1)–(3) | Starting from `delta=n*partial f/partial z`, first and hidden matrix derivatives are `delta*source.T/n`, with first source `x/sqrt(d)`, and the readout derivative is `h/n`. Multiplication by `2*r/m` and block mobilities `n*kappa_1,kappa_2,...,n*kappa_last` gives exactly (2). Frobenius rank-one products give all factors of `d` and `n` in (3). No residual or factor `2/m` belongs inside a kernel block. |
| Block PSD and dissipation, (3)–(5) | Each block is a Gram of the output derivatives weighted by a positive scalar mobility, hence PSD. With the output Jacobian `J`, `K=J D J.T`, `grad(loss)=2 J.T r/m`, and velocity `-D grad(loss)`. Thus `f_dot=-2 K r/m` and `loss_dot=-4 r.T K r/m^2=-||D^(-1/2) velocity||^2`. The integrated energy identity follows. Small floating negative eigenvalues from rounding are not a contradiction of this exact PSD statement. |
| Global finite-width flow existence, section 3 | Globally defined C2 scalar activations make the finite loss C2 and the flow vector field locally Lipschitz. The nonnegative loss and energy identity bound the squared speed integrated over every finite interval. Cauchy–Schwarz gives (6). At a hypothetical finite maximal time, the path is Cauchy in a metric equivalent to Euclidean distance since fixed-width mobilities are positive constants. It has a finite limit and the local ODE solution extends there. No bounded activation or GD stability assumption is needed. |
| Width-uniform finite-horizon bounds, section 4 | The energy displacement bounds control first Frobenius norm divided by `sqrt(n)`, readout RMS, and middle operator norms. With bounded activation derivatives, `abs(phi(z)) <= abs(phi(0))+b*abs(z)` closes the forward RMS induction. Transposed middle operator norms and derivative bounds close the backward induction. Cauchy–Schwarz bounds each kernel entry. Data, depth, dimension, activation functions, rates and horizon remain fixed in this argument. |
| Gaussian high-probability initial event | For first weights, squared Frobenius norm divided by `n` converges to fixed `d`; readout squared RMS tends to zero. A `1/4` sphere net can have cardinality at most `9^n`; approximation of both bilinear-form arguments costs a factor 2 in the operator norm. A fixed net form has variance `1/n`, giving the displayed `2*9^(2n)*exp(-n*M^2/8)` bound. A sufficiently large fixed `M` and fixed-depth union bound work. Bounded initial activations/readout then bound initial loss. This establishes no nonlinear population identification. |
| `docs/gaussian_calculus.md`, equations (1)–(5) | Rowwise Gaussian orthogonal decomposition gives conditional mean `y*1.T/n` and remaining covariance `(1/n)P`. For `q=W.T*g(y)`, the mean is the random finite-width `a_n*1` and covariance is `sigma_n^2*P`. Polynomial growth ensures the required Gaussian moments and LLNs. The displayed RMS coupling error vanishes, including `sigma=0`. Empirical weak convergence plus second-moment convergence gives quadratic Wasserstein convergence; coordinate matching transfers it to `q`. The Gaussian integration-by-parts boundary term vanishes under the stated growth assumptions on `g,g'`. |
| Two-direction conditioning, (6)–(7) | Compatibility `U.T*Y=R.T*V` makes the stated `M` satisfy both constraints. Homogeneous perturbations are exactly `(I-P_U)A(I-P_V)`. Both summands of `M` are orthogonal to that subspace, so it is the minimum-Frobenius-norm affine solution. Isotropic Gaussian projection gives the stated residual law and the new-query variance. Empty spans have the natural zero-projector interpretation. Adaptive extension requires the explicitly stated independent recorded roots and queries measurable from previous answers; then conditioning proceeds inductively on a fixed next linear query. No future-answer dependence, hidden observations, or stability of nearly singular limiting Grams is silently allowed. |
| Gradient-direction identities, (8) | `D_F F=||g||^2`; differentiating once gives `2*g.T*H*g`. Differentiating its three factors in direction `g` gives `2*T[g,g,g]+4*||H*g||^2`, using symmetric `H`. C3 regularity is sufficient for these identities. For constant positive-definite mobility, `theta=D^(1/2)q` gives the stated Euclidean-coordinate formulation. Residual factors must be differentiated when changing from the predictor's gradient direction to squared-loss physical time; these identities do not assert a convergent Taylor series or an exchange of width limits and derivatives. |
| Wick recurrence, (9), including singular covariance | A finite PSD covariance has a real square root `A`, so `X=A*G`. Gaussian integration by parts in independent standard coordinates gives `E[X_i P(X)]=sum_j Sigma_ij E[partial_j P(X)]`, with zero polynomial boundary terms. Removing one `i` leg gives multiplicity `alpha_j-1_(j=i)` exactly as implemented. Every surviving transition lowers total degree by two. Odd degree vanishes by central symmetry, and zero degree is one after validation. Rational inputs keep all operations exact. |
| Exact PSD validator | For pivot `a<0`, the first basis vector violates PSD. For `a=0`, any nonzero off-diagonal pivot row gives a negative quadratic form, so that row must vanish. For `a>0`, completing the square makes PSD equivalent to PSD of `C-b*b.T/a`. Recursion therefore correctly handles singular/zero covariances without tolerances or zero-pivot inversion. The code validates before any zero/odd-degree shortcut. |

The local Wick cache is freshly constructed per call and cleared in `finally`,
including exceptions during evaluation. No cross-call cached values are used.
The exponent-state bound and degree-based recursion bound are correct as stated.
The API explicitly targets small exact moments; this review does not require
unbounded recursion, rational bit sizes, or state counts.

## API and numerical boundary audit

Parameter construction, nonempty equal-width shapes, finite real arrays,
per-evaluation revalidation, activation sequences, label shapes, positive finite
kappas, and explicit seed validation were read and exercised through the
provided and independent tests. Mutation of parameter arrays is documented;
frozen dataclasses do not promise immutable array storage. GD returns independent
arrays and updates all blocks from the original state at ordinary scales.

Callback input and output copying is correct for the supported ownership
contract. Independent tests reused the same scratch array for both activation
value and derivative at depth three, overwrote callback inputs in place, reused
the callbacks across APIs, and mutated retained callback inputs after return.
Results agreed with pure tanh callbacks, and saved states/inputs remained intact.
Invalid shapes, complex/bool/nonfinite callback outputs were rejected. Mutating
unrelated external calculation state is expressly outside the callback contract.

Zero steps returned independent copies without running callbacks for Python
int/float, NumPy unsigned integer, and NumPy floating zero. They still rejected
invalid input/label/kappa structure. Nonzero unsigned steps fail as R1 describes.

The stable tanh and arctan derivative formulas avoid the advertised saturation
cancellation and premature squaring overflow in their representable range.
Scaled loss evaluation passed both a large finite mean-square and a smallest
subnormal squared-loss example. The supplied suite confirms rejection of an
unrepresentable loss and an unrepresentable sum of finite kernel blocks.
Existing mantissa/exponent assembly also successfully handles finite GD with
an unrepresentable velocity, and cancellation with a GD addend. These successes
do not address the earlier normalization losses in R2–R4.

Not counted as defects: arbitrary raw dot products that overflow or underflow,
floating Gram eigenvalues slightly below zero from rounding, derivatives whose
true standalone value is below float64 range, absence of a loss-decrease
guarantee for arbitrary GD steps, and absence of an infinite-width theorem.

## Actual test evidence

Runtime: **Python 3.10.12, NumPy 1.26.4**. This matches the sole pinned runtime
dependency and the documented Python 3.10+ requirement. Runs used one BLAS/OMP
thread and no bytecode output. Commands below run from the review root.

Provided checks:

```sh
TMPDIR=/tmp/pde-code-round3.HFZHf0 PYTHONDONTWRITEBYTECODE=1 \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 make check
```

Actual result: exit 0; `Library boundary and local links checked: 12 files.`;
`Ran 47 tests in 0.134s`; `OK`. The checker count is the 12 `.py`/`.md` input
files under `code/` and `docs/`, not the complete 14-file review inventory.
Its passing result checks selected source structure, dependencies and local
links. It supplies no evidence of mathematical correctness or floating-range
correctness beyond the tests that separately execute.

Independent checks:

```sh
TMPDIR=/tmp/pde-code-round3.HFZHf0 PYTHONPATH=code \
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python -B review_checks.py
```

Actual result: exit 1, as intended for assertions that expose current defects;
`SUMMARY: 7 passed groups; 15 failed counterexamples; 22 total`.

| Independent group | Actual result / scope |
| --- | --- |
| Unsigned GD steps | 4 failures; exact actual/expected values in R1 |
| Kernel normalization | 4 failures; each prematurely zero versus `2**-52` or `2**-53` |
| First-layer input normalization | 1 failure; zero prediction/loss versus `2**-52` and `2**-104` |
| Gradient normalization underflow | 4 failures; flow and GD, first and readout blocks, zero versus `-2**-50` |
| Gradient normalization overflow | 2 failures; finite flow/GD rejected before final scaling |
| Forward-mode derivative oracle | PASS: 18 networks, 238 parameter coordinates; widths 1/2/3, depths 1/2/4, input dimensions 1/4, four samples including duplicate/opposite/zero inputs. Independently propagated dual-number Jacobians check forward values, loss gradients, flow, simultaneous GD, every kernel block, output flow and numerical PSD. Activations include tanh, arctan and a shifted cubic. |
| Exact latent-polynomial oracle | PASS: 120 rational mixing matrices, dimensions 1–4, latent dimensions 1–3, degrees 0–8, plus 120 coordinate permutations. Polynomial expansion in independent Gaussian coordinates and scalar double-factorial moments provide an oracle independent of the covariance Wick recurrence. Singular matrices and signed correlations are included. |
| Exact principal-minor oracle | PASS: all 125 symmetric 2-by-2 matrices with entries in `{-2,-1,0,1,2}` and all 729 symmetric 3-by-3 matrices with entries in `{-1,0,1}`. Exact determinant enumeration classifies 43 as PSD. All 2,562 zero/odd/even-degree validation calls agree, plus three exact `1e-80` near-boundary cases. |
| Finite Gaussian conditioning algebra | PASS: 6 two-direction query configurations, including empty/full spans. The chapter's matrix formula agrees with independently formed vectorized affine Gaussian projection, its mean constraints and its residual projector. This bounded calculation supplements the proof; it does not test an adaptive width limit. |
| Callback ownership | PASS: depth-three shared value/derivative scratch buffer, in-place input changes, reuse across APIs, retained-input mutation after return, and unchanged parameter/input/label arrays. |
| Zero-step and domains | PASS: 4 zero-step scalar types, 4 invalid zero-step structures, 12 invalid callbacks, 12 exact-type rejections, and 4 accepted integer scalar types for exact moments. |
| Finite-scale controls | PASS: GD rescues an unrepresentable velocity; 5 signed/floating step types; exact large and subnormal scaled losses. |

The independent failures were also reproduced in small direct calls before
being collected into the retained script. No implementation fix was applied
to make either suite pass.

## Complete input hash manifest and read coverage

All coverage ranges below are inclusive and constitute a full read through EOF,
not keyword-only inspection. Total input: **14 files, 1,925 lines, 86,793 bytes**.
Every listed initial SHA-256 digest was checked again after testing and returned
`OK`. Review-generated files are separate from this input manifest.

| Input file | Read coverage | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `Makefile` | 1–9, full | 257 | `740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65` |
| `requirements.txt` | 1–2, full | 111 | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |
| `code/README.md` | 1–159, full | 7,765 | `756c5dcf19f358b64dad6dfaa450164b67e5f087c3b98274d2026574a3fa282d` |
| `code/pde/__init__.py` | 1–26, full | 611 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 1–342, full | 14,441 | `c588140c2dbb033f87a20bd8ce7db45bc8e2c37c1f4fbc8a419f0c5a97647192` |
| `code/pde/gaussian_moments.py` | 1–114, full | 4,464 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tools/check_library.py` | 1–100, full | 4,910 | `7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6` |
| `code/tests/test_finite_network.py` | 1–297, full | 15,154 | `a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931` |
| `code/tests/test_gaussian_moments.py` | 1–110, full | 5,179 | `9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea` |
| `code/tests/test_numerical_contract.py` | 1–145, full | 7,491 | `a9ec5463b086d61d25df41e55eb42db090b2a7d2615f555703be73d265fd071a` |
| `code/tests/test_library_boundary.py` | 1–58, full | 2,352 | `375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a` |
| `docs/NOTATION.md` | 1–98, full | 5,110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | 1–214, full | 8,355 | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `docs/gaussian_calculus.md` | 1–251, full | 10,593 | `6f2917573f0d55faa47c3652a3ccac1c72dbfead68c3931e0b90baba629ba550` |

Retained independent test artifact: `review_checks.py`, 457 lines, 20,768 bytes,
SHA-256 `291e2589cd6e00ac47e4b5412e892f28c0436c87abfaaaaa1c292e763a4d6613`.
This report is an output and is not included in its own input hash manifest.
