from fractions import Fraction

from .factored_expression import (
    compile_factored,
    evaluate_polynomial_activation,
    walk,
)
from .artifact_evaluator import evaluate_artifact_polynomial
from .coefficient_map import expand_coefficient_map
from .smooth_control import normalized_sine_values
from .build_self_contained_report import (
    SEPARATED_BEGIN,
    SEPARATED_END,
    UNIT_BEGIN,
    UNIT_END,
    embedded_payload,
)
from pathlib import Path
import json


def test_exact_controls_and_parity() -> None:
    result = compile_factored(5)
    assert not result.derivatives[0]
    assert not result.derivatives[2]
    assert not result.derivatives[4]

    assert [evaluate_polynomial_activation(result.derivatives[k], [2]) for k in (1, 3, 5)] == [4, 0, 0]
    assert [evaluate_polynomial_activation(result.derivatives[k], [0, 1]) for k in (1, 3, 5)] == [3, 48, 1464]
    assert [evaluate_polynomial_activation(result.derivatives[k], [1, 1]) for k in (1, 3, 5)] == [6, 112, 4400]
    assert [evaluate_polynomial_activation(result.derivatives[k], [0, 0, 1]) for k in (1, 3, 5)] == [111, 1_685_184, 77_400_633_120]


def test_quadratic_stieltjes_coefficients() -> None:
    result = compile_factored(5)
    A = evaluate_polynomial_activation(result.A, [0, 0, 1])
    B = evaluate_polynomial_activation(result.B3, [0, 0, 1])
    C = evaluate_polynomial_activation(result.C, [0, 0, 1])
    mu0 = B / (2 * A**2)
    mu1 = (4 * B**2 - A * C) / (24 * A**5)
    assert mu0 == Fraction(280864, 4107)
    assert mu1 == Fraction(38443196932, 5616860517)


def test_terminal_grammar_has_no_auxiliary_gaussians_and_stops_at_five() -> None:
    result = compile_factored(5)
    unit = result.C.specialize_unit_gram()
    assert unit.maximum_derivative() == 5
    assert len(walk(unit)) < 2000
    for node in walk(unit):
        if node.node[0] == "atom":
            assert node.node[1] == "M"
            assert len(node.node[2]) == 8
            assert not any(node.node[2][6:])


def test_serialized_layer_separated_formula_replays_quadratic_control() -> None:
    path = Path(__file__).with_name("LAYER_SEPARATED_ABC_NORMAL_FORM.txt")
    assert evaluate_artifact_polynomial(path, [0, 0, 1]) == {
        "A": Fraction(111),
        "B": Fraction(1_685_184),
        "C": Fraction(77_400_633_120),
    }
    assert evaluate_artifact_polynomial(path, [0, 1], q0=3) == {
        "A": Fraction(9),
        "B": Fraction(432),
        "C": Fraction(39_528),
    }


def test_serialized_unit_formula_is_in_the_exact_unit_gram_quotient() -> None:
    path = Path(__file__).with_name("UNIT_GRAM_ABC_NORMAL_FORM.txt")
    text = path.read_text()
    assert "M_{200000}" not in text
    assert "X_{" not in text and "Y_{" not in text and "Q0" not in text
    # The linear activation lies in the unit-Gram quotient.
    assert evaluate_artifact_polynomial(path, [0, 1]) == {
        "A": Fraction(3),
        "B": Fraction(48),
        "C": Fraction(1464),
    }


def test_frozen_independent_map_agrees_atom_by_atom() -> None:
    result = compile_factored(5)
    independent_path = Path(__file__).parents[1] / "independent" / "independent_coefficient_map.json"
    document = json.loads(independent_path.read_text())
    for name, root in {
        "A": result.A,
        "B": result.B3,
        "C": result.C,
    }.items():
        primary = expand_coefficient_map(root.specialize_unit_gram())
        independent = {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in document["unit_gram"][name]
        }
        assert primary == independent

    tagged_document = json.loads(
        (independent_path.with_name("independent_layer_tagged_coefficient_map.json")).read_text()
    )
    for name, root in {
        "A": result.A,
        "B": result.B3,
        "C": result.C,
    }.items():
        assert expand_coefficient_map(root) == {
            tuple(sorted(item["atoms"])): Fraction(item["coefficient"])
            for item in tagged_document[name]
        }


def test_normalized_sine_is_pade_but_not_positive_stieltjes() -> None:
    values = normalized_sine_values(48)
    assert abs(values["A"] - 4.03709694646564) < 1.0e-12
    assert abs(values["B"] + 103.257331146774) < 1.0e-10
    assert abs(values["C"] - 29944.4323429373) < 1.0e-7
    assert values["mu0"] < 0 and values["mu1"] < 0


def test_self_contained_report_embeds_frozen_artifacts_byte_for_byte() -> None:
    order5 = Path(__file__).parents[1]
    report = (order5 / "H2_B1_ORDER5_SELF_CONTAINED.md").read_text()
    unit = Path(__file__).with_name("UNIT_GRAM_ABC_NORMAL_FORM.txt").read_text()
    separated = Path(__file__).with_name(
        "LAYER_SEPARATED_ABC_NORMAL_FORM.txt"
    ).read_text()
    assert embedded_payload(report, UNIT_BEGIN, UNIT_END) == unit
    assert embedded_payload(report, SEPARATED_BEGIN, SEPARATED_END) == separated


def test_all_frozen_coefficient_comparisons_report_zero_discrepancies() -> None:
    order5 = Path(__file__).parents[1]
    combined = json.loads(Path(__file__).with_name("INDEPENDENT_COMPARISON.json").read_text())
    symbolic = json.loads(
        (order5 / "independent" / "SYMBOLIC_Q0_PRIMARY_COMPARISON.json").read_text()
    )
    assert combined["pass"] and symbolic["pass"]
    for family in ("discrepancy_counts", "tagged_discrepancy_counts", "symbolic_q0_discrepancy_counts"):
        assert combined[family] == {"A": 0, "B": 0, "C": 0}
