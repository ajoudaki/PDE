"""Observation-only Gram extension of the unchanged study closure producer."""
from __future__ import annotations

import argparse
import ast
from fractions import Fraction
import importlib.util
import inspect
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PLAN = HERE / "GRAM_20260914_PLAN.md"
SPEC = importlib.util.spec_from_file_location("wide_gram_base_closure", HERE / "WIDE_GPU_20260914_CLOSURE.py")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)
np = base.np
solver = base.solver
RUN_CAP = 300.0
WORKER_CAP = 1200.0
GLOBAL_CAP = 2400.0
OUTPUT_CAP = 4 * 1024**3
TOLERANCE = 2e-11


def configurations():
    items = [dict(c, step="1/200", kind="quadrature_control" if c["refined"] else "primary")
             for c in base.configurations()]
    items.extend(dict(id=case + "_N3_halfstep", case=case, order=3,
                      initialization_nodes=1024, population_nodes=512,
                      refined=False, step="1/400", kind="time_control")
                 for case in base.CASES)
    return items


def source_hashes():
    result = base.source_hashes()
    result.update({str(path.relative_to(ROOT)): base.digest(path)
                   for path in (Path(__file__), PLAN)})
    return result


def manifest(output):
    output = Path(output).resolve()
    output.relative_to(ROOT / "data/generated/wide_network_closure_comparison")
    value = json.loads((output / "gram_campaign.json").read_text())
    if value["plan_sha256"] != base.digest(PLAN):
        raise ValueError("Gram campaign does not match the frozen plan")
    source = Path(value["source_run"]).resolve()
    source.relative_to(ROOT / "data/generated/wide_network_closure_comparison")
    if source == output:
        raise ValueError("Replay output must differ from its source run")
    for name in ("inputs.npz", "inputs.json"):
        if base.digest(output / name) != base.digest(source / name):
            raise ValueError("Gram input is not a literal copy of the earlier input: " + name)
    return value


def output_bytes(output):
    total = 0
    for path in output.rglob("*"):
        try:
            if path.is_file():
                total += path.stat().st_size
        except FileNotFoundError:
            # Concurrent workers atomically replace their own temporary records.
            continue
    return total


def global_remaining(record, local_start):
    return GLOBAL_CAP - (time.time() - float(record.get("experiment_started_epoch", local_start)))


def weighted_gram(hidden, probabilities):
    hidden = np.asarray(hidden, dtype=np.float64)
    probabilities = np.asarray(probabilities, dtype=np.float64)
    return hidden.T @ (probabilities[:, None] * hidden)


def gram_observation(state, data, circle, row):
    inputs = np.concatenate((data.inputs, circle), axis=0)
    chunks = [solver._fields(state, inputs[start:start + 16], False)
              for start in range(0, len(inputs), 16)]
    hidden = [np.concatenate([chunk[name] for chunk in chunks], axis=1)
              for name in ("h1", "h2")]
    grams = np.stack([weighted_gram(h, p) for h, p in zip(hidden, (state.p1, state.p2))])
    if not np.isfinite(grams).all():
        raise FloatingPointError("Nonfinite Gram observation")
    symmetry = float(np.max(np.abs(grams - grams.transpose(0, 2, 1))))
    bound = float(np.max(np.abs(grams)))
    m = len(data.inputs)
    trace = np.diagonal(grams[:, :m, :m], axis1=1, axis2=2) @ data.probabilities
    trace_error = float(np.max(np.abs(trace - row["raw_rms"]**2)))
    if symmetry > TOLERANCE or bound > 1 + TOLERANCE or trace_error > TOLERANCE:
        raise AssertionError(f"Gram gates failed: symmetry={symmetry}, bound={bound}, trace={trace_error}")
    return grams, dict(symmetry_error=symmetry, maximum_absolute_entry=bound,
                      diagonal_rms_error=trace_error)


