# Bounded flat-study path repair handoff

Repository: `/home/amir/Codes/PDE`. Date: 2026-09-09.
Worker scope: live study Python/shell bindings and private temporary diagnostics only.
Read: `/tmp/refactor-code-audit-Cokj1yaG/RECOMMENDATION.md`, `FOUNDATION_HANDOFF.md`, and the move/navigation manifests.

## Result

Changed **78 live Python files; zero shell files**. Restored the **83 previously passing checks** at the new locations. An additional **27 existing checks were attempted: 26 passed, one errored because NumPy 1.26.4 lacks `np.trapezoid`**. Therefore the existing-check total for this worker is **109 passed, one environment error**, not an all-study validation.

Additional private probes: **nine exact inventory families evaluated successfully** and **seven affected imports succeeded**. Normal proxy-package import and the centered-quadratic import chain were blocked by missing SymPy. The isolated inventory probe loads the actual inventory and exact-series code in a private namespace, bypassing only the package initializer's optional SymPy hierarchy imports; it does not count as a successful normal package import.

No Git command/write, dependency installation, C++ compilation, GPU invocation, unfiltered repository test discovery, production experiment, frozen-manifest regeneration, or immutable payload modification was performed. No changes to `docs/`, `code/`, `data/`, study README/index files, scientific formulas, or literal frozen hash values. The source snapshot contains 556 live Python files and nine shell files; all 556 parse/compile in memory and all nine shells pass syntax-only checking.

## Repairs

- Quadratic independent-reference bindings in the base and order-five Gaussian tests, with the frozen order-seven JSON bound to its exact historical-data destination.
- Residual proof-audit/bridge/tail/scalar consumers bound to the existing activation-control implementation. The generalization, residual core, and activation-control implementations remain distinct.
- Proxy inventory repository depth repaired. Generated campaign results use `data/historical/studies/mfp_quadratic_compiler`; retained certificate JSON and theory source use their manifest-designated source locations. All nine families now evaluate with real inputs.
- Hybrid proxy/width-ladder, finite-width/direct-Loewner, cubic/sine/identity/quadratic, and order-five cross-study imports and ancestor calculations repaired.
- Selected historical input readers rebound explicitly. Output destinations were not redirected into immutable historical data.
- Broken generated reproduction-command paths corrected. Frozen labels and frozen expected hashes were retained.

## Existing checks and commands

Each baseline suite ran in a separate process with a 45-second timeout, `python -B`, bytecode disabled, and one BLAS/OpenMP/MKL/NumExpr thread. Runtime temporary outputs were directed into this private directory.

| Suite at new location | Passed |
|---|---:|
| `studies.mfp_gaussian_calculus.compiler.run_checks` | 12 |
| `studies.mfp_gaussian_calculus.b2.run_checks` | 12 |
| `studies/resnet_operator_core/tests` | 12 |
| `studies/resnet_generalization/tests/test_generalization_core.py` | 7 |
| Generalization dense/Galerkin/structural controls | 15 |
| `studies/mfp_finite_step_single_hidden_mlp` | 10 |
| `studies.rcgc_compiler.test_rcgc_compiler` | 6 |
| `studies/stieltjes_resolution/test_alpha_interval_tools.py` | 4 |
| `studies.mfp_gaussian_calculus.depth.test_exact_depth_program` | 5 |
| **Original bounded baseline** | **83** |
| `resnet_proof_audit/tests/test_dense_gates.py` | 6 |
| `resnet_proof_audit/tests/test_cross_p.py` | 8 |
| `resnet_proof_audit/tests/test_pde_tangent.py` | 10, plus 1 error |
| Selected order-five finite-width independent compiler/frozen endpoint checks | 2 |

The tangent error is `StabilityInfrastructureTests.test_stage5_helper_returns_archive_ready_finite_arrays`, at `source/pde_tangent.py:1744`: `AttributeError: module 'numpy' has no attribute 'trapezoid'`. No mathematical/API compatibility change was made to conceal it.

Reproduce the exact original 83:
```sh
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /tmp/flat-study-path-repair-OE9KpPVL/baseline.py
```

All explicit commands, process results, timings, and captured outputs are in [baseline-results.json](/tmp/flat-study-path-repair-OE9KpPVL/baseline-results.json) and [targeted-results.json](/tmp/flat-study-path-repair-OE9KpPVL/targeted-results.json). Follow-up inventory/import receipts are in [supplemental-results.json](/tmp/flat-study-path-repair-OE9KpPVL/supplemental-results.json).

