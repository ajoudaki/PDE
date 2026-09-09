"""Compile all six response-aware order-five maps and audit general-t margins."""

from collections import Counter
from fractions import Fraction as F

import full_l2_paired_transition as c


def atom_excess(exponent):
    e = sum((r - 1) * exponent[r] for r in range(2, 6))
    k = sum(exponent[2:])
    return e, k


def elementary_maps():
    q0, q1, q2, q3, q4 = [c.compile_weighted_path(path) for path in c.PATHS]
    flow = c.compile_weighted_path((F(1), F(1, 2), F(1, 3), F(1, 4), F(1, 5)))
    e1 = 120 * q0
    e2 = 6 * (q1 - q0)
    e3 = 4 * (q2 - q0)
    e4 = 2 * (q3 - q1 - q2 + q0)
    e5 = 2 * (q4 - q1)
    e6 = F(15, 2) * (
        flow - F(1, 60) * e1 - F(11, 60) * e2 - F(7, 60) * e3
        - F(1, 4) * e4 - F(3, 10) * e5
    )
    return (e1, e2, e3, e4, e5, e6)


def margin_audit(expressions):
    census = Counter()
    bad = []
    zero = []
    for family, expression in enumerate(expressions, 1):
        for index, (monomial, coefficient) in enumerate(expression.terms):
            blocks = []
            for layer, exponent in monomial:
                e, k = atom_excess(exponent)
                if not e:
                    continue
                if (e, k) == (4, 1):
                    k = 2
                blocks.append((layer, e, k, exponent))
            for mask in range(1, 1 << len(blocks)):
                new = [block for bit, block in enumerate(blocks) if mask & (1 << bit)]
                md = 1 + sum(k + 1 - e for _layer, e, k, _exponent in new)
                mg = 1 + sum(3 - e for _layer, e, _k, _exponent in new)
                census[(md, mg)] += 1
                if md < 0 or mg < 0:
                    bad.append((family, index, coefficient, new, md, mg))
                if (md, mg) == (0, 0):
                    zero.append((family, index, coefficient, new))
    return census, bad, zero


def main():
    maps = elementary_maps()
    print("elementary term counts", tuple(len(expr.terms) for expr in maps))
    # Reconstruct the t=1 pair, including the identically zero E6 weight.
    paired = F(1, 24)*maps[0] + F(5, 3)*maps[1] + maps[2] + F(1, 2)*maps[3] + maps[4]
    _paths, old = c.compile_paired_map()
    assert paired.terms == old.terms
    census, bad, zero = margin_audit(maps)
    print("general-family margin census", dict(sorted(census.items())))
    print("bad", len(bad))
    if bad:
        for item in bad[:20]:
            print("BAD", item)
    print("zero", len(zero), "by family", Counter(item[0] for item in zero))
    assert not bad
    for family, index, coefficient, new in zero:
        assert len(new) == 1 and new[0][1:3] == (4, 2), (family, index, coefficient, new)


if __name__ == "__main__":
    main()
