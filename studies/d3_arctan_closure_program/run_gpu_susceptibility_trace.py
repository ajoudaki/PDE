#!/usr/bin/env python3
"""Hutchinson/autodiff diagnostic for the causal susceptibility trace.

The forcing is inserted only in the lower use of R2.  All later layers and
transpose reuses remain in the graph, so this measures the full cavity-bulk
response rather than a frozen-lower surrogate.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import numpy as np
import torch


MASTER_SEED = 2026082311


def theta(u: torch.Tensor) -> torch.Tensor:
    return u + u.pow(3) / 3.0


def inverse_theta(r: torch.Tensor) -> torch.Tensor:
    # u^3+3u=3r and sinh(3a)=3sinh(a)+4sinh(a)^3.
    return 2.0 * torch.sinh(torch.asinh(1.5 * r) / 3.0)


def unforced_fields(A, r, G1, G2):
    u = inverse_theta(r)
    x1 = torch.atan(u)
    z2 = G1 @ x1
    x2 = torch.atan(z2)
    d2 = torch.reciprocal(1.0 + z2.square())
    z3 = G2 @ x2
    x3 = torch.atan(z3)
    d3 = torch.reciprocal(1.0 + z3.square())
    b3 = A * d3
    r2 = G2.T @ b3
    return x1, x2, x3, d2, b3, r2


def evolve(A0, r0, G10, G20, forcing, h: float):
    A, r, G1, G2 = A0, r0, G10, G20
    n = A.numel()
    for k in range(forcing.shape[0]):
        x1, x2, x3, d2, b3, r2 = unforced_fields(A, r, G1, G2)
        b2 = d2 * (r2 + forcing[k])
        q1 = G1.T @ b2
        A = A + h * x3
        r = r + h * q1
        G1 = G1 + (h / n) * b2[:, None] * x1[None, :]
        G2 = G2 + (h / n) * b3[:, None] * x2[None, :]
    _, x2, _, _, _, r2 = unforced_fields(A, r, G1, G2)
    return x2, r2, (A, r, G1, G2)


def summarize(kappa: torch.Tensor, h: float):
    positive = torch.clamp(kappa, min=0.0).sum()
    negative = torch.clamp(-kappa, min=0.0).sum()
    return {
        "tv": (positive + negative).item(),
        "signed": kappa.sum().item(),
        "positive": positive.item(),
        "negative": negative.item(),
        "max_rate": (kappa.abs().max() / h).item(),
        "last_rate": (kappa[-1] / h).item(),
    }


def one_orbit(n, steps, h, probes, device, dtype, seed, fd_check,
              fd_epsilon, exact_basis, draw_float64):
    gen = torch.Generator(device=device)
    gen.manual_seed(seed)
    scale = n ** -0.5
    draw_dtype = torch.float64 if draw_float64 else dtype
    A0 = torch.randn(n, generator=gen, device=device,
                     dtype=draw_dtype).to(dtype)
    u0 = torch.randn(n, generator=gen, device=device,
                     dtype=draw_dtype).to(dtype)
    r0 = theta(u0)
    G10 = torch.randn((n, n), generator=gen, device=device,
                      dtype=draw_dtype).to(dtype) * scale
    G20 = torch.randn((n, n), generator=gen, device=device,
                      dtype=draw_dtype).to(dtype) * scale
    forcing = torch.zeros((steps, n), device=device, dtype=dtype,
                          requires_grad=True)

    x2, r2, _ = evolve(A0, r0, G10, G20, forcing, h)
    if exact_basis:
        if probes != n:
            raise ValueError("exact-basis requires probes == width")
        gammas = torch.eye(n, device=device, dtype=dtype)
    else:
        signs = torch.randint(0, 2, (probes, n), generator=gen,
                              device=device, dtype=torch.int64)
        gammas = signs.to(dtype).mul_(2).sub_(1).mul_(scale)
    estimates = []
    for q in range(probes):
        scalar = torch.dot(gammas[q], x2)
        grad = torch.autograd.grad(
            scalar, forcing, retain_graph=(q + 1 < probes),
            create_graph=False, allow_unused=False,
        )[0]
        estimates.append((grad * gammas[q][None, :]).sum(dim=1).detach())
    estimates = torch.stack(estimates)
    mean_kappa = estimates.mean(dim=0)
    half = probes // 2
    first = estimates[:half].mean(dim=0)
    second = estimates[half:].mean(dim=0)
    main = summarize(mean_kappa, h)
    first_stats = summarize(first, h)
    second_stats = summarize(second, h)
    denom = max(main["tv"], torch.finfo(dtype).eps)
    main["half_rel_tv"] = abs(first_stats["tv"] - second_stats["tv"]) / denom
    main["probe_point_rmse"] = torch.sqrt(
        torch.mean((first - second).square())
    ).item()
    main["r2_l2"] = torch.sqrt(torch.mean(r2.detach().square())).item()
    main["x2_l2"] = torch.sqrt(torch.mean(x2.detach().square())).item()

    fd_records = []
    if fd_check:
        directions = (max(0, steps // 4), max(0, 3 * steps // 4))
        gamma = gammas[0].detach()
        for ell in directions:
            with torch.no_grad():
                plus = torch.zeros((steps, n), device=device, dtype=dtype)
                minus = torch.zeros((steps, n), device=device, dtype=dtype)
                plus[ell] = fd_epsilon * gamma
                minus[ell] = -fd_epsilon * gamma
                xp, _, _ = evolve(A0, r0, G10, G20, plus, h)
                xm, _, _ = evolve(A0, r0, G10, G20, minus, h)
                fd = torch.dot(gamma, xp - xm).item() / (2.0 * fd_epsilon)
            ad = estimates[0, ell].item()
            fd_records.append({
                "ell": ell, "ad": ad, "fd": fd,
                "abs_error": abs(ad - fd),
                "rel_error": abs(ad - fd) / max(abs(ad), abs(fd), 1.0e-12),
            })

    payload = {
        **main,
        "first_tv": first_stats["tv"],
        "second_tv": second_stats["tv"],
        "first_signed": first_stats["signed"],
        "second_signed": second_stats["signed"],
        "kappa": mean_kappa.cpu().to(torch.float64).numpy(),
        "probe_kappa": estimates.cpu().to(torch.float64).numpy(),
        "fd": fd_records,
    }
    del forcing, x2, r2, estimates, mean_kappa
    if device.type == "cuda":
        torch.cuda.empty_cache()
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--horizon", type=float, required=True)
    parser.add_argument("--step", type=float, required=True)
    parser.add_argument("--replicas", type=int, required=True)
    parser.add_argument("--probes", type=int, default=8)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--dtype", choices=("float32", "float64"),
                        default="float32")
    parser.add_argument("--seed-offset", type=int, default=0)
    parser.add_argument("--fd-check", action="store_true")
    parser.add_argument("--fd-epsilon", type=float, default=0.01)
    parser.add_argument("--exact-basis", action="store_true")
    parser.add_argument("--draw-float64", action="store_true")
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    steps = int(round(args.horizon / args.step))
    if not math.isclose(steps * args.step, args.horizon,
                        rel_tol=0.0, abs_tol=1.0e-10):
        raise ValueError("horizon must be an integer multiple of step")
    if args.probes < 2 or args.probes % 2:
        raise ValueError("probes must be an even integer >=2")
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    device = torch.device(args.device)
    records = []
    started = time.time()
    for replica in range(args.replicas):
        seed = (MASTER_SEED + args.seed_offset + 10_000_019 * args.width
                + 1_000_003 * replica + 1009 * steps)
        record = one_orbit(
            args.width, steps, args.step, args.probes, device, dtype, seed,
            args.fd_check, args.fd_epsilon, args.exact_basis,
            args.draw_float64,
        )
        record["seed"] = seed
        records.append(record)
        print(json.dumps({
            "width": args.width, "replica": replica + 1,
            "replicas": args.replicas, "tv": record["tv"],
            "seconds": time.time() - started,
        }), flush=True)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / (
        f"susceptibility_{args.tag}_n{args.width}_h{args.step:g}_T{args.horizon:g}.npz"
    )
    scalar_keys = [
        "tv", "signed", "positive", "negative", "max_rate", "last_rate",
        "half_rel_tv", "probe_point_rmse", "r2_l2", "x2_l2",
        "first_tv", "second_tv", "first_signed", "second_signed", "seed",
    ]
    out = {
        "width": np.asarray(args.width), "horizon": np.asarray(args.horizon),
        "step": np.asarray(args.step), "replicas": np.asarray(args.replicas),
        "probes": np.asarray(args.probes), "dtype": np.asarray(args.dtype),
        "exact_basis": np.asarray(args.exact_basis),
        "draw_float64": np.asarray(args.draw_float64),
        "seed_offset": np.asarray(args.seed_offset),
    }
    for key in scalar_keys:
        out[key] = np.asarray([record[key] for record in records])
    out["kappa"] = np.stack([record["kappa"] for record in records])
    out["probe_kappa"] = np.stack(
        [record["probe_kappa"] for record in records]
    )
    out["fd_json"] = np.asarray(json.dumps([r["fd"] for r in records]))
    np.savez_compressed(target, **out)
    print(json.dumps({"saved": str(target),
                      "seconds": time.time() - started}), flush=True)


if __name__ == "__main__":
    main()
