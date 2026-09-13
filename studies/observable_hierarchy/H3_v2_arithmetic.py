"""Finite arithmetic and joint Gaussian cubature for the observable solver.

Float64 is the fast backend. Decimal precision is an actual refinement axis.
No positive covariance direction is deleted: callers regularize before the
strict Cholesky factorization. This module contains no training model.
"""
from contextlib import nullcontext
from decimal import Decimal, localcontext, getcontext, MAX_EMAX, MIN_EMIN
from fractions import Fraction
import math

import numpy as np
from pde.observable_fixed import Fixed, rational_pi


class Arithmetic:
    def __init__(self, digits=None, backend="decimal"):
        if digits is not None and (isinstance(digits, bool) or not isinstance(digits, int) or digits < 20):
            raise ValueError("digits must be None (float64) or an integer at least 20")
        self.digits = digits
        if backend not in ("decimal", "rational") or (backend == "rational" and digits is None):
            raise ValueError("backend must be decimal or rational; rational requires digits")
        self.backend = backend
        self.dtype = float if digits is None else object

    def context(self):
        if self.digits is None or self.backend == "rational":
            return nullcontext()
        active = getcontext().copy()
        active.prec = self.digits
        active.Emax, active.Emin = MAX_EMAX, MIN_EMIN
        return localcontext(active)

    def real(self, value):
        with self.context():
            return self._real(value)

    def _real(self, value):
        if isinstance(value, bool):
            raise ValueError("booleans are not numerical inputs")
        if self.backend == "rational":
            return Fixed(value, self.digits)
        if isinstance(value, Fraction):
            return self._real(value.numerator) / self._real(value.denominator)
        if self.digits is None:
            result = float(value)
            if not math.isfinite(result):
                raise ValueError("nonfinite numerical input")
            return result
        result = value if isinstance(value, Decimal) else (Decimal(int(value)) if isinstance(value, (int, np.integer)) else Decimal(str(value)))
        if not result.is_finite():
            raise ValueError("nonfinite numerical input")
        return +result

    def array(self, value):
        original = np.asarray(value)
        if original.dtype.kind == "b":
            raise ValueError("booleans are not numerical inputs")
        with self.context():
            flat = [self.real(item) for item in original.flat]
        return np.asarray(flat, dtype=self.dtype).reshape(original.shape)

    def zeros(self, shape):
        return np.full(shape, self.real(0), dtype=self.dtype)

    def eye(self, dimension):
        result = self.zeros((dimension, dimension))
        np.fill_diagonal(result, self.real(1))
        return result

    def finite(self, value):
        if self.digits is None:
            return bool(np.all(np.isfinite(value)))
        return all((x.is_finite() if isinstance(x, (Decimal, Fixed)) else math.isfinite(x)) for x in np.asarray(value).flat)

    def _map(self, value, float_function, decimal_function):
        a = np.asarray(value)
        if self.digits is None:
            return float_function(a)
        with self.context():
            out = [decimal_function(self.real(x)) for x in a.flat]
        return np.asarray(out, dtype=object).reshape(a.shape)

    def sqrt(self, value):
        return self._map(value, np.sqrt, lambda x: x.sqrt())

    def tanh(self, value):
        def gate(x):
            e = (-2 * abs(x)).exp()
            h = (1 - e) / (1 + e)
            return -h if x < 0 else h
        return self._map(value, np.tanh, gate)

    def pi(self):
        if self.digits is None:
            return math.pi
        if self.backend == "rational":
            return Fixed(rational_pi(self.digits), self.digits)
        with localcontext() as ctx:
            ctx.prec = self.digits + 10
            threshold = Decimal(10) ** (-ctx.prec)
            def atan_inverse(n):
                x = Decimal(1) / n
                power, total, k = x, x, 1
                while True:
                    power *= -x*x
                    term = power / (2*k+1)
                    total += term
                    if abs(term) < threshold:
                        return total
                    k += 1
            result = 16*atan_inverse(5) - 4*atan_inverse(239)
        with self.context():
            return +result

    def trig(self, value, cosine=False):
        if self.digits is None:
            return (np.cos if cosine else np.sin)(value)
        if self.backend == "rational":
            return self._map(value, np.cos if cosine else np.sin, lambda x: x.trig(cosine))
        pi = self.pi()
        def evaluate(x):
            with localcontext() as ctx:
                ctx.prec = self.digits + 10
                # The extra digits protect a fixed input; no uniform claim
                # over input magnitudes is made at any chosen precision.
                x = x % (2*pi)
                if x > pi:
                    x -= 2*pi
                if x < -pi:
                    x += 2*pi
                term = Decimal(1) if cosine else x
                total, k = term, 0
                threshold = Decimal(10) ** (-ctx.prec)
                while True:
                    a = 2*k+1 if cosine else 2*k+2
                    term *= -x*x / (a*(a+1))
                    total += term
                    if abs(term) < threshold:
                        break
                    k += 1
            return +total
        return self._map(value, np.cos if cosine else np.sin, evaluate)

    def cholesky(self, matrix):
        matrix = np.asarray(matrix)
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or not self.finite(matrix):
            raise ValueError("Cholesky needs a finite square matrix")
        if self.digits is None:
            try:
                return np.linalg.cholesky((matrix + matrix.T)/2)
            except np.linalg.LinAlgError as exc:
                raise ValueError("positive covariance pivot unresolved; increase precision or refinement parameters") from exc
        with self.context():
            n = len(matrix)
            lower = self.zeros(matrix.shape)
            for i in range(n):
                for j in range(i+1):
                    s = (matrix[i, j]+matrix[j, i])/2
                    for k in range(j):
                        s -= lower[i, k]*lower[j, k]
                    if i == j:
                        if s <= 0:
                            raise ValueError("positive covariance pivot unresolved; increase decimal precision")
                        lower[i, j] = s.sqrt()
                    else:
                        lower[i, j] = s/lower[j, j]
            return lower

    def inverse_lower(self, lower):
        lower = np.asarray(lower)
        n = len(lower)
        if self.digits is None:
            return np.linalg.solve(lower, np.eye(n))
        with self.context():
            result = self.zeros((n, n))
            for column in range(n):
                for row in range(column, n):
                    s = self.real(int(row == column))
                    for k in range(column, row):
                        s -= lower[row, k]*result[k, column]
                    result[row, column] = s/lower[row, row]
            return result


