"""Emit the complete local degree/equality-partition ledger for Gamma_04."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from . import gamma04_contraction as g4


def pairing_count(even_degree: int) -> int:
    if even_degree & 1:
        return 0
    value = 1
    for odd in range(1, even_degree, 2):
        value *= odd
    return value


def involution_count(degree: int) -> int:
    # A forward leg is either paired with another forward leg or contracted
    # against F0 by Stein.  Hence leading patterns are partial matchings.
    values = [1, 1]
    for size in range(2, degree + 1):
        values.append(values[-1] + (size - 1) * values[-2])
    return values[degree]


def report() -> dict[str, object]:
    q = g4.local_polynomials()
    raw = {
        "gamma04_next": g4.rm(q["x0"], q["h4"]),
        "a41_next": g4.r_derivative(q["h4"], "e", 1),
        "a43_next": g4.r_derivative(q["h4"], "e", 4),
    }
    targets = {}
    for name, polynomial in raw.items():
        degree = Counter(
            (sum(monomial.forward), sum(monomial.reverse))
            for monomial in polynomial
        )
        targets[name] = {
            "pre_wick_local_monomials": len(polynomial),
            "degree_classes": [
                {
                    "forward_degree": forward,
                    "reverse_degree": reverse,
                    "local_monomials": count,
                    "leading_forward_partial_matchings": involution_count(forward),
                    "leading_reverse_pairings": pairing_count(reverse),
                    "vanishes_if_reverse_degree_odd": bool(reverse & 1),
                }
                for (forward, reverse), count in sorted(degree.items())
            ],
            "contracted_M_only_terms": len(g4.transitions()[name]),
        }
    return {
        "scope": "one local post-R3 Gamma_04 transition",
        "targets": targets,
        "maximum_forward_innovation_degree": 4,
        "maximum_reverse_innovation_degree": 4,
        "leading_partition_rule": (
            "reverse legs are perfectly paired; forward legs are partially "
            "paired and every singleton is contracted to F0 by Stein"
        ),
        "negative_width_rule": (
            "after forced transpose identifications are extracted, merging c "
            "distinct leading covariance/Stein index blocks loses c free sums "
            "and contributes O(n^(-c)); all c>=1 sectors vanish at fixed H "
            "under the stated uniform moment bound"
        ),
        "transpose_response_branches": {
            "Delta0": {
                "coefficient": "4*Gamma03+6*Gamma12+4*Gamma21+Gamma30",
                "status": "zero by odd-total readout parity",
            },
            "Delta1": {
                "coefficient": "6*Gamma02+8*Gamma11+3*Gamma20",
                "reduced": "9*Gamma02+8*Gamma11",
                "inherited": "a41",
            },
            "Delta2": {
                "coefficient": "4*Gamma01+3*Gamma10",
                "status": "zero by odd-total readout parity",
            },
            "Delta3": {
                "coefficient": "Gamma00=1",
                "inherited": "a43",
            },
        },
    }


if __name__ == "__main__":
    result = report()
    path = Path(__file__).resolve().parent / "EQUALITY_PARTITION_LEDGER.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
