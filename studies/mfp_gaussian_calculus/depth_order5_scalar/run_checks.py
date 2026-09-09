"""Deterministic exact checks for the flattened arbitrary-depth scalar witness."""

from __future__ import annotations

import json

from .primary.audit_full_scalar_recurrence import run_audit
from .primary.compare_full_independent_recurrences import run as compare_routes
from .verify_canonical_report import verify as verify_report


def main() -> None:
    exact = run_audit()
    independent = compare_routes([1, 2, 3, 4])
    report = verify_report()
    print(
        json.dumps(
            {
                "exact_map_audit": exact["decision"],
                "two_route_sector_audit": independent["decision"],
                "canonical_report": report["decision"],
                "canonical_report_sha256": report["report_sha256"],
                "C_counts": {
                    depth: audit["comparisons"]["C"]["candidate_count"]
                    for depth, audit in exact["depths"].items()
                },
                "C_discrepancies": {
                    depth: audit["comparisons"]["C"]["discrepancy_count"]
                    for depth, audit in exact["depths"].items()
                },
                "maximum_activation_derivative": max(
                    audit["terminal_alphabet"]["derivative_ceiling"]
                    for audit in exact["depths"].values()
                ),
                "nonpolynomial_regression": exact["nonpolynomial_regression"]["decision"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
