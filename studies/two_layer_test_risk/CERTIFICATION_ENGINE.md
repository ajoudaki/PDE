# Arithmetic engine for a certified fixed-coefficient calculation

Author: `certification_engine`, 2026-09-10. This is approach B of the reopened
study, under the user's request to resolve the previously open sign. It changes
neither model nor witness. The engine evaluates the exact scalar expectations
in `CUBIC_DERIVATION.md`; it supplies no network trajectory or empirical training
claim. Root owns final integration/error propagation and the current README.

## Exact reduction of the costly integral

Training slots are 0,1,2 and passive slot is 3. Put `H_i=tanh(Y_i)`,
`d_i=1-H_i^2`, `dd_i=-2H_i d_i`, and `S=sum_a p_a H_a`.
Take any exact dyadic factor `Lhat` with training rows supported on its first
three columns. Conditional on the first three independent standard normals,
the training quantities are fixed and

`Y_x = m + sigma gamma_4`.

The only needed conditional passive quantities are

`A=E_4 H_x`, `B=E_4 d_x`, `C=E_4 dd_x`.

The seventeen distinct dynamic outer moments are

- `E[S^2 B d_b]`, three values (`dynamic_V`);
- `E[S A d_a d_b]`, six symmetric values (`dynamic_C`);
- `E[B d_a]`, three values (`dynamic_dd`);
- `E[S C]`, one value (`dynamic_ESdd`);
- `E[A dd_a]`, three values (`dynamic_Hdd`);
- `E[S A]`, one value (`dynamic_SH`).

These are direct conditional expectations of the original scalar formula.
For example `V_xb=E S^2 d_x d_b`, and the second group is the original
`C_ab=E H_x S d_a d_b`. The two reverse-response derivatives become

`E partial_i U_x = p_i E d_i d_x + 1_(i=x) E S dd_x`,

`E partial_i(H_x d_a) = 1_(i=x) E d_x d_a + 1_(i=a) E H_x dd_a`.

Thus neither matrix response is discarded. Training moments `E S^2`,
`E S^2 d_a d_b`, `E d_a d_b`, and `E S dd_a` use only the first three roots.
Lower moments remain the inexpensive two-root tensors `Q_ij`, `L_ab` and
`T_abij` from the exact cubic proof. No pair/triple-only factorization of the
entire coefficient was found: expanding `S^2 d_x d_b` genuinely includes four
distinct upper coordinates. Conditioning reduces work without altering that law.

## Finite-rule implementation and interface

The retained source is [certificate_kernel.cpp](certificate_kernel.cpp).
It uses normalized Gaussian trapezoid weights without mass renormalization.
The root's driver chooses and certifies the spacings, truncations, covariance
perturbation and circle quadrature. This engine only evaluates the chosen
finite sum. Its compiler contract is

```
g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off certificate_kernel.cpp -o OUTPUT
```

The source requires binary64, round to nearest, and at least 64 significand
bits in `long double`. It invokes no library exponential or hyperbolic tangent.
Parsing is checked independently: all received real inputs are echoed as exact
IEEE binary64 bit patterns. Every reported scalar is cast once from its
long-double accumulator to binary64 and returned as a bit pattern too. The
driver must compare echoed inputs with the intended dyadic inputs; a mismatch
invalidates the run. Integer counts are parsed separately.

Input tokens for mode `lower` are, in this order:

```
lower
m0 m1
h0 h1 normal_density_constant
eight direction entries, row-major (four rows, two coordinates)
```

Output arrays `Q_bits`, `L_bits`, and `T_bits` are row-major with respectively
16,16,256 entries, and the last tensor is ordered `(a,b,i,j)`.

Input tokens for mode `upper` are

```
upper
m0 m1 m2 m3
h0 h1 h2 h3 normal_density_constant
sixteen factor entries, row-major
p0 p1 p2
```

Its training arrays are `ES2_bits`, `V_bits`, `ddgram_bits`, `ESdd_bits`.
Dynamic arrays have the names displayed above with suffix `_bits`; symmetric
three-by-three arrays are returned as all nine entries. Training rows must have
zero fourth column. A zero passive fourth column may use `m3=h3=0`, which
omits that independent Gaussian exactly; training axes cannot be omitted.
Metadata includes parsed input bits, actual outer/total node counts, long-double
mantissa size, and finite one-dimensional rule masses.

The primitive-only mode takes `primitives`, an integer count, and that many
real values; it returns tanh for each and exp(-x) where `0<=x<=64`. This is for
fixed deterministic arithmetic checks, not coefficient evaluation.

## Elementary exponential and tanh enclosure

Write `u=2^-53`, the binary64 unit roundoff. For `0<=r<=64`, define
`s=r/256`, so `0<=s<=1/4`. The kernel evaluates the degree-twelve Taylor
polynomial of `exp(-s)` by Horner, then squares eight times. The coefficients
are reciprocals of exact integers `k!`, `0<=k<=12`; each computed coefficient
has relative error at most `u`. Multiplication by `1/256` is exact.

