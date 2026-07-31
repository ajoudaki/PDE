from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import sys
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "source"))

from dense_gates import (  # noqa: E402
    construct_invisible_perturbation,
    empirical_degree_one_hermite_phi,
    estimate_depth_homogenization,
    initialize_gaussian_master,
    materialize_coupled_state,
    retained_row_coefficients,
    simulate_checkpoints,
)

# ``dense_gates`` has already installed the canonical source path.
from dense_reference import (  # noqa: E402
    ModelSpec,
    forward_adjoint,
    rk4_param_step,
)


def _spec(*, n: int, depth: int, seed: int = 91) -> ModelSpec:
    X = np.array(
        [
            [1.0, 0.2, -0.1],
            [0.0, 0.9, 0.25],
            [0.1, -0.15, 0.95],
        ]
    )
    y = np.array([0.7, -0.45, 0.25])
    return ModelSpec(
        n=n,
        depth=depth,
        X=X,
        y=y,
        seed=seed,
        sigma_w=0.65,
        A=1.0,
        gamma=1.0,
        activation="tanh",
    )


class CoupledMasterTests(unittest.TestCase):
    def test_width_prefix_and_depth_block_sum_couplings_are_exact(self) -> None:
        master = initialize_gaussian_master(
            n_max=14,
            depth_max=8,
            input_dim=3,
            seed=1021,
        )
        small = materialize_coupled_state(master, _spec(n=7, depth=4))
        wide = materialize_coupled_state(master, _spec(n=14, depth=4))

        np.testing.assert_array_equal(small.B, wide.B[:7])
        np.testing.assert_array_equal(small.a, wide.a[:7])
        small_standard = small.W * np.sqrt(7.0) / 0.65
        wide_standard = wide.W * np.sqrt(14.0) / 0.65
        np.testing.assert_allclose(
            small_standard,
            wide_standard[:, :7, :7],
            rtol=0.0,
            # The two paths undo distinct sqrt(n) scalings, so a handful of
            # final-bit roundoff differences are expected.
            atol=1e-15,
        )

        coarse = materialize_coupled_state(master, _spec(n=9, depth=2))
        fine = materialize_coupled_state(master, _spec(n=9, depth=8))
        expected = fine.W.reshape(2, 4, 9, 9).sum(axis=1) / 2.0
        np.testing.assert_allclose(coarse.W, expected, rtol=2e-16, atol=2e-16)
        np.testing.assert_array_equal(coarse.B, fine.B)
        np.testing.assert_array_equal(coarse.a, fine.a)

        repeated = materialize_coupled_state(master, _spec(n=9, depth=2))
        np.testing.assert_array_equal(repeated.B, coarse.B)
        np.testing.assert_array_equal(repeated.W, coarse.W)
        np.testing.assert_array_equal(repeated.a, coarse.a)

    def test_invalid_non_nested_depth_is_rejected(self) -> None:
        master = initialize_gaussian_master(
            n_max=8,
            depth_max=8,
            input_dim=3,
            seed=4,
        )
        with self.assertRaisesRegex(ValueError, "divide"):
            materialize_coupled_state(master, _spec(n=8, depth=3))


class CheckpointSimulatorTests(unittest.TestCase):
    def test_exact_checkpoints_match_direct_rk4_and_are_restartable(self) -> None:
        spec = _spec(n=9, depth=3)
        master = initialize_gaussian_master(
            n_max=9,
            depth_max=3,
            input_dim=3,
            seed=110,
        )
        initial = materialize_coupled_state(master, spec)
        trajectory = simulate_checkpoints(
            initial,
            spec,
            (0.0, 0.01, 0.025),
            dt=0.01,
        )
        self.assertEqual(trajectory.f.shape, (3, 3))
        self.assertEqual(trajectory.gram.shape, (3, 4, 3, 3))
        self.assertEqual(trajectory.theta.shape, (3, 3, 3))
        for theta in trajectory.theta:
            np.testing.assert_allclose(theta, theta.T, atol=1e-14)
            self.assertGreaterEqual(float(np.linalg.eigvalsh(theta)[0]), -1e-11)

        direct = rk4_param_step(initial, 0.01, spec)
        direct = rk4_param_step(direct, 0.01, spec)
        direct = rk4_param_step(direct, 0.005, spec)
        np.testing.assert_allclose(trajectory.final_state.B, direct.B)
        np.testing.assert_allclose(trajectory.final_state.W, direct.W)
        np.testing.assert_allclose(trajectory.final_state.a, direct.a)

        first_leg = simulate_checkpoints(
            initial,
            spec,
            (0.0, 0.02),
            dt=0.01,
        )
        second_leg = simulate_checkpoints(
            first_leg.final_state,
            spec,
            (0.02, 0.04),
            dt=0.01,
            start_time=0.02,
        )
        whole = simulate_checkpoints(
            initial,
            spec,
            (0.0, 0.02, 0.04),
            dt=0.01,
        )
        np.testing.assert_array_equal(second_leg.f[0], whole.f[1])
        np.testing.assert_allclose(second_leg.f[1], whole.f[2], atol=2e-15)
        np.testing.assert_allclose(
            second_leg.gram[1],
            whole.gram[2],
            atol=2e-15,
        )
        np.testing.assert_allclose(
            second_leg.theta[1],
            whole.theta[2],
            atol=2e-15,
        )

        # The simulator takes ownership of no caller array.
        pristine = materialize_coupled_state(master, spec)
        np.testing.assert_array_equal(initial.B, pristine.B)
        np.testing.assert_array_equal(initial.W, pristine.W)
        np.testing.assert_array_equal(initial.a, pristine.a)


