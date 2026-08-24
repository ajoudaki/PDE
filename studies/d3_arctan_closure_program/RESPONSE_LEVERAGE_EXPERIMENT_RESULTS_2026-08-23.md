# Results: column-response leverage and entropy

**Run date:** 23 August 2026.  The design and all decision thresholds were
frozen in `RESPONSE_LEVERAGE_EXPERIMENT_PREREGISTRATION_2026-08-23.md` before
either data set was generated.

## Reproducibility record

The coarse run used widths (128,256,512), four seeds per width, RK4 step
(0.02), horizon (4), four Hutchinson probes, and central perturbation
(2\cdot10^{-4}).  The independent numerical audit used the same seeds and
probes at widths (128,256), RK4 step (0.01), and perturbation (10^{-4}).
Both runs used script SHA-256
`df94b5aee0c47be9deed389b5ad1d8aa0bd77b8b31201209f541fec3a549bd02`.

The fine/coarse audit compared every recorded statistic on all eight paired
runs: **all 144 comparisons passed** the preregistered 10-percent symmetric
(or (10^{-3}) small-value absolute) tolerance.  The numerical verdict is
therefore eligible to be read under the frozen rules.

Raw and derived records are in

- `experiment_response_leverage_2026-08-23.jsonl`;
- `experiment_response_leverage_fine_2026-08-23.jsonl`;
- `experiment_response_leverage_summary_2026-08-23.json`.

## Frozen summary statistics

Each entry is the median across four seeds of the maximum through the stated
horizon.  Slopes are least-squares slopes of log median against log width.

| horizon | statistic | (n=128) | (n=256) | (n=512) | slope |
|---:|---|---:|---:|---:|---:|
| 2 | response Frobenius | 0.6384 | 0.5563 | 0.6574 | 0.0211 |
| 2 | inverse participation | 12.311 | 13.046 | 10.972 | -0.0831 |
| 2 | top-one-percent mass | 0.3877 | 0.3080 | 0.2424 | -0.3387 |
| 2 | entropy ratio | 0.3515 | 0.3269 | 0.2932 | -0.1309 |
| 4 | response Frobenius | 1.2665 | 1.7625 | 1.4199 | 0.0825 |
| 4 | inverse participation | 56.873 | 49.123 | 105.701 | 0.4471 |
| 4 | top-one-percent mass | 0.8338 | 0.6691 | 0.9217 | 0.0723 |
| 4 | entropy ratio | 0.7352 | 0.6607 | 0.6896 | -0.0462 |

At horizon (1), for reference, the Frobenius slope was (0.1340), the
inverse-participation slope was (-0.0117), and the width-512 top-one-percent
mass and entropy ratio were (0.1672) and (0.1577), respectively.

## Preregistered verdict

The formal verdict is **evidence against delocalization**.

Two independently frozen rejection conditions trigger at horizon (4):

1. inverse participation has slope (0.4471\ge0.30) and its width-512 median
   is (105.701>8);
2. the width-512 top-one-percent mass is (0.9217>0.35) and exceeds its
   width-128 value (0.8338).

The Frobenius rejection condition does *not* trigger: its horizon-4 slope is
only (0.0825).  Thus the experiment distinguishes two claims which must not
be conflated.  It is evidence that the canonical column response becomes
strongly concentrated on a small set of rows by time (4), but it is not
evidence that its total Frobenius norm diverges with width.  Indeed, the
observed total norm remains compatible with the desired width-uniform
response estimate over these widths.

## Proof consequence

The proposed proof invariant “propagate diffuse row leverage of the column
response” is rejected.  In particular, a proof cannot assume bounded IPR,
small top-percent mass, or near-uniform row weights throughout a fixed
compact interval.  This agrees with the exact entropy audit: entropy and
fixed Rényi/IPR functionals do not form a closed restartable state for the
coupled tangent.

No theorem claim is upgraded or falsified by this experiment.  The surviving
mathematical target is a norm estimate that tolerates localization—most
plausibly a target-specific covariant/projected response, a signed
conditional-regression estimate, or a localized-energy estimate whose rare
active rows are controlled jointly with their Gaussian coefficients.
