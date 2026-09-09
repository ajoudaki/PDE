# Frozen initialization-only order-13 typical-jet experiment

Status: **preregistered before any seed in this experiment is evaluated**.

## Purpose and claim level

The exact peeling computation now gives the deterministic mean-field feature
jet through order eleven and hence the exact Stieltjes moments
`mu_0,...,mu_4`.  Exact order thirteen is not yet computationally feasible.
This experiment provides a cheap, independent estimate of its scale.

It targets the median of a normalized finite-width initialization jet.  It is
not an estimator with a proved expectation interpretation, and it cannot
certify the Stieltjes conjecture.  Its only inferential role is:

1. verify the same estimator against the five exact lower coefficients;
2. estimate the next normalized coefficient on fresh seeds;
3. check whether that estimate lies on the positive or negative side of the
   exact next-Hankel threshold.

## Observable

For each independent Gaussian initialization, compute the ordinary feature
Taylor coefficients

$$
F_n(s)=\sum_{r=0}^6 a_{r,n}s^{2r+1}+\text{even powers}+O(s^{14})
$$

using the exact finite-width polynomial recurrence for the canonical feature
flow.  The antithetic pair `(a,W,u)` and `(-a,W,u)` removes every even power;
the odd coefficients are identical and therefore need only be evaluated once.

Since the first derivative is the weighted squared gradient norm,
`a_{0,n}>0`.  Define the dimensionless per-initialization ratios

$$
c_{r,n}=\frac{a_{r,n}}{a_{0,n}^{2r+1}},\qquad 1\le r\le6.
$$

If the finite-width jet self-averages to the audited mean-field jet, then

$$
c_{r,n}\longrightarrow c_r:=\frac{a_r}{111^{2r+1}}.
$$

The exact targets `c_1,...,c_5` are read from
`studies/stieltjes_conjecture/theory/certificates_order11.json`.  The next shifted
three-by-three Hankel determinant is nonnegative exactly when

$$
c_6\le c_{6,*}=5.376867065701546\times10^{-5}.
$$

The inequality reverses because the next Stieltjes moment `mu_5=-g_6`
decreases linearly with `a_6` when all lower coefficients are fixed.

## Frozen design

- Widths: `n=128,256`.
- Independent initializations: 512 at each width.
- Seed rule: `SeedSequence([2026081601,width,zero_based_index])`.
- Ordinary Taylor order: 13.
- No positive-time simulation.
- No seed from any earlier pilot, calibration, or Loewner experiment is used.
- The run is sequential, capped at four BLAS/OpenMP threads and 8 GiB address
  space.  Only six normalized scalars per initialization are retained.

## Primary intervals and frozen classification

For each width and each `r`, report the sample median and the exact
distribution-free 95% order-statistic confidence interval for the population
median.  Bootstrap intervals are not used.

The local calibration gate passes only if:

1. at width 256, the exact values of all `c_1,...,c_5` lie in their respective
   median intervals;
2. at width 128, the exact values of `c_4,c_5` lie in their intervals;
3. for every `r<=5`, the two width medians have the same sign as the exact
   target;
4. the relative difference between the two width medians of `c_5` is at most
   20%.

Conditional on that gate:

- **empirical positive-side signal:** the upper endpoint of the `c_6` median
  interval is below `c_{6,*}` at both widths;
- **empirical negative-side signal:** the lower endpoint is above `c_{6,*}` at
  both widths;
- **order-13 inconclusive:** otherwise.

If the calibration gate fails, the result is **uncalibrated/inconclusive**
regardless of `c_6`.  There is no outcome-dependent increase in sample size,
change of normalization, trimming, or seed reuse.

## Frozen command

```bash
OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
python studies/stieltjes_conjecture/numerics/finite_width/run_fresh_order13_median.py
```