Here and below the elementary rounding model is used only for normal results;
the harmless tiny-input exception is covered explicitly below. If
`gamma_j=ju/(1-ju)`, induction on Horner's recurrence, expanding each operation's
factor `1+delta`, gives absolute evaluation error at most

`gamma_25 sum_(k=0)^12 s^k/k! <= (4/3) gamma_25`.

The last inequality follows from `sum s^k/k! <= sum s^k <=4/3`.
The alternating-series bound gives

`0 <= P_12(-s)-exp(-s) <= (1/4)^13/13!`.

Also `exp(-s)>=1-s>=3/4`. Consequently the initial relative error is at most

`delta_0 = (16/9) gamma_25 + (4/3)(1/4)^13/13! < 46u`.

Eight rounded squarings produce relative error bounded by

`(1+46u)^256 (1+u)^255 - 1 < 2e-12`.

The number 255 is the sum of the rounding-error multiplicities
`1+2+4+...+128`; the initial error has multiplicity 256. This proves the
kernel's relative bound `2e-12` for `exp_negative(r)`. The smallest final
exponential on this range is `exp(-64)>2^-93`, so squaring never approaches
underflow. Extremely tiny input `r` can make its division by 256 or a
multiplication inside Horner subnormal; each such absolute error is at most
`2^-1075`. Even pessimistically adding this at all 26 operations and
multiplying by 256 is smaller than
`2^-1060`, which is absorbed by the strict slack in `2e-12`.

For `|z|<=16`, the kernel substitutes `q=exp_negative(2|z|)` into

`tanh(z)=sign(z)(1-q)/(1+q)`.

The exact map in `q` has derivative of magnitude `2/(1+q)^2<=2` for `q>=0`.
Thus exponential error contributes at most `4e-12`. Rounding in the numerator,
denominator and division contributes less than `6u`; subtraction near zero
does not invalidate this absolute bound. Projection onto the correct interval
`[0,1]` cannot increase the error. For `|z|>16`, returning its sign has error
`2/(exp(2|z|)+1) < 2 exp(-32) < 3e-14`. Therefore the global absolute bound is

`|bounded_tanh(z)-tanh(z)| <= 5e-12`.

This proof depends on elementary rational inequalities and IEEE arithmetic,
not the accuracy of a platform `tanh` or `exp` implementation. Compiler fast-math
and fused contraction are excluded so that the stated operation counts apply.

## Uniform arithmetic enclosure for every reported moment

The following intentionally loose envelope is used by the driver:

> Every returned moment differs by at most `1e-9` from the exact finite
> tensor sum at the supplied exact dyadic root factors, spacings, directions
> and label coefficients, using exact tanh and the true normal density.

The envelope requires all of the following, checked by source or driver:

1. `0<h_j<=1`, `m_j<=200`, `m_j h_j<=9` for present axes;
2. factor and direction entries have magnitude at most two;
3. `sum |p_a|<=1`;
4. the supplied density constant differs from `1/sqrt(2pi)` by at most `1e-15`;
5. exact finite one-dimensional Gaussian masses are at most `1.000001`;
6. binary64 and long-double contracts above and finite intermediate/output values.

Condition 5 follows, for example, from the Gaussian infinite-trapezoid identity
in the accompanying error proof and `h<=1`; truncation only decreases mass.
The source reports its masses as an additional diagnostic, not as a replacement
for that bound. The radius and coefficient bounds give Gaussian node magnitudes
at most nine and exact dot-product absolute sums at most 72. Node multiplication
and at most seven dot-product operations change each preactivation by less than
`1e-13`. The derivative bound `|tanh'|<=1` therefore enlarges the primitive
activation bound to at most `6e-12` at an exact quadrature node. Direct expansion
of `d=1-H^2`, `dd=-2H+2H^3` on `[-1,1]` gives errors at most `1.3e-11` and
`2.6e-11`, including their displayed arithmetic operations.

Each Gaussian exponent differs from its exact node exponent by at most
`1.5e-14`: forming a node, squaring it and dividing by two uses the bound
`3u * 81/2` with slack. Since `exp(-x)` has relative sensitivity one, the
primitive exponential, two weight multiplications, and the density-constant
error give a relative weight error below `3e-12`. A product of four weights
has relative error below `1.3e-11`, including the actual product operations.

For completeness, the real integrands contain only `H,d,dd,S` with
`|H|,|d|<=1`, `|dd|<=2`, `|S|<=1`; `S` is a three-term weighted sum.
Every listed moment contains at most six such elementary activation/gate
factors after expanding `S` or `S^2`. The sum of absolute label coefficients
in these expansions is at most one. Multiplying telescopically, each product's
activation and gate error is less than `6*2.6e-11`, and arithmetic plus weight
error is less than `4e-11`. Hence `2e-10` bounds the pointwise-and-weight
contribution for every moment. The exact product rule mass is at most
`1.000001^4<1.000005`, so this contributes less than `2.00001e-10` in total.

