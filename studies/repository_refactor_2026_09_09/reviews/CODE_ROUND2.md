# Isolated adversarial library audit

**Verdict: NOTCLEAN.** Three required numerical/API fixes remain. The supplied
36 tests and the structural checker pass, but additional bounded tests expose
two avoidable scaling failures and a distinct GD composition failure. One
failure silently returns a kernel approximately 291 orders of magnitude too
small. No mathematical normalization error or exact rational moment error was
found in the inspected material.

## Scope and execution

The sole inspected input tree was `/tmp/pde-code-round2.GpEWZi`. All 13 input
files were read in full: every implementation, test and tool, all three math
documents, the README, Makefile and requirements. Total coverage is 1,752 lines
and 77,793 bytes. The exact file manifest appears below.

No repository, history, other review, web resource, agent, study, or outside
source file was consulted. No package was installed. Tests used the existing
Python 3.10.12 and NumPy 1.26.4 runtime, matching the pinned NumPy requirement.
Commands ran from the isolated directory with bytecode writing disabled;
numerical runs used one BLAS/OpenMP thread. Additional tests ran from standard
input, with results on standard output and no generated data files. Checker
probes substituted source text in memory without executing the substituted
imports. This review is the only added file; input hashes were checked again
after the tests and after writing the review.

These findings concern the candidate reusable library itself. They require no
study reproduction or changes to chapters outside this bundle.

## Required fixes

### R1 — P2: forming `n*kappa` first rejects finite flow velocities

Location: `code/pde/finite_network.py:261-267`, especially lines 263-264.

`flow_velocity` first stores the first/readout mobility in float64, then
multiplies it by the gradient. A valid finite multiplier can overflow when
multiplied by width even though the requested velocity is finite. It also
turns an exactly zero gradient into `inf*0`, rejecting a stationary state.

Reproducer, run with `PYTHONPATH=code python -B`:

```python
from pde import IDENTITY, Parameters, flow_velocity

p = Parameters(([[1.0], [1.0]],), [1.0, 1.0])
for label in (0.75, 1.0):
    try:
        print(flow_velocity(p, [[1.0]], [label], IDENTITY,
                            kappas=[1e308, 1e308]))
    except ValueError as error:
        print(label, error)
# Both calls: warnings and ValueError: weight 1 must be finite
```

Here `n=2`, `d=m=L=1`, both hidden coordinates and the prediction equal one,
and every output Jacobian entry is `1/2`. In the first call, `r=1/4`, so every
loss-gradient entry is `1/4`. Every exact velocity entry is therefore
`-(2*kappa)*(1/4) = -5e307`, a finite float64-scale result. In the second call
every velocity entry is exactly zero. Forward evaluation, gradients, and all
matrix products are finite in both calls.

Required change: compose width, rate and gradient with range-aware scaling,
or use an equivalently stable evaluation of the physical-flow formula,
without requiring the isolated `n*kappa` intermediate to fit float64. Retain
rejection when the final velocity actually overflows. Add regressions for
both nonzero and zero residuals, including both endpoint blocks. Merely
suppressing warnings or rejecting these otherwise valid `kappas` does not
restore the stated finite-positive-multiplier API.

### R2 — P2: kernel factor order can silently erase a finite kernel

Location: `code/pde/finite_network.py:294-297`.

The first and middle blocks evaluate `kappa * source_Gram * delta_Gram` from
left to right. All Gram matrices can be representable while the first
elementwise multiplication underflows or overflows. The final finiteness
check cannot detect the resulting silent zero.

This exact binary example has no inaccurate or overflowing matrix product:

```python
from pde import IDENTITY, Parameters, kernel, kernel_blocks

p = Parameters(([[2.0**27]],), [2.0**511])
x = [[2.0**-27]]
kappas = [2.0**-1022, 2.0**-1022]
print(kernel_blocks(p, x, IDENTITY, kappas=kappas)[:, 0, 0])
print(kernel(p, x, IDENTITY, kappas=kappas)[0, 0])
```

