"""Deterministic publication gate for the independent Gamma04 route."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .compare_route_a import compare as compare_route_a
from .run_exact_audit import run as run_exact


HERE = Path(__file__).resolve().parent


def main() -> None:
    exact = run_exact()
    routes = compare_route_a()
    sine = json.loads((HERE / "NORMALIZED_SINE_EXPERIMENT.json").read_text())
    final_freeze = HERE / "FINAL_PRODUCER_FREEZE.json"
    results = {
        "exact_audit": exact["decision"],
        "population_discrepancies": {
            depth: record["total_discrepancies"]
            for depth, record in exact["population_atomwise_comparisons"].items()
        },
        "two_state_projection_discrepancies": {
            depth: record["total_discrepancies"]
            for depth, record in exact["two_state_projection_comparisons"].items()
        },
        "route_comparison": routes["decision"],
        "sine_regression": sine["decision"],
        "final_producer_freeze_sha256": hashlib.sha256(final_freeze.read_bytes()).hexdigest(),
    }
    passed = (
        exact["decision"] == "pass"
        and all(value == 0 for value in results["population_discrepancies"].values())
        and all(value == 0 for value in results["two_state_projection_discrepancies"].values())
        and routes["decision"].startswith("pass:")
        and sine["decision"] == "pass"
    )
    results["decision"] = "pass" if passed else "fail"
    print(json.dumps(results, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
