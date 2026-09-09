#!/usr/bin/env python3
"""Hash-locked FP64 explicit-Euler A/M/V local qualification.

The exact frozen FP32 initialization is regenerated and cast to FP64.  The
frozen FP32 runner is not edited: a hash-checked six-token dtype transform is
compiled in memory, and its transformed digest is itself frozen.
"""

from __future__ import annotations

import argparse
import copy
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback
import types
from typing import Any

os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"

import numpy as np
import torch


SUCCESSOR_RELATIVE = Path(
    "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
    "breadth_panel/fp64_successor"
)
CONFIG_RELATIVE = SUCCESSOR_RELATIVE / "FROZEN_LOCAL_QUALIFICATION.json"
LOCK_RELATIVE = SUCCESSOR_RELATIVE / "FROZEN_LOCAL_QUALIFICATION_LOCK.json"
UNLOCK_RELATIVE = SUCCESSOR_RELATIVE / "LOCAL_QUALIFICATION_UNLOCK.json"
STAGE_RESULT_RELATIVE = SUCCESSOR_RELATIVE / "LOCAL_QUALIFICATION_RESULT.json"
REQUIRED_LOCKED_FILES = frozenset(
    {
        str(SUCCESSOR_RELATIVE / "PROTOCOL.md"),
        str(CONFIG_RELATIVE),
        str(SUCCESSOR_RELATIVE / "run_local_qualification.py"),
        str(SUCCESSOR_RELATIVE / "adjudicate_local_qualification.py"),
        str(SUCCESSOR_RELATIVE / "gpu_preflight.py"),
        str(SUCCESSOR_RELATIVE / "watchdog_launcher.py"),
        str(SUCCESSOR_RELATIVE / "tests/test_fp64_local.py"),
        "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
        "breadth_panel/FROZEN_ONE_INPUT_POINTS.json",
        "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
        "breadth_panel/one_input/one_input_engine.py",
        "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
        "breadth_panel/one_input/one_input_runner.py",
        "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
        "width_ladder/euler_fp32/euler_engine.py",
        "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
        "width_ladder/euler_fp32/nested_init.py",
    }
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} is not a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    write_json(temporary, value)
    os.replace(temporary, path)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def format_seconds(value: float) -> str:
    return format(float(value), ".12g")


def source_bundle_sha256(files: dict[str, str]) -> str:
    return sha256_bytes(
        "\n".join(f"{name} {digest}" for name, digest in sorted(files.items())).encode()
    )


def cuda_identity(device_name: str) -> dict[str, Any]:
    device = torch.device(device_name)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("an available CUDA device is required")
    properties = torch.cuda.get_device_properties(device)
    identity: dict[str, Any] = {
        "name": properties.name,
        "total_memory_bytes": int(properties.total_memory),
        "compute_capability": [int(properties.major), int(properties.minor)],
        "multi_processor_count": int(properties.multi_processor_count),
    }
    uuid = getattr(properties, "uuid", None)
    if uuid is not None:
        identity["uuid"] = str(uuid)
    return identity


