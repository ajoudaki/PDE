"""Generic solvers for a *compiled* finite McKean--Vlasov Liouville PDE.

This module is intentionally model-agnostic.  The dense-muP repository does
not currently emit the finite drift V, moment table, history ODE, or initial
Gaussian pushforward required to instantiate it.  Consequently this file is
solver infrastructure, not a simulation of the neural PDE.

The supported equation is

    d rho / dt + div(rho * b(x; M[rho], kappa)) = 0,
    d kappa / dt = K(M[rho], kappa).

Two independent weak solvers are provided:

1. weighted characteristics initialized by tensor Gauss--Hermite cubature;
2. a Hermite stochastic-Galerkin approximation of the characteristic map
   x = X(g,t), g ~ N(0,I).

Scrambled Sobol initial points can be fed to ``integrate_characteristics``
for a third, randomized characteristic realization.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import factorial
from typing import Callable

import numpy as np
from numpy.polynomial.hermite_e import hermeval
from numpy.polynomial.hermite import hermgauss
from scipy.special import ndtri
from scipy.stats import qmc

Array = np.ndarray


@dataclass(frozen=True)
class CompiledLiouville:
    """Numerical contract that the symbolic neural-PDE compiler must emit."""

    latent_dim: int
    state_dim: int
    kappa_dim: int
    initial_map: Callable[[Array], Array]
    moments: Callable[[Array, Array], Array]
    drift: Callable[[Array, Array, Array], Array]
    kappa_rhs: Callable[[Array, Array], Array]


def tensor_normal_rule(order: int, dim: int) -> tuple[Array, Array]:
    """Positive tensor Gauss--Hermite rule for N(0,I_dim)."""

    if order < 1 or dim < 1:
        raise ValueError("order and dim must be positive")
    z, w = hermgauss(order)
    z = np.sqrt(2.0) * z
    w = w / np.sqrt(np.pi)
    tuples = list(product(range(order), repeat=dim))
    nodes = np.asarray([[z[j] for j in idx] for idx in tuples], dtype=float)
    weights = np.asarray(
        [np.prod([w[j] for j in idx]) for idx in tuples], dtype=float
    )
    weights /= np.sum(weights)
    return nodes, weights


def scrambled_normal_sobol(
    power: int, dim: int, seed: int
) -> tuple[Array, Array]:
    """2**power scrambled Sobol points transformed to N(0,I_dim)."""

    if power < 1 or dim < 1:
        raise ValueError("power and dim must be positive")
    u = qmc.Sobol(d=dim, scramble=True, seed=seed).random_base2(power)
    eps = np.finfo(float).eps
    g = ndtri(np.clip(u, eps, 1.0 - eps))
    return g, np.full(g.shape[0], 1.0 / g.shape[0])


def _coupled_rhs(
    model: CompiledLiouville, x: Array, weights: Array, kappa: Array
) -> tuple[Array, Array]:
    mom = model.moments(x, weights)
    return model.drift(x, mom, kappa), model.kappa_rhs(mom, kappa)


def integrate_characteristics(
    model: CompiledLiouville,
    latent_nodes: Array,
    weights: Array,
    kappa0: Array,
    dt: float,
    steps: int,
) -> tuple[Array, Array]:
    """Classical RK4 for the coupled empirical-measure characteristic ODE."""

    x = np.asarray(model.initial_map(latent_nodes), dtype=float)
    kappa = np.asarray(kappa0, dtype=float).copy()
    weights = np.asarray(weights, dtype=float)
    if x.shape != (weights.size, model.state_dim):
        raise ValueError("initial_map returned the wrong shape")

    for _ in range(steps):
        x1, k1 = _coupled_rhs(model, x, weights, kappa)
        x2, k2 = _coupled_rhs(
            model, x + 0.5 * dt * x1, weights, kappa + 0.5 * dt * k1
        )
        x3, k3 = _coupled_rhs(
            model, x + 0.5 * dt * x2, weights, kappa + 0.5 * dt * k2
        )
        x4, k4 = _coupled_rhs(
            model, x + dt * x3, weights, kappa + dt * k3
        )
        x += (dt / 6.0) * (x1 + 2.0 * x2 + 2.0 * x3 + x4)
        kappa += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return x, kappa


def total_degree_indices(dim: int, degree: int) -> list[tuple[int, ...]]:
    """All multi-indices alpha with |alpha| <= degree."""

    return [
        alpha
        for alpha in product(range(degree + 1), repeat=dim)
        if sum(alpha) <= degree
    ]


def normalized_hermite_matrix(
    nodes: Array, indices: list[tuple[int, ...]]
) -> Array:
    """Orthonormal probabilists' Hermite basis evaluated at normal nodes."""

    nodes = np.asarray(nodes, dtype=float)
    out = np.ones((nodes.shape[0], len(indices)), dtype=float)
    for j, alpha in enumerate(indices):
        for axis, degree in enumerate(alpha):
            coeff = np.zeros(degree + 1)
            coeff[-1] = 1.0
            out[:, j] *= hermeval(nodes[:, axis], coeff) / np.sqrt(
                factorial(degree)
            )
    return out


