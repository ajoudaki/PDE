# Practical comparison of residual-adapted finite-panel sources

## Scope and question

New study for the user's request to compare the paper's new cubic-logarithmic
construction with the previous practical Logarithmic implementation. Inputs
are the current paper (especially methods.tex and the complete panel appendix),
its single capture executable, and established docs/code. No other study's
research or saved experiment arrays are inputs. Initial HEAD: `9329a1a`.
All executable changes stay in `paper/figures/capture_trajectory.py`; generated
products stay in `data/generated/cubic_log_comparison_20261008/`, outside Git.
The manuscript and previous experiments are not modified.

The paper changes source construction, not the selected nonlinear runtime.
Its certified increasing disks lead to local polynomial coefficients in one
fixed source space, with no temporal forcing during compressed training.
The previous executable already uses geometric time intervals, so the new
log-cubed theorem does not automatically imply a practical improvement over
that baseline. Initialization-only finite-jet availability is distinct from
the full-horizon rollout producer used in this empirical comparison.

## Frozen experiment contract

Question: does a residual-adapted physical-time source partition improve
dense-trajectory fidelity at fixed retained state, or permit a smaller state
at comparable fidelity, relative to the existing geometric partition?

- Canonical Gaussian dense reference, two tanh hidden layers, zero readout,
  existing MSE mobilities. Width4096, eight training inputs, thirty passive
  scored inputs declared at setup. Passive labels never enter setup/training.
  Data seed47 and passive subsampling seed48, no PCA or input-span reduction.
- Four cases only: sphere3/seed601, raw digits1/7/seed601, circle/seed601,
  raw digits1/7/seed602. The circle is a nontrivial high-frequency stress;
  the second digits initialization checks whether the direction is seed-specific.
  Data and label arrays are shared between the two digits cases.
- Both methods use the same dense initialization, source horizon32,
  degree8 Chebyshev polynomials, nine fitting plus eight interleaved checking
  nodes per interval, paired initialized images, source normalization,
  float32 RK4 source flow and float64 coefficient/selection work.
- Old boundaries are exactly0,1,2,4,8,16,32. For the practical new rule, let
  rho(t) be training residual RMS obtained in a disposable preliminary dense
  rollout. Starting at t=0, use interval length
  `log1p(0.1*Y/rho(t))/log1p(0.1)`, capped at the remaining horizon.
  Thus the initial interval has length1 and later intervals expand as
  residual activity declines. Log-linear interpolation of a fixed0.125-spaced
  residual trace defines rho between nodes. This is an empirical version of
  the paper's logarithmic flaring-height formula, **not** its conservative
  certified constants or its initialization-only compiler. The factor0.1
  places the crossover at residual RMS0.1Y; it is fixed, not searched.
- A second common dense rollout supplies the union of both methods' fitting
  nodes and a common checking grid. Both arms therefore see identical dense
  fields wherever times coincide. Common checking times are129 equally spaced
  midpoints on[0,32], with any coincident fitting node omitted. Fields are
  stored temporarily; no dense parameter history is retained.
- A single seeded rank20 randomized SVD per layer/family supplies nested
  source ranks12 and6. Same removal of initialized mandatory directions as
  the old implementation. Compact widths are respectively
  `4*(max(d+9,17)+3*rank)`:212/140 in d=2,3 and436/364 in d=64.
  Both partitions are tested at both budgets. No rank or selector search
  beyond the existing fixed four-candidate selector. Reject full retention
  or additional constructor source truncation as a valid compression test.
- Same rank-safe floor in all arms: min(1e-4, initial dense normalized
  training-feature-Gram gap/8). Record floor activation/conditioning and
  exact initialized Gram/action diagnostics. This is the existing empirical
  rank-safe optimizer; the paper's exact inverse guarantee is not asserted
  outside its hypotheses.
