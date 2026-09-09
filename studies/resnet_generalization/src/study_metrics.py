"""Audit-fixed metrics for the sparse PDE generalization study.

This module deliberately has no file discovery, plotting, or solver imports.
It consumes already-loaded trajectories, verifies their provenance, and
computes dimension-generic comparison, plateau, and trajectory-bootstrap
statistics.

Array conventions
-----------------
``Trajectory`` stores

* ``f`` with shape ``(time, m)``,
* ``grams`` with shape ``(time, depth, m, m)``, and
* ``theta`` with shape ``(time, m, m)``.

``DenseEnsemble`` adds a leading ensemble-member axis to each observable.
All bootstrap resampling is along that leading axis, so an entire trajectory
is always resampled as one statistical unit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

import numpy as np

Array = np.ndarray

CASE_METADATA_FIELDS = (
    "case_sha256",
    "X",
    "y",
    "activation",
    "sigma_w",
    "A",
    "gamma",
)

PRIMARY_BOOTSTRAP_METRICS = (
    "gram_increment_sup_fro",
    "gram_increment_normalized_sup",
    "output_increment_sup_l2",
    "output_increment_normalized_sup",
    "loss_of_ensemble_mean_sup_abs",
    "loss_of_ensemble_mean_normalized_sup",
)


class MetadataMismatchError(ValueError):
    """Raised when two trajectories do not describe the same study case."""


class TimeGridMismatchError(ValueError):
    """Raised when trajectories do not have exactly the same sampled times."""


def _float_array(value: Any, *, name: str) -> Array:
    array = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} contains a non-finite value")
    return array


def _validate_times(times: Array) -> None:
    if times.ndim != 1 or times.size < 2:
        raise ValueError("times must be a one-dimensional array of length >= 2")
    if np.any(np.diff(times) <= 0.0):
        raise ValueError("times must be strictly increasing")


def _validated_metadata(metadata: Mapping[str, Any], m: int) -> dict[str, Any]:
    result = dict(metadata)
    missing = [key for key in CASE_METADATA_FIELDS if key not in result]
    if missing:
        raise ValueError(f"metadata is missing required fields {missing}")
    X = _float_array(result["X"], name="metadata X")
    y = _float_array(result["y"], name="metadata y")
    if X.ndim != 2 or y.shape != (m,) or X.shape[1] != m:
        raise ValueError(
            "metadata X/y shapes must be (d,m) and (m,), matching observables"
        )
    for key in ("sigma_w", "A", "gamma"):
        scalar = float(result[key])
        if not np.isfinite(scalar):
            raise ValueError(f"metadata {key} must be finite")
        result[key] = scalar
    result["X"] = X
    result["y"] = y
    result["case_sha256"] = str(result["case_sha256"])
    result["activation"] = str(result["activation"])
    return result


@dataclass(frozen=True)
class Trajectory:
    """One deterministic PDE trajectory or one already-averaged trajectory."""

    times: Array
    f: Array
    grams: Array
    theta: Array
    metadata: Mapping[str, Any]

    def __post_init__(self) -> None:
        times = _float_array(self.times, name="times")
        f = _float_array(self.f, name="f")
        grams = _float_array(self.grams, name="grams")
        theta = _float_array(self.theta, name="theta")
        _validate_times(times)
        if f.ndim != 2:
            raise ValueError("f must have shape (time,m)")
        nt, m = f.shape
        if times.size != nt:
            raise ValueError("times and f have different time dimensions")
        if grams.ndim != 4 or grams.shape[:1] != (nt,):
            raise ValueError("grams must have shape (time,depth,m,m)")
        if grams.shape[1] < 2 or grams.shape[-2:] != (m, m):
            raise ValueError("grams has an invalid depth or sample dimension")
        if theta.shape != (nt, m, m):
            raise ValueError("theta must have shape (time,m,m)")
        metadata = _validated_metadata(self.metadata, m)
        object.__setattr__(self, "times", times)
        object.__setattr__(self, "f", f)
        object.__setattr__(self, "grams", grams)
        object.__setattr__(self, "theta", theta)
        object.__setattr__(self, "metadata", metadata)

    @property
    def m(self) -> int:
        return int(self.f.shape[-1])


@dataclass(frozen=True)
class DenseEnsemble:
    """Raw finite-network trajectories with one leading member axis."""

    times: Array
    f: Array
    grams: Array
    theta: Array
    metadata: Mapping[str, Any]

    def __post_init__(self) -> None:
        times = _float_array(self.times, name="times")
        f = _float_array(self.f, name="f")
        grams = _float_array(self.grams, name="grams")
        theta = _float_array(self.theta, name="theta")
        _validate_times(times)
        if f.ndim != 3:
            raise ValueError("dense f must have shape (member,time,m)")
        members, nt, m = f.shape
        if members < 1:
            raise ValueError("the dense ensemble must contain at least one member")
        if times.size != nt:
            raise ValueError("times and dense f have different time dimensions")
        if grams.ndim != 5 or grams.shape[:2] != (members, nt):
            raise ValueError(
                "dense grams must have shape (member,time,depth,m,m)"
            )
        if grams.shape[2] < 2 or grams.shape[-2:] != (m, m):
            raise ValueError(
                "dense grams has an invalid depth or sample dimension"
            )
        if theta.shape != (members, nt, m, m):
            raise ValueError(
                "dense theta must have shape (member,time,m,m)"
            )
        metadata = _validated_metadata(self.metadata, m)
        object.__setattr__(self, "times", times)
        object.__setattr__(self, "f", f)
        object.__setattr__(self, "grams", grams)
        object.__setattr__(self, "theta", theta)
        object.__setattr__(self, "metadata", metadata)

    @property
    def members(self) -> int:
        return int(self.f.shape[0])

    @property
    def m(self) -> int:
        return int(self.f.shape[-1])

    def mean_trajectory(self) -> Trajectory:
        """Return the ensemble-mean observables without changing metadata."""

        return Trajectory(
            times=self.times,
            f=np.mean(self.f, axis=0),
            grams=np.mean(self.grams, axis=0),
            theta=np.mean(self.theta, axis=0),
            metadata=self.metadata,
        )


@dataclass(frozen=True)
class DepthAlignment:
    """Dense Gram values evaluated at the PDE's equally spaced depth nodes."""

    values: Array
    method: str
    source_nodes: int
    target_nodes: int
    source_indices: tuple[int, ...] | None


