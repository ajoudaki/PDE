#!/usr/bin/env python3
"""Preregistered scalar-particle scan for oscillatory residual activations.

This is exploratory evidence only.  It deliberately reports tail
concentration diagnostics because ordinary Monte Carlo can completely miss
the Gaussian rare events relevant to high iterates.
"""

from __future__ import annotations

import argparse
import math
import numpy as np
from scipy.integrate import quad


def normal_expectation(fun):
    scale = 1.0 / math.sqrt(2.0 * math.pi)
    value, _ = quad(
        lambda x: fun(x) * math.exp(-0.5 * x * x) * scale,
        -10.0,
        10.0,
        epsabs=2e-11,
        epsrel=2e-11,
        limit=1200,
    )
    return value


def activation(p: int, lam: float):
    # A dense deterministic trapezoid is more robust than adaptive quadrature
    # for the highly oscillatory p=5 phase.  The omitted Gaussian tail is less
    # than 1e-15 at |x|=8.
    grid = np.linspace(-8.0, 8.0, 2_000_001)
    density = np.exp(-0.5 * grid * grid) / math.sqrt(2.0 * math.pi)
    raw = grid + lam * np.sin(grid**p)
    rms2 = np.trapz(raw * raw * density, grid)
    scale = math.sqrt(rms2)

    def phi(x):
        return (x + lam * np.sin(x**p)) / scale

    def dphi(x):
        return (1.0 + lam * p * x ** (p - 1) * np.cos(x**p)) / scale

    return phi, dphi, scale


def identity():
    return (lambda x: x), (lambda x: np.ones_like(x)), 1.0


def run(a0, z0, steps, h, phi, dphi):
    a = a0.copy()
    z = z0.copy()
    live = np.ones(a.shape, dtype=bool)
    for _ in range(steps):
        with np.errstate(over="ignore", invalid="ignore"):
            a_new = a + h * phi(z)
            z_new = z + h * a * dphi(z)
        live &= np.isfinite(a_new) & np.isfinite(z_new)
        a, z = a_new, z_new
        if not np.all(live):
            a = np.where(live, a, np.nan)
            z = np.where(live, z, np.nan)
    with np.errstate(over="ignore", invalid="ignore"):
        contribution = a * phi(z)
    return contribution


def summarize(x):
    finite = np.isfinite(x)
    y = x[finite]
    if len(y) == 0:
        return (0.0, math.nan, math.nan, math.nan, math.nan)
    order = np.argsort(np.abs(y))
    trim = y[order[: max(1, int(0.999 * len(y)))]]
    return (
        float(np.mean(finite)),
        float(np.mean(y)),
        float(np.mean(trim)),
        float(np.quantile(np.abs(y), 0.999)),
        float(np.max(np.abs(y))),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--power", type=int, default=18)
    parser.add_argument("--max-t", type=int, default=16)
    args = parser.parse_args()
    rng = np.random.default_rng(20260825)
    size = 2**args.power
    a0 = rng.standard_normal(size)
    z0 = rng.standard_normal(size)
    candidates = [
        ("identity", identity()),
        ("p3_lam0.1", activation(3, 0.1)),
        ("p3_lam0.25", activation(3, 0.25)),
        ("p5_lam0.05", activation(5, 0.05)),
        ("p5_lam0.1", activation(5, 0.1)),
    ]
    for name, (phi, dphi, scale) in candidates:
        print("candidate", name, "scale", scale)
        for rho in (0.05,):
            for t in tuple(x for x in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32)
                           if x <= args.max_t):
                h = rho / t
                fine = run(a0, z0, 2 * t, h, phi, dphi)
                coarse = run(a0, z0, t, 2.0 * h, phi, dphi)
                delta = fine - coarse
                print("scan", rho, t, summarize(delta), flush=True)


if __name__ == "__main__":
    main()
