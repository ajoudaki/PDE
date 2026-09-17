"""Independent read-only arithmetic/trajectory audit of eight PCA benchmarks."""
import hashlib
import json
from pathlib import Path
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/generated/first_order_dimension_mnist"
HERE = BASE / "pca_speed_check"
EXPECTED_HASH = {
    "original": "bc18a91521dff93f563a3828a0ba3d941ac7f23436978db7810aeeee06ef8c7f",
    "pca": "420da6f2ca6fb3c6163d9d91f32ddf95b1c3258c98f5e26cea6860f43dfa1b54",
}
FIELDS = ("initialization_seconds", "integration_seconds", "training_wall_seconds",
          "moving_state_bytes", "retained_model_bytes",
          "retained_model_and_best_checkpoint_bytes", "peak_allocated_bytes",
          "peak_with_controls_and_test_bytes")
RATIO_FIELDS = ("integration_seconds", "training_wall_seconds", "moving_state_bytes",
                "retained_model_bytes", "retained_model_and_best_checkpoint_bytes",
                "peak_allocated_bytes", "peak_with_controls_and_test_bytes")
SERIES = ("train_predictions", "val_predictions", "gram1", "gram2")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_comparison(first, second, prefix=False):
    report = {}
    with np.load(first, allow_pickle=False) as left, np.load(second, allow_pickle=False) as right:
        times = left["times"]
        indices = np.asarray([np.flatnonzero(right["times"] == t)[0] for t in times]) if prefix else slice(None)
        assert np.array_equal(times, right["times"][indices])
        for key in SERIES:
            a, b = left[key], right[key][indices]
            same = bool(a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes())
            report[key] = {"bitwise_equal": same, "shape": list(a.shape), "dtype": str(a.dtype),
                           "maximum_absolute_difference": float(np.max(np.abs(a.astype(np.float64) - b.astype(np.float64))))}
        for key in ("train_y", "val_y", "panel_u"):
            a, b = left[key], right[key]
            report[key] = {"bitwise_equal": bool(a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes())}
    return report


