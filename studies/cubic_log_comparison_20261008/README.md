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
