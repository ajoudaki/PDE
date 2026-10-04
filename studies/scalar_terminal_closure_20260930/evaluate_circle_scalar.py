"""Export and evaluate the 729-number circle terminal model, without training.

Evaluation depends only on NumPy, SciPy, threadpoolctl, the four model arrays,
elapsed duration, and caller-supplied angles. It never imports the producer.
Export and check are separate commands that may read completed run artifacts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from threadpoolctl import threadpool_info, threadpool_limits


SHAPES = {"matrix": (8, 8), "drift": (8,), "fourier": (64, 10),
          "initial_state": (17,)}
RTOL, ATOL = 1e-10, 1e-12


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        stream.write(json.dumps(value, indent=2, allow_nan=False) + "\n")


def write_npz(path, arrays):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        np.savez_compressed(stream, **arrays)


def validate_model(model):
    if set(model) != set(SHAPES):
        raise ValueError(f"Model must contain exactly {sorted(SHAPES)}")
    for key, shape in SHAPES.items():
        value = np.asarray(model[key])
        if value.shape != shape or value.dtype != np.dtype("float64"):
            raise ValueError(f"{key} must be float64 with shape {shape}")
        if not np.isfinite(value).all():
            raise ValueError(f"{key} contains nonfinite values")
    if sum(np.asarray(value).size for value in model.values()) != 729:
        raise ValueError("Model must have exactly 729 numeric entries")


def load_model(path):
    with np.load(path, allow_pickle=False) as source:
        # Inspect keys before loading arrays: population handoffs are rejected.
        if set(source.files) != set(SHAPES):
            raise ValueError("Not a standalone four-array scalar model")
        model = {key: source[key].copy() for key in SHAPES}
    validate_model(model)
    return model


def export_case(run, case, output, provenance=None):
    """Export the selected completed case's fixed primary (MSE 0.01) handoff."""
    run = Path(run).resolve()
    output = Path(output).resolve()
    if not case or Path(case).name != case or case in (".", ".."):
        raise ValueError("case must be a single directory name")
    snapshot = (run / "results.json").read_bytes()
    records = json.loads(snapshot)["results"]
    matches = [item for item in records if item["case"] == case]
    if len(matches) != 1:
        raise ValueError("Case is not uniquely present among completed results")
    selected = matches[0]["selected"]
    if selected not in ("fine", "refined"):
        raise ValueError("Expected the producer's selected fine/refined run")
    directory = run / case / selected
    summary_path = directory / "summary.json"
    summary = json.loads(summary_path.read_text())
    if summary["case"] != case:
        raise ValueError("Selected summary does not match the requested case")
    primary = [item for item in summary["handoffs"] if item["threshold"] == 0.01]
    if len(primary) != 1:
        raise ValueError("Selected case lacks exactly one primary handoff")
    handoff = directory / "handoff_0.01.npz"
    with np.load(handoff, allow_pickle=False) as source:
        # NPZ is lazy: no neuronwise or query-panel arrays are loaded here.
        residual = np.asarray(source["residual"], dtype=np.float64)
        if residual.shape != (8,):
            raise ValueError("Expected eight training residuals")
        model = {key: np.asarray(source[key], dtype=np.float64).copy()
                 for key in ("matrix", "drift", "fourier")}
        model["initial_state"] = np.concatenate((residual, np.zeros(9)))
        handoff_time = float(source["time"])
    validate_model(model)
    endpoint_time = float(summary["final_time"])
    if (not np.isfinite([handoff_time, endpoint_time]).all()
            or endpoint_time < handoff_time
            or handoff_time != float(primary[0]["time"])):
        raise ValueError("Inconsistent handoff/endpoint metadata")
    if provenance is not None and Path(provenance).resolve() == output:
        raise ValueError("Model and provenance paths must differ")
    write_npz(output, model)
    metadata = dict(
        format="circle-terminal-729-v1", case=case, selected=selected,
        primary_threshold=0.01, numeric_entries=729, moving_entries=17,
        fixed_entries=712, handoff_global_time=handoff_time,
        endpoint_global_time=endpoint_time,
        recorded_elapsed_duration=endpoint_time - handoff_time,
        model_sha256=digest(output), source_handoff=str(handoff),
        source_handoff_sha256=digest(handoff), source_summary=str(summary_path),
        source_summary_sha256=digest(summary_path),
        results_snapshot_sha256=hashlib.sha256(snapshot).hexdigest(),
        evaluator_sha256=digest(__file__),
        limitation="Terminal model only; full q1 training produced the handoff.")
    if provenance is not None:
        write_json(provenance, metadata)
    return metadata


