"""Exact tangent diagnostics for the canonical operator--Galerkin PDE.

The routines in this module differentiate the implementation in
``dense_pde.operator_galerkin``; they do not introduce a second primal PDE.
The primary stability diagnostic is deliberately modest in scope: it is the
exact induced gain for a *declared finite dictionary* of residual directions
and impulse times.  It is not, and is never labelled as, a full-state
worst-case ``C_T``.

An impulse below is an instantaneous jump in the tangent state.  This is the
correct discretization-independent representation of an ideal time impulse;
it is not a forcing divided by one RK time step.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence

import numpy as np


_CANONICAL_SOURCE = (
    Path(__file__).resolve().parents[2]
    / "activation_linearity_smoking_gun"
    / "source"
    / "src"
)
if str(_CANONICAL_SOURCE) not in sys.path:
    sys.path.insert(0, str(_CANONICAL_SOURCE))

from activations import get_activation  # noqa: E402
from dense_pde.operator_galerkin import (  # noqa: E402
    Fields,
    Observable,
    PDEQuadrature,
    PDESpec,
    PDEState,
    observe,
    rk4_step,
    solve_fields,
    vector_field,
)

from cross_p import (  # noqa: E402
    StateNormComponents,
    project_state,
    weighted_state_norm,
)


Array = np.ndarray
_OBSERVABLE_NAMES = ("f", "loss", "grams", "theta")


@dataclass
class TangentFields:
    """Directional derivatives of every array returned by ``solve_fields``."""

    dh: Array
    dp: Array
    dz: Array
    dD: Array
    dbeta: Array
    dhcoef: Array


@dataclass(frozen=True)
class ObservableTangent:
    """JVP of the four observables used by the proof-obligation audit."""

    f: Array
    loss: float
    grams: Array
    theta: Array


@dataclass(frozen=True)
class TangentTrajectory:
    times: Array
    states: tuple[PDEState, ...]
    tangents: tuple[PDEState, ...]
    f: Array
    loss: Array
    grams: Array
    theta: Array
    tangent_norm: Array


@dataclass(frozen=True)
class ImpulseResponse:
    label: str
    impulse_time: float
    direction_norm: float
    trajectory: TangentTrajectory


@dataclass(frozen=True)
class ResidualImpulse:
    """One explicitly supplied residual direction at one source time."""

    time: float
    direction: PDEState
    label: str = ""


@dataclass(frozen=True)
class ObservableScales:
    """Positive scales used to make observable blocks dimensionless."""

    f: float = 1.0
    loss: float = 1.0
    grams: float = 1.0
    theta: float = 1.0

    def validate(self) -> None:
        for name in _OBSERVABLE_NAMES:
            value = float(getattr(self, name))
            if not np.isfinite(value) or value <= 0.0:
                raise ValueError(f"observable scale {name!r} must be positive")


@dataclass(frozen=True)
class ResidualSubspaceGain:
    """Finite-dictionary group-L1/L2 impulse to Linf-observable gain.

    At each declared source time, coefficients across the orthonormal
    residual directions carry an L2 norm; these group norms are summed over
    source time.  For the output norm
    ``max_(sink time, observable block) ||block||_2``, the induced norm is
    exactly the largest response-matrix spectral norm over source time, sink
    time, and block.  This is the discrete
    ``L1(time;L2(state))->Linf(observable)`` norm required to multiply a
    state-norm residual integral.  It remains restricted to the supplied
    direction/time dictionary.
    """

    gain: float
    atom_l1_gain: float
    column_gains: Array
    block_response_norms: Array
    group_response_gains: Array
    block_labels: tuple[str, ...]
    block_sizes: tuple[int, ...]
    observation_times: Array
    impulse_times: Array
    source_times: Array
    direction_norms: Array
    impulse_labels: tuple[str, ...]
    maximizing_impulse: int
    maximizing_source: int
    maximizing_time: int
    maximizing_block: int
    maximizing_atom_coefficients: Array
    flattened_response_columns: Array
    flattened_observable_dimension: int
    responses: tuple[ImpulseResponse, ...]
    scope: str = (
        "finite group-L1(time)/L2(direction) residual dictionary; "
        "not a full-state C_T"
    )


@dataclass(frozen=True)
class L2ResponseSVD:
    """Secondary flattened L2-time response diagnostic."""

    singular_values: Array
    left_vectors: Array
    right_vectors: Array
    weighted_response_matrix: Array
    time_weights: Array
    operator_norm: float
    scope: str = "secondary flattened finite-dictionary L2 diagnostic"


@dataclass(frozen=True)
class NonlinearAmplitudeCheck:
    amplitude: float
    central_absolute_error: float
    central_relative_error: float
    plus_absolute_error: float
    minus_absolute_error: float
    symmetry_defect: float


@dataclass(frozen=True)
class NonlinearImpulseCheck:
    times: Array
    direction_norm: float
    checks: tuple[NonlinearAmplitudeCheck, ...]
    tangent_response: TangentTrajectory


@dataclass(frozen=True)
class BlockArclength:
    times: Array
    B_speed: Array
    a_speed: Array
    c_speed: Array
    total_speed: Array
    B: float
    a: float
    c: float
    total: float


@dataclass(frozen=True)
class ResidualDirectionBasis:
    snapshot_times: Array
    snapshots: tuple[PDEState, ...]
    snapshot_norms: Array
    directions: tuple[PDEState, ...]
    weighted_gram: Array
    discarded_snapshots: tuple[int, ...]


@dataclass(frozen=True)
class Stage5SerializableResult:
    """Arrays and JSON-safe details for the study's existing archive writer."""

    arrays: Mapping[str, Array]
    detail: Mapping[str, Any]


def _validate_state_pair(state: PDEState, tangent: PDEState) -> None:
    if (
        state.B.shape != tangent.B.shape
        or state.a.shape != tangent.a.shape
        or state.c.shape != tangent.c.shape
    ):
        raise ValueError("state and tangent must have identical shapes")
    arrays = (
        state.B,
        state.a,
        state.c,
        tangent.B,
        tangent.a,
        tangent.c,
    )
    if not all(np.all(np.isfinite(value)) for value in arrays):
        raise FloatingPointError("state and tangent must be finite")


def _activation_second_derivative(name: str, z: Array) -> Array:
    """Exact second derivative for every activation in the frozen registry."""

    if name == "tanh":
        value = np.tanh(z)
        return -2.0 * value * (1.0 - value * value)
    if name == "identity" or name == "linear_c2":
        return np.zeros_like(z)
    if name == "tanh_c2":
        value = np.tanh(2.0 * z)
        return -4.0 * value * (1.0 - value * value)
    if name == "tanh_c4":
        value = np.tanh(4.0 * z)
        return -8.0 * value * (1.0 - value * value)
    if name == "erf":
        return (
            -0.5
            * np.pi
            * z
            * np.exp(-0.25 * np.pi * z * z)
        )
    if name == "atan":
        scaled = 0.5 * np.pi * z
        return (
            -0.5
            * np.pi**2
            * z
            / (1.0 + scaled * scaled) ** 2
        )
    # Keep failure explicit if the canonical registry is extended.
    get_activation(name)
    raise ValueError(
        f"no exact second derivative registered for activation {name!r}"
    )