def verification():
    """Deterministic nonorthogonal fixture; no scientific initializer or flow."""
    h = np.asarray([[.2, -.7, .4], [.9, .1, -.2], [-.5, .3, .8], [.6, -.4, -.1]])
    p = np.asarray([.1, .2, .3, .4])
    q = np.asarray([.2, .3, .5])
    gram = weighted_gram(h, p)
    oracle = np.asarray([[sum(float(p[i]) * float(h[i, a]) * float(h[i, b])
                             for i in range(len(p))) for b in range(h.shape[1])]
                         for a in range(h.shape[1])])
    np.testing.assert_allclose(gram, oracle, atol=1e-15, rtol=1e-15)
    permutation = [2, 0, 3, 1]
    np.testing.assert_allclose(weighted_gram(h[permutation], p[permutation]), gram,
                               atol=1e-15, rtol=1e-15)
    np.testing.assert_allclose(gram, gram.T, atol=1e-15, rtol=0)
    assert np.min(np.linalg.eigvalsh(gram)) > -1e-14
    assert np.max(np.abs(gram)) <= 1
    explicit_second = sum(float(q[a] * p[i] * h[i, a]**2)
                          for a in range(len(q)) for i in range(len(p)))
    np.testing.assert_allclose(q @ np.diag(gram), explicit_second, atol=1e-15, rtol=0)
    ar = solver.Arithmetic()
    state = solver.State(
        b1=np.asarray([[.3, -.2], [.5, .4], [-.1, .6]]),
        g=np.asarray([[.2, -.5], [.3, .6], [-.7, .1]]),
        w=np.asarray([[.4, -.2], [.1, .5], [-.6, .3]]),
        p1=np.asarray([.2, .3, .5]),
        b2=np.asarray([[.2, .3], [-.1, .5], [.6, -.4], [.7, .2]]),
        c=np.asarray([.2, -.3, .1, .4]), p2=p,
        M=np.asarray([[.4, -.2], [.1, .7]]),
        D=np.asarray([[.3, -.1], [.2, .6]]), arithmetic=ar).validate()
    data = solver.DataLaw(np.asarray([[1., 0.], [.6, .8]]), np.asarray([1., -1.]),
                          np.asarray([.35, .65])).validate(ar)
    circle = solver.circle_inputs(19, ar)
    frozen = [getattr(state, name).copy() for name in ("w", "c", "M")]
    row, _ = base.collect(state, data, circle)
    observed, gates = gram_observation(state, data, circle, row)
    u = np.concatenate((data.inputs, circle))
    h1 = np.asarray([[np.tanh(sum(float(state.w[i, d] * u[a, d]) for d in range(2)))
                      for a in range(len(u))] for i in range(3)])
    action = np.asarray([[sum(float(state.b1[i, j] * state.p1[i] * h1[i, a])
                             for i in range(3)) for a in range(len(u))] for j in range(2)])
    h2 = np.asarray([[np.tanh(sum(float(state.b2[i, j] * state.M[j, k] * action[k, a])
                                  for j in range(2) for k in range(2)))
                      for a in range(len(u))] for i in range(4)])
    for layer, (hidden, weights) in enumerate(((h1, state.p1), (h2, state.p2))):
        direct = np.asarray([[sum(float(weights[i] * hidden[i, a] * hidden[i, b])
                                  for i in range(len(weights))) for b in range(len(u))]
                             for a in range(len(u))])
        np.testing.assert_allclose(observed[layer], direct, atol=2e-15, rtol=2e-14)
        assert np.min(np.linalg.eigvalsh(observed[layer])) > -1e-13
    for name, expected in zip(("w", "c", "M"), frozen):
        np.testing.assert_array_equal(getattr(state, name), expected)
    tree = ast.parse(inspect.getsource(base.run_configuration))
    calls = [ast.unparse(node.func) for node in ast.walk(tree) if isinstance(node, ast.Call)]
    assert "solver.initialize" in calls and "solver.evolve" in calls and "collect" in calls
    return dict(status="passed", explicit_entrywise_oracle=True,
                population_permutation=True, positive_semidefinite=True,
                scalar_trace=True, blocked_field_oracle=True, observation_preserves_state=True,
                original_integrator_reused=True, fixture_gates=gates, source_hashes=source_hashes())


