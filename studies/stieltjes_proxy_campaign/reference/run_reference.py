#!/usr/bin/env python3
"""Fail-closed configuration runner for finite-width reference points.

Scientific execution is mechanically locked until ``PRODUCTION_UNLOCK.json``
binds a frozen configuration hash to the current source-bundle hash.  The
validation-only configuration does not satisfy that gate and cannot be
mistaken for scientific evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import resource
import sys
import time
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import torch

from reference_engine import BudgetStop, NumericalInvalid, PointCaps, run_point


HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
SOURCE_FILES = (
    HERE / "canonical_model.py",
    HERE / "reference_engine.py",
    Path(__file__),
    HERE / "run_capped_reference.sh",
)
HARD_CEILINGS = {
    "total_wall_seconds": 86_400.0,
    "point_wall_seconds": 21_600.0,
    "max_points": 64,
    "max_width": 16_384,
    "max_antithetic_pairs": 2_048,
    "max_output_nodes": 4_096,
    "max_steps_all_batches": 200_000,
    "max_host_rss_gib": 128.0,
    "max_gpu_memory_gib": 23.0,
    "max_raw_curve_mib": 4_096.0,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def source_hashes() -> dict[str, str]:
    return {path.name: sha256(path) for path in SOURCE_FILES}


def source_bundle_sha256(hashes: dict[str, str]) -> str:
    payload = "".join(f"{name}\0{hashes[name]}\n" for name in sorted(hashes))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config",
        type=Path,
        help="a fixed JSON configuration under reference/configs/",
    )
    return parser.parse_args()


def _require_number_at_most(
    value: float | int, ceiling_name: str, *, label: str
) -> None:
    ceiling = HARD_CEILINGS[ceiling_name]
    if value > ceiling:
        raise ValueError(f"{label}={value} exceeds hard ceiling {ceiling}")


def _validate_config_path(path: Path) -> Path:
    resolved = path.resolve()
    config_root = (HERE / "configs").resolve()
    if resolved.parent != config_root or resolved.suffix != ".json":
        raise ValueError("configuration must be a direct JSON child of reference/configs")
    return resolved


def _production_gate(
    config: dict[str, Any], config_path: Path, hashes: dict[str, str]
) -> dict[str, Any]:
    purpose = config.get("purpose")
    if purpose == "validation_only":
        return {"required": False}
    if purpose != "scientific_production":
        raise ValueError("purpose must be validation_only or scientific_production")
    unlock_path = HERE / "PRODUCTION_UNLOCK.json"
    if not unlock_path.exists():
        raise PermissionError(
            "scientific production is locked: PRODUCTION_UNLOCK.json is absent"
        )
    unlock = json.loads(unlock_path.read_text())
    expected = {
        "status": "protocol_frozen_and_execution_authorized",
        "config_name": config_path.name,
        "config_sha256": sha256(config_path),
        "source_bundle_sha256": source_bundle_sha256(hashes),
    }
    expected.update(_analysis_lock_fields(config, config_path))
    for key, value in expected.items():
        if unlock.get(key) != value:
            raise PermissionError(
                f"scientific production lock mismatch for {key}: "
                f"expected {value!r}, found {unlock.get(key)!r}"
            )
    protocol_path = _protocol_path_for_config(config_path)
    protocol_expected = {
        "protocol_name": protocol_path.name,
        "protocol_sha256": sha256(protocol_path),
    }
    for key, value in protocol_expected.items():
        if unlock.get(key) != value:
            raise PermissionError(
                f"scientific production lock mismatch for {key}: "
                f"expected {value!r}, found {unlock.get(key)!r}"
            )
    return {
        "required": True,
        "unlock_name": unlock_path.name,
        "unlock_sha256": sha256(unlock_path),
        **expected,
        **protocol_expected,
    }


def _analysis_lock_fields(
    config: dict[str, Any], config_path: Path
) -> dict[str, str]:
    """Return mandatory unlock fields for a frozen offline-analysis contract.

    Older frozen runs did not have a separate machine-readable analysis file,
    so their historical locks remain valid.  Successor 02 does have one and
    is fail-closed if its name, location, back-reference, or hash is missing.
    """

    metadata = config.get("analysis", {})
    if metadata is None:
        metadata = {}
    if not isinstance(metadata, dict):
        raise ValueError("configuration analysis metadata must be an object")
    name = metadata.get("analysis_config")
    analysis_required = config_path.name == "FROZEN_SUCCESSOR_02.json"
    if name is None:
        if analysis_required:
            raise ValueError("successor-02 requires a frozen analysis configuration")
        return {}
    if not isinstance(name, str) or not name:
        raise ValueError("analysis_config must be a nonempty filename")
    path = (HERE / "configs" / name).resolve()
    config_root = (HERE / "configs").resolve()
    if path.parent != config_root or path.name != name or path.suffix != ".json":
        raise ValueError("analysis_config must be a direct JSON child of reference/configs")
    if not path.is_file():
        raise FileNotFoundError(f"frozen analysis configuration is absent: {path}")
    analysis = json.loads(path.read_text())
    if analysis.get("production_config") != config_path.name:
        raise ValueError(
            "frozen analysis configuration does not point back to the production config"
        )
    return {
        "analysis_config_name": path.name,
        "analysis_config_sha256": sha256(path),
    }


def _protocol_path_for_config(config_path: Path) -> Path:
    """Map a frozen production-config name to its required frozen protocol."""

    if config_path.name == "FROZEN_PRODUCTION.json":
        protocol_name = "PROTOCOL.md"
    elif (
        config_path.name.startswith("FROZEN_SUCCESSOR_")
        and config_path.name.endswith(".json")
    ):
        identifier = config_path.name[
            len("FROZEN_SUCCESSOR_") : -len(".json")
        ]
        if not identifier.isdigit():
            raise ValueError("successor config identifier must contain only digits")
        protocol_name = f"SUCCESSOR_{identifier}_PROTOCOL.md"
    else:
        raise ValueError(
            f"no frozen protocol naming rule for production config {config_path.name!r}"
        )
    protocol_path = (HERE.parent / protocol_name).resolve()
    if protocol_path.parent != HERE.parent.resolve() or not protocol_path.is_file():
        raise FileNotFoundError(f"required frozen protocol is absent: {protocol_path}")
    return protocol_path


def _dtype(name: str) -> torch.dtype:
    if name != "float64":
        raise ValueError("only float64 is admissible for this reference campaign")
    return torch.float64


def _device(name: str, gpu_memory_gib: float) -> torch.device:
    device = torch.device(name)
    if device.type == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("configuration requests CUDA but CUDA is unavailable")
        if device.index is None or device.index >= torch.cuda.device_count():
            raise RuntimeError(f"requested CUDA device is unavailable: {name}")
        total = torch.cuda.get_device_properties(device).total_memory / 2**30
        if gpu_memory_gib >= total:
            raise ValueError(
                f"GPU cap {gpu_memory_gib:.3f} GiB must be below device total "
                f"{total:.3f} GiB"
            )
        torch.cuda.set_device(device)
        torch.cuda.set_per_process_memory_fraction(gpu_memory_gib / total, device)
        torch.cuda.reset_peak_memory_stats(device)
    return device


def _validate_point(
    point: dict[str, Any], global_caps: dict[str, Any], dtype: torch.dtype
) -> PointCaps:
    required = {
        "id",
        "mode",
        "width",
        "antithetic_pairs",
        "pair_batch_size",
        "seed_base",
        "step",
        "output_nodes",
        "caps",
    }
    missing = sorted(required - point.keys())
    if missing:
        raise ValueError(f"point is missing required fields: {missing}")
    width = int(point["width"])
    pairs = int(point["antithetic_pairs"])
    batch_pairs = int(point["pair_batch_size"])
    nodes = list(point["output_nodes"])
    _require_number_at_most(width, "max_width", label="width")
    _require_number_at_most(pairs, "max_antithetic_pairs", label="pairs")
    _require_number_at_most(len(nodes), "max_output_nodes", label="output nodes")
    if width > int(global_caps["max_width"]):
        raise ValueError("point width exceeds the configuration-global cap")
    if pairs > int(global_caps["max_antithetic_pairs"]):
        raise ValueError("point pair count exceeds the configuration-global cap")
    if not (1 <= batch_pairs <= pairs):
        raise ValueError("pair_batch_size must lie in [1, antithetic_pairs]")
    mode = str(point["mode"])
    endpoint = float(point["max_time"] if mode == "physical" else point["max_output"])
    step = float(point["step"])
    if step <= 0.0 or endpoint < 0.0:
        raise ValueError("step must be positive and endpoint nonnegative")
    for tolerance_name in (
        "antithetic_initial_cancellation_tolerance",
        "loss_nonincrease_tolerance",
    ):
        if tolerance_name in point:
            tolerance = float(point[tolerance_name])
            if not np.isfinite(tolerance) or tolerance < 0.0:
                raise ValueError(
                    f"{tolerance_name} must be finite and nonnegative"
                )
    steps_per_batch = int(round(endpoint / step))
    batches = math_ceil_div(pairs, batch_pairs)
    total_steps = steps_per_batch * batches
    point_caps = point["caps"]
    if total_steps > int(point_caps["max_steps_all_batches"]):
        raise ValueError(
            f"point declares {total_steps} batch steps but caps "
            f"{point_caps['max_steps_all_batches']}"
        )
    _require_number_at_most(
        total_steps, "max_steps_all_batches", label="steps across batches"
    )
    _require_number_at_most(
        float(point_caps["wall_seconds"]),
        "point_wall_seconds",
        label="point wall seconds",
    )
    _require_number_at_most(
        float(point_caps["host_rss_gib"]),
        "max_host_rss_gib",
        label="point host RSS GiB",
    )
    _require_number_at_most(
        float(point_caps["gpu_memory_gib"]),
        "max_gpu_memory_gib",
        label="point GPU GiB",
    )

    element_bytes = torch.tensor([], dtype=dtype).element_size()
    trajectories_per_batch = 2 * batch_pairs
    state_elements = trajectories_per_batch * (width * width + 2 * width)
    method_multiplier = 20 if point.get("integrator", "midpoint") == "rk4" else 12
    predicted_working_gib = state_elements * element_bytes * method_multiplier / 2**30
    memory_cap = (
        float(point_caps["gpu_memory_gib"])
        if str(global_caps["device"]).startswith("cuda")
        else float(point_caps["host_rss_gib"])
    )
    if predicted_working_gib > 0.90 * memory_cap:
        raise ValueError(
            f"conservative working-memory estimate {predicted_working_gib:.3f} GiB "
            f"exceeds 90% of point cap {memory_cap:.3f} GiB"
        )
    raw_fields = 9
    predicted_raw_mib = (
        (steps_per_batch + 1) * (2 * pairs) * raw_fields * element_bytes / 2**20
    )
    if predicted_raw_mib > float(point_caps["max_raw_curve_mib"]):
        raise ValueError(
            f"raw-curve estimate {predicted_raw_mib:.3f} MiB exceeds point cap"
        )
    _require_number_at_most(
        float(point_caps["max_raw_curve_mib"]),
        "max_raw_curve_mib",
        label="raw curve MiB",
    )
    return PointCaps(
        wall_seconds=float(point_caps["wall_seconds"]),
        max_steps=int(point_caps["max_steps_all_batches"]),
        host_rss_gib=float(point_caps["host_rss_gib"]),
        gpu_memory_gib=float(point_caps["gpu_memory_gib"]),
        state_ceiling=float(point_caps["state_ceiling"]),
        kernel_ceiling=float(point_caps["kernel_ceiling"]),
        kernel_floor=float(point_caps["kernel_floor"]),
        diagnostic_stride=int(point_caps["diagnostic_stride"]),
    )


def math_ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def _json_dump(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _command_record() -> dict[str, Any]:
    """Return a JSON-safe reproduction record for this Python invocation."""

    return {
        "python_executable": sys.executable,
        "argv": [str(argument) for argument in sys.argv],
    }


def _resource_snapshot(device: torch.device) -> dict[str, float | int]:
    """Best-effort fallback telemetry when the engine did not return normally."""

    gpu_peak = 0.0
    if device.type == "cuda":
        gpu_peak = torch.cuda.max_memory_allocated(device) / 2**30
    return {
        "integrator_steps_all_batches": 0,
        "max_host_rss_gib": (
            float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20
        ),
        "max_gpu_allocated_gib": gpu_peak,
    }


def _exception_diagnostics(
    exc: BaseException, device: torch.device
) -> dict[str, Any]:
    attached = getattr(exc, "point_diagnostics", None)
    if isinstance(attached, dict):
        return dict(attached)
    return _resource_snapshot(device)


def _caps_with_remaining_wall(caps: PointCaps, remaining: float) -> PointCaps:
    """Intersect a point wall cap with the run's unused global wall budget."""

    if remaining <= 0.0:
        raise BudgetStop("global wall cap reached before point start")
    return replace(caps, wall_seconds=min(caps.wall_seconds, remaining))


