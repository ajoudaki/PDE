#!/usr/bin/env python3
"""Independent raw-array summaries and figures for the frozen fitting study.

No training module is imported. All fits are judged on the actual labelled
samples. Circle-grid predictions, when present in producer output, are not
treated as ground truth or used in these figures.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
from typing import Any

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

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
    "width105": "Dense width 105 (11,340 total)",
}


def load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as data:
        return {key: np.array(data[key], copy=True) for key in data.files}


def metrics(prediction: np.ndarray, y: np.ndarray) -> dict[str, Any]:
    finite = bool(np.all(np.isfinite(prediction)))
    difference = prediction - y
    return {
        "mse": float(np.mean(difference * difference)) if finite else None,
        "sign_errors": int(np.count_nonzero(~(y * prediction > 0))),
        "max_abs_error": float(np.max(np.abs(difference))) if finite else None,
        "minimum_signed_margin": float(np.min(y * prediction)) if finite else None,
        "finite": finite,
    }


def forward(model: str, state: dict[str, np.ndarray], initial: dict[str, np.ndarray], u: np.ndarray) -> np.ndarray:
    """Reconstruct the stated network directly from saved canonical arrays."""
    W = np.asarray(state["W"], dtype=np.float64)
    c = np.asarray(state["c"], dtype=np.float64).reshape(-1)
    n = W.shape[0]
    if W.shape != (n, 2) or c.shape != (n,):
        raise ValueError("Invalid W/c dimensions")
    first = np.tanh(W @ u.T)
    if model == "network":
        second = np.tanh(np.asarray(state["A"], dtype=np.float64) @ first)
    elif model == "closure":
        B1 = np.asarray(initial["B1"], dtype=np.float64)
        B2 = np.asarray(initial["B2"], dtype=np.float64)
        M = np.asarray(state["M"], dtype=np.float64)
        second = np.tanh(B2 @ M @ ((B1.T @ first) / n))
    else:
        raise ValueError(f"Unknown model {model!r}")
    return (c / n) @ second


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gain_label(value: str) -> str:
    return "canonical" if value in ("primary", "canonical") else value


def get_float(value: Any) -> float | None:
    return float(value) if value is not None and np.isfinite(float(value)) else None


def scan_attempt(path: Path, run_root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    record = json.loads((path / "record.json").read_text())
    config = record["config"]
    m, width, seed = int(config["m"]), int(config["width"]), int(config["seed"])
    model = str(config["model"])
    key = f"width{width}" if model == "network" else f"closure{width}"
    relative = str(path.relative_to(run_root))
    reproduction = any(token in relative.lower() for token in ("repro", "repeat"))
    row: dict[str, Any] = {
        "attempt": relative,
        "model": key,
        "m": m,
        "seed": seed,
        "initialization": gain_label(str(config["gain"])),
        "first_weight_gain": record.get("first_weight_gain", 1 if config["gain"] == "primary" else m / 2),
        "reproduction": reproduction,
        "terminal_reason": record.get("status", "unknown"),
        "producer_fit": record.get("fit"),
        "producer_numerical_valid": record.get("numerical_valid"),
        "producer_oracle_pass": record.get("oracle_pass"),
        "budget_respected": record.get("budget_respected"),
        "attempt_elapsed_seconds": record.get("elapsed_seconds_before_final_record_write"),
        "adam_steps_completed": record.get("adam_steps_completed"),
        "lbfgs_evaluations": record.get("lbfgs_evaluations"),
        "stopping_phase": record.get("stopping_phase"),
        "trainable_scalars": width * width + 3 * width if model == "network" else 3 * width + 15,
        "retained_predictor_scalars": width * width + 3 * width if model == "network" else 11 * width + 15,
        "record_sha256": file_sha256(path / "record.json"),
    }
    payload: dict[str, Any] = {"path": path, "record": record, "row": row, "trace": []}
    try:
        dataset = load_npz(path / "dataset.npz")
        y = np.asarray(dataset["y"], dtype=np.float64).reshape(-1)
        u = np.asarray(dataset["u"], dtype=np.float64)
        if u.shape == (2, m):
            u = u.T
        theta = np.asarray(dataset["theta"], dtype=np.float64).reshape(-1)
        expected_theta = 2 * np.pi * np.arange(m) / m
        expected_u = np.column_stack((np.cos(expected_theta), np.sin(expected_theta))) / np.sqrt(2)
        data_valid = bool(
            y.shape == (m,) and u.shape == (m, 2) and theta.shape == (m,)
            and np.array_equal(y, (-1.0) ** np.arange(m))
            and np.max(np.abs(theta - expected_theta)) <= 1e-14
            and np.max(np.abs(u - expected_u)) <= 1e-14
        )
        row["dataset_valid"] = data_valid
        initial = load_npz(path / "initial.npz")
        saved_predictions = load_npz(path / "predictions.npz")
        payload.update({"theta": theta, "y": y, "predictions": {}})
        states_valid = True
        for name in ("initial", "best", "final"):
            state = initial if name == "initial" else load_npz(path / f"{name}.npz")
            pred = forward(model, state, initial, u)
            values = metrics(pred, y)
            payload["predictions"][name] = pred
            for metric, value in values.items():
                row[f"{name}_{metric}"] = value
            saved = np.asarray(saved_predictions[f"{name}_train"]).reshape(-1)
            discrepancy = float(np.max(np.abs(saved - pred)))
            claimed_mse = record["diagnostics"][name]["mse"]
            mse_discrepancy = abs(values["mse"] - claimed_mse) if values["mse"] is not None and claimed_mse is not None else None
            state_valid = bool(values["finite"] and np.isfinite(discrepancy) and discrepancy <= PRED_TOL and mse_discrepancy is not None and mse_discrepancy <= MSE_TOL)
            row[f"{name}_prediction_discrepancy"] = get_float(discrepancy)
            row[f"{name}_mse_discrepancy"] = get_float(mse_discrepancy)
            row[f"{name}_replay_valid"] = state_valid
            states_valid = states_valid and state_valid
        row["raw_replay_valid"] = bool(data_valid and states_valid)
        row["recomputed_fit"] = bool(row["best_finite"] and row["best_mse"] <= FIT_MSE and row["best_sign_errors"] == 0)
        row["fit_flag_agrees"] = bool(row["recomputed_fit"] == bool(record.get("fit")))
        row["analysis_fit"] = bool(row["recomputed_fit"] and row["raw_replay_valid"] and row["fit_flag_agrees"])
        row["accepted_fit"] = row["analysis_fit"]
        row["decision_valid"] = bool(row["raw_replay_valid"] and row["fit_flag_agrees"])
        row["fit_verification"] = "strict_float64_replay" if row["decision_valid"] else "unresolved"
        row["reported_mse"] = row["best_mse"]
        row["reported_sign_errors"] = row["best_sign_errors"]
        row["reported_max_abs_error"] = row["best_max_abs_error"]
        row["read_error"] = ""
        payload["extra_states"] = []
        for name in ("optimizer_terminal", "pre_polish_best", "polish_candidate"):
            state_path = path / f"{name}.npz"
            if state_path.exists():
                extra = metrics(forward(model, load_npz(state_path), initial, u), y)
                payload["extra_states"].append({"attempt": relative, "state": name, **extra})
    except Exception as exc:
        row.update({"raw_replay_valid": False, "analysis_fit": False, "accepted_fit": False, "decision_valid": False, "fit_verification": "unresolved", "read_error": f"{type(exc).__name__}: {exc}"})
    trace_path = path / "trace.jsonl"
    if trace_path.exists():
        for line_number, line in enumerate(trace_path.read_text().splitlines(), 1):
            try:
                payload["trace"].append(json.loads(line))
            except json.JSONDecodeError:
                row["trace_error"] = f"Invalid JSON on line {line_number}"
                break
    finite_trace = [entry for entry in payload["trace"] if entry.get("mse") is not None and np.isfinite(entry["mse"])]
    row["trace_evaluations"] = len(payload["trace"])
    row["trace_last_seconds"] = max((entry.get("elapsed_seconds", 0.0) for entry in payload["trace"]), default=0.0)
    row["trace_lowest_mse"] = min((entry["mse"] for entry in finite_trace), default=None)
    row["best_gradient_norm_reported"] = record.get("diagnostics", {}).get("best", {}).get("gradient", {})
    row["readout_polish"] = record.get("readout_polish", record.get("polish", {}))
    return row, payload


def attach_launch_manifest(run_root: Path, rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Retain every launch, including supervisor failures without a checkpoint."""
    manifest_path = run_root / "run_record.json"
    if not manifest_path.exists():
        return None
    manifest = json.loads(manifest_path.read_text())
    by_attempt = {row["attempt"]: row for row in rows}
    for job in manifest.get("jobs", []):
        launch_path = Path(job["output"])
        if not launch_path.is_absolute():
            # Runner paths are ordinarily absolute; explicit cwd resolves any
            # relative paths without silently treating them as dataset names.
            launch_path = Path(job.get("cwd", run_root)) / launch_path
        relative = str(launch_path.resolve().relative_to(run_root))
        row = by_attempt.get(relative)
        if row is None:
            width = int(job["width"])
            model = f"width{width}" if job["model"] == "network" else f"closure{width}"
            gain = "rescue" if "rescue" in job.get("stage", "") or job.get("input_gain", 1) != 1 else "canonical"
            row = {
                "attempt": relative, "model": model, "m": int(job["samples"]),
                "seed": int(job["seed"]), "initialization": gain,
                "first_weight_gain": job.get("input_gain"),
                "reproduction": job.get("stage") == "reproduction",
                "terminal_reason": "missing_attempt_record",
                "raw_replay_valid": False, "analysis_fit": False,
                "accepted_fit": False, "decision_valid": False, "fit_verification": "unresolved",
                "read_error": "Launch recorded without a readable final attempt record",
            }
            rows.append(row)
            by_attempt[relative] = row
        row.update({
            "stage": job.get("stage"),
            "reproduction": job.get("stage") == "reproduction",
            "process_returncode": job.get("returncode"),
            "process_wall_seconds": job.get("process_wall_seconds"),
            "supervisor_failure": job.get("supervisor_failure"),
        })
    return {
        "path": str(manifest_path), "sha256": file_sha256(manifest_path),
        **{key: manifest.get(key) for key in ("status", "worker_wall_cap", "spent_worker_seconds", "selected_samples", "gates", "reproductions", "source_hashes")},
        "launch_count": len(manifest.get("jobs", [])),
    }


