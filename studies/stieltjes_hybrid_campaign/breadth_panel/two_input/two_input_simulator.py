#!/usr/bin/env python3
"""Bounded explicit-Euler simulator for one two-input antithetic lineage.

The simulator is intentionally configuration-driven and contains no frozen
campaign point list.  One invocation holds exactly one antithetic lineage
(two trajectories) in memory.  Validation pairs and width screens are built
from separate invocations whose manifests bind their point configurations.
"""

from __future__ import annotations

import math
import resource
import time
from collections.abc import Callable, Mapping
from typing import Any

import numpy as np
import torch

import two_input_engine as model


ALLOWED_STEPS = (1.0e-5, 2.0e-5)
ALLOWED_PURPOSES = ("validation_coarse", "validation_fine", "width_screen")

SCALAR_OBSERVABLES = (
    "g",
    "delta",
    "kernel_g",
    "kernel_delta",
    "cross_kernel",
    "kernel_g_a",
    "kernel_g_W",
    "kernel_g_u",
    "kernel_delta_a",
    "kernel_delta_W",
    "kernel_delta_u",
    "cross_kernel_a",
    "cross_kernel_W",
    "cross_kernel_u",
    "effective_numerator",
    "transverse_numerator",
    "loss_full",
    "loss_projected",
)

MATRIX_OBSERVABLES = (
    "output",
    "residual",
    "q1",
    "q2",
    "kernel_matrix",
    "kernel_a_matrix",
    "kernel_W_matrix",
    "kernel_u_matrix",
)

UPDATE_FIELDS = (
    "a_unchanged_fraction",
    "u_unchanged_fraction",
    "w_sample_unchanged_fraction",
    "a_ideal_update_l2",
    "u_ideal_update_l2",
    "w_ideal_update_l2",
    "w_sample_ideal_update_l2",
    "a_applied_update_l2",
    "u_applied_update_l2",
    "w_sample_applied_update_l2",
    "a_applied_to_ideal_ratio",
    "u_applied_to_ideal_ratio",
    "w_sample_applied_to_ideal_ratio",
    "a_update_cosine",
    "u_update_cosine",
    "w_sample_update_cosine",
)

STATE_FIELDS = (
    "a_max_abs",
    "u_max_abs",
    "w_sample_max_abs",
)


class BudgetStop(RuntimeError):
    """A declared resource or step cap ended the point inconclusively."""


class NumericalInvalid(RuntimeError):
    """A numerical invariant or trajectory gate failed."""


class Guard:
    def __init__(self, caps: Mapping[str, Any], device: torch.device) -> None:
        self.caps = caps
        self.device = device
        self.started = time.monotonic()
        self.completed_steps = 0
        self.max_gpu_gib = 0.0
        self.max_host_gib = 0.0
        if device.type == "cuda":
            torch.cuda.synchronize(device)
            torch.cuda.reset_peak_memory_stats(device)

    def snapshot(self) -> dict[str, float | int]:
        host_gib = (
            float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20
        )
        self.max_host_gib = max(self.max_host_gib, host_gib)
        if self.device.type == "cuda":
            gpu_gib = float(torch.cuda.max_memory_allocated(self.device)) / 2**30
            self.max_gpu_gib = max(self.max_gpu_gib, gpu_gib)
        return {
            "elapsed_seconds": time.monotonic() - self.started,
            "completed_steps": self.completed_steps,
            "max_host_rss_gib": self.max_host_gib,
            "max_gpu_allocated_gib": self.max_gpu_gib,
        }

    def check(self) -> None:
        snapshot = self.snapshot()
        reason = None
        if snapshot["elapsed_seconds"] >= float(self.caps["wall_seconds"]):
            reason = "wall cap reached"
        elif snapshot["max_host_rss_gib"] > float(
            self.caps["host_rss_gib"]
        ):
            reason = "host RSS cap reached"
        elif self.device.type == "cuda" and snapshot[
            "max_gpu_allocated_gib"
        ] > float(self.caps["gpu_memory_gib"]):
            reason = "GPU allocation cap reached"
        if reason is not None:
            error = BudgetStop(reason)
            error.point_diagnostics = snapshot
            raise error


