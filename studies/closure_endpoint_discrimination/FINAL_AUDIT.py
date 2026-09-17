"""Independent saved-array audit; no model import, replay, or training."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np

STUDY = Path(__file__).resolve().parent
GENERATED = STUDY.parents[1] / "data/generated/closure_endpoint_discrimination"


def sha256(path):
    value = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def owned(path):
    path = Path(path).resolve()
    if not path.is_relative_to(GENERATED):
        raise ValueError("input/output outside this study")
    return path


def load_npz(path):
    with np.load(path, allow_pickle=False) as values:
        return {key: values[key].copy() for key in values.files}


def norms(difference, mask):
    difference = np.asarray(difference, dtype=np.float64)
    return dict(gap_rms=float(np.sqrt(np.mean(difference[mask] ** 2))),
                gap_max=float(np.max(np.abs(difference[mask]))),
                circle_rms=float(np.sqrt(np.mean(difference ** 2))),
                circle_max=float(np.max(np.abs(difference))))


def gram_relative(left, right):
    return [float(np.linalg.norm(a - b) / np.linalg.norm(b)) for a, b in zip(left, right)]


def audit(manifest_path, verification_path):
    manifest_path, verification_path = owned(manifest_path), owned(verification_path)
    manifest = json.loads(manifest_path.read_text())
    verification = json.loads(verification_path.read_text())
    if verification.get("passed") is not True or verification.get("manifest_sha256") != sha256(manifest_path):
        raise ValueError("manifest does not have a matching passed verification")
    inputs = load_npz(owned(manifest["inputs_path"]))
    m = len(inputs["labels"])
    mask, observation_mask = inputs["gap_dense_mask"].astype(bool), inputs["gap_mask"].astype(bool)
    datasets, records = {}, {}
    time = float(manifest["common_time"])
    for name, path in manifest["jobs"].items():
        path = owned(path if isinstance(path, str) else path["path"])
        record_path, array_path = path / "record.json", path / "trajectories.npz"
        record = json.loads(record_path.read_text())
        validated = verification["jobs"][name]
        if validated.get("passed") is not True or validated["record_sha256"] != sha256(record_path):
            raise ValueError("record changed after verification: " + name)
        expected = record.get("output_hashes", record.get("hashes", {}))["trajectories.npz"]
        if sha256(array_path) != expected:
            raise ValueError("trajectory changed after verification: " + name)
        values = load_npz(array_path)
        if float(values["times"][-1]) != time or record.get("status") != "complete":
            raise ValueError("not a complete common endpoint: " + name)
        if not all(np.all(np.isfinite(value)) for value in values.values() if np.issubdtype(value.dtype, np.number)):
            raise ValueError("nonfinite saved array: " + name)
        datasets[name], records[name] = values, record
    def dense(name):
        return np.asarray(datasets[name]["dense_predictions"], dtype=np.float64).reshape(-1)
    def index(name, target):
        matches = np.flatnonzero(np.abs(datasets[name]["times"] - target) <= 1e-8)
        if len(matches) != 1:
            raise ValueError(f"no unique time {target} in {name}")
        return matches[0]
    def circle(name, target):
        return np.asarray(datasets[name]["predictions"][index(name, target), m:], dtype=np.float64)
    def mse(name):
        residual = np.asarray(datasets[name]["predictions"][-1, :m], dtype=np.float64) - inputs["labels"]
        return float(np.sum(inputs["probabilities"] * residual ** 2))
    seeds = [f"net_n8192_s{seed}" for seed in (11, 29, 47)]
    network_dense = np.mean([dense(name) for name in seeds], axis=0)
    network_gram = np.mean([np.asarray(datasets[name]["grams"][-1], dtype=np.float64) for name in seeds], axis=0)
    network_initial_gram = np.mean([np.asarray(datasets[name]["grams"][0], dtype=np.float64) for name in seeds], axis=0)
    rows = {}
    for name, values in datasets.items():
        windows = []
        for start, end in ((time-50, time-25), (time-25, time)):
            drift = norms(circle(name, end) - circle(name, start), observation_mask)
            loss_delta = abs(float(values["loss"][index(name, end)] - values["loss"][index(name, start)]))
            windows.append(dict(start=start, end=end, circle_max=drift["circle_max"], loss_change=loss_delta,
                                passed=drift["circle_max"] < .005 and loss_delta < .0005))
        rows[name] = dict(network_error=norms(dense(name) - network_dense, mask), training_mse=mse(name),
                          recorded_loss=float(values["loss"][-1]),
                          drift100=norms(circle(name, time) - circle(name, time-100), observation_mask),
                          plateau_windows=windows, plateau_passed=all(window["passed"] for window in windows),
                          gram_current_error_vs_network=gram_relative(values["grams"][-1], network_gram),
                          gram_own_frozen_error_vs_network=gram_relative(values["grams"][0], network_gram),
                          gram_change_relative_to_own_initial=gram_relative(values["grams"][-1], values["grams"][0]),
                          paired_hidden_movement=np.asarray(values["movement"][-1], dtype=np.float64).tolist())
    controls = {}
    def add_control(name, left, right, category, limit=None):
        metrics = norms(dense(left) - dense(right), mask)
        loss_difference = abs(mse(left) - mse(right))
        controls[name] = dict(**metrics, left=left, right=right, category=category,
                              loss_difference=loss_difference, circle_limit=limit,
                              passed=True if limit is None else metrics["circle_max"] <= limit and loss_difference <= .001)
    for order in (1, 3, 5):
        add_control(f"N{order}_main_to_fine", f"cl_N{order}_main", f"cl_N{order}_fine", "earlier_quadrature")
        add_control(f"N{order}_fine_to_finest", f"cl_N{order}_fine", f"cl_N{order}_finest", "quadrature", .025)
        add_control(f"N{order}_half_step", f"cl_N{order}_main", f"cl_N{order}_half", "step", .002)
    add_control("network_half_step", seeds[0], "net_n8192_s11_half", "step", .002)
    add_control("network_precision", "net_n4096_s11", "net_n4096_s11_double", "precision", .002)
    add_control("network_width", seeds[0], "net_n4096_s11", "width")
    for left, right in itertools.combinations(seeds, 2):
        add_control(left + "_vs_" + right, left, right, "seed")
    current_controls = {name: value for name, value in controls.items() if value["category"] != "earlier_quadrature"}
    uncertainty = {metric: dict(value=max(value[metric] for value in current_controls.values()),
                               witness=max(current_controls, key=lambda name: current_controls[name][metric]))
                   for metric in ("gap_rms", "gap_max")}
    with_drift = dict(current_controls)
    with_drift.update({"drift100_"+name: row["drift100"] for name, row in rows.items()})
    drift_uncertainty = {metric: dict(value=max(value[metric] for value in with_drift.values()),
                                     witness=max(with_drift, key=lambda name: with_drift[name][metric]))
                         for metric in ("gap_rms", "gap_max")}
    pairs = {}
    for left, right in ((1, 3), (3, 5)):
        result = {}
        for level in ("main", "fine", "finest"):
            a, b = f"cl_N{left}_{level}", f"cl_N{right}_{level}"
            metrics = norms(dense(a) - dense(b), mask)
            previous = norms(circle(a, time-100) - circle(b, time-100), observation_mask)
            metrics.update(visible=metrics["gap_rms"] >= .075 and metrics["gap_max"] >= .15,
                           previous100=previous, previous100_visible=previous["gap_rms"] >= .075 and previous["gap_max"] >= .15)
            result[level] = metrics
        result["fivefold_numerical_margin"] = all(min(result[level][metric] for level in ("main", "finest")) > 5*uncertainty[metric]["value"]
                                                  for metric in ("gap_rms", "gap_max"))
        result["fivefold_margin_including_drift"] = all(min(result[level][metric] for level in ("main", "finest")) > 5*drift_uncertainty[metric]["value"]
                                                        for metric in ("gap_rms", "gap_max"))
        train_names = [f"cl_N{left}_main", f"cl_N{right}_main", f"cl_N{left}_finest", f"cl_N{right}_finest"] + seeds
        result["max_training_mse"] = max(mse(name) for name in train_names)
        result["max_pair_training_rms"] = max(float(np.sqrt(np.mean((datasets[a]["predictions"][-1, :m] - datasets[b]["predictions"][-1, :m])**2)))
                                               for a, b in itertools.combinations(train_names, 2))
        pairs[f"{left}-{right}"] = result
    mean_training_prediction = np.mean([datasets[name]["predictions"][-1, :m] for name in seeds], axis=0)
    reference = dict(mean_seed_mse=float(np.mean([mse(name) for name in seeds])),
                     mse_of_mean_prediction=float(np.mean((mean_training_prediction - inputs["labels"])**2)),
                     seed_pointwise_range_max=float(np.max(np.ptp([dense(name) for name in seeds], axis=0))),
                     gram_frozen_network_baseline_error=gram_relative(network_initial_gram, network_gram),
                     gram_current_change_relative_initial=gram_relative(network_gram, network_initial_gram))
    return dict(time=time, manifest=str(manifest_path), manifest_sha256=sha256(manifest_path),
                verification=str(verification_path), verification_sha256=sha256(verification_path),
                audit_source_sha256=sha256(__file__), rows=rows, pairs=pairs, controls=controls,
                numerical_controls_passed=all(value["passed"] for value in current_controls.values()),
                numerical_uncertainty=uncertainty, uncertainty_with_drift=drift_uncertainty,
                all_plateaus_passed=all(row["plateau_passed"] for row in rows.values()),
                all_drift100_passed=all(row["drift100"]["circle_max"] <= .01 for row in rows.values()),
                reference=reference,
                definitions={"gram_current_error_vs_network": "||G_model(T)-mean_seed G_net(T)||_F / ||mean_seed G_net(T)||_F, separately for both hidden layers",
                             "gram_own_frozen_error_vs_network": "||G_model(0)-mean_seed G_net(T)||_F / ||mean_seed G_net(T)||_F",
                             "gram_change_relative_to_own_initial": "||G_model(T)-G_model(0)||_F / ||G_model(0)||_F",
                             "gap": "fixed open arcs (104,166) and (284,346) degrees; 1440-point endpoint panel",
                             "drift": "whole-circle 720-point saved panel over the last 100 physical time units"},
                scope="Independent read-only saved-array audit. Shape distance, reference error and settling are separate quantities.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--verification", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    out = owned(args.out)
    if out.exists():
        raise ValueError("audit output must be fresh")
    result = audit(args.manifest, args.verification)
    out.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    names = [f"cl_N{n}_main" for n in (1, 3, 5)] + [f"net_n8192_s{s}" for s in (11, 29, 47)]
    print(json.dumps(dict(time=result["time"], numerical_controls_passed=result["numerical_controls_passed"],
                          all_plateaus_passed=result["all_plateaus_passed"],
                          rows={name:result["rows"][name] for name in names}, pairs=result["pairs"],
                          controls=result["controls"], reference=result["reference"]), indent=2))


if __name__ == "__main__":
    main()
