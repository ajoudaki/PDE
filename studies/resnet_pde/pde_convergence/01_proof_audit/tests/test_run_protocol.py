"""Protocol-compiler and sequential-authorization tests."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


SOURCE = Path(__file__).resolve().parents[1] / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

import run_protocol as driver  # noqa: E402
import run_study  # noqa: E402
import structural_runner  # noqa: E402


class InventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = driver.load_protocol()
        cls.inventory = driver.inventory(cls.protocol)

    def test_exact_batch_counts_and_conditional_breakdown(self) -> None:
        expected = {
            "stage0-phase-a": 12,
            "stage0-phase-b": 60,
            "stage0-downward": 6,
            "stage1-screen": 24,
            "stage1-positive": 12,
            "stage2": 4,
            "stage3-screen": 8,
            "stage3-confirm": 24,
            "stage4-active": 9,
            "stage5-active": 36,
            "p70": 32,
            "stage6": 32,
        }
        self.assertEqual(
            {
                name: value["job_count"]
                for name, value in self.inventory["batches"].items()
            },
            expected,
        )
        self.assertEqual(
            self.inventory["crosschecks"],
            {
                "stage4_active_jobs": 9,
                "stage5_active_jobs": 36,
                "p70_generator_jobs": 8,
                "p70_numerics_jobs": 8,
                "p70_gain_jobs": 16,
            },
        )

    def test_every_output_is_absolute_unique_and_protocol_derived(self) -> None:
        outputs = []
        for command in driver.EXECUTION_COMMANDS:
            jobs = driver.compile_batch(command, self.protocol)
            for job in jobs:
                self.assertTrue(job.output.is_absolute())
                self.assertTrue(
                    job.output.is_relative_to(driver.RESULTS_ROOT)
                )
                self.assertEqual(job.output.suffix, ".npz")
                outputs.append(job.output)
        self.assertEqual(len(outputs), len(set(outputs)))

        phase_b = driver.compile_batch("stage0-phase-b", self.protocol)
        self.assertTrue(phase_b)
        self.assertTrue(
            all(
                "--allow-phase-b-refinements" in job.arguments
                for job in phase_b
            )
        )
        for command in ("stage0-phase-a", "stage0-downward"):
            self.assertTrue(
                all(
                    "--allow-phase-b-refinements" not in job.arguments
                    for job in driver.compile_batch(command, self.protocol)
                )
            )

    def test_generated_jobs_are_admitted_by_scientific_validators(self) -> None:
        common_validators = {
            "numerics": run_study._validate_numerics_config,
            "scaling": run_study._validate_scaling_config,
            "homogenization": run_study._validate_homogenization_config,
            "attack": run_study._validate_attack_config,
        }
        structural_validators = {
            "generator": structural_runner._validate_generator_config,
            "gain": structural_runner._validate_gain_config,
            "tail_dense": structural_runner._validate_tail_dense_config,
        }
        with mock.patch.object(
            run_study,
            "available_memory_bytes",
            return_value=512 * 1024**3,
        ):
            for command in driver.EXECUTION_COMMANDS:
                for job in driver.compile_batch(command, self.protocol):
                    if job.stage in common_validators:
                        parsed = run_study.build_parser().parse_args(
                            job.arguments
                        )
                        config = common_validators[job.stage](
                            self.protocol, parsed
                        )
                        self.assertTrue(config)
                    elif job.stage in structural_validators:
                        parsed = structural_runner.build_parser().parse_args(
                            job.arguments
                        )
                        config = structural_validators[job.stage](
                            self.protocol, parsed
                        )
                        self.assertTrue(config)
                    elif job.stage == "tail_pde":
                        # The first block of each chain is directly
                        # admissible; later blocks deliberately require the
                        # preceding sealed output and are checked below.
                        if "--restart-from" not in job.arguments:
                            parsed = (
                                structural_runner.build_parser().parse_args(
                                    job.arguments
                                )
                            )
                            config = (
                                structural_runner._validate_tail_pde_config(
                                    self.protocol, parsed
                                )
                            )
                            self.assertEqual(config["block_start"], 0.0)
                    else:
                        self.fail(f"unhandled generated stage: {job.stage}")

    def test_stage6_restart_paths_form_four_exact_chains(self) -> None:
        jobs = driver.compile_batch("stage6", self.protocol)
        pde = [job for job in jobs if job.stage == "tail_pde"]
        dense = [job for job in jobs if job.stage == "tail_dense"]
        ladder = [
            float(value)
            for value in self.protocol["stage_6_all_time_tail"][
                "horizon_ladder"
            ]
        ]
        seeds = self.protocol["stage_0_integrity_and_numerics"][
            "nested_ladder"
        ]["scramble_seeds"]
        self.assertEqual(len(pde), len(seeds) * len(ladder))
        self.assertEqual(
            len(dense),
            self.protocol["stage_6_all_time_tail"]["dense_diagnostic"][
                "roots"
            ],
        )
        for seed_index, seed in enumerate(seeds):
            chain = pde[
                seed_index * len(ladder) : (seed_index + 1) * len(ladder)
            ]
            previous = None
            for expected_end, job in zip(ladder, chain):
                arguments = list(job.arguments)
                self.assertEqual(
                    int(arguments[arguments.index("--seed") + 1]), seed
                )
                self.assertEqual(
                    float(
                        arguments[arguments.index("--block-end") + 1]
                    ),
                    expected_end,
                )
                if previous is None:
                    self.assertNotIn("--restart-from", arguments)
                else:
                    self.assertEqual(
                        Path(
                            arguments[
                                arguments.index("--restart-from") + 1
                            ]
                        ),
                        previous,
                    )
                previous = job.output


class AuthorizationTests(unittest.TestCase):
    @staticmethod
    def _summary(**results):
        return {"stage_results": results}

    def test_phase_b_authorization_uses_measured_unlock(self) -> None:
        passed = self._summary(
            stage_0_numerics={
                "phase_A_gate": {
                    "status": "PASS",
                    "reason_codes": ["NUMERICS_PHASE_A_UNLOCK_PASSES"],
                },
                "metrics": {"phase_A": {"unlocked": True}},
            }
        )
        driver.authorize("stage0-phase-b", passed)
        failed = self._summary(
            stage_0_numerics={
                "phase_A_gate": {
                    "status": "UNRESOLVED",
                    "reason_codes": [
                        "NUMERICS_PHASE_A_UNLOCK_UNRESOLVED"
                    ],
                },
                "metrics": {"phase_A": {"unlocked": False}},
            }
        )
        with self.assertRaises(driver.AuthorizationError):
            driver.authorize("stage0-phase-b", failed)

    def test_positive_and_confirmation_require_measured_triggers(self) -> None:
        positive = self._summary(
            stage_1_ordered_target={
                "gate": {
                    "reason_codes": [
                        "ORDERED_POSITIVE_TIER_TRIGGERED_INCOMPLETE"
                    ]
                },
                "metrics": {"tier": "screen"},
            }
        )
        driver.authorize("stage1-positive", positive)
        with self.assertRaises(driver.AuthorizationError):
            driver.authorize(
                "stage1-positive",
                self._summary(
                    stage_1_ordered_target={
                        "gate": {
                            "status": "FAIL",
                            "reason_codes": [
                                "ORDERED_WIDTH_RATIO_NONCONTRACTING"
                            ],
                        },
                        "metrics": {"tier": "screen"},
                    }
                ),
            )
        confirmation = self._summary(
            stage_3_same_state_attack={
                "gate": {
                    "metrics": {"confirmation_triggered": True}
                },
                "metrics": {"screen_complete": True},
            }
        )
        driver.authorize("stage3-confirm", confirmation)
        with self.assertRaises(driver.AuthorizationError):
            driver.authorize(
                "stage3-confirm",
                self._summary(
                    stage_3_same_state_attack={
                        "gate": {
                            "metrics": {"confirmation_triggered": False}
                        },
                        "metrics": {"screen_complete": True},
                    }
                ),
            )

    def test_stage5_and_p70_require_measured_generator_and_gain_gates(
        self,
    ) -> None:
        summary = self._summary(
            stage_4_generator_consistency={
                "trigger_state": "TRIGGER_READY"
            },
            stage_5_amplification={
                "P70_trigger_state": "AMPLIFIED_P15_READY"
            },
        )
        driver.authorize("stage5-active", summary)
        driver.authorize("p70", summary)
        denied = self._summary(
            stage_4_generator_consistency={
                "trigger_state": "NOT_READY"
            },
            stage_5_amplification={"P70_trigger_state": "NOT_READY"},
        )
        with self.assertRaises(driver.AuthorizationError):
            driver.authorize("stage5-active", denied)
        with self.assertRaises(driver.AuthorizationError):
            driver.authorize("p70", denied)

        # A partially completed P70 generator look preserves the measured
        # base authorization in Stage 4 while active Stage 5 still carries
        # its original P15 trigger.
        partial_resume = self._summary(
            stage_4_generator_consistency={
                "trigger_state": "P70_AUTHORIZED_AND_EVALUATED",
                "P70_authorization": {
                    "base_trigger_ready": True,
                    "authorized": True,
                },
            },
            stage_5_amplification={
                "P70_trigger_state": "AMPLIFIED_P15_READY"
            },
        )
        driver.authorize("p70", partial_resume)

    def test_stage6_requires_fresh_finite_horizon_pass(self) -> None:
        driver.authorize(
            "stage6",
            {
                "finite_horizon_identification": {
                    "gate": {"status": "PASS"}
                }
            },
        )
        for status in ("UNRESOLVED", "FAIL"):
            with self.assertRaises(driver.AuthorizationError):
                driver.authorize(
                    "stage6",
                    {
                        "finite_horizon_identification": {
                            "gate": {"status": status}
                        }
                    },
                )


class CommandSafetyTests(unittest.TestCase):
    def test_all_requested_subcommands_parse(self) -> None:
        parser = driver.build_parser()
        self.assertEqual(parser.parse_args(["status"]).command, "status")
        for command in driver.EXECUTION_COMMANDS:
            parsed = parser.parse_args([command, "--list"])
            self.assertEqual(parsed.command, command)
            self.assertTrue(parsed.list)

    def test_list_mode_does_not_create_output_tree(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "never-created"
            stream = io.StringIO()
            with (
                mock.patch.object(driver, "RESULTS_ROOT", results),
                mock.patch.object(driver, "execute_batch") as execute,
                contextlib.redirect_stdout(stream),
            ):
                self.assertEqual(
                    driver.main(["stage0-phase-a", "--list"]), 0
                )
            self.assertFalse(results.exists())
            execute.assert_not_called()
            payload = json.loads(stream.getvalue())
            self.assertEqual(payload["job_count"], 12)

    def test_draft_status_blocks_before_verifier_or_execution(self) -> None:
        protocol = {
            **driver.load_protocol(),
            "status": (
                "draft_pending_source_freeze_no_new_"
                "scientific_trajectory_generated"
            ),
        }
        with (
            mock.patch.object(driver, "verify_frozen_and_archives") as verify,
            mock.patch.object(driver, "_run_child") as child,
        ):
            with self.assertRaisesRegex(RuntimeError, "forbidden"):
                driver.execute_batch("stage0-phase-a", protocol, ())
        verify.assert_not_called()
        child.assert_not_called()

    def test_child_environment_fixes_all_thread_counts(self) -> None:
        environment = driver._child_environment()
        for key, value in driver.THREAD_ENVIRONMENT.items():
            self.assertEqual(environment[key], value)

    def test_batch_verifies_before_and_after_and_runs_serially(self) -> None:
        protocol = {**driver.load_protocol(), "status": driver.READY_STATUS}
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            jobs = tuple(
                driver.Job(
                    batch="stage2",
                    stage="homogenization",
                    program=driver.RUN_STUDY,
                    arguments=("homogenization",),
                    output=root / f"job{index}.npz",
                    identity={"index": index},
                )
                for index in range(2)
            )
            calls = []

            def run_child(command):
                calls.append(tuple(command))
                output = Path(command[command.index("--output") + 1])
                output.write_bytes(b"synthetic")

            with (
                mock.patch.object(
                    driver, "verify_frozen_and_archives"
                ) as verify,
                mock.patch.object(
                    driver, "run_analyzer", return_value={}
                ) as analyzer,
                mock.patch.object(driver, "_run_child", side_effect=run_child),
            ):
                driver.execute_batch("stage2", protocol, jobs)
            self.assertEqual(verify.call_count, 2)
            self.assertEqual(analyzer.call_count, 1)
            self.assertEqual(
                [Path(call[call.index("--output") + 1]) for call in calls],
                [job.output for job in jobs],
            )


if __name__ == "__main__":
    unittest.main()
