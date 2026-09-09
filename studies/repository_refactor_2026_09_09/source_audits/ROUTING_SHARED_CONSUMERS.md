# Final shared-consumer and helper-placement slice

Repository: `/home/amir/Codes/PDE`. Status: **complete within the authorized scope; frozen for independent acceptance**. Freeze time and exact hashes are recorded in `FROZEN_SLICE.json`.

## Three consumers

| File under `studies/mfp_gaussian_calculus/` | Change |
|---|---|
| `depth_order5/audit/run_checks.py:10` | Unconditional archive-only refusal is the first executable statement, before imports, file access, or report reconstruction. Its frozen-promotion/report pipeline has no supported fresh interface. |
| `depth_order5/primary/run_lightweight_checks.py:3` | Same fail-closed treatment before all imports/work. No bypass, historical replay regeneration, or replacement freeze was added. |
| `depth_order5_scalar/primary/audit_full_scalar_recurrence.py:38` | Defaults to `data/generated/mfp_gaussian_calculus` as its study-data input root. `--input-dir` selects an explicit read-only root; `--historical-inputs` explicitly selects retained historical data. These choices are mutually exclusive. The callable `run_audit` at line 215 exposes the same options. Output remains JSON on stdout: this consumer creates no output files. |

The scalar audit's labels at **45–50** distinguish `source/...` from `inputs/...`; emitted `input_roots` at **226** supply the corresponding absolute roots. The control-result reader at **151–159**, sine-experiment reader at **186–198**, and reference-map reads at **53–78** all follow the selected root. No selected data path is serialized relative to the source tree.

The reference-loader dependency still has source-bound defaults. Without editing that fourth file or its shared global state, this audit now resolves the three reference paths locally and applies the same digest, schema, canonicalization, and expected-count contract. It reuses the independent canonicalizer and unchanged expected digests/counts. The shared `depth_order5_scalar/audit/reference_maps.py` is byte-unchanged.

The H2 formula manifest remains a fixed source input. Explicit historical mode can read the retained source `depth_order5/independent/CONTROL_AUDIT.json` when there is no historical-data copy. Fresh mode never silently falls back to that certificate or historical experiment results. Formula calculations, candidate freeze digest, expected values, and existing proof/evidence/seal bytes were not changed.

## Stable support placement

Moved the helper to **`studies/_output_paths.py`**, directly beside the flat study catalogue. `REPO_ROOT` now uses `Path(__file__).resolve().parents[1]` at **line 14**. The old `studies/repository_refactor_2026_09_09/output_paths.py` is removed as part of the move; no forwarding shim or live dependency on that dated study remains. The helper's content is otherwise byte-identical to its pre-move version. Its old source is retained in this private `BEFORE.json` snapshot as well as the moved file.

There are **40 direct live importers across eight studies**: 39 existing callers were mechanically rewritten; the scalar audit is the new caller. Exact importer files and line numbers are in `FROZEN_SLICE.json`. The helper imports only standard-library `argparse` and `pathlib` (plus the annotations language directive), and does not import study implementations or the established `code/pde` library. Existing direct-script repository-root bootstrap code was left unchanged. No package folder was added, and nothing was placed in or edited under `code/`.

| Importing study | Direct importers |
|---|---:|
| `causal_flow_peeling_calculus` | 4 |
| `d3_arctan_closure_program` | 3 |
| `resnet_activation_controls` | 3 |
| `mfp_identity_compiler` | 3 |
| `mfp_linear_growth_uniform_counterexample` | 2 |
| `mfp_gaussian_calculus` | 18 |
| `stieltjes_direct_loewner` | 3 |
| `stieltjes_proxy_campaign` | 4 |

The original private tiny-test harness now imports the stable module. Its previous frozen test log/report/inventory was not overwritten; the rerun logs are saved in this new private directory.

## Verification

**28/28 tiny tests pass:** the prior 15 routing tests plus 13 shared-consumer/placement tests. Final transcripts are `original-routing-tests-3.txt` and `shared-consumers-tests-3.txt`. An earlier synthetic fixture used a string rather than integer depth key; the fixture was corrected, with no implementation change needed. Earlier transcripts remain available for transparency.

Checks include:

- actual execution of both archive modules with imports forbidden, for both import and direct-entrypoint modes;
- exact mechanical equality of all 39 importer changes and the helper's single anchoring change;
- fresh/historical/explicit input selection and label-to-path round trips outside the source tree;
- stubbed end-to-end scalar audit flow proving that all result readers receive the selected root;
- retained candidate/reference digests, expected reference counts, both accepted map schemas, and refusal of digest/count/schema mismatches;
- read-only retained control/experiment checks and reference-file hashes, without expanding the historical maps;
- unchanged mathematical function bodies and **11 protected source/evidence/history/seal files**, including Hegel's hostile-audit guard;
- the prior tiny writer/checkpoint/guard tests and 11 real CLI help checks from an external working directory.

No campaign, installation, symbolic production audit, new scientific result, report reconstruction, seal refresh, historical write, Git operation, or unrelated repository edit was performed. Temporary synthetic fixtures were confined to `/tmp` and automatically removed.

## Remaining blockers and boundary

**No unresolved routing blocker remains in these three authorized consumers or the helper move.** The two archival entrypoints now intentionally refuse instead of presenting a broken fresh pipeline. Fresh scalar mode requires the selected fresh input files; absent fresh data is not permission to copy, regenerate, or silently substitute historical evidence. Full scientific audit execution was deliberately not part of this verification.

Hegel's `run_hostile_checks.py`, the reference-loader source, all immutable payloads, repository reports/manifests/seals, `code/`, and other workers' non-mechanical changes were left untouched. The source change inventory distinguishes the 39 import-only edits from the three consumer edits and the helper move. The combined current fingerprints also supersede import-path hashes from the earlier 49-file slice; its historical report and snapshots remain unchanged.