@dataclass(frozen=True)
class BootstrapSamples:
    """Bootstrap samples of the primary comparison statistics."""

    seed: int
    replicates: int
    metrics: Mapping[str, Array]

    def __post_init__(self) -> None:
        if self.replicates < 1:
            raise ValueError("replicates must be positive")
        copied: dict[str, Array] = {}
        for name, values in self.metrics.items():
            array = _float_array(values, name=f"bootstrap metric {name}")
            if array.shape != (self.replicates,):
                raise ValueError(
                    f"bootstrap metric {name} must have shape "
                    f"({self.replicates},)"
                )
            copied[name] = array
        object.__setattr__(self, "metrics", copied)


@dataclass(frozen=True)
class SimultaneousUCB:
    """Centered percentile upper bounds, simultaneous over named cases."""

    confidence: float
    replicates: int
    critical_value: float
    observed: Mapping[str, float]
    upper_bounds: Mapping[str, float]
    centered_max_samples: Array


def _metadata_equal(key: str, left: Any, right: Any) -> bool:
    if key in {"X", "y"}:
        try:
            left_array = np.asarray(left, dtype=float)
            right_array = np.asarray(right, dtype=float)
        except (TypeError, ValueError):
            return False
        return bool(np.array_equal(left_array, right_array))
    if key in {"sigma_w", "A", "gamma"}:
        try:
            return bool(float(left) == float(right))
        except (TypeError, ValueError):
            return False
    return bool(left == right)


def validate_metadata_match(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
) -> None:
    """Require exact equality of every case-defining metadata field."""

    for key in CASE_METADATA_FIELDS:
        if key not in left or key not in right:
            raise MetadataMismatchError(f"missing metadata field {key!r}")
        if not _metadata_equal(key, left[key], right[key]):
            raise MetadataMismatchError(f"metadata mismatch for {key}")


def validate_pair(
    pde: Trajectory,
    dense: DenseEnsemble | Trajectory,
) -> None:
    """Validate case provenance and require a byte-value-identical time grid."""

    validate_metadata_match(pde.metadata, dense.metadata)
    if not np.array_equal(pde.times, dense.times):
        raise TimeGridMismatchError("PDE and dense time grids differ")
    if pde.m != dense.m:
        raise ValueError("PDE and dense sample dimensions differ")


