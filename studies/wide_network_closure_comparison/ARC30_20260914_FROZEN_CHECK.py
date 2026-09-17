#!/usr/bin/env python3
"""Independent arithmetic check of the ARC30 frozen activation-Gram baseline.

Inputs are restricted to inputs.npz and the four specified raw Gram/record pairs.
No trajectory, existing analysis, other study, or maintained model code is read.
Run from /home/amir/Codes/PDE with:
    python studies/wide_network_closure_comparison/ARC30_20260914_FROZEN_CHECK.py
"""

import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/generated/wide_network_closure_comparison/ARC30_20260914_v1"
DEST = ROOT / "data/generated/wide_network_closure_comparison/ARC30_20260914_frozen_baseline_v1/independent_check.json"
RUNS = [f"network/arcs30_n8192_s{seed}" for seed in (11, 29, 47)]
RUNS.append("closure/arcs30_N5_fine")


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def frobenius_rms(matrix):
    """||A||_F/m for an m-by-m matrix, evaluated by a matrix norm."""
    assert matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]
    return float(np.linalg.norm(matrix, ord="fro") / matrix.shape[0])


def checked_extrema(series, times):
    index = int(np.argmax(series))
    return {"max": float(series[index]), "max_time": float(times[index]),
            "terminal": float(series[-1]), "initial": float(series[0])}


