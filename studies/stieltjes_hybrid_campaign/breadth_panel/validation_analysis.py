#!/usr/bin/env python3
"""Fail-closed analysis of the frozen one-input Euler validation pairs.

This module performs no simulation.  It verifies the frozen authority chain,
the exactly-once attempt ledger, all six manifests and raw archive hashes, and
then evaluates the preregistered local-method gates on the common physical
output clock.  The raw ``runs/`` directory remains ignored; the compact JSON
and Markdown outputs preserve the scientific result and its provenance.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Iterable

import numpy as np


PANEL_ROOT = Path(__file__).resolve().parent
RUN_ROOT = PANEL_ROOT / "runs" / "validation_one_input_v1"
CONFIG_PATH = PANEL_ROOT / "FROZEN_ONE_INPUT_POINTS.json"
LOCK_PATH = PANEL_ROOT / "FROZEN_ONE_INPUT_LOCK.json"
UNLOCK_PATH = PANEL_ROOT / "ONE_INPUT_VALIDATION_UNLOCK.json"
ATTEMPTS_PATH = RUN_ROOT / "ATTEMPTS.json"
RESULT_PATH = PANEL_ROOT / "VALIDATION_RESULT.json"
REPORT_PATH = PANEL_ROOT / "RESULTS.md"

PHYSICAL_NODES = np.asarray((0.5, 0.75, 0.9, 0.95), dtype=np.float64)
GROUPS = {
    "A": ("A_validation_h2", "A_validation_h1"),
    "M": ("M_validation_h2", "M_validation_h1"),
    "V": ("V_validation_h2", "V_validation_h1"),
}
EXPECTED_CONFIGURATIONS = {
    "A": "centered_c1",
    "M": "relative_metric_l2",
    "V": "variance_vhalf",
}

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

DRIVER_LIMITS = {"max": 0.002, "rms": 0.0005, "cumulative": 0.0005}
COSINE_LIMITS = {"a": 0.999, "u": 0.999, "w": 0.995}
RATIO_LIMITS = {"a": (0.95, 1.05), "u": (0.95, 1.05), "w": (0.80, 1.20)}
LOCAL_DIFFERENCE_CEILING = 0.002


class ValidationError(RuntimeError):
    """Raised when frozen provenance or raw data fail closed."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    _require(isinstance(value, dict), f"{path} is not a JSON object")
    return value


def _parse_utc(value: str, label: str) -> dt.datetime:
    parsed = dt.datetime.fromisoformat(value)
    _require(parsed.tzinfo is not None, f"{label} lacks a UTC offset")
    return parsed.astimezone(dt.timezone.utc)


def _bundle_digest(entries: dict[str, str]) -> str:
    digest = hashlib.sha256()
    for relative, expected in sorted(entries.items()):
        digest.update(relative.encode("utf-8") + b"\0")
        digest.update(expected.encode("ascii") + b"\n")
    return digest.hexdigest()


def _command_value(command: list[str], flag: str) -> str:
    _require(command.count(flag) == 1, f"manifest command does not contain one {flag}")
    index = command.index(flag)
    _require(index + 1 < len(command), f"manifest command truncates {flag}")
    return command[index + 1]


def _ends_with_path(value: str, expected: str) -> bool:
    return Path(value).as_posix().endswith(expected)


