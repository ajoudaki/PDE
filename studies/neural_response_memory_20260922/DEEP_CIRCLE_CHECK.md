# Internal independent check of the three-hidden-layer circle construction

Checker: scoped agent `/root/deep_audit`, 2026-09-24–25. This is an internal
implementation/theory check, not an isolated promotion review. No training
campaign is run by this checker. Final verdict: **PASS with one documented
checkpoint recovery** for the finite algebra, implementation, deterministic
checks, empirical scores/gates, complete saved-state replay and opposite-GPU
reproduction checks. The original corrupt archive and failed replay remain
preserved; no training trajectory or reported score was changed.

## Scope and complete read coverage

Read in full: `DEEP_CIRCLE_DERIVATION.md`, `deep_moment_engine.py`,
`deep_circle_run.py`, `test_deep_moment_engine.py`, `DEEP_CIRCLE_PROTOCOL.md`,
the authorized dependency `moment_engine.py`, `docs/NOTATION.md` and
`code/pde/finite_network.py`, and the later-authorized `deep_circle_cases.json`.
The entire runner was reread after the supervisor identified additions to its
repository, thread and lifecycle metadata. Process inputs were the supplied root instructions,
`RESEARCH_WORKFLOW.md`, the investigate-conjectures skill with adversarial-audit
and decisive-experiments references, and solve-math-rigorously. No other study,
old experiment result, external scientific source or prior review was read.
The supervisor supplied authorization for the dependency after its import was
identified. No Git mutation was performed.
The later authorized scope included all 40 primary and two reproduction run
outputs, the current experiment's analyzer JSON, and the narrow recovery
artifacts described below. No other study or previous campaign was inspected.

The construction has three bias-free tanh hidden layers and two trained
internal matrices. The exact finite model uses unhalved mean squared loss,
readout normalization `1/n`, mobilities `(n,1,1,n)`, and independently drawn
stored readout standard deviation `1/n`. The experiment's circle rows already
represent `x/sqrt(2)` and receive no further input scaling. Both moment links
use the same activity clock `s'=sqrt(mean(r^2))` and their own forward/backward
history arrays. Dense and moment engines share the exact NumPy draw order.

## Algebra and implementation verdict

The gradient factors, derivative ordering, triangular Legendre transport,
sample averaging, virtual-prefix initialization and reconstruction are
consistent. The derivative of each reconstructed matrix equals the dense
physical vector field evaluated at the reconstructed network plus the stated
positive-sign covariance defect. Both forward and reverse actions use actual
transposes of the same current matrices/factors. The initial two defects vanish,
and an exactly zero residual is absorbing even at noninitial history states.

The continuous response lift and its invariants are derived correctly. The
production implementation evaluates fresh tanh responses and residual RMS;
it implements the nonlifted closure and does **not** numerically implement a
rational lifted RHS. The derivation and protocol distinguish these claims.
There is no dense-trajectory forcing or separately trained reverse operator.

The controller compares Euler/Heun differences using the same hidden-matrix
Frobenius/sqrt(n) convention for dense and reconstructed states. It separately
controls all four moment arrays and the activity coordinate. This is a local
numerical heuristic, not a bound on output error or a width-uniform stability
theorem. Full-run refinement is necessary to resolve closure discrepancies.
Loss crossings use actual training MSE along the Heun continuous extension.
Only bracketed crossings are located; the recorded label does not certify an
unobserved earlier crossing inside an accepted step with nonmonotone loss.

The Frobenius factor norm uses Gram contractions with a roundoff zero clamp.
The matrix-difference factorization avoids subtracting two large reconstructed
matrices. Severe cancellation in a Gram norm remains a floating-point
limitation; the deterministic states checked here showed no material error.
The construction compresses learned moving state, while retaining both dense
initial matrices and their forward/transpose multiplication cost.

## Executed deterministic evidence

Author suite command:

```text
/home/amir/miniconda3/bin/python -m unittest discover -s studies/neural_response_memory_20260922 -p test_deep_moment_engine.py -v
```

Outcome: **9 tests passed** in 0.546 seconds and again in 0.607 seconds after
the runner metadata additions. This covers independent Torch
autograd, exact initial tangents, both adjoints/defects, physical controller,
zero-loss boundary, physical crossing/checkpoint replay, exact horizon cap,
and identical trajectories when the query-panel size changes.

