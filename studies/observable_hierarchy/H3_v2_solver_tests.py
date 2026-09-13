"""Deterministic semantics tests; no research trajectory is run here."""
import importlib
import tempfile
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import numpy as np

if __name__ == "__main__":
    from H3_v2_candidate_loader import load_candidate
    load_candidate()

from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_fixed import Fixed
from pde.observable_solver import (State, DataLaw, ArcLaw, rhs, loss, predict,
    paired_observations, save_restart, load_restart, interpolate_state)


class ArithmeticTests(unittest.TestCase):
    def test_precision_is_used_outside_context(self):
        x = Arithmetic(80).real(Fraction(1, 3))
        self.assertEqual(len(x.as_tuple().digits), 80)
        self.assertIsInstance(Arithmetic(24, "rational").real(Fraction(1, 3)), Fixed)

    def test_rational_transcendentals_and_refinement(self):
        for digits in (24, 36):
            ar = Arithmetic(digits, "rational")
            dr = Arithmetic(digits+20)
            for text in ("0.2", "1.3", "-2.1"):
                x = ar.real(text)
                with dr.context():
                    reference = dr.real(text)
                    error = abs(Decimal(x.exp().units)/Decimal(x.scale)-reference.exp())
                    self.assertLess(error, Decimal(10)**(-digits+2))
            for text in ("0.02", "1", "2.7"):
                x = ar.real(text)
                with dr.context():
                    reference = dr.real(text)
                    for got, expected in ((x.ln(), reference.ln()), (x.sqrt(), reference.sqrt())):
                        error = abs(Decimal(got.units)/Decimal(got.scale)-expected)
                        self.assertLess(error, Decimal(10)**(-digits+2))
            x = ar.real(Fraction(1, 3))
            self.assertAlmostEqual(float(x.trig()), np.sin(1/3), places=14)
            self.assertAlmostEqual(float(x.trig(True)), np.cos(1/3), places=14)

    def test_joint_prefix_and_covariance(self):
        ar = Arithmetic()
        a = gaussian_points(64, 3, ar)
        b = gaussian_points(64, 6, ar)
        np.testing.assert_array_equal(a, b[:, :3])
        np.testing.assert_array_equal(a[:16], gaussian_points(16, 3, ar))
        positive = np.array([[1., 1.], [1., 1.]])+0.01*np.eye(2)
        for ar in (Arithmetic(), Arithmetic(40), Arithmetic(24, "rational")):
            p = ar.array(positive)
            L = ar.cholesky(p)
            T = ar.inverse_lower(L)
            np.testing.assert_allclose(np.asarray(L @ L.T, float), positive, atol=1e-14)
            np.testing.assert_allclose(np.asarray(T @ L, float), np.eye(2), atol=1e-14)


def example(ar=None):
    ar = ar or Arithmetic()
    A = ar.array
    state = State(A([[1., .2], [1., -.3], [1., .6]]), A([[.2, -.8], [.7, .5], [-.4, .3]]),
                  A([[.24, -.79], [.69, .48], [-.37, .27]]), A([.2, .3, .5]),
                  A([[1., .4], [1., -.7]]), A([.08, -.05]), A([.4, .6]),
                  A([[.4, .2], [-.1, .3]]), A([[.39, .21], [-.11, .29]]), ar)
    data = DataLaw(A([[1, 0], [Fraction(3, 5), Fraction(4, 5)]]), A([1, -1]), A([.3, .7]))
    return state.validate(), data.validate(ar)


class SolverSemantics(unittest.TestCase):
    def test_gradient_energy_and_batched_vector_field(self):
        state, data = example()
        v = rhs(state, data)
        for a, b in zip(v, rhs(state, data, block_size=1)):
            np.testing.assert_allclose(a, b, atol=1e-15)
        norm = state.p1 @ np.sum(v[0]**2, axis=1)+state.p2 @ (v[1]**2)+np.sum(v[2]**2)
        h = 1e-5
        plus = state.dynamic_copy(state.w+h*v[0], state.c+h*v[1], state.M+h*v[2])
        minus = state.dynamic_copy(state.w-h*v[0], state.c-h*v[1], state.M-h*v[2])
        derivative = (loss(plus, data)-loss(minus, data))/(2*h)
        self.assertAlmostEqual(derivative, -norm, delta=1e-10)

    def test_actual_transpose_and_joint_pairs(self):
        state, data = example()
        a = np.array([.3, -.5, .9])
        d = np.array([-.2, .7])
        forward = state.b2 @ state.M @ (state.b1.T @ (state.p1*a))
        reverse = state.b1 @ state.M.T @ (state.b2.T @ (state.p2*d))
        self.assertAlmostEqual(state.p2 @ (d*forward), state.p1 @ (a*reverse), places=15)
        obs = paired_observations(state, data, block_size=1)
        for key, rms, p in (("first_pairs", "rms1", state.p1), ("second_pairs", "rms2", state.p2)):
            pair = obs[key]
            value = p @ ((pair[:, :, 1]-pair[:, :, 0])**2) @ data.probabilities
            self.assertAlmostEqual(obs[rms]**2, value, places=15)
        initial = state.dynamic_copy(state.g.copy(), np.zeros_like(state.c), state.D.copy())
        self.assertEqual(paired_observations(initial, data)["rms1"], 0)
        self.assertEqual(paired_observations(initial, data)["rms2"], 0)

    def test_restart_exact_values_all_backends(self):
        for ar in (Arithmetic(), Arithmetic(40), Arithmetic(24, "rational")):
            state, data = example(ar)
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory)/"restart.json"
                save_restart(path, state, data)
                restored, restored_data = load_restart(path)
            for key in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"):
                np.testing.assert_array_equal(getattr(state, key), getattr(restored, key))
            np.testing.assert_array_equal(predict(state, data.inputs), predict(restored, restored_data.inputs))
            for first, second in zip(rhs(state, data), rhs(restored, restored_data)):
                np.testing.assert_array_equal(first, second)

    def test_represented_scope_and_interpolation(self):
        ar = Arithmetic()
        law = ArcLaw().quadrature(8, ar)
        self.assertEqual(len(law.inputs), 16)
        atom = ArcLaw(a=0, b=0, c=0, d=0).quadrature(8, ar)
        self.assertEqual(len(atom.inputs), 2)
        self.assertAlmostEqual(float(atom.inputs[0] @ atom.inputs[1]), .6)
        for parameters in (dict(a="-1/10"), dict(p="1/4"), dict(p=.5)):
            with self.assertRaises(ValueError):
                ArcLaw(**parameters)
        state, data = example()
        other = state.dynamic_copy(state.w+.01, state.c+.02, state.M+.03)
        midpoint = interpolate_state(state, other, Fraction(1, 2))
        np.testing.assert_allclose(midpoint.M, state.M+.015)
        bad = state.copy()
        bad.g[0, 0] += 1
        with self.assertRaises(ValueError):
            interpolate_state(state, bad, .5)


if __name__ == "__main__":
    unittest.main()
