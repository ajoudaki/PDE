"""Post-freeze literal comparison against the primary order-five compiler."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from ..compiler.coefficient_map import expand_coefficient_map
from ..compiler.factored_expression import compile_factored


HERE = Path(__file__).resolve().parent


def _read_map(path: Path, section: str | None = None) -> dict[str, dict[tuple[str, ...], Fraction]]:
    document = json.loads(path.read_text())
    if section is not None:
        document = document[section]
    answer = {}
    for name in "ABC":
        answer[name] = {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in document[name]
        }
    return answer


def _diff(left, right):
    report = {}
    for name in "ABC":
        mismatches = []
        for monomial in sorted(set(left[name]) | set(right[name])):
            if left[name].get(monomial, 0) != right[name].get(monomial, 0):
                mismatches.append(
                    {
                        "atoms": list(monomial),
                        "primary": str(left[name].get(monomial, 0)),
                        "independent": str(right[name].get(monomial, 0)),
                    }
                )
        report[name] = {
            "primary_terms": len(left[name]),
            "independent_terms": len(right[name]),
            "discrepancy_count": len(mismatches),
            "discrepancies": mismatches,
        }
    return report


def main() -> None:
    unit_path = HERE / "independent_coefficient_map.json"
    tagged_path = HERE / "independent_layer_tagged_coefficient_map.json"
    unit = _read_map(unit_path, "unit_gram")
    tagged = _read_map(tagged_path)

    compiled = compile_factored(5)
    roots = {"A": compiled.A, "B": compiled.B3, "C": compiled.C}
    primary_tagged = {
        name: {tuple(sorted(monomial)): coefficient for monomial, coefficient in expand_coefficient_map(root).items()}
        for name, root in roots.items()
    }
    primary_unit = {
        name: {
            tuple(sorted(monomial)): coefficient
            for monomial, coefficient in expand_coefficient_map(root.specialize_unit_gram()).items()
        }
        for name, root in roots.items()
    }
    unit_diff = _diff(primary_unit, unit)
    tagged_diff = _diff(primary_tagged, tagged)
    report = {
        "comparison_time": "post-freeze",
        "normalizations": {
            "unit": "Q0=Q1=Q2=1 and M_200000=1",
            "tagged": "Q0=1; X at N(0,Q0), Y at N(0,Q1), Q1=X_200000",
        },
        "independent_hashes": {
            "unit_exact_file": hashlib.sha256(unit_path.read_bytes()).hexdigest(),
            "tagged_exact_file": hashlib.sha256(tagged_path.read_bytes()).hexdigest(),
        },
        "unit": unit_diff,
        "tagged": tagged_diff,
    }
    report["pass"] = not any(
        report[scope][name]["discrepancy_count"]
        for scope in ("unit", "tagged")
        for name in "ABC"
    )
    path = HERE / "PRIMARY_COMPARISON.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(path.read_text())
    if not report["pass"]:
        raise SystemExit("post-freeze coefficient comparison failed")


if __name__ == "__main__":
    main()