def integrate_hermite_map(
    model: CompiledLiouville,
    degree: int,
    quadrature_order: int,
    kappa0: Array,
    dt: float,
    steps: int,
) -> tuple[Array, Array, list[tuple[int, ...]]]:
    """Stochastic Galerkin evolution of X(g,t), g~N(0,I).

    The characteristic map is represented as

        X(g,t) = sum_{|alpha|<=degree} c_alpha(t) H_alpha(g).

    The nonlinear residual is projected with a positive tensor
    Gauss--Hermite rule.  This evolves basis coefficients, not quadrature
    particles, and supplies an independent discretization check.
    """

    g, weights = tensor_normal_rule(quadrature_order, model.latent_dim)
    indices = total_degree_indices(model.latent_dim, degree)
    basis = normalized_hermite_matrix(g, indices)
    weighted_basis_t = basis.T * weights[None, :]
    x0 = np.asarray(model.initial_map(g), dtype=float)
    coeff = weighted_basis_t @ x0
    kappa = np.asarray(kappa0, dtype=float).copy()

    def rhs(c: Array, k: Array) -> tuple[Array, Array]:
        x = basis @ c
        mom = model.moments(x, weights)
        velocity = model.drift(x, mom, k)
        return weighted_basis_t @ velocity, model.kappa_rhs(mom, k)

    for _ in range(steps):
        c1, k1 = rhs(coeff, kappa)
        c2, k2 = rhs(coeff + 0.5 * dt * c1, kappa + 0.5 * dt * k1)
        c3, k3 = rhs(coeff + 0.5 * dt * c2, kappa + 0.5 * dt * k2)
        c4, k4 = rhs(coeff + dt * c3, kappa + dt * k3)
        coeff += (dt / 6.0) * (c1 + 2.0 * c2 + 2.0 * c3 + c4)
        kappa += (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    return coeff, kappa, indices


def linear_mean_field_benchmark() -> CompiledLiouville:
    """Analytically soluble smoke test: xdot=-(x-E[x]), x0=1+2g."""

    return CompiledLiouville(
        latent_dim=1,
        state_dim=1,
        kappa_dim=0,
        initial_map=lambda g: 1.0 + 2.0 * g,
        moments=lambda x, w: np.asarray([w @ x[:, 0]]),
        drift=lambda x, mom, _k: -(x - mom[0]),
        kappa_rhs=lambda _mom, _k: np.empty(0),
    )


if __name__ == "__main__":
    benchmark = linear_mean_field_benchmark()
    g, w = tensor_normal_rule(order=9, dim=1)
    x, _ = integrate_characteristics(
        benchmark, g, w, np.empty(0), dt=0.01, steps=100
    )
    exact = 1.0 + 2.0 * np.exp(-1.0) * g
    characteristic_error = np.max(np.abs(x - exact))

    coeff, _, indices = integrate_hermite_map(
        benchmark,
        degree=2,
        quadrature_order=9,
        kappa0=np.empty(0),
        dt=0.01,
        steps=100,
    )
    basis = normalized_hermite_matrix(g, indices)
    galerkin_error = np.max(np.abs(basis @ coeff - exact))
    print(
        {
            "characteristic_max_error": float(characteristic_error),
            "hermite_map_max_error": float(galerkin_error),
        }
    )
