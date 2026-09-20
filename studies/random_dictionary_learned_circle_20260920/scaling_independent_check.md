# Independent scaling output check

Internal empirical audit, 2026-09-20. This is not an independent integration,
promotion review, asymptotic result, or assessment of other studies.

**All final discovery and confirmation outputs pass this empirical audit.**
The complete discovery audit verifies 42 closure cells, and each of the two
fresh confirmation groups verifies 27. All 192 model/reference metric records
across their two selected numerical levels agree exactly with the reported
float64 errors; the required tolerance was 1e-11. Every selected model and
reference is fitted and its own endpoint refinement discrepancy is at most
0.01 after the permitted numerical-resolution runs.

The paired-family improvement observed in discovery and confirmation group 1
does not satisfy the frozen discriminator in confirmation group 2. The outlier
family also fails the required ratio improvement. Therefore neither eligible
positive family qualifies for the width branch. No width experiment is
triggered. A one-bit archive repair and an isolated failed audit process are
documented below; the repaired inputs subsequently pass replay and integrity
checks.

## Scope and independence

The supervisor assigned this checker a fresh scoped context. Scientific reading
was restricted to `SCALING_PROTOCOL.md`, `scaling_cases.py`, the explicitly
subsequently permitted `diverse_cases.py`, and this study's raw `scaling_*` and
`diverse_*` output schemas. Relevant raw dictionary validation metadata was
inspected. The supervisor explicitly permitted the historical
`diverse_analysis01/selected_levels.json` selection record and supplied the
neutral saved-state maps below. The scaling `metrics.json`, `summary.json` and
ratio/target CSV files were read as claimed outputs to compare, not as
implementation inputs. The summary extension takes its numerical inputs from
the prior independent raw-output audit, including independently measured
dictionary dimensions. For C2 archive verification, the supervisor additionally
provided `scaling_archive_repair01/repair.json`, its preserved original, repaired
target and the five named same-initialization donor archives. The repair source
was not read; the repair was independently checked at the byte/member level.

No analyzer, benchmark, dictionary producer, prior review report, other study,
or other task history was read or imported. Producer/analysis/report files
referenced by raw source manifests were hashed as bytes without interpreting
their contents. Only `scaling_cases.py` and its `diverse_cases.py` dependency
are imported from the study. Process reading comprised root `AGENTS.md`, Part 1
of `RESEARCH_WORKFLOW.md`, the investigate-conjectures skill and its
decisive-experiments/adversarial-audit references.

For saved unit directions `u`, the independent replay implements

```
full:    h = tanh(w @ u.T); H = tanh(M @ h); f = c @ H / n
closure: h = tanh(w @ u.T); a = b1.T @ h / n
         H = tanh(b2 @ (M @ a)); f = c @ H / n
```

Each snapshot uses its saved `w`, `c`, and `M`. For a difference vector on the
8192-point circle grid, L1 is mean absolute difference, MSE is mean squared
difference, RMS is its square root, and maximum error is maximum absolute
difference. The nested grid takes every second point. Contractions, predictions,
spectra, norms, and nested-grid metric differences execute on CUDA float64.
Only one model's replay or one endpoint comparison is resident at a time.

The checker independently selects the finest two attempted tolerances from
raw worker records, retaining unsuccessful attempts, and compares historical
selections against the permitted frozen selection record. It checks declared
and executed cells/orders, exact case declarations, saved summary/result
agreement, grids/shapes, finite float64 arrays, first fitted crossing, decreasing
loss, initial and final circle prediction replay, final 8192-angle replay,
initial/final training loss replay, uniform carriers and saved initial closure
state. Dictionary checks independently recompute normalized Gram spectra,
effective ranks, Gaussian column RMS and orthogonal Gram residuals.

## Executed evidence

The completed raw-output audits exited 0 on CUDA1, NVIDIA GeForce RTX 3090, PyTorch 2.9.0+cu130,
NumPy 1.26.4, Python 3.10.14. Thread environment was one thread for OpenBLAS,
OpenMP and MKL, with `CUBLAS_WORKSPACE_CONFIG=:4096:8`. The default Python and
the sandbox CUDA environment were initially unavailable; those launcher checks
failed before GPU computation. Execution used the existing miniconda Python
with authorized host GPU access. No training was performed.