Independent checker command:

```text
PYTHONDONTWRITEBYTECODE=1 /home/amir/miniconda3/bin/python studies/neural_response_memory_20260922/check_deep_circle.py --out data/generated/neural_response_memory_20260922/deep_circle_audit01/algebra03
```

Evidence: `data/generated/neural_response_memory_20260922/deep_circle_audit01/algebra03/check.json`.
This contains complete source SHA256 hashes, software versions, exact command,
and component errors. Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130,
float64, CPU, one Torch thread. The maintained NumPy oracle was loaded directly
from `code/pde/finite_network.py`; its raw input was `sqrt(d)*U.T`, matching
the experiment's already scaled rows.

Cases `(n,d,M)=(1,1,1),(11,3,5),(17,2,3)` were checked at every P=1,2,3.
States included independent noninitial perturbations. Checks used literal
indexwise reconstruction and product-rule derivatives, rather than the
engine's factor flattening. Repeating the complete sample set three times
preserved both dense and moment vector fields. The moving-history transport
was separately checked against 16-node Gaussian quadrature for a cubic
history on a changing interval.

| Check | Largest observed absolute difference |
|---|---:|
| Dense physical velocity versus maintained NumPy | 4.44e-16 |
| Reconstructed matrix product-rule derivative | 2.78e-17 |
| Physical derivative minus dense field versus exact defect | 8.33e-17 |
| Controller ratio versus explicitly reconstructed matrices | 1.32e-11 |
| Moment transport versus quadrature finite difference | 2.31e-10 |
| Four-sample oddness quotient versus eight antipodal samples | 1.11e-16 |

The quotient check uses the actual equal_mixed_odd labels and directions from
the frozen case file. For a bias-free odd activation, hidden responses and
residuals change sign on an antipodal sample, while all backpropagated deltas
remain unchanged. Both history factors therefore change sign, preserving
their product. At P=1,2,3, initial and noninitial states were checked for
identical loss, clock, first/readout velocities, reconstructed internal
matrices, their physical derivatives, and sign-correct A/B sources. The dense
physical velocities were checked separately. This validates the eight-to-four
quotient for this deeper architecture.

The first checker attempt, retained under `algebra01`, failed because this
checker's quadrature scalar tensors defaulted to float32. Making those scalar
inputs float64 resolved the discrepancy. No production-code change resulted.

Four additional tiny CPU smoke runs (width 5, two samples, dense and P3, two
resolutions, 16 query points) test the audit pipeline itself. All 16 saved
observation panels, physical loss crossings and checkpoint hashes replayed
successfully, and independent scores were produced. Their retained paths are
`deep_circle_audit01/smoke01` and `deep_circle_audit01/smoke_check01/check.json`.
These are deterministic software checks, not width 4096 scientific evidence.

On 2026-09-25, replay-reader provenance checks were strengthened to compare
manifest/summary contents, current frozen source hashes, literal task inputs,
physical final times and observation labels/counts. A fresh CPU smoke replay
of eight observations/four checkpoints passed with maximum panel difference
4.17e-17 (`replay_reader_smoke02/check.json`). The new reproduction comparator
checks bytes of every scientific array and every checkpoint field, excluding
only `integration_wall_times`. A separate negative check confirmed that a
wall-clock-only change is ignored and a one-bit first-weight change is found
(`reproduction_comparator_negative01/comparator_check.json`). The latter
directory is an intentionally altered test fixture, not a scientific run.

## Saved-run and empirical checks

Independent CPU scoring of all 40 completed primary trajectories passed.
All 75 milestone comparisons, 15 final endpoint comparisons and 75 pairwise
order comparisons match `deep_circle_analysis01/metrics_summary.json`; the
largest metric discrepancy is 1.09e-19. Every individual absolute/relative
refinement, nested-grid and physical-loss gate was checked and matched.
All 75 numerical gates pass. No conditional resolution is required by the
frozen protocol. All 40 array hashes, effective configuration hashes,
manifest/summary agreement and frozen production-source hashes were checked;
every primary run reached MSE .001 and shares one exact initialization hash.

Evidence is `deep_circle_audit01/score_final01/check.json`,
`deep_circle_audit01/analyzer_comparison01/check.json`, and
`deep_circle_audit01/metadata_final01/check.json`. The score command's complete
40-run argument list is retained in `score_final01_command.json`.

