#!/usr/bin/env python3
"""Small one-input deformation layer over the audited FP32 Euler primitives.

This module deliberately contains no campaign runner or result writer.  It
only supplies the four already-theorized one-input configurations needed by
the breadth-panel tests and the exact physical-to-proxy coordinate map.
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

import euler_engine as audited_euler  # noqa: E402
import nested_init as audited_init  # noqa: E402


State = audited_euler.State
Tangent = audited_euler.Tangent


@dataclass(frozen=True)
class Configuration:
    key: str
    centering: float = 0.0
    hidden_metric: float = 1.0
    middle_weight_variance: float = 1.0
    proxy_family: str = "canonical"
    proxy_parameters: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if not math.isfinite(self.centering):
            raise ValueError("centering must be finite")
        if not math.isfinite(self.hidden_metric) or self.hidden_metric < 0.0:
            raise ValueError("hidden metric must be finite and nonnegative")
        if (
            not math.isfinite(self.middle_weight_variance)
            or self.middle_weight_variance <= 0.0
        ):
            raise ValueError("middle-weight variance must be finite and positive")


CANONICAL = Configuration("canonical")
CENTERED_C1 = Configuration(
    "centered_c1",
    centering=1.0,
    proxy_family="centered_activation",
    proxy_parameters=(("c", "1"),),
)
RELATIVE_METRIC_L2 = Configuration(
    "relative_metric_l2",
    hidden_metric=2.0,
    proxy_family="relative_metric_output",
    proxy_parameters=(("lambda", "2"),),
)
VARIANCE_VHALF = Configuration(
    "variance_vhalf",
    middle_weight_variance=0.5,
    proxy_family="variance_homotopy",
    proxy_parameters=(("alpha", "1/2"),),
)
CONFIGURATIONS = (CANONICAL, CENTERED_C1, RELATIVE_METRIC_L2, VARIANCE_VHALF)
CONFIGURATION_BY_KEY = {configuration.key: configuration for configuration in CONFIGURATIONS}


def centered_gaussian_moments(configuration: Configuration) -> dict[str, float]:
    """Return the three moments needed for exact finite-width initialization.

    If ``h=U**2-c`` for ``U ~ N(0,1)``, the notation is

    ``m2=E[h**2]``, ``m4=E[h**4]``, and ``r=E[U**2 h**2]``.

    Keeping ``r`` separate is essential: the first-layer kernel component
    contains the self-contraction in which the differentiated ``U`` is also
    present in ``h``.
    """

    c = configuration.centering
    return {
        "m2": 3.0 - 2.0 * c + c * c,
        "m4": 105.0 - 60.0 * c + 18.0 * c**2 - 4.0 * c**3 + c**4,
        "r": 15.0 - 6.0 * c + c * c,
    }


def initial_finite_width_means(
    configuration: Configuration, width: int
) -> dict[str, float]:
    """Exact Gaussian means of the initialized finite-``n`` observables.

    These are expectations over one ordinary Gaussian network.  Antithetic
    readout pairing leaves every kernel component and both hidden norms
    unchanged while making the pair-mean output exactly zero.
    """

    if int(width) != width or width < 1:
        raise ValueError("width must be a positive integer")
    n = float(width)
    moments = centered_gaussian_moments(configuration)
    m2, m4, r = moments["m2"], moments["m4"], moments["r"]
    metric = configuration.hidden_metric
    v = configuration.middle_weight_variance
    empirical_h2_square = m2 * m2 + (m4 - m2 * m2) / n
    kernel_a = 3.0 * v * v * empirical_h2_square
    kernel_W = 4.0 * metric * v * empirical_h2_square
    kernel_u = 16.0 * metric * v * v * (m2 + (3.0 * r - m2) / n)
    return {
        "output": 0.0,
        "q1": 1.0,
        "q2": v * m2,
        "kernel_a": kernel_a,
        "kernel_W": kernel_W,
        "kernel_u": kernel_u,
        "kernel": kernel_a + kernel_W + kernel_u,
        **moments,
    }


def initial_mean_field_values(configuration: Configuration) -> dict[str, float]:
    """Return the elementary Gaussian infinite-width initialization gate."""

    metric = configuration.hidden_metric
    v = configuration.middle_weight_variance
    hidden_second_moment = centered_gaussian_moments(configuration)["m2"]
    kernel_a = 3.0 * v * v * hidden_second_moment**2
    kernel_W = metric * 4.0 * v * hidden_second_moment**2
    kernel_u = metric * 16.0 * v * v * hidden_second_moment
    return {
        "output": 0.0,
        "q1": 1.0,
        "q2": v * hidden_second_moment,
        "kernel_a": kernel_a,
        "kernel_W": kernel_W,
        "kernel_u": kernel_u,
        "kernel": kernel_a + kernel_W + kernel_u,
    }


@dataclass
class Observables:
    """Physical-coordinate observables for each finite-width trajectory."""

    output: torch.Tensor
    kernel: torch.Tensor
    kernel_a: torch.Tensor
    kernel_W: torch.Tensor
    kernel_u: torch.Tensor
    weighted_kernel: torch.Tensor
    loss: torch.Tensor
    q1: torch.Tensor
    q2: torch.Tensor


@dataclass
class ProxyObservables:
    """Coordinates used by the accepted exact proxy inventory.

    For the variance homotopy, ``proxy_time = v * physical_time``.  All other
    configurations have ``v=1`` and hence use the physical coordinates.
    """

    output: torch.Tensor
    target: float
    kernel: torch.Tensor
    kernel_a: torch.Tensor
    kernel_W: torch.Tensor
    kernel_u: torch.Tensor
    weighted_kernel: torch.Tensor
    loss: torch.Tensor
    q1: torch.Tensor
    q2: torch.Tensor
    time_scale: float


def _physical_state_digest(
    seed: int,
    lineage: int,
    width: int,
    configuration: Configuration,
    a: np.ndarray,
    u: np.ndarray,
    W: np.ndarray,
) -> str:
    digest = hashlib.sha256()
    digest.update(b"breadth-panel-one-input-physical-state-v1\0")
    digest.update(
        (
            f"{seed}\0{lineage}\0{width}\0{configuration.key}\0"
            f"{configuration.centering.hex()}\0"
            f"{configuration.hidden_metric.hex()}\0"
            f"{configuration.middle_weight_variance.hex()}\0"
        ).encode("ascii")
    )
    for array in (a, u, W):
        digest.update(np.asarray(array, dtype="<f4", order="C").tobytes())
    return digest.hexdigest()


def physical_prefix_digest(
    seed: int,
    lineage: int,
    size: int,
    configuration: Configuration,
    a: np.ndarray,
    u: np.ndarray,
    W: np.ndarray,
) -> str:
    """Hash a transformed physical coordinate prefix independently of width.

    In particular, the variance-homotopy digest binds the rounded
    ``sqrt(v) * W`` bytes rather than merely retaining the unscaled RNG
    prefix.  Omitting the parent width makes equal coordinate prefixes at
    ``n=2048`` and ``n=4096`` compare byte-for-byte.
    """

    if size < 1 or size > len(a) or size > len(u):
        raise ValueError("physical prefix exceeds vector state")
    if size > W.shape[0] or size > W.shape[1]:
        raise ValueError("physical prefix exceeds matrix state")
    digest = hashlib.sha256()
    digest.update(b"breadth-panel-one-input-physical-prefix-v1\0")
    digest.update(struct.pack("<QQQ", int(seed), int(lineage), int(size)))
    digest.update(
        (
            f"{configuration.key}\0{configuration.centering.hex()}\0"
            f"{configuration.hidden_metric.hex()}\0"
            f"{configuration.middle_weight_variance.hex()}\0"
        ).encode("ascii")
    )
    for label, array in (
        (b"a", a[:size]),
        (b"u", u[:size]),
        (b"W", W[:size, :size]),
    ):
        digest.update(label + b"\0")
        digest.update(np.asarray(array, dtype="<f4", order="C").tobytes(order="C"))
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
    """Reuse the frozen coordinate RNG, then apply the physical variance.

    ``middle_weight_variance`` is a variance, not a standard deviation.  The
    initialized physical matrix is therefore ``sqrt(v) * W_base``.  The
    frozen digest is retained as RNG provenance and a separate digest binds
    the transformed physical state.
    """

    a_np, u_np, W_base, base_digest, base_prefixes = audited_init.generate_lineage(
        width,
        seed=seed,
        lineage=lineage,
        row_block=row_block,
        prefix_sizes=prefix_sizes,
    )
    std_scale = np.float32(math.sqrt(configuration.middle_weight_variance))
    W_np = np.multiply(W_base, std_scale, dtype=np.float32)
    physical_digest = _physical_state_digest(
        seed, lineage, width, configuration, a_np, u_np, W_np
    )
    physical_prefixes = {
        int(size): physical_prefix_digest(
            seed,
            lineage,
            int(size),
            configuration,
            a_np,
            u_np,
            W_np,
        )
        for size in prefix_sizes
    }
    a0 = torch.from_numpy(a_np).to(device=device)
    u0 = torch.from_numpy(u_np).to(device=device)
    W0 = torch.from_numpy(W_np).to(device=device)
    state = State(
        torch.stack((a0, -a0), dim=0),
        torch.stack((W0, W0), dim=0),
        torch.stack((u0, u0), dim=0),
    )
    return state, {
        "configuration": configuration.key,
        "base_state_sha256": base_digest,
        "base_prefix_sha256": dict(base_prefixes),
        "physical_state_sha256": physical_digest,
        "physical_prefix_sha256": physical_prefixes,
        "middle_weight_variance": configuration.middle_weight_variance,
        "middle_weight_std_scale_fp32": float(std_scale),
    }


def fused_eval(
    state: State,
    configuration: Configuration,
    *,
    target: float = 1.0,
) -> tuple[Tangent, Observables]:
    """Evaluate the physical squared-loss field and all panel observables.

    The block metric is ``diag(I_a, lambda I_W, lambda I_u)``.  Consequently
    the physical update uses one factor of ``lambda`` on each hidden tangent,
    and ``K=n grad(f)^T M grad(f)`` uses one (not two) factor on each hidden
    kernel component.
    """

    n = state.width
    inv_n = 1.0 / n
    inv_sqrt_n = 1.0 / math.sqrt(n)
    u2 = state.u.square()
    hidden = (
        u2
        if configuration.centering == 0.0
        else u2 - configuration.centering
    )
    z = torch.bmm(state.W, hidden.unsqueeze(-1)).squeeze(-1) * inv_sqrt_n
    az = state.a * z
    back = torch.bmm(state.W.transpose(1, 2), az.unsqueeze(-1)).squeeze(-1)
    output = torch.mean(state.a * z.square(), dim=1)

    raw_kernel_a = inv_n * torch.sum(z.pow(4), dim=1)
    raw_kernel_W = (
        4.0
        * inv_n**2
        * torch.sum(az.square(), dim=1)
        * torch.sum(hidden.square(), dim=1)
    )
    raw_kernel_u = 16.0 * inv_n**2 * torch.sum(
        state.u.square() * back.square(), dim=1
    )
    metric = configuration.hidden_metric
    kernel_a = raw_kernel_a
    kernel_W = metric * raw_kernel_W
    kernel_u = metric * raw_kernel_u
    kernel = kernel_a + kernel_W + kernel_u
    residual = target - output
    factor = 2.0 * residual

    da = factor[:, None] * z.square()
    raw_coefficient = (2.0 * inv_sqrt_n) * factor
    coefficient = metric * raw_coefficient
    dW = coefficient[:, None, None] * az.unsqueeze(2) * hidden.unsqueeze(1)
    raw_du = (4.0 * inv_sqrt_n) * state.u * back * factor[:, None]
    du = metric * raw_du
    dW_l2 = (
        torch.abs(coefficient)
        * torch.linalg.vector_norm(az, dim=1)
        * torch.linalg.vector_norm(hidden, dim=1)
    )
    W_inner_dW = 2.0 * metric * factor * float(n) * output
    tangent = Tangent(da, dW, du, dW_l2, W_inner_dW)
    observables = Observables(
        output=output,
        kernel=kernel,
        kernel_a=kernel_a,
        kernel_W=kernel_W,
        kernel_u=kernel_u,
        weighted_kernel=residual * kernel,
        loss=residual.square(),
        q1=torch.mean(state.u.square(), dim=1),
        q2=torch.mean(z.square(), dim=1),
    )
    return tangent, observables


def to_proxy_coordinates(
    observables: Observables,
    configuration: Configuration,
    *,
    target: float = 1.0,
) -> ProxyObservables:
    """Map physical records to the exact hierarchy's comparison chart.

    With middle-weight variance ``v``, the accepted hierarchy is

    ``z=f/v``, ``kappa(z)=K(v*z)/v``, ``z_target=target/v``.

    Its natural squared-loss clock is ``tau=v*t``.  Thus the proxy driver and
    loss are the physical weighted kernel and loss divided by ``v**2``.
    ``Q2/v`` is included only as a dimensionless diagnostic; no independent
    variance-homotopy Q2 hierarchy is claimed.
    """

    v = configuration.middle_weight_variance
    return ProxyObservables(
        output=observables.output / v,
        target=target / v,
        kernel=observables.kernel / v,
        kernel_a=observables.kernel_a / v,
        kernel_W=observables.kernel_W / v,
        kernel_u=observables.kernel_u / v,
        weighted_kernel=observables.weighted_kernel / (v * v),
        loss=observables.loss / (v * v),
        q1=observables.q1,
        q2=observables.q2 / v,
        time_scale=v,
    )