def _exact_allowed_step(value: float) -> bool:
    return any(
        math.isclose(value, step, rel_tol=0.0, abs_tol=1e-15)
        for step in ALLOWED_STEPS
    )


def validate_point(point: Mapping[str, Any]) -> None:
    required = {
        "id",
        "purpose",
        "seed",
        "lineage",
        "width",
        "sigma",
        "theta",
        "step",
        "stop_g",
        "output_nodes",
        "prefix_digest_sizes",
        "rng_row_block",
        "w_monitor_seed",
        "w_monitor_extent",
        "w_monitor_sample_size",
        "diagnostic_stride",
        "wall_sync_stride",
        "caps",
    }
    optional: set[str] = set()
    missing = required - set(point)
    unknown = set(point) - required - optional
    if missing:
        raise ValueError(f"point is missing fields: {sorted(missing)}")
    if unknown:
        raise ValueError(f"point has unknown fields: {sorted(unknown)}")
    if not str(point["id"]) or "/" in str(point["id"]):
        raise ValueError("point id must be a nonempty path component")
    if point["purpose"] not in ALLOWED_PURPOSES:
        raise ValueError("unsupported point purpose")
    if int(point["seed"]) < 0 or int(point["lineage"]) < 0:
        raise ValueError("seed and lineage must be nonnegative")
    width = int(point["width"])
    if width < 1 or width >= model.audited_init.ROW_BASE:
        raise ValueError("width is outside the nested RNG range")
    if int(point["sigma"]) not in (-1, 1):
        raise ValueError("sigma must be +1 or -1")
    if not math.isclose(
        float(point["theta"]), model.CORE_THETA, rel_tol=0.0, abs_tol=1e-14
    ):
        raise ValueError("the breadth point admits only theta=+1/sqrt(2)")
    step = float(point["step"])
    if not _exact_allowed_step(step):
        raise ValueError("only h=2e-5 and h=1e-5 are admitted")
    if point["purpose"] == "validation_coarse" and step != 2.0e-5:
        raise ValueError("coarse validation requires h=2e-5")
    if point["purpose"] in ("validation_fine", "width_screen") and step != 1.0e-5:
        raise ValueError("fine validation and width screens require h=1e-5")
    stop_g = float(point["stop_g"])
    if not 0.0 < stop_g <= 0.95:
        raise ValueError("stop_g must lie in (0,.95]")
    nodes = tuple(float(value) for value in point["output_nodes"])
    if not nodes or tuple(sorted(set(nodes))) != nodes:
        raise ValueError("output nodes must be nonempty and strictly increasing")
    if nodes[0] < 0.0 or nodes[-1] > stop_g:
        raise ValueError("output nodes must lie in [0,stop_g]")
    prefixes = tuple(int(value) for value in point["prefix_digest_sizes"])
    if not prefixes or tuple(sorted(set(prefixes))) != prefixes:
        raise ValueError("prefix sizes must be nonempty and strictly increasing")
    if prefixes[-1] > width:
        raise ValueError("prefix exceeds width")
    row_block = int(point["rng_row_block"])
    if row_block < 1:
        raise ValueError("rng_row_block must be positive")
    extent = int(point["w_monitor_extent"])
    sample = int(point["w_monitor_sample_size"])
    if extent < 1 or extent > width:
        raise ValueError("W monitor extent must lie within width")
    if sample < 1 or sample > extent * extent:
        raise ValueError("invalid W monitor sample size")
    if int(point["diagnostic_stride"]) < 1:
        raise ValueError("diagnostic_stride must be positive")
    if int(point["wall_sync_stride"]) < 1:
        raise ValueError("wall_sync_stride must be positive")
    caps = point["caps"]
    cap_fields = {
        "wall_seconds",
        "max_steps",
        "host_rss_gib",
        "gpu_memory_gib",
        "state_abs_ceiling",
        "kernel_ceiling",
        "component_sum_ulp_multiplier",
        "channel_psd_ulp_multiplier",
        "mean_g_monotonicity_tolerance",
        "mean_loss_monotonicity_tolerance",
    }
    if set(caps) != cap_fields:
        raise ValueError("caps must contain exactly the declared hard-cap fields")
    if int(caps["max_steps"]) < 1:
        raise ValueError("max_steps must be positive")
    for key in (
        "wall_seconds",
        "host_rss_gib",
        "gpu_memory_gib",
        "state_abs_ceiling",
        "kernel_ceiling",
        "component_sum_ulp_multiplier",
        "channel_psd_ulp_multiplier",
    ):
        if not math.isfinite(float(caps[key])) or float(caps[key]) <= 0.0:
            raise ValueError(f"cap {key} must be finite and positive")
    for key in (
        "mean_g_monotonicity_tolerance",
        "mean_loss_monotonicity_tolerance",
    ):
        if not math.isfinite(float(caps[key])) or float(caps[key]) < 0.0:
            raise ValueError(f"tolerance {key} must be finite and nonnegative")


