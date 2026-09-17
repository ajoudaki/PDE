"""Saved-data analysis of the frozen thirty-degree extension; no trajectories.

The prior campaign's pure Gram-metric helpers are reused without modifying their
source or outputs. Changed-data runs are checked against the original random
initializations, not against the previous scalar trajectories.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated/wide_network_closure_comparison"
PLAN = STUDY / "ARC30_20260914_PLAN.md"
OLD = GENERATED / "GRAM_20260914_v1"
_spec = importlib.util.spec_from_file_location("arc30_gram_metrics", STUDY / "GRAM_20260914_ANALYSIS.py")
gram = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gram)
np = gram.np
CASE = "arcs30"
SEEDS, WIDTHS = (11, 29, 47), (2048, 8192)
LIMIT = .002


def closure_configurations():
    result = []
    for order, suffix, q, p, step, kind in (
        (1, "", 1024, 512, "1/200", "primary"),
        (3, "", 1024, 512, "1/200", "primary"),
        (5, "", 1024, 512, "1/200", "primary"),
        (3, "_refined", 2048, 1024, "1/200", "quadrature_control"),
        (3, "_halfstep", 1024, 512, "1/400", "time_control"),
        (5, "_refined", 2048, 1024, "1/200", "quadrature_control"),
        (5, "_fine", 4096, 2048, "1/200", "quadrature_control"),
        (5, "_fine_halfstep", 4096, 2048, "1/400", "time_control")):
        result.append(dict(id=f"{CASE}_N{order}{suffix}", case=CASE, order=order,
            initialization_nodes=q, population_nodes=p, step=step, refined=q > 1024, kind=kind))
    return result


def network_configurations():
    result = [dict(name=f"{CASE}_n{width}_s{seed}", case=CASE, width=width,
        seed=seed, step=.01, dtype="float32", kind="primary") for width in WIDTHS for seed in SEEDS]
    result.extend((dict(name=f"{CASE}_n8192_s11_halfstep", case=CASE, width=8192,
        seed=11, step=.005, dtype="float32", kind="time_control"),
        dict(name=f"{CASE}_n2048_s11_float64", case=CASE, width=2048,
        seed=11, step=.01, dtype="float64", kind="precision_control")))
    return result


def source_checks(record, family):
    sources = record.get("source_hashes", {}).copy()
    result = {}
    for relative, expected in sources.items():
        candidate = Path(relative)
        path = ((STUDY if candidate.parent == Path(".") else ROOT) / candidate).resolve()
        if not (path.is_relative_to(STUDY) or path.is_relative_to(ROOT / "code")):
            raise ValueError("recorded source is outside assigned study/code scope")
        result[relative] = gram.digest(path) == expected
    if family == "network":
        for field, filenames in (
            ("source_sha256", ("WIDE_GPU_20260914_NETWORK.py", "GRAM_20260914_NETWORK.py", "ARC30_20260914_NETWORK.py")),
            ("gram_source_sha256", ("GRAM_20260914_NETWORK.py", "ARC30_20260914_NETWORK.py"))):
            if record.get(field):
                matching = [name for name in filenames if (STUDY / name).exists()
                            and gram.digest(STUDY / name) == record[field]]
                result[field] = bool(matching)
    if not result or not all(result.values()):
        raise ValueError("missing or mismatched current source hashes")
    return result


def load_run(output, family, config, inputs, input_hash):
    name = config.get("name", config.get("id"))
    folder = output / family / name
    status = dict(family=family, name=name, configuration=config)
    path = folder / "record.json"
    if not path.exists():
        return None, dict(status, status="unstarted_or_missing")
    record = gram.read_json(path)
    status.update(status=record.get("status", "missing_status"), record_sha256=gram.digest(path), error=record.get("error"))
    if status["status"] != "complete":
        return None, status
    if not record.get("gram_sha256") or record.get("gram_completed_observations") != 206:
        return None, dict(status, status="awaiting_final_gram_record")
    recorded = record if family == "network" else record.get("configuration", record)
    keys = ("case", "width", "seed", "step", "dtype", "kind") if family == "network" else (
        "case", "order", "initialization_nodes", "population_nodes", "step", "refined", "kind")
    for key in keys:
        if key == "step" and family == "closure":
            equal = Fraction(str(recorded.get(key))) == Fraction(config[key])
        else:
            equal = recorded.get(key) == config[key]
        if not equal:
            raise ValueError(f"{name}: frozen configuration mismatch at {key}")
    if record.get("inputs_sha256", record.get("inputs_npz_sha256")) != input_hash:
        raise ValueError(f"{name}: wrong input checksum")
    if record.get("gram_plan_sha256", record.get("plan_sha256")) != gram.digest(PLAN):
        raise ValueError(f"{name}: wrong frozen plan checksum")
    sources = source_checks(record, family)
    hashes = {}
    for filename, field in (("gram.npy", "gram_sha256"), ("observations.npz", "observations_sha256")):
        hashes[field] = gram.digest(folder / filename)
        if hashes[field] != record.get(field):
            raise ValueError(f"{name}: output checksum mismatch: {filename}")
    with np.load(folder / "observations.npz", allow_pickle=False) as archive:
        arrays = {key: archive[key].copy() for key in archive.files}
    times = inputs["times"]
    if not np.array_equal(arrays.get("times"), times):
        raise ValueError(f"{name}: observation schedule mismatch")
    shapes = {"times": (206,), "loss": (206,), "mean_prediction": (206,),
        "predictions": (206, 128), "data_predictions": (206, 16)}
    shapes.update({key: (206, 2) for key in gram.FIELDS if key not in shapes})
    for key, shape in shapes.items():
        if key not in arrays or arrays[key].shape != shape or not np.isfinite(arrays[key]).all():
            raise ValueError(f"{name}: invalid saved scalar/prediction {key}")
    if not all(np.isfinite(value).all() for value in arrays.values()):
        raise ValueError(f"{name}: nonfinite extra observable")
    matrices = np.load(folder / "gram.npy", mmap_mode="r", allow_pickle=False)
    if matrices.shape != (206, 2, 144, 144) or matrices.dtype != np.float64:
        raise ValueError(f"{name}: Gram shape/dtype mismatch")
    if record.get("gram_shape") != list(matrices.shape):
        raise ValueError(f"{name}: recorded Gram shape mismatch")
    q, y = inputs[CASE + "_probabilities"], inputs[CASE + "_labels"]
    tolerance = 2e-6 if config.get("dtype") == "float32" else 2e-11
    validation = dict(finite=True, maximum_asymmetry=0., maximum_absolute_entry=0.,
        maximum_diagonal_rms_squared_error=0., maximum_diagonal_second_moment_error=0.,
        trace_tolerance=tolerance, symmetry_bound_tolerance=2e-11)
    for start in range(0, 206, 16):
        block = matrices[start:start + 16]
        if not np.isfinite(block).all():
            raise ValueError(f"{name}: nonfinite Gram entry")
        trace = np.diagonal(block[:, :, :16, :16], axis1=2, axis2=3) @ q
        errors = dict(maximum_asymmetry=float(np.max(np.abs(block - block.transpose(0, 1, 3, 2)))),
            maximum_absolute_entry=float(np.max(np.abs(block))),
            maximum_diagonal_rms_squared_error=float(np.max(np.abs(trace - arrays["raw_rms"][start:start + 16] ** 2))),
            maximum_diagonal_second_moment_error=float(np.max(np.abs(trace - arrays["second_moments"][start:start + 16]))))
        for key, value in errors.items():
            validation[key] = max(validation[key], value)
    identities = dict(
        loss=float(np.max(np.abs(arrays["loss"] - np.sum((arrays["data_predictions"] - y) ** 2 * q, axis=1)))),
        mean_prediction=float(np.max(np.abs(arrays["mean_prediction"] - arrays["data_predictions"] @ q))),
        raw_rms=float(np.max(np.abs(arrays["second_moments"] - arrays["raw_rms"] ** 2))),
        paired_motion=float(np.max(np.abs(arrays["motion_rms"] ** 2 -
            (arrays["second_moments"] + arrays["initial_second_moments"] - 2 * arrays["cross_moments"])))),
        fixed_initial_moments=float(np.max(np.abs(arrays["initial_second_moments"] - arrays["initial_second_moments"][0]))),
        zero_initial_motion=float(np.max(np.abs(arrays["motion_rms"][0]))))
    validation["scalar_identity_errors"] = identities
    eigenvalues = []
    for instant in (0., 1., 5., 40.):
        indices = np.flatnonzero(times == instant)
        if len(indices) != 1:
            raise ValueError(f"{name}: missing PSD check time {instant}")
        for layer in range(2):
            matrix = matrices[indices[0], layer]
            values = np.linalg.eigvalsh((matrix + matrix.T) / 2)
            roundoff = 100 * np.finfo(np.float64).eps * 144 * max(1., float(np.max(np.abs(values))))
            eigenvalues.append(dict(time=instant, layer=layer + 1, minimum=float(values[0]),
                maximum=float(values[-1]), roundoff_tolerance=roundoff, passed=bool(values[0] >= -roundoff)))
    validation["eigenvalues"] = eigenvalues
    expected_steps = int(Fraction(40) / Fraction(str(config["step"])))
    validation["expected_steps"] = expected_steps
    validation["actual_steps"] = record.get("steps")
    validation["steps_verified"] = record.get("steps") == expected_steps
    if family == "closure":
        validation["actual_steps_at_last_observation"] = record.get("steps_completed_at_last_observation")
        validation["steps_verified"] &= record.get("steps_completed_at_last_observation") == expected_steps
        validation["fixed_marks_verified"] = (record.get("fixed_marks_verified") is True
            and record.get("fixed_signature_initial") == record.get("fixed_signature_final"))
        initialization_hashes = record.get("initialization_array_sha256", {})
        validation["initialization_array_hashes_recorded"] = (isinstance(initialization_hashes, dict)
            and set(initialization_hashes) == {"b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"}
            and all(isinstance(value, str) and len(value) == 64 for value in initialization_hashes.values()))
    else:
        old_name = name.replace(CASE + "_", "arcs_", 1)
        previous_path = OLD / "network" / old_name / "record.json"
        previous = gram.read_json(previous_path)
        initial_hashes = record.get("initial_float64_block_hashes")
        validation["initialization_matches_old_arcs"] = (isinstance(initial_hashes, list) and len(initial_hashes) == 3
            and initial_hashes == previous.get("initial_float64_block_hashes"))
        validation["old_initialization_record_sha256"] = gram.digest(previous_path)
        validation["tf32_disabled"] = record.get("tf32") is False
        validation["reduced_precision_accumulation_disabled"] = record.get("reduced_precision_accumulation") is False
    validation["passed"] = bool(validation["maximum_asymmetry"] <= 2e-11
        and validation["maximum_absolute_entry"] <= 1 + 2e-11
        and validation["maximum_diagonal_rms_squared_error"] <= tolerance
        and validation["maximum_diagonal_second_moment_error"] <= tolerance
        and max(identities.values()) <= tolerance and all(row["passed"] for row in eigenvalues)
        and validation["steps_verified"]
        and (validation["fixed_marks_verified"] and validation["initialization_array_hashes_recorded"] if family == "closure"
             else validation["initialization_matches_old_arcs"] and validation["tf32_disabled"] and validation["reduced_precision_accumulation_disabled"]))
    status.update(**hashes, validation=validation, source_hash_validation=sources,
        completed_observations=206, wall_seconds=record.get("wall_seconds"),
        cpu_seconds=record.get("cpu_seconds"), peak_allocated_bytes=record.get("peak_allocated_bytes"),
        peak_rss_bytes=record.get("peak_rss_bytes"), torch_version=record.get("torch_version"),
        gpu=record.get("gpu"), numpy_version=record.get("numpy", record.get("numpy_version")),
        scalar_replay_status="not_applicable_changed_training_data")
    return dict(name=name, family=family, config=config, record=record, arrays=arrays, gram=matrices), status


def scalar_comparisons(left, reference, times, metadata, curves=False):
    rows = []
    for observable in ("loss", "predictions"):
        difference = np.abs(left[observable] - reference[observable])
        if observable == "loss":
            rms, entry, norm = difference, difference, np.abs(reference[observable])
        else:
            rms = np.sqrt(np.mean(difference ** 2, axis=1))
            entry = np.max(difference, axis=1)
            norm = np.sqrt(np.mean(reference[observable] ** 2, axis=1))
        row = dict(metadata, observable=observable, **gram.summarize(rms, entry, norm, times, curves))
        if curves:
            row.update(left_curve=left[observable].tolist() if observable == "loss" else None,
                reference_curve=reference[observable].tolist() if observable == "loss" else None)
        if observable == "loss":
            row.update(loss_absolute_max=row["primary_rms_max"], loss_initial=float(left[observable][0]),
                loss_terminal=float(left[observable][-1]), reference_loss_terminal=float(reference[observable][-1]))
        rows.append(row)
    return rows


def scalar_mean(runs):
    return {key: np.mean([run["arrays"][key] for run in runs], axis=0) for key in gram.FIELDS}


def relevant_control_kinds(closure):
    if "_N1" in closure:
        return [], "no_order1_closure_diagnostic"
    if "_N3" in closure:
        return ["N3_quadrature", "N3_time"], "matched_order3_diagnostics"
    if closure == CASE + "_N5":
        return ["N5_quadrature_1024_2048", "N5_quadrature_2048_4096", "N5_fine_time"], "two_refinements_and_transferred_finest_time_diagnostic"
    if closure == CASE + "_N5_refined":
        return ["N5_quadrature_2048_4096", "N5_fine_time"], "next_refinement_and_transferred_finest_time_diagnostic"
    return ["N5_quadrature_2048_4096", "N5_fine_time"], "finest_refinement_and_matched_time_diagnostic"


def compatible(row, control):
    return all(control.get(key) == row.get(key) for key in ("case", "observable", "layer", "panel"))


def annotate(rows, controls):
    for row in rows:
        required, scope = relevant_control_kinds(row["closure"])
        required = ["network_time", "network_precision", *required]
        selected = {c["control_kind"]: c for c in controls if compatible(row, c) and c["control_kind"] in required}
        complete = set(selected) == set(required)
        network_pass = all(kind in selected and selected[kind]["primary_rms_max"] <= LIMIT
                           for kind in ("network_time", "network_precision"))
        closure_kinds = [kind for kind in required if not kind.startswith("network_")]
        closure_pass = bool(closure_kinds) and all(kind in selected and selected[kind]["primary_rms_max"] <= LIMIT
                                                  for kind in closure_kinds)
        values = {key: value["primary_rms_max"] for key, value in selected.items()}
        resolved = complete and network_pass and closure_pass
        lower, upper = (.05, .10) if row["observable"] == "loss" else (.02, .05)
        row.update(numerical_control_values=values, relevant_control_kinds=required,
            numerical_controls_complete=complete and bool(closure_kinds), network_controls_pass=network_pass,
            closure_controls_pass=closure_pass, numerical_controls_pass=resolved,
            numerical_label="resolved_under_declared_diagnostics" if resolved else
                "closure_resolution_unavailable" if not closure_kinds else "numerically_unresolved",
            numerical_control_scope=scope, maximum_numerical_control=max(values.values()) if values else None,
            diagnostics_are_error_bounds=False, time_control_matches_resolution=row["closure"] in (
                CASE + "_N3", CASE + "_N3_halfstep", CASE + "_N5_fine", CASE + "_N5_fine_halfstep"),
            descriptive_closeness=("secondary_no_frozen_closeness_threshold" if row["observable"] == "predictions" else
                "close" if row["primary_rms_max"] <= lower else "material_discrepancy" if row["primary_rms_max"] > upper else "inconclusive"))


def trends(rows, controls, scalar=False):
    result = []
    categories = [(None, None, observable) for observable in ("loss", "predictions")] if scalar else list(
        itertools.product((1, 2), ("data", "circle"), ("G", "DeltaG")))
    for width, (layer, panel, observable) in itertools.product(WIDTHS, categories):
        matched = {r["order"]: r for r in rows if r["width"] == width and r.get("layer") == layer
            and r.get("panel") == panel and r["observable"] == observable
            and r["closure"] in (CASE + "_N1", CASE + "_N3", CASE + "_N5")}
        if set(matched) != {1, 3, 5}:
            continue
        for metric in ("primary_rms_max", "rms_time_average", "rms_time_integral", "maximum_entry_error",
                       "rms_terminal", "relative_rms_max"):
            values = [matched[order][metric] for order in (1, 3, 5)]
            if any(value is None for value in values):
                continue
            needed = set(matched[3]["relevant_control_kinds"]) | set(matched[5]["relevant_control_kinds"])
            selected = [c for c in controls if compatible(matched[5], c) and c["control_kind"] in needed]
            control_values = [c[metric] for c in selected if c[metric] is not None]
            worst = max(control_values) if control_values else None
            complete = {c["control_kind"] for c in selected} == needed and len(control_values) == len(selected)
            improvements = [values[0] - values[1], values[1] - values[2]]
            monotone = values[0] >= values[1] >= values[2]
            exceeds = complete and all(delta > worst for delta in improvements)
            gate = matched[3]["numerical_controls_pass"] and matched[5]["numerical_controls_pass"]
            result.append(dict(case=CASE, width=width, layer=layer, panel=panel, observable=observable,
                metric=metric, N1=values[0], N3=values[1], N5=values[2],
                N1_to_N3_improvement=improvements[0], N3_to_N5_improvement=improvements[1],
                monotone_nondecreasing_accuracy=monotone, strictly_decreasing_error=all(x > 0 for x in improvements),
                maximum_same_metric_control=worst, available_controls_complete=complete,
                both_improvements_exceed_controls=exceeds, numerical_controls_pass=gate,
                order_attribution_supported_by_available_diagnostics=gate and exceeds,
                order1_closure_diagnostic_available=False, controls_are_error_bounds=False))
    summary = []
    for width, observable in itertools.product(WIDTHS, ("loss", "predictions") if scalar else ("G", "DeltaG")):
        selected = [r for r in result if r["width"] == width and r["observable"] == observable and r["metric"] == "primary_rms_max"]
        expected = 1 if scalar else 4
        count = sum(r["monotone_nondecreasing_accuracy"] for r in selected)
        summary.append(dict(width=width, observable=observable, metric="primary_rms_max", expected_combinations=expected,
            available_combinations=len(selected), monotone_combinations=count,
            numerically_attributable_combinations=sum(r["order_attribution_supported_by_available_diagnostics"] for r in selected),
            all_observable_trend="supported_descriptively" if count == len(selected) == expected else
                "mixed" if len(selected) == expected and 0 < count < expected else
                "not_supported" if len(selected) == expected else "incomplete"))
    return result, summary


def old_scalar_run(family, name, preservation):
    directory = OLD / family / name
    for filename in ("record.json", "observations.npz"):
        path = directory / filename
        preservation[str(path)] = gram.digest(path)
    record = gram.read_json(directory / "record.json")
    if preservation[str(directory / "observations.npz")] != record["observations_sha256"]:
        raise ValueError("old-angle scalar checksum mismatch: " + name)
    with np.load(directory / "observations.npz", allow_pickle=False) as archive:
        values = {key: archive[key].copy() for key in archive.files}
    return dict(arrays=values, record=record)


def previous_angle(rows, scalar_rows, times, preservation):
    path = OLD / "gram_comparison.json"
    preservation[str(path)] = gram.digest(path)
    prior = gram.read_json(path)
    if not np.array_equal(prior["times"], times):
        raise ValueError("old-angle metric time grid differs")
    old_rows = [row for row in prior["seed_mean_comparisons"] if row["case"] == "arcs"]
    old_scalar_rows = []
    for width in WIDTHS:
        runs = [old_scalar_run("network", f"arcs_n{width}_s{seed}", preservation) for seed in SEEDS]
        mean = scalar_mean(runs)
        for suffix in ("N1", "N3", "N5", "N3_refined", "N3_halfstep"):
            old = old_scalar_run("closure", "arcs_" + suffix, preservation)
            if not np.array_equal(old["arrays"]["times"], times):
                raise ValueError("old scalar time grid differs")
            old_scalar_rows.extend(scalar_comparisons(old["arrays"], mean, times,
                dict(case="arcs", width=width, closure="arcs_" + suffix), True))
    def match(new_rows, previous_rows):
        output = []
        for row in new_rows:
            old_name = row["closure"].replace(CASE + "_", "arcs_", 1)
            found = [old for old in previous_rows if old["closure"] == old_name
                and all(old.get(key) == row.get(key) for key in ("width", "layer", "panel", "observable"))]
            if not found:
                continue
            old = found[0]
            result = {key: row.get(key) for key in ("width", "layer", "panel", "observable", "closure", "order")}
            result.update(case=CASE, previous_case="arcs", previous_closure=old_name)
            for metric in ("primary_rms_max", "rms_initial", "rms_terminal", "rms_time_average", "rms_time_integral",
                           "maximum_entry_error", "relative_rms_max", "relative_rms_terminal"):
                result["old_" + metric], result["new_" + metric] = old[metric], row[metric]
                result[metric + "_change"] = row[metric] - old[metric] if old[metric] is not None and row[metric] is not None else None
                result[metric + "_ratio"] = row[metric] / old[metric] if old[metric] is not None and old[metric] > 1e-12 and row[metric] is not None else None
            result.update(old_rms_curve=old["rms_curve"], new_rms_curve=row["rms_curve"])
            output.append(result)
        return output
    return match(rows, old_rows), match(scalar_rows, old_scalar_rows)


def validate_inputs(output, campaign):
    metadata = gram.read_json(output / "inputs.json")
    input_hash = gram.digest(output / "inputs.npz")
    if input_hash != metadata["npz_sha256"]:
        raise ValueError("input NPZ checksum mismatch")
    if campaign["plan_sha256"] != gram.digest(PLAN):
        raise ValueError("campaign plan checksum mismatch")
    with np.load(output / "inputs.npz", allow_pickle=False) as archive:
        arrays = {key: archive[key].copy() for key in archive.files}
    if not all(np.isfinite(value).all() for value in arrays.values()):
        raise ValueError("nonfinite working input")
    for key, literal in metadata.get("exact_arrays", {}).items():
        expected = np.asarray([float.fromhex(x) for x in literal["values"]]).reshape(literal["shape"])
        if not np.array_equal(arrays[key], expected):
            raise ValueError("literal working input mismatch: " + key)
        literal_hash = hashlib.sha256(json.dumps(literal, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()
        if literal_hash != metadata.get("array_sha256", {}).get(key):
            raise ValueError("literal input array checksum mismatch: " + key)
    if set(metadata.get("exact_arrays", {})) != set(arrays):
        raise ValueError("incomplete exact working input specification")
    u, y, q = (arrays[CASE + "_" + key] for key in ("inputs", "labels", "probabilities"))
    if u.shape != (16, 2) or not np.array_equal(y, np.r_[np.ones(8), -np.ones(8)]) or not np.array_equal(q, np.full(16, 1/16)):
        raise ValueError("training shape/labels/weights differ from fixed menu")
    z = u[:8, 1] / (1 + u[:8, 0])
    expected_z = (2 * np.arange(8) - 7) / 7 * np.tan(np.pi / 12)
    angles = np.degrees(np.arctan2(u[:8, 1], u[:8, 0]))
    norm_error = float(np.max(np.abs(np.sum(u * u, axis=1) - 1)))
    margin = y * (u[:, 0] - u[:, 1]) / np.sqrt(2)
    with np.load(OLD / "inputs.npz", allow_pickle=False) as archive:
        old_inputs = {key: archive[key].copy() for key in archive.files}
    checks = dict(quarter_turn_exact=np.array_equal(u[8:], np.column_stack((-u[:8, 1], u[:8, 0]))),
        stereographic_spacing_error=float(np.max(np.abs(z - expected_z))),
        unit_norm_error=norm_error, endpoint_angles_degrees=angles[[0, -1]].tolist(),
        minimum_normalized_margin=float(np.min(margin)), expected_margin=float(np.sin(np.pi / 12)),
        old_maximum_sample_deviation_degrees=float(np.max(np.abs(np.degrees(np.arctan2(old_inputs["arcs_inputs"][:8, 1], old_inputs["arcs_inputs"][:8, 0]))))),
        circle_unchanged=np.array_equal(arrays["circle"], old_inputs["circle"]),
        times_unchanged=np.array_equal(arrays["times"], old_inputs["times"]))
    checks["passed"] = bool(checks["quarter_turn_exact"] and checks["stereographic_spacing_error"] < 2e-15
        and norm_error < 2e-14 and np.max(np.abs(angles[[0, -1]] - np.array([-30, 30]))) < 2e-12
        and abs(np.min(margin) - np.sin(np.pi / 12)) < 2e-14
        and checks["circle_unchanged"] and checks["times_unchanged"]
        and arrays["times"].shape == (206,) and arrays["circle"].shape == (128, 2))
    if not checks["passed"]:
        raise ValueError("independent input geometry check failed")
    return arrays, input_hash, checks


def analyze(output):
    started = time.perf_counter()
    output = output.resolve()
    if output.parent != GENERATED.resolve() or not output.name.startswith("ARC30_"):
        raise ValueError("analysis output must be this study's fresh ARC30_* run")
    campaign_path = output / "arc30_campaign.json"
    campaign = gram.read_json(campaign_path)
    campaign_hash = gram.digest(campaign_path)
    inputs, input_hash, input_validation = validate_inputs(output, campaign)
    times, q = inputs["times"], inputs[CASE + "_probabilities"]
    preservation = {str(path): gram.digest(path) for path in (
        OLD / "inputs.npz", OLD / "inputs.json", OLD / "gram_campaign.json",
        STUDY / "GRAM_20260914_ANALYSIS.py", STUDY / "GRAM_20260914_PLAN.md",
        STUDY / "WIDE_GPU_20260914_NETWORK.py", STUDY / "WIDE_GPU_20260914_CLOSURE.py")}
    frozen_preservation = {}
    for field in ("preservation_manifest", "old_study_sources"):
        for relative, expected in campaign.get(field, {}).items():
            path = ((STUDY if field == "old_study_sources" else ROOT) / relative).resolve()
            if not (path.is_relative_to(GENERATED) or path.is_relative_to(STUDY)):
                raise ValueError("old preservation manifest is outside this study")
            frozen_preservation[str(path)] = expected
    if not frozen_preservation:
        raise ValueError("missing frozen old-evidence preservation manifest")
    launch_source_checks = source_checks(dict(source_hashes=campaign.get("launch_source_hashes", {})), "campaign")
    if campaign.get("inputs_sha256") != input_hash or campaign.get("inputs_json_sha256") != gram.digest(output / "inputs.json"):
        raise ValueError("campaign input hashes differ from working input files")
    configurations = {"network": network_configurations(), "closure": closure_configurations()}
    if {c["name"]: c for c in campaign["network_configs"]} != {c["name"]: c for c in configurations["network"]}:
        raise ValueError("campaign network configurations differ from the fixed eight-run menu")
    if {c["id"]: c for c in campaign["closure_configs"]} != {c["id"]: c for c in configurations["closure"]}:
        raise ValueError("campaign closure configurations differ from the fixed eight-run menu")
    runs, statuses = {"network": {}, "closure": {}}, []
    for family, configs in configurations.items():
        for config in configs:
            run, status = load_run(output, family, config, inputs, input_hash)
            statuses.append(status)
            if run:
                runs[family][run["name"]] = run
    networks, closures = runs["network"], runs["closure"]
    tables = {key: [] for key in ("seed_mean_comparisons", "individual_comparisons", "width_mean_comparisons",
        "seed_pair_comparisons", "numerical_controls", "frozen_initial_baselines", "scalar_seed_mean_comparisons",
        "scalar_individual_comparisons", "scalar_width_mean_comparisons", "scalar_seed_pair_comparisons",
        "scalar_numerical_controls", "resolution_span_comparisons", "scalar_resolution_span_comparisons")}
    grouped, scalar_grouped = {}, {}
    def compare(left, right, meta, gram_key, scalar_key, curves=False):
        tables[gram_key].extend(gram.comparisons(left["gram"], right["gram"], times, q, meta, curves))
        tables[scalar_key].extend(scalar_comparisons(left["arrays"], right["arrays"], times, meta, curves))
    for width in WIDTHS:
        group = [networks[f"{CASE}_n{width}_s{seed}"] for seed in SEEDS if f"{CASE}_n{width}_s{seed}" in networks]
        for left, right in itertools.combinations(group, 2):
            compare(left, right, dict(case=CASE, width=width, left=left["name"], reference=right["name"]),
                    "seed_pair_comparisons", "scalar_seed_pair_comparisons")
        if len(group) == 3:
            mean = np.zeros_like(group[0]["gram"], subok=False)
            for run in group:
                mean += run["gram"] / 3
            grouped[width], scalar_grouped[width] = mean, scalar_mean(group)
            tables["frozen_initial_baselines"].extend(gram.baseline_rows(mean, times, q,
                dict(case=CASE, width=width, family="network_seed_mean", name=f"{CASE}_n{width}_mean", seeds=list(SEEDS))))
    if set(grouped) == set(WIDTHS):
        compare(dict(gram=grouped[2048], arrays=scalar_grouped[2048]), dict(gram=grouped[8192], arrays=scalar_grouped[8192]),
            dict(case=CASE, smaller_width=2048, reference_width=8192, reference="n8192_three_seed_mean"),
            "width_mean_comparisons", "scalar_width_mean_comparisons", True)
    for run in networks.values():
        c = run["config"]
        if c["kind"] == "primary":
            continue
        baseline_name = f"{CASE}_n{c['width']}_s{c['seed']}"
        if baseline_name in networks:
            compare(run, networks[baseline_name], dict(case=CASE, family="network", width=c["width"],
                control=run["name"], reference=baseline_name,
                control_kind="network_time" if c["kind"] == "time_control" else "network_precision"),
                "numerical_controls", "scalar_numerical_controls", True)
    for control, baseline, kind in (
        ("N3_refined", "N3", "N3_quadrature"), ("N3_halfstep", "N3", "N3_time"),
        ("N5_refined", "N5", "N5_quadrature_1024_2048"),
        ("N5_fine", "N5_refined", "N5_quadrature_2048_4096"),
        ("N5_fine_halfstep", "N5_fine", "N5_fine_time")):
        control_name, baseline_name = CASE + "_" + control, CASE + "_" + baseline
        if control_name in closures and baseline_name in closures:
            initial_match = None
            if kind in ("N3_time", "N5_fine_time"):
                initial_match = (closures[control_name]["record"]["initialization_array_sha256"]
                                 == closures[baseline_name]["record"]["initialization_array_sha256"])
                if not initial_match:
                    raise ValueError("closure time control initialization differs from its baseline")
            compare(closures[control_name], closures[baseline_name], dict(case=CASE, family="closure",
                control=control_name, reference=baseline_name, control_kind=kind,
                time_control_initialization_matches=initial_match),
                "numerical_controls", "scalar_numerical_controls", True)
    for target in ("N5_fine", "N5_fine_halfstep"):
        a, b = CASE + "_N5", CASE + "_" + target
        if a in closures and b in closures:
            compare(closures[a], closures[b], dict(case=CASE, family="closure", baseline=a, reference=b),
                "resolution_span_comparisons", "scalar_resolution_span_comparisons", True)
    for family_runs in runs.values():
        for run in family_runs.values():
            c = run["config"]
            tables["frozen_initial_baselines"].extend(gram.baseline_rows(run["gram"], times, q,
                dict(case=CASE, family=run["family"], name=run["name"], width=c.get("width"),
                     seed=c.get("seed"), order=c.get("order"), kind=c.get("kind"))))
    for closure in closures.values():
        c = closure["config"]
        common = dict(case=CASE, closure=closure["name"], order=c["order"], refined=c["refined"],
            initialization_nodes=c["initialization_nodes"], population_nodes=c["population_nodes"], step=c["step"], closure_kind=c["kind"])
        for network in networks.values():
            n = network["config"]
            compare(closure, network, dict(common, width=n["width"], seed=n["seed"], network_kind=n["kind"],
                network=network["name"], reference=network["name"]), "individual_comparisons", "scalar_individual_comparisons")
        for width in grouped:
            compare(closure, dict(gram=grouped[width], arrays=scalar_grouped[width]),
                dict(common, width=width, seeds=list(SEEDS), reference=f"{CASE}_n{width}_three_seed_mean"),
                "seed_mean_comparisons", "scalar_seed_mean_comparisons", True)
    for key in ("numerical_controls", "scalar_numerical_controls"):
        for row in tables[key]:
            row["below_declared_0_002"] = row["primary_rms_max"] <= LIMIT
    annotate(tables["seed_mean_comparisons"], tables["numerical_controls"])
    annotate(tables["scalar_seed_mean_comparisons"], tables["scalar_numerical_controls"])
    tables["monotonicity"], tables["monotonicity_summary"] = trends(tables["seed_mean_comparisons"], tables["numerical_controls"])
    tables["scalar_monotonicity"], tables["scalar_monotonicity_summary"] = trends(tables["scalar_seed_mean_comparisons"], tables["scalar_numerical_controls"], True)
    tables["old_angle_comparisons"], tables["scalar_old_angle_comparisons"] = previous_angle(
        tables["seed_mean_comparisons"], tables["scalar_seed_mean_comparisons"], times, preservation)
    preserved = {path: gram.digest(path) == expected for path, expected in preservation.items()}
    frozen_preserved = {path: gram.digest(path) == expected for path, expected in frozen_preservation.items()}
    if not all(preserved.values()) or gram.digest(campaign_path) != campaign_hash:
        raise ValueError("an input or previous artifact changed during postprocessing")
    if not all(frozen_preserved.values()):
        raise ValueError("an old study source or output differs from its frozen pre-experiment hash")
    result = dict(format="arc30-20260914-comparison-v1", created_utc=datetime.now(timezone.utc).isoformat(),
        status="complete" if len(networks) == len(closures) == 8 else "incomplete", expected_run_count=16,
        completed_run_count=len(networks) + len(closures),
        validation_pass=len(statuses) == 16 and all(r.get("validation", {}).get("passed", False) for r in statuses),
        input_validation=input_validation, source_sha256=gram.digest(__file__), metric_dependency_sha256=gram.digest(gram.__file__),
        plan_sha256=gram.digest(PLAN), inputs_sha256=input_hash, inputs_json_sha256=gram.digest(output / "inputs.json"),
        campaign_sha256=campaign_hash, command=sys.argv, numpy_version=np.__version__, times=times.tolist(), runs=statuses,
        thread_environment={key: os.environ.get(key) for key in gram.THREAD_KEYS},
        old_input_hashes=preservation, old_inputs_preserved=all(preserved.values()),
        frozen_old_preservation_hashes=frozen_preservation,
        frozen_old_preservation_count=len(frozen_preservation),
        frozen_old_sources_and_outputs_preserved=all(frozen_preserved.values()),
        launch_source_hash_validation=launch_source_checks,
        scientific_trajectories_started=0, wall_seconds=time.perf_counter() - started,
        conventions=dict(primary_gram="Maximum saved-time sqrt(sum_ab q_a q_b E_ab^2), separately each layer/panel.",
            primary_loss="Maximum absolute difference of losses; reference is mean of three losses, not loss of mean prediction.",
            secondary_prediction="RMS over 128 circle prediction differences; no frozen descriptive closeness cutoff.",
            DeltaG="G(t)-G(0), not a neuron-displacement Gram or general cross-time Gram.",
            relative="Reference norm >1e-12; undefined values null; time integral only over adjacent valid points.",
            frozen_initial_baseline="Norm of G(t)-G(0), with relative curves divided by current G(t) norm.",
            numerical_cutoff=.002, numerical_scope="Separate network and appropriate closure refinement/time diagnostics; no error-bound claim.",
            N1_numerics="No order1 closure diagnostic is in the fixed menu; report network controls and unavailable closure resolution.",
            N5_time_scope="Only finest N5 has matched-resolution time control; other N5 resolutions explicitly label the transferred time diagnostic.",
            old_angle="Matching scalar/Gram discrepancy statistics on prior approximately-five-degree outputs; no older file is overwritten.",
            relative_angle_spacing="Identical relative stereographic spacing, with actual maximum deviation 30 degrees.",
            loss_thresholds="<=0.05 close; >0.10 material discrepancy; intervening range inconclusive.",
            gram_thresholds="<=0.02 close; >0.05 material discrepancy; intervening range inconclusive.",
            labels="Two simple linearly separable clusters; normalized minimum margin sin(15 degrees).",
            limits="Saved-time, fixed-width, finite-panel numerical evidence; no asymptotic or continuous-time certification."), **tables)
    for key, rows in tables.items():
        gram.csv_write(output / ("arc30_" + key + ".csv"), rows)
    gram.atomic_json(output / "arc30_comparison.json", result)
    return result


def fixture():
    """Independent weighted-entry, nonuniform-time and scalar mean checks."""
    weights = np.array([.2, .8])
    matrix = np.array([[[1., 2.], [3., 4.]], [[2., 0.], [0., 2.]], [[0., 0.], [0., 0.]]])
    expected = np.array([sum(weights[a] * weights[b] * row[a, b] ** 2 for a in range(2) for b in range(2)) ** .5 for row in matrix])
    np.testing.assert_allclose(gram.weighted_norm(matrix, weights), expected, atol=1e-15)
    times = np.array([0., 1., 3.])
    result = gram.summarize(np.array([0., 2., 4.]), np.array([0., 3., 5.]), np.array([0., 1., 2.]), times, True)
    assert result["rms_time_integral"] == 7 and result["relative_rms_curve"] == [None, 2., 2.]
    assert result["relative_rms_integrated_duration"] == 2
    a = np.zeros((3, 2, 130, 130))
    b = np.zeros_like(a)
    a[0, :, :2, :2], a[1, :, :2, :2], a[2, :, :2, :2] = 1., 2., 3.
    b[:, :, :2, :2] = .5
    compared = [r for r in gram.comparisons(a, b, times, weights, {}) if r["layer"] == 1 and r["panel"] == "data"]
    assert compared[0]["primary_rms_max"] == 2.5 and compared[1]["primary_rms_max"] == 2.
    assert compared[1]["relative_rms_max"] is None
    left = dict(loss=np.array([1., .8, .6]), predictions=np.array([[1., -1.], [.5, -.5], [0., 0.]]))
    right = dict(loss=np.array([1., .6, .3]), predictions=np.zeros((3, 2)))
    rows = scalar_comparisons(left, right, times, {}, True)
    np.testing.assert_allclose(rows[0]["rms_curve"], [0., .2, .3])
    np.testing.assert_allclose(rows[1]["rms_curve"], [1., .5, 0.])
    fake = [dict(arrays={key: np.array([value]) for key in gram.FIELDS}) for value in (1., 4., 9.)]
    assert scalar_mean(fake)["loss"][0] == 14 / 3
    return dict(status="passed", weighted_entry_oracle=True, nonuniform_time_integral=True,
        undefined_relative_handling=True, G_and_DeltaG=True, loss_absolute_and_prediction_rms=True, mean_of_losses=True,
        source_sha256=gram.digest(__file__), metric_dependency_sha256=gram.digest(gram.__file__), scientific_trajectories_started=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--fixture-only", action="store_true")
    arguments = parser.parse_args()
    if arguments.fixture_only:
        print(json.dumps(fixture(), indent=2))
        return
    if arguments.output is None:
        parser.error("--output is required unless --fixture-only")
    result = analyze(arguments.output)
    print(json.dumps({key: result[key] for key in ("status", "completed_run_count", "expected_run_count", "validation_pass", "wall_seconds")}, indent=2))


if __name__ == "__main__":
    main()
