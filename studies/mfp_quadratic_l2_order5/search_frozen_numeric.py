#!/usr/bin/env python3
"""Gauss-Hermite search for signed frozen paired defects (exploratory)."""

import numpy as np
from numpy.polynomial.hermite import hermgauss


def eval_poly(c, x):
    return np.polynomial.polynomial.polyval(x, c)


def deriv(c):
    return np.arange(1, len(c))*c[1:]


def output(c, h, steps, A, Z):
    dc = deriv(c)
    a, z = A.copy(), Z.copy()
    for _ in range(steps):
        oa, oz = a, z
        a = oa + h*eval_poly(c, oz)
        z = oz + h*oa*eval_poly(dc, oz)
    return a*eval_poly(c, z)


def main():
    nodes, weights = hermgauss(80)
    nodes = np.sqrt(2)*nodes
    W = np.outer(weights, weights)/np.pi
    A, Z = np.meshgrid(nodes, nodes, indexing="ij")
    rng = np.random.default_rng(20260825)
    hs = np.array([.01, .03, .1, .3, 1.0])
    best = (np.inf, None)
    for trial in range(20000):
        c = rng.normal(size=4)
        # Exact Gaussian L2 norm from the same sufficiently-high quadrature.
        norm = np.sqrt(np.sum(W*eval_poly(c, Z)**2))
        c /= norm
        vals = []
        for h in hs:
            fine = np.sum(W*output(c, h, 2, A, Z))
            coarse = np.sum(W*output(c, 2*h, 1, A, Z))
            vals.append(fine-coarse)
        m = min(vals)
        if m < best[0]:
            best = (m, (c.copy(), vals))
        if m < -1e-8:
            print("FOUND", c, vals)
            return
    print("NO NEGATIVE; BEST", best)


if __name__ == "__main__":
    main()
