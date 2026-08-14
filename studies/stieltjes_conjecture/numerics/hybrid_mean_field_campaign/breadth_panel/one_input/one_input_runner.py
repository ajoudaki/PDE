#!/usr/bin/env python3
"""Bounded FP32 Euler runner for one-input breadth-panel points.

The runner is intentionally small: it executes one antithetic lineage at a
time, retains the raw observable curves needed for common-output-clock
analysis, and records aggregate update-rounding diagnostics.  It does not
classify Stieltjes compatibility and it does not launch itself.
"""

from __future__ import annotations

import gc
import math
import resource
import time
from dataclasses import dataclass
from typing import Any

import numpy as np
import torch

import one_input_engine as model


OBSERVABLE_FIELDS = (
    "output",
    "kernel",
    "kernel_a",
    "kernel_W",
    "kernel_u",
    "weighted_kernel",
    "loss",
    "q1",
    "q2",
)

UPDATE_FIELDS = (
    "a_unchanged_fraction",
    "u_unchanged_fraction",
    "w_unchanged_fraction",
    "a_ratio",
    "u_ratio",
    "w_ratio",
    "a_cosine",
    "u_cosine",
    "w_cosine",
)


class BudgetStop(RuntimeError):
    pass


class NumericalInvalid(RuntimeError):
    pass


@dataclass
class Guard:
    caps: dict[str, Any]
    device: torch.device

    def __post_init__(self) -> None:
        self.started = time.monotonic()
        self.steps = 0
        self.max_gpu_gib = 0.0
        self.max_host_gib = 0.0
        if self.device.type == "cuda":
            torch.cuda.synchronize(self.device)
            torch.cuda.reset_peak_memory_stats(self.device)

    def snapshot(self) -> dict[str, float | int]:
        self.max_host_gib = max(
            self.max_host_gib,
            float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20,
        )
        if self.device.type == "cuda":
            self.max_gpu_gib = max(
                self.max_gpu_gib,
                float(torch.cuda.max_memory_allocated(self.device)) / 2**30,
            )
        return {
            "elapsed_seconds": time.monotonic() - self.started,
            "steps": self.steps,
            "max_gpu_allocated_gib": self.max_gpu_gib,
            "max_host_rss_gib": self.max_host_gib,
        }

    def check(self, *, before_step: bool) -> None:
        status = self.snapshot()
        if status["elapsed_seconds"] >= float(self.caps["wall_seconds"]):
            raise BudgetStop("wall cap reached")
        exhausted = (
            self.steps >= int(self.caps["max_steps_all_lineages"])
            if before_step
            else self.steps > int(self.caps["max_steps_all_lineages"])
        )
        if exhausted:
            raise BudgetStop("step cap reached")
        if self.max_host_gib > float(self.caps["host_rss_gib"]):
            raise BudgetStop("host RSS cap reached")
        if self.device.type == "cuda" and self.max_gpu_gib > float(
            self.caps["gpu_memory_gib"]
        ):
            raise BudgetStop("GPU allocation cap reached")


def configuration_by_key(key: str) -> model.Configuration:
    matches = {configuration.key: configuration for configuration in model.CONFIGURATIONS}
    try:
        return matches[key]
    except KeyError as exc:
        raise ValueError(f"unknown one-input configuration {key!r}") from exc


