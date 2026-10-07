"""Deterministic finite-transform checks, not a neural training experiment."""

import cmath
import math


def fft(values, inverse=False):
    size = len(values)
    if size == 1:
        return [complex(values[0])]
    assert size % 2 == 0
    even = fft(values[::2], inverse)
    odd = fft(values[1::2], inverse)
    sign = 1 if inverse else -1
    result = [0j] * size
    for k in range(size // 2):
        term = cmath.exp(sign * 2j * math.pi * k / size) * odd[k]
        result[k] = even[k] + term
        result[k + size // 2] = even[k] - term
    return result


def analyze(values):
    size = len(values)
    mirrored = [0j] * (4 * size)
    for j, value in enumerate(values):
        mirrored[2 * j + 1] = value
        mirrored[4 * size - (2 * j + 1)] = value
    spectrum = fft(mirrored)
    return [spectrum[0].real / (2 * size)] + [
        spectrum[k].real / size for k in range(1, size)
    ]


def primitive(coefficients):
    size = len(coefficients)
    result = [0.0] * (size + 1)
    result[1] += coefficients[0]
    if size > 1:
        result[2] += coefficients[1] / 4
    for k in range(2, size):
        result[k + 1] += coefficients[k] / (2 * (k + 1))
        result[k - 1] -= coefficients[k] / (2 * (k - 1))
    result[0] = -sum(value * (-1) ** k for k, value in enumerate(result[1:], 1))
    return result


def synthesize_at_nodes(coefficients, size):
    assert len(coefficients) <= size + 1
    spectrum = [0j] * (4 * size)
    spectrum[0] = coefficients[0]
    for k in range(1, min(size, len(coefficients))):
        spectrum[k] = spectrum[4 * size - k] = coefficients[k] / 2
    values = fft(spectrum, inverse=True)  # Unnormalized inverse sum.
    return [values[2 * j + 1].real for j in range(size)]


def evaluate(coefficients, x):
    total = coefficients[0]
    previous, current = 1.0, x
    for k in range(1, len(coefficients)):
        total += coefficients[k] * current
        previous, current = current, 2 * x * current - previous
    return total


def run():
    maximum_error = 0.0
    checked = 0
    for size in (8, 16, 32, 64):
        angles = [(2 * j + 1) * math.pi / (2 * size) for j in range(size)]
        nodes = [math.cos(angle) for angle in angles]
        values = [math.sin(j + 0.3) + 0.25 * math.cos(2 * j) for j in range(size)]
        coefficients = analyze(values)
        direct = [sum(values) / size] + [
            2 * sum(v * math.cos(k * angle) for v, angle in zip(values, angles)) / size
            for k in range(1, size)
        ]
        errors = [abs(a - b) for a, b in zip(coefficients, direct)]
        errors += [abs(a - b) for a, b in zip(synthesize_at_nodes(coefficients, size), values)]

        integrated = primitive(coefficients)
        errors += [
            abs(a - evaluate(integrated, x))
            for a, x in zip(synthesize_at_nodes(integrated, size), nodes)
        ]
        errors.append(abs(evaluate(integrated, -1)))

        square_primitive = primitive(analyze([x * x for x in nodes]))
        errors += [
            abs(evaluate(square_primitive, x) - (x**3 + 1) / 3)
            for x in (-1, -0.73, 0, 0.42, 1)
        ]

        # The highest integrated coefficient vanishes at iteration nodes,
        # but is indispensable at the panel endpoint.
        highest = primitive([0.0] * (size - 1) + [1.0])
        assert abs(highest[size] - 1 / (2 * size)) < 1e-15
        errors += [
            abs(a - evaluate(highest, x))
            for a, x in zip(synthesize_at_nodes(highest, size), nodes)
        ]
        assert abs(evaluate(highest, 1) - evaluate(highest[:-1], 1)) > 0.4 / size

        maximum_error = max(maximum_error, max(errors))
        assert max(errors) < 1e-11, (size, max(errors))
        checked += len(errors) + 2
    print(f"PASS: {checked} scalar comparisons; maximum absolute error {maximum_error:.3e}")
    print("Checked DCT analysis, synthesis, integration, and retained endpoint coefficient.")
    print("No dense-network simulation, timing benchmark, or finite-precision stability claim.")


if __name__ == "__main__":
    run()