def stitch_pde_segments(segments: Sequence[Trajectory]) -> Trajectory:
    """Stitch restart segments, retaining exactly one copy of each boundary.

    Every segment must use the same case metadata and must begin exactly at
    the preceding segment's final stored time.  The duplicated boundary
    observables must also agree exactly.  These strict checks prevent a
    mismatched restart from being silently interpreted as one trajectory.
    """

    if not segments:
        raise ValueError("at least one PDE segment is required")
    first = segments[0]
    if len(segments) == 1:
        return first
    sample_step = float(first.times[1] - first.times[0])

    def check_uniform_grid(segment: Trajectory, index: int) -> None:
        expected = (
            segment.times[0]
            + np.arange(segment.times.size, dtype=float) * sample_step
        )
        scale = max(1.0, float(np.max(np.abs(expected))))
        tolerance = 32.0 * np.finfo(float).eps * scale
        if float(np.max(np.abs(segment.times - expected))) > tolerance:
            raise TimeGridMismatchError(
                f"segment {index} does not use the common sample step"
            )

    check_uniform_grid(first, 0)
    arrays: dict[str, list[Array]] = {
        "times": [first.times],
        "f": [first.f],
        "grams": [first.grams],
        "theta": [first.theta],
    }
    previous = first
    for index, segment in enumerate(segments[1:], start=1):
        validate_metadata_match(first.metadata, segment.metadata)
        check_uniform_grid(segment, index)
        if segment.m != first.m:
            raise ValueError(f"segment {index} has a different sample count")
        if segment.grams.shape[1:] != first.grams.shape[1:]:
            raise ValueError(f"segment {index} has a different Gram shape")
        if segment.times[0] != previous.times[-1]:
            raise TimeGridMismatchError(
                f"segment {index} does not start at the prior endpoint"
            )
        for name in ("f", "grams", "theta"):
            if not np.array_equal(
                getattr(previous, name)[-1], getattr(segment, name)[0]
            ):
                raise ValueError(
                    f"segment {index} has a discontinuous {name} boundary"
                )
            arrays[name].append(getattr(segment, name)[1:])
        arrays["times"].append(segment.times[1:])
        previous = segment
    stored_times = np.concatenate(arrays["times"], axis=0)
    if np.any(np.diff(stored_times) <= 0.0):
        raise TimeGridMismatchError("stitched time grid is not increasing")
    # ``start + k*dt`` in a continuation can differ by one ulp from
    # ``(offset+k)*dt`` in a fresh dense run.  After the strict common-step
    # check above, emit the unique canonical grid so exact pair validation
    # remains meaningful.
    times = first.times[0] + np.arange(stored_times.size) * sample_step
    metadata = dict(first.metadata)
    metadata["stitched_segments"] = len(segments)
    metadata["stitched_start_time"] = float(times[0])
    metadata["stitched_end_time"] = float(times[-1])
    return Trajectory(
        times=times,
        f=np.concatenate(arrays["f"], axis=0),
        grams=np.concatenate(arrays["grams"], axis=0),
        theta=np.concatenate(arrays["theta"], axis=0),
        metadata=metadata,
    )


def align_dense_depth(
    dense_grams: Array,
    target_nodes: int,
) -> DepthAlignment:
    """Evaluate dense Grams at equally spaced PDE nodes in ``[0,1]``.

    If every target node exists on the dense grid, exact array subsampling is
    used.  Otherwise the two neighboring dense nodes are combined by linear
    interpolation.  The depth axis is inferred as the third axis from the
    end, so both mean and memberwise Gram arrays are accepted.
    """

    values = _float_array(dense_grams, name="dense grams")
    if values.ndim < 3:
        raise ValueError("dense grams must end in (depth,m,m)")
    if values.shape[-1] != values.shape[-2]:
        raise ValueError("dense Gram matrices must be square")
    source_nodes = int(values.shape[-3])
    if source_nodes < 2 or target_nodes < 2:
        raise ValueError("source and target depth grids need at least two nodes")
    depth_axis = values.ndim - 3
    if source_nodes == target_nodes:
        indices = tuple(range(source_nodes))
        return DepthAlignment(
            values=values,
            method="identity",
            source_nodes=source_nodes,
            target_nodes=target_nodes,
            source_indices=indices,
        )
    if source_nodes >= target_nodes and (
        (source_nodes - 1) % (target_nodes - 1) == 0
    ):
        stride = (source_nodes - 1) // (target_nodes - 1)
        indices_array = np.arange(target_nodes, dtype=int) * stride
        aligned = np.take(values, indices_array, axis=depth_axis)
        return DepthAlignment(
            values=aligned,
            method="exact_subsample",
            source_nodes=source_nodes,
            target_nodes=target_nodes,
            source_indices=tuple(int(i) for i in indices_array),
        )
    positions = np.linspace(0.0, source_nodes - 1, target_nodes)
    left = np.floor(positions).astype(int)
    right = np.minimum(left + 1, source_nodes - 1)
    weight = positions - left
    left_values = np.take(values, left, axis=depth_axis)
    right_values = np.take(values, right, axis=depth_axis)
    weight_shape = [1] * values.ndim
    weight_shape[depth_axis] = target_nodes
    reshaped_weight = weight.reshape(weight_shape)
    aligned = (1.0 - reshaped_weight) * left_values
    aligned += reshaped_weight * right_values
    return DepthAlignment(
        values=aligned,
        method="linear_interpolation",
        source_nodes=source_nodes,
        target_nodes=target_nodes,
        source_indices=None,
    )


