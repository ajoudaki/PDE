"""Small deterministic exact checks; no historical artifacts or campaigns."""

from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial
import unittest

from pde.exact_calculus import (
    determinant, euler_pullback_words, forest_key, paired_euler_weights,
    quadratic_axis_certificate, revert_series,
)


def polynomial_composition(a, b, length):
    # Independent schoolbook powers, rather than production Horner composition.
    result = [Q(0)]*length
    power = [Q(1)] + [Q(0)]*(length-1)
    for coefficient in a:
        result = [x+coefficient*y for x, y in zip(result, power)]
        power = [sum((power[i]*b[k-i] for i in range(k+1) if k-i < len(b)), Q(0))
                 for k in range(length)]
    return result


def permutation_determinant(matrix):
    result = Q(0)
    for perm in permutations(range(len(matrix))):
        term = Q((-1)**sum(perm[i] > perm[j] for i in range(len(perm))
                          for j in range(i+1, len(perm))))
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        result += term
    return result


class EulerPullbackTests(unittest.TestCase):
    def test_words_against_independent_step_slot_enumeration(self):
        for order in range(6):
            for steps in range(5):
                expected = {}
                for slots in product(range(order+1), repeat=steps):
                    if sum(slots) == order:
                        word = tuple(k for k in slots if k)
                        expected[word] = expected.get(word, Q(0))+1
                result = euler_pullback_words(order, steps)
                self.assertEqual(result, expected)
                self.assertTrue(all(type(value) is Q for value in result.values()))

    def test_every_displayed_temporal_polynomial(self):
        expected = {
            1: ((0,),),
            2: ((0, -2), (0, 1)),
            3: ((0, -6, 0), (0, 3, -2), (0, -2, 2)),
            4: ((0, -14, 0, 0), (0, 7, -6, 0),
                (0, -Q(14, 3), 6, -Q(4, 3)), (0, Q(7, 2), -Q(11, 2), 2)),
            5: ((0, -30, 0, 0, 0), (0, 15, -14, 0, 0),
                (0, -10, 14, -4, 0), (0, Q(15, 2), -Q(77, 6), 6, -Q(2, 3)),
                (0, -6, Q(35, 3), -7, Q(4, 3))),
        }
        self.assertEqual(paired_euler_weights(0), ())
        for order, rows in expected.items():
            result = paired_euler_weights(order)
            self.assertEqual(result, rows)
            self.assertTrue(all(type(value) is Q for row in result for value in row))

    def test_nonlinear_scalar_euler_against_differential_words(self):
        # Direct polynomial Euler for v(x)=1+x^2, u(x)=2x+x^3 at x=1/3.
        # This tests operator order and moving v, independently of word counts.
        def multiply(a, b, length=None):
            full = len(a)+len(b)-1
            return [sum((a[i]*b[k-i] for i in range(len(a))
                         if 0 <= k-i < len(b)), Q(0))
                    for k in range(full if length is None else length)]

        def value(poly, x):
            return sum((c*x**k for k, c in enumerate(poly)), Q(0))

        def word_value(word):
            poly = [Q(0), Q(2), Q(0), Q(1)]
            for k in reversed(word):
                derivative = [poly[j]*Q(factorial(j), factorial(j-k))
                              for j in range(k, len(poly))]
                if not derivative:
                    return Q(0)
                power = [Q(1)]
                for _ in range(k):
                    power = multiply(power, [Q(1), Q(0), Q(1)])
                poly = [c/factorial(k) for c in multiply(derivative, power)]
            return value(poly, Q(1, 3))

        order = 6
        def direct(steps, scale):
            x = [Q(1, 3)]+[Q(0)]*order
            for _ in range(steps):
                velocity = multiply(x, x, order+1)
                velocity[0] += 1
                x = [x[0]]+[x[j]+scale*velocity[j-1] for j in range(1, order+1)]
            cube = multiply(multiply(x, x, order+1), x, order+1)
            return [2*a+b for a, b in zip(x, cube)]

        for steps in (0, 1, 2, 3):
            direct_single = direct(steps, 1)
            fine, coarse = direct(2*steps, 1), direct(steps, 2)
            for degree in range(order+1):
                words = euler_pullback_words(degree, steps)
                self.assertEqual(sum((weight*word_value(word) for word, weight in words.items()), Q(0)),
                                 direct_single[degree])
                rows = paired_euler_weights(degree)
                all_words = euler_pullback_words(degree, degree)
                assembled = sum((value(rows[len(word)-1], steps)*word_value(word)
                                 for word in all_words if word), Q(0))
                self.assertEqual(assembled, fine[degree]-coarse[degree])

    def test_domains_and_return_ownership(self):
        for invalid in (-1, True, 1.0, Q(1), "2", None):
            with self.assertRaises(ValueError):
                paired_euler_weights(invalid)
            with self.assertRaises(ValueError):
                euler_pullback_words(invalid, 0)
            with self.assertRaises(ValueError):
                euler_pullback_words(0, invalid)
        result = euler_pullback_words(3, 2)
        result[(3,)] = 0
        self.assertEqual(euler_pullback_words(3, 2)[(3,)], 2)


