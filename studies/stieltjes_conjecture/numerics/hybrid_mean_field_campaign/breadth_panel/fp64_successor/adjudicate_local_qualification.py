#!/usr/bin/env python3
"""Independent read-back adjudicator for the FP64 A/M/V local stage."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import struct
from typing import Any

import numpy as np


SUCCESSOR_RELATIVE = Path(
    "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
    "breadth_panel/fp64_successor"
)
CONFIG_RELATIVE = SUCCESSOR_RELATIVE / "FROZEN_LOCAL_QUALIFICATION.json"
LOCK_RELATIVE = SUCCESSOR_RELATIVE / "FROZEN_LOCAL_QUALIFICATION_LOCK.json"
UNLOCK_RELATIVE = SUCCESSOR_RELATIVE / "LOCAL_QUALIFICATION_UNLOCK.json"
PREFLIGHT_RELATIVE = SUCCESSOR_RELATIVE / "GPU_PREFLIGHT.json"
RESULT_RELATIVE = SUCCESSOR_RELATIVE / "LOCAL_QUALIFICATION_RESULT.json"
PARENT_POINTS_RELATIVE = Path(
    "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
    "breadth_panel/FROZEN_ONE_INPUT_POINTS.json"
)
REQUIRED_LOCKED_FILES = frozenset(
    {
        str(SUCCESSOR_RELATIVE / "PROTOCOL.md"),
        str(CONFIG_RELATIVE),
        str(SUCCESSOR_RELATIVE / "run_local_qualification.py"),
        str(SUCCESSOR_RELATIVE / "adjudicate_local_qualification.py"),
        str(SUCCESSOR_RELATIVE / "gpu_preflight.py"),
        str(SUCCESSOR_RELATIVE / "watchdog_launcher.py"),
        str(SUCCESSOR_RELATIVE / "tests/test_fp64_local.py"),
        str(PARENT_POINTS_RELATIVE),
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
OBSERVABLE_FIELDS = (
    "output",
    "kernel",
    "kernel_a",
    "kernel_W",
    "kernel_u",
    "weighted_kernel",
    "loss",
    "q1",
    "q2",
)
UPDATE_FIELDS = (
    "a_unchanged_fraction",
    "u_unchanged_fraction",
    "w_unchanged_fraction",
    "a_ratio",
    "u_ratio",
    "w_ratio",
    "a_cosine",
    "u_cosine",
    "w_cosine",
)
VALIDITY_GATES = frozenset(
    {
        "initialization_and_monitor",
        "pair_wall_cap",
        "pair_gpu_second_cap",
        "point_resource_caps",
        "deterministic_fp64_mode",
        "complete_finite_positive",
        "kernel_component_sum",
    }
)


class LiveAttemptError(RuntimeError):
    """Raised when adjudication is requested while a watchdog is still live."""


class StageStillOpen(RuntimeError):
    """Raised for a passing prefix that still has an authorized next group."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_bundle_sha256(files: dict[str, str]) -> str:
    payload = "\n".join(
        f"{name} {digest}" for name, digest in sorted(files.items())
    ).encode()
    return sha256_bytes(payload)


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} is not a JSON object")
    return value


def write_json_exclusive(path: Path, value: dict[str, Any]) -> None:
    payload = json.dumps(value, indent=2, sort_keys=True) + "\n"
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        temporary.unlink(missing_ok=True)