def solve_fields_jvp(
    state: PDEState,
    tangent: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    fields: Fields | None = None,
) -> tuple[TangentFields, Fields]:
    """Differentiate the canonical forward and backward depth solves."""

    _validate_state_pair(state, tangent)
    if fields is None:
        fields = solve_fields(state, spec, quadrature)

    N = spec.depth_nodes
    M = spec.base_points
    R = spec.fast_points
    m = spec.y.size
    P = spec.basis_size
    delta = 1.0 / N
    phi = quadrature.phi
    wb = quadrature.base_weights
    wf = quadrature.fast_weights

    dh = np.empty((N + 1, M, m), dtype=float)
    dz = np.empty((N, M, R, m), dtype=float)
    dD = np.empty_like(dz)
    dhcoef = np.empty((N, P, m), dtype=float)

    dh[0] = tangent.B @ spec.X
    for ell in range(N):
        dhcoef[ell] = phi.T @ (wb[:, None] * dh[ell])
        row = (
            spec.sigma_w * quadrature.epsilon[None, :, :]
            + state.c[ell]
        )
        dz[ell] = (
            np.einsum(
                "irp,pm->irm",
                tangent.c[ell],
                fields.hcoef[ell],
                optimize=True,
            )
            + np.einsum(
                "irp,pm->irm", row, dhcoef[ell], optimize=True
            )
        )
        dD[ell] = (
            _activation_second_derivative(spec.activation, fields.z[ell])
            * dz[ell]
        )
        dh[ell + 1] = (
            dh[ell]
            + spec.gamma
            * delta
            * np.einsum(
                "r,irm->im",
                wf,
                fields.D[ell] * dz[ell],
                optimize=True,
            )
        )

    dp = np.empty_like(dh)
    dbeta = np.empty_like(dz)
    dp[N] = tangent.a[:, None]
    for ell in range(N - 1, -1, -1):
        dbeta[ell] = (
            dD[ell] * fields.p[ell + 1, :, None, :]
            + fields.D[ell] * dp[ell + 1, :, None, :]
        )
        row = (
            spec.sigma_w * quadrature.epsilon[None, :, :]
            + state.c[ell]
        )
        dtranspose = (
            np.einsum(
                "i,r,irp,irm->pm",
                wb,
                wf,
                tangent.c[ell],
                fields.beta[ell],
                optimize=True,
            )
            + np.einsum(
                "i,r,irp,irm->pm",
                wb,
                wf,
                row,
                dbeta[ell],
                optimize=True,
            )
        )
        dp[ell] = (
            dp[ell + 1]
            + spec.gamma * delta * (phi @ dtranspose)
        )

    tangent_fields = TangentFields(
        dh=dh,
        dp=dp,
        dz=dz,
        dD=dD,
        dbeta=dbeta,
        dhcoef=dhcoef,
    )
    if not all(
        np.all(np.isfinite(value))
        for value in (
            dh,
            dp,
            dz,
            dD,
            dbeta,
            dhcoef,
        )
    ):
        raise FloatingPointError("nonfinite tangent field")
    return tangent_fields, fields


# Natural spelling variants retained for audit scripts.
tangent_solve_fields = solve_fields_jvp
solve_fields_tangent = solve_fields_jvp


def vector_field_jvp(
    state: PDEState,
    tangent: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    fields: Fields | None = None,
    tangent_fields: TangentFields | None = None,
) -> PDEState:
    """Exact Jacobian-vector product of the PDE characteristic velocity."""

    _validate_state_pair(state, tangent)
    if tangent_fields is None:
        tangent_fields, fields = solve_fields_jvp(
            state, tangent, spec, quadrature, fields
        )
    elif fields is None:
        fields = solve_fields(state, spec, quadrature)

    wb = quadrature.base_weights
    assert fields is not None
    f = np.einsum(
        "i,i,im->m", wb, state.a, fields.h[-1], optimize=True
    )
    df = np.einsum(
        "i,i,im->m", wb, tangent.a, fields.h[-1], optimize=True
    ) + np.einsum(
        "i,i,im->m", wb, state.a, tangent_fields.dh[-1], optimize=True
    )
    e = f - spec.y

    dBdot = -(
        (
            tangent_fields.dp[0] * e[None, :]
            + fields.p[0] * df[None, :]
        )
        @ spec.X.T
    )
    dadot = -(
        tangent_fields.dh[-1] @ e
        + fields.h[-1] @ df
    )
    dcdot = -spec.gamma * (
        np.einsum(
            "lirq,lpq,q->lirp",
            tangent_fields.dbeta,
            fields.hcoef,
            e,
            optimize=True,
        )
        + np.einsum(
            "lirq,lpq,q->lirp",
            fields.beta,
            tangent_fields.dhcoef,
            e,
            optimize=True,
        )
        + np.einsum(
            "lirq,lpq,q->lirp",
            fields.beta,
            fields.hcoef,
            df,
            optimize=True,
        )
    )
    result = PDEState(B=dBdot, a=dadot, c=dcdot)
    if not all(
        np.all(np.isfinite(value))
        for value in (result.B, result.a, result.c)
    ):
        raise FloatingPointError("nonfinite vector-field JVP")
    return result


def observable_jvp(
    state: PDEState,
    tangent: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    fields: Fields | None = None,
    tangent_fields: TangentFields | None = None,
) -> ObservableTangent:
    """Exact JVP of output, loss, all-depth Grams, and tangent kernel."""

    _validate_state_pair(state, tangent)
    if tangent_fields is None:
        tangent_fields, fields = solve_fields_jvp(
            state, tangent, spec, quadrature, fields
        )
    elif fields is None:
        fields = solve_fields(state, spec, quadrature)
    assert fields is not None

    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    f = np.einsum(
        "i,i,im->m", wb, state.a, fields.h[-1], optimize=True
    )
    df = np.einsum(
        "i,i,im->m", wb, tangent.a, fields.h[-1], optimize=True
    ) + np.einsum(
        "i,i,im->m", wb, state.a, tangent_fields.dh[-1], optimize=True
    )
    e = f - spec.y
    dloss = float(e @ df)
    dgrams = (
        np.einsum(
            "i,lim,lin->lmn",
            wb,
            tangent_fields.dh,
            fields.h,
            optimize=True,
        )
        + np.einsum(
            "i,lim,lin->lmn",
            wb,
            fields.h,
            tangent_fields.dh,
            optimize=True,
        )
    )

    dgp0 = (
        tangent_fields.dp[0].T @ (wb[:, None] * fields.p[0])
        + fields.p[0].T @ (wb[:, None] * tangent_fields.dp[0])
    )
    dtheta = dgrams[-1] + (spec.X.T @ spec.X) * dgp0
    for ell in range(spec.depth_nodes):
        gh = fields.hcoef[ell].T @ fields.hcoef[ell]
        dgh = (
            tangent_fields.dhcoef[ell].T @ fields.hcoef[ell]
            + fields.hcoef[ell].T @ tangent_fields.dhcoef[ell]
        )
        gbeta = np.einsum(
            "i,r,irq,irs->qs",
            wb,
            wf,
            fields.beta[ell],
            fields.beta[ell],
            optimize=True,
        )
        dgbeta = (
            np.einsum(
                "i,r,irq,irs->qs",
                wb,
                wf,
                tangent_fields.dbeta[ell],
                fields.beta[ell],
                optimize=True,
            )
            + np.einsum(
                "i,r,irq,irs->qs",
                wb,
                wf,
                fields.beta[ell],
                tangent_fields.dbeta[ell],
                optimize=True,
            )
        )
        dtheta += (
            spec.gamma**2 / spec.depth_nodes
        ) * (dgh * gbeta + gh * dgbeta)
    dtheta = 0.5 * (dtheta + dtheta.T)
    result = ObservableTangent(
        f=df,
        loss=dloss,
        grams=dgrams,
        theta=dtheta,
    )
    if not all(
        np.all(np.isfinite(value))
        for value in (result.f, result.grams, result.theta)
    ) or not np.isfinite(result.loss):
        raise FloatingPointError("nonfinite observable JVP")
    return result


