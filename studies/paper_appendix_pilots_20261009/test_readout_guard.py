"""Bounded CPU regressions for the paper's corrected-readout safeguards.

Run with ``python studies/paper_appendix_pilots_20261009/test_readout_guard.py``.
These checks use full-retention states and no experiment or source archives.
"""

import importlib.util
import contextlib
import io
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import torch


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "paper_capture_readout_guard", ROOT / "paper/figures/capture_trajectory.py"
)
capture = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(capture)


class ReadoutGuardChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous_threads = torch.get_num_threads()
        torch.set_num_threads(1)

    @classmethod
    def tearDownClass(cls):
        torch.set_num_threads(cls.previous_threads)

    def setUp(self):
        self.inputs = torch.tensor([[1., 0.], [.6, .8]], dtype=torch.float64)
        self.labels = torch.tensor([.1, -.08], dtype=torch.float64)
        self.queries = torch.tensor([[0., 1.], [-.8, .6]], dtype=torch.float64)

    def model(self, kind, inputs=None, seed=0, scale=1., depth=2, floor=None,
              dtype=torch.float64):
        inputs = self.inputs if inputs is None else inputs
        inputs, labels = inputs.to(dtype=dtype), self.labels.to(dtype=dtype)
        dense = capture.DeepDense(12, 2, depth, "tanh", seed, torch.device("cpu"))
        dense.initial_state = [value.to(dtype=dtype) for value in dense.initial_state]
        dense.initial_state[0].mul_(scale)
        if kind == "Harmonic":
            return capture.Harmonic(dense, inputs, labels, budget=12)
        return capture.DeepHarmonic(
            dense, inputs, labels, None, budget=12, readout_floor=floor
        )

    def close(self, actual, expected):
        torch.testing.assert_close(actual, expected, atol=2e-12, rtol=2e-11)

    @staticmethod
    def features(state, inputs):
        # Evaluate the tanh forward pass without the implementation's helpers.
        hs = [(state[0] @ inputs.T).tanh()]
        for mixer in state[2:-1]:
            hs.append((mixer @ hs[-1]).tanh())
        return hs

    def old_cholesky_oracle(self, model, state):
        """The pre-guard arithmetic, including the metric backward equations."""
        hs = self.features(state, self.inputs)
        metric = model.metrics[-1]
        normalized = hs[-1] / math.sqrt(len(self.labels))
        gram = normalized.T @ (metric @ normalized)
        gram = (gram + gram.T) / 2
        factor = torch.linalg.cholesky(gram)
        correction = (self.labels - state[-1]) / math.sqrt(len(self.labels))
        correction -= normalized.T @ (metric @ state[1])
        readout = state[1] + normalized @ torch.cholesky_solve(
            correction[:, None], factor
        ).flatten()

        deltas = [None] * len(hs)
        deltas[-1] = readout[:, None] * (1 - hs[-1].square())
        for layer in range(len(hs) - 2, -1, -1):
            deltas[layer] = (1 - hs[layer].square()) * (
                model.metric_inverses[layer]
                @ (state[layer + 2].T @ (model.metrics[layer + 1] @ deltas[layer + 1]))
            )
        scale, deficit = 2 / len(self.labels), state[-1]
        kernel = hs[-1].T @ (metric @ hs[-1])
        kernel += (deltas[0].T @ (model.metrics[0] @ deltas[0])) * (
            self.inputs @ self.inputs.T
        )
        updates = [
            scale * (deltas[0] * deficit) @ self.inputs,
            scale * hs[-1] @ deficit,
        ]
        for layer in range(1, len(hs)):
            incoming = model.metrics[layer - 1] @ hs[layer - 1]
            updates.append(scale * (deltas[layer] * deficit) @ incoming.T)
            kernel += (deltas[layer].T @ (model.metrics[layer] @ deltas[layer])) * (
                hs[layer - 1].T @ incoming
            )
        updates.append(-scale * kernel @ deficit)
        predictions = (metric @ readout) @ self.features(state, self.queries)[-1]
        return readout, gram, predictions, updates

    def test_dependent_inputs_rejected_at_initialization(self):
        for kind in ("DeepHarmonic", "Harmonic"):
            for seed in (0, 1, 10):
                for second in ((1., 0.), (-1., 0.), (0., 0.), (1., 1e-10)):
                    with self.subTest(kind=kind, seed=seed, second=second):
                        inputs = torch.tensor([[1., 0.], second], dtype=torch.float64)
                        with self.assertRaisesRegex(ArithmeticError, "rank deficient"):
                            self.model(kind, inputs=inputs, seed=seed)

    def test_valid_small_scale_is_accepted(self):
        for kind in ("DeepHarmonic", "Harmonic"):
            with self.subTest(kind=kind):
                model = self.model(kind, scale=1e-6)
                state = [value.clone() for value in model.initial_state]
                state[-1].zero_()
                self.close(model.predict(state, self.inputs, self.inputs, self.labels), self.labels)
                self.assertTrue(all(bool(torch.isfinite(value).all()) for value in
                                    model.rhs(state, self.inputs, self.labels)))

    def test_well_conditioned_float32_state_is_accepted_without_dtype_change(self):
        inputs, labels = self.inputs.float(), self.labels.float()
        for kind in ("DeepHarmonic", "Harmonic"):
            with self.subTest(kind=kind):
                model = self.model(kind, dtype=torch.float32)
                state = [value.clone() for value in model.initial_state]
                state[1].add_(.02)
                state[-1].mul_(.37)
                before = [value.clone() for value in state]
                readout = model._readout(state, inputs, labels)
                self.assertEqual(readout[0].dtype, torch.float32)
                self.assertEqual(readout[-1].dtype, torch.float32)
                prediction = model.predict(state, inputs, inputs, labels)
                torch.testing.assert_close(prediction, labels-state[-1], atol=2e-6, rtol=2e-5)
                for value in model.rhs(state, inputs, labels):
                    self.assertEqual(value.dtype, torch.float32)
                    self.assertTrue(bool(torch.isfinite(value).all()))
                self.assertTrue(all(torch.equal(old, current) for old, current in zip(before, state)))

    def test_rank_loss_after_initialization_rejected_by_every_entry_point(self):
        for kind in ("DeepHarmonic", "Harmonic"):
            model = self.model(kind)
            state = [value.clone() for value in model.initial_state]
            state[0].zero_()
            operations = {
                "readout": lambda: model._readout(state, self.inputs, self.labels),
                "predict": lambda: model.predict(state, self.queries, self.inputs, self.labels),
                "rhs": lambda: model.rhs(state, self.inputs, self.labels),
                "prepare_query": lambda: model.prepare_query(state, self.inputs, self.labels),
            }
            for operation, call in operations.items():
                with self.subTest(kind=kind, operation=operation):
                    with self.assertRaisesRegex(ArithmeticError, "rank deficient"):
                        call()

    def test_valid_nonzero_state_preserves_old_cholesky_arithmetic(self):
        for kind, depth in (("Harmonic", 2), ("DeepHarmonic", 2), ("DeepHarmonic", 3)):
            with self.subTest(kind=kind, depth=depth):
                model = self.model(kind, seed=17, depth=depth)
                state = [value.clone() for value in model.initial_state]
                state[0].add_(.003)
                state[1].copy_(torch.linspace(-.03, .04, len(state[1]), dtype=torch.float64))
                for mixer in state[2:-1]:
                    mixer.add_(.002)
                state[-1].copy_(.37 * self.labels)
                readout, gram, predictions, updates = self.old_cholesky_oracle(model, state)
                actual_readout = model._readout(state, self.inputs, self.labels)
                self.close(actual_readout[0], readout)
                self.close(actual_readout[-1], gram)
                self.close(model.predict(state, self.queries, self.inputs, self.labels), predictions)
                self.close(model.prepare_query(state, self.inputs, self.labels)(self.queries), predictions)
                self.close(model.predict(state, self.inputs, self.inputs, self.labels),
                           self.labels - state[-1])
                actual_updates = model.rhs(state, self.inputs, self.labels)
                self.assertEqual(len(actual_updates), len(updates))
                for actual, expected in zip(actual_updates, updates):
                    self.close(actual, expected)

    def test_inaccurate_or_nonfinite_reconstruction_rejected(self):
        for kind in ("DeepHarmonic", "Harmonic"):
            model = self.model(kind)
            state = [value.clone() for value in model.initial_state]
            state[-1].zero_()
            for wrong_value in (0., float("nan")):
                with self.subTest(kind=kind, wrong_value=wrong_value):
                    def incorrect_solution(rhs, factor):
                        return torch.full_like(rhs, wrong_value)

                    with patch.object(torch, "cholesky_solve", side_effect=incorrect_solution):
                        with self.assertRaisesRegex(ArithmeticError, "training identity"):
                            model._readout(state, self.inputs, self.labels)

    def test_regularized_deep_harmonic_duplicate_inputs_remain_callable(self):
        inputs = self.inputs[:1].repeat(2, 1)
        model = self.model("DeepHarmonic", inputs=inputs, floor=1e-5)
        state = [value.clone() for value in model.initial_state]
        state[1].add_(.03)
        state[-1].mul_(.37)
        predictions = model.predict(state, self.queries, inputs, self.labels)
        self.assertTrue(bool(torch.isfinite(predictions).all()))
        self.close(model.prepare_query(state, inputs, self.labels)(self.queries), predictions)
        self.assertTrue(all(bool(torch.isfinite(value).all()) for value in
                            model.rhs(state, inputs, self.labels)))

    def test_explicit_harmonic_runtime_dtype_config_and_cli(self):
        for dtype in (None, "float32", "float64"):
            with self.subTest(dtype=dtype):
                config = capture._experiment_merge(capture.EXPERIMENT_DEFAULTS, {
                    "methods": {"non_oblivious": {"harmonic": {"runtime_dtype": dtype}}}
                })
                capture._experiment_validate(config)
                cli = [] if dtype is None else [
                    "--methods.non_oblivious.harmonic.runtime_dtype", dtype
                ]
                cli_config, _ = capture._experiment_config(cli)
                self.assertEqual(cli_config, config)
                self.assertEqual(config["training"]["dtype"], "float32")
                for family in ("harmonic", "logarithmic"):
                    self.assertEqual(capture._experiment_setup(config, family)["rollout_dtype"], "float32")
                self.assertNotIn("runtime_dtype", config["methods"]["non_oblivious"]["logarithmic"])

        legacy = capture._experiment_merge(capture.EXPERIMENT_DEFAULTS, {})
        del legacy['methods']['non_oblivious']['harmonic']['runtime_dtype']
        capture._experiment_validate(legacy)

        invalid = capture._experiment_merge(capture.EXPERIMENT_DEFAULTS, {
            "methods": {"non_oblivious": {"harmonic": {"runtime_dtype": "float16"}}}
        })
        with self.assertRaisesRegex(ValueError, "Harmonic runtime_dtype"):
            capture._experiment_validate(invalid)
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                capture._experiment_config([
                    "--methods.non_oblivious.harmonic.runtime_dtype", "float16"
                ])
        self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
