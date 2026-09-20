"""Replay and compare saved scaling endpoints; never fit an asymptotic rate.

Historical input is a selected_levels.json file (or its containing directory).
Every error uses the selected full reference at the corresponding primary or
refined level. Extra roots replace a cell's pair by its latest two attempted
levels, including failed attempts. Simulation and metric arithmetic require CUDA.
"""
import argparse
import csv
import json
import math
from pathlib import Path
import sys

import numpy as np
import torch

from analyze import evaluate_saved, tensor
from benchmark import ROOT, save_json, setup
from diverse_analyze import finite, sha256, metrics
from diverse_cases import CASES_V2


METHODS = ("ours", "gaussian", "orthogonal")
DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21), 6: (213, 28),
              7: (333, 36), 8: (499, 45), 9: (720, 55)}
TARGETS = (1., .5, .3, .2, .1, .05, .02, .01)
GATE, REPLAY = .01, 1e-10
NAMESPACE = (ROOT / "data/generated/random_dictionary_learned_circle_20260920").resolve()
COLORS = {"ours": "#1261a0", "gaussian": "#ce6c1b", "orthogonal": "#7d4196"}


def owned_path(path):
    path = Path(path).resolve()
    if not path.is_relative_to(NAMESPACE):
        raise ValueError(f"Input/output outside this study's generated namespace: {path}")
    return path


def cases_of(config):
    cases = config["cases"]
    return cases if isinstance(cases, dict) else {name: CASES_V2[name] for name in cases}


def identity(case):
    return {key: case[key] for key in ("angles_degrees", "labels")}


def load_configs(root):
    paths = sorted(root.glob("config*.json"))
    if not paths:
        raise ValueError(f"No producer config in {root}")
    return [{"path": str(path.resolve()), "sha256": sha256(path),
             "config": json.loads(path.read_text())} for path in paths]


def config_for(entries, case, model):
    order = None if model == "full" else int(model.rsplit("_p", 1)[1])
    matches = [entry for entry in entries if case in cases_of(entry["config"]) and
               (order is None or order in entry["config"]["orders"])]
    if not matches:
        raise ValueError(f"Producer config does not declare {case}_{model}")
    first = matches[0]["config"]
    for entry in matches[1:]:
        for key in ("width", "network_seed", "dictionary_seed", "rtol", "atol"):
            if entry["config"].get(key) != first.get(key):
                raise ValueError(f"Ambiguous producer metadata for {case}_{model}: {key}")
    key = f"{case}_{model}"
    explicit = [entry for entry in matches if key in entry["config"].get("selected_cells", [])]
    executed = [entry for entry in matches if (model == "full" and entry["config"].get("include_full", False)) or
                (order is not None and order in entry["config"].get("orders_executed", []))]
    preferred = explicit or executed or matches
    worker_matches = [entry for entry in preferred if list(cases_of(entry["config"])).index(case) %
                      entry["config"].get("workers", 2) == entry["config"].get("worker", 0)]
    return (worker_matches or preferred)[0]


def check_correspondence(config, baseline, case):
    for key in ("width", "network_seed", "dictionary_seed"):
        if config.get(key) != baseline.get(key):
            raise ValueError(f"Mismatched {key} for {case}")
    for key, default in (("threshold", 1e-3), ("dtype", "float64"), ("endpoint_nodes", 8192)):
        if config.get(key, default) != baseline.get(key, default):
            raise ValueError(f"Mismatched {key} for {case}")
    if identity(cases_of(config)[case]) != identity(cases_of(baseline)[case]):
        raise ValueError(f"Mismatched training configuration: {case}")
    # Study adapters may gain features. Only shared maintained scientific source
    # hashes are compared; every complete producer hash map is retained below.
    old = baseline.get("source_hashes", {})
    for path, digest in config.get("source_hashes", {}).items():
        if (path.startswith("code/") or "/code/pde/" in path) and path in old and old[path] != digest:
            raise ValueError(f"Changed maintained simulation source: {path}")