def attach_adjudications(path: Path | None, run_root: Path, rows: list[dict[str, Any]], payloads: list[dict[str, Any]] | None = None) -> dict[str, Any] | None:
    """Apply explicit checked high-precision decisions without erasing failures."""
    if path is None:
        return None
    adjudications = json.loads(path.read_text())
    applied = []
    for row in rows:
        key = str((run_root / row["attempt"]).resolve())
        check = adjudications.get(key)
        if check is None:
            continue
        row["independent_adjudication"] = check
        if check.get("record_sha256") != row.get("record_sha256"):
            raise ValueError(f"Adjudication record hash mismatch for {row['attempt']}")
        valid = bool(check.get("resolved") and check.get("stable_to_higher_precision"))
        if not valid:
            continue
        mse, signs = float(check["mse"]), int(check["sign_errors"])
        fit = bool(mse <= FIT_MSE and signs == 0)
        if fit != bool(check["fit"]) or fit != bool(check["checked_fit"]):
            raise ValueError(f"Adjudication fit flag disagrees with its metrics for {row['attempt']}")
        evidence_path = Path(check["evidencepath"])
        evidence = json.loads(evidence_path.read_text())
        attempt_path = run_root / row["attempt"]
        if evidence.get("best_sha256") != file_sha256(attempt_path / "best.npz") or evidence.get("dataset_sha256") != file_sha256(attempt_path / "dataset.npz"):
            raise ValueError(f"High-precision checkpoint/data hash mismatch for {row['attempt']}")
        row.update({
            "accepted_fit": fit, "decision_valid": True,
            "fit_verification": "independent_high_precision",
            "reported_mse": mse, "reported_sign_errors": signs,
            "reported_max_abs_error": float(check["max_abs_error"]),
        })
        if payloads is not None:
            payload = next((item for item in payloads if item["row"] is row), None)
            if payload is not None:
                payload["plot_best"] = np.asarray([float(value) for value in evidence["high_precision"]["predictions_decimal"]])
        applied.append(row["attempt"])
    return {"path": str(path.resolve()), "sha256": file_sha256(path), "applied_attempts": applied}


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: json.dumps(value, sort_keys=True) if isinstance(value, (dict, list)) else value for key, value in row.items()})


