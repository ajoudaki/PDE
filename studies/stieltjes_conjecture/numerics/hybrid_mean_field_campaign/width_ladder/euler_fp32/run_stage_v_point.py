#!/usr/bin/env python3
"""Fail-closed, one-attempt runner for the two locked Stage-V points."""

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

# Required by deterministic CUDA GEMM before the first CUDA context is made.
# Override ambient state: the numerical mode is part of the frozen experiment.
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
import torch

from euler_engine import BudgetStop, NumericalInvalid, run_point


HERE = Path(__file__).resolve().parent
CONFIG = HERE / "configs" / "FROZEN_STAGE_V.json"
LOCK = HERE / "FROZEN_STAGE_V_MANIFEST.json"
UNLOCK = HERE / "STAGE_V_UNLOCK.json"
RUN_ROOT = HERE / "runs" / "stage_v"
LEDGER = HERE / ".runtime" / "stage_v_attempts.json"
LEDGER_LOCK = HERE / ".runtime" / "stage_v_attempts.lock"


class ExternalTermination(RuntimeError):
    pass


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


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


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


def validate_lock() -> tuple[dict[str, Any], str]:
    if not LOCK.is_file():
        raise RuntimeError("Stage V is source-locked only after hostile audit")
    lock = load_json(LOCK)
    if lock.get("status") != "frozen_after_hostile_audit":
        raise RuntimeError("Stage-V source lock lacks hostile-audit disposition")
    for relative, expected in lock.get("files", {}).items():
        path = HERE / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"locked source mismatch: {relative}")
    if lock["parent_protocol_sha256"] != load_json(CONFIG)[
        "parent_protocol_sha256"
    ]:
        raise RuntimeError("parent-protocol binding mismatch")
    return lock, sha256(LOCK)


def validate_unlock(lock_sha: str) -> dict[str, Any]:
    if not UNLOCK.is_file():
        raise RuntimeError("Stage V has no execution unlock")
    unlock = load_json(UNLOCK)
    if unlock.get("status") != "authorized_stage_v_only":
        raise RuntimeError("unlock does not authorize Stage V")
    if unlock.get("frozen_manifest_sha256") != lock_sha:
        raise RuntimeError("unlock does not bind the current source lock")
    if unlock.get("config_sha256") != sha256(CONFIG):
        raise RuntimeError("unlock does not bind the frozen config")
    if (HERE / unlock.get("run_root", "")).resolve() != RUN_ROOT.resolve():
        raise RuntimeError("unlock does not bind the fixed run root")
    return unlock


def parse_device(name: str) -> torch.device:
    device = torch.device(name)
    if device.type != "cuda":
        raise RuntimeError("locked Stage V requires one CUDA GPU lineage")
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable")
    index = 0 if device.index is None else int(device.index)
    if index < 0 or index >= torch.cuda.device_count():
        raise RuntimeError("CUDA device index unavailable")
    torch.cuda.set_device(index)
    torch.empty(1, dtype=torch.float32, device=device)
    torch.cuda.synchronize(device)
    return device


def environment(device: torch.device, numerical: dict[str, Any]) -> dict[str, Any]:
    return {
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "torch": torch.__version__,
        "cuda_runtime": torch.version.cuda,
        "device": str(device),
        "gpu_name": torch.cuda.get_device_name(device),
        "gpu_capability": list(torch.cuda.get_device_capability(device)),
        "numerical_mode": numerical,
    }


def reserve_attempt(point_id: str) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER_LOCK.open("a+") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        ledger = load_json(LEDGER) if LEDGER.is_file() else {"attempts": {}}
        if point_id in ledger["attempts"]:
            raise RuntimeError(f"point {point_id} already consumed its only attempt")
        ledger["attempts"][point_id] = {"reserved_utc": utc_now()}
        atomic_json(LEDGER, ledger)


