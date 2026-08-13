#!/usr/bin/env python3
"""Bounded finite-width reference solvers for the global proxy campaign."""

from __future__ import annotations

import math
import resource
import time
from dataclasses import dataclass
from typing import Any

import numpy as np
import torch

from canonical_model import (
    Observables,
    State,
    add_scaled,
    generate_antithetic_state,
    linear_combination,
    observables,
    scaled_rhs,
    state_all_finite,
    state_max_abs,
)


class BudgetStop(RuntimeError):
    """A declared point-level resource cap was reached."""


class NumericalInvalid(RuntimeError):
    """A fail-closed numerical validity condition was violated."""


@dataclass(frozen=True)
class PointCaps:
    wall_seconds: float
    max_steps: int
    host_rss_gib: float
    gpu_memory_gib: float
    state_ceiling: float
    kernel_ceiling: float
    kernel_floor: float
    diagnostic_stride: int


class BudgetGuard:
    def __init__(self, caps: PointCaps, device: torch.device) -> None:
        self.caps = caps
        self.device = device
        self.start = time.monotonic()
        self.steps = 0
        self.max_host_rss_gib = 0.0
        self.max_gpu_allocated_gib = 0.0

    @staticmethod
    def _host_max_rss_gib() -> float:
        # Linux reports ru_maxrss in KiB.
        return float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20

    def check(self, *, count_step: bool = False) -> None:
        if count_step:
            self.steps += 1
        elapsed = time.monotonic() - self.start
        self.max_host_rss_gib = max(self.max_host_rss_gib, self._host_max_rss_gib())
        if self.device.type == "cuda":
            allocated = torch.cuda.max_memory_allocated(self.device) / 2**30
            self.max_gpu_allocated_gib = max(self.max_gpu_allocated_gib, allocated)
        if elapsed > self.caps.wall_seconds:
            raise BudgetStop(
                f"point wall cap reached: {elapsed:.3f}s > {self.caps.wall_seconds:.3f}s"
            )
        if self.steps > self.caps.max_steps:
            raise BudgetStop(
                f"point step cap reached: {self.steps} > {self.caps.max_steps}"
            )
        if self.max_host_rss_gib > self.caps.host_rss_gib:
            raise BudgetStop(
                "host RSS cap reached: "
                f"{self.max_host_rss_gib:.3f} GiB > {self.caps.host_rss_gib:.3f} GiB"
            )
        if (
            self.device.type == "cuda"
            and self.max_gpu_allocated_gib > self.caps.gpu_memory_gib
        ):
            raise BudgetStop(
                "GPU allocation cap reached: "
                f"{self.max_gpu_allocated_gib:.3f} GiB > "
                f"{self.caps.gpu_memory_gib:.3f} GiB"
            )

    def summary(self) -> dict[str, float | int]:
        return {
            "elapsed_seconds": time.monotonic() - self.start,
            "integrator_steps_all_batches": self.steps,
            "max_host_rss_gib": self.max_host_rss_gib,
            "max_gpu_allocated_gib": self.max_gpu_allocated_gib,
        }


def integrator_step(
    state: State,
    step: float,
    *,
    mode: str,
    method: str,
    target: float,
    kernel_floor: float,
) -> State:
    """One explicit fixed step.  No curve differentiation is used."""

    if method == "midpoint":
        k1, _ = scaled_rhs(
            state, mode, target=target, kernel_floor=kernel_floor
        )
        midpoint = add_scaled(state, k1, 0.5 * step)
        k2, _ = scaled_rhs(
            midpoint, mode, target=target, kernel_floor=kernel_floor
        )
        return add_scaled(state, k2, step)
    if method == "rk4":
        k1, _ = scaled_rhs(
            state, mode, target=target, kernel_floor=kernel_floor
        )
        k2, _ = scaled_rhs(
            add_scaled(state, k1, 0.5 * step),
            mode,
            target=target,
            kernel_floor=kernel_floor,
        )
        k3, _ = scaled_rhs(
            add_scaled(state, k2, 0.5 * step),
            mode,
            target=target,
            kernel_floor=kernel_floor,
        )
        k4, _ = scaled_rhs(
            add_scaled(state, k3, step),
            mode,
            target=target,
            kernel_floor=kernel_floor,
        )
        return linear_combination(
            state,
            ((1.0 / 6.0, k1), (1.0 / 3.0, k2), (1.0 / 3.0, k3), (1.0 / 6.0, k4)),
            step,
        )
    raise ValueError(f"unknown integration method: {method!r}")


