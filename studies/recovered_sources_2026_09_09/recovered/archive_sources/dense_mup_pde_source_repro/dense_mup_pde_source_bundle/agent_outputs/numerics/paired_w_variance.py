#!/usr/bin/env python3
"""Conditional fast-layer variance diagnostic for iid residual depth.

Each pair shares B(0) and a(0), independently redraws every dense W_l, and
is then trained independently with the same data.  The statistic

    (1 / (2 n m)) ||H_L - H'_L||_F^2,
    (1 / (2 n m)) ||P_0 - P'_0||_F^2

estimate the forward and adjoint variances conditional on the immutable
base-neuron latent.  Decay as 1/L is necessary for the operator-Galerkin
PDE's slow fields h(g,s,t), p(g,s,t) to be functions of the base latent
after continuous-depth homogenization.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, os.fspath(ROOT / "dense_mup_pde_repro" / "src"))

from dense_reference import (  # noqa: E402
    ModelSpec,
    ParamState,
    forward_adjoint,
    initialize,
    rk4_param_step,
)


def _one(
    task: tuple[int, int, int, float, float]
) -> tuple[int, float, float, float, float]:
    width, depth, pair_index, train_time, dt = task
    X = np.eye(2)
    y = np.asarray([0.8, -0.55])
    first_spec = ModelSpec(
        n=width,
        depth=depth,
        X=X,
        y=y,
        seed=700000 + 10 * pair_index,
    )
    second_spec = ModelSpec(
        n=width,
        depth=depth,
        X=X,
        y=y,
        seed=700001 + 10 * pair_index,
    )
    first = initialize(first_spec)
    independent = initialize(second_spec)
    second = ParamState(
        B=first.B.copy(),
        W=independent.W.copy(),
        a=first.a.copy(),
    )

    def statistics() -> tuple[float, float]:
        fields1 = forward_adjoint(first, first_spec)
        fields2 = forward_adjoint(second, second_spec)
        h_variance = float(
            0.5 * np.mean((fields1.H[-1] - fields2.H[-1]) ** 2)
        )
        p_variance = float(
            0.5 * np.mean((fields1.P[0] - fields2.P[0]) ** 2)
        )
        return h_variance, p_variance

    h_initial, p_initial = statistics()
    steps = int(round(train_time / dt))
    for _ in range(steps):
        first = rk4_param_step(first, dt, first_spec)
        second = rk4_param_step(second, dt, second_spec)
    h_trained, p_trained = statistics()
    return depth, h_initial, p_initial, h_trained, p_trained


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=128)
    parser.add_argument("--pairs", type=int, default=24)
    parser.add_argument("--depths", type=int, nargs="+", default=[8, 16, 32, 64])
    parser.add_argument("--train-time", type=float, default=0.5)
    parser.add_argument("--dt", type=float, default=0.02)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "paired_W_conditional_variance_hp.csv"
        ),
    )
    args = parser.parse_args()

    tasks = [
        (
            args.width,
            depth,
            pair + 1000 * depth,
            args.train_time,
            args.dt,
        )
        for depth in args.depths
        for pair in range(args.pairs)
    ]
    grouped: dict[int, list[tuple[float, float, float, float]]] = {
        depth: [] for depth in args.depths
    }
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(_one, task) for task in tasks]
        for future in as_completed(futures):
            depth, h_initial, p_initial, h_trained, p_trained = (
                future.result()
            )
            grouped[depth].append(
                (h_initial, p_initial, h_trained, p_trained)
            )

    rows: list[tuple[float, ...]] = []
    for depth in args.depths:
        values = np.asarray(grouped[depth])
        rows.append(
            (
                float(depth),
                float(np.mean(values[:, 0])),
                float(np.std(values[:, 0], ddof=1) / np.sqrt(args.pairs)),
                float(np.mean(values[:, 1])),
                float(np.std(values[:, 1], ddof=1) / np.sqrt(args.pairs)),
                float(np.mean(values[:, 2])),
                float(np.std(values[:, 2], ddof=1) / np.sqrt(args.pairs)),
                float(np.mean(values[:, 3])),
                float(np.std(values[:, 3], ddof=1) / np.sqrt(args.pairs)),
            )
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            (
                "L",
                "h_var_t0",
                "h_se_t0",
                "p_var_t0",
                "p_se_t0",
                "h_var_t0p5",
                "h_se_t0p5",
                "p_var_t0p5",
                "p_se_t0p5",
            )
        )
        writer.writerows(rows)
    array = np.asarray(rows)
    slope_initial = np.polyfit(np.log(array[:, 0]), np.log(array[:, 1]), 1)[0]
    slope_p_initial = np.polyfit(
        np.log(array[:, 0]), np.log(array[:, 3]), 1
    )[0]
    slope_h_trained = np.polyfit(
        np.log(array[:, 0]), np.log(array[:, 5]), 1
    )[0]
    slope_p_trained = np.polyfit(
        np.log(array[:, 0]), np.log(array[:, 7]), 1
    )[0]
    print(
        {
            "output": os.fspath(args.output),
            "h_initial_loglog_slope": float(slope_initial),
            "p_initial_loglog_slope": float(slope_p_initial),
            "h_trained_loglog_slope": float(slope_h_trained),
            "p_trained_loglog_slope": float(slope_p_trained),
            "rows": rows,
        }
    )


if __name__ == "__main__":
    main()
