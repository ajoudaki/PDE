"""Preregistered Hutchinson diagnostic for column-response leverage.

Evidence only; see RESPONSE_LEVERAGE_EXPERIMENT_PREREGISTRATION_2026-08-23.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from pathlib import Path

import numpy as np

from experiment_middle_response import derived, initialization, rk4


def integrate_b3_path(initial_state, gamma1, gamma2, horizon, step, checkpoint):
    steps = int(round(horizon / step))
    stride = int(round(checkpoint / step))
    if abs(steps * step - horizon) > 1e-10:
        raise ValueError("horizon must be an integer multiple of step")
    if abs(stride * step - checkpoint) > 1e-10:
        raise ValueError("checkpoint must be an integer multiple of step")
    state = tuple(x.copy() for x in initial_state)
    path = []
    for k in range(steps + 1):
        if k % stride == 0:
            path.append(derived(state, gamma1, gamma2)["b3"].copy())
        if k < steps:
            state = rk4(state, gamma1, gamma2, step)
    return path


def leverage_stats(row_energy):
    total = float(np.sum(row_energy))
    if total <= np.finfo(float).tiny:
        return {
            "frobenius": 0.0,
            "entropy": 0.0,
            "entropy_ratio": 0.0,
            "inverse_participation": 1.0,
            "max_n_weight": 1.0,
            "top_one_percent_mass": 0.01,
        }
    n = row_energy.size
    weights = row_energy / total
    positive = weights > 0.0
    entropy = float(np.sum(weights[positive] * np.log(n * weights[positive])))
    count = max(1, int(np.ceil(0.01 * n)))
    top = np.partition(weights, n - count)[n - count :]
    return {
        "frobenius": float(np.sqrt(total)),
        "entropy": entropy,
        "entropy_ratio": entropy / np.log(n),
        "inverse_participation": float(n * np.sum(weights * weights)),
        "max_n_weight": float(n * np.max(weights)),
        "top_one_percent_mass": float(np.sum(top)),
    }


def run_one(n, seed, horizon, step, checkpoint, probes, epsilon):
    started = time.monotonic()
    rng, initial_state, gamma1, gamma2 = initialization(n, seed)
    column = int(rng.integers(n))
    probe_values = rng.choice(np.array([-1.0, 1.0]), size=(probes, n))
    row_energy_path = [np.zeros(n) for _ in range(int(round(horizon / checkpoint)) + 1)]
    for probe in probe_values:
        plus = gamma2.copy()
        minus = gamma2.copy()
        shift = epsilon * probe / np.sqrt(n)
        plus[:, column] += shift
        minus[:, column] -= shift
        plus_path = integrate_b3_path(
            initial_state, gamma1, plus, horizon, step, checkpoint
        )
        minus_path = integrate_b3_path(
            initial_state, gamma1, minus, horizon, step, checkpoint
        )
        for row_energy, left, right in zip(row_energy_path, plus_path, minus_path):
            jvp = (left - right) / (2.0 * epsilon)
            row_energy += jvp * jvp / probes
    return {
        "n": n,
        "seed": seed,
        "column": column,
        "horizon": horizon,
        "step": step,
        "checkpoint": checkpoint,
        "probes": probes,
        "epsilon": epsilon,
        "records": [
            {"s": k * checkpoint, **leverage_stats(row_energy)}
            for k, row_energy in enumerate(row_energy_path)
        ],
        "wall_seconds": time.monotonic() - started,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", nargs="+", type=int, required=True)
    parser.add_argument("--seeds", nargs="+", type=int, required=True)
    parser.add_argument("--horizon", type=float, default=4.0)
    parser.add_argument("--step", type=float, default=0.02)
    parser.add_argument("--checkpoint", type=float, default=0.2)
    parser.add_argument("--probes", type=int, default=4)
    parser.add_argument("--epsilon", type=float, default=2e-4)
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
            for seed0 in args.seeds:
                result = run_one(
                    n=n,
                    seed=seed0 + n,
                    horizon=args.horizon,
                    step=args.step,
                    checkpoint=args.checkpoint,
                    probes=args.probes,
                    epsilon=args.epsilon,
                )
                handle.write(json.dumps(result, sort_keys=True) + "\n")
                handle.flush()
                print(
                    f"n={n} seed={seed0+n} wall={result['wall_seconds']:.2f}s",
                    flush=True,
                )


if __name__ == "__main__":
    main()
