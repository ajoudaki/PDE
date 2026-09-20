# Finite dictionary scaling: results

Interim: discovery through p9 is independently checked; the predeclared fresh
confirmation stage is running. This report will be completed at the protocol's
terminal gate. Nothing here is promoted to the established book or code.

## Scientific target and interpretation

Approximate the same finite width-2048, two-hidden-layer tanh network's learned
function on the circle. Every predictor is evaluated at its own first detected
training MSE1e-3 crossing; the full reference is evaluated at its own crossing.
The canonical Gaussian initialization, actual small random readout, all-block
training, physical mobilities(n,1,n), unhalved loss and eight training inputs
are retained. Errors use8192 uniform circle angles, with a nested4096 check.
The maximum is a sampled maximum, not a certified continuous supremum.

The observable dictionaries use only initialized forward/reverse actions,
maintained Chebyshev words/tails and the frozen ridge schedule. Gaussian and
orthogonal controls have the same nested random spans and distinct frame
conditioning. Historical p1/3/5 errors below were recomputed against the newly
tightened full reference; old published error values were not spliced in.
Historical per-cell tolerances retain their authoritative selected levels.

The question is finite approximation efficiency versus dictionary budget.
A matched-budget error advantage and a smallest-tested-budget comparison are
different observations. Neither supplies an asymptotic exponent, a lower bound
on an untested budget, a universal ranking, a speedup or a population theorem.
Through p9, polynomial enrichment refines the same initialized coordinates;
it does not test the eventual full action-word hierarchy. The ridge also varies
with order, so these curves describe the complete frozen construction.

## Discovery: the advantage grows on one family and contracts on the other

The following are selected-coarser-level RMS errors; complete both-level RMS,
L1 and sampled-maximum tables are in the linked analysis. Better random means
the smaller error of the two distinct controls at that same budget.

| Case | p | Columns | Ours RMS | Gaussian RMS | Orthogonal RMS | Better random / ours |
|---|---:|---:|---:|---:|---:|---:|
| Paired cluster | 1 | 8 | 0.28493 | 0.65789 | 0.63239 | 2.219 |
| Paired cluster | 3 | 45 | 0.16551 | 0.55017 | 0.59801 | 3.324 |
| Paired cluster | 5 | 149 | 0.09412 | 0.48721 | 0.45508 | 4.835 |
| Paired cluster | 6 | 241 | 0.08696 | 0.39003 | 0.38906 | 4.474 |
| Paired cluster | 7 | 369 | 0.04998 | 0.31677 | 0.36478 | 6.337 |
| Paired cluster | 8 | 544 | 0.04485 | 0.26242 | 0.29623 | 5.851 |
| Paired cluster | 9 | 775 | 0.02597 | 0.19003 | 0.27234 | 7.316 |
| Two outliers, alternating | 1 | 8 | 1.03782 | 1.56255 | 1.58629 | 1.506 |
| Two outliers, alternating | 3 | 45 | 0.54967 | 1.37952 | 1.30295 | 2.370 |
| Two outliers, alternating | 5 | 149 | 0.37793 | 1.20391 | 1.17701 | 3.114 |
| Two outliers, alternating | 6 | 241 | 0.39758 | 1.01876 | 0.99356 | 2.499 |
| Two outliers, alternating | 7 | 369 | 0.43034 | 1.01653 | 0.85528 | 1.987 |
| Two outliers, alternating | 8 | 544 | 0.35633 | 0.91777 | 0.71465 | 2.006 |
| Two outliers, alternating | 9 | 775 | 0.33498 | 0.82007 | 0.64879 | 1.937 |

The outlier Gaussian p7 selected coarser endpoint is its level1 run after the
allowed numerical-resolution branch; its paired full reference is the common
selected-coarser full endpoint. The exact mixed-level paths are retained.

At p9, paired-cluster sampled maximum errors are0.05680,0.46151,0.61565 for
ours/Gaussian/orthogonal; outlier maxima are0.70097,1.41122,1.09288. Our
outlier maximum worsens from p8(0.65587) to p9 despite its RMS improving.
Our outlier RMS also worsens from p5 through p7. Even the paired-cluster
relative advantage dips at p6 and p8; there is no stepwise-monotone gap.

The paired p5-to-p9 RMS reduction is72.404%/72.488% at the two selected
levels; the better-random/ours ratio increases51.319%/51.412%. These comfortably
pass the frozen15%/20% confirmation gate. Outliers fail: RMS reduction is only
11.363%/12.263%, while the relative advantage decreases37.812%/37.157%.

![Discovery error and ratio curves](../../data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_figure01/scaling_summary.png)

## Smallest tested budgets, with both numerical levels required

Entries are dictionary columns K1+K2. A dash means the target was not
demonstrated at any tested valid budget; it is not a lower bound. All eight
fixed targets and both error norms remain in the complete analysis tables.

