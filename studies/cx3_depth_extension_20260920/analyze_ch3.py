"""Read-only verification of the five saved operational runs; no evolution.

Decode the float64 checkpoint directly and use dense weighted population
matrices, without importing the initializer or closure implementation.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(value):
    return np.array([float.fromhex(x) for x in value["values"]]).reshape(value["shape"])


def dense_fields(state, inputs, initial=False):
    b, pi = state["b"], state["pi"]
    matrices = state["D" if initial else "M"]
    h = [np.tanh(state["g" if initial else "w"] @ inputs.T)]
    for k, matrix in enumerate(matrices):
        action = (b[k+1] @ matrix @ b[k].T) * pi[k][None, :]
        h.append(np.tanh(action @ h[-1]))
    prediction = (pi[-1]*state["c"]) @ h[-1]
    return h, prediction


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    started = time.process_time()
    directory = args.directory.resolve()
    repo = Path(__file__).resolve().parents[2]
    provenance = json.loads((directory/"provenance.json").read_text())
    for name, expected in provenance["sources"].items():
        assert digest(repo/name) == expected, name
    reports, observations = [], {}
    for tag in "abcde":
        case = directory/tag
        report = json.loads((case/"report.json").read_text())
        assert report["status"] == "pass" and report["exact_restart"]
        for name, expected in report["output_hashes"].items():
            assert digest(case/name) == expected, (tag, name)
        checkpoint = json.loads((case/"final.json").read_text())
        assert checkpoint == json.loads((case/"resumed.json").read_text())
        assert checkpoint["digits"] is None
        raw = checkpoint["state"]
        state = {key: ([decode(v) for v in value] if isinstance(value, list)
                       else decode(value)) for key, value in raw.items()}
        with np.load(case/"observations.npz", allow_pickle=False) as saved:
            obs = {key: saved[key] for key in saved.files}
        assert all(np.all(np.isfinite(v)) for v in obs.values())
        observations[tag] = obs
        current, prediction = dense_fields(state, obs["inputs"])
        initial, _ = dense_fields(state, obs["inputs"], initial=True)
        _, panel_prediction = dense_fields(state, obs["panel"])
        errors = [float(np.max(np.abs(prediction-obs["training_prediction"]))),
                  float(np.max(np.abs(panel_prediction-obs["predictions"])))]
        rms = []
        for k in range(len(current)):
            pair = np.stack((initial[k], current[k]), axis=-1)
            errors.append(float(np.max(np.abs(pair-obs[f"pairs_{k+1}"]))))
            square = (pair[:, :, 1]-pair[:, :, 0])**2
            rms.append(float(np.sqrt(state["pi"][k] @ square @ obs["input_weights"])))
        risk = float(obs["input_weights"] @ ((prediction-obs["labels"])**2))
        assert max(errors) <= 1e-11, (tag, errors)
        assert abs(risk-report["loss"]) <= 1e-11
        assert np.max(np.abs(np.array(rms)-report["rms"])) <= 1e-11
        reports.append(dict(id=tag, status="pass", loss=risk, rms=rms,
                            dense_observation_max_error=max(errors),
                            feature_counts=report["feature_counts"],
                            state_array_bytes=report["retained_state_bytes"]["arrays"],
                            operation_cpu_seconds=report["cpu_seconds"],
                            operation_peak_rss_bytes=report["peak_rss_bytes"],
                            exact_restart=True, hashes_match=True))
    differences = {}
    for first, second in (("a", "e"), ("b", "d"), ("a", "b"), ("b", "c")):
        differences[first+"_"+second] = dict(
            panel_prediction_max_abs=float(np.max(np.abs(
                observations[first]["predictions"]-observations[second]["predictions"]))),
            rms_max_abs=float(np.max(np.abs(observations[first]["rms"]-
                                          observations[second]["rms"]))))
    result = dict(status="pass", provenance_matches=True, cases=reports,
                  diagnostic_differences_without_accuracy_claim=differences,
                  operation_total_cpu_seconds=sum(r["operation_cpu_seconds"] for r in reports),
                  operation_peak_rss_bytes=max(r["operation_peak_rss_bytes"] for r in reports),
                  analysis_cpu_seconds=time.process_time()-started,
                  analyzer_sha256=digest(Path(__file__)))
    (directory/"analysis.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
