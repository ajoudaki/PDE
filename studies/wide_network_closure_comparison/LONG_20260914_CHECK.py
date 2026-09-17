#!/usr/bin/env python3
"""Bounded independent arithmetic check, without trajectory reproduction.

Reads only the frozen LONG plan/scope, inputs.npz, all 16 completed stage-640
record/observation/Gram pairs, and the three width-8192 initial stage-40 Grams.
"""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/wide_network_closure_comparison"
BASE = ROOT / "data/generated/wide_network_closure_comparison/LONG_20260914_v1"
CLOSURES = ["N1", "N3", "N3_halfstep", "N3_refined", "N5", "N5_fine", "N5_fine_halfstep", "N5_refined"]
RUNS = [f"network/arcs30_n{n}_s{s}" for n in (2048, 8192) for s in (11, 29, 47)]
RUNS += ["network/arcs30_n2048_s11_float64", "network/arcs30_n8192_s11_halfstep"]
RUNS += [f"closure/arcs30_{c}" for c in CLOSURES]
PANELS = {"training": slice(0, 16), "circle": slice(16, 144)}
TIMES = np.arange(320.0, 641.0, 16.0)
SELECT = [0, 10, 20]


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def rms(a):
    return float(np.linalg.norm(a, "fro") / a.shape[-1])


