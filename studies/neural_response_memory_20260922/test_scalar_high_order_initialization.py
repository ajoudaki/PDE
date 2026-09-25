"""Deterministic exact-coefficient checks; no research training or wide pilots."""

import os
import unittest

import numpy as np
import torch

import scalar_aggregate_engine as aggregate
import scalar_circle_probe_engine as original
import scalar_high_order_initialization as initialized
import scalar_high_order_oracle as oracle


def circle(angles):
    angles = np.asarray(angles)
    return np.column_stack((np.cos(angles), np.sin(angles)))


class HighOrderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)
        cls.cases = []
        for width, samples, seed, added_readout in ((3, 2, 19, 0.), (7, 3, 23, .7)):
            params = aggregate.initialize_network(width, 2, depth=3, seed=seed)
            params[-1][:] += added_readout*np.linspace(-.7, 1., width)
            inputs = circle(np.linspace(.13, 1.31, samples))
            probes = circle([-.21, .66, 2.19])
            expected = oracle.initialize_probe_coefficients(params, inputs, probes, order=6)
            actual, metadata = initialized.initialize_probe_coefficients(
                params, inputs, probes, order=6, device="cpu", batch_size=2,
                word_chunk_size=7, return_metadata=True)
            cls.cases.append((params, inputs, probes, expected, actual, metadata))

    def test_every_ordered_word_through_degree_four_against_dense_multijet(self):
        for params, inputs, probes, expected, actual, metadata in self.cases:
            with self.subTest(width=len(params[-1]), samples=len(inputs)):
                for order in range(1, 7):
                    name = "T"+str(order)
                    self.assertEqual(actual[name].shape, (len(probes),)+(len(inputs),)*(order-1))
                    self.assertIsInstance(actual[name], np.ndarray)
                    np.testing.assert_allclose(actual[name], expected[name], rtol=3e-11, atol=2e-12)
                self.assertEqual(metadata["initialization_hash"], initialized.array_hash(*params))
                self.assertEqual(metadata["status"], "complete")

    def test_oracle_and_production_match_original_order_four(self):
        for params, inputs, probes, expected, actual, _ in self.cases:
            old = original.initialize_probe_coefficients(params, inputs, probes, order=4)
            for order, name in enumerate(("f", "Theta", "C", "Q"), 1):
                np.testing.assert_allclose(expected["T"+str(order)], old[name], rtol=2e-12, atol=2e-13)
                np.testing.assert_allclose(actual["T"+str(order)], old[name], rtol=2e-12, atol=2e-13)

    def test_repeated_indices_and_noncommuting_derivative_order(self):
        params, inputs, probes, _, actual, _ = self.cases[1]
        for word in ((0, 0, 0, 0), (2, 1, 2, 1), (0, 1, 2, 0)):
            expected = oracle.selected_word_kernel(params, inputs, probes, word)
            np.testing.assert_allclose(actual["T6"][(slice(None), slice(None), *word)],
                                       expected, rtol=3e-11, atol=2e-12)
        difference = actual["T4"]-actual["T4"].swapaxes(-1, -2)
        self.assertGreater(np.max(np.abs(difference)), 1e-8)

    def test_outer_direction_finite_difference_recomputes_inner_moving_directions(self):
        params, inputs, probes, _, actual, _ = self.cases[1]
        word = (1, 0, 1, 2)
        direction = aggregate.sample_direction(params, inputs, word[-1])
        target = actual["T6"][(slice(None), slice(None), *word)]
        errors = []
        for step in (1e-4, 5e-5):
            plus = tuple(p+step*g for p, g in zip(params, direction))
            minus = tuple(p-step*g for p, g in zip(params, direction))
            difference = (oracle.selected_word_kernel(plus, inputs, probes, word[:-1])
                          -oracle.selected_word_kernel(minus, inputs, probes, word[:-1]))/(2*step)
            errors.append(float(np.max(np.abs(difference-target))))
        self.assertLess(errors[-1], 2e-7)
        self.assertLessEqual(errors[-1], errors[0]*1.1+1e-10)

    def test_probe_word_batching_and_order_five_prefix(self):
        params, inputs, probes, _, actual, _ = self.cases[0]
        other = initialized.initialize_probe_coefficients(params, inputs, probes, 6, device="cpu",
                                                          batch_size=1, word_chunk_size=3)
        prefix = initialized.initialize_probe_coefficients(params, inputs, probes, 5, device="cpu",
                                                           batch_size=3, word_chunk_size=8)
        for name in actual:
            np.testing.assert_allclose(other[name], actual[name], rtol=2e-12, atol=2e-13)
            if name in prefix:
                np.testing.assert_allclose(prefix[name], actual[name], rtol=2e-12, atol=2e-13)

    def test_training_coefficients_and_first_pair_symmetry(self):
        params, inputs, _, _, _, _ = self.cases[0]
        values = initialized.initialize_coefficients(params, inputs, 6, device="cpu", word_chunk_size=5)
        expected = oracle.initialize_coefficients(params, inputs, 6)
        for name in values:
            np.testing.assert_allclose(values[name], expected[name], rtol=3e-11, atol=2e-12)
            if name != "T1":
                np.testing.assert_allclose(values[name], values[name].swapaxes(0, 1), rtol=2e-12, atol=2e-13)

    def test_antipodal_outputs_match_explicit_queries_at_every_order(self):
        params, inputs, probes, _, _, _ = self.cases[0]
        half = probes[:2]
        full = np.concatenate((half, -half))
        reconstructed, metadata = initialized.initialize_antipodal_probe_coefficients(
            params, inputs, half, 6, device="cpu", batch_size=2, word_chunk_size=8, return_metadata=True)
        direct = initialized.initialize_probe_coefficients(params, inputs, full, 6, device="cpu",
                                                           batch_size=3, word_chunk_size=5)
        for name in direct:
            np.testing.assert_allclose(reconstructed[name], direct[name], rtol=3e-12, atol=3e-13)
        self.assertEqual(metadata["computed_query_count"], 2)
        self.assertEqual(metadata["query_count"], 4)
        self.assertEqual(metadata["probe_input_hash"], initialized.array_hash(full))

    def test_resource_limits_are_enforced(self):
        params, inputs, probes, _, _, _ = self.cases[0]
        with self.assertRaises(initialized.InitializationLimit) as caught:
            initialized.initialize_probe_coefficients(params, inputs, probes, 6, device="cpu", max_rss_bytes=1)
        self.assertEqual(caught.exception.metadata["status"], "resource_limit")
        with self.assertRaisesRegex(ValueError, "ceiling"):
            initialized.initialize_coefficients(params, inputs, device="cpu", max_cuda_bytes=initialized.CUDA_LIMIT+1)

    @unittest.skipUnless(torch.cuda.is_available(), "CUDA unavailable; coordinate a free device before running")
    def test_gpu_all_words_against_cpu_and_dense_multijet(self):
        device = os.environ.get("SCALAR_TEST_CUDA_DEVICE", "cuda:1")
        for params, inputs, probes, expected, actual, _ in self.cases:
            values = initialized.initialize_probe_coefficients(params, inputs, probes, 6, device=device,
                                                               batch_size=2, word_chunk_size=7)
            for name in values:
                np.testing.assert_allclose(values[name], actual[name], rtol=3e-11, atol=3e-12)
                np.testing.assert_allclose(values[name], expected[name], rtol=3e-11, atol=3e-12)


if __name__ == "__main__":
    unittest.main()
