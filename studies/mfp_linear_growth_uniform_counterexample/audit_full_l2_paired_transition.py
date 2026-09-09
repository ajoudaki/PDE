"""Exact hostile audit of the full L=2 paired order-five transition sector."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
try:
    from .map_inputs import load_map, parse_map_path
except ImportError:
    from map_inputs import load_map, parse_map_path

DATA = None


def data():
    # No file access at import. Standalone execution selects its input below.
    return DATA if DATA is not None else load_map()


def gaussian_moment(power: int) -> int:
    if power % 2:
        return 0
    answer = 1
    for odd in range(1, power, 2):
        answer *= odd
    return answer


def collapsed_map():
    answer: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for term in data()["paired_map"]:
        key = tuple(sorted(tuple(atom["exponent"]) for atom in term["atoms"]))
        answer[key] += Fraction(term["coefficient"])
    return {key: value for key, value in answer.items() if value}


def identity_value(expression) -> Fraction:
    total = Fraction(0)
    for monomial, coefficient in expression.items():
        value = coefficient
        for atom in monomial:
            if any(atom[2:]):
                value = 0
                break
            value *= gaussian_moment(atom[0])
        total += value
    return total


def atom_excess(atom) -> tuple[int, int]:
    excess = sum((order - 1) * atom[order] for order in range(2, 6))
    factors = sum(atom[2:])
    return excess, factors


def principal_weights(expression):
    # Return the coefficients of int (rho')^2, int rho rho'', and
    # int R rho''' before the three integration-by-parts identities.
    result = [defaultdict(Fraction) for _ in range(3)]
    for monomial, coefficient in expression.items():
        high = [atom for atom in monomial if any(atom[2:])]
        if len(high) != 1:
            continue
        special = high[0]
        kind = None
        multiplier = Fraction(1)
        if sum(special[2:]) == 2 and special[3] == 2:
            kind = 0                       # (phi''')^2
        elif sum(special[2:]) == 2 and special[2] == 1 and special[4] == 1:
            kind = 1                       # phi'' phi''''
        elif sum(special[2:]) == 1 and special[5] == 1 and special[1] >= 1:
            kind = 2                       # one slope variation in phi' phi'''''
            multiplier = Fraction(special[1])
        if kind is None:
            continue

        value = coefficient * multiplier
        removed = False
        for atom in monomial:
            if not removed and atom == special:
                removed = True
                continue
            if any(atom[2:]):
                value = 0
                break
            value *= gaussian_moment(atom[0])
        result[kind][special[0]] += value
    return tuple(dict(item) for item in result)


def layer_principal_weights(layer: str):
    # Perform the same extraction before identifying the two layer alphabets.
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for term in data()["paired_map"]:
        high = [atom for atom in term["atoms"] if any(atom["exponent"][2:])]
        if len(high) != 1 or high[0]["layer"] != layer:
            continue
        special = tuple(high[0]["exponent"])
        kind = None
        multiplier = Fraction(1)
        if sum(special[2:]) == 2 and special[3] == 2:
            kind = 0
        elif sum(special[2:]) == 2 and special[2] == 1 and special[4] == 1:
            kind = 1
        elif sum(special[2:]) == 1 and special[5] == 1 and special[1] >= 1:
            kind = 2
            multiplier = Fraction(special[1])
        if kind is None:
            continue
        value = Fraction(term["coefficient"]) * multiplier
        removed = False
        for atom in term["atoms"]:
            if not removed and atom is high[0]:
                removed = True
                continue
            exponent = atom["exponent"]
            if any(exponent[2:]):
                value = 0
                break
            value *= gaussian_moment(exponent[0])
        result[kind] += value
    return tuple(result)


def lower_general_principal_certificate():
    """Return the three X-principal terms without evaluating Y slope moments."""

    selected = []
    for index, term in enumerate(data()["paired_map"]):
        high = [atom for atom in term["atoms"] if any(atom["exponent"][2:])]
        if len(high) != 1 or high[0]["layer"] != "X":
            continue
        exponent = high[0]["exponent"]
        excess, factors = atom_excess(tuple(exponent))
        if excess == 4 and factors in {1, 2}:
            selected.append((index, term))

    assert [index for index, _term in selected] == [685, 686, 691]
    expected = (
        ("15", [0, 4, 0, 2, 0, 0]),
        ("25", [0, 4, 1, 0, 1, 0]),
        ("5/8", [0, 5, 0, 0, 0, 1]),
    )
    for (_index, term), (coefficient, special) in zip(selected, expected):
        assert term["coefficient"] == coefficient
        assert term["atoms"][0] == {"layer": "X", "exponent": special}
        assert term["atoms"][1:] == [
            {"layer": "Y", "exponent": [0, 2, 0, 0, 0, 0]},
            {"layer": "Y", "exponent": [0, 2, 0, 0, 0, 0]},
            {"layer": "Y", "exponent": [0, 2, 0, 0, 0, 0]},
        ]
    return tuple(index for index, _term in selected)


def maximum_naive_sector_factorization():
    # A moment atom with excess e>0 contributes naively w^(1-e).  Extract
    # the complete w^-5 sector and compare it with the displayed product.
    actual: dict[tuple[tuple[str, tuple[int, ...]], ...], Fraction] = defaultdict(Fraction)
    for term in data()["paired_map"]:
        degree = 0
        key = []
        for atom in term["atoms"]:
            exponent = tuple(atom["exponent"])
            excess, _ = atom_excess(exponent)
            if excess:
                degree += excess - 1
            key.append((atom["layer"], exponent))
        if degree == 5:
            actual[tuple(sorted(key))] += Fraction(term["coefficient"])
    actual = {key: value for key, value in actual.items() if value}

    def atom(layer: str, digits: str):
        return (layer, tuple(int(char) for char in digits))

    factors = [
        {atom("X", "220000"): Fraction(1)},
        {atom("X", "220000"): Fraction(1)},
        {atom("X", "020000"): Fraction(1), atom("X", "200000"): Fraction(1)},
        {atom("X", "020000"): Fraction(1), atom("X", "200000"): Fraction(1)},
        {atom("X", "020000"): Fraction(1), atom("X", "200000"): Fraction(1)},
        {
            atom("Y", "000200"): Fraction(1),
            atom("Y", "001010"): Fraction(2),
            atom("Y", "010001"): Fraction(1),
        },
        {atom("Y", "002000"): Fraction(1), atom("Y", "010100"): Fraction(1)},
        {atom("Y", "002000"): Fraction(1), atom("Y", "010100"): Fraction(1)},
    ]
    expected = {(): Fraction(1)}
    for factor in factors:
        updated: dict[tuple[tuple[str, tuple[int, ...]], ...], Fraction] = defaultdict(Fraction)
        for left, a in expected.items():
            for right, b in factor.items():
                updated[tuple(sorted(left + (right,)))] += a * b
        expected = dict(updated)
    assert actual == expected
    return len(actual)


def margin_census():
    # For w=delta*sqrt(gamma), replace a lone excess-four fifth derivative
    # by its first nontrivial (quadratic-amplitude) contribution.  The pair
    # below records powers of delta and sqrt(gamma) after division by the
    # principal delta^-1 gamma^-1/2 scale.
    census = Counter()
    bad = []
    principal_only = 0
    for index, term in enumerate(data()["paired_map"]):
        blocks = []
        for atom in term["atoms"]:
            excess, factors = atom_excess(tuple(atom["exponent"]))
            if not excess:
                continue
            if (excess, factors) == (4, 1):
                factors = 2
            blocks.append((excess, factors))
        # Any nonempty subset of the high-derivative moment atoms may come
        # from the newly inserted interval; the complementary atoms may be
        # arbitrarily large but fixed remnants of the finite old ladder.
        for mask in range(1, 1 << len(blocks)):
            new_blocks = [block for bit, block in enumerate(blocks) if mask & (1 << bit)]
            delta_margin = 1 + sum(k + 1 - e for e, k in new_blocks)
            gamma_margin_twice = 1 + sum(3 - e for e, _k in new_blocks)
            census[(delta_margin, gamma_margin_twice)] += 1
            if delta_margin < 0 or gamma_margin_twice < 0:
                bad.append((index, new_blocks, delta_margin, gamma_margin_twice))
            if (delta_margin, gamma_margin_twice) == (0, 0):
                assert len(new_blocks) == 1 and new_blocks[0] == (4, 2)
                principal_only += 1
    assert not bad
    return dict(sorted(census.items())), principal_only


def cubic_principal_weights():
    path = HERE / "full_l2_paired_transition.py"
    spec = importlib.util.spec_from_file_location("paired_transition_compiler", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    cubic = module.compile_paired_cubic_map()

    def extract(expression, layer):
        result = [Fraction(0), Fraction(0)]
        for monomial, coefficient in expression.terms:
            high = [atom for atom in monomial if any(atom[1][2:])]
            if len(high) != 1 or high[0][0] != layer:
                continue
            special = high[0][1]
            kind = None
            multiplier = 1
            if sum(special[2:]) == 2 and special[2] == 2:
                kind = 0                       # (phi'')^2
            elif sum(special[2:]) == 1 and special[3] == 1 and special[1] >= 1:
                kind = 1                       # slope variation times phi'''
                multiplier = special[1]
            if kind is None:
                continue
            value = coefficient * multiplier
            removed = False
            for atom in monomial:
                if not removed and atom == high[0]:
                    removed = True
                    continue
                if any(atom[1][2:]):
                    value = 0
                    break
                value *= gaussian_moment(atom[1][0])
            result[kind] += value
        return tuple(result)

    lower = extract(cubic, "X")
    upper = extract(cubic, "Y")
    collapsed = cubic.collapse_unit_layers()
    total = extract(collapsed, "M")
    assert len(cubic.terms) == 50
    assert lower == (Fraction(6), Fraction(9, 2))
    assert upper == (Fraction(68), Fraction(55))
    assert total == (Fraction(74), Fraction(119, 2))
    assert total[0] - total[1] == Fraction(29, 2)

    margins = Counter()
    zero_margin = 0
    for monomial, _coefficient in cubic.terms:
        blocks = []
        for _layer, exponent in monomial:
            excess, factors = atom_excess(exponent)
            if not excess:
                continue
            if (excess, factors) == (2, 1):
                factors = 2
            blocks.append((excess, factors))
        for mask in range(1, 1 << len(blocks)):
            new_blocks = [block for bit, block in enumerate(blocks) if mask & (1 << bit)]
            # Divide by delta^2 gamma w^-1 = delta gamma^(1/2).
            delta_margin = sum(k + 1 - e for e, k in new_blocks) - 1
            gamma_margin_twice = sum(3 - e for e, _k in new_blocks) - 1
            assert delta_margin >= 0 and gamma_margin_twice >= 0
            margins[(delta_margin, gamma_margin_twice)] += 1
            if (delta_margin, gamma_margin_twice) == (0, 0):
                assert len(new_blocks) == 1 and new_blocks[0] == (2, 2)
                zero_margin += 1
    return len(cubic.terms), lower, upper, total, dict(sorted(margins.items()))


def main() -> None:
    global DATA
    DATA = load_map(parse_map_path())
    expression = collapsed_map()
    assert len(data()["paired_map"]) == 979
    assert len(expression) == 954
    assert identity_value(expression) == 20

    total = principal_weights(expression)
    assert total == ({0: Fraction(783)}, {0: Fraction(1481)}, {0: Fraction(3219, 8)})
    total_ibp = total[0][0] - total[1][0] + total[2][0]
    assert total_ibp == Fraction(-2365, 8)

    lower = layer_principal_weights("X")
    upper = layer_principal_weights("Y")
    assert lower == (Fraction(15), Fraction(25), Fraction(25, 8))
    assert upper == (Fraction(768), Fraction(1456), Fraction(1597, 4))
    assert lower[0] - lower[1] + lower[2] == Fraction(-55, 8)
    assert upper[0] - upper[1] + upper[2] == Fraction(-1155, 4)
    lower_general = lower_general_principal_certificate()

    worst_terms = maximum_naive_sector_factorization()
    margins, principal_terms = margin_census()
    cubic = cubic_principal_weights()
    assert worst_terms == 36
    assert principal_terms == 267

    print("layer-separated terms", len(data()["paired_map"]))
    print("unit-layer terms", len(expression))
    print("identity control", identity_value(expression))
    print("quadratic principal raw weights", total)
    print("quadratic principal integrated weight", total_ibp)
    print("lower/upper raw weights", lower, upper)
    print("general-background lower principal indices", lower_general)
    print("naive w^-5 factorized terms", worst_terms)
    print("scaled-margin census", margins)
    print("zero-margin single principal terms", principal_terms)
    print("cubic terms and lower/upper/total raw weights", cubic)


if __name__ == "__main__":
    main()