class HomogenizationEstimatorTests(unittest.TestCase):
    def _run(self):
        return estimate_depth_homogenization(
            _spec(n=9, depth=4),
            depths=(2, 4),
            ensemble_size=4,
            seed=20260724,
            # Exercise the requested positive-time trained checkpoint.
            checkpoints=(0.0, 0.5),
            dt=0.1,
        )

    def test_model_free_statistics_are_deterministic_and_fully_accounted(self) -> None:
        report = self._run()
        repeated = self._run()
        self.assertEqual(report.depths, (2, 4))
        self.assertEqual(report.ensemble_size, 4)
        self.assertEqual(set(report.checkpoints), {0.0, 0.5})
        np.testing.assert_array_equal(report.shared_B, repeated.shared_B)
        np.testing.assert_array_equal(report.shared_a, repeated.shared_a)

        for time in (0.0, 0.5):
            checkpoint = report.checkpoints[time]
            checkpoint_repeated = repeated.checkpoints[time]
            for direction in ("forward", "backward"):
                table = getattr(checkpoint, direction)
                repeated_table = getattr(checkpoint_repeated, direction)

                # The equal-depth pooled reference makes the depth-averaged
                # ensemble biases sum exactly to zero across depths.
                pooled_bias = np.mean(
                    np.stack([table[d].mean_residual for d in report.depths]),
                    axis=0,
                )
                self.assertLess(float(np.linalg.norm(pooled_bias)), 2e-13)

                for depth in report.depths:
                    stats = table[depth]
                    stats_again = repeated_table[depth]
                    self.assertEqual(
                        stats.cross_depth_covariance.shape,
                        (depth, depth),
                    )
                    self.assertGreaterEqual(stats.variance, 0.0)
                    self.assertAlmostEqual(
                        stats.integrated_cross_depth_covariance,
                        stats.variance,
                        places=13,
                    )
                    self.assertAlmostEqual(
                        stats.rms * stats.rms,
                        stats.variance,
                        places=13,
                    )
                    np.testing.assert_array_equal(
                        stats.cross_depth_covariance,
                        stats_again.cross_depth_covariance,
                    )
                    np.testing.assert_array_equal(
                        stats.mean_residual,
                        stats_again.mean_residual,
                    )

                variance_slope = getattr(
                    checkpoint,
                    f"{direction}_variance_slope",
                )
                rms_slope = getattr(checkpoint, f"{direction}_rms_slope")
                bias_slope = getattr(checkpoint, f"{direction}_bias_slope")
                self.assertTrue(np.isfinite(variance_slope))
                self.assertTrue(np.isfinite(rms_slope))
                self.assertTrue(np.isfinite(bias_slope))
                self.assertAlmostEqual(
                    rms_slope,
                    0.5 * variance_slope,
                    places=12,
                )


