"""Small deterministic exact checks; no historical artifacts or campaigns."""

from fractions import Fraction as Q
from itertools import permutations
import unittest

from pde.exact_calculus import determinant, forest_key, quadratic_axis_certificate, revert_series


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
