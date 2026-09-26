# Matched derivative-p3 benchmark inputs

Scoped empirical input audit, 2026-09-22. The identified task is
`two_outliers_alternating` at width 2048. Its final archived derivative-p7
finer circle RMS is **0.7564240400073452**, matching the user's approximate
recollection of 0.78. The frozen derivative-p3 finer RMS is
**1.1001187613717835**. Both compare each model's own fitted endpoint with
the same dense model's own fitted endpoint.

## Authority and scope

The supervisor's explicit assignment narrowly authorized reading the benchmark's
definitions, results, settings, producer dependencies, and raw outputs in
`studies/gradient_flow_probe_dictionary_20260921`, its generated namespace,
and its designated original-circle archive,
`studies/random_dictionary_learned_circle_20260920` and the matching generated
namespace. This is a matched-test exception for those empirical inputs, not
permission to import unrelated research or theories from other studies.

The supervisor subsequently transmitted the user's clarification: initialize
with the **exact derivative-p3 vectors**, then unfreeze/train them, retaining
the old model otherwise. That clarification supersedes a streaming/cache
interpretation of this test. This audit identifies the frozen control and exact
initial values; it does not prescribe the new factor mobilities.

I applied the required `investigate-conjectures` skill to maintain evidence and
claim boundaries. I performed read-only source/archive inspection, file hashing,
array equality checks, and arithmetic on saved endpoint predictions. No training,
GPU use, Git action, benchmark modification, or new trajectory occurred. The
only written artifact is this report. This is not a new independent full-state
replay of the historical trajectories.

## Exact task, model, and initialization

- Case: `two_outliers_alternating`.
- Eight angles in degrees: `[15, 27, 39, 51, 63, 75, 165, 285]`.
- Labels in that order: `[1, -1, 1, -1, 1, -1, 1, -1]`.
- Normalized API inputs: `u(theta) = (cos(theta), sin(theta))`; physical circle
  radius is `sqrt(2)` under the maintained input convention.
- Two hidden widths: `n1 = n2 = 2048`; input dimension 2; tanh; no biases.
- Network seed: `20260920`. Archive random-control dictionary seed is `7319`,
  but derivative-p3 itself is deterministic from the archived network and the
  two fixed axis probes, with no additional random dictionary draw.
- Mean **unhalved** training MSE; all three original blocks train together.
  Dense physical block mobilities are `(n, 1, n)`. The frozen compressed model
  uses the maintained canonical coefficient dynamics, as specified in its
  original protocol and `ClosureEngine`.
- The actual finite random initial readout is preserved.
- The whole compressed middle action is `b2 @ M @ b1.T / n`, with no dense
  background. For a normalized input column `u`,
  `h1=tanh(w@u)`, `z2=b2@M@(b1.T@h1/n)`, and `f=c@tanh(z2)/n`.

Derivative-p3 has `b1.shape=(2048,6)`, `b2.shape=(2048,12)`, and
`M.shape=(12,6)`: 18 dictionary vectors, 72 trained middle coefficients, and
`3*n+72 = 6216` originally trained scalars. Unfreezing both factor tables adds
`n*(6+12)=36864` trained scalars, for 43080 total under the same representation.
Derivative-p7 has dimensions `(26,46)`: 72 vectors, 1196 middle coefficients,
7340 originally trained scalars. These order labels refer to the derivative
dictionary and must not be confused with the older action-word p3/p7.

The p3 raw generator column orders are lower
`h1,h2,L11,L12,L21,L22`, and upper
`U11,U12,U21,U22,C1,...,C8`. Stored `b1,b2` are the actual **ridge-normalized**
tables used by training, not the raw generator tables. The ridge is
`eta=1/(1024*4^2)=6.103515625e-5`; normalization is the raw Gram plus `eta*I`
followed by the inverse Cholesky transpose. No raw-column rescaling or rank
deletion was used. The exact definition is in the complete `new_dictionary.py`.

For an exact matched initialization, load `b1,b2,w[0],c[0],M[0]` directly from
the finer frozen-p3 `arrays.npz` below. The archive's constant `D` equals
`M[0]` bit for bit. `w[0],c[0],M[0],b1,b2,D` agree bit for bit between the
primary and finer p3 runs. The p3 `w[0],c[0]` also agree bit for bit with both
selected dense initial checkpoints. The dense initial middle array is
2048-by-2048 and is **not** the compressed 12-by-6 core.

The historical suite builder actually read the initial full state from
`data/generated/random_dictionary_learned_circle_20260920/diverse_refined01/quadrant_grouped_full/arrays.npz`.
Its config hashes for all three initial arrays agree with the selected outlier
dense archive's first arrays, which I checked directly. Therefore the outlier
raw checkpoint suffices to identify the same shared initialization without
regenerating a random draw.

## Authoritative raw files

All paths below are relative to `/home/amir/Codes/PDE`. Each listed trajectory
directory contains both `arrays.npz` and `summary.json`.

