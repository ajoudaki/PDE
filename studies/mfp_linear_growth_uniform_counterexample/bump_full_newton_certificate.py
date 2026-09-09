"""Exact all-amplitude Newton/Laurent census for the localized bump.

This consumes ``FULL_L2_PAIRED_ORDER5_MAP.json`` and expands the normalized
activation

    phi(x) = (x + d*w*exp(-((x-X)/w)^2/2)) / ||...||_2

through every amplitude degree present in the finite map.  Coefficients are
stored in the exact basis ``H^a X^b / sqrt(s)``, where
``H=exp(-X^2/2)`` and ``s`` is square-free.  The purpose is to certify the
most singular power of ``w`` after all 979 monomials and the RMS
normalization have been combined.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb, factorial
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
try:
    from .map_inputs import load_map, parse_map_path
except ImportError:
    from map_inputs import load_map, parse_map_path
MAX_DELTA = 20
MIN_W = -12
MAX_W = 6
MAX_DENSITY = 10


def padd(a, b):
    out = defaultdict(Fraction, a)
    for k, v in b.items():
        out[k] += v
    return {k: v for k, v in out.items() if v}


def pmul(a, b):
    out = defaultdict(Fraction)
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] += x * y
    return {k: v for k, v in out.items() if v}


def ppow(a, n):
    out = {0: Fraction(1)}
    for _ in range(n):
        out = pmul(out, a)
    return out


def pder(a):
    return {k - 1: k * v for k, v in a.items() if k}


Q = [{0: Fraction(1)}]
for _ in range(5):
    Q.append(padd(pder(Q[-1]), {k + 1: -v for k, v in Q[-1].items()}))


def odd_df(n):
    out = 1
    for k in range(1, n + 1, 2):
        out *= k
    return out


def square_decompose(n):
    """Return q,s with n=q^2*s and s square-free."""
    q = 1
    s = 1
    p = 2
    while p * p <= n:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        q *= p ** (count // 2)
        if count % 2:
            s *= p
        p += 1
    if n > 1:
        s *= n
    return q, s


# Exact expression key: (power of H, square-free radical denominator, X power).
def eadd(a, b):
    out = defaultdict(Fraction, a)
    for k, v in b.items():
        out[k] += v
    return {k: v for k, v in out.items() if v}


def escale(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def emul(a, b):
    out = defaultdict(Fraction)
    for (ha, sa, xa), ca in a.items():
        for (hb, sb, xb), cb in b.items():
            q, s = square_decompose(sa * sb)
            out[(ha + hb, s, xa + xb)] += ca * cb / q
    return {k: v for k, v in out.items() if v}


def base_moment(power):
    if power % 2:
        return Fraction(0)
    return Fraction(odd_df(power - 1))


def local_integral(poly, localized):
    q, squarefree = square_decompose(localized)
    out = defaultdict(Fraction)
    for power, coefficient in poly.items():
        if power % 2:
            continue
        pairs = power // 2
        value = coefficient * Fraction(odd_df(power - 1), localized**pairs * q)
        out[(1, squarefree, 0)] += value
    return dict(out)


def atom_series(exponent):
    nu = tuple(exponent)
    high = sum(nu[2:])
    out = defaultdict(dict)
    if high == 0:
        value = base_moment(nu[0])
        if value:
            out[(0, 0)] = {(0, 1, 0): value}

    for i0 in range(nu[0] + 1):
        for i1 in range(nu[1] + 1):
            degree = i0 + i1 + high
            if degree == 0 or degree > MAX_DELTA:
                continue
            localized = degree
            choose = Fraction(comb(nu[0], i0) * comb(nu[1], i1))
            derivative_poly = pmul(ppow(Q[0], i0), ppow(Q[1], i1))
            base_w = i0
            for r in range(2, 6):
                derivative_poly = pmul(derivative_poly, ppow(Q[r], nu[r]))
                base_w += (1 - r) * nu[r]

            remaining_x = nu[0] - i0
            for xy in range(remaining_x + 1):
                xpower = remaining_x - xy
                xycoef = Fraction(comb(remaining_x, xy))
                initial_poly = pmul(derivative_poly, {xy: Fraction(1)})
                for a in range(MAX_DENSITY + 1):
                    for b in range((MAX_DENSITY - a) // 2 + 1):
                        density_order = a + 2 * b
                        wpow = 1 + base_w + xy + density_order
                        if not MIN_W <= wpow <= MAX_W:
                            continue
                        coefficient = choose * xycoef * Fraction(
                            (-1) ** (a + b), factorial(a) * factorial(b) * 2**b
                        )
                        polynomial = pmul(initial_poly, {a + 2 * b: Fraction(1)})
                        expression = local_integral(polynomial, localized)
                        expression = {
                            (hp, sf, xp + xpower + a): value
                            for (hp, sf, xp), value in expression.items()
                        }
                        key = (degree, wpow)
                        out[key] = eadd(out[key], escale(expression, coefficient))
    return {k: v for k, v in out.items() if v}


def smul(a, b):
    out = defaultdict(dict)
    for (da, wa), ea in a.items():
        for (db, wb), eb in b.items():
            degree = da + db
            wpow = wa + wb
            if degree > MAX_DELTA or not MIN_W <= wpow <= MAX_W:
                continue
            key = (degree, wpow)
            out[key] = eadd(out[key], emul(ea, eb))
    return {k: v for k, v in out.items() if v}


def sscale(a, c):
    return {k: escale(v, c) for k, v in a.items() if escale(v, c)}


def spow(a, n):
    out = {(0, 0): {(0, 1, 0): Fraction(1)}}
    for _ in range(n):
        out = smul(out, a)
    return out


def generalized_binomial(alpha, n):
    out = Fraction(1)
    for j in range(n):
        out *= alpha - j
    return out / factorial(n)


def normalization_series(total_factors):
    q = atom_series((2, 0, 0, 0, 0, 0))
    u = dict(q)
    u[(0, 0)] = eadd(u.get((0, 0), {}), {(0, 1, 0): Fraction(-1)})
    u = {k: v for k, v in u.items() if v}
    alpha = Fraction(-total_factors, 2)
    answer = {(0, 0): {(0, 1, 0): Fraction(1)}}
    power = {(0, 0): {(0, 1, 0): Fraction(1)}}
    # u has delta degree at least one, so twenty powers terminate.
    for j in range(1, MAX_DELTA + 1):
        power = smul(power, u)
        if not power:
            break
        answer = _sadd(answer, sscale(power, generalized_binomial(alpha, j)))
    return answer


def _sadd(a, b):
    out = defaultdict(dict, a)
    for key, expression in b.items():
        out[key] = eadd(out[key], expression)
    return {k: v for k, v in out.items() if v}


def compile_map(map_path=None):
    DATA = load_map(map_path)
    ATOM_CACHE = {
        tuple(atom["exponent"]): atom_series(atom["exponent"])
        for term in DATA["paired_map"]
        for atom in term["atoms"]
    }
    total = defaultdict(dict)
    for term in DATA["paired_map"]:
        series = {(0, 0): {(0, 1, 0): Fraction(1)}}
        factors = 0
        ordered_atoms = sorted(
            term["atoms"],
            key=lambda atom: min(w for _, w in ATOM_CACHE[tuple(atom["exponent"])])
        )
        for atom in ordered_atoms:
            exponent = tuple(atom["exponent"])
            factors += sum(exponent)
            series = smul(series, ATOM_CACHE[exponent])
        series = smul(series, normalization_series(factors))
        coefficient = Fraction(term["coefficient"])
        for key, expression in series.items():
            total[key] = eadd(total[key], escale(expression, coefficient))
    return {k: v for k, v in total.items() if v}


def main():
    result = compile_map(parse_map_path())
    print("nonzero negative Laurent powers after all 979 terms")
    for (degree, wpow), expression in sorted(result.items()):
        if wpow < 0:
            print("delta", degree, "w", wpow, expression)


if __name__ == "__main__":
    main()
