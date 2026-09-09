"""Quadrature evaluator for the finite-step one-hidden-layer Gaussian DAG."""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from numpy.polynomial.hermite import hermgauss


ArrayFunction = Callable[[np.ndarray], np.ndarray]


def _standard_gaussian_rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    """Return nodes and normalized weights for a standard Gaussian."""
    if order < 2:
        raise ValueError("order must be at least 2")
    nodes, weights = hermgauss(order)
    return np.sqrt(2.0) * nodes, weights / np.sqrt(np.pi)


def expected_output_raw(
    phi: ArrayFunction,
    dphi: ArrayFunction,
    eta: float,
    *,
    q: float = 1.0,
    order: int = 80,
    eta_readout: float | None = None,
    eta_feature: float | None = None,
) -> float:
    """Evaluate E[(A+eta_a phi(Z)) phi(Z+eta_w q A phi'(Z))]."""
    if q <= 0.0:
        raise ValueError("q must be positive")
    eta_a = eta if eta_readout is None else eta_readout
    eta_w = eta if eta_feature is None else eta_feature
    nodes, weights = _standard_gaussian_rule(order)
    a = nodes[None, :]
    z = np.sqrt(q) * nodes[:, None]
    z_plus = z + eta_w * q * a * dphi(z)
    integrand = (a + eta_a * phi(z)) * phi(z_plus)
    return float(weights @ integrand @ weights)


def expected_output_stein(
    phi: ArrayFunction,
    dphi: ArrayFunction,
    eta: float,
    *,
    q: float = 1.0,
    order: int = 80,
    eta_readout: float | None = None,
    eta_feature: float | None = None,
) -> float:
    """Evaluate the conditional-Stein form of the same expectation."""
    if q <= 0.0:
        raise ValueError("q must be positive")
    eta_a = eta if eta_readout is None else eta_readout
    eta_w = eta if eta_feature is None else eta_feature
    nodes, weights = _standard_gaussian_rule(order)
    a = nodes[None, :]
    z = np.sqrt(q) * nodes[:, None]
    z_plus = z + eta_w * q * a * dphi(z)
    integrand = (
        eta_a * phi(z) * phi(z_plus)
        + eta_w * q * dphi(z) * dphi(z_plus)
    )
    return float(weights @ integrand @ weights)


def expected_output_steps(
    phi: ArrayFunction,
    dphi: ArrayFunction,
    eta: float,
    steps: int,
    *,
    q: float = 1.0,
    order: int = 80,
) -> float:
    """Iterate simultaneous feature-ascent Euler steps from Gaussian data."""
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    if q <= 0.0:
        raise ValueError("q must be positive")

    nodes, weights = _standard_gaussian_rule(order)
    a = np.broadcast_to(nodes[None, :], (order, order)).copy()
    z = np.broadcast_to(
        np.sqrt(q) * nodes[:, None], (order, order)
    ).copy()

    for _ in range(steps):
        a_next = a + eta * phi(z)
        z_next = z + eta * q * a * dphi(z)
        a, z = a_next, z_next

    return float(weights @ (a * phi(z)) @ weights)


def expected_output_steps_stein(
    phi: ArrayFunction,
    dphi: ArrayFunction,
    ddphi: ArrayFunction,
    eta: float,
    steps: int,
    *,
    q: float = 1.0,
    order: int = 80,
) -> float:
    """Evaluate the k-step output through its initial-Gaussian tangent."""
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    if q <= 0.0:
        raise ValueError("q must be positive")

    nodes, weights = _standard_gaussian_rule(order)
    a = np.broadcast_to(nodes[None, :], (order, order)).copy()
    z = np.broadcast_to(
        np.sqrt(q) * nodes[:, None], (order, order)
    ).copy()
    u = np.ones_like(a)
    v = np.zeros_like(z)
    readout_sum = np.zeros_like(z)

    for _ in range(steps):
        readout_sum += phi(z)
        u_next = u + eta * dphi(z) * v
        v_next = v + eta * q * (
            u * dphi(z) + a * ddphi(z) * v
        )
        a_next = a + eta * phi(z)
        z_next = z + eta * q * a * dphi(z)
        a, z, u, v = a_next, z_next, u_next, v_next

    integrand = eta * readout_sum * phi(z) + dphi(z) * v
    return float(weights @ integrand @ weights)
