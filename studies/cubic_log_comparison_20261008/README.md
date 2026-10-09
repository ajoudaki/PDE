# Practical comparison of residual-adapted finite-panel sources

## Scope and question

### Three independently coupled repetitions, 2026-10-09

Display update: at the user's request, `runner_three_seeds_plot.json` now selects
means with plus/minus one sample standard deviation (ddof=1), not standard
errors. The same raw paired scores produce `runner_three_seeds/plots/plot_007/`
under this study's generated namespace; the median/range figures in plot006 are
preserved. No training was rerun. Nine points still have3 seeds, Logarithmic850
has2, visibly labelled. All means/SDs were reconstructed from the per-seed
scores; all lower SD bounds are positive, so every requested bar is displayed.
The original data and per-repetition provenance are unchanged. Both PNGs were
visually checked. The plotter omits an SD bar for singletons (SD is undefined).

The user requests exactly two additional reference seeds,602/603, for Dense,
Legendre and Logarithmic only, combined with the completed601 repetition.
Configuration: `runner_two_more_seeds.json`. Architecture, data, training,
source setup and the three largest budgets remain identical to
`runner_largest_three.json`. Each new seed rebuilds the coupled compressions
and independently initializes its dense comparators. No601 rerun, Harmonic,
low-rank or frozen-feature fits, new sizes, tuning, retries or refinement.

This is22 new fits: reference plus four dense comparators, three Legendre
orders and three Logarithmic budgets per repetition. Use both RTX3090 GPUs,
one repetition per GPU,120s per source setup/fit,1200s command cap. Successful
execution means completed finite trajectories with matching data/time grids,
verified counts and reconstructed scores, not a predetermined ranking.
Failures stay inconclusive without replacement seeds. Endpoint and
worst-recorded-time test RMS are computed against each repetition's own
reference, then summarized by three-seed medians and observed min–max bars,
not confidence intervals. Keep original run manifests and raw data unchanged;
the merged figure records their separate provenance. Full-horizon rollout
setup, empirical source ranks and declared Logarithmic test inputs remain
explicit; this adds no asymptotic or continuous-time certificate. Root owns
config/notes; a scoped agent adds plot-only saved-run merging after both
workers have loaded the unchanged producer; a saved-array consistency check
closes this bounded batch.

Outcome:21 successful new fits; one initializer failure, without a retry or
replacement. Seed602's width850/rank65 Logarithmic source has layer1 condition
19.6555686>16 after64 candidates, so that repetition is inconclusive for this
budget. The command correctly exits1. Seed602/603 elapsed times are374.59/441.96s
on the two GPUs concurrently; completed fits take17.56–69.84s. All completed
fits reach the full20480-step horizon. Nine displayed points have three seeds;
Logarithmic850 has two and is explicitly annotated2/3. Observed medians:

| Method | Width/order | Endpoint test RMS | Worst recorded test RMS | Seeds |
|---|---:|---:|---:|---:|
| Dense | 1446 | 0.0104392 | 0.0178676 | 3 |
| Dense | 2047 | 0.00873262 | 0.0174012 | 3 |
| Dense | 2895 | 0.00628602 | 0.0102609 | 3 |
| Dense | 4096 | 0.00800371 | 0.0109219 | 3 |
| Legendre | 2 | 0.000898489 | 0.00138006 | 3 |
| Legendre | 3 | 0.000628800 | 0.000628800 | 3 |
| Legendre | 12 | 0.0000604475 | 0.0000604475 | 3 |
| Logarithmic | 424 | 0.00232826 | 0.00232826 | 3 |
| Logarithmic | 600 | 0.00127645 | 0.00127645 | 3 |
| Logarithmic | 850 | 0.000693551 | 0.000760539 | 2 |

Every successful compression realization is below its own independent-dense
comparator in both recorded metrics. This statement is conditional on successful
construction and does not erase the failed850 initializer. Existing601 raw
arrays are unchanged. All three repetitions used the identical producer snapshot
SHA256`294643221e28f3a2fa32267ffd29f2a585da624416c1183e775a7451826a83fd`.
New602/603 trajectory hashes are
`1049f0253b012c038a83a864aded29a6eb0fc6ec5345c7c95e41de6c739167e9` and
`6f12e658aa77a8a31c1568a58a2bea5c7221d836b3612029ef7801fdce31d850`.
Final figures, per-seed metrics, original input provenance and full fixed/learned
storage counts are under
`data/generated/cubic_log_comparison_20261008/runner_three_seeds/plots/plot_006/`.
The plot-only merged-run interface preserves each original producer identity;
AST comparison confirms every numerical model, initializer and integration
function is unchanged. Saved-run merge, single-run compatibility, CLI empty-list
handling and duplicate/incompatible-input rejection checks passed. No additional
scientific fits were used for these software checks. This requested batch stops
with the initializer failure retained, not repaired through selection changes.
The scoped read-only checker independently reconstructed all per-seed scores
and medians/ranges within1e-15, verified finite65-by38 arrays, grids, counts,
source settings, untruncated constructors, distinct references/role seeds and
unchanged601 data, and visually checked both final figures. Maximum accepted
source condition is15.4471. The failed initializer remains explicitly recorded.

```sh
timeout --signal=TERM --kill-after=10s 1200 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py run --config studies/cubic_log_comparison_20261008/runner_two_more_seeds.json
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py plot --config studies/cubic_log_comparison_20261008/runner_three_seeds_plot.json
```

### One-seed largest-three runner check, 2026-10-09

The user requests one production-scale check of the new configuration runner,
not another sweep: three largest sizes on the current curves per method and live
plot updates. Frozen configuration: `runner_largest_three.json`. Same sphere3
task, m8/p30, width4096, two tanh hidden layers, data47/reference601, zero
readout and canonical MSE mobilities; float32 Euler step0.0015625 through T32,
65 recorded times. Dense smaller widths1446/2047/2895, Legendre orders2/3/12,
low-rank ranks16/24/96, Harmonic and Logarithmic widths424/600/850 with source
ranks29/44/65. One independent width4096 comparator and frozen features are
retained as anchors. All auxiliary seeds use the runner's recorded deterministic
role streams; those differ from the older hand-launched seed choices.

Primary output is endpoint test RMS against the coupled reference; also save
worst-recorded-time RMS, training loss, storage and timing. A successful software
check requires completed finite trajectories on identical data/time grids and
reconstructed scores/counts, not a predetermined accuracy ranking. Record
selection/runtime failures as inconclusive. No new numerical-refinement
certificate or asymptotic conclusion is claimed. Full-horizon rollout source
setup and declared Logarithmic test inputs remain explicit. One repetition on
one GPU, <=120s per source setup/fit, 20min command cap, 18 fits total including
reference/comparators. No retries, new sizes, seeds, tuning or replacement runs.
Root owns the config/record; a read-only scoped check verifies sizes and final
saved-array consistency. Stop when this batch and its check finish.

Outcome: all18 fits completed, no setup/runtime failures or omitted points,
717.78s total on one RTX3090. Per-fit times were2.93–69.83s; shared Harmonic
and Logarithmic source construction took4.21s and5.75s. Every fit reached
20480 Euler steps and the common65-time grid. Reference, all three Legendre
trajectories and frozen features reproduce the historical same-reference
predictions bit-for-bit. Auxiliary stochastic seeds differ by design, so the
other curves are fresh realizations rather than exact-repeat targets.

| Method | Orders/widths/ranks, ascending | Endpoint test RMS, same order |
|---|---|---|
| Dense smaller | 1446 / 2047 / 2895 | 0.0168676 / 0.00951770 / 0.00628602 |
| Legendre | 2 / 3 / 12 | 0.000915328 / 0.000617116 / 0.0000593923 |
| Low rank | 16 / 24 / 96 | 0.213900 / 0.188131 / 0.155279 |
| Harmonic | 424 / 600 / 850 | 0.00413241 / 0.00338363 / 0.00278934 |
| Logarithmic | 424 / 600 / 850 | 0.00265481 / 0.00103306 / 0.000743328 |

