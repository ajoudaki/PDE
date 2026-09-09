"""Exact finite-width Wick oracle for the unnormalised deep-linear network."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


def _double_factorial(power_minus_one: int) -> int:
    answer = 1
    for value in range(power_minus_one, 0, -2):
        answer *= value
    return answer


def _add_into(answer: Polynomial, polynomial: Polynomial) -> None:
    for exponent, coefficient in polynomial.items():
        value = answer.get(exponent, 0) + coefficient
        if value:
            answer[exponent] = value
        elif exponent in answer:
            del answer[exponent]


def _multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for alpha, ca in left.items():
        for beta, cb in right.items():
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            answer[exponent] = answer.get(exponent, 0) + ca * cb
    return answer


def _derivative(polynomial: Polynomial, coordinate: int) -> Polynomial:
    answer: Polynomial = {}
    for exponent, coefficient in polynomial.items():
        power = exponent[coordinate]
        if power:
            reduced = list(exponent)
            reduced[coordinate] -= 1
            key = tuple(reduced)
            answer[key] = answer.get(key, 0) + power * coefficient
    return answer


def _wick(polynomial: Polynomial) -> int:
    answer = 0
    for exponent, coefficient in polynomial.items():
        if any(power % 2 for power in exponent):
            continue
        value = coefficient
        for power in exponent:
            if power:
                value *= _double_factorial(power - 1)
        answer += value
    return answer


def deep_linear_wick(
    hidden_depth: int, width: int, *, order: int = 5, progress: bool = False
) -> tuple[Fraction, ...]:
    """Return exact ``E[D_n^k f_n]`` for the linear depth-H network.

    The unnormalised path polynomial is

        P=sum a_iH W^H_iH,i(H-1) ... W^2_i2,i1 r_i1.

    If ``L=H+1`` is the number of independent parameter blocks, then
    ``f=n^(-L/2)P`` and

        D^k f = n^(k-(k+1)L/2) (grad P.grad)^k P.

    For the nonzero odd derivative orders the exponent is integral.
    """

    if hidden_depth < 1 or width < 1:
        raise ValueError("depth and width must be positive")
    if not 0 <= order <= 5:
        raise ValueError("order must lie from zero through five")
    n = width
    matrix_count = hidden_depth - 1
    dimension = n + matrix_count * n * n + n
    zero = (0,) * dimension

    def variable(index: int) -> Polynomial:
        exponent = [0] * dimension
        exponent[index] = 1
        return {tuple(exponent): 1}

    first = [variable(index) for index in range(n)]
    matrices: list[list[list[Polynomial]]] = []
    cursor = n
    for _ in range(matrix_count):
        matrix = []
        for _i in range(n):
            row = []
            for _j in range(n):
                row.append(variable(cursor))
                cursor += 1
            matrix.append(row)
        matrices.append(matrix)
    readout = [variable(cursor + index) for index in range(n)]

    output: Polynomial = {}
    for path in product(range(n), repeat=hidden_depth):
        term = first[path[0]]
        for matrix_index, matrix in enumerate(matrices):
            term = _multiply(term, matrix[path[matrix_index + 1]][path[matrix_index]])
        term = _multiply(term, readout[path[-1]])
        _add_into(output, term)

    gradient = [_derivative(output, coordinate) for coordinate in range(dimension)]

    def operator(polynomial: Polynomial) -> Polynomial:
        answer: Polynomial = {}
        for coordinate in range(dimension):
            _add_into(answer, _multiply(gradient[coordinate], _derivative(polynomial, coordinate)))
        return answer

    block_count = hidden_depth + 1
    current = output
    result: list[Fraction] = []
    for derivative_order in range(order + 1):
        expectation = _wick(current)
        exponent_twice = 2 * derivative_order - (derivative_order + 1) * block_count
        if expectation == 0:
            result.append(Fraction(0))
        else:
            if exponent_twice % 2:
                raise AssertionError("nonzero Gaussian expectation has half-integral n scaling")
            exponent = exponent_twice // 2
            result.append(
                Fraction(expectation * n**exponent, 1)
                if exponent >= 0
                else Fraction(expectation, n ** (-exponent))
            )
        if progress:
            print(
                f"H={hidden_depth} n={width} k={derivative_order} "
                f"terms={len(current)} expectation={result[-1]}",
                flush=True,
            )
        if derivative_order != order:
            current = operator(current)
    return tuple(result)


if __name__ == "__main__":
    for depth in (2, 3, 4):
        for width in (1, 2):
            print(deep_linear_wick(depth, width, progress=True))