def primes(count):
    result, candidate = [], 2
    while len(result) < count:
        if all(candidate % p for p in result if p*p <= candidate):
            result.append(candidate)
        candidate += 1
    return result


def radical_inverse(index, base):
    """Exact numerator/denominator, with index >= 1 and base >= 2."""
    numerator, denominator = 0, 1
    while index:
        index, digit = divmod(index, base)
        numerator = numerator*base + digit
        denominator *= base
    return numerator, denominator


def gaussian_points(count, dimension, arithmetic):
    """First count Halton points transformed jointly by Box–Muller.

    Points are deterministic integration nodes, never neuron coordinates.
    Prefix coordinates agree when the requested Gaussian dimension grows.
    """
    if any(isinstance(n, bool) or not isinstance(n, int) for n in (count, dimension)) or count < 1 or dimension < 0:
        raise ValueError("count must be positive and dimension nonnegative integers")
    ar = arithmetic
    if dimension == 0:
        return ar.zeros((count, 0))
    uniforms = ar.zeros((count, 2*((dimension+1)//2)))
    with ar.context():
        for j, base in enumerate(primes(uniforms.shape[1])):
            for k in range(count):
                numerator, denominator = radical_inverse(k+1, base)
                uniforms[k, j] = ar.real(numerator)/ar.real(denominator)
        if ar.digits is None:
            radii = np.sqrt(-2*np.log(uniforms[:, ::2]))
        else:
            radii = np.asarray([(-2*x.ln()).sqrt() for x in uniforms[:, ::2].flat], dtype=object).reshape(count, -1)
        angles = 2*ar.pi()*uniforms[:, 1::2]
        output = ar.zeros(uniforms.shape)
        output[:, ::2] = radii*ar.trig(angles, cosine=True)
        output[:, 1::2] = radii*ar.trig(angles)
    return output[:, :dimension].copy()
