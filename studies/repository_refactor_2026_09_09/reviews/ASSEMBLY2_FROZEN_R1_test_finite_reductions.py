"""Independent finite metric, differentiation and Lax checks; no trajectories."""

import unittest

import numpy as np

from pde.finite_network import (
    Activation, IDENTITY, Parameters, flow_velocity, forward, kernel_blocks,
)
from pde.finite_reductions import (
    frozen_quadratic, frozen_quadratic_step, mixed_lax, mixed_quadratic,
    rms_quadratic,
)


SQUARE = Activation("square", lambda z: z * z, lambda z: 2.0 * z)


def arrays(state):
    return state.weights + (state.readout,)


def shifted(state, direction, amount):
    values = tuple(a + amount * b for a, b in zip(arrays(state), arrays(direction)))
    return Parameters(values[:-1], values[-1])


def coordinate_shift(state, block, index, amount):
    values = [a.copy() for a in arrays(state)]
    values[block][index] += amount
    return Parameters(tuple(values[:-1]), values[-1])


def finite_state(n):
    rng = np.random.default_rng(590 + n)
    return Parameters((rng.normal(scale=0.7, size=(n, 1)),
                       rng.normal(scale=0.4, size=(n, n))),
                      rng.normal(scale=0.8, size=n))


def normalized_output(state, epsilon):
    """Definition alone, without any backward fields or reduction code."""
    n = state.width
    first = state.weights[0][:, 0] ** 2
    first = first / np.sqrt(np.sum(first ** 2) / n + epsilon)
    last = (state.weights[1] @ first) ** 2
    last = last / np.sqrt(np.sum(last ** 2) / n + epsilon)
    return state.readout @ last / n


class MixedReductionTests(unittest.TestCase):
    def test_against_existing_layerwise_core(self):
        for n in (1, 3):
            state = finite_state(n)
            for model in ("QI", "IQ", "QQ"):
                activations = tuple(SQUARE if c == "Q" else IDENTITY for c in model)
                reference_output = forward(state, [[1.0]], activations).output[0]
                for label in (-0.4, 0.7, reference_output):
                    with self.subTest(n=n, model=model, label=label):
                        result = mixed_quadratic(state, label, model=model)
                        self.assertAlmostEqual(result.output, reference_output, places=14)
                        expected = flow_velocity(state, [[1.0]], [label], activations)
                        for got, want in zip(arrays(result.velocity), arrays(expected)):
                            np.testing.assert_allclose(got, want, atol=2e-14, rtol=2e-14)
                        # Choosing residual -1/2 makes the core physical RHS
                        # independently equal the unit output-ascent field.
                        expected_ascent = flow_velocity(
                            state, [[1.0]], [reference_output + 0.5], activations)
                        for got, want in zip(arrays(result.ascent), arrays(expected_ascent)):
                            np.testing.assert_allclose(got, want, atol=2e-14, rtol=2e-14)
                        expected_k = kernel_blocks(state, [[1.0]], activations)[:, 0, 0]
                        np.testing.assert_allclose(result.kernel_blocks, expected_k, atol=2e-14)

    def test_lax_chain_rule_both_mixed_models(self):
        state = finite_state(3)
        step = 1e-6
        for model in ("QI", "IQ"):
            result = mixed_quadratic(state, 0.4, model=model)
            lax = mixed_lax(state, model=model)
            plus = mixed_lax(shifted(state, result.ascent, step), model=model)
            minus = mixed_lax(shifted(state, result.ascent, -step), model=model)
            np.testing.assert_allclose((plus.factor - minus.factor) / (2 * step),
                                       lax.factor_ascent, atol=2e-10, rtol=2e-7)
            np.testing.assert_allclose((plus.operator - minus.operator) / (2 * step),
                                       lax.ascent, atol=2e-10, rtol=2e-7)
            if model == "QI":
                np.testing.assert_allclose(lax.operator[1:, 0] * np.sqrt(3),
                                           result.fields["q"], atol=1e-15)
                matrix, a = state.weights[1], state.readout
                dmatrix, da = result.ascent.weights[1], result.ascent.readout
                derivative = dmatrix @ matrix.T + matrix @ dmatrix.T
                derivative -= (np.outer(da, a) + np.outer(a, da)) / 3
                np.testing.assert_allclose(derivative, 0.0, atol=2e-15)
            else:
                np.testing.assert_allclose(lax.operator[:-1, -1] * np.sqrt(3),
                                           result.fields["z"], atol=1e-15)

    def test_spectrum_orientation_witness_is_raw_realizable(self):
        h = np.array([1.0, 2.0, 3.0])
        states = [Parameters((np.sqrt(h)[:, None], np.eye(3)), a)
                  for a in ([1.0, 0.0, 0.0], [1 / 3, -2 / 3, 2 / 3])]
        values = [mixed_quadratic(s, 1.0, model="QI") for s in states]
        lax = [mixed_lax(s, model="QI") for s in states]
        d = np.array([1.0, 1.0, -1.0])
        orthogonal = np.eye(3) - 2 * np.outer(d, d) / 3
        conjugacy = np.eye(4)
        conjugacy[1:, 1:] = orthogonal
        np.testing.assert_allclose(conjugacy @ lax[0].operator @ conjugacy.T,
                                   lax[1].operator, atol=2e-15)
        np.testing.assert_allclose(orthogonal @ h, h, atol=1e-15)
        np.testing.assert_allclose([x.output for x in values], [1 / 3, 1 / 3])
        np.testing.assert_allclose([x.kernel for x in values], [68 / 9, 28 / 3])
        self.assertGreater(abs(values[0].output_velocity - values[1].output_velocity), 1.0)

    def test_qq_balance_chain_rule(self):
        state = finite_state(4)
        result = mixed_quadratic(state, 0.7, model="QQ")
        matrix, a, u = state.weights[1], state.readout, state.weights[0][:, 0]
        dmatrix, da, du = (result.ascent.weights[1], result.ascent.readout,
                          result.ascent.weights[0][:, 0])
        row = 2 * state.width * np.sum(matrix * dmatrix, axis=1) - 4 * a * da
        column = 2 * state.width * np.sum(matrix * dmatrix, axis=0) - u * du
        np.testing.assert_allclose(row, result.row_balance_ascent, atol=2e-15)
        np.testing.assert_allclose(column, result.column_balance_ascent, atol=2e-15)


