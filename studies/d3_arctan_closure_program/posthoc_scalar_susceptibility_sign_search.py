#!/usr/bin/env python3
"""Post-hoc exact-forward-tangent search for scalar susceptibility signs.

This is an exploratory falsification tool, not preregistered evidence.  At n=1
the normalized trace is the scalar derivative itself, so no stochastic trace
estimator is involved.  The tangent below differentiates every state field and
both learned weights through the exact Euler program.
"""

from __future__ import annotations

import argparse
import json
import math

import torch


MASTER_SEED = 2026082329


def inverse_theta(r: torch.Tensor) -> torch.Tensor:
    return 2.0 * torch.sinh(torch.asinh(1.5 * r) / 3.0)


def advance(A, r, g1, g2, tA, tr, tg1, tg2, h: float, inject: bool):
    u = inverse_theta(r)
    d1 = torch.reciprocal(1.0 + u.square())
    tu = d1 * tr
    x1 = torch.atan(u)
    tx1 = d1 * tu

    z2 = g1 * x1
    tz2 = tg1 * x1 + g1 * tx1
    d2 = torch.reciprocal(1.0 + z2.square())
    td2 = -2.0 * z2 * d2.square() * tz2
    x2 = torch.atan(z2)
    tx2 = d2 * tz2

    z3 = g2 * x2
    tz3 = tg2 * x2 + g2 * tx2
    d3 = torch.reciprocal(1.0 + z3.square())
    td3 = -2.0 * z3 * d3.square() * tz3
    x3 = torch.atan(z3)
    tx3 = d3 * tz3

    b3 = A * d3
    tb3 = tA * d3 + A * td3
    r2 = g2 * b3
    tr2 = tg2 * b3 + g2 * tb3
    b2 = d2 * r2
    tb2 = td2 * r2 + d2 * (tr2 + (1.0 if inject else 0.0))
    q1 = g1 * b2
    tq1 = tg1 * b2 + g1 * tb2

    A_new = A + h * x3
    r_new = r + h * q1
    g1_new = g1 + h * b2 * x1
    g2_new = g2 + h * b3 * x2
    tA_new = tA + h * tx3
    tr_new = tr + h * tq1
    tg1_new = tg1 + h * (tb2 * x1 + b2 * tx1)
    tg2_new = tg2 + h * (tb3 * x2 + b3 * tx2)
    return A_new, r_new, g1_new, g2_new, tA_new, tr_new, tg1_new, tg2_new


def final_x2_tangent(A, r, g1, g2, tA, tr, tg1, tg2):
    del A, g2, tA, tg2
    u = inverse_theta(r)
    d1 = torch.reciprocal(1.0 + u.square())
    x1 = torch.atan(u)
    tx1 = d1.square() * tr
    z2 = g1 * x1
    tz2 = tg1 * x1 + g1 * tx1
    return torch.reciprocal(1.0 + z2.square()) * tz2


def run(batch: int, steps: int, h: float, source: int, scale: float,
        device: torch.device, seed: int):
    gen = torch.Generator(device=device)
    gen.manual_seed(seed)
    dtype = torch.float64
    A = scale * torch.randn(batch, generator=gen, device=device, dtype=dtype)
    u = scale * torch.randn(batch, generator=gen, device=device, dtype=dtype)
    r = u + u.pow(3) / 3.0
    g1 = scale * torch.randn(batch, generator=gen, device=device, dtype=dtype)
    g2 = scale * torch.randn(batch, generator=gen, device=device, dtype=dtype)
    tA = torch.zeros_like(A)
    tr = torch.zeros_like(A)
    tg1 = torch.zeros_like(A)
    tg2 = torch.zeros_like(A)
    with torch.no_grad():
        for k in range(steps):
            A, r, g1, g2, tA, tr, tg1, tg2 = advance(
                A, r, g1, g2, tA, tr, tg1, tg2, h, k == source
            )
        response = final_x2_tangent(A, r, g1, g2, tA, tr, tg1, tg2)
        finite = torch.isfinite(response)
        valid = response[finite]
        min_value, min_local = torch.min(valid, dim=0)
        finite_indices = torch.nonzero(finite, as_tuple=False).flatten()
        min_index = finite_indices[min_local]
        payload = {
            "batch": batch,
            "steps": steps,
            "h": h,
            "horizon": steps * h,
            "source": source,
            "source_time": source * h,
            "scale": scale,
            "finite": int(finite.sum().item()),
            "negative": int((valid < 0).sum().item()),
            "zero_or_negative": int((valid <= 0).sum().item()),
            "minimum": float(min_value.item()),
            "q001": float(torch.quantile(valid, 0.001).item()),
            "q01": float(torch.quantile(valid, 0.01).item()),
            "mean": float(torch.mean(valid).item()),
            "mean_absolute": float(torch.mean(torch.abs(valid)).item()),
            "median": float(torch.median(valid).item()),
            "maximum": float(torch.max(valid).item()),
            "argmin": {
                "A0": float((A.new_tensor(0.0)).item()),
                "index": int(min_index.item()),
            },
        }
    # Redraw just the winning initial condition deterministically for reporting.
    gen.manual_seed(seed)
    draws = [scale * torch.randn(batch, generator=gen, device=device,
                                 dtype=dtype) for _ in range(4)]
    payload["argmin"].update({
        "A0": float(draws[0][min_index].item()),
        "u0": float(draws[1][min_index].item()),
        "g10": float(draws[2][min_index].item()),
        "g20": float(draws[3][min_index].item()),
    })
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=200_000)
    parser.add_argument("--horizon", type=float, default=4.0)
    parser.add_argument("--step", type=float, default=0.02)
    parser.add_argument("--source-fractions", default="0,0.25,0.5,0.75")
    parser.add_argument("--scales", default="1,2,4")
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    steps = int(round(args.horizon / args.step))
    if not math.isclose(steps * args.step, args.horizon,
                        rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("horizon must be an integer multiple of step")
    fractions = [float(x) for x in args.source_fractions.split(",")]
    scales = [float(x) for x in args.scales.split(",")]
    device = torch.device(args.device)
    for a, scale in enumerate(scales):
        for b, fraction in enumerate(fractions):
            source = min(steps - 1, max(0, int(round(fraction * steps))))
            result = run(
                args.batch, steps, args.step, source, scale, device,
                MASTER_SEED + 1009 * a + 1_000_003 * b,
            )
            print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
