"""Small independent checks of finite-network normalization and dynamics."""

import unittest

import numpy as np

from pde import (
    ARCTAN, IDENTITY, TANH, Activation, Parameters, backward, flow_velocity,
    forward, gd_step, initialize, kernel, kernel_blocks, loss, loss_gradients,
)


SHIFTED = Activation("shifted_arctan", lambda z: 1.0 + np.arctan(z) / 10.0,
                     lambda z: 0.1 / (1.0 + z * z))


def blocks(parameters):
    return parameters.weights + (parameters.readout,)


def replaced(parameters, block, index, increment):
    arrays = [array.copy() for array in blocks(parameters)]
    arrays[block][index] += increment
    return Parameters(tuple(arrays[:-1]), arrays[-1])


def shifted(parameters, tangent, amount):
    arrays = tuple(a + amount * b for a, b in zip(blocks(parameters), blocks(tangent)))
    return Parameters(arrays[:-1], arrays[-1])


def problem(depth):
    rng = np.random.default_rng(731 + depth)
    # Unit RMS, correlated, opposite, and repeated inputs; rank is only two.
    x = np.array([[1.0, 0.6, -1.0, 1.0], [0.0, 0.8, 0.0, 0.0]]) * np.sqrt(2.0)
    y = np.array([0.7, -0.4, -0.9, -0.7])
    # Use a general finite state, not just the vanishing-readout initialization.
    parameters = Parameters(
        (rng.normal(scale=0.6, size=(3, 2)),) + tuple(
            rng.normal(scale=0.5, size=(3, 3)) for _ in range(depth - 1)
        ), rng.normal(scale=0.8, size=3),
    )
    activations = tuple((ARCTAN, SHIFTED, TANH)[i % 3] for i in range(depth))
    return parameters, x, y, activations


class InitializationTests(unittest.TestCase):
    def test_exact_gaussian_scales_draw_order_and_seed(self):
        n, depth, d, seed = 5, 3, 2, 119
        state = initialize(n, depth, d, seed=seed)
        rng = np.random.default_rng(seed)
        expected = (rng.standard_normal((n, d)),) + tuple(
            rng.standard_normal((n, n)) / np.sqrt(n) for _ in range(depth - 1)
        ) + (rng.standard_normal(n) / n,)
        for actual, reference in zip(blocks(state), expected):
            np.testing.assert_array_equal(actual, reference)
        self.assertGreater(np.linalg.norm(state.readout), 0)
        for a, b in zip(blocks(state), blocks(initialize(n, depth, d, seed=seed))):
            np.testing.assert_array_equal(a, b)
        self.assertFalse(np.array_equal(state.readout, initialize(n, depth, d, seed=seed + 1).readout))

    def test_one_layer_width_one_and_global_rng_is_unchanged(self):
        before = np.random.get_state()
        state = initialize(1, 1, 1, seed=0)
        after = np.random.get_state()
        self.assertEqual(len(state.weights), 1)
        self.assertEqual(state.weights[0].shape, (1, 1))
        self.assertEqual(state.readout.shape, (1,))
        self.assertEqual(before[0], after[0])
        np.testing.assert_array_equal(before[1], after[1])
        self.assertEqual(before[2:], after[2:])


