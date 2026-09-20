"""Render the eight validated scaling configurations from saved endpoint curves.

Only display sampling/rounding is performed. RMS values are copied unchanged
from the final analysis, never recomputed from the downsampled display curves.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

from scaling_cases import CONFIRMATION, DISCOVERY

STUDY = "random_dictionary_learned_circle_20260920"
HERE = Path(__file__).resolve().parent
DATA_ROOT = HERE.parents[1] / "data" / "generated" / STUDY
METHODS = ("ours", "gaussian", "orthogonal")
SOURCES = (
    ("scaling_discovery_analysis01", DISCOVERY),
    ("scaling_confirm1_analysis02", CONFIRMATION[1]),
    ("scaling_confirm2_analysis03", CONFIRMATION[2]),
)
TITLES = {
    "quadrant_pairs": "Paired discovery",
    "pairs_confirm1": "Paired fresh 1",
    "pairs_confirm2": "Paired fresh 2",
    "two_outliers_alternating": "Outlier discovery",
    "outliers_confirm1": "Outlier fresh 1",
    "outliers_confirm2": "Outlier fresh 2",
    "negative_confirm1": "Negative control fresh 1",
    "negative_confirm2": "Negative control fresh 2",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def export(out):
    out = out.resolve()
    if not out.is_relative_to(DATA_ROOT.resolve()) or out == DATA_ROOT.resolve():
        raise ValueError("Output must be a new directory within this study's generated data")
    cases, inputs = {}, {}
    sample_count, grid_count, decimals = 1024, 8192, 6
    stride = grid_count // sample_count
    for analysis_name, geometries in SOURCES:
        analysis = DATA_ROOT / analysis_name
        for name in ("metrics.json", "summary.json", "circle_errors.npz"):
            path = analysis / name
            inputs[str(path)] = sha256(path)
        rows = json.loads((analysis / "metrics.json").read_text())
        summary = json.loads((analysis / "summary.json").read_text())
        expected = {(case, method, p) for case in geometries for p in summary["orders"] for method in METHODS}
        assert {(r["case"], r["method"], r["order"]) for r in rows} == expected
        assert len(rows) == len(expected) and all(r["valid"] and r["refined_eligible"] for r in rows)
        with np.load(analysis / "circle_errors.npz", allow_pickle=False) as arrays:
            for case, geometry in geometries.items():
                case_rows = [r for r in rows if r["case"] == case]
                first = case_rows[0]
                ref_key = case + "_full_refined"
                angles, ref_inputs = arrays[ref_key + "_angles"], arrays[ref_key + "_inputs"]
                assert angles.shape == (grid_count,)
                assert np.allclose(angles, np.arange(grid_count) * (2 * np.pi / grid_count), rtol=0, atol=1e-14)
                extent = max(abs(v) for v in geometry["labels"])

                def curve(key):
                    nonlocal extent
                    assert np.array_equal(arrays[key + "_angles"], angles)
                    assert np.array_equal(arrays[key + "_inputs"], ref_inputs)
                    values = arrays[key + "_prediction"]
                    assert values.shape == (grid_count,) and np.isfinite(values).all()
                    extent = max(extent, float(np.abs(values).max()))
                    return np.round(values[::stride], decimals).tolist()

                reference = {"curve": curve(ref_key), "time": first["full_refined_time"],
                             "mse": first["full_refined_loss"], "rtol": first["full_refined_rtol"],
                             "atol": first["full_refined_atol"]}
                orders = []
                for p in sorted(summary["orders"]):
                    selected = {r["method"]: r for r in case_rows if r["order"] == p}
                    base = selected["ours"]
                    item = {"p": p, "k1": base["k1"], "k2": base["k2"],
                            "columns": base["dictionary_columns"], "models": {}}
                    for method in METHODS:
                        row = selected[method]
                        assert row["full_refined_directory"] == first["full_refined_directory"]
                        assert (row["k1"], row["k2"], row["dictionary_columns"]) == (item["k1"], item["k2"], item["columns"])
                        assert row["refined_status"] == row["full_refined_status"] == "fitted"
                        item["models"][method] = {
                            "curve": curve(f"{case}_{method}_p{p}_refined"),
                            "rms": row["refined_l2"], "time": row["refined_time"],
                            "mse": row["refined_loss"], "rtol": row["refined_rtol"], "atol": row["refined_atol"],
                        }
                    orders.append(item)
                cases[case] = {"id": case, "label": TITLES[case],
                               "anglesDegrees": geometry["angles_degrees"], "labels": geometry["labels"],
                               "width": summary["width"], "threshold": summary["threshold"],
                               "networkSeed": summary["network_seed"], "dictionarySeed": summary["dictionary_seed"],
                               "extent": extent, "reference": reference, "orders": orders}
    data = {"schema": 1, "level": "selected finer", "gridCount": grid_count,
            "sampleCount": sample_count, "sampleStride": stride, "roundDecimals": decimals,
            "cases": [cases[key] for key in TITLES]}
    encoded = json.dumps(data, separators=(",", ":"), allow_nan=False).encode()
    template = HERE / "scaling_radial_template.html"
    markup = template.read_text()
    assert markup.count("__SCALING_PAYLOAD__") == 1
    markup = markup.replace("__SCALING_PAYLOAD__", base64.b64encode(gzip.compress(encoded, mtime=0)).decode())
    assert len(markup.encode()) < 1_000_000
    out.mkdir(parents=True, exist_ok=False)
    (out / "viewer_data.json").write_bytes(encoded)
    (out / "scaling-circle-experiments.html").write_text(markup)
    sources = [Path(__file__).resolve(), template, HERE / "scaling_cases.py", HERE / "diverse_cases.py"]
    provenance = {"command": sys.argv, "sources": {str(p): sha256(p) for p in sources},
                  "inputs": inputs, "outputs": {p.name: sha256(p) for p in out.iterdir()},
                  "cases": list(TITLES), "curves": 104, "comparisons": 96,
                  "display": {"angles": sample_count, "stride": stride, "round_decimals": decimals},
                  "metrics": "Exact saved refined_l2 from 8192 angles; no metric recomputation or training",
                  "reference": "Each case's shared current full_refined_prediction; not historical_full",
                  "endpoints": "Each predictor's own first detected training-MSE threshold crossing",
                  "scale": "Fixed across p and visible methods within each case, using all full-grid curve extents"}
    (out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({"out": str(out), "fragment_bytes": len(markup.encode()), "cases": len(cases), "curves": 104}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    export(parser.parse_args().out)
