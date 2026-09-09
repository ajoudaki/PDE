"""Preregistered finite-width mechanism probe.

This is deliberately evidence-only.  It uses common random initialization for
the fine and coarse Euler trajectories of the exact finite-width network.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.hermite import hermgauss


@dataclass(frozen=True)
class Activation:
    power: int
    lam: float
    scale: float

    @property
    def name(self) -> str:
        return f"x+{self.lam:g}sin(x^{self.power})"

    def phi(self, x: np.ndarray) -> np.ndarray:
        return (x + self.lam * np.sin(x**self.power)) / self.scale

    def dphi(self, x: np.ndarray) -> np.ndarray:
        p = self.power
        return (
            1.0 + self.lam * p * x ** (p - 1) * np.cos(x**p)
        ) / self.scale


def gaussian_l2_scale(power: int, lam: float, order: int = 256) -> float:
    # hermgauss integrates exp(-x^2); G=sqrt(2)x and divide by sqrt(pi).
    x, w = hermgauss(order)
    g = math.sqrt(2.0) * x
    raw = g + lam * np.sin(g**power)
    return float(math.sqrt(np.dot(w, raw * raw) / math.sqrt(math.pi)))


def output(act: Activation, u: np.ndarray, w: np.ndarray, a: np.ndarray) -> float:
    n = len(u)
    x = act.phi(u)
    z = w @ x / math.sqrt(n)
    return float(np.dot(a, act.phi(z)) / n)


def step(
    act: Activation,
    h: float,
    u: np.ndarray,
    w: np.ndarray,
    a: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = len(u)
    root_n = math.sqrt(n)
    x = act.phi(u)
    z = w @ x / root_n
    y = act.phi(z)
    c = a * act.dphi(z)
    back = w.T @ c / root_n
    return (
        u + h * back * act.dphi(u),
        w + (h / root_n) * np.outer(c, x),
        a + h * y,
    )


def trajectory(
    act: Activation,
    h: float,
    steps: int,
    init: tuple[np.ndarray, np.ndarray, np.ndarray],
) -> float:
    u, w, a = (v.copy() for v in init)
    with np.errstate(over="raise", invalid="raise"):
        for _ in range(steps):
            u, w, a = step(act, h, u, w, a)
        return output(act, u, w, a)


def paired_sample(
    act: Activation, n: int, t: int, rho: float, seed: int
) -> dict[str, float | bool]:
    rng = np.random.default_rng(seed)
    init = (rng.standard_normal(n), rng.standard_normal((n, n)), rng.standard_normal(n))
    h = rho / t
    try:
        fine = trajectory(act, h, 2 * t, init)
        coarse = trajectory(act, 2 * h, t, init)
        return {"fine": fine, "coarse": coarse, "delta": fine - coarse, "finite": True}
    except (FloatingPointError, OverflowError):
        return {"fine": math.nan, "coarse": math.nan, "delta": math.nan, "finite": False}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", nargs="+", type=int, default=[64, 128])
    parser.add_argument("--seeds", type=int, default=8)
    parser.add_argument("--rho", type=float, default=0.05)
    parser.add_argument("--times", nargs="+", type=int, default=[1, 2, 3, 4, 6, 8, 12, 16])
    parser.add_argument(
        "--spec",
        action="append",
        default=[],
        help="candidate as power,lambda; repeat this option",
    )
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    specs = (
        [(int(v.split(",")[0]), float(v.split(",")[1])) for v in args.spec]
        if args.spec
        else [(1, 0.0), (1, 0.25), (3, 0.1), (3, 0.25), (3, 0.5), (5, 0.05), (5, 0.1)]
    )
    activations = [
        Activation(p, lam, gaussian_l2_scale(p, lam)) for p, lam in specs
    ]
    rows: list[dict[str, float | int | str]] = []
    for act in activations:
        for n in args.widths:
            for t in args.times:
                samples = [
                    paired_sample(act, n, t, args.rho, 1_000_003 * k + 97 * t + n)
                    for k in range(args.seeds)
                ]
                vals = np.asarray([s["delta"] for s in samples if s["finite"]], dtype=float)
                rows.append(
                    {
                        "activation": act.name,
                        "scale": act.scale,
                        "width": n,
                        "t": t,
                        "rho": args.rho,
                        "finite_samples": int(len(vals)),
                        "mean_delta": float(np.mean(vals)) if len(vals) else math.nan,
                        "se_delta": float(np.std(vals, ddof=1) / math.sqrt(len(vals))) if len(vals) > 1 else math.nan,
                        "median_abs_delta": float(np.median(np.abs(vals))) if len(vals) else math.nan,
                        "max_abs_delta": float(np.max(np.abs(vals))) if len(vals) else math.nan,
                    }
                )
    if args.compact:
        for row in rows:
            print(
                row["activation"], row["width"], row["t"],
                row["finite_samples"],
                f'{row["mean_delta"]:.8g}', f'{row["se_delta"]:.3g}',
                f'{row["median_abs_delta"]:.8g}', f'{row["max_abs_delta"]:.8g}',
            )
    else:
        print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
