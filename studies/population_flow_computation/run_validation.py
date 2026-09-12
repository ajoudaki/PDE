"""Bounded validation driver; all runs are exploratory numerical source processes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import time

import numpy as np
import scipy

from directional_solver import DirectionalSolver, NumericalFailure


def digest(path):
    checksum = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""):
            checksum.update(chunk)
    return checksum.hexdigest()


def law(case, specification):
    if case["law"] == "reference":
        return [[1., 0.], [0., 1.]], [.5, .5], [1., -1.]
    a, b, p = (specification["arc_law"][key] for key in ("a", "b", "p"))
    cells = case["arc_cells"]
    v = -1 + (2 * np.arange(cells) + 1) / cells
    cosine, sine = np.cos(a*v), np.sin(a*v)
    directions = np.vstack((np.column_stack((cosine, sine)), np.column_stack((-sine, cosine))))
    labels = np.r_[1-b*(1+v)/2, -1+b*(1+v)/2]
    weights = np.r_[np.full(cells, p/cells), np.full(cells, (1-p)/cells)]
    return directions.tolist(), weights.tolist(), labels.tolist()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--case", action="append", help="listed case name; default all")
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    root = study.parents[1]
    generated = root / "data/generated/population_flow_computation"
    if not args.output.resolve().is_relative_to(generated.resolve()):
        parser.error("output must be study-owned generated data")
    args.output.mkdir(parents=True, exist_ok=False)
    specification_path = study / "validation_cases.json"
    specification = json.loads(specification_path.read_text())
    cases = specification["case_definitions"]
    if args.case:
        requested = set(args.case)
        if requested - {c["name"] for c in cases}:
            parser.error("unknown case")
        cases = [c for c in cases if c["name"] in requested]
    angles = np.arange(specification["circle_points"])*2*np.pi/specification["circle_points"]
    circle = np.column_stack((np.cos(angles), np.sin(angles)))
    observed_angles = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4])
    observed = np.column_stack((np.cos(observed_angles), np.sin(observed_angles)))
    source_paths = [Path(__file__), study/"directional_solver.py", specification_path, study/"validation_plan.md"]
    provenance = {
        "source_hashes": {str(p.relative_to(root)): digest(p) for p in source_paths},
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        "platform": platform.platform(), "cwd": os.getcwd(), "specification": specification,
        "threads": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
    }
    (args.output/"provenance.json").write_text(json.dumps(provenance, indent=2)+"\n")
    started = time.perf_counter()
    outcomes = []
    for case in cases:
        if time.perf_counter()-started > 540:
            outcomes.append({"name": case["name"], "status": "not_run_wall_budget"})
            (args.output/"outcomes.json").write_text(json.dumps(outcomes, indent=2)+"\n")
            break
        case_dir = args.output/case["name"]
        case_dir.mkdir()
        directions, weights, labels = law(case, specification)
        config = {k: case[k] for k in ("representatives", "h", "noise", "precision")}
        config.update(seed=specification["seed"], directions=directions, weights=weights, labels=labels)
        (case_dir/"config.json").write_text(json.dumps(config, indent=2)+"\n")
        solver = DirectionalSolver(config)
        case_started = time.perf_counter()
        status, failure = "completed", None
        times, predictions = [0.], [solver.predict(circle, 16)]
        try:
            for step in range(case["steps"]):
                if time.perf_counter()-started > 570:
                    raise NumericalFailure("preregistered wall budget reached")
                solver.step()
                # Eight fixed output intervals; no full history diagnostic each step.
                if (step+1) % max(1, case["steps"]//8) == 0:
                    times.append(solver.time)
                    predictions.append(solver.predict(circle, 16))
            prediction_32 = solver.predict(circle, 32)
            pair = solver.paired_hidden_draws(observed, draws=4, seed=specification["query_seed"])
            moments = {
                "hidden_motion_squared_upper": pair["hidden_motion_squared"].tolist(),
                "hidden_motion_squared_lower": np.mean((pair["lower_current_H"]-pair["lower_initial_H"])**2, axis=0).tolist(),
                "cross_hidden_moment_upper": pair["cross_hidden_moment"].tolist(),
                "upper_D_rms": np.sqrt(np.mean(pair["upper_D"]**2, axis=(0,1))).tolist(),
                "lower_Q_rms": np.sqrt(np.mean(pair["lower_Q"]**2, axis=(0,1))).tolist(),
                "query_sampling_draws": 4,
                "roundoff_eigenvalue_clips": pair["roundoff_eigenvalue_clips"],
                "reverse_roundoff_eigenvalue_clips": pair["reverse_roundoff_eigenvalue_clips"],
            }
            (case_dir/"joint_moments.json").write_text(json.dumps(moments, indent=2)+"\n")
            np.savez(case_dir/"predictions.npz", times=np.asarray(times), circle=circle,
                     predictions=np.asarray(predictions), final_order32=prediction_32)
            diagnostics = solver.diagnostics(order=32)
            diagnostics["passive_order16_order32_grid_difference"] = float(np.max(np.abs(predictions[-1]-prediction_32)))
            (case_dir/"diagnostics.json").write_text(json.dumps(diagnostics, indent=2)+"\n")
        except (NumericalFailure, FloatingPointError, np.linalg.LinAlgError) as exc:
            status, failure = "failed", str(exc)
        solver.save(case_dir/"final_state.npz")
        checkpoint_hash = digest(case_dir/"final_state.npz")
        result = {"name": case["name"], "status": status, "failure": failure,
                  "completed_steps": solver.steps, "calls": solver.calls, "physical_time": solver.time,
                  "wall_seconds": time.perf_counter()-case_started,
                  "peak_process_memory_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  "checkpoint_bytes": (case_dir/"final_state.npz").stat().st_size,
                  "checkpoint_sha256": checkpoint_hash}
        (case_dir/"outcome.json").write_text(json.dumps(result, indent=2)+"\n")
        outcomes.append(result)
        (args.output/"outcomes.json").write_text(json.dumps(outcomes, indent=2)+"\n")
        print(json.dumps(result), flush=True)
        if case["name"] == "short_reference" and status != "completed":
            break
    return 0 if all(r["status"] == "completed" for r in outcomes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
