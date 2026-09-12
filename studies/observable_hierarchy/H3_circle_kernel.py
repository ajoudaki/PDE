#!/usr/bin/env python3
"""Certified initialized Hermite kernel on the whole input circle.

No trajectory is integrated. Coefficients use one-dimensional interval Simpson
quadrature. Prediction takes the existing current readout coefficient interval.
See H3_circle_kernel_proof.md for the fixed reference-law scope and error floor.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import ROUND_CEILING, getcontext
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import time

import H3_shorttime_solver as primitive

I, D = primitive.I, primitive.D
NORMALIZER, rational = primitive.NORMALIZER, primitive.rational
DEGREE, PANELS, RADIUS = 7, 8192, 8
HORIZON = F(1, 200)
MAX_B_RADIUS = F(1, 10**8)
MAX_COORDINATE_RADII_SUM = F(1, 10**6)
ANALYTIC_ENVELOPE = F(2417, 10**9)
TARGET_ERROR = F(1, 100000)
CONVERSION_BUDGET = F(1, 10**40)


def hermite_polynomials(degree=DEGREE):
    """Probabilists' Hermite polynomials as ascending integer coefficients."""
    if type(degree) is not int or degree < 0:
        raise ValueError("nonnegative integer degree required")
    polys = [[1]]
    if degree:
        polys.append([0, 1])
    for n in range(1, degree):
        next_poly = [0] + polys[n]
        for k, value in enumerate(polys[n-1]):
            next_poly[k] -= n * value
        polys.append(next_poly)
    return polys


def derivative_polynomial(poly, tanh_power=1):
    """Fourth x derivative of P(x)tanh(sigma*x)^j times normal density."""
    terms = {(i, tanh_power, 0): a for i, a in enumerate(poly) if a}
    for _ in range(4):
        out = defaultdict(int)
        for (i, j, k), a in terms.items():
            if i:
                out[i-1, j, k] += i*a
            if j:
                out[i, j-1, k+1] += j*a
                out[i, j+1, k+1] -= j*a
            out[i+1, j, k] -= a
        terms = {key: a for key, a in out.items() if a}
    return terms


def gaussian_monomial_bounds(degree):
    """Certified integer bounds for sup_x |x|^j normal_density(x)."""
    bounds = []
    for j in range(degree+1):
        maximum = NORMALIZER if j == 0 else (
            I(j).sqrt()**j * (-I(j)/2).exp() * NORMALIZER)
        bounds.append(int(maximum.hi.to_integral_value(rounding=ROUND_CEILING)))
    return bounds


def derivative_bounds(degree=DEGREE):
    polys = hermite_polynomials(degree)
    envelope = gaussian_monomial_bounds(degree+4)
    bounds = {n: sum(abs(a)*envelope[i]
                     for (i, j, k), a in derivative_polynomial(polys[n]).items())
              for n in range(1, degree+1, 2)}
    bounds[0] = sum(abs(a)*envelope[i]
                    for (i, j, k), a in derivative_polynomial([1], 2).items())
    return bounds, envelope


def gaussian_tail_moments(radius, degree):
    """Upper intervals for E[|G|^j 1_{|G|>radius}], j<=degree."""
    radius = I.coerce(radius)
    if radius.lo <= 0:
        raise ValueError("positive radius required")
    density = (-(radius**2)/2).exp()*NORMALIZER
    tail = [2*density/radius]
    if degree:
        tail.append(2*density)
    for j in range(2, degree+1):
        tail.append(2*(radius**(j-1))*density+(j-1)*tail[j-2])
    return tail


