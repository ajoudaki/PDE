from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dense_mup.analysis import plateau_ladder
from dense_mup.core import (
    ModelSpec,
    ParamState,
    field_vector_field,
    fields_from_params,
    forward_adjoint,
    initialize,
    parameter_vector_field,
    rk4_field_step,
    rk4_param_step,
    snapshot_from_params,
)


def loss(state: ParamState, spec: ModelSpec) -> float:
    fa = forward_adjoint(state, spec)
    e = state.a @ fa.H[-1] / spec.n - spec.y
    return float(0.5 * e @ e)


class AlgebraTests(unittest.TestCase):
    def setUp(self) -> None:
        X = np.asarray(
            [[1.0, 0.03, 0.0], [0.0, 0.99955, 0.02], [0.0, 0.0, 0.9998]]
        )
        self.spec = ModelSpec(
            n=12,
            depth=4,
            X=X,
            y=np.asarray([0.8, -0.55, 0.35]),
            seed=123,
            sigma_w=0.7,
            A=1.05,
            gamma=0.95,
        )
        self.state = initialize(self.spec)

    def _finite_difference(
        self, block: str, index: tuple[int, ...], eps: float = 1e-5
    ) -> float:
        plus = self.state.copy()
        minus = self.state.copy()
        getattr(plus, block)[index] += eps
        getattr(minus, block)[index] -= eps
        return (loss(plus, self.spec) - loss(minus, self.spec)) / (2 * eps)

    def test_muP_vector_field_matches_finite_difference(self) -> None:
        dot = parameter_vector_field(self.state, self.spec)
        checks = [
            ("a", (2,), -dot.a[2] / self.spec.n),
            ("B", (3, 1), -dot.B[3, 1] / self.spec.n),
            (
                "W",
                (2, 4, 5),
                -dot.W[2, 4, 5] / self.spec.depth,
            ),
        ]
        for block, index, analytic in checks:
            numeric = self._finite_difference(block, index)
            self.assertAlmostEqual(numeric, float(analytic), delta=2e-8)

    def test_K_equals_depth_reproduces_exact_training_derivatives(self) -> None:
        exact_snapshot, exact_hdot, exact_pdot = snapshot_from_params(
            self.state, self.spec
        )
        base = fields_from_params(self.state, self.spec)
        projected = field_vector_field(base, self.spec, self.spec.depth)
        h_rel = np.linalg.norm(projected.H - exact_hdot) / np.linalg.norm(
            exact_hdot
        )
        p_rel = np.linalg.norm(projected.P - exact_pdot) / np.linalg.norm(
            exact_pdot
        )
        self.assertLess(h_rel, 2e-14)
        self.assertLess(p_rel, 2e-14)
        self.assertLess(exact_snapshot.kernel_identity_defect, 2e-14)

    def test_zero_residual_freezes_both_systems(self) -> None:
        fa = forward_adjoint(self.state, self.spec)
        fitted_y = self.state.a @ fa.H[-1] / self.spec.n
        fitted = ModelSpec(
            **{**self.spec.__dict__, "y": fitted_y.copy()}
        )
        pdot = parameter_vector_field(self.state, fitted)
        self.assertEqual(float(np.linalg.norm(pdot.B)), 0.0)
        self.assertEqual(float(np.linalg.norm(pdot.W)), 0.0)
        self.assertEqual(float(np.linalg.norm(pdot.a)), 0.0)
        base = fields_from_params(self.state, fitted)
        fdot = field_vector_field(base, fitted, 2)
        self.assertEqual(float(np.linalg.norm(fdot.H)), 0.0)
        self.assertEqual(float(np.linalg.norm(fdot.P)), 0.0)

    def test_integrated_K_equals_depth_is_rk4_floor_control(self) -> None:
        spec = ModelSpec(
            n=10,
            depth=3,
            X=np.eye(3),
            y=np.asarray([0.8, -0.55, 0.35]),
            seed=9,
        )
        exact = initialize(spec)
        field = fields_from_params(exact, spec)
        dt = 0.002
        for _ in range(50):
            exact = rk4_param_step(exact, dt, spec)
            field = rk4_field_step(field, dt, spec, spec.depth)
        exact_field = fields_from_params(exact, spec)
        f_exact = exact.a @ exact_field.H[-1] / spec.n
        f_field = field.a @ field.H[-1] / spec.n
        g_exact = np.einsum(
            "lnr,lnq->lrq", exact_field.H, exact_field.H
        ) / spec.n
        g_field = np.einsum("lnr,lnq->lrq", field.H, field.H) / spec.n
        self.assertLess(float(np.linalg.norm(f_field - f_exact)), 2e-11)
        self.assertLess(
            float(
                np.max(
                    np.linalg.norm(g_field - g_exact, axis=(-2, -1))
                )
            ),
            6e-11,
        )


