#!/usr/bin/env python3
"""Independent saved-array metrics and fixed numerical gates; never trains.

The scientific decisions and formulas below implement PROTOCOL.md.  This module
does not import the producer or use producer-computed losses for fit decisions.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import numpy as np

TIMES = np.array([0, .01, .03, .1, .3, 1, 3, 5, 10, 20, 40, 60,
                  100, 160, 250, 400, 630, 800, 1000.], dtype=float)
SEEDS = (20260921, 20260922, 20260923)
MODELS = ("width55", "closure1024", "width105")
WIDTHS = {"width55": 55, "closure1024": 1024, "width105": 105}
LEVELS = {"primary": (1e-6, 1e-9, 2.), "fine": (1e-8, 1e-11, 1.),
          "finer": (1e-10, 1e-13, .5)}
HARMONICS = np.array([1, 3, 5])
COEFFICIENT = math.sqrt(32 / 21)
TARGET_COS = COEFFICIENT * np.array([1., 0., .25])
TARGET_SIN = COEFFICIENT * np.array([0., .5, 0.])
FIT_MSE = .001


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(2**20), b""):
            h.update(block)
    return h.hexdigest()


def target(theta):
    theta = np.asarray(theta)
    return COEFFICIENT * (np.cos(theta) + .5*np.sin(3*theta) +
                          .25*np.cos(5*theta))


def panel_metrics(predictions, theta):
    """Discrete equal-weight orthogonal Fourier decomposition on either panel."""
    f = np.asarray(predictions, dtype=float)
    theta = np.asarray(theta, dtype=float)
    if f.ndim != 2 or f.shape[1] != theta.size:
        raise ValueError("predictions must have checkpoint by panel shape")
    co = np.cos(HARMONICS[:, None] * theta[None, :])
    si = np.sin(HARMONICS[:, None] * theta[None, :])
    a = 2 * f @ co.T / theta.size
    b = 2 * f @ si.T / theta.size
    component = .5 * ((a - TARGET_COS)**2 + (b - TARGET_SIN)**2)
    outside = np.mean((f - a@co - b@si)**2, axis=1)
    mse = np.mean((f - target(theta))**2, axis=1)
    return {"mse": mse, "rmse": np.sqrt(mse), "cosine": a, "sine": b,
            "component_error": component, "outside_energy": outside,
            "decomposition_error": np.abs(mse - component.sum(axis=1) - outside),
            "sign_accuracy": np.mean(np.sign(f) == np.sign(target(theta)), axis=1)}


def block_slices(model):
    n = WIDTHS[model]
    middle = 15 if model == "closure1024" else n*n
    return {"W": slice(0, 2*n), "middle": slice(2*n, 2*n+middle),
            "c": slice(2*n+middle, 3*n+middle)}


def _max(values, default=0.):
    return float(np.max(values)) if np.size(values) else default


def _plain(value):
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(v) for v in value]
    if isinstance(value, np.ndarray):
        return _plain(value.tolist())
    if isinstance(value, np.generic):
        return _plain(value.item())
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def _write_json(path, value):
    path.write_text(json.dumps(_plain(value), indent=2, sort_keys=True) + "\n")


def monotonicity(times, losses):
    times, losses = np.asarray(times), np.asarray(losses)
    finite = bool(np.all(np.isfinite(times)) and np.all(np.isfinite(losses)))
    increasing_times = bool(times.size > 1 and np.all(np.diff(times) > 0))
    ratios = np.diff(losses) / (5e-7 * np.maximum(1., losses[:-1]))
    return {"pass": finite and increasing_times and _max(ratios) <= 1,
            "max_increase": _max(np.diff(losses)),
            "max_increase_to_allowance": _max(ratios),
            "finite": finite, "strictly_increasing_times": increasing_times}


def compare_arrays(coarse, finer):
    """Run dictionaries contain arrays, recomputed panel metrics, and model.

    Check all declared checkpoints, never just terminal predictions.  A partial
    pair has diagnostic prefix differences but cannot pass the completion gate.
    """
    ta, tb = coarse["times"], finer["times"]
    common, ia, ib = np.intersect1d(ta, tb, return_indices=True)
    result = {"common_times": common.tolist(),
              "all_checkpoints": bool(np.array_equal(common, TIMES)),
              "same_model": coarse["model"] == finer["model"],
              "same_seed": coarse["seed"] == finer["seed"],
              "both_complete": bool(coarse["complete"] and finer["complete"])}
    if not len(common):
        return {**result, "pass": False, "reason": "no common checkpoints"}
    for panel in ("train", "passive"):
        result[panel + "_prediction_max_difference"] = _max(np.abs(
            coarse[panel + "_predictions"][ia] - finer[panel + "_predictions"][ib]))
        result[panel + "_rmse_max_difference"] = _max(np.abs(
            coarse[panel]["rmse"][ia] - finer[panel]["rmse"][ib]))
    blocks = {}
    for name, loc in block_slices(finer["model"]).items():
        a, b = coarse["states"][ia, loc], finer["states"][ib, loc]
        rms = np.sqrt(np.mean((a-b)**2, axis=1))
        allowed = 2e-4 * (1 + np.sqrt(np.mean(b*b, axis=1)))
        blocks[name] = {"max_rms_difference": _max(rms),
                        "max_fraction_of_allowance": _max(rms/allowed),
                        "rms_difference_by_time": rms.tolist(),
                        "allowance_by_time": allowed.tolist(),
                        "pass": bool(np.all(rms <= allowed))}
    result["parameter_blocks"] = blocks
    result["same_final_fit_decision"] = bool(
        result["all_checkpoints"] and
        (coarse["train"]["mse"][ia[-1]] <= FIT_MSE) ==
        (finer["train"]["mse"][ib[-1]] <= FIT_MSE))
    result["finer_monotonicity"] = finer["monotonicity"]
    result["pass"] = bool(
        result["all_checkpoints"] and result["same_model"] and
        result["same_seed"] and result["both_complete"] and
        all(result[p+"_prediction_max_difference"] <= 2e-4 and
            result[p+"_rmse_max_difference"] <= 5e-5 for p in ("train", "passive")) and
        all(block["pass"] for block in blocks.values()) and
        result["same_final_fit_decision"] and finer["monotonicity"]["pass"])
    return result


def reproduction_arrays(original, repeat):
    common, ia, ib = np.intersect1d(original["times"], repeat["times"],
                                  return_indices=True)
    complete = bool(np.array_equal(common, TIMES) and original["complete"]
                    and repeat["complete"])
    result = {"all_checkpoints": complete, "common_times": common.tolist()}
    if not len(common):
        return {**result, "pass": False}
    result["parameter_max_difference"] = _max(np.abs(
        original["states"][ia] - repeat["states"][ib]))
    for panel in ("train", "passive"):
        result[panel+"_prediction_max_difference"] = _max(np.abs(
            original[panel+"_predictions"][ia] - repeat[panel+"_predictions"][ib]))
    result["same_all_checkpoint_fit_decisions"] = bool(np.array_equal(
        original["train"]["mse"][ia] <= FIT_MSE,
        repeat["train"]["mse"][ib] <= FIT_MSE))
    result["pass"] = bool(complete and result["same_all_checkpoint_fit_decisions"] and
                          result["parameter_max_difference"] <= 1e-10 and
                          all(result[p+"_prediction_max_difference"] <= 1e-10
                              for p in ("train", "passive")))
    return result


def array_sha256(array):
    a = np.ascontiguousarray(array)
    descriptor = json.dumps({"dtype": a.dtype.str, "shape": list(a.shape)},
                            sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(descriptor + b"\n" + a.tobytes()).hexdigest()


def read_run(directory, *, verify_hashes=True):
    """Read one retained worker; recompute every decision metric from prediction."""
    directory = Path(directory).resolve()
    record = json.loads((directory / "result.json").read_text())
    config = record["config"]
    model, seed, level = config["model"], config["seed"], config["level"]
    issues = []
    if model not in MODELS or seed not in SEEDS or level not in LEVELS:
        raise ValueError("run lies outside the fixed model/seed/level design")
    if config.get("checkpoints") != TIMES.tolist():
        issues.append("configured checkpoints differ from the fixed protocol")
    rtol, atol, max_step = LEVELS[level]
    for name, wanted in (("rtol", rtol), ("atol", atol), ("max_step", max_step),
                         ("dtype", "float64"), ("numerical_threads", 1),
                         ("wall_seconds", 400.0),
                         ("mobilities", [WIDTHS[model], 1, WIDTHS[model]])):
        if config.get(name) != wanted:
            issues.append("incorrect configuration " + name)
    hashes = {}
    if verify_hashes:
        for filename, expected in record.get("output_sha256", {}).items():
            path = directory / filename
            ok = path.is_file() and sha256(path) == expected
            hashes[filename] = ok
            if not ok:
                issues.append("output hash mismatch: " + filename)
        required = {"source.npz", "checkpoints.npz", "final.npz", "accepted_steps.csv", "config.json"}
        if not required <= set(hashes):
            issues.append("required output hashes missing")
    with np.load(directory / "source.npz", allow_pickle=False) as archive:
        source = {key: archive[key] for key in archive.files}
    for key, array in source.items():
        if verify_hashes and record.get("source_array_sha256", {}).get(key) != array_sha256(array):
            issues.append("source array hash mismatch: " + key)
    with np.load(directory / "checkpoints.npz", allow_pickle=False) as archive:
        saved = {key: archive[key] for key in archive.files}
    times = saved["times"]
    states = saved["states"]
    expected_size = block_slices(model)["c"].stop
    if times.ndim != 1 or states.shape != (len(times), expected_size):
        raise ValueError("checkpoint state shape mismatch")
    if not np.array_equal(times, TIMES[:len(times)]):
        issues.append("saved observation times are not the common-time prefix")
    if not np.array_equal(states[0], source["initial_state"]):
        issues.append("first saved state differs from the retained initialization")
    if not all(np.all(np.isfinite(value)) for value in saved.values()):
        issues.append("nonfinite checkpoint arrays")
    if states.dtype != np.dtype("float64"):
        issues.append("packed states are not float64")
    n = WIDTHS[model]
    rng = np.random.default_rng(seed)
    canonical = {"W0": rng.standard_normal((n, 2)),
                 "A0": rng.standard_normal((n, n))/np.sqrt(n),
                 "c0": rng.standard_normal(n)/n}
    for name, value in canonical.items():
        if not np.array_equal(source[name], value):
            issues.append("canonical initialization mismatch: " + name)
    expected_initial = np.concatenate((source["W0"].ravel(),
        source["M0" if model == "closure1024" else "A0"].ravel(), source["c0"]))
    if not np.array_equal(source["initial_state"], expected_initial):
        issues.append("initial packed state disagrees with canonical blocks")
    result = {"path": str(directory), "model": model, "seed": seed,
              "level": level, "record": record, "times": times, "states": states,
              "rhs": saved["rhs"], "source_hashes": record.get("source_sha256", {}),
              "hash_checks": hashes, "issues": issues, "saved": saved}
    for panel, size, offset in (("train", 126, 0), ("passive", 1024, .5)):
        theta = 2*np.pi*(np.arange(size)+offset)/size
        x = np.column_stack((np.cos(theta), np.sin(theta)))
        for key, wanted in (("theta", theta), ("x", x), ("u", x/np.sqrt(2)),
                            ("y", target(theta))):
            actual = source[panel+"_"+key]
            if actual.shape != wanted.shape or _max(np.abs(actual-wanted)) > 5e-13:
                issues.append("incorrect " + panel + " data field " + key)
        f = saved[panel+"_prediction"]
        if f.shape != (len(times), size):
            raise ValueError("prediction shape mismatch")
        metrics = panel_metrics(f, theta)
        metrics["saved_loss_max_difference"] = _max(np.abs(metrics["mse"] - saved[panel+"_loss"]))
        if metrics["saved_loss_max_difference"] > 1e-10:
            issues.append(panel + " recorded loss disagrees with saved prediction")
        if _max(metrics["decomposition_error"]) > 1e-10:
            issues.append(panel + " Fourier energy decomposition failed")
        result[panel] = metrics
        result[panel+"_predictions"] = f
        result[panel+"_theta"] = theta
    with (directory / "accepted_steps.csv").open(newline="") as handle:
        history = list(csv.DictReader(handle))
    columns = {name: np.array([float(row[name]) for row in history])
               for name in ("accepted_index", "time", "loss", "step", "nfev_ode", "wall_seconds", "dissipation")}
    result["accepted"] = columns
    result["monotonicity"] = monotonicity(columns["time"], columns["loss"])
    if len(history) != record["accepted_steps"]+1:
        issues.append("accepted-step count mismatch")
    if len(history) and columns["time"][-1] != record["physical_time"]:
        issues.append("accepted final time disagrees with record")
    step_error = _max(np.abs(np.diff(columns["time"]) - columns["step"][1:]))
    if step_error > 2e-12:
        issues.append("recorded physical step sizes disagree with endpoint times")
    result["step_time_consistency_error"] = step_error
    if len(history) and (np.any(np.diff(columns["wall_seconds"]) < 0) or
                         np.any(np.diff(columns["nfev_ode"]) < 0)):
        issues.append("wall time or RHS counters decrease")
    if len(history) and _max(columns["step"]) > max_step*(1+1e-12):
        issues.append("maximum physical step violated")
    checkpoint_wall, checkpoint_rhs = [], []
    for index, t in enumerate(times):
        match = np.flatnonzero(columns["time"] == t)
        if len(match) != 1:
            issues.append("checkpoint is not a unique accepted endpoint: " + str(t))
            checkpoint_wall.append(float("nan")); checkpoint_rhs.append(float("nan"))
        else:
            j = match[0]
            checkpoint_wall.append(columns["wall_seconds"][j])
            checkpoint_rhs.append(columns["nfev_ode"][j])
            if abs(columns["loss"][j] - result["train"]["mse"][index]) > 1e-10:
                issues.append("accepted-step and saved-array loss disagree at " + str(t))
    result["checkpoint_wall_seconds"] = np.array(checkpoint_wall)
    result["checkpoint_nfev_ode"] = np.array(checkpoint_rhs)
    dissipation = np.zeros(len(times))
    for name, loc in block_slices(model).items():
        mobility = 1 if name == "middle" else WIDTHS[model]
        dissipation += np.sum(saved["rhs"][:, loc]**2, axis=1)/mobility
    result["dissipation_saved_error"] = _max(np.abs(dissipation-saved["dissipation"]))
    if not np.allclose(dissipation, saved["dissipation"], atol=2e-12, rtol=2e-10):
        issues.append("saved physical squared-gradient norm disagrees with saved RHS")
    counts = record.get("counts", {})
    fixed = 8192 if model == "closure1024" else 0
    for key, wanted in (("dynamic_scalars", expected_size),
                        ("frozen_dictionary_scalars", fixed),
                        ("dynamic_plus_dictionary_scalars", expected_size+fixed)):
        if counts.get(key) != wanted:
            issues.append("incorrect predictor scalar count " + key)
    if record["nfev_ode"] > 150000 or record["accepted_steps"] > 30000:
        issues.append("per-worker RHS/accepted-step budget violated")
    result["complete"] = bool(record["status"] == "completed" and
                              record["physical_time"] == 1000 and np.array_equal(times, TIMES))
    result["valid_arrays"] = not issues
    fit = np.flatnonzero(result["train"]["mse"] <= FIT_MSE)
    result["first_saved_fit_time"] = float(times[fit[0]]) if len(fit) else None
    result["first_saved_fit_bracket"] = ([float(times[max(0,fit[0]-1)]), float(times[fit[0]])]
                                           if len(fit) else None)
    return result


def compare_runs(coarse_directory, finer_directory):
    """Runner entry point: selected-pair accuracy and finer monotonicity gate."""
    coarse, finer = read_run(coarse_directory), read_run(finer_directory)
    comparison = compare_arrays(coarse, finer)
    comparison["array_issues"] = {"coarse": coarse["issues"], "finer": finer["issues"]}
    comparison["same_source_hashes"] = coarse["source_hashes"] == finer["source_hashes"]
    comparison["pass"] = bool(comparison["pass"] and coarse["valid_arrays"] and
                              finer["valid_arrays"] and comparison["same_source_hashes"])
    return _plain(comparison)


def _summarize_run(run):
    out = {key: run[key] for key in ("path", "model", "seed", "level", "complete",
           "valid_arrays", "issues", "first_saved_fit_time", "first_saved_fit_bracket",
           "monotonicity", "hash_checks", "source_hashes", "dissipation_saved_error")}
    out.update(status=run["record"]["status"], physical_time=run["record"]["physical_time"],
               accepted_steps=run["record"]["accepted_steps"],
               nfev_ode=run["record"]["nfev_ode"], timing=run["record"]["timing"],
               counts=run["record"]["counts"], times=run["times"])
    for panel in ("train", "passive"):
        out[panel] = run[panel]
    for name in ("hidden_rms_displacement", "saturation_diagnostics", "dissipation"):
        if name in run["saved"]:
            out[name] = run["saved"][name]
    return _plain(out)


def aggregate(runroot, replay_path):
    runroot = Path(runroot).resolve()
    manifest_path = runroot / "run_record.json"
    manifest = json.loads(manifest_path.read_text())
    issues, unavailable, loaded = [], [], {}
    root = Path(__file__).resolve().parents[2]
    frozen = manifest.get("frozen_sources", {})
    for relative, expected in frozen.items():
        path = root / relative
        if not path.is_file() or sha256(path) != expected:
            issues.append("current frozen source does not match manifest: " + relative)
    analyzer_relative = str(Path(__file__).resolve().relative_to(root))
    if frozen.get(analyzer_relative) != sha256(__file__):
        issues.append("analyzer was not frozen at its current source hash")
    preflight_path = Path(manifest["preflight"])
    preflight = json.loads(preflight_path.read_text())
    if sha256(preflight_path) != manifest["preflight_sha256"] or not preflight.get("passed"):
        issues.append("preflight missing, changed, or did not pass")
    replay = json.loads(Path(replay_path).read_text()) if replay_path else {}
    if not replay.get("passed", False):
        issues.append("independent saved-array replay not passed")
    for key, basename in (("producer_sha256", "flow_benchmark.py"),
                          ("checker_sha256", "flow_check.py"),
                          ("protocol_sha256", "PROTOCOL.md")):
        expected = frozen.get(str(Path(__file__).resolve().with_name(basename).relative_to(root)))
        if replay.get(key) != expected:
            issues.append("replay source binding mismatch: " + key)
    attempts = manifest["attempts"]
    replay_runs = {str(Path(row["directory"]).resolve()): row for row in replay.get("runs", [])}
    attempt_directories = {str(Path(row["directory"]).resolve()) for row in attempts}
    if set(replay_runs) != attempt_directories or len(replay_runs) != len(replay.get("runs", [])):
        issues.append("replay does not cover the exact retained attempt set once each")
    if replay.get("campaign") and Path(replay["campaign"]).resolve() != runroot:
        issues.append("replay names another campaign")
    by_key = {}
    for attempt in attempts:
        key = (attempt["model"], attempt["seed"], attempt["level"], attempt["kind"])
        if key in by_key:
            issues.append("duplicate retained configuration " + str(key))
        by_key[key] = attempt
        if key[0] not in MODELS or key[1] not in SEEDS or key[2] not in LEVELS:
            issues.append("undeclared configuration " + str(key))
        if key[3] == "reproduction" and key[1] != SEEDS[0]:
            issues.append("reproduction uses an undeclared seed")
        directory = Path(attempt["directory"])
        checked = replay_runs.get(str(directory.resolve()))
        if (not checked or not checked.get("passed") or not checked.get("output_hashes_verified")
                or checked.get("result_sha256") != attempt.get("result_sha256")):
            issues.append("attempt lacks matching successful independent replay: " + str(directory))
        try:
            if attempt.get("result_sha256") != sha256(directory/"result.json"):
                issues.append("runner result hash mismatch: " + str(directory))
            run = read_run(directory)
            loaded[key] = run
            if any(run[name] != attempt[name] for name in ("model", "seed", "level")):
                run["issues"].append("worker configuration disagrees with runner")
            for relative, expected in frozen.items():
                if Path(relative).name in ("flow_benchmark.py", "PROTOCOL.md", "finite_network.py"):
                    if run["source_hashes"].get(str(root/relative)) != expected:
                        run["issues"].append("worker scientific source hash disagrees with freeze: " + relative)
            pools = run["record"].get("environment", {}).get("threadpools", [])
            if not pools or any(pool.get("num_threads") != 1 for pool in pools):
                run["issues"].append("one-thread numerical policy not verified")
            run["valid_arrays"] = not run["issues"]
        except (OSError, ValueError, KeyError, IndexError) as error:
            unavailable.append({"configuration": key, "path": str(directory), "error": str(error)})
    wall = sum(attempt["worker_process_wall_seconds"] for attempt in attempts)
    budget = {"worker_process_wall_seconds": wall,
              "matches_runner_total": abs(wall-manifest["worker_process_wall_seconds"]) <= 1e-6,
              "within_4200_seconds": wall <= 4200,
              "max_worker_seconds": max((a["worker_process_wall_seconds"] for a in attempts), default=0),
              "max_declared_concurrency": manifest.get("maximum_concurrency"),
              "attempt_count": len(attempts),
              "primary_fine_attempts": sum(a["kind"] == "original" and a["level"] != "finer" for a in attempts),
              "finer_attempts": sum(a["kind"] == "original" and a["level"] == "finer" for a in attempts),
              "reproduction_attempts": sum(a["kind"] == "reproduction" for a in attempts)}
    attempt_by_id = {a["id"]: a for a in attempts}
    batch_ids, prior = [], 0.
    reservations_valid = bool(manifest.get("batches"))
    for batch in manifest.get("batches", []):
        ids = batch["jobs"]
        accounted = sum(attempt_by_id[j]["worker_process_wall_seconds"] for j in ids if j in attempt_by_id)
        reservations_valid &= bool(1 <= len(ids) <= 2 and batch["reserved_seconds"] == 430*len(ids)
            and abs(batch["prior_wall_seconds"]-prior) <= 1e-6
            and batch["prior_wall_seconds"]+batch["reserved_seconds"] <= 4200
            and batch["status"] == "complete"
            and abs(batch.get("after_wall_seconds", -1)-prior-accounted) <= 1e-6)
        batch_ids.extend(ids)
        prior += accounted
    reservations_valid &= len(batch_ids) == len(set(batch_ids)) and set(batch_ids) == set(attempt_by_id)
    budget["reservations_verified"] = bool(reservations_valid)
    budget["batches"] = manifest.get("batches", [])
    budget["pass"] = bool(budget["matches_runner_total"] and budget["within_4200_seconds"] and
                          budget["max_worker_seconds"] <= 430 and budget["max_declared_concurrency"] <= 2 and
                          reservations_valid and
                          budget["primary_fine_attempts"] <= 18 and budget["finer_attempts"] <= 9 and
                          budget["reproduction_attempts"] <= 3)
    if not budget["pass"]:
        issues.append("execution budget or concurrency accounting failed")
    selections, comparisons, reproductions, diagnostic = {}, [], {}, {}
    for model in MODELS:
        for seed in SEEDS:
            base = (model, seed)
            p, f, ff = [loaded.get((*base, level, "original")) for level in LEVELS]
            candidate = next((r for r in (ff, f, p) if r is not None), None)
            if candidate:
                diagnostic[base] = candidate
            first = None
            if p and f:
                first = compare_arrays(p, f)
                first["pass"] &= p["valid_arrays"] and f["valid_arrays"] and p["source_hashes"] == f["source_hashes"]
                comparisons.append({"model": model, "seed": seed, "levels": ["primary", "fine"], **first})
            if first and first["pass"]:
                selections[base] = f
                if ff:
                    issues.append("undeclared finer run after passing primary/fine: " + str(base))
            elif p and f and ff and p["complete"] and f["complete"] and p["valid_arrays"] and f["valid_arrays"]:
                second = compare_arrays(f, ff)
                second["pass"] &= ff["valid_arrays"] and f["source_hashes"] == ff["source_hashes"]
                comparisons.append({"model": model, "seed": seed, "levels": ["fine", "finer"], **second})
                if second["pass"]:
                    selections[base] = ff
            if base in selections:
                diagnostic[base] = selections[base]
        original = selections.get((model, SEEDS[0]))
        repeat = loaded.get((model, SEEDS[0], original["level"], "reproduction")) if original else None
        if original and repeat:
            reproduction = reproduction_arrays(original, repeat)
            reproduction["pass"] &= repeat["valid_arrays"] and original["source_hashes"] == repeat["source_hashes"]
            reproductions[model] = reproduction
        else:
            reproductions[model] = {"pass": False, "reason": "selected first-seed run or its reproduction unavailable"}
    declared_selection = {(r["model"], r["seed"]): r["level"] for r in manifest.get("selected", [])}
    independently_selected = {key: run["level"] for key, run in selections.items()}
    if declared_selection != independently_selected:
        issues.append("runner and independent analysis selections disagree")
    runner_comparisons = {(r["model"], r["seed"], Path(r["fine"]).name.rsplit("_", 1)[-1]): r
                          for r in manifest.get("comparisons", [])}
    for comparison in comparisons:
        key = (comparison["model"], comparison["seed"], comparison["levels"][-1])
        runner = runner_comparisons.get(key)
        if runner is None or bool(runner["passed"]) != bool(comparison["pass"]):
            issues.append("runner and independent refinement decisions disagree: " + str(key))
    runner_reproductions = {r["model"]: r for r in manifest.get("reproductions", [])}
    for model, comparison in reproductions.items():
        runner = runner_reproductions.get(model)
        if runner is not None and bool(runner["passed"]) != bool(comparison["pass"]):
            issues.append("runner and independent reproduction decisions disagree: " + model)
    models = {}
    for model in MODELS:
        rows = [selections.get((model, seed)) for seed in SEEDS]
        complete = all(row is not None for row in rows)
        valid = bool(complete and reproductions[model]["pass"] and not issues)
        models[model] = {"numerically_valid": valid, "resolved_seeds": sum(r is not None for r in rows),
                         "trainable_scalars": block_slices(model)["c"].stop,
                         "retained_predictor_scalars": block_slices(model)["c"].stop+(8192 if model == "closure1024" else 0)}
        if complete:
            for panel in ("train", "passive"):
                values = [float(row[panel]["rmse"][-1]) for row in rows]
                models[model][panel+"_rmse"] = values
                models[model][panel+"_median_rmse"] = float(np.median(values))
            models[model]["fit_count"] = sum(row["train"]["mse"][-1] <= FIT_MSE for row in rows)
    separations = {}
    closure = models["closure1024"]
    for dense in ("width55", "width105"):
        control = models[dense]
        valid = closure["numerically_valid"] and control["numerically_valid"]
        ratio = None
        if "train_median_rmse" in closure and "train_median_rmse" in control:
            numerator, denominator = closure["train_median_rmse"], control["train_median_rmse"]
            ratio = numerator/denominator if denominator else (1. if numerator == 0 else float("inf"))
        discriminator = (ratio is not None and closure["fit_count"] >= 2 and
                         control["fit_count"] == 0 and ratio <= 1/3)
        separations[dense] = {"valid": valid, "closure_over_dense_median_rmse": ratio,
                              "strong_separation": bool(valid and discriminator),
                              "conclusion": ("strong separation" if discriminator else "strong separation not observed")
                              if valid else "numerically inconclusive"}
    summary = {"manifest": str(manifest_path), "manifest_sha256": sha256(manifest_path),
               "analyzer_sha256": sha256(__file__), "protocol_sha256": manifest["protocol_sha256"],
               "preflight": str(preflight_path), "replay": str(replay_path) if replay_path else None,
               "replay_sha256": sha256(replay_path) if replay_path else None,
               "issues": issues, "unavailable_runs": unavailable, "budget": budget,
               "comparisons": comparisons, "reproductions": reproductions,
               "models": models, "separations": separations,
               "selected": [{"model": model, "seed": seed, "level": run["level"], "path": run["path"]}
                            for (model, seed), run in selections.items()],
               "runs": [_summarize_run(run) for run in loaded.values()],
               "scope": "Descriptive fixed-seed finite-model comparison at T=1000; no confidence interval, lower bound, or all-time claim."}
    return _plain(summary), diagnostic


def write_tables(output, diagnostic):
    endpoint_rows, harmonic_rows, checkpoint_rows = [], [], []
    for (model, seed), run in diagnostic.items():
        last = len(run["times"])-1
        motion = run["saved"].get("hidden_rms_displacement", np.full((last+1, 2), np.nan))[last]
        row = {"model": model, "seed": seed, "level": run["level"],
               "complete": run["complete"], "arrays_valid": run["valid_arrays"],
               "physical_time": run["times"][last],
               "train_rmse": run["train"]["rmse"][last], "passive_rmse": run["passive"]["rmse"][last],
               "first_saved_fit_time": run["first_saved_fit_time"],
               "first_fit_previous_saved_time": (run["first_saved_fit_bracket"] or [None])[0],
               "hidden1_rms_motion": motion[0], "hidden2_rms_motion": motion[1],
               "accepted_steps": run["record"]["accepted_steps"], "nfev_ode": run["record"]["nfev_ode"],
               "worker_reported_wall_seconds": run["record"]["timing"]["wall_before_result_write"]}
        endpoint_rows.append(row)
        for panel in ("train", "passive"):
            met = run[panel]
            for i, harmonic in enumerate(HARMONICS):
                harmonic_rows.append({"model": model, "seed": seed, "level": run["level"],
                    "panel": panel, "physical_time": run["times"][last], "harmonic": harmonic,
                    "cosine": met["cosine"][last,i], "target_cosine": TARGET_COS[i],
                    "cosine_error": met["cosine"][last,i]-TARGET_COS[i],
                    "sine": met["sine"][last,i], "target_sine": TARGET_SIN[i],
                    "sine_error": met["sine"][last,i]-TARGET_SIN[i],
                    "error_energy": met["component_error"][last,i],
                    "outside_energy": met["outside_energy"][last]})
            for k, t in enumerate(run["times"]):
                checkpoint_rows.append({"model": model, "seed": seed, "level": run["level"],
                    "panel": panel, "physical_time": t, "mse": met["mse"][k], "rmse": met["rmse"][k],
                    "harmonic1_error_energy": met["component_error"][k,0],
                    "harmonic3_error_energy": met["component_error"][k,1],
                    "harmonic5_error_energy": met["component_error"][k,2],
                    "outside_energy": met["outside_energy"][k],
                    "wall_seconds": run["checkpoint_wall_seconds"][k], "nfev_ode": run["checkpoint_nfev_ode"][k]})
    for name, rows in (("endpoints.csv", endpoint_rows), ("harmonics.csv", harmonic_rows),
                       ("checkpoints.csv", checkpoint_rows)):
        with (output/name).open("x", newline="") as handle:
            if rows:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                writer.writeheader(); writer.writerows(rows)
    return endpoint_rows


def write_plots(output, diagnostic, summary):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    colors = {"width55": "#0072B2", "closure1024": "#D55E00", "width105": "#009E73"}
    labels = {"width55": "Dense 55", "closure1024": "Closure 1024, p=1", "width105": "Dense 105"}
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.dpi": 180})
    valid = all(row["numerically_valid"] for row in summary["models"].values())
    suffix = "" if valid else " — diagnostic; numerical validity unresolved"

    def save(fig, stem):
        fig.tight_layout()
        for ext in ("png", "pdf"):
            fig.savefig(output/(stem+"."+ext), bbox_inches="tight")
        plt.close(fig)

    def band(ax, model, panel, metric, component=None):
        runs = [diagnostic.get((model, seed)) for seed in SEEDS]
        runs = [r for r in runs if r is not None]
        if not runs:
            return
        common = runs[0]["times"]
        for run in runs[1:]:
            common = np.intersect1d(common, run["times"])
        values = []
        for run in runs:
            index = np.searchsorted(run["times"], common)
            v = run[panel][metric][index]
            values.append(v if component is None else v[:, component])
        values = np.maximum(np.asarray(values), 1e-18)
        ax.plot(common, np.median(values, axis=0), color=colors[model], label=labels[model], lw=2)
        ax.fill_between(common, values.min(axis=0), values.max(axis=0), color=colors[model], alpha=.16)
        ax.set_xscale("symlog", linthresh=.01); ax.set_yscale("log")
        ax.set_xlabel("Physical flow time"); ax.grid(alpha=.18)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    for ax, panel in zip(axes, ("train", "passive")):
        for model in MODELS:
            band(ax, model, panel, "mse")
        ax.axhline(FIT_MSE, color="gray", linestyle=":", label="Fit threshold")
        ax.set_title("Training, 126 angles" if panel == "train" else "Passive, 1024 midpoint angles")
        ax.set_ylabel("Mean squared error")
    axes[0].legend(fontsize=8)
    fig.suptitle("Canonical gradient flow: median and fixed-seed range"+suffix, fontsize=11)
    save(fig, "loss_physical_time")
    fig, axes = plt.subplots(2, 3, figsize=(12, 7))
    for row, panel in enumerate(("train", "passive")):
        for col, harmonic in enumerate(HARMONICS):
            ax = axes[row,col]
            for model in MODELS:
                band(ax, model, panel, "component_error", col)
            ax.set_title(f"{panel.capitalize()} harmonic {harmonic}")
            ax.set_ylabel("Coefficient error energy")
    axes[0,0].legend(fontsize=8)
    fig.suptitle("Harmonic loss: median and fixed-seed range"+suffix, fontsize=11)
    save(fig, "harmonic_loss")
    fig, ax = plt.subplots(figsize=(10, 4))
    theta = 2*np.pi*(np.arange(1024)+.5)/1024
    ax.plot(theta, target(theta), "k--", lw=2, label="Analytic target")
    for model in MODELS:
        runs = [diagnostic.get((model, seed)) for seed in SEEDS]
        runs = [r for r in runs if r is not None and r["complete"]]
        if runs:
            predictions = np.array([r["passive_predictions"][-1] for r in runs])
            ax.plot(theta, np.median(predictions, axis=0), color=colors[model], label=labels[model])
            ax.fill_between(theta, predictions.min(axis=0), predictions.max(axis=0),
                            color=colors[model], alpha=.16)
    ax.set_xlabel("Angle θ (radians)"); ax.set_ylabel("Prediction")
    ax.set_title("Circle prediction at physical time 1000"+suffix)
    ax.legend(fontsize=8, ncol=2); ax.grid(alpha=.18)
    save(fig, "final_circle_prediction")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    for model in MODELS:
        for seed_index, seed in enumerate(SEEDS):
            run = diagnostic.get((model, seed))
            if run is None:
                continue
            for ax, clock, xlabel in zip(axes, ("checkpoint_wall_seconds", "checkpoint_nfev_ode"),
                                        ("Worker wall seconds", "ODE RHS evaluations")):
                ax.plot(run[clock], np.maximum(run["train"]["mse"], 1e-18), color=colors[model],
                        alpha=.5+.2*(seed_index==0), label=labels[model] if seed_index==0 else None)
                ax.set_yscale("log"); ax.set_xlabel(xlabel); ax.set_ylabel("Training mean squared error")
                ax.grid(alpha=.18)
    axes[0].legend(fontsize=8)
    fig.suptitle("Recorded cost of each fixed-seed trajectory"+suffix, fontsize=11)
    save(fig, "loss_wall_rhs")


def write_report(output, summary, endpoint_rows):
    models, separations = summary["models"], summary["separations"]
    def fmt(value):
        return "unavailable" if value is None else f"{value:.6g}"
    lines = ["# Smooth mixed-frequency circle: canonical-flow results", ""]
    for control, result in separations.items():
        ratio = result["closure_over_dense_median_rmse"]
        lines += [f"Against {control}: **{result['conclusion']}**. Closure/dense median terminal training RMSE ratio: {fmt(ratio)}.", ""]
    lines += ["These are descriptive results for the three fixed seeds 20260921–20260923, the explicit finite initialized dictionary, and physical time 1000. They do not establish a representation lower bound, a population approximation theorem, a nonlazy theorem, or an all-time advantage.", "",
        "The fixed regression target is `sqrt(32/21)*(cos(theta)+sin(3*theta)/2+cos(5*theta)/4)`, with unit mean square. Training uses 126 equally spaced unit-circle x values and u=x/sqrt(2); the passive panel uses 1024 midpoint angles. Both hidden layers use tanh, canonical Gaussian initialization, unhalved squared loss, and raw block mobilities (n,1,n).", "",
        "| Model | Trainable / retained predictor scalars | Fits / 3 | Median training RMSE | Median passive RMSE | Numerical gates |",
        "|---|---:|---:|---:|---:|---|"]
    for model in MODELS:
        row = models[model]
        lines.append(f"| {model} | {row['trainable_scalars']} / {row['retained_predictor_scalars']} | {row.get('fit_count','unresolved')} | {fmt(row.get('train_median_rmse'))} | {fmt(row.get('passive_median_rmse'))} | {'pass' if row['numerically_valid'] else 'unresolved'} |")
    lines += ["", "A fit means MSE≤0.001. The strong-separation rule additionally requires closure fits on at least two seeds, dense fits on no seeds, and a closure median RMSE at most one third the dense median. Error ratios remain informative when that conjunction fails; fitting by both methods does not by itself imply equal accuracy or equal fitting time.", "",
        "| Model | Seed | Level | Last saved t | Training RMSE | Passive RMSE | First saved fit t | Hidden RMS motion (layer 1, 2) |",
        "|---|---:|---|---:|---:|---:|---:|---|"]
    for row in endpoint_rows:
        lines.append(f"| {row['model']} | {row['seed']} | {row['level']} | {fmt(row['physical_time'])} | {fmt(row['train_rmse'])} | {fmt(row['passive_rmse'])} | {fmt(row['first_saved_fit_time'])} | {fmt(row['hidden1_rms_motion'])}, {fmt(row['hidden2_rms_motion'])} |")
    lines += ["", "First saved fit times only bracket a crossing between the preceding checkpoint and the displayed time. `endpoints.csv` retains those brackets. Missing fit times mean no saved checkpoint met the threshold. Hidden motion is descriptive.", "",
        "Fourier coefficients on each panel are `a_k=2 mean(f cos(k theta))` and `b_k=2 mean(f sin(k theta))`. Harmonic loss is `((a_k-a_target)^2+(b_k-b_target)^2)/2`; outside energy is the mean square after removing the predicted harmonics 1,3,5. Their sum reconstructs the total MSE to roundoff. Full per-seed coefficients, coefficient errors and outside energies for both panels are in `harmonics.csv`; every saved time appears in `checkpoints.csv` and `analysis.json`.", "",
        "![Loss versus physical time](loss_physical_time.png)", "",
        "![Harmonic losses](harmonic_loss.png)", "",
        "![Final passive predictions](final_circle_prediction.png)", "",
        "The physical-time and harmonic plots show medians and ranges across the fixed seeds; these ranges are not confidence intervals. Cost curves retain each seed separately. Corresponding PDF files are provided for export.", ""]
    comparisons = summary["comparisons"]
    if comparisons:
        maximum_prediction = max(max(c.get(p+"_prediction_max_difference",0) for p in ("train", "passive")) for c in comparisons)
        maximum_rmse = max(max(c.get(p+"_rmse_max_difference",0) for p in ("train", "passive")) for c in comparisons)
        lines += [f"Across all retained refinement comparisons, the largest saved prediction discrepancy was {maximum_prediction:.6g} and the largest RMSE discrepancy was {maximum_rmse:.6g}. Failed coarse comparisons remain recorded; the selected pair alone determines resolution acceptance.", ""]
    lines += ["| Model | First-seed reproduction |", "|---|---|"]
    for model in MODELS:
        row = summary["reproductions"][model]
        lines.append(f"| {model} | {'pass' if row['pass'] else 'unresolved'} |")
    budget = summary["budget"]
    lines += ["", f"The {budget['attempt_count']} retained worker attempts used {budget['worker_process_wall_seconds']:.3f} cumulative process wall seconds against the 4200-second allowance. Maximum worker wall time was {budget['max_worker_seconds']:.3f} seconds. This accounting includes failed and reproduction attempts. Numerical integration, full-array replay, saved-array metrics, source hashes, and budget checks are recorded separately in `analysis.json`.", "",
        "The numerical gates compare both panels at all 19 checkpoints, all three parameter blocks, terminal fit decisions, and accepted-step loss monotonicity. Selected first-seed reproductions additionally compare parameters, predictions, and all saved fit decisions. Independent replay checks the raw-state forward map and RHS; this analysis independently recomputes metrics and selection from saved arrays.", ""]
    if summary["issues"] or summary["unavailable_runs"]:
        lines += ["Unresolved validity issues:", ""]
        lines += ["- "+issue for issue in summary["issues"]]
        lines += ["- Unavailable retained run: "+str(row) for row in summary["unavailable_runs"]]
        lines.append("")
    lines += ["No additional target, seed, width, initialization, optimizer, horizon or tolerance search is implied by this report. The prescribed experiment terminates with this comparison regardless of outcome.", "",
        f"Provenance: manifest SHA-256 `{summary['manifest_sha256']}`; analyzer SHA-256 `{summary['analyzer_sha256']}`; protocol SHA-256 `{summary['protocol_sha256']}`.", ""]
    text = "\n".join(lines)
    (output/"report.md").write_text(text)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    started, cpu_started = time.perf_counter(), time.process_time()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    summary, diagnostic = aggregate(args.runs, args.replay)
    endpoints = write_tables(output, diagnostic)
    write_plots(output, diagnostic, summary)
    report = write_report(output, summary, endpoints)
    if args.report:
        if args.report.exists():
            raise ValueError("refusing to overwrite existing report")
        # Study report links are relative to the study rather than analysis output.
        relative = os.path.relpath(output, args.report.resolve().parent)
        for stem in ("loss_physical_time", "harmonic_loss", "final_circle_prediction"):
            report = report.replace("("+stem+".png)", "("+relative+"/"+stem+".png)")
        args.report.write_text(report)
    summary["analysis_process"] = {"wall_seconds": time.perf_counter()-started,
        "cpu_seconds": time.process_time()-cpu_started, "python": sys.version,
        "numpy": np.__version__, "platform": platform.platform(), "command": sys.argv,
        "cwd": str(Path.cwd())}
    summary["output_sha256"] = {p.name: sha256(p) for p in output.iterdir() if p.is_file()}
    _write_json(output/"analysis.json", summary)
    print(json.dumps({"separations": summary["separations"], "issues": summary["issues"],
                      "analysis_wall_seconds": summary["analysis_process"]["wall_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
