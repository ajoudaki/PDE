#!/usr/bin/env python3
"""One-shot, non-scientific GPU preflight for the locked FP64 successor."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys

os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_local_qualification as local


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--device", required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    if args.config.resolve() != (repo / local.CONFIG_RELATIVE).resolve():
        raise RuntimeError("configuration is not the canonical successor file")
    if args.lock.resolve() != (repo / local.LOCK_RELATIVE).resolve():
        raise RuntimeError("source lock is not the canonical successor file")
    frozen = local.read_json(args.config)
    lock = local.read_json(args.lock)
    if lock.get("schema") != "breadth-fp64-local-lock-v1" or lock.get("status") != "frozen":
        raise RuntimeError("invalid source lock")
    files = lock.get("files", {})
    if set(files) != local.REQUIRED_LOCKED_FILES:
        raise RuntimeError("source lock does not contain the canonical dependency set")
    if lock.get("bundle_sha256") != local.source_bundle_sha256(files):
        raise RuntimeError("source-lock bundle digest is invalid")
    for relative, expected in files.items():
        if local.sha256_file(repo / relative) != expected:
            raise RuntimeError(f"source-lock mismatch for {relative}")
    expected_watchdog = (
        f"preflight:preflight:"
        f"{int(frozen['external_watchdogs']['gpu_preflight_seconds'])}"
    )
    if os.environ.get("FP64_WATCHDOG_ACTIVE") != expected_watchdog:
        raise RuntimeError("GPU preflight must run under the frozen external watchdog")
    output = Path(__file__).resolve().parent / "GPU_PREFLIGHT.json"
    attempt_path = Path(__file__).resolve().parent / "GPU_PREFLIGHT_ATTEMPT.json"
    if output.exists():
        raise RuntimeError("the one-shot GPU preflight result already exists")
    attempt = {
        "schema": "breadth-fp64-gpu-preflight-attempt-v1",
        "status": "running",
        "device": args.device,
        "watchdog": expected_watchdog,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "lock_sha256": local.sha256_file(args.lock),
        "config_sha256": local.sha256_file(args.config),
    }
    descriptor = os.open(attempt_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(json.dumps(attempt, indent=2, sort_keys=True) + "\n")

    original_excepthook = sys.excepthook

    def record_uncaught(exc_type, exc_value, exc_traceback):
        attempt.update(
            status="failed",
            ended_utc=datetime.now(timezone.utc).isoformat(),
            error_type=exc_type.__name__,
            error=str(exc_value),
        )
        local.write_json_atomic(attempt_path, attempt)
        original_excepthook(exc_type, exc_value, exc_traceback)

    sys.excepthook = record_uncaught
    device = torch.device(args.device)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("CUDA preflight requires an available CUDA device")
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")
    runner = local.load_fp64_runner(repo, frozen)
    point = {
        "key": "fp64_gpu_preflight",
        "purpose": "unit_test",
        "configuration": "centered_c1",
        "width": 32,
        "step": 1e-5,
        "max_time": 4e-5,
        "lineage_start": 0,
        "lineage_stop": 1,
        "prefix_sizes": [32],
        "rng_row_block": 16,
        "w_monitor_size": 32,
        "w_monitor_extent": 32,
        "w_monitor_seed": 2026081701,
        "diagnostic_stride": 1,
        "wall_sync_stride": 1,
        "caps": {
            "wall_seconds": 20,
            "max_steps_all_lineages": 4,
            "gpu_memory_gib": 1,
            "host_rss_gib": 2,
            "kernel_ceiling": 1e6,
            "state_ceiling": 1e4,
        },
    }
    runs = [runner.run_point(point, seed=2026081702, device=device) for _ in range(2)]
    fields = ("raw_output", "raw_kernel", "raw_weighted_kernel", "update_w_cosine")
    deterministic = all(
        np.array_equal(runs[0][0][field], runs[1][0][field]) for field in fields
    )
    dtype_ok = all(runs[0][0][field].dtype == np.float64 for field in fields)
    init = runs[0][1]["lineages"][0]["initialization"]
    initialization_ok = bool(
        init.get("dynamics_dtype") == "float64"
        and init.get("initialization_bytes")
        == "frozen-fp32-cast-exactly-to-fp64"
        and runs[0][1]["lineages"][0]["initialization"]
        == runs[1][1]["lineages"][0]["initialization"]
    )
    deterministic_mode = bool(
        torch.are_deterministic_algorithms_enabled()
        and not torch.backends.cuda.matmul.allow_tf32
        and not torch.backends.cudnn.allow_tf32
        and os.environ.get("CUBLAS_WORKSPACE_CONFIG") == ":4096:8"
    )
    resource_ok = bool(
        max(run[1]["max_gpu_allocated_gib"] for run in runs)
        <= point["caps"]["gpu_memory_gib"]
        and max(run[1]["max_host_rss_gib"] for run in runs)
        <= point["caps"]["host_rss_gib"]
        and max(run[1]["elapsed_seconds"] for run in runs)
        <= point["caps"]["wall_seconds"]
    )
    state_digest = hashlib.sha256(
        b"".join(np.ascontiguousarray(runs[0][0][field]).tobytes() for field in fields)
    ).hexdigest()
    result = {
        "schema": "breadth-fp64-gpu-preflight-v1",
        "status": (
            "pass"
            if deterministic and dtype_ok and initialization_ok and deterministic_mode and resource_ok
            else "fail"
        ),
        "device": args.device,
        "gpu_name": torch.cuda.get_device_name(device),
        "gpu_identity": local.cuda_identity(args.device),
        "torch_version": torch.__version__,
        "cuda_version": torch.version.cuda,
        "deterministic_replay": deterministic,
        "float64_arrays": dtype_ok,
        "initialization_ok": initialization_ok,
        "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
        "tf32_matmul": bool(torch.backends.cuda.matmul.allow_tf32),
        "tf32_cudnn": bool(torch.backends.cudnn.allow_tf32),
        "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
        "external_watchdog": expected_watchdog,
        "resource_caps_pass": resource_ok,
        "dynamics_dtype": init.get("dynamics_dtype"),
        "initialization_contract": init.get("initialization_bytes"),
        "sample_output_digest": state_digest,
        "max_gpu_allocated_gib": max(run[1]["max_gpu_allocated_gib"] for run in runs),
        "max_host_rss_gib": max(run[1]["max_host_rss_gib"] for run in runs),
        "lock_sha256": local.sha256_file(args.lock),
        "config_sha256": local.sha256_file(args.config),
    }
    local.write_json(output, result)
    attempt.update(
        status=result["status"],
        ended_utc=datetime.now(timezone.utc).isoformat(),
        result_sha256=local.sha256_file(output),
    )
    local.write_json_atomic(attempt_path, attempt)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