def verify_authority() -> dict[str, Any]:
    """Verify the live lock, unlock, point file, and exactly-once ledger."""

    config = load_json(CONFIG_PATH)
    lock = load_json(LOCK_PATH)
    unlock = load_json(UNLOCK_PATH)
    attempts = load_json(ATTEMPTS_PATH)

    _require(lock.get("schema") == "breadth-one-input-source-lock-v1", "wrong lock schema")
    _require(lock.get("status") == "frozen", "source lock is not frozen")
    entries = lock.get("sha256")
    _require(isinstance(entries, dict) and entries, "source lock has no hash table")
    for relative, expected in entries.items():
        _require(isinstance(expected, str) and len(expected) == 64, f"bad digest for {relative}")
        target = PANEL_ROOT / relative
        _require(target.is_file(), f"locked source is missing: {relative}")
        _require(sha256(target) == expected, f"locked source hash mismatch: {relative}")
    _require(_bundle_digest(entries) == lock.get("bundle_sha256"), "source bundle mismatch")

    config_digest = sha256(CONFIG_PATH)
    lock_digest = sha256(LOCK_PATH)
    unlock_digest = sha256(UNLOCK_PATH)
    _require(lock.get("config_sha256") == config_digest, "lock does not bind point file")
    _require(
        entries.get("FROZEN_ONE_INPUT_POINTS.json") == config_digest,
        "locked table does not bind point file",
    )
    _require(
        unlock.get("schema") == "breadth-one-input-validation-unlock-v1",
        "wrong unlock schema",
    )
    _require(unlock.get("status") == "execution-authorized-once", "unlock is inactive")
    _require(unlock.get("lock_sha256") == lock_digest, "unlock does not bind lock")
    _require(unlock.get("config_sha256") == config_digest, "unlock does not bind config")
    _require(
        (PANEL_ROOT / str(unlock.get("output_root"))).resolve() == RUN_ROOT.resolve(),
        "unlock output root differs from frozen run root",
    )

    points = config.get("points")
    _require(isinstance(points, list), "point file has no points list")
    point_map = {str(point.get("key")): point for point in points}
    expected_points = {point for pair in GROUPS.values() for point in pair}
    _require(len(point_map) == len(points), "point keys are not unique")
    _require(set(point_map) == expected_points, "point file differs from six validation points")
    _require(set(unlock.get("allowed_points", {})) == expected_points, "unlock point set differs")
    _require(set(unlock.get("point_groups", {})) == expected_points, "unlock group set differs")
    _require(
        set(unlock.get("external_timeout_seconds", {})) == expected_points,
        "unlock timeout set differs",
    )

    _require(attempts.get("schema") == "breadth-attempt-ledger-v1", "wrong ledger schema")
    ledger = attempts.get("attempts")
    _require(isinstance(ledger, dict), "attempt ledger lacks attempts")
    _require(set(ledger) == expected_points, "attempt ledger is not exactly the six authorized points")
    declared_total = 0.0
    declared_by_group = {group: 0.0 for group in GROUPS}
    for key in sorted(expected_points):
        point = point_map[key]
        attempt = ledger[key]
        expected_group = str(unlock["point_groups"][key])
        expected_device = str(unlock["allowed_points"][key])
        declared = float(point["caps"]["wall_seconds"])
        _require(attempt.get("status") == "complete", f"{key} ledger status is not complete")
        _require(attempt.get("group") == expected_group, f"{key} ledger group mismatch")
        _require(attempt.get("device") == expected_device, f"{key} ledger device mismatch")
        _require(
            float(attempt.get("declared_wall_seconds")) == declared,
            f"{key} ledger wall reservation mismatch",
        )
        reserved = _parse_utc(str(attempt.get("reserved_utc")), f"{key} reservation")
        ended = _parse_utc(str(attempt.get("ended_utc")), f"{key} completion")
        _require(ended >= reserved, f"{key} ledger completion precedes reservation")
        declared_total += declared
        declared_by_group[expected_group] += declared
    _require(
        declared_total <= float(unlock["cumulative_wall_seconds"]),
        "ledger exceeds cumulative reservation budget",
    )
    _require(
        all(value <= float(unlock["per_group_wall_seconds"]) for value in declared_by_group.values()),
        "ledger exceeds a per-group reservation budget",
    )
    recorded_ledgers = sorted(
        path.relative_to(PANEL_ROOT).as_posix() for path in PANEL_ROOT.rglob("ATTEMPTS.json")
    )
    _require(
        recorded_ledgers == ["runs/validation_one_input_v1/ATTEMPTS.json"],
        "unexpected breadth-panel attempt ledger is present",
    )

    return {
        "config": config,
        "point_map": point_map,
        "lock": lock,
        "unlock": unlock,
        "attempts": attempts,
        "hashes": {
            "config_sha256": config_digest,
            "lock_sha256": lock_digest,
            "unlock_sha256": unlock_digest,
            "attempt_ledger_sha256": sha256(ATTEMPTS_PATH),
            "source_bundle_sha256": str(lock["bundle_sha256"]),
        },
        "locked_file_count": len(entries),
        "declared_wall_seconds": declared_total,
        "declared_wall_seconds_by_group": declared_by_group,
        "recorded_attempt_ledgers": recorded_ledgers,
    }