## Environment and skipped work

Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0. Missing: pytest, PyTorch, Matplotlib, SymPy, mpmath. This is not a reproduction of the pinned modern dependency environment.

Skipped: PyTorch/GPU campaigns; pytest-dependent collection; Matplotlib-dependent long-horizon suite; SymPy/mpmath suites; C++-building tests; large exact/Wick/Monte Carlo programs; runners that create configs, mutate run directories, delete artifacts, or regenerate scientific seals. No replacements/stubs were installed to manufacture passing tests.

Source-byte changes necessarily invalidate any historical seal that hashes the old live source bytes. Expected hash literals and stored manifests were not regenerated. A relocation repair is not a refreshed scientific freeze.

## Missing data and remaining bounded-work boundaries

**No data was missing from the nine checked inventory families.** The 27 unique complete historical input paths directly represented as literals in the changed files also exist and match manifest byte sizes. Other assembled input paths are covered only by the targeted checks or source inspection, not by a complete data inventory.

The scan below records **26 remaining top-level path candidates** whose source-side location is absent but whose historical destination exists. It is a diagnostic list, not 26 confirmed runnable failures: it includes output files and mutable ledgers. These are mainly frozen orchestration/configuration readers and output/input mixtures outside the 83-check baseline. They were not blanket-rebound into historical storage: a writer or provenance guard can use the same root as a reader. Runtime frozen-label resolvers and embedded old paths in frozen manifests still need a separate provenance-aware replay decision. This bounded handoff does **not** claim every live runner or all historical studies are repaired/validated.

- [studies/resnet_proof_audit/source/run_protocol.py:28](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/run_protocol.py:28): `PROTOCOL_PATH`; retained destination `data/historical/studies/resnet_proof_audit/protocol/preregistered_protocol.json`.
- [studies/resnet_proof_audit/source/run_protocol.py:29](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/run_protocol.py:29): `FREEZE_PATH`; retained destination `data/historical/studies/resnet_proof_audit/results/seals/FROZEN_INPUTS.json`.
- [studies/resnet_proof_audit/source/analyze_results.py:39](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/analyze_results.py:39): `PROTOCOL_PATH`; retained destination `data/historical/studies/resnet_proof_audit/protocol/preregistered_protocol.json`.
- [studies/resnet_proof_audit/source/analyze_results.py:40](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/analyze_results.py:40): `FROZEN_INPUTS_PATH`; retained destination `data/historical/studies/resnet_proof_audit/results/seals/FROZEN_INPUTS.json`.
- [studies/resnet_proof_audit/source/run_study.py:32](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/run_study.py:32): `PROTOCOL_PATH`; retained destination `data/historical/studies/resnet_proof_audit/protocol/preregistered_protocol.json`.
- [studies/resnet_proof_audit/source/run_study.py:33](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/run_study.py:33): `FROZEN_INPUTS_PATH`; retained destination `data/historical/studies/resnet_proof_audit/results/seals/FROZEN_INPUTS.json`.
- [studies/resnet_proof_audit/protocol/freeze_study.py:20](/home/amir/Codes/PDE/studies/resnet_proof_audit/protocol/freeze_study.py:20): `PROTOCOL`; retained destination `data/historical/studies/resnet_proof_audit/protocol/preregistered_protocol.json`.
- [studies/resnet_proof_audit/protocol/freeze_study.py:21](/home/amir/Codes/PDE/studies/resnet_proof_audit/protocol/freeze_study.py:21): `SEAL`; retained destination `data/historical/studies/resnet_proof_audit/results/seals/FROZEN_INPUTS.json`.
- [studies/resnet_proof_audit/protocol/verify_study.py:20](/home/amir/Codes/PDE/studies/resnet_proof_audit/protocol/verify_study.py:20): `SEAL`; retained destination `data/historical/studies/resnet_proof_audit/results/seals/FROZEN_INPUTS.json`.
- [studies/stieltjes_proxy_campaign/proxy/run_frozen_boundary.py:18](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/proxy/run_frozen_boundary.py:18): `OUTPUT`; retained destination `data/historical/studies/stieltjes_proxy_campaign/boundary_result.json`.
- [studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py:33](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py:33): `REFERENCE_NPZ`; retained destination `data/historical/studies/stieltjes_proxy_campaign/reference/runs/canonical_n8192_r8_fp32_holdout_20260814/canonical_physical_n8192_r8_fp32_holdout.npz`.
- [studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n4096.py:41](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n4096.py:41): `REFERENCE_NPZ`; retained destination `data/historical/studies/stieltjes_proxy_campaign/reference/runs/canonical_n4096_r8_fp32_cast_control_20260814/canonical_physical_n4096_r8_fp32_cast_control.npz`.
- [studies/resnet_generalization/protocol/run_grid.py:26](/home/amir/Codes/PDE/studies/resnet_generalization/protocol/run_grid.py:26): `REGISTRY`; retained destination `data/historical/studies/resnet_generalization/protocol/cases.json`.
- [studies/resnet_generalization/tests/test_runner_hashes.py:16](/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_runner_hashes.py:16): `REGISTRY`; retained destination `data/historical/studies/resnet_generalization/protocol/cases.json`.
- [studies/resnet_generalization/tests/test_study_provenance.py:13](/home/amir/Codes/PDE/studies/resnet_generalization/tests/test_study_provenance.py:13): `REGISTRY`; retained destination `data/historical/studies/resnet_generalization/protocol/cases.json`.
- [studies/resnet_activation_controls/run_experiment.py:38](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py:38): `PROTOCOL_PATH`; retained destination `data/historical/studies/resnet_activation_controls/protocol/preregistered_protocol.json`.
- [studies/resnet_activation_controls/run_experiment.py:39](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py:39): `CASES_PATH`; retained destination `data/historical/studies/resnet_activation_controls/protocol/cases.json`.
- [studies/resnet_activation_controls/run_experiment.py:52](/home/amir/Codes/PDE/studies/resnet_activation_controls/run_experiment.py:52): `PARENT_RELEASE`; retained destination `data/historical/studies/resnet_activation_controls/parent/dense_mup_pde_generalization_repro.zip`.
- [studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py:36](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py:36): `FP64_CONFIG_PATH`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/FROZEN_LOCAL_QUALIFICATION.json`.
- [studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:27](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:27): `CONFIG_PATH`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/breadth_panel/FROZEN_ONE_INPUT_POINTS.json`.
- [studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:30](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:30): `ATTEMPTS_PATH`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/breadth_panel/runs/validation_one_input_v1/ATTEMPTS.json`.
- [studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:31](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py:31): `RESULT_PATH`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/breadth_panel/VALIDATION_RESULT.json`.
- [studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py:32](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py:32): `CONFIG`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/configs/FROZEN_STAGE_V.json`.
- [studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py:36](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py:36): `LEDGER`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/.runtime/stage_v_attempts.json`.
- [studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/analyze_stage_v.py:16](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/analyze_stage_v.py:16): `CONFIG`; retained destination `data/historical/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/configs/FROZEN_STAGE_V.json`.
- [studies/mfp_program_history/report/build_report.py:24](/home/amir/Codes/PDE/studies/mfp_program_history/report/build_report.py:24): `REPORT_PDF`; retained destination `data/historical/studies/mfp_program_history/report/MEAN_FIELD_PEELING_REPORT.pdf`.

