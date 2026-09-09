#!/usr/bin/env python3
"""Matched-initialization Euler-GD versus RK4 gradient-flow check at n=4096.

This is an isolated side-conversation validation script.  It does not modify
the frozen reference runner or any prior scientific artifact.
"""

from __future__ import annotations

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


WIDTH = 4096
PAIR_COUNT = 8
PAIR_BATCH_SIZE = 4
SEED_BASE = 202608140200
TARGET = 1.0
MAX_TIME = 0.024
OUTPUT_NODES = np.asarray([0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
STEPS = (2.0e-5, 1.0e-5, 5.0e-6)
TOTAL_WALL_CAP_SECONDS = 300.0
POINT_WALL_CAP_SECONDS = 180.0

REFERENCE_NPZ = REFERENCE / (
    "runs/canonical_n4096_r8_fp32_cast_control_20260814/"
    "canonical_physical_n4096_r8_fp32_cast_control.npz"
)
OUTPUT_JSON = Path(
    "/home/amir/.codex/visualizations/2026/08/14/"
    "019fff0b-20b5-7c23-8d3e-178d14b24fdd/"
    "gd-vs-rk4-n4096-result.json"
)


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
    """Reproduce the historical FP64 Gaussian stream, then evolve in FP32."""

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
        state64.a.to(dtype=torch.float32),
        state64.W.to(dtype=torch.float32),
        state64.u.to(dtype=torch.float32),
    )
    initial32 = canonical_model.observables(state32)
    return state32, {
        "initial_output": initial32.output,
        "initial_kernel": initial32.kernel,
        "projection_relative_norm": init64["projection_relative_norm"].to(
            dtype=torch.float32
        ),
    }


def euler_integrator_step(
    state: canonical_model.State,
    step: float,
    *,
    mode: str,
    method: str,
    target: float,
    kernel_floor: float,
) -> canonical_model.State:
    if method != "euler":
        raise ValueError(f"isolated validation expects Euler, got {method!r}")
    tangent, _ = canonical_model.scaled_rhs(
        state, mode, target=target, kernel_floor=kernel_floor
    )
    return canonical_model.add_scaled(state, tangent, step)


def point(step: float) -> dict[str, object]:
    return {
        "id": f"canonical_gd_n4096_r8_h{step:.0e}",
        "mode": "physical",
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": SEED_BASE,
        "target": TARGET,
        "integrator": "euler",
        "microcanonical_readout": False,
        "step": step,
        "max_time": MAX_TIME,
        "output_nodes": OUTPUT_NODES.tolist(),
        "monotonic_tolerance": 1.0e-7,
        "loss_nonincrease_tolerance": 1.0e-7,
    }


def caps(step: float) -> reference_engine.PointCaps:
    steps_per_batch = int(round(MAX_TIME / step))
    batch_count = math.ceil(PAIR_COUNT / PAIR_BATCH_SIZE)
    return reference_engine.PointCaps(
        wall_seconds=POINT_WALL_CAP_SECONDS,
        max_steps=steps_per_batch * batch_count,
        host_rss_gib=12.0,
        gpu_memory_gib=22.5,
        state_ceiling=10_000.0,
        kernel_ceiling=1.0e10,
        kernel_floor=1.0e-10,
        diagnostic_stride=25,
    )


def node_metrics(
    arrays: dict[str, np.ndarray], reference: np.lib.npyio.NpzFile
) -> dict[str, object]:
    k = arrays["effective_kernel"]
    k_ref = reference["effective_kernel"]
    direct = arrays["mean_direct_kernel"]
    direct_ref = reference["mean_direct_kernel"]
    times = arrays["physical_time_at_nodes"]
    times_ref = reference["physical_time_at_nodes"]
    k_rel = np.abs(k - k_ref) / np.maximum(np.abs(k_ref), 1.0e-30)
    direct_rel = np.abs(direct - direct_ref) / np.maximum(
        np.abs(direct_ref), 1.0e-30
    )
    index_09 = int(np.flatnonzero(np.isclose(OUTPUT_NODES, 0.9))[0])

    common_time = np.linspace(0.0, MAX_TIME, 241)
    y = np.interp(common_time, arrays["raw_time"], arrays["raw_mean_output"])
    y_ref = np.interp(
        common_time, reference["raw_time"], reference["raw_mean_output"]
    )
    return {
        "effective_kernel_at_nodes": k.tolist(),
        "max_relative_effective_kernel_error": float(np.max(k_rel)),
        "relative_effective_kernel_error_at_y_0p9": float(k_rel[index_09]),
        "effective_kernel_at_y_0p9": float(k[index_09]),
        "rk4_effective_kernel_at_y_0p9": float(k_ref[index_09]),
        "max_relative_direct_kernel_error": float(np.max(direct_rel)),
        "max_absolute_hitting_time_error": float(np.max(np.abs(times - times_ref))),
        "max_absolute_mean_output_error_at_common_times": float(
            np.max(np.abs(y - y_ref))
        ),
        "terminal_mean_output": float(arrays["raw_mean_output"][-1]),
    }


def main() -> int:
    if not REFERENCE_NPZ.exists():
        raise FileNotFoundError(REFERENCE_NPZ)
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable")
    device = torch.device("cuda:1")
    reference_engine.generate_antithetic_state = float64_draw_then_cast
    reference_engine.integrator_step = euler_integrator_step
    torch.cuda.set_device(device)
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(device)

    started = time.monotonic()
    deadline = started + TOTAL_WALL_CAP_SECONDS
    ref = np.load(REFERENCE_NPZ)
    results: list[dict[str, object]] = []
    for step in STEPS:
        if time.monotonic() >= deadline:
            raise TimeoutError("cumulative five-minute wall cap reached")
        torch.cuda.reset_peak_memory_stats(device)
        point_started = time.monotonic()
        arrays, diagnostics = reference_engine.run_point(
            point(step),
            device=device,
            dtype=torch.float32,
            caps=caps(step),
            absolute_wall_deadline=deadline,
        )
        metrics = node_metrics(arrays, ref)
        results.append(
            {
                "rescaled_step_h": step,
                "ordinary_loss_learning_rate_nh": WIDTH * step,
                "elapsed_seconds": time.monotonic() - point_started,
                "peak_gpu_allocated_gib": torch.cuda.max_memory_allocated(device)
                / 2**30,
                "diagnostics": diagnostics,
                "metrics": metrics,
            }
        )

    errors = [
        float(item["metrics"]["max_relative_effective_kernel_error"])
        for item in results
    ]
    output_errors = [
        float(item["metrics"]["max_absolute_mean_output_error_at_common_times"])
        for item in results
    ]
    contraction = [errors[i] / errors[i + 1] for i in range(len(errors) - 1)]
    finest_pass = errors[-1] <= 2.0e-3 and output_errors[-1] <= 2.0e-4
    halving_pass = contraction[-1] >= 1.5
    verdict = "pass" if finest_pass and halving_pass else "inconclusive"

    payload = {
        "schema_version": 1,
        "status": verdict,
        "claim_scope": (
            "matched-initialization Euler discretization agreement with the existing "
            "FP32 RK4 n=4096 reference; not evidence about width convergence"
        ),
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": SEED_BASE,
        "dtype": "float32",
        "reference_integrator": "rk4",
        "tested_integrator": "forward_euler_gradient_descent",
        "max_time": MAX_TIME,
        "output_nodes": OUTPUT_NODES.tolist(),
        "precommitted_gates": {
            "finest_max_relative_effective_kernel_error": 2.0e-3,
            "finest_max_absolute_mean_output_error": 2.0e-4,
            "last_step_halving_error_contraction_at_least": 1.5,
            "cumulative_wall_seconds": TOTAL_WALL_CAP_SECONDS,
        },
        "reference_npz": str(REFERENCE_NPZ),
        "reference_npz_sha256": sha256(REFERENCE_NPZ),
        "script": str(Path(__file__).resolve()),
        "script_sha256": sha256(Path(__file__).resolve()),
        "results": results,
        "max_relative_kernel_error_contraction_factors": contraction,
        "total_elapsed_seconds": time.monotonic() - started,
        "verdict": verdict,
        "interpretation": (
            "Pass means ordinary small-step GD is a numerically adequate integrator "
            "for these matched n=4096 trajectories at the finest tested step."
        ),
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
