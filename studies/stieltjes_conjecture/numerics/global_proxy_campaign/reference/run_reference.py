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
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import torch

from reference_engine import BudgetStop, NumericalInvalid, PointCaps, run_point


HERE = Path(__file__).resolve().parent
RUNS = HERE / "runs"
SOURCE_FILES = (HERE / "canonical_model.py", HERE / "reference_engine.py", Path(__file__))
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
) -> None:
    purpose = config.get("purpose")
    if purpose == "validation_only":
        return
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
    for key, value in expected.items():
        if unlock.get(key) != value:
            raise PermissionError(
                f"scientific production lock mismatch for {key}: "
                f"expected {value!r}, found {unlock.get(key)!r}"
            )


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
    _production_gate(config, config_path, hashes)
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
    summary: dict[str, Any] = {
        "status": "running",
        "purpose": config["purpose"],
        "scientific_evidence_admissible": config["purpose"] == "scientific_production",
        "config_name": config_path.name,
        "config_sha256": config_hash,
        "source_sha256": hashes,
        "source_bundle_sha256": source_bundle_sha256(hashes),
        "environment": environment_record(device),
        "points": [],
    }
    _json_dump(output / "summary.json", summary)

    terminal_failure = False
    for point, caps in zip(points, validated_caps):
        if time.monotonic() - run_start > total_wall_cap:
            summary["status"] = "stopped_global_wall_cap"
            terminal_failure = True
            break
        point_id = str(point["id"])
        point_start = time.monotonic()
        record: dict[str, Any] = {
            "id": point_id,
            "mode": point["mode"],
            "width": int(point["width"]),
            "antithetic_pairs": int(point["antithetic_pairs"]),
            "status": "running",
        }
        summary["points"].append(record)
        _json_dump(output / "summary.json", summary)
        try:
            arrays, diagnostics = run_point(
                point, device=device, dtype=dtype, caps=caps
            )
            array_path = output / f"{point_id}.npz"
            np.savez_compressed(array_path, **arrays)
            elapsed = time.monotonic() - point_start
            if elapsed > caps.wall_seconds:
                raise BudgetStop(
                    f"point cap exceeded including serialization: "
                    f"{elapsed:.3f}s > {caps.wall_seconds:.3f}s"
                )
            record.update(
                {
                    "status": "complete_validation_only"
                    if config["purpose"] == "validation_only"
                    else "complete_scientific_point",
                    "diagnostics": diagnostics,
                    "arrays_file": array_path.name,
                    "arrays_sha256": sha256(array_path),
                    "arrays_bytes": array_path.stat().st_size,
                    "elapsed_seconds_including_serialization": elapsed,
                }
            )
        except BudgetStop as exc:
            record.update({"status": "stopped_budget", "reason": str(exc)})
            terminal_failure = True
        except NumericalInvalid as exc:
            record.update({"status": "inconclusive_numerical_invalid", "reason": str(exc)})
            terminal_failure = True
        except torch.cuda.OutOfMemoryError as exc:
            record.update({"status": "stopped_cuda_oom", "reason": str(exc)})
            terminal_failure = True
        except Exception as exc:
            record.update(
                {"status": "failed_implementation_or_environment", "reason": repr(exc)}
            )
            terminal_failure = True
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

