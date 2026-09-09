#!/usr/bin/env python3
"""Small CPU validation tests; none are scientific trajectory evidence."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import time
import unittest
from pathlib import Path

import numpy as np
import torch


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import canonical_model as model  # noqa: E402
import reference_engine as engine  # noqa: E402
import run_reference as runner  # noqa: E402


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

    def test_failure_retains_completed_step_and_resource_telemetry(self) -> None:
        caps = engine.PointCaps(
            wall_seconds=30.0,
            max_steps=2,
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
            "antithetic_pairs": 2,
            "pair_batch_size": 2,
            "seed_base": 202608130506,
            "target": 1.0,
            "integrator": "rk4",
            "microcanonical_readout": False,
            "step": 0.0001,
            "max_time": 0.0001,
            "output_nodes": [0.0, 0.99],
            "monotonic_tolerance": 1e-10,
        }
        with self.assertRaises(engine.NumericalInvalid) as caught:
            engine.run_point(
                point, device=torch.device("cpu"), dtype=torch.float64, caps=caps
            )
        diagnostics = caught.exception.point_diagnostics
        self.assertEqual(diagnostics["integrator_steps_all_batches"], 1)
        self.assertGreater(diagnostics["elapsed_seconds"], 0.0)
        self.assertGreater(diagnostics["max_host_rss_gib"], 0.0)
        self.assertEqual(diagnostics["max_gpu_allocated_gib"], 0.0)

    def test_absolute_global_deadline_is_enforced_by_point_guard(self) -> None:
        caps = engine.PointCaps(
            wall_seconds=30.0,
            max_steps=2,
            host_rss_gib=4.0,
            gpu_memory_gib=1.0,
            state_ceiling=1e4,
            kernel_ceiling=1e10,
            kernel_floor=1e-14,
            diagnostic_stride=1,
        )
        guard = engine.BudgetGuard(
            caps,
            torch.device("cpu"),
            absolute_wall_deadline=time.monotonic() - 1.0,
        )
        with self.assertRaisesRegex(engine.BudgetStop, "global wall cap"):
            guard.check()

    def test_antithetic_initial_cancellation_is_fail_closed(self) -> None:
        malformed = torch.tensor([1.0, -0.9], dtype=torch.float64)
        with self.assertRaisesRegex(engine.NumericalInvalid, "cancellation defect"):
            engine._antithetic_cancellation_certificate(malformed, 1, 1e-12)

    def test_physical_mean_loss_increase_is_fail_closed(self) -> None:
        shape = (2, 2)
        batch = {
            "coordinate": np.array([0.0, 0.0001]),
            "output": np.array([[0.0, 0.0], [0.1, 0.1]]),
            "kernel": np.ones(shape),
            "weighted_kernel": np.ones(shape),
            "loss": np.array([[1.0, 1.0], [1.1, 1.1]]),
            "q1": np.ones(shape),
            "q2": np.ones(shape),
            "kernel_a": np.ones(shape),
            "kernel_W": np.ones(shape),
            "kernel_u": np.ones(shape),
        }
        with self.assertRaisesRegex(engine.NumericalInvalid, "mean physical loss"):
            engine.aggregate_physical(
                [batch],
                np.array([0.0, 0.1]),
                target=1.0,
                monotonic_tolerance=1e-12,
                loss_nonincrease_tolerance=1e-12,
            )


class ProductionLockTests(unittest.TestCase):
    def test_validation_gate_returns_non_scientific_authorization_record(self) -> None:
        config_path = HERE / "configs" / "validation_cpu_v3.json"
        config = json.loads(config_path.read_text())
        record = runner._production_gate(
            config, config_path, runner.source_hashes()
        )
        self.assertEqual(record, {"required": False})

    def test_lock_sources_include_wrapper_and_successor_protocol_is_determined(self) -> None:
        self.assertIn(HERE / "run_capped_reference.sh", runner.SOURCE_FILES)
        protocol = runner._protocol_path_for_config(
            HERE / "configs" / "FROZEN_SUCCESSOR_01.json"
        )
        self.assertEqual(protocol.name, "SUCCESSOR_01_PROTOCOL.md")

    def test_successor02_lock_binds_frozen_analysis_name_and_hash(self) -> None:
        config_path = HERE / "configs" / "FROZEN_SUCCESSOR_02.json"
        config = json.loads(config_path.read_text())
        fields = runner._analysis_lock_fields(config, config_path)
        analysis_path = HERE / "configs" / "FROZEN_SUCCESSOR_02_ANALYSIS.json"
        self.assertEqual(
            fields,
            {
                "analysis_config_name": analysis_path.name,
                "analysis_config_sha256": runner.sha256(analysis_path),
            },
        )
        missing = dict(config)
        missing["analysis"] = dict(config["analysis"])
        missing["analysis"].pop("analysis_config")
        with self.assertRaisesRegex(ValueError, "requires a frozen analysis"):
            runner._analysis_lock_fields(missing, config_path)

    def test_remaining_global_wall_intersects_point_cap(self) -> None:
        caps = engine.PointCaps(
            wall_seconds=30.0,
            max_steps=2,
            host_rss_gib=4.0,
            gpu_memory_gib=1.0,
            state_ceiling=1e4,
            kernel_ceiling=1e10,
            kernel_floor=1e-14,
            diagnostic_stride=1,
        )
        effective = runner._caps_with_remaining_wall(caps, 0.25)
        self.assertEqual(effective.wall_seconds, 0.25)
        with self.assertRaisesRegex(engine.BudgetStop, "global wall cap"):
            runner._caps_with_remaining_wall(caps, 0.0)

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

    def test_runner_failure_certificate_is_complete_and_not_admissible(self) -> None:
        run_id = "temporary_failure_telemetry_test"
        run_directory = HERE / "runs" / run_id
        config = HERE / "configs" / "_temporary_failure_telemetry_test.json"
        failure = {
            "schema_version": 1,
            "purpose": "validation_only",
            "run_id": run_id,
            "dtype": "float64",
            "global_caps": {
                "device": "cpu",
                "total_wall_seconds": 30,
                "max_points": 2,
                "max_width": 4,
                "max_antithetic_pairs": 2,
            },
            "points": [
                {
                    "id": "completed_validation_point",
                    "mode": "physical",
                    "width": 4,
                    "antithetic_pairs": 2,
                    "pair_batch_size": 2,
                    "seed_base": 202608130508,
                    "target": 1.0,
                    "integrator": "rk4",
                    "microcanonical_readout": False,
                    "step": 0.0001,
                    "max_time": 0.0001,
                    "output_nodes": [0.0],
                    "monotonic_tolerance": 1e-10,
                    "caps": {
                        "wall_seconds": 20,
                        "max_steps_all_batches": 2,
                        "host_rss_gib": 4.0,
                        "gpu_memory_gib": 1.0,
                        "max_raw_curve_mib": 1.0,
                        "state_ceiling": 10000.0,
                        "kernel_ceiling": 10000000000.0,
                        "kernel_floor": 1e-14,
                        "diagnostic_stride": 1,
                    },
                },
                {
                    "id": "declared_short_horizon",
                    "mode": "physical",
                    "width": 4,
                    "antithetic_pairs": 2,
                    "pair_batch_size": 2,
                    "seed_base": 202608130507,
                    "target": 1.0,
                    "integrator": "rk4",
                    "microcanonical_readout": False,
                    "step": 0.0001,
                    "max_time": 0.0001,
                    "output_nodes": [0.0, 0.99],
                    "monotonic_tolerance": 1e-10,
                    "caps": {
                        "wall_seconds": 20,
                        "max_steps_all_batches": 2,
                        "host_rss_gib": 4.0,
                        "gpu_memory_gib": 1.0,
                        "max_raw_curve_mib": 1.0,
                        "state_ceiling": 10000.0,
                        "kernel_ceiling": 10000000000.0,
                        "kernel_floor": 1e-14,
                        "diagnostic_stride": 1,
                    },
                }
            ],
        }
        try:
            shutil.rmtree(run_directory, ignore_errors=True)
            config.write_text(json.dumps(failure))
            completed = subprocess.run(
                [sys.executable, str(HERE / "run_reference.py"), str(config)],
                cwd=HERE,
                text=True,
                capture_output=True,
                timeout=30,
                check=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stderr)
            summary = json.loads((run_directory / "summary.json").read_text())
            self.assertEqual(summary["run_purpose"], "validation_only")
            self.assertFalse(summary["accepted_as_scientific_evidence"])
            self.assertFalse(summary["scientific_evidence_admissible"])
            self.assertIsNotNone(summary["command"]["python_executable"])
            self.assertIsNotNone(summary["started_utc"])
            self.assertIsNotNone(summary["ended_utc"])
            completed_record = summary["points"][0]
            self.assertEqual(completed_record["status"], "complete_validation_only")
            self.assertEqual(completed_record["seed_base"], 202608130508)
            self.assertFalse(completed_record["accepted_as_scientific_evidence"])
            self.assertIsNotNone(completed_record["command"]["argv"])
            self.assertIsNotNone(completed_record["started_utc"])
            self.assertIsNotNone(completed_record["ended_utc"])
            self.assertGreater(completed_record["elapsed_seconds"], 0.0)
            self.assertEqual(
                completed_record["diagnostics"]["integrator_steps_all_batches"], 1
            )
            record = summary["points"][1]
            self.assertEqual(record["seed_base"], 202608130507)
            self.assertEqual(record["run_purpose"], "validation_only")
            self.assertFalse(record["accepted_as_scientific_evidence"])
            self.assertIsNotNone(record["started_utc"])
            self.assertIsNotNone(record["ended_utc"])
            self.assertGreater(record["elapsed_seconds"], 0.0)
            diagnostics = record["diagnostics"]
            self.assertEqual(diagnostics["integrator_steps_all_batches"], 1)
            self.assertGreater(diagnostics["max_host_rss_gib"], 0.0)
            self.assertEqual(diagnostics["max_gpu_allocated_gib"], 0.0)
        finally:
            config.unlink(missing_ok=True)
            shutil.rmtree(run_directory, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