Independent dense endpoint/worst-recorded RMS is0.00826425/0.0103911;
frozen features give0.218863/0.552208. Thus all nine compression points lie
below the measured independent-dense discrepancy in both displayed metrics
for this one seed. This is not an asymptotic or multi-seed conclusion.
The x-axis is learned scalar state; all fixed storage remains charged in
the accompanying caption/table. Source/trajectory SHA256:
`294643221e28f3a2fa32267ffd29f2a585da624416c1183e775a7451826a83fd` /
`66436993eb5a5c7a3126bc45ab0728c18014ac28e71b5dea2a1031dba965a003`.
Final plots, caption, per-seed metrics and full storage counts are under
`data/generated/cubic_log_comparison_20261008/runner_largest_three/plots/plot_010/`.
Progress plots001–009 and raw data remain retained. No executable changes,
new orders, replacement seeds, reruns or numerical-refinement batch were used.
The scoped saved-array check passed all18 runs: data/time grids, losses,
source/version hashes, learned/fixed counts and absence of constructor
truncation. Largest selected source condition was14.9753, below16.
One metadata caveat is retained: constructor diagnostics' `runtime_dtype`
still denotes float64 assembly before deployment casting; the executed-run
dtype and saved predictions correctly record float32. This affects no
trajectory or score and was not used to infer training precision.

```sh
timeout --signal=TERM --kill-after=10s 1200 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py run --config studies/cubic_log_comparison_20261008/runner_largest_three.json
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py plot --config studies/cubic_log_comparison_20261008/runner_largest_three.json
```

### Config-runner maintenance, 2026-10-09

The user approved a compact JSON interface with oblivious/non-oblivious method
groups, shared source-setup options, generated CLI overrides, and independently
rebuilt coupled compressions for every reference seed. This is implementation
maintenance of the same experiments, not a new accuracy campaign. All executable
code remains in `paper/figures/capture_trajectory.py`; the editable default is
`paper/figures/compression_experiment.json`, with usage in `paper/scripts/README.md`.

`run` uses defaults < JSON < CLI, with strict field/type checks and optional
method-local setup overrides. `plot` reads saved trajectories, computes each
model's error against its own repetition reference, and only then aggregates.
Source/config/data identities protect reuse; failed attempts are preserved.
Source snapshots, seeds, raw arrays, timings and both learned/fixed counts are
retained. The full-rollout, empirical-rank and finite-time-grid qualifications
are unchanged. No large training runs or paper figures were replaced.

Bounded implementation checks passed: typed merge and empty-list overrides,
per-method inheritance, deterministic distinct seed streams, existing Legendre/
baseline/Harmonic algebra checks, and tiny end-to-end runs on CPU and both
RTX3090 GPUs. Two reference seeds each rebuilt all three compressions and shared
identical data; source seeds and reference initialization hashes differed.
Additional tiny checks exercised raw 64-dimensional Digits, the NPZ loader, and
three-layer GELU Logarithmic with float64 and a different temporal order.
Saved-array plotting and exact-config reuse passed; a scoped read-only review
found and prompted fixes for partial-config schema validation and damaged-cache
recovery. Source helper defaults were checked for unchanged output; configuration
options now expose temporal/spatial orders, rollout step/precision and selection
condition limit without changing the default algorithms.

Reproduction (use a fresh output override after source changes):

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py run --config studies/cubic_log_comparison_20261008/runner_smoke.json
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py plot --config studies/cubic_log_comparison_20261008/runner_smoke.json
```

Evidence folders under `data/generated/cubic_log_comparison_20261008/` are
`config_runner_smoke`, `config_runner_gpu`, `config_runner_digits`,
`config_runner_deep`, `config_runner_npz`, and `config_runner_final`; each stores its exact executed
source snapshot and configuration. These are short software checks, not
scientific evidence of training convergence or compression asymptotics.

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

## Authorized follow-up: new Logarithmic only on sphere3

The user requests the first point for a future learned-state versus endpoint
RMS figure: sphere3, width4096, eight training and thirty declared passive
inputs, Euler, normalized by the iid-dense endpoint RMS. The user clarified
that the latest implementation should remain unchanged. In particular this
is still the empirical rank-truncated, rollout-initialized construction,
not the paper's full coefficient-space/initialization-jet construction.

Run only new width424/rank29 with64 coordinate candidates, matching the latest
successful circle configuration. Reuse this study's sphere3/seed601 dense
references and data; retain degree8, rank37 randomized SVD, conditioning cap16,
floor from the sphere3 reference, horizon32 and Euler step0.0015625. No other
compressed method, control, budget, seed or rescue search is run. One compact
Euler fit, capped120s; setup capped120s; full command capped240s. Primary
score is RMS over all30 test predictions at the common endpoint divided by
the saved iid-dense endpoint RMS. Separately report learned and fixed counts.
No fresh budget-specific refinement certificate is asserted. Check saved
predictions, time grids, data hashes and state counts once, then stop.

```sh
timeout 240 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py cubic-budget --partition new --factors 4 --selection-trials 64 --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --out data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --devices cuda:0 cuda:1
```

Status: the single fit completed. Endpoint test RMS is0.00188513755 versus
the iid-dense endpoint RMS0.00338088494, giving the requested ratio0.557587.
Moving state is181,480 scalars (181,472 network parameters and8 deficit
coordinates); fixed metrics/inverses/floor add539,329, total720,809. Relative
to the16,793,600-scalar dense model, this is92.54-fold moving-state reduction
and23.30-fold total-state reduction. These are different storage comparisons.

Setup took7.05s, Euler training60.95s, total68.16s. Final training MSE is
0.00120493. The readout floor was inactive at all recorded times; no extra
constructor truncation occurred. One final saved-array check passed: all65
times and38 inputs match the reference, predictions are finite, training losses
and endpoint RMS reconstruct correctly, and retained counts agree. No other
method or budget was run. No fresh budget-specific step refinement was added.
This supplies one empirical point below1 for the proposed figure, not an
asymptotic compression certificate or a comparison against unrun controls.

Executed source SHA256:
`144e8d199306c192a3c1bac2aab387acfdffc2597194ed30db8f0ac03ad95bba`.
Generated trajectory NPZ SHA256:
`05fbda4534a5654ad2ff3aff977a4a109f1855951311813b315957c5c5bd8645`.

## Authorized figure continuation: Legendre, Harmonic and the dense pair

The user now requests the remaining method points on the same sphere3 task.
Reuse exactly the saved sphere3 dense/iid pair and the latest Logarithmic
point. Add two runs only: Legendre order12 (the existing width4096 preset),
and Harmonic width424/rank29 with64 selector candidates to match Logarithmic's
moving-state budget. Keep Harmonic's existing degree8 time/degree5 spatial
source, source seed601, selector seed501, and exact unregularized readout.
Its72 fixed sphere nodes exclude the scored inputs. Logarithmic's declared
panel and rank-safe floor remain distinct; do not imply identical setup scope.

The hypothesis tested is that each fixed configuration's endpoint RMS ratio
is at most1; report ratios above1 unchanged. Finite-step validity requires
the complete common horizon, finite outputs, unchanged data/reference hashes,
matching time grids and prediction-derived losses. Legendre's lifted-coordinate
drift is recorded, not silently corrected. No new step-refinement certificate
is asserted. Charge actual executable moving state, including auxiliary
coordinates, and all fixed matrices. Dense x is the per-network count, not
the sum of both reference runs. This is one measured dense pair, not a
population variability quantile. No baselines, other orders, seeds or rescue
searches. Each setup/fit is capped120s; both fits run on separate GPUs;
the complete command is capped360s. One saved-array consistency check follows.

```sh
timeout 360 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_other_points --devices cuda:0 cuda:1
```

Both requested fits completed, with no additional configurations. The actual
four figure points are:

| Method | Moving scalars | Fixed scalars | Endpoint test RMS vs dense | Ratio to dense pair |
|---|---:|---:|---:|---:|
| Legendre, order12 | 868,354 | 16,777,240 | 0.0000593923 | 0.0175671 |
| Harmonic, width424/rank29 | 181,480 | 539,328 | 0.00461017 | 1.36360 |
| Logarithmic, previous width424/rank29 | 181,480 | 539,329 | 0.00188514 | 0.557587 |
| Independent large dense, width4096 | 16,793,600 | 0 | 0.00338088 | 1 |

Legendre and Logarithmic fall below1; Harmonic does not at this fixed budget.
No tuning was performed to change that outcome. Legendre's total17,645,594
scalars exceed dense total storage: its reduction concerns moving state, not
total retained storage. Its executable counts include65,537 lifted auxiliary
coordinates beyond the canonical paper representation. The dense row charges
one model, although its error uses two independently initialized large models.

Legendre setup/fit took0.12s/52.71s; Harmonic4.87s/54.61s; parallel batch60.16s.
Final training MSEs were0.0011970 and0.0011216. Legendre's terminal lifted
activation drift maxima were0.0004342 and0.0005128, and its residual-RMS
coordinate differed from recomputed RMS by0.0020199. These are recorded
finite-Euler effects, not corrected away; the small output discrepancy is
not promoted to a comparably sharp continuous-GF certificate. Harmonic uses
its exact Gram inverse without the Logarithmic model's floor. No new
budget-specific refinement was run for either method.

The one saved-array check recomputed all four endpoints and their common
denominator, checked the65-by38 finite prediction grids, data identity,
training losses and moving/fixed counts. It passed. A scoped read-only runner
check found no invalidating reference/scoring/count defect. PNG/PDF plots
were generated and visually inspected; they label fixed storage and explicitly
omit the not-yet-run matched controls. The script's inherited reference scope
describes the consumed dense/Logarithmic reference protocol; each added method's
actual source contract is the one specified above and in its model record.

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_other_points
```

