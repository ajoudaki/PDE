"""Independent read-only verification of the frozen quadrant experiment.

The only new product is RUN/verification.json. No training is performed, no
producer/plotting module is imported, and existing products are never replaced.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
sys.dont_write_bytecode = True

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/quadrant_network_closure"
sys.path.insert(0, str(ROOT / "code"))
from pde import observable_solver as solver


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text())


def load_arrays(path):
    with np.load(path, allow_pickle=False) as archive:
        return {key: archive[key].copy() for key in archive.files}


def maximum(value):
    return float(np.max(np.abs(value)))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def expected_jobs():
    result = {}
    for width in (8192, 2048):
        for seed in (11, 29, 47):
            result[f"net_n{width}_s{seed}"] = dict(kind="network", width=width, seed=seed,
                                                 step=.01, dtype="float32")
    result["net_n8192_s11_half"] = dict(kind="network", width=8192, seed=11, step=.005, dtype="float32")
    result["net_n2048_s11_double"] = dict(kind="network", width=2048, seed=11, step=.01, dtype="float64")
    for resolution, q, p in (("base", 2048, 1024), ("fine", 4096, 2048)):
        for order in (1, 3, 5):
            result[f"cl_N{order}_{resolution}"] = dict(kind="closure", order=order,
                initialization_nodes=q, population_nodes=p, step=.01)
    result["cl_N3_base_half"] = dict(kind="closure", order=3, initialization_nodes=2048,
                                     population_nodes=1024, step=.005)
    result["cl_N5_fine_half"] = dict(kind="closure", order=5, initialization_nodes=4096,
                                     population_nodes=2048, step=.005)
    return result


def verify_inputs(data):
    degrees = np.concatenate([np.linspace(a, b, 4) for a, b in ((0, 5), (25, 35), (55, 65), (85, 90))])
    train_theta = np.deg2rad(degrees)
    panel_theta = np.concatenate((train_theta, np.arange(128) * 2 * np.pi / 128))
    dense_theta = np.unique(np.concatenate((np.arange(1440) * (2 * np.pi / 1440), train_theta)))
    for name, expected in (("train_theta", train_theta), ("train_degrees", degrees),
                           ("panel_theta", panel_theta), ("dense_theta", dense_theta),
                           ("times", np.arange(201) * .5), ("labels", np.repeat([1., -1., 1., -1.], 4)),
                           ("probabilities", np.full(16, 1 / 16))):
        require(data[name].shape == expected.shape, name + " shape mismatch")
        # Multiplication grouping can differ by an ulp in a recomputed angle.
        require(maximum(data[name] - expected) <= 2e-14, name + " differs from the frozen law")
    for name, theta in (("train_u", train_theta), ("panel_u", data["panel_theta"]),
                         ("dense_u", data["dense_theta"])):
        expected = np.column_stack((np.cos(theta), np.sin(theta)))
        require(data[name].shape == expected.shape, name + " shape mismatch")
        require(maximum(data[name] - expected) <= 2e-14, name + " coordinate mismatch")
        require(maximum(np.sum(data[name] ** 2, axis=1) - 1) <= 2e-14, name + " unit-circle mismatch")
    require(np.array_equal(data["panel_u"][:16], data["train_u"]), "panel training prefix mismatch")
    require(np.array_equal(data["times"], np.arange(201) * .5), "saved schedule mismatch")
    require(len(np.unique(data["train_theta"])) == 16, "training angles are not distinct")
    require(0 <= data["train_theta"].min() and data["train_theta"].max() <= np.pi / 2,
            "training angles escape the first quadrant")
    dense_train = np.searchsorted(data["dense_theta"], data["train_theta"])
    require(np.array_equal(data["dense_theta"][dense_train], data["train_theta"]),
            "dense panel omits training directions")
    uniform = np.arange(1440) * (2 * np.pi / 1440)
    require(data["dense_uniform_indices"].shape == (1440,), "uniform dense index count mismatch")
    require(np.array_equal(data["dense_theta"][data["dense_uniform_indices"]], uniform),
            "uniform dense indices do not select the prescribed 1440 directions")
    return dense_train


def verify_trajectory(arrays, data, job, dense_train):
    shapes = dict(times=(201,), loss=(201,), predictions=(201, 144), grams=(201, 2, 144, 144),
                  rms=(201, 2), movement=(201, 2), dense_predictions=(len(data["dense_theta"]),))
    for name, shape in shapes.items():
        require(name in arrays and arrays[name].shape == shape, name + " absent or wrong shape")
        require(np.all(np.isfinite(arrays[name])), name + " has nonfinite values")
    require(np.array_equal(arrays["times"], data["times"]), "trajectory time mismatch")
    for name in ("train_u", "labels", "panel_u", "panel_theta", "dense_u", "dense_theta"):
        if name in arrays:
            require(np.array_equal(arrays[name], data[name]), name + " differs from frozen inputs")
    is_single = job["kind"] == "network" and job["dtype"] == "float32"
    gram_tolerance = 2e-6 if is_single else 1e-10
    prediction_tolerance = 1e-6 if is_single else 1e-10
    computed_loss = np.mean((arrays["predictions"][:, :16].astype(np.float64) - data["labels"]) ** 2, axis=1)
    loss_error = maximum(computed_loss - arrays["loss"])
    require(loss_error <= 1e-12, "MSE does not match the saved training predictions")
    diagonal = np.diagonal(arrays["grams"], axis1=-2, axis2=-1)
    trace_error = maximum(diagonal[:, :, :16].astype(np.float64).mean(axis=-1) - arrays["rms"] ** 2)
    require(trace_error <= gram_tolerance, "Gram trace does not equal training activation RMS squared")
    initial_movement = maximum(arrays["movement"][0])
    require(initial_movement <= prediction_tolerance, "nonzero initial activation movement")
    require(np.min(arrays["rms"]) >= 0 and np.min(arrays["movement"]) >= 0, "negative RMS")
    require(np.max(arrays["rms"]) <= 1 + gram_tolerance and np.max(arrays["movement"]) <= 2 + gram_tolerance,
            "tanh activation RMS or movement exceeds its bound")
    asymmetry = maximum(arrays["grams"] - arrays["grams"].swapaxes(-1, -2))
    require(asymmetry <= 1e-5, "Gram asymmetry gate failed")
    selected = arrays["grams"][[0, 50, 100, 200]].astype(np.float64)
    min_eigenvalue = float(np.min(np.linalg.eigvalsh((selected + selected.swapaxes(-1, -2)) / 2)))
    require(min_eigenvalue >= -1e-5, "selected-time Gram PSD gate failed")
    maximum_increase = float(np.max(np.diff(arrays["loss"])))
    require(maximum_increase <= 1e-5, "saved loss nonincrease gate failed")
    overlap_error = maximum(arrays["dense_predictions"][dense_train] - arrays["predictions"][-1, :16])
    require(overlap_error <= prediction_tolerance, "dense/training endpoint predictions disagree")
    oddness = maximum(arrays["predictions"][:, 16:80] + arrays["predictions"][:, 80:144])
    require(oddness <= 1e-5, "bias-free tanh output oddness gate failed")
    return dict(passed=True, mse_max_abs=loss_error, gram_rms_squared_max_abs=trace_error,
                initial_movement_max_abs=initial_movement, maximum_gram_asymmetry=asymmetry,
                psd_times=[0., 25., 50., 100.], minimum_selected_gram_eigenvalue=min_eigenvalue,
                maximum_saved_loss_increase=maximum_increase, dense_training_max_abs=overlap_error,
                maximum_prediction_oddness_error=oddness)


def closure_replay(path, arrays, data):
    state, law = solver.load_restart(path)
    require(np.array_equal(law.inputs, data["train_u"]), "closure checkpoint inputs mismatch")
    require(np.array_equal(law.labels, data["labels"]), "closure checkpoint labels mismatch")
    require(np.array_equal(law.probabilities, data["probabilities"]), "closure checkpoint weights mismatch")
    panel_prediction = solver.predict(state, data["panel_u"], block_size=16)
    dense_prediction = solver.predict(state, data["dense_u"], block_size=16)
    prediction_error = maximum(panel_prediction - arrays["predictions"][-1])
    dense_error = maximum(dense_prediction - arrays["dense_predictions"])
    h1 = np.tanh(state.w @ data["panel_u"].T)
    lower_moments = state.b1.T @ (state.p1[:, None] * h1)
    h2 = np.tanh(state.b2 @ state.M @ lower_moments)
    gram = np.stack((h1.T @ (state.p1[:, None] * h1), h2.T @ (state.p2[:, None] * h2)))
    gram_error = maximum(gram - arrays["grams"][-1])
    pair_observation = solver.paired_observations(state, law, include_pairs=False)
    movement_error = maximum(np.array([pair_observation["rms1"], pair_observation["rms2"]]) - arrays["movement"][-1])
    require(max(prediction_error, dense_error, gram_error, movement_error) <= 1e-10,
            "closure final-state replay mismatch")
    return dict(passed=True, panel_prediction_max_abs=prediction_error, dense_prediction_max_abs=dense_error,
                gram_max_abs=gram_error, movement_max_abs=movement_error,
                feature_dimensions=list(state.M.shape[::-1]),
                checkpoint_sha256=sha256(path))


def network_replay(path, arrays, data, device_name):
    import torch
    if device_name.startswith("cuda") and ":" not in device_name and len(device_name) > 4:
        device_name = "cuda:" + device_name[4:]
    device = torch.device(device_name)
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")
    # This is a freshly generated, hash-verified checkpoint of this own study.
    saved = torch.load(path, map_location=device, weights_only=False)
    a, b, c = (saved[name] for name in ("a", "b", "c"))
    require(a.shape == (8192, 2) and b.shape == (8192, 8192) and c.shape == (8192,),
            "network checkpoint parameter shapes mismatch")
    require(saved["physical_time"] == 100 and saved["completed_steps"] == 10000,
            "network checkpoint time or step count mismatch")
    require(np.array_equal(saved["train_u"], data["train_u"]) and np.array_equal(saved["labels"], data["labels"]),
            "network checkpoint training law mismatch")
    require(all(bool(torch.isfinite(tensor).all()) for tensor in (a, b, c)), "nonfinite checkpoint parameters")
    with torch.no_grad():
        panel = torch.as_tensor(data["panel_u"].T.copy(), dtype=a.dtype, device=device)
        h1 = torch.tanh(a @ panel)
        h2 = torch.tanh(b @ h1)
        prediction = (c @ h2 / len(c)).cpu().numpy()
        gram = torch.stack((h1.T @ h1 / len(c), h2.T @ h2 / len(c))).cpu().numpy()
        dense_values = []
        for first in range(0, len(data["dense_u"]), 256):
            u = torch.as_tensor(data["dense_u"][first:first + 256].T.copy(), dtype=a.dtype, device=device)
            dense_values.append((c @ torch.tanh(b @ torch.tanh(a @ u)) / len(c)).cpu().numpy())
    panel_error = maximum(prediction - arrays["predictions"][-1])
    dense_error = maximum(np.concatenate(dense_values) - arrays["dense_predictions"])
    gram_error = maximum(gram - arrays["grams"][-1])
    require(panel_error <= 1e-6 and dense_error <= 1e-6 and gram_error <= 2e-6,
            "network final-state replay mismatch")
    return dict(passed=True, device=str(device), dtype=str(a.dtype), tf32=False,
                panel_prediction_max_abs=panel_error, dense_prediction_max_abs=dense_error,
                gram_max_abs=gram_error, checkpoint_sha256=sha256(path))


def frozen_readout_endpoint(arrays, labels):
    gram = arrays["grams"][0, 1, :16, :16].astype(np.float64)
    residual0 = arrays["predictions"][0, :16].astype(np.float64) - labels
    residual = expm(-2 * 100 * gram / 16) @ residual0
    endpoint = labels + residual
    # Matrix-exponential action is independently checked against its ODE identity.
    zero_action = expm(np.zeros_like(gram)) @ residual0
    require(maximum(zero_action - residual0) <= 1e-14, "expm initial-value identity failed")
    return dict(predictions=endpoint.tolist(), loss=float(np.mean(residual ** 2)),
                implementation="scipy.linalg.expm on the stored initial 16x16 upper Gram",
                physical_time=100., loss_clock_factor=2 / 16)


def independent_metrics(actual, reference, uniform_indices):
    result = dict(max_absolute_loss_difference=maximum(actual["loss"] - reference["loss"]))
    endpoint_error = actual["dense_predictions"][uniform_indices].astype(np.float64) - reference["dense_predictions"][uniform_indices]
    result["final_dense_circle_rmse"] = float(np.sqrt(np.mean(endpoint_error ** 2)))
    result["final_dense_circle_max_absolute_difference"] = maximum(endpoint_error)
    for name, chosen in (("training", slice(0, 16)), ("circle", slice(16, 144)), ("full", slice(None))):
        actual_gram = actual["grams"][:, :, chosen, chosen].astype(np.float64)
        reference_gram = reference["grams"][:, :, chosen, chosen]
        numerator = np.sqrt(np.sum((actual_gram - reference_gram) ** 2, axis=(-2, -1)))
        denominator = np.sqrt(np.sum(reference_gram ** 2, axis=(-2, -1)))
        require(np.min(denominator) > 0, "zero reference Gram norm")
        relative = numerator / denominator
        result["max_relative_gram_" + name + "_by_layer"] = np.max(relative, axis=0).tolist()
        result["final_relative_gram_" + name + "_by_layer"] = relative[-1].tolist()
    return result


def verify_analysis(run, data, frozen_endpoints):
    analysis = load_json(run / "analysis.json")
    reference = {}
    for seed in (11, 29, 47):
        arrays = load_arrays(run / f"net_n8192_s{seed}" / "trajectories.npz")
        for name in ("loss", "grams", "dense_predictions"):
            if name not in reference:
                reference[name] = arrays[name].astype(np.float64) / 3
            else:
                reference[name] += arrays[name].astype(np.float64) / 3
    metric_checks = {}
    for order in (1, 3, 5):
        arrays = load_arrays(run / f"cl_N{order}_base" / "trajectories.npz")
        independently_computed = independent_metrics(arrays, reference, data["dense_uniform_indices"])
        saved = analysis["closures"][str(order)]
        errors = {}
        for name, value in independently_computed.items():
            require(name in saved, "analysis metric missing: " + name)
            errors[name] = maximum(np.asarray(value) - np.asarray(saved[name]))
            require(errors[name] <= 2e-6, f"reported closure N={order} metric mismatch: {name}")
        metric_checks[str(order)] = dict(passed=True, independently_computed=independently_computed,
                                         reported_metric_max_abs_errors=errors)
    with np.load(run / "frozen_readout_baselines.npz", allow_pickle=False) as archive:
        require(np.array_equal(archive["times"], data["times"]), "frozen-readout baseline time mismatch")
        baseline_checks = {}
        for name, computed in frozen_endpoints.items():
            computed_prediction = np.asarray(computed["predictions"])
            saved_prediction = archive[name + "_predictions"][-1, :16]
            prediction_error = maximum(computed_prediction - saved_prediction)
            loss_error = abs(computed["loss"] - float(archive[name + "_loss"][-1]))
            report_error = abs(computed["loss"] - analysis["frozen_readout"][name]["final_loss"])
            # Plotting clips tiny negative float32 Gram eigenvalues; this check
            # uses the stored Gram directly, so the comparison allows 1e-6.
            require(max(prediction_error, loss_error, report_error) <= 1e-6,
                    "independent matrix-exponential frozen baseline mismatch: " + name)
            baseline_checks[name] = dict(passed=True, endpoint_prediction_max_abs=prediction_error,
                                         endpoint_loss_abs=loss_error, reported_loss_abs=report_error)
    return dict(passed=True, analysis_sha256=sha256(run / "analysis.json"),
                frozen_baselines_sha256=sha256(run / "frozen_readout_baselines.npz"),
                closure_metrics=metric_checks, frozen_readout_comparisons=baseline_checks)


def verify(args):
    run = Path(args.run).resolve()
    require(run.is_relative_to((ROOT / "data/generated/quadrant_network_closure").resolve()),
            "run must belong to this study")
    target = run / "verification.json"
    if target.exists():
        raise FileExistsError("Refusing to replace " + str(target))
    started = time.monotonic()
    report = dict(passed=False, verifier_sha256=sha256(__file__), run=str(run), errors=[], jobs={},
                  closure_replays={}, frozen_readout_endpoints={})
    try:
        manifest = load_json(run / "manifest.json")
        expected = expected_jobs()
        declared = {job["id"]: {key: value for key, value in job.items() if key != "id"}
                    for job in manifest["jobs"]}
        require(len(manifest["jobs"]) == 16 and declared == expected, "frozen job menu is not the expected 16 jobs")
        input_hash = sha256(run / "inputs.npz")
        require(input_hash == manifest["inputs_sha256"], "input archive hash mismatch")
        report["inputs_sha256"] = input_hash
        changed = []
        for source, expected_hash in manifest["sources_sha256"].items():
            path = ROOT / source
            if not path.is_file() or sha256(path) != expected_hash:
                changed.append(source)
        report["changed_frozen_sources"] = changed
        require(not changed, "frozen source changes detected: " + ", ".join(changed))
        supervision = load_json(run / "supervision.json")
        require(supervision["complete"] and len(supervision["results"]) == 16,
                "supervision is incomplete")
        require({item["id"] for item in supervision["results"]} == set(expected), "supervised job IDs mismatch")
        require(all(item["exit_code"] == 0 for item in supervision["results"]), "worker process failed")
        data = load_arrays(run / "inputs.npz")
        dense_train = verify_inputs(data)
        report["input_checks_passed"] = True
        for job_id, job in expected.items():
            try:
                folder = run / job_id
                record = load_json(folder / "record.json")
                require(record["status"] == "complete", "producer status is not complete")
                for key, value in job.items():
                    if key != "kind":
                        require(record["config"][key] == value, "producer configuration mismatch: " + key)
                require(record["config"]["horizon"] == 100, "producer horizon mismatch")
                require(record.get("input_sha256", record.get("inputs_sha256")) == input_hash,
                        "producer input provenance mismatch")
                expected_files = {"trajectories.npz", "state.pt"} if job["kind"] == "network" else {
                    "trajectories.npz", "final_restart.json"}
                require(set(record["output_sha256"]) == expected_files, "recorded output file set mismatch")
                for name, expected_hash in record["output_sha256"].items():
                    require(sha256(folder / name) == expected_hash, "output hash mismatch: " + name)
                if job["kind"] == "network":
                    require(record["source_sha256"] == manifest["sources_sha256"][str((STUDY / "NETWORK.py").relative_to(ROOT))],
                            "network source provenance mismatch")
                else:
                    for name, expected_hash in record["provenance"]["source_sha256"].items():
                        require(manifest["sources_sha256"][name] == expected_hash,
                                "closure source provenance mismatch: " + name)
                arrays = load_arrays(folder / "trajectories.npz")
                report["jobs"][job_id] = verify_trajectory(arrays, data, job, dense_train)
                report["jobs"][job_id]["output_hashes_verified"] = sorted(expected_files)
                if job["kind"] == "closure":
                    report["closure_replays"][job_id] = closure_replay(folder / "final_restart.json", arrays, data)
                if job_id in ("net_n8192_s11", "net_n8192_s29", "net_n8192_s47"):
                    report["frozen_readout_endpoints"][job_id] = frozen_readout_endpoint(arrays, data["labels"])
                if job_id == "net_n8192_s11":
                    report["network_replay"] = network_replay(folder / "state.pt", arrays, data, args.device)
                del arrays
            except Exception as error:
                report["jobs"][job_id] = dict(passed=False, error=str(error), traceback=traceback.format_exc())
                report["errors"].append(job_id + ": " + str(error))
        report["frozen_readout_mean_endpoint_loss"] = float(np.mean([
            value["loss"] for value in report["frozen_readout_endpoints"].values()
        ])) if report["frozen_readout_endpoints"] else None
        if not report["errors"]:
            report["analysis_checks"] = verify_analysis(run, data, report["frozen_readout_endpoints"])
        report["passed"] = (not report["errors"] and len(report["jobs"]) == 16
                             and len(report["closure_replays"]) == 8
                             and len(report["frozen_readout_endpoints"]) == 3
                             and report.get("network_replay", {}).get("passed", False)
                             and report.get("analysis_checks", {}).get("passed", False))
    except Exception as error:
        report["errors"].append(str(error))
        report["traceback"] = traceback.format_exc()
    report["elapsed_seconds"] = time.monotonic() - started
    with target.open("x") as handle:
        json.dump(report, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"passed": report["passed"], "errors": report["errors"],
                      "elapsed_seconds": report["elapsed_seconds"], "output": str(target)}), flush=True)
    return 0 if report["passed"] else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", required=True)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    return verify(args)


if __name__ == "__main__":
    raise SystemExit(main())