def group_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups = []
    for model in MODEL_ORDER:
        for m in LADDER:
            for gain in ("canonical", "rescue"):
                members = [r for r in rows if r["model"] == model and r["m"] == m and r["initialization"] == gain and not r["reproduction"]]
                if members:
                    finite = [r["reported_mse"] for r in members if r.get("reported_mse") is not None]
                    groups.append({"model": model, "m": m, "initialization": gain, "attempts": len(members), "fits": sum(bool(r["accepted_fit"]) for r in members), "decision_valid": sum(bool(r["decision_valid"]) for r in members), "raw_replays_valid": sum(bool(r["raw_replay_valid"]) for r in members), "minimum_mse": min(finite) if finite else None, "maximum_mse": max(finite) if finite else None, "seeds": ",".join(str(r["seed"]) for r in members)})
    return groups


def gate_selection(rows: list[dict[str, Any]]) -> tuple[int | None, list[dict[str, Any]]]:
    audit = []
    selected = None
    for m in LADDER:
        members = [r for r in rows if r["model"] == "width55" and r["m"] == m and not r["reproduction"]]
        canonical = [r for r in members if r["initialization"] == "canonical"]
        rescue = [r for r in members if r["initialization"] == "rescue"]
        complete = len(canonical) == 3 and {r["seed"] for r in canonical} == set(SEEDS)
        failed_all = bool(complete and len(rescue) == 3 and {r["seed"] for r in rescue} == set(SEEDS) and all(r["decision_valid"] for r in members) and not any(r["accepted_fit"] for r in members))
        audit.append({"m": m, "canonical_attempts": len(canonical), "rescue_attempts": len(rescue), "fits": sum(bool(r["accepted_fit"]) for r in members), "complete_failure_suite": failed_all})
        if m > 55 and failed_all and selected is None:
            selected = m
    return selected, audit