Executed fitting source SHA256:
`2673dea74a8b15b124b4b302de5018273294b244f1c874a6a6e236814d0848d4`.
New trajectory NPZ SHA256:
`065c0612b86eb8c4a061c532ea54a21ad3930167fd18aeb2fb1833fd60c73c66`.
The plotting-only command was added after the fits; its own source hash is
recorded in `point_check.json`. No training equations changed between methods.
Environment remains Python3.10.14, Torch2.9.0+cu130, NumPy1.26.4, twoRTX3090,
one Torch CPU thread and TF32 disabled; assemblyfloat64, executionfloat32.

## Authorized absolute-RMS size/accuracy curves

The user requests actual endpoint RMS (no normalization) and three smaller
dense sizes, Legendre orders1/2/3, and a corresponding Logarithmic size curve.
This continues the same figure/task, not a new dataset or seed search.
Fractions mean moving/learned scalar counts, not hidden width. The three
dense widths are2895/2047/1446, the largest integer widths within1/2,1/4,1/8
of16,793,600. They use seed10601, as does the saved large iid-dense run;
each is independent of reference seed601, but the points are not independent
seed replicates. Same canonical width-dependent initialization and mobilities.

Logarithmic widths299/210/148 fit within1/2,1/4,1/8 of its current181,480
moving scalars. Allocate source ranks19/11/6 using the previous approximately
four-coordinates-per-source-direction rule. One shared new-partition source
fit requests ranks29/19/11/6, preserving rank37 randomized SVD/seed501,
the original source-flow observation grid, readout floor and64-candidate
selector/cap16. The extra rank29 is a source prefix, not an additional fit.
No source or construction settings are chosen from prediction errors.
Legendre changes only its order to1,2,3. Reuse all four previously measured
larger points, including Harmonic, without further training.

Exactly nine new fits, the same8/30 inputs, two tanh layers, float32 Euler
step0.0015625 to time32. At most one fit per GPU, each capped120s; shared
source setup capped120s, complete command900s. One final saved-array/figure
check; no refinements, replacement seeds, failed-budget rescues or more models.
Evaluate endpoint test RMS against the same saved coupled dense run, never
ground-truth labels. The question is the observed size/error tradeoff, with
no assumption of monotonicity. Incomplete/nonfinite/grid-mismatched runs are
inconclusive, not plotted as endpoint results. Charge all fixed storage and
lifted auxiliaries. Lines join single-realization measurements, not confidence
bands, asymptotic fits or proofs of an exponent.

```sh
timeout 900 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --tradeoff --previous-points data/generated/cubic_log_comparison_20261008/sphere3_other_points --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_tradeoff --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_tradeoff
```

All nine authorized fits completed, with no replacement/rescue runs. New
measurements (the larger endpoints and Harmonic are reused unchanged):

| Method | Configuration | Moving scalars | Fixed scalars | Endpoint RMS vs dense |
|---|---|---:|---:|---:|
| Dense | half budget, width2895 | 8,392,605 | 0 | 0.00691741 |
| Dense | quarter budget, width2047 | 4,198,397 | 0 | 0.01252705 |
| Dense | eighth budget, width1446 | 2,096,700 | 0 | 0.00747569 |
| Legendre | order1 | 147,458 | 16,777,218 | 0.000689169 |
| Legendre | order2 | 212,994 | 16,777,220 | 0.000915328 |
| Legendre | order3 | 278,530 | 16,777,222 | 0.000617116 |
| Logarithmic | width299/rank19 | 90,605 | 268,204 | 0.00375374 |
| Logarithmic | width210/rank11 | 44,948 | 132,301 | 0.00643357 |
| Logarithmic | width148/rank6 | 22,504 | 65,713 | 0.01427495 |

The large iid-dense endpoint is0.00338088494, shown as its actual RMS rather
than1. Logarithmic's tested size curve is monotone; this single dense seed
and the small Legendre orders are not. Preserve these nonmonotonic outcomes:
the connecting lines are not expected-error laws. Order1's endpoint accuracy
also does not imply trajectory-wide accuracy: its maximum-time RMS is0.009218.
No result is substituted for an all-time/sphere or confidence certificate.

The complete batch took236.98s. Shared Logarithmic source setup took6.08s,
dense fits19.5–20.0s, Legendre53.5–55.1s, Logarithmic64.8–69.6s; every fit
completed the full horizon under120s. All final training MSEs lie between
0.0009875 and0.0012257. Legendre lifted activation drifts remain below0.000579,
and residual-RMS coordinate drift is0.001964–0.002036; no correction or new
step-refinement claim is made. The source partition/grid check and absence of
extra constructor truncation passed for all three Logarithmic sizes.

A scoped independent read-only check found no invalidating budgeting,
reference or per-GPU scheduling defect. The single saved-array check passed
for all13 points (nine new, four reused), reconstructing endpoint RMS,
training losses, grids, counts and common data. PNG/PDF were visually inspected.
The legend exposes fixed storage, and the y-axis is now absolute prediction
RMS. Same-size low-rank/NTK controls have not been added in this continuation.

Executed source SHA256:
`d53ed8879a6c5bd7aedffe8cfc2163395bdadc5646da301a4775b9b377066afa`.
Generated trajectory NPZ SHA256:
`6a4cc0aae3c8c75e124c26aeede18856ddb81ad52467ae1d2cade85f877be751`.
Environment matches the preceding two-point run. The nine-fit continuation
is complete; no additional experiments are pending under this batch.

## Authorized width1446 seed check and NTK point

The user clarified that the existing smallest dense width1446 should stay;
the intervening width1024 request was withdrawn before any run or code change
for it. Add only dense seeds10602/10603 to the existing10601 result, keeping
the same width4096 reference601, dataset and Euler protocol. Compute the mean
of three individual endpoint RMS values and the standard error as their
sample standard deviation (ddof1) divided by sqrt3. This uncertainty is over
dense initialization conditional on the fixed data and reference, not over
reference seeds or test resampling and not the RMS of an ensemble prediction.
Replace only the plotted width1446 measurement by this mean with an SE bar;
the other widths remain single-seed observations. Preserve all original arrays.

Add the existing exact initial-NTK finite-panel dynamics, initialized from the
same dense reference. With zero initial readout, the initial NTK is H^T H/n.
Retain8 moving dual coefficients, the8-by8 training kernel and30-by8 test
cross-kernel:304 fixed kernel scalars. The stored114 input-coordinate scalars
are common panel data and are labeled separately. No dense weights remain.
This is a panel decoder, not an arbitrary-input representation. Concatenated
train/test prediction uses the existing two kernels without duplicated storage.
Use the same20,480 explicit Euler updates; no closed-form GF substitution.

Exactly two new dense fits plus one NTK fit, at most one per GPU,120s cap
each and360s for the command. No source fitting, compression reruns, larger
seed sweep or refinement. One tiny registered-panel algebra check and one
saved-array consistency check. Failed/incomplete fits remain inconclusive;
do not drop a seed from the three-seed summary or silently replace it.

```sh
timeout 360 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --seed-check --previous-points data/generated/cubic_log_comparison_20261008/sphere3_tradeoff --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_seed_check_ntk --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_seed_check_ntk
```

All three new fits completed. Width1446 endpoint RMS values for seeds
10601/10602/10603 are respectively0.00747569037,0.01560965223,0.00759262076.
Their mean is0.01022598778, sample SD0.00466275673, and SE0.00269204385.
The previous single width1446 point is replaced only in the new plot by this
three-seed mean/error bar; its raw observation remains available unchanged.
With only three seeds, this is a small-sample conditional uncertainty estimate,
not a confidence guarantee for arbitrary data or an independently resampled
large reference. No means were computed for other widths.

Frozen NTK endpoint RMS is0.21886297776 versus the coupled dense predictions.
Its training MSE at the common endpoint is0.03137235, compared with0.00119561
and0.00117593 for the two new dense seeds. NTK therefore has not fitted to the
dense models' training-loss level by time32; no longer-horizon run is substituted.
The panel NTK is plotted at8 moving scalars, with304 fixed kernel entries and
114 panel-input scalars labeled. A marked x-axis break isolates that point
without compressing the visible scale of the earlier curves.

