#!/usr/bin/env python3
"""One bounded four-pair shard of the exploratory n=16384 FP32 Euler run."""

from __future__ import annotations

import argparse
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
PAIR_COUNT = 4
PAIR_BATCH_SIZE = 2
SEED_BASE = 202608140200
STEP = 5.0e-6
MAX_TIME = 0.024
WALL_CAP_SECONDS = 1200.0
GPU_CAP_GIB = 22.0
OUTPUT_NODES = np.asarray([0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
OUTPUT_ROOT = Path(
    "/home/amir/.codex/visualizations/2026/08/14/"
    "019fff0b-20b5-7c23-8d3e-178d14b24fdd"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


_original_generator = canonical_model.generate_antithetic_state
_step_calls = 0
_rounding_diagnostics: list[dict[str, float | int]] = []


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
    """Match the prior width-series FP64 draws before FP32 evolution."""

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
    """Euler step plus a bounded first-step FP32 rounding diagnostic."""

    global _step_calls
    if method != "euler":
        raise ValueError(method)
    tangent, _ = canonical_model.scaled_rhs(
        state, mode, target=target, kernel_floor=kernel_floor
    )
    updated = canonical_model.add_scaled(state, tangent, step)
    if _step_calls % int(round(MAX_TIME / STEP)) == 0:
        # A 512x512 leading block per trajectory is a deterministic million-entry
        # sample.  It estimates the update-resolution floor without allocating a
        # full n^2 boolean tensor.
        old_w = state.W[:, :512, :512]
        new_w = updated.W[:, :512, :512]
        _rounding_diagnostics.append(
            {
                "batch_index": len(_rounding_diagnostics),
                "sampled_W_entries": int(old_w.numel()),
                "fraction_sampled_W_unchanged": float(
                    torch.mean((old_w == new_w).float()).item()
                ),
                "fraction_a_unchanged": float(
                    torch.mean((state.a == updated.a).float()).item()
                ),
                "fraction_u_unchanged": float(
                    torch.mean((state.u == updated.u).float()).item()
                ),
            }
        )
    _step_calls += 1
    return updated


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard", type=int, choices=(0, 1), required=True)
    parser.add_argument("--device", choices=("cuda:0", "cuda:1"), required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA unavailable")
    pair_start = 4 * args.shard
    adjusted_seed_base = SEED_BASE + 104_729 * pair_start
    output_npz = OUTPUT_ROOT / f"gd-n16384-eight-pair-shard{args.shard}.npz"
    output_json = OUTPUT_ROOT / f"gd-n16384-eight-pair-shard{args.shard}.json"
    if output_npz.exists() or output_json.exists():
        raise FileExistsError("no-overwrite gate: shard output already exists")

    device = torch.device(args.device)
    torch.cuda.set_device(device)
    total_gib = torch.cuda.get_device_properties(device).total_memory / 2**30
    torch.cuda.set_per_process_memory_fraction(GPU_CAP_GIB / total_gib, device)
    reference_engine.generate_antithetic_state = float64_draw_then_cast
    reference_engine.integrator_step = euler_step

    steps = int(round(MAX_TIME / STEP))
    point = {
        "id": f"canonical_gd_n16384_pairs_{pair_start}_{pair_start + 3}_h5e-6",
        "mode": "physical",
        "width": WIDTH,
        "antithetic_pairs": PAIR_COUNT,
        "pair_batch_size": PAIR_BATCH_SIZE,
        "seed_base": adjusted_seed_base,
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
        max_steps=steps * (PAIR_COUNT // PAIR_BATCH_SIZE),
        host_rss_gib=16.0,
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
    try:
        arrays, diagnostics = reference_engine.run_point(
            point,
            device=device,
            dtype=torch.float32,
            caps=caps,
            absolute_wall_deadline=started + WALL_CAP_SECONDS,
        )
        elapsed = time.monotonic() - started
        OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(output_npz, **arrays)
        payload = {
            "schema_version": 1,
            "status": "complete_exploratory_shard",
            "claim_scope": (
                "four of eight n=16384 antithetic pairs under FP32 Euler GD; "
                "sampling and FP32 update error remain unresolved"
            ),
            "started_utc": started_utc,
            "ended_utc": datetime.now(timezone.utc).isoformat(),
            "device": args.device,
            "dtype": "float32",
            "width": WIDTH,
            "global_pair_indices": list(range(pair_start, pair_start + PAIR_COUNT)),
            "antithetic_pairs": PAIR_COUNT,
            "pair_batch_size": PAIR_BATCH_SIZE,
            "seed_base_global": SEED_BASE,
            "seed_base_shard": adjusted_seed_base,
            "rescaled_step_h": STEP,
            "ordinary_loss_learning_rate_nh": WIDTH * STEP,
            "max_time": MAX_TIME,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "gpu_memory_cap_gib": GPU_CAP_GIB,
            "elapsed_seconds": elapsed,
            "peak_gpu_allocated_gib": torch.cuda.max_memory_allocated(device) / 2**30,
            "diagnostics": diagnostics,
            "first_step_fp32_rounding": _rounding_diagnostics,
            "output_nodes": arrays["output_nodes"].tolist(),
            "effective_kernel_at_nodes": arrays["effective_kernel"].tolist(),
            "mean_loss_at_nodes": arrays["mean_loss"].tolist(),
            "loss_of_mean_output_at_nodes": arrays["loss_of_mean_output"].tolist(),
            "npz": str(output_npz),
            "npz_sha256": sha256(output_npz),
            "script": str(Path(__file__).resolve()),
            "script_sha256": sha256(Path(__file__).resolve()),
            "terminal_stop_no_retry": True,
        }
        output_json.write_text(json.dumps(payload, indent=2) + "\n")
        print(json.dumps(payload, indent=2))
        return 0
    except Exception as exc:
        elapsed = time.monotonic() - started
        OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
        failure = {
            "schema_version": 1,
            "status": "failed_closed",
            "started_utc": started_utc,
            "ended_utc": datetime.now(timezone.utc).isoformat(),
            "device": args.device,
            "global_pair_indices": list(range(pair_start, pair_start + PAIR_COUNT)),
            "elapsed_seconds": elapsed,
            "peak_gpu_allocated_gib": torch.cuda.max_memory_allocated(device) / 2**30,
            "exception_type": type(exc).__name__,
            "exception": str(exc),
            "first_step_fp32_rounding": _rounding_diagnostics,
            "terminal_stop_no_retry": True,
        }
        output_json.write_text(json.dumps(failure, indent=2) + "\n")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
