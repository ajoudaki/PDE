"""Deterministic finite-flow checks; no sampling panels or training runs."""

from fractions import Fraction
from math import factorial
import unittest

import numpy as np

from pde import Activation, Parameters, flow_velocity, forward, kernel
from pde.finite_jets import flow_jet


def identity(j, z):
    return z.copy() if j == 0 else np.full_like(z, 1.0 if j == 1 else 0.0)


def cubic(j, z):
    return (z**3, 3*z**2, 6*z, np.full_like(z, 6.0))[j]


def smooth(j, z):
    return (0.4 + np.sin(z), np.cos(z), -np.sin(z), -np.cos(z))[j]


def activation(oracle):
    return Activation("test", lambda z: oracle(0, z), lambda z: oracle(1, z))


def blocks(state):
    return state.weights + (state.readout,)


def pack(state):
    return np.concatenate([v.ravel() for v in blocks(state)])


def unpack(vector, template):
    offset, arrays = 0, []
    for block in blocks(template):
        arrays.append(vector[offset:offset + block.size].reshape(block.shape))
        offset += block.size
    return Parameters(tuple(arrays[:-1]), arrays[-1])


def example():
    # Independent neuron populations and a deliberately nonsymmetric matrix.
    state = Parameters(([[0.2, -0.1, 0.3, 0.4], [-0.4, 0.2, 0.1, -0.3]],
                        [[0.3, -0.5], [0.7, 0.2]]), [0.6, -0.4])
    return state, np.array([[0.8], [-0.3], [0.5], [1.2]]), np.array([0.7])


