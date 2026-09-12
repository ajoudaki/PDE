#!/usr/bin/env python3
"""Deterministic arithmetic, quadrature, and contraction checks; no trajectory."""
from decimal import Decimal as D
from fractions import Fraction as F
import copy
from pathlib import Path
import tempfile
import unittest

import H3_shorttime_solver as s


def enclosed(interval, exact):
    # Compare decimal endpoints to exact rational numbers without rounding.
    return F(interval.lo) <= exact <= F(interval.hi)


class IntervalTests(unittest.TestCase):
    def test_arithmetic_against_exact_rationals(self):
        for a in [F(-7, 3), F(-1, 11), F(0), F(2, 7), F(17, 13)]:
            for b in [F(-3, 5), F(1, 19), F(4, 3)]:
                x, y = s.rational(a), s.rational(b)
                self.assertTrue(enclosed(x + y, a + b))
                self.assertTrue(enclosed(x - y, a - b))
                self.assertTrue(enclosed(x * y, a * b))
                self.assertTrue(enclosed(x / y, a / b))
                self.assertTrue(enclosed(x ** 4, a ** 4))
        self.assertTrue(enclosed(s.I(-1, 2) ** 2, F(0)))
        self.assertTrue(enclosed(s.I(-1, 2) ** 2, F(4)))

    def test_exp_against_rational_series(self):
        # exp(1) sum through 119 plus a geometric bound on the positive tail.
        factorial, total = 1, F(1)
        for k in range(1, 120):
            factorial *= k
            total += F(1, factorial)
        remainder = F(1, factorial * 120) / (1 - F(1, 121))
        interval = s.I(1).exp()
        self.assertLessEqual(F(interval.lo), total)
        self.assertGreaterEqual(F(interval.hi), total + remainder)

    def test_pi_and_symmetry(self):
        self.assertGreater(s.PI.lo, D("3.14159265358979323846264338327950288419716939937510"))
        self.assertLess(s.PI.hi, D("3.14159265358979323846264338327950288419716939937511"))
        z = s.I("0.71").tanh()
        minus = s.I("-0.71").tanh()
        self.assertLessEqual(z.lo, -minus.lo)
        self.assertGreaterEqual(z.hi, -minus.hi)

    def test_zero_variance_quadrature(self):
        moments, _ = s.gaussian_moments(s.I(0), panels=512)
        for name in ["s2", "s3", "s4"]:
            self.assertTrue(enclosed(moments[name], F(1)))
        for name in ["h2", "h4", "h6", "h2s2", "h2s4", "zh", "zhs3", "z2s2"]:
            self.assertTrue(enclosed(moments[name], F(0)))


class AlgebraTests(unittest.TestCase):
    def test_upper_contraction_against_exact_four_point_sum(self):
        # Independence/oddness identities are algebraic. A symmetric rational
        # four-point product law gives an independent exact arithmetic oracle.
        h, H, z = F(1, 2), F(1, 4), F(1, 2)
        l, gate = 1 - h*h, 1-H*H
        g = {"h2": h*h, "s2": l*l, "h2s2": h*h*l*l,
             "s4": l**4, "h2s4": h*h*l**4}
        u = {"h2": H*H, "h4": H**4, "s2": gate**2, "s3": gate**3,
             "s4": gate**4, "h2s2": H*H*gate**2, "h2s4": H*H*gate**4,
             "zh": z*H, "zhs3": z*H*gate**3, "z2s2": z*z*gate**2}
        coeff = s.reference_coefficients({k: s.rational(v) for k, v in g.items()},
                                         {k: s.rational(v) for k, v in u.items()})
        q, k = g["h2"], u["h2"]
        a, gamma = 1 - 4*k + 3*u["h4"], (1-k)**2
        v = u["h2s2"] + k*u["s2"]
        V = g["s4"]*(v+gamma**2*q)+a*a*g["h2s4"]
        c1, c2 = a*g["h2s2"], -gamma*g["s2"]*q
        A, B, C = c1/q, c2/q, q+g["s2"]
        residual = V-(c1*c1+c2*c2)/q
        oracle = F(0)
        for sign1 in [-1, 1]:
            for sign2 in [-1, 1]:
                mean = A*sign1*z+B*sign2*z+C*(sign1*H-sign2*H)*gate
                oracle += gate**2*(mean*mean+residual)/4
        self.assertTrue(enclosed(coeff["n1sq"], V))
        self.assertTrue(enclosed(coeff["n2sq"], oracle))

    def test_symbolic_derivative_bound_is_not_zero(self):
        expected = {"h2": 1098, "h2s4": 788640, "z2s2": 20952}
        for name, exact in expected.items():
            self.assertEqual(s.fourth_derivative_bound(name), exact)


