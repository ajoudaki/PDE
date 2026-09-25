"""Bounded CPU algebra/derivative checks for the Legendre variant."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
import torch

from orthogonal_moment_engine import OrthogonalMomentEngine

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.finite_network import initialize, flow_velocity


class OrthogonalMomentEngineTests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        rng = np.random.default_rng(29)
        self.d, self.n, self.M, self.P = 3, 8, 4, 4
        self.inputs = rng.normal(size=(self.M, self.d))/np.sqrt(self.d)
        self.labels = rng.normal(size=self.M)

    def engine(self, lifted=False, labels=None):
        return OrthogonalMomentEngine(self.d, self.n, self.P, self.inputs,
                                      self.labels if labels is None else labels, lifted=lifted)

    def close(self, actual, expected, *, atol=3e-12, rtol=3e-11):
        torch.testing.assert_close(torch.as_tensor(actual), torch.as_tensor(expected), atol=atol, rtol=rtol)

    def noninitial(self, engine):
        state = engine.initial_state()
        generator = torch.Generator().manual_seed(83)
        state.s.fill_(.8)
        state.C.fill_(1.8)
        state.A = .1*torch.randn(state.A.shape, generator=generator, dtype=torch.float64)
        state.B += .15*torch.randn(state.B.shape, generator=generator, dtype=torch.float64)
        state.w += .03*torch.randn(state.w.shape, generator=generator, dtype=torch.float64)
        state.c += .04*torch.randn(state.c.shape, generator=generator, dtype=torch.float64)
        if engine.lifted:
            state.h1 = torch.tanh(state.w @ engine.inputs.T)
            state.h2 = torch.tanh(engine.apply_hidden(state, state.h1))
            state.rho = torch.sqrt((state.c @ state.h2/engine.n-engine.labels).square().mean())
        return state

    def test_virtual_prefix_initialization_and_exact_initial_tangent(self):
        engine = self.engine()
        state = engine.initial_state()
        self.assertEqual(engine.eta, 1)
        self.close(state.A, torch.zeros_like(state.A), atol=0, rtol=0)
        self.close(state.B[0], engine.h10, atol=0, rtol=0)
        self.close(state.B[1:], torch.zeros_like(state.B[1:]), atol=0, rtol=0)
        self.close(state.C, torch.ones_like(state.C), atol=0, rtol=0)
        velocity = engine.rhs(state)
        fields = engine.fields(state)
        self.close(velocity.A, (fields["delta2"]*fields["r"])[None].expand_as(state.A))
        self.close(velocity.B[0], fields["rho"]*engine.h10)
        self.close(velocity.B[1:], torch.zeros_like(velocity.B[1:]))
        reference = flow_velocity(initialize(self.n, 2, self.d, seed=20260920),
                                  self.inputs.T*np.sqrt(self.d), self.labels)
        self.close(velocity.w, reference.weights[0])
        self.close(velocity.c, reference.readout)
        left, right = engine.derivative_factors(state, velocity)
        self.close(left @ right.T, reference.weights[1])
        self.close(engine.defect_frobenius(state), torch.zeros((), dtype=torch.float64))
        u_projection, h_projection = engine.endpoint_projections(state)
        self.close(u_projection, torch.zeros_like(u_projection), atol=0, rtol=0)
        self.close(h_projection, engine.h10, atol=0, rtol=0)

    def test_moving_basis_transport_against_integrals(self):
        engine = self.engine()
        nodes, weights = leggauss(40)
        basis = legvander(nodes, self.P-1)
        scale = np.arange(1, self.n*self.M+1).reshape(self.n, self.M)/30

        def history(t):
            return (1+.3*t[:, None, None]+.2*t[:, None, None]**3)*scale

        def moments(length):
            t = (nodes+1)*length/2
            return np.einsum("q,qk,qim->kim", weights*length/2, basis, history(t))

        length, rho = 2.3, .7
        moment = torch.tensor(moments(length), dtype=torch.float64)
        source = torch.tensor(rho*history(np.array([length]))[0], dtype=torch.float64)
        actual = engine.transport_moments(moment, source, rho, length)
        eps = 2e-6
        expected = (moments(length+rho*eps)-moments(length-rho*eps))/(2*eps)
        self.close(actual, expected, atol=3e-9, rtol=3e-9)

    def test_weight_derivative_defect_factors_and_norm(self):
        engine = self.engine()
        state = self.noninitial(engine)
        velocity = engine.rhs(state)
        left, right = engine.derivative_factors(state, velocity)
        derivative = left @ right.T
        fields = engine.fields(state)
        full_velocity = (-2/(self.M*self.n))*(fields["delta2"]*fields["r"]) @ fields["h1"].T
        el, er = engine.defect_factors(state)
        self.assertEqual(el.shape, (self.n, self.M))
        self.close(derivative-full_velocity, el @ er.T)
        self.close(engine.defect_frobenius(state, block_size=2), torch.linalg.norm(derivative-full_velocity))
        eps = 2e-6
        finite_difference = (engine.reconstruct_delta_for_diagnostics(state.add_scaled(velocity, eps))
                             -engine.reconstruct_delta_for_diagnostics(state.add_scaled(velocity, -eps)))/(2*eps)
        self.close(finite_difference, derivative, atol=2e-11, rtol=2e-8)

    def test_lifted_tangency_and_rational_rhs(self):
        engine = self.engine(lifted=True)
        state = self.noninitial(engine)
        velocity = engine.rhs(state)

        def recompute(w, c, A, B, C, s):
            delta = (-2/(self.M*self.n*(s+1)))*torch.einsum("pim,pjm,p->ij", A, B, engine.legendre_weights)
            h1 = torch.tanh(w @ engine.inputs.T)
            h2 = torch.tanh((engine.W0+delta) @ h1)
            rho = torch.sqrt((c @ h2/engine.n-engine.labels).square().mean())
            return h1, h2, rho

        _, expected = torch.autograd.functional.jvp(recompute, state.tensors()[:6], velocity.tensors()[:6])
        for actual, reference in zip((velocity.h1, velocity.h2, velocity.rho), expected):
            self.close(actual, reference)
        with patch("torch.tanh", side_effect=AssertionError("tanh in lifted RHS")), \
             patch("torch.sqrt", side_effect=AssertionError("sqrt in lifted RHS")), \
             patch.object(engine, "reconstruct_delta_for_diagnostics", side_effect=AssertionError("dense reconstruction")):
            rational = engine.rhs(state)
        for actual, expected in zip(rational.tensors(), velocity.tensors()):
            self.close(actual, expected, atol=0, rtol=0)
        self.close(velocity.C, velocity.s.expand_as(state.C), atol=0, rtol=0)
        self.close(engine.moment_diagnostics(state)["C_minus_L"], torch.zeros_like(state.C), atol=0, rtol=0)

    def test_zero_residual_stops(self):
        probe = self.engine()
        labels = probe.fields(probe.initial_state())["f"]
        for lifted in (False, True):
            engine = self.engine(lifted=lifted, labels=labels)
            state = engine.initial_state()
            for value in engine.rhs(state).tensors():
                self.close(value, torch.zeros_like(value), atol=0, rtol=0)
            self.close(engine.defect_frobenius(state), torch.zeros((), dtype=torch.float64), atol=0, rtol=0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
