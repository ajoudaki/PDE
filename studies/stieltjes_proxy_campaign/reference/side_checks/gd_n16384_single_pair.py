#!/usr/bin/env python3
"""Bounded FP32 Euler-GD trajectory for one n=16384 antithetic pair."""

from __future__ import annotations

import hashlib
import json
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


WIDTH = 16384
PAIR_COUNT = 1
PAIR_BATCH_SIZE = 1
SEED_BASE = 202608140200
STEP = 5.0e-6
MAX_TIME = 0.024
WALL_CAP_SECONDS = 600.0
GPU_CAP_GIB = 12.0
OUTPUT_NODES = np.asarray([0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
OUTPUT_ROOT = Path(
    "/home/amir/.codex/visualizations/2026/08/14/"
    "019fff0b-20b5-7c23-8d3e-178d14b24fdd"
)
OUTPUT_NPZ = OUTPUT_ROOT / "gd-n16384-single-pair-h5e-6.npz"
OUTPUT_JSON = OUTPUT_ROOT / "gd-n16384-single-pair-h5e-6.json"


def sha256(path: Path) -> str:
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
    """Match the existing width-series FP64 draw stream before FP32 evolution."""

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


def main() -> int:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable")
    device = torch.device("cuda:1")
    torch.cuda.set_device(device)
    total_gib = torch.cuda.get_device_properties(device).total_memory / 2**30
    torch.cuda.set_per_process_memory_fraction(GPU_CAP_GIB / total_gib, device)
    reference_engine.generate_antithetic_state = float64_draw_then_cast
    reference_engine.integrator_step = euler_step

    steps = int(round(MAX_TIME / STEP))
    point = {
        "id": "canonical_gd_n16384_single_pair_h5e-6",
        "mode": "physical",
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": SEED_BASE,
        "target": 1.0,
        "integrator": "euler",
        "microcanonical_readout": False,
        "step": STEP,
        "max_time": MAX_TIME,
        "output_nodes": OUTPUT_NODES.tolist(),
        "monotonic_tolerance": 1.0e-7,
        "loss_nonincrease_tolerance": 1.0e-7,
    }
    caps = reference_engine.PointCaps(
        wall_seconds=WALL_CAP_SECONDS,
        max_steps=steps,
        host_rss_gib=12.0,
        gpu_memory_gib=GPU_CAP_GIB,
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
        absolute_wall_deadline=started + WALL_CAP_SECONDS,
    )
    elapsed = time.monotonic() - started
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(OUTPUT_NPZ, **arrays)
    payload = {
        "schema_version": 1,
        "status": "complete_exploratory_single_pair",
        "claim_scope": (
            "one n=16384 antithetic pair under FP32 Euler GD; sampling and "
            "FP32 update error are unresolved"
        ),
        "started_utc": started_utc,
        "ended_utc": datetime.now(timezone.utc).isoformat(),
        "device": "cuda:1",
        "dtype": "float32",
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": SEED_BASE,
        "rescaled_step_h": STEP,
        "ordinary_loss_learning_rate_nh": WIDTH * STEP,
        "max_time": MAX_TIME,
        "wall_cap_seconds": WALL_CAP_SECONDS,
        "gpu_memory_cap_gib": GPU_CAP_GIB,
        "elapsed_seconds": elapsed,
        "peak_gpu_allocated_gib": torch.cuda.max_memory_allocated(device) / 2**30,
        "diagnostics": diagnostics,
        "output_nodes": arrays["output_nodes"].tolist(),
        "effective_kernel_at_nodes": arrays["effective_kernel"].tolist(),
        "mean_direct_kernel_at_nodes": arrays["mean_direct_kernel"].tolist(),
        "physical_time_at_nodes": arrays["physical_time_at_nodes"].tolist(),
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