def configuration_from_point(point: Mapping[str, Any]) -> model.Configuration:
    return model.Configuration(
        f"{point['id']}_configuration",
        float(point["theta"]),
        int(point["sigma"]),
    )


def monotonicity_diagnostics(
    g: np.ndarray,
    loss: np.ndarray,
    *,
    g_tolerance: float,
    loss_tolerance: float,
) -> dict[str, float | bool]:
    mean_g = np.mean(np.asarray(g, dtype=np.float64), axis=1)
    mean_loss = np.mean(np.asarray(loss, dtype=np.float64), axis=1)
    worst_g_drop = max(0.0, float(np.max(-np.diff(mean_g), initial=0.0)))
    worst_loss_rise = max(
        0.0, float(np.max(np.diff(mean_loss), initial=0.0))
    )
    return {
        "maximum_mean_g_drop": worst_g_drop,
        "maximum_mean_loss_rise": worst_loss_rise,
        "mean_g_nondecreasing": worst_g_drop <= g_tolerance,
        "mean_loss_nonincreasing": worst_loss_rise <= loss_tolerance,
    }


def driver_diagnostics(
    time_values: np.ndarray,
    g: np.ndarray,
    effective_numerator: np.ndarray,
    *,
    through_g: float,
) -> dict[str, float]:
    time_values = np.asarray(time_values, dtype=np.float64)
    mean_g = np.mean(np.asarray(g, dtype=np.float64), axis=1)
    exact_driver = 2.0 * np.mean(
        np.asarray(effective_numerator, dtype=np.float64), axis=1
    )
    dt = np.diff(time_values)
    if np.any(dt <= 0.0):
        raise ValueError("time values must be strictly increasing")
    selected = mean_g[:-1] <= through_g
    if not np.any(selected):
        raise ValueError("driver window is empty")
    finite_difference = np.diff(mean_g) / dt
    defect = finite_difference - exact_driver[:-1]
    finite_difference = finite_difference[selected]
    exact_driver = exact_driver[:-1][selected]
    defect = defect[selected]
    selected_dt = dt[selected]
    scale = np.maximum(
        0.5 * (np.abs(finite_difference) + np.abs(exact_driver)), 1e-12
    )
    rms_scale = max(float(np.sqrt(np.mean(exact_driver**2))), 1e-12)
    total_motion = max(
        abs(float(np.sum(selected_dt * finite_difference))), 1e-12
    )
    return {
        "driver_max_relative_defect": float(np.max(np.abs(defect) / scale)),
        "driver_relative_rms_defect": float(
            np.sqrt(np.mean(defect**2)) / rms_scale
        ),
        "driver_cumulative_relative_defect": abs(
            float(np.sum(selected_dt * defect))
        )
        / total_motion,
    }