def _load_arrays(path: Path, point: dict[str, Any]) -> dict[str, np.ndarray]:
    expected = {
        "time",
        "lineage_ids",
        "column_lineage_id",
        "antithetic_sign",
        "array_schema_version",
        "checkpoint_steps",
        "w_recurrence_relative_error",
        "w_monitor_rows",
        "w_monitor_cols",
        *(f"raw_{field}" for field in OBSERVABLE_FIELDS),
        *(f"proxy_{field}" for field in OBSERVABLE_FIELDS),
        *(f"update_{field}" for field in UPDATE_FIELDS),
    }
    with np.load(path, allow_pickle=False) as archive:
        _require(set(archive.files) == expected, f"{path} array schema differs")
        arrays = {key: np.asarray(archive[key]) for key in archive.files}

    step = float(point["step"])
    steps = int(round(float(point["max_time"]) / step))
    _require(arrays["array_schema_version"].item() == b"breadth-one-input-arrays-v1", "wrong array schema")
    _require(arrays["time"].shape == (steps + 1,), "wrong time shape")
    _require(
        np.array_equal(arrays["time"], np.arange(steps + 1, dtype=np.float64) * step),
        "stored time grid differs from exact Euler grid",
    )
    _require(np.array_equal(arrays["lineage_ids"], np.asarray((0,), dtype=np.int64)), "wrong lineage IDs")
    _require(np.array_equal(arrays["column_lineage_id"], np.asarray((0, 0), dtype=np.int64)), "wrong column lineage IDs")
    _require(np.array_equal(arrays["antithetic_sign"], np.asarray((1, -1), dtype=np.int8)), "wrong antithetic signs")
    for prefix in ("raw", "proxy"):
        for field in OBSERVABLE_FIELDS:
            _require(arrays[f"{prefix}_{field}"].shape == (steps + 1, 2), f"wrong {prefix}_{field} shape")
    for field in UPDATE_FIELDS:
        _require(arrays[f"update_{field}"].shape == (steps, 2), f"wrong update_{field} shape")
    _require(arrays["w_recurrence_relative_error"].ndim == 2, "wrong recurrence-error rank")
    _require(arrays["w_recurrence_relative_error"].shape[1] == 2, "wrong recurrence-error columns")
    _require(
        arrays["checkpoint_steps"].shape[0] == arrays["w_recurrence_relative_error"].shape[0],
        "checkpoint and recurrence lengths differ",
    )
    for key, value in arrays.items():
        if np.issubdtype(value.dtype, np.floating):
            _require(bool(np.all(np.isfinite(value))), f"nonfinite array {key}")
    for prefix in ("raw", "proxy"):
        for field in ("kernel", "kernel_a", "kernel_W", "kernel_u", "q1", "q2"):
            _require(bool(np.all(arrays[f"{prefix}_{field}"] > 0.0)), f"nonpositive {prefix}_{field}")
    return arrays


def _verify_proxy_coordinates(arrays: dict[str, np.ndarray], configuration: str) -> None:
    if configuration in {"centered_c1", "relative_metric_l2"}:
        for field in OBSERVABLE_FIELDS:
            _require(
                np.array_equal(arrays[f"proxy_{field}"], arrays[f"raw_{field}"]),
                f"identity proxy map failed for {configuration}/{field}",
            )
        return
    _require(configuration == "variance_vhalf", "unexpected validation configuration")
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
    for field, factor in factors.items():
        _require(
            np.array_equal(arrays[f"proxy_{field}"], factor * arrays[f"raw_{field}"]),
            f"variance proxy map failed for {field}",
        )


def _recompute_diagnostics(arrays: dict[str, np.ndarray], step: float) -> dict[str, float]:
    mean_output = arrays["raw_output"].mean(axis=1)
    mean_loss = arrays["raw_loss"].mean(axis=1)
    through = mean_output[:-1] <= 0.95
    _require(bool(np.any(through)), "no update lies through y=.95")
    lhs = np.diff(mean_output) / (2.0 * step)
    rhs = arrays["raw_weighted_kernel"][:-1].mean(axis=1)
    defect = lhs - rhs
    scale = np.maximum(np.abs(rhs[through]), 1e-12)
    diagnostics = {
        "driver_max_relative_defect_through_y_0_95": float(np.max(np.abs(defect[through]) / scale)),
        "driver_rms_relative_defect_through_y_0_95": float(
            np.sqrt(np.mean(defect[through] ** 2))
            / max(np.sqrt(np.mean(rhs[through] ** 2)), 1e-12)
        ),
        "driver_cumulative_relative_defect_through_y_0_95": float(
            abs(np.sum(2.0 * step * defect[through]))
            / max(abs(np.sum(2.0 * step * rhs[through])), 1e-12)
        ),
        "minimum_mean_output_increment": float(np.min(np.diff(mean_output))),
        "maximum_mean_loss_increment": float(np.max(np.diff(mean_loss))),
        "maximum_w_recurrence_relative_error": float(np.max(arrays["w_recurrence_relative_error"])),
    }
    mask = through[:, None]
    for field in ("a_unchanged_fraction", "u_unchanged_fraction", "w_unchanged_fraction"):
        diagnostics[f"maximum_{field}_through_y_0_95"] = float(
            np.max(np.where(mask, arrays[f"update_{field}"], -np.inf))
        )
    for field in ("a_ratio", "u_ratio", "w_ratio", "a_cosine", "u_cosine", "w_cosine"):
        values = np.where(mask, arrays[f"update_{field}"], np.nan)
        diagnostics[f"minimum_{field}_through_y_0_95"] = float(np.nanmin(values))
        if field.endswith("ratio"):
            diagnostics[f"maximum_{field}_through_y_0_95"] = float(np.nanmax(values))
    return diagnostics


