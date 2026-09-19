"""Deterministic supplied-state checks; no training experiment or limit claim."""
import unittest

import numpy as np

from pde.finite_network import Activation, Parameters, flow_velocity, forward, gd_step


def activations():
    return (
        Activation("softplus", lambda z: np.logaddexp(0., z),
                   lambda z: 1. / (1. + np.exp(-z))),
        Activation("oscillating_linear", lambda z: z + .4 * np.sin(z),
                   lambda z: 1. + .4 * np.cos(z)),
        Activation("nonodd_bounded", lambda z: .3 + np.sin(z), np.cos),
        # C1,1 with flat gate and nondifferentiable second derivative.
        Activation("quadratic_smooth_relu",
                   lambda z: np.where(z <= 0, 0, np.where(z < 1, z*z/2, z-.5)),
                   lambda z: np.clip(z, 0, 1)),
    )


class Identities(unittest.TestCase):
    def setUp(self):
        self.n = 7
        rng = np.random.default_rng(20260919)
        self.state = Parameters((rng.normal(size=(self.n, 2)),
                                 rng.normal(size=(self.n, self.n))/np.sqrt(self.n)),
                                rng.normal(size=self.n)/self.n)
        self.x = np.sqrt(2.) * np.eye(2)
        self.y = np.array([1., -1.])

    @staticmethod
    def swap(state):
        return Parameters((state.weights[0][:, ::-1], state.weights[1]), -state.readout)

    def assert_state_close(self, a, b):
        for x, y in zip((*a.weights, a.readout), (*b.weights, b.readout)):
            np.testing.assert_allclose(x, y, atol=3e-13, rtol=3e-13)

    def test_loss_flow_and_raw_step_symmetry_without_oddness(self):
        for phi in activations():
            with self.subTest(activation=phi.name):
                transformed = self.swap(self.state)
                f = forward(self.state, self.x, phi).output
                fq = forward(transformed, self.x, phi).output
                np.testing.assert_allclose(fq, -f[::-1], atol=3e-13, rtol=3e-13)
                self.assertAlmostEqual(np.mean((f-self.y)**2),
                                       np.mean((fq-self.y)**2), places=12)
                self.assert_state_close(
                    flow_velocity(transformed, self.x, self.y, phi),
                    self.swap(flow_velocity(self.state, self.x, self.y, phi)))
                self.assert_state_close(
                    gd_step(transformed, self.x, self.y, .003, phi),
                    self.swap(gd_step(self.state, self.x, self.y, .003, phi)))

    def test_feature_ascent_chain_rule_and_raw_metric(self):
        # These formulas are derived directly from b=<c,(H1-H2)/2>.
        # Finite-difference oracles evaluate only the network forward map.
        for phi in activations():
            with self.subTest(activation=phi.name):
                w, a = self.state.weights
                c = self.state.readout
                z1 = w.copy()
                h1 = phi.value(z1)
                z2 = a @ h1
                h2 = phi.value(z2)
                h = (h2[:, 0]-h2[:, 1])/2
                upper = c[:, None] * phi.derivative(z2)
                vw = .5 * phi.derivative(z1) * (a.T @ upper) * self.y
                va = (upper*self.y) @ h1.T / (2*self.n)
                dz2 = va @ h1 + a @ (phi.derivative(z1)*vw)
                dh = (phi.derivative(z2)*dz2) @ self.y/2
                hidden_speed2 = np.sum(vw*vw)/self.n + np.sum(va*va)
                self.assertAlmostEqual(float(c@dh/self.n), hidden_speed2, places=12)
                eps = 1e-6
                def shifted(sign):
                    p = Parameters((w+sign*eps*vw, a+sign*eps*va), c+sign*eps*h)
                    f = forward(p, self.x, phi).output
                    return float(f@self.y/2), phi.value((a+sign*eps*va) @
                                 phi.value(w+sign*eps*vw)) @ self.y/2
                bp, hp = shifted(1)
                bm, hm = shifted(-1)
                np.testing.assert_allclose((hp-hm)/(2*eps), dh, atol=2e-8, rtol=2e-7)
                self.assertAlmostEqual((bp-bm)/(2*eps),
                                       float(h@h/self.n)+hidden_speed2, places=8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
