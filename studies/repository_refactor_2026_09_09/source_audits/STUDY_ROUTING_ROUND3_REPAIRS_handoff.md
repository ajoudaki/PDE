# F1–F7 migration implementation handoff

Status: COMPLETE for the requested slice; ready for integration/review. No coordinator blocker. Repository edits are finished; no commit was made.

This implements the confirmed acceptance findings and specifically authorized path-consumer qualifications only. It is not a broader legacy/science audit and does not establish scientific correctness or reproduction.

## Exact change inventory

33 files changed or added, all inside the seven owned study trees: 18 implementation files (17 modified, one new study-local boundary module), six README qualifications, eight new bounded test files, and one existing bounded test adaptation. No shared helper, root metadata, configuration, scientific source seal, or historical artifact was edited.

The complete integration diff, including untracked/new files, is [changes.patch](/tmp/pde-migration-fixes.Lq2emFoj/changes.patch). The workspace already contains these edits; do not apply the patch over them a second time. [changed-files.json](/tmp/pde-migration-fixes.Lq2emFoj/changed-files.json) lists exact targets. [changed-hashes.json](/tmp/pde-migration-fixes.Lq2emFoj/changed-hashes.json) provides full per-target before/after SHA-256 values; null before means a newly added file.

| Finding | Implemented boundary repair |
|---|---|
| F1 | Both finite-width mains now use the already declared `MFP_COMPILER` recurrence path instead of undefined `PEELING`. No recurrence/calibration arithmetic changed. |
| F2 | Shared frozen `StudyPaths` guards added to corrected-clock main/log callable; proof processed-output CLI/writer/atomic helper; breadth validation main/writer; both proxy side-check entry and publication paths. Original path objects are guarded before losing alias information. |
| F3 | Both exact-reference raw runners precompute the unchanged configuration identity and final name before seed workers. Final and deterministic partial paths are checked against selected PDE-seal/case-registry inputs. |
| F4 | Both PDE raw siblings use the same final/partial input check for restart and case-registry inputs before time stepping. Activation raw partials now use exclusive creation; activation text/record writer destinations and partials are guarded and exclusive. |
| F5 | Width analysis checks output against all five selected inputs before any input load and again before publication. Same-path, lexical, symlink, and hardlink collisions refuse. |
| F6 | Both GD/RK4 side checks guard their outputs and check/open their required fixed reference before CUDA work. No reference fallback, new input selector, or cap change was introduced. |
| F7 | Archive-only refusal is the first statement in both attempt-claim and attempt-finish callables, before lock creation, ledger access, or budget accounting. Existing CLI/reservation/failure guards remain intact. |
| Path item 1 | Activation seal consumer now joins logical labels to `RESULTS.parent`, matching the producer and analyzer. All hash/authorization comparisons are otherwise unchanged. |
| Config qualification | `load_reference_run` rejects omitted `config_path` with a clear error before reading the summary. Explicit configuration remains supported; there is no guessed source path. |
| Historical-only qualification | Proxy README explicitly documents the two side checks as fixed historical-reference consumers, not consumers of newly generated runs. |

Equivalent sibling repairs were confined to already inspected boundaries: generalization PDE preflight, activation record partial writer, proof atomic writer/CLI preflight, and n4096 reference opening. No unrelated long-horizon or legacy cases were added.

Primary implementation entry files:

- [Generalization raw boundary helper](/home/amir/Codes/PDE/studies/resnet_generalization/generalization_paths.py), [exact runner](/home/amir/Codes/PDE/studies/resnet_generalization/run_exact_reference.py), [PDE runner](/home/amir/Codes/PDE/studies/resnet_generalization/run_pde.py).
- [Activation local boundary helper](/home/amir/Codes/PDE/studies/resnet_activation_controls/output_paths.py), [exact runner](/home/amir/Codes/PDE/studies/resnet_activation_controls/source/run_exact_reference.py), [PDE runner](/home/amir/Codes/PDE/studies/resnet_activation_controls/source/run_pde.py), [analysis writer](/home/amir/Codes/PDE/studies/resnet_activation_controls/analyze_activation.py), [record writer/seal consumer](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py).
- [Proof processed-output interface](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/analyze_results.py).
- [Corrected-clock interface](/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/run_corrected_clock_test.py).
- [Order-13 main](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_order13_median.py), [calibrated-ratio main](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_calibrated_ratio.py).
- [Breadth validation writer](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py), [width input/output preflight](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/width_analysis.py), [archive-only mutation callables](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/run_local_qualification.py).
- [n4096 side check](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n4096.py), [n8192 side check](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py), [explicit-config consumer](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/reference_data.py).

