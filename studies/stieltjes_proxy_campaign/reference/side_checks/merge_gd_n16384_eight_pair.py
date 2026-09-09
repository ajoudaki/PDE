#!/usr/bin/env python3
"""Merge two completed n=16384 shards from raw trajectories."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


OUTPUT_ROOT = Path(
    "/home/amir/.codex/visualizations/2026/08/14/"
    "019fff0b-20b5-7c23-8d3e-178d14b24fdd"
)
INPUT_NPZ = [
    OUTPUT_ROOT / "gd-n16384-eight-pair-shard0.npz",
    OUTPUT_ROOT / "gd-n16384-eight-pair-shard1.npz",
]
INPUT_JSON = [
    OUTPUT_ROOT / "gd-n16384-eight-pair-shard0.json",
    OUTPUT_ROOT / "gd-n16384-eight-pair-shard1.json",
]
OUTPUT_NPZ = OUTPUT_ROOT / "gd-n16384-eight-pair-h5e-6.npz"
OUTPUT_JSON = OUTPUT_ROOT / "gd-n16384-eight-pair-h5e-6.json"
OUTPUT_NODES = np.asarray([0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def interpolate_rows(x: np.ndarray, rows: np.ndarray) -> np.ndarray:
    return np.vstack(
        [np.interp(OUTPUT_NODES, x, rows[:, j]) for j in range(rows.shape[1])]
    ).T


def main() -> int:
    if OUTPUT_NPZ.exists() or OUTPUT_JSON.exists():
        raise FileExistsError("no-overwrite gate: merged output already exists")
    metadata = [json.loads(path.read_text()) for path in INPUT_JSON]
    if any(item.get("status") != "complete_exploratory_shard" for item in metadata):
        raise RuntimeError("both shards must be complete")
    shards = [np.load(path) for path in INPUT_NPZ]
    raw_time = np.asarray(shards[0]["raw_time"], dtype=np.float64)
    if not np.array_equal(raw_time, shards[1]["raw_time"]):
        raise RuntimeError("shard time grids differ")

    trajectory_output = np.concatenate(
        [item["raw_trajectory_output"] for item in shards], axis=1
    )
    trajectory_kernel = np.concatenate(
        [item["raw_trajectory_kernel"] for item in shards], axis=1
    )
    trajectory_weighted = np.concatenate(
        [item["raw_trajectory_weighted_kernel"] for item in shards], axis=1
    )
    trajectory_loss = np.concatenate(
        [item["raw_trajectory_loss"] for item in shards], axis=1
    )
    if trajectory_output.shape[1] != 16:
        raise RuntimeError("expected 16 trajectories from eight antithetic pairs")

    mean_output = trajectory_output.mean(axis=1)
    mean_loss = trajectory_loss.mean(axis=1)
    loss_of_mean_output = np.square(1.0 - mean_output)
    mean_effective_kernel = trajectory_weighted.mean(axis=1) / (1.0 - mean_output)
    keep = np.concatenate(([True], np.diff(mean_output) > 0.0))
    x = mean_output[keep]
    if OUTPUT_NODES[-1] > x[-1] + 1.0e-7:
        raise RuntimeError("merged curve did not reach the final output node")
    node_time = np.interp(OUTPUT_NODES, x, raw_time[keep])
    node_output = interpolate_rows(x, trajectory_output[keep])
    node_kernel = interpolate_rows(x, trajectory_kernel[keep])
    node_weighted = interpolate_rows(x, trajectory_weighted[keep])
    node_loss = interpolate_rows(x, trajectory_loss[keep])
    effective_kernel = node_weighted.mean(axis=1) / (1.0 - OUTPUT_NODES)
    direct_kernel = node_kernel.mean(axis=1)
    node_mean_loss = node_loss.mean(axis=1)
    node_loss_of_mean = np.square(1.0 - OUTPUT_NODES)

    arrays = {
        "raw_time": raw_time,
        "raw_mean_output": mean_output,
        "raw_mean_loss": mean_loss,
        "raw_loss_of_mean_output": loss_of_mean_output,
        "raw_mean_effective_kernel": mean_effective_kernel,
        "raw_trajectory_output": trajectory_output,
        "raw_trajectory_kernel": trajectory_kernel,
        "raw_trajectory_weighted_kernel": trajectory_weighted,
        "raw_trajectory_loss": trajectory_loss,
        "output_nodes": OUTPUT_NODES,
        "physical_time_at_nodes": node_time,
        "effective_kernel": effective_kernel,
        "mean_direct_kernel": direct_kernel,
        "mean_loss": node_mean_loss,
        "loss_of_mean_output": node_loss_of_mean,
        "node_raw_output": node_output,
        "node_raw_kernel": node_kernel,
        "node_raw_weighted_kernel": node_weighted,
        "node_raw_loss": node_loss,
    }
    np.savez_compressed(OUTPUT_NPZ, **arrays)
    payload = {
        "schema_version": 1,
        "status": "complete_exploratory_eight_pair_merge",
        "claim_scope": (
            "eight n=16384 antithetic pairs under FP32 Euler GD; raw shard "
            "trajectories merged before output-coordinate interpolation"
        ),
        "width": 16384,
        "antithetic_pairs": 8,
        "trajectory_count": 16,
        "dtype": "float32",
        "rescaled_step_h": 5.0e-6,
        "max_time": 0.024,
        "output_nodes": OUTPUT_NODES.tolist(),
        "effective_kernel_at_nodes": effective_kernel.tolist(),
        "mean_direct_kernel_at_nodes": direct_kernel.tolist(),
        "physical_time_at_nodes": node_time.tolist(),
        "mean_physical_loss_at_nodes": node_mean_loss.tolist(),
        "loss_of_mean_output_at_nodes": node_loss_of_mean.tolist(),
        "loss_jensen_gap_at_nodes": (node_mean_loss - node_loss_of_mean).tolist(),
        "maximum_loss_jensen_gap": float(
            np.max(node_mean_loss - node_loss_of_mean)
        ),
        "terminal_mean_output": float(mean_output[-1]),
        "minimum_mean_output_increment": float(np.min(np.diff(mean_output))),
        "maximum_mean_loss_increment": float(np.max(np.diff(mean_loss))),
        "shards": [
            {
                "json": str(json_path),
                "json_sha256": sha256(json_path),
                "npz": str(npz_path),
                "npz_sha256": sha256(npz_path),
                "elapsed_seconds": item["elapsed_seconds"],
                "peak_gpu_allocated_gib": item["peak_gpu_allocated_gib"],
                "first_step_fp32_rounding": item["first_step_fp32_rounding"],
            }
            for json_path, npz_path, item in zip(INPUT_JSON, INPUT_NPZ, metadata)
        ],
        "npz": str(OUTPUT_NPZ),
        "npz_sha256": sha256(OUTPUT_NPZ),
        "script": str(Path(__file__).resolve()),
        "script_sha256": sha256(Path(__file__).resolve()),
        "terminal_stop_no_retry": True,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