def source_level(directory, name, configs, baseline, case, model, metadata=None):
    directory = owned_path(directory)
    root = str(directory.parent)
    if root not in configs:
        configs[root] = load_configs(directory.parent)
    entry = config_for(configs[root], case, model)
    config = entry["config"]
    check_correspondence(config, baseline, case)
    if metadata is not None:
        for key in ("rtol", "atol"):
            if metadata[key] != config[key]:
                raise ValueError(f"Selected tolerance disagrees with producer: {directory} {key}")
    return {"name": name, "directory": str(directory), "config_path": entry["path"],
            "rtol": config["rtol"], "atol": config["atol"], "config": config}


def select_inputs(args):
    roots = [owned_path(root) for root in (args.primary, args.refined, *args.extra)]
    configs = {str(root): load_configs(root) for root in roots}
    baseline = configs[str(roots[0])][0]["config"]
    cases = cases_of(baseline)
    orders = sorted(set(args.orders if args.orders is not None else baseline["orders"]))
    if not orders or not set(orders).issubset(baseline["orders"]):
        raise ValueError("--orders must be a nonempty subset of the planned producer orders")
    refined = configs[str(roots[1])][0]["config"]
    if set(cases_of(refined)) != set(cases) or refined["orders"] != baseline["orders"]:
        raise ValueError("Primary/refinement must declare the same cases and orders")
    history, historical_path = None, None
    if args.historical:
        historical_path = owned_path(args.historical)
        if historical_path.is_dir():
            historical_path /= "selected_levels.json"
        history = json.loads(historical_path.read_text())
        if any(order < 6 for order in orders):
            raise ValueError("Historical extension roots must contain only new orders >=6")
        orders = sorted(set(orders) | {1, 3, 5})
    selected, historical_references = {}, {}
    for case in cases:
        for model in ["full"] + [f"{method}_p{order}" for order in orders for method in METHODS]:
            key = f"{case}_{model}"
            refreshed_full = model == "full" and (
                any(entry["config"].get("include_full", False) for entry in configs[str(roots[0])]) or
                any((root / key).exists() for root in roots[:2]))
            historical = history is not None and (
                (model == "full" and not refreshed_full) or
                (model != "full" and int(model.rsplit("_p", 1)[1]) < 6))
            if history is not None and model == "full" and refreshed_full:
                record = history["cells"].get(key)
                if record:
                    historical_references[case] = [source_level(record[f"{suite}_directory"],
                        "historical_reference_" + record[f"{suite}_level"], configs, baseline, case, model,
                        {name: record[f"{suite}_{name}"] for name in ("rtol", "atol")})
                        for suite in ("primary", "refined")]
            if historical:
                record = history["cells"].get(key)
                if record is None:
                    raise ValueError(f"Historical selection omits declared cell: {key}")
                levels = [source_level(record[f"{suite}_directory"], "historical_" + record[f"{suite}_level"],
                            configs, baseline, case, model,
                            {name: record[f"{suite}_{name}"] for name in ("rtol", "atol")})
                          for suite in ("primary", "refined")]
            else:
                levels = [source_level(root / key, suite, configs, baseline, case, model)
                          for root, suite in zip(roots[:2], ("primary", "refined"))]
            for index, root in enumerate(roots[2:], 1):
                # A created directory is an attempted cell even without arrays.
                if (root / key).exists() or any(key in entry["config"].get("selected_cells", []) for entry in configs[str(root)]):
                    levels.append(source_level(root / key, f"extra_{index}", configs, baseline, case, model))
            for first, second in zip(levels, levels[1:]):
                if not all(0 < second[name] < first[name] for name in ("rtol", "atol")):
                    raise ValueError(f"Nondecreasing per-cell tolerances: {key}")
            selected[key] = {"case": case, "model": model, "origin": "historical" if historical else "fresh",
                             "levels": levels, "primary": levels[-2], "refined": levels[-1]}
    return baseline, cases, orders, selected, configs, historical_path, historical_references