## Bounded verification

**92 tests passed across 19 explicitly selected suites; no failures.** This includes the original 62 allowed tests and 30 new test methods, many containing multiple alias/input-role cases. No broad test discovery was used.

[test-results.json](/tmp/pde-migration-fixes.Lq2emFoj/test-results.json) contains exact suite names, counts and log locations. [fixture-hashes.json](/tmp/pde-migration-fixes.Lq2emFoj/fixture-hashes.json) contains **72 exact before/after protected-fixture hash records; all match**.

Tests used extracted complete interfaces or explicitly identified publication/preflight blocks, standard-library mocks, inert private bytes, and the original permitted tiny-array fixtures. No real scientific worker, trajectory, coefficient generation, reanalysis, native compilation, GPU/training, or installation ran. Every child used bytecode-disabled execution, the private temporary/cache directory and a 45-second upper timeout.

Covered failure paths include:

- refusal before loader/worker/CUDA calls or output-directory creation where the required path is already known;
- missing and unreadable fixed side-check references;
- named output-directory/final/intermediate aliases;
- own-input final/partial collisions for both raw families;
- exclusive partial creation and refusal of stale partials;
- failed exact publication preserving both selected input and previous final, with the resulting partial blocking a retry before workers;
- proof atomic replacement failure preserving the previous final and cleaning only its own random temporary;
- claim/finish refusal before any lock or ledger access.

Positive controls preserve useful behavior: distinct restart inputs in the same output directory, regular raw output with mocked workers, ordinary processed-result replacement, write-once idempotence, normal corrected-clock logging, clean CLI progression to mocked input/device boundaries, and explicit config loading for generated or historical summary locations.

`git diff --check` passed for the seven owned trees.

| Suite | Tests | Log |
|---|---:|---|
| resnet_generalization/tests/test_migration_paths.py | 7 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-00.log) |
| resnet_generalization/tests/test_output_boundaries.py | 7 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-01.log) |
| resnet_generalization/tests/test_writer_boundaries.py | 6 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-02.log) |
| resnet_proof_audit/tests/test_trapezoid_compat.py | 1 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-03.log) |
| stieltjes_finite_width/test_migration_paths.py | 5 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-04.log) |
| stieltjes_finite_width/test_output_boundaries.py | 3 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-05.log) |
| stieltjes_finite_width/test_shared_output_paths.py | 6 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-06.log) |
| stieltjes_hybrid_campaign/breadth_panel/test_migration_paths.py | 9 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-07.log) |
| stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py | 4 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-08.log) |
| stieltjes_hybrid_campaign/width_ladder/euler_fp32/test_output_boundaries.py | 6 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-09.log) |
| stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py | 8 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-10.log) |
| resnet_generalization/tests/test_raw_output_preflight.py | 7 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-11.log) |
| resnet_activation_controls/tests/test_migration_boundaries.py | 5 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-12.log) |
| resnet_proof_audit/tests/test_migration_boundaries.py | 4 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-13.log) |
| stieltjes_finite_width/test_migration_preflight.py | 1 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-14.log) |
| stieltjes_direct_loewner/test_writer_boundaries.py | 3 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-15.log) |
| stieltjes_hybrid_campaign/breadth_panel/test_acceptance_boundaries.py | 3 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-16.log) |
| stieltjes_hybrid_campaign/width_ladder/test_analysis_boundaries.py | 2 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-17.log) |
| stieltjes_proxy_campaign/analysis/tests/test_reference_migration_boundaries.py | 5 | [PASS](/tmp/pde-migration-fixes.Lq2emFoj/suite-18.log) |

## Function/AST and frozen-contract preservation

[function-ast.json](/tmp/pde-migration-fixes.Lq2emFoj/function-ast.json) records exact before/after AST hashes for definitions in changed Python files. [preservation.json](/tmp/pde-migration-fixes.Lq2emFoj/preservation.json) records the stricter comparison:

- **335 existing definition ASTs are unchanged** in implementation files.
- **24 changed boundary functions compare identically after only the enumerated path/guard/partial-open normalizations.** The normalization rules are recorded in [check_preservation.py](/tmp/pde-migration-fixes.Lq2emFoj/check_preservation.py); this is not a claim that those 24 full ASTs are unchanged.
- Moved raw `scientific_config` and configuration-hash assignments are individually exact-AST matched before/after. The side checks' moved reference loads and n8192 output-name expressions are also exact-AST matched.
- Every pre-existing module-level assignment in changed implementation files is exact-AST preserved. Scientific constants, point/cap declarations, seeds and algorithm settings are unchanged.
- **58 inventoried JSON/configuration/hash-list/shell files are byte-identical.** Stored expected hashes, source seals, unlocks, attempt allowances and budget settings were not renewed.
- The frozen shared helper is byte-identical before/after:
  `8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e`.

The before snapshot covers 232 selected files; the after snapshot covers 241, accounting for nine additions. Of the original files, 208 are unchanged and 24 changed. Inventory selection is scoped Python, shell, JSON, README/REPRODUCTION and SHA256-named files, excluding prior audit products, plus the shared helper for preservation only.

## Exact inventory and evidence hashes

[before.sha256](/tmp/pde-migration-fixes.Lq2emFoj/before.sha256) and [after.sha256](/tmp/pde-migration-fixes.Lq2emFoj/after.sha256) contain exact per-file hashes; original bytes are retained privately under `before/`.

| Artifact | SHA-256 |
|---|---|
| [before.sha256](/tmp/pde-migration-fixes.Lq2emFoj/before.sha256) | `1799dfa4cfc22c161b11b8c73a3e1001b52ce31b204a2b6a9a288640ae4b4a6c` |
| [after.sha256](/tmp/pde-migration-fixes.Lq2emFoj/after.sha256) | `fcf4eddd790efa30ab8e909e9eeb9a10b488b8bdcef4a2445e3563509587a72e` |
| [changes.patch](/tmp/pde-migration-fixes.Lq2emFoj/changes.patch) | `406619c23884531868d68141fc46fe058404372a57f13badda381f7687d2a599` |
| [preservation.json](/tmp/pde-migration-fixes.Lq2emFoj/preservation.json) | `5f4f640d5a50cb0da1fdf166aa40ffe5d7d7acee28e5867a4d0b25434fd60158` |
| [test-results.json](/tmp/pde-migration-fixes.Lq2emFoj/test-results.json) | `d375a6dde64d818ccff1e8365ef5f7002a095417c6f3838b5746c8030b07f635` |
| [fixture-hashes.json](/tmp/pde-migration-fixes.Lq2emFoj/fixture-hashes.json) | `2ea0920042ad429e175938f150c2c079eb76282277f7c48c3b075a5ae708703c` |

## Explicit limits and integration notes

- No commit, source-seal creation/reset, historical-data mutation or authorization/budget renewal occurred. Historical data contents were not needed for the tests.
- Existing frozen-source/hash refusals remain valid limitations. Changed live source bytes do not imply permission to update stored expected hashes.
- Raw PDE output identity still depends on unchanged quadrature/restart setup; its final-name collision check now runs immediately after that setup and before sample allocation/time stepping. Initial named-output-tree guards run before setup. No new identity/hash formula was invented to avoid that dependency.
- Raw/activation deterministic partials are intentionally preserved on failure and block retries; this slice does not authorize resetting them.
- Omitted `config_path` is now a deliberate callable error. The frozen-pilot CLI already supplies explicit config. Broad research tests were neither run nor expanded to bless the change.
- The side checks remain historical-only, with their original budgets/settings. No new fresh-run selection workflow was added.
- No guarantee about malicious concurrent filesystem mutation, numerical/scientific correctness, or full experiment reproducibility is made.
- All repository writes were restricted to the seven owned trees. The coordinator's disjoint integrated slices, shared helper and root metadata were not edited.

The implementation slice is complete. Further work should be the coordinator's bounded integration/fresh review, not expanded legacy investigation.