def _verify_manifest(
    key: str,
    point: dict[str, Any],
    manifest: dict[str, Any],
    arrays_path: Path,
    authority: dict[str, Any],
) -> None:
    hashes = authority["hashes"]
    unlock = authority["unlock"]
    attempt = authority["attempts"]["attempts"][key]
    _require(manifest.get("status") == "complete", f"{key} manifest is not complete")
    _require(manifest.get("completed_under_caps") is True, f"{key} did not complete under caps")
    _require(manifest.get("accepted_for_scientific_analysis") is False, f"{key} was prematurely accepted")
    _require(manifest.get("point") == key, f"{key} manifest point mismatch")
    _require(manifest.get("point_contract") == point, f"{key} manifest point contract mismatch")
    _require(manifest.get("config_sha256") == hashes["config_sha256"], f"{key} config hash mismatch")
    _require(manifest.get("lock_sha256") == hashes["lock_sha256"], f"{key} lock hash mismatch")
    _require(manifest.get("unlock_sha256") == hashes["unlock_sha256"], f"{key} unlock hash mismatch")
    _require(
        manifest.get("source_bundle_sha256") == hashes["source_bundle_sha256"],
        f"{key} source bundle mismatch",
    )
    _require(manifest.get("raw_sha256") == sha256(arrays_path), f"{key} raw archive hash mismatch")
    expected_device = str(unlock["allowed_points"][key])
    _require(manifest.get("device") == expected_device, f"{key} manifest device mismatch")
    _require(manifest.get("gpu_name") in unlock["allowed_gpu_names"], f"{key} GPU is unauthorized")
    _require(manifest.get("deterministic_algorithms") is True, f"{key} determinism disabled")
    _require(manifest.get("tf32_matmul") is False, f"{key} TF32 enabled")
    _require(manifest.get("cublas_workspace_config") == ":4096:8", f"{key} CUBLAS mode mismatch")
    _require(float(manifest["outer_elapsed_seconds"]) < float(point["caps"]["wall_seconds"]), f"{key} wall cap crossed")
    _require(float(manifest["outer_gpu_allocated_gib"]) <= float(point["caps"]["gpu_memory_gib"]), f"{key} GPU cap crossed")
    _require(float(manifest["outer_host_rss_gib"]) <= float(point["caps"]["host_rss_gib"]), f"{key} host cap crossed")
    _require(
        _parse_utc(str(manifest["started_utc"]), f"{key} manifest start")
        >= _parse_utc(str(attempt["reserved_utc"]), f"{key} reservation"),
        f"{key} began before its reservation",
    )
    _require(
        _parse_utc(str(manifest["ended_utc"]), f"{key} manifest end")
        <= _parse_utc(str(attempt["ended_utc"]), f"{key} ledger end"),
        f"{key} ledger ended before manifest",
    )

    command = manifest.get("command")
    _require(isinstance(command, list) and all(isinstance(v, str) for v in command), f"{key} command malformed")
    _require(_ends_with_path(command[0], "breadth_panel/one_input/run_one_input_point.py"), f"{key} wrong runner")
    _require(_command_value(command, "--point") == key, f"{key} command point mismatch")
    _require(_command_value(command, "--device") == expected_device, f"{key} command device mismatch")
    _require(
        int(_command_value(command, "--external-timeout-seconds"))
        == int(unlock["external_timeout_seconds"][key]),
        f"{key} command timeout mismatch",
    )
    expected_suffixes = {
        "--config": "breadth_panel/FROZEN_ONE_INPUT_POINTS.json",
        "--lock": "breadth_panel/FROZEN_ONE_INPUT_LOCK.json",
        "--unlock": "breadth_panel/ONE_INPUT_VALIDATION_UNLOCK.json",
        "--output": f"breadth_panel/runs/validation_one_input_v1/{key}",
    }
    for flag, suffix in expected_suffixes.items():
        _require(_ends_with_path(_command_value(command, flag), suffix), f"{key} command {flag} mismatch")


