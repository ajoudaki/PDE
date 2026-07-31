from __future__ import annotations

import unittest

import numpy as np

from operator_hermite_pde import (
    OperatorPDEConfig,
    OperatorState,
    initialize,
    rk4_step,
    solve_depth_bvp,
    vector_field,
)


class OperatorHermitePDETests(unittest.TestCase):
    def setUp(self) -> None:
        self.cfg = OperatorPDEConfig(
            X=np.eye(2),
            y=np.asarray([0.8, -0.55]),
            depth=4,
            basis_degree=1,
            base_rule_order=3,
            row_rule_order=2,
        )
        self.ws = initialize(self.cfg)

    @staticmethod
    def perturbed(
        state: OperatorState, block: str, index: tuple[int, ...], eps: float
    ) -> OperatorState:
        out = state.copy()
        getattr(out, block)[index] += eps
        return out

    def loss(self, state: OperatorState) -> float:
        return float(vector_field(state, self.cfg, self.ws)[1]["loss"])

    def test_weighted_parameter_gradients(self) -> None:
        state = self.ws.state
        vf, _ = vector_field(state, self.cfg, self.ws)
        eps = 2.0e-6
        checks = [
            ("b", (2, 1), self.ws.base_weights[2], 1.0),
            ("a", (3,), self.ws.base_weights[3], 1.0),
            (
                "c",
                (1, 2, 3, 1),
                self.ws.base_weights[2] * self.ws.row_weights[3],
                1.0 / self.cfg.depth,
            ),
        ]
        for block, index, weight, depth_metric in checks:
            plus = self.loss(self.perturbed(state, block, index, eps))
            minus = self.loss(self.perturbed(state, block, index, -eps))
            fd = (plus - minus) / (2.0 * eps)
            predicted = (
                -weight * depth_metric * getattr(vf, block)[index]
            )
            self.assertAlmostEqual(fd, predicted, delta=2.0e-8)

    def test_shared_operator_adjoint_identity(self) -> None:
        state = self.ws.state
        h, p, H, z, beta = solve_depth_bvp(
            state, self.cfg, self.ws
        )
        del h, H
        rng = np.random.default_rng(91)
        r = 1
        dh = rng.normal(size=self.ws.base.shape[0])
        dh0 = dh.copy()
        forcing = rng.normal(
            size=(
                self.cfg.depth,
                self.ws.base.shape[0],
                self.ws.row_weights.size,
            )
        )
        for ell in range(self.cfg.depth):
            dH = np.einsum(
                "x,xj,x->j",
                self.ws.base_weights,
                self.ws.phi,
                dh,
                optimize=True,
            )
            dz = np.einsum(
                "xej,j->xe", state.c[ell], dH, optimize=True
            )
            dz += forcing[ell]
            D = 1.0 - np.tanh(z[ell, :, :, r]) ** 2
            dh = dh + (self.cfg.gamma / self.cfg.depth) * np.einsum(
                "e,xe->x",
                self.ws.row_weights,
                D * dz,
                optimize=True,
            )
        lhs = np.einsum(
            "x,x,x->",
            self.ws.base_weights,
            state.a,
            dh,
            optimize=True,
        )
        rhs = np.einsum(
            "x,x,x->",
            self.ws.base_weights,
            p[0, :, r],
            dh0,
            optimize=True,
        )
        rhs += (self.cfg.gamma / self.cfg.depth) * np.einsum(
            "x,e,lxe,lxe->",
            self.ws.base_weights,
            self.ws.row_weights,
            beta[:, :, :, r],
            forcing,
            optimize=True,
        )
        self.assertAlmostEqual(float(lhs), float(rhs), delta=2.0e-12)

    def test_tangent_kernel_output_identity(self) -> None:
        state = self.ws.state
        vf, obs = vector_field(state, self.cfg, self.ws)
        eps = 2.0e-6
        plus = OperatorState(
            state.b + eps * vf.b,
            state.a + eps * vf.a,
            state.c + eps * vf.c,
        )
        minus = OperatorState(
            state.b - eps * vf.b,
            state.a - eps * vf.a,
            state.c - eps * vf.c,
        )
        f_plus = np.asarray(vector_field(plus, self.cfg, self.ws)[1]["f"])
        f_minus = np.asarray(vector_field(minus, self.cfg, self.ws)[1]["f"])
        fd = (f_plus - f_minus) / (2.0 * eps)
        predicted = np.asarray(obs["predicted_f_dot"])
        np.testing.assert_allclose(fd, predicted, rtol=1.0e-8, atol=2.0e-9)
        self.assertGreaterEqual(
            float(np.linalg.eigvalsh(np.asarray(obs["theta"]))[0]),
            -1.0e-12,
        )

    def test_restart_semigroup_numerically(self) -> None:
        dt = 0.01
        direct = self.ws.state.copy()
        for _ in range(10):
            direct = rk4_step(direct, dt, self.cfg, self.ws)
        restarted = self.ws.state.copy()
        for _ in range(4):
            restarted = rk4_step(restarted, dt, self.cfg, self.ws)
        checkpoint = restarted.copy()
        for _ in range(6):
            checkpoint = rk4_step(checkpoint, dt, self.cfg, self.ws)
        np.testing.assert_array_equal(direct.b, checkpoint.b)
        np.testing.assert_array_equal(direct.a, checkpoint.a)
        np.testing.assert_array_equal(direct.c, checkpoint.c)


if __name__ == "__main__":
    unittest.main()