class InvisibleContinuationTests(unittest.TestCase):
    def test_rank_one_attack_preserves_present_and_changes_future(self) -> None:
        spec = _spec(n=28, depth=3)
        master = initialize_gaussian_master(
            n_max=28,
            depth_max=3,
            input_dim=3,
            seed=3001,
        )
        initialization = materialize_coupled_state(master, spec)
        trained = simulate_checkpoints(
            initialization,
            spec,
            (0.0, 0.04),
            dt=0.01,
        ).final_state
        result = construct_invisible_perturbation(
            trained,
            initialization,
            spec,
            layer=1,
            alpha=1.0,
            restart_horizon=4e-4,
            restart_dt=1e-4,
            finite_difference_epsilon=5e-7,
            candidate_seed=17,
        )

        self.assertEqual(result.phi.shape, (28, 5))
        self.assertEqual(result.U.shape, (28, 1))
        self.assertEqual(result.A.shape, (1, 1))
        self.assertEqual(result.V.shape, (28, 1))
        np.testing.assert_allclose(
            result.delta_W,
            result.U @ result.A @ result.V.T,
            rtol=0.0,
            atol=0.0,
        )
        singular_values = np.linalg.svd(result.delta_W, compute_uv=False)
        self.assertAlmostEqual(float(singular_values[0]), 1.0, places=13)
        self.assertLess(float(singular_values[1]), 2e-15)

        fields = forward_adjoint(trained, spec)
        beta = fields.D[1] * fields.P[2]
        np.testing.assert_allclose(
            result.delta_W @ result.phi,
            0.0,
            atol=2e-13,
        )
        np.testing.assert_allclose(
            result.delta_W @ fields.H[1],
            0.0,
            atol=2e-13,
        )
        np.testing.assert_allclose(
            result.delta_W.T @ beta,
            0.0,
            atol=2e-13,
        )
        before_coefficients = retained_row_coefficients(
            trained.W[1],
            result.phi,
        )
        after_coefficients = retained_row_coefficients(
            result.perturbed_state.W[1],
            result.phi,
        )
        np.testing.assert_allclose(
            after_coefficients,
            before_coefficients,
            atol=3e-13,
        )

        for name in (
            "deltaW_Phi_fro",
            "deltaW_H_fro",
            "deltaW_T_beta_fro",
            "frobenius_norm_error",
        ):
            self.assertLess(result.constraint_defects[name], 5e-13)
        self.assertAlmostEqual(
            result.constraint_defects["entry_rms"],
            1.0 / spec.n,
            places=14,
        )
        self.assertAlmostEqual(
            result.constraint_defects["entry_rms_times_n_over_alpha"],
            1.0,
            places=14,
        )
        self.assertTrue(
            np.isfinite(
                result.constraint_defects["max_entry_times_n_over_alpha"]
            )
        )
        for defect in result.current_invariance_defects.values():
            self.assertLess(defect, 2e-11)

        self.assertIn("U[", result.selected_candidate)
        self.assertIn("|V[", result.selected_candidate)
        self.assertGreater(len(result.candidate_proxy_scores), 0)
        self.assertTrue(np.all(np.isfinite(result.dot_gram_difference)))
        self.assertGreater(result.dot_gram_norm, 1e-9)
        self.assertGreater(
            float(np.linalg.norm(result.restart_gram_difference[-1])),
            1e-12,
        )

        # A very short independent RK4 restart recovers the directly estimated
        # difference in the initial Gram velocity.
        restart_derivative = (
            result.restart_gram_difference[-1]
            / result.restart_times[-1]
        )
        np.testing.assert_allclose(
            restart_derivative,
            result.dot_gram_difference,
            rtol=3e-2,
            # Components whose first derivative is analytically zero retain
            # an O(horizon) second-order restart remainder.
            atol=4e-7,
        )
        np.testing.assert_allclose(
            result.restart_f_difference[0],
            0.0,
            atol=2e-13,
        )
        np.testing.assert_allclose(
            result.restart_gram_difference[0],
            0.0,
            atol=2e-13,
        )
        np.testing.assert_allclose(
            result.restart_theta_difference[0],
            0.0,
            atol=2e-13,
        )

    def test_degree_one_basis_requires_the_claimed_three_dimensional_labels(
        self,
    ) -> None:
        spec = _spec(n=8, depth=2)
        master = initialize_gaussian_master(
            n_max=8,
            depth_max=2,
            input_dim=3,
            seed=8,
        )
        state = materialize_coupled_state(master, spec)
        phi = empirical_degree_one_hermite_phi(state)
        np.testing.assert_allclose(
            phi[:, 0],
            np.full(8, 1.0 / np.sqrt(8.0)),
        )
        np.testing.assert_allclose(phi[:, 1:4], state.B / np.sqrt(8.0))
        np.testing.assert_allclose(phi[:, 4], state.a / np.sqrt(8.0))

        invalid = type(state)(
            B=state.B[:, :2],
            W=state.W,
            a=state.a,
        )
        with self.assertRaisesRegex(ValueError, "P=5"):
            empirical_degree_one_hermite_phi(invalid)


if __name__ == "__main__":
    unittest.main()
