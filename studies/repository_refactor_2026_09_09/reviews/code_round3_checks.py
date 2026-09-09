"""Independent, bounded review evidence. Run with -B and PYTHONPATH=code.

This review artifact does not edit inputs, write files, or use the network.
Known counterexamples are assertions of the intended result, so they FAIL.
"""

from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import atan, prod, sqrt, tanh
from numbers import Real
import sys
import warnings

import numpy as np

from pde import (
    ARCTAN, IDENTITY, TANH, Activation, Parameters, backward, flow_velocity,
    forward, gaussian_moment, gd_step, kernel, kernel_blocks, loss, loss_gradients,
)


results = []


def check(name, function):
    try:
        detail = function()
    except Exception as error:
        results.append((name, False))
        print(f"FAIL {name}: {type(error).__name__}: {error}")
    else:
        results.append((name, True))
        print(f"PASS {name}: {detail}")


def same(actual, expected):
    if actual != expected:
        raise AssertionError(f"actual={actual!r}, expected={expected!r}")


def blocks(state):
    return state.weights + (state.readout,)


def unsigned_step(dtype):
    step = dtype(1)
    assert isinstance(step, Real) and np.isfinite(step) and step >= 0
    state = Parameters(([[1.0]],), [1.0])
    with warnings.catch_warnings(record=True) as observed:
        warnings.simplefilter("always")
        updated = gd_step(state, [[1.0]], [0.0], step, IDENTITY)
    value = updated.weights[0][0, 0]
    assert value == -1.0, (f"eta={dtype.__name__}(1), W={value!r}, "
                           f"readout={updated.readout[0]!r}, expected=-1.0; "
                           f"warnings={[str(w.message) for w in observed]}")


def normalized_kernel(which):
    tiny_root, rate = 2.0**-537, 2.0**1023
    same(float(np.array([tiny_root]) @ np.array([tiny_root])), 2.0**-1074)
    if which == "readout":
        state = Parameters(([[tiny_root], [0.0]],), [0.0, 0.0])
        actual = kernel_blocks(state, [[1.0]], IDENTITY, kappas=[1.0, rate])[-1, 0, 0]
        expected = 2.0**-52
    elif which == "input":
        state = Parameters(([[0.0, 0.0, 0.0, 0.0]],), [1.0])
        actual = kernel_blocks(state, [[tiny_root], [0.0], [0.0], [0.0]],
                               IDENTITY, kappas=[rate, 1.0])[0, 0, 0]
        expected = 2.0**-53
    elif which == "delta":
        state = Parameters(([[0.0], [0.0]],), [tiny_root, 0.0])
        actual = kernel_blocks(state, [[1.0]], IDENTITY, kappas=[rate, 1.0])[0, 0, 0]
        expected = 2.0**-52
    else:
        state = Parameters(([[tiny_root], [0.0]], np.zeros((2, 2))), [1.0, 0.0])
        actual = kernel_blocks(state, [[1.0]], IDENTITY, kappas=[1.0, rate, 1.0])[1, 0, 0]
        expected = 2.0**-53
    same(actual, expected)


def input_normalization():
    state = Parameters(([[2.0**1023, 0.0, 0.0, 0.0]],), [1.0])
    inputs = np.array([[2.0**-1074], [0.0], [0.0], [0.0]])
    same(float((state.weights[0] @ inputs)[0, 0]), 2.0**-51)
    same(float(((state.weights[0] @ inputs) / 2.0)[0, 0]), 2.0**-52)
    actual = forward(state, inputs, IDENTITY).output[0]
    actual_loss = loss(state, inputs, [0.0], IDENTITY)
    assert actual == 2.0**-52 and actual_loss == 2.0**-104, (
        f"forward={actual!r}, expected={2.0**-52!r}; "
        f"loss={actual_loss!r}, expected={2.0**-104!r}")


def normalized_update(which, target):
    small, rate = 2.0**-1074, 2.0**1023
    if target == "first":
        state = Parameters((np.zeros((4, 1)),), np.ones(4))
        inputs, rates = [[small]], [rate, 1.0]
    else:
        state = Parameters((np.full((4, 1), small),), np.zeros(4))
        inputs, rates = [[1.0]], [1.0, rate]
    if which == "flow":
        result = flow_velocity(state, inputs, [-1.0], IDENTITY, kappas=rates)
    else:
        result = gd_step(state, inputs, [-1.0], 1.0, IDENTITY, kappas=rates)
    actual = result.weights[0][0, 0] if target == "first" else result.readout[0]
    same(actual, -2.0**-50)


