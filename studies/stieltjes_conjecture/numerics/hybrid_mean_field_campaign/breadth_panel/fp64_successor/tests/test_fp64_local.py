from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np
import torch


HERE = Path(__file__).resolve().parent
SUCCESSOR = HERE.parent
REPO = SUCCESSOR.parents[5]
SCRIPT = SUCCESSOR / "run_local_qualification.py"
SPEC = importlib.util.spec_from_file_location("fp64_local_qualification", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
ADJUDICATOR_SCRIPT = SUCCESSOR / "adjudicate_local_qualification.py"
ADJUDICATOR_SPEC = importlib.util.spec_from_file_location(
    "fp64_local_adjudicator", ADJUDICATOR_SCRIPT
)
assert ADJUDICATOR_SPEC is not None and ADJUDICATOR_SPEC.loader is not None
ADJUDICATOR = importlib.util.module_from_spec(ADJUDICATOR_SPEC)
sys.modules[ADJUDICATOR_SPEC.name] = ADJUDICATOR
ADJUDICATOR_SPEC.loader.exec_module(ADJUDICATOR)
WATCHDOG_SCRIPT = SUCCESSOR / "watchdog_launcher.py"
WATCHDOG_SPEC = importlib.util.spec_from_file_location(
    "fp64_watchdog_launcher", WATCHDOG_SCRIPT
)
assert WATCHDOG_SPEC is not None and WATCHDOG_SPEC.loader is not None
WATCHDOG = importlib.util.module_from_spec(WATCHDOG_SPEC)
sys.modules[WATCHDOG_SPEC.name] = WATCHDOG
WATCHDOG_SPEC.loader.exec_module(WATCHDOG)


class FP64LocalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.frozen = json.loads(
            (SUCCESSOR / "FROZEN_LOCAL_QUALIFICATION.json").read_text(encoding="utf-8")
        )

    def test_symmetric_relative(self) -> None:
        actual = MODULE.symmetric_relative(
            np.asarray([2.0, 0.0]), np.asarray([1.0, 0.0])
        )
        np.testing.assert_allclose(actual, np.asarray([2.0 / 3.0, 0.0]))

    def test_primitive_first_clock(self) -> None:
        output = np.asarray([[0.0, 0.0], [0.5, 0.5], [0.95, 0.95]])
        weighted = np.asarray([[1.0, 1.0], [1.0, 3.0], [2.0, 4.0]])
        arrays = {"time": np.asarray([0.0, 1.0, 2.0]), "raw_output": output}
        for name in (
            "raw_kernel",
            "raw_kernel_a",
            "raw_kernel_W",
            "raw_kernel_u",
            "raw_loss",
            "raw_q1",
            "raw_q2",
        ):
            arrays[name] = np.ones_like(output)
        arrays["raw_weighted_kernel"] = weighted
        nodes = np.asarray([0.5, 0.95])
        result = MODULE.primitive_clock(arrays, nodes)
        np.testing.assert_allclose(result["weighted_kernel_numerator"], [2.0, 3.0])
        np.testing.assert_allclose(result["Keff"], [4.0, 60.0])

    def test_hash_checked_transform_and_cpu_smoke(self) -> None:
        runner = MODULE.load_fp64_runner(REPO, self.frozen)
        point = {
            "key": "unit_fp64",
            "purpose": "unit_test",
            "configuration": "centered_c1",
            "width": 8,
            "step": 1e-5,
            "max_time": 2e-5,
            "lineage_start": 0,
            "lineage_stop": 1,
            "prefix_sizes": [8],
            "rng_row_block": 4,
            "w_monitor_size": 8,
            "w_monitor_extent": 8,
            "w_monitor_seed": 123,
            "diagnostic_stride": 1,
            "wall_sync_stride": 1,
            "caps": {
                "wall_seconds": 10,
                "max_steps_all_lineages": 2,
                "gpu_memory_gib": 1,
                "host_rss_gib": 2,
                "kernel_ceiling": 1e6,
                "state_ceiling": 1e4,
            },
        }
        arrays, outer = runner.run_point(point, seed=7, device=torch.device("cpu"))
        self.assertEqual(outer["lineages"][0]["initialization"]["dynamics_dtype"], "float64")
        self.assertEqual(arrays["raw_output"].dtype, np.float64)
        self.assertTrue(np.all(np.isfinite(arrays["raw_kernel"])))

    def test_initialization_gate_normalizes_integer_prefix_keys(self) -> None:
        group = self.frozen["groups"]["A"]
        diagnostics = {
            "monitor_sha256": group["expected_monitor_sha256"],
            "initialization": {
                "base_state_sha256": self.frozen["expected_common_initialization"]["base_state_sha256"],
                "base_prefix_sha256": {
                    int(key): value
                    for key, value in self.frozen["expected_common_initialization"]["base_prefix_sha256"].items()
                },
                "physical_state_sha256": group["expected_physical_state_sha256"],
                "dynamics_dtype": "float64",
                "initialization_bytes": "frozen-fp32-cast-exactly-to-fp64",
            },
        }
        self.assertTrue(
            MODULE.initialization_gate(diagnostics, self.frozen, group)
        )

    def test_canonical_ledger_consumes_exactly_one_attempt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            frozen = dict(self.frozen)
            frozen["run_root"] = (
                "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
                "breadth_panel/fp64_successor/runs/local_v1"
            )
            output, ledger, attempt = MODULE.reserve_canonical_attempt(
                repo,
                frozen,
                "A",
                "cuda:0",
                {"lock_sha256": "l", "unlock_sha256": "u", "source_bundle_sha256": "s"},
            )
            self.assertEqual(output.name, "A")
            self.assertEqual(attempt["status"], "reserved")
            provenance = {
                "lock_sha256": "l",
                "unlock_sha256": "u",
                "source_bundle_sha256": "s",
            }
            MODULE.write_json(
                output / "ATTEMPT.json",
                {"schema": "breadth-fp64-local-attempt-v1", **attempt},
            )
            previous = os.environ.get("FP64_WATCHDOG_ACTIVE")
            os.environ["FP64_WATCHDOG_ACTIVE"] = (
                f"group:A:{MODULE.format_seconds(attempt['watchdog_timeout_seconds'])}"
            )
            try:
                _output, _ledger, claimed = MODULE.claim_canonical_attempt(
                    repo, frozen, "A", "cuda:0", provenance
                )
            finally:
                if previous is None:
                    os.environ.pop("FP64_WATCHDOG_ACTIVE", None)
                else:
                    os.environ["FP64_WATCHDOG_ACTIVE"] = previous
            self.assertEqual(claimed["status"], "running")
            MODULE.finish_canonical_attempt(
                ledger,
                "A",
                {"status": "complete", "gpu_seconds": 1.0},
            )
            with self.assertRaisesRegex(RuntimeError, "already consumed"):
                MODULE.reserve_canonical_attempt(
                    repo,
                    frozen,
                    "A",
                    "cuda:0",
                    {"lock_sha256": "l", "unlock_sha256": "u", "source_bundle_sha256": "s"},
                )

    def test_runner_and_adjudicator_lock_the_same_complete_bundle(self) -> None:
        self.assertEqual(MODULE.REQUIRED_LOCKED_FILES, ADJUDICATOR.REQUIRED_LOCKED_FILES)
        self.assertIn(
            str(MODULE.SUCCESSOR_RELATIVE / "watchdog_launcher.py"),
            MODULE.REQUIRED_LOCKED_FILES,
        )

    def test_terminal_prefix_classification(self) -> None:
        order = ["A", "M", "V"]
        complete = lambda passed: {  # noqa: E731
            "status": "complete",
            "all_local_gates_pass": passed,
        }
        decision = lambda passed, gate="w_cosine": {  # noqa: E731
            "all_local_gates_pass": passed,
            "gates": {gate: passed},
        }
        cases = (
            (
                {"A": complete(True), "M": complete(True), "V": complete(True)},
                {"A": decision(True), "M": decision(True), "V": decision(True)},
                {},
                "pass",
                None,
            ),
            ({"A": complete(False)}, {"A": decision(False)}, {}, "gate_fail", "A"),
            (
                {"A": complete(True), "M": complete(False)},
                {"A": decision(True), "M": decision(False)},
                {},
                "gate_fail",
                "M",
            ),
            ({"A": {"status": "failed"}}, {}, {}, "inconclusive", "A"),
            ({"A": {"status": "running"}}, {}, {}, "inconclusive", "A"),
            (
                {"A": complete(True)},
                {"A": decision(True)},
                {},
                "open",
                "M",
            ),
            (
                {"A": complete(False)},
                {"A": decision(False, "point_resource_caps")},
                {},
                "inconclusive",
                "A",
            ),
            (
                {"A": complete(True)},
                {},
                {"A": "readback_validation_failed:synthetic"},
                "inconclusive",
                "A",
            ),
        )
        for attempts, decisions, errors, expected_status, expected_group in cases:
            keys = list(attempts)
            status, _reason, group = ADJUDICATOR.classify_validated_prefix(
                order, keys, attempts, decisions, errors
            )
            self.assertEqual((status, group), (expected_status, expected_group))

    def test_stale_attempt_provenance_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(RuntimeError, "provenance differs"):
                ADJUDICATOR.verify_attempt_record(
                    Path(directory),
                    "A",
                    {
                        "group": "A",
                        "device": "cuda:0",
                        "status": "running",
                        "lock_sha256": "stale",
                    },
                    {"lock_sha256": "current"},
                )

    def test_point_resource_failure_is_independently_detected(self) -> None:
        result = {
            "outer_resources": {
                role: {
                    "elapsed_seconds": 1.0,
                    "max_gpu_allocated_gib": 1.0,
                    "max_host_rss_gib": 1.0,
                }
                for role in ("coarse", "fine")
            }
        }
        self.assertTrue(ADJUDICATOR.point_resource_caps_pass(result, self.frozen))
        result["outer_resources"]["fine"]["max_gpu_allocated_gib"] = 3.1
        self.assertFalse(ADJUDICATOR.point_resource_caps_pass(result, self.frozen))

    def test_raw_schema_corruption_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "corrupt.npz"
            np.savez(path, time=np.asarray([0.0], dtype=np.float64))
            point = {
                "step": 1e-5,
                "max_time": 1e-5,
                "lineage_start": 0,
                "lineage_stop": 1,
            }
            with self.assertRaisesRegex(RuntimeError, "schema differs"):
                ADJUDICATOR.load_raw(path, point)

    def test_remaining_stage_budget_reduces_the_next_watchdog(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            frozen = dict(self.frozen)
            provenance = {
                "lock_sha256": "l",
                "unlock_sha256": "u",
                "source_bundle_sha256": "s",
            }
            output, ledger, attempt = MODULE.reserve_canonical_attempt(
                repo, frozen, "A", "cuda:0", provenance
            )
            MODULE.write_json(
                output / "ATTEMPT.json",
                {"schema": "breadth-fp64-local-attempt-v1", **attempt},
            )
            previous = os.environ.get("FP64_WATCHDOG_ACTIVE")
            os.environ["FP64_WATCHDOG_ACTIVE"] = (
                f"group:A:{MODULE.format_seconds(attempt['watchdog_timeout_seconds'])}"
            )
            try:
                MODULE.claim_canonical_attempt(repo, frozen, "A", "cuda:0", provenance)
            finally:
                if previous is None:
                    os.environ.pop("FP64_WATCHDOG_ACTIVE", None)
                else:
                    os.environ["FP64_WATCHDOG_ACTIVE"] = previous
            MODULE.finish_canonical_attempt(
                ledger,
                "A",
                {
                    "status": "complete",
                    "gpu_seconds": 200.0,
                    "all_local_gates_pass": True,
                },
            )
            _output, _ledger, next_attempt = MODULE.reserve_canonical_attempt(
                repo, frozen, "M", "cuda:0", provenance
            )
            self.assertEqual(next_attempt["stage_gpu_seconds_before"], 200.0)
            self.assertEqual(next_attempt["watchdog_timeout_seconds"], 69.0)

    def test_external_failure_is_charged_to_the_stage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ledger = root / "ATTEMPTS.json"
            attempt = root / "A" / "ATTEMPT.json"
            attempt.parent.mkdir()
            WATCHDOG.write_atomic(
                attempt,
                {"schema": "breadth-fp64-local-attempt-v1", "status": "reserved"},
            )
            WATCHDOG.write_atomic(
                ledger,
                {
                    "stage_gpu_seconds_ceiling": 270,
                    "attempts": {"A": {"status": "reserved"}},
                },
            )
            WATCHDOG.finalize_external_group_failure(
                ledger,
                attempt,
                "A",
                12.5,
                "ExternalWatchdogTimeout",
                "synthetic timeout",
            )
            final = json.loads(ledger.read_text(encoding="utf-8"))
            self.assertEqual(final["attempts"]["A"]["status"], "failed")
            self.assertEqual(final["consumed_gpu_seconds"], 12.5)
            self.assertTrue(final["stage_budget_pass"])

    def test_atomic_terminal_publication_is_exclusive(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "RESULT.json"
            ADJUDICATOR.write_json_exclusive(path, {"status": "pass"})
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["status"], "pass")
            with self.assertRaises(FileExistsError):
                ADJUDICATOR.write_json_exclusive(path, {"status": "replacement"})

    def test_live_watchdog_cannot_be_terminally_adjudicated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            path = (
                repo
                / ADJUDICATOR.SUCCESSOR_RELATIVE
                / "watchdog_records/A.json"
            )
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps(
                    {
                        "schema": "breadth-fp64-external-watchdog-v1",
                        "status": "running",
                        "mode": "group",
                        "group": "A",
                        "device": "cuda:0",
                        "launcher_pid": os.getpid(),
                        "timeout_seconds": 89.0,
                        "stage_gpu_seconds_before": 0.0,
                    }
                ),
                encoding="utf-8",
            )
            frozen = {
                "run_root": "runs/local_v1",
                "external_watchdogs": {"group_pair_seconds": 89},
            }
            record = {
                "status": "reserved",
                "watchdog_timeout_seconds": 89.0,
                "stage_gpu_seconds_before": 0.0,
            }
            with self.assertRaises(ADJUDICATOR.LiveAttemptError):
                ADJUDICATOR.verify_group_watchdog(repo, frozen, "A", record)

    def test_raw_integer_dtypes_are_exact(self) -> None:
        point = {
            "step": 1e-5,
            "max_time": 2e-5,
            "lineage_start": 0,
            "lineage_stop": 1,
            "diagnostic_stride": 1,
            "w_monitor_size": 1,
            "w_monitor_extent": 1,
            "configuration": "centered_c1",
        }
        arrays = {
            "time": np.arange(3, dtype=np.float64) * 1e-5,
            "lineage_ids": np.asarray([0], dtype=np.int64),
            "column_lineage_id": np.asarray([0, 0], dtype=np.int64),
            "antithetic_sign": np.asarray([1, -1], dtype=np.int8),
            "array_schema_version": np.asarray(
                b"breadth-one-input-fp64-cast-arrays-v1", dtype="S48"
            ),
            "dynamics_dtype": np.asarray(b"float64", dtype="S16"),
            "initialization_contract": np.asarray(
                b"frozen-fp32-cast-exactly-to-fp64", dtype="S48"
            ),
            "checkpoint_steps": np.asarray([1, 2], dtype=np.int64),
            "w_recurrence_relative_error": np.zeros((2, 2), dtype=np.float64),
            "w_monitor_rows": np.asarray([0], dtype=np.int64),
            "w_monitor_cols": np.asarray([0], dtype=np.int64),
        }
        for field in ADJUDICATOR.OBSERVABLE_FIELDS:
            arrays[f"raw_{field}"] = np.ones((3, 2), dtype=np.float64)
            arrays[f"proxy_{field}"] = np.ones((3, 2), dtype=np.float64)
        for field in ADJUDICATOR.UPDATE_FIELDS:
            arrays[f"update_{field}"] = np.ones((2, 2), dtype=np.float64)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "raw.npz"
            np.savez(path, **arrays)
            ADJUDICATOR.load_raw(path, point)
            arrays["lineage_ids"] = np.asarray([0], dtype=np.int32)
            np.savez(path, **arrays)
            with self.assertRaisesRegex(RuntimeError, "wrong lineage IDs"):
                ADJUDICATOR.load_raw(path, point)


if __name__ == "__main__":
    unittest.main()
