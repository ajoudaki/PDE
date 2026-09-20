# Finite dictionary scaling: results

The bounded experiment finds useful finite approximation gains from larger
observable dictionaries, but **does not confirm a consistently growing advantage
over random dictionaries across fresh configurations**. The paired discovery
case and first fresh paired case show a growing p5-to-p9 gap; the second fresh
paired case shows a contracting gap. Outlier-family gaps contract in all three
conditions, and the better random control remains more accurate on both negatives.
Consequently Stage D does not qualify. No asymptotic rate is inferred.

All 96 final closure/reference comparisons pass the specified numerical gates
and independent raw/summary checks. This is internally checked empirical
evidence; nothing is promoted to the established book or code.

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
| Two outliers, alternating | 7 | 369 | 0.43034 | 1.01656 | 0.85528 | 1.987 |
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

The selected-coarser-level results are below. The two-level discriminator table
following them makes the replication outcome explicit. Columns grow from 149
at p5 to 775 at p9; middle coefficients grow from 2,688 to 39,600.

| Fresh condition | Our RMS p5 → p9 | Our sampled max p5 → p9 | Better random / ours RMS p5 → p9 |
|---|---:|---:|---:|
| Paired, group 1 | 0.08491 → 0.03154 | 0.18968 → 0.07005 | 5.056 → 7.559 |
| Paired, group 2 | 0.04407 → 0.02887 | 0.09714 → 0.06374 | 8.305 → 5.654 |
| Outliers, group 1 | 0.38801 → 0.29772 | 0.79849 → 0.65877 | 2.931 → 2.113 |
| Outliers, group 2 | 0.43095 → 0.35115 | 0.82844 → 0.74611 | 2.870 → 2.089 |
| Negative, group 1 | 0.02657 → 0.02316 | 0.09133 → 0.08143 | 0.415 → 0.695 |
| Negative, group 2 | 0.02624 → 0.02104 | 0.07823 → 0.06312 | 0.400 → 0.802 |

Numbers separated by a slash below are the two selected numerical levels.
The frozen criterion requires at least 15% RMS reduction and at least 20%
ratio growth at both levels. Percentage changes are comfortably separated from
the decision thresholds; switching numerical level does not change any verdict.

| Fresh condition | Our RMS reduction (%) | Ratio change (%) | Pass both levels? |
|---|---:|---:|---|
| Paired, group 1 | 62.856 / 62.826 | +49.497 / +49.382 | Yes |
| Paired, group 2 | 34.500 / 34.516 | −31.921 / −31.872 | No |
| Outliers, group 1 | 23.271 / 23.249 | −27.899 / −27.928 | No |
| Outliers, group 2 | 18.518 / 18.538 | −27.187 / −27.157 | No |
| Negative, group 1 | 12.861 / 12.865 | +67.511 / +67.488 | No |
| Negative, group 2 | 19.810 / 19.817 | +100.787 / +100.757 | Yes, but not an eligible positive family |

Neither positive family passes in both fresh groups. **The width-4096 stage
is not run because its scientific gate fails**, despite ample remaining compute.
The negative-control pass in group 2 cannot trigger Stage D. Its ratio remains
below one: the better random dictionary is still more accurate. Moreover, both
random methods become less accurate as their dictionaries grow on both negative
controls. A rising ratio can reflect deterioration of the controls as well as
improvement of our method, so it must not be described as a universal win.

Absolute p5-to-p9 RMS and sampled-maximum errors improve for our method in all
six fresh conditions. At p9 the better random RMS is about 7.55 and 5.65 times
ours for the two paired cases, and about 2.11 and 2.09 times ours for the two
outlier cases. These are substantial matched-budget advantages on those cases;
the growth of that advantage beyond p5 is not robust across the tested cases.

For tested-budget efficiency, both fresh paired cases reach RMS 0.1 using 149
columns, while neither random method reaches it at any tested budget through
775. For RMS 0.05, our smallest tested budget is 775 in group 1 and 149 in
group 2. Neither reaches RMS 0.02. On both negatives, the random dictionaries
already reach RMS 0.01 with 8 columns, while ours does not reach RMS 0.02 at
any tested budget. Each statement requires both numerical levels; the complete
fixed-target tables include non-achievements and sampled-maximum targets.

