"""Literal exact-rational comparison of already-frozen depth maps.

This file was added after ``PRIMARY_FREEZE_MANIFEST.json`` was sealed.  It
does not import either compiler and never rewrites producer artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
INDEPENDENT = HERE.parent / "independent"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_primary(entries, *, drop_q0: bool):
    answer = {}
    for atoms, coefficient in entries:
        key = tuple(atom for atom in atoms if not (drop_q0 and atom == "Q0"))
        answer[key] = answer.get(key, Fraction(0)) + Fraction(coefficient)
    return {key: value for key, value in answer.items() if value}


def normalize_independent(entries):
    answer = {}
    for entry in entries:
        key = tuple(entry["atoms"])
        answer[key] = answer.get(key, Fraction(0)) + Fraction(entry["coefficient"])
    return {key: value for key, value in answer.items() if value}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, choices=(3, 4), required=True)
    parser.add_argument("--quotient", choices=("tagged", "unit"), required=True)
    args = parser.parse_args()
    depth, quotient = args.depth, args.quotient

    primary_manifest_path = HERE / "PRIMARY_FREEZE_MANIFEST.json"
    independent_manifest_path = INDEPENDENT / "FROZEN_MANIFEST.json"
    primary_manifest = json.loads(primary_manifest_path.read_text())
    independent_manifest = json.loads(independent_manifest_path.read_text())

    if quotient == "tagged":
        primary_name = f"H{depth}_LAYER_TAGGED_COEFFICIENTS.json"
        independent_name = f"H{depth}_TAGGED_COEFFICIENT_MAP.json"
        independent_key = f"H{depth}_TAGGED"
    else:
        primary_name = f"H{depth}_UNIT_COEFFICIENTS.json"
        independent_name = f"H{depth}_UNIT_COEFFICIENT_MAP.json"
        independent_key = f"H{depth}_UNIT"
    primary_path = HERE / primary_name
    independent_path = INDEPENDENT / independent_name

    expected_primary_hash = primary_manifest["artifacts"][primary_name]["sha256"]
    expected_independent_hash = independent_manifest["artifacts"][independent_key]["expanded"]["sha256"]
    actual_primary_hash = sha256(primary_path)
    actual_independent_hash = sha256(independent_path)
    if actual_primary_hash != expected_primary_hash:
        raise AssertionError("primary artifact changed after freeze")
    if actual_independent_hash != expected_independent_hash:
        raise AssertionError("independent artifact changed after freeze")

    primary_raw = json.loads(primary_path.read_text())
    independent_raw = json.loads(independent_path.read_text())
    discrepancies = {}
    counts = {}
    for root in ("A", "B", "C"):
        left = normalize_primary(
            primary_raw["roots"][root], drop_q0=(quotient == "tagged")
        )
        right = normalize_independent(independent_raw[root])
        keys = set(left) | set(right)
        difference = [
            (key, left.get(key, Fraction(0)), right.get(key, Fraction(0)))
            for key in keys
            if left.get(key, Fraction(0)) != right.get(key, Fraction(0))
        ]
        counts[root] = {
            "primary_terms_after_Q0_1": len(left),
            "independent_terms": len(right),
            "discrepancies": len(difference),
        }
        discrepancies[root] = [
            {
                "atoms": list(key),
                "primary": str(left_value),
                "independent": str(right_value),
            }
            for key, left_value, right_value in sorted(difference)[:20]
        ]

    report = {
        "schema": "route-s-frozen-cross-comparison-v1",
        "depth": depth,
        "quotient": quotient,
        "comparison_scope": (
            "layer tags retained and primary Q0 specialized exactly to 1"
            if quotient == "tagged"
            else "unit Gram with M_200000=1 in both maps"
        ),
        "primary_freeze_manifest_sha256": sha256(primary_manifest_path),
        "independent_freeze_manifest_sha256": sha256(independent_manifest_path),
        "primary_artifact": {"file": primary_name, "sha256": actual_primary_hash},
        "independent_artifact": {
            "file": independent_name,
            "sha256": actual_independent_hash,
        },
        "counts": counts,
        "first_discrepancies": discrepancies,
        "pass": all(record["discrepancies"] == 0 for record in counts.values()),
    }
    output = HERE / f"H{depth}_{quotient.upper()}_FROZEN_COMPARISON.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(output)
    print(json.dumps(counts, indent=2, sort_keys=True))
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