New dense fits took19.66s and19.65s; NTK2.96s; total23.20s. A tiny CPU check
verified concatenated-panel predictions without duplicated kernels and rejected
unregistered queries. A scoped read-only check verified the initial-kernel
normalization, seed scope, storage counts and mean/SE formula. The saved-array
check reconstructed all endpoints, time grids, state counts and new training
losses, and verified the three-seed statistics. It passed. The plot follows
the full saved-result ancestry and was visually inspected; a label-only
adjustment was then rendered with no additional fits. Other methods and
budgets are unchanged; this continuation is closed.

Executed fitting source SHA256:
`39e31ca0db4faa8946c00d9690435fef5ce7062bfbe71b12a87a91e91214049b`.
Generated trajectory NPZ SHA256:
`c48a7d9a51bcfe50da2a71a90b9b6e1690f2efc3b4d76f3f67851691a20dc87b`.

## Authorized Harmonic size curve

The user asks to turn the Harmonic point into a measured size/error curve.
Add only widths299/210/148 with source ranks19/11/6, matching the three
smaller Logarithmic moving-state budgets. Preserve the existing width424
Harmonic point, all other methods, NTK and the dense1446 three-seed mean/SE.
No new dataset, seed selection, geometry/order sweep or fitted scaling law.

Generate the existing rank29 Harmonic source once, with unchanged source
seed601, rank37 randomized SVD, degree8 time fits, degree5 spherical modes
and72 fixed sphere nodes independent of scored inputs. Lower ranks use its
leading column prefixes, rather than separate lower-rank randomized SVDs.
The shared source report's errors describe the rank29 source fit; they are
not claimed as error bounds for the smaller prefixes. Actual predictions
from each autonomous trained model supply the requested error measurements.
Keep exact unregularized readout,64 selector candidates, selector seed501,
conditioning cap16 and absence of further constructor truncation.

Same reference4096/seed601,8 training and30 passive scored inputs, horizon32,
Euler step0.0015625, float64 source assembly/float32 execution. Exactly three
new fits; shared setup and each fit capped120s, full command360s. One active
fit per GPU; no failed-budget rescue, refinement or additional configurations.
Primary score is absolute endpoint test RMS against the coupled dense run.
Incomplete/nonfinite/grid-mismatched results are inconclusive. No assumption
that accuracy improves monotonically with the selected width. One final
saved-array check and visual inspection; source/retained counts stay separate.

```sh
timeout 360 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --harmonic-curve --previous-points data/generated/cubic_log_comparison_20261008/sphere3_seed_check_ntk --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_harmonic_curve --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_harmonic_curve
```

All three fits completed without guard changes or further truncation. The
Harmonic curve now contains four measured points:

| Width | Source rank | Moving scalars | Fixed scalars | Endpoint RMS vs dense |
|---:|---:|---:|---:|---:|
| 148 | 6 | 22,504 | 65,712 | 0.0198713131 |
| 210 | 11 | 44,948 | 132,300 | 0.0124085072 |
| 299 | 19 | 90,605 | 268,203 | 0.0078964255 |
| 424, reused | 29 | 181,480 | 539,328 | 0.0046101679 |

Errors decrease over these tested budgets, but all four remain above the
measured large-dense-pair RMS0.00338088494. At each matching moving budget,
the measured Logarithmic error is lower. These are descriptive observations
for the same fixed reference, not a general superiority or scaling theorem.
Harmonic's sources still exclude scored inputs; its scope differs from the
declared-panel Logarithmic initializer. No adjustment was made to improve
the observed ordering.

Shared source setup took4.29s; widths299/210/148 trained in54.24/53.88/48.13s.
Total batch107.87s, all fits within120s. Their final training MSEs were
0.00104443,0.00102133,0.00100555. The scoped read-only source/count/branch
check passed, as did the saved-array check of all19 raw points and the
inherited dense1446 mean/SE. The updated PNG/PDF was visually inspected;
NTK, dense error bar and every preexisting result are unchanged. No additional
fit, source-rank search or numerical refinement was performed.

Executed source SHA256:
`411d246259cc650682c5a2b772c97d148f0e1cacf4bb13721aabc9c86782ba23`.
Generated trajectory NPZ SHA256:
`5c8394c8b5029231fedda7354c23285fe57e59aa7d3ba85662cffcf1872d66c0`.
This three-fit continuation is complete.

## Authorized low-rank curve and frozen-feature reference line

The user requests replacing the NTK point by a horizontal dashed accuracy
reference, and adding a range of low-rank trained adapters on the existing
width4096 backbone (the conversational4000 is this same width). Keep all
previous prediction arrays, including the dense1446 three-seed mean/SE.
The dashed line is the existing dual-kernel measurement, equivalent in exact
arithmetic to4096 trained readout weights on frozen dense features; its
position makes no storage claim. The large-dense-pair benchmark becomes dotted.

Exactly four new fits: existing BudgetLoRA with hidden ranks1,4,8,20 and first
layer rank min(rank,3). Both Gaussian matrices are frozen at the coupled
dense601 initialization; readout and both pairs of adapter factors train.
Zero left factors preserve the initialized network. Adapter seed30601 and
existing expected-initial-induced-mobility normalization are fixed, with no
fitted multiplier or source rollout. Right factors start orthonormal. These
are factor-gradient models, not optimal projected dense updates; the expected
initial normalization is not a guarantee of matching later dense dynamics.

Moving counts are16387,49161,81929,180233; fixed backbone storage is16789504
for each. Both factor matrices count as trained, and the readout counts4096.
No claim of total-state compression is made for these low-rank controls.
Keep d3, two tanh layers, m8, p30, reference601, same labels/data, physical
time32 and float32 Euler step0.0015625 (20480 updates). Scored labels and
coupled future predictions are unavailable to initialization/training.

Primary outcome: endpoint RMS against the saved coupled dense on30 inputs,
plotted against actual moving scalar counts. This tests whether low-rank
adaptation alone attains similar measured fidelity at roughly comparable
learned budgets, without assuming an ordering or monotonicity. Every finite,
complete common-grid result is reported; nonfinite/incomplete runs remain
inconclusive, with no replacement rank/seed or learning-rate rescue. No
continuous-GF or exponent claim follows. As in the preceding curves, no
new rank-specific Euler refinement certificate is asserted.

Before fitting, run the existing tiny autograd/initial-field/full-rank-mobility
oracles and exact storage checks. One active fit per GPU, each capped120s,
setup capped120s, total command360s; stop after four fits and one saved-array
check/visual inspection. Root owns the code and record. A scoped read-only
checker covers adapter normalization/counts and device movement. No other
method, dataset, width or seed is rerun.

```sh
timeout 360 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --lowrank-curve --previous-points data/generated/cubic_log_comparison_20261008/sphere3_harmonic_curve --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_lowrank_curve --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_lowrank_curve
```

All four requested fits completed. The same step and horizon are used for
every compared model; these are errors against dense predictions, not labels.

| Hidden rank | First rank | Moving scalars | Endpoint RMS vs dense | Final training MSE | Fit seconds |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 16,387 | 0.101852977 | 0.000332131 | 41.57 |
| 4 | 3 | 49,161 | 0.258924267 | 0.00000127759 | 42.16 |
| 8 | 3 | 81,929 | 0.240833518 | 0.00000395046 | 41.81 |
| 20 | 3 | 180,233 | 0.201166451 | 0.00000357025 | 42.16 |

The complete batch took85.41s on twoRTX3090s; adapter setup took0.001–0.047s
per rank after generating the shared initial dense network. All runs fit the
training labels well but remain30.1–76.6times the measured large-dense-pair
endpoint discrepancy0.00338088494. Increasing rank does not improve error
monotonically. No point, learning-rate multiplier or seed was selected after
scoring. The shared seed does not make different-shaped factor subspaces
nested. This is evidence about this untuned factor-gradient control, not a
lower bound for all low-rank optimizers. No rank-specific step refinement or
continuous-flow claim is made.

The frozen-feature reference is now dashed at0.218862978, with no x-coordinate
or axis break; dense-pair discrepancy is dotted. All previous observations
and the three-seed error bar are preserved. Fixed backbone storage16789504
is labelled separately for every low-rank point. Thus low-rank adapters and
Legendre save moving coordinates here, not total retained coefficients.

