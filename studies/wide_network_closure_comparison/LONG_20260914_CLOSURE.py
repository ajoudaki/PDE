"""Frozen fixed-Heun closure continuation with checked replay and actual restarts."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


# The inherited producer sets all numerical thread counts before importing NumPy.
arc = module("long_closure_arc", HERE / "ARC30_20260914_CLOSURE.py")
common = module("long_closure_common", HERE / "LONG_20260914_COMMON.py")
base, gram = arc.base, arc.gram
np, solver = base.np, base.solver
PLAN_SHA256 = "e3ff7a4462d6ddf17c6cb287c76875edd56a6c933bd6b7b2f83ba3dfa25aebc8"
ARRAY_NAMES = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
REPLAY_ATOL, REPLAY_RTOL = 1e-10, 1e-9
GRAM_TOLERANCE = 2e-11


def source_hashes():
    result = arc.source_hashes()
    for path in (Path(__file__), common.PLAN, HERE / "LONG_20260914_COMMON.py"):
        result[str(path.relative_to(common.ROOT))] = common.sha(path)
    return result


def initial_hashes(state):
    return {name: base.array_hash(getattr(state, name)) for name in ARRAY_NAMES}


def compare_arrays(actual, expected, name, atol=REPLAY_ATOL, rtol=REPLAY_RTOL):
    actual, expected = np.asarray(actual), np.asarray(expected)
    if actual.shape != expected.shape:
        raise AssertionError(f"{name}: shape mismatch {actual.shape} != {expected.shape}")
    if not np.isfinite(actual).all() or not np.isfinite(expected).all():
        raise AssertionError(f"{name}: nonfinite values")
    error = float(np.max(np.abs(actual - expected))) if actual.size else 0.
    if not np.allclose(actual, expected, atol=atol, rtol=rtol):
        raise AssertionError(f"{name}: replay/continuity mismatch, maximum absolute error {error}")
    return error


def check_loss_change(previous, current):
    increase = float(current - previous)
    limit = max(1e-4, .01 * float(previous))
    if increase > limit:
        raise FloatingPointError(f"Saved loss increased by {increase}, above {limit}")
    return increase


def validate_observation(row, grams, data, endpoint=False):
    if not all(np.isfinite(value).all() for value in row.values()):
        raise FloatingPointError("Nonfinite scalar or prediction observation")
    if grams.shape != (2, 144, 144) or not np.isfinite(grams).all():
        raise AssertionError("Invalid full Gram shape or values")
    if row["predictions"].shape != (128,) or row["data_predictions"].shape != (16,):
        raise AssertionError("Invalid prediction panel shape")
    residual = row["data_predictions"] - data.labels
    loss_error = abs(float(row["loss"]) - float(data.probabilities @ (residual * residual)))
    if loss_error > GRAM_TOLERANCE:
        raise AssertionError("Loss does not agree with training predictions")
    symmetry = float(np.max(np.abs(grams - grams.transpose(0, 2, 1))))
    bound = float(np.max(np.abs(grams)))
    trace = np.diagonal(grams[:, :16, :16], axis1=1, axis2=2) @ data.probabilities
    trace_error = float(np.max(np.abs(trace - row["raw_rms"] ** 2)))
    if max(symmetry, trace_error) > GRAM_TOLERANCE or bound > 1 + GRAM_TOLERANCE:
        raise AssertionError("Gram symmetry, boundedness, or weighted diagonal gate failed")
    result = dict(loss_from_predictions_error=loss_error, symmetry_error=symmetry,
                  maximum_absolute_entry=bound, diagonal_rms_error=trace_error)
    if endpoint:
        minimum = float(min(np.linalg.eigvalsh((g + g.T) / 2).min() for g in grams))
        if minimum < -GRAM_TOLERANCE:
            raise AssertionError(f"Endpoint Gram is not positive semidefinite: {minimum}")
        result["endpoint_minimum_eigenvalue"] = minimum
    return result


def load_inputs(output, manifest):
    with np.load(output / "inputs.npz", allow_pickle=False) as archive:
        arrays = {name: archive[name].copy() for name in archive.files}
    metadata = json.loads((output / "inputs.json").read_text())
    expected = {"times", "circle", "arcs30_inputs", "arcs30_labels", "arcs30_probabilities"}
    if set(arrays) != expected or set(metadata["array_sha256"]) != expected:
        raise AssertionError("Prepared input fields differ from ARC30")
    for key in expected:
        if base.array_hash(arrays[key]) != metadata["array_sha256"][key]:
            raise AssertionError("Prepared input array hash mismatch: " + key)
    if common.sha(output / "inputs.npz") != manifest["inputs_sha256"]:
        raise AssertionError("Prepared input archive hash mismatch")
    if arrays["circle"].shape != (128, 2) or arrays["arcs30_inputs"].shape != (16, 2):
        raise AssertionError("Prepared panel shape mismatch")
    np.testing.assert_array_equal(arrays["times"], np.asarray([float(t) for t in base.observation_times()]))
    return arrays, metadata


def archived_evidence(source, config):
    directory = source / "closure" / config["id"]
    record_path = directory / "record.json"
    record = json.loads(record_path.read_text())
    if (record["status"] != "complete" or record["configuration"] != config
            or Fraction(record["last_time"]) != 40 or record["completed_observations"] != 206):
        raise AssertionError("Archived closure run is incomplete or has a different configuration")
    for filename, key in (("observations.npz", "observations_sha256"), ("gram.npy", "gram_sha256")):
        if common.sha(directory / filename) != record[key]:
            raise AssertionError("Archived evidence hash mismatch: " + filename)
    for relative, expected in record["source_hashes"].items():
        # Source paths are limited to this study's producers and maintained APIs.
        path = (common.ROOT / relative).resolve()
        if not (path.is_relative_to(HERE) or path.is_relative_to(common.ROOT / "code")):
            raise AssertionError("Archived source outside assigned source boundary")
        if common.sha(path) != expected:
            raise AssertionError("Archived producer source has changed: " + relative)
    with np.load(directory / "observations.npz", allow_pickle=False) as archive:
        observations = {name: archive[name].copy() for name in archive.files}
    grams = np.load(directory / "gram.npy", mmap_mode="r", allow_pickle=False)
    if grams.shape != (206, 2, 144, 144):
        raise AssertionError("Archived Gram schedule is incomplete")
    return record, observations, grams, {
        "directory": str(directory.relative_to(common.ROOT)),
        "record_sha256": common.sha(record_path),
        "observations_sha256": common.sha(directory / "observations.npz"),
        "gram_sha256": common.sha(directory / "gram.npy"),
    }


def save_checkpoint(path, state, data):
    if path.exists():
        raise FileExistsError("Refusing to replace an existing actual-state checkpoint")
    temporary = path.with_suffix(path.suffix + ".tmp")
    solver.save_restart(temporary, state, data)
    restored, restored_data = solver.load_restart(temporary)
    for name in ARRAY_NAMES:
        np.testing.assert_array_equal(getattr(restored, name), getattr(state, name))
    for name in ("inputs", "labels", "probabilities"):
        np.testing.assert_array_equal(getattr(restored_data, name), getattr(data, name))
    if base.fixed_signature(restored, restored_data) != base.fixed_signature(state, data):
        raise AssertionError("Checkpoint roundtrip changed frozen metadata or arrays")
    temporary.replace(path)
    return common.sha(path)


def run_configuration(output, name, target):
    output = Path(output).resolve()
    manifest = common.load_manifest(output)
    if common.sha(common.PLAN) != PLAN_SHA256 or manifest["plan_sha256"] != PLAN_SHA256:
        raise AssertionError("Frozen long-horizon plan hash mismatch")
    if manifest["closure_configs"] != arc.configurations():
        raise AssertionError("Long-horizon closure menu differs from ARC30")
    config = next(c for c in arc.configurations() if c["id"] == name)
    if target not in common.STAGES:
        raise ValueError("Target is not a declared common stage")
    source = Path(manifest["source_run"]).resolve()
    if source != common.SOURCE.resolve():
        raise AssertionError("Source run differs from the frozen ARC30 archive")
    instants = common.stage_times(target)
    bootstrap = target == 40
    step = Fraction(config["step"]) if bootstrap else Fraction(1, 40 if config["kind"] == "time_control" else 20)
    start_time = Fraction(0 if bootstrap else target // 2)
    if len(instants) != (206 if bootstrap else 21) or instants[0] != start_time or instants[-1] != target:
        raise AssertionError("Invalid stage observation schedule")
    if any((instant / step).denominator != 1 for instant in instants):
        raise AssertionError("Stage observation times are not on the frozen Heun mesh")
    directory = common.stage_directory(output, "closure", name, target)
    directory.mkdir(parents=True, exist_ok=False)
    started, cpu_started = time.monotonic(), time.process_time()
    rows, saved_times = [], []
    mapped = None
    record = dict(format="long-20260914-closure-stage-v1", status="running", configuration=config,
                  name=name, family="closure", target=target, from_time=float(start_time),
                  time_fractions=[str(t) for t in instants], step_size=str(step),
                  steps_requested=int((Fraction(target) - start_time) / step), steps_completed=0,
                  completed_observations=0, source_hashes=source_hashes(), plan_sha256=PLAN_SHA256,
                  inputs_sha256=manifest["inputs_sha256"], inputs_json_sha256=common.sha(output / "inputs.json"),
                  command=sys.argv, created_utc=datetime.now(timezone.utc).isoformat(),
                  python=sys.version, numpy=np.__version__, platform=platform.platform(),
                  thread_environment={key: os.environ.get(key) for key in base.THREAD_KEYS},
                  observation_semantics="Passive observations at exact fixed-Heun nodes; original initial marks retained.",
                  checkpoint_semantics="Exact actual state and DataLaw; loaded from immediately preceding endpoint.",
                  source_run=str(source), loss_increases=[], maximum_gate_errors={},
                  prior_checkpoint_sha256=None, validation=dict(passed=False),
                  phase_seconds=dict(initialization=0., evolution=0., observation=0., checkpoint=0.))
    common.write(directory / "record.json", record)
    try:
        common.guard_budget(output, started)
        arrays, input_metadata = load_inputs(output, manifest)
        previous_record, previous_observations, previous_grams = None, None, None
        old_record, old_observations, old_grams = None, None, None
        phase = time.monotonic()
        if bootstrap:
            old_record, old_observations, old_grams, provenance = archived_evidence(source, config)
            record["archived_replay_evidence"] = provenance
            np.testing.assert_array_equal(old_observations["times"], np.asarray([float(t) for t in instants]))
            state = solver.initialize(config["order"], initialization_nodes=config["initialization_nodes"],
                                      population_nodes=config["population_nodes"], digits=None,
                                      backend="decimal", epsilon_cov="0.001")
            data = solver.DataLaw(*(arrays["arcs30_" + key].copy() for key in ("inputs", "labels", "probabilities")),
                                  input_metadata["cases"]["arcs30"]["law_metadata"]).validate(state.arithmetic)
            hashes = initial_hashes(state)
            if hashes != old_record["initialization_array_sha256"]:
                raise AssertionError("Fresh initialized closure arrays do not match ARC30 hashes")
            if not (np.array_equal(state.w, state.g) and np.array_equal(state.M, state.D)
                    and np.array_equal(state.c, np.zeros_like(state.c))):
                raise AssertionError("Fresh closure initialization contract failed")
            record["initialization_array_sha256"] = hashes
            record["replay_check"] = dict(status="running", absolute_tolerance=REPLAY_ATOL,
                                         relative_tolerance=REPLAY_RTOL, compared_observations=0,
                                         maximum_absolute_error=0., per_field_errors={}, gram_maximum_absolute_error=0.)
            record["replay"] = record["replay_check"]
            record["replay"]["passed"] = False
        else:
            previous_directory = common.stage_directory(output, "closure", name, target // 2)
            previous_record_path = previous_directory / "record.json"
            previous_record = json.loads(previous_record_path.read_text())
            if (previous_record["status"] != "complete" or previous_record["target"] != target // 2
                    or previous_record["configuration"] != config
                    or previous_record["source_hashes"] != record["source_hashes"]
                    or previous_record["inputs_sha256"] != record["inputs_sha256"]):
                raise AssertionError("Immediately preceding stage is not a matching complete state")
            prior = previous_directory / "checkpoint.json"
            if common.sha(prior) != previous_record["checkpoint_sha256"]:
                raise AssertionError("Prior actual-state checkpoint hash mismatch")
            for filename, key in (("observations.npz", "observations_sha256"), ("gram.npy", "gram_sha256")):
                if common.sha(previous_directory / filename) != previous_record[key]:
                    raise AssertionError("Prior endpoint observation hash mismatch: " + filename)
            state, data = solver.load_restart(prior)
            record["prior_checkpoint"] = dict(path=str(prior.relative_to(common.ROOT)),
                                              sha256=common.sha(prior), time=target // 2,
                                              prior_record_sha256=common.sha(previous_record_path))
            record["prior_checkpoint_sha256"] = record["prior_checkpoint"]["sha256"]
            record["initialization_array_sha256"] = previous_record["initialization_array_sha256"]
            with np.load(previous_directory / "observations.npz", allow_pickle=False) as archive:
                previous_observations = {key: archive[key][-1].copy() for key in archive.files if key != "times"}
            previous_grams = np.load(previous_directory / "gram.npy", mmap_mode="r", allow_pickle=False)[-1]
        for key in ("inputs", "labels", "probabilities"):
            np.testing.assert_array_equal(getattr(data, key), arrays["arcs30_" + key])
        if data.metadata != input_metadata["cases"]["arcs30"]["law_metadata"]:
            raise AssertionError("Checkpoint DataLaw metadata differs from prepared inputs")
        record["phase_seconds"]["initialization"] = time.monotonic() - phase
        frozen = base.fixed_signature(state, data)
        expected_frozen = old_record["fixed_signature_initial"] if bootstrap else previous_record["fixed_signature_final"]
        if frozen != expected_frozen:
            raise AssertionError("Frozen marks or DataLaw differ from predecessor")
        record["fixed_signature_initial"] = frozen
        record["state_bytes"] = solver.state_bytes(state)
        shape = (len(instants), 2, 144, 144)
        mapped = np.lib.format.open_memmap(directory / "gram.npy", mode="w+", dtype=np.float64, shape=shape)
        mapped[:] = np.nan
        mapped.flush()
        record["gram_shape"] = list(shape)
        previous_time = start_time
        for index, instant in enumerate(instants):
            common.guard_budget(output, started)
            phase = time.monotonic()
            steps = int((instant - previous_time) / step)
            if steps:
                state = solver.evolve(state, data, steps=steps, step_size=step, block_size=base.BLOCK_SIZE)
            record["phase_seconds"]["evolution"] += time.monotonic() - phase
            record["steps_completed"] += steps
            previous_time = instant
            common.guard_budget(output, started)
            phase = time.monotonic()
            row, _ = base.collect(state, data, arrays["circle"])
            observed, _ = gram.gram_observation(state, data, arrays["circle"], row)
            gates = validate_observation(row, observed, data, endpoint=index == len(instants) - 1)
            for key, value in gates.items():
                if key == "endpoint_minimum_eigenvalue":
                    record[key] = value
                else:
                    record["maximum_gate_errors"][key] = max(value, record["maximum_gate_errors"].get(key, 0.))
            if bootstrap:
                if set(old_observations) != set(row) | {"times"}:
                    raise AssertionError("Replay observation fields differ from the archive")
                replay = record["replay_check"]
                for key, value in row.items():
                    error = compare_arrays(value, old_observations[key][index], f"bootstrap {instant} {key}")
                    replay["per_field_errors"][key] = max(error, replay["per_field_errors"].get(key, 0.))
                error = compare_arrays(observed, old_grams[index], f"bootstrap {instant} Gram")
                replay["gram_maximum_absolute_error"] = max(error, replay["gram_maximum_absolute_error"])
                replay["maximum_absolute_error"] = max(replay["gram_maximum_absolute_error"], *replay["per_field_errors"].values())
                replay["compared_observations"] = index + 1
            elif index == 0:
                if set(previous_observations) != set(row):
                    raise AssertionError("Predecessor observation fields differ")
                errors = {key: compare_arrays(value, previous_observations[key], "checkpoint " + key,
                                              atol=0., rtol=0.) for key, value in row.items()}
                errors["gram"] = compare_arrays(observed, previous_grams, "checkpoint Gram", atol=0., rtol=0.)
                record["checkpoint_continuity"] = dict(status="passed", exact_equality=True,
                                                       per_field_maximum_absolute_error=errors)
            # Preserve a failing loss observation before raising its numerical gate.
            prior_loss = float(rows[-1]["loss"]) if rows else None
            rows.append(row)
            saved_times.append(instant)
            mapped[index] = observed
            mapped.flush()
            record["completed_observations"] = len(rows)
            record["last_time"] = str(instant)
            record["phase_seconds"]["observation"] += time.monotonic() - phase
            if prior_loss is not None:
                increase = float(row["loss"]) - prior_loss
                if increase > 0:
                    record["loss_increases"].append(dict(time=str(instant), previous=prior_loss,
                                                         current=float(row["loss"]), increase=increase))
                check_loss_change(prior_loss, float(row["loss"]))
            if len(rows) % 10 == 0 or index == len(instants) - 1:
                base.save_rows(directory / "observations.npz", saved_times, rows)
                common.write(directory / "record.json", record)
        record["fixed_signature_final"] = base.fixed_signature(state, data)
        record["fixed_marks_verified"] = frozen == record["fixed_signature_final"]
        if not record["fixed_marks_verified"]:
            raise AssertionError("Frozen closure marks or DataLaw changed during evolution")
        if record["steps_completed"] != record["steps_requested"]:
            raise AssertionError("Completed Heun count differs from requested count")
        common.guard_budget(output, started)
        phase = time.monotonic()
        record["checkpoint_sha256"] = save_checkpoint(directory / "checkpoint.json", state, data)
        record["checkpoint_file"] = "checkpoint.json"
        record["phase_seconds"]["checkpoint"] = time.monotonic() - phase
        if bootstrap:
            record["replay_check"].update(status="passed", passed=True,
                                          exact_equality=record["replay_check"]["maximum_absolute_error"] == 0.)
        record["validation"] = dict(passed=True, maximum_gate_errors=record["maximum_gate_errors"],
                                    endpoint_minimum_eigenvalue=record["endpoint_minimum_eigenvalue"],
                                    fixed_marks_verified=record["fixed_marks_verified"],
                                    checkpoint_exact_roundtrip=True)
        record["status"] = "complete"
    except Exception as exc:
        record.update(status="failure", error=repr(exc), traceback=traceback.format_exc())
    finally:
        if mapped is not None:
            mapped.flush()
            record["gram_sha256"] = common.sha(directory / "gram.npy")
        base.save_rows(directory / "observations.npz", saved_times, rows)
        if (directory / "observations.npz").exists():
            record["observations_sha256"] = common.sha(directory / "observations.npz")
        record["wall_seconds"] = time.monotonic() - started
        record["cpu_seconds"] = time.process_time() - cpu_started
        record["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        record["gram_completed_observations"] = len(rows)
        record["completed_utc"] = datetime.now(timezone.utc).isoformat()
        common.write(directory / "record.json", record)
    print(json.dumps({key: record.get(key) for key in ("name", "target", "status", "wall_seconds", "error")}), flush=True)
    return 0 if record["status"] == "complete" else 1


def verification():
    """Deterministic non-scientific checks; no closure initializer or trajectory."""
    fixture = gram.verification()
    assert len(common.stage_times(40)) == 206
    for target in common.STAGES:
        instants = common.stage_times(target)
        for step in ((Fraction(1, 200), Fraction(1, 400)) if target == 40
                     else (Fraction(1, 20), Fraction(1, 40))):
            assert all((instant / step).denominator == 1 for instant in instants)
        if target > 40:
            assert len(instants) == 21 and instants[0] == target / 2 and instants[-1] == target
    assert compare_arrays(np.asarray([1., 2.]), np.asarray([1., 2.]), "equal") == 0
    assert compare_arrays(np.asarray([1. + 1e-10]), np.asarray([1.]), "tolerated") > 0
    for function in (lambda: compare_arrays(np.asarray([1.1]), np.asarray([1.]), "mismatch"),
                     lambda: compare_arrays(np.asarray([np.nan]), np.asarray([1.]), "nan"),
                     lambda: check_loss_change(.1, .2)):
        try:
            function()
        except (AssertionError, FloatingPointError):
            pass
        else:
            raise AssertionError("Expected numerical rejection was not raised")
    return dict(status="passed", inherited_gram_fixture=fixture, fixed_mesh_stage_schedule=True,
                replay_comparison_positive_and_negative_checks=True, loss_increase_gate=True,
                scientific_trajectories=0, source_hashes=source_hashes())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--run-id", choices=[c["id"] for c in arc.configurations()])
    parser.add_argument("--target", type=int, choices=common.STAGES)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if args.verify_only:
        print(json.dumps(verification(), indent=2), flush=True)
        return 0
    if args.output is None or args.run_id is None or args.target is None:
        parser.error("A stage worker requires --output, --run-id, and --target")
    return run_configuration(args.output, args.run_id, args.target)


if __name__ == "__main__":
    raise SystemExit(main())
