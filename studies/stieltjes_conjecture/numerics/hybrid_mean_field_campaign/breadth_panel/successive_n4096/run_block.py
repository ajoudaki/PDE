#!/usr/bin/env python3
"""Run one existing 8-lineage n=4096 block with the validated FP64 engine."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
from typing import Any

os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"

import numpy as np
import torch


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
FP64_DIR = HERE.parent / "fp64_successor"
if str(FP64_DIR) not in sys.path:
    sys.path.insert(0, str(FP64_DIR))

import run_local_qualification as fp64  # noqa: E402


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"{path} is not a JSON object")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--configuration", choices=("C", "A", "M", "V"), required=True)
    parser.add_argument("--lineage-start", type=int, required=True)
    parser.add_argument("--lineage-stop", type=int, required=True)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()

    config_path = HERE / "CONFIG.json"
    config = read_json(config_path)
    block = [args.lineage_start, args.lineage_stop]
    if block not in config["lineage_blocks"]:
        raise RuntimeError("lineage interval is not one of the existing frozen 8-lineage blocks")
    if args.device != "cuda:0":
        raise RuntimeError("this campaign uses the already validated cuda:0 FP64 environment")
    device = torch.device(args.device)
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable")

    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")

    fp64_config_path = FP64_DIR / "FROZEN_LOCAL_QUALIFICATION.json"
    fp64_config = read_json(fp64_config_path)
    runner = fp64.load_fp64_runner(REPO, fp64_config)
    spec = config["configurations"][args.configuration]
    steps = int(round(float(spec["max_time"]) / float(config["step"])))
    lineages = args.lineage_stop - args.lineage_start
    point = {
        "key": f"{args.configuration}_n4096_L{args.lineage_start}_{args.lineage_stop}",
        "purpose": "width_screen",
        "configuration": spec["engine_key"],
        "width": int(config["width"]),
        "step": float(config["step"]),
        "max_time": float(spec["max_time"]),
        "lineage_start": args.lineage_start,
        "lineage_stop": args.lineage_stop,
        "prefix_sizes": [2048, 4096],
        "rng_row_block": 128,
        "w_monitor_size": 4096,
        "w_monitor_extent": 2048,
        "w_monitor_seed": int(spec["monitor_seed"]),
        "diagnostic_stride": 256,
        "wall_sync_stride": 32,
        "caps": {
            "wall_seconds": float(
                config["point_caps"]["wall_seconds_per_8_lineage_block"]
            ),
            "max_steps_all_lineages": steps * lineages,
            "gpu_memory_gib": float(config["point_caps"]["gpu_memory_gib"]),
            "host_rss_gib": float(config["point_caps"]["host_rss_gib"]),
            "kernel_ceiling": float(config["point_caps"]["kernel_ceiling"]),
            "state_ceiling": float(config["point_caps"]["state_ceiling"]),
        },
    }
    output = HERE / "runs" / point["key"]
    output.mkdir(parents=True, exist_ok=False)
    started = datetime.now(timezone.utc).isoformat()
    arrays, diagnostics = runner.run_point(
        point,
        seed=int(config["seed"]),
        device=device,
    )
    arrays["array_schema_version"] = np.asarray(
        b"breadth-successive-fp64-arrays-v1", dtype="S48"
    )
    arrays["dynamics_dtype"] = np.asarray(b"float64", dtype="S16")
    arrays["initialization_contract"] = np.asarray(
        b"frozen-fp32-cast-exactly-to-fp64", dtype="S48"
    )
    arrays_path = output / "arrays.npz"
    np.savez_compressed(arrays_path, **arrays)
    lock_path = FP64_DIR / "FROZEN_LOCAL_QUALIFICATION_LOCK.json"
    manifest = {
        "schema": "breadth-successive-n4096-block-result-v1",
        "status": "complete",
        "configuration": args.configuration,
        "point": point,
        "seed": config["seed"],
        "device": args.device,
        "gpu_identity": fp64.cuda_identity(args.device),
        "torch_version": torch.__version__,
        "cuda_version": torch.version.cuda,
        "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
        "tf32_matmul": bool(torch.backends.cuda.matmul.allow_tf32),
        "tf32_cudnn": bool(torch.backends.cudnn.allow_tf32),
        "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
        "started_utc": started,
        "ended_utc": datetime.now(timezone.utc).isoformat(),
        "diagnostics": diagnostics,
        "arrays_file": "arrays.npz",
        "arrays_sha256": sha256_file(arrays_path),
        "provenance": {
            "campaign_config_sha256": sha256_file(config_path),
            "run_script_sha256": sha256_file(Path(__file__)),
            "validated_fp64_config_sha256": sha256_file(fp64_config_path),
            "validated_fp64_source_lock_sha256": sha256_file(lock_path),
            "validated_fp64_source_bundle_sha256": read_json(lock_path)["bundle_sha256"],
            "command": sys.argv,
        },
    }
    manifest_path = output / "MANIFEST.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "configuration": args.configuration,
                "lineages": block,
                "elapsed_seconds": diagnostics["elapsed_seconds"],
                "max_gpu_allocated_gib": diagnostics["max_gpu_allocated_gib"],
                "arrays_sha256": manifest["arrays_sha256"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
