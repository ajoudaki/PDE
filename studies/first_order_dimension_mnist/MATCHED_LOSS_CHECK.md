# Independent matched-training-loss check

Scoped numerical checker: `/root/matched_loss_check`, 2026-09-15. This checks the
new saved-snapshot comparison in the existing `first_order_dimension_mnist`
study. No training, GPU work, external source retrieval or promotion was
performed. Inputs are the complete `RUN.py`, `VALIDATION_ANALYSIS.py` and
`REPORT.md`, and the six `main4096/{network,closure}_{1729,2718,3141}`
`observations.npz`, `summary.json` and `config.json` files. Shared workflow and
the applicable investigate-conjectures skill/reference instructions were read.
The independent raw-array computations below were completed before reading
`MATCHED_LOSS.py` or its generated output.

## Frozen comparison and direct recomputation

The network reference is the arithmetic mean of the three actual networks'
1,000 raw validation predictions at T=600. The loss target is the arithmetic
mean of their three individual final training MSEs over all 10,552 training
rows. Each closure selects the saved time minimizing the absolute difference
between its training MSE and that target. Selection uses neither validation
outputs nor fitted scaling. The comparison at T=600 uses the same reference.

All six saved clocks equal 0,10,...,600; all training/validation label arrays
agree exactly. MSE is recomputed from saved float32 predictions after conversion
to float64. The network final training losses are
`0.0066165568662395445`, `0.006675886804104055`, and
`0.006637167415556845`; their mean is `0.0066432036953001485`.
The training MSE of the network **mean predictor** is instead
`0.006592181749366867` and is not the selection target.

| Closure seed | Closest saved time | Training MSE | Relative target mismatch | Validation RMS at matched time | Validation RMS at T=600 |
|---:|---:|---:|---:|---:|---:|
| 1729 | 380 | 0.006648208123014116 | +0.07533% | 0.04371279725711765 | 0.05359793780246006 |
| 2718 | 370 | 0.006752851431044825 | +1.65052% | 0.043523081799070454 | 0.05205177467016982 |
| 3141 | 370 | 0.006645267586955264 | +0.03107% | 0.04511109342264451 | 0.05298223551075214 |

RMS is `sqrt(mean((closure - fixed_network_mean)**2))`. Mean individual RMS
falls from `0.05287731599446068` to `0.044115657492944195`, a
`16.56978675399171%` reduction. Relative RMS at the matched times is
4.47092%, 4.45152%, and 4.61394%. The corresponding mean absolute errors are
0.02831933, 0.02793791, and 0.02877251. The closure-mean versus network-mean
RMS falls from `0.05024256304035405` to `0.0409541835714318`.

Within-class Pearson correlations increase for each seed and class:

| Closure seed | Digit 3, matched | Digit 3, T=600 | Digit 5, matched | Digit 5, T=600 |
|---:|---:|---:|---:|---:|
| 1729 | 0.97336224 | 0.95735897 | 0.95784498 | 0.94182080 |
| 2718 | 0.97711577 | 0.96602209 | 0.95549055 | 0.93770443 |
| 3141 | 0.97353815 | 0.95993921 | 0.95443037 | 0.94112400 |

This is an empirical improvement in average output discrepancy. It is not
uniform improvement: the largest matched individual error is 0.38704892,
versus 0.35555075 at T=600. Sign disagreements are 2,4,4 at the matched times
versus 2,4,3 at T=600. The matched comparison changes physical time and does
not supersede the distinct same-physical-time result or establish equality of
hidden dynamics, a convergence rate, or accuracy beyond these runs.

## Snapshot-spacing sensitivity

Each closure's recomputed training losses are strictly decreasing over the
61 saved times. The target is bracketed by T380/T390 for seed1729 and
T370/T380 for seeds2718 and3141. Direct output RMS at the nearest saved time
and its immediate neighboring times is:

| Closure seed | Earlier neighbor | Matched time | Later neighbor |
|---:|---:|---:|---:|
| 1729 | T370: 0.04367534 | T380: 0.04371280 | T390: 0.04385540 |
| 2718 | T360: 0.04362023 | T370: 0.04352308 | T380: 0.04353729 |
| 3141 | T360: 0.04525940 | T370: 0.04511109 | T380: 0.04507009 |

All these saved snapshots improve RMS relative to their respective T=600
closure output. The maximum within-seed RMS range is below 0.000190. The
conclusion is therefore insensitive to the immediate neighboring saved
snapshots, although exact loss equality is unavailable on this time grid.
Replacing the common target by each paired network's own final training loss
selects the same three saved times; matching equal seed numbers is merely a
sensitivity check and does not couple network/closure initializations.

## Check method and provenance

The checker loaded only the explicitly allowed raw arrays and computed all
losses, snapshot choices, residual norms and within-class correlations directly
using NumPy float64. It imported no study analysis or metric functions. A
second calculation used Python `math.fsum` of scalar squared residuals for
training losses and Python `min` for each seed-specific target, confirming
the selected times independently of the vectorized implementation. The
retained numerical evidence is
[`independent_metrics.json`](../../data/generated/first_order_dimension_mnist/matched_loss_check/independent_metrics.json),
including SHA256 hashes of all 18 raw run input files, loss values, individual
metrics, class metrics, and immediate-neighbor diagnostics. The command used
`/home/amir/miniconda3/bin/python -B` from `/home/amir/Codes/PDE`.

The numerical check reproduces this analysis from retained observations. It
does not retrain the six upstream models, reconstruct their checkpoints or
independently verify image IDs against the source dataset, which were outside
the scoped inputs. Existing producer checks are not repeated or independently
endorsed here.

## Completed source/export correspondence audit

**PASS for the saved-data analysis scope.** After freezing the independent
results above, the checker read all of `MATCHED_LOSS.py` and checked its
`matched_loss4096_001` outputs. The source selects solely by training MSE and
plots the unmodified saved validation outputs against the fixed T600 network
mean, with shared axes and no output calibration. The rendered scatter was
also inspected: both panels retain all three closure seeds, correct class
colors, the identity line, and the stated times and average RMS values.

An independent scalar-sum oracle checked 1,887 reported numerical values:
individual, within-class, ensemble, all nine closure/network pairs, individual
network-loss targets, both saved snapshots bracketing each target, and
network/network RMS. It used `math.fsum` for residual means and second moments
and the covariance formula for correlation, importing no study metric or
matching functions. The maximum absolute discrepancy was
`3.3306690738754696e-16`, below the declared `1e-12` check tolerance.
All nine individual-network-loss targets retain the same selected closure
times as the common target.

Every prediction, label and selected time in `sample_predictions.npz` agrees
exactly with raw inputs and direct recomputation. All 1,000 rows and all 11
non-ID columns in `validation_samples.csv` agree exactly with those values;
its column names correctly encode T600, T380 and T370. Exported IDs agree
exactly between CSV and NPZ and are unique; source-dataset ID correctness
remains outside this checker’s assigned scope.

All recorded input/source hashes were checked, including the plan hash as
metadata. Run configurations equal the embedded summary configurations and
have the assigned width, model, seed and digit pair. The inspected source
SHA256 is
`97b595a44ddc24b98ca126021541203656c7236d6f4487689f2c5e1d2f93a15b`.
[`export_audit.json`](../../data/generated/first_order_dimension_mnist/matched_loss_check/export_audit.json)
retains the check count, tolerance, maximum discrepancy, source hashes and
hashes of all six generated artifacts. No unresolved numerical or export
correspondence defect was found in this scope. This PASS is an internal
postprocessing check, not a new upstream training reproduction or promotion.
