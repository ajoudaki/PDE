#!/usr/bin/env python3
"""Bounded ordinary physical-flow engine for the coupled width ladder."""

from __future__ import annotations

import gc
import hashlib
import importlib.util
import math
import os
import platform
import resource
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np
import torch


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[4]
CANONICAL_MODEL_PATH = (
    REPO_ROOT
    / "studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference"
    / "canonical_model.py"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_canonical_model():
    spec = importlib.util.spec_from_file_location(
        "hybrid_width_canonical_model", CANONICAL_MODEL_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load canonical model at {CANONICAL_MODEL_PATH}")
    module = importlib.util.module_from_spec(spec)
    # Dataclasses inspect sys.modules while the module is executing.
    import sys

    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


canonical_model = _load_canonical_model()

from nested_rng import generate_nested_antithetic_state  # noqa: E402


class BudgetStop(RuntimeError):
    pass


class NumericalInvalid(RuntimeError):
    pass


@dataclass(frozen=True)
class Caps:
    wall_seconds: float
    max_steps_all_batches: int
    host_rss_gib: float
    gpu_memory_gib: float
    state_ceiling: float
    kernel_ceiling: float
    kernel_floor: float
    diagnostic_stride: int

    @classmethod
    def from_dict(cls, values: dict[str, Any]) -> "Caps":
        return cls(
            wall_seconds=float(values["wall_seconds"]),
            max_steps_all_batches=int(values["max_steps_all_batches"]),
            host_rss_gib=float(values["host_rss_gib"]),
            gpu_memory_gib=float(values["gpu_memory_gib"]),
            state_ceiling=float(values["state_ceiling"]),
            kernel_ceiling=float(values["kernel_ceiling"]),
            kernel_floor=float(values["kernel_floor"]),
            diagnostic_stride=int(values["diagnostic_stride"]),
        )


class Guard:
    def __init__(
        self,
        caps: Caps,
        device: torch.device,
        progress_callback: Callable[[dict[str, float | int]], None] | None = None,
    ) -> None:
        self.caps = caps
        self.device = device
        self.started = time.monotonic()
        self.steps = 0
        self.max_host_rss_gib = 0.0
        self.max_gpu_allocated_gib = 0.0
        self.max_state_amplitude = 0.0
        self.progress_callback = progress_callback

    @staticmethod
    def host_rss_gib() -> float:
        return float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20

    def observe_resources(self) -> None:
        self.max_host_rss_gib = max(self.max_host_rss_gib, self.host_rss_gib())
        if self.device.type == "cuda":
            allocated = float(torch.cuda.max_memory_allocated(self.device)) / 2**30
            self.max_gpu_allocated_gib = max(
                self.max_gpu_allocated_gib, allocated
            )

    def _budget_stop(self, message: str) -> None:
        exc = BudgetStop(message)
        exc.point_diagnostics = self.summary()
        raise exc

    def check_budget(self) -> None:
        self.observe_resources()
        elapsed = time.monotonic() - self.started
        if elapsed >= self.caps.wall_seconds:
            self._budget_stop(
                f"wall cap {self.caps.wall_seconds:.3f}s reached at {elapsed:.3f}s"
            )
        if self.steps > self.caps.max_steps_all_batches:
            self._budget_stop("integrator-step cap reached")
        if self.max_host_rss_gib > self.caps.host_rss_gib:
            self._budget_stop("host RSS cap reached")
        if (
            self.device.type == "cuda"
            and self.max_gpu_allocated_gib > self.caps.gpu_memory_gib
        ):
            self._budget_stop("GPU allocation cap reached")

    def check_before_step(self) -> None:
        """Fail before starting any step that would exceed a hard cap."""

        self.check_budget()
        if self.steps >= self.caps.max_steps_all_batches:
            self._budget_stop("integrator-step cap reached before next step")

    def validate(self, state, obs) -> None:
        tensors = (obs.output, obs.kernel, obs.kernel_a, obs.kernel_W, obs.kernel_u)
        if not all(bool(torch.all(torch.isfinite(x)).item()) for x in tensors):
            raise NumericalInvalid("nonfinite state observable")
        if bool(torch.any(obs.kernel <= self.caps.kernel_floor).item()):
            raise NumericalInvalid("kernel reached declared floor")
        if bool(torch.any(obs.kernel >= self.caps.kernel_ceiling).item()):
            raise NumericalInvalid("kernel reached declared ceiling")
        if not canonical_model.state_all_finite(state):
            raise NumericalInvalid("nonfinite parameter state")
        amplitude = float(torch.amax(canonical_model.state_max_abs(state)).item())
        self.max_state_amplitude = max(self.max_state_amplitude, amplitude)
        if amplitude >= self.caps.state_ceiling:
            raise NumericalInvalid("parameter state reached declared ceiling")
        if self.progress_callback is not None:
            self.progress_callback(self.summary())
        self.check_budget()

    def summary(self) -> dict[str, float | int]:
        self.observe_resources()
        return {
            "elapsed_seconds": time.monotonic() - self.started,
            "integrator_steps_all_batches": self.steps,
            "max_host_rss_gib": self.max_host_rss_gib,
            "max_gpu_allocated_gib": self.max_gpu_allocated_gib,
            "max_state_amplitude": self.max_state_amplitude,
        }


def fused_physical_eval(state, *, target: float):
    """Return physical RHS and all observables from one primitive evaluation."""

    n = state.width
    inv_n = 1.0 / n
    inv_sqrt_n = 1.0 / math.sqrt(n)
    u2, z, az, v = canonical_model.forward_primitives(state)
    output = torch.mean(state.a * z.square(), dim=1)
    sum_u4 = torch.sum(u2.square(), dim=1)
    sum_az2 = torch.sum(az.square(), dim=1)
    kernel_a = inv_n * torch.sum(z.pow(4), dim=1)
    kernel_W = 4.0 * inv_n**2 * sum_az2 * sum_u4
    kernel_u = 16.0 * inv_n**2 * torch.sum(u2 * v.square(), dim=1)
    obs = canonical_model.Observables(
        output=output,
        kernel=kernel_a + kernel_W + kernel_u,
        q1=torch.mean(u2, dim=1),
        q2=torch.mean(z.square(), dim=1),
        kernel_a=kernel_a,
        kernel_W=kernel_W,
        kernel_u=kernel_u,
    )
    factor = 2.0 * (target - output)
    raw_a = z.square()
    raw_W = (2.0 * inv_sqrt_n) * az.unsqueeze(2) * u2.unsqueeze(1)
    raw_u = (4.0 * inv_sqrt_n) * state.u * v
    tangent = canonical_model.State(
        raw_a * factor[:, None],
        raw_W * factor[:, None, None],
        raw_u * factor[:, None],
    )
    return tangent, obs


def rk4_step_with_k1(state, k1, step: float, *, target: float):
    k2, _ = fused_physical_eval(
        canonical_model.add_scaled(state, k1, 0.5 * step), target=target
    )
    k3, _ = fused_physical_eval(
        canonical_model.add_scaled(state, k2, 0.5 * step), target=target
    )
    k4, _ = fused_physical_eval(
        canonical_model.add_scaled(state, k3, step), target=target
    )
    return canonical_model.linear_combination(
        state,
        (
            (1.0 / 6.0, k1),
            (1.0 / 3.0, k2),
            (1.0 / 3.0, k3),
            (1.0 / 6.0, k4),
        ),
        step,
    )


def rk4_step(state, step: float, *, target: float, kernel_floor: float):
    del kernel_floor
    k1, _ = fused_physical_eval(state, target=target)
    return rk4_step_with_k1(state, k1, step, target=target)


def _integer_steps(endpoint: float, step: float) -> int:
    count = int(round(endpoint / step))
    if count < 1 or not math.isclose(
        count * step, endpoint, rel_tol=0.0, abs_tol=1e-13
    ):
        raise ValueError("max_time must be a positive exact step endpoint")
    return count


def _pair_average(values: torch.Tensor) -> torch.Tensor:
    if values.shape[0] % 2:
        raise ValueError("trajectory axis is not antithetic-paired")
    return values.reshape(values.shape[0] // 2, 2).mean(dim=1)


def _record_row(curves: dict[str, torch.Tensor], row: int, obs, target: float) -> None:
    residual = target - obs.output
    curves["output"][row] = obs.output
    curves["kernel"][row] = obs.kernel
    curves["weighted_kernel"][row] = residual * obs.kernel
    curves["loss"][row] = residual.square()
    curves["q1"][row] = obs.q1
    curves["q2"][row] = obs.q2


def _simulate_batch(
    point: dict[str, Any],
    lineage_ids: np.ndarray,
    *,
    seed: int,
    device: torch.device,
    guard: Guard,
) -> dict[str, np.ndarray]:
    width = int(point["width"])
    step = float(point["step"])
    max_time = float(point["max_time"])
    steps = _integer_steps(max_time, step)
    target = float(point.get("target", 1.0))
    if target != 1.0:
        raise ValueError("the frozen campaign target is exactly one")

    state, initial_state_sha256 = generate_nested_antithetic_state(
        width,
        lineage_ids,
        seed,
        device=device,
        dtype=torch.float64,
        row_block=int(point.get("rng_row_block", 256)),
        return_digests=True,
    )
    count = 2 * len(lineage_ids)
    fields = ("output", "kernel", "weighted_kernel", "loss", "q1", "q2")
    curves = {
        key: torch.empty((steps + 1, count), dtype=torch.float64, device=device)
        for key in fields
    }

    with torch.no_grad():
        tangent, initial = fused_physical_eval(state, target=target)
        guard.validate(state, initial)
        paired_output_sum = initial.output.reshape(-1, 2).sum(dim=1)
        cancellation = float(torch.max(torch.abs(paired_output_sum)).item())
        cancellation_scale = max(1.0, float(torch.max(torch.abs(initial.output)).item()))
        cancellation_tol = 64.0 * torch.finfo(torch.float64).eps * cancellation_scale
        if cancellation > cancellation_tol:
            raise NumericalInvalid("initial antithetic output cancellation failed")
        for component in (initial.kernel_a, initial.kernel_W, initial.kernel_u):
            branches = component.reshape(-1, 2)
            if not torch.equal(branches[:, 0], branches[:, 1]):
                raise NumericalInvalid("initial antithetic kernel component mismatch")
        component_sum = initial.kernel_a + initial.kernel_W + initial.kernel_u
        if not torch.equal(component_sum, initial.kernel):
            # Canonical evaluation uses exactly this addition order, so equality
            # is expected.  Fall back to an ulp-scale check only for backend
            # reassociation.
            torch.testing.assert_close(
                component_sum, initial.kernel, rtol=8e-15, atol=8e-15
            )
        _record_row(curves, 0, initial, target)
        init_components = torch.stack(
            (
                _pair_average(initial.kernel_a),
                _pair_average(initial.kernel_W),
                _pair_average(initial.kernel_u),
            ),
            dim=1,
        )

        for index in range(1, steps + 1):
            guard.check_before_step()
            state = rk4_step_with_k1(state, tangent, step, target=target)
            guard.steps += 1
            tangent, obs = fused_physical_eval(state, target=target)
            _record_row(curves, index, obs, target)
            if index % guard.caps.diagnostic_stride == 0 or index == steps:
                guard.validate(state, obs)

    result = {
        key: value.detach().cpu().numpy().astype(np.float64, copy=False)
        for key, value in curves.items()
    }
    result["initial_components"] = (
        init_components.detach().cpu().numpy().astype(np.float64, copy=False)
    )
    result["initial_total"] = result["initial_components"].sum(axis=1)
    result["lineage_ids"] = lineage_ids.astype(np.int64, copy=True)
    result["initial_state_sha256"] = initial_state_sha256
    result["antithetic_cancellation"] = np.array(cancellation, dtype=np.float64)
    result["antithetic_cancellation_tolerance"] = np.array(
        cancellation_tol, dtype=np.float64
    )
    del state, curves, initial, init_components
    gc.collect()
    if device.type == "cuda":
        torch.cuda.empty_cache()
    return result


def _validate_raw_point(
    arrays: dict[str, np.ndarray], point: dict[str, Any]
) -> dict[str, float]:
    output = arrays["raw_output"]
    kernel = arrays["raw_kernel"]
    loss = arrays["raw_loss"]
    nodes = np.asarray(point["output_nodes"], dtype=np.float64)
    monotone_tol = float(point["monotonic_tolerance"])
    target = float(point.get("target", 1.0))
    if not np.all(np.isfinite(output)) or not np.all(np.isfinite(kernel)):
        raise NumericalInvalid("nonfinite raw curve")
    if np.any(kernel <= 0.0):
        raise NumericalInvalid("nonpositive raw kernel")

    mean_output = output.mean(axis=1)
    min_mean_increment = float(np.min(np.diff(mean_output)))
    if min_mean_increment < -monotone_tol:
        raise NumericalInvalid("ensemble mean output is nonmonotone")
    if abs(mean_output[0]) > float(point["mean_initial_output_tolerance"]):
        raise NumericalInvalid("antithetic ensemble mean does not start at zero")
    if mean_output[-1] < nodes[-1] - monotone_tol:
        raise NumericalInvalid("ensemble mean does not reach final output node")

    mean_loss = loss.mean(axis=1)
    max_loss_increment = float(np.max(np.diff(mean_loss)))
    if max_loss_increment > float(point["loss_nonincrease_tolerance"]):
        raise NumericalInvalid("ensemble mean loss increases")

    f0 = output[0]
    if np.any(f0 >= target):
        raise NumericalInvalid("a trajectory starts at or above the target")
    progress = (output - f0[None, :]) / (target - f0[None, :])
    min_progress_increment = float(np.min(np.diff(progress, axis=0)))
    if min_progress_increment < -monotone_tol:
        raise NumericalInvalid("a normalized-progress trajectory is nonmonotone")
    if np.any(progress[-1] < nodes[-1] - monotone_tol):
        raise NumericalInvalid("at least one trajectory does not hit the final node")

    return {
        "minimum_mean_output_increment": min_mean_increment,
        "maximum_mean_loss_increment": max_loss_increment,
        "minimum_path_progress_increment": min_progress_increment,
        "terminal_mean_output": float(mean_output[-1]),
        "minimum_terminal_path_progress": float(np.min(progress[-1])),
        "maximum_abs_initial_output": float(np.max(np.abs(f0))),
    }


def run_point(
    point: dict[str, Any],
    *,
    seed: int,
    device: torch.device,
    progress_callback: Callable[[dict[str, float | int]], None] | None = None,
) -> tuple[dict[str, np.ndarray], dict[str, Any]]:
    """Run one frozen point and retain raw curves for honest re-inversion."""

    if str(point.get("mode")) != "physical":
        raise ValueError("only ordinary physical mode is admitted")
    if str(point.get("dtype")) != "float64":
        raise ValueError("only float64 is admitted")
    start = int(point["lineage_start"])
    stop = int(point["lineage_stop"])
    if start < 0 or stop <= start:
        raise ValueError("invalid half-open lineage range")
    all_ids = np.arange(start, stop, dtype=np.int64)
    batch_size = int(point["pair_batch_size"])
    if batch_size < 1:
        raise ValueError("pair_batch_size must be positive")
    caps = Caps.from_dict(point["caps"])
    guard = Guard(caps, device, progress_callback=progress_callback)
    batches = []
    for offset in range(0, len(all_ids), batch_size):
        guard.check_budget()
        batch_ids = all_ids[offset : offset + batch_size]
        batches.append(
            _simulate_batch(
                point, batch_ids, seed=seed, device=device, guard=guard
            )
        )

    steps = _integer_steps(float(point["max_time"]), float(point["step"]))
    arrays: dict[str, np.ndarray] = {
        "raw_time": np.arange(steps + 1, dtype=np.float64) * float(point["step"]),
        "lineage_ids": np.concatenate([batch["lineage_ids"] for batch in batches]),
        "initial_components": np.concatenate(
            [batch["initial_components"] for batch in batches], axis=0
        ),
        "initial_total": np.concatenate(
            [batch["initial_total"] for batch in batches], axis=0
        ),
        "initial_state_sha256": np.concatenate(
            [batch["initial_state_sha256"] for batch in batches], axis=0
        ),
        "output_nodes": np.asarray(point["output_nodes"], dtype=np.float64),
    }
    for key in ("output", "kernel", "weighted_kernel", "loss", "q1", "q2"):
        arrays[f"raw_{key}"] = np.concatenate([batch[key] for batch in batches], axis=1)

    try:
        diagnostics = _validate_raw_point(arrays, point)
    except Exception as exc:
        exc.point_diagnostics = guard.summary()
        raise
    diagnostics.update(guard.summary())
    diagnostics["max_antithetic_cancellation"] = float(
        max(float(batch["antithetic_cancellation"]) for batch in batches)
    )
    diagnostics["max_antithetic_cancellation_tolerance"] = float(
        max(float(batch["antithetic_cancellation_tolerance"]) for batch in batches)
    )
    diagnostics["trajectory_count"] = int(arrays["raw_output"].shape[1])
    diagnostics["lineage_count"] = int(len(arrays["lineage_ids"]))
    return arrays, diagnostics


def environment_record(device: torch.device) -> dict[str, Any]:
    record: dict[str, Any] = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "pid": os.getpid(),
        "torch": torch.__version__,
        "numpy": np.__version__,
        "device": str(device),
        "canonical_model_path": str(CANONICAL_MODEL_PATH),
        "canonical_model_sha256": sha256_file(CANONICAL_MODEL_PATH),
    }
    if device.type == "cuda":
        record.update(
            {
                "cuda_device_name": torch.cuda.get_device_name(device),
                "cuda_runtime": torch.version.cuda,
                "cuda_device_count": torch.cuda.device_count(),
            }
        )
    return record
