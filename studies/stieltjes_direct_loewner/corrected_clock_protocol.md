# Corrected common-clock Loewner experiment

Frozen after a numerical-validity pilot and before inspecting any independent
scientific-seed output.

## Correction and estimand

Feature time is `s`, not the argument of the target kernel. For each
antithetic pair, the raw kernel is

\[
g_{r,n}(s)=\tfrac12\{G_{r,+}(s)+G_{r,-}(s)\},
\qquad G=n\lVert\nabla f\rVert^2.
\]

The intended common-clock relation is

\[
y=F(s),\qquad K(y)=G(s)=G(F^{-1}(y)).
\]

Because the finite-width Gaussian ensemble has rare finite-time explosions,
this experiment does not estimate an ordinary finite-width expectation. It
uses the following explicitly declared robust, width-dependent typical proxy.

For a cutoff `C_n`, clip each paired scalar kernel to `[-C_n,C_n]`, form fixed
contiguous block means, and take their coordinatewise median:

\[
G^{(B,C)}_n(s)=\operatorname{median}_{b=1,\ldots,B}
 \operatorname{mean}_{r\in b}\operatorname{clip}(g_{r,n}(s),C_n).
\]

Then define

\[
F^{(B,C)}_n(s)=\int_0^s G^{(B,C)}_n(t)\,dt.
\]

This preserves the common-clock identity by construction. It is a typical-limit
proxy, not an ordinary expectation. The direct median-of-means of paired
`f(s)-f(0)` is retained only as a consistency diagnostic.

The finite-width initial offset is removed explicitly:

\[
K^{\rm corr}_n(y)=111+G_n(F_n^{-1}(y))-G_n(0),
\qquad
R_n(x)=\frac{K^{\rm corr}_n(\sqrt x)-111}{x}.
\]

## Validity-only pilot

Pilot seed base `2026081301`, widths `(64,128,256)`, pairs `(24,16,8)`,
`s_max=0.003`, and RK4 step `0.00005` were used only to establish reachability.
No pilot trajectory escaped. At `s=0.003`, the integrated median output ranges
were respectively `0.2004`, `0.2849`, and `0.2535`. Pilot observations are not
included in any scientific estimate or confidence calculation.

## Frozen independent scientific design

- Output nodes:
  \(y=(0.04,0.08,0.12,0.16)\), hence
  \(x=y^2=(0.0016,0.0064,0.0144,0.0256)\).
- Widths and independent antithetic-pair counts:
  `(64:140, 128:70, 256:70)`.
- Simulations are stored in batches of 35 pairs. Batch seed bases are
  `2026081401`, `2026081402`, ...; no pilot seed is reused.
- Feature-time range `0 <= s <= 0.003`; primary RK4 step `0.00005`.
- First half of each width is discovery; second half is confirmation. Both
  halves have sizes divisible by 5 and 7.
- Primary robust specification: `B=7` blocks and
  `C_n=111*sqrt(n)`.
- Blocking sensitivity: `B=5`, same cutoff.
- Cutoff sensitivity: `C_n=111*n`, with both `B=7` and `B=5`.
- A state reaching component magnitude `1e12` is marked escaped; its subsequent
  positive kernel values are represented by the declared scalar cutoff. Raw
  escape and clipping counts are reported.

## Clock elimination and diagonal estimation

The robust `G(s)` is integrated on its uniform grid by composite Simpson rules
(with a local trapezoid/3/8 completion). The resulting strictly increasing
`F(s)` is the only map used to eliminate feature time.

For stable diagonals, set `X=F(s)^2` and

\[
R_{\rm raw}(X)=\frac{G(s)-G(0)}{X}.
\]

Fit `R_raw` on the frozen output window `0.02 <= F(s) <= 0.18` in a Chebyshev
basis. The primary degree is 3; degrees 2 and 4 are interpolation sensitivities.
Evaluate the fit and its analytic derivative at the four frozen `x` nodes.
These give both Loewner matrices, including

\[
A_{ii}=-R'(x_i),\qquad B_{ii}=R(x_i)+x_iR'(x_i).
\]

The fit RMS and maximum residuals are reported. Failure to bracket every output
node, nonmonotone `F`, or strong degree instability makes the result
inconclusive.

## Frozen inference and uncertainty

For each width, the primary discovery proxy selects the minimum-eigenvalue
unit vector separately for `A` and `B`. That vector is then fixed. The primary
confirmation half supplies its quadratic form. Pair bootstrap resampling of
the confirmation half (`5000` deterministic resamples) recomputes the complete
median-of-means, clock elimination, fit, and matrix. A negative direction is
called empirically confirmed only when its one-sided percentile upper bound is
below zero after Bonferroni familywise level `0.01` across six width-by-matrix
tests, and the sign survives all blocking, cutoff, and polynomial-degree
sensitivities.

This remains finite-width empirical evidence. It is not an interval-arithmetic
certificate, a proof of the limiting matrix sign, or a proof/disproof of the
Stieltjes conjecture.

Conditioning diagnostics are eigenvalues, minimum eigenvalue divided by trace
and spectral norm, the lowest eigengap, discovery bootstrap eigenvector angles,
fit residuals, and sensitivity scores.

## Numerical validity and controls

The first 35-pair batch at each width is rerun with RK4 step `0.000025`. Primary
and half-step proxy matrices are compared with the confirmation bootstrap
scale. Direct paired `f` increments are compared with integrated `G`.

At the same output nodes, exact normalized controls are:

- two atoms: weights `(0.6,0.4)`, nodes `(10,100)`;
- three atoms: weights `(0.5,0.3,0.2)`, nodes `(5,40,160)`.

They test matrix signs, diagonals, and expected rank deficiency only.
