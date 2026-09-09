#!/usr/bin/env python3
"""Fail-closed CLI for one two-input FP32 Euler point."""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import platform
import resource
import shlex
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np

# This must be set before the first CUDA context is created.
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
os.environ["NVIDIA_TF32_OVERRIDE"] = "0"
import torch

from two_input_simulator import (
    BudgetStop,
    NumericalInvalid,
    simulate_point,
    validate_point,
)


HERE = Path(__file__).resolve().parent
REQUIRED_LOCK_BASENAMES = {
    "two_input_engine.py",
    "two_input_simulator.py",
    "run_two_input_point.py",
    "run_capped_two_input.sh",
    "PROTOCOL.md",
    "proxy_contract.py",
}
REQUIRED_LOCK_TARGETS = {
    "two_input_engine.py": HERE / "two_input_engine.py",
    "two_input_simulator.py": HERE / "two_input_simulator.py",
    "run_two_input_point.py": HERE / "run_two_input_point.py",
    "run_capped_two_input.sh": HERE / "run_capped_two_input.sh",
    "PROTOCOL.md": HERE.parent / "PROTOCOL.md",
    "proxy_contract.py": HERE.parent / "proxy_contract.py",
}


class ExternalTermination(RuntimeError):
    pass


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_bundle_sha256(
    root: Path, entries: dict[str, str]
) -> str:
    """Hash the exact ordered path/digest table declared by a source lock."""

    del root
    digest = hashlib.sha256()
    for relative, expected in sorted(entries.items()):
        digest.update(
            relative.encode("utf-8")
            + b"\0"
            + expected.encode("ascii")
            + b"\n"
        )
    return digest.hexdigest()


def verify_lock(lock_path: Path, config_path: Path) -> dict[str, Any]:
    lock = json.loads(lock_path.read_text())
    if lock.get("status") != "frozen":
        raise RuntimeError("source lock is not frozen")
    entries = lock.get("sha256")
    if not isinstance(entries, dict) or not entries:
        raise RuntimeError("source lock has no file hashes")
    root = lock_path.parent
    bound_targets = {
        basename
        for basename, target in REQUIRED_LOCK_TARGETS.items()
        if any(
            Path(relative).name == basename
            and (root / relative).resolve() == target.resolve()
            for relative in entries
        )
    }
    missing = REQUIRED_LOCK_BASENAMES - bound_targets
    if missing:
        raise RuntimeError(
            f"source lock omits required source/protocol/proxy files: {sorted(missing)}"
        )
    for relative, expected in entries.items():
        path = root / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"source-lock mismatch for {relative}")
    if sha256(config_path) != lock.get("config_sha256"):
        raise RuntimeError("configuration hash differs from source lock")
    actual_bundle = source_bundle_sha256(root, entries)
    if actual_bundle != lock.get("bundle_sha256"):
        raise RuntimeError("source bundle hash differs from source lock")
    return lock


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def verify_unlock(
    unlock_path: Path,
    lock_path: Path,
    config_path: Path,
    point: dict[str, Any],
    device_name: str,
    output_root_argument: Path,
) -> tuple[dict[str, Any], Path]:
    unlock = json.loads(unlock_path.read_text())
    if unlock.get("status") != "execution-authorized-once":
        raise RuntimeError("execution unlock is not active")
    if unlock.get("lock_sha256") != sha256(lock_path):
        raise RuntimeError("unlock does not bind the source lock")
    if unlock.get("config_sha256") != sha256(config_path):
        raise RuntimeError("unlock does not bind the point config")
    if unlock.get("allowed_points", {}).get(point["id"]) != device_name:
        raise RuntimeError("point/device pair is not authorized")
    root = (unlock_path.parent / unlock["output_root"]).resolve()
    if output_root_argument.resolve() != root:
        raise RuntimeError("output root differs from the authorized path")
    if point["id"] not in unlock.get("point_groups", {}):
        raise RuntimeError("unlock omits the point budget group")
    if not unlock.get("allowed_gpu_names"):
        raise RuntimeError("unlock has no allowed GPU class")
    for key in ("cumulative_wall_seconds", "per_group_wall_seconds"):
        if float(unlock.get(key, 0.0)) <= 0.0:
            raise RuntimeError(f"unlock has invalid {key}")
    return unlock, root