The existing tiny CPU checks passed: initial-field error0, factor-gradient
error1.11e-16, full-rank induced-mobility error7.63e-17, kernel-Euler error
6.94e-18, and seven budget cases. The scoped read-only review checked factor
normalization/counts and caught a device-transfer omission before execution;
the frozen first matrix is now moved/cast together with the hidden matrix.
The final saved-array check passed for all23 raw points, including every
65-by38 prediction grid, common inputs/times, endpoint RMS, trained/fixed
counts, new training losses and inherited mean/SE. PNG/PDF were visually
inspected. No additional experiments were run.

Executed source SHA256:
`b14e23e0113452d6cfa5987473cc83cee6ff3df20e0d21455dd3208303c2e97b`.
Generated trajectory NPZ SHA256:
`9c29a0632deda8078daf40669fdbb8a9ab72d74724116b7f2e12531796d005f3`.
The environment remains Python3.10.14, Torch2.9.0+cu130, NumPy1.26.4,
one Torch CPU thread, TF32 disabled, float64 initialization and float32 Euler.
This four-fit continuation is complete.

### Independent reference repetitions, limited to two new dense fits

The user explicitly permits exactly two new large-dense runs, with no other
training. Run width4096 seeds602/603 at the unchanged sphere3 task, data seed47,
m8,p30,L2,tanh, float64 initialization cast to float32, Euler h0.0015625,T32,
20480steps,65 observations. One fit per GPU,120s per fit,300s command cap.
No new compact/control fits, tuning, retries or numerical refinements.

Re-score stored three-seed dense groups using pairs (10601,601), (10602,602),
(10603,603). These repetitions have independently initialized references,
conditional on the same data; different widths still share references within
each repetition. Single-run compression/control curves retain their original
coupled reference601. Four available large-dense trajectories allow only two
disjoint dense-pair scores: (601,10601) and (602,603). Show their median and
observed range, explicitly two pairs, not three independent repetitions.
No accuracy-based exclusion. Failed finite-output/data/grid/count gates are
inconclusive with no rescue. Fresh output sphere3_reference_seeds continues
sphere3_compression_larger; `sphere-points --reference-seeds` runs only the
two new references. Re-pairing/plotting use stored arrays exclusively.

Exactly two fits completed in21.77s total command time,21.09s/20.89s each.
Final training MSEs for602/603 are0.001092467/0.001205591. All27 stored
small-dense scores were re-paired; single-run compression/control scores
remain unchanged. The displayed median scores are:

| Dense width | Independent pair count | Endpoint RMS | Worst recorded-time RMS |
|---:|---:|---:|---:|
| 148 | 3 | 0.03393410100 | 0.05608408401 |
| 253 | 3 | 0.02443692960 | 0.03089660660 |
| 509 | 3 | 0.01407745555 | 0.02178637892 |
| 1021 | 3 | 0.01002058161 | 0.02113582725 |
| 2047 | 3 | 0.01007477849 | 0.01252704651 |
| 4096 | 2 | 0.006383352230 | 0.01237977772 |

The new large pair602/603 has endpoint RMS0.00938581952 and worst-time
RMS0.01682322481. Together with the old disjoint601/10601 pair, it defines
the new4096 point, dotted benchmark and observed min–max bar. With two
observations the median is their arithmetic midpoint. Three-seed smaller
widths aggregate their individual pair scores, taking each temporal maximum
before the median for the worst-time plot. These repetitions are independent
within a width conditional on the fixed data, not independent across widths
or from the benchmark; references are shared within each repetition.

Both paired PNG/PDFs were visually inspected and saved-array checks passed.
Raw/common-reference measurements are preserved in `points`; newly re-paired
measurements are separately recorded in `paired_comparisons`, together with
the second disjoint large-pair score and explicit pairing metadata. There
were no compression/control runs, new widths, retries, or refinements.

```sh
timeout 300 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --reference-seeds --previous-points data/generated/cubic_log_comparison_20261008/sphere3_compression_larger --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_reference_seeds --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_reference_seeds --metric endpoint --seed-statistic median --thin-dense --clean --independent-references
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_reference_seeds --metric max-time --seed-statistic median --thin-dense --clean --independent-references
```

Executed fit-source SHA256: `c179cfe4b1672850e500b4a8489c81d044c82a982909555073cd9923cdfbac2b`.
Trajectory SHA256: `6edda0b2bdc90b20f814cb16c17fc484bfc44ac4fee5a8de6379aa52bc4ac6ea`.
Environment/precision unchanged. The subsequent plot-only edits have their
own source hashes in the figure check files. Final outputs in
sphere3_reference_seeds are endpoint_points_median_thinned_clean_paired
and max_time_points_median_thinned_clean_paired, with separate caption files.
The scoped checker independently reconstructed all27 small-pair scores and
both large-pair scores directly from NPZs, verified both sets of medians/ranges,
matched data/grids/losses and the exact two-run count, and confirmed all53
inherited raw points and single-run compression/control metrics are unchanged.
No issues were found. This two-fit continuation is complete.

### Two larger Harmonic and Logarithmic sizes

The user requests two additional larger points for each compression curve.
Use2x/4x the current largest181480 moving-coordinate budget, giving widths600
and850, actual moving counts362408 and725908. The existing rank-to-budget
rule gives source ranks44 and65. Exactly four new single-witness fits, no
seed/selector searches beyond the unchanged64 candidates, and no tuning or
replacement fits. Primary output is endpoint RMS against the same dense4096
reference; preserve the latest dense three-seed medians and thinned display.
Report all outcomes, including nonmonotone accuracy; no accuracy-based exclusion.

Keep sphere3,m8,p30,L2,tanh, source RK4 step0.125 throughT32, degree8 time
fits, Harmonic degree5/72-node independent input quadrature, and Logarithmic
declared38-input panel with labels withheld. Harmonic sources are computed
once at rank65 using seed601 and prefixed to44; Logarithmic sources use the
unchanged new partition with nested ranks65/44 and seed501. Larger randomized
SVD workspaces do not make these spans nested with the old rank29 source;
old measured points remain intact. No full-source or initialization-only
certificate is newly asserted. Runtime stays float32 Euler h0.0015625,T32,
20480steps,65 observations; assembly stays float64, TF32 disabled.

Gate source ranks, widths, condition<=16, no fallback source truncation,
finite outputs, matching data/time grids, actual storage and endpoint RMS.
Retain the original Logarithmic readout floor and Harmonic exact readout.
Cap each source setup and fit at120s, whole command600s; one fit per GPU.
A failed gate is inconclusive, with no rescue or new settings. Stop after
these four fits. Root owns code/notes; a scoped checker independently verifies
the new points and preservation of the previous figure's data. Fresh output:
data/generated/cubic_log_comparison_20261008/sphere3_compression_larger,
continuing sphere3_mid_seeds, via `sphere-points --compression-larger`.

All four fits completed without errors, in156.29s total command time.
Shared source setup took4.46s for Harmonic and5.73s for Logarithmic; model
assembly took0.88–1.17s each. Euler fits took54.06/54.01s for Harmonic600/850
and69.38/71.99s for Logarithmic600/850. Final training MSEs are0.001117–0.001194.

| Width | Moving scalars | Harmonic fixed | Logarithmic fixed | Harmonic endpoint RMS | Logarithmic endpoint RMS |
|---:|---:|---:|---:|---:|---:|
| 600 | 362,408 | 1,080,000 | 1,080,001 | 0.003376969634 | 0.001358723459 |
| 850 | 725,908 | 2,167,500 | 2,167,501 | 0.003490483667 | 0.0004004948285 |

The dense-pair endpoint RMS remains0.00338088494. Harmonic's second larger
point is slightly worse than its first; that nonmonotonicity is retained.
Logarithmic improves at both larger sizes. These are single witnesses with
unchanged finite-Euler and empirical full-rollout source qualifications, not
a source certificate or a fitted asymptotic scaling law. Existing49 raw
points, all dense seed summaries and the thinned display are preserved.
The saved-array plotting checks passed, and the updated PNG was inspected.
One label offset was adjusted after the runs to avoid overlap with Legendre.

```sh
timeout 600 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --compression-larger --previous-points data/generated/cubic_log_comparison_20261008/sphere3_mid_seeds --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_compression_larger --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_compression_larger --metric endpoint --seed-statistic median --thin-dense
```

Executed source SHA256: `2869097b35e6604b1107767178e4414ecb74cb8f851ed02ba6e22c968f4aacdf`.
Trajectory SHA256: `55209ab7efb22a03ea2658f5e18205c0683b6e8a57d0faedf3e50bce6f5ffffc`.
Same recorded software, precision, one-thread and two-GPU settings.
Final PNG/PDF: sphere3_compression_larger/endpoint_points_median_thinned.
The scoped checker independently reconstructed all four endpoints and training
losses, verified counts/data/grids, source conditions and absence of fallback
truncation, and confirmed the49 inherited points/nine seed groups are unchanged.
The largest source condition is14.627884, below16. No fresh step refinement
was performed; the check does not strengthen the numerical qualification.
This four-fit extension is complete; no further fits or rescues were made.

