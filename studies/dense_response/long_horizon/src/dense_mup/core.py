"""Dense Euclidean-muP residual network and q/r response projection.

The exact finite network is

    H[0] = B X
    H[l+1] = H[l] + (gamma / L) tanh(W[l] H[l])
    f = a^T H[L] / n

with Euclidean gradient-flow multipliers eta_W=L and eta_B=eta_a=n.

The projected FieldState evolves W, a, H, and P as independent fields.
Its H_t and P_t velocities are the coupled grade-K chronological q/r
response truncations.  It deliberately retains every dense W matrix; it is
therefore a finite-matrix response surrogate, not the width-independent
Liouville PDE conjectured in the accompanying theory note.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, TypeVar

import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class ModelSpec:
    n: int
    depth: int
    X: Array
    y: Array
    seed: int
    sigma_w: float = 0.65
    A: float = 1.0
    gamma: float = 1.0

    def validate(self) -> None:
        if self.n < 1 or self.depth < 1:
            raise ValueError("n and depth must be positive")
        if self.X.ndim != 2 or self.y.ndim != 1:
            raise ValueError("X must be d x m and y must be length m")
        if self.X.shape[1] != self.y.size:
            raise ValueError("X and y disagree on sample count")
        if self.sigma_w <= 0 or self.A <= 0 or self.gamma <= 0:
            raise ValueError("sigma_w, A, and gamma must be positive")


@dataclass
class ParamState:
    B: Array
    W: Array
    a: Array

    def copy(self) -> "ParamState":
        return ParamState(self.B.copy(), self.W.copy(), self.a.copy())


@dataclass
class FieldState:
    W: Array
    a: Array
    H: Array
    P: Array

    def copy(self) -> "FieldState":
        return FieldState(
            self.W.copy(), self.a.copy(), self.H.copy(), self.P.copy()
        )


@dataclass
class ForwardAdjoint:
    H: Array
    P: Array
    Z: Array
    T: Array
    D: Array


@dataclass
class ObservableSnapshot:
    f: Array
    loss: float
    grams: Array
    f_dot: Array
    loss_dot: float
    gram_dot: Array
    theta: Array
    theta_min: float
    kernel_identity_defect: float
    residual_norm: float
    output_speed: float
    gram_speed: float
    forward_defect: float
    adjoint_defect: float
    terminal_defect: float


def initialize(spec: ModelSpec) -> ParamState:
    """Match the initialization order used by the corrected original audit."""

    spec.validate()
    rng = np.random.default_rng(spec.seed)
    d = spec.X.shape[0]
    B = rng.normal(size=(spec.n, d))
    W = rng.normal(
        scale=spec.sigma_w / np.sqrt(spec.n),
        size=(spec.depth, spec.n, spec.n),
    )
    a = rng.normal(scale=spec.A, size=spec.n)
    return ParamState(B=B, W=W, a=a)


def forward_adjoint(state: ParamState, spec: ModelSpec) -> ForwardAdjoint:
    L = spec.depth
    delta = 1.0 / L
    n, m = spec.n, spec.y.size
    H = np.empty((L + 1, n, m), dtype=float)
    Z = np.empty((L, n, m), dtype=float)
    T = np.empty_like(Z)
    D = np.empty_like(Z)
    H[0] = state.B @ spec.X
    for ell in range(L):
        Z[ell] = state.W[ell] @ H[ell]
        T[ell] = np.tanh(Z[ell])
        D[ell] = 1.0 - T[ell] * T[ell]
        H[ell + 1] = H[ell] + spec.gamma * delta * T[ell]

    P = np.empty_like(H)
    P[L] = state.a[:, None]
    for ell in range(L - 1, -1, -1):
        P[ell] = P[ell + 1] + spec.gamma * delta * (
            state.W[ell].T @ (D[ell] * P[ell + 1])
        )
    return ForwardAdjoint(H=H, P=P, Z=Z, T=T, D=D)


def fields_from_params(state: ParamState, spec: ModelSpec) -> FieldState:
    fa = forward_adjoint(state, spec)
    return FieldState(
        W=state.W.copy(),
        a=state.a.copy(),
        H=fa.H.copy(),
        P=fa.P.copy(),
    )


def parameter_vector_field(state: ParamState, spec: ModelSpec) -> ParamState:
    fa = forward_adjoint(state, spec)
    f = state.a @ fa.H[-1] / spec.n
    e = f - spec.y
    adot = -(fa.H[-1] @ e)
    Bdot = -((fa.P[0] * e[None, :]) @ spec.X.T)
    Wdot = np.empty_like(state.W)
    for ell in range(spec.depth):
        beta = fa.D[ell] * fa.P[ell + 1]
        Wdot[ell] = -spec.gamma * (
            (beta * e[None, :]) @ fa.H[ell].T
        ) / spec.n
    return ParamState(B=Bdot, W=Wdot, a=adot)


def exact_training_derivatives(
    state: ParamState, spec: ModelSpec
) -> tuple[Array, Array, ParamState, ForwardAdjoint]:
    """Differentiate the exact forward and backward depth recurrences."""

    L = spec.depth
    delta = 1.0 / L
    pdot = parameter_vector_field(state, spec)
    fa = forward_adjoint(state, spec)

    Hdot = np.empty_like(fa.H)
    Zdot = np.empty_like(fa.Z)
    Ddot = np.empty_like(fa.D)
    Hdot[0] = pdot.B @ spec.X
    for ell in range(L):
        Zdot[ell] = (
            pdot.W[ell] @ fa.H[ell] + state.W[ell] @ Hdot[ell]
        )
        Ddot[ell] = -2.0 * fa.T[ell] * fa.D[ell] * Zdot[ell]
        Hdot[ell + 1] = Hdot[ell] + spec.gamma * delta * (
            fa.D[ell] * Zdot[ell]
        )

    Pdot = np.empty_like(fa.P)
    Pdot[L] = pdot.a[:, None]
    for ell in range(L - 1, -1, -1):
        beta = fa.D[ell] * fa.P[ell + 1]
        Pdot[ell] = Pdot[ell + 1] + spec.gamma * delta * (
            pdot.W[ell].T @ beta
            + state.W[ell].T
            @ (
                Ddot[ell] * fa.P[ell + 1]
                + fa.D[ell] * Pdot[ell + 1]
            )
        )
    return Hdot, Pdot, pdot, fa


def field_vector_field(
    state: FieldState, spec: ModelSpec, order: int
) -> FieldState:
    """Coupled grade-K q/r projected hierarchy vector field."""

    if order < 0:
        raise ValueError("response order must be nonnegative")
    L = spec.depth
    delta = 1.0 / L
    n, m = spec.n, spec.y.size
    Qx = spec.X.T @ spec.X

    Z = np.empty((L, n, m), dtype=float)
    T = np.empty_like(Z)
    D = np.empty_like(Z)
    for ell in range(L):
        Z[ell] = state.W[ell] @ state.H[ell]
        T[ell] = np.tanh(Z[ell])
        D[ell] = 1.0 - T[ell] * T[ell]

    f = state.a @ state.H[-1] / n
    e = f - spec.y
    adot = -(state.H[-1] @ e)
    Wdot = np.empty_like(state.W)
    for ell in range(L):
        beta = D[ell] * state.P[ell + 1]
        Wdot[ell] = -spec.gamma * (
            (beta * e[None, :]) @ state.H[ell].T
        ) / n

    # q[k,ell,:,r] is the grade-k forward training response.
    q = np.zeros((order + 1, L + 1, n, m), dtype=float)
    q[0, 0] = -((state.P[0] * e[None, :]) @ Qx)
    for ell in range(L):
        beta = D[ell] * state.P[ell + 1]
        Gh = state.H[ell].T @ state.H[ell] / n
        forcing = -(spec.gamma**2) * D[ell] * (
            (beta * e[None, :]) @ Gh
        )
        q[0, ell + 1] = q[0, ell] + delta * forcing
        for k in range(1, order + 1):
            propagated = spec.gamma * D[ell] * (
                state.W[ell] @ q[k - 1, ell]
            )
            q[k, ell + 1] = q[k, ell] + delta * propagated
    Hdot = np.sum(q, axis=0)

    # The coupled r source consistently uses the projected Hdot.
    Ddot = np.empty_like(D)
    source_t = np.empty_like(D)
    for ell in range(L):
        Zdot = Wdot[ell] @ state.H[ell] + state.W[ell] @ Hdot[ell]
        Ddot[ell] = -2.0 * T[ell] * D[ell] * Zdot
        source_t[ell] = spec.gamma * (
            Wdot[ell].T @ (D[ell] * state.P[ell + 1])
            + state.W[ell].T @ (Ddot[ell] * state.P[ell + 1])
        )

    # r[k,ell,:,r] is the grade-k backward training response.
    r = np.zeros((order + 1, L + 1, n, m), dtype=float)
    r[0, L] = adot[:, None]
    for ell in range(L - 1, -1, -1):
        r[0, ell] = r[0, ell + 1] + delta * source_t[ell]
        for k in range(1, order + 1):
            propagated = spec.gamma * state.W[ell].T @ (
                D[ell] * r[k - 1, ell + 1]
            )
            r[k, ell] = r[k, ell + 1] + delta * propagated
    Pdot = np.sum(r, axis=0)
    return FieldState(W=Wdot, a=adot, H=Hdot, P=Pdot)


StateT = TypeVar("StateT", ParamState, FieldState)


def _combine_param(
    state: ParamState,
    terms: tuple[tuple[float, ParamState], ...],
    scale: float,
) -> ParamState:
    return ParamState(
        B=state.B
        + scale * sum(weight * term.B for weight, term in terms),
        W=state.W
        + scale * sum(weight * term.W for weight, term in terms),
        a=state.a
        + scale * sum(weight * term.a for weight, term in terms),
    )


def _combine_field(
    state: FieldState,
    terms: tuple[tuple[float, FieldState], ...],
    scale: float,
) -> FieldState:
    return FieldState(
        W=state.W
        + scale * sum(weight * term.W for weight, term in terms),
        a=state.a
        + scale * sum(weight * term.a for weight, term in terms),
        H=state.H
        + scale * sum(weight * term.H for weight, term in terms),
        P=state.P
        + scale * sum(weight * term.P for weight, term in terms),
    )


def rk4_param_step(
    state: ParamState, dt: float, spec: ModelSpec
) -> ParamState:
    k1 = parameter_vector_field(state, spec)
    k2 = parameter_vector_field(
        _combine_param(state, ((1.0, k1),), dt / 2.0), spec
    )
    k3 = parameter_vector_field(
        _combine_param(state, ((1.0, k2),), dt / 2.0), spec
    )
    k4 = parameter_vector_field(
        _combine_param(state, ((1.0, k3),), dt), spec
    )
    return _combine_param(
        state,
        ((1.0, k1), (2.0, k2), (2.0, k3), (1.0, k4)),
        dt / 6.0,
    )


def rk4_field_step(
    state: FieldState, dt: float, spec: ModelSpec, order: int
) -> FieldState:
    vf: Callable[[FieldState], FieldState] = lambda s: field_vector_field(
        s, spec, order
    )
    k1 = vf(state)
    k2 = vf(_combine_field(state, ((1.0, k1),), dt / 2.0))
    k3 = vf(_combine_field(state, ((1.0, k2),), dt / 2.0))
    k4 = vf(_combine_field(state, ((1.0, k3),), dt))
    return _combine_field(
        state,
        ((1.0, k1), (2.0, k2), (2.0, k3), (1.0, k4)),
        dt / 6.0,
    )


def tangent_kernel(state: FieldState, spec: ModelSpec) -> Array:
    L = spec.depth
    n = spec.n
    Qx = spec.X.T @ spec.X
    theta = state.H[-1].T @ state.H[-1] / n
    theta = theta + Qx * (state.P[0].T @ state.P[0] / n)
    for ell in range(L):
        z = state.W[ell] @ state.H[ell]
        D = 1.0 - np.tanh(z) ** 2
        beta = D * state.P[ell + 1]
        Gh = state.H[ell].T @ state.H[ell] / n
        Gb = beta.T @ beta / n
        theta = theta + (spec.gamma**2 / L) * (Gh * Gb)
    return 0.5 * (theta + theta.T)


def manifold_defects(state: FieldState, spec: ModelSpec) -> tuple[float, float, float]:
    """Normalized defects in forward, adjoint, and terminal constraints."""

    L = spec.depth
    delta = 1.0 / L
    h_scale = max(float(np.linalg.norm(state.H)), 1e-15)
    p_scale = max(float(np.linalg.norm(state.P)), 1e-15)
    fwd_sq = 0.0
    adj_sq = 0.0
    for ell in range(L):
        z = state.W[ell] @ state.H[ell]
        T = np.tanh(z)
        D = 1.0 - T * T
        fwd = (
            state.H[ell + 1]
            - state.H[ell]
            - spec.gamma * delta * T
        )
        adj = (
            state.P[ell]
            - state.P[ell + 1]
            - spec.gamma
            * delta
            * (state.W[ell].T @ (D * state.P[ell + 1]))
        )
        fwd_sq += float(np.sum(fwd * fwd))
        adj_sq += float(np.sum(adj * adj))
    terminal = state.P[-1] - state.a[:, None]
    return (
        float(np.sqrt(fwd_sq) / h_scale),
        float(np.sqrt(adj_sq) / p_scale),
        float(np.linalg.norm(terminal) / p_scale),
    )


def snapshot_from_field(
    state: FieldState, deriv: FieldState, spec: ModelSpec
) -> ObservableSnapshot:
    n = spec.n
    f = state.a @ state.H[-1] / n
    e = f - spec.y
    f_dot = (
        deriv.a @ state.H[-1] + state.a @ deriv.H[-1]
    ) / n
    grams = np.einsum("lnr,lnq->lrq", state.H, state.H) / n
    gram_dot = (
        np.einsum("lnr,lnq->lrq", deriv.H, state.H)
        + np.einsum("lnr,lnq->lrq", state.H, deriv.H)
    ) / n
    theta = tangent_kernel(state, spec)
    theta_e = theta @ e
    fwd_def, adj_def, terminal_def = manifold_defects(state, spec)
    return ObservableSnapshot(
        f=f,
        loss=float(0.5 * e @ e),
        grams=grams,
        f_dot=f_dot,
        loss_dot=float(e @ f_dot),
        gram_dot=gram_dot,
        theta=theta,
        theta_min=float(np.linalg.eigvalsh(theta)[0]),
        kernel_identity_defect=float(np.linalg.norm(f_dot + theta_e)),
        residual_norm=float(np.linalg.norm(e)),
        output_speed=float(np.linalg.norm(f_dot)),
        gram_speed=float(
            np.max(np.linalg.norm(gram_dot, axis=(-2, -1)))
        ),
        forward_defect=fwd_def,
        adjoint_defect=adj_def,
        terminal_defect=terminal_def,
    )


def snapshot_from_params(
    state: ParamState, spec: ModelSpec
) -> tuple[ObservableSnapshot, Array, Array]:
    Hdot, Pdot, pdot, fa = exact_training_derivatives(state, spec)
    field = FieldState(state.W, state.a, fa.H, fa.P)
    deriv = FieldState(pdot.W, pdot.a, Hdot, Pdot)
    return snapshot_from_field(field, deriv, spec), Hdot, Pdot


def normalized_error(x: Array, y: Array, floor: float = 1e-14) -> float:
    return float(np.linalg.norm(x - y) / max(np.linalg.norm(y), floor))


def rms_error(x: Array, y: Array) -> float:
    return float(np.sqrt(np.mean((x - y) ** 2)))
