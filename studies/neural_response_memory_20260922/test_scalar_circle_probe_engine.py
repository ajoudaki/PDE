"""Deterministic small-network checks; this file runs no training campaign."""

import unittest
from unittest.mock import patch

import numpy as np
from numpy.testing import assert_allclose
from scipy.integrate import solve_ivp

import scalar_aggregate_engine as aggregate
import scalar_circle_probe_engine as probe


def circle(angles):
    return np.column_stack((np.cos(angles), np.sin(angles)))


class PassiveProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params = aggregate.initialize_network(5, 2, depth=3, seed=713)
        cls.params = (*cls.params[:-1], cls.params[-1] * 4)
        cls.train = circle([0.17, 1.13])
        cls.probes = circle([0.41, 2.2, -0.72])
        cls.labels = np.array([0.4, -0.6])
        cls.coefficients = aggregate.initialize_coefficients(cls.params, cls.train)
        cls.passive = probe.initialize_probe_coefficients(cls.params, cls.train, cls.probes)

    def test_rectangular_tensors_against_combined_full_oracle(self):
        m = len(self.train)
        full = aggregate.initialize_coefficients(self.params, np.vstack((self.train, self.probes)))
        for degree, name in enumerate(("f", "Theta", "C", "Q")):
            expected = full[name][(slice(m, None),) + (slice(0, m),) * degree]
            self.assertEqual(self.passive[name].shape, (len(self.probes),) + (m,) * degree)
            assert_allclose(self.passive[name], expected, rtol=3e-13, atol=3e-14)

    def test_training_probes_reproduce_original_coefficients_at_every_order(self):
        for order in (2, 3, 4):
            actual = probe.initialize_probe_coefficients(self.params, self.train, self.train, order)
            self.assertEqual(len(actual), order)
            for name, value in actual.items():
                assert_allclose(value, self.coefficients[name], rtol=2e-13, atol=2e-14)

    def test_moving_direction_Q_by_centered_derivative_of_C(self):
        step = 2e-6
        for d in range(len(self.train)):
            gd = aggregate.sample_direction(self.params, self.train, d)
            plus = tuple(p + step * g for p, g in zip(self.params, gd))
            minus = tuple(p - step * g for p, g in zip(self.params, gd))
            cp = probe.initialize_probe_coefficients(plus, self.train, self.probes, 3)["C"]
            cm = probe.initialize_probe_coefficients(minus, self.train, self.probes, 3)["C"]
            assert_allclose((cp - cm) / (2 * step), self.passive["Q"][:, :, :, d],
                            rtol=3e-7, atol=2e-10)

    def test_no_square_probe_kernel_and_forward_only(self):
        with patch.object(aggregate, "_plain_fields", side_effect=AssertionError("square plain fields")), \
             patch.object(aggregate, "_jet_fields", side_effect=AssertionError("square jet fields")):
            actual = probe.initialize_probe_coefficients(self.params, self.train, self.probes)
            prediction = probe.forward_only(self.params, self.probes)
        for name, value in actual.items():
            assert_allclose(value, self.passive[name])
        assert_allclose(prediction, self.passive["f"], rtol=0, atol=1e-15)

    def test_signature_readout_against_explicit_passive_ODE(self):
        for order in (2, 3, 4):
            hierarchy = probe.SignatureHierarchy(self.coefficients, self.labels, order)
            names = ("f", "Theta", "C", "Q")[:order - 1]
            shapes = [self.passive[name].shape for name in names]
            sizes = [int(np.prod(shape)) for shape in shapes]
            offsets = np.cumsum([hierarchy.size, *sizes])
            initial = np.concatenate([hierarchy.initial_state(),
                                      *(self.passive[name].ravel() for name in names)])

            def explicit_rhs(time, state):
                scalar_state = state[:hierarchy.size]
                velocity = -2 / hierarchy.M * (hierarchy.unpack(scalar_state)["f"] - self.labels)
                fields = [state[offsets[i]:offsets[i + 1]].reshape(shape)
                          for i, shape in enumerate(shapes)]
                terminal = self.passive[("f", "Theta", "C", "Q")[order - 1]]
                return np.concatenate([hierarchy.rhs(time, scalar_state),
                                       *(np.tensordot(value, velocity, axes=([-1], [0])).ravel()
                                         for value in [*fields[1:], terminal])])

            solution = solve_ivp(explicit_rhs, (0, 0.8), initial, method="DOP853",
                                 rtol=2e-12, atol=2e-14, t_eval=np.linspace(0, 0.8, 13))
            self.assertTrue(solution.success, solution.message)
            for state in solution.y.T:
                scalar_state = state[:hierarchy.size]
                assert_allclose(hierarchy.readout(self.passive, scalar_state),
                                state[offsets[0]:offsets[1]], rtol=2e-10, atol=2e-12)
                assert_allclose(hierarchy.readout(self.coefficients, scalar_state),
                                hierarchy.unpack(scalar_state)["f"], rtol=2e-10, atol=2e-12)

    def test_runtime_neural_functions_disabled_and_no_feedback(self):
        hierarchy = probe.SignatureHierarchy(self.coefficients, self.labels)
        state = hierarchy.initial_state()
        state[hierarchy.training_size:] = np.linspace(-0.2, 0.3, hierarchy.size - hierarchy.training_size)
        ordinary_training = hierarchy.training.rhs(0, hierarchy.training_state(state))
        with patch.object(aggregate, "_plain_fields", side_effect=AssertionError("network")), \
             patch.object(aggregate, "_jet_fields", side_effect=AssertionError("network")), \
             patch.object(aggregate, "network_rhs", side_effect=AssertionError("network")), \
             patch.object(probe, "_fields", side_effect=AssertionError("network")), \
             patch.object(probe, "forward_only", side_effect=AssertionError("network")):
            derivative = hierarchy(0, state)
            output = hierarchy.readout(self.passive, state)
            changed = state.copy()
            changed[hierarchy.training_size:] *= 13
            changed_derivative = hierarchy(0, changed)
        assert_allclose(derivative[:hierarchy.training_size], ordinary_training, rtol=0, atol=0)
        assert_allclose(changed_derivative[:hierarchy.training_size], ordinary_training, rtol=0, atol=0)
        self.assertTrue(np.isfinite(output).all())
        self.assertEqual(hierarchy.training.counts()["neuron_scalars"], 0)
        self.assertEqual(hierarchy.size - hierarchy.training_size, 2 + 4 + 8)
        second_order = probe.SignatureHierarchy(self.coefficients, self.labels, 2)
        self.assertEqual(tuple(second_order.signatures(second_order.initial_state())), ("z",))

    def test_restart_preserves_signatures(self):
        hierarchy = probe.SignatureHierarchy(self.coefficients, self.labels)
        options = dict(method="DOP853", rtol=2e-12, atol=2e-14)
        whole = solve_ivp(hierarchy, (0, 0.8), hierarchy.initial_state(), **options)
        first = solve_ivp(hierarchy, (0, 0.31), hierarchy.initial_state(), **options)
        second = solve_ivp(hierarchy, (0.31, 0.8), first.y[:, -1], **options)
        self.assertTrue(whole.success and first.success and second.success)
        assert_allclose(second.y[:, -1], whole.y[:, -1], rtol=2e-10, atol=3e-12)