### Clean figure with separate caption

At the user's request, `sphere-points-plot --clean` produces a presentation
variant with title `3D sphere`, axes `Learned state` and `Test RMS`, short
legend names, and no point annotations or embedded footer. All measurements,
median/range bars and reference-line heights are unchanged. The point orders,
seed qualifications, exact fixed-storage counts, training protocol and empirical
source limitations move into adjacent `.caption.txt` and `.caption.tex` files
generated by the same script. No experiments were run. Output/check filenames
gain `_clean`, preserving previous figures. The clean PNG was visually checked.
The scoped equality check confirmed unchanged points, medians, ranges and
reference values; caption storage ranges match the displayed models exactly.
Its wording clarification specifies that Harmonic quadrature nodes are fixed
and independent of the scored inputs, not independent random samples.

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_compression_larger --metric endpoint --seed-statistic median --thin-dense --clean
```

### Frozen features as a trained-readout point

The user now requests the frozen-features baseline as a dot, using the full
width4096 frozen dense network with only its readout trained. Add
`--frozen-point` to the preceding plotting command. The dot is at4096 learned
coordinates and the unchanged endpoint RMS0.21886297775687721; its frozen
backbone retains16789504 additional weights, total16793600. The displayed
storage uses this primal architecture, while the original8-state/304-fixed
finite-panel dual-Euler implementation and its measurements remain unchanged
in the raw report/check data. Captions explicitly distinguish the two; no
new primal training run is implied. All other points/bars and their scores
are unchanged. The x-axis expands to include the dot. New PNG/PDF/caption/check
files use the additional `_frozen_point` suffix, preserving the dashed-line
version. Plot consistency checks passed and the figure was visually inspected.

## Authorized low-rank / Legendre rank-capacity matching

The user requests replacing the displayed low-rank ranks by equivalents of
Legendre order. Each order-q moment array has shape(q,n,m), and flattening
mode/sample indices produces an n-by(qm) factor. The hidden increment is the
product of two such factors, so its rank is at most min(n,qm), not q. With
m8, displayed orders1/2/3/12 therefore match adapter ranks8/16/24/96. This
is a rank-capacity match, not an equality of the realized numerical ranks,
training dynamics or stored-coordinate counts.

Reuse the completed rank8 run and add only ranks16,24,96. Existing BudgetLoRA,
coupled dense601 initialization, adapter seed30601, zero left factors,
orthonormal right factors and factor mobilities remain unchanged. Every new
and reused matched control has full first-layer rank3, eliminating the earlier
rank1 versus rank3 first-layer change within the displayed series. Different
factor shapes with one seed need not give nested subspaces. No source rollout,
label-based selection, learning-rate tuning or replacement seed is introduced.

The matching counts are:

| Legendre order | Low-rank hidden rank | Low-rank moving scalars | Legendre moving scalars |
|---:|---:|---:|---:|
| 1 | 8 | 81,929 | 147,458 |
| 2 | 16 | 147,465 | 212,994 |
| 3 | 24 | 213,001 | 278,530 |
| 12 | 96 | 802,825 | 868,354 |

Legendre stores two additional n-by-m lifted feature arrays and two scalars;
BudgetLoRA's full-rank first-layer factorization costs nine scalars more than
Legendre's directly trained first matrix. Consequently these rank-matched
moving counts differ by65529, which is preserved on the x-axis. Low-rank fixed
storage remains16789504. Earlier ranks1/4/20 remain in the raw evidence but
are excluded from this requested rank-matched plot by an explicit display
policy. No observed-error criterion determines the displayed ranks.

Same d3,L2,tanh,m8,p30, reference4096/601, float32 Euler h0.0015625,T32,
20480 updates, same65 observations and withheld query labels. Primary metric
is endpoint RMS against the saved dense predictions. No monotonicity is
assumed. Nonfinite/incomplete/common-grid failures are inconclusive; no rescue
or new step refinement. Three fits only, one per GPU at a time,120s per fit,
360s total. Reuse existing gradient oracles since the low-rank equations are
unchanged; check rank/count correspondence, then one saved-array consistency
check and visual inspection. Root owns code/notes; scoped read-only checking
covers the exact rank correspondence and storage qualifications.

```sh
timeout 360 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --lowrank-legendre --previous-points data/generated/cubic_log_comparison_20261008/sphere3_lowrank_curve --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_lowrank_legendre --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_lowrank_legendre
```

All three new fits completed. The rank-matched comparison is:

| Legendre order | Low-rank hidden rank | Low-rank endpoint RMS | Legendre endpoint RMS |
|---:|---:|---:|---:|
| 1 | 8, reused | 0.240833518 | 0.000689169 |
| 2 | 16 | 0.214446870 | 0.000915328 |
| 3 | 24 | 0.189105862 | 0.000617116 |
| 12 | 96 | 0.150747994 | 0.0000593923 |

For this displayed rank range low-rank error decreases with rank, but remains
far above Legendre at matched hidden-increment rank capacity. This is a
comparison of these specific update rules, not proof that all low-rank
optimizers fail. The earlier rank1 result remains in the original evidence
and remains better than these four; it was omitted here solely to implement
the user's predeclared rank-matching request, not because it failed a gate.

Ranks16/24/96 trained in41.92/42.57/38.44s, with final training MSE
2.15e-6/8.23e-6/4.17e-5. New adapter assembly took0.053/0.0095/0.0045s;
the complete batch took81.35s. Only three new fits occurred. Rank8, all
Legendre/Harmonic/Logarithmic/dense predictions and the NTK measurement were
reused unchanged. No new rank-specific refinement was performed.

The scoped rank/storage check and final saved-array consistency check passed.
The latter verifies all26 raw points, common grids/data, derived losses/RMS,
counts, inherited mean/SE and requested displayed-rank mapping. The PNG/PDF
was visually inspected, with only label placement adjusted afterward. Earlier
ranks1/4/20 remain stored but do not appear in this replacement low-rank curve.

Executed fitting source SHA256:
`e67ce1166f2e0f99d004c97c7bfd55a2b316762fc1ff45816c64d05a1701ca5b`.
Generated trajectory NPZ SHA256:
`8d42c7468c6c8c64c2c92eaa21ddfcae0fbca772a3775701506b16265118549c`.
The plotting-only label change is separately hashed in point_check.json.
Environment, initialization precision, Euler precision and hardware remain
unchanged. This three-fit continuation is complete.

## Authorized two smaller dense points

The user requests dense points at half and quarter of the current smallest
dense model's size. As in the earlier clarified budget convention, fractions
refer to parameter counts, not hidden widths. The current smallest width1446
has2096700 trained parameters. Largest integer widths within budgets1048350
and524175 are1021 and722, with1046525 and524172 parameters respectively.
All dense weights train; there is no fixed model state.

Run exactly these two models with seed10601, matching the single-seed convention
of other dense sizes and remaining independent of the coupled reference601.
Retain the existing width1446 three-seed mean/SE; do not turn the new single
measurements into means or claim error bars. Same d3,L2,tanh,m8,p30, reference
width4096, initialization law/mobilities, float32 Euler h0.0015625,T32,
20480 updates and65 observations. Primary metric is endpoint test RMS against
the same saved dense predictions, not label loss. No monotonicity is assumed.

Two fits, one per GPU,120s each and240s total. No seed replacements, additional
widths, tuning or new step refinement. Nonfinite/incomplete/grid-mismatched
results remain inconclusive. Preserve all previous curves, the matched low-
rank display policy, and dashed frozen-feature reference. One saved-array
check and visual inspection after fitting. A scoped read-only checker verifies
the parameter-budget arithmetic; root owns code and notes.

```sh
timeout 240 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --dense-smaller --previous-points data/generated/cubic_log_comparison_20261008/sphere3_lowrank_legendre --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_dense_smaller --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_dense_smaller
```

Both requested fits completed, with no additional runs:

| Budget relative to width1446 | Width | Moving/total scalars | Endpoint RMS vs dense | Final training MSE |
|---|---:|---:|---:|---:|
| Half | 1,021 | 1,046,525 | 0.00465754127 | 0.00125394110 |
| Quarter | 722 | 524,172 | 0.00719115089 | 0.00116042653 |

Each fit took19.34s; the parallel batch took19.91s. Endpoint errors are1.378
and2.127times the unchanged measured dense-pair discrepancy0.00338088494.
These are single-seed observations; the resulting dense size curve is not
monotone and is not an estimate of an expected scaling law. No seed was
replaced or added. The width1446 three-seed mean/SE is unchanged, as are all
compressed and low-rank curves and the frozen-feature reference.

The scoped size-budget check and saved-array check passed: all28 raw points,
common grids/data, new prediction-derived losses, RMS and state counts,
inherited mean/SE and matched-rank display policy. The updated PNG/PDF was
visually inspected; no plot-only label adjustment was needed. No new-width
Euler refinement or continuous-flow certificate is claimed.

Executed source SHA256:
`f749c28926c041123c81ccfe1c019de0a4928a6a07d8b0cc32acd95867444654`.
Generated trajectory NPZ SHA256:
`357886a1b5aabfc2a5ea2ec96320fb4693d5adf9216f5e935ba14a082faee6a9`.
Environment and precision are unchanged. This two-fit continuation is complete.

## Worst-recorded-time version of the same figure

At the user's request, replot the existing trajectories using the maximum,
over the65 common times0,0.5,...,32, of RMS prediction discrepancy over the
30 test inputs. This is maximum-in-time of spatial RMS, not RMS of pointwise
temporal maxima, a time average, or a continuous-time supremum. No model is
rerun and no raw results, endpoint figure or consumed report is overwritten.
The script's new `--metric max-time` option writes max_time_points.png/pdf
and max_time_point_check.json alongside the unchanged endpoint outputs.

Both reference lines use the new metric: large-dense pair0.00793633063,
frozen-feature baseline0.55220750243. Width1446 uses the mean of the three
individual-seed temporal maxima,0.01606239312, with SE0.00496894477. This is
not the maximum of the three-seed mean RMS curve. All other plotted points
remain individual realizations. Actual state counts and matched-rank display
policy are unchanged.

The dense worst-time values at widths722/1021/1446/2047/2895/4096 are
0.00719115089/0.02113582725/0.01606239312/0.01252704651/0.00800657363/
0.00793633063 (width1446 is the mean described above). The endpoint can hide
transient discrepancies: width1021 peaks at time2, with worst RMS4.54times
its endpoint value. The width curve remains nonmonotone; this is not an
averaged scaling-law estimate.

A scoped checker independently recomputed all28 trajectories and confirmed
the plot uses the selected metric for every point, reference line and SE.
The saved-array checks passed, and the PNG was visually inspected; its
vertical label was shortened for readability. The check JSON records source
and trajectory hashes and the per-seed metric values. No new precision or
continuous-flow certificate is asserted.

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_dense_smaller --metric max-time
```

