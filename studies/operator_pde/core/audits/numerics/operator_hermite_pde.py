"""Prototype isonormal/Hermite operator-Galerkin neural PDE.

This is an explicit width-independent surrogate for the iid-depth dense
Euclidean-muP ResNet.  It is *not* part of the existing reproducibility
bundle and does not establish convergence to the canonical dense limit.

For an immutable base-neuron latent g=(B(0)-row,a(0)/A), let phi_j(g) be a
fixed orthonormal Hermite basis.  A row of each dense operator is represented
on the retained column subspace by coefficients c_j:

    (W_P u)(g,c) = sum_j c_j <phi_j,u>,
    (W_P^T v)(g) = sum_j phi_j(g) E[c_j v(g,c)].

The same c is used in both orientations.  Projecting the ordinary Euclidean
gradient gives

    c_dot_j = -gamma sum_r e_r beta_r <phi_j,h_r>.

At continuous depth the fast row coefficients are averaged conditionally on
g.  Their conditional law obeys a finite Liouville equation, solved here by
nested positive cubature characteristics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

import numpy as np

from liouville_solvers import (
    normalized_hermite_matrix,
    scrambled_normal_sobol,
    tensor_normal_rule,
    total_degree_indices,
)

Array = np.ndarray


@dataclass(frozen=True)
class OperatorPDEConfig:
    X: Array
    y: Array
    depth: int = 16
    basis_degree: int = 1
    base_rule_order: int = 5
    row_rule_order: int = 3
    row_sobol_power: int | None = None
    row_seed: int = 1701
    row_moment_match: bool = True
    sigma_w: float = 0.65
    A: float = 1.0
    gamma: float = 1.0


@dataclass
class OperatorState:
    b: Array
    a: Array
    c: Array

    def copy(self) -> "OperatorState":
        return OperatorState(self.b.copy(), self.a.copy(), self.c.copy())


@dataclass
class OperatorWorkspace:
    base: Array
    base_weights: Array
    row_weights: Array
    phi: Array
    state: OperatorState


def initialize(config: OperatorPDEConfig) -> OperatorWorkspace:
    d, _m = config.X.shape
    latent_dim = d + 1
    base, base_weights = tensor_normal_rule(
        config.base_rule_order, latent_dim
    )
    indices = total_degree_indices(latent_dim, config.basis_degree)
    phi = normalized_hermite_matrix(base, indices)
    if config.row_sobol_power is None:
        row, row_weights = tensor_normal_rule(
            config.row_rule_order, len(indices)
        )
    else:
        row, row_weights = scrambled_normal_sobol(
            config.row_sobol_power, len(indices), config.row_seed
        )
        if config.row_moment_match:
            mean = row_weights @ row
            centered = row - mean
            covariance = (centered.T * row_weights[None, :]) @ centered
            eigval, eigvec = np.linalg.eigh(covariance)
            if eigval[0] <= 0:
                raise ValueError("Sobol covariance is not positive definite")
            inv_sqrt = (eigvec / np.sqrt(eigval)[None, :]) @ eigvec.T
            row = centered @ inv_sqrt
    mx, me, rank = base.shape[0], row.shape[0], len(indices)
    b = base[:, :d].copy()
    a = config.A * base[:, d].copy()
    c = np.broadcast_to(
        config.sigma_w * row[None, None, :, :],
        (config.depth, mx, me, rank),
    ).copy()
    return OperatorWorkspace(
        base=base,
        base_weights=base_weights,
        row_weights=row_weights,
        phi=phi,
        state=OperatorState(b=b, a=a, c=c),
    )


def solve_depth_bvp(
    state: OperatorState,
    config: OperatorPDEConfig,
    workspace: OperatorWorkspace,
) -> tuple[Array, Array, Array, Array, Array]:
    """Return h, p, coefficient moments H, z, and beta."""

    L = config.depth
    delta = 1.0 / L
    mx = workspace.base.shape[0]
    m = config.y.size
    h = np.empty((L + 1, mx, m), dtype=float)
    H = np.empty((L, m, workspace.phi.shape[1]), dtype=float)
    z = np.empty(
        (L, mx, workspace.row_weights.size, m), dtype=float
    )
    tanh_z = np.empty_like(z)
    h[0] = state.b @ config.X
    for ell in range(L):
        H[ell] = np.einsum(
            "x,xj,xr->rj",
            workspace.base_weights,
            workspace.phi,
            h[ell],
            optimize=True,
        )
        z[ell] = np.einsum(
            "xej,rj->xer", state.c[ell], H[ell], optimize=True
        )
        tanh_z[ell] = np.tanh(z[ell])
        mean_tanh = np.einsum(
            "e,xer->xr",
            workspace.row_weights,
            tanh_z[ell],
            optimize=True,
        )
        h[ell + 1] = h[ell] + config.gamma * delta * mean_tanh

    p = np.empty_like(h)
    beta = np.empty_like(z)
    p[L] = state.a[:, None]
    for ell in range(L - 1, -1, -1):
        deriv = 1.0 - tanh_z[ell] ** 2
        beta[ell] = deriv * p[ell + 1, :, None, :]
        column_moment = np.einsum(
            "x,e,xej,xer->rj",
            workspace.base_weights,
            workspace.row_weights,
            state.c[ell],
            beta[ell],
            optimize=True,
        )
        transpose_action = np.einsum(
            "xj,rj->xr", workspace.phi, column_moment, optimize=True
        )
        p[ell] = p[ell + 1] + (
            config.gamma * delta * transpose_action
        )
    return h, p, H, z, beta


def vector_field(
    state: OperatorState,
    config: OperatorPDEConfig,
    workspace: OperatorWorkspace,
) -> tuple[OperatorState, dict[str, Array | float]]:
    h, p, H, _z, beta = solve_depth_bvp(state, config, workspace)
    f = np.einsum(
        "x,x,xr->r",
        workspace.base_weights,
        state.a,
        h[-1],
        optimize=True,
    )
    e = f - config.y
    adot = -(h[-1] @ e)
    bdot = -np.einsum(
        "xr,r,dr->xd", p[0], e, config.X, optimize=True
    )
    cdot = -config.gamma * np.einsum(
        "lxer,r,lrj->lxej", beta, e, H, optimize=True
    )
    grams = np.einsum(
        "x,lxr,lxq->lrq",
        workspace.base_weights,
        h,
        h,
        optimize=True,
    )
    theta = np.einsum(
        "x,xr,xq->rq",
        workspace.base_weights,
        h[-1],
        h[-1],
        optimize=True,
    )
    gp0 = np.einsum(
        "x,xr,xq->rq",
        workspace.base_weights,
        p[0],
        p[0],
        optimize=True,
    )
    theta += (config.X.T @ config.X) * gp0
    for ell in range(config.depth):
        projected_h_gram = H[ell] @ H[ell].T
        beta_gram = np.einsum(
            "x,e,xer,xeq->rq",
            workspace.base_weights,
            workspace.row_weights,
            beta[ell],
            beta[ell],
            optimize=True,
        )
        theta += (
            (config.gamma**2 / config.depth)
            * projected_h_gram
            * beta_gram
        )
    theta = 0.5 * (theta + theta.T)
    obs: dict[str, Array | float] = {
        "f": f,
        "loss": float(0.5 * e @ e),
        "grams": grams,
        "theta": theta,
        "predicted_f_dot": -(theta @ e),
    }
    return OperatorState(bdot, adot, cdot), obs


def _combine(
    state: OperatorState, deriv: OperatorState, scale: float
) -> OperatorState:
    return OperatorState(
        state.b + scale * deriv.b,
        state.a + scale * deriv.a,
        state.c + scale * deriv.c,
    )


def rk4_step(
    state: OperatorState,
    dt: float,
    config: OperatorPDEConfig,
    workspace: OperatorWorkspace,
) -> OperatorState:
    k1, _ = vector_field(state, config, workspace)
    k2, _ = vector_field(_combine(state, k1, 0.5 * dt), config, workspace)
    k3, _ = vector_field(_combine(state, k2, 0.5 * dt), config, workspace)
    k4, _ = vector_field(_combine(state, k3, dt), config, workspace)
    return OperatorState(
        state.b + (dt / 6.0) * (k1.b + 2 * k2.b + 2 * k3.b + k4.b),
        state.a + (dt / 6.0) * (k1.a + 2 * k2.a + 2 * k3.a + k4.a),
        state.c + (dt / 6.0) * (k1.c + 2 * k2.c + 2 * k3.c + k4.c),
    )


def run(
    config: OperatorPDEConfig,
    duration: float,
    dt: float,
    sample_dt: float,
) -> dict[str, Array]:
    workspace = initialize(config)
    state = workspace.state
    steps = int(round(duration / dt))
    stride = int(round(sample_dt / dt))
    times: list[float] = []
    outputs: list[Array] = []
    losses: list[float] = []
    grams: list[Array] = []
    for step in range(steps + 1):
        if step % stride == 0:
            _, obs = vector_field(state, config, workspace)
            times.append(step * dt)
            outputs.append(np.asarray(obs["f"]))
            losses.append(float(obs["loss"]))
            grams.append(np.asarray(obs["grams"]))
        if step < steps:
            state = rk4_step(state, dt, config, workspace)
    return {
        "time": np.asarray(times),
        "f": np.asarray(outputs),
        "loss": np.asarray(losses),
        "grams": np.asarray(grams),
    }


if __name__ == "__main__":
    X = np.eye(2)
    y = np.asarray([0.8, -0.55])
    cfg = OperatorPDEConfig(X=X, y=y)
    rank = comb(X.shape[0] + 1 + cfg.basis_degree, cfg.basis_degree)
    print(
        {
            "operator_rank": rank,
            "base_nodes": cfg.base_rule_order ** (X.shape[0] + 1),
            "row_nodes_per_base": cfg.row_rule_order**rank,
        }
    )
    trace = run(cfg, duration=0.2, dt=0.02, sample_dt=0.02)
    print(
        {
            "initial_loss": float(trace["loss"][0]),
            "final_loss": float(trace["loss"][-1]),
            "terminal_gram_motion": float(
                np.max(
                    np.linalg.norm(
                        trace["grams"] - trace["grams"][0],
                        axis=(-2, -1),
                    )
                )
            ),
        }
    )
