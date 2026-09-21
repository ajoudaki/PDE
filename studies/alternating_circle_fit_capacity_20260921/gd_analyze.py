#!/usr/bin/env python3
"""Independent NumPy replay and reporting for the frozen GD-only campaign.

This program imports no training code and performs no optimization. It reads
all launches, including failed attempts, and keeps each seed and reproduction
separate. Circle-grid predictions have no assumed target between samples.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
from typing import Any

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np

FIT_MSE = 1e-3
PRED_TOL = 1e-8
MSE_TOL = 1e-9
SEEDS = (20260921, 20260922, 20260923)
LADDER = (30, 62, 126, 254)
MODEL_ORDER = ("width55", "closure1024", "width105")
MODEL_LABELS = {
    "width55": "Dense width 55 (3,190 trainable)",
    "closure1024": "Closure n=1024, p=1 (3,087 trainable)",
    "width105": "Dense width 105 (11,340 retained)",
}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as values:
        return {name: np.array(values[name], copy=True) for name in values.files}


def clean(value: Any) -> Any:
    """Produce strict JSON while preserving unavailable/nonfinite diagnostics."""
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if isinstance(value, np.ndarray):
        return clean(value.tolist())
    if isinstance(value, (np.floating, float)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.bool_):
        return bool(value)
    return value


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(clean(value), indent=2, allow_nan=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: json.dumps(clean(value), sort_keys=True) if isinstance(value, (dict, list)) else clean(value) for key, value in row.items()})


def metrics(prediction: np.ndarray, target: np.ndarray) -> dict[str, Any]:
    prediction = np.asarray(prediction, dtype=np.float64).reshape(-1)
    target = np.asarray(target, dtype=np.float64).reshape(-1)
    if prediction.shape != target.shape:
        raise ValueError("Prediction/target shape mismatch")
    finite = bool(np.all(np.isfinite(prediction)))
    error = prediction - target
    mse = float(np.mean(error * error)) if finite else None
    signs = int(np.count_nonzero(~(target * prediction > 0)))
    return {
        "mse": mse, "rmse": np.sqrt(mse) if mse is not None else None,
        "sign_errors": signs,
        "max_abs_error": float(np.max(np.abs(error))) if finite else None,
        "minimum_signed_margin": float(np.min(target * prediction)) if finite else None,
        "finite": finite, "fit": bool(finite and mse <= FIT_MSE and signs == 0),
    }


def forward_and_gradient(model: str, state: dict[str, np.ndarray], initial: dict[str, np.ndarray], u: np.ndarray, y: np.ndarray | None = None) -> tuple[np.ndarray, dict[str, float] | None]:
    """Direct array reconstruction in canonical W,middle,c coordinates."""
    W = np.asarray(state["W"], dtype=np.float64)
    c = np.asarray(state["c"], dtype=np.float64).reshape(-1)
    n = W.shape[0]
    if W.shape != (n, 2) or c.shape != (n,) or u.shape[1:] != (2,):
        raise ValueError("Invalid input or canonical W/c dimensions")
    first = np.tanh(W @ u.T)
    if model == "network":
        middle = np.asarray(state["A"], dtype=np.float64)
        if middle.shape != (n, n):
            raise ValueError("Invalid dense A dimensions")
        second = np.tanh(middle @ first)
    elif model == "closure":
        B1 = np.asarray(initial["B1"], dtype=np.float64)
        B2 = np.asarray(initial["B2"], dtype=np.float64)
        middle = np.asarray(state["M"], dtype=np.float64)
        if B1.shape != (n, 5) or B2.shape != (n, 3) or middle.shape != (3, 5):
            raise ValueError("Invalid closure dictionary or M dimensions")
        features = B1.T @ first / n
        second = np.tanh(B2 @ middle @ features)
    else:
        raise ValueError(f"Unknown model {model!r}")
    prediction = (c / n) @ second
    if y is None:
        return prediction, None
    derivative = 2 * (prediction - y) / y.size
    second_gradient = (c / n)[:, None] * derivative[None, :] * (1 - second * second)
    gc = second @ derivative / n
    if model == "network":
        gm = second_gradient @ first.T
        first_gradient = middle.T @ second_gradient
    else:
        reduced_gradient = B2.T @ second_gradient
        gm = reduced_gradient @ features.T
        first_gradient = B1 @ (middle.T @ reduced_gradient) / n
    gw = (first_gradient * (1 - first * first)) @ u
    squared = {"W": float(np.sum(gw * gw)), "middle": float(np.sum(gm * gm)), "c": float(gc @ gc)}
    Q = n * squared["W"] + squared["middle"] + n * squared["c"]
    return prediction, {
        "W_gradient_norm": np.sqrt(squared["W"]),
        "middle_gradient_norm": np.sqrt(squared["middle"]),
        "c_gradient_norm": np.sqrt(squared["c"]),
        "raw_gradient_norm": np.sqrt(sum(squared.values())),
        "physical_gradient_squared": Q,
        "physical_gradient_norm": np.sqrt(Q),
        "W_norm": float(np.linalg.norm(W)),
        "middle_norm": float(np.linalg.norm(middle)),
        "c_norm": float(np.linalg.norm(c)),
    }


def close_number(actual: Any, expected: Any, atol: float = 1e-12, rtol: float = 1e-12) -> bool:
    try:
        return bool(np.isfinite(actual) and np.isfinite(expected)
                    and abs(float(actual) - float(expected)) <= atol + rtol * abs(float(expected)))
    except (TypeError, ValueError):
        return False


def audit_trace(record: dict[str, Any], trace: list[dict[str, Any]]) -> dict[str, Any]:
    config = record["config"]
    failures: list[str] = []
    normalized = []
    clock, rejections, last_eta = 0.0, 0, None
    if not trace or trace[0].get("accepted_step") != 0:
        return {"valid": False, "failures": ["Missing initial trace entry"], "normalized": []}
    if trace[0].get("phase") != "initial" or trace[0].get("physical_clock") != 0 or trace[0].get("forward_evaluations") != 1:
        failures.append("Initial trace phase/clock/forward count mismatch")
    previous_loss = float(trace[0]["mse"])
    normalized.append({"mse": previous_loss, "physical_clock": 0.0, "accepted_steps": 0, "eta": None, "physical_Q": None})
    eta_values = []
    q_values = []
    for index, entry in enumerate(trace[1:], 1):
        here = []
        eta, halvings = float(entry["eta"]), int(entry["halvings"])
        q = float(entry["gradient_from_previous"]["physical_Q"])
        expected_first = min(float(config["eta_max"]), float(config["eta_max"]) if last_eta is None else 2 * last_eta,
                             float(config["max_physical_clock"]) - clock)
        expected_eta = expected_first * 2.0 ** -halvings
        expected_slack = 1e-14 * max(1.0, previous_loss)
        expected_armijo = previous_loss - 1e-4 * eta * q + expected_slack
        if entry.get("accepted_step") != index or entry.get("phase") != "gd":
            here.append("index/phase")
        if not 0 <= halvings <= 30 or not 0 < eta <= float(config["eta_max"]):
            here.append("step bound")
        if not close_number(entry.get("eta_first"), expected_first, atol=1e-14, rtol=1e-14) or not close_number(eta, expected_eta, atol=1e-14, rtol=1e-14):
            here.append("step schedule")
        if not close_number(entry.get("previous_mse"), previous_loss, atol=1e-14, rtol=1e-14):
            here.append("previous loss")
        gradient = entry["gradient_from_previous"]
        blocks = gradient["canonical_blocks"]
        middle_key = "A" if config["model"] == "network" else "M"
        block_q = config["width"] * (float(blocks["W"]) ** 2 + float(blocks["c"]) ** 2) + float(blocks[middle_key]) ** 2
        if not close_number(q, block_q, atol=1e-26, rtol=1e-11) or not np.isfinite(q) or q < config["gradient_floor"]:
            here.append("physical gradient norm")
        if not close_number(entry.get("armijo_roundoff_slack"), expected_slack, atol=1e-28, rtol=1e-13):
            here.append("Armijo slack")
        if not close_number(entry.get("armijo_threshold"), expected_armijo, atol=1e-14, rtol=1e-14):
            here.append("Armijo formula")
        if not np.isfinite(entry["mse"]) or entry["mse"] > expected_armijo + 2e-15 * max(1.0, abs(expected_armijo)):
            here.append("Armijo acceptance")
        clock += eta
        rejections += halvings
        if not close_number(entry.get("physical_clock"), clock, atol=1e-10, rtol=1e-13):
            here.append("clock sum")
        if entry.get("rejected_trials") != halvings or entry.get("rejected_trials_total") != rejections:
            here.append("rejection count")
        if entry.get("forward_evaluations") != 1 + index + rejections:
            here.append("forward count")
        if here:
            failures.append(f"Accepted step {index}: " + ", ".join(here))
        previous_loss, last_eta = float(entry["mse"]), eta
        eta_values.append(eta)
        q_values.append(q)
        normalized.append({"mse": previous_loss, "physical_clock": clock, "accepted_steps": index, "eta": eta, "physical_Q": q})
    accepted = len(trace) - 1
    unfinished = record.get("unfinished_line_search") or {}
    tail_rejections = int(unfinished.get("rejected_trials", 0))
    if record.get("accepted_steps") != accepted:
        failures.append("Record accepted-step count mismatch")
    if not close_number(record.get("physical_clock"), clock, atol=1e-10, rtol=1e-13):
        failures.append("Record physical clock mismatch")
    if record.get("rejected_trials") != rejections + tail_rejections:
        failures.append("Record rejection count mismatch")
    if record.get("forward_evaluations") != 1 + accepted + rejections + tail_rejections:
        failures.append("Record forward-evaluation count mismatch")
    if accepted > config["max_accepted_steps"] or clock > config["max_physical_clock"] + 1e-10 or record["forward_evaluations"] > config["max_forward_evals"]:
        failures.append("Per-attempt accepted-step/evaluation/clock cap exceeded")
    if record.get("elapsed_seconds_before_final_record_write", float("inf")) > config["max_seconds"]:
        failures.append("Per-attempt wall-clock cap exceeded")
    if record.get("status") == "step_limit" and accepted != config["max_accepted_steps"]:
        failures.append("Step-limit reason without step cap")
    if record.get("status") == "physical_clock_limit" and not close_number(clock, config["max_physical_clock"], atol=1e-10, rtol=0):
        failures.append("Physical-clock reason without clock cap")
    if record.get("status") == "evaluation_limit" and record.get("forward_evaluations") != config["max_forward_evals"]:
        failures.append("Evaluation-limit reason without evaluation cap")
    losses = [float(entry["mse"]) for entry in trace]
    diagnostics = record.get("diagnostics", {})
    if not close_number(diagnostics.get("best", {}).get("mse"), min(losses), atol=MSE_TOL, rtol=0):
        failures.append("Best checkpoint loss not best accepted/initial loss")
    if not close_number(diagnostics.get("final", {}).get("mse"), losses[-1], atol=MSE_TOL, rtol=0):
        failures.append("Final checkpoint loss not terminal accepted loss")
    if record.get("status") == "gradient_floor" and not diagnostics.get("final", {}).get("gradient", {}).get("physical_Q", float("inf")) < config["gradient_floor"]:
        failures.append("Gradient-floor reason without gradient floor")
    if record.get("status") == "fit_reached" and not (losses[-1] <= FIT_MSE and trace[-1].get("sign_errors") == 0):
        failures.append("Fit stop without terminal fit")
    if any(entry["mse"] <= FIT_MSE and entry.get("sign_errors") == 0 for entry in trace[:-1]):
        failures.append("Training continued after an earlier accepted fitting state")
    if any(float(after["elapsed_seconds"]) < float(before["elapsed_seconds"]) for before, after in zip(trace, trace[1:])):
        failures.append("Trace elapsed seconds decreased")
    phases = record.get("phase_counts", {})
    if phases.get("gd_accepted") != accepted or phases.get("gd_trial_forwards") != record["forward_evaluations"] - 1:
        failures.append("Phase counters disagree with accepted/forward counts")
    return {"valid": not failures, "failures": failures, "accepted_steps": accepted,
            "physical_clock": clock, "rejected_trials_completed_searches": rejections,
            "unfinished_rejected_trials": tail_rejections,
            "eta_min": min(eta_values) if eta_values else None,
            "eta_max_realized": max(eta_values) if eta_values else None,
            "eta_median": float(np.median(eta_values)) if eta_values else None,
            "eta_mean": float(np.mean(eta_values)) if eta_values else None,
            "first_Q": q_values[0] if q_values else None,
            "last_previous_Q": q_values[-1] if q_values else None,
            "normalized": normalized}


def scan_attempt(path: Path, run_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    record = json.loads((path / "record.json").read_text())
    config = record["config"]
    width, m, seed = int(config["width"]), int(config["m"]), int(config["seed"])
    model = config["model"]
    relative = str(path.relative_to(run_root))
    row: dict[str, Any] = {
        "attempt": relative, "model": f"width{width}" if model == "network" else f"closure{width}",
        "m": m, "seed": seed, "initialization": "high" if config["gain"] == "rescue" else "canonical",
        "first_weight_gain": record.get("first_weight_gain"), "eta_max": float(config["eta_max"]),
        "device": config.get("device"),
        "reproduction": "repro" in relative.lower() or "repeat" in relative.lower(),
        "terminal_reason": record.get("status"), "producer_fit": record.get("fit"),
        "precision_limited_endpoint": record.get("status") == "gradient_floor",
        "producer_numerical_valid": record.get("numerical_valid"),
        "producer_budget_respected": record.get("budget_respected"),
        "accepted_steps": record.get("accepted_steps"), "physical_clock": record.get("physical_clock"),
        "forward_evaluations": record.get("forward_evaluations"), "rejected_trials": record.get("rejected_trials"),
        "nonfinite_rejected_trials": record.get("nonfinite_rejected_trials"),
        "attempt_elapsed_seconds": record.get("elapsed_seconds_before_final_record_write"),
        "initialization_seconds": record.get("phase_times", {}).get("initialization_seconds"),
        "gd_seconds": record.get("phase_times", {}).get("gd_seconds"),
        "export_seconds": record.get("phase_times", {}).get("export_seconds"),
        "trainable_scalars": width * width + 3 * width if model == "network" else 3 * width + 15,
        "retained_predictor_scalars": width * width + 3 * width if model == "network" else 11 * width + 15,
        "record_sha256": file_sha256(path / "record.json"),
        "raw_replay_valid": False, "trace_valid": False, "decision_valid": False,
        "accepted_fit": False, "errors": [],
    }
    payload: dict[str, Any] = {"row": row, "record": record, "normalized_trace": []}
    try:
        dataset = load_npz(path / "dataset.npz")
        y = np.asarray(dataset["y"], dtype=np.float64).reshape(-1)
        u = np.asarray(dataset["u"], dtype=np.float64)
        theta = np.asarray(dataset["theta"], dtype=np.float64).reshape(-1)
        expected_theta = 2 * np.pi * np.arange(m) / m
        expected_u = np.column_stack((np.cos(expected_theta), np.sin(expected_theta))) / np.sqrt(2)
        data_valid = bool(y.shape == (m,) and u.shape == (m, 2) and theta.shape == (m,)
                          and np.array_equal(y, (-1.0) ** np.arange(m))
                          and np.max(np.abs(theta - expected_theta)) <= 1e-14
                          and np.max(np.abs(u - expected_u)) <= 1e-14)
        row["dataset_valid"] = data_valid
        initial = load_npz(path / "initial.npz")
        saved_predictions = load_npz(path / "predictions.npz")
        replay_valid = data_valid
        payload.update({"theta": theta, "y": y, "predictions": {}})
        for name in ("initial", "best", "final"):
            state = initial if name == "initial" else load_npz(path / f"{name}.npz")
            if any(state[key].dtype != np.dtype("float64") for key in ("W", "c", "A" if model == "network" else "M")):
                raise ValueError("Retained canonical state is not float64")
            prediction, gradient = forward_and_gradient(model, state, initial, u, y)
            values = metrics(prediction, y)
            payload["predictions"][name] = prediction
            for key, value in {**values, **gradient}.items():
                row[f"{name}_{key}"] = value
            saved = np.asarray(saved_predictions[f"{name}_train"]).reshape(-1)
            pred_error = float(np.max(np.abs(prediction - saved)))
            diagnostic = record["diagnostics"][name]
            row[f"{name}_saturation"] = diagnostic.get("saturation")
            mse_error = abs(values["mse"] - diagnostic["mse"]) if values["mse"] is not None else None
            circle_u = np.asarray(dataset["circle_u"], dtype=np.float64)
            circle_prediction = np.concatenate([forward_and_gradient(model, state, initial, circle_u[i:i + 512])[0]
                                                for i in range(0, len(circle_u), 512)])
            circle_error = float(np.max(np.abs(circle_prediction - np.asarray(saved_predictions[f"{name}_circle"]).reshape(-1))))
            gradient_q_error = abs(gradient["physical_gradient_squared"] - diagnostic["gradient"]["physical_Q"])
            gradient_valid = close_number(gradient["physical_gradient_squared"], diagnostic["gradient"]["physical_Q"], atol=1e-16, rtol=1e-7)
            valid = bool(values["finite"] and pred_error <= PRED_TOL and circle_error <= PRED_TOL
                         and mse_error is not None and mse_error <= MSE_TOL and gradient_valid)
            row.update({f"{name}_prediction_discrepancy": pred_error,
                        f"{name}_circle_prediction_discrepancy": circle_error,
                        f"{name}_mse_discrepancy": mse_error,
                        f"{name}_gradient_Q_discrepancy": gradient_q_error,
                        f"{name}_replay_valid": valid})
            replay_valid = replay_valid and valid
        row["raw_replay_valid"] = replay_valid
        row["fit_flag_agrees"] = row["best_fit"] == bool(record.get("fit"))
        row["optimizer_metadata_valid"] = bool(record.get("block_mobilities") == [width, 1, width]
            and record.get("trainable_scalar_count") == row["trainable_scalars"]
            and config["gain"] in ("primary", "rescue")
            and record.get("first_weight_gain") == (1 if config["gain"] == "primary" else m / 2)
            and config["eta_max"] in (1.0, .5) and m in LADDER and seed in SEEDS
            and config["max_accepted_steps"] == 30000 and config["max_forward_evals"] == 90000
            and config["max_physical_clock"] == 10000 and config["max_seconds"] == 75
            and config["export_reserve_seconds"] == 5)
        environment = record.get("environment", {})
        row["environment_valid"] = bool(environment.get("torch_threads") == 1
            and environment.get("torch_interop_threads") == 1 and environment.get("deterministic_algorithms") is True
            and environment.get("tf32") is False and environment.get("cudnn_tf32") is False
            and config.get("threads") == 1 and str(config.get("device", "")).startswith("cuda:"))
        outputs_hashes = record.get("outputs_sha256", {})
        row["output_hashes_valid"] = bool(outputs_hashes and all((path / filename).is_file() and file_sha256(path / filename) == digest
                                                                  for filename, digest in outputs_hashes.items()))
    except Exception as exc:
        row["errors"].append(f"Replay: {type(exc).__name__}: {exc}")
    try:
        trace = [json.loads(line) for line in (path / "trace.jsonl").read_text().splitlines() if line.strip()]
        audit = audit_trace(record, trace)
        payload["normalized_trace"] = audit.pop("normalized")
        row["trace_valid"] = audit["valid"]
        row["trace_audit"] = audit
        for key in ("eta_min", "eta_max_realized", "eta_mean", "eta_median"):
            row[key] = audit.get(key)
    except Exception as exc:
        row["errors"].append(f"Trace: {type(exc).__name__}: {exc}")
    row["decision_valid"] = bool(row["raw_replay_valid"] and row["trace_valid"] and row.get("fit_flag_agrees")
        and row.get("optimizer_metadata_valid") and row.get("environment_valid") and row.get("output_hashes_valid")
        and record.get("numerical_valid") and record.get("budget_respected")
        and record.get("status") not in ("error", "nonfinite", "line_search_failed", "interrupted", "initializing"))
    row["accepted_fit"] = bool(row["decision_valid"] and row.get("best_fit"))
    return row, payload


def attach_manifest(run_root: Path, rows: list[dict[str, Any]]) -> dict[str, Any]:
    path = run_root / "run_record.json"
    manifest = json.loads(path.read_text())
    by_attempt = {row["attempt"]: row for row in rows}
    failures = []
    spent = 0.0
    jobs = manifest.get("jobs", [])
    seen_outputs = set()
    for job in jobs:
        output = Path(job["output"])
        if not output.is_absolute():
            output = Path(job.get("cwd", run_root)) / output
        relative = str(output.resolve().relative_to(run_root))
        if relative in seen_outputs:
            failures.append(f"Repeated launch output: {relative}")
        seen_outputs.add(relative)
        row = by_attempt.get(relative)
        if row is None:
            width = int(job["width"])
            row = {"attempt": relative, "model": f"width{width}" if job["model"] == "network" else f"closure{width}",
                   "m": int(job["m"]), "seed": int(job["seed"]),
                   "initialization": "high" if job["gain"] == "rescue" else "canonical",
                   "eta_max": float(job["eta_max"]), "device": job.get("device"),
                   "raw_replay_valid": False, "trace_valid": False, "decision_valid": False,
                   "accepted_fit": False, "terminal_reason": "missing_attempt_record",
                   "errors": ["Recorded launch has no readable attempt record"]}
            rows.append(row)
            by_attempt[relative] = row
        row.update({"stage": job.get("stage"), "reproduction": job.get("stage") == "reproduction",
                    "process_returncode": job.get("returncode"), "process_wall_seconds": job.get("process_wall_seconds"),
                    "supervisor_failure": job.get("supervisor_failure"), "original_output": job.get("original_output")})
        job_model = f"width{job['width']}" if job["model"] == "network" else f"closure{job['width']}"
        row["launch_settings_valid"] = bool(row["model"] == job_model and row["m"] == job["m"] and row["seed"] == job["seed"]
                                            and row["eta_max"] == job["eta_max"] and row["device"] == job["device"]
                                            and row["initialization"] == ("high" if job["gain"] == "rescue" else "canonical"))
        row["decision_valid"] = bool(row["decision_valid"] and row["launch_settings_valid"]
                                     and job.get("returncode") == 0 and not job.get("supervisor_failure"))
        row["accepted_fit"] = bool(row["decision_valid"] and row.get("best_fit"))
        duration = job.get("process_wall_seconds")
        if duration is None or not np.isfinite(duration) or duration < 0 or duration > 85:
            failures.append(f"Invalid or over-reservation worker duration: {relative}")
        else:
            spent += float(duration)
    orphaned = set(by_attempt) - seen_outputs
    if orphaned:
        failures.append("Attempt records absent from launch manifest: " + ", ".join(sorted(orphaned)))
        for name in orphaned:
            by_attempt[name]["decision_valid"] = False
            by_attempt[name]["accepted_fit"] = False
    if len(jobs) > 51:
        failures.append("More than 51 launches")
    if not close_number(spent, manifest.get("spent_worker_seconds"), atol=1e-8, rtol=1e-12):
        failures.append("Worker-time sum disagrees with manifest")
    if spent > 2500 or manifest.get("worker_wall_cap") != 2500:
        failures.append("Cumulative worker wall cap mismatch/exceeded")
    # The runner launches groups in fixed pairs, then a final singleton. Every
    # next group is reserved before launch; actual durations fund later stages.
    previous_spent, index = 0.0, 0
    grouping_keys = ("stage", "model", "width", "m", "gain", "eta_max")
    while index < len(jobs):
        group = [jobs[index]]
        if index + 1 < len(jobs) and jobs[index].get("stage") != "reproduction" and all(jobs[index].get(key) == jobs[index + 1].get(key) for key in grouping_keys):
            group.append(jobs[index + 1])
        if previous_spent + 85 * len(group) > 2500 + 1e-8:
            failures.append(f"Launch reservation exceeded cap at job {index}")
        if len({job.get("device") for job in group}) != len(group):
            failures.append(f"Concurrent batch reused a GPU at job {index}")
        previous_spent += sum(float(job.get("process_wall_seconds") or 0) for job in group)
        index += len(group)
    return {"path": str(path), "sha256": file_sha256(path), "manifest": manifest,
            "budget_valid": not failures, "budget_failures": failures,
            "computed_worker_seconds": spent, "launch_count": len(jobs)}


def audit_reproductions(rows: list[dict[str, Any]], payloads: list[dict[str, Any]], run_root: Path, selected: int | None) -> dict[str, Any]:
    checks = []
    traces = {payload["row"]["attempt"]: payload.get("normalized_trace", []) for payload in payloads}
    if selected is None:
        return {"complete": False, "all_stable": False, "checks": []}
    for eta in (1.0, 0.5):
        for model in MODEL_ORDER:
            originals = members_for(rows, model, selected, "high", eta)
            successes = [row for row in originals if row.get("accepted_fit")]
            preferred = min(successes or originals, key=lambda row: row["seed"], default=None)
            repeats = [row for row in rows if row["reproduction"] and row["model"] == model
                       and row["m"] == selected and row["initialization"] == "high" and row["eta_max"] == eta]
            check: dict[str, Any] = {"model": model, "eta_max": eta, "complete": len(repeats) == 1 and preferred is not None,
                                     "expected_seed": preferred["seed"] if preferred else None, "stable": False}
            if len(repeats) == 1 and preferred is not None:
                repeat = repeats[0]
                check.update(original=preferred["attempt"], repetition=repeat["attempt"], actual_seed=repeat["seed"])
                provenance_valid = bool(repeat["seed"] == preferred["seed"] and repeat["device"] == preferred["device"]
                    and repeat.get("original_output") is not None
                    and Path(repeat["original_output"]).resolve() == (run_root / preferred["attempt"]).resolve())
                final_error = abs(preferred["final_mse"] - repeat["final_mse"]) if preferred.get("final_mse") is not None and repeat.get("final_mse") is not None else None
                best_error = abs(preferred["best_mse"] - repeat["best_mse"]) if preferred.get("best_mse") is not None and repeat.get("best_mse") is not None else None
                same_fit = bool(preferred.get("best_fit") == repeat.get("best_fit"))
                check.update(provenance_valid=provenance_valid, final_mse_difference=final_error,
                             best_mse_difference=best_error, same_fit=same_fit,
                             same_stopping_reason=preferred.get("terminal_reason") == repeat.get("terminal_reason"))
                check["stable"] = bool(provenance_valid and preferred["decision_valid"] and repeat["decision_valid"]
                                       and same_fit and final_error is not None and final_error <= 1e-6)
                check["accepted_steps"] = [preferred.get("accepted_steps"), repeat.get("accepted_steps")]
                time_censored = (preferred.get("accepted_steps") != repeat.get("accepted_steps")
                                 and "time_limit" in (preferred.get("terminal_reason"), repeat.get("terminal_reason")))
                check["time_censored"] = time_censored
                prefix = list(zip(traces.get(preferred["attempt"], []), traces.get(repeat["attempt"], [])))
                shared: dict[str, Any] = {"accepted_states": len(prefix)}
                for field in ("mse", "physical_clock", "eta", "physical_Q"):
                    differences = [abs(a[field] - b[field]) for a, b in prefix if a.get(field) is not None and b.get(field) is not None]
                    shared[f"maximum_{field}_difference"] = max(differences) if differences else None
                shared["identical_logged_mse_clock_eta_Q"] = bool(prefix and all(all(a.get(field) == b.get(field)
                    for field in ("accepted_steps", "mse", "physical_clock", "eta", "physical_Q")) for a, b in prefix))
                check["shared_prefix"] = shared
                check["classification"] = ("endpoint_pass" if check["stable"] else "time_censored" if time_censored
                                           else "endpoint_discrepancy" if provenance_valid else "provenance_failure")
                repeat["reproduction_audit"] = check.copy()
            checks.append(check)
    return {"complete": all(check["complete"] for check in checks),
            "all_stable": all(check["stable"] for check in checks), "checks": checks}


def members_for(rows: list[dict[str, Any]], model: str, m: int, gain: str, eta: float) -> list[dict[str, Any]]:
    return [row for row in rows if row["model"] == model and row["m"] == m
            and row["initialization"] == gain and row["eta_max"] == eta
            and not row["reproduction"]]


def group_status(members: list[dict[str, Any]]) -> dict[str, Any]:
    complete = len(members) == len(SEEDS) and {row["seed"] for row in members} == set(SEEDS)
    valid = bool(complete and all(row.get("decision_valid", False) for row in members))
    values = [row["best_mse"] for row in members if row.get("best_mse") is not None]
    return {
        "attempts": len(members), "complete_seed_set": complete,
        "all_valid": valid, "valid_attempts": sum(bool(row.get("decision_valid")) for row in members),
        "fits": sum(bool(row.get("accepted_fit")) for row in members),
        "minimum_mse": min(values) if values else None,
        "maximum_mse": max(values) if values else None,
        "seeds": [row["seed"] for row in members],
    }


def group_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups = []
    for m in LADDER:
        for gain in ("high", "canonical"):
            for eta in (1.0, 0.5):
                for model in MODEL_ORDER:
                    members = members_for(rows, model, m, gain, eta)
                    if members:
                        groups.append({"model": model, "m": m, "initialization": gain,
                                       "eta_max": eta, **group_status(members)})
    return groups


def audit_selection(rows: list[dict[str, Any]], recorded: int | None) -> dict[str, Any]:
    gates, candidate, prefix_valid = [], None, True
    for m in LADDER:
        dense = group_status(members_for(rows, "width55", m, "high", 1.0))
        closure = group_status(members_for(rows, "closure1024", m, "high", 1.0))
        if dense["attempts"] == 0 and closure["attempts"] == 0:
            continue
        valid = dense["all_valid"] and closure["all_valid"]
        qualifies = bool(valid and dense["fits"] == 0 and closure["fits"] >= 2)
        gates.append({"m": m, "width55": dense, "closure1024": closure,
                      "candidate": qualifies, "prefix_valid_before": prefix_valid})
        if candidate is None and qualifies:
            candidate = m
        if candidate is None:
            prefix_valid = bool(prefix_valid and valid)
    ladder_complete = len(gates) == len(LADDER) and all(g["width55"]["complete_seed_set"] and g["closure1024"]["complete_seed_set"] for g in gates)
    selected = candidate if candidate is not None else 254 if ladder_complete else None
    selected_prefix = [gate for gate in gates if selected is not None and gate["m"] <= selected]
    sequence_valid = bool(selected is not None and len(selected_prefix) == LADDER.index(selected) + 1
                          and all(g["width55"]["all_valid"] and g["closure1024"]["all_valid"] for g in selected_prefix)
                          and not any(g["m"] > selected for g in gates))
    return {"selected_m": selected, "candidate_m": candidate,
            "recorded_selected_m": recorded, "agrees_with_manifest": selected == recorded,
            "selection_sequence_valid": sequence_valid, "ladder_complete": ladder_complete,
            "gates": gates}


def audit_comparisons(rows: list[dict[str, Any]], m: int | None) -> dict[str, Any]:
    comparisons: dict[str, Any] = {}
    if m is None:
        return comparisons
    for dense in ("width55", "width105"):
        caps = []
        for eta in (1.0, 0.5):
            closure_status = group_status(members_for(rows, "closure1024", m, "high", eta))
            dense_status = group_status(members_for(rows, dense, m, "high", eta))
            valid = closure_status["all_valid"] and dense_status["all_valid"]
            caps.append({"eta_max": eta, "closure": closure_status, "dense": dense_status,
                         "valid": valid,
                         "separation": bool(valid and closure_status["fits"] >= 2 and dense_status["fits"] == 0)})
        comparisons[dense] = {"caps": caps,
                              "insensitive_to_step_cap": all(cap["separation"] for cap in caps)}
    return comparisons


def audit_manifest_decisions(manifest: dict[str, Any], selection: dict[str, Any], comparisons: dict[str, Any]) -> dict[str, Any]:
    failures = []
    expected_gates = {gate["m"]: gate for gate in selection["gates"]}
    recorded_gates = manifest.get("ladder", [])
    if len({gate["m"] for gate in recorded_gates}) != len(recorded_gates):
        failures.append("Manifest repeats a ladder gate")
    for gate in recorded_gates:
        expected = expected_gates.get(gate["m"])
        if expected is None or gate.get("dense55_fits") != expected["width55"]["fits"] or gate.get("closure_fits") != expected["closure1024"]["fits"] or bool(gate.get("candidate")) != expected["candidate"]:
            failures.append(f"Manifest ladder gate differs from checked arrays at m={gate['m']}")
    if bool(manifest.get("candidate_found")) != (selection["candidate_m"] is not None):
        failures.append("Manifest candidate-found flag differs from checked arrays")
    for model, comparison in comparisons.items():
        field = f"{model}_separation_both_caps"
        if field in manifest and bool(manifest[field]) != comparison["insensitive_to_step_cap"]:
            failures.append(f"Manifest {model} step-sensitivity decision differs from checked arrays")
    if manifest.get("status") == "complete" and set(expected_gates) != {gate["m"] for gate in recorded_gates}:
        failures.append("Complete manifest omits a computed ladder gate")
    return {"valid": not failures, "failures": failures}


def save_figure(fig: Any, base: Path) -> None:
    fig.savefig(base.with_suffix(".png"), dpi=180)
    fig.savefig(base.with_suffix(".pdf"))


def plot_ladder(plt: Any, rows: list[dict[str, Any]], output: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    colors = plt.get_cmap("tab10").colors
    for axis, model in zip(axes, ("width55", "closure1024")):
        for index, seed in enumerate(SEEDS):
            members = sorted([row for row in rows if row["model"] == model and row["seed"] == seed
                              and row["initialization"] == "high" and row["eta_max"] == 1.0
                              and not row["reproduction"] and row.get("best_mse") is not None], key=lambda row: row["m"])
            axis.plot([LADDER.index(row["m"]) for row in members], [max(row["best_mse"], 1e-18) for row in members],
                      color=colors[index], marker="o", label=f"Seed {seed}", lw=1.2)
            for row in members:
                if not row.get("decision_valid"):
                    axis.scatter(LADDER.index(row["m"]), max(row["best_mse"], 1e-18), marker="x", color="red", s=90, zorder=4)
        axis.axhline(FIT_MSE, color="black", ls="--", lw=1)
        axis.set_xticks(range(len(LADDER)), labels=[str(m) for m in LADDER])
        axis.set_xlabel("Number of alternating samples m")
        axis.set_title(MODEL_LABELS[model], fontsize=10)
        axis.set_yscale("log")
        axis.grid(alpha=.2)
        axis.legend(fontsize=8)
    axes[0].set_ylabel("Best replayed training MSE")
    fig.suptitle("Primary high-gain GD ladder, maximum step 1; dashed line = 0.001", fontsize=11)
    fig.tight_layout()
    save_figure(fig, output / "gd_sample_ladder")
    plt.close(fig)


def plot_learning(plt: Any, payloads: list[dict[str, Any]], m: int, output: Path) -> None:
    colors = plt.get_cmap("tab10").colors
    regimes = (("high", 1.0, "High gain, maximum step 1"),
               ("high", 0.5, "High gain, maximum step 0.5"),
               ("canonical", 1.0, "Canonical gain 1, maximum step 1"))
    for xfield, xlabel in (("physical_clock", "Physical clock (sum of accepted step sizes)"),
                           ("accepted_steps", "Accepted GD updates")):
        fig, axes = plt.subplots(3, 3, figsize=(14, 10), squeeze=False, sharey=True)
        for i, model in enumerate(MODEL_ORDER):
            for j, (gain, eta, label) in enumerate(regimes):
                axis = axes[i, j]
                attempts = [p for p in payloads if p["row"]["m"] == m and p["row"]["model"] == model
                            and p["row"]["initialization"] == gain and p["row"]["eta_max"] == eta]
                for payload in attempts:
                    row = payload["row"]
                    trace = [entry for entry in payload.get("normalized_trace", [])
                             if entry.get("mse") is not None and np.isfinite(entry["mse"])]
                    if not trace:
                        continue
                    seed_index = SEEDS.index(row["seed"])
                    axis.plot([entry[xfield] for entry in trace], [max(entry["mse"], 1e-18) for entry in trace],
                              color=colors[seed_index], ls="--" if row["reproduction"] else "-", lw=1.2,
                              marker="o" if len(trace) == 1 else None, markersize=4, clip_on=False,
                              label=f"{row['seed']}" + (" repeat" if row["reproduction"] else ""))
                if not attempts:
                    axis.text(.5, .5, "Not completed", ha="center", va="center", transform=axis.transAxes)
                axis.axhline(FIT_MSE, color="black", ls=":", lw=.8)
                axis.set_yscale("log")
                axis.set_xlim(left=0)
                axis.grid(alpha=.2)
                axis.set_title(MODEL_LABELS[model] + "\n" + label, fontsize=9)
                axis.set_xlabel(xlabel, fontsize=8)
                if j == 0:
                    axis.set_ylabel("Training MSE")
                if attempts:
                    axis.legend(fontsize=6, loc="best")
        fig.suptitle(f"Full-batch GD at selected m={m}; every accepted state, dashed reproductions", fontsize=11)
        fig.tight_layout(rect=(0, 0, 1, .965))
        save_figure(fig, output / f"gd_selected_m{m}_{xfield}")
        plt.close(fig)


def attach_checker(path: Path, rows: list[dict[str, Any]], run_root: Path) -> dict[str, Any]:
    checker = json.loads(path.read_text())
    failures = []
    if checker.get("run_record_sha256") != file_sha256(run_root / "run_record.json"):
        failures.append("Independent check refers to a different launch manifest")
    attempts = {str(Path(attempt["output"]).resolve()): attempt for attempt in checker.get("attempts", [])}
    for row in rows:
        checked = attempts.get(str((run_root / row["attempt"]).resolve()))
        bound = bool(checked and checked.get("record_sha256") == row.get("record_sha256"))
        row["independent_check_present"] = checked is not None
        row["independent_check_hash_bound"] = bound
        row["independent_check_passed"] = bool(bound and checked.get("passed"))
        if checked is not None:
            row["independent_check_failures"] = checked.get("failures", [])
        row["decision_valid"] = bool(row["decision_valid"] and row["independent_check_passed"])
        row["accepted_fit"] = bool(row["decision_valid"] and row.get("best_fit"))
        if not bound:
            failures.append(f"Missing or hash-unbound independent check: {row['attempt']}")
    return {"path": str(path.resolve()), "sha256": file_sha256(path),
            "passed": bool(checker.get("passed") and not failures), "binding_failures": failures,
            "checker_sha256": checker.get("checker_sha256"), "elapsed_seconds": checker.get("elapsed_seconds"),
            "campaign_checks": checker.get("campaign_checks"), "raw_overall_passed": checker.get("passed")}


def fmt(value: Any, digits: int = 5) -> str:
    if value is None:
        return "—"
    if isinstance(value, bool):
        return "yes" if value else "no"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, (float, np.floating)):
        return f"{value:.{digits}g}"
    return str(value).replace("|", "\\|")


def markdown_table(headers: list[str], records: list[list[Any]]) -> str:
    return "\n".join(["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
                     + ["| " + " | ".join(fmt(value) for value in row) + " |" for row in records])


def range_text(rows: list[dict[str, Any]], field: str) -> str:
    values = [float(row[field]) for row in rows if row.get(field) is not None]
    return f"{fmt(min(values))}–{fmt(max(values))}" if values else "—"


def conclusion(summary: dict[str, Any]) -> str:
    selection = summary["selection"]
    if not summary["scientific_comparison_valid"]:
        return "Inconclusive for the complete registered comparison: at least one numerical, selection, budget, completion or reproduction gate is unresolved. The tables retain all observed finite-budget endpoints."
    m = selection["selected_m"]
    width55 = summary["comparisons"].get("width55", {})
    if width55.get("insensitive_to_step_cap"):
        wider = summary["comparisons"].get("width105", {}).get("insensitive_to_step_cap")
        return (f"Yes, with the registered high-gain initialization and within this finite GD protocol: at m={m}, the closure fitted at least two of three seeds while dense width 55 fitted none, at both maximum steps 1 and 0.5. "
                + ("The same registered separation also held against dense width 105." if wider else "The total-retained-size comparison with dense width 105 must be assessed separately below."))
    if selection.get("candidate_m") is not None:
        caps = width55.get("caps", [])
        counts = (f"Closure fits were {caps[0]['closure']['fits']}/3 at maximum step 1 and {caps[1]['closure']['fits']}/3 at maximum step 0.5; "
                  f"dense width 55 fitted {caps[0]['dense']['fits']}/3 and {caps[1]['dense']['fits']}/3, respectively. ") if len(caps) == 2 else ""
        return (f"The high-gain GD ladder produced a candidate at m={m}, but the registered separation did not survive both step caps. "
                + counts + "This does not establish a step-cap-insensitive fitting advantage within the frozen wall-time and step budgets.")
    return "No registered fitting advantage was demonstrated by this GD-only test: no ladder case met the closure ≥2/3 fits and dense-width-55 0/3 criterion. This is a finite-budget result, not a representation or capacity lower bound."


def write_report(path: Path, summary: dict[str, Any], output: Path) -> None:
    if path.exists():
        raise ValueError(f"Refusing to overwrite existing report: {path}")
    rows, selected = summary["attempts"], summary["selection"]["selected_m"]
    lines = ["# GD-only alternating-circle fitting results", "", conclusion(summary), "",
        "This report concerns full-batch simultaneous gradient descent with canonical mobilities (n,1,n) and scalar Armijo backtracking. It uses no Adam, momentum, clipping, least-squares readout solve, optimizer warm start or quasi-Newton stage. A fit requires unhalved training MSE ≤0.001 and zero nonpositive signed margins. The high-gain initialization multiplies W by m/2; the canonical control uses gain 1.", "",
        "## Checked fit counts", "",
        markdown_table(["m", "Initialization", "Maximum step", "Model", "Fits / 3", "Valid / 3", "Best-MSE range"],
            [[group["m"], group["initialization"], group["eta_max"], group["model"], f"{group['fits']}/3",
              f"{group['valid_attempts']}/3", f"{fmt(group['minimum_mse'])}–{fmt(group['maximum_mse'])}"] for group in summary["groups"]]), "",
        f"The independently computed selected case is {fmt(selected)}; the recorded case is {fmt(summary['selection']['recorded_selected_m'])}. Selection agrees: {fmt(summary['selection']['agrees_with_manifest'])}. The first-candidate stopping rule is valid: {fmt(summary['selection']['selection_sequence_valid'])}.", "",
        "## Step-cap and initialization controls", ""]
    for model, result in summary["comparisons"].items():
        lines.append(f"For {model}, separation at maximum step 1: {fmt(result['caps'][0]['separation'])}; at maximum step 0.5: {fmt(result['caps'][1]['separation'])}; registered separation at both caps: {fmt(result['insensitive_to_step_cap'])}.")
        lines.append("")
    canonical_groups = [group for group in summary["groups"] if group["m"] == selected and group["initialization"] == "canonical"]
    if canonical_groups:
        lines.extend(["With canonical gain 1, the separate checked fit counts were "
                      + "; ".join(f"{group['model']}: {group['fits']}/3" for group in canonical_groups) + ".", ""])
    near_misses = [row for row in rows if not row["reproduction"] and row["m"] == selected
                  and row["model"] == "closure1024" and row["initialization"] == "high" and row["eta_max"] == .5
                  and not row.get("best_fit") and row.get("best_sign_errors") == 0 and row.get("terminal_reason") == "time_limit"]
    if near_misses:
        lines.extend(["At maximum step 0.5, the following closure attempts reached the wall-time limit with zero sign errors but remained above the strict MSE fit threshold: "
                      + "; ".join(f"seed {row['seed']}, MSE {row['best_mse']:.9g}, {row['accepted_steps']} accepted steps, physical clock {row['physical_clock']:.9g}"
                                  for row in near_misses) + ". They count as nonfits under the frozen protocol; no continuation was run.", ""])
    lines.extend(["Halving a maximum scalar step is a learning-rate sensitivity check. It does not prove convergence to continuous gradient flow. Realized steps and physical clocks below must be considered because the same wall-time/step/evaluation caps can terminate architectures at different points. Canonical initialization results are separate controls, not additional high-gain seeds.", "",
        "## Optimization endpoints at the selected case", "",
        markdown_table(["Model", "Gain", "η max", "Accepted steps", "Physical clock", "Attempt seconds", "Realized η range", "Final Q range", "Stops"],
            [[model, gain, eta, range_text(members, "accepted_steps"), range_text(members, "physical_clock"),
              range_text(members, "attempt_elapsed_seconds"),
              f"{fmt(min((r['eta_min'] for r in members if r.get('eta_min') is not None), default=None))}–{fmt(max((r['eta_max_realized'] for r in members if r.get('eta_max_realized') is not None), default=None))}",
              range_text(members, "final_physical_gradient_squared"),
              ", ".join(f"{stop}: {sum(r['terminal_reason'] == stop for r in members)}" for stop in sorted({str(r['terminal_reason']) for r in members}))]
             for gain, eta in (("high", 1.0), ("high", 0.5), ("canonical", 1.0))
             for model in MODEL_ORDER
             if (members := members_for(rows, model, selected, gain, eta))]), "",
        "## Every original attempt", "",
        "MSE, RMSE and sign errors are recomputed from the best saved canonical arrays. Q is the physical squared gradient norm at the final accepted state. Exact values, initial/final diagnostics, wall times, realized step ranges and all replay discrepancies appear in attempts.csv.", "",
        markdown_table(["m", "Model", "Gain", "η max", "Seed", "Initial MSE", "Best MSE", "RMSE", "Sign errors", "Steps", "Clock", "Final Q", "Stop", "Valid"],
            [[row["m"], row["model"], row["initialization"], row["eta_max"], row["seed"], row.get("initial_mse"),
              row.get("best_mse"), row.get("best_rmse"), row.get("best_sign_errors"), row.get("accepted_steps"),
              row.get("physical_clock"), row.get("final_physical_gradient_squared"), row.get("terminal_reason"), row.get("decision_valid")]
             for row in rows if not row["reproduction"]]), "",
        "## Reproductions", "",
        "Reproductions use the first successful seed in increasing order, or seed 20260921 when no seed fitted, with the same device and settings. They are not additional seeds. The registered stability gate compares fit status and final endpoint MSE (absolute difference ≤1e−6). Unequal accepted-step counts involving a wall stop are separately labelled time-censored; their common accepted-step prefix is compared without extra training. Prefix equality does not replace the endpoint gate.", "",
        markdown_table(["Model", "η max", "Expected seed", "Actual seed", "Final-MSE difference", "Same fit", "Stable", "Time-censored", "Identical shared trace"],
            [[check["model"], check["eta_max"], check.get("expected_seed"), check.get("actual_seed"), check.get("final_mse_difference"),
              check.get("same_fit"), check["stable"], check.get("time_censored"), check.get("shared_prefix", {}).get("identical_logged_mse_clock_eta_Q")]
             for check in summary["reproductions"]["checks"]]), "",
        markdown_table(["Model", "η max", "Seed", "Best MSE", "RMSE", "Sign errors", "Steps", "Clock", "Final Q", "Stop", "Valid"],
            [[row["model"], row["eta_max"], row["seed"], row.get("best_mse"), row.get("best_rmse"), row.get("best_sign_errors"),
              row.get("accepted_steps"), row.get("physical_clock"), row.get("final_physical_gradient_squared"),
              row.get("terminal_reason"), row.get("decision_valid")] for row in rows if row["reproduction"]]), "",
        "## Numerical and budget audit", "",
        f"All independent NumPy train/circle/endpoint-gradient replays passed: {fmt(summary['all_raw_replays_valid'])}. All accepted-step Armijo/clock/evaluation traces passed: {fmt(summary['all_traces_valid'])}. The separate construction, source, gradient and update-pair checker passed: {fmt(summary['independent_checker']['passed'])}. All attempt decision gates passed: {fmt(summary['all_decisions_valid'])}.", "",
        f"The manifest contains {summary['attempt_count']} attempts ({summary['original_attempt_count']} originals and {summary['reproduction_count']} reproductions). Total worker-process wall time is {summary['manifest_audit']['computed_worker_seconds']:.3f}s / 2500s; budget arithmetic passed: {fmt(summary['manifest_audit']['budget_valid'])}. Campaign status: {summary['manifest_audit']['status']}.", "",
        "Each attempt was capped at 30,000 accepted steps, 90,000 training forward evaluations, physical clock 10,000, and 75 seconds including initialization and export, with five seconds reserved for export. Wall/step/clock caps are endpoint descriptions, not proofs of a converged minimum. Gradient-floor endpoints are precision-limited; tanh backward uses 1−h² and rounded saturation can make it zero. Saturation fractions and all endpoint gradients are retained in attempts.csv. A failed line search or unexplained numerical discrepancy blocks the affected comparison.", "",
        "The dataset, odd antipodal parity, all seeds, gains and stages are frozen. Width 55 matches trainable scalar count approximately (3,190 versus 3,087); width 105 matches total retained predictor scalars approximately (11,340 versus 11,279). The closure count includes 8,192 frozen dictionary scalars and excludes the discarded source A. These are parameter-count controls, not equal-width, equal-compute or generalization comparisons.", "",
        "## Artifacts", "",
        f"- [All raw-array diagnostics]({output / 'attempts.csv'})", f"- [Machine-readable audit]({output / 'analysis.json'})",
        f"- [Sample ladder figure]({output / 'gd_sample_ladder.png'})",
        f"- [Separate independent checker]({summary['independent_checker']['path']})", ""])
    if selected is not None:
        lines.extend([f"- [Learning curves versus physical clock]({output / f'gd_selected_m{selected}_physical_clock.png'})",
                      f"- [Learning curves versus accepted updates]({output / f'gd_selected_m{selected}_accepted_steps.png'})", ""])
    if summary.get("failures"):
        lines.extend(["## Unresolved audit conditions", ""] + [f"- {failure}" for failure in summary["failures"]] + [""])
    lines.extend(["The strongest defensible claim is empirical performance under these finite attempts. Failure to fit cannot establish that either architecture lacks a fitting representation. The controls do not establish asymptotic convergence, a continuous-flow limit, generalization, or a universal sample-efficiency advantage.", ""])
    path.write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="Fresh analysis directory")
    parser.add_argument("--checker-json", type=Path, required=True, help="Completed independent replay check bound to this manifest")
    parser.add_argument("--report", type=Path, help="Fresh GD_RESULTS.md path; never overwritten")
    args = parser.parse_args()
    run_root, output = args.run_root.resolve(), args.out.resolve()
    if output.exists():
        raise SystemExit(f"Refusing existing analysis output directory: {output}")
    if args.report and args.report.exists():
        raise SystemExit(f"Refusing existing report: {args.report}")
    if not args.checker_json.is_file():
        raise SystemExit("Independent final checker JSON must exist before final analysis")
    rows, payloads, read_errors = [], [], []
    for record_path in sorted(run_root.rglob("record.json")):
        try:
            row, payload = scan_attempt(record_path.parent, run_root)
            rows.append(row)
            payloads.append(payload)
        except Exception as exc:
            read_errors.append(f"{record_path.parent.name}: {type(exc).__name__}: {exc}")
    manifest_audit = attach_manifest(run_root, rows)
    manifest = manifest_audit.pop("manifest")
    manifest_audit.update({key: manifest.get(key) for key in ("status", "source_hashes", "spent_worker_seconds", "selected_m", "candidate_found")})
    checker = attach_checker(args.checker_json, rows, run_root)
    rows.sort(key=lambda row: (row["reproduction"], row["m"], row["initialization"] == "canonical", -row["eta_max"],
                               MODEL_ORDER.index(row["model"]), row["seed"]))
    selection = audit_selection(rows, manifest.get("selected_m"))
    selected = selection["selected_m"]
    reproductions = audit_reproductions(rows, payloads, run_root, selected)
    comparisons = audit_comparisons(rows, selected)
    manifest_decisions = audit_manifest_decisions(manifest, selection, comparisons)
    groups = group_rows(rows)
    controls_complete = bool(selected is not None and all(group_status(members_for(rows, model, selected, gain, eta))["all_valid"]
        for model in MODEL_ORDER for gain, eta in (("high", 1.0), ("high", 0.5), ("canonical", 1.0))))
    summary = {
        "analysis_source_sha256": file_sha256(Path(__file__)), "run_root": str(run_root),
        "fit_mse_threshold": FIT_MSE, "prediction_tolerance": PRED_TOL, "mse_tolerance": MSE_TOL,
        "attempt_count": len(rows), "original_attempt_count": sum(not row["reproduction"] for row in rows),
        "reproduction_count": sum(row["reproduction"] for row in rows),
        "all_raw_replays_valid": bool(rows and all(row["raw_replay_valid"] for row in rows)),
        "all_traces_valid": bool(rows and all(row["trace_valid"] for row in rows)),
        "all_decisions_valid": bool(rows and all(row["decision_valid"] for row in rows)),
        "controls_complete_and_valid": controls_complete,
        "selection": selection, "comparisons": comparisons, "reproductions": reproductions,
        "manifest_decisions": manifest_decisions,
        "groups": groups, "attempts": rows, "manifest_audit": manifest_audit, "independent_checker": checker,
        "scope": "Independent NumPy prediction and endpoint-gradient replay; trace, stopping, all-launch, budget, gate and reproduction reporting. No training module imported.",
        "failures": read_errors + manifest_audit["budget_failures"] + checker["binding_failures"] + manifest_decisions["failures"],
    }
    summary["scientific_comparison_valid"] = bool(summary["all_decisions_valid"] and controls_complete
        and selection["agrees_with_manifest"] and selection["selection_sequence_valid"]
        and manifest_audit["budget_valid"] and manifest_decisions["valid"] and checker["passed"] and reproductions["all_stable"]
        and manifest_audit["status"] == "complete")
    if not selection["agrees_with_manifest"]:
        summary["failures"].append("Computed selected case disagrees with the launch manifest")
    if not controls_complete:
        summary["failures"].append("The complete valid three-seed high-gain/step-cap/canonical control suite is unavailable")
    if not reproductions["all_stable"]:
        summary["failures"].append("At least one required reproduction is missing or fails the registered endpoint-stability gate")
    if not checker["passed"]:
        summary["failures"].append("Independent checker did not pass the complete campaign")
    for row in rows:
        if not row["decision_valid"]:
            false_flags = [key for key in ("raw_replay_valid", "trace_valid", "fit_flag_agrees", "optimizer_metadata_valid",
                                          "environment_valid", "output_hashes_valid", "launch_settings_valid", "independent_check_passed") if not row.get(key)]
            summary["failures"].append(f"{row['attempt']}: invalid decision ({', '.join(false_flags)}); stop={row['terminal_reason']}")
            summary["failures"].extend(f"{row['attempt']}: {error}" for error in row.get("errors", []))
            summary["failures"].extend(f"{row['attempt']}: {error}" for error in row.get("trace_audit", {}).get("failures", [])[:5])
            summary["failures"].extend(f"{row['attempt']}: independent check: {error}" for error in row.get("independent_check_failures", []))
    summary["conclusion"] = conclusion(summary)
    output.mkdir(parents=True)
    os.environ["MPLCONFIGDIR"] = str(output / "matplotlib-cache")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    write_csv(output / "attempts.csv", rows)
    write_csv(output / "groups.csv", groups)
    plot_ladder(plt, rows, output)
    if selected is not None:
        plot_learning(plt, payloads, selected, output)
    write_json(output / "analysis.json", summary)
    if args.report:
        write_report(args.report.resolve(), summary, output)
    print(json.dumps({key: summary[key] for key in ("attempt_count", "all_raw_replays_valid", "all_traces_valid",
                                                   "all_decisions_valid", "scientific_comparison_valid", "conclusion")}, indent=2))


if __name__ == "__main__":
    main()
