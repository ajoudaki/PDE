#!/usr/bin/env python3
"""Study-owned finite canonical gradient-flow producer.

All models use the maintained Gaussian draw, unhalved mean squared loss,
normalized data u=x/sqrt(2), and simultaneous physical mobilities (n,1,n).
The finite p=1 dictionary is frozen from that draw; no population initializer,
optimization step, readout solve, clipping, or state rescaling is used.
"""
from __future__ import annotations

import os
import time

MODULE_ENTRY_WALL = time.perf_counter()
MODULE_ENTRY_CPU = time.process_time()

for _thread_variable in (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import inspect
import json
from pathlib import Path
import platform
import resource
import signal
import sys

import numpy as np
import scipy
from scipy.integrate import DOP853
from threadpoolctl import threadpool_info, threadpool_limits

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "code"))
from pde.finite_network import initialize


MODEL_WIDTHS = {"width55": 55, "width105": 105, "closure1024": 1024}
LEVELS = {
    "primary": {"rtol": 1e-6, "atol": 1e-9, "max_step": 2.0},
    "fine": {"rtol": 1e-8, "atol": 1e-11, "max_step": 1.0},
    "finer": {"rtol": 1e-10, "atol": 1e-13, "max_step": 0.5},
}
CHECKPOINTS = np.array(
    [0, .01, .03, .1, .3, 1, 3, 5, 10, 20, 40, 60, 100, 160, 250,
     400, 630, 800, 1000],
    dtype=np.float64,
)
RIDGE = 1.0 / 4096.0
MAX_RHS = 150000
MAX_ACCEPTED_STEPS = 30000
EXPORT_RESERVE_SECONDS = 10.0


def circle_data(count: int, *, midpoint: bool = False) -> dict[str, np.ndarray]:
    """Uniform angular panel, with the user's actual x and normalized u."""
    theta = 2 * np.pi * (np.arange(count, dtype=np.float64) + (.5 if midpoint else 0)) / count
    x = np.column_stack((np.cos(theta), np.sin(theta)))
    labels = np.sqrt(32.0 / 21.0) * (
        np.cos(theta) + .5 * np.sin(3 * theta) + .25 * np.cos(5 * theta)
    )
    return {"theta": theta, "x": x, "u": x / np.sqrt(2.0), "y": labels}


def sech2(z: np.ndarray) -> np.ndarray:
    """Stable tanh derivative, identical to the maintained NumPy convention."""
    with np.errstate(under="ignore"):
        e = np.exp(-np.abs(z))
        return (2 * e / (1 + e * e)) ** 2


