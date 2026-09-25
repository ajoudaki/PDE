"""Deterministic equivalence checks for exact cached scalar initialization."""

import unittest

import numpy as np

import scalar_aggregate_engine as original
import scalar_circle_probe_engine as original_probe
import scalar_wide_initialization as wide


class WideInitializationTests(unittest.TestCase):
    def assert_coefficients(self, actual, expected):
        self.assertEqual(set(actual), set(expected))
        for name in expected:
            np.testing.assert_allclose(actual[name], expected[name], rtol=4e-11, atol=2e-12,
                                       err_msg=name)

    def test_complete_reference_all_orders_depths_and_readout_scales(self):
        rng = np.random.default_rng(6214)
        train, probes = rng.normal(size=(3, 2)), rng.normal(size=(5, 2))
        for depth in (2, 3):
            for width in (2, 7):
                for readout_scale in (0., .07, 1.4):
                    params = list(original.initialize_network(width, 2, depth, seed=181))
                    params[0] *= .7
                    for matrix in params[1:-1]:
                        matrix *= 1.2
                    params[-1] = rng.normal(size=width)*readout_scale
                    old_probe = original_probe.initialize_probe_coefficients(params, train, probes, order=4)
                    old_training = original.initialize_coefficients(params, train, order=4)
                    for order in (2, 3, 4):
                        names = ("f", "Theta", "C", "Q")[:order]
                        new_probe = wide.initialize_probe_coefficients(params, train, probes, order=order, batch_size=2)
                        new_training = wide.initialize_coefficients(params, train, order=order, batch_size=2)
                        self.assert_coefficients(new_probe, {key:old_probe[key] for key in names})
                        self.assert_coefficients(new_training, {key:old_training[key] for key in names})

    def test_batch_partition_probe_training_and_input_immutability(self):
        rng = np.random.default_rng(82)
        params = original.initialize_network(11, 3, depth=3, seed=112)
        train = rng.normal(size=(4, 3))
        probes = np.vstack((rng.normal(size=(7, 3)), train))
        copies = [value.copy() for value in (*params, train, probes)]
        first = wide.initialize_probe_coefficients(params, train, probes, batch_size=1)
        second = wide.initialize_probe_coefficients(params, train, probes, batch_size=50)
        self.assert_coefficients(first, second)
        training = original.initialize_coefficients(params, train)
        self.assert_coefficients({key:value[-len(train):] for key, value in first.items()}, training)
        for value, previous in zip((*params, train, probes), copies):
            np.testing.assert_array_equal(value, previous)

    def test_ordered_moving_direction_term_is_present(self):
        rng = np.random.default_rng(812)
        train, probes = rng.normal(size=(3, 2)), rng.normal(size=(4, 2))
        params = list(original.initialize_network(5, 2, depth=3, seed=310))
        params[-1] = rng.normal(size=5)*.5
        actual = wide.initialize_probe_coefficients(params, train, probes, batch_size=3)
        expected = original_probe.initialize_probe_coefficients(params, train, probes)
        self.assert_coefficients(actual, expected)
        # This fixture has genuinely ordered derivative directions. A shortcut
        # that symmetrizes c,d would therefore fail independently of tolerance.
        asymmetry = np.max(abs(expected["Q"]-expected["Q"].swapaxes(2, 3)))
        self.assertGreater(asymmetry, 1e-5)

    def test_saturated_tanh_and_one_sample(self):
        params = list(original.initialize_network(3, 2, depth=3, seed=621))
        params[0] *= 50
        params[1] *= 30
        params[-1] *= 10
        train = np.array([[3., -2.]])
        probes = np.array([[.5, 1.], [-2., .3]])
        actual = wide.initialize_probe_coefficients(params, train, probes, batch_size=1)
        self.assert_coefficients(actual, original_probe.initialize_probe_coefficients(params, train, probes))
        self.assertTrue(all(np.isfinite(value).all() for value in actual.values()))

    def test_invalid_inputs(self):
        params = original.initialize_network(3, 2, depth=2)
        inputs = np.eye(2)
        for batch in (0, -1, True, 1.2):
            with self.assertRaises(ValueError):
                wide.initialize_coefficients(params, inputs, batch_size=batch)
        with self.assertRaises(ValueError):
            wide.initialize_probe_coefficients(params, inputs, np.ones((3, 3)))


if __name__ == "__main__":
    unittest.main()