def configuration_certificate(degree=DEGREE, panels=PANELS, radius=RADIUS):
    """Static bounds; run before evaluating any initialized integral."""
    if degree != DEGREE or panels != PANELS or radius != RADIUS:
        raise ValueError("this bounded preflight fixes degree7/panels8192/radius8")
    bounds, monomials = derivative_bounds(degree)
    polys = hermite_polynomials(degree)
    tails = gaussian_tail_moments(I(radius), degree)
    errors = {}
    for n, bound in bounds.items():
        truncation = I(radius)**5 * bound / (90*panels**4)
        tail = tails[0] if n == 0 else sum(
            (abs(a)*tails[j] for j, a in enumerate(polys[n]) if a), I(0))
        errors[str(n)] = dict(fourth_derivative=bound,
                             simpson=truncation.record(), tail=tail.record())
    return dict(degree=degree, panels=panels, radius=radius,
                precision_digits=getcontext().prec,
                gaussian_monomial_envelopes=monomials, errors=errors,
                criterion="whole-circle numerical error plus 2.417e-6 <=1e-5",
                max_readout_interval_radius=str(MAX_B_RADIUS),
                max_coordinate_radii_sum=str(MAX_COORDINATE_RADII_SUM),
                resource_limit="60 core seconds, one core, 8 GiB; no trajectory")


def coefficient_integrals(sigma, configuration):
    """Enclose variance and odd raw Hermite coefficients at fixed sigma."""
    sigma = I.coerce(sigma)
    if sigma.lo < 0 or sigma.hi > 1:
        raise ValueError("sigma interval must lie in [0,1]")
    degree, panels, radius = (configuration[k] for k in ('degree', 'panels', 'radius'))
    if (degree, panels, radius) != (DEGREE, PANELS, RADIUS):
        raise ValueError("configuration differs from frozen bounded preflight")
    sums = {n: I(0) for n in [0, *range(1, degree+1, 2)]}
    step = I(radius)/panels
    for j in range(panels+1):
        x = step*j
        h = (sigma*x).tanh()
        density = (-(x**2)/2).exp()*NORMALIZER
        weight = 1 if j in (0, panels) else (4 if j % 2 else 2)
        multiplier = density*weight
        sums[0] = sums[0]+h*h*multiplier
        old, current = I(1), x
        for n in range(1, degree+1):
            if n % 2:
                sums[n] = sums[n]+h*current*multiplier
            old, current = current, x*current-n*old
    result = {}
    for n, total in sums.items():
        simpson = 2*step*total/3
        err = configuration['errors'][str(n)]
        truncation, tail = (I(**err[k]) for k in ('simpson', 'tail'))
        interval = simpson.widen(truncation)
        if n == 0:
            interval = I(max(D(0), interval.lo), (interval.hi+tail.hi).next_plus())
        else:
            interval = interval.widen(tail)
        result[n] = interval
    return result


def midpoint_radius(interval):
    lo, hi = F(interval.lo), F(interval.hi)
    return (lo+hi)/2, (hi-lo)/2


def interval_record_map(values):
    return {str(n): value.record() for n, value in values.items()}