def verify_bundle(
    repo: Path,
    config_path: Path,
    lock_path: Path,
    unlock_path: Path,
) -> tuple[dict[str, str], dict[str, Any], dict[str, Any]]:
    canonical = {
        "config": (repo / CONFIG_RELATIVE).resolve(),
        "lock": (repo / LOCK_RELATIVE).resolve(),
        "unlock": (repo / UNLOCK_RELATIVE).resolve(),
    }
    if config_path.resolve() != canonical["config"]:
        raise RuntimeError("configuration is not the canonical successor file")
    if lock_path.resolve() != canonical["lock"]:
        raise RuntimeError("source lock is not the canonical successor file")
    if unlock_path.resolve() != canonical["unlock"]:
        raise RuntimeError("unlock is not the canonical successor file")

    frozen = read_json(config_path)
    if frozen.get("schema") != "breadth-fp64-local-qualification-v1":
        raise RuntimeError("wrong frozen configuration schema")
    lock = read_json(lock_path)
    if lock.get("schema") != "breadth-fp64-local-lock-v1" or lock.get("status") != "frozen":
        raise RuntimeError("invalid source lock")
    files = lock.get("files", {})
    if set(files) != REQUIRED_LOCKED_FILES:
        raise RuntimeError("source lock does not contain the canonical dependency set")
    bundle_sha = source_bundle_sha256(files)
    if lock.get("bundle_sha256") != bundle_sha:
        raise RuntimeError("source-lock bundle digest is invalid")
    for relative, expected in files.items():
        if sha256_file(repo / relative) != expected:
            raise RuntimeError(f"source-lock mismatch for {relative}")

    lock_sha = sha256_file(lock_path)
    config_sha = sha256_file(config_path)
    unlock = read_json(unlock_path)
    if unlock.get("schema") != "breadth-fp64-local-unlock-v1":
        raise RuntimeError("wrong unlock schema")
    if unlock.get("status") != "authorized" or unlock.get("lock_sha256") != lock_sha:
        raise RuntimeError("unlock does not authorize the locked bundle")
    if unlock.get("config_sha256") != config_sha:
        raise RuntimeError("unlock does not bind the frozen configuration")
    if unlock.get("authorized_groups") != ["A", "M", "V"]:
        raise RuntimeError("unlock does not authorize the exact frozen sequence")
    if unlock.get("authorized_devices") != ["cuda:0"]:
        raise RuntimeError("this stage must use its one preflighted CUDA device")
    if unlock.get("max_attempts_per_group") != 1:
        raise RuntimeError("unlock changed the exactly-once rule")

    preflight_contract = unlock.get("gpu_preflight", {})
    preflight_path = (repo / preflight_contract.get("path", "")).resolve()
    if preflight_path != (repo / PREFLIGHT_RELATIVE).resolve():
        raise RuntimeError("unlock names a noncanonical GPU preflight")
    preflight_sha = sha256_file(preflight_path)
    if preflight_contract.get("sha256") != preflight_sha:
        raise RuntimeError("GPU preflight digest differs from the unlock")
    preflight = read_json(preflight_path)
    preflight_attempt_path = (repo / preflight_contract.get("attempt_path", "")).resolve()
    if preflight_attempt_path != (repo / SUCCESSOR_RELATIVE / "GPU_PREFLIGHT_ATTEMPT.json").resolve():
        raise RuntimeError("unlock names a noncanonical GPU preflight attempt")
    preflight_attempt_sha = sha256_file(preflight_attempt_path)
    if preflight_contract.get("attempt_sha256") != preflight_attempt_sha:
        raise RuntimeError("GPU preflight-attempt digest differs from the unlock")
    preflight_attempt = read_json(preflight_attempt_path)
    preflight_watchdog_path = (repo / preflight_contract.get("watchdog_path", "")).resolve()
    if preflight_watchdog_path != (repo / SUCCESSOR_RELATIVE / "watchdog_records/preflight.json").resolve():
        raise RuntimeError("unlock names a noncanonical preflight watchdog")
    preflight_watchdog_sha = sha256_file(preflight_watchdog_path)
    if preflight_contract.get("watchdog_sha256") != preflight_watchdog_sha:
        raise RuntimeError("preflight-watchdog digest differs from the unlock")
    preflight_watchdog = read_json(preflight_watchdog_path)
    required_preflight = bool(
        preflight.get("schema") == "breadth-fp64-gpu-preflight-v1"
        and preflight.get("status") == "pass"
        and preflight.get("device") == "cuda:0"
        and preflight.get("lock_sha256") == lock_sha
        and preflight.get("config_sha256") == config_sha
        and preflight.get("deterministic_replay") is True
        and preflight.get("float64_arrays") is True
        and preflight.get("initialization_ok") is True
        and preflight.get("resource_caps_pass") is True
        and preflight.get("dynamics_dtype") == "float64"
        and preflight.get("initialization_contract")
        == "frozen-fp32-cast-exactly-to-fp64"
        and preflight.get("deterministic_algorithms") is True
        and preflight.get("tf32_matmul") is False
        and preflight.get("tf32_cudnn") is False
        and preflight.get("cublas_workspace_config") == ":4096:8"
        and preflight.get("external_watchdog")
        == f"preflight:preflight:{int(frozen['external_watchdogs']['gpu_preflight_seconds'])}"
        and preflight_attempt.get("status") == "pass"
        and preflight_attempt.get("result_sha256") == preflight_sha
        and preflight_attempt.get("lock_sha256") == lock_sha
        and preflight_attempt.get("config_sha256") == config_sha
        and preflight_watchdog.get("status") == "completed"
        and preflight_watchdog.get("mode") == "preflight"
        and preflight_watchdog.get("device") == "cuda:0"
        and preflight_watchdog.get("returncode") == 0
        and preflight_watchdog.get("timeout_seconds")
        == int(frozen["external_watchdogs"]["gpu_preflight_seconds"])
        and preflight_watchdog.get("result_sha256") == preflight_sha
        and preflight_watchdog.get("attempt_sha256") == preflight_attempt_sha
    )
    if not required_preflight:
        raise RuntimeError("GPU preflight did not satisfy the frozen contract")
    provenance = {
        "lock_sha256": lock_sha,
        "unlock_sha256": sha256_file(unlock_path),
        "config_sha256": config_sha,
        "preflight_sha256": preflight_sha,
        "preflight_attempt_sha256": preflight_attempt_sha,
        "preflight_watchdog_sha256": preflight_watchdog_sha,
        "source_bundle_sha256": bundle_sha,
    }
    return provenance, frozen, preflight


def decode_scalar(array: np.ndarray) -> str:
    value = array.item()
    return value.decode("utf-8") if isinstance(value, bytes) else str(value)


def monitor_digest(arrays: dict[str, np.ndarray], point: dict[str, Any]) -> str:
    pairs = np.column_stack((arrays["w_monitor_rows"], arrays["w_monitor_cols"]))
    payload = np.asarray(pairs, dtype="<i8", order="C").tobytes(order="C")
    header = struct.pack(
        "<QQQ",
        int(point["w_monitor_seed"]),
        int(point["w_monitor_extent"]),
        int(point["w_monitor_size"]),
    )
    return hashlib.sha256(b"euler-fp32-W-monitor-v1\0" + header + payload).hexdigest()