def leakage_series(
    g: np.ndarray,
    delta: np.ndarray,
    kernel_g: np.ndarray,
    kernel_delta: np.ndarray,
    cross_kernel: np.ndarray,
) -> dict[str, np.ndarray]:
    arrays = tuple(
        np.asarray(value, dtype=np.float64)
        for value in (g, delta, kernel_g, kernel_delta, cross_kernel)
    )
    g, delta, kernel_g, kernel_delta, cross_kernel = arrays
    if not all(value.shape == g.shape for value in arrays):
        raise ValueError("all leakage inputs must have the same (time,replica) shape")
    mean_g = np.mean(g, axis=1)
    first = np.sqrt(np.mean(delta**2, axis=1)) / np.maximum(
        np.abs(1.0 - mean_g), 1e-12
    )
    second = np.abs(np.mean(delta * cross_kernel, axis=1)) / np.maximum(
        np.abs(np.mean((1.0 - g) * kernel_g, axis=1)), 1e-12
    )
    third = np.mean(np.abs(cross_kernel), axis=1) / np.sqrt(
        np.maximum(
            np.mean(kernel_g, axis=1) * np.mean(kernel_delta, axis=1),
            1e-24,
        )
    )
    return {
        "leakage_delta_rms_over_residual": first,
        "leakage_delta_C_over_longitudinal": second,
        "leakage_cross_correlation": third,
    }


def leakage_diagnostics(
    g: np.ndarray,
    delta: np.ndarray,
    kernel_g: np.ndarray,
    kernel_delta: np.ndarray,
    cross_kernel: np.ndarray,
    *,
    through_g: float,
) -> dict[str, float]:
    series = leakage_series(g, delta, kernel_g, kernel_delta, cross_kernel)
    selected = np.mean(np.asarray(g, dtype=np.float64), axis=1) <= through_g
    if not np.any(selected):
        raise ValueError("leakage window is empty")
    maxima = {key: float(np.max(value[selected])) for key, value in series.items()}
    return {**maxima, "maximum_leakage_score": max(maxima.values())}


def common_g_clock(
    time_values: np.ndarray,
    g: np.ndarray,
    fields: Mapping[str, np.ndarray],
    nodes: np.ndarray,
) -> dict[str, np.ndarray]:
    """Interpolate all replicas at the common ensemble-mean ``g`` clock."""

    time_values = np.asarray(time_values, dtype=np.float64)
    g = np.asarray(g, dtype=np.float64)
    nodes = np.asarray(nodes, dtype=np.float64)
    if g.ndim != 2 or g.shape[0] != time_values.size:
        raise ValueError("g must have shape (time,replica)")
    mean_g = np.mean(g, axis=1)
    if np.any(np.diff(mean_g) < 0.0):
        raise ValueError("common-g clock requires a nondecreasing ensemble mean")
    if nodes.ndim != 1 or np.any(np.diff(nodes) <= 0.0):
        raise ValueError("nodes must be a strictly increasing vector")
    if nodes[0] < mean_g[0] or nodes[-1] > mean_g[-1]:
        raise ValueError("requested node lies outside the common-g trajectory")

    result: dict[str, np.ndarray] = {
        "output_nodes": nodes.copy(),
        "node_time": np.empty(nodes.size, dtype=np.float64),
    }
    for key, value in fields.items():
        value = np.asarray(value)
        if value.shape[0] != time_values.size:
            raise ValueError(f"field {key} has a different time dimension")
        result[f"node_{key}"] = np.empty(
            (nodes.size, *value.shape[1:]), dtype=np.float64
        )

    for node_index, node in enumerate(nodes):
        right = int(np.searchsorted(mean_g, node, side="left"))
        if right == 0:
            left = right
            weight = 0.0
        else:
            left = right - 1
            denominator = mean_g[right] - mean_g[left]
            weight = 0.0 if denominator == 0.0 else (node - mean_g[left]) / denominator
        result["node_time"][node_index] = (
            (1.0 - weight) * time_values[left] + weight * time_values[right]
        )
        for key, value in fields.items():
            value = np.asarray(value, dtype=np.float64)
            result[f"node_{key}"][node_index] = (
                (1.0 - weight) * value[left] + weight * value[right]
            )
    return result