def validate_point(point: dict[str, Any]) -> None:
    required = {
        "key",
        "purpose",
        "configuration",
        "width",
        "step",
        "max_time",
        "lineage_start",
        "lineage_stop",
        "prefix_sizes",
        "rng_row_block",
        "w_monitor_size",
        "w_monitor_extent",
        "w_monitor_seed",
        "diagnostic_stride",
        "wall_sync_stride",
        "caps",
    }
    if set(point) != required:
        raise ValueError(
            f"point fields differ: missing={sorted(required-set(point))}, "
            f"extra={sorted(set(point)-required)}"
        )
    configuration_by_key(str(point["configuration"]))
    purpose = str(point["purpose"])
    if purpose not in {"validation_coarse", "validation_fine", "width_screen", "unit_test"}:
        raise ValueError("unknown point purpose")
    integer_fields = (
        "width",
        "lineage_start",
        "lineage_stop",
        "rng_row_block",
        "w_monitor_size",
        "w_monitor_extent",
        "w_monitor_seed",
        "diagnostic_stride",
        "wall_sync_stride",
    )
    if any(
        not isinstance(point[field], int) or isinstance(point[field], bool)
        for field in integer_fields
    ):
        raise ValueError("integer point fields must be JSON integers")
    if any(not isinstance(value, int) or isinstance(value, bool) for value in point["prefix_sizes"]):
        raise ValueError("prefix sizes must be JSON integers")
    width = int(point["width"])
    if width <= 0 or (purpose == "unit_test" and width > 64):
        raise ValueError("invalid width")
    if purpose != "unit_test" and width not in {2048, 4096, 8192}:
        raise ValueError("scientific width is outside the frozen ladder")
    step = float(point["step"])
    if step not in {1e-5, 2e-5}:
        raise ValueError("step is outside the audited pair")
    if purpose == "validation_coarse" and step != 2e-5:
        raise ValueError("coarse validation requires h=2e-5")
    if purpose in {"validation_fine", "width_screen"} and step != 1e-5:
        raise ValueError("fine/screen point requires h=1e-5")
    steps = int(round(float(point["max_time"]) / step))
    if steps <= 0 or not math.isclose(
        steps * step, float(point["max_time"]), rel_tol=0.0, abs_tol=1e-12
    ):
        raise ValueError("max_time is not an exact positive step endpoint")
    start, stop = int(point["lineage_start"]), int(point["lineage_stop"])
    if start < 0 or stop <= start:
        raise ValueError("invalid lineage interval")
    prefixes = tuple(int(value) for value in point["prefix_sizes"])
    if not prefixes or tuple(sorted(set(prefixes))) != prefixes or prefixes[-1] != width:
        raise ValueError("prefix sizes must be sorted, unique, and end at width")
    expected_extent = width if width < 2048 else 2048
    if int(point["w_monitor_extent"]) != expected_extent:
        raise ValueError("W monitor extent differs from frozen common extent")
    if int(point["w_monitor_size"]) <= 0:
        raise ValueError("W monitor size must be positive")
    if int(point["rng_row_block"]) <= 0:
        raise ValueError("RNG row block must be positive")
    if int(point["diagnostic_stride"]) <= 0 or int(point["wall_sync_stride"]) <= 0:
        raise ValueError("diagnostic strides must be positive")
    caps = point["caps"]
    required_caps = {
        "wall_seconds",
        "max_steps_all_lineages",
        "gpu_memory_gib",
        "host_rss_gib",
        "kernel_ceiling",
        "state_ceiling",
    }
    if set(caps) != required_caps:
        raise ValueError("cap fields differ from the frozen schema")
    if int(caps["max_steps_all_lineages"]) != steps * (stop - start):
        raise ValueError("step cap does not equal the exact declared work")
    if any(float(caps[key]) <= 0.0 for key in required_caps):
        raise ValueError("caps must be positive")


def _monitor_coordinates(size: int, seed: int, extent: int) -> tuple[np.ndarray, np.ndarray, str]:
    rows, cols, digest = model.audited_init.monitor_coordinates(
        size, seed=seed, extent=extent
    )
    return rows, cols, digest