def verify_lock(
    repo: Path,
    config_path: Path,
    lock_path: Path,
    unlock_path: Path,
    group: str,
    device: str,
) -> dict[str, str]:
    canonical_config = (repo / CONFIG_RELATIVE).resolve()
    canonical_lock = (repo / LOCK_RELATIVE).resolve()
    canonical_unlock = (repo / UNLOCK_RELATIVE).resolve()
    if config_path.resolve() != canonical_config:
        raise RuntimeError("configuration is not the canonical successor file")
    if lock_path.resolve() != canonical_lock:
        raise RuntimeError("source lock is not the canonical successor file")
    if unlock_path.resolve() != canonical_unlock:
        raise RuntimeError("unlock is not the canonical successor file")
    lock = read_json(lock_path)
    if lock.get("schema") != "breadth-fp64-local-lock-v1" or lock.get("status") != "frozen":
        raise RuntimeError("invalid or unfrozen FP64 source lock")
    files = lock.get("files")
    if not isinstance(files, dict) or not files:
        raise RuntimeError("source lock has no files")
    if set(files) != REQUIRED_LOCKED_FILES:
        raise RuntimeError("source lock does not contain the exact canonical dependency set")
    bundle_sha = source_bundle_sha256(files)
    if lock.get("bundle_sha256") != bundle_sha:
        raise RuntimeError("source-lock bundle digest is invalid")
    for relative, expected in files.items():
        actual = sha256_file(repo / relative)
        if actual != expected:
            raise RuntimeError(f"source-lock mismatch for {relative}: {actual} != {expected}")
    lock_sha = sha256_file(lock_path)
    frozen = read_json(config_path)
    unlock = read_json(unlock_path)
    if unlock.get("schema") != "breadth-fp64-local-unlock-v1" or unlock.get("status") != "authorized":
        raise RuntimeError("FP64 local execution is not authorized")
    if unlock.get("lock_sha256") != lock_sha:
        raise RuntimeError("unlock does not bind the current source lock")
    config_sha = sha256_file(config_path)
    if unlock.get("config_sha256") != config_sha:
        raise RuntimeError("unlock does not bind the current frozen configuration")
    if unlock.get("authorized_groups") != ["A", "M", "V"]:
        raise RuntimeError("unlock does not authorize the exact frozen group sequence")
    if group not in unlock["authorized_groups"]:
        raise RuntimeError(f"group {group} is not authorized")
    if device not in unlock.get("authorized_devices", []):
        raise RuntimeError(f"device {device} is not authorized")
    if int(unlock.get("max_attempts_per_group", 0)) != 1:
        raise RuntimeError("unlock must authorize exactly one attempt per group")
    preflight_contract = unlock.get("gpu_preflight", {})
    preflight_path = repo / preflight_contract.get("path", "")
    expected_preflight_path = (repo / SUCCESSOR_RELATIVE / "GPU_PREFLIGHT.json").resolve()
    if preflight_path.resolve() != expected_preflight_path:
        raise RuntimeError("unlock names a noncanonical GPU preflight")
    if not preflight_path.is_file():
        raise RuntimeError("authorized GPU preflight is missing")
    if sha256_file(preflight_path) != preflight_contract.get("sha256"):
        raise RuntimeError("GPU preflight digest differs from the unlock")
    preflight = read_json(preflight_path)
    preflight_attempt_path = repo / preflight_contract.get("attempt_path", "")
    expected_attempt_path = (
        repo / SUCCESSOR_RELATIVE / "GPU_PREFLIGHT_ATTEMPT.json"
    ).resolve()
    if preflight_attempt_path.resolve() != expected_attempt_path:
        raise RuntimeError("unlock names a noncanonical GPU preflight attempt")
    if sha256_file(preflight_attempt_path) != preflight_contract.get("attempt_sha256"):
        raise RuntimeError("GPU preflight-attempt digest differs from the unlock")
    preflight_attempt = read_json(preflight_attempt_path)
    preflight_watchdog_path = repo / preflight_contract.get("watchdog_path", "")
    expected_watchdog_path = (
        repo / SUCCESSOR_RELATIVE / "watchdog_records/preflight.json"
    ).resolve()
    if preflight_watchdog_path.resolve() != expected_watchdog_path:
        raise RuntimeError("unlock names a noncanonical preflight watchdog")
    if sha256_file(preflight_watchdog_path) != preflight_contract.get("watchdog_sha256"):
        raise RuntimeError("preflight-watchdog digest differs from the unlock")
    preflight_watchdog = read_json(preflight_watchdog_path)
    current_identity = cuda_identity(device)
    if (
        preflight.get("status") != "pass"
        or preflight.get("device") != device
        or preflight.get("lock_sha256") != lock_sha
        or preflight.get("config_sha256") != config_sha
        or preflight.get("dynamics_dtype") != "float64"
        or preflight.get("initialization_contract")
        != "frozen-fp32-cast-exactly-to-fp64"
        or preflight.get("initialization_ok") is not True
        or preflight.get("resource_caps_pass") is not True
        or preflight.get("deterministic_replay") is not True
        or preflight.get("float64_arrays") is not True
        or preflight.get("deterministic_algorithms") is not True
        or preflight.get("tf32_matmul") is not False
        or preflight.get("tf32_cudnn") is not False
        or preflight.get("cublas_workspace_config") != ":4096:8"
        or preflight.get("gpu_identity") != current_identity
        or preflight.get("torch_version") != torch.__version__
        or preflight.get("cuda_version") != torch.version.cuda
        or preflight.get("external_watchdog")
        != f"preflight:preflight:{int(frozen['external_watchdogs']['gpu_preflight_seconds'])}"
        or preflight_attempt.get("status") != "pass"
        or preflight_attempt.get("result_sha256") != sha256_file(preflight_path)
        or preflight_attempt.get("lock_sha256") != lock_sha
        or preflight_attempt.get("config_sha256") != config_sha
        or preflight_watchdog.get("status") != "completed"
        or preflight_watchdog.get("mode") != "preflight"
        or preflight_watchdog.get("device") != device
        or preflight_watchdog.get("returncode") != 0
        or preflight_watchdog.get("timeout_seconds")
        != int(frozen["external_watchdogs"]["gpu_preflight_seconds"])
        or preflight_watchdog.get("result_sha256") != sha256_file(preflight_path)
        or preflight_watchdog.get("attempt_sha256") != sha256_file(preflight_attempt_path)
    ):
        raise RuntimeError("GPU preflight does not authorize this execution environment")
    return {
        "lock_sha256": lock_sha,
        "unlock_sha256": sha256_file(unlock_path),
        "config_sha256": config_sha,
        "preflight_sha256": sha256_file(preflight_path),
        "preflight_attempt_sha256": sha256_file(preflight_attempt_path),
        "preflight_watchdog_sha256": sha256_file(preflight_watchdog_path),
        "source_bundle_sha256": bundle_sha,
    }


