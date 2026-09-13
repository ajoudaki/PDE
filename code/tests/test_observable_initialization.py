"""Deterministic initializer checks only; no trajectory or neural simulation."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest
from dataclasses import replace
from fractions import Fraction
from unittest.mock import patch

import numpy as np


from pde import observable_words as words
from pde import observable_arithmetic as arithmetic
from pde import observable_compiler as compiler
from pde import observable_initialization as initialization


class ExactWordChecks(unittest.TestCase):
    @staticmethod
    def literal_tree_signature(word):
        if word is None:
            return None
        result, pending = [], [word]
        while pending:
            node = pending.pop()
            result.append((node.op, node.population, node.scalar, node.bounded, len(node.args)))
            pending.extend(reversed(node.args))
        return result

    def test_natural_code_mapping_matches_maintained_prefix_2048(self):
        from pde.observable_closure import decode_word as maintained_decode
        for code in range(2049):
            exact, previous = words.decode_word(code), maintained_decode(code)
            self.assertEqual(self.literal_tree_signature(exact),
                             self.literal_tree_signature(previous), msg=f"code {code}")
            if exact is not None and exact.bounded:
                self.assertIsInstance(exact.envelope, Fraction)

    def test_large_and_small_rational_envelopes_are_exact(self):
        huge, tiny = Fraction(1 << 20000, 3), Fraction(1, 1 << 20000)
        scaled = words.scale(huge, words.constant(1))
        self.assertEqual(scaled.scalar, huge)
        self.assertEqual(scaled.envelope, huge)
        self.assertEqual(words.scale(tiny, scaled).envelope, Fraction(1, 3))
        self.assertEqual(words.multiply(scaled, scaled).envelope, huge*huge)
        self.assertFalse(words.action(scaled).bounded)
        self.assertEqual(words.unary("tanh", words.action(scaled)).envelope, Fraction(1))
        self.assertIn("bounded=True", repr(scaled))
        with self.assertRaises(ValueError):
            words.scale(0.5, words.constant(1))

    def test_typing_and_literal_duplicates(self):
        self.assertEqual(words.constant(1), words.constant(1))
        self.assertNotEqual(words.constant(1), words.scale(1, words.constant(1)))
        self.assertEqual(words.scale(Fraction(2, 4), words.constant(1)),
                         words.scale(Fraction(1, 2), words.constant(1)))
        self.assertFalse(words.scale(0, words.seed("g1")).bounded)
        self.assertEqual(words.scale(0, words.constant(1)).envelope, Fraction(0))
        with self.assertRaises(ValueError):
            words.action(words.seed("g1"))
        with self.assertRaises(ValueError):
            words.multiply(words.seed("g1"), words.constant(1))
        with self.assertRaises(ValueError):
            words.add(words.constant(1), words.constant(2))
        with self.assertRaises(AttributeError):
            words.constant(1).envelope = Fraction(4)

    def test_deep_shared_dag_hash_equality_and_exact_growth(self):
        left, right = words.constant(1), words.constant(1)
        for _ in range(2500):
            left, right = words.add(left, left), words.add(right, right)
        self.assertEqual(left, right)
        self.assertEqual(hash(left), hash(right))
        self.assertEqual(len({left, right}), 1)
        self.assertEqual(left.envelope, Fraction(1 << 2500))
        self.assertNotEqual(left, words.scale(1, right))

    def test_deep_natural_decoder_uses_an_explicit_stack(self):
        code, expected = 2, words.seed("g1")
        for _ in range(2200):
            code = 4+8*code
            expected = words.unary("sin", expected)
        self.assertEqual(words.decode_word(code), expected)
        self.assertIs(words.decode_word(code), words.decode_word(code))

    def test_deep_chebyshev_dag_has_exact_syntax_envelope(self):
        degree = 1500
        coordinate = words.unary("tanh", words.seed("g1"))
        polynomial = initialization._polynomial_words((coordinate,), ((degree,),), degree)[0]
        self.assertTrue(polynomial.bounded)
        self.assertIsInstance(polynomial.envelope, Fraction)
        self.assertGreater(polynomial.envelope.numerator.bit_length(), 1024)
        self.assertIsInstance(hash(polynomial), int)


class InitializerChecks(unittest.TestCase):
    def make(self, order=1, q=64, p=79, digits=None, backend="decimal"):
        return initialization.initialize_features(
            order, arithmetic=arithmetic.Arithmetic(digits, backend),
            initialization_nodes=q, population_nodes=p, epsilon_cov="0.01")

    def test_dictionary_counts_nested_outputs_and_unretained_actions(self):
        previous = None
        for order, expected in ((1, (5, 3)), (2, (15, 6)), (3, (35, 10))):
            dictionary = initialization.build_dictionary(order)
            self.assertEqual((len(dictionary.first_words), len(dictionary.second_words)), expected)
            self.assertTrue(dictionary.fast_core)
            self.assertTrue(all(w.bounded for w in dictionary.first_words+dictionary.second_words))
            if previous is not None:
                self.assertTrue(set(previous.first_words) < set(dictionary.first_words))
                self.assertTrue(set(previous.second_words) < set(dictionary.second_words))
            previous = dictionary
        # Code 7 is unbounded and must not become a retained action query.
        seventh = initialization.build_dictionary(7)
        self.assertTrue(seventh.fast_core)
        self.assertNotIn(initialization.decode_word(7), seventh.first_words+seventh.second_words)

    def test_polynomial_named_derivatives_against_independent_differences(self):
        ar = arithmetic.Arithmetic()
        dictionary = initialization.build_dictionary(3)
        first = np.linspace(-1.1, 1.3, 52).reshape(13, 4)
        second = np.linspace(-1.2, 0.8, 26).reshape(13, 2)
        v, alpha, tau, step = 0.4, 0.7, 0.3, 1e-6
        base = initialization._core_tables(dictionary, first, second, v, alpha, tau, ar)
        for coordinate in range(2):
            plus, minus = first.copy(), first.copy()
            plus[:, 2+coordinate] += step/np.sqrt(tau)
            minus[:, 2+coordinate] -= step/np.sqrt(tau)
            fp = initialization._core_tables(dictionary, plus, second, v, alpha, tau, ar)[0]
            fm = initialization._core_tables(dictionary, minus, second, v, alpha, tau, ar)[0]
            np.testing.assert_allclose((fp-fm)/(2*step), base[2][:, :, coordinate], atol=2e-8, rtol=2e-8)
            plus, minus = second.copy(), second.copy()
            plus[:, coordinate] += step/np.sqrt(v)
            minus[:, coordinate] -= step/np.sqrt(v)
            fp = initialization._core_tables(dictionary, first, plus, v, alpha, tau, ar)[1]
            fm = initialization._core_tables(dictionary, first, minus, v, alpha, tau, ar)[1]
            np.testing.assert_allclose((fp-fm)/(2*step), base[3][:, :, coordinate], atol=2e-8, rtol=2e-8)

    def test_cholesky_orientation_against_raw_filter_oracle(self):
        ar = arithmetic.Arithmetic()
        raw1 = np.array([[1., -.8, .2], [1., .3, .9], [1., .7, -.6], [1., .4, .2]])
        raw2 = np.array([[1., -.6], [1., .4], [1., .9]])
        gram1, gram2 = raw1.T@raw1/len(raw1), raw2.T@raw2/len(raw2)
        C, eta = np.array([[.2, .1, -.3], [.4, -.1, .5]]), .07
        b1, b2, D = initialization._normalize(raw1, raw2, gram1, gram2, C, ar, eta)
        query = np.array([.3, -.4, 1.2, .8])
        actual = b2@D@(b1.T@query/len(raw1))
        expected = raw2@np.linalg.solve(gram2+eta*np.eye(2), C)@np.linalg.solve(
            gram1+eta*np.eye(3), raw1.T@query/len(raw1))
        np.testing.assert_allclose(actual, expected, atol=2e-14, rtol=2e-14)
        self.assertLessEqual(np.linalg.eigvalsh(b1.T@b1/len(b1)).max(), 1+1e-13)
        self.assertLessEqual(np.linalg.eigvalsh(b2.T@b2/len(b2)).max(), 1+1e-13)

    def test_constant_covariance_and_nonzero_response_terms(self):
        ar, q = arithmetic.Arithmetic(), 256
        result = self.make(q=q, p=q)
        v = float(result.metadata["core_constants"]["v"])
        alpha = float(result.metadata["core_constants"]["alpha"])
        tau = float(result.metadata["core_constants"]["tau_core"])
        dictionary = initialization.build_dictionary(1)
        raw1, raw2, d1, d2, g, h, upper = initialization._core_tables(
            dictionary, arithmetic.gaussian_points(q, 4, ar),
            arithmetic.gaussian_points(q, 2, ar), v, alpha, tau, ar)
        eta = 1/(1024*4)
        L1 = np.linalg.cholesky(raw1.T@raw1/q+eta*np.eye(5))
        L2 = np.linalg.cholesky(raw2.T@raw2/q+eta*np.eye(3))
        C = L2@result.D@L1.T
        self.assertAlmostEqual(C[1, 1], alpha*v, places=13)
        covariance = d2.mean(axis=0)@(raw1.T@h/q).T
        response = (raw2.T@upper/q)@d1.mean(axis=0).T
        self.assertGreater(response[1, 3], 0.01)
        np.testing.assert_allclose(C, covariance+response, atol=2e-13, rtol=2e-13)
        self.assertGreater(abs(C[1, 3]-covariance[1, 3]), 0.01)

    def test_independent_population_axis_and_all_three_orders(self):
        for order in (1, 2, 3):
            small, large = self.make(order, p=31), self.make(order, p=53)
            np.testing.assert_array_equal(small.g, large.g[:31])
            np.testing.assert_allclose(small.b1, large.b1[:31], atol=3e-14, rtol=3e-14)
            np.testing.assert_allclose(small.b2, large.b2[:31], atol=3e-14, rtol=3e-14)
            np.testing.assert_array_equal(small.D, large.D)
            self.assertFalse(small.metadata["epsilon_cov_used"])
            json.dumps(small.metadata)

    def test_retained_constant_tail_has_no_rank_pruning(self):
        dictionary = initialization.build_dictionary(4)
        self.assertEqual((len(dictionary.first_words), len(dictionary.second_words)), (71, 15))
        self.assertEqual(dictionary.tail_codes, (4,))
        result = self.make(4, q=8, p=9)
        self.assertEqual(result.metadata["feature_dimensions"], [71, 15])
        self.assertEqual(result.metadata["retained_tail_codes"], [4])
        self.assertFalse(result.metadata["epsilon_cov_used"])
        self.assertEqual(result.b1.shape, (9, 71))

    def test_decimal_refines_fixed_finite_initializer(self):
        low, high = self.make(2, q=16, p=19, digits=30), self.make(2, q=16, p=19, digits=50)
        with arithmetic.Arithmetic(60).context():
            difference = max(abs(a-b) for a, b in zip(low.D.flat, high.D.flat))
        self.assertLess(difference, arithmetic.Arithmetic(60).real("1e-22"))
        floating = self.make(2, q=16, p=19)
        np.testing.assert_allclose(np.asarray(high.D, dtype=float), floating.D, atol=2e-10, rtol=2e-10)

    def test_rational_backend_small_static_initializer(self):
        fixed = self.make(1, q=3, p=4, digits=20, backend="rational")
        decimal = self.make(1, q=3, p=4, digits=30)
        np.testing.assert_allclose(np.asarray(fixed.D, dtype=float), np.asarray(decimal.D, dtype=float),
                                   atol=2e-12, rtol=2e-12)
        self.assertEqual(fixed.metadata["arithmetic_backend"], "rational")
        json.dumps(fixed.metadata)

    def test_real_generic_compiler_dispatch_on_small_action_fixture(self):
        # Exercise the actual fallback integration without allocating degree 60.
        # The fixture is explicit; this is not an executed full-order-60 claim.
        base = initialization.build_dictionary(1)
        extra = initialization.unary("sin", initialization.action(initialization.constant(1)))
        fixture = replace(base, second_words=base.second_words+(extra,), second_tail=(extra,), fast_core=False)
        with patch.object(initialization, "build_dictionary", return_value=fixture):
            result = self.make(q=24, p=29)
        self.assertEqual(result.D.shape, (4, 5))
        self.assertEqual(result.b1.shape, (29, 5))
        self.assertEqual(result.metadata["initialization_strategy"], "complete-gaussian-program")
        self.assertTrue(result.metadata["epsilon_cov_used"])
        self.assertTrue(np.isfinite(result.D).all())

    def test_resource_rejection_precedes_cloud_allocation(self):
        calls = []
        def forbidden_rule(*args):
            calls.append(args)
            raise AssertionError("should not allocate")
        with self.assertRaises(initialization.InitializationResourceLimit):
            initialization.initialize_features(2, arithmetic=arithmetic.Arithmetic(),
                initialization_nodes=8, population_nodes=9, epsilon_cov="0.01",
                limits=initialization.InitializationLimits(max_working_bytes=1),
                gaussian_points=forbidden_rule)
        self.assertEqual(calls, [])
        with self.assertRaises(initialization.InitializationResourceLimit):
            initialization.build_dictionary(1, limits=initialization.InitializationLimits(max_features_per_population=4))


if __name__ == "__main__":
    unittest.main(verbosity=2)
