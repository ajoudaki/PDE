#!/usr/bin/env python3
"""Run the preregistered middle-query first-passage diagnostic."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import torch


LEVELS = (1.5, 2.0, 3.0)
MASTER_SEED = 2026082389


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

    dx1 = d1.square() * q1
    self_term = x1.square().mean(dim=1, keepdim=True) * b2
    bath = torch.bmm(G1, dx1.unsqueeze(-1)).squeeze(-1)
    v2 = self_term + bath
    dx2 = d2 * v2
    dz3 = x2.square().mean(dim=1, keepdim=True) * b3
    dz3 = dz3 + torch.bmm(G2, dx2.unsqueeze(-1)).squeeze(-1)
    db3 = d3 * x3 - 2.0 * z3 * d3 * b3 * dz3
    dr2 = b3.square().mean(dim=1, keepdim=True) * x2
    dr2 = dr2 + torch.bmm(G2.transpose(1, 2), db3.unsqueeze(-1)).squeeze(-1)
    return {
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "d1": d1,
        "d2": d2,
        "d3": d3,
        "z2": z2,
        "z3": z3,
        "b3": b3,
        "r2": r2,
        "b2": b2,
        "q1": q1,
        "du": du,
        "S": self_term,
        "H": bath,
        "V": v2,
        "dz3": dz3,
        "db3": db3,
        "dr2": dr2,
    }


def midpoint_step(A, u, G1, G2, h):
    f = fields(A, u, G1, G2)
    half = 0.5 * h
    n = A.shape[1]
    Am = A + half * f["x3"]
    um = u + half * f["du"]
    G1m = G1 + (half / n) * f["b2"].unsqueeze(2) * f["x1"].unsqueeze(1)
    G2m = G2 + (half / n) * f["b3"].unsqueeze(2) * f["x2"].unsqueeze(1)
    fm = fields(Am, um, G1m, G2m)
    return (
        A + h * fm["x3"],
        u + h * fm["du"],
        G1 + (h / n) * fm["b2"].unsqueeze(2) * fm["x1"].unsqueeze(1),
        G2 + (h / n) * fm["b3"].unsqueeze(2) * fm["x2"].unsqueeze(1),
    )


def blank_summary(shape, device, dtype):
    nan = torch.full(shape, float("nan"), device=device, dtype=dtype)
    zero = torch.zeros(shape, device=device, dtype=dtype)
    false = torch.zeros(shape, device=device, dtype=torch.bool)
    return {
        "seen": false.clone(),
        "open_misaligned_at_cross": false.clone(),
        "cross_time": nan.clone(),
        "cross_D": nan.clone(),
        "cross_ZR": nan.clone(),
        "cross_coop": nan.clone(),
        "cross_Rgrowth": nan.clone(),
        "cross_opp_ratio": nan.clone(),
        "time_align": nan.clone(),
        "time_close": nan.clone(),
        "time_exit": nan.clone(),
        "occupation_O": zero.clone(),
        "occupation_C": zero.clone(),
        "run_O": zero.clone(),
        "run_C": zero.clone(),
        "longest_O": zero.clone(),
        "longest_C": zero.clone(),
    }


def update_summary(summary, f, previous_abs, level, t, h):
    r = f["r2"]
    abs_r = r.abs()
    d = f["d2"]
    z = f["z2"]
    s = f["S"]
    bath = f["H"]
    v = f["V"]
    sign_r = torch.sign(r)
    aligned = z * r > 0.0
    open_gate = d >= 0.5
    above = abs_r >= level
    open_misaligned = above & open_gate & (~aligned)
    slow = open_misaligned & (sign_r * v <= s.abs() / 4.0)

    crossing = (~summary["seen"]) & (previous_abs < level) & above
    summary["seen"] |= crossing
    summary["open_misaligned_at_cross"] |= crossing & open_misaligned
    eps = 1.0e-12
    opposing = s * bath < 0.0
    opp_ratio = torch.where(opposing, bath.abs() / (s.abs() + eps),
                            torch.full_like(r, float("nan")))
    values = {
        "cross_time": torch.full_like(r, t),
        "cross_D": d,
        "cross_ZR": z * r,
        "cross_coop": sign_r * v / (s.abs() + bath.abs() + eps),
        "cross_Rgrowth": sign_r * f["dr2"],
        "cross_opp_ratio": opp_ratio,
    }
    for name, value in values.items():
        summary[name] = torch.where(crossing, value, summary[name])

    active = summary["seen"]
    unresolved_align = active & torch.isnan(summary["time_align"])
    unresolved_close = active & torch.isnan(summary["time_close"])
    unresolved_exit = active & torch.isnan(summary["time_exit"])
    elapsed = torch.clamp(torch.full_like(r, t) - summary["cross_time"], min=0.0)
    summary["time_align"] = torch.where(unresolved_align & aligned, elapsed,
                                          summary["time_align"])
    summary["time_close"] = torch.where(unresolved_close & (~open_gate), elapsed,
                                          summary["time_close"])
    summary["time_exit"] = torch.where(unresolved_exit & (abs_r < level), elapsed,
                                         summary["time_exit"])

    summary["occupation_O"] += h * open_misaligned.to(r.dtype)
    summary["occupation_C"] += h * slow.to(r.dtype)
    summary["run_O"] = torch.where(open_misaligned, summary["run_O"] + h,
                                     torch.zeros_like(r))
    summary["run_C"] = torch.where(slow, summary["run_C"] + h,
                                     torch.zeros_like(r))
    summary["longest_O"] = torch.maximum(summary["longest_O"], summary["run_O"])
    summary["longest_C"] = torch.maximum(summary["longest_C"], summary["run_C"])


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def directional_derivative_audit(A, u, G1, G2, dtype):
    """Centered-difference audit of the three displayed velocity formulas."""
    f = fields(A, u, G1, G2)
    n = A.shape[1]
    dA = f["x3"]
    du = f["du"]
    dG1 = f["b2"].unsqueeze(2) * f["x1"].unsqueeze(1) / n
    dG2 = f["b3"].unsqueeze(2) * f["x2"].unsqueeze(1) / n
    eps = 5.0e-3 if dtype == torch.float32 else 2.0e-6
    fp = fields(A + eps * dA, u + eps * du,
                G1 + eps * dG1, G2 + eps * dG2)
    fm = fields(A - eps * dA, u - eps * du,
                G1 - eps * dG1, G2 - eps * dG2)
    numerical = {
        "z2": (fp["z2"] - fm["z2"]) / (2.0 * eps),
        "z3": (fp["z3"] - fm["z3"]) / (2.0 * eps),
        "r2": (fp["r2"] - fm["r2"]) / (2.0 * eps),
    }
    exact = {"z2": f["V"], "z3": f["dz3"], "r2": f["dr2"]}
    result = {}
    for name in numerical:
        delta = (numerical[name] - exact[name]).to(torch.float64)
        scale = exact[name].to(torch.float64).square().mean(dim=1).sqrt()
        rms = delta.square().mean(dim=1).sqrt()
        result[f"fd_{name}_rms"] = rms.cpu().numpy()
        result[f"fd_{name}_relative"] = (rms / (scale + 1.0e-12)).cpu().numpy()
    return result


@torch.no_grad()
def simulate_chunk(n, start, count, step, horizon, device, dtype,
                   draw_float64, seed_offset):
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

    steps = int(round(horizon / step))
    if abs(steps * step - horizon) > 1.0e-10:
        raise ValueError("step must divide horizon")
    shape = (count, n)
    summaries = {level: blank_summary(shape, device, dtype) for level in LEVELS}
    derivative_audit = directional_derivative_audit(A, u, G1, G2, dtype)
    f = fields(A, u, G1, G2)
    previous_abs = f["r2"].abs() + 1.0e-7
    max_identity_residual = torch.zeros(count, device=device, dtype=torch.float64)
    max_dz3_residual = torch.zeros(count, device=device, dtype=torch.float64)
    max_dr2_residual = torch.zeros(count, device=device, dtype=torch.float64)

    for k in range(steps + 1):
        t = k * step
        f = fields(A, u, G1, G2)
        algebra = (f["V"] - f["S"] - f["H"]).abs().amax(dim=1)
        max_identity_residual = torch.maximum(max_identity_residual,
                                               algebra.to(torch.float64))
        dG2 = f["b3"].unsqueeze(2) * f["x2"].unsqueeze(1) / n
        dz3_direct = torch.bmm(dG2, f["x2"].unsqueeze(-1)).squeeze(-1)
        dz3_direct += torch.bmm(G2, (f["d2"] * f["V"]).unsqueeze(-1)).squeeze(-1)
        dr2_direct = torch.bmm(dG2.transpose(1, 2),
                               f["b3"].unsqueeze(-1)).squeeze(-1)
        dr2_direct += torch.bmm(G2.transpose(1, 2),
                                f["db3"].unsqueeze(-1)).squeeze(-1)
        dz3_error = (f["dz3"] - dz3_direct).abs().amax(dim=1)
        dr2_error = (f["dr2"] - dr2_direct).abs().amax(dim=1)
        max_dz3_residual = torch.maximum(max_dz3_residual,
                                         dz3_error.to(torch.float64))
        max_dr2_residual = torch.maximum(max_dr2_residual,
                                         dr2_error.to(torch.float64))
        interval = step if k < steps else 0.0
        for level in LEVELS:
            update_summary(summaries[level], f, previous_abs, level, t, interval)
        previous_abs = f["r2"].abs()
        if k < steps:
            A, u, G1, G2 = midpoint_step(A, u, G1, G2, step)

    output = {"identity_residual": max_identity_residual.cpu().numpy(),
              "dz3_identity_residual": max_dz3_residual.cpu().numpy(),
              "dr2_identity_residual": max_dr2_residual.cpu().numpy(),
              **derivative_audit}
    for level, summary in summaries.items():
        key = str(level).replace(".", "p")
        for name, value in summary.items():
            output[f"L{key}_{name}"] = value.cpu().numpy()
    return seed, output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--replicas", type=int, required=True)
    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--horizon", type=float, default=4.0)
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
            args.width, start, count, args.step, args.horizon, device, dtype,
            args.draw_float64, args.seed_offset,
        )
        chunks.append(records)
        seeds.append((start, count, seed))
        print(json.dumps({"width": args.width, "done": start + count,
                          "seconds": time.time() - started}), flush=True)

    payload = {
        "width": np.asarray(args.width),
        "replicas": np.asarray(args.replicas),
        "step": np.asarray(args.step),
        "horizon": np.asarray(args.horizon),
        "dtype": np.asarray(args.dtype),
        "draw_float64": np.asarray(args.draw_float64),
        "seed_offset": np.asarray(args.seed_offset),
        "script_sha256": np.asarray(script_sha256()),
        "batch_seed_table": np.asarray(seeds, dtype=np.int64),
    }
    for name in chunks[0]:
        payload[name] = np.concatenate([chunk[name] for chunk in chunks], axis=0)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    target = args.output_dir / f"first_passage_{args.tag}_n{args.width}.npz"
    np.savez_compressed(target, **payload)
    print(json.dumps({"saved": str(target), "seconds": time.time() - started}),
          flush=True)


if __name__ == "__main__":
    main()
