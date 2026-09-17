"""Independent saved-network verification; no optimizer or training is run.

Read only this study's named campaign and the maintained finite reference.
Use one CPU thread and at most 60 CPU seconds. Full-circle replay is selected
only when a fixed 64-column matrix evaluation estimates under 30 CPU seconds
for all retained checkpoints; otherwise replay indices 0,10,...,1430.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "code"))
from pde import finite_network as ref


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for part in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            result.update(part)
    return result.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def predict(arrays, theta):
    """Independent float64 evaluation of the physical stored-array model."""
    W, V, c = arrays
    u = np.stack((np.cos(theta), np.sin(theta)))
    h1 = np.tanh(W @ u)
    h2 = np.tanh(V @ h1)
    return c @ h2 / c.size


def initial_digest(cfg):
    p = ref.initialize(cfg["width"], 2, 2, seed=cfg["seed"])
    result = hashlib.sha256()
    for array in (*p.weights, p.readout):
        result.update(np.asarray(array, dtype=cfg["dtype"]).tobytes())
    return result.hexdigest()


def run(campaign, output, include_wide=False):
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    started_cpu, started_wall = time.process_time(), time.monotonic()
    output.mkdir(parents=True, exist_ok=False)
    manifest = read_json(campaign / "manifest.json")
    configs = list(manifest["configs"])
    waves = ["main"]
    if include_wide:
        configs += manifest["conditional_wide"]
        waves.append("wide")
    for wave in waves:
        batch = read_json(campaign / f"{wave}_batch.json")
        require(batch["exit_codes"] == [0, 0], f"{wave}: worker exit")
        require(not batch["missing"] and batch["stop_reason"] is None,
                f"{wave}: incomplete wave")

    source_checks = {}
    for relative, expected in manifest["source_hashes"].items():
        actual = digest(ROOT / relative)
        require(actual == expected, f"source mismatch: {relative}")
        archived = campaign / "producer_sources" / Path(relative).name
        archive_hash = digest(archived) if archived.exists() else None
        if archive_hash is not None:
            require(archive_hash == expected, f"archived source mismatch: {relative}")
        source_checks[relative] = {"expected": expected, "actual": actual,
                                   "archived": archive_hash}

    by_id, initial_hashes, observations, rows = {}, {}, {}, []
    expected_main = {(d, n, s, "main") for d in (15, 30, 90)
                     for n in (1024, 4096) for s in (1729, 2718, 3141)}
    expected_main |= {(30, 4096, 1729, "half"), (30, 1024, 1729, "precision")}
    actual_main = {(c["delta"], c["width"], c["seed"], c["variant"])
                   for c in manifest["configs"]}
    require(actual_main == expected_main and len(manifest["configs"]) == 20,
            "main configuration design mismatch")
    if include_wide:
        require({(c["delta"], c["width"], c["seed"], c["variant"])
                 for c in manifest["conditional_wide"]} ==
                {(30, 8192, s, "main") for s in (1729, 2718, 3141)},
                "wide configuration design mismatch")
    theta = 2 * np.pi * np.arange(1440) / 1440
    for cfg in configs:
        name = cfg["id"]
        require(name not in by_id, "duplicate run identifier")
        by_id[name] = cfg
        directory = campaign / name
        record, local = read_json(directory / "record.json"), read_json(directory / "config.json")
        require(record["status"] == "complete", f"{name}: incomplete record")
        require(local == cfg == record["config"], f"{name}: per-seed config mismatch")
        require(record["source_hashes"] == manifest["source_hashes"], f"{name}: source mismatch")
        require(name == f"pair_d{cfg['delta']}_n{cfg['width']}_s{cfg['seed']}_{cfg['variant']}",
                f"{name}: identifier normalization mismatch")
        require(cfg["angles_degrees"] == [45 - cfg["delta"] / 2, 45 + cfg["delta"] / 2]
                and cfg["labels"] == [-1., 1.] and cfg["rotation"] == 45
                and cfg["amplitude"] == 1. and cfg["kind"] == "pair", f"{name}: data mismatch")
        require(cfg["h"] == (.01 if cfg["variant"] == "half" else .02)
                and cfg["dtype"] == ("float64" if cfg["variant"] == "precision" else "float32"),
                f"{name}: numerical configuration mismatch")
        checks = record["checks"]
        require(all(value is None or np.isfinite(value) for value in checks.values()),
                f"{name}: nonfinite recorded check")
        file_hashes = {}
        for filename, expected in record["outputs"].items():
            actual = digest(directory / filename)
            require(actual == expected, f"{name}: output hash mismatch: {filename}")
            file_hashes[filename] = actual
        with np.load(directory / "observations.npz", allow_pickle=False) as archive:
            saved = {key: archive[key] for key in archive.files}
        require(all(np.all(np.isfinite(a)) for a in saved.values()),
                f"{name}: nonfinite saved observation")
        require(np.array_equal(saved["theta"], theta), f"{name}: circle grid mismatch")
        require(saved["dense_predictions"].shape == (1440,)
                and saved["common_T100"].shape == (1440,), f"{name}: dense shape mismatch")
        count = len(saved["times"])
        require(np.array_equal(saved["times"], 10. * np.arange(count))
                and 100 <= saved["times"][-1] <= 300, f"{name}: physical clock mismatch")
        require(saved["predictions"].shape == (count, 512)
                and saved["train_predictions"].shape == (count, 2), f"{name}: observation shape mismatch")
        require(all(saved[k].shape == (2, 2) for k in
                    ("gram1_initial", "gram2_initial", "gram1_final", "gram2_final")),
                f"{name}: hidden Gram shape mismatch")
        computed_loss = np.mean((saved["train_predictions"] - np.asarray(cfg["labels"])) ** 2, axis=1)
        require(np.allclose(computed_loss, saved["loss"], rtol=0, atol=1e-14), f"{name}: loss mismatch")
        require(float(np.max(np.diff(saved["loss"]))) <= 1e-6, f"{name}: recorded loss increase")
        require(record["final_time"] == saved["times"][-1]
                and record["final_loss"] == saved["loss"][-1], f"{name}: endpoint mismatch")
        curves = saved["predictions"]
        final_scale = .002 * max(1., float(np.max(abs(curves[-1]))))
        final_gate = bool(saved["loss"][-1] <= 1e-6
                          and np.max(abs(curves[-1] - curves[-3])) <= final_scale
                          and np.max(abs(curves[-3] - curves[-5])) <= final_scale)
        require(record["settled"] == final_gate, f"{name}: settling gate mismatch")
        require(record["stop_reason"] == ("mild_settling" if final_gate else "time_cap"),
                f"{name}: stopping reason mismatch")
        if saved["times"][-1] == 100:
            require(np.array_equal(saved["dense_predictions"], saved["common_T100"]),
                    f"{name}: common-time prediction mismatch")
        tolerance = 1e-10 if cfg["dtype"] == "float64" else 2e-5
        oddness = float(np.max(abs(saved["dense_predictions"][:720] + saved["dense_predictions"][720:])))
        stop_oddness = float(np.max(abs(curves[:, :256] + curves[:, 256:])))
        require(max(oddness, stop_oddness) <= tolerance, f"{name}: odd parity mismatch")
        key = cfg["width"], cfg["seed"], cfg["dtype"]
        if key not in initial_hashes:
            initial_hashes[key] = initial_digest(cfg)
        require(initial_hashes[key] == record["initial_weight_sha256"], f"{name}: initial seed/dtype mismatch")
        require((directory / "state.npz").exists() == cfg["retain_state"], f"{name}: retention mismatch")
        observations[name] = saved
        rows.append(dict(id=name, width=cfg["width"], seed=cfg["seed"], all_observation_arrays_finite=True,
                         saved_shapes={k: list(a.shape) for k, a in saved.items()},
                         source_config_data_identity=True, initialization_digest_verified=True,
                         output_hashes=file_hashes, circle_oddness=oddness, stop_panel_oddness=stop_oddness,
                         settled=final_gate, retained_parameters_checked=False))

    retained = sorted((c for c in configs if c["retain_state"]), key=lambda c: -c["width"])
    row_by_id = {row["id"]: row for row in rows}
    indices, benchmark, estimated_seconds = None, None, None
    replay_outputs = {}
    for cfg in retained:
        name, n = cfg["id"], cfg["width"]
        with np.load(campaign / name / "state.npz", allow_pickle=False) as archive:
            require(set(archive.files) == {"W", "V", "c"}, f"{name}: state keys")
            stored = tuple(archive[key] for key in ("W", "V", "c"))
        require(tuple(a.shape for a in stored) == ((n, 2), (n, n), (n,)), f"{name}: parameter shapes")
        require(all(a.dtype == np.dtype(cfg["dtype"]) for a in stored), f"{name}: parameter dtype")
        require(all(np.all(np.isfinite(a)) for a in stored), f"{name}: nonfinite retained parameter")
        arrays = tuple(np.asarray(a, dtype=np.float64) for a in stored)
        del stored
        if indices is None:
            before = time.process_time()
            predict(arrays, theta[:64])
            benchmark = time.process_time() - before
            estimated_seconds = benchmark * (1440 / 64) * sum(c["width"] ** 2 for c in retained) / n ** 2
            indices = np.arange(1440) if estimated_seconds < 30 else np.arange(0, 1440, 10)
        before = time.process_time()
        actual = predict(arrays, theta[indices])
        expected = observations[name]["dense_predictions"][indices]
        error = float(np.max(abs(actual - expected)))
        tolerance = 1e-10 if cfg["dtype"] == "float64" else 2e-5
        require(np.all(np.isfinite(actual)) and error <= tolerance, f"{name}: CPU replay error {error}")
        # A separate maintained-reference evaluation at fixed 144 angles also
        # verifies the explicit input sqrt(2) convention and stored readout/n.
        reference_indices = np.arange(0, 1440, 10)
        reference_u = np.stack((np.cos(theta[reference_indices]), np.sin(theta[reference_indices])))
        parameters = ref.Parameters(arrays[:2], arrays[2])
        reference_prediction = ref.forward(parameters, np.sqrt(2) * reference_u).output
        direct_reference = predict(arrays, theta[reference_indices])
        reference_error = float(np.max(abs(reference_prediction - direct_reference)))
        require(reference_error <= 1e-10, f"{name}: maintained convention mismatch")
        row_by_id[name].update(retained_parameters_checked=True, all_retained_parameters_finite=True,
                              independent_cpu_replay_max_abs_error=error, replay_tolerance=tolerance,
                              maintained_reference_max_abs_error=reference_error,
                              replay_cpu_seconds=time.process_time() - before)
        replay_outputs[name] = actual
        del arrays, parameters
    cpu = time.process_time() - started_cpu
    require(cpu < 60, "CPU budget exceeded")
    result = dict(passed=True, campaign=str(campaign), configs_checked=len(configs), retained_states_checked=len(retained),
                  verifier_sha256=digest(__file__), manifest_sha256=digest(campaign / "manifest.json"),
                  source_checks=source_checks, rows=rows, replay_indices=indices.tolist(),
                  maintained_reference_indices=list(range(0, 1440, 10)), benchmark_64_cpu_seconds=benchmark,
                  estimated_full_replay_cpu_seconds=estimated_seconds, cpu_seconds=cpu,
                  wall_seconds=time.monotonic() - started_wall,
                  maximum_cpu_replay_error=max(row.get("independent_cpu_replay_max_abs_error", 0.) for row in rows),
                  maximum_oddness=max(row["circle_oddness"] for row in rows),
                  limitations=["Unretained final parameter arrays cannot be scanned or independently replayed.",
                               "This verifies saved endpoints and observations; it does not rerun training or prove every intermediate parameter state finite."],
                  environment={"numpy": np.__version__, "threads": {key: os.environ[key] for key in
                               ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}})
    np.savez_compressed(output / "independent_replay.npz", indices=indices, **replay_outputs)
    (output / "verification.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({key: result[key] for key in ("passed", "configs_checked", "retained_states_checked",
                                                "maximum_cpu_replay_error", "maximum_oddness", "cpu_seconds", "wall_seconds")}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--include-wide", action="store_true")
    args = parser.parse_args()
    run(args.campaign.resolve(), args.output.resolve(), args.include_wide)