class RMSReductionTests(unittest.TestCase):
    def test_every_output_gradient_coordinate_and_kernel_block(self):
        step = 1e-6
        for n in (1, 3):
            state = finite_state(n)
            for epsilon in (0.2, 1.3):
                result = rms_quadratic(state, 0.7, epsilon=epsilon)
                self.assertAlmostEqual(result.output, normalized_output(state, epsilon), places=14)
                for block, raw in enumerate(arrays(state)):
                    gradient = np.empty_like(raw)
                    for index in np.ndindex(raw.shape):
                        plus = normalized_output(coordinate_shift(state, block, index, step), epsilon)
                        minus = normalized_output(coordinate_shift(state, block, index, -step), epsilon)
                        gradient[index] = (plus - minus) / (2 * step)
                    mobility = 1 if block == 1 else n
                    with self.subTest(n=n, epsilon=epsilon, block=block):
                        np.testing.assert_allclose(arrays(result.ascent)[block],
                                                   mobility * gradient, atol=3e-10, rtol=2e-6)
                        np.testing.assert_allclose(result.kernel_blocks[block],
                                                   mobility * np.sum(gradient ** 2),
                                                   atol=3e-10, rtol=3e-6)

    def test_complete_field_chain_rule_and_physical_energy(self):
        state, epsilon, step = finite_state(3), 0.35, 1e-6
        for label in (-0.5, 0.8):
            result = rms_quadratic(state, label, epsilon=epsilon)
            plus = rms_quadratic(shifted(state, result.ascent, step), label, epsilon=epsilon)
            minus = rms_quadratic(shifted(state, result.ascent, -step), label, epsilon=epsilon)
            for name, derivative in result.field_ascent.items():
                np.testing.assert_allclose((plus.fields[name] - minus.fields[name]) / (2 * step),
                                           derivative, atol=3e-10, rtol=2e-6)
            p = normalized_output(shifted(state, result.velocity, step), epsilon)
            m = normalized_output(shifted(state, result.velocity, -step), epsilon)
            self.assertAlmostEqual((p - m) / (2 * step), result.output_velocity, places=8)
            self.assertAlmostEqual(((p - label) ** 2 - (m - label) ** 2) / (2 * step),
                                   result.loss_velocity, places=8)
            metric_speed = sum(np.sum(v * v) / rate
                               for v, rate in zip(arrays(result.velocity), (3, 1, 3)))
            self.assertAlmostEqual(metric_speed, -result.loss_velocity, places=13)
            h, q = (result.fields[name] for name in ("h", "q"))
            pi = np.eye(3) - np.outer(h, h) / 3
            reduced_operator = 4 / result.fields["alpha"] * pi @ np.diag(h) @ pi
            np.testing.assert_allclose(reduced_operator @ q, result.field_ascent["h"], atol=2e-15)
            np.testing.assert_allclose(q @ reduced_operator @ q / 3,
                                       result.kernel_blocks[0], atol=2e-15)

    def test_signed_balance_drifts_from_raw_parameter_chain_rule(self):
        state = finite_state(3)
        for epsilon in (0.1, 1.7):
            result = rms_quadratic(state, -0.2, epsilon=epsilon)
            matrix, a, u = state.weights[1], state.readout, state.weights[0][:, 0]
            dmatrix, da, du = (result.ascent.weights[1], result.ascent.readout,
                              result.ascent.weights[0][:, 0])
            row = 6 * np.sum(matrix * dmatrix, axis=1) - 4 * a * da
            column = 6 * np.sum(matrix * dmatrix, axis=0) - u * du
            np.testing.assert_allclose(row, result.row_balance_ascent, atol=2e-15)
            np.testing.assert_allclose(column, result.column_balance_ascent, atol=2e-15)
            self.assertGreater(np.linalg.norm(row), 1e-6)

    def test_zero_coordinates_sign_quotient_and_zero_residual(self):
        state = Parameters(([[0.0], [0.4], [-0.7]], np.eye(3)), [0.3, -0.5, 0.2])
        reflected = Parameters((-state.weights[0], state.weights[1]), state.readout)
        first = rms_quadratic(state, 0.8, epsilon=0.5)
        second = rms_quadratic(reflected, 0.8, epsilon=0.5)
        np.testing.assert_array_equal(first.ascent.weights[0], -second.ascent.weights[0])
        np.testing.assert_array_equal(first.velocity.weights[1], second.velocity.weights[1])
        np.testing.assert_array_equal(first.velocity.readout, second.velocity.readout)
        np.testing.assert_array_equal(first.field_ascent["h"], second.field_ascent["h"])
        self.assertEqual(first.ascent.weights[0][0, 0], 0.0)
        stopped = rms_quadratic(state, first.output, epsilon=0.5)
        for value in arrays(stopped.velocity):
            np.testing.assert_array_equal(value, np.zeros_like(value))
        self.assertGreater(stopped.kernel, 0.0)
        zero = Parameters((np.zeros((1, 1)), np.zeros((1, 1))), [0.0])
        empty = rms_quadratic(zero, 1.0, epsilon=0.5)
        self.assertEqual(empty.kernel, 0.0)
        self.assertEqual(empty.loss, 1.0)