def plot_all_attempts(plt: Any, rows: list[dict[str, Any]], output: Path) -> None:
    available = [key for key in MODEL_ORDER if any(row["model"] == key for row in rows)]
    fig, axes = plt.subplots(1, len(available), figsize=(5 * len(available), 4.5), squeeze=False, sharey=True)
    colors = plt.get_cmap("tab10").colors
    for axis, model in zip(axes[0], available):
        for row in rows:
            if row["model"] != model or row.get("reported_mse") is None:
                continue
            seed_index = SEEDS.index(row["seed"]) if row["seed"] in SEEDS else 0
            gain = row["initialization"]
            offset = (seed_index - 1) * 0.08 + (0.19 if gain == "rescue" else -0.19)
            x = LADDER.index(row["m"]) + offset
            marker = "D" if row["reproduction"] else ("o" if gain == "canonical" else "^")
            axis.scatter(x, max(row["reported_mse"], 1e-18), color=colors[seed_index], marker=marker, s=62, facecolors="none" if row["reproduction"] else colors[seed_index], linewidths=1.2, zorder=3)
            if not row["raw_replay_valid"]:
                axis.scatter(x, max(row["reported_mse"], 1e-18), color="red", marker="x", s=100, zorder=4)
        axis.axhline(FIT_MSE, color="black", ls="--", lw=1, label="Fit MSE threshold")
        axis.set_xticks(range(len(LADDER)), labels=[str(m) for m in LADDER])
        axis.set_xlabel("Number of labelled circle samples m")
        axis.set_title(MODEL_LABELS[model], fontsize=10)
        axis.set_yscale("log")
        axis.grid(axis="y", alpha=.25)
    axes[0, 0].set_ylabel("Best retained training MSE (checked precision)")
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], marker="o", ls="", color=colors[i], label=f"Seed {seed}") for i, seed in enumerate(SEEDS)]
    handles += [Line2D([], [], marker="o", ls="", color="gray", label="Canonical"), Line2D([], [], marker="^", ls="", color="gray", label="High-gain rescue"), Line2D([], [], marker="D", markerfacecolor="none", ls="", color="gray", label="Same-settings reproduction")]
    if any(not row["raw_replay_valid"] for row in rows):
        handles.append(Line2D([], [], marker="x", ls="", color="red", label="Strict float64 replay discrepancy (see audit)"))
    fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=8, frameon=False)
    fig.suptitle("Every attempt shown separately; a fit also requires zero sign errors", fontsize=11)
    fig.tight_layout(rect=(0, .14, 1, .94))
    save_figure(fig, output / "all_attempts_mse")
    plt.close(fig)