- Common fine Euler step0.0015625, coarse0.003125, physical horizon32;
  dense and all four compact models get both. One iid dense run uses the
  fine step. Observe every0.5 physical time. No small/LoRA/NTK reruns: the
  decision is source builder versus source builder, not another baseline grid.

## Outcomes, validity, and stopping

Primary score: maximum recorded-time RMS on the thirty passive inputs
relative to the coupled dense reference. Also report endpoint RMS, test-label
MSE, and maximum absolute error over the full38-input panel. Each uses its
corresponding measured iid-dense discrepancy, not a population quantile.
Report post-truncation source errors on the common checking grid, not only
the pre-truncation polynomial-fit error. All retained scalar counts and
shared/source-specific setup work are exposed. Shared-rollout wall time is
not presented as a native one-method setup-time benchmark.

An arm is numerically resolved when dense plus compact coarse/fine RMS is
below10% of the iid-dense RMS. Accuracy passes at ratio<=3; fitting below
training MSE0.01 is recorded separately. At each budget, call the new rule
better only when its RMS is<=0.8 times the old RMS and the improvement exceeds
twice the summed compact coarse/fine discrepancies. Call it worse using the
reciprocal1.25 factor and the same numerical separation. Otherwise report
similar observed accuracy or numerically inconclusive, not proven equivalence.
The stronger efficiency signal is that new-small passes where old-small fails,
with old-full passing. Results for an individual initializer do not settle the
paper's asymptotic existence or confidence claim.

Tiny source/schedule algebra checks are permitted before the four cases;
there is no scientific pilot and no post-result tuning. Use both GPUs, one
case per GPU at a time. Cap each integration and complete source setup at120s,
each case at900s, and the complete paired batch at35 minutes. Once the four
cases and one narrow saved-array consistency check finish, stop. Failed
numeric gates or source selection remain inconclusive; no rescue sweep.
Scoped read-only mechanism checking is allowed; root owns code, records and Git.

## Status

Primary construction sources have been read; the same-runtime/new-source
distinction was independently checked. The single executable now implements
the paired source producer, four-arm runtime and saved-array comparison.
A scoped read-only runner check verified the frozen data/rank/metric contract;
its actionable reporting points were corrected. Tiny schedule, label-rescaling
and degree-eight polynomial-recovery checks pass (maximum error2.8e-15).
The four fresh cases are complete. The single saved-array check passed312
assertions. The bounded empirical comparison is internally checked, not a
promotion or validation of the asymptotic theorem. No further experiments are
authorized by this frozen batch; the campaign is closed.

Frozen launch (from the repository root, both RTX3090 GPUs):

```sh
timeout 2100 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py compression-sweep --protocol cubic --plan studies/cubic_log_comparison_20261008/plan.json --devices cuda:0 cuda:1 --case-seconds 900 --out data/generated/cubic_log_comparison_20261008/paired_run
```

