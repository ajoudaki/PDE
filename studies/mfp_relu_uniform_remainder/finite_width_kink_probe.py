"""Preregistered exact finite-width ReLU/leaky-ReLU paired-defect probe."""

from __future__ import annotations

import argparse
import json
import math
import numpy as np


def activation(x, leak, scale):
    return scale * np.where(x >= 0, x, leak * x)


def derivative(x, leak, scale):
    return scale * np.where(x >= 0, 1.0, leak)


def step(u, w, a, h, leak, scale):
    n = u.shape[-1]
    root = math.sqrt(n)
    x = activation(u, leak, scale)
    z = np.einsum("bij,bj->bi", w, x) / root
    y = activation(z, leak, scale)
    c = a * derivative(z, leak, scale)
    back = np.einsum("bji,bj->bi", w, c) / root
    return (
        u + h * back * derivative(u, leak, scale),
        w + (h / root) * c[:, :, None] * x[:, None, :],
        a + h * y,
    )


def output(u, w, a, leak, scale):
    n = u.shape[-1]
    x = activation(u, leak, scale)
    z = np.einsum("bij,bj->bi", w, x) / math.sqrt(n)
    return np.mean(a * activation(z, leak, scale), axis=1)


def trajectory(init, h, steps, leak, scale):
    state = tuple(x.copy() for x in init)
    for _ in range(steps):
        state = step(*state, h, leak, scale)
    return output(*state, leak, scale)


def samples(n, seeds, batch, hs, leak):
    scale = math.sqrt(2.0 / (1.0 + leak * leak))
    accum = {h: [] for h in hs + [-h for h in hs]}
    rng = np.random.default_rng(9173 + n + round(1000 * leak))
    remaining = seeds
    while remaining:
        size = min(batch, remaining)
        init = (
            rng.standard_normal((size, n)),
            rng.standard_normal((size, n, n)),
            rng.standard_normal((size, n)),
        )
        for h in tuple(accum):
            fine = trajectory(init, h, 2, leak, scale)
            coarse = trajectory(init, 2 * h, 1, leak, scale)
            accum[h].append(fine - coarse)
        remaining -= size
    return {h: np.concatenate(parts) for h, parts in accum.items()}


def mean_se(x):
    return float(np.mean(x)), float(np.std(x, ddof=1) / math.sqrt(len(x)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", nargs="+", type=int, default=[32, 64, 128])
    parser.add_argument("--seeds", type=int, default=4096)
    parser.add_argument("--batch", type=int, default=64)
    parser.add_argument("--hs", nargs="+", type=float, default=[0.04, 0.02, 0.01])
    parser.add_argument("--leaks", nargs="+", type=float, default=[0.0, 0.1])
    args = parser.parse_args()
    rows = []
    for leak in args.leaks:
        for n in args.widths:
            vals = samples(n, args.seeds, args.batch, args.hs, leak)
            for h in args.hs:
                d = vals[h]
                dn = vals[-h]
                do = 0.5 * (d - dn)
                m2, s2 = mean_se(d / (h * abs(h)))
                m3, s3 = mean_se(d / h**3)
                ma2, sa2 = mean_se(do / h**2)
                ma3, sa3 = mean_se(do / h**3)
                mo, so = mean_se((d + dn) / h**2)
                rows.append({
                    "leak": leak, "width": n, "h": h, "seeds": len(d),
                    "delta_over_habs_h": [m2, s2],
                    "delta_over_h3": [m3, s3],
                    "antithetic_delta_over_h2": [ma2, sa2],
                    "antithetic_delta_over_h3": [ma3, sa3],
                    "oddness_over_h2": [mo, so],
                })
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
