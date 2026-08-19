"""Regenerate the complete order-five normal-form artifacts and manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .factored_expression import (
    compile_factored,
    emit_cse,
    evaluate_polynomial_activation,
    walk,
)


HERE = Path(__file__).resolve().parent


def _header(alphabet: str) -> str:
    return f"""# GENERATED FILE -- do not edit by hand.
# Generator: compiler/generate_artifacts.py
# Grammar: dependency-first deterministic arithmetic DAG.
# Each t_N is defined before use.  There are no random/tangent/response nodes.
# Moment alphabet: {alphabet}
# Exponent order is (phi,phi',phi'',phi''',phi^(4),phi^(5)).
"""


def main() -> None:
    result = compile_factored(5)
    arbitrary = compile_factored(5, arbitrary_q0=True)
    separated_roots = {"A": arbitrary.A, "B": arbitrary.B3, "C": arbitrary.C}
    control_roots = {"A": result.A, "B": result.B3, "C": result.C}
    unit_roots = {name: value.specialize_unit_gram() for name, value in control_roots.items()}

    separated = _header(
        "X_nu=E_{N(0,Q0)}[...] and Y_nu=E_{N(0,Q1)}[...]"
    ) + emit_cse(separated_roots) + "\n"
    unit = _header(
        "M_nu=E_{G~N(0,1)}[product_r phi^(r)(G)^nu_r], with M_200000=1"
    ) + emit_cse(unit_roots) + "\n"

    paths = {
        "layer_separated": HERE / "LAYER_SEPARATED_ABC_NORMAL_FORM.txt",
        "unit_gram": HERE / "UNIT_GRAM_ABC_NORMAL_FORM.txt",
    }
    paths["layer_separated"].write_text(separated)
    paths["unit_gram"].write_text(unit)

    controls = {}
    for name, coefficients in {
        "constant_2": [2],
        "linear": [0, 1],
        "affine_1_plus_x": [1, 1],
        "quadratic": [0, 0, 1],
    }.items():
        controls[name] = {
            "A": str(evaluate_polynomial_activation(result.A, coefficients)),
            "B": str(evaluate_polynomial_activation(result.B3, coefficients)),
            "C": str(evaluate_polynomial_activation(result.C, coefficients)),
        }

    manifest = {
        "formula_status": "algebraically_audited_zero_independent_atomwise_discrepancies",
        "derivative_order": 5,
        "maximum_activation_derivative": result.C.maximum_derivative(),
        "factored_node_counts": {
            "A": len(walk(result.A)),
            "B": len(walk(result.B3)),
            "C": len(walk(result.C)),
            "unit_A": len(walk(unit_roots["A"])),
            "unit_B": len(walk(unit_roots["B"])),
            "unit_C": len(walk(unit_roots["C"])),
        },
        "controls": controls,
        "sha256": {
            name: hashlib.sha256(path.read_bytes()).hexdigest()
            for name, path in paths.items()
        },
    }
    (HERE / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
