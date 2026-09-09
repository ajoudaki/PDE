"""Independent scalar audit reference for the fixed-depth B=1 GNF.

This module does not implement the four-Gaussian IR in
``DEPTH_B1_GAUSSIAN_RECURSION.md``.  It contracts that IR analytically first.
At each layer it retains only the three forward quantities actually needed by
the terminal scalar: ``G11=E[(X^[1])^2]``, ``G02=E[X^[0] X^[2]]``, and
``a3=E[d X^[3] / dR]``.  The differentiated reverse pass retains ``beta``
and ``chi``.  Every update is a one-dimensional Gaussian expectation.

It is an audit oracle, not the authoritative derivation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt
from typing import Callable

import numpy as np
from numpy.polynomial.hermite import hermgauss


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class DepthB1AuditResult:
    ntk: float
    straight_line: float
    hessian_square: float
    correction: float
    q: np.ndarray
    d: np.ndarray
    reverse_variance: np.ndarray
    source_variance: np.ndarray
    theta: np.ndarray
    g11: np.ndarray
    g02: np.ndarray
    a3: np.ndarray
    beta: np.ndarray
    chi: np.ndarray


def _gaussian_values(
    variance: float,
    activation_derivative: DerivativeOracle,
    order: int,
) -> tuple[np.ndarray, np.ndarray, tuple[np.ndarray, ...]]:
    if variance < 0.0:
        raise ValueError("variance must be nonnegative")
    if order < 2:
        raise ValueError("quadrature order must be at least two")
    nodes, weights = hermgauss(order)
    points = sqrt(2.0 * variance) * nodes
    probability_weights = weights / sqrt(pi)
    derivatives = tuple(
        np.asarray(activation_derivative(r, points), dtype=np.float64)
        for r in range(4)
    )
    return points, probability_weights, derivatives


def evaluate_depth_b1_audit_recurrence(
    input_variance: float,
    hidden_layers: int,
    activation_derivative: DerivativeOracle,
    *,
    quadrature_order: int = 80,
) -> DepthB1AuditResult:
    """Evaluate the independently contracted fixed-``H``, ``B=1`` recursion."""

    if hidden_layers < 1:
        raise ValueError("hidden_layers must be positive")
    if input_variance < 0.0:
        raise ValueError("input_variance must be nonnegative")

    h = hidden_layers
    q = np.zeros(h + 1, dtype=np.float64)
    d = np.zeros(h + 1, dtype=np.float64)
    atoms: list[dict[str, float] | None] = [None] * (h + 1)
    q[0] = input_variance

    for layer in range(1, h + 1):
        _, weights, values = _gaussian_values(
            q[layer - 1], activation_derivative, quadrature_order
        )
        p0, p1, p2, p3 = values
        expectation = lambda value: float(np.dot(weights, value))
        q[layer] = expectation(p0**2)
        d[layer] = expectation(p1**2)
        atoms[layer] = {
            "p1_4": expectation(p1**4),
            "p0_p2": expectation(p0 * p2),
            "p0_p2_p1_2": expectation(p0 * p2 * p1**2),
            "p3_p1": expectation(p3 * p1),
            "p2_2": expectation(p2**2),
            "p3_p1_3": expectation(p3 * p1**3),
            "p2_2_p1_2": expectation(p2**2 * p1**2),
            "p1_2_p0_2": expectation(p1**2 * p0**2),
            "p2_p1_2_p0": expectation(p2 * p1**2 * p0),
        }

    # R_l has variance b_l; Delta_l=phi'(Z_l)R_l has variance p_l.
    reverse_variance = np.zeros(h + 1, dtype=np.float64)
    source_variance = np.zeros(h + 1, dtype=np.float64)
    reverse_variance[h] = 1.0
    for layer in range(h, 0, -1):
        source_variance[layer] = d[layer] * reverse_variance[layer]
        if layer > 1:
            reverse_variance[layer - 1] = source_variance[layer]

    theta = np.zeros(h + 1, dtype=np.float64)
    theta[0] = q[0]
    for layer in range(1, h + 1):
        theta[layer] = q[layer] + d[layer] * theta[layer - 1]

    # Bottom-up frozen forward jet.
    g11 = np.zeros(h + 1, dtype=np.float64)
    g02 = np.zeros(h + 1, dtype=np.float64)
    a3 = np.zeros(h + 1, dtype=np.float64)

    first = atoms[1]
    assert first is not None
    b = reverse_variance[1]
    g11[1] = q[0] ** 2 * b * first["p1_4"]
    g02[1] = q[0] ** 2 * b * first["p0_p2_p1_2"]
    a3[1] = 3.0 * q[0] ** 3 * b * first["p3_p1_3"]

    for layer in range(2, h + 1):
        local = atoms[layer]
        assert local is not None
        lam1 = theta[layer - 1]
        lam3 = a3[layer - 1] + 3.0 * g02[layer - 1]
        b = reverse_variance[layer]
        previous_g11 = g11[layer - 1]
        previous_g02 = g02[layer - 1]

        g11[layer] = (
            previous_g11 * d[layer]
            + lam1**2 * b * local["p1_4"]
        )
        g02[layer] = (
            previous_g11 * local["p0_p2"]
            + lam1**2 * b * local["p0_p2_p1_2"]
            + previous_g02 * (d[layer] + local["p0_p2"])
        )
        a3[layer] = (
            3.0 * lam1 * previous_g11 * local["p3_p1"]
            + 3.0 * lam1**3 * b * local["p3_p1_3"]
            + 3.0
            * lam1
            * previous_g02
            * (local["p3_p1"] + local["p2_2"])
            + lam3 * d[layer]
        )

    straight_line = a3[h] + 3.0 * g02[h]

    # Top-down differentiated reverse jet.  At the top, R_tilde=X^[0],
    # corresponding to kappa=1 and zero fresh E variance.
    beta = np.zeros(h + 1, dtype=np.float64)
    chi = np.zeros(h + 1, dtype=np.float64)
    next_beta = 0.0
    next_chi = 1.0
    for layer in range(h, 0, -1):
        local = atoms[layer]
        assert local is not None
        previous_g11 = 0.0 if layer == 1 else g11[layer - 1]
        lam1 = theta[layer - 1]
        b = reverse_variance[layer]
        beta[layer] = (
            previous_g11 * b * local["p2_2"]
            + 3.0 * lam1**2 * b**2 * local["p2_2_p1_2"]
            + next_beta * d[layer]
            + next_chi**2 * local["p1_2_p0_2"]
            + 2.0 * lam1 * next_chi * b * local["p2_p1_2_p0"]
        )
        rho0 = (
            lam1
            * b
            * (local["p3_p1"] + local["p2_2"])
            + next_chi * (local["p0_p2"] + d[layer])
        )
        chi[layer] = source_variance[layer] + rho0
        next_beta = beta[layer]
        next_chi = chi[layer]

    hessian_square = g11[h] + q[0] * beta[1]
    for layer in range(2, h + 1):
        hessian_square += (
            q[layer - 1] * beta[layer]
            + source_variance[layer] * g11[layer - 1]
        )

    correction = 2.0 * straight_line + 4.0 * hessian_square
    return DepthB1AuditResult(
        ntk=float(theta[h]),
        straight_line=float(straight_line),
        hessian_square=float(hessian_square),
        correction=float(correction),
        q=q,
        d=d,
        reverse_variance=reverse_variance,
        source_variance=source_variance,
        theta=theta,
        g11=g11,
        g02=g02,
        a3=a3,
        beta=beta,
        chi=chi,
    )