@torch.no_grad()
def audit(level, case, model, device):
    directory, config = Path(level["directory"]), level["config"]
    summary_path, arrays_path = directory / "summary.json", directory / "arrays.npz"
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
    record = {key: value for key, value in level.items() if key != "config"}
    record.update(status=summary.get("status", "missing_summary"), loss=finite(summary.get("loss")),
                  time=finite(summary.get("time")), seconds=finite(summary.get("seconds")),
                  replay_valid=False, fitted=False, reasons=[], summary=summary,
                  files={str(path): sha256(path) for path in (summary_path, arrays_path) if path.exists()})
    if "selected_cells" in config:
        record["declared_executed"] = f"{case}_{model}" in config["selected_cells"]
    record["dictionary_metadata"] = []
    if model != "full":
        for path in sorted(directory.parent.glob(f"dictionary_*_{model}.json")):
            record["dictionary_metadata"].append({"path": str(path), "sha256": sha256(path),
                                                  "metadata": json.loads(path.read_text())})
    if not summary_path.exists():
        record["reasons"].append("missing summary.json")
    if not arrays_path.exists():
        record["reasons"].append("missing arrays.npz")
        return record, None
    try:
        with np.load(arrays_path, allow_pickle=False) as saved:
            small = {key: saved[key][[0, -1]] for key in ("w", "c", "M")}
            small.update({key: saved[key] for key in ("endpoint_inputs", "training_inputs", "labels")})
            small.update({key: saved[key] for key in ("b1", "b2") if key in saved})
            width, nodes = config["width"], config.get("endpoint_nodes", 8192)
            training_case = cases_of(config)[case]
            if small["w"].shape != (2, width, 2) or small["c"].shape != (2, width):
                raise ValueError("unexpected state width or input dimension")
            if model == "full":
                if small["M"].shape != (2, width, width) or "b1" in small or "b2" in small:
                    raise ValueError("full reference has unexpected middle-state representation")
                record.update(k1=None, k2=None)
            else:
                k1, k2 = small["b1"].shape[1], small["b2"].shape[1]
                if (small["b1"].shape[0] != width or small["b2"].shape[0] != width or
                        small["M"].shape != (2, k2, k1)):
                    raise ValueError("inconsistent frozen dictionary/state dimensions")
                order = int(model.rsplit("_p", 1)[1])
                if order in DIMENSIONS and (k1, k2) != DIMENSIONS[order]:
                    raise ValueError("saved dimensions disagree with retained dictionary order")
                record.update(k1=k1, k2=k2)
            f = tensor(saved["endpoint_prediction"], device)
            angles, inputs = saved["endpoint_angles"], saved["endpoint_inputs"]
            if f.shape != (nodes,) or angles.shape != (nodes,) or inputs.shape != (nodes, 2):
                raise ValueError("unexpected endpoint grid shape")
            target_angles = torch.arange(nodes, device=device, dtype=torch.float64) * (2 * math.pi / nodes)
            target_grid = torch.stack((target_angles.cos(), target_angles.sin()), 1)
            train_angles = tensor(np.asarray(training_case["angles_degrees"]), device) * (math.pi / 180)
            target_train = torch.stack((train_angles.cos(), train_angles.sin()), 1)
            labels = tensor(small["labels"], device)
            if small["training_inputs"].shape != tuple(target_train.shape) or labels.shape != (len(train_angles),):
                raise ValueError("unexpected training-input/label shape")
            losses, times = tensor(saved["losses"], device), tensor(saved["times"], device)
            snapshots = tensor(saved["snapshot_times"], device)
            training = evaluate_saved(small, device, small["training_inputs"])
            actual_loss = (training - labels).square().mean()
            initial_training = evaluate_saved(small, device, small["training_inputs"], snapshot=0)
            checks = {
                "endpoint_grid_error": finite((tensor(angles, device) - target_angles).abs().max()),
                "endpoint_input_error": finite((tensor(inputs, device) - target_grid).abs().max()),
                "training_input_error": finite((tensor(small["training_inputs"], device) - target_train).abs().max()),
                "labels_error": finite((labels - tensor(np.asarray(training_case["labels"]), device)).abs().max()),
                "checkpoint_replay_max": finite((f - evaluate_saved(small, device)).abs().max()),
                "initial_checkpoint_replay_max": finite((evaluate_saved(small, device, saved["circle_inputs"], 0) -
                                                        tensor(saved["circle_predictions"][0], device)).abs().max()),
                "loss_replay_error": finite((actual_loss - summary.get("loss", float("nan"))).abs()),
                "loss_trace_final_error": finite((losses[-1] - actual_loss).abs()),
                "initial_loss_replay_error": finite(((initial_training - labels).square().mean() - losses[0]).abs()),
            }
            trace_valid = (losses.shape == times.shape and len(times) > 0 and len(snapshots) > 0 and
                bool(torch.isfinite(losses).all()) and bool(torch.isfinite(times).all()) and
                bool((times[1:] > times[:-1]).all()) and record["time"] is not None and
                bool((times[-1] - record["time"]).abs() <= REPLAY) and
                bool((snapshots[-1] - times[-1]).abs() <= REPLAY))
            threshold = config.get("threshold", 1e-3)
            crossing = bool(trace_valid and losses[-1] <= threshold * (1 + 1e-8) and
                            (losses[:-1] > threshold).all())
            for name, value in checks.items():
                if value is None or value > REPLAY:
                    record["reasons"].append(f"failed {name}")
            for name in ("rtol", "atol"):
                if summary.get(name) != config[name]:
                    record["reasons"].append(f"summary/config {name} mismatch")
            if not trace_valid:
                record["reasons"].append("invalid loss/time trace")
            if not bool(torch.isfinite(f).all()):
                record["reasons"].append("nonfinite endpoint prediction")
            record.update(checks, recomputed_training_loss=finite(actual_loss), first_crossing_verified=crossing,
                          replay_valid=not record["reasons"],
                          fitted=bool(record["status"] == "fitted" and crossing and actual_loss <= threshold * (1 + 1e-8)))
            if not record["fitted"]:
                record["reasons"].append(f"not fitted: {record['status']}, loss={finite(actual_loss)}")
            return record, {"prediction": f, "angles": angles, "inputs": inputs}
    except (OSError, ValueError, KeyError, RuntimeError, IndexError, TypeError) as exc:
        record["reasons"].append(f"array/replay failure: {type(exc).__name__}: {exc}")
        return record, None


