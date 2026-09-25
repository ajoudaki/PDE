"""Small deterministic equation/solver checks; no wide research training."""

import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from scipy.integrate import solve_ivp
import torch

import scalar_aggregate_engine as aggregate
from scalar_circle_probe_engine import forward_only
from scalar_wide_dense import (CanonicalDenseEngine, PROTOCOL_CUDA_LIMIT_BYTES,
                               PROTOCOL_RSS_LIMIT_BYTES, integrate, memory_status,
                               normalized_config, run)
from deep_circle_run import array_hash


def circle(angles):
    angles = np.asarray(angles)
    return np.column_stack((np.cos(angles), np.sin(angles)))


class DenseEquationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)
        os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False

    def setUp(self):
        self.params = aggregate.initialize_network(7, 2, depth=3, seed=59)
        self.inputs = circle([.17, .52, 1.31])
        self.labels = np.array([.3, -.5, .2])

    def assert_oracle(self, device):
        for moved in (False, True):
            params = tuple(value.copy() for value in self.params)
            if moved:
                # Non-negligible hidden velocities expose readout/mobility mistakes.
                params[-1][:] += np.linspace(-.7, .8, len(params[-1]))
            engine = CanonicalDenseEngine(params, self.inputs, self.labels, device=device)
            state = engine.initial_state()
            self.assertEqual(array_hash(*params), array_hash(*state.tensors()))
            fields = aggregate.network_fields(params, self.inputs)
            np.testing.assert_allclose(engine.predict(state, self.inputs).cpu().numpy(),
                                       fields["f"], rtol=2e-13, atol=2e-14)
            query = circle([0., .33, 2.7, 4.1])
            np.testing.assert_allclose(engine.predict(state, query).cpu().numpy(),
                                       forward_only(params, query), rtol=2e-13, atol=2e-14)
            for actual, wanted in zip(engine.rhs(state).tensors(),
                                      aggregate.network_rhs(params, self.inputs, self.labels)):
                np.testing.assert_allclose(actual.cpu().numpy(), wanted, rtol=3e-13, atol=2e-14)

    def test_cpu_matches_numpy_initialization_prediction_and_rhs(self):
        self.assert_oracle("cpu")

    @unittest.skipUnless(torch.cuda.is_available(), "CUDA unavailable; run explicitly on a free GPU")
    def test_gpu_matches_numpy_and_cpu(self):
        device = os.environ.get("SCALAR_TEST_CUDA_DEVICE", "cuda:0")
        self.assert_oracle(device)
        cpu = CanonicalDenseEngine(self.params, self.inputs, self.labels, device="cpu")
        gpu = CanonicalDenseEngine(self.params, self.inputs, self.labels, device=device)
        for a, b in zip(cpu.rhs(cpu.initial_state()).tensors(), gpu.rhs(gpu.initial_state()).tensors()):
            np.testing.assert_allclose(a.numpy(), b.cpu().numpy(), rtol=3e-13, atol=2e-14)

    def test_mse_derivative_and_mobility_against_autograd(self):
        params = tuple(value.copy() for value in self.params)
        params[-1][:] += np.linspace(-.7, .8, len(params[-1]))
        engine = CanonicalDenseEngine(params, self.inputs, self.labels, device="cpu")
        velocity = engine.rhs(engine.initial_state()).tensors()
        tensors = [torch.tensor(value, dtype=torch.float64, requires_grad=True) for value in params]
        value = torch.tensor(self.inputs.T, dtype=torch.float64)
        for matrix in tensors[:-1]:
            value = torch.tanh(matrix @ value)
        output = tensors[-1] @ value / engine.n
        loss = ((output-torch.tensor(self.labels))**2).mean()
        gradients = torch.autograd.grad(loss, tensors)
        mobilities = (engine.n, 1, 1, engine.n)
        for v, gradient, mobility in zip(velocity, gradients, mobilities):
            torch.testing.assert_close(v, -mobility*gradient, rtol=3e-13, atol=2e-14)
        derivative = sum(float((gradient*v).sum()) for gradient, v in zip(gradients, velocity))
        fields = aggregate.network_fields(params, self.inputs)
        residual = fields["f"]-self.labels
        wanted = -4/engine.M**2 * residual @ fields["Theta"] @ residual
        self.assertAlmostEqual(derivative, wanted, delta=2e-13)
        self.assertLess(derivative, 0.)
        self.assertAlmostEqual(derivative, -sum(float(v.square().sum())/mobility
                                               for v, mobility in zip(velocity, mobilities)), delta=2e-13)

    def test_zero_residual_is_stationary(self):
        labels = aggregate.network_fields(self.params, self.inputs)["f"]
        engine = CanonicalDenseEngine(self.params, self.inputs, labels, device="cpu")
        for value in engine.rhs(engine.initial_state()).tensors():
            self.assertLess(float(value.abs().max()), 1e-15)


class DenseStoppingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)
        cls.inputs = circle([.2, 1.2])
        cls.labels = np.array([.15, -.12])
        cls.params = aggregate.initialize_network(5, 2, depth=3, seed=31)

    def config(self, **overrides):
        return normalized_config(dict(inputs=self.inputs.tolist(), labels=self.labels.tolist(),
                                      width=5, seed=31, device="cpu", max_time=256.,
                                      max_wall_seconds=60., **overrides))

    def solve(self, **overrides):
        config = self.config(**overrides)
        engine = CanonicalDenseEngine(self.params, self.inputs, self.labels, device="cpu")
        state, trace, result = integrate(engine, config)
        return engine, state, trace, result

    def test_first_downward_fit_and_tolerance_agreement_with_numpy_ivp(self):
        coarse = self.solve(rtol=2e-5, atol=2e-7)
        fine = self.solve(rtol=5e-6, atol=5e-8)
        shapes = tuple(value.shape for value in self.params)

        def rhs(t, state):
            params = aggregate.unflatten_network(state, shapes)
            return aggregate.flatten_network(aggregate.network_rhs(params, self.inputs, self.labels))

        def event(t, state):
            params = aggregate.unflatten_network(state, shapes)
            return np.mean((forward_only(params, self.inputs)-self.labels)**2)-1e-6

        event.direction, event.terminal = -1, True
        reference = solve_ivp(rhs, (0, 256.), aggregate.flatten_network(self.params),
                              method="DOP853", rtol=2e-11, atol=2e-13, events=event)
        self.assertEqual(reference.status, 1)
        reference_time = reference.t[-1]
        reference_params = aggregate.unflatten_network(reference.y[:, -1], shapes)
        query = circle(2*np.pi*(np.arange(32)+.371)/32)
        reference_f = forward_only(reference_params, query)
        differences = []
        for engine, state, trace, result in (coarse, fine):
            self.assertEqual(result["status"], "fitted")
            self.assertTrue(np.all(trace["losses"][:-1] > 1e-6))
            self.assertLessEqual(trace["losses"][-1], 1e-6)
            self.assertGreater(trace["losses"][-1], 1e-6*(1-1e-7))
            self.assertTrue(np.all(np.diff(trace["times"]) > 0))
            self.assertGreater(result["crossing_bracket"]["left_loss"], 1e-6)
            self.assertLessEqual(result["crossing_bracket"]["right_loss"], 1e-6)
            prediction = engine.predict(state, query).numpy()
            differences.append(np.max(np.abs(prediction-reference_f)))
            self.assertLess(abs(result["time"]-reference_time)/reference_time, .001)
            self.assertLess(differences[-1], 2e-4)
        self.assertLess(differences[1], differences[0])
        self.assertLess(abs(coarse[-1]["time"]-fine[-1]["time"])/fine[-1]["time"], .001)

    def test_caps_and_initially_fitted_are_not_crossings(self):
        _, _, trace, result = self.solve(max_steps=1)
        self.assertEqual(result["status"], "max_steps")
        self.assertEqual(len(trace["times"]), 2)
        self.assertIsNone(result["crossing_bracket"])
        _, _, trace, result = self.solve(target_loss=1.)
        self.assertEqual(result["status"], "initially_below_target")
        self.assertEqual(len(trace["times"]), 1)
        self.assertIsNone(result["crossing_bracket"])

    def test_normalization_is_rejected_not_silently_changed(self):
        with self.assertRaisesRegex(ValueError, "already"):
            normalized_config(dict(inputs=(self.inputs/np.sqrt(2)).tolist(), labels=self.labels.tolist()))

    def test_memory_cap_stops_before_a_trial_and_cannot_exceed_protocol(self):
        config = self.config(max_process_rss_bytes=1)
        engine = CanonicalDenseEngine(self.params, self.inputs, self.labels, device="cpu")
        with patch("scalar_wide_dense.heun_trial") as trial:
            _, trace, result = integrate(engine, config)
        trial.assert_not_called()
        self.assertEqual(result["status"], "memory_limit")
        self.assertFalse(result["resource_limits_satisfied"])
        self.assertEqual(len(trace["times"]), 1)
        self.assertIn("peak_process_rss_bytes", result["memory_limit_violations"])
        for key, ceiling in (("max_process_rss_bytes", PROTOCOL_RSS_LIMIT_BYTES),
                             ("max_cuda_allocated_bytes", PROTOCOL_CUDA_LIMIT_BYTES)):
            with self.assertRaisesRegex(ValueError, "protocol ceiling"):
                self.config(**{key: ceiling+1})

    def test_cuda_memory_guard_without_gpu_work(self):
        config = self.config()
        with patch("torch.cuda.max_memory_allocated", return_value=PROTOCOL_CUDA_LIMIT_BYTES), \
             patch("torch.cuda.max_memory_reserved", return_value=PROTOCOL_CUDA_LIMIT_BYTES):
            usage, violations = memory_status("cuda:1", config)
        self.assertEqual(usage["peak_cuda_allocated_bytes"], PROTOCOL_CUDA_LIMIT_BYTES)
        self.assertIn("peak_cuda_allocated_bytes", violations)

    def test_setup_and_readout_memory_excess_cannot_report_a_valid_fit(self):
        scratch = Path(__file__).resolve().parents[2]/"data/generated/neural_response_memory_20260922"
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="scalar_wide_dense_test_", dir=scratch) as temporary:
            output = Path(temporary)/"setup"
            with patch("scalar_wide_dense.integrate") as solver:
                result = run(self.config(max_process_rss_bytes=1), output)
            solver.assert_not_called()
            self.assertEqual(result["status"], "memory_limit")
            self.assertEqual(result["memory_limit_phase"], "initialization")
            self.assertFalse(result["scientific_validity"])
            self.assertFalse((output/"trajectory.npz").exists())

            def fake_integrate(engine, config):
                return engine.initial_state(), dict(times=np.array([0.]), losses=np.array([1e-6])), \
                    dict(status="fitted", time=0., training_mse=1e-6, accepted=0, rejected=0)

            usage = dict(peak_process_rss_bytes=0, peak_cuda_allocated_bytes=0, peak_cuda_reserved_bytes=0)
            excess_usage = dict(usage, peak_process_rss_bytes=PROTOCOL_RSS_LIMIT_BYTES)
            violations = dict(peak_process_rss_bytes=dict(observed_bytes=PROTOCOL_RSS_LIMIT_BYTES,
                                                          limit_bytes=PROTOCOL_RSS_LIMIT_BYTES))
            output = Path(temporary)/"readout"
            with patch("scalar_wide_dense.integrate", side_effect=fake_integrate), \
                 patch("scalar_wide_dense.memory_status", side_effect=[
                     (usage, {}), (usage, {}), (excess_usage, violations)]):
                result = run(self.config(grid_angles=[0., 1.], off_grid_angles=[.2]), output)
            self.assertEqual(result["status"], "memory_limit")
            self.assertEqual(result["memory_limit_phase"], "readout")
            self.assertFalse(json.loads((output/"result.json").read_text())["scientific_validity"])
            self.assertFalse((output/"trajectory.npz").exists())


if __name__ == "__main__":
    unittest.main()
