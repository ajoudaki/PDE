#!/usr/bin/env python3
"""FP32 Euler/RK4 validation engine with exact update-stall monitoring."""

from __future__ import annotations

import gc
import math
import resource
import time
from dataclasses import dataclass
from typing import Any, Callable

import numpy as np
import torch

from nested_init import generate_lineage, monitor_coordinates


@dataclass
class State:
    a: torch.Tensor
    W: torch.Tensor
    u: torch.Tensor

    @property
    def width(self) -> int:
        return int(self.a.shape[1])


@dataclass
class Observables:
    output: torch.Tensor
    kernel: torch.Tensor
    kernel_a: torch.Tensor
    kernel_W: torch.Tensor
    kernel_u: torch.Tensor


@dataclass
class Tangent:
    a: torch.Tensor
    W: torch.Tensor
    u: torch.Tensor
    w_derivative_l2: torch.Tensor
    w_state_inner_derivative: torch.Tensor


class BudgetStop(RuntimeError):
    pass


class NumericalInvalid(RuntimeError):
    pass


class Guard:
    def __init__(self, caps: dict[str, Any], device: torch.device) -> None:
        self.caps = caps
        self.device = device
        self.started = time.monotonic()
        self.steps = 0
        self.max_gpu_gib = 0.0
        self.max_host_gib = 0.0
        if self.device.type == "cuda":
            torch.cuda.synchronize(self.device)
            torch.cuda.reset_peak_memory_stats(self.device)

    def snapshot(self) -> dict[str, float | int]:
        host = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20
        self.max_host_gib = max(self.max_host_gib, host)
        if self.device.type == "cuda":
            gpu = float(torch.cuda.max_memory_allocated(self.device)) / 2**30
            self.max_gpu_gib = max(self.max_gpu_gib, gpu)
        return {
            "elapsed_seconds": time.monotonic() - self.started,
            "steps": self.steps,
            "max_host_rss_gib": self.max_host_gib,
            "max_gpu_allocated_gib": self.max_gpu_gib,
        }

    def before_step(self) -> None:
        record = self.snapshot()
        if record["elapsed_seconds"] >= float(self.caps["wall_seconds"]):
            self._stop("wall cap reached")
        if self.steps >= int(self.caps["max_steps_all_lineages"]):
            self._stop("step cap reached before next step")
        if self.max_host_gib > float(self.caps["host_rss_gib"]):
            self._stop("host RSS cap reached")
        if self.device.type == "cuda" and self.max_gpu_gib > float(
            self.caps["gpu_memory_gib"]
        ):
            self._stop("GPU allocation cap reached")

    def after_step(self) -> None:
        """A completed final step may itself cross a wall or memory cap."""

        record = self.snapshot()
        if record["elapsed_seconds"] >= float(self.caps["wall_seconds"]):
            self._stop("wall cap crossed by completed step")
        if self.max_host_gib > float(self.caps["host_rss_gib"]):
            self._stop("host RSS cap crossed by completed step")
        if self.device.type == "cuda" and self.max_gpu_gib > float(
            self.caps["gpu_memory_gib"]
        ):
            self._stop("GPU allocation cap crossed by completed step")

    def _stop(self, message: str) -> None:
        exc = BudgetStop(message)
        exc.point_diagnostics = self.snapshot()
        raise exc


def fused_eval(state: State, *, target: float = 1.0) -> tuple[Tangent, Observables]:
    n = state.width
    inv_n = 1.0 / n
    inv_sqrt_n = 1.0 / math.sqrt(n)
    u2 = state.u.square()
    z = torch.bmm(state.W, u2.unsqueeze(-1)).squeeze(-1) * inv_sqrt_n
    az = state.a * z
    v = torch.bmm(state.W.transpose(1, 2), az.unsqueeze(-1)).squeeze(-1)
    output = torch.mean(state.a * z.square(), dim=1)
    sum_u4 = torch.sum(u2.square(), dim=1)
    sum_az2 = torch.sum(az.square(), dim=1)
    kernel_a = inv_n * torch.sum(z.pow(4), dim=1)
    kernel_W = 4.0 * inv_n**2 * sum_az2 * sum_u4
    kernel_u = 16.0 * inv_n**2 * torch.sum(u2 * v.square(), dim=1)
    obs = Observables(
        output=output,
        kernel=kernel_a + kernel_W + kernel_u,
        kernel_a=kernel_a,
        kernel_W=kernel_W,
        kernel_u=kernel_u,
    )
    factor = 2.0 * (target - output)
    da = z.square() * factor[:, None]
    coefficient = (2.0 * inv_sqrt_n) * factor
    dW = coefficient[:, None, None] * az.unsqueeze(2) * u2.unsqueeze(1)
    du = (4.0 * inv_sqrt_n) * state.u * v * factor[:, None]
    # Exact algebraic norms avoid an additional full W reduction each step.
    dW_l2 = (
        torch.abs(coefficient)
        * torch.linalg.vector_norm(az, dim=1)
        * torch.linalg.vector_norm(u2, dim=1)
    )
    W_inner_dW = 2.0 * factor * float(n) * output
    return Tangent(da, dW, du, dW_l2, W_inner_dW), obs


