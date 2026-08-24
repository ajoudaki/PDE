#!/usr/bin/env python3
"""Generate the preregistered hidden-neuron gauge-block gradient records."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch


HORIZONS = (1.0, 2.0, 4.0)
MODES = ("gauge", "row", "column")
ORDERS = (2, 4, 6, 8)
MASTER_SEED = 2026082307


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


def rk2_step(A, u, G1, G2, step):
    x1, x2, x3, b3, b2, du = fields(A, u, G1, G2)
    half = 0.5 * step
    width = A.shape[1]
    Am = A + half * x3
    um = u + half * du
    G1m = G1 + (half / width) * b2.unsqueeze(2) * x1.unsqueeze(1)
    G2m = G2 + (half / width) * b3.unsqueeze(2) * x2.unsqueeze(1)
    x1m, x2m, x3m, b3m, b2m, dum = fields(Am, um, G1m, G2m)
    return (
        A + step * x3m,
        u + step * dum,
        G1 + (step / width) * b2m.unsqueeze(2) * x1m.unsqueeze(1),
        G2 + (step / width) * b3m.unsqueeze(2) * x2m.unsqueeze(1),
    )


@torch.no_grad()
def simulate_chunk(width, start, count, probes, step, epsilon, device,
                   dtype, draw_float64, seed_offset):
    seed = MASTER_SEED + 10_000_019 * width + 1_000_003 * start + seed_offset
    generator = torch.Generator(device=device)
    generator.manual_seed(seed)
    draw_dtype = torch.float64 if draw_float64 else dtype
    scale = width ** -0.5
    A0 = torch.randn((count, width), generator=generator, device=device,
                     dtype=draw_dtype).to(dtype)
    u0 = torch.randn((count, width), generator=generator, device=device,
                     dtype=draw_dtype).to(dtype)
    G10 = torch.randn((count, width, width), generator=generator,
                      device=device, dtype=draw_dtype).to(dtype) * scale
    G20 = torch.randn((count, width, width), generator=generator,
                      device=device, dtype=draw_dtype).to(dtype) * scale
    signs1 = torch.randint(0, 2, (count, probes, width), generator=generator,
                           device=device, dtype=torch.int64)
    signs2 = torch.randint(0, 2, (count, probes, width), generator=generator,
                           device=device, dtype=torch.int64)
    signs1 = signs1.to(dtype).mul_(2).sub_(1)
    signs2 = signs2.to(dtype).mul_(2).sub_(1)

    modes = len(MODES)
    copies = modes * probes * 2
    A = A0[:, None, None, None, :].expand(
        count, modes, probes, 2, width
    ).clone()
    u = u0[:, None, None, None, :].expand(
        count, modes, probes, 2, width
    ).clone()
    G1 = G10[:, None, None, None, :, :].expand(
        count, modes, probes, 2, width, width
    ).clone()
    G2 = G20[:, None, None, None, :, :].expand(
        count, modes, probes, 2, width, width
    ).clone()
    delta1 = epsilon * signs1 * scale
    delta2 = epsilon * signs2 * scale
    # Modes 0 and 1 perturb the incoming row; modes 0 and 2 perturb the
    # outgoing column.  Sign index 0 is plus and 1 is minus.
    for mode in (0, 1):
        G1[:, mode, :, 0, 0, :] += delta1
        G1[:, mode, :, 1, 0, :] -= delta1
    for mode in (0, 2):
        G2[:, mode, :, 0, :, 0] += delta2
        G2[:, mode, :, 1, :, 0] -= delta2

    static_column = G20[:, None, None, None, :, 0].expand(
        count, modes, probes, 2, width
    ).clone()
    for mode in (0, 2):
        static_column[:, mode, :, 0, :] += delta2
        static_column[:, mode, :, 1, :] -= delta2

    A = A.reshape(count * copies, width)
    u = u.reshape(count * copies, width)
    G1 = G1.reshape(count * copies, width, width)
    G2 = G2.reshape(count * copies, width, width)
    static_column = static_column.reshape(count * copies, width)

    Ab, ub, G1b, G2b = A0.clone(), u0.clone(), G10.clone(), G20.clone()
    max_steps = int(round(max(HORIZONS) / step))
    targets = {int(round(value / step)): value for value in HORIZONS}
    output = {}
    for k in range(max_steps + 1):
        if k in targets:
            _, _, _, b3, _, _ = fields(A, u, G1, G2)
            static_query = (static_column * b3).sum(dim=1).reshape(
                count, modes, probes, 2
            )
            derivatives = (
                static_query[:, :, :, 0] - static_query[:, :, :, 1]
            ) / (2.0 * epsilon)
            _, _, _, b3b, _, _ = fields(Ab, ub, G1b, G2b)
            base_query = (G20[:, :, 0] * b3b).sum(dim=1)
            record = {"query": base_query.cpu().to(torch.float64).numpy()}
            for mode, name in enumerate(MODES):
                values = derivatives[:, mode]
                gradient = values.square().mean(dim=1).sqrt()
                record[f"grad_{name}"] = gradient.cpu().to(torch.float64).numpy()
                record[f"dir_{name}"] = values.cpu().to(torch.float64).numpy()
                record[f"mom_{name}"] = torch.stack([
                    values.abs().pow(order).mean(dim=1)
                    for order in ORDERS
                ], dim=1).cpu().to(torch.float64).numpy()
            output[targets[k]] = record
        if k < max_steps:
            A, u, G1, G2 = rk2_step(A, u, G1, G2, step)
            Ab, ub, G1b, G2b = rk2_step(Ab, ub, G1b, G2b, step)
    return seed, output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--replicas", type=int, required=True)
    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--probes", type=int, default=4)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--epsilon", type=float, default=0.002)
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
        "orders": np.asarray(ORDERS, dtype=np.int64),
        "batch_seed_table": np.asarray(seeds, dtype=np.int64),
    }
    for horizon in HORIZONS:
        key = str(horizon).replace(".", "p")
        for name in chunks[0][horizon]:
            payload[f"s{key}_{name}"] = np.concatenate([
                chunk[horizon][name] for chunk in chunks
            ])
    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / f"gauge_{args.tag}_n{args.width}.npz"
    np.savez_compressed(target, **payload)
    print(json.dumps({"saved": str(target),
                      "seconds": time.time() - started}), flush=True)


if __name__ == "__main__":
    main()
