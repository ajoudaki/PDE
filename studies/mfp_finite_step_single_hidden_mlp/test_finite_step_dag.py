"""Regression checks for the finite-step Gaussian DAG."""

from __future__ import annotations

import unittest

import numpy as np

from finite_step_dag import (
    expected_output_raw,
    expected_output_stein,
    expected_output_steps,
    expected_output_steps_stein,
)


class FiniteStepDagTests(unittest.TestCase):
    def test_constant_control(self) -> None:
        c = 1.7
        eta = 0.31
        phi = lambda z: np.zeros_like(z) + c
        dphi = lambda z: np.zeros_like(z)
        got = expected_output_raw(phi, dphi, eta, q=0.8, order=24)
        self.assertAlmostEqual(got, eta * c * c, places=13)

    def test_identity_control(self) -> None:
        eta = -0.27
        q = 0.65
        phi = lambda z: z
        dphi = lambda z: np.ones_like(z)
        got = expected_output_raw(phi, dphi, eta, q=q, order=24)
        self.assertAlmostEqual(got, 2.0 * eta * q, places=13)

    def test_quadratic_control(self) -> None:
        eta = 0.19
        q = 0.73
        phi = lambda z: z * z
        dphi = lambda z: 2.0 * z
        expected = 7.0 * eta * q**2 + 12.0 * eta**3 * q**4
        got = expected_output_raw(phi, dphi, eta, q=q, order=32)
        self.assertAlmostEqual(got, expected, places=12)

    def test_raw_and_stein_dags_agree_for_tanh(self) -> None:
        phi = np.tanh
        dphi = lambda z: 1.0 - np.tanh(z) ** 2
        raw = expected_output_raw(phi, dphi, 0.8, q=1.2, order=100)
        stein = expected_output_stein(phi, dphi, 0.8, q=1.2, order=100)
        self.assertAlmostEqual(raw, stein, places=12)

    def test_separate_block_rates(self) -> None:
        phi = np.tanh
        dphi = lambda z: 1.0 - np.tanh(z) ** 2
        kwargs = {
            "q": 0.9,
            "order": 100,
            "eta_readout": 0.4,
            "eta_feature": -0.2,
        }
        raw = expected_output_raw(phi, dphi, 0.0, **kwargs)
        stein = expected_output_stein(phi, dphi, 0.0, **kwargs)
        self.assertAlmostEqual(raw, stein, places=12)

    def test_one_step_iterator_matches_direct_formula(self) -> None:
        phi = np.tanh
        dphi = lambda z: 1.0 - np.tanh(z) ** 2
        direct = expected_output_raw(phi, dphi, 0.4, q=1.1, order=80)
        iterated = expected_output_steps(
            phi, dphi, 0.4, 1, q=1.1, order=80
        )
        self.assertAlmostEqual(direct, iterated, places=13)

    def test_two_step_identity_control(self) -> None:
        eta = 0.23
        q = 0.7
        phi = lambda z: z
        dphi = lambda z: np.ones_like(z)
        expected = 4.0 * eta * q * (1.0 + eta**2 * q)
        got = expected_output_steps(phi, dphi, eta, 2, q=q, order=24)
        self.assertAlmostEqual(got, expected, places=13)

    def test_two_step_quadratic_control(self) -> None:
        eta = 0.11
        q = 0.6
        phi = lambda z: z * z
        dphi = lambda z: 2.0 * z
        expected = (
            14.0 * eta * q**2
            + 540.0 * eta**3 * q**4
            + 6792.0 * eta**5 * q**6
            + 29040.0 * eta**7 * q**8
            + 20160.0 * eta**9 * q**10
        )
        got = expected_output_steps(phi, dphi, eta, 2, q=q, order=32)
        self.assertAlmostEqual(got, expected, places=11)

    def test_k_step_raw_and_stein_dags_agree(self) -> None:
        phi = np.tanh
        dphi = lambda z: 1.0 - np.tanh(z) ** 2
        ddphi = lambda z: -2.0 * np.tanh(z) * (1.0 - np.tanh(z) ** 2)
        kwargs = {"q": 0.85, "order": 100}
        raw = expected_output_steps(phi, dphi, 0.13, 5, **kwargs)
        stein = expected_output_steps_stein(
            phi, dphi, ddphi, 0.13, 5, **kwargs
        )
        self.assertAlmostEqual(raw, stein, places=12)

    def test_k_step_identity_closed_form(self) -> None:
        eta = 0.17
        steps = 7
        phi = lambda z: z
        dphi = lambda z: np.ones_like(z)
        expected = 0.5 * (
            (1.0 + eta) ** (2 * steps)
            - (1.0 - eta) ** (2 * steps)
        )
        got = expected_output_steps(
            phi, dphi, eta, steps, q=1.0, order=24
        )
        self.assertAlmostEqual(got, expected, places=12)


if __name__ == "__main__":
    unittest.main()
