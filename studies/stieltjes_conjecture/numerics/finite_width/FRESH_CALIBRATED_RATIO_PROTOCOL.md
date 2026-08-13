# Frozen fresh-seed calibrated adjacent-ratio experiment

Status: **preregistered before evaluating any seed below**.

## Motivation and scope

The raw normalized-jet median in `FRESH_ORDER13_MEDIAN_PROTOCOL.md` failed its
lower-order calibration gate and is not used.  Before that failed run, an
independent exploratory calculation had proposed a different estimator:
calibrate the next adjacent-coefficient ratio by the finite-width bias observed
in the preceding adjacent ratio.  Post-failure diagnostics confirmed that this
specific pre-existing construction is much more stable on the old data.

This protocol now tests it on completely fresh initializations.  It remains an
empirical estimator of a typical large-width jet, not a theorem about the
ordinary finite-width expectation and not a Stieltjes certificate.

## Frozen statistic

For each initialization, calculate

$$
c_{r,n}=\frac{a_{r,n}}{a_{0,n}^{2r+1}},\qquad c_{0,n}=1,
$$

and the adjacent ratios

$$
R_{r,n}=\frac{c_{r,n}}{c_{r-1,n}},\qquad1\le r\le6.
$$

Let \(M_{r,n}\) be the sample median of \(R_{r,n}\).  For \(2\le r\le6\),
define

$$
\widehat c_{r,n}
=c_{r-1}\frac{c_{r-1}}{c_{r-2}}
 \frac{M_{r,n}}{M_{r-1,n}},
$$

where every \(c_j\) on the right is the exact deterministic mean-field value.
The premise is that the leading finite-width multiplicative bias changes slowly
with derivative order and cancels in \(M_r/M_{r-1}\).

No regression, fitted exponent, trimming, clipping, or data-dependent
calibration constant is allowed.

## Frozen design

- Widths: 128 and 256.
- Fresh independent Gaussian initializations: 512 per width.
- Seed rule: `SeedSequence([2026081701,width,zero_based_index])`.
- Taylor order 13; no positive-time simulation.
- 20,000 paired nonparametric bootstrap resamples at each width.
- Bootstrap seed rule: `SeedSequence([2026081702,width])`.
- Four BLAS/OpenMP threads and an 8 GiB address-space cap.

The seed base differs from every earlier experiment.

## Frozen calibration and decision gates

For each \(\widehat c_r\), report the point estimate and the 95% percentile
bootstrap interval.

The estimator is calibrated only if all of the following hold:

1. the exact \(c_2,c_3,c_4,c_5\) lie in their respective intervals at both
   widths;
2. the point estimates of \(c_3,c_4,c_5\) have at most 5% relative error at
   both widths;
3. the two width estimates of \(c_6\) differ by at most 10% relative to their
   mean.

Conditional on calibration, compare \(\widehat c_6\) with the exact shifted
Hankel threshold

$$
c_{6,*}=5.376867065701546\times10^{-5}.
$$

- **Empirical positive-side signal:** both 95% upper endpoints are below the
  threshold.
- **Empirical negative-side signal:** both 95% lower endpoints are above it.
- **Inconclusive:** otherwise.

Calibration failure overrides every order-13 result.  The experiment stops
after this frozen analysis; there is no sample-size extension or estimator
change.

## Frozen command

```bash
OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 \
python studies/stieltjes_conjecture/numerics/finite_width/run_fresh_calibrated_ratio.py
```