class MovingFlowTests(unittest.TestCase):
    def test_raw_api_shapes_normalization_and_first_derivative(self):
        state, x, y = example()
        rates = [0.4, 1.7, 0.9]
        result = flow_jet(state, x, y, smooth, kappas=rates)
        fields = forward(state, x, activation(smooth))
        np.testing.assert_array_equal(result.output_coefficients[0], fields.output)
        self.assertEqual(result.output_coefficients.shape, (4, 1))
        for layer in range(2):
            self.assertEqual(result.hidden_coefficients[layer].shape, (4, 2, 1))
            np.testing.assert_array_equal(result.hidden_coefficients[layer][0], fields.hidden[layer])
            np.testing.assert_array_equal(result.preactivation_coefficients[layer][0], fields.preactivations[layer])
        np.testing.assert_array_equal(pack(result.parameter_coefficients[0]), pack(state))
        np.testing.assert_allclose(pack(result.parameter_coefficients[1]),
                                   pack(flow_velocity(state, x, y, activation(smooth), kappas=rates)),
                                   rtol=2e-15, atol=2e-16)
        expected = -2 * kernel(state, x, activation(smooth), kappas=rates) @ (fields.output - y)
        np.testing.assert_allclose(result.output_derivatives[1], expected, rtol=2e-15)
        for k in range(4):
            np.testing.assert_array_equal(result.output_derivatives[k],
                                          factorial(k) * result.output_coefficients[k])

    def test_linear_equal_weights_hand_solution_is_moving_flow(self):
        # n=d=1, phi(z)=z, y=0: all weights c obey c'=-2c^5.
        # c=(1+8t)^(-1/4), z2=c^2, f=c^3.
        state = Parameters(([[1.0]], [[1.0]]), [1.0])
        result = flow_jet(state, [[1.0]], [0.0], identity)
        for k, expected in enumerate([1.0, -2.0, 10.0, -60.0]):
            np.testing.assert_allclose(pack(result.parameter_coefficients[k]), expected, rtol=1e-15)
        np.testing.assert_allclose(result.preactivation_coefficients[1][:, 0, 0],
                                   [1.0, -4.0, 24.0, -160.0], rtol=1e-15)
        np.testing.assert_allclose(result.output_coefficients[:, 0],
                                   [1.0, -6.0, 42.0, -308.0], rtol=1e-15)
        # Freezing theta'(0) instead gives (1-2t)^3, whose t^2 term is 12.
        self.assertGreater(abs(result.output_coefficients[2, 0] - 12.0), 20.0)

    def test_cubic_hand_solution_uses_every_activation_derivative(self):
        # f = W3*(W2)^3*(W1)^9. Rates (1/9,1/3,1) preserve W1=W2=W3=c.
        # c'=-2c^25; c=(1+48t)^(-1/24), h1=c^3, z2=c^4, h2=c^12, f=c^13.
        state = Parameters(([[1.0]], [[1.0]]), [1.0])
        result = flow_jet(state, [[1.0]], [0.0], cubic, kappas=[1/9, 1/3, 1])
        def expected(power):
            a = Fraction(power, 24)
            return np.array([1, -48*a, 48**2*a*(a+1)/2,
                             -48**3*a*(a+1)*(a+2)/6], dtype=float)
        for k, value in enumerate(expected(1)):
            np.testing.assert_allclose(pack(result.parameter_coefficients[k]), value, rtol=2e-15)
        for actual, power in ((result.hidden_coefficients[0], 3),
                              (result.preactivation_coefficients[1], 4),
                              (result.hidden_coefficients[1], 12)):
            np.testing.assert_allclose(actual[:, 0, 0], expected(power), rtol=2e-15)
        np.testing.assert_allclose(result.output_coefficients[:, 0], expected(13), rtol=2e-15)

    def test_constant_activation_differentiates_residual_in_physical_time(self):
        state, x, y = example()
        def constant(j, z):
            return np.full_like(z, 2.0 if j == 0 else 0.0)
        result = flow_jet(state, x, y, constant, kappas=[0.5, 0.8, 1.5])
        # f-y = (f0-y) exp(-2*kappa3*2^2*t), hence decay rate 12.
        residual = result.output_coefficients[0, 0] - y[0]
        for k in range(1, 4):
            self.assertAlmostEqual(result.output_coefficients[k, 0], residual*(-12)**k/factorial(k))
            for w in result.parameter_coefficients[k].weights:
                np.testing.assert_array_equal(w, np.zeros_like(w))

    def test_parameter_acceleration_and_jerk_against_existing_rhs_differences(self):
        state, x, y = example()
        theta = pack(state)
        rates = [0.4, 1.7, 0.9]
        def rhs(values):
            return pack(flow_velocity(unpack(values, state), x, y, activation(smooth), kappas=rates))
        v = rhs(theta)
        eps = 2e-4
        plus, minus = rhs(theta + eps*v), rhs(theta - eps*v)
        acceleration = (plus - minus) / (2*eps)
        # theta''' = V''[V,V] + V' (V' V), evaluated using only the old RHS.
        jerk = ((plus - 2*v + minus) / eps**2
                + (rhs(theta + eps*acceleration) - rhs(theta - eps*acceleration)) / (2*eps))
        result = flow_jet(state, x, y, smooth, kappas=rates)
        np.testing.assert_allclose(2*pack(result.parameter_coefficients[2]), acceleration,
                                   rtol=3e-6, atol=2e-8)
        np.testing.assert_allclose(6*pack(result.parameter_coefficients[3]), jerk,
                                   rtol=8e-6, atol=2e-7)

    def test_forward_fields_along_parameter_polynomial(self):
        state, x, y = example()
        result = flow_jet(state, x, y, smooth)
        def actual(t):
            theta = sum(t**k * pack(p) for k, p in enumerate(result.parameter_coefficients))
            fields = forward(unpack(theta, state), x, activation(smooth))
            return np.concatenate([v.ravel() for v in fields.preactivations + fields.hidden + (fields.output,)])
        def coefficient(k):
            return np.concatenate([v[k].ravel() for v in result.preactivation_coefficients
                                   + result.hidden_coefficients + (result.output_coefficients,)])
        step = 4e-4
        a, b, c, d, e = (actual(t*step) for t in (-2, -1, 0, 1, 2))
        np.testing.assert_allclose((d-b)/(2*step), coefficient(1), rtol=3e-6, atol=3e-7)
        np.testing.assert_allclose((d-2*c+b)/step**2, 2*coefficient(2), rtol=1e-5, atol=3e-7)
        np.testing.assert_allclose((e-2*d+2*b-a)/(2*step**3), 6*coefficient(3), rtol=8e-5, atol=5e-6)

    def test_independent_neuron_relabeling_preserves_output(self):
        state, x, y = example()
        # Permute only layer 1; layer 2's neuron labels are held fixed.
        permutation = [1, 0]
        changed = Parameters((state.weights[0][permutation], state.weights[1][:, permutation]), state.readout)
        a, b = (flow_jet(p, x, y, smooth) for p in (state, changed))
        np.testing.assert_allclose(a.output_coefficients, b.output_coefficients, rtol=2e-14, atol=2e-15)
        for k in range(4):
            np.testing.assert_allclose(b.parameter_coefficients[k].weights[0],
                                       a.parameter_coefficients[k].weights[0][permutation], atol=2e-15)
            np.testing.assert_allclose(b.parameter_coefficients[k].weights[1],
                                       a.parameter_coefficients[k].weights[1][:, permutation], atol=2e-15)

    def test_zero_residual_and_zero_input(self):
        state, x, _ = example()
        y = forward(state, x, activation(smooth)).output
        result = flow_jet(state, x, y, smooth)
        for p in result.parameter_coefficients[1:]:
            np.testing.assert_array_equal(pack(p), np.zeros_like(pack(p)))
        np.testing.assert_array_equal(result.output_coefficients[1:], np.zeros((3, 1)))
        result = flow_jet(state, np.zeros_like(x), [0.7], smooth)
        for k in range(1, 4):
            np.testing.assert_array_equal(result.parameter_coefficients[k].weights[0], np.zeros((2, 4)))
            np.testing.assert_array_equal(result.preactivation_coefficients[0][k], np.zeros((2, 1)))
        self.assertGreater(np.linalg.norm(result.parameter_coefficients[1].readout), 0)