## Authorized two-seed check of the smallest dense model

The user asks whether the unexpectedly good smallest dense point survives two
additional initializations. Run only width722 (524172 trained parameters),
seeds10602/10603, alongside the existing seed10601 from sphere3_dense_smaller.
New names dense_n722_seed10602/10603 avoid collision with the width1446 seed
replicates. The dataset, width4096/reference601, two tanh layers, m8/p30,
float32 Euler h0.0015625,T32 and65 recorded times remain fixed. Test labels
are used neither to train nor to select seeds. Exactly two fits, one per GPU,
120s each, command cap240s; no replacement seeds, other widths or refinement.

Primary metric is each seed's maximum-over-recorded-time test RMS. Plot the
mean of these three scalar maxima with sample SD/sqrt3; this is not the maximum
of an averaged trajectory. Preserve the older width1446 mean/SE group, all
other raw observations and the rank-matched low-rank display. Each group uses
the same metric consistently. Store individual outcomes regardless of ordering;
failed/incomplete/nonfinite/grid-mismatched fits remain inconclusive, without
silently dropping a seed. The check addresses this initialization, dataset
and reference only, not a width-scaling law or population confidence guarantee.

Root owns code/notes; a scoped read-only checker verifies distinct group/seed
identities and independently recomputes the two groups' statistics. One saved-
array check and visual inspection follow the two fits, with no expanded campaign.

```sh
timeout 240 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --smallest-seed-check --previous-points data/generated/cubic_log_comparison_20261008/sphere3_dense_smaller --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_smallest_seeds --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_smallest_seeds --metric max-time
```

Both new fits completed. Width722 results (maximum over65 saved times):

| Seed | Worst-time test RMS | Endpoint test RMS |
|---:|---:|---:|
| 10601, reused | 0.00719115089 | 0.00719115089 |
| 10602 | 0.02970791188 | 0.02184131559 |
| 10603 | 0.01864839611 | 0.01864839611 |
| Mean | 0.01851581963 | 0.01589362086 |
| Standard error | 0.00650036701 | 0.00444778677 |

The original very low error did not recur in either added seed. It is the
best of these three observations, not representative of their average.
The mean worst-time RMS is about2.33times the fixed large-dense-pair benchmark
0.00793633063. Three seeds still give a small-sample conditional estimate, not
a population confidence or width-scaling conclusion. The new worst errors
occur at time2 and32 respectively; endpoint and worst-time metrics remain
distinct. Final training MSEs are0.00122048 and0.00128505.

Fits took19.46/19.61s; total20.13s. The figure now shows both width722 and1446
as three-seed means with SE bars. The width1446 worst-time mean0.01606239312
and SE0.00496894477, all other observations, the matched-rank low-rank display
and both reference lines are unchanged. Old raw points/figures are preserved.

The scoped checker independently reconstructed the new errors and both seed
groups from saved arrays; the plotting check passed for all30 raw points,
grids/data, parameter counts, losses and summaries. Width-qualified names avoid
overwriting earlier replicate identities. The final PNG/PDF was visually
inspected. No seed replacement, extra run, or step refinement occurred.

Executed source SHA256:
`f319d819315c377e414bd09922811f4e040260a2f8d9b9c782f388a1c91307c3`.
Generated trajectory NPZ SHA256:
`87989a7eae20e18cda08d72aeca414923758901f99a3987235dccb088a6c1918`.
Environment and precision are unchanged. This two-fit continuation is complete.

## Median display for replicated widths

The user requests medians instead of means wherever multiple seeds exist.
The plotting-only `--seed-statistic median` option centers each replicated
width on the median of its three per-seed scores and replaces mean-SE bars
with the observed minimum–maximum range. These ranges are descriptive, not
confidence intervals or median standard errors. With the current max-time
metric, the median is taken after each seed's temporal maximum.

