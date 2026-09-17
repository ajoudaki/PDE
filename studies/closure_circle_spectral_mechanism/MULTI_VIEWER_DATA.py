"""Extend the frozen radial display with the saved multipoint network campaign.

This is a presentation export, with no training or new physical evolution.
Every original case, network seed, closure order, and saved time is retained.
Only displayed angular values are rounded; training predictions retain their
original precision so interpolation uses the actual weighted training MSE.
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


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATED = ROOT / "data/generated/closure_circle_spectral_mechanism"
BASE = GENERATED / "radial_viewer_001"
MULTI = GENERATED / "network_comparison_multi_001"
OUTPUT = GENERATED / "radial_viewer_multi_001"
MULTI_CASES = {"triple_d20", "triple_d40", "triple_d60",
               "quad_d15", "quad_d30", "quad_d45"}
WIDTHS = {1024, 4096}
SEEDS = {1729, 2718, 3141}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sample(values, count):
    """Periodic linear resampling on a uniform circle, without any rotation."""
    values = np.asarray(values, dtype=float)
    positions = np.arange(count, dtype=float) * values.shape[-1] / count
    left = np.floor(positions).astype(int)
    blend = positions - left
    return (values[..., left] * (1 - blend)
            + values[..., (left + 1) % values.shape[-1]] * blend)


def empirical_loss(predictions, labels, weights):
    return np.sum((np.asarray(predictions) - labels) ** 2 * weights, axis=-1)


def error(candidate, reference):
    reference = np.asarray(reference)
    difference = np.asarray(candidate) - reference
    return dict(maxAbs=float(np.max(np.abs(difference))),
                relativeRms=float(np.sqrt(np.mean(difference ** 2))
                                  / max(np.sqrt(np.mean(reference ** 2)), 1e-30)))


def run(output=OUTPUT):
    started = time.perf_counter()
    output = Path(output).resolve()
    if output != OUTPUT or output.exists():
        raise ValueError("output must be the fresh radial_viewer_multi_001 directory")
    inputs = {}

    def checked(path, expected=None):
        path = Path(path).resolve()
        allowed = [HERE, GENERATED, ROOT / "docs", ROOT / "code"]
        if not any(path.is_relative_to(directory) for directory in allowed):
            raise ValueError("input outside this study's permitted source boundary")
        digest = sha(path)
        if expected is not None and digest != expected:
            raise ValueError("input hash mismatch: " + str(path))
        inputs[str(path.relative_to(ROOT))] = digest
        return digest

    def read_json(path, expected=None):
        checked(path, expected)
        return json.loads(Path(path).read_text())

    old_checks = read_json(BASE / "export_checks.json")
    if old_checks["status"] != "PASS":
        raise ValueError("the original display has no passing export check")
    data = read_json(BASE / "viewer_data.json", old_checks["viewerDataSha256"])
    checked(HERE / "VIEWER_DATA.py", old_checks["exporterSha256"])
    for name, expected in old_checks["inputsSha256"].items():
        checked(ROOT / name, expected)
    if data["angularSamples"] != 240 or len(data["cases"]) != 15:
        raise ValueError("unexpected original display schema")
    cases = {case["id"]: case for case in data["cases"]}
    original_ids = {model["id"] for case in cases.values() for model in case["models"]}
    closure_root = GENERATED / "campaign_001"
    network_root = GENERATED / "network_comparison_001"
    closure_summary = read_json(closure_root / "analysis_final/summary.json")
    network_summary = read_json(network_root / "analysis_final/summary.json")
    manifest = read_json(MULTI / "manifest.json")
    checked(MULTI / "manifest.sha256")
    manifest_hash = inputs[str((MULTI / "manifest.json").relative_to(ROOT))]
    if (MULTI / "manifest.sha256").read_text().strip() != manifest_hash:
        raise ValueError("multipoint manifest differs from its frozen hash")
    for name, expected in manifest["source_hashes"].items():
        checked(ROOT / name, expected)
    for name, expected in manifest["input_hashes"].items():
        checked(ROOT / name, expected)
    for archived in manifest["archived_sources"].values():
        checked(MULTI / archived["path"], archived["sha256"])
    worker_checks = read_json(GENERATED / "multi_worker_checks_001/batch.json")
    if not worker_checks["passed"] or worker_checks["source_hashes"] != manifest["source_hashes"]:
        raise ValueError("matching frozen producer correctness checks are required")

    configs = manifest["configs"]
    main_configs = [config for config in configs if config["variant"] == "main"]
    controls = [config for config in configs if config["variant"] != "main"]
    expected_main = {(case_id, width, seed) for case_id in MULTI_CASES
                     for width in WIDTHS for seed in SEEDS}
    actual_main = {(config["name"], config["width"], config["seed"])
                   for config in main_configs}
    expected_controls = {(case_id, "half", 4096, 1729) for case_id in MULTI_CASES}
    expected_controls |= {(case_id, "precision", 1024, 1729) for case_id in MULTI_CASES}
    actual_controls = {(config["name"], config["variant"], config["width"], config["seed"])
                       for config in controls}
    if (len(configs) != 48 or len(main_configs) != 36 or len(controls) != 12
            or actual_main != expected_main or actual_controls != expected_controls
            or len({config["id"] for config in configs}) != 48):
        raise ValueError("the multipoint campaign does not have its complete prescribed matrix")

    raw_models = {}
    record_checks = []
    control_checks = []

    def read_model(root, name, case, expected_config, expected_record=None, new=False):
        record = read_json(root / name / "record.json", expected_record)
        if record["status"] != "complete" or record["config"] != expected_config:
            raise ValueError("incomplete or mismatched record: " + name)
        config = record["config"]
        for field, case_field in [("kind", "kind"), ("delta", "delta"),
                                  ("rotation", "rotation"), ("amplitude", "amplitude"),
                                  ("angles_degrees", "anglesDegrees"), ("labels", "labels")]:
            if config[field] != case[case_field]:
                raise ValueError("training-data geometry mismatch: " + name)
        for filename, expected in record["outputs"].items():
            if new or filename in ("config.json", "observations.npz"):
                checked(root / name / filename, expected)
        if json.loads((root / name / "config.json").read_text()) != config:
            raise ValueError("config file differs from the record: " + name)
        if new and (record["source_hashes"] != manifest["source_hashes"]
                    or record["input_hashes"] != manifest["input_hashes"]
                    or record["manifest_sha256"] != manifest_hash):
            raise ValueError("producer source or input provenance mismatch: " + name)
        keys = ["times", "loss", "predictions", "train_predictions", "dense_predictions"]
        if new:
            keys += ["theta", "stop_theta", "common_T100"]
        with np.load(root / name / "observations.npz", allow_pickle=False) as saved:
            raw = {key: saved[key] for key in keys}
            if "order" in config:
                if not (np.array_equal(saved["labels"], case["labels"])
                        and np.allclose(saved["weights"], case["weights"], rtol=0, atol=1e-15)
                        and np.allclose(saved["angles"], np.deg2rad(case["anglesDegrees"]),
                                        rtol=0, atol=1e-14)):
                    raise ValueError("raw closure training-data mismatch: " + name)
        if not all(np.all(np.isfinite(value)) for value in raw.values()):
            raise ValueError("nonfinite observation: " + name)
        times = raw["times"]
        if (times[0] != 0 or not np.all(np.diff(times) > 0)
                or raw["predictions"].shape[0] != len(times)
                or raw["train_predictions"].shape != (len(times), len(case["labels"]))
                or raw["dense_predictions"].shape != (1440,)):
            raise ValueError("invalid observation dimensions or clock: " + name)
        losses = empirical_loss(raw["train_predictions"], case["labels"], case["weights"])
        loss_error = float(np.max(np.abs(losses - raw["loss"])))
        if (loss_error > 1e-11 or abs(losses[-1] - record["final_loss"]) > 1e-11
                or times[-1] != record.get("final_time", record.get("last_time"))):
            raise ValueError("raw training MSE or final time mismatch: " + name)
        if new:
            if (not np.array_equal(times, np.arange(0., 121., 10.))
                    or raw["predictions"].shape != (13, 512)
                    or raw["common_T100"].shape != (1440,)
                    or not np.allclose(raw["stop_theta"], 2 * np.pi * np.arange(512) / 512,
                                       rtol=0, atol=1e-14)
                    or not np.allclose(raw["theta"], 2 * np.pi * np.arange(1440) / 1440,
                                       rtol=0, atol=1e-14)):
                raise ValueError("multipoint campaign clock or circle grid mismatch: " + name)
            tolerance = 2e-5 if config["dtype"] == "float32" else 1e-10
            oddness = float(np.max(np.abs(raw["dense_predictions"][:720]
                                         + raw["dense_predictions"][720:])))
            settling_tolerance = .002 * max(1., float(np.max(np.abs(raw["predictions"][-1]))))
            settled = bool(losses[-1] <= 1e-6
                           and np.max(np.abs(raw["predictions"][10] - raw["predictions"][8])) <= settling_tolerance
                           and np.max(np.abs(raw["predictions"][12] - raw["predictions"][10])) <= settling_tolerance)
            if (record["settled"] != settled or record["stop_reason"] != "fixed_T120"
                    or oddness > tolerance or not record["checks"]["finite_states"]
                    or record["checks"]["disk_replay"] > tolerance
                    or np.max(np.diff(losses)) > 1e-6):
                raise ValueError("multipoint raw validity or settling check failed: " + name)
        raw_models[name] = raw
        report = dict(id=name, rawLossMaxAbs=loss_error, savedFrameCount=len(times),
                      savedPanelAngles=int(raw["predictions"].shape[-1]),
                      firstPositiveTime=float(times[1]), firstPositiveLoss=float(losses[1]),
                      finalTime=float(times[-1]), finalLoss=float(losses[-1]),
                      settled=bool(record["settled"]), stopReason=record["stop_reason"],
                      trainingDataIdentity=True, sourceHashesVerified=True)
        return record, losses, report

    for case in cases.values():
        for model in case["models"]:
            name = model["id"]
            if model["kind"] == "network-mean":
                continue
            if model["kind"] == "closure":
                root = closure_root
                analyzed = closure_summary["records"][name]
                expected = closure_summary["input_hashes"][name]["record"]
            else:
                root = network_root
                analyzed = network_summary["network_records"][name]
                expected = analyzed["record_sha256"]
            record, losses, report = read_model(root, name, case, analyzed["config"], expected)
            raw = raw_models[name]
            if (model["times"] != raw["times"].tolist()
                    or model["trainPredictions"] != raw["train_predictions"].tolist()
                    or model["losses"] != losses.tolist()
                    or model["settled"] != bool(record["settled"])):
                raise ValueError("original display differs from its raw record: " + name)
            model["stopReason"] = record["stop_reason"]
            record_checks.append(report)

    for config in configs:
        case = cases[config["name"]]
        name = config["id"]
        record, losses, report = read_model(MULTI, name, case, config, new=True)
        if config["variant"] != "main":
            control_checks.append(report)
            continue
        raw = raw_models[name]
        case["models"].append(dict(id=name, label=f"NN {config['width']} · seed {config['seed']}",
            kind="network", width=config["width"], seed=config["seed"],
            times=raw["times"].tolist(), losses=losses.tolist(),
            trainPredictions=raw["train_predictions"].tolist(), finalTime=float(raw["times"][-1]),
            finalLoss=float(losses[-1]), settled=bool(record["settled"]),
            stopReason=record["stop_reason"], lossDefinition="weighted training MSE",
            sourceAngularSamples=int(raw["predictions"].shape[-1]),
            notes=["Actual finite network; its saved initial output is retained.",
                   "The recorded endpoint is T=120; the mild-settling flag is reported separately."]))
        record_checks.append(report)

    batch = read_json(MULTI / "main_batch.json")
    if (batch["exit_codes"] != [0, 0] or batch["missing"] or batch["stop_reason"] is not None
            or set(batch["completed"]) != {config["id"] for config in configs}
            or batch["source_hashes"] != manifest["source_hashes"]
            or batch["manifest_sha256"] != manifest_hash):
        raise ValueError("multipoint campaign completion or provenance check failed")

    mean_checks = []
    for case in cases.values():
        networks = [model for model in case["models"] if model["kind"] == "network"]
        case["networkAvailable"] = bool(networks)
        if networks:
            case["notes"] = [note for note in case["notes"]
                             if note != "No actual-network trajectory was recorded for this case."]
        for width in sorted({model["width"] for model in networks}):
            members = sorted([model for model in networks if model["width"] == width],
                             key=lambda model: model["seed"])
            if (len(members) != 3 or {member["seed"] for member in members} != SEEDS
                    or any(model["times"] != members[0]["times"] for model in members)):
                raise ValueError("a seed mean requires three complete, matched clocks")
            ids = [model["id"] for model in members]
            stacked_train = np.stack([raw_models[key]["train_predictions"] for key in ids], axis=1)
            flattened_train = stacked_train.reshape(len(members[0]["times"]), -1)
            labels = np.tile(case["labels"], 3)
            weights = np.tile(np.asarray(case["weights"]) / 3, 3)
            losses = empirical_loss(flattened_train, labels, weights)
            expected_losses = np.mean([model["losses"] for model in members], axis=0)
            mean_error = float(np.max(np.abs(losses - expected_losses)))
            if mean_error > 1e-14:
                raise ValueError("mean per-seed MSE mismatch")
            name = f"{case['id']}_nn{width}_mean"
            raw_models[name] = dict(
                predictions=np.mean([raw_models[key]["predictions"] for key in ids], axis=0),
                dense_predictions=np.mean([raw_models[key]["dense_predictions"] for key in ids], axis=0))
            replacement = dict(id=name, label=f"NN {width} · mean of 3 seeds",
                kind="network-mean", width=width, times=members[0]["times"], losses=losses.tolist(),
                trainPredictions=stacked_train.mean(axis=1).tolist(),
                lossTrainPredictions=flattened_train.tolist(), lossLabels=labels.tolist(),
                lossWeights=weights.tolist(), memberIds=ids, finalTime=members[0]["finalTime"],
                finalLoss=float(losses[-1]), settled=all(model["settled"] for model in members),
                stopReason="member recorded endpoints", sourceAngularSamples=512,
                lossDefinition="mean of the three per-seed weighted training MSEs",
                notes=["Displayed curve and train predictions are arithmetic seed means. The loss is the mean per-seed MSE, including seed spread."])
            existing = next((i for i, model in enumerate(case["models"]) if model["id"] == name), None)
            if existing is None:
                case["models"].append(replacement)
            else:
                previous = case["models"][existing]
                for field in ["times", "losses", "trainPredictions", "lossTrainPredictions",
                              "lossLabels", "lossWeights", "memberIds"]:
                    if previous[field] != replacement[field]:
                        raise ValueError("original seed mean changed: " + name + " / " + field)
                case["models"][existing] = replacement
            mean_checks.append(dict(id=name, memberIds=ids, meanPerSeedMseMaxAbs=mean_error))

    endpoint_checks = []
    for case in cases.values():
        networks = [model for model in case["models"]
                    if model["kind"] in ("network", "network-mean")]
        closures = [model for model in case["models"] if model["kind"] == "closure"]
        analyzed = closure_summary["records"][closures[0]["id"]]
        path = closure_root / "analysis_final" / analyzed["derived_file"]
        checked(path, analyzed["derived_sha256"])
        with np.load(path, allow_pickle=False) as saved:
            ntk_dense = saved["ntk_endpoint"]
        if (ntk_dense.shape != (1440,) or not np.all(np.isfinite(ntk_dense))
                or np.max(np.abs(sample(ntk_dense, 240) - case["ntk"]["endpoint"])) > 1e-8):
            raise ValueError("original NTK endpoint differs from dense analysis: " + case["id"])
        for model, dense in [(model, raw_models[model["id"]]["dense_predictions"])
                             for model in closures] + [(case["ntk"], ntk_dense)]:
            model["endpointNetworkErrors"] = {
                network["id"]: error(dense, raw_models[network["id"]]["dense_predictions"])["relativeRms"]
                for network in networks}
            endpoint_checks.append(dict(case=case["id"], model=model.get("id", "ntk"),
                comparisons=len(networks), sourceAngularSamples=1440,
                reference="selected network's recorded endpoint; denominator is network circle RMS"))

    data["defaultCase"] = "quad_d15"
    data["notes"] = [
        "The controls display saved main trajectories; all original cases, closure orders, widths, seeds, and observation times are retained.",
        "Actual networks are available for the three existing pair cases and all six three- and four-point cases. Refinement and precision controls remain in the source campaign and export provenance.",
        "Time interpolation is linear between observations saved every 10 physical time units. It does not recover unobserved dynamics.",
        "Matched-loss interpolation solves the weighted MSE of linearly interpolated training predictions. It is an interpolated comparison, not a saved trajectory state.",
        "N is closure order; NN widths are actual finite-network widths. The true initial NTK is a separate frozen-kernel baseline.",
        "Recorded endpoints use each trained model's last saved state. The new multipoint networks end at T=120, including runs that did not meet mild settling. The NTK endpoint is its analytic infinite-time limit.",
        "Endpoint circle errors use the original 1440-angle arrays, with the selected network as denominator. Recorded endpoints can have different final times; common-time and matched-MSE modes are separate comparisons.",
        "Displayed circles use periodic angular interpolation and numerical rounding. Training predictions and losses retain full precision; source measurements remain in the original dense arrays."]

    def populate_curves(decimals):
        reports = []
        for case in cases.values():
            for model in case["models"]:
                raw = raw_models[model["id"]]
                panel = sample(raw["predictions"], 240)
                final = sample(raw["dense_predictions"], 240)
                displayed_panel = np.round(panel, decimals)
                displayed_final = np.round(final, decimals)
                model["curves"] = displayed_panel.tolist()
                model["finalCurve"] = displayed_final.tolist()
                endpoint_error = error(sample(displayed_final, 1440), raw["dense_predictions"])
                panel_error = error(sample(displayed_panel, raw["predictions"].shape[-1]), raw["predictions"])
                if endpoint_error["relativeRms"] >= .005:
                    raise ValueError("display endpoint exceeds 0.5% relative RMS: " + model["id"])
                reports.append(dict(id=model["id"], **endpoint_error,
                    trajectoryAngularRelativeRms=panel_error["relativeRms"],
                    panelQuantizationMaxAbs=float(np.max(np.abs(displayed_panel - panel))),
                    finalQuantizationMaxAbs=float(np.max(np.abs(displayed_final - final))),
                    finalVsLastSavedPanelMaxAbs=float(np.max(np.abs(displayed_final - displayed_panel[-1])))))
            case["maxAbsEndpoint"] = float(max(np.max(np.abs(case["ntk"]["endpoint"])),
                *[np.max(np.abs(model["finalCurve"])) for model in case["models"]]))
        return reports

    template = (HERE / "RADIAL_VIEWER.html").read_bytes()
    placeholder = b"__COMPRESSED_VIEWER_DATA__"
    if template.count(placeholder) != 1:
        raise ValueError("viewer template has no unique embedding marker")
    attempts = []
    for decimals in (5, 4):
        angular_checks = populate_curves(decimals)
        data["curveDecimalPlaces"] = decimals
        serialized = json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()
        compressed = gzip.compress(serialized, compresslevel=9, mtime=0)
        embedded_bytes = len(base64.b64encode(compressed))
        fragment_bytes = len(template) - len(placeholder) + embedded_bytes
        attempts.append(dict(curveDecimalPlaces=decimals, gzipBase64Bytes=embedded_bytes,
                             estimatedFragmentBytes=fragment_bytes))
        if fragment_bytes < 1_000_000:
            break
    else:
        raise ValueError("complete export exceeds the strict 1 MB fragment budget")

    reloaded = json.loads(serialized)
    loss_error = 0.
    for case in reloaded["cases"]:
        for model in case["models"]:
            predictions = model.get("lossTrainPredictions", model["trainPredictions"])
            labels = model.get("lossLabels", case["labels"])
            weights = model.get("lossWeights", case["weights"])
            discrepancy = np.max(np.abs(empirical_loss(predictions, labels, weights) - model["losses"]))
            loss_error = max(loss_error, float(discrepancy))
    models = [model for case in reloaded["cases"] for model in case["models"]]
    counts = {kind: sum(model["kind"] == kind for model in models)
              for kind in ("closure", "network", "network-mean")}
    if (counts != {"closure": 52, "network": 54, "network-mean": 18}
            or len(record_checks) != 106 or len(control_checks) != 12
            or len({model["id"] for model in models}) != 124
            or not original_ids.issubset({model["id"] for model in models})
            or not all(cases[case_id]["networkAvailable"] for case_id in MULTI_CASES)
            or loss_error > 1e-14):
        raise ValueError("final completeness or loss roundtrip check failed")

    checks = dict(status="PASS", cases=len(cases), savedMainTrajectories=len(record_checks),
        closureMainTrajectories=52, networkMainTrajectories=54, networkMeans=18,
        newNetworkMainTrajectories=36, newNetworkMeans=12, validatedNewControlTrajectories=12,
        originalModelIdsPreserved=True, savedTimesPreserved=True, defaultCase=data["defaultCase"],
        angularSamples=240, curveDecimalPlaces=decimals, jsonBytes=len(serialized),
        gzipBytes=len(compressed), gzipBase64Bytes=embedded_bytes,
        estimatedFragmentBytes=fragment_bytes, sizeAttempts=attempts,
        roundtripTrainingLossMaxAbs=loss_error,
        maxFinalAngularRelativeRms=max(row["relativeRms"] for row in angular_checks),
        maxFinalAngularMaxAbs=max(row["maxAbs"] for row in angular_checks),
        maxDisplayQuantizationAbs=max(max(row["panelQuantizationMaxAbs"], row["finalQuantizationMaxAbs"])
                                      for row in angular_checks),
        records=record_checks, newControlRecords=control_checks, networkMeanChecks=mean_checks,
        ntk=old_checks["ntk"], endpointNetworkComparisons=endpoint_checks,
        angularResampling=angular_checks, inputsSha256=inputs, exporterSha256=sha(__file__),
        elapsedSeconds=time.perf_counter() - started,
        threads={key: os.environ.get(key) for key in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]},
        limitations=data["notes"])
    output.mkdir(exist_ok=False)
    (output / "viewer_data.json").write_bytes(serialized)
    checks["viewerDataSha256"] = sha(output / "viewer_data.json")
    (output / "export_checks.json").write_text(json.dumps(checks, indent=2, allow_nan=False) + "\n")
    print(json.dumps({key: checks[key] for key in ["status", "cases", "savedMainTrajectories",
        "networkMainTrajectories", "networkMeans", "angularSamples", "curveDecimalPlaces",
        "jsonBytes", "gzipBase64Bytes", "estimatedFragmentBytes", "elapsedSeconds",
        "maxFinalAngularRelativeRms", "maxDisplayQuantizationAbs"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()
    run(arguments.output)
