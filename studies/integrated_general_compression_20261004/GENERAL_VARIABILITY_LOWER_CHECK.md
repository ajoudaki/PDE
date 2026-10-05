# Integration check for the general dense variability lower bound

2026-10-04. Coordinator's internal mathematical and source-interface check,
not an independent promotion review. The user requested that only general
lower results enter the integrated theorem. No special endpoint theorem,
orthogonal geometry, or bounded-value activation assumption is used here.

## Frozen scientific inputs and assembled statements

The table preserves the names and hashes of the reviewed snapshots;
it does not bind the current edited files. The redundant sample-polynomial
statement has been removed. Its order formula is retained in
[LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md](LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md), (4),
and the consolidated interface is [RESULT.md](RESULT.md).

| File | SHA-256 |
|---|---|
| GENERAL_INNOVATION_LOWER.md | 7d614fbe45b13770b45d314eab9b4f3a5c1c43103060be70c64f13cf7a94c553 |
| GENERAL_ONSET_NONDEGENERACY.md | 9478903b5ad650d2c51265cc3fc9de2787d5d421f1c2dbb5567474b677b00508 |
| GENERAL_TRAJECTORY_LOWER_BRIDGE.md | 32da5b9db05797d5f5405c22ad708ecc0f74e4247aabe13ff16cfb9f448fd372 |
| GENERAL_TRAJECTORY_LOWER_BRIDGE_CHECK.md | 4c7107e0ad489fbd91f9d961798dfbba2e1d3ecd5831c0f3989fae279ead3737 |
| GENERAL_VARIABILITY_LOWER_RESULT.md | bd009395a1b5d6c53b798094f80dfeee3d64fdc90de4a14e32c4f9fab1d8ab92 |
| RESULT.md | eb039b9b9c006a8f68a3b56d8d05d6f2e2ab9fe9010861d6d54076b254218040 |
| SAMPLE_POLYNOMIAL_STATEMENT.md (reviewed snapshot; removed) | 049fa7094ce8d651bc8952fe26ea0fc660da955962552879a91eb1f88bde0900 |

The separate bridge reconstruction reviewed candidate
c6c53f4b062f29daaf1b7c0eaf427c354e6263a8a48322bf8db22a6777cc36a2.
Its two recorded corrections have been applied in the frozen final
bridge above:

1. The covariance differential (6) now has the required plus before
   its middle term.
2. Section 5 uses the latest quarter-log order under the simpler beta
   cap, retaining the earlier recurrence-based order for the larger
   common label allowance. Its optional finite-width inversion also
   uses the valid quarter-log exponent.

The original reconstruction is preserved as a report of its exact
reviewed candidate, rather than silently changing its source hash.

## Mathematical reconstruction

For a feature vector \(H\), \(Q=\mathbb E HH^\top\succ0\),
\(S=y^\top H\), and \(c=Qy\), the exact squared-area identity gives
\[
\|c\wedge H\|^2
=\|(HS-c)\wedge H\|^2
\le\|HS-c\|^2\|H\|^2.
\]
With \(A=\|c\|\), \(D=\operatorname{tr}Q-c^\top Qc/A^2\),
truncation at squared radius \(2\mathbb E\|H\|^4/D\) yields
\[
\operatorname{tr}\operatorname{Cov}(HS)
\ge\frac{A^2D^2}{4\mathbb E\|H\|^4}.
\]
Every denominator is positive for \(m\ge2\) and nonzero labels.
The equal Gaussian marginals give
\(\mathbb E\|H\|^4\le m^2\mu_4\) and
\(\operatorname{tr}Q=mq_L\).
Writing \(N=A^2D\), the spectral bounds
\[
N\ge(m-1)\gamma A^2,\qquad
N\ge\gamma^2(mq_L-\gamma)\|y\|^2
\]
give the claimed \(\gamma^3q_L\|y\|^2/(16\mu_4)\) lower floor.
The second bound is valid even at singular preactivation covariances:
it is algebra on the positive definite feature matrix \(Q\), not its
Gaussian precursor.

The last-layer innovation in the initialized Gram central limit theorem
is a positive semidefinite summand. Its contraction at one deterministic
training query has variance at least the trace divided by \(m\).
The two-copy onset normalization is \(8/m^2\), giving
\(\sigma^2\ge\gamma^3q_LY^2/(2m^2\mu_4)\). No cancellation with
earlier-layer innovations can decrease this floor.

