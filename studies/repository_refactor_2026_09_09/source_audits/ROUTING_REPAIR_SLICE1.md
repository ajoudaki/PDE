# Frozen routing repair slice

Repository: `/home/amir/Codes/PDE`. Frozen **2026-09-09 11:52:12 UTC** for independent acceptance. No further repository edits by this task after this freeze.

**Implemented: 49 Python source/test/support files; 15 tiny tests pass. Full repository acceptance is not claimed: three shared Gaussian consumer interfaces still need owner disposition below.**

Exact files, pre-implementation/frozen SHA-256 values, routing line numbers and entrypoints: `PATCH_INVENTORY.json`. Original static findings and pre-implementation inventory remain frozen as `REPORT.md` and `FROZEN_INVENTORY.json`; the original report hash still matches. `TEST_RESULTS.txt` is the successful verification transcript; `test_routing.py` is the reproducible private fixture suite.

## Implemented scope

All paths below are repository-relative. Output overrides are checked before computation where an entrypoint or callable accepts them. Fresh defaults are rooted at `data/generated/<study>`, independent of working directory. The support helper rejects repository source/history/other-study destinations and symlink redirection beneath output directories; explicit external scratch is permitted. Parsing does not create output directories.

| Group | Frozen implementation |
|---|---|
| A1 | Four causal-flow probes now have `--output-dir`; defaults preserve the `experiments/outputs/<probe>` suffix under generated data. No scientific loops or calculations changed. |
| A2 | Three D3 GPU analyzers now separate `--input-dir` / `--historical-inputs` from `--output-dir`. Default inputs match the generated `gpu_gauge_gradient_results`, `gpu_tail_results`, or `gpu_weighted_response_results` directories; result JSON/Markdown goes to the generated study root. Existing simulation CLIs still require user-selected output paths. |
| A6 | Standalone activation PDE/reference runners use `data/generated/resnet_activation_controls/results/raw` and reject unsafe overrides at the start of `run`. Figure builder separates input/output roots; `--historical-inputs` explicitly reads retained `evidence/processed`, without fallback to historical data during fresh mode. The actual retained summary and CSV were checked for presence. |
| A7 | Identity search, spectral closure and Hankel audit write under generated `linear_gaussian_program/depth2_all_order_search`. Closure/Hankel expose explicit fresh or historical input selection. The production-artifact regression reads fixed historical results, or an explicit `IDENTITY_SEARCH_INPUT_DIR` fixture; expected mathematical values were not changed. |
| A9 | Linear coefficient-map producer has a generated default and `--output-dir`. Six connected readers accept `--map-path` or `--historical-inputs`; default map input is fresh generated data. Removed import-time payload reads; the Newton reader's existing atom-cache construction is now inside its existing computation function after input selection. No formulas changed. |
| A10 | Direct-Loewner defaults had already been moved concurrently. Added output safety checks to simulation/diagnostic entrypoints and an explicit fresh `--output-dir` on the clock pilot. Did not rewrite the concurrently repaired corrected-clock or finite-width runners. |
| A11 | Remaining Gaussian prediction, gate, comparison, audit, diagnostic-ledger and regression writers now use generated output interfaces. Resumable NPY checkpoints are read/written only in the selected fresh output directory. Comparison inputs select fresh/historical coefficient data while retained formula source and freeze evidence remain read-only. Prediction digests remain pinned. Updated the disjoint observable and Route-A result consumers; shared consumers are deferred below. |
| A13 | Proxy reference runner defaults to generated `reference/runs`, accepts `--output-root`, and preserves direct-child run IDs, nonempty-run refusal and production authorization. The FP32 delegate and capped launcher inherit the new default without changes. |
| B | Three n16384 side checks no longer default to an old visualization directory. Default output is generated `reference/side_checks`; merger has separate explicit input selection. Existing shard/merge refusal is retained; the single-pair entrypoint now also refuses existing results before device work. Old visualization shards can be read only by an explicit `--input-dir` when needed. |
| C | `depth_order5/independent/freeze_depth_maps.py` now fails closed in both `main` and its artifact writer. `depth_order5_scalar/multi_observable/independent_route_a/reduce_gamma04.py:emit` fails closed; its pure `transitions()` remains available. No recompilation, seal rewrite, or new-freeze option was introduced. Other order5/primary re-freezers were already guarded concurrently and were not edited again. |
| D mixed | `depth_order5/primary/generate_frozen_artifacts.py:83` and `order5/compiler/generate_artifacts.py:31` already fail closed; the tiny tests verified these guards before any work. No further edit needed. Pure recurrence/formula-source generators and hand-authored configuration were intentionally not swept into a data relocation. |