![First fresh group](../../data/generated/random_dictionary_learned_circle_20260920/scaling_confirm1_figure01/scaling_summary.png)

![Second fresh group](../../data/generated/random_dictionary_learned_circle_20260920/scaling_confirm2_figure01/scaling_summary.png)

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

## Protocol completion and numerical qualifications

Stages A, B and C complete: 28, 24 and 120 scheduled trajectories, respectively,
plus three permitted extra-resolution trajectories. All 175 fit the common
training-MSE threshold. The 14 Stage D trajectories are not run because neither
positive family satisfies the two-fresh-group discriminator. No replacement
seeds, changed geometries, extra orders, new training batches or promotion follow.

All final selected endpoints pass fit, replay, grid, dictionary metadata and
own-endpoint refinement gates. Discovery and the two confirmation groups have
42, 27 and 27 valid closure/reference comparisons. Independent raw audits check
5,389, 3,660 and 3,660 assertions; independent summary audits check 6,327, 8,763
and 8,763 assertions, respectively. Maximum selected own-endpoint discrepancies
are 0.00989941, 0.00915284 and 0.00790421. These are consistency checks, not
certified trajectory errors or a claim of a known numerical error floor.
The largest recorded nested-4096 versus 8192-grid sensitivities are
2.22e-16 for RMS and 1.2813e-5 for sampled maximum across the final analyses.

Three initial own-endpoint discrepancies exceeded 0.01. Each received exactly
one extra attempt, selected solely by the frozen numerical criterion. The original
failed comparisons and all three attempts remain available:

| Cell | Original discrepancy | Latest-pair discrepancy |
|---|---:|---:|
| Discovery outlier Gaussian p7 | 0.0129855 | 0.00683494 |
| Fresh outlier group 1, orthogonal p5 | 0.0108479 | 0.00156076 |
| Fresh outlier group 2, orthogonal p1 | 0.0187888 | 0.00185624 |

The campaign used 2,008.215602 summed training-worker seconds out of 6,000;
3,991.784398 remain unused, with no outstanding reservation. The preflight
used 2.084 seconds from its separate 120-second allowance and was not repeated.
Postprocessing/audit times are recorded separately. Remaining compute is not
authorization to extend the closed protocol.

One C2 saved archive failed its CRC check in the frozen lower basis. Exactly
one bit differed from five byte-identical redundant copies, all matching the
original declared size and CRC. The original damaged archive is preserved;
`scaling_repair_archive.py` restored only that bit, leaving every other archive
byte unchanged. An independent structural audit verified all 20 checks. No
training or numerical basis recomputation was used for the repair. The cause
of corruption is unknown. Failed analysis01 is retained; final analysis03 uses
the repaired archive and the latest allowed numerical attempts. One initial
independent audit process exited139 before producing metrics; a fresh retry and
the final raw/summary audits exited0 and passed. Failed launches are preserved
in the independent report; neither failure caused a training rerun.

## Evidence and audit scope

Discovery final analysis:
[full tables](../../data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_analysis01/tables.md),
`metrics.json`, `summary.json`, `validation.json`, `provenance.json`,
`ratios.csv`, `target_accuracy.csv`, `tested_budget_ratios.csv`, `curves.png`
and `circle_errors.npz` in that directory. Confirmation final analyses:
[group 1 tables](../../data/generated/random_dictionary_learned_circle_20260920/scaling_confirm1_analysis02/tables.md),
[group 2 tables](../../data/generated/random_dictionary_learned_circle_20260920/scaling_confirm2_analysis03/tables.md).
Each has the same metrics, complete fixed-target tables, ratios, provenance,
validation and circle-error products as discovery.

Raw arrays retain all8192-angle
endpoints,2048-angle trajectory snapshots and reconstructible states/bases.

Independent raw replay/aggregation: [report](scaling_independent_check.md).
Independent protocol/metadata checks: [report](scaling_gate_audit.md).
The independently checked terminal branch and budget record is
`scaling_gate_audit01/D_gate.json` in the generated namespace. It records all
175 trajectories, zero metadata problems and no qualifying width-test family.

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
