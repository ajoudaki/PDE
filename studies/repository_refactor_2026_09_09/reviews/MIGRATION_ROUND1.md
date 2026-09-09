# Independent repository-migration audit

Verdict: **NEEDS FIXES — three path/interface defects remain. Preservation passes.**

Repository: `/home/amir/Codes/PDE`. Comparison: the live working tree against `4e6ff81`, including untracked migration helpers. Final scoped hash check: 2026-09-09 11:20:19 UTC. This is a repository-migration review, not a mathematical or core-algorithm review.

The 35 restored configurations and three historical seals are present and byte-exact. No loss of inventoried original source, retained data/backups, or recorded recovered payloads was found. Twenty-five selected repository regressions passed. These facts do not establish that every migrated study command has a coherent runnable interface.

## Required fixes

### F1 — P2: Generalization output relocation breaks its precheck and seal paths

[run_grid.py:27](/home/amir/Codes/PDE/studies/resnet_generalization/protocol/run_grid.py:27) now writes under `data/generated/resnet_generalization/results/generalization`. Its connected [pde_precheck.py:16](/home/amir/Codes/PDE/studies/resnet_generalization/pde_precheck.py:16) still reads `studies/resnet_generalization/results/generalization`. The runner invokes that precheck without supplying the new input root at lines 830–837.

The runner also still serializes evidence with `path.relative_to(ROOT)` at lines 577 and 987, and the numerical-decision path at line 1005. `ROOT` is the source study, so a file beneath the new generated root cannot be represented this way. Its seal reader at line 358 and numerical-decision reader at line 817 likewise resolve labels against the source root.

Independent reproduction used the actual imported constants and the exact relative-path operation on a synthetic pathname; it raised `ValueError` without creating a file. Writer and precheck roots demonstrably differ. See [generalization-path-regression.json](/tmp/pde-migration-independent-8YBF0QQe/generalization-path-regression.json).

Required fix: give the connected writer, precheck, seal serializer, and seal consumer a consistent evidence-root interface. Keep source labels distinct from evidence labels and pass the input root to the child precheck. Add tiny temporary-fixture checks for the reader/writer agreement and label round trip. Do not refresh the historical dynamics manifest to make this pass.

The current historical source freeze can reject this runner before execution. That expected rejection does not remove the independently demonstrated path inconsistency; no campaign was launched to reproduce it.

### F2 — P2: The symbolic cubic audit still reads three moved results from source

The changed [audit_symbolic_order5.py:25](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_symbolic_order5.py:25) fixes the quadratic source dependency but leaves these input bindings at their former source-side locations:

- `two_input_plus_gaussian_program/results_symbolic_order5.json`;
- `two_input_plus_gaussian_program/results_order3.json`;
- `depth2_gaussian_program/results_order9.json`.

All three are beneath `studies/mfp_cubic_compiler/` in the reader, are absent there, and are retained beneath `data/historical/studies/mfp_cubic_compiler/`. Their retained hashes match both the inventory and this audit's expected input digests.

Calling only `load_document()` raises `FileNotFoundError` immediately. This is an unrepaired migration path, not missing source/data, a missing dependency, or a deliberate frozen-source hash refusal. See `cubic_load_document` and `cubic_missing_inputs` in [probes.json](/tmp/pde-migration-independent-8YBF0QQe/probes.json).

Required fix: bind these three read-only inputs to their manifest destinations and test presence/hash resolution without compiling or reproducing the cubic program. Preserve expected hashes. Other source hashes can still fail afterward because migrated live sources differ from their historical freeze; that is a separate provenance issue.

### F3 — P2: Several changed writers still create outputs in the source tree

The explicit data contract requires fresh study outputs under `data/generated/<study>/...`. The following changed live files still use source-owned output paths:

| Writer | Concrete evidence |
|---|---|
| [run_fresh_calibrated_ratio.py:26](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_calibrated_ratio.py:26) | `OUT = HERE / "runs/fresh_calibrated_ratio_run"`; creates that directory and writes results there. |
| [run_fresh_order13_median.py:28](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_order13_median.py:28) | `OUT = HERE / "runs/fresh_order13_median_run"`; same source/data violation. |
| [jet_control_variate.py:22](/home/amir/Codes/PDE/studies/stieltjes_finite_width/jet_control_variate.py:22) | Historical input root was repaired, but NPZ/results output remains under `HERE/runs` (lines 178, 188, 219). |
| [run_h3_sine_regression.py:102](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_sine_regression.py:102) | Writes `H3_NORMALIZED_SINE_RAW.npz` beside the script. Its changed postprocessor reads the retained historical copy instead. |
| [run_h3_curvature_extension.py:121](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_curvature_extension.py:121) | Same split for the extension raw NPZ and its postprocessor. |
| [compare_independent.py:43](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/compiler/compare_independent.py:43) | Writes three coefficient-map JSON files and a comparison JSON beside source, while historical input maps were rebound to data. |

