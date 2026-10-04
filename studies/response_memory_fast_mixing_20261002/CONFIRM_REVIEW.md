# Independent confirmation and scaling evidence review

Verdict: **PASS for the fixed five-metric initialization-confirmation gate and
the two independently reproduced width-8192 trajectories.** The recorded
width-16384 time and peak-memory ratios also pass their numerical thresholds.
This review supports those bounded empirical statements, not a universality
theorem, improved predictive risk, or an architectural breakthrough. The
width-16384 TF32-versus-IEEE and exact-repeat checks are being audited separately
by the supervising task; this review does not independently certify those
additional artifacts.

The review used the assigned current producer, all three preserved producer
versions, the confirmation protocol and aggregation script, and the original
`training02`, `refinement01`, `confirmation01`, and `scaling01` artifacts.
It independently reconstructed the metrics from raw predictions/activations,
checked reported losses against saved labels, and reran two cases on reserved
GPU0. No scientific producer source was changed. The earlier review's missing
activation-artifact objection is resolved by v2 and later saved arrays.

## Frozen sources and version scope

| Source | SHA-256 |
|---|---|
| Confirmation protocol at review start and in original confirmation/reviewer run configs | `6f659f9699c932bf07c7390da25f8244d44d49bad0b8b64d1b466c473502e7e5` |
| Protocol after verification-only allowance was appended | `f8d78795571c77a7629c5d43e79980725d4cc202bf1e505e6304e3f4c00b3a80` |
| Current `fast_training.py` | `7ac6e50064cff7b33b6bc4424a78ee969e033ab1da0606999a26088aae71c7ee` |
| `fast_training_v3.py`, producer recorded by original confirmation | `a41d7f91ab1a3dd51084eeca3a9903f72700bfaaa5b75cbad2ad01b012b53f1e` |
| `fast_training_v2.py`, producer recorded by training02/refinement01 | `29249ff756aaea90965352d6fb7feee7b5b52edfdf4815ab4e094460987feaec` |
| `fast_training_v1.py` | `753beb081da05f3f73394e423142bbff52fbe5ce3ac9e53273f33e87314353b0` |
| `reuse_check.py` | `3eb7e3e3bd07f1c5ae636dd30b180e4f5fe2403d6a06f9fd9ad3a66aaae6a3b2` |
| `analyze_training.py` | `96b8bdc73584838fdacac7894387a9dcea72c0a5ab53b16851b72583b50860ab` |

V1 to v2 adds retained hidden training activations. V2 to v3 adds large-width
operator checks, timing guards, and optional precision/protocol arguments.
V3 to current changes only the initial strict-check precision: IEEE matrix
multiplication is used during those checks, then the requested TF32 setting is
restored. No forward equation, physical velocity, initialization, Heun update,
or no-TF32 scientific trajectory changes in these diffs. The independent
cross-device reproductions below provide an additional direct check of that
last statement for the selected confirmation cases.

The later protocol addition explicitly permits verification repeats after the
scientific results. It does not change the five metrics or scientific
thresholds, and verification repeats are not new statistical replicates. The
review's original GPU-run configuration retains the original protocol hash.
The artifact hash manifest was written after the allowance was appended, so
its protocol entry records the later hash. Both identities are disclosed here.
The aggregation script is not included among the original run config's hashed
sources; its current formulas match the frozen protocol, but that config alone
does not independently certify the script's historical pre-execution freeze.

Full hashes for the read source/artifact set, independent analysis code, and
machine-readable results are under
`data/generated/response_memory_fast_mixing_20261002/training_review/`:
`confirmation_input_sha256.json`, `confirm_independent.py`,
`independent_confirmation.json`, `independent_scaling.json`,
`independent_refinement.json`, and `independent_gpu_reproduction.json`.

## Independent five-metric recomputation

There are exactly 20 confirmation runs: width 8192, five seeds 7501–7505, and
four matrix laws. Each saved prediction array has shape (21\times357), and
each hidden training activation array has shape (21\times64\times8192).
Every saved time grid is (0,2,\ldots,40), and inspected predictions and
activations are finite.

