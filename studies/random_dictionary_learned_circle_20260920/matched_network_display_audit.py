"""Independent saved-data export audit; no scientific metric calculation.

Archived from matched_network_preview01/display_audit.py. Audit assertions are
unchanged; explicit input paths and an exclusive output path make it reusable.
The original executed scratch copy and its evidence remain preserved.
"""
import argparse
import base64
import csv
import gzip
import hashlib
import json
from pathlib import Path
import re

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / "data" / "generated" / HERE.name
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--analysis", type=Path, required=True)
parser.add_argument("--plots", type=Path, required=True)
parser.add_argument("--radial", type=Path, required=True)
parser.add_argument("--display", type=Path, required=True)
parser.add_argument("--out", type=Path, required=True, help="Fresh JSON output; existing files are never replaced")
parser.add_argument("--browser-checks", type=Path,
                    default=BASE / "matched_network_preview01" / "browser_checks.json")
args = parser.parse_args()
ANALYSIS, PLOTS, RADIAL, DISPLAY, OUT, BROWSER_CHECKS = (
    value.resolve() for value in (args.analysis, args.plots, args.radial, args.display,
                                  args.out, args.browser_checks))
if OUT.exists():
    raise FileExistsError(f"Refusing to replace existing audit output: {OUT}")


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


rows = json.loads((ANALYSIS / "metrics.json").read_text())
selection = json.loads((ANALYSIS / "selected_levels.json").read_text())
payload = json.loads((RADIAL / "viewer_data.json").read_text())
markup = DISPLAY.read_text()
assert markup == (RADIAL / "matched-network-width1024.html").read_text()
assert len(markup.encode()) < 1_000_000
assert not re.search(r"<!doctype|<html|<head>|<body", markup, flags=re.I)
encoded = re.search(r'<script data-role="payload" type="application/octet-stream">([^<]+)</script>', markup).group(1)
assert json.loads(gzip.decompress(base64.b64decode(encoded))) == payload
assert payload["gridCount"] == 8192 and payload["sampleCount"] == 1024
assert payload["sampleStride"] == 8 and payload["roundDecimals"] == 6
assert len(payload["cases"]) == 2
curves = 0
with np.load(ANALYSIS / "pointwise_circle_errors.npz", allow_pickle=False) as arrays:
    for case in payload["cases"]:
        assert case["anglesDegrees"] == selection["cases"][case["id"]]["angles_degrees"]
        assert case["labels"] == selection["cases"][case["id"]]["labels"]
        assert [order["p"] for order in case["orders"]] == [1, 3, 5]
        models = {"full": case["reference"]}
        for order in case["orders"]:
            assert set(order["models"]) == {"ours", "small_trainable", "small_total"}
            for method, data in order["models"].items():
                model = f"{method}_p{order['p']}"
                row = next(r for r in rows if r["case"] == case["id"] and r["model"] == model)
                assert data["rms"] == row["refined_rms"]
                assert (data["width"], data["trainable"], data["total"]) == (
                    row["width"], row["trainable_parameters"], row["model_parameters"])
                models[model] = data
        assert len(models) == 10
        for model, data in models.items():
            pair = selection["cells"][case["id"] + "_" + model]
            record = pair["refined"]
            assert data["trainable"] == record["actual_trainable_parameters"]
            assert data["total"] == record["actual_model_parameters"]
            for label, field in (("level", "level"), ("rtol", "rtol"), ("atol", "atol"), ("time", "time"), ("mse", "loss")):
                assert data[label] == record[field]
            expected = np.round(arrays[case["id"] + "_" + model + "_refined_prediction"][::8], 6)
            assert np.array_equal(np.array(data["curve"]), expected)
            curves += 1
with (PLOTS / "plotted_rms.csv").open() as stream:
    exported = list(csv.DictReader(stream))
assert len(exported) == len(rows) == 18
for exported_row in exported:
    row = next(r for r in rows if (r["case"], r["model"]) == (exported_row["case"], exported_row["model"]))
    for level in ("primary", "refined"):
        assert float(exported_row[level + "_rms"]) == row[level + "_rms"]
        assert exported_row[level + "_directory"] == row[level + "_directory"]
    for field in ("width", "order", "k1", "k2", "dictionary_vectors", "trainable_parameters", "model_parameters"):
        assert int(exported_row[field]) == row[field]
traces = {}
with (PLOTS / "training_mse.csv").open() as stream:
    for row in csv.DictReader(stream):
        key = (row["case"], row["model"], row["selected"])
        traces.setdefault(key, []).append(row)
assert len(traces) == 40
samples = 0
for (case, model, level), trace in traces.items():
    record = selection["cells"][case + "_" + model][level]
    with np.load(Path(record["directory"]) / "arrays.npz", allow_pickle=False) as arrays:
        assert len(trace) == len(arrays["times"]) == len(arrays["losses"])
        for index, row in enumerate(trace):
            assert int(row["sample_index"]) == index
            assert row["directory"] == record["directory"]
            assert int(row["numerical_level"]) == record["level"]
            assert float(row["physical_time"]) == arrays["times"][index]
            assert float(row["training_mse"]) == arrays["losses"][index]
    samples += len(trace)
for folder in (PLOTS, RADIAL):
    provenance = json.loads((folder / "provenance.json").read_text())
    outputs = provenance.get("output_hashes", provenance.get("outputs"))
    for filename, expected in outputs.items():
        assert digest(folder / filename) == expected
    sources = provenance.get("source_hashes", provenance.get("sources"))
    for filename, expected in sources.items():
        assert digest(filename) == expected
browser = json.loads(BROWSER_CHECKS.read_text())
assert browser["passed"] and not browser["errors"]
result = dict(passed=True, curves=curves, exact_rms_rows=len(rows), exact_selected_traces=len(traces),
    exact_training_samples=samples, display_sha256=digest(DISPLAY),
    source_sha256=digest(__file__), scientific_recomputation=False,
    checks=["fragment equals durable export", "decoded embedded payload equals saved JSON", "20 saved finer curves downsampled every 8 angles and rounded to 6 decimals",
            "every displayed parameter count equals independent raw-state audit", "18 RMS CSV rows exactly match saved analysis", "40 CSV loss traces exactly match saved raw arrays",
            "all source/output provenance hashes current", "browser checks pass"])
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("x") as stream:
    stream.write(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