These are concrete writer/consumer interfaces, not objections to tracking essential configuration or provenance JSON. Ignoring `runs/` in Git does not physically separate outputs from source. The paired sine scripts can also leave a user postprocessing historical bytes instead of the newly generated file.

Required fix: expose explicit fresh output paths under generated data, and distinguish historical replay inputs from newly generated inputs in the connected readers. Where a command is intentionally archival only, make that restriction explicit at its entry point before any work or writes. Test routing with tiny synthetic files or path-only fixtures; do not run the original experiments.

No writer above was executed. This finding concerns incomplete migration acceptance, not an allegation that archived bytes were overwritten during this audit.

## Preservation and restoration evidence

The requested plan, move manifest, restoration manifest, verifier, and both migration-round reports were inspected as contract/evidence. Their reported PASS counts were not accepted as this audit's results. [contract-hashes.json](/tmp/pde-migration-independent-8YBF0QQe/contract-hashes.json) records the exact inspected bytes, including `INVENTORY_BEFORE.json`. The move manifest and original inventory also have no diff against `4e6ff81`.

The verifier was inspected before execution: it reads files/Git batch input, computes hashes, and emits JSON; it contains no repository write or seal-generation path. All 3,075 move destinations exist inside the repository, with zero duplicate origins or destinations. Its two removed aliases are recorded navigation symlinks; their underlying source is represented in the preserved inventory.

| Check | Independently observed result |
|---|---|
| Original source against safety snapshot `25dfbf2` | 2,575 files; 71,717,649 bytes; zero failures |
| Unchanged current original source | 2,396 files; 68,388,289 bytes |
| Changed current original source | 180 files, listed individually by the verifier; original bytes remain in the verified snapshot |
| Retained data | 836 files; 678,208,098 bytes; all size/SHA-256 checks pass |
| Retained backups | 41 files; 2,106,818 bytes; all checks pass |
| Recovered original/tar/checkpoint records | 272 files; 6,180,850 bytes; all checks pass |
| Restored source configurations | 35 files; all exact |
| Restored historical seals | 3 files; all exact |
| Combined restored metadata | 143,813 bytes; both original retained and restored copies checked |

The sole snapshot exception is the inventory tool's self-row, `studies/repository_refactor_2026_09_09/inventory.mjs` (3,278 inventoried bytes). This is an explicit tooling exception, not a waived pre-existing research file. All 2,576 original source rows remain present in the current filesystem; 2,396 unchanged plus 180 changed accounts for them.

For every restored row, this audit independently computed SHA-256 and length of both `from` and `to`, then joined the retained destination through the move manifest back to the original inventory row. All 38 joins and byte comparisons passed. [restored-hash-check.json](/tmp/pde-migration-independent-8YBF0QQe/restored-hash-check.json) contains every exact path, byte count, expected and observed digest, classification, and original inventory record.

Historical seal SHA-256 values:

| Restored seal | SHA-256 |
|---|---|
| `resnet_activation_controls/historical_seals/FROZEN_INPUTS.json` | `76887fc5f8774360c56080986c6bba57208992c34b3639941ffb6e6fe8e05ed2` |
| `resnet_proof_audit/historical_seals/FROZEN_INPUTS.json` | `c3c5a4779d4546d3704401929aa97bca79daf81876063a83fc84df075f485244` |
| `stieltjes_hybrid_campaign/historical_seals/FROZEN_PROTOCOL.json` | `33d167afe0bc4f8b936dd96259d0afe2c83afad63ffdddd19772ce76a56a6dfe` |

Full outputs: [snapshot-verification.json](/tmp/pde-migration-independent-8YBF0QQe/snapshot-verification.json), [filesystem-verification.json](/tmp/pde-migration-independent-8YBF0QQe/filesystem-verification.json).

