from __future__ import annotations

import unittest

import numpy as np

from dense_pde import (
    PDESpec,
    build_hybrid_quadrature,
    initialize as initialize_pde,
    observe,
    rk4_step,
    vector_field,
)
from dense_reference import (
    ModelSpec,
    forward_adjoint,
    initialize as initialize_dense,
    rk4_param_step,
)


class StructuralControlTests(unittest.TestCase):
    def test_pde_sample_permutation_equivariance(self) -> None:
        X = np.array(
            [[1.0, 0.5, 0.2], [0.0, np.sqrt(0.75), -0.3], [0.0, 0.0, np.sqrt(0.87)]]
        )
        y = np.array([0.8, -0.55, 0.35])
        perm = np.array([2, 0, 1])
        spec = PDESpec(X, y, 5, 4, 81, 16, 333, activation="erf")
        permuted = PDESpec(
            X[:, perm],
            y[perm],
            5,
            4,
            81,
            16,
            333,
            activation="erf",
        )
        quadrature = build_hybrid_quadrature(spec)
        other_quadrature = build_hybrid_quadrature(permuted)
        np.testing.assert_array_equal(
            quadrature.base_latent, other_quadrature.base_latent
        )
        state = initialize_pde(spec, quadrature)
        obs = observe(state, spec, quadrature)
        obs_permuted = observe(state, permuted, other_quadrature)
        np.testing.assert_allclose(obs_permuted.f, obs.f[perm], atol=2e-13)
        np.testing.assert_allclose(
            obs_permuted.grams,
            obs.grams[:, perm][:, :, perm],
            atol=2e-13,
        )
        next_state = rk4_step(state, 0.02, spec, quadrature)
        next_permuted = rk4_step(
            state, 0.02, permuted, other_quadrature
        )
        np.testing.assert_allclose(next_permuted.B, next_state.B, atol=2e-13)
        np.testing.assert_allclose(next_permuted.a, next_state.a, atol=2e-13)
        np.testing.assert_allclose(next_permuted.c, next_state.c, atol=2e-13)

    def test_duplicate_conflicting_inputs_have_irreducible_loss(self) -> None:
        X = np.array([[1.0, 1.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 0.0]])
        y = np.array([0.8, -0.4, 0.35])
        lower_bound = (y[0] - y[1]) ** 2 / 4.0

        pde_spec = PDESpec(X, y, 5, 6, 81, 32, 444)
        quadrature = build_hybrid_quadrature(pde_spec)
        pde_state = initialize_pde(pde_spec, quadrature)
        for _ in range(100):
            pde_state = rk4_step(pde_state, 0.02, pde_spec, quadrature)
        pde_obs = observe(pde_state, pde_spec, quadrature)
        self.assertLess(abs(pde_obs.f[0] - pde_obs.f[1]), 2e-13)
        self.assertGreaterEqual(pde_obs.loss + 2e-13, lower_bound)

        dense_spec = ModelSpec(24, 8, X, y, 445)
        dense_state = initialize_dense(dense_spec)
        for _ in range(100):
            dense_state = rk4_param_step(dense_state, 0.02, dense_spec)
        fields = forward_adjoint(dense_state, dense_spec)
        dense_f = dense_state.a @ fields.H[-1] / dense_spec.n
        dense_loss = 0.5 * np.sum((dense_f - y) ** 2)
        self.assertLess(abs(dense_f[0] - dense_f[1]), 2e-13)
        self.assertGreaterEqual(dense_loss + 2e-13, lower_bound)

    def test_zero_label_pde_null_is_explicitly_trivial(self) -> None:
        X = np.eye(3)
        spec = PDESpec(X, np.zeros(3), 5, 4, 81, 16, 555)
        quadrature = build_hybrid_quadrature(spec)
        state = initialize_pde(spec, quadrature)
        velocity, _ = vector_field(state, spec, quadrature)
        self.assertLess(float(np.max(np.abs(velocity.B))), 1e-14)
        self.assertLess(float(np.max(np.abs(velocity.a))), 1e-14)
        self.assertLess(float(np.max(np.abs(velocity.c))), 1e-14)


if __name__ == "__main__":
    unittest.main()
