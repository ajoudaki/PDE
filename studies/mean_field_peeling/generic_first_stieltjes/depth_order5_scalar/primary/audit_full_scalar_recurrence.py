"""Exact post-freeze audit of the full deterministic order-five recurrence.

The candidate depth assembler is independent of the frozen H=2,3,4 map
producers.  This audit fully distributes its A, B, C roots with rational
arithmetic, uses the independently frozen reference loader/canonicalizer,
and records exact controls and terminal-alphabet checks.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from ..audit.exact_controls import activation_atom, evaluate
from ..audit.reference_maps import EXPECTED_COUNTS, REFERENCE, difference, load_reference
from ...order5.compiler.coefficient_map import expand_coefficient_map
from ...order5.compiler.factored_expression import walk
from .audit_frozen_sector import projection_audit
from .moving_scalar_extension import assemble_moving_recurrence
from .scalar_frozen_recurrence import derivative_ceiling


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CANDIDATE_FREEZE = HERE / "FULL_SCALAR_CANDIDATE_FREEZE.json"
EXPECTED_FREEZE_HASH = "d731ec66b067b8739df305426c6aa6d06bbc309d5fd624bd16d1c283ca649728"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidate_maps(depth: int):
    result = assemble_moving_recurrence(depth)
    roots = {"A": result.frozen.A, "B": result.frozen.B, "C": result.C}
    maps = {name: expand_coefficient_map(value) for name, value in roots.items()}
    return result, roots, maps


def terminal_alphabet(roots) -> dict[str, object]:
    symbols: set[str] = set()
    bad_atom_arities: set[int] = set()
    atom_count = 0
    for root in roots.values():
        for node in walk(root):
            if node.node[0] == "symbol":
                symbols.add(node.node[1])
            elif node.node[0] == "atom":
                atom_count += 1
                if node.node[1] != "M" or len(node.node[2]) != 6:
                    bad_atom_arities.add(len(node.node[2]))
    return {
        "residual_symbols": sorted(symbols),
        "bad_atom_arities": sorted(bad_atom_arities),
        "distinct_DAG_atom_nodes": atom_count,
        "derivative_ceiling": derivative_ceiling(roots),
    }


def exact_controls(maps) -> dict[str, dict[str, str]]:
    activations = {
        "constant_1": (1,),
        "unit_affine_3_4": (Fraction(3, 5), Fraction(4, 5)),
        "linear": (0, 1),
        # Algebraic quotient only: x^2 does not preserve the unit Gram.
        "formal_unit_quotient_x2": (0, 0, 1),
    }
    result = {
        label: {name: str(evaluate(poly, activation)) for name, poly in maps.items()}
        for label, activation in activations.items()
    }
    result["normalized_affine_(1+x)/sqrt2"] = {
        name: scaled_activation_value(poly, (1, 1), 2) for name, poly in maps.items()
    }
    result["normalized_quadratic_x2/sqrt3"] = {
        name: scaled_activation_value(poly, (0, 0, 1), 3) for name, poly in maps.items()
    }
    return result


def scaled_activation_value(poly, base, denominator: int) -> str:
    """Exactly evaluate phi=p/sqrt(denominator) in Q[sqrt(denominator)]."""

    atom_cache: dict[str, Fraction] = {}
    rational = Fraction(0)
    radical = Fraction(0)
    for atoms, coefficient in poly.items():
        value = coefficient
        scale_degree = 0
        for name in atoms:
            if name not in atom_cache:
                atom_cache[name] = activation_atom(name, tuple(Fraction(x) for x in base))
            value *= atom_cache[name]
            scale_degree += sum(int(x) for x in name.split("_")[1])
        if scale_degree % 2 == 0:
            rational += value / denominator ** (scale_degree // 2)
        else:
            radical += value / denominator ** ((scale_degree + 1) // 2)
    if radical:
        return f"{rational}+({radical})*sqrt({denominator})"
    return str(rational)


def companion_controls() -> dict[str, object]:
    h2_path = ROOT / "order5/compiler/MANIFEST.json"
    deep_path = ROOT / "depth_order5/independent/CONTROL_AUDIT.json"
    h2 = json.loads(h2_path.read_text())
    deep = json.loads(deep_path.read_text())
    expected = {
        "2": {"A": "111", "B": "1685184", "C": "77400633120"},
        "3": {"A": "14175", "B": "139445032896", "C": "4298284752832899360"},
        "4": {
            "A": "138351807",
            "B": "59385566223611232192",
            "C": "81427352525619060193821492876576",
        },
    }
    actual = {
        "2": h2["controls"]["quadratic"],
        "3": deep["depths"]["3"]["quadratic"],
        "4": deep["depths"]["4"]["quadratic"],
    }
    if actual != expected:
        raise AssertionError((actual, expected))
    return {
        "scope": "companion layer-tagged/arbitrary-Gram maps; not a substitution into the unit-Gram recurrence",
        "values": actual,
        "files": {
            str(h2_path.relative_to(ROOT)): sha256(h2_path),
            str(deep_path.relative_to(ROOT)): sha256(deep_path),
        },
    }


def nonpolynomial_regression() -> dict[str, object]:
    path = ROOT / "depth_order5/audit/NORMALIZED_SINE_EXPERIMENT.json"
    data = json.loads(path.read_text())
    if data["decision"] != "pass" or data["total_networks"] != 7700:
        raise AssertionError((data["decision"], data["total_networks"]))
    return {
        "scope": "pre-registered normalized-sine finite-width regression inherited after exact map equality",
        "sha256": sha256(path),
        "decision": data["decision"],
        "total_networks": data["total_networks"],
        "fits": {
            depth: {
                key: fit[key]
                for key in (
                    "population_prediction",
                    "intercept",
                    "intercept_standard_error",
                    "z",
                    "chi_square_p_value",
                    "valid",
                )
            }
            for depth, fit in data["fits"].items()
        },
    }


def run_audit() -> dict[str, object]:
    if sha256(CANDIDATE_FREEZE) != EXPECTED_FREEZE_HASH:
        raise RuntimeError("candidate freeze hash drift")
    projection = projection_audit()
    if any(projection.values()):
        raise AssertionError(projection)

    result: dict[str, object] = {
        "schema": "full-scalar-order5-exact-audit-v1",
        "candidate_freeze_sha256": EXPECTED_FREEZE_HASH,
        "lower_order_projection_transition_discrepancies": projection,
        "depths": {},
        "quadratic_controls": companion_controls(),
        "nonpolynomial_regression": nonpolynomial_regression(),
    }
    expected_linear = {
        2: {"A": "3", "B": "48", "C": "1464"},
        3: {"A": "4", "B": "160", "C": "13888"},
        4: {"A": "5", "B": "400", "C": "73240"},
    }
    for depth in (2, 3, 4):
        recurrence, roots, maps = candidate_maps(depth)
        reference = load_reference(depth)
        comparisons = {
            name: difference(maps[name], reference[name]) for name in ("A", "B", "C")
        }
        alphabet = terminal_alphabet(roots)
        controls = exact_controls(maps)
        reference_path, reference_hash = REFERENCE[depth]
        depth_result = {
            "reference": {
                "path": str(reference_path.relative_to(ROOT)),
                "sha256": reference_hash,
            },
            "expected_monomial_counts": EXPECTED_COUNTS[depth],
            "comparisons": comparisons,
            "terminal_alphabet": alphabet,
            "controls": controls,
            "sector_monomial_counts": {
                "S5": len(expand_coefficient_map(recurrence.frozen.straight5)),
                "AC": len(expand_coefficient_map(recurrence.frozen.gram31)),
                "Bm2": len(expand_coefficient_map(recurrence.B_m2)),
                "m2norm": len(expand_coefficient_map(recurrence.m2_norm)),
                "Am3": len(expand_coefficient_map(recurrence.A_m3)),
            },
        }
        result["depths"][str(depth)] = depth_result
        if any(value["discrepancy_count"] for value in comparisons.values()):
            raise AssertionError((depth, comparisons))
        if alphabet["residual_symbols"] or alphabet["bad_atom_arities"]:
            raise AssertionError((depth, alphabet))
        if alphabet["derivative_ceiling"] > 5:
            raise AssertionError((depth, alphabet["derivative_ceiling"]))
        if controls["constant_1"] != {"A": "1", "B": "0", "C": "0"}:
            raise AssertionError((depth, controls["constant_1"]))
        if controls["linear"] != expected_linear[depth]:
            raise AssertionError((depth, controls["linear"]))

    result["decision"] = "PASS: zero exact coefficient discrepancies at H=2,3,4"
    return result


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