def aligned(first, second):
    return (first is not None and second is not None and
            np.array_equal(first["angles"], second["angles"]) and
            np.array_equal(first["inputs"], second["inputs"]))


def valid_endpoint(record):
    return record["fitted"] and record["replay_valid"]


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        if rows:
            fields = list(dict.fromkeys(key for row in rows for key in row))
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows({key: json.dumps(value) if isinstance(value, (dict, list)) else value
                              for key, value in row.items()} for row in rows)


@torch.no_grad()
def comparisons(rows, cases, orders, targets, device):
    lookup = {(row["case"], row["model"]): row for row in rows}
    ratios, accuracy, observations = [], [], []
    for case in cases:
        for order in orders:
            group = [lookup[case, f"{method}_p{order}"] for method in METHODS]
            ours = group[0]
            ratio = {"case": case, "order": order, "valid": all(row["valid"] for row in group),
                     "dictionary_columns": ours["dictionary_columns"], "middle_coefficients": ours["middle_coefficients"]}
            for prefix in ("", "refined_"):
                for field in ("l1", "l2", "max_abs"):
                    denominator = ours[prefix + field]
                    for control, row in zip(METHODS[1:], group[1:]):
                        value = row[prefix + field]
                        ratio[prefix + control + "_over_ours_" + field] = (
                            finite(torch.tensor(value, device=device, dtype=torch.float64) / denominator)
                            if ratio["valid"] and value is not None and denominator is not None and denominator > 0 else None)
                    values = [ratio[prefix + control + "_over_ours_" + field] for control in METHODS[1:]]
                    ratio[prefix + "better_random_over_ours_" + field] = (
                        finite(torch.tensor(values, device=device, dtype=torch.float64).min())
                        if all(value is not None for value in values) else None)
            ratios.append(ratio)
        for method in METHODS:
            tested = [lookup[case, f"{method}_p{order}"] for order in orders]
            for field in ("l1", "l2", "max_abs"):
                for target in targets:
                    achieved = [row for row in tested if row["valid"] and row[field] <= target and row["refined_" + field] <= target]
                    best = min(achieved, key=lambda row: row["dictionary_columns"]) if achieved else None
                    accuracy.append({"case": case, "method": method, "metric": field, "target": target,
                        "status": "achieved_at_tested_budget" if best else "not_demonstrated_at_tested_budgets",
                        "smallest_tested_achieving_order": best["order"] if best else None,
                        "dictionary_columns": best["dictionary_columns"] if best else None,
                        "middle_coefficients": best["middle_coefficients"] if best else None,
                        "tested_orders": orders, "valid_tested_orders": [row["order"] for row in tested if row["valid"]],
                        "achieving_tested_orders": [row["order"] for row in achieved],
                        "unresolved_tested_orders": [row["order"] for row in tested if not row["valid"]]})
            valid = [row for row in tested if row["valid"]]
            observations.append({"case": case, "method": method, "tested_orders": orders,
                "valid_orders": [row["order"] for row in valid], "all_tested_valid": len(valid) == len(tested),
                "successive_valid_rms_changes": [{"from_order": left["order"], "to_order": right["order"],
                    "primary_change": finite(torch.tensor(right["l2"], device=device, dtype=torch.float64) - left["l2"]),
                    "refined_change": finite(torch.tensor(right["refined_l2"], device=device, dtype=torch.float64) - left["refined_l2"])}
                    for left, right in zip(valid, valid[1:])]})
    budget_ratios = []
    for case in cases:
        for field in ("l1", "l2", "max_abs"):
            for target in targets:
                matches = {row["method"]: row for row in accuracy if row["case"] == case and
                           row["metric"] == field and row["target"] == target}
                for method in METHODS[1:]:
                    own, control = matches["ours"], matches[method]
                    record = {"case": case, "metric": field, "target": target, "control": method,
                              "ours_status": own["status"], "control_status": control["status"]}
                    for field_name in ("dictionary_columns", "middle_coefficients"):
                        record[field_name + "_ratio"] = (finite(torch.tensor(control[field_name], device=device,
                            dtype=torch.float64) / own[field_name]) if own[field_name] and control[field_name] else None)
                    budget_ratios.append(record)
    return ratios, accuracy, budget_ratios, observations


