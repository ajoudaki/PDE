"""Frozen atomwise comparison with the independently implemented compiler."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from .coefficient_map import expand_coefficient_map, serializable_map
from .factored_expression import compile_factored

from studies.mfp_gaussian_calculus.study_paths import (
    GENERATED_ROOT, input_directory, require_output, guard_output_inputs,
)


HERE = Path(__file__).resolve().parent
OUTPUT = GENERATED_ROOT / "order5/compiler"
INDEPENDENT = input_directory("order5/independent") / "independent_coefficient_map.json"
INDEPENDENT_TAGGED = INDEPENDENT.with_name("independent_layer_tagged_coefficient_map.json")
INDEPENDENT_SYMBOLIC_Q0 = INDEPENDENT.with_name("independent_symbolic_q0_coefficient_map.json")


def comparison_paths(argv=None, *, output_default: Path = OUTPUT):
    parser = argparse.ArgumentParser()
    inputs = parser.add_mutually_exclusive_group()
    inputs.add_argument("--independent-dir", type=Path)
    inputs.add_argument("--historical", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args(argv)
    inputs_root = args.independent_dir or input_directory("order5/independent", historical=args.historical)
    output = require_output(args.output_dir or (output_default / "historical_review" if args.historical else output_default))
    return inputs_root, output


def main() -> None:
    inputs_root, output = comparison_paths()
    independent_path = inputs_root / INDEPENDENT.name
    independent_tagged_path = inputs_root / INDEPENDENT_TAGGED.name
    independent_symbolic_path = inputs_root / INDEPENDENT_SYMBOLIC_Q0.name
    guard_output_inputs(
        (output / name for name in (
            "PRIMARY_UNIT_COEFFICIENT_MAP.json", "PRIMARY_LAYER_TAGGED_COEFFICIENT_MAP.json",
            "PRIMARY_SYMBOLIC_Q0_COEFFICIENT_MAP.json", "INDEPENDENT_COMPARISON.json",
        )),
        (independent_path, independent_tagged_path, independent_symbolic_path),
    )
    for path in (independent_path, independent_tagged_path, independent_symbolic_path):
        if not path.is_file():
            raise FileNotFoundError(path)
    output.mkdir(parents=True, exist_ok=True)
    result = compile_factored(5)
    roots = {
        "A": result.A.specialize_unit_gram(),
        "B": result.B3.specialize_unit_gram(),
        "C": result.C.specialize_unit_gram(),
    }
    primary = {name: serializable_map(expand_coefficient_map(root)) for name, root in roots.items()}
    primary_text = json.dumps(
        {
            "format": "primary-H2-B1-unit-Mpoly-v1",
            "normalization": "M_200000=1",
            "unit_gram": primary,
        },
        separators=(",", ":"),
        sort_keys=True,
    ) + "\n"
    primary_path = output / "PRIMARY_UNIT_COEFFICIENT_MAP.json"
    primary_path.write_text(primary_text)

    tagged = {
        name: serializable_map(expand_coefficient_map(root))
        for name, root in {"A": result.A, "B": result.B3, "C": result.C}.items()
    }
    tagged_text = json.dumps(
        {
            "format": "primary-H2-B1-layer-tagged-Q0=1-v1",
            "unit_input_metric": "Q0=1",
            "layer_tagged": tagged,
        },
        separators=(",", ":"),
        sort_keys=True,
    ) + "\n"
    tagged_path = output / "PRIMARY_LAYER_TAGGED_COEFFICIENT_MAP.json"
    tagged_path.write_text(tagged_text)

    arbitrary = compile_factored(5, arbitrary_q0=True)
    symbolic_q0: dict[str, list[dict[str, object]]] = {}
    symbolic_q0_maps: dict[
        str, dict[tuple[tuple[str, ...], int], Fraction]
    ] = {}
    for name, root in {
        "A": arbitrary.A,
        "B": arbitrary.B3,
        "C": arbitrary.C,
    }.items():
        graded: dict[tuple[tuple[str, ...], int], Fraction] = {}
        for monomial, coefficient in expand_coefficient_map(root).items():
            degree = monomial.count("Q0")
            activation_atoms = tuple(sorted(atom for atom in monomial if atom != "Q0"))
            key = (activation_atoms, degree)
            graded[key] = graded.get(key, Fraction(0)) + coefficient
        graded = {key: value for key, value in graded.items() if value}
        symbolic_q0_maps[name] = graded
        symbolic_q0[name] = [
            {
                "atoms": list(atoms),
                "q0_degree": degree,
                "coefficient": str(coefficient),
            }
            for (atoms, degree), coefficient in sorted(graded.items())
        ]
    symbolic_text = json.dumps(
        {
            "format": "primary-H2-B1-symbolic-Q0-graded-Mpoly-v1",
            "maps": symbolic_q0,
        },
        separators=(",", ":"),
        sort_keys=True,
    ) + "\n"
    symbolic_path = output / "PRIMARY_SYMBOLIC_Q0_COEFFICIENT_MAP.json"
    symbolic_path.write_text(symbolic_text)

    independent_document = json.loads(independent_path.read_text())
    independent_tagged = json.loads(independent_tagged_path.read_text())
    independent_symbolic_q0 = json.loads(independent_symbolic_path.read_text())
    discrepancies: dict[str, list[dict[str, object]]] = {}
    for name in ("A", "B", "C"):
        left = {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in primary[name]
        }
        right = {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in independent_document["unit_gram"][name]
        }
        mismatch = []
        for monomial in sorted(set(left) | set(right)):
            if left.get(monomial, 0) != right.get(monomial, 0):
                mismatch.append(
                    {
                        "atoms": list(monomial),
                        "primary": str(left.get(monomial, 0)),
                        "independent": str(right.get(monomial, 0)),
                    }
                )
        discrepancies[name] = mismatch

    tagged_discrepancies: dict[str, list[dict[str, object]]] = {}
    for name in ("A", "B", "C"):
        left = {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in tagged[name]
        }
        right = {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in independent_tagged[name]
        }
        mismatch = []
        for monomial in sorted(set(left) | set(right)):
            if left.get(monomial, 0) != right.get(monomial, 0):
                mismatch.append(
                    {
                        "atoms": list(monomial),
                        "primary": str(left.get(monomial, 0)),
                        "independent": str(right.get(monomial, 0)),
                    }
                )
        tagged_discrepancies[name] = mismatch

    symbolic_discrepancies: dict[str, list[dict[str, object]]] = {}
    for name in ("A", "B", "C"):
        left = symbolic_q0_maps[name]
        right = {
            (tuple(sorted(item["atoms"])), int(item["q0_degree"])): Fraction(
                item["coefficient"]
            )
            for item in independent_symbolic_q0["maps"][name]
        }
        mismatch = []
        for key in sorted(set(left) | set(right)):
            if left.get(key, 0) != right.get(key, 0):
                atoms, degree = key
                mismatch.append(
                    {
                        "atoms": list(atoms),
                        "q0_degree": degree,
                        "primary": str(left.get(key, 0)),
                        "independent": str(right.get(key, 0)),
                    }
                )
        symbolic_discrepancies[name] = mismatch

    report = {
        "comparison": "exact_rational_atomwise_after_Q0=1_and_M_200000=1",
        "independent_frozen_sha256": hashlib.sha256(independent_path.read_bytes()).hexdigest(),
        "independent_tagged_frozen_sha256": hashlib.sha256(
            independent_tagged_path.read_bytes()
        ).hexdigest(),
        "primary_sha256": hashlib.sha256(primary_path.read_bytes()).hexdigest(),
        "primary_tagged_sha256": hashlib.sha256(tagged_path.read_bytes()).hexdigest(),
        "independent_symbolic_q0_frozen_sha256": hashlib.sha256(
            independent_symbolic_path.read_bytes()
        ).hexdigest(),
        "primary_symbolic_q0_sha256": hashlib.sha256(
            symbolic_path.read_bytes()
        ).hexdigest(),
        "term_counts": {name: len(primary[name]) for name in ("A", "B", "C")},
        "discrepancy_counts": {name: len(discrepancies[name]) for name in ("A", "B", "C")},
        "discrepancies": discrepancies,
        "tagged_term_counts": {
            name: len(tagged[name]) for name in ("A", "B", "C")
        },
        "tagged_discrepancy_counts": {
            name: len(tagged_discrepancies[name]) for name in ("A", "B", "C")
        },
        "tagged_discrepancies": tagged_discrepancies,
        "symbolic_q0_term_counts": {
            name: len(symbolic_q0[name]) for name in ("A", "B", "C")
        },
        "symbolic_q0_discrepancy_counts": {
            name: len(symbolic_discrepancies[name]) for name in ("A", "B", "C")
        },
        "symbolic_q0_discrepancies": symbolic_discrepancies,
        "pass": (
            not any(discrepancies.values())
            and not any(tagged_discrepancies.values())
            and not any(symbolic_discrepancies.values())
        ),
    }
    (output / "INDEPENDENT_COMPARISON.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n"
    )
    if not report["pass"]:
        raise SystemExit("independent atomwise comparison failed")


if __name__ == "__main__":
    main()