def main():
    input_hashes = {str((BASE / "inputs.npz").relative_to(ROOT)): sha256(BASE / "inputs.npz")}
    with np.load(BASE / "inputs.npz", allow_pickle=False) as inputs:
        times = inputs["times"].copy()
        assert inputs["arcs30_inputs"].shape == (16, 2)
        assert inputs["circle"].shape == (128, 2)
    assert times.ndim == 1 and times[0] == 0.0 and np.all(np.diff(times) > 0)
    grams = []
    for run in RUNS:
        pair = BASE / run
        record = json.loads((pair / "record.json").read_text())
        for name in ("record.json", "gram.npy"):
            file = pair / name
            input_hashes[str(file.relative_to(ROOT))] = sha256(file)
        assert record["status"] == "complete"
        assert record["gram_completed_observations"] == len(times)
        assert float(record["last_time"]) == times[-1]
        assert record["gram_sha256"] == input_hashes[str((pair / "gram.npy").relative_to(ROOT))]
        declared_inputs_hash = record.get("inputs_sha256", record.get("inputs_npz_sha256"))
        assert declared_inputs_hash == input_hashes[str((BASE / "inputs.npz").relative_to(ROOT))]
        gram = np.load(pair / "gram.npy", mmap_mode="r", allow_pickle=False)
        assert gram.shape == (len(times), 2, 144, 144)
        assert list(gram.shape) == record["gram_shape"]
        assert gram.dtype == np.float64 and np.all(np.isfinite(gram))
        assert np.array_equal(gram, gram.swapaxes(-2, -1))
        grams.append(gram)

    panels = {}
    maximum_oracle_absolute_discrepancy = 0.0
    for panel, selection in (("training", slice(0, 16)), ("circle", slice(16, 144))):
        panels[panel] = {}
        for layer in range(2):
            # Average matrices before computing norms, as explicitly assigned.
            observed = np.stack([g[:, layer, selection, selection] for g in grams[:3]]).mean(axis=0)
            closure = grams[3][:, layer, selection, selection]
            differences = (observed - observed[0], closure - observed)
            e0, e5 = [np.array([frobenius_rms(a) for a in delta]) for delta in differences]
            magnitude = np.array([frobenius_rms(a) for a in observed])
            assert e0[0] == 0.0 and magnitude[0] > 0 and magnitude[-1] > 0
            # A scalar compensated sum provides an independent norm oracle at
            # each error curve's maximum and at the terminal observation.
            for delta, errors in zip(differences, (e0, e5)):
                for index in {0, int(np.argmax(errors)), len(times) - 1}:
                    a = delta[index]
                    oracle = math.sqrt(math.fsum(float(x) ** 2 for x in a.flat)) / a.shape[0]
                    gap = abs(oracle - errors[index])
                    maximum_oracle_absolute_discrepancy = max(maximum_oracle_absolute_discrepancy, gap)
                    assert math.isclose(oracle, errors[index], rel_tol=2e-14, abs_tol=1e-16)
            frozen_wins = e0 < e5
            transitions = np.flatnonzero(frozen_wins[:-1] != frozen_wins[1:])
            panels[panel][f"layer_{layer + 1}"] = {
                "m": int(observed.shape[-1]),
                "frozen_error": checked_extrema(e0, times),
                "closure_error": checked_extrema(e5, times),
                "ratio_max_frozen_to_max_closure": float(e0.max() / e5.max()),
                "ratio_terminal_frozen_to_terminal_closure": float(e0[-1] / e5[-1]),
                "initial_gram_frobenius_over_m": float(magnitude[0]),
                "terminal_gram_frobenius_over_m": float(magnitude[-1]),
                "max_movement_relative_to_initial_gram": float(e0.max() / magnitude[0]),
                "terminal_movement_relative_to_initial_gram": float(e0[-1] / magnitude[0]),
                "max_movement_relative_to_terminal_gram": float(e0.max() / magnitude[-1]),
                "terminal_movement_relative_to_terminal_gram": float(e0[-1] / magnitude[-1]),
                "sampled_times_frozen_strictly_beats_closure": times[frozen_wins].tolist(),
                "sampled_times_equal_error": times[e0 == e5].tolist(),
                "frozen_win_transition_brackets": [[float(times[i]), float(times[i + 1])] for i in transitions],
                "frozen_error_curve": e0.tolist(),
                "closure_error_curve": e5.tolist(),
            }

    result = {
        "format": "arc30-frozen-baseline-independent-arithmetic-v1",
        "claim_type": "empirical postprocessing of retained arrays",
        "scope": "Independent arithmetic cross-check; no trajectory reproduction and no promotion review.",
        "inputs": input_hashes,
        "source_sha256": sha256(Path(__file__)),
        "command": "python studies/wide_network_closure_comparison/ARC30_20260914_FROZEN_CHECK.py",
        "working_directory": str(ROOT),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "seeds": [11, 29, 47],
        "width": 8192,
        "training_indices_half_open": [0, 16],
        "circle_indices_half_open": [16, 144],
        "formulas": {
            "network_mean": "Gbar(t) = (G_seed11(t) + G_seed29(t) + G_seed47(t))/3",
            "frozen": "E0(t) = ||Gbar(t)-Gbar(0)||_F/m",
            "closure": "E5(t) = ||G_N5_fine(t)-Gbar(t)||_F/m",
            "max_ratio": "max_t E0(t) / max_t E5(t)",
            "relative_initial_movement": "||Gbar(t)-Gbar(0)||_F / ||Gbar(0)||_F",
            "relative_terminal_movement": "||Gbar(t)-Gbar(0)||_F / ||Gbar(T)||_F",
        },
        "checks": {"input_hashes_match_records": True,
                   "shapes_completion_times_finiteness_and_exact_symmetry": True,
                   "zero_initial_frozen_error": True,
                   "compensated_scalar_norm_oracle_maximum_absolute_discrepancy": maximum_oracle_absolute_discrepancy},
        "times": times.tolist(),
        "panels": panels,
        "limitations": ["Maxima and comparison times concern the saved 206 observations only.",
                        "Transition brackets do not establish a continuous-time crossing location.",
                        "The baseline is each panel's empirical seed-mean initial activation Gram.",
                        "No NTK, predictor, loss, trajectory or producer implementation is evaluated."],
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with DEST.open("x") as output:
        json.dump(result, output, indent=2, allow_nan=False)
        output.write("\n")
    print(json.dumps({"output": str(DEST), "checks": result["checks"],
                      "panels": {p: {l: {k: v for k, v in d.items() if not k.endswith("_curve")}
                                      for l, d in q.items()} for p, q in panels.items()}}, indent=2))


if __name__ == "__main__":
    main()
