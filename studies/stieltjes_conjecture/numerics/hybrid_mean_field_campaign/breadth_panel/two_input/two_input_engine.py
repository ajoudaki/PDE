#!/usr/bin/env python3
"""Auditable two-input squared-loss field for the breadth panel.

This module is deliberately an engine, not a campaign runner.  It implements
the physical two-sample problem whose formal mean-field symmetry channels
were computed in MFP Campaign 2.

For labels ``(1, sigma)`` and average squared loss

    L = ((1-f_1)^2 + (sigma-f_2)^2) / 2,

the scaled gradient flow is

    parameter_dot = -n grad(L) = n sum_alpha r_alpha grad(f_alpha).

The input Gram matrix enters twice: it is the covariance of the two
first-hidden preactivations at initialization and the fixed pullback metric
for their gradients throughout training.  Both occurrences are required for
the simulation to represent an actual two-input network.
"""

from __future__ import annotations

import hashlib
import math
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch


HERE = Path(__file__).resolve().parent
EULER_DIR = HERE.parents[1] / "width_ladder" / "euler_fp32"
if str(EULER_DIR) not in sys.path:
    sys.path.insert(0, str(EULER_DIR))

import nested_init as audited_init  # noqa: E402


CORE_T = 0.5
CORE_THETA = math.sqrt(CORE_T)
SECOND_INPUT_COUNTER_OFFSET = audited_init.ROW_BASE


@dataclass(frozen=True)
class Configuration:
    key: str
    theta: float
    sigma: int

    def __post_init__(self) -> None:
        if not math.isfinite(self.theta) or abs(self.theta) > 1.0:
            raise ValueError("theta must be finite and lie in [-1,1]")
        if self.sigma not in (-1, 1):
            raise ValueError("sigma must be +1 or -1")

    @property
    def t(self) -> float:
        return self.theta * self.theta

    @property
    def labels(self) -> tuple[float, float]:
        return (1.0, float(self.sigma))


CORE_EQUAL = Configuration("two_input_equal_t_half", CORE_THETA, 1)
CORE_OPPOSITE = Configuration("two_input_opposite_t_half", CORE_THETA, -1)
CORE_CONFIGURATIONS = (CORE_EQUAL, CORE_OPPOSITE)


@dataclass
class State:
    """Finite-width states.

    Shapes are ``a: (R,n)``, ``W: (R,n,n)``, and ``u: (R,2,n)``.  The two
    entries of ``u`` are preactivations of the same first-layer neurons on
    the two inputs, not two independent parameter blocks.
    """

    a: torch.Tensor
    W: torch.Tensor
    u: torch.Tensor

    @property
    def width(self) -> int:
        return int(self.a.shape[1])


@dataclass
class Tangent:
    """Exact ``-n grad(L)`` tangent in reduced coordinates."""

    a: torch.Tensor
    W: torch.Tensor
    u: torch.Tensor
    w_derivative_l2: torch.Tensor
    w_state_inner_derivative: torch.Tensor


@dataclass
class Observables:
    """Raw outputs, the full NTK, and label/transverse channel readouts."""

    output: torch.Tensor
    residual: torch.Tensor
    g: torch.Tensor
    delta: torch.Tensor
    kernel_matrix: torch.Tensor
    kernel_a_matrix: torch.Tensor
    kernel_W_matrix: torch.Tensor
    kernel_u_matrix: torch.Tensor
    kernel_g: torch.Tensor
    kernel_delta: torch.Tensor
    cross_kernel: torch.Tensor
    kernel_g_a: torch.Tensor
    kernel_g_W: torch.Tensor
    kernel_g_u: torch.Tensor
    kernel_delta_a: torch.Tensor
    kernel_delta_W: torch.Tensor
    kernel_delta_u: torch.Tensor
    cross_kernel_a: torch.Tensor
    cross_kernel_W: torch.Tensor
    cross_kernel_u: torch.Tensor
    effective_numerator: torch.Tensor
    transverse_numerator: torch.Tensor
    loss_full: torch.Tensor
    loss_projected: torch.Tensor
    q1: torch.Tensor
    q2: torch.Tensor

    @property
    def Kg(self) -> torch.Tensor:
        """Alias matching the notation in the two-input MFP report."""

        return self.kernel_g

    @property
    def Kdelta(self) -> torch.Tensor:
        return self.kernel_delta

    @property
    def C(self) -> torch.Tensor:
        return self.cross_kernel

    @property
    def C_a(self) -> torch.Tensor:
        return self.cross_kernel_a

    @property
    def C_W(self) -> torch.Tensor:
        return self.cross_kernel_W

    @property
    def C_u(self) -> torch.Tensor:
        return self.cross_kernel_u