class FourierTests(unittest.TestCase):
    def test_known_cosine_sine_tensors_at_grid_and_offgrid(self):
        grid = 2 * np.pi * np.arange(33) / 33
        constant = np.array([[0.3, 0.6], [-0.1, 0.9]])
        cosine = np.array([[0.4, -0.8], [0.2, 1.1]])
        sine = np.array([[-0.7, 0.2], [0.6, -0.3]])

        def values(theta):
            return constant + np.cos(2 * theta)[..., None, None] * cosine + np.sin(3 * theta)[..., None, None] * sine

        modes = probe.fit_fourier(values(grid), 4)
        self.assertEqual(modes.shape, (5, 2, 2))
        assert_allclose(modes[2], cosine / 2, atol=3e-16)
        assert_allclose(modes[3], -1j * sine / 2, atol=3e-16)
        for angles in (grid, np.array([[0.13, 0.89], [2.49, -0.61]]), np.asarray(0.83)):
            assert_allclose(probe.evaluate_fourier(modes, angles), values(angles), atol=2e-15)
        constant_modes = probe.fit_fourier(np.full(9, 2.5), 0)
        assert_allclose(probe.evaluate_fourier(constant_modes, [0.3, 1.2]), [2.5, 2.5])

    def test_fourier_and_signature_readout_commute(self):
        rng = np.random.default_rng(114)
        m, count = 2, 25
        angles = 2 * np.pi * np.arange(count) / count
        coefficients = {}
        for degree, name in enumerate(("f", "Theta", "C", "Q")):
            shape = (m,) * degree
            a, b, c = (rng.standard_normal(shape) for _ in range(3))
            coefficients[name] = (a + np.cos(angles).reshape((count,) + (1,) * degree) * b
                                  + np.sin(2 * angles).reshape((count,) + (1,) * degree) * c)
        training = {name: value[:m] for name, value in coefficients.items()}
        hierarchy = probe.SignatureHierarchy(training, [1, -1])
        state = hierarchy.initial_state()
        state[hierarchy.training_size:] = rng.standard_normal(hierarchy.size - hierarchy.training_size)
        compressed = probe.fit_fourier_coefficients(coefficients, 3)
        direct = hierarchy.readout(coefficients, state)
        from_modes = probe.evaluate_fourier(hierarchy.readout(compressed, state), angles)
        assert_allclose(from_modes, direct, atol=2e-14)
        reconstructed = probe.evaluate_fourier_coefficients(compressed, angles)
        for name in coefficients:
            assert_allclose(reconstructed[name], coefficients[name], atol=3e-15)

    def test_invalid_fourier_and_state_shapes(self):
        for mode in (True, -1, 4, 2.5):
            with self.assertRaises(ValueError):
                probe.fit_fourier(np.ones(8), mode)
        with self.assertRaises(ValueError):
            probe.fit_fourier(np.ones(8, dtype=complex), 2)
        hierarchy = probe.SignatureHierarchy({"f": np.zeros(2), "Theta": np.eye(2)}, [1, -1], 2)
        with self.assertRaises(ValueError):
            hierarchy.signatures(np.zeros(hierarchy.size + 1))
        with self.assertRaises(ValueError):
            hierarchy.readout({"f": np.zeros(3), "Theta": np.zeros((3, 3))}, hierarchy.initial_state())


if __name__ == "__main__":
    unittest.main()