| Evidence | Initial pair audit A01 | Selected-pair audit A02 |
|---|---:|---:|
| Technical checks passed | 3788/3788 | 3809/3809 |
| Replayed trajectories | 64 | 64 |
| Model/reference metric records | 60 | 60 |
| Maximum metric discrepancy | 0 | 0 |
| Maximum prediction/loss replay discrepancy | 5.885e-15 | 5.885e-15 |
| Maximum Gram spectrum replay discrepancy | 0 | 0 |
| Maximum selected own endpoint discrepancy | 0.01298549988 | 0.009899405244 |
| All selected numerical gates | No | Yes |
| Checker wall seconds | 6.805 | 6.564 |

A01 independently confirms that the sole failed numerical-resolution gate was
`two_outliers_alternating_gaussian_p7`, with both endpoints fitted and maximum
discrepancy 0.012985499879930806. A02 selects its refinement and extra-refinement
outputs; the new discrepancy is 0.006834943869450161. No trajectory is removed
from the retained evidence. The maximum nested-grid sensitivity across A02 is
2.459e-6 for L1, 2.221e-16 for MSE/RMS, and 2.866e-6 for maximum error.

The source gate verifies every manifest-listed maintained module and identified
benchmark/dictionary/case/refinement producer against its recorded hash: all
167 such records in A02 match current files. Incidental manifest drift occurs
in `README.md`, `diverse_analyze.py`, `validate_diverse_runner.py` and this
checker, which was being developed when the extra worker snapshotted the broad
manifest. These are classified separately and do not supply the audited
trajectory production logic. All actual/current and expected hashes, complete
commands, selected source directories, per-check values, numerical metrics
and environment are retained in the evidence JSON files.

Reproduce with the exact `command` and environment in
`data/generated/random_dictionary_learned_circle_20260920/scaling_independent_check_A02/checks.json`,
using a new `--out` path and coordinating CUDA1 before execution. The command
includes all six historical trajectory roots, scaling discovery primary,
refined, and extra roots, and compares `scaling_discovery_A_analysis02`.

## Completed Stage B audit

After the supervisor appended all twenty-four Stage B trajectories to the same
discovery primary/refined roots, the unchanged frozen checker ran against
`scaling_discovery_analysis01` into `scaling_independent_check_B01`. It exited 0
in 10.234 seconds, auditing orders 1, 3, 5, 6, 7, 8, 9 and the full references.
The exact command, augmented input hashes and environment are retained in that
run's `checks.json`. No additional numerical-refinement candidate was found.

| Check | B01 result |
|---|---:|
| Technical checks passed | 5389/5389 |
| Replayed trajectories | 88 |
| Model/reference metric records | 84 |
| Maximum metric discrepancy | 0 |
| Maximum prediction/loss replay discrepancy | 1.077e-14 |
| Maximum Gram spectrum replay discrepancy | 0 |
| Maximum selected own endpoint discrepancy | 0.009899405244 |
| Maximum own endpoint discrepancy among new p8/p9 cells | 0.004419362209 |
| Unchanged producer/maintained source hash records | 227/227 |
| All selected numerical gates | Pass |

Source mismatch classifications are unchanged from A02: only incidental broad
manifest entries differ. The largest recorded regularized raw-Gram condition
through p9 is 908821.272; the largest recorded triangular residual is 6.995e-15.
The nested-grid maximum sensitivities remain the A02 values above.

Scalar comparisons of the independently recomputed RMS values give the
following preregistered p5-to-p9 discovery trigger, retaining both levels:

| Family | Level | Our RMS reduction | Better-random/ours ratio increase | C trigger |
|---|---|---:|---:|---|
| quadrant_pairs | lower selected | 72.4038% | 51.3186% | Pass |
| quadrant_pairs | higher selected | 72.4883% | 51.4124% | Pass |
| two_outliers_alternating | lower selected | 11.3629% | -37.8118% | Fail |
| two_outliers_alternating | higher selected | 12.2630% | -37.1570% | Fail |

The thresholds are at least 15% RMS reduction and at least 20% ratio increase
at both levels. Thus the paired-cluster discovery case triggers the fixed
confirmation campaign for both families and the negative control. This is a
branch decision on the discovery data, not confirmation evidence.

## Independent discovery summary audit

`scaling_independent_summary.py` independently derives random/ours ratios,
valid and unresolved tested-order sets, achieved target sets, smallest tested
budgets, and control/ours tested-budget ratios from B01's independent metrics
and dictionary dimensions. It uses exact `<=` target comparisons at both levels
with no threshold-rounding tolerance. All scalar arithmetic runs on CUDA
float64; structural key matching and file handling use the CPU. The original
raw-output checker remains unchanged.