These checks establish preservation relative to the repository's inventories and local safety snapshot. They do not authenticate inaccessible pre-recovery external originals; no outside recovery directories or prior private reports were opened.

## Historical authorization and expected failures

- Proof audit: all 23 original source labels resolve; 14 match frozen bytes and nine differ. Historical status returns `historical_only` and `current_execution_authorized: false`. The live generated seal is absent while the historical seal is present. Unsafe resolver labels were rejected. The separate freeze entry point was inspected and refuses when the historical seal exists.
- Activation controls: both requiring the live input seal and attempting the input-manifest creation helper refuse before any write. Evidence labels use the generated evidence root; an outside path is rejected.
- Stage V: the actual retained unlock fails the fresh-root binding check. Both recorded points, `v_n8192_h1e5` and `v_n8192_h5e6`, are rejected as already consumed before a writable ledger is opened. Only the inspected stdlib guard functions were extracted for this check; this is not a PyTorch module or GPU execution test.
- Breadth lock: all 23 entries now resolve, including the restored point configuration. Twenty match; three changed live source files do not. Expected hashes were not changed.
- The n8192 analyzer correctly refuses its transformed n4096 source: expected `731eeddbf362aebd89991a9dd83f8fe5db324ffc6764d9c44326d1df8fc34dd8`, observed `a4ed38e1bba7ca7ad1000031a337418b022eab7743fe773a7ec2a132d3c2d802`.
- No existing 64-hex digest literal was added, removed, or replaced in the inspected Python patch. The restored metadata and all 100 scoped Python files had no start/end hash drift.

No accidental reauthorization by the restored three seals was observed. This is not a blanket claim that every legacy freeze writer is safe to execute. In particular, [freeze_primary.py:92](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/primary/freeze_primary.py:92) still explicitly overwrites its original manifest/hash paths and asserts a pre-comparison freeze. This pre-existing writer currently encounters moved artifact inputs before that point; it was not executed. It must remain excluded from migration replay, or gain an existing-seal refusal and a separately reviewed new-output interface before being presented as supported fresh tooling. Missing historical inputs must never be “fixed” by running a re-freezer over a claimed lock.

The unchanged frozen labels in retained manifests are evidence. The changed literal path expectations in `test_production_hidden_recurrence.py` do not match those retained labels; the source-byte assertion already fails first. Those historical provenance tests were not run or made to pass, and no archived metadata was rewritten.

## Tests and execution limits

All selected test execution used Python `-B`, bytecode suppression, one BLAS/OpenMP/MKL thread, a private `TMPDIR`, and 45-second per-process limits. Inspected repository test code ran under an additional Python audit hook rejecting writes outside this private directory and child execution. Synthetic fixture writes stayed private.

| Selected repository checks | Passed |
|---|---:|
| `studies.resnet_proof_audit.tests.test_verify_study` | 4 |
| `studies.resnet_proof_audit.tests.test_run_protocol` | 13 |
| `test_analyze_results.DiscoveryAndMissingStageTests` | 4 |
| `test_trapezoid_compat` | 1 |
| `compiler.test_finite_width_jet.test_generic_oracle_matches_quadratic_reference_seedwise` | 1 |
| `order5.finite_width.test_order5.test_generic_quadratic_matches_accepted_finite_width_compiler` | 1 |
| `order5.finite_width.test_order5.test_quadratic_exact_frozen_large_width_endpoint` | 1 |
| **Total distinct repository tests** | **25** |

The last three are within `studies.mfp_gaussian_calculus`; they exercise repaired imports and one retained frozen-data path, without a new experiment. Exact commands and test names are in [verifier-tests.json](/tmp/pde-migration-independent-8YBF0QQe/verifier-tests.json), [protocol-tests.json](/tmp/pde-migration-independent-8YBF0QQe/protocol-tests.json), [discovery-tests.json](/tmp/pde-migration-independent-8YBF0QQe/discovery-tests.json), and the private `probes.py`/`probes.json`.

The established library's read-only structural checker passed on 19 files. This checks local links/import declarations and does not verify mathematics or substitute for an isolated established-library test run. Core implementation tests and mathematical claims remain with the parent review.

Independent static checks parsed the 100 scoped Python files and resolved 403 top-level path expressions without executing source bodies. This is a candidate scan, not complete dynamic path coverage. Connected code was inspected where necessary, notably generalization precheck/seal consumers and the n8192 transformation guard.

