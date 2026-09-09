"""Independent canonical loader for the three frozen unit-Gram references.

This module was written before the candidate scalar recurrence was inspected.
It intentionally knows only the public coefficient-map schemas, not any
producer transition implementation.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping


ROOT = Path(__file__).resolve().parents[2]

REFERENCE = {
    2: (
        ROOT / "order5/compiler/PRIMARY_UNIT_COEFFICIENT_MAP.json",
        "68dd13460fb5bfab187d0d7e61b90adeec43a2311c2cab2726fd68b73fbf37f2",
    ),
    3: (
        ROOT / "depth_order5/primary/H3_UNIT_COEFFICIENTS.json",
        "564c6a27d6071e8601d21fd167dfd8f21d7ac9fe2323695a626eeebf73b980c6",
    ),
    4: (
        ROOT / "depth_order5/primary/H4_UNIT_COEFFICIENTS.json",
        "b3b220b76c8d30037cf0bfc0a8a1dc05884b28601a1c28e45b0daf9ff64faa5d",
    ),
}

EXPECTED_COUNTS = {
    2: {"A": 3, "B": 46, "C": 974},
    3: {"A": 4, "B": 160, "C": 6519},
    4: {"A": 5, "B": 350, "C": 17641},
}

Monomial = tuple[str, ...]
Polynomial = dict[Monomial, Fraction]


def _fraction(text: str | int) -> Fraction:
    return Fraction(text)


def canonical_polynomial(entries: Iterable[object]) -> Polynomial:
    """Canonicalize either historical frozen-map entry schema."""

    answer: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for entry in entries:
        if isinstance(entry, dict):
            atoms = entry["atoms"]
            coefficient = entry["coefficient"]
        else:
            atoms, coefficient = entry
        key = tuple(sorted(str(atom) for atom in atoms))
        answer[key] += _fraction(coefficient)
    return {key: value for key, value in sorted(answer.items()) if value}


def load_reference(depth: int) -> dict[str, Polynomial]:
    path, expected_hash = REFERENCE[depth]
    payload = path.read_bytes()
    actual_hash = hashlib.sha256(payload).hexdigest()
    if actual_hash != expected_hash:
        raise RuntimeError(
            f"reference hash drift at H={depth}: {actual_hash} != {expected_hash}"
        )
    raw = json.loads(payload)
    roots = raw.get("unit_gram", raw.get("roots"))
    if roots is None:
        raise ValueError(f"unrecognized reference schema at {path}")
    result = {name: canonical_polynomial(entries) for name, entries in roots.items()}
    counts = {name: len(poly) for name, poly in result.items()}
    if counts != EXPECTED_COUNTS[depth]:
        raise RuntimeError(f"reference count drift at H={depth}: {counts}")
    return result


def difference(
    candidate: Mapping[Monomial, Fraction],
    reference: Mapping[Monomial, Fraction],
) -> dict[str, object]:
    candidate_keys = set(candidate)
    reference_keys = set(reference)
    unequal = {
        key: (candidate[key], reference[key])
        for key in sorted(candidate_keys & reference_keys)
        if candidate[key] != reference[key]
    }
    return {
        "candidate_count": len(candidate),
        "reference_count": len(reference),
        "missing_count": len(reference_keys - candidate_keys),
        "extra_count": len(candidate_keys - reference_keys),
        "unequal_count": len(unequal),
        "discrepancy_count": (
            len(reference_keys - candidate_keys)
            + len(candidate_keys - reference_keys)
            + len(unequal)
        ),
        "missing_sample": [list(key) for key in sorted(reference_keys - candidate_keys)[:10]],
        "extra_sample": [list(key) for key in sorted(candidate_keys - reference_keys)[:10]],
        "unequal_sample": [
            {
                "atoms": list(key),
                "candidate": str(values[0]),
                "reference": str(values[1]),
            }
            for key, values in list(unequal.items())[:10]
        ],
    }


if __name__ == "__main__":
    for h in sorted(REFERENCE):
        maps = load_reference(h)
        print(h, {name: len(poly) for name, poly in maps.items()})
