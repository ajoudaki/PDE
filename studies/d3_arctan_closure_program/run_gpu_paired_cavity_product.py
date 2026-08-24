#!/usr/bin/env python3
"""Run the preregistered genuine paired-cavity product diagnostic."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

import numpy as np
import torch


HORIZONS = (1.0, 2.0, 4.0)
MOMENTS = (2, 4, 6, 8)
MASTER_SEED = 2026082317


def fields(A, u, G1, G2):
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
    return x1, z2, x2, x3, b3, r2, b2, du


def midpoint_step(A, u, G1, G2, h):
    x1, _, x2, x3, b3, _, b2, du = fields(A, u, G1, G2)
    half = 0.5 * h
    n = A.shape[1]
    Am = A + half * x3
    um = u + half * du
    G1m = G1 + (half / n) * b2.unsqueeze(2) * x1.unsqueeze(1)
    G2m = G2 + (half / n) * b3.unsqueeze(2) * x2.unsqueeze(1)
    x1m, _, x2m, x3m, b3m, _, b2m, dum = fields(Am, um, G1m, G2m)
    A = A + h * x3m
    u = u + h * dum
    G1 = G1 + (h / n) * b2m.unsqueeze(2) * x1m.unsqueeze(1)
    G2 = G2 + (h / n) * b3m.unsqueeze(2) * x2m.unsqueeze(1)
    return A, u, G1, G2


def lp(v, q):
    vd = v.to(torch.float64).abs()
    return vd.pow(q).mean(dim=1).pow(1.0 / q)


def checkpoint_stats(z2, r2, indices):
    batch, copies, n = z2.shape
    assert copies == 2
    dz = z2[:, 0] - z2[:, 1]
    rc = r2[:, 1]
    prod = rc * dz
    scale = math.sqrt(n)
    result = {}
    for q in MOMENTS:
        result[f"j{q}"] = (scale * lp(prod, q)).cpu().numpy()
        result[f"z{q}"] = (scale * lp(dz, q)).cpu().numpy()
        result[f"r{q}"] = lp(rc, q).cpu().numpy()
    rows = torch.arange(batch, device=z2.device)
    result["cavity_zero_z"] = z2[rows, 1, indices].abs().to(
        torch.float64
    ).cpu().numpy()
    result["cavity_zero_r"] = r2[rows, 1, indices].abs().to(
        torch.float64
    ).cpu().numpy()
    # Ancillary alignment statistic; it is not part of the frozen verdict.
    denom = (
        lp(rc, 4) * lp(dz, 4) * scale
    ).clamp_min(torch.finfo(torch.float64).tiny)
    result["alignment_l2_over_l4"] = (
        scale * lp(prod, 2) / denom
    ).cpu().numpy()
    return result


@torch.no_grad()
def simulate_chunk(n, start, count, step, device, dtype, draw_float64,
                   seed_offset):
    seed = MASTER_SEED + 10_000_019 * n + 1_000_003 * start + seed_offset
    gen = torch.Generator(device=device)
    gen.manual_seed(seed)
    draw_dtype = torch.float64 if draw_float64 else dtype
    A0 = torch.randn((count, n), generator=gen, device=device,
                     dtype=draw_dtype).to(dtype)
    u0 = torch.randn((count, n), generator=gen, device=device,
                     dtype=draw_dtype).to(dtype)
    scale = n ** -0.5
    G10 = torch.randn((count, n, n), generator=gen, device=device,
                      dtype=draw_dtype).to(dtype).mul_(scale)
    G20 = torch.randn((count, n, n), generator=gen, device=device,
                      dtype=draw_dtype).to(dtype).mul_(scale)
    indices = torch.randint(
        0, n, (count,), generator=gen, device=device, dtype=torch.int64
    )

    A = A0[:, None, :].expand(count, 2, n).clone()
    u = u0[:, None, :].expand(count, 2, n).clone()
    G1 = G10[:, None, :, :].expand(count, 2, n, n).clone()
    G2 = G20[:, None, :, :].expand(count, 2, n, n).clone()
    rows = torch.arange(count, device=device)
    G1[rows, 1, indices, :] = 0.0
    G2[rows, 1, :, indices] = 0.0
    A = A.reshape(2 * count, n)
    u = u.reshape(2 * count, n)
    G1 = G1.reshape(2 * count, n, n)
    G2 = G2.reshape(2 * count, n, n)

    max_steps = int(round(max(HORIZONS) / step))
    if abs(max_steps * step - max(HORIZONS)) > 1e-10:
        raise ValueError("step must divide the largest horizon")
    targets = {int(round(s / step)): s for s in HORIZONS}
    output = {}
    for k in range(max_steps + 1):
        if k in targets:
            _, z2, _, _, _, r2, _, _ = fields(A, u, G1, G2)
            z2 = z2.reshape(count, 2, n)
            r2 = r2.reshape(count, 2, n)
            output[targets[k]] = checkpoint_stats(z2, r2, indices)
        if k < max_steps:
            A, u, G1, G2 = midpoint_step(A, u, G1, G2, step)
    return seed, indices.cpu().numpy(), output


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--replicas", type=int, required=True)
    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dtype", choices=("float32", "float64"),
                        default="float32")
    parser.add_argument("--draw-float64", action="store_true")
    parser.add_argument("--seed-offset", type=int, default=0)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    device = torch.device(args.device)
    chunks = []
    seeds = []
    indices = []
    started = time.time()
    for start in range(0, args.replicas, args.batch_size):
        count = min(args.batch_size, args.replicas - start)
        seed, js, records = simulate_chunk(
            args.width, start, count, args.step, device, dtype,
            args.draw_float64, args.seed_offset,
        )
        seeds.append((start, count, seed))
        indices.append(js)
        chunks.append(records)
        print(json.dumps({
            "width": args.width,
            "done": start + count,
            "seconds": time.time() - started,
        }), flush=True)

    payload = {
        "width": np.asarray(args.width),
        "replicas": np.asarray(args.replicas),
        "step": np.asarray(args.step),
        "dtype": np.asarray(args.dtype),
        "draw_float64": np.asarray(args.draw_float64),
        "seed_offset": np.asarray(args.seed_offset),
        "script_sha256": np.asarray(script_sha256()),
        "batch_seed_table": np.asarray(seeds, dtype=np.int64),
        "cavity_indices": np.concatenate(indices),
    }
    for horizon in HORIZONS:
        hkey = str(horizon).replace(".", "p")
        for name in chunks[0][horizon]:
            payload[f"s{hkey}_{name}"] = np.concatenate(
                [chunk[horizon][name] for chunk in chunks]
            )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / (
        f"paired_product_{args.tag}_n{args.width}.npz"
    )
    np.savez_compressed(target, **payload)
    print(json.dumps({
        "saved": str(target),
        "seconds": time.time() - started,
    }), flush=True)


if __name__ == "__main__":
    main()