def _validate(
    state: model.State,
    observables: model.Observables,
    rows: torch.Tensor,
    cols: torch.Tensor,
    caps: dict[str, Any],
    *,
    full: bool,
) -> None:
    tensors = [
        state.a,
        state.u,
        state.W[:, rows, cols],
        *(getattr(observables, field) for field in OBSERVABLE_FIELDS),
    ]
    if full:
        tensors.append(state.W)
    if not all(bool(torch.all(torch.isfinite(value)).item()) for value in tensors):
        raise NumericalInvalid("nonfinite state or observable")
    if any(
        bool(torch.any(getattr(observables, name) <= 0.0).item())
        for name in ("kernel", "kernel_a", "kernel_W", "kernel_u", "q1", "q2")
    ):
        raise NumericalInvalid("nonpositive kernel component or squared norm")
    if float(torch.amax(observables.kernel).item()) >= float(caps["kernel_ceiling"]):
        raise NumericalInvalid("kernel ceiling reached")
    sampled_max = max(
        float(torch.amax(torch.abs(state.a)).item()),
        float(torch.amax(torch.abs(state.u)).item()),
        float(torch.amax(torch.abs(state.W[:, rows, cols])).item()),
    )
    if sampled_max >= float(caps["state_ceiling"]):
        raise NumericalInvalid("sampled state ceiling reached")
    if full and float(torch.amax(torch.abs(state.W)).item()) >= float(
        caps["state_ceiling"]
    ):
        raise NumericalInvalid("full W state ceiling reached")