def plots(out, rows, cases, orders):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(3 * len(cases), 2, figsize=(12, 8 * len(cases)), squeeze=False)
    for index, case in enumerate(cases):
        for metric_index, field in enumerate(("l2", "l1", "max_abs")):
            for column, budget in enumerate(("dictionary_columns", "middle_coefficients")):
                ax = axes[3 * index + metric_index, column]
                for method in METHODS:
                    selected = [next(row for row in rows if row["case"] == case and row["model"] == f"{method}_p{p}") for p in orders]
                    x = [row[budget] for row in selected]
                    for prefix, style in (("", "-"), ("refined_", "--")):
                        y = [row[prefix + field] if row["valid"] else np.nan for row in selected]
                        ax.plot(x, y, style, marker="o", markersize=4, color=COLORS[method],
                                label=method + (" primary" if not prefix else " refined"))
                    invalid = [row for row in selected if not row["valid"] and row[field] is not None]
                    ax.scatter([row[budget] for row in invalid], [row[field] for row in invalid],
                               color=COLORS[method], marker="x", s=45)
                ax.set_xscale("log")
                ax.set_yscale("log")
                ax.set_xlabel("Total dictionary columns K1+K2" if column == 0 else "Middle coefficients K1*K2")
                ax.set_ylabel({"l2": "Circle RMS", "l1": "Circle mean absolute error", "max_abs": "Sampled-circle maximum error"}[field])
                ax.set_title(case)
                ax.grid(alpha=.2)
                ax.legend(fontsize=7)
    fig.suptitle("Endpoint error versus tested budget; × = unresolved fitted diagnostic; no fitted slopes")
    fig.tight_layout(rect=(0, 0, 1, .98))
    fig.savefig(out / "curves.png", dpi=160)
    plt.close(fig)