For each seed and time, the reviewer independently formed the two training
Grams (hh^\top/n) and (gg^\top/n) in float64. Each law was averaged over
its five seeds before taking RMS differences from the Gaussian ensemble mean.
No neuron-coordinate matching across different laws was used. This reproduces
the protocol's precise order of averaging and all five reported distances:

| RMS distance to Gaussian ensemble mean | Flat | Quarter-circle | Gaussian diagonal |
|---|---:|---:|---:|
| Predictions, all times/examples | 0.01779215 | **0.00194452** | 0.02060188 |
| First-layer training Gram | 0.00858803 | **0.00097648** | 0.01067156 |
| Second-layer training Gram | 0.01745681 | **0.00142600** | 0.02805459 |
| First-layer RMS-motion trajectory | 0.02148023 | **0.00028110** | 0.01334114 |
| Second-layer RMS-motion trajectory | 0.02489235 | **0.00097928** | 0.04947662 |

The independent implementation matches the submitted analysis to numerical
precision. Quarter-circle is closest on all five metrics, and its prediction
distance is below 0.01. All five quarter-circle runs exceed 0.03 first-layer
motion and improve held-out MSE over their own fixed features by 59.48–60.44%,
well above the required 5%. All other laws also meet that feature-learning
criterion in all five runs; useful feature learning is not unique to the
quarter-circle law.

Raw predictions and labels independently reproduce the submitted train/test
MSE, frozen test MSE, and classification-error summaries within float32
rounding. The motion trajectories use the saved scalar metrics over all 357
images; only training activations were retained, so the reviewer cannot
independently reconstruct the held-out component of those motion scalars from
the activation files alone. The already-reviewed producer computes that
component directly, and the selected complete reruns reproduce its results.
Raw parameter states were not saved, so this is an audit of finite saved
observables, not an independent full-state finiteness certificate.

## Initialization variability and statistical limits

The independent unit of initialization variability is a seed's entire set of
paired law trajectories, not each time, image, neuron, or Gram entry. Shared
first-layer initialization and the producer's common random draws across some
laws must be retained in resampling.

As a descriptive robustness check, the reviewer resampled five seed clusters
10,000 times, using fixed seed 91537. Each resample recomputed ensemble means
and all five RMS distances. Quarter-circle's distance remained below each
alternative in every resample. All five leave-one-seed-out comparisons also
retained all distance orderings and the 0.01 prediction threshold. The paired
bootstrap percentile margins are recorded in the machine-readable report.
These are exploratory uncertainty diagnostics for five seeds, not rigorous
population confidence guarantees or additional independent experiments.

For scale, empirical RMS standard errors of the ensemble prediction means are
0.00260 for Gaussian and 0.00246 for quarter-circle. Accounting for their
pairing, the RMS standard error of the mean prediction difference is 0.00235.
Their measured separation 0.00194 is therefore not evidence of a resolved
nonzero population difference;
nor does a small observed separation prove equality. The considerably larger
flat/Gaussian-diagonal separations support the comparative engineering gate.

Terminal held-out MSE means and sample standard deviations over five seeds are:

| Law | Mean MSE | Seed sample SD |
|---|---:|---:|
| Gaussian | 0.0601332 | 0.0004406 |
| Flat | 0.0609127 | 0.0003273 |
| Quarter-circle | 0.0604308 | 0.0004787 |
| Gaussian diagonal | 0.0587666 | 0.0003416 |

Every run has six errors among 293 held-out images. Zero variation of that
error count across seeds says nothing about uncertainty over new datasets.
Gaussian diagonal has the lowest empirical mean MSE here despite being a worse
match to the Gaussian learner's trajectories. The gate measures fidelity to
a reference learner, not superior task performance. The task and split were
shared with the pilot, so confirmation is over fresh initialization only.

## Independent GPU0 reproduction and numerical checks

The reviewer executed the unchanged current producer on physical GPU0, exposed
as `cuda:0` by `CUDA_VISIBLE_DEVICES=0`, using the original width 8192, seed
7501, (dt=0.02), horizon 40, and no TF32. Gaussian and quarter-circle outputs
were written to the fresh `reuse_training_review/` directory. Both devices are
reported as NVIDIA GeForce RTX 3090; the original source and reproduced source
versions are accounted for above.