class ContractTests(unittest.TestCase):
    def test_order_prefix_and_no_unused_derivative_requests(self):
        state, x, y = example()
        full = flow_jet(state, x, y, smooth)
        for order in range(4):
            calls = []
            def oracle(j, z):
                calls.append(j)
                self.assertLessEqual(j, order)
                self.assertEqual(z.shape, (2, 1))
                return smooth(j, z)
            result = flow_jet(state, x, y, oracle, order=np.int64(order))
            self.assertEqual(calls, list(range(order+1))*2)
            np.testing.assert_array_equal(result.output_coefficients, full.output_coefficients[:order+1])
            for k in range(order+1):
                np.testing.assert_array_equal(pack(result.parameter_coefficients[k]), pack(full.parameter_coefficients[k]))

    def test_inplace_and_shared_buffer_callbacks_are_owned(self):
        state, x, y = example()
        original = pack(state).copy(), x.copy(), y.copy()
        scratch = np.empty((2, 1))
        def inplace(j, z):
            z[:] = smooth(j, z)
            return z
        def reused(j, z):
            scratch[:] = smooth(j, z)
            z.fill(123.0)
            return scratch
        reference = flow_jet(state, x, y, smooth)
        for oracle in (inplace, reused):
            result = flow_jet(state, x, y, oracle)
            scratch.fill(-999.0)
            np.testing.assert_array_equal(result.output_coefficients, reference.output_coefficients)
            for actual, expected in zip(result.parameter_coefficients, reference.parameter_coefficients):
                np.testing.assert_array_equal(pack(actual), pack(expected))
            for actual, expected in zip(result.preactivation_coefficients + result.hidden_coefficients,
                                        reference.preactivation_coefficients + reference.hidden_coefficients):
                np.testing.assert_array_equal(actual, expected)
        for actual, expected in zip((pack(state), x, y), original):
            np.testing.assert_array_equal(actual, expected)
        for old, new in zip(blocks(state), blocks(reference.parameter_coefficients[0])):
            self.assertFalse(np.shares_memory(old, new))
        reference.parameter_coefficients[0].weights[0].fill(77.0)
        np.testing.assert_array_equal(pack(state), original[0])
        derivatives = result.output_derivatives
        derivatives.fill(99)
        self.assertFalse(np.shares_memory(derivatives, result.output_coefficients))

    def test_invalid_scope_arguments_and_mutated_parameters(self):
        state, x, y = example()
        for order in (-1, 4, 1.0, True, np.bool_(False), "2"):
            with self.subTest(order=order), self.assertRaises(ValueError):
                flow_jet(state, x, y, smooth, order=order)
        with self.assertRaises(TypeError):
            flow_jet(None, x, y, smooth)
        for depth in (1, 3):
            p = Parameters((state.weights[0],) + (state.weights[1],)*(depth-1), state.readout)
            with self.assertRaises(ValueError):
                flow_jet(p, x, y, smooth)
        for value in (x[:, 0], x.T, np.tile(x, 2), np.empty((4, 0)), x*float("nan"), x+1j,
                      np.ones((4, 1), dtype=bool)):
            with self.assertRaises(ValueError):
                flow_jet(state, value, y, smooth)
        for value in (0.7, [[0.7]], [0.7, 0.8], [np.inf], [True], [1j]):
            with self.assertRaises(ValueError):
                flow_jet(state, x, value, smooth)
        for value in ([1, 1], [1, 0, 1], [-1, 1, 1], [1, np.inf, 1], [1, np.nan, 1], [True]*3):
            with self.assertRaises(ValueError):
                flow_jet(state, x, y, smooth, kappas=value)
        with self.assertRaises(TypeError):
            flow_jet(state, x, y, None)
        state.weights[1][0, 0] = np.nan
        with self.assertRaises(ValueError):
            flow_jet(state, x, y, smooth)

    def test_invalid_callback_shape_type_finiteness_at_every_order(self):
        state = Parameters(([[1.0]], [[1.0]]), [1.0])
        bad = (lambda z: 1.0, lambda z: z[:, 0], lambda z: z[None],
               lambda z: np.full_like(z, np.nan), lambda z: np.full_like(z, np.inf),
               lambda z: z.astype(complex), lambda z: z.astype(bool),
               lambda z: z.astype(str))
        for order in range(4):
            for invalid in bad:
                def oracle(j, z):
                    return invalid(z) if j == order else identity(j, z)
                with self.subTest(order=order, invalid=invalid), self.assertRaises(ValueError):
                    flow_jet(state, [[1.0]], [0.0], oracle)

    def test_nonfinite_contractions_and_derivative_conversion_rejected(self):
        state = Parameters(([[1e308]], [[2.0]]), [1.0])
        with self.assertRaises(ValueError):
            flow_jet(state, [[1.0]], [0.0], identity, order=0)
        state = Parameters(([[1.0]], [[1.0]]), [1.0])
        with self.assertRaises(ValueError):
            flow_jet(state, [[1.0]], [0.0], identity, kappas=[1e308]*3)
        result = flow_jet(state, [[1.0]], [0.0], identity)
        result.output_coefficients[3, 0] = 1e308
        with self.assertRaisesRegex(ValueError, "output derivatives"):
            _ = result.output_derivatives

    def test_scaling_keeps_representable_first_order_coefficients(self):
        # A huge residual must not first be multiplied by -2 in isolation.
        state = Parameters(([[0.0]], [[1.0]]), [1.0])
        result = flow_jet(state, [[1.0]], [-2.0**1023], identity, order=1,
                          kappas=[0.25, 1.0, 1.0])
        self.assertEqual(result.parameter_coefficients[1].weights[0][0, 0], -2.0**1022)
        # Preserve a subnormal first raw contraction before applying mobility.
        result = flow_jet(state, [[2.0**-1074]], [-1.0], identity, order=1,
                          kappas=[2.0**1023, 1.0, 1.0])
        self.assertEqual(result.parameter_coefficients[1].weights[0][0, 0], -2.0**-50)
        # First-layer normalization follows the raw matrix product.
        state = Parameters(([[2.0**1023, 0.0, 0.0, 0.0]], [[1.0]]), [1.0])
        result = flow_jet(state, [[2.0**-1074], [0.0], [0.0], [0.0]], [0.0], identity, order=0)
        self.assertEqual(result.output_coefficients[0, 0], 2.0**-52)


if __name__ == "__main__":
    unittest.main()
