"""Deterministic CPU algebra/restart checks; no benchmark training."""
import io
import unittest
from unittest.mock import patch
import numpy as np
import torch
from factor_control_engine import FactorEngine, FactorState, heun_trial
from run_factor_control import integrate


class FactorControlTests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        rng = np.random.default_rng(71)
        self.engine = FactorEngine(2, 11, 3, rng.standard_normal((4, 2))/np.sqrt(2), rng.standard_normal(4))
        self.state = self.engine.initial_state()
        self.state.A.copy_(torch.tensor(rng.standard_normal((11, 3))*.1))

    def test_forward_transpose(self):
        engine, state = self.engine, self.state
        values = torch.arange(55, dtype=torch.float64).reshape(11, 5)/31
        dense = engine.W0+state.A@state.B
        torch.testing.assert_close(engine.apply_hidden(state, values), dense@values)
        torch.testing.assert_close(engine.apply_hidden(state, values, transpose=True), dense.T@values)

    def test_autograd_energy_and_induced_velocity(self):
        engine = self.engine
        state = FactorState(*(x.clone().requires_grad_() for x in self.state.tensors()))
        dense = engine.W0+state.A@state.B
        h1 = torch.tanh(state.w@engine.inputs.T)
        prediction = state.c@torch.tanh(dense@h1)/engine.n
        loss = (prediction-engine.labels).square().mean()
        gradients = torch.autograd.grad(loss, (*state.tensors(), dense), retain_graph=True)
        velocity = engine.rhs(state)
        mobilities = (engine.n, engine.n, 1, 1)
        for actual, gradient, mobility in zip(velocity.tensors(), gradients[:4], mobilities):
            torch.testing.assert_close(actual, -mobility*gradient, rtol=1e-12, atol=1e-13)
        energy_derivative = sum((g*v).sum() for g, v in zip(gradients[:4], velocity.tensors()))
        dissipation = -sum(v.square().sum()/m for v, m in zip(velocity.tensors(), mobilities))
        torch.testing.assert_close(energy_derivative, dissipation, rtol=1e-12, atol=1e-13)
        induced = velocity.A@state.B+state.A@velocity.B
        expected = -gradients[4]@state.B.T@state.B-state.A@state.A.T@gradients[4]
        torch.testing.assert_close(induced, expected, rtol=1e-12, atol=1e-13)

    def test_initialization_and_nested_directions(self):
        engine = self.engine
        rng = np.random.default_rng(20260920)
        initial = engine.initial_state()
        np.testing.assert_array_equal(initial.w.numpy(), rng.standard_normal((11, 2)))
        np.testing.assert_array_equal(engine.W0.numpy(), rng.standard_normal((11, 11))/np.sqrt(11))
        np.testing.assert_array_equal(initial.c.numpy(), rng.standard_normal(11)/11)
        np.testing.assert_array_equal(initial.B.numpy(), np.random.default_rng(20260924).standard_normal((3, 11))/np.sqrt(3))
        large = FactorEngine(2, 11, 7, engine.inputs, engine.labels).initial_state()
        torch.testing.assert_close(initial.B*np.sqrt(3), large.B[:3]*np.sqrt(7), rtol=1e-15, atol=1e-15)
        self.assertEqual(float((initial.A@initial.B).norm()), 0.)
        velocity = engine.rhs(initial)
        self.assertGreater(float(velocity.A.norm()), 0.)
        self.assertEqual(float(velocity.B.norm()), 0.)
        initial.B.zero_()
        both_zero = engine.rhs(initial)
        self.assertEqual(float(both_zero.A.norm()+both_zero.B.norm()), 0.)

    def test_physical_error_and_own_restart(self):
        engine, state = self.engine, self.state
        step, rtol, atol = .01, 1e-4, 1e-6
        euler = state.add_scaled(engine.rhs(state), step)
        candidate, ratio = heun_trial(engine, state, step, rtol, atol)
        raw = [float((c-b).square().mean().sqrt()/(atol+rtol*max(float(a.square().mean().sqrt()),
                    float(c.square().mean().sqrt()), 1.))) for a,b,c in zip(state.tensors(), euler.tensors(), candidate.tensors())]
        dense_error = (candidate.A@candidate.B-euler.A@euler.B).norm()
        scale = max(float((state.A@state.B).norm()), float((candidate.A@candidate.B).norm()), 1.)
        self.assertAlmostEqual(ratio, max(*raw, float(dense_error)/(atol+rtol*scale)), places=10)
        buffer = io.BytesIO()
        np.savez(buffer, **{k:x.numpy() for k,x in zip(candidate.names(), candidate.tensors())})
        buffer.seek(0)
        with np.load(buffer, allow_pickle=False) as archive:
            restored = FactorState(*(engine.tensor(archive[name]) for name in candidate.names()))
        restart_engine = FactorEngine(2, 11, 3, engine.inputs, engine.labels)
        for a,b in zip(engine.rhs(candidate).tensors(), restart_engine.rhs(restored).tensors()):
            torch.testing.assert_close(a, b, rtol=0, atol=0)
        for a,b in zip(heun_trial(engine,candidate,step,rtol,atol)[0].tensors(),
                       heun_trial(restart_engine,restored,step,rtol,atol)[0].tensors()):
            torch.testing.assert_close(a, b, rtol=0, atol=0)

    def test_caps_preserve_accepted_state(self):
        engine, state = self.engine, self.state
        stopped, arrays, summary = integrate(engine, state, engine.inputs.numpy(), [0.], 1e-4, 1e-6, max_steps=0)
        self.assertEqual(summary["status"], "step_cap")
        self.assertEqual(arrays["losses"].shape, (1,))
        for a,b in zip(state.tensors(), stopped.tensors()):
            torch.testing.assert_close(a,b,rtol=0,atol=0)

    def test_invalid_trials_record_numerical_failure(self):
        engine, state = self.engine, self.state
        with patch("run_factor_control.heun_trial", side_effect=ValueError("deliberate invalid trial")):
            stopped, _, summary = integrate(engine, state, engine.inputs.numpy(), [0.], 1e-4, 1e-6)
        self.assertEqual(summary["status"], "numerical_failure")
        self.assertGreater(summary["rejected"], 0)
        self.assertEqual(summary["accepted"], 0)
        for a,b in zip(state.tensors(), stopped.tensors()):
            torch.testing.assert_close(a,b,rtol=0,atol=0)


if __name__ == "__main__":
    unittest.main()