| Case | Metric | Target | Ours | Gaussian | Orthogonal |
|---|---|---:|---:|---:|---:|
| Paired cluster | RMS | 0.5 | 8 | 149 | 149 |
| Paired cluster | RMS | 0.3 | 8 | 544 | 544 |
| Paired cluster | RMS | 0.2 | 45 | 775 | — |
| Paired cluster | RMS | 0.1 | 149 | — | — |
| Paired cluster | RMS | 0.05 | 544 | — | — |
| Paired cluster | Sampled max | 0.5 | 45 | 775 | — |
| Paired cluster | Sampled max | 0.1 | 775 | — | — |
| Two outliers | RMS | 1 | 45 | 544 | 241 |
| Two outliers | RMS | 0.5 | 149 | — | — |
| Two outliers | Sampled max | 1 | 149 | — | — |

In particular, paired p7 does **not** meet RMS0.05 at both levels:
0.0499841 versus0.0500180. Paired p8 likewise narrowly misses sampled-max0.1
at both levels. The thresholds are not relaxed to turn these into successes.

## Fresh configurations and seeds

Confirmation uses two frozen geometry/seed groups, each containing a paired
cluster, an alternating cluster with outliers and a negative control. Geometry
and initialization change together, so their separate effects are not identified.
Only p1,p5,p9 are tested here; an untested intermediate order may reach a target.

In the first group, paired-cluster RMS falls from0.08491 to0.03154, and the
better-random/ours ratio rises from5.056 to7.559. Both numerical levels pass the
15% RMS-reduction and20% ratio-growth discriminator. Its sampled maximum falls
from0.18968 to0.07005. The group's complete outlier comparison is pending its
single allowed orthogonal-p5 numerical-resolution check.

The first negative control remains adverse: at p1,p5,p9 our RMS values are
0.02897,0.02657,0.02316; the better random errors are0.00782,0.01102,0.01609.
Enlargement improves our own approximation modestly, while degrading both
random controls here. The resulting ratio increase is not a win: random is
still more accurate, and our p5-to-p9 RMS reduction is only12.86%.

The second group's evaluation and the conditional width gate are pending.

## Cost and rank accounting

At n2048, moving-state scalars are3n+K1*K2 and frozen dictionary scalars are
n(K1+K2). Initial states and implementation caches are additional. Every
closure retains the full moving first-layer rows and readout.

| p | K1,K2 | Columns | Middle coefficients | Moving scalars | Dictionary scalars |
|---:|---|---:|---:|---:|---:|
| 1 | 5,3 | 8 | 15 | 6159 | 16384 |
| 3 | 35,10 | 45 | 350 | 6494 | 92160 |
| 5 | 128,21 | 149 | 2688 | 8832 | 305152 |
| 6 | 213,28 | 241 | 5964 | 12108 | 493568 |
| 7 | 333,36 | 369 | 11988 | 18132 | 755712 |
| 8 | 499,45 | 544 | 22455 | 28599 | 1114112 |
| 9 | 720,55 | 775 | 39600 | 45744 | 1587200 |

Discovery observable lower numerical ranks at p5/6/7/8/9 are126/210/330/495/715;
upper ranks and random ranks equal nominal counts. These use the recorded
1e-10 relative Gram-spectrum cutoff, with effective-rank spectra retained.
Constant-tail dependencies are allowed; a numerical rank deficit is not by
itself a proof that every missing direction is an exact symbolic dependency.
The full network's moving-state count is4,200,448. Feature-count ratios must
not be presented as whole-state, storage or speed ratios.

## Evidence and audit scope

Discovery final analysis:
[full tables](../../data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_analysis01/tables.md),
`metrics.json`, `summary.json`, `validation.json`, `provenance.json`,
`ratios.csv`, `target_accuracy.csv`, `tested_budget_ratios.csv`, `curves.png`
and `circle_errors.npz` in that directory. Raw arrays retain all8192-angle
endpoints,2048-angle trajectory snapshots and reconstructible states/bases.

Independent raw replay/aggregation: [report](scaling_independent_check.md).
Independent protocol/metadata checks: [report](scaling_gate_audit.md).
Exact commands, per-stage reservations, exit status, spent/remaining budgets
and conditional decisions: [execution record](SCALING_RUN_RECORD.md), producer
configurations, and generated `scaling_decisions01/*.json`.

The raw arithmetic audit uses independently implemented saved-state formulas;
its normalized Gram, replay and metric checks do not import analyzer logic.
Raw pre-normalization Cholesky factors were not saved, so their conditioning
and triangular gates use retained metadata plus unchanged producer/preflight
evidence. Tolerance refinement is an empirical consistency check, not an ODE
error certificate. No independent full retraining or continuous-circle
supremum certificate is claimed.
