# Isolated migration-interface acceptance — NOT CLEAN

Date: 2026-09-09. Snapshot: the seven current study directories, shared output-path helper, and root ignore file named in the request. This is a migration/output-boundary acceptance, not a scientific review.

## Result

NOT CLEAN. The 11 inspected bounded suites pass all 62 tests, but independent private diagnostics expose additional routing, named-output, own-input, early-refusal, and callable attempt-state defects.

No source or data edits were made. All audit-created files and sentinel mutations were confined to the new private directory `/tmp/pde-migration-acceptance.EdK0cKSV`. No live workflow was disabled. No historical authorization, frozen hash, attempt allowance, or budget was refreshed.

## Concrete blockers

### F1. Two finite-width entry points reference an undefined migrated path

[Order-13 main](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_order13_median.py:126) and [calibrated-ratio main](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_calibrated_ratio.py:135) use `PEELING / "finite_width_jet_reference.py"`; their current module-level path is named `MFP_COMPILER`.

Both complete `main()` functions were exercised with coefficient/target work and resource changes mocked. Each raised `NameError: name 'PEELING' is not defined`, after creating its output directory and attempting its memory-limit step, before the scientific worker. This is a current source-path error, not an expected freeze refusal. The referenced compiler study is outside scope and was not read.

Evidence: the two `undefined_migrated_path` records in [diagnostic-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/diagnostic-results.json).

### F2. Named output destinations do not consistently receive alias guards

These are tests of the program's named outputs, not complaints about an arbitrary caller choosing an inappropriate output location. All aliases were fixed before the call; no concurrent mutation or filesystem-security guarantee is asserted.

- **Direct Loewner corrected-clock runner:** [main](/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/run_corrected_clock_test.py:304) makes the fixed generated output directory and opens its `run.log` through [log_factory](/home/amir/Codes/PDE/studies/stieltjes_direct_loewner/run_corrected_clock_test.py:49) in truncating mode, without the shared guard. The complete main was stopped before science by a mocked environment-description call. A pre-existing log hardlink, log symlink, or output-directory alias changed a private retained-input sentinel.
- **Proof-audit processed writer:** [write_processed](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/analyze_results.py:6849) rejects only destinations resolving under historical data. In a private replica of the repository layout, the normal generated `historical_review/processed` directory aliased to the study's source directory; the actual callable replaced a source sentinel. [_atomic_write](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/analyze_results.py:6280) uses an exclusive temporary file and replacement, which protects a leaf's other hardlinks from truncation, but does not repair this directory-boundary hole.
- **Hybrid breadth validation outputs:** [write_outputs](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:751) directly writes the fixed generated `VALIDATION_RESULT.json` and `RESULTS.md`. Its actual callable changed a private retained-input sentinel hardlinked to the named JSON output.
- **Proxy GD/RK4 side-check outputs:** the fixed writers in [n4096](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n4096.py:276) and [n8192](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py:218) directly write JSON without the named-output guard. Their actual publication statements changed private reference-input sentinels hardlinked to those outputs. Their scientific bodies were not executed.

Evidence: `corrected_clock_log_alias` in [diagnostic-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/diagnostic-results.json); `proof_named_output_directory_alias`, `hybrid_named_validation_output_hardlink`, and both `proxy_named_sidecheck_output_hardlink` records in [additional-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/additional-results.json).

### F3. Both raw exact-reference writers can replace their own selected PDE-seal input

The complete raw `run()` functions read the explicitly selected `--pde-seal`, include its content hash in the output identity, and later replace the final destination without comparing that destination to the input:

- [Generalization run](/home/amir/Codes/PDE/studies/resnet_generalization/run_exact_reference.py:100): exclusive partial at line 256, unqualified final replacement at line 275.
- [Activation run](/home/amir/Codes/PDE/studies/resnet_activation_controls/source/run_exact_reference.py:100): truncating partial at line 249, final replacement at line 267.

A private diagnostic ran each actual function with all numerical operations and the seed worker mocked. It first obtained the actual configuration-derived output name, then renamed an unchanged inert JSON input to that final name and selected it as `--pde-seal`. Because identity depends on the input's bytes, not its pathname, the second call selected the same output name and replaced its own input. No real seal was produced or authorized.

