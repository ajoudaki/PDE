"""Preregistered diagnostics for diagonal arctan loop erasure.

This is evidence only.  See DIAGONAL_GAUGE_EXPERIMENT_PREREGISTRATION_2026-08-23.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from pathlib import Path

import numpy as np

from experiment_middle_response import (
    add,
    derived,
    field_stats,
    initialization,
    inv_theta,
    rhs,
    rk4,
)


def theta(v: np.ndarray) -> np.ndarray:
    return v + v**3 / 3.0


def extended(state, gamma1, gamma2, sampled_rows):
    base = derived(state, gamma1, gamma2)
    a, r, p1, p2 = state
    g1 = gamma1 + p1
    g2 = gamma2 + p2
    u = inv_theta(r)
    d1 = 1.0 / (1.0 + u * u)
    z2 = g1 @ base["x1"]
    d2 = 1.0 / (1.0 + z2 * z2)
    z3 = g2 @ base["x2"]
    d3 = 1.0 / (1.0 + z3 * z3)

    a1 = float(np.mean(base["x1"] ** 2))
    gt_b2 = g1.T @ base["b2"]
    z2_dot = a1 * base["b2"] + g1 @ ((d1 * d1) * gt_b2)
    kappa2 = a1 + (g1 * g1) @ (d1 * d1)
    y2 = z2_dot - kappa2 * base["b2"]
    ratio2 = -2.0 * z2 / (1.0 + z2 * z2)
    c2 = ratio2 * y2
    x2_dot = d2 * z2_dot
    a2 = float(np.mean(base["x2"] ** 2))
    z3_dot = a2 * base["b3"] + g2 @ x2_dot

    kappa3 = []
    y3 = []
    c3 = []
    for raw_i in sampled_rows:
        i = int(raw_i)
        v = d2 * g2[i, :]
        k_i = a2 + a1 * float(v @ v) + float(
            ((d1 * (g1.T @ v)) ** 2).sum()
        )
        yy = float(z3_dot[i] - k_i * base["b3"][i])
        kappa3.append(k_i)
        y3.append(yy)
        c3.append(float(-2.0 * z3[i] / (1.0 + z3[i] ** 2) * yy))

    count = max(1, int(np.ceil(0.01 * z2.size)))
    selected = np.argpartition(np.abs(base["r2"]), -count)[-count:]
    denom = float(np.sqrt(np.mean(c2 * c2)))
    leverage = float(np.sqrt(np.mean(c2[selected] ** 2)) / max(denom, 1e-15))
    return {
        "base": base,
        "z2": z2,
        "z3": z3,
        "kappa2": kappa2,
        "y2": y2,
        "c2": c2,
        "kappa3": np.asarray(kappa3),
        "y3": np.asarray(y3),
        "c3": np.asarray(c3),
        "leverage_c2_top1pct_r2": leverage,
    }


def quantiles(v):
    return {str(q): float(np.quantile(v, q)) for q in (0.01, 0.05, 0.5)}


def record_extended(d, s):
    return {
        "s": float(s),
        "f": d["base"]["f"],
        "K": d["base"]["K"],
        "y2": field_stats(d["y2"]),
        "c2": field_stats(d["c2"]),
        "kappa2_quantiles": quantiles(d["kappa2"]),
        "sampled_kappa3_quantiles": quantiles(d["kappa3"]),
        "sampled_y3": field_stats(d["y3"]),
        "sampled_c3": field_stats(d["c3"]),
        "leverage_c2_top1pct_r2": d["leverage_c2_top1pct_r2"],
    }


def integrate_extended(initial_state, gamma1, gamma2, horizon, step,
                       sampled_rows, retain_states=False):
    steps = int(round(horizon / step))
    checkpoint_steps = int(round(0.1 / step))
    if abs(steps * step - horizon) > 1e-10 or abs(checkpoint_steps * step - 0.1) > 1e-10:
        raise ValueError("horizon and 0.1 must be integer multiples of step")
    state = tuple(x.copy() for x in initial_state)
    records = []
    states = []
    integral_k = 0.0
    previous_k = None
    for k in range(steps + 1):
        base = derived(state, gamma1, gamma2)
        if previous_k is not None:
            integral_k += step * (previous_k + base["K"]) / 2.0
        previous_k = base["K"]
        if k % checkpoint_steps == 0:
            d = extended(state, gamma1, gamma2, sampled_rows)
            records.append(record_extended(d, k * step))
            if retain_states:
                states.append({
                    "z2": d["z2"].copy(),
                    "z3": d["z3"].copy(),
                })
        if k < steps:
            state = rk4(state, gamma1, gamma2, step)
    defect = abs(
        (records[-1]["f"] - records[0]["f"]) - integral_k
    ) / (1.0 + abs(records[-1]["f"] - records[0]["f"]))
    return records, states, float(defect)


def cavity_record(main_state, cavity_state, s):
    dz2 = main_state["z2"] - cavity_state["z2"]
    dz3 = main_state["z3"] - cavity_state["z3"]
    dt2 = theta(main_state["z2"]) - theta(cavity_state["z2"])
    dt3 = theta(main_state["z3"]) - theta(cavity_state["z3"])
    n = dz2.size
    norm = lambda v: float(np.sqrt(np.mean(v * v)))
    return {
        "s": float(s),
        "sqrt_n_dz2_l2": np.sqrt(n) * norm(dz2),
        "sqrt_n_dtheta2_l2": np.sqrt(n) * norm(dt2),
        "sqrt_n_dz3_l2": np.sqrt(n) * norm(dz3),
        "sqrt_n_dtheta3_l2": np.sqrt(n) * norm(dt3),
    }


def run_one(n, seed, horizon, step, cavity_columns, sampled_top_rows):
    started = time.monotonic()
    rng, initial_state, gamma1, gamma2 = initialization(n, seed)
    rows = rng.choice(n, size=min(sampled_top_rows, n), replace=False)
    main_records, main_states, main_defect = integrate_extended(
        initial_state, gamma1, gamma2, horizon, step, rows,
        retain_states=cavity_columns > 0,
    )
    cavities = []
    columns = rng.choice(n, size=min(cavity_columns, n), replace=False)
    for raw_j in columns:
        j = int(raw_j)
        cavity_gamma2 = gamma2.copy()
        cavity_gamma2[:, j] = 0.0
        _, cavity_states, cavity_defect = integrate_extended(
            initial_state, gamma1, cavity_gamma2, horizon, step, rows,
            retain_states=True,
        )
        cavities.append({
            "column": j,
            "solver_identity_defect": cavity_defect,
            "records": [
                cavity_record(m, c, rec["s"])
                for m, c, rec in zip(main_states, cavity_states, main_records)
            ],
        })
    return {
        "n": n,
        "seed": seed,
        "horizon": horizon,
        "step": step,
        "main_solver_identity_defect": main_defect,
        "records": main_records,
        "cavities": cavities,
        "wall_seconds": time.monotonic() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", nargs="+", type=int, required=True)
    parser.add_argument("--seeds", nargs="+", type=int, required=True)
    parser.add_argument("--horizon", type=float, default=2.0)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--cavity-columns", type=int, default=4)
    parser.add_argument("--sampled-top-rows", type=int, default=16)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    meta = {
        "kind": "metadata",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "platform": platform.platform(),
        "arguments": vars(args) | {"output": str(args.output)},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps(meta, sort_keys=True) + "\n")
        handle.flush()
        for n in args.widths:
            for seed in args.seeds:
                result = run_one(
                    n, seed + n, args.horizon, args.step,
                    args.cavity_columns, args.sampled_top_rows,
                )
                handle.write(json.dumps(result, sort_keys=True) + "\n")
                handle.flush()
                print(
                    f"n={n} seed={seed+n} wall={result['wall_seconds']:.2f}s",
                    flush=True,
                )


if __name__ == "__main__":
    main()
