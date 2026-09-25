"""Prepare and score the user-requested width-2048 scalar comparison.

Dense training is delegated to scalar_wide_dense.py on GPU. This script only
initializes coefficients, evolves the neuron-free scalar ODE, and scores
saved endpoints. Every invocation writes to fresh or explicitly named outputs.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import sys
import time

import numpy as np
import scipy

from scalar_aggregate_engine import initialize_network, unflatten_network
from scalar_aggregate_run import write_json, file_hash
from scalar_circle_probe_engine import initialize_probe_coefficients as reference_initializer, forward_only
from scalar_wide_initialization import initialize_probe_coefficients
from scalar_long_time_engine import frozen_kernel_endpoint, StiffSignatureHierarchy, recenter_coefficients
from run_scalar_long_time import integrate, spatial_check, rms, read_npz
from run_scalar_circle_endpoints import deadline_call

HERE = Path(__file__).resolve().parent
NAMES = ("f", "Theta", "C", "Q")
SOURCES = ("run_scalar_wide.py", "scalar_wide_initialization.py", "scalar_wide_dense.py",
           "scalar_aggregate_engine.py", "scalar_aggregate_run.py", "scalar_circle_probe_engine.py",
           "scalar_long_time_engine.py", "run_scalar_long_time.py", "run_scalar_circle_endpoints.py",
           "deep_moment_engine.py", "deep_circle_run.py", "moment_engine.py",
           "SCALAR_WIDE_PROTOCOL.md", "SCALAR_WIDE_INITIALIZATION.md", "deep_circle_cases.json")


def array_hash(*values):
    digest = hashlib.sha256()
    for value in values:
        value = np.asarray(value)
        digest.update(str(value.shape).encode())
        digest.update(str(value.dtype).encode())
        digest.update(value.tobytes(order="C"))
    return digest.hexdigest()


def prepare(case, seed, output, seconds, large_check=False):
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    cases = json.loads((HERE / "deep_circle_cases.json").read_text())
    item = cases[case]
    theta = np.deg2rad(item["angles_degrees"])
    inputs = np.column_stack((np.cos(theta), np.sin(theta)))
    labels = np.array(item["labels"], dtype=float)
    angles = 2 * np.pi * np.arange(1024) / 1024
    off_angles = 2 * np.pi * (np.arange(32) + np.sqrt(2) / 10) / 32
    circle = lambda theta: np.column_stack((np.cos(theta), np.sin(theta)))
    points = np.vstack((circle(angles), circle(off_angles), inputs))
    config = dict(case=case, width=2048, seed=seed, inputs=inputs.tolist(), labels=labels.tolist(),
                  hidden_layers=3, target_loss=1e-6, off_grid_angles=off_angles.tolist())
    write_json(output / "configuration.json", config)
    snapshots = output / "sources"
    snapshots.mkdir()
    source_hashes = {}
    for name in SOURCES:
        if not (HERE/name).exists():
            raise FileNotFoundError("required source before freezing initialization: " + name)
        shutil.copy2(HERE/name, snapshots/name)
        source_hashes[name] = file_hash(HERE/name)
    params = initialize_network(2048, 2, depth=3, seed=seed)
    initialization_hash = array_hash(*params)
    coefficient_start = time.perf_counter()
    coefficients = deadline_call(lambda: initialize_probe_coefficients(
        params, inputs, points, order=4, batch_size=128), seconds)
    coefficient_seconds = time.perf_counter() - coefficient_start
    m = len(labels)
    initial = {name: coefficients[name][-m:].copy() for name in NAMES}
    np.savez_compressed(output / "initial_coefficients.npz", **initial, inputs=inputs, labels=labels)
    np.savez_compressed(output / "probe_coefficients.npz", **coefficients, angles=angles,
                        off_angles=off_angles, probe_inputs=points)
    oracle = None
    if large_check:
        selected = np.vstack((circle(np.array([0., np.pi / 7])), inputs[:2]))
        elapsed = time.perf_counter() - started
        if elapsed >= seconds:
            raise TimeoutError("initialization cap before independent four-probe check")
        old = deadline_call(lambda: reference_initializer(params, inputs, selected, order=4), seconds-elapsed)
        new = deadline_call(lambda: initialize_probe_coefficients(params, inputs, selected, order=4,
                                                                  batch_size=128), max(1., seconds-(time.perf_counter()-started)))
        oracle = {}
        for name in NAMES:
            change = float(np.max(abs(old[name] - new[name])))
            bound = 1e-11 + 1e-9 * float(np.max(abs(old[name])))
            oracle[name] = dict(maximum_difference=change, bound=bound, passed=change <= bound)
        np.savez_compressed(output / "initialization_oracle.npz", points=selected,
                            **{"reference_"+k: v for k,v in old.items()},
                            **{"optimized_"+k: v for k,v in new.items()})
        if not all(entry["passed"] for entry in oracle.values()):
            write_json(output / "initialization_failure.json", oracle)
            raise RuntimeError("large-width initializer disagrees with legacy implementation")
    if any(file_hash(HERE/name) != digest for name, digest in source_hashes.items()):
        raise RuntimeError("source changed during coefficient initialization")
    record = dict(status="initialized", **config, initialization_hash=initialization_hash,
                  coefficient_seconds=coefficient_seconds, seconds=time.perf_counter()-started,
                  initialization_oracle=oracle, coefficient_hashes={
                      name: array_hash(coefficients[name]) for name in NAMES},
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                  software=dict(python=sys.version, numpy=np.__version__, scipy=scipy.__version__,
                                platform=platform.platform()),
                  threads={key:os.environ.get(key) for key in
                           ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                  command=sys.argv, sources=source_hashes)
    if record["peak_rss_bytes"] >= 8 * 1024**3:
        raise MemoryError("initialization exceeded declared RSS cap")
    write_json(output/"initialization.json", record)
    print(json.dumps({k:record[k] for k in ("status", "case", "seed", "seconds", "coefficient_seconds", "initialization_oracle")}), flush=True)
    return record


def load_run(directory):
    path = directory/"trajectory_spatial_refined.npz"
    if not path.exists():
        path = directory/"trajectory.npz"
    return read_npz(path), json.loads((directory/"result.json").read_text())


def compare(first, second, first_record, second_record, discrepancy):
    n = min(len(first["grid"]), len(second["grid"]))
    change = rms(first["grid"][::len(first["grid"])//n]-second["grid"][::len(second["grid"])//n])
    dt = abs(float(first["time"])-float(second["time"]))/max(1., float(second["time"]))
    probe = max(first_record.get("training_probe_gap", 0.), second_record.get("training_probe_gap", 0.))
    fitted = first_record["status"] == second_record["status"] == "fitted"
    return dict(numerical_change=change, time_relative_change=dt, training_probe_gap=probe,
                passed=bool(fitted and change <= .002 and change <= .1*max(discrepancy, 1e-6)
                            and dt <= .001 and probe <= 1e-4))


def score(source, directory, reproduction=None):
    initial = read_npz(source/"initial_coefficients.npz")
    probe_path = directory/"probe_coefficients_refined.npz"
    probe = read_npz(probe_path if probe_path.exists() else source/"probe_coefficients.npz")
    families = {}
    for model in ("dense", "order4"):
        folders = sorted((p for p in directory.glob(model+"_resolution*") if p.is_dir()),
                         key=lambda p:int(p.name.split("resolution")[-1]))
        families[model] = [(p, *load_run(p)) for p in folders if (p/"result.json").exists()]
        if len(families[model]) < 2:
            raise ValueError("two completed resolutions required for " + model)
    dense, scalar = (families[name][-1][1] for name in ("dense", "order4"))
    discrepancy = rms(scalar["grid"]-dense["grid"])
    gates = {}
    for model, runs in families.items():
        _, first, fr = runs[-2]
        _, second, sr = runs[-1]
        gates[model] = compare(first, second, fr, sr, discrepancy)
    spatial, modes = spatial_check(scalar, probe, dense)
    np.savez_compressed(directory/"order4_fourier.npz", endpoint=modes)
    baseline = frozen_kernel_endpoint(initial, initial["labels"], target=1e-6, time_cap=1e9)
    prediction = (np.asarray(probe["f"], dtype=np.longdouble)
                  + np.asarray(probe["Theta"], dtype=np.longdouble) @ np.asarray(baseline["z"], dtype=np.longdouble))
    count = len(probe["angles"])
    control = dict(time=np.array(baseline["time"]), train_f=baseline["train_f"], z=baseline["z"],
                   grid=np.asarray(prediction[:count], dtype=float), off_grid=np.asarray(prediction[count:count+32], dtype=float),
                   train_probe=np.asarray(prediction[count+32:], dtype=float), status=np.array(baseline["status"]))
    np.savez_compressed(directory/"order2_spectral.npz", **control)
    control_spatial, control_modes = spatial_check(control, probe, dense)
    np.savez_compressed(directory/"order2_fourier.npz", endpoint=control_modes)
    repeated = {}
    if reproduction is not None:
        for model in ("dense", "order4"):
            other, record = load_run(reproduction/model)
            _, own, own_record = families[model][-1]
            repeated[model] = compare(own, other, own_record, record, discrepancy)
    fitted = all(runs[-1][2]["status"] == "fitted" for runs in families.values())
    valid = (all(g["passed"] for g in gates.values()) and spatial["quadrature_pass"]
             and spatial["fourier_pass"] and all(g["passed"] for g in repeated.values()))
    # First hard seed requires the independent repetition before a final verdict.
    config = json.loads((source/"configuration.json").read_text())
    needs_reproduction = config["case"] == "quadrant_alternating" and config["seed"] == 20260920
    pending_reproduction = needs_reproduction and reproduction is None
    verdict = ("no_matched_endpoint" if not fitted else "reproduction_pending" if pending_reproduction else
               "numerically_inconclusive" if not valid else "agreement" if discrepancy <= .1 else
               "adverse" if discrepancy > .2 else "inconclusive")
    result = dict(configuration=source.name, **config, gates=gates, spatial=spatial,
                  records={name:[record for _, _, record in runs] for name,runs in families.items()},
                  order2=dict(status=baseline["status"], time=baseline["time"], loss=baseline["loss"], spatial=control_spatial),
                  reproduction=repeated, verdict=verdict)
    write_json(directory/"summary.json", result)
    print(json.dumps(dict(event="scored", configuration=source.name, verdict=verdict,
                          circle_rms=discrepancy, gates=gates)), flush=True)
    return result


def refine_spatial(source, directory, seconds):
    """One predeclared passive-only 2048-angle refinement, without training."""
    initial = read_npz(source/"initial_coefficients.npz")
    config = json.loads((source/"configuration.json").read_text())
    original_probe = read_npz(source/"probe_coefficients.npz")
    angles = 2*np.pi*np.arange(2048)/2048
    off = original_probe["off_angles"]
    points = np.vstack((np.column_stack((np.cos(angles),np.sin(angles))),
                        np.column_stack((np.cos(off),np.sin(off))), initial["inputs"]))
    params = initialize_network(2048, 2, depth=3, seed=config["seed"])
    coefficients = deadline_call(lambda:initialize_probe_coefficients(params, initial["inputs"], points,
                                                                      order=4, batch_size=128), seconds)
    path = directory/"probe_coefficients_refined.npz"
    if path.exists():
        raise FileExistsError("only one spatial refinement is permitted")
    np.savez_compressed(path, **coefficients, angles=angles, off_angles=off, probe_inputs=points)
    model = StiffSignatureHierarchy(initial, initial["labels"], 4)
    for folder in sorted(p for p in directory.glob("order4_resolution*") if p.is_dir()):
        arrays, record = load_run(folder)
        if not record["from_zero"]:
            raise ValueError("wide campaign spatial replay requires time-zero scalar initialization")
        anchor = coefficients
        for state in arrays["segment_states"]:
            anchor = recenter_coefficients(anchor, model.signatures(state))
        values = anchor["f"]
        arrays.update(grid=np.asarray(values[:2048],float), off_grid=np.asarray(values[2048:2080],float),
                      train_probe=np.asarray(values[2080:],float))
        np.savez_compressed(folder/"trajectory_spatial_refined.npz", **arrays)
    for folder in sorted(p for p in directory.glob("dense_resolution*") if p.is_dir()):
        arrays, _ = load_run(folder)
        params = unflatten_network(arrays["flatstate"], ((2048,2),(2048,2048),(2048,2048),(2048,)))
        prediction = forward_only(params, points)
        arrays.update(grid=prediction[:2048], off_grid=prediction[2048:2080], grid_angles=angles)
        np.savez(folder/"trajectory_spatial_refined.npz", **arrays)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "scalar", "score", "spatial"))
    parser.add_argument("--source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--case", choices=("equal_mixed_odd", "quadrant_alternating"), default="quadrant_alternating")
    parser.add_argument("--seed", type=int, default=20260920)
    parser.add_argument("--seconds", type=float, default=600.)
    parser.add_argument("--rtol", type=float, default=1e-9)
    parser.add_argument("--large-check", action="store_true")
    parser.add_argument("--reproduction", type=Path)
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare(args.case, args.seed, args.output, args.seconds, args.large_check)
    elif args.mode == "scalar":
        integrate(args.source, args.output, 0, args.rtol, "BDF", True, args.seconds)
    elif args.mode == "spatial":
        refine_spatial(args.source, args.output, args.seconds)
    else:
        score(args.source, args.output, args.reproduction)


if __name__ == "__main__":
    main()