Both cases match the original confirmation **bit for bit** in every saved
prediction, both hidden training activation arrays, fixed-feature predictions,
initial Gram, and time grid. Saved data, labels, and exact split indices also
match bit for bit. All maximum absolute and RMS discrepancies are zero, so no
cross-device tolerance relaxation was needed.

Both eager/captured one-step errors are zero. The width-8192 Hadamard-involution
relative error is (1.48\times10^{-7}); the normalized adjoint errors are
(8.50\times10^{-9}) for Gaussian and (3.06\times10^{-10}) for quarter-circle.
The independently launched run completes both trajectories in 10.14 recorded
seconds, within a process-level 580-second timeout and the assignment's
10-minute/four-run ceiling. Exactly two GPU fits were run; GPU0 was released
after completion. Their warmed training times were 5.80 s and 1.52 s. These
two reviewer timings are reproduction metadata, not a replacement for the
three-seed width-16384 performance experiment.

The older width-2048 half-step artifacts were also compared independently with
their (dt=0.02) counterparts. Maximum-over-time prediction RMS changes are
(1.11\times10^{-5}) for Gaussian and (1.14\times10^{-5}) for quarter-circle,
below 0.002. This checks that earlier setting; it is not a half-step test at
every larger width. No extra setting or seed search was performed by the
reviewer.

## Scaling numbers and their practical scope

The six width-16384 TF32 records contain exactly the prescribed two laws and
three seeds 7511–7513. The reviewer independently recomputed:

| Quantity | Gaussian | Quarter-circle | Gaussian / quarter-circle |
|---|---:|---:|---:|
| Median warmed training time | 12.66486 s | 2.42734 s | **5.21758** |
| Median peak allocated CUDA bytes | 1,316,446,208 | 243,687,424 | **5.40219** |
| Moving model scalars | 3,162,113 | 3,162,113 | 1 |
| Stored mixer entries | 268,435,456 | 147,456 | — |

Both time and memory ratios exceed 2. Both laws pass the stated feature-learning
criterion in all three runs. Setup times are separately recorded: approximately
3.82–4.88 s for Gaussian and 0.061–0.062 s for quarter-circle. Stored-entry counts
mix float and integer entries and count the mathematical mixer, not every
live array; the allocator peak is the relevant measured CUDA-memory result.

The timed training region includes scheduled full-data evaluation and host
transfers of predictions/features. It excludes setup and final NumPy archive
serialization/disk writing. Results should preserve this timing boundary and
hardware/settings, rather than advertise an unrestricted end-to-end application
speedup. Runtime ordering and only three seeds also limit performance
uncertainty claims. The independent review of these records verifies the
reported ratios; the supervising task's separate width-16384 precision and
replay checks are still needed to close the full numerical scaling gate.

A materially cheaper baseline already suffices for this small task: the
width-2048 dense Gaussian pilot has median warmed time 0.78389 s, peak
63,059,968 bytes, and six held-out errors in each of three runs. Its held-out
MSEs are 0.05961–0.06144. It is cheaper than width-16384 quarter-circle while
achieving the same observed classification error. Same-width gains therefore
do not show the fastest useful solution to the data problem.

## Supported claim and remaining boundary

The evidence supports a fast prescribed-spectrum implementation that, for this
q=1 response-memory learner and fixed digits-3/8 experiment, closely matches
five selected Gaussian-reference ensemble summaries and reduces measured
same-width computational cost on the tested hardware. It also supports useful
feature movement relative to the specified fixed-feature readout baseline.

It does not establish a distributional limit, equivalence under arbitrary
adaptive reuse, transfer to other datasets/depths/closure orders, better
predictive risk, or priority for structured transforms. Direct trained
low-rank/dynamical-low-rank and other strong fast-architecture controls remain
absent from this experiment. The stated protocol makes no novelty claim for
the transform itself. No external theorem's applicability or literature
priority was independently verified in this scoped empirical review. These
limits must remain attached to any summary of the PASS.
