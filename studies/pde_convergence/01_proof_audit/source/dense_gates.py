"""Dense-network gates for the neural-PDE proof-obligation audit.

This module deliberately reuses the canonical dense residual-network dynamics
from ``activation_linearity_smoking_gun/source/src``.  It adds only diagnostic
infrastructure:

* coupled Gaussian initializations for honest width/depth Cauchy studies;
* checkpointed RK4 trajectories with the full hidden Gram and NTK paths;
* a model-free, paired depth-homogenization estimator; and
* an adversarial same-compressed-state continuation test.

No PDE prediction enters any calculation in this file.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys
from typing import Iterable, Mapping

import numpy as np


# Import the frozen canonical implementation rather than copying its dynamics.
_CANONICAL_SRC = (
    Path(__file__).resolve().parents[2]
    / "activation_linearity_smoking_gun"
    / "source"
    / "src"
)
if not _CANONICAL_SRC.is_dir():
    raise ImportError(f"canonical dense source is missing: {_CANONICAL_SRC}")
if str(_CANONICAL_SRC) not in sys.path:
    sys.path.insert(0, str(_CANONICAL_SRC))

from activations import get_activation  # noqa: E402
from dense_reference import (  # noqa: E402
    FieldState,
    ModelSpec,
    ParamState,
    forward_adjoint,
    parameter_vector_field,
    rk4_param_step,
    tangent_kernel,
)
from dense_pde.operator_galerkin import (  # noqa: E402
    _eval_hermite_basis,
    _multi_indices,
)


Array = np.ndarray


def _copy_state(state: ParamState) -> ParamState:
    return ParamState(state.B.copy(), state.W.copy(), state.a.copy())


def _shift_state(
    state: ParamState,
    velocity: ParamState,
    scale: float,
) -> ParamState:
    return ParamState(
        B=state.B + scale * velocity.B,
        W=state.W + scale * velocity.W,
        a=state.a + scale * velocity.a,
    )


@dataclass(frozen=True)
class GaussianMaster:
    """Unscaled standard-Gaussian arrays underlying a coupled model family."""

    seed: int
    n_max: int
    depth_max: int
    input_dim: int
    B_standard: Array
    W_standard: Array
    a_standard: Array

    def validate(self) -> None:
        if self.n_max < 1 or self.depth_max < 1 or self.input_dim < 1:
            raise ValueError("master dimensions must be positive")
        if self.B_standard.shape != (self.n_max, self.input_dim):
            raise ValueError("invalid master B shape")
        if self.W_standard.shape != (
            self.depth_max,
            self.n_max,
            self.n_max,
        ):
            raise ValueError("invalid master W shape")
        if self.a_standard.shape != (self.n_max,):
            raise ValueError("invalid master a shape")
        for array in (self.B_standard, self.W_standard, self.a_standard):
            if not np.all(np.isfinite(array)):
                raise ValueError("master arrays must be finite")


def initialize_gaussian_master(
    *,
    n_max: int,
    depth_max: int,
    input_dim: int,
    seed: int,
) -> GaussianMaster:
    """Draw deterministic master arrays in one documented RNG order.

    ``W_standard`` is *unscaled*: every entry is standard normal.  Width
    ``n`` is materialized by taking top-left blocks and multiplying by
    ``sigma_w/sqrt(n)``.  This is the only valid way to share the same
    underlying Gaussian entries while retaining the correct law at every
    width.
    """

    if n_max < 1 or depth_max < 1 or input_dim < 1:
        raise ValueError("n_max, depth_max, and input_dim must be positive")
    rng = np.random.default_rng(seed)
    master = GaussianMaster(
        seed=int(seed),
        n_max=int(n_max),
        depth_max=int(depth_max),
        input_dim=int(input_dim),
        B_standard=rng.normal(size=(n_max, input_dim)),
        W_standard=rng.normal(size=(depth_max, n_max, n_max)),
        a_standard=rng.normal(size=n_max),
    )
    master.validate()
    return master


def materialize_coupled_state(
    master: GaussianMaster,
    spec: ModelSpec,
) -> ParamState:
    """Materialize one width/depth member of a nested Gaussian family.

    Width coupling uses prefixes of ``B`` and ``a`` and top-left blocks of the
    same standard-Gaussian ``W`` array.  If ``q=depth_max/depth``, coarse
    standard-normal layer ``ell`` is

    ``sum_{j=0}^{q-1} Z[q*ell+j] / sqrt(q)``.

    Thus a coarse layer has the right marginal law while being exactly coupled
    to the corresponding consecutive fine layers.
    """

    master.validate()
    spec.validate()
    if spec.n > master.n_max:
        raise ValueError("requested width exceeds the master width")
    if spec.X.shape[0] != master.input_dim:
        raise ValueError("spec input dimension disagrees with master")
    if master.depth_max % spec.depth:
        raise ValueError("requested depth must divide master.depth_max")

    block = master.depth_max // spec.depth
    standard = master.W_standard.reshape(
        spec.depth,
        block,
        master.n_max,
        master.n_max,
    ).sum(axis=1) / np.sqrt(float(block))
    return ParamState(
        B=master.B_standard[: spec.n].copy(),
        W=(
            spec.sigma_w
            / np.sqrt(float(spec.n))
            * standard[:, : spec.n, : spec.n]
        ).copy(),
        a=(spec.A * master.a_standard[: spec.n]).copy(),
    )


@dataclass(frozen=True)
class DenseTrajectory:
    """Checkpoint states and observable paths from an RK4 integration."""

    times: Array
    states: tuple[ParamState, ...]
    f: Array
    gram: Array
    theta: Array

    @property
    def final_state(self) -> ParamState:
        return self.states[-1]


def _observables(state: ParamState, spec: ModelSpec) -> tuple[Array, Array, Array]:
    fields = forward_adjoint(state, spec)
    f = state.a @ fields.H[-1] / spec.n
    gram = np.einsum("lnr,lns->lrs", fields.H, fields.H) / spec.n
    theta = tangent_kernel(
        FieldState(state.W, state.a, fields.H, fields.P),
        spec,
    )
    return f, gram, theta


def simulate_checkpoints(
    state: ParamState,
    spec: ModelSpec,
    checkpoint_times: Iterable[float],
    *,
    dt: float,
    start_time: float = 0.0,
) -> DenseTrajectory:
    """Integrate to exact checkpoint times and retain restartable states.

    A final fractional RK4 step is used when a checkpoint is not an integer
    multiple of ``dt``.  The input state is never mutated.
    """

    spec.validate()
    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be positive and finite")
    if not np.isfinite(start_time):
        raise ValueError("start_time must be finite")
    times = np.asarray(tuple(float(t) for t in checkpoint_times), dtype=float)
    if times.ndim != 1 or times.size == 0:
        raise ValueError("at least one checkpoint is required")
    if not np.all(np.isfinite(times)):
        raise ValueError("checkpoint times must be finite")
    if np.any(np.diff(times) <= 0.0):
        raise ValueError("checkpoint times must be strictly increasing")
    tolerance = 64.0 * np.finfo(float).eps * max(
        1.0,
        abs(start_time),
        float(np.max(np.abs(times))),
    )
    if times[0] < start_time - tolerance:
        raise ValueError("a checkpoint precedes start_time")

    current = _copy_state(state)
    current_time = float(start_time)
    stored_states: list[ParamState] = []
    f_path: list[Array] = []
    gram_path: list[Array] = []
    theta_path: list[Array] = []

    for target in times:
        while current_time < target - tolerance:
            step = min(dt, target - current_time)
            current = rk4_param_step(current, float(step), spec)
            current_time += step
        current_time = float(target)
        snapshot = _copy_state(current)
        f, gram, theta = _observables(snapshot, spec)
        stored_states.append(snapshot)
        f_path.append(f)
        gram_path.append(gram)
        theta_path.append(theta)

    return DenseTrajectory(
        times=times,
        states=tuple(stored_states),
        f=np.stack(f_path),
        gram=np.stack(gram_path),
        theta=np.stack(theta_path),
    )


@dataclass(frozen=True)
class HomogenizationStats:
    """Model-free depth-cancellation statistics at one physical depth.

    ``mean_bias_rms`` is retained as a compatibility name, but it is only the
    contrast between this depth's ensemble mean and an in-sample pooled mean.
    It is *not* an estimator of bias in the PDE conditional/Onsager mean.
    """

    depth: int
    mean_residual: Array
    mean_bias_rms: float
    variance: float
    rms: float
    cross_depth_covariance: Array
    integrated_cross_depth_covariance: float


@dataclass(frozen=True)
class HomogenizationCheckpoint:
    """Forward/backward statistics and fitted depth exponents."""

    time: float
    forward: Mapping[int, HomogenizationStats]
    backward: Mapping[int, HomogenizationStats]
    forward_bias_slope: float
    forward_variance_slope: float
    forward_rms_slope: float
    backward_bias_slope: float
    backward_variance_slope: float
    backward_rms_slope: float


@dataclass(frozen=True)
class HomogenizationReport:
    """Complete paired, model-free homogenization audit."""

    depths: tuple[int, ...]
    ensemble_size: int
    checkpoints: Mapping[float, HomogenizationCheckpoint]
    pooled_mean_definition: str
    shared_B: Array
    shared_a: Array


def _layer_actions(state: ParamState, spec: ModelSpec) -> tuple[Array, Array]:
    fields = forward_adjoint(state, spec)
    forward = fields.T.copy()
    backward = np.empty_like(forward)
    for ell in range(spec.depth):
        beta = fields.D[ell] * fields.P[ell + 1]
        backward[ell] = state.W[ell].T @ beta
    return forward, backward


def _align_layers(actions: Array, depth_max: int) -> Array:
    depth = actions.shape[0]
    if depth_max % depth:
        raise ValueError("depth must divide the finest depth")
    return np.repeat(actions, depth_max // depth, axis=0)


def _innovation_stats(
    aligned_actions: Array,
    pooled_mean: Array,
    depth: int,
) -> HomogenizationStats:
    """Contract residual layer fields without hiding cross-depth covariance."""

    residual_aligned = aligned_actions - pooled_mean[None, ...]
    fine_depth = residual_aligned.shape[1]
    if fine_depth % depth:
        raise ValueError("native depth does not divide aligned depth")
    block = fine_depth // depth
    residual = residual_aligned.reshape(
        residual_aligned.shape[0],
        depth,
        block,
        *residual_aligned.shape[2:],
    ).mean(axis=2)
    residual_average = residual.mean(axis=1)
    mean_residual = residual_average.mean(axis=0)
    mean_bias_rms = float(np.sqrt(np.mean(mean_residual * mean_residual)))

    centered_average = residual_average - mean_residual[None, ...]
    count = aligned_actions.shape[0]
    if count < 2:
        raise ValueError("at least two resamples are required")
    components = int(np.prod(centered_average.shape[1:]))
    variance = float(
        np.sum(centered_average * centered_average)
        / ((count - 1) * components)
    )

    centered_layers = residual - residual.mean(axis=0, keepdims=True)
    flat = centered_layers.reshape(count, centered_layers.shape[1], -1)
    covariance = np.einsum("rlc,rkc->lk", flat, flat)
    covariance /= float((count - 1) * flat.shape[2])
    integrated = float(np.mean(covariance))

    # This equality is an internal accounting identity: the double covariance
    # sum is precisely the variance of the depth-averaged innovation.
    if not np.isclose(integrated, variance, rtol=2e-12, atol=2e-14):
        raise RuntimeError("cross-depth covariance accounting failed")

    return HomogenizationStats(
        depth=depth,
        mean_residual=mean_residual,
        mean_bias_rms=mean_bias_rms,
        variance=variance,
        rms=float(np.sqrt(max(variance, 0.0))),
        cross_depth_covariance=covariance,
        integrated_cross_depth_covariance=integrated,
    )


def _fitted_log_slope(depths: tuple[int, ...], values: list[float]) -> float:
    x = np.asarray(depths, dtype=float)
    y = np.asarray(values, dtype=float)
    mask = np.isfinite(y) & (y > 32.0 * np.finfo(float).tiny)
    if np.count_nonzero(mask) < 2:
        return float("nan")
    return float(np.polyfit(np.log(x[mask]), np.log(y[mask]), 1)[0])


def estimate_depth_homogenization(
    base_spec: ModelSpec,
    *,
    depths: Iterable[int],
    ensemble_size: int,
    seed: int,
    checkpoints: Iterable[float] = (0.0, 0.5),
    dt: float = 0.02,
) -> HomogenizationReport:
    """Estimate model-free trained depth cancellation without a PDE mean.

    One ``B,a`` draw is shared by every member.  Each ensemble member resamples
    an independent finest-depth ``W`` family; all requested depths within that
    member are coupled by normalized consecutive-block sums.  Layer actions are
    lifted to the finest grid.  Their equal-depth/equal-replicate pooled mean is
    a common centering reference for comparing the raw actions.

    The report separates the depth-to-pooled mean contrast from centered
    variance and retains the complete cross-depth covariance matrix.  Because
    the same samples define the pooled mean, this function cannot detect a
    common missing conditional/Onsager term.  That candidate-specific bias
    requires an explicit per-member predictor or a held-out cross-fit.
    """

    base_spec.validate()
    depth_tuple = tuple(sorted({int(depth) for depth in depths}))
    if len(depth_tuple) < 2 or depth_tuple[0] < 1:
        raise ValueError("at least two positive depths are required")
    depth_max = depth_tuple[-1]
    if any(depth_max % depth for depth in depth_tuple):
        raise ValueError("every depth must divide the finest depth")
    if ensemble_size < 2:
        raise ValueError("ensemble_size must be at least two")

    checkpoint_tuple = tuple(float(t) for t in checkpoints)
    if checkpoint_tuple != tuple(sorted(set(checkpoint_tuple))):
        raise ValueError("checkpoints must be unique and sorted")
    if not checkpoint_tuple or checkpoint_tuple[0] < 0.0:
        raise ValueError("checkpoints must be nonempty and nonnegative")

    base_master = initialize_gaussian_master(
        n_max=base_spec.n,
        depth_max=depth_max,
        input_dim=base_spec.X.shape[0],
        seed=seed,
    )
    shared_B = base_master.B_standard.copy()
    shared_a = base_spec.A * base_master.a_standard.copy()

    records: dict[
        float,
        dict[str, dict[int, list[Array]]],
    ] = {
        time: {
            "forward": {depth: [] for depth in depth_tuple},
            "backward": {depth: [] for depth in depth_tuple},
        }
        for time in checkpoint_tuple
    }

    seed_sequence = np.random.SeedSequence([int(seed), 0x484F4D])
    child_sequences = seed_sequence.spawn(ensemble_size)
    for child in child_sequences:
        W_standard = np.random.default_rng(child).normal(
            size=(depth_max, base_spec.n, base_spec.n)
        )
        master = GaussianMaster(
            seed=int(child.generate_state(1, dtype=np.uint64)[0]),
            n_max=base_spec.n,
            depth_max=depth_max,
            input_dim=base_spec.X.shape[0],
            B_standard=base_master.B_standard,
            W_standard=W_standard,
            a_standard=base_master.a_standard,
        )
        for depth in depth_tuple:
            spec = replace(base_spec, depth=depth)
            state = materialize_coupled_state(master, spec)
            trajectory = simulate_checkpoints(
                state,
                spec,
                checkpoint_tuple,
                dt=dt,
            )
            for index, time in enumerate(checkpoint_tuple):
                forward, backward = _layer_actions(
                    trajectory.states[index],
                    spec,
                )
                records[time]["forward"][depth].append(
                    _align_layers(forward, depth_max)
                )
                records[time]["backward"][depth].append(
                    _align_layers(backward, depth_max)
                )

    checkpoint_reports: dict[float, HomogenizationCheckpoint] = {}
    for time in checkpoint_tuple:
        kind_reports: dict[str, dict[int, HomogenizationStats]] = {}
        slopes: dict[str, tuple[float, float, float]] = {}
        for kind in ("forward", "backward"):
            arrays = {
                depth: np.stack(records[time][kind][depth])
                for depth in depth_tuple
            }
            pooled = np.mean(
                np.concatenate([arrays[depth] for depth in depth_tuple], axis=0),
                axis=0,
            )
            stats = {
                depth: _innovation_stats(arrays[depth], pooled, depth)
                for depth in depth_tuple
            }
            kind_reports[kind] = stats
            bias_slope = _fitted_log_slope(
                depth_tuple,
                [stats[depth].mean_bias_rms for depth in depth_tuple],
            )
            variance_slope = _fitted_log_slope(
                depth_tuple,
                [stats[depth].variance for depth in depth_tuple],
            )
            rms_slope = _fitted_log_slope(
                depth_tuple,
                [stats[depth].rms for depth in depth_tuple],
            )
            slopes[kind] = (bias_slope, variance_slope, rms_slope)

        checkpoint_reports[time] = HomogenizationCheckpoint(
            time=time,
            forward=kind_reports["forward"],
            backward=kind_reports["backward"],
            forward_bias_slope=slopes["forward"][0],
            forward_variance_slope=slopes["forward"][1],
            forward_rms_slope=slopes["forward"][2],
            backward_bias_slope=slopes["backward"][0],
            backward_variance_slope=slopes["backward"][1],
            backward_rms_slope=slopes["backward"][2],
        )

    return HomogenizationReport(
        depths=depth_tuple,
        ensemble_size=ensemble_size,
        checkpoints=checkpoint_reports,
        pooled_mean_definition=(
            "in-sample equal-depth/equal-resample centering mean on the "
            "finest normalized-depth grid; not a conditional/Onsager mean"
        ),
        shared_B=shared_B,
        shared_a=shared_a,
    )


def empirical_hermite_phi(
    initialization_state: ParamState,
    *,
    basis_size: int,
    readout_scale: float = 1.0,
) -> Array:
    """Evaluate the nested Hermite family on the empirical immutable labels.

    The immutable labels are ``theta_i=(B_i(0),a_i(0)/A)``.  Raw
    probabilists' Hermites are enumerated by total degree in exactly the same
    order as the operator--Galerkin PDE.  Division by ``sqrt(n)`` gives the
    Euclidean design convention used by the invisible-state constraints.
    Callers that need an empirical orthogonal projector must orthonormalize
    this span; retaining the literal Hermite columns avoids silently rotating
    the compressed coordinates at finite width.
    """

    if initialization_state.B.ndim != 2:
        raise ValueError("initial B must be a matrix")
    n, input_dim = initialization_state.B.shape
    if initialization_state.a.shape != (n,):
        raise ValueError("initial B and a disagree on width")
    if not 1 <= basis_size <= n:
        raise ValueError("basis_size must lie between one and the width")
    if not np.isfinite(readout_scale) or readout_scale <= 0.0:
        raise ValueError("readout_scale must be positive and finite")
    labels = np.column_stack(
        (initialization_state.B, initialization_state.a / readout_scale)
    )
    indices = _multi_indices(input_dim + 1, basis_size)
    raw = _eval_hermite_basis(labels, indices)
    phi = raw / np.sqrt(float(n))
    if np.linalg.matrix_rank(phi) != basis_size:
        raise ValueError("empirical Hermite design is rank deficient")
    return phi


def empirical_degree_one_hermite_phi(
    initialization_state: ParamState,
    *,
    readout_scale: float = 1.0,
) -> Array:
    """Return the complete degree-one basis for the canonical d=3 model."""

    if initialization_state.B.shape[1] != 3:
        raise ValueError("the requested degree-one P=5 basis requires d=3")
    return empirical_hermite_phi(
        initialization_state,
        basis_size=5,
        readout_scale=readout_scale,
    )


def retained_row_coefficients(W: Array, phi: Array) -> Array:
    """Return the retained row coefficients ``W @ Phi``."""

    if W.ndim != 2 or phi.ndim != 2 or W.shape[1] != phi.shape[0]:
        raise ValueError("W and Phi shapes are incompatible")
    return W @ phi


def _orthonormal_span(matrix: Array) -> Array:
    if matrix.ndim != 2:
        raise ValueError("span input must be a matrix")
    if matrix.shape[1] == 0:
        return np.empty((matrix.shape[0], 0), dtype=float)
    U, singular_values, _ = np.linalg.svd(matrix, full_matrices=False)
    if singular_values.size == 0:
        return np.empty((matrix.shape[0], 0), dtype=float)
    tolerance = (
        max(matrix.shape)
        * np.finfo(float).eps
        * max(float(singular_values[0]), 1.0)
    )
    return U[:, singular_values > tolerance]


def _project_off(span: Array, vector: Array) -> Array:
    if span.shape[1]:
        vector = vector - span @ (span.T @ vector)
        # A second pass suppresses roundoff for nearly dependent constraints.
        vector = vector - span @ (span.T @ vector)
    return vector


def _structured_candidates(
    sources: Mapping[str, Array],
    forbidden_span: Array,
    *,
    rng: np.random.Generator,
    limit: int,
) -> list[tuple[str, Array]]:
    candidates: list[tuple[str, Array]] = []
    for name, source in sources.items():
        if source.ndim == 1:
            source = source[:, None]
        projected = source - forbidden_span @ (forbidden_span.T @ source)
        if forbidden_span.shape[1]:
            projected -= forbidden_span @ (forbidden_span.T @ projected)
        if np.linalg.norm(projected) <= 1e-13:
            continue
        left, singular_values, _ = np.linalg.svd(projected, full_matrices=False)
        if singular_values.size and singular_values[0] > 1e-13:
            candidates.append((f"{name}:sv1", left[:, 0]))
        column_norms = np.linalg.norm(projected, axis=0)
        if column_norms.size and float(np.max(column_norms)) > 1e-13:
            index = int(np.argmax(column_norms))
            candidates.append(
                (f"{name}:column{index}", projected[:, index] / column_norms[index])
            )

    fallback = _project_off(
        forbidden_span,
        rng.normal(size=forbidden_span.shape[0]),
    )
    fallback_norm = float(np.linalg.norm(fallback))
    if fallback_norm <= 1e-13:
        raise ValueError("constraint span leaves no usable null direction")
    candidates.append(("projected_random", fallback / fallback_norm))

    # Remove duplicate directions, including sign duplicates.
    unique: list[tuple[str, Array]] = []
    for name, vector in candidates:
        vector = _project_off(forbidden_span, vector)
        norm = float(np.linalg.norm(vector))
        if norm <= 1e-13:
            continue
        vector /= norm
        if any(abs(float(vector @ old)) > 1.0 - 1e-10 for _, old in unique):
            continue
        unique.append((name, vector))
        if len(unique) >= limit:
            break
    if not unique:
        raise ValueError("no structured null-space candidate survived")
    return unique


def _hidden_time_derivative(
    state: ParamState,
    spec: ModelSpec,
    *,
    epsilon: float,
) -> Array:
    velocity = parameter_vector_field(state, spec)
    plus = forward_adjoint(_shift_state(state, velocity, epsilon), spec).H
    minus = forward_adjoint(_shift_state(state, velocity, -epsilon), spec).H
    return (plus - minus) / (2.0 * epsilon)


def _gram_time_derivative(
    state: ParamState,
    spec: ModelSpec,
    *,
    epsilon: float,
) -> Array:
    velocity = parameter_vector_field(state, spec)
    plus = _observables(_shift_state(state, velocity, epsilon), spec)[1]
    minus = _observables(_shift_state(state, velocity, -epsilon), spec)[1]
    return (plus - minus) / (2.0 * epsilon)


@dataclass(frozen=True)
class InvisiblePerturbationResult:
    """Perturbed restart plus all same-state and continuation diagnostics."""

    perturbed_state: ParamState
    phi: Array
    U: Array
    A: Array
    V: Array
    delta_W: Array
    selected_candidate: str
    candidate_proxy_scores: Mapping[str, float]
    constraint_defects: Mapping[str, float]
    current_invariance_defects: Mapping[str, float]
    dot_gram_difference: Array
    dot_gram_norm: float
    restart_times: Array
    restart_f_difference: Array
    restart_gram_difference: Array
    restart_theta_difference: Array


def construct_invisible_perturbation(
    state: ParamState,
    initialization_state: ParamState,
    spec: ModelSpec,
    *,
    layer: int,
    basis_size: int = 5,
    alpha: float = 1.0,
    restart_horizon: float = 0.02,
    restart_dt: float = 0.005,
    finite_difference_epsilon: float = 2e-6,
    candidate_seed: int = 0,
    candidate_limit_per_side: int = 8,
    validation_tolerance: float = 2e-9,
) -> InvisiblePerturbationResult:
    """Construct and audit a rank-one future-equivalence attack.

    The perturbation is ``deltaW = U A V.T`` with ``A=[[alpha]]``.  ``V`` is
    projected off both the empirical Hermite space and the current hidden
    training fields, while ``U`` is projected off the current ``beta`` fields.
    Consequently

    ``deltaW @ Phi = 0``, ``deltaW @ H = 0``, and
    ``deltaW.T @ beta = 0``

    up to roundoff.  Candidate directions are generated from projected
    ``Hdot``, ``H``, and ``P`` fields, not from future target curves.
    """

    spec.validate()
    if not 0 <= layer < spec.depth:
        raise ValueError("layer is outside the network")
    if not np.isfinite(alpha) or alpha <= 0.0:
        raise ValueError("alpha must be positive and finite")
    if restart_horizon <= 0.0 or restart_dt <= 0.0:
        raise ValueError("restart horizon and step must be positive")
    if finite_difference_epsilon <= 0.0:
        raise ValueError("finite-difference epsilon must be positive")
    if candidate_limit_per_side < 1:
        raise ValueError("candidate limit must be positive")

    fields = forward_adjoint(state, spec)
    phi = empirical_hermite_phi(
        initialization_state,
        basis_size=basis_size,
        readout_scale=spec.A,
    )
    H = fields.H[layer]
    beta = fields.D[layer] * fields.P[layer + 1]
    right_span = _orthonormal_span(np.column_stack((phi, H)))
    left_span = _orthonormal_span(beta)
    if right_span.shape[1] >= spec.n or left_span.shape[1] >= spec.n:
        raise ValueError("no invisible rank-one subspace remains")

    Hdot = _hidden_time_derivative(
        state,
        spec,
        epsilon=finite_difference_epsilon,
    )
    rng = np.random.default_rng(candidate_seed)
    right_candidates = _structured_candidates(
        {
            "Hdot": Hdot[layer],
            "H": H,
            "P": fields.P[layer],
            "Pnext": fields.P[layer + 1],
        },
        right_span,
        rng=rng,
        limit=candidate_limit_per_side,
    )
    left_candidates = _structured_candidates(
        {
            "Pnext": fields.P[layer + 1],
            "P": fields.P[layer],
            "H": H,
            "Hdot": Hdot[layer],
            "Hdot_next": Hdot[layer + 1],
        },
        left_span,
        rng=rng,
        limit=candidate_limit_per_side,
    )

    # A cheap causal proxy ranks the structured pairs.  The exact dot-Gram
    # finite difference is then evaluated on the best few pairs.
    proxy_pairs: list[tuple[float, str, Array, Array]] = []
    proxy_scores: dict[str, float] = {}
    for uname, u in left_candidates:
        left_response = (
            np.linalg.norm(u @ H)
            + np.linalg.norm(u @ fields.P[layer + 1])
            + np.linalg.norm(u @ Hdot[layer])
        )
        for vname, v in right_candidates:
            right_response = (
                np.linalg.norm(v @ Hdot[layer])
                + 0.1 * np.linalg.norm(v @ fields.P[layer])
            )
            label = f"U[{uname}]|V[{vname}]"
            proxy = float(left_response * right_response)
            proxy_scores[label] = proxy
            proxy_pairs.append((proxy, label, u, v))
    proxy_pairs.sort(key=lambda item: (-item[0], item[1]))
    evaluated_pairs = proxy_pairs[: min(12, len(proxy_pairs))]

    base_dot_gram = _gram_time_derivative(
        state,
        spec,
        epsilon=finite_difference_epsilon,
    )
    best: tuple[float, str, Array, Array, Array] | None = None
    for _, label, u, v in evaluated_pairs:
        delta = alpha * np.outer(u, v)
        candidate = _copy_state(state)
        candidate.W[layer] += delta
        difference = (
            _gram_time_derivative(
                candidate,
                spec,
                epsilon=finite_difference_epsilon,
            )
            - base_dot_gram
        )
        score = float(np.linalg.norm(difference))
        if best is None or score > best[0]:
            best = (score, label, u, v, difference)
    if best is None:
        raise RuntimeError("candidate search produced no evaluated pair")
    dot_gram_norm, selected_label, u, v, dot_gram_difference = best

    # Reproject and renormalize once more before committing the perturbation.
    u = _project_off(left_span, u)
    v = _project_off(right_span, v)
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    U = u[:, None]
    A = np.array([[float(alpha)]])
    V = v[:, None]
    delta_W = U @ A @ V.T
    perturbed = _copy_state(state)
    perturbed.W[layer] += delta_W

    constraint_defects = {
        "deltaW_Phi_fro": float(np.linalg.norm(delta_W @ phi)),
        "deltaW_H_fro": float(np.linalg.norm(delta_W @ H)),
        "deltaW_T_beta_fro": float(np.linalg.norm(delta_W.T @ beta)),
        "frobenius_norm_error": float(
            abs(np.linalg.norm(delta_W) - alpha)
        ),
        # For an alpha-one dense rank-one update the entrywise RMS is exactly
        # 1/n; the maximum is also retained to diagnose localization.
        "entry_rms": float(np.sqrt(np.mean(delta_W * delta_W))),
        "entry_rms_times_n_over_alpha": float(
            np.sqrt(np.mean(delta_W * delta_W)) * spec.n / alpha
        ),
        "max_entry_times_n_over_alpha": float(
            np.max(np.abs(delta_W)) * spec.n / alpha
        ),
    }

    perturbed_fields = forward_adjoint(perturbed, spec)
    f_before, gram_before, theta_before = _observables(state, spec)
    f_after, gram_after, theta_after = _observables(perturbed, spec)
    coefficient_before = retained_row_coefficients(state.W[layer], phi)
    coefficient_after = retained_row_coefficients(
        perturbed.W[layer],
        phi,
    )
    current_defects = {
        "Z_fro": float(np.linalg.norm(perturbed_fields.Z - fields.Z)),
        "activation_fro": float(
            np.linalg.norm(perturbed_fields.T - fields.T)
        ),
        "H_fro": float(np.linalg.norm(perturbed_fields.H - fields.H)),
        "P_fro": float(np.linalg.norm(perturbed_fields.P - fields.P)),
        "output_l2": float(np.linalg.norm(f_after - f_before)),
        "gram_fro": float(np.linalg.norm(gram_after - gram_before)),
        "ntk_fro": float(np.linalg.norm(theta_after - theta_before)),
        "compressed_coefficients_fro": float(
            np.linalg.norm(coefficient_after - coefficient_before)
        ),
    }
    guarded = (
        constraint_defects["deltaW_Phi_fro"],
        constraint_defects["deltaW_H_fro"],
        constraint_defects["deltaW_T_beta_fro"],
        constraint_defects["frobenius_norm_error"],
        *current_defects.values(),
    )
    if max(guarded) > validation_tolerance:
        raise RuntimeError(
            "constructed perturbation failed same-state validation: "
            f"max defect {max(guarded):.3e}"
        )

    # Recompute the selected finite difference after the final reprojection.
    dot_gram_difference = (
        _gram_time_derivative(
            perturbed,
            spec,
            epsilon=finite_difference_epsilon,
        )
        - base_dot_gram
    )
    dot_gram_norm = float(np.linalg.norm(dot_gram_difference))

    restart_times = np.array([0.0, float(restart_horizon)])
    base_restart = simulate_checkpoints(
        state,
        spec,
        restart_times,
        dt=min(restart_dt, restart_horizon),
    )
    perturbed_restart = simulate_checkpoints(
        perturbed,
        spec,
        restart_times,
        dt=min(restart_dt, restart_horizon),
    )

    return InvisiblePerturbationResult(
        perturbed_state=perturbed,
        phi=phi,
        U=U,
        A=A,
        V=V,
        delta_W=delta_W,
        selected_candidate=selected_label,
        candidate_proxy_scores=proxy_scores,
        constraint_defects=constraint_defects,
        current_invariance_defects=current_defects,
        dot_gram_difference=dot_gram_difference,
        dot_gram_norm=dot_gram_norm,
        restart_times=restart_times,
        restart_f_difference=perturbed_restart.f - base_restart.f,
        restart_gram_difference=(
            perturbed_restart.gram - base_restart.gram
        ),
        restart_theta_difference=(
            perturbed_restart.theta - base_restart.theta
        ),
    )


__all__ = [
    "DenseTrajectory",
    "GaussianMaster",
    "HomogenizationCheckpoint",
    "HomogenizationReport",
    "HomogenizationStats",
    "InvisiblePerturbationResult",
    "construct_invisible_perturbation",
    "empirical_degree_one_hermite_phi",
    "empirical_hermite_phi",
    "estimate_depth_homogenization",
    "initialize_gaussian_master",
    "materialize_coupled_state",
    "retained_row_coefficients",
    "simulate_checkpoints",
]