def reserve_attempt(
    root: Path,
    unlock: dict[str, Any],
    point: dict[str, Any],
    device_name: str,
) -> Path:
    """Atomically consume one point attempt and its declared group budgets."""

    root.mkdir(parents=True, exist_ok=True)
    mutex_path = root / ".attempts.lock"
    ledger_path = root / "ATTEMPTS.json"
    with mutex_path.open("a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        ledger = (
            json.loads(ledger_path.read_text())
            if ledger_path.exists()
            else {"schema": "breadth-two-input-attempt-ledger-v1", "attempts": {}}
        )
        if ledger.get("schema") != "breadth-two-input-attempt-ledger-v1":
            raise RuntimeError("attempt ledger schema mismatch")
        attempts = ledger["attempts"]
        if point["id"] in attempts:
            raise RuntimeError("point already consumed its one attempt")
        declared = float(point["caps"]["wall_seconds"])
        cumulative = sum(
            float(record["declared_wall_seconds"])
            for record in attempts.values()
        )
        if cumulative + declared > float(unlock["cumulative_wall_seconds"]):
            raise RuntimeError("cumulative wall budget would be exceeded")
        group = unlock["point_groups"][point["id"]]
        group_total = sum(
            float(record["declared_wall_seconds"])
            for record in attempts.values()
            if record["group"] == group
        )
        if group_total + declared > float(unlock["per_group_wall_seconds"]):
            raise RuntimeError("per-group wall budget would be exceeded")
        attempts[point["id"]] = {
            "status": "reserved",
            "group": group,
            "device": device_name,
            "declared_wall_seconds": declared,
            "reserved_utc": utc_now(),
        }
        atomic_json(ledger_path, ledger)
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    return ledger_path