def input_gram(
    configuration: Configuration,
    *,
    dtype: torch.dtype,
    device: torch.device,
) -> torch.Tensor:
    theta = configuration.theta
    return torch.tensor(
        ((1.0, theta), (theta, 1.0)), dtype=dtype, device=device
    )


def _state_digest(
    seed: int,
    lineage: int,
    width: int,
    configuration: Configuration,
    a: np.ndarray,
    u: np.ndarray,
    W: np.ndarray,
) -> str:
    digest = hashlib.sha256()
    digest.update(b"breadth-panel-two-input-physical-state-v1\0")
    digest.update(struct.pack("<QQQd", seed, lineage, width, configuration.theta))
    digest.update(struct.pack("<b", configuration.sigma))
    for label, array in ((b"a", a), (b"u", u), (b"W", W)):
        digest.update(label + b"\0")
        digest.update(
            np.asarray(array, dtype="<f4", order="C").tobytes(order="C")
        )
    return digest.hexdigest()


def build_antithetic_state(
    configuration: Configuration,
    width: int,
    *,
    seed: int,
    lineage: int,
    device: torch.device,
    row_block: int = 128,
    prefix_sizes: tuple[int, ...] = (),
) -> tuple[State, dict[str, Any]]:
    """Build a nested FP32 antithetic pair with covariance ``Q(theta)``.

    The first Gaussian coordinate is exactly the audited one-input ``u``
    stream.  A disjoint counter interval in that same domain supplies the
    second independent coordinate, so no shape-dependent RNG consumption is
    introduced.  The correlated second preactivation is rounded to FP32 only
    after the linear combination.
    """

    a_np, u1_np, W_np, base_digest, base_prefixes = audited_init.generate_lineage(
        width,
        seed=seed,
        lineage=lineage,
        row_block=row_block,
        prefix_sizes=prefix_sizes,
    )
    counters = SECOND_INPUT_COUNTER_OFFSET + np.arange(width, dtype=np.uint64)
    independent = audited_init.normal(
        counters, seed=seed, lineage=lineage, domain="u"
    )
    orthogonal_scale = math.sqrt(max(0.0, 1.0 - configuration.theta**2))
    u2_np = (
        configuration.theta * u1_np.astype(np.float64)
        + orthogonal_scale * independent
    ).astype(np.float32)
    u_np = np.stack((u1_np, u2_np), axis=0)
    physical_digest = _state_digest(
        seed, lineage, width, configuration, a_np, u_np, W_np
    )
    physical_prefixes = {
        size: _state_digest(
            seed,
            lineage,
            size,
            configuration,
            a_np[:size],
            u_np[:, :size],
            W_np[:size, :size],
        )
        for size in prefix_sizes
    }

    a0 = torch.from_numpy(a_np).to(device=device)
    W0 = torch.from_numpy(W_np).to(device=device)
    u0 = torch.from_numpy(u_np).to(device=device)
    state = State(
        a=torch.stack((a0, -a0), dim=0),
        W=torch.stack((W0, W0), dim=0),
        u=torch.stack((u0, u0), dim=0),
    )
    return state, {
        "configuration": configuration.key,
        "theta": configuration.theta,
        "t": configuration.t,
        "sigma": configuration.sigma,
        "labels": list(configuration.labels),
        "base_one_input_state_sha256": base_digest,
        "base_one_input_prefix_sha256": dict(base_prefixes),
        "physical_state_sha256": physical_digest,
        "physical_prefix_sha256": physical_prefixes,
        "second_input_counter_offset": SECOND_INPUT_COUNTER_OFFSET,
    }


