"""Small CPU oracles for the extracted dictionary component; no saved data."""
import math
import unittest

import numpy as np
import torch

from pde import observable_dictionaries as core
from pde.finite_torch import NetworkEngine
from pde.observable_torch_p1 import ClosureEngine, TensorState


def numpy_word(word, w, A):
    """Independent scalar syntax interpretation on the finite dense carrier."""
    op = word.op
    if op == "one":
        return np.ones(len(w))
    if op in ("g1", "g2"):
        return w[:, int(op[-1]) - 1]
    if op == "action":
        return (A if word.population == 2 else A.T) @ numpy_word(word.args[0], w, A)
    values = [numpy_word(arg, w, A) for arg in word.args]
    if op in ("tanh", "sin", "cos"):
        return getattr(np, op)(values[0])
    if op == "scale":
        return float(word.scalar) * values[0]
    if op == "add":
        return values[0] + values[1]
    if op == "multiply":
        return values[0] * values[1]
    raise AssertionError(op)


class DictionaryTests(unittest.TestCase):
    def setUp(self):
        self.network = NetworkEngine(2, 144, 210, device="cpu", dtype=torch.float64)
        self.initial = self.network.initial_state()

    def test_counts_and_all_retained_words(self):
        expected = [(5, 3), (15, 6), (35, 10), (71, 15), (128, 21),
                    (213, 28), (333, 36), (499, 45), (720, 55)]
        for p, shape in enumerate(expected, 1):
            with self.subTest(p=p):
                definition = core.build_dictionary(p)
                raw = core.raw_observable_values(self.initial, p)
                self.assertEqual(tuple(x.shape[1] for x in raw), shape)
                for actual, words in zip(raw, (definition.first_words, definition.second_words)):
                    oracle = np.column_stack([numpy_word(word, self.initial.w.numpy(),
                                                        self.initial.M.numpy()) for word in words])
                    np.testing.assert_allclose(actual.numpy(), oracle, atol=2e-13, rtol=2e-13)

    def test_ridge_normalization_and_initial_action(self):
        p = 5
        raw = core.raw_observable_values(self.initial, p)
        b1, b2 = core.dictionaries(self.initial, p, "ours")
        for source, basis in zip(raw, (b1, b2)):
            x = source.numpy()
            L = np.linalg.cholesky(x.T @ x / 144 + np.eye(x.shape[1]) / (1024 * 36))
            np.testing.assert_allclose(basis.numpy(), np.linalg.solve(L, x.T).T,
                                       atol=2e-10, rtol=2e-10)
        engine, state = core.build(self.initial, p, "ours")
        filtered = b2 @ b2.T @ self.initial.M @ b1 @ b1.T / 144**2
        represented = engine.b2 @ state.M @ engine.b1.T / 144
        torch.testing.assert_close(filtered, represented, atol=2e-12, rtol=2e-12)
        torch.testing.assert_close(state.c, self.initial.c, atol=0, rtol=0)
        metadata = core.dictionary_metadata(self.initial, p, "ours", bases=(b1, b2))
        self.assertEqual(metadata["nominal_dimensions"], [128, 21])
        self.assertLessEqual(metadata["populations"][0]["numerical_rank"], 126)
        self.assertGreater(metadata["populations"][0]["ridge_condition"], 1)
        self.assertLess(metadata["populations"][0]["triangular_solve_residual"], 1e-12)

    def test_frozen_random_blocks_prefix_and_span(self):
        before = torch.random.get_rng_state().clone()
        large = core.dictionaries(self.initial, 9, "gaussian")
        for p in (1, 2, 3, 4, 5, 7):
            for lower, upper in zip(core.dictionaries(self.initial, p, "gaussian"), large):
                torch.testing.assert_close(lower, upper[:, :lower.shape[1]], atol=1e-14, rtol=1e-14)
        # Check the retained draw convention independently, including appended seeds.
        for layer, basis in enumerate(large):
            rng = torch.Generator().manual_seed(7319 + layer)
            old = torch.randn((144, (128, 21)[layer]), generator=rng, dtype=torch.float64)
            rng.manual_seed(7319 + 100000 + layer)
            added = torch.randn((144, (592, 34)[layer]), generator=rng, dtype=torch.float64)
            raw = torch.cat((old, added), dim=1)
            torch.testing.assert_close(basis, raw / raw.square().mean(0).sqrt(), atol=0, rtol=0)
        g = core.dictionaries(self.initial, 5, "gaussian")
        q = core.dictionaries(self.initial, 5, "orthogonal")
        qsmall = core.dictionaries(self.initial, 3, "orthogonal")
        for gaussian, orthogonal, smaller in zip(g, q, qsmall):
            k = orthogonal.shape[1]
            torch.testing.assert_close(orthogonal.T @ orthogonal / 144,
                                       torch.eye(k, dtype=torch.float64), atol=2e-14, rtol=2e-14)
            torch.testing.assert_close(gaussian.square().mean(0),
                                       torch.ones(k, dtype=torch.float64), atol=1e-14, rtol=1e-14)
            torch.testing.assert_close(orthogonal @ (orthogonal.T @ gaussian) / 144,
                                       gaussian, atol=4e-14, rtol=4e-14)
            prefix = orthogonal[:, :smaller.shape[1]]
            # QR orientation is immaterial; compare prefix subspaces.
            torch.testing.assert_close(prefix @ prefix.T, smaller @ smaller.T,
                                       atol=2e-12, rtol=2e-12)
        self.assertTrue(torch.equal(before, torch.random.get_rng_state()))

    def test_velocity_against_autograd_at_nonzero_readout(self):
        for method in core.METHODS:
            with self.subTest(method=method):
                engine, state = core.build(self.initial, 2, method)
                state.c.add_(0.13)
                inputs = torch.tensor([[1., 0.], [0.6, 0.8], [-0.8, 0.6]], dtype=torch.float64)
                data = engine.prepare_data(inputs, [1., -0.4, 0.2], [0.2, 0.3, 0.5])
                w, c, M = (value.clone().requires_grad_() for value in (state.w, state.c, state.M))
                h1 = torch.tanh(w @ inputs.T)
                h2 = torch.tanh(engine.b2 @ M @ engine.b1.T @ h1 / 144)
                f = c @ h2 / 144
                loss = ((f - data.labels).square() * data.probabilities).sum()
                gradients = torch.autograd.grad(loss, (w, c, M))
                actual = engine.rhs(state, data)
                for velocity, gradient, mobility in zip((actual.w, actual.c, actual.M),
                                                         gradients, (144, 144, 1)):
                    torch.testing.assert_close(velocity, -mobility * gradient, atol=1e-12, rtol=1e-12)
                ref = engine.rhs(state, data, implementation="reference")
                for key in ("w", "c", "M"):
                    torch.testing.assert_close(getattr(actual, key), getattr(ref, key), atol=1e-12, rtol=1e-12)

    def test_complete_basis_reduces_to_dense_network(self):
        net = NetworkEngine(2, 8, 22, device="cpu", dtype=torch.float64)
        initial = net.initial_state()
        basis = math.sqrt(8) * torch.eye(8, dtype=torch.float64)
        D = basis.T @ initial.M @ basis / 8
        engine = ClosureEngine(basis, initial.w, basis, D, dtype=torch.float64)
        state = engine.state(initial.w, initial.c, D)
        data = engine.prepare_data([[1., 0.], [0.6, 0.8]], [1., -1.])
        for exact, reduced in ((initial, state),
                               (net.heun_step(initial, data, .01), engine.heun_step(state, data, .01))):
            torch.testing.assert_close(net.predict(exact, data.inputs), engine.predict(reduced, data.inputs),
                                       atol=2e-14, rtol=2e-14)
            dense_velocity, velocity = net.rhs(exact, data), engine.rhs(reduced, data)
            for key in ("w", "c", "M"):
                torch.testing.assert_close(getattr(dense_velocity, key), getattr(velocity, key),
                                           atol=2e-14, rtol=2e-14)

    def test_general_d_p1_weighted_sphere_triple(self):
        engine, state = core.initialize_population_p1(3, 32, 53)
        self.assertEqual((engine.K1, engine.K2, engine.d), (7, 4, 3))
        self.assertTrue(torch.equal(state.c, torch.zeros(32, dtype=torch.float64)))
        inputs = torch.tensor([[1., 0., 0.], [.6, .8, 0.], [0., .6, .8]], dtype=torch.float64)
        data = engine.prepare_data(inputs, [1., -.5, .3], [.2, .3, .5])
        state = engine.evolve(state, data, steps=2, step_size=.01)
        w, c, M = (value.clone().requires_grad_() for value in (state.w, state.c, state.M))
        h1 = torch.tanh(w @ inputs.T)
        h2 = torch.tanh(engine.b2 @ M @ engine.b1.T @ (engine.p1[:, None] * h1))
        prediction = (engine.p2 * c) @ h2
        loss = ((prediction - data.labels).square() * data.probabilities).sum()
        gradients = torch.autograd.grad(loss, (w, c, M))
        actual = engine.rhs(state, data)
        expected = (-gradients[0] / engine.p1[:, None],
                    -gradients[1] / engine.p2, -gradients[2])
        for velocity, oracle in zip((actual.w, actual.c, actual.M), expected):
            torch.testing.assert_close(velocity, oracle, atol=1e-13, rtol=1e-13)
        torch.testing.assert_close(engine.predict(state, inputs), prediction.detach(),
                                   atol=1e-14, rtol=1e-14)

    def test_caps_crossing_and_endpoint_metric_oracle(self):
        net = NetworkEngine(2, 8, 7, device="cpu", dtype=torch.float64)
        state = net.initial_state()
        data = net.prepare_data([[1., 0.], [0.6, 0.8]], [1., -1.])
        initial_loss = float(net.loss(state, data))
        next_loss = float(net.loss(net.heun_step(state, data, .01), data))
        threshold = (initial_loss + next_loss) / 2
        self.assertLess(next_loss, threshold)
        stopped = core.fit_endpoint(net, state, data, step_size=.01, max_steps=1, threshold=threshold)
        self.assertEqual(stopped.status, "fitted")
        self.assertTrue(0 < stopped.time < .01)
        self.assertLessEqual(stopped.loss, threshold)
        self.assertAlmostEqual(stopped.loss, threshold, places=11)
        missed = core.fit_endpoint(net, state, data, step_size=.01, max_steps=0, threshold=threshold)
        self.assertEqual(missed.status, "step_cap")
        with self.assertRaises(ValueError):
            core.endpoint_errors(net, missed, net, stopped, data.inputs)
        # Distinct independently supplied fitted states: metric is a panel RMS.
        other_state = net.heun_step(state, data, .01)
        other = core.Endpoint(other_state, .01, float(net.loss(other_state, data)),
                              threshold, 1, "fitted")
        actual = core.endpoint_errors(net, stopped, net, other, data.inputs)
        delta = (net.predict(stopped.state, data.inputs) - net.predict(other_state, data.inputs)).numpy()
        self.assertAlmostEqual(actual["rms"], float(np.sqrt(np.mean(delta**2))), places=15)
        self.assertAlmostEqual(actual["l1"], float(np.mean(abs(delta))), places=15)
        self.assertAlmostEqual(actual["sampled_max"], float(np.max(abs(delta))), places=15)
        zero = core.fit_endpoint(net, state, data, step_size=.01, max_steps=0, threshold=2 * initial_loss)
        self.assertEqual((zero.status, zero.time, zero.steps), ("fitted", 0., 0))

    def test_validation_and_frozen_ownership(self):
        for order in (True, 0, 10, 1.5):
            with self.assertRaises(ValueError):
                core.build(self.initial, order, "ours")
        tiny = NetworkEngine(2, 4, 1, dtype=torch.float64).initial_state()
        with self.assertRaises(ValueError):
            core.build(tiny, 1, "orthogonal")
        for seed in (True, -1, 2**64, 0.5):
            with self.assertRaises(ValueError):
                core.build(self.initial, 1, "gaussian", seed)
        engine, state = core.build(self.initial, 1, "ours")
        original = engine.g.clone()
        self.initial.w.add_(1)
        torch.testing.assert_close(engine.g, original, atol=0, rtol=0)
        engine.b1[0, 0] += 1
        with self.assertRaises(ValueError):
            engine.predict(state, [[1., 0.]])


if __name__ == "__main__":
    torch.set_num_threads(1)
    unittest.main(verbosity=2)