def number(value):
    return "—" if value is None else f"{value:.6g}"


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--refined", type=Path, required=True)
    parser.add_argument("--historical", type=Path)
    parser.add_argument("--orders", type=int, nargs="+", help="Executed new orders for interim reporting; default: all planned orders")
    parser.add_argument("--extra", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    baseline, cases, orders, selected, configs, historical_path, historical_references = select_inputs(args)
    out = owned_path(args.out)
    device = setup(args.device)
    out.mkdir(parents=True, exist_ok=False)
    rows, validation, pointwise, reference_crosschecks = [], {}, {}, {}
    for case in cases:
        audited = {}
        for model in ["full"] + [f"{method}_p{order}" for order in orders for method in METHODS]:
            key = f"{case}_{model}"
            selection = selected[key]
            levels = [audit(level, case, model, device) for level in selection["levels"]]
            (pr, pa), (rr, ra) = levels[-2:]
            discrepancy = finite((pa["prediction"] - ra["prediction"]).abs().max()) if aligned(pa, ra) else None
            valid = bool(valid_endpoint(pr) and valid_endpoint(rr) and discrepancy is not None and discrepancy <= GATE)
            reasons = [f"{suite}: {reason}" for suite, record in (("primary", pr), ("refined", rr)) for reason in record["reasons"]]
            if discrepancy is None or discrepancy > GATE:
                reasons.append(f"endpoint refinement discrepancy {discrepancy} exceeds/misses {GATE}")
            if model != "full" and (pr.get("k1"), pr.get("k2")) != (rr.get("k1"), rr.get("k2")):
                valid = False
                reasons.append("primary/refined dictionary dimensions differ")
            validation[key] = {"valid": valid, "step_refinement_endpoint_max": discrepancy, "reasons": reasons,
                               "primary": pr, "refined": rr, "all_levels": [record for record, _ in levels]}
            audited[model] = (pr, pa, rr, ra, valid)
            for suite, arrays in (("primary", pa), ("refined", ra)):
                if arrays is not None:
                    for name in ("angles", "inputs"):
                        pointwise[f"{key}_{suite}_{name}"] = arrays[name]
                    pointwise[f"{key}_{suite}_prediction"] = arrays["prediction"].cpu().numpy()
        fp, fa, fr, fra, full_valid = audited["full"]
        if case in historical_references:
            reference_crosschecks[case] = {}
            for suite, old_level, current in zip(("primary", "refined"), historical_references[case], (fa, fra)):
                record, old = audit(old_level, case, "full", device)
                reference_crosschecks[case][suite] = {"historical": record,
                    "refreshed_minus_historical_endpoint_max": finite((current["prediction"] - old["prediction"]).abs().max())
                    if aligned(current, old) else None}
                if old is not None:
                    pointwise[f"{case}_historical_full_{suite}_prediction"] = old["prediction"].cpu().numpy()
        for order in orders:
            for method in METHODS:
                model, key = f"{method}_p{order}", f"{case}_{method}_p{order}"
                pr, pa, rr, ra, model_valid = audited[model]
                fallback = DIMENSIONS.get(order, (None, None))
                k1, k2 = pr.get("k1", fallback[0]), pr.get("k2", fallback[1])
                row = {"case": case, "model": model, "method": method, "order": order, "origin": selected[key]["origin"],
                    "k1": k1, "k2": k2, "dictionary_columns": k1 + k2 if k1 and k2 else None,
                    "middle_coefficients": k1 * k2 if k1 and k2 else None,
                    "total_state_scalars": 3 * baseline["width"] + k1 * k2 if k1 and k2 else None,
                    "dictionary_storage_scalars": baseline["width"] * (k1 + k2) if k1 and k2 else None,
                    "valid": model_valid and full_valid, "eligible": valid_endpoint(pr) and valid_endpoint(fp),
                    "refined_eligible": valid_endpoint(rr) and valid_endpoint(fr),
                    "step_refinement_endpoint_max": validation[key]["step_refinement_endpoint_max"],
                    "full_step_refinement_endpoint_max": validation[case + "_full"]["step_refinement_endpoint_max"],
                    "reasons": validation[key]["reasons"] + ["full: " + reason for reason in validation[case + "_full"]["reasons"]]}
                for prefix, record in (("", pr), ("refined_", rr), ("full_", fp), ("full_refined_", fr)):
                    row.update({prefix + name: record.get(name) for name in ("directory", "rtol", "atol", "status", "loss", "time", "seconds")})
                for prefix, arrays, full, eligible in (("", pa, fa, row["eligible"]), ("refined_", ra, fra, row["refined_eligible"])):
                    row.update({prefix + diagnostic + field: None for diagnostic in ("", "terminal_") for field in ("l1", "l2", "mse", "max_abs")})
                    row[prefix + "grid_l2_change"], row[prefix + "grid_max_change"] = None, None
                    if aligned(arrays, full):
                        error = arrays["prediction"] - full["prediction"]
                        measured = metrics(error)
                        if any(value is None for value in measured.values()):
                            row["valid"] = False
                            row["reasons"].append(prefix + "nonfinite endpoint error metric")
                        row.update({prefix + "terminal_" + name: value for name, value in measured.items()})
                        if eligible:
                            row.update({prefix + name: value for name, value in measured.items()})
                        pointwise[key + ("_refined" if prefix else "_primary") + "_signed_error"] = error.cpu().numpy()
                        pointwise[key + ("_refined" if prefix else "_primary") + "_absolute_error"] = error.abs().cpu().numpy()
                        row[prefix + "grid_l2_change"] = finite((error.square().mean().sqrt() - error[::2].square().mean().sqrt()).abs())
                        row[prefix + "grid_max_change"] = finite((error.abs().max() - error[::2].abs().max()).abs())
                    else:
                        row["valid"] = False
                        row["reasons"].append(prefix + "full/closure grids missing or different")
                rows.append(row)
        print(f"Analyzed {case}: {sum(row['valid'] for row in rows if row['case'] == case)}/{3 * len(orders)} valid pairs", flush=True)
        # Keep retained outputs on CPU; no saved state or circle tensor is needed
        # after this case. This also limits GPU memory during later rendering.
        del audited, levels, pr, pa, rr, ra, fp, fa, fr, fra
    targets = baseline.get("target_accuracies", TARGETS)
    ratios, accuracy, budget_ratios, observations = comparisons(rows, cases, orders, targets, device)
    definitions = (
        "Each predictor is evaluated at its own first detected accepted-step training-MSE threshold crossing; "
        "parameter-chord localization is not a certified exact-flow first crossing. Errors use the corresponding "
        "selected primary/refined full endpoint on the entire saved uniform circle grid. L2 means RMS, L1 means "
        "mean absolute error, and max_abs is a sampled maximum, not a certified continuous supremum. A valid pair "
        "requires fitted/replayed full and closure endpoints at both selected tolerances and each predictor's "
        "refinement discrepancy <=0.01. Both tolerance errors must meet a target. Budgets denote retained nominal "
        "columns and middle coefficients, not effective rank: full first rows and readout still evolve. No fitted "
        "slopes, arbitrary-accuracy guarantee, statistical significance, or universal superiority follows. Missing, "
        "unfitted, or unstable cells cannot establish failure at any untested budget.")
    summary = {"definitions": definitions, "stage": baseline.get("stage"), "cases": list(cases), "orders": orders,
        "width": baseline["width"], "network_seed": baseline["network_seed"], "dictionary_seed": baseline["dictionary_seed"],
        "threshold": baseline.get("threshold", 1e-3), "refinement_gate": GATE,
        "full_state_scalars": baseline["width"] ** 2 + 3 * baseline["width"],
        "historical_extension": historical_path is not None, "valid_comparisons": sum(row["valid"] for row in rows),
        "declared_comparisons": len(rows), "all_comparisons_valid": all(row["valid"] for row in rows),
        "scientific_verdict": "No automatic scientific PASS; finite tested-budget observations only.",
        "random_over_ours": ratios, "target_accuracy": accuracy, "tested_budget_ratios": budget_ratios,
        "observations": observations, "exclusions": {row["case"] + "_" + row["model"]: row["reasons"] for row in rows if not row["valid"]}}
    summary["historical_reference_crosschecks"] = reference_crosschecks
    save_json(out / "metrics.json", rows)
    write_csv(out / "metrics.csv", rows)
    save_json(out / "summary.json", summary)
    save_json(out / "validation.json", validation)
    for name, values in (("ratios", ratios), ("target_accuracy", accuracy), ("tested_budget_ratios", budget_ratios)):
        write_csv(out / f"{name}.csv", values)
    np.savez(out / "circle_errors.npz", **pointwise)
    report = "# Tested dictionary-budget scaling\n\n" + definitions + "\n\n"
    report += f"Valid paired comparisons: **{summary['valid_comparisons']}/{len(rows)}**.\n\n"
    report += "State scalars = 3n + K1*K2; frozen dictionary storage = n(K1+K2), reported separately.\n\n"
    report += "| Case | Model | K1+K2 | K1*K2 | RMS primary / refined | L1 primary / refined | Max primary / refined | Valid |\n|---|---|---:|---:|---:|---:|---:|---|\n"
    for row in rows:
        values = [f"{number(row[field])} / {number(row['refined_' + field])}" for field in ("l2", "l1", "max_abs")]
        report += f"| {row['case']} | {row['model']} | {row['dictionary_columns']} | {row['middle_coefficients']} | " + " | ".join(values) + f" | {row['valid']} |\n"
    report += "\n## Random/ours error ratios at matched budgets\n\n| Case | Order | Gaussian/ours RMS, primary / refined | Orthogonal/ours RMS, primary / refined | Valid |\n|---|---:|---:|---:|---|\n"
    for row in ratios:
        values = [f"{number(row[method + '_over_ours_l2'])} / {number(row['refined_' + method + '_over_ours_l2'])}" for method in METHODS[1:]]
        report += f"| {row['case']} | {row['order']} | " + " | ".join(values) + f" | {row['valid']} |\n"
    report += "\n## Smallest tested budget meeting target at both tolerances\n\nA blank means not demonstrated among tested valid budgets; it is not a lower bound on the required budget. All L1 targets and tested-budget ratios are also in CSV/JSON.\n\n"
    report += "| Case | Metric | Target | Ours K1+K2 (K1*K2) | Gaussian K1+K2 (K1*K2) | Orthogonal K1+K2 (K1*K2) |\n|---|---|---:|---:|---:|---:|\n"
    for case in cases:
        for field in ("l2", "max_abs"):
            for target in targets:
                cells = []
                for method in METHODS:
                    match = next(row for row in accuracy if row["case"] == case and row["metric"] == field and row["target"] == target and row["method"] == method)
                    cells.append(f"{match['dictionary_columns']} ({match['middle_coefficients']})" if match["dictionary_columns"] else "—")
                report += f"| {case} | {field} | {target:g} | " + " | ".join(cells) + " |\n"
    report += "\n## Unresolved comparisons\n\n"
    report += "\n".join(f"- {key}: {'; '.join(reasons)}" for key, reasons in summary["exclusions"].items()) or "None."
    report += "\n\nAll selected endpoint paths, file hashes, producer configurations and tolerance levels are retained in provenance.json and validation.json; pointwise primary/refined predictions and errors are in circle_errors.npz.\n"
    (out / "tables.md").write_text(report)
    plots(out, rows, cases, orders)
    provenance = {"command": sys.argv, "device": device, "analysis_sha256": sha256(Path(__file__)),
        "helper_sha256": {str(Path(__file__).with_name(name)): sha256(Path(__file__).with_name(name))
                          for name in ("analyze.py", "diverse_analyze.py", "benchmark.py")},
        "producer_configs": configs,
        "historical_selection": {"path": str(historical_path), "sha256": sha256(historical_path)} if historical_path else None,
        "selected_cells": {key: {"origin": value["origin"], **{suite: validation[key][suite] for suite in ("primary", "refined")}} for key, value in selected.items()},
        "historical_reference_crosschecks": reference_crosschecks,
        "maintained_source_hash_policy": "Reject mismatches in shared maintained code hashes; record every study-helper hash without requiring old/new adapters to be identical.",
        "replay_tolerance": REPLAY, "refinement_endpoint_max_limit": GATE,
        "output_hashes": {str(path): sha256(path) for path in sorted(out.iterdir()) if path.is_file()}}
    save_json(out / "provenance.json", provenance)
    torch.cuda.synchronize(device)
    torch.cuda.empty_cache()
    print(f"Saved {out}; valid comparisons {summary['valid_comparisons']}/{len(rows)}", flush=True)


if __name__ == "__main__":
    main()