def replay_check(output, config, directory, shared):
    if config["kind"] == "time_control":
        return dict(status="not_applicable_new_time_control", baseline=config["case"] + "_N3")
    old = Path(shared["source_run"]) / "closure" / config["id"] / "observations.npz"
    new = directory / "observations.npz"
    if not old.exists() or not new.exists():
        return dict(status="missing_input", source=str(old))
    with np.load(old, allow_pickle=False) as left, np.load(new, allow_pickle=False) as right:
        if set(left.files) != set(right.files):
            return dict(status="field_mismatch", old_fields=left.files, new_fields=right.files)
        if any(left[key].shape != right[key].shape for key in left.files):
            return dict(status="incomplete_shape", source=str(old))
        errors = {key: float(np.max(np.abs(left[key] - right[key]))) for key in left.files}
    maximum = max(errors.values())
    return dict(status="passed" if maximum <= 1e-10 else "failed", maximum_absolute_error=maximum,
                tolerance=1e-10, per_field_errors=errors, source=str(old), source_sha256=base.digest(old))


def run_configuration(output, config):
    shared = manifest(output)
    arrays, _ = base.load_inputs(output)
    directory = output / "closure" / config["id"]
    directory.mkdir(parents=True, exist_ok=True)
    if (directory / "record.json").exists() or (directory / "gram.npy").exists():
        raise FileExistsError("Refusing to overwrite an existing Gram trajectory")
    started = time.time()
    shape = (len(arrays["times"]), 2, len(arrays[config["case"] + "_inputs"]) + 128,
             len(arrays[config["case"] + "_inputs"]) + 128)
    if output_bytes(output) + int(np.prod(shape)) * 8 + 4096 > OUTPUT_CAP:
        raise RuntimeError("Frozen total output cap would be exceeded")
    gram_path = directory / "gram.npy"
    mapped = np.lib.format.open_memmap(gram_path, mode="w+", dtype=np.float64, shape=shape)
    mapped[:] = np.nan
    mapped.flush()
    progress = dict(format="gram-closure-observations-v1", completed_rows=0, shape=list(shape),
                    dtype="float64", input_order="training inputs then all 128 circle inputs; no deduplication",
                    training_count=shape[2]-128, source_hashes=source_hashes(),
                    times_sha256=base.array_hash(arrays["times"]),
                    maximum_gate_errors=dict(symmetry_error=0., maximum_absolute_entry=0., diagonal_rms_error=0.))
    original_collect, original_atomic, original_h = base.collect, base.atomic_json, base.H
    original_limit = base.RUN_WALL_CAP

    def collect(state, data, circle):
        if time.time() - started >= RUN_CAP or global_remaining(shared, started) <= 0:
            raise TimeoutError("Frozen Gram trajectory/global wall cap")
        if output_bytes(output) >= OUTPUT_CAP:
            raise RuntimeError("Frozen total output cap reached")
        row, paired = original_collect(state, data, circle)
        gram, gates = gram_observation(state, data, circle, row)
        index = progress["completed_rows"]
        if index >= shape[0]:
            raise AssertionError("Too many Gram observations")
        mapped[index] = gram
        mapped.flush()
        progress["completed_rows"] = index + 1
        progress["last_time"] = float(arrays["times"][index])
        for key, value in gates.items():
            progress["maximum_gate_errors"][key] = max(progress["maximum_gate_errors"][key], value)
        original_atomic(directory / "gram_progress.json", progress)
        return row, paired

    def atomic(path, value):
        if path == directory / "record.json":
            value["format"] = "gram-20260914-closure-v1"
            value["steps"] = int(Fraction(40) / base.H)
            value["gram"] = dict(progress, file="gram.npy",
                                 valid_rows=min(progress["completed_rows"], value.get("completed_observations", 0)))
            value["gram_shape"] = list(shape)
            value["gram_completed_observations"] = value["gram"]["valid_rows"]
            value["source_hashes"] = source_hashes()
            value["gram_plan_sha256"] = base.digest(PLAN)
            value["original_comparison_status"] = "Gram replay consistency recorded separately below"
            value["original_comparison_scope"] = "Compares only the previous run in this same study."
            if value["status"] != "running":
                mapped.flush()
                value["gram"]["sha256"] = base.digest(gram_path)
                value["gram_sha256"] = value["gram"]["sha256"]
                value["replay_check"] = replay_check(output, config, directory, shared)
                if value["status"] == "complete" and value["gram"]["valid_rows"] != shape[0]:
                    value["status"] = "failure"
                    value["error"] = "Gram row count does not match completed trajectory"
        return original_atomic(path, value)

    base.collect, base.atomic_json, base.H = collect, atomic, Fraction(config["step"])
    base.RUN_WALL_CAP = min(RUN_CAP, max(0., global_remaining(shared, started)))
    try:
        return base.run_configuration(output, config)
    finally:
        mapped.flush()
        base.collect, base.atomic_json, base.H = original_collect, original_atomic, original_h
        base.RUN_WALL_CAP = original_limit


