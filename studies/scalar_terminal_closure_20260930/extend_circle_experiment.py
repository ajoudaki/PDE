"""Supplemental continuation of frozen circle runs, with unchanged handoffs.

Training requires a complete original results.json. --check performs only a
discarded one-step resume check and zero-duration endpoint reconstruction.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import shutil
import sys
import time

import numpy as np
from threadpoolctl import threadpool_info, threadpool_limits

HERE = Path(__file__).resolve().parent
GENERATED = HERE.parents[1] / "data" / "generated" / HERE.name
PRODUCER_SHA256 = "f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba"
CASES = ("two_outliers_alternating", "quadrant_alternating", "quadrant_pairs",
         "quadrant_center_edges", "equal_mixed_odd")
RAM_LIMIT = 4 * 1024**3


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def write_json(path, value):
    temporary = Path(str(path) + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def producer(run):
    path = run / "circle_terminal_experiment.py"
    if digest(path) != PRODUCER_SHA256:
        raise ValueError("Frozen producer hash does not match the authorized dependency")
    spec = importlib.util.spec_from_file_location("frozen_circle_producer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Guard:
    def __init__(self, seconds, cpu_seconds=None):
        self.start = time.perf_counter()
        self.deadline = self.start + seconds
        self.cpu_start = time.process_time()
        self.cpu_limit = cpu_seconds
        self.high_water_rss = 0

    def __call__(self):
        self.high_water_rss = max(self.high_water_rss,
                                 resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)
        if self.high_water_rss > RAM_LIMIT:
            raise MemoryError("Process high-water RSS exceeded the 4 GiB bound")
        if time.perf_counter() >= self.deadline:
            raise TimeoutError("Supplemental wall-time budget exhausted")
        if self.cpu_limit is not None and time.process_time()-self.cpu_start >= self.cpu_limit:
            raise TimeoutError("Validation CPU-time budget exhausted")


def finite_states(dense, q1):
    if not all(np.isfinite(block).all() for block in dense + q1):
        raise FloatingPointError("Nonfinite proposed full state")
    if q1[4].shape != (1,) or q1[4][0] <= 0:
        raise FloatingPointError("Invalid q1 activity clock")


def load_states(path):
    with np.load(path, allow_pickle=False) as saved:
        dense = tuple(saved[key].copy() for key in ("dense_a", "dense_w", "dense_readout"))
        q1 = tuple(saved[key].copy() for key in ("q1_a", "q1_readout", "values", "keys", "clock"))
    finite_states(dense, q1)
    return dense, q1


def save_states(path, dense, q1):
    np.savez_compressed(path, dense_a=dense[0], dense_w=dense[1], dense_readout=dense[2],
                        q1_a=q1[0], q1_readout=q1[1], values=q1[2], keys=q1[3], clock=q1[4])


def task_arrays(task):
    inputs = np.asarray(task["normalized_inputs_u"], dtype=float)
    if inputs.shape == (8, 2):
        inputs = inputs.T
    labels = np.asarray(task["labels"], dtype=float)
    if inputs.shape != (2, 8) or labels.shape != (8,):
        raise ValueError(f"Unexpected task input/label shapes: {inputs.shape}, {labels.shape}")
    return inputs, labels


def advance_pair(p, dense, q1, w0, inputs, labels, step, guard):
    def rhs(state, kind):
        guard()
        return p.velocity(state, kind, w0, inputs, labels)[0]
    new_dense = p.rk4(dense, rhs(dense, "dense"), lambda s: rhs(s, "dense"), step)
    new_q1 = p.rk4(q1, rhs(q1, "q1"), lambda s: rhs(s, "q1"), step)
    finite_states(new_dense, new_q1)
    guard()
    return new_dense, new_q1


def guarded_scalar(p, matrix, drift, residual, times, guard):
    m = len(residual)
    initial = np.r_[residual, np.zeros(m+1)]
    if times[-1] == times[0]:
        return initial[None, :], 0
    def rhs(t, state):
        guard()
        r = state[:m]
        norm = np.linalg.norm(r)
        return np.concatenate((-matrix @ r + norm * drift, r, [norm]))
    guard()
    solved = p.solve_ivp(rhs, (times[0], times[-1]), initial, method="DOP853",
                         t_eval=times, rtol=1e-10, atol=1e-12)
    if not solved.success or not np.isfinite(solved.y).all():
        raise RuntimeError("Scalar continuation failed: " + solved.message)
    return solved.y.T, solved.nfev


def finalize(p, dense, q1, w0, curves, old_summary, directory, guard, started):
    """Reevaluate endpoints and the original frozen scalar ODEs; no new handoff."""
    guard()
    queries = p.circle_inputs(curves["angles"])
    dense_output = p.predict(dense, "dense", w0, queries)
    guard()
    q1_output = p.predict(q1, "q1", w0, queries)
    curves.update(dense_output=dense_output, q1_output=q1_output)
    labels, times = curves["labels"], curves["times"]
    m = len(labels)
    query_basis = p.fourier_basis(curves["angles"])
    train_basis = p.fourier_basis(curves["train_angles"])
    summaries = []
    for old_handoff in old_summary["handoffs"]:
        guard()
        item = copy.deepcopy(old_handoff)
        tag = f"{item['threshold']:g}"
        with np.load(directory / f"handoff_{tag}.npz", allow_pickle=False) as stored:
            handoff = {key: stored[key] for key in ("matrix", "drift", "residual", "fourier",
                "query_f", "query_c", "query_b", "time")}
        mask = times >= float(handoff["time"])
        scalar, evaluations = guarded_scalar(p, handoff["matrix"], handoff["drift"],
                                             handoff["residual"], times[mask], guard)
        integrated, norm_integral = scalar[-1, m:2*m], scalar[-1, -1]
        weights = np.r_[1., -integrated, norm_integral]
        coefficients = handoff["fourier"] @ weights
        scalar_output, train_output = query_basis @ coefficients, train_basis @ coefficients
        direct = handoff["query_f"] - handoff["query_c"] @ integrated + handoff["query_b"] * norm_integral
        exact_train = labels + handoff["residual"] - handoff["matrix"] @ integrated + handoff["drift"] * norm_integral
        scalar_loss = np.mean(scalar[:, :m]**2, axis=1)
        curves.update({f"scalar_output_{tag}": scalar_output,
            f"scalar_direct_output_{tag}": direct, f"static_output_{tag}": handoff["query_f"],
            f"scalar_times_{tag}": times[mask], f"scalar_loss_{tag}": scalar_loss,
            f"scalar_state_{tag}": scalar})
        away = np.abs(dense_output) >= .05
        signs = np.sign(scalar_output) != np.sign(dense_output)
        item.update(scalar_vs_dense_rms=p.rms(scalar_output-dense_output),
            scalar_vs_dense_max=float(np.max(np.abs(scalar_output-dense_output))),
            scalar_vs_q1_rms=p.rms(scalar_output-q1_output),
            scalar_vs_q1_max=float(np.max(np.abs(scalar_output-q1_output))),
            direct_scalar_vs_q1_rms=p.rms(direct-q1_output),
            fourier_output_error_rms=p.rms(scalar_output-direct),
            static_vs_q1_rms=p.rms(handoff["query_f"]-q1_output),
            sign_disagreement=float(np.mean(signs)),
            sign_disagreement_away=float(np.mean(signs[away])) if np.any(away) else None,
            dense_away_fraction=float(np.mean(away)), scalar_final_loss=float(scalar_loss[-1]),
            fourier_predictor_train_mse=p.rms(train_output-labels)**2,
            fourier_train_consistency_max=float(np.max(np.abs(train_output-labels-scalar[-1, :m]))),
            exact_train_observer_consistency_max=float(np.max(np.abs(exact_train-labels-scalar[-1, :m]))),
            max_loss_error_vs_q1=float(np.max(np.abs(scalar_loss-curves["q1_loss"][mask]))),
            scalar_final_residual=scalar[-1, :m].tolist(), scalar_nfev=evaluations)
        summaries.append(item)
    guard()
    if not all(np.isfinite(value).all() for value in curves.values()):
        raise FloatingPointError("Nonfinite endpoint/scalar output")
    np.savez_compressed(directory / "curves.npz", **curves)
    save_states(directory / "endpoint_states.npz", dense, q1)
    summary = copy.deepcopy(old_summary)
    elapsed = time.perf_counter()-started
    summary.update(final_time=float(times[-1]), dense_final_loss=float(curves["dense_loss"][-1]),
        q1_final_loss=float(curves["q1_loss"][-1]),
        fitted=bool(max(curves["dense_loss"][-1], curves["q1_loss"][-1]) <= 1e-6),
        q1_vs_dense_rms=p.rms(q1_output-dense_output),
        q1_vs_dense_max=float(np.max(np.abs(q1_output-dense_output))),
        q1_dense_sign_disagreement=float(np.mean(np.sign(q1_output) != np.sign(dense_output))),
        handoffs=summaries, wall_seconds=old_summary["wall_seconds"]+elapsed,
        extension_wall_seconds=elapsed, original_final_time=old_summary["final_time"],
        peak_rss_bytes=max(old_summary["peak_rss_bytes"], guard.high_water_rss),
        continuation="supplemental_from_saved_endpoint",
        scalar_history="Original frozen ODE reintegrated to the new endpoint at unchanged tolerances")
    write_json(directory / "summary.json", summary)
    return summary


def resume_case(p, source, destination, task, w0, guard, target_time=None):
    destination.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    old = read_json(source / "summary.json")
    with np.load(source / "curves.npz", allow_pickle=False) as saved:
        curves = {key: saved[key] for key in saved.files}
    dense, q1 = load_states(source / "endpoint_states.npz")
    for handoff in old["handoffs"]:
        name = f"handoff_{handoff['threshold']:g}.npz"
        shutil.copy2(source / name, destination / name)
    inputs, labels = task_arrays(task)
    step = float(old["step"])
    if step not in (1/8, 1/16):
        raise ValueError("Supplemental plan permits only the original coarse/fine steps")
    start_time, t = float(curves["times"][-1]), float(curves["times"][-1])
    maximum = 1024. if target_time is None else float(target_time)
    if maximum < t or abs((maximum-t)/step-round((maximum-t)/step)) > 1e-8:
        raise ValueError("Target is not a nonnegative number of the unchanged RK steps")
    times = list(curves["times"])
    dense_loss = list(curves["dense_loss"])
    q1_loss = list(curves["q1_loss"])
    residuals = list(curves["q1_residual"])

    def histories():
        return dict(times=np.asarray(times), dense_loss=np.asarray(dense_loss),
                    q1_loss=np.asarray(q1_loss), q1_residual=np.asarray(residuals))

    try:
        guard()
        initial_dense = p.fields(dense, "dense", w0, inputs, False)["f"]-labels
        initial_q1 = p.fields(q1, "q1", w0, inputs, False)["f"]-labels
        if not (np.allclose(initial_q1, residuals[-1], rtol=1e-10, atol=1e-12)
                and np.isclose(np.mean(initial_dense**2), dense_loss[-1], rtol=1e-9, atol=1e-12)
                and np.isclose(np.mean(initial_q1**2), q1_loss[-1], rtol=1e-9, atol=1e-12)):
            raise ValueError("Saved endpoint states do not reproduce original endpoint losses")
        last_print = time.perf_counter()
        for index in range(1, int(round((maximum-start_time)/step))+1):
            if target_time is None and max(dense_loss[-1], q1_loss[-1]) <= 1e-7:
                break
            proposed_dense, proposed_q1 = advance_pair(p, dense, q1, w0, inputs, labels, step, guard)
            rd = p.fields(proposed_dense, "dense", w0, inputs, False)["f"]-labels
            rq = p.fields(proposed_q1, "q1", w0, inputs, False)["f"]-labels
            ld, lq = float(np.mean(rd**2)), float(np.mean(rq**2))
            if not np.isfinite(ld+lq):
                raise FloatingPointError("Nonfinite loss at proposed step")
            guard()
            dense, q1 = proposed_dense, proposed_q1
            t = start_time + index*step
            times.append(t); dense_loss.append(ld); q1_loss.append(lq); residuals.append(rq.copy())
            if time.perf_counter()-last_print > 25:
                print(f"EXTEND {task['case']} dt={step:g} t={t:g} dense={ld:.3g} q1={lq:.3g}", flush=True)
                last_print = time.perf_counter()
        curves.update(histories())
        return finalize(p, dense, q1, w0, curves, old, destination, guard, started)
    except BaseException as error:
        # The last accepted dense/q1 pair and only valid observed history are retained.
        save_states(destination / "partial_states.npz", dense, q1)
        np.savez_compressed(destination / "partial_trajectory.npz", **histories(),
                            angles=curves["angles"], train_angles=curves["train_angles"], labels=labels)
        write_json(destination / "interruption.json", dict(type=type(error).__name__, message=str(error),
            last_accepted_time=t, original_final_time=start_time, requested_final_time=maximum,
            high_water_rss_bytes=guard.high_water_rss, complete=False))
        raise


def copy_case(source, target, guard):
    target.mkdir()
    hashes = {}
    for resolution in ("coarse", "fine", "refined"):
        directory = source / resolution
        if not (directory / "summary.json").is_file():
            continue
        output = target / resolution
        output.mkdir()
        for name in ("summary.json", "curves.npz", "endpoint_states.npz"):
            guard(); shutil.copy2(directory / name, output / name)
            hashes[str(directory / name)] = digest(directory / name)
        for item in read_json(directory / "summary.json")["handoffs"]:
            name = f"handoff_{item['threshold']:g}.npz"
            guard(); shutil.copy2(directory / name, output / name)
            hashes[str(directory / name)] = digest(directory / name)
    return hashes


def validate(p, run, output, tasks, w0, guard):
    case = CASES[0]
    source = run / case / "fine"
    dense, q1 = load_states(source / "endpoint_states.npz")
    inputs, labels = task_arrays(tasks[case])
    step = read_json(source / "summary.json")["step"]
    resumed = advance_pair(p, dense, q1, w0, inputs, labels, step, guard)
    direct = []
    for state, kind in ((dense, "dense"), (q1, "q1")):
        rhs = lambda s, k=kind: p.velocity(s, k, w0, inputs, labels)[0]
        direct.append(p.rk4(state, rhs(state), rhs, step))
    errors = [float(np.max(np.abs(a-b))) for left, right in zip(resumed, direct) for a, b in zip(left, right)]
    if max(errors) != 0:
        raise AssertionError(errors)
    original_summary = read_json(source / "summary.json")
    summary = resume_case(p, source, output / "zero_duration", tasks[case], w0, guard,
                          original_summary["final_time"])
    with np.load(source / "curves.npz", allow_pickle=False) as original, np.load(
            output / "zero_duration" / "curves.npz", allow_pickle=False) as rebuilt:
        curve_errors = {key: float(np.max(np.abs(original[key]-rebuilt[key]))) for key in original.files}
    if max(curve_errors.values()) > 1e-10:
        raise AssertionError(curve_errors)
    # An expired deadline must leave a reconstructible partial state/history.
    expired = Guard(-1.)
    try:
        resume_case(p, source, output / "interruption_check", tasks[case], w0, expired,
                    original_summary["final_time"])
    except TimeoutError:
        pass
    else:
        raise AssertionError("Expired continuation did not stop")
    retained_dense, retained_q1 = load_states(output / "interruption_check" / "partial_states.npz")
    if not all(np.array_equal(a, b) for left, right in ((dense, retained_dense), (q1, retained_q1))
               for a, b in zip(left, right)):
        raise AssertionError("Interruption changed the accepted state")
    guard()
    report = dict(passed=True, case=case, one_step_max_errors=errors,
                  zero_duration_array_max_errors=curve_errors,
                  saved_state_loss_reconstruction_passed=True, interruption_preserved_state=True,
                  wall_seconds=time.perf_counter()-guard.start,
                  cpu_seconds=time.process_time()-guard.cpu_start,
                  high_water_rss_bytes=guard.high_water_rss, producer_sha256=PRODUCER_SHA256)
    report["input_hashes"] = {str(path): digest(path) for path in source.iterdir()
                              if path.suffix in (".json", ".npz")}
    write_json(output / "checks.json", report)
    print(json.dumps(report, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--budget", type=float, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    run, output = args.run.resolve(), args.output.resolve()
    if not run.is_relative_to(GENERATED) or not output.is_relative_to(GENERATED):
        parser.error("Source and output must remain inside this study's generated namespace")
    if args.budget <= 0:
        parser.error("A positive remaining wall-time budget is required")
    p = producer(run)
    original = read_json(run / "results.json")
    if not args.check and (not original.get("complete") or {r["case"] for r in original["results"]} != set(CASES)):
        parser.error("Extension training requires the complete original five-case campaign")
    unsupported = [item["case"] for item in original["results"]
        if item["selected"] != "fine" and item["refinement"]["passed"] and max(
            item[item["selected"]]["dense_final_loss"], item[item["selected"]]["q1_final_loss"]) > 1e-6]
    if not args.check and unsupported:
        parser.error("Cannot continue a previously failed coarse/fine pair after refined selection: "
                     + ", ".join(unsupported))
    output.mkdir(parents=True, exist_ok=False)
    guard = Guard(args.budget, cpu_seconds=30. if args.check else None)
    tasks = {task["case"]: task for task in read_json(run / "circle_task_inputs.json")["tasks"]}
    with np.load(run / "initialization.npz", allow_pickle=False) as initialization:
        w0 = initialization["w0"].copy()
    files = [Path(__file__), HERE / "CIRCLE_ENDPOINT_EXTENSION_PLAN.md",
             run / "circle_terminal_experiment.py", run / "circle_task_inputs.json",
             run / "initialization.npz", run / "CIRCLE_EXPERIMENT_PLAN.md"]
    with threadpool_limits(limits=2):
        for path in files:
            guard(); shutil.copy2(path, output / path.name)
        shutil.copy2(run / "results.json", output / "original_results.json")
        shutil.copy2(run / "provenance.json", output / "original_provenance.json")
        hashes = {str(path): digest(path) for path in files}
        hashes[str(run / "results.json")] = digest(output / "original_results.json")
        write_json(output / "provenance.json", dict(command=sys.argv, python=sys.version,
            executable=sys.executable, numpy=np.__version__, threads=threadpool_info(),
            original_run=str(run), producer_sha256=PRODUCER_SHA256, source_hashes=hashes,
            budget_seconds=args.budget, caller_responsible_for_cumulative_budget_and_120s_reserve=True,
            supplement="Original models, handoffs, coefficients and tolerances; extra physical time only"))
        if args.check:
            validate(p, run, output, tasks, w0, guard)
            return 0
        results = copy.deepcopy(original["results"])
        eligible = []
        for item in results:
            selected = item[item["selected"]]
            needs_fit = max(selected["dense_final_loss"], selected["q1_final_loss"]) > 1e-6
            item["continuation_status"] = ("eligible_pending" if needs_fit and item["refinement"]["passed"]
                else "unchanged_original_refinement_failed" if needs_fit else "unchanged_original_fitted")
            if item["continuation_status"] == "eligible_pending":
                eligible.append(item["case"])
        package = dict(results=results, complete=False, supplemental=True, original_run=str(run),
                       eligible_cases=eligible, original_complete=True)
        active = None
        copied_cases = []
        try:
            for item in results:
                guard(); hashes.update(copy_case(run / item["case"], output / item["case"], guard))
                copied_cases.append(item["case"])
                write_json(output / "input_artifact_hashes.json", hashes)
            write_json(output / "results.json", package)
            for item in results:
                if item["case"] not in eligible:
                    continue
                active = item["case"]
                guard()
                source, case_dir = run / active, output / active
                pending = case_dir / "continuation_pending"
                coarse = resume_case(p, source / "coarse", pending / "coarse", tasks[active], w0, guard)
                fine = resume_case(p, source / "fine", pending / "fine", tasks[active], w0, guard, coarse["final_time"])
                guard()
                sensitivity = p.refinement(pending / "coarse", pending / "fine")
                # Publish only a complete same-time pair; originals remain separately accessible.
                initial_dir = case_dir / "initial_comparison"
                initial_dir.mkdir()
                for resolution in ("coarse", "fine", "refined"):
                    if (case_dir / resolution).exists():
                        (case_dir / resolution).rename(initial_dir / resolution)
                (pending / "coarse").rename(case_dir / "coarse")
                (pending / "fine").rename(case_dir / "fine")
                pending.rmdir()
                item.update(selected="fine", coarse=coarse, fine=fine, refined=None,
                            refinement=sensitivity, continuation_status="supplemental_completed",
                            original_selected_endpoint=read_json(source / item["selected"] / "summary.json")["final_time"])
                write_json(output / "results.json", package)
                active = None
            package.update(complete=True, wall_seconds=time.perf_counter()-guard.start,
                           high_water_rss_bytes=guard.high_water_rss)
            write_json(output / "results.json", package)
            return 0
        except BaseException as error:
            for item in results:
                if item["case"] == active:
                    item["continuation_status"] = "interrupted_original_comparison_retained"
            package.update(results=[item for item in results if item["case"] in copied_cases],
                           complete=False, wall_seconds=time.perf_counter()-guard.start,
                           high_water_rss_bytes=guard.high_water_rss)
            write_json(output / "results.json", package)
            write_json(output / "failure.json", dict(type=type(error).__name__, message=str(error),
                active_case=active, wall_seconds=time.perf_counter()-guard.start,
                high_water_rss_bytes=guard.high_water_rss))
            raise


if __name__ == "__main__":
    raise SystemExit(main())