def _ratio_and_cosine(
    applied: torch.Tensor, ideal: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    applied_flat = applied.reshape(applied.shape[0], -1)
    ideal_flat = ideal.reshape(ideal.shape[0], -1)
    applied_norm = torch.linalg.vector_norm(applied_flat, dim=1)
    ideal_norm = torch.linalg.vector_norm(ideal_flat, dim=1)
    tiny = torch.finfo(torch.float32).tiny
    ratio = applied_norm / torch.clamp(ideal_norm, min=tiny)
    cosine = torch.sum(applied_flat * ideal_flat, dim=1) / torch.clamp(
        applied_norm * ideal_norm, min=tiny
    )
    return ratio, cosine


def simulate_lineage(
    point: dict[str, Any],
    *,
    seed: int,
    lineage: int,
    device: torch.device,
    guard: Guard,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    configuration = configuration_by_key(str(point["configuration"]))
    width = int(point["width"])
    step = float(point["step"])
    max_time = float(point["max_time"])
    steps = int(round(max_time / step))
    if not math.isclose(steps * step, max_time, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("max_time must be an exact step endpoint")
    prefix_sizes = tuple(int(value) for value in point["prefix_sizes"])
    state, initialization = model.build_antithetic_state(
        configuration,
        width,
        seed=seed,
        lineage=lineage,
        device=device,
        row_block=int(point.get("rng_row_block", 128)),
        prefix_sizes=prefix_sizes,
    )
    row_np, col_np, monitor_digest = _monitor_coordinates(
        int(point["w_monitor_size"]),
        int(point["w_monitor_seed"]),
        int(point["w_monitor_extent"]),
    )
    if int(point["w_monitor_extent"]) > width:
        raise ValueError("W monitor extent exceeds width")
    rows = torch.from_numpy(row_np).to(device=device)
    cols = torch.from_numpy(col_np).to(device=device)
    observables_store = {
        field: torch.empty((steps + 1, 2), dtype=torch.float32, device=device)
        for field in OBSERVABLE_FIELDS
    }
    updates_store = {
        field: torch.empty((steps, 2), dtype=torch.float32, device=device)
        for field in UPDATE_FIELDS
    }
    diagnostic_stride = int(point["diagnostic_stride"])
    wall_sync_stride = int(point["wall_sync_stride"])
    checkpoint_steps: list[int] = []
    w_recurrence_errors: list[np.ndarray] = []

    with torch.no_grad():
        w_norm2 = torch.sum(state.W.square(), dim=(1, 2), dtype=torch.float64)
        tangent, observables = model.fused_eval(state, configuration)
        _validate(state, observables, rows, cols, guard.caps, full=True)
        for field in OBSERVABLE_FIELDS:
            observables_store[field][0] = getattr(observables, field)
        for index in range(steps):
            if device.type == "cuda" and index % wall_sync_stride == 0:
                torch.cuda.synchronize(device)
            guard.check(before_step=True)
            before_a = state.a.clone()
            before_u = state.u.clone()
            before_w = state.W[:, rows, cols].clone()
            ideal_a = step * tangent.a
            ideal_u = step * tangent.u
            ideal_w = step * tangent.W[:, rows, cols]

            state.a.add_(tangent.a, alpha=step)
            state.W.add_(tangent.W, alpha=step)
            state.u.add_(tangent.u, alpha=step)
            applied_a = state.a - before_a
            applied_u = state.u - before_u
            applied_w = state.W[:, rows, cols] - before_w
            updates_store["a_unchanged_fraction"][index] = torch.mean(
                (state.a == before_a).to(torch.float32), dim=1
            )
            updates_store["u_unchanged_fraction"][index] = torch.mean(
                (state.u == before_u).to(torch.float32), dim=1
            )
            updates_store["w_unchanged_fraction"][index] = torch.mean(
                (state.W[:, rows, cols] == before_w).to(torch.float32), dim=1
            )
            for prefix, applied, ideal in (
                ("a", applied_a, ideal_a),
                ("u", applied_u, ideal_u),
                ("w", applied_w, ideal_w),
            ):
                ratio, cosine = _ratio_and_cosine(applied, ideal)
                updates_store[f"{prefix}_ratio"][index] = ratio
                updates_store[f"{prefix}_cosine"][index] = cosine
            w_norm2 = (
                w_norm2
                + 2.0
                * step
                * tangent.w_state_inner_derivative.to(torch.float64)
                + step**2 * tangent.w_derivative_l2.to(torch.float64).square()
            )
            guard.steps += 1
            tangent, observables = model.fused_eval(state, configuration)
            for field in OBSERVABLE_FIELDS:
                observables_store[field][index + 1] = getattr(observables, field)
            checkpoint = index + 1 == steps or (index + 1) % diagnostic_stride == 0
            if checkpoint:
                _validate(state, observables, rows, cols, guard.caps, full=True)
                actual = torch.sum(
                    state.W.square(), dim=(1, 2), dtype=torch.float64
                )
                error = torch.abs(actual - w_norm2) / torch.clamp(
                    torch.abs(actual), min=1e-24
                )
                checkpoint_steps.append(index + 1)
                w_recurrence_errors.append(error.cpu().numpy())
            if device.type == "cuda" and (index + 1) % wall_sync_stride == 0:
                torch.cuda.synchronize(device)
            guard.check(before_step=False)

    arrays = {
        "time": np.arange(steps + 1, dtype=np.float64) * step,
        **{
            f"raw_{field}": value.cpu().numpy().astype(np.float64)
            for field, value in observables_store.items()
        },
        **{
            f"update_{field}": value.cpu().numpy().astype(np.float64)
            for field, value in updates_store.items()
        },
        "checkpoint_steps": np.asarray(checkpoint_steps, dtype=np.int64),
        "w_recurrence_relative_error": np.stack(w_recurrence_errors, axis=0),
        "w_monitor_rows": row_np,
        "w_monitor_cols": col_np,
    }
    proxy = model.to_proxy_coordinates(observables=model.Observables(**{
        field: torch.from_numpy(arrays[f"raw_{field}"])
        for field in OBSERVABLE_FIELDS
    }), configuration=configuration)
    for field in OBSERVABLE_FIELDS:
        arrays[f"proxy_{field}"] = getattr(proxy, field).numpy().astype(np.float64)

    mean_output = arrays["raw_output"].mean(axis=1)
    mean_loss = arrays["raw_loss"].mean(axis=1)
    through = mean_output[:-1] <= 0.95
    lhs = np.diff(mean_output) / (2.0 * step)
    rhs = arrays["raw_weighted_kernel"][:-1].mean(axis=1)
    defect = lhs - rhs
    scale = np.maximum(np.abs(rhs[through]), 1e-12)
    diagnostics = {
        **guard.snapshot(),
        "configuration": configuration.key,
        "width": width,
        "step": step,
        "lineage": lineage,
        "terminal_mean_output": float(mean_output[-1]),
        "minimum_mean_output_increment": float(np.min(np.diff(mean_output))),
        "maximum_mean_loss_increment": float(np.max(np.diff(mean_loss))),
        "driver_max_relative_defect_through_y_0_95": float(
            np.max(np.abs(defect[through]) / scale)
        ),
        "driver_rms_relative_defect_through_y_0_95": float(
            np.sqrt(np.mean(defect[through] ** 2))
            / max(np.sqrt(np.mean(rhs[through] ** 2)), 1e-12)
        ),
        "driver_cumulative_relative_defect_through_y_0_95": float(
            abs(np.sum(2.0 * step * defect[through]))
            / max(abs(np.sum(2.0 * step * rhs[through])), 1e-12)
        ),
        "maximum_w_recurrence_relative_error": float(
            np.max(arrays["w_recurrence_relative_error"])
        ),
        "initialization": initialization,
        "monitor_sha256": monitor_digest,
        "finite_width_initial_means": model.initial_finite_width_means(
            configuration, width
        ),
    }
    update_mask = through[:, None]
    for field in ("a_unchanged_fraction", "u_unchanged_fraction", "w_unchanged_fraction"):
        diagnostics[f"maximum_{field}_through_y_0_95"] = float(
            np.max(np.where(update_mask, arrays[f"update_{field}"], -np.inf))
        )
    for field in ("a_ratio", "u_ratio", "w_ratio", "a_cosine", "u_cosine", "w_cosine"):
        values = np.where(update_mask, arrays[f"update_{field}"], np.nan)
        diagnostics[f"minimum_{field}_through_y_0_95"] = float(np.nanmin(values))
        if field.endswith("ratio"):
            diagnostics[f"maximum_{field}_through_y_0_95"] = float(np.nanmax(values))
    del state, tangent, observables, observables_store, updates_store
    gc.collect()
    if device.type == "cuda":
        torch.cuda.empty_cache()
    return arrays, diagnostics


def run_point(
    point: dict[str, Any], *, seed: int, device: torch.device
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    validate_point(point)
    start = int(point["lineage_start"])
    stop = int(point["lineage_stop"])
    if stop <= start:
        raise ValueError("empty lineage interval")
    guard = Guard(point["caps"], device)
    pieces: list[dict[str, np.ndarray]] = []
    lineage_diagnostics: list[dict[str, Any]] = []
    for lineage in range(start, stop):
        if device.type == "cuda":
            torch.cuda.synchronize(device)
        guard.check(before_step=False)
        arrays, diagnostics = simulate_lineage(
            point,
            seed=seed,
            lineage=lineage,
            device=device,
            guard=guard,
        )
        pieces.append(arrays)
        lineage_diagnostics.append(diagnostics)
        if device.type == "cuda":
            torch.cuda.synchronize(device)
        guard.check(before_step=False)
    combined: dict[str, np.ndarray] = {
        "time": pieces[0]["time"],
        "lineage_ids": np.arange(start, stop, dtype=np.int64),
        "column_lineage_id": np.repeat(
            np.arange(start, stop, dtype=np.int64), 2
        ),
        "antithetic_sign": np.tile(np.asarray((1, -1), dtype=np.int8), stop - start),
        "array_schema_version": np.asarray(
            b"breadth-one-input-arrays-v1", dtype="S32"
        ),
    }
    for key in pieces[0]:
        if key == "time":
            continue
        if key in {"w_monitor_rows", "w_monitor_cols", "checkpoint_steps"}:
            if not all(np.array_equal(piece[key], pieces[0][key]) for piece in pieces):
                raise NumericalInvalid(f"shared array {key} differs by lineage")
            combined[key] = pieces[0][key]
        else:
            axis = 1 if pieces[0][key].ndim >= 2 else 0
            combined[key] = np.concatenate([piece[key] for piece in pieces], axis=axis)
    if device.type == "cuda":
        torch.cuda.synchronize(device)
    guard.check(before_step=False)
    return combined, {
        **guard.snapshot(),
        "lineage_start": start,
        "lineage_stop": stop,
        "lineages": lineage_diagnostics,
    }