def load_fp64_runner(repo: Path, frozen: dict[str, Any]):
    panel = repo / "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/breadth_panel"
    one_input = panel / "one_input"
    if str(one_input) not in sys.path:
        sys.path.insert(0, str(one_input))
    model = importlib.import_module("one_input_engine")
    if Path(model.__file__).resolve() != (one_input / "one_input_engine.py").resolve():
        raise RuntimeError("one_input_engine was imported from an unexpected path")
    expected_euler = (
        repo
        / "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign"
        / "width_ladder/euler_fp32/euler_engine.py"
    ).resolve()
    expected_init = expected_euler.with_name("nested_init.py")
    if Path(model.audited_euler.__file__).resolve() != expected_euler:
        raise RuntimeError("euler_engine was imported from an unexpected path")
    if Path(model.audited_init.__file__).resolve() != expected_init:
        raise RuntimeError("nested_init was imported from an unexpected path")

    transform = frozen["source_transform"]
    source_path = repo / transform["runner_path"]
    source_bytes = source_path.read_bytes()
    if sha256_bytes(source_bytes) != transform["runner_sha256"]:
        raise RuntimeError("frozen FP32 runner digest changed")
    source = source_bytes.decode("utf-8")
    token = "torch.float32"
    if source.count(token) != int(transform["torch_float32_occurrences"]):
        raise RuntimeError("unexpected FP32 token count in frozen runner")
    transformed = source.replace(token, "torch.float64")
    if sha256_bytes(transformed.encode("utf-8")) != transform["transformed_runner_sha256"]:
        raise RuntimeError("FP64 transformed-runner digest changed")

    module_name = "breadth_fp64_successor_transformed_runner"
    module = types.ModuleType(module_name)
    module.__file__ = str(source_path)
    sys.modules[module_name] = module
    exec(compile(transformed, str(source_path), "exec"), module.__dict__)

    current_build = module.model.build_antithetic_state
    original_build = getattr(current_build, "_fp32_original", current_build)

    def build_fp64(*args, **kwargs):
        state, metadata = original_build(*args, **kwargs)
        state64 = module.model.State(
            state.a.to(dtype=torch.float64),
            state.W.to(dtype=torch.float64),
            state.u.to(dtype=torch.float64),
        )
        if {state64.a.dtype, state64.W.dtype, state64.u.dtype} != {torch.float64}:
            raise RuntimeError("state cast to FP64 failed")
        metadata = dict(metadata)
        metadata.update(
            dynamics_dtype="float64",
            initialization_bytes="frozen-fp32-cast-exactly-to-fp64",
        )
        return state64, metadata

    build_fp64._fp32_original = original_build  # type: ignore[attr-defined]
    module.model.build_antithetic_state = build_fp64
    return module


