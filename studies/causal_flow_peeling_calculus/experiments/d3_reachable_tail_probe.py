#!/usr/bin/env python3
"""Preregistered O1 depth-three arctan reachable-tail probe.

Learned matrices are retained as exact Euler rank-one histories.  Every
forward/transpose call therefore reuses the same Gaussian source and learned
operator without materializing the latter densely.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import torch


CLIPS = [None, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0]
SAVE_TIMES = [0.0, 0.25, 0.5, 1.0]
POWERS = [2, 3, 4, 6, 8, 10, 12, 16]
TAIL_LEVELS = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]


def learned_forward(b_hist, x_hist, count, v, h, n):
    if count == 0:
        return torch.zeros_like(v)
    coeff = torch.einsum("cns,cn->cs", x_hist[:, :, :count], v) / n
    return h * torch.einsum("cns,cs->cn", b_hist[:, :, :count], coeff)


def learned_transpose(b_hist, x_hist, count, v, h, n):
    if count == 0:
        return torch.zeros_like(v)
    coeff = torch.einsum("cns,cn->cs", b_hist[:, :, :count], v) / n
    return h * torch.einsum("cns,cs->cn", x_hist[:, :, :count], coeff)


def forward_backward(A, u, gamma1, gamma2, histories, count, h):
    b2_hist, x1_hist, b3_hist, x2_hist = histories
    n = u.shape[1]
    x1 = torch.atan(u)
    z2 = x1 @ gamma1.T + learned_forward(b2_hist, x1_hist, count, x1, h, n)
    x2 = torch.atan(z2)
    z3 = x2 @ gamma2.T + learned_forward(b3_hist, x2_hist, count, x2, h, n)
    x3 = torch.atan(z3)
    b3 = A / (1.0 + z3.square())
    r2 = b3 @ gamma2 + learned_transpose(b3_hist, x2_hist, count, b3, h, n)
    clipped_r2 = r2.clone()
    for c, radius in enumerate(CLIPS):
        if radius is not None:
            clipped_r2[c].clamp_(min=-radius, max=radius)
    b2 = clipped_r2 / (1.0 + z2.square())
    r1 = b2 @ gamma1 + learned_transpose(b2_hist, x1_hist, count, b2, h, n)
    b1 = r1 / (1.0 + u.square())
    return x1, z2, x2, z3, x3, b3, r2, b2, r1, b1


def stable_empirical_moment(abs_v, power, n):
    positive = abs_v > 0
    if not bool(positive.any()):
        return 0.0, 0.0
    logs = torch.log(abs_v[positive])
    log_sum = torch.logsumexp(power * logs, dim=0)
    log_sum_sq = torch.logsumexp(2 * power * logs, dim=0)
    moment = torch.exp((log_sum - math.log(n)) / power).item()
    effective_count = torch.exp(2 * log_sum - log_sum_sq).item()
    return moment, effective_count


def add_statistics(rows, width, trial, step, time, A, u, values):
    x1, z2, x2, z3, x3, b3, r2, b2, r1, b1 = values
    n = width
    raw_r2 = r2[0]
    for c, radius in enumerate(CLIPS):
        rv = r2[c]
        base = {
            "width": width,
            "trial": trial,
            "step": step,
            "time": time,
            "clip": "raw" if radius is None else radius,
            "A_l2": torch.linalg.vector_norm(A[c]).item() / math.sqrt(n),
            "u_l2": torch.linalg.vector_norm(u[c]).item() / math.sqrt(n),
            "r2_l2": torch.linalg.vector_norm(rv).item() / math.sqrt(n),
            "r2_max": rv.abs().max().item(),
            "b3_l2": torch.linalg.vector_norm(b3[c]).item() / math.sqrt(n),
            "b2_l2": torch.linalg.vector_norm(b2[c]).item() / math.sqrt(n),
            "b1_l2": torch.linalg.vector_norm(b1[c]).item() / math.sqrt(n),
            "predictor": torch.mean(A[c] * x3[c]).item(),
            "kernel": (
                torch.mean(x3[c].square())
                + torch.mean(b3[c].square()) * torch.mean(x2[c].square())
                + torch.mean(b2[c].square()) * torch.mean(x1[c].square())
                + torch.mean(b1[c].square())
            ).item(),
            "delta_A_raw": torch.linalg.vector_norm(A[c] - A[0]).item() / math.sqrt(n),
            "delta_u_raw": torch.linalg.vector_norm(u[c] - u[0]).item() / math.sqrt(n),
            "delta_r2_raw": torch.linalg.vector_norm(rv - raw_r2).item() / math.sqrt(n),
        }
        abs_r = rv.abs().to(torch.float64)
        for p in POWERS:
            mp, effective_count = stable_empirical_moment(abs_r, p, n)
            base[f"M{p}"] = mp
            base[f"M{p}_over_sqrtp"] = mp / math.sqrt(p)
            base[f"M{p}_over_p"] = mp / p
            base[f"M{p}_effective_count"] = effective_count
        for threshold in TAIL_LEVELS:
            excess = torch.clamp(abs_r - threshold, min=0.0)
            base[f"tau_{threshold:g}"] = torch.sqrt(torch.mean(excess.square())).item()
            base[f"count_{threshold:g}"] = int((abs_r > threshold).sum().item())
        rows.append(base)


def run_one(width, trial, dt, horizon, device, dtype):
    steps = int(round(horizon / dt))
    if abs(steps * dt - horizon) > 1e-10:
        raise ValueError("horizon must be an integer multiple of dt")
    generator = torch.Generator(device=device)
    generator.manual_seed(9173 + 1000003 * width + 7919 * trial)
    scale = 1.0 / math.sqrt(width)
    gamma1 = torch.randn((width, width), generator=generator, device=device, dtype=dtype) * scale
    gamma2 = torch.randn((width, width), generator=generator, device=device, dtype=dtype) * scale
    A0 = torch.randn(width, generator=generator, device=device, dtype=dtype)
    u0 = torch.randn(width, generator=generator, device=device, dtype=dtype)
    configs = len(CLIPS)
    A = A0.expand(configs, -1).clone()
    u = u0.expand(configs, -1).clone()
    histories = tuple(
        torch.empty((configs, width, steps), device=device, dtype=dtype)
        for _ in range(4)
    )
    b2_hist, x1_hist, b3_hist, x2_hist = histories
    save_steps = {int(round(t / dt)): t for t in SAVE_TIMES if t <= horizon + 1e-12}
    rows = []
    with torch.no_grad():
        for step in range(steps + 1):
            values = forward_backward(A, u, gamma1, gamma2, histories, step, dt)
            if step in save_steps:
                add_statistics(rows, width, trial, step, save_steps[step], A, u, values)
            if step == steps:
                break
            x1, _, x2, _, x3, b3, _, b2, _, b1 = values
            x1_hist[:, :, step] = x1
            b2_hist[:, :, step] = b2
            x2_hist[:, :, step] = x2
            b3_hist[:, :, step] = b3
            A.add_(x3, alpha=dt)
            u.add_(b1, alpha=dt)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", default="1024,2048,4096")
    parser.add_argument("--trials", type=int, default=4)
    parser.add_argument("--dt", type=float, default=0.005)
    parser.add_argument("--horizon", type=float, default=1.0)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=["float32", "float64"], default="float32")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    widths = [int(x) for x in args.widths.split(",") if x]
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")
    all_rows = []
    for width in widths:
        for trial in range(args.trials):
            all_rows.extend(run_one(width, trial, args.dt, args.horizon, device, dtype))
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    with (output / "raw.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(all_rows[0]))
        writer.writeheader()
        writer.writerows(all_rows)
    metadata = {
        "widths": widths,
        "trials": args.trials,
        "dt": args.dt,
        "horizon": args.horizon,
        "device": str(device),
        "dtype": args.dtype,
        "clips": CLIPS,
        "save_times": SAVE_TIMES,
        "powers": POWERS,
        "tail_levels": TAIL_LEVELS,
        "torch": torch.__version__,
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"rows": len(all_rows), **metadata}, indent=2))


if __name__ == "__main__":
    main()