def load_raw(
    path: Path,
    point: dict[str, Any],
) -> dict[str, np.ndarray]:
    expected = {
        "time",
        "lineage_ids",
        "column_lineage_id",
        "antithetic_sign",
        "array_schema_version",
        "dynamics_dtype",
        "initialization_contract",
        "checkpoint_steps",
        "w_recurrence_relative_error",
        "w_monitor_rows",
        "w_monitor_cols",
        *(f"raw_{field}" for field in OBSERVABLE_FIELDS),
        *(f"proxy_{field}" for field in OBSERVABLE_FIELDS),
        *(f"update_{field}" for field in UPDATE_FIELDS),
    }
    with np.load(path, allow_pickle=False) as archive:
        if set(archive.files) != expected:
            raise RuntimeError(f"raw array schema differs in {path}")
        arrays = {name: np.asarray(archive[name]) for name in archive.files}
    if decode_scalar(arrays["array_schema_version"]) != "breadth-one-input-fp64-cast-arrays-v1":
        raise RuntimeError(f"wrong raw schema in {path}")
    if decode_scalar(arrays["dynamics_dtype"]) != "float64":
        raise RuntimeError(f"wrong dynamics dtype in {path}")
    if decode_scalar(arrays["initialization_contract"]) != "frozen-fp32-cast-exactly-to-fp64":
        raise RuntimeError(f"wrong initialization contract in {path}")

    step = float(point["step"])
    steps = int(round(float(point["max_time"]) / step))
    start, stop = int(point["lineage_start"]), int(point["lineage_stop"])
    columns = 2 * (stop - start)
    exact_time = np.arange(steps + 1, dtype=np.float64) * step
    if arrays["time"].dtype != np.float64 or not np.array_equal(arrays["time"], exact_time):
        raise RuntimeError(f"wrong exact Euler time grid in {path}")
    if arrays["lineage_ids"].dtype != np.int64 or not np.array_equal(
        arrays["lineage_ids"], np.arange(start, stop, dtype=np.int64)
    ):
        raise RuntimeError(f"wrong lineage IDs in {path}")
    if arrays["column_lineage_id"].dtype != np.int64 or not np.array_equal(
        arrays["column_lineage_id"], np.repeat(np.arange(start, stop, dtype=np.int64), 2)
    ):
        raise RuntimeError(f"wrong column-lineage IDs in {path}")
    if arrays["antithetic_sign"].dtype != np.int8 or not np.array_equal(
        arrays["antithetic_sign"], np.tile(np.asarray((1, -1), dtype=np.int8), stop - start)
    ):
        raise RuntimeError(f"wrong antithetic signs in {path}")
    for prefix in ("raw", "proxy"):
        for field in OBSERVABLE_FIELDS:
            if arrays[f"{prefix}_{field}"].shape != (steps + 1, columns):
                raise RuntimeError(f"wrong {prefix}_{field} shape in {path}")
    for field in UPDATE_FIELDS:
        if arrays[f"update_{field}"].shape != (steps, columns):
            raise RuntimeError(f"wrong update_{field} shape in {path}")
    stride = int(point["diagnostic_stride"])
    expected_checkpoints = list(range(stride, steps + 1, stride))
    if not expected_checkpoints or expected_checkpoints[-1] != steps:
        expected_checkpoints.append(steps)
    if arrays["checkpoint_steps"].dtype != np.int64 or not np.array_equal(
        arrays["checkpoint_steps"], np.asarray(expected_checkpoints, dtype=np.int64)
    ):
        raise RuntimeError(f"wrong checkpoint grid in {path}")
    if arrays["w_recurrence_relative_error"].shape != (len(expected_checkpoints), columns):
        raise RuntimeError(f"wrong W-recurrence shape in {path}")
    monitor_size = int(point["w_monitor_size"])
    rows, cols = arrays["w_monitor_rows"], arrays["w_monitor_cols"]
    if rows.dtype != np.int64 or cols.dtype != np.int64:
        raise RuntimeError(f"wrong monitor index dtype in {path}")
    if rows.shape != (monitor_size,) or cols.shape != (monitor_size,):
        raise RuntimeError(f"wrong monitor size in {path}")
    pairs = list(zip(rows.tolist(), cols.tolist()))
    if pairs != sorted(set(pairs)):
        raise RuntimeError(f"monitor coordinates are not sorted and unique in {path}")
    extent = int(point["w_monitor_extent"])
    if np.any(rows < 0) or np.any(rows >= extent) or np.any(cols < 0) or np.any(cols >= extent):
        raise RuntimeError(f"monitor coordinate outside frozen extent in {path}")

    for name, value in arrays.items():
        if np.issubdtype(value.dtype, np.floating):
            if value.dtype != np.float64 or not bool(np.all(np.isfinite(value))):
                raise RuntimeError(f"nonfinite or non-FP64 scientific array {name} in {path}")
    for prefix in ("raw", "proxy"):
        for field in ("kernel", "kernel_a", "kernel_W", "kernel_u", "q1", "q2"):
            if not bool(np.all(arrays[f"{prefix}_{field}"] > 0.0)):
                raise RuntimeError(f"nonpositive {prefix}_{field} in {path}")
    configuration = str(point["configuration"])
    if configuration in {"centered_c1", "relative_metric_l2"}:
        factors = {field: 1.0 for field in OBSERVABLE_FIELDS}
    elif configuration == "variance_vhalf":
        factors = {
            "output": 2.0,
            "kernel": 2.0,
            "kernel_a": 2.0,
            "kernel_W": 2.0,
            "kernel_u": 2.0,
            "weighted_kernel": 4.0,
            "loss": 4.0,
            "q1": 1.0,
            "q2": 2.0,
        }
    else:
        raise RuntimeError(f"unexpected configuration {configuration}")
    for field, factor in factors.items():
        if not np.array_equal(arrays[f"proxy_{field}"], factor * arrays[f"raw_{field}"]):
            raise RuntimeError(f"proxy-coordinate identity failed for {field} in {path}")
    return arrays


