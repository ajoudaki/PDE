"""Finite-width tail audit for the depth-three one-sample gradient flow.

This script is discriminating evidence for activation selection, not a proof.
It uses the normalized mean-field metric and records empirical moment/tail
diagnostics for the two reused-adjoint cotangents.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Activation:
    name: str
    alpha: float = 0.5

    def value(self, x: np.ndarray) -> np.ndarray:
        if self.name == "asinh":
            return np.arcsinh(x)
        if self.name == "leaky_atan":
            return self.alpha * x + (1.0 - self.alpha) * np.arctan(x)
        if self.name == "atan":
            return np.arctan(x)
        if self.name == "tanh":
            return np.tanh(x)
        raise ValueError(self.name)

    def derivative(self, x: np.ndarray) -> np.ndarray:
        if self.name == "asinh":
            return 1.0 / np.sqrt(1.0 + x * x)
        if self.name == "leaky_atan":
            return self.alpha + (1.0 - self.alpha) / (1.0 + x * x)
        if self.name == "atan":
            return 1.0 / (1.0 + x * x)
        if self.name == "tanh":
            y = np.tanh(x)
            return 1.0 - y * y
        raise ValueError(self.name)


def fields(state: tuple[np.ndarray, ...], activation: Activation) -> dict[str, np.ndarray | float]:
    u, a, g1, g2 = state
    x1 = activation.value(u)
    z2 = g1 @ x1
    x2 = activation.value(z2)
    z3 = g2 @ x2
    x3 = activation.value(z3)
    b3 = a * activation.derivative(z3)
    q2 = g2.T @ b3
    b2 = activation.derivative(z2) * q2
    q1 = g1.T @ b2
    b1 = activation.derivative(u) * q1
    f = float(np.mean(a * x3))
    kernel = float(
        np.mean(x3 * x3)
        + np.mean(b1 * b1)
        + np.mean(b2 * b2) * np.mean(x1 * x1)
        + np.mean(b3 * b3) * np.mean(x2 * x2)
    )
    return {
        "x1": x1,
        "z2": z2,
        "x2": x2,
        "z3": z3,
        "x3": x3,
        "b3": b3,
        "q2": q2,
        "b2": b2,
        "q1": q1,
        "b1": b1,
        "f": f,
        "kernel": kernel,
    }


def rhs(
    state: tuple[np.ndarray, ...], activation: Activation, label: float
) -> tuple[np.ndarray, ...]:
    u, a, g1, g2 = state
    f = fields(state, activation)
    residual_factor = 2.0 * (label - float(f["f"]))
    n = u.size
    return (
        residual_factor * f["b1"],
        residual_factor * f["x3"],
        residual_factor * np.outer(f["b2"], f["x1"]) / n,
        residual_factor * np.outer(f["b3"], f["x2"]) / n,
    )


def add_scaled(
    state: tuple[np.ndarray, ...], tangent: tuple[np.ndarray, ...], scale: float
) -> tuple[np.ndarray, ...]:
    return tuple(x + scale * dx for x, dx in zip(state, tangent, strict=True))


def rk4_step(
    state: tuple[np.ndarray, ...], dt: float, activation: Activation, label: float
) -> tuple[np.ndarray, ...]:
    k1 = rhs(state, activation, label)
    k2 = rhs(add_scaled(state, k1, 0.5 * dt), activation, label)
    k3 = rhs(add_scaled(state, k2, 0.5 * dt), activation, label)
    k4 = rhs(add_scaled(state, k3, dt), activation, label)
    return tuple(
        x + (dt / 6.0) * (d1 + 2.0 * d2 + 2.0 * d3 + d4)
        for x, d1, d2, d3, d4 in zip(state, k1, k2, k3, k4, strict=True)
    )


def tail_summary(x: np.ndarray) -> dict[str, float | list[float]]:
    absolute = np.abs(x)
    second = float(np.mean(absolute**2))
    ratios = []
    for p in (2, 4, 6, 8, 12, 16):
        root_moment = float(np.mean(absolute**p) ** (1.0 / p))
        ratios.append(root_moment / p)
    order = np.sort(absolute**2)[::-1]
    n = x.size
    return {
        "l2_sq": second,
        "max_over_sqrt_n": float(np.max(absolute) / np.sqrt(n)),
        "moment_root_over_p": ratios,
        "top_1_energy_fraction": float(order[0] / np.sum(order)) if second else 0.0,
        "top_sqrt_n_energy_fraction": (
            float(np.sum(order[: max(1, int(np.sqrt(n)))]) / np.sum(order))
            if second
            else 0.0
        ),
    }


def run_one(
    width: int,
    seed: int,
    activation: Activation,
    horizon: float,
    dt: float,
    label: float,
) -> list[dict[str, object]]:
    rng = np.random.default_rng(seed)
    state = (
        rng.standard_normal(width),
        rng.standard_normal(width),
        rng.standard_normal((width, width)) / np.sqrt(width),
        rng.standard_normal((width, width)) / np.sqrt(width),
    )
    checkpoints = np.linspace(0.0, horizon, 5)
    records: list[dict[str, object]] = []
    next_checkpoint = 0

    def record(checkpoint: float) -> None:
        f = fields(state, activation)
        records.append(
            {
                "activation": activation.name,
                "alpha": activation.alpha,
                "width": width,
                "seed": seed,
                "time": float(checkpoint),
                "predictor": f["f"],
                "kernel": f["kernel"],
                "q2": tail_summary(f["q2"]),
                "q1": tail_summary(f["q1"]),
                "a": tail_summary(state[1]),
            }
        )

    record(float(checkpoints[0]))
    next_checkpoint = 1
    steps = int(np.ceil(horizon / dt))
    time = 0.0
    for _ in range(steps):
        step_size = min(dt, horizon - time)
        state = rk4_step(state, step_size, activation, label)
        time += step_size
        while (
            next_checkpoint < len(checkpoints)
            and time + 1.0e-12 >= checkpoints[next_checkpoint]
        ):
            record(float(checkpoints[next_checkpoint]))
            next_checkpoint += 1
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", nargs="+", type=int, default=[128, 256, 512])
    parser.add_argument("--seeds", nargs="+", type=int, default=[11, 29, 47])
    parser.add_argument("--horizon", type=float, default=2.0)
    parser.add_argument("--dt", type=float, default=0.01)
    parser.add_argument("--label", type=float, default=1.0)
    parser.add_argument("--alpha", type=float, default=0.5)
    parser.add_argument(
        "--summary",
        action="store_true",
        help="print one aggregate row per activation/width instead of raw records",
    )
    args = parser.parse_args()

    activations = [
        Activation("asinh"),
        Activation("leaky_atan", args.alpha),
        Activation("atan"),
        Activation("tanh"),
    ]
    output: list[dict[str, object]] = []
    for activation in activations:
        for width in args.widths:
            for seed in args.seeds:
                output.extend(
                    run_one(width, seed, activation, args.horizon, args.dt, args.label)
                )
    if not args.summary:
        print(json.dumps(output, indent=2))
        return

    summary: list[dict[str, object]] = []
    for activation in activations:
        for width in args.widths:
            rows = [
                row
                for row in output
                if row["activation"] == activation.name
                and row["width"] == width
                and abs(float(row["time"]) - args.horizon) < 1.0e-12
            ]
            item: dict[str, object] = {
                "activation": activation.name,
                "width": width,
                "seeds": len(rows),
            }
            for scalar in ("predictor", "kernel"):
                item[scalar] = float(np.mean([row[scalar] for row in rows]))
            for field in ("q2", "q1", "a"):
                item[field] = {
                    key: float(np.mean([row[field][key] for row in rows]))
                    for key in (
                        "l2_sq",
                        "max_over_sqrt_n",
                        "top_1_energy_fraction",
                        "top_sqrt_n_energy_fraction",
                    )
                }
                item[field]["moment_root_over_p"] = np.mean(
                    [row[field]["moment_root_over_p"] for row in rows], axis=0
                ).tolist()
            summary.append(item)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
