#!/usr/bin/env python3
"""Step-refinement and finite-difference check of a scalar negative response."""

from __future__ import annotations

import argparse
import json

import torch

from posthoc_scalar_susceptibility_sign_search import advance, final_x2_tangent


def theta(u):
    return u + u.pow(3) / 3.0


def inverse_theta(r):
    return 2.0 * torch.sinh(torch.asinh(1.5 * r) / 3.0)


def primal(A, r, g1, g2, h: float, steps: int, source: int, forcing):
    for k in range(steps):
        u = inverse_theta(r)
        x1 = torch.atan(u)
        z2 = g1 * x1
        x2 = torch.atan(z2)
        d2 = torch.reciprocal(1.0 + z2.square())
        z3 = g2 * x2
        x3 = torch.atan(z3)
        d3 = torch.reciprocal(1.0 + z3.square())
        b3 = A * d3
        r2 = g2 * b3
        b2 = d2 * (r2 + (forcing if k == source else 0.0))
        q1 = g1 * b2
        A, r, g1, g2 = (
            A + h * x3,
            r + h * q1,
            g1 + h * b2 * x1,
            g2 + h * b3 * x2,
        )
    u = inverse_theta(r)
    return torch.atan(g1 * torch.atan(u))


def tangent(A0, u0, g10, g20, h: float, steps: int, source: int, device):
    vals = [torch.tensor(x, dtype=torch.float64, device=device)
            for x in (A0, u0, g10, g20)]
    A, u, g1, g2 = vals
    r = theta(u)
    z = torch.zeros((), dtype=torch.float64, device=device)
    tA = tr = tg1 = tg2 = z
    with torch.no_grad():
        for k in range(steps):
            A, r, g1, g2, tA, tr, tg1, tg2 = advance(
                A, r, g1, g2, tA, tr, tg1, tg2, h, k == source
            )
        return float(final_x2_tangent(
            A, r, g1, g2, tA, tr, tg1, tg2
        ).item())


def check(A0, u0, g10, g20, horizon, h, source_time, epsilons, device):
    steps = round(horizon / h)
    source = round(source_time / h)
    if source >= steps:
        raise ValueError("source must precede horizon")
    ad = tangent(A0, u0, g10, g20, h, steps, source, device)
    constants = [torch.tensor(x, dtype=torch.float64, device=device)
                 for x in (A0, u0, g10, g20)]
    A, u, g1, g2 = constants
    r = theta(u)
    fds = []
    with torch.no_grad():
        for epsilon in epsilons:
            ep = torch.tensor(epsilon, dtype=torch.float64, device=device)
            xp = primal(A, r, g1, g2, h, steps, source, ep)
            xm = primal(A, r, g1, g2, h, steps, source, -ep)
            fd = float(((xp - xm) / (2.0 * ep)).item())
            fds.append({
                "epsilon": epsilon,
                "fd": fd,
                "relative_error": abs(fd - ad) / max(abs(fd), abs(ad), 1e-300),
            })
    return {
        "h": h,
        "steps": steps,
        "source": source,
        "source_time": source * h,
        "response": ad,
        "response_rate": ad / h,
        "finite_differences": fds,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--A0", type=float, default=-1.470785533780316)
    parser.add_argument("--u0", type=float, default=0.4908137184109185)
    parser.add_argument("--g10", type=float, default=-0.5085760700447663)
    parser.add_argument("--g20", type=float, default=-3.566619346733452)
    parser.add_argument("--horizon", type=float, default=4.0)
    parser.add_argument("--source-time", type=float, default=0.0)
    parser.add_argument("--steps", default="0.04,0.02,0.01,0.005,0.0025")
    parser.add_argument("--epsilons", default="1e-3,1e-4,1e-5,1e-6")
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    epsilons = [float(x) for x in args.epsilons.split(",")]
    records = []
    for h in [float(x) for x in args.steps.split(",")]:
        records.append(check(
            args.A0, args.u0, args.g10, args.g20, args.horizon, h,
            args.source_time, epsilons, torch.device(args.device)
        ))
    print(json.dumps({
        "initial": {"A0": args.A0, "u0": args.u0,
                    "g10": args.g10, "g20": args.g20},
        "horizon": args.horizon,
        "records": records,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