def _add_state(state: State, tangent: Tangent, scale: float) -> State:
    return State(
        state.a + scale * tangent.a,
        state.W + scale * tangent.W,
        state.u + scale * tangent.u,
    )


def rk4_step(state: State, k1: Tangent, step: float, *, target: float) -> State:
    k2, _ = fused_eval(_add_state(state, k1, 0.5 * step), target=target)
    k3, _ = fused_eval(_add_state(state, k2, 0.5 * step), target=target)
    k4, _ = fused_eval(_add_state(state, k3, step), target=target)
    return State(
        state.a
        + step
        * (k1.a / 6.0 + k2.a / 3.0 + k3.a / 3.0 + k4.a / 6.0),
        state.W
        + step
        * (k1.W / 6.0 + k2.W / 3.0 + k3.W / 3.0 + k4.W / 6.0),
        state.u
        + step
        * (k1.u / 6.0 + k2.u / 3.0 + k3.u / 3.0 + k4.u / 6.0),
    )


def _build_state(
    width: int,
    seed: int,
    lineage: int,
    device: torch.device,
    row_block: int,
    prefix_sizes: tuple[int, ...],
) -> tuple[State, str, dict[int, str]]:
    a_np, u_np, W_np, digest, prefix_digests = generate_lineage(
        width,
        seed=seed,
        lineage=lineage,
        row_block=row_block,
        prefix_sizes=prefix_sizes,
    )
    a0 = torch.from_numpy(a_np).to(device=device)
    u0 = torch.from_numpy(u_np).to(device=device)
    W0 = torch.from_numpy(W_np).to(device=device)
    a = torch.stack((a0, -a0), dim=0)
    u = torch.stack((u0, u0), dim=0)
    W = torch.stack((W0, W0), dim=0)
    del a_np, u_np, W_np, a0, u0, W0
    gc.collect()
    return State(a, W, u), digest, prefix_digests


OBS_FIELDS = (
    "output",
    "kernel",
    "kernel_a",
    "kernel_W",
    "kernel_u",
    "weighted_kernel",
    "loss",
)

UPDATE_FIELDS = (
    "a_unchanged_fraction",
    "u_unchanged_fraction",
    "w_sample_unchanged_fraction",
    "a_ideal_update_l2",
    "u_ideal_update_l2",
    "w_ideal_update_l2",
    "a_applied_update_l2",
    "u_applied_update_l2",
    "w_sample_ideal_update_l2",
    "w_sample_applied_update_l2",
    "w_sample_applied_to_ideal_ratio",
    "a_applied_to_ideal_ratio",
    "u_applied_to_ideal_ratio",
    "a_update_cosine",
    "u_update_cosine",
    "w_sample_update_cosine",
)

STATE_FIELDS = (
    "a_l2",
    "u_l2",
    "w_ideal_recurrence_l2",
    "w_sample_l2",
    "max_abs_a",
    "max_abs_u",
    "max_abs_w_sample",
)


def _record_obs(storage, row: int, obs: Observables) -> None:
    residual = 1.0 - obs.output
    storage["output"][row] = obs.output
    storage["kernel"][row] = obs.kernel
    storage["kernel_a"][row] = obs.kernel_a
    storage["kernel_W"][row] = obs.kernel_W
    storage["kernel_u"][row] = obs.kernel_u
    storage["weighted_kernel"][row] = residual * obs.kernel
    storage["loss"][row] = residual.square()


