"""Analyze saved input-index hidden Grams; never run a scientific trajectory.

All destinations are confined to the requested fresh GRAM run directory. Original
scalar observations are read only for an independent replay-consistency check.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys
import time

# This postprocessor shares the host with bounded scientific workers.
THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
for _key in THREAD_KEYS:
    os.environ[_key] = "1"
sys.dont_write_bytecode = True
import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/wide_network_closure_comparison"
HISTORICAL = GENERATED / "WIDE_GPU_20260914_202109Z"
PLAN = STUDY / "GRAM_20260914_PLAN.md"
CASES, WIDTHS, SEEDS = ("axis", "arcs"), (2048, 8192), (11, 29, 47)
FIELDS = ("loss", "raw_rms", "motion_rms", "predictions", "data_predictions",
          "mean_prediction", "second_moments", "initial_second_moments", "cross_moments")
SAFE_NORM = 1e-12
CONTROL_LIMIT = .002


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def atomic_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def csv_write(path, rows):
    rows = [{key: value for key, value in row.items()
             if not isinstance(value, (dict, list, tuple))} for row in rows]
    fields = list(dict.fromkeys(key for row in rows for key in row))
    if not fields:
        return
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def closure_configurations():
    return [dict(id=f"{case}_N{order}{suffix}", case=case, order=order,
                 initialization_nodes=2048 if suffix == "_refined" else 1024,
                 population_nodes=1024 if suffix == "_refined" else 512,
                 step="1/400" if suffix == "_halfstep" else "1/200",
                 refined=suffix == "_refined", kind=("quadrature_control" if suffix == "_refined"
                 else "time_control" if suffix == "_halfstep" else "primary"))
            for case in CASES for order, suffix in
            ((1, ""), (3, ""), (5, ""), (3, "_refined"), (3, "_halfstep"))]


def replay_check(directory, historical, family, config, arrays, record):
    """Read original data without invoking or replacing historical analysis."""
    name = config.get("name", config.get("id"))
    result = dict(family=family, name=name, case=config["case"],
                  tolerance=2e-6 if config.get("dtype") == "float32" else 1e-10)
    previous = historical / family / name
    if family == "closure" and name.endswith("_halfstep"):
        result.update(status="new_time_control_no_historical_counterpart", consistent=None)
        return result
    if not (previous / "observations.npz").exists():
        result.update(status="missing_historical_observations", consistent=False)
        return result
    old_record_path = previous / "record.json"
    old_record = read_json(old_record_path)
    old_hash = digest(previous / "observations.npz")
    if old_hash != old_record.get("observations_sha256"):
        raise ValueError(f"{name}: historical observation checksum mismatch")
    with np.load(previous / "observations.npz", allow_pickle=False) as archive:
        if not np.array_equal(archive["times"], arrays["times"]):
            raise ValueError(f"{name}: historical replay time grid mismatch")
        errors = {}
        for key in archive.files:
            if key not in arrays:
                raise ValueError(f"{name}: missing historical observable {key}")
            if archive[key].shape != arrays[key].shape:
                raise ValueError(f"{name}: historical shape mismatch for {key}")
            errors[key] = float(np.max(np.abs(archive[key] - arrays[key])))
    worst = max(errors.values())
    closure_replay = record.get("replay_check", {})
    supplied = record.get("replay_maximum_differences", closure_replay.get("per_field_errors"))
    supplied_consistent = record.get("replay_consistent")
    if supplied_consistent is None and closure_replay.get("status") in ("passed", "failed"):
        supplied_consistent = closure_replay["status"] == "passed"
    result.update(status="compared", historical_observations_sha256=old_hash,
                  historical_record_sha256=digest(old_record_path),
                  maximum_absolute_differences=errors, maximum_absolute_difference=worst,
                  consistent=worst <= result["tolerance"],
                  runner_consistent=supplied_consistent,
                  runner_flag_matches=(supplied_consistent == (worst <= result["tolerance"]))
                  if supplied_consistent is not None else None,
                  runner_errors_match=all(key in errors and errors[key] == value
                      for key, value in supplied.items()) if isinstance(supplied, dict) else None)
    return result


def load_run(base, historical, family, config, inputs, input_hash):
    name = config.get("name", config.get("id"))
    directory = base / family / name
    status = dict(family=family, name=name, configuration=config)
    record_path = directory / "record.json"
    if not record_path.exists():
        return None, dict(status, status="unstarted_or_missing")
    record = read_json(record_path)
    status.update(status=record.get("status", "missing_status"),
                  record_sha256=digest(record_path), error=record.get("error"))
    if status["status"] != "complete":
        return None, status
    count = record.get("gram_completed_observations", record.get("completed_observations"))
    if not record.get("gram_sha256") or count != len(inputs["times"]):
        return None, dict(status, status="awaiting_final_gram_record", gram_count=count)
    recorded_config = record if family == "network" else record.get("configuration", record)
    for key in (("case", "width", "seed", "dtype", "step", "kind") if family == "network" else
                ("case", "order", "initialization_nodes", "population_nodes", "step", "refined", "kind")):
        if recorded_config.get(key) != config[key]:
            raise ValueError(f"{name}: configuration mismatch at {key}")
    if record.get("inputs_sha256", record.get("inputs_npz_sha256")) != input_hash:
        raise ValueError(f"{name}: input checksum mismatch")
    hashes = {}
    for filename, field in (("observations.npz", "observations_sha256"), ("gram.npy", "gram_sha256")):
        hashes[field] = digest(directory / filename)
        if hashes[field] != record.get(field):
            raise ValueError(f"{name}: {filename} checksum mismatch")
    plan_hash = record.get("gram_plan_sha256", record.get("plan_sha256"))
    if plan_hash is not None and plan_hash != digest(PLAN):
        raise ValueError(f"{name}: Gram plan checksum mismatch")
    source_validation = {}
    sources = record.get("source_hashes", {}).copy()
    if family == "network":
        sources.update({str((STUDY / "WIDE_GPU_20260914_NETWORK.py").relative_to(ROOT)): record["source_sha256"],
                        str((STUDY / "GRAM_20260914_NETWORK.py").relative_to(ROOT)): record["gram_source_sha256"]})
    for relative, expected_hash in sources.items():
        source_path = (ROOT / relative).resolve()
        if not (source_path.is_relative_to(STUDY) or source_path.is_relative_to(ROOT / "code")):
            raise ValueError(f"{name}: provenance source outside assigned source scope")
        source_validation[relative] = digest(source_path) == expected_hash
    if not all(source_validation.values()):
        raise ValueError(f"{name}: recorded source checksum differs from current source")
    with np.load(directory / "observations.npz", allow_pickle=False) as archive:
        arrays = {key: archive[key].copy() for key in archive.files}
    times = inputs["times"]
    if not np.array_equal(times, arrays["times"]):
        raise ValueError(f"{name}: observation time grid mismatch")
    case, m = config["case"], len(inputs[config["case"] + "_labels"])
    shapes = {"times": times.shape, "loss": times.shape, "mean_prediction": times.shape,
              "predictions": (len(times), 128), "data_predictions": (len(times), m)}
    shapes.update({key: (len(times), 2) for key in FIELDS if key not in shapes})
    for key, shape in shapes.items():
        if key not in arrays or arrays[key].shape != shape or not np.isfinite(arrays[key]).all():
            raise ValueError(f"{name}: invalid scalar observable {key}")
    for key, array in arrays.items():
        if not np.isfinite(array).all():
            raise ValueError(f"{name}: nonfinite additional scalar {key}")
    gram = np.load(directory / "gram.npy", mmap_mode="r", allow_pickle=False)
    expected = (len(times), 2, m + 128, m + 128)
    if gram.shape != expected or gram.dtype != np.float64:
        raise ValueError(f"{name}: invalid Gram shape or accumulation dtype")
    if record.get("gram_shape") is not None and list(gram.shape) != record["gram_shape"]:
        raise ValueError(f"{name}: recorded Gram shape differs from saved matrix")
    tolerance = 2e-6 if config.get("dtype") == "float32" else 2e-11
    q, y = inputs[case + "_probabilities"], inputs[case + "_labels"]
    validation = dict(finite=True, maximum_asymmetry=0., maximum_absolute_entry=0.,
                      maximum_diagonal_rms_squared_error=0.,
                      maximum_diagonal_second_moment_error=0., tolerance=tolerance)
    for start in range(0, len(times), 16):
        block = gram[start:start + 16]
        if not np.isfinite(block).all():
            raise ValueError(f"{name}: nonfinite saved Gram")
        diagonal = np.diagonal(block[:, :, :m, :m], axis1=2, axis2=3) @ q
        for field, error in (
            ("maximum_asymmetry", float(np.max(np.abs(block - block.transpose(0, 1, 3, 2))))),
            ("maximum_absolute_entry", float(np.max(np.abs(block)))),
            ("maximum_diagonal_rms_squared_error", float(np.max(np.abs(diagonal - arrays["raw_rms"][start:start + 16] ** 2)))),
            ("maximum_diagonal_second_moment_error", float(np.max(np.abs(diagonal - arrays["second_moments"][start:start + 16]))))):
            validation[field] = max(validation[field], error)
    scalar_identities = dict(
        loss=float(np.max(np.abs(arrays["loss"] - np.sum((arrays["data_predictions"] - y) ** 2 * q, axis=1)))),
        mean_prediction=float(np.max(np.abs(arrays["mean_prediction"] - arrays["data_predictions"] @ q))),
        second_moments=float(np.max(np.abs(arrays["second_moments"] - arrays["raw_rms"] ** 2))),
        motion_second_moments=float(np.max(np.abs(arrays["motion_rms"] ** 2 -
            (arrays["second_moments"] + arrays["initial_second_moments"] - 2 * arrays["cross_moments"])))),
        fixed_initial_moments=float(np.max(np.abs(arrays["initial_second_moments"] - arrays["initial_second_moments"][0]))),
        zero_initial_motion=float(np.max(np.abs(arrays["motion_rms"][0]))))
    validation["scalar_identity_errors"] = scalar_identities
    validation["eigenvalues"] = []
    for instant in (0., 1., 5., 40.):
        matches = np.flatnonzero(times == instant)
        if len(matches) != 1:
            raise ValueError(f"{name}: missing exact eigenvalue inspection time {instant}")
        for layer in range(2):
            matrix = np.asarray(gram[matches[0], layer])
            eigenvalues = np.linalg.eigvalsh((matrix + matrix.T) / 2)
            # Conservative backward-roundoff scale for the float64 Gram/eigensolve.
            roundoff = 100 * np.finfo(np.float64).eps * matrix.shape[0] * max(1., float(np.max(np.abs(eigenvalues))))
            validation["eigenvalues"].append(dict(time=instant, layer=layer + 1,
                minimum=float(eigenvalues[0]), maximum=float(eigenvalues[-1]),
                roundoff_tolerance=roundoff, passed=bool(eigenvalues[0] >= -roundoff)))
    validation["passed"] = bool(validation["maximum_asymmetry"] <= tolerance
        and validation["maximum_absolute_entry"] <= 1 + tolerance
        and validation["maximum_diagonal_rms_squared_error"] <= tolerance
        and validation["maximum_diagonal_second_moment_error"] <= tolerance
        and max(scalar_identities.values()) <= tolerance
        and all(row["passed"] for row in validation["eigenvalues"]))
    replay = replay_check(directory, historical, family, config, arrays, record)
    status.update(**hashes, gram_shape=list(gram.shape), completed_observations=count,
                  wall_seconds=record.get("wall_seconds"), cpu_seconds=record.get("cpu_seconds"),
                  gram_validation=validation, replay=replay,
                  initial_float64_block_hashes=record.get("initial_float64_block_hashes"),
                  source_hash_validation=source_validation,
                  source_hashes=record.get("source_hashes"),
                  gram_source_sha256=record.get("gram_source_sha256", record.get("source_sha256")))
    return dict(name=name, family=family, config=config, gram=gram, arrays=arrays, record=record), status


def weighted_norm(array, q):
    return np.sqrt(np.maximum(0., np.einsum("tab,a,b->t", array * array, q, q, optimize=True)))


def integral(values, times):
    return float(np.sum((values[1:] + values[:-1]) * np.diff(times) / 2))


def summarize(rms, entry, norm, times, keep_curves=False):
    valid = norm > SAFE_NORM
    relative = np.full(len(times), np.nan)
    relative[valid] = rms[valid] / norm[valid]
    segment = valid[:-1] & valid[1:]
    valid_duration = float(np.sum(np.diff(times)[segment]))
    relative_integral = float(np.sum(((relative[1:] + relative[:-1]) * np.diff(times) / 2)[segment]))
    duration = float(times[-1] - times[0])
    worst, entry_worst = int(np.argmax(rms)), int(np.argmax(entry))
    result = dict(primary_rms_max=float(rms[worst]), primary_rms_max_time=float(times[worst]),
        rms_initial=float(rms[0]), rms_terminal=float(rms[-1]),
        rms_time_integral=integral(rms, times), rms_time_average=integral(rms, times) / duration,
        maximum_entry_error=float(entry[entry_worst]), maximum_entry_error_time=float(times[entry_worst]),
        entry_error_initial=float(entry[0]), entry_error_terminal=float(entry[-1]),
        entry_error_time_integral=integral(entry, times), entry_error_time_average=integral(entry, times) / duration,
        reference_rms_max=float(np.max(norm)), reference_rms_initial=float(norm[0]),
        reference_rms_terminal=float(norm[-1]), reference_rms_time_integral=integral(norm, times),
        relative_rms_max=float(np.max(relative[valid])) if valid.any() else None,
        relative_rms_initial=float(relative[0]) if valid[0] else None,
        relative_rms_terminal=float(relative[-1]) if valid[-1] else None,
        relative_rms_valid_count=int(valid.sum()), relative_rms_omitted_count=int((~valid).sum()),
        relative_rms_time_integral=relative_integral if valid_duration else None,
        relative_rms_time_average=relative_integral / valid_duration if valid_duration else None,
        relative_rms_integrated_duration=valid_duration, relative_reference_norm_floor=SAFE_NORM)
    if keep_curves:
        result.update(rms_curve=rms.tolist(), entry_max_curve=entry.tolist(), reference_rms_curve=norm.tolist(),
                      relative_rms_curve=[float(value) if np.isfinite(value) else None for value in relative])
    return result


def comparisons(left, reference, times, probabilities, metadata, keep_curves=False):
    """Compare full Grams and initial-subtracted Grams with the right-hand norm."""
    rows, m = [], len(probabilities)
    for panel, selected, q in (("data", slice(0, m), probabilities),
                               ("circle", slice(m, m + 128), np.full(128, 1 / 128))):
        for layer in range(2):
            a = np.asarray(left[:, layer, selected, selected])
            b = np.asarray(reference[:, layer, selected, selected])
            for observable in ("G", "DeltaG"):
                aa, bb = (a, b) if observable == "G" else (a - a[0], b - b[0])
                difference = aa - bb
                rms = weighted_norm(difference, q)
                entry = np.max(np.abs(difference), axis=(1, 2))
                norm = weighted_norm(bb, q)
                rows.append(dict(metadata, layer=layer + 1, panel=panel, observable=observable,
                                 **summarize(rms, entry, norm, times, keep_curves)))
    return rows


def baseline_rows(gram, times, probabilities, metadata):
    rows, m = [], len(probabilities)
    for panel, selected, q in (("data", slice(0, m), probabilities),
                               ("circle", slice(m, m + 128), np.full(128, 1 / 128))):
        for layer in range(2):
            values = np.asarray(gram[:, layer, selected, selected])
            motion = values - values[0]
            rows.append(dict(metadata, layer=layer + 1, panel=panel, observable="DeltaG",
                **summarize(weighted_norm(motion, q), np.max(np.abs(motion), axis=(1, 2)),
                            weighted_norm(values, q), times, True)))
    return rows


def annotate_numerics(means, controls):
    for row in means:
        selected = [control for control in controls if all(control[key] == row[key]
                    for key in ("case", "layer", "panel", "observable"))]
        control_values = {control["control_kind"]: control["primary_rms_max"] for control in selected}
        complete = len(control_values) == 4
        worst = max(control_values.values()) if control_values else None
        numerical = complete and worst <= CONTROL_LIMIT
        row.update(numerical_controls_complete=complete, numerical_controls_pass=numerical,
            maximum_numerical_control=worst, numerical_control_values=control_values,
            order3_controls_apply_directly_to_order=row["order"] == 3,
            n5_error_bound_available=False,
            descriptive_closeness=("close" if row["primary_rms_max"] <= .02 else
                "material_disagreement" if row["primary_rms_max"] > .05 else "inconclusive"),
            numerical_label="resolved_under_declared_diagnostics" if numerical else "numerically_unresolved")


def monotonicity(means, controls):
    rows = []
    for case, width, layer, panel, observable in itertools.product(CASES, WIDTHS, (1, 2),
                                                                  ("data", "circle"), ("G", "DeltaG")):
        matched = {row["order"]: row for row in means if row["case"] == case and row["width"] == width
                   and row["layer"] == layer and row["panel"] == panel and row["observable"] == observable
                   and row["closure"] in (f"{case}_N1", f"{case}_N3", f"{case}_N5")}
        if set(matched) != {1, 3, 5}:
            continue
        relevant = [row for row in controls if row["case"] == case and row["layer"] == layer
                    and row["panel"] == panel and row["observable"] == observable]
        for metric in ("primary_rms_max", "rms_time_average", "rms_time_integral",
                       "maximum_entry_error", "rms_terminal", "relative_rms_max"):
            values = [matched[order][metric] for order in (1, 3, 5)]
            if any(value is None for value in values):
                continue
            improvements = [values[0] - values[1], values[1] - values[2]]
            control_values = [row[metric] for row in relevant if row[metric] is not None]
            worst = max(control_values) if control_values else None
            controls_complete = len(control_values) == 4
            numerically_resolved = all(matched[order]["numerical_controls_pass"] for order in (1, 3, 5))
            decreasing = values[0] >= values[1] >= values[2]
            strict = values[0] > values[1] > values[2]
            attributable = (controls_complete and numerically_resolved and strict
                            and all(improvement > worst for improvement in improvements))
            rows.append(dict(case=case, width=width, layer=layer, panel=panel, observable=observable,
                metric=metric, N1=values[0], N3=values[1], N5=values[2],
                N1_to_N3_improvement=improvements[0], N3_to_N5_improvement=improvements[1],
                monotone_nondecreasing_accuracy=decreasing, strictly_decreasing_error=strict,
                maximum_same_metric_control=worst, numerical_controls_complete=controls_complete,
                numerical_controls_pass=numerically_resolved,
                both_improvements_exceed_controls=controls_complete and strict and all(x > worst for x in improvements),
                order_attribution_supported_by_declared_diagnostics=attributable,
                order5_controls_are_error_bound=False))
    summary = []
    for width, observable, metric in itertools.product(WIDTHS, ("G", "DeltaG"),
            ("primary_rms_max", "rms_time_average", "rms_time_integral", "maximum_entry_error",
             "rms_terminal", "relative_rms_max")):
        selected = [row for row in rows if row["width"] == width and row["observable"] == observable and row["metric"] == metric]
        count = sum(row["monotone_nondecreasing_accuracy"] for row in selected)
        summary.append(dict(width=width, observable=observable, metric=metric, expected_combinations=8,
            available_combinations=len(selected), monotone_combinations=count,
            strict_combinations=sum(row["strictly_decreasing_error"] for row in selected),
            numerically_attributable_combinations=sum(row["order_attribution_supported_by_declared_diagnostics"] for row in selected),
            all_observable_trend=("supported_descriptively" if len(selected) == count == 8 else
                "mixed" if len(selected) == 8 and count else "not_supported" if len(selected) == 8 else "incomplete")))
    return rows, summary


def analyze(base):
    started = time.perf_counter()
    base = base.resolve()
    if base.parent != GENERATED.resolve() or not base.name.startswith("GRAM_"):
        raise ValueError("analysis destination must be a fresh GRAM_* directory in this study")
    campaign = read_json(base / "gram_campaign.json")
    if campaign["plan_sha256"] != digest(PLAN):
        raise ValueError("campaign frozen plan checksum mismatch")
    historical = Path(campaign["source_run"]).resolve()
    if historical != HISTORICAL.resolve():
        raise ValueError("historical scalar input must be this study's original run")
    metadata = read_json(base / "inputs.json")
    input_hash = digest(base / "inputs.npz")
    if input_hash != metadata["npz_sha256"]:
        raise ValueError("working input archive checksum mismatch")
    with np.load(base / "inputs.npz", allow_pickle=False) as archive:
        inputs = {key: archive[key].copy() for key in archive.files}
    times = inputs["times"]
    if times.shape != (206,) or times[0] != 0 or times[-1] != 40 or not np.all(np.diff(times) > 0):
        raise ValueError("invalid frozen observation schedule")
    if inputs["circle"].shape != (128, 2) or not all(np.isfinite(x).all() for x in inputs.values()):
        raise ValueError("invalid or nonfinite working inputs")
    if "exact_arrays" in metadata:
        for key, value in metadata["exact_arrays"].items():
            expected = np.asarray([float.fromhex(x) for x in value["values"]]).reshape(value["shape"])
            if not np.array_equal(inputs[key], expected):
                raise ValueError("literal input identity failed: " + key)
    for case, m in (("axis", 2), ("arcs", 16)):
        q = inputs[case + "_probabilities"]
        if q.shape != (m,) or np.any(q < 0) or abs(q.sum() - 1) > 1e-14:
            raise ValueError("invalid training probabilities: " + case)
    runs, statuses = {"network": {}, "closure": {}}, []
    configs = {"network": campaign["network_configs"], "closure": closure_configurations()}
    if len(configs["network"]) != 16:
        raise ValueError("frozen network menu must contain 16 configurations")
    for family, family_configs in configs.items():
        for config in family_configs:
            run, status = load_run(base, historical, family, config, inputs, input_hash)
            statuses.append(status)
            if run is not None:
                runs[family][run["name"]] = run
    networks, closures = runs["network"], runs["closure"]
    individual, means, width_rows, seed_pairs, controls, movement = [], [], [], [], [], []
    grouped = {}
    for case in CASES:
        q = inputs[case + "_probabilities"]
        for width in WIDTHS:
            group = [networks[f"{case}_n{width}_s{seed}"] for seed in SEEDS
                     if f"{case}_n{width}_s{seed}" in networks]
            for left, right in itertools.combinations(group, 2):
                seed_pairs.extend(comparisons(left["gram"], right["gram"], times, q,
                    dict(case=case, width=width, left=left["name"], reference=right["name"])))
            if len(group) == 3:
                mean = np.zeros_like(group[0]["gram"], subok=False)
                for run in group:
                    mean += run["gram"] / 3
                grouped[(case, width)] = mean
                movement.extend(baseline_rows(mean, times, q,
                    dict(case=case, width=width, family="network_seed_mean", name=f"{case}_n{width}_mean", seeds=list(SEEDS))))
        if all((case, width) in grouped for width in WIDTHS):
            width_rows.extend(comparisons(grouped[(case, 2048)], grouped[(case, 8192)], times, q,
                dict(case=case, smaller_width=2048, reference_width=8192, reference="n8192_three_seed_mean"), True))
        for run in networks.values():
            c = run["config"]
            if c["case"] != case or c["kind"] == "primary":
                continue
            baseline_name = f"{case}_n{c['width']}_s{c['seed']}"
            if baseline_name in networks:
                baseline = networks[baseline_name]
                matching = run["record"].get("initial_float64_block_hashes") == baseline["record"].get("initial_float64_block_hashes")
                if not matching:
                    raise ValueError(f"{run['name']}: numerical control initialization mismatch")
                controls.extend(comparisons(run["gram"], baseline["gram"], times, q,
                    dict(case=case, family="network", control_kind="network_" + c["kind"],
                         control=run["name"], reference=baseline_name, width=c["width"],
                         initial_float64_hashes_match=matching), True))
        for suffix, kind in (("_refined", "closure_quadrature_control"), ("_halfstep", "closure_time_control")):
            control_name, baseline_name = f"{case}_N3{suffix}", f"{case}_N3"
            if control_name in closures and baseline_name in closures:
                controls.extend(comparisons(closures[control_name]["gram"], closures[baseline_name]["gram"], times, q,
                    dict(case=case, family="closure", control_kind=kind, control=control_name,
                         reference=baseline_name, order=3), True))
    for family_runs in runs.values():
        for run in family_runs.values():
            c = run["config"]
            movement.extend(baseline_rows(run["gram"], times, inputs[c["case"] + "_probabilities"],
                dict(case=c["case"], family=run["family"], name=run["name"], width=c.get("width"),
                     seed=c.get("seed"), order=c.get("order"), kind=c.get("kind"))))
    for closure in closures.values():
        c = closure["config"]
        common = dict(case=c["case"], closure=closure["name"], order=c["order"],
                      refined=c["refined"], closure_kind=c["kind"])
        q = inputs[c["case"] + "_probabilities"]
        for network in networks.values():
            n = network["config"]
            if n["case"] == c["case"]:
                individual.extend(comparisons(closure["gram"], network["gram"], times, q,
                    dict(common, network=network["name"], reference=network["name"], width=n["width"],
                         seed=n["seed"], network_kind=n["kind"])))
        for width in WIDTHS:
            if (c["case"], width) in grouped:
                means.extend(comparisons(closure["gram"], grouped[(c["case"], width)], times, q,
                    dict(common, width=width, seeds=list(SEEDS), reference=f"{c['case']}_n{width}_three_seed_mean"), True))
    for row in controls:
        row["below_declared_0_002"] = row["primary_rms_max"] <= CONTROL_LIMIT
    annotate_numerics(means, controls)
    trend, trend_summary = monotonicity(means, controls)
    complete = len(networks) == 16 and len(closures) == 10
    checks_pass = all(row.get("gram_validation", {}).get("passed", False) for row in statuses)
    replay_rows = [row["replay"] for row in statuses if "replay" in row]
    replays_pass = (len([row for row in replay_rows if row["status"] == "compared"]) == 24
                    and all(row["consistent"] for row in replay_rows if row["status"] != "new_time_control_no_historical_counterpart"))
    output = dict(format="hidden-gram-20260914-comparison-v1", created_utc=datetime.now(timezone.utc).isoformat(),
        status="complete" if complete else "incomplete", expected_run_count=26, completed_run_count=len(networks) + len(closures),
        validation_pass=checks_pass, replay_consistency_pass=replays_pass,
        source_sha256=digest(__file__), plan_sha256=digest(PLAN), inputs_sha256=input_hash,
        inputs_json_sha256=digest(base / "inputs.json"), campaign_sha256=digest(base / "gram_campaign.json"),
        command=sys.argv, numpy_version=np.__version__, thread_environment={key: os.environ[key] for key in THREAD_KEYS},
        historical_source_run=str(historical), times=times.tolist(), runs=statuses,
        conventions=dict(gram="Input-index, population-weighted hidden activation products; no data weights inside entries.",
            panel_order="Training inputs, then all 128 original circle inputs; no deduplication.",
            norm="sqrt(sum_ab q_a q_b E_ab^2), using training probabilities or uniform circle probabilities.",
            primary="Maximum weighted Frobenius RMS over the 206 saved times, not a continuous-time supremum.",
            DeltaG="G(t)-G(0); not a neuron displacement Gram or a general cross-time Gram.",
            seed_mean="Arithmetic mean of all three saved Gram matrices at a fixed width; increments then subtract that mean's initialization.",
            spread="Every pair of the three declared seeds; descriptive spread, no confidence interval.",
            relative=f"Pointwise discrepancy divided by reference-panel norm only when norm > {SAFE_NORM}; undefined values are null.",
            relative_integration="Trapezoidal integral only across adjacent valid reference norms; average divides by that valid duration.",
            frozen_baseline="Magnitude of G(t)-G(0); its optional relative curve divides by the current G(t) norm.",
            integration="Trapezoidal on the original nonuniform saved time grid; absolute time averages divide by 40.",
            numerical="All four case/layer/panel/observable control discrepancies must be <=0.002; N3 controls are diagnostics and not N5 error bounds.",
            order_attribution="Both error reductions must strictly exceed all four same-metric numerical controls, with the primary control gate passed.",
            thresholds="Each primary <=0.02 is descriptively close; >0.05 is material disagreement; intervening values inconclusive.",
            labels="Axis data and two simple linearly separable arc clusters; no complicated-label test.",
            scope="Finite widths, saved times, fixed panels and tested closure orders only; no asymptotic or continuous-time certification."),
        seed_mean_comparisons=means, individual_comparisons=individual, width_mean_comparisons=width_rows,
        seed_pair_comparisons=seed_pairs, numerical_controls=controls, frozen_initial_baselines=movement,
        monotonicity=trend, monotonicity_summary=trend_summary, replay_checks=replay_rows)
    output["wall_seconds"] = time.perf_counter() - started
    for key in ("seed_mean_comparisons", "individual_comparisons", "width_mean_comparisons", "seed_pair_comparisons",
                "numerical_controls", "frozen_initial_baselines", "monotonicity", "monotonicity_summary", "replay_checks"):
        csv_write(base / ("gram_" + key + ".csv"), output[key])
    atomic_json(base / "gram_comparison.json", output)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.output)
    print(json.dumps({key: result[key] for key in ("status", "completed_run_count", "expected_run_count",
                                                  "validation_pass", "replay_consistency_pass", "wall_seconds")}, indent=2))


if __name__ == "__main__":
    main()