| Circle task | P1 RMS | P2 RMS | P3 RMS |
|---|---:|---:|---:|
| two_outliers_alternating | .108086211 | .023797219 | .031476459 |
| quadrant_alternating | .274642803 | .028358443 | .058491243 |
| quadrant_pairs | .012185557 | .003708120 | .001214942 |
| quadrant_center_edges | .078973166 | .025701932 | .007246026 |
| equal_mixed_odd | .014984607 | .002412359 | .000281860 |

These are full-circle RMS discrepancies against the fine dense reference at
each model's own MSE .001 crossing. P3 improves on P1 for all five tasks;
P2 improves on P3 on both alternating tasks. P1 exceeds the coarse .1
agreement threshold on both alternating tasks. This finite result does not
establish monotone hierarchy convergence.

The two fresh repetitions have completed on opposite GPUs. The dense original
on cuda:0 versus repetition on cuda:1 matched all 48 scientific array fields
across six NPZ files bit for bit. The P3 original on cuda:1 versus repetition
on cuda:0 matched all 66 fields across six files bit for bit. These comparisons
include the complete saved final state, trajectories, predictions and all five
checkpoint states. Only `integration_wall_times` was excluded. The maximum
numeric difference is zero for both pairs. Evidence:
`deep_circle_audit01/reproduction_check01/check.json`.

The scoped checker's first escalated GPU launch did not execute: the tool
returned no session or process IDs and was interrupted while awaiting a result.
No replay outputs existed. The supervisor verified host GPUs were idle and
launched the exact retained `replay_launch.json` commands/environment instead.
This is an execution handoff, not a failed scientific run. The checker authored
the independent replay code; the supervisor owns its host launch/wait. The
complete GPU replay passed after the narrow checkpoint recovery below.

The all-archive CRC screen covered all 252 NPZ files from the 40 primary and two
reproduction runs. Exactly one member failed: `W3.npy` in the coarse dense
quadrant-pairs `checkpoint_loss_0p001.npz`. Its whole-file SHA256 still matched
the hash recorded by the producer, so the inconsistent bytes were already
present when that hash was recorded. The cause of the single-bit alteration
is not established. All other 251 archives pass CRC, including this run's
complete final state in `arrays.npz`.

The corrupted checkpoint differs from its redundant valid final state in
exactly one bit of one float64 word, at flattened W3 index 14205696. Its other
five fields, including physical time and training loss, are byte-identical to
the final state. Restoring the differing bit from that final state reproduces
the checkpoint's original recorded CRC exactly (`0x47745a98`). The preserved
raw checkpoint word is `0xbf8dbf86b3a6a13b`; the redundant valid final word is
`0xbf8dbf86f3a6a13b` (absolute difference 1.862645149e-9).

The supervisor authorized a narrow reproducible recovery, implemented in
`repair_deep_circle_checkpoint.py`. It verifies both original hashes, the exact
one-bit discrepancy, all intact fields, and the restored original CRC; copies
the archive into `deep_circle_recovery01`; and changes only that bit in the
copy. The recovered checkpoint now passes CRC and every field matches the
valid final state byte for byte. Original files and all scientific metrics are
preserved. A replay view symlinks unchanged files and copies the summary with
only the recovered checkpoint hash updated. This requires no training rerun.

Recovery evidence: `corruption_diagnostic01/check.json`, `raw_comparison.json`,
`one_bit_crc.json`, and `all_archive_integrity01/check.json` under the audit
directory; `deep_circle_recovery01/repair_manifest.json` records exact hashes,
the changed file-byte offset 247929386, values and replay-view mapping. The
recovered archive SHA256 is
`8bfd906ab07c56aef7e1553bb6d7b8e9c97c292027503f6b49913c11bc2320df`.
The original failed GPU0 log and its eight completed-run records remain in
`replay_gpu0.log` and `replay_gpu0/check.json`. GPU1 independently completed
21 runs, 147 observations and 105 checkpoints. The remaining 13 GPU0 runs passed
in `replay_gpu0_recovered/check.json`, using the explicitly mapped recovery
view for the affected run. The supervisor separately verified the whole-file
byte difference and summary change in `deep_circle_recovery01/supervisor_verification.json`.