def _record_state(storage, row: int, state: State, w_norm2, rows, cols) -> None:
    sample = state.W[:, rows, cols]
    storage["a_l2"][row] = torch.linalg.vector_norm(state.a, dim=1)
    storage["u_l2"][row] = torch.linalg.vector_norm(state.u, dim=1)
    storage["w_ideal_recurrence_l2"][row] = torch.sqrt(
        torch.clamp(w_norm2, min=0.0)
    ).to(torch.float32)
    storage["w_sample_l2"][row] = torch.linalg.vector_norm(sample, dim=1)
    storage["max_abs_a"][row] = torch.amax(torch.abs(state.a), dim=1)
    storage["max_abs_u"][row] = torch.amax(torch.abs(state.u), dim=1)
    storage["max_abs_w_sample"][row] = torch.amax(torch.abs(sample), dim=1)


def _validate_current(
    state: State,
    obs: Observables,
    rows,
    cols,
    *,
    full_W: bool,
    caps: dict[str, Any],
) -> None:
    tensors = (
        obs.output,
        obs.kernel,
        obs.kernel_a,
        obs.kernel_W,
        obs.kernel_u,
        state.a,
        state.u,
        state.W[:, rows, cols],
    )
    if not all(bool(torch.all(torch.isfinite(value)).item()) for value in tensors):
        raise NumericalInvalid("nonfinite state, sample, or observable")
    if bool(torch.any(obs.kernel <= 0.0).item()):
        raise NumericalInvalid("nonpositive direct kernel")
    if any(
        bool(torch.any(component <= 0.0).item())
        for component in (obs.kernel_a, obs.kernel_W, obs.kernel_u)
    ):
        raise NumericalInvalid("nonpositive kernel component")
    if bool(torch.any(obs.kernel < float(caps["kernel_floor"])).item()):
        raise NumericalInvalid("kernel below declared floor")
    if bool(torch.any(obs.kernel > float(caps["kernel_ceiling"])).item()):
        raise NumericalInvalid("kernel above declared ceiling")
    component_sum = obs.kernel_a + obs.kernel_W + obs.kernel_u
    component_scale = torch.maximum(torch.abs(obs.kernel), torch.ones_like(obs.kernel))
    component_tolerance = (
        float(caps["component_sum_ulp_multiplier"])
        * torch.finfo(torch.float32).eps
        * component_scale
    )
    if bool(torch.any(torch.abs(obs.kernel - component_sum) > component_tolerance).item()):
        raise NumericalInvalid("direct kernel fails component-sum identity")
    sample_ceiling = max(
        float(torch.amax(torch.abs(state.a)).item()),
        float(torch.amax(torch.abs(state.u)).item()),
        float(torch.amax(torch.abs(state.W[:, rows, cols])).item()),
    )
    if sample_ceiling >= float(caps["state_ceiling"]):
        raise NumericalInvalid("sampled state exceeds declared ceiling")
    if full_W:
        if not bool(torch.all(torch.isfinite(state.W)).item()):
            raise NumericalInvalid("nonfinite full W state")
        if float(torch.amax(torch.abs(state.W)).item()) >= float(
            caps["state_ceiling"]
        ):
            raise NumericalInvalid("full W state exceeds declared ceiling")