| Model | Level | Trajectory directory | Worker configuration in its parent directory |
|---|---|---|---|
| Dense | Primary | `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_primary01/two_outliers_alternating_full` | `config_A_worker1.json` |
| Dense | Finer | `data/generated/random_dictionary_learned_circle_20260920/scaling_discovery_refined01/two_outliers_alternating_full` | `config_A_worker1.json` |
| Frozen derivative p3 | Primary | `data/generated/gradient_flow_probe_dictionary_20260921/suite_primary01/two_outliers_alternating_new_p3` | `config_worker0.json` |
| Frozen derivative p3 | Finer | `data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/two_outliers_alternating_new_p3` | `config_worker0.json` |
| Frozen derivative p7 | Primary | `data/generated/gradient_flow_probe_dictionary_20260921/p7_primary01/two_outliers_alternating_new_p7` | `config_worker0.json` |
| Frozen derivative p7 | Finer | `data/generated/gradient_flow_probe_dictionary_20260921/p7_refined01/two_outliers_alternating_new_p7` | `config_worker0.json` |

The raw arrays contain `endpoint_prediction`, `endpoint_angles`,
`endpoint_inputs`, `training_inputs`, `labels`, all accepted `times/losses`,
`accepted_steps`, `local_error_ratios`, and saved state/prediction snapshots.
State arrays `w,c,M` have a leading snapshot axis. Use their last snapshot for
the endpoint and their first for initialization. `b1,b2,D,g,p1,p2` are constant
tables in the frozen compressed archives. There is no epoch variable: these
are full-batch gradient-flow times and adaptive accepted integration steps.

Final joined metrics and historical validation are
`data/generated/gradient_flow_probe_dictionary_20260921/p7_analysis_final01/{metrics,validation}.json`.
The common dense pair is fixed in
`studies/gradient_flow_probe_dictionary_20260921/SUITE_MANIFEST.json`, cell
`two_outliers_alternating_full`. The later `scaling_discovery` dense pair
supersedes the original `diverse_analysis01` dense pair for this task; do not
mix old-reference scores with this selected reference.

## Endpoints and numerical settings

Every listed trajectory fitted. Primary/finer tolerances are respectively
`rtol=6.25e-5/1.5625e-5`, `atol=6.25e-7/1.5625e-7`. They used float64 CUDA,
deterministic algorithms, disabled TF32, simultaneous adaptive Heun with
embedded Euler error estimation, initial step `.05`, maximum step `2`,
minimum permitted step `1e-7`, maximum flow time `10000`, maximum accepted
steps `30000`, and a per-trajectory integration wall limit of 180 seconds.
The producer also enforces each invocation's separately recorded worker budget.

The recorded interpreter is `/home/amir/miniconda3/bin/python -B`
(`SUITE_RUN_RECORD.md`, execution-environment paragraph). The saved versions
are Python 3.10.14, PyTorch `2.9.0+cu130`, and NumPy 1.26.4. The recorded
environment sets `PYTHONPATH=code`, `PYTHONDONTWRITEBYTECODE=1`,
`OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`, and
`CUBLAS_WORKSPACE_CONFIG=:4096:8`.

The controller uses RMS-scaled read-in/readout errors and a Frobenius-scaled
middle error relative to the trained middle increment, with the increment
norm clamped below by 1. Candidate steps must satisfy the error ratio gate and
the declared loss-decrease gate. Endpoint localization uses 30 bisections on
the parameter chord of the first accepted Heun step crossing training
MSE `0.001`. This is a numerical first crossing, not an exact-flow certificate.

| Model | Level | Fitted flow time | Training MSE | Accepted steps | Circle RMS vs dense |
|---|---|---:|---:|---:|---:|
| Dense | Primary | 156.95793150508746 | 0.0009999999999991429 | 1042 | 0 |
| Dense | Finer | 156.95289234260915 | 0.000999999999993258 | 1562 | 0 |
| Frozen p3 | Primary | 241.9962045396258 | 0.0009999999999977696 | 2767 | 1.1001879441182023 |
| Frozen p3 | Finer | 241.98527414956894 | 0.0009999999999967945 | 3339 | 1.1001187613717835 |
| Frozen p7 | Primary | 220.67409615224955 | 0.0009999999999986907 | 2125 | 0.7563259845808216 |
| Frozen p7 | Finer | 220.6768397610208 | 0.0009999999999964731 | 2693 | 0.7564240400073452 |

Saved dense snapshots are `0,1,2,5,10,20,40,80` and the final time. P3/p7
also save time `160` before their final time. All six raw loss histories have
every preterminal accepted loss above `.001` and terminal loss at or below
`.001`. No common-time endpoint or fixed epoch count is implied.

## Metric and validity checks

For each numerical level, let `theta_j=2*pi*j/8192`, `j=0,...,8191`.
The primary metric is