def finite_width_initial_kernel_means(
    configuration: Configuration, width: int
) -> dict[str, float]:
    """Exact Gaussian means for the two frozen ``t=1/2`` controls.

    These are physical channel kernels, including the finite-width Wick
    correction.  They are used only as initialization control variates and
    regression gates; they do not replace any positive-time observation.
    """

    if width <= 0:
        raise ValueError("width must be positive")
    if not math.isclose(configuration.t, CORE_T, rel_tol=0.0, abs_tol=1e-14):
        raise ValueError("finite-width controls are frozen only at t=1/2")
    inverse_width = 1.0 / width
    if configuration.sigma == 1:
        kernel_a = 22.0 + 212.0 * inverse_width
        kernel_W = 26.0 + 286.0 * inverse_width
        kernel_u = 32.0 + 472.0 * inverse_width
    else:
        kernel_a = 5.0 + 76.0 * inverse_width
        kernel_W = 10.0 + 98.0 * inverse_width
        kernel_u = 16.0 + 200.0 * inverse_width
    return {
        "kernel_a": kernel_a,
        "kernel_W": kernel_W,
        "kernel_u": kernel_u,
        "kernel": kernel_a + kernel_W + kernel_u,
    }


def _validate_state(state: State) -> None:
    if state.a.ndim != 2 or state.W.ndim != 3 or state.u.ndim != 3:
        raise ValueError("state tensors must have ranks 2, 3, and 3")
    replicas, width = state.a.shape
    if state.W.shape != (replicas, width, width):
        raise ValueError("W must have shape (R,n,n)")
    if state.u.shape != (replicas, 2, width):
        raise ValueError("u must have shape (R,2,n)")
    if state.a.dtype != state.W.dtype or state.a.dtype != state.u.dtype:
        raise ValueError("all state tensors must have the same dtype")
    if state.a.device != state.W.device or state.a.device != state.u.device:
        raise ValueError("all state tensors must be on the same device")


def _channel_form(
    matrix: torch.Tensor, left: torch.Tensor, right: torch.Tensor
) -> torch.Tensor:
    return 0.25 * torch.einsum("s,rst,t->r", left, matrix, right)


