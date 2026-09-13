"""Slow rational fixed-point backend with no library precision ceiling.

Every retained scalar is an integer multiple of 10**(-digits). Basic operations
round to nearest (ties to even); elementary functions use finite rational series.
This backend supplies an executable arithmetic refinement, not an error certificate.
"""
from fractions import Fraction
from decimal import Decimal
import math


def nearest(value):
    q, r = divmod(value.numerator, value.denominator)
    return q + int(2*r > value.denominator or (2*r == value.denominator and q % 2))


def _atan(x, tolerance):
    power, total, k = x, x, 1
    while True:
        power *= -x*x
        term = power/(2*k+1)
        total += term
        if abs(term) <= tolerance:
            return total
        k += 1


def rational_pi(digits):
    tolerance = Fraction(1, 10**(digits+5))
    return 16*_atan(Fraction(1, 5), tolerance)-4*_atan(Fraction(1, 239), tolerance)


def _log_unit(x, tolerance):
    # x in [1,2], so z in [0,1/3]; omitted tail <= 3*next term.
    z = (x-1)/(x+1)
    power, total, k = z, z, 1
    while True:
        power *= z*z
        term = power/(2*k+1)
        total += term
        if abs(term) <= tolerance:
            return 2*total
        k += 1


class Fixed:
    __slots__ = ("units", "digits", "scale")
    __array_priority__ = 0

    def __init__(self, value, digits):
        self.digits, self.scale = digits, 10**digits
        if isinstance(value, Fixed):
            value = value.fraction()
        elif isinstance(value, Decimal):
            value = Fraction(value)
        elif isinstance(value, float):
            if not math.isfinite(value):
                raise ValueError("nonfinite fixed-point input")
            value = Fraction.from_float(value)
        else:
            value = Fraction(value)
        self.units = nearest(value*self.scale)

    @classmethod
    def from_units(cls, units, digits):
        result = object.__new__(cls)
        result.units, result.digits, result.scale = units, digits, 10**digits
        return result

    def fraction(self):
        return Fraction(self.units, self.scale)

    def _other(self, other):
        if isinstance(other, Fixed):
            if other.digits != self.digits:
                raise ValueError("fixed-point arithmetic precision mismatch")
            return other
        try:
            return Fixed(other, self.digits)
        except (TypeError, ValueError):
            return NotImplemented

    def __add__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else Fixed.from_units(self.units+other.units, self.digits)

    __radd__ = __add__

    def __neg__(self):
        return Fixed.from_units(-self.units, self.digits)

    def __sub__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else self+(-other)

    def __rsub__(self, other):
        return (-self)+other

    def __mul__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else Fixed.from_units(nearest(Fraction(self.units*other.units, self.scale)), self.digits)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else Fixed.from_units(nearest(Fraction(self.units*self.scale, other.units)), self.digits)

    def __rtruediv__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else other/self

    def __pow__(self, power):
        if not isinstance(power, int):
            return NotImplemented
        if power < 0:
            return Fixed(1, self.digits)/(self**(-power))
        value, base = Fixed(1, self.digits), self
        while power:
            if power & 1:
                value *= base
            power //= 2
            if power:
                base *= base
        return value

    def __abs__(self):
        return Fixed.from_units(abs(self.units), self.digits)

    def __pos__(self):
        return self

    def __float__(self):
        return float(self.fraction())

    def __bool__(self):
        return self.units != 0

    def __eq__(self, other):
        other = self._other(other)
        return False if other is NotImplemented else self.units == other.units

    def __lt__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else self.units < other.units

    def __le__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else self.units <= other.units

    def __gt__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else self.units > other.units

    def __ge__(self, other):
        other = self._other(other)
        return NotImplemented if other is NotImplemented else self.units >= other.units

    def __repr__(self):
        return "Fixed.from_units("+hex(self.units)+", "+str(self.digits)+")"

    def is_finite(self):
        return True

    def sqrt(self):
        if self.units < 0:
            raise ValueError("negative square root")
        # floor differs from the exact root by less than one output unit.
        return Fixed.from_units(math.isqrt(self.units*self.scale), self.digits)

    def ln(self):
        if self.units <= 0:
            raise ValueError("logarithm requires a positive argument")
        x, k = self.fraction(), 0
        while x >= 2:
            x /= 2
            k += 1
        while x < 1:
            x *= 2
            k -= 1
        tolerance = Fraction(1, 10**(self.digits+5)*(abs(k)+1))
        return Fixed(_log_unit(x, tolerance)+k*_log_unit(Fraction(2), tolerance), self.digits)

    def exp(self):
        x = abs(self.fraction())
        if not x:
            return Fixed(1, self.digits)
        y, squarings = x, 0
        while y > Fraction(1, 2):
            y /= 2
            squarings += 1
        # Exact rational powering propagates series error by at most
        # 2**s * exp(2*x); 10**(ceil(2*x)+s+5) is a larger guard.
        guard = (2*x.numerator+x.denominator-1)//x.denominator+squarings+5
        tolerance = Fraction(1, 10**(self.digits+guard))
        term, value, n = Fraction(1), Fraction(1), 1
        while True:
            term *= y/n
            value += term
            if term <= tolerance:
                break
            n += 1
        for _ in range(squarings):
            value *= value
        if self.units < 0:
            value = 1/value
        return Fixed(value, self.digits)

    def trig(self, cosine=False):
        pi = rational_pi(self.digits+5)
        x = self.fraction() % (2*pi)
        if x > pi:
            x -= 2*pi
        term = Fraction(1) if cosine else x
        value, k = term, 0
        tolerance = Fraction(1, 10**(self.digits+5))
        while True:
            a = 2*k+1 if cosine else 2*k+2
            term *= -x*x/(a*(a+1))
            value += term
            if abs(term) <= tolerance:
                return Fixed(value, self.digits)
            k += 1
