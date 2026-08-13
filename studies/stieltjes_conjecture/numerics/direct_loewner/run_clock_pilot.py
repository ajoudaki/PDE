#!/usr/bin/env python3
"""Numerical-validity pilot for the corrected common-clock experiment."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

import corrected_clock_core as core


HERE = Path(__file__).resolve().parent
SEED_BASE = 2026081301
WIDTHS = (64, 128, 256)
PAIR_COUNTS = {64: 24, 128: 16, 256: 8}
S_MAX = 0.003
STEP = 0.00005


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    output = HERE / "runs/clock_pilot_20260813"
    output.mkdir(exist_ok=True)
    summary: dict[str, object] = {
        "status": "validity_pilot_only_not_scientific_evidence",
        "command": " ".join(sys.argv),
        "seed_base": SEED_BASE,
        "s_max": S_MAX,
        "step": STEP,
        "widths": {},
    }
    for width in WIDTHS:
        print(f"START pilot width={width}", flush=True)
        data = core.simulate_pair_curves(
            width, PAIR_COUNTS[width], SEED_BASE, S_MAX, STEP
        )
        np.savez_compressed(output / f"pilot_width_{width}.npz", **data)
        finite_pairs = np.isfinite(data["pair_g"]).sum(axis=0)
        median_g = np.median(np.clip(data["pair_g"], 0.0, 111.0 * width), axis=0)
        F = core.cumulative_simpson_uniform(median_g, STEP)
        item = {
            "pairs": PAIR_COUNTS[width],
            "finite_pairs_min": int(finite_pairs.min()),
            "finite_pairs_at_end": int(finite_pairs[-1]),
            "median_g0": float(median_g[0]),
            "median_g_end": float(median_g[-1]),
            "integrated_output_y_end": float(F[-1]),
            "integrated_output_y_at_s": {
                str(float(data["times"][j])): float(F[j])
                for j in (10, 20, 30, 40, 60)
            },
            "direct_f_median_end": float(
                np.median(np.clip(data["pair_f_direct"][:, -1], 0.0, width))
            ),
            "escape_count": int(np.isfinite(data["escape_time"]).sum()),
        }
        summary["widths"][str(width)] = item
        print(json.dumps({"width": width, **item}, sort_keys=True), flush=True)
    summary_path = output / "pilot_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    files = sorted(output.glob("*.npz")) + [summary_path]
    manifest = {
        path.name: {"sha256": sha256(path), "bytes": path.stat().st_size}
        for path in files
    }
    for source in (Path(__file__), Path(core.__file__)):
        manifest["source/" + source.name] = {
            "sha256": sha256(source), "bytes": source.stat().st_size
        }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