class ReductionContractTests(unittest.TestCase):
    def test_scope_validation_and_fresh_arrays(self):
        state = finite_state(3)
        for invalid in (0, -1, np.inf, np.nan, True, "0.5"):
            with self.assertRaises(ValueError):
                rms_quadratic(state, 1.0, epsilon=invalid)
        for invalid in ("II", "qq", [], None):
            with self.assertRaises(ValueError):
                mixed_quadratic(state, 1.0, model=invalid)
        with self.assertRaises(ValueError):
            mixed_lax(state, model="QQ")
        for invalid in (np.inf, np.nan, True, [1.0]):
            with self.assertRaises(ValueError):
                mixed_quadratic(state, invalid)
        for bad in (Parameters((np.ones((2, 1)),), np.ones(2)),
                    Parameters((np.ones((2, 2)), np.eye(2)), np.ones(2))):
            with self.assertRaises(ValueError):
                rms_quadratic(bad, 1.0, epsilon=0.1)
            with self.assertRaises(ValueError):
                mixed_quadratic(bad, 1.0)
        before = tuple(x.copy() for x in arrays(state))
        for result in (mixed_quadratic(state, 0.3), rms_quadratic(state, 0.3, epsilon=0.4)):
            for returned in (*arrays(result.ascent), *arrays(result.velocity),
                             *result.fields.values(), *result.field_ascent.values()):
                if isinstance(returned, np.ndarray):
                    for source in arrays(state):
                        self.assertFalse(np.shares_memory(returned, source))
            result.fields["h"][:] = 99
        for actual, saved in zip(arrays(state), before):
            np.testing.assert_array_equal(actual, saved)
        state.weights[1][0, 0] = np.nan
        with self.assertRaises(ValueError):
            mixed_lax(state, model="QI")