class FormalArithmeticTests(unittest.TestCase):
    def test_reversion_two_compositions_and_exact_known_inverse(self):
        self.assertEqual(revert_series([0, 1, 1, 0, 0, 0]), [0, 1, -1, 2, -5, 14])
        for a in ([0, Q(2, 3), 4, -1, 0, 7], [0, -3], [0, 63, 0, 12960, 0, 0, 2]):
            old = a.copy()
            b = revert_series(a)
            target = [0, 1] + [0]*(len(a)-2)
            self.assertEqual(polynomial_composition(a, b, len(a)), target)
            self.assertEqual(polynomial_composition(b, a, len(a)), target)
            self.assertEqual(a, old)
            self.assertTrue(all(type(x) is Q for x in b))

    def test_determinants_swaps_singular_empty_and_rational(self):
        for matrix in ([], [[0]], [[0, 2], [3, 4]], [[1, 2], [2, 4]],
                       [[Q(1, 3), 2, -3], [0, 4, Q(2, 7)], [2, 0, 1]]):
            old = [row.copy() for row in matrix]
            self.assertEqual(determinant(matrix), permutation_determinant(matrix))
            self.assertEqual(matrix, old)
            self.assertIs(type(determinant(matrix)), Q)

    def test_invalid_rational_inputs(self):
        for a in ([], [0], [1, 2], [0, 0, 1], [0, 1.0], [0, True], "01", [0, complex(1)]):
            with self.assertRaises(ValueError):
                revert_series(a)
        for a in ([[1, 2]], [[1], [2]], [[1.0]], [[True]], [1], "bad"):
            with self.assertRaises(ValueError):
                determinant(a)


class ForestTests(unittest.TestCase):
    def test_relabeling_all_orders_and_edge_orientations(self):
        colors = [(2, 1), (1, 2), (1, 2), (2, 0), (1, 4)]
        edges = [(0, 1), (0, 2), (3, 4)]
        reference = forest_key(colors, edges)
        for perm in permutations(range(5)):
            old_to_new = {old: new for new, old in enumerate(perm)}
            changed = [(old_to_new[v], old_to_new[u]) for u, v in reversed(edges)]
            self.assertEqual(forest_key([colors[i] for i in perm], changed), reference)
        self.assertEqual(hash(reference), hash(forest_key(colors, edges)))
        self.assertEqual(colors, [(2, 1), (1, 2), (1, 2), (2, 0), (1, 4)])

    def test_components_decorations_and_empty(self):
        self.assertEqual(forest_key([], []), ())
        one = forest_key([(1, 2)], [])
        self.assertEqual(forest_key([(1, 2), (1, 2)], []), one+one)
        self.assertNotEqual(one, forest_key([(2, 2)], []))
        self.assertNotEqual(one, forest_key([(1, 3)], []))
        self.assertNotEqual(forest_key([(1, 0), (2, 0)], []),
                            forest_key([(1, 0), (2, 0)], [(0, 1)]))

    def test_invalid_graphs(self):
        colors = [(1, 0), (2, 0), (1, 0), (2, 0)]
        for edges in ([(0, 0)], [(0, 2)], [(0, 4)], [(0, -1)], [(True, 1)],
                      [(0, 1), (1, 0)], [(0, 1), (1, 2), (2, 3), (3, 0)], [(0,)]):
            with self.assertRaises(ValueError):
                forest_key(colors, edges)
        for colors in ([(0, 1)], [(3, 0)], [(1, -1)], [(1, True)], [(1, 0.0)], [1], "bad"):
            with self.assertRaises(ValueError):
                forest_key(colors, [])


class CertificateTests(unittest.TestCase):
    def test_displayed_exact_certificate_and_independent_witness(self):
        result = quadratic_axis_certificate()
        self.assertEqual(result["derivatives"][1::2],
                         [63, 77760, 274547232, 2141006515200, 31149221916487680,
                          759035131220036321280, 28719223368439752070594560])
        self.assertEqual(result["derivatives"][::2], [0]*7)
        expected = [Q(480, 49), Q(43756, 151263), Q(7214528, 200120949),
                    Q(12545175968, 2402451992745), Q(171752915595136, 200241971143303005),
                    Q(2199776554157960896, 14570607030242443158825)]
        self.assertEqual(result["moments"], expected)
        matrix = [[expected[i+j+1] for j in range(3)] for i in range(3)]
        target = -Q(86245462994269879146938487857152, 200150589172828762588730609071155193161975)
        self.assertEqual(permutation_determinant(matrix), target)
        self.assertEqual(result["shifted_determinant"], target)
        v = [Q(40042013405871059816, 2310453239160606810795),
             -Q(14165989123115588, 49896409440894219), Q(1)]
        value = sum(v[i]*v[j]*expected[i+j+1] for i in range(3) for j in range(3))
        self.assertEqual(value, -Q(673792679642733430835456936384,
                                   329714727520793070279653295504327135))
        self.assertEqual(result["witness"], v)
        self.assertEqual(result["witness_value"], value)
        self.assertEqual(result["kernel"][1::2], [0]*6)
        self.assertEqual(result["kernel"][0], 63)
        result["moments"][0] = 0
        self.assertEqual(quadratic_axis_certificate()["moments"], expected)


if __name__ == "__main__":
    unittest.main()
