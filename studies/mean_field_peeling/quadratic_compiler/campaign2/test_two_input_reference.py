#!/usr/bin/env python3

import unittest

import two_input_reference as ref


class MomentTests(unittest.TestCase):
    def test_bivariate_low_moments(self):
        self.assertEqual(ref.bivariate_moment(2, 2), (1, 0, 2))
        self.assertEqual(ref.bivariate_moment(3, 1), (0, 3))
        self.assertEqual(ref.bivariate_moment(4, 0), (3,))
        self.assertEqual(ref.bivariate_moment(1, 0), (0,))

    def test_polynomial_arithmetic(self):
        self.assertEqual(ref.mul((1, 2), (3, 4)), (3, 10, 8))
        self.assertEqual(ref.add((1, -1), (-1, 1)), (0,))


class JetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plus = ref.run(1, 3)[1]
        cls.minus = ref.run(-1, 3)[1]

    def test_even_orders_vanish(self):
        self.assertEqual(self.plus[0], (0,))
        self.assertEqual(self.plus[2], (0,))
        self.assertEqual(self.minus[0], (0,))
        self.assertEqual(self.minus[2], (0,))

    def test_first_derivative(self):
        self.assertEqual(ref.theta_to_t(self.plus[1]), (63, 20, 28))
        self.assertEqual(ref.theta_to_t(self.minus[1]), (48, -20, -28))

    def test_plus_endpoint_order_three(self):
        p = ref.theta_to_t(self.plus[3])
        self.assertEqual(sum(p), 1685184)

    def test_minus_forced_order_three_zero(self):
        # Divisibility by (1-t)^2 implies value and first derivative vanish at 1.
        p = ref.theta_to_t(self.minus[3])
        self.assertEqual(sum(p), 0)
        self.assertEqual(sum(i * x for i, x in enumerate(p)), 0)


if __name__ == "__main__":
    unittest.main()

