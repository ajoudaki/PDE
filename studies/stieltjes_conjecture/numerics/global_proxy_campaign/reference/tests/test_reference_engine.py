#!/usr/bin/env python3
"""Small CPU validation tests; none are scientific trajectory evidence."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import torch


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import canonical_model as model  # noqa: E402
import reference_engine as engine  # noqa: E402


class AnalyticFormulaTests(unittest.TestCase):
    def setUp(self) -> None:
        torch.set_default_dtype(torch.float64)
        self.device = torch.device("cpu")

    def test_analytic_gradient_and_kernel_match_autograd(self) -> None:
        state, _ = model.generate_antithetic_state(
            3,
            2,
            202608130501,
            device=self.device,
            dtype=torch.float64,
        )
        analytic_rhs = model.feature_rhs(state)
        analytic_obs = model.observables(state)
        a = state.a.clone().requires_grad_(True)
        W = state.W.clone().requires_grad_(True)
        u = state.u.clone().requires_grad_(True)
        autograd_state = model.State(a, W, u)
        outputs = model.output(autograd_state)
        ga, gW, gu = torch.autograd.grad(outputs.sum(), (a, W, u))
        width = state.width
        torch.testing.assert_close(analytic_rhs.a, width * ga, rtol=1e-12, atol=1e-12)
        torch.testing.assert_close(analytic_rhs.W, width * gW, rtol=1e-12, atol=1e-12)
        torch.testing.assert_close(analytic_rhs.u, width * gu, rtol=1e-12, atol=1e-12)
        autograd_kernel = width * (
            ga.square().sum(dim=1)
            + gW.square().sum(dim=(1, 2))
            + gu.square().sum(dim=1)
        )
        torch.testing.assert_close(
            analytic_obs.kernel, autograd_kernel, rtol=1e-12, atol=1e-12
        )
        torch.testing.assert_close(
            analytic_obs.kernel,
            analytic_obs.kernel_a + analytic_obs.kernel_W + analytic_obs.kernel_u,
            rtol=1e-14,
            atol=1e-14,
        )

    def test_vector_field_chain_rules(self) -> None:
        state, _ = model.generate_antithetic_state(
            4,
            2,
            202608130502,
            device=self.device,
            dtype=torch.float64,
            microcanonical_readout=True,
        )
        output_rhs, obs = model.scaled_rhs(state, "output_clock")
        physical_rhs, _ = model.scaled_rhs(state, "physical", target=1.0)

        def directional(tangent: model.State) -> torch.Tensor:
            eps = 1.0e-6
            plus = model.output(model.add_scaled(state, tangent, eps))
            minus = model.output(model.add_scaled(state, tangent, -eps))
            return (plus - minus) / (2.0 * eps)

        torch.testing.assert_close(
            directional(output_rhs),
            torch.ones_like(obs.output),
            rtol=2e-8,
            atol=2e-8,
        )
        torch.testing.assert_close(
            directional(physical_rhs),
            2.0 * (1.0 - obs.output) * obs.kernel,
            rtol=2e-8,
            atol=2e-8,
        )

    def test_antithetic_and_microcanonical_initialization(self) -> None:
        ordinary, ordinary_init = model.generate_antithetic_state(
            7,
            3,
            202608130503,
            device=self.device,
            dtype=torch.float64,
        )
        initial = ordinary_init["initial_output"].reshape(3, 2)
        torch.testing.assert_close(initial[:, 0], -initial[:, 1], rtol=0.0, atol=0.0)
        micro, micro_init = model.generate_antithetic_state(
            7,
            3,
            202608130503,
            device=self.device,
            dtype=torch.float64,
            microcanonical_readout=True,
        )
        self.assertLess(float(torch.max(torch.abs(model.output(micro))).item()), 5e-15)
        self.assertTrue(
            bool(torch.all(micro_init["projection_relative_norm"] >= 0.0).item())
        )


class SolverTests(unittest.TestCase):
    def test_output_clock_identity_and_step_convergence(self) -> None:
        caps = engine.PointCaps(
            wall_seconds=30.0,
            max_steps=100,
            host_rss_gib=4.0,
            gpu_memory_gib=1.0,
            state_ceiling=1e4,
            kernel_ceiling=1e10,
            kernel_floor=1e-14,
            diagnostic_stride=1,
        )

        def point(step: float) -> dict:
            return {
                "mode": "output_clock",
                "width": 4,
                "antithetic_pairs": 2,
                "pair_batch_size": 2,
                "seed_base": 202608130504,
                "target": 1.0,
                "integrator": "rk4",
                "microcanonical_readout": True,
                "step": step,
                "max_output": 0.02,
                "output_nodes": [0.0, 0.01, 0.02],
                "output_defect_tolerance": 1e-8,
            }

        coarse, coarse_diag = engine.run_point(
            point(0.005), device=torch.device("cpu"), dtype=torch.float64, caps=caps
        )
        fine, fine_diag = engine.run_point(
            point(0.0025), device=torch.device("cpu"), dtype=torch.float64, caps=caps
        )
        self.assertLess(coarse_diag["maximum_absolute_output_clock_defect"], 1e-8)
        self.assertLess(fine_diag["maximum_absolute_output_clock_defect"], 1e-9)
        self.assertLess(
            float(np.max(np.abs(coarse["mean_kernel"] - fine["mean_kernel"]))),
            1e-5,
        )

    def test_physical_effective_kernel_definition(self) -> None:
        caps = engine.PointCaps(
            wall_seconds=30.0,
            max_steps=20,
            host_rss_gib=4.0,
            gpu_memory_gib=1.0,
            state_ceiling=1e4,
            kernel_ceiling=1e10,
            kernel_floor=1e-14,
            diagnostic_stride=1,
        )
        point = {
            "mode": "physical",
            "width": 4,
            "antithetic_pairs": 4,
            "pair_batch_size": 4,
            "seed_base": 202608130505,
            "target": 1.0,
            "integrator": "rk4",
            "microcanonical_readout": False,
            "step": 0.0001,
            "max_time": 0.0004,
            "output_nodes": [0.0, 0.005, 0.01],
            "monotonic_tolerance": 1e-10,
        }
        arrays, diagnostics = engine.run_point(
            point, device=torch.device("cpu"), dtype=torch.float64, caps=caps
        )
        reconstructed = arrays["node_raw_weighted_kernel"].mean(axis=1) / (
            1.0 - arrays["output_nodes"]
        )
        np.testing.assert_allclose(arrays["effective_kernel"], reconstructed)
        self.assertEqual(diagnostics["trajectory_count"], 8)


class ProductionLockTests(unittest.TestCase):
    def test_unfrozen_production_config_is_rejected_before_output(self) -> None:
        production = {
            "schema_version": 1,
            "purpose": "scientific_production",
            "run_id": "must_not_run",
            "dtype": "float64",
            "global_caps": {},
            "points": [],
        }
        config = HERE / "configs" / "_temporary_unfrozen_production_test.json"
        try:
            config.write_text(json.dumps(production))
            completed = subprocess.run(
                [sys.executable, str(HERE / "run_reference.py"), str(config)],
                cwd=HERE,
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertTrue(
                "scientific production is locked" in completed.stderr
                or "scientific production lock mismatch" in completed.stderr
            )
            self.assertFalse((HERE / "runs" / "must_not_run").exists())
        finally:
            config.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
