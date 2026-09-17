"""Immutable staged continuation of the frozen thirty-degree dense networks."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import traceback

import numpy as np
import torch

import WIDE_GPU_20260914_NETWORK as original
import GRAM_20260914_NETWORK as gram_observer
import LONG_20260914_COMMON as common


def source_hashes():
    paths = (Path(__file__), Path(common.__file__), Path(original.__file__),
             Path(gram_observer.__file__), common.PLAN)
    return {str(path.relative_to(common.ROOT)): common.sha(path) for path in paths}


def check_observation(row, gram, probabilities, dtype):
    tolerance = 2e-6 if dtype == "float32" else 2e-11
    if not all(np.isfinite(value).all() for value in row.values()):
        raise FloatingPointError("Nonfinite scalar/prediction observation")
    if gram.shape != (2, 144, 144) or not np.isfinite(gram).all():
        raise AssertionError("Invalid Gram shape or nonfinite Gram")
    if np.abs(gram).max() > 1 + 2e-11:
        raise AssertionError("Activation Gram outside tanh range")
    np.testing.assert_allclose(gram, gram.transpose(0, 2, 1), atol=2e-11, rtol=0)
    diagonal = np.diagonal(gram[:, :16, :16], axis1=1, axis2=2)
    np.testing.assert_allclose(diagonal @ probabilities, row["raw_rms"] ** 2,
                               atol=tolerance, rtol=0)
    return tolerance


def observe(state, u, y, p, circle, initial, dtype):
    versions = [value._version for value in state]
    row = original.observe(state, u, y, p, circle, initial)
    train, panel = original.fields(state, u), original.fields(state, circle)
    gram = torch.stack([
        gram_observer.gram_of(torch.cat((train[j], panel[j]), dim=1))
        for j in (1, 3)
    ]).cpu().numpy()
    if versions != [value._version for value in state]:
        raise AssertionError("Observation changed a parameter")
    probabilities, labels = p.cpu().double().numpy(), y.cpu().double().numpy()
    tolerance = check_observation(row, gram, probabilities, dtype)
    expected_loss = np.sum(probabilities * (row["data_predictions"] - labels) ** 2)
    np.testing.assert_allclose(row["loss"], expected_loss, atol=tolerance, rtol=0)
    return row, gram


def atomic_npz(path, **values):
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("xb") as stream:
        np.savez_compressed(stream, **values)
    temporary.replace(path)


def compare_arrays(current, archived, atol, rtol=1e-9):
    if set(current) != set(archived):
        raise AssertionError("Observation field names changed")
    errors = {}
    exact = True
    for key, value in current.items():
        before = np.asarray(archived[key])
        if value.shape != before.shape:
            raise AssertionError(f"Observation shape changed: {key}")
        errors[key] = float(np.max(np.abs(value - before), initial=0))
        exact = exact and np.array_equal(value, before)
        np.testing.assert_allclose(value, before, atol=atol, rtol=rtol,
                                   err_msg=f"Archived replay mismatch: {key}")
    return errors, exact


def load_checkpoint(directory, config, shared, expected_time, hashes):
    record = json.loads((directory / "record.json").read_text())
    path = directory / "checkpoint.pt"
    checkpoint_hash = common.sha(path)
    if record.get("status") != "complete" or record.get("target") != expected_time:
        raise AssertionError("Preceding stage did not complete at the required time")
    if record.get("inputs_sha256") != shared["inputs_sha256"] or record.get("plan_sha256") != shared["plan_sha256"]:
        raise AssertionError("Preceding record input/plan checksum mismatch")
    if record["checkpoint_sha256"] != checkpoint_hash:
        raise AssertionError("Preceding checkpoint checksum mismatch")
    if record["observations_sha256"] != common.sha(directory / "observations.npz"):
        raise AssertionError("Preceding observation checksum mismatch")
    if record["gram_sha256"] != common.sha(directory / "gram.npy"):
        raise AssertionError("Preceding Gram checksum mismatch")
    saved = torch.load(path, map_location="cpu", weights_only=True)
    if saved["config"] != config or saved["time"] != expected_time:
        raise AssertionError("Checkpoint configuration/time mismatch")
    if saved["source_hashes"] != hashes or record["source_hashes"] != hashes:
        raise AssertionError("Producer sources changed between stages")
    if saved["inputs_sha256"] != shared["inputs_sha256"]:
        raise AssertionError("Checkpoint input checksum mismatch")
    if saved["plan_sha256"] != shared["plan_sha256"]:
        raise AssertionError("Checkpoint plan checksum mismatch")
    n = config["width"]
    expected_shapes = ((n, 2), (n, n), (n,))
    expected_dtype = torch.float32 if config["dtype"] == "float32" else torch.float64
    if len(saved["state"]) != 3 or len(saved["initial"]) != 2:
        raise AssertionError("Checkpoint state block count mismatch")
    for array, shape in zip(saved["state"], expected_shapes):
        if tuple(array.shape) != shape or array.dtype != expected_dtype:
            raise AssertionError("Checkpoint state shape/dtype mismatch")
        if not torch.isfinite(array).all():
            raise FloatingPointError("Nonfinite checkpoint state")
    for array in saved["initial"]:
        if tuple(array.shape) != (n, 16) or array.dtype != expected_dtype:
            raise AssertionError("Checkpoint initial activation shape/dtype mismatch")
        if not torch.isfinite(array).all():
            raise FloatingPointError("Nonfinite checkpoint initial activation")
    return saved, checkpoint_hash, record


@torch.no_grad()
def worker(output, name, target):
    output = Path(output).resolve()
    shared = common.load_manifest(output)
    configs = [value for value in shared["network_configs"] if value["name"] == name]
    if len(configs) != 1 or target not in common.STAGES:
        raise ValueError("Run or target is outside the frozen menu")
    config = configs[0]
    times = np.asarray(common.stage_times(target), dtype=np.float64)
    start_time = 0.0 if target == 40 else target / 2
    if times[0] != start_time or times[-1] != target:
        raise AssertionError("Invalid frozen observation times")
    expected_count = 206 if target == 40 else 21
    if len(times) != expected_count or np.any(np.diff(times) <= 0):
        raise AssertionError("Invalid frozen observation count/order")
    directory = common.stage_directory(output, "network", name, target)
    directory.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    hashes = source_hashes()
    source = Path(shared["source_run"])
    archived = source / "network" / name
    archive_record_path = archived / "record.json"
    archive_record = json.loads(archive_record_path.read_text())
    if archive_record["status"] != "complete":
        raise AssertionError("Archived network is incomplete")
    for key, value in config.items():
        if archive_record.get(key) != value:
            raise AssertionError(f"Archived configuration mismatch: {key}")
    if archive_record["inputs_sha256"] != common.sha(source / "inputs.npz"):
        raise AssertionError("Archived input checksum mismatch")
    if shared["inputs_sha256"] != archive_record["inputs_sha256"]:
        raise AssertionError("Long-run training inputs differ from the archived inputs")
    h = config["step"] if target == 40 else (0.025 if config["kind"] == "time_control" else 0.05)
    steps = round((target - start_time) / h)
    record = dict(config, family="network", config=config, target=target,
                  start_time=start_time, status="running", step=h, actual_steps=0,
                  source_hashes=hashes, inputs_sha256=shared["inputs_sha256"],
                  plan_sha256=shared["plan_sha256"], checkpoint_file="checkpoint.pt",
                  archive_record_sha256=common.sha(archive_record_path),
                  archived_run=str(archived), command=sys.argv,
                  torch_version=torch.__version__, numpy_version=np.__version__,
                  cuda_version=torch.version.cuda, visible_device=os.environ.get("CUDA_VISIBLE_DEVICES"),
                  tf32=False, reduced_precision_accumulation=False,
                  gram_accumulation="float64", gram_panel_order="16 training, then 128 circle inputs",
                  observed_loss_increases=[], completed_observations=0,
                  gram_completed_observations=0, validation=dict(passed=False))
    common.write(directory / "record.json", record)
    rows = []
    buffer = None

    def persist():
        if rows:
            atomic_npz(directory / "observations.npz", times=times[:len(rows)],
                       **{key: np.stack([row[key] for row in rows]) for key in rows[0]})
        if buffer is not None:
            buffer.flush()
        record.update(completed_observations=len(rows), gram_completed_observations=len(rows),
                      wall_seconds=time.monotonic() - started)
        common.write(directory / "record.json", record)

    def append(state):
        row, gram = observe(state, u, y, p, circle, initial, config["dtype"])
        previous_loss = float(rows[-1]["loss"]) if rows else None
        index = len(rows)
        buffer[index] = gram
        rows.append(row)
        if previous_loss is not None and float(row["loss"]) > previous_loss:
            current_loss = float(row["loss"])
            increase = dict(time=float(times[index]), previous=previous_loss, current=current_loss,
                            increase=current_loss - previous_loss)
            record["observed_loss_increases"].append(increase)
            if current_loss - previous_loss > max(1e-4, .01 * previous_loss):
                raise FloatingPointError("Saved loss increase exceeds frozen numerical gate")

    try:
        common.guard_budget(output, started)
        dtype = original.setup(config["dtype"])
        record["gpu"] = torch.cuda.get_device_name()
        record["gpu_total_bytes"] = torch.cuda.get_device_properties(0).total_memory
        _, u, y, p, circle = original.load_inputs(output, config["case"], dtype)
        if tuple(u.shape) != (2, 16) or tuple(circle.shape) != (2, 128):
            raise AssertionError("Frozen input panel shapes changed")
        previous_directory = None
        if target == 40:
            state, initial_hashes = original.initialize(config["width"], config["seed"], dtype)
            fs = original.fields(state, u)
            initial = (fs[1].clone(), fs[3].clone())
            del fs
            record["previous_checkpoint_sha256"] = None
            record["prior_checkpoint_sha256"] = None
        else:
            previous_directory = common.stage_directory(output, "network", name, int(start_time))
            saved, previous_hash, previous_record = load_checkpoint(
                previous_directory, config, shared, start_time, hashes)
            state = tuple(value.to("cuda") for value in saved["state"])
            initial = tuple(value.to("cuda") for value in saved["initial"])
            initial_hashes = saved["initial_float64_block_hashes"]
            record["previous_checkpoint_sha256"] = previous_hash
            record["prior_checkpoint_sha256"] = previous_hash
            record["previous_record_sha256"] = common.sha(previous_directory / "record.json")
            del saved, previous_record
        record["initial_float64_block_hashes"] = initial_hashes
        if initial_hashes != archive_record["initial_float64_block_hashes"]:
            raise AssertionError("Frozen Gaussian initialization hashes changed")
        record["trainable_parameters"] = sum(value.numel() for value in state)
        buffer = np.lib.format.open_memmap(directory / "gram.npy", mode="w+", dtype=np.float64,
                                           shape=(len(times), 2, 144, 144))
        buffer[:] = np.nan
        append(state)
        if previous_directory is not None:
            with np.load(previous_directory / "observations.npz") as old:
                previous_row = {key: old[key][-1] for key in old.files if key != "times"}
            tolerance = 2e-6 if config["dtype"] == "float32" else 2e-11
            differences, exact = compare_arrays(rows[0], previous_row, tolerance)
            previous_gram = np.load(previous_directory / "gram.npy", mmap_mode="r")[-1]
            gram_difference = float(np.max(np.abs(buffer[0] - previous_gram)))
            np.testing.assert_allclose(buffer[0], previous_gram, atol=tolerance, rtol=1e-9)
            record["checkpoint_continuity"] = dict(passed=True,
                exact=bool(exact and np.array_equal(buffer[0], previous_gram)),
                scalar_maximum_differences=differences, gram_maximum_difference=gram_difference)
        index = 1
        observation_steps = None if target == 40 else np.rint((times - start_time) / h).astype(np.int64)
        if observation_steps is not None:
            np.testing.assert_allclose(start_time + observation_steps * h, times, atol=1e-10, rtol=0)
        for k in range(1, steps + 1):
            old = state
            state = original.heun(old, u, y, p, h)
            record["actual_steps"] = k
            record["last_time"] = start_time + k * h
            if target == 40:
                # Match the archived driver operation for operation, including t=.005 interpolation.
                while index < len(times) and times[index] <= k * h + 1e-10:
                    fraction = (times[index] - (k - 1) * h) / h
                    observed = state if fraction >= 1 - 1e-9 else tuple(
                        a + fraction * (b - a) for a, b in zip(old, state))
                    append(observed)
                    index += 1
            elif index < len(times) and k == observation_steps[index]:
                append(state)
                index += 1
            if k % 500 == 0:
                common.guard_budget(output, started)
                if torch.cuda.max_memory_allocated() > 18 * 1024 ** 3:
                    raise MemoryError("Frozen per-worker GPU allocation cap exceeded")
                persist()
                print(json.dumps(dict(name=name, target=target, time=record["last_time"],
                                      loss=float(rows[-1]["loss"]), wall_seconds=record["wall_seconds"])), flush=True)
        if len(rows) != len(times) or index != len(times):
            raise AssertionError("Incomplete stage observations")
        eigenvalues = np.linalg.eigvalsh(buffer[-1])
        record["endpoint_minimum_gram_eigenvalues"] = eigenvalues[:, 0].tolist()
        if eigenvalues.min() < -2e-11:
            raise AssertionError("Endpoint activation Gram fails PSD tolerance")
        if target == 40:
            if archive_record["observations_sha256"] != common.sha(archived / "observations.npz"):
                raise AssertionError("Archived observation checksum mismatch")
            if archive_record["gram_sha256"] != common.sha(archived / "gram.npy"):
                raise AssertionError("Archived Gram checksum mismatch")
            current = dict(times=times, **{key: np.stack([row[key] for row in rows]) for key in rows[0]})
            atol = 2e-6 if config["dtype"] == "float32" else 2e-11
            with np.load(archived / "observations.npz") as old:
                old_values = dict(old)
                errors = {key: float(np.max(np.abs(value - old_values[key])))
                          for key, value in current.items()}
                exact = all(np.array_equal(value, old_values[key]) for key, value in current.items())
                old_gram = np.load(archived / "gram.npy", mmap_mode="r")
                gram_error = float(np.max(np.abs(buffer - old_gram)))
                record["replay"] = dict(passed=False, absolute_tolerance=atol, relative_tolerance=1e-9,
                    scalar_maximum_differences=errors, gram_maximum_difference=gram_error,
                    exact=bool(exact and np.array_equal(buffer, old_gram)),
                    observations_sha256=common.sha(archived / "observations.npz"),
                    gram_sha256=common.sha(archived / "gram.npy"))
                compare_arrays(current, old_values, atol)
                np.testing.assert_allclose(buffer, old_gram, atol=atol, rtol=1e-9)
                record["replay"]["passed"] = True
        common.guard_budget(output, started)
        checkpoint = dict(time=float(target), config=config, source_hashes=hashes,
                          inputs_sha256=shared["inputs_sha256"],
                          plan_sha256=shared["plan_sha256"],
                          initial_float64_block_hashes=initial_hashes,
                          state=tuple(value.cpu() for value in state),
                          initial=tuple(value.cpu() for value in initial),
                          previous_checkpoint_sha256=record["previous_checkpoint_sha256"])
        checkpoint_path = directory / "checkpoint.pt"
        temporary = checkpoint_path.with_suffix(".pt.tmp")
        with temporary.open("xb") as stream:
            torch.save(checkpoint, stream)
        temporary.replace(checkpoint_path)
        del checkpoint
        common.guard_budget(output, started)
        torch.cuda.synchronize()
        record.update(checkpoint_sha256=common.sha(checkpoint_path),
                      peak_allocated_bytes=torch.cuda.max_memory_allocated(),
                      final_loss=float(rows[-1]["loss"]), completed_at_epoch=time.time(),
                      validation=dict(passed=True, shapes_times_counts=True, finite=True,
                          gram_symmetry_range=True, weighted_training_diagonal=True,
                          loss_from_predictions=True, endpoint_gram_psd=True,
                          frozen_initialization=True, passive_observation=True,
                          loss_increase_gate=True))
        persist()
        record.update(status="complete", observations_sha256=common.sha(directory / "observations.npz"),
                      gram_sha256=common.sha(directory / "gram.npy"))
        common.write(directory / "record.json", record)
        print(json.dumps(record), flush=True)
    except BaseException:
        record.update(status="failed", error=traceback.format_exc())
        persist()
        raise


def fixture():
    """Small deterministic observer/checkpoint checks; no scientific trajectory."""
    rng = np.random.default_rng(1871)
    checks = []
    for dtype in (torch.float32, torch.float64):
        n = 7
        state = tuple(torch.tensor(value, dtype=dtype) for value in (
            rng.normal(size=(n, 2)), rng.normal(size=(n, n)) / np.sqrt(n), rng.normal(size=n) / n))
        u = torch.tensor(rng.normal(size=(2, 16)), dtype=dtype)
        y = torch.tensor(np.tile((-1., 1.), 8), dtype=dtype)
        p = torch.full((16,), 1 / 16, dtype=dtype)
        circle = torch.tensor(rng.normal(size=(2, 128)), dtype=dtype)
        fs = original.fields(state, u)
        initial = fs[1].clone(), fs[3].clone()
        with torch.no_grad():
            row, gram = observe(state, u, y, p, circle, initial, str(dtype).split(".")[-1])
        np.testing.assert_array_equal(row["motion_rms"], np.zeros(2))
        minimum = float(np.linalg.eigvalsh(gram).min())
        if minimum < -2e-11:
            raise AssertionError("Fixture Gram failed PSD")
        differences, exact = compare_arrays(row, row, 0, 0)
        assert exact and max(differences.values()) == 0
        config = dict(width=n, dtype=str(dtype).split(".")[-1], name="fixture")
        shared = dict(inputs_sha256="fixture_inputs", plan_sha256="fixture_plan")
        with tempfile.TemporaryDirectory(prefix="long_network_fixture_") as temporary:
            directory = Path(temporary)
            saved = dict(config=config, time=40., source_hashes={}, **shared,
                         state=state, initial=initial)
            torch.save(saved, directory / "checkpoint.pt")
            atomic_npz(directory / "observations.npz", times=np.array([40.]),
                       **{key: np.asarray(value)[None] for key, value in row.items()})
            np.save(directory / "gram.npy", gram[None])
            record = dict(status="complete", target=40, source_hashes={}, **shared,
                          checkpoint_sha256=common.sha(directory / "checkpoint.pt"),
                          observations_sha256=common.sha(directory / "observations.npz"),
                          gram_sha256=common.sha(directory / "gram.npy"))
            common.write(directory / "record.json", record)
            restored, _, _ = load_checkpoint(directory, config, shared, 40., {})
            for value, recovered in zip(state + initial, restored["state"] + restored["initial"]):
                torch.testing.assert_close(value, recovered, atol=0, rtol=0)
            record["checkpoint_sha256"] = "deliberately_wrong_fixture_hash"
            common.write(directory / "record.json", record)
            try:
                load_checkpoint(directory, config, shared, 40., {})
            except AssertionError as error:
                assert str(error) == "Preceding checkpoint checksum mismatch"
            else:
                raise AssertionError("Corrupt checkpoint hash was accepted")
        checks.append(dict(dtype=str(dtype), minimum_gram_eigenvalue=minimum,
                           observer_passive=True, weighted_moments=True, prediction_loss=True,
                           checkpoint_roundtrip_exact=True, checkpoint_corruption_rejected=True))
    return dict(status="passed", checks=checks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--target", type=int, required=True)
    args = parser.parse_args()
    worker(args.output, args.run_id, args.target)
