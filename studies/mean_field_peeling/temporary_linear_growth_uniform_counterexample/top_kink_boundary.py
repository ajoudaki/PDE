"""Exact top-gate h^2 boundary symbol for normalized leaky ReLU.

The limiting initial normal velocities are
    A = R + 2 a p_+,  B = R + 2 a p_-,
where a~N(0,1), R~N(0,e), and e=E phi'(G)^4.  This file evaluates the
piecewise quadratic boundary integral; it is an audit aid, not the width
identification proof.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from numpy.polynomial.hermite import hermgauss


def symbol(readout: np.ndarray, response: np.ndarray, p: float, q: float) -> np.ndarray:
    """Full-potential symbol, including the smooth off-diagonal slope.

    ``minus`` and ``plus`` below are the normal Euler velocities on the two
    sides.  Their corresponding full-observable slopes are velocity/2, not
    merely ``readout*q`` and ``readout*p``; omitting the common response is
    the tempting but incorrect frozen-head calculation.
    """
    minus = response + 2.0 * readout * q
    plus = response + 2.0 * readout * p
    jump = readout * (p - q)  # (plus-minus)/2
    crossing = (minus > 0.0) | (plus < 0.0)
    return jump * minus * plus * crossing


def quadrature(leak: float, order: int) -> tuple[float, float, float, float]:
    scale = math.sqrt(2.0 / (1.0 + leak * leak))
    p, q = scale, scale * leak
    e = 2.0 * (1.0 + leak**4) / (1.0 + leak * leak) ** 2
    nodes, weights = hermgauss(order)
    a = math.sqrt(2.0) * nodes[:, None]
    r = math.sqrt(2.0 * e) * nodes[None, :]
    w = weights[:, None] * weights[None, :] / math.pi
    k = symbol(a, r, p, q)
    mean = float(np.sum(w * k))
    neg = float(np.sum(w * np.minimum(k, 0.0)))
    pos = float(np.sum(w * np.maximum(k, 0.0)))
    return mean, pos, neg, e


def positive_integral(leak: float, order: int = 600) -> float:
    """One-dimensional positive formula for gamma(0) E[symbol]."""
    scale = math.sqrt(2.0 / (1.0 + leak * leak))
    p, q = scale, scale * leak
    e = 2.0 * (1.0 + leak**4) / (1.0 + leak * leak) ** 2
    # Gauss--Legendre on the compact interval [2q,2p].
    nodes, weights = np.polynomial.legendre.leggauss(order)
    lo, hi = 2.0 * q, 2.0 * p
    y = 0.5 * (hi - lo) * nodes + 0.5 * (hi + lo)
    integral = 0.5 * (hi - lo) * np.dot(
        weights,
        (y - lo) * (hi - y) / (1.0 + y * y / e) ** 2.5,
    )
    return float(3.0 * (p - q) * integral / (4.0 * math.pi * math.sqrt(e)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--order", type=int, default=300)
    ap.add_argument("--leaks", nargs="+", type=float, default=[0, .01, .1, .25, .5, .75, .9, .99])
    args = ap.parse_args()
    gamma0 = 1.0 / math.sqrt(2.0 * math.pi)
    for leak in args.leaks:
        mean, pos, neg, e = quadrature(leak, args.order)
        exact = positive_integral(leak)
        print(
            f"leak={leak:.6g} e={e:.9g} EK={mean:.12g} "
            f"gamma0_EK={gamma0*mean:.12g} integral={exact:.12g} "
            f"pos={pos:.12g} neg={neg:.12g}"
        )


if __name__ == "__main__":
    main()
