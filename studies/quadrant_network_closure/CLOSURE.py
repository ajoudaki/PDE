"""Frozen quadrant experiment: maintained closure evolution and observations.

Run this file as a worker. It never constructs a finite network, changes the
maintained initializer, or reads another study. All outputs belong to the
caller-specified fresh directory inside this study's generated namespace.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time
import traceback

# The frozen CPU experiment uses one numerical thread per worker.
for _thread_setting in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_setting] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
GENERATED = ROOT / "data/generated/quadrant_network_closure"
sys.path.insert(0, str(ROOT / "code"))
from pde import observable_solver as solver


def _hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _json(path, value):
    temporary = Path(str(path) + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n")
    temporary.replace(path)


def _provenance():
    sources = [Path(__file__), ROOT / "studies/quadrant_network_closure/EXPERIMENT_PLAN.md"]
    sources.extend(ROOT / "code/pde" / name for name in (
        "observable_solver.py", "observable_initialization.py", "observable_arithmetic.py",
        "observable_fixed.py", "observable_words.py"))
    git_head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              text=True, capture_output=True, check=False)
    return {
        "source_sha256": {str(p.relative_to(ROOT)): _hash(p) for p in sources},
        "git_head": git_head.stdout.strip() if git_head.returncode == 0 else None,
        "command": [sys.executable, *sys.argv], "python": platform.python_version(),
        "numpy": np.__version__, "platform": platform.platform(),
        "thread_environment": {key: os.environ.get(key) for key in (
            "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
    }


def _fresh_output(path):
    path = Path(path).resolve()
    if not path.is_relative_to(GENERATED.resolve()):
        raise ValueError("outputs must stay in data/generated/quadrant_network_closure")
    path.mkdir(parents=True, exist_ok=False)
    return path


def _inputs(path):
    with np.load(path, allow_pickle=False) as archive:
        names = ("train_u", "labels", "panel_u", "panel_theta", "dense_u", "dense_theta", "times")
        data = {name: np.asarray(archive[name], dtype=np.float64).copy() for name in names}
    if any(not np.all(np.isfinite(value)) for value in data.values()):
        raise ValueError("nonfinite experiment inputs")
    if data["train_u"].shape != (16, 2) or data["labels"].shape != (16,):
        raise ValueError("the frozen training law has 16 two-dimensional inputs")
    angles = np.deg2rad(np.concatenate([np.linspace(a, b, 4) for a, b in (
        (0, 5), (25, 35), (55, 65), (85, 90))]))
    expected = np.column_stack((np.cos(angles), np.sin(angles)))
    if not np.allclose(data["train_u"], expected, rtol=0, atol=2e-14):
        raise ValueError("training directions differ from the frozen four-cluster law")
    if not np.array_equal(data["labels"], np.repeat([1., -1., 1., -1.], 4)):
        raise ValueError("labels differ from the frozen alternating cluster labels")
    if data["panel_u"].shape != (144, 2) or data["panel_theta"].shape != (144,):
        raise ValueError("the observation panel must contain 144 directions")
    if not np.array_equal(data["panel_u"][:16], data["train_u"]):
        raise ValueError("the first 16 panel entries must be the training directions")
    if data["dense_u"].ndim != 2 or data["dense_u"].shape[1] != 2:
        raise ValueError("invalid dense direction array")
    if len(data["dense_u"]) < 1440 or data["dense_theta"].shape != (len(data["dense_u"]),):
        raise ValueError("the final dense panel must contain at least 1440 directions")
    if not np.array_equal(data["times"], np.arange(201, dtype=float) / 2):
        raise ValueError("saved times must be 0, .5, ..., 100")
    for name in ("train_u", "panel_u", "dense_u"):
        if not np.allclose(np.sum(data[name] ** 2, axis=1), 1, rtol=0, atol=2e-14):
            raise ValueError(name + " must contain unit directions")
    for prefix in ("panel", "dense"):
        coordinates = np.column_stack((np.cos(data[prefix + "_theta"]),
                                       np.sin(data[prefix + "_theta"])))
        if not np.allclose(data[prefix + "_u"], coordinates, rtol=0, atol=2e-14):
            raise ValueError(prefix + " angles and coordinates disagree")
    return data


def _activation_fields(state, directions):
    """Read-only direct evaluation of the two nonlinear activation fields."""
    h1 = np.tanh(state.w @ directions.T)
    a = state.b1.T @ (state.p1[:, None] * h1)
    h2 = np.tanh(state.b2 @ (state.M @ a))
    return h1, h2


def _observe(state, directions, initial_training, labels):
    fields = _activation_fields(state, directions)
    predictions = state.p2 @ (state.c[:, None] * fields[1])
    grams = np.stack([h.T @ (p[:, None] * h)
                      for h, p in zip(fields, (state.p1, state.p2))])
    rms = np.array([np.sqrt(p @ np.mean(h[:, :16] ** 2, axis=1))
                    for h, p in zip(fields, (state.p1, state.p2))])
    movement = np.array([np.sqrt(p @ np.mean((h[:, :16] - initial) ** 2, axis=1))
                         for h, initial, p in zip(fields, initial_training, (state.p1, state.p2))])
    loss = float(np.mean((predictions[:16] - labels) ** 2))
    if not all(np.all(np.isfinite(value)) for value in (predictions, grams, rms, movement, loss)):
        raise ValueError("nonfinite observation")
    return dict(loss=loss, predictions=predictions, grams=grams, rms=rms, movement=movement)


def _save_trajectory(path, data, observations, dense_predictions=None):
    count = len(observations)
    arrays = {key: np.asarray([value[key] for value in observations])
              for key in ("loss", "predictions", "grams", "rms", "movement")}
    arrays.update(times=data["times"][:count], train_u=data["train_u"], labels=data["labels"],
                  panel_u=data["panel_u"], panel_theta=data["panel_theta"],
                  dense_u=data["dense_u"], dense_theta=data["dense_theta"])
    if dense_predictions is not None:
        arrays["dense_predictions"] = dense_predictions
    np.savez_compressed(path, **arrays)


def _deadline(_signum, _frame):
    raise TimeoutError("the frozen 600-second worker wall-time budget expired")


def run(args):
    out = _fresh_output(args.out)
    started, cpu_started = time.monotonic(), time.process_time()
    record = dict(status="running", kind="closure", config={
        "order": args.order, "initialization_nodes": args.initialization_nodes,
        "population_nodes": args.population_nodes, "step": args.step,
        "horizon": 100, "dtype": "float64", "block_size": 16,
        "input_convention": "unit u; physical network x=sqrt(2)u",
        "loss_convention": "unhalved uniform mean square",
    }, provenance=_provenance(), inputs_sha256=_hash(args.inputs))
    _json(out / "record.json", record)
    observations, state, data, law = [], None, None, None
    signal.signal(signal.SIGALRM, _deadline)
    signal.setitimer(signal.ITIMER_REAL, 600)
    try:
        data = _inputs(args.inputs)
        pair = (args.initialization_nodes, args.population_nodes)
        if pair not in ((2048, 1024), (4096, 2048)):
            raise ValueError("quadrature configuration is outside the frozen run menu")
        if args.step not in (.01, .005):
            raise ValueError("step is outside the frozen run menu")
        if args.step == .005 and (args.order, pair) not in ((3, (2048, 1024)), (5, (4096, 2048))):
            raise ValueError("this time-refinement configuration is outside the frozen run menu")
        step_indices = np.rint(data["times"] / args.step).astype(np.int64)
        if not np.allclose(step_indices * args.step, data["times"], rtol=0, atol=2e-12):
            raise ValueError("observation times must lie on this Heun mesh")
        state = solver.initialize(order=args.order, initialization_nodes=args.initialization_nodes,
                                  population_nodes=args.population_nodes)
        law = solver.DataLaw(data["train_u"].copy(), data["labels"].copy(), np.full(16, 1 / 16), {
            "scope": "exploratory first-quadrant four-cluster law through physical T=100",
            "angles_degrees": np.rad2deg(np.arctan2(data["train_u"][:, 1], data["train_u"][:, 0])).tolist(),
        }).validate(state.arithmetic)
        record["initialization_seconds"] = time.monotonic() - started
        record["initialization_metadata"] = state.metadata
        record["retained_state_bytes"] = solver.state_bytes(state)
        initial_training = tuple(h.copy() for h in _activation_fields(state, data["train_u"]))
        current_index = 0
        last_progress = time.monotonic()
        observation_seconds = 0.0
        for index, (physical_time, target_index) in enumerate(zip(data["times"], step_indices)):
            if target_index > current_index:
                state = solver.evolve(state, law, steps=int(target_index - current_index),
                                      step_size=args.step, block_size=16)
            current_index = int(target_index)
            before_observe = time.monotonic()
            item = _observe(state, data["panel_u"], initial_training, data["labels"])
            observation_seconds += time.monotonic() - before_observe
            observations.append(item)
            if index and item["loss"] > observations[-2]["loss"] + 1e-5:
                raise ValueError("saved loss increases beyond the frozen numerical gate")
            if time.monotonic() - last_progress >= 20 or index == len(data["times"]) - 1:
                print(json.dumps({"time": float(physical_time), "loss": item["loss"],
                                  "elapsed_seconds": time.monotonic() - started}), flush=True)
                last_progress = time.monotonic()
        dense_predictions = solver.predict(state, data["dense_u"], block_size=16)
        _save_trajectory(out / "trajectories.npz", data, observations, dense_predictions)
        solver.save_restart(out / "final_restart.json", state, law)
        restored, restored_law = solver.load_restart(out / "final_restart.json")
        exact_restart = all(np.array_equal(getattr(state, key), getattr(restored, key)) for key in (
            "b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"))
        exact_restart &= all(np.array_equal(getattr(law, key), getattr(restored_law, key))
                             for key in ("inputs", "labels", "probabilities"))
        exact_restart &= state.metadata == restored.metadata and law.metadata == restored_law.metadata
        exact_restart &= np.array_equal(dense_predictions, solver.predict(restored, data["dense_u"], block_size=16))
        if not exact_restart:
            raise ValueError("final exact own-state restart check failed")
        gram_stack = np.asarray([item["grams"] for item in observations])
        gram_symmetry = float(np.max(np.abs(gram_stack - gram_stack.swapaxes(-1, -2))))
        # Full Grams are retained; PSD is checked at every saved time for both layers.
        minimum_gram_eigenvalue = float(np.min(np.linalg.eigvalsh(
            (gram_stack + gram_stack.swapaxes(-1, -2)) / 2)))
        if gram_symmetry > 1e-10 or minimum_gram_eigenvalue < -1e-5:
            raise ValueError("Gram symmetry or PSD gate failed")
        record.update(status="complete", observation_seconds=observation_seconds,
                      final_loss=observations[-1]["loss"], exact_final_restart=bool(exact_restart),
                      maximum_gram_asymmetry=gram_symmetry,
                      minimum_gram_eigenvalue=minimum_gram_eigenvalue,
                      maximum_saved_loss_increase=float(np.max(np.diff([x["loss"] for x in observations]))),
                      observations_completed=len(observations), final_time=100.0)
    except Exception as error:
        record.update(status="failed", error_type=type(error).__name__, error=str(error),
                      traceback=traceback.format_exc(), observations_completed=len(observations),
                      final_time=float(data["times"][len(observations)-1]) if observations else None)
        if observations and data is not None and not (out / "trajectories.npz").exists():
            _save_trajectory(out / "partial_trajectories.npz", data, observations)
        if state is not None and law is not None and not (out / "final_restart.json").exists():
            solver.save_restart(out / "partial_restart.json", state, law)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        record.update(elapsed_seconds=time.monotonic() - started,
                      cpu_seconds=time.process_time() - cpu_started,
                      peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)
        record["output_sha256"] = {p.name: _hash(p) for p in out.iterdir()
                                   if p.is_file() and p.name != "record.json"}
        _json(out / "record.json", record)
    print(json.dumps({"status": record["status"], "out": str(out),
                      "elapsed_seconds": record["elapsed_seconds"],
                      "error": record.get("error")}), flush=True)
    return 0 if record["status"] == "complete" else 1


def check(args):
    """Small deterministic implementation gates; no T=100 training run."""
    out = _fresh_output(args.out)
    started = time.monotonic()
    record = dict(status="running", kind="closure_implementation_check", provenance=_provenance())
    try:
        state = solver.initialize(order=1, initialization_nodes=128, population_nodes=64)
        angles = np.linspace(0, np.pi / 2, 16)
        u = np.column_stack((np.cos(angles), np.sin(angles)))
        labels = np.repeat([1., -1., 1., -1.], 4)
        law = solver.DataLaw(u, labels, np.full(16, 1 / 16)).validate(state.arithmetic)
        initial = tuple(h.copy() for h in _activation_fields(state, u))
        frozen = state.copy()
        random = np.random.default_rng(20260914)
        current = state.dynamic_copy(state.w + .07 * random.normal(size=state.w.shape),
                                     .13 * random.normal(size=state.c.shape),
                                     state.M + .03 * random.normal(size=state.M.shape)).validate()
        panel = np.concatenate((u, solver.circle_inputs(8, current.arithmetic)))
        observation = _observe(current, panel, initial, labels)
        maintained_predictions = solver.predict(current, panel)
        prediction_error = float(np.max(np.abs(observation["predictions"] - maintained_predictions)))
        assert prediction_error < 1e-12
        maintained_pairs = solver.paired_observations(current, law)
        movement_error = float(np.max(np.abs(observation["movement"] - np.array([
            maintained_pairs["rms1"], maintained_pairs["rms2"]]))))
        assert movement_error < 1e-12
        gram_loop_error, rms_identity_error = 0., 0.
        for layer, (h, p) in enumerate(zip(_activation_fields(current, panel), (current.p1, current.p2))):
            direct = sum(weight * np.outer(row, row) for row, weight in zip(h, p))
            gram_loop_error = max(gram_loop_error, float(np.max(np.abs(observation["grams"][layer] - direct))))
            rms_identity_error = max(rms_identity_error, abs(observation["rms"][layer] ** 2 -
                                                            float(np.mean(np.diag(direct)[:16]))))
        assert gram_loop_error < 1e-12 and rms_identity_error < 1e-12
        assert abs(observation["loss"] - float(solver.loss(current, law))) < 1e-12
        half = solver.evolve(current, law, steps=1, step_size=.003)
        solver.save_restart(out / "check_restart.json", half, law)
        loaded, loaded_law = solver.load_restart(out / "check_restart.json")
        resumed = solver.evolve(loaded, loaded_law, steps=1, step_size=.003)
        uninterrupted = solver.evolve(current, law, steps=2, step_size=.003)
        for name in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"):
            assert np.array_equal(getattr(resumed, name), getattr(uninterrupted, name))
            assert np.array_equal(getattr(state, name), getattr(frozen, name))
        # Check the two-stage update on all moving blocks at a nonzero state.
        k = solver.rhs(current, law)
        stage = current.dynamic_copy(*(getattr(current, name) + .003 * value
                                       for name, value in zip(("w", "c", "M"), k)))
        ell = solver.rhs(stage, law)
        heun_error = max(float(np.max(np.abs(getattr(half, name) -
                           (getattr(current, name) + .0015 * (first + second)))))
                         for name, first, second in zip(("w", "c", "M"), k, ell))
        assert heun_error < 1e-12
        record.update(status="pass", prediction_max_abs=prediction_error,
                      movement_max_abs=movement_error, gram_loop_max_abs=gram_loop_error,
                      rms_gram_identity_max_abs=rms_identity_error, heun_max_abs=heun_error,
                      exact_restart_continuation=True, unchanged_initial_state=True)
    except Exception as error:
        record.update(status="failed", error=str(error), traceback=traceback.format_exc())
    record["passed"] = record["status"] == "pass"
    record["elapsed_seconds"] = time.monotonic() - started
    record["output_sha256"] = {p.name: _hash(p) for p in out.iterdir() if p.is_file()}
    _json(out / "check.json", record)
    _json(out / "record.json", record)
    print(json.dumps(record, indent=2, allow_nan=False), flush=True)
    return 0 if record["status"] == "pass" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--order", type=int, choices=(1, 3, 5), default=1)
    parser.add_argument("--initialization-nodes", type=int, default=2048)
    parser.add_argument("--population-nodes", type=int, default=1024)
    parser.add_argument("--step", type=float, default=.01)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.check and args.inputs is None:
        parser.error("--inputs is required for a scientific worker")
    return check(args) if args.check else run(args)


if __name__ == "__main__":
    raise SystemExit(main())
