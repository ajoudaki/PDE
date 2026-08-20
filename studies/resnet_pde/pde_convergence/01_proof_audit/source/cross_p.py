"""Common-quadrature diagnostics across Hermite--Galerkin levels.

This module is deliberately a thin diagnostic layer over the canonical
``dense_pde.operator_galerkin`` implementation.  In particular, it does not
reimplement the PDE vector field.  Its main purpose is to make comparisons
between Galerkin levels meaningful: every level uses the same Gauss--Hermite
base labels and a literal prefix of one centered, block-whitened Sobol row
array.

The scientific defaults are the complete degree-zero through degree-three
Hermite spaces in four Gaussian label coordinates,

    P = 5, 15, 35,

with an order-four tensor Gauss--Hermite rule (M = 4**4 = 256).  Smaller
levels and dimensions are accepted for unit tests and inexpensive audits.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Iterable, Mapping, Sequence

import numpy as np


# The proof-obligation study is a sibling of the immutable canonical study.
# Runners may already put this directory on sys.path; the fallback makes the
# module directly importable in isolation without copying scientific source.
_CANONICAL_SOURCE = (
    Path(__file__).resolve().parents[2]
    / "activation_linearity_smoking_gun"
    / "source"
    / "src"
)
if str(_CANONICAL_SOURCE) not in sys.path:
    sys.path.insert(0, str(_CANONICAL_SOURCE))

from dense_pde.operator_galerkin import (  # noqa: E402
    PDEQuadrature,
    PDESpec,
    PDEState,
    _eval_hermite_basis,
    _multi_indices,
    _normal_hermite_tensor,
    _normal_sobol,
    observe,
    rk4_step,
    vector_field,
)


Array = np.ndarray
DEFAULT_LEVELS = (5, 15, 35)


@dataclass(frozen=True)
class NestedQuadratureFamily:
    """A set of PDE specifications and literal-prefix quadratures."""

    levels: tuple[int, ...]
    master_levels: tuple[int, ...]
    specs: Mapping[int, PDESpec]
    quadratures: Mapping[int, PDEQuadrature]
    raw_epsilon: Array
    base_order: int

    @property
    def maximum_level(self) -> int:
        return self.levels[-1]

    def spec(self, level: int) -> PDESpec:
        return self.specs[level]

    def quadrature(self, level: int) -> PDEQuadrature:
        return self.quadratures[level]


@dataclass(frozen=True)
class StateNormComponents:
    B: float
    a: float
    c: float
    total: float


@dataclass(frozen=True)
class VelocityDefect:
    """Absolute weighted defects in the three characteristic velocities."""

    Bdot: float
    adot: float
    cdot: float
    total: float


@dataclass(frozen=True)
class ObservableDirectionalDerivative:
    f: Array
    loss: float
    grams: Array
    step: float


@dataclass(frozen=True)
class ObservableDerivativeDefect:
    f: float
    loss: float
    grams: float
    total: float
    left: ObservableDirectionalDerivative
    right: ObservableDirectionalDerivative


@dataclass(frozen=True)
class GeneratorDiagnostics:
    """Generator consistency and feedback diagnostics for one P < Pmax pair."""

    low_level: int
    high_level: int
    lift_consistency: VelocityDefect
    lift_outgoing_high_cdot: float
    outgoing_high_cdot: float
    high_to_low_feedback: VelocityDefect
    lift_observable_defect: ObservableDerivativeDefect
    feedback_observable_defect: ObservableDerivativeDefect
    lift_full_observable_defect: ObservableDerivativeDefect
    feedback_full_observable_defect: ObservableDerivativeDefect


@dataclass(frozen=True)
class ShadowRestart:
    times: Array
    state_defect: Array
    f_defect: Array
    loss_defect: Array
    gram_defect: Array


@dataclass(frozen=True)
class RestrictedSystem:
    state: PDEState
    spec: PDESpec
    quadrature: PDEQuadrature
    coefficients: Array


@dataclass(frozen=True)
class BasisDiagnostic:
    rank: int
    state_tail: float
    generator_tail: float
    feedback: VelocityDefect
    observable_defect: ObservableDerivativeDefect


def _validate_levels(levels: Sequence[int]) -> tuple[int, ...]:
    result = tuple(int(level) for level in levels)
    if not result or any(level < 1 for level in result):
        raise ValueError("levels must be a nonempty sequence of positive integers")
    if tuple(sorted(set(result))) != result:
        raise ValueError("levels must be strictly increasing")
    return result


def _symmetric_inverse_sqrt(matrix: Array, floor: float = 1e-13) -> Array:
    matrix = 0.5 * (matrix + matrix.T)
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    if eigenvalues[0] <= floor:
        raise ValueError(
            "weighted block is rank deficient: "
            f"minimum eigenvalue={eigenvalues[0]:.3e}"
        )
    return (eigenvectors / np.sqrt(eigenvalues)) @ eigenvectors.T


def _block_orthonormalize(
    raw: Array,
    weights: Array,
    block_ends: Sequence[int],
    *,
    center: bool,
) -> Array:
    """Weighted block Gram--Schmidt without modifying completed prefixes.

    Each new block is projected twice against the already completed columns
    and symmetrically whitened inside the block.  Consequently adding a later
    declared level cannot rotate or otherwise change an earlier prefix.
    """

    raw = np.asarray(raw, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if raw.ndim != 2 or weights.shape != (raw.shape[0],):
        raise ValueError("raw and weights have incompatible shapes")
    if np.any(weights <= 0.0) or not np.isclose(np.sum(weights), 1.0):
        raise ValueError("weights must be positive and sum to one")
    ends = _validate_levels(block_ends)
    if ends[-1] != raw.shape[1]:
        raise ValueError("last block boundary must equal the column count")

    work = raw.copy()
    if center:
        work -= np.sum(weights[:, None] * work, axis=0, keepdims=True)

    completed = np.empty((raw.shape[0], 0), dtype=float)
    start = 0
    for end in ends:
        block = work[:, start:end].copy()
        if completed.shape[1]:
            for _ in range(2):
                coefficients = completed.T @ (weights[:, None] * block)
                block -= completed @ coefficients
        gram = block.T @ (weights[:, None] * block)
        block = block @ _symmetric_inverse_sqrt(gram)
        if completed.shape[1]:
            # One final reorthogonalization removes roundoff from whitening.
            coefficients = completed.T @ (weights[:, None] * block)
            block -= completed @ coefficients
            gram = block.T @ (weights[:, None] * block)
            block = block @ _symmetric_inverse_sqrt(gram)
        completed = np.concatenate((completed, block), axis=1)
        start = end
    return completed


def _quadrature_record(
    *,
    base_latent: Array,
    base_weights: Array,
    raw_phi: Array,
    phi: Array,
    raw_epsilon: Array,
    epsilon: Array,
    fast_weights: Array,
    multi_indices: tuple[tuple[int, ...], ...],
) -> PDEQuadrature:
    raw_basis_gram = raw_phi.T @ (base_weights[:, None] * raw_phi)
    phi_gram = phi.T @ (base_weights[:, None] * phi)
    centered_raw_epsilon = raw_epsilon - np.sum(
        fast_weights[:, None] * raw_epsilon, axis=0, keepdims=True
    )
    raw_fast_cov = centered_raw_epsilon.T @ (
        fast_weights[:, None] * centered_raw_epsilon
    )
    fast_cov = epsilon.T @ (fast_weights[:, None] * epsilon)
    raw_basis_eigenvalues = np.linalg.eigvalsh(raw_basis_gram)
    raw_fast_eigenvalues = np.linalg.eigvalsh(raw_fast_cov)
    return PDEQuadrature(
        base_latent=base_latent.copy(),
        base_weights=base_weights.copy(),
        phi=phi.copy(),
        epsilon=epsilon.copy(),
        fast_weights=fast_weights.copy(),
        multi_indices=multi_indices,
        raw_basis_gram_error=float(
            np.linalg.norm(raw_basis_gram - np.eye(phi.shape[1]), ord=2)
        ),
        raw_basis_min_eigenvalue=float(raw_basis_eigenvalues[0]),
        raw_basis_max_eigenvalue=float(raw_basis_eigenvalues[-1]),
        raw_basis_condition=float(
            raw_basis_eigenvalues[-1] / raw_basis_eigenvalues[0]
        ),
        whitened_basis_gram_error=float(
            np.linalg.norm(phi_gram - np.eye(phi.shape[1]), ord=2)
        ),
        fast_mean_error=float(
            np.linalg.norm(np.sum(fast_weights[:, None] * epsilon, axis=0))
        ),
        raw_fast_min_eigenvalue=float(raw_fast_eigenvalues[0]),
        raw_fast_max_eigenvalue=float(raw_fast_eigenvalues[-1]),
        raw_fast_condition=float(
            raw_fast_eigenvalues[-1] / raw_fast_eigenvalues[0]
        ),
        fast_cov_error=float(
            np.linalg.norm(fast_cov - np.eye(epsilon.shape[1]), ord=2)
        ),
    )


def build_nested_quadratures(
    template: PDESpec,
    levels: Sequence[int] = DEFAULT_LEVELS,
    *,
    base_order: int = 4,
    master_levels: Sequence[int] | None = None,
) -> NestedQuadratureFamily:
    """Build compatible specifications and genuinely nested quadratures.

    With the scientific defaults and three input coordinates, the base rule
    has exactly ``4**4 = 256`` points.  One ``R x Pmaster`` scrambled Sobol
    Gaussian array is generated and block-whitened once.  The quadrature at
    every smaller P is a literal slice of the completed arrays.

    ``master_levels`` must include every level that may be activated later.
    This matters because a scrambled Sobol construction is dimension
    dependent: rebuilding a 35-dimensional family in 70 dimensions does not
    preserve its earlier coordinates.  Supplying the same predeclared master
    schedule makes later conditional extensions byte-stable.
    """

    levels = _validate_levels(levels)
    master_levels = _validate_levels(
        levels if master_levels is None else master_levels
    )
    if any(level not in master_levels for level in levels):
        raise ValueError("every active level must be a declared master level")
    pmax = master_levels[-1]
    latent_dim = template.X.shape[0] + 1
    base_latent, base_weights = _normal_hermite_tensor(base_order, latent_dim)
    if template.fast_points <= pmax:
        raise ValueError("fast_points must exceed the largest declared level")

    indices = _multi_indices(latent_dim, pmax)
    raw_phi_max = _eval_hermite_basis(base_latent, indices)
    phi_max = _block_orthonormalize(
        raw_phi_max, base_weights, master_levels, center=False
    )

    raw_epsilon = _normal_sobol(
        template.fast_points,
        pmax,
        template.quadrature_seed + 104729,
    )
    fast_weights = np.full(
        template.fast_points, 1.0 / template.fast_points, dtype=float
    )
    epsilon_max = _block_orthonormalize(
        raw_epsilon, fast_weights, master_levels, center=True
    )

    specs: dict[int, PDESpec] = {}
    quadratures: dict[int, PDEQuadrature] = {}
    for level in levels:
        spec = dataclasses.replace(
            template,
            basis_size=level,
            base_points=base_latent.shape[0],
        )
        spec.validate()
        specs[level] = spec
        quadratures[level] = _quadrature_record(
            base_latent=base_latent,
            base_weights=base_weights,
            raw_phi=raw_phi_max[:, :level],
            phi=phi_max[:, :level],
            raw_epsilon=raw_epsilon[:, :level],
            epsilon=epsilon_max[:, :level],
            fast_weights=fast_weights,
            multi_indices=indices[:level],
        )

    return NestedQuadratureFamily(
        levels=levels,
        master_levels=master_levels,
        specs=specs,
        quadratures=quadratures,
        raw_epsilon=raw_epsilon.copy(),
        base_order=base_order,
    )


def project_state(state: PDEState, target_level: int) -> PDEState:
    """Project a characteristic state onto its first ``target_level`` modes."""

    if not 1 <= target_level <= state.c.shape[-1]:
        raise ValueError("target_level must lie between one and the state level")
    return PDEState(
        B=state.B.copy(),
        a=state.a.copy(),
        c=state.c[..., :target_level].copy(),
    )


def lift_state(state: PDEState, target_level: int) -> PDEState:
    """Lift a state by retaining its prefix and zeroing learned high modes."""

    source_level = state.c.shape[-1]
    if target_level < source_level:
        raise ValueError("target_level cannot be smaller than the state level")
    c = np.zeros(state.c.shape[:-1] + (target_level,), dtype=state.c.dtype)
    c[..., :source_level] = state.c
    return PDEState(B=state.B.copy(), a=state.a.copy(), c=c)


def _norm_components(state: PDEState, quadrature: PDEQuadrature) -> StateNormComponents:
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    if state.B.shape[0] != wb.size or state.a.shape != (wb.size,):
        raise ValueError("state slow coordinates do not match the quadrature")
    if state.c.ndim != 4 or state.c.shape[0] < 1:
        raise ValueError("state coefficients must have shape (N,M,R,P)")
    if state.c.shape[1:3] != (wb.size, wf.size):
        raise ValueError("state coefficient coordinates do not match the quadrature")
    p = quadrature.phi.shape[1]
    if (
        quadrature.epsilon.ndim != 2
        or quadrature.epsilon.shape != (wf.size, p)
        or state.c.shape[-1] != p
    ):
        raise ValueError("state coefficient level does not match the quadrature")
    B2 = float(np.einsum("i,id,id->", wb, state.B, state.B, optimize=True))
    a2 = float(np.einsum("i,i,i->", wb, state.a, state.a, optimize=True))
    c2 = float(
        np.einsum(
            "i,r,lirp,lirp->",
            wb,
            wf,
            state.c,
            state.c,
            optimize=True,
        )
        / state.c.shape[0]
    )
    B = float(np.sqrt(max(B2, 0.0)))
    a = float(np.sqrt(max(a2, 0.0)))
    c = float(np.sqrt(max(c2, 0.0)))
    return StateNormComponents(
        B=B,
        a=a,
        c=c,
        total=float(np.sqrt(max(B2 + a2 + c2, 0.0))),
    )


def weighted_state_norm(
    state: PDEState,
    quadrature: PDEQuadrature,
    *,
    components: bool = False,
) -> float | StateNormComponents:
    """Weighted L2 norm, with uniform integration over continuous depth."""

    result = _norm_components(state, quadrature)
    return result if components else result.total


def _subtract(left: PDEState, right: PDEState) -> PDEState:
    if (
        left.B.shape != right.B.shape
        or left.a.shape != right.a.shape
        or left.c.shape != right.c.shape
    ):
        raise ValueError("states must have identical shapes")
    return PDEState(B=left.B - right.B, a=left.a - right.a, c=left.c - right.c)


def state_difference_norm(
    left: PDEState,
    right: PDEState,
    quadrature: PDEQuadrature,
    *,
    components: bool = False,
) -> float | StateNormComponents:
    return weighted_state_norm(
        _subtract(left, right), quadrature, components=components
    )


def _velocity_defect(
    left: PDEState, right: PDEState, quadrature: PDEQuadrature
) -> VelocityDefect:
    values = _norm_components(_subtract(left, right), quadrature)
    return VelocityDefect(
        Bdot=values.B, adot=values.a, cdot=values.c, total=values.total
    )


def _add_scaled(state: PDEState, direction: PDEState, scale: float) -> PDEState:
    return PDEState(
        B=state.B + scale * direction.B,
        a=state.a + scale * direction.a,
        c=state.c + scale * direction.c,
    )


def centered_observable_derivative(
    state: PDEState,
    direction: PDEState,
    spec: PDESpec,
    quadrature: PDEQuadrature,
    *,
    relative_step: float = 2e-6,
) -> ObservableDirectionalDerivative:
    """Centered finite-difference derivative of f, loss, and the Gram path."""

    if relative_step <= 0.0:
        raise ValueError("relative_step must be positive")
    direction_norm = float(weighted_state_norm(direction, quadrature))
    step = relative_step / max(1.0, direction_norm)
    plus = observe(_add_scaled(state, direction, step), spec, quadrature)
    minus = observe(_add_scaled(state, direction, -step), spec, quadrature)
    denominator = 2.0 * step
    return ObservableDirectionalDerivative(
        f=(plus.f - minus.f) / denominator,
        loss=float((plus.loss - minus.loss) / denominator),
        grams=(plus.grams - minus.grams) / denominator,
        step=step,
    )


def _observable_derivative_defect(
    left: ObservableDirectionalDerivative,
    right: ObservableDirectionalDerivative,
) -> ObservableDerivativeDefect:
    if left.f.shape != right.f.shape or left.grams.shape != right.grams.shape:
        raise ValueError("observable derivatives have incompatible shapes")
    f = float(np.linalg.norm(left.f - right.f))
    loss = abs(left.loss - right.loss)
    grams = float(
        np.linalg.norm(left.grams - right.grams)
        / np.sqrt(left.grams.shape[0])
    )
    return ObservableDerivativeDefect(
        f=f,
        loss=loss,
        grams=grams,
        total=float(np.sqrt(f * f + loss * loss + grams * grams)),
        left=left,
        right=right,
    )


def _compatible_pair(
    low_spec: PDESpec,
    high_spec: PDESpec,
    low_quadrature: PDEQuadrature,
    high_quadrature: PDEQuadrature,
) -> None:
    if low_spec.basis_size > high_spec.basis_size:
        raise ValueError("low level exceeds high level")
    scalar_names = (
        "depth_nodes",
        "base_points",
        "fast_points",
        "sigma_w",
        "A",
        "gamma",
        "activation",
    )
    if any(
        getattr(low_spec, name) != getattr(high_spec, name)
        for name in scalar_names
    ):
        raise ValueError("PDE specifications differ outside basis_size")
    if not np.array_equal(low_spec.X, high_spec.X) or not np.array_equal(
        low_spec.y, high_spec.y
    ):
        raise ValueError("PDE data differ across levels")
    p = low_spec.basis_size
    if not np.array_equal(low_quadrature.base_latent, high_quadrature.base_latent):
        raise ValueError("base quadratures are not common")
    if not np.array_equal(low_quadrature.base_weights, high_quadrature.base_weights):
        raise ValueError("base weights are not common")
    if not np.array_equal(low_quadrature.fast_weights, high_quadrature.fast_weights):
        raise ValueError("fast weights are not common")
    if not np.array_equal(low_quadrature.phi, high_quadrature.phi[:, :p]):
        raise ValueError("Hermite basis is not a literal prefix")
    if not np.array_equal(low_quadrature.epsilon, high_quadrature.epsilon[:, :p]):
        raise ValueError("fast Gaussian array is not a literal prefix")


def generator_diagnostics(
    low_state: PDEState,
    high_state: PDEState,
    low_spec: PDESpec,
    high_spec: PDESpec,
    low_quadrature: PDEQuadrature,
    high_quadrature: PDEQuadrature,
    *,
    finite_difference_step: float = 2e-6,
) -> GeneratorDiagnostics:
    """Compute lift consistency, outgoing tail, and high-to-low feedback."""

    _compatible_pair(low_spec, high_spec, low_quadrature, high_quadrature)
    p = low_spec.basis_size
    pmax = high_spec.basis_size
    if low_state.c.shape[-1] != p or high_state.c.shape[-1] != pmax:
        raise ValueError("state levels do not match their specifications")

    low_velocity, _ = vector_field(low_state, low_spec, low_quadrature)
    lifted_low = lift_state(low_state, pmax)
    lifted_high_velocity, _ = vector_field(
        lifted_low, high_spec, high_quadrature
    )
    projected_lift_velocity = project_state(lifted_high_velocity, p)
    lift_consistency = _velocity_defect(
        projected_lift_velocity, low_velocity, low_quadrature
    )

    lift_outgoing = PDEState(
        B=np.zeros_like(lifted_high_velocity.B),
        a=np.zeros_like(lifted_high_velocity.a),
        c=lifted_high_velocity.c.copy(),
    )
    lift_outgoing.c[..., :p] = 0.0
    lift_outgoing_high_cdot = float(
        weighted_state_norm(lift_outgoing, high_quadrature)
    )

    high_velocity, _ = vector_field(high_state, high_spec, high_quadrature)
    outgoing = PDEState(
        B=np.zeros_like(high_velocity.B),
        a=np.zeros_like(high_velocity.a),
        c=high_velocity.c.copy(),
    )
    outgoing.c[..., :p] = 0.0
    outgoing_high_cdot = float(weighted_state_norm(outgoing, high_quadrature))
    projected_high_state = project_state(high_state, p)
    projected_high_velocity = project_state(high_velocity, p)
    low_from_high_velocity, _ = vector_field(
        projected_high_state, low_spec, low_quadrature
    )
    feedback = _velocity_defect(
        projected_high_velocity, low_from_high_velocity, low_quadrature
    )

    lift_obs_projected = centered_observable_derivative(
        low_state,
        projected_lift_velocity,
        low_spec,
        low_quadrature,
        relative_step=finite_difference_step,
    )
    lift_obs_full = centered_observable_derivative(
        lifted_low,
        lifted_high_velocity,
        high_spec,
        high_quadrature,
        relative_step=finite_difference_step,
    )
    lift_obs_low = centered_observable_derivative(
        low_state,
        low_velocity,
        low_spec,
        low_quadrature,
        relative_step=finite_difference_step,
    )
    feedback_obs_projected = centered_observable_derivative(
        projected_high_state,
        projected_high_velocity,
        low_spec,
        low_quadrature,
        relative_step=finite_difference_step,
    )
    feedback_obs_full = centered_observable_derivative(
        high_state,
        high_velocity,
        high_spec,
        high_quadrature,
        relative_step=finite_difference_step,
    )
    feedback_obs_low = centered_observable_derivative(
        projected_high_state,
        low_from_high_velocity,
        low_spec,
        low_quadrature,
        relative_step=finite_difference_step,
    )

    return GeneratorDiagnostics(
        low_level=p,
        high_level=pmax,
        lift_consistency=lift_consistency,
        lift_outgoing_high_cdot=lift_outgoing_high_cdot,
        outgoing_high_cdot=outgoing_high_cdot,
        high_to_low_feedback=feedback,
        lift_observable_defect=_observable_derivative_defect(
            lift_obs_projected, lift_obs_low
        ),
        feedback_observable_defect=_observable_derivative_defect(
            feedback_obs_projected, feedback_obs_low
        ),
        lift_full_observable_defect=_observable_derivative_defect(
            lift_obs_full, lift_obs_low
        ),
        feedback_full_observable_defect=_observable_derivative_defect(
            feedback_obs_full, feedback_obs_low
        ),
    )


def shadow_restart(
    high_state: PDEState,
    low_spec: PDESpec,
    high_spec: PDESpec,
    low_quadrature: PDEQuadrature,
    high_quadrature: PDEQuadrature,
    *,
    dt: float,
    steps: int,
) -> ShadowRestart:
    """Restart P and Pmax from the same projected high state for a short time."""

    _compatible_pair(low_spec, high_spec, low_quadrature, high_quadrature)
    if dt <= 0.0 or steps < 0:
        raise ValueError("dt must be positive and steps must be nonnegative")
    low_state = project_state(high_state, low_spec.basis_size)
    high = high_state.copy()
    low = low_state.copy()
    times = np.arange(steps + 1, dtype=float) * dt
    state_defect = np.empty(steps + 1, dtype=float)
    f_defect = np.empty(steps + 1, dtype=float)
    loss_defect = np.empty(steps + 1, dtype=float)
    gram_defect = np.empty(steps + 1, dtype=float)

    for index in range(steps + 1):
        high_observable = observe(high, high_spec, high_quadrature)
        low_observable = observe(low, low_spec, low_quadrature)
        state_defect[index] = float(
            state_difference_norm(
                project_state(high, low_spec.basis_size),
                low,
                low_quadrature,
            )
        )
        f_defect[index] = np.linalg.norm(
            high_observable.f - low_observable.f
        )
        loss_defect[index] = abs(
            high_observable.loss - low_observable.loss
        )
        gram_defect[index] = (
            np.linalg.norm(high_observable.grams - low_observable.grams)
            / np.sqrt(high_observable.grams.shape[0])
        )
        if index < steps:
            high = rk4_step(high, dt, high_spec, high_quadrature)
            low = rk4_step(low, dt, low_spec, low_quadrature)

    arrays = (state_defect, f_defect, loss_defect, gram_defect)
    if not all(np.all(np.isfinite(array)) for array in arrays):
        raise FloatingPointError("nonfinite value in shadow restart")
    return ShadowRestart(
        times=times,
        state_defect=state_defect,
        f_defect=f_defect,
        loss_defect=loss_defect,
        gram_defect=gram_defect,
    )


def _canonicalize_columns(matrix: Array) -> Array:
    result = matrix.copy()
    for column in range(result.shape[1]):
        pivot = int(np.argmax(np.abs(result[:, column])))
        if result[pivot, column] < 0.0:
            result[:, column] *= -1.0
    return result


def hermite_subspace(pmax: int, rank: int) -> Array:
    """Coefficient matrix for the first ``rank`` fixed Hermite functions."""

    if not 1 <= rank <= pmax:
        raise ValueError("rank must lie between one and pmax")
    return np.eye(pmax, dtype=float)[:, :rank]


def random_subspace(pmax: int, rank: int, *, seed: int) -> Array:
    """Seeded Haar-like coefficient subspace."""

    if not 1 <= rank <= pmax:
        raise ValueError("rank must lie between one and pmax")
    raw = np.random.default_rng(seed).normal(size=(pmax, rank))
    q, _ = np.linalg.qr(raw, mode="reduced")
    return _canonicalize_columns(q)


def trajectory_pod_subspace(
    states: Sequence[PDEState],
    quadrature: PDEQuadrature,
    rank: int,
    *,
    operators: Sequence[PDEState] = (),
) -> Array:
    """Weighted POD of learned coefficient states and optional velocities."""

    records = tuple(states) + tuple(operators)
    if not records:
        raise ValueError("at least one state or operator snapshot is required")
    pmax = records[0].c.shape[-1]
    if not 1 <= rank <= pmax:
        raise ValueError("rank must lie between one and the snapshot level")
    covariance = np.zeros((pmax, pmax), dtype=float)
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    for record in records:
        if record.c.shape[-1] != pmax:
            raise ValueError("all POD snapshots must have the same level")
        covariance += np.einsum(
            "i,r,lirp,lirq->pq",
            wb,
            wf,
            record.c,
            record.c,
            optimize=True,
        ) / record.c.shape[0]
    covariance = 0.5 * (covariance + covariance.T)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    order = np.argsort(eigenvalues, kind="stable")[::-1]
    return _canonicalize_columns(eigenvectors[:, order[:rank]])


def _coefficient_subspace(
    subspace: Array,
    quadrature: PDEQuadrature,
    *,
    tolerance: float = 2e-10,
) -> Array:
    """Accept coefficient columns or weighted-orthonormal base-grid values."""

    subspace = np.asarray(subspace, dtype=float)
    if subspace.ndim != 2:
        raise ValueError("subspace must be a matrix")
    pmax = quadrature.phi.shape[1]
    if subspace.shape[0] == pmax:
        coefficients = subspace.copy()
    elif subspace.shape[0] == quadrature.phi.shape[0]:
        wb = quadrature.base_weights
        weighted_gram = subspace.T @ (wb[:, None] * subspace)
        if np.linalg.norm(
            weighted_gram - np.eye(subspace.shape[1]), ord=2
        ) > tolerance:
            raise ValueError("base-grid subspace is not weighted orthonormal")
        coefficients = quadrature.phi.T @ (wb[:, None] * subspace)
        reconstruction = quadrature.phi @ coefficients
        residual = np.sqrt(
            np.sum(wb[:, None] * (subspace - reconstruction) ** 2)
        )
        if residual > tolerance:
            raise ValueError("subspace lies outside the Pmax Hermite span")
    else:
        raise ValueError("subspace has neither coefficient nor base-grid shape")
    gram = coefficients.T @ coefficients
    if np.linalg.norm(gram - np.eye(coefficients.shape[1]), ord=2) > tolerance:
        raise ValueError("subspace columns are not orthonormal")
    return coefficients


def restrict_to_subspace(
    high_state: PDEState,
    high_spec: PDESpec,
    high_quadrature: PDEQuadrature,
    subspace: Array,
) -> RestrictedSystem:
    """Restrict the state and both orientations of the operator to Q."""

    coefficients = _coefficient_subspace(subspace, high_quadrature)
    rank = coefficients.shape[1]
    if high_state.c.shape[-1] != coefficients.shape[0]:
        raise ValueError("state and subspace have different maximum levels")
    phi = high_quadrature.phi @ coefficients
    epsilon = high_quadrature.epsilon @ coefficients
    state = PDEState(
        B=high_state.B.copy(),
        a=high_state.a.copy(),
        c=np.einsum(
            "lirp,pk->lirk", high_state.c, coefficients, optimize=True
        ),
    )
    spec = dataclasses.replace(high_spec, basis_size=rank)
    spec.validate()
    quadrature = _quadrature_record(
        base_latent=high_quadrature.base_latent,
        base_weights=high_quadrature.base_weights,
        raw_phi=phi,
        phi=phi,
        raw_epsilon=epsilon,
        epsilon=epsilon,
        fast_weights=high_quadrature.fast_weights,
        # These indices are metadata only for a rotated basis.
        multi_indices=high_quadrature.multi_indices[:rank],
    )
    return RestrictedSystem(
        state=state,
        spec=spec,
        quadrature=quadrature,
        coefficients=coefficients,
    )


def basis_diagnostic(
    high_state: PDEState,
    high_spec: PDESpec,
    high_quadrature: PDEQuadrature,
    subspace: Array,
    *,
    finite_difference_step: float = 2e-6,
) -> BasisDiagnostic:
    """High-to-subspace state, generator, feedback, and observable defects."""

    restricted = restrict_to_subspace(
        high_state, high_spec, high_quadrature, subspace
    )
    q = restricted.coefficients
    projector = q @ q.T
    reconstructed_c = np.einsum(
        "lirk,kp->lirp", restricted.state.c, q.T, optimize=True
    )
    state_tail_record = PDEState(
        B=np.zeros_like(high_state.B),
        a=np.zeros_like(high_state.a),
        c=high_state.c - reconstructed_c,
    )
    state_tail = float(weighted_state_norm(state_tail_record, high_quadrature))

    high_velocity, _ = vector_field(high_state, high_spec, high_quadrature)
    restricted_velocity, _ = vector_field(
        restricted.state, restricted.spec, restricted.quadrature
    )
    projected_high_velocity = PDEState(
        B=high_velocity.B.copy(),
        a=high_velocity.a.copy(),
        c=np.einsum(
            "lirp,pk->lirk", high_velocity.c, q, optimize=True
        ),
    )
    feedback = _velocity_defect(
        projected_high_velocity,
        restricted_velocity,
        restricted.quadrature,
    )
    generator_tail_record = PDEState(
        B=np.zeros_like(high_velocity.B),
        a=np.zeros_like(high_velocity.a),
        c=np.einsum(
            "lirp,pq->lirq",
            high_velocity.c,
            np.eye(q.shape[0]) - projector,
            optimize=True,
        ),
    )
    generator_tail = float(
        weighted_state_norm(generator_tail_record, high_quadrature)
    )

    high_observable_derivative = centered_observable_derivative(
        high_state,
        high_velocity,
        high_spec,
        high_quadrature,
        relative_step=finite_difference_step,
    )
    restricted_observable_derivative = centered_observable_derivative(
        restricted.state,
        restricted_velocity,
        restricted.spec,
        restricted.quadrature,
        relative_step=finite_difference_step,
    )
    observable_defect = _observable_derivative_defect(
        high_observable_derivative, restricted_observable_derivative
    )
    values: Iterable[float] = (
        state_tail,
        generator_tail,
        feedback.total,
        observable_defect.total,
    )
    if not all(np.isfinite(value) for value in values):
        raise FloatingPointError("nonfinite basis diagnostic")
    return BasisDiagnostic(
        rank=q.shape[1],
        state_tail=state_tail,
        generator_tail=generator_tail,
        feedback=feedback,
        observable_defect=observable_defect,
    )


def build_subspace_basis(
    kind: str,
    *,
    pmax: int,
    rank: int,
    seed: int | None = None,
    states: Sequence[PDEState] = (),
    quadrature: PDEQuadrature | None = None,
    operators: Sequence[PDEState] = (),
) -> Array:
    """Dispatch fixed-Hermite, seeded-random, or trajectory-POD bases."""

    normalized = kind.strip().lower().replace("_", "-")
    if normalized in {"hermite", "fixed-hermite"}:
        return hermite_subspace(pmax, rank)
    if normalized in {"random", "seeded-random"}:
        if seed is None:
            raise ValueError("a seed is required for a random subspace")
        return random_subspace(pmax, rank, seed=seed)
    if normalized in {"pod", "trajectory-pod"}:
        if quadrature is None:
            raise ValueError("quadrature is required for trajectory POD")
        return trajectory_pod_subspace(
            states, quadrature, rank, operators=operators
        )
    raise ValueError(f"unknown subspace kind {kind!r}")