def _rms(values: Array) -> float:
    return float(np.sqrt(np.mean(np.square(values))))


def _matrix_error_summary(
    delta: Array,
    times: Array,
    *,
    has_depth: bool,
) -> dict[str, Any]:
    norms = np.linalg.norm(delta, axis=(-2, -1))
    flat_index = int(np.argmax(norms))
    if has_depth:
        time_index, depth_index = np.unravel_index(flat_index, norms.shape)
        terminal = float(np.max(norms[-1]))
        result: dict[str, Any] = {
            "sup_fro": float(norms[time_index, depth_index]),
            "rms_fro": _rms(norms),
            "terminal_sup_fro": terminal,
            "max_abs_entry": float(np.max(np.abs(delta))),
            "max_time_index": int(time_index),
            "max_time": float(times[time_index]),
            "max_depth_index": int(depth_index),
            "max_depth_fraction": (
                float(depth_index / (norms.shape[1] - 1))
                if norms.shape[1] > 1
                else 0.0
            ),
        }
    else:
        time_index = flat_index
        result = {
            "sup_fro": float(norms[time_index]),
            "rms_fro": _rms(norms),
            "terminal_fro": float(norms[-1]),
            "max_abs_entry": float(np.max(np.abs(delta))),
            "max_time_index": int(time_index),
            "max_time": float(times[time_index]),
        }
    return result


def _vector_error_summary(delta: Array, times: Array) -> dict[str, Any]:
    norms = np.linalg.norm(delta, axis=-1)
    index = int(np.argmax(norms))
    return {
        "sup_l2": float(norms[index]),
        "rms_l2": _rms(norms),
        "terminal_l2": float(norms[-1]),
        "max_abs_component": float(np.max(np.abs(delta))),
        "max_time_index": index,
        "max_time": float(times[index]),
    }


def _scalar_error_summary(delta: Array, times: Array) -> dict[str, Any]:
    absolute = np.abs(delta)
    index = int(np.argmax(absolute))
    return {
        "sup_abs": float(absolute[index]),
        "rms": _rms(delta),
        "terminal_abs": float(absolute[-1]),
        "max_time_index": index,
        "max_time": float(times[index]),
    }


