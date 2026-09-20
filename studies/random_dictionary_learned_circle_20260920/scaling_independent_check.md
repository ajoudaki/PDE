# Independent scaling output check

Internal empirical audit, 2026-09-20. This is not an independent integration,
promotion review, asymptotic result, or assessment of other studies.

**Stage A after its permitted resolution run passes this audit.** All 3,809
technical checks pass. Every selected model/reference pair is fitted and its
own endpoint refinement discrepancy is at most 0.01. Sixty independently
computed metric records, comprising thirty closure cells at two selected
numerical levels, agree with the published analysis exactly at saved float64
precision; the required comparison tolerance was 1e-11.

## Scope and independence

The supervisor assigned this checker a fresh scoped context. Scientific reading
was restricted to `SCALING_PROTOCOL.md`, `scaling_cases.py`, the explicitly
subsequently permitted `diverse_cases.py`, and this study's raw `scaling_*` and
`diverse_*` output schemas. Relevant raw dictionary validation metadata was
inspected. The supervisor explicitly permitted the historical
`diverse_analysis01/selected_levels.json` selection record and supplied the
neutral saved-state maps below. The two scaling `metrics.json` files were read
as claimed outputs to compare, not as implementation inputs.

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

Both runs exited 0 on CUDA1, NVIDIA GeForce RTX 3090, PyTorch 2.9.0+cu130,
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

## Limits and remaining work

The raw basis and Cholesky factors used in the learned dictionary whitening are
not saved. Their gates are checked against retained metadata, with unchanged
producer source and the separate preflight record; they are not independently
reconstructed here. The largest recorded regularized raw-Gram condition is
252226.434 (limit 1e10); the largest recorded triangular solve residual is
3.04e-15 (limit 1e-8). This audit recomputes normalized Gram spectra but does not
independently rerun legacy dictionary generation or every trajectory RHS step.

The numerical endpoint comparisons are empirical consistency diagnostics,
not rigorous ODE error bounds. This audit validates finite saved outputs and
their reported errors, without proving rates, feature efficiency asymptotics,
generalization over datasets/seeds, or population/infinite-width limits.
Stage B and later output require additional audits when generated.

## Source and evidence fingerprints

All values are SHA-256. Full input-artifact hashes are in each evidence JSON.

| Artifact | Hash |
|---|---|
| Executed checker, both A audits | `3223fd4588588f7b3f39729f942000647b9c0cfb2e0b9ee66f5479e266fef10d` |
| A01 checks.json | `39d822654de571c2427ecf581daadfa6af5b04671125ed5b7776603f6d7d423e` |
| A02 checks.json | `eb1a799c1c5c7a95797db0e28ed64391d7a204e172388f0dab1bac2af61e3bdc` |
| SCALING_PROTOCOL.md | `a75939d69f4b5db961fab1d6ab1b9a66bdfee0ab9d69b11c9e4d02fb62418e7b` |
| scaling_cases.py | `a0276e2627aef6a1c52e5c179ef24a6f5f063e369daebadb06a39bf81e087d22` |
| diverse_cases.py | `65942e3e8e52b2f4af10242963c0159cda80a8c80f9d2c8dc9f77c5d9d3aa6f4` |
| AGENTS.md | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| RESEARCH_WORKFLOW.md (Part 1 read) | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| decisive-experiments.md | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| adversarial-audit.md | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