def _allocate_stores(
    max_steps: int, device: torch.device
) -> tuple[dict[str, torch.Tensor], dict[str, torch.Tensor], dict[str, torch.Tensor]]:
    observables: dict[str, torch.Tensor] = {}
    for key in SCALAR_OBSERVABLES:
        observables[key] = torch.empty(
            (max_steps + 1, 2), dtype=torch.float32, device=device
        )
    for key in ("output", "residual", "q1", "q2"):
        observables[key] = torch.empty(
            (max_steps + 1, 2, 2), dtype=torch.float32, device=device
        )
    for key in (
        "kernel_matrix",
        "kernel_a_matrix",
        "kernel_W_matrix",
        "kernel_u_matrix",
    ):
        observables[key] = torch.empty(
            (max_steps + 1, 2, 2, 2), dtype=torch.float32, device=device
        )
    updates = {
        key: torch.empty((max_steps, 2), dtype=torch.float32, device=device)
        for key in UPDATE_FIELDS
    }
    states = {
        key: torch.empty(
            (max_steps + 1, 2), dtype=torch.float32, device=device
        )
        for key in STATE_FIELDS
    }
    return observables, updates, states


def _cheap_validity(
    state: model.State,
    obs: model.Observables,
    rows: torch.Tensor,
    cols: torch.Tensor,
    caps: Mapping[str, Any],
) -> tuple[dict[str, torch.Tensor], torch.Tensor]:
    """Queue inexpensive checks without synchronizing the CUDA stream."""

    w_sample = state.W[:, rows, cols]
    tensors = [state.a, state.u, w_sample]
    tensors.extend(getattr(obs, key) for key in SCALAR_OBSERVABLES)
    tensors.extend(getattr(obs, key) for key in MATRIX_OBSERVABLES)
    valid = torch.stack(
        tuple(torch.all(torch.isfinite(value)) for value in tensors)
    ).all()
    ceiling = float(caps["state_abs_ceiling"])
    maxima = {
        "a_max_abs": torch.amax(torch.abs(state.a), dim=1),
        "u_max_abs": torch.amax(torch.abs(state.u), dim=(1, 2)),
        "w_sample_max_abs": torch.amax(torch.abs(w_sample), dim=1),
    }
    for value in maxima.values():
        valid = valid & torch.all(value < ceiling)
    valid = valid & torch.all(obs.kernel_g > 0.0)
    valid = valid & torch.all(obs.kernel_delta > 0.0)
    valid = valid & torch.all(obs.kernel_g < float(caps["kernel_ceiling"]))
    valid = valid & torch.all(obs.kernel_delta < float(caps["kernel_ceiling"]))
    epsilon = torch.finfo(torch.float32).eps
    scale = torch.maximum(torch.abs(obs.kernel_g), torch.ones_like(obs.kernel_g))
    component_tolerance = (
        float(caps["component_sum_ulp_multiplier"]) * epsilon * scale
    )
    for total, parts in (
        (obs.kernel_g, (obs.kernel_g_a, obs.kernel_g_W, obs.kernel_g_u)),
        (
            obs.kernel_delta,
            (obs.kernel_delta_a, obs.kernel_delta_W, obs.kernel_delta_u),
        ),
        (
            obs.cross_kernel,
            (obs.cross_kernel_a, obs.cross_kernel_W, obs.cross_kernel_u),
        ),
    ):
        valid = valid & torch.all(
            torch.abs(total - sum(parts)) <= component_tolerance
        )
    determinant = obs.kernel_g * obs.kernel_delta - obs.cross_kernel.square()
    psd_scale = torch.maximum(
        obs.kernel_g * obs.kernel_delta, torch.ones_like(obs.kernel_g)
    )
    psd_tolerance = (
        float(caps["channel_psd_ulp_multiplier"]) * epsilon * psd_scale
    )
    valid = valid & torch.all(determinant >= -psd_tolerance)
    loss_identity = obs.loss_projected + obs.delta.square()
    valid = valid & torch.all(
        torch.abs(obs.loss_full - loss_identity) <= component_tolerance
    )
    return maxima, valid


def _validate_full_W(
    state: model.State, caps: Mapping[str, Any]
) -> torch.Tensor:
    """Synchronizing full-matrix scan used only at declared diagnostics."""

    maximum = torch.amax(torch.abs(state.W), dim=(1, 2))
    valid = torch.all(torch.isfinite(state.W)) & torch.all(
        maximum < float(caps["state_abs_ceiling"])
    )
    if not bool(valid.item()):
        raise NumericalInvalid("full W failed finite/absolute-ceiling check")
    return maximum