def symmetric_relative(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    denominator = 0.5 * (np.abs(a) + np.abs(b))
    return np.divide(
        np.abs(a - b),
        denominator,
        out=np.zeros_like(denominator, dtype=np.float64),
        where=denominator != 0.0,
    )


def primitive_clock(arrays: dict[str, np.ndarray], nodes: np.ndarray) -> dict[str, np.ndarray]:
    output = np.asarray(arrays["raw_output"], dtype=np.float64).mean(axis=1)
    if not np.all(np.isfinite(output)) or not np.all(np.diff(output) > 0.0):
        raise RuntimeError("ensemble mean output is not finite and strictly increasing")
    if output[0] > nodes[0] or output[-1] < nodes[-1]:
        raise RuntimeError("trajectory does not cover every frozen output node")

    def mean_at(field: str) -> np.ndarray:
        primitive = np.asarray(arrays[field], dtype=np.float64).mean(axis=1)
        if not np.all(np.isfinite(primitive)):
            raise RuntimeError(f"nonfinite primitive {field}")
        return np.interp(nodes, output, primitive)

    weighted = mean_at("raw_weighted_kernel")
    result = {
        "node_time": np.interp(nodes, output, np.asarray(arrays["time"], dtype=np.float64)),
        "mean_output": nodes.copy(),
        "weighted_kernel_numerator": weighted,
        "Keff": weighted / (1.0 - nodes),
        "Kdir": mean_at("raw_kernel"),
        "Ka": mean_at("raw_kernel_a"),
        "KW": mean_at("raw_kernel_W"),
        "Ku": mean_at("raw_kernel_u"),
        "mean_loss": mean_at("raw_loss"),
        "loss_of_mean_output": (1.0 - nodes) ** 2,
        "Q1": mean_at("raw_q1"),
        "Q2": mean_at("raw_q2"),
    }
    if np.any(result["Keff"] <= 0.0) or np.any(result["Kdir"] <= 0.0):
        raise RuntimeError("nonpositive interpolated kernel")
    return result


def initialization_gate(
    diagnostics: dict[str, Any], frozen: dict[str, Any], group_contract: dict[str, Any]
) -> bool:
    init = diagnostics["initialization"]
    common = frozen["expected_common_initialization"]
    prefix_digests = {
        str(key): value for key, value in init.get("base_prefix_sha256", {}).items()
    }
    return bool(
        init.get("base_state_sha256") == common["base_state_sha256"]
        and prefix_digests == common["base_prefix_sha256"]
        and init.get("physical_state_sha256") == group_contract["expected_physical_state_sha256"]
        and diagnostics.get("monitor_sha256") == group_contract["expected_monitor_sha256"]
        and init.get("dynamics_dtype") == "float64"
        and init.get("initialization_bytes") == "frozen-fp32-cast-exactly-to-fp64"
    )


def decide(
    fine_diagnostics: dict[str, Any],
    differences: dict[str, np.ndarray],
    frozen: dict[str, Any],
    group_contract: dict[str, Any],
    initialization_ok: bool,
    pair_elapsed: float,
    pair_gpu_seconds: float,
    component_sum_relative: float,
    complete_finite_positive: bool,
    point_resource_caps: bool,
) -> dict[str, bool]:
    t = frozen["thresholds"]
    gates = {
        "initialization_and_monitor": initialization_ok,
        "pair_wall_cap": pair_elapsed <= float(frozen["pair_wall_seconds"]),
        "pair_gpu_second_cap": pair_gpu_seconds <= float(frozen["pair_wall_seconds"]),
        "point_resource_caps": point_resource_caps,
        "deterministic_fp64_mode": bool(
            torch.are_deterministic_algorithms_enabled()
            and not torch.backends.cuda.matmul.allow_tf32
            and not torch.backends.cudnn.allow_tf32
            and os.environ.get("CUBLAS_WORKSPACE_CONFIG") == ":4096:8"
        ),
        "complete_finite_positive": complete_finite_positive,
        "kernel_component_sum": component_sum_relative
        <= t["kernel_component_sum_relative_ceiling"],
        "mean_output_monotone": fine_diagnostics["minimum_mean_output_increment"] >= t["mean_output_increment_floor"],
        "mean_loss_monotone": fine_diagnostics["maximum_mean_loss_increment"] <= t["mean_loss_increment_ceiling"],
        "a_cosine": fine_diagnostics["minimum_a_cosine_through_y_0_95"] >= t["a_cosine_floor"],
        "u_cosine": fine_diagnostics["minimum_u_cosine_through_y_0_95"] >= t["u_cosine_floor"],
        "w_cosine": fine_diagnostics["minimum_w_cosine_through_y_0_95"] >= t["w_cosine_floor"],
        "a_ratio": t["a_ratio_interval"][0] <= fine_diagnostics["minimum_a_ratio_through_y_0_95"] and fine_diagnostics["maximum_a_ratio_through_y_0_95"] <= t["a_ratio_interval"][1],
        "u_ratio": t["u_ratio_interval"][0] <= fine_diagnostics["minimum_u_ratio_through_y_0_95"] and fine_diagnostics["maximum_u_ratio_through_y_0_95"] <= t["u_ratio_interval"][1],
        "w_ratio": t["w_ratio_interval"][0] <= fine_diagnostics["minimum_w_ratio_through_y_0_95"] and fine_diagnostics["maximum_w_ratio_through_y_0_95"] <= t["w_ratio_interval"][1],
        "driver_max": fine_diagnostics["driver_max_relative_defect_through_y_0_95"] <= t["driver_max_ceiling"],
        "driver_rms": fine_diagnostics["driver_rms_relative_defect_through_y_0_95"] <= t["driver_rms_ceiling"],
        "driver_cumulative": fine_diagnostics["driver_cumulative_relative_defect_through_y_0_95"] <= t["driver_cumulative_ceiling"],
        "coarse_fine_keff": float(np.max(differences["Keff"])) <= t["coarse_fine_keff_ceiling"],
    }
    gates["coarse_fine_q2"] = (
        float(np.max(differences["Q2"])) <= t["coarse_fine_q2_ceiling"]
        if group_contract["q2_gate"]
        else True
    )
    return gates


def reserve_canonical_attempt(
    repo: Path,
    frozen: dict[str, Any],
    group: str,
    device: str,
    provenance: dict[str, str],
) -> tuple[Path, Path, dict[str, Any]]:
    run_root = (repo / frozen["run_root"]).resolve()
    expected_root = (
        repo
        / "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign"
        / "breadth_panel/fp64_successor/runs/local_v1"
    ).resolve()
    if run_root != expected_root:
        raise RuntimeError("frozen run root is not the canonical successor path")
    run_root.mkdir(parents=True, exist_ok=True)
    ledger_path = run_root / "ATTEMPTS.json"
    lock_path = run_root / ".attempts.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        if (repo / STAGE_RESULT_RELATIVE).exists():
            raise RuntimeError("the local stage already has a terminal adjudication")
        if ledger_path.exists():
            ledger = read_json(ledger_path)
        else:
            ledger = {
                "schema": "breadth-fp64-local-attempt-ledger-v1",
                "max_attempts_per_group": 1,
                "stage_gpu_seconds_ceiling": frozen["stage_gpu_seconds"],
                "provenance": provenance,
                "attempts": {},
            }
        if ledger.get("schema") != "breadth-fp64-local-attempt-ledger-v1":
            raise RuntimeError("wrong shared attempt-ledger schema")
        if ledger.get("max_attempts_per_group") != 1:
            raise RuntimeError("shared attempt ledger changed the attempt ceiling")
        if float(ledger.get("stage_gpu_seconds_ceiling", -1.0)) != float(
            frozen["stage_gpu_seconds"]
        ):
            raise RuntimeError("shared attempt ledger changed the stage budget")
        if ledger.get("provenance") != provenance:
            raise RuntimeError("shared attempt ledger belongs to a different frozen bundle")
        attempts = ledger.get("attempts")
        if not isinstance(attempts, dict):
            raise RuntimeError("corrupt shared attempt ledger")
        order = list(frozen["group_order"])
        if list(attempts.keys()) != order[: len(attempts)]:
            raise RuntimeError("shared attempt ledger violates the frozen serial order")
        if group in attempts:
            raise RuntimeError(f"the sole durable attempt for group {group} is already consumed")
        expected_group = order[len(attempts)] if len(attempts) < len(order) else None
        if group != expected_group:
            raise RuntimeError(f"fixed serial order requires {expected_group}, not {group}")
        for predecessor in order[: len(attempts)]:
            record = attempts.get(predecessor, {})
            if record.get("status") != "complete" or not record.get(
                "all_local_gates_pass", False
            ):
                raise RuntimeError(
                    f"predecessor {predecessor} did not complete with every local gate"
                )
        if ledger.get("stage_budget_pass") is False:
            raise RuntimeError("stage GPU-second budget was already exhausted")
        consumed = sum(
            float(record.get("gpu_seconds", 0.0)) for record in attempts.values()
        )
        remaining = float(frozen["stage_gpu_seconds"]) - consumed
        safety = float(
            frozen["external_watchdogs"]["remaining_stage_safety_seconds"]
        )
        watchdog_timeout = min(
            float(frozen["external_watchdogs"]["group_pair_seconds"]),
            remaining - safety,
        )
        if watchdog_timeout <= 0.0:
            raise RuntimeError("no safely watchdog-bounded stage budget remains")
        output = run_root / group
        output.mkdir(parents=False, exist_ok=False)
        attempt = {
            "group": group,
            "status": "reserved",
            "device": device,
            "reserved_utc": utc_now(),
            "stage_gpu_seconds_before": consumed,
            "watchdog_timeout_seconds": watchdog_timeout,
            **provenance,
        }
        attempts[group] = attempt
        write_json_atomic(ledger_path, ledger)
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
    return output, ledger_path, attempt


def claim_canonical_attempt(
    repo: Path,
    frozen: dict[str, Any],
    group: str,
    device: str,
    provenance: dict[str, str],
) -> tuple[Path, Path, dict[str, Any]]:
    run_root = (repo / frozen["run_root"]).resolve()
    ledger_path = run_root / "ATTEMPTS.json"
    lock_path = run_root / ".attempts.lock"
    output = run_root / group
    attempt_path = output / "ATTEMPT.json"
    with lock_path.open("a+", encoding="utf-8") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        if (repo / STAGE_RESULT_RELATIVE).exists():
            raise RuntimeError("the local stage already has a terminal adjudication")
        ledger = read_json(ledger_path)
        if ledger.get("provenance") != provenance:
            raise RuntimeError("reserved attempt belongs to a different frozen bundle")
        record = ledger.get("attempts", {}).get(group, {})
        if (
            record.get("status") != "reserved"
            or record.get("device") != device
            or any(record.get(key) != value for key, value in provenance.items())
        ):
            raise RuntimeError("canonical watchdog reservation is absent or invalid")
        expected_watchdog = (
            f"group:{group}:{format_seconds(record['watchdog_timeout_seconds'])}"
        )
        if os.environ.get("FP64_WATCHDOG_ACTIVE") != expected_watchdog:
            raise RuntimeError("scientific execution is outside its reserved watchdog")
        attempt = read_json(attempt_path)
        if attempt.get("status") != "reserved" or any(
            attempt.get(key) != value for key, value in provenance.items()
        ):
            raise RuntimeError("durable attempt file differs from its reservation")
        started = utc_now()
        attempt.update(status="running", started_utc=started)
        record.update(status="running", started_utc=started)
        write_json_atomic(attempt_path, attempt)
        write_json_atomic(ledger_path, ledger)
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
    return output, ledger_path, attempt


def finish_canonical_attempt(
    ledger_path: Path, group: str, updates: dict[str, Any]
) -> None:
    lock_path = ledger_path.parent / ".attempts.lock"
    with lock_path.open("a+", encoding="utf-8") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        ledger = read_json(ledger_path)
        attempt = ledger["attempts"][group]
        if attempt.get("status") != "running":
            raise RuntimeError("canonical attempt is not in running state")
        attempt.update(updates)
        consumed_gpu_seconds = sum(
            float(record.get("gpu_seconds", 0.0))
            for record in ledger["attempts"].values()
        )
        ledger["consumed_gpu_seconds"] = consumed_gpu_seconds
        ledger["stage_budget_pass"] = consumed_gpu_seconds <= float(
            ledger["stage_gpu_seconds_ceiling"]
        )
        write_json_atomic(ledger_path, ledger)
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)


