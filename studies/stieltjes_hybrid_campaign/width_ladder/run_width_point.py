#!/usr/bin/env python3
"""Fail-closed point runner for the coupled width ladder."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import resource
import shlex
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import torch

from width_engine import BudgetStop, NumericalInvalid, environment_record, run_point


HERE = Path(__file__).resolve().parent
LOCK_PATH = HERE / "FROZEN_LOCK.json"


class ExternalTermination(RuntimeError):
    pass


def _termination_handler(signum, _frame):
    raise ExternalTermination(f"received external signal {signum}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def validate_lock(config_path: Path) -> tuple[dict[str, Any], str]:
    if not LOCK_PATH.exists():
        raise RuntimeError("scientific source lock does not exist")
    lock = load_json(LOCK_PATH)
    if lock.get("status") != "frozen_after_validation":
        raise RuntimeError("scientific source lock is not frozen after validation")
    expected_config = lock["files"].get(str(config_path.relative_to(HERE)))
    if expected_config != sha256(config_path):
        raise RuntimeError("production config differs from source lock")
    for relative, expected in lock["files"].items():
        path = HERE / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"locked source mismatch: {relative}")
    return lock, sha256(LOCK_PATH)


def validate_unlock(
    unlock_path: Path | None,
    *,
    lock_sha256: str,
    config_sha256: str,
    point_id: str,
    run_root: Path,
) -> dict[str, Any]:
    if unlock_path is None or not unlock_path.is_file():
        raise RuntimeError("scientific execution requires a separate unlock record")
    unlock = load_json(unlock_path)
    if unlock.get("status") != "authorized_for_width_viability_stage":
        raise RuntimeError("unlock status does not authorize this stage")
    if unlock.get("frozen_lock_sha256") != lock_sha256:
        raise RuntimeError("unlock does not bind the current source lock")
    if unlock.get("production_config_sha256") != config_sha256:
        raise RuntimeError("unlock does not bind the production config")
    if point_id not in unlock.get("authorized_point_ids", []):
        raise RuntimeError("unlock does not authorize this point")
    declared_root = (HERE / str(unlock.get("run_root", ""))).resolve()
    if declared_root != run_root.resolve():
        raise RuntimeError("unlock binds a different one-attempt run root")
    return unlock


def validate_predecessors(
    point: dict[str, Any], run_root: Path, lock_sha256: str
) -> None:
    for predecessor in point.get("predecessors", []):
        manifest_path = run_root / str(predecessor) / "manifest.json"
        if not manifest_path.is_file():
            raise RuntimeError(f"predecessor {predecessor} has no manifest")
        manifest = load_json(manifest_path)
        if manifest.get("status") != "complete_scientific_valid":
            raise RuntimeError(f"predecessor {predecessor} did not complete validly")
        if manifest.get("frozen_lock_sha256") != lock_sha256:
            raise RuntimeError(f"predecessor {predecessor} used another source lock")


def parse_device(name: str) -> torch.device:
    device = torch.device(name)
    if device.type == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA was requested but is unavailable")
        index = 0 if device.index is None else device.index
        if index < 0 or index >= torch.cuda.device_count():
            raise RuntimeError("CUDA device index is unavailable")
        torch.cuda.set_device(index)
    return device


def write_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--point", required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--unlock", type=Path)
    args = parser.parse_args()

    config_path = args.config.resolve()
    config = load_json(config_path)
    points = {str(point["id"]): point for point in config["points"]}
    if args.point not in points:
        raise ValueError(f"unknown point {args.point!r}")
    point = points[args.point]
    purpose = str(config["purpose"])
    scientific = purpose == "scientific_production_locked"
    if not scientific and purpose != "validation_only_never_scientific":
        raise ValueError(f"unknown config purpose {purpose!r}")

    lock: dict[str, Any] | None = None
    lock_digest: str | None = None
    unlock: dict[str, Any] | None = None
    if scientific:
        lock, lock_digest = validate_lock(config_path)
        unlock = validate_unlock(
            args.unlock,
            lock_sha256=lock_digest,
            config_sha256=sha256(config_path),
            point_id=args.point,
            run_root=args.run_root,
        )
        validate_predecessors(point, args.run_root, lock_digest)

    # Device/environment validation precedes the irreversible one-attempt
    # directory creation.  A missing GPU therefore cannot consume the attempt.
    device = parse_device(args.device)
    environment = environment_record(device)
    point_dir = args.run_root / args.point
    if point_dir.exists():
        raise RuntimeError(f"refusing to overwrite existing point directory {point_dir}")
    point_dir.mkdir(parents=True)
    manifest_path = point_dir / "manifest.json"
    arrays_path = point_dir / "arrays.npz"
    outer_started = time.monotonic()
    if device.type == "cuda":
        torch.cuda.reset_peak_memory_stats(device)
    started = utc_now()
    base_manifest: dict[str, Any] = {
        "schema_version": 1,
        "point_id": args.point,
        "purpose": purpose,
        "started_utc": started,
        "command": " ".join(shlex.quote(piece) for piece in sys.argv),
        "cwd": os.getcwd(),
        "config_path": str(config_path),
        "config_sha256": sha256(config_path),
        "point_config": point,
        "environment": environment,
        "frozen_lock_sha256": lock_digest,
        "unlock_sha256": sha256(args.unlock) if unlock is not None else None,
    }
    write_manifest(manifest_path, {**base_manifest, "status": "running"})
    previous_sigterm = signal.signal(signal.SIGTERM, _termination_handler)

    def heartbeat(diagnostics: dict[str, float | int]) -> None:
        write_manifest(
            manifest_path,
            {
                **base_manifest,
                "status": "running",
                "heartbeat_utc": utc_now(),
                "point_diagnostics": diagnostics,
            },
        )

    try:
        arrays, diagnostics = run_point(
            point,
            seed=int(config["seed"]),
            device=device,
            progress_callback=heartbeat,
        )
        np.savez_compressed(arrays_path, **arrays)
        status = "complete_scientific_valid" if scientific else "complete_validation_only"
        final = {
            **base_manifest,
            "status": status,
            "completed_utc": utc_now(),
            "diagnostics": diagnostics,
            "arrays_file": arrays_path.name,
            "arrays_sha256": sha256(arrays_path),
            "scientific_evidence_admissible": scientific,
        }
        write_manifest(manifest_path, final)
        return 0
    except Exception as exc:
        outer_telemetry = {
            "outer_elapsed_seconds": time.monotonic() - outer_started,
            "outer_host_max_rss_gib": float(
                resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            )
            / 2**20,
            "outer_gpu_max_allocated_gib": (
                float(torch.cuda.max_memory_allocated(device)) / 2**30
                if device.type == "cuda"
                else 0.0
            ),
        }
        failure = {
            **base_manifest,
            "status": "failed_inconclusive",
            "completed_utc": utc_now(),
            "exception_type": type(exc).__name__,
            "exception": str(exc),
            "point_diagnostics": getattr(exc, "point_diagnostics", {}),
            "outer_telemetry": outer_telemetry,
            "scientific_evidence_admissible": False,
        }
        write_manifest(manifest_path, failure)
        if isinstance(exc, (BudgetStop, NumericalInvalid)):
            return 2
        raise
    finally:
        signal.signal(signal.SIGTERM, previous_sigterm)


if __name__ == "__main__":
    raise SystemExit(main())