## Exact changed paths

The complete scoped patch is [worker.diff](/tmp/flat-study-path-repair-OE9KpPVL/worker.diff). Before/after source hashes are in [changed-paths.json](/tmp/flat-study-path-repair-OE9KpPVL/changed-paths.json); syntax, hash-literal, and checked-data results are in [verification.json](/tmp/flat-study-path-repair-OE9KpPVL/verification.json). All comparisons use this worker's pre-edit live-source snapshot, independently of concurrent Git/core/index work.

- [studies/mfp_cubic_compiler/depth2_gaussian_program/depth2_cubic_stieltjes_audit.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/depth2_gaussian_program/depth2_cubic_stieltjes_audit.py)
- [studies/mfp_cubic_compiler/depth2_gaussian_program/test_depth2_cubic_exact_jet.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/depth2_gaussian_program/test_depth2_cubic_exact_jet.py)
- [studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_symbolic_order5.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_symbolic_order5.py)
- [studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_two_input_cubic_plus.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_two_input_cubic_plus.py)
- [studies/mfp_cubic_compiler/two_input_plus_gaussian_program/test_two_input_cubic_plus.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/test_two_input_cubic_plus.py)
- [studies/mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_plus_fixed_rho_jet.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_plus_fixed_rho_jet.py)
- [studies/mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_stieltjes_order5.py](/home/amir/Codes/PDE/studies/mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_stieltjes_order5.py)
- [studies/mfp_gaussian_calculus/compiler/test_finite_width_jet.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/compiler/test_finite_width_jet.py)
- [studies/mfp_gaussian_calculus/depth_order5/primary/freeze_primary.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5/primary/freeze_primary.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/hostile_gamma04_derivation.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/hostile_gamma04_derivation.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/hostile_gamma04_derivation_v2.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/hostile_gamma04_derivation_v2.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_curvature_extension.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_curvature_extension.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_sine_regression.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_sine_regression.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_curvature_extension.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_curvature_extension.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_sine_regression.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_h3_sine_regression.py)
- [studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_hostile_checks.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/run_hostile_checks.py)
- [studies/mfp_gaussian_calculus/order5/audit_hostile.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/audit_hostile.py)
- [studies/mfp_gaussian_calculus/order5/compiler/compare_independent.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/compiler/compare_independent.py)
- [studies/mfp_gaussian_calculus/order5/finite_width/test_order5.py](/home/amir/Codes/PDE/studies/mfp_gaussian_calculus/order5/finite_width/test_order5.py)
- [studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py](/home/amir/Codes/PDE/studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py)
- [studies/mfp_identity_compiler/linear_gaussian_program/identity_order13_stieltjes_audit.py](/home/amir/Codes/PDE/studies/mfp_identity_compiler/linear_gaussian_program/identity_order13_stieltjes_audit.py)
- [studies/mfp_identity_compiler/linear_gaussian_program/identity_stieltjes_audit.py](/home/amir/Codes/PDE/studies/mfp_identity_compiler/linear_gaussian_program/identity_stieltjes_audit.py)
- [studies/mfp_linear_growth_uniform_counterexample/bump_laurent_certificate.py](/home/amir/Codes/PDE/studies/mfp_linear_growth_uniform_counterexample/bump_laurent_certificate.py)
- [studies/mfp_linear_growth_uniform_counterexample/evaluate_full_l2_transition.py](/home/amir/Codes/PDE/studies/mfp_linear_growth_uniform_counterexample/evaluate_full_l2_transition.py)
- [studies/mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py](/home/amir/Codes/PDE/studies/mfp_linear_growth_uniform_counterexample/full_l2_paired_transition.py)
- [studies/mfp_quadratic_compiler/campaign1/test_hankel_analysis.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign1/test_hankel_analysis.py)
- [studies/mfp_quadratic_compiler/campaign1/test_order9_q2_order8.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign1/test_order9_q2_order8.py)
- [studies/mfp_quadratic_compiler/campaign4/make_provenance.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign4/make_provenance.py)
- [studies/mfp_quadratic_compiler/campaign4/test_results_and_certificates.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign4/test_results_and_certificates.py)
- [studies/mfp_quadratic_compiler/campaign5_b3/postprocess_lower_moments.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign5_b3/postprocess_lower_moments.py)
- [studies/mfp_quadratic_compiler/campaign5_b3/test_b2_order5_gate.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign5_b3/test_b2_order5_gate.py)
- [studies/mfp_quadratic_compiler/campaign5_b3/test_stage_c_sector.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/campaign5_b3/test_stage_c_sector.py)
- [studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py)
- [studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_order13_stieltjes_audit.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_order13_stieltjes_audit.py)
- [studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_stieltjes_audit.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/depth3_gaussian_program/depth3_stieltjes_audit.py)
- [studies/mfp_quadratic_compiler/depth3_gaussian_program/test_depth3_order13_stieltjes.py](/home/amir/Codes/PDE/studies/mfp_quadratic_compiler/depth3_gaussian_program/test_depth3_order13_stieltjes.py)
- [studies/mfp_quadratic_l2_order5/audit_direct.py](/home/amir/Codes/PDE/studies/mfp_quadratic_l2_order5/audit_direct.py)
- [studies/mfp_quadratic_l2_order5/audit_quadratic_euler_jet.py](/home/amir/Codes/PDE/studies/mfp_quadratic_l2_order5/audit_quadratic_euler_jet.py)
- [studies/mfp_quadratic_l2_order5/quadratic_exact.py](/home/amir/Codes/PDE/studies/mfp_quadratic_l2_order5/quadratic_exact.py)
- [studies/mfp_sine_compiler/depth2_gaussian_program/normalized_sine_order5.py](/home/amir/Codes/PDE/studies/mfp_sine_compiler/depth2_gaussian_program/normalized_sine_order5.py)
- [studies/mfp_sine_compiler/depth2_gaussian_program/raw_sine_order5.py](/home/amir/Codes/PDE/studies/mfp_sine_compiler/depth2_gaussian_program/raw_sine_order5.py)
- [studies/mfp_sine_compiler/depth2_gaussian_program/sine_order9_stieltjes_audit.py](/home/amir/Codes/PDE/studies/mfp_sine_compiler/depth2_gaussian_program/sine_order9_stieltjes_audit.py)
- [studies/mfp_sine_compiler/depth2_gaussian_program/test_sine_order5.py](/home/amir/Codes/PDE/studies/mfp_sine_compiler/depth2_gaussian_program/test_sine_order5.py)
- [studies/resnet_bridgeability/targeted_bridge_test.py](/home/amir/Codes/PDE/studies/resnet_bridgeability/targeted_bridge_test.py)
- [studies/resnet_proof_audit/protocol/freeze_study.py](/home/amir/Codes/PDE/studies/resnet_proof_audit/protocol/freeze_study.py)
- [studies/resnet_proof_audit/source/cross_p.py](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/cross_p.py)
- [studies/resnet_proof_audit/source/dense_gates.py](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/dense_gates.py)
- [studies/resnet_proof_audit/source/pde_tangent.py](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/pde_tangent.py)
- [studies/resnet_proof_audit/source/run_study.py](/home/amir/Codes/PDE/studies/resnet_proof_audit/source/run_study.py)
- [studies/resnet_scalar_stress/one_input_hermite_ladder.py](/home/amir/Codes/PDE/studies/resnet_scalar_stress/one_input_hermite_ladder.py)
- [studies/resnet_tail_compactness/coupled_cauchy_ledger.py](/home/amir/Codes/PDE/studies/resnet_tail_compactness/coupled_cauchy_ledger.py)
- [studies/resnet_tail_compactness/targeted_tail_commutator.py](/home/amir/Codes/PDE/studies/resnet_tail_compactness/targeted_tail_commutator.py)
- [studies/stieltjes_finite_width/jet_control_variate.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/jet_control_variate.py)
- [studies/stieltjes_finite_width/run_fresh_calibrated_ratio.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_calibrated_ratio.py)
- [studies/stieltjes_finite_width/run_fresh_order13_median.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_fresh_order13_median.py)
- [studies/stieltjes_finite_width/run_positive_time_pair_median.py](/home/amir/Codes/PDE/studies/stieltjes_finite_width/run_positive_time_pair_median.py)
- [studies/stieltjes_hybrid_campaign/bounded_dmft/truncated_mfp_reference.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/bounded_dmft/truncated_mfp_reference.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/tests/test_fp64_local.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/tests/test_fp64_local.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/one_input/tests/test_one_input_engine.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/one_input/tests/test_one_input_engine.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/proxy_contract.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/proxy_contract.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/analyze.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/run_block.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_n4096/run_block.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/compare_with_n4096.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/compare_with_n4096.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/run_block.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/successive_n8192/run_block.py)
- [studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py)
- [studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/tests/test_euler_fp32.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/tests/test_euler_fp32.py)
- [studies/stieltjes_hybrid_campaign/width_ladder/width_engine.py](/home/amir/Codes/PDE/studies/stieltjes_hybrid_campaign/width_ladder/width_engine.py)
- [studies/stieltjes_proxy_campaign/proxy/inventory.py](/home/amir/Codes/PDE/studies/stieltjes_proxy_campaign/proxy/inventory.py)
- [studies/stieltjes_resolution/block_metric_counterexample.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/block_metric_counterexample.py)
- [studies/stieltjes_resolution/block_metric_positive_alpha_jet.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/block_metric_positive_alpha_jet.py)
- [studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py)
- [studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_recurrence.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_recurrence.py)
- [studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_scalar_audit.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_scalar_audit.py)
- [studies/stieltjes_resolution/canonical_hidden_high_order/production_hidden_recurrence.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/production_hidden_recurrence.py)
- [studies/stieltjes_resolution/canonical_hidden_high_order/test_independent_hidden_recurrence.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/test_independent_hidden_recurrence.py)
- [studies/stieltjes_resolution/canonical_hidden_high_order/test_production_hidden_recurrence.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_hidden_high_order/test_production_hidden_recurrence.py)
- [studies/stieltjes_resolution/canonical_high_order/test_independent_canonical_recurrence.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_high_order/test_independent_canonical_recurrence.py)
- [studies/stieltjes_resolution/canonical_high_order/test_production_canonical_recurrence.py](/home/amir/Codes/PDE/studies/stieltjes_resolution/canonical_high_order/test_production_canonical_recurrence.py)

