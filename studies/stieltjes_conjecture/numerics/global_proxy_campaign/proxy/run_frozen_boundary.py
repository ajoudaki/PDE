#!/usr/bin/env python3
"""Run and preserve the preregistered exact variance-boundary calibration."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import platform
import sys
import time

from proxy.boundary_benchmark import benchmark_boundary


HERE = Path(__file__).resolve().parent
CAMPAIGN = HERE.parent
OUTPUT = CAMPAIGN / "boundary_result.json"
EXPECTED_PROTOCOL_SHA256 = (
    "8e52c717e7a1f3c80fd3549231556dd0127974f5460d32ca199cfb116893855c"
)
SOURCE_NAMES = (
    "boundary_benchmark.py",
    "curves.py",
    "exact_series.py",
    "hierarchy.py",
    "variance_boundary.py",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    protocol = CAMPAIGN / "PROTOCOL.md"
    if sha256(protocol) != EXPECTED_PROTOCOL_SHA256:
        raise RuntimeError("frozen protocol hash mismatch")
    if OUTPUT.exists():
        raise FileExistsError(f"refusing to overwrite {OUTPUT}")

    started = time.monotonic()
    result = benchmark_boundary(grid_points=501, y_max=0.99).record()
    elapsed = time.monotonic() - started
    rational = result["rational_levels"]
    brackets = result["brackets"]
    side_tolerance = 2.0e-13
    gates = {
        "grid_is_frozen": result["grid_points"] == 501 and result["y_max"] == 0.99,
        "all_rational_sides_valid": all(
            level["maximum_side_violation"] <= side_tolerance
            for level in rational
        ),
        "brackets_nested": all(
            right["sup_log_width"] < left["sup_log_width"]
            for left, right in zip(brackets, brackets[1:])
        ),
        "reference_inside_every_bracket": all(
            bracket["maximum_reference_escape"] <= side_tolerance
            for bracket in brackets
        ),
        "final_sup_log_kernel_error_below_1e_minus_5": (
            rational[-1]["sup_log_kernel_error"] < 1.0e-5
        ),
        "wall_below_120_seconds": elapsed < 120.0,
    }
    payload = {
        "status": "pass" if all(gates.values()) else "fail",
        "claim_scope": (
            "exact no-width Lambert-W boundary calibration; not evidence for "
            "the canonical finite-width/global bridge"
        ),
        "protocol_sha256": sha256(protocol),
        "source_sha256": {
            name: sha256(HERE / name) for name in SOURCE_NAMES
        },
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
        },
        "elapsed_seconds": elapsed,
        "gates": gates,
        "benchmark": result,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "output": str(OUTPUT),
        "output_sha256": sha256(OUTPUT),
        "elapsed_seconds": elapsed,
        "gates": gates,
    }, indent=2, sort_keys=True))
    return 0 if payload["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