class CircleKernel:
    """Fixed initialized kernel certificate; evaluation retains no history."""

    def __init__(self, q, v, alpha, beta):
        self.q, self.v = q, v
        self.alpha, self.beta = dict(alpha), dict(beta)
        expected = set(range(1, DEGREE+1, 2))
        if set(self.alpha) != expected or set(self.beta) != expected:
            raise ValueError("all four odd coefficients through degree7 required")
        if q.lo <= 0 or q.hi > 1 or v.lo < 0 or v.hi > 1:
            raise ValueError("invalid initialized variances")
        if any(value.lo < 0 for value in [*alpha.values(), *beta.values()]):
            raise ValueError("coefficient intervals must be nonnegative")
        self.alpha_mid = {n: midpoint_radius(value)[0] for n, value in alpha.items()}
        self.beta_mid = {n: midpoint_radius(value)[0] for n, value in beta.items()}
        self.q_mid, eq = midpoint_radius(q)
        ea = sum(midpoint_radius(value)[1] for value in alpha.values())
        eb = sum(midpoint_radius(value)[1] for value in beta.values())
        self.alpha_tail = max(F(0), F(q.hi)-sum(F(value.lo) for value in alpha.values()))
        self.beta_tail = max(F(0), F(v.hi)-sum(F(value.lo) for value in beta.values()))
        if sum(F(value.lo) for value in alpha.values()) > F(q.hi):
            raise ValueError("alpha intervals contradict Parseval")
        if sum(F(value.lo) for value in beta.values()) > F(v.hi):
            raise ValueError("beta intervals contradict Parseval")
        # Bessel bounds the true outer polynomial's slope on [-1,1] by q.
        self.parameter_error = F(q.hi)*(ea/F(q.lo)
            +sum(self.alpha_mid.values())*eq/(F(q.lo)*self.q_mid))+eb
        self.kernel_error = self.alpha_tail+self.beta_tail+self.parameter_error
        self.midpoint_lipschitz = (sum(n*a for n,a in self.alpha_mid.items())/self.q_mid
                                  *sum(n*a for n,a in self.beta_mid.items()))

    def midpoint_kernel(self, rho):
        """Exact rational midpoint model; rho is a supplied exact correlation."""
        if not isinstance(rho, (F, int)) or isinstance(rho, bool):
            raise TypeError("use an exact Fraction or integer correlation")
        rho = F(rho)
        if abs(rho) > 1:
            raise ValueError("correlation outside [-1,1]")
        inner = sum(a*rho**n for n, a in self.alpha_mid.items())/self.q_mid
        inner = min(F(1), max(F(-1), inner))
        return sum(a*inner**n for n, a in self.beta_mid.items())

    def kernel_enclosure(self, rho):
        return rational(self.midpoint_kernel(rho)).widen(rational(self.kernel_error))

    def uniform_prediction_error(self, readout_radius=MAX_B_RADIUS,
                                 coordinate_radii_sum=MAX_COORDINATE_RADII_SUM):
        readout_radius = F(readout_radius)
        coordinate_radii_sum = F(coordinate_radii_sum)
        if min(readout_radius, coordinate_radii_sum) < 0:
            raise ValueError("nonnegative radii required")
        return (2*HORIZON*self.kernel_error+2*F(self.v.hi)*readout_radius
                +HORIZON*self.midpoint_lipschitz*coordinate_radii_sum+CONVERSION_BUDGET)

    def prediction(self, b, u1, u2):
        """Enclose fF for exact rational unit u and supplied current b interval.

        The interval must already enclose the same reference readout state.
        This API does not establish that premise or integrate its evolution.
        Returned arithmetic widening is included in the interval itself.
        """
        if getcontext().prec < 60:
            raise ValueError("prediction certificate requires at least 60 Decimal digits")
        if any(not isinstance(u, (F, int)) or isinstance(u, bool) for u in (u1,u2)):
            raise TypeError("unit coordinates must be exact Fractions or integers")
        u1, u2 = F(u1), F(u2)
        if u1*u1+u2*u2 != 1:
            raise ValueError("coordinates must form an exact unit vector")
        b = I.coerce(b)
        # Exact zero-initial reference dynamics satisfy 0<=b<=T.
        b = I(max(D(0), b.lo), min(D('0.005'), b.hi))
        mid, radius = midpoint_radius(b)
        if radius > MAX_B_RADIUS:
            raise ValueError("readout interval exceeds the declared numerical error budget")
        value = mid*(self.midpoint_kernel(u1)-self.midpoint_kernel(u2))
        error = 2*abs(mid)*self.kernel_error+2*F(self.v.hi)*radius
        return rational(value).widen(rational(error))

    def prediction_box(self, b, u1, u2):
        """Enclose fF for every true unit direction in the supplied interval box.

        This is an effective-input interface: the caller supplies enclosures of
        its actual unit vector, with no sine/cosine computation inside this API.
        A box that cannot intersect the unit circle is rejected. The current b
        interval has the same independently certified premise as prediction().
        """
        if getcontext().prec < 60:
            raise ValueError("prediction certificate requires at least 60 Decimal digits")
        coords = [I.coerce(u) for u in (u1,u2)]
        coords = [I(max(D(-1),u.lo),min(D(1),u.hi)) for u in coords]
        low_norm = sum((F(0) if u.lo <= 0 <= u.hi else min(F(u.lo)**2,F(u.hi)**2))
                       for u in coords)
        high_norm = sum(max(F(u.lo)**2,F(u.hi)**2) for u in coords)
        if not low_norm <= 1 <= high_norm:
            raise ValueError("coordinate box does not intersect the unit circle")
        coord_mid_radius = [midpoint_radius(u) for u in coords]
        input_radius = sum(pair[1] for pair in coord_mid_radius)
        if input_radius > MAX_COORDINATE_RADII_SUM:
            raise ValueError("coordinate box exceeds the declared input error budget")
        b = I.coerce(b)
        b = I(max(D(0),b.lo),min(D('0.005'),b.hi))
        mid, radius = midpoint_radius(b)
        if radius > MAX_B_RADIUS:
            raise ValueError("readout interval exceeds the declared numerical error budget")
        value = mid*(self.midpoint_kernel(coord_mid_radius[0][0])
                     -self.midpoint_kernel(coord_mid_radius[1][0]))
        error = (2*abs(mid)*self.kernel_error+2*F(self.v.hi)*radius
                 +abs(mid)*self.midpoint_lipschitz*input_radius)
        return rational(value).widen(rational(error))

    def record(self):
        return dict(format='H3-circle-Hermite-v1', degree=DEGREE,
                    q=self.q.record(), v=self.v.record(),
                    alpha=interval_record_map(self.alpha), beta=interval_record_map(self.beta),
                    alpha_tail=str(self.alpha_tail), beta_tail=str(self.beta_tail),
                    parameter_error=str(self.parameter_error), kernel_error=str(self.kernel_error))

    @classmethod
    def from_record(cls, record):
        if record.get('format') != 'H3-circle-Hermite-v1' or record.get('degree') != DEGREE:
            raise ValueError("unsupported kernel certificate")
        return cls(I(**record['q']), I(**record['v']),
                   {int(n):I(**v) for n,v in record['alpha'].items()},
                   {int(n):I(**v) for n,v in record['beta'].items()})


