#!/usr/bin/env python3
"""Exact six-moment Stieltjes audit for the accepted depth-3 order-13 jet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from depth3_stieltjes_audit import (
    audit_hankels,
    fraction_string,
    load_existing_moment_transform,
    moments_from_triangular_identity,
)


HERE = Path(__file__).resolve().parent
INPUT = HERE / "results_order13.json"
PROTOCOL = HERE / "ORDER13_STIELTJES_PROTOCOL.md"
DERIVATIVE_ENGINE = HERE / "depth3_exact_jet.py"
MOMENT_AUDIT_PRIMITIVES = HERE / "depth3_stieltjes_audit.py"
REPO = HERE.parents[3]
EXACT_SERIES = (
    REPO
    / "studies/stieltjes_conjecture/numerics/global_proxy_campaign/proxy/exact_series.py"
)

EXPECTED_SHA256 = {
    "input": "2813c24ce18b31254d762fc4cd7b46c89c01d696022bc31ba58da0e85c84b257",
    "protocol": "52562a4ffb2e61c5d153a9a1d50a0197a4a2490660839cf69f88836f3f046956",
    "derivative_engine": "f7f40919f6a286ad82facfc6451ab9809ed8ed7999110f0aadd58bafb96e2a5c",
    "moment_audit_primitives": "4c8207612cb3a807bb60884d179424fa02a6eb4fbea73ddea90881557cc74a46",
    "exact_series_route": "d003563deb87c6baea7f423f954979f3082b306035eeba35cc223dda25d0ed60",
}

EXPECTED_PREFIX = (
    "95641312/275625",
    "3963629647049188/3230587705078125",
    "12164741271894434633792/601040746943206787109375",
    "4206861574840394358968837051264/9862678589590839304447174072265625",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    actual_hashes = {
        "input": sha256(INPUT),
        "protocol": sha256(PROTOCOL),
        "derivative_engine": sha256(DERIVATIVE_ENGINE),
        "moment_audit_primitives": sha256(MOMENT_AUDIT_PRIMITIVES),
        "exact_series_route": sha256(EXACT_SERIES),
    }
    if actual_hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={actual_hashes}, expected={EXPECTED_SHA256}"
        )

    document = json.loads(INPUT.read_text())
    derivatives = {int(key): int(value) for key, value in document["derivatives"].items()}
    if sorted(derivatives) != list(range(14)):
        raise AssertionError("the input jet is not contiguous through order thirteen")
    if any(derivatives[order] for order in range(0, 14, 2)):
        raise AssertionError("input parity gate failed")
    odd_derivatives = {
        order: derivatives[order] for order in range(1, 14, 2)
    }

    baseline_a, moments_a = load_existing_moment_transform()(odd_derivatives)
    baseline_b, moments_b = moments_from_triangular_identity(odd_derivatives)
    if baseline_a != baseline_b or moments_a != moments_b:
        raise AssertionError("the two exact moment transformations disagree")
    if len(moments_a) != 6:
        raise AssertionError("order thirteen must determine exactly six moments")
    if tuple(map(fraction_string, moments_a[:4])) != EXPECTED_PREFIX:
        raise AssertionError("the accepted order-nine moment prefix changed")

    hankels = audit_hankels(moments_a)
    if hankels["accessible_matrix_count"] != 6:
        raise AssertionError("six ordinary/shifted Hankel matrices must be accessible")
    new_matrices = (
        hankels["ordinary"]["H_2"],
        hankels["shifted"]["H_2_plus"],
    )
    for matrix in new_matrices:
        if len(matrix["principal_minors"]) != 7:
            raise AssertionError("a 3x3 audit must contain all seven principal minors")

    all_principal_minors_positive = all(
        record["positive_semidefinite"]
        and all(not value.startswith("-") and value != "0"
                for value in record["principal_minors"].values())
        for family in (hankels["ordinary"], hankels["shifted"])
        for record in family.values()
    )

    payload = {
        "model": document["model"],
        "max_feature_derivative_order": 13,
        "kernel_convention": (
            "K(y)=F'(F^{-1}(y))=F'(0)+sum_r (-1)^r mu_r y^(2r+2)"
        ),
        "kernel_baseline": fraction_string(baseline_a),
        "moments": {
            f"mu_{index}": {
                "exact": fraction_string(value),
                "decimal": float(value),
                "sign": "positive" if value > 0 else "zero" if value == 0 else "negative",
            }
            for index, value in enumerate(moments_a)
        },
        "hankel_audit": hankels,
        "all_accessible_principal_minors_strictly_positive": (
            all_principal_minors_positive
        ),
        "moment_routes_agree": True,
        "validation": "passed",
        "verdict": (
            "all_six_moment_hankel_conditions_strictly_pass"
            if all_principal_minors_positive
            and hankels["all_accessible_matrices_positive_definite"]
            else "at_least_one_six_moment_hankel_condition_fails"
        ),
        "next_unavailable_conditions": {
            "mu_6_and_H_3": "require F^(15)(0)",
            "mu_7_and_H_3_plus": "require F^(17)(0)",
        },
        "sha256": actual_hashes,
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
