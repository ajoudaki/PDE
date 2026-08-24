"""Preregistered evidence run for the adaptive middle adjoint.

This integrates the exact unclipped feature-time flow.  It is not a proof and
does not alter any claim status.  See EXPERIMENT_PREREGISTRATION_2026-08-23.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from pathlib import Path

import numpy as np


def inv_theta(r: np.ndarray) -> np.ndarray:
    return 2.0 * np.sinh(np.arcsinh(1.5 * r) / 3.0)


def derived(state, gamma1: np.ndarray, gamma2: np.ndarray):
    a, r, p1, p2 = state
    g1 = gamma1 + p1
    g2 = gamma2 + p2
    u = inv_theta(r)
    d1 = 1.0 / (1.0 + u * u)
    x1 = np.arctan(u)
    z2 = g1 @ x1
    d2 = 1.0 / (1.0 + z2 * z2)
    x2 = np.arctan(z2)
    z3 = g2 @ x2
    d3 = 1.0 / (1.0 + z3 * z3)
    x3 = np.arctan(z3)
    b3 = a * d3
    r2_static = gamma2.T @ b3
    r2_learned = p2.T @ b3
    r2 = r2_static + r2_learned
    b2 = d2 * r2
    q1 = g1.T @ b2
    f = float(np.mean(a * x3))
    energies = (
        float(np.mean(x3 * x3)),
        float(np.mean(b3 * b3) * np.mean(x2 * x2)),
        float(np.mean(b2 * b2) * np.mean(x1 * x1)),
        float(np.mean((d1 * q1) ** 2)),
    )
    return {
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "b3": b3,
        "r2": r2,
        "r2_static": r2_static,
        "r2_learned": r2_learned,
        "b2": b2,
        "q1": q1,
        "f": f,
        "energies": energies,
        "K": float(sum(energies)),
    }


def rhs(state, gamma1: np.ndarray, gamma2: np.ndarray):
    d = derived(state, gamma1, gamma2)
    n = state[0].size
    return (
        d["x3"],
        d["q1"],
        np.outer(d["b2"], d["x1"]) / n,
        np.outer(d["b3"], d["x2"]) / n,
    )


def add(state, tangent, scale: float):
    return tuple(x + scale * dx for x, dx in zip(state, tangent))


def rk4(state, gamma1: np.ndarray, gamma2: np.ndarray, h: float):
    k1 = rhs(state, gamma1, gamma2)
    k2 = rhs(add(state, k1, h / 2.0), gamma1, gamma2)
    k3 = rhs(add(state, k2, h / 2.0), gamma1, gamma2)
    k4 = rhs(add(state, k3, h), gamma1, gamma2)
    return tuple(
        x + h * (v1 + 2.0 * v2 + 2.0 * v3 + v4) / 6.0
        for x, v1, v2, v3, v4 in zip(state, k1, k2, k3, k4)
    )


def field_stats(v: np.ndarray):
    abs_v = np.abs(v)
    l2 = float(np.sqrt(np.mean(v * v)))
    scale = l2 if l2 > 0.0 else 1.0
    result = {
        "max": float(np.max(abs_v)),
        "condensation": float(np.max(abs_v) / (np.sqrt(v.size) * scale)),
        "survival_std": {
            str(q): float(np.mean(abs_v > q * scale)) for q in (2, 3, 4, 5)
        },
    }
    for p in (2, 4, 6, 8):
        lp = float(np.mean(abs_v**p) ** (1.0 / p))
        result[f"l{p}"] = lp
        result[f"l{p}_over_p"] = lp / p
    return result


def snapshot(state, gamma1: np.ndarray, gamma2: np.ndarray, s: float,
             retain_b3: bool):
    d = derived(state, gamma1, gamma2)
    record = {
        "s": float(s),
        "f": d["f"],
        "K": d["K"],
        "energies": list(d["energies"]),
        "r2": field_stats(d["r2"]),
        "r2_static": field_stats(d["r2_static"]),
        "r2_learned": field_stats(d["r2_learned"]),
    }
    return record, (d["b3"].copy() if retain_b3 else None), d["K"]


def integrate(initial_state, gamma1: np.ndarray, gamma2: np.ndarray,
              horizon: float, step: float, checkpoint: float = 0.1,
              retain_b3: bool = False):
    steps_float = horizon / step
    if abs(steps_float - round(steps_float)) > 1e-10:
        raise ValueError("horizon must be an integer multiple of step")
    checkpoint_float = checkpoint / step
    if abs(checkpoint_float - round(checkpoint_float)) > 1e-10:
        raise ValueError("checkpoint must be an integer multiple of step")
    steps = int(round(steps_float))
    checkpoint_steps = int(round(checkpoint_float))
    state = tuple(x.copy() for x in initial_state)
    records = []
    b3_path = []
    integral_k = 0.0
    previous_k = None
    for k in range(steps + 1):
        d = derived(state, gamma1, gamma2)
        if previous_k is not None:
            integral_k += step * (previous_k + d["K"]) / 2.0
        previous_k = d["K"]
        if k % checkpoint_steps == 0:
            record, b3, _ = snapshot(
                state, gamma1, gamma2, k * step, retain_b3
            )
            records.append(record)
            if retain_b3:
                b3_path.append(b3)
        if k < steps:
            state = rk4(state, gamma1, gamma2, step)
    f0 = records[0]["f"]
    f1 = records[-1]["f"]
    solver_identity_defect = abs((f1 - f0) - integral_k) / (1.0 + abs(f1 - f0))
    return {
        "records": records,
        "b3_path": b3_path,
        "solver_identity_defect": float(solver_identity_defect),
    }


def initialization(n: int, seed: int):
    rng = np.random.default_rng(seed)
    a0 = rng.normal(size=n)
    u0 = rng.normal(size=n)
    r0 = u0 + u0**3 / 3.0
    gamma1 = rng.normal(size=(n, n)) / np.sqrt(n)
    gamma2 = rng.normal(size=(n, n)) / np.sqrt(n)
    zeros = np.zeros((n, n), dtype=np.float64)
    return rng, (a0, r0, zeros, zeros.copy()), gamma1, gamma2


def run_seed(n: int, seed: int, horizon: float, step: float,
             cavity_columns: int):
    start = time.monotonic()
    rng, initial_state, gamma1, gamma2 = initialization(n, seed)
    main = integrate(
        initial_state, gamma1, gamma2, horizon, step, retain_b3=cavity_columns > 0
    )
    cavities = []
    if cavity_columns > 0:
        columns = rng.choice(n, size=min(cavity_columns, n), replace=False)
        for j_raw in columns:
            j = int(j_raw)
            column = gamma2[:, j].copy()
            gamma2_cavity = gamma2.copy()
            gamma2_cavity[:, j] = 0.0
            cavity = integrate(
                initial_state, gamma1, gamma2_cavity, horizon, step,
                retain_b3=True,
            )
            response_records = []
            for main_record, b3, b3_cavity in zip(
                main["records"], main["b3_path"], cavity["b3_path"]
            ):
                h_j = float(column @ b3_cavity)
                delta_j = float(column @ (b3 - b3_cavity))
                cavity_l2 = float(np.sqrt(np.mean(b3_cavity * b3_cavity)))
                path_difference = float(np.sqrt(np.mean((b3 - b3_cavity) ** 2)))
                response_records.append({
                    "s": main_record["s"],
                    "H_std": abs(h_j) / max(cavity_l2, np.finfo(float).tiny),
                    "delta_abs": abs(delta_j),
                    "delta_relative": abs(delta_j) / (1.0 + abs(h_j)),
                    "b3_path_difference_l2": path_difference,
                })
            cavities.append({
                "column": j,
                "solver_identity_defect": cavity["solver_identity_defect"],
                "records": response_records,
            })
    main.pop("b3_path", None)
    return {
        "n": n,
        "seed": seed,
        "horizon": horizon,
        "step": step,
        "main": main,
        "cavities": cavities,
        "wall_seconds": time.monotonic() - start,
    }


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", type=int, nargs="+", required=True)
    parser.add_argument("--seeds", type=int, nargs="+", required=True)
    parser.add_argument("--horizon", type=float, default=2.0)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--cavity-columns", type=int, default=0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    metadata = {
        "kind": "metadata",
        "script_sha256": script_sha256(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "platform": platform.platform(),
        "arguments": vars(args) | {"output": str(args.output)},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps(metadata, sort_keys=True) + "\n")
        handle.flush()
        for n in args.widths:
            for seed in args.seeds:
                result = run_seed(
                    n=n,
                    seed=seed + n,
                    horizon=args.horizon,
                    step=args.step,
                    cavity_columns=args.cavity_columns,
                )
                handle.write(json.dumps(result, sort_keys=True) + "\n")
                handle.flush()
                print(
                    f"n={n} seed={seed+n} cavities={args.cavity_columns} "
                    f"wall={result['wall_seconds']:.2f}s",
                    flush=True,
                )


if __name__ == "__main__":
    main()