def initialize(configuration):
    lower = coefficient_integrals(I(1), configuration)
    q = lower[0]
    upper = coefficient_integrals(q.sqrt(), configuration)
    alpha = {n:(lower[n]**2/math.factorial(n)).nonnegative() for n in lower if n}
    beta = {n:(upper[n]**2/math.factorial(n)).nonnegative() for n in upper if n}
    return CircleKernel(q, upper[0], alpha, beta), lower, upper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, help='fresh output directory')
    args = parser.parse_args()
    destination = Path(args.output)
    destination.mkdir(parents=True, exist_ok=False)
    configuration = configuration_certificate()
    (destination/'configuration.json').write_text(json.dumps(configuration, indent=2)+'\n')
    started = time.perf_counter()
    kernel, lower, upper = initialize(configuration)
    numerical = kernel.uniform_prediction_error()
    total = numerical+ANALYTIC_ENVELOPE
    assert numerical < TARGET_ERROR-ANALYTIC_ENVELOPE
    assert total < TARGET_ERROR
    result = dict(status='whole-circle initialized-kernel numerical certificate PASS',
                  scope='reference law only; no trajectory; analytic GF envelope is an explicit external component',
                  kernel=kernel.record(), raw_lower=interval_record_map(lower), raw_upper=interval_record_map(upper),
                  numerical_error=str(numerical), numerical_error_display=float(numerical),
                  analytic_envelope=str(ANALYTIC_ENVELOPE), total_error=str(total), total_error_display=float(total),
                  uniform_time_interval=['0','0.005'], max_b_radius=str(MAX_B_RADIUS),
                  max_coordinate_radii_sum=str(MAX_COORDINATE_RADII_SUM),
                  radius_of_decimal_conversion='returned interval operations include outward conversion',
                  elapsed_seconds=time.perf_counter()-started,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  python=platform.python_version(), platform=platform.platform(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  primitive_sha256=hashlib.sha256(Path(primitive.__file__).read_bytes()).hexdigest())
    (destination/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','numerical_error_display','total_error_display',
                                                'elapsed_seconds','peak_rss_kib')}, indent=2))


if __name__ == '__main__':
    main()
