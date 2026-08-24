#!/usr/bin/env python3
"""Run the preregistered middle saturation/nonalignment diagnostic."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import torch


HORIZONS = (1.0, 2.0, 4.0)
MASTER_SEED = 2026082347


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
    return x1, d1, z2, x2, d2, x3, b3, r2, b2, q1, du


def midpoint_step(A, u, G1, G2, h):
    x1, _, _, x2, _, x3, b3, _, b2, _, du = fields(A, u, G1, G2)
    half = 0.5 * h
    n = A.shape[1]
    Am = A + half * x3
    um = u + half * du
    G1m = G1 + (half / n) * b2.unsqueeze(2) * x1.unsqueeze(1)
    G2m = G2 + (half / n) * b3.unsqueeze(2) * x2.unsqueeze(1)
    x1m, _, _, x2m, _, x3m, b3m, _, b2m, _, dum = fields(
        Am, um, G1m, G2m
    )
    A = A + h * x3m
    u = u + h * dum
    G1 = G1 + (h / n) * b2m.unsqueeze(2) * x1m.unsqueeze(1)
    G2 = G2 + (h / n) * b3m.unsqueeze(2) * x2m.unsqueeze(1)
    return A, u, G1, G2


def checkpoint(A, u, G1, G2):
    x1, d1, z2, _, d2, _, _, r2, b2, q1, _ = fields(A, u, G1, G2)
    dx1 = d1.square() * q1
    self_term = x1.square().mean(dim=1, keepdim=True) * b2
    bath = torch.bmm(G1, dx1.unsqueeze(-1)).squeeze(-1)
    velocity = self_term + bath
    residual = (velocity - self_term - bath).to(torch.float64).abs().amax(dim=1)
    return {
        "R": r2.cpu().to(torch.float32).numpy(),
        "D": d2.cpu().to(torch.float32).numpy(),
        "S": self_term.cpu().to(torch.float32).numpy(),
        "H": bath.cpu().to(torch.float32).numpy(),
        "V": velocity.cpu().to(torch.float32).numpy(),
        "Z": z2.cpu().to(torch.float32).numpy(),
        "identity_residual": residual.cpu().numpy(),
    }


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


@torch.no_grad()
def simulate_chunk(n, start, count, step, device, dtype, draw_float64,
                   seed_offset):
    seed = MASTER_SEED + 10_000_019 * n + 1_000_003 * start + seed_offset
    generator = torch.Generator(device=device)
    generator.manual_seed(seed)
    draw_dtype = torch.float64 if draw_float64 else dtype
    A = torch.randn((count, n), generator=generator, device=device,
                    dtype=draw_dtype).to(dtype)
    u = torch.randn((count, n), generator=generator, device=device,
                    dtype=draw_dtype).to(dtype)
    scale = n ** -0.5
    G1 = torch.randn((count, n, n), generator=generator, device=device,
                     dtype=draw_dtype).to(dtype).mul_(scale)
    G2 = torch.randn((count, n, n), generator=generator, device=device,
                     dtype=draw_dtype).to(dtype).mul_(scale)

    max_steps = int(round(max(HORIZONS) / step))
    if abs(max_steps * step - max(HORIZONS)) > 1e-10:
        raise ValueError("step must divide the largest horizon")
    targets = {int(round(t / step)): t for t in HORIZONS}
    output = {}
    for k in range(max_steps + 1):
        if k in targets:
            output[targets[k]] = checkpoint(A, u, G1, G2)
        if k < max_steps:
            A, u, G1, G2 = midpoint_step(A, u, G1, G2, step)
    return seed, output


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
    started = time.time()
    for start in range(0, args.replicas, args.batch_size):
        count = min(args.batch_size, args.replicas - start)
        seed, records = simulate_chunk(
            args.width, start, count, args.step, device, dtype,
            args.draw_float64, args.seed_offset,
        )
        chunks.append(records)
        seeds.append((start, count, seed))
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
    }
    for horizon in HORIZONS:
        hkey = str(horizon).replace(".", "p")
        for name in chunks[0][horizon]:
            payload[f"s{hkey}_{name}"] = np.concatenate(
                [chunk[horizon][name] for chunk in chunks], axis=0
            )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / f"middle_saturation_{args.tag}_n{args.width}.npz"
    np.savez_compressed(target, **payload)
    print(json.dumps({
        "saved": str(target),
        "seconds": time.time() - started,
    }), flush=True)


if __name__ == "__main__":
    main()
