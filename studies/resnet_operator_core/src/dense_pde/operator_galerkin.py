"""Operator-Galerkin PDE for the continuous-depth dense Euclidean-muP model.

This module contains no finite-network width and no dense n-by-n weight
matrix.  For a fixed orthonormal family ``phi_j`` on the immutable Gaussian
neuron-type variable x, the iid initial dense operator is represented by

    (W0 u)(x, eps) = sigma_w * sum_j eps_j <phi_j, u>.

The learned part of one row is represented by coefficients c_j:

    (W u)(x, eps) = sum_j (sigma_w eps_j + c_j) <phi_j, u>.

The same coefficients give the transpose

    W* beta = sum_j phi_j E[(sigma_w eps_j + c_j) beta].

Consequently orientation and transpose reuse are exact at every finite
basis order P.  The coefficient characteristics are the projected ordinary
Euclidean muP gradient flow

    c_j,t = -gamma sum_q e_q beta_q <phi_j, h_q>.

The distribution in (x, eps, c) obeys a finite-dimensional McKean--Vlasov
continuity equation.  This file solves it by deterministic equal-weight
characteristics.  M and R are quadrature resolutions, not network widths.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import factorial

import numpy as np
from scipy.special import eval_hermitenorm, ndtri
from scipy.stats import qmc

Array = np.ndarray


@dataclass(frozen=True)
class PDESpec:
    """Static architecture and compiler parameters.

    ``basis_size`` is the operator Galerkin order P and ``depth_nodes`` is
    the deterministic depth discretization N.  ``base_points`` and
    ``fast_points`` control numerical integration only.
    """

    X: Array
    y: Array
    basis_size: int
    depth_nodes: int
    base_points: int
    fast_points: int
    quadrature_seed: int = 20260723
    sigma_w: float = 0.65
    A: float = 1.0
    gamma: float = 1.0

    def validate(self) -> None:
        if self.X.ndim != 2 or self.y.ndim != 1:
            raise ValueError("X must be d x m and y must have shape (m,)")
        if self.X.shape[1] != self.y.size:
            raise ValueError("X and y disagree on sample count")
        if min(
            self.basis_size,
            self.depth_nodes,
            self.base_points,
            self.fast_points,
        ) < 1:
            raise ValueError("all compiler and quadrature sizes must be positive")
        if self.base_points < self.basis_size:
            raise ValueError("base_points must be at least basis_size")
        if self.fast_points <= self.basis_size:
            raise ValueError("fast_points must exceed basis_size for whitening")
        for value, name in (
            (self.sigma_w, "sigma_w"),
            (self.A, "A"),
            (self.gamma, "gamma"),
        ):
            if value <= 0:
                raise ValueError(f"{name} must be positive")


@dataclass(frozen=True)
class PDEQuadrature:
    """Static quadrature and fixed operator basis."""

    base_latent: Array  # (M, d+1), standard Gaussian
    base_weights: Array  # (M,), positive and sums to one
    phi: Array  # (M, P), empirically orthonormal
    epsilon: Array  # (R, P), centered and whitened
    fast_weights: Array  # (R,), positive and sums to one
    multi_indices: tuple[tuple[int, ...], ...]
    raw_basis_gram_error: float
    raw_basis_min_eigenvalue: float
    raw_basis_max_eigenvalue: float
    raw_basis_condition: float
    whitened_basis_gram_error: float
    fast_mean_error: float
    raw_fast_min_eigenvalue: float
    raw_fast_max_eigenvalue: float
    raw_fast_condition: float
    fast_cov_error: float


@dataclass
class PDEState:
    """Characteristic state.

    B and a are slow neuron-type fields.  c[l,i,r,j] is the learned row
    coefficient at depth cell l, base point i, fast point r, basis mode j.
    """

    B: Array  # (M, d)
    a: Array  # (M,)
    c: Array  # (N, M, R, P)

    def copy(self) -> "PDEState":
        return PDEState(self.B.copy(), self.a.copy(), self.c.copy())


@dataclass
class Fields:
    h: Array  # (N+1, M, m)
    p: Array  # (N+1, M, m)
    z: Array  # (N, M, R, m)
    D: Array  # (N, M, R, m)
    beta: Array  # (N, M, R, m)
    hcoef: Array  # (N, P, m)


@dataclass
class Observable:
    f: Array
    loss: float
    grams: Array
    theta: Array
    theta_min: float
    residual_norm: float
    loss_dot: float
    projected_energy: Array


def _normal_sobol(count: int, dim: int, seed: int) -> Array:
    if count & (count - 1):
        raise ValueError("Sobol point counts must be powers of two")
    sampler = qmc.Sobol(d=dim, scramble=True, seed=seed)
    unit = sampler.random_base2(int(np.log2(count)))
    unit = np.clip(unit, np.finfo(float).eps, 1.0 - np.finfo(float).eps)
    return ndtri(unit)


def _multi_indices(dim: int, count: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate multivariate Hermites by total degree then lexicographically.

    Degree one is deliberately ordered x_0, x_1, ..., so P=d+2 contains
    the constant, every input-map coordinate, and the readout coordinate.
    """

    records: list[tuple[int, ...]] = []
    degree = 0
    while len(records) < count:
        degree_records = [
            alpha for alpha in product(range(degree + 1), repeat=dim)
            if sum(alpha) == degree
        ]
        degree_records.sort(
            key=lambda alpha: tuple(
                -alpha[j] for j in range(dim)
            )
        )
        records.extend(degree_records)
        degree += 1
    return tuple(records[:count])