Observed blocks: `[0.0, 2.2250738585072014e-308]`; observed total:
`2.2250738585072014e-308`.

The notation gives `h=1`, `delta=2**511`, input Gram `2**-54`, and delta Gram
`2**1022`. Thus the correct first block is

```text
2**-1022 * 2**-54 * 2**1022 = 2**-54
                                  = 5.551115123125783e-17.
```

The readout block is `2**-1022`, and the correctly rounded total is
`2**-54`. The implementation instead first forms `2**-1076`, rounds it to
zero, then multiplies by `2**1022`. No exception or nonfinite result exposes
the error.

The complementary overflow case was also reproduced:

```python
p = Parameters(([[0.1]],), [0.1])
kernel_blocks(p, [[10.0]], IDENTITY, kappas=[1e307, 1.0])
# Observed: RuntimeWarning, then ValueError: kernel blocks must be finite
# Correct blocks are approximately [1e307, 1.0].
```

Here the input Gram is 100 and the delta Gram is approximately 0.01. Their
weighted product is finite, but `1e307*100` overflows first.

Required change: assemble the three finite factors with scaling that preserves
representable products, including zero entries and signed off-diagonal
entries. Use the same approach for first and middle blocks. A fixed change
of multiplication order alone is not a general solution: other finite factor
combinations overflow or underflow in that order. Add exact-power-of-two
underflow regressions and complementary overflow regressions, checking both
individual blocks and the total. Keep rejecting genuinely overflowing totals.

The README's limitation at lines 75-77 explicitly concerns arbitrary matrix
products. R1 and R2 occur after well-behaved matrix products, in the library's
own scalar/elementwise normalization. They are not demands for correctly
rounded BLAS, arbitrary precision, or support for an unrepresentable output.

### R3 — P2: GD unnecessarily requires a representable unscaled velocity

Location: `code/pde/finite_network.py:278-283`.

`gd_step` calls `flow_velocity` before applying `eta`. This imposes the range
restriction of a different public operation on an otherwise finite GD update,
including the zero-step identity. This remains a problem after R1 is fixed:
in this width-one example the physical velocity itself really does overflow.

```python
from pde import IDENTITY, Parameters, gd_step

p = Parameters(([[1.0]],), [1.0])
for eta in (0.0, 1e-308):
    try:
        print(gd_step(p, [[1.0]], [0.0], eta, IDENTITY,
                      kappas=[1e308, 1e308]))
    except ValueError as error:
        print(eta, error)
# Each call observed: ValueError: weight 1 must be finite
```

The prediction and residual equal one, and both loss gradients equal two.
Thus the physical velocity is `-2e308`, which `flow_velocity` is right to
reject as a float64 return value. But the requested zero-step result is an
independent copy of `p`; the positive-step result has both entries near `-1`,
because `1 - 2*(1e-308*1e308)` is finite. All gradient and matrix computations
in this example fit float64.

Required change: evaluate the GD increment using the combined step, mobility,
and gradient factors without first constructing an overflowing velocity.
Provide the zero-step identity while maintaining the intended argument
validation and array-ownership contract. Add regressions distinguishing
`flow_velocity` rejection from successful small-step and zero-step GD. Keep
the simultaneous, pre-update-state semantics and final finite-value checks.

## Mathematical and normalization audit

### Finite network and flow

The symbolic implementation agrees with `docs/NOTATION.md` and
`docs/finite_dynamics.md`; the findings above concern floating evaluation:

