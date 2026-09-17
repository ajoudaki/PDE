#!/usr/bin/env python3
"""Frozen descriptive analysis for the shifted four-pole experiment; no training."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shlex
import sys

import numpy as np

STUDY = Path(__file__).resolve().parent
REPO = STUDY.parents[1]
PANELS = {"training": slice(0, 16), "circle": slice(16, 144)}


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path, value):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, allow_nan=False)
        handle.write("\n")


def provenance():
    return {"utc": datetime.now(timezone.utc).isoformat(),
            "command": shlex.join(getattr(sys, "orig_argv", [sys.executable, *sys.argv])),
            "argv": getattr(sys, "orig_argv", [sys.executable, *sys.argv]),
            "python": sys.version, "numpy": np.__version__,
            "analysis_source_sha256": sha256(__file__)}


def matrix_rms(value):
    """Frobenius norm divided by matrix side length, not number of entries."""
    value = np.asarray(value, dtype=np.float64)
    return np.sqrt(np.mean(value * value, axis=(-2, -1)))


def frozen_readout(times, gram, f0, labels):
    """Exact full-batch readout flow for the frozen hidden Gram and uniform law."""
    gram = np.asarray(gram, dtype=np.float64)
    labels, f0 = np.asarray(labels), np.asarray(f0)
    eigenvalues, eigenvectors = np.linalg.eigh((gram + gram.T) / 2)
    minimum = float(eigenvalues.min())
    if minimum < -2e-10:
        raise ValueError(f"frozen readout Gram minimum eigenvalue {minimum} is below -2e-10")
    # Retain rounding-sized negative eigenvalues: this is the original working
    # Gram exponential, not a projected-PSD replacement.
    coefficients = eigenvectors.T @ (f0 - labels)
    decay = np.exp(-2 * np.asarray(times)[:, None] * eigenvalues[None, :] / len(labels))
    prediction = labels + (decay * coefficients) @ eigenvectors.T
    losses = np.mean((prediction - labels) ** 2, axis=1)
    return prediction, losses, minimum


def verify(output):
    output.mkdir(parents=True, exist_ok=False)
    rng = np.random.default_rng(721)
    features = rng.normal(size=(7, 4))
    gram = features.T @ features / 7
    f0, labels = rng.normal(size=(2, 4))
    times = np.array([0., .2, 1.3])
    prediction, losses, minimum = frozen_readout(times, gram, f0, labels)
    eps = 1e-5
    plus = frozen_readout(times + eps, gram, f0, labels)[0]
    minus = frozen_readout(times - eps, gram, f0, labels)[0]
    derivative = (plus - minus) / (2 * eps)
    expected = -2 * (prediction - labels) @ gram / 4
    diagonal = np.diag([.2, .4, .6, .8])
    actual = frozen_readout(times, diagonal, f0, labels)[0]
    exact = labels + np.exp(-times[:, None] * np.diag(diagonal) / 2) * (f0 - labels)
    checks = {
        "zero_time_max_error": float(np.max(np.abs(prediction[0] - f0))),
        "differential_equation_max_error": float(np.max(np.abs(derivative - expected))),
        "diagonal_exact_solution_max_error": float(np.max(np.abs(actual - exact))),
        "zero_kernel_max_error": float(np.max(np.abs(frozen_readout(times, np.zeros((4, 4)), f0, labels)[0] - f0))),
        "loss_identity_max_error": float(np.max(np.abs(losses - np.mean((prediction-labels)**2, axis=1)))),
        "ones_matrix_rms_error": abs(float(matrix_rms(np.ones((4, 4))))-1),
        "identity_matrix_rms_error": abs(float(matrix_rms(np.eye(4)))-.5),
        "gram_minimum_eigenvalue": minimum,
    }
    base = np.broadcast_to(np.arange(3.)[:, None, None, None], (3, 2, 144, 144))
    comparison = discrepancy({"loss": np.zeros(3), "gram": base+2},
                             {"loss": np.zeros(3), "gram": base}, np.arange(3.))
    checks["constant_shift_gram_rms_error"] = max(abs(number-2) for key, number in metric_maxima(comparison).items() if ".G." in key)
    checks["constant_shift_delta_gram_error"] = max(number for key, number in metric_maxima(comparison).items() if ".DeltaG." in key)
    tiny_negative = np.diag([-1e-12, .4, .6, .8])
    negative_prediction = frozen_readout(np.array([100.]), tiny_negative, f0, labels)[0]
    negative_exact = labels + np.exp(-50*np.diag(tiny_negative))*(f0-labels)
    checks["negative_roundoff_eigenvalue_preserved_error"] = float(np.max(np.abs(negative_prediction-negative_exact)))
    try:
        frozen_readout(times, np.diag([-1e-8, .4, .6, .8]), f0, labels)
    except ValueError:
        checks["non_psd_kernel_rejection_error"] = 0.
    else:
        checks["non_psd_kernel_rejection_error"] = 1.
    checks["pass"] = all(value < (2e-9 if "differential" in name else 2e-13)
                         for name, value in checks.items() if name != "gram_minimum_eigenvalue")
    write_json(output / "verification.json", {"provenance": provenance(), "checks": checks,
               "scope": "Deterministic algebra and finite-difference ODE checks only; no scientific training."})
    if not checks["pass"]:
        raise SystemExit("analysis verification failed")
    print(json.dumps(checks, sort_keys=True))


def _maximum(value):
    value = np.asarray(value)
    index = np.unravel_index(np.argmax(value), value.shape)
    return {"value": float(value[index]), "index": list(map(int, index))}


def load_manifest(output):
    path = output / "manifest.json"
    with path.open() as handle:
        return path, json.load(handle)


def load_run(output, kind, config, inputs):
    name = config["name"]
    folder = output / kind / name
    report = {"kind": kind, "config": config, "folder": str(folder), "issues": [],
              "hashes": {}, "available": False, "valid": False}
    record_path = folder / "record.json"
    if record_path.exists():
        report["record"] = json.loads(record_path.read_text())
    else:
        report["issues"].append("missing record.json")
    try:
        with np.load(folder / "observations.npz", allow_pickle=False) as archive:
            observations = {key: archive[key] for key in archive.files}
        gram = np.load(folder / "gram.npy", mmap_mode="r", allow_pickle=False)
    except (OSError, ValueError) as error:
        report["issues"].append(f"unavailable observations: {error}")
        return report, None
    report["available"] = True
    for path in sorted(folder.iterdir()):
        if path.is_file():
            report["hashes"][path.name] = sha256(path)
    record = report.get("record", {})
    if record.get("config") != config:
        report["issues"].append("recorded configuration missing or differs from manifest")
    output_hashes = record.get("output_hashes", {})
    if not output_hashes:
        report["issues"].append("record contains no output hashes")
    for filename, entry in output_hashes.items():
        expected_hash = entry.get("sha256") if isinstance(entry, dict) else entry
        if report["hashes"].get(filename) != expected_hash:
            report["issues"].append(f"output hash mismatch: {filename}")
    report["observed_shapes"] = {key: list(value.shape) for key, value in observations.items()}
    report["observed_shapes"]["gram"] = list(gram.shape)
    if "times" in observations and "loss" in observations:
        finite_prefix = np.isfinite(observations["times"]) & np.isfinite(observations["loss"])
        report["retained_observed_loss"] = {"times": observations["times"][finite_prefix].tolist(),
                                            "loss": observations["loss"][finite_prefix].tolist()}
    shape_issues = []
    expected = {"times": (201,), "loss": (201,), "predictions": (201, 144),
                "raw_rms": (201, 2), "movement_rms": (201, 2)}
    for key, shape in expected.items():
        if key not in observations or observations[key].shape != shape:
            shape_issues.append(f"{key} must have shape {shape}")
    if gram.shape != (201, 2, 144, 144):
        shape_issues.append("gram must have shape (201,2,144,144)")
    report["issues"].extend(shape_issues)
    if shape_issues:
        return report, None
    if gram.dtype != np.float64:
        report["issues"].append("Gram storage is not float64")
    for key, value in {**observations, "gram": gram}.items():
        if not np.isfinite(value).all():
            report["issues"].append(f"nonfinite {key}")
    if report["issues"]:
        return report, None
    if not np.array_equal(observations["times"], inputs["times"]):
        report["issues"].append("observation times differ from frozen input times")
    recorded_count = record.get("observation_count", record.get("counts", {}).get("observations"))
    if recorded_count != 201:
        report["issues"].append("recorded observation count differs from 201")
    if "observation_times" in record and not np.array_equal(record["observation_times"], observations["times"]):
        report["issues"].append("recorded observation times differ from saved times")
    tolerance = 3e-6 if str(config.get("dtype", "float64")) == "float32" else 2e-10
    labels, weights = inputs["labels"], inputs["weights"]
    recomputed_loss = ((observations["predictions"][:, :16] - labels) ** 2) @ weights
    loss_error = np.abs(recomputed_loss - observations["loss"])
    diagonal = np.diagonal(gram, axis1=-2, axis2=-1)
    raw_rms_error = np.abs(observations["raw_rms"] ** 2 - diagonal[:, :, :16] @ weights)
    symmetry_error = float(np.max(np.abs(gram - gram.swapaxes(-2, -1))))
    initial_movement = float(np.max(np.abs(observations["movement_rms"][0])))
    rms = observations["raw_rms"]
    movement = observations["movement_rms"]
    rms_bound_error = float(max(0, np.max(np.abs(rms - rms[0]) - movement),
                                np.max(movement - rms - rms[0]), -np.min(movement)))
    parity_error = float(np.max(np.abs(observations["predictions"][:, 16:80] + observations["predictions"][:, 80:144])))
    endpoint_eigenvalues = [[float(np.linalg.eigvalsh((gram[t, layer]+gram[t, layer].T)/2).min())
                            for layer in (0, 1)] for t in (0, 200)]
    increase = np.diff(observations["loss"])
    increase_bound = np.maximum(1e-6, 1e-4 * observations["loss"][:-1])
    increases = np.flatnonzero(increase > increase_bound)
    report["checks"] = {
        "observation_count": len(observations["times"]), "tolerance": tolerance,
        "max_loss_identity_error": float(loss_error.max()),
        "max_raw_rms_squared_identity_error": float(raw_rms_error.max()),
        "max_gram_asymmetry": symmetry_error,
        "max_gram_absolute_entry": float(np.max(np.abs(gram))),
        "minimum_gram_diagonal": float(diagonal.min()),
        "endpoint_minimum_eigenvalues": endpoint_eigenvalues,
        "initial_movement_max": initial_movement, "rms_triangle_bound_error": rms_bound_error,
        "max_circle_prediction_oddness_error": parity_error,
        "loss_increases": [{"time": float(observations["times"][i+1]), "increase": float(increase[i]),
                            "allowed": float(increase_bound[i])} for i in increases],
        "movement_limitation": "Saved same-time Grams cannot reconstruct cross-time activation products; raw-RMS identity, initial zero and triangle bounds checked.",
    }
    conditions = {"loss identity": np.all(loss_error <= tolerance*np.maximum(1, np.abs(observations["loss"]))),
                  "Gram/raw RMS identity": raw_rms_error.max() <= tolerance,
                  "Gram symmetry": symmetry_error <= tolerance,
                  "Gram bounds": np.max(np.abs(gram)) <= 1+tolerance and diagonal.min() >= -tolerance,
                  "endpoint PSD": np.min(endpoint_eigenvalues) >= -2e-10,
                  "initial movement": initial_movement <= tolerance,
                  "RMS triangle bounds": rms_bound_error <= tolerance,
                  "prediction oddness": parity_error <= tolerance,
                  "sampled loss monotonicity": not len(increases)}
    for label, passed in conditions.items():
        if not passed:
            report["issues"].append(f"failed {label}")
    status = str(report.get("record", {}).get("status", "")).lower()
    if status and status not in {"ok", "success", "completed", "complete", "passed"}:
        report["issues"].append(f"recorded status: {status}")
    report["valid"] = not report["issues"]
    report["curves"] = {key: observations[key].tolist() for key in ("loss", "raw_rms", "movement_rms")}
    report["terminal_loss"] = float(observations["loss"][-1])
    report["fits_at_declared_cutoff"] = report["terminal_loss"] <= .01
    return report, {**observations, "gram": gram, "config": config, "valid": report["valid"]}


def discrepancy(left, right, times):
    result = {"loss": {"maximum": _maximum(np.abs(left["loss"]-right["loss"])),
                       "curve": np.abs(left["loss"]-right["loss"]).tolist()}, "panels": {}}
    for label, panel in PANELS.items():
        a, b = left["gram"][:, :, panel, panel], right["gram"][:, :, panel, panel]
        difference = a-b
        delta = difference-difference[0]
        value = {}
        for quantity, array in (("G", difference), ("DeltaG", delta)):
            curves = matrix_rms(array)
            value[quantity] = {f"layer{layer+1}": {"maximum": _maximum(curves[:, layer]),
                                 "curve": curves[:, layer].tolist()} for layer in (0, 1)}
        result["panels"][label] = value
    for item in [result["loss"], *[item for panel in result["panels"].values()
                 for quantity in panel.values() for item in quantity.values()]]:
        item["maximum"]["time"] = float(times[item["maximum"]["index"][0]])
    return result


def metric_maxima(comparison):
    return {"loss": comparison["loss"]["maximum"]["value"],
            **{f"{panel}.{quantity}.{layer}": item["maximum"]["value"]
               for panel, quantities in comparison["panels"].items()
               for quantity, layers in quantities.items() for layer, item in layers.items()}}


def _matches(config, **query):
    for key, expected in query.items():
        actual = config.get(key)
        if key == "step":
            if actual is None or abs(float(actual)-expected) > 1e-12:
                return False
        elif actual != expected:
            return False
    return True


def analyze(output):
    destination = output / "analysis.json"
    if destination.exists():
        raise FileExistsError(destination)
    manifest_path, manifest = load_manifest(output)
    input_path = output / "inputs.npz"
    with np.load(input_path, allow_pickle=False) as archive:
        inputs = {key: archive[key] for key in archive.files}
    if not np.array_equal(inputs["times"], np.arange(201)/2):
        raise ValueError("frozen times are not exactly 0:0.5:100")
    if inputs["panel"].shape != (144, 2) or inputs["inputs"].shape != (16, 2):
        raise ValueError("unexpected input or panel shape")
    if not np.array_equal(inputs["inputs"], inputs["panel"][:16]):
        raise ValueError("training inputs are not first on the panel")
    if not np.allclose(inputs["weights"], np.full(16, 1/16), rtol=0, atol=0):
        raise ValueError("readout formula requires the frozen uniform law")
    result = {"provenance": provenance(), "scope": "Exploratory finite experiment at one law through T=100; no hierarchy convergence or population-limit theorem.",
              "times": inputs["times"].tolist(), "runs": {}, "width_means": {},
              "controls": {}, "comparisons": {}, "order_rankings": {}, "issues": []}
    result["provenance"].update(manifest_sha256=sha256(manifest_path), inputs_sha256=sha256(input_path),
                                plan_sha256=sha256(STUDY / "EXPERIMENT_PLAN.md"), source_hashes={})
    for key in ("inputs_sha256", "plan_sha256"):
        if manifest.get(key) != result["provenance"][key]:
            result["issues"].append(f"frozen {key} missing or mismatched")
    for name, expected in manifest.get("source_hashes", {}).items():
        path = Path(name)
        if not path.is_absolute():
            path = REPO / path
        actual = sha256(path) if path.exists() else None
        result["provenance"]["source_hashes"][name] = {"expected": expected, "actual": actual}
        if actual != expected:
            result["issues"].append(f"source hash mismatch: {name}")
    if not manifest.get("source_hashes"):
        result["issues"].append("manifest contains no frozen source hashes")
    arrays = {}
    for kind in ("network", "closure"):
        configs = manifest.get(kind+"_runs", [])
        if len(configs) != 8:
            result["issues"].append(f"expected eight {kind} configurations, found {len(configs)}")
        for config in configs:
            key = kind+"/"+config["name"]
            report, values = load_run(output, kind, config, inputs)
            result["runs"][key] = report
            if values is not None:
                arrays[key] = values
            if not report["valid"]:
                result["issues"].append(f"invalid or unavailable run: {key}")

    def select(kind, **query):
        found = [key for key, value in arrays.items() if key.startswith(kind+"/") and _matches(value["config"], **query)]
        return found[0] if len(found) == 1 else None

    means = {}
    for width in (2048, 8192):
        keys = [select("network", width=width, seed=seed, step=.01, dtype="float32") for seed in (11, 29, 47)]
        if not all(keys):
            result["issues"].append(f"width {width} lacks a complete three-seed reference")
            continue
        runs = [arrays[key] for key in keys]
        mean = {field: sum(np.asarray(run[field], dtype=np.float64) for run in runs)/3
                for field in ("gram", "loss", "predictions", "raw_rms", "movement_rms")}
        mean["valid"] = all(run["valid"] for run in runs)
        means[width] = mean
        baselines = []
        for key, run in zip(keys, runs):
            prediction, losses, minimum = frozen_readout(inputs["times"], run["gram"][0, 1, :16, :16],
                                                        run["predictions"][0, :16], inputs["labels"])
            baseline = {"run": key, "loss": losses.tolist(), "terminal_loss": float(losses[-1]),
                        "minimum_raw_kernel_eigenvalue": minimum,
                        "kernel_psd_within_tolerance": bool(minimum >= -2e-10),
                        "symmetrization_max_change": float(np.max(np.abs(run["gram"][0, 1, :16, :16]-run["gram"][0, 1, :16, :16].T))/2),
                        "zero_time_max_prediction_error": float(np.max(np.abs(prediction[0]-run["predictions"][0, :16])))}
            if minimum < -2e-10:
                result["issues"].append(f"frozen readout kernel is not PSD within tolerance: {key}")
            baselines.append(baseline)
            result["runs"][key]["frozen_readout"] = baseline
        baseline_mean = np.mean([entry["loss"] for entry in baselines], axis=0)
        spreads = {key: discrepancy(run, mean, inputs["times"]) for key, run in zip(keys, runs)}
        frozen = {"gram": np.broadcast_to(mean["gram"][0], mean["gram"].shape), "loss": mean["loss"]}
        frozen_error = discrepancy(frozen, mean, inputs["times"])
        summary = {"members": keys, "valid": mean["valid"], "loss": mean["loss"].tolist(),
                   "terminal_loss": float(mean["loss"][-1]), "fits_at_declared_cutoff": bool(mean["loss"][-1] <= .01),
                   "loss_seed_min": np.min([run["loss"] for run in runs], axis=0).tolist(),
                   "loss_seed_max": np.max([run["loss"] for run in runs], axis=0).tolist(),
                   "seed_deviations_from_mean": spreads, "frozen_gram_baseline": frozen_error,
                   "frozen_readout_mean_loss": baseline_mean.tolist(), "frozen_readout_per_seed": baselines,
                   "movement_rms_mean": mean["movement_rms"].tolist(),
                   "hidden_training_advantage": {"terminal_actual": float(mean["loss"][-1]),
                       "terminal_readout_only": float(baseline_mean[-1]),
                       "absolute_improvement": float(baseline_mean[-1]-mean["loss"][-1]),
                       "passes_declared_effect_cutoff": bool(mean["loss"][-1] <= baseline_mean[-1]/2 and baseline_mean[-1]-mean["loss"][-1] >= .05)}}
        result["width_means"][str(width)] = summary
    if len(means) == 2:
        result["width_spread"] = discrepancy(means[2048], means[8192], inputs["times"])

    control_specs = [
        ("network_time", "network", dict(width=8192, seed=11, dtype="float32", step=.01), dict(width=8192, seed=11, dtype="float32", step=.005)),
        ("network_precision", "network", dict(width=2048, seed=11, dtype="float32", step=.01), dict(width=2048, seed=11, dtype="float64", step=.01)),
        ("closure_time_N3", "closure", dict(order=3, initialization_nodes=2048, population_nodes=1024, step=.01), dict(order=3, initialization_nodes=2048, population_nodes=1024, step=.005)),
        ("closure_time_N5", "closure", dict(order=5, initialization_nodes=4096, population_nodes=2048, step=.01), dict(order=5, initialization_nodes=4096, population_nodes=2048, step=.005)),
        *[(f"closure_quadrature_N{order}", "closure", dict(order=order, initialization_nodes=2048, population_nodes=1024, step=.01), dict(order=order, initialization_nodes=4096, population_nodes=2048, step=.01)) for order in (1, 3, 5)],
    ]
    for name, kind, a, b in control_specs:
        left, right = select(kind, **a), select(kind, **b)
        if not left or not right:
            result["controls"][name] = {"pass": False, "status": "unresolved: missing observations", "queries": [a, b]}
            continue
        comparison = discrepancy(arrays[left], arrays[right], inputs["times"])
        maxima = metric_maxima(comparison)
        passed = arrays[left]["valid"] and arrays[right]["valid"] and all(value <= .002 for value in maxima.values())
        result["controls"][name] = {"pass": bool(passed), "status": "resolved within declared cutoff" if passed else "unresolved", "members": [left, right], "maxima": maxima, "comparison": comparison}

    for width, mean in means.items():
        baseline = result["width_means"][str(width)]["frozen_gram_baseline"]
        for key, value in arrays.items():
            if not key.startswith("closure/"):
                continue
            comparison = discrepancy(value, mean, inputs["times"])
            maxima = metric_maxima(comparison)
            operational = {name: number <= (.02 if name == "loss" else .05) for name, number in maxima.items()}
            improvement = {}
            for panel, quantities in comparison["panels"].items():
                for layer in ("layer1", "layer2"):
                    error = quantities["G"][layer]["maximum"]["value"]
                    frozen = baseline["panels"][panel]["G"][layer]["maximum"]["value"]
                    improvement[panel+"."+layer] = {"closure_maximum": error, "frozen_maximum": frozen,
                        "nontrivial_reference_movement": frozen > .02,
                        "halves_frozen_error": bool(error <= frozen/2),
                        "ratio_to_frozen": error/frozen if frozen > 0 else None}
            result["comparisons"][f"{key}:width{width}"] = {"reference_width": width, "closure": key,
                 "comparison": comparison, "maxima": maxima, "operational_agreement": operational,
                 "all_operational_cutoffs_pass": all(operational.values()), "frozen_gram_improvement": improvement}
        for q, p in ((2048, 1024), (4096, 2048)):
            members = [select("closure", order=order, initialization_nodes=q, population_nodes=p, step=.01) for order in (1, 3, 5)]
            if all(members):
                ranking = {}
                for metric in metric_maxima(result["comparisons"][f"{members[0]}:width{width}"]["comparison"]):
                    values = [{"order": arrays[key]["config"]["order"], "run": key,
                               "value": result["comparisons"][f"{key}:width{width}"]["maxima"][metric]} for key in members]
                    ranking[metric] = sorted(values, key=lambda item: item["value"])
                result["order_rankings"][f"width{width}_Q{q}_P{p}"] = ranking

    unresolved = [name for name, control in result["controls"].items() if not control["pass"]]
    result["verdict"] = {"all_16_runs_valid": len(result["runs"]) == 16 and all(run["valid"] for run in result["runs"].values()),
        "all_numerical_controls_pass": not unresolved, "unresolved_axes": unresolved,
        "interpretation": "descriptive only" if unresolved or result["issues"] else "operational agreement can be assessed at the declared finite resolutions",
        "limits": ["A single law and bounded horizon do not establish hierarchy convergence.",
                   "Width and seed spread are descriptive; two widths do not identify an infinite-width limit.",
                   "Time, precision and quadrature controls are distinct; passing one cannot resolve another."]}
    if "8192" in result["width_means"]:
        advantage = result["width_means"]["8192"]["hidden_training_advantage"]
        advantage["supported_with_controls"] = bool(advantage["passes_declared_effect_cutoff"]
            and result["width_means"]["8192"]["valid"]
            and result["controls"]["network_time"]["pass"] and result["controls"]["network_precision"]["pass"]
            and not any("hash" in issue for issue in result["issues"]))
    write_json(destination, result)
    print(json.dumps({"analysis": str(destination), "sha256": sha256(destination), "verdict": result["verdict"]}, sort_keys=True))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        verify(args.output)
    else:
        analyze(args.output)


if __name__ == "__main__":
    main()
