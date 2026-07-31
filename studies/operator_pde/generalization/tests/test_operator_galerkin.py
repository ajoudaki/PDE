from __future__ import annotations

import dataclasses
import unittest

import numpy as np

from dense_pde.operator_galerkin import (
    PDESpec,
    PDEState,
    build_quadrature,
    build_hybrid_quadrature,
    build_tensor_quadrature,
    initialize,
    observe,
    solve_fields,
    transpose_pairing_defect,
    vector_field,
)


def small_spec(**updates) -> PDESpec:
    values = dict(
        X=np.eye(3),
        y=np.array([0.8, -0.55, 0.35]),
        basis_size=5,
        depth_nodes=4,
        base_points=32,
        fast_points=16,
        quadrature_seed=1234,
        sigma_w=0.65,
        A=1.0,
        gamma=1.0,
    )
    values.update(updates)
    return PDESpec(**values)


class OperatorGalerkinTests(unittest.TestCase):
    def test_static_cubature_moments(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        x = quadrature.base_latent
        self.assertLess(
            np.linalg.norm(
                np.sum(quadrature.base_weights[:, None] * x, axis=0)
            ),
            1e-12,
        )
        self.assertLess(
            np.linalg.norm(
                x.T @ (quadrature.base_weights[:, None] * x) - np.eye(4)
            ),
            1e-12,
        )
        self.assertLess(quadrature.whitened_basis_gram_error, 1e-11)
        self.assertLess(quadrature.fast_mean_error, 1e-11)
        self.assertLess(quadrature.fast_cov_error, 1e-11)

    def test_parseval_covariance(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        rng = np.random.default_rng(2)
        slow = rng.normal(size=spec.base_points)
        coefficients = quadrature.phi.T @ (
            quadrature.base_weights * slow
        )
        row = (
            spec.sigma_w * quadrature.epsilon[None, :, :]
            + state.c[0]
        )
        Wu = np.einsum("irp,p->ir", row, coefficients, optimize=True)
        observed = float(
            np.einsum(
                "i,r,ir,ir->",
                quadrature.base_weights,
                quadrature.fast_weights,
                Wu,
                Wu,
                optimize=True,
            )
        )
        expected = float(spec.sigma_w**2 * coefficients @ coefficients)
        self.assertLess(abs(observed - expected), 2e-13)

    def test_shared_transpose_pairing(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        rng = np.random.default_rng(3)
        state.c[:] = rng.normal(scale=0.1, size=state.c.shape)
        defect = transpose_pairing_defect(
            state,
            spec,
            quadrature,
            ell=2,
            slow_u=rng.normal(size=spec.base_points),
            fast_v=rng.normal(
                size=(spec.base_points, spec.fast_points)
            ),
        )
        self.assertLess(defect, 2e-13)

    def test_orientation_mutation_is_detected(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        rng = np.random.default_rng(314)
        state.c[:] = rng.normal(scale=0.15, size=state.c.shape)
        slow_u = rng.normal(size=spec.base_points)
        fast_v = rng.normal(size=(spec.base_points, spec.fast_points))
        ell = 1
        row = (
            spec.sigma_w * quadrature.epsilon[None, :, :]
            + state.c[ell]
        )
        ucoef = quadrature.phi.T @ (
            quadrature.base_weights * slow_u
        )
        Wu = np.einsum("irp,p->ir", row, ucoef, optimize=True)
        lhs = float(
            np.einsum(
                "i,r,ir,ir->",
                quadrature.base_weights,
                quadrature.fast_weights,
                Wu,
                fast_v,
                optimize=True,
            )
        )
        # Deliberately give the transpose an independently permuted fast-row
        # realization. A useful orientation audit must reject this mutation.
        wrong_row = np.roll(row, shift=3, axis=1)
        wrong_coeff = np.einsum(
            "i,r,irp,ir->p",
            quadrature.base_weights,
            quadrature.fast_weights,
            wrong_row,
            fast_v,
            optimize=True,
        )
        wrong_Wtv = quadrature.phi @ wrong_coeff
        wrong_rhs = float(
            np.einsum(
                "i,i,i->",
                quadrature.base_weights,
                slow_u,
                wrong_Wtv,
                optimize=True,
            )
        )
        self.assertGreater(abs(lhs - wrong_rhs), 1e-3)

    def test_output_kernel_identity_by_directional_difference(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        fields = solve_fields(state, spec, quadrature)
        obs = observe(state, spec, quadrature, fields)
        velocity, _ = vector_field(state, spec, quadrature, fields)
        step = 2e-7
        displaced = PDEState(
            B=state.B + step * velocity.B,
            a=state.a + step * velocity.a,
            c=state.c + step * velocity.c,
        )
        fdot = (observe(displaced, spec, quadrature).f - obs.f) / step
        predicted = -obs.theta @ (obs.f - spec.y)
        self.assertLess(np.linalg.norm(fdot - predicted), 2e-6)
        self.assertGreaterEqual(obs.theta_min, -1e-12)

    def test_zero_residual_freezes_every_characteristic(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        current_f = observe(state, spec, quadrature).f
        zero_spec = dataclasses.replace(spec, y=current_f)
        velocity, _ = vector_field(state, zero_spec, quadrature)
        self.assertEqual(float(np.max(np.abs(velocity.B))), 0.0)
        self.assertEqual(float(np.max(np.abs(velocity.a))), 0.0)
        self.assertEqual(float(np.max(np.abs(velocity.c))), 0.0)

    def test_positive_time_state_accepts_new_labels(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        state.c[:] = 0.03
        original_velocity, _ = vector_field(state, spec, quadrature)
        current_f = observe(state, spec, quadrature).f
        changed_spec = dataclasses.replace(
            spec,
            y=current_f + np.array([0.1, -0.05, 0.02]),
        )
        changed_velocity, _ = vector_field(state, changed_spec, quadrature)
        self.assertTrue(np.all(np.isfinite(changed_velocity.c)))
        self.assertGreater(
            np.linalg.norm(changed_velocity.c - original_velocity.c),
            1e-4,
        )

    def test_no_finite_network_weight_state(self) -> None:
        spec = small_spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        self.assertNotIn("n", {field.name for field in dataclasses.fields(spec)})
        self.assertEqual(
            {field.name for field in dataclasses.fields(state)},
            {"B", "a", "c"},
        )
        self.assertEqual(
            state.c.shape,
            (
                spec.depth_nodes,
                spec.base_points,
                spec.fast_points,
                spec.basis_size,
            ),
        )

    def test_tensor_gauss_hermite_realization(self) -> None:
        # 3^4 base nodes and 3^5 fast nodes for P=5.
        spec = small_spec(base_points=81, fast_points=243)
        quadrature = build_tensor_quadrature(
            spec, base_order=3, fast_order=3
        )
        self.assertLess(quadrature.raw_basis_gram_error, 1e-12)
        self.assertLess(quadrature.fast_mean_error, 1e-12)
        self.assertLess(quadrature.fast_cov_error, 1e-12)
        obs = observe(initialize(spec, quadrature), spec, quadrature)
        self.assertLess(np.linalg.norm(obs.f), 1e-12)

    def test_hybrid_complete_quadratic_basis_is_exact_and_nested(self) -> None:
        p5 = small_spec(
            basis_size=5,
            base_points=81,
            fast_points=128,
        )
        p15 = small_spec(
            basis_size=15,
            base_points=81,
            fast_points=128,
        )
        q5 = build_hybrid_quadrature(p5, base_order=3)
        q15 = build_hybrid_quadrature(p15, base_order=3)
        self.assertLess(q15.raw_basis_gram_error, 2e-12)
        self.assertEqual(q15.multi_indices[:5], q5.multi_indices)
        self.assertLess(np.max(np.abs(q15.phi[:, :5] - q5.phi)), 2e-12)
        self.assertLess(q15.fast_mean_error, 1e-12)
        self.assertLess(q15.fast_cov_error, 1e-11)


if __name__ == "__main__":
    unittest.main()
