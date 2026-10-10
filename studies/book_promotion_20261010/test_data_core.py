"""Deterministic dataset contracts; synthetic MNIST fixtures, never a download."""
import json
import sys
import types
import unittest
from unittest.mock import patch

import numpy as np

from data_core import (binary_mnist_from_arrays, circle_query_inputs, load_binary_mnist,
                       toy_data, toy_target)


def mnist_fixture(split=0):
    images = np.zeros((12, 28, 28), dtype=np.uint8)
    images[:, 0, 0] = np.arange(1, 13)+20*split
    images[:, 3, 5] = 2*np.arange(1, 13)+3
    targets = np.array([1, 7, 3, 1, 7, 1, 7, 7, 1, 3, 1, 7])
    return images, targets


class ToyDataTests(unittest.TestCase):
    def test_target_against_independent_polynomial_and_special_directions(self):
        v = np.array([[1., 0.], [0., 1.], [-1., 0.], [0., -1.], [.6, .8], [-.8, .6]])
        x, y = v.T
        expected = 3*y-4*y**3 + .5*(16*x**5-20*x**3+5*x)
        np.testing.assert_allclose(toy_target(v), expected, atol=3e-15)
        for d in (3, 10):
            rows = np.ones((3, d))/np.sqrt(d)
            rows[1, 0] *= -1
            rows[2, 1] *= -1
            np.testing.assert_allclose(toy_target(rows), [2., -2., 0.], atol=1e-15)

    def test_train_only_target_scaling_and_unit_rows(self):
        data = toy_data(2, train_samples=9, query_samples=19, seed=31, label_scale=.2)
        x, y = data.train_inputs.T
        raw = 3*y-4*y**3 + .5*(16*x**5-20*x**3+5*x)
        scale = np.sqrt(np.mean(raw**2))
        x, y = data.query_inputs.T
        raw_query = 3*y-4*y**3 + .5*(16*x**5-20*x**3+5*x)
        np.testing.assert_allclose(data.train_labels, .2*raw/scale, atol=3e-15)
        np.testing.assert_allclose(data.query_labels, .2*raw_query/scale, atol=3e-15)
        self.assertAlmostEqual(np.mean(data.train_labels**2), .04)
        self.assertNotAlmostEqual(np.mean(data.query_labels**2), .04, places=4)
        for rows in (data.train_inputs, data.query_inputs):
            self.assertEqual(rows.dtype, np.float64)
            np.testing.assert_allclose(np.linalg.norm(rows, axis=1), 1., atol=2e-16)
        self.assertEqual(set(data.train_ids) & set(data.query_ids), set())
        json.dumps(data.provenance)

    def test_local_seed_contract_and_query_count_independence(self):
        state = np.random.get_state()
        for d in (2, 3):
            first = toy_data(d, 8, 13, 47)
            same = toy_data(d, 8, 13, 47)
            larger = toy_data(d, 8, 21, 47)
            changed = toy_data(d, 8, 13, 48)
            np.testing.assert_array_equal(first.train_inputs, same.train_inputs)
            np.testing.assert_array_equal(first.query_inputs, same.query_inputs)
            np.testing.assert_array_equal(first.train_inputs, larger.train_inputs)
            np.testing.assert_array_equal(first.train_labels, larger.train_labels)
            self.assertFalse(np.array_equal(first.train_inputs, changed.train_inputs))
            if d == 2:
                np.testing.assert_array_equal(first.query_inputs, changed.query_inputs)
            else:
                np.testing.assert_array_equal(first.query_inputs, larger.query_inputs[:13])
        after = np.random.get_state()
        self.assertEqual(state[0], after[0])
        np.testing.assert_array_equal(state[1], after[1])
        self.assertEqual(state[2:], after[2:])

    def test_circle_grid_phase_and_no_endpoint_duplication(self):
        np.testing.assert_allclose(circle_query_inputs(4, phase=0),
                                   [[1., 0.], [0., 1.], [-1., 0.], [0., -1.]], atol=2e-16)
        actual = circle_query_inputs(30)
        np.testing.assert_allclose(actual[0], [np.cos(.137), np.sin(.137)], atol=0)
        self.assertEqual(len(np.unique(actual, axis=0)), 30)

    def test_invalid_toy_inputs(self):
        for kwargs in ({'dimension': 1}, {'dimension': True}, {'train_samples': 0},
                       {'query_samples': 1.5}, {'seed': -1}, {'seed': 2**32-1},
                       {'label_scale': 0}, {'label_scale': float('nan')}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                toy_data(**kwargs)
        for rows in ([[0., 0.]], [[2., 0.]], [[float('nan'), 0.]], [[1+0j, 0]]):
            with self.assertRaises(ValueError):
                toy_target(rows)


class BinaryMNISTTests(unittest.TestCase):
    def setUp(self):
        self.train = mnist_fixture(0)
        self.test = mnist_fixture(1)

    def prepare(self, **kwargs):
        return binary_mnist_from_arrays(*self.train, *self.test,
                                        train_samples=5, query_samples=7, **kwargs)

    def test_filter_balance_order_labels_and_raw_pixel_normalization(self):
        data = self.prepare(label_scale=.25)
        # Frozen row-order oracle from the paper's seed-47 recipe on these fixtures.
        selected = ([7, 4, 0, 5, 10], [5, 0, 7, 6, 10, 8, 11])
        for source, rows, inputs, labels, ids, split in (
                (self.train, selected[0], data.train_inputs, data.train_labels, data.train_ids, 'train'),
                (self.test, selected[1], data.query_inputs, data.query_labels, data.query_ids, 'test')):
            images, targets = source
            self.assertEqual(inputs.shape, (len(rows), 784))
            self.assertEqual(inputs.dtype, np.float64)
            self.assertEqual(list(ids), [f'mnist:{split}:{row}' for row in rows])
            expected = np.zeros_like(inputs)
            for i, row in enumerate(rows):
                a, b = float(images[row, 0, 0]), float(images[row, 3, 5])
                denominator = np.hypot(a, b)
                expected[i, 0], expected[i, 3*28+5] = a/denominator, b/denominator
            np.testing.assert_allclose(inputs, expected, atol=1e-16)
            np.testing.assert_array_equal(labels, [-.25 if targets[r] == 1 else .25 for r in rows])
            self.assertEqual(np.count_nonzero(labels < 0), (len(rows)+1)//2)
        self.assertEqual(set(data.train_ids) & set(data.query_ids), set())
        self.assertEqual(data.provenance['source'], 'caller_supplied_arrays')
        json.dumps(data.provenance)

    def test_test_pool_never_changes_training_data_and_inputs_not_mutated(self):
        original_train = tuple(v.copy() for v in self.train)
        original_test = tuple(v.copy() for v in self.test)
        first = self.prepare()
        changed_images = self.test[0].copy()
        changed_images[:, 5, 5] = 200
        second = binary_mnist_from_arrays(*self.train, changed_images, self.test[1],
                                          train_samples=5, query_samples=7)
        np.testing.assert_array_equal(first.train_inputs, second.train_inputs)
        np.testing.assert_array_equal(first.train_labels, second.train_labels)
        np.testing.assert_array_equal(first.train_ids, second.train_ids)
        self.assertFalse(np.array_equal(first.query_inputs, second.query_inputs))
        for before, after in zip((*original_train, *original_test), (*self.train, *self.test)):
            np.testing.assert_array_equal(before, after)
        for inputs, source in ((first.train_inputs, self.train[0]), (first.query_inputs, self.test[0])):
            self.assertFalse(np.shares_memory(inputs, source))

    def test_seed_replay_and_independent_splits(self):
        first = self.prepare(seed=47)
        second = self.prepare(seed=47)
        changed = self.prepare(seed=48)
        np.testing.assert_array_equal(first.train_inputs, second.train_inputs)
        np.testing.assert_array_equal(first.query_inputs, second.query_inputs)
        self.assertEqual(first.provenance, second.provenance)
        self.assertFalse(np.array_equal(first.train_ids, changed.train_ids))
        reversed_pair = self.prepare(digit_pair=(7, 1))
        self.assertEqual(np.count_nonzero(reversed_pair.train_labels == -1), 3)
        for label, identifier in zip(reversed_pair.train_labels, reversed_pair.train_ids):
            digit = self.train[1][int(identifier.rsplit(':', 1)[1])]
            self.assertEqual(label, -1 if digit == 7 else 1)

    def test_invalid_sources_pairs_and_insufficient_classes(self):
        for pair in ((1, 1), (1,), (1, 2, 3), (True, 7), (1., 7), (1, 10), None):
            with self.subTest(pair=pair), self.assertRaises(ValueError):
                self.prepare(digit_pair=pair)
        with self.assertRaisesRegex(ValueError, 'too few'):
            binary_mnist_from_arrays(*self.train, *self.test, train_samples=11, query_samples=7)
        with self.assertRaisesRegex(ValueError, 'uint8'):
            binary_mnist_from_arrays(self.train[0].astype(float), self.train[1], *self.test)
        zeros = np.zeros_like(self.train[0])
        with self.assertRaisesRegex(ValueError, 'nonzero norm'):
            binary_mnist_from_arrays(zeros, self.train[1], *self.test, train_samples=5, query_samples=7)

    def test_loader_uses_official_flags_and_download_is_explicit(self):
        calls = []
        datasets = types.ModuleType('torchvision.datasets')

        def fake_mnist(**kwargs):
            calls.append(kwargs)
            images, targets = self.train if kwargs['train'] else self.test
            return types.SimpleNamespace(data=images, targets=targets)

        datasets.MNIST = fake_mnist
        package = types.ModuleType('torchvision')
        package.datasets = datasets
        with patch.dict(sys.modules, {'torchvision': package, 'torchvision.datasets': datasets}):
            actual = load_binary_mnist('/synthetic-unused-cache', train_samples=5, query_samples=7)
            self.assertEqual(calls, [dict(root='/synthetic-unused-cache', train=True, download=False),
                                     dict(root='/synthetic-unused-cache', train=False, download=False)])
            np.testing.assert_array_equal(actual.train_inputs, self.prepare().train_inputs)
            self.assertIn('official train/test', actual.provenance['source'])
            load_binary_mnist('/synthetic-unused-cache', train_samples=5, query_samples=7, download=True)
            self.assertTrue(all(v['download'] for v in calls[2:]))
            with self.assertRaises(ValueError):
                load_binary_mnist('/synthetic-unused-cache', download='yes')
            with self.assertRaises(ValueError):
                load_binary_mnist('')


class IntegrationTests(unittest.TestCase):
    def test_direct_float64_tensor_conversion_and_short_core_step(self):
        import torch
        from compression_core import Dense, Legendre, step

        data = toy_data(3, train_samples=4, query_samples=7, seed=17, label_scale=.1)
        inputs, labels, query = [torch.from_numpy(v) for v in
                                 (data.train_inputs, data.train_labels, data.query_inputs)]
        dense = Dense(12, 3, seed=19)
        for model in (dense, Legendre(dense, inputs, labels, order=2)):
            next_state = step(model, model.initial_state, inputs, labels, .001, method='euler')
            prediction = model.predict(next_state, query)
            self.assertEqual(tuple(prediction.shape), (7,))
            self.assertTrue(bool(torch.isfinite(prediction).all()))
            self.assertGreater(float(torch.linalg.vector_norm(prediction)), 0.)


if __name__ == '__main__':
    unittest.main()