def _eval_hermite_basis(x: Array, indices: tuple[tuple[int, ...], ...]) -> Array:
    values = np.ones((x.shape[0], len(indices)), dtype=float)
    for j, alpha in enumerate(indices):
        norm = 1.0
        for coordinate, degree in enumerate(alpha):
            if degree:
                values[:, j] *= eval_hermitenorm(degree, x[:, coordinate])
                norm *= factorial(degree)
        values[:, j] /= np.sqrt(norm)
    return values


def _symmetric_inverse_sqrt(matrix: Array, floor: float = 1e-12) -> Array:
    eigenvalues, eigenvectors = np.linalg.eigh(0.5 * (matrix + matrix.T))
    if eigenvalues[0] <= floor:
        raise ValueError(
            f"quadrature Gram is rank deficient: min eigenvalue={eigenvalues[0]}"
        )
    return (eigenvectors / np.sqrt(eigenvalues)) @ eigenvectors.T


def build_quadrature(spec: PDESpec) -> PDEQuadrature:
    spec.validate()
    latent_dim = spec.X.shape[0] + 1
    x = _normal_sobol(spec.base_points, latent_dim, spec.quadrature_seed)
    base_weights = np.full(spec.base_points, 1.0 / spec.base_points)
    # Make the initialization moments used by the model exact at every
    # numerical resolution.  This is a deterministic cubature correction,
    # not a learned or positive-time fit.
    x = x - np.mean(x, axis=0, keepdims=True)
    x_cov = x.T @ (base_weights[:, None] * x)
    x = x @ _symmetric_inverse_sqrt(x_cov)
    indices = _multi_indices(latent_dim, spec.basis_size)
    raw_phi = _eval_hermite_basis(x, indices)
    raw_gram = raw_phi.T @ (base_weights[:, None] * raw_phi)
    raw_basis_eigenvalues = np.linalg.eigvalsh(raw_gram)
    phi = raw_phi @ _symmetric_inverse_sqrt(raw_gram)
    phi_gram = phi.T @ (base_weights[:, None] * phi)

    epsilon = _normal_sobol(
        spec.fast_points,
        spec.basis_size,
        spec.quadrature_seed + 104729,
    )
    fast_weights = np.full(spec.fast_points, 1.0 / spec.fast_points)
    epsilon = (
        epsilon
        - np.sum(fast_weights[:, None] * epsilon, axis=0, keepdims=True)
    )
    epsilon_cov = epsilon.T @ (fast_weights[:, None] * epsilon)
    raw_fast_eigenvalues = np.linalg.eigvalsh(epsilon_cov)
    epsilon = epsilon @ _symmetric_inverse_sqrt(epsilon_cov)
    whitened_cov = epsilon.T @ (fast_weights[:, None] * epsilon)

    return PDEQuadrature(
        base_latent=x,
        base_weights=base_weights,
        phi=phi,
        epsilon=epsilon,
        fast_weights=fast_weights,
        multi_indices=indices,
        raw_basis_gram_error=float(
            np.linalg.norm(raw_gram - np.eye(spec.basis_size), ord=2)
        ),
        raw_basis_min_eigenvalue=float(raw_basis_eigenvalues[0]),
        raw_basis_max_eigenvalue=float(raw_basis_eigenvalues[-1]),
        raw_basis_condition=float(
            raw_basis_eigenvalues[-1] / raw_basis_eigenvalues[0]
        ),
        whitened_basis_gram_error=float(
            np.linalg.norm(phi_gram - np.eye(spec.basis_size), ord=2)
        ),
        fast_mean_error=float(
            np.linalg.norm(
                np.sum(fast_weights[:, None] * epsilon, axis=0)
            )
        ),
        raw_fast_min_eigenvalue=float(raw_fast_eigenvalues[0]),
        raw_fast_max_eigenvalue=float(raw_fast_eigenvalues[-1]),
        raw_fast_condition=float(
            raw_fast_eigenvalues[-1] / raw_fast_eigenvalues[0]
        ),
        fast_cov_error=float(
            np.linalg.norm(whitened_cov - np.eye(spec.basis_size), ord=2)
        ),
    )


