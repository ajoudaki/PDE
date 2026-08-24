#!/usr/bin/env python3
"""Generate the preregistered weighted off-column response records."""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
import torch


HORIZONS = (1.0, 2.0, 4.0)
MASTER_SEED = 2026082305


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
    return x1, x2, x3, b3, b2, du


def rk2_step(A, u, G1, G2, h):
    x1, x2, x3, b3, b2, du = fields(A, u, G1, G2)
    half = 0.5 * h
    Am = A + half * x3
    um = u + half * du
    G1m = G1 + (half / A.shape[1]) * b2.unsqueeze(2) * x1.unsqueeze(1)
    G2m = G2 + (half / A.shape[1]) * b3.unsqueeze(2) * x2.unsqueeze(1)
    x1m, x2m, x3m, b3m, b2m, dum = fields(Am, um, G1m, G2m)
    A = A + h * x3m
    u = u + h * dum
    G1 = G1 + (h / A.shape[1]) * b2m.unsqueeze(2) * x1m.unsqueeze(1)
    G2 = G2 + (h / A.shape[1]) * b3m.unsqueeze(2) * x2m.unsqueeze(1)
    return A, u, G1, G2


def energy_stats(row_energy):
    total = row_energy.sum(dim=1)
    tiny = torch.finfo(row_energy.dtype).tiny
    weights = row_energy / total.clamp_min(tiny).unsqueeze(1)
    n = row_energy.shape[1]
    count = max(1, int(math.ceil(0.01 * n)))
    top = torch.topk(weights, count, dim=1).values.sum(dim=1)
    ipr = n * weights.square().sum(dim=1)
    return total.sqrt(), ipr, top


@torch.no_grad()
def simulate_chunk(n, start, count, probes, step, epsilon, device,
                   dtype, draw_float64, seed_offset):
    seed = MASTER_SEED + 10_000_019 * n + 1_000_003 * start + seed_offset
    gen = torch.Generator(device=device)
    gen.manual_seed(seed)
    draw_dtype = torch.float64 if draw_float64 else dtype
    scale = n ** -0.5
    A0 = torch.randn((count, n), generator=gen, device=device,
                     dtype=draw_dtype).to(dtype)
    u0 = torch.randn((count, n), generator=gen, device=device,
                     dtype=draw_dtype).to(dtype)
    G10 = torch.randn((count, n, n), generator=gen, device=device,
                      dtype=draw_dtype).to(dtype) * scale
    G20 = torch.randn((count, n, n), generator=gen, device=device,
                      dtype=draw_dtype).to(dtype) * scale
    signs = torch.randint(0, 2, (count, probes, n), generator=gen,
                          device=device, dtype=torch.int64)
    signs = signs.to(dtype).mul_(2).sub_(1)

    copies = probes * 2
    A = A0[:, None, None, :].expand(count, probes, 2, n).clone()
    u = u0[:, None, None, :].expand(count, probes, 2, n).clone()
    G1 = G10[:, None, None, :, :].expand(count, probes, 2, n, n).clone()
    G2 = G20[:, None, None, :, :].expand(count, probes, 2, n, n).clone()
    delta = epsilon * signs * scale
    G2[:, :, 0, :, 0] += delta
    G2[:, :, 1, :, 0] -= delta
    A = A.reshape(count * copies, n)
    u = u.reshape(count * copies, n)
    G1 = G1.reshape(count * copies, n, n)
    G2 = G2.reshape(count * copies, n, n)

    C0 = G20.clone()
    C0[:, :, 0] = 0.0
    max_steps = int(round(max(HORIZONS) / step))
    targets = {int(round(s / step)): s for s in HORIZONS}
    out = {}
    for k in range(max_steps + 1):
        if k in targets:
            _, x2, _, b3, _, _ = fields(A, u, G1, G2)
            x2 = x2.reshape(count, probes, 2, n)
            b3 = b3.reshape(count, probes, 2, n)
            jx = (x2[:, :, 0] - x2[:, :, 1]) / (2.0 * epsilon)
            jb = (b3[:, :, 0] - b3[:, :, 1]) / (2.0 * epsilon)
            C_rep = C0[:, None].expand(count, probes, n, n).reshape(
                count * probes, n, n
            )
            y = torch.bmm(C_rep, jx.reshape(count * probes, n, 1))
            y = y.reshape(count, probes, n)
            row_y = y.square().mean(dim=1)
            row_b = jb.square().mean(dim=1)
            endpoint_weight = (1.0 + A0.abs()).square()
            fy, ipry, topy = energy_stats(row_y)
            fay, ipray, topay = energy_stats(endpoint_weight * row_y)
            fb, iprb, topb = energy_stats(row_b)
            fab, iprab, topab = energy_stats(endpoint_weight * row_b)
            out[targets[k]] = {
                "f_cx": fy.cpu().to(torch.float64).numpy(),
                "f_ax": fay.cpu().to(torch.float64).numpy(),
                "q_ax": (fay / fy.clamp_min(torch.finfo(dtype).tiny)).cpu().to(torch.float64).numpy(),
                "ipr_ax": ipray.cpu().to(torch.float64).numpy(),
                "top_ax": topay.cpu().to(torch.float64).numpy(),
                "f_b": fb.cpu().to(torch.float64).numpy(),
                "f_ab": fab.cpu().to(torch.float64).numpy(),
                "q_ab": (fab / fb.clamp_min(torch.finfo(dtype).tiny)).cpu().to(torch.float64).numpy(),
                "ipr_ab": iprab.cpu().to(torch.float64).numpy(),
                "top_ab": topab.cpu().to(torch.float64).numpy(),
            }
        if k < max_steps:
            A, u, G1, G2 = rk2_step(A, u, G1, G2, step)
    return seed, out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--replicas", type=int, required=True)
    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--probes", type=int, default=4)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--epsilon", type=float, default=0.002)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32")
    parser.add_argument("--draw-float64", action="store_true")
    parser.add_argument("--seed-offset", type=int, default=0)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    device = torch.device(args.device)
    chunks = []
    seeds = []
    started = time.time()
    for start in range(0, args.replicas, args.batch_size):
        count = min(args.batch_size, args.replicas - start)
        seed, records = simulate_chunk(
            args.width, start, count, args.probes, args.step, args.epsilon,
            device, dtype, args.draw_float64, args.seed_offset,
        )
        seeds.append((start, count, seed))
        chunks.append(records)
        print(json.dumps({"width": args.width, "done": start + count,
                          "seconds": time.time() - started}), flush=True)
    payload = {
        "width": np.asarray(args.width), "replicas": np.asarray(args.replicas),
        "probes": np.asarray(args.probes), "step": np.asarray(args.step),
        "epsilon": np.asarray(args.epsilon), "dtype": np.asarray(args.dtype),
        "draw_float64": np.asarray(args.draw_float64),
        "seed_offset": np.asarray(args.seed_offset),
        "batch_seed_table": np.asarray(seeds, dtype=np.int64),
    }
    for s in HORIZONS:
        key = str(s).replace(".", "p")
        for name in chunks[0][s]:
            payload[f"s{key}_{name}"] = np.concatenate(
                [chunk[s][name] for chunk in chunks]
            )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / f"weighted_{args.tag}_n{args.width}.npz"
    np.savez_compressed(target, **payload)
    print(json.dumps({"saved": str(target),
                      "seconds": time.time() - started}), flush=True)


if __name__ == "__main__":
    main()