def comparison_metrics(
    pde: Trajectory,
    dense: DenseEnsemble | Trajectory,
) -> dict[str, Any]:
    """Compare one PDE curve with a dense ensemble mean on the full domain."""

    validate_pair(pde, dense)
    dense_mean = dense.mean_trajectory() if isinstance(dense, DenseEnsemble) else dense
    aligned = align_dense_depth(dense_mean.grams, pde.grams.shape[1])
    dense_grams = aligned.values
    y = np.asarray(pde.metadata["y"], dtype=float)

    pde_gram_increment = pde.grams - pde.grams[0:1]
    dense_gram_increment = dense_grams - dense_grams[0:1]
    gram_increment = _matrix_error_summary(
        pde_gram_increment - dense_gram_increment,
        pde.times,
        has_depth=True,
    )
    pde_gram_motion = float(
        np.max(np.linalg.norm(pde_gram_increment, axis=(-2, -1)))
    )
    dense_gram_motion = float(
        np.max(np.linalg.norm(dense_gram_increment, axis=(-2, -1)))
    )
    gram_denominator = max(pde_gram_motion, dense_gram_motion, 0.05)
    gram_increment.update(
        {
            "pde_motion_sup_fro": pde_gram_motion,
            "dense_motion_sup_fro": dense_gram_motion,
            "denominator": gram_denominator,
            "normalized_sup": gram_increment["sup_fro"] / gram_denominator,
        }
    )

    pde_output_increment = pde.f - pde.f[0]
    dense_output_increment = dense_mean.f - dense_mean.f[0]
    output_increment = _vector_error_summary(
        pde_output_increment - dense_output_increment,
        pde.times,
    )
    pde_output_motion = float(
        np.max(np.linalg.norm(pde_output_increment, axis=-1))
    )
    dense_output_motion = float(
        np.max(np.linalg.norm(dense_output_increment, axis=-1))
    )
    output_denominator = max(
        float(np.linalg.norm(y)),
        pde_output_motion,
        dense_output_motion,
        0.1,
    )
    output_increment.update(
        {
            "pde_motion_sup_l2": pde_output_motion,
            "dense_motion_sup_l2": dense_output_motion,
            "denominator": output_denominator,
            "normalized_sup": output_increment["sup_l2"] / output_denominator,
        }
    )

    pde_loss = 0.5 * np.sum(np.square(pde.f - y), axis=-1)
    dense_loss = 0.5 * np.sum(np.square(dense_mean.f - y), axis=-1)
    loss_gap = _scalar_error_summary(pde_loss - dense_loss, pde.times)
    loss_denominator = max(float(pde_loss[0]), float(dense_loss[0]), 0.1)
    loss_gap.update(
        {
            "pde_initial_loss": float(pde_loss[0]),
            "dense_initial_loss": float(dense_loss[0]),
            "denominator": loss_denominator,
            "normalized_sup": loss_gap["sup_abs"] / loss_denominator,
        }
    )

    return {
        "m": pde.m,
        "time_points": int(pde.times.size),
        "depth_alignment": {
            "method": aligned.method,
            "source_nodes": aligned.source_nodes,
            "target_nodes": aligned.target_nodes,
            "source_indices": aligned.source_indices,
        },
        "gram_increment": gram_increment,
        "output_increment": output_increment,
        "loss_of_ensemble_mean": loss_gap,
        "gram_absolute": _matrix_error_summary(
            pde.grams - dense_grams,
            pde.times,
            has_depth=True,
        ),
        "theta_absolute": _matrix_error_summary(
            pde.theta - dense_mean.theta,
            pde.times,
            has_depth=False,
        ),
        "output_absolute": _vector_error_summary(
            pde.f - dense_mean.f,
            pde.times,
        ),
    }


def _final_half_start(times: Array) -> tuple[int, float]:
    midpoint = 0.5 * (float(times[0]) + float(times[-1]))
    matches = np.flatnonzero(times == midpoint)
    if matches.size != 1:
        raise TimeGridMismatchError(
            "the final-half midpoint must occur exactly once on the time grid"
        )
    return int(matches[0]), midpoint


def _plateau_curve_metrics(
    times: Array,
    f: Array,
    grams: Array,
    loss: Array,
    speed: Array,
) -> dict[str, Any]:
    start, midpoint = _final_half_start(times)
    output_from_start = np.linalg.norm(f[start:] - f[start], axis=-1)
    gram_from_start = np.linalg.norm(
        grams[start:] - grams[start], axis=(-2, -1)
    )
    output_steps = np.linalg.norm(np.diff(f[start:], axis=0), axis=-1)
    gram_steps = np.linalg.norm(
        np.diff(grams[start:], axis=0), axis=(-2, -1)
    )
    loss_from_start = np.abs(loss[start:] - loss[start])
    speed_norm = np.linalg.norm(speed[start:], axis=-1)
    speed_index = int(np.argmax(speed_norm))
    return {
        "tail_start_index": start,
        "tail_start_time": midpoint,
        "tail_end_time": float(times[-1]),
        "output_endpoint_drift_l2": float(output_from_start[-1]),
        "output_max_drift_l2": float(np.max(output_from_start)),
        "output_discrete_arclength_l2": float(np.sum(output_steps)),
        "gram_endpoint_drift_sup_fro": float(
            np.max(gram_from_start[-1])
        ),
        "gram_max_drift_sup_fro": float(np.max(gram_from_start)),
        "gram_discrete_arclength_sum_step_sup_fro": float(
            np.sum(np.max(gram_steps, axis=1))
        ),
        "analytic_output_speed_sup_l2": float(speed_norm[speed_index]),
        "analytic_output_speed_max_time_index": start + speed_index,
        "analytic_output_speed_max_time": float(times[start + speed_index]),
        "loss_endpoint_drift_abs": float(loss_from_start[-1]),
        "loss_max_drift_abs": float(np.max(loss_from_start)),
        "tail_start_loss": float(loss[start]),
        "tail_end_loss": float(loss[-1]),
    }