The summary audit exited 0 on CUDA0 in 0.728 seconds, with all 6,327 checks
passing. All fourteen random/ours rows, 144 target rows and 96 tested-budget
ratio rows match both `summary.json` and their CSV copies, including field and
row multiplicity checks; no missing or extra rows were found. The largest
numerical discrepancy is 1.777e-15 (tolerance 1e-11). Evidence and
the exact command are in
`data/generated/random_dictionary_learned_circle_20260920/scaling_independent_check_B_summary01/summary_checks.json`.

The paired-cluster p7 RMS values are **0.04998412879949979** and
**0.05001803553249867** at the two selected levels. Thus p7 does **not** satisfy
the 0.05 target at both levels. The independently verified smallest tested
qualifying order is **p8**. The outlier case does not reach RMS 0.05 at any
tested order. These statements concern tested budgets only.

## Initial first-confirmation audit

Only `scaling_confirm1_primary01`, `scaling_confirm1_refined01` and their
claimed `scaling_confirm1_analysis01` output were supplied for this audit;
the cases are `pairs_confirm1`, `outliers_confirm1` and `negative_confirm1`.
The raw checker received a scope-only change: it now opens historical
selection records only when historical discovery cells are actually present.
The C1 audit therefore uses no historical trajectory or selection output.
Metric, replay and gate calculations are unchanged.

The raw audit `scaling_independent_check_C1_initial` exited 0 in 9.280 seconds,
passing all 3,639 technical checks and independently computing all 54 metric
records from sixty replayed trajectories. All metric discrepancies are zero;
the largest prediction/loss replay discrepancy is 1.399e-14. All sixty
producer/maintained source checks match. The sole failed numerical gate is `outliers_confirm1_orthogonal_p5`:
both endpoints are fitted, but their maximum discrepancy is
**0.010847879157941165**, exceeding 0.01. Thus 26/27 closure comparisons are
numerically valid, and this cell qualifies for the frozen resolution branch.
Its RMS endpoint discrepancy is 0.004553397212402149. The failed pair remains
in the evidence; it is not silently excluded or treated as scientifically valid.

The corresponding summary audit
`scaling_independent_check_C1_initial_summary` exited 0 in 0.557 seconds,
passing 8,762 checks. It verifies all nine random/ours rows, 216 target rows
and 144 budget-ratio rows in both JSON and CSV, including the invalid cell's
validity flags, unresolved-order lists and resulting exclusions. Further
confirmation results remain unaudited until generated. This initial failed
resolution gate is superseded for current selection by the following final
audit, while its source evidence is retained.

## Final first-confirmation audit

`scaling_independent_check_C1_final` adds `scaling_confirm1_extra01` and checks
`scaling_confirm1_analysis02`. The independently selected latest two levels
for `outliers_confirm1_orthogonal_p5` are refinement and extra-refinement; their
maximum discrepancy is **0.0015607632979275365**. The largest selected
discrepancy anywhere in C1 is 0.00915283984148818, so all 27 closure cells and
their references meet every numerical gate. All 3,660 raw technical checks pass;
all 54 metric records match exactly, and the largest replay discrepancy remains
1.399e-14. All 75 producer/maintained source records match. Both raw and summary processes
exited 0; their wall times were 9.624 and 0.608 seconds.

The raw checker additionally guards historical reads by width 2048, preventing
future width-4096 inputs from importing width-2048 selections. This scope-only
change does not affect the C1 arithmetic. The summary checker now also retains
the following p5-to-p9 RMS discriminator calculations directly in its evidence,
with all arithmetic and threshold comparisons on CUDA float64:

| Case | Level | Our RMS reduction | Better-random/ours ratio increase | Discriminator |
|---|---|---:|---:|---|
| pairs_confirm1 | lower selected | 62.8562% | 49.4969% | Pass |
| pairs_confirm1 | higher selected | 62.8260% | 49.3818% | Pass |
| outliers_confirm1 | lower selected | 23.2709% | -27.8990% | Fail |
| outliers_confirm1 | higher selected | 23.2492% | -27.9278% | Fail |
| negative_confirm1 | lower selected | 12.8610% | 67.5114% | Fail |
| negative_confirm1 | higher selected | 12.8646% | 67.4879% | Fail |

The final C1 summary passes all 8,763 checks over the same complete nine ratio,
216 target and 144 budget-ratio rows. One fresh configuration alone does not
trigger the width branch; the corresponding second fresh condition is required.

## Second-confirmation archive integrity and failed process