Activation also overwrote the same input when placed at its deterministic partial name; replacement then removed that input pathname. Generalization's exclusive partial correctly raised `FileExistsError` in the partial-name positive-control case, preserving the input, but did not protect the final-name case.

Evidence: all four records, with exact input before/after hashes, in [exact-input-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/exact-input-results.json). These are full-function mocked boundary executions, not numerical runs.

### F4. Activation restart and intermediate publication paths remain unsafe

[Activation PDE publication](/home/amir/Codes/PDE/studies/resnet_activation_controls/source/run_pde.py:375) opens its deterministic partial with `wb` and replaces the final path at line 396 without the generalization runner's explicit restart-input overlap check. The shared directory guard does not detect an ordinary single-link file whose pathname is also the selected input. Actual publication statements overwrote private final-name and partial-name restart sentinels. This diagnostic covered publication only; it did not load a real restart or execute a PDE trajectory.

[Activation _atomic_text](/home/amir/Codes/PDE/studies/resnet_activation_controls/analyze_activation.py:1103) similarly opens its deterministic partial with `w`. The complete callable overwrote an existing ordinary partial, and followed pre-existing partial hardlink/symlink aliases to a private input. The full analyzer's real frozen-map checks were not bypassed: the proved result is the intermediate-writer boundary, not successful execution of a frozen analysis.

Evidence: `activation_raw_restart_overlap` and `activation_analysis_intermediate` in [diagnostic-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/diagnostic-results.json).

### F5. Width analysis can destroy one of its own five selected inputs

[width_analysis.main](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/width_analysis.py:870) accepts five explicit input archives, reads them, and directly writes `--output` at line 920 without comparing it to those inputs.

The complete main, with ingestion restricted to private sentinel bytes and all analysis mocked, returned success after overwriting the selected `--n2048` input. Same-path, lexical-alias, symlink, and hardlink variants all reproduced the issue. All five selected inputs were read; no resampling or reanalysis occurred. This is an own-input collision, not a finding against freely chosen output directories.

Evidence: four `width_analysis_own_input_alias` records in [diagnostic-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/diagnostic-results.json).

### F6. Proxy n8192 side-check detects a missing reference only after the worker call

[n8192 main](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py:107) initializes CUDA and calls the point worker at line 149 before opening its required reference at line 156. Unlike the n4096 counterpart, it has no missing-reference preflight. Its selected wall cap is 600 or 1200 seconds.

The complete main with a fully mocked torch/engine environment reached the worker with the private reference path absent. The worker mock stopped immediately: no CUDA initialization or computation actually ran. This establishes failure ordering, not measured wasted runtime or the presence/absence of a real historical archive.

Evidence: `proxy_missing_reference_late_check` in [diagnostic-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/diagnostic-results.json).

### F7. Archive-only attempt mutation callables omit the current-authorization refusal

The six FP64-related CLI mains, reservation callable, and external failure-finalization callable correctly refuse through the archive-only guard. However, [claim_canonical_attempt](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/run_local_qualification.py:525) and [finish_canonical_attempt](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/run_local_qualification.py:570) omit that guard.

On a wholly synthetic private ledger with matching fixture provenance and a fixture watchdog token, the actual callables changed reserved → running → failed and recalculated consumed GPU seconds and the stage-budget flag; the current-authorization guard was never called. The claim callable also opens its lock before validating the supplied reservation. Finish accepts the supplied update mapping after checking only that the record is running.

This is narrowly a state-mutating callable boundary gap. No actual historical ledger was inspected or modified, no real terminal attempt was shown eligible, and no live runner/hash gate was bypassed. It does not establish that a current CLI can restart an archived campaign.

Evidence: `archive_only_callable_ledger_mutators`, including all three exact ledger hashes, in [additional-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/additional-results.json).

## Additional routing discrepancies and optional improvements

These are separated from the directly demonstrated blockers above.