def array_sha256(array: np.ndarray) -> str:
    """Hash exact shape, dtype, and C-order working bytes."""
    a = np.ascontiguousarray(array)
    descriptor = json.dumps(
        {"dtype": a.dtype.str, "shape": list(a.shape)}, sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(descriptor + b"\n" + a.tobytes()).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


@dataclass
class Model:
    name: str
    seed: int
    W0: np.ndarray
    A0: np.ndarray
    c0: np.ndarray
    B1: np.ndarray | None = None
    B2: np.ndarray | None = None
    rawB1: np.ndarray | None = None
    rawB2: np.ndarray | None = None
    chol1: np.ndarray | None = None
    chol2: np.ndarray | None = None
    M0: np.ndarray | None = None

    def __post_init__(self):
        self.n = len(self.c0)
        self.is_closure = self.name == "closure1024"
        self.middle_shape = (3, 5) if self.is_closure else (self.n, self.n)
        self.train = circle_data(126)
        self.passive = circle_data(1024, midpoint=True)
        self.initial = self.pack(
            self.W0, self.M0 if self.is_closure else self.A0, self.c0,
        )
        if self.is_closure:
            self.B1T_over_n = np.ascontiguousarray(self.B1.T / self.n)
            self.B2T = np.ascontiguousarray(self.B2.T)
        for name in ("W0", "A0", "c0", "B1", "B2", "rawB1", "rawB2",
                     "chol1", "chol2", "M0", "initial"):
            value = getattr(self, name)
            if value is not None:
                value.flags.writeable = False

    def pack(self, W: np.ndarray, middle: np.ndarray, c: np.ndarray) -> np.ndarray:
        return np.concatenate((W.ravel(), middle.ravel(), c.ravel()))

    def unpack(self, state: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        split = 2 * self.n
        end_middle = split + int(np.prod(self.middle_shape))
        if state.shape != (end_middle + self.n,):
            raise ValueError("packed state shape mismatch")
        return (state[:split].reshape(self.n, 2),
                state[split:end_middle].reshape(self.middle_shape),
                state[end_middle:])

    def fields(self, state: np.ndarray, inputs: np.ndarray):
        W, middle, c = self.unpack(state)
        z1 = W @ inputs.T
        if not np.all(np.isfinite(z1)):
            raise FloatingPointError("nonfinite first preactivation")
        h1 = np.tanh(z1)
        if self.is_closure:
            z2 = self.B2 @ (middle @ (self.B1T_over_n @ h1))
        else:
            z2 = middle @ h1
        if not np.all(np.isfinite(z2)):
            raise FloatingPointError("nonfinite second preactivation")
        h2 = np.tanh(z2)
        return h1, h2, c @ h2 / self.n

    def predict(self, state: np.ndarray, inputs: np.ndarray) -> np.ndarray:
        result = self.fields(state, inputs)[2]
        if not np.all(np.isfinite(result)):
            raise FloatingPointError("nonfinite prediction")
        return result

    def rhs(self, t: float, state: np.ndarray, inputs=None, labels=None) -> np.ndarray:
        """Analytic physical GF. The time argument is intentionally unused."""
        if inputs is None:
            inputs, labels = self.train["u"], self.train["y"]
        if not np.all(np.isfinite(state)):
            raise FloatingPointError("nonfinite ODE state")
        W, middle, c = self.unpack(state)
        z1 = W @ inputs.T
        if not np.all(np.isfinite(z1)):
            raise FloatingPointError("nonfinite first preactivation")
        h1 = np.tanh(z1)
        if self.is_closure:
            a = self.B1T_over_n @ h1
            z2 = self.B2 @ (middle @ a)
            if not np.all(np.isfinite(z2)):
                raise FloatingPointError("nonfinite second preactivation")
            h2 = np.tanh(z2)
            residual_weight = (c @ h2 / self.n - labels) / len(labels)
            dc = -2 * (h2 @ residual_weight)
            d = (self.B2T * (c / self.n)) @ sech2(z2)
            q = (self.B1 @ middle.T) @ d
            dW = -2 * ((sech2(z1) * q * residual_weight) @ inputs)
            dmiddle = -2 * ((d * residual_weight) @ a.T)
        else:
            z2 = middle @ h1
            if not np.all(np.isfinite(z2)):
                raise FloatingPointError("nonfinite second preactivation")
            h2 = np.tanh(z2)
            residual_weight = (c @ h2 / self.n - labels) / len(labels)
            delta2 = c[:, None] * sech2(z2)
            delta1 = (middle.T @ delta2) * sech2(z1)
            dW = -2 * ((delta1 * residual_weight) @ inputs)
            dmiddle = (-2 / self.n) * ((delta2 * residual_weight) @ h1.T)
            dc = -2 * (h2 @ residual_weight)
        result = self.pack(dW, dmiddle, dc)
        if not np.all(np.isfinite(result)):
            raise FloatingPointError("nonfinite ODE velocity")
        return result

    def dissipation(self, velocity: np.ndarray) -> float:
        """-dL/dt=sum(Wdot²)/n+sum(middledot²)+sum(cdot²)/n."""
        dW, dmiddle, dc = self.unpack(velocity)
        return float(np.sum(dW * dW) / self.n
                     + np.sum(dmiddle * dmiddle) + np.sum(dc * dc) / self.n)

    def source_arrays(self) -> dict[str, np.ndarray]:
        result = {"W0": self.W0, "A0": self.A0, "c0": self.c0,
                  "initial_state": self.initial}
        for name in ("B1", "B2", "rawB1", "rawB2", "chol1", "chol2", "M0"):
            value = getattr(self, name)
            if value is not None:
                result[name] = value
        for label, panel in (("train", self.train), ("passive", self.passive)):
            result.update({label + "_" + name: value for name, value in panel.items()})
        return result

    def counts(self) -> dict:
        dynamic = self.initial.size
        if self.is_closure:
            frozen = self.B1.size + self.B2.size
            algorithmic = dynamic + frozen
        else:
            frozen, algorithmic = 0, dynamic
        return {"dynamic_scalars": dynamic, "dynamic_bytes": dynamic * 8,
                "frozen_dictionary_scalars": frozen,
                "dynamic_plus_dictionary_scalars": algorithmic,
                "dynamic_plus_dictionary_bytes": algorithmic * 8,
                "dense_source_scalars": self.W0.size + self.A0.size + self.c0.size,
                "archival_source_copies_needed_after_initialization": False,
                "archive_and_solver_workspace_excluded": True}


def build_model(name: str, seed: int) -> Model:
    n = MODEL_WIDTHS[name]
    draw = initialize(n, 2, 2, seed=seed)
    W, A, c = draw.weights[0], draw.weights[1], draw.readout
    if name != "closure1024":
        return Model(name, seed, W, A, c)
    H = np.tanh(W)
    U = np.tanh(A @ H)
    R = np.tanh(A.T @ U)
    rawB1 = np.column_stack((np.ones(n), H, R))
    rawB2 = np.column_stack((np.ones(n), U))
    chol1 = np.linalg.cholesky(rawB1.T @ rawB1 / n + RIDGE * np.eye(5))
    chol2 = np.linalg.cholesky(rawB2.T @ rawB2 / n + RIDGE * np.eye(3))
    # solve(L, raw.T).T = raw @ L**(-T), with lower Cholesky L.
    B1 = np.ascontiguousarray(np.linalg.solve(chol1, rawB1.T).T)
    B2 = np.ascontiguousarray(np.linalg.solve(chol2, rawB2.T).T)
    M0 = (B2.T @ A @ B1) / n
    return Model(name, seed, W, A, c, B1, B2, rawB1, rawB2, chol1, chol2, M0)


class WallBudgetExceeded(RuntimeError):
    pass


class RunInterrupted(RuntimeError):
    pass


class ResourceBudgetExceeded(RuntimeError):
    pass


def _write_json(path: Path, record: dict):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(record, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write("\n")


def _snapshot(model: Model, t: float, state: np.ndarray, velocity=None) -> dict:
    velocity = model.rhs(t, state) if velocity is None else velocity.copy()
    h1, h2, train_prediction = model.fields(state, model.train["u"])
    h10, h20, _ = model.fields(model.initial, model.train["u"])
    passive_prediction = model.predict(state, model.passive["u"])
    W, middle, _ = model.unpack(state)
    z1 = W @ model.train["u"].T
    z2 = (model.B2 @ (middle @ (model.B1T_over_n @ h1))
          if model.is_closure else middle @ h1)
    saturation = np.array([
        [np.max(np.abs(z)), np.mean(np.abs(z) > 20), np.mean(np.abs(h) == 1)]
        for z, h in ((z1, h1), (z2, h2))
    ])
    return {
        "time": np.array(t), "state": state.copy(), "rhs": velocity,
        "train_prediction": train_prediction, "passive_prediction": passive_prediction,
        "train_loss": np.array(np.mean((train_prediction - model.train["y"]) ** 2)),
        "passive_loss": np.array(np.mean((passive_prediction - model.passive["y"]) ** 2)),
        "dissipation": np.array(model.dissipation(velocity)),
        "hidden_rms_displacement": np.array([
            np.sqrt(np.mean((h1 - h10) ** 2)), np.sqrt(np.mean((h2 - h20) ** 2)),
        ]),
        "saturation_diagnostics": saturation,
    }


def run(model_name: str, seed: int, level: str, output: Path, wall_seconds: float,
        *, checkpoints: np.ndarray | None = None, clock_origin=None) -> dict:
    """Run one declared trajectory. Alternate checkpoints are for preflight only."""
    start_wall, start_cpu = ((time.perf_counter(), time.process_time())
                             if clock_origin is None else clock_origin)
    started_utc = datetime.now(timezone.utc).isoformat()
    if not np.isfinite(wall_seconds) or wall_seconds <= 0:
        raise ValueError("wall-seconds must be positive and finite")
    times = CHECKPOINTS.copy() if checkpoints is None else np.asarray(checkpoints, dtype=float)
    if (times.ndim != 1 or len(times) < 2 or times[0] != 0
            or not np.all(np.isfinite(times)) or not np.all(np.diff(times) > 0)):
        raise ValueError("checkpoint times must start at zero and strictly increase")
    output = Path(output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    config = {"model": model_name, "seed": seed, "level": level,
              "solver": "scipy.integrate.DOP853", **LEVELS[level],
              "checkpoints": times.tolist(), "wall_seconds": wall_seconds,
              "loss": "mean((prediction-label)**2)", "mobilities": [MODEL_WIDTHS[model_name], 1, MODEL_WIDTHS[model_name]],
              "checkpoint_policy": "accepted endpoints; restart DOP853 at each checkpoint",
              "dtype": "float64", "numerical_threads": 1,
              "wall_clock_origin": "run() entry for imported preflight; CLI module entry for CLI runs",
              "export_reserve_seconds": EXPORT_RESERVE_SECONDS,
              "rhs_limit": MAX_RHS, "accepted_step_limit": MAX_ACCEPTED_STEPS,
              "cleanup_policy": "stop evolution 10 seconds before wall limit; preserve last accepted state",
              "command": sys.argv, "cwd": os.getcwd()}
    _write_json(output / "config.json", config)
    phase = {"initialization": 0.0, "evolution": 0.0, "observations": 0.0,
             "step_diagnostics": 0.0, "serialization": 0.0}
    source_paths = [Path(__file__).resolve(), REPO / "code/pde/__init__.py", REPO / "code/pde/finite_network.py",
                    Path(inspect.getsourcefile(DOP853)).resolve()]
    scipy_rk = Path(inspect.getsourcefile(DOP853)).resolve()
    source_paths.extend(scipy_rk.with_name(name) for name in (
        "base.py", "common.py", "dop853_coefficients.py"))
    for filename in ("PROTOCOL.md",):
        path = Path(__file__).with_name(filename)
        if path.exists():
            source_paths.append(path)
    source_hashes = {str(path): file_sha256(path) for path in source_paths}
    ode_calls, snapshot_calls, accepted_steps = 0, 0, 0
    last_state, last_t, solver = None, 0.0, None
    snapshots = []
    model = None
    status, failure = "running", None
    last_h_abs = None

    def check_budget():
        if time.perf_counter() - start_wall >= max(0.0, wall_seconds - EXPORT_RESERVE_SECONDS):
            raise WallBudgetExceeded("evolution wall allowance reached; final export reserve started")

    def fun(t, state):
        nonlocal ode_calls
        check_budget()
        if ode_calls + snapshot_calls >= MAX_RHS:
            raise ResourceBudgetExceeded("RHS evaluation limit reached")
        ode_calls += 1
        return model.rhs(t, state)

    def capture(t, state, velocity=None):
        nonlocal snapshot_calls
        phase_start = time.perf_counter()
        if velocity is None:
            snapshot_calls += 1
        snap = _snapshot(model, t, state, velocity)
        snap["wall_seconds"] = np.array(time.perf_counter() - start_wall)
        snap["nfev_ode"] = np.array(ode_calls, dtype=np.int64)
        phase["observations"] += time.perf_counter() - phase_start
        return snap

    def interrupted(signum, frame):
        raise RunInterrupted("received signal " + str(signum))

    old_sigterm = signal.signal(signal.SIGTERM, interrupted)
    step_columns = ["accepted_index", "time", "loss", "step", "nfev_ode",
                    "wall_seconds", "dissipation"]
    with threadpool_limits(limits=1), (output / "accepted_steps.csv").open("x", newline="") as step_file:
        writer = csv.DictWriter(step_file, fieldnames=step_columns)
        writer.writeheader()
        try:
            phase_start = time.perf_counter()
            model = build_model(model_name, seed)
            phase["initialization"] = time.perf_counter() - phase_start
            last_state = model.initial.copy()
            source = model.source_arrays()
            phase_start = time.perf_counter()
            np.savez(output / "source.npz", **source)
            phase["serialization"] += time.perf_counter() - phase_start
            snapshots.append(capture(0.0, last_state))
            writer.writerow({"accepted_index": 0, "time": 0.0,
                             "loss": float(snapshots[-1]["train_loss"]), "step": 0.0,
                             "nfev_ode": 0, "wall_seconds": time.perf_counter() - start_wall,
                             "dissipation": float(snapshots[-1]["dissipation"])})
            step_file.flush()
            check_budget()
            for bound in times[1:]:
                phase_start = time.perf_counter()
                try:
                    first_step = None if last_h_abs is None else min(last_h_abs, float(bound - last_t))
                    solver = DOP853(fun, last_t, last_state, float(bound),
                                    first_step=first_step, **LEVELS[level])
                finally:
                    phase["evolution"] += time.perf_counter() - phase_start
                while solver.status == "running":
                    check_budget()
                    if accepted_steps >= MAX_ACCEPTED_STEPS:
                        raise ResourceBudgetExceeded("accepted step limit reached")
                    phase_start = time.perf_counter()
                    try:
                        message = solver.step()
                    finally:
                        phase["evolution"] += time.perf_counter() - phase_start
                    if solver.status == "failed":
                        raise RuntimeError("DOP853 failed: " + str(message))
                    if not np.all(np.isfinite(solver.y)):
                        raise FloatingPointError("nonfinite accepted endpoint")
                    last_state, last_t = solver.y.copy(), float(solver.t)
                    accepted_steps += 1
                    phase_start = time.perf_counter()
                    prediction = model.predict(last_state, model.train["u"])
                    loss = float(np.mean((prediction - model.train["y"]) ** 2))
                    if not np.isfinite(loss):
                        raise FloatingPointError("nonfinite accepted loss")
                    writer.writerow({"accepted_index": accepted_steps, "time": last_t,
                                     "loss": loss, "step": float(solver.step_size),
                                     "nfev_ode": ode_calls, "wall_seconds": time.perf_counter() - start_wall,
                                     "dissipation": model.dissipation(solver.f)})
                    step_file.flush()
                    phase["step_diagnostics"] += time.perf_counter() - phase_start
                last_h_abs = float(solver.h_abs)
                snapshots.append(capture(last_t, last_state, solver.f))
                check_budget()
            status = "completed"
        except WallBudgetExceeded as error:
            status, failure = "wall_censored", str(error)
        except RunInterrupted as error:
            status, failure = "interrupted", str(error)
        except ResourceBudgetExceeded as error:
            status, failure = "resource_censored", str(error)
        except (FloatingPointError, ValueError, RuntimeError, OverflowError, np.linalg.LinAlgError) as error:
            status, failure = "numerical_failure", type(error).__name__ + ": " + str(error)
        finally:
            signal.signal(signal.SIGTERM, old_sigterm)
        termination_wall = time.perf_counter() - start_wall
        if last_state is not None:
            last_velocity = (solver.f if solver is not None and solver.t == last_t
                             and np.array_equal(solver.y, last_state) else None)
            if last_velocity is None and snapshots and float(snapshots[-1]["time"]) == last_t:
                last_velocity = snapshots[-1]["rhs"]
            final = capture(last_t, last_state, last_velocity)
            phase_start = time.perf_counter()
            np.savez(output / "final.npz", **final)
            phase["serialization"] += time.perf_counter() - phase_start
        else:
            final = None
        if snapshots:
            phase_start = time.perf_counter()
            np.savez(output / "checkpoints.npz", **{
                {"time": "times", "state": "states"}.get(key, key):
                np.stack([snapshot[key] for snapshot in snapshots]) for key in snapshots[0]
            })
            phase["serialization"] += time.perf_counter() - phase_start
        record = {
            "format": "smooth-circle-canonical-flow-v1", "status": status,
            "failure": failure, "started_utc": started_utc, "config": config,
            "physical_time": last_t, "final_loss": None if final is None else float(final["train_loss"]),
            "final_passive_loss": None if final is None else float(final["passive_loss"]),
            "completed_checkpoints": [float(snap["time"]) for snap in snapshots],
            "accepted_steps": accepted_steps, "nfev_ode": ode_calls,
            "rhs_calls_observation": snapshot_calls,
            "rhs_calls_total": ode_calls + snapshot_calls,
            "counts": None if model is None else model.counts(),
            "source_sha256": source_hashes,
            "source_array_sha256": {} if model is None else {
                key: array_sha256(value) for key, value in model.source_arrays().items()
            },
            "output_sha256": {path.name: file_sha256(path) for path in output.iterdir() if path.is_file()},
            "timing": {"wall_at_termination": termination_wall,
                       "wall_before_result_write": time.perf_counter() - start_wall,
                       "cleanup_wall": time.perf_counter() - start_wall - termination_wall,
                       "cpu_before_result_write": time.process_time() - start_cpu,
                       "phases_wall": phase},
            "environment": {"python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
                            "platform": platform.platform(), "machine": platform.machine(),
                            "executable": sys.executable, "threadpools": threadpool_info(),
                            "thread_variables": {name: os.environ.get(name) for name in (
                                "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                                "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")},
                            "peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024},
            "working_formula_notes": "Float64 tanh and stable sech^2(z)=(2*exp(-abs(z))/(1+exp(-2*abs(z))))^2.",
            "saturation_columns": ["maximum_absolute_preactivation", "fraction_abs_z_gt20", "fraction_abs_tanh_equals1"],
            "saturation_panel": "126 training points; layer axis first,second",
            "git_head_supplied_by_runner": os.environ.get("FLOW_GIT_HEAD"),
            "scope": "Finite widths and fixed finite dictionary; no population-limit or convergence claim.",
        }
        if model is not None and model.is_closure:
            record["dictionary"] = {
                "raw_first_columns": ["1", "tanh(W0[:,0])", "tanh(W0[:,1])", "tanh(A0.T@U)[:,0]", "tanh(A0.T@U)[:,1]"],
                "raw_second_columns": ["1", "U[:,0]", "U[:,1]"],
                "U": "tanh(A0@tanh(W0))", "ridge": RIDGE,
                "normalization": "rawB @ chol(rawB.T@rawB/n + I/4096)^(-T)",
                "contraction": "M0=B2.T@A0@B1/n",
                "regularized_gram_condition": [
                    float(np.linalg.cond(model.chol1 @ model.chol1.T)),
                    float(np.linalg.cond(model.chol2 @ model.chol2.T)),
                ],
            }
        _write_json(output / "result.json", record)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=MODEL_WIDTHS, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--level", choices=LEVELS, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--wall-seconds", type=float, default=400.0)
    args = parser.parse_args()
    if args.seed < 0:
        parser.error("seed must be nonnegative")
    result = run(args.model, args.seed, args.level, args.output, args.wall_seconds,
                 clock_origin=(MODULE_ENTRY_WALL, MODULE_ENTRY_CPU))
    print(json.dumps({key: result[key] for key in (
        "status", "physical_time", "final_loss", "accepted_steps", "nfev_ode")}, sort_keys=True))
    return 0 if result["status"] == "completed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
