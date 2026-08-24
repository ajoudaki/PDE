#!/usr/bin/env python3
"""Preregistered GPU audit of high moments in the depth-3 arctan flow.

The scientific contract and interpretation thresholds are frozen in
GPU_HIGH_MOMENT_TAIL_PREREGISTRATION_2026-08-23.md.  This program only
generates raw per-network/per-coordinate records; analysis is separate.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
import torch


P_ORDERS = (2, 3, 4, 6, 8, 10, 12)
HORIZONS = (1.0, 2.0, 4.0, 8.0)
MASTER_SEED = 2026082303


def fields(A: torch.Tensor, u: torch.Tensor, G1: torch.Tensor, G2: torch.Tensor):
    x1 = torch.atan(u)
    d1 = torch.reciprocal(1.0 + u.square())
    z2 = torch.bmm(G1, x1.unsqueeze(-1)).squeeze(-1)
    x2 = torch.atan(z2)
    d2 = torch.reciprocal(1.0 + z2.square())
    z3 = torch.bmm(G2, x2.unsqueeze(-1)).squeeze(-1)
    x3 = torch.atan(z3)
    d3 = torch.reciprocal(1.0 + z3.square())
    b3 = A * d3
    r2 = torch.bmm(G2.transpose(1, 2), b3.unsqueeze(-1)).squeeze(-1)
    b2 = d2 * r2
    q1 = torch.bmm(G1.transpose(1, 2), b2.unsqueeze(-1)).squeeze(-1)
    du = d1 * q1

    rho1 = x1.square().mean(dim=1)
    rho2 = x2.square().mean(dim=1)
    lower_action = rho1 * b2.square().mean(dim=1) + du.square().mean(dim=1)
    kernel_blocks = torch.stack(
        (
            x3.square().mean(dim=1),
            rho2 * b3.square().mean(dim=1),
            rho1 * b2.square().mean(dim=1),
            du.square().mean(dim=1),
        ),
        dim=1,
    )
    return {
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "b3": b3,
        "r2": r2,
        "b2": b2,
        "q1": q1,
        "du": du,
        "lower_action": lower_action,
        "kernel_blocks": kernel_blocks,
    }


def moment_rows(x: torch.Tensor) -> torch.Tensor:
    # Log-sum-exp avoids overflow in the p=12 diagnostic without changing it.
    ax = x.abs().to(torch.float64).clamp_min(torch.finfo(torch.float64).tiny)
    lx = ax.log()
    rows = []
    logn = math.log(x.shape[1])
    for p in P_ORDERS:
        rows.append(torch.exp((torch.logsumexp(p * lx, dim=1) - logn) / p))
    return torch.stack(rows, dim=1)


def record_state(state, accumulated_action):
    f = fields(*state)
    return {
        "r2_values": f["r2"].detach().cpu().to(torch.float32).numpy(),
        "b2_values": f["b2"].detach().cpu().to(torch.float32).numpy(),
        "q1_values": f["q1"].detach().cpu().to(torch.float32).numpy(),
        "r2_moments": moment_rows(f["r2"]).cpu().numpy(),
        "b2_moments": moment_rows(f["b2"]).cpu().numpy(),
        "q1_moments": moment_rows(f["q1"]).cpu().numpy(),
        "kernel_blocks": f["kernel_blocks"].detach().cpu().to(torch.float64).numpy(),
        "accumulated_action": accumulated_action.detach().cpu().to(torch.float64).numpy(),
    }


@torch.no_grad()
def simulate_batch(
    n: int,
    start: int,
    count: int,
    step: float,
    device: torch.device,
    seed_offset: int | None,
    dtype: torch.dtype,
    draw_float64: bool,
):
    # The seed rule is frozen and recorded per batch.  Each batch consumes one
    # disjoint Philox stream; changing the batch schedule would change the raw
    # draw and is therefore included in metadata.
    tail = int(round(1e6 * step)) if seed_offset is None else seed_offset
    seed = MASTER_SEED + 10_000_019 * n + 1_000_003 * start + tail
    gen = torch.Generator(device=device)
    gen.manual_seed(seed)
    draw_dtype = torch.float64 if draw_float64 else dtype
    A = torch.randn((count, n), generator=gen, device=device, dtype=draw_dtype).to(dtype)
    u = torch.randn((count, n), generator=gen, device=device, dtype=draw_dtype).to(dtype)
    scale = n ** -0.5
    G1 = torch.randn((count, n, n), generator=gen, device=device, dtype=draw_dtype).to(dtype) * scale
    G2 = torch.randn((count, n, n), generator=gen, device=device, dtype=draw_dtype).to(dtype) * scale
    action = torch.zeros(count, device=device, dtype=torch.float64)

    max_steps = int(round(max(HORIZONS) / step))
    target_steps = {int(round(s / step)): s for s in HORIZONS}
    records = {}

    for k in range(max_steps + 1):
        if k in target_steps:
            records[target_steps[k]] = record_state((A, u, G1, G2), action)
        if k == max_steps:
            break

        f0 = fields(A, u, G1, G2)
        half = 0.5 * step
        Am = A + half * f0["x3"]
        um = u + half * f0["du"]
        G1m = G1 + (half / n) * f0["b2"].unsqueeze(2) * f0["x1"].unsqueeze(1)
        G2m = G2 + (half / n) * f0["b3"].unsqueeze(2) * f0["x2"].unsqueeze(1)

        fm = fields(Am, um, G1m, G2m)
        A.add_(fm["x3"], alpha=step)
        u.add_(fm["du"], alpha=step)
        G1.add_((step / n) * fm["b2"].unsqueeze(2) * fm["x1"].unsqueeze(1))
        G2.add_((step / n) * fm["b3"].unsqueeze(2) * fm["x2"].unsqueeze(1))
        action.add_(fm["lower_action"].to(torch.float64), alpha=step)

    return seed, records


def concatenate_records(chunks):
    out = {}
    for horizon in HORIZONS:
        names = chunks[0][horizon].keys()
        out[horizon] = {
            name: np.concatenate([chunk[horizon][name] for chunk in chunks], axis=0)
            for name in names
        }
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--replicas", type=int, required=True)
    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--tag", default="main")
    parser.add_argument("--seed-offset", type=int)
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32")
    parser.add_argument("--draw-float64", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    if not torch.cuda.is_available() and str(args.device).startswith("cuda"):
        raise RuntimeError("CUDA requested but unavailable")
    device = torch.device(args.device)
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    args.output_dir.mkdir(parents=True, exist_ok=True)
    chunks = []
    seeds = []
    started = time.time()
    for start in range(0, args.replicas, args.batch_size):
        count = min(args.batch_size, args.replicas - start)
        seed, records = simulate_batch(
            args.width,
            start,
            count,
            args.step,
            device,
            args.seed_offset,
            dtype,
            args.draw_float64,
        )
        seeds.append((start, count, seed))
        chunks.append(records)
        elapsed = time.time() - started
        print(json.dumps({"width": args.width, "done": start + count,
                          "replicas": args.replicas, "seconds": elapsed}), flush=True)

    records = concatenate_records(chunks)
    payload = {
        "width": np.asarray(args.width),
        "replicas": np.asarray(args.replicas),
        "batch_size": np.asarray(args.batch_size),
        "step": np.asarray(args.step),
        "p_orders": np.asarray(P_ORDERS),
        "horizons": np.asarray(HORIZONS),
        "master_seed": np.asarray(MASTER_SEED),
        "seed_offset": np.asarray(-1 if args.seed_offset is None else args.seed_offset),
        "dtype": np.asarray(args.dtype),
        "draw_float64": np.asarray(args.draw_float64),
        "batch_seed_table": np.asarray(seeds, dtype=np.int64),
        "elapsed_seconds": np.asarray(time.time() - started),
    }
    for horizon, values in records.items():
        key = str(horizon).replace(".", "p")
        for name, value in values.items():
            payload[f"s{key}_{name}"] = value
    target = args.output_dir / f"tail_{args.tag}_n{args.width}_h{args.step:g}.npz"
    np.savez_compressed(target, **payload)
    print(json.dumps({"saved": str(target), "seconds": time.time() - started}), flush=True)


if __name__ == "__main__":
    main()
