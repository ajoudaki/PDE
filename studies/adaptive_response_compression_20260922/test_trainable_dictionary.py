"""Independent CPU checks for the trainable population dictionary model.

The differentiable oracle below spells out the scalar loss independently of
the model's forward/backward implementation. Test fixtures use general,
nonorthogonal dictionaries with unequal feature dimensions.
"""

from pathlib import Path
import importlib.util
import tempfile
import unittest

import numpy as np
import torch


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
NAMES = ("w", "c", "B1", "B2", "M")


def literal_fields(arrays, inputs):
    """No calls to model code; preserve the autograd graph."""
    n = arrays["w"].shape[0]
    h = torch.tanh(arrays["w"] @ inputs.T)
    a = arrays["B1"].T @ h / n
    v = arrays["M"] @ a
    H = torch.tanh(arrays["B2"] @ v)
    f = arrays["c"] @ H / n
    return h, a, v, H, f


def literal_loss(arrays, inputs, labels, probabilities):
    f = literal_fields(arrays, inputs)[-1]
    return torch.sum(probabilities * torch.square(f - labels))


def general_fixture(n=7, k1=2, k2=3, samples=8, seed=43821):
    rng = np.random.default_rng(seed)
    shapes = {"w": (n, 2), "c": (n,), "B1": (n, k1),
              "B2": (n, k2), "M": (k2, k1)}
    arrays = {name: torch.tensor(rng.normal(size=shape) * .35,
                                dtype=torch.float64)
              for name, shape in shapes.items()}
    # A shared offset makes nonorthogonality deliberate, not merely probable.
    arrays["B1"] += .2
    arrays["B2"] += .1
    inputs = torch.tensor(rng.normal(size=(samples, 2)), dtype=torch.float64)
    labels = torch.tensor(rng.normal(size=samples), dtype=torch.float64)
    probabilities = torch.arange(samples, dtype=torch.float64)
    probabilities /= probabilities.sum()
    return arrays, inputs, labels, probabilities


def autograd_velocity(arrays, inputs, labels, probabilities, *, train_bases=True):
    leaves = {name: value.detach().clone().requires_grad_()
              for name, value in arrays.items()}
    loss = literal_loss(leaves, inputs, labels, probabilities)
    derivatives = torch.autograd.grad(loss, tuple(leaves[name] for name in NAMES))
    n = arrays["w"].shape[0]
    gradients = dict(zip(NAMES, derivatives))
    velocity = {name: -gradients[name] * (1 if name == "M" else n)
                for name in NAMES}
    if not train_bases:
        velocity["B1"] = torch.zeros_like(velocity["B1"])
        velocity["B2"] = torch.zeros_like(velocity["B2"])
    return loss.detach(), gradients, velocity


def load_module(filename, name):
    spec = importlib.util.spec_from_file_location(name, filename)
    module = importlib.util.module_from_spec(spec)
    # Dataclass decorators inspect sys.modules during module execution.
    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


MODEL = load_module(STUDY / "trainable_dictionary.py", "checked_trainable_dictionary")
ORACLE = load_module(ROOT / "code/pde/observable_torch_p1.py", "checked_frozen_closure")
DIAGNOSTICS = {}


def model_state(arrays):
    return MODEL.State(arrays["w"].clone(), arrays["c"].clone(), arrays["M"].clone(),
                       arrays["B1"].clone(), arrays["B2"].clone())


def state_arrays(state):
    return {"w": state.w, "c": state.c, "B1": state.b1,
            "B2": state.b2, "M": state.M}


