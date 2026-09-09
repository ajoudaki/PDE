# Frozen positive-time pair-median common-clock test

Status: **preregistered before positive-time simulation**.

The fresh initialization-only pair-median gate in
`FRESH_PAIR_MEDIAN_PROTOCOL.md` passed all of its frozen conditions.  This is
the separately frozen branch authorized by that result.  It tests a stopped,
individual-pair-median typical-flow proxy.  It is not an ordinary finite-width
expectation and cannot prove the Stieltjes conjecture.

## 1. Canonical model and same fresh pairs

For widths `n=128,256`, use exactly the 224 initialization pairs from the
fresh local test:

```text
SeedSequence([91723651, width, zero_based_pair_index])
```

Each pair is `(a,W,u)` and `(-a,W,u)`, with all unnegated coordinates iid
standard Gaussian.  Evolve

\[
z=n^{-1/2}Wu^2,\qquad f=n^{-1}\sum_i a_i z_i^2,
\]

\[
a'=z^2,\qquad
W'=2n^{-1/2}(az)(u^2)^\top,\qquad
u'=4n^{-1/2}u\odot W^\top(az).
\]

The feature-time kernel is the exact flow derivative

\[
G_{r,n}(s)=\tfrac12\bigl(f'_{r,+}(s)+f'_{r,-}(s)\bigr).
\]

Simulate `0 <= s <= 0.003` by RK4 with primary step `0.00005`.  The first 16
pairs at each width are also simulated with step `0.000025` solely for the
frozen step-halving check.

## 2. Stopping and initialization-only control variate

A raw trajectory is stopped if any state component is nonfinite or exceeds
`1e12`.  Its subsequent raw scalar kernel is set to the fixed cap `111*n`.
All raw scalar pair curves are clipped to `[0,111*n]` before aggregation.
The experiment is invalid if more than 5% of pairs stop, or if the median is
at the cap at any time.

From the exact order-five initialization jet, calculate each pair's constant
and quadratic kernel coefficients `c0` and `c2`.  Apply

\[
G^{\rm cv}_{r,n}(s)
=G_{r,n}(s)+(111-c_{r,0})+(842592-c_{r,2})s^2.
\]

Only the audited values `F'(0)=111` and `F'''(0)/2=842592` enter the control
variate.  The regenerated fifth-order jets must reproduce the archived fresh
local-test values to relative error at most `1e-12`.

## 3. Typical proxy and common clock

For any fixed subset of pairs, define

\[
G_n(s)=\operatorname{median}_r G^{\rm cv}_{r,n}(s),
\qquad
F_n(s)=\int_0^sG_n(t)\,dt.
\]

The integral uses cumulative composite Simpson rules on the uniform grid.
The output-coordinate kernel is defined only through the same clock:

\[
K_n(F_n(s))=G_n(s).
\]

Set

\[
R_n(x)=\frac{K_n(\sqrt{x})-111}{x},
\qquad
R(0)=\frac{280864}{4107}=68.386656927\ldots.
\]

Fit

\[
R_n(x)=R(0)+xq_n(x)
\]

on the primary window `0.02 <= F_n <= 0.18`.  The primary degree of `q` is
three.  Frozen sensitivities use degrees two and four and windows
`[0.02,0.16]` and `[0.03,0.18]`.

The four fixed output nodes are

\[
y=(0.04,0.08,0.12,0.16),qquad x=y^2.
\]

## 4. Local validity gates

The coefficient

\[
q(0)=-6.844249882233634\ldots
\]

was tested in the initialization-only experiment but is not imposed on this
positive-time fit.  The next coefficient is completely held out:

\[
q'(0)=
\frac{37578479127292096}{12802987609542045}
=2.935133601\ldots.
\]

Using all 224 pairs and 5,000 deterministic pair-bootstrap resamples:

1. the 95% interval for `q(0)` must contain its exact value and have width at
   most 10;
2. the width-256 95% interval for `q'(0)` must contain its exact value and have
   width at most 25;
3. the width-128 point estimate of `q'(0)` must be positive and differ from the
   width-256 estimate by at most 10;
4. changing fit degree from three to two or four may change `q(0)` by at most
   1 and `q'(0)` by at most 5;
5. the primary fit maximum residual must be at most `1e-5`.

Any failure makes every Loewner result **inconclusive**.

## 5. Loewner matrices

For `x_i` above, construct

\[
A_{ij}=-\frac{R(x_i)-R(x_j)}{x_i-x_j},
\qquad
B_{ij}=\frac{x_iR(x_i)-x_jR(x_j)}{x_i-x_j},
\]

with diagonal limits

\[
A_{ii}=-R'(x_i),\qquad B_{ii}=R(x_i)+x_iR'(x_i).
\]

Stieltjes representability requires both matrices to be positive
semidefinite.

Pairs `0,...,111` form discovery; pairs `112,...,223` form confirmation.  For
each width and each matrix, the discovery half fixes its minimum-eigenvalue
unit vector.  The confirmation statistic is that fixed vector's quadratic
form in the confirmation matrix.  Five thousand deterministic bootstrap
resamples of confirmation pairs recompute the entire median, common clock,
fit, and matrix while holding the discovery vector fixed.

The one-sided familywise level is 0.01 over four width-by-matrix tests, hence
each confirmation upper/lower percentile is evaluated at `0.0025/0.9975`.

An empirical **negative signal** is declared only if, for the same matrix
(`A` or `B`):

- the adjusted confirmation upper bound is below zero at both widths;
- every frozen degree/window sensitivity has a negative confirmation point
  score at both widths; and
- the ratio of absolute primary scores, width 256 over width 128, lies in
  `[0.25,4]`, excluding a visibly collapsing or exploding finite-width effect.

Empirical **finite-node compatibility** is declared only if the adjusted
lower bound is nonnegative for both matrices at both widths and every frozen
sensitivity score is nonnegative.  This is still not a proof.

Every other valid outcome is **Loewner-inconclusive**.

## 6. Numerical gates and controls

- Every clock must be strictly increasing and bracket `y=0.18`.
- On the 16-pair step-halving subset, the maximum relative corrected-kernel
  difference must be at most `1e-5`; the relative spectral difference of both
  Loewner matrices must be at most `1e-3`.
- No more than 5% of pairs may stop and the aggregate median may never hit the
  cap.
- Exact two-atom `(weights .6,.4; lambdas 10,100)` and three-atom
  `(weights .5,.3,.2; lambdas 5,40,160)` controls must have no eigenvalue below
  `-1e-10`; their expected rank deficiencies are recorded.

Failure of a numerical gate yields **invalid/inconclusive**, never evidence
for either sign.

## 7. Resources, seeds, and stop

- Six BLAS/OpenMP threads maximum.
- Eight-GiB process address-space limit.
- Simulation batches contain eight antithetic pairs.
- Local and confirmation bootstraps use frozen seeds
  `SeedSequence([731902,width,scope])`.
- All raw pair curves, jets, stopping data, fits, scores, bootstrap arrays,
  logs, source hashes, and peak RSS are preserved.
- The experiment stops after this report.  No additional nodes, time windows,
  widths, samples, or estimator changes are authorized by an observed result.