def environment_record(device: torch.device) -> dict[str, Any]:
    result: dict[str, Any] = {
        "python": sys.version,
        "platform": platform.platform(),
        "torch": torch.__version__,
        "torch_cuda_build": torch.version.cuda,
        "numpy": np.__version__,
        "device": str(device),
        "pid": os.getpid(),
    }
    if device.type == "cuda":
        properties = torch.cuda.get_device_properties(device)
        free, total = torch.cuda.mem_get_info(device)
        result["cuda_device"] = {
            "name": properties.name,
            "total_memory_gib": total / 2**30,
            "free_memory_gib_at_start": free / 2**30,
            "capability": list(properties.major_minor) if hasattr(properties, "major_minor") else [properties.major, properties.minor],
        }
    return result


def main() -> int:
    args = parse_args()
    config_path = _validate_config_path(args.config)
    config = json.loads(config_path.read_text())
    if int(config.get("schema_version", -1)) != 1:
        raise ValueError("unsupported configuration schema")
    hashes = source_hashes()
    authorization = _production_gate(config, config_path, hashes)
    global_caps = dict(config["global_caps"])
    total_wall_cap = float(global_caps["total_wall_seconds"])
    _require_number_at_most(
        total_wall_cap, "total_wall_seconds", label="total wall seconds"
    )
    points = list(config["points"])
    _require_number_at_most(len(points), "max_points", label="point count")
    if len(points) > int(global_caps["max_points"]):
        raise ValueError("point count exceeds configuration-global cap")
    dtype = _dtype(str(config["dtype"]))
    max_gpu_cap = max(float(point["caps"]["gpu_memory_gib"]) for point in points)
    device = _device(str(global_caps["device"]), max_gpu_cap)
    validated_caps = [
        _validate_point(point, global_caps, dtype) for point in points
    ]

    output = (RUNS / str(config["run_id"])).resolve()
    if output.parent != RUNS.resolve():
        raise ValueError("run_id must resolve to a direct child of reference/runs")
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"refusing to overwrite nonempty run directory: {output}")
    output.mkdir(parents=True, exist_ok=True)
    config_hash = sha256(config_path)
    run_start = time.monotonic()
    global_wall_deadline = run_start + total_wall_cap
    run_started_utc = _utc_now()
    command = _command_record()
    summary: dict[str, Any] = {
        "status": "running",
        "run_purpose": config["purpose"],
        # Purpose records what was requested.  Acceptance remains false until
        # every registered point has completed and the run closes normally.
        "accepted_as_scientific_evidence": False,
        "scientific_evidence_admissible": False,
        "command": command,
        "started_utc": run_started_utc,
        "ended_utc": None,
        "config_name": config_path.name,
        "config_sha256": config_hash,
        "registered_seed_bases": [int(point["seed_base"]) for point in points],
        "source_sha256": hashes,
        "source_bundle_sha256": source_bundle_sha256(hashes),
        "authorization": authorization,
        "environment": environment_record(device),
        "points": [],
    }
    _json_dump(output / "summary.json", summary)

    terminal_failure = False
    for point, caps in zip(points, validated_caps):
        elapsed_before_point = time.monotonic() - run_start
        if elapsed_before_point >= total_wall_cap:
            summary["status"] = "stopped_global_wall_cap"
            terminal_failure = True
            break
        effective_caps = _caps_with_remaining_wall(
            caps, total_wall_cap - elapsed_before_point
        )
        if device.type == "cuda":
            # Point certificates report point-local CUDA peaks.  Run-level
            # peaks are reconstructed as the maximum of these certificates.
            torch.cuda.reset_peak_memory_stats(device)
        point_id = str(point["id"])
        point_start = time.monotonic()
        point_started_utc = _utc_now()
        record: dict[str, Any] = {
            "id": point_id,
            "mode": point["mode"],
            "width": int(point["width"]),
            "antithetic_pairs": int(point["antithetic_pairs"]),
            "seed_base": int(point["seed_base"]),
            "run_purpose": config["purpose"],
            "accepted_as_scientific_evidence": False,
            "scientific_evidence_admissible": False,
            "command": command,
            "started_utc": point_started_utc,
            "ended_utc": None,
            "declared_point_wall_seconds": caps.wall_seconds,
            "effective_point_wall_seconds": effective_caps.wall_seconds,
            "status": "running",
        }
        summary["points"].append(record)
        _json_dump(output / "summary.json", summary)
        try:
            arrays, diagnostics = run_point(
                point,
                device=device,
                dtype=dtype,
                caps=effective_caps,
                absolute_wall_deadline=global_wall_deadline,
            )
            record["diagnostics"] = diagnostics
            array_path = output / f"{point_id}.npz"
            np.savez_compressed(array_path, **arrays)
            elapsed = time.monotonic() - point_start
            if time.monotonic() > global_wall_deadline:
                raise BudgetStop(
                    "global wall cap exceeded including point serialization"
                )
            if elapsed > effective_caps.wall_seconds:
                raise BudgetStop(
                    "effective point/global wall cap exceeded including serialization: "
                    f"{elapsed:.3f}s > {effective_caps.wall_seconds:.3f}s"
                )
            record.update(
                {
                    "status": "complete_validation_only"
                    if config["purpose"] == "validation_only"
                    else "complete_scientific_point",
                    "arrays_file": array_path.name,
                    "arrays_sha256": sha256(array_path),
                    "arrays_bytes": array_path.stat().st_size,
                    "elapsed_seconds_including_serialization": elapsed,
                }
            )
        except BudgetStop as exc:
            record.update(
                {
                    "status": "stopped_budget",
                    "reason": str(exc),
                    "diagnostics": record.get(
                        "diagnostics", _exception_diagnostics(exc, device)
                    ),
                }
            )
            terminal_failure = True
        except NumericalInvalid as exc:
            record.update(
                {
                    "status": "inconclusive_numerical_invalid",
                    "reason": str(exc),
                    "diagnostics": record.get(
                        "diagnostics", _exception_diagnostics(exc, device)
                    ),
                }
            )
            terminal_failure = True
        except torch.cuda.OutOfMemoryError as exc:
            record.update(
                {
                    "status": "stopped_cuda_oom",
                    "reason": str(exc),
                    "diagnostics": record.get(
                        "diagnostics", _exception_diagnostics(exc, device)
                    ),
                }
            )
            terminal_failure = True
        except Exception as exc:
            record.update(
                {
                    "status": "failed_implementation_or_environment",
                    "reason": repr(exc),
                    "diagnostics": record.get(
                        "diagnostics", _exception_diagnostics(exc, device)
                    ),
                }
            )
            terminal_failure = True
        record["ended_utc"] = _utc_now()
        record["elapsed_seconds"] = time.monotonic() - point_start
        record.setdefault("diagnostics", _resource_snapshot(device))
        _json_dump(output / "summary.json", summary)
        if terminal_failure:
            break

    if summary["status"] == "running":
        summary["status"] = "terminated_after_point_failure" if terminal_failure else (
            "complete_validation_only"
            if config["purpose"] == "validation_only"
            else "complete_scientific_run"
        )
    summary["total_elapsed_seconds"] = time.monotonic() - run_start
    summary["ended_utc"] = _utc_now()
    run_accepted = summary["status"] == "complete_scientific_run" and bool(points)
    summary["accepted_as_scientific_evidence"] = run_accepted
    summary["scientific_evidence_admissible"] = run_accepted
    for record in summary["points"]:
        point_accepted = run_accepted and record["status"] == "complete_scientific_point"
        record["accepted_as_scientific_evidence"] = point_accepted
        record["scientific_evidence_admissible"] = point_accepted
    point_diagnostics = [
        record.get("diagnostics", {}) for record in summary["points"]
    ]
    fallback_resources = _resource_snapshot(device)
    summary["run_diagnostics"] = {
        "integrator_steps_all_points": sum(
            int(diagnostics.get("integrator_steps_all_batches", 0))
            for diagnostics in point_diagnostics
        ),
        "max_host_rss_gib": max(
            [float(fallback_resources["max_host_rss_gib"])]
            + [
                float(diagnostics.get("max_host_rss_gib", 0.0))
                for diagnostics in point_diagnostics
            ]
        ),
        "max_gpu_allocated_gib": max(
            [float(fallback_resources["max_gpu_allocated_gib"])]
            + [
                float(diagnostics.get("max_gpu_allocated_gib", 0.0))
                for diagnostics in point_diagnostics
            ]
        ),
    }
    summary["terminal_stop_no_unregistered_branch"] = True
    _json_dump(output / "summary.json", summary)
    manifest = {
        path.name: {"sha256": sha256(path), "bytes": path.stat().st_size}
        for path in sorted(output.iterdir())
        if path.is_file()
    }
    _json_dump(output / "manifest.json", manifest)
    return 1 if terminal_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