def main():
    started = time.perf_counter()
    names = [f"{representation}_{model}_r{repetition}"
             for representation in ("original", "pca")
             for model in ("network", "closure") for repetition in (1, 2)]
    missing = [name for name in names if not (BASE / "pca_speed" / name / "summary.json").exists()]
    if missing:
        print(json.dumps({"pending": missing}))
        return
    results, gates, files = {}, {}, {}
    by_gpu = {}
    for name in names:
        path = BASE / "pca_speed" / name
        summary = json.loads((path / "summary.json").read_text())
        config = json.loads((path / "config.json").read_text())
        representation, model, repetition = name.split("_")
        repetition = int(repetition[1:])
        d = 784 if representation == "original" else 240
        n, stored = 4096, 2048
        step = 0.25 if model == "network" else 0.125
        expected_gpu = (0 if model == "network" else 1) if repetition == 1 else (1 if model == "network" else 0)
        moving = 4 * (n * d + n * n + n) if model == "network" else 4 * (stored * (d + 1) + 2 * d * d)
        retained = 2 * moving if model == "network" else 4 * (8 * stored * d + 3 * stored + 4 * d * d)
        with np.load(path / "observations.npz", allow_pickle=False) as arrays:
            saved_dimensions = arrays["panel_u"].shape[1]
            clock_exact = np.array_equal(arrays["times"], np.arange(0, 101, 10, dtype=float))
        flags = {
            "summary_configuration_matches_config_file": config == summary["configuration"],
            "correct_model_width_seed_task": config["model"] == model and config["width"] == n and config["seed"] == 1729 and config["task"] == "mnist",
            "float32_tf32_disabled": config["dtype"] == "float32" and config["environment"]["tf32"] is False,
            "correct_gpu_crossover": config["gpu"] == expected_gpu and config["environment"]["device"] == f"cuda:{expected_gpu}",
            "correct_step_and_count": config["step"] == step and summary["steps"] == 100 / step,
            "complete_fixed_horizon": config["horizon"] == 100 and summary["final_time"] == 100 and summary["stop_reason"] == "horizon" and not config["continue_validation"],
            "correct_data_dimension": summary["data"]["metadata"]["dimension"] == d and saved_dimensions == d,
            "correct_dataset_hash": summary["data"]["metadata"]["dataset_sha256"] == EXPECTED_HASH[representation],
            "correct_block_and_no_precision_probe": config["block"] == 2048 and not config["precision_probe"],
            "correct_observation_clock": bool(clock_exact),
            "integration_timing_positive_and_bounded_by_loop": 0 < summary["integration_seconds"] <= summary["training_wall_seconds"],
            "endpoint_cumulative_time_matches_total": summary["observations"][-1]["cumulative_integration_seconds"] == summary["integration_seconds"],
            "moving_bytes_match_formula": summary["moving_state_bytes"] == moving,
            "retained_bytes_match_formula": summary["retained_model_bytes"] == retained,
            "retained_plus_best_bytes_match_formula": summary["retained_model_and_best_checkpoint_bytes"] == retained + moving,
            "peak_fields_ordered": summary["peak_with_controls_and_test_bytes"] >= summary["peak_allocated_bytes"] >= retained + moving,
        }
        if model == "closure":
            init = summary["initialization"]
            flags["correct_folded_population_and_dimensions"] = (
                init["input_dimension"] == d and init["nominal_population_nodes"] == n
                and init["stored_population_nodes"] == stored and init["sign_folded"] is True
                and init["population_rule"] == "antithetic" and init["feature_dimensions"] == [2*d, d])
        gates[name] = flags
        results[name] = {"gpu": expected_gpu, "dimension": d, "steps": summary["steps"],
                         "step": step, **{field: summary[field] for field in FIELDS},
                         "integration_seconds_per_step": summary["integration_seconds"] / summary["steps"],
                         "integration_seconds_per_physical_time": summary["integration_seconds"] / summary["final_time"],
                         "dataset_sha256": summary["data"]["metadata"]["dataset_sha256"],
                         "runtime_environment": config["environment"],
                         "implementation_hashes": {key: config["source_sha256"][key] for key in ("RUN.py", "P1_ENGINE.py", "NETWORK_ENGINE.py", "P1_INITIALIZATION.py")}}
        by_gpu[(representation, model, expected_gpu)] = name
        files[name] = {"summary_sha256": digest(path / "summary.json"), "config_sha256": digest(path / "config.json"),
                       "observations_sha256": digest(path / "observations.npz")}
    ratios = {}
    comparisons = (
        ("pca_closure_over_pca_network", ("pca", "closure"), ("pca", "network")),
        ("original_closure_over_original_network", ("original", "closure"), ("original", "network")),
        ("pca_closure_over_original_network", ("pca", "closure"), ("original", "network")),
        ("pca_closure_over_original_closure", ("pca", "closure"), ("original", "closure")),
        ("pca_network_over_original_network", ("pca", "network"), ("original", "network")),
    )
    for label, numerator, denominator in comparisons:
        gpu_ratios = []
        for gpu in (0, 1):
            first, second = by_gpu[(*numerator, gpu)], by_gpu[(*denominator, gpu)]
            gpu_ratios.append({"gpu": gpu, "numerator": first, "denominator": second,
                               **{key: results[first][key] / results[second][key] for key in RATIO_FIELDS}})
        ratios[label] = {"per_gpu": gpu_ratios,
                         "minimum": {key: min(row[key] for row in gpu_ratios) for key in RATIO_FIELDS},
                         "maximum": {key: max(row[key] for row in gpu_ratios) for key in RATIO_FIELDS},
                         "arithmetic_mean": {key: float(np.mean([row[key] for row in gpu_ratios])) for key in RATIO_FIELDS}}
    repetition, original_prefix, dispersion = {}, {}, {}
    for representation in ("original", "pca"):
        for model in ("network", "closure"):
            label = f"{representation}_{model}"
            first = BASE / "pca_speed" / f"{label}_r1" / "observations.npz"
            second = BASE / "pca_speed" / f"{label}_r2" / "observations.npz"
            repetition[label] = raw_comparison(first, second)
            times = [results[f"{label}_r{rep}"]["integration_seconds"] for rep in (1, 2)]
            relative_range = (max(times) - min(times)) / float(np.mean(times))
            dispersion[label] = {"minimum_seconds": min(times), "maximum_seconds": max(times),
                                 "relative_range_over_mean": relative_range,
                                 "above_15_percent": relative_range > 0.15}
            if representation == "original":
                original_prefix[model] = raw_comparison(first, BASE / "main4096" / f"{model}_1729" / "observations.npz", prefix=True)
    implementation_equal = all(result["implementation_hashes"] == next(iter(results.values()))["implementation_hashes"] for result in results.values())
    environment_equal = all({k: v for k,v in result["runtime_environment"].items() if k != "device"} == {k: v for k,v in next(iter(results.values()))["runtime_environment"].items() if k != "device"} for result in results.values())
    passed = (all(all(flags.values()) for flags in gates.values()) and implementation_equal and environment_equal
              and all(all(item["bitwise_equal"] for item in case.values()) for case in repetition.values())
              and all(all(item["bitwise_equal"] for item in case.values()) for case in original_prefix.values()))
    report = {"passed": passed, "run_gates": gates, "runs": results, "same_gpu_ratios": ratios,
              "timing_dispersion": dispersion, "repeated_runs": repetition, "original_main_T100_prefix": original_prefix,
              "implementation_hashes_identical": implementation_equal, "runtime_environment_equal_except_device": environment_equal,
              "input_hashes": files, "check_source_sha256": digest(Path(__file__)),
              "audit_seconds": time.perf_counter() - started,
              "limits": "Observed fixed T100 benchmarks only; no asymptotic complexity, accuracy or convergence inference"}
    (HERE / "check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"passed": passed, "seconds": report["audit_seconds"], "timing_dispersion": dispersion,
                      "ratios": {key: {"minimum": row["minimum"]["integration_seconds"], "maximum": row["maximum"]["integration_seconds"]} for key, row in ratios.items()}}))


if __name__ == "__main__":
    main()
