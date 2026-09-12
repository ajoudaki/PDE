#!/usr/bin/env python3
"""Study-only interval certificate for the preregistered reference law.

No canonical GF or neural training is simulated. --preflight evaluates only
quadrature bounds and a small elementary-function timing probe. --run evaluates
initialized Gaussian moments and the six-state Duhamel candidate. See the
associated numerical note for the mathematical scope and missing C-H3 bridges.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import resource
import time

getcontext().prec = 60
D = Decimal


class I:
    """Closed interval; every rounded elementary result is widened by one ulp."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, D) else D(str(lo))
        self.hi = self.lo if hi is None else (hi if isinstance(hi, D) else D(str(hi)))
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def coerce(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = self.coerce(other)
        return I((self.lo + other.lo).next_minus(), (self.hi + other.hi).next_plus())

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        values = [self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi]
        return I(min(values).next_minus(), max(values).next_plus())

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("interval contains zero")
        values = [self.lo / other.lo, self.lo / other.hi,
                  self.hi / other.lo, self.hi / other.hi]
        return I(min(values).next_minus(), max(values).next_plus())

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("only nonnegative integer interval powers")
        if n == 0:
            return I(1)
        # Use only correctly-rounded multiplications, not the Decimal general
        # transcendental power operation.
        answers = []
        for endpoint in (self.lo, self.hi):
            value = I(1)
            for _ in range(n):
                value = value * I(endpoint)
            answers.append(value)
        lo = min(value.lo for value in answers)
        hi = max(value.hi for value in answers)
        if n % 2 == 0 and self.lo <= 0 <= self.hi:
            lo = D(0)
        return I(lo, hi)

    def exp(self):
        # Decimal exp is correctly rounded; explicit widening encloses it.
        return I(self.lo.exp().next_minus(), self.hi.exp().next_plus())

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("negative square-root lower endpoint")
        return I(max(D(0), self.lo.sqrt().next_minus()), self.hi.sqrt().next_plus())

    def tanh(self):
        # Evaluate the monotone scalar map at each endpoint separately.
        answers = []
        for endpoint in (self.lo, self.hi):
            e = (I(2) * I(endpoint)).exp()
            answers.append((e - 1) / (e + 1))
        return I(answers[0].lo, answers[1].hi)

    def widen(self, radius):
        radius = self.coerce(radius)
        return I((self.lo - radius.hi).next_minus(),
                 (self.hi + radius.hi).next_plus())

    def nonnegative(self):
        if self.hi < 0:
            raise ValueError("negative enclosure of nonnegative quantity")
        return I(max(D(0), self.lo), self.hi)

    def record(self):
        return {"lo": str(self.lo), "hi": str(self.hi)}


def rational(x: Fraction) -> I:
    return I(x.numerator) / I(x.denominator)


def atan_reciprocal(n: int, terms: int = 64) -> I:
    s = sum((Fraction((-1) ** k, (2 * k + 1) * n ** (2 * k + 1))
             for k in range(terms)), Fraction(0))
    remainder = Fraction(1, (2 * terms + 1) * n ** (2 * terms + 1))
    return rational(s).widen(rational(remainder))


PI = 16 * atan_reciprocal(5) - 4 * atan_reciprocal(239)
NORMALIZER = 1 / (2 * PI).sqrt()


# name -> (power of z, polynomial in tanh(z)); all integrands are even and >=0.
POLYS = {
    "h2": (0, {2: 1}),
    "h4": (0, {4: 1}),
    "h6": (0, {6: 1}),
    "s2": (0, {0: 1, 2: -2, 4: 1}),
    "s3": (0, {0: 1, 2: -3, 4: 3, 6: -1}),
    "s4": (0, {0: 1, 2: -4, 4: 6, 6: -4, 8: 1}),
    "h2s2": (0, {2: 1, 4: -2, 6: 1}),
    "h2s4": (0, {2: 1, 4: -4, 6: 6, 8: -4, 10: 1}),
    "zh": (1, {1: 1}),
    "zhs3": (1, {1: 1, 3: -3, 5: 3, 7: -1}),
    "z2s2": (2, {0: 1, 2: -2, 4: 1}),
}


def fourth_derivative_bound(name: str) -> int:
    """Bound sup |(z^a P(tanh z) rho(x))''''| for z=sigma*x, 0<=sigma<=1."""
    a, poly = POLYS[name]
    terms = {(a, j, a): value for j, value in poly.items()}
    # D[Q rho] = (Q_x + sigma(1-h^2) Q_h - x Q) rho.
    for _ in range(4):
        result = defaultdict(int)
        for (i, j, k), value in terms.items():
            if i:
                result[i - 1, j, k] += i * value
            if j:
                result[i, j - 1, k + 1] += j * value
                result[i, j + 1, k + 1] -= j * value
            result[i + 1, j, k] -= value
        terms = {key: value for key, value in result.items() if value}
    # Verified in preflight from max |x|^j rho(x) at sqrt(j).
    gaussian_bounds = (1, 1, 1, 1, 1, 2, 5)
    return sum(abs(value) * gaussian_bounds[i] for (i, j, k), value in terms.items())


def scalar_integrands(z: I):
    h = z.tanh()
    h2 = h ** 2
    s = 1 - h2
    s2, s3, s4 = s ** 2, s ** 3, s ** 4
    return {
        "h2": h2, "h4": h2 ** 2, "h6": h2 ** 3,
        "s2": s2, "s3": s3, "s4": s4,
        "h2s2": h2 * s2, "h2s4": h2 * s4,
        "zh": z * h, "zhs3": z * h * s3, "z2s2": z ** 2 * s2,
    }


def tail_bound(power: int, radius: I) -> I:
    phi = (-(radius ** 2) / 2).exp() * NORMALIZER
    if power == 0:
        return 2 * phi / radius
    if power == 1:
        return 2 * phi
    if power == 2:
        return 2 * phi * (radius + 1 / radius)
    raise ValueError(power)


def gaussian_moments(sigma: I, panels: int = 8192, radius: int = 8):
    if panels <= 0 or panels % 2:
        raise ValueError("Simpson subdivision count must be positive and even")
    if sigma.lo < 0 or sigma.hi > 1:
        raise ValueError("moment bound requires sigma in [0,1]")
    sums = {name: I(0) for name in POLYS}
    radius_i, step = I(radius), I(radius) / panels
    started = time.perf_counter()
    for j in range(panels + 1):
        # Multiplication by step is interval arithmetic, never an untracked float.
        x = step * j
        z = sigma * x
        density = (-(x ** 2) / 2).exp() * NORMALIZER
        weight = 1 if j in (0, panels) else (4 if j % 2 else 2)
        for name, value in scalar_integrands(z).items():
            sums[name] = sums[name] + value * density * weight
    result, error = {}, {}
    for name, value in sums.items():
        simpson = 2 * step * value / 3
        derivative = fourth_derivative_bound(name)
        truncation = radius_i ** 5 * derivative / (90 * panels ** 4)
        gaussian_tail = tail_bound(POLYS[name][0], radius_i)
        enclosure = simpson.widen(truncation)
        # Nonnegative integrands: the omitted Gaussian tails add [0, tail].
        result[name] = I(max(D(0), enclosure.lo),
                         (enclosure.hi + gaussian_tail.hi).next_plus())
        error[name] = {"simpson": truncation.record(), "tail": gaussian_tail.record()}
    return result, {"seconds": time.perf_counter() - started,
                    "subdivisions": panels, "radius": radius, "errors": error}


def sharpened_bounds(t: I):
    """Formula bounds on [0,.005], including two elementary energy bootstraps."""
    T = I("0.005")
    ell = 4 / (3 * I(3).sqrt())
    sigma = I("0.52").sqrt()
    kappa = sigma + (10 + 4 * T ** 2) * T ** 2
    a = 4 * kappa + 2 * kappa ** 2 * T ** 2
    z = 2 * a + 2 * kappa
    c = I(2) / 3 * (1 + 2 * T) * z * (2 * T).exp()
    shift, R = 1 + ell * sigma, I(8)
    cutoff = (R - shift) / sigma
    density = (-(cutoff ** 2) / 2).exp() * NORMALIZER
    # Mills' upper bound safely replaces the Gaussian upper-tail probability.
    tau = (2 * ((sigma ** 2 * cutoff + 2 * sigma * shift) * density
                + (sigma ** 2 + shift ** 2) * density / cutoff)).sqrt()
    cw = ((4 + 8 * sigma * T) * c + (8 * ell + 16 * sigma * T) * z
          + 8 * kappa ** 2 + 4 * ell * R * a)
    ck = (2 + 4 * sigma * T) * c + (4 * ell + 8 * sigma * T) * z + 4 * kappa * a
    ew = cw * t ** 4 / 4 + 2 * tau * t ** 2
    ek = ck * t ** 4 / 4
    root3fourth = I(3).sqrt().sqrt()
    d = 2 * (root3fourth * sigma + shift)
    ez = 2 * ew + ell * d ** 2 * t ** 4 + ek + 2 * kappa * a * t ** 4
    # Prediction below uses the cheaper frozen kernel observation, with its own
    # explicit error to the nonlinear target. Hidden motion remains nonzero.
    frozen_prediction_error = (c + 2 * z) * t ** 3
    return {"row": ew, "middle": ek, "upper": ez,
            "frozen_prediction": frozen_prediction_error, "ell": ell}


def reference_coefficients(g, upper):
    q, k = g["h2"], upper["h2"]
    m, n = g["s2"], g["h2s2"]
    alpha = 1 - 4 * k + 3 * upper["h4"]
    gamma = (1 - k) ** 2
    v = upper["h2s2"] + k * upper["s2"]
    n1sq = g["s4"] * (v + gamma ** 2 * q) + alpha ** 2 * g["h2s4"]
    A, B, C = alpha * n / q, -gamma * m, q + m
    n2sq = (n1sq * upper["s2"]
            + A ** 2 * (upper["z2s2"] - q * upper["s2"])
            + 2 * C * (A * upper["zhs3"] - B * upper["s3"] * upper["zh"])
            + C ** 2 * (upper["h2s4"] + k * upper["s4"]))
    return {"q": q, "k": k, "alpha": alpha, "gamma": gamma,
            "v": v, "n1sq": n1sq, "n2sq": n2sq}


def clock_free_step(b: I, beta: I, k: I, duration: I):
    decay = (-k * duration).exp()
    b_next = decay * b + (1 - decay) / k
    beta_next = beta + (b_next ** 2 - b ** 2) / 2
    return b_next, beta_next


def checkpoint_encode(elapsed: Fraction, b: I, beta: I, coeff: dict) -> dict:
    """Save numerical state and the cumulative analytical certificate origin.

    The exact rational elapsed time is certificate bookkeeping, not an input
    to the autonomous b,beta vector field. The prior interval endpoints are
    serialized as decimal strings without rounding or loss of precision.
    """
    if elapsed < 0 or elapsed > FROZEN_HORIZON:
        raise ValueError("checkpoint time outside the frozen horizon")
    return {
        "format": "H3_shorttime_reference_checkpoint_v1",
        "state": {"b": b.record(), "beta": beta.record()},
        "coefficients": {key: value.record() for key, value in coeff.items()},
        "certificate": {
            "elapsed_time": {"numerator": elapsed.numerator, "denominator": elapsed.denominator},
            "horizon": {"numerator": 1, "denominator": 200},
            "analytical_origin": "original canonical initialization at t=0",
            "analytical_envelope": "sharpened_bounds plus reference_observations spatial remainder",
            "prior_arithmetic_error": "included in every preserved interval endpoint",
            "precision_digits": getcontext().prec,
        },
    }


FROZEN_HORIZON = Fraction(1, 200)
REQUIRED_COEFFICIENTS = {"q", "k", "alpha", "gamma", "v", "n1sq", "n2sq"}


def checkpoint_decode(payload: dict):
    if not isinstance(payload, dict) or payload.get("format") != "H3_shorttime_reference_checkpoint_v1":
        raise ValueError("unsupported checkpoint format")
    try:
        certificate = payload["certificate"]
        time_record = certificate["elapsed_time"]
        if (type(time_record["numerator"]) is not int
                or type(time_record["denominator"]) is not int
                or time_record["denominator"] <= 0):
            raise ValueError("invalid exact checkpoint time")
        elapsed = Fraction(time_record["numerator"], time_record["denominator"])
        if not 0 <= elapsed <= FROZEN_HORIZON:
            raise ValueError("checkpoint time outside the frozen horizon")
        if (certificate["horizon"] != {"numerator": 1, "denominator": 200}
                or certificate["analytical_origin"] != "original canonical initialization at t=0"
                or certificate["precision_digits"] != getcontext().prec):
            raise ValueError("checkpoint certificate contract mismatch")
        def read_interval(record):
            if not isinstance(record, dict) or set(record) != {"lo", "hi"}:
                raise ValueError("invalid interval encoding")
            if not isinstance(record["lo"], str) or not isinstance(record["hi"], str):
                raise ValueError("interval endpoints must be exact decimal strings")
            lo, hi = D(record["lo"]), D(record["hi"])
            if not lo.is_finite() or not hi.is_finite() or lo > hi:
                raise ValueError("nonfinite or reversed checkpoint interval")
            return I(lo, hi)
        if set(payload["coefficients"]) != REQUIRED_COEFFICIENTS:
            raise ValueError("checkpoint coefficient list mismatch")
        b = read_interval(payload["state"]["b"])
        beta = read_interval(payload["state"]["beta"])
        coeff = {key: read_interval(value) for key, value in payload["coefficients"].items()}
        if any(coeff[key].lo <= 0 for key in ("q", "k", "n1sq", "n2sq")):
            raise ValueError("checkpoint positivity gate failed")
        return elapsed, b, beta, coeff
    except (KeyError, TypeError, ArithmeticError) as error:
        raise ValueError("invalid checkpoint") from error


def save_checkpoint(path: Path, elapsed: Fraction, b: I, beta: I, coeff: dict):
    payload = checkpoint_encode(elapsed, b, beta, coeff)
    # Validate before writing, including precision and finite endpoints.
    checkpoint_decode(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as output:
        json.dump(payload, output, indent=2)
        output.write("\n")


def load_checkpoint(path: Path):
    return checkpoint_decode(json.loads(path.read_text()))


def advance_checkpoint(saved, duration: Fraction):
    elapsed, b, beta, coeff = saved
    if duration < 0 or elapsed + duration > FROZEN_HORIZON:
        raise ValueError("continuation exceeds the certified horizon")
    b_new, beta_new = clock_free_step(b, beta, coeff["k"], rational(duration))
    return elapsed + duration, b_new, beta_new, coeff


def reference_observations(coeff, b: I, beta: I, t: I):
    bounds = sharpened_bounds(t)
    ell = bounds["ell"]
    # Universal initialized L4 bounds for U=(H1-H2)s1 and P=A0*U.
    u2 = I("1.04").sqrt()
    root3fourth = I(3).sqrt().sqrt()
    p4 = root3fourth * u2 + 2
    # R=qU + A0(l^2 P): forward noise norm <= 2 ||U||2 and response <=2.
    r4 = I("1.04") + 2 * root3fourth * u2 + 2
    first_spatial = ell * beta ** 2 * p4 ** 2 / 2
    upper_spatial = ell * beta ** 2 * r4 ** 2 / 2
    lower_estimate = beta * coeff["n1sq"].nonnegative().sqrt()
    upper_estimate = beta * coeff["n2sq"].nonnegative().sqrt()
    lower_error = bounds["row"] + first_spatial
    upper_error = bounds["upper"] + upper_spatial
    first_certificate = lower_estimate.widen(lower_error).nonnegative()
    upper_certificate = upper_estimate.widen(upper_error).nonnegative()
    f_at_e1 = b * coeff["k"]
    prediction_certificate = f_at_e1.widen(bounds["frozen_prediction"])
    return {
        "time": t.record(), "b": b.record(), "beta_diagonal": beta.record(),
        "first_rms_estimate": lower_estimate.record(),
        "upper_rms_estimate": upper_estimate.record(),
        "first_rms_true_enclosure": first_certificate.record(),
        "upper_rms_true_enclosure": upper_certificate.record(),
        "first_rms_analytic_error": lower_error.record(),
        "upper_rms_analytic_error": upper_error.record(),
        "prediction_e1_estimate": f_at_e1.record(),
        "prediction_e1_true_enclosure": prediction_certificate.record(),
        "whole_circle_prediction_error": bounds["frozen_prediction"].record(),
        "whole_circle_signal_lower": str(max(D(0), prediction_certificate.lo)),
        # Uniform |c|<=2t, |H|<=1 gives this true whole-circle upper endpoint.
        "whole_circle_signal_upper": str((2 * t).hi),
    }


def preflight(panels: int):
    started = time.perf_counter()
    norm_checks = []
    for j, bound in enumerate((1, 1, 1, 1, 1, 2, 5)):
        if j == 0:
            maximum = NORMALIZER
        else:
            maximum = I(j).sqrt() ** j * (-I(j) / 2).exp() * NORMALIZER
        if maximum.hi >= bound:
            raise AssertionError("invalid derivative-envelope table")
        norm_checks.append(maximum.record())
    # The universal .52 variance bound follows from E min(G^2,1)=1-2phi(1).
    phi1 = (-I(1) / 2).exp() * NORMALIZER
    if (1 - 2 * phi1).hi >= D("0.52"):
        raise AssertionError("initial variance bound failed")
    # Timing probe is initialization arithmetic only, not a trained trajectory.
    probe_started = time.perf_counter()
    for j in range(128):
        scalar_integrands(I(j) / 32)
    probe_seconds = time.perf_counter() - probe_started
    error = {name: (I(8) ** 5 * fourth_derivative_bound(name)
                    / (90 * panels ** 4)).record() for name in POLYS}
    bounds = sharpened_bounds(I("0.005"))
    return {"mode": "preflight", "panels": panels, "precision_digits": 60,
            "pi_enclosure": PI.record(), "gaussian_envelope_checks": norm_checks,
            "quadrature_bounds": error,
            "analytic_bounds_at_T": {key: value.record() for key, value in bounds.items()},
            "timing_probe_seconds": probe_seconds,
            "conservative_runtime_estimate_seconds": probe_seconds * 2 * (panels + 1) / 128 * 8,
            "seconds": time.perf_counter() - started}


def run(panels: int, checkpoint_path: Path):
    started = time.perf_counter()
    g, gmeta = gaussian_moments(I(1), panels)
    q = g["h2"]
    if q.lo <= 0 or q.hi >= D("0.52"):
        raise ArithmeticError("q initialization gate failed")
    upper, umeta = gaussian_moments(q.sqrt(), panels)
    coeff = reference_coefficients(g, upper)
    if min(coeff["n1sq"].lo, coeff["n2sq"].lo, coeff["k"].lo) <= 0:
        raise ArithmeticError("moment positivity/covariance gate failed")
    initialization_seconds = time.perf_counter() - started
    evolution_started = time.perf_counter()
    b0, beta0 = I(0), I(0)
    half_time = Fraction(1, 400)
    half = rational(half_time)
    bhalf, betahalf = clock_free_step(b0, beta0, coeff["k"], half)
    save_checkpoint(checkpoint_path, half_time, bhalf, betahalf, coeff)
    # Actually discard the in-memory continuation inputs: reload all state,
    # coefficients and certificate time from the saved JSON checkpoint.
    loaded = load_checkpoint(checkpoint_path)
    final_time, bend, betaend, restored_coeff = advance_checkpoint(loaded, half_time)
    direct_b, direct_beta = clock_free_step(b0, beta0, coeff["k"], 2 * half)
    restart_agreement = not (bend.hi < direct_b.lo or direct_b.hi < bend.lo
                            or betaend.hi < direct_beta.lo or direct_beta.hi < betaend.lo)
    observations = [reference_observations(coeff, b0, beta0, I(0)),
                    reference_observations(coeff, bhalf, betahalf, half),
                    reference_observations(restored_coeff, bend, betaend, rational(final_time))]
    final = observations[-1]
    def width(record):
        return I(record["hi"]) - I(record["lo"])
    errors = {
        "first_total": (I(final["first_rms_analytic_error"]["hi"])
                       + width(final["first_rms_estimate"]) / 2).hi,
        "upper_total": (I(final["upper_rms_analytic_error"]["hi"])
                       + width(final["upper_rms_estimate"]) / 2).hi,
        "prediction_total": (I(final["whole_circle_prediction_error"]["hi"])
                            + width(final["prediction_e1_estimate"]) / 2).hi,
    }
    # Prediction error is uniform; its positive sup lower bound is witnessed at e1.
    passed = (D(final["whole_circle_signal_lower"]) > D("1e-4")
              and D(final["first_rms_true_enclosure"]["lo"]) > D("1e-7")
              and D(final["upper_rms_true_enclosure"]["lo"]) > D("1e-7")
              and errors["first_total"] <= D("1e-7")
              and errors["upper_total"] <= D("1e-7")
              and errors["prediction_total"] <= D("1e-5")
              and restart_agreement)
    return {"mode": "reference_certificate", "pass": passed,
            "scope": "reference Duhamel output certificate; not full C-H3",
            "precision_digits": 60,
            "initialization": {"g": gmeta, "upper": umeta,
                               "seconds": initialization_seconds},
            "moments_g": {key: value.record() for key, value in g.items()},
            "moments_upper": {key: value.record() for key, value in upper.items()},
            "coefficients": {key: value.record() for key, value in coeff.items()},
            "observations": observations, "restart_enclosures_overlap": restart_agreement,
            "checkpoint": {"path": str(checkpoint_path),
                           "sha256": hashlib.sha256(checkpoint_path.read_bytes()).hexdigest(),
                           "reloaded_elapsed": {"numerator": loaded[0].numerator,
                                                "denominator": loaded[0].denominator},
                           "reloaded_b": loaded[1].record(), "reloaded_beta": loaded[2].record()},
            "total_error_at_T": {key: str(value) for key, value in errors.items()},
            "evolution_seconds": time.perf_counter() - evolution_started,
            "seconds": time.perf_counter() - started}


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--run", action="store_true")
    parser.add_argument("--panels", type=int, default=8192)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("refusing to overwrite an existing result")
    if args.panels < 2 or args.panels % 2:
        raise SystemExit("positive even subdivision count required")
    result = (preflight(args.panels) if args.preflight
              else run(args.panels, args.output.parent / "midpoint_checkpoint.json"))
    result["environment"] = {"python": platform.python_version(),
                             "platform": platform.platform(),
                             "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                             "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("mode", "seconds")}
                     | {"output": str(args.output), "pass": result.get("pass")}, indent=2))


if __name__ == "__main__":
    main()