class FiniteIdentityTests(unittest.TestCase):
    def test_linear_forward_backward_and_input_normalization(self):
        x = np.array([[1.0, 2.0, -1.0], [3.0, -1.0, -3.0]])
        first = np.array([[0.5, 1.0], [-0.4, 0.7]])
        middle = (np.array([[0.3, -0.8], [0.9, 0.1]]), np.array([[1.2, 0.2], [-0.1, 0.6]]))
        a = np.array([0.7, -1.1])
        for depth in (1, 2, 3):
            with self.subTest(depth=depth):
                state = Parameters((first,) + middle[:depth - 1], a)
                expected_hidden = first @ x / np.sqrt(2.0)
                for matrix in middle[:depth - 1]:
                    expected_hidden = matrix @ expected_hidden
                result = forward(state, x, IDENTITY)
                np.testing.assert_allclose(result.hidden[-1], expected_hidden, atol=1e-15)
                np.testing.assert_allclose(result.output, a @ expected_hidden / 2, atol=1e-15)
                delta = backward(state, x, IDENTITY)
                expected_delta = np.broadcast_to(a[:, None], (2, x.shape[1]))
                for layer in range(depth - 1, -1, -1):
                    np.testing.assert_allclose(delta[layer], expected_delta, atol=1e-15)
                    if layer:
                        expected_delta = state.weights[layer].T @ expected_delta

    def test_loss_gradients_all_coordinates_all_blocks(self):
        epsilon = 1e-6
        for depth in (1, 2, 3):
            state, x, y, activations = problem(depth)
            analytic = loss_gradients(state, x, y, activations)
            for block, values in enumerate(blocks(state)):
                numeric = np.empty_like(values)
                for index in np.ndindex(values.shape):
                    plus = loss(replaced(state, block, index, epsilon), x, y, activations)
                    minus = loss(replaced(state, block, index, -epsilon), x, y, activations)
                    numeric[index] = (plus - minus) / (2 * epsilon)
                with self.subTest(depth=depth, block=block):
                    np.testing.assert_allclose(blocks(analytic)[block], numeric, atol=2e-9, rtol=2e-6)

    def test_kernel_blocks_against_numeric_output_jacobians(self):
        epsilon = 1e-6
        for depth in (1, 2, 3):
            state, x, _, activations = problem(depth)
            kappas = np.linspace(0.4, 1.7, depth + 1)
            rates = kappas.copy()
            rates[[0, -1]] *= state.width
            actual = kernel_blocks(state, x, activations, kappas=kappas)
            for block, values in enumerate(blocks(state)):
                jacobian = []
                for index in np.ndindex(values.shape):
                    plus = forward(replaced(state, block, index, epsilon), x, activations).output
                    minus = forward(replaced(state, block, index, -epsilon), x, activations).output
                    jacobian.append((plus - minus) / (2 * epsilon))
                jacobian = np.array(jacobian)
                expected = rates[block] * (jacobian.T @ jacobian)
                with self.subTest(depth=depth, block=block):
                    np.testing.assert_allclose(actual[block], expected, atol=2e-9, rtol=2e-6)
                    np.testing.assert_allclose(actual[block], actual[block].T, atol=1e-15)
                    self.assertGreaterEqual(np.linalg.eigvalsh(actual[block]).min(), -2e-14)
            np.testing.assert_array_equal(kernel(state, x, activations, kappas=kappas), actual.sum(axis=0))

    def test_flow_output_velocity_and_weighted_energy(self):
        for depth in (1, 2, 3):
            state, full_x, full_y, activations = problem(depth)
            for samples in (1, 4):
                x, y = full_x[:, :samples], full_y[:samples]
                kappas = np.linspace(0.3, 1.4, depth + 1)
                velocity = flow_velocity(state, x, y, activations, kappas=kappas)
                r = forward(state, x, activations).output - y
                k = kernel(state, x, activations, kappas=kappas)
                step = 1e-6
                plus, minus = shifted(state, velocity, step), shifted(state, velocity, -step)
                numeric_fdot = (forward(plus, x, activations).output - forward(minus, x, activations).output) / (2 * step)
                numeric_lossdot = (loss(plus, x, y, activations) - loss(minus, x, y, activations)) / (2 * step)
                rates = kappas.copy()
                rates[[0, -1]] *= state.width
                energy = sum(np.sum(v * v) / rate for v, rate in zip(blocks(velocity), rates))
                with self.subTest(depth=depth, samples=samples):
                    np.testing.assert_allclose(numeric_fdot, -2 * k @ r / samples, atol=2e-9, rtol=2e-6)
                    np.testing.assert_allclose(numeric_lossdot, -energy, atol=2e-9, rtol=2e-6)
                    np.testing.assert_allclose(energy, 4 * (r @ k @ r) / samples**2, atol=2e-13, rtol=2e-13)

    def test_simultaneous_gd_has_exact_hand_computed_update(self):
        state = Parameters((np.array([[1.0], [2.0]]),), np.array([3.0, 4.0]))
        x, y = np.ones((1, 1)), np.ones(1)
        before = tuple(a.copy() for a in blocks(state))
        new = gd_step(state, x, y, 0.1, IDENTITY)
        np.testing.assert_allclose(new.weights[0], [[-1.7], [-1.6]], atol=1e-15)
        np.testing.assert_allclose(new.readout, [2.1, 2.2], atol=1e-15)
        for original, saved in zip(blocks(state), before):
            np.testing.assert_array_equal(original, saved)
        np.testing.assert_array_equal(x, [[1.0]])
        np.testing.assert_array_equal(y, [1.0])
        for old, new_array in zip(blocks(state), blocks(new)):
            self.assertFalse(np.shares_memory(old, new_array))

    def test_gd_all_depths_matches_independent_loss_differences(self):
        for depth in (1, 2, 3):
            state, x, y, activations = problem(depth)
            kappas = np.linspace(0.6, 1.5, depth + 1)
            rates = kappas.copy()
            rates[[0, -1]] *= state.width
            eta, epsilon = 0.07, 1e-6
            new = gd_step(state, x, y, eta, activations, kappas=kappas)
            for block, values in enumerate(blocks(state)):
                for index in np.ndindex(values.shape):
                    gradient = (
                        loss(replaced(state, block, index, epsilon), x, y, activations)
                        - loss(replaced(state, block, index, -epsilon), x, y, activations)
                    ) / (2 * epsilon)
                    self.assertAlmostEqual(blocks(new)[block][index], values[index] - eta * rates[block] * gradient, delta=2e-9)

    def test_zero_residual_and_zero_step(self):
        for depth in (1, 2, 3):
            state, x, _, activations = problem(depth)
            y = forward(state, x, activations).output
            velocity = flow_velocity(state, x, y, activations)
            for v in blocks(velocity):
                np.testing.assert_array_equal(v, np.zeros_like(v))
            new = gd_step(state, x, y + 1, 0.0, activations)
            for old, v in zip(blocks(state), blocks(new)):
                np.testing.assert_array_equal(old, v)
                self.assertFalse(np.shares_memory(old, v))

    def test_correlated_opposite_and_conflicting_samples_preserved(self):
        x = np.array([[1.0, 0.6, -1.0, 1.0], [0.0, 0.8, 0.0, 0.0]]) * np.sqrt(2)
        state = initialize(4, 3, 2, seed=42)
        values = forward(state, x, ARCTAN).output
        self.assertAlmostEqual(values[2], -values[0], delta=1e-15)
        self.assertEqual(values[3], values[0])
        k = kernel(state, x, ARCTAN)
        np.testing.assert_allclose(k[:, 2], -k[:, 0], atol=1e-15)
        np.testing.assert_allclose(k[:, 3], k[:, 0], atol=1e-15)
        self.assertGreater(abs(k[0, 1]), 1e-6)
        duplicate_x = x[:, [0, 3]]
        self.assertGreaterEqual(loss(state, duplicate_x, [1.0, -1.0], ARCTAN), 1.0)
        positive = flow_velocity(state, duplicate_x, [1.0, 1.0], ARCTAN)
        opposite = flow_velocity(state, duplicate_x, [1.0, -1.0], ARCTAN)
        self.assertGreater(np.linalg.norm(positive.readout - opposite.readout), 1e-3)

    def test_batch_permutation_and_duplication_preserve_dynamics(self):
        state, x, y, activations = problem(3)
        permutation = np.array([2, 0, 3, 1])
        k = kernel(state, x, activations)
        np.testing.assert_allclose(kernel(state, x[:, permutation], activations), k[np.ix_(permutation, permutation)], atol=1e-15)
        reference = flow_velocity(state, x, y, activations)
        variants = (
            flow_velocity(state, x[:, permutation], y[permutation], activations),
            flow_velocity(state, np.tile(x, 2), np.tile(y, 2), activations),
        )
        for variant in variants:
            for a, b in zip(blocks(reference), blocks(variant)):
                np.testing.assert_allclose(a, b, atol=1e-15)


