"""Independent closed-form and domain checks for exact Gaussian moments."""

from copy import deepcopy
from fractions import Fraction as Q
import unittest

from pde.gaussian_moments import gaussian_moment


class GaussianMomentTests(unittest.TestCase):
    def test_univariate_known_even_and_odd_moments(self):
        variance = Q(2, 3)
        standard_even = (1, 1, 3, 15, 105, 945, 10395)
        for half_degree, coefficient in enumerate(standard_even):
            value = gaussian_moment([[variance]], [2 * half_degree])
            self.assertIsInstance(value, Q)
            self.assertEqual(value, coefficient * variance**half_degree)
        for degree in (1, 3, 5, 7):
            self.assertEqual(gaussian_moment([[variance]], [degree]), Q(0))

    def test_correlated_bivariate_known_moments(self):
        covariance = [[2, Q(1, 3)], [Q(1, 3), 3]]
        expected = {
            (1, 1): Q(1, 3),
            (2, 2): Q(56, 9),
            (3, 3): Q(164, 9),
            (4, 2): Q(116, 3),
            (0, 4): Q(27),
            (2, 1): Q(0),
        }
        for powers, answer in expected.items():
            with self.subTest(powers=powers):
                self.assertEqual(gaussian_moment(covariance, powers), answer)

    def test_trivariate_pairings_and_negative_correlation(self):
        covariance = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
        # Six-leg pairings: 8 + 4 + 4 + 4 + 8 = 28.
        self.assertEqual(gaussian_moment(covariance, [2, 2, 2]), Q(28))
        self.assertEqual(gaussian_moment([[2, Q(-1, 3)], [Q(-1, 3), 3]], [3, 1]), Q(-2))

    def test_independent_coordinates_factor(self):
        diagonal = [[2, 0, 0], [0, 3, 0], [0, 0, Q(1, 2)]]
        self.assertEqual(gaussian_moment(diagonal, [4, 2, 2]), Q(18))
        self.assertEqual(gaussian_moment(diagonal, [1, 1, 2]), Q(0))

    def test_singular_rank_one_covariance(self):
        # X=(2Z,-Z,0), Z standard Gaussian, gives an independent scalar formula.
        covariance = [[4, -2, 0], [-2, 1, 0], [0, 0, 0]]
        self.assertEqual(gaussian_moment(covariance, [2, 4, 0]), Q(60))
        self.assertEqual(gaussian_moment(covariance, [3, 1, 0]), Q(-24))
        self.assertEqual(gaussian_moment(covariance, [2, 2, 2]), Q(0))
        self.assertEqual(gaussian_moment([[1, 1], [1, 1]], [2, 2]), Q(3))

    def test_zero_pivots_and_zero_covariance(self):
        covariance = [[0, 0, 0], [0, 2, 2], [0, 2, 2]]
        self.assertEqual(gaussian_moment(covariance, [0, 2, 2]), Q(12))
        self.assertEqual(gaussian_moment(covariance, [2, 2, 2]), Q(0))
        self.assertEqual(gaussian_moment([[0, 0], [0, 0]], [0, 0]), Q(1))
        self.assertEqual(gaussian_moment([[0, 0], [0, 0]], [2, 0]), Q(0))

    def test_permutation_preserves_moment(self):
        covariance = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]
        powers = [2, 3, 1]
        expected = gaussian_moment(covariance, powers)
        permutation = [2, 0, 1]
        permuted = [[covariance[i][j] for j in permutation] for i in permutation]
        self.assertEqual(gaussian_moment(permuted, [powers[i] for i in permutation]), expected)

    def test_inputs_unchanged_and_cache_does_not_cross_calls(self):
        covariance, powers = [[1, Q(1, 2)], [Q(1, 2), 1]], [2, 2]
        saved = deepcopy(covariance), powers.copy()
        self.assertEqual(gaussian_moment(covariance, powers), Q(3, 2))
        self.assertEqual((covariance, powers), saved)
        covariance[0][0] = 2
        self.assertEqual(gaussian_moment(covariance, powers), Q(5, 2))

    def test_shapes_and_finite_sequences(self):
        for covariance, powers in (([], []), ([[1, 0]], [2]), ([[1], [0]], [2, 2]), ([[1]], []), ([[1]], [1, 2])):
            with self.subTest(covariance=covariance, powers=powers), self.assertRaises(ValueError):
                gaussian_moment(covariance, powers)
        for covariance, powers in (("1", [2]), ([1], [2]), ([[1]], "2"), ([[1]], iter([2]))):
            with self.assertRaises(TypeError):
                gaussian_moment(covariance, powers)

    def test_invalid_covariance_entries_and_degrees(self):
        for value in (1.0, float("nan"), float("inf"), True, 1j, "1"):
            with self.assertRaises(TypeError):
                gaussian_moment([[value]], [2])
        for power in (1.0, Q(2), True, float("inf"), "2"):
            with self.assertRaises(TypeError):
                gaussian_moment([[1]], [power])
        with self.assertRaises(ValueError):
            gaussian_moment([[1]], [-2])

    def test_asymmetric_and_indefinite_covariance_rejected(self):
        invalid = (
            [[1, 0], [1, 1]], [[-1]], [[1, 2], [2, 1]],
            [[0, 1], [1, 2]], [[1, 1], [1, 1 - Q(1, 10**30)]],
            [[1, 0, 0], [0, 0, 1], [0, 1, 2]],
        )
        for covariance in invalid:
            for first_power in (0, 1, 2):
                # Validation cannot be bypassed by a constant or odd moment.
                powers = [first_power] + [0] * (len(covariance) - 1)
                with self.subTest(covariance=covariance, powers=powers), self.assertRaises(ValueError):
                    gaussian_moment(covariance, powers)


if __name__ == "__main__":
    unittest.main()