The separate bridge check reconstructs the localized source event:
the finite-query proof replaces the frame union by a fixed query union
and reruns the mixed-response, continuity, pole and moment stops.
It does not infer a larger domain by restriction of the old event.
The permitted real time interval has length
\(\chi m/[\gamma\sqrt{\log(en)}]\), where the original source label
allowance gives a positive activation/depth-only lower choice of \(\chi\).
The simpler beta cap permits \(\chi=1\).
All of the original width gates are retained.

The Chebyshev derivative inequality supplies a factor
\(r/(2N^2)\), with \(N=O(\log(en))\), and exponentially small
polynomial-approximation remainder. Thus the powers are exactly
\[
\frac{m}{\gamma}\frac1{\log(en)^{1/2}}
\cdot\frac1{\log(en)^2}
\cdot\frac{\gamma^{3/2}Y}{m\sqrt n}
=\frac{Y\sqrt\gamma}{\sqrt n\log(en)^{5/2}}.
\]
The displayed coefficient \(1/128\) is a safe weakening of
\(1/(64\sqrt2)\). The fourth-moment ratio and \(\chi\) depend only on
activation/depth, because all original inputs have the same norm.

The Gaussian quantile \(\Phi^{-1}(1/2+\delta/4)\) leaves limiting
success probability \(1-\delta/2\); subtracting the vanishing source
failure and CLT errors gives eventual \(1-\delta\). This is a bound
at each individual sufficiently large width, not a simultaneous event
over infinitely many independent widths or a quantitative
growing-dataset theorem.

## Comparison and storage algebra

Both permitted Legendre baseline prescriptions bound the explicit
expression \(C_nq^{-2}\sqrt{\log(eq)}\) by \(Y/\sqrt n\).
For \(q'_n=\lceil q_n\log(en)^{3/2}\rceil\), the squared-order
ratio is at most \(\log(en)^{-3}\), while the square root of the
logarithm ratio is eventually at most two.
This proves error at most \(2Y/[\sqrt n\log(en)^3]\), and the
moving-state power stays \(5/4+o(1)\).
The sharper compact error \(n^{-1}e^{O(\sqrt{\log(en)})}\) plus its
endpoint tail is also little-o of the lower scale.

For every fixed failure tolerance, intersect the lower event with the
comparison events. On the intersection each relative error is bounded
by a deterministic sequence tending to zero. The failure tolerance is
arbitrary, proving convergence of both ratios to zero in probability.
Independence of these events is unnecessary. Ratios on a zero-denominator
event can be assigned arbitrary values: the lower bound shows that its
probability tends to zero. The conclusion concerns the ratio of complete
trajectory norms; it is not a pointwise or endpoint ratio.

The optional dense-family accuracy consequence is a necessary condition
only in the large-width regime. If its discrepancy is at most
\(\varepsilon\) with failure probability \(\delta<1/2\), intersect that
event with the lower event at the same failure probability. This gives
\[
n\log(en)^5\gtrsim_{\phi,L,\delta}Y^2\gamma/\varepsilon^2.
\]
For fixed task, monotonic inversion yields
\(n=\Omega(\varepsilon^{-2}/\log(1/\varepsilon)^5)\).
For example, if \(n\le\varepsilon^{-2}\), then
\(\log(en)=O(\log(1/\varepsilon))\); the complementary case is already
larger than the proposed bound. Since \(L\ge2\), dense parameter count
contains \((L-1)n^2\), yielding the stated fourth-power lower with
ten logarithms. This is not a representation or bit lower bound.

## Scope and validation

The general integration preserves arbitrary fixed depth, the same
layer-dependent analytic bounded-derivative activation class with
unbounded values, arbitrary sphere geometry with positive feature gap,
the original mean-loss normalization and physical times, and the existing
small-label allowance. Actual \(Y\) remains in every lower and error
amplitude. No empirical experiment or learned-population approximation
is used.

The lower is transient. Its use of a training query makes endpoint
cancellation explicit. It matches the dense upper in the width exponent
up to logarithmic/subpolynomial losses, but does not establish sharp
sample, dimension or conditioning powers. The \(m=1\) constant-feature
exception and zero labels are correctly excluded from the universal
positive statement.

Text checks found no control characters, balanced inline and display
math delimiters, and valid local file links in the new proof and
integrated statements. No new executable implementation or numerical
experiment needed testing. The separate final integration review is
recorded in GENERAL_LOWER_INTEGRATION_REVIEW.md.
