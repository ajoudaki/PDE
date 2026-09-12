#!/usr/bin/env python3
"""Static exact-oracle tests for the circle kernel; no dynamics or fitting."""
from fractions import Fraction as F
import math
import unittest

import H3_circle_kernel as k


def normal_moment(n):
    return 0 if n % 2 else math.factorial(n)//(2**(n//2)*math.factorial(n//2))


class HermiteTests(unittest.TestCase):
    def test_exact_orthogonality_and_correlated_gaussian_identity(self):
        p = k.hermite_polynomials()
        rho, sigma = F(3,5), F(4,5)
        for m in range(8):
            for n in range(8):
                total = F(0)
                for i,a in enumerate(p[m]):
                    for j,b in enumerate(p[n]):
                        for ell in range(j+1):
                            total += (a*b*math.comb(j,ell)*rho**ell*sigma**(j-ell)
                                      *normal_moment(i+ell)*normal_moment(j-ell))
                self.assertEqual(total, math.factorial(n)*rho**n if m==n else 0)

    def test_derivative_normal_density_oracle(self):
        # rho''''=(x^4-6x^2+3)rho when the multiplier is constant.
        self.assertEqual(k.derivative_polynomial([1],0),
                         {(4,0,0):1,(2,0,0):-6,(0,0,0):3})

    def test_envelope_matches_existing_h2_bound(self):
        bounds, mono = k.derivative_bounds()
        self.assertEqual(mono[:7], [1,1,1,1,1,2,5])
        self.assertEqual(bounds[0], 1098)
        self.assertEqual(k.hermite_polynomials()[7], [0,-105,0,105,0,-21,0,1])


class EvaluationTests(unittest.TestCase):
    def fixture(self):
        # A finite odd identity example has zero omitted Hermite mass.
        alpha = {n:k.I(0) for n in (1,3,5,7)}
        beta = dict(alpha)
        alpha[1], beta[1] = k.I('.25'), k.I('.125')
        return k.CircleKernel(k.I('.25'), k.I('.125'), alpha, beta)

    def test_exact_endpoint_oddness_and_restart(self):
        obj = self.fixture()
        for rho in (F(-1),F(-3,5),F(0),F(4,5),F(1)):
            self.assertEqual(obj.midpoint_kernel(rho), rho/8)
        self.assertEqual(obj.kernel_error, 0)
        restored = k.CircleKernel.from_record(obj.record())
        self.assertEqual(restored.record(), obj.record())
        result = restored.prediction(k.I('.003'),F(3,5),F(4,5))
        exact = F(3,1000)*F(-1,5)/8
        self.assertLessEqual(F(result.lo),exact)
        self.assertGreaterEqual(F(result.hi),exact)

    def test_domain_rejection(self):
        obj=self.fixture()
        with self.assertRaises(ValueError):
            obj.prediction(k.I('.003'),F(1),F(1))
        with self.assertRaises(TypeError):
            obj.midpoint_kernel(.5)
        with self.assertRaises(ValueError):
            obj.prediction(k.I('0','.001'),1,0)

    def test_parameter_error_against_exact_rational_perturbations(self):
        alpha={n:k.I(0) for n in (1,3,5,7)}
        beta=dict(alpha)
        alpha[1]=k.I('.249','.251')
        beta[1]=k.I('.124','.126')
        obj=k.CircleKernel(k.I('.249','.251'),k.I('.124','.126'),alpha,beta)
        # Actual alpha=q and beta=v is a normalized linear feature model;
        # q>=v is precisely its Bessel slope constraint.
        for q in (F(249,1000),F(251,1000)):
            for v in (F(124,1000),F(126,1000)):
                for rho in (F(-1),F(-3,5),F(0),F(4,5),F(1)):
                    self.assertLessEqual(abs(v*rho-obj.midpoint_kernel(rho)),obj.parameter_error)

    def test_input_box_for_irrational_unit_direction(self):
        obj = self.fixture()
        u = 1/k.I(2).sqrt()
        result = obj.prediction_box(k.I('.003'),u,u)
        self.assertLessEqual(result.lo,0)
        self.assertGreaterEqual(result.hi,0)
        result = obj.prediction_box(k.I('.003'),k.I('.59999999','.60000001'),
                                    k.I('.79999999','.80000001'))
        exact = F(3,1000)*F(-1,5)/8
        self.assertLessEqual(F(result.lo),exact)
        self.assertGreaterEqual(F(result.hi),exact)
        with self.assertRaises(ValueError):
            obj.prediction_box(k.I('.003'),k.I('.6'),k.I('.6'))


if __name__ == '__main__':
    unittest.main()
