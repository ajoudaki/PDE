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
Fresh scientific experiments are pending. No claim of improvement is made yet.

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
