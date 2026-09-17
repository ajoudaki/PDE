"""Independent raw-array audit of the frozen thirty-degree comparison.

Scientific input scope before freezing: ARC30 plan and preparation source,
ARC30_v1 working inputs, and seven named completed run records/raw arrays.
No producer, analyzer, report, historical trajectory, or other study is loaded.
This script runs deterministic postprocessing only, never a trajectory.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"
sys.dont_write_bytecode = True
import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
RUN = ROOT / "data/generated/wide_network_closure_comparison/ARC30_20260914_v1"
NETWORKS = [f"network/arcs30_n8192_s{seed}" for seed in (11, 29, 47)]
CLOSURES = [f"closure/arcs30_N{order}" for order in (1, 3, 5)] + ["closure/arcs30_N5_fine"]
EXPECTED_SHAPE = (206, 2, 144, 144)
PANELS = {"training": slice(0, 16), "circle": slice(16, 144)}


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def require(condition, explanation):
    if not condition:
        raise AssertionError(explanation)


def maxabs(array):
    return float(np.max(np.abs(array)))


def rms_curve(errors):
    """Frobenius norm divided by matrix side: sqrt(sum_ab E_ab^2/m^2)."""
    require(errors.ndim == 3 and errors.shape[-1] == errors.shape[-2], "Square matrix sequence required")
    m = errors.shape[-1]
    return np.linalg.norm(errors.reshape(len(errors), m * m), axis=1) / m


def curve_summary(curve, times):
    index = int(np.argmax(curve))
    return {"maximum": float(curve[index]), "maximum_time": float(times[index]),
            "initial": float(curve[0]), "terminal": float(curve[-1]),
            "saved_time_mean": float(np.mean(curve))}


def deterministic_oracles():
    # Nonorthogonal population features; explicit weighted sums are the oracle.
    h = np.array([[.2, -.3, .7], [.8, .4, -.1], [-.5, .6, .2], [.1, -.2, -.4]])
    p = np.array([.1, .2, .3, .4])
    q = np.array([.2, .3, .5])
    gram = h.T @ (p[:, None] * h)
    manual = np.array([[math.fsum(float(p[i] * h[i, a] * h[i, b]) for i in range(4))
                        for b in range(3)] for a in range(3)])
    gram_error = maxabs(gram - manual)
    require(gram_error < 2e-16, "Weighted Gram does not match explicit population sum")
    trace = float(q @ np.diag(gram))
    direct = math.fsum(float(p[i] * q[a] * h[i, a] ** 2) for i in range(4) for a in range(3))
    require(abs(trace - direct) < 2e-16, "Weighted trace identity failed")
    # Off-diagonal errors must occur twice, exactly as full matrices specify.
    error = np.array([[[1., 2.], [2., 3.]]])
    require(abs(rms_curve(error)[0] - math.sqrt(18) / 2) < 5e-16, "Matrix-entry normalization failed")
    perm = np.array([2, 0, 1])
    require(maxabs(gram[np.ix_(perm, perm)] - h[:, perm].T @ (p[:, None] * h[:, perm])) < 2e-16,
            "Gram permutation covariance failed")
    require(np.linalg.eigvalsh(gram)[0] >= -2e-16, "Fixture Gram is not PSD")
    return {"status": "passed", "weighted_gram_explicit_sum_max_error": gram_error,
            "weighted_trace_direct_second_moment_error": abs(trace - direct),
            "off_diagonal_full_matrix_normalization": "sqrt(18)/2",
            "permutation_and_psd": "passed"}


def check_inputs():
    metadata_path = RUN / "inputs.json"
    array_path = RUN / "inputs.npz"
    metadata = json.loads(metadata_path.read_text())
    require(sha256(array_path) == metadata["npz_sha256"], "Working NPZ hash mismatch")
    require(sha256(STUDY / "ARC30_20260914_PLAN.md") == metadata["plan_sha256"], "Plan changed")
    require(sha256(STUDY / "ARC30_20260914_PREPARE.py") == metadata["producer_sha256"], "Input source changed")
    with np.load(array_path, allow_pickle=False) as archive:
        arrays = {key: archive[key].copy() for key in archive.files}
    require(set(arrays) == set(metadata["exact_arrays"]), "Working array inventory mismatch")
    for key, array in arrays.items():
        exact = metadata["exact_arrays"][key]
        decoded = np.array([float.fromhex(value) for value in exact["values"]]).reshape(exact["shape"])
        require(array.dtype == np.float64 and np.array_equal(array, decoded), f"Exact float64 input mismatch: {key}")
        representation = {"shape": list(array.shape), "values": [float(value).hex() for value in array.flat]}
        require(canonical_sha(representation) == metadata["array_sha256"][key], f"Array hash mismatch: {key}")
        require(np.all(np.isfinite(array)), f"Nonfinite working input: {key}")

    u, labels, weights = (arrays[key] for key in ("arcs30_inputs", "arcs30_labels", "arcs30_probabilities"))
    circle, times = arrays["circle"], arrays["times"]
    require(u.shape == (16, 2) and circle.shape == (128, 2), "Input-panel shape mismatch")
    require(np.array_equal(labels, [1.] * 8 + [-1.] * 8), "Binary label order mismatch")
    require(np.array_equal(weights, [1 / 16] * 16) and weights.sum() == 1, "Training masses mismatch")
    angles = np.degrees(np.arctan2(u[:, 1], u[:, 0]))
    endpoints = angles[[0, 7, 8, 15]]
    require(maxabs(endpoints - [-30., 30., 60., 120.]) < 3e-14, "Actual sample endpoints are not thirty-degree arcs")
    unit_error = maxabs(np.sum(u * u, axis=1) - 1)
    circle_unit_error = maxabs(np.sum(circle * circle, axis=1) - 1)
    require(unit_error < 5e-16 and circle_unit_error < 1e-14, "Nonunit observation inputs")
    require(np.array_equal(u[8:, 0], -u[:8, 1]) and np.array_equal(u[8:, 1], u[:8, 0]), "Second cluster is not exact quarter-turn")
    recovered_z = u[:8, 1] / (1 + u[:8, 0])
    expected_z = np.array([(2 * j - 7) / 7 * math.tan(math.pi / 12) for j in range(8)])
    require(maxabs(recovered_z - expected_z) < 2e-16, "Stereographic input positions mismatch")
    margin = float(np.min(labels * (u[:, 0] - u[:, 1]) / math.sqrt(2)))
    require(abs(margin - math.sin(math.pi / 12)) < 5e-16, "Separating margin mismatch")
    fractions = [Fraction(value) for value in metadata["time_fractions"]]
    expected_fractions = [Fraction(0), Fraction(1, 200), Fraction(1, 100), Fraction(1, 50),
                          Fraction(1, 20), Fraction(1, 10)] + [Fraction(j, 5) for j in range(1, 201)]
    require(fractions == expected_fractions, "Frozen time grid differs from all 206 expected times")
    require(np.array_equal(times, [float(value) for value in expected_fractions]), "Saved times differ from rational schedule")
    require(times.shape == (206,) and times[0] == 0 and times[-1] == 40 and np.all(np.diff(times) > 0), "Invalid time interval")
    result = {"status": "passed", "input_files_sha256": {str(metadata_path.relative_to(ROOT)): sha256(metadata_path),
              str(array_path.relative_to(ROOT)): sha256(array_path)}, "array_sha256": metadata["array_sha256"],
              "endpoints_degrees": endpoints.tolist(), "training_max_unit_norm_error": unit_error,
              "circle_max_unit_norm_error": circle_unit_error, "labels": labels.tolist(), "weights": weights.tolist(),
              "minimum_normalized_label_margin": margin, "time_count": len(times),
              "all_times_exactly_match_rational_schedule": True,
              "historical_circle_time_preservation": "Not independently checked: historical inputs are outside assigned scope"}
    return arrays, result, metadata


def check_run(relative_path, inputs, metadata):
    path = RUN / relative_path
    record_path = path / "record.json"
    record = json.loads(record_path.read_text())
    # Do not load even a partial raw file until these finalization gates pass.
    require(record["status"] == "complete", f"Run not final: {relative_path}")
    require(record.get("gram_sha256") and record.get("observations_sha256"), f"Final hashes missing: {relative_path}")
    require(record["completed_observations"] == record["gram_completed_observations"] == 206,
            f"Final observation count mismatch: {relative_path}")
    require(tuple(record["gram_shape"]) == EXPECTED_SHAPE, f"Final Gram shape mismatch: {relative_path}")
    require(Fraction(str(record["last_time"])) == 40, f"Final time mismatch: {relative_path}")
    require(record["gram_plan_sha256"] == metadata["plan_sha256"], f"Run plan mismatch: {relative_path}")
    is_network = relative_path.startswith("network/")
    input_key = "inputs_sha256" if is_network else "inputs_npz_sha256"
    require(record[input_key] == metadata["npz_sha256"], f"Run input mismatch: {relative_path}")
    require(record["steps"] == (4000 if is_network else 8000), f"Step count mismatch: {relative_path}")
    if is_network:
        require(record["width"] == 8192 and record["seed"] in (11, 29, 47) and record["step"] == .01
                and record["dtype"] == "float32" and record["kind"] == "primary", "Network configuration mismatch")
    else:
        config = record["configuration"]
        fine = relative_path.endswith("_fine")
        require(config["initialization_nodes"] == (4096 if fine else 1024)
                and config["population_nodes"] == (2048 if fine else 512)
                and config["step"] == "1/200", "Closure configuration mismatch")
        require(record["fixed_marks_verified"] is True and record["steps_completed_at_last_observation"] == 8000,
                "Closure completion/fixed-mark metadata failed")
        require(record["gram"]["completed_rows"] == record["gram"]["valid_rows"] == 206, "Nested Gram count mismatch")
        require(record["gram"]["sha256"] == record["gram_sha256"], "Nested Gram hash mismatch")

    hashes = {"record.json": sha256(record_path)}
    for filename, key in (("gram.npy", "gram_sha256"), ("observations.npz", "observations_sha256")):
        hashes[filename] = sha256(path / filename)
        require(hashes[filename] == record[key], f"Final file hash mismatch: {relative_path}/{filename}")
    with np.load(path / "observations.npz", allow_pickle=False) as archive:
        obs = {key: archive[key].copy() for key in archive.files}
    gram = np.load(path / "gram.npy", mmap_mode="r", allow_pickle=False)
    require(gram.shape == EXPECTED_SHAPE and gram.dtype == np.float64, "Raw Gram layout mismatch")
    require(np.array_equal(obs["times"], inputs["times"]), "Raw observation time mismatch")
    expected_shapes = {"times": (206,), "loss": (206,), "data_predictions": (206, 16),
                       "predictions": (206, 128), "raw_rms": (206, 2)}
    for key, array in obs.items():
        require(array.shape[0] == 206 and np.all(np.isfinite(array)), f"Incomplete/nonfinite raw observable: {key}")
        if key in expected_shapes:
            require(array.shape == expected_shapes[key], f"Raw observable shape mismatch: {key}")
    require(np.all(np.isfinite(gram)), "Nonfinite Gram")
    symmetry = maxabs(gram - gram.swapaxes(-1, -2))
    largest_entry = maxabs(gram)
    require(symmetry <= 2e-11 and largest_entry <= 1 + 2e-11, "Gram symmetry/entry gates failed")
    trace = np.diagonal(gram[:, :, :16, :16], axis1=-2, axis2=-1) @ inputs["arcs30_probabilities"]
    diagonal_error = maxabs(trace - obs["raw_rms"] ** 2)
    tolerance = 2e-6 if is_network else 2e-11
    require(diagonal_error <= tolerance, "Gram training trace/raw RMS identity failed")
    residuals = obs["data_predictions"] - inputs["arcs30_labels"]
    recomputed_loss = np.array([math.fsum(float(weight * value * value) for weight, value in
                               zip(inputs["arcs30_probabilities"], residual)) for residual in residuals])
    loss_error = maxabs(recomputed_loss - obs["loss"])
    require(loss_error <= tolerance, "Unhalved weighted squared loss identity failed")
    mean_prediction_error = maxabs(obs["data_predictions"] @ inputs["arcs30_probabilities"] - obs["mean_prediction"])
    require(mean_prediction_error <= tolerance, "Weighted mean prediction identity failed")
    minimum_eigenvalues = {}
    for time in (0., 1., 5., 40.):
        index = int(np.flatnonzero(inputs["times"] == time)[0])
        eigenvalues = [float(np.linalg.eigvalsh(gram[index, layer])[0]) for layer in range(2)]
        require(min(eigenvalues) >= -2e-11, "Gram PSD checkpoint failed")
        minimum_eigenvalues[str(time)] = eigenvalues
    require(sha256(record_path) == hashes["record.json"], "Final record changed while checking")
    audit = {"status": "passed", "file_sha256": hashes, "configuration": record.get("configuration", {
             key: record[key] for key in ("width", "seed", "step", "dtype", "kind") if key in record}),
             "producer_source_hashes_as_recorded_not_reaudited": record.get("source_hashes", {}),
             "source_sha256_as_recorded": record.get("source_sha256"),
             "raw_shapes_and_all_206_times": "passed", "maximum_symmetry_error": symmetry,
             "maximum_absolute_gram_entry": largest_entry, "training_diagonal_raw_rms_squared_error": diagonal_error,
             "loss_recomputed_from_data_predictions_max_error": loss_error,
             "weighted_mean_prediction_max_error": mean_prediction_error, "scalar_identity_tolerance": tolerance,
             "full_144_input_gram_psd_minimum_eigenvalues_at_checkpoints": minimum_eigenvalues,
             "initialization_hashes_as_recorded": record.get("initial_float64_block_hashes", record.get("initialization_array_sha256")),
             "initialization_historical_match": "Producer claim retained only; no historical record loaded"}
    return gram, obs, audit


def gram_metrics(candidate, reference, times):
    result = {}
    for panel, selected in PANELS.items():
        result[panel] = {}
        for layer in range(2):
            observed = np.asarray(candidate[:, layer, selected, selected])
            target = reference[:, layer, selected, selected]
            absolute_error = observed - target
            # Each side loses its own initial Gram. This is not a displacement Gram.
            change_error = (observed - observed[0]) - (target - target[0])
            result[panel][f"layer_{layer + 1}"] = {
                "G": curve_summary(rms_curve(absolute_error), times),
                "DeltaG": curve_summary(rms_curve(change_error), times)}
            for error in (absolute_error, change_error):
                for t in (0, 10, 205):
                    explicit = math.sqrt(math.fsum(float(x) ** 2 for x in error[t].flat)) / error.shape[-1]
                    require(abs(explicit - rms_curve(error[t:t + 1])[0]) <= 2e-15,
                            "Frobenius metric disagrees with explicit all-entry scalar sum")
    return result


def compare_frozen(analysis_path):
    """Compare already frozen numbers; never recompute them from author results."""
    require(analysis_path.resolve() == RUN / "arc30_comparison.json", "Only the authorized result path may be compared")
    output = RUN / "independent_check.json"
    payload = json.loads(output.read_text())
    frozen = payload["frozen_calculation"]
    require(canonical_sha(frozen) == payload["frozen_calculation_sha256"], "Frozen calculation integrity failed")
    require(payload["main_analysis_comparison"] is None, "Comparison already retained; do not overwrite it")
    source_snapshot = RUN / "independent_check_frozen_source.py"
    require(sha256(source_snapshot) == frozen["source_sha256"][Path(__file__).name], "Frozen checker source snapshot mismatch")
    analysis_hash = sha256(analysis_path)
    analysis = json.loads(analysis_path.read_text())
    tolerance = 2e-15
    comparisons = []

    def compare_row(label, own, main):
        # The author's rms_time_average is a time integral; our saved_time_mean
        # is an arithmetic saved-grid mean. Compare the latter to that curve.
        values = {"maximum": main["primary_rms_max"], "maximum_time": main["primary_rms_max_time"],
                  "initial": main["rms_initial"], "terminal": main["rms_terminal"],
                  "saved_time_mean": float(np.mean(main["rms_curve"]))}
        differences = {key: abs(own[key] - value) for key, value in values.items()}
        comparisons.append({"metric": label, "independent": own, "main_analysis_equivalents": values,
                            "absolute_differences": differences, "passed": max(differences.values()) <= tolerance})

    for closure, metrics in frozen["metrics"].items():
        for panel in PANELS:
            for layer in (1, 2):
                for observable in ("G", "DeltaG"):
                    matching = [row for row in analysis["seed_mean_comparisons"]
                                if row["closure"] == closure and row["width"] == 8192 and row["layer"] == layer
                                and row["panel"] == ("data" if panel == "training" else "circle")
                                and row["observable"] == observable and row["seeds"] == [11, 29, 47]]
                    require(len(matching) == 1, "Unique Gram metric match missing")
                    own = metrics["grams"][panel][f"layer_{layer}"][observable]
                    compare_row(f"{closure}/{panel}/layer_{layer}/{observable}", own, matching[0])
        matching = [row for row in analysis["scalar_seed_mean_comparisons"]
                    if row["closure"] == closure and row["width"] == 8192 and row["observable"] == "loss"
                    and row["seeds"] == [11, 29, 47]]
        require(len(matching) == 1, "Unique loss metric match missing")
        compare_row(f"{closure}/loss", metrics["loss_absolute_error"], matching[0])
    require(len(comparisons) == 36, "Expected 32 Gram and 4 loss metric comparisons")
    require(sha256(analysis_path) == analysis_hash, "Main analysis changed during comparison")
    status = "passed" if all(row["passed"] for row in comparisons) else "failed"
    comparison = {"status": status, "analysis_path": str(analysis_path), "analysis_sha256": analysis_hash,
                  "source_sha256": sha256(__file__), "frozen_checker_source_snapshot": str(source_snapshot),
                  "frozen_checker_source_snapshot_sha256": sha256(source_snapshot),
                  "command": [sys.executable, str(Path(__file__).resolve()), "--compare", str(analysis_path)],
                  "created_utc": datetime.now(timezone.utc).isoformat(),
                  "scope": "32 Gram metrics and 4 loss metrics for the four frozen closures versus width8192 three-seed means; five equivalent summary values per metric",
                  "absolute_comparison_tolerance": tolerance, "metric_count": len(comparisons), "scalar_value_count": len(comparisons) * 5,
                  "maximum_absolute_difference": max(value for row in comparisons for value in row["absolute_differences"].values()),
                  "calculations_remain_frozen": True, "rows": comparisons}
    payload["main_analysis_comparison"] = comparison
    payload["status"] = status
    payload["checker_development_note"] = "One pre-freeze checker attempt stopped at closure metadata last_time stored as the exact string '40'; the checker was corrected to parse rational metadata before the successful frozen calculation. No trajectory or raw data changed."
    require(canonical_sha(payload["frozen_calculation"]) == payload["frozen_calculation_sha256"], "Comparison mutated frozen result")
    temporary = output.with_suffix(".comparison.tmp")
    with temporary.open("x") as stream:
        json.dump(payload, stream, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(output)
    return {key: value for key, value in comparison.items() if key != "rows"}


def run_check():
    output = RUN / "independent_check.json"
    require(not output.exists(), "Independent frozen result already exists; preserve it")
    oracles = deterministic_oracles()
    inputs, input_audit, metadata = check_inputs()
    all_data = {}
    audits = {}
    for relative in NETWORKS + CLOSURES:
        gram, obs, audit = check_run(relative, inputs, metadata)
        all_data[relative] = (gram, obs)
        audits[relative] = audit
    reference = np.zeros(EXPECTED_SHAPE, dtype=np.float64)
    for relative in NETWORKS:
        reference += all_data[relative][0]
    reference /= 3
    loss_reference = np.mean([all_data[relative][1]["loss"] for relative in NETWORKS], axis=0)
    mean_prediction = np.mean([all_data[relative][1]["data_predictions"] for relative in NETWORKS], axis=0)
    loss_of_mean_prediction = (mean_prediction - inputs["arcs30_labels"]) ** 2 @ inputs["arcs30_probabilities"]
    metrics = {}
    for relative in CLOSURES:
        gram, obs = all_data[relative]
        metrics[relative.split("/")[-1]] = {
            "grams": gram_metrics(gram, reference, inputs["times"]),
            "loss_absolute_error": curve_summary(np.abs(obs["loss"] - loss_reference), inputs["times"]),
            "initial_loss": float(obs["loss"][0]), "terminal_loss": float(obs["loss"][-1])}
    reference_evolution = {}
    for panel, selected in PANELS.items():
        reference_evolution[panel] = {}
        for layer in range(2):
            values = reference[:, layer, selected, selected]
            reference_evolution[panel][f"layer_{layer + 1}"] = curve_summary(rms_curve(values - values[0]), inputs["times"])
    frozen = {"status": "passed", "claim_type": "empirical deterministic raw-array cross-check",
              "checked_by": "/root/arc30_raw_check", "created_utc": datetime.now(timezone.utc).isoformat(),
              "command": [sys.executable, str(Path(__file__).resolve())], "cwd": str(ROOT),
              "python": sys.version, "numpy": np.__version__, "platform": platform.platform(),
              "read_scope": ["ARC30_20260914_PLAN.md", "ARC30_20260914_PREPARE.py", "ARC30_v1 inputs.json/inputs.npz",
                             "named run record.json, observations.npz and gram.npy", "required shared instructions and research skill"],
              "independence": "Calculations frozen before viewing main analysis source/results; no producer imported",
              "source_sha256": {name: sha256(STUDY / name) for name in (
                  "ARC30_20260914_PLAN.md", "ARC30_20260914_PREPARE.py", "ARC30_20260914_CHECK.py")},
              "model_scope": "Frozen bias-free two-hidden-layer tanh model; finite width 8192, seeds 11/29/47; closures N1/N3/N5 Q1024 P512 and N5 Q4096 P2048; saved times 0 through 40",
              "metric_definitions": {"G": "max_saved_time ||G_closure(t)-mean_seed G_network(t)||_F / m",
                  "DeltaG": "max_saved_time ||[G_closure(t)-G_closure(0)]-[mean_seed G_network(t)-mean_seed G_network(0)]||_F / m",
                  "panel_sizes": {"training": 16, "circle": 128}, "gram_entry_weights": "1/m^2 over all m^2 entries, including both off-diagonal orientations",
                  "loss": "max_saved_time abs(loss_closure(t)-mean_seed loss_network(t)); losses are weighted, unhalved squared residuals",
                  "saved_time_mean": "Arithmetic average over the saved-time grid, not an integral in time"},
              "deterministic_oracles": oracles, "inputs": input_audit, "runs": audits,
              "reference_initial_loss": float(loss_reference[0]), "reference_terminal_loss": float(loss_reference[-1]),
              "mean_losses_versus_loss_of_mean_predictions_max_difference": maxabs(loss_reference - loss_of_mean_prediction),
              "reference_frozen_initial_gram_baseline_error": reference_evolution, "metrics": metrics,
              "limitations": ["No trajectory rerun: this independently reproduces metrics and checks observation identities, not the dynamics.",
                  "No producer implementation audit, historical comparison, or initial-state reconstruction is within this assignment.",
                  "No network or closure numerical-resolution controls are evaluated here; descriptive agreement is not certified accuracy.",
                  "No claim of continuous-time bounds, hierarchy convergence, arbitrary-accuracy approximation, or infinite-width identification."]}
    payload = {"format": "arc30-independent-check-v1", "frozen_calculation_sha256": canonical_sha(frozen),
               "frozen_calculation": frozen, "main_analysis_comparison": None}
    with output.open("x") as stream:
        json.dump(payload, stream, indent=2, allow_nan=False)
        stream.write("\n")
    return {"status": "passed", "output": str(output), "frozen_calculation_sha256": payload["frozen_calculation_sha256"],
            "metrics": metrics}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oracles-only", action="store_true")
    parser.add_argument("--compare", type=Path, help="Compare already frozen results to the explicitly authorized main result")
    args = parser.parse_args()
    result = compare_frozen(args.compare) if args.compare else deterministic_oracles() if args.oracles_only else run_check()
    print(json.dumps(result, indent=2, allow_nan=False))
