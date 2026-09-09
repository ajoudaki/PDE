"""Small deterministic exact checks; no historical artifacts or campaigns."""

from fractions import Fraction, Fraction as Q
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


class GeneralForestCalculusTests(unittest.TestCase):
    """Independent finite sums and raw substitutions, without stored tables."""

    @staticmethod
    def value(forest, a, u, g):
        from fractions import Fraction
        n = len(a)
        neighbors = [[] for _ in forest.colors]
        for i, j in forest.edges:
            neighbors[i].append(j)
            neighbors[j].append(i)
        visited = set()

        def subtree(vertex, parent, label):
            population, exponent = forest.colors[vertex]
            value = (a if population == 1 else u)[label]**exponent
            visited.add(vertex)
            for child in neighbors[vertex]:
                if child == parent:
                    continue
                value *= sum((subtree(child, vertex, other) *
                              (g[label][other] if population == 1 else g[other][label])
                              for other in range(n)), Fraction(0))
            return value
        result = Fraction(1)
        for vertex in range(len(forest.colors)):
            if vertex not in visited:
                result *= sum((subtree(vertex, -1, label) for label in range(n)), Fraction(0))
        assert len(forest.edges) % 2 == 0
        return result/n**(len(forest.edges)//2 + forest.components)

    @staticmethod
    def direct_expectation(forest, n):
        from itertools import product
        from fractions import Fraction
        value = Fraction(0)
        for labeling in product(range(n), repeat=len(forest.colors)):
            powers = {}
            for vertex, (population, degree) in enumerate(forest.colors):
                key = (population, labeling[vertex])
                powers[key] = powers.get(key, 0) + degree
            for i, j in forest.edges:
                if forest.colors[i][0] == 2:
                    i, j = j, i
                key = (3, labeling[i], labeling[j])
                powers[key] = powers.get(key, 0) + 1
            term = 1
            for degree in powers.values():
                if degree % 2:
                    term = 0
                    break
                for k in range(1, degree, 2):
                    term *= k
            value += term
        return value/n**(len(forest.edges)//2 + forest.components)

    def test_finite_equality_partitions_against_unrestricted_label_sums(self):
        from pde.exact_calculus import GaussianForest, forest_expectation
        forests = [
            GaussianForest((), ()),
            GaussianForest(((1, 2),), ()),
            GaussianForest(((1, 2), (1, 2)), ()),
            GaussianForest(((1, 0), (2, 2), (2, 2)), ((0, 1), (0, 2))),
            GaussianForest(((1, 2), (1, 1), (1, 1), (2, 2), (2, 2), (2, 2), (2, 2)),
                           ((0, 3), (0, 4), (0, 5), (0, 6), (1, 3), (2, 3))),
        ]
        for forest in forests:
            for n in (1, 2, 3):
                self.assertEqual(forest_expectation(forest, width=n), self.direct_expectation(forest, n))
        self.assertEqual(forest_expectation(forests[-1]), 27)
        self.assertEqual(forest_expectation(forests[-2]), 3)
        self.assertEqual(forest_expectation(forests[2], width=3), Fraction(5, 3))
        odd = GaussianForest(((1, 0), (2, 0)), ((0, 1),))
        self.assertEqual(forest_expectation(odd, width=3), 0)
        self.assertEqual(forest_expectation(odd), 0)

    def test_derivative_polynomials_against_raw_ward_identities(self):
        from pde.exact_calculus import GaussianForest, quadratic_forest_derivatives, forest_expectation
        root = GaussianForest(((1, 1), (2, 2), (2, 2)), ((0, 1), (0, 2)))
        hidden = GaussianForest(((2, 2),), ())
        output_jets = quadratic_forest_derivatives(root, 2, alpha=Fraction(2, 3), beta=Fraction(4, 5))
        hidden_jets = quadratic_forest_derivatives(hidden, 3, alpha=Fraction(2, 3), beta=Fraction(4, 5))
        for k in range(1, 4):
            self.assertEqual(hidden_jets[k], {term: Fraction(16, 3)*value
                                             for term, value in output_jets[k-1].items()})
        for n in (1, 2):
            a = [Fraction(2+i, 3) for i in range(n)]
            u = [Fraction(1-i, 2) for i in range(n)]
            g = [[Fraction(1+2*i-j, 4) for j in range(n)] for i in range(n)]
            z_squared = [sum(g[i][j]*g[i][l]*u[j]**2*u[l]**2
                             for j in range(n) for l in range(n))/n for i in range(n)]
            da = z_squared
            du = [4*Fraction(2, 3)*sum(a[i]*g[i][j]*g[i][l]*u[j]*u[l]**2
                                       for i in range(n) for l in range(n))/n for j in range(n)]
            dg = [[2*Fraction(4, 5)*sum(a[i]*g[i][l]*u[j]**2*u[l]**2
                                       for l in range(n))/n for j in range(n)] for i in range(n)]
            expected = sum(da[i]**2 for i in range(n))/n
            expected += sum(du[j]**2 for j in range(n))/(n*Fraction(2, 3))
            expected += sum(dg[i][j]**2 for i in range(n) for j in range(n))/(n*Fraction(4, 5))
            actual = sum(coef*self.value(term, a, u, g) for term, coef in output_jets[1].items())
            self.assertEqual(actual, expected)
        boundary = quadratic_forest_derivatives(root, 1, alpha=0, beta=1)[1]
        self.assertEqual(sum(coef*forest_expectation(term) for term, coef in boundary.items()), 63)

    def test_simultaneous_euler_forest_pullback_against_direct_raw_vectors(self):
        from pde.exact_calculus import GaussianForest, quadratic_euler_pullback
        n = 2
        a, u = [Fraction(1, 2), Fraction(-2, 3)], [Fraction(2, 3), Fraction(-1, 4)]
        g = [[Fraction(1, 3), Fraction(2, 5)], [Fraction(-1, 2), Fraction(3, 7)]]
        roots = [GaussianForest(((1, 1), (2, 2), (2, 2)), ((0, 1), (0, 2))),
                 GaussianForest(((2, 2),), ()), GaussianForest(((2, 4),), ())]
        f = self.value(roots[0], a, u, g)
        for loss, step, label in ((False, Fraction(-1, 7), 1), (True, Fraction(1, 11), Fraction(2, 3))):
            s = 2*step*(label-f) if loss else step
            da = [sum(g[i][j]*g[i][l]*u[j]**2*u[l]**2
                      for j in range(n) for l in range(n))/n for i in range(n)]
            du = [4*sum(a[i]*g[i][j]*g[i][l]*u[j]*u[l]**2
                        for i in range(n) for l in range(n))/n for j in range(n)]
            dg = [[2*sum(a[i]*g[i][l]*u[j]**2*u[l]**2 for l in range(n))/n
                   for j in range(n)] for i in range(n)]
            aa = [x+s*y for x, y in zip(a, da)]
            uu = [x+s*y for x, y in zip(u, du)]
            gg = [[g[i][j]+s*dg[i][j] for j in range(n)] for i in range(n)]
            for root in roots:
                polynomial = quadratic_euler_pullback(root, step, loss=loss, label=label)
                self.assertEqual(sum(coef*self.value(term, a, u, g) for term, coef in polynomial.items()),
                                 self.value(root, aa, uu, gg))

    def test_weighted_parameter_tree_tensor_meaning(self):
        from pde.exact_calculus import gradient_tree_terms
        from math import factorial
        # f(x)=x^3/3, M=2, x=1. D=2*x^2*d/dx supplies a direct scalar check.
        derivatives = [Fraction(1, 3), Fraction(1), Fraction(2), Fraction(2)]
        expected = Fraction(1, 3)
        for order in range(6):
            trees = gradient_tree_terms(order)
            self.assertEqual(sum(weight for weight, edges in trees.values()), factorial(order))
            total = 0
            for weight, edges in trees.values():
                degrees = [0]*(order+1)
                for i, j in edges:
                    degrees[i] += 1
                    degrees[j] += 1
                value = weight*2**order
                for degree in degrees:
                    value *= derivatives[degree] if degree < len(derivatives) else 0
                total += value
            self.assertEqual(total, expected)
            expected *= 2*(order+3)

    def test_forest_domains_canonicalization_and_owned_polynomials(self):
        from pde.exact_calculus import (GaussianForest, forest_expectation,
            quadratic_forest_derivatives, quadratic_euler_pullback, gradient_tree_terms)
        colors, edges = [[1, 0], [2, 2], [2, 2]], [[0, 1], [0, 2]]
        forest = GaussianForest(colors, edges)
        same = GaussianForest(((2, 2), (1, 0), (2, 2)), ((0, 1), (2, 1)))
        self.assertEqual(forest, same)
        colors[0][1] = 9
        edges.clear()
        self.assertEqual(forest_expectation(forest), 3)
        for bad in (True, 1.0, -1):
            with self.assertRaises(ValueError):
                gradient_tree_terms(bad)
            with self.assertRaises(ValueError):
                forest_expectation(forest, width=bad)
        with self.assertRaises(ValueError):
            GaussianForest(((True, 0),), ())
        with self.assertRaises(ValueError):
            quadratic_forest_derivatives(GaussianForest(((2, 1),), ()), 1)
        for rate in (True, 0.5, -1):
            with self.assertRaises(ValueError):
                quadratic_forest_derivatives(forest, 1, alpha=rate)
        with self.assertRaises(ValueError):
            quadratic_euler_pullback(forest, 1, loss=1)
        with self.assertRaises(ValueError):
            quadratic_euler_pullback(forest, 1, label=2)
        levels = quadratic_forest_derivatives(forest, 0)
        levels[0].clear()
        self.assertEqual(quadratic_forest_derivatives(forest, 0)[0], {forest: 1})


class FiniteCertificateExtensionTests(unittest.TestCase):
    def test_singular_and_nonsingular_next_hankel_thresholds(self):
        from pde.exact_calculus import next_hankel_threshold, determinant
        self.assertEqual(next_hankel_threshold([], []), 0)
        self.assertEqual(next_hankel_threshold([[1, 2], [2, 4]], [3, 6]), 9)
        self.assertEqual(next_hankel_threshold([[0, 0], [0, 2]], [0, 3]), Fraction(9, 2))
        for A, b in (([[2, 1], [1, 3]], [1, 2]), ([[1]], [2])):
            threshold = next_hankel_threshold(A, b)
            full = [row[:] + [value] for row, value in zip(A, b)] + [b[:] + [threshold]]
            self.assertEqual(determinant(full), 0)
            full[-1][-1] += 1
            self.assertEqual(determinant(full), determinant(A))
        for A, b in (([[0, 1], [1, 0]], [0, 0]), ([[1, 2], [2, 4]], [1, 3]),
                     ([[1, 2], [1, 3]], [0, 0]), ([[True]], [1])):
            with self.assertRaises(ValueError):
                next_hankel_threshold(A, b)

    def test_bernstein_interval_conversion_and_degree_elevation(self):
        from pde.exact_calculus import bernstein_coefficients
        from math import comb
        coefficients = [Fraction(2), Fraction(-3), Fraction(5), Fraction(-7)]
        left, right = Fraction(-2, 3), Fraction(4, 5)
        for degree in (3, 5):
            beta = bernstein_coefficients(coefficients, left, right, degree=degree)
            for i in range(degree+1):
                t = Fraction(i, degree)
                x = left+(right-left)*t
                actual = sum(beta[j]*comb(degree, j)*t**j*(1-t)**(degree-j) for j in range(degree+1))
                self.assertEqual(actual, sum(c*x**j for j, c in enumerate(coefficients)))
        self.assertEqual(bernstein_coefficients([-1], 0, 1), (-1,))
        for args in (([], 0, 1), ([1], 1, 0), ([True], 0, 1), ([1], 0.0, 1)):
            with self.assertRaises(ValueError):
                bernstein_coefficients(*args)
        with self.assertRaises(ValueError):
            bernstein_coefficients([1], 0, 1, degree=True)

    def test_identity_shallow_step_matches_raw_vectors(self):
        from pde.exact_calculus import identity_shallow_step
        a, u = [Fraction(1, 2), Fraction(-2, 3)], [Fraction(2, 5), Fraction(3, 7)]
        f = sum(x*y for x, y in zip(a, u))/2
        q = sum(x*x+y*y for x, y in zip(a, u))/2
        d = sum(x*x-y*y for x, y in zip(a, u))/2
        label, rate, step = Fraction(2, 7), Fraction(3, 2), Fraction(1, 13)
        b = -2*rate*step*(f-label)
        aa, uu = [x+b*y for x, y in zip(a, u)], [y+b*x for x, y in zip(a, u)]
        expected = (sum(x*y for x, y in zip(aa, uu))/2,
                    sum(x*x+y*y for x, y in zip(aa, uu))/2,
                    sum(x*x-y*y for x, y in zip(aa, uu))/2)
        self.assertEqual(identity_shallow_step(f, q, d, label, rate, step), expected)
        for args in ((1, 1, 0, 1, 1, 1), (0, 2, 3, 1, 1, 1),
                     (0, 2, 0, 1, True, 1), (0, 2, 0, 1, 1, -1)):
            with self.assertRaises(ValueError):
                identity_shallow_step(*args)


class GaussianHeadTests(unittest.TestCase):
    def test_head_against_series_and_exact_gaussian_quadrature(self):
        # Rank-one blocks allow integration against two independent Gaussians.
        # Rational interpolatory quadrature is exact on degree-eight polynomials;
        # the independent oracle composes time series, not the Bell graph.
        from pde.exact_calculus import gaussian_hidden_head
        u, v = [1, 2, -1, 3, -2], [1, -2, 1, 3]
        covariance = [[Q(u[i]*u[j]) if i < 5 and j < 5 else
                       Q(v[i-5]*v[j-5]) if i >= 5 and j >= 5 else Q(0)
                       for j in range(9)] for i in range(9)]
        keys = ('lambda1', 'lambda2', 'lambda30', 'lambda32', 'lambda41',
                'lambda43', 'c10', 'd21', 'd30', 'd32')
        rates = dict(zip(keys, (Q(1, 3), Q(-1, 2), Q(2, 3), Q(1, 4),
                               Q(3, 5), Q(-2, 5), Q(1, 2), Q(2, 3),
                               Q(-1, 3), Q(1, 5))))
        result = gaussian_hidden_head(covariance, rates, [1, 1, 1])

        def raw(z0, v0, shift=0):
            z = [Q(z0)]
            r = [Q(v0)]
            h = [1+z0+z0*z0]
            d = [(1+2*z0)*v0]
            for j in range(1, 5):
                if j == 1:
                    zj = u[j]*z0 + rates['lambda1']*d[0]
                elif j == 2:
                    zj = u[j]*z0 + rates['lambda2']*d[1]
                elif j == 3:
                    zj = u[j]*z0 + rates['lambda30']*d[0] + 2*rates['lambda32']*d[2]
                else:
                    zj = u[j]*z0 + rates['lambda41']*d[1] + 6*rates['lambda43']*d[3]
                z.append(zj/factorial(j))
                h = polynomial_composition([1, 1, 1], z, j+1)
                if j < 4:
                    rj = (v[j]*v0 + rates['c10']*h[0] + shift if j == 1 else
                          v[j]*v0 + rates['d21']*h[1] if j == 2 else
                          v[j]*v0 + rates['d30']*h[0] + 2*rates['d32']*h[2])
                    r.append(rj/factorial(j))
                    slope = polynomial_composition([1, 2], z, j+1)
                    d = [sum((slope[k]*r[l-k] for k in range(l+1)), Q(0))
                         for l in range(j+1)]
            derivatives = [factorial(j)*h[j] for j in range(5)]
            return derivatives

        def normal_moment(k):
            return Q(0) if k % 2 else Q(factorial(k), 2**(k//2)*factorial(k//2))

        nodes = list(range(-4, 5))
        weights = []
        for node in nodes:
            polynomial = [Q(1)]
            for other in nodes:
                if node != other:
                    new = [Q(0)]*(len(polynomial)+1)
                    for k, coefficient in enumerate(polynomial):
                        new[k] -= other*coefficient/(node-other)
                        new[k+1] += coefficient/(node-other)
                    polynomial = new
            weights.append(sum((c*normal_moment(k) for k, c in enumerate(polynomial)), Q(0)))
        expected = dict.fromkeys(('gamma', 'gram13', 'gram22', 'A41'), Q(0))
        for z0, wz in zip(nodes, weights):
            for v0, wv in zip(nodes, weights):
                h = raw(Q(z0), Q(v0))
                expected['gamma'] += wz*wv*h[0]*h[4]
                expected['gram13'] += wz*wv*h[1]*h[3]
                expected['gram22'] += wz*wv*h[2]*h[2]
                # h4 has degree at most two in the separate V1 coordinate.
                expected['A41'] += wz*wv*(raw(Q(z0), Q(v0), 1)[4]-raw(Q(z0), Q(v0), -1)[4])/2
        for key, value in expected.items():
            self.assertEqual(result[key], value)
        self.assertEqual(result['A43'], 5*rates['lambda43'])
        self.assertEqual(result['squared_rms_fourth'],
                         2*result['gamma']+8*result['gram13']+6*result['gram22'])

    def test_head_domains_constant_and_owned_results(self):
        from pde.exact_calculus import gaussian_hidden_head
        import copy
        covariance = [[int(i == j) for j in range(9)] for i in range(9)]
        rates = dict.fromkeys(('lambda1', 'lambda2', 'lambda30', 'lambda32',
                               'lambda41', 'lambda43', 'c10', 'd21', 'd30', 'd32'), 1)
        original = copy.deepcopy((covariance, rates))
        result = gaussian_hidden_head(covariance, rates, [2])
        self.assertTrue(all(value == 0 and type(value) is Q for value in result.values()))
        result['gamma'] = 100
        self.assertEqual(gaussian_hidden_head(covariance, rates, [2])['gamma'], 0)
        self.assertEqual((covariance, rates), original)
        cases = []
        bad = copy.deepcopy(covariance); bad[0][0] = 2; cases.append((bad, rates, [1]))
        bad = copy.deepcopy(covariance); bad[0][5] = bad[5][0] = Q(1, 2); cases.append((bad, rates, [1]))
        bad = copy.deepcopy(covariance); bad[1][1] = -1; cases.append((bad, rates, [1]))
        bad = copy.deepcopy(covariance); bad[1][0] = 1; cases.append((bad, rates, [1]))
        cases += [(covariance, {}, [1]), (covariance, rates, []),
                  (covariance, {**rates, 'c10': True}, [1]), (covariance, rates, [1.0])]
        for args in cases:
            with self.assertRaises((ValueError, TypeError)):
                gaussian_hidden_head(*args)


if __name__ == "__main__":
    unittest.main()
