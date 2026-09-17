#!/usr/bin/env python3
"""Frozen-plan closure worker; verification never launches a research trajectory."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import resource
import shlex
import shutil
import signal
import sys
import time
import traceback

THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
ORIGINAL_THREAD_ENV = {key: os.environ.get(key) for key in THREAD_KEYS}
for _key in THREAD_KEYS:
    os.environ[_key] = "1"
sys.dont_write_bytecode = True
STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/xor_network_closure"
sys.path.insert(0, str(ROOT / "code"))

import numpy as np
from pde import observable_solver as solver
from pde.observable_arithmetic import Arithmetic

STATE_KEYS = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
SOURCE_NAMES = ("observable_solver.py", "observable_initialization.py",
                "observable_arithmetic.py", "observable_fixed.py", "observable_words.py")
TOL = 2e-10
GIB = 1024 ** 3


class StopRun(RuntimeError):
    pass


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def array_hash(array):
    value = np.ascontiguousarray(array)
    digest = hashlib.sha256()
    digest.update(json.dumps({"shape": value.shape, "dtype": value.dtype.str},
                             sort_keys=True).encode())
    digest.update(value.tobytes())
    return digest.hexdigest()


def state_hashes(state):
    return {key: array_hash(getattr(state, key)) for key in STATE_KEYS}


def source_hashes():
    paths = [Path(__file__).resolve(), STUDY / "EXPERIMENT_PLAN.md",
             ROOT / "docs/NOTATION.md", ROOT / "code/README.md"]
    paths.extend(ROOT / "code/pde" / name for name in SOURCE_NAMES)
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths}


def write_json(path, record):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n")
    temporary.replace(path)


def environment():
    config = io.StringIO()
    with contextlib.redirect_stdout(config):
        np.show_config()
    return {"python": sys.version, "executable": sys.executable,
            "platform": platform.platform(), "machine": platform.machine(),
            "processor": platform.processor(), "hostname": platform.node(),
            "numpy": np.__version__, "numpy_config": config.getvalue(),
            "thread_environment": {key: os.environ[key] for key in THREAD_KEYS},
            "original_thread_environment": ORIGINAL_THREAD_ENV,
            "cpu_affinity": sorted(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None,
            "command": shlex.join(getattr(sys, "orig_argv", [sys.executable, *sys.argv])), "cwd": os.getcwd()}


def output_hashes(directory):
    return {str(path.relative_to(directory)): sha256(path)
            for path in sorted(directory.rglob("*"))
            if path.is_file() and path.name not in ("record.json", "record.json.tmp")}


def contained(path, parent):
    path = Path(path).resolve()
    if path == parent or parent not in path.parents:
        raise ValueError(f"output must be a child of {parent}")
    return path


def resource_check(deadline, reserve=0):
    if time.time() >= deadline:
        raise StopRun("worker or global scientific wall-time limit reached (5s evidence reserve)")
    if shutil.disk_usage(GENERATED).free < 3 * GIB + reserve:
        raise StopRun("minimum 3 GiB free disk bound would be crossed")
    size = sum(path.stat().st_size for path in GENERATED.rglob("*") if path.is_file())
    if size + reserve > 8 * GIB:
        raise StopRun("8 GiB study generated-output bound would be crossed")


def hidden_fields(state, panel):
    """Current activations evaluated in input blocks of 16, in float64."""
    first = np.empty((len(state.p1), len(panel)), dtype=np.float64)
    second = np.empty((len(state.p2), len(panel)), dtype=np.float64)
    for start in range(0, len(panel), 16):
        stop = min(start + 16, len(panel))
        h1 = np.tanh(state.w @ panel[start:stop].T)
        coefficients = state.b1.T @ (state.p1[:, None] * h1)
        h2 = np.tanh(state.b2 @ (state.M @ coefficients))
        first[:, start:stop], second[:, start:stop] = h1, h2
    return first, second


def observations(state, data, panel, initial_hidden):
    hidden = hidden_fields(state, panel)
    prediction = state.p2 @ (state.c[:, None] * hidden[1])
    residual = prediction[:len(data.inputs)] - data.labels
    loss = float(data.probabilities @ (residual * residual))
    grams, raw, movement = [], [], []
    for actual, initial, population in zip(hidden, initial_hidden, (state.p1, state.p2)):
        grams.append(actual.T @ (population[:, None] * actual))
        train = actual[:, :len(data.inputs)]
        change = train - initial[:, :len(data.inputs)]
        raw.append(np.sqrt(population @ (train * train) @ data.probabilities))
        movement.append(np.sqrt(population @ (change * change) @ data.probabilities))
    return {"loss": loss, "predictions": prediction, "gram": np.stack(grams),
            "raw_rms": np.asarray(raw), "movement_rms": np.asarray(movement)}


def validate_observation(value, data, endpoint=False):
    if not all(np.isfinite(item).all() for item in value.values()):
        raise ValueError("nonfinite observation")
    grams = value["gram"]
    symmetry = float(np.max(np.abs(grams - grams.transpose(0, 2, 1))))
    bounded = float(np.max(np.abs(grams)))
    diagonals = np.diagonal(grams, axis1=1, axis2=2)
    raw_square = diagonals[:, :len(data.inputs)] @ data.probabilities
    identity = float(np.max(np.abs(raw_square - value["raw_rms"] ** 2)))
    residual = value["predictions"][:len(data.inputs)] - data.labels
    loss_identity = abs(value["loss"] - float(data.probabilities @ (residual * residual)))
    if symmetry > TOL or bounded > 1 + TOL or np.min(diagonals) < -TOL:
        raise ValueError("Gram symmetry or tanh bound failed")
    if identity > TOL or loss_identity > TOL:
        raise ValueError("Gram diagonal/RMS or MSE identity failed")
    eigenvalues = [float(np.linalg.eigvalsh(gram)[0]) for gram in grams] if endpoint else None
    if eigenvalues is not None and min(eigenvalues) < -TOL:
        raise ValueError("endpoint Gram PSD gate failed")
    return {"symmetry_max_abs": symmetry, "gram_max_abs": bounded,
            "raw_rms_square_identity_max_abs": identity,
            "loss_identity_abs": loss_identity, "minimum_eigenvalues": eigenvalues}


def verify(output):
    output = contained(output, GENERATED / "checks")
    output.mkdir(parents=True, exist_ok=False)
    started = time.time()
    record = {"kind": "deterministic-implementation-check", "status": "running",
              "started_epoch": started, "environment": environment(), "source_hashes": source_hashes()}
    write_json(output / "record.json", record)
    try:
        rng = np.random.default_rng(7329)
        p1 = np.arange(1, 8, dtype=float); p1 /= p1.sum()
        p2 = np.arange(1, 10, dtype=float); p2 /= p2.sum()
        g = rng.normal(size=(7, 2))
        D = rng.normal(scale=0.2, size=(3, 4))
        state = solver.State(rng.normal(size=(7, 4)), g, g + rng.normal(scale=0.2, size=g.shape),
                             p1, rng.normal(size=(9, 3)), rng.normal(scale=0.2, size=9), p2,
                             D + rng.normal(scale=0.1, size=D.shape), D, Arithmetic(),
                             {"scope": "nonzero synthetic implementation state"}).validate()
        angles = np.arange(19) * (2 * np.pi / 19)
        panel = np.column_stack((np.cos(angles), np.sin(angles)))
        data = solver.DataLaw(panel[:4], np.array([1., -1., 0.3, -0.2]),
                              np.array([0.1, 0.2, 0.3, 0.4])).validate(state.arithmetic)
        initial = state.dynamic_copy(state.g, np.zeros_like(state.c), state.D)
        initial_hidden = hidden_fields(initial, panel)
        actual = observations(state, data, panel, initial_hidden)
        fields = solver._fields(state, panel, backward=False)
        paired = solver.paired_observations(state, data, block_size=16)
        errors = {}
        def check(name, left, right):
            error = float(np.max(np.abs(np.asarray(left) - np.asarray(right))))
            errors[name] = error
            if error > 2e-13:
                raise AssertionError(f"{name}: {error}")
        for layer, (key, pop) in enumerate((("h1", state.p1), ("h2", state.p2))):
            check(f"hidden_layer_{layer+1}", hidden_fields(state, panel)[layer], fields[key])
            manual = np.zeros((len(panel), len(panel)))
            for weight, row in zip(pop, fields[key]):
                manual += weight * np.outer(row, row)
            check(f"gram_layer_{layer+1}", actual["gram"][layer], manual)
        check("predictions", actual["predictions"], solver.predict(state, panel, block_size=16))
        check("loss", actual["loss"], solver.loss(state, data, block_size=16))
        check("movement_rms", actual["movement_rms"], [paired["rms1"], paired["rms2"]])
        gate = validate_observation(actual, data, endpoint=True)
        initial_observation = observations(initial, data, panel, initial_hidden)
        check("initial_movement_zero", initial_observation["movement_rms"], np.zeros(2))
        solver.save_restart(output / "synthetic_restart.json", state, data)
        restored, restored_data = solver.load_restart(output / "synthetic_restart.json")
        if state_hashes(state) != state_hashes(restored):
            raise AssertionError("restart changed state bits")
        for name in ("inputs", "labels", "probabilities"):
            if not np.array_equal(getattr(data, name), getattr(restored_data, name)):
                raise AssertionError("restart changed data bits")
        solver.save_restart(output / "synthetic_restart_roundtrip.json", restored, restored_data)
        if sha256(output / "synthetic_restart.json") != sha256(output / "synthetic_restart_roundtrip.json"):
            raise AssertionError("restart roundtrip is not byte-exact")
        left = solver.evolve(state, data, steps=2, step_size=0.01, block_size=16)
        right = solver.evolve(restored, restored_data, steps=2, step_size=0.01, block_size=16)
        if state_hashes(left) != state_hashes(right):
            raise AssertionError("synthetic restart evolution changed bits")
        check("restart_observations", observations(restored, restored_data, panel, initial_hidden)["gram"], actual["gram"])
        np.savez(output / "synthetic_observations.npz", **actual)
        record.update(status="success", checks=errors, numerical_gates=gate,
                      restart_state_bit_exact=True, restart_file_byte_exact=True,
                      restart_continuation_bit_exact=True,
                      initialization_state_hashes=state_hashes(state),
                      research_trajectories_run=0)
    except Exception as exc:
        record.update(status="failed", error=f"{type(exc).__name__}: {exc}", traceback=traceback.format_exc())
    record.update(finished_epoch=time.time(), wall_seconds=time.time()-started,
                  output_hashes=output_hashes(output), output_hash_exclusions=["record.json (self-referential)"])
    write_json(output / "record.json", record)
    print(json.dumps({"status": record["status"], "output": str(output), "record_sha256": sha256(output / "record.json")}))
    return 0 if record["status"] == "success" else 1


def run(output, run_id):
    output = contained(output, GENERATED)
    if not run_id or Path(run_id).name != run_id or run_id in (".", ".."):
        raise ValueError("run-id must be one safe directory name")
    directory = output / "closure" / run_id
    directory.mkdir(parents=True, exist_ok=False)
    started = time.time()
    record = {"kind": "closure", "run_id": run_id, "status": "running", "started_epoch": started,
              "environment": environment(), "source_hashes": source_hashes(),
              "observation_count": 0, "observation_times": [], "steps_completed": 0,
              "dtype": "float64", "block_size": 16, "integrator": "maintained simultaneous explicit Heun",
              "loss_increase_flags": [], "timings": {"initialization_seconds": 0., "evolution_seconds": 0., "observation_seconds": 0.}}
    write_json(directory / "record.json", record)
    gram = None
    saved = {"times": [], "loss": [], "predictions": [], "raw_rms": [], "movement_rms": []}
    try:
        manifest_path = output / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        configs = manifest["closure_runs"]
        matches = [item for item in configs if item["name"] == run_id]
        if len(matches) != 1:
            raise ValueError("run-id must match exactly one declared closure_runs name")
        config = matches[0]
        record.update(config=config, manifest_sha256=sha256(manifest_path), inputs_sha256=sha256(output / "inputs.npz"))
        if manifest["inputs_sha256"] != record["inputs_sha256"]:
            raise ValueError("shared input hash differs from frozen manifest")
        if manifest["plan_sha256"] != sha256(STUDY / "EXPERIMENT_PLAN.md"):
            raise ValueError("experiment plan hash differs from frozen manifest")
        required_sources = [str(Path(__file__).resolve().relative_to(ROOT))]
        required_sources += ["code/pde/" + name for name in SOURCE_NAMES]
        for name in required_sources:
            if manifest["source_hashes"].get(name) != record["source_hashes"][name]:
                raise ValueError(f"source hash differs from frozen manifest: {name}")
        selected = (config["order"], config["initialization_nodes"], config["population_nodes"], float(config["step"]))
        allowed = {(n, q, p, .01) for n in (1, 3, 5) for q, p in ((2048, 1024), (4096, 2048))}
        allowed |= {(3, 2048, 1024, .005), (5, 4096, 2048, .005)}
        if selected not in allowed:
            raise ValueError("configuration is outside the eight predeclared closure runs")
        scientific_start = float(manifest["scientific_start_epoch"])
        if not np.isfinite(scientific_start) or scientific_start > time.time() + 1:
            raise ValueError("invalid common scientific start epoch")
        deadline = min(started + 600, scientific_start + 1200) - 5
        record.update(scientific_start_epoch=scientific_start, scientific_deadline_epoch=scientific_start + 1200,
                      worker_deadline_epoch=started + 600, computation_deadline_epoch=deadline)
        def alarm(_signal, _frame):
            raise StopRun("worker or global scientific wall-time bound reached")
        signal.signal(signal.SIGALRM, alarm)
        signal.signal(signal.SIGTERM, alarm)
        resource_check(deadline)
        signal.setitimer(signal.ITIMER_REAL, max(0.001, deadline - time.time()))
        with np.load(output / "inputs.npz", allow_pickle=False) as archive:
            inputs, labels, weights, panel, times = (np.asarray(archive[key], dtype=np.float64)
                                                   for key in ("inputs", "labels", "weights", "panel", "times"))
        expected_times = np.arange(201, dtype=np.float64) * 0.5
        if inputs.shape != (16, 2) or labels.shape != (16,) or weights.shape != (16,) or panel.shape != (144, 2):
            raise ValueError("input/panel shape differs from frozen contract")
        if not np.array_equal(times, expected_times) or not np.array_equal(inputs, panel[:16]):
            raise ValueError("observation schedule or training-first panel differs from contract")
        if not all(np.isfinite(a).all() for a in (inputs, labels, weights, panel, times)):
            raise ValueError("nonfinite shared inputs")
        if not np.array_equal(weights, np.full(16, 1/16)):
            raise ValueError("training weights must be exactly equal")
        if np.max(np.abs(np.sum(panel * panel, axis=1) - 1)) > 2e-12:
            raise ValueError("panel is not on the unit circle")
        record["input_array_hashes"] = {key: array_hash(value) for key, value in
                                         zip(("inputs", "labels", "weights", "panel", "times"),
                                             (inputs, labels, weights, panel, times))}
        resource_check(deadline, reserve=201 * 2 * 144 * 144 * 8 + 32 * 1024**2)
        tick = time.perf_counter()
        state = solver.initialize(order=config["order"], initialization_nodes=config["initialization_nodes"],
                                  population_nodes=config["population_nodes"], digits=None)
        data = solver.DataLaw(inputs, labels, weights,
                               {"scope": "exploratory shifted four-pole XOR", "source": "inputs.npz"}).validate(state.arithmetic)
        record["timings"]["initialization_seconds"] = time.perf_counter() - tick
        record.update(initialization_state_hashes=state_hashes(state), initialization_metadata=state.metadata,
                      retained_state_bytes=solver.state_bytes(state))
        if not np.array_equal(state.w, state.g) or np.any(state.c != 0) or not np.array_equal(state.M, state.D):
            raise ValueError("maintained initializer violated the own-state initial convention")
        initial_hidden = hidden_fields(state, panel)
        gram = np.lib.format.open_memmap(directory / "gram.npy", mode="w+", dtype=np.float64,
                                        shape=(201, 2, 144, 144))
        gram[:] = np.nan
        gram.flush()
        step = float(config["step"])
        steps_per_observation = int(round(0.5 / step))
        if steps_per_observation * step != 0.5:
            raise ValueError("step does not divide the observation interval")
        aggregate = {"symmetry_max_abs": 0., "gram_max_abs": 0., "raw_rms_square_identity_max_abs": 0., "loss_identity_abs": 0.}
        for index, physical_time in enumerate(times):
            resource_check(deadline)
            if index:
                tick = time.perf_counter()
                state = solver.evolve(state, data, steps=steps_per_observation, step_size=step, block_size=16)
                record["timings"]["evolution_seconds"] += time.perf_counter() - tick
                record["steps_completed"] += steps_per_observation
            tick = time.perf_counter()
            value = observations(state, data, panel, initial_hidden)
            try:
                gates = validate_observation(value, data, endpoint=index == len(times)-1)
            except Exception:
                np.savez(directory / "failed_observation.npz", time=float(physical_time), **value)
                raise
            for key in aggregate:
                aggregate[key] = max(aggregate[key], gates[key])
            if gates["minimum_eigenvalues"] is not None:
                record["endpoint_minimum_eigenvalues"] = gates["minimum_eigenvalues"]
            if index and value["loss"] - saved["loss"][-1] > max(1e-6, 1e-4 * saved["loss"][-1]):
                record["loss_increase_flags"].append({"time": float(physical_time), "previous_loss": saved["loss"][-1],
                                                      "loss": value["loss"], "increase": value["loss"]-saved["loss"][-1]})
            gram[index] = value["gram"]
            saved["times"].append(float(physical_time))
            for key in ("loss", "predictions", "raw_rms", "movement_rms"):
                saved[key].append(value[key])
            record["timings"]["observation_seconds"] += time.perf_counter() - tick
            record.update(observation_count=len(saved["times"]), observation_times=saved["times"],
                          numerical_gates=aggregate, last_observed_time=float(physical_time))
            np.savez(directory / "observations.npz", **{key: np.asarray(value) for key, value in saved.items()})
            gram.flush()
            write_json(directory / "record.json", record)
        resource_check(deadline, reserve=32 * 1024**2)
        solver.save_restart(directory / "checkpoint.json", state, data)
        record.update(status="success", endpoint_state_hashes=state_hashes(state), endpoint_time=100.,
                      finite_observations=True, expected_observation_count=201,
                      sampled_loss_monotonicity_pass=not record["loss_increase_flags"])
    except BaseException as exc:
        record.update(status="stopped" if isinstance(exc, StopRun) else "failed",
                      error=f"{type(exc).__name__}: {exc}", traceback=traceback.format_exc())
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if gram is not None:
            gram.flush()
        record.update(finished_epoch=time.time(), wall_seconds=time.time() - started,
                      peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
                      exit_status=0 if record["status"] == "success" else 1,
                      output_hashes=output_hashes(directory),
                      output_hash_exclusions=["record.json (self-referential)"],
                      partial_evidence_policy="valid observation prefix only; unsampled Gram slices remain NaN")
        write_json(directory / "record.json", record)
    print(json.dumps({"run_id": run_id, "status": record["status"], "observations": record["observation_count"],
                      "wall_seconds": record["wall_seconds"]}), flush=True)
    return record["exit_status"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--run-id")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        if args.run_id is not None:
            parser.error("--verify does not accept --run-id")
        return verify(args.output)
    if args.run_id is None:
        parser.error("--run-id is required for a declared research run")
    return run(args.output, args.run_id)


if __name__ == "__main__":
    raise SystemExit(main())
