"""Canonical finite dense residual network used only as a reference.

For ``L=depth`` the network and ordinary Euclidean muP gradient flow are

    H[0]     = B X
    H[l + 1] = H[l] + (gamma / L) sigma(W[l] H[l])
    f        = a.T H[L] / n

    B_t      = -sum_r e_r p_r(0) x_r.T
    W_t[l]   = -(gamma / n) sum_r e_r beta_r(l) h_r(l).T
    a_t      = -sum_r e_r h_r(1).

Equivalently, these are Euclidean learning-rate multipliers
``eta_B=eta_a=n`` and ``eta_W=L`` relative to the raw loss gradients.
Nothing in this module is called by the PDE vector field.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from activations import get_activation

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
    activation: str = "tanh"

    def validate(self) -> None:
        if self.n < 1 or self.depth < 1:
            raise ValueError("n and depth must be positive")
        if self.X.ndim != 2 or self.y.ndim != 1:
            raise ValueError("X must be d x m and y must be length m")
        if self.X.shape[1] != self.y.size:
            raise ValueError("X and y disagree on sample count")
        if min(self.sigma_w, self.A, self.gamma) <= 0:
            raise ValueError("sigma_w, A, and gamma must be positive")
        get_activation(self.activation)


@dataclass
class ParamState:
    B: Array
    W: Array
    a: Array


@dataclass
class FieldState:
    W: Array
    a: Array
    H: Array
    P: Array


@dataclass
class ForwardAdjoint:
    H: Array
    P: Array
    Z: Array
    T: Array
    D: Array


def initialize(spec: ModelSpec) -> ParamState:
    """Draw the exact finite model in a fixed, documented RNG order."""

    spec.validate()
    rng = np.random.default_rng(spec.seed)
    B = rng.normal(size=(spec.n, spec.X.shape[0]))
    W = rng.normal(
        scale=spec.sigma_w / np.sqrt(spec.n),
        size=(spec.depth, spec.n, spec.n),
    )
    a = rng.normal(scale=spec.A, size=spec.n)
    return ParamState(B=B, W=W, a=a)


def forward_adjoint(state: ParamState, spec: ModelSpec) -> ForwardAdjoint:
    """Solve the discrete residual forward and unit-output adjoint equations."""

    activation = get_activation(spec.activation)
    delta = 1.0 / spec.depth
    H = np.empty(
        (spec.depth + 1, spec.n, spec.y.size),
        dtype=float,
    )
    Z = np.empty((spec.depth, spec.n, spec.y.size), dtype=float)
    T = np.empty_like(Z)
    D = np.empty_like(Z)
    H[0] = state.B @ spec.X
    for ell in range(spec.depth):
        Z[ell] = state.W[ell] @ H[ell]
        T[ell] = activation.value(Z[ell])
        D[ell] = activation.derivative(Z[ell])
        H[ell + 1] = H[ell] + spec.gamma * delta * T[ell]

    P = np.empty_like(H)
    P[-1] = state.a[:, None]
    for ell in range(spec.depth - 1, -1, -1):
        P[ell] = P[ell + 1] + spec.gamma * delta * (
            state.W[ell].T @ (D[ell] * P[ell + 1])
        )
    return ForwardAdjoint(H=H, P=P, Z=Z, T=T, D=D)


def parameter_vector_field(state: ParamState, spec: ModelSpec) -> ParamState:
    """Ordinary Euclidean muP gradient-flow velocity."""

    fields = forward_adjoint(state, spec)
    residual = state.a @ fields.H[-1] / spec.n - spec.y
    adot = -(fields.H[-1] @ residual)
    Bdot = -((fields.P[0] * residual[None, :]) @ spec.X.T)
    Wdot = np.empty_like(state.W)
    for ell in range(spec.depth):
        beta = fields.D[ell] * fields.P[ell + 1]
        Wdot[ell] = -spec.gamma * (
            (beta * residual[None, :]) @ fields.H[ell].T
        ) / spec.n
    return ParamState(B=Bdot, W=Wdot, a=adot)


def _shift(
    state: ParamState,
    terms: tuple[tuple[float, ParamState], ...],
    scale: float,
) -> ParamState:
    return ParamState(
        B=state.B + scale * sum(weight * term.B for weight, term in terms),
        W=state.W + scale * sum(weight * term.W for weight, term in terms),
        a=state.a + scale * sum(weight * term.a for weight, term in terms),
    )


def rk4_param_step(state: ParamState, dt: float, spec: ModelSpec) -> ParamState:
    """One classical RK4 step of the exact finite gradient flow."""

    k1 = parameter_vector_field(state, spec)
    k2 = parameter_vector_field(_shift(state, ((1.0, k1),), dt / 2.0), spec)
    k3 = parameter_vector_field(_shift(state, ((1.0, k2),), dt / 2.0), spec)
    k4 = parameter_vector_field(_shift(state, ((1.0, k3),), dt), spec)
    return _shift(
        state,
        ((1.0, k1), (2.0, k2), (2.0, k3), (1.0, k4)),
        dt / 6.0,
    )


def tangent_kernel(state: FieldState, spec: ModelSpec) -> Array:
    """Exact finite-network muP tangent kernel on the fixed dataset."""

    activation = get_activation(spec.activation)
    Qx = spec.X.T @ spec.X
    theta = state.H[-1].T @ state.H[-1] / spec.n
    theta = theta + Qx * (state.P[0].T @ state.P[0] / spec.n)
    for ell in range(spec.depth):
        z = state.W[ell] @ state.H[ell]
        D = activation.derivative(z)
        beta = D * state.P[ell + 1]
        Gh = state.H[ell].T @ state.H[ell] / spec.n
        Gb = beta.T @ beta / spec.n
        theta = theta + (spec.gamma**2 / spec.depth) * (Gh * Gb)
    return 0.5 * (theta + theta.T)