| Quantity | Verified convention |
| --- | --- |
| First preactivation | `W1 @ X / sqrt(d)`; the code scales `X` first |
| Middle preactivation | `Wl @ h`, with no additional width factor |
| Readout | `readout @ hL / n` |
| Initialization variances | first `1`, middle `1/n`, stored readout `1/n**2` |
| Backward coordinate | `delta_l = n * partial f / partial z_l`, with no residual |
| Loss and gradients | `mean(r**2)` and gradient coefficient `2/(m*n)` |
| Mobilities | `n*kappa_1`, middle `kappa_l`, `n*kappa_(L+1)` |
| First kernel block | `kappa_1 * (X.T@X/d) * (delta_1.T@delta_1/n)` |
| Middle kernel block | `kappa_l * (h.T@h/n) * (delta_l.T@delta_l/n)` |
| Readout kernel block | `kappa_(L+1) * (hL.T@hL/n)` |
| Prediction/loss flow | `f_dot=-2*K*r/m`; `loss_dot=-4*r.T*K*r/m**2` |

The parameter derivatives in finite-dynamics equation (1) follow by the chain
rule and the Frobenius outer-product identity. Multiplication by `2r/m` and
the stated mobilities gives equation (2), including the different endpoint
and middle width factors. Pairing the output gradients gives equation (3).
The PSD argument is valid even for singular input Grams and arbitrary finite
data; no whitening or inverse is involved. The same pairing yields the
weighted energy identity (4)-(5), with the sign and factors 2 and 4 correct.

The global finite-width existence proof is valid for real C2 activations:
the finite loss is C2, its metric-gradient vector field is locally Lipschitz,
and the nonnegative-loss energy identity bounds the weighted path length on
every finite interval. Equation (6) makes the solution Cauchy at any putative
finite maximal endpoint. Positive finite-dimensional mobilities make that
metric equivalent to the ordinary metric, permitting local continuation.
Bounded activations are not needed for this argument, and it does not imply
GD stability.

The width-independent bounds correctly add bounded activation derivatives,
fixed depth/data and uniform initial norm/loss bounds. The forward induction
uses `|phi(z)| <= |phi(0)| + sup|phi'|*|z|`; the reverse induction uses middle
operator norms and readout RMS. Equation (7) supplies exactly the needed
increment bounds. The Gaussian initial event is consistent with the notation:
first squared RMS tends to `d`, readout squared RMS has expectation `1/n**2`,
and the two `1/4`-nets give the stated bound
`2*9**(2*n)*exp(-n*M**2/8)` for each middle operator norm. Fixed sufficiently
large `M` and fixed depth suffice. No unsupported infinite-width trajectory
theorem is inferred from these estimates.

### Gaussian calculus and exact rational moments

In Gaussian-calculus equations (1)-(5), conditioning each row on its row sum
gives the stated mean and orthogonal Gaussian remainder with entry variance
`1/n`. Consequently the transpose response has conditional mean `a_n*1` and
covariance `sigma_n**2*P`, with no missing factor of `n`. Polynomial growth
provides the required moments and integration-by-parts boundary control.
The displayed RMS coupling bound, followed by empirical second-moment and
weak convergence, supports the claimed quadratic Wasserstein convergence,
including `sigma=0`. The population distinction is maintained.

For equations (6)-(7), the compatibility condition makes `MV=Y` and
`M.T@U=R`; the homogeneous space is exactly
`A=(I-P_U) A (I-P_V)`. The given mean is orthogonal to that space. Isotropic
Gaussian conditioning therefore leaves exactly the projected independent
Gaussian remainder, and a new fixed/transcript-measurable query has scale
`||(I-P_V)v||/sqrt(n)`. The adaptive extension records the necessary
independent roots and nonanticipating query rule. No stability of nearly
singular limiting Gram inverses is claimed or established.

Equation (8) is correct: differentiating `2<g,Hg>` contributes
`2*T[g,g,g] + 4*||Hg||**2`. The constant positive-definite metric coordinate
change is also correct. The finite-order statements do not imply analyticity
or an interchange of limits and time derivatives.

The Wick implementation follows equation (9) exactly. Removing one occurrence
of coordinate `i` leaves `alpha_j - 1_(j=i)` pairing choices at coordinate
`j`; each term contributes that count times `Sigma_ij` and the remaining
moment. Every recursive edge lowers total degree by two. The proof via
`X=A*G` justifies Gaussian integration by parts for singular PSD covariance,
so nonsingularity is unnecessary. The rational square root need not exist:
only the proof uses a real square root; computation uses rational covariance
entries and Fraction arithmetic throughout.

