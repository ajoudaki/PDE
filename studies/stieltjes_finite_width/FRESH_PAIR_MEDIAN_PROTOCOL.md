# Frozen fresh-seed pair-median calibration test

Status: **preregistered; not yet run**.  This file was written before any of
the fresh initialization seeds below were inspected.

## Decision being tested

The earlier median-of-block-means estimator reproduced the exact intercept
after an initialization-jet control variate, but failed on the held-out next
coefficient because the fifth-order per-pair jet has a very heavy positive
tail.  A post-hoc diagnostic suggested that the median across individual
antithetic pairs may estimate the intended typical mean-field coefficient.

This test asks only whether that estimator passes an independent fresh-seed
local calibration.  It does **not** inspect Loewner matrices and it does not
simulate positive-time trajectories.

## Canonical initialization and per-pair observable

For each width `n` and fresh pair index `r`, independently sample

\[
a_i,u_j,W_{ij}\sim N(0,1),
\]

and evaluate the exact order-five ordinary Taylor jet under

\[
z=n^{-1/2}Wu^2,\qquad f=n^{-1}\sum_i a_i z_i^2,
\]

\[
a'=z^2,\qquad
W'=2n^{-1/2}(az)(u^2)^\top,\qquad
u'=4n^{-1/2}u\odot W^\top(az).
\]

The pair consists of `(a,W,u)` and `(-a,W,u)`.  Their averaged jet removes
the odd-in-`a` finite-width terms exactly.  If

\[
f_r(s)=f_{r,1}s+f_{r,3}s^3+f_{r,5}s^5+O(s^7),
\]

then the per-pair estimate of the held-out coefficient is

\[
q_{r,n}
=\frac{5f_{r,5}}{111^4}
-\frac{2(842592)^2}{3(111)^5}.
\]

The target value, fixed before the run, is

\[
q_*=-\frac{38443196932}{5616860517}
=-6.844249882233634\ldots.
\]

No positive-time data and no fitted global curve enter this statistic.

## Frozen sample sizes and seeds

- Widths: `128` and `256`.
- Fresh antithetic-pair count: `224` at each width.
- Pair-generation seed rule:
  `SeedSequence([91723651, width, pair_index])`.
- Bootstrap seed rule:
  `SeedSequence([410927, width])`.
- The two widths therefore use independent samples; no prior pilot or
  trajectory seed is reused.

The old exploratory width-256 percentile interval had width approximately
`16.83` with 70 pairs.  Under the standard `N^{-1/2}` uncertainty projection,

\[
16.83\sqrt{70/224}=9.41,
\]

so 224 is the smallest convenient count with a modest margin below the frozen
maximum width 10.  The same count at width 128 gives a direct finite-width
consistency check without allocating a larger secondary experiment.

## Primary estimator and confidence interval

At each width, the primary estimate is the ordinary sample median of the 224
values `q_r,n`.

The primary 95% confidence interval is the exact distribution-free order-
statistic interval for a population median.  If `q_(1) <= ... <= q_(N)` and
`k` is the largest integer satisfying

\[
2\Pr\{\operatorname{Bin}(N,1/2)\le k-1\}\le0.05,
\]

the interval is

\[
[q_{(k)},q_{(N-k+1)}].
\]

A 10,000-resample percentile bootstrap interval is reported only as a
secondary diagnostic and cannot override the exact interval.

## Frozen gate

The gate passes only if all of the following hold:

1. At width 256 the exact 95% median interval contains `q_*`.
2. That width-256 interval has total width at most `10`.
3. The width-128 interval also contains `q_*`.
4. Both point estimates are negative.
5. Each point estimate is within `5` of `q_*`, and the two point estimates
   differ by at most `5`.

Classification:

- **Pass:** all five conditions hold.
- **Underpowered/inconclusive:** the width-256 interval contains `q_*` but is
  wider than 10.
- **Calibration failure:** the width-256 interval is at most 10 wide but
  excludes `q_*`, or any finite-width consistency condition 3--5 fails.

There is no outcome-dependent increase in pair count.

## Branch and stopping rule

The run stops after writing the initialization-jet results.  It never starts
a trajectory simulation.  A pass merely authorizes a separately frozen,
fresh-seed positive-time common-clock/Loewner protocol; it is not itself
evidence for the Stieltjes conjecture.  A non-pass prohibits that branch.

## Resource and reproducibility constraints

- At most six BLAS/OpenMP threads.
- Process address-space limit: 8 GiB.
- Jets are generated in batches of eight pairs and only the scalar per-pair
  coefficients are retained.  The estimated live dense-array footprint at
  `n=256` is below 0.2 GiB.
- Output includes all 448 scalar pair statistics, summaries, exact interval
  indices and coverage, source hashes, peak RSS, Python/NumPy versions, and
  the frozen seed rules.

Frozen command, to be run only after approval:

```bash
OPENBLAS_NUM_THREADS=6 OMP_NUM_THREADS=6 MKL_NUM_THREADS=6 \
python studies/stieltjes_conjecture/numerics/finite_width/run_fresh_pair_median.py
```