class PlateauDetectorTests(unittest.TestCase):
    @staticmethod
    def protocol() -> dict:
        return {
            "horizons": [4.0, 8.0, 16.0],
            "tail_fraction": 0.5,
            "absolute_scale": 1e-6,
            "motion_scale": 1e-4,
            "residual_scale": 1e-5,
            "arclength_multiplier": 2.0,
        }

    @staticmethod
    def synthetic(kind: str) -> tuple[dict, dict]:
        t = np.linspace(0.0, 16.0, 401)
        y = np.asarray([0.8, -0.55, 0.35])
        direction = np.asarray([0.5, -0.2, 0.1])
        base = np.stack([np.eye(3), 1.2 * np.eye(3)], axis=0)
        shift = np.stack(
            [
                np.asarray([[0.3, 0.1, 0.0], [0.1, -0.2, 0.0], [0.0, 0.0, 0.1]]),
                np.asarray([[0.5, -0.1, 0.0], [-0.1, 0.2, 0.05], [0.0, 0.05, -0.1]]),
            ],
            axis=0,
        )
        if kind == "decay":
            decay = np.exp(-4.0 * t)
            f = y[None, :] + decay[:, None] * direction
            f_dot = -4.0 * decay[:, None] * direction
            grams = base[None, :] + (1.0 - decay)[:, None, None, None] * shift
            gram_dot = 4.0 * decay[:, None, None, None] * shift
        elif kind == "slow":
            f = y[None, :] + np.exp(-2.0 * t)[:, None] * direction
            f_dot = -2.0 * np.exp(-2.0 * t)[:, None] * direction
            grams = base[None, :] + 0.01 * t[:, None, None, None] * shift
            gram_dot = np.broadcast_to(0.01 * shift, grams.shape)
        elif kind == "oscillation":
            f = y[None, :] + np.exp(-2.0 * t)[:, None] * direction
            f_dot = -2.0 * np.exp(-2.0 * t)[:, None] * direction
            grams = base[None, :] + 1e-3 * np.sin(20 * t)[:, None, None, None] * shift
            gram_dot = 0.02 * np.cos(20 * t)[:, None, None, None] * shift
        elif kind == "reactivation":
            decay = np.exp(-4.0 * t)
            ramp = 0.01 * np.maximum(t - 10.0, 0.0)
            f = y[None, :] + decay[:, None] * direction
            f_dot = -4.0 * decay[:, None] * direction
            grams = (
                base[None, :]
                + (1.0 - decay)[:, None, None, None] * shift
                + ramp[:, None, None, None] * shift
            )
            gram_dot = (
                4.0 * decay[:, None, None, None] * shift
                + (t > 10.0)[:, None, None, None] * 0.01 * shift
            )
        else:
            raise ValueError(kind)
        arrays = {
            "times": t,
            "f": f[None, :],
            "grams": grams[None, :],
            "residual_norm": np.linalg.norm(f - y, axis=-1)[None, :],
            "output_speed": np.linalg.norm(f_dot, axis=-1)[None, :],
            "gram_speed": np.max(
                np.linalg.norm(gram_dot, axis=(-2, -1)), axis=1
            )[None, :],
        }
        return {"y": y.tolist()}, arrays

    def test_decay_passes_and_validates(self) -> None:
        metadata, arrays = self.synthetic("decay")
        result = plateau_ladder(metadata, arrays, 0, self.protocol())
        self.assertIsNotNone(result["candidate_horizon"])
        self.assertEqual(result["validated_through"], 16.0)

    def test_slow_drift_is_rejected(self) -> None:
        metadata, arrays = self.synthetic("slow")
        result = plateau_ladder(metadata, arrays, 0, self.protocol())
        self.assertIsNone(result["candidate_horizon"])

    def test_oscillation_is_rejected(self) -> None:
        metadata, arrays = self.synthetic("oscillation")
        result = plateau_ladder(metadata, arrays, 0, self.protocol())
        self.assertIsNone(result["candidate_horizon"])

    def test_late_reactivation_cancels_earlier_pass(self) -> None:
        metadata, arrays = self.synthetic("reactivation")
        result = plateau_ladder(metadata, arrays, 0, self.protocol())
        self.assertEqual(result["first_passing_horizon"], 8.0)
        self.assertIsNone(result["candidate_horizon"])
        self.assertIsNone(result["validated_through"])


if __name__ == "__main__":
    unittest.main()