def _to_numpy(tensor: torch.Tensor) -> np.ndarray:
    return tensor.detach().cpu().numpy().astype(np.float64, copy=False)


def _record(obs: Observables, target: float) -> dict[str, np.ndarray]:
    residual = target - obs.output
    return {
        "output": _to_numpy(obs.output),
        "kernel": _to_numpy(obs.kernel),
        "weighted_kernel": _to_numpy(residual * obs.kernel),
        "loss": _to_numpy(residual.square()),
        "q1": _to_numpy(obs.q1),
        "q2": _to_numpy(obs.q2),
        "kernel_a": _to_numpy(obs.kernel_a),
        "kernel_W": _to_numpy(obs.kernel_W),
        "kernel_u": _to_numpy(obs.kernel_u),
    }


def _validate_state_and_observables(
    state: State,
    obs: Observables,
    caps: PointCaps,
    *,
    check_state_amplitude: bool,
) -> float:
    if bool(torch.any(~torch.isfinite(obs.output)).item()):
        raise NumericalInvalid("nonfinite output")
    if bool(torch.any(~torch.isfinite(obs.kernel)).item()):
        raise NumericalInvalid("nonfinite kernel")
    if bool(torch.any(obs.kernel <= caps.kernel_floor).item()):
        raise NumericalInvalid("kernel at or below declared floor")
    if bool(torch.any(obs.kernel >= caps.kernel_ceiling).item()):
        raise NumericalInvalid("kernel at or above declared ceiling")
    if not check_state_amplitude:
        return math.nan
    if not state_all_finite(state):
        raise NumericalInvalid("nonfinite parameter state")
    amplitude = float(torch.amax(state_max_abs(state)).item())
    if amplitude >= caps.state_ceiling:
        raise NumericalInvalid(
            f"state ceiling reached: {amplitude:.6g} >= {caps.state_ceiling:.6g}"
        )
    return amplitude