def _add_scaled(
    state: PDEState, terms: Sequence[tuple[float, PDEState]], scale: float
) -> PDEState:
    return PDEState(
        B=state.B + scale * sum(weight * value.B for weight, value in terms),
        a=state.a + scale * sum(weight * value.a for weight, value in terms),
        c=state.c + scale * sum(weight * value.c for weight, value in terms),
    )


def _scale_state(state: PDEState, scale: float) -> PDEState:
    return PDEState(
        B=scale * state.B,
        a=scale * state.a,
        c=scale * state.c,
    )


def coupled_rk4_step(
    state: PDEState,
    tangent: PDEState,
    dt: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> tuple[PDEState, PDEState]:
    """RK4 step of the augmented primal+tangent ODE.

    The tangent is evaluated at the same four primal stage states.  Therefore
    this is also the exact derivative (up to floating point) of the canonical
    nonlinear RK4 map.
    """

    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be positive")
    _validate_state_pair(state, tangent)

    k1, fields1 = vector_field(state, spec, quadrature)
    l1 = vector_field_jvp(
        state, tangent, spec, quadrature, fields=fields1
    )

    state2 = _add_scaled(state, ((1.0, k1),), dt / 2.0)
    tangent2 = _add_scaled(tangent, ((1.0, l1),), dt / 2.0)
    k2, fields2 = vector_field(state2, spec, quadrature)
    l2 = vector_field_jvp(
        state2, tangent2, spec, quadrature, fields=fields2
    )

    state3 = _add_scaled(state, ((1.0, k2),), dt / 2.0)
    tangent3 = _add_scaled(tangent, ((1.0, l2),), dt / 2.0)
    k3, fields3 = vector_field(state3, spec, quadrature)
    l3 = vector_field_jvp(
        state3, tangent3, spec, quadrature, fields=fields3
    )

    state4 = _add_scaled(state, ((1.0, k3),), dt)
    tangent4 = _add_scaled(tangent, ((1.0, l3),), dt)
    k4, fields4 = vector_field(state4, spec, quadrature)
    l4 = vector_field_jvp(
        state4, tangent4, spec, quadrature, fields=fields4
    )

    new_state = _add_scaled(
        state,
        ((1.0, k1), (2.0, k2), (2.0, k3), (1.0, k4)),
        dt / 6.0,
    )
    new_tangent = _add_scaled(
        tangent,
        ((1.0, l1), (2.0, l2), (2.0, l3), (1.0, l4)),
        dt / 6.0,
    )
    return new_state, new_tangent


tangent_rk4_step = coupled_rk4_step


def weighted_tangent_inner_product(
    left: PDEState,
    right: PDEState,
    quadrature: PDEQuadrature,
) -> float:
    """Weighted inner product whose norm is exactly ``cross_p``'s norm."""

    _validate_state_pair(left, right)
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    return float(
        np.einsum("i,id,id->", wb, left.B, right.B, optimize=True)
        + np.einsum("i,i,i->", wb, left.a, right.a, optimize=True)
        + np.einsum(
            "i,r,lirp,lirp->",
            wb,
            wf,
            left.c,
            right.c,
            optimize=True,
        )
        / left.c.shape[0]
    )


def weighted_tangent_norm(
    tangent: PDEState,
    quadrature: PDEQuadrature,
    *,
    components: bool = False,
) -> float | StateNormComponents:
    """Alias of the weighted state norm, with tangent-specific semantics."""

    return weighted_state_norm(
        tangent, quadrature, components=components
    )


def pack_weighted_state(
    tangent: PDEState, quadrature: PDEQuadrature
) -> Array:
    """Pack a tangent into Euclidean coordinates that realize its true norm."""

    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    if tangent.B.shape[0] != wb.size:
        raise ValueError("slow coordinate count does not match quadrature")
    if tangent.c.shape[1:3] != (wb.size, wf.size):
        raise ValueError("coefficient coordinates do not match quadrature")
    N = tangent.c.shape[0]
    B = tangent.B * np.sqrt(wb)[:, None]
    a = tangent.a * np.sqrt(wb)
    c = tangent.c * np.sqrt(
        wb[None, :, None, None]
        * wf[None, None, :, None]
        / N
    )
    return np.concatenate((B.ravel(), a.ravel(), c.ravel()))


def unpack_weighted_state(
    packed: Array,
    template: PDEState,
    quadrature: PDEQuadrature,
) -> PDEState:
    """Inverse of :func:`pack_weighted_state` for a supplied state layout."""

    packed = np.asarray(packed, dtype=float)
    expected = template.B.size + template.a.size + template.c.size
    if packed.ndim != 1 or packed.size != expected:
        raise ValueError(f"packed vector must have shape ({expected},)")
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    N = template.c.shape[0]
    stop_B = template.B.size
    stop_a = stop_B + template.a.size
    B = packed[:stop_B].reshape(template.B.shape) / np.sqrt(wb)[:, None]
    a = packed[stop_B:stop_a].reshape(template.a.shape) / np.sqrt(wb)
    c = packed[stop_a:].reshape(template.c.shape) / np.sqrt(
        wb[None, :, None, None]
        * wf[None, None, :, None]
        / N
    )
    return PDEState(B=B, a=a, c=c)


def _validated_times(times: Sequence[float]) -> Array:
    result = np.asarray(times, dtype=float)
    if (
        result.ndim != 1
        or result.size < 1
        or not np.all(np.isfinite(result))
        or np.any(np.diff(result) <= 0.0)
    ):
        raise ValueError("times must be a finite, strictly increasing vector")
    return result


def _advance_state(
    state: PDEState,
    duration: float,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> PDEState:
    if duration < -1e-14:
        raise ValueError("cannot integrate backward")
    if duration <= 0.0:
        return state.copy()
    steps = max(1, int(np.ceil(duration / max_step)))
    step = duration / steps
    current = state.copy()
    for _ in range(steps):
        current = rk4_step(current, step, spec, quadrature)
    return current


def _advance_coupled(
    state: PDEState,
    tangent: PDEState,
    duration: float,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> tuple[PDEState, PDEState]:
    if duration < -1e-14:
        raise ValueError("cannot integrate backward")
    if duration <= 0.0:
        return state.copy(), tangent.copy()
    steps = max(1, int(np.ceil(duration / max_step)))
    step = duration / steps
    current_state = state.copy()
    current_tangent = tangent.copy()
    for _ in range(steps):
        current_state, current_tangent = coupled_rk4_step(
            current_state,
            current_tangent,
            step,
            spec,
            quadrature,
        )
    return current_state, current_tangent


def integrate_state_checkpoints(
    initial_state: PDEState,
    times: Sequence[float],
    *,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> tuple[PDEState, ...]:
    """Integrate the canonical state to exact requested checkpoint times."""

    time_array = _validated_times(times)
    if max_step <= 0.0 or not np.isfinite(max_step):
        raise ValueError("max_step must be positive")
    states = [initial_state.copy()]
    current = initial_state.copy()
    for left, right in zip(time_array[:-1], time_array[1:]):
        current = _advance_state(
            current, float(right - left), max_step, spec, quadrature
        )
        states.append(current.copy())
    return tuple(states)


def _integrate_observable_checkpoints(
    initial_state: PDEState,
    times: Sequence[float],
    *,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> tuple[Observable, ...]:
    """Streaming primal integration that retains observables, never states."""

    time_array = _validated_times(times)
    current = initial_state.copy()
    observables = [observe(current, spec, quadrature)]
    for left, right in zip(time_array[:-1], time_array[1:]):
        current = _advance_state(
            current, float(right - left), max_step, spec, quadrature
        )
        observables.append(observe(current, spec, quadrature))
    return tuple(observables)


def integrate_coupled_tangent(
    initial_state: PDEState,
    initial_tangent: PDEState,
    times: Sequence[float],
    *,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    retain_states: bool = True,
) -> TangentTrajectory:
    """Integrate and observe an exact tangent from a checkpoint."""

    time_array = _validated_times(times)
    if max_step <= 0.0 or not np.isfinite(max_step):
        raise ValueError("max_step must be positive")
    _validate_state_pair(initial_state, initial_tangent)
    states: list[PDEState] = []
    tangents: list[PDEState] = []
    observable_tangents: list[ObservableTangent] = []
    tangent_norms: list[float] = []

    current_state = initial_state.copy()
    current_tangent = initial_tangent.copy()
    for index, time in enumerate(time_array):
        if index:
            current_state, current_tangent = _advance_coupled(
                current_state,
                current_tangent,
                float(time - time_array[index - 1]),
                max_step,
                spec,
                quadrature,
            )
        fields = solve_fields(current_state, spec, quadrature)
        tangent_fields, _ = solve_fields_jvp(
            current_state,
            current_tangent,
            spec,
            quadrature,
            fields,
        )
        derivative = observable_jvp(
            current_state,
            current_tangent,
            spec,
            quadrature,
            fields,
            tangent_fields,
        )
        if retain_states:
            states.append(current_state.copy())
            tangents.append(current_tangent.copy())
        observable_tangents.append(derivative)
        tangent_norms.append(
            float(weighted_tangent_norm(current_tangent, quadrature))
        )

    return TangentTrajectory(
        times=time_array.copy(),
        states=tuple(states),
        tangents=tuple(tangents),
        f=np.stack([value.f for value in observable_tangents]),
        loss=np.asarray([value.loss for value in observable_tangents]),
        grams=np.stack([value.grams for value in observable_tangents]),
        theta=np.stack([value.theta for value in observable_tangents]),
        tangent_norm=np.asarray(tangent_norms),
    )


def impulse_response(
    checkpoint_state: PDEState,
    direction: PDEState,
    times: Sequence[float],
    *,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    normalize: bool = False,
    label: str = "",
    retain_states: bool = True,
) -> ImpulseResponse:
    """Propagate an instantaneous tangent jump from one checkpoint."""

    norm = float(weighted_tangent_norm(direction, quadrature))
    if norm <= 0.0 or not np.isfinite(norm):
        raise ValueError("impulse direction must have positive finite norm")
    tangent = _scale_state(direction, 1.0 / norm) if normalize else direction
    trajectory = integrate_coupled_tangent(
        checkpoint_state,
        tangent,
        times,
        max_step=max_step,
        spec=spec,
        quadrature=quadrature,
        retain_states=retain_states,
    )
    return ImpulseResponse(
        label=label,
        impulse_time=float(np.asarray(times, dtype=float)[0]),
        direction_norm=norm,
        trajectory=trajectory,
    )


def _validate_observable_selection(
    blocks: Sequence[str], scales: ObservableScales
) -> tuple[str, ...]:
    selected = tuple(str(name) for name in blocks)
    if not selected or len(set(selected)) != len(selected):
        raise ValueError("observable_blocks must be nonempty and unique")
    unknown = set(selected) - set(_OBSERVABLE_NAMES)
    if unknown:
        raise ValueError(f"unknown observable blocks: {sorted(unknown)}")
    scales.validate()
    return selected


def _observable_arrays(
    value: ObservableTangent,
    selected: Sequence[str],
    scales: ObservableScales,
) -> tuple[tuple[str, Array], ...]:
    records: list[tuple[str, Array]] = []
    for name in selected:
        scale = float(getattr(scales, name))
        if name == "f":
            records.append(("f", np.asarray(value.f).ravel() / scale))
        elif name == "loss":
            records.append(
                ("loss", np.asarray([value.loss], dtype=float) / scale)
            )
        elif name == "grams":
            for ell in range(value.grams.shape[0]):
                records.append(
                    (
                        f"gram[{ell}]",
                        np.asarray(value.grams[ell]).ravel() / scale,
                    )
                )
        elif name == "theta":
            records.append(
                ("theta", np.asarray(value.theta).ravel() / scale)
            )
    return tuple(records)


def flatten_observable_jvp(
    value: ObservableTangent,
    *,
    observable_blocks: Sequence[str] = _OBSERVABLE_NAMES,
    scales: ObservableScales = ObservableScales(),
) -> Array:
    """Flatten selected, scaled observable blocks in a fixed order."""

    selected = _validate_observable_selection(observable_blocks, scales)
    return np.concatenate(
        [array for _, array in _observable_arrays(value, selected, scales)]
    )


def _trajectory_observable(
    trajectory: TangentTrajectory, index: int
) -> ObservableTangent:
    return ObservableTangent(
        f=trajectory.f[index],
        loss=float(trajectory.loss[index]),
        grams=trajectory.grams[index],
        theta=trajectory.theta[index],
    )


def residual_subspace_l1_to_linf_gain(
    initial_state: PDEState,
    impulses: Sequence[ResidualImpulse],
    observation_times: Sequence[float],
    *,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    observable_blocks: Sequence[str] = ("f", "grams"),
    scales: ObservableScales = ObservableScales(),
    retain_response_states: bool = True,
) -> ResidualSubspaceGain:
    """Exact group-L1(time)/L2(direction) gain on a finite dictionary.

    Directions are normalized with :func:`weighted_tangent_norm`.  The
    reported number is

    ``max_(source,sink,block) ||response_matrix||_(2->2)``,

    where the response matrix contains the supplied residual directions at a
    common source time.  This is exactly induced by summing the direction-L2
    group norm over source times and taking a maximum observable-block L2 norm
    over sink times.  The legacy atomwise L1 max-column value is retained
    separately as ``atom_l1_gain``.  No claim is made about untested state
    directions or source times.
    """

    selected = _validate_observable_selection(observable_blocks, scales)
    times = _validated_times(observation_times)
    atoms = tuple(impulses)
    if not atoms:
        raise ValueError("at least one residual impulse is required")
    source_times = np.asarray([atom.time for atom in atoms], dtype=float)
    if (
        not np.all(np.isfinite(source_times))
        or np.any(source_times < times[0] - 1e-13)
        or np.any(source_times > times[-1] + 1e-13)
    ):
        raise ValueError("every impulse time must lie in the observation range")

    union_times = np.unique(np.concatenate((times, source_times)))
    if union_times[0] != times[0]:
        raise ValueError("initial state must correspond to first observation")
    base_states = integrate_state_checkpoints(
        initial_state,
        union_times,
        max_step=max_step,
        spec=spec,
        quadrature=quadrature,
    )
    base_by_time = {
        float(time): state for time, state in zip(union_times, base_states)
    }

    responses: list[ImpulseResponse] = []
    direction_norms: list[float] = []
    labels: list[str] = []
    block_norm_columns: list[Array] = []
    flat_columns: list[Array] = []
    block_labels: tuple[str, ...] | None = None
    block_sizes: tuple[int, ...] | None = None
    flat_dimension: int | None = None

    for atom_index, atom in enumerate(atoms):
        label = atom.label or f"impulse_{atom_index}"
        source = float(atom.time)
        active_observation_times = times[times >= source - 1e-13]
        local_times = np.unique(
            np.concatenate((np.asarray([source]), active_observation_times))
        )
        response = impulse_response(
            base_by_time[source],
            atom.direction,
            local_times,
            max_step=max_step,
            spec=spec,
            quadrature=quadrature,
            normalize=True,
            label=label,
            retain_states=retain_response_states,
        )
        if retain_response_states:
            responses.append(response)
        else:
            trajectory = response.trajectory
            responses.append(
                ImpulseResponse(
                    label=response.label,
                    impulse_time=response.impulse_time,
                    direction_norm=response.direction_norm,
                    trajectory=TangentTrajectory(
                        times=trajectory.times,
                        states=(),
                        tangents=(),
                        f=trajectory.f,
                        loss=trajectory.loss,
                        grams=trajectory.grams,
                        theta=trajectory.theta,
                        tangent_norm=trajectory.tangent_norm,
                    ),
                )
            )
        direction_norms.append(response.direction_norm)
        labels.append(label)

        local_lookup = {
            float(time): index
            for index, time in enumerate(response.trajectory.times)
        }
        per_time_blocks: list[Array] = []
        per_time_flat: list[Array] = []
        for sink in times:
            if sink < source - 1e-13:
                if block_labels is None or flat_dimension is None:
                    # Obtain dimensions from the source-time response.
                    source_value = _trajectory_observable(
                        response.trajectory, local_lookup[source]
                    )
                    records = _observable_arrays(
                        source_value, selected, scales
                    )
                    block_labels = tuple(name for name, _ in records)
                    block_sizes = tuple(array.size for _, array in records)
                    flat_dimension = sum(array.size for _, array in records)
                per_time_blocks.append(
                    np.zeros(len(block_labels), dtype=float)
                )
                per_time_flat.append(
                    np.zeros(flat_dimension, dtype=float)
                )
                continue
            value = _trajectory_observable(
                response.trajectory, local_lookup[float(sink)]
            )
            records = _observable_arrays(value, selected, scales)
            current_labels = tuple(name for name, _ in records)
            current_sizes = tuple(array.size for _, array in records)
            if block_labels is None:
                block_labels = current_labels
                block_sizes = current_sizes
            elif current_labels != block_labels:
                raise RuntimeError("observable block layout changed")
            elif current_sizes != block_sizes:
                raise RuntimeError("observable block sizes changed")
            flat = np.concatenate([array for _, array in records])
            if flat_dimension is None:
                flat_dimension = flat.size
            elif flat.size != flat_dimension:
                raise RuntimeError("observable dimension changed")
            per_time_blocks.append(
                np.asarray([np.linalg.norm(array) for _, array in records])
            )
            per_time_flat.append(flat)
        block_norm_columns.append(np.stack(per_time_blocks))
        flat_columns.append(np.concatenate(per_time_flat))

    assert (
        block_labels is not None
        and block_sizes is not None
        and flat_dimension is not None
    )
    # Shapes: atom x sink-time x observable-block, and flattened-time x atom.
    block_response_norms = np.stack(block_norm_columns)
    flattened_columns = np.stack(flat_columns, axis=1)
    column_gains = np.max(block_response_norms, axis=(1, 2))
    atom_l1_gain = float(np.max(column_gains))

    # Reconstitute the actual block vectors, group columns by source time,
    # and compute the exact L2(direction)->L2(block) norm for each
    # source/sink/block cell.
    atom_time_flat = flattened_columns.T.reshape(
        len(atoms), times.size, flat_dimension
    )
    unique_sources = np.unique(source_times)
    group_gains = np.zeros(
        (unique_sources.size, times.size, len(block_labels)), dtype=float
    )
    best: tuple[float, int, int, int, Array, Array] | None = None
    offsets = np.cumsum((0,) + block_sizes)
    for source_index, source in enumerate(unique_sources):
        atom_indices = np.flatnonzero(source_times == source)
        if atom_indices.size == 0:
            raise RuntimeError("empty source-time impulse group")
        for sink_index in range(times.size):
            for block_index in range(len(block_labels)):
                start = int(offsets[block_index])
                stop = int(offsets[block_index + 1])
                matrix = atom_time_flat[
                    atom_indices, sink_index, start:stop
                ].T
                if matrix.size == 0:
                    singular_value = 0.0
                    right = np.zeros(atom_indices.size)
                else:
                    _, singular_values, right_vectors_t = np.linalg.svd(
                        matrix, full_matrices=False
                    )
                    singular_value = float(singular_values[0])
                    right = right_vectors_t[0]
                group_gains[
                    source_index, sink_index, block_index
                ] = singular_value
                if best is None or singular_value > best[0]:
                    best = (
                        singular_value,
                        source_index,
                        sink_index,
                        block_index,
                        atom_indices,
                        right,
                    )
    if best is None:
        raise RuntimeError("no residual response block was evaluated")
    (
        gain,
        maximizing_source,
        maximizing_time,
        maximizing_block,
        maximizing_atom_indices,
        local_coefficients,
    ) = best
    global_coefficients = np.zeros(len(atoms), dtype=float)
    global_coefficients[maximizing_atom_indices] = local_coefficients
    maximizing_impulse = int(
        maximizing_atom_indices[int(np.argmax(np.abs(local_coefficients)))]
    )
    return ResidualSubspaceGain(
        gain=gain,
        atom_l1_gain=atom_l1_gain,
        column_gains=column_gains,
        block_response_norms=block_response_norms,
        group_response_gains=group_gains,
        block_labels=block_labels,
        block_sizes=block_sizes,
        observation_times=times.copy(),
        impulse_times=source_times,
        source_times=unique_sources,
        direction_norms=np.asarray(direction_norms),
        impulse_labels=tuple(labels),
        maximizing_impulse=maximizing_impulse,
        maximizing_source=int(maximizing_source),
        maximizing_time=int(maximizing_time),
        maximizing_block=int(maximizing_block),
        maximizing_atom_coefficients=global_coefficients,
        flattened_response_columns=flattened_columns,
        flattened_observable_dimension=flat_dimension,
        responses=tuple(responses),
    )


def _trapezoid_weights(times: Array) -> Array:
    if times.size == 1:
        return np.ones(1, dtype=float)
    weights = np.empty_like(times)
    weights[0] = 0.5 * (times[1] - times[0])
    weights[-1] = 0.5 * (times[-1] - times[-2])
    if times.size > 2:
        weights[1:-1] = 0.5 * (times[2:] - times[:-2])
    return weights


def flattened_response_svd(
    result: ResidualSubspaceGain,
    *,
    time_weights: Sequence[float] | None = None,
) -> L2ResponseSVD:
    """SVD of flattened responses, explicitly secondary to max-column gain."""

    if time_weights is None:
        weights = _trapezoid_weights(result.observation_times)
    else:
        weights = np.asarray(time_weights, dtype=float)
        if weights.shape != result.observation_times.shape:
            raise ValueError("time_weights have the wrong shape")
        if np.any(weights < 0.0) or not np.all(np.isfinite(weights)):
            raise ValueError("time_weights must be finite and nonnegative")
    row_scale = np.repeat(
        np.sqrt(weights), result.flattened_observable_dimension
    )
    matrix = row_scale[:, None] * result.flattened_response_columns
    left, singular_values, right_transpose = np.linalg.svd(
        matrix, full_matrices=False
    )
    return L2ResponseSVD(
        singular_values=singular_values,
        left_vectors=left,
        right_vectors=right_transpose.T,
        weighted_response_matrix=matrix,
        time_weights=weights,
        operator_norm=float(singular_values[0]) if singular_values.size else 0.0,
    )


def _observable_difference(
    left: Observable, right: Observable, denominator: float
) -> ObservableTangent:
    return ObservableTangent(
        f=(left.f - right.f) / denominator,
        loss=float((left.loss - right.loss) / denominator),
        grams=(left.grams - right.grams) / denominator,
        theta=(left.theta - right.theta) / denominator,
    )


def _observable_second_difference(
    plus: Observable,
    center: Observable,
    minus: Observable,
    denominator: float,
) -> ObservableTangent:
    return ObservableTangent(
        f=(plus.f + minus.f - 2.0 * center.f) / denominator,
        loss=float(
            (plus.loss + minus.loss - 2.0 * center.loss) / denominator
        ),
        grams=(
            plus.grams + minus.grams - 2.0 * center.grams
        )
        / denominator,
        theta=(
            plus.theta + minus.theta - 2.0 * center.theta
        )
        / denominator,
    )


def nonlinear_impulse_check(
    checkpoint_state: PDEState,
    direction: PDEState,
    times: Sequence[float],
    amplitudes: Sequence[float],
    *,
    max_step: float,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    observable_blocks: Sequence[str] = ("f", "grams"),
    scales: ObservableScales = ObservableScales(),
    normalize_direction: bool = True,
    retain_trajectory_states: bool = True,
) -> NonlinearImpulseCheck:
    """Compare tangent response with symmetric nonlinear restarted trajectories."""

    selected = _validate_observable_selection(observable_blocks, scales)
    time_array = _validated_times(times)
    amplitude_array = np.asarray(amplitudes, dtype=float)
    if (
        amplitude_array.ndim != 1
        or amplitude_array.size < 1
        or np.any(amplitude_array <= 0.0)
        or not np.all(np.isfinite(amplitude_array))
    ):
        raise ValueError("amplitudes must be a positive finite vector")

    direction_norm = float(weighted_tangent_norm(direction, quadrature))
    if direction_norm <= 0.0:
        raise ValueError("direction must have positive norm")
    tangent_direction = (
        _scale_state(direction, 1.0 / direction_norm)
        if normalize_direction
        else direction.copy()
    )
    tangent_response = integrate_coupled_tangent(
        checkpoint_state,
        tangent_direction,
        time_array,
        max_step=max_step,
        spec=spec,
        quadrature=quadrature,
        retain_states=retain_trajectory_states,
    )
    baseline_observables = _integrate_observable_checkpoints(
        checkpoint_state,
        time_array,
        max_step=max_step,
        spec=spec,
        quadrature=quadrature,
    )
    tangent_vectors = np.stack(
        [
            flatten_observable_jvp(
                _trajectory_observable(tangent_response, index),
                observable_blocks=selected,
                scales=scales,
            )
            for index in range(time_array.size)
        ]
    )
    reference = max(float(np.max(np.linalg.norm(tangent_vectors, axis=1))), 1e-15)

    checks: list[NonlinearAmplitudeCheck] = []
    for amplitude in amplitude_array:
        plus_initial = _add_scaled(
            checkpoint_state, ((1.0, tangent_direction),), float(amplitude)
        )
        minus_initial = _add_scaled(
            checkpoint_state, ((1.0, tangent_direction),), -float(amplitude)
        )
        plus_observables = _integrate_observable_checkpoints(
            plus_initial,
            time_array,
            max_step=max_step,
            spec=spec,
            quadrature=quadrature,
        )
        minus_observables = _integrate_observable_checkpoints(
            minus_initial,
            time_array,
            max_step=max_step,
            spec=spec,
            quadrature=quadrature,
        )
        central_vectors: list[Array] = []
        plus_vectors: list[Array] = []
        minus_vectors: list[Array] = []
        symmetry_vectors: list[Array] = []
        for plus, center, minus in zip(
            plus_observables, baseline_observables, minus_observables
        ):
            central_vectors.append(
                flatten_observable_jvp(
                    _observable_difference(
                        plus, minus, 2.0 * float(amplitude)
                    ),
                    observable_blocks=selected,
                    scales=scales,
                )
            )
            plus_vectors.append(
                flatten_observable_jvp(
                    _observable_difference(
                        plus, center, float(amplitude)
                    ),
                    observable_blocks=selected,
                    scales=scales,
                )
            )
            minus_vectors.append(
                flatten_observable_jvp(
                    _observable_difference(
                        center, minus, float(amplitude)
                    ),
                    observable_blocks=selected,
                    scales=scales,
                )
            )
            symmetry_vectors.append(
                flatten_observable_jvp(
                    _observable_second_difference(
                        plus,
                        center,
                        minus,
                        2.0 * float(amplitude),
                    ),
                    observable_blocks=selected,
                    scales=scales,
                )
            )
        central = np.stack(central_vectors)
        plus_linearized = np.stack(plus_vectors)
        minus_linearized = np.stack(minus_vectors)
        symmetry = np.stack(symmetry_vectors)
        central_error = float(
            np.max(np.linalg.norm(central - tangent_vectors, axis=1))
        )
        checks.append(
            NonlinearAmplitudeCheck(
                amplitude=float(amplitude),
                central_absolute_error=central_error,
                central_relative_error=central_error / reference,
                plus_absolute_error=float(
                    np.max(
                        np.linalg.norm(
                            plus_linearized - tangent_vectors, axis=1
                        )
                    )
                ),
                minus_absolute_error=float(
                    np.max(
                        np.linalg.norm(
                            minus_linearized - tangent_vectors, axis=1
                        )
                    )
                ),
                symmetry_defect=float(
                    np.max(np.linalg.norm(symmetry, axis=1))
                ),
            )
        )
    return NonlinearImpulseCheck(
        times=time_array,
        direction_norm=direction_norm,
        checks=tuple(checks),
        tangent_response=tangent_response,
    )


def projected_back_residual(
    high_state: PDEState,
    low_spec: PDESpec,
    high_spec: PDESpec,
    low_quadrature: PDEQuadrature,
    high_quadrature: PDEQuadrature,
) -> PDEState:
    """Return ``Pi_low F_high(Y)-F_low(Pi_low Y)`` at one checkpoint."""

    if low_spec.basis_size > high_spec.basis_size:
        raise ValueError("low basis level cannot exceed high basis level")
    if high_state.c.shape[-1] != high_spec.basis_size:
        raise ValueError("high state does not match high specification")
    if (
        not np.array_equal(
            low_quadrature.base_weights, high_quadrature.base_weights
        )
        or not np.array_equal(
            low_quadrature.fast_weights, high_quadrature.fast_weights
        )
        or not np.array_equal(
            low_quadrature.phi,
            high_quadrature.phi[:, : low_spec.basis_size],
        )
        or not np.array_equal(
            low_quadrature.epsilon,
            high_quadrature.epsilon[:, : low_spec.basis_size],
        )
    ):
        raise ValueError("low and high quadratures are not literal prefixes")
    projected = project_state(high_state, low_spec.basis_size)
    high_velocity, _ = vector_field(
        high_state, high_spec, high_quadrature
    )
    projected_high_velocity = project_state(
        high_velocity, low_spec.basis_size
    )
    low_velocity, _ = vector_field(
        projected, low_spec, low_quadrature
    )
    return PDEState(
        B=projected_high_velocity.B - low_velocity.B,
        a=projected_high_velocity.a - low_velocity.a,
        c=projected_high_velocity.c - low_velocity.c,
    )


def orthonormalize_residual_snapshots(
    snapshots: Sequence[PDEState],
    snapshot_times: Sequence[float],
    quadrature: PDEQuadrature,
    *,
    relative_tolerance: float = 1e-10,
) -> ResidualDirectionBasis:
    """Chronological, twice-reorthogonalized weighted Gram--Schmidt.

    The chronological rule makes the finite L1 dictionary deterministic.
    Nearly dependent snapshots are reported and omitted rather than divided
    by a vanishing norm.
    """

    records = tuple(snapshots)
    times = np.asarray(snapshot_times, dtype=float)
    if not records or times.shape != (len(records),):
        raise ValueError("one finite time is required per residual snapshot")
    if not np.all(np.isfinite(times)) or relative_tolerance <= 0.0:
        raise ValueError("snapshot times and tolerance must be valid")
    template = records[0]
    for record in records:
        _validate_state_pair(template, record)
    norms = np.asarray(
        [float(weighted_tangent_norm(record, quadrature)) for record in records]
    )
    scale = float(np.max(norms))
    if scale <= 0.0:
        raise ValueError("all residual snapshots are exactly zero")
    cutoff = relative_tolerance * scale
    basis: list[PDEState] = []
    discarded: list[int] = []
    for index, snapshot in enumerate(records):
        candidate = snapshot.copy()
        for _ in range(2):
            for direction in basis:
                coefficient = weighted_tangent_inner_product(
                    direction, candidate, quadrature
                )
                candidate = _add_scaled(
                    candidate, ((1.0, direction),), -coefficient
                )
        norm = float(weighted_tangent_norm(candidate, quadrature))
        if norm <= cutoff:
            discarded.append(index)
            continue
        basis.append(_scale_state(candidate, 1.0 / norm))
    if not basis:
        raise ValueError("all residual snapshots are numerically zero")
    gram = np.asarray(
        [
            [
                weighted_tangent_inner_product(left, right, quadrature)
                for right in basis
            ]
            for left in basis
        ]
    )
    if np.linalg.norm(gram - np.eye(len(basis)), ord=2) > 5e-10:
        raise RuntimeError("residual directions failed weighted orthonormality")
    return ResidualDirectionBasis(
        snapshot_times=times.copy(),
        snapshots=records,
        snapshot_norms=norms,
        directions=tuple(basis),
        weighted_gram=gram,
        discarded_snapshots=tuple(discarded),
    )


def stage5_serializable_result(
    base_initial_state: PDEState,
    high_checkpoint_states: Sequence[PDEState],
    high_checkpoint_times: Sequence[float],
    low_spec: PDESpec,
    high_spec: PDESpec,
    low_quadrature: PDEQuadrature,
    high_quadrature: PDEQuadrature,
    *,
    impulse_times: Sequence[float],
    observation_times: Sequence[float],
    max_step: float,
    nonlinear_amplitudes: Sequence[float] = (0.25, 0.5, 1.0),
    observable_blocks: Sequence[str] = ("f", "grams"),
    scales: ObservableScales = ObservableScales(),
    basis_relative_tolerance: float = 1e-10,
    precomputed_residuals: Sequence[PDEState] | None = None,
    serialize_residual_states: bool = True,
) -> Stage5SerializableResult:
    """Build one serializable Stage-5 result without writing or sealing it.

    Exact orchestration is:

    1. form low-projected high-to-low back residuals at supplied checkpoints;
    2. apply chronological weighted Gram--Schmidt;
    3. cross every retained direction with every declared impulse time;
    4. compute the exact finite group-L1(time)/L2(direction) gain and the
       secondary flattened L2 SVD;
    5. run symmetric nonlinear checks on the maximizing singular direction.

    The caller should pass ``result.arrays`` and ``result.detail`` to the
    study runner's existing atomic, provenance-bound archive writer.  Keeping
    sealing outside this numerical module avoids a second archive format.
    """

    checkpoint_times = np.asarray(high_checkpoint_times, dtype=float)
    if precomputed_residuals is None:
        high_states = tuple(high_checkpoint_states)
        if len(high_states) != checkpoint_times.size:
            raise ValueError("high checkpoint states and times disagree")
        residuals = tuple(
            projected_back_residual(
                state,
                low_spec,
                high_spec,
                low_quadrature,
                high_quadrature,
            )
            for state in high_states
        )
        residual_source = (
            "projected online from supplied "
            f"P{high_spec.basis_size} states into P{low_spec.basis_size}"
        )
    else:
        if tuple(high_checkpoint_states):
            raise ValueError(
                "high states and precomputed residuals are mutually exclusive"
            )
        residuals = tuple(precomputed_residuals)
        if len(residuals) != checkpoint_times.size:
            raise ValueError(
                "precomputed residuals and checkpoint times disagree"
            )
        for value in residuals:
            _validate_state_pair(base_initial_state, value)
        residual_source = (
            "precomputed online from the same common "
            f"P{low_spec.basis_size}/P{high_spec.basis_size} quadrature"
        )
    basis = orthonormalize_residual_snapshots(
        residuals,
        checkpoint_times,
        low_quadrature,
        relative_tolerance=basis_relative_tolerance,
    )
    residual_coefficients = np.asarray(
        [
            [
                weighted_tangent_inner_product(
                    direction, snapshot, low_quadrature
                )
                for direction in basis.directions
            ]
            for snapshot in basis.snapshots
        ]
    )
    reconstruction_errors: list[float] = []
    for snapshot, coefficients in zip(
        basis.snapshots, residual_coefficients
    ):
        reconstruction = _scale_state(
            basis.directions[0], float(coefficients[0])
        )
        for coefficient, direction in zip(
            coefficients[1:], basis.directions[1:]
        ):
            reconstruction = _add_scaled(
                reconstruction,
                ((float(coefficient), direction),),
                1.0,
            )
        remainder = _add_scaled(
            snapshot, ((1.0, reconstruction),), -1.0
        )
        reconstruction_errors.append(
            float(weighted_tangent_norm(remainder, low_quadrature))
        )
    residual_l2_norm = np.linalg.norm(residual_coefficients, axis=1)
    residual_l2_integral = float(
        np.trapezoid(residual_l2_norm, checkpoint_times)
    )
    sources = np.asarray(impulse_times, dtype=float)
    if sources.ndim != 1 or sources.size < 1:
        raise ValueError("impulse_times must be nonempty")
    impulses = tuple(
        ResidualImpulse(
            time=float(source),
            direction=direction,
            label=f"residual_basis_{basis_index}@t={source:.12g}",
        )
        for source in sources
        for basis_index, direction in enumerate(basis.directions)
    )
    gain = residual_subspace_l1_to_linf_gain(
        base_initial_state,
        impulses,
        observation_times,
        max_step=max_step,
        spec=low_spec,
        quadrature=low_quadrature,
        observable_blocks=observable_blocks,
        scales=scales,
        retain_response_states=False,
    )
    svd = flattened_response_svd(gain)

    maximizing_atoms = tuple(
        (float(coefficient), atom)
        for coefficient, atom in zip(
            gain.maximizing_atom_coefficients, impulses
        )
        if abs(float(coefficient)) > 0.0
    )
    if not maximizing_atoms:
        raise RuntimeError("maximizing group direction has no active atom")
    source = float(maximizing_atoms[0][1].time)
    if any(
        not np.isclose(atom.time, source)
        for _, atom in maximizing_atoms
    ):
        raise RuntimeError("maximizing group mixes distinct source times")
    maximizing_direction = _scale_state(
        maximizing_atoms[0][1].direction,
        maximizing_atoms[0][0],
    )
    for coefficient, atom in maximizing_atoms[1:]:
        maximizing_direction = _add_scaled(
            maximizing_direction,
            ((coefficient, atom.direction),),
            1.0,
        )
    observation_array = _validated_times(observation_times)
    checkpoint_grid = np.unique(
        np.concatenate((np.asarray([observation_array[0], source]),))
    )
    base_checkpoints = integrate_state_checkpoints(
        base_initial_state,
        checkpoint_grid,
        max_step=max_step,
        spec=low_spec,
        quadrature=low_quadrature,
    )
    checkpoint_state = base_checkpoints[-1]
    nonlinear_times = np.unique(
        np.concatenate(
            (
                np.asarray([source]),
                observation_array[observation_array >= source - 1e-13],
            )
        )
    )
    nonlinear = nonlinear_impulse_check(
        checkpoint_state,
        maximizing_direction,
        nonlinear_times,
        nonlinear_amplitudes,
        max_step=max_step,
        spec=low_spec,
        quadrature=low_quadrature,
        observable_blocks=observable_blocks,
        scales=scales,
        normalize_direction=True,
        retain_trajectory_states=False,
    )

    arrays: dict[str, Array] = {
        "residual_snapshot_times": basis.snapshot_times,
        "residual_snapshot_norms": basis.snapshot_norms,
        "residual_basis_coefficients": residual_coefficients,
        "residual_basis_reconstruction_error": np.asarray(
            reconstruction_errors
        ),
        "residual_subspace_l2_norm": residual_l2_norm,
        "residual_subspace_l2_time_integral": np.asarray(
            residual_l2_integral
        ),
        "residual_basis_weighted_gram": basis.weighted_gram,
        "observation_times": gain.observation_times,
        "impulse_times": gain.impulse_times,
        "direction_norms": gain.direction_norms,
        "block_response_norms": gain.block_response_norms,
        "group_response_gains": gain.group_response_gains,
        "column_gains": gain.column_gains,
        "primary_residual_subspace_gain": np.asarray(gain.gain),
        "amplified_residual_bound_point": np.asarray(
            gain.gain * residual_l2_integral
        ),
        "atom_l1_gain": np.asarray(gain.atom_l1_gain),
        "source_times": gain.source_times,
        "observable_block_sizes": np.asarray(
            gain.block_sizes, dtype=np.int64
        ),
        "maximizing_atom_coefficients": gain.maximizing_atom_coefficients,
        "maximizing_indices": np.asarray(
            [
                gain.maximizing_impulse,
                gain.maximizing_source,
                gain.maximizing_time,
                gain.maximizing_block,
            ],
            dtype=np.int64,
        ),
        "flattened_response_columns": gain.flattened_response_columns,
        "secondary_l2_singular_values": svd.singular_values,
        "secondary_l2_left_vectors": svd.left_vectors,
        "secondary_l2_right_vectors": svd.right_vectors,
        "secondary_l2_time_weights": svd.time_weights,
        "nonlinear_times": nonlinear.times,
        "nonlinear_amplitudes": np.asarray(
            [value.amplitude for value in nonlinear.checks]
        ),
        "nonlinear_central_absolute_error": np.asarray(
            [value.central_absolute_error for value in nonlinear.checks]
        ),
        "nonlinear_central_relative_error": np.asarray(
            [value.central_relative_error for value in nonlinear.checks]
        ),
        "nonlinear_plus_absolute_error": np.asarray(
            [value.plus_absolute_error for value in nonlinear.checks]
        ),
        "nonlinear_minus_absolute_error": np.asarray(
            [value.minus_absolute_error for value in nonlinear.checks]
        ),
        "nonlinear_symmetry_defect": np.asarray(
            [value.symmetry_defect for value in nonlinear.checks]
        ),
    }
    if serialize_residual_states:
        arrays.update(
            {
                "residual_snapshot_B": np.stack(
                    [value.B for value in basis.snapshots]
                ),
                "residual_snapshot_a": np.stack(
                    [value.a for value in basis.snapshots]
                ),
                "residual_snapshot_c": np.stack(
                    [value.c for value in basis.snapshots]
                ),
                "residual_basis_B": np.stack(
                    [value.B for value in basis.directions]
                ),
                "residual_basis_a": np.stack(
                    [value.a for value in basis.directions]
                ),
                "residual_basis_c": np.stack(
                    [value.c for value in basis.directions]
                ),
            }
        )
    if not all(np.all(np.isfinite(value)) for value in arrays.values()):
        raise FloatingPointError("nonfinite Stage-5 serializable array")
    detail: dict[str, Any] = {
        "primary_gain_scope": gain.scope,
        "primary_gain_definition": (
            "maximum response-matrix spectral norm over source time, sink "
            "time, and observable block; exact on the finite "
            "group-L1(time)/L2(direction) residual dictionary"
        ),
        "legacy_atom_l1_gain": gain.atom_l1_gain,
        "secondary_gain_scope": svd.scope,
        "full_state_gain_computed": False,
        "residual_basis_semantics": (
            "chronological twice-reorthogonalized weighted Gram-Schmidt of "
            "low-projected high-minus-low generator residual snapshots"
        ),
        "residual_snapshot_source": residual_source,
        "response_state_retention": (
            "primal/tangent checkpoint states discarded after extracting "
            "compact observable response arrays"
        ),
        "residual_state_serialization": (
            "full residual/basis states included"
            if serialize_residual_states
            else "omitted after reconstruction diagnostics to keep the "
            "stage archive compact"
        ),
        "residual_time_integral_semantics": (
            "trapezoidal integral on the declared generator checkpoint grid "
            "of the L2 norm of residual-basis coefficients; reconstruction "
            "errors are archived separately and must be negligible, while "
            "source-time grid refinement remains a separate gate"
        ),
        "discarded_residual_snapshot_indices": list(
            basis.discarded_snapshots
        ),
        "impulse_labels": list(gain.impulse_labels),
        "observable_block_labels": list(gain.block_labels),
        "observable_blocks": list(observable_blocks),
        "observable_scales": {
            name: float(getattr(scales, name)) for name in _OBSERVABLE_NAMES
        },
        "nonlinear_check_direction": (
            "maximizing right singular vector in the residual basis at "
            f"source time {source:.12g}"
        ),
        "ideal_impulse_semantics": (
            "instantaneous tangent-state jump, never a one-step forcing/dt"
        ),
    }
    return Stage5SerializableResult(arrays=arrays, detail=detail)


def block_state_arclength(
    states: Sequence[PDEState],
    times: Sequence[float],
    spec: PDESpec,
    quadrature: PDEQuadrature,
) -> BlockArclength:
    """Trapezoidal integral of weighted B, a, c, and total state speeds."""

    time_array = _validated_times(times)
    state_records = tuple(states)
    if len(state_records) != time_array.size:
        raise ValueError("states and times must have the same length")
    components: list[StateNormComponents] = []
    for state in state_records:
        velocity, _ = vector_field(state, spec, quadrature)
        value = weighted_tangent_norm(
            velocity, quadrature, components=True
        )
        assert isinstance(value, StateNormComponents)
        components.append(value)
    B_speed = np.asarray([value.B for value in components])
    a_speed = np.asarray([value.a for value in components])
    c_speed = np.asarray([value.c for value in components])
    total_speed = np.asarray([value.total for value in components])
    dt = np.diff(time_array)

    def integrate(values: Array) -> float:
        return float(np.sum(0.5 * dt * (values[:-1] + values[1:])))

    return BlockArclength(
        times=time_array.copy(),
        B_speed=B_speed,
        a_speed=a_speed,
        c_speed=c_speed,
        total_speed=total_speed,
        B=integrate(B_speed),
        a=integrate(a_speed),
        c=integrate(c_speed),
        total=integrate(total_speed),
    )


__all__ = [
    "BlockArclength",
    "ImpulseResponse",
    "L2ResponseSVD",
    "NonlinearAmplitudeCheck",
    "NonlinearImpulseCheck",
    "ObservableScales",
    "ObservableTangent",
    "ResidualDirectionBasis",
    "ResidualImpulse",
    "ResidualSubspaceGain",
    "Stage5SerializableResult",
    "TangentFields",
    "TangentTrajectory",
    "block_state_arclength",
    "coupled_rk4_step",
    "flatten_observable_jvp",
    "flattened_response_svd",
    "impulse_response",
    "integrate_coupled_tangent",
    "integrate_state_checkpoints",
    "nonlinear_impulse_check",
    "observable_jvp",
    "pack_weighted_state",
    "projected_back_residual",
    "residual_subspace_l1_to_linf_gain",
    "solve_fields_jvp",
    "solve_fields_tangent",
    "tangent_rk4_step",
    "tangent_solve_fields",
    "unpack_weighted_state",
    "vector_field_jvp",
    "weighted_tangent_inner_product",
    "weighted_tangent_norm",
    "orthonormalize_residual_snapshots",
    "stage5_serializable_result",
]
