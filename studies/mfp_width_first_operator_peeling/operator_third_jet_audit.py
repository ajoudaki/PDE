"""Exact polynomial audit for the direct width-first Price third jet.

This script does not derive a coefficient from finite-width initialization
jets.  It checks the last algebraic simplification after the four Gaussian
operator nodes have been differentiated directly at h=0.
"""

from fractions import Fraction


NAMES = ("d", "e", "m", "j", "s", "ell", "b", "r", "t")
N = len(NAMES)


class Poly:
    def __init__(self, terms=None):
        self.terms = {
            powers: Fraction(value)
            for powers, value in (terms or {}).items()
            if value
        }

    @staticmethod
    def constant(value):
        return Poly({(0,) * N: Fraction(value)})

    @staticmethod
    def variable(index):
        powers = [0] * N
        powers[index] = 1
        return Poly({tuple(powers): Fraction(1)})

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly.constant(value)

    def __add__(self, other):
        other = Poly.coerce(other)
        out = dict(self.terms)
        for powers, value in other.terms.items():
            out[powers] = out.get(powers, Fraction(0)) + value
            if not out[powers]:
                del out[powers]
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({powers: -value for powers, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly.coerce(other))

    def __rsub__(self, other):
        return Poly.coerce(other) - self

    def __mul__(self, other):
        other = Poly.coerce(other)
        out = {}
        for left, a in self.terms.items():
            for right, b_value in other.terms.items():
                powers = tuple(x + y for x, y in zip(left, right))
                out[powers] = out.get(powers, Fraction(0)) + a * b_value
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("negative powers are unsupported")
        out = Poly.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power >>= 1
        return out

    def is_zero(self):
        return not self.terms

    def format(self):
        if self.is_zero():
            return "0"
        pieces = []
        for powers, coefficient in sorted(self.terms.items()):
            monomial = "*".join(
                name if power == 1 else f"{name}^{power}"
                for name, power in zip(NAMES, powers)
                if power
            ) or "1"
            pieces.append(f"{coefficient}*{monomial}")
        return " + ".join(pieces)


d, e, m, j, s, ell, b, r, t = [Poly.variable(i) for i in range(N)]

c = 1 + d
k = 2 * d + b + c * (r + t)
tau = ell + 2 * c * m + 3 * c**2 * s + e * d * t

H = c**2 * e + c * tau + 2 * e * d**2 + 3 * d**2 * s + k**2 * ell + 2 * d * k * m
S = (
    3 * c**2 * m
    + 3 * e * d * b
    + 3 * d * m * (d + b)
    + 3 * c**3 * j
    + 3 * c * e * d * r
    + 3 * c * d * m * (r + t)
    + 3 * d**2 * (m + j)
)

beta = b + c * r
delta = d + c * t

# Direct first-terminal Price result.
direct_f1_3 = (
    3 * c**2 * m
    + 3 * c**3 * j
    + 3 * d**2 * (m + j)
    + 3 * d * m * delta
    + 3 * d * (e + m) * beta
)
if not (direct_f1_3 - S).is_zero():
    raise AssertionError("the direct one-step third jet does not equal S_phi")

# Direct lower-operator second jets.
q11_2 = 2 * d * (e + m)
q02_2 = 2 * k * ell + 6 * d * m
q12_2 = 4 * d * e + 7 * d * m + 2 * k * ell
q22_2 = 8 * d * e + 12 * d * m + 4 * k * ell

# First-top response derivatives.
sigma10_1 = delta
sigma11_1 = beta

# Sum L20''' + L21''' obtained by direct lower Price differentiation.
lsum_3 = (
    33 * d * j
    + 18 * k * m
    + 36 * d * s
    + 6 * sigma11_1 * e
    + 12 * k * ell
    + 12 * d * e
    + 39 * d * m
)

# Explicit-h part of the final top Gaussian integrand's third derivative.
explicit_f2_3 = (
    12 * c**2 * e
    + 12 * c * ell
    + 36 * c**3 * s
    + 57 * c**2 * m
    + 33 * c**3 * j
    + d * lsum_3
)

# Price correction from the second jet of the final Q covariance.
covariance_f2_3 = (
    sigma11_1 * (27 * d * e + 39 * d * m + 12 * k * ell)
    + sigma10_1 * (12 * d * e + 39 * d * m + 12 * k * ell)
)

direct_f2_3 = explicit_f2_3 + covariance_f2_3
target_f2_3 = 11 * S + 12 * H

difference = direct_f2_3 - target_f2_3
if not difference.is_zero():
    raise AssertionError(difference.format())

print("exact identity verified: F2'''(0) = 11 S_phi + 12 H_phi")