class CheckpointTests(unittest.TestCase):
    @staticmethod
    def coefficients():
        return {"q": s.I(".39", ".40"), "k": s.I(".23", ".24"),
                "alpha": s.I(".2", ".3"), "gamma": s.I(".4", ".5"),
                "v": s.I(".1", ".2"), "n1sq": s.I(".1", ".2"),
                "n2sq": s.I(".2", ".3")}

    def test_saved_nonzero_interval_width_survives_reload(self):
        b, beta = s.I(".002", ".003"), s.I(".000002", ".000005")
        with tempfile.TemporaryDirectory(prefix="H3_shorttime_test_") as temporary:
            path = Path(temporary) / "checkpoint.json"
            s.save_checkpoint(path, F(1, 400), b, beta, self.coefficients())
            elapsed, loaded_b, loaded_beta, coeff = s.load_checkpoint(path)
            self.assertEqual(elapsed, F(1, 400))
            self.assertEqual(loaded_b.record(), b.record())
            self.assertEqual(loaded_beta.record(), beta.record())
            self.assertEqual(coeff["q"].record(), self.coefficients()["q"].record())
            with self.assertRaises(FileExistsError):
                s.save_checkpoint(path, elapsed, loaded_b, loaded_beta, coeff)

    def test_invalid_checkpoint_rejection(self):
        original = s.checkpoint_encode(F(1, 400), s.I(".002"), s.I(".000002"),
                                       self.coefficients())
        cases = []
        bad = copy.deepcopy(original)
        bad["state"]["b"] = {"lo": "2", "hi": "1"}
        cases.append(bad)
        bad = copy.deepcopy(original)
        bad["state"]["beta"] = {"lo": "NaN", "hi": "1"}
        cases.append(bad)
        bad = copy.deepcopy(original)
        bad["certificate"]["elapsed_time"] = {"numerator": -1, "denominator": 400}
        cases.append(bad)
        bad = copy.deepcopy(original)
        bad["certificate"]["analytical_origin"] = "restart time"
        cases.append(bad)
        bad = copy.deepcopy(original)
        del bad["coefficients"]["n1sq"]
        cases.append(bad)
        for bad in cases:
            with self.assertRaises(ValueError):
                s.checkpoint_decode(bad)

    def test_resumed_and_direct_enclosures_with_prior_uncertainty(self):
        coeff = self.coefficients()
        half = F(1, 400)
        first_b, first_beta = s.clock_free_step(s.I(0), s.I(0), coeff["k"], s.rational(half))
        saved = s.checkpoint_decode(s.checkpoint_encode(half, first_b, first_beta, coeff))
        elapsed, resumed_b, resumed_beta, _ = s.advance_checkpoint(saved, half)
        direct_b, direct_beta = s.clock_free_step(s.I(0), s.I(0), coeff["k"], s.rational(2*half))
        self.assertEqual(elapsed, F(1, 200))
        self.assertLessEqual(resumed_b.lo, direct_b.hi)
        self.assertGreaterEqual(resumed_b.hi, direct_b.lo)
        self.assertLessEqual(resumed_beta.lo, direct_beta.hi)
        self.assertGreaterEqual(resumed_beta.hi, direct_beta.lo)
        self.assertGreater(resumed_b.hi-resumed_b.lo, D(0))
        with self.assertRaises(ValueError):
            s.advance_checkpoint(saved, F(1, 100))


if __name__ == "__main__":
    unittest.main()
