"""Regression checks for finite arithmetic and callback ownership."""

import unittest

import numpy as np

from pde import (
    ARCTAN, IDENTITY, TANH, Activation, Parameters, backward, forward,
    flow_velocity, gd_step, kernel, kernel_blocks, loss, loss_gradients,
)


class NumericalContractTests(unittest.TestCase):
    def test_unsigned_positive_steps_are_descent_steps(self):
        state = Parameters(([[1.0]],), [1.0])
        for dtype in (np.uint8, np.uint16, np.uint32, np.uint64):
            with self.subTest(dtype=dtype):
                result = gd_step(state, [[1.0]], [0.0], dtype(1), IDENTITY)
                np.testing.assert_array_equal(result.weights[0], [[-1.0]])
                np.testing.assert_array_equal(result.readout, [-1.0])

    def test_kernel_normalization_preserves_subnormal_raw_grams(self):
        small, rate = 2.0**-537, 2.0**1023
        cases = (
            (Parameters(([[small], [0.0]],), [0.0, 0.0]), [[1.0]],
             [1.0, rate], -1, 2.0**-52),
            (Parameters(([[0.0, 0.0, 0.0, 0.0]],), [1.0]),
             [[small], [0.0], [0.0], [0.0]], [rate, 1.0], 0, 2.0**-53),
            (Parameters(([[0.0], [0.0]],), [small, 0.0]), [[1.0]],
             [rate, 1.0], 0, 2.0**-52),
            (Parameters(([[small], [0.0]], np.zeros((2, 2))), [1.0, 0.0]),
             [[1.0]], [1.0, rate, 1.0], 1, 2.0**-53),
        )
        for state, inputs, rates, block, expected in cases:
            with self.subTest(block=block, dimension=state.weights[0].shape):
                actual = kernel_blocks(state, inputs, IDENTITY, kappas=rates)
                self.assertEqual(actual[block, 0, 0], expected)

    def test_first_layer_normalizes_after_raw_contraction(self):
        state = Parameters(([[2.0**1023, 0.0, 0.0, 0.0]],), [1.0])
        inputs = [[2.0**-1074], [0.0], [0.0], [0.0]]
        self.assertEqual(forward(state, inputs, IDENTITY).output[0], 2.0**-52)
        self.assertEqual(loss(state, inputs, [0.0], IDENTITY), 2.0**-104)

    def test_physical_updates_preserve_subnormal_raw_contractions(self):
        small, rate = 2.0**-1074, 2.0**1023
        for first in (True, False):
            if first:
                state = Parameters((np.zeros((4, 1)),), np.ones(4))
                inputs, rates = [[small]], [rate, 1.0]
            else:
                state = Parameters((np.full((4, 1), small),), np.zeros(4))
                inputs, rates = [[1.0]], [1.0, rate]
            results = (flow_velocity(state, inputs, [-1.0], IDENTITY, kappas=rates),
                       gd_step(state, inputs, [-1.0], 1.0, IDENTITY, kappas=rates))
            for index, result in enumerate(results):
                with self.subTest(first=first, update=index):
                    actual = result.weights[0][0, 0] if first else result.readout[0]
                    self.assertEqual(actual, -2.0**-50)

    def test_physical_updates_do_not_require_representable_loss_gradient(self):
        state = Parameters(([[0.0]],), [1.0])
        with self.assertRaises(ValueError):
            loss_gradients(state, [[1.0]], [-2.0**1023], IDENTITY)
        velocity = flow_velocity(state, [[1.0]], [-2.0**1023], IDENTITY,
                                 kappas=[0.25, 1.0])
        updated = gd_step(state, [[1.0]], [-2.0**1023], 0.25, IDENTITY)
        self.assertEqual(velocity.weights[0][0, 0], -2.0**1022)
        self.assertEqual(updated.weights[0][0, 0], -2.0**1022)

    def test_large_mobility_preserves_finite_velocity_and_stationarity(self):
        state = Parameters(([[1.0], [1.0]],), [1.0, 1.0])
        for label, expected in ((0.75, -5e307), (1.0, 0.0)):
            with self.subTest(label=label):
                result = flow_velocity(state, [[1.0]], [label], IDENTITY,
                                       kappas=[1e308, 1e308])
                np.testing.assert_allclose(result.weights[0], expected)
                np.testing.assert_allclose(result.readout, expected)

    def test_kernel_scale_order_preserves_binary_result_and_signed_entries(self):
        state = Parameters(([[2.0**27]],), [2.0**511])
        x = [[2.0**-27, -(2.0**-27)]]
        blocks = kernel_blocks(state, x, IDENTITY, kappas=[2.0**-1022] * 2)
        expected = 2.0**-54 * np.array([[1.0, -1.0], [-1.0, 1.0]])
        np.testing.assert_array_equal(blocks[0], expected)
        np.testing.assert_array_equal(kernel(state, x, IDENTITY, kappas=[2.0**-1022] * 2),
                                      expected)
        # Identity backsignals are the same for each input; the input Gram
        # contributes the negative off-diagonal signs.

    def test_middle_kernel_scale_order(self):
        scale = Activation("scale", lambda z: np.ldexp(z, -27),
                           lambda z: np.full_like(z, 2.0**-27))
        state = Parameters(([[1.0]], [[2.0**27]]), [2.0**511])
        blocks = kernel_blocks(state, [[1.0, -1.0]], (scale, IDENTITY),
                               kappas=[2.0**-1022] * 3)
        expected = 2.0**-54 * np.array([[1.0, -1.0], [-1.0, 1.0]])
        np.testing.assert_array_equal(blocks[1], expected)

    def test_kernel_scale_order_avoids_premature_overflow(self):
        state = Parameters(([[0.1]],), [0.1])
        blocks = kernel_blocks(state, [[10.0]], IDENTITY, kappas=[1e307, 1.0])
        np.testing.assert_allclose(blocks[:, 0, 0], [1e307, 1.0])

    def test_gd_does_not_require_representable_velocity(self):
        state = Parameters(([[1.0]],), [1.0])
        with self.assertRaises(ValueError):
            flow_velocity(state, [[1.0]], [0.0], IDENTITY, kappas=[1e308] * 2)
        result = gd_step(state, [[1.0]], [0.0], 1e-308, IDENTITY, kappas=[1e308] * 2)
        np.testing.assert_allclose(result.weights[0], -1.0)
        np.testing.assert_allclose(result.readout, -1.0)
        zero = gd_step(state, [[1.0]], [0.0], 0.0, IDENTITY, kappas=[1e308] * 2)
        np.testing.assert_array_equal(zero.weights[0], state.weights[0])
        self.assertFalse(np.shares_memory(zero.weights[0], state.weights[0]))
        self.assertFalse(np.shares_memory(zero.readout, state.readout))

    def test_gd_addition_cancels_unrepresentable_increment(self):
        state = Parameters(([[1e308]],), [1.0])
        result = gd_step(state, [[1e-308]], [0.0], 1e308, IDENTITY,
                         kappas=[1e308, 1e-308])
        np.testing.assert_allclose(result.weights[0] / 1e308, -1.0)
        np.testing.assert_allclose(result.readout, -1.0)

    def test_inplace_value_preserves_preactivation(self):
        activation = Activation("inplace_tanh", lambda z: np.tanh(z, out=z), TANH.derivative)
        state = Parameters((np.array([[2.0]]),), np.array([3.0]))
        result = forward(state, [[1.0]], activation)
        self.assertEqual(result.preactivations[0][0, 0], 2.0)
        self.assertAlmostEqual(result.hidden[0][0, 0], np.tanh(2.0))

    def test_inplace_value_has_correct_loss_gradient(self):
        activation = Activation("inplace_tanh", lambda z: np.tanh(z, out=z), TANH.derivative)
        state = Parameters((np.array([[2.0]]),), np.array([3.0]))
        actual = loss_gradients(state, [[1.0]], [1.0], activation)
        expected = loss_gradients(state, [[1.0]], [1.0], TANH)
        np.testing.assert_allclose(actual.weights[0], expected.weights[0])
        np.testing.assert_allclose(actual.readout, expected.readout)

    def test_inplace_derivative_preserves_hidden(self):
        def derivative(z):
            z.fill(1.0)
            return z
        activation = Activation("inplace_derivative", lambda z: z, derivative)
        state = Parameters((np.array([[2.0]]),), np.array([1.0]))
        actual = loss_gradients(state, [[1.0]], [0.0], activation)
        self.assertEqual(actual.readout[0], 8.0)

    def test_reused_output_buffer_does_not_alias_layers(self):
        scratch = np.empty((1, 1))
        def value(z):
            np.copyto(scratch, z)
            return scratch
        activation = Activation("buffered_identity", value, np.ones_like)
        state = Parameters((np.array([[2.0]]), np.array([[3.0]])), np.array([1.0]))
        result = forward(state, [[1.0]], activation)
        self.assertEqual(result.hidden[0][0, 0], 2.0)
        self.assertEqual(result.hidden[1][0, 0], 6.0)
        scratch.fill(99.0)
        self.assertEqual(result.hidden[1][0, 0], 6.0)

    def test_saturated_tanh_gradient_retains_representable_signal(self):
        state = Parameters((np.array([[20.0]]),), np.array([1e10]))
        actual = loss_gradients(state, [[1.0]], [0.0], TANH).weights[0][0, 0]
        expected = 2e20 * np.tanh(20.0) / np.cosh(20.0) ** 2
        self.assertAlmostEqual(actual / expected, 1.0, places=14)

    def test_large_arctan_gradient_retains_representable_signal(self):
        state = Parameters((np.array([[1e155]]),), np.array([1e153]))
        actual = loss_gradients(state, [[1.0]], [0.0], ARCTAN).weights[0][0, 0]
        self.assertAlmostEqual(actual / (np.pi * 1e-4), 1.0, places=12)

    def test_large_batch_mean_square_is_representable(self):
        state = Parameters((np.array([[0.0]]),), np.array([0.0]))
        value = loss(state, [[1.0, 1.0]], [1e154, 1e154], IDENTITY)
        self.assertAlmostEqual(value / 1e308, 1.0, places=14)

    def test_unrepresentable_loss_is_rejected(self):
        state = Parameters((np.array([[0.0]]),), np.array([0.0]))
        with self.assertRaisesRegex(ValueError, "loss"):
            loss(state, [[1.0]], [1e308], IDENTITY)

    def test_unrepresentable_total_kernel_is_rejected(self):
        state = Parameters((np.array([[1.0]]),), np.array([1.0]))
        blocks = kernel_blocks(state, [[1.0]], IDENTITY, kappas=[1e308, 1e308])
        self.assertTrue(np.all(np.isfinite(blocks)))
        with self.assertRaisesRegex(ValueError, "total kernel"):
            kernel(state, [[1.0]], IDENTITY, kappas=[1e308, 1e308])

    def test_builtin_derivatives_at_branch_boundaries_and_both_signs(self):
        values = np.array([-100.0, -20.0, -1.0, -0.1, 0.0, 0.1, 1.0, 20.0, 100.0])
        np.testing.assert_allclose(TANH.derivative(values), 1.0 / np.cosh(values) ** 2,
                                   rtol=1e-14, atol=0.0)
        values = np.r_[values, np.nextafter(1.0, 0.0), np.nextafter(1.0, 2.0)]
        np.testing.assert_allclose(ARCTAN.derivative(values), 1.0 / (1.0 + values ** 2),
                                   rtol=1e-14, atol=0.0)
        for value in (-1e155, 1e155):
            self.assertGreater(float(ARCTAN.derivative(np.array(value))), 0.0)
        self.assertEqual(float(TANH.derivative(np.array(0.0))), 1.0)


if __name__ == "__main__":
    unittest.main()