class TrainableDictionaryChecks(unittest.TestCase):
    def assert_tensor_equal(self, actual, expected, *, atol=2e-13, rtol=2e-12):
        torch.testing.assert_close(actual, expected, atol=atol, rtol=rtol)

    def test_forward_and_loss_at_general_unequal_rank_states(self):
        for n, k1, k2 in ((7, 2, 3), (5, 6, 12)):
            with self.subTest(n=n, k1=k1, k2=k2):
                arrays, inputs, labels, probabilities = general_fixture(n, k1, k2)
                state = model_state(arrays)
                MODEL.validate(state)
                actual = MODEL.forward(state, inputs)
                expected = literal_fields(arrays, inputs)
                for name, value in zip(("h", "a", "v", "H", "f"), expected):
                    self.assert_tensor_equal(actual[name], value)
                self.assert_tensor_equal(MODEL.loss(state, inputs, labels, probabilities),
                                         literal_loss(arrays, inputs, labels, probabilities))
                for block_size in (1, 3, 256):
                    self.assert_tensor_equal(MODEL.predict(state, inputs, block_size), expected[-1])

    def test_all_velocities_against_independent_autograd(self):
        max_error = 0.
        for n, k1, k2 in ((7, 2, 3), (5, 6, 12)):
            arrays, inputs, labels, probabilities = general_fixture(n, k1, k2)
            for weighted in (False, True):
                for train_bases in (False, True):
                    with self.subTest(n=n, weighted=weighted, train_bases=train_bases):
                        weights = probabilities if weighted else torch.full_like(probabilities, 1 / len(labels))
                        _, _, expected = autograd_velocity(arrays, inputs, labels, weights,
                                                           train_bases=train_bases)
                        actual = state_arrays(MODEL.rhs(model_state(arrays), inputs, labels,
                                              probabilities if weighted else None,
                                              train_basis=train_bases))
                        for name in NAMES:
                            self.assert_tensor_equal(actual[name], expected[name])
                            max_error = max(max_error, float((actual[name] - expected[name]).abs().max()))
        DIAGNOSTICS["autograd_max_absolute_error"] = max_error

    def test_each_field_by_central_directional_differences(self):
        arrays, inputs, labels, probabilities = general_fixture()
        state = model_state(arrays)
        velocity = state_arrays(MODEL.rhs(state, inputs, labels, probabilities))
        rng = np.random.default_rng(278113)
        errors = {}
        for name in NAMES:
            with self.subTest(name=name):
                direction = torch.tensor(rng.normal(size=arrays[name].shape), dtype=torch.float64)
                direction /= direction.norm()
                plus = {key: value.clone() for key, value in arrays.items()}
                minus = {key: value.clone() for key, value in arrays.items()}
                eps = 1e-5
                plus[name] += eps * direction
                minus[name] -= eps * direction
                difference = (literal_loss(plus, inputs, labels, probabilities) -
                              literal_loss(minus, inputs, labels, probabilities)) / (2 * eps)
                analytic = -(velocity[name] * direction).sum() / (1 if name == "M" else len(state.c))
                errors[name] = float((difference - analytic).abs())
                self.assert_tensor_equal(difference, analytic, atol=2e-10, rtol=2e-7)
        DIAGNOSTICS["directional_difference_errors"] = errors

    def test_continuous_energy_dissipation(self):
        arrays, inputs, labels, probabilities = general_fixture()
        state = model_state(arrays)
        for train_bases in (False, True):
            with self.subTest(train_bases=train_bases):
                _, gradients, _ = autograd_velocity(arrays, inputs, labels, probabilities,
                                                    train_bases=train_bases)
                velocity = state_arrays(MODEL.rhs(state, inputs, labels, probabilities,
                                                  train_basis=train_bases))
                derivative = sum((gradients[name] * velocity[name]).sum() for name in NAMES)
                negative_norm = -sum(velocity[name].square().sum() /
                                     (1 if name == "M" else len(state.c)) for name in NAMES)
                self.assert_tensor_equal(derivative, negative_norm)
                self.assertLess(float(derivative), 0.)
                eps = 1e-4
                plus = {name: arrays[name] + eps * velocity[name] for name in NAMES}
                minus = {name: arrays[name] - eps * velocity[name] for name in NAMES}
                difference = (literal_loss(plus, inputs, labels, probabilities) -
                              literal_loss(minus, inputs, labels, probabilities)) / (2 * eps)
                self.assert_tensor_equal(difference, negative_norm, atol=2e-10, rtol=2e-7)
                DIAGNOSTICS["trainable" if train_bases else "frozen"] = {
                    "energy_derivative": float(derivative),
                    "norm_identity_error": float((derivative - negative_norm).abs()),
                    "directional_difference_error": float((difference - negative_norm).abs())}

    def test_frozen_bases_reduce_to_maintained_closure(self):
        arrays, inputs, labels, probabilities = general_fixture(n=5, k1=6, k2=12)
        state = model_state(arrays)
        engine = ORACLE.ClosureEngine(arrays["B1"], arrays["w"], arrays["B2"],
                                     arrays["M"], block_size=3, forward_mode="direct")
        frozen_state = engine.state(arrays["w"], arrays["c"], arrays["M"])
        data = engine.prepare_data(inputs, labels, probabilities)
        self.assert_tensor_equal(MODEL.predict(state, inputs), engine.predict(frozen_state, data.inputs))
        actual = MODEL.rhs(state, inputs, labels, probabilities, train_basis=False)
        for implementation in ("reference", "optimized"):
            expected = engine.rhs(frozen_state, data, implementation=implementation)
            for name in ("w", "c", "M"):
                self.assert_tensor_equal(getattr(actual, name), getattr(expected, name))
        self.assertEqual(torch.count_nonzero(actual.b1).item(), 0)
        self.assertEqual(torch.count_nonzero(actual.b2).item(), 0)
        # heun_trial has a uniform-sample interface, so its oracle uses uniform data.
        uniform_data = engine.prepare_data(inputs, labels)
        step = .025
        candidate, error = MODEL.heun_trial(state, inputs, labels, step, state.M, 1e-4, 1e-6,
                                            train_basis=False)
        expected = engine.heun_step(frozen_state, uniform_data, step, implementation="reference")
        self.assertTrue(np.isfinite(error))
        for name in ("w", "c", "M"):
            self.assert_tensor_equal(getattr(candidate, name), getattr(expected, name))
        self.assert_tensor_equal(candidate.b1, state.b1, atol=0, rtol=0)
        self.assert_tensor_equal(candidate.b2, state.b2, atol=0, rtol=0)

    def test_five_array_checkpoint_reconstructs_forward_rhs_and_step(self):
        arrays, inputs, labels, probabilities = general_fixture(n=5, k1=6, k2=12)
        state = model_state(arrays)
        generated = ROOT / "data/generated" / STUDY.name / "verification"
        generated.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="restart-", dir=generated) as scratch:
            path = Path(scratch) / "state.npz"
            np.savez(path, **state.numpy(), inputs=inputs.numpy(), labels=labels.numpy(),
                     probabilities=probabilities.numpy())
            with np.load(path, allow_pickle=False) as archive:
                reconstructed = MODEL.State(*(torch.tensor(archive[name], dtype=torch.float64)
                                              for name in MODEL.NAMES))
                loaded_inputs, loaded_labels, loaded_probabilities = (
                    torch.tensor(archive[name], dtype=torch.float64)
                    for name in ("inputs", "labels", "probabilities"))
        for name in MODEL.NAMES:
            self.assert_tensor_equal(getattr(reconstructed, name), getattr(state, name), atol=0, rtol=0)
        self.assert_tensor_equal(MODEL.predict(reconstructed, loaded_inputs),
                                 MODEL.predict(state, inputs), atol=0, rtol=0)
        expected_rhs = MODEL.rhs(state, inputs, labels, probabilities)
        actual_rhs = MODEL.rhs(reconstructed, loaded_inputs, loaded_labels, loaded_probabilities)
        for name in MODEL.NAMES:
            self.assert_tensor_equal(getattr(actual_rhs, name), getattr(expected_rhs, name), atol=0, rtol=0)
        expected_step, expected_error = MODEL.heun_trial(state, inputs, labels, .025, state.M, 1e-4, 1e-6)
        actual_step, actual_error = MODEL.heun_trial(reconstructed, loaded_inputs, loaded_labels,
                                                    .025, state.M, 1e-4, 1e-6)
        self.assertEqual(actual_error, expected_error)
        for name in MODEL.NAMES:
            self.assert_tensor_equal(getattr(actual_step, name), getattr(expected_step, name), atol=0, rtol=0)
        # This fixture has nonzero c; both dictionaries must actually move.
        self.assertGreater(float((actual_step.b1 - state.b1).norm()), 0.)
        self.assertGreater(float((actual_step.b2 - state.b2).norm()), 0.)

    def test_runner_archives_restore_initial_metric_anchor(self):
        initial_path = ROOT / "data/generated/gradient_flow_probe_dictionary_20260921/suite_refined01/two_outliers_alternating_new_p3/arrays.npz"
        run_root = ROOT / "data/generated" / STUDY.name
        run_names = ("trainable_p3_primary01", "trainable_p3_refined01")
        if not all((run_root / name / "arrays.npz").is_file() for name in run_names):
            self.skipTest("Both authorized base-run archives are not yet available")
        with np.load(initial_path, allow_pickle=False) as archive:
            original = {name: archive[name][0].copy() if name in ("w", "c", "M")
                        else archive[name].copy() for name in MODEL.NAMES}
        for run_name in run_names:
            with self.subTest(run=run_name):
                with np.load(run_root / run_name / "arrays.npz", allow_pickle=False) as archive:
                    for name in MODEL.NAMES:
                        np.testing.assert_array_equal(archive[name][0], original[name])
                    saved_state = MODEL.State(*(torch.tensor(archive[name][-1], dtype=torch.float64)
                                                for name in MODEL.NAMES))
                    initial_M = torch.tensor(archive["M"][0], dtype=torch.float64)
                    inputs = torch.tensor(archive["training_inputs"], dtype=torch.float64)
                    labels = torch.tensor(archive["labels"], dtype=torch.float64)
                original_M = torch.tensor(original["M"], dtype=torch.float64)
                self.assert_tensor_equal(initial_M, original_M, atol=0, rtol=0)
                self.assertGreater(float((saved_state.M - initial_M).norm()), 0.)
                restored_arrays = saved_state.numpy()
                restored = MODEL.State(*(torch.tensor(restored_arrays[name], dtype=torch.float64)
                                         for name in MODEL.NAMES))
                expected, expected_error = MODEL.heun_trial(saved_state, inputs, labels, .01,
                                                            original_M, 1.5625e-5, 1.5625e-7)
                actual, actual_error = MODEL.heun_trial(restored, inputs, labels, .01,
                                                        initial_M, 1.5625e-5, 1.5625e-7)
                for name in MODEL.NAMES:
                    self.assert_tensor_equal(getattr(actual, name), getattr(expected, name), atol=0, rtol=0)
                self.assertEqual(actual_error, expected_error)
                DIAGNOSTICS[run_name + "_initial_arrays_exact"] = True
                DIAGNOSTICS[run_name + "_restored_Heun_error"] = actual_error


if __name__ == "__main__":
    import json
    torch.set_num_threads(1)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TrainableDictionaryChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps(DIAGNOSTICS, indent=2, sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)
