#!/usr/bin/env python3
"""Compile and execute the frozen proof-obligation protocol serially.

This is intentionally an orchestration layer only.  Every job coordinate is
read from ``preregistered_protocol.json``; the scientific runners remain the
sole validators and implementations of their respective dynamics.  Conditional
branches are authorized only by a freshly generated measured-gate summary.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Mapping, Sequence

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import run_study as common_runner  # noqa: E402

AUDIT_ROOT = HERE.parent
PROTOCOL_PATH = AUDIT_ROOT / "protocol" / "preregistered_protocol.json"
FREEZE_PATH = AUDIT_ROOT / "results" / "seals" / "FROZEN_INPUTS.json"
RESULTS_ROOT = AUDIT_ROOT / "results"
PROCESSED_SUMMARY = RESULTS_ROOT / "processed" / "summary.json"
RUN_STUDY = HERE / "run_study.py"
STRUCTURAL_RUNNER = HERE / "structural_runner.py"
ANALYZER = HERE / "analyze_results.py"
VERIFIER = AUDIT_ROOT / "protocol" / "verify_study.py"
READY_STATUS = "preregistered_before_new_scientific_trajectories"
THREAD_ENVIRONMENT = {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "BLIS_NUM_THREADS": "1",
    "PYTHONHASHSEED": "0",
}


class AuthorizationError(RuntimeError):
    """Raised when a measured sequential gate does not authorize a branch."""


def _reject_duplicate_pairs(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(
            handle, object_pairs_hook=_reject_duplicate_pairs
        )
    if not isinstance(value, dict):
        raise ValueError(f"JSON root is not an object: {path}")
    return value


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_protocol() -> dict[str, Any]:
    return common_runner.load_protocol(PROTOCOL_PATH)


def _format_number(value: int | float) -> str:
    return f"{float(value):.15g}" if isinstance(value, float) else str(value)


@dataclass(frozen=True)
class Job:
    """One exact scientific-runner invocation."""

    batch: str
    stage: str
    program: Path
    arguments: tuple[str, ...]
    output: Path
    identity: Mapping[str, Any]

    def command(self) -> tuple[str, ...]:
        return (
            sys.executable,
            str(self.program),
            *self.arguments,
            "--output",
            str(self.output),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "batch": self.batch,
            "stage": self.stage,
            "program": str(self.program),
            "arguments": list(self.arguments),
            "output": str(self.output),
            "identity": dict(self.identity),
        }


def _output_path(stage: str, identity: Mapping[str, Any]) -> Path:
    digest = hashlib.sha256(
        _canonical_json(identity).encode("utf-8")
    ).hexdigest()[:20]
    return RESULTS_ROOT / stage / f"{stage}_{digest}.npz"


def _job(
    *,
    batch: str,
    stage: str,
    program: Path,
    arguments: Sequence[str],
    identity: Mapping[str, Any],
) -> Job:
    complete_identity = {
        "batch": batch,
        "stage": stage,
        "program": program.name,
        **dict(identity),
    }
    return Job(
        batch=batch,
        stage=stage,
        program=program,
        arguments=tuple(str(value) for value in arguments),
        output=_output_path(stage, complete_identity),
        identity=complete_identity,
    )


def _resolution_configs(
    resolution: Mapping[str, Any],
) -> tuple[dict[str, int | float], ...]:
    """Expand exactly the declared primary scrambles and refinements."""

    primary = resolution["primary"]
    configs = [
        {
            "base_order": int(primary["base_order"]),
            "N": int(primary["N"]),
            "R": int(primary["R"]),
            "dt": float(primary["dt"]),
            "seed": int(seed),
        }
        for seed in primary["scramble_seeds"]
    ]
    configs.extend(
        {
            "base_order": int(item["base_order"]),
            "N": int(item["N"]),
            "R": int(item["R"]),
            "dt": float(item["dt"]),
            "seed": int(item["seed"]),
        }
        for item in resolution[
            "one_axis_refinements_at_seed_20260723"
        ]
    )
    canonical = [_canonical_json(item) for item in configs]
    if len(canonical) != len(set(canonical)):
        raise ValueError("resolution inventory contains duplicate jobs")
    return tuple(configs)


def _time_grid_names(stage5: Mapping[str, Any]) -> tuple[str, ...]:
    grids = stage5["time_grids"]
    names = tuple(
        str(name)
        for name, values in grids.items()
        if isinstance(values, list)
    )
    if not names:
        raise ValueError("Stage-5 has no declared source-time grids")
    return names


def _numerics_job(
    batch: str,
    P: int,
    config: Mapping[str, Any],
    *,
    horizon: float,
    phase_b: bool = False,
    conditional_p70: bool = False,
) -> Job:
    arguments = [
        "numerics",
        "--P",
        str(P),
        "--base-order",
        str(int(config["base_order"])),
        "--N",
        str(int(config["N"])),
        "--R",
        str(int(config["R"])),
        "--dt",
        _format_number(float(config["dt"])),
        "--seed",
        str(int(config["seed"])),
        "--T",
        _format_number(float(horizon)),
    ]
    if phase_b:
        arguments.append("--allow-phase-b-refinements")
    if conditional_p70:
        arguments.append("--allow-conditional-p70")
    return _job(
        batch=batch,
        stage="numerics",
        program=RUN_STUDY,
        arguments=arguments,
        identity={
            "P": int(P),
            "T": float(horizon),
            **{
                key: config[key]
                for key in ("base_order", "N", "R", "dt", "seed")
            },
            "phase_b": phase_b,
            "conditional_p70": conditional_p70,
        },
    )


def _structural_resolution_arguments(
    config: Mapping[str, Any],
) -> list[str]:
    return [
        "--base-order",
        str(int(config["base_order"])),
        "--N",
        str(int(config["N"])),
        "--R",
        str(int(config["R"])),
        "--dt",
        _format_number(float(config["dt"])),
        "--seed",
        str(int(config["seed"])),
    ]


def compile_batch(
    command: str,
    protocol: Mapping[str, Any],
) -> tuple[Job, ...]:
    """Compile one named batch solely from frozen protocol fields."""

    stage0 = protocol["stage_0_integrity_and_numerics"]
    execution = stage0["execution_inventory"]
    active_levels = tuple(int(value) for value in execution["active_levels"])
    jobs: list[Job] = []
    if command in {
        "stage0-phase-a",
        "stage0-phase-b",
        "stage0-downward",
    }:
        if command == "stage0-phase-a":
            configs = execution["phase_A_primary_configs_per_level"]
            phase_b = False
        elif command == "stage0-phase-b":
            configs = execution[
                "phase_B_conditional_upward_configs_per_level"
            ]
            phase_b = True
        else:
            configs = execution[
                "seed0_downward_diagnostic_configs_per_level"
            ]
            phase_b = False
        for P in active_levels:
            for config in configs:
                jobs.append(
                    _numerics_job(
                        command,
                        P,
                        config,
                        horizon=float(stage0["active_horizon"]),
                        phase_b=phase_b,
                    )
                )
    elif command in {"stage1-screen", "stage1-positive"}:
        tier = command.removeprefix("stage1-")
        stage = protocol["stage_1_ordered_target"]
        grid = stage[f"{tier}_grid"]
        n_grid = ",".join(str(int(value)) for value in grid["n"])
        L_grid = ",".join(str(int(value)) for value in grid["L"])
        for root in range(int(grid["coupled_roots"])):
            jobs.append(
                _job(
                    batch=command,
                    stage="scaling",
                    program=RUN_STUDY,
                    arguments=[
                        "scaling",
                        "--tier",
                        tier,
                        "--n-grid",
                        n_grid,
                        "--L-grid",
                        L_grid,
                        "--root-index",
                        str(root),
                        "--T",
                        _format_number(float(stage["active_horizon"])),
                        "--dt",
                        _format_number(float(stage["dt"])),
                    ],
                    identity={
                        "tier": tier,
                        "n_grid": list(grid["n"]),
                        "L_grid": list(grid["L"]),
                        "root_index": root,
                    },
                )
            )
    elif command == "stage2":
        stage = protocol["stage_2_homogenization"]
        depths = ",".join(str(int(value)) for value in stage["depths"])
        dt = float(protocol["stage_1_ordered_target"]["dt"])
        for root in range(int(stage["outer_B_a_roots"])):
            jobs.append(
                _job(
                    batch=command,
                    stage="homogenization",
                    program=RUN_STUDY,
                    arguments=[
                        "homogenization",
                        "--outer-root-index",
                        str(root),
                        "--depths",
                        depths,
                        "--replicas",
                        str(
                            int(
                                stage[
                                    "independent_W_replicas_per_outer_root"
                                ]
                            )
                        ),
                        "--dt",
                        _format_number(dt),
                    ],
                    identity={
                        "outer_root_index": root,
                        "widths": list(stage["widths"]),
                        "depths": list(stage["depths"]),
                        "replicas": int(
                            stage[
                                "independent_W_replicas_per_outer_root"
                            ]
                        ),
                    },
                )
            )
    elif command in {"stage3-screen", "stage3-confirm"}:
        stage = protocol["stage_3_same_state_attack"]
        sequential = stage["sequential_design"]
        cells = (
            [sequential["screen_cell"]]
            if command == "stage3-screen"
            else sequential["confirmation_cells"]
        )
        root_count = int(stage["heldout_roots"])
        if int(sequential["screen_roots"]) != root_count:
            raise ValueError("Stage-3 root inventory is inconsistent")
        for cell in cells:
            for root in range(root_count):
                jobs.append(
                    _job(
                        batch=command,
                        stage="attack",
                        program=RUN_STUDY,
                        arguments=[
                            "attack",
                            "--n",
                            str(int(cell["n"])),
                            "--L",
                            str(int(cell["L"])),
                            "--root-index",
                            str(root),
                        ],
                        identity={
                            "n": int(cell["n"]),
                            "L": int(cell["L"]),
                            "root_index": root,
                        },
                    )
                )
    elif command == "stage4-active":
        stage = protocol["stage_4_generator_consistency"]
        resolution = stage["numerical_resolution"]
        maximum_level = max(int(value) for value in stage["levels"])
        for config in _resolution_configs(resolution):
            jobs.append(
                _job(
                    batch=command,
                    stage="generator",
                    program=STRUCTURAL_RUNNER,
                    arguments=[
                        "generator",
                        *_structural_resolution_arguments(config),
                        "--max-level",
                        str(maximum_level),
                    ],
                    identity={"max_level": maximum_level, **config},
                )
            )
    elif command == "stage5-active":
        stage = protocol["stage_5_amplification"]
        configs = _resolution_configs(stage["numerical_resolution"])
        pair_by_low = {
            int(low): int(high) for low, high in stage["residual_pairs"]
        }
        if set(pair_by_low) != {
            int(value) for value in stage["low_levels"]
        }:
            raise ValueError("Stage-5 low-level/pair inventories disagree")
        for low_level in stage["low_levels"]:
            high_level = pair_by_low[int(low_level)]
            for time_grid in _time_grid_names(stage):
                for config in configs:
                    jobs.append(
                        _job(
                            batch=command,
                            stage="gain",
                            program=STRUCTURAL_RUNNER,
                            arguments=[
                                "gain",
                                *_structural_resolution_arguments(config),
                                "--low-level",
                                str(int(low_level)),
                                "--high-level",
                                str(high_level),
                                "--time-grid",
                                str(time_grid),
                            ],
                            identity={
                                "low_level": int(low_level),
                                "high_level": high_level,
                                "time_grid": str(time_grid),
                                **config,
                            },
                        )
                    )
    elif command == "p70":
        p70_declaration = stage0["P70_conditional_extension"]
        p70_level = int(p70_declaration["P"])
        resolution = p70_declaration["numerical_resolution"]
        configs = _resolution_configs(resolution)
        for config in configs:
            jobs.append(
                _job(
                    batch=command,
                    stage="generator",
                    program=STRUCTURAL_RUNNER,
                    arguments=[
                        "generator",
                        *_structural_resolution_arguments(config),
                        "--max-level",
                        str(p70_level),
                        "--allow-conditional-p70",
                    ],
                    identity={"max_level": p70_level, **config},
                )
            )
        for config in execution["conditional_P70_configs"]:
            jobs.append(
                _numerics_job(
                    command,
                    p70_level,
                    config,
                    horizon=float(stage0["active_horizon"]),
                    conditional_p70=True,
                )
            )
        stage5 = protocol["stage_5_amplification"]
        conditional_pair = tuple(
            int(value)
            for value in stage5["conditional_P70_extension"][
                "residual_pair"
            ]
        )
        if len(conditional_pair) != 2 or conditional_pair[1] != p70_level:
            raise ValueError("conditional P70 residual pair is inconsistent")
        low_level, high_level = conditional_pair
        for time_grid in _time_grid_names(stage5):
            for config in configs:
                jobs.append(
                    _job(
                        batch=command,
                        stage="gain",
                        program=STRUCTURAL_RUNNER,
                        arguments=[
                            "gain",
                            *_structural_resolution_arguments(config),
                            "--low-level",
                            str(low_level),
                            "--high-level",
                            str(high_level),
                            "--time-grid",
                            str(time_grid),
                            "--allow-conditional-p70",
                        ],
                        identity={
                            "low_level": low_level,
                            "high_level": high_level,
                            "time_grid": str(time_grid),
                            **config,
                        },
                    )
                )
    elif command == "stage6":
        stage = protocol["stage_6_all_time_tail"]
        trigger = stage.get("execution_trigger")
        if not isinstance(trigger, str) or not trigger.strip():
            raise ValueError("Stage 6 has no frozen execution trigger")
        ladder = tuple(float(value) for value in stage["horizon_ladder"])
        boundaries = tuple(zip((0.0,) + ladder[:-1], ladder))
        primary = stage0["nested_ladder"]
        for seed in primary["scramble_seeds"]:
            previous: Path | None = None
            for start, end in boundaries:
                identity = {
                    "seed": int(seed),
                    "block_start": start,
                    "block_end": end,
                }
                output = _output_path(
                    "tail_pde",
                    {
                        "batch": command,
                        "stage": "tail_pde",
                        "program": STRUCTURAL_RUNNER.name,
                        **identity,
                    },
                )
                arguments = [
                    "tail-pde",
                    "--block-end",
                    _format_number(end),
                    "--base-order",
                    str(int(primary["primary_base_order"])),
                    "--N",
                    str(int(primary["primary_N"])),
                    "--R",
                    str(int(primary["primary_R"])),
                    "--dt",
                    _format_number(float(primary["primary_dt"])),
                    "--seed",
                    str(int(seed)),
                ]
                if previous is not None:
                    arguments.extend(
                        ["--restart-from", str(previous)]
                    )
                jobs.append(
                    Job(
                        batch=command,
                        stage="tail_pde",
                        program=STRUCTURAL_RUNNER,
                        arguments=tuple(arguments),
                        output=output,
                        identity={
                            "batch": command,
                            "stage": "tail_pde",
                            "program": STRUCTURAL_RUNNER.name,
                            **identity,
                        },
                    )
                )
                previous = output
        dense = stage["dense_diagnostic"]
        dt = float(protocol["stage_1_ordered_target"]["dt"])
        for root in range(int(dense["roots"])):
            jobs.append(
                _job(
                    batch=command,
                    stage="tail_dense",
                    program=STRUCTURAL_RUNNER,
                    arguments=[
                        "tail-dense",
                        "--root-index",
                        str(root),
                        "--horizon",
                        _format_number(float(dense["maximum_horizon"])),
                        "--dt",
                        _format_number(dt),
                    ],
                    identity={
                        "root_index": root,
                        "n": int(dense["n"]),
                        "L": int(dense["L"]),
                        "horizon": float(dense["maximum_horizon"]),
                    },
                )
            )
    else:
        raise ValueError(f"unknown protocol batch: {command}")
    outputs = [job.output for job in jobs]
    if len(outputs) != len(set(outputs)):
        raise ValueError(f"{command} compiled duplicate output paths")
    return tuple(jobs)


EXECUTION_COMMANDS = (
    "stage0-phase-a",
    "stage0-phase-b",
    "stage0-downward",
    "stage1-screen",
    "stage1-positive",
    "stage2",
    "stage3-screen",
    "stage3-confirm",
    "stage4-active",
    "stage5-active",
    "p70",
    "stage6",
)


def inventory(protocol: Mapping[str, Any]) -> dict[str, Any]:
    batches = {
        command: compile_batch(command, protocol)
        for command in EXECUTION_COMMANDS
    }
    p70 = batches["p70"]
    return {
        "protocol_status": protocol.get("status"),
        "batches": {
            name: {
                "job_count": len(jobs),
                "existing_outputs": sum(
                    job.output.is_file() for job in jobs
                ),
                "jobs": [job.to_dict() for job in jobs],
            }
            for name, jobs in batches.items()
        },
        "crosschecks": {
            "stage4_active_jobs": len(batches["stage4-active"]),
            "stage5_active_jobs": len(batches["stage5-active"]),
            "p70_generator_jobs": sum(
                job.stage == "generator" for job in p70
            ),
            "p70_numerics_jobs": sum(
                job.stage == "numerics" for job in p70
            ),
            "p70_gain_jobs": sum(job.stage == "gain" for job in p70),
        },
    }


def _child_environment() -> dict[str, str]:
    environment = dict(os.environ)
    environment.update(THREAD_ENVIRONMENT)
    return environment


def _run_child(arguments: Sequence[str], *, capture: bool = False) -> str:
    completed = subprocess.run(
        list(arguments),
        check=True,
        env=_child_environment(),
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=None,
    )
    return completed.stdout or ""


def verify_frozen_and_archives() -> None:
    raw = _run_child(
        (
            sys.executable,
            str(VERIFIER),
            "--check-evidence",
        ),
        capture=True,
    )
    payload = json.loads(raw)
    if not isinstance(payload, Mapping) or payload.get("status") != "verified":
        raise ValueError("freeze verifier returned an invalid status payload")


def run_analyzer() -> dict[str, Any]:
    raw = _run_child(
        (
            sys.executable,
            str(ANALYZER),
            "--audit-root",
            str(AUDIT_ROOT),
        ),
        capture=True,
    )
    payload = json.loads(raw)
    if not isinstance(payload, Mapping) or payload.get("status") != "analyzed":
        raise ValueError("analyzer returned an invalid status payload")
    summary = _load_json(PROCESSED_SUMMARY)
    if not FREEZE_PATH.is_file():
        raise FileNotFoundError(f"missing freeze: {FREEZE_PATH}")
    identity = summary.get("analysis_identity")
    if not isinstance(identity, Mapping):
        raise ValueError("processed summary has no analysis identity")
    if (
        identity.get("protocol_sha256") != _sha256_file(PROTOCOL_PATH)
        or identity.get("frozen_inputs_sha256")
        != _sha256_file(FREEZE_PATH)
        or identity.get("analyzer_source_sha256")
        != _sha256_file(ANALYZER)
        or identity.get("scientific_trajectory_execution") is not False
    ):
        raise ValueError("processed summary identity does not match the freeze")
    return summary


def _stage_result(
    summary: Mapping[str, Any], key: str
) -> Mapping[str, Any]:
    results = summary.get("stage_results")
    if not isinstance(results, Mapping):
        raise AuthorizationError("analysis summary has no stage results")
    value = results.get(key)
    if not isinstance(value, Mapping):
        raise AuthorizationError(f"analysis summary lacks {key}")
    return value


def authorize(command: str, summary: Mapping[str, Any]) -> None:
    """Authorize a conditional branch from measured analyzed gates only."""

    if command == "stage0-phase-b":
        result = _stage_result(summary, "stage_0_numerics")
        phase_gate = result.get("phase_A_gate", {})
        phase_metrics = result.get("metrics", {}).get("phase_A", {})
        if not (
            isinstance(phase_gate, Mapping)
            and phase_gate.get("status") == "PASS"
            and "NUMERICS_PHASE_A_UNLOCK_PASSES"
            in phase_gate.get("reason_codes", ())
            and isinstance(phase_metrics, Mapping)
            and phase_metrics.get("unlocked") is True
        ):
            raise AuthorizationError(
                "measured Stage-0 Phase-A gate did not authorize Phase B"
            )
    elif command == "stage1-positive":
        result = _stage_result(summary, "stage_1_ordered_target")
        reasons = result.get("gate", {}).get("reason_codes", ())
        initial_trigger = (
            "ORDERED_POSITIVE_TIER_TRIGGERED_INCOMPLETE" in reasons
            and result.get("metrics", {}).get("tier") == "screen"
        )
        screen_gate = result.get("screen_gate")
        resumed_authorized = (
            isinstance(screen_gate, Mapping)
            and screen_gate.get("status") != "FAIL"
            and result.get("metrics", {}).get("tier") == "positive"
        )
        if not (initial_trigger or resumed_authorized):
            raise AuthorizationError(
                "measured Stage-1 screen did not authorize the positive tier"
            )
    elif command == "stage3-confirm":
        result = _stage_result(summary, "stage_3_same_state_attack")
        gate_metrics = result.get("gate", {}).get("metrics", {})
        metrics = result.get("metrics", {})
        if not (
            isinstance(gate_metrics, Mapping)
            and gate_metrics.get("confirmation_triggered") is True
            and isinstance(metrics, Mapping)
            and metrics.get("screen_complete") is True
        ):
            raise AuthorizationError(
                "measured Stage-3 screen did not authorize confirmation"
            )
    elif command == "stage5-active":
        stage4 = _stage_result(summary, "stage_4_generator_consistency")
        already_authorized = (
            isinstance(stage4.get("P70_authorization"), Mapping)
            and stage4["P70_authorization"].get("base_trigger_ready")
            is True
        )
        if not (
            stage4.get("trigger_state") == "TRIGGER_READY"
            or already_authorized
        ):
            raise AuthorizationError(
                "measured Stage-4 generator gate did not authorize Stage 5"
            )
    elif command == "p70":
        stage4 = _stage_result(summary, "stage_4_generator_consistency")
        stage5 = _stage_result(summary, "stage_5_amplification")
        stage4_auth = stage4.get("P70_authorization")
        stage5_auth = stage5.get("P70_authorization")
        measured_base_ready = (
            stage4.get("trigger_state") == "TRIGGER_READY"
            or (
                isinstance(stage4_auth, Mapping)
                and (
                    stage4_auth.get("base_trigger_ready") is True
                    or stage4_auth.get("authorized") is True
                )
            )
        )
        measured_p15_ready = (
            stage5.get("P70_trigger_state") == "AMPLIFIED_P15_READY"
            or (
                isinstance(stage5_auth, Mapping)
                and (
                    stage5_auth.get("P15_amplification_ready") is True
                    or stage5_auth.get("authorized") is True
                )
            )
        )
        if not (measured_base_ready and measured_p15_ready):
            raise AuthorizationError(
                "measured Stage-4/5 gates did not authorize P70"
            )
    elif command == "stage6":
        result = summary.get("finite_horizon_identification")
        if (
            not isinstance(result, Mapping)
            or not isinstance(result.get("gate"), Mapping)
            or result["gate"].get("status") != "PASS"
        ):
            raise AuthorizationError(
                "measured finite-horizon identification gate did not "
                "authorize Stage 6"
            )


CONDITIONAL_COMMANDS = {
    "stage0-phase-b",
    "stage1-positive",
    "stage3-confirm",
    "stage5-active",
    "p70",
    "stage6",
}


def execute_batch(
    command: str,
    protocol: Mapping[str, Any],
    jobs: Sequence[Job],
) -> None:
    if protocol.get("status") != READY_STATUS:
        raise RuntimeError(
            "scientific execution is forbidden while protocol status is "
            f"{protocol.get('status')!r}; expected {READY_STATUS!r}"
        )
    verify_frozen_and_archives()
    if command in CONDITIONAL_COMMANDS:
        authorize(command, run_analyzer())
    for job in jobs:
        _run_child(job.command())
    missing = [str(job.output) for job in jobs if not job.output.is_file()]
    if missing:
        raise RuntimeError(
            "scientific runner returned without publishing expected outputs: "
            + ", ".join(missing)
        )
    verify_frozen_and_archives()
    run_analyzer()


def _status_payload(protocol: Mapping[str, Any]) -> dict[str, Any]:
    compiled = inventory(protocol)
    protocol_ready = protocol.get("status") == READY_STATUS
    freeze_present = FREEZE_PATH.is_file()
    payload = {
        "protocol_status": protocol.get("status"),
        "protocol_ready": protocol_ready,
        "execution_ready": protocol_ready and freeze_present,
        "freeze_present": freeze_present,
        "processed_summary_present": PROCESSED_SUMMARY.is_file(),
        "batch_counts": {
            key: value["job_count"]
            for key, value in compiled["batches"].items()
        },
        "existing_outputs": {
            key: value["existing_outputs"]
            for key, value in compiled["batches"].items()
        },
        "crosschecks": compiled["crosschecks"],
        "thread_environment": THREAD_ENVIRONMENT,
    }
    if freeze_present:
        verify_frozen_and_archives()
        payload["freeze_verified"] = True
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Execute exact frozen PDE proof-obligation batches."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("status")
    for command in EXECUTION_COMMANDS:
        child = subparsers.add_parser(command)
        mode = child.add_mutually_exclusive_group()
        mode.add_argument(
            "--list",
            action="store_true",
            help="print the exact batch without executing it",
        )
        mode.add_argument(
            "--dry-run",
            action="store_true",
            help="alias for --list; performs no writes",
        )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    protocol = load_protocol()
    if args.command == "status":
        print(json.dumps(_status_payload(protocol), indent=2, sort_keys=True))
        return 0
    jobs = compile_batch(args.command, protocol)
    if args.list or args.dry_run:
        print(
            json.dumps(
                {
                    "protocol_status": protocol.get("status"),
                    "execution_would_be_allowed": (
                        protocol.get("status") == READY_STATUS
                    ),
                    "batch": args.command,
                    "job_count": len(jobs),
                    "jobs": [job.to_dict() for job in jobs],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    execute_batch(args.command, protocol, jobs)
    print(
        json.dumps(
            {
                "status": "completed",
                "batch": args.command,
                "job_count": len(jobs),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