def _normal_hermite_tensor(order: int, dim: int) -> tuple[Array, Array]:
    """Tensor Gauss--Hermite rule for N(0,I_dim)."""

    if order < 2:
        raise ValueError("Gauss-Hermite order must be at least two")
    nodes_1d, weights_1d = np.polynomial.hermite.hermgauss(order)
    nodes_1d = np.sqrt(2.0) * nodes_1d
    weights_1d = weights_1d / np.sqrt(np.pi)
    index = np.array(list(product(range(order), repeat=dim)), dtype=int)
    nodes = nodes_1d[index]
    weights = np.prod(weights_1d[index], axis=1)
    return nodes, weights


def build_tensor_quadrature(
    spec: PDESpec, base_order: int = 3, fast_order: int = 3
) -> PDEQuadrature:
    """Independent deterministic tensor-cubature realization.

    This is practical only for the first Galerkin level.  It is useful as a
    method audit because it shares no Sobol points or empirical whitening
    with :func:`build_quadrature`.
    """

    spec.validate()
    latent_dim = spec.X.shape[0] + 1
    x, base_weights = _normal_hermite_tensor(base_order, latent_dim)
    epsilon, fast_weights = _normal_hermite_tensor(
        fast_order, spec.basis_size
    )
    if x.shape[0] != spec.base_points:
        raise ValueError(
            f"base_points must equal base_order^(d+1)={x.shape[0]}"
        )
    if epsilon.shape[0] != spec.fast_points:
        raise ValueError(
            f"fast_points must equal fast_order^P={epsilon.shape[0]}"
        )

    indices = _multi_indices(latent_dim, spec.basis_size)
    raw_phi = _eval_hermite_basis(x, indices)
    raw_gram = raw_phi.T @ (base_weights[:, None] * raw_phi)
    raw_basis_eigenvalues = np.linalg.eigvalsh(raw_gram)
    phi = raw_phi @ _symmetric_inverse_sqrt(raw_gram)
    phi_gram = phi.T @ (base_weights[:, None] * phi)
    epsilon_mean = np.sum(fast_weights[:, None] * epsilon, axis=0)
    epsilon_cov = epsilon.T @ (fast_weights[:, None] * epsilon)
    raw_fast_eigenvalues = np.linalg.eigvalsh(epsilon_cov)

    return PDEQuadrature(
        base_latent=x,
        base_weights=base_weights,
        phi=phi,
        epsilon=epsilon,
        fast_weights=fast_weights,
        multi_indices=indices,
        raw_basis_gram_error=float(
            np.linalg.norm(raw_gram - np.eye(spec.basis_size), ord=2)
        ),
        raw_basis_min_eigenvalue=float(raw_basis_eigenvalues[0]),
        raw_basis_max_eigenvalue=float(raw_basis_eigenvalues[-1]),
        raw_basis_condition=float(
            raw_basis_eigenvalues[-1] / raw_basis_eigenvalues[0]
        ),
        whitened_basis_gram_error=float(
            np.linalg.norm(phi_gram - np.eye(spec.basis_size), ord=2)
        ),
        fast_mean_error=float(np.linalg.norm(epsilon_mean)),
        raw_fast_min_eigenvalue=float(raw_fast_eigenvalues[0]),
        raw_fast_max_eigenvalue=float(raw_fast_eigenvalues[-1]),
        raw_fast_condition=float(
            raw_fast_eigenvalues[-1] / raw_fast_eigenvalues[0]
        ),
        fast_cov_error=float(
            np.linalg.norm(epsilon_cov - np.eye(spec.basis_size), ord=2)
        ),
    )