def _record_observables(
    stores: dict[str, torch.Tensor], index: int, obs: model.Observables
) -> None:
    for key in stores:
        stores[key][index] = getattr(obs, key)


def _record_update(
    stores: dict[str, torch.Tensor],
    index: int,
    state: model.State,
    tangent: model.Tangent,
    step: float,
    rows: torch.Tensor,
    cols: torch.Tensor,
) -> None:
    a_before = state.a.clone()
    u_before = state.u.clone()
    w_before = state.W[:, rows, cols].clone()
    ideal_a = step * tangent.a
    ideal_u = step * tangent.u
    ideal_w = step * tangent.W[:, rows, cols]
    model.euler_step_in_place(state, tangent, step)
    applied_a = state.a - a_before
    applied_u = state.u - u_before
    w_after = state.W[:, rows, cols]
    applied_w = w_after - w_before

    flat = lambda value: value.reshape(value.shape[0], -1)
    ideal_a_norm = torch.linalg.vector_norm(flat(ideal_a), dim=1)
    ideal_u_norm = torch.linalg.vector_norm(flat(ideal_u), dim=1)
    ideal_w_norm = torch.linalg.vector_norm(flat(ideal_w), dim=1)
    applied_a_norm = torch.linalg.vector_norm(flat(applied_a), dim=1)
    applied_u_norm = torch.linalg.vector_norm(flat(applied_u), dim=1)
    applied_w_norm = torch.linalg.vector_norm(flat(applied_w), dim=1)
    tiny = torch.finfo(torch.float32).tiny

    stores["a_unchanged_fraction"][index] = torch.mean(
        (state.a == a_before).to(torch.float32), dim=1
    )
    stores["u_unchanged_fraction"][index] = torch.mean(
        (state.u == u_before).to(torch.float32), dim=(1, 2)
    )
    stores["w_sample_unchanged_fraction"][index] = torch.mean(
        (w_after == w_before).to(torch.float32), dim=1
    )
    stores["a_ideal_update_l2"][index] = ideal_a_norm
    stores["u_ideal_update_l2"][index] = ideal_u_norm
    stores["w_ideal_update_l2"][index] = step * tangent.w_derivative_l2
    stores["w_sample_ideal_update_l2"][index] = ideal_w_norm
    stores["a_applied_update_l2"][index] = applied_a_norm
    stores["u_applied_update_l2"][index] = applied_u_norm
    stores["w_sample_applied_update_l2"][index] = applied_w_norm
    stores["a_applied_to_ideal_ratio"][index] = applied_a_norm / torch.clamp(
        ideal_a_norm, min=tiny
    )
    stores["u_applied_to_ideal_ratio"][index] = applied_u_norm / torch.clamp(
        ideal_u_norm, min=tiny
    )
    stores["w_sample_applied_to_ideal_ratio"][index] = applied_w_norm / torch.clamp(
        ideal_w_norm, min=tiny
    )
    stores["a_update_cosine"][index] = torch.sum(
        flat(applied_a) * flat(ideal_a), dim=1
    ) / torch.clamp(applied_a_norm * ideal_a_norm, min=tiny)
    stores["u_update_cosine"][index] = torch.sum(
        flat(applied_u) * flat(ideal_u), dim=1
    ) / torch.clamp(applied_u_norm * ideal_u_norm, min=tiny)
    stores["w_sample_update_cosine"][index] = torch.sum(
        flat(applied_w) * flat(ideal_w), dim=1
    ) / torch.clamp(applied_w_norm * ideal_w_norm, min=tiny)


def _to_numpy(value: torch.Tensor) -> np.ndarray:
    return value.detach().cpu().numpy()