def main():
    records = {r: json.loads((BASE / r / "stage_000640/record.json").read_text()) for r in RUNS}
    assert len(records) == 16 and all(r["status"] == "complete" for r in records.values())
    hashes = {}

    def remember(path):
        value = digest(path)
        hashes[str(path.relative_to(ROOT))] = value
        return value

    plan_hash = remember(STUDY / "LONG_20260914_PLAN.md")
    remember(STUDY / "LONG_20260914_SANITY_SCOPE.md")
    inputs_hash = remember(BASE / "inputs.npz")
    with np.load(BASE / "inputs.npz", allow_pickle=False) as z:
        labels, weights = z["arcs30_labels"], z["arcs30_probabilities"]
        assert labels.shape == weights.shape == (16,)
        assert z["times"].shape == (206,) and z["times"][0] == 0 and z["times"][-1] == 40
    observations, grams, run_results = {}, {}, {}
    for run, record in records.items():
        folder = BASE / run / "stage_000640"
        remember(folder / "record.json")
        assert record["inputs_sha256"] == inputs_hash and record["plan_sha256"] == plan_hash
        assert remember(folder / "observations.npz") == record["observations_sha256"]
        assert remember(folder / "gram.npy") == record["gram_sha256"]
        assert record["completed_observations"] == record["gram_completed_observations"] == 21
        assert float(record["last_time"]) == record["target"] == 640
        with np.load(folder / "observations.npz", allow_pickle=False) as z:
            o = {k: z[k] for k in z.files}
        assert np.array_equal(o["times"], TIMES)
        assert all(a.shape[0] == 21 and np.isfinite(a).all() for a in o.values())
        g = np.load(folder / "gram.npy", mmap_mode="r", allow_pickle=False)
        assert g.shape == (21, 2, 144, 144) and np.isfinite(g).all()
        assert np.array_equal(g, g.swapaxes(-1, -2)) and np.abs(g).max() <= 1 + 2e-11
        minima = [float(np.linalg.eigvalsh(g[-1, layer])[0]) for layer in range(2)]
        assert min(minima) >= -2e-11
        computed_loss = ((o["data_predictions"] - labels) ** 2 * weights).sum(axis=1)
        loss_gap = float(np.max(np.abs(computed_loss - o["loss"])))
        tolerance = 2e-6 if record.get("dtype") == "float32" else 2e-11
        assert loss_gap <= tolerance
        diagonal = (np.diagonal(g[:, :, :16, :16], axis1=-2, axis2=-1) * weights).sum(axis=-1)
        diagonal_gap = float(np.max(np.abs(diagonal - o["raw_rms"] ** 2)))
        assert diagonal_gap <= tolerance
        run_results[run] = {
            "loss_320_480_640": o["loss"][SELECT].tolist(),
            "relative_loss_change_480_to_640": float(o["loss"][-1] / o["loss"][10] - 1),
            "gram_rms_change_480_to_640": {
                panel: [rms(g[20, layer, s, s] - g[10, layer, s, s]) for layer in range(2)]
                for panel, s in PANELS.items()},
            "endpoint_full_gram_minimum_eigenvalues": minima,
            "maximum_loss_from_predictions_error": loss_gap,
            "maximum_weighted_gram_diagonal_raw_rms_squared_error": diagonal_gap,
        }
        observations[run], grams[run] = o, g

    means = {n: sum(grams[f"network/arcs30_n{n}_s{s}"] for s in (11, 29, 47)) / 3 for n in (2048, 8192)}
    mean_losses = {str(n): np.mean([observations[f"network/arcs30_n{n}_s{s}"]["loss"][SELECT]
                                  for s in (11, 29, 47)], axis=0).tolist() for n in means}
    errors = {}
    for c in CLOSURES:
        g = grams[f"closure/arcs30_{c}"]
        errors[c] = {str(n): {panel: [[rms(g[t, layer, s, s] - mean[t, layer, s, s])
                                      for layer in range(2)] for t in SELECT]
                              for panel, s in PANELS.items()} for n, mean in means.items()}
    initial = []
    for seed in (11, 29, 47):
        path = BASE / f"network/arcs30_n8192_s{seed}/stage_000040/gram.npy"
        remember(path)
        g = np.load(path, mmap_mode="r", allow_pickle=False)
        assert g.shape == (206, 2, 144, 144) and np.isfinite(g[0]).all()
        initial.append(g[0])
    frozen = np.mean(initial, axis=0)
    baseline = {panel: [rms(means[8192][-1, layer, s, s] - frozen[layer, s, s])
                        for layer in range(2)] for panel, s in PANELS.items()}
    result = {
        "scope": "Independent saved-array arithmetic only; no producer audit, trajectory reproduction, or promotion review.",
        "sample_times": [320, 480, 640], "layer_order": [1, 2],
        "formula": "Matrix RMS = ||A||_F/m; mean three seeded network Gram matrices before taking the norm; loss = sum_i p_i(f_i-y_i)^2.",
        "checks": {"all_16_records_complete": True, "record_input_plan_and_output_hashes": True,
                   "exact_21_times_and_counts": True, "finite_symmetry_range": True,
                   "endpoint_psd_tolerance": 2e-11, "loss_and_diagonal_identities": True},
        "network_three_seed_mean_losses": mean_losses,
        "runs": run_results, "closure_gram_error_320_480_640": errors,
        "frozen_width8192_endpoint_error": baseline,
        "input_hashes": hashes, "checker_source_sha256": digest(Path(__file__)),
        "command": "OPENBLAS_NUM_THREADS=1 python studies/wide_network_closure_comparison/LONG_20260914_CHECK.py",
        "numpy_version": np.__version__,
        "limitations": ["Only supplied stage-640 records/arrays and three initial Grams were checked.",
                        "Prior checkpoint/source hashes are recorded upstream but their targets are outside this check's input scope.",
                        "Initial stage-40 Gram hashes are retained here without reading their stage records."]}
    with (BASE / "independent_final_check.json").open("x") as f:
        json.dump(result, f, indent=2, allow_nan=False)
        f.write("\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("input_hashes", "runs", "closure_gram_error_320_480_640")}, indent=2))
    print("closure loss / training error vs8192 at 320,480,640")
    for c in CLOSURES:
        print(c, run_results[f"closure/arcs30_{c}"]["loss_320_480_640"], errors[c]["8192"]["training"])
    print("run late Gram changes (training L1,L2; circle L1,L2)")
    for run, d in run_results.items():
        print(run, d["gram_rms_change_480_to_640"])


if __name__ == "__main__":
    main()