def run(args: argparse.Namespace) -> dict[str, Any]:
    repo = args.repo.resolve()
    frozen = read_json(args.config)
    if frozen.get("schema") != "breadth-fp64-local-qualification-v1":
        raise RuntimeError("wrong frozen qualification schema")
    group_contract = frozen["groups"][args.group]
    provenance = verify_lock(
        repo,
        args.config,
        args.lock,
        args.unlock,
        args.group,
        args.device,
    )

    output, ledger_path, attempt = claim_canonical_attempt(
        repo, frozen, args.group, args.device, provenance
    )
    attempt_path = output / "ATTEMPT.json"
    expected_watchdog = (
        f"group:{args.group}:{format_seconds(attempt['watchdog_timeout_seconds'])}"
    )

    started = time.monotonic()
    try:
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        torch.set_float32_matmul_precision("highest")
        device = torch.device(args.device)
        if device.type != "cuda" or not torch.cuda.is_available():
            raise RuntimeError("a CUDA device is required")

        panel = repo / "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/breadth_panel"
        parent_points_path = panel / "FROZEN_ONE_INPUT_POINTS.json"
        parent = read_json(parent_points_path)
        points = {point["key"]: point for point in parent["points"]}
        runner = load_fp64_runner(repo, frozen)
        records: dict[str, dict[str, Any]] = {}
        for role, point_key in (
            ("coarse", group_contract["coarse_point"]),
            ("fine", group_contract["fine_point"]),
        ):
            point = copy.deepcopy(points[point_key])
            if int(point["width"]) != int(frozen["width"]):
                raise RuntimeError("parent point width differs from frozen FP64 width")
            point["caps"]["wall_seconds"] = frozen["point_caps"]["wall_seconds"]
            point["caps"]["gpu_memory_gib"] = frozen["point_caps"]["gpu_memory_gib"]
            point["caps"]["host_rss_gib"] = frozen["point_caps"]["host_rss_gib"]
            arrays, outer = runner.run_point(point, seed=int(frozen["seed"]), device=device)
            arrays["array_schema_version"] = np.asarray(
                b"breadth-one-input-fp64-cast-arrays-v1", dtype="S48"
            )
            arrays["dynamics_dtype"] = np.asarray(b"float64", dtype="S16")
            arrays["initialization_contract"] = np.asarray(
                b"frozen-fp32-cast-exactly-to-fp64", dtype="S48"
            )
            raw_path = output / f"{role}_arrays.npz"
            np.savez_compressed(raw_path, **arrays)
            records[role] = {
                "arrays": arrays,
                "outer": outer,
                "point": point,
                "raw_path": raw_path,
                "raw_sha256": sha256_file(raw_path),
            }

        nodes = np.asarray(frozen["nodes"], dtype=np.float64)
        clocks = {role: primitive_clock(records[role]["arrays"], nodes) for role in records}
        differences = {
            name: symmetric_relative(clocks["coarse"][name], clocks["fine"][name])
            for name in ("Keff", "Kdir", "Ka", "KW", "Ku", "mean_loss", "Q1", "Q2")
        }
        coarse_diag = records["coarse"]["outer"]["lineages"][0]
        fine_diag = records["fine"]["outer"]["lineages"][0]
        initialization_ok = (
            initialization_gate(coarse_diag, frozen, group_contract)
            and initialization_gate(fine_diag, frozen, group_contract)
            and coarse_diag["initialization"] == fine_diag["initialization"]
        )
        elapsed = time.monotonic() - started
        pair_gpu_seconds = sum(
            float(records[role]["outer"]["elapsed_seconds"]) for role in records
        )
        component_sum_relative = max(
            float(
                np.max(
                    np.abs(
                        clocks[role]["Kdir"]
                        - clocks[role]["Ka"]
                        - clocks[role]["KW"]
                        - clocks[role]["Ku"]
                    )
                    / np.maximum(np.abs(clocks[role]["Kdir"]), 1e-300)
                )
            )
            for role in records
        )
        positive_fields = ("raw_kernel", "raw_kernel_a", "raw_kernel_W", "raw_kernel_u", "raw_q1", "raw_q2")
        complete_finite_positive = all(
            all(
                np.issubdtype(value.dtype, np.floating)
                and value.dtype == np.float64
                and bool(np.all(np.isfinite(value)))
                for value in records[role]["arrays"].values()
                if np.issubdtype(value.dtype, np.floating)
            )
            and all(bool(np.all(records[role]["arrays"][name] > 0.0)) for name in positive_fields)
            for role in records
        )
        point_resource_caps = all(
            float(records[role]["outer"]["elapsed_seconds"])
            <= float(frozen["point_caps"]["wall_seconds"])
            and float(records[role]["outer"]["max_gpu_allocated_gib"])
            <= float(frozen["point_caps"]["gpu_memory_gib"])
            and float(records[role]["outer"]["max_host_rss_gib"])
            <= float(frozen["point_caps"]["host_rss_gib"])
            for role in records
        )
        gates = decide(
            fine_diag,
            differences,
            frozen,
            group_contract,
            initialization_ok,
            elapsed,
            pair_gpu_seconds,
            component_sum_relative,
            complete_finite_positive,
            point_resource_caps,
        )
        result = {
            "schema": "breadth-fp64-local-result-v1",
            "status": "complete",
            "claim_scope": "local-fixed-step-fp64-euler-qualification-only",
            "group": args.group,
            "configuration": group_contract["configuration"],
            "width": frozen["width"],
            "nodes": frozen["nodes"],
            "initialization_contract": frozen["initialization_contract"],
            "steps": {role: records[role]["point"]["step"] for role in records},
            "point_keys": {role: records[role]["point"]["key"] for role in records},
            "device": args.device,
            "gpu_name": torch.cuda.get_device_name(device),
            "gpu_identity": cuda_identity(args.device),
            "torch_version": torch.__version__,
            "cuda_version": torch.version.cuda,
            "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
            "external_watchdog": expected_watchdog,
            "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
            "tf32_matmul": bool(torch.backends.cuda.matmul.allow_tf32),
            "tf32_cudnn": bool(torch.backends.cudnn.allow_tf32),
            "started_utc": attempt["started_utc"],
            "ended_utc": utc_now(),
            "elapsed_seconds": elapsed,
            "gpu_seconds": pair_gpu_seconds,
            "kernel_component_sum_max_relative": component_sum_relative,
            "provenance": {
                **provenance,
                "config_sha256": sha256_file(args.config),
                "parent_points_sha256": sha256_file(parent_points_path),
                "raw_sha256": {role: records[role]["raw_sha256"] for role in records},
                "command": sys.argv,
            },
            "clock_values": {
                role: {name: value.tolist() for name, value in clocks[role].items()}
                for role in clocks
            },
            "coarse_fine": {
                name: {
                    "nodewise_symmetric_relative": value.tolist(),
                    "maximum_symmetric_relative": float(np.max(value)),
                }
                for name, value in differences.items()
            },
            "coarse_diagnostics": coarse_diag,
            "fine_diagnostics": fine_diag,
            "outer_resources": {
                role: {
                    "elapsed_seconds": records[role]["outer"]["elapsed_seconds"],
                    "max_gpu_allocated_gib": records[role]["outer"]["max_gpu_allocated_gib"],
                    "max_host_rss_gib": records[role]["outer"]["max_host_rss_gib"],
                }
                for role in records
            },
            "gates": gates,
            "all_local_gates_pass": all(gates.values()),
            "branch_eligible": False,
            "branch_note": (
                "Only the independent all-A/M/V stage adjudicator can mark "
                "the next branch eligible."
            ),
        }
        result_path = output / "RESULT.json"
        write_json(result_path, result)
        attempt.update(
            status="complete",
            ended_utc=result["ended_utc"],
            result_sha256=sha256_file(result_path),
            all_local_gates_pass=result["all_local_gates_pass"],
            gpu_seconds=pair_gpu_seconds,
        )
        write_json(attempt_path, attempt)
        finish_canonical_attempt(
            ledger_path,
            args.group,
            {
                "status": "complete",
                "ended_utc": result["ended_utc"],
                "result_sha256": attempt["result_sha256"],
                "attempt_sha256": sha256_file(attempt_path),
                "all_local_gates_pass": result["all_local_gates_pass"],
                "gpu_seconds": pair_gpu_seconds,
            },
        )
        return result
    except BaseException as exc:
        consumed = time.monotonic() - started
        attempt.update(
            status="failed",
            ended_utc=utc_now(),
            error_type=type(exc).__name__,
            error=str(exc),
            traceback=traceback.format_exc(),
            gpu_seconds=consumed,
        )
        write_json(attempt_path, attempt)
        finish_canonical_attempt(
            ledger_path,
            args.group,
            {
                "status": "failed",
                "ended_utc": attempt["ended_utc"],
                "error_type": attempt["error_type"],
                "error": attempt["error"],
                "attempt_sha256": sha256_file(attempt_path),
                "gpu_seconds": consumed,
            },
        )
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--unlock", type=Path, required=True)
    parser.add_argument("--group", choices=("A", "M", "V"), required=True)
    parser.add_argument("--device", required=True)
    args = parser.parse_args()
    result = run(args)
    print(
        json.dumps(
            {
                "group": result["group"],
                "all_local_gates_pass": result["all_local_gates_pass"],
                "coarse_fine_keff": result["coarse_fine"]["Keff"]["maximum_symmetric_relative"],
                "w_cosine": result["fine_diagnostics"]["minimum_w_cosine_through_y_0_95"],
                "driver_max": result["fine_diagnostics"]["driver_max_relative_defect_through_y_0_95"],
                "elapsed_seconds": result["elapsed_seconds"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