def plateau_metrics(
    trajectory: Trajectory | DenseEnsemble,
) -> dict[str, Any]:
    """Compute the preregistered plateau diagnostics over the final half.

    PDE output speed is evaluated as ``-Theta(t) (f(t)-y)``.  For a dense
    ensemble it is the ensemble mean of the memberwise analytic velocities
    ``-Theta_s(t) (f_s(t)-y)``; it is intentionally *not* reconstructed from
    separately averaged ``Theta`` and ``f``.
    """

    y = np.asarray(trajectory.metadata["y"], dtype=float)
    if isinstance(trajectory, Trajectory):
        residual = trajectory.f - y
        speed = -np.einsum(
            "tij,tj->ti", trajectory.theta, residual, optimize=True
        )
        loss = 0.5 * np.sum(np.square(residual), axis=-1)
        result = _plateau_curve_metrics(
            trajectory.times,
            trajectory.f,
            trajectory.grams,
            loss,
            speed,
        )
        result["trajectory_kind"] = "pde"
        return result

    f_mean = np.mean(trajectory.f, axis=0)
    grams_mean = np.mean(trajectory.grams, axis=0)
    residual_members = trajectory.f - y
    member_speeds = -np.einsum(
        "stij,stj->sti",
        trajectory.theta,
        residual_members,
        optimize=True,
    )
    speed = np.mean(member_speeds, axis=0)
    loss = 0.5 * np.sum(np.square(f_mean - y), axis=-1)
    result = _plateau_curve_metrics(
        trajectory.times,
        f_mean,
        grams_mean,
        loss,
        speed,
    )
    start = int(result["tail_start_index"])
    member_output_endpoint = np.linalg.norm(
        trajectory.f[:, -1] - trajectory.f[:, start], axis=-1
    )
    member_gram_endpoint = np.max(
        np.linalg.norm(
            trajectory.grams[:, -1] - trajectory.grams[:, start],
            axis=(-2, -1),
        ),
        axis=-1,
    )
    member_loss = 0.5 * np.sum(
        np.square(trajectory.f - y), axis=-1
    )
    member_loss_endpoint = np.abs(
        member_loss[:, -1] - member_loss[:, start]
    )
    result.update(
        {
            "trajectory_kind": "dense_ensemble",
            "ensemble_members": trajectory.members,
            "member_output_endpoint_drift_p95_l2": float(
                np.quantile(member_output_endpoint, 0.95)
            ),
            "member_gram_endpoint_drift_p95_sup_fro": float(
                np.quantile(member_gram_endpoint, 0.95)
            ),
            "member_loss_endpoint_drift_p95_abs": float(
                np.quantile(member_loss_endpoint, 0.95)
            ),
        }
    )
    return result