Before a C2 CUDA audit started, the author analyzer failed on a ZIP CRC error.
An independent read-only `ZipFile.testzip()` scan of all sixty C2 primary and
refined archives found exactly one damaged archive:
`scaling_confirm2_refined01/outliers_confirm2_ours_p9/arrays.npz`. Reading each
member identified `b1.npy` as its only failing member. The other five C2
`ours_p9` archives contain identical `b1.npy` payloads of 11,796,608 bytes,
SHA-256 `7f0780eaafeca12c34b9143204566f88120a3f0f94ea8b5173e16680f282ab97`,
with CRC32 2899841163 matching the damaged member's original recorded CRC.

The supervisor preserved the whole damaged archive in
`scaling_archive_repair01/original_corrupt_arrays.npz` and restored only the
static basis payload from the unanimous donors. Independent verification
derived the payload offset from the preserved ZIP local header, compared the
complete original and repaired byte strings, read and compared every other
ZIP member, CRC-tested the repaired archive and donors, and checked all
manifest hashes. All twenty checks pass. Exactly **one bit in one byte**
changed: archive offset 15,133,226, corresponding to payload offset 10,927,588.
Every byte outside the payload, including headers and trajectory arrays, is
identical; every non-`b1.npy` decoded member is identical. No training or
scientific array computation was repeated for this repair. Its cause remains
unknown. Independent evidence is retained in
`scaling_independent_check_C2_archive_integrity01.json` and
`scaling_independent_check_C2_repair01.json`.

The first subsequent C2 audit process exited **139** without progress output
or a completed check artifact. It did not establish a numerical verdict. The
failed attempt is preserved in `scaling_independent_check_C2_failed_launch01.json`.
A repeat CPU CRC scan passed all sixty archives; CUDA1 was idle with 43 MiB
allocated out of 24,576 MiB, without an observed memory-pressure explanation.
One authorized bounded retry enabled `PYTHONFAULTHANDLER=1`, retained its log,
and exited 0 in 9.680 seconds. The process failure did not recur, but its cause
is unresolved. No training was rerun.

This retry, `scaling_independent_check_C2_retry01`, passed all 3,639 technical
checks and all 54 metric comparisons against `scaling_confirm2_analysis02`.
It independently identified the sole initial numerical failure:
`outliers_confirm2_orthogonal_p1`, both endpoints fitted, maximum discrepancy
**0.01878879938778244**. This separate numerical issue was then handled by the
permitted extra refinement, not by the archive repair.

## Final second-confirmation audit and stopping decision

`scaling_independent_check_C2_final` adds `scaling_confirm2_extra01` and checks
`scaling_confirm2_analysis03`. It exited 0 in 9.163 seconds with all 3,660
technical checks passing, sixty trajectories replayed and all 54 metric
records agreeing exactly. The largest prediction/loss replay discrepancy is
1.311e-14. All 75 producer/maintained source hashes match; normalized Gram
spectra replay exactly. The largest recorded regularized raw-Gram condition
is 919267.499 and the largest recorded triangular residual is 6.440e-15.

The independently selected refinement/extra pair for
`outliers_confirm2_orthogonal_p1` has discrepancy **0.001856237740659461**.
The maximum over all selected C2 predictors is 0.007904212677237878. Thus all
27 closure comparisons and their references satisfy the numerical gates.
The final summary audit exited 0 in 0.591 seconds and passed all 8,763 checks
over nine ratio rows, 216 target rows and 144 tested-budget-ratio rows in both
JSON and CSV. Its maximum numerical mismatch is 1.777e-15.

The independent CUDA summary calculation gives:

| Case | Level | Our RMS reduction | Better-random/ours ratio increase | Generic discriminator |
|---|---|---:|---:|---|
| pairs_confirm2 | lower selected | 34.4996% | -31.9206% | Fail |
| pairs_confirm2 | higher selected | 34.5156% | -31.8719% | Fail |
| outliers_confirm2 | lower selected | 18.5177% | -27.1868% | Fail |
| outliers_confirm2 | higher selected | 18.5385% | -27.1574% | Fail |
| negative_confirm2 | lower selected | 19.8105% | 100.7866% | Pass |
| negative_confirm2 | higher selected | 19.8168% | 100.7572% | Pass |

Neither eligible positive family passes in both fresh conditions, so the
frozen D gate is false. The negative control's generic discriminator pass does
not qualify it for D. Its better-random/ours RMS ratios are approximately 0.40
at p5 and 0.80 at p9, so the random control still has lower error there despite
the growing ratio. This negative result remains visible rather than being
treated as support for a family-specific mechanism or universal superiority.

