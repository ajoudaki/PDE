"""Deterministic source identities, independent of trained trajectories."""
import unittest
from fractions import Fraction

import numpy as np

from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_compiler import GaussianCompiler
from depth_initialization import (
    DepthGaussianCompiler, root, one, unary, action, add, dictionary, initialize,
    _condition_diagnostic, _finite_float,
)


class InitializerTests(unittest.TestCase):
    def compiler(self, depth=3, dimension=2, digits=None, backend="decimal"):
        return DepthGaussianCompiler(depth, dimension, Arithmetic(digits, backend),
                                     gaussian_points, 24, Fraction(1, 100))

    def test_depth_two_exact_maintained_compiler_parity(self):
        h = unary("tanh", root(1))
        z = action(h, 2)
        H = unary("tanh", z)
        p = action(H, 1)
        words = (h, z, H, p, action(unary("tanh", p), 2))
        ar = Arithmetic()
        old = GaussianCompiler(ar, gaussian_points, 24, Fraction(1, 100)).compile(words, 17)
        new = self.compiler(2).compile(words, 17)
        for word in words:
            np.testing.assert_array_equal(new.evaluate(word), old.evaluate(word))
            np.testing.assert_array_equal(new.evaluate(word, 17), old.evaluate(word, 17))

    def test_matrix_identity_and_opposite_response(self):
        h = unary("tanh", root(1))
        forward2 = action(h, 2)
        reverse3 = action(one(3), 2)
        operand = unary("tanh", add(forward2, reverse3))
        forward3, reverse2 = action(operand, 3), action(operand, 1)
        program = self.compiler().compile((forward2, reverse3, operand, forward3, reverse2))
        i2, i3 = program._word(forward2, False), program._word(reverse3, False)
        s2, s3 = program.sources[i2], program.sources[i3]
        self.assertEqual(program.factors[2][s3.index, s2.index], 0)
        derivative = np.mean(1-program.evaluate(operand)**2)
        f = program.sources[program._word(forward3, False)]
        r = program.sources[program._word(reverse2, False)]
        self.assertEqual(len(f.response), 1)
        self.assertEqual(len(r.response), 1)
        self.assertEqual(f.response[0][0], program._word(one(3), False))
        self.assertEqual(r.response[0][0], program._word(h, False))
        self.assertAlmostEqual(f.response[0][1], derivative, places=13)
        self.assertAlmostEqual(r.response[0][1], derivative, places=13)
        _, gradient = program.evaluate(operand, derivative=True)
        expected = 1-program.evaluate(operand)**2
        np.testing.assert_allclose(gradient[:, s2.index], expected, rtol=0, atol=1e-14)
        np.testing.assert_allclose(gradient[:, s3.index], expected, rtol=0, atol=1e-14)

    def test_four_layers_and_three_full_row_coordinates(self):
        h = unary("tanh", root(3))
        words = [h]
        for layer in (2, 3, 4):
            h = unary("tanh", action(h, layer))
            words.append(h)
        for layer in (3, 2, 1):
            h = unary("tanh", action(h, layer))
            words.append(h)
        program = self.compiler(4, 3).compile(words)
        self.assertEqual(set(program.source_lists), {1, 2, 3, 4})
        for word in words:
            self.assertTrue(np.all(np.isfinite(program.evaluate(word, 13))))
        with self.assertRaises(ValueError):
            action(one(1), 3)

    def test_core_feature_counts_and_nested_words(self):
        previous = [set(), set(), set()]
        for order, counts in ((1, (5, 5, 3)), (3, (35, 35, 10)), (5, (127, 126, 21))):
            lists = dictionary(order, 3, 2)
            self.assertEqual(tuple(map(len, lists)), counts)
            for old, words in zip(previous, lists):
                self.assertTrue(old.issubset(set(words)))
            previous = [set(words) for words in lists]

    def test_large_fixed_dimension_has_no_recursion_ceiling(self):
        lists = dictionary(1, 3, 600)
        self.assertEqual(tuple(map(len, lists)), (1201, 1201, 601))

    def test_float_diagnostics_do_not_limit_exact_values(self):
        enormous = Fraction(10**1000)
        self.assertIsNone(_finite_float(enormous))
        self.assertIsNone(_condition_diagnostic(np.asarray([[enormous]], object), Fraction(1, 100)))

    def test_exact_backend_small_program(self):
        h = unary("tanh", root(1))
        z = action(h, 2)
        p = action(unary("tanh", z), 1)
        program = self.compiler(3, 2, 24, "rational").compile((z, p))
        self.assertTrue(program.ar.finite(program.evaluate(p, 9)))

    def test_initialization_has_complete_joint_marks_and_no_transcript(self):
        result = initialize(1, 3, 2, initialization_nodes=24, population_nodes=13)
        self.assertEqual([a.shape for a in result["b"]], [(13, 5), (13, 5), (13, 3)])
        self.assertEqual([a.shape for a in result["D"]], [(5, 5), (3, 5)])
        self.assertEqual(result["g"].shape, (13, 2))
        self.assertNotIn("program", result)
        self.assertEqual(len(result["metadata"]["reverse_contraction_discrepancies"]), 2)


if __name__ == "__main__":
    unittest.main()
