"""Exact all-six-source audit for the general-horizon L=2 transition.

The t=1 paired map has zero coefficient on ``||H^2 g||^2``.  This audit
compiles that sixth elementary differential separately, combines all six
with their exact polynomial-in-t Euler weights, and repeats the hostile
old/new subset census on the resulting polynomial map.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


compiler = load("full_l2_transition_compiler", "full_l2_paired_transition.py")
weights_module = load("general_t_weights", "general_t_transition_weights.py")
F = Fraction


def trim(poly):
    answer = list(poly)
    while answer and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def add(left, right):
    answer = [F(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        answer[index] += value
    for index, value in enumerate(right):
        answer[index] += value
    return trim(answer)


def scale(poly, scalar):
    return trim(tuple(F(scalar) * value for value in poly))


def gaussian_moment(power: int) -> int:
    if power % 2:
        return 0
    answer = 1
    for odd in range(1, power, 2):
        answer *= odd
    return answer


def atom_excess(exponent):
    excess = sum((order - 1) * exponent[order] for order in range(2, 6))
    factors = sum(exponent[2:])
    return excess, factors


def polynomial_map(elementary, weight_polynomials):
    answer = defaultdict(tuple)
    for expression, weight in zip(elementary, weight_polynomials):
        for monomial, coefficient in expression.terms:
            answer[monomial] = add(answer[monomial], scale(weight, coefficient))
    return {monomial: coefficient for monomial, coefficient in answer.items() if coefficient}


def evaluate_identity(expression):
    answer = ()
    for monomial, coefficient in expression.items():
        scalar = 1
        for _layer, exponent in monomial:
            if any(exponent[2:]):
                scalar = 0
                break
            scalar *= gaussian_moment(exponent[0])
        answer = add(answer, scale(coefficient, scalar))
    return answer


def principal_weights(expression, layer=None):
    """Raw polynomials for (phi''')^2, phi''phi4, and phi'phi5."""

    result = [(), (), ()]
    for monomial, coefficient in expression.items():
        high = [atom for atom in monomial if any(atom[1][2:])]
        if len(high) != 1 or (layer is not None and high[0][0] != layer):
            continue
        special = high[0][1]
        kind = None
        multiplier = 1
        if sum(special[2:]) == 2 and special[3] == 2:
            kind = 0
        elif sum(special[2:]) == 2 and special[2] == 1 and special[4] == 1:
            kind = 1
        elif sum(special[2:]) == 1 and special[5] == 1 and special[1] >= 1:
            kind = 2
            multiplier = special[1]
        if kind is None:
            continue
        scalar = multiplier
        removed = False
        for atom in monomial:
            if not removed and atom == high[0]:
                removed = True
                continue
            if any(atom[1][2:]):
                scalar = 0
                break
            scalar *= gaussian_moment(atom[1][0])
        result[kind] = add(result[kind], scale(coefficient, scalar))
    return tuple(result)


def subset_margin_census(expression):
    census = Counter()
    bad = []
    zero = []
    for monomial_index, (monomial, coefficient) in enumerate(expression.items()):
        blocks = []
        for _layer, exponent in monomial:
            excess, factors = atom_excess(exponent)
            if not excess:
                continue
            if (excess, factors) == (4, 1):
                factors = 2
            blocks.append((excess, factors))
        for mask in range(1, 1 << len(blocks)):
            new = [block for bit, block in enumerate(blocks) if mask & (1 << bit)]
            delta_margin = 1 + sum(k + 1 - e for e, k in new)
            gamma_margin_twice = 1 + sum(3 - e for e, _k in new)
            census[(delta_margin, gamma_margin_twice)] += 1
            record = (monomial_index, coefficient, tuple(new), monomial)
            if delta_margin < 0 or gamma_margin_twice < 0:
                bad.append((record, delta_margin, gamma_margin_twice))
            if delta_margin == gamma_margin_twice == 0:
                zero.append(record)
    return dict(sorted(census.items())), bad, zero


def main():
    _paths, elementary = compiler.compile_elementary_maps()
    results = weights_module.exact_results()
    paired_weights = results[2]
    general = polynomial_map(elementary, paired_weights)

    assert len(elementary) == 6
    # The sixth source is genuinely absent at t=1 but nonzero generally.
    assert sum(paired_weights[5], F(0)) == 0
    assert paired_weights[5] != ()

    identity = evaluate_identity(general)
    # Direct scalar identity-network audit: 20 at t=1.
    assert sum(identity, F(0)) == 20

    total = principal_weights(general)
    lower = principal_weights(general, "X")
    upper = principal_weights(general, "Y")
    integrated_total = add(add(total[0], scale(total[1], -1)), total[2])
    integrated_lower = add(add(lower[0], scale(lower[1], -1)), lower[2])
    integrated_upper = add(add(upper[0], scale(upper[1], -1)), upper[2])
    node_symbol = results[6]
    assert integrated_total == scale(node_symbol, 645)
    assert integrated_lower == scale(node_symbol, 15)
    assert integrated_upper == scale(node_symbol, 630)

    census, bad, zero = subset_margin_census(general)
    assert not bad
    assert zero
    assert all(
        len(blocks) == 1 and blocks[0] == (4, 2)
        for _, _, blocks, _monomial in zero
    )

    e6_census, e6_bad, e6_zero = subset_margin_census(
        {monomial: (F(coefficient),) for monomial, coefficient in elementary[5].terms}
    )
    assert not e6_bad
    e6_principal = principal_weights(
        {monomial: (F(coefficient),) for monomial, coefficient in elementary[5].terms}
    )
    e6_integrated = add(
        add(e6_principal[0], scale(e6_principal[1], -1)), e6_principal[2]
    )
    # E6 has no *integrated* quadratic excess-four principal symbol.  Its
    # conservative zero-margin ledger may still contain lone phi^(5)
    # atoms; those improve after four integrations by parts.
    assert not e6_integrated

    print("elementary term counts", tuple(len(item.terms) for item in elementary))
    print("general polynomial-map terms", len(general))
    print("identity polynomial", identity)
    print("raw total principal polynomials", total)
    print("integrated total/lower/upper", integrated_total, integrated_lower, integrated_upper)
    print("all-source subset margin census", census)
    print("all-source zero-margin subsets", len(zero))
    print("E6 subset margins", e6_census)
    print("E6 zero-margin subsets", len(e6_zero))
    print("E6 raw/integrated principal", e6_principal, e6_integrated)
    for record in e6_zero[:20]:
        index, coefficient, blocks, monomial = record
        print("E6 zero", index, coefficient, blocks, monomial)


if __name__ == "__main__":
    main()
