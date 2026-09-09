#!/usr/bin/env python3
"""Exact depth-one identity jet and all-order Stieltjes audit."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

try:
    from .identity_order13_stieltjes_audit import (
        audit_depth_order13,
        load_reversion_route,
    )
except ImportError:  # Allow direct execution from this directory.
    from identity_order13_stieltjes_audit import (
        audit_depth_order13,
        load_reversion_route,
    )


Q = Fraction
HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "DEPTH1_ORDER13_PROTOCOL.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def catalan_scaled(index: int) -> Fraction:
    if index < 0:
        raise ValueError("moment index must be nonnegative")
    catalan = math.comb(2 * index, index) // (index + 1)
    return Q(catalan, 4**index)


def depth1_derivatives(max_order: int = 13) -> list[int]:
    if max_order < 0:
        raise ValueError("maximum order must be nonnegative")
    return [0 if order % 2 == 0 else 2**order for order in range(max_order + 1)]


def build_audit() -> dict[str, object]:
    derivatives = depth1_derivatives(13)
    result = audit_depth_order13(1, derivatives, load_reversion_route())
    moments = tuple(
        Q(record["exact"]) for record in result["moments"].values()
    )
    expected = tuple(catalan_scaled(index) for index in range(6))
    if moments != expected:
        raise AssertionError(f"Catalan moment formula failed: {moments} != {expected}")
    if not result["all_23_accessible_minors_positive"]:
        raise AssertionError("an order-thirteen-accessible Hankel minor failed")
    return result


def compact_minor_records(
    records: dict[str, dict[str, object]]
) -> dict[str, str]:
    return {formula: str(record["exact"]) for formula, record in records.items()}


def main() -> int:
    result = build_audit()
    payload = {
        "format": "depth1-identity-order13-all-order-stieltjes-v1",
        "model": "one-hidden-layer identity feature-ascent",
        "finite_width_flow": "A'=u, u'=A",
        "width_limit_feature": "F(t)=sinh(2t)",
        "output_kernel": "K(y)=2*sqrt(1+y^2)",
        "derivatives": depth1_derivatives(13),
        "moments": {
            f"mu_{index}": str(catalan_scaled(index))
            for index in range(6)
        },
        "all_order_moment_formula": "mu_r=Catalan(r)/4^r",
        "representing_measure": (
            "dnu(x)=(2/pi)*sqrt((1-x)/x)*1_(0,1)(x) dx"
        ),
        "new_shifted_H_2_plus": result["new_shifted_H_2_plus"],
        "accessible_minors": {
            size: compact_minor_records(records)
            for size, records in result[
                "all_unique_accessible_hankel_minors"
            ].items()
        },
        "unique_minor_counts": result["unique_minor_counts"],
        "all_23_accessible_minors_positive": True,
        "finite_order_verdict": "all accessible conditions pass strictly",
        "all_order_verdict": (
            "all ordinary and shifted Hankel matrices are positive definite"
        ),
        "protocol_sha256": sha256(PROTOCOL),
        "claim_boundary": (
            "all-order conclusion applies only to the frozen depth-one "
            "identity architecture"
        ),
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
