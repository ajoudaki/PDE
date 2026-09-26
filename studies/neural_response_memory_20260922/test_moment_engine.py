"""Small deterministic CPU identities; no training or GPU launches."""

import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import numpy as np
import torch

from moment_engine import (MomentEngine, MomentState, factor_action,
                           factor_frobenius, linear_combination)


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_network import initialize, forward, flow_velocity


class MomentEngineTests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        self.n, self.d, self.M, self.P = 9, 3, 5, 3
        rng = np.random.default_rng(12)
        self.inputs = rng.normal(size=(self.M, self.d))/np.sqrt(self.d)
        self.labels = rng.normal(size=self.M)

    def engine(self, lifted=False, labels=None):
        return MomentEngine(self.d, self.n, self.P, self.inputs,
                            self.labels if labels is None else labels, lifted=lifted)

    def close(self, left, right, *, atol=2e-12, rtol=2e-11):
        torch.testing.assert_close(torch.as_tensor(left), torch.as_tensor(right), atol=atol, rtol=rtol)

    def noninitial(self, engine):
        state = engine.initial_state()
        generator = torch.Generator().manual_seed(101)
        state.C = torch.linspace(.2, .4, self.P, dtype=torch.float64)
        state.A = state.C[:, None, None]*torch.randn(state.A.shape, generator=generator, dtype=torch.float64)*.1
        state.B = state.C[:, None, None]*(engine.h10[None]+torch.randn(state.B.shape, generator=generator, dtype=torch.float64)*.2)
        state.s.fill_(.4)
        state.w += .02*torch.randn(state.w.shape, generator=generator, dtype=torch.float64)
        state.c += .02*torch.randn(state.c.shape, generator=generator, dtype=torch.float64)
        if engine.lifted:
            state.h1 = torch.tanh(state.w @ engine.inputs.T)
            state.h2 = torch.tanh(engine.apply_hidden(state, state.h1))
            state.rho = torch.sqrt((state.c @ state.h2/engine.n-engine.labels).square().mean())
        return state

    def test_canonical_initialization_and_initial_derivative(self):
        engine = self.engine()
        state = engine.initial_state()
        canonical = initialize(self.n, 2, self.d, seed=20260920)
        self.close(state.w, canonical.weights[0], atol=0, rtol=0)
        self.close(engine.W0, canonical.weights[1], atol=0, rtol=0)
        self.close(state.c, canonical.readout, atol=0, rtol=0)
        inputs = self.inputs.T*np.sqrt(self.d)
        reference = flow_velocity(canonical, inputs, self.labels)
        velocity = engine.rhs(state)
        self.close(velocity.w, reference.weights[0])
        self.close(velocity.c, reference.readout)
        left, right = engine.derivative_factors(state, velocity)
        self.close(left @ right.T, reference.weights[1])
        self.close(engine.predict(state, self.inputs), forward(canonical, inputs).output)
        self.close(engine.defect_frobenius(state), torch.zeros((), dtype=torch.float64))
        for value in engine.moment_diagnostics(state).values():
            self.close(value, torch.zeros_like(value), atol=0, rtol=0)
        self.assertEqual(engine.eta, 1e-3/self.P**6)

    def test_factor_actions_transpose_and_arbitrary_query(self):
        engine = self.engine()
        state = self.noninitial(engine)
        dense = engine.reconstruct_delta_for_diagnostics(state)
        generator = torch.Generator().manual_seed(27)
        x = torch.randn((self.n, 4), generator=generator, dtype=torch.float64)
        y = torch.randn((self.n, 4), generator=generator, dtype=torch.float64)
        self.close(engine.apply_delta(state, x), dense @ x)
        self.close(engine.apply_delta(state, y, transpose=True), dense.T @ y)
        self.close((y*engine.apply_delta(state, x)).sum(),
                   (engine.apply_delta(state, y, transpose=True)*x).sum())
        panel = torch.randn((7, self.d), generator=generator, dtype=torch.float64)
        expected = state.c @ torch.tanh((engine.W0+dense) @ torch.tanh(state.w @ panel.T))/self.n
        self.close(engine.predict(state, panel), expected)
        self.close(factor_frobenius(*engine.delta_factors(state), block_size=4), torch.linalg.norm(dense))

    def test_defect_product_rule_and_finite_difference(self):
        engine = self.engine()
        state = self.noninitial(engine)
        velocity = engine.rhs(state)
        left, right = engine.derivative_factors(state, velocity)
        delta_dot = left @ right.T
        fields = engine.fields(state)
        full_velocity = (-2/(self.M*self.n))*(fields["delta2"]*fields["r"]) @ fields["h1"].T
        el, er = engine.defect_factors(state)
        self.close(delta_dot-full_velocity, el @ er.T)
        self.close(engine.defect_frobenius(state, block_size=4), torch.linalg.norm(delta_dot-full_velocity))
        eps = 2e-6
        finite_difference = (engine.reconstruct_delta_for_diagnostics(state.add_scaled(velocity, eps))
                             -engine.reconstruct_delta_for_diagnostics(state.add_scaled(velocity, -eps)))/(2*eps)
        self.close(finite_difference, delta_dot, atol=5e-12, rtol=5e-9)

    def test_lifted_tangency_by_autograd_and_rational_rhs(self):
        engine = self.engine(lifted=True)
        state = self.noninitial(engine)
        velocity = engine.rhs(state)

        def recompute(w, c, A, B, C, s):
            h1 = torch.tanh(w @ engine.inputs.T)
            learned = (-2/(engine.M*engine.n))*torch.einsum("pim,pjm,p->ij", A, B, C.reciprocal())
            h2 = torch.tanh((engine.W0+learned) @ h1)
            r = c @ h2/engine.n-engine.labels
            return h1, h2, torch.sqrt(r.square().mean())

        base = state.tensors()[:6]
        tangent = velocity.tensors()[:6]
        _, expected = torch.autograd.functional.jvp(recompute, base, tangent)
        for actual, reference in zip((velocity.h1, velocity.h2, velocity.rho), expected):
            self.close(actual, reference)
        # The lifted RHS must not evaluate either nonrational initialization map.
        with patch("torch.tanh", side_effect=AssertionError("tanh in lifted RHS")), \
             patch("torch.sqrt", side_effect=AssertionError("sqrt in lifted RHS")), \
             patch.object(engine, "reconstruct_delta_for_diagnostics", side_effect=AssertionError("dense reconstruction in RHS")):
            rational_velocity = engine.rhs(state)
        for actual, reference in zip(rational_velocity.tensors(), velocity.tensors()):
            self.close(actual, reference, atol=0, rtol=0)
        diagnostics = engine.lift_diagnostics(state)
        for name in ("h1_max", "h2_max", "rho_abs", "rho_recomputed_abs"):
            self.close(diagnostics[name], torch.zeros((), dtype=torch.float64), atol=0, rtol=0)

    def test_derivative_memory_identities(self):
        engine = self.engine(lifted=True)
        state = self.noninitial(engine)
        velocity = engine.rhs(state)

        def memory_and_q(*values):
            current = MomentState(*values)
            q = (current.c[:, None]*(1-current.h2.square())
                 *(current.c @ current.h2/engine.n-engine.labels)/current.rho)
            D1 = current.C[:, None, None]*current.h1[None]-current.B
            D2 = current.C[:, None, None]*q[None]-current.A-engine.eta*engine.q0[None]
            return D1, D2, q

        _, (D1dot, D2dot, qdot) = torch.autograd.functional.jvp(memory_and_q, state.tensors(), velocity.tensors())
        self.close(D1dot, state.C[:, None, None]*velocity.h1[None])
        self.close(D2dot, state.C[:, None, None]*qdot[None])

    def test_stationary_zero_residual_and_state_operations(self):
        probe = self.engine(lifted=True)
        labels = probe.fields(probe.initial_state())["f"]
        for lifted in (False, True):
            engine = self.engine(lifted=lifted, labels=labels)
            state = engine.initial_state()
            velocity = engine.rhs(state)
            for value in velocity.tensors():
                self.close(value, torch.zeros_like(value), atol=0, rtol=0)
            self.close(engine.defect_frobenius(state), torch.zeros((), dtype=torch.float64), atol=0, rtol=0)
            duplicate = linear_combination((.25, .75), (state, state))
            for actual, reference in zip(duplicate.tensors(), state.tensors()):
                self.close(actual, reference)
                self.assertNotEqual(actual.data_ptr(), reference.data_ptr())
            invalid = state.clone()
            invalid.C[0] = 0
            with self.assertRaisesRegex(ValueError, "positive C"):
                engine.rhs(invalid)


if __name__ == "__main__":
    unittest.main(verbosity=2)