def evaluate_model(model, duration, angles, samples=201, deadline=None):
    """Return an elapsed-time residual curve and final Fourier circle outputs.

    State order is (r[8], integral(r)[8], integral(norm(r))[1]). Its initial
    state can also be a saved terminal state, retaining the same Fourier data.
    No path, global training time, labels, or population arrays enter this API.
    """
    validate_model(model)
    duration = float(duration)
    angles = np.asarray(angles, dtype=np.float64)
    if not np.isfinite(duration) or duration < 0:
        raise ValueError("duration must be finite and nonnegative")
    if angles.ndim != 1 or not angles.size or not np.isfinite(angles).all():
        raise ValueError("angles must be a nonempty finite vector in radians")
    if not isinstance(samples, (int, np.integer)) or samples < 2:
        raise ValueError("samples must be an integer at least two")

    def check_deadline():
        if deadline is not None and time.perf_counter() >= deadline:
            raise TimeoutError("Scalar evaluation exceeded its wall-time budget")

    check_deadline()
    matrix, drift = model["matrix"], model["drift"]

    def rhs(_elapsed, state):
        check_deadline()
        residual = state[:8]
        norm = np.linalg.norm(residual)
        return np.concatenate((-matrix @ residual + norm * drift, residual, [norm]))

    if duration == 0:
        elapsed = np.zeros(1)
        state = model["initial_state"][None, :].copy()
        nfev = 0
    else:
        elapsed = np.linspace(0, duration, samples)
        solved = solve_ivp(rhs, (0, duration), model["initial_state"],
                           method="DOP853", t_eval=elapsed, rtol=RTOL, atol=ATOL)
        if not solved.success or not np.isfinite(solved.y).all():
            raise RuntimeError("Scalar integration failed: " + solved.message)
        state, nfev = solved.y.T, solved.nfev
    weights = np.concatenate(([1.], -state[-1, 8:16], [state[-1, 16]]))
    frequencies = np.arange(1, 64, 2)
    phase = angles[:, None] * frequencies[None, :]
    basis = np.concatenate((np.cos(phase), np.sin(phase)), axis=1)
    circle_output = basis @ (model["fourier"] @ weights)
    residual_loss = np.mean(state[:, :8] ** 2, axis=1)
    check_deadline()
    if not np.isfinite(circle_output).all() or not np.isfinite(residual_loss).all():
        raise FloatingPointError("Nonfinite scalar output")
    return dict(elapsed=elapsed, state=state, residual_loss=residual_loss,
                angles=angles.copy(), circle_output=circle_output), nfev


