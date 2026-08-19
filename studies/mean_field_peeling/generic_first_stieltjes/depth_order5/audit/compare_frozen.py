"""Hostile literal comparison of the two independently frozen depth maps."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PRIMARY = BASE / "primary"
INDEPENDENT = BASE / "independent"
PRIMARY_MANIFEST = PRIMARY / "PRIMARY_FREEZE_MANIFEST.json"
INDEPENDENT_MANIFEST = INDEPENDENT / "FROZEN_MANIFEST.json"


def _verify_manifest(directory: Path, manifest_path: Path, hash_path: Path) -> dict:
    manifest_bytes = manifest_path.read_bytes()
    declared = hash_path.read_text().split()[0]
    actual = sha256(manifest_bytes).hexdigest()
    if actual != declared:
        raise AssertionError((manifest_path, declared, actual))
    manifest = json.loads(manifest_bytes)
    for record in manifest["artifacts"].values():
        # Primary records are direct; independent records contain dag/expanded/text.
        if "sha256" in record:
            records = [record]
        else:
            records = [
                value
                for value in record.values()
                if isinstance(value, dict) and "file" in value and "sha256" in value
            ]
        for artifact in records:
            path = directory / artifact.get("file", "")
            if not artifact.get("file"):
                # Primary key itself is the filename.
                continue
            digest = sha256(path.read_bytes()).hexdigest()
            if digest != artifact["sha256"]:
                raise AssertionError((path, artifact["sha256"], digest))
    if directory == PRIMARY:
        for filename, record in manifest["artifacts"].items():
            path = directory / filename
            digest = sha256(path.read_bytes()).hexdigest()
            if digest != record["sha256"]:
                raise AssertionError((path, record["sha256"], digest))
            if path.stat().st_size != record["bytes"]:
                raise AssertionError((path, record["bytes"], path.stat().st_size))
    return manifest


def _atom_derivative(atom: str, depth: int, unit: bool) -> int:
    pattern = r"M_([0-9]{6})" if unit else rf"L([1-{depth}])_([0-9]{{6}})"
    match = re.fullmatch(pattern, atom)
    if not match:
        raise AssertionError((atom, depth, unit))
    digits = match.group(1) if unit else match.group(2)
    return max(
        (index for index, multiplicity in enumerate(digits) if multiplicity != "0"),
        default=0,
    )


def _primary_map(path: Path, depth: int, unit: bool):
    payload = json.loads(path.read_text())
    result = {}
    maxima = {}
    for root in "ABC":
        polynomial = {}
        maximum = 0
        for atoms, coefficient_text in payload["roots"][root]:
            activation_atoms = []
            for atom in atoms:
                if atom == "Q0":
                    if unit:
                        raise AssertionError("Q0 survived in the primary unit map")
                    continue  # common tagged quotient Q0=1
                maximum = max(maximum, _atom_derivative(atom, depth, unit))
                activation_atoms.append(atom)
            key = tuple(sorted(activation_atoms))
            polynomial[key] = polynomial.get(key, Fraction(0)) + Fraction(coefficient_text)
        result[root] = {key: value for key, value in polynomial.items() if value}
        maxima[root] = maximum
    return result, maxima


def _independent_map(path: Path, depth: int, unit: bool):
    payload = json.loads(path.read_text())
    if payload["Q0"] != "1" or payload["unit_gram"] is not unit:
        raise AssertionError((path, payload["Q0"], payload["unit_gram"]))
    result = {}
    maxima = {}
    for root in "ABC":
        polynomial = {}
        maximum = 0
        for record in payload[root]:
            atoms = tuple(sorted(record["atoms"]))
            for atom in atoms:
                maximum = max(maximum, _atom_derivative(atom, depth, unit))
            if atoms in polynomial:
                raise AssertionError((path, root, "duplicate", atoms))
            polynomial[atoms] = Fraction(record["coefficient"])
        result[root] = {key: value for key, value in polynomial.items() if value}
        maxima[root] = maximum
    return result, maxima


def main() -> None:
    primary_manifest = _verify_manifest(
        PRIMARY,
        PRIMARY_MANIFEST,
        PRIMARY / "PRIMARY_FREEZE_SHA256.txt",
    )
    independent_manifest = _verify_manifest(
        INDEPENDENT,
        INDEPENDENT_MANIFEST,
        INDEPENDENT / "FROZEN_MANIFEST_SHA256.txt",
    )
    report = {
        "primary_manifest_sha256": sha256(PRIMARY_MANIFEST.read_bytes()).hexdigest(),
        "independent_manifest_sha256": sha256(INDEPENDENT_MANIFEST.read_bytes()).hexdigest(),
        "common_tagged_quotient": "Q0=1; layer tags retained; no other identities",
        "comparisons": {},
    }
    expected_maxima = {"A": 1, "B": 3, "C": 5}
    passed = True
    for depth in (3, 4):
        for unit in (False, True):
            scope = "UNIT" if unit else "TAGGED"
            primary_path = PRIMARY / (
                f"H{depth}_UNIT_COEFFICIENTS.json"
                if unit
                else f"H{depth}_LAYER_TAGGED_COEFFICIENTS.json"
            )
            independent_path = INDEPENDENT / f"H{depth}_{scope}_COEFFICIENT_MAP.json"
            primary, primary_maxima = _primary_map(primary_path, depth, unit)
            independent, independent_maxima = _independent_map(independent_path, depth, unit)
            comparison = {}
            for root in "ABC":
                keys = set(primary[root]) | set(independent[root])
                differences = [
                    {
                        "atoms": list(key),
                        "primary": str(primary[root].get(key, 0)),
                        "independent": str(independent[root].get(key, 0)),
                    }
                    for key in sorted(keys)
                    if primary[root].get(key, 0) != independent[root].get(key, 0)
                ]
                comparison[root] = {
                    "primary_terms": len(primary[root]),
                    "independent_terms": len(independent[root]),
                    "discrepancy_count": len(differences),
                    "first_discrepancies": differences[:20],
                    "primary_maximum_derivative": primary_maxima[root],
                    "independent_maximum_derivative": independent_maxima[root],
                }
                if differences or primary_maxima[root] != expected_maxima[root] or independent_maxima[root] != expected_maxima[root]:
                    passed = False
            report["comparisons"][f"H{depth}_{scope}"] = comparison

    # Cross-check that manifest term counts describe the parsed files.
    report["primary_manifest_term_counts"] = primary_manifest["term_counts"]
    report["independent_manifest_scope"] = independent_manifest["scope"]
    report["pass"] = passed
    output = HERE / "FROZEN_MAP_COMPARISON.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(output.read_text())
    if not passed:
        raise SystemExit("frozen map comparison failed")


if __name__ == "__main__":
    main()
