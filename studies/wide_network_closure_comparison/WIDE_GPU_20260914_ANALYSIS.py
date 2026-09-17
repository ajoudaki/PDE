"""Frozen-plan comparisons of completed finite networks and observable closures.

This reads saved observations only. It does not run either evolution or infer
continuous-time suprema between the declared observation times.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


FIELDS = ("loss", "raw_rms", "motion_rms", "predictions", "data_predictions",
          "mean_prediction", "second_moments", "initial_second_moments", "cross_moments")
CASES = ("axis", "arcs")
SEEDS = (11, 29, 47)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def compare(a, b):
    """Absolute discrepancies; a and b must share the exact saved time grid."""
    if not np.array_equal(a["times"], b["times"]):
        raise ValueError("comparison requires identical time arrays")
    times = a["times"]
    difference = a["predictions"] - b["predictions"]
    rms = np.sqrt(np.mean(difference * difference, axis=1))
    integral = float(np.trapz(rms, times))
    worst = int(np.argmax(rms))
    result = dict(prediction_rms_max=float(rms[worst]),
                  prediction_rms_max_time=float(times[worst]),
                  prediction_coordinate_max=float(np.max(np.abs(difference))),
                  prediction_rms_time_integral=integral,
                  prediction_rms_time_average=integral / float(times[-1] - times[0]),
                  prediction_rms_terminal=float(rms[-1]),
                  loss_max=float(np.max(np.abs(a["loss"] - b["loss"]))),
                  loss_terminal=float(abs(a["loss"][-1] - b["loss"][-1])),
                  data_prediction_coordinate_max=float(np.max(np.abs(
                      a["data_predictions"] - b["data_predictions"]))),
                  mean_prediction_max=float(np.max(np.abs(
                      a["mean_prediction"] - b["mean_prediction"]))))
    for field in ("raw_rms", "motion_rms"):
        delta = np.abs(a[field] - b[field])
        for layer in range(2):
            result[f"{field}{layer+1}_max"] = float(delta[:, layer].max())
            result[f"{field}{layer+1}_initial"] = float(delta[0, layer])
            result[f"{field}{layer+1}_terminal"] = float(delta[-1, layer])
    return result


def core_max(metrics):
    return max(metrics[key] for key in (
        "prediction_rms_max", "loss_max", "raw_rms1_max", "raw_rms2_max",
        "motion_rms1_max", "motion_rms2_max"))


def load_run(base, family, config, inputs, input_hash):
    name = config["name"] if family == "network" else config["id"]
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
    recorded_config = record if family == "network" else record["configuration"]
    for key, value in config.items():
        if recorded_config.get(key) != value:
            raise ValueError(f"{name}: configuration mismatch at {key}")
    recorded_hash = record.get("inputs_sha256", record.get("inputs_npz_sha256"))
    if recorded_hash != input_hash:
        raise ValueError(f"{name}: different working inputs")
    npz_path = directory / "observations.npz"
    if digest(npz_path) != record["observations_sha256"]:
        raise ValueError(f"{name}: observation hash mismatch")
    with np.load(npz_path, allow_pickle=False) as archive:
        arrays = {key: np.asarray(archive[key], dtype=np.float64) for key in ("times",) + FIELDS}
    times = inputs["times"]
    if not np.array_equal(arrays["times"], times):
        raise ValueError(f"{name}: incomplete or different observation schedule")
    case = config["case"]
    m = len(inputs[case + "_labels"])
    shapes = {"loss": (len(times),), "mean_prediction": (len(times),),
              "predictions": (len(times), 128), "data_predictions": (len(times), m)}
    shapes.update({key: (len(times), 2) for key in FIELDS if key not in shapes})
    for key, expected in shapes.items():
        if arrays[key].shape != expected or not np.isfinite(arrays[key]).all():
            raise ValueError(f"{name}: invalid {key} shape or nonfinite value")
    tolerance = 2e-6 if config.get("dtype") == "float32" else 2e-11
    p, y = inputs[case + "_probabilities"], inputs[case + "_labels"]
    identities = {
        "loss": np.sum((arrays["data_predictions"] - y) ** 2 * p, axis=1),
        "mean_prediction": arrays["data_predictions"] @ p,
        "second_moments": arrays["raw_rms"] ** 2,
    }
    for key, recomputed in identities.items():
        if not np.allclose(arrays[key], recomputed, rtol=tolerance, atol=tolerance):
            raise ValueError(f"{name}: observable identity failed: {key}")
    motion = arrays["second_moments"] + arrays["initial_second_moments"] - 2 * arrays["cross_moments"]
    if not np.allclose(arrays["motion_rms"] ** 2, motion, rtol=tolerance, atol=tolerance):
        raise ValueError(f"{name}: paired moment identity failed")
    if not np.allclose(arrays["initial_second_moments"], arrays["initial_second_moments"][0],
                       rtol=0, atol=tolerance):
        raise ValueError(f"{name}: initial moments changed")
    if np.max(np.abs(arrays["motion_rms"][0])) > tolerance:
        raise ValueError(f"{name}: displacement at initialization is nonzero")
    status.update(observations_sha256=record["observations_sha256"],
                  wall_seconds=record.get("wall_seconds"),
                  loss_increases=record.get("observed_loss_increases", record.get("loss_increases", [])))
    return dict(name=name, config=config, record=record, arrays=arrays), status


def mean_run(runs):
    if len(runs) != 3 or sorted(r["config"]["seed"] for r in runs) != list(SEEDS):
        raise ValueError("seed means require all three declared seeds")
    return {"times": runs[0]["arrays"]["times"], **{
        field: np.mean([r["arrays"][field] for r in runs], axis=0) for field in FIELDS}}


def terminal(run):
    a, c = run["arrays"], run["config"]
    return dict(name=run["name"], case=c["case"], family="network" if "width" in c else "closure",
                width=c.get("width"), seed=c.get("seed"), order=c.get("order"),
                refined=c.get("refined"), kind=c.get("kind"), loss=float(a["loss"][-1]),
                raw_rms1=float(a["raw_rms"][-1, 0]), raw_rms2=float(a["raw_rms"][-1, 1]),
                motion_rms1=float(a["motion_rms"][-1, 0]), motion_rms2=float(a["motion_rms"][-1, 1]),
                initial_raw_rms1=float(a["raw_rms"][0, 0]),
                initial_raw_rms2=float(a["raw_rms"][0, 1]))


def csv_write(path, rows):
    if not rows:
        return
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def analyze(base):
    base = base.resolve()
    input_hash = digest(base / "inputs.npz")
    if input_hash != read_json(base / "inputs.json")["npz_sha256"]:
        raise ValueError("input archive hash mismatch")
    with np.load(base / "inputs.npz", allow_pickle=False) as archive:
        inputs = {key: archive[key] for key in archive.files}
    if (inputs["times"].ndim != 1 or inputs["times"][0] != 0 or inputs["times"][-1] != 40
            or not np.all(np.diff(inputs["times"]) > 0) or inputs["circle"].shape != (128, 2)):
        raise ValueError("invalid common time or passive panel grid")
    campaign = read_json(base / "network_campaign.json")
    large = campaign["calibration"]["selected_large_width"]
    configurations = {"network": campaign["configs"], "closure": [
        dict(id=f"{case}_N{order}", case=case, order=order,
             initialization_nodes=1024, population_nodes=512, refined=False)
        for case in CASES for order in (1, 3, 5)] + [
        dict(id=f"{case}_N3_refined", case=case, order=3,
             initialization_nodes=2048, population_nodes=1024, refined=True) for case in CASES]}
    all_runs, statuses = {"network": {}, "closure": {}}, []
    for family, configs in configurations.items():
        for config in configs:
            run, status = load_run(base, family, config, inputs, input_hash)
            statuses.append(status)
            if run:
                all_runs[family][run["name"]] = run
    networks, closures = all_runs["network"], all_runs["closure"]
    individual, means, width_checks, spread, controls, quadrature, reproductions = [], [], [], [], [], [], []
    grouped = {}
    for case in CASES:
        for width in (2048, large):
            runs = [r for r in networks.values() if r["config"]["case"] == case
                    and r["config"]["width"] == width and r["config"]["kind"] == "primary"]
            for left, right in itertools.combinations(runs, 2):
                spread.append(dict(case=case, width=width, left=left["name"], right=right["name"],
                                   **compare(left["arrays"], right["arrays"])))
            if len(runs) == 3:
                grouped[(case, width)] = mean_run(runs)
        if (case, 2048) in grouped and (case, large) in grouped:
            width_checks.append(dict(case=case, smaller_width=2048, larger_width=large,
                                     **compare(grouped[(case, 2048)], grouped[(case, large)])))
        for run in networks.values():
            c = run["config"]
            if c["case"] != case or c["kind"] == "primary":
                continue
            baseline_name = f"{case}_n{c['width']}_s{c['seed']}"
            if baseline_name in networks:
                baseline = networks[baseline_name]
                hashes_match = run["record"]["initial_float64_block_hashes"] == baseline["record"]["initial_float64_block_hashes"]
                if not hashes_match:
                    raise ValueError(f"{run['name']}: control initialization does not match baseline")
                metrics = compare(run["arrays"], baseline["arrays"])
                controls.append(dict(case=case, kind=c["kind"], control=run["name"],
                                     baseline=baseline_name, initial_float64_hashes_match=hashes_match,
                                     below_0_005=core_max(metrics) < .005, **metrics))
        if f"{case}_N3" in closures and f"{case}_N3_refined" in closures:
            quadrature.append(dict(case=case, baseline=f"{case}_N3", refined=f"{case}_N3_refined",
                **compare(closures[f"{case}_N3"]["arrays"], closures[f"{case}_N3_refined"]["arrays"])))
    for closure in closures.values():
        c, record = closure["config"], closure["record"]
        common = dict(case=c["case"], closure=closure["name"], order=c["order"], refined=c["refined"])
        if record.get("matching_original_run"):
            reproductions.append(dict(**common, original=record["matching_original_run"],
                compared_observations=len(record.get("original_comparisons", [])),
                within_1e_10=record.get("original_comparison_within_1e_10"),
                maximum_absolute_differences=record.get("original_maximum_absolute_differences")))
        for network in networks.values():
            n = network["config"]
            if n["case"] == c["case"]:
                individual.append(dict(**common, network=network["name"], width=n["width"],
                    seed=n["seed"], kind=n["kind"], **compare(network["arrays"], closure["arrays"])))
        for width in (2048, large):
            key = (c["case"], width)
            if key not in grouped:
                continue
            metrics = compare(grouped[key], closure["arrays"])
            hidden = max(metrics[f"{field}{layer}_max"]
                         for field in ("raw_rms", "motion_rms") for layer in (1, 2))
            relevant_controls = [row for row in controls if row["case"] == c["case"]]
            network_numerical = len(relevant_controls) == 2 and all(row["below_0_005"] for row in relevant_controls)
            relevant_quadrature = [row for row in quadrature if row["case"] == c["case"]]
            quadrature_pass = len(relevant_quadrature) == 1 and core_max(relevant_quadrature[0]) < .005
            # The declared order-3 refinement is a resolution diagnostic, not
            # an error bound for other orders. A failed diagnostic prevents an
            # unconditional pass of the plan's numerical-control requirement.
            numerical = network_numerical and quadrature_pass
            pass_values = metrics["prediction_rms_max"] <= .05 and hidden <= .03 and metrics["loss_max"] <= .05
            material = metrics["prediction_rms_max"] > .10 or hidden > .06
            verdict = ("material_disagreement_at_tested_resolution" if material and numerical
                       else "agreement_at_tested_resolution" if pass_values and numerical
                       else "inconclusive_at_tested_resolution")
            means.append(dict(**common, width=width, seeds="11,29,47", largest_width=width == large,
                              numerical_controls_pass=numerical,
                              network_time_precision_controls_pass=network_numerical,
                              order3_quadrature_diagnostic_pass=quadrature_pass,
                              quadrature_refinement_matches_order=c["order"] == 3,
                              agreement_values_pass=pass_values,
                              material_disagreement_values=material, descriptive_verdict=verdict,
                              **metrics))
    output = dict(format="wide-gpu-20260914-comparison-v1", created_utc=datetime.now(timezone.utc).isoformat(),
        command=sys.argv, source_sha256=digest(__file__), inputs_sha256=input_hash,
        plan_sha256=digest(Path(__file__).with_name("WIDE_GPU_20260914_PLAN.md")),
        status="complete" if all(s["status"] == "complete" for s in statuses) else "incomplete",
        selected_large_width=large, expected_run_count=24,
        completed_run_count=sum(s["status"] == "complete" for s in statuses), runs=statuses,
        conventions={"prediction_rms": "sqrt(mean over the 128 circle coordinates of squared output differences))",
          "maxima": "Maximum over the shared saved times, not a certified continuous-time supremum.",
          "time_integral": "Trapezoidal integral of saved RMS discrepancies; average divides by T=40.",
          "seed_mean": "Mean of each scalar observable and each prediction coordinate over all three seeds; mean loss is not loss of mean prediction.",
          "spread": "All three pairwise seed discrepancies, without a confidence interval claim.",
          "verdict": "Frozen descriptive thresholds at tested widths, subject to reported width sensitivity; no convergence certification."},
        individual_comparisons=individual, seed_mean_comparisons=means, width_mean_comparisons=width_checks,
        seed_pair_comparisons=spread, numerical_controls=controls, closure_quadrature_controls=quadrature,
        archive_reproductions=reproductions,
        terminal_values=[terminal(run) for family in all_runs.values() for run in family.values()])
    for key in ("individual_comparisons", "seed_mean_comparisons", "width_mean_comparisons",
                "seed_pair_comparisons", "numerical_controls", "closure_quadrature_controls", "terminal_values"):
        csv_write(base / f"{key}.csv", output[key])
    path = base / "comparison.json"
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = analyze(args.output)
    print(json.dumps({key: result[key] for key in ("status", "completed_run_count", "expected_run_count",
                                                 "selected_large_width")}, indent=2))


if __name__ == "__main__":
    main()
