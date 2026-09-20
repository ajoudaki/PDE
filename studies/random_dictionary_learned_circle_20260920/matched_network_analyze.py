"""Replay all matched-network attempts and compare their latest two levels.

Scientific replay, checks, and metrics require CUDA float64. This program never
trains. Failed and superseded attempts remain in validation.json. The two small
network budget definitions are compared separately and are never minimized.
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

from benchmark import ROOT, NetworkEngine, save_json, setup
from diverse_cases import CASES_V2
from scaling_dictionary import build, dictionary_metadata


STUDY = Path(__file__).resolve().parent
NAMESPACE = ROOT / "data/generated/random_dictionary_learned_circle_20260920"
CASE_NAMES = ("quadrant_alternating", "two_outliers_alternating")
ORDERS = (1, 3, 5)
METHODS = ("ours", "small_trainable", "small_total")
DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21)}
MODELS = ["full"] + [f"{method}_p{order}" for order in ORDERS for method in METHODS]
WIDTH, SEED, THRESHOLD, GATE, REPLAY = 1024, 20260920, .001, .01, 1e-10
SOURCE_NAMES = {"matched_network_benchmark.py", "benchmark.py", "diverse_benchmark.py",
                "diverse_cases.py", "scaling_dictionary.py", "diverse_dictionary.py",
                "MATCHED_NETWORK_PROTOCOL.md"}


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def number(value):
    try:
        value = float(value)
        return value if math.isfinite(value) else None
    except (ValueError, TypeError):
        return None


def tensor(value, device):
    return torch.as_tensor(np.array(value, copy=True), dtype=torch.float64, device=device)


def owned(path):
    path = Path(path).resolve()
    if not path.is_relative_to(NAMESPACE.resolve()) or not path.name.startswith("matched_network_"):
        raise ValueError(f"Expected this study's matched_network_* generated root: {path}")
    return path


def expected_specs():
    """Independent integer counts, including all redundant frozen columns."""
    result = {"full": dict(method="full", p=None, width=WIDTH,
                           trainable_parameters=WIDTH ** 2 + 3 * WIDTH,
                           model_parameters=WIDTH ** 2 + 3 * WIDTH)}
    for order, (k1, k2) in DIMENSIONS.items():
        train = 3 * WIDTH + k1 * k2
        total = train + WIDTH * (k1 + k2)
        shared = dict(p=order, dictionary_dimensions=[k1, k2], dictionary_vectors=k1 + k2,
                      closure_trainable_parameters=train, closure_model_parameters=total)
        result[f"ours_p{order}"] = dict(**shared, method="ours", width=WIDTH,
                                       trainable_parameters=train, model_parameters=total)
        for match, budget in (("trainable", train), ("total", total)):
            width = 1
            while width * width + 3 * width < budget:
                width += 1
            count = width * width + 3 * width
            result[f"small_{match}_p{order}"] = dict(**shared, method=f"small_{match}",
                width=width, matched_budget=budget, trainable_parameters=count,
                model_parameters=count, excess_parameters=count-budget,
                excess_fraction=count / budget - 1)
    return result


def read_json(path):
    return json.loads(Path(path).read_text())


def configurations(root, specs):
    entries = []
    for path in sorted(root.glob("config_worker*.json")):
        config = read_json(path)
        reasons, source_checks = [], {}
        expected = dict(cases={case: CASES_V2[case] for case in CASE_NAMES}, width=WIDTH,
            network_seed=SEED, orders=list(ORDERS), models=specs, threshold=THRESHOLD,
            dtype="float64", coupling="fixed_prefix_canonical_rescaling", step=.05,
            max_step=2., max_time=10000., max_steps=30000, circle_nodes=2048,
            endpoint_nodes=8192, per_trajectory_limit_seconds=180, training_run=True)
        for key, value in expected.items():
            if config.get(key) != value:
                reasons.append(f"configuration mismatch: {key}")
        level = config.get("level")
        if type(level) is not int or level not in range(4):
            reasons.append("configuration level must be 0,1,2,3")
        else:
            for key, value in (("rtol", 6.25e-5 / 4 ** level), ("atol", 6.25e-7 / 4 ** level)):
                if config.get(key) != value:
                    reasons.append(f"configuration mismatch: {key}")
        worker = config.get("worker")
        case = config.get("case")
        if type(worker) is not int or worker not in (0, 1) or case != CASE_NAMES[worker]:
            reasons.append("worker/case identity mismatch")
        declared = config.get("selected_cells", [])
        expected_order = [f"{case}_{model}" for model in MODELS]
        if not isinstance(declared, list) or not declared or declared != [x for x in expected_order if x in declared]:
            reasons.append("selected cells are missing, duplicated, unknown, or out of protocol order")
        if level in (0, 1) and declared != expected_order:
            reasons.append("base configuration does not declare all ten models")
        if not isinstance(config.get("device"), str) or not config["device"].startswith("cuda"):
            reasons.append("producer did not declare CUDA")
        if not 0 < (number(config.get("worker_limit_seconds")) or 0) <= 600:
            reasons.append("worker reservation outside (0,600]")
        source_hashes = config.get("source_hashes", {})
        required = {str((STUDY / name).relative_to(ROOT)) for name in SOURCE_NAMES}
        if not required.issubset(source_hashes):
            reasons.append("producer hash map omits required sources")
        for name, digest in source_hashes.items():
            source = (ROOT / name).resolve()
            allowed = (source.is_relative_to(ROOT / "code/pde") or
                       (source.parent == STUDY and source.name in SOURCE_NAMES))
            actual = sha256(source) if allowed and source.is_file() else None
            source_checks[name] = dict(declared=digest, current=actual, matches=actual == digest)
            if actual != digest:
                reasons.append(f"source hash mismatch or out-of-scope source: {name}")
        protocol = STUDY / "MATCHED_NETWORK_PROTOCOL.md"
        if config.get("protocol_sha256") != sha256(protocol) or config.get("protocol_path") != str(protocol.relative_to(ROOT)):
            reasons.append("protocol path/hash mismatch")
        entries.append(dict(path=str(path), sha256=sha256(path), config=config,
                            reasons=reasons, source_checks=source_checks))
    return entries


def select_inputs(roots, specs):
    configs = {str(root): configurations(root, specs) for root in roots}
    selected = {}
    for case in CASE_NAMES:
        for model in MODELS:
            key, attempts = f"{case}_{model}", []
            for index, root in enumerate(roots):
                entries = [entry for entry in configs[str(root)]
                           if key in entry["config"].get("selected_cells", [])]
                if index >= 2 and not entries and not (root / key).exists():
                    continue
                entry = entries[0] if len(entries) == 1 else None
                reasons = [] if entry else [f"expected one declaring worker config, found {len(entries)}"]
                config = entry["config"] if entry else {}
                level = config.get("level", index if index < 2 else None)
                if index < 2 and level != index:
                    reasons.append("base root has wrong numerical level")
                attempts.append(dict(directory=str(root / key), config_path=entry["path"] if entry else None,
                    config_sha256=entry["sha256"] if entry else None, level=level,
                    rtol=config.get("rtol"), atol=config.get("atol"), config=config,
                    reasons=reasons + (entry["reasons"] if entry else [])))
            attempts.sort(key=lambda record: record["level"] if type(record["level"]) is int else 99)
            levels = [record["level"] for record in attempts]
            issues = []
            if len(levels) != len(set(levels)) or levels != list(range(len(levels))):
                issues.append("attempted numerical levels are duplicated, missing, or nonconsecutive")
            if len(attempts) > 4:
                issues.append("more than two extra attempts")
            selected[key] = dict(case=case, model=model, attempts=attempts, issues=issues)
    extra_count = sum(len(cell["attempts"]) - 2 for cell in selected.values())
    if extra_count > 12:
        for cell in selected.values():
            cell["issues"].append("suite exceeds twelve extra trajectories")
    return selected, configs


@torch.no_grad()
def predict(states, inputs, snapshot, device):
    """Independent forward replay from stored tensors; no engine prediction."""
    w, c, middle = (tensor(states[key][snapshot], device) for key in ("w", "c", "M"))
    values = []
    bases = [tensor(states[key], device) for key in ("b1", "b2")] if "b1" in states else None
    for batch in tensor(inputs, device).split(256):
        lower = torch.tanh(w @ batch.T)
        upper = middle @ lower if bases is None else bases[1] @ (middle @ (bases[0].T @ lower / len(w)))
        values.append(c @ torch.tanh(upper) / len(c))
    return torch.cat(values)


@torch.no_grad()
def audit(attempt, case, model, spec, initial, dictionary_cache, device):
    directory, config = Path(attempt["directory"]), attempt["config"]
    record = {key: value for key, value in attempt.items() if key != "config"}
    record["reasons"] = list(attempt["reasons"])
    record.update(status="missing_summary", fitted=False, replay_valid=False, files={})
    summary_path, arrays_path = directory / "summary.json", directory / "arrays.npz"
    for path in (summary_path, arrays_path, directory / "exception.json"):
        if path.exists():
            record["files"][str(path)] = sha256(path)
    try:
        summary = read_json(summary_path) if summary_path.exists() else {}
        record["summary"] = summary
        record.update({key: summary.get(key) for key in ("loss", "time", "seconds", "retained_bytes", "rms_hidden1", "rms_hidden2")})
        record["status"] = summary.get("status", "missing_summary")
        if not summary_path.exists():
            record["reasons"].append("missing summary.json")
        if not arrays_path.exists():
            record["reasons"].append("missing arrays.npz")
            return record, None
        with np.load(arrays_path, allow_pickle=False) as saved:
            for key in saved.files:
                array = saved[key]
                if array.dtype.kind not in "fiu" or (key != "labels" and array.dtype != np.float64):
                    record["reasons"].append(f"unexpected saved dtype: {key}={array.dtype}")
                if not bool(torch.isfinite(tensor(array, device)).all()):
                    record["reasons"].append(f"nonfinite saved array: {key}")
            states = {key: saved[key][[0, -1]] for key in ("w", "c", "M")}
            states.update({key: saved[key] for key in ("b1", "b2", "g", "D", "p1", "p2") if key in saved})
            width = spec["width"]
            k1, k2 = DIMENSIONS[spec["p"]] if spec["p"] else (None, None)
            expected_middle = (k2, k1) if spec["method"] == "ours" else (width, width)
            if states["w"].shape != (2, width, 2) or states["c"].shape != (2, width) or states["M"].shape != (2, *expected_middle):
                raise ValueError("saved trainable state shape does not match declared model")
            snapshots = saved["snapshot_times"]
            if any(len(saved[key]) != len(snapshots) for key in ("w", "c", "M", "circle_predictions")):
                raise ValueError("state/prediction snapshot counts disagree")
            if saved["endpoint_prediction"].shape != (8192,) or saved["circle_predictions"].shape != (len(snapshots), 2048):
                raise ValueError("saved predictions have unexpected grid/snapshot shape")
            is_closure = spec["method"] == "ours"
            if is_closure != ("b1" in states) or is_closure != ("b2" in states):
                raise ValueError("model type and frozen dictionary presence disagree")
            trainable = sum(states[key][0].size for key in ("w", "c", "M"))
            total = trainable + sum(states[key].size for key in ("b1", "b2") if key in states)
            record.update(actual_trainable_parameters=trainable, actual_model_parameters=total)
            for key, value in (("actual_trainable_parameters", trainable), ("actual_model_parameters", total),
                               ("model", model), ("model_specification", spec)):
                if summary.get(key) != value:
                    record["reasons"].append(f"summary model/count mismatch: {key}")
            if trainable != spec["trainable_parameters"] or total != spec["model_parameters"]:
                record["reasons"].append("actual scalar counts do not match independent budget")
            checks = {}

            def difference(name, observed, expected):
                observed = observed if isinstance(observed, torch.Tensor) else tensor(observed, device)
                expected = expected if isinstance(expected, torch.Tensor) else tensor(expected, device)
                value = number((observed - expected).abs().max()) if observed.shape == expected.shape else None
                checks[name] = value
                if value is None or value > REPLAY:
                    record["reasons"].append(f"failed {name}")

            if is_closure:
                if spec["p"] not in dictionary_cache:
                    engine, state = build(initial, spec["p"], "ours")
                    metadata = dictionary_metadata(initial, spec["p"], "ours", bases=(engine.b1, engine.b2))
                    dictionary_cache[spec["p"]] = (engine, state, metadata)
                engine, expected, metadata = dictionary_cache[spec["p"]]
                for name in ("b1", "b2", "g", "D", "p1", "p2"):
                    difference("initialized_" + name + "_error", states[name], getattr(engine, name))
                record["recomputed_dictionary_metadata"] = metadata
                metadata_path = directory.parent / f"dictionary_worker{config.get('worker')}_{model}.json"
                if metadata_path.exists():
                    record["files"][str(metadata_path)] = sha256(metadata_path)
                    recorded_metadata = read_json(metadata_path)
                    record["recorded_dictionary_metadata"] = recorded_metadata
                    for key in ("order", "method", "width", "nominal_dimensions", "ridge", "all_finite"):
                        if recorded_metadata.get(key) != metadata[key]:
                            record["reasons"].append(f"dictionary metadata identity mismatch: {key}")
                    populations = recorded_metadata.get("populations", [])
                    if len(populations) != 2 or any(
                            number(population.get("ridge_condition")) is None or
                            number(population.get("triangular_solve_residual")) is None or
                            population["ridge_condition"] > 1e10 or
                            population["triangular_solve_residual"] > 1e-8
                            for population in populations):
                        record["reasons"].append("recorded dictionary condition/residual gate failed")
                else:
                    record["reasons"].append("missing dictionary metadata")
                for population in metadata["populations"]:
                    if population["ridge_condition"] > 1e10 or population["triangular_solve_residual"] > 1e-8:
                        record["reasons"].append("recomputed dictionary condition/residual gate failed")
                for name in ("w", "c", "M"):
                    difference("initial_" + name + "_error", states[name][0], getattr(expected, name))
                expected_retained_bytes = engine.retained_bytes(expected)
            else:
                expected = dict(w=initial.w[:width], c=initial.c[:width] * (WIDTH / width),
                                M=initial.M[:width, :width] * math.sqrt(WIDTH / width))
                for name in ("w", "c", "M"):
                    difference("initial_" + name + "_prefix_rescaling_error", states[name][0], expected[name])
                expected_retained_bytes = 2 * 8 * trainable
            record["recomputed_retained_bytes"] = expected_retained_bytes
            if summary.get("retained_bytes") != expected_retained_bytes:
                record["reasons"].append("engine retained-byte count mismatch")
            for prefix, nodes in (("endpoint", 8192), ("circle", 2048)):
                angles = torch.arange(nodes, device=device, dtype=torch.float64) * (2 * math.pi / nodes)
                grid = torch.stack((angles.cos(), angles.sin()), 1)
                difference(prefix + "_angles_error", saved[prefix + "_angles"], angles)
                difference(prefix + "_inputs_error", saved[prefix + "_inputs"], grid)
            train_angles = tensor(CASES_V2[case]["angles_degrees"], device) * (math.pi / 180)
            difference("training_inputs_error", saved["training_inputs"], torch.stack((train_angles.cos(), train_angles.sin()), 1))
            difference("training_labels_error", saved["labels"], CASES_V2[case]["labels"])
            endpoint = tensor(saved["endpoint_prediction"], device)
            difference("endpoint_replay_error", endpoint, predict(states, saved["endpoint_inputs"], -1, device))
            for index, label in ((0, "initial"), (-1, "final")):
                difference(label + "_circle_replay_error", saved["circle_predictions"][index], predict(states, saved["circle_inputs"], index, device))
            labels = tensor(saved["labels"], device)
            initial_loss = (predict(states, saved["training_inputs"], 0, device) - labels).square().mean()
            final_loss = (predict(states, saved["training_inputs"], -1, device) - labels).square().mean()
            hidden = []
            for index in (0, -1):
                lower = torch.tanh(tensor(states["w"][index], device) @ tensor(saved["training_inputs"], device).T)
                middle = tensor(states["M"][index], device)
                upper = torch.tanh(tensor(states["b2"], device) @ (middle @ (tensor(states["b1"], device).T @ lower / width))) if is_closure else torch.tanh(middle @ lower)
                hidden.append((lower, upper))
            for index in range(2):
                displacement = (hidden[1][index] - hidden[0][index]).square().mean().sqrt()
                difference(f"hidden{index + 1}_motion_error", displacement, summary.get(f"rms_hidden{index + 1}", float("nan")))
            losses, times = tensor(saved["losses"], device), tensor(saved["times"], device)
            difference("initial_summary_loss_error", initial_loss, summary.get("initial_loss", float("nan")))
            difference("final_summary_loss_error", final_loss, summary.get("loss", float("nan")))
            difference("initial_trace_loss_error", initial_loss, losses[0])
            difference("final_trace_loss_error", final_loss, losses[-1])
            trace_valid = (times.ndim == 1 and losses.shape == times.shape and len(times) > 0 and
                bool(times[0] == 0) and bool((times[1:] > times[:-1]).all()) and
                bool((losses[1:] <= losses[:-1] * (1 + 1e-8) + 1e-12).all()) and
                abs(float(times[-1]) - float(summary["time"])) <= REPLAY and
                snapshots[0] == 0 and abs(snapshots[-1] - float(times[-1])) <= REPLAY and
                bool((tensor(snapshots[1:], device) > tensor(snapshots[:-1], device)).all()))
            accepted, errors = tensor(saved["accepted_steps"], device), tensor(saved["local_error_ratios"], device)
            step_valid = (accepted.shape == times[1:].shape == errors.shape and
                len(accepted) == summary["steps"] and len(accepted) <= 30000 and
                bool((accepted > 0).all()) and bool((accepted <= 2 + REPLAY).all()) and
                bool((errors >= 0).all()) and bool((errors <= 1).all()) and
                (bool((accepted - times.diff()).abs().max() <= REPLAY) if len(accepted) else len(times) == 1))
            trace_valid = trace_valid and step_valid
            if summary.get("loss_increases_above_1e-10") != int((losses.diff() > 1e-10).sum()):
                record["reasons"].append("summary loss-increase diagnostic disagrees with trace")
            if not trace_valid:
                record["reasons"].append("invalid accepted loss/time/step/error trace")
            first_crossing = bool(trace_valid and final_loss <= THRESHOLD * (1 + 1e-8) and
                                  (losses[:-1] > THRESHOLD).all())
            for name in ("rtol", "atol"):
                if summary.get(name) != config.get(name):
                    record["reasons"].append(f"summary/config {name} mismatch")
            record.update(checks=checks, initial_recomputed_loss=number(initial_loss),
                recomputed_loss=number(final_loss), first_crossing_verified=first_crossing,
                replay_valid=not record["reasons"], fitted=summary.get("status") == "fitted" and first_crossing)
            if not record["fitted"]:
                record["reasons"].append(f"not fitted at first detected crossing: {summary.get('status')}")
            return record, dict(prediction=endpoint, angles=saved["endpoint_angles"], inputs=saved["endpoint_inputs"])
    except (OSError, ValueError, KeyError, TypeError, IndexError, RuntimeError) as exc:
        record["reasons"].append(f"audit failure: {type(exc).__name__}: {exc}")
        return record, None


def aligned(first, second):
    return first is not None and second is not None and np.array_equal(first["angles"], second["angles"]) and np.array_equal(first["inputs"], second["inputs"])


def endpoint_valid(record):
    return record["replay_valid"] and record["fitted"]


def error_metrics(error):
    return dict(rms=number(error.square().mean().sqrt()), l1=number(error.abs().mean()),
                mse=number(error.square().mean()), max_abs=number(error.abs().max()))


def csv_write(path, rows):
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: json.dumps(value) if isinstance(value, (dict, list)) else value for key, value in row.items()} for row in rows)


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, default=NAMESPACE / "matched_network_primary01")
    parser.add_argument("--refined", type=Path, default=NAMESPACE / "matched_network_refined01")
    parser.add_argument("--extra", action="append", type=Path, default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cuda:1")
    args = parser.parse_args()
    roots = [owned(root) for root in (args.primary, args.refined, *args.extra)]
    if len(roots) != len(set(roots)):
        raise ValueError("input roots must be distinct")
    out = owned(args.out)
    if out.exists() or out in roots:
        raise FileExistsError("analysis output must be a fresh root")
    device = setup(args.device)
    specs = expected_specs()
    selected, configs = select_inputs(roots, specs)
    out.mkdir(parents=True, exist_ok=False)
    initial = NetworkEngine(2, WIDTH, SEED, device=device, dtype=torch.float64, block_size=256).initial_state()
    dictionary_cache, validation, selections, rows, pointwise = {}, {}, {}, [], {}
    for case in CASE_NAMES:
        audited = {}
        for model in MODELS:
            key = f"{case}_{model}"
            cell = selected[key]
            attempts = [audit(attempt, case, model, specs[model], initial, dictionary_cache, device) for attempt in cell["attempts"]]
            branch_checks = []
            for index in range(2, len(attempts)):
                left, right = attempts[index - 2:index]
                difference = number((left[1]["prediction"] - right[1]["prediction"]).abs().max()) if aligned(left[1], right[1]) else None
                eligible = endpoint_valid(left[0]) and endpoint_valid(right[0]) and difference is not None and difference > GATE
                branch_checks.append(dict(level=attempts[index][0]["level"], eligible=eligible, prior_refinement_endpoint_max=difference))
                if not eligible:
                    cell["issues"].append(f"extra level {attempts[index][0]['level']} did not satisfy the predeclared numerical branch")
            primary, refined = attempts[-2:]
            refinement = number((primary[1]["prediction"] - refined[1]["prediction"]).abs().max()) if aligned(primary[1], refined[1]) else None
            reasons = list(cell["issues"])
            for level, attempt in (("primary", primary), ("refined", refined)):
                reasons.extend(level + ": " + reason for reason in attempt[0]["reasons"])
            if refinement is None or refinement > GATE:
                reasons.append("selected endpoint refinement discrepancy exceeds 0.01 or is unavailable")
            valid = not reasons and all(endpoint_valid(attempt[0]) for attempt in (primary, refined))
            validation[key] = dict(case=case, model=model, valid=valid, reasons=reasons,
                refinement_endpoint_max=refinement, attempts=[attempt[0] for attempt in attempts],
                branch_checks=branch_checks, primary=primary[0], refined=refined[0])
            selections[key] = {name: validation[key][name] for name in ("case", "model", "valid", "reasons", "refinement_endpoint_max", "primary", "refined")}
            audited[model] = dict(primary=primary, refined=refined)
            for level, attempt in (("primary", primary), ("refined", refined)):
                if attempt[1] is not None:
                    pointwise[f"{key}_{level}_prediction"] = attempt[1]["prediction"].cpu().numpy()
                    pointwise[f"{case}_angles"] = attempt[1]["angles"]
        full = validation[f"{case}_full"]
        for model in MODELS[1:]:
            key, spec = f"{case}_{model}", specs[model]
            check = validation[key]
            k1, k2 = DIMENSIONS[spec["p"]]
            row = dict(case=case, model=model, method=spec["method"], order=spec["p"], width=spec["width"],
                k1=k1, k2=k2, dictionary_vectors=k1+k2, trainable_parameters=spec["trainable_parameters"],
                model_parameters=spec["model_parameters"], matched_budget=spec.get("matched_budget"),
                valid=check["valid"] and full["valid"], reasons=check["reasons"] + ["full: " + reason for reason in full["reasons"]],
                refinement_endpoint_max=check["refinement_endpoint_max"], full_refinement_endpoint_max=full["refinement_endpoint_max"])
            for level in ("primary", "refined"):
                record, arrays = audited[model][level]
                reference, reference_arrays = audited["full"][level]
                row.update({level + "_" + field: record.get(field) for field in
                    ("directory", "config_path", "level", "rtol", "atol", "status", "loss", "time", "seconds", "retained_bytes", "rms_hidden1", "rms_hidden2")})
                row.update({level + "_full_" + field: reference.get(field) for field in
                    ("directory", "level", "rtol", "atol", "status", "loss", "time")})
                row[level + "_eligible"] = endpoint_valid(record) and endpoint_valid(reference)
                for field in ("rms", "l1", "mse", "max_abs"):
                    for label in ("", "terminal_", "grid4096_", "grid_"):
                        row[level + "_" + label + field + ("_change" if label == "grid_" else "")] = None
                if aligned(arrays, reference_arrays):
                    error = arrays["prediction"] - reference_arrays["prediction"]
                    measured, nested = error_metrics(error), error_metrics(error[::2])
                    for field, value in measured.items():
                        row[level + "_terminal_" + field] = value
                        row[level + "_" + field] = value if row[level + "_eligible"] else None
                        row[level + "_grid4096_" + field] = nested[field]
                        row[level + "_grid_" + field + "_change"] = number(torch.tensor(value, device=device, dtype=torch.float64).sub(nested[field]).abs()) if value is not None and nested[field] is not None else None
                        if value is None:
                            row["valid"] = False
                            row["reasons"].append(level + " nonfinite error metric")
                    pointwise[f"{key}_{level}_signed_error"] = error.cpu().numpy()
                    pointwise[f"{key}_{level}_absolute_error"] = error.abs().cpu().numpy()
                else:
                    row["valid"] = False
                    row["reasons"].append(level + " model/full grids missing or different")
            rows.append(row)
        print(f"Audited {case}: {sum(row['valid'] for row in rows if row['case'] == case)}/9 valid model rows", flush=True)
        del audited
    lookup = {(row["case"], row["model"]): row for row in rows}
    comparisons = []
    for case in CASE_NAMES:
        for order in ORDERS:
            ours = lookup[case, f"ours_p{order}"]
            for match in ("trainable", "total"):
                baseline = lookup[case, f"small_{match}_p{order}"]
                comparison = dict(case=case, order=order, match=match, baseline_model=baseline["model"],
                    baseline_width=baseline["width"], valid=ours["valid"] and baseline["valid"],
                    reasons=["ours: " + reason for reason in ours["reasons"]] + ["small: " + reason for reason in baseline["reasons"]])
                for level in ("primary", "refined"):
                    ours_error, small_error = ours[level + "_rms"], baseline[level + "_rms"]
                    comparison[level + "_ours_rms"] = ours_error
                    comparison[level + "_baseline_rms"] = small_error
                    comparison[level + "_baseline_over_ours_rms"] = number(torch.tensor(small_error, device=device, dtype=torch.float64) / ours_error) if ours_error is not None and small_error is not None and ours_error > 0 else None
                    comparison[level + "_winner"] = ("ours" if ours_error < small_error else "small" if small_error < ours_error else "tie") if ours_error is not None and small_error is not None else "unavailable"
                same = comparison["primary_winner"] == comparison["refined_winner"]
                comparison["verdict"] = comparison["primary_winner"] if comparison["valid"] and same and comparison["primary_winner"] in ("ours", "small") else "inconclusive"
                comparisons.append(comparison)
    definitions = ("Each predictor is measured at its own first detected training-MSE 0.001 crossing, localized on an accepted Heun parameter chord. "
        "RMS is sqrt(mean((predictor-full)^2)) on 8192 uniform circle angles; L1 is mean absolute discrepancy and max_abs is a sampled maximum. "
        "Primary/refined denote each predictor's latest two attempted levels, independently selected, against the corresponding selected full reference; actual tolerances are recorded. "
        "Validity requires fitted, replayed, source/configuration/initialization/count checked endpoints and endpoint refinement maximum <=0.01 for both model and full reference. "
        "Grid4096 diagnostics use every second 8192 point. Invalid or unfitted terminal metrics remain diagnostics and do not support winners. "
        "Both parameter matches remain separate. All scientific calculations use CUDA float64. This finite-realization agreement comparison establishes neither unseen-label risk nor a capacity lower bound, universal superiority, or an asymptotic rate.")
    summary = dict(definitions=definitions, cases=list(CASE_NAMES), orders=list(ORDERS), models=specs,
        width=WIDTH, network_seed=SEED, threshold=THRESHOLD, refinement_gate=GATE,
        declared_model_rows=len(rows), valid_model_rows=sum(row["valid"] for row in rows),
        declared_comparisons=len(comparisons), valid_comparisons=sum(row["valid"] for row in comparisons),
        verdict_counts={verdict: sum(row["verdict"] == verdict for row in comparisons) for verdict in ("ours", "small", "inconclusive")},
        comparisons=comparisons, attempted_trajectories=sum(len(cell["attempts"]) for cell in validation.values()),
        failed_attempts=[dict(cell=key, directory=attempt["directory"], level=attempt["level"], status=attempt["status"], reasons=attempt["reasons"]) for key, cell in validation.items() for attempt in cell["attempts"] if not endpoint_valid(attempt)],
        exclusions={f"{row['case']}_{row['model']}": row["reasons"] for row in rows if not row["valid"]})
    save_json(out / "metrics.json", rows)
    csv_write(out / "metrics.csv", rows)
    csv_write(out / "comparisons.csv", comparisons)
    save_json(out / "validation.json", validation)
    save_json(out / "summary.json", summary)
    save_json(out / "selected_levels.json", dict(cases={case: CASES_V2[case] for case in CASE_NAMES}, cells=selections))
    np.savez(out / "pointwise_circle_errors.npz", **pointwise)
    fmt = lambda value: "—" if value is None else f"{value:.6g}"
    report = "# Matched-network endpoint comparison\n\n" + definitions + "\n\n"
    report += f"Valid model rows: {summary['valid_model_rows']}/18. Valid pairwise comparisons: {summary['valid_comparisons']}/12.\n\n"
    report += "| Case | Model | Width | Trained scalars | Total scalars | RMS primary / refined | L1 primary / refined | Max primary / refined | Valid |\n|---|---|---:|---:|---:|---:|---:|---:|---|\n"
    for row in rows:
        cells = [f"{fmt(row['primary_' + field])} / {fmt(row['refined_' + field])}" for field in ("rms", "l1", "max_abs")]
        report += f"| {row['case']} | {row['model']} | {row['width']} | {row['trainable_parameters']} | {row['model_parameters']} | " + " | ".join(cells) + f" | {row['valid']} |\n"
    report += "\n| Case | Order | Match | Small width | Small/ours RMS primary / refined | Primary winner | Refined winner | Verdict |\n|---|---:|---|---:|---:|---|---|---|\n"
    for row in comparisons:
        report += f"| {row['case']} | {row['order']} | {row['match']} | {row['baseline_width']} | {fmt(row['primary_baseline_over_ours_rms'])} / {fmt(row['refined_baseline_over_ours_rms'])} | {row['primary_winner']} | {row['refined_winner']} | {row['verdict']} |\n"
    report += "\n## Unresolved model rows\n\n" + ("\n".join(f"- {key}: {'; '.join(reasons)}" for key, reasons in summary["exclusions"].items()) or "None.")
    report += "\n\nEvery attempted trajectory, including superseded failures, is audited in validation.json. Selected paths and tolerances are in selected_levels.json. Raw configurations, source checks, and input/output hashes are in provenance.json.\n"
    (out / "tables.md").write_text(report)
    provenance = dict(command=sys.argv, device=device, dtype="float64", gpu=torch.cuda.get_device_name(device),
        torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
        analysis_sha256=sha256(__file__), producer_configs=configs, roots=[str(root) for root in roots],
        protocol_sha256=sha256(STUDY / "MATCHED_NETWORK_PROTOCOL.md"), replay_tolerance=REPLAY,
        refinement_endpoint_max_limit=GATE, selection_policy="latest two attempted numerical levels per predictor, preserving failures",
        input_hashes={path: digest for cell in validation.values() for attempt in cell["attempts"] for path, digest in attempt["files"].items()},
        helper_hashes={str(STUDY / name): sha256(STUDY / name) for name in ("benchmark.py", "diverse_cases.py", "scaling_dictionary.py", "diverse_dictionary.py")},
        output_hashes={str(path): sha256(path) for path in sorted(out.iterdir()) if path.is_file()})
    save_json(out / "provenance.json", provenance)
    torch.cuda.synchronize(device)
    torch.cuda.empty_cache()
    print(json.dumps(dict(output=str(out), valid_model_rows=summary["valid_model_rows"], valid_comparisons=summary["valid_comparisons"], verdict_counts=summary["verdict_counts"])), flush=True)


if __name__ == "__main__":
    main()