Environment: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. PyTorch, SymPy, mpmath, pytest, and Matplotlib are absent. Normal proxy import was attempted and fails for missing SymPy; it is recorded as an environment gap, not a successful import or migration defect. No dependencies were installed.

No campaigns, unfiltered discovery, new scientific experiments, C++/GPU/TeX builds, seal regeneration, Git mutation commands, repository edits, other-agent calls, conversation-history queries, or web access were performed. No prior private audit artifacts were consulted. Initial filename-only instruction discovery briefly included the parent `/home/amir/Codes` and returned two unrelated AGENTS.md filenames; neither file was opened or used. All substantive research/code/data inspection stayed in PDE.

Private harness issues are recorded separately: the first write guard rejected stdlib CPU/platform probes and fd-relative temporary cleanup; the harness was corrected and the selected tests rerun successfully. An initial Node child-process capture stalled/returned empty output; it was stopped, and the verifier's documented shell pipeline produced the recorded successful checks. These were audit-harness failures, not repository test failures.

## Exact reviewed Python scope

Ninety-eight files occur in the diff against `4e6ff81`; two additional untracked files are `source/migration_paths.py` and `tests/test_trapezoid_compat.py` beneath `resnet_proof_audit`. The patch is [python-path-diff.patch](/tmp/pde-migration-independent-8YBF0QQe/python-path-diff.patch). Exact initial/final SHA-256 and sizes are in [source-hashes-start.json](/tmp/pde-migration-independent-8YBF0QQe/source-hashes-start.json) and [source-hashes-end.json](/tmp/pde-migration-independent-8YBF0QQe/source-hashes-end.json); [final-checks.json](/tmp/pde-migration-independent-8YBF0QQe/final-checks.json) records zero scoped drift.

Paths below are relative to `/home/amir/Codes/PDE`. Review concerned imports, root calculations, read/write destinations, and historical authorization; it did not audit their mathematical bodies.

