"""Exact local audits for the Route S population compiler."""

from __future__ import annotations

from studies.mean_field_peeling.generic_first_stieltjes.order5.compiler.coefficient_map import (
    expand_coefficient_map,
)
from studies.mean_field_peeling.generic_first_stieltjes.order5.compiler.factored_expression import (
    compile_factored,
)

from .depth_population_jet import (
    compile_depth,
    evaluate_polynomial_activation,
    specialize_unit_gram,
    terminal_maximum_derivative,
)


def _rename_h2_layers(mapping):
    answer = {}
    for monomial, coefficient in mapping.items():
        renamed = []
        for token in monomial:
            if token.startswith("L1_"):
                token = "X_" + token[3:]
            elif token.startswith("L2_"):
                token = "Y_" + token[3:]
            renamed.append(token)
        key = tuple(sorted(renamed))
        answer[key] = answer.get(key, 0) + coefficient
    return answer


def test_h2_atomwise_reference() -> None:
    primary = compile_depth(2)
    reference = compile_factored(5, arbitrary_q0=True)
    for index, root in ((1, primary.A), (3, primary.B), (5, primary.C)):
        left = _rename_h2_layers(expand_coefficient_map(root))
        right = expand_coefficient_map(reference.derivatives[index])
        assert left == right

        left_unit = expand_coefficient_map(specialize_unit_gram(root))
        right_unit = expand_coefficient_map(
            reference.derivatives[index].specialize_unit_gram()
        )
        assert left_unit == right_unit


def test_depth_controls_and_parity() -> None:
    expected = {
        3: {
            "linear": (4, 160, 13888),
            "affine": (10, 540, 71152),
            "quadratic": (14175, 139445032896, 4298284752832899360),
        },
        4: {
            "linear": (5, 400, 73240),
            "affine": (15, 1848, 591176),
            "quadratic": (
                138351807,
                59385566223611232192,
                81427352525619060193821492876576,
            ),
        },
    }
    for depth in (3, 4):
        result = compile_depth(depth)
        assert not result.derivatives[0]
        assert not result.derivatives[2]
        assert not result.derivatives[4]
        assert tuple(terminal_maximum_derivative(root) for root in (result.A, result.B, result.C)) == (1, 3, 5)
        assert tuple(evaluate_polynomial_activation(root, depth, (2,)) for root in (result.A, result.B, result.C)) == (4, 0, 0)
        for name, coefficients in {
            "linear": (0, 1),
            "affine": (1, 1),
            "quadratic": (0, 0, 1),
        }.items():
            actual = tuple(
                evaluate_polynomial_activation(root, depth, coefficients)
                for root in (result.A, result.B, result.C)
            )
            assert actual == expected[depth][name]

