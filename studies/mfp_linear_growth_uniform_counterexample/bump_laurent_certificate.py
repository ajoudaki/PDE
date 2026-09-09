"""Exact delta^2 Laurent census for the full L=2 paired order-five map.

The raw activation is

    Phi(x) = x + delta*w*exp(-((x-X)/w)^2/2).

The script expands every one-dimensional moment atom in the frozen 979-term
map, retaining exact rational coefficients.  Expressions use the formal
basis

    H = exp(-X^2/2),   R = 1/sqrt(2),   X.

Thus a key ``(h,r,x)`` denotes ``H**h * R**r * X**x``.  No numerical
quadrature or floating-point cancellation is used.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path


HERE = Path(__file__).resolve().parent
MAP = HERE / "FULL_L2_PAIRED_ORDER5_MAP.json"


def poly_add(a, b):
    out = defaultdict(Fraction, a)
    for k, v in b.items():
        out[k] += v
    return {k: v for k, v in out.items() if v}


def poly_mul(a, b):
    out = defaultdict(Fraction)
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] += x * y
    return {k: v for k, v in out.items() if v}


def poly_derivative(a):
    return {k - 1: k * v for k, v in a.items() if k}


def poly_shift(a):
    return {k + 1: v for k, v in a.items()}


def poly_pow(a, n):
    out = {0: Fraction(1)}
    for _ in range(n):
        out = poly_mul(out, a)
    return out


# Q_r satisfies d^r exp(-y^2/2)/dy^r = Q_r(y) exp(-y^2/2).
Q = [{0: Fraction(1)}]
for _ in range(5):
    Q.append(poly_add(poly_derivative(Q[-1]), {k: -v for k, v in poly_shift(Q[-1]).items()}))


def odd_double_factorial(n):
    if n <= 0:
        return 1
    out = 1
    for k in range(1, n + 1, 2):
        out *= k
    return out


# Expr is a sparse rational combination of H^h R^r X^x.
def expr_add(a, b):
    out = defaultdict(Fraction, a)
    for k, v in b.items():
        out[k] += v
    return {k: v for k, v in out.items() if v}


def expr_scale(a, c):
    return {k: c * v for k, v in a.items() if c * v}


def expr_mul(a, b):
    out = defaultdict(Fraction)
    for (ha, ra, xa), ca in a.items():
        for (hb, rb, xb), cb in b.items():
            out[(ha + hb, ra + rb, xa + xb)] += ca * cb
    return {k: v for k, v in out.items() if v}


def gaussian_base_moment(power):
    if power % 2:
        return Fraction(0)
    return Fraction(odd_double_factorial(power - 1))


def integrate_localized(poly, localized_factors):
    """Return gamma(X) times the y integral in the H,R basis."""

    out = defaultdict(Fraction)
    for ypower, coefficient in poly.items():
        if ypower % 2:
            continue
        pairs = ypower // 2
        moment = Fraction(odd_double_factorial(ypower - 1), localized_factors**pairs)
        # sqrt(2*pi/m) / sqrt(2*pi) = 1/sqrt(m).
        if localized_factors == 1:
            rpower = 0
        elif localized_factors == 2:
            rpower = 1
        else:
            raise ValueError("delta degree at most two was expected")
        out[(1, rpower, 0)] += coefficient * moment
    return dict(out)


def atom_series(exponent, max_density_order=8):
    """Map (delta degree, w power) to an exact Expr."""

    nu = tuple(exponent)
    out = defaultdict(dict)
    high_count = sum(nu[2:])

    if high_count == 0:
        base = gaussian_base_moment(nu[0])
        if base:
            out[(0, 0)] = {(0, 0, 0): base}

    for i0 in range(nu[0] + 1):
        for i1 in range(nu[1] + 1):
            ddegree = i0 + i1 + high_count
            if ddegree == 0 or ddegree > 2:
                continue
            localized = ddegree
            choose = Fraction(comb(nu[0], i0) * comb(nu[1], i1))
            derivative_poly = poly_pow(Q[0], i0)
            derivative_poly = poly_mul(derivative_poly, poly_pow(Q[1], i1))
            base_w = i0
            for r in range(2, 6):
                derivative_poly = poly_mul(derivative_poly, poly_pow(Q[r], nu[r]))
                base_w += (1 - r) * nu[r]

            # Expand each unperturbed x as X + w*y.
            for x_y_count in range(nu[0] - i0 + 1):
                x_count = nu[0] - i0 - x_y_count
                xcoef = Fraction(comb(nu[0] - i0, x_y_count))
                xy_poly = poly_mul(derivative_poly, {x_y_count: Fraction(1)})

                # gamma(X+w*y)/gamma(X)
                # = exp(-X*w*y) exp(-w^2*y^2/2).
                for a in range(max_density_order + 1):
                    for b in range((max_density_order - a) // 2 + 1):
                        density_order = a + 2 * b
                        density_coef = Fraction((-1) ** (a + b), factorial(a) * factorial(b) * 2**b)
                        density_poly = poly_mul(xy_poly, {a + 2 * b: Fraction(1)})
                        integral = integrate_localized(density_poly, localized)
                        integral = {
                            (hp, rp, xp + x_count + a): value
                            for (hp, rp, xp), value in integral.items()
                        }
                        coefficient = choose * xcoef * density_coef
                        wpow = 1 + base_w + x_y_count + density_order
                        key = (ddegree, wpow)
                        out[key] = expr_add(out[key], expr_scale(integral, coefficient))
    return {k: v for k, v in out.items() if v}


def series_mul(a, b, min_w=-12, max_w=4):
    out = defaultdict(dict)
    for (da, wa), ea in a.items():
        for (db, wb), eb in b.items():
            if da + db > 2 or not min_w <= wa + wb <= max_w:
                continue
            key = (da + db, wa + wb)
            out[key] = expr_add(out[key], expr_mul(ea, eb))
    return {k: v for k, v in out.items() if v}


def compile_census():
    data = json.loads(MAP.read_text())
    atoms = {
        tuple(atom["exponent"])
        for term in data["paired_map"]
        for atom in term["atoms"]
    }
    cache = {atom: atom_series(atom) for atom in atoms}
    total = defaultdict(dict)
    for term in data["paired_map"]:
        series = {(0, 0): {(0, 0, 0): Fraction(1)}}
        for atom in term["atoms"]:
            series = series_mul(series, cache[tuple(atom["exponent"])])
        coefficient = Fraction(term["coefficient"])
        for key, expression in series.items():
            total[key] = expr_add(total[key], expr_scale(expression, coefficient))
    return {key: value for key, value in total.items() if value}


def main():
    result = compile_census()
    print("nonzero delta^2 Laurent powers")
    for (degree, wpow), expression in sorted(result.items()):
        if degree == 2 and wpow <= 0:
            print(wpow, expression)


if __name__ == "__main__":
    main()