The passive inner sums contain at most 401 terms and are accumulated in
long double. Outer sums contain at most `401^3=64,481,201` terms. With
long-double unit roundoff at most `2^-64`, the same elementary product-of-rounding
factors argument bounds total summation error by

`4 gamma_(64,481,201)(2^-64) < 1.5e-11`.

The factor four covers a bounded inner sum and its subsequent outer sum.
All remaining long-double products and the final binary64 cast contribute
less than `1e-13`; their multiplicands have the bounded magnitudes just stated.
This total is below `2.2e-10`, strictly below the declared `1e-9` enclosure.
Tiny underflowed summands are bounded in absolute value by `2^-1075` per
binary64 operation, or its still smaller long-double counterpart; even using
the maximal node count and 100 operations per node, their sum is far below
the `1e-13` slack. Overflow is excluded by the displayed finite ranges.

This arithmetic envelope is separate from Gaussian discretization/tails,
lower-law direction errors, upper covariance errors, algebraic propagation,
and the circle quadrature error. The final certificate must include all of them.

## Executed deterministic verification

The retained independent check source is
[check_certificate_kernel.py](check_certificate_kernel.py). The exact command,
from the repository root, was

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python -B studies/two_layer_test_risk/check_certificate_kernel.py --output data/generated/two_layer_test_risk/kernel_check_20260910_01
```

The fresh run completed successfully in 0.80 seconds. It compiled the engine
with the displayed flags using GCC 11.4.0, checked nineteen fixed primitive
inputs from -100 to 100 using an exact rational degree-forty alternating
series and directed 180-bit dyadic squaring oracle, and checked all lower
and upper moment contractions on one fixed supplied finite rule by an
independent direct NumPy tensor calculation. The primitive oracle verifies
elementary-function accuracy; the NumPy comparison verifies the finite-sum
contractions, without claiming certified NumPy elementary-function bounds.
It additionally exercised the omitted passive-root branch. This is an
implementation check on supplied states, not an evaluation of `chi`.

Maximum contraction discrepancy was `5.88418203051333e-15`, below `1e-9`.
All primitive enclosures passed; the largest observed exponential relative
error bound was `2.3531240982442e-14`, below `2e-12`. The binary reported
64 significand bits for long double. Python was 3.10.12, NumPy 1.26.4,
one numerical-library thread, x86_64 Linux. Exact command, environment,
per-primitive errors, per-contraction errors, input bits and output bits
are retained in the run's `result.json`, `primitive.json`, `lower.json`,
`upper.json`, `singular.json`, and `compile.log`.

Frozen source hash:
`9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9`.
Check-source hash:
`cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1`.
Compiled-binary hash:
`8c5b241801eaa4b8912989b9e404eb9693e63e94487661071c3bfa7044c189c7`.
These checks support this exact kernel version only. They do not replace
the analytic arithmetic envelope or any remaining integration-error proof.

## Cost and representation decisions

The diagnostic training factor has columns with maxima approximately
`0.628,0.101,0.374`; passive conditional standard deviation was at most about
`0.218` in the old non-certified outputs. These numbers are planning evidence
only. With a per-coordinate contour tolerance around `1e-9`, radius eight
and suitable anisotropic spacings, indicative node counts are `53,23,35,23`,
about 0.98 million four-root nodes per angle. Actual factors and certified
spacings determine the production counts. A passive row may enlarge any
column maximum, and no cost promise assumes it does not.

The inner loop evaluates only three conditional quantities; the seventeen
dynamic moments are accumulated after it. Exact reflection and antipodal
symmetries, when justified by the driver's angle argument, reduce the number
of distinct angles by a factor close to four. No favorable teacher or dataset
is selected. No coefficient execution was performed while drafting this plan.

Installed `libmpfr.so.6` and `libgmp.so.10` were found, but their development
headers and Python ball-arithmetic wrappers were absent. The engine therefore
does not depend on them. Small constants and downstream algebra can be
enclosed by the driver's exact rational arithmetic. Cholesky is only a way to
choose a dyadic factor: the exact covariance is `Lhat Lhat^T`, and its residual
against the target covariance must be certified separately. No accuracy claim
for a floating solve or square root is imported.

## Reading and ownership

Read root `AGENTS.md`, the full workflow, the study README, complete
`docs/README.md` and `docs/NOTATION.md`, the exact coefficient source and
`QUADRATURE.md`, and all coefficient/response formulas in the complete
`CUBIC_DERIVATION.md`. The engine does not change or independently reprove the
population-flow theorem and does not call maintained APIs. It uses the
previously derived coefficient as its exact mathematical input; final research
synthesis must retain that input's complete dependency/proof checks.

Required skills read: `solve-math-rigorously` and `investigate-conjectures`,
including research-contract, evidence-ledger, adversarial-audit,
decisive-experiments and proof-search-orchestration references. This is an
author subtask, not an isolated promotion review. Initial resumed HEAD was
`df1117948764a984e7fd2d28949a3c87bc284f84`; concurrent edits were preserved.
This author writes only this file and the separately assigned engine/test
sources. Root remains sole README editor and Git writer.