def _integer_steps(endpoint: float, step: float) -> int:
    steps = int(round(endpoint / step))
    if steps < 0 or not math.isclose(steps * step, endpoint, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("endpoint must be a nonnegative exact step endpoint")
    return steps


def simulate_batch(
    point: dict[str, Any],
    *,
    pair_offset: int,
    pair_count: int,
    device: torch.device,
    dtype: torch.dtype,
    guard: BudgetGuard,
) -> dict[str, Any]:
    """Simulate one memory-bounded antithetic batch."""

    mode = str(point["mode"])
    if mode not in {"physical", "output_clock"}:
        raise ValueError("mode must be physical or output_clock")
    endpoint_key = "max_time" if mode == "physical" else "max_output"
    endpoint = float(point[endpoint_key])
    step = float(point["step"])
    steps = _integer_steps(endpoint, step)
    if steps > guard.caps.max_steps:
        raise BudgetStop(
            f"declared integration needs {steps} steps, cap is {guard.caps.max_steps}"
        )
    microcanonical = bool(point.get("microcanonical_readout", False))
    if mode == "output_clock" and not microcanonical:
        raise ValueError("output_clock mode requires microcanonical_readout=true")
    if mode == "physical" and microcanonical:
        raise ValueError("ordinary physical mode must not microcanonically condition")

    state, init = generate_antithetic_state(
        int(point["width"]),
        pair_count,
        int(point["seed_base"]),
        device=device,
        dtype=dtype,
        pair_offset=pair_offset,
        microcanonical_readout=microcanonical,
    )
    target = float(point.get("target", 1.0))
    method = str(point.get("integrator", "midpoint"))
    coordinates = np.arange(steps + 1, dtype=np.float64) * step
    fields = (
        "output",
        "kernel",
        "weighted_kernel",
        "loss",
        "q1",
        "q2",
        "kernel_a",
        "kernel_W",
        "kernel_u",
    )
    curves = {
        key: np.empty((steps + 1, 2 * pair_count), dtype=np.float64)
        for key in fields
    }
    max_state_amplitude = 0.0
    with torch.no_grad():
        obs = observables(state)
        initial_amplitude = _validate_state_and_observables(
            state, obs, guard.caps, check_state_amplitude=True
        )
        max_state_amplitude = max(max_state_amplitude, initial_amplitude)
        first = _record(obs, target)
        for key in fields:
            curves[key][0] = first[key]
        for index in range(1, steps + 1):
            state = integrator_step(
                state,
                step,
                mode=mode,
                method=method,
                target=target,
                kernel_floor=guard.caps.kernel_floor,
            )
            obs = observables(state)
            check_amplitude = (
                index % guard.caps.diagnostic_stride == 0 or index == steps
            )
            amplitude = _validate_state_and_observables(
                state,
                obs,
                guard.caps,
                check_state_amplitude=check_amplitude,
            )
            if math.isfinite(amplitude):
                max_state_amplitude = max(max_state_amplitude, amplitude)
            values = _record(obs, target)
            for key in fields:
                curves[key][index] = values[key]
            guard.check(count_step=True)

    initial_output = _to_numpy(init["initial_output"])
    pair_initial_sum = initial_output.reshape(pair_count, 2).sum(axis=1)
    result: dict[str, Any] = {
        "coordinate": coordinates,
        **curves,
        "max_state_amplitude": max_state_amplitude,
        "max_abs_antithetic_initial_output_sum": float(
            np.max(np.abs(pair_initial_sum))
        ),
        "max_abs_initial_output": float(np.max(np.abs(initial_output))),
        "projection_relative_norm": _to_numpy(init["projection_relative_norm"]),
    }
    return result


def _pair_average_numpy(values: np.ndarray) -> np.ndarray:
    if values.shape[-1] % 2:
        raise ValueError("raw trajectory count is not even")
    new_shape = values.shape[:-1] + (values.shape[-1] // 2, 2)
    return values.reshape(new_shape).mean(axis=-1)


def _interpolate_rows(
    x: np.ndarray,
    rows: np.ndarray,
    nodes: np.ndarray,
) -> np.ndarray:
    return np.vstack([np.interp(nodes, x, rows[:, j]) for j in range(rows.shape[1])]).T


def aggregate_physical(
    batches: list[dict[str, Any]],
    output_nodes: np.ndarray,
    *,
    target: float,
    monotonic_tolerance: float,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    coordinate = batches[0]["coordinate"]
    raw = {
        key: np.concatenate([batch[key] for batch in batches], axis=1)
        for key in (
            "output",
            "kernel",
            "weighted_kernel",
            "loss",
            "q1",
            "q2",
            "kernel_a",
            "kernel_W",
            "kernel_u",
        )
    }
    mean_output = raw["output"].mean(axis=1)
    increments = np.diff(mean_output)
    if float(np.min(increments)) < -monotonic_tolerance:
        raise NumericalInvalid(
            "ensemble mean output is nonmonotone beyond declared tolerance"
        )
    if output_nodes[0] < mean_output[0] - monotonic_tolerance:
        raise NumericalInvalid("first requested mean-output node precedes the trajectory")
    if output_nodes[-1] > mean_output[-1] + monotonic_tolerance:
        raise NumericalInvalid("physical-time cap did not reach the final output node")

    # Remove only exact/repeated abscissas for interpolation; do not isotonic-fit
    # or otherwise alter a scientifically meaningful nonmonotone trajectory.
    keep = np.concatenate(([True], np.diff(mean_output) > 0.0))
    if int(np.count_nonzero(keep)) < 2:
        raise NumericalInvalid("mean-output grid is degenerate")
    x = mean_output[keep]
    t = coordinate[keep]
    node_time = np.interp(output_nodes, x, t)
    node_raw = {
        key: _interpolate_rows(x, values[keep], output_nodes)
        for key, values in raw.items()
    }
    mean_weighted = node_raw["weighted_kernel"].mean(axis=1)
    denominator = target - output_nodes
    if np.any(denominator <= 0.0):
        raise NumericalInvalid("physical effective kernel requires output nodes below one")
    effective_kernel = mean_weighted / denominator
    summary_arrays = {
        "output_nodes": output_nodes,
        "physical_time_at_nodes": node_time,
        "effective_kernel": effective_kernel,
        "mean_direct_kernel": node_raw["kernel"].mean(axis=1),
        "mean_loss": node_raw["loss"].mean(axis=1),
        "loss_of_mean_output": np.square(denominator),
        "mean_q1": node_raw["q1"].mean(axis=1),
        "mean_q2": node_raw["q2"].mean(axis=1),
        "mean_kernel_a": node_raw["kernel_a"].mean(axis=1),
        "mean_kernel_W": node_raw["kernel_W"].mean(axis=1),
        "mean_kernel_u": node_raw["kernel_u"].mean(axis=1),
        "raw_time": coordinate,
        "raw_mean_output": mean_output,
        "raw_mean_effective_numerator": raw["weighted_kernel"].mean(axis=1),
        "raw_trajectory_output": raw["output"],
        "raw_trajectory_kernel": raw["kernel"],
        "raw_trajectory_weighted_kernel": raw["weighted_kernel"],
        "raw_trajectory_loss": raw["loss"],
        "node_raw_output": node_raw["output"],
        "node_raw_kernel": node_raw["kernel"],
        "node_raw_weighted_kernel": node_raw["weighted_kernel"],
        "node_raw_loss": node_raw["loss"],
        "node_pair_output": _pair_average_numpy(node_raw["output"]),
        "node_pair_kernel": _pair_average_numpy(node_raw["kernel"]),
        "node_pair_weighted_kernel": _pair_average_numpy(
            node_raw["weighted_kernel"]
        ),
    }
    diagnostics = {
        "initial_mean_output": float(mean_output[0]),
        "terminal_mean_output": float(mean_output[-1]),
        "minimum_mean_output_increment": float(np.min(increments)),
        "maximum_output_variance_at_nodes": float(
            np.max(np.var(node_raw["output"], axis=1, ddof=1))
        ),
        "maximum_loss_jensen_gap_at_nodes": float(
            np.max(summary_arrays["mean_loss"] - summary_arrays["loss_of_mean_output"])
        ),
        "trajectory_count": int(raw["output"].shape[1]),
    }
    return summary_arrays, diagnostics


def cumulative_trapezoid(values: np.ndarray, step: float) -> np.ndarray:
    result = np.zeros_like(values)
    if len(values) > 1:
        result[1:] = np.cumsum(0.5 * step * (values[:-1] + values[1:]))
    return result


def aggregate_output_clock(
    batches: list[dict[str, Any]],
    output_nodes: np.ndarray,
    *,
    target: float,
    output_defect_tolerance: float,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    coordinate = batches[0]["coordinate"]
    raw = {
        key: np.concatenate([batch[key] for batch in batches], axis=1)
        for key in (
            "output",
            "kernel",
            "loss",
            "q1",
            "q2",
            "kernel_a",
            "kernel_W",
            "kernel_u",
        )
    }
    defect = raw["output"] - coordinate[:, None]
    max_defect = float(np.max(np.abs(defect)))
    if max_defect > output_defect_tolerance:
        raise NumericalInvalid(
            f"output-clock identity defect {max_defect:.6g} exceeds "
            f"{output_defect_tolerance:.6g}"
        )
    if output_nodes[0] < coordinate[0] or output_nodes[-1] > coordinate[-1]:
        raise NumericalInvalid("requested output node is outside output-clock range")
    node_raw = {
        key: _interpolate_rows(coordinate, values, output_nodes)
        for key, values in raw.items()
    }
    mean_kernel_full = raw["kernel"].mean(axis=1)
    denominator = 2.0 * (target - coordinate) * mean_kernel_full
    if np.any(denominator <= 0.0):
        raise NumericalInvalid("cannot reconstruct physical time at or beyond output one")
    physical_time_full = cumulative_trapezoid(
        np.reciprocal(denominator), coordinate[1] - coordinate[0]
    )
    summary_arrays = {
        "output_nodes": output_nodes,
        "mean_kernel": node_raw["kernel"].mean(axis=1),
        "mean_loss": node_raw["loss"].mean(axis=1),
        "mean_q1": node_raw["q1"].mean(axis=1),
        "mean_q2": node_raw["q2"].mean(axis=1),
        "mean_kernel_a": node_raw["kernel_a"].mean(axis=1),
        "mean_kernel_W": node_raw["kernel_W"].mean(axis=1),
        "mean_kernel_u": node_raw["kernel_u"].mean(axis=1),
        "physical_time_from_mean_kernel": np.interp(
            output_nodes, coordinate, physical_time_full
        ),
        "raw_output_clock": coordinate,
        "raw_mean_kernel": mean_kernel_full,
        "raw_physical_time_from_mean_kernel": physical_time_full,
        "raw_trajectory_output": raw["output"],
        "raw_trajectory_kernel": raw["kernel"],
        "raw_trajectory_loss": raw["loss"],
        "node_raw_output": node_raw["output"],
        "node_raw_kernel": node_raw["kernel"],
        "node_raw_loss": node_raw["loss"],
        "node_pair_kernel": _pair_average_numpy(node_raw["kernel"]),
    }
    diagnostics = {
        "maximum_absolute_output_clock_defect": max_defect,
        "maximum_output_variance_at_nodes": float(
            np.max(np.var(node_raw["output"], axis=1, ddof=1))
        ),
        "trajectory_count": int(raw["output"].shape[1]),
        "max_projection_relative_norm": float(
            max(np.max(batch["projection_relative_norm"]) for batch in batches)
        ),
    }
    return summary_arrays, diagnostics


def run_point(
    point: dict[str, Any],
    *,
    device: torch.device,
    dtype: torch.dtype,
    caps: PointCaps,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Run one declared point, respecting its batch and resource caps."""

    guard = BudgetGuard(caps, device)
    pair_count = int(point["antithetic_pairs"])
    pair_batch_size = int(point["pair_batch_size"])
    if pair_batch_size < 1 or pair_batch_size > pair_count:
        raise ValueError("pair_batch_size must lie in [1, antithetic_pairs]")
    batches: list[dict[str, Any]] = []
    for offset in range(0, pair_count, pair_batch_size):
        current = min(pair_batch_size, pair_count - offset)
        guard.check()
        batches.append(
            simulate_batch(
                point,
                pair_offset=offset,
                pair_count=current,
                device=device,
                dtype=dtype,
                guard=guard,
            )
        )

    output_nodes = np.asarray(point["output_nodes"], dtype=np.float64)
    if np.any(np.diff(output_nodes) < 0.0):
        raise ValueError("output_nodes must be nondecreasing")
    if point["mode"] == "physical":
        arrays, diagnostics = aggregate_physical(
            batches,
            output_nodes,
            target=float(point.get("target", 1.0)),
            monotonic_tolerance=float(point["monotonic_tolerance"]),
        )
    else:
        arrays, diagnostics = aggregate_output_clock(
            batches,
            output_nodes,
            target=float(point.get("target", 1.0)),
            output_defect_tolerance=float(point["output_defect_tolerance"]),
        )
    diagnostics.update(guard.summary())
    diagnostics.update(
        {
            "max_state_amplitude": float(
                max(batch["max_state_amplitude"] for batch in batches)
            ),
            "max_abs_antithetic_initial_output_sum": float(
                max(
                    batch["max_abs_antithetic_initial_output_sum"]
                    for batch in batches
                )
            ),
            "max_abs_initial_output": float(
                max(batch["max_abs_initial_output"] for batch in batches)
            ),
        }
    )
    return arrays, diagnostics