def build_hybrid_quadrature(
    spec: PDESpec,
    base_order: int = 3,
) -> PDEQuadrature:
    """Tensor Gauss--Hermite base labels plus whitened Sobol row noise.

    For the complete degree-two basis in four base dimensions, order-three
    Gauss--Hermite integrates every basis Gram entry exactly. Unlike a full
    tensor rule, the fast ``P``-dimensional Gaussian remains practical.
    """

    spec.validate()
    latent_dim = spec.X.shape[0] + 1
    x, base_weights = _normal_hermite_tensor(base_order, latent_dim)
    if x.shape[0] != spec.base_points:
        raise ValueError(
            f"base_points must equal base_order^(d+1)={x.shape[0]}"
        )
    indices = _multi_indices(latent_dim, spec.basis_size)
    raw_phi = _eval_hermite_basis(x, indices)
    raw_gram = raw_phi.T @ (base_weights[:, None] * raw_phi)
    raw_basis_eigenvalues = np.linalg.eigvalsh(raw_gram)
    phi = raw_phi @ _symmetric_inverse_sqrt(raw_gram)
    phi_gram = phi.T @ (base_weights[:, None] * phi)

    epsilon = _normal_sobol(
        spec.fast_points,
        spec.basis_size,
        spec.quadrature_seed + 104729,
    )
    fast_weights = np.full(spec.fast_points, 1.0 / spec.fast_points)
    epsilon = (
        epsilon
        - np.sum(fast_weights[:, None] * epsilon, axis=0, keepdims=True)
    )
    epsilon_cov = epsilon.T @ (fast_weights[:, None] * epsilon)
    raw_fast_eigenvalues = np.linalg.eigvalsh(epsilon_cov)
    epsilon = epsilon @ _symmetric_inverse_sqrt(epsilon_cov)
    whitened_cov = epsilon.T @ (fast_weights[:, None] * epsilon)

    return PDEQuadrature(
        base_latent=x,
        base_weights=base_weights,
        phi=phi,
        epsilon=epsilon,
        fast_weights=fast_weights,
        multi_indices=indices,
        raw_basis_gram_error=float(
            np.linalg.norm(raw_gram - np.eye(spec.basis_size), ord=2)
        ),
        raw_basis_min_eigenvalue=float(raw_basis_eigenvalues[0]),
        raw_basis_max_eigenvalue=float(raw_basis_eigenvalues[-1]),
        raw_basis_condition=float(
            raw_basis_eigenvalues[-1] / raw_basis_eigenvalues[0]
        ),
        whitened_basis_gram_error=float(
            np.linalg.norm(phi_gram - np.eye(spec.basis_size), ord=2)
        ),
        fast_mean_error=float(
            np.linalg.norm(
                np.sum(fast_weights[:, None] * epsilon, axis=0)
            )
        ),
        raw_fast_min_eigenvalue=float(raw_fast_eigenvalues[0]),
        raw_fast_max_eigenvalue=float(raw_fast_eigenvalues[-1]),
        raw_fast_condition=float(
            raw_fast_eigenvalues[-1] / raw_fast_eigenvalues[0]
        ),
        fast_cov_error=float(
            np.linalg.norm(whitened_cov - np.eye(spec.basis_size), ord=2)
        ),
    )


