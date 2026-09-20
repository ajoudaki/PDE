# Independent scaling output check

Internal empirical audit, 2026-09-20. This is not an independent integration,
promotion review, asymptotic result, or assessment of other studies.

**Discovery Stages A and B pass this audit.** The complete B01 audit passes all
5,389 technical checks. Every selected model/reference pair is fitted and its
own endpoint refinement discrepancy is at most 0.01. Eighty-four independently
computed metric records, comprising forty-two closure cells at two selected
numerical levels, agree with the published analysis exactly at saved float64
precision; the required comparison tolerance was 1e-11. The paired-cluster
family satisfies the preregistered confirmation trigger at both selected levels.
The initial first-confirmation audit verifies 26/27 closure cells; one cell
requires the permitted numerical refinement described below.

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
dictionary dimensions.

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

The raw-output audits exited 0 on CUDA1, NVIDIA GeForce RTX 3090, PyTorch 2.9.0+cu130,
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
confirmation and resolution results remain unaudited until generated.

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
Confirmation and width-check outputs require additional audits when generated.

## Source and evidence fingerprints

All values are SHA-256. Full input-artifact hashes are in each evidence JSON.

| Artifact | Hash |
|---|---|
| Executed checker, all A/B audits | `3223fd4588588f7b3f39729f942000647b9c0cfb2e0b9ee66f5479e266fef10d` |
| Executed checker, C1 initial (scoped historical read) | `fda52cd1ceb2453f3a7dbedd81eaaacc4990b996cd70bc9ea3afad169afd915a` |
| A01 checks.json | `39d822654de571c2427ecf581daadfa6af5b04671125ed5b7776603f6d7d423e` |
| A02 checks.json | `eb1a799c1c5c7a95797db0e28ed64391d7a204e172388f0dab1bac2af61e3bdc` |
| B01 checks.json | `66c3cb49c3916b1e99a3b5fd517f53d4788c54c6c7d6b4bc42d1d4a3b38ef980` |
| Executed independent summary checker | `571588d79ff87d36b62a378d6ab4ce56db741d682fc84d6840f7c8498afa74d0` |
| B_summary01 summary_checks.json | `b6bb50ba401425bab5ee48f8a087523b6723cd6fec1d06ecb474fc9837654de7` |
| C1_initial checks.json | `a7a42637c4d3bd0b8650572551039d0f22e71f20661070b9d18250da8a753c77` |
| C1_initial_summary summary_checks.json | `db0f4a85ff4aeb3593727b32eb4faac446beb7329e037afa75951283771d0955` |
| SCALING_PROTOCOL.md | `a75939d69f4b5db961fab1d6ab1b9a66bdfee0ab9d69b11c9e4d02fb62418e7b` |
| scaling_cases.py | `a0276e2627aef6a1c52e5c179ef24a6f5f063e369daebadb06a39bf81e087d22` |
| diverse_cases.py | `65942e3e8e52b2f4af10242963c0159cda80a8c80f9d2c8dc9f77c5d9d3aa6f4` |
| AGENTS.md | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| RESEARCH_WORKFLOW.md (Part 1 read) | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| decisive-experiments.md | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| adversarial-audit.md | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