Width722 has median0.01864839611 and observed range0.00719115089–0.02970791188.
Width1446 has median0.01490965744 and range0.00809039055–0.02518713138. Single-
seed points, both reference lines, raw arrays and prior mean plots are unchanged.
The new PNG/PDF/check JSON have a `_median` suffix. Both medians/ranges were
independently checked, the saved-array checks passed, and the figure was
visually inspected. Only label placement was adjusted to avoid the range bars.
No new model runs or numerical refinement occurred.

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_smallest_seeds --metric max-time --seed-statistic median
```

## Authorized dense budget descent with live median updates

The user requests further half-sized dense models with three seeds at every
size, stopping near width150/the smallest compression budget, with a figure
update after each size. Starting from width722's524172 parameters, choose the
largest integer widths within successive half-parameter budgets:509,359,253,
178. Finish with width148, whose22496 parameters match the smallest compressed
model's22504 to within eight scalars. This last point is an explicitly stated
budget-matched stop, not another exact halving. Counts are261117,130317,65021,
32396,22496. No widths below148 are authorized in this continuation.

Exactly fifteen fits: seeds10601/10602/10603 for each new width, no replacement
seeds, rank/source changes, refinements or tuning. Same d3,L2,tanh,m8,p30,
reference4096/601, initialization law/mobilities, float32 Euler h0.0015625,T32,
20480 updates and65 observation times. Primary metric: maximum recorded-time
test RMS against the fixed dense reference. Report the median and observed
min–max across the three seeds, not a confidence interval. Preserve all earlier
curves and seed groups. A group is plotted only when all three fits complete
and pass finite-output/grid/data/count checks; otherwise stop and report that
group inconclusive without dropping seeds or extending the campaign.

Use the existing two-GPU queue, one active fit per GPU,120s per fit,300s per
width command,1500s cumulative fitting-command cap. Expected runtime remains
well below these caps. Run one width group at a time; then check/render and
show its updated median figure before advancing. The same plotting command
checks all previously consumed arrays and seed groups; no repeated broader
audit or new theoretical assertion. Root owns code/notes; a scoped read-only
checker verifies budgets/group preservation and the final statistics.

Reproduction uses the single executable's `sphere-points --dense-width WIDTH`
option with the usual reference/logarithmic paths, `--devices cuda:0 cuda:1`,
and a fresh output folder. Start `--previous-points` at sphere3_smallest_seeds,
then use each completed folder as the next input. Output folders, in order,
are sphere3_dense_n509, sphere3_dense_n359, sphere3_dense_n253,
sphere3_dense_n178, sphere3_dense_n148 under this study's generated namespace.
Each report preserves the exact command and input/source hashes. After each:

```sh
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run OUTPUT_FOLDER --metric max-time --seed-statistic median
```

All fifteen fits completed, with live plot updates after each three-seed group:

| Width | Trained/total scalars | Median worst-time RMS | Observed seed range | Group run seconds |
|---:|---:|---:|---:|---:|
| 509 | 261,117 | 0.02023050853 | 0.01638162183–0.02958234284 | 36.81 |
| 359 | 130,317 | 0.03126300512 | 0.01735477148–0.03759980099 | 36.11 |
| 253 | 65,021 | 0.03089660660 | 0.01996536841–0.03129052258 | 36.32 |
| 178 | 32,396 | 0.02570755221 | 0.02538072683–0.02684648920 | 36.03 |
| 148 | 22,496 | 0.05328507442 | 0.03724532061–0.05668228589 | 36.19 |

The five run commands sum to181.47s, excluding plotting/tool overhead. Each
individual fit took16.45–19.47s, and every final training MSE is between
0.001132 and0.001487. All45 raw points, including prior observations, remain
in the final report's provenance chain. The final seven replicated widths
are1446,722,509,359,253,178,148, each with the same three seed identifiers;
the figure plots per-width medians and observed ranges, not a confidence band.
Cross-width reuse of seed numbers is not an independent dataset/reference
replication. The nonmonotone359/253/178 segment is preserved without tuning.

At the terminal nearly matched moving budget, dense148 median worst RMS is
0.0532851, versus the existing single Harmonic148 result0.0198713 and single
Logarithmic148 result0.0142750. The compressed models retain22504 moving
coordinates and65712/65713 fixed coefficients; dense148 retains22496 moving
weights and no fixed model weights. Thus the learned-state comparison is
near-exact, but total retained storage and replication counts differ. This
is a fixed-data/reference empirical comparison, not an asymptotic exponent
or universal ordering. No endpoint metric is substituted for worst-time RMS.

The scoped checker independently recomputed all fifteen new trajectories,
their counts, losses and endpoint/worst metrics, checked shared data and the
65-time grid, and confirmed preservation of earlier seed groups and low-rank
display settings. The plotting checks passed at every group, and each PNG
was visually inspected. Repeated per-point seed labels were removed once
the curve became crowded; the caption and error bars retain that information.
This was the only between-group source change and does not affect training.
No new widths, replacement seeds, numerical refinement or rescue were added.

Executed source SHA256 for509:
`112492f08c521ba69b94e167e9443ab5804ebc51354a95dfdbe25548fbd7a724`.
Executed source SHA256 for359/253/178/148:
`52b468e013358187ec7b44148908c9dcb24aac985fa46842595b8f957295d3a6`.
Trajectory NPZ SHA256 values in width order:

- 509: `096d04a9a95d2de20a2ae4d5b2ff6cc648a80dd162f23da2d75efa8de432c97b`.
- 359: `3f324d577af50b8a9352c57752ac4565b1eb2105a4718683ee21a90eec620ed0`.
- 253: `acd7eeee79caee91af0c4c5b1d1d91f3cfb2cb0fd737790c1b605a06343eb197`.
- 178: `6ca3d71d560ed0b214b26a5f0ac14f60968d6768fd560f811b786ffee1bf3b21`.
- 148: `13fff948de50082cc92b5b046d2aec6c24737b62154c0111b7d354733f10ce0e`.

Environment remains Python3.10.14/Torch2.9.0+cu130/NumPy1.26.4, twoRTX3090s,
one Torch CPU thread, TF32 disabled, float64 initialization and float32 Euler.
The final figure is sphere3_dense_n148/max_time_points_median.png (also PDF).
This fifteen-fit continuation is complete and stops at the agreed budget.

### Thinned dense display

At the user's request, the plotting-only `--thin-dense` option keeps alternate
dense widths in ascending order, including both endpoints:148,253,509,1021,
2047,4096. All raw results and earlier plots remain intact. Legend entries now
omit their parenthetical suffixes; fixed-storage counts move to the caption.
Only the three displayed replicated widths148,253,509 are listed in the seed
caption. No model is rerun and no score or error bar is changed. Reproduce with
the preceding `sphere-points-plot` command on sphere3_dense_n148, adding
`--thin-dense`; outputs have the additional `_thinned` suffix. Saved-array
consistency and display-subset checks pass; the PNG was visually inspected.

### Two additional seeds at widths1021 and2047

The user authorizes exactly four new fits: seeds10602/10603 at each existing
width1021/2047, reusing the original10601 observations. This checks how much
the two single-seed endpoint observations vary with initialization, without
changing any method or selecting seeds by performance. Primary output is the
same thinned endpoint-RMS figure, with three-seed medians and observed min–max
bars at these two additional widths. Report every valid outcome; there is no
accuracy-based exclusion or claim of population significance from three seeds.

Same sphere3 data/reference601, m8,p30,L2,tanh, canonical initializations and
mobilities, float64 assembly and float32 Euler h0.0015625,T32,20480steps,
65 saved times. Final training MSE, finite65-by38 predictions, exact data/time
grids, counts and reconstructed RMS are checked. A numerical/runtime failure
is inconclusive, with no replacement run. One fit per GPU,120s per fit,
300s total command cap; stop after four fits. No new widths, tuning or
refinement. Root owns code/notes; a scoped read-only checker verifies the
four new trajectories and preservation of the existing data/plot interface.
Fresh output: data/generated/cubic_log_comparison_20261008/sphere3_mid_seeds,
continuing sphere3_dense_n148. The single executable's new
`--dense-extra-seeds 1021 2047` continuation runs only the missing seeds.

All four fits completed in39.59s for the two-GPU run command,19.40–19.64s
per fit. Final training MSEs are0.001139–0.001242. Endpoint test RMS against
the unchanged width4096 reference is:

| Width | Seed10601, reused | Seed10602 | Seed10603 | Median | Observed min–max |
|---:|---:|---:|---:|---:|---:|
| 1021 | 0.00465754127 | 0.01773958316 | 0.00946705843 | 0.00946705843 | 0.00465754127–0.01773958316 |
| 2047 | 0.01252704651 | 0.01061779148 | 0.00864759948 | 0.01061779148 | 0.00864759948–0.01252704651 |

The new summaries replace the single-seed display, not the original raw data.
All prior observations remain unchanged. The thinned figure still shows
widths148,253,509,1021,2047,4096; its first five points now have three-seed
medians/ranges. The large–large endpoint benchmark remains0.00338088494.
Bars describe initialization variation conditional on this fixed task and
reference, not confidence intervals or independent task replications.
Saved-array consistency checks passed and the updated PNG was visually
inspected. No extra widths, seeds, tuning, or refinement were performed.

```sh
timeout 300 /home/amir/miniconda3/bin/python -B -u paper/figures/capture_trajectory.py sphere-points --dense-extra-seeds 1021 2047 --previous-points data/generated/cubic_log_comparison_20261008/sphere3_dense_n148 --reference data/generated/cubic_log_comparison_20261008/paired_run/sphere3_seed601 --logarithmic data/generated/cubic_log_comparison_20261008/sphere3_new_4_trials64 --out data/generated/cubic_log_comparison_20261008/sphere3_mid_seeds --devices cuda:0 cuda:1
/home/amir/miniconda3/bin/python -B paper/figures/capture_trajectory.py sphere-points-plot --run data/generated/cubic_log_comparison_20261008/sphere3_mid_seeds --metric endpoint --seed-statistic median --thin-dense
```

Source SHA256: `c8e8f66923cc297e396484075492da0063503c3fb0287674cd8ab2cf44be06f9`.
Trajectory SHA256: `ca31de428349fa1b97f44d0f7bbf57a881eb881abd124b3a4624fa162eb2bbb3`.
Same previously recorded Python/Torch/NumPy, GPUs, thread and precision settings.
Final figure: sphere3_mid_seeds/endpoint_points_median_thinned.png, also PDF.
The scoped checker independently reconstructed all four endpoint errors,
both medians/ranges, data/time grids and counts; it confirmed all45 inherited
points and prior seed summaries are unchanged and no original seed was rerun.
This four-fit continuation is complete.