`RMS = sqrt(mean_j((f_model(theta_j,t_model_fit)-f_dense(theta_j,t_dense_fit))^2))`.

Each model is evaluated at its own first detected training-MSE crossing;
the dense reference is evaluated at its own crossing. This measures agreement
with the dense learned circle function, not error against a prescribed
ground-truth circle function. Secondary metrics are mean absolute discrepancy
and sampled maximum discrepancy. The nested 4096-node check uses every second
8192-grid point. Sampled maxima are not continuous-circle supremum bounds.

Fresh arithmetic on the saved endpoint predictions reproduces the four p3/p7
reported RMS scores to at most `2.23e-16`; all four prediction grids agree
exactly with their corresponding dense grid. Finer p3 L1/max are
`0.876216415873295 / 1.995010855421451`; finer p7 L1/max are
`0.6118483764578104 / 1.192137418509588`. RMS 8192/4096 differences are at most
`2.23e-16` in this fresh arithmetic.

The own-endpoint primary/finer sampled maximum differences, checked directly,
are dense `0.0009031267389815597`, p3 `0.0026477805767691764`, and p7
`0.0016901961867840098`. All pass the original `.01` gate. The original
validation also marks all three selected pairs valid, with no extra branch.
Historical source/config/replay validation is inherited from that archive;
this input audit only freshly checks the identities, raw endpoint arithmetic,
and first-crossing history properties described above.

## Fresh SHA-256 identities

Hashes below were recomputed from the files, not merely transcribed from
the historical analyzer.

| File | SHA-256 |
|---|---|
| Dense primary `arrays.npz` | `5dc1b931e5c26b8b6c500a029e6332237ec0bc09382f0e0a87341198882bdb32` |
| Dense finer `arrays.npz` | `70d4c76f6817b7e0e2c24be3dad9b8883054d1ebdf031d66efdb2677106c5357` |
| P3 primary `arrays.npz` | `424ad881e323c9bbe4b0117ca6aca92250698813b5e218be6a706240cdc07eeb` |
| P3 finer `arrays.npz` | `300b6ef7b3a60de6920f65d3ba1cddee5f447fa910f61bfa2c6fde712bf8905a` |
| P7 primary `arrays.npz` | `ce4977b4575f925607f30c0b5a06783f220546b240fb04419963721a6b06862a` |
| P7 finer `arrays.npz` | `6798ff05de475f8880fa90a6caa71a65d5420bbddf15ea794cc48a152d782d5b` |

Exact p3 initialized array hashes, using contiguous float64 array bytes:

| Array | SHA-256 |
|---|---|
| `w[0]` | `da24d2b86aed45dfa6e7442e24bfcb968ec28fcfbcfb2f5f07ac066601fffd63` |
| `c[0]` | `460ee22d13695cbe3226805bf5b24b124100e32be5717737508c79d8679b0db6` |
| `M[0] = D` | `180b5c47b29548554dd966d0a82d1729856c2548266b5992b0f9d4012f8a7b2b` |
| `b1` | `07ae8e86299f61231b3bca59037821ed7e650367ff66619067f891841728df83` |
| `b2` | `e4ac8d345dd11dddd70a58214f3dc3abbe8a7bc9098492fed83c777499bd08f5` |

The shared dense initial middle-array hash is
`559c9ad62fd9feab4fb4671e854b86ec975240a12aa8792873824ebe2344b3f9`.

## Consumed source chain

Empirical protocol/results/selection sources in the derivative study:
`SUITE_PROTOCOL.md`, `SUITE_REPORTING_AMENDMENT.md`,
`SUITE_ARCHIVE_INVENTORY.md`, `P7_PROTOCOL.md`, `P7_RESULTS.md`,
`P7_RUN_RECORD.md`, and the selected task/config records in
`SUITE_MANIFEST.json` and `p7_analysis_final01/{metrics,validation}.json`.
The interpreter was checked in the execution-environment paragraph of
`SUITE_RUN_RECORD.md`; original-circle README command lines confirm that path.

Complete relevant producer/helper sources read in that study:
`p7_run.py`, `suite_run.py`, `comparison_run.py`, `new_dictionary.py`,
`p7_analyze.py`, and `p7_merge.py`. In the original-circle archive:
`benchmark.py`, `diverse_benchmark.py`, and `scaling_benchmark.py`.
The six raw trajectory summaries, worker configurations, required NPZ members,
and the finer p3 `two_outliers_alternating_new_p3_dictionary.json` were also
inspected. No source from an unrelated study was used.

The inherited maintained engine imports are
`code/pde/finite_torch.py` (`NetworkEngine`) and
`code/pde/observable_torch_p1.py` (`ClosureEngine`, `TensorState`). This audit
traces those import dependencies but does not claim a fresh full maintained
engine review or a fresh p7 symbolic derivation. Those are unnecessary for
identifying and reusing the exact archived p3 factors and the matched endpoint
comparison.
