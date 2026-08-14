#!/usr/bin/env python3
"""One bounded matched n=8192 Euler-GD point against the frozen FP32 RK4 run."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch


HERE = Path(__file__).resolve().parent
REFERENCE = HERE.parent
sys.path.insert(0, str(REFERENCE))

import canonical_model  # noqa: E402
import reference_engine  # noqa: E402


WIDTH = 8192
PAIR_COUNT = 8
PAIR_BATCH_SIZE = 2
SEED_BASE = 202608140200
MAX_TIME = 0.024
OUTPUT_NODES = np.asarray([0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
REFERENCE_NPZ = REFERENCE / (
    "runs/canonical_n8192_r8_fp32_holdout_20260814/"
    "canonical_physical_n8192_r8_fp32_holdout.npz"
)
OUTPUT_ROOT = Path(
    "/home/amir/.codex/visualizations/2026/08/14/"
    "019fff0b-20b5-7c23-8d3e-178d14b24fdd"
)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


_original_generator = canonical_model.generate_antithetic_state


def float64_draw_then_cast(
    width: int,
    pair_count: int,
    seed_base: int,
    *,
    device: torch.device,
    dtype: torch.dtype,
    pair_offset: int = 0,
    microcanonical_readout: bool = False,
):
    state64, init64 = _original_generator(
        width,
        pair_count,
        seed_base,
        device=device,
        dtype=torch.float64,
        pair_offset=pair_offset,
        microcanonical_readout=microcanonical_readout,
    )
    state32 = canonical_model.State(
        state64.a.float(), state64.W.float(), state64.u.float()
    )
    initial32 = canonical_model.observables(state32)
    return state32, {
        "initial_output": initial32.output,
        "initial_kernel": initial32.kernel,
        "projection_relative_norm": init64["projection_relative_norm"].float(),
    }


def euler_step(
    state: canonical_model.State,
    step: float,
    *,
    mode: str,
    method: str,
    target: float,
    kernel_floor: float,
) -> canonical_model.State:
    if method != "euler":
        raise ValueError(method)
    tangent, _ = canonical_model.scaled_rhs(
        state, mode, target=target, kernel_floor=kernel_floor
    )
    return canonical_model.add_scaled(state, tangent, step)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", type=float, required=True, choices=(5.0e-6, 2.5e-6))
    parser.add_argument("--device", required=True, choices=("cuda:0", "cuda:1"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    step = float(args.step)
    wall_cap = 600.0 if step == 5.0e-6 else 1200.0
    device = torch.device(args.device)
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable")
    torch.cuda.set_device(device)
    reference_engine.generate_antithetic_state = float64_draw_then_cast
    reference_engine.integrator_step = euler_step
    steps_per_batch = int(round(MAX_TIME / step))
    batch_count = math.ceil(PAIR_COUNT / PAIR_BATCH_SIZE)
    point = {
        "id": f"canonical_gd_n8192_r8_h{step:.1e}",
        "mode": "physical",
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": SEED_BASE,
        "target": 1.0,
        "integrator": "euler",
        "microcanonical_readout": False,
        "step": step,
        "max_time": MAX_TIME,
        "output_nodes": OUTPUT_NODES.tolist(),
        "monotonic_tolerance": 1.0e-7,
        "loss_nonincrease_tolerance": 1.0e-7,
    }
    caps = reference_engine.PointCaps(
        wall_seconds=wall_cap,
        max_steps=steps_per_batch * batch_count,
        host_rss_gib=12.0,
        gpu_memory_gib=10.0,
        state_ceiling=10_000.0,
        kernel_ceiling=1.0e10,
        kernel_floor=1.0e-10,
        diagnostic_stride=25,
    )
    started_utc = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(device)
    arrays, diagnostics = reference_engine.run_point(
        point,
        device=device,
        dtype=torch.float32,
        caps=caps,
        absolute_wall_deadline=started + wall_cap,
    )
    reference = np.load(REFERENCE_NPZ)
    kernel = arrays["effective_kernel"]
    kernel_ref = reference["effective_kernel"]
    direct = arrays["mean_direct_kernel"]
    direct_ref = reference["mean_direct_kernel"]
    kernel_rel = np.abs(kernel - kernel_ref) / np.maximum(np.abs(kernel_ref), 1e-30)
    direct_rel = np.abs(direct - direct_ref) / np.maximum(
        np.abs(direct_ref), 1e-30
    )
    common_time = np.linspace(0.0, MAX_TIME, 241)
    output = np.interp(common_time, arrays["raw_time"], arrays["raw_mean_output"])
    output_ref = np.interp(
        common_time, reference["raw_time"], reference["raw_mean_output"]
    )
    index_09 = int(np.flatnonzero(np.isclose(OUTPUT_NODES, 0.9))[0])
    payload = {
        "schema_version": 1,
        "status": "complete_validation_only",
        "claim_scope": "matched Euler-GD discretization versus frozen n=8192 FP32 RK4",
        "started_utc": started_utc,
        "ended_utc": datetime.now(timezone.utc).isoformat(),
        "device": args.device,
        "dtype": "float32",
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": SEED_BASE,
        "rescaled_step_h": step,
        "ordinary_loss_learning_rate_nh": WIDTH * step,
        "wall_cap_seconds": wall_cap,
        "gpu_memory_cap_gib": 10.0,
        "elapsed_seconds": time.monotonic() - started,
        "peak_gpu_allocated_gib": torch.cuda.max_memory_allocated(device) / 2**30,
        "diagnostics": diagnostics,
        "output_nodes": OUTPUT_NODES.tolist(),
        "effective_kernel_at_nodes": kernel.tolist(),
        "rk4_effective_kernel_at_nodes": kernel_ref.tolist(),
        "metrics": {
            "max_relative_effective_kernel_error": float(np.max(kernel_rel)),
            "relative_effective_kernel_error_at_y_0p9": float(kernel_rel[index_09]),
            "effective_kernel_at_y_0p9": float(kernel[index_09]),
            "rk4_effective_kernel_at_y_0p9": float(kernel_ref[index_09]),
            "max_relative_direct_kernel_error": float(np.max(direct_rel)),
            "max_absolute_hitting_time_error": float(
                np.max(
                    np.abs(
                        arrays["physical_time_at_nodes"]
                        - reference["physical_time_at_nodes"]
                    )
                )
            ),
            "max_absolute_mean_output_error_at_common_times": float(
                np.max(np.abs(output - output_ref))
            ),
            "terminal_mean_output": float(arrays["raw_mean_output"][-1]),
        },
        "reference_npz": str(REFERENCE_NPZ),
        "reference_npz_sha256": file_sha256(REFERENCE_NPZ),
        "script": str(Path(__file__).resolve()),
        "script_sha256": file_sha256(Path(__file__).resolve()),
    }
    suffix = "5e-6" if step == 5.0e-6 else "2p5e-6"
    output_path = OUTPUT_ROOT / f"gd-vs-rk4-n8192-h{suffix}.json"
    output_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