def _bootstrap_primary_batch(
    pde: Trajectory,
    dense_f_members: Array,
    dense_gram_members: Array,
    counts: Array,
) -> dict[str, Array]:
    members = int(dense_f_members.shape[0])
    weights = counts.astype(float) / members
    dense_f = np.einsum(
        "bs,stm->btm", weights, dense_f_members, optimize=True
    )
    dense_grams = np.einsum(
        "bs,stdij->btdij", weights, dense_gram_members, optimize=True
    )
    y = np.asarray(pde.metadata["y"], dtype=float)

    pde_g_inc = pde.grams - pde.grams[0:1]
    dense_g_inc = dense_grams - dense_grams[:, 0:1]
    gram_norms = np.linalg.norm(
        dense_g_inc - pde_g_inc[None, ...], axis=(-2, -1)
    )
    gram_error = np.max(gram_norms, axis=(1, 2))
    pde_g_motion = float(
        np.max(np.linalg.norm(pde_g_inc, axis=(-2, -1)))
    )
    dense_g_motion = np.max(
        np.linalg.norm(dense_g_inc, axis=(-2, -1)), axis=(1, 2)
    )
    gram_denominator = np.maximum(
        np.maximum(pde_g_motion, dense_g_motion), 0.05
    )

    pde_f_inc = pde.f - pde.f[0]
    dense_f_inc = dense_f - dense_f[:, 0:1]
    output_norms = np.linalg.norm(
        dense_f_inc - pde_f_inc[None, ...], axis=-1
    )
    output_error = np.max(output_norms, axis=1)
    pde_f_motion = float(np.max(np.linalg.norm(pde_f_inc, axis=-1)))
    dense_f_motion = np.max(
        np.linalg.norm(dense_f_inc, axis=-1), axis=1
    )
    output_denominator = np.maximum.reduce(
        (
            np.full(counts.shape[0], np.linalg.norm(y)),
            np.full(counts.shape[0], pde_f_motion),
            dense_f_motion,
            np.full(counts.shape[0], 0.1),
        )
    )

    pde_loss = 0.5 * np.sum(np.square(pde.f - y), axis=-1)
    dense_loss = 0.5 * np.sum(
        np.square(dense_f - y[None, None, :]), axis=-1
    )
    loss_error = np.max(np.abs(dense_loss - pde_loss[None, :]), axis=1)
    loss_denominator = np.maximum.reduce(
        (
            np.full(counts.shape[0], pde_loss[0]),
            dense_loss[:, 0],
            np.full(counts.shape[0], 0.1),
        )
    )
    return {
        "gram_increment_sup_fro": gram_error,
        "gram_increment_normalized_sup": gram_error / gram_denominator,
        "output_increment_sup_l2": output_error,
        "output_increment_normalized_sup": output_error / output_denominator,
        "loss_of_ensemble_mean_sup_abs": loss_error,
        "loss_of_ensemble_mean_normalized_sup": (
            loss_error / loss_denominator
        ),
    }


def bootstrap_comparison_metrics(
    pde: Trajectory,
    dense: DenseEnsemble,
    *,
    replicates: int = 2000,
    seed: int = 24681357,
    batch_size: int = 16,
    resample_counts: Array | None = None,
) -> BootstrapSamples:
    """Resample complete dense trajectories and recompute primary metrics.

    Passing the same ``resample_counts`` to multiple cases preserves an
    explicitly paired/common-random-number design.  Omitting it creates the
    counts deterministically from ``seed``.
    """

    validate_pair(pde, dense)
    if replicates < 1:
        raise ValueError("replicates must be positive")
    if batch_size < 1:
        raise ValueError("batch_size must be positive")
    if resample_counts is None:
        all_counts = trajectory_resample_counts(
            dense.members,
            replicates=replicates,
            seed=seed,
        )
    else:
        all_counts = np.asarray(resample_counts)
        if all_counts.shape != (replicates, dense.members):
            raise ValueError(
                "resample_counts must have shape (replicates,members)"
            )
        if not np.issubdtype(all_counts.dtype, np.integer):
            raise ValueError("resample_counts must contain integers")
        if np.any(all_counts < 0) or np.any(
            np.sum(all_counts, axis=1) != dense.members
        ):
            raise ValueError(
                "every resample_counts row must be nonnegative and sum "
                "to the ensemble size"
            )
    # Align each member once.  Aligning every bootstrap mean would perform the
    # same linear map ``replicates`` times and is needlessly expensive.
    dense_gram_members = align_dense_depth(
        dense.grams, pde.grams.shape[1]
    ).values
    output = {
        name: np.empty(replicates, dtype=float)
        for name in PRIMARY_BOOTSTRAP_METRICS
    }
    for start in range(0, replicates, batch_size):
        stop = min(start + batch_size, replicates)
        batch = _bootstrap_primary_batch(
            pde,
            dense.f,
            dense_gram_members,
            all_counts[start:stop],
        )
        for name in PRIMARY_BOOTSTRAP_METRICS:
            output[name][start:stop] = batch[name]
    return BootstrapSamples(
        seed=seed,
        replicates=replicates,
        metrics=output,
    )


def trajectory_resample_counts(
    members: int,
    *,
    replicates: int = 2000,
    seed: int = 24681357,
) -> Array:
    """Return deterministic multinomial counts for whole-trajectory draws."""

    if members < 1:
        raise ValueError("members must be positive")
    if replicates < 1:
        raise ValueError("replicates must be positive")
    rng = np.random.default_rng(seed)
    return rng.multinomial(
        members,
        np.full(members, 1.0 / members),
        size=replicates,
    )


