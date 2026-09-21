#!/usr/bin/env python3
"""Export audited best-checkpoint predictions for a display-only radial view.

No optimization is performed. Training samples are retained separately from
an adaptive subset of the existing 8192-node circle grid. There is no target
function between labelled samples. Precision-adjudicated Adam cases use their
existing checked sample predictions and omit unverified circle curves.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import heapq
import json
import os
from pathlib import Path
import time
from typing import Any

for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"
import numpy as np

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
GENERATED = ROOT / "data/generated" / STUDY.name
SEEDS = (20260921, 20260922, 20260923)
GRID = 8192
FIT_MSE = 0.001
PRED_TOL = 1e-8
MSE_TOL = 1e-9
DISPLAY_TOL = 0.002
MAX_VERTICES = 2048
MIN_VERTICES = 128


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def read_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as values:
        return {key: np.array(values[key], copy=True) for key in values.files}


def packed(array: np.ndarray, dtype: str) -> str:
    return base64.b64encode(np.asarray(array, dtype=dtype).tobytes()).decode("ascii")


def forward(model: str, state: dict[str, np.ndarray], initial: dict[str, np.ndarray], u: np.ndarray) -> np.ndarray:
    n = state["W"].shape[0]
    first = np.tanh(state["W"] @ u.T)
    if model.startswith("width"):
        second = np.tanh(state["A"] @ first)
    else:
        second = np.tanh(initial["B2"] @ state["M"] @ (initial["B1"].T @ first / n))
    return (state["c"] / n) @ second


def sample_metrics(prediction: np.ndarray, y: np.ndarray) -> dict[str, Any]:
    if not np.isfinite(prediction).all():
        raise ValueError("Nonfinite sample prediction")
    mse = float(np.mean((prediction - y) ** 2))
    signs = int(np.count_nonzero(y * prediction <= 0))
    return {"mse": mse, "rmse": float(np.sqrt(mse)), "signErrors": signs,
            "fit": bool(mse <= FIT_MSE and signs == 0)}


def periodic_interpolate(indices: np.ndarray, values: np.ndarray) -> np.ndarray:
    return np.interp(np.arange(GRID), np.append(indices, GRID), np.append(values, values[0]))


def adaptive_circle(values: np.ndarray) -> tuple[np.ndarray, np.ndarray, dict[str, Any]]:
    """Greedy maximum-error refinement against all existing circle grid nodes."""
    if values.shape != (GRID,) or not np.isfinite(values).all():
        raise ValueError("Invalid circle prediction grid")
    closed = np.append(values, values[0])
    indices = set(range(0, GRID, GRID // MIN_VERTICES))
    indices.update((int(np.argmin(values)), int(np.argmax(values))))
    heap: list[tuple[float, int, int, int]] = []

    def push(left: int, right: int) -> None:
        if right - left <= 1:
            return
        nodes = np.arange(left + 1, right)
        linear = closed[left] + (closed[right] - closed[left]) * (nodes - left) / (right - left)
        errors = np.abs(closed[nodes] - linear)
        offset = int(np.argmax(errors))
        heapq.heappush(heap, (-float(errors[offset]), left, right, int(nodes[offset])))

    starting = sorted(indices) + [GRID]
    for left, right in zip(starting, starting[1:]):
        push(left, right)
    while heap and len(indices) < MAX_VERTICES:
        error, left, right, middle = heapq.heappop(heap)
        if -error <= DISPLAY_TOL:
            break
        indices.add(middle)
        push(left, middle)
        push(middle, right)
    selected = np.asarray(sorted(indices), dtype="<u2")
    exact = values[selected]
    displayed = exact.astype("<f4")
    rounding = float(np.max(np.abs(displayed.astype(np.float64) - exact)))
    before_rounding = float(np.max(np.abs(periodic_interpolate(selected, exact) - values)))
    combined = float(np.max(np.abs(periodic_interpolate(selected, displayed.astype(np.float64)) - values)))
    return selected, displayed, {
        "vertices": len(selected), "targetAbsoluteInterpolationError": DISPLAY_TOL,
        "beforeRoundingInterpolationError": before_rounding, "roundingError": rounding,
        "combinedInterpolationError": combined,
        "targetMetBeforeRounding": before_rounding <= DISPLAY_TOL + 1e-12,
        "fullGridMinimum": float(np.min(values)), "fullGridMaximum": float(np.max(values)),
        "fullGridMaxAbs": float(np.max(np.abs(values))),
        "globalExtremaRetained": bool(int(np.argmin(values)) in indices and int(np.argmax(values)) in indices),
        "scope": "Periodic linear interpolation in prediction value compared only with the original 8192 stored grid nodes; not a continuous-angle error bound or geometric canvas-pixel bound.",
    }


def best_trace_entry(path: Path, record: dict[str, Any], round_id: str) -> dict[str, Any]:
    best = None
    count = 0
    with path.open() as handle:
        for line in handle:
            if not line.strip():
                continue
            entry = json.loads(line)
            count += 1
            loss = entry.get("mse")
            if loss is not None and np.isfinite(loss) and (best is None or loss < best["mse"]):
                best = entry
    if best is None:
        raise ValueError("No finite checkpoint-selection trace entry")
    reported = record["diagnostics"]["best"]["mse"]
    if abs(best["mse"] - reported) > MSE_TOL:
        raise ValueError("Minimum trace loss does not bind saved best checkpoint")
    if round_id == "gd" and best.get("phase") not in ("initial", "gd"):
        raise ValueError("Unexpected non-GD phase in GD best checkpoint")
    return {"bestPhase": best.get("phase"),
            "bestStep": best.get("accepted_step") if round_id == "gd" else best.get("optimizer_step"),
            "bestEvaluation": best.get("forward_evaluations") if round_id == "gd" else best.get("evaluation"),
            "traceEntries": count,
            "bestStateKind": ("accepted simultaneous GD state" if best.get("phase") == "gd" else
                              "evaluated LBFGS state; may be a line-search trial" if best.get("phase") == "lbfgs" else
                              "least-squares readout polish" if best.get("phase") == "readout_polish" else
                              "Adam state" if best.get("phase") == "adam" else "initial state")}


def export_attempt(round_id: str, row: dict[str, Any], run_root: Path, adjudications: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    path = run_root / row["attempt"]
    if row.get("reproduction") or not row.get("decision_valid"):
        raise ValueError("Exporter requires an original checked attempt")
    record_path = path / "record.json"
    record = read_json(record_path)
    if sha256(record_path) != row["record_sha256"]:
        raise ValueError("Analysis/record hash mismatch")
    for name in ("dataset.npz", "initial.npz", "best.npz", "predictions.npz", "trace.jsonl"):
        expected = record.get("outputs_sha256", {}).get(name)
        if expected is None or sha256(path / name) != expected:
            raise ValueError(f"Record/output hash mismatch for {name}")
    config = record["config"]
    m, seed, width = int(config["m"]), int(config["seed"]), int(config["width"])
    model = f"width{width}" if config["model"] == "network" else f"closure{width}"
    gain = "canonical" if config["gain"] == "primary" else "high"
    if m != row["m"] or seed != row["seed"] or model != row["model"] or seed not in SEEDS:
        raise ValueError("Record/analysis configuration mismatch")
    if (gain == "canonical") != (row["initialization"] == "canonical"):
        raise ValueError("Initialization labels disagree")
    if record["first_weight_gain"] != (1 if gain == "canonical" else m / 2):
        raise ValueError("Initialization gain mismatch")
    dataset = read_npz(path / "dataset.npz")
    expected_theta = 2 * np.pi * np.arange(m) / m
    expected_y = (-1.0) ** np.arange(m)
    circle_theta = 2 * np.pi * np.arange(GRID) / GRID
    if not np.array_equal(dataset["y"], expected_y) or np.max(np.abs(dataset["theta"] - expected_theta)) > 1e-14:
        raise ValueError("Training sample order/labels changed")
    if dataset["circle_theta"].shape != (GRID,) or np.max(np.abs(dataset["circle_theta"] - circle_theta)) > 1e-14:
        raise ValueError("Circle-grid coordinate recipe changed")
    initial, state, saved = (read_npz(path / name) for name in ("initial.npz", "best.npz", "predictions.npz"))
    fp_prediction = forward(model, state, initial, dataset["u"])
    adjudication = adjudications.get(str(path.resolve())) if round_id == "adam" else None
    audit: dict[str, Any] = {
        "id": f"{round_id}:{row['attempt']}", "path": str(path),
        "recordSha256": sha256(record_path), "bestSha256": sha256(path / "best.npz"),
        "datasetSha256": sha256(path / "dataset.npz"), "predictionsSha256": sha256(path / "predictions.npz"),
        "traceSha256": sha256(path / "trace.jsonl"),
        "float64SampleSavedDiscrepancy": float(np.max(np.abs(fp_prediction - saved["best_train"]))),
    }
    if adjudication:
        evidence_path = Path(adjudication["evidencepath"])
        evidence = read_json(evidence_path)
        if not adjudication.get("resolved") or not adjudication.get("stable_to_higher_precision") or adjudication["record_sha256"] != audit["recordSha256"]:
            raise ValueError("Unresolved or stale high-precision adjudication")
        if evidence["best_sha256"] != audit["bestSha256"] or evidence["dataset_sha256"] != audit["datasetSha256"]:
            raise ValueError("High-precision checkpoint/data hash mismatch")
        sample_prediction = np.asarray([float(value) for value in evidence["high_precision"]["predictions_decimal"]], dtype=np.float64)
        precision = "60/90-digit checked training samples; float64 circle curve withheld"
        audit.update(adjudicationSha256=sha256(GENERATED / "check_scratch/numerical_adjudications.json"),
                     highPrecisionEvidence=str(evidence_path), highPrecisionEvidenceSha256=sha256(evidence_path),
                     highPrecisionDigits=evidence["high_precision"]["digits"])
        circle = None
        circle_reason = "Saved float64 predictions failed the strict replay check. Existing high-precision evidence covers training samples only; no validated between-sample curve is available."
    else:
        if not row.get("raw_replay_valid") or audit["float64SampleSavedDiscrepancy"] > PRED_TOL:
            raise ValueError("Unaudited float64 training samples")
        sample_prediction = fp_prediction
        precision = "independent float64 replay"
        circle = np.concatenate([forward(model, state, initial, dataset["circle_u"][start:start + 512]) for start in range(0, GRID, 512)])
        audit["circleReplayError"] = float(np.max(np.abs(circle - saved["best_circle"])))
        circle_reason = ""
        if not np.isfinite(circle).all() or audit["circleReplayError"] > PRED_TOL:
            circle = None
            circle_reason = "Training samples are checked, but the saved circle grid fails the independent float64 prediction tolerance; its curve is withheld."
    checked = sample_metrics(sample_prediction, expected_y)
    authoritative_mse = float(row["reported_mse"] if round_id == "adam" else row["best_mse"])
    authoritative_signs = int(row["reported_sign_errors"] if round_id == "adam" else row["best_sign_errors"])
    if abs(checked["mse"] - authoritative_mse) > MSE_TOL or checked["signErrors"] != authoritative_signs or checked["fit"] != row["accepted_fit"]:
        raise ValueError("Exported samples disagree with checked analysis decision")
    audit["sampleMseDiscrepancy"] = abs(checked["mse"] - authoritative_mse)
    trace = best_trace_entry(path / "trace.jsonl", record, round_id)
    audit["traceSelection"] = trace
    result = {
        "id": audit["id"], "round": round_id, "model": model, "m": m, "seed": seed,
        "gain": gain, "gainValue": record["first_weight_gain"],
        "etaMax": float(config["eta_max"]) if round_id == "gd" else None,
        "mse": authoritative_mse, "rmse": float(np.sqrt(authoritative_mse)),
        "signErrors": authoritative_signs, "fit": bool(row["accepted_fit"]),
        "bestPhase": trace["bestPhase"], "bestStep": trace["bestStep"], "bestEvaluation": trace["bestEvaluation"],
        "bestStateKind": trace["bestStateKind"], "terminalReason": record["status"],
        "adamSteps": record.get("adam_steps_completed"), "lbfgsEvaluations": record.get("lbfgs_evaluations"),
        "gdSteps": record.get("accepted_steps"), "physicalClock": record.get("physical_clock"),
        "samples64": packed(sample_prediction, "<f8"),
        "circle32": None, "indices16": None, "circleCount": 0, "circleAvailable": circle is not None,
        "circleReason": circle_reason, "precision": precision,
        "circleReplayError": audit.get("circleReplayError"), "circleRoundingError": None,
        "circleInterpolationError": None, "circleMin": None, "circleMax": None, "circleMaxAbs": None,
        "trainable": int(row["trainable_scalars"]), "retained": int(row["retained_predictor_scalars"]),
    }
    if circle is not None:
        indices, values, display = adaptive_circle(circle)
        result.update(circle32=packed(values, "<f4"), indices16=packed(indices, "<u2"), circleCount=len(indices),
                      circleRoundingError=display["roundingError"], circleInterpolationError=display["combinedInterpolationError"],
                      circleMin=display["fullGridMinimum"], circleMax=display["fullGridMaximum"], circleMaxAbs=display["fullGridMaxAbs"])
        audit["display"] = display
        decoded_values = np.frombuffer(base64.b64decode(result["circle32"]), dtype="<f4")
        decoded_indices = np.frombuffer(base64.b64decode(result["indices16"]), dtype="<u2")
        if not np.array_equal(decoded_values, values) or not np.array_equal(decoded_indices, indices):
            raise ValueError("Circle packing failed round-trip")
    decoded_samples = np.frombuffer(base64.b64decode(result["samples64"]), dtype="<f8")
    if not np.array_equal(decoded_samples, sample_prediction):
        raise ValueError("Float64 sample packing failed exact round-trip")
    audit.update(circleAvailable=result["circleAvailable"], circleReason=circle_reason, sampleCount=m, passed=True)
    return result, audit


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=GENERATED / "radial_view01")
    args = parser.parse_args()
    output = args.out.resolve()
    if output.exists() or not output.is_relative_to(GENERATED):
        raise SystemExit("Output must be a fresh directory owned by this study")
    started = time.perf_counter()
    sources = {"adam": GENERATED / "analysis01/analysis.json", "gd": GENERATED / "gd_analysis01/analysis.json"}
    adjudications = read_json(GENERATED / "check_scratch/numerical_adjudications.json")
    records, audits, group_audits, input_hashes = [], [], [], {}
    for round_id, analysis_path in sources.items():
        analysis = read_json(analysis_path)
        input_hashes[str(analysis_path)] = sha256(analysis_path)
        run_root = Path(analysis["run_root"])
        rows = [row for row in analysis["attempts"] if not row["reproduction"]]
        expected = 30 if round_id == "adam" else 39
        if len(rows) != expected or not analysis["all_decisions_valid"]:
            raise ValueError("Checked original-attempt scope changed")
        for row in rows:
            result, audit = export_attempt(round_id, row, run_root, adjudications)
            records.append(result)
            audits.append(audit)
        for group in analysis["groups"]:
            gain = "canonical" if group["initialization"] == "canonical" else "high"
            eta = group.get("eta_max") if round_id == "gd" else None
            members = [row for row in records if row["round"] == round_id and row["model"] == group["model"]
                       and row["m"] == group["m"] and row["gain"] == gain and row["etaMax"] == eta]
            if len(members) != group["attempts"] or sum(row["fit"] for row in members) != group["fits"]:
                raise ValueError("Exported selections/fit counts disagree with checked group")
            group_audits.append({"round": round_id, "model": group["model"], "m": group["m"], "gain": gain,
                                 "etaMax": eta, "attempts": len(members), "fits": sum(row["fit"] for row in members), "passed": True})
    records.sort(key=lambda row: (row["round"], row["m"], row["gain"], row["etaMax"] or 0, row["model"], row["seed"]))
    payload = {
        "version": 1, "circleGrid": GRID, "fitMse": FIT_MSE, "checkpoint": "best saved parameter witness",
        "rounds": [{"id": "adam", "label": "Adam / LBFGS / readout", "selectedM": 254},
                   {"id": "gd", "label": "Full-batch GD + scalar Armijo", "selectedM": 126}],
        "models": [{"id": "width55", "label": "Dense width 55", "width": 55, "trainable": 3190, "retained": 3190},
                   {"id": "closure1024", "label": "Closure n=1024, p=1", "width": 1024, "trainable": 3087, "retained": 11279},
                   {"id": "width105", "label": "Dense width 105", "width": 105, "trainable": 11340, "retained": 11340}],
        "encoding": {"samples64": "base64 little-endian float64 in exact training sample order",
                     "circle32": "base64 little-endian float32 for display only",
                     "indices16": "base64 little-endian uint16, angles 2*pi*index/circleGrid",
                     "trainingAngles": "2*pi*j/m", "trainingLabels": "(-1)^j; no between-sample target"},
        "displayErrorScope": "Interpolation error compares the packed display values to all 8192 original circle nodes; it is not a bound at unsampled angles.",
        "notes": ["Original attempts only; reproductions and unrun combinations are excluded.",
                  "Training markers retain binary64 values; authoritative metric decisions are never recomputed from display-only curves.",
                  "The four high-precision Adam exceptions show checked sample markers only.",
                  "Predictions between labels are model outputs, not a supplied target function.",
                  "No new training or optimization was performed."],
        "records": records,
    }
    encoded = json.dumps(payload, separators=(",", ":"), allow_nan=False).encode()
    compressed = gzip.compress(encoded, compresslevel=9, mtime=0)
    wrapped = base64.b64encode(compressed)
    if gzip.decompress(base64.b64decode(wrapped)) != encoded:
        raise ValueError("Gzip/base64 whole-payload round-trip failed")
    output.mkdir(parents=True)
    (output / "payload.json").write_bytes(encoded)
    (output / "payload.json.gz").write_bytes(compressed)
    (output / "payload.gz.b64").write_bytes(wrapped)
    available = [audit for audit in audits if audit["circleAvailable"]]
    audit_report = {
        "passed": True, "training_performed": False, "exporterSha256": sha256(Path(__file__)),
        "inputAnalysisSha256": input_hashes, "recordCount": len(records),
        "originalCounts": {round_id: sum(row["round"] == round_id for row in records) for round_id in sources},
        "circleCount": len(available), "withheldCircles": [audit["id"] for audit in audits if not audit["circleAvailable"]],
        "maximumCircleReplayError": max(audit["circleReplayError"] for audit in available),
        "maximumCircleRoundingError": max(audit["display"]["roundingError"] for audit in available),
        "maximumCircleInterpolationError": max(audit["display"]["combinedInterpolationError"] for audit in available),
        "interpolationTarget": DISPLAY_TOL,
        "curvesExceedingInterpolationTarget": [audit["id"] for audit in available if not audit["display"]["targetMetBeforeRounding"]],
        "maximumCircleVertices": max(audit["display"]["vertices"] for audit in available),
        "allGlobalExtremaRetained": all(audit["display"]["globalExtremaRetained"] for audit in available),
        "payloadBytes": len(encoded), "gzipBytes": len(compressed), "gzipBase64Bytes": len(wrapped),
        "outputsSha256": {name: sha256(output / name) for name in ("payload.json", "payload.json.gz", "payload.gz.b64")},
        "groups": group_audits, "attempts": audits, "elapsedSeconds": time.perf_counter() - started,
    }
    (output / "audit.json").write_text(json.dumps(audit_report, indent=2, allow_nan=False) + "\n")
    (output / "README.md").write_text(
        "# Audited radial-view payload\n\n"
        f"Contains {len(records)} original best-checkpoint records (Adam 30, GD 39); {len(available)} circle curves and four high-precision sample-only cases.\n\n"
        "The UI decodes gzip/base64 payload.gz.b64 with built-in DecompressionStream. Within JSON, samples64 is little-endian float64; circle32 is little-endian float32; indices16 is little-endian uint16. Training angle j is 2πj/m, label (-1)^j; curve angle is 2πindex/8192.\n\n"
        "Training markers and checked fit decisions are distinct from display-only curves. Four precision-adjudicated Adam cases use existing 90-digit sample predictions converted to binary64, and omit their unchecked float64 circle grid. No between-sample target is defined.\n\n"
        f"Adaptive display sampling retains 128–{MAX_VERTICES} vertices per curve, explicitly including both global extrema. Maximum error against the full 8192-node replayed circle grid after float32 packing: {audit_report['maximumCircleInterpolationError']:.9g}. This is a sampled-grid interpolation discrepancy, not a bound on unsampled angles. Circle extrema are measured on all 8192 nodes; substantial overshoot must not be silently clipped.\n\n"
        f"Payload sizes: JSON {len(encoded)} bytes; gzip {len(compressed)} bytes; embedded gzip/base64 {len(wrapped)} bytes. All selection counts, sample metrics, record/checkpoint/data hashes, packing round-trips and circle replays passed. No training was performed.\n")
    print(json.dumps({key: audit_report[key] for key in ("passed", "recordCount", "circleCount", "maximumCircleReplayError",
        "maximumCircleRoundingError", "maximumCircleInterpolationError", "curvesExceedingInterpolationTarget",
        "payloadBytes", "gzipBytes", "gzipBase64Bytes", "elapsedSeconds")}, indent=2))


if __name__ == "__main__":
    main()
