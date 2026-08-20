from __future__ import annotations

import unittest

import numpy as np

from dense_reference import (
    FieldState,
    ModelSpec,
    forward_adjoint,
    initialize,
    parameter_vector_field,
    tangent_kernel,
)


class DenseReferenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = ModelSpec(
            n=12,
            depth=4,
            X=np.eye(3),
            y=np.array([0.8, -0.55, 0.35]),
            seed=9182,
        )
        self.state = initialize(self.spec)

    def loss(self, state) -> float:
        fields = forward_adjoint(state, self.spec)
        residual = state.a @ fields.H[-1] / self.spec.n - self.spec.y
        return float(0.5 * residual @ residual)

    def test_vector_field_is_scaled_euclidean_gradient(self) -> None:
        velocity = parameter_vector_field(self.state, self.spec)
        rng = np.random.default_rng(12)
        directions = {
            "B": rng.normal(size=self.state.B.shape),
            "W": rng.normal(size=self.state.W.shape),
            "a": rng.normal(size=self.state.a.shape),
        }
        epsilon = 2e-6
        for name, direction in directions.items():
            plus = type(self.state)(
                self.state.B.copy(),
                self.state.W.copy(),
                self.state.a.copy(),
            )
            minus = type(self.state)(
                self.state.B.copy(),
                self.state.W.copy(),
                self.state.a.copy(),
            )
            setattr(plus, name, getattr(plus, name) + epsilon * direction)
            setattr(minus, name, getattr(minus, name) - epsilon * direction)
            derivative = (self.loss(plus) - self.loss(minus)) / (2 * epsilon)
            multiplier = {
                "B": self.spec.n,
                "W": self.spec.depth,
                "a": self.spec.n,
            }[name]
            predicted = -float(
                np.sum(getattr(velocity, name) * direction)
            ) / multiplier
            self.assertLess(abs(derivative - predicted), 3e-8)

    def test_tangent_kernel_matches_output_velocity(self) -> None:
        fields = forward_adjoint(self.state, self.spec)
        residual = self.state.a @ fields.H[-1] / self.spec.n - self.spec.y
        theta = tangent_kernel(
            FieldState(self.state.W, self.state.a, fields.H, fields.P),
            self.spec,
        )
        velocity = parameter_vector_field(self.state, self.spec)
        step = 2e-7
        displaced = type(self.state)(
            self.state.B + step * velocity.B,
            self.state.W + step * velocity.W,
            self.state.a + step * velocity.a,
        )
        fields_next = forward_adjoint(displaced, self.spec)
        f = self.state.a @ fields.H[-1] / self.spec.n
        f_next = displaced.a @ fields_next.H[-1] / self.spec.n
        self.assertLess(np.linalg.norm((f_next - f) / step + theta @ residual), 2e-5)
        self.assertGreaterEqual(np.linalg.eigvalsh(theta)[0], -1e-12)


if __name__ == "__main__":
    unittest.main()