def _interpolate_observables(arrays: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    output = arrays["raw_output"].mean(axis=1)
    _require(bool(np.all(np.diff(output) > 0.0)), "ensemble-output clock is not strictly increasing")
    _require(output[0] <= PHYSICAL_NODES[0] and output[-1] >= PHYSICAL_NODES[-1], "output clock does not bracket nodes")
    weighted = arrays["raw_weighted_kernel"].mean(axis=1)
    values = {
        "Keff": weighted / (1.0 - output),
        "Kdir": arrays["raw_kernel"].mean(axis=1),
        "Q2": arrays["raw_q2"].mean(axis=1),
    }
    return {name: np.interp(PHYSICAL_NODES, output, curve) for name, curve in values.items()}


def _symmetric_relative(coarse: np.ndarray, fine: np.ndarray) -> np.ndarray:
    denominator = 0.5 * (np.abs(coarse) + np.abs(fine))
    return np.divide(
        np.abs(fine - coarse),
        denominator,
        out=np.zeros_like(denominator),
        where=denominator != 0.0,
    )


def _as_floats(values: Iterable[float]) -> list[float]:
    return [float(value) for value in values]


def _gate_record(
    group: str,
    fine_diagnostics: dict[str, float],
    coarse_fine: dict[str, Any],
    archive_valid: bool,
) -> tuple[dict[str, bool], list[str]]:
    passes = {
        "complete_finite_positive": archive_valid,
        "mean_output_nondecreasing": fine_diagnostics["minimum_mean_output_increment"] >= -1e-6,
        "mean_loss_nonincreasing": fine_diagnostics["maximum_mean_loss_increment"] <= 1e-6,
        "a_cosine": fine_diagnostics["minimum_a_cosine_through_y_0_95"] >= COSINE_LIMITS["a"],
        "u_cosine": fine_diagnostics["minimum_u_cosine_through_y_0_95"] >= COSINE_LIMITS["u"],
        "w_cosine": fine_diagnostics["minimum_w_cosine_through_y_0_95"] >= COSINE_LIMITS["w"],
        "a_ratio": RATIO_LIMITS["a"][0]
        <= fine_diagnostics["minimum_a_ratio_through_y_0_95"]
        <= fine_diagnostics["maximum_a_ratio_through_y_0_95"]
        <= RATIO_LIMITS["a"][1],
        "u_ratio": RATIO_LIMITS["u"][0]
        <= fine_diagnostics["minimum_u_ratio_through_y_0_95"]
        <= fine_diagnostics["maximum_u_ratio_through_y_0_95"]
        <= RATIO_LIMITS["u"][1],
        "w_ratio": RATIO_LIMITS["w"][0]
        <= fine_diagnostics["minimum_w_ratio_through_y_0_95"]
        <= fine_diagnostics["maximum_w_ratio_through_y_0_95"]
        <= RATIO_LIMITS["w"][1],
        "driver_max": fine_diagnostics["driver_max_relative_defect_through_y_0_95"] <= DRIVER_LIMITS["max"],
        "driver_rms": fine_diagnostics["driver_rms_relative_defect_through_y_0_95"] <= DRIVER_LIMITS["rms"],
        "driver_cumulative": fine_diagnostics["driver_cumulative_relative_defect_through_y_0_95"] <= DRIVER_LIMITS["cumulative"],
        "Keff_coarse_fine": coarse_fine["Keff"]["max_symmetric_relative_difference"]
        <= coarse_fine["Keff"]["gate_threshold"],
    }
    if group == "M":
        passes["Q2_coarse_fine"] = (
            coarse_fine["Q2"]["max_symmetric_relative_difference"]
            <= LOCAL_DIFFERENCE_CEILING
        )
    failures = [name for name, passed in passes.items() if not passed]
    return passes, failures


def _frozen_gaps() -> dict[str, float]:
    if str(PANEL_ROOT) not in sys.path:
        sys.path.insert(0, str(PANEL_ROOT))
    import proxy_contract  # noqa: PLC0415

    points = proxy_contract.frozen_proxy_points()
    result: dict[str, float] = {}
    for group in GROUPS:
        values = points[group].kernels(0.9)
        result[group] = float(proxy_contract.symmetric_relative_gap(values[2], values[1]))
    return result


def analyze() -> dict[str, Any]:
    authority = verify_authority()
    gaps = _frozen_gaps()
    point_records: dict[str, Any] = {}
    group_arrays: dict[str, dict[str, dict[str, np.ndarray]]] = {}
    manifest_hashes: dict[str, str] = {}
    raw_hashes: dict[str, str] = {}
    resource_points: dict[str, dict[str, float]] = {}

    for group, pair in GROUPS.items():
        group_arrays[group] = {}
        for label, key in zip(("coarse", "fine"), pair):
            point = authority["point_map"][key]
            _require(point["configuration"] == EXPECTED_CONFIGURATIONS[group], f"{key} configuration mismatch")
            point_root = RUN_ROOT / key
            manifest_path = point_root / "manifest.json"
            arrays_path = point_root / "arrays.npz"
            _require(manifest_path.is_file() and arrays_path.is_file(), f"{key} output is incomplete")
            manifest = load_json(manifest_path)
            _verify_manifest(key, point, manifest, arrays_path, authority)
            arrays = _load_arrays(arrays_path, point)
            _verify_proxy_coordinates(arrays, str(point["configuration"]))
            diagnostics = _recompute_diagnostics(arrays, float(point["step"]))
            stored = manifest["diagnostics"]["lineages"]
            _require(len(stored) == 1, f"{key} is not one lineage")
            for metric, value in diagnostics.items():
                _require(float(stored[0][metric]) == value, f"{key} diagnostic mismatch: {metric}")
            _require(int(manifest["diagnostics"]["steps"]) == arrays["time"].size - 1, f"{key} step count mismatch")
            group_arrays[group][label] = arrays
            point_records[key] = {"manifest": manifest, "diagnostics": diagnostics}
            manifest_hashes[key] = sha256(manifest_path)
            raw_hashes[key] = sha256(arrays_path)
            resource_points[key] = {
                "outer_elapsed_seconds": float(manifest["outer_elapsed_seconds"]),
                "outer_gpu_allocated_gib": float(manifest["outer_gpu_allocated_gib"]),
                "outer_host_rss_gib": float(manifest["outer_host_rss_gib"]),
            }

        coarse_key, fine_key = pair
        coarse_manifest = point_records[coarse_key]["manifest"]
        fine_manifest = point_records[fine_key]["manifest"]
        coarse_init = coarse_manifest["diagnostics"]["lineages"][0]["initialization"]
        fine_init = fine_manifest["diagnostics"]["lineages"][0]["initialization"]
        _require(coarse_init == fine_init, f"{group} coarse/fine initialization digests differ")
        _require(
            coarse_manifest["diagnostics"]["lineages"][0]["monitor_sha256"]
            == fine_manifest["diagnostics"]["lineages"][0]["monitor_sha256"],
            f"{group} monitor digests differ",
        )
        coarse_arrays = group_arrays[group]["coarse"]
        fine_arrays = group_arrays[group]["fine"]
        for field in OBSERVABLE_FIELDS:
            _require(
                np.array_equal(coarse_arrays[f"raw_{field}"][0], fine_arrays[f"raw_{field}"][0]),
                f"{group} coarse/fine physical initial arrays differ: {field}",
            )
        for field in ("w_monitor_rows", "w_monitor_cols"):
            _require(np.array_equal(coarse_arrays[field], fine_arrays[field]), f"{group} monitor samples differ")

    base_state_digests = set()
    base_prefix_records = set()
    for group, (_, fine_key) in GROUPS.items():
        initialization = point_records[fine_key]["manifest"]["diagnostics"]["lineages"][0]["initialization"]
        base_state_digests.add(initialization["base_state_sha256"])
        base_prefix_records.add(json.dumps(initialization["base_prefix_sha256"], sort_keys=True))
    _require(len(base_state_digests) == 1, "base-state digest differs across configurations")
    _require(len(base_prefix_records) == 1, "base-prefix digests differ across configurations")

    configurations: dict[str, Any] = {}
    failed_groups: list[str] = []
    for group, (coarse_key, fine_key) in GROUPS.items():
        coarse_values = _interpolate_observables(group_arrays[group]["coarse"])
        fine_values = _interpolate_observables(group_arrays[group]["fine"])
        gap = gaps[group]
        keff_threshold = min(LOCAL_DIFFERENCE_CEILING, 0.25 * gap)
        coarse_fine: dict[str, Any] = {}
        for observable in ("Keff", "Kdir", "Q2"):
            differences = _symmetric_relative(coarse_values[observable], fine_values[observable])
            coarse_fine[observable] = {
                "coarse": _as_floats(coarse_values[observable]),
                "fine": _as_floats(fine_values[observable]),
                "symmetric_relative_difference": _as_floats(differences),
                "max_symmetric_relative_difference": float(np.max(differences)),
            }
        coarse_fine["Keff"]["gate_threshold"] = keff_threshold
        coarse_fine["Q2"]["gate_threshold"] = LOCAL_DIFFERENCE_CEILING if group == "M" else None

        fine_diagnostics = point_records[fine_key]["diagnostics"]
        gate_pass, failures = _gate_record(group, fine_diagnostics, coarse_fine, True)
        local_pass = not failures
        if not local_pass:
            failed_groups.append(group)
        configurations[group] = {
            "configuration": EXPECTED_CONFIGURATIONS[group],
            "local_validation_status": "pass" if local_pass else "fail",
            "scientific_status": "local-pass-only" if local_pass else "inconclusive",
            "failed_gates": failures,
            "gate_pass": gate_pass,
            "frozen_m1_m2_symmetric_gap_y_0_9": gap,
            "physical_output_nodes": _as_floats(PHYSICAL_NODES),
            "coarse_fine": coarse_fine,
            "fine_diagnostics": fine_diagnostics,
            "unchanged_update_fractions_are_red_flags_not_gates": True,
        }

    global_stop = len(failed_groups) >= 2
    _require(failed_groups == ["A", "V"], "derived validation outcome differs from frozen decision")
    _require(configurations["M"]["local_validation_status"] == "pass", "M did not locally pass")
    _require(global_stop, "two-failure panel stop was not triggered")

    actual_elapsed = sum(value["outer_elapsed_seconds"] for value in resource_points.values())
    result: dict[str, Any] = {
        "schema": "breadth-one-input-local-validation-result-v1",
        "bottom_line": (
            "A and V fail local numerical gates and are scientifically inconclusive; "
            "M passes local validation only.  The two-failure hard stop terminates the panel "
            "before any width screen or two-input run is authorized or recorded, so this round "
            "adds no Stieltjes evidence."
        ),
        "authority": {
            **authority["hashes"],
            "analysis_source_sha256": sha256(Path(__file__)),
            "locked_file_count_verified": authority["locked_file_count"],
            "manifest_sha256": manifest_hashes,
            "raw_sha256": raw_hashes,
            "attempts_verified": 6,
            "attempt_statuses": {key: "complete" for key in sorted(raw_hashes)},
            "recorded_attempt_ledgers": authority["recorded_attempt_ledgers"],
        },
        "gate_thresholds": {
            "driver_relative": DRIVER_LIMITS,
            "minimum_update_cosine": COSINE_LIMITS,
            "update_norm_ratio_interval": {key: list(value) for key, value in RATIO_LIMITS.items()},
            "coarse_fine_ceiling": LOCAL_DIFFERENCE_CEILING,
            "mean_output_increment_floor": -1e-6,
            "mean_loss_increment_ceiling": 1e-6,
        },
        "configurations": configurations,
        "global_decision": {
            "failed_local_configurations": failed_groups,
            "failed_local_configuration_count": len(failed_groups),
            "two_failure_hard_stop_triggered": global_stop,
            "width_screen_authorized_or_recorded": False,
            "two_input_authorized_or_recorded": False,
            "recorded_output_points": sorted(raw_hashes),
            "stieltjes_evidence_added": False,
            "terminal_status": "stopped-by-preregistered-local-validation-rule",
        },
        "resources": {
            "reserved_wall_seconds": authority["declared_wall_seconds"],
            "reserved_wall_seconds_by_group": authority["declared_wall_seconds_by_group"],
            "actual_outer_elapsed_seconds_sum": actual_elapsed,
            "maximum_outer_gpu_allocated_gib": max(v["outer_gpu_allocated_gib"] for v in resource_points.values()),
            "maximum_outer_host_rss_gib": max(v["outer_host_rss_gib"] for v in resource_points.values()),
            "points": resource_points,
        },
    }
    return result


def _percent(value: float) -> str:
    return f"{100.0 * value:.5f}%"


def render_report(result: dict[str, Any], result_sha256: str) -> str:
    configs = result["configurations"]
    lines = [
        "# Breadth-panel local validation result",
        "",
        "Status: **terminated by the preregistered two-failure hard stop**.",
        "",
        result["bottom_line"],
        "",
        "## Frozen-gate outcome",
        "",
        "| config | local outcome | max h2/h1 Keff | max h2/h1 Kdir | max h2/h1 Q2 | decisive failed gates |",
        "|---|---|---:|---:|---:|---|",
    ]
    for group in GROUPS:
        record = configs[group]
        comparisons = record["coarse_fine"]
        failed = ", ".join(record["failed_gates"]) or "none"
        lines.append(
            f"| {group} | {record['local_validation_status']} "
            f"({record['scientific_status']}) | "
            f"{_percent(comparisons['Keff']['max_symmetric_relative_difference'])} | "
            f"{_percent(comparisons['Kdir']['max_symmetric_relative_difference'])} | "
            f"{_percent(comparisons['Q2']['max_symmetric_relative_difference'])} | {failed} |"
        )
    lines.extend(
        [
            "",
            "All three coarse/fine kernel comparisons pass the frozen 0.20% ceiling. "
            "M's separately required Q2 comparison also passes.  A nevertheless fails because "
            "its fine-run driver maximum is "
            f"{_percent(configs['A']['fine_diagnostics']['driver_max_relative_defect_through_y_0_95'])} "
            "(limit 0.20%) and its minimum sampled-W update cosine is "
            f"{configs['A']['fine_diagnostics']['minimum_w_cosine_through_y_0_95']:.9f} "
            "(floor 0.995).  V fails because its fine-run minimum sampled-W cosine is "
            f"{configs['V']['fine_diagnostics']['minimum_w_cosine_through_y_0_95']:.9f}. "
            "Unchanged-update fractions were retained as red flags and were not promoted to gates.",
            "",
            "M is only a qualification of this FP32 Euler method for that configuration.  No width "
            "ladder is authorized or recorded, so M is not a finite-width Stieltjes compatibility "
            "result.",
            "",
            "## Provenance and scope",
            "",
            f"The analyzer verified {result['authority']['locked_file_count_verified']} locked source/data "
            "hashes, the lock-implied bundle, the execution unlock, all six manifest/raw hashes, "
            "the exact point contracts, deterministic/TF32 settings, resource caps, common initial "
            "and prefix digests, and exactly six completed ledger reservations.  The raw archives "
            "remain ignored; their digests are retained in `VALIDATION_RESULT.json`.",
            "",
            f"Actual summed outer runtime was {result['resources']['actual_outer_elapsed_seconds_sum']:.3f} s; "
            f"peak recorded allocation was {result['resources']['maximum_outer_gpu_allocated_gib']:.3f} GiB "
            f"GPU and {result['resources']['maximum_outer_host_rss_gib']:.3f} GiB host RSS.",
            "",
            "By the frozen contract, two local-method failures stop the entire panel.  Therefore no "
            "one-input width screen, two-input validation, Stieltjes-bound comparison, or evidential "
            "claim is authorized or recorded in this round.",
            "",
            "The frozen protocol and point JSON deliberately retain their prospective pre-execution "
            "headers; this report and VALIDATION_RESULT.json are the terminal decision artifacts.",
            "",
            "## Reproduction",
            "",
            "From the repository root, run `python studies/stieltjes_conjecture/numerics/"
            "hybrid_mean_field_campaign/breadth_panel/validation_analysis.py --check` to reverify "
            "the locally preserved, Git-ignored NPZ arrays against the tracked manifests and result.  "
            "Use `--write` instead of `--check` to regenerate both compact outputs.",
            "",
            f"`VALIDATION_RESULT.json` SHA-256: `{result_sha256}`.",
            "",
        ]
    )
    return "\n".join(lines)


def _json_bytes(result: dict[str, Any]) -> bytes:
    return (json.dumps(result, indent=2, sort_keys=True) + "\n").encode("utf-8")


def write_outputs(result: dict[str, Any]) -> None:
    result_bytes = _json_bytes(result)
    result_digest = hashlib.sha256(result_bytes).hexdigest()
    RESULT_PATH.write_bytes(result_bytes)
    REPORT_PATH.write_text(render_report(result, result_digest), encoding="utf-8")


def check_outputs(result: dict[str, Any]) -> None:
    expected = _json_bytes(result)
    _require(RESULT_PATH.is_file(), "tracked validation result is missing")
    _require(RESULT_PATH.read_bytes() == expected, "tracked validation result is stale")
    digest = hashlib.sha256(expected).hexdigest()
    _require(REPORT_PATH.is_file(), "tracked validation report is missing")
    _require(
        REPORT_PATH.read_text(encoding="utf-8") == render_report(result, digest),
        "tracked validation report is stale",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = analyze()
    if args.write:
        write_outputs(result)
    else:
        check_outputs(result)
    print(result["bottom_line"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
