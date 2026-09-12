"""Bounded deterministic implementation checks; no population accuracy claim.

One full invocation executes exactly three solver trajectories: P=64,m=2 at
6 steps, a duplicate split 2+4 steps, and P=16,m=2 float32 at 1 step (26 calls).
Other checks use fixed small arrays. Outputs remain in the study namespace.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import sys
import time
import unittest
import uuid

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal

from directional_solver import DirectionalSolver, NumericalFailure, SolverConfig, covariance_extension


RUN = Path(__file__).resolve().parents[2] / "data/generated/population_flow_computation" / ("implementation_tests_" + uuid.uuid4().hex[:12])


def configuration(precision="float64", representatives=64):
    return SolverConfig(representatives=representatives, h=0.025, noise=0.05, seed=1701,
                        directions=[[1, 0], [0.6, 0.8]], weights=[0.4, 0.6], labels=[0.7, -0.3], precision=precision)


class SourceSolverTests(unittest.TestCase):
    def test_covariance_prefix_singular_clean_gram_and_innovation_orientation(self):
        fields = np.array([[1, 1, -1], [2, 2, -2], [-1, -1, 1], [0.5, 0.5, -0.5]])
        e = np.array([[0.2, 0.5, -1], [-0.7, 0.1, 0.4], [0.8, -0.3, 0.9], [0.6, -0.2, 1.1]])
        empty = np.empty((4, 0))
        old_factor, old_source, _ = covariance_extension(empty, fields[:, :2], np.empty((0, 0)), empty, e[:, :2], 0.2)
        factor, source, checks = covariance_extension(fields[:, :2], fields[:, 2:], old_factor, e[:, :2], e[:, 2:], 0.2)
        assert_array_equal(factor[:2, :2], old_factor)
        assert_allclose(factor @ factor.T, fields.T @ fields / 4 + 0.04 * np.eye(3), atol=3e-15)
        assert_allclose(np.hstack((old_source, source)), e @ factor.T, atol=1e-15)
        self.assertGreaterEqual(checks["minimum_schur"], 0.04 - 1e-14)
        # An impossible old covariance must fail instead of silently adding noise.
        with self.assertRaises(NumericalFailure):
            covariance_extension(fields[:, :2], fields[:, 2:], old_factor * 0.01, e[:, :2], e[:, 2:], 0.2)

    def test_weighted_directional_duality_by_complete_sign_enumeration(self):
        signs = np.array(list(itertools.product((-1.0, 1.0), repeat=4)))
        omega = np.array([0.005, 0.08, 0.2, 0.01])
        probes = signs / np.sqrt(omega)
        jacobian = np.array([[0.2, -0.5], [1.3, 0.4], [-0.1, 2.0], [0.7, -0.2]])
        tangent = probes @ jacobian
        estimate = (omega * probes).T @ tangent / len(signs)
        assert_allclose(estimate, jacobian, atol=5e-16)
        # The local current-source derivative can be removed before sketching.
        for signs_now in ((-1, 1), (1, -1)):
            direct = np.array(signs_now) / np.sqrt([0.003, 0.007])
            observed = tangent + direct
            assert_allclose((omega * probes).T @ (observed - direct) / len(signs), jacobian, atol=6e-16)

    def test_frozen_coordinate_tangents_against_central_difference(self):
        # Supplied coordinates, sources, coefficients; no solver trajectory.
        w = np.array([[0.1, -0.2], [0.3, 0.4], [-0.5, 0.2]])
        vw = np.array([[0.2, 0.1], [-0.3, 0.4], [0.1, -0.2]])
        c, vc = np.array([0.2, -0.1, 0.3]), np.array([0.4, 0.1, -0.2])
        u = np.array([[1, 0], [0.6, 0.8]])
        z = np.array([[0.1, 0.4], [-0.2, 0.5], [0.3, -0.1]])
        zdot = np.array([[0.3, -0.1], [0.2, 0.4], [-0.5, 0.1]])
        q = np.array([[0.2, -0.4], [0.1, 0.3], [-0.1, 0.4]])
        qdot = np.array([[0.1, 0.2], [-0.3, 0.2], [0.4, -0.2]])
        gamma = np.array([0.03, -0.01])
        h, v = np.tanh(w @ u.T), np.tanh(z)
        dh, dv = 1-h*h, 1-v*v
        expected_w = vw + ((-2*h*dh*(vw @ u.T)*q + dh*qdot)*gamma) @ u
        expected_c = vc + (dv*zdot) @ gamma
        def coordinate_map(epsilon):
            perturbed_w = w + epsilon*vw
            hidden = np.tanh(perturbed_w @ u.T)
            return (perturbed_w + (((1-hidden*hidden)*(q+epsilon*qdot))*gamma) @ u,
                    c+epsilon*vc+np.tanh(z+epsilon*zdot) @ gamma)
        plus, minus = coordinate_map(1e-6), coordinate_map(-1e-6)
        assert_allclose((plus[0]-minus[0])/2e-6, expected_w, rtol=1e-8, atol=4e-11)
        assert_allclose((plus[1]-minus[1])/2e-6, expected_c, rtol=1e-8, atol=4e-11)

    def test_trajectories_initial_oracle_restart_queries_and_float32(self):
        solver = DirectionalSolver(configuration())
        # Clean initial/current actions are exactly the same joint draw.
        initial_query = solver.paired_hidden_draws(solver.config.directions, draws=2, seed=18)
        assert_array_equal(initial_query["initial_preactivation"], initial_query["current_preactivation"])
        assert_array_equal(initial_query["lower_Q"], 0)
        assert_array_equal(initial_query["upper_D"], 0)
        assert_array_equal(solver.predict(solver.config.directions, 12), 0)
        solver.step()
        h = np.tanh(solver.g @ solver.u.T)
        gamma = 2 * solver.config.h * solver.weights * solver.labels
        q = solver.config.noise * solver.Eminus[:, :solver.m]
        assert_allclose(solver.w, solver.g + (((1-h*h)*q)*gamma) @ solver.u, atol=2e-16)
        assert_allclose(solver.c, np.tanh(solver.Bplus) @ gamma, atol=2e-16)
        assert_allclose(solver.v_w, (((1-h*h)*solver.Rminus)*gamma) @ solver.u, atol=2e-16)
        assert_allclose(solver.v_c, ((1-np.tanh(solver.Bplus)**2)*solver.Rplus) @ gamma, atol=2e-16)
        assert_array_equal(solver.D, 0)
        self.assertFalse(np.array_equal(solver.Eplus, solver.Eminus))
        for _ in range(5):
            prefix = {name: getattr(solver, name).copy() for name in ("Lplus", "Lminus", "Eplus", "Eminus", "Bplus", "Bminus")}
            solver.step()
            for name, previous in prefix.items():
                assert_array_equal(getattr(solver, name)[:previous.shape[0], :previous.shape[1]], previous)
        uninterrupted = {name: getattr(solver, name).copy() for name in solver.array_names}
        prediction = solver.predict(solver.config.directions, 20)
        old_rng = solver.rng_state()
        query = solver.paired_hidden_draws(solver.config.directions, draws=3, seed=991)
        assert_array_equal(solver.predict(solver.config.directions, 20), prediction)
        self.assertEqual(solver.rng_state(), old_rng)
        for name in solver.array_names:
            assert_array_equal(getattr(solver, name), uninterrupted[name])
        # Joint query marginal prediction agrees with the deterministic quadrature
        # only up to query sampling error; no narrow sampling assertion is imposed.
        self.assertEqual(query["lower_Q"].shape, (3, 64, 2))
        self.assertTrue(np.all(np.isfinite(query["lower_Q"])))
        restarted = DirectionalSolver(configuration())
        restarted.step()
        restarted.step()
        checkpoint = RUN / "checkpoint_at_step_2.npz"
        restarted.save(checkpoint)
        saved = {name: getattr(restarted, name).copy() for name in restarted.array_names}
        saved_rng = restarted.rng_state()
        restarted = DirectionalSolver.load(checkpoint)
        self.assertEqual(restarted.rng_state(), saved_rng)
        for name in restarted.array_names:
            assert_array_equal(getattr(restarted, name), saved[name])
        for _ in range(4):
            restarted.step()
        for name in solver.array_names:
            assert_array_equal(getattr(restarted, name), uninterrupted[name])
        self.assertEqual(restarted.rng_state(), solver.rng_state())
        assert_array_equal(restarted.predict(solver.config.directions, 20), prediction)
        self.assertLess(solver.diagnostics()["covariance_reconstruction_relative_frobenius"]["plus"], 3e-15)
        solver.save(RUN / "uninterrupted_final.npz")
        restarted.save(RUN / "restarted_final.npz")
        low_precision = DirectionalSolver(configuration("float32", representatives=16))
        low_precision.step()
        low_precision.save(RUN / "float32_step_1.npz")
        loaded32 = DirectionalSolver.load(RUN / "float32_step_1.npz")
        for name in low_precision.array_names:
            assert_array_equal(getattr(loaded32, name), getattr(low_precision, name))
        self.assertEqual(loaded32.w.dtype, np.float32)
        (RUN / "checked_diagnostics.json").write_text(json.dumps({"float64": solver.diagnostics(20), "float32": loaded32.diagnostics(20)}, indent=2) + "\n")

    def test_configuration_validation(self):
        config = dict(vars(configuration()))
        config.update(directions=[[1, 0], [0.6, 0.8], [-1, 0]], labels=[1, 2, 3], weights=[0.4, 0, 0.6])
        solver = DirectionalSolver(config)
        self.assertEqual(solver.m, 2)
        self.assertEqual(solver.config.labels, [1, 3])
        config["weights"] = [0.4, -0.2, 0.8]
        with self.assertRaises(ValueError):
            DirectionalSolver(config)


if __name__ == "__main__":
    RUN.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SourceSolverTests)
    with (RUN / "tests.txt").open("x") as report:
        result = unittest.TextTestRunner(stream=report, verbosity=2).run(suite)
    print((RUN / "tests.txt").read_text())
    provenance = {"argv": sys.argv, "cwd": os.getcwd(), "python": platform.python_version(), "numpy": np.__version__, "run_directory": str(RUN), "wall_seconds": time.perf_counter()-started, "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors), "trajectory_budget": {"trajectories": 3, "steps_total": 13, "training_calls_total": 26}, "source_hashes": {name: hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest() for name in ("directional_solver.py", "test_directional_solver.py")}, "threads": {name: os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}}
    (RUN / "outcome.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps(provenance))
    raise SystemExit(0 if result.wasSuccessful() else 1)