1. **Activation seal routing is internally inconsistent, behind the existing freeze limit.** [_evidence_relative](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py:103) labels files relative to `RESULTS.parent`, giving `results/pde/input.npz` under the generated study root. [_require_seal_common](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py:828) instead resolves that label as `ROOT / relative` at line 852, under the source study. The analyzer uses the generated evidence root. A private in-memory metadata fixture confirmed the producer/consumer disagreement without creating a seal. Only the input-manifest dependency was mocked to isolate path resolution. The real freeze remains an explicit accepted limit; this is not a request to refresh it, nor a claim that the full current gated workflow runs.
2. **Proxy callable's optional config inference is stale.** [load_reference_run](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/reference_data.py:118) still infers `reference/configs/<name>` beside the run hierarchy when `config_path` is omitted. With the producer's generated run layout, this points into generated data rather than current source configs. A private summary with zero points failed there; supplying the current source config explicitly succeeded. The documented explicit-summary/config workflow remains available. Making the callable require that explicit argument, or providing a deliberate source-config mapping, is an optional interface cleanup relative to that documented workflow.
3. **Both proxy GD/RK4 side checks are historical-only consumers.** They hardwire historical reference paths and have no fresh-input selector; the main reference producer writes generated runs. This is not an implicit fallback and was not treated as historical authorization. An explicit fresh/historical selector would improve live producer-consumer usability without retiring those useful checks. Independently, their writer and late-input-check defects remain F2/F6.
4. Add bounded regression coverage for the reproduced holes while preserving the working live validation/raw workflows. No expansion to scientific tests or renewal of frozen authorization is needed to demonstrate the boundary failures.

## Routing, early refusal, and failure-path checks that passed

- The shared [StudyPaths helper](/home/amir/Codes/PDE/studies/_output_paths.py) and inspected adapters distinguish current generated outputs from source/historical data, reject pre-existing symlink/multiple-link output trees, and do not create directories when refusing. Their scope is ordinary pre-existing path aliases, not hostile concurrent filesystems.
- Generalization's grid, precheck, and verifier agree on generated `results/generalization`; evidence labels round-trip through that selected evidence root. The precheck child receives its actual input root. Historical selection is explicit and routes review output back to generated data.
- Proof-audit discovery distinguishes generated evidence from explicit historical review. Historical interpretation does not constitute execution authorization. Its processed writer still has F2.
- Activation raw defaults and figure input/output roots are migrated. Figure historical selection is explicit. Raw/intermediate issues and the separate seal-label discrepancy are described above.
- Finite-width fresh pair output matches the positive-time consumer; corrected-clock output matches the jet consumer. Input-directory/historical selection is explicit, with no automatic historical fallback. The two other finite-width mains still have F1.
- Hybrid successive consumers forward the selected array and manifest roots. Explicit historical selection uses historical arrays and the retained current-source manifests. The n8192 frozen analyzer-transform mismatch still refuses before work/output creation, including the comparison entry point; its expected hash was not changed.
- The six legacy FP64 main guards, reservation, and external failure-finalization refusal checks pass. Stage-V output tests cover named point restrictions, authorization/digest checks, and timeout-finalization constraints; current frozen/consumed identities were not reset. The inspected watchdog shell retains its 65/125-second wrapper limits around 60/120-second work limits. No watchdog or timeout campaign was run. F7 concerns the other two mutation callables only.
- Proxy frozen-pilot output validation runs before work and its success/failure publications refuse existing final and partial paths. Its frozen source-binding refusal is retained. Reference producer and shard/single/merge destinations were traced; the guarded shard/merge interfaces preserve new-output constraints.
- The root [.gitignore](/home/amir/Codes/PDE/.gitignore) ignores generated/data artifacts; ignore rules themselves are not treated as write protection.
- Existing source/hash/unlock/budget refusals are accepted limits. No finding asks that a stored expected hash, seal, authorization, or budget be renewed merely to make migrated code execute.

## Executed bounded suites

Each suite was read before execution and run in an isolated child, with bytecode disabled, private temporary/cache destinations, and a 45-second child timeout. No broad test discovery was used.