def finalize_attempt(ledger_path: Path, point_id: str, status: str) -> None:
    mutex_path = ledger_path.parent / ".attempts.lock"
    with mutex_path.open("a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        ledger = json.loads(ledger_path.read_text())
        ledger["attempts"][point_id].update(
            status=status,
            ended_utc=utc_now(),
        )
        atomic_json(ledger_path, ledger)
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def configure_ieee_fp32() -> dict[str, Any]:
    torch.use_deterministic_algorithms(True)
    torch.set_float32_matmul_precision("highest")
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    if hasattr(torch.backends.cuda.matmul, "fp32_precision"):
        torch.backends.cuda.matmul.fp32_precision = "ieee"
    return {
        "float32_matmul_precision": torch.get_float32_matmul_precision(),
        "cuda_matmul_allow_tf32": bool(torch.backends.cuda.matmul.allow_tf32),
        "cuda_matmul_fp32_precision": getattr(
            torch.backends.cuda.matmul, "fp32_precision", None
        ),
        "cudnn_allow_tf32": bool(torch.backends.cudnn.allow_tf32),
        "deterministic_algorithms": bool(
            torch.are_deterministic_algorithms_enabled()
        ),
        "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
    }


def parse_cuda(name: str) -> torch.device:
    device = torch.device(name)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("production runner requires an available CUDA device")
    index = 0 if device.index is None else int(device.index)
    if index < 0 or index >= torch.cuda.device_count():
        raise RuntimeError("CUDA device index unavailable")
    torch.cuda.set_device(index)
    torch.empty(1, dtype=torch.float32, device=device)
    torch.cuda.synchronize(device)
    return device


def load_point(
    config_path: Path, point_id: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    config = json.loads(config_path.read_text())
    if set(config) != {"schema_version", "points"} or config["schema_version"] != 1:
        raise ValueError("config must have schema_version=1 and a points list")
    points = config["points"]
    identifiers = [str(point.get("id", "")) for point in points]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("point ids must be unique")
    try:
        point = points[identifiers.index(point_id)]
    except ValueError as exc:
        raise ValueError(f"unknown point id {point_id!r}") from exc
    validate_point(point)
    return config, point


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--unlock", type=Path, required=True)
    parser.add_argument("--point", required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    lock = verify_lock(args.lock.resolve(), args.config.resolve())
    config, point = load_point(args.config, args.point)
    del config
    unlock, output_root = verify_unlock(
        args.unlock.resolve(),
        args.lock.resolve(),
        args.config.resolve(),
        point,
        args.device,
        args.output_root,
    )
    numerical_mode = configure_ieee_fp32()
    device = parse_cuda(args.device)
    gpu_name = torch.cuda.get_device_name(device)
    if gpu_name not in unlock["allowed_gpu_names"]:
        raise RuntimeError("GPU model is absent from the execution unlock")
    point_dir = output_root / args.point
    if point_dir.exists():
        raise RuntimeError(f"refusing to overwrite prior point {point_dir}")
    started = time.monotonic()
    ledger_path = reserve_attempt(output_root, unlock, point, args.device)
    point_dir.mkdir(parents=True)
    manifest_path = point_dir / "manifest.json"
    arrays_path = point_dir / "arrays.npz"
    source_paths = (
        HERE / "two_input_engine.py",
        HERE / "two_input_simulator.py",
        HERE / "run_two_input_point.py",
        HERE / "run_capped_two_input.sh",
    )
    base = {
        "schema_version": 1,
        "status": "running",
        "scientific_evidence_admissible": False,
        "point_id": args.point,
        "point_config": point,
        "started_utc": utc_now(),
        "command": " ".join(shlex.quote(value) for value in sys.argv),
        "cwd": os.getcwd(),
        "config_path": str(args.config.resolve()),
        "config_sha256": sha256(args.config),
        "lock_sha256": sha256(args.lock),
        "unlock_sha256": sha256(args.unlock),
        "source_bundle_sha256": lock["bundle_sha256"],
        "source_sha256": {
            path.name: sha256(path) for path in source_paths
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": np.__version__,
            "torch": torch.__version__,
            "cuda_runtime": torch.version.cuda,
            "device": str(device),
            "gpu_name": gpu_name,
            "gpu_capability": list(torch.cuda.get_device_capability(device)),
            "numerical_mode": numerical_mode,
        },
    }
    atomic_json(manifest_path, base)

    def heartbeat(payload: dict[str, Any]) -> None:
        atomic_json(
            manifest_path,
            {**base, "heartbeat_utc": utc_now(), "heartbeat": payload},
        )

    def terminate(signum, _frame):
        raise ExternalTermination(f"received external signal {signum}")

    previous = signal.signal(signal.SIGTERM, terminate)
    try:
        arrays, diagnostics = simulate_point(
            point, device=device, progress_callback=heartbeat
        )
        temporary = arrays_path.with_suffix(".npz.tmp")
        with temporary.open("wb") as handle:
            np.savez_compressed(handle, **arrays)
        os.replace(temporary, arrays_path)
        torch.cuda.synchronize(device)
        outer_elapsed = time.monotonic() - started
        host_gib = float(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        ) / 2**20
        gpu_gib = float(torch.cuda.max_memory_allocated(device)) / 2**30
        if outer_elapsed >= float(point["caps"]["wall_seconds"]):
            raise BudgetStop("wall cap crossed during serialization")
        if host_gib > float(point["caps"]["host_rss_gib"]):
            raise BudgetStop("host cap crossed during serialization")
        if gpu_gib > float(point["caps"]["gpu_memory_gib"]):
            raise BudgetStop("GPU cap crossed during serialization")
        atomic_json(
            manifest_path,
            {
                **base,
                "status": "complete_numerically_valid_unadjudicated",
                "completed_utc": utc_now(),
                "arrays_file": arrays_path.name,
                "arrays_sha256": sha256(arrays_path),
                "diagnostics": diagnostics,
                "outer_elapsed_seconds": outer_elapsed,
                "outer_host_max_rss_gib": host_gib,
                "outer_gpu_max_allocated_gib": gpu_gib,
            },
        )
        finalize_attempt(ledger_path, point["id"], "complete")
        return 0
    except Exception as exc:
        atomic_json(
            manifest_path,
            {
                **base,
                "status": (
                    "terminated_inconclusive"
                    if isinstance(exc, ExternalTermination)
                    else "failed_inconclusive"
                ),
                "completed_utc": utc_now(),
                "exception_type": type(exc).__name__,
                "exception": str(exc),
                "point_diagnostics": getattr(exc, "point_diagnostics", {}),
                "outer_elapsed_seconds": time.monotonic() - started,
                "outer_host_max_rss_gib": float(
                    resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                )
                / 2**20,
                "outer_gpu_max_allocated_gib": float(
                    torch.cuda.max_memory_allocated(device)
                )
                / 2**30,
            },
        )
        finalize_attempt(
            ledger_path,
            point["id"],
            "terminated" if isinstance(exc, ExternalTermination) else "failed",
        )
        if isinstance(
            exc,
            (BudgetStop, NumericalInvalid, ExternalTermination),
        ):
            return 2
        raise
    finally:
        signal.signal(signal.SIGTERM, previous)


if __name__ == "__main__":
    raise SystemExit(main())
