"""Export a compact radial viewer from the two closed, saved campaigns.

No training is performed. Circle curves are periodic linear resamples of saved
panels; time interpolation is a display interpolation, not a recovered flow.
Training predictions retain full precision so matched-loss interpolation can
use their actual weighted MSE, including the mean per-seed network MSE.
"""

import argparse
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np

from ANALYZE import FrozenKernel
from NTK import kernel


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_circle_spectral_mechanism"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sample(values, count):
    """Periodic linear resampling on uniform grids, without angular rotation."""
    values = np.asarray(values, dtype=float)
    source_count = values.shape[-1]
    locations = np.arange(count, dtype=float) * source_count / count
    left = np.floor(locations).astype(int)
    blend = locations - left
    return (values[..., left] * (1 - blend)
            + values[..., (left + 1) % source_count] * blend)


def curves_list(values):
    return np.round(values, 7).tolist()


def error(candidate, reference):
    difference = np.asarray(candidate) - reference
    return {"maxAbs": float(np.max(np.abs(difference))),
            "relativeRms": float(np.sqrt(np.mean(difference**2))
                                 / max(np.sqrt(np.mean(np.asarray(reference)**2)), 1e-30))}


def empirical_loss(predictions, labels, weights):
    return np.sum((np.asarray(predictions) - labels)**2 * weights, axis=-1)