def simulate_point(
    point: Mapping[str, Any],
    *,
    device: torch.device,
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Run one fail-closed antithetic lineage until the common mean reaches stop_g."""

    validate_point(point)
    configuration = configuration_from_point(point)
    caps = point["caps"]
    guard = Guard(caps, device)
    max_steps = int(caps["max_steps"])
    step = float(point["step"])
    prefix_sizes = tuple(int(value) for value in point["prefix_digest_sizes"])
    state, initialization = model.build_antithetic_state(
        configuration,
        int(point["width"]),
        seed=int(point["seed"]),
        lineage=int(point["lineage"]),
        device=device,
        row_block=int(point["rng_row_block"]),
        prefix_sizes=prefix_sizes,
    )
    row_np, col_np, monitor_sha = model.audited_init.monitor_coordinates(
        int(point["w_monitor_sample_size"]),
        seed=int(point["w_monitor_seed"]),
        extent=int(point["w_monitor_extent"]),
    )
    rows = torch.from_numpy(row_np).to(device=device)
    cols = torch.from_numpy(col_np).to(device=device)
    obs_store, update_store, state_store = _allocate_stores(max_steps, device)
    validity_store = torch.empty(
        max_steps + 1, dtype=torch.bool, device=device
    )
    diagnostic_stride = int(point["diagnostic_stride"])
    wall_sync_stride = int(point["wall_sync_stride"])
    full_w_steps: list[int] = []
    full_w_maxima: list[np.ndarray] = []

    reached = False
    with torch.no_grad():
        tangent, obs = model.fused_eval(state, configuration)
        maxima, valid = _cheap_validity(state, obs, rows, cols, caps)
        validity_store[0] = valid
        _record_observables(obs_store, 0, obs)
        for key, value in maxima.items():
            state_store[key][0] = value
        full_w_steps.append(0)
        full_w_maxima.append(_to_numpy(_validate_full_W(state, caps)))
        if not bool(validity_store[0].item()):
            raise NumericalInvalid("initial cheap observable/channel check failed")
        initial_mean_g = float(torch.mean(obs.g).item())
        if initial_mean_g >= float(point["stop_g"]):
            raise NumericalInvalid("initial state already reached the stop coordinate")
        previous_g_tensor = torch.mean(obs.g)
        previous_loss_tensor = torch.mean(obs.loss_full)
        last_validity_check = 1
        guard.check()

        for index in range(max_steps):
            _record_update(
                update_store, index, state, tangent, step, rows, cols
            )
            del tangent, obs
            tangent, obs = model.fused_eval(state, configuration)
            guard.completed_steps = index + 1
            maxima, valid = _cheap_validity(state, obs, rows, cols, caps)
            _record_observables(obs_store, index + 1, obs)
            for key, value in maxima.items():
                state_store[key][index + 1] = value
            mean_g_tensor = torch.mean(obs.g)
            mean_loss_tensor = torch.mean(obs.loss_full)
            valid = valid & (
                mean_g_tensor
                >= previous_g_tensor
                - float(caps["mean_g_monotonicity_tolerance"])
            )
            valid = valid & (
                mean_loss_tensor
                <= previous_loss_tensor
                + float(caps["mean_loss_monotonicity_tolerance"])
            )
            validity_store[index + 1] = valid
            previous_g_tensor = mean_g_tensor
            previous_loss_tensor = mean_loss_tensor

            step_number = index + 1
            diagnostic_due = step_number % diagnostic_stride == 0
            sync_due = (
                diagnostic_due
                or step_number % wall_sync_stride == 0
                or step_number == max_steps
            )
            if diagnostic_due:
                full_w_steps.append(step_number)
                full_w_maxima.append(_to_numpy(_validate_full_W(state, caps)))
            if not sync_due:
                continue
            if device.type == "cuda":
                torch.cuda.synchronize(device)
            if not bool(
                torch.all(
                    validity_store[last_validity_check : step_number + 1]
                ).item()
            ):
                raise NumericalInvalid(
                    "cheap observable/channel or monotonicity check failed"
                )
            last_validity_check = step_number + 1
            guard.check()
            mean_g = float(mean_g_tensor.item())
            mean_loss = float(mean_loss_tensor.item())
            if progress_callback is not None:
                progress_callback(
                    {
                        **guard.snapshot(),
                        "mean_g": mean_g,
                        "mean_full_loss": mean_loss,
                    }
                )
            if mean_g >= float(point["stop_g"]):
                if not full_w_steps or full_w_steps[-1] != step_number:
                    full_w_steps.append(step_number)
                    full_w_maxima.append(
                        _to_numpy(_validate_full_W(state, caps))
                    )
                guard.check()
                reached = True
                break

    if not reached:
        error = BudgetStop("step cap reached before stop_g")
        error.point_diagnostics = guard.snapshot()
        raise error

    completed = guard.completed_steps
    arrays = {
        key: _to_numpy(value[: completed + 1])
        for key, value in obs_store.items()
    }
    arrays.update(
        {
            key: _to_numpy(value[:completed])
            for key, value in update_store.items()
        }
    )
    arrays.update(
        {
            key: _to_numpy(value[: completed + 1])
            for key, value in state_store.items()
        }
    )
    arrays["time"] = step * np.arange(completed + 1, dtype=np.float64)
    arrays["w_monitor_rows"] = row_np.astype(np.int64)
    arrays["w_monitor_cols"] = col_np.astype(np.int64)
    arrays["w_monitor_sha256"] = np.asarray(monitor_sha.encode("ascii"), dtype="S64")
    arrays["initial_state_sha256"] = np.asarray(
        initialization["physical_state_sha256"].encode("ascii"), dtype="S64"
    )
    arrays["prefix_digest_sizes"] = np.asarray(prefix_sizes, dtype=np.int64)
    arrays["initial_prefix_sha256"] = np.asarray(
        [
            initialization["physical_prefix_sha256"][size].encode("ascii")
            for size in prefix_sizes
        ],
        dtype="S64",
    )
    arrays["full_w_check_steps"] = np.asarray(full_w_steps, dtype=np.int64)
    arrays["full_w_max_abs_at_checks"] = np.asarray(
        full_w_maxima, dtype=np.float32
    )

    node_fields = {
        key: arrays[key]
        for key in SCALAR_OBSERVABLES
        if key not in ("loss_full", "loss_projected")
    }
    node_fields.update(
        {
            "loss_full": arrays["loss_full"],
            "loss_projected": arrays["loss_projected"],
            "q1": arrays["q1"],
            "q2": arrays["q2"],
        }
    )
    node_arrays = common_g_clock(
        arrays["time"],
        arrays["g"],
        node_fields,
        np.asarray(point["output_nodes"], dtype=np.float64),
    )
    arrays.update(node_arrays)
    leakage = leakage_series(
        arrays["g"],
        arrays["delta"],
        arrays["kernel_g"],
        arrays["kernel_delta"],
        arrays["cross_kernel"],
    )
    arrays.update(leakage)

    monotonicity = monotonicity_diagnostics(
        arrays["g"],
        arrays["loss_full"],
        g_tolerance=float(caps["mean_g_monotonicity_tolerance"]),
        loss_tolerance=float(caps["mean_loss_monotonicity_tolerance"]),
    )
    driver = driver_diagnostics(
        arrays["time"],
        arrays["g"],
        arrays["effective_numerator"],
        through_g=float(point["stop_g"]),
    )
    leakage_summary = leakage_diagnostics(
        arrays["g"],
        arrays["delta"],
        arrays["kernel_g"],
        arrays["kernel_delta"],
        arrays["cross_kernel"],
        through_g=float(point["stop_g"]),
    )
    update_summary = {
        f"maximum_{key}": float(np.max(arrays[key]))
        for key in (
            "a_unchanged_fraction",
            "u_unchanged_fraction",
            "w_sample_unchanged_fraction",
        )
    }
    update_summary.update(
        {
            f"minimum_{key}": float(np.min(arrays[key]))
            for key in (
                "a_applied_to_ideal_ratio",
                "u_applied_to_ideal_ratio",
                "w_sample_applied_to_ideal_ratio",
                "a_update_cosine",
                "u_update_cosine",
                "w_sample_update_cosine",
            )
        }
    )
    diagnostics = {
        **guard.snapshot(),
        "reached_stop_g": True,
        "final_mean_g": float(np.mean(arrays["g"][-1])),
        "initialization": initialization,
        "w_monitor_sha256": monitor_sha,
        "exact_initial_kernel_control": model.finite_width_initial_kernel_means(
            configuration, int(point["width"])
        ),
        "monotonicity": monotonicity,
        "driver": driver,
        "leakage": leakage_summary,
        "updates": update_summary,
    }
    return arrays, diagnostics