## Limits and remaining work

The raw basis and Cholesky factors used in the learned dictionary whitening are
not saved. Their gates are checked against retained metadata, with unchanged
producer source and the separate preflight record; they are not independently
reconstructed here. The largest recorded regularized raw-Gram condition through
Stage B is 908821.272 (limit 1e10); the largest recorded triangular solve residual
is 6.995e-15 (limit 1e-8). This audit recomputes normalized Gram spectra but does not
independently rerun legacy dictionary generation or every trajectory RHS step.

The numerical endpoint comparisons are empirical consistency diagnostics,
not rigorous ODE error bounds. This audit validates finite saved outputs and
their reported errors, without proving rates, feature efficiency asymptotics,
generalization over datasets/seeds, or population/infinite-width limits.
The completed final discovery and confirmation outputs are audited. The
conditional width branch is not triggered. No further training is authorized
by these audit results.

## Source and evidence fingerprints

All values are SHA-256. Full input-artifact hashes are in each evidence JSON.

| Artifact | Hash |
|---|---|
| Executed checker, all A/B audits | `3223fd4588588f7b3f39729f942000647b9c0cfb2e0b9ee66f5479e266fef10d` |
| Executed checker, C1 initial (scoped historical read) | `fda52cd1ceb2453f3a7dbedd81eaaacc4990b996cd70bc9ea3afad169afd915a` |
| Executed checker, C1 final and all C2 audits (historical width guard) | `3c1666d0fb5cb83b4175c9a97f27609fd784b44fa314a2e83af5d98020ed3a67` |
| A01 checks.json | `39d822654de571c2427ecf581daadfa6af5b04671125ed5b7776603f6d7d423e` |
| A02 checks.json | `eb1a799c1c5c7a95797db0e28ed64391d7a204e172388f0dab1bac2af61e3bdc` |
| B01 checks.json | `66c3cb49c3916b1e99a3b5fd517f53d4788c54c6c7d6b4bc42d1d4a3b38ef980` |
| Executed independent summary checker | `571588d79ff87d36b62a378d6ab4ce56db741d682fc84d6840f7c8498afa74d0` |
| Executed C1/C2 final summary checker (adds discriminator evidence) | `846690d359bf77c51949753157361b8ee23903576964bc15003de8147e58b1aa` |
| B_summary01 summary_checks.json | `b6bb50ba401425bab5ee48f8a087523b6723cd6fec1d06ecb474fc9837654de7` |
| C1_initial checks.json | `a7a42637c4d3bd0b8650572551039d0f22e71f20661070b9d18250da8a753c77` |
| C1_initial_summary summary_checks.json | `db0f4a85ff4aeb3593727b32eb4faac446beb7329e037afa75951283771d0955` |
| C1_final checks.json | `02870f7abece1e82faa67d167023338852c369da777fa31c9e5a778a8e3d6016` |
| C1_final_summary summary_checks.json | `4e065986d495a77ced9db27aa3ae854035e1cb7c88f38ffca820149d6bce825f` |
| C2 archive integrity evidence | `56a9a190c2509a314dae29d0b535292eac7f5da35251f63adf8021db790c91eb` |
| C2 independent repair evidence | `86da8d0c0193dd4189e0f92e746d3df005ae7ec493d8fb8a77e68f2d86bb6034` |
| C2 failed-launch record | `7936574501a0360a4982f407aed0745b814a21ff31d4c2cde2b14833137384b5` |
| C2_retry01 checks.json | `3e9fac4c47170dd00d0a5b0963189dd962d9bf27d3ef1f7c52fe9bebb3913e99` |
| C2_final checks.json | `99da572b4f1c19184af0dac31d1e01f8cb7d07eaeadada2a82546acee3255bcc` |
| C2_final_summary summary_checks.json | `7cb081115513d7142816669576c23ec507a6ea6fb7f5d51492b26a798c8120db` |
| SCALING_PROTOCOL.md | `a75939d69f4b5db961fab1d6ab1b9a66bdfee0ab9d69b11c9e4d02fb62418e7b` |
| scaling_cases.py | `a0276e2627aef6a1c52e5c179ef24a6f5f063e369daebadb06a39bf81e087d22` |
| diverse_cases.py | `65942e3e8e52b2f4af10242963c0159cda80a8c80f9d2c8dc9f77c5d9d3aa6f4` |
| AGENTS.md | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| RESEARCH_WORKFLOW.md (Part 1 read) | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| decisive-experiments.md | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| adversarial-audit.md | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