def overflowing_gradient(which):
    state = Parameters(([[0.0]],), [1.0])
    with np.errstate(over="ignore", invalid="ignore"):
        try:
            if which == "flow":
                result = flow_velocity(state, [[1.0]], [-2.0**1023], IDENTITY,
                                       kappas=[0.25, 1.0])
            else:
                result = gd_step(state, [[1.0]], [-2.0**1023], 0.25, IDENTITY)
        except ValueError as error:
            raise AssertionError(f"raised {error!r}; finite expected=-2**1022") from error
    same(result.weights[0][0, 0], -2.0**1022)


class Dual:
    """Forward-mode derivative oracle, independent of library backpropagation."""

    def __init__(self, value, derivative):
        self.value, self.derivative = float(value), derivative

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.value + other.value, self.derivative + other.derivative)
        return Dual(self.value + other, self.derivative)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.value * other.value,
                        self.derivative * other.value + self.value * other.derivative)
        return Dual(self.value * other, self.derivative * other)

    __rmul__ = __mul__


POLY = Activation("smooth_polynomial", lambda z: 0.2 + z + z**3 / 20.0,
                  lambda z: 1.0 + 3.0 * z**2 / 20.0)


def ad_activation(z, kind):
    if kind == 0:
        value = tanh(z.value)
        return Dual(value, (1.0 - value * value) * z.derivative)
    if kind == 1:
        return Dual(atan(z.value), z.derivative / (1.0 + z.value * z.value))
    return 0.2 + z + z * z * z * 0.05


def dual_outputs(state, inputs):
    arrays = blocks(state)
    count = sum(a.size for a in arrays)
    basis = np.eye(count)
    offset, dual_arrays = 0, []
    for array in arrays:
        entries = [Dual(v, basis[offset + i]) for i, v in enumerate(array.flat)]
        dual_arrays.append(np.array(entries, dtype=object).reshape(array.shape))
        offset += array.size
    outputs = []
    for sample in range(inputs.shape[1]):
        h = list(inputs[:, sample] / sqrt(inputs.shape[0]))
        for layer, weight in enumerate(dual_arrays[:-1]):
            h = [ad_activation(sum(weight[i, j] * h[j] for j in range(len(h))), layer % 3)
                 for i in range(state.width)]
        outputs.append(sum(a * v for a, v in zip(dual_arrays[-1], h)) * (1.0 / state.width))
    return np.array([v.value for v in outputs]), np.array([v.derivative for v in outputs])


def forward_mode_audit():
    rng = np.random.default_rng(905031)
    cases, coordinates = 0, 0
    for depth, width, dimension in product((1, 2, 4), (1, 2, 3), (1, 4)):
        state = Parameters((rng.normal(0, 0.3, (width, dimension)),) + tuple(
            rng.normal(0, 0.3, (width, width)) for _ in range(depth - 1)),
            rng.normal(0, 0.4, width))
        v = rng.normal(0, 0.4, dimension)
        x = np.stack((v, -v, v, np.zeros_like(v)), axis=1)
        y = np.array([0.3, -0.7, -0.4, 0.9])
        activations = tuple((TANH, ARCTAN, POLY)[i % 3] for i in range(depth))
        rates = np.linspace(0.2, 1.7, depth + 1)
        mobilities = rates.copy()
        mobilities[[0, -1]] *= width
        f, jacobian = dual_outputs(state, x)
        np.testing.assert_allclose(forward(state, x, activations).output, f, rtol=2e-12, atol=1e-14)
        residual = f - y
        expected_grad = (2.0 / y.size) * jacobian.T @ residual
        expected_blocks = []
        expected_velocity = []
        offset = 0
        for array, mobility in zip(blocks(state), mobilities):
            local = jacobian[:, offset:offset + array.size]
            expected_blocks.append(mobility * local @ local.T)
            expected_velocity.extend(-mobility * expected_grad[offset:offset + array.size])
            offset += array.size
        actual_grad = np.concatenate([a.ravel() for a in blocks(loss_gradients(state, x, y, activations))])
        actual_vel = np.concatenate([a.ravel() for a in blocks(flow_velocity(state, x, y, activations, kappas=rates))])
        np.testing.assert_allclose(actual_grad, expected_grad, rtol=3e-12, atol=1e-14)
        np.testing.assert_allclose(actual_vel, expected_velocity, rtol=3e-12, atol=1e-14)
        actual_kernel = kernel_blocks(state, x, activations, kappas=rates)
        np.testing.assert_allclose(actual_kernel, expected_blocks, rtol=3e-12, atol=1e-14)
        updated = gd_step(state, x, y, 0.07, activations, kappas=rates)
        before = np.concatenate([a.ravel() for a in blocks(state)])
        after = np.concatenate([a.ravel() for a in blocks(updated)])
        np.testing.assert_allclose(after, before + 0.07 * np.array(expected_velocity), rtol=3e-12, atol=1e-14)
        np.testing.assert_allclose(jacobian @ actual_vel, -2.0 * actual_kernel.sum(axis=0) @ residual / y.size,
                                   rtol=3e-12, atol=1e-14)
        assert np.min(np.linalg.eigvalsh(actual_kernel)) >= -1e-13
        cases += 1
        coordinates += jacobian.shape[1]
    return f"{cases} networks, {coordinates} parameter coordinates; forward/gradient/flow/GD/kernel/output flow/PSD"