def run_campaign(output):
    shared = manifest(output)
    base.load_inputs(output)
    path = output / "closure_campaign.json"
    if path.exists():
        raise FileExistsError("Refusing to overwrite an earlier closure campaign")
    verification_result = verification()
    base.atomic_json(output / "closure_gram_verification.json", verification_result)
    start = time.time()
    campaign = dict(status="running", maximum_runs=10, source_hashes=source_hashes(),
                    run_wall_cap=RUN_CAP, worker_wall_cap=WORKER_CAP, global_wall_cap=GLOBAL_CAP,
                    output_cap_bytes=OUTPUT_CAP, numerical_threads=1, runs=[], command=sys.argv)
    base.atomic_json(path, campaign)
    worker_seconds = 0.
    for config in configurations():
        remaining = min(WORKER_CAP - worker_seconds, global_remaining(shared, start))
        if remaining <= 0 or output_bytes(output) >= OUTPUT_CAP:
            campaign["runs"].append(dict(id=config["id"], status="unstarted_budget"))
            continue
        directory = output / "closure" / config["id"]
        directory.mkdir(parents=True, exist_ok=False)
        command = [sys.executable, "-B", str(Path(__file__).resolve()), "--output", str(output),
                   "--worker-id", config["id"]]
        launched = time.time()
        stop_reason = None
        with (directory / "worker.log").open("xb") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, cwd=ROOT)
            while process.poll() is None:
                elapsed = time.time() - launched
                if elapsed >= min(RUN_CAP, remaining):
                    stop_reason = "wall_budget"
                elif output_bytes(output) >= OUTPUT_CAP:
                    stop_reason = "output_budget"
                if stop_reason:
                    process.terminate()
                    try:
                        process.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                    break
                time.sleep(.25)
        elapsed = time.time() - launched
        worker_seconds += elapsed
        record_path = directory / "record.json"
        record = json.loads(record_path.read_text()) if record_path.exists() else dict(configuration=config)
        if stop_reason or process.returncode != 0:
            record.update(status="stopped" if stop_reason else "failure", worker_exit_code=process.returncode,
                          stop_reason=stop_reason, supervisor_wall_seconds=elapsed)
            progress_path = directory / "gram_progress.json"
            if progress_path.exists():
                progress = json.loads(progress_path.read_text())
                record["gram"] = dict(progress, file="gram.npy", valid_rows=progress["completed_rows"],
                                      sha256=base.digest(directory / "gram.npy"))
            base.atomic_json(record_path, record)
        campaign["runs"].append(dict(id=config["id"], status=record.get("status", "failure"),
                                     returncode=process.returncode, wall_seconds=elapsed, command=command))
        campaign.update(worker_wall_seconds=worker_seconds, wall_seconds=time.time() - start)
        base.atomic_json(path, campaign)
        print(json.dumps(campaign["runs"][-1]), flush=True)
    campaign.update(status="complete" if all(r["status"] == "complete" for r in campaign["runs"]) else "incomplete",
                    worker_wall_seconds=worker_seconds, wall_seconds=time.time() - start,
                    total_output_bytes=output_bytes(output))
    base.atomic_json(path, campaign)
    return 0 if campaign["status"] == "complete" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--run", action="store_true")
    action.add_argument("--verify-only", action="store_true")
    action.add_argument("--worker-id", choices=[c["id"] for c in configurations()])
    args = parser.parse_args()
    output = args.output.resolve()
    if args.verify_only:
        manifest(output)
        print(json.dumps(verification(), indent=2), flush=True)
        return 0
    if args.worker_id:
        return run_configuration(output, next(c for c in configurations() if c["id"] == args.worker_id))
    return run_campaign(output)


if __name__ == "__main__":
    raise SystemExit(main())