One final check/plot, after all four cases:

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py cubic-summary --root data/generated/cubic_log_comparison_20261008/paired_run --out data/generated/cubic_log_comparison_20261008/summary
```

The runtime cap applies to each Euler integration, the full paired source/setup
phase, and each case separately. Source metadata record the preliminary residual
rollout and shared union-node rollout separately from per-partition fitting/SVD
and per-model assembly. Those shared costs are not charged as though they were
native latency measurements for either standalone method. Model diagnostics are
float64 assembly checks; deployment is float32 and is checked by Euler refinement.

## Results: no consistent practical improvement

At identical retained state, seven of eight old/new comparisons have similar
observed accuracy under the predeclared20% separation rule. The new rule is
worse in the remaining comparison (sphere3, source rank12:49.7% higher RMS).
"Similar" is an operational outcome, not a statistical equivalence claim.
There is no case where new-small passes while old-small fails and old-full
passes. Therefore this test does **not** support replacing the practical old
initializer with the new rule to gain accuracy or reduce retained storage.

The following is maximum recorded-time test RMS divided by the independently
initialized dense-pair maximum recorded-time test RMS. Lower is better; the
frozen accuracy threshold is3. Test RMS concerns predictions against dense,
not classification accuracy or ground-truth label MSE.

| Case | Old, rank12 | New, rank12 | Old, rank6 | New, rank6 |
|---|---:|---:|---:|---:|
| Sphere, d=3, seed601 | 0.887 | 1.328 | 2.157 | 2.011 |
| Raw digits1/7, seed601 | 0.460 | 0.442 | 0.747 | 0.746 |
| Circle, d=2, seed601 | 4.516 | 4.333 | 4.013 | 4.325 |
| Raw digits1/7, seed602 | 0.769 | 0.808 | 1.706 | 1.640 |

Both constructions pass the primary accuracy criterion at both budgets on
sphere3 and both digits initializations. Both fail it at both budgets on the
circle. All16 compressed runs pass the numerical gate: the largest dense-plus-
compact step-refinement RMS is4.57% of its dense-pair RMS, below the10% limit.
Every dense, iid-dense and compressed run finishes the common horizon32 with
training MSE below0.01. Low training loss therefore does not explain away the
circle's genuine prediction-fidelity failure.

Absolute RMS values (same row ordering; the benchmark is one measured dense
pair, not the theorem's population confidence quantile):

| Case | Dense pair | Old rank12 | New rank12 | Old rank6 | New rank6 |
|---|---:|---:|---:|---:|---:|
| Sphere3/601 | 0.007936 | 0.007041 | 0.010538 | 0.017119 | 0.015958 |
| Digits1/7/601 | 0.024673 | 0.011344 | 0.010897 | 0.018421 | 0.018412 |
| Circle/601 | 0.027832 | 0.125679 | 0.120607 | 0.111685 | 0.120384 |
| Digits1/7/602 | 0.013702 | 0.010534 | 0.011078 | 0.023381 | 0.022478 |

The maximum absolute discrepancy over **all38 panel points** and the same65
recorded times is a separate, stronger spatial metric. Its corresponding
dense-pair-normalized ratios are:

| Case | Old rank12 | New rank12 | Old rank6 | New rank6 |
|---|---:|---:|---:|---:|
| Sphere3/601 | 1.128 | 1.795 | 3.888 | 3.573 |
| Digits1/7/601 | 0.663 | 0.630 | 1.020 | 1.020 |
| Circle/601 | 6.025 | 5.506 | 5.296 | 5.750 |
| Digits1/7/602 | 0.756 | 0.764 | 1.199 | 1.576 |

Thus the smaller sphere3 models pass RMS but fail the factor3 maximum-error
check; do not substitute the RMS pass for the paper's supremum guarantee.
Endpoint RMS, label MSE, full loss traces and predictions are also retained
in the case reports/arrays. None of these finite observations is an all-time
or arbitrary-input certificate.

### Retained state and measured work

Each storage entry applies equally to old and new. Total includes the moving
network, deficit vector, all fixed metrics/inverses and the scalar floor;
common data, warmup objects and integration workspace are excluded.

| Input dimension | Source rank | Compact width | Learned scalars | Total retained scalars |
|---|---:|---:|---:|---:|
| 2 | 12 | 212 | 45,588 | 180,421 |
| 2 | 6 | 140 | 20,028 | 78,829 |
| 3 | 12 | 212 | 45,800 | 180,633 |
| 3 | 6 | 140 | 20,168 | 78,969 |
| 64 | 12 | 436 | 218,444 | 788,733 |
| 64 | 6 | 364 | 156,164 | 553,653 |

The corresponding dense totals are16,789,504,16,793,600 and17,043,456 scalars
in d=2,3,64. The source-rank6 sphere3 models achieve about213-fold total-state
compression and pass the primary RMS comparison with either initializer.
They do not pass the stronger panel-maximum comparison above.

| Case | Old/new intervals | Residual precursor, s | Shared source flow, s | Paired source setup, s | Old/new fit+SVD, s |
|---|---:|---:|---:|---:|---:|
| Sphere3/601 | 6/7 | 1.53 | 2.88 | 6.16 | 0.074/0.075 |
| Digits1/7/601 | 6/7 | 1.51 | 2.65 | 5.58 | 0.072/0.074 |
| Circle/601 | 6/15 | 1.57 | 3.84 | 7.60 | 0.073/0.128 |
| Digits1/7/602 | 6/7 | 1.58 | 2.68 | 5.63 | 0.073/0.075 |

Compact assembly adds0.067–0.176s per model. Each fine Euler compressed run
takes61.9–64.5s, versus18.8–19.4s for its dense reference; compression here saves
state, not wall-clock training time in this implementation. Old/new training
costs are effectively unchanged because their runtime and tensor sizes agree.
Each complete four-arm case takes429–444s; two workers finish the frozen batch
in about15minutes. No individual integration or paired setup exceeds120s.

The residual precursor costs256 RK4 updates; the shared source flow costs
421,423,522,421 updates respectively. Both traverse the **full physical horizon**.
The fine Euler runs use20,480 updates. Shared flow and diagnostic work are
deliberately common to both arms, so paired setup times must not be called
standalone old/new initialization benchmarks. This new empirical rule adds a
residual precursor and does not reduce interval/coefficient work here.

### Interpretation and qualifications

The sharper theorem changes the sufficient approximation schedule, not the
autonomous compact optimizer. The old practical producer already uses
geometrically widening intervals. Consequently an improved theoretical
worst-case count does not automatically improve this existing practical
producer. At these settings the new rule uses7 or15 intervals, not fewer
than the old6. Common-grid post-truncation source RMS is slightly lower for
the new source spaces, but this does not translate consistently into better
nonlinear prediction trajectories.

No additional constructor truncation or full-width retention occurred.
The readout floor is inactive at all65 observed times in every compressed
run (not a claim about every intervening step). Initialized Gram and image
actions are checked in float64 assembly; runtime refinement is in float32.
Both arms use the same empirical four-candidate coordinate selector, rank
truncation and rank-safe optimizer. These are not substituted into the
conservative source certificate and then declared certified.

This experiment adapts the flaring idea with empirical constants and full-
horizon source rollouts. It does **not** test the finite-jet, initialization-only
compiler, prove the log-cubed exponent from one width, establish arbitrary
unseen-input decoding, or refute the paper's asymptotic existence theorem.
All passive inputs are declared at setup; their labels are withheld. No test
labels are an argument to either source builder or compact constructor.
No post-result tuning, rescue cases, new widths or extra seeds were run.

### Evidence and reproduction

Executed source commit: `dcbc68f`. Python3.10.14, Torch2.9.0+cu130,
NumPy1.26.4, two RTX3090 GPUs, one CPU thread per worker, TF32 disabled.
The commands above exited0. The `cubic-summary` command checked312 assertions:
source hashes, all44 trajectory time grids/shapes, prediction-derived training
losses, RMS/endpoint/panel scores, state counts, absence of hidden truncation
and refinement arithmetic. The figure was visually inspected. Reports record
data hashes, configurations, source work and precision qualifications.

Executable SHA256:
`3286f43a88fed033a7c57ee4992f83153f4a242233e693ea12b7581602448cd2`.
Plan SHA256:
`43131e507cef484ce770ef16e5498181346d44862f8ec2bf245555c08b233fd4`.

Generated case reports and arrays are under
`data/generated/cubic_log_comparison_20261008/paired_run/`;
the combined check report and PNG/PDF figure are under the sibling `summary/`.
Trajectory NPZ SHA256 values, in table order:

- Sphere3/601: `5f38fb7613ffd7d9ca7eb46ef58aa958916e9afdf77de8b82c2f2c510ad4fc5c`.
- Digits1/7/601: `e25e8a8053da9930bf0f278b3de2c888c6c588adbec63fa4a5b458066216dd72`.
- Circle/601: `92fe8ae52d36c1d9e8ba087cec0a4f86b6372fca154245e5459e35fdf5d52bb7`.
- Digits1/7/602: `2b5720d67685fc4f562ceb427872a65a0d0c0a8f3e7277dc17cbcef40594ce51`.

Recommendation: retain the old initializer as the practical default; regard
the new construction as a sharper theoretical guarantee, with no demonstrated
practical advantage from this direct schedule adaptation. Preserve the failed
circle cases and the RMS-versus-panel-maximum distinction. The manuscript and
previous experiments were not changed.

## Authorized follow-up: two larger old-circle budgets

The user explicitly reopened the circle case for exactly two additional runs,
clarifying2x/4x **total retained storage**, relative to the old width212 result.
This is a budget continuation, not a new seed or method search. Frozen choices:
width300/rank19 (360,909 scalars,2.00037x) and width424/rank29 (720,385 scalars,
3.99280x). Both the source-space capacity and coordinate count increase using
the same allocation rule. One rank37 randomized SVD gives nested ranks19/29;
these are not strictly nested with the original rank12/rank20 SVD.

Reuse exactly the original circle's data, dense reference, model seed601,
selection/SVD seed501, floor, degree8 old source intervals, horizon32 and
Euler step0.0015625. Source preparation retains the original union observation
grid (including nodes not fitted by the old construction), because those nodes
also determine shortened RK4 steps. Verify this grid against the saved report.
No new-construction model is fitted. Test labels stay out of setup/training.

Primary outcome: endpoint RMS against the same saved dense predictions on
all30 test points, compared with old width212 endpoint RMS0.0730863.
Report increases as well as decreases; reductions below20% are not interpreted
as substantial improvement. Reject incomplete/nonfinite runs, extra source
truncation, wrong retained counts or grid/data mismatches. These two runs use
the previously refined step but receive **no fresh step-refinement certificate**;
small differences are not promoted to a GF claim. Exactly two fine Euler fits,
one per GPU,120s each, one common setup capped120s,400s total wall cap.
No follow-on runs, rank tuning or rescue after either outcome.

```sh
timeout 400 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py cubic-budget --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere2_seed601 --out data/generated/cubic_log_comparison_20261008/circle_larger_budgets --devices cuda:0 cuda:1
```

Status: exactly two fits completed; no additional runs. Both improved endpoint
RMS substantially. The earlier four-case results remain unchanged. Unrelated
concurrent manuscript edits are preserved.

| Old-circle configuration | Total retained scalars | Endpoint test RMS vs dense | Improvement over original |
|---|---:|---:|---:|
| Original, width212/rank12 | 180,421 | 0.0730863 | — |
| Approximately2x, width300/rank19 | 360,909 | 0.0167651 | 4.36-fold |
| Approximately4x, width424/rank29 | 720,385 | 0.00395727 | 18.47-fold |

The saved dense-pair endpoint RMS is0.00552362. Thus the4x model is below that
measured benchmark;2x remains about3.04times it. Worst-recorded-time RMS is
0.0266578 and0.00514229 respectively, versus the original0.125679 and dense
pair0.0278325. These are prediction differences, not label RMSE.

The two final training MSEs are0.00209825 and0.00287910. The readout floor is
inactive at all recorded times. The common source grid matched the original
to1e-12; no extra constructor truncation or full retention occurred. Saved
trajectories are finite65-by38 arrays with identical dense observation times,
and their endpoint test RMS was independently recomputed from all30 test
columns. Both improvements exceed the frozen20% threshold. They are internally
checked finite-step observations, not fresh budget-specific GF certificates.

Setup took8.16s; the two parallel fits took68.76s and68.38s, with76.93s total
elapsed. Runtime cap and two-fit limit were respected. The launch command
above exited0. Environment remains Python3.10.14/Torch2.9.0+cu130/NumPy1.26.4,
two RTX3090 GPUs, one Torch CPU thread, TF32 disabled; offline assemblyfloat64,
runtimefloat32. Source SHA256:
`7b0d449eb5949033fbcea6bbe84f47bb003f50ce239344881b8c3330f6f5f955`.
Generated `circle_larger_budgets/trajectories.npz` SHA256:
`10a31d2bb237c7d9cbe0650da7ba147d7e6b6c8db696fffd3d7bc62c9b498c02`.
The report also hashes the consumed dense-reference report and arrays.

Interpretation: increasing both source rank and coordinate budget repairs this
particular circle mismatch at4x storage in the measured Euler experiment.
This does not identify which increased component caused the improvement,
prove monotone convergence, or alter the old/new comparison at the original
budgets. The requested two-run continuation is now closed.

## Authorized follow-up: the same two budgets for the new construction

The user next requested the new construction at the same2x/4x budgets. Freeze
exactly the preceding width300/rank19 and width424/rank29 configurations,
data, dense reference, seeds, floor, source-flow observation grid, degree8,
nested rank37 SVD and Euler settings. Only the fitted source partition changes
from old geometric intervals to the new residual-adapted intervals. Retained
state, runtime and test-label isolation are unchanged. No new optimization or
additional cases. Both are warmup-rollout empirical constructions, not the
finite-jet compiler. The original experiment provides the new width212 baseline.

Primary metric is endpoint RMS against the same dense reference, compared
with the old construction at matching storage and with new width212's0.0729340.
Use the same finite/grid/storage/truncation checks and20% descriptive improvement
threshold. Exactly two fine Euler fits,120s each, common setup capped120s,
400s wall limit. No fresh budget-specific step refinement or rescue runs.

```sh
timeout 400 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py cubic-budget --partition new --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere2_seed601 --out data/generated/cubic_log_comparison_20261008/circle_larger_budgets_new --devices cuda:0 cuda:1
```

The initial launch exited1 during width424 assembly: the existing layer1
source-condition cap16 failed. Zero Euler fits started; width300 had already
assembled successfully and was registered. This4x outcome is invalid/inconclusive,
not an RMS measurement. An interim conversational attribution to2x was corrected
immediately after reading the saved registration metadata.
No threshold change, alternate selector/seed, larger budget or rescue is made.
The already assembled2x configuration has not yet trained. The runner
now accepts `--factors 2` to execute that remaining fit alone,
without retrying the failed4x case. Shared rank37 source production and all
scientific settings remain unchanged. The failed launch's artifacts are kept.

```sh
timeout 240 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py cubic-budget --partition new --factors 2 --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere2_seed601 --out data/generated/cubic_log_comparison_20261008/circle_larger_budgets_new_2 --devices cuda:0 cuda:1
```

Status:4x failed setup; the2x fit completed. No extra scientific configuration
was added and the failed4x configuration was not retried or modified.

| Total-storage budget | Old endpoint RMS | New endpoint RMS |
|---|---:|---:|
| Original,180,421 scalars | 0.0730863 | 0.0729340 |
| Approximately2x,360,909 scalars | 0.0167651 | 0.0132641 |
| Approximately4x,720,385 scalars | 0.00395727 | No RMS: setup guard failed |

The new2x endpoint error is20.88% below old2x,5.50-fold below new width212,
and2.401times the measured dense-pair endpoint RMS0.00552362. Its worst-
recorded-time RMS is0.0239931; final training MSE is0.00223738. The readout
floor is inactive at all recorded times. Layer source-embedding maxima were
14.1694 and10.8808, below the unchanged16 cap. This is a finite-step result
with no new-budget refinement certificate; the4x setup rejection is an
inconclusive configuration, not evidence of prediction error or nonexistence.

The valid2x run used the identical65 times,38 panel inputs, retained count
and saved dense reference. Endpoint RMS was independently reconstructed
from all30 held-out-label test columns; arrays are finite. Setup took8.18s
and training61.83s,70.02s total; the preceding failed assembly took8.18s and
started no training. No additional model fit, selector trial or tolerance
change was performed. Both failed and completed artifact directories remain.

The initial attempted pair used executable SHA256
`7789f015021e2f69d6568a14e0ba9d7d668e5e9b1e7db45b95fd8615b1587045`;
the successful single-factor dispatch used
`37b432c7a4e8af7cc20313bb810f46200b5fb8309d8113222ad1a7485193195e`.
The latter change only permits selecting an already-authorized factor and
records setup errors; it does not change source or training mathematics.
`circle_larger_budgets_new_2/trajectories.npz` SHA256:
`72190af86f0cf6b258c5c87a6e360215a325324ca8ad39d0bb0fdcd161803c2e`.
Environment/precision match the old-budget follow-up. The continuation is
closed with one measured endpoint result and one setup failure.

## Authorized retry: more coordinate samples for new4x

The user explicitly requested retrying the new method with more random
coordinate samples. Retry only the previously rejected width424/rank29
configuration with64 candidates per layer instead of4. Retained storage stays
720,385 scalars; source construction, rank37 SVD, model/selection seeds,
conditioning cap16, data, reference and Euler settings remain unchanged.
The64-candidate sequence extends the original first4 with the same generator.
Select solely by source-Gram conditioning, never by test prediction error.
Record both the best condition among the first4 and the final best condition.

One source/setup attempt and at most one fine Euler fit; setup and fit each
capped120s, total240s. If no valid selection is found, stop without further
trials or a relaxed guard. Primary metric is endpoint test RMS against the
same saved dense reference and old4x result0.00395727; retain the original
finite-step/no-new-refinement qualification. No other budget or seed is run.

```sh
timeout 240 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py cubic-budget --partition new --factors 4 --selection-trials 64 --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere2_seed601 --out data/generated/cubic_log_comparison_20261008/circle_new_4_trials64 --devices cuda:0 cuda:1
```

Status: one authorized retry completed successfully. Earlier failed artifacts
are retained. The first layer's best condition among the original4 candidates
was16.0636139, barely above16; among64 it was12.0339674. The second layer
remained10.2295242. Thus the same conditioning guard passed at unchanged storage.
The candidate was chosen before training solely by conditioning, not test RMS.

The new4x endpoint RMS is0.0109307133, versus old4x0.0039572688, new2x0.0132640852
and dense-pair endpoint0.0055236243. The new4x result is therefore1.979times the
measured dense-pair endpoint discrepancy,17.6% lower than new2x, but2.762times
old4x. Worst-recorded-time RMS is0.0135652838. Final training MSE is0.00236210;
the readout floor is inactive at all recorded times. Its modest reduction from
new2x does not meet the earlier20% descriptive substantial-improvement threshold.

No source rank, width, retained count, seed, cap or Euler step changed. Source
selection effort differs: this new4x uses64 candidates, while old4x used4.
Do not interpret it as a matched-selector-effort comparison or infer that
improved conditioning monotonically improves prediction accuracy.

One fit completed in62.21s; setup8.62s; total70.99s. Independently reconstructed
endpoint RMS and identical65-time/38-point grids passed, arrays are finite,
and total retained storage is720,385 scalars. The tiny pre-run synthetic
selector check also confirmed exact first-four candidate preservation and
nonincreasing best conditioning. No fresh step-refinement run was added.
The command exited0. Source SHA256:
`b83f70ef30a9243c18e4e705e86f41ee4cccdece3d82e403c160086eea9b809e`.
`circle_new_4_trials64/trajectories.npz` SHA256:
`54070c7be1915403834a92ae4a953c049ec181a3edfc2e1a9040dd86c2a42114`.
Environment/precision are unchanged from the preceding budget runs.

This resolves the practical setup rejection at this budget with the explicitly
authorized larger sampling effort. It supersedes the absence of a measured
new4x result, not the historical fact that the original4-candidate setup failed.
It does not establish superiority over old4x or a new theorem. The retry is
closed; no additional runs or selector searches were made.