The exact PSD validator correctly applies the zero-pivot/zero-row necessity
and positive-pivot Schur-complement equivalence. It preserves symmetry and
handles negative correlations, singular covariances and later zero pivots.
All covariance and power validation precedes the odd/constant shortcuts.
Accepted input data are copied into tuples, the result is a Fraction, and
the cache is local and cleared in `finally`. No defect was found in this
implementation or its mathematical proof.

### Callback and ownership audit

`_evaluate` passes a private copy to each callback and copies the validated
return value. Thus an in-place activation cannot overwrite stored
preactivations, and a shared output buffer cannot overwrite earlier hidden
states or derivatives. An additional test used the same scratch array for
both value and derivative callbacks at depths 1, 3 and 5. All eight public
evaluation/update operations agreed with ordinary ARCTAN, and parameters,
inputs, labels and retained results remained unchanged when scratch was
overwritten. This tests the documented ownership behavior; arbitrary mutation
of unrelated captured external state remains outside the callback contract.

The built-in stable tanh/arctangent derivative formulas and scaled mean-square
loss were checked against their stated formulas and supplied regressions.
Ordinary float64 matrix-product overflow/underflow and derivatives below
float64 range remain limitations; no all-extreme-input accuracy claim is
made on their behalf. The concrete required findings isolate additional
avoidable scaling failures beyond that documented matrix-product limitation.

## Test evidence and adequacy

Executed `make check`: the boundary checker reported 11 source/doc files;
all **36 supplied unit tests passed**. The two additional manifest files are
Makefile and requirements, which were separately read in full.

Additional bounded independent checks:

| Check | Method and outcome |
| --- | --- |
| 9 finite networks | Widths 1/2/3, depths 1/2/4, `d=4`, `m=3`; enumerated every identity-network input-to-output path as a rational monomial and differentiated each monomial independently. Outputs, loss, every gradient/flow/GD block and every kernel block agreed within `rtol=2e-13, atol=2e-15`. |
| 441 exact moments | Expanded `X=A*G` directly into independent scalar Gaussian powers for six rational loading matrices of dimensions 1-4 and all exponent vectors of total degree at most 6. Included negative entries, zero rows and deficient rank. Exact Fraction equality in every case. This reference did not use the Wick recurrence. |
| 1,728 PSD decisions | Enumerated symmetric 3-by-3 integer matrices with diagonals in `{-1,0,1,2}` and off-diagonals in `{-1,0,1}`. Compared constant-moment acceptance with all principal minors computed by the determinant permutation formula. Every decision agreed. |
| Callback composition | Shared, in-place value/derivative scratch across depths 1/3/5; forward, backward, loss, gradients, flow, GD and both kernel APIs all passed. |
| Extreme scalar factors | Reproduced R1, both R2 directions and both R3 steps. These expose failures despite the supplied suite passing. |
| Six checker probes | In-memory source substitutions confirmed rejection of an undeclared absolute import and a missing inline local link; confirmed acceptance of missing `pde`/relative submodules and a missing reference-style link; correctly ignored a link-shaped string in displayed math. |

The existing finite-difference Jacobian/gradient checks, weighted dissipation
checks, simultaneous-update hand calculation, normalization and batch tests
are useful independent evidence at ordinary scale. The exact-moment tests
cover the major algebraic and domain branches. They do not need campaign
outputs or external studies to function.

They are insufficient for the current numerical/API contract: no supplied
test combines a large positive mobility with a zero/small gradient, separates
a finite GD increment from an overflowing velocity, or combines finite Gram
factors whose intermediate scalar product loses range. Tests for R1-R3 are
required with the fixes. Preserve the existing rejection tests for genuinely
unrepresentable loss and total kernel; accepting silent zero/inf results is
not an acceptable resolution.

## Boundary checker: role and optional improvements

