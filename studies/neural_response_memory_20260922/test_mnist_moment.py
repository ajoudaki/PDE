"""Small CPU correctness tests for the MNIST comparison implementation."""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import torch

from moment_engine import MomentState
from orthogonal_moment_engine import OrthogonalMomentEngine
from mnist_moment_run import (
    DenseEngine, DenseState, component_error, heun_interpolant, heun_trial,
    load_dataset, locate_loss_crossing, parser, run,
)


class MnistMomentTests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        self.d, self.n, self.M = 5, 9, 7
        rng = np.random.default_rng(231)
        self.inputs = rng.normal(size=(self.M, self.d))/np.sqrt(self.d)
        self.labels = rng.normal(size=self.M)
        self.seed = 20260924

    def dense(self):
        return DenseEngine(self.d, self.n, self.inputs, self.labels, seed=self.seed)

    def moment(self, order):
        return OrthogonalMomentEngine(self.d, self.n, order, self.inputs,
                                      self.labels, seed=self.seed, lifted=False)

    def test_dense_velocity_matches_independent_autograd(self):
        engine = self.dense()
        state = engine.initial_state()
        state.c += torch.linspace(-.4, .5, self.n, dtype=torch.float64)
        w, W, c = (value.clone().requires_grad_() for value in state.tensors())
        h1 = torch.tanh(w @ torch.tensor(self.inputs).T)
        h2 = torch.tanh(W @ h1)
        loss = ((c @ h2/self.n-torch.tensor(self.labels))**2).mean()
        gradients = torch.autograd.grad(loss, (w, W, c))
        velocity = engine.rhs(state)
        for actual, grad, mobility in zip(velocity.tensors(), gradients, (self.n, 1, self.n)):
            torch.testing.assert_close(actual, -mobility*grad, rtol=2e-13, atol=2e-14)

    def test_all_orders_have_identical_canonical_initialization_and_tangent(self):
        dense = self.dense()
        ds = dense.initial_state()
        dv = dense.rhs(ds)
        for order in (1, 2, 3):
            with self.subTest(order=order):
                engine = self.moment(order)
                state = engine.initial_state()
                torch.testing.assert_close(state.w, ds.w, rtol=0, atol=0)
                torch.testing.assert_close(state.c, ds.c, rtol=0, atol=0)
                torch.testing.assert_close(engine.W0, ds.W, rtol=0, atol=0)
                with patch.object(engine, "reconstruct_delta_for_diagnostics",
                                  side_effect=AssertionError("dense learned matrix")):
                    velocity = engine.rhs(state)
                    prediction = engine.predict(state, self.inputs)
                torch.testing.assert_close(prediction, dense.predict(ds, self.inputs), rtol=0, atol=0)
                torch.testing.assert_close(velocity.w, dv.w, rtol=0, atol=0)
                torch.testing.assert_close(velocity.c, dv.c, rtol=0, atol=0)
                # Dense multiplication is confined to this n=9 algebra test.
                left, right = engine.derivative_factors(state, velocity)
                torch.testing.assert_close(left @ right.T, dv.W, rtol=2e-13, atol=2e-14)

    def test_heun_interpolation_crossing_and_error_semantics(self):
        class Decay:
            @staticmethod
            def rhs(state):
                return DenseState(*(-value for value in state.tensors()))

            @staticmethod
            def predict(state, inputs):
                return state.w.reshape(1)

            inputs = torch.ones((1, 1), dtype=torch.float64)
            labels = torch.zeros(1, dtype=torch.float64)

        state = DenseState(*(torch.tensor(1., dtype=torch.float64) for _ in range(3)))
        first, second, euler, candidate = heun_trial(Decay(), state, .5)
        self.assertEqual(float(euler.w), .5)
        self.assertEqual(float(candidate.w), .625)
        self.assertEqual(float(heun_interpolant(state, first, second, .5, 0).w), 1.)
        self.assertEqual(float(heun_interpolant(state, first, second, .5, 1).w), .625)
        fraction, event, loss = locate_loss_crossing(Decay(), state, first, second, .5, .64)
        self.assertAlmostEqual(float(event.w), .8, places=9)
        self.assertAlmostEqual(loss, .64, places=9)
        self.assertGreater(fraction, 0.)
        self.assertLess(fraction, 1.)
        self.assertAlmostEqual(component_error(state, euler, candidate, .1, .01), .125/.11)
        with self.assertRaises(ValueError):
            locate_loss_crossing(Decay(), state, first, second, .5, .1)

    def test_own_state_roundtrip_has_identical_continuation(self):
        for engine in (self.dense(), self.moment(3)):
            state = engine.initial_state()
            state = heun_trial(engine, state, .01)[-1]
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory)/"state.npz"
                np.savez(path, **{name: value.numpy() for name, value in
                                zip(state.names(), state.tensors())})
                with np.load(path, allow_pickle=False) as archive:
                    fields = {name: torch.tensor(archive[name]) for name in state.names()}
                restored = DenseState(**fields) if isinstance(state, DenseState) else MomentState(**fields)
            expected = heun_trial(engine, state, .007)[-1]
            actual = heun_trial(engine, restored, .007)[-1]
            for left, right in zip(expected.tensors(), actual.tensors()):
                torch.testing.assert_close(left, right, rtol=0, atol=0)

    def test_max_time_output_and_validation_label_isolation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root/"prepared.npz"
            common = dict(train_inputs=self.inputs, train_labels=self.labels,
                          validation_inputs=self.inputs[:3], train_ids=np.arange(self.M),
                          validation_ids=np.arange(3))
            results = []
            for index, validation_labels in enumerate((np.zeros(3), np.full(3, 1000.))):
                np.savez(path, **common, validation_labels=validation_labels)
                args = parser().parse_args([
                    "--dataset", str(path), "--out", str(root/str(index)),
                    "--model", "moment", "--order", "2", "--width", "9",
                    "--max-time", ".025", "--initial-step", ".02", "--rtol", ".001",
                    "--target-loss", ".000001",
                ])
                args.atol = args.rtol*.01
                with contextlib.redirect_stdout(io.StringIO()):
                    summary = run(args)
                self.assertEqual(summary["status"], "max_time")
                self.assertEqual(summary["time"], .025)
                self.assertGreaterEqual(summary["integration_seconds_excluding_observations"], 0.)
                with np.load(root/str(index)/"arrays.npz", allow_pickle=False) as archive:
                    results.append({name: archive[name].copy()
                                    for name in ("w", "c", "A", "B", "C", "s", "times", "losses")})
            for name in results[0]:
                np.testing.assert_array_equal(results[0][name], results[1][name])
            loaded = load_dataset(path)
            self.assertEqual(loaded["train_inputs"].shape, (self.M, self.d))


if __name__ == "__main__":
    unittest.main(verbosity=2)
