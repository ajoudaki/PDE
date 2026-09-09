"""Evidence-only common-random probe of the h^4 kink term.

This uses the exact finite-width q=1, L=2 update.  It is not a proof; its
purpose is to determine the likely small-h exponent/sign before doing the
boundary calculation.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def phi(x: np.ndarray, leak: float, scale: float) -> np.ndarray:
    return scale * np.where(x >= 0.0, x, leak * x)


def dphi(x: np.ndarray, leak: float, scale: float) -> np.ndarray:
    return scale * np.where(x >= 0.0, 1.0, leak)


def step(
    u: np.ndarray,
    w: np.ndarray,
    a: np.ndarray,
    h: float,
    leak: float,
    scale: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n = u.shape[-1]
    root = math.sqrt(n)
    x = phi(u, leak, scale)
    z = np.einsum("bij,bj->bi", w, x) / root
    c = a * dphi(z, leak, scale)
    back = np.einsum("bji,bj->bi", w, c) / root
    return (
        u + h * back * dphi(u, leak, scale),
        w + (h / root) * c[:, :, None] * x[:, None, :],
        a + h * phi(z, leak, scale),
    )


def output(
    u: np.ndarray, w: np.ndarray, a: np.ndarray, leak: float, scale: float
) -> np.ndarray:
    n = u.shape[-1]
    x = phi(u, leak, scale)
    z = np.einsum("bij,bj->bi", w, x) / math.sqrt(n)
    return np.mean(a * phi(z, leak, scale), axis=1)


def delta(init, h: float, leak: float, scale: float) -> np.ndarray:
    fine = tuple(v.copy() for v in init)
    coarse = tuple(v.copy() for v in init)
    fine = step(*fine, h, leak, scale)
    fine = step(*fine, h, leak, scale)
    coarse = step(*coarse, 2.0 * h, leak, scale)
    return output(*fine, leak, scale) - output(*coarse, leak, scale)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--width", type=int, default=32)
    ap.add_argument("--samples", type=int, default=20000)
    ap.add_argument("--batch", type=int, default=250)
    ap.add_argument("--h", type=float, default=0.02)
    ap.add_argument("--leaks", nargs="+", type=float, default=[0.0, 0.1, 0.5])
    ap.add_argument("--seed", type=int, default=901)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    for leak in args.leaks:
        scale = math.sqrt(2.0 / (1.0 + leak * leak))
        estimates = []
        raw_h = []
        raw_half = []
        remaining = args.samples
        while remaining:
            b = min(remaining, args.batch)
            n = args.width
            init = (
                rng.standard_normal((b, n)),
                rng.standard_normal((b, n, n)),
                rng.standard_normal((b, n)),
            )
            anti = (init[0], init[1], -init[2])
            # The readout flip converts h to -h.  Averaging the two samples
            # projects exactly onto the ensemble-symmetric part and greatly
            # reduces Monte Carlo noise without changing E Delta(h).
            dh = 0.5 * (
                delta(init, args.h, leak, scale)
                + delta(anti, args.h, leak, scale)
            )
            d2 = 0.5 * (
                delta(init, args.h / 2.0, leak, scale)
                + delta(anti, args.h / 2.0, leak, scale)
            )
            estimates.append(2.0 * (dh - 8.0 * d2) / args.h**4)
            raw_h.append(dh)
            raw_half.append(d2)
            remaining -= b
        est = np.concatenate(estimates)
        xh = np.concatenate(raw_h)
        x2 = np.concatenate(raw_half)
        print(
            f"leak={leak:g} n={args.width} h={args.h:g} samples={args.samples} "
            f"c4={est.mean():.8g} se={est.std(ddof=1)/math.sqrt(len(est)):.3g} "
            f"mean_delta_h={xh.mean():.8g} mean_delta_h2={x2.mean():.8g}"
        )


if __name__ == "__main__":
    main()
