# stieltjes proxy campaign

This is a preserved research study, not an established-library entry. Historical
claims and audit labels retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for corrections and the [established reading guide](../../docs/README.md) for
currently maintained self-contained proofs.

## Source documents

- [FAILED_STAGE2.md](FAILED_STAGE2.md)
- [PROTOCOL.md](PROTOCOL.md)
- [RESULTS.md](RESULTS.md)
- [SUCCESSOR_01_PROTOCOL.md](SUCCESSOR_01_PROTOCOL.md)
- [SUCCESSOR_02_PROTOCOL.md](SUCCESSOR_02_PROTOCOL.md)

Generated data were separated during the repository cleanup. Old absolute paths,
commands and frozen hashes may describe the historical layout; the
[migration record](../repository_refactor_2026_09_09/PLAN.md) explains how to locate
preserved files. Do not run an old campaign assuming its former output layout.

Fresh reference runs use repository
`data/generated/stieltjes_proxy_campaign/reference/runs/`; retained runs are
read-only under `data/historical/studies/stieltjes_proxy_campaign/reference/runs/`.
Source/configuration/unlock files remain here. The consumed scientific attempt
is not reopened by moving its data, and current source-hash gates remain binding.

The offline CLI is `analysis/run_frozen_pilot.py`. It requires explicit
`--summary`, `--config`, `--analysis-config`, and `--output`; it does not search
for runs. Both its success and failure writers require a new destination under
this study's generated tree or external scratch and refuse final/temporary
collisions before analysis. See [analysis/README.md](analysis/README.md) for
current paths. Old source-binding failures are real limitations, not permission
to waive checks or regenerate expected seals.

The callable `load_reference_run` likewise requires an explicit `config_path`;
it never guesses a config from generated or historical run directories.

`reference/side_checks/gd_vs_rk4_n4096.py` and `gd_vs_rk4_n8192_point.py` remain
historical-only comparisons against their explicitly fixed retained references.
They do not consume fresh reference runs or silently select a replacement.
Both guard named outputs and open the required reference before CUDA work;
missing/unreadable references refuse without producing a result. Their original
numerical routines, fixed settings and wall/resource caps are unchanged.