def primitive_clock(arrays: dict[str, np.ndarray], nodes: np.ndarray) -> dict[str, np.ndarray]:
    output = arrays["raw_output"].mean(axis=1)
    if not np.all(np.diff(output) > 0.0) or output[0] > nodes[0] or output[-1] < nodes[-1]:
        raise RuntimeError("raw trajectory does not provide the frozen common output clock")

    def at(field: str) -> np.ndarray:
        return np.interp(nodes, output, arrays[field].mean(axis=1))

    weighted = at("raw_weighted_kernel")
    return {
        "node_time": np.interp(nodes, output, arrays["time"]),
        "mean_output": nodes.copy(),
        "weighted_kernel_numerator": weighted,
        "Keff": weighted / (1.0 - nodes),
        "Kdir": at("raw_kernel"),
        "Ka": at("raw_kernel_a"),
        "KW": at("raw_kernel_W"),
        "Ku": at("raw_kernel_u"),
        "mean_loss": at("raw_loss"),
        "loss_of_mean_output": (1.0 - nodes) ** 2,
        "Q1": at("raw_q1"),
        "Q2": at("raw_q2"),
    }


def symmetric_relative(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    denominator = 0.5 * (np.abs(a) + np.abs(b))
    return np.divide(
        np.abs(a - b),
        denominator,
        out=np.zeros_like(denominator),
        where=denominator != 0.0,
    )


def raw_fine_diagnostics(arrays: dict[str, np.ndarray], step: float) -> dict[str, float]:
    output = arrays["raw_output"].mean(axis=1)
    loss = arrays["raw_loss"].mean(axis=1)
    through = output[:-1] <= 0.95
    if not bool(np.any(through)):
        raise RuntimeError("fine run has no updates through y=.95")
    rhs = arrays["raw_weighted_kernel"][:-1].mean(axis=1)
    defect = np.diff(output) / (2.0 * step) - rhs
    scale = np.maximum(np.abs(rhs[through]), 1e-12)
    values: dict[str, float] = {
        "minimum_mean_output_increment": float(np.min(np.diff(output))),
        "maximum_mean_loss_increment": float(np.max(np.diff(loss))),
        "driver_max": float(np.max(np.abs(defect[through]) / scale)),
        "driver_rms": float(
            np.sqrt(np.mean(defect[through] ** 2))
            / max(np.sqrt(np.mean(rhs[through] ** 2)), 1e-12)
        ),
        "driver_cumulative": float(
            abs(np.sum(2.0 * step * defect[through]))
            / max(abs(np.sum(2.0 * step * rhs[through])), 1e-12)
        ),
    }
    mask = through[:, None]
    for block in ("a", "u", "w"):
        ratio = np.where(mask, arrays[f"update_{block}_ratio"], np.nan)
        cosine = np.where(mask, arrays[f"update_{block}_cosine"], np.nan)
        values[f"{block}_ratio_min"] = float(np.nanmin(ratio))
        values[f"{block}_ratio_max"] = float(np.nanmax(ratio))
        values[f"{block}_cosine_min"] = float(np.nanmin(cosine))
    return values


def expected_initialization(result: dict[str, Any], frozen: dict[str, Any], group: str) -> bool:
    contract = frozen["groups"][group]
    common = frozen["expected_common_initialization"]
    checks = []
    for role in ("coarse_diagnostics", "fine_diagnostics"):
        diagnostics = result[role]
        init = diagnostics["initialization"]
        prefixes = {str(key): value for key, value in init["base_prefix_sha256"].items()}
        checks.append(
            init["base_state_sha256"] == common["base_state_sha256"]
            and prefixes == common["base_prefix_sha256"]
            and init["physical_state_sha256"] == contract["expected_physical_state_sha256"]
            and diagnostics["monitor_sha256"] == contract["expected_monitor_sha256"]
            and init["dynamics_dtype"] == "float64"
            and init["initialization_bytes"] == "frozen-fp32-cast-exactly-to-fp64"
        )
    return all(checks) and result["coarse_diagnostics"]["initialization"] == result["fine_diagnostics"]["initialization"]


def assert_result_arrays(
    result: dict[str, Any],
    clocks: dict[str, dict[str, np.ndarray]],
    differences: dict[str, np.ndarray],
) -> None:
    for role, values in clocks.items():
        for name, expected in values.items():
            actual = np.asarray(result["clock_values"][role][name], dtype=np.float64)
            if not np.array_equal(actual, expected):
                raise RuntimeError(f"stored clock value differs for {role}/{name}")
    for name, expected in differences.items():
        record = result["coarse_fine"][name]
        if not np.array_equal(
            np.asarray(record["nodewise_symmetric_relative"], dtype=np.float64), expected
        ) or float(record["maximum_symmetric_relative"]) != float(np.max(expected)):
            raise RuntimeError(f"stored coarse/fine value differs for {name}")


def point_resource_caps_pass(result: dict[str, Any], frozen: dict[str, Any]) -> bool:
    point_caps = frozen["point_caps"]
    return all(
        float(result["outer_resources"][role]["elapsed_seconds"])
        <= float(point_caps["wall_seconds"])
        and float(result["outer_resources"][role]["max_gpu_allocated_gib"])
        <= float(point_caps["gpu_memory_gib"])
        and float(result["outer_resources"][role]["max_host_rss_gib"])
        <= float(point_caps["host_rss_gib"])
        for role in ("coarse", "fine")
    )


def adjudicate_group(
    repo: Path,
    group_dir: Path,
    group: str,
    frozen: dict[str, Any],
    points: dict[str, dict[str, Any]],
    ledger_record: dict[str, Any],
    provenance: dict[str, str],
    preflight: dict[str, Any],
) -> dict[str, Any]:
    attempt_path = group_dir / "ATTEMPT.json"
    if sha256_file(attempt_path) != ledger_record.get("attempt_sha256"):
        raise RuntimeError(f"ledger/attempt hash mismatch for {group}")
    attempt = read_json(attempt_path)
    if attempt.get("status") != "complete" or any(
        attempt.get(key) != value for key, value in provenance.items()
    ):
        raise RuntimeError(f"attempt provenance differs for {group}")
    result_path = group_dir / "RESULT.json"
    if sha256_file(result_path) != ledger_record.get("result_sha256"):
        raise RuntimeError(f"ledger/result hash mismatch for {group}")
    result = read_json(result_path)
    contract = frozen["groups"][group]
    if (
        result.get("schema") != "breadth-fp64-local-result-v1"
        or result.get("status") != "complete"
        or result.get("group") != group
        or result.get("configuration") != contract["configuration"]
        or result.get("width") != frozen["width"]
        or result.get("nodes") != frozen["nodes"]
        or result.get("initialization_contract") != frozen["initialization_contract"]
        or result.get("device") != "cuda:0"
        or result.get("gpu_identity") != preflight["gpu_identity"]
        or result.get("gpu_name") != preflight["gpu_name"]
        or result.get("torch_version") != preflight["torch_version"]
        or result.get("cuda_version") != preflight["cuda_version"]
        or result.get("branch_eligible") is not False
        or result.get("provenance", {}).get("parent_points_sha256")
        != sha256_file(repo / PARENT_POINTS_RELATIVE)
        or any(result.get("provenance", {}).get(key) != value for key, value in provenance.items())
    ):
        raise RuntimeError(f"result contract or provenance differs for {group}")
    watchdog_path = repo / SUCCESSOR_RELATIVE / "watchdog_records" / f"{group}.json"
    watchdog = read_json(watchdog_path)
    if (
        watchdog.get("schema") != "breadth-fp64-external-watchdog-v1"
        or watchdog.get("status") != "completed"
        or watchdog.get("mode") != "group"
        or watchdog.get("group") != group
        or watchdog.get("device") != "cuda:0"
        or watchdog.get("returncode") != 0
        or watchdog.get("timeout_seconds")
        != float(ledger_record["watchdog_timeout_seconds"])
        or watchdog.get("stage_gpu_seconds_before")
        != float(ledger_record["stage_gpu_seconds_before"])
        or result.get("external_watchdog")
        != f"group:{group}:{format(float(ledger_record['watchdog_timeout_seconds']), '.12g')}"
        or watchdog.get("result_sha256") != sha256_file(result_path)
        or watchdog.get("attempt_sha256") != sha256_file(attempt_path)
    ):
        raise RuntimeError(f"external-watchdog record differs for {group}")
    raw: dict[str, dict[str, np.ndarray]] = {}
    role_points: dict[str, dict[str, Any]] = {}
    for role in ("coarse", "fine"):
        point_key = contract[f"{role}_point"]
        point = points[point_key]
        role_points[role] = point
        if result["point_keys"][role] != point_key or float(result["steps"][role]) != float(point["step"]):
            raise RuntimeError(f"stored point contract differs for {group}/{role}")
        path = group_dir / f"{role}_arrays.npz"
        if sha256_file(path) != result["provenance"]["raw_sha256"][role]:
            raise RuntimeError(f"raw hash mismatch for {group}/{role}")
        raw[role] = load_raw(path, point)
        digest = monitor_digest(raw[role], point)
        if digest != contract["expected_monitor_sha256"]:
            raise RuntimeError(f"raw monitor digest differs for {group}/{role}")

    nodes = np.asarray(frozen["nodes"], dtype=np.float64)
    clocks = {role: primitive_clock(raw[role], nodes) for role in raw}
    difference_names = ("Keff", "Kdir", "Ka", "KW", "Ku", "mean_loss", "Q1", "Q2")
    differences = {
        name: symmetric_relative(clocks["coarse"][name], clocks["fine"][name])
        for name in difference_names
    }
    assert_result_arrays(result, clocks, differences)
    diagnostics = raw_fine_diagnostics(raw["fine"], float(role_points["fine"]["step"]))
    diagnostic_map = {
        "minimum_mean_output_increment": "minimum_mean_output_increment",
        "maximum_mean_loss_increment": "maximum_mean_loss_increment",
        "driver_max": "driver_max_relative_defect_through_y_0_95",
        "driver_rms": "driver_rms_relative_defect_through_y_0_95",
        "driver_cumulative": "driver_cumulative_relative_defect_through_y_0_95",
        "a_ratio_min": "minimum_a_ratio_through_y_0_95",
        "a_ratio_max": "maximum_a_ratio_through_y_0_95",
        "u_ratio_min": "minimum_u_ratio_through_y_0_95",
        "u_ratio_max": "maximum_u_ratio_through_y_0_95",
        "w_ratio_min": "minimum_w_ratio_through_y_0_95",
        "w_ratio_max": "maximum_w_ratio_through_y_0_95",
        "a_cosine_min": "minimum_a_cosine_through_y_0_95",
        "u_cosine_min": "minimum_u_cosine_through_y_0_95",
        "w_cosine_min": "minimum_w_cosine_through_y_0_95",
    }
    for recomputed, stored in diagnostic_map.items():
        if diagnostics[recomputed] != float(result["fine_diagnostics"][stored]):
            raise RuntimeError(f"stored fine diagnostic differs for {group}/{stored}")

    component_sum = max(
        float(
            np.max(
                np.abs(values["Kdir"] - values["Ka"] - values["KW"] - values["Ku"])
                / np.maximum(np.abs(values["Kdir"]), 1e-300)
            )
        )
        for values in clocks.values()
    )
    if component_sum != float(result["kernel_component_sum_max_relative"]):
        raise RuntimeError(f"stored component-sum diagnostic differs for {group}")
    pair_gpu_seconds = sum(
        float(result["outer_resources"][role]["elapsed_seconds"])
        for role in ("coarse", "fine")
    )
    if pair_gpu_seconds != float(result["gpu_seconds"]):
        raise RuntimeError(f"stored GPU seconds differ for {group}")
    point_resource_caps = point_resource_caps_pass(result, frozen)
    thresholds = frozen["thresholds"]
    gates = {
        "initialization_and_monitor": expected_initialization(result, frozen, group),
        "pair_wall_cap": float(result["elapsed_seconds"]) <= frozen["pair_wall_seconds"],
        "pair_gpu_second_cap": pair_gpu_seconds <= frozen["pair_wall_seconds"],
        "point_resource_caps": point_resource_caps,
        "deterministic_fp64_mode": bool(
            result["deterministic_algorithms"]
            and not result["tf32_matmul"]
            and not result["tf32_cudnn"]
            and result["cublas_workspace_config"] == ":4096:8"
        ),
        "complete_finite_positive": True,
        "kernel_component_sum": component_sum
        <= thresholds["kernel_component_sum_relative_ceiling"],
        "mean_output_monotone": diagnostics["minimum_mean_output_increment"]
        >= thresholds["mean_output_increment_floor"],
        "mean_loss_monotone": diagnostics["maximum_mean_loss_increment"]
        <= thresholds["mean_loss_increment_ceiling"],
        "a_cosine": diagnostics["a_cosine_min"] >= thresholds["a_cosine_floor"],
        "u_cosine": diagnostics["u_cosine_min"] >= thresholds["u_cosine_floor"],
        "w_cosine": diagnostics["w_cosine_min"] >= thresholds["w_cosine_floor"],
        "a_ratio": thresholds["a_ratio_interval"][0]
        <= diagnostics["a_ratio_min"]
        <= diagnostics["a_ratio_max"]
        <= thresholds["a_ratio_interval"][1],
        "u_ratio": thresholds["u_ratio_interval"][0]
        <= diagnostics["u_ratio_min"]
        <= diagnostics["u_ratio_max"]
        <= thresholds["u_ratio_interval"][1],
        "w_ratio": thresholds["w_ratio_interval"][0]
        <= diagnostics["w_ratio_min"]
        <= diagnostics["w_ratio_max"]
        <= thresholds["w_ratio_interval"][1],
        "driver_max": diagnostics["driver_max"] <= thresholds["driver_max_ceiling"],
        "driver_rms": diagnostics["driver_rms"] <= thresholds["driver_rms_ceiling"],
        "driver_cumulative": diagnostics["driver_cumulative"]
        <= thresholds["driver_cumulative_ceiling"],
        "coarse_fine_keff": float(np.max(differences["Keff"]))
        <= thresholds["coarse_fine_keff_ceiling"],
        "coarse_fine_q2": (
            float(np.max(differences["Q2"])) <= thresholds["coarse_fine_q2_ceiling"]
            if contract["q2_gate"]
            else True
        ),
    }
    if result.get("gates") != gates or result.get("all_local_gates_pass") != all(gates.values()):
        raise RuntimeError(f"runner/adjudicator gate mismatch for {group}")
    if ledger_record.get("all_local_gates_pass") != all(gates.values()):
        raise RuntimeError(f"ledger/adjudicator decision mismatch for {group}")
    if float(ledger_record.get("gpu_seconds", -1.0)) != pair_gpu_seconds:
        raise RuntimeError(f"ledger GPU seconds differ for {group}")
    return {
        "group": group,
        "gates": gates,
        "all_local_gates_pass": all(gates.values()),
        "coarse_fine_keff": float(np.max(differences["Keff"])),
        "coarse_fine_q2": float(np.max(differences["Q2"])),
        "w_cosine": diagnostics["w_cosine_min"],
        "driver_max": diagnostics["driver_max"],
        "gpu_seconds": pair_gpu_seconds,
        "result_sha256": sha256_file(result_path),
        "raw_sha256": result["provenance"]["raw_sha256"],
        "watchdog_sha256": sha256_file(watchdog_path),
    }


def verify_attempt_record(
    group_dir: Path,
    group: str,
    record: dict[str, Any],
    provenance: dict[str, str],
) -> None:
    if record.get("group") != group or record.get("device") != "cuda:0":
        raise RuntimeError(f"ledger attempt identity differs for {group}")
    if any(record.get(key) != value for key, value in provenance.items()):
        raise RuntimeError(f"ledger attempt provenance differs for {group}")
    attempt_path = group_dir / "ATTEMPT.json"
    status = record.get("status")
    if status in {"complete", "failed"}:
        if sha256_file(attempt_path) != record.get("attempt_sha256"):
            raise RuntimeError(f"ledger/attempt hash mismatch for {group}")
    elif attempt_path.exists():
        attempt = read_json(attempt_path)
        if attempt.get("status") != status or status not in {"reserved", "running"} or any(
            attempt.get(key) != value for key, value in provenance.items()
        ):
            raise RuntimeError(f"open attempt record differs for {group}")


def verify_group_watchdog(
    repo: Path,
    frozen: dict[str, Any],
    group: str,
    record: dict[str, Any],
) -> str:
    path = repo / SUCCESSOR_RELATIVE / "watchdog_records" / f"{group}.json"
    watchdog = read_json(path)
    if (
        watchdog.get("schema") != "breadth-fp64-external-watchdog-v1"
        or watchdog.get("mode") != "group"
        or watchdog.get("group") != group
        or watchdog.get("device") != "cuda:0"
        or watchdog.get("timeout_seconds")
        != float(record["watchdog_timeout_seconds"])
        or watchdog.get("stage_gpu_seconds_before")
        != float(record["stage_gpu_seconds_before"])
    ):
        raise RuntimeError(f"external-watchdog identity differs for {group}")
    if watchdog.get("status") == "running":
        launcher_pid = int(watchdog.get("launcher_pid", -1))
        if launcher_pid <= 0:
            raise RuntimeError(f"group {group} has no valid live-watchdog PID")
        try:
            os.kill(launcher_pid, 0)
        except (ProcessLookupError, ValueError):
            raise RuntimeError(f"group {group} has a stale incomplete watchdog")
        except PermissionError:
            pass
        raise LiveAttemptError(f"group {group} watchdog is still running")
    attempt_path = repo / frozen["run_root"] / group / "ATTEMPT.json"
    if attempt_path.exists() and watchdog.get("attempt_sha256") not in {
        None,
        sha256_file(attempt_path),
    }:
        raise RuntimeError(f"external-watchdog attempt digest differs for {group}")
    status = record.get("status")
    if status == "complete":
        result_path = repo / frozen["run_root"] / group / "RESULT.json"
        valid = bool(
            watchdog.get("status") == "completed"
            and watchdog.get("returncode") == 0
            and watchdog.get("result_sha256") == sha256_file(result_path)
            and watchdog.get("attempt_sha256") == sha256_file(attempt_path)
        )
    elif status == "failed":
        if record.get("error_type") == "ExternalWatchdogTimeout":
            terminal_match = bool(
                watchdog.get("status") == "timed_out"
                and watchdog.get("returncode") == 124
            )
        elif record.get("error_type") == "ExternalLauncherError":
            terminal_match = bool(
                watchdog.get("status") == "launcher_error"
                and watchdog.get("returncode") == 125
            )
        else:
            terminal_match = bool(
                watchdog.get("status") == "child_exit_nonzero"
                and int(watchdog.get("returncode", 0)) != 0
            )
        valid = bool(
            terminal_match
            and watchdog.get("attempt_sha256") == sha256_file(attempt_path)
        )
    elif status in {"reserved", "running"}:
        valid = False
    else:
        valid = False
    if not valid:
        raise RuntimeError(f"external-watchdog terminal status differs for {group}")
    return sha256_file(path)


def classify_validated_prefix(
    order: list[str],
    keys: list[str],
    attempts: dict[str, dict[str, Any]],
    decisions: dict[str, dict[str, Any]],
    readback_errors: dict[str, str],
) -> tuple[str, str, str | None]:
    for group in keys:
        if group in readback_errors:
            return "inconclusive", readback_errors[group], group
        status = attempts[group].get("status")
        if status == "complete":
            decision = decisions.get(group)
            if decision is None:
                return "inconclusive", "missing_independent_group_decision", group
            if not decision["all_local_gates_pass"]:
                failed = sorted(
                    name for name, passed in decision["gates"].items() if not passed
                )
                if set(failed) & VALIDITY_GATES:
                    return (
                        "inconclusive",
                        "validity_or_resource_gate_failed:" + ",".join(failed),
                        group,
                    )
                return (
                    "gate_fail",
                    "one_or_more_original_numerical_gates_failed:"
                    + ",".join(failed),
                    group,
                )
        elif status in {"failed", "reserved", "running"}:
            record = attempts[group]
            reason = (
                f"attempt_{status}:"
                f"{record.get('error_type', 'no_error_type')}:"
                f"{record.get('error', 'no_error_message')}"
            )
            return "inconclusive", reason, group
        else:
            return "inconclusive", f"unknown_attempt_status:{status}", group
    if len(keys) == len(order):
        return "pass", "all_A_M_V_original_local_gates_passed", None
    return "open", "passing_prefix_has_an_unattempted_next_group", order[len(keys)]


def adjudicate_locked_stage(
    repo: Path,
    frozen: dict[str, Any],
    preflight: dict[str, Any],
    provenance: dict[str, str],
    run_root: Path,
    ledger_path: Path,
) -> dict[str, Any]:
    ledger = read_json(ledger_path)
    if (
        ledger.get("schema") != "breadth-fp64-local-attempt-ledger-v1"
        or ledger.get("max_attempts_per_group") != 1
        or float(ledger.get("stage_gpu_seconds_ceiling", -1.0))
        != float(frozen["stage_gpu_seconds"])
        or ledger.get("provenance") != provenance
    ):
        raise RuntimeError("attempt-ledger header differs from the frozen bundle")
    attempts = ledger.get("attempts", {})
    order = frozen["group_order"]
    keys = list(attempts)
    if not keys or keys != order[: len(keys)]:
        raise RuntimeError("ledger is empty or not a valid frozen prefix")

    parent = read_json(repo / PARENT_POINTS_RELATIVE)
    points = {point["key"]: point for point in parent["points"]}
    decisions: dict[str, dict[str, Any]] = {}
    readback_errors: dict[str, str] = {}
    cumulative_before = 0.0
    watchdog_ceiling = float(frozen["external_watchdogs"]["group_pair_seconds"])
    safety = float(
        frozen["external_watchdogs"]["remaining_stage_safety_seconds"]
    )
    for index, group in enumerate(keys):
        record = attempts[group]
        group_dir = run_root / group
        try:
            if index < len(keys) - 1 and (
                record.get("status") != "complete"
                or record.get("all_local_gates_pass") is not True
            ):
                raise RuntimeError(f"attempt exists after terminal predecessor {group}")
            expected_timeout = min(
                watchdog_ceiling,
                float(frozen["stage_gpu_seconds"]) - cumulative_before - safety,
            )
            if (
                float(record.get("stage_gpu_seconds_before", -1.0))
                != cumulative_before
                or float(record.get("watchdog_timeout_seconds", -1.0))
                != expected_timeout
                or expected_timeout <= 0.0
            ):
                raise RuntimeError(f"prospective stage-budget reservation differs for {group}")
            verify_attempt_record(group_dir, group, record, provenance)
            verify_group_watchdog(repo, frozen, group, record)
            if record.get("status") == "complete":
                decision = adjudicate_group(
                    repo,
                    group_dir,
                    group,
                    frozen,
                    points,
                    record,
                    provenance,
                    preflight,
                )
                decisions[group] = decision
                if not decision["all_local_gates_pass"]:
                    break
            elif record.get("status") == "failed":
                break
            else:
                raise RuntimeError(f"nonterminal attempt status {record.get('status')}")
        except LiveAttemptError:
            raise
        except Exception as exc:
            readback_errors[group] = (
                f"readback_validation_failed:{type(exc).__name__}:{exc}"
            )
            break
        cumulative_before += float(record.get("gpu_seconds", 0.0))

    terminal_status, terminal_reason, terminal_group = classify_validated_prefix(
        order, keys, attempts, decisions, readback_errors
    )
    if terminal_status == "open":
        raise StageStillOpen(terminal_reason)
    if terminal_status != "pass" and terminal_group in keys and keys[-1] != terminal_group:
        terminal_status = "inconclusive"
        terminal_reason += ":ledger_contains_attempt_after_terminal_group"

    budget_accounting_complete = all(
        record.get("status") in {"complete", "failed"}
        and "gpu_seconds" in record
        for record in attempts.values()
    )
    recorded_gpu_seconds = sum(
        float(record.get("gpu_seconds", 0.0)) for record in attempts.values()
    )
    stage_budget_pass = bool(
        budget_accounting_complete
        and recorded_gpu_seconds <= float(frozen["stage_gpu_seconds"])
    )
    ledger_budget_valid = bool(
        ("consumed_gpu_seconds" not in ledger or float(ledger["consumed_gpu_seconds"]) == recorded_gpu_seconds)
        and ("stage_budget_pass" not in ledger or bool(ledger["stage_budget_pass"]) == stage_budget_pass)
    )
    if not ledger_budget_valid:
        terminal_status = "inconclusive"
        terminal_reason += ":ledger_budget_accounting_mismatch"
        stage_budget_pass = False
    if terminal_status == "pass" and not stage_budget_pass:
        terminal_status = "inconclusive"
        terminal_reason = "stage_budget_or_accounting_gate_failed"
    groups = [decisions[group] for group in keys if group in decisions]
    all_pass = bool(
        terminal_status == "pass"
        and stage_budget_pass
        and len(groups) == len(order)
    )
    return {
        "schema": "breadth-fp64-local-stage-result-v1",
        "status": terminal_status,
        "reason": terminal_reason,
        "terminal_group": terminal_group,
        "claim_scope": "local-fixed-step-fp64-euler-qualification-only",
        "groups": groups,
        "attempted_prefix": keys,
        "recorded_gpu_seconds": recorded_gpu_seconds,
        "budget_accounting_complete": budget_accounting_complete,
        "stage_gpu_seconds_ceiling": frozen["stage_gpu_seconds"],
        "stage_budget_pass": stage_budget_pass,
        "all_groups_pass": all_pass,
        "next_branch_eligible_for_separate_authorization": all_pass,
        "next_branch_launched": False,
        "provenance": {
            **provenance,
            "ledger_sha256": sha256_file(ledger_path),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--unlock", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    expected_script = (repo / SUCCESSOR_RELATIVE / "adjudicate_local_qualification.py").resolve()
    if Path(__file__).resolve() != expected_script:
        raise RuntimeError("adjudicator is not running from the canonical successor")
    provenance, frozen, preflight = verify_bundle(repo, args.config, args.lock, args.unlock)
    run_root = (repo / frozen["run_root"]).resolve()
    expected_root = (repo / SUCCESSOR_RELATIVE / "runs/local_v1").resolve()
    if run_root != expected_root:
        raise RuntimeError("frozen run root is not canonical")
    ledger_path = run_root / "ATTEMPTS.json"
    stage_lock = run_root / ".attempts.lock"
    output = repo / RESULT_RELATIVE
    with stage_lock.open("a+", encoding="utf-8") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        if output.exists():
            raise RuntimeError("the local stage already has a terminal adjudication")
        result = adjudicate_locked_stage(
            repo,
            frozen,
            preflight,
            provenance,
            run_root,
            ledger_path,
        )
        write_json_exclusive(output, result)
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["all_groups_pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