def initialize(spec: PDESpec, quadrature: PDEQuadrature) -> PDEState:
    d = spec.X.shape[0]
    M = spec.base_points
    return PDEState(
        B=quadrature.base_latent[:, :d].copy(),
        a=(spec.A * quadrature.base_latent[:, d]).copy(),
        c=np.zeros(
            (
                spec.depth_nodes,
                M,
                spec.fast_points,
                spec.basis_size,
            ),
            dtype=float,
        ),
    )


def _row_coefficients(
    state: PDEState, spec: PDESpec, quadrature: PDEQuadrature, ell: int
) -> Array:
    return (
        spec.sigma_w * quadrature.epsilon[None, :, :]
        + state.c[ell]
    )


def solve_fields(
    state: PDEState, spec: PDESpec, quadrature: PDEQuadrature
) -> Fields:
    """Solve the depth-forward/depth-adjoint equations at one training state."""

    N = spec.depth_nodes
    M = spec.base_points
    R = spec.fast_points
    m = spec.y.size
    P = spec.basis_size
    delta = 1.0 / N
    phi = quadrature.phi
    wb = quadrature.base_weights
    wf = quadrature.fast_weights

    h = np.empty((N + 1, M, m), dtype=float)
    z = np.empty((N, M, R, m), dtype=float)
    D = np.empty_like(z)
    hcoef = np.empty((N, P, m), dtype=float)
    h[0] = state.B @ spec.X
    for ell in range(N):
        hcoef[ell] = phi.T @ (wb[:, None] * h[ell])
        row = _row_coefficients(state, spec, quadrature, ell)
        z[ell] = np.einsum(
            "irp,pm->irm", row, hcoef[ell], optimize=True
        )
        tanh_z = np.tanh(z[ell])
        D[ell] = 1.0 - tanh_z * tanh_z
        h[ell + 1] = (
            h[ell]
            + spec.gamma
            * delta
            * np.einsum("r,irm->im", wf, tanh_z, optimize=True)
        )

    p = np.empty_like(h)
    beta = np.empty_like(z)
    p[N] = state.a[:, None]
    for ell in range(N - 1, -1, -1):
        beta[ell] = D[ell] * p[ell + 1, :, None, :]
        row = _row_coefficients(state, spec, quadrature, ell)
        transpose_coeff = np.einsum(
            "i,r,irp,irm->pm",
            wb,
            wf,
            row,
            beta[ell],
            optimize=True,
        )
        p[ell] = (
            p[ell + 1]
            + spec.gamma * delta * (phi @ transpose_coeff)
        )

    return Fields(h=h, p=p, z=z, D=D, beta=beta, hcoef=hcoef)


def vector_field(
    state: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    fields: Fields | None = None,
) -> tuple[PDEState, Fields]:
    """Projected standard Euclidean-muP characteristic velocity."""

    if fields is None:
        fields = solve_fields(state, spec, quadrature)
    f = np.einsum(
        "i,i,im->m",
        quadrature.base_weights,
        state.a,
        fields.h[-1],
        optimize=True,
    )
    e = f - spec.y

    Bdot = -((fields.p[0] * e[None, :]) @ spec.X.T)
    adot = -(fields.h[-1] @ e)
    cdot = -spec.gamma * np.einsum(
        "lirq,lpq,q->lirp",
        fields.beta,
        fields.hcoef,
        e,
        optimize=True,
    )
    return PDEState(B=Bdot, a=adot, c=cdot), fields


