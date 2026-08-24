"""Mechanism-preserving numerical tail audit for the frozen depth-three model.

This is bounded evidence, never a convergence proof.  It integrates the exact
finite feature-ascent ODE in the original parameter coordinates and reports
empirical tail diagnostics for the two adaptive adjoint fields.
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.special import gamma, hyp2f1


def normalized_power_saturator(z, q):
    """Odd unit-range primitive of (1+z^2)^(-q/2), for q>1."""
    half_range = (
        np.sqrt(np.pi) * gamma((q - 1.0) / 2.0) / (2.0 * gamma(q / 2.0))
    )
    primitive = z * hyp2f1(0.5, q / 2.0, 1.5, -(z * z))
    return primitive / half_range, (1.0 + z * z) ** (-q / 2.0) / half_range


def raw_power_saturator(z, q, lam=0.125):
    """Positive shifted primitive with fixed gate amplitude, not unit range."""
    half_range = (
        np.sqrt(np.pi) * gamma((q - 1.0) / 2.0) / (2.0 * gamma(q / 2.0))
    )
    primitive = z * hyp2f1(0.5, q / 2.0, 1.5, -(z * z))
    # The shift 1 keeps a uniform positive floor because lam*half_range < 1
    # for the two q values exposed below.
    return 1.0 + lam * primitive, lam * (1.0 + z * z) ** (-q / 2.0)


def activation(name, z):
    if name == "arctan":
        return np.arctan(z), 1.0 / (1.0 + z * z)
    if name == "asinh":
        return np.arcsinh(z), 1.0 / np.sqrt(1.0 + z * z)
    if name == "tanh":
        x = np.tanh(z)
        return x, 1.0 - x * x
    if name == "sine":
        return np.sin(z), np.cos(z)
    if name == "shifted_sine":
        eps = 0.2
        return 1.0 + eps * np.sin(z), eps * np.cos(z)
    if name == "shifted_cosine":
        eps = 0.2
        return 1.0 + eps * np.cos(z), -eps * np.sin(z)
    if name == "gudermannian":
        # gd(z)=arcsin(tanh z)=arctan(sinh z), with gd'(z)=sech z.
        # The first representation avoids overflow in sinh on stress runs.
        t = np.tanh(z)
        return np.arcsin(t), np.sqrt(np.maximum(0.0, 1.0 - t * t))
    if name == "shifted_gudermannian":
        eps = 0.2
        t = np.tanh(z)
        gd = np.arcsin(t)
        return 1.0 + eps * gd, (
            eps * np.sqrt(np.maximum(0.0, 1.0 - t * t))
        )
    if name == "residual_sine":
        return z + 0.25 * np.sin(z), 1.0 + 0.25 * np.cos(z)
    if name == "residual_tanh":
        eps = 0.2
        x = np.tanh(z)
        return z + eps * x, 1.0 + eps * (1.0 - x * x)
    if name == "residual_gudermannian":
        eps = 0.2
        t = np.tanh(z)
        gd = np.arcsin(t)
        return z + eps * gd, (
            1.0 + eps * np.sqrt(np.maximum(0.0, 1.0 - t * t))
        )
    if name == "shifted_gaussian_bump":
        eps = 0.2
        bump = np.exp(-0.5 * z * z)
        return 1.0 + eps * bump, -eps * z * bump
    if name == "shifted_softsign":
        eps = 0.2
        root = np.sqrt(1.0 + z * z)
        return 1.0 + eps * z / root, eps / (root * root * root)
    if name == "shifted_power_1p25":
        eps = 0.2
        value, derivative = normalized_power_saturator(z, 1.25)
        return 1.0 + eps * value, eps * derivative
    if name == "shifted_power_1p5":
        eps = 0.2
        value, derivative = normalized_power_saturator(z, 1.5)
        return 1.0 + eps * value, eps * derivative
    if name == "raw_power_1p333":
        return raw_power_saturator(z, 4.0 / 3.0)
    if name == "raw_power_1p5":
        return raw_power_saturator(z, 1.5)
    if name == "composed_power_1p5":
        lam = 0.125
        v = np.arcsinh(z)
        primitive = v * hyp2f1(0.5, 0.75, 1.5, -(v * v))
        derivative = (
            lam
            * (1.0 + v * v) ** (-0.75)
            / np.sqrt(1.0 + z * z)
        )
        return 1.0 + lam * primitive, derivative
    if name == "shifted_arctan":
        eps = 0.2
        return 1.0 + eps * (2.0 / np.pi) * np.arctan(z), (
            eps * (2.0 / np.pi) / (1.0 + z * z)
        )
    if name == "shifted_tanh":
        eps = 0.2
        x = np.tanh(z)
        return 1.0 + eps * x, eps * (1.0 - x * x)
    if name == "hyperbolic_exp":
        eps = 0.2
        v = np.arcsinh(z)
        e = np.exp(eps * v)
        return 1.0 + e, eps * e / np.sqrt(1.0 + z * z)
    raise ValueError(f"unknown activation {name!r}")


def derived(state, name):
    a, u, g1, g2 = state
    x1, d1 = activation(name, u)
    z2 = g1 @ x1
    x2, d2 = activation(name, z2)
    z3 = g2 @ x2
    x3, d3 = activation(name, z3)
    b3 = a * d3
    r2 = g2.T @ b3
    b2 = d2 * r2
    q1 = g1.T @ b2
    p1 = d1 * q1
    f = np.mean(a * x3)
    k = (
        np.mean(x3 * x3)
        + np.mean(b3 * b3) * np.mean(x2 * x2)
        + np.mean(b2 * b2) * np.mean(x1 * x1)
        + np.mean(p1 * p1)
    )
    return x1, x2, x3, b3, r2, b2, q1, p1, f, k


def rhs(state, name):
    a, _, _, _ = state
    x1, x2, x3, b3, _, b2, _, p1, _, _ = derived(state, name)
    n = a.size
    return x3, p1, np.outer(b2, x1) / n, np.outer(b3, x2) / n


def add(state, tangent, scale):
    return tuple(x + scale * dx for x, dx in zip(state, tangent))


def rk4(state, h, name):
    k1 = rhs(state, name)
    k2 = rhs(add(state, k1, h / 2.0), name)
    k3 = rhs(add(state, k2, h / 2.0), name)
    k4 = rhs(add(state, k3, h), name)
    return tuple(
        x + h * (d1 + 2.0 * d2 + 2.0 * d3 + d4) / 6.0
        for x, d1, d2, d3, d4 in zip(state, k1, k2, k3, k4)
    )


def diagnostics(v):
    square = np.sort(v * v)[::-1]
    total = float(np.sum(square))
    top_count = max(1, int(np.ceil(0.01 * v.size)))
    return {
        "max": float(np.max(np.abs(v))),
        "l2": float(np.mean(np.abs(v) ** 2) ** 0.5),
        "l4": float(np.mean(np.abs(v) ** 4) ** 0.25),
        "l8": float(np.mean(np.abs(v) ** 8) ** 0.125),
        "top_1pct_square_fraction": (
            float(np.sum(square[:top_count]) / total) if total else 0.0
        ),
    }


def snapshot(state, name, time):
    fields = derived(state, name)
    _, _, _, b3, r2, b2, q1, p1, f, k = fields
    return {
        "time": time,
        "f": float(f),
        "K": float(k),
        "b3": diagnostics(b3),
        "r2": diagnostics(r2),
        "b2": diagnostics(b2),
        "q1": diagnostics(q1),
        "p1": diagnostics(p1),
    }


def run(name, n, seed, horizon, step):
    rng = np.random.default_rng(seed)
    state = (
        rng.normal(size=n),
        rng.normal(size=n),
        rng.normal(size=(n, n)) / np.sqrt(n),
        rng.normal(size=(n, n)) / np.sqrt(n),
    )
    steps = int(round(horizon / step))
    checkpoints = {0, steps // 4, steps // 2, steps}
    records = []
    for k in range(steps + 1):
        if k in checkpoints:
            records.append(snapshot(state, name, k * step))
        if k < steps:
            state = rk4(state, step, name)
    return {"activation": name, "n": n, "seed": seed, "records": records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--activations",
        nargs="+",
        default=[
            "arctan",
            "asinh",
            "tanh",
            "sine",
            "shifted_sine",
            "shifted_cosine",
            "gudermannian",
            "shifted_gudermannian",
            "residual_sine",
            "residual_tanh",
            "residual_gudermannian",
            "shifted_gaussian_bump",
            "shifted_softsign",
            "shifted_power_1p25",
            "shifted_power_1p5",
            "raw_power_1p333",
            "raw_power_1p5",
            "composed_power_1p5",
            "shifted_arctan",
            "shifted_tanh",
            "hyperbolic_exp",
        ],
    )
    parser.add_argument("--widths", type=int, nargs="+", default=[128, 256])
    parser.add_argument("--seed", type=int, default=20260822)
    parser.add_argument("--horizon", type=float, default=0.5)
    parser.add_argument("--step", type=float, default=0.01)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    results = []
    for activation_name in args.activations:
        for n in args.widths:
            results.append(
                run(
                    activation_name,
                    n,
                    args.seed + 1009 * n,
                    args.horizon,
                    args.step,
                )
            )
    if args.summary:
        compact = []
        for result in results:
            final = result["records"][-1]
            compact.append(
                {
                    "activation": result["activation"],
                    "n": result["n"],
                    "time": final["time"],
                    "f": final["f"],
                    "K": final["K"],
                    "r2": final["r2"],
                    "q1": final["q1"],
                }
            )
        print(json.dumps(compact, indent=2))
    else:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