def run(output, preferred_samples=240):
    started = time.perf_counter()
    output = Path(output).resolve()
    if output.parent != GENERATED or output.exists():
        raise ValueError("output must be a fresh direct study-generated subdirectory")
    if preferred_samples not in (180, 240, 360):
        raise ValueError("supported display grids are 180, 240 and 360")
    closure_root = GENERATED / "campaign_001"
    network_root = GENERATED / "network_comparison_001"
    closure_summary_path = closure_root / "analysis_final/summary.json"
    network_summary_path = network_root / "analysis_final/summary.json"
    closure_summary = json.loads(closure_summary_path.read_text())
    network_summary = json.loads(network_summary_path.read_text())
    inputs = {}

    def checked(path, expected=None):
        digest = sha(path)
        if expected is not None and digest != expected:
            raise ValueError("input hash mismatch: " + str(path))
        inputs[str(path.relative_to(ROOT))] = digest
        return digest

    checked(closure_summary_path)
    checked(network_summary_path)
    checked(closure_root / "manifest.json", closure_summary["manifest_sha256"])
    checked(network_root / "manifest.json", network_summary["provenance"]["manifest_sha256"])
    for name in ["ANALYZE.py", "NTK.py", "PLAN.md"]:
        checked(HERE / name, closure_summary["source_sha256"][str(HERE / name)])
    checked(HERE / "NET_PLAN.md",
            network_summary["provenance"]["source_sha256"][str(HERE / "NET_PLAN.md")])

    cases = {}
    raw_models = {}
    record_checks = []
    ntk_checks = []

    def read_model(root, name, analyzed, case, kind):
        record_path = root / name / "record.json"
        record = json.loads(record_path.read_text())
        expected_record = (closure_summary["input_hashes"][name]["record"]
                           if kind == "closure" else analyzed["record_sha256"])
        checked(record_path, expected_record)
        if record["status"] != "complete" or record["config"] != analyzed["config"]:
            raise ValueError("incomplete or mismatched raw record: " + name)
        checked(root / name / "config.json", record["outputs"]["config.json"])
        observed_path = root / name / "observations.npz"
        checked(observed_path, record["outputs"]["observations.npz"])
        with np.load(observed_path, allow_pickle=False) as saved:
            raw = {key: saved[key] for key in ["times", "loss", "predictions",
                                             "train_predictions", "dense_predictions"]}
            if kind == "closure":
                if not (np.array_equal(saved["labels"], case["labels"])
                        and np.allclose(saved["weights"], case["weights"], rtol=0, atol=1e-15)
                        and np.allclose(saved["angles"], np.deg2rad(case["anglesDegrees"]),
                                        rtol=0, atol=1e-14)):
                    raise ValueError("raw training-data mismatch: " + name)
        if not all(np.all(np.isfinite(value)) for value in raw.values()):
            raise ValueError("nonfinite data: " + name)
        times = raw["times"]
        if times[0] != 0 or not np.all(np.diff(times) > 0):
            raise ValueError("non-increasing physical clock: " + name)
        if (raw["predictions"].shape[0] != len(times)
                or raw["train_predictions"].shape != (len(times), len(case["labels"]))):
            raise ValueError("saved panel dimensions do not match: " + name)
        losses = empirical_loss(raw["train_predictions"], case["labels"], case["weights"])
        loss_error = float(np.max(np.abs(losses - raw["loss"])))
        if (loss_error > 1e-11 or abs(times[-1] - analyzed["final_time"]) > 1e-10
                or abs(losses[-1] - analyzed["final_loss"]) > 1e-11):
            raise ValueError("loss or final time mismatch: " + name)
        config = analyzed["config"]
        notes = []
        if kind == "closure":
            label = "N=" + str(config["order"])
            for control in closure_summary["controls"]:
                if control["right"] == name and not control["settled_endpoint_valid"]:
                    notes.append("Quadrature control failed the 2% circle tolerance: "
                                 + f"{100 * control['final']['relative_rms']:.2f}% relative RMS.")
            if not analyzed["available_controls"]:
                notes.append("No matched refinement control was recorded for this trajectory.")
        else:
            label = f"NN {config['width']} · seed {config['seed']}"
            notes.append("Actual finite network; its saved initial output is retained.")
        model = dict(id=name, label=label, kind=kind, times=times.tolist(),
                     losses=losses.tolist(), trainPredictions=raw["train_predictions"].tolist(),
                     finalTime=float(times[-1]), finalLoss=float(losses[-1]),
                     settled=bool(record["settled"]), notes=notes,
                     lossDefinition="weighted training MSE",
                     sourceAngularSamples=int(raw["predictions"].shape[-1]))
        if kind == "closure":
            model["order"] = config["order"]
        else:
            model.update(width=config["width"], seed=config["seed"])
        raw_models[name] = raw
        case["models"].append(model)
        record_checks.append(dict(id=name, rawLossMaxAbs=loss_error,
                                  savedFrameCount=len(times),
                                  savedPanelAngles=int(raw["predictions"].shape[-1]),
                                  firstPositiveTime=float(times[1]),
                                  firstPositiveLoss=float(losses[1])))

    for name, analyzed in closure_summary["records"].items():
        config = analyzed["config"]
        if config["control"] != "main":
            continue
        case_id = config["name"]
        if case_id not in cases:
            if config["kind"] == "pair":
                label = f"2 points · {config['delta']}° apart · midpoint {config['rotation']}°"
            else:
                label = f"{3 if config['kind'] == 'triple' else 4} points · {config['delta']}° spacing"
            if config["amplitude"] != 1:
                label += f" · A={config['amplitude']}"
            cases[case_id] = dict(id=case_id, label=label, kind=config["kind"],
                                 delta=config["delta"], rotation=config["rotation"],
                                 amplitude=config["amplitude"], anglesDegrees=config["angles_degrees"],
                                 labels=config["labels"], weights=[1 / len(config["labels"])] * len(config["labels"]),
                                 notes=[], models=[], ntkSource=name)
        read_model(closure_root, name, analyzed, cases[case_id], "closure")

    for name, analyzed in network_summary["network_records"].items():
        config = analyzed["config"]
        if config["variant"] != "main":
            continue
        case_id = f"pair_d{config['delta']}_r45"
        case = cases[case_id]
        if (config["angles_degrees"] != case["anglesDegrees"]
                or config["labels"] != case["labels"]
                or config["amplitude"] != case["amplitude"]):
            raise ValueError("unmatched network case: " + name)
        read_model(network_root, name, analyzed, case, "network")

    for case in cases.values():
        networks = [model for model in case["models"] if model["kind"] == "network"]
        case["networkAvailable"] = bool(networks)
        if not networks:
            case["notes"].append("No actual-network trajectory was recorded for this case.")
        if not any(model.get("order") == 2 for model in case["models"]):
            case["notes"].append("N=2 was recorded only for the unit-amplitude two-point sweep.")
        if case["id"] == "triple_d40":
            case["notes"].append("N=1 and N=5 failed the quadrature refinement tolerance; their order comparison is provisional.")
        for width in sorted({model["width"] for model in networks}):
            members = sorted([model for model in networks if model["width"] == width],
                             key=lambda model: model["seed"])
            if len(members) != 3 or any(model["times"] != members[0]["times"] for model in members):
                raise ValueError("the network mean requires exactly three matched clocks")
            ids = [model["id"] for model in members]
            stacked_train = np.stack([raw_models[key]["train_predictions"] for key in ids], axis=1)
            flattened_train = stacked_train.reshape(len(members[0]["times"]), -1)
            mean_labels = np.tile(case["labels"], len(members))
            mean_weights = np.tile(np.asarray(case["weights"]) / len(members), len(members))
            losses = empirical_loss(flattened_train, mean_labels, mean_weights)
            mean_id = f"{case['id']}_nn{width}_mean"
            raw_models[mean_id] = dict(predictions=np.mean([raw_models[key]["predictions"] for key in ids], axis=0),
                                       dense_predictions=np.mean([raw_models[key]["dense_predictions"] for key in ids], axis=0))
            case["models"].append(dict(id=mean_id, label=f"NN {width} · mean of 3 seeds",
                kind="network-mean", width=width, times=members[0]["times"], losses=losses.tolist(),
                trainPredictions=stacked_train.mean(axis=1).tolist(),
                lossTrainPredictions=flattened_train.tolist(), lossLabels=mean_labels.tolist(),
                lossWeights=mean_weights.tolist(), memberIds=ids,
                finalTime=members[0]["finalTime"], finalLoss=float(losses[-1]),
                settled=all(model["settled"] for model in members), sourceAngularSamples=512,
                lossDefinition="mean of the three per-seed weighted training MSEs",
                notes=["Displayed curve and train predictions are arithmetic seed means. The loss is the mean per-seed MSE, including seed spread."]))

    # Half-degree input geometries allow a single deterministic kernel table.
    # Every value still comes from the study's Q=128 numerical Gaussian integral.
    kernel_grid = kernel(np.deg2rad(np.arange(720) * .5), quad_nodes=128)

    def tabulated_kernel(degrees):
        indices = np.asarray(degrees) * 2
        if np.max(np.abs(indices - np.rint(indices))) > 1e-10:
            raise ValueError("geometry does not lie on the exact half-degree table")
        return kernel_grid[np.rint(indices).astype(int) % 720]

    for case in cases.values():
        train_degrees = np.asarray(case["anglesDegrees"])
        query_degrees = np.arange(preferred_samples) * 360 / preferred_samples
        gram = tabulated_kernel(train_degrees[:, None] - train_degrees[None, :])
        cross = tabulated_kernel(query_degrees[:, None] - train_degrees[None, :])
        flow = FrozenKernel(gram, cross, case["labels"], case["weights"])
        if not np.all(flow.positive):
            raise ValueError("this compact mode export requires full numerical kernel rank")
        scaled_vectors = flow.root[:, None] * flow.vectors
        factors = flow.coordinates / flow.eigenvalues
        basis = (cross @ scaled_vectors) * factors
        train_basis = (gram @ scaled_vectors) * factors
        endpoint = basis.sum(axis=1)
        modes_error = 0.
        for t in [0., .001, .5, 5., 37., 100., 1000.]:
            response = -np.expm1(-2 * flow.eigenvalues * t)
            modes_error = max(modes_error, float(np.max(np.abs(basis @ response - flow.predict(t)))))
        source_id = case.pop("ntkSource")
        analyzed = closure_summary["records"][source_id]
        derived_path = closure_root / "analysis_final" / analyzed["derived_file"]
        checked(derived_path, analyzed["derived_sha256"])
        with np.load(derived_path, allow_pickle=False) as saved:
            expected_endpoint = sample(saved["ntk_endpoint"], preferred_samples)
            expected_T100 = sample(saved["ntk_T100"], preferred_samples)
            endpoint_error = float(np.max(np.abs(endpoint - expected_endpoint)))
            T100_error = float(np.max(np.abs(basis @ -np.expm1(-200 * flow.eigenvalues) - expected_T100)))
        if max(endpoint_error, T100_error, modes_error) > 1e-8:
            raise ValueError("NTK modes do not reproduce stored analysis: " + case["id"])
        case["ntk"] = {"lambda": flow.eigenvalues.tolist(), "basis": basis.tolist(),
                       "trainBasis": train_basis.tolist(), "endpoint": endpoint.tolist(),
                       "coordinates": flow.coordinates.tolist(), "labels": case["labels"],
                       "weights": case["weights"], "quadratureNodes": 128,
                       "initialOutput": 0, "lossDefinition": "weighted training MSE",
                       "notes": ["True limiting initial tangent kernel, zero initial output, full-MSE physical clock.",
                                 "f(t) = basis @ (1 - exp(-2*lambda*t)); endpoint = sum of basis columns.",
                                 "Training loss = sum(coordinates^2 * exp(-4*lambda*t))."]}
        ntk_checks.append(dict(case=case["id"], endpointMaxAbs=endpoint_error,
                               T100MaxAbs=T100_error, arbitraryTimeModeMaxAbs=modes_error,
                               minEigenvalue=float(flow.eigenvalues.min())))

    payload = dict(version=1, angularSamples=preferred_samples,
                   anglesDegrees=(np.arange(preferred_samples) * 360 / preferred_samples).tolist(),
                   defaultCase="pair_d30_r45", cases=list(cases.values()),
                   notes=["The controls display saved main trajectories from both closed campaigns; no training was rerun.",
                          "Time interpolation is linear between observations saved every 10 physical time units. It does not recover unobserved dynamics.",
                          "Matched-loss interpolation solves the weighted MSE of linearly interpolated training predictions. It is an interpolated comparison, not a saved trajectory state.",
                          "N is closure order; NN widths are actual finite-network widths. The true initial NTK is a separate frozen-kernel baseline.",
                          "The final endpoint for a trained model is its last saved, mildly settled state. The NTK endpoint is its analytic infinite-time limit.",
                          "Displayed circles use periodic angular interpolation. Scientific measurements remain in the original 1440-angle analyses."])

    def populate_curves(count):
        resampling = []
        for case in payload["cases"]:
            for model in case["models"]:
                raw = raw_models[model["id"]]
                model["curves"] = curves_list(sample(raw["predictions"], count))
                model["finalCurve"] = curves_list(sample(raw["dense_predictions"], count))
                resampling.append(dict(id=model["id"],
                    **error(sample(model["finalCurve"], 1440), raw["dense_predictions"]),
                    finalVsLastSavedPanelMaxAbs=float(np.max(np.abs(
                        np.asarray(model["finalCurve"]) - np.asarray(model["curves"][-1]))))))
            case["maxAbsEndpoint"] = float(max(np.max(np.abs(case["ntk"]["endpoint"])),
                *[np.max(np.abs(model["finalCurve"])) for model in case["models"]]))
        return resampling

    resampling = populate_curves(preferred_samples)

    def serialize():
        return json.dumps(payload, separators=(",", ":"), ensure_ascii=False,
                          allow_nan=False).encode("utf-8")

    serialized = serialize()
    if len(base64.b64encode(gzip.compress(serialized, compresslevel=9, mtime=0))) > 750_000 and preferred_samples == 360:
        payload["angularSamples"] = 180
        payload["anglesDegrees"] = payload["anglesDegrees"][::2]
        for case in payload["cases"]:
            case["ntk"]["basis"] = case["ntk"]["basis"][::2]
            case["ntk"]["endpoint"] = case["ntk"]["endpoint"][::2]
        resampling = populate_curves(180)
        serialized = serialize()
    compressed = gzip.compress(serialized, compresslevel=9, mtime=0)
    if len(base64.b64encode(compressed)) > 750_000:
        raise ValueError("export exceeds its compressed embedded-data budget")
    if len(cases) != 15 or len(record_checks) != 70:
        raise ValueError("expected 15 cases, 52 closure main runs and 18 network main runs")

    # Reload the actual bytes and verify precision-sensitive training losses.
    reloaded = json.loads(serialized)
    roundtrip_loss_error = 0.
    for case in reloaded["cases"]:
        for model in case["models"]:
            predictions = model.get("lossTrainPredictions", model["trainPredictions"])
            labels = model.get("lossLabels", case["labels"])
            weights = model.get("lossWeights", case["weights"])
            discrepancy = np.max(np.abs(empirical_loss(predictions, labels, weights) - model["losses"]))
            roundtrip_loss_error = max(roundtrip_loss_error, float(discrepancy))
    if roundtrip_loss_error > 1e-14:
        raise ValueError("serialized training loss precision failed")

    checks = dict(status="PASS", cases=len(cases), savedMainTrajectories=len(record_checks),
                  closureMainTrajectories=sum("order" in model for case in cases.values() for model in case["models"]),
                  networkMainTrajectories=18, networkMeans=6,
                  angularSamples=payload["angularSamples"], curveDecimalPlaces=7,
                  jsonBytes=len(serialized), gzipBytes=len(compressed),
                  gzipBase64Bytes=len(base64.b64encode(compressed)),
                  roundtripTrainingLossMaxAbs=roundtrip_loss_error,
                  maxFinalAngularRelativeRms=max(row["relativeRms"] for row in resampling),
                  maxFinalAngularMaxAbs=max(row["maxAbs"] for row in resampling),
                  records=record_checks, ntk=ntk_checks, angularResampling=resampling,
                  inputsSha256=inputs, exporterSha256=sha(__file__),
                  elapsedSeconds=time.perf_counter() - started,
                  threads={key: os.environ.get(key) for key in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]},
                  limitations=payload["notes"])
    output.mkdir(exist_ok=False)
    (output / "viewer_data.json").write_bytes(serialized)
    checks["viewerDataSha256"] = sha(output / "viewer_data.json")
    (output / "export_checks.json").write_text(json.dumps(checks, indent=2, allow_nan=False) + "\n")
    print(json.dumps({key: checks[key] for key in ["status", "cases", "savedMainTrajectories",
                     "angularSamples", "jsonBytes", "gzipBytes", "gzipBase64Bytes", "elapsedSeconds",
                     "maxFinalAngularRelativeRms", "maxFinalAngularMaxAbs"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=GENERATED / "radial_viewer_001")
    parser.add_argument("--angles", type=int, default=240, choices=[180, 240, 360])
    arguments = parser.parse_args()
    run(arguments.output, arguments.angles)
