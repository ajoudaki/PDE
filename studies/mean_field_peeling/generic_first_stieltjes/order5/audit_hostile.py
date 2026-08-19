"""Hostile, derivation-independent exact checks for the order-five package.

This file is deliberately outside both coefficient compilers.  It uses a
minimal exact sparse-polynomial algebra to check the universal differential
identity on a generic two-variable polynomial.  Later coefficient-map gates
are appended here only after both producers have frozen their outputs.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb, exp, sqrt
from pathlib import Path
import re


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, Fraction]

# Canonical moment-polynomial types used only by the frozen-artifact diff.
MomentAtom = tuple[int, ...]
MomentMonomial = tuple[MomentAtom, ...]
MomentPolynomial = dict[MomentMonomial, Fraction]

HERE = Path(__file__).resolve().parent
PRIMARY_UNIT = HERE / "compiler" / "UNIT_GRAM_ABC_NORMAL_FORM.txt"
PRIMARY_TAGGED = HERE / "compiler" / "LAYER_SEPARATED_ABC_NORMAL_FORM.txt"
PRIMARY_MANIFEST = HERE / "compiler" / "MANIFEST.json"
INDEPENDENT_JSON = HERE / "independent" / "independent_coefficient_map.json"
INDEPENDENT_HASH = HERE / "independent" / "FROZEN_SHA256.txt"
INDEPENDENT_TAGGED_JSON = HERE / "independent" / "independent_layer_tagged_coefficient_map.json"
INDEPENDENT_TAGGED_HASH = HERE / "independent" / "LAYER_TAGGED_FROZEN_SHA256.txt"
PRIMARY_SYMBOLIC_Q0_JSON = HERE / "compiler" / "PRIMARY_SYMBOLIC_Q0_COEFFICIENT_MAP.json"
INDEPENDENT_SYMBOLIC_Q0_JSON = HERE / "independent" / "independent_symbolic_q0_coefficient_map.json"
INDEPENDENT_SYMBOLIC_Q0_HASH = HERE / "independent" / "SYMBOLIC_Q0_FROZEN_SHA256.txt"
SYMBOLIC_Q0_COMPARISON = HERE / "independent" / "SYMBOLIC_Q0_PRIMARY_COMPARISON.json"
SELF_CONTAINED = HERE / "H2_B1_ORDER5_SELF_CONTAINED.md"
SELF_CONTAINED_MANIFEST = HERE / "SELF_CONTAINED_MANIFEST.json"
UNIT_ATOM = re.compile(r"M_\{([0-9]{6})\}")
TAGGED_ATOM = re.compile(r"([XY])_\{([0-9]{6})\}")


def add(*polynomials: Polynomial) -> Polynomial:
    out: dict[Exponent, Fraction] = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return {key: value for key, value in out.items() if value}


def scale(polynomial: Polynomial, coefficient: int | Fraction) -> Polynomial:
    coefficient = Fraction(coefficient)
    return {
        exponent: coefficient * value
        for exponent, value in polynomial.items()
        if coefficient * value
    }


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: dict[Exponent, Fraction] = {}
    for alpha, ca in left.items():
        for beta, cb in right.items():
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            out[exponent] = out.get(exponent, Fraction(0)) + ca * cb
    return {key: value for key, value in out.items() if value}


def derivative(polynomial: Polynomial, coordinate: int) -> Polynomial:
    out: dict[Exponent, Fraction] = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[coordinate]
        if not power:
            continue
        reduced = list(exponent)
        reduced[coordinate] -= 1
        key = tuple(reduced)
        out[key] = out.get(key, Fraction(0)) + power * coefficient
    return out


def tensor_derivative(polynomial: Polynomial, indices: tuple[int, ...]) -> Polynomial:
    out = polynomial
    for coordinate in indices:
        out = derivative(out, coordinate)
    return out


def dot(left: list[Polynomial], right: list[Polynomial]) -> Polynomial:
    return add(*(multiply(x, y) for x, y in zip(left, right)))


def apply_hessian(f: Polynomial, vector: list[Polynomial]) -> list[Polynomial]:
    dimension = len(vector)
    return [
        add(
            *(
                multiply(tensor_derivative(f, (i, j)), vector[j])
                for j in range(dimension)
            )
        )
        for i in range(dimension)
    ]


def contract(
    f: Polynomial,
    rank: int,
    vectors: tuple[list[Polynomial], ...],
) -> Polynomial:
    dimension = len(vectors[0])
    if rank != len(vectors):
        raise ValueError("rank/vector mismatch")
    terms: list[Polynomial] = []
    for indices in product(range(dimension), repeat=rank):
        term = tensor_derivative(f, indices)
        for slot, coordinate in enumerate(indices):
            term = multiply(term, vectors[slot][coordinate])
        terms.append(term)
    return add(*terms)


def gradient_flow_operator(f: Polynomial, observable: Polynomial) -> Polynomial:
    dimension = len(next(iter(f)))
    return add(
        *(
            multiply(derivative(f, coordinate), derivative(observable, coordinate))
            for coordinate in range(dimension)
        )
    )


def generic_polynomial() -> Polynomial:
    """Dense degree-five polynomial with no symmetry or homogeneous shortcut."""

    out: Polynomial = {}
    for total_degree in range(1, 6):
        for first_power in range(total_degree + 1):
            exponent = (first_power, total_degree - first_power)
            # Deterministic, non-factorized coefficients; all are nonzero.
            coefficient = Fraction(
                2 + 3 * total_degree + 5 * first_power + first_power * total_degree,
                1 + (total_degree + first_power) % 3,
            )
            out[exponent] = coefficient
    return out


def test_universal_six_family_identity() -> None:
    f = generic_polynomial()
    p = [derivative(f, coordinate) for coordinate in range(2)]
    hp = apply_hessian(f, p)
    h2p = apply_hessian(f, hp)
    tpp = [
        contract(f, 3, ([{(0, 0): Fraction(int(i == coordinate))} for i in range(2)], p, p))
        for coordinate in range(2)
    ]

    direct = f
    for _ in range(5):
        direct = gradient_flow_operator(f, direct)

    families = add(
        scale(contract(f, 5, (p, p, p, p, p)), 2),
        scale(contract(f, 4, (hp, p, p, p)), 22),
        scale(contract(f, 3, (tpp, p, p)), 14),
        scale(contract(f, 3, (h2p, p, p)), 30),
        scale(contract(f, 3, (hp, hp, p)), 36),
        scale(dot(h2p, h2p), 16),
    )
    assert direct == families


def test_raw_width_scaling_exponents() -> None:
    """Substitution v=n p makes every raw family exactly n**5 times its base."""

    # (explicit prefactor in the raw formula, number of occurrences of v)
    # Nested T[v,v] and each H application are linear and do not alter the
    # count of v occurrences.  Squaring H**2 v contributes two occurrences.
    families = ((0, 5), (1, 4), (1, 4), (2, 3), (2, 3), (3, 2))
    assert tuple(prefactor + velocity_count for prefactor, velocity_count in families) == (5,) * 6


def test_pade_series_algebra() -> None:
    """Check the inverse/kernel coefficients as exact rational examples."""

    # Use non-special rational values so that no cancellation can hide a sign.
    A, B, C = Fraction(7), Fraction(11), Fraction(13)
    mu0 = B / (2 * A**2)
    mu1 = (4 * B**2 - A * C) / (24 * A**5)
    inverse_1 = 1 / A
    inverse_3 = -B / (6 * A**4)
    inverse_5 = (10 * B**2 - A * C) / (120 * A**7)

    # [y^2] and [y^4] in F'(t(y)).
    k2 = B * inverse_1**2 / 2
    k4 = B * inverse_1 * inverse_3 + C * inverse_1**4 / 24
    assert k2 == mu0
    assert k4 == -mu1
    # Rational kernel A + mu0*y^2/(1+(mu1/mu0)*y^2).
    assert -mu0 * (mu1 / mu0) == -mu1
    assert inverse_5 == (10 * B**2 - A * C) / (120 * A**7)


def mp_add(left: MomentPolynomial, right: MomentPolynomial) -> MomentPolynomial:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return {key: value for key, value in out.items() if value}


def mp_mul(left: MomentPolynomial, right: MomentPolynomial) -> MomentPolynomial:
    if not left or not right:
        return {}
    out: dict[MomentMonomial, Fraction] = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(sorted(lm + rm))
            out[monomial] = out.get(monomial, Fraction(0)) + lc * rc
    return {key: value for key, value in out.items() if value}


def _primary_factor(token: str, values: dict[str, MomentPolynomial]) -> MomentPolynomial:
    token = token.strip()
    if token in values:
        return values[token]
    match = UNIT_ATOM.fullmatch(token)
    if match:
        atom = tuple(int(value) for value in match.group(1))
        return {(atom,): Fraction(1)}
    return {(): Fraction(token)}


def parse_primary_unit_artifact() -> dict[str, MomentPolynomial]:
    """Expand the primary deterministic DAG into exact sparse coefficient maps."""

    values: dict[str, MomentPolynomial] = {}
    allowed_name = re.compile(r"(?:t_[0-9]{5}|A|B|C)")
    for raw_line in PRIMARY_UNIT.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, rhs = (piece.strip() for piece in line.split("=", 1))
        assert allowed_name.fullmatch(name), name
        value: MomentPolynomial = {}
        for summand in rhs.split(" + "):
            term: MomentPolynomial = {(): Fraction(1)}
            for factor in summand.split(" * "):
                term = mp_mul(term, _primary_factor(factor, values))
            value = mp_add(value, term)
        values[name] = value
    return {name: values[name] for name in ("A", "B", "C")}


def parse_independent_unit_artifact() -> dict[str, MomentPolynomial]:
    payload = json.loads(INDEPENDENT_JSON.read_text())
    assert payload["normalization"] == "M_200000=1"
    result: dict[str, MomentPolynomial] = {}
    for root in ("A", "B", "C"):
        polynomial: MomentPolynomial = {}
        for term in payload["unit_gram"][root]:
            coefficient = Fraction(term["coefficient"])
            atoms: list[MomentAtom] = []
            for text in term["atoms"]:
                assert text.startswith("M_")
                digits = text[2:]
                assert len(digits) == 6 and digits.isdigit(), text
                atoms.append(tuple(int(value) for value in digits))
            monomial = tuple(sorted(atoms))
            polynomial[monomial] = polynomial.get(monomial, Fraction(0)) + coefficient
        result[root] = {key: value for key, value in polynomial.items() if value}
    return result


def parse_primary_tagged_artifact_q0_one() -> dict[str, dict[tuple[str, ...], Fraction]]:
    values: dict[str, dict[tuple[str, ...], Fraction]] = {
        "Q0": {(): Fraction(1)}
    }

    def factor(token: str) -> dict[tuple[str, ...], Fraction]:
        token = token.strip()
        if token in values:
            return values[token]
        match = TAGGED_ATOM.fullmatch(token)
        if match:
            name = f"{match.group(1)}_{match.group(2)}"
            return {(name,): Fraction(1)}
        return {(): Fraction(token)}

    for raw_line in PRIMARY_TAGGED.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, rhs = (piece.strip() for piece in line.split("=", 1))
        answer: dict[tuple[str, ...], Fraction] = {}
        for summand in rhs.split(" + "):
            term: dict[tuple[str, ...], Fraction] = {(): Fraction(1)}
            for token in summand.split(" * "):
                term = mp_mul(term, factor(token))  # same tuple-sorting algebra
            answer = mp_add(answer, term)
        values[name] = answer
    return {root: values[root] for root in ("A", "B", "C")}


def parse_independent_tagged_artifact() -> dict[str, dict[tuple[str, ...], Fraction]]:
    payload = json.loads(INDEPENDENT_TAGGED_JSON.read_text())
    assert payload["Q0"] == "1"
    result: dict[str, dict[tuple[str, ...], Fraction]] = {}
    for root in ("A", "B", "C"):
        polynomial: dict[tuple[str, ...], Fraction] = {}
        for term in payload[root]:
            atoms = tuple(sorted(term["atoms"]))
            polynomial[atoms] = polynomial.get(atoms, Fraction(0)) + Fraction(term["coefficient"])
        result[root] = {key: value for key, value in polynomial.items() if value}
    return result


def parse_symbolic_q0_artifact(
    path: Path,
) -> dict[str, dict[tuple[tuple[str, ...], int], Fraction]]:
    """Parse a frozen graded X/Y moment polynomial without compiler imports."""

    payload = json.loads(path.read_text())
    result: dict[str, dict[tuple[tuple[str, ...], int], Fraction]] = {}
    for root in ("A", "B", "C"):
        polynomial: dict[tuple[tuple[str, ...], int], Fraction] = {}
        terms = payload["maps"][root]
        for term in terms:
            atoms = tuple(sorted(term["atoms"]))
            for atom in atoms:
                match = re.fullmatch(r"[XY]_[0-9]{6}", atom)
                assert match, atom
                multiplicities = tuple(int(value) for value in atom[2:])
                assert max(
                    (
                        derivative
                        for derivative, multiplicity in enumerate(multiplicities)
                        if multiplicity
                    ),
                    default=0,
                ) <= 5
            degree = term["q0_degree"]
            assert isinstance(degree, int) and degree >= 0
            coefficient = Fraction(term["coefficient"])
            assert coefficient
            key = (atoms, degree)
            assert key not in polynomial, (path, root, key)
            polynomial[key] = coefficient
        result[root] = polynomial
    return result


def test_frozen_hashes_and_atom_grammar() -> None:
    manifest = json.loads(PRIMARY_MANIFEST.read_text())
    primary_bytes = PRIMARY_UNIT.read_bytes()
    assert sha256(primary_bytes).hexdigest() == manifest["sha256"]["unit_gram"]
    assert sha256(PRIMARY_TAGGED.read_bytes()).hexdigest() == manifest["sha256"]["layer_separated"]

    independent_bytes = INDEPENDENT_JSON.read_bytes()
    declared = INDEPENDENT_HASH.read_text().split()[0]
    assert sha256(independent_bytes).hexdigest() == declared
    tagged_bytes = INDEPENDENT_TAGGED_JSON.read_bytes()
    tagged_declared = INDEPENDENT_TAGGED_HASH.read_text().split()[0]
    assert sha256(tagged_bytes).hexdigest() == tagged_declared
    symbolic_bytes = INDEPENDENT_SYMBOLIC_Q0_JSON.read_bytes()
    symbolic_declared = INDEPENDENT_SYMBOLIC_Q0_HASH.read_text().split()[0]
    assert sha256(symbolic_bytes).hexdigest() == symbolic_declared

    primary = parse_primary_unit_artifact()
    independent = parse_independent_unit_artifact()
    normalized_variance = (2, 0, 0, 0, 0, 0)
    for source in (primary, independent):
        for polynomial in source.values():
            for monomial in polynomial:
                for atom in monomial:
                    assert len(atom) == 6
                    assert normalized_variance != atom
                    assert max(
                        (index for index, multiplicity in enumerate(atom) if multiplicity),
                        default=0,
                    ) <= 5

    tagged_text = PRIMARY_TAGGED.read_text()
    tagged_atoms = TAGGED_ATOM.findall(tagged_text)
    assert tagged_atoms
    for _, digits in tagged_atoms:
        atom = tuple(int(value) for value in digits)
        assert max(
            (index for index, multiplicity in enumerate(atom) if multiplicity),
            default=0,
        ) <= 5


def _ordinary_polynomial_multiply(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, ca in enumerate(left):
        for j, cb in enumerate(right):
            out[i + j] += ca * cb
    return tuple(out)


def _ordinary_polynomial_derivative(
    coefficients: tuple[Fraction, ...], order: int
) -> tuple[Fraction, ...]:
    out = coefficients
    for _ in range(order):
        out = tuple(Fraction(index) * value for index, value in enumerate(out[1:], 1))
        if not out:
            return (Fraction(0),)
    return out


def activation_product_moment(
    atom: MomentAtom,
    coefficients: tuple[Fraction, ...],
    variance: Fraction,
) -> Fraction:
    polynomial = (Fraction(1),)
    for derivative_order, multiplicity in enumerate(atom):
        factor = _ordinary_polynomial_derivative(coefficients, derivative_order)
        for _ in range(multiplicity):
            polynomial = _ordinary_polynomial_multiply(polynomial, factor)
    answer = Fraction(0)
    for power, coefficient in enumerate(polynomial):
        if power % 2:
            continue
        wick = 1
        for value in range(power - 1, 0, -2):
            wick *= value
        answer += coefficient * wick * variance ** (power // 2)
    return answer


def evaluate_tagged_artifact(
    coefficients: tuple[int | Fraction, ...], *, q0: int | Fraction = 1
) -> dict[str, Fraction]:
    """Evaluate the emitted arbitrary-variance DAG without compiler imports."""

    coefficients = tuple(Fraction(value) for value in coefficients)
    q0 = Fraction(q0)
    q1 = activation_product_moment((2, 0, 0, 0, 0, 0), coefficients, q0)
    values: dict[str, Fraction] = {"Q0": q0}
    atoms: dict[tuple[str, MomentAtom], Fraction] = {}

    def factor(token: str) -> Fraction:
        token = token.strip()
        if token in values:
            return values[token]
        match = TAGGED_ATOM.fullmatch(token)
        if match:
            layer = match.group(1)
            atom = tuple(int(value) for value in match.group(2))
            key = (layer, atom)
            if key not in atoms:
                variance = q0 if layer == "X" else q1
                atoms[key] = activation_product_moment(atom, coefficients, variance)
            return atoms[key]
        return Fraction(token)

    for raw_line in PRIMARY_TAGGED.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        name, rhs = (piece.strip() for piece in line.split("=", 1))
        total = Fraction(0)
        for summand in rhs.split(" + "):
            value = Fraction(1)
            for token in summand.split(" * "):
                value *= factor(token)
            total += value
        values[name] = total
    return {root: values[root] for root in ("A", "B", "C")}


def test_layer_tagged_exact_controls() -> None:
    expected = {
        (2,): (4, 0, 0),
        (0, 1): (3, 48, 1464),
        (1, 1): (6, 112, 4400),
        (0, 0, 1): (111, 1_685_184, 77_400_633_120),
    }
    for coefficients, target in expected.items():
        result = evaluate_tagged_artifact(coefficients)
        assert tuple(result[root] for root in ("A", "B", "C")) == target


def normalized_sine_moment(atom: MomentAtom) -> float:
    """Closed Fourier evaluation, not quadrature or a Hermite truncation."""

    sine_power = atom[0] + atom[2] + atom[4]
    cosine_power = atom[1] + atom[3] + atom[5]
    if sine_power % 2:
        return 0.0
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)
    derivative_sign = (-1) ** (atom[2] + atom[3])
    expectation = 0.0
    for j in range(sine_power + 1):
        for k in range(cosine_power + 1):
            frequency = sine_power - 2 * j + cosine_power - 2 * k
            expectation += (
                comb(sine_power, j)
                * (-1) ** j
                * comb(cosine_power, k)
                * exp(-(frequency**2) / 2.0)
            )
    expectation *= (-1) ** (sine_power // 2) / 2 ** (sine_power + cosine_power)
    return derivative_sign * expectation / normalization ** (sine_power + cosine_power)


def evaluate_unit_float(polynomial: MomentPolynomial) -> float:
    answer = 0.0
    for monomial, coefficient in polynomial.items():
        value = float(coefficient)
        for atom in monomial:
            value *= normalized_sine_moment(atom)
        answer += value
    return answer


def test_preregistered_sine_prediction_and_result() -> None:
    roots = parse_primary_unit_artifact()
    predictions = {root: evaluate_unit_float(polynomial) for root, polynomial in roots.items()}
    assert abs(predictions["A"] - 4.037096946465644) < 1.0e-11
    assert abs(predictions["B"] + 103.25733114677432) < 1.0e-10
    assert abs(predictions["C"] - 29944.43234293731) < 1.0e-8
    result = json.loads((HERE / "SINE_REGRESSION_RESULT.json").read_text())
    assert result["decision"] == "pass"
    assert result["diagnostics_valid"] is True
    assert result["z_score"] <= 3.0
    assert abs(result["prediction"] - predictions["C"]) < 1.0e-8


def test_bounded_q0_spot_report() -> None:
    report = json.loads((HERE / "independent" / "Q0_SPOT_COMPARISON.json").read_text())
    assert report["pass"] is True
    assert set(report["points"]) == {"1/2", "2"}
    for point in report["points"].values():
        assert {root: point[root]["discrepancy_count"] for root in ("A", "B", "C")} == {
            "A": 0,
            "B": 0,
            "C": 0,
        }


def test_self_contained_report_integrity() -> None:
    manifest = json.loads(SELF_CONTAINED_MANIFEST.read_text())
    report_bytes = SELF_CONTAINED.read_bytes()
    assert sha256(report_bytes).hexdigest() == manifest["sha256"]["report"]
    assert sha256(PRIMARY_UNIT.read_bytes()).hexdigest() == manifest["sha256"]["unit_gram"]
    assert sha256(PRIMARY_TAGGED.read_bytes()).hexdigest() == manifest["sha256"]["layer_separated"]

    report = report_bytes.decode()
    unit_begin = "<!-- BEGIN EMBEDDED UNIT ARTIFACT -->\n```text\n"
    unit_end = "```\n<!-- END EMBEDDED UNIT ARTIFACT -->"
    tagged_begin = "<!-- BEGIN EMBEDDED LAYER-SEPARATED ARTIFACT -->\n```text\n"
    tagged_end = "```\n<!-- END EMBEDDED LAYER-SEPARATED ARTIFACT -->"
    embedded_unit = report.split(unit_begin, 1)[1].split(unit_end, 1)[0]
    embedded_tagged = report.split(tagged_begin, 1)[1].split(tagged_end, 1)[0]
    assert embedded_unit == PRIMARY_UNIT.read_text()
    assert embedded_tagged == PRIMARY_TAGGED.read_text()
    assert manifest["embedded_byte_equality"] == {
        "layer_separated": True,
        "unit_gram": True,
    }

    # Documentation-specific required endpoints.
    for exact_text in (
        r"\mu_0={B\over2A^2}",
        r"\mu_1={4B^2-AC\over24A^5}",
        r"K(y)=F'(F^{-1}(y))",
        r"K_{[0/1]}(y)",
        r"\dot y=2\eta(1-y)K_{[0/1]}(y)",
        r"L_{[0/1]}(t)=(1-y(t))^2",
    ):
        assert exact_text in report


def test_literal_unit_coefficient_map_diff() -> None:
    primary = parse_primary_unit_artifact()
    independent = parse_independent_unit_artifact()
    expected_sizes = {"A": 3, "B": 46, "C": 974}
    for root in ("A", "B", "C"):
        assert len(primary[root]) == expected_sizes[root]
        assert len(independent[root]) == expected_sizes[root]
        if primary[root] != independent[root]:
            keys = sorted(set(primary[root]) | set(independent[root]))
            differences = [
                (key, primary[root].get(key, 0), independent[root].get(key, 0))
                for key in keys
                if primary[root].get(key, 0) != independent[root].get(key, 0)
            ]
            raise AssertionError(f"{root} coefficient mismatch: {differences[:10]}")


def test_literal_tagged_q0_one_coefficient_map_diff() -> None:
    primary = parse_primary_tagged_artifact_q0_one()
    independent = parse_independent_tagged_artifact()
    expected_sizes = {"A": 3, "B": 50, "C": 1045}
    for root in ("A", "B", "C"):
        assert len(primary[root]) == expected_sizes[root]
        assert len(independent[root]) == expected_sizes[root]
        if primary[root] != independent[root]:
            keys = sorted(set(primary[root]) | set(independent[root]))
            differences = [
                (key, primary[root].get(key, 0), independent[root].get(key, 0))
                for key in keys
                if primary[root].get(key, 0) != independent[root].get(key, 0)
            ]
            raise AssertionError(f"tagged {root} coefficient mismatch: {differences[:10]}")


def test_literal_symbolic_q0_coefficient_map_diff() -> None:
    """Compare every explicit Q0 coefficient in the two frozen maps."""

    primary = parse_symbolic_q0_artifact(PRIMARY_SYMBOLIC_Q0_JSON)
    independent = parse_symbolic_q0_artifact(INDEPENDENT_SYMBOLIC_Q0_JSON)
    expected_sizes = {"A": 3, "B": 50, "C": 1045}
    degree_bounds = {"A": 1, "B": 3, "C": 5}
    for root in ("A", "B", "C"):
        assert len(primary[root]) == expected_sizes[root]
        assert len(independent[root]) == expected_sizes[root]
        assert max(degree for (_, degree) in primary[root]) == degree_bounds[root]
        assert max(degree for (_, degree) in independent[root]) == degree_bounds[root]
        if primary[root] != independent[root]:
            keys = sorted(set(primary[root]) | set(independent[root]))
            differences = [
                (key, primary[root].get(key, 0), independent[root].get(key, 0))
                for key in keys
                if primary[root].get(key, 0) != independent[root].get(key, 0)
            ]
            raise AssertionError(f"symbolic-Q0 {root} mismatch: {differences[:10]}")

    payload = json.loads(INDEPENDENT_SYMBOLIC_Q0_JSON.read_text())
    assert payload["degree_bounds"] == degree_bounds
    assert payload["observed_maximum_degrees"] == degree_bounds
    assert payload["interpolation_points"] == ["1/2", "1", "3/2", "2", "5/2", "3"]
    assert payload["holdout_point"] == "7/2"
    assert payload["holdout_discrepancy_counts"] == {"A": 0, "B": 0, "C": 0}

    report = json.loads(SYMBOLIC_Q0_COMPARISON.read_text())
    assert report["comparison_time"] == "after independent interpolation artifact freeze"
    assert report["independent_exact_file_sha256"] == sha256(
        INDEPENDENT_SYMBOLIC_Q0_JSON.read_bytes()
    ).hexdigest()
    assert report["pass"] is True
    assert report["degree_bounds"] == degree_bounds
    assert report["independent_observed_degrees"] == degree_bounds
    assert report["primary_observed_degrees"] == degree_bounds
    assert report["holdout_discrepancy_counts"] == {"A": 0, "B": 0, "C": 0}
    for root in ("A", "B", "C"):
        entry = report["coefficients"][root]
        assert entry["primary_graded_terms"] == expected_sizes[root]
        assert entry["independent_graded_terms"] == expected_sizes[root]
        assert entry["discrepancy_count"] == 0
        assert entry["discrepancies"] == []


def _mp_sum(*polynomials: MomentPolynomial) -> MomentPolynomial:
    answer: MomentPolynomial = {}
    for polynomial in polynomials:
        answer = mp_add(answer, polynomial)
    return answer


def _mp_product(*polynomials: MomentPolynomial) -> MomentPolynomial:
    answer: MomentPolynomial = {(): Fraction(1)}
    for polynomial in polynomials:
        answer = mp_mul(answer, polynomial)
    return answer


def _mp_scale(coefficient: int | Fraction, polynomial: MomentPolynomial) -> MomentPolynomial:
    coefficient = Fraction(coefficient)
    return {key: coefficient * value for key, value in polynomial.items() if coefficient * value}


def _mp_power(polynomial: MomentPolynomial, exponent: int) -> MomentPolynomial:
    answer: MomentPolynomial = {(): Fraction(1)}
    for _ in range(exponent):
        answer = mp_mul(answer, polynomial)
    return answer


def _mp_atom(digits: str) -> MomentPolynomial:
    return {((tuple(int(value) for value in digits)),): Fraction(1)}


def test_documented_compact_B_expands_to_frozen_map() -> None:
    """Literal transcription gate for PRIMARY_GAUSSIAN_NORMAL_FORM.md (2.2--2.5)."""

    one = {(): Fraction(1)}
    d = _mp_atom("020000")
    e = _mp_atom("040000")
    m = _mp_atom("121000")
    j = _mp_atom("030100")
    s = _mp_atom("022000")
    ell = _mp_atom("220000")
    b = _mp_atom("101000")
    r = _mp_atom("010100")
    v = _mp_atom("002000")
    c = _mp_sum(one, d)
    tau = _mp_sum(
        ell,
        _mp_scale(2, _mp_product(c, m)),
        _mp_scale(3, _mp_product(_mp_power(c, 2), s)),
        _mp_product(e, d, v),
    )
    k = _mp_sum(_mp_scale(2, d), b, _mp_product(c, _mp_sum(r, v)))
    kappa = _mp_scale(3, _mp_product(d, _mp_sum(m, j)))
    h3 = _mp_sum(
        _mp_product(_mp_power(c, 2), e),
        tau,
        _mp_scale(2, _mp_product(e, _mp_power(d, 2))),
        _mp_scale(3, _mp_product(_mp_power(d, 2), s)),
        _mp_product(_mp_power(k, 2), ell),
        _mp_product(tau, d),
        _mp_scale(2, _mp_product(d, k, m)),
    )
    s3 = _mp_sum(
        _mp_scale(3, _mp_product(_mp_power(c, 2), m)),
        _mp_scale(3, _mp_product(e, d, b)),
        _mp_scale(3, _mp_product(d, m, _mp_sum(d, b))),
        _mp_scale(3, _mp_product(_mp_power(c, 3), j)),
        _mp_scale(3, _mp_product(c, e, d, r)),
        _mp_scale(3, _mp_product(c, d, m, _mp_sum(r, v))),
        _mp_product(kappa, d),
    )
    documented = _mp_sum(_mp_scale(4, h3), _mp_scale(2, s3))
    frozen = parse_primary_unit_artifact()["B"]
    assert len(documented) == 46
    assert documented == frozen


def run() -> None:
    tests = (
        test_universal_six_family_identity,
        test_raw_width_scaling_exponents,
        test_pade_series_algebra,
        test_frozen_hashes_and_atom_grammar,
        test_literal_unit_coefficient_map_diff,
        test_literal_tagged_q0_one_coefficient_map_diff,
        test_literal_symbolic_q0_coefficient_map_diff,
        test_documented_compact_B_expands_to_frozen_map,
        test_layer_tagged_exact_controls,
        test_preregistered_sine_prediction_and_result,
        test_bounded_q0_spot_report,
        test_self_contained_report_integrity,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")


if __name__ == "__main__":
    run()