| Inspected suite | Tests | Result |
|---|---:|---|
| [resnet_generalization/tests/test_migration_paths.py](/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_migration_paths.py) | 7 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-00.log) |
| [resnet_generalization/tests/test_output_boundaries.py](/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_output_boundaries.py) | 7 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-01.log) |
| [resnet_generalization/tests/test_writer_boundaries.py](/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_writer_boundaries.py) | 6 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-02.log) |
| [resnet_proof_audit/tests/test_trapezoid_compat.py](/home/amir/Codes/PDE/studies/resnet_proof_audit/tests/test_trapezoid_compat.py) | 1 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-03.log) |
| [stieltjes_finite_width/test_migration_paths.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/test_migration_paths.py) | 5 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-04.log) |
| [stieltjes_finite_width/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/test_output_boundaries.py) | 3 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-05.log) |
| [stieltjes_finite_width/test_shared_output_paths.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/test_shared_output_paths.py) | 6 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-06.log) |
| [stieltjes_hybrid_campaign/breadth_panel/test_migration_paths.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/test_migration_paths.py) | 9 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-07.log) |
| [stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/test_output_boundaries.py) | 4 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-08.log) |
| [stieltjes_hybrid_campaign/width_ladder/euler_fp32/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/test_output_boundaries.py) | 6 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-09.log) |
| [stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/analysis/tests/test_output_boundaries.py) | 8 | [PASS log](/tmp/pde-migration-acceptance.EdK0cKSV/suite-10.log) |

Total: **62 passed, 0 failed**. These are interface/boundary/compatibility tests, not research validation. Tiny private NumPy fixtures in the allowed suites were permitted; the additional independent diagnostics used standard-library AST/mocks and inert bytes.

## Exact before/after input hashes

The baseline and final inventories contain the same **233 current files**, in the same order, with every per-file SHA-256 identical:

- [Before: exact per-file hashes](/tmp/pde-migration-acceptance.EdK0cKSV/inputs-before.sha256)
- [After: exact per-file hashes](/tmp/pde-migration-acceptance.EdK0cKSV/inputs-after.sha256)

SHA-256 of the entire before manifest: `6e23ec13a6ab131dfed30889d034d1744c16436d036ca1134bcdec4629f24ea3`.

SHA-256 of the entire after manifest: `6e23ec13a6ab131dfed30889d034d1744c16436d036ca1134bcdec4629f24ea3`.

Inventory selection: all scoped Python, shell, JSON, README.md, REPRODUCTION.md, and filenames matching `*SHA256*`, excluding `audits/` and `stage0_contact_audit.json`, plus the shared helper and root ignore file. The full manifest is the exact coverage definition, not a claim to hash every document or every historical data file.

Counts: `resnet_activation_controls`: 19; `resnet_generalization`: 41; `resnet_proof_audit`: 24; `stieltjes_direct_loewner`: 6; `stieltjes_finite_width`: 11; `stieltjes_hybrid_campaign`: 67; `stieltjes_proxy_campaign`: 63; `shared helper / root ignore`: 2.

Exact before/after sentinel and synthetic-ledger hashes are recorded separately in the three diagnostic JSON files. Those intentionally changed private fixtures are not the frozen workspace inputs or historical evidence.

Diagnostic-record file SHA-256 values:

| Record file | SHA-256 |
|---|---|
| [diagnostic-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/diagnostic-results.json) | `4ff04abf98c3bfbef982eee4bda827166f537738a9b69c24a0c235644cd8c7c6` |
| [exact-input-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/exact-input-results.json) | `42a3a5d5ffa87c463bfa846d7bf3b5fd835322822aa44dda641951cc2fb732c6` |
| [additional-results.json](/tmp/pde-migration-acceptance.EdK0cKSV/additional-results.json) | `ed03739502549122c3681f602b9ce4bebf6adea6c2ab01f12369851768181055` |

## Scope and limits

Only the current seven-study scope, shared helper, and root ignore file supplied repository guidance. No prior report/review/audit, task/chat history, or other study source was used. README/REPRODUCTION material was used for current commands and limits, not mathematical conclusions. Historical array contents and real historical ledgers/seals were not needed or opened for these diagnostics.

Complete relevant interface functions were read; AST extraction was used for isolated callables or publication blocks where importing or running the full module could trigger prohibited scientific dependencies. Each finding says whether the complete callable or only its publication block was exercised. Mock results do not establish full-runtime availability.

No trajectories, coefficients, reanalysis, broad research tests, native compilation, installation, training/GPU work, real seal creation/reset, or historical mutation was performed. References to out-of-scope compiler/engine study sources were traced as paths only. No scientific correctness, numerical accuracy, reproducibility, successful scientific rerun, or malicious/concurrent-filesystem security claim is made.
