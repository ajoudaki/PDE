"""Exact algebra and independent Gaussian identities for mfp_expr."""

import math
import unittest
from fractions import Fraction

from pde.mfp_expr import (
    Expr, UnsupportedExpression, const, diff, evaluate, expand,
    gaussian_expectation, phi, render, substitute, symbol, symbols,
)


class ExpressionTests(unittest.TestCase):
    def setUp(self):
        self.x, self.y = symbol("x"), symbol("y")

    def test_exact_constants_and_arithmetic(self):
        self.assertEqual(const(1) / 3 + Fraction(1, 6), const(Fraction(1, 2)))
        self.assertEqual(4 / const(2), const(2))
        self.assertEqual(const(2.5) + 1, const(3.5))
        self.assertIsInstance(const(3).value, Fraction)

    def test_decimal_float_constants_have_exact_symbolic_arithmetic(self):
        self.assertEqual(const(0.1) + 0.2 - 0.3, const(0))
        self.assertEqual(const(0.1), const(Fraction(1, 10)))
        self.assertIsInstance(const(0.1).value, Fraction)

    def test_canonical_commutative_arithmetic(self):
        x, y = self.x, self.y
        self.assertEqual(2 * x + 3 * x - x, 4 * x)
        self.assertEqual(x * y * x, y * x**2)
        self.assertEqual(x + y, y + x)
        self.assertEqual((x * y) ** 3, x**3 * y**3)
        self.assertEqual((x**2) ** 3, x**6)
        self.assertEqual((x + y) - (x + y), const(0))
        self.assertEqual(hash(x * y), hash(y * x))
        self.assertEqual(len({symbol("x"), x}), 1)

    def test_distributive_expansion(self):
        x, y = self.x, self.y
        self.assertEqual(expand((x + y) ** 3), x**3 + 3*x**2*y + 3*x*y**2 + y**3)
        self.assertEqual(expand((x + y)*(x - y)), x**2-y**2)

    def test_chain_and_product_rules(self):
        x, y = self.x, self.y
        self.assertEqual(diff(phi(x*y, 2), x), y * phi(x*y, 3))
        self.assertEqual(diff(phi(phi(x)), x), phi(phi(x), 1) * phi(x, 1))
        self.assertEqual(diff(x**5, x), 5*x**4)
        self.assertEqual(diff(phi(x), y), const(0))
        self.assertEqual(diff(x*y*x, x), 2*x*y)

    def test_simultaneous_substitution(self):
        x, y = self.x, self.y
        self.assertEqual(substitute(x + 2*y, {x: y, y: 3}), y + 6)
        self.assertEqual(substitute(phi(x*y), {x*y: 2}), phi(2))
        self.assertEqual(symbols(phi(x*y) + x), frozenset((x, y)))

    def test_numeric_evaluation_with_polynomial_activation(self):
        # phi(t)=t^3; this oracle gives its exact derivatives independently.
        def cubic(order, value):
            if order > 3:
                return 0
            return math.factorial(3) // math.factorial(3-order) * value**(3-order)
        x, y = self.x, self.y
        expression = phi(x*y) + phi(x, 1) - phi(y, 2)
        self.assertEqual(evaluate(expression, {x: 2, y: 3}, cubic), 210)
        self.assertEqual(evaluate(diff(expression, x), {x: 2, y: 3}, cubic), 336)

    def test_render_retains_derivative_order_and_source_names(self):
        rendered = render(phi(self.x, 2) + self.y**3)
        self.assertIn("phi^(2)(x)", rendered)
        self.assertIn("(y)^3", rendered)

    def test_rejects_unsupported_and_nonfinite_operations(self):
        for value in (float("inf"), float("nan"), "3", 1j):
            with self.assertRaises(UnsupportedExpression):
                const(value)
        for exponent in (-1, 0.5, True):
            with self.assertRaises(UnsupportedExpression):
                self.x**exponent
        with self.assertRaises(UnsupportedExpression):
            self.x / self.y
        with self.assertRaises(ZeroDivisionError):
            self.x / 0
        with self.assertRaises(UnsupportedExpression):
            phi(self.x, -1)
        with self.assertRaises(UnsupportedExpression):
            diff(self.x, self.x + 1)
        with self.assertRaises(UnsupportedExpression):
            Expr("inverse", (self.x,))


