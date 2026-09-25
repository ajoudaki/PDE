"""Tiny deterministic algebra checks; not an empirical training campaign."""

import unittest
from unittest.mock import patch

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal
from scipy.integrate import solve_ivp

import scalar_aggregate_engine as engine


def shifted(params, direction, amount):
    return tuple(a + amount * b for a, b in zip(params, direction))


class TestScalarAggregateEngine(unittest.TestCase):
    def setUp(self):
        self.inputs = np.array([[0.7, -0.2], [0.1, 0.9]])
        self.labels = np.array([0.6, -0.3])

    def parameters(self, depth=3):
        params = engine.initialize_network(4, 2, depth, seed=81 + depth)
        return (*params[:-1], np.array([0.3, -0.2, 0.4, 0.1]))

    def test_exact_initialization_draw_order_and_parameter_roundtrip(self):
        for depth in (2, 3):
            params = engine.initialize_network(4, 2, depth, seed=19)
            rng = np.random.default_rng(19)
            expected = (rng.standard_normal((4, 2)),
                        *(rng.standard_normal((4, 4)) / 2 for _ in range(depth - 1)),
                        rng.standard_normal(4) / 4)
            for actual, reference in zip(params, expected):
                assert_array_equal(actual, reference)
            shapes = tuple(p.shape for p in params)
            recovered = engine.unflatten_network(engine.flatten_network(params), shapes)
            for actual, reference in zip(recovered, params):
                assert_array_equal(actual, reference)

    def test_physical_gradients_kernel_and_dense_velocity(self):
        for depth in (2, 3):
            params = self.parameters(depth)
            shapes = tuple(p.shape for p in params)
            flat = engine.flatten_network(params)
            n = len(params[-1])
            mobility = engine.flatten_network((np.full_like(params[0], n),
                        *(np.ones_like(p) for p in params[1:-1]), np.full_like(params[-1], n)))
            numerical_jacobian = np.empty((len(self.inputs), len(flat)))
            eps = 2e-6
            for index in range(len(flat)):
                perturbation = np.zeros_like(flat)
                perturbation[index] = eps
                plus = engine.network_fields(engine.unflatten_network(flat + perturbation, shapes), self.inputs)["f"]
                minus = engine.network_fields(engine.unflatten_network(flat - perturbation, shapes), self.inputs)["f"]
                numerical_jacobian[:, index] = (plus - minus) / (2 * eps)
            fields = engine.network_fields(params, self.inputs)
            directions = np.array([engine.flatten_network(engine.sample_direction(params, self.inputs, a))
                                   for a in range(len(self.inputs))])
            assert_allclose(directions, numerical_jacobian * mobility, rtol=2e-6, atol=2e-9)
            assert_allclose(fields["Theta"], (numerical_jacobian * mobility) @ numerical_jacobian.T,
                            rtol=2e-6, atol=2e-9)
            dense_velocity = engine.flatten_network(engine.network_rhs(params, self.inputs, self.labels))
            expected_velocity = -2 / len(self.inputs) * ((fields["f"] - self.labels) @ directions)
            assert_allclose(dense_velocity, expected_velocity, rtol=2e-14, atol=2e-14)
            assert_allclose(numerical_jacobian @ dense_velocity,
                            -2 / len(self.inputs) * fields["Theta"] @ (fields["f"] - self.labels),
                            rtol=2e-6, atol=2e-9)

    def test_first_and_ordered_second_directional_coefficients(self):
        for depth in (2, 3):
            params = self.parameters(depth)
            coefficients = engine.initialize_coefficients(params, self.inputs, order=4)
            self.assertEqual(set(coefficients), {"f", "Theta", "C", "Q"})
            assert_allclose(coefficients["Theta"], coefficients["Theta"].T, atol=2e-14)
            assert_allclose(coefficients["C"], coefficients["C"].swapaxes(0, 1), atol=2e-14)
            assert_allclose(coefficients["Q"], coefficients["Q"].swapaxes(0, 1), atol=2e-14)
            eps = 2e-5
            for d in range(len(self.inputs)):
                gd = engine.sample_direction(params, self.inputs, d)
                plus_params, minus_params = shifted(params, gd, eps), shifted(params, gd, -eps)
                plus = engine.initialize_coefficients(plus_params, self.inputs, order=3)
                minus = engine.initialize_coefficients(minus_params, self.inputs, order=3)
                assert_allclose(coefficients["C"][:, :, d], (plus["Theta"] - minus["Theta"]) / (2 * eps),
                                rtol=3e-6, atol=2e-9)
                # C must be recomputed at each perturbed state: g_c moves too.
                assert_allclose(coefficients["Q"][:, :, :, d], (plus["C"] - minus["C"]) / (2 * eps),
                                rtol=4e-6, atol=3e-9)
                for c in range(len(self.inputs)):
                    exact = engine.direction_derivative(params, self.inputs, c, gd)
                    plus_gc = engine.sample_direction(plus_params, self.inputs, c)
                    minus_gc = engine.sample_direction(minus_params, self.inputs, c)
                    for value, vp, vm in zip(exact, plus_gc, minus_gc):
                        assert_allclose(value, (vp - vm) / (2 * eps), rtol=4e-6, atol=3e-9)
            # The ordered derivative indices are not Hessian-symmetric.
            self.assertGreater(np.linalg.norm(coefficients["Q"] - coefficients["Q"].swapaxes(2, 3)), 1e-7)

    def test_moving_direction_term_is_present(self):
        params = self.parameters(3)
        coefficients = engine.initialize_coefficients(params, self.inputs, order=4)
        gc = engine.sample_direction(params, self.inputs, 0)
        gd = engine.sample_direction(params, self.inputs, 1)
        moving = engine.direction_derivative(params, self.inputs, 0, gd)
        eps = 2e-4
        fixed_hessian = np.zeros((2, 2))
        for sign_c in (-1, 1):
            for sign_d in (-1, 1):
                perturbed = tuple(p + eps * sign_c * c + eps * sign_d * d
                                  for p, c, d in zip(params, gc, gd))
                fixed_hessian += sign_c * sign_d * engine.network_fields(perturbed, self.inputs)["Theta"]
        fixed_hessian /= 4 * eps ** 2
        moving_term = (engine.network_fields(shifted(params, moving, eps), self.inputs)["Theta"]
                       - engine.network_fields(shifted(params, moving, -eps), self.inputs)["Theta"]) / (2 * eps)
        self.assertGreater(np.linalg.norm(moving_term), 1e-5)
        assert_allclose(coefficients["Q"][:, :, 0, 1], fixed_hessian + moving_term,
                        rtol=3e-5, atol=1e-8)

    def test_scalar_rhs_contract_counts_and_zero_residual(self):
        coefficients = engine.initialize_coefficients(self.parameters(), self.inputs)
        for order in (2, 3, 4):
            model = engine.ScalarHierarchy(coefficients, self.labels, order)
            state = model.initial_state()
            original = state.copy()
            tensors = model.tensors(state)
            self.assertEqual(state.size, sum(2 ** degree for degree in range(1, order)))
            self.assertEqual(model.counts()["aggregate_scalars"], sum(2 ** degree for degree in range(1, order + 1)))
            self.assertEqual(model.counts()["neuron_scalars"], 0)
            self.assertEqual(model.counts()["network_parameter_scalars"], 0)
            assert_array_equal(model.pack(model.unpack(state)), state)
            with patch.object(engine, "_plain_fields", side_effect=AssertionError("neuron access")), \
                 patch.object(engine, "_jet_fields", side_effect=AssertionError("neuron access")):
                derivative = model.unpack(model.rhs(0.0, state))
                assert_array_equal(model.rhs(0.0, state), model.rhs(17.0, state))
            for current, following in zip(model.all_names[:-1], model.all_names[1:]):
                expected = -np.tensordot(tensors[following], tensors["f"] - self.labels, axes=([-1], [0]))
                assert_allclose(derivative[current], expected, atol=0, rtol=0)
            assert_array_equal(state, original)
            self.assertFalse(model.terminal.flags.writeable)
            owned_arrays = {key for key, value in vars(model).items() if isinstance(value, np.ndarray)}
            self.assertEqual(owned_arrays, {"labels", "terminal", "_initial"})
            stationary = engine.ScalarHierarchy(coefficients, coefficients["f"], order)
            assert_array_equal(stationary.rhs(0.0, stationary.initial_state()), np.zeros(stationary.size))

    def test_scalar_copy_isolation_and_restart(self):
        coefficients = engine.initialize_coefficients(self.parameters(), self.inputs)
        for order in (2, 3, 4):
            source = {name: value.copy() for name, value in coefficients.items()}
            labels = self.labels.copy()
            model = engine.ScalarHierarchy(source, labels, order)
            initial, terminal = model.initial_state(), model.terminal.copy()
            for value in source.values():
                value.fill(999)
            labels.fill(999)
            assert_array_equal(model.initial_state(), initial)
            assert_array_equal(model.terminal, terminal)
            options = dict(method="DOP853", rtol=1e-11, atol=1e-13)
            full = solve_ivp(model.rhs, (0.0, 0.06), initial, **options)
            left = solve_ivp(model.rhs, (0.0, 0.03), initial, **options)
            right = solve_ivp(model.rhs, (0.03, 0.06), left.y[:, -1], **options)
            self.assertTrue(full.success and left.success and right.success)
            assert_allclose(full.y[:, -1], right.y[:, -1], rtol=1e-10, atol=1e-12)
            assert_array_equal(model.terminal, terminal)

    def test_reject_malformed_inputs(self):
        params = self.parameters()
        for order in (1, 5, True, 3.5):
            with self.assertRaises(ValueError):
                engine.initialize_coefficients(params, self.inputs, order)
        with self.assertRaises(ValueError):
            engine.network_fields(params, np.ones((2, 3)))
        with self.assertRaises(ValueError):
            engine.sample_direction(params, self.inputs, -1)
        with self.assertRaises(ValueError):
            engine.direction_derivative(params, self.inputs, 0, params[:-1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
