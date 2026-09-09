from __future__ import annotations

from pathlib import Path
import sys
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "source"))

from cross_p import (  # noqa: E402
    basis_diagnostic,
    build_nested_quadratures,
    build_subspace_basis,
    generator_diagnostics,
    hermite_subspace,
    lift_state,
    project_state,
    random_subspace,
    restrict_to_subspace,
    shadow_restart,
    state_difference_norm,
    trajectory_pod_subspace,
    weighted_state_norm,
)
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    initialize,
    rk4_step,
    vector_field,
)


def small_family():
    template = PDESpec(
        X=np.array([[1.0, -0.4]]),
        y=np.array([0.7, -0.25]),
        basis_size=2,
        depth_nodes=2,
        base_points=16,
        fast_points=16,
        quadrature_seed=90210,
        sigma_w=0.45,
        gamma=0.7,
        activation="tanh",
    )
    return build_nested_quadratures(
        template, levels=(2, 4, 7), base_order=4
    )


class NestedQuadratureTests(unittest.TestCase):
    def test_literal_prefixes_and_every_declared_covariance(self) -> None:
        family = small_family()
        qmax = family.quadrature(7)
        self.assertEqual(family.raw_epsilon.shape, (16, 7))
        for level in family.levels:
            with self.subTest(level=level):
                quadrature = family.quadrature(level)
                np.testing.assert_array_equal(
                    quadrature.base_latent, qmax.base_latent
                )
                np.testing.assert_array_equal(
                    quadrature.phi, qmax.phi[:, :level]
                )
                np.testing.assert_array_equal(
                    quadrature.epsilon, qmax.epsilon[:, :level]
                )
                phi_gram = quadrature.phi.T @ (
                    quadrature.base_weights[:, None] * quadrature.phi
                )
                epsilon_mean = np.sum(
                    quadrature.fast_weights[:, None] * quadrature.epsilon,
                    axis=0,
                )
                epsilon_cov = quadrature.epsilon.T @ (
                    quadrature.fast_weights[:, None] * quadrature.epsilon
                )
                np.testing.assert_allclose(
                    phi_gram, np.eye(level), rtol=0.0, atol=2e-13
                )
                np.testing.assert_allclose(
                    epsilon_mean, 0.0, rtol=0.0, atol=2e-13
                )
                np.testing.assert_allclose(
                    epsilon_cov, np.eye(level), rtol=0.0, atol=2e-13
                )

    def test_scientific_default_has_order_four_256_point_base(self) -> None:
        template = PDESpec(
            X=np.eye(3),
            y=np.array([0.8, -0.55, 0.35]),
            basis_size=5,
            depth_nodes=1,
            base_points=256,
            fast_points=64,
            quadrature_seed=11,
        )
        family = build_nested_quadratures(template)
        self.assertEqual(family.levels, (5, 15, 35))
        self.assertEqual(family.quadrature(35).base_latent.shape, (256, 4))
        self.assertLess(
            family.quadrature(35).whitened_basis_gram_error, 2e-12
        )
        self.assertLess(family.quadrature(35).fast_cov_error, 2e-12)

    def test_predeclared_master_makes_later_extension_byte_stable(self) -> None:
        template = PDESpec(
            X=np.array([[1.0, -0.4]]),
            y=np.array([0.7, -0.25]),
            basis_size=2,
            depth_nodes=2,
            base_points=16,
            fast_points=16,
            quadrature_seed=4401,
            sigma_w=0.45,
            gamma=0.7,
            activation="tanh",
        )
        early = build_nested_quadratures(
            template,
            levels=(2, 4),
            master_levels=(2, 4, 7),
            base_order=4,
        )
        extended = build_nested_quadratures(
            template,
            levels=(2, 4, 7),
            master_levels=(2, 4, 7),
            base_order=4,
        )
        self.assertEqual(early.master_levels, (2, 4, 7))
        for level in (2, 4):
            np.testing.assert_array_equal(
                early.quadrature(level).phi,
                extended.quadrature(level).phi,
            )
            np.testing.assert_array_equal(
                early.quadrature(level).epsilon,
                extended.quadrature(level).epsilon,
            )


