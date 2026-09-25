"""Deterministic exact-algebra and solver checks, not research trajectories."""

import math
import unittest

import numpy as np
from scipy.integrate import BDF, solve_ivp
from scipy.sparse import eye
from scipy.sparse.linalg import spsolve

from scalar_high_order_engine import ScalarHierarchy, StructuredBDF, recenter_coefficients
from scalar_long_time_engine import StiffSignatureHierarchy, recenter_coefficients as old_recenter


class HighOrderEngineTests(unittest.TestCase):
    def fixture(self, order, m=2, signatures=True, complex_values=False):
        rng = np.random.default_rng(740+order+m)
        coefficients = {"T"+str(j):.08*rng.normal(size=(m,)*j) for j in range(1, order+1)}
        if complex_values:
            coefficients = {name:value+.03j*rng.normal(size=value.shape) for name, value in coefficients.items()}
        labels = rng.normal(size=m)*.3
        model = ScalarHierarchy(coefficients, labels, order, signatures)
        state = model.initial_state()+.05*rng.normal(size=model.size)
        return model, state, coefficients, labels

    def test_all_jacobian_columns_by_complex_step_orders_two_through_six(self):
        for order in range(2, 7):
            for signatures in (False, True):
                model, state, _, _ = self.fixture(order, signatures=signatures)
                expected = model.jac(0., state).toarray()
                observed = np.empty_like(expected)
                for column in range(model.size):
                    probe = state.astype(complex)
                    probe[column] += 1e-30j
                    observed[:, column] = model.rhs(0., probe).imag/1e-30
                np.testing.assert_allclose(observed, expected, rtol=4e-14, atol=4e-15)

    def test_complex_tensor_jacobian_direction(self):
        rng = np.random.default_rng(150)
        for order in range(2, 7):
            model, state, _, _ = self.fixture(order, complex_values=True)
            direction = rng.normal(size=model.size)+1j*rng.normal(size=model.size)
            step = 2e-6
            finite = (model.rhs(0., state+step*direction)-model.rhs(0., state-step*direction))/(2*step)
            np.testing.assert_allclose(model.jac(0., state)@direction, finite, rtol=2e-8, atol=1e-10)

    def test_schur_newton_solve_against_dense_and_sparse_systems(self):
        rng = np.random.default_rng(751)
        for order in range(2, 7):
            for signatures in (False, True):
                for complex_values in (False, True):
                    model, state, _, _ = self.fixture(order, signatures=signatures, complex_values=complex_values)
                    jac = model.jac(0., state)
                    snapshot = model.linearize(state)
                    for gamma in (0., .17, -.3, .07+.12j):
                        matrix = eye(model.size, format="csc")-gamma*jac
                        rhs = rng.normal(size=model.size)+.2j*rng.normal(size=model.size)
                        factor = snapshot.factor(gamma)
                        observed = factor.solve(rhs)
                        np.testing.assert_allclose(observed, np.linalg.solve(matrix.toarray(), rhs), rtol=5e-13, atol=5e-13)
                        np.testing.assert_allclose(observed, spsolve(matrix, rhs), rtol=5e-13, atol=5e-13)
                        np.testing.assert_allclose(matrix@observed, rhs, rtol=5e-13, atol=5e-13)
                        multiple = np.column_stack((rhs, 2*rhs.conjugate()))
                        np.testing.assert_allclose(factor.solve(multiple), np.linalg.solve(matrix.toarray(), multiple),
                                                   rtol=5e-13, atol=5e-13)

    def test_snapshot_and_cached_factor_do_not_follow_mutable_state(self):
        model, state, coefficients, labels = self.fixture(6)
        snapshot = model.linearize(state)
        old_matrix = np.eye(model.size)-.13*model.jac(0., state).toarray()
        factor = snapshot.factor(.13)
        rhs = np.arange(model.size)*.01
        expected = np.linalg.solve(old_matrix, rhs)
        state += 7
        labels[:] = 9
        for coefficient in coefficients.values():
            coefficient[:] = -11
        model.linearize(state).factor(.7)
        np.testing.assert_allclose(factor.solve(rhs), expected, rtol=5e-13, atol=5e-13)
        for value in (*snapshot.tensors.values(), *snapshot.signatures.values(), snapshot.velocity):
            self.assertFalse(np.shares_memory(value, state))
            self.assertFalse(value.flags.writeable)

    def test_generic_order_four_matches_original_equations_and_recenter(self):
        model, state, coefficients, labels = self.fixture(4, m=3)
        old_names = ("f", "Theta", "C", "Q")
        old_coefficients = {name:coefficients["T"+str(j)] for j, name in enumerate(old_names, 1)}
        old = StiffSignatureHierarchy(old_coefficients, labels, 4)
        np.testing.assert_array_equal(model.initial_state(), old.initial_state())
        # The generic chain scales the residual before contraction. The old
        # implementation scales its contraction; this changes final rounding.
        np.testing.assert_allclose(model.rhs(0., state), old.rhs(0., state), rtol=2e-15, atol=2e-17)
        np.testing.assert_array_equal(model.jac(0., state).toarray(), old.jac(0., state).toarray())
        first = recenter_coefficients(coefficients, model.signatures(state))
        second = old_recenter(old_coefficients, old.signatures(state))
        for j, name in enumerate(old_names, 1):
            np.testing.assert_array_equal(first["T"+str(j)], second[name])

    @staticmethod
    def straight_signature(velocity, duration, order):
        result, product = {}, np.array(1.)
        for k in range(1, order):
            product = np.multiply.outer(velocity, product)
            result["sigma"+str(k)] = product*duration**k/math.factorial(k)
        return result

    def test_recenter_chen_composition_and_reset_preserves_training(self):
        for order in range(2, 7):
            model, state, coefficients, _ = self.fixture(order, complex_values=True)
            first = self.straight_signature(np.array([.3, -.2]), .8, order)
            later = self.straight_signature(np.array([-.1, .4]), .6, order)
            total = {}
            for k in range(1, order):
                value = np.zeros((2,)*k)
                for r in range(k+1):
                    left = later["sigma"+str(r)] if r else np.array(1.)
                    right = first["sigma"+str(k-r)] if k-r else np.array(1.)
                    value += np.multiply.outer(left, right).reshape((2,)*k)
                total["sigma"+str(k)] = value
            copies = {name:value.copy() for name, value in coefficients.items()}
            once = recenter_coefficients(coefficients, total)
            twice = recenter_coefficients(recenter_coefficients(coefficients, first), later)
            for name in coefficients:
                np.testing.assert_allclose(once[name], twice[name], rtol=2e-14, atol=2e-15)
                np.testing.assert_array_equal(coefficients[name], copies[name])
            self.assertIs(once["T"+str(order)], coefficients["T"+str(order)])
            reset = model.reset_signatures(state)
            np.testing.assert_array_equal(reset[:model.training_size], state[:model.training_size])
            np.testing.assert_array_equal(reset[model.training_size:], 0.)

    def test_recenter_matches_independent_forced_passive_evolution(self):
        rng = np.random.default_rng(887)
        for order in range(2, 7):
            m, count = 2, 3
            coefficients = {"T"+str(j):.1*rng.normal(size=(count,)+(m,)*(j-1))
                            +.03j*rng.normal(size=(count,)+(m,)*(j-1)) for j in range(1, order+1)}
            sizes = [count*m**(j-1) for j in range(1, order)]
            bounds = np.cumsum([0]+sizes)
            sig_sizes = [m**k for k in range(1, order)]
            sig_bounds = bounds[-1]+np.cumsum([0]+sig_sizes)
            initial = np.concatenate([coefficients["T"+str(j)].reshape(-1) for j in range(1, order)]
                                     +[np.zeros(sum(sig_sizes))])
            def forced_rhs(time, state):
                velocity = np.array([.3+.1*time, -.2+.07*time*time])
                fields = [state[bounds[j-1]:bounds[j]].reshape((count,)+(m,)*(j-1))
                          for j in range(1, order)]+[coefficients["T"+str(order)]]
                result = [np.tensordot(fields[j], velocity, axes=([-1], [0])).reshape(-1) for j in range(1, order)]
                previous = np.array(1.)
                for k in range(1, order):
                    result.append(np.multiply.outer(velocity, previous).reshape(-1))
                    previous = state[sig_bounds[k-1]:sig_bounds[k]].reshape((m,)*k)
                return np.concatenate(result)
            solution = solve_ivp(forced_rhs, (0., .9), initial, method="DOP853", rtol=1e-12, atol=1e-14)
            self.assertTrue(solution.success)
            final = solution.y[:, -1]
            signatures = {"sigma"+str(k):final[sig_bounds[k-1]:sig_bounds[k]].reshape((m,)*k)
                          for k in range(1, order)}
            actual = recenter_coefficients(coefficients, signatures)
            for j in range(1, order):
                expected = final[bounds[j-1]:bounds[j]].reshape((count,)+(m,)*(j-1))
                np.testing.assert_allclose(actual["T"+str(j)], expected, rtol=2e-11, atol=3e-13)

    def test_structured_bdf_inherits_steps_and_matches_stock_bdf(self):
        self.assertIs(StructuredBDF._step_impl, BDF._step_impl)
        for order in range(2, 7):
            for signatures in (False, True):
                model, initial, _, _ = self.fixture(order, signatures=signatures)
                common = dict(rtol=1e-9, atol=1e-11, dense_output=True)
                stock = solve_ivp(model.rhs, (0., 2.), initial, method="BDF", jac=model.jac, **common)
                structured = solve_ivp(model, (0., 2.), initial, method=StructuredBDF, **common)
                self.assertTrue(stock.success)
                self.assertTrue(structured.success)
                points = np.linspace(0., 2., 17)
                np.testing.assert_allclose(stock.sol(points), structured.sol(points), rtol=3e-7, atol=1e-9)
                self.assertEqual(stock.njev, structured.njev)
                self.assertEqual(stock.nlu, structured.nlu)

    def test_counts_and_validation(self):
        for order in range(2, 7):
            model, _, _, _ = self.fixture(order, m=3)
            self.assertEqual(model.size, 2*sum(3**j for j in range(1, order)))
            expected = 3**order+4*sum(3**j for j in range(2, order))+3
            self.assertEqual(model.jac(0., model.initial_state()).nnz, expected)
        for order in (1, 7, True, 3.5):
            with self.assertRaises(ValueError):
                ScalarHierarchy({"T1":np.zeros(2), "T2":np.eye(2)}, np.zeros(2), order)


if __name__ == "__main__":
    unittest.main()
