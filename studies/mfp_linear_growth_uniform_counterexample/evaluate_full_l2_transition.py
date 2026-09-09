"""High-precision evaluator for the exact paired order-five moment map.

The normalized activation family is

    psi_w(x) = (x + delta*w*exp(-((x-X)/w)^2/2)) / ||...||_{L2(gamma)}.

Every required Gaussian activation moment is evaluated analytically by
expanding into polynomial times Gaussian factors.  Decimal arithmetic is
used only after this exact finite expansion; no quadrature is involved.
"""

from __future__ import annotations

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
try:
    from .map_inputs import load_map, parse_map_path
except ImportError:
    from map_inputs import load_map, parse_map_path


def poly_mul(left: dict[int, Fraction], right: dict[int, Fraction]):
    out: dict[int, Fraction] = defaultdict(Fraction)
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] += a * b
    return {k: v for k, v in out.items() if v}


def poly_pow(base: dict[int, Fraction], power: int):
    out = {0: Fraction(1)}
    for _ in range(power):
        out = poly_mul(out, base)
    return out


HERMITE_DERIVATIVE = {
    1: {1: Fraction(-1)},
    2: {2: Fraction(1), 0: Fraction(-1)},
    3: {3: Fraction(-1), 1: Fraction(3)},
    4: {4: Fraction(1), 2: Fraction(-6), 0: Fraction(3)},
    5: {5: Fraction(-1), 3: Fraction(10), 1: Fraction(-15)},
}


def dec_fraction(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def normal_raw_moment(power: int, mean: Decimal, variance: Decimal) -> Decimal:
    answer = Decimal(0)
    for pairs in range(power // 2 + 1):
        singles = power - 2 * pairs
        coefficient = Decimal(comb(power, 2 * pairs))
        double_factorial = 1
        for odd in range(1, 2 * pairs, 2):
            double_factorial *= odd
        mean_factor = Decimal(1) if singles == 0 else mean**singles
        answer += coefficient * Decimal(double_factorial) * variance**pairs * mean_factor
    return answer


def localized_integral(
    polynomial: dict[int, Fraction],
    gaussian_power: int,
    coefficient: Decimal,
    w: Decimal,
    center: Decimal,
) -> Decimal:
    """Integral gamma(center+w*y) coefficient*poly(y)*P(y)^k dy."""

    if gaussian_power <= 0:
        raise ValueError("localized terms must contain a P factor")
    a = Decimal(gaussian_power) + w * w
    b = center * w
    mean = -b / a
    variance = Decimal(1) / a
    # gamma(center+w*y) times the unnormalised Gaussian integral.
    prefactor = (
        coefficient
        * (-center * center / Decimal(2)).exp()
        / a.sqrt()
        * (b * b / (Decimal(2) * a)).exp()
    )
    value = Decimal(0)
    for power, rational in polynomial.items():
        value += dec_fraction(rational) * normal_raw_moment(power, mean, variance)
    return prefactor * value


def x_polynomial(power: int, w: Decimal, center: Decimal):
    return {
        k: Fraction(comb(power, k)) * Fraction(w) ** k * Fraction(center) ** (power - k)
        for k in range(power + 1)
    }


def base_normal_moment(power: int) -> Decimal:
    if power % 2:
        return Decimal(0)
    value = 1
    for odd in range(1, power, 2):
        value *= odd
    return Decimal(value)


def raw_atom(exponent, w: Decimal, center: Decimal, delta: Decimal) -> Decimal:
    """Gaussian moment for raw phi=x+delta*w*P and its derivatives."""

    nu = tuple(int(value) for value in exponent)
    has_high = any(nu[r] for r in range(2, 6))
    answer = Decimal(0)

    # Choose i localized P factors from phi^nu0 and j P' factors from
    # (1+delta P')^nu1.  High derivatives always contribute a P factor.
    for i in range(nu[0] + 1):
        for j in range(nu[1] + 1):
            if not has_high and i == 0 and j == 0:
                answer += base_normal_moment(nu[0])
                continue

            delta_j = Decimal(1) if j == 0 else delta**j
            coefficient = (
                Decimal(comb(nu[0], i))
                * Decimal(comb(nu[1], j))
                * (delta * w) ** i
                * delta_j
            )
            polynomial = x_polynomial(nu[0] - i, w, center)
            gaussian_power = i + j
            if j:
                polynomial = poly_mul(polynomial, poly_pow(HERMITE_DERIVATIVE[1], j))

            for derivative in range(2, 6):
                multiplicity = nu[derivative]
                if not multiplicity:
                    continue
                coefficient *= (delta * w ** (1 - derivative)) ** multiplicity
                polynomial = poly_mul(
                    polynomial,
                    poly_pow(HERMITE_DERIVATIVE[derivative], multiplicity),
                )
                gaussian_power += multiplicity

            answer += w * localized_integral(
                polynomial, gaussian_power, coefficient, w, center
            )
    return answer


def load_collapsed_map(map_path=None):
    data = load_map(map_path)
    combined: dict[tuple[tuple[int, ...], ...], Fraction] = defaultdict(Fraction)
    for term in data["paired_map"]:
        key = tuple(sorted(tuple(atom["exponent"]) for atom in term["atoms"]))
        combined[key] += Fraction(term["coefficient"])
    return {key: value for key, value in combined.items() if value}


def evaluate(w_text: str, center_text: str = "2", delta_text: str = "0.1", *, map_path=None):
    getcontext().prec = 100
    w = Decimal(w_text)
    center = Decimal(center_text)
    delta = Decimal(delta_text)
    expression = load_collapsed_map(map_path)
    atoms = {atom for monomial in expression for atom in monomial}
    raw_q = raw_atom((2, 0, 0, 0, 0, 0), w, center, delta)
    scale = raw_q.sqrt()
    values = {}
    for atom in atoms:
        raw = raw_atom(atom, w, center, delta)
        values[atom] = raw / scale ** sum(atom)
    total = Decimal(0)
    for monomial, rational in expression.items():
        value = dec_fraction(rational)
        for atom in monomial:
            value *= values[atom]
        total += value
    return total, raw_q, len(atoms), len(expression)


def main():
    map_path = parse_map_path()
    for w in ("0.2", "0.1", "0.05", "0.025", "0.0125", "0.00625"):
        value, q, atoms, terms = evaluate(w, map_path=map_path)
        print(w, value, "w3", value * Decimal(w) ** 3, "w1", value * Decimal(w), "q", q)
    print("atoms", atoms, "terms", terms)


if __name__ == "__main__":
    main()
