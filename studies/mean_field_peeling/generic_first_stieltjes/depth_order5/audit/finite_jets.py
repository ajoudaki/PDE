"""Producer-independent finite-width jets for arbitrary fixed hidden depth.

Route A expands the exact moving feature ODE in ordinary time coefficients.
Route B expands the original network in raw parameter perturbations and
applies ``n grad(f).grad`` as a sparse multivariate polynomial operator.
The two implementations share only the activation derivative oracle and the
literal network convention frozen in AUDIT_CONTRACT.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import cos, factorial, isqrt, sin, sqrt, tanh
from random import Random
from typing import Callable, Sequence


Number = int | float | Fraction
Vector = list[Number]
Matrix = list[list[Number]]


@dataclass(frozen=True)
class Activation:
    name: str
    derivatives: Callable[[Number, int], list[Number]]


def polynomial_activation(coefficients: Sequence[Number], name: str = "polynomial") -> Activation:
    coefficients = tuple(coefficients)

    def derivatives(x: Number, maximum: int) -> list[Number]:
        answer: list[Number] = []
        for order in range(maximum + 1):
            value: Number = 0
            for power in range(order, len(coefficients)):
                multiplier = factorial(power) // factorial(power - order)
                value += coefficients[power] * multiplier * x ** (power - order)
            answer.append(value)
        return answer

    return Activation(name, derivatives)


def sine_activation() -> Activation:
    def derivatives(x: Number, maximum: int) -> list[Number]:
        xf = float(x)
        cycle = (sin(xf), cos(xf), -sin(xf), -cos(xf))
        return [cycle[order % 4] for order in range(maximum + 1)]

    return Activation("sin", derivatives)


def normalized_sine_activation() -> Activation:
    normalization = sqrt((1.0 - __import__("math").exp(-2.0)) / 2.0)
    base = sine_activation()

    def derivatives(x: Number, maximum: int) -> list[Number]:
        return [value / normalization for value in base.derivatives(x, maximum)]

    return Activation("normalized_sine", derivatives)


def _poly_derivative(coefficients: list[Number]) -> list[Number]:
    return [index * coefficients[index] for index in range(1, len(coefficients))] or [0]


def _poly_multiply(left: list[Number], right: list[Number]) -> list[Number]:
    answer: list[Number] = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def _poly_evaluate(coefficients: list[Number], x: Number) -> Number:
    answer: Number = 0
    for coefficient in reversed(coefficients):
        answer = answer * x + coefficient
    return answer


def tanh_activation() -> Activation:
    # P_r(tanh x)=d^r tanh(x)/dx^r and
    # P_(r+1)(t)=(1-t^2)P_r'(t).
    derivative_polynomials: list[list[Number]] = [[0, 1]]
    for _ in range(10):
        derivative_polynomials.append(
            _poly_multiply(_poly_derivative(derivative_polynomials[-1]), [1, 0, -1])
        )

    def derivatives(x: Number, maximum: int) -> list[Number]:
        value = tanh(float(x))
        return [_poly_evaluate(derivative_polynomials[order], value) for order in range(maximum + 1)]

    return Activation("tanh", derivatives)


@dataclass(frozen=True)
class Parameters:
    first: Vector
    matrices: list[Matrix]  # raw W^2,...,W^H
    readout: Vector

    @property
    def width(self) -> int:
        return len(self.first)

    @property
    def depth(self) -> int:
        return len(self.matrices) + 1


def random_parameters(depth: int, width: int, seed: int) -> Parameters:
    if depth < 1 or width < 1:
        raise ValueError("depth and width must be positive")
    rng = Random(seed)
    first = [rng.gauss(0.0, 1.0) for _ in range(width)]
    matrices = [
        [[rng.gauss(0.0, 1.0) for _ in range(width)] for _ in range(width)]
        for _ in range(depth - 1)
    ]
    readout = [rng.gauss(0.0, 1.0) for _ in range(width)]
    return Parameters(first, matrices, readout)


def _sqrt_q0(q0: Number) -> Number:
    if isinstance(q0, Fraction):
        numerator = isqrt(q0.numerator)
        denominator = isqrt(q0.denominator)
        if numerator * numerator == q0.numerator and denominator * denominator == q0.denominator:
            return Fraction(numerator, denominator)
    if q0 == 1:
        return type(q0)(1)
    return sqrt(float(q0))


def _series_mul(left: Sequence[Number], right: Sequence[Number], order: int) -> list[Number]:
    return [
        sum((left[p] * right[k - p] for p in range(k + 1)), 0)
        for k in range(order + 1)
    ]


def _series_compose(
    coefficients: Sequence[Number], activation: Activation, derivative_order: int, order: int
) -> list[Number]:
    """Ordinary Taylor coefficients of phi^(s)(x(t))."""

    base = coefficients[0]
    derivatives = activation.derivatives(base, derivative_order + order)
    delta = [0] + list(coefficients[1 : order + 1])
    answer: list[Number] = [0] * (order + 1)
    power: list[Number] = [1] + [0] * order
    for multiplicity in range(order + 1):
        if multiplicity:
            power = _series_mul(power, delta, order)
        derivative_value = derivatives[derivative_order + multiplicity]
        if derivative_value == 0:
            continue
        scalar = derivative_value / factorial(multiplicity)
        for k in range(order + 1):
            answer[k] += scalar * power[k]
    return answer


def _forward_series(
    z1: list[list[Number]],
    matrices: list[list[list[list[Number]]]],
    activation: Activation,
    order: int,
) -> tuple[list[list[list[Number]]], list[list[list[Number]]]]:
    """Return z^ell and h^ell series through ``order``."""

    width = len(z1)
    z_layers: list[list[list[Number]]] = [
        [list(z1[i][: order + 1]) for i in range(width)]
    ]
    h_layers: list[list[list[Number]]] = [
        [_series_compose(z_layers[0][i], activation, 0, order) for i in range(width)]
    ]
    for matrix in matrices:
        previous = h_layers[-1]
        z_current = [[0] * (order + 1) for _ in range(width)]
        for i in range(width):
            for k in range(order + 1):
                z_current[i][k] = sum(
                    (
                        matrix[i][j][p] * previous[j][k - p]
                        for j in range(width)
                        for p in range(k + 1)
                    ),
                    0,
                )
        z_layers.append(z_current)
        h_layers.append(
            [_series_compose(z_current[i], activation, 0, order) for i in range(width)]
        )
    return z_layers, h_layers


def moving_flow_jet(
    parameters: Parameters,
    activation: Activation,
    *,
    q0: Number = 1,
    order: int = 5,
) -> tuple[Number, ...]:
    """Exact ordinary-series expansion of the finite-width feature flow."""

    if order > 5:
        raise ValueError("this hostile oracle is frozen through order five")
    n = parameters.width
    root_n = sqrt(n) if n != 1 else 1
    root_q0 = _sqrt_q0(q0)
    z1 = [[0] * (order + 1) for _ in range(n)]
    for i, value in enumerate(parameters.first):
        z1[i][0] = root_q0 * value
    matrices = [
        [
            [[raw[i][j] / root_n] + [0] * order for j in range(n)]
            for i in range(n)
        ]
        for raw in parameters.matrices
    ]
    readout = [[value] + [0] * order for value in parameters.readout]

    for k in range(order):
        z_layers, h_layers = _forward_series(z1, matrices, activation, k)
        hp_layers = [
            [_series_compose(z_layers[layer][i], activation, 1, k) for i in range(n)]
            for layer in range(parameters.depth)
        ]

        backward: list[list[list[Number]]] = [None] * parameters.depth  # type: ignore[list-item]
        backward[-1] = [
            _series_mul(readout[i][: k + 1], hp_layers[-1][i], k)
            for i in range(n)
        ]
        for layer in range(parameters.depth - 2, -1, -1):
            matrix = matrices[layer]
            transported = [[0] * (k + 1) for _ in range(n)]
            for j in range(n):
                for degree in range(k + 1):
                    transported[j][degree] = sum(
                        (
                            matrix[i][j][p] * backward[layer + 1][i][degree - p]
                            for i in range(n)
                            for p in range(degree + 1)
                        ),
                        0,
                    )
            backward[layer] = [
                _series_mul(hp_layers[layer][j], transported[j], k)
                for j in range(n)
            ]

        inverse = Fraction(1, k + 1) if all(
            isinstance(value, (int, Fraction)) for value in parameters.first
        ) else 1.0 / (k + 1)
        for i in range(n):
            z1[i][k + 1] = q0 * backward[0][i][k] * inverse
            readout[i][k + 1] = h_layers[-1][i][k] * inverse

        for matrix_index, matrix in enumerate(matrices):
            left = backward[matrix_index + 1]
            right = h_layers[matrix_index]
            for i in range(n):
                for j in range(n):
                    coefficient = sum(
                        (left[i][p] * right[j][k - p] for p in range(k + 1)), 0
                    )
                    matrix[i][j][k + 1] = coefficient * inverse / n

    _, h_layers = _forward_series(z1, matrices, activation, order)
    output_coefficients = [
        sum(
            (
                readout[i][p] * h_layers[-1][i][k - p]
                for i in range(n)
                for p in range(k + 1)
            ),
            0,
        )
        / n
        for k in range(order + 1)
    ]
    return tuple(factorial(k) * output_coefficients[k] for k in range(order + 1))


# Route B: raw multivariate Taylor algebra.
Exponent = tuple[int, ...]
SparsePolynomial = dict[Exponent, Number]


def _mp_add(*polynomials: SparsePolynomial) -> SparsePolynomial:
    answer: SparsePolynomial = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            answer[exponent] = answer.get(exponent, 0) + coefficient
    return {key: value for key, value in answer.items() if value != 0}


def _mp_scale(polynomial: SparsePolynomial, scalar: Number) -> SparsePolynomial:
    return {key: scalar * value for key, value in polynomial.items() if scalar * value != 0}


def _mp_mul(
    left: SparsePolynomial, right: SparsePolynomial, maximum_degree: int
) -> SparsePolynomial:
    answer: SparsePolynomial = {}
    for alpha, ca in left.items():
        for beta, cb in right.items():
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            if sum(exponent) <= maximum_degree:
                answer[exponent] = answer.get(exponent, 0) + ca * cb
    return {key: value for key, value in answer.items() if value != 0}


def _mp_derivative(polynomial: SparsePolynomial, coordinate: int) -> SparsePolynomial:
    answer: SparsePolynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[coordinate]
        if power:
            reduced = list(exponent)
            reduced[coordinate] -= 1
            key = tuple(reduced)
            answer[key] = answer.get(key, 0) + power * coefficient
    return answer


def _mp_constant(polynomial: SparsePolynomial, dimension: int) -> Number:
    return polynomial.get((0,) * dimension, 0)


def _mp_activation(
    argument: SparsePolynomial,
    activation: Activation,
    dimension: int,
    maximum_degree: int,
) -> SparsePolynomial:
    zero = (0,) * dimension
    base = argument.get(zero, 0)
    delta = dict(argument)
    delta.pop(zero, None)
    derivatives = activation.derivatives(base, maximum_degree)
    answer: SparsePolynomial = {}
    power: SparsePolynomial = {zero: 1}
    for multiplicity in range(maximum_degree + 1):
        if multiplicity:
            power = _mp_mul(power, delta, maximum_degree)
        if derivatives[multiplicity] == 0:
            continue
        answer = _mp_add(
            answer,
            _mp_scale(power, derivatives[multiplicity] / factorial(multiplicity)),
        )
    return answer


def raw_parameter_jet(
    parameters: Parameters,
    activation: Activation,
    *,
    q0: Number = 1,
    order: int = 5,
) -> tuple[Number, ...]:
    """Apply the raw finite-dimensional operator to a multivariate Taylor jet."""

    if order > 5:
        raise ValueError("this hostile oracle is frozen through order five")
    n = parameters.width
    depth = parameters.depth
    dimension = n + (depth - 1) * n * n + n
    zero = (0,) * dimension

    flat_values: list[Number] = list(parameters.first)
    for matrix in parameters.matrices:
        for row in matrix:
            flat_values.extend(row)
    flat_values.extend(parameters.readout)

    variables: list[SparsePolynomial] = []
    for coordinate, base in enumerate(flat_values):
        exponent = [0] * dimension
        exponent[coordinate] = 1
        variables.append({zero: base, tuple(exponent): 1})

    cursor = 0
    first = variables[cursor : cursor + n]
    cursor += n
    raw_matrices: list[list[list[SparsePolynomial]]] = []
    for _ in range(depth - 1):
        matrix = []
        for _i in range(n):
            matrix.append(variables[cursor : cursor + n])
            cursor += n
        raw_matrices.append(matrix)
    readout = variables[cursor : cursor + n]

    root_q0 = _sqrt_q0(q0)
    root_n = sqrt(n) if n != 1 else 1
    h = [
        _mp_activation(_mp_scale(first[i], root_q0), activation, dimension, order)
        for i in range(n)
    ]
    for raw_matrix in raw_matrices:
        z: list[SparsePolynomial] = []
        for i in range(n):
            terms = [
                _mp_mul(raw_matrix[i][j], h[j], order) for j in range(n)
            ]
            inverse_root_n: Number = Fraction(1, 1) if n == 1 else 1.0 / root_n
            z.append(_mp_scale(_mp_add(*terms), inverse_root_n))
        h = [_mp_activation(value, activation, dimension, order) for value in z]
    output = _mp_scale(
        _mp_add(*[_mp_mul(readout[i], h[i], order) for i in range(n)]),
        Fraction(1, n),
    )

    gradient = [_mp_derivative(output, coordinate) for coordinate in range(dimension)]
    current = output
    values: list[Number] = []
    for derivative_order in range(order + 1):
        values.append(_mp_constant(current, dimension))
        if derivative_order == order:
            break
        retained_degree = order - derivative_order - 1
        terms = [
            _mp_mul(
                gradient[coordinate],
                _mp_derivative(current, coordinate),
                retained_degree,
            )
            for coordinate in range(dimension)
        ]
        current = _mp_scale(_mp_add(*terms), n)
    return tuple(values)


def scaled_error(left: Sequence[Number], right: Sequence[Number]) -> float:
    return max(
        abs(float(a) - float(b)) / max(1.0, abs(float(a)), abs(float(b)))
        for a, b in zip(left, right)
    )


def direct_first_derivative_energy(
    parameters: Parameters, activation: Activation, *, q0: Number = 1
) -> Number:
    """Compute ``D_n f=n||grad f||^2`` from raw forward/backward factors."""

    n = parameters.width
    root_n = sqrt(n) if n != 1 else 1
    root_q0 = _sqrt_q0(q0)
    z_layers: list[Vector] = [[root_q0 * value for value in parameters.first]]
    h_layers: list[Vector] = [
        [activation.derivatives(value, 0)[0] for value in z_layers[0]]
    ]
    hp_layers: list[Vector] = [
        [activation.derivatives(value, 1)[1] for value in z_layers[0]]
    ]
    for raw_matrix in parameters.matrices:
        previous = h_layers[-1]
        z = [
            sum((raw_matrix[i][j] * previous[j] for j in range(n)), 0) / root_n
            for i in range(n)
        ]
        z_layers.append(z)
        h_layers.append([activation.derivatives(value, 0)[0] for value in z])
        hp_layers.append([activation.derivatives(value, 1)[1] for value in z])

    backward: list[Vector] = [None] * parameters.depth  # type: ignore[list-item]
    backward[-1] = [
        parameters.readout[i] * hp_layers[-1][i] for i in range(n)
    ]
    for layer in range(parameters.depth - 2, -1, -1):
        raw_matrix = parameters.matrices[layer]
        transported = [
            sum((raw_matrix[i][j] * backward[layer + 1][i] for i in range(n)), 0)
            / root_n
            for j in range(n)
        ]
        backward[layer] = [
            hp_layers[layer][j] * transported[j] for j in range(n)
        ]

    energy: Number = sum((value * value for value in h_layers[-1]), 0) / n
    energy += q0 * sum((value * value for value in backward[0]), 0) / n
    for layer in range(1, parameters.depth):
        left_norm = sum((value * value for value in backward[layer]), 0)
        right_norm = sum((value * value for value in h_layers[layer - 1]), 0)
        energy += left_norm * right_norm / (n * n)
    return energy
