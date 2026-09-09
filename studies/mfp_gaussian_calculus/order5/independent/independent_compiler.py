"""Independent order-five Gaussian-normal-form compiler for H=2, B=1.

This module deliberately does not import the primary order-five compiler.  It
implements the large-width coefficient algebra from the exact rank-one matrix
flow

    adot = phi(z),  Adot = b h^T / n,  udot = phi'(u) A^T b,

using ordinary (not exponential) Taylor coefficients.  Matrix reuse is
handled by chronological forward/reverse response terms.  All auxiliary
Gaussians are then removed by an inverse-free Wick--Stein recursion.  The
terminal objects are sparse polynomials in the one-dimensional atoms M_nu.

Layer-tagged atoms are retained first (X for U ~ N(0,Q0), Y for
Z ~ N(0,Q1)).  A separate exact homomorphism then identifies the two layers
and imposes E[phi(G)^2]=1 for the unit-Gram specialization.  No Hermite or
polynomial approximation of phi is used.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path
from typing import DefaultDict, Iterable, Mapping


MAX_DERIVATIVE = 9  # permits response intermediates; terminal audit is <= 5
NF = 5              # F_1,...,F_5
NR = 5              # R_0,...,R_4

# Layer tags are -1 for X/U and -2 for Y/Z.  The remaining entries are the
# derivative-multiplicity vector.  The empty tuple is the multiplicative unit.
Atom = tuple[int, ...]
MomentMonomial = tuple[Atom, ...]
MPoly = dict[MomentMonomial, Fraction]


def _trim_atom(counts: Iterable[int], layer: int) -> Atom:
    values = list(counts)
    while values and values[-1] == 0:
        values.pop()
    return () if not values else (layer, *values)


def _unit_atom(atom: Atom) -> Atom:
    """Forget the layer tag and impose M_200000=1."""

    if not atom:
        return ()
    counts = tuple(atom[1:]) if atom[0] in (-1, -2) else atom
    return () if counts == (2,) else counts


def collapse_unit_gram(polynomial: Mapping[MomentMonomial, Fraction]) -> MPoly:
    out: DefaultDict[MomentMonomial, Fraction] = defaultdict(Fraction)
    for monomial, coefficient in polynomial.items():
        collapsed = tuple(sorted(value for atom in monomial if (value := _unit_atom(atom))))
        out[collapsed] += coefficient
    return {key: value for key, value in out.items() if value}


def _moment_monomial(*atoms: Atom) -> MomentMonomial:
    return tuple(sorted(atom for atom in atoms if atom))


def mp_const(value: int | Fraction) -> MPoly:
    value = Fraction(value)
    return {} if value == 0 else {(): value}


def mp_add(*polynomials: Mapping[MomentMonomial, Fraction]) -> MPoly:
    out: DefaultDict[MomentMonomial, Fraction] = defaultdict(Fraction)
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] += coefficient
    return {key: value for key, value in out.items() if value}


def mp_scale(polynomial: Mapping[MomentMonomial, Fraction], value: int | Fraction) -> MPoly:
    value = Fraction(value)
    if not value:
        return {}
    return {key: value * coefficient for key, coefficient in polynomial.items() if coefficient}


def mp_mul(left: Mapping[MomentMonomial, Fraction], right: Mapping[MomentMonomial, Fraction]) -> MPoly:
    if not left or not right:
        return {}
    out: DefaultDict[MomentMonomial, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            out[tuple(sorted(lm + rm))] += lc * rc
    return {key: value for key, value in out.items() if value}


@dataclass(frozen=True, order=True)
class RandomMonomial:
    """One random-coordinate monomial before Gaussian elimination."""

    x: tuple[int, ...]
    y: tuple[int, ...]
    a: int
    f: tuple[int, ...]
    r: tuple[int, ...]
    moments: MomentMonomial = ()


RPoly = dict[RandomMonomial, Fraction]


ZERO_MONOMIAL = RandomMonomial(
    (0,) * MAX_DERIVATIVE,
    (0,) * MAX_DERIVATIVE,
    0,
    (0,) * NF,
    (0,) * NR,
    (),
)


def rp_const(value: int | Fraction) -> RPoly:
    value = Fraction(value)
    return {} if not value else {ZERO_MONOMIAL: value}


def rp_generator(kind: str, index: int = 0) -> RPoly:
    x = [0] * MAX_DERIVATIVE
    y = [0] * MAX_DERIVATIVE
    f = [0] * NF
    r = [0] * NR
    a = 0
    if kind == "x":
        x[index] = 1
    elif kind == "y":
        y[index] = 1
    elif kind == "a":
        a = 1
    elif kind == "f":
        f[index - 1] = 1
    elif kind == "r":
        r[index] = 1
    else:
        raise ValueError(kind)
    monomial = RandomMonomial(tuple(x), tuple(y), a, tuple(f), tuple(r), ())
    return {monomial: Fraction(1)}


def rp_from_mp(polynomial: Mapping[MomentMonomial, Fraction]) -> RPoly:
    return {
        RandomMonomial(
            ZERO_MONOMIAL.x,
            ZERO_MONOMIAL.y,
            0,
            ZERO_MONOMIAL.f,
            ZERO_MONOMIAL.r,
            monomial,
        ): coefficient
        for monomial, coefficient in polynomial.items()
        if coefficient
    }


def rp_add(*polynomials: Mapping[RandomMonomial, Fraction]) -> RPoly:
    out: DefaultDict[RandomMonomial, Fraction] = defaultdict(Fraction)
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] += coefficient
    return {key: value for key, value in out.items() if value}


def rp_scale(polynomial: Mapping[RandomMonomial, Fraction], value: int | Fraction) -> RPoly:
    value = Fraction(value)
    if not value:
        return {}
    return {key: value * coefficient for key, coefficient in polynomial.items() if coefficient}


def _add_counts(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def rp_mul(left: Mapping[RandomMonomial, Fraction], right: Mapping[RandomMonomial, Fraction]) -> RPoly:
    if not left or not right:
        return {}
    out: DefaultDict[RandomMonomial, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = RandomMonomial(
                _add_counts(lm.x, rm.x),
                _add_counts(lm.y, rm.y),
                lm.a + rm.a,
                _add_counts(lm.f, rm.f),
                _add_counts(lm.r, rm.r),
                tuple(sorted(lm.moments + rm.moments)),
            )
            out[monomial] += lc * rc
    return {key: value for key, value in out.items() if value}


def rp_product(*polynomials: Mapping[RandomMonomial, Fraction]) -> RPoly:
    out = rp_const(1)
    for polynomial in polynomials:
        out = rp_mul(out, polynomial)
    return out


def rp_power(polynomial: Mapping[RandomMonomial, Fraction], exponent: int) -> RPoly:
    if exponent < 0:
        raise ValueError("negative exponent")
    out = rp_const(1)
    base = dict(polynomial)
    power = exponent
    while power:
        if power & 1:
            out = rp_mul(out, base)
        power //= 2
        if power:
            base = rp_mul(base, base)
    return out


def rp_derivative(polynomial: Mapping[RandomMonomial, Fraction], kind: str, index: int) -> RPoly:
    """Syntactic derivative with respect to F_s or R_s.

    F_0 is the base Gaussian activation argument, so differentiation raises
    the derivative order of one Y factor.  This is only an intermediate
    operation; terminal atoms above order five are rejected.
    """

    out: DefaultDict[RandomMonomial, Fraction] = defaultdict(Fraction)
    for monomial, coefficient in polynomial.items():
        if kind == "r":
            count = monomial.r[index]
            if not count:
                continue
            r = list(monomial.r)
            r[index] -= 1
            target = RandomMonomial(monomial.x, monomial.y, monomial.a, monomial.f, tuple(r), monomial.moments)
            out[target] += coefficient * count
        elif kind == "f" and index > 0:
            count = monomial.f[index - 1]
            if not count:
                continue
            f = list(monomial.f)
            f[index - 1] -= 1
            target = RandomMonomial(monomial.x, monomial.y, monomial.a, tuple(f), monomial.r, monomial.moments)
            out[target] += coefficient * count
        elif kind == "f" and index == 0:
            for derivative, count in enumerate(monomial.y[:-1]):
                if not count:
                    continue
                y = list(monomial.y)
                y[derivative] -= 1
                y[derivative + 1] += 1
                target = RandomMonomial(monomial.x, tuple(y), monomial.a, monomial.f, monomial.r, monomial.moments)
                out[target] += coefficient * count
        else:
            raise ValueError((kind, index))
    return {key: value for key, value in out.items() if value}


def series_mul(left: list[RPoly], right: list[RPoly], order: int) -> list[RPoly]:
    return [
        rp_add(*(rp_mul(left[p], right[k - p]) for p in range(k + 1)))
        for k in range(order + 1)
    ]


def phi_series_coefficient(
    base: str,
    activation_derivative: int,
    delta: list[RPoly],
    order: int,
) -> RPoly:
    """Coefficient [t^order] phi^(activation_derivative)(G+delta(t))."""

    if not delta or delta[0]:
        raise ValueError("delta series must have a zero constant coefficient")
    result: RPoly = {}
    power_series = [rp_const(1)] + [{} for _ in range(order)]
    for multiplicity in range(order + 1):
        if multiplicity:
            power_series = series_mul(power_series, delta, order)
        derivative = activation_derivative + multiplicity
        if derivative >= MAX_DERIVATIVE:
            raise ValueError("increase MAX_DERIVATIVE")
        generator = rp_generator(base, derivative)
        result = rp_add(
            result,
            rp_scale(rp_mul(generator, power_series[order]), Fraction(1, factorial(multiplicity))),
        )
    return result


def _double_factorial_odd(n: int) -> int:
    answer = 1
    for value in range(n, 0, -2):
        answer *= value
    return answer


class GaussianEliminator:
    """Inverse-free Wick--Stein expectation for the chronological state."""

    def __init__(self, *, unit_gram: bool = False) -> None:
        self.H: dict[tuple[int, int], MPoly] = {}
        self.B: dict[tuple[int, int], MPoly] = {}
        self.unit_gram = unit_gram
        # Existing covariance entries are immutable, so these caches remain
        # valid as later chronological rows are appended.
        self._r_cache: dict[tuple[int, ...], MPoly] = {(0,) * NR: {(): Fraction(1)}}
        self._f_cache: dict[tuple[tuple[int, ...], tuple[int, ...]], dict[tuple[int, ...], MPoly]] = {}
        self._rf_cache: dict[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]], dict[tuple[int, ...], MPoly]] = {}

    @staticmethod
    def _entry(table: Mapping[tuple[int, int], MPoly], i: int, j: int) -> MPoly:
        return table[(max(i, j), min(i, j))]

    def _wick_r(self, exponents: tuple[int, ...]) -> MPoly:
        if exponents in self._r_cache:
            return self._r_cache[exponents]
        if sum(exponents) % 2:
            self._r_cache[exponents] = {}
            return {}
        i = next(index for index, count in enumerate(exponents) if count)
        remainder = list(exponents)
        remainder[i] -= 1
        answer: MPoly = {}
        for j, count in enumerate(remainder):
            if not count:
                continue
            paired = list(remainder)
            paired[j] -= 1
            sub = self._wick_r(tuple(paired))
            answer = mp_add(answer, mp_scale(mp_mul(self._entry(self.B, i, j), sub), count))
        self._r_cache[exponents] = answer
        return answer

    def _stein_f(self, exponents: tuple[int, ...], y: tuple[int, ...]) -> dict[tuple[int, ...], MPoly]:
        key = (exponents, y)
        if key in self._f_cache:
            return self._f_cache[key]
        if not any(exponents):
            answer = {y: {(): Fraction(1)}}
            self._f_cache[key] = answer
            return answer
        i0 = next(index for index, count in enumerate(exponents) if count)
        i = i0 + 1  # state coordinate zero is F_1
        remainder = list(exponents)
        remainder[i0] -= 1
        accumulated: dict[tuple[int, ...], MPoly] = {}

        # Pair F_i with another auxiliary F_j.
        for j0, count in enumerate(remainder):
            if not count:
                continue
            paired = list(remainder)
            paired[j0] -= 1
            covariance = self._entry(self.H, i, j0 + 1)
            for yout, entries in self._stein_f(tuple(paired), y).items():
                piece = mp_scale(mp_mul(covariance, entries), count)
                accumulated[yout] = mp_add(accumulated.get(yout, {}), piece)

        # Or attach F_i to the base F_0 and differentiate the integrand.
        covariance0 = self._entry(self.H, i, 0)
        for derivative, count in enumerate(y[:-1]):
            if not count:
                continue
            raised = list(y)
            raised[derivative] -= 1
            raised[derivative + 1] += 1
            for yout, entries in self._stein_f(tuple(remainder), tuple(raised)).items():
                piece = mp_scale(mp_mul(covariance0, entries), count)
                accumulated[yout] = mp_add(accumulated.get(yout, {}), piece)

        answer = {state: value for state, value in accumulated.items() if value}
        self._f_cache[key] = answer
        return answer

    def expectation(self, polynomial: Mapping[RandomMonomial, Fraction]) -> MPoly:
        answer: MPoly = {}
        for monomial, coefficient in polynomial.items():
            if monomial.a % 2:
                continue
            a_moment = _double_factorial_odd(monomial.a - 1) if monomial.a else 1
            r_moment = self._wick_r(monomial.r)
            if not r_moment:
                continue
            rf_key = (monomial.r, monomial.f, monomial.y)
            if rf_key not in self._rf_cache:
                self._rf_cache[rf_key] = {
                    y_counts: mp_mul(r_moment, f_moment)
                    for y_counts, f_moment in self._stein_f(monomial.f, monomial.y).items()
                }
            f_reductions = self._rf_cache[rf_key]
            x_atom = _trim_atom(monomial.x, -1)
            scalar = Fraction(coefficient * a_moment)
            for y_counts, rf_moment in f_reductions.items():
                y_atom = _trim_atom(y_counts, -2)
                base_moments = _moment_monomial(x_atom, y_atom, *monomial.moments)
                for covariance_moments, covariance_coefficient in rf_moment.items():
                    full = tuple(sorted(base_moments + covariance_moments))
                    answer[full] = answer.get(full, Fraction(0)) + scalar * covariance_coefficient
                    if not answer[full]:
                        del answer[full]
        return collapse_unit_gram(answer) if self.unit_gram else answer


@dataclass
class IndependentResult:
    A: MPoly
    B: MPoly
    C: MPoly
    f_coefficients: list[MPoly]
    H: dict[tuple[int, int], MPoly]
    reverse_covariance: dict[tuple[int, int], MPoly]
    diagnostics: dict[str, object]


def compile_layer_tagged(
    *, q0: int | Fraction = 1, progress: bool = False, unit_gram: bool = False
) -> IndependentResult:
    """Compile layer-tagged coefficient maps through order five.

    The distributional meanings of tagged atoms are
    X_nu=E_{N(0,Q0)} prod phi^(r)^nu_r and
    Y_nu=E_{N(0,Q1)} prod phi^(r)^nu_r, where Q1=X_200....
    ``q0`` is retained as an exact rational prefactor; the frozen control map
    uses Q0=q0=1.
    """

    eliminate = GaussianEliminator(unit_gram=unit_gram)
    x = [rp_generator("x", derivative) for derivative in range(MAX_DERIVATIVE)]
    y = [rp_generator("y", derivative) for derivative in range(MAX_DERIVATIVE)]
    a0 = rp_generator("a")

    h: list[RPoly] = [x[0]]
    hp: list[RPoly] = [x[1]]
    u_delta: list[RPoly] = [{}]
    z_delta: list[RPoly] = [{}]
    g: list[RPoly] = [y[0]]
    gp: list[RPoly] = [y[1]]
    a: list[RPoly] = [a0]
    b: list[RPoly] = [rp_mul(a0, y[1])]
    r: list[RPoly] = []

    eliminate.H[(0, 0)] = eliminate.expectation(rp_mul(h[0], h[0]))
    eliminate.B[(0, 0)] = eliminate.expectation(rp_mul(b[0], b[0]))

    beta00 = eliminate.expectation(rp_derivative(b[0], "f", 0))
    r0 = rp_add(rp_generator("r", 0), rp_mul(h[0], rp_from_mp(beta00)))
    r.append(r0)
    u1 = rp_scale(rp_mul(hp[0], r0), q0)
    u_delta.append(u1)
    h.append(phi_series_coefficient("x", 0, u_delta, 1))
    hp.append(phi_series_coefficient("x", 1, u_delta, 1))

    sizes: dict[str, object] = {"beta_00_terms": len(beta00)}

    # Full chronological steps k=1,...,4.
    for k in range(1, 5):
        if progress:
            print(f"step {k}: establish H/F/z/g/b/B/R/u/h", flush=True)

        for ell in range(k + 1):
            eliminate.H[(k, ell)] = eliminate.expectation(rp_mul(h[k], h[ell]))
            if progress:
                print(f"step {k}: H({k},{ell}) terms={len(eliminate.H[(k, ell)])}", flush=True)
        if progress:
            print(f"step {k}: H done", flush=True)

        forward = rp_generator("f", k)
        responses = []
        for s in range(k):
            alpha = eliminate.expectation(rp_derivative(h[k], "r", s))
            responses.append(rp_mul(b[s], rp_from_mp(alpha)))

        low_rank = []
        for m in range(1, k + 1):
            for p in range(m):
                q = m - 1 - p
                covariance = eliminate._entry(eliminate.H, q, k - m)
                low_rank.append(rp_scale(rp_mul(b[p], rp_from_mp(covariance)), Fraction(1, m)))
        zk = rp_add(forward, *responses, *low_rank)
        if progress:
            print(f"step {k}: z done ({len(zk)})", flush=True)
        z_delta.append(zk)
        g.append(phi_series_coefficient("y", 0, z_delta, k))
        gp.append(phi_series_coefficient("y", 1, z_delta, k))
        a.append(rp_scale(g[k - 1], Fraction(1, k)))
        bk = rp_add(*(rp_mul(a[p], gp[k - p]) for p in range(k + 1)))
        b.append(bk)
        if progress:
            print(f"step {k}: b done ({len(bk)})", flush=True)

        for ell in range(k + 1):
            eliminate.B[(k, ell)] = eliminate.expectation(rp_mul(b[k], b[ell]))
        if progress:
            print(f"step {k}: B done", flush=True)

        reverse = rp_generator("r", k)
        reverse_responses = []
        for s in range(k + 1):
            beta = eliminate.expectation(rp_derivative(b[k], "f", s))
            reverse_responses.append(rp_mul(h[s], rp_from_mp(beta)))
        reverse_low_rank = []
        for m in range(1, k + 1):
            for p in range(m):
                q = m - 1 - p
                covariance = eliminate._entry(eliminate.B, p, k - m)
                reverse_low_rank.append(rp_scale(rp_mul(h[q], rp_from_mp(covariance)), Fraction(1, m)))
        rk = rp_add(reverse, *reverse_responses, *reverse_low_rank)
        if progress:
            print(f"step {k}: r done ({len(rk)})", flush=True)
        r.append(rk)

        uk1 = rp_scale(
            rp_add(*(rp_mul(hp[p], r[k - p]) for p in range(k + 1))),
            Fraction(q0, k + 1),
        )
        u_delta.append(uk1)
        h.append(phi_series_coefficient("x", 0, u_delta, k + 1))
        hp.append(phi_series_coefficient("x", 1, u_delta, k + 1))

        sizes[f"step_{k}"] = {
            "h": len(h[k]), "z": len(zk), "g": len(g[k]), "b": len(bk),
            "r": len(rk), "next_h": len(h[k + 1]),
            "H_total_terms": sum(len(value) for key, value in eliminate.H.items() if key[0] <= k),
            "B_total_terms": sum(len(value) for key, value in eliminate.B.items() if key[0] <= k),
        }
        if progress:
            print(sizes[f"step_{k}"], flush=True)

    # Terminal forward step k=5; b_5 and R_5 are not needed by f_5.
    k = 5
    for ell in range(k + 1):
        eliminate.H[(k, ell)] = eliminate.expectation(rp_mul(h[k], h[ell]))
    forward = rp_generator("f", k)
    responses = []
    for s in range(k):
        alpha = eliminate.expectation(rp_derivative(h[k], "r", s))
        responses.append(rp_mul(b[s], rp_from_mp(alpha)))
    low_rank = []
    for m in range(1, k + 1):
        for p in range(m):
            q = m - 1 - p
            covariance = eliminate._entry(eliminate.H, q, k - m)
            low_rank.append(rp_scale(rp_mul(b[p], rp_from_mp(covariance)), Fraction(1, m)))
    z5 = rp_add(forward, *responses, *low_rank)
    z_delta.append(z5)
    g.append(phi_series_coefficient("y", 0, z_delta, 5))
    a.append(rp_scale(g[4], Fraction(1, 5)))

    f_coefficients: list[MPoly] = []
    for k in range(6):
        coefficient = eliminate.expectation(
            rp_add(*(rp_mul(a[p], g[k - p]) for p in range(k + 1)))
        )
        f_coefficients.append(coefficient)

    result = IndependentResult(
        A=mp_scale(f_coefficients[1], factorial(1)),
        B=mp_scale(f_coefficients[3], factorial(3)),
        C=mp_scale(f_coefficients[5], factorial(5)),
        f_coefficients=f_coefficients,
        H=eliminate.H,
        reverse_covariance=eliminate.B,
        diagnostics=sizes,
    )
    return result


def compile_unit_gram(*, progress: bool = False) -> IndependentResult:
    return compile_layer_tagged(q0=1, progress=progress, unit_gram=True)


def _atom_text(atom: Atom) -> str:
    if atom and atom[0] in (-1, -2):
        tag = "X" if atom[0] == -1 else "Y"
        counts = atom[1:]
        width = max(6, len(counts))
        return tag + "_" + "".join(str(value) for value in counts + (0,) * (width - len(counts)))
    width = max(6, len(atom))
    return "M_" + "".join(str(value) for value in atom + (0,) * (width - len(atom)))


def mpoly_to_terms(polynomial: Mapping[MomentMonomial, Fraction]) -> list[dict[str, object]]:
    return [
        {
            "coefficient": str(coefficient),
            "atoms": [_atom_text(atom) for atom in monomial],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]


def mpoly_text(polynomial: Mapping[MomentMonomial, Fraction]) -> str:
    if not polynomial:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(polynomial.items()):
        atoms = " ".join(_atom_text(atom) for atom in monomial) or "1"
        pieces.append(f"({coefficient})*{atoms}")
    return " +\n".join(pieces)


def write_result(unit: IndependentResult, directory: Path) -> dict[str, str]:
    directory.mkdir(parents=True, exist_ok=True)
    payload = {
        "format": "independent-H2-B1-unit-Mpoly-v3",
        "normalization": "M_200000=1",
        "unit_gram": {
            "A": mpoly_to_terms(unit.A),
            "B": mpoly_to_terms(unit.B),
            "C": mpoly_to_terms(unit.C),
        },
        "parity": {
            "F0": mpoly_to_terms(unit.f_coefficients[0]),
            "F2_over_2factorial": mpoly_to_terms(unit.f_coefficients[2]),
            "F4_over_4factorial": mpoly_to_terms(unit.f_coefficients[4]),
        },
        "diagnostics": unit.diagnostics,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    exact_file_bytes = encoded + b"\n"
    json_path = directory / "independent_coefficient_map.json"
    json_path.write_bytes(exact_file_bytes)
    digest = hashlib.sha256(exact_file_bytes).hexdigest()
    (directory / "FROZEN_SHA256.txt").write_text(digest + "  independent_coefficient_map.json\n")
    (directory / "A.txt").write_text(mpoly_text(unit.A) + "\n")
    (directory / "B.txt").write_text(mpoly_text(unit.B) + "\n")
    (directory / "C.txt").write_text(mpoly_text(unit.C) + "\n")
    return {"json": str(json_path), "sha256": digest}


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    compiled = compile_unit_gram(progress=True)
    # The expensive layer-tagged map is intentionally not generated by the
    # default command.  Polynomial controls use a direct exact specialization.
    locations = write_result(compiled, root)
    print(json.dumps(locations, indent=2))
    print("term counts", len(compiled.A), len(compiled.B), len(compiled.C))