def save_figure(fig: Any, base: Path) -> None:
    fig.savefig(base.with_suffix(".png"), dpi=180)
    fig.savefig(base.with_suffix(".pdf"))


def plot_selected(plt: Any, payloads: list[dict[str, Any]], m: int, output: Path, comparison: bool = True) -> None:
    selected = [p for p in payloads if p["row"]["m"] == m]
    available = [key for key in MODEL_ORDER if any(p["row"]["model"] == key for p in selected)]
    colors = plt.get_cmap("tab10").colors
    for kind in ("loss", "predictions"):
        fig, axes = plt.subplots(len(available), 2, figsize=(12, 3.25 * len(available)), squeeze=False)
        for model_index, model in enumerate(available):
            for gain_index, gain in enumerate(("canonical", "rescue")):
                axis = axes[model_index, gain_index]
                attempts = [p for p in selected if p["row"]["model"] == model and p["row"]["initialization"] == gain]
                axis.set_title(f"{MODEL_LABELS[model]} | {gain}", fontsize=9)
                if not attempts:
                    axis.text(.5, .5, "Not run under the frozen gate", ha="center", va="center", transform=axis.transAxes)
                if kind == "predictions" and attempts and "y" in attempts[0]:
                    axis.scatter(attempts[0]["theta"], attempts[0]["y"], c="black", marker="x", s=25, lw=.9, label="Actual training labels", zorder=4)
                for payload in attempts:
                    row = payload["row"]
                    seed_index = SEEDS.index(row["seed"]) if row["seed"] in SEEDS else 0
                    label = str(row["seed"]) + (" reproduction" if row["reproduction"] else "")
                    color = colors[seed_index]
                    if kind == "loss":
                        trace = [entry for entry in payload["trace"] if entry.get("mse") is not None and np.isfinite(entry["mse"])]
                        if not trace:
                            continue
                        x = [entry["elapsed_seconds"] for entry in trace]
                        losses = np.asarray([max(entry["mse"], 1e-18) for entry in trace])
                        axis.plot(x, losses, color=color, lw=.4, alpha=.18)
                        axis.plot(x, np.minimum.accumulate(losses), color=color, lw=1.4, ls="--" if row["reproduction"] else "-", label=label)
                        polish = [entry for entry in trace if entry.get("phase") == "readout_polish"]
                        if polish:
                            axis.scatter([entry["elapsed_seconds"] for entry in polish], [max(entry["mse"], 1e-18) for entry in polish], color=color, marker="*", s=70, zorder=5)
                    elif "predictions" in payload:
                        prediction = payload.get("plot_best", payload["predictions"]["best"])
                        axis.scatter(payload["theta"], prediction, color=color, marker="D" if row["reproduction"] else "o", s=12, alpha=.65, facecolors="none" if row["reproduction"] else color, label=label)
                if kind == "loss":
                    axis.axhline(FIT_MSE, color="black", lw=.8, ls="--")
                    axis.set_yscale("log")
                    axis.set_xlabel("Elapsed attempt seconds")
                    axis.set_ylabel("Training MSE")
                else:
                    axis.set_xlabel("Training-sample angle θ")
                    axis.set_ylabel("Label or best retained prediction")
                    axis.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi], ["0", "π/2", "π", "3π/2", "2π"])
                axis.grid(alpha=.18)
                if attempts:
                    axis.legend(fontsize=7, loc="best")
        caption = "Faint: evaluations; bold: running minimum; dashed: reproduction; star: readout polish." if kind == "loss" else "Only sampled labels and predictions are shown; no between-sample target is assumed."
        prefix = "Selected comparison" if comparison else "Final ladder case (no comparison gate opened)"
        fig.suptitle(f"{prefix} m={m}. {caption}", fontsize=10)
        fig.tight_layout(rect=(0, 0, 1, .96))
        save_figure(fig, output / f"selected_m{m}_{kind}")
        plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="Fresh output directory; existing directories are rejected")
    parser.add_argument("--selected-m", type=int, choices=LADDER, help="Root's selected comparison, cross-checked and reported against the raw gate")
    parser.add_argument("--adjudications", type=Path, help="Independent 60/90-digit replay decisions keyed by absolute attempt path")
    args = parser.parse_args()
    run_root = args.run_root.resolve()
    output = args.out.resolve()
    if output.exists():
        raise SystemExit(f"Refusing existing output directory: {output}")
    record_paths = sorted(run_root.rglob("record.json"))
    if not record_paths:
        raise SystemExit(f"No attempt records found under {run_root}")
    output.mkdir(parents=True)
    os.environ["MPLCONFIGDIR"] = str(output / "matplotlib-cache")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rows, payloads = [], []
    for record_path in record_paths:
        row, payload = scan_attempt(record_path.parent, run_root)
        rows.append(row)
        payloads.append(payload)
    launch_manifest = attach_launch_manifest(run_root, rows)
    adjudication_source = attach_adjudications(args.adjudications, run_root, rows, payloads)
    rows.sort(key=lambda r: (r["reproduction"], MODEL_ORDER.index(r["model"]) if r["model"] in MODEL_ORDER else 99, r["m"], r["initialization"], r["seed"]))
    groups = group_rows(rows)
    selected, gate_audit = gate_selection(rows)
    recorded_selection = args.selected_m
    if recorded_selection is None and launch_manifest is not None:
        recorded_selection = launch_manifest.get("selected_samples")
    gate_agrees = recorded_selection == selected if launch_manifest is not None or args.selected_m is not None else None
    display_m = recorded_selection if recorded_selection is not None else selected if selected is not None else 254
    write_csv(output / "attempts.csv", rows)
    write_csv(output / "groups.csv", groups)
    extra_states = [state for payload in payloads for state in payload.get("extra_states", [])]
    if extra_states:
        write_csv(output / "readout_states.csv", extra_states)
    plot_all_attempts(plt, rows, output)
    plot_selected(plt, payloads, display_m, output, comparison=recorded_selection is not None or selected is not None)
    summary = {
        "analysis_source_sha256": file_sha256(Path(__file__)),
        "run_root": str(run_root),
        "fit_mse_threshold": FIT_MSE,
        "prediction_replay_tolerance": PRED_TOL,
        "mse_replay_tolerance": MSE_TOL,
        "selected_m": selected,
        "recorded_selected_m": recorded_selection,
        "gate_agrees_with_manifest": gate_agrees,
        "display_m": display_m,
        "gate_audit": gate_audit,
        "attempt_count": len(rows),
        "original_attempt_count": sum(not row["reproduction"] for row in rows),
        "reproduction_count": sum(row["reproduction"] for row in rows),
        "all_raw_replays_valid": all(row["raw_replay_valid"] for row in rows),
        "all_decisions_valid": all(row["decision_valid"] for row in rows),
        "groups": groups,
        "attempts": rows,
        "launch_manifest": launch_manifest,
        "adjudication_source": adjudication_source,
        "scope": "Independent NumPy array replay and reporting; not a replacement for the separate checker of construction, derivatives, provenance, and reproduction.",
    }
    (output / "analysis.json").write_text(json.dumps(summary, indent=2, allow_nan=False) + "\n")
    print(json.dumps({key: summary[key] for key in ("selected_m", "attempt_count", "original_attempt_count", "reproduction_count", "all_raw_replays_valid")}, indent=2))


if __name__ == "__main__":
    main()
