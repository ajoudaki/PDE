from __future__ import annotations

import unittest

import numpy as np
from scipy.special import erf

from activations import ACTIVATIONS, ACTIVATION_NAMES, get_activation
from dense_pde import (
    PDESpec,
    PDEState,
    build_quadrature,
    initialize as initialize_pde,
    observe,
    vector_field,
)
from dense_reference import (
    FieldState,
    ModelSpec,
    ParamState,
    forward_adjoint,
    initialize as initialize_dense,
    parameter_vector_field,
    tangent_kernel,
)


def _dataset(m: int, d: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """Deterministic nonorthogonal data with mixed-sign labels."""

    rng = np.random.default_rng(4100 + 17 * m + d)
    X = rng.normal(size=(d, m))
    X /= np.linalg.norm(X, axis=0, keepdims=True)
    y = ((-1.0) ** np.arange(m)) * np.linspace(0.35, 0.9, m)
    return X, y


def _dense_loss(state: ParamState, spec: ModelSpec) -> float:
    fields = forward_adjoint(state, spec)
    residual = state.a @ fields.H[-1] / spec.n - spec.y
    return float(0.5 * residual @ residual)


class ActivationRegistryTests(unittest.TestCase):
    def test_registry_is_closed_and_formulas_are_normalized(self) -> None:
        self.assertEqual(ACTIVATION_NAMES, ("tanh", "erf", "atan"))
        self.assertEqual(set(ACTIVATIONS), set(ACTIVATION_NAMES))
        with self.assertRaises(TypeError):
            ACTIVATIONS["relu"] = ACTIVATIONS["tanh"]  # type: ignore[index]
        z = np.linspace(-2.25, 2.25, 19)
        expected = {
            "tanh": np.tanh(z),
            "erf": erf(0.5 * np.sqrt(np.pi) * z),
            "atan": (2.0 / np.pi) * np.arctan(0.5 * np.pi * z),
        }
        for name in ACTIVATION_NAMES:
            with self.subTest(activation=name):
                activation = get_activation(name)
                np.testing.assert_allclose(
                    activation.value(z), expected[name], rtol=0.0, atol=0.0
                )
                self.assertEqual(float(activation.value(np.array([0.0]))[0]), 0.0)
                self.assertEqual(
                    float(activation.derivative(np.array([0.0]))[0]), 1.0
                )

    def test_exact_derivatives_match_centered_differences(self) -> None:
        z = np.linspace(-3.0, 3.0, 31)
        step = 2e-6
        for name in ACTIVATION_NAMES:
            with self.subTest(activation=name):
                activation = get_activation(name)
                finite_difference = (
                    activation.value(z + step) - activation.value(z - step)
                ) / (2.0 * step)
                np.testing.assert_allclose(
                    activation.derivative(z),
                    finite_difference,
                    rtol=2e-9,
                    atol=3e-11,
                )

    def test_unknown_or_aliased_activation_is_rejected(self) -> None:
        X, y = _dataset(3)
        for invalid in ("relu", "TANH", ""):
            with self.subTest(implementation="dense", activation=invalid):
                with self.assertRaisesRegex(ValueError, "unknown activation"):
                    ModelSpec(
                        n=8,
                        depth=3,
                        X=X,
                        y=y,
                        seed=1,
                        activation=invalid,
                    ).validate()
            with self.subTest(implementation="pde", activation=invalid):
                with self.assertRaisesRegex(ValueError, "unknown activation"):
                    PDESpec(
                        X=X,
                        y=y,
                        basis_size=X.shape[0] + 2,
                        depth_nodes=3,
                        base_points=16,
                        fast_points=8,
                        activation=invalid,
                    ).validate()

    def test_default_remains_tanh(self) -> None:
        X, y = _dataset(2)
        dense = ModelSpec(n=4, depth=2, X=X, y=y, seed=5)
        pde = PDESpec(
            X=X,
            y=y,
            basis_size=X.shape[0] + 2,
            depth_nodes=2,
            base_points=16,
            fast_points=8,
        )
        self.assertEqual(dense.activation, "tanh")
        self.assertEqual(pde.activation, "tanh")


class CrossConfigurationIdentityTests(unittest.TestCase):
    def test_dense_scaled_gradient_and_kernel_identities(self) -> None:
        for m in range(2, 6):
            X, y = _dataset(m)
            for activation_name in ACTIVATION_NAMES:
                with self.subTest(m=m, activation=activation_name):
                    spec = ModelSpec(
                        n=8,
                        depth=3,
                        X=X,
                        y=y,
                        seed=900 + m,
                        activation=activation_name,
                    )
                    state = initialize_dense(spec)
                    fields = forward_adjoint(state, spec)
                    residual = (
                        state.a @ fields.H[-1] / spec.n - spec.y
                    )
                    velocity = parameter_vector_field(state, spec)
                    rng = np.random.default_rng(1200 + m)
                    directions = {
                        "B": rng.normal(size=state.B.shape),
                        "W": rng.normal(size=state.W.shape),
                        "a": rng.normal(size=state.a.shape),
                    }
                    step = 1e-6
                    for name, direction in directions.items():
                        plus = ParamState(
                            B=state.B.copy(),
                            W=state.W.copy(),
                            a=state.a.copy(),
                        )
                        minus = ParamState(
                            B=state.B.copy(),
                            W=state.W.copy(),
                            a=state.a.copy(),
                        )
                        setattr(
                            plus,
                            name,
                            getattr(plus, name) + step * direction,
                        )
                        setattr(
                            minus,
                            name,
                            getattr(minus, name) - step * direction,
                        )
                        derivative = (
                            _dense_loss(plus, spec)
                            - _dense_loss(minus, spec)
                        ) / (2.0 * step)
                        multiplier = {
                            "B": spec.n,
                            "W": spec.depth,
                            "a": spec.n,
                        }[name]
                        predicted = -float(
                            np.sum(getattr(velocity, name) * direction)
                        ) / multiplier
                        self.assertLess(
                            abs(derivative - predicted),
                            2e-7 * max(1.0, abs(predicted)),
                        )

                    theta = tangent_kernel(
                        FieldState(state.W, state.a, fields.H, fields.P),
                        spec,
                    )
                    plus = ParamState(
                        B=state.B + step * velocity.B,
                        W=state.W + step * velocity.W,
                        a=state.a + step * velocity.a,
                    )
                    minus = ParamState(
                        B=state.B - step * velocity.B,
                        W=state.W - step * velocity.W,
                        a=state.a - step * velocity.a,
                    )
                    f_plus_fields = forward_adjoint(plus, spec)
                    f_minus_fields = forward_adjoint(minus, spec)
                    f_plus = plus.a @ f_plus_fields.H[-1] / spec.n
                    f_minus = minus.a @ f_minus_fields.H[-1] / spec.n
                    fdot = (f_plus - f_minus) / (2.0 * step)
                    np.testing.assert_allclose(
                        fdot,
                        -theta @ residual,
                        rtol=2e-7,
                        atol=2e-8,
                    )
                    self.assertGreaterEqual(
                        float(np.linalg.eigvalsh(theta)[0]), -1e-12
                    )

    def test_pde_output_kernel_identity_and_psd(self) -> None:
        for m in range(2, 6):
            X, y = _dataset(m)
            for activation_name in ACTIVATION_NAMES:
                with self.subTest(m=m, activation=activation_name):
                    spec = PDESpec(
                        X=X,
                        y=y,
                        basis_size=X.shape[0] + 2,
                        depth_nodes=3,
                        base_points=16,
                        fast_points=8,
                        quadrature_seed=2000 + m,
                        activation=activation_name,
                    )
                    quadrature = build_quadrature(spec)
                    state = initialize_pde(spec, quadrature)
                    rng = np.random.default_rng(2400 + m)
                    state.B += rng.normal(scale=0.02, size=state.B.shape)
                    state.a += rng.normal(scale=0.02, size=state.a.shape)
                    state.c += rng.normal(scale=0.025, size=state.c.shape)
                    observable = observe(state, spec, quadrature)
                    velocity, _ = vector_field(state, spec, quadrature)
                    step = 2e-7
                    plus = PDEState(
                        B=state.B + step * velocity.B,
                        a=state.a + step * velocity.a,
                        c=state.c + step * velocity.c,
                    )
                    minus = PDEState(
                        B=state.B - step * velocity.B,
                        a=state.a - step * velocity.a,
                        c=state.c - step * velocity.c,
                    )
                    fdot = (
                        observe(plus, spec, quadrature).f
                        - observe(minus, spec, quadrature).f
                    ) / (2.0 * step)
                    predicted = -observable.theta @ (
                        observable.f - spec.y
                    )
                    np.testing.assert_allclose(
                        fdot, predicted, rtol=5e-7, atol=3e-8
                    )
                    self.assertGreaterEqual(observable.theta_min, -1e-12)
                    np.testing.assert_allclose(
                        observable.loss_dot,
                        -(
                            (observable.f - spec.y)
                            @ observable.theta
                            @ (observable.f - spec.y)
                        ),
                        rtol=2e-14,
                        atol=2e-14,
                    )

    def test_p_equals_d_plus_two_is_complete_linear_basis(self) -> None:
        for m in range(2, 6):
            d = m
            X, y = _dataset(m, d=d)
            expected_indices = [(0,) * (d + 1)]
            expected_indices.extend(
                tuple(int(k == coordinate) for k in range(d + 1))
                for coordinate in range(d + 1)
            )
            for activation_name in ACTIVATION_NAMES:
                with self.subTest(m=m, activation=activation_name):
                    spec = PDESpec(
                        X=X,
                        y=y,
                        basis_size=d + 2,
                        depth_nodes=2,
                        base_points=16,
                        fast_points=16,
                        quadrature_seed=3000 + m,
                        activation=activation_name,
                    )
                    quadrature = build_quadrature(spec)
                    self.assertEqual(
                        quadrature.multi_indices, tuple(expected_indices)
                    )
                    expected_values = np.column_stack(
                        (
                            np.ones(spec.base_points),
                            quadrature.base_latent,
                        )
                    )
                    np.testing.assert_allclose(
                        quadrature.phi,
                        expected_values,
                        rtol=0.0,
                        atol=2e-12,
                    )


if __name__ == "__main__":
    unittest.main()
