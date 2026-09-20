"""GPU analysis of all declared width-2048 cells, including failed trajectories.

Primary aggregates use one common configuration set for all nine models. A case
is included only when its full network and all nine closures fit in both suites,
pass checkpoint/loss replay, and change by at most 0.01 under refinement.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np
import torch

from analyze import evaluate_saved, tensor
from benchmark import save_json, setup
from diverse_cases import CASES_V2


METHODS = ("ours", "gaussian", "orthogonal")
ORDERS = (1, 3, 5)
MODELS = [f"{method}_p{p}" for p in ORDERS for method in METHODS]
THRESHOLD = 1e-3
REFINEMENT_LIMIT = 0.01
REPLAY_TOLERANCE = 1e-10
COLORS = {"ours": "#1261a0", "gaussian": "#ce6c1b", "orthogonal": "#7d4196"}


def finite(value):
    """Keep failed/nonfinite trajectories JSON-serializable without inventing data."""
    if value is None:
        return None
    value = float(value)
    return value if math.isfinite(value) else None


def sha256(path):
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def csv_file(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows({k: json.dumps(v) if isinstance(v, (list, dict)) else v
                         for k, v in row.items()} for row in rows)


def validate_configs(primary, refined):
    """Workers share flat result directories but retain separate producer records."""
    configs = {}
    for suite, folder in (("primary", primary), ("refined", refined)):
        paths = sorted(folder.glob("config*.json"))
        if not paths:
            raise ValueError(f"No producer configurations found in {folder}")
        configs[suite] = [(path, json.loads(path.read_text())) for path in paths]
    baseline = configs["primary"][0][1]
    expected = {"cases": CASES_V2, "width": 2048, "orders": list(ORDERS),
                "network_seed": 20260920, "dictionary_seed": 7319,
                "threshold": THRESHOLD, "dtype": "float64"}
    for suite, entries in configs.items():
        for path, config in entries:
            for key, value in expected.items():
                if json.dumps(config.get(key), sort_keys=True) != json.dumps(value, sort_keys=True):
                    raise ValueError(f"Unexpected {key} in {path}")
            for key in ("cases", "width", "network_seed", "dictionary_seed", "threshold", "orders", "dtype"):
                if config.get(key) != baseline.get(key):
                    raise ValueError(f"Mismatched {key} in {path}")
            sources = {p: h for p, h in config["source_hashes"].items()
                       if p.startswith("code/") or Path(p).name in
                       ("benchmark.py", "diverse_benchmark.py", "diverse_dictionary.py", "diverse_cases.py")}
            baseline_sources = {p: h for p, h in baseline["source_hashes"].items()
                                if p.startswith("code/") or Path(p).name in
                                ("benchmark.py", "diverse_benchmark.py", "diverse_dictionary.py", "diverse_cases.py")}
            if sources != baseline_sources:
                raise ValueError(f"Changed simulation source in {path}")
        # Worker partitioning must not change solver tolerances inside a suite.
        for _, config in entries[1:]:
            for key in ("rtol", "atol", "step", "max_step"):
                if config.get(key) != entries[0][1].get(key):
                    raise ValueError(f"Worker solver settings differ: {suite} {key}")
    pc, rc = configs["primary"][0][1], configs["refined"][0][1]
    for key in ("rtol", "atol"):
        if not 0 < rc[key] < pc[key]:
            raise ValueError(f"Refinement must tighten {key}")
    return {suite: {str(path): {"sha256": sha256(path), "config": config}
                    for path, config in entries} for suite, entries in configs.items()}


@torch.no_grad()
def audit_cell(folder, case, model, suite, device):
    """Replay retained states; keep failures explicit and avoid retaining big states."""
    key = f"{case}_{model}"
    directory = folder / key
    summary_path, arrays_path = directory / "summary.json", directory / "arrays.npz"
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    record = {
        "suite": suite, "case": case, "model": model,
        "status": summary.get("status", "missing_summary"),
        "loss": finite(summary.get("loss")), "time": finite(summary.get("time")),
        "seconds": finite(summary.get("seconds")), "steps": summary.get("steps"),
        "summary_present": summary_path.exists(), "arrays_present": arrays_path.exists(),
        "checkpoint_replay_max": None, "initial_checkpoint_replay_max": None,
        "recomputed_training_loss": None, "loss_replay_error": None,
        "loss_trace_final_error": None, "initial_loss_replay_error": None,
        "training_input_error": None, "labels_error": None,
        "endpoint_grid_error": None, "endpoint_input_error": None,
        "first_crossing_verified": False, "replay_valid": False, "fitted": False,
        "reasons": [], "summary": summary,
    }
    if not summary_path.exists():
        record["reasons"].append("missing summary.json")
    if not arrays_path.exists():
        record["reasons"].append("missing arrays.npz")
        return record, None
    try:
        with np.load(arrays_path, allow_pickle=False) as saved:
            # npz members are not mmap-able. Keep only initial/terminal states so
            # width-2048 checkpoint histories do not accumulate across cells.
            small = {name: saved[name][[0, -1]] for name in ("w", "c", "M")}
            small.update({name: saved[name] for name in
                          ("endpoint_inputs", "training_inputs", "labels")})
            small.update({name: saved[name] for name in ("b1", "b2") if name in saved})
            if small["w"].shape != (2, 2048, 2) or small["c"].shape != (2, 2048):
                raise ValueError("checkpoint has unexpected width/input dimension")
            if small["training_inputs"].shape != (8, 2) or small["labels"].shape != (8,):
                raise ValueError("checkpoint does not contain eight scalar-labeled inputs")
            f = tensor(saved["endpoint_prediction"], device)
            angles = saved["endpoint_angles"]
            endpoint_inputs = saved["endpoint_inputs"]
            if f.shape != (8192,) or angles.shape != (8192,) or endpoint_inputs.shape != (8192, 2):
                raise ValueError("endpoint grid has unexpected shape")
            expected_angles = torch.arange(8192, device=device, dtype=torch.float64) * (2 * math.pi / 8192)
            record["endpoint_grid_error"] = finite((tensor(angles, device) - expected_angles).abs().max())
            expected_grid = torch.stack((expected_angles.cos(), expected_angles.sin()), dim=1)
            record["endpoint_input_error"] = finite((tensor(endpoint_inputs, device) - expected_grid).abs().max())
            losses, times, snapshot_times = saved["losses"], saved["times"], saved["snapshot_times"]
            replay = evaluate_saved(small, device)
            record["checkpoint_replay_max"] = finite((f - replay).abs().max())
            initial = evaluate_saved(small, device, saved["circle_inputs"], snapshot=0)
            record["initial_checkpoint_replay_max"] = finite(
                (initial - tensor(saved["circle_predictions"][0], device)).abs().max())
            training = evaluate_saved(small, device, small["training_inputs"])
            labels = tensor(small["labels"], device)
            actual_loss = finite((training - labels).square().mean())
            record["recomputed_training_loss"] = actual_loss
            initial_training = evaluate_saved(small, device, small["training_inputs"], snapshot=0)
            initial_loss = finite((initial_training - labels).square().mean())
            record["initial_loss_replay_error"] = (finite(abs(initial_loss - float(losses[0])))
                                                    if initial_loss is not None else None)
            if actual_loss is not None and record["loss"] is not None:
                record["loss_replay_error"] = abs(actual_loss - record["loss"])
                record["loss_trace_final_error"] = finite(abs(float(losses[-1]) - record["loss"]))
            training_angles = tensor(np.asarray(CASES_V2[case]["angles_degrees"]), device) * (math.pi / 180)
            expected_inputs = torch.stack((training_angles.cos(), training_angles.sin()), dim=1)
            record["training_input_error"] = finite((tensor(small["training_inputs"], device)
                                                       - expected_inputs).abs().max())
            record["labels_error"] = finite((labels - tensor(np.asarray(CASES_V2[case]["labels"]), device)).abs().max())
            # The whole loss trace is retained; first crossing is checked at
            # accepted steps. Within-step localization belongs to the producer.
            lt, tt = tensor(losses, device), tensor(times, device)
            trace_valid = (len(losses) == len(times) and len(times) > 0 and
                           bool(torch.isfinite(lt).all()) and bool(torch.isfinite(tt).all()) and
                           bool((tt[1:] > tt[:-1]).all()) and record["time"] is not None and
                           abs(float(times[-1]) - record["time"]) <= REPLAY_TOLERANCE and
                           abs(float(snapshot_times[-1]) - float(times[-1])) <= REPLAY_TOLERANCE)
            record["first_crossing_verified"] = bool(trace_valid and
                float(losses[-1]) <= THRESHOLD * (1 + 1e-8) and bool((lt[:-1] > THRESHOLD).all()))
            checks = ("checkpoint_replay_max", "initial_checkpoint_replay_max", "loss_replay_error",
                      "loss_trace_final_error", "initial_loss_replay_error", "training_input_error", "labels_error",
                      "endpoint_grid_error", "endpoint_input_error")
            for name in checks:
                if record[name] is None or record[name] > REPLAY_TOLERANCE:
                    record["reasons"].append(f"failed {name}")
            if not trace_valid:
                record["reasons"].append("invalid loss/time trace")
            record["replay_valid"] = bool(summary_path.exists() and trace_valid and
                all(record[name] is not None and record[name] <= REPLAY_TOLERANCE for name in checks))
            record["fitted"] = bool(record["status"] == "fitted" and actual_loss is not None and
                                      actual_loss <= THRESHOLD * (1 + 1e-8) and record["first_crossing_verified"])
            if not record["fitted"]:
                record["reasons"].append(f"not fitted: {record['status']}, loss={actual_loss}")
            if not bool(torch.isfinite(f).all()):
                record["reasons"].append("nonfinite endpoint output")
                record["replay_valid"] = False
            return record, {"prediction": f, "angles": angles, "inputs": endpoint_inputs}
    except (OSError, ValueError, KeyError, RuntimeError, IndexError) as exc:
        record["reasons"].append(f"array/replay failure: {type(exc).__name__}: {exc}")
        return record, None


@torch.no_grad()
def metrics(error):
    absolute = error.abs()
    return {"l1": finite(absolute.mean()), "l2": finite(error.square().mean().sqrt()),
            "mse": finite(error.square().mean()), "max_abs": finite(absolute.max())}


@torch.no_grad()
def aggregate(rows, model, cases, device):
    selected = [row for row in rows if row["model"] == model and row["case"] in cases]
    out = {"model": model, "case_count": len(selected), "cases": list(cases)}
    for suite, prefix in (("primary", ""), ("refined", "refined_")):
        for field in ("l1", "l2", "max_abs"):
            values = torch.tensor([row[prefix + field] for row in selected], device=device, dtype=torch.float64)
            out[f"{suite}_mean_case_{field}"] = finite(values.mean()) if len(values) else None
            out[f"{suite}_max_case_{field}"] = finite(values.max()) if len(values) else None
    return out


def number(value):
    return "—" if value is None else f"{value:.5f}"


def metric_table(rows, field):
    table = "| Configuration | " + " | ".join(MODELS) + " |\n|---|" + "---:|" * len(MODELS) + "\n"
    for case in CASES_V2:
        cells = []
        for model in MODELS:
            row = next(r for r in rows if r["case"] == case and r["model"] == model)
            if not row["eligible"]:
                cells.append(f"NOT FITTED ({row['status']}; loss {row['loss']})")
            else:
                cells.append(number(row[field]) + (" †" if not row["valid"] else ""))
        table += "| " + case + " | " + " | ".join(cells) + " |\n"
    return table


def aggregate_table(aggregates):
    fields = ("primary_mean_case_l2", "primary_max_case_l2", "primary_mean_case_max_abs",
              "primary_max_case_max_abs", "primary_mean_case_l1", "primary_max_case_l1")
    table = "| Model | Cases | Mean case RMS | Max case RMS | Mean case maxabs | Max case maxabs | Mean case L1 | Max case L1 |\n"
    table += "|---|---:|---:|---:|---:|---:|---:|---:|\n"
    for row in aggregates:
        table += "| " + row["model"] + f" | {row['case_count']} | " + " | ".join(number(row[k]) for k in fields) + " |\n"
    return table


def figures(out, plots, rows):
    # Plotting only: scientific metrics and checkpoint replay run on the GPU.
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    fig, axes = plt.subplots(3, 4, figsize=(14, 10), subplot_kw={"projection": "polar"})
    for ax, (case, config) in zip(axes.flat, CASES_V2.items()):
        angles = np.deg2rad(config["angles_degrees"])
        labels = np.asarray(config["labels"])
        for label, color, marker in ((1, "#ba332c", "o"), (-1, "#1764a2", "s")):
            mask = labels == label
            ax.scatter(angles[mask], np.ones(mask.sum()), c=color, marker=marker, s=38)
        for angle, label in zip(angles, labels):
            ax.text(angle, 1.16, f"{label:+g}", ha="center", va="center", fontsize=8)
        ax.set_ylim(0, 1.35)
        ax.set_yticks([])
        ax.set_title(case, fontsize=10, pad=16)
    fig.suptitle("Twelve fixed configurations: eight circle inputs, labels +1 (red) / −1 (blue)")
    fig.tight_layout(rect=(0, 0, 1, .96))
    fig.savefig(out / "configuration_geometry.png", dpi=160)
    plt.close(fig)
    lookup = {(r["case"], r["model"]): r for r in rows}
    for p in ORDERS:
        for errors in (False, True):
            fig, axes = plt.subplots(3, 4, figsize=(17, 10), sharex=True)
            for ax, (case, config) in zip(axes.flat, CASES_V2.items()):
                data = plots.get(case, {})
                full = data.get("full")
                if full is not None and not errors:
                    ax.plot(full["angles"] * 180 / np.pi, full["prediction"], c="black", lw=1.7,
                            ls="-" if full["valid"] else "--")
                if not errors:
                    ax.scatter(config["angles_degrees"], config["labels"], color="black", marker="x", s=24, zorder=5)
                for method in METHODS:
                    model = f"{method}_p{p}"
                    value = data.get(model)
                    if value is None or (errors and full is None):
                        continue
                    row = lookup[case, model]
                    y = np.abs(value["prediction"] - full["prediction"]) if errors else value["prediction"]
                    ax.plot(value["angles"] * 180 / np.pi, y, c=COLORS[method], lw=1.1,
                            ls="-" if row["valid"] else "--")
                invalid = [method for method in METHODS if not lookup[case, f"{method}_p{p}"]["valid"]]
                ax.set_title(case + (" †" if invalid else ""), fontsize=10)
                ax.set_xlim(0, 360)
                ax.set_xticks((0, 90, 180, 270, 360))
                ax.grid(alpha=.2)
                if invalid:
                    ax.text(.02, .03, "Not validated: " + ", ".join(invalid), transform=ax.transAxes, fontsize=7)
            handles = [Line2D([0], [0], c=COLORS[m], label=m) for m in METHODS]
            if not errors:
                handles.insert(0, Line2D([0], [0], c="black", label="Full network"))
            fig.legend(handles=handles, loc="upper center", ncol=len(handles), bbox_to_anchor=(.5, .97))
            fig.suptitle(f"p={p}: " + ("absolute circle error" if errors else "learned circle functions") +
                         " (dashed: terminal diagnostics failing a validity gate)")
            fig.supxlabel("Circle angle (degrees)")
            fig.supylabel("Absolute prediction error" if errors else "Prediction")
            fig.tight_layout(rect=(.015, .02, 1, .925))
            fig.savefig(out / f"{'absolute_errors' if errors else 'learned_functions'}_p{p}.png", dpi=160)
            plt.close(fig)


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--refined", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    provenance = validate_configs(args.primary, args.refined)
    device = setup(args.device)
    args.out.mkdir(parents=True, exist_ok=False)
    rows, trajectories, validations, pointwise, plots = [], [], {}, {}, {}
    for case in CASES_V2:
        cells = {}
        plots[case] = {}
        for model in ["full"] + MODELS:
            key = f"{case}_{model}"
            pr, pa = audit_cell(args.primary, case, model, "primary", device)
            rr, ra = audit_cell(args.refined, case, model, "refined", device)
            trajectories.extend((pr, rr))
            refinement = None
            reasons = [f"{suite}: {reason}" for suite, record in (("primary", pr), ("refined", rr))
                       for reason in record["reasons"]]
            aligned = pa is not None and ra is not None
            if aligned:
                aligned = np.array_equal(pa["angles"], ra["angles"]) and np.array_equal(pa["inputs"], ra["inputs"])
                if aligned:
                    refinement = finite((pa["prediction"] - ra["prediction"]).abs().max())
                else:
                    reasons.append("primary/refined angle grids differ")
            if refinement is None or refinement > REFINEMENT_LIMIT:
                reasons.append(f"refinement maximum {refinement} exceeds/misses {REFINEMENT_LIMIT}")
            valid = bool(pr["fitted"] and rr["fitted"] and pr["replay_valid"] and rr["replay_valid"] and
                         refinement is not None and refinement <= REFINEMENT_LIMIT)
            validations[key] = {"primary": pr, "refined": rr, "step_refinement_endpoint_max": refinement,
                                "valid": valid, "reasons": reasons}
            cells[model] = (pr, pa, rr, ra, valid)
            if pa is not None:
                plots[case][model] = {"angles": pa["angles"], "prediction": pa["prediction"].cpu().numpy(), "valid": valid}
                pointwise[key + "_primary_prediction"] = plots[case][model]["prediction"]
                pointwise[key + "_angles"] = pa["angles"]
            if ra is not None:
                pointwise[key + "_refined_prediction"] = ra["prediction"].cpu().numpy()
        fp, fa, fr, fra, full_valid = cells["full"]
        for model in MODELS:
            key = f"{case}_{model}"
            pr, pa, rr, ra, model_valid = cells[model]
            pair_primary = bool(pr["fitted"] and fp["fitted"] and pr["replay_valid"] and fp["replay_valid"])
            pair_refined = bool(rr["fitted"] and fr["fitted"] and rr["replay_valid"] and fr["replay_valid"])
            row = {"case": case, "model": model, "eligible": pair_primary,
                   "refined_eligible": pair_refined, "valid": model_valid and full_valid,
                   "common_case": False, "status": pr["status"], "full_status": fp["status"],
                   "refined_status": rr["status"], "refined_full_status": fr["status"],
                   "loss": pr["loss"], "full_loss": fp["loss"], "time": pr["time"],
                   "full_time": fp["time"], "seconds": pr["seconds"],
                   "refined_loss": rr["loss"], "refined_full_loss": fr["loss"],
                   "refined_time": rr["time"], "refined_full_time": fr["time"],
                   "refined_seconds": rr["seconds"],
                   "step_refinement_endpoint_max": validations[key]["step_refinement_endpoint_max"],
                   "full_step_refinement_endpoint_max": validations[case + "_full"]["step_refinement_endpoint_max"],
                   "rms1": finite(pr["summary"].get("rms_hidden1")),
                   "rms2": finite(pr["summary"].get("rms_hidden2")),
                   "reasons": validations[key]["reasons"] + ["full: " + r for r in validations[case + "_full"]["reasons"]]}
            for field in ("l1", "l2", "mse", "max_abs"):
                for prefix in ("", "refined_", "terminal_", "refined_terminal_"):
                    row[prefix + field] = None
            row["grid_max_change"], row["grid_l2_change"] = None, None
            for suite, value, full, eligible, prefix in (("primary", pa, fa, pair_primary, ""),
                                                        ("refined", ra, fra, pair_refined, "refined_")):
                if value is None or full is None:
                    continue
                if not np.array_equal(value["angles"], full["angles"]):
                    row["valid"] = False
                    row["reasons"].append(f"{suite}: full/closure angle grids differ")
                    continue
                error = value["prediction"] - full["prediction"]
                measured = metrics(error)
                row.update({prefix + "terminal_" + k: v for k, v in measured.items()})
                if eligible:
                    row.update({prefix + k: v for k, v in measured.items()})
                pointwise[key + f"_{suite}_signed_error"] = error.cpu().numpy()
                pointwise[key + f"_{suite}_absolute_error"] = error.abs().cpu().numpy()
                if suite == "primary":
                    row["grid_max_change"] = finite(error.abs().max() - error[::2].abs().max())
                    row["grid_l2_change"] = finite((error.square().mean().sqrt() - error[::2].square().mean().sqrt()).abs())
            rows.append(row)
        print(f"Analyzed {case}: {sum(r['valid'] for r in rows if r['case'] == case)}/9 valid comparisons", flush=True)
    common = [case for case in CASES_V2 if all(row["valid"] for row in rows if row["case"] == case)]
    for row in rows:
        row["common_case"] = row["case"] in common
    common_summary = [aggregate(rows, model, common, device) for model in MODELS]
    method_summary = [aggregate(rows, model, [r["case"] for r in rows if r["model"] == model and r["valid"]], device)
                      for model in MODELS]
    coverage = [{"model": model, "declared_cases": len(CASES_V2), "common_valid_cases": len(common),
                 "primary_fitted_pairs": sum(r["eligible"] for r in rows if r["model"] == model),
                 "both_suites_fitted_pairs": sum(r["eligible"] and r["refined_eligible"] for r in rows if r["model"] == model),
                 "method_valid_cases": sum(r["valid"] for r in rows if r["model"] == model)} for model in MODELS]
    exclusions = {case: {r["model"]: r["reasons"] for r in rows if r["case"] == case and not r["valid"]}
                  for case in CASES_V2 if case not in common}
    definitions = ("For each configuration and model, form the pointwise endpoint error relative to that "
        "configuration's full network at each predictor's own first detected accepted-step MSE 1e-3 crossing, "
        "localized by parameter-chord bisection; this is not a certified exact-flow first crossing. "
        "Case RMS is sqrt(mean(error^2)); "
        "case maxabs is max(abs(error)); case L1 is mean(abs(error)), on 8192 uniform circle angles. "
        "The primary nine-row summary takes the arithmetic mean and maximum of each case metric over the SAME "
        "common configuration set: full plus all nine models fitted in both suites, passed replay, and each "
        "primary/refined endpoint difference was <=0.01. Mean case RMS is not pooled RMS. Separate method-specific "
        "summaries may cover different cases and must not be read as a matched cross-method ranking. "
        "Terminal diagnostics for unfitted runs are retained separately and excluded from learned-function summaries.")
    save_json(args.out / "metrics.json", rows)
    save_json(args.out / "trajectories.json", trajectories)
    save_json(args.out / "validation.json", validations)
    save_json(args.out / "summary.json", {"definitions": definitions, "declared_cases": list(CASES_V2),
        "common_case_count": len(common), "common_cases": common, "exclusions": exclusions,
        "common_summary": common_summary, "method_specific_summary": method_summary, "coverage": coverage})
    for name, data in (("metrics", rows), ("trajectories", trajectories), ("common_summary", common_summary),
                       ("method_specific_summary", method_summary), ("coverage", coverage)):
        csv_file(args.out / f"{name}.csv", data)
    for name, field in (("rms", "l2"), ("max_abs", "max_abs")):
        csv_file(args.out / f"per_case_{name}.csv", [{"case": case, **{model:
            next(r[field] for r in rows if r["case"] == case and r["model"] == model) for model in MODELS}}
            for case in CASES_V2])
    np.savez(args.out / "circle_errors.npz", **pointwise)
    report = "# Twelve-configuration learned-circle comparison\n\n" + definitions + "\n\n"
    report += f"Common valid configurations: **{len(common)}/{len(CASES_V2)}**. "
    report += "Included: " + (", ".join(common) or "none") + ".\n\n"
    report += "## Primary matched summary\n\n" + aggregate_table(common_summary)
    report += "\n## Per-configuration RMS\n\n" + metric_table(rows, "l2")
    report += "\n## Per-configuration maximum absolute error\n\n" + metric_table(rows, "max_abs")
    report += "\n† Primary fitted comparison failing refinement or replay; excluded from validated aggregates. "
    report += "A NOT FITTED cell can also reflect an unfitted full reference; all statuses/losses/times are in trajectories.csv.\n"
    report += "\n## Method-specific coverage (different case sets)\n\n" + aggregate_table(method_summary)
    report += "\n## Exclusions from the common configuration set\n\n"
    if exclusions:
        for case, failures in exclusions.items():
            report += f"- {case}: " + "; ".join(f"{model}: {', '.join(reasons)}" for model, reasons in failures.items()) + "\n"
    else:
        report += "None.\n"
    report += ("\nThe NPZ retains primary and refined signed/absolute pointwise errors, terminal predictions, and angle grids. "
               "Raw producer NPZ files retain arbitrary-angle checkpoint reconstruction. Maxima are sampled-circle maxima, "
               "not certified continuous suprema. These deterministic, one-seed comparisons do not establish statistical "
               "significance, population convergence, or universal dictionary superiority.\n")
    (args.out / "tables.md").write_text(report)
    figures(args.out, plots, rows)
    save_json(args.out / "analysis_provenance.json", {"command": sys.argv, "device": device,
        "analysis_sha256": sha256(Path(__file__)), "checkpoint_replay_source_sha256": sha256(Path(__file__).with_name("analyze.py")),
        "producer_configs": provenance, "simulation_source_correspondence": True,
        "summary_source": "per-cell summary.json; root results.json is not used",
        "refinement_endpoint_max_limit": REFINEMENT_LIMIT, "replay_tolerance": REPLAY_TOLERANCE})
    files = sorted(p for root in (args.primary, args.refined, args.out) for p in root.rglob("*") if p.is_file())
    save_json(args.out / "artifact_hashes.json", {str(p): sha256(p) for p in files})
    print(aggregate_table(common_summary), flush=True)
    print(f"Common valid cases: {len(common)}/{len(CASES_V2)}; exclusions: {', '.join(exclusions) or 'none'}", flush=True)


if __name__ == "__main__":
    main()