class GaussianTests(unittest.TestCase):
    def setUp(self):
        self.g, self.h = symbol("G"), symbol("H")
        self.atoms = {}

    def atom(self, expression):
        if expression not in self.atoms:
            self.atoms[expression] = symbol(f"I{len(self.atoms)}")
        return self.atoms[expression]

    def expect(self, expression, covariance=None, flat_only=False):
        if covariance is None:
            covariance = {(self.g, self.g): 1}
        return gaussian_expectation(expression, (self.g, self.h), covariance, self.atom, flat_only)

    def test_standard_normal_moments_without_atoms(self):
        # Independent closed moments: odd=0 and E[G^(2k)]=(2k-1)!!.
        for power, expected in ((0, 1), (1, 0), (2, 1), (3, 0), (4, 3), (5, 0), (6, 15)):
            self.assertEqual(self.expect(self.g**power), const(expected))
        self.assertEqual(self.atoms, {})

    def test_bivariate_wick_with_symbolic_covariance(self):
        a, b, c = symbol("a"), symbol("b"), symbol("c")
        covariance = {(self.g, self.g): a, (self.g, self.h): c, (self.h, self.h): b}
        self.assertEqual(expand(self.expect(self.g**2*self.h**2, covariance)), a*b + 2*c**2)
        self.assertEqual(self.expect(self.g**3*self.h, covariance), 3*a*c)

    def test_nonzero_mean_is_an_explicit_shift(self):
        mean = symbol("mu")
        self.assertEqual(self.expect((mean + self.g)**3), mean**3 + 3*mean)

    def test_stein_activation_identity(self):
        variance = symbol("q")
        result = self.expect(self.g * phi(self.g), {(self.g, self.g): variance})
        self.assertEqual(result, variance*self.atom(phi(self.g, 1)))
        self.assertEqual(set(self.atoms), {phi(self.g, 1)})

    def test_second_stein_and_product_derivatives(self):
        g, h = self.g, self.h
        q, c = symbol("q"), symbol("c")
        result = self.expect(g**2*phi(g), {(g, g): q})
        self.assertEqual(expand(result), q*self.atom(phi(g)) + q**2*self.atom(phi(g, 2)))
        covariance = {(g, g): q, (g, h): c, (h, h): 2}
        result = self.expect(g*phi(g)*phi(h), covariance)
        expected = q*self.atom(phi(g, 1)*phi(h)) + c*self.atom(phi(g)*phi(h, 1))
        self.assertEqual(result, expected)

    def test_singular_coordinates_remain_formally_distinct(self):
        g, h = self.g, self.h
        covariance = {(g, g): 1, (g, h): 1, (h, h): 1}
        self.assertNotEqual(g, h)
        self.assertEqual(diff(phi(g), h), const(0))
        self.assertEqual(self.expect((g-h)**2, covariance), const(0))
        self.expect(phi(g), covariance)
        self.expect(phi(h), covariance)
        self.assertEqual(set(self.atoms), {phi(g), phi(h)})
        self.assertEqual(self.expect(g*phi(h), covariance), self.atom(phi(h, 1)))

    def test_deterministic_coefficients_are_pulled_out(self):
        coefficient = symbol("s")
        self.assertEqual(self.expect(coefficient*phi(self.g) + 2*coefficient), coefficient*self.atom(phi(self.g)) + 2*coefficient)
        self.assertEqual(self.expect(phi(coefficient)), phi(coefficient))

    def test_nested_phi_uses_general_integral_without_stein_loop(self):
        g = self.g
        expressions = (g*phi(g**2), g**2*phi(phi(g)), phi(g + phi(g)))
        for expression in expressions:
            self.assertEqual(self.expect(3*expression), 3*self.atom(expression))
            with self.assertRaises(UnsupportedExpression):
                self.expect(expression, flat_only=True)
        self.assertEqual(set(self.atoms), set(expressions))

    def test_flat_mode_rejects_every_nonliteral_activation_argument(self):
        for expression in (phi(self.g + self.h), phi(2*self.g), phi(1), phi(symbol("s"))):
            with self.assertRaises(UnsupportedExpression):
                self.expect(expression, flat_only=True)
        self.assertEqual(self.expect(phi(self.g, 3)**2, flat_only=True), self.atom(phi(self.g, 3)**2))

    def test_nested_and_flat_summands_reduce_separately(self):
        g = self.g
        result = self.expect(g*phi(g**2) + g*phi(g) + g**4)
        expected = self.atom(g*phi(g**2)) + self.atom(phi(g, 1)) + 3
        self.assertEqual(result, expected)

    def test_input_contract_errors(self):
        g, h = self.g, self.h
        for covariance in ({(g, g): g}, {(g, h): 1, (h, g): 2}, {(g, symbol("unknown")): 0}):
            with self.assertRaises(UnsupportedExpression):
                self.expect(g, covariance)
        with self.assertRaises(UnsupportedExpression):
            gaussian_expectation(g, (g, g), {}, self.atom)
        with self.assertRaises(UnsupportedExpression):
            gaussian_expectation(phi(g), (g,), {}, lambda expression: g)


if __name__ == "__main__":
    unittest.main()