def _combine(
    state: PDEState,
    terms: tuple[tuple[float, PDEState], ...],
    scale: float,
) -> PDEState:
    return PDEState(
        B=state.B + scale * sum(w * v.B for w, v in terms),
        a=state.a + scale * sum(w * v.a for w, v in terms),
        c=state.c + scale * sum(w * v.c for w, v in terms),
    )


def rk4_step(
    state: PDEState,
    dt: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> PDEState:
    k1, _ = vector_field(state, spec, quadrature)
    k2, _ = vector_field(
        _combine(state, ((1.0, k1),), dt / 2.0), spec, quadrature
    )
    k3, _ = vector_field(
        _combine(state, ((1.0, k2),), dt / 2.0), spec, quadrature
    )
    k4, _ = vector_field(
        _combine(state, ((1.0, k3),), dt), spec, quadrature
    )
    return _combine(
        state,
        ((1.0, k1), (2.0, k2), (2.0, k3), (1.0, k4)),
        dt / 6.0,
    )


def heun_step(
    state: PDEState,
    dt: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> PDEState:
    """One explicit trapezoidal (Heun) step for method cross-checks."""

    k1, _ = vector_field(state, spec, quadrature)
    predictor = _combine(state, ((1.0, k1),), dt)
    k2, _ = vector_field(predictor, spec, quadrature)
    return _combine(state, ((1.0, k1), (1.0, k2)), dt / 2.0)


def observe(
    state: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    fields: Fields | None = None,
) -> Observable:
    if fields is None:
        fields = solve_fields(state, spec, quadrature)
    M = spec.base_points
    R = spec.fast_points
    N = spec.depth_nodes
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    f = np.einsum(
        "i,i,im->m", wb, state.a, fields.h[-1], optimize=True
    )
    e = f - spec.y
    grams = np.einsum(
        "i,lim,lin->lmn",
        wb,
        fields.h,
        fields.h,
        optimize=True,
    )
    gp0 = fields.p[0].T @ (wb[:, None] * fields.p[0])
    theta = grams[-1] + (spec.X.T @ spec.X) * gp0
    projected_energy = np.empty((N, spec.y.size), dtype=float)
    for ell in range(N):
        gh_projected = fields.hcoef[ell].T @ fields.hcoef[ell]
        gbeta = np.einsum(
            "i,r,irq,irs->qs",
            wb,
            wf,
            fields.beta[ell],
            fields.beta[ell],
            optimize=True,
        )
        theta += (
            spec.gamma**2 / N
        ) * gh_projected * gbeta
        full_diag = np.diag(grams[ell])
        projected_energy[ell] = np.divide(
            np.diag(gh_projected),
            full_diag,
            out=np.ones_like(full_diag),
            where=full_diag > 1e-15,
        )
    theta = 0.5 * (theta + theta.T)
    return Observable(
        f=f,
        loss=float(0.5 * e @ e),
        grams=grams,
        theta=theta,
        theta_min=float(np.linalg.eigvalsh(theta)[0]),
        residual_norm=float(np.linalg.norm(e)),
        loss_dot=float(-(e @ theta @ e)),
        projected_energy=projected_energy,
    )


def transpose_pairing_defect(
    state: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    ell: int,
    slow_u: Array,
    fast_v: Array,
) -> float:
    """Numerically verify <Wu,v> = <u,W*v> for one depth cell."""

    row = _row_coefficients(state, spec, quadrature, ell)
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    ucoef = quadrature.phi.T @ (wb * slow_u)
    Wu = np.einsum("irp,p->ir", row, ucoef, optimize=True)
    lhs = float(
        np.einsum("i,r,ir,ir->", wb, wf, Wu, fast_v, optimize=True)
    )
    transpose_coeff = np.einsum(
        "i,r,irp,ir->p", wb, wf, row, fast_v, optimize=True
    )
    Wtv = quadrature.phi @ transpose_coeff
    rhs = float(np.einsum("i,i,i->", wb, slow_u, Wtv, optimize=True))
    return abs(lhs - rhs)