def check_export(run, case, output_dir, deadline):
    """One completed-case consistency check; never reruns full training."""
    start = time.perf_counter()
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=False)
    shutil.copyfile(__file__, output_dir / "evaluate_circle_scalar.py")
    metadata = export_case(run, case, output_dir / "model.npz",
                           output_dir / "model.provenance.json")
    curves = Path(metadata["source_handoff"]).parent / "curves.npz"
    with np.load(curves, allow_pickle=False) as source:
        angles = source["angles"].copy()
        reference_state = source["scalar_state_0.01"].copy()
        reference_loss = source["scalar_loss_0.01"].copy()
        reference_output = source["scalar_output_0.01"].copy()
        reference_times = source["scalar_times_0.01"].copy()
    duration = float(reference_times[-1] - reference_times[0])
    if duration != metadata["recorded_elapsed_duration"]:
        raise ValueError("Raw scalar duration disagrees with completed summary")
    np.save(output_dir / "angles.npy", angles, allow_pickle=False)
    # Run the copied file as an independent program in the export directory.
    # Its evaluate command receives no source-run path and no provenance JSON.
    command = [sys.executable, "evaluate_circle_scalar.py", "evaluate",
               "--model", "model.npz", "--duration", repr(duration),
               "--angles", "angles.npy", "--samples", str(len(reference_times)),
               "--output", "evaluation.npz"]
    remaining = deadline - time.perf_counter()
    if remaining <= 0:
        raise TimeoutError("Portable check exhausted its wall-time budget")
    environment = os.environ.copy()
    for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                 "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
        environment[name] = "2"
    child = subprocess.run(command, cwd=output_dir, env=environment,
                           capture_output=True, text=True, timeout=remaining,
                           check=True)
    with np.load(output_dir / "evaluation.npz", allow_pickle=False) as result:
        errors = dict(
            endpoint_state_max=float(np.max(np.abs(result["state"][-1] - reference_state[-1]))),
            endpoint_residual_loss_abs=float(abs(result["residual_loss"][-1] - reference_loss[-1])),
            endpoint_circle_max=float(np.max(np.abs(result["circle_output"] - reference_output))),
            curve_state_max=float(np.max(np.abs(result["state"] - reference_state))),
            curve_residual_loss_max=float(np.max(np.abs(result["residual_loss"] - reference_loss))),
            elapsed_grid_max=float(np.max(np.abs(result["elapsed"] - (reference_times-reference_times[0])))))
    model = load_model(output_dir / "model.npz")
    zero, _ = evaluate_model(model, 0, angles[:7], deadline=deadline)
    zero_state_error = float(np.max(np.abs(zero["state"][0] - model["initial_state"])))
    try:
        load_model(metadata["source_handoff"])
    except ValueError:
        rejects_population_handoff = True
    else:
        rejects_population_handoff = False
    endpoint_keys = ("endpoint_state_max", "endpoint_residual_loss_abs",
                     "endpoint_circle_max")
    endpoint_passed = all(errors[key] <= 1e-8 for key in endpoint_keys)
    report = dict(
        case=case, selected=metadata["selected"], passed=(
            endpoint_passed and errors["elapsed_grid_max"] <= 1e-8
            and zero_state_error == 0
            and rejects_population_handoff), tolerance=1e-8,
        acceptance_scope="Recorded endpoint; full-curve errors are diagnostics",
        endpoint_passed=endpoint_passed,
        numeric_entries=sum(a.size for a in model.values()),
        model_shapes={key: list(a.shape) for key, a in model.items()},
        errors=errors, zero_duration_state_max=zero_state_error,
        rejects_population_handoff=rejects_population_handoff,
        elapsed_duration=duration, angle_count=len(angles),
        scalar_time_count=len(reference_times), child_command=command,
        child_stdout=child.stdout.strip(), child_stderr=child.stderr.strip(),
        python=sys.version, numpy=np.__version__, scipy=scipy.__version__,
        threads=threadpool_info(), wall_seconds=time.perf_counter()-start,
        budget_seconds=60, maximum_threads=2,
        source_curves=str(curves.resolve()), source_curves_sha256=digest(curves),
        evaluator_sha256=digest(__file__), model_sha256=digest(output_dir / "model.npz"),
        evaluation_sha256=digest(output_dir / "evaluation.npz"))
    write_json(output_dir / "check.json", report)
    if not report["passed"]:
        raise AssertionError("Portable model consistency check failed; see check.json")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export", help="Export a completed selected primary handoff")
    export.add_argument("--run", type=Path, required=True)
    export.add_argument("--case", required=True)
    export.add_argument("--output", type=Path, required=True)
    export.add_argument("--provenance", type=Path)
    evaluate = commands.add_parser("evaluate", help="Use only a standalone model and angles")
    evaluate.add_argument("--model", type=Path, required=True)
    evaluate.add_argument("--duration", type=float, required=True)
    evaluate.add_argument("--angles", type=Path, required=True, help="One-dimensional NPY, radians")
    evaluate.add_argument("--samples", type=int, default=201)
    evaluate.add_argument("--output", type=Path, required=True)
    check = commands.add_parser("check", help="Export and independently evaluate one completed case")
    check.add_argument("--run", type=Path, required=True)
    check.add_argument("--case", required=True)
    check.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    deadline = time.perf_counter() + 60
    with threadpool_limits(limits=2):
        if args.command == "export":
            report = export_case(args.run, args.case, args.output, args.provenance)
        elif args.command == "evaluate":
            angles = np.load(args.angles, allow_pickle=False)
            result, nfev = evaluate_model(load_model(args.model), args.duration,
                                           angles, args.samples, deadline)
            write_npz(args.output, result)
            report = dict(numeric_entries=729, duration=args.duration,
                          final_residual_loss=float(result["residual_loss"][-1]),
                          angle_count=len(angles), scalar_nfev=nfev,
                          model_sha256=digest(args.model), output_sha256=digest(args.output))
        else:
            report = check_export(args.run, args.case, args.output_dir, deadline)
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