class StateMapAndGeneratorTests(unittest.TestCase):
    def test_projection_lift_and_weighted_norm(self) -> None:
        family = small_family()
        q7 = family.quadrature(7)
        state = initialize(family.spec(7), q7)
        rng = np.random.default_rng(44)
        state.c[:] = rng.normal(scale=0.03, size=state.c.shape)
        low = project_state(state, 4)
        lifted = lift_state(low, 7)
        np.testing.assert_array_equal(low.B, state.B)
        np.testing.assert_array_equal(low.a, state.a)
        np.testing.assert_array_equal(low.c, state.c[..., :4])
        np.testing.assert_array_equal(lifted.c[..., :4], low.c)
        np.testing.assert_array_equal(lifted.c[..., 4:], 0.0)
        self.assertGreater(weighted_state_norm(state, q7), 0.0)
        tail = state.copy()
        tail.c[..., :4] = 0.0
        tail.B[:] = 0.0
        tail.a[:] = 0.0
        self.assertAlmostEqual(
            state_difference_norm(state, lifted, q7),
            weighted_state_norm(tail, q7),
            places=14,
        )
        wrong_level = PDEState(
            B=state.B.copy(),
            a=state.a.copy(),
            c=state.c[..., :6].copy(),
        )
        with self.assertRaisesRegex(ValueError, "level"):
            weighted_state_norm(wrong_level, q7)

    def test_zero_defects_when_p_equals_pmax(self) -> None:
        family = small_family()
        spec = family.spec(7)
        quadrature = family.quadrature(7)
        state = initialize(spec, quadrature)
        rng = np.random.default_rng(7)
        state.c[:] = rng.normal(scale=0.015, size=state.c.shape)
        diagnostics = generator_diagnostics(
            state,
            state.copy(),
            spec,
            spec,
            quadrature,
            quadrature,
        )
        self.assertEqual(diagnostics.lift_consistency.total, 0.0)
        self.assertEqual(diagnostics.lift_outgoing_high_cdot, 0.0)
        self.assertEqual(diagnostics.outgoing_high_cdot, 0.0)
        self.assertEqual(diagnostics.high_to_low_feedback.total, 0.0)
        self.assertEqual(diagnostics.lift_observable_defect.total, 0.0)
        self.assertEqual(diagnostics.feedback_observable_defect.total, 0.0)
        self.assertEqual(diagnostics.lift_full_observable_defect.total, 0.0)
        self.assertEqual(
            diagnostics.feedback_full_observable_defect.total, 0.0
        )

    def test_cross_level_diagnostics_and_shadow_are_finite(self) -> None:
        family = small_family()
        high_spec = family.spec(7)
        high_q = family.quadrature(7)
        high = initialize(high_spec, high_q)
        high = rk4_step(high, 0.01, high_spec, high_q)
        low = project_state(high, 4)
        diagnostics = generator_diagnostics(
            low,
            high,
            family.spec(4),
            high_spec,
            family.quadrature(4),
            high_q,
        )
        values = (
            diagnostics.lift_consistency.total,
            diagnostics.lift_outgoing_high_cdot,
            diagnostics.outgoing_high_cdot,
            diagnostics.high_to_low_feedback.total,
            diagnostics.lift_observable_defect.total,
            diagnostics.feedback_observable_defect.total,
            diagnostics.lift_full_observable_defect.total,
            diagnostics.feedback_full_observable_defect.total,
        )
        self.assertTrue(np.all(np.isfinite(values)))
        shadow = shadow_restart(
            high,
            family.spec(4),
            high_spec,
            family.quadrature(4),
            high_q,
            dt=0.005,
            steps=2,
        )
        self.assertEqual(shadow.times.shape, (3,))
        self.assertTrue(np.all(np.isfinite(shadow.state_defect)))
        self.assertTrue(np.all(np.isfinite(shadow.f_defect)))
        self.assertTrue(np.all(np.isfinite(shadow.loss_defect)))
        self.assertTrue(np.all(np.isfinite(shadow.gram_defect)))


class BasisDiagnosticTests(unittest.TestCase):
    def test_three_basis_families_are_orthonormal_and_restrict(self) -> None:
        family = small_family()
        spec = family.spec(7)
        quadrature = family.quadrature(7)
        state = initialize(spec, quadrature)
        state = rk4_step(state, 0.015, spec, quadrature)
        velocity, _ = vector_field(state, spec, quadrature)
        bases = {
            "hermite": hermite_subspace(7, 4),
            "random": random_subspace(7, 4, seed=123),
            "pod": trajectory_pod_subspace(
                (state,), quadrature, 4, operators=(velocity,)
            ),
            "dispatch": build_subspace_basis(
                "trajectory-pod",
                pmax=7,
                rank=4,
                states=(state,),
                operators=(velocity,),
                quadrature=quadrature,
            ),
        }
        for name, basis in bases.items():
            with self.subTest(name=name):
                np.testing.assert_allclose(
                    basis.T @ basis, np.eye(4), rtol=0.0, atol=2e-13
                )
                restricted = restrict_to_subspace(
                    state, spec, quadrature, basis
                )
                self.assertEqual(restricted.state.c.shape[-1], 4)
                phi_gram = restricted.quadrature.phi.T @ (
                    restricted.quadrature.base_weights[:, None]
                    * restricted.quadrature.phi
                )
                np.testing.assert_allclose(
                    phi_gram, np.eye(4), rtol=0.0, atol=3e-13
                )
                diagnostic = basis_diagnostic(
                    state, spec, quadrature, basis
                )
                self.assertTrue(
                    np.all(
                        np.isfinite(
                            [
                                diagnostic.state_tail,
                                diagnostic.generator_tail,
                                diagnostic.feedback.total,
                                diagnostic.observable_defect.total,
                            ]
                        )
                    )
                )

    def test_full_basis_has_exact_zero_defect(self) -> None:
        family = small_family()
        spec = family.spec(7)
        quadrature = family.quadrature(7)
        state = initialize(spec, quadrature)
        state = rk4_step(state, 0.01, spec, quadrature)
        diagnostic = basis_diagnostic(
            state, spec, quadrature, hermite_subspace(7, 7)
        )
        self.assertEqual(diagnostic.state_tail, 0.0)
        self.assertEqual(diagnostic.generator_tail, 0.0)
        self.assertEqual(diagnostic.feedback.total, 0.0)
        self.assertEqual(diagnostic.observable_defect.total, 0.0)


if __name__ == "__main__":
    unittest.main()
