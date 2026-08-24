"""Bounded numerical hostile check for middle-adjoint concentration.

This is evidence only.  It integrates the exact finite feature flow and reports
empirical moderate moments and maxima of the two middle backpropagated fields.
"""

import argparse
import json

import numpy as np


def inv_theta(r):
    return 2.0 * np.sinh(np.arcsinh(1.5 * r) / 3.0)


def derived(state):
    a, r, g1, g2 = state
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
    r2 = g2.T @ b3
    b2 = d2 * r2
    q1 = g1.T @ b2
    f = np.mean(a * x3)
    k = (
        np.mean(x3 * x3)
        + np.mean(b3 * b3) * np.mean(x2 * x2)
        + np.mean(b2 * b2) * np.mean(x1 * x1)
        + np.mean((d1 * q1) ** 2)
    )
    return x1, x2, x3, b3, r2, b2, q1, f, k


def rhs(state):
    a, _, _, _ = state
    x1, x2, x3, b3, _, b2, q1, _, _ = derived(state)
    n = a.size
    return x3, q1, np.outer(b2, x1) / n, np.outer(b3, x2) / n


def add(state, tangent, scale):
    return tuple(x + scale * dx for x, dx in zip(state, tangent))


def rk4(state, h):
    k1 = rhs(state)
    k2 = rhs(add(state, k1, h / 2.0))
    k3 = rhs(add(state, k2, h / 2.0))
    k4 = rhs(add(state, k3, h))
    return tuple(
        x + h * (d1 + 2.0 * d2 + 2.0 * d3 + d4) / 6.0
        for x, d1, d2, d3, d4 in zip(state, k1, k2, k3, k4)
    )


def moment_norm(v, p):
    return float(np.mean(np.abs(v) ** p) ** (1.0 / p))


def snapshot(state, time):
    _, _, _, _, r2, b2, q1, f, k = derived(state)
    result = {"time": time, "f": float(f), "K": float(k)}
    for name, value in (("r2", r2), ("b2", b2), ("q1", q1)):
        result[name] = {
            "max": float(np.max(np.abs(value))),
            "l2": moment_norm(value, 2),
            "l4": moment_norm(value, 4),
            "l8": moment_norm(value, 8),
        }
    return result


def run(n, seed, horizon, step):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=n)
    u = rng.normal(size=n)
    r = u + u**3 / 3.0
    g1 = rng.normal(size=(n, n)) / np.sqrt(n)
    g2 = rng.normal(size=(n, n)) / np.sqrt(n)
    state = (a, r, g1, g2)
    checkpoints = {0, int(round(0.25 * horizon / step)), int(round(0.5 * horizon / step)), int(round(horizon / step))}
    records = []
    steps = int(round(horizon / step))
    for k in range(steps + 1):
        if k in checkpoints:
            records.append(snapshot(state, k * step))
        if k < steps:
            state = rk4(state, step)
    return {"n": n, "seed": seed, "horizon": horizon, "step": step, "records": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", type=int, nargs="+", default=[128, 256, 512])
    parser.add_argument("--seed", type=int, default=20260821)
    parser.add_argument("--horizon", type=float, default=0.5)
    parser.add_argument("--step", type=float, default=0.01)
    args = parser.parse_args()
    print(json.dumps([run(n, args.seed + n, args.horizon, args.step) for n in args.widths], indent=2))


if __name__ == "__main__":
    main()