New implementation support: `studies/repository_refactor_2026_09_09/output_paths.py`; study-specific linear map input helper: `studies/mfp_linear_growth_uniform_counterexample/map_inputs.py`. No existing repository-maintenance code or manifest was changed.

## Precise shared-consumer handoff / remaining integration blockers

No direct agent-messaging tool was exposed in this task. This section is the message to main; these shared files were deliberately **not edited**. Their owner should either provide a distinct fresh-input interface or explicitly retain them as archive-only. Do not repair them by regenerating historical artifacts/seals.

1. `studies/mfp_gaussian_calculus/depth_order5/audit/run_checks.py`: source-bound comparison/Q0 inputs at **60, 68** and experiment input at **87** do not follow the new producer outputs under generated `depth_order5/audit`. Its freeze readers at **33–56** also join moved coefficient artifacts to source directories. It additionally invokes the primary report verification interface. Requires owner decision on historical replay versus fresh verification; keep fixed freeze metadata distinct from selected result inputs.
2. `studies/mfp_gaussian_calculus/depth_order5/primary/run_lightweight_checks.py`: **49–54** reads new comparison/Q0/gate/experiment/control products through source-side `hostile` and `independent` directories; **27–42** couples frozen artifacts and primary products. It is shared with the concurrently modified primary/report routes. Select generated result roots separately from immutable source/freeze inputs, or explicitly close the archival entrypoint.
3. `studies/mfp_gaussian_calculus/depth_order5_scalar/primary/audit_full_scalar_recurrence.py`: **108** reads the independent control result from source and **138** reads the sine experiment from source. Moving these two bindings alone is insufficient: **131–132** serialize input labels with `relative_to(ROOT)` where ROOT is source. Use explicit input-root selection and compatible labels, preserving existing expected values and hashes.

Hegel-owned `depth_order5_scalar/multi_observable/audit/run_hostile_checks.py` already raises archive-only at **21–24**, before subprocess work. Its dormant Route-A ledger/result and Route-S experiment references are **not** an additional live blocker; leave that guard intact. F1–F3 and A12 were untouched. Main's A3–A5 and A8 were untouched, including their tests, docs, manifests and commits.

## Verification and limits

- **15/15 tests pass**, including syntax compilation across all modified study sources, actual CLI help for 11 inspected entrypoints from an external working directory, default/historical/override root checks, symlink rejection, a stubbed causal writer, a stubbed identity writer, D3 and proxy input-boundary checks, two tiny pre-existing NPY checkpoint-resume fixtures, and archive guards before computation.
- Tests create only short-lived `/tmp/pde-routing-test-*` fixtures; cleanup is automatic. No campaign, scientific benchmark, production runner, installation or mathematical reproduction was run. No generated study data was produced as part of verification.
- `torch`, `sympy`, `pandas`, and `matplotlib` are absent from the available Python environment. Their production modules were **not** fully imported/executed; routing functions were compiled from the actual source AST with numerical boundaries stubbed. This is a verification limit, not a proposal to install dependencies or run campaigns.
- Existing source freezes may correctly reject changed live source. No digest expectations, historical bytes, configuration, seal, proof/report source, repository manifest, Git state, or core mathematical algorithm was edited by this task.

The frozen source slice is ready for independent routing review. The three shared interfaces above prevent claiming end-to-end fresh-consumer completeness for the entire Gaussian study.
