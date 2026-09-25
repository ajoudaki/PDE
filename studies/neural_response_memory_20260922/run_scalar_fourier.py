"""Bounded scalar-Fourier/dense comparison; see SCALAR_FOURIER_EXPERIMENT_PROTOCOL.md.

Run from the repository root with a fresh --out directory. The reference-only
phase can run while a compiler is being developed; --phase scalars continues
that same directory and never overwrites an existing cell.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pickle
import platform
import sys
import time
from pathlib import Path

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np
import scipy
from scipy.integrate import solve_ivp

from scalar_fourier_reference import DenseReference, PopulationReference, initialize

ANGLES = np.deg2rad([10., 125.])
U = np.stack([np.cos(ANGLES), np.sin(ANGLES)])
LABELS = np.array([1., -1.])
THETA = np.arange(4096) * (2 * np.pi / 4096)
CIRCLE = np.stack([np.cos(THETA), np.sin(THETA)])
CONFIG = dict(width=16, seed=20260920, depth=3, activation="tanh", P=1,
              J=8, cutoffs=[5, 7, 9, 11], horizon=40., target_mse=.001,
              angles_degrees=[10., 125.], labels=LABELS.tolist(),
              quadrature=256, circle_points=4096, rtol=1e-7, atol=1e-9,
              fit_wall_seconds=120., compiler_wall_seconds=120.,
              max_patterns=4000, max_terms=200000, state_limit=1e8)


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def hashes():
    folder = Path(__file__).parent
    names = ["run_scalar_fourier.py", "scalar_fourier_reference.py",
             "scalar_fourier_engine.py", "SCALAR_FOURIER_EXPERIMENT_PROTOCOL.md"]
    return {name: hashlib.sha256((folder / name).read_bytes()).hexdigest()
            for name in names if (folder / name).exists()}


def rms(a):
    return float(np.sqrt(np.mean(np.asarray(a) ** 2)))


def fit(rhs, initial, output, *, rtol, atol, stop_at_target):
    start = time.monotonic()
    last = [0., np.array(initial, copy=True)]

    def checked_rhs(t, z):
        if time.monotonic() - start > CONFIG["fit_wall_seconds"]:
            raise TimeoutError(f"fit exceeded wall budget at t={t:.8g}")
        if not np.all(np.isfinite(z)) or np.max(np.abs(z)) > CONFIG["state_limit"]:
            raise FloatingPointError(f"state exceeded validity limit at t={t:.8g}")
        value = rhs(t, z)
        if not np.all(np.isfinite(value)):
            raise FloatingPointError(f"nonfinite derivative at t={t:.8g}")
        last[:] = [float(t), np.array(z, copy=True)]
        return value

    def event(t, z):
        return float(np.mean((output(z) - LABELS) ** 2) - CONFIG["target_mse"])
    event.terminal = stop_at_target
    event.direction = -1
    try:
        sol = solve_ivp(checked_rhs, (0., CONFIG["horizon"]), initial,
                        method="DOP853", rtol=rtol, atol=atol,
                        events=event, dense_output=True)
        elapsed = time.monotonic() - start
        crossing = float(sol.t_events[0][0]) if len(sol.t_events[0]) else None
        final_t = crossing if crossing is not None else float(sol.t[-1])
        final = sol.sol(final_t)
        record = dict(success=bool(sol.success), message=sol.message,
                      reached_target=crossing is not None, fit_time=final_t,
                      integrated_to=float(sol.t[-1]), solver_seconds=elapsed,
                      nfev=int(sol.nfev), accepted_steps=len(sol.t)-1,
                      training_output=output(final).tolist(),
                      training_rms=rms(output(final)-LABELS),
                      maximum_final_state=float(np.max(np.abs(final))))
        return sol, final, record
    except (TimeoutError, FloatingPointError, ValueError) as exc:
        return None, last[1], dict(success=False, reached_target=False,
                                error=repr(exc), last_rhs_time=last[0],
                                solver_seconds=time.monotonic()-start,
                                last_state_is_accepted=False)


def tail_rms(values, J):
    coeff = np.fft.fft(values) / len(values)
    keep = np.zeros(len(values), bool)
    keep[:J+1] = True
    if J:
        keep[-J:] = True
    return float(np.sqrt(np.sum(np.abs(coeff[~keep]) ** 2)))


def export_fourier_model(folder, coefficients, physical_time):
    coefficients = np.asarray(coefficients)
    write_json(folder / "fourier_model.json", dict(
        convention="f(theta)=constant+sum_k[cosine[k-1]*cos(k*theta)+sine[k-1]*sin(k*theta)]",
        angle_unit="radians", physical_time=physical_time,
        constant=float(coefficients[0]),
        cosine=(2*coefficients[1::2]).tolist(), sine=(2*coefficients[2::2]).tolist()))


def save_solution(folder, model, sol, final, record, initial):
    values = model.predict(final, CIRCLE.T)
    record.update(circle_rms=rms(values), circle_tail_rms_J8=tail_rms(values, 8),
                  state_count=len(initial))
    if sol is not None:
        times = np.unique(np.r_[np.linspace(0, sol.t[-1], 81), record["fit_time"]])
        states = sol.sol(times)
        outputs = np.array([model.predict(states[:, i], U.T) for i in range(len(times))])
        np.savez_compressed(folder / "trajectory.npz", times=times,
                            training_output=outputs, states=states)
        with (folder / "solution.pkl").open("wb") as handle:
            pickle.dump(sol, handle)
    np.savez_compressed(folder / "final.npz", theta=THETA, circle=values,
                        state=final, initial_state=initial)
    write_json(folder / "result.json", record)


def references(out, refined=False):
    initialization = initialize(CONFIG["width"], CONFIG["seed"])
    rtol, atol = (1e-9, 1e-11) if refined else (CONFIG["rtol"], CONFIG["atol"])
    for name, cls in [("dense", DenseReference), ("parent_P1", PopulationReference)]:
        folder = out / (name + ("_refined" if refined else ""))
        folder.mkdir()
        model = cls(U.T, LABELS, initialization)
        initial = model.initial.copy()
        sol, final, record = fit(model.rhs, initial, lambda z: model.predict(z, U.T),
                                 rtol=rtol, atol=atol, stop_at_target=False)
        record.update(source_hashes=hashes(), rtol=rtol, atol=atol)
        save_solution(folder, model, sol, final, record, initial)
        print(json.dumps({"cell": folder.name, **record}), flush=True)


def scalar_cell(out, K, *, refined=False, J=8):
    from scalar_fourier_engine import ScalarFourierSystem
    folder = out / (f"scalar_K{K}" + ("_refined" if refined else "") +
                    (f"_J{J}" if J != 8 else ""))
    folder.mkdir()
    start = time.monotonic()
    try:
        system = ScalarFourierSystem(U, LABELS, K, J=J,
                                     max_patterns=CONFIG["max_patterns"],
                                     max_terms=CONFIG["max_terms"],
                                     compile_seconds=CONFIG["compiler_wall_seconds"],
                                     include_energy=False)
    except Exception as exc:
        record = dict(phase="compilation", success=False, error=repr(exc),
                      compile_seconds=time.monotonic()-start, source_hashes=hashes())
        if hasattr(exc, "stats"):
            record["statistics"] = exc.stats
        write_json(folder / "result.json", record)
        print(json.dumps({"cell": folder.name, **record}), flush=True)
        return False, False
    compile_seconds = time.monotonic()-start
    init = initialize(CONFIG["width"], CONFIG["seed"])
    start = time.monotonic()
    z0 = system.initialize(init.w, init.W20, init.W30, init.c,
                           quadrature=512 if refined else CONFIG["quadrature"])
    initialization_seconds = time.monotonic()-start
    rtol, atol = (1e-9, 1e-11) if refined else (CONFIG["rtol"], CONFIG["atol"])
    sol, final, record = fit(system.rhs, z0, system.training_output,
                             rtol=rtol, atol=atol, stop_at_target=True)
    record.update(phase="integration", K=K, J=J, statistics=system.statistics(),
                  source_hashes=hashes(), compile_seconds=compile_seconds,
                  initialization_seconds=initialization_seconds, rtol=rtol, atol=atol,
                  quadrature=512 if refined else CONFIG["quadrature"], state_count=len(z0))
    values = system.circle_output(final, THETA)
    fourier_train = system.circle_output(final, ANGLES)
    record["fourier_training_output"] = fourier_train.tolist()
    record["fourier_training_rms"] = rms(fourier_train-LABELS)
    record["fourier_vs_training_readout_rms"] = rms(fourier_train-system.training_output(final))
    np.savez_compressed(folder / "final.npz", theta=THETA, circle=values,
                        state=final, initial_state=z0,
                        fourier_coefficients=system.fourier_coefficients(final))
    if sol is not None:
        export_fourier_model(folder, system.fourier_coefficients(final), record["fit_time"])
        times = np.linspace(0, sol.t[-1], 81)
        states = sol.sol(times)
        outputs = np.array([system.training_output(states[:, i]) for i in range(len(times))])
        np.savez_compressed(folder / "trajectory.npz", times=times,
                            training_output=outputs, states=states)
    with (folder / "runtime.pkl").open("wb") as handle:
        pickle.dump(system, handle)
    write_json(folder / "result.json", record)
    print(json.dumps({"cell": folder.name, **record}), flush=True)
    return True, bool(record.get("reached_target"))


def analyze(out):
    for name in ("dense", "parent_P1"):
        status = json.loads((out / name / "result.json").read_text())
        if not (status.get("success") and status.get("reached_target")):
            raise RuntimeError(f"Cannot label fitted comparisons: {name} did not fit successfully")
    initialization = initialize(CONFIG["width"], CONFIG["seed"])
    dense = DenseReference(U.T, LABELS, initialization)
    parent = PopulationReference(U.T, LABELS, initialization)
    dense_circle = np.load(out / "dense/final.npz")["circle"]
    parent_circle = np.load(out / "parent_P1/final.npz")["circle"]
    with (out / "dense/solution.pkl").open("rb") as handle:
        dense_sol = pickle.load(handle)
    with (out / "parent_P1/solution.pkl").open("rb") as handle:
        parent_sol = pickle.load(handle)
    scores = {"parent_vs_dense_own_fit_rms": rms(parent_circle-dense_circle), "cells": {}}
    for folder in sorted(out.glob("scalar_K*")):
        result_path = folder / "result.json"
        result = json.loads(result_path.read_text())
        if not (folder / "final.npz").exists() or "fit_time" not in result:
            scores["cells"][folder.name] = result
            continue
        values = np.load(folder / "final.npz")["circle"]
        t = result["fit_time"]
        if not (dense_sol.t[0] <= t <= dense_sol.t[-1] and
                parent_sol.t[0] <= t <= parent_sol.t[-1]):
            raise RuntimeError(f"{folder.name} comparison would extrapolate a reference solution")
        dense_same = dense.predict(dense_sol.sol(t), CIRCLE.T)
        parent_same = parent.predict(parent_sol.sol(t), CIRCLE.T)
        result.update(circle_vs_dense_rms=rms(values-dense_circle),
                      circle_vs_dense_max=float(np.max(np.abs(values-dense_circle))),
                      circle_vs_dense_relative_rms=rms(values-dense_circle)/rms(dense_circle),
                      circle_vs_parent_rms=rms(values-parent_circle),
                      same_time_vs_dense_rms=rms(values-dense_same),
                      same_time_vs_parent_rms=rms(values-parent_same))
        np.savez_compressed(folder / "matched_reference.npz", theta=THETA,
                            dense=dense_same, parent=parent_same)
        scores["cells"][folder.name] = result
    for name in ("dense", "parent_P1"):
        refined = out / f"{name}_refined/final.npz"
        if refined.exists():
            scores[f"{name}_refinement_circle_rms"] = rms(
                np.load(refined)["circle"]-np.load(out / name / "final.npz")["circle"])
    for folder in out.glob("scalar_K*_refined"):
        base = out / folder.name.removesuffix("_refined") / "final.npz"
        if (folder / "final.npz").exists() and base.exists():
            scores[folder.name+"_prediction_change_rms"] = rms(
                np.load(folder / "final.npz")["circle"]-np.load(base)["circle"])
    write_json(out / "scores.json", scores)
    print(json.dumps(scores, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--phase", choices=["references", "scalars", "refine", "analyze"], required=True)
    parser.add_argument("--cutoff", type=int)
    parser.add_argument("--bandwidth", type=int, default=8)
    args = parser.parse_args()
    out = args.out
    if args.phase == "references":
        out.mkdir(parents=True, exist_ok=False)
        write_json(out / "config.json", dict(CONFIG, command=sys.argv, cwd=os.getcwd(),
                    python=sys.version, numpy=np.__version__, scipy=scipy.__version__,
                    platform=platform.platform(), source_hashes=hashes()))
        references(out)
    elif args.phase == "scalars":
        for K in [args.cutoff] if args.cutoff is not None else CONFIG["cutoffs"]:
            compiled, fitted = scalar_cell(out, K, J=args.bandwidth)
            if not compiled:
                break
    elif args.phase == "refine":
        references(out, refined=True)
        if args.cutoff is not None:
            scalar_cell(out, args.cutoff, refined=True)
    elif args.phase == "analyze":
        analyze(out)


if __name__ == "__main__":
    main()
