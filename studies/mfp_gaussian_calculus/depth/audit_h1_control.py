"""Reproduce the independent generic-activation H=1 control.

This is an audit utility, not part of the arbitrary-depth recurrence.  It
compares the closed one-hidden-layer Gaussian formula against the exact
finite-width moving-flow compiler averaged over independent neurons.
"""

from __future__ import annotations

import argparse
from math import sqrt

import numpy as np
from numpy.polynomial.hermite import hermgauss

from .finite_width_jet import feature_ascent_jet
from .model import sample_state


def quadratic_derivative(order: int, x: np.ndarray) -> np.ndarray:
    if order == 0:
        return x**2
    if order == 1:
        return 2.0 * x
    if order == 2:
        return 2.0 * np.ones_like(x)
    return np.zeros_like(x)


def sine_derivative(order: int, x: np.ndarray) -> np.ndarray:
    return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]


def tanh_derivative(order: int, x: np.ndarray) -> np.ndarray:
    t = np.tanh(x)
    return (
        t,
        1.0 - t * t,
        -2.0 * t * (1.0 - t * t),
        -2.0 * (1.0 - t * t) * (1.0 - 3.0 * t * t),
    )[order]


CASES = (
    ("quadratic", quadratic_derivative, 0.7),
    ("sin", sine_derivative, 1.3),
    ("tanh", tanh_derivative, 0.9),
)


def gaussian_correction(q0: float, oracle, *, order: int = 160) -> float:
    """Evaluate the closed H=1 expression by Gauss--Hermite quadrature."""

    nodes, weights = hermgauss(order)
    u = sqrt(2.0 * q0) * nodes
    phi, phi1, phi2, phi3 = (oracle(r, u) for r in range(4))
    integrand = (
        4.0 * q0**2 * phi1**4
        + 4.0 * q0 * phi**2 * phi1**2
        + 14.0 * q0**2 * phi * phi2 * phi1**2
        + 12.0 * q0**3 * phi2**2 * phi1**2
        + 6.0 * q0**3 * phi3 * phi1**3
    )
    return float(weights @ integrand / sqrt(np.pi))


def finite_width_samples(
    q0: float,
    oracle,
    *,
    width: int,
    seeds: int,
) -> np.ndarray:
    values = []
    gram = np.asarray([[q0]])
    channel = np.asarray([1.0])
    for seed in range(seeds):
        state = sample_state(width, gram, 1, 97_000 + seed)
        values.append(
            feature_ascent_jet(state, gram, channel, oracle).derivatives[3]
        )
    return np.asarray(values)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=250_000)
    parser.add_argument("--seeds", type=int, default=10)
    parser.add_argument("--quadrature-order", type=int, default=160)
    args = parser.parse_args()
    for name, oracle, q0 in CASES:
        target = gaussian_correction(q0, oracle, order=args.quadrature_order)
        samples = finite_width_samples(
            q0, oracle, width=args.width, seeds=args.seeds
        )
        standard_error = (
            float(samples.std(ddof=1) / sqrt(args.seeds))
            if args.seeds > 1
            else float("nan")
        )
        print(
            f"{name:9s} q0={q0:.1f} GH={target:.12g} "
            f"finite={samples.mean():.12g} SE={standard_error:.6g}"
        )


if __name__ == "__main__":
    main()