- `studies/mfp_cubic_compiler/depth2_gaussian_program/depth2_cubic_stieltjes_audit.py`
- `studies/mfp_cubic_compiler/depth2_gaussian_program/test_depth2_cubic_exact_jet.py`
- `studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_symbolic_order5.py`
- `studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_two_input_cubic_plus.py`
- `studies/mfp_cubic_compiler/two_input_plus_gaussian_program/test_two_input_cubic_plus.py`
- `studies/mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_plus_fixed_rho_jet.py`
- `studies/mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_stieltjes_order5.py`
- `studies/mfp_gaussian_calculus/compiler/test_finite_width_jet.py`
- `studies/mfp_gaussian_calculus/depth_order5/primary/freeze_primary.py`
- `studies/mfp_gaussian_calculus/depth_order5/primary/generate_frozen_artifacts.py`
- `studies/mfp_gaussian_calculus/depth_order5/primary/test_depth_population_jet.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/hostile_gamma04_derivation.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/hostile_gamma04_derivation_v2.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_curvature_extension.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_sine_regression.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_curvature_extension.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_sine_regression.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_hostile_checks.py`
- `studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/independent_route_a/run_sine_regression.py`
- `studies/mfp_gaussian_calculus/order5/audit_hostile.py`
- `studies/mfp_gaussian_calculus/order5/compiler/compare_independent.py`
- `studies/mfp_gaussian_calculus/order5/finite_width/test_order5.py`
- `studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py`
- `studies/mfp_identity_compiler/linear_gaussian_program/identity_order13_stieltjes_audit.py`
- `studies/mfp_identity_compiler/linear_gaussian_program/identity_stieltjes_audit.py`
- `studies/mfp_linear_growth_uniform_counterexample/bump_laurent_certificate.py`
- `studies/mfp_linear_growth_uniform_counterexample/evaluate_full_l2_transition.py`
- `studies/mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py`
- `studies/mfp_program_history/report/build_report.py`
- `studies/mfp_quadratic_compiler/campaign1/test_hankel_analysis.py`
- `studies/mfp_quadratic_compiler/campaign1/test_order9_q2_order8.py`
- `studies/mfp_quadratic_compiler/campaign4/make_provenance.py`
- `studies/mfp_quadratic_compiler/campaign4/test_results_and_certificates.py`
- `studies/mfp_quadratic_compiler/campaign5_b3/postprocess_lower_moments.py`
- `studies/mfp_quadratic_compiler/campaign5_b3/test_b2_order5_gate.py`
- `studies/mfp_quadratic_compiler/campaign5_b3/test_stage_c_sector.py`
- `studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py`
- `studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_order13_stieltjes_audit.py`
- `studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_stieltjes_audit.py`
- `studies/mfp_quadratic_compiler/depth3_gaussian_program/test_depth3_order13_stieltjes.py`
- `studies/mfp_quadratic_l2_order5/audit_direct.py`
- `studies/mfp_quadratic_l2_order5/audit_quadratic_euler_jet.py`
- `studies/mfp_quadratic_l2_order5/quadratic_exact.py`
- `studies/mfp_sine_compiler/depth2_gaussian_program/normalized_sine_order5.py`
- `studies/mfp_sine_compiler/depth2_gaussian_program/raw_sine_order5.py`
- `studies/mfp_sine_compiler/depth2_gaussian_program/sine_order9_stieltjes_audit.py`
- `studies/mfp_sine_compiler/depth2_gaussian_program/test_sine_order5.py`
- `studies/repository_refactor_2026_09_09/source_audits/migration_crosscheck.py`
- `studies/resnet_activation_controls/analyze_activation.py`
- `studies/resnet_activation_controls/run_experiment.py`
- `studies/resnet_bridgeability/targeted_bridge_test.py`
- `studies/resnet_generalization/protocol/run_grid.py`
- `studies/resnet_proof_audit/protocol/freeze_study.py`
- `studies/resnet_proof_audit/protocol/verify_study.py`
- `studies/resnet_proof_audit/source/analyze_results.py`
- `studies/resnet_proof_audit/source/cross_p.py`
- `studies/resnet_proof_audit/source/dense_gates.py`
- `studies/resnet_proof_audit/source/pde_tangent.py`
- `studies/resnet_proof_audit/source/run_protocol.py`
- `studies/resnet_proof_audit/source/run_study.py`
- `studies/resnet_proof_audit/source/structural_runner.py`
- `studies/resnet_scalar_stress/one_input_hermite_ladder.py`
- `studies/resnet_tail_compactness/coupled_cauchy_ledger.py`
- `studies/resnet_tail_compactness/targeted_tail_commutator.py`
- `studies/stieltjes_finite_width/jet_control_variate.py`
- `studies/stieltjes_finite_width/run_fresh_calibrated_ratio.py`
- `studies/stieltjes_finite_width/run_fresh_order13_median.py`
- `studies/stieltjes_finite_width/run_positive_time_pair_median.py`
- `studies/stieltjes_hybrid_campaign/bounded_dmft/truncated_mfp_reference.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/adjudicate_local_qualification.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/run_local_qualification.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/tests/test_fp64_local.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/watchdog_launcher.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/one_input/tests/test_one_input_engine.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/proxy_contract.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/run_block.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/compare_with_n4096.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/run_block.py`
- `studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py`
- `studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/analyze_stage_v.py`
- `studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py`
- `studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/tests/test_euler_fp32.py`
- `studies/stieltjes_hybrid_campaign/width_ladder/width_engine.py`
- `studies/stieltjes_proxy_campaign/proxy/inventory.py`
- `studies/stieltjes_proxy_campaign/proxy/run_frozen_boundary.py`
- `studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n4096.py`
- `studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py`
- `studies/stieltjes_resolution/block_metric_counterexample.py`
- `studies/stieltjes_resolution/block_metric_positive_alpha_jet.py`
- `studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py`
- `studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_recurrence.py`
- `studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_scalar_audit.py`
- `studies/stieltjes_resolution/canonical_hidden_high_order/production_hidden_recurrence.py`
- `studies/stieltjes_resolution/canonical_hidden_high_order/test_independent_hidden_recurrence.py`
- `studies/stieltjes_resolution/canonical_hidden_high_order/test_production_hidden_recurrence.py`
- `studies/stieltjes_resolution/canonical_high_order/test_independent_canonical_recurrence.py`
- `studies/stieltjes_resolution/canonical_high_order/test_production_canonical_recurrence.py`
- `studies/resnet_proof_audit/source/migration_paths.py`
- `studies/resnet_proof_audit/tests/test_trapezoid_compat.py`

The report and diagnostics are confined to the new mode-0700 directory `/tmp/pde-migration-independent-8YBF0QQe`. No fix has been applied to the repository.

