"""Export selected saved matched-network predictions as a radial comparison.

Only display subsampling and rounding occur. RMS values are copied from the
8192-angle analysis; the displayed curves are never used to recalculate them.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import json
from pathlib import Path
import sys

import numpy as np

from matched_network_plots import (CASES, DATA_ROOT, DIMENSIONS, HERE, METHODS,
                                   ORDERS, WIDTH, digest, owned, read_inputs)


def export(analysis, out, allow_unresolved=False, display_path=None):
    analysis, out = owned(analysis), owned(out)
    if out.exists():
        raise FileExistsError(out)
    rows, summary, selection, _, hashes = read_inputs(analysis, allow_unresolved)
    arrays_path = analysis / "pointwise_circle_errors.npz"
    hashes[str(arrays_path)] = digest(arrays_path)
    cases, sample_count, grid_count, decimals = [], 1024, 8192, 6
    stride = grid_count // sample_count
    with np.load(arrays_path, allow_pickle=False) as arrays:
        for case, title in CASES.items():
            angles = arrays[f"{case}_angles"]
            if angles.shape != (grid_count,) or not np.allclose(
                    angles, np.arange(grid_count) * (2 * np.pi / grid_count), rtol=0, atol=1e-14):
                raise ValueError("Unexpected analysis circle grid")
            geometry = selection["cases"][case]
            extent = max(abs(v) for v in geometry["labels"])

            def curve(model):
                nonlocal extent
                values = arrays[f"{case}_{model}_refined_prediction"]
                if values.shape != (grid_count,) or not np.isfinite(values).all():
                    raise ValueError(f"Malformed selected prediction: {case} {model}")
                extent = max(extent, float(np.abs(values).max()))
                return np.round(values[::stride], decimals).tolist()

            def metadata(model, width, trainable, total, rms=None, valid=None):
                pair = selection["cells"][f"{case}_{model}"]
                record = pair["refined"]
                return dict(curve=curve(model), width=width, trainable=trainable,
                    total=total, rms=rms, time=record["time"], mse=record["loss"],
                    level=record["level"], rtol=record["rtol"], atol=record["atol"],
                    valid=pair["valid"] if valid is None else valid,
                    reasons=pair["reasons"], refinementMax=pair["refinement_endpoint_max"])

            reference = metadata("full", WIDTH, WIDTH ** 2 + 3 * WIDTH, WIDTH ** 2 + 3 * WIDTH)
            orders = []
            for p in ORDERS:
                k1, k2 = DIMENSIONS[p]
                models = {}
                for method in METHODS:
                    row = next(r for r in rows if (r["case"], r["method"], r["order"]) == (case, method, p))
                    models[method] = metadata(row["model"], row["width"], row["trainable_parameters"],
                        row["model_parameters"], row["refined_rms"], row["valid"])
                orders.append(dict(p=p, k1=k1, k2=k2, columns=k1 + k2, models=models))
            cases.append(dict(id=case, label=title, anglesDegrees=geometry["angles_degrees"],
                labels=geometry["labels"], width=WIDTH, threshold=summary["threshold"],
                extent=extent, reference=reference, orders=orders))
    data = dict(schema=1, level="selected finer", gridCount=grid_count,
                sampleCount=sample_count, sampleStride=stride, roundDecimals=decimals, cases=cases)
    encoded = json.dumps(data, separators=(",", ":"), allow_nan=False).encode()
    template = HERE / "matched_network_radial_template.html"
    markup = template.read_text()
    token = "__MATCHED_NETWORK_PAYLOAD__"
    if markup.count(token) != 1:
        raise ValueError("Expected a single radial payload placeholder")
    markup = markup.replace(token, base64.b64encode(gzip.compress(encoded, mtime=0)).decode())
    if len(markup.encode()) >= 1_000_000:
        raise ValueError("Inline fragment exceeds the display-size limit")
    out.mkdir(parents=True)
    (out / "viewer_data.json").write_bytes(encoded)
    (out / "matched-network-width1024.html").write_text(markup)
    if display_path is not None:
        display_path = Path(display_path).resolve()
        display_path.write_text(markup)
    source_paths = [Path(__file__).resolve(), HERE / "matched_network_plots.py", template]
    provenance = dict(command=[sys.executable, "-B", *sys.argv],
        sources={str(path): digest(path) for path in source_paths}, inputs=hashes,
        outputs={path.name: digest(path) for path in out.iterdir()},
        analysis=str(analysis), display_path=str(display_path) if display_path else None,
        display_sha256=digest(display_path) if display_path else None,
        cases=list(CASES), curves=20, orders=list(ORDERS),
        display=dict(angles=sample_count, stride=stride, round_decimals=decimals),
        metrics="Saved refined_rms on 8192 angles; never recalculated from display curves",
        levels="Per-cell latest selected numerical level, including selected extra-resolution runs",
        unresolved={cell: pair["reasons"] for cell, pair in selection["cells"].items() if not pair["valid"]},
        scale="Per-case common radial scale across all p and all visible/hidden methods; extent uses all saved full-grid outputs and labels",
        endpoints="Each predictor's own first detected MSE threshold crossing",
        scope="Read-only saved predictions, scalar metrics, and parameter counts; no scientific recomputation or training")
    (out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps(dict(out=str(out), fragment_bytes=len(markup.encode()), cases=len(cases), curves=20)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--display-path", type=Path)
    parser.add_argument("--allow-unresolved", action="store_true")
    args = parser.parse_args()
    export(args.analysis, args.out, args.allow_unresolved, args.display_path)
