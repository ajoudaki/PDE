#!/usr/bin/env python3
"""Exact finite-width canonical quadratic model in PyTorch.

This module contains no statistical aggregation and no approximation to the
gradient.  The only numerical approximation used by the campaign lives in the
ODE solvers.  Batch dimension zero always indexes independent finite-width
networks.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import torch


Tensor = torch.Tensor


@dataclass
class State:
    """Canonical parameters, batched on axis zero."""

    a: Tensor
    W: Tensor
    u: Tensor

    @property
    def batch_size(self) -> int:
        return int(self.a.shape[0])

    @property
    def width(self) -> int:
        return int(self.a.shape[1])

    def clone(self) -> "State":
        return State(self.a.clone(), self.W.clone(), self.u.clone())


@dataclass
class Observables:
    """Direct analytic observables for every member of a batch."""

    output: Tensor
    kernel: Tensor
    q1: Tensor
    q2: Tensor
    kernel_a: Tensor
    kernel_W: Tensor
    kernel_u: Tensor


def add_scaled(state: State, tangent: State, scale: float) -> State:
    return State(
        state.a + scale * tangent.a,
        state.W + scale * tangent.W,
        state.u + scale * tangent.u,
    )


def linear_combination(
    state: State,
    terms: tuple[tuple[float, State], ...],
    step: float,
) -> State:
    """Return ``state + step * sum(coefficient * tangent)``."""

    a = state.a
    W = state.W
    u = state.u
    for coefficient, tangent in terms:
        a = a + (step * coefficient) * tangent.a
        W = W + (step * coefficient) * tangent.W
        u = u + (step * coefficient) * tangent.u
    return State(a, W, u)


def forward_primitives(state: State) -> tuple[Tensor, Tensor, Tensor, Tensor]:
    """Return ``u^2, z, a*z, W^T(a*z)`` with the exact model scaling."""

    n = state.width
    u2 = state.u.square()
    z = torch.bmm(state.W, u2.unsqueeze(-1)).squeeze(-1) / math.sqrt(n)
    az = state.a * z
    v = torch.bmm(state.W.transpose(1, 2), az.unsqueeze(-1)).squeeze(-1)
    return u2, z, az, v


def output(state: State) -> Tensor:
    _, z, _, _ = forward_primitives(state)
    return torch.mean(state.a * z.square(), dim=1)


def feature_rhs(state: State) -> State:
    """Return ``n * grad(f_n)`` exactly, without automatic differentiation."""

    n = state.width
    u2, z, az, v = forward_primitives(state)
    inv_sqrt_n = 1.0 / math.sqrt(n)
    da = z.square()
    dW = (2.0 * inv_sqrt_n) * az.unsqueeze(2) * u2.unsqueeze(1)
    du = (4.0 * inv_sqrt_n) * state.u * v
    return State(da, dW, du)


def observables(state: State) -> Observables:
    """Return output, direct kernel, and hidden squared-RMS observables.

    The kernel is evaluated by its analytic sum-of-squares formula

        K_n = n ||grad f_n||^2,

    not by differentiating an output curve.
    """

    n = state.width
    inv_n = 1.0 / n
    u2, z, az, v = forward_primitives(state)
    sum_u4 = torch.sum(u2.square(), dim=1)
    sum_az2 = torch.sum(az.square(), dim=1)
    kernel_a = inv_n * torch.sum(z.pow(4), dim=1)
    kernel_W = 4.0 * inv_n**2 * sum_az2 * sum_u4
    kernel_u = 16.0 * inv_n**2 * torch.sum(u2 * v.square(), dim=1)
    return Observables(
        output=torch.mean(state.a * z.square(), dim=1),
        kernel=kernel_a + kernel_W + kernel_u,
        q1=torch.mean(u2, dim=1),
        q2=torch.mean(z.square(), dim=1),
        kernel_a=kernel_a,
        kernel_W=kernel_W,
        kernel_u=kernel_u,
    )


def scaled_rhs(
    state: State,
    mode: str,
    *,
    target: float = 1.0,
    kernel_floor: float = 1.0e-14,
) -> tuple[State, Observables]:
    """Return a physical-time or output-clock vector field.

    ``physical`` implements gradient flow for ``(target-f)^2``:

        theta_dot = 2 (target-f) n grad(f).

    ``output_clock`` implements the same parameter-space route with output as
    time:

        d theta / d y = n grad(f) / K_n.
    """

    obs = observables(state)
    raw = feature_rhs(state)
    if mode == "physical":
        factor = 2.0 * (target - obs.output)
    elif mode == "output_clock":
        if bool(torch.any(~torch.isfinite(obs.kernel)).item()):
            raise FloatingPointError("nonfinite kernel in output-clock RHS")
        if bool(torch.any(obs.kernel <= kernel_floor).item()):
            raise FloatingPointError("kernel reached the output-clock floor")
        factor = obs.kernel.reciprocal()
    else:
        raise ValueError(f"unknown clock mode: {mode!r}")
    return State(
        raw.a * factor[:, None],
        raw.W * factor[:, None, None],
        raw.u * factor[:, None],
    ), obs


def state_max_abs(state: State) -> Tensor:
    return torch.maximum(
        torch.maximum(
            torch.amax(torch.abs(state.a), dim=1),
            torch.amax(torch.abs(state.W), dim=(1, 2)),
        ),
        torch.amax(torch.abs(state.u), dim=1),
    )


def state_all_finite(state: State) -> bool:
    return bool(
        torch.all(torch.isfinite(state.a)).item()
        and torch.all(torch.isfinite(state.W)).item()
        and torch.all(torch.isfinite(state.u)).item()
    )


def generate_antithetic_state(
    width: int,
    pair_count: int,
    seed_base: int,
    *,
    device: torch.device,
    dtype: torch.dtype,
    pair_offset: int = 0,
    microcanonical_readout: bool = False,
) -> tuple[State, dict[str, Tensor]]:
    """Generate Gaussian base draws and their readout-sign antithetic copies.

    If ``microcanonical_readout`` is true, the base readout is projected onto
    the hyperplane orthogonal to the initialization vector ``z(0)^2``.  This
    imposes ``f_n(0)=0`` exactly up to floating-point roundoff.  The operation
    is a rank-one finite-width conditioning and must be reported separately
    from the ordinary Gaussian ensemble.
    """

    if width < 1 or pair_count < 1:
        raise ValueError("width and pair_count must be positive")
    base_a: list[Tensor] = []
    base_W: list[Tensor] = []
    base_u: list[Tensor] = []
    for local_index in range(pair_count):
        pair_index = pair_offset + local_index
        generator = torch.Generator(device=device)
        generator.manual_seed(int(seed_base + 104_729 * pair_index))
        base_a.append(torch.randn(width, generator=generator, device=device, dtype=dtype))
        base_u.append(torch.randn(width, generator=generator, device=device, dtype=dtype))
        base_W.append(
            torch.randn(
                (width, width), generator=generator, device=device, dtype=dtype
            )
        )

    a0 = torch.stack(base_a)
    W0 = torch.stack(base_W)
    u0 = torch.stack(base_u)
    projection_relative_norm = torch.zeros(pair_count, device=device, dtype=dtype)
    if microcanonical_readout:
        provisional = State(a0, W0, u0)
        _, z0, _, _ = forward_primitives(provisional)
        q = z0.square()
        denominator = torch.sum(q.square(), dim=1)
        if bool(torch.any(denominator <= 0.0).item()):
            raise FloatingPointError("degenerate microcanonical projection")
        coefficient = torch.sum(a0 * q, dim=1) / denominator
        removed = coefficient[:, None] * q
        projection_relative_norm = torch.linalg.vector_norm(removed, dim=1) / torch.clamp(
            torch.linalg.vector_norm(a0, dim=1), min=torch.finfo(dtype).tiny
        )
        a0 = a0 - removed

    # Pair adjacency is an invariant used by all downstream pair summaries.
    a = torch.stack((a0, -a0), dim=1).reshape(2 * pair_count, width)
    W = torch.stack((W0, W0), dim=1).reshape(2 * pair_count, width, width)
    u = torch.stack((u0, u0), dim=1).reshape(2 * pair_count, width)
    state = State(a, W, u)
    initial = observables(state)
    return state, {
        "initial_output": initial.output,
        "initial_kernel": initial.kernel,
        "projection_relative_norm": projection_relative_norm,
    }


def pair_average(values: Tensor) -> Tensor:
    if values.shape[0] % 2:
        raise ValueError("antithetic batch size must be even")
    return values.reshape(values.shape[0] // 2, 2, *values.shape[1:]).mean(dim=1)