def simulate_lineage(
    point: dict[str, Any],
    *,
    seed: int,
    lineage: int,
    device: torch.device,
    guard: Guard,
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, np.ndarray]:
    width = int(point["width"])
    step = float(point["step"])
    max_time = float(point["max_time"])
    steps = int(round(max_time / step))
    if not math.isclose(steps * step, max_time, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("max_time is not an exact step endpoint")
    method = str(point["integrator"])
    if method not in {"euler", "rk4"}:
        raise ValueError("integrator must be euler or rk4")
    target = float(point["target"])
    if target != 1.0:
        raise ValueError("this frozen child admits only target=1")
    prefix_sizes = tuple(int(value) for value in point["prefix_digest_sizes"])
    if tuple(sorted(set(prefix_sizes))) != prefix_sizes:
        raise ValueError("prefix digest sizes must be strictly increasing")
    if not prefix_sizes or prefix_sizes[-1] > width:
        raise ValueError("prefix digest sizes must be nonempty and within width")
    state, state_sha, prefix_digests = _build_state(
        width,
        seed,
        lineage,
        device,
        int(point.get("rng_row_block", 128)),
        prefix_sizes,
    )
    row_np, col_np, monitor_sha = monitor_coordinates(
        int(point["w_monitor_sample_size"]),
        seed=int(point["w_monitor_seed"]),
        extent=int(point["w_monitor_extent"]),
    )
    if np.max(row_np) >= width or np.max(col_np) >= width:
        raise ValueError("monitor extent exceeds width")
    rows = torch.from_numpy(row_np).to(device=device)
    cols = torch.from_numpy(col_np).to(device=device)

    obs_store = {
        key: torch.empty((steps + 1, 2), dtype=torch.float32, device=device)
        for key in OBS_FIELDS
    }
    state_store = {
        key: torch.empty((steps + 1, 2), dtype=torch.float32, device=device)
        for key in STATE_FIELDS
    }
    update_store = {
        key: torch.empty((steps, 2), dtype=torch.float32, device=device)
        for key in UPDATE_FIELDS
    }

    with torch.no_grad():
        w_norm2 = torch.sum(state.W.square(), dim=(1, 2), dtype=torch.float64)
        checkpoint_steps = [0]
        checkpoint_actual_w_l2 = [
            torch.linalg.vector_norm(state.W.reshape(2, -1), dim=1)
            .detach()
            .cpu()
            .numpy()
            .astype(np.float64)
        ]
        tangent, obs = fused_eval(state, target=target)
        _validate_current(
            state, obs, rows, cols, full_W=True, caps=guard.caps
        )
        _record_obs(obs_store, 0, obs)
        _record_state(state_store, 0, state, w_norm2, rows, cols)
        if progress_callback is not None:
            progress_callback(
                {
                    **guard.snapshot(),
                    "lineage": lineage,
                    "completed_step": 0,
                    "mean_output": float(torch.mean(obs.output).item()),
                    "mean_direct_kernel": float(torch.mean(obs.kernel).item()),
                }
            )
        for index in range(steps):
            guard.before_step()
            if method == "euler":
                a_before = state.a.clone()
                u_before = state.u.clone()
                w_before = state.W[:, rows, cols].clone()
                ideal_a = step * tangent.a
                ideal_u = step * tangent.u
                ideal_w_sample = step * tangent.W[:, rows, cols]
                update_store["a_ideal_update_l2"][index] = torch.linalg.vector_norm(
                    ideal_a, dim=1
                )
                update_store["u_ideal_update_l2"][index] = torch.linalg.vector_norm(
                    ideal_u, dim=1
                )
                update_store["w_ideal_update_l2"][index] = (
                    step * tangent.w_derivative_l2
                )
                update_store["w_sample_ideal_update_l2"][index] = (
                    torch.linalg.vector_norm(ideal_w_sample, dim=1)
                )
                state.a.add_(tangent.a, alpha=step)
                state.W.add_(tangent.W, alpha=step)
                state.u.add_(tangent.u, alpha=step)
                a_applied = state.a - a_before
                u_applied = state.u - u_before
                w_after = state.W[:, rows, cols]
                w_applied = w_after - w_before
                update_store["a_unchanged_fraction"][index] = torch.mean(
                    (state.a == a_before).to(torch.float32), dim=1
                )
                update_store["u_unchanged_fraction"][index] = torch.mean(
                    (state.u == u_before).to(torch.float32), dim=1
                )
                update_store["w_sample_unchanged_fraction"][index] = torch.mean(
                    (w_after == w_before).to(torch.float32), dim=1
                )
                update_store["a_applied_update_l2"][index] = (
                    torch.linalg.vector_norm(a_applied, dim=1)
                )
                update_store["u_applied_update_l2"][index] = (
                    torch.linalg.vector_norm(u_applied, dim=1)
                )
                applied_w_norm = torch.linalg.vector_norm(w_applied, dim=1)
                ideal_w_sample_norm = update_store["w_sample_ideal_update_l2"][index]
                update_store["w_sample_applied_update_l2"][index] = applied_w_norm
                update_store["w_sample_applied_to_ideal_ratio"][index] = (
                    applied_w_norm
                    / torch.clamp(
                        ideal_w_sample_norm, min=torch.finfo(torch.float32).tiny
                    )
                )
                a_ideal_norm = update_store["a_ideal_update_l2"][index]
                u_ideal_norm = update_store["u_ideal_update_l2"][index]
                a_applied_norm = update_store["a_applied_update_l2"][index]
                u_applied_norm = update_store["u_applied_update_l2"][index]
                tiny = torch.finfo(torch.float32).tiny
                update_store["a_applied_to_ideal_ratio"][index] = (
                    a_applied_norm / torch.clamp(a_ideal_norm, min=tiny)
                )
                update_store["u_applied_to_ideal_ratio"][index] = (
                    u_applied_norm / torch.clamp(u_ideal_norm, min=tiny)
                )
                update_store["a_update_cosine"][index] = torch.sum(
                    a_applied * ideal_a, dim=1
                ) / torch.clamp(a_applied_norm * a_ideal_norm, min=tiny)
                update_store["u_update_cosine"][index] = torch.sum(
                    u_applied * ideal_u, dim=1
                ) / torch.clamp(u_applied_norm * u_ideal_norm, min=tiny)
                update_store["w_sample_update_cosine"][index] = torch.sum(
                    w_applied * ideal_w_sample, dim=1
                ) / torch.clamp(
                    applied_w_norm * ideal_w_sample_norm, min=tiny
                )
                w_norm2 = (
                    w_norm2
                    + 2.0
                    * step
                    * tangent.w_state_inner_derivative.to(torch.float64)
                    + step**2 * tangent.w_derivative_l2.to(torch.float64).square()
                )
            else:
                state = rk4_step(state, tangent, step, target=target)
            guard.steps += 1
            tangent, obs = fused_eval(state, target=target)
            _record_obs(obs_store, index + 1, obs)
            if method == "euler":
                _record_state(state_store, index + 1, state, w_norm2, rows, cols)
            checkpoint = (
                index + 1 == steps
                or (index + 1) % int(point["diagnostic_stride"]) == 0
            )
            if checkpoint:
                _validate_current(
                    state,
                    obs,
                    rows,
                    cols,
                    full_W=True,
                    caps=guard.caps,
                )
                checkpoint_steps.append(index + 1)
                checkpoint_actual_w_l2.append(
                    torch.linalg.vector_norm(state.W.reshape(2, -1), dim=1)
                    .detach()
                    .cpu()
                    .numpy()
                    .astype(np.float64)
                )
                if progress_callback is not None:
                    progress_callback(
                        {
                            **guard.snapshot(),
                            "lineage": lineage,
                            "completed_step": index + 1,
                            "mean_output": float(torch.mean(obs.output).item()),
                            "mean_direct_kernel": float(torch.mean(obs.kernel).item()),
                        }
                    )
            wall_sync = (
                index + 1 == steps
                or (index + 1) % int(point["wall_sync_stride"]) == 0
            )
            if device.type == "cuda" and wall_sync:
                torch.cuda.synchronize(device)
            guard.after_step()

    result = {
        f"raw_{key}": value.detach().cpu().numpy().astype(np.float64)
        for key, value in obs_store.items()
    }
    if method == "euler":
        result.update(
            {
                f"state_{key}": value.detach().cpu().numpy().astype(np.float64)
                for key, value in state_store.items()
            }
        )
        result.update(
            {
                f"update_{key}": value.detach().cpu().numpy().astype(np.float64)
                for key, value in update_store.items()
            }
        )
    result["initial_state_sha256"] = np.asarray(state_sha, dtype="S64")
    result["prefix_digest_sizes"] = np.asarray(prefix_sizes, dtype=np.int64)
    result["initial_prefix_sha256"] = np.asarray(
        [prefix_digests[size] for size in prefix_sizes], dtype="S64"
    )
    result["w_monitor_sha256"] = np.asarray(monitor_sha, dtype="S64")
    result["w_monitor_rows"] = row_np
    result["w_monitor_cols"] = col_np
    result["w_norm_checkpoint_steps"] = np.asarray(
        checkpoint_steps, dtype=np.int64
    )
    expected_checkpoints = np.asarray(
        point["expected_full_w_checkpoint_steps"], dtype=np.int64
    )
    if not np.array_equal(result["w_norm_checkpoint_steps"], expected_checkpoints):
        raise NumericalInvalid("full-W checkpoint schedule differs from declaration")
    result["w_actual_l2_at_checkpoints"] = np.stack(
        checkpoint_actual_w_l2, axis=0
    )
    del state, tangent, obs, obs_store, state_store, update_store
    gc.collect()
    if device.type == "cuda":
        torch.cuda.empty_cache()
    return result


def _normalized_progress_kernel(
    time_output: np.ndarray, time_kernel: np.ndarray, nodes: np.ndarray
) -> np.ndarray:
    result = np.empty((len(nodes), time_output.shape[1]), dtype=np.float64)
    for column in range(time_output.shape[1]):
        f = time_output[:, column]
        f0 = f[0]
        progress = (f - f0) / (1.0 - f0)
        if np.min(np.diff(progress)) < -1e-6 or progress[-1] < nodes[-1]:
            raise NumericalInvalid("trajectory fails normalized-progress hitting gate")
        keep = np.concatenate(([True], np.diff(progress) > 0.0))
        result[:, column] = np.interp(
            nodes, progress[keep], time_kernel[keep, column]
        )
    return result


def _common_clock_summary(arrays: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    nodes = arrays["output_nodes"]
    time = arrays["raw_time"]
    mean_output = arrays["raw_output"].mean(axis=1)
    if np.min(np.diff(mean_output)) < -1e-6:
        raise NumericalInvalid("mean output is nonmonotone")
    keep = np.concatenate(([True], np.diff(mean_output) > 0.0))
    x = mean_output[keep]
    if nodes[-1] > x[-1]:
        raise NumericalInvalid("mean output does not hit final node")
    node_time = np.interp(nodes, x, time[keep])

    def mean_at(key: str) -> np.ndarray:
        mean_curve = arrays[key].mean(axis=1)
        return np.interp(node_time, time, mean_curve)

    numerator = mean_at("raw_weighted_kernel")
    denominator = 1.0 - nodes
    return {
        "node_physical_time": node_time,
        "node_effective_kernel": numerator / denominator,
        "node_mean_direct_kernel": mean_at("raw_kernel"),
        "node_mean_kernel_a": mean_at("raw_kernel_a"),
        "node_mean_kernel_W": mean_at("raw_kernel_W"),
        "node_mean_kernel_u": mean_at("raw_kernel_u"),
        "node_mean_physical_loss": mean_at("raw_loss"),
        "node_loss_of_mean_output": np.square(denominator),
    }


def run_point(
    point: dict[str, Any],
    *,
    seed: int,
    device: torch.device,
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    if str(point["dtype"]) != "float32":
        raise ValueError("this child admits only float32")
    if float(point["target"]) != 1.0:
        raise ValueError("this frozen child admits only target=1")
    start = int(point["lineage_start"])
    stop = int(point["lineage_stop"])
    if stop <= start:
        raise ValueError("empty lineage range")
    guard = Guard(point["caps"], device)
    pieces = []
    try:
        for lineage in range(start, stop):
            pieces.append(
                simulate_lineage(
                    point,
                    seed=seed,
                    lineage=lineage,
                    device=device,
                    guard=guard,
                    progress_callback=progress_callback,
                )
            )
    except Exception as exc:
        if not hasattr(exc, "point_diagnostics"):
            exc.point_diagnostics = guard.snapshot()
        raise
    steps = int(round(float(point["max_time"]) / float(point["step"])))
    arrays: dict[str, np.ndarray] = {
        "raw_time": np.arange(steps + 1, dtype=np.float64) * float(point["step"]),
        "update_time": np.arange(steps, dtype=np.float64) * float(point["step"]),
        "lineage_ids": np.arange(start, stop, dtype=np.int64),
        "initial_state_sha256": np.asarray(
            [piece["initial_state_sha256"] for piece in pieces], dtype="S64"
        ).reshape(-1),
        "prefix_digest_sizes": pieces[0]["prefix_digest_sizes"],
        "initial_prefix_sha256": np.stack(
            [piece["initial_prefix_sha256"] for piece in pieces], axis=0
        ),
        "w_monitor_sha256": pieces[0]["w_monitor_sha256"],
        "w_monitor_rows": pieces[0]["w_monitor_rows"],
        "w_monitor_cols": pieces[0]["w_monitor_cols"],
        "output_nodes": np.asarray(point["output_nodes"], dtype=np.float64),
    }
    if not all(
        bool(piece["w_monitor_sha256"] == pieces[0]["w_monitor_sha256"])
        for piece in pieces
    ):
        raise NumericalInvalid("W monitor coordinate hashes differ by lineage")
    for key in pieces[0]:
        if key.startswith("raw_") or key.startswith("state_") or key.startswith("update_"):
            arrays[key] = np.concatenate([piece[key] for piece in pieces], axis=1)
    if not all(
        np.array_equal(piece["w_norm_checkpoint_steps"], pieces[0]["w_norm_checkpoint_steps"])
        for piece in pieces
    ):
        raise NumericalInvalid("full-W checkpoint schedules differ by lineage")
    arrays["w_norm_checkpoint_steps"] = pieces[0]["w_norm_checkpoint_steps"]
    arrays["w_actual_l2_at_checkpoints"] = np.concatenate(
        [piece["w_actual_l2_at_checkpoints"] for piece in pieces], axis=1
    )
    positive_nodes = arrays["output_nodes"][arrays["output_nodes"] > 0.0]
    arrays["normalized_progress_nodes"] = positive_nodes
    arrays["normalized_progress_kernel"] = _normalized_progress_kernel(
        arrays["raw_output"], arrays["raw_kernel"], positive_nodes
    )
    arrays.update(_common_clock_summary(arrays))
    mean_output = arrays["raw_output"].mean(axis=1)
    mean_loss = arrays["raw_loss"].mean(axis=1)
    diagnostics: dict[str, Any] = guard.snapshot()
    initial_output = arrays["raw_output"][0].reshape(-1, 2)
    initial_components = {
        key: arrays[key][0].reshape(-1, 2)
        for key in ("raw_kernel_a", "raw_kernel_W", "raw_kernel_u")
    }
    ulp_multiplier = float(point["initial_symmetry_ulp_multiplier"])
    eps32 = float(torch.finfo(torch.float32).eps)
    output_scale = np.maximum(np.max(np.abs(initial_output), axis=1), 1.0)
    output_scaled_defect = np.abs(initial_output.sum(axis=1)) / (
        ulp_multiplier * eps32 * output_scale
    )
    component_scaled_defect = []
    for values in initial_components.values():
        scale = np.maximum(np.max(np.abs(values), axis=1), 1.0)
        component_scaled_defect.append(
            np.abs(values[:, 0] - values[:, 1])
            / (ulp_multiplier * eps32 * scale)
        )
    component_scaled_defect = np.concatenate(component_scaled_defect)
    diagnostics.update(
        {
            "target": 1.0,
            "initial_mean_output": float(mean_output[0]),
            "initial_antithetic_output_scaled_ulp_defect": float(
                np.max(output_scaled_defect)
            ),
            "initial_antithetic_component_scaled_ulp_defect": float(
                np.max(component_scaled_defect)
            ),
            "terminal_mean_output": float(mean_output[-1]),
            "minimum_mean_output_increment": float(np.min(np.diff(mean_output))),
            "maximum_mean_loss_increment": float(np.max(np.diff(mean_loss))),
            "maximum_loss_jensen_gap": float(
                np.max(mean_loss - np.square(1.0 - mean_output))
            ),
            "lineage_count": stop - start,
            "trajectory_count": 2 * (stop - start),
        }
    )
    if abs(diagnostics["initial_mean_output"]) > float(
        point["initial_mean_output_tolerance"]
    ):
        raise NumericalInvalid("initial antithetic mean-output gate failed")
    if diagnostics["initial_antithetic_output_scaled_ulp_defect"] > 1.0:
        raise NumericalInvalid("initial antithetic output-cancellation gate failed")
    if diagnostics["initial_antithetic_component_scaled_ulp_defect"] > 1.0:
        raise NumericalInvalid("initial antithetic component-equality gate failed")
    if diagnostics["minimum_mean_output_increment"] < -float(
        point["monotonic_tolerance"]
    ):
        raise NumericalInvalid("mean output monotonicity gate failed")
    if diagnostics["maximum_mean_loss_increment"] > float(
        point["loss_nonincrease_tolerance"]
    ):
        raise NumericalInvalid("mean physical loss gate failed")
    step = float(point["step"])
    driver_lhs = np.diff(mean_output) / (2.0 * step)
    driver_rhs = arrays["raw_weighted_kernel"][:-1].mean(axis=1)
    driver_defect = driver_lhs - driver_rhs
    through = mean_output[:-1] <= 0.9
    scale = np.maximum(np.abs(driver_rhs[through]), 1e-12)
    diagnostics.update(
        {
            "driver_max_relative_defect_through_y_0_9": float(
                np.max(np.abs(driver_defect[through]) / scale)
            ),
            "driver_relative_rms_defect_through_y_0_9": float(
                np.sqrt(np.mean(driver_defect[through] ** 2))
                / max(np.sqrt(np.mean(driver_rhs[through] ** 2)), 1e-12)
            ),
            "driver_cumulative_relative_defect_through_y_0_9": float(
                abs(np.sum(2.0 * step * driver_defect[through]))
                / max(
                    abs(np.sum(2.0 * step * driver_rhs[through])), 1e-12
                )
            ),
        }
    )
    if str(point["integrator"]) == "euler":
        inferential_steps = mean_output[:-1] <= 0.9
        if not np.any(inferential_steps):
            raise NumericalInvalid("empty update-audit window through y=0.9")

        def window(key: str) -> np.ndarray:
            return arrays[key][inferential_steps]

        checkpoint_steps = arrays["w_norm_checkpoint_steps"]
        checkpoint_through = mean_output[checkpoint_steps] <= 0.9
        actual_w = arrays["w_actual_l2_at_checkpoints"][checkpoint_through]
        ideal_w = arrays["state_w_ideal_recurrence_l2"][checkpoint_steps][
            checkpoint_through
        ]
        w_recurrence_relative = np.abs(ideal_w - actual_w) / np.maximum(
            np.abs(actual_w), 1e-12
        )
        diagnostics.update(
            {
                "maximum_a_unchanged_fraction_through_y_0_9": float(
                    np.max(window("update_a_unchanged_fraction"))
                ),
                "maximum_u_unchanged_fraction_through_y_0_9": float(
                    np.max(window("update_u_unchanged_fraction"))
                ),
                "maximum_w_sample_unchanged_fraction_through_y_0_9": float(
                    np.max(window("update_w_sample_unchanged_fraction"))
                ),
                "median_w_sample_unchanged_fraction_through_y_0_9": float(
                    np.median(window("update_w_sample_unchanged_fraction"))
                ),
                "minimum_w_sample_applied_to_ideal_ratio_through_y_0_9": float(
                    np.min(window("update_w_sample_applied_to_ideal_ratio"))
                ),
                "maximum_w_sample_applied_to_ideal_ratio_through_y_0_9": float(
                    np.max(window("update_w_sample_applied_to_ideal_ratio"))
                ),
                "minimum_a_applied_to_ideal_ratio_through_y_0_9": float(
                    np.min(window("update_a_applied_to_ideal_ratio"))
                ),
                "maximum_a_applied_to_ideal_ratio_through_y_0_9": float(
                    np.max(window("update_a_applied_to_ideal_ratio"))
                ),
                "minimum_u_applied_to_ideal_ratio_through_y_0_9": float(
                    np.min(window("update_u_applied_to_ideal_ratio"))
                ),
                "maximum_u_applied_to_ideal_ratio_through_y_0_9": float(
                    np.max(window("update_u_applied_to_ideal_ratio"))
                ),
                "minimum_a_update_cosine_through_y_0_9": float(
                    np.min(window("update_a_update_cosine"))
                ),
                "minimum_u_update_cosine_through_y_0_9": float(
                    np.min(window("update_u_update_cosine"))
                ),
                "minimum_w_sample_update_cosine_through_y_0_9": float(
                    np.min(window("update_w_sample_update_cosine"))
                ),
                "maximum_w_ideal_recurrence_relative_error_through_y_0_9": float(
                    np.max(w_recurrence_relative)
                ),
                "maximum_a_unchanged_fraction_all_time": float(
                    np.max(arrays["update_a_unchanged_fraction"])
                ),
                "maximum_u_unchanged_fraction_all_time": float(
                    np.max(arrays["update_u_unchanged_fraction"])
                ),
                "maximum_w_sample_unchanged_fraction_all_time": float(
                    np.max(arrays["update_w_sample_unchanged_fraction"])
                ),
            }
        )
    return arrays, diagnostics