def fused_eval(
    state: State, configuration: Configuration
) -> tuple[Tangent, Observables]:
    """Evaluate the exact two-sample average-loss field in one forward pass.

    If ``q=(1,sigma)`` and ``p=(1,-sigma)``, then

    ``g=q.f/2``, ``delta=p.f/2``, ``Kg=n|grad g|^2``,
    ``Kdelta=n|grad delta|^2``, and ``C=n grad(g).grad(delta)``.

    The returned numerators give the exact finite-width identities

    ``g_dot = 2*((1-g)*Kg - delta*C)`` and
    ``delta_dot = 2*((1-g)*C - delta*Kdelta)``.
    """

    _validate_state(state)
    n = state.width
    inv_n = 1.0 / n
    inv_sqrt_n = 1.0 / math.sqrt(n)
    gram = input_gram(
        configuration, dtype=state.u.dtype, device=state.u.device
    )
    labels = state.u.new_tensor(configuration.labels)

    u2 = state.u.square()
    z = torch.bmm(state.W, u2.transpose(1, 2)).transpose(1, 2) * inv_sqrt_n
    az = state.a[:, None, :] * z
    back = torch.bmm(state.W.transpose(1, 2), az.transpose(1, 2)).transpose(
        1, 2
    )
    output = torch.mean(state.a[:, None, :] * z.square(), dim=2)
    residual = labels[None, :] - output

    kernel_a = inv_n * torch.einsum(
        "rsi,rti->rst", z.square(), z.square()
    )
    readout_cross = torch.einsum("rsi,rti->rst", az, az)
    hidden_cross = torch.einsum("rsj,rtj->rst", u2, u2)
    kernel_W = 4.0 * inv_n**2 * readout_cross * hidden_cross
    ub = state.u * back
    kernel_u = (
        16.0
        * inv_n**2
        * torch.einsum("rsj,rtj->rst", ub, ub)
        * gram[None, :, :]
    )
    kernel = kernel_a + kernel_W + kernel_u

    da = torch.einsum("rs,rsi->ri", residual, z.square())
    dW = (2.0 * inv_sqrt_n) * torch.einsum(
        "rs,rsi,rsj->rij", residual, az, u2
    )
    u_source = residual[:, :, None] * ub
    du = (4.0 * inv_sqrt_n) * torch.einsum(
        "st,rtj->rsj", gram, u_source
    )
    w_derivative_l2 = torch.sqrt(
        torch.clamp(
            4.0
            * inv_n
            * torch.einsum(
                "rs,rt,rst,rst->r",
                residual,
                residual,
                readout_cross,
                hidden_cross,
            ),
            min=0.0,
        )
    )
    w_state_inner_derivative = 2.0 * float(n) * torch.sum(
        residual * output, dim=1
    )
    tangent = Tangent(
        da,
        dW,
        du,
        w_derivative_l2,
        w_state_inner_derivative,
    )

    sigma = float(configuration.sigma)
    q = state.u.new_tensor((1.0, sigma))
    p = state.u.new_tensor((1.0, -sigma))
    g = 0.5 * torch.einsum("s,rs->r", q, output)
    delta = 0.5 * torch.einsum("s,rs->r", p, output)

    kg_parts = tuple(_channel_form(part, q, q) for part in (
        kernel_a, kernel_W, kernel_u
    ))
    kd_parts = tuple(_channel_form(part, p, p) for part in (
        kernel_a, kernel_W, kernel_u
    ))
    cross_parts = tuple(_channel_form(part, q, p) for part in (
        kernel_a, kernel_W, kernel_u
    ))
    kernel_g = sum(kg_parts)
    kernel_delta = sum(kd_parts)
    cross_kernel = sum(cross_parts)
    projected_residual = 1.0 - g
    effective_numerator = projected_residual * kernel_g - delta * cross_kernel
    transverse_numerator = projected_residual * cross_kernel - delta * kernel_delta
    loss_full = 0.5 * residual.square().sum(dim=1)
    loss_projected = projected_residual.square()

    observables = Observables(
        output=output,
        residual=residual,
        g=g,
        delta=delta,
        kernel_matrix=kernel,
        kernel_a_matrix=kernel_a,
        kernel_W_matrix=kernel_W,
        kernel_u_matrix=kernel_u,
        kernel_g=kernel_g,
        kernel_delta=kernel_delta,
        cross_kernel=cross_kernel,
        kernel_g_a=kg_parts[0],
        kernel_g_W=kg_parts[1],
        kernel_g_u=kg_parts[2],
        kernel_delta_a=kd_parts[0],
        kernel_delta_W=kd_parts[1],
        kernel_delta_u=kd_parts[2],
        cross_kernel_a=cross_parts[0],
        cross_kernel_W=cross_parts[1],
        cross_kernel_u=cross_parts[2],
        effective_numerator=effective_numerator,
        transverse_numerator=transverse_numerator,
        loss_full=loss_full,
        loss_projected=loss_projected,
        q1=torch.mean(state.u.square(), dim=2),
        q2=torch.mean(z.square(), dim=2),
    )
    return tangent, observables


def euler_step_in_place(state: State, tangent: Tangent, step: float) -> State:
    """Apply the frozen FP32 Euler update in place.

    ``add_(..., alpha=step)`` matches the qualified Stage-V arithmetic path.
    An algebraically equivalent out-of-place multiply/add is deliberately not
    used because its FP32 rounding and unchanged-entry behavior can differ.
    """

    state.a.add_(tangent.a, alpha=step)
    state.W.add_(tangent.W, alpha=step)
    state.u.add_(tangent.u, alpha=step)
    return state