## Complete replay, feature movement and evidence versions

Consolidating the eight successful records retained in the original failed
GPU0 report, the 21 GPU1 records and the 13 recovery-replay records gives
exactly **42 unique completed runs, 294 observation panels and 210 checkpoint
states**. The original-to-recovery path mapping is explicit; there are no
duplicates or omissions. Each panel contains all 8192 circle directions.
The maximum circle prediction rebuild difference is **3.387290448e-13**;
the maximum training prediction rebuild difference is **5.653255641e-13**.
The checker reconstructs both physical dense matrices independently of the
engine's factor-action forward routine, then validates all saved predictions,
physical losses, times, initialization and artifact hashes.

Final evidence: `deep_circle_audit01/final_consolidation01/check.json` contains
the complete run inventory, source/evidence hashes and the recovery mapping.
The supervisor's separate consolidation, retained as
`deep_circle_audit01/supervisor_final_verification.json`, agrees on counts,
maximum prediction discrepancy and feature-motion ranges. Exact worker
commands, environment and exit statuses are retained in `replay_launch.json`,
`replay_execution.json` and the `replay_recovery_*.json` receipts. The original
GPU0 process status remains FAIL; the aggregate verdict uses only its eight
completed per-run checks together with the subsequent successful replay.

For each hidden layer, feature motion is
`sqrt(mean((h_final-h_initial)**2))` over neurons and training samples.
Restricting to the **20 finest primary trajectories**, one dense/P1/P2/P3
trajectory per task at rtol `3.125e-6`, excluding repetitions, gives:

| Quantity | Minimum | Maximum |
|---|---:|---:|
| First hidden activation RMS movement | .345440853 | .648572494 |
| Second hidden activation RMS movement | .382720099 | .736775144 |
| Third hidden activation RMS movement | .460716998 | .677562886 |
| First-weight entry RMS movement | .766006584 | 3.409935744 |
| Stored readout RMS movement | 2.115184732 | 5.184949810 |

The full per-task, per-model table is
`deep_circle_audit01/final_consolidation01/finest_primary_motion.csv`, with the
same values embedded in the JSON. These are substantial measured finite-width
feature changes; they establish neither an asymptotic nonlazy limit nor a
theorem about feature movement at arbitrary width or time.

Selected source SHA256 values (all other input hashes are in the check JSON):

| Source | SHA256 |
|---|---|
| DEEP_CIRCLE_DERIVATION.md | `17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9` |
| deep_moment_engine.py | `97aa9bc3ac99a982ec81ab8abac3e240aca2e05aecb37e1d6a24b3e7f4ba9f23` |
| deep_circle_run.py | `714a08211750662365f57e5a0c5c45e6f461ac0a9ca1fb1307470f15487fcddc` |
| check_deep_circle.py | `d534ef615a93a66dffc21e1721ccf4bf0a1da1442faa49fb6ed611886a48c86b` |
| repair_deep_circle_checkpoint.py | `1f0ab42534c58f40a9feb2601c34b4324fe62e2cb57550f26b121386c07adaec` |

Selected evidence SHA256 values:

| Evidence | SHA256 |
|---|---|
| final_consolidation01/check.json | `989ca061b83dfa417104aa248f609b5caa4357278d12520e42d342b666318f00` |
| analyzer_comparison01/check.json | `669d4112c42c49b7f3ede05f88dd0dfdce3be4f361ee680d2d72fd5ef821a6cd` |
| reproduction_check01/check.json | `efa3322ab5dd0dc4c556ce1ca2498c4dbd4820342537fb84064b1dd956e9a170` |
| all_archive_integrity01/check.json | `48e4f05a3cdd1549816f0192feb7b55ade82d85688ca91296792a9f239a2f87e` |
| deep_circle_recovery01/repair_manifest.json | `c51e62f474aa1698b8a5a338d9198c550412ddefd6ce46d28492c4a5ea094001` |

Hierarchy convergence, all-time validity, a population limit and
width-independent complexity remain unsupported by this check. Saved state
replay verifies inference and reported metrics; the independent fine/repeated
trajectories supply the empirical reproduction evidence.

This internal validation is complete with the one documented archive recovery.
All requested algebra, numerical scoring, saved-state replay, reproduction and
finite-width feature-motion checks are recorded; no additional run is pending.
