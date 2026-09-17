"""Fresh, bounded H4 closure curves for the frozen wide-network comparison.

The study-owned input specification supplies the frozen working data and output
panel. Historical archive paths are provenance only and are never opened.
Every trajectory calls the maintained initializer afresh; legacy H4 archive
comparisons are retained in the original evidence and are not rerun here.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time
import traceback


THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
for _key in THREAD_KEYS:
    os.environ[_key] = "1"
os.environ["OMP_DYNAMIC"] = "FALSE"
os.environ["MKL_DYNAMIC"] = "FALSE"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde import observable_solver as solver

PLAN = Path(__file__).with_name("WIDE_GPU_20260914_PLAN.md")
INPUT_SPECIFICATION = Path(__file__).with_name("WIDE_GPU_20260914_INPUTS.json")
CASES = ("axis", "arcs")
H = Fraction(1, 200)
BLOCK_SIZE = 16
RUN_WALL_CAP = 300.0
CAMPAIGN_WALL_CAP = 1200.0


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def atomic_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def array_hash(array):
    array = np.ascontiguousarray(array, dtype=np.float64)
    return canonical_hash({"shape": list(array.shape), "values":
                           [float(value).hex() for value in array.flat]})


def exact_array(array):
    array = np.asarray(array, dtype=np.float64)
    return {"shape": list(array.shape),
            "values": [float(value).hex() for value in array.flat]}


def decode_array(record):
    if set(record) != {"shape", "values"}:
        raise ValueError("unsupported frozen array schema")
    shape = record["shape"]
    if any(type(size) is not int or size < 0 for size in shape):
        raise ValueError("invalid frozen shape")
    array = np.asarray([float.fromhex(value) for value in record["values"]],
                       dtype=np.float64).reshape(shape)
    if not np.isfinite(array).all():
        raise ValueError("nonfinite frozen array")
    return array


def observation_times():
    return sorted({Fraction(value) for value in ("0", "0.005", "0.01", "0.02", "0.05", "0.1")}
                  | {Fraction(index, 5) for index in range(1, 201)})


def source_hashes():
    paths = [Path(__file__), PLAN, INPUT_SPECIFICATION, ROOT / "code/README.md",
             ROOT / "code/pde/__init__.py", *sorted((ROOT / "code/pde").glob("observable_*.py"))]
    return {str(path.relative_to(ROOT)): digest(path) for path in paths}


def git_metadata():
    result = {}
    for key, args in (("head", ["rev-parse", "HEAD"]),
                      ("dirty_paths", ["status", "--porcelain=v1", "--untracked-files=all"])):
        process = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
        result[key] = process.stdout.strip() if process.returncode == 0 else None
    return result


def read_input_specification():
    specification = json.loads(INPUT_SPECIFICATION.read_text())
    if specification.get("format") != "wide-gpu-20260914-inputs-v1":
        raise ValueError("unsupported frozen input specification")
    if specification["plan_sha256"] != digest(PLAN):
        raise ValueError("input specification belongs to another frozen plan")
    if set(specification["cases"]) != set(CASES):
        raise ValueError("frozen input case mismatch")
    names = {"times", "circle"} | {
        case + "_" + name for case in CASES for name in ("inputs", "labels", "probabilities")}
    if (set(specification["exact_arrays"]) != names
            or set(specification["array_sha256"]) != names):
        raise ValueError("frozen input key mismatch")
    arrays = {name: decode_array(value) for name, value in specification["exact_arrays"].items()}
    for name, value in arrays.items():
        if array_hash(value) != specification["array_sha256"][name]:
            raise ValueError("frozen array checksum mismatch: " + name)
    times = observation_times()
    if (specification["time_fractions"] != [str(t) for t in times]
            or not np.array_equal(arrays["times"], np.asarray([float(t) for t in times]))):
        raise ValueError("frozen input observation schedule mismatch")
    for case, count in (("axis", 2), ("arcs", 16)):
        if arrays[case + "_inputs"].shape != (count, 2):
            raise ValueError("wrong frozen data shape: " + case)
        solver.DataLaw(*(arrays[case + "_" + name].copy()
                         for name in ("inputs", "labels", "probabilities")),
                       specification["cases"][case]["law_metadata"]).validate(solver.Arithmetic())
    circle = arrays["circle"]
    if circle.shape != (128, 2) or np.any(np.abs(np.sum(circle * circle, axis=1) - 1) > 2e-12):
        raise ValueError("wrong frozen circle panel shape or normalization")
    return arrays, specification


def prepare_inputs(output):
    output.mkdir(parents=True, exist_ok=True)
    if (output / "inputs.npz").exists() or (output / "inputs.json").exists():
        raise FileExistsError("shared inputs already exist; refusing to replace them")
    arrays, specification = read_input_specification()
    metadata = {"format": "wide-gpu-20260914-inputs-v1", "created_utc":
                datetime.now(timezone.utc).isoformat(), "plan_sha256": digest(PLAN),
                "producer_sha256": digest(__file__), "cases": specification["cases"],
                "input_specification_path": str(INPUT_SPECIFICATION.relative_to(ROOT)),
                "input_specification_sha256": digest(INPUT_SPECIFICATION),
                "historical_input_provenance": {
                    key: specification[key] for key in ("created_utc", "producer_sha256", "npz_sha256")},
                "case_provenance_scope": "Original case paths and hashes are historical provenance only; no source archive is opened.",
                "time_fractions": [str(t) for t in observation_times()],
                "input_convention": "All inputs and circle contain normalized u=x/sqrt(2), rows are samples."}
    metadata["array_sha256"] = {name: array_hash(value) for name, value in arrays.items()}
    metadata["exact_arrays"] = {name: exact_array(value) for name, value in arrays.items()}
    with (output / "inputs.npz").open("xb") as stream:
        np.savez_compressed(stream, **arrays)
    metadata["npz_sha256"] = digest(output / "inputs.npz")
    with (output / "inputs.json").open("x") as stream:
        json.dump(metadata, stream, indent=2, allow_nan=False)
        stream.write("\n")
    return metadata


def load_inputs(output):
    metadata = json.loads((output / "inputs.json").read_text())
    if metadata["plan_sha256"] != digest(PLAN):
        raise ValueError("prepared inputs belong to another frozen plan")
    if metadata["npz_sha256"] != digest(output / "inputs.npz"):
        raise ValueError("shared NPZ checksum mismatch")
    with np.load(output / "inputs.npz", allow_pickle=False) as archive:
        arrays = {name: archive[name].copy() for name in archive.files}
    if set(arrays) != set(metadata["array_sha256"]):
        raise ValueError("shared input key mismatch")
    for name, value in arrays.items():
        if array_hash(value) != metadata["array_sha256"][name]:
            raise ValueError("shared array checksum mismatch: " + name)
    if metadata["time_fractions"] != [str(t) for t in observation_times()]:
        raise ValueError("shared observation schedule differs from the frozen schedule")
    return arrays, metadata


def configurations():
    result = []
    for case in CASES:
        for order in (1, 3, 5):
            result.append(dict(id=f"{case}_N{order}", case=case, order=order,
                               initialization_nodes=1024, population_nodes=512, refined=False))
    for case in CASES:
        result.append(dict(id=f"{case}_N3_refined", case=case, order=3,
                           initialization_nodes=2048, population_nodes=1024, refined=True))
    return result


def pair_statistics(pairs, first_weights, second_weights, input_weights):
    """Scalar second/cross moments and direct squared paired displacement."""
    initial, current, cross, motion = [], [], [], []
    for values, weights in zip(pairs, (first_weights, second_weights)):
        left, right = values[:, :, 0], values[:, :, 1]
        initial.append(float(weights @ (left * left) @ input_weights))
        current.append(float(weights @ (right * right) @ input_weights))
        cross.append(float(weights @ (left * right) @ input_weights))
        motion.append(float(weights @ ((right - left) ** 2) @ input_weights))
    initial, current, cross, motion = map(np.asarray, (initial, current, cross, motion))
    if not np.allclose(motion, current + initial - 2 * cross, rtol=1e-11, atol=2e-13):
        raise AssertionError("paired moment identity failed")
    return dict(initial_second_moments=initial, second_moments=current, cross_moments=cross,
                motion_second_moments=motion, raw_rms=np.sqrt(current), motion_rms=np.sqrt(motion))


def collect(state, data, circle):
    paired = solver.paired_observations(state, data, block_size=BLOCK_SIZE)
    statistics = pair_statistics((paired["first_pairs"], paired["second_pairs"]),
                                 paired["first_weights"], paired["second_weights"], paired["input_weights"])
    maintained_motion = np.asarray([paired["rms1"], paired["rms2"]])
    if not np.allclose(statistics["motion_rms"], maintained_motion, atol=2e-13, rtol=1e-11):
        raise AssertionError("independent paired RMS differs from maintained observation")
    statistics["motion_rms"] = maintained_motion
    predictions = solver.predict(state, circle, block_size=BLOCK_SIZE)
    data_predictions = solver.predict(state, data.inputs, block_size=BLOCK_SIZE)
    residual = data_predictions - data.labels
    row = dict(**statistics, loss=np.asarray(data.probabilities @ (residual * residual)),
               mean_prediction=np.asarray(data.probabilities @ data_predictions),
               predictions=predictions, data_predictions=data_predictions)
    if not all(np.isfinite(value).all() for value in row.values()):
        raise ValueError("nonfinite observation")
    return row, paired


def fixed_signature(state, data):
    fields = {name: array_hash(getattr(state, name)) for name in ("b1", "g", "p1", "b2", "p2", "D")}
    fields.update({"data_" + name: array_hash(getattr(data, name)) for name in ("inputs", "labels", "probabilities")})
    fields["state_metadata"] = canonical_hash(state.metadata)
    fields["data_metadata"] = canonical_hash(data.metadata)
    return fields


def save_rows(path, times, rows):
    if not rows:
        return
    arrays = {name: np.stack([row[name] for row in rows]) for name in rows[0]}
    arrays["times"] = np.asarray([float(t) for t in times])
    temporary = path.with_suffix(".npz.tmp")
    with temporary.open("wb") as stream:
        np.savez_compressed(stream, **arrays)
    temporary.replace(path)


def run_configuration(output, config):
    directory = output / "closure" / config["id"]
    directory.mkdir(parents=True, exist_ok=True)
    record_path = directory / "record.json"
    if record_path.exists():
        raise FileExistsError("refusing to repeat existing configuration")
    wall_start, cpu_start = time.perf_counter(), time.process_time()
    record = dict(format="wide-gpu-20260914-closure-v1", configuration=config,
                  configuration_sha256=canonical_hash(config), status="running", command=sys.argv,
                  created_utc=datetime.now(timezone.utc).isoformat(), source_hashes=source_hashes(),
                  git=git_metadata(), python=sys.version, numpy=np.__version__, platform=platform.platform(),
                  thread_environment={key: os.environ.get(key) for key in THREAD_KEYS},
                  step_size=str(H), steps=8000, block_size=BLOCK_SIZE,
                  original_comparisons=[], loss_increases=[], completed_observations=0,
                  matching_original_run=None,
                  original_comparison_status="not_rerun_after_study_relocation",
                  original_comparison_scope="Legacy H4 archive comparisons remain in the original run evidence; this run does not read or compare those archives.",
                  loss_increase_threshold="next > previous + 1e-7 + 1e-5*abs(previous)",
                  phase_seconds=dict(initialization=0.0, evolution=0.0, observation=0.0),
                  observation_semantics="Additional observations only split evolve calls at unchanged Heun nodes; fields and reduction grouping may differ at floating roundoff. No observations feed evolution.",
                  moment_semantics="Population and data weighted activation moments; cross is own initial/current product; second/current, initial_second/initial; direct squared motion avoids cancellation.")
    rows, saved_times = [], []
    atomic_json(record_path, record)
    try:
        arrays, shared = load_inputs(output)
        record["inputs_npz_sha256"] = shared["npz_sha256"]
        record["inputs_json_sha256"] = digest(output / "inputs.json")
        record["archive_input_provenance"] = shared["cases"][config["case"]]
        record["archive_input_provenance_scope"] = "Historical case provenance only; source paths are not opened."
        record["input_specification_sha256"] = shared.get("input_specification_sha256")
        phase = time.perf_counter()
        state = solver.initialize(config["order"], initialization_nodes=config["initialization_nodes"],
                                  population_nodes=config["population_nodes"], digits=None,
                                  backend="decimal", epsilon_cov="0.001")
        case = config["case"]
        data = solver.DataLaw(*(arrays[case + "_" + name].copy() for name in ("inputs", "labels", "probabilities")),
                              shared["cases"][case]["law_metadata"]).validate(state.arithmetic)
        circle = arrays["circle"].copy()
        record["phase_seconds"]["initialization"] = time.perf_counter() - phase
        record["initialization_metadata"] = state.metadata
        record["state_bytes"] = solver.state_bytes(state)
        frozen = fixed_signature(state, data)
        record["fixed_signature_initial"] = frozen
        previous_index = 0
        for instant in observation_times():
            if time.perf_counter() - wall_start > RUN_WALL_CAP:
                raise TimeoutError("closure worker wall cap reached")
            coordinate = instant / H
            if coordinate.denominator != 1:
                raise AssertionError("frozen closure observation schedule must lie on its Heun mesh")
            index = int(coordinate)
            phase = time.perf_counter()
            if index > previous_index:
                state = solver.evolve(state, data, steps=index - previous_index,
                                      step_size=H, block_size=BLOCK_SIZE)
            record["phase_seconds"]["evolution"] += time.perf_counter() - phase
            previous_index = index
            phase = time.perf_counter()
            row, paired = collect(state, data, circle)
            if rows:
                before, after = float(rows[-1]["loss"]), float(row["loss"])
                if after > before + 1e-7 + 1e-5 * abs(before):
                    record["loss_increases"].append(dict(time=str(instant), previous=before, current=after))
            rows.append(row)
            saved_times.append(instant)
            record["phase_seconds"]["observation"] += time.perf_counter() - phase
            record["completed_observations"] = len(rows)
            record["last_time"] = str(instant)
            if len(rows) % 10 == 0 or instant == 40:
                save_rows(directory / "observations.npz", saved_times, rows)
                atomic_json(record_path, record)
        record["fixed_signature_final"] = fixed_signature(state, data)
        if frozen != record["fixed_signature_final"]:
            raise AssertionError("frozen marks or data changed")
        record["status"] = "complete"
    except Exception as exc:
        record.update(status="failure", error=repr(exc), traceback=traceback.format_exc())
    finally:
        save_rows(directory / "observations.npz", saved_times, rows)
        record["wall_seconds"] = time.perf_counter() - wall_start
        record["cpu_seconds"] = time.process_time() - cpu_start
        record["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
        if (directory / "observations.npz").exists():
            record["observations_sha256"] = digest(directory / "observations.npz")
        atomic_json(record_path, record)
    print(json.dumps({key: record.get(key) for key in ("configuration", "status", "wall_seconds", "error")}), flush=True)
    return 0 if record["status"] == "complete" else 1


def run_campaign(output):
    if not (output / "inputs.json").exists():
        prepare_inputs(output)
    load_inputs(output)
    closure = output / "closure"
    closure.mkdir(exist_ok=False)
    started = time.perf_counter()
    campaign = dict(format="wide-gpu-20260914-closure-campaign-v1", status="running",
                    command=sys.argv, source_hashes=source_hashes(), maximum_runs=8,
                    run_wall_cap=RUN_WALL_CAP, campaign_wall_cap=CAMPAIGN_WALL_CAP, runs=[])
    path = output / "closure_campaign.json"
    atomic_json(path, campaign)
    for config in configurations():
        remaining = CAMPAIGN_WALL_CAP - (time.perf_counter() - started)
        if remaining <= 0:
            campaign["runs"].append(dict(id=config["id"], status="unstarted_budget"))
            continue
        directory = closure / config["id"]
        directory.mkdir()
        command = [sys.executable, "-B", str(Path(__file__).resolve()), "--output", str(output), "--worker-id", config["id"]]
        worker_started = time.perf_counter()
        with (directory / "worker.log").open("xb") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, cwd=ROOT)
            try:
                code = process.wait(timeout=min(RUN_WALL_CAP, remaining))
                status = "complete" if code == 0 else "failure"
            except subprocess.TimeoutExpired:
                process.kill()
                code = process.wait()
                status = "timeout"
                worker_record_path = directory / "record.json"
                record = json.loads(worker_record_path.read_text()) if worker_record_path.exists() else {"configuration": config}
                record.update(status="timeout", error="Supervisor stopped the worker at its declared wall limit.")
                atomic_json(worker_record_path, record)
        campaign["runs"].append(dict(id=config["id"], status=status, returncode=code,
                                     wall_seconds=time.perf_counter() - worker_started, command=command))
        atomic_json(path, campaign)
    campaign["wall_seconds"] = time.perf_counter() - started
    campaign["status"] = "complete" if all(row["status"] == "complete" for row in campaign["runs"]) else "incomplete"
    atomic_json(path, campaign)
    return 0 if campaign["status"] == "complete" else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--prepare-only", action="store_true")
    action.add_argument("--run", action="store_true")
    action.add_argument("--worker-id", choices=[config["id"] for config in configurations()], help=argparse.SUPPRESS)
    args = parser.parse_args()
    output = args.output.resolve()
    if args.prepare_only:
        metadata = prepare_inputs(output)
        print(json.dumps(dict(status="prepared", output=str(output), npz_sha256=metadata["npz_sha256"])))
        return 0
    if args.worker_id:
        return run_configuration(output, next(config for config in configurations() if config["id"] == args.worker_id))
    return run_campaign(output)


if __name__ == "__main__":
    raise SystemExit(main())