class FrozenQuadraticTests(unittest.TestCase):
    def test_raw_gradient_kernel_and_simultaneous_euler(self):
        # Differentiate the unreduced connector/readout loss in every coordinate.
        h = np.array([0.2, -0.7, 1.1])
        matrix = np.arange(9).reshape(3, 3) / 11.0 - 0.3
        a = np.array([-0.6, 0.4, 0.9])
        q, label, eps = h @ h / 3, -0.35, 1e-6
        def output(b, v):
            return np.sum(v * np.square(b @ h)) / (3 * np.sqrt(3))
        z = matrix @ h
        result = frozen_quadratic(a, z, q, label)
        gradients, jacobians = [], []
        for block, original in enumerate((matrix, a)):
            gradient, jacobian = np.empty_like(original), np.empty_like(original)
            for index in np.ndindex(original.shape):
                plus, minus = original.copy(), original.copy()
                plus[index] += eps
                minus[index] -= eps
                fp = output(plus, a) if block == 0 else output(matrix, plus)
                fm = output(minus, a) if block == 0 else output(matrix, minus)
                jacobian[index] = (fp - fm) / (2 * eps)
                gradient[index] = ((fp - label) ** 2 - (fm - label) ** 2) / (4 * eps)
            gradients.append(gradient)
            jacobians.append(jacobian)
        db, da = -gradients[0], -3 * gradients[1]
        np.testing.assert_allclose(result.readout_velocity, da, atol=1e-10, rtol=2e-7)
        np.testing.assert_allclose(result.preactivation_velocity, db @ h, atol=1e-10, rtol=2e-7)
        np.testing.assert_allclose(result.kernel_blocks,
                                   [np.sum(jacobians[0] ** 2), 3 * np.sum(jacobians[1] ** 2)],
                                   atol=1e-10, rtol=2e-7)
        eta = 0.07
        next_a, next_z = frozen_quadratic_step(a, z, q, eta, label)
        np.testing.assert_allclose(next_a, a + eta * da, atol=1e-11)
        np.testing.assert_allclose(next_z, (matrix + eta * db) @ h, atol=1e-11)
        speed = np.sum(db ** 2) + da @ da / 3
        self.assertAlmostEqual(-result.loss_velocity, speed, places=10)

    def test_physical_half_loss_and_recomputed_raw_interpolation(self):
        a, z, q, label = np.array([0.3, -0.8]), np.array([0.4, -0.2]), 0.7, 0.6
        result = frozen_quadratic(a, z, q, label)
        step = 1e-6
        def f(s):
            return np.mean((a + s * result.readout_velocity)
                           * (z + s * result.preactivation_velocity) ** 2) / np.sqrt(3)
        self.assertAlmostEqual((f(step) - f(-step)) / (2 * step),
                               result.output_velocity, places=9)
        self.assertAlmostEqual(((f(step) - label) ** 2 - (f(-step) - label) ** 2)
                               / (4 * step), result.loss_velocity, places=9)
        next_a, next_z = frozen_quadratic_step(a, z, q, 0.2, label)
        midpoint = frozen_quadratic((a + next_a) / 2, (z + next_z) / 2, q, label)
        self.assertAlmostEqual(midpoint.output, f(0.1), places=14)

    def test_zero_feature_zero_residual_and_return_ownership(self):
        a, z = np.array([0.3, -0.8]), np.array([0.4, -0.2])
        result = frozen_quadratic(a, z, 0.7)
        stopped = frozen_quadratic(a, z, 0.7, result.output)
        np.testing.assert_array_equal(stopped.readout_velocity, 0)
        np.testing.assert_array_equal(stopped.preactivation_velocity, 0)
        for eta in (0, 0.2):
            aa, zz = frozen_quadratic_step(a, z, 0.7, eta, result.output)
            np.testing.assert_array_equal(aa, a)
            np.testing.assert_array_equal(zz, z)
            self.assertFalse(np.shares_memory(aa, a))
            self.assertFalse(np.shares_memory(zz, z))
        zero = frozen_quadratic(a, np.zeros(2), 0)
        self.assertEqual(zero.loss, 0.5)
        np.testing.assert_array_equal(zero.kernel_blocks, 0)
        np.testing.assert_array_equal(zero.readout_velocity, 0)
        for arr in (result.kernel_blocks, result.readout_velocity, result.preactivation_velocity):
            self.assertFalse(np.shares_memory(arr, a))
            self.assertFalse(np.shares_memory(arr, z))

    def test_input_and_range_contract(self):
        for a, z, q in (([], [], 1), ([1], [1, 2], 1), ([[1]], [1], 1),
                        ([True], [1], 1), ([1j], [1], 1), (["1"], [1], 1),
                        ([np.nan], [1], 1), ([1], [np.inf], 1),
                        ([1], [1], -1), ([1], [1], 0), ([1], [1], True)):
            with self.subTest(a=a, z=z, q=q), self.assertRaises(ValueError):
                frozen_quadratic(a, z, q)
        for value in (-1, np.inf, np.nan, True, "0.1"):
            with self.assertRaises(ValueError):
                frozen_quadratic_step([1], [1], 1, value)
        for label in (np.inf, np.nan, True, "1"):
            with self.assertRaises(ValueError):
                frozen_quadratic([1], [1], 1, label)
        with self.assertRaises(ValueError):
            frozen_quadratic([1], [1e200], 1)
        with self.assertRaises(ValueError):
            frozen_quadratic_step([1], [2], 1, 1e308)


if __name__ == "__main__":
    unittest.main()
