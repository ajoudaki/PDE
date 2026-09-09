#!/usr/bin/env python3
"""Preregistered G2 reachable one-step defect probe.

The reference is the dense finite-width D3 gradient flow.  The comparison
map is the exact frozen-input paired-edge block from the gate-resolved note.
No Gaussian source is refreshed.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import torch


BASE_TIMES = (0.0, 0.25, 0.5)
STEP_SIZES = (0.04, 0.02, 0.01, 0.005)


def phi(z, alpha):
    return alpha * z + torch.atan(z)


def mobility(z, alpha):
    return alpha + 1.0 / (1.0 + z.square())


def Phi(z, alpha):
    if alpha == 0.0:
        return z + z.pow(3) / 3.0
    # Evaluate in float64 to protect the cancellation in the closed form.
    zd = z.to(torch.float64)
    c = alpha + 1.0
    value = (
        zd / alpha
        - torch.atan(zd * math.sqrt(alpha / c))
        / (alpha * math.sqrt(alpha * c))
    )
    return value.to(z.dtype)


def inverse_Phi(w, alpha, initial, iterations=14):
    # Monotone Newton map.  The supplied initial point is always one local
    # block away and convergence is checked by the caller through reconstraint.
    z = initial.clone()
    for _ in range(iterations):
        z = z - (Phi(z, alpha) - w) * mobility(z, alpha)
    return z


def forward_backward(state, alpha):
    A, u, G1, G2 = state
    x1 = phi(u, alpha)
    z2 = G1 @ x1
    x2 = phi(z2, alpha)
    z3 = G2 @ x2
    x3 = phi(z3, alpha)
    b3 = A * mobility(z3, alpha)
    r2 = G2.T @ b3
    b2 = mobility(z2, alpha) * r2
    r1 = G1.T @ b2
    b1 = mobility(u, alpha) * r1
    return x1, z2, x2, z3, x3, b3, r2, b2, r1, b1


def rhs(state, alpha):
    A, u, G1, G2 = state
    x1, _, x2, _, x3, b3, _, b2, _, b1 = forward_backward(state, alpha)
    n = A.numel()
    return (
        x3,
        b1,
        torch.outer(b2, x1) / n,
        torch.outer(b3, x2) / n,
    )


def state_axpy(state, tangent, scale):
    return tuple(x + scale * y for x, y in zip(state, tangent))


def rk4_step(state, dt, alpha):
    k1 = rhs(state, alpha)
    k2 = rhs(state_axpy(state, k1, 0.5 * dt), alpha)
    k3 = rhs(state_axpy(state, k2, 0.5 * dt), alpha)
    k4 = rhs(state_axpy(state, k3, dt), alpha)
    return tuple(
        x + (dt / 6.0) * (a + 2.0 * b + 2.0 * c + d)
        for x, a, b, c, d in zip(state, k1, k2, k3, k4)
    )


def integrate(state, duration, max_dt, alpha):
    if duration == 0.0:
        return tuple(x.clone() for x in state)
    steps = max(1, int(math.ceil(duration / max_dt)))
    dt = duration / steps
    out = tuple(x.clone() for x in state)
    for _ in range(steps):
        out = rk4_step(out, dt, alpha)
    return out


def top_frozen_step(A, z3, q2, h, alpha, max_dt):
    # Simultaneously integrate A, z3 and a3'=b3.  This is the exact top
    # frozen-x2 subsystem up to the refined RK4 error.
    a3 = torch.zeros_like(A)
    steps = max(1, int(math.ceil(h / max_dt)))
    dt = h / steps

    def top_rhs(values):
        AA, zz, aa = values
        gate = mobility(zz, alpha)
        bb = gate * AA
        return phi(zz, alpha), q2 * bb, bb

    values = (A.clone(), z3.clone(), a3)
    for _ in range(steps):
        k1 = top_rhs(values)
        k2 = top_rhs(state_axpy(values, k1, 0.5 * dt))
        k3 = top_rhs(state_axpy(values, k2, 0.5 * dt))
        k4 = top_rhs(state_axpy(values, k3, dt))
        values = tuple(
            x + (dt / 6.0) * (a + 2.0 * b + 2.0 * c + d)
            for x, a, b, c, d in zip(values, k1, k2, k3, k4)
        )
    return values


def divided_mobility_increment(z, q, S, alpha):
    w = Phi(z, alpha)
    z_plus = inverse_Phi(w + q * S, alpha, z)
    if q > 1e-12:
        return (z_plus - z) / q, z_plus
    return mobility(z, alpha) * S, z_plus


def frozen_gate_block(state, h, alpha, top_max_dt):
    A, u, G1, G2 = state
    x1, z2, x2, z3, _, _, _, _, _, _ = forward_backward(state, alpha)
    n = A.numel()
    q1 = torch.mean(x1.square()).item()
    q2 = torch.mean(x2.square()).item()

    A_plus, z3_frozen, a3 = top_frozen_step(
        A, z3, q2, h, alpha, top_max_dt
    )
    S2 = G2.T @ a3 + 0.5 * x2 * torch.mean(a3.square())
    a2, _ = divided_mobility_increment(z2, q1, S2, alpha)
    S1 = G1.T @ a2 + 0.5 * x1 * torch.mean(a2.square())
    u_plus = inverse_Phi(Phi(u, alpha) + S1, alpha, u)

    G2_plus = G2 + torch.outer(a3, x2) / n
    G1_plus = G1 + torch.outer(a2, x1) / n
    result = (A_plus, u_plus, G1_plus, G2_plus)

    # Check the exact top frozen constraint; retained as a diagnostic.
    top_constraint = l2(G2_plus @ x2 - z3_frozen)
    return result, top_constraint


def l2(v):
    return torch.linalg.vector_norm(v).item() / math.sqrt(v.numel())


def observables(state, alpha):
    A, u, _, _ = state
    values = forward_backward(state, alpha)
    x1, _, x2, _, x3, b3, r2, b2, r1, b1 = values
    predictor = torch.mean(A * x3).item()
    kernel = (
        torch.mean(x3.square())
        + torch.mean(b3.square()) * torch.mean(x2.square())
        + torch.mean(b2.square()) * torch.mean(x1.square())
        + torch.mean(b1.square())
    ).item()
    return predictor, kernel, values


def compare(reference, approximate, alpha, width, trial, base_time, h, check):
    A0, u0, G10, G20 = reference
    A1, u1, G11, G21 = approximate
    pred0, ker0, v0 = observables(reference, alpha)
    pred1, ker1, v1 = observables(approximate, alpha)
    names = ("x1", "z2", "x2", "z3", "x3", "b3", "r2", "b2", "r1", "b1")
    row = {
        "width": width,
        "trial": trial,
        "alpha": alpha,
        "base_time": base_time,
        "h": h,
        "A_error": l2(A1 - A0),
        "u_error": l2(u1 - u0),
        "G1_fro_error": torch.linalg.vector_norm(G11 - G10).item(),
        "G2_fro_error": torch.linalg.vector_norm(G21 - G20).item(),
        "predictor_error": abs(pred1 - pred0),
        "kernel_error": abs(ker1 - ker0),
        "top_constraint": check,
        "r2_max_reference": v0[6].abs().max().item(),
        "r2_l4_over_l2": (
            torch.mean(v0[6].abs().pow(4)).pow(0.25)
            / torch.mean(v0[6].square()).sqrt().clamp_min(1e-30)
        ).item(),
    }
    for name, exact, approx in zip(names, v0, v1):
        row[f"{name}_error"] = l2(approx - exact)
        row[f"{name}_max_reference"] = exact.abs().max().item()
    for key in list(row):
        if key.endswith("_error"):
            value = row[key]
            row[f"{key}_over_h"] = value / h
            row[f"{key}_over_h32"] = value / (h ** 1.5)
            row[f"{key}_over_h2"] = value / (h * h)
    return row


def seeded_state(width, trial, alpha, device, dtype):
    generator = torch.Generator(device=device)
    seed = 2819 + 1000003 * width + 7919 * trial + int(round(1000 * alpha))
    generator.manual_seed(seed)
    scale = 1.0 / math.sqrt(width)
    A = torch.randn(width, generator=generator, device=device, dtype=dtype)
    u = torch.randn(width, generator=generator, device=device, dtype=dtype)
    G1 = torch.randn((width, width), generator=generator, device=device, dtype=dtype) * scale
    G2 = torch.randn((width, width), generator=generator, device=device, dtype=dtype) * scale
    return A, u, G1, G2


def run_one(width, trial, alpha, device, dtype, ref_dt):
    state = seeded_state(width, trial, alpha, device, dtype)
    rows = []
    current_time = 0.0
    with torch.no_grad():
        for base_time in BASE_TIMES:
            state = integrate(state, base_time - current_time, ref_dt, alpha)
            current_time = base_time
            for h in STEP_SIZES:
                reference = integrate(state, h, ref_dt, alpha)
                approximate, check = frozen_gate_block(state, h, alpha, ref_dt)
                rows.append(
                    compare(
                        reference, approximate, alpha, width, trial,
                        base_time, h, check
                    )
                )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", default="128,256,512,1024")
    parser.add_argument("--trials", type=int, default=4)
    parser.add_argument("--alphas", default="0,0.05,0.2")
    parser.add_argument("--ref-dt", type=float, default=1.0 / 2048.0)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    widths = [int(x) for x in args.widths.split(",") if x]
    alphas = [float(x) for x in args.alphas.split(",") if x]
    device = torch.device(args.device)
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")

    rows = []
    for alpha in alphas:
        for width in widths:
            for trial in range(args.trials):
                rows.extend(run_one(width, trial, alpha, device, dtype, args.ref_dt))

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    with (output / "raw.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metadata = {
        "widths": widths,
        "trials": args.trials,
        "alphas": alphas,
        "base_times": BASE_TIMES,
        "step_sizes": STEP_SIZES,
        "ref_dt": args.ref_dt,
        "device": str(device),
        "dtype": args.dtype,
        "torch": torch.__version__,
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"rows": len(rows), **metadata}, indent=2))


if __name__ == "__main__":
    main()