def validate_predecessor(point_id: str, lock_sha: str) -> None:
    if point_id != "v_n8192_h5e6":
        return
    path = RUN_ROOT / "v_n8192_h1e5" / "manifest.json"
    if not path.is_file():
        raise RuntimeError("fine point requires completed coarse point")
    manifest = load_json(path)
    if manifest.get("status") != "complete_validation_valid":
        raise RuntimeError("coarse predecessor is not valid")
    if manifest.get("frozen_manifest_sha256") != lock_sha:
        raise RuntimeError("coarse predecessor used a different source lock")


def finalize_timeout(point_id: str) -> int:
    path = RUN_ROOT / point_id / "manifest.json"
    if not path.is_file():
        return 0
    manifest = load_json(path)
    if manifest.get("status") == "running":
        manifest.update(
            status="failed_inconclusive_external_timeout",
            completed_utc=utc_now(),
            scientific_evidence_admissible=False,
            outer_failure_telemetry={
                "reason": "external timeout or forced termination",
                "host_max_rss_gib": float(
                    resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
                )
                / 2**20,
            },
        )
        atomic_json(path, manifest)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--point", required=True)
    parser.add_argument("--device")
    parser.add_argument("--finalize-timeout", action="store_true")
    args = parser.parse_args()
    if args.finalize_timeout:
        return finalize_timeout(args.point)

    config = load_json(CONFIG)
    points = {point["id"]: point for point in config["points"]}
    if args.point not in points:
        raise ValueError("only the two frozen Stage-V point IDs are accepted")
    lock, lock_sha = validate_lock()
    unlock = validate_unlock(lock_sha)
    if args.point not in unlock.get("authorized_point_ids", []):
        raise RuntimeError("unlock does not authorize this point")
    if args.device is None:
        raise RuntimeError("--device is required")
    numerical = configure_ieee_fp32()
    device = parse_device(args.device)
    validate_predecessor(args.point, lock_sha)

    point = points[args.point]
    point_dir = RUN_ROOT / args.point
    if point_dir.exists():
        raise RuntimeError("refusing to overwrite a prior Stage-V attempt")
    reserve_attempt(args.point)
    point_dir.mkdir(parents=True)
    manifest_path = point_dir / "manifest.json"
    arrays_path = point_dir / "arrays.npz"
    started = time.monotonic()
    base = {
        "schema_version": 1,
        "status": "running",
        "point_id": args.point,
        "point_config": point,
        "target": 1.0,
        "started_utc": utc_now(),
        "command": " ".join(shlex.quote(value) for value in sys.argv),
        "cwd": os.getcwd(),
        "config_sha256": sha256(CONFIG),
        "protocol_sha256": sha256(HERE / "PROTOCOL.md"),
        "frozen_manifest_sha256": lock_sha,
        "unlock_sha256": sha256(UNLOCK),
        "environment": environment(device, numerical),
        "scientific_evidence_admissible": False,
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
        arrays, diagnostics = run_point(
            point,
            seed=int(config["seed"]),
            device=device,
            progress_callback=heartbeat,
        )
        temporary = arrays_path.with_suffix(".npz.tmp")
        with temporary.open("wb") as handle:
            np.savez_compressed(handle, **arrays)
        os.replace(temporary, arrays_path)
        atomic_json(
            manifest_path,
            {
                **base,
                "status": "complete_validation_valid",
                "completed_utc": utc_now(),
                "diagnostics": diagnostics,
                "arrays_file": arrays_path.name,
                "arrays_sha256": sha256(arrays_path),
            },
        )
        return 0
    except Exception as exc:
        atomic_json(
            manifest_path,
            {
                **base,
                "status": "failed_inconclusive",
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
        if isinstance(exc, (BudgetStop, NumericalInvalid, ExternalTermination)):
            return 2
        raise
    finally:
        signal.signal(signal.SIGTERM, previous)


if __name__ == "__main__":
    raise SystemExit(main())
