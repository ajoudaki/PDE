"""Trace generation for exact and projected long-horizon dynamics."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable

import numpy as np

from .core import (
    FieldState,
    ModelSpec,
    field_vector_field,
    fields_from_params,
    initialize,
    normalized_error,
    rk4_field_step,
    rk4_param_step,
    rms_error,
    snapshot_from_field,
    snapshot_from_params,
)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def config_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _require_integer_ratio(numerator: float, denominator: float, name: str) -> int:
    ratio = numerator / denominator
    rounded = int(round(ratio))
    if not np.isclose(ratio, rounded, rtol=0.0, atol=1e-10):
        raise ValueError(f"{name} must be an integer multiple of dt")
    return rounded


def _model_spec(run: dict[str, Any]) -> ModelSpec:
    X = np.asarray(run["X"], dtype=float)
    y = np.asarray(run["y"], dtype=float)
    return ModelSpec(
        n=int(run["n"]),
        depth=int(run["depth"]),
        X=X,
        y=y,
        seed=int(run["seed"]),
        sigma_w=float(run["sigma_w"]),
        A=float(run["A"]),
        gamma=float(run["gamma"]),
    )


def run_trace(
    run: dict[str, Any],
    output_path: Path,
    progress: Callable[[str], None] | None = None,
) -> dict[str, Any]:
    """Run one exact/response comparison and write a non-pickle NPZ trace."""

    spec = _model_spec(run)
    dt = float(run["dt"])
    duration = float(run["duration"])
    restart_time = float(run.get("restart_time", 0.0))
    sample_dt = float(run["sample_dt"])
    requested_orders = sorted({int(x) for x in run["orders"]})
    orders = requested_orders.copy()
    if run.get("control_order", False) and spec.depth not in orders:
        orders.append(spec.depth)
    if dt <= 0 or duration <= 0 or restart_time < 0:
        raise ValueError("dt and duration must be positive; restart_time nonnegative")
    steps = _require_integer_ratio(duration, dt, "duration")
    restart_steps = _require_integer_ratio(restart_time, dt, "restart_time")
    sample_every = _require_integer_ratio(sample_dt, dt, "sample_dt")

    exact = initialize(spec)
    for _ in range(restart_steps):
        exact = rk4_param_step(exact, dt, spec)
    projected: dict[int, FieldState] = {
        order: fields_from_params(exact, spec) for order in orders
    }

    labels = ["exact", *[f"K{order}" for order in orders]]
    snapshots: dict[str, list[Any]] = {
        key: []
        for key in (
            "f",
            "loss",
            "grams",
            "f_dot",
            "loss_dot",
            "gram_dot",
            "theta",
            "theta_min",
            "kernel_identity_defect",
            "residual_norm",
            "output_speed",
            "gram_speed",
            "forward_defect",
            "adjoint_defect",
            "terminal_defect",
        )
    }
    times: list[float] = []
    inst_h_rel: list[list[float]] = []
    inst_p_rel: list[list[float]] = []
    inst_h_rms: list[list[float]] = []
    inst_p_rms: list[list[float]] = []

    def record(step: int) -> None:
        exact_snapshot, exact_hdot, exact_pdot = snapshot_from_params(
            exact, spec
        )
        method_snaps = [exact_snapshot]
        base = fields_from_params(exact, spec)
        h_rel_row: list[float] = []
        p_rel_row: list[float] = []
        h_rms_row: list[float] = []
        p_rms_row: list[float] = []
        for order in orders:
            projected_deriv_at_exact = field_vector_field(base, spec, order)
            h_rel_row.append(
                normalized_error(projected_deriv_at_exact.H, exact_hdot)
            )
            p_rel_row.append(
                normalized_error(projected_deriv_at_exact.P, exact_pdot)
            )
            h_rms_row.append(
                rms_error(projected_deriv_at_exact.H, exact_hdot)
            )
            p_rms_row.append(
                rms_error(projected_deriv_at_exact.P, exact_pdot)
            )
            deriv = field_vector_field(projected[order], spec, order)
            method_snaps.append(
                snapshot_from_field(projected[order], deriv, spec)
            )

        times.append(restart_time + step * dt)
        inst_h_rel.append(h_rel_row)
        inst_p_rel.append(p_rel_row)
        inst_h_rms.append(h_rms_row)
        inst_p_rms.append(p_rms_row)
        for key in snapshots:
            snapshots[key].append(
                [getattr(snapshot, key) for snapshot in method_snaps]
            )

    for step in range(steps + 1):
        if step % sample_every == 0 or step == steps:
            record(step)
        if step == steps:
            break
        exact = rk4_param_step(exact, dt, spec)
        for order in orders:
            projected[order] = rk4_field_step(
                projected[order], dt, spec, order
            )
        if progress and (
            step == 0
            or (step + 1) % max(1, steps // 4) == 0
            or step + 1 == steps
        ):
            progress(
                f"{run['id']}: {100.0 * (step + 1) / steps:5.1f}%"
            )

    arrays = {
        "times": np.asarray(times, dtype=float),
        "method_labels": np.asarray(labels, dtype="U32"),
        "orders": np.asarray(orders, dtype=int),
        "inst_h_rel": np.asarray(inst_h_rel, dtype=float).T,
        "inst_p_rel": np.asarray(inst_p_rel, dtype=float).T,
        "inst_h_rms": np.asarray(inst_h_rms, dtype=float).T,
        "inst_p_rms": np.asarray(inst_p_rms, dtype=float).T,
    }
    for key, values in snapshots.items():
        # record-major -> method-major for convenient analysis
        arrays[key] = np.swapaxes(np.asarray(values, dtype=float), 0, 1)

    metadata = {
        **run,
        "requested_orders": requested_orders,
        "orders": orders,
        "config_sha256": config_hash(run),
        "model": "dense unconstrained 1/L residual tanh ResNet",
        "training": "ordinary Euclidean muP gradient flow",
        "surrogate": "coupled q/r finite-matrix response projection",
        "actual_compiled_liouville_pde_run": False,
        "integrator": "fixed-step classical RK4",
        "samples_recorded": len(times),
        "status": "completed",
    }
    arrays["metadata_json"] = np.asarray(canonical_json(metadata))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(output_path, **arrays)
    return metadata


def load_trace(path: Path) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    with np.load(path, allow_pickle=False) as data:
        arrays = {name: data[name] for name in data.files}
    metadata = json.loads(str(arrays.pop("metadata_json")))
    return metadata, arrays
