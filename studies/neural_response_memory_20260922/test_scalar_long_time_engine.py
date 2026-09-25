"""Deterministic local checks; these are not research trajectories."""

import unittest

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

from scalar_circle_probe_engine import SignatureHierarchy
from scalar_long_time_engine import (StiffSignatureHierarchy,
                                     frozen_kernel_endpoint,
                                     recenter_coefficients)


class LongTimeEngineTests(unittest.TestCase):
    def coefficients(self, m=3, count=None, complex_values=False):
        rng = np.random.default_rng(711)
        count = m if count is None else count
        result = {name: .04 * rng.normal(size=(count,) + (m,) * degree)
                  for degree, name in enumerate(("f", "Theta", "C", "Q"))}
        if complex_values:
            result = {key: value + .03j * rng.normal(size=value.shape)
                      for key, value in result.items()}
        return result

    def test_all_jacobian_columns_with_ordered_tensors(self):
        rng = np.random.default_rng(110)
        for order in (2, 3, 4):
            model = StiffSignatureHierarchy(self.coefficients(), np.array([.4, -.3, .2]), order)
            state = model.initial_state() + .1 * rng.normal(size=model.size)
            jacobian = model.jac(0., state).toarray()
            step = 1e-6
            finite = np.empty_like(jacobian)
            for column in range(model.size):
                direction = np.zeros(model.size)
                direction[column] = step
                finite[:, column] = (model.rhs(0., state + direction)
                                     - model.rhs(0., state - direction)) / (2 * step)
            np.testing.assert_allclose(jacobian, finite, rtol=2e-7, atol=2e-10)
            original = SignatureHierarchy(self.coefficients(), model.labels, order)
            np.testing.assert_array_equal(model.rhs(0., state), original.rhs(0., state))

    def test_eight_sample_shape_and_sparsity(self):
        model = StiffSignatureHierarchy(self.coefficients(m=8), np.ones(8))
        matrix = model.jac(0., model.initial_state())
        self.assertEqual(matrix.shape, (1168, 1168))
        self.assertEqual(matrix.nnz, 6408)

    def test_recenter_matches_explicit_forced_passive_system(self):
        m, count = 3, 2
        for complex_values in (False, True):
            old = self.coefficients(m=m, count=count, complex_values=complex_values)
            originals = {key: value.copy() for key, value in old.items()}
            shapes = {key: old[key].shape for key in ("f", "Theta", "C")}
            sizes = [int(np.prod(shape)) for shape in shapes.values()]
            ends = np.cumsum([0] + sizes)
            initial = np.concatenate([old[key].reshape(-1) for key in shapes]
                                     + [np.zeros(m + m*m + m*m*m)])
            def rhs(t, state):
                velocity = np.array([.2 + .1*t, -.13 + .04*t*t, .05*np.sin(t)])
                values = {key: state[ends[j]:ends[j+1]].reshape(shape)
                          for j, (key, shape) in enumerate(shapes.items())}
                signature = state[ends[-1]:]
                z, integral = signature[:m], signature[m:m+m*m].reshape(m, m)
                return np.concatenate((
                    (values["Theta"] @ velocity).reshape(-1),
                    np.tensordot(values["C"], velocity, axes=([-1], [0])).reshape(-1),
                    np.tensordot(old["Q"], velocity, axes=([-1], [0])).reshape(-1),
                    velocity, np.outer(velocity, z).reshape(-1),
                    (velocity[:, None, None] * integral).reshape(-1)))
            final = solve_ivp(rhs, (0., 1.3), initial, method="DOP853",
                              rtol=2e-12, atol=2e-14).y[:, -1]
            tail = final[ends[-1]:].real
            sig = dict(z=tail[:m], I=tail[m:m+m*m].reshape(m, m),
                       J=tail[m+m*m:].reshape(m, m, m))
            updated = recenter_coefficients(old, sig)
            for j, (key, shape) in enumerate(shapes.items()):
                np.testing.assert_allclose(updated[key],
                                           final[ends[j]:ends[j+1]].reshape(shape),
                                           rtol=3e-11, atol=3e-13)
            self.assertIs(updated["Q"], old["Q"])
            for key in old:
                np.testing.assert_array_equal(old[key], originals[key])

    def test_stiff_methods_and_restarted_training_are_consistent(self):
        coefficients = self.coefficients()
        labels = np.array([.4, -.3, .2])
        model = StiffSignatureHierarchy(coefficients, labels)
        initial = model.initial_state()
        common = dict(rtol=2e-10, atol=2e-12, dense_output=True)
        reference = solve_ivp(model.rhs, (0., 2.), initial, method="DOP853", **common)
        for method in ("BDF", "Radau"):
            solution = solve_ivp(model.rhs, (0., 2.), initial, method=method,
                                 jac=model.jac, **common)
            self.assertTrue(solution.success)
            np.testing.assert_allclose(solution.y[:, -1], reference.y[:, -1],
                                       rtol=3e-7, atol=2e-9)
        first = solve_ivp(model.rhs, (0., .8), initial, method="BDF", jac=model.jac, **common)
        split_state = first.y[:, -1]
        split_coefficients = model.training.tensors(model.training_state(split_state))
        restart = StiffSignatureHierarchy(split_coefficients, labels)
        second = solve_ivp(restart.rhs, (.8, 2.), restart.initial_state(), method="BDF",
                           jac=restart.jac, **common)
        np.testing.assert_allclose(second.y[:restart.training_size, -1],
                                   reference.y[:model.training_size, -1], rtol=3e-7, atol=2e-9)
        probe = self.coefficients(count=2, complex_values=True)
        split_probe = recenter_coefficients(probe, model.signatures(split_state))
        twice = restart.readout(split_probe, second.y[:, -1])
        unsplit = model.readout(probe, reference.y[:, -1])
        np.testing.assert_allclose(twice, unsplit, rtol=3e-7, atol=2e-9)

    def test_spectral_endpoint_and_zero_mode_integral(self):
        theta = np.diag([.4, .03, 0.])
        coefficients = dict(f=np.array([.2, -.1, 0.]), Theta=theta)
        labels = np.array([1., -1., 0.])
        endpoint = frozen_kernel_endpoint(coefficients, labels)
        self.assertEqual(endpoint["status"], "fitted")
        self.assertAlmostEqual(endpoint["loss"], 1e-6, delta=2e-18)
        expected = labels + expm(-2/3 * theta * endpoint["time"]) @ (coefficients["f"]-labels)
        np.testing.assert_allclose(endpoint["train_f"], expected, rtol=2e-14, atol=2e-14)
        np.testing.assert_allclose(coefficients["f"] + theta @ endpoint["z"], expected,
                                   rtol=2e-14, atol=2e-14)
        labels[2] = .2
        capped = frozen_kernel_endpoint(coefficients, labels, time_cap=20.)
        self.assertEqual(capped["status"], "time_cap")
        self.assertAlmostEqual(capped["z"][2], 2/3 * .2 * 20.)

    def test_indefinite_kernel_first_crossing_without_projection(self):
        coefficients = dict(f=np.array([1., .01]), Theta=np.diag([1., -.1]))
        endpoint = frozen_kernel_endpoint(coefficients, np.zeros(2), target=.001, time_cap=100.)
        self.assertEqual(endpoint["status"], "fitted")
        self.assertLess(endpoint["time"], 10.)
        self.assertLess(endpoint["eigenvalues"][0], 0.)
        self.assertAlmostEqual(endpoint["loss"], .001, delta=2e-17)
        before = expm(-coefficients["Theta"] * (endpoint["time"]-1e-4)) @ coefficients["f"]
        self.assertGreater(np.mean(before**2), .001)


if __name__ == "__main__":
    unittest.main()