The checker correctly describes itself as structural, not a proof verifier.
It parses source without importing the implementation, checks selected
absolute-import roots and inline local Markdown links, and reports symlinks.
The current bundle's actual imports and local links were also manually
inspected; no present dependency on studies or files outside `code/` and
`docs/` was found. Makefile appropriately follows this limited check with the
unit tests. Passing either step cannot certify the mathematics or numerical
correctness, as R1-R3 demonstrate.

Optional, not blockers for the current input tree:

1. `code/tools/check_library.py:63-68` allows any `pde.*` name without resolving
   the submodule and ignores relative imports. The in-memory substitutions
   `import pde.missing_audit_module` and
   `from .missing_audit_module import value` both passed. Resolve local imports
   or document this as an allowlist lint, not a complete dependency closure.
2. Lines 40-54 only handle the selected inline-link syntax. A missing
   reference-style link passed the probe. Add reference-link coverage if that
   Markdown syntax is permitted; anchors, HTML and richer link syntax are
   also not comprehensively checked by this regex.
3. Lines 34-39 flag a symlink but do not immediately skip reading it. Source
   inspection shows a symlink to a `.py`/`.md` file can therefore be opened
   before failure is reported. Skip it immediately if the checker is intended
   to preserve a strict read boundary. No symlink was present and no external
   target was opened in this audit.
4. The moment implementation's recursive Python stack imposes a practical
   order limit beyond rational operation counts. The small-order scope and
   growth warning already make this nonblocking; documenting possible
   `RecursionError` or using iterative state evaluation would make the API
   limitation more explicit.

## Complete read coverage and exact input manifest

Every range below was read from its first line through EOF, including all
tests and prose. Byte counts and SHA-256 cover the original bytes, not a
normalized rendering. There were no symlinks. `REVIEW.md` is an output and is
deliberately excluded from the input manifest.

| Input | Lines read | Bytes |
| --- | ---: | ---: |
| `Makefile` | 1-9 | 257 |
| `requirements.txt` | 1-2 | 111 |
| `code/README.md` | 1-154 | 7,396 |
| `code/pde/__init__.py` | 1-26 | 611 |
| `code/pde/finite_network.py` | 1-307 | 12,615 |
| `code/pde/gaussian_moments.py` | 1-114 | 4,464 |
| `code/tests/test_finite_network.py` | 1-297 | 15,154 |
| `code/tests/test_gaussian_moments.py` | 1-110 | 5,179 |
| `code/tests/test_numerical_contract.py` | 1-92 | 4,455 |
| `code/tools/check_library.py` | 1-78 | 3,493 |
| `docs/NOTATION.md` | 1-98 | 5,110 |
| `docs/finite_dynamics.md` | 1-214 | 8,355 |
| `docs/gaussian_calculus.md` | 1-251 | 10,593 |

```text
740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65  Makefile
c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2  requirements.txt
3854a31c4c7e90ebbf45b174fd73f0a36efe0e5e7b3949302ca965d39578d5e4  code/README.md
65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3  code/pde/__init__.py
0c68f2f6a5cdbfd14d42e413f9e89863348218a4adb41129dcaabca22ef529c2  code/pde/finite_network.py
6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae  code/pde/gaussian_moments.py
a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931  code/tests/test_finite_network.py
9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea  code/tests/test_gaussian_moments.py
43d07e96ed30643c04663fcf9dbae4ffcb02ce31c6821378aac0f8b6ac47d434  code/tests/test_numerical_contract.py
07f65578fa0da04fb0738dd141ac591c0cd4f2116e3755e6de6c8bba12e757d1  code/tools/check_library.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c  docs/finite_dynamics.md
6f2917573f0d55faa47c3652a3ccac1c72dbfead68c3931e0b90baba629ba550  docs/gaussian_calculus.md
```

Release disposition: fix R1-R3 and add their regressions before treating this
candidate as clean under its stated numerical/API contract. The optional
checker improvements and high-order moment engineering are not substitutes
for those fixes.