class ValidationTests(unittest.TestCase):
    def test_invalid_initialization(self):
        for field in ("width", "depth", "input_dimension"):
            for bad in (0, -1, 1.5, True):
                args = dict(width=2, depth=2, input_dimension=2, seed=0)
                args[field] = bad
                with self.subTest(field=field, value=bad), self.assertRaises(ValueError):
                    initialize(**args)
        for seed in (-1, 1.5, True):
            with self.assertRaises(ValueError):
                initialize(2, 2, 2, seed=seed)

    def test_parameter_shapes_and_values(self):
        bad_parameters = (
            ((), np.ones(2)), ((np.ones((2, 2)),), np.ones((2, 1))),
            ((np.ones((3, 2)),), np.ones(2)), ((np.ones((2, 0)),), np.ones(2)),
            ((np.ones((2, 2)), np.ones((2, 3))), np.ones(2)),
            ((np.array([[np.nan]]),), np.ones(1)),
            ((np.ones((1, 1)),), np.array([np.inf])),
            ((np.array([[1j]]),), np.ones(1)),
        )
        for weights, readout in bad_parameters:
            with self.assertRaises(ValueError):
                Parameters(weights, readout)
        state = initialize(2, 1, 2, seed=0)
        state.weights[0][0, 0] = np.nan
        with self.assertRaises(ValueError):
            forward(state, np.ones((2, 1)))

    def test_inputs_labels_and_mobilities(self):
        state = initialize(2, 2, 2, seed=0)
        x, y = np.eye(2), np.zeros(2)
        for bad in ([1, 2], np.ones((3, 2)), np.empty((2, 0)), [[np.nan], [1]], [[1j], [1]], [[True], [False]]):
            with self.assertRaises(ValueError):
                forward(state, bad)
        for bad in (1, [1], [[1, 2]], [np.inf, 0]):
            with self.assertRaises(ValueError):
                flow_velocity(state, x, bad)
        for bad in ([], [1, 1], [0, 1, 1], [-1, 1, 1], [1, np.nan, 1], [1, np.inf, 1]):
            with self.assertRaises(ValueError):
                flow_velocity(state, x, y, kappas=bad)
            with self.assertRaises(ValueError):
                kernel(state, x, kappas=bad)
        for bad in (-0.1, np.nan, np.inf, True, "0.1"):
            with self.assertRaises(ValueError):
                gd_step(state, x, y, bad)

    def test_activation_validation_and_layerwise_values(self):
        state = initialize(2, 2, 2, seed=0)
        x = np.eye(2)
        with self.assertRaises(ValueError):
            forward(state, x, (TANH,))
        with self.assertRaises(TypeError):
            forward(state, x, "tanh")
        with self.assertRaises(TypeError):
            Activation("bad", None, np.ones_like)
        bad_shape = Activation("scalar", lambda z: 0.0, np.ones_like)
        with self.assertRaises(ValueError):
            forward(state, x, bad_shape)
        bad_derivative = Activation("wrong_derivative", np.tanh, lambda z: np.ones(1))
        with self.assertRaises(ValueError):
            backward(state, x, bad_derivative)
        nonfinite = Activation("nonfinite", lambda z: np.full_like(z, np.inf), np.ones_like)
        with self.assertRaises(ValueError):
            forward(state, x, nonfinite)
        shared = forward(state, x, ARCTAN).output
        np.testing.assert_array_equal(shared, forward(state, x, (ARCTAN, ARCTAN)).output)
        self.assertGreater(np.linalg.norm(shared - forward(state, x, (ARCTAN, SHIFTED)).output), 1e-3)


if __name__ == "__main__":
    unittest.main()