def gaussian_scalar_moment(degree):
    return Q(0) if degree % 2 else Q(prod(range(1, degree, 2)))


def latent_polynomial_moment(mixing, powers):
    rank = len(mixing[0])
    polynomial = {(0,) * rank: Q(1)}
    for row, power in zip(mixing, powers):
        for _ in range(power):
            expanded = {}
            for exponent, coefficient in polynomial.items():
                for j, entry in enumerate(row):
                    raised = list(exponent)
                    raised[j] += 1
                    key = tuple(raised)
                    expanded[key] = expanded.get(key, Q(0)) + coefficient * entry
            polynomial = expanded
    return sum((coefficient * prod(gaussian_scalar_moment(p) for p in exponent)
                for exponent, coefficient in polynomial.items()), Q(0))


def exact_wick_audit():
    rng = np.random.default_rng(905032)
    for case in range(120):
        dimension, rank = 1 + case % 4, 1 + (case // 4) % 3
        mixing = [[Q(int(rng.integers(-2, 3)), int(rng.integers(1, 4)))
                   for _ in range(rank)] for _ in range(dimension)]
        covariance = [[sum((a * b for a, b in zip(u, v)), Q(0)) for v in mixing] for u in mixing]
        powers = [0] * dimension
        for _ in range(case % 9):
            powers[int(rng.integers(dimension))] += 1
        expected = latent_polynomial_moment(mixing, powers)
        same(gaussian_moment(covariance, powers), expected)
        order = list(reversed(range(dimension)))
        same(gaussian_moment([[covariance[i][j] for j in order] for i in order],
                             [powers[i] for i in order]), expected)
    return "120 independent latent-polynomial expansions, degrees 0..8, dimensions 1..4, ranks <=3; 120 permutations"


def determinant(matrix):
    total = Q(0)
    for order in permutations(range(len(matrix))):
        inversions = sum(order[i] > order[j] for i in range(len(order)) for j in range(i + 1, len(order)))
        total += (-1)**inversions * prod(matrix[i][j] for i, j in enumerate(order))
    return total


def all_principal_minors_nonnegative(matrix):
    for size in range(1, len(matrix) + 1):
        for subset in combinations(range(len(matrix)), size):
            if determinant([[matrix[i][j] for j in subset] for i in subset]) < 0:
                return False
    return True


def exact_psd_audit():
    matrices, calls, accepted = 0, 0, 0
    for dimension, values in ((2, (-2, -1, 0, 1, 2)), (3, (-1, 0, 1))):
        positions = [(i, j) for i in range(dimension) for j in range(i, dimension)]
        for entries in product(values, repeat=len(positions)):
            matrix = [[Q(0) for _ in range(dimension)] for _ in range(dimension)]
            for (i, j), value in zip(positions, entries):
                matrix[i][j] = matrix[j][i] = Q(value)
            expected = all_principal_minors_nonnegative(matrix)
            for degree in (0, 1, 2):
                try:
                    gaussian_moment(matrix, [degree] + [0] * (dimension - 1))
                    actual = True
                except ValueError:
                    actual = False
                same(actual, expected)
                calls += 1
            matrices += 1
            accepted += expected
    for sign in (-1, 0, 1):
        matrix = [[1, 1], [1, 1 + sign * Q(1, 10**80)]]
        try:
            gaussian_moment(matrix, [0, 0])
            actual = True
        except ValueError:
            actual = False
        same(actual, sign >= 0)
    return f"{matrices} matrices ({accepted} PSD); {calls} zero/odd/even validation calls; 3 exact 1e-80 boundary cases"


def gaussian_conditioning_algebra():
    rng = np.random.default_rng(905033)
    n = 4
    for left_rank, right_rank in ((0, 0), (0, 2), (2, 0), (1, 2), (3, 2), (4, 3)):
        u = np.linalg.qr(rng.normal(size=(n, n)))[0][:, :left_rank]
        v = np.linalg.qr(rng.normal(size=(n, n)))[0][:, :right_rank]
        w = rng.normal(size=(n, n))
        y, r = w @ v, w.T @ u
        pu, pv = u @ u.T, v @ v.T
        mean = y @ v.T + u @ r.T @ (np.eye(n) - pv)
        remaining = np.kron(np.eye(n) - pu, np.eye(n) - pv)
        constraints = np.array([
            np.concatenate(((basis.reshape(n, n) @ v).ravel(),
                            (basis.reshape(n, n).T @ u).ravel()))
            for basis in np.eye(n*n)
        ]).T
        observed = np.concatenate((y.ravel(), r.ravel()))
        inverse = np.linalg.pinv(constraints)
        np.testing.assert_allclose(mean.ravel(), inverse @ observed, rtol=2e-12, atol=2e-14)
        np.testing.assert_allclose(remaining, np.eye(n*n) - inverse @ constraints,
                                   rtol=2e-12, atol=2e-14)
        np.testing.assert_allclose(mean @ v, y, rtol=2e-12, atol=2e-14)
        np.testing.assert_allclose(mean.T @ u, r, rtol=2e-12, atol=2e-14)
        np.testing.assert_allclose(constraints @ remaining, 0.0, atol=2e-14)
    return "6 finite two-direction conditioning cases, including empty and full spans; vectorized affine projection agrees"


def callback_audit():
    scratch = np.empty((2, 3))
    retained = []

    def value(z):
        retained.append(z)
        np.tanh(z, out=z)
        scratch[:] = z
        return scratch

    def derivative(z):
        retained.append(z)
        z[:] = 1.0 / np.cosh(z)**2
        scratch[:] = z
        return scratch

    buffered = Activation("shared_value_and_derivative_buffer", value, derivative)
    state = Parameters(([[0.2, -0.1], [0.3, 0.4]], [[0.4, 0.1], [-0.2, 0.6]],
                        [[0.7, -0.1], [0.3, 0.5]]), [0.8, -0.3])
    inputs, labels = np.array([[0.2, -0.6, 0.2], [0.7, 0.1, 0.7]]), np.array([0.1, -0.2, 0.8])
    saved = [a.copy() for a in blocks(state)] + [inputs.copy(), labels.copy()]
    f = forward(state, inputs, buffered)
    reference = forward(state, inputs, TANH)
    for actual, expected in zip(f.preactivations + f.hidden + (f.output,),
                                reference.preactivations + reference.hidden + (reference.output,)):
        np.testing.assert_allclose(actual, expected, rtol=2e-14, atol=1e-15)
    for function in (loss_gradients, flow_velocity):
        for actual, expected in zip(blocks(function(state, inputs, labels, buffered)),
                                    blocks(function(state, inputs, labels, TANH))):
            np.testing.assert_allclose(actual, expected, rtol=2e-14, atol=1e-15)
    np.testing.assert_allclose(kernel(state, inputs, buffered), kernel(state, inputs, TANH),
                               rtol=2e-14, atol=1e-15)
    for actual, expected in zip(blocks(gd_step(state, inputs, labels, 0.1, buffered)),
                                blocks(gd_step(state, inputs, labels, 0.1, TANH))):
        np.testing.assert_allclose(actual, expected, rtol=2e-14, atol=1e-15)
    for z in retained:
        z.fill(99.0)
    scratch.fill(99.0)
    for actual, expected in zip(f.preactivations + f.hidden, reference.preactivations + reference.hidden):
        np.testing.assert_array_equal(actual, expected)
    for actual, expected in zip(list(blocks(state)) + [inputs, labels], saved):
        np.testing.assert_array_equal(actual, expected)
    return "depth 3; shared buffer across value/derivative and calls; in-place inputs; retained-input mutation; no aliases"


def zero_and_domain_audit():
    def unused(z):
        raise AssertionError("zero step evaluated a callback")

    activation = Activation("must_not_run", unused, unused)
    state = Parameters(([[1.0]],), [1.0])
    for eta in (0, 0.0, np.uint64(0), np.float32(0)):
        result = gd_step(state, [[1.0]], [0.0], eta, activation)
        for old, new in zip(blocks(state), blocks(result)):
            np.testing.assert_array_equal(old, new)
            assert not np.shares_memory(old, new)
    invalid_arguments = [([[1.0]], [np.nan], None), ([[1.0]], [0.0], [0.0, 1.0]),
                         ([[np.inf]], [0.0], None), ([[1.0]], [[0.0]], None)]
    for x, y, rates in invalid_arguments:
        try:
            gd_step(state, x, y, 0.0, activation, kappas=rates)
        except (ValueError, TypeError):
            pass
        else:
            raise AssertionError("zero step accepted invalid structure")
    outputs = [lambda z: np.zeros(z.shape, dtype=complex), lambda z: np.zeros(z.shape, dtype=bool),
               lambda z: np.full_like(z, np.nan), lambda z: np.full_like(z, np.inf),
               lambda z: np.zeros((2, 1)), lambda z: 1.0]
    for output in outputs:
        for derivative in (False, True):
            a = Activation("invalid", (lambda z: z) if derivative else output,
                           output if derivative else np.ones_like)
            try:
                (backward if derivative else forward)(state, [[1.0]], a)
            except (ValueError, TypeError):
                pass
            else:
                raise AssertionError("accepted invalid callback result")
    for value in (True, np.bool_(True), 1.0, np.float64(1.0), 1j, "1"):
        for covariance, powers in (([[value]], [2]), ([[1]], [value])):
            try:
                gaussian_moment(covariance, powers)
            except TypeError:
                pass
            else:
                raise AssertionError(f"accepted invalid exact value {value!r}")
    for integer in (1, np.int8(1), np.int64(1), np.uint64(1)):
        same(gaussian_moment([[integer]], [np.int64(2)]), Q(1))
    return "4 zero-step scalar types, 4 invalid zero-step structures, 12 invalid callbacks, 12 exact type rejections, 4 integer types"


def finite_scale_controls():
    state = Parameters(([[1.0]],), [1.0])
    result = gd_step(state, [[1.0]], [0.0], 2.0**-1023, IDENTITY,
                     kappas=[2.0**1023] * 2)
    same(result.weights[0][0, 0], -1.0)
    same(result.readout[0], -1.0)
    for eta in (1.0, 1, np.int64(1), np.float32(1), np.float64(1)):
        same(gd_step(state, [[1.0]], [0.0], eta, IDENTITY).readout[0], -1.0)
    zero = Parameters(([[0.0]],), [0.0])
    same(loss(zero, [[1.0, 1.0]], [2.0**511, 2.0**511], IDENTITY), 2.0**1022)
    same(loss(zero, [[1.0]], [2.0**-537], IDENTITY), 2.0**-1074)
    return "unrepresentable velocity rescued in GD; 5 signed/floating step types; normal and subnormal scaled losses"


print(f"Runtime: Python {sys.version.split()[0]}, NumPy {np.__version__}")
for dtype in (np.uint8, np.uint16, np.uint32, np.uint64):
    check(f"unsigned_step_{dtype.__name__}", lambda dtype=dtype: unsigned_step(dtype))
for which in ("readout", "input", "delta", "middle"):
    check(f"kernel_normalization_{which}", lambda which=which: normalized_kernel(which))
check("forward_input_normalization", input_normalization)
for which, target in product(("flow", "gd"), ("first", "readout")):
    check(f"gradient_underflow_{which}_{target}", lambda which=which, target=target: normalized_update(which, target))
for which in ("flow", "gd"):
    check(f"gradient_overflow_{which}", lambda which=which: overflowing_gradient(which))
check("forward_mode_derivative_oracle", forward_mode_audit)
check("exact_latent_polynomial_oracle", exact_wick_audit)
check("exact_principal_minor_oracle", exact_psd_audit)
check("finite_gaussian_conditioning_algebra", gaussian_conditioning_algebra)
check("callback_ownership", callback_audit)
check("zero_step_and_domains", zero_and_domain_audit)
check("finite_scale_controls", finite_scale_controls)
passed = sum(ok for _, ok in results)
print(f"SUMMARY: {passed} passed groups; {len(results) - passed} failed counterexamples; {len(results)} total")
raise SystemExit(0 if passed == len(results) else 1)
