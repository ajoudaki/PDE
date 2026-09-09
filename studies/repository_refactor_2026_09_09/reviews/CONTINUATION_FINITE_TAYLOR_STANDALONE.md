# Standalone finite reductions and formal-jet validation

27 scientific files, no studies, data, or PDF exporter.

```text
python -B code/tools/check_library.py
Library boundary and local links checked: 25 files.
make test
make[1]: Entering directory '/tmp/pde_finite_taylor_standalone'
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_*.py' -v
test_displayed_exact_certificate_and_independent_witness (test_exact_calculus.CertificateTests) ... ok
test_domains_and_return_ownership (test_exact_calculus.EulerPullbackTests) ... ok
test_every_displayed_temporal_polynomial (test_exact_calculus.EulerPullbackTests) ... ok
test_nonlinear_scalar_euler_against_differential_words (test_exact_calculus.EulerPullbackTests) ... ok
test_words_against_independent_step_slot_enumeration (test_exact_calculus.EulerPullbackTests) ... ok
test_components_decorations_and_empty (test_exact_calculus.ForestTests) ... ok
test_invalid_graphs (test_exact_calculus.ForestTests) ... ok
test_relabeling_all_orders_and_edge_orientations (test_exact_calculus.ForestTests) ... ok
test_determinants_swaps_singular_empty_and_rational (test_exact_calculus.FormalArithmeticTests) ... ok
test_invalid_rational_inputs (test_exact_calculus.FormalArithmeticTests) ... ok
test_reversion_two_compositions_and_exact_known_inverse (test_exact_calculus.FormalArithmeticTests) ... ok
test_inplace_and_shared_buffer_callbacks_are_owned (test_finite_jets.ContractTests) ... ok
test_invalid_callback_shape_type_finiteness_at_every_order (test_finite_jets.ContractTests) ... ok
test_invalid_scope_arguments_and_mutated_parameters (test_finite_jets.ContractTests) ... ok
test_nonfinite_contractions_and_derivative_conversion_rejected (test_finite_jets.ContractTests) ... ok
test_order_prefix_and_no_unused_derivative_requests (test_finite_jets.ContractTests) ... ok
test_scaling_keeps_representable_first_order_coefficients (test_finite_jets.ContractTests) ... ok
test_constant_activation_differentiates_residual_in_physical_time (test_finite_jets.MovingFlowTests) ... ok
test_cubic_hand_solution_uses_every_activation_derivative (test_finite_jets.MovingFlowTests) ... ok
test_forward_fields_along_parameter_polynomial (test_finite_jets.MovingFlowTests) ... ok
test_independent_neuron_relabeling_preserves_output (test_finite_jets.MovingFlowTests) ... ok
test_linear_equal_weights_hand_solution_is_moving_flow (test_finite_jets.MovingFlowTests) ... ok
test_parameter_acceleration_and_jerk_against_existing_rhs_differences (test_finite_jets.MovingFlowTests) ... ok
test_raw_api_shapes_normalization_and_first_derivative (test_finite_jets.MovingFlowTests) ... ok
test_zero_residual_and_zero_input (test_finite_jets.MovingFlowTests) ... ok
test_batch_permutation_and_duplication_preserve_dynamics (test_finite_network.FiniteIdentityTests) ... ok
test_correlated_opposite_and_conflicting_samples_preserved (test_finite_network.FiniteIdentityTests) ... ok
test_flow_output_velocity_and_weighted_energy (test_finite_network.FiniteIdentityTests) ... ok
test_gd_all_depths_matches_independent_loss_differences (test_finite_network.FiniteIdentityTests) ... ok
test_kernel_blocks_against_numeric_output_jacobians (test_finite_network.FiniteIdentityTests) ... ok
test_linear_forward_backward_and_input_normalization (test_finite_network.FiniteIdentityTests) ... ok
test_loss_gradients_all_coordinates_all_blocks (test_finite_network.FiniteIdentityTests) ... ok
test_simultaneous_gd_has_exact_hand_computed_update (test_finite_network.FiniteIdentityTests) ... ok
test_zero_residual_and_zero_step (test_finite_network.FiniteIdentityTests) ... ok
test_exact_gaussian_scales_draw_order_and_seed (test_finite_network.InitializationTests) ... ok
test_one_layer_width_one_and_global_rng_is_unchanged (test_finite_network.InitializationTests) ... ok
test_activation_validation_and_layerwise_values (test_finite_network.ValidationTests) ... ok
test_inputs_labels_and_mobilities (test_finite_network.ValidationTests) ... ok
test_invalid_initialization (test_finite_network.ValidationTests) ... ok
test_parameter_shapes_and_values (test_finite_network.ValidationTests) ... ok
test_against_existing_layerwise_core (test_finite_reductions.MixedReductionTests) ... ok
test_lax_chain_rule_both_mixed_models (test_finite_reductions.MixedReductionTests) ... ok
test_qq_balance_chain_rule (test_finite_reductions.MixedReductionTests) ... ok
test_spectrum_orientation_witness_is_raw_realizable (test_finite_reductions.MixedReductionTests) ... ok
test_complete_field_chain_rule_and_physical_energy (test_finite_reductions.RMSReductionTests) ... ok
test_every_output_gradient_coordinate_and_kernel_block (test_finite_reductions.RMSReductionTests) ... ok
test_signed_balance_drifts_from_raw_parameter_chain_rule (test_finite_reductions.RMSReductionTests) ... ok
test_zero_coordinates_sign_quotient_and_zero_residual (test_finite_reductions.RMSReductionTests) ... ok
test_scope_validation_and_fresh_arrays (test_finite_reductions.ReductionContractTests) ... ok
test_asymmetric_and_indefinite_covariance_rejected (test_gaussian_moments.GaussianMomentTests) ... ok
test_correlated_bivariate_known_moments (test_gaussian_moments.GaussianMomentTests) ... ok
test_independent_coordinates_factor (test_gaussian_moments.GaussianMomentTests) ... ok
test_inputs_unchanged_and_cache_does_not_cross_calls (test_gaussian_moments.GaussianMomentTests) ... ok
test_invalid_covariance_entries_and_degrees (test_gaussian_moments.GaussianMomentTests) ... ok
test_permutation_preserves_moment (test_gaussian_moments.GaussianMomentTests) ... ok
test_shapes_and_finite_sequences (test_gaussian_moments.GaussianMomentTests) ... ok
test_singular_rank_one_covariance (test_gaussian_moments.GaussianMomentTests) ... ok
test_trivariate_pairings_and_negative_correlation (test_gaussian_moments.GaussianMomentTests) ... ok
test_univariate_known_even_and_odd_moments (test_gaussian_moments.GaussianMomentTests) ... ok
test_zero_pivots_and_zero_covariance (test_gaussian_moments.GaussianMomentTests) ... ok
test_dangling_symlink_rejected_without_reading (test_library_boundary.LibraryBoundaryTests) ... ok
test_existing_relative_module (test_library_boundary.LibraryBoundaryTests) ... ok
test_missing_inline_and_reference_links (test_library_boundary.LibraryBoundaryTests) ... ok
test_missing_modules_and_undeclared_imports (test_library_boundary.LibraryBoundaryTests) ... ok
test_valid_links_and_math_lookalikes (test_library_boundary.LibraryBoundaryTests) ... ok
test_builtin_derivatives_at_branch_boundaries_and_both_signs (test_numerical_contract.NumericalContractTests) ... ok
test_first_layer_normalizes_after_raw_contraction (test_numerical_contract.NumericalContractTests) ... ok
test_gd_addition_cancels_unrepresentable_increment (test_numerical_contract.NumericalContractTests) ... ok
test_gd_does_not_require_representable_velocity (test_numerical_contract.NumericalContractTests) ... ok
test_inplace_derivative_preserves_hidden (test_numerical_contract.NumericalContractTests) ... ok
test_inplace_value_has_correct_loss_gradient (test_numerical_contract.NumericalContractTests) ... ok
test_inplace_value_preserves_preactivation (test_numerical_contract.NumericalContractTests) ... ok
test_kernel_normalization_preserves_subnormal_raw_grams (test_numerical_contract.NumericalContractTests) ... ok
test_kernel_scale_order_avoids_premature_overflow (test_numerical_contract.NumericalContractTests) ... ok
test_kernel_scale_order_preserves_binary_result_and_signed_entries (test_numerical_contract.NumericalContractTests) ... ok
test_large_arctan_gradient_retains_representable_signal (test_numerical_contract.NumericalContractTests) ... ok
test_large_batch_mean_square_is_representable (test_numerical_contract.NumericalContractTests) ... ok
test_large_mobility_preserves_finite_velocity_and_stationarity (test_numerical_contract.NumericalContractTests) ... ok
test_middle_kernel_scale_order (test_numerical_contract.NumericalContractTests) ... ok
test_physical_updates_do_not_require_representable_loss_gradient (test_numerical_contract.NumericalContractTests) ... ok
test_physical_updates_preserve_subnormal_raw_contractions (test_numerical_contract.NumericalContractTests) ... ok
test_reused_output_buffer_does_not_alias_layers (test_numerical_contract.NumericalContractTests) ... ok
test_saturated_tanh_gradient_retains_representable_signal (test_numerical_contract.NumericalContractTests) ... ok
test_unrepresentable_loss_is_rejected (test_numerical_contract.NumericalContractTests) ... ok
test_unrepresentable_total_kernel_is_rejected (test_numerical_contract.NumericalContractTests) ... ok
test_unsigned_positive_steps_are_descent_steps (test_numerical_contract.NumericalContractTests) ... ok

----------------------------------------------------------------------
Ran 86 tests in 0.431s

OK
make[1]: Leaving directory '/tmp/pde_finite_taylor_standalone'
```
