# Research studies

Each row below is a top-level study directory. There are no enclosing scientific
program directories. Internal folders such as implementations, tests, independent
routes and immutable source/review collections describe roles within a study;
they are not an additional active-study hierarchy.

Start with the [reconciled research map](project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for claim statuses and supersession, or the [established library](../docs/README.md)
for complete maintained theory. This catalogue is not a list of accepted theorems.
Some folders contain proved auxiliary results; others contain rejected attempts,
experiments, conditional extensions or immutable historical copies.

The [source-recovery collection](recovered_sources_2026_09_09/README.md) preserves
temporary and other-user sources. The [refactor record](repository_refactor_2026_09_09/PLAN.md)
contains exact old-to-new paths and rollback information. Frozen source/review
copies are intentionally byte-preserved: an old path or hash in such a document
is provenance, not a promise that the former working directory still exists.
Historical runtime outputs are under `data/historical/` at the repository root.

The single shared support module [_output_paths.py](_output_paths.py) handles
fresh-output and explicit historical-input selection for several working
studies. It is exploration infrastructure, not another study or an established
mathematical API. Keeping it beside the catalogue avoids a permanent dependency
on a dated migration study. Study-specific rules remain inside their studies.

## Flat catalogue

- [activation_class_all_depths](activation_class_all_depths/README.md)
- [arctan_l2_order_one_readout](arctan_l2_order_one_readout/README.md)
- [arctan_l3_order_one_readout](arctan_l3_order_one_readout/README.md)
- [arctan_source_reaudit](arctan_source_reaudit/README.md)
- [arctan_source_reconstruction](arctan_source_reconstruction/README.md)
- [calibrated_near_identity_reviews](calibrated_near_identity_reviews/README.md)
- [causal_flow_peeling_calculus](causal_flow_peeling_calculus/README.md)
- [convex_offset_all_depths](convex_offset_all_depths/README.md)
- [d3_arctan_closure_program](d3_arctan_closure_program/README.md)
- [deep_linear_closure_boundary](deep_linear_closure_boundary/README.md)
- [deep_linear_joint_limit](deep_linear_joint_limit/README.md)
- [four_thread_consolidation](four_thread_consolidation/README.md)
- [historical_project_documents](historical_project_documents/README.md)
- [leaky_arctan_l3_operator_limit](leaky_arctan_l3_operator_limit/README.md)
- [mfp_cubic_compiler](mfp_cubic_compiler/README.md)
- [mfp_depth_time_doubling](mfp_depth_time_doubling/README.md)
- [mfp_finite_step_single_hidden_mlp](mfp_finite_step_single_hidden_mlp/README.md)
- [mfp_finite_step_two_hidden_mlp](mfp_finite_step_two_hidden_mlp/README.md)
- [mfp_gaussian_calculus](mfp_gaussian_calculus/README.md)
- [mfp_general_depth_four_vs_two_bound](mfp_general_depth_four_vs_two_bound/README.md)
- [mfp_general_depth_general_time_stepdoubling_bound](mfp_general_depth_general_time_stepdoubling_bound/README.md)
- [mfp_general_depth_halfstep_bound](mfp_general_depth_halfstep_bound/README.md)
- [mfp_general_time_doubling](mfp_general_time_doubling/README.md)
- [mfp_identity_compiler](mfp_identity_compiler/README.md)
- [mfp_joint_width_mesh_quadratic](mfp_joint_width_mesh_quadratic/README.md)
- [mfp_linear_growth_uniform_counterexample](mfp_linear_growth_uniform_counterexample/README.md)
- [mfp_loss_gradient_flow_audit](mfp_loss_gradient_flow_audit/README.md)
- [mfp_loss_gradient_time_doubling](mfp_loss_gradient_time_doubling/README.md)
- [mfp_loss_mesh_resolution](mfp_loss_mesh_resolution/README.md)
- [mfp_loss_time_doubling](mfp_loss_time_doubling/README.md)
- [mfp_near_identity_omfp](mfp_near_identity_omfp/README.md)
- [mfp_next_rung](mfp_next_rung/README.md)
- [mfp_omfp_continuous_time](mfp_omfp_continuous_time/README.md)
- [mfp_oscillatory_linear_growth](mfp_oscillatory_linear_growth/README.md)
- [mfp_polynomial_uniform_no_go](mfp_polynomial_uniform_no_go/README.md)
- [mfp_program_history](mfp_program_history/README.md)
- [mfp_quadratic_compiler](mfp_quadratic_compiler/README.md)
- [mfp_quadratic_l2_order5](mfp_quadratic_l2_order5/README.md)
- [mfp_quadratic_loss_initial_layer](mfp_quadratic_loss_initial_layer/README.md)
- [mfp_quantitative_width_first_bound](mfp_quantitative_width_first_bound/README.md)
- [mfp_quantitative_width_first_bound_general_t](mfp_quantitative_width_first_bound_general_t/README.md)
- [mfp_quantitative_width_first_bound_rung3](mfp_quantitative_width_first_bound_rung3/README.md)
- [mfp_quantitative_width_first_bound_rung4](mfp_quantitative_width_first_bound_rung4/README.md)
- [mfp_quantitative_width_first_rung3](mfp_quantitative_width_first_rung3/README.md)
- [mfp_relu_uniform_remainder](mfp_relu_uniform_remainder/README.md)
- [mfp_scaling_comparison](mfp_scaling_comparison/README.md)
- [mfp_sine_compiler](mfp_sine_compiler/README.md)
- [mfp_spike_corridor_l2](mfp_spike_corridor_l2/README.md)
- [mfp_three_hidden_halfstep_bound](mfp_three_hidden_halfstep_bound/README.md)
- [mfp_uniform_near_identity_l2](mfp_uniform_near_identity_l2/README.md)
- [mfp_width_first_operator_peeling](mfp_width_first_operator_peeling/README.md)
- [moderate_sine_global](moderate_sine_global/README.md)
- [odd_activation_lower_powers_three_inputs](odd_activation_lower_powers_three_inputs/README.md)
- [odd_mixture_general_depth](odd_mixture_general_depth/README.md)
- [odd_mixture_separation_quantitative](odd_mixture_separation_quantitative/README.md)
- [practical_fixed_depth2](practical_fixed_depth2/README.md)
- [practical_global_limit_assessment](practical_global_limit_assessment/README.md)
- [project_wide_audit_2026_09_08](project_wide_audit_2026_09_08/README.md)
- [quadratic_nonclosure](quadratic_nonclosure/README.md)
- [rcgc_arctan_l2](rcgc_arctan_l2/README.md)
- [rcgc_arctan_l3](rcgc_arctan_l3/README.md)
- [rcgc_compiler](rcgc_compiler/README.md)
- [rcgc_linear_depth](rcgc_linear_depth/README.md)
- [rcgc_program_history](rcgc_program_history/README.md)
- [rcgc_shallow](rcgc_shallow/README.md)
- [recovered_sources_2026_09_09](recovered_sources_2026_09_09/README.md)
- [research_workflow_2026_09_10](research_workflow_2026_09_10/README.md) — permanent process maintenance
- [repository_refactor_2026_09_09](repository_refactor_2026_09_09/README.md)
- [residual_continuous_depth_gradient_flow](residual_continuous_depth_gradient_flow/README.md)
- [resnet_activation_controls](resnet_activation_controls/README.md)
- [resnet_bridgeability](resnet_bridgeability/README.md)
- [resnet_dense_early_audit](resnet_dense_early_audit/README.md)
- [resnet_dense_long_horizon](resnet_dense_long_horizon/README.md)
- [resnet_generalization](resnet_generalization/README.md)
- [resnet_lean_salvage](resnet_lean_salvage/README.md)
- [resnet_operator_core](resnet_operator_core/README.md)
- [resnet_program_history](resnet_program_history/README.md)
- [resnet_proof_audit](resnet_proof_audit/README.md)
- [resnet_reproduction_2026_07_31](resnet_reproduction_2026_07_31/README.md)
- [resnet_scalar_stress](resnet_scalar_stress/README.md)
- [resnet_tail_compactness](resnet_tail_compactness/README.md)
- [stieltjes_direct_loewner](stieltjes_direct_loewner/README.md)
- [stieltjes_finite_width](stieltjes_finite_width/README.md)
- [stieltjes_hybrid_campaign](stieltjes_hybrid_campaign/README.md)
- [stieltjes_program_history](stieltjes_program_history/README.md)
- [stieltjes_proxy_campaign](stieltjes_proxy_campaign/README.md)
- [stieltjes_resolution](stieltjes_resolution/README.md)
- [stieltjes_theory_history](stieltjes_theory_history/README.md)
- [tanh_l3_operator_limit](tanh_l3_operator_limit/README.md)
- [three_sample_activation_class](three_sample_activation_class/README.md)
- [three_sample_near_identity_all_depths](three_sample_near_identity_all_depths/README.md)
- [three_sample_odd_activation_depth2](three_sample_odd_activation_depth2/README.md)
- [three_sample_odd_activation_full_resolution](three_sample_odd_activation_full_resolution/README.md)
- [three_sample_odd_activation_threshold](three_sample_odd_activation_threshold/README.md)
- [three_sample_odd_gain_all_depths](three_sample_odd_gain_all_depths/README.md)
- [three_sample_self_contained](three_sample_self_contained/README.md)
- [three_sample_separated_angle_theorem](three_sample_separated_angle_theorem/README.md)
- [two_sample_activation_design](two_sample_activation_design/README.md)
- [two_sample_odd_activation_delta10](two_sample_odd_activation_delta10/README.md)
- [two_sample_odd_activation_depth4](two_sample_odd_activation_depth4/README.md)
- [two_sample_odd_activation_depth56](two_sample_odd_activation_depth56/README.md)
- [two_sample_odd_activation_power10](two_sample_odd_activation_power10/README.md)
- [two_sample_odd_activation_power4](two_sample_odd_activation_power4/README.md)
- [two_sample_odd_activation_quantitative](two_sample_odd_activation_quantitative/README.md)
- [two_sample_odd_activation_theorem](two_sample_odd_activation_theorem/README.md)
- [two_sample_separated_angle_theorem](two_sample_separated_angle_theorem/README.md)

## Starting and promoting work

The permanent [study lifecycle and promotion gates](../RESEARCH_WORKFLOW.md) are
introduced automatically by the root [AGENTS.md](../AGENTS.md). One research
thrust occupies one study even when several PDE/PDE-2 tasks cooperate. Use
`python -B studies/_workflow.py start <name> --question "..." --owner "..."`
from the repository root, or `adopt` for an existing study. The helper creates
current records and freezes hash-bound review inputs; its checks establish only
evidence readiness, not scientific correctness or permission to bypass reviews.
The helper itself, like `_output_paths.py`, is shared exploration infrastructure,
not an established mathematical API or a new scientific programme hierarchy.


Use one distinctive study name for a scientific investigation. Keep its question,
model/clock contract, current claim status, source dependencies, experiments and
review evidence explicit. Do not split every intermediate proof lemma into a new
study. Keep independent verification implementations genuinely independent.

Write generated output to an explicit directory under `data/`; record the full
command, configuration and seed. A study may use the established code or theory.
The reverse dependency is prohibited, including from tests, figures and proof
appendices. Promotion requires bringing the entire accepted dependency closure
into the library, reconciling notation, independent value screening, paired full
correctness audits and a separate review of the actual final integration. New
provenance and acceptance records stay in the originating study, not in the dated
refactor study. Generated scratch and review execution outputs use only the study
data namespace; author edits stay in the study until the integration role takes over.