def observed_primary_metrics(metrics: Mapping[str, Any]) -> dict[str, float]:
    """Extract bootstrap-compatible primary statistics from a comparison."""

    return {
        "gram_increment_sup_fro": float(
            metrics["gram_increment"]["sup_fro"]
        ),
        "gram_increment_normalized_sup": float(
            metrics["gram_increment"]["normalized_sup"]
        ),
        "output_increment_sup_l2": float(
            metrics["output_increment"]["sup_l2"]
        ),
        "output_increment_normalized_sup": float(
            metrics["output_increment"]["normalized_sup"]
        ),
        "loss_of_ensemble_mean_sup_abs": float(
            metrics["loss_of_ensemble_mean"]["sup_abs"]
        ),
        "loss_of_ensemble_mean_normalized_sup": float(
            metrics["loss_of_ensemble_mean"]["normalized_sup"]
        ),
    }


def centered_simultaneous_ucb(
    observed: Mapping[str, float],
    bootstrap: Mapping[str, Array],
    *,
    confidence: float = 0.95,
) -> SimultaneousUCB:
    """Construct a centered bootstrap UCB simultaneous over cases.

    For bootstrap replicate ``b`` this computes

    ``max_case(T_case^*(b) - T_case)``,

    takes its upper percentile, and adds the resulting common critical value
    to every observed case statistic.  ``method="higher"`` makes the empirical
    quantile conservative on the finite replicate grid.  The critical value is
    clipped below at zero so the reported upper bound cannot fall below the
    observed statistic.
    """

    if not 0.0 < confidence < 1.0:
        raise ValueError("confidence must lie strictly between zero and one")
    observed_keys = set(observed)
    bootstrap_keys = set(bootstrap)
    if not observed_keys or observed_keys != bootstrap_keys:
        raise ValueError("observed and bootstrap case keys must match and be nonempty")
    ordered = sorted(observed_keys)
    arrays: list[Array] = []
    replicates: int | None = None
    cleaned_observed: dict[str, float] = {}
    for case_id in ordered:
        estimate = float(observed[case_id])
        if not np.isfinite(estimate):
            raise ValueError(f"observed statistic for {case_id} is non-finite")
        sample = _float_array(
            bootstrap[case_id], name=f"bootstrap statistic for {case_id}"
        )
        if sample.ndim != 1 or sample.size < 1:
            raise ValueError(
                f"bootstrap statistic for {case_id} must be one-dimensional"
            )
        if replicates is None:
            replicates = int(sample.size)
        elif sample.size != replicates:
            raise ValueError("all cases must use the same bootstrap replicates")
        cleaned_observed[case_id] = estimate
        arrays.append(sample - estimate)
    centered_max = np.max(np.stack(arrays, axis=0), axis=0)
    critical = max(
        0.0,
        float(np.quantile(centered_max, confidence, method="higher")),
    )
    upper = {
        case_id: cleaned_observed[case_id] + critical
        for case_id in ordered
    }
    assert replicates is not None
    return SimultaneousUCB(
        confidence=float(confidence),
        replicates=replicates,
        critical_value=critical,
        observed=cleaned_observed,
        upper_bounds=upper,
        centered_max_samples=centered_max,
    )


def centered_simultaneous_ucbs(
    observed_by_case: Mapping[str, Mapping[str, float]],
    bootstrap_by_case: Mapping[str, BootstrapSamples],
    *,
    confidence: float = 0.95,
) -> dict[str, SimultaneousUCB]:
    """Apply :func:`centered_simultaneous_ucb` to every common metric."""

    case_ids = set(observed_by_case)
    if not case_ids or case_ids != set(bootstrap_by_case):
        raise ValueError("observed and bootstrap case keys must match and be nonempty")
    first_case = sorted(case_ids)[0]
    metric_names = set(observed_by_case[first_case])
    if not metric_names:
        raise ValueError("at least one metric is required")
    for case_id in case_ids:
        if set(observed_by_case[case_id]) != metric_names:
            raise ValueError("all observed cases must expose the same metrics")
        if set(bootstrap_by_case[case_id].metrics) != metric_names:
            raise ValueError("all bootstrap cases must expose the same metrics")
    result: dict[str, SimultaneousUCB] = {}
    for metric in sorted(metric_names):
        observed = {
            case_id: float(observed_by_case[case_id][metric])
            for case_id in case_ids
        }
        bootstrap = {
            case_id: bootstrap_by_case[case_id].metrics[metric]
            for case_id in case_ids
        }
        result[metric] = centered_simultaneous_ucb(
            observed,
            bootstrap,
            confidence=confidence,
        )
    return result
