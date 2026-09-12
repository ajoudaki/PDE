"""Deterministic static checks; no trajectory or Monte Carlo is run.

The default imports pde.observable_closure from the installed package.
H2_PROTOTYPE_MODULE may override that import for isolated checks.
"""
import importlib
import math
import os
from pathlib import Path
import tempfile
import unittest

import numpy as np

core = importlib.import_module(os.environ.get("H2_PROTOTYPE_MODULE", "pde.observable_closure"))


class WordAndSourceTests(unittest.TestCase):
    def test_natural_number_decoder_and_types(self):
        for a in range(10):
            for b in range(10):
                self.assertEqual(core.unpair(core.pair(a, b)), (a, b))
        self.assertEqual(core.decode_word(4 + 8 * 2), core.unary("sin", core.seed("g1")))
        self.assertIsNone(core.decode_word(4 + 8 * 2 + 3))  # A g1 is invalid.
        self.assertIsNone(core.decode_word(4 + 8 * core.pair(0, 1) + 4))
        self.assertEqual(core.decode_word(4 + 8 * core.pair(0, 0) + 5),
                         core.multiply(core.constant(1), core.constant(1)))
        first, second, _ = core.initial_dictionary(1)
        self.assertEqual((len(first), len(second)), (6, 4))
        self.assertEqual(first[0], first[-1])  # Candidate keeps duplicates.
        self.assertEqual(second[-2], second[-1])
        with self.assertRaises(ValueError):
            core.decode_word(True)
        with self.assertRaises(ValueError):
            core.multiply(core.seed("g1"), core.seed("g2"))
        with self.assertRaises(core.ResourceLimit):
            core.initial_dictionary(6, max_codes=5)

    def test_pilot_covariances_response_and_stein_pairing(self):
        pilot = core.pilot_words()
        program = core.GaussianProgram(core.QuadratureLimits(order=15, max_innovation_dimension=4)).compile(pilot.values())
        variance_h = (1 - math.exp(-2)) / 2
        variance_s = (1 - math.exp(-2 * variance_h)) / 2
        response = math.exp(-variance_h / 2)
        self.assertEqual(len(program.sources), 4)
        self.assertAlmostEqual(program.diagnostics[0]["variance"], variance_h, delta=3e-12)
        self.assertAlmostEqual(program.diagnostics[2]["variance"], variance_s, delta=3e-12)
        self.assertAlmostEqual(program.diagnostics[2]["response"][0], response, delta=3e-12)
        self.assertAlmostEqual(program.diagnostics[2]["response"][1], 0, delta=3e-14)
        first, second = program.carriers[1], program.carriers[2]
        p1, h1 = program.evaluate(pilot["p1"]), program.evaluate(pilot["h1"])
        z1, s1 = program.evaluate(pilot["z1"]), program.evaluate(pilot["s1"])
        lhs = first.weights @ (h1 * p1)
        rhs = second.weights @ (z1 * s1)
        self.assertAlmostEqual(lhs, response * variance_h, delta=3e-12)
        self.assertAlmostEqual(lhs, rhs, delta=3e-12)
        # Removing response gives zero here and fails this nonzero identity.
        self.assertGreater(abs(lhs), 0.3)
        centered = first.gaussian[:, program.sources[pilot["p1"]].gaussian_index]
        np.testing.assert_allclose(p1, centered + response * h1, atol=3e-12, rtol=0)

    def test_named_derivatives_and_forward_reuse_after_reverse(self):
        pilot = core.pilot_words()
        limits = core.QuadratureLimits(order=15, max_innovation_dimension=4)
        program = core.GaussianProgram(limits).compile(pilot.values())
        p1 = program.evaluate(pilot["p1"])
        value, gradient = program.evaluate(pilot["t1"], derivative=True)
        np.testing.assert_allclose(value, np.tanh(p1), rtol=0, atol=0)
        np.testing.assert_allclose(gradient[:, 0], 1 - np.tanh(p1) ** 2, rtol=0, atol=0)
        np.testing.assert_allclose(gradient[:, 1], 0, rtol=0, atol=0)
        new_forward = core.action(pilot["t1"])
        expected_response = program.carriers[1].weights @ gradient[:, 0]
        program.compile([new_forward])
        descriptor = program.sources[new_forward]
        self.assertAlmostEqual(descriptor.response[0][1], expected_response, delta=2e-15)
        second = program.carriers[2]
        gaussian = second.gaussian[:, descriptor.gaussian_index]
        np.testing.assert_allclose(program.evaluate(new_forward) - gaussian,
                                   expected_response * program.evaluate(pilot["s1"]), atol=5e-15, rtol=0)
        source_count = len(program.sources)
        program.compile([new_forward, pilot["z1"], new_forward])
        self.assertEqual(len(program.sources), source_count)

    def test_zero_and_singular_gaussian_sources_keep_named_coordinates(self):
        one = core.constant(1)
        zero_source = core.action(core.scale(0, one))
        first_source = core.action(one)
        scaled_source = core.action(core.scale(2, one))
        program = core.GaussianProgram().compile([zero_source, first_source, scaled_source])
        self.assertEqual(len(program.carriers[2].sources), 3)
        self.assertEqual(program.carriers[2].factor.shape[1], 1)
        np.testing.assert_allclose(program.evaluate(zero_source), 0, atol=0, rtol=0)
        np.testing.assert_allclose(program.evaluate(scaled_source), 2 * program.evaluate(first_source), atol=1e-14, rtol=0)
        _, derivatives = program.evaluate(scaled_source, derivative=True)
        np.testing.assert_allclose(derivatives[:, :2], 0, atol=0, rtol=0)
        np.testing.assert_allclose(derivatives[:, 2], 1, atol=0, rtol=0)
        # The coefficient covariance is uncentered: E[1*1]=1, not zero.
        self.assertAlmostEqual(program.diagnostics[1]["variance"], 1, delta=1e-15)
        self.assertEqual(program.diagnostics[2]["independent_source_dimensions"], 1)

    def test_quadrature_and_source_resource_limits(self):
        with self.assertRaises(core.ResourceLimit):
            core.gaussian_rule(4, core.QuadratureLimits(order=5, max_nodes=100))
        with self.assertRaises(core.ResourceLimit):
            core.GaussianProgram(core.QuadratureLimits(max_named_sources=1)).compile(core.pilot_words().values())
        with self.assertRaises(ValueError):
            core.GaussianProgram().compile([])
        with self.assertRaises(ValueError):
            core.QuadratureLimits(order=1)


class RidgeTests(unittest.TestCase):
    def test_singular_repeated_and_zero_dictionary_columns(self):
        raw = np.array([[1., 1., 0., -1.], [1., 1., 0., 0.], [1., 1., 0., 1.]])
        probabilities = np.array([0.25, 0.5, 0.25])
        b, transform, gram = core.ridge_features(raw, probabilities, order=4)
        self.assertEqual(b.shape, raw.shape)
        self.assertEqual(transform.shape, (4, 4))
        self.assertLessEqual(np.linalg.eigvalsh(b.T @ (probabilities[:, None] * b)).max(), 1 + 1e-13)
        np.testing.assert_allclose(transform @ (gram + np.eye(4) / 16) @ transform, np.eye(4), atol=2e-14, rtol=0)
        np.testing.assert_allclose(b[:, 0], b[:, 1], atol=2e-14, rtol=0)
        np.testing.assert_allclose(b[:, 2], 0, atol=0, rtol=0)
        with self.assertRaises(core.NumericalInitializationError):
            core.ridge_features(raw, probabilities, order=1100)
        with self.assertRaises(ValueError):
            core.ridge_features(np.empty((3, 0)), probabilities, 1)


class PopulationStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.initial, cls.program = core.initialize(1)
        cls.data = core.DataLaw([[1., 0.], [0., 1.], [0.6, 0.8]], [1., -1., 0.2], [0.4, 0.4, 0.2])

    def supplied_state(self):
        state = self.initial.copy()
        g = state.first.g
        state.first.w += 0.07 * np.column_stack([np.sin(g[:, 1]) + 0.2, np.cos(g[:, 0]) - 0.4])
        state.second.c = 0.12 * np.sin(state.second.b[:, 0]) + 0.04 * np.cos(state.second.b[:, 1])
        i, j = np.indices(state.M.shape)
        state.M += 0.025 * np.sin(1 + i + 2 * j)
        return state

    def test_initialization_and_actual_retained_populations(self):
        state = self.initial
        self.assertEqual(state.first.b.shape, (625, 6))
        self.assertEqual(state.second.b.shape, (3125, 4))
        self.assertEqual(state.M.shape, (4, 6))
        np.testing.assert_array_equal(state.first.w, state.first.g)
        np.testing.assert_array_equal(state.second.c, 0)
        np.testing.assert_array_equal(state.M, state.D)
        self.assertFalse(state.metadata["exact_initial_law"])
        self.assertEqual(state.metadata["ridge"], 0.5)
        self.assertTrue(all("negative_schur_roundoff_correction" in item
                            for item in state.metadata["source_diagnostics"]))
        np.testing.assert_array_equal(core.fields(state, self.data.inputs)["f"], 0)
        velocity = core.rhs(state, self.data)
        np.testing.assert_array_equal(velocity.w, 0)
        np.testing.assert_array_equal(velocity.M, 0)
        self.assertGreater(np.linalg.norm(velocity.c), 0)

    def test_actual_transpose_contraction(self):
        state = self.supplied_state()
        v = np.sin(state.first.g[:, 0]) + 0.3 * np.cos(state.first.g[:, 1])
        u = np.tanh(state.second.b[:, 0] - 0.4 * state.second.b[:, 1])
        forward = core.apply_action(state, 1, v)
        reverse = core.apply_action(state, 2, u)
        lhs = state.second.probabilities @ (u * forward)
        rhs = state.first.probabilities @ (v * reverse)
        self.assertAlmostEqual(lhs, rhs, delta=3e-15)
        # Unequal feature and quadrature dimensions prohibit a hidden plain
        # transposition of population arrays or identification of carriers.
        self.assertNotEqual(len(state.first.b), len(state.second.b))
        self.assertNotEqual(state.M.shape[0], state.M.shape[1])

    def test_all_matrix_and_selected_population_coordinate_gradients(self):
        state = self.supplied_state()
        velocity = core.rhs(state, self.data)
        epsilon = 2e-6
        for index in np.ndindex(state.M.shape):
            plus, minus = state.copy(), state.copy()
            plus.M[index] += epsilon
            minus.M[index] -= epsilon
            finite_difference = (core.loss(plus, self.data) - core.loss(minus, self.data)) / (2 * epsilon)
            self.assertAlmostEqual(finite_difference, -velocity.M[index], delta=7e-11)
        for row in np.argsort(state.first.probabilities)[-3:]:
            for coordinate in (0, 1):
                plus, minus = state.copy(), state.copy()
                plus.first.w[row, coordinate] += epsilon
                minus.first.w[row, coordinate] -= epsilon
                finite_difference = (core.loss(plus, self.data) - core.loss(minus, self.data)) / (2 * epsilon)
                expected = -state.first.probabilities[row] * velocity.w[row, coordinate]
                self.assertAlmostEqual(finite_difference, expected, delta=7e-11)
        for row in np.argsort(state.second.probabilities)[-3:]:
            plus, minus = state.copy(), state.copy()
            plus.second.c[row] += epsilon
            minus.second.c[row] -= epsilon
            finite_difference = (core.loss(plus, self.data) - core.loss(minus, self.data)) / (2 * epsilon)
            self.assertAlmostEqual(finite_difference, -state.second.probabilities[row] * velocity.c[row], delta=7e-11)

    def test_energy_directional_identity_all_blocks_move(self):
        state = self.supplied_state()
        velocity = core.rhs(state, self.data)
        self.assertGreater(np.linalg.norm(velocity.w), 1e-6)
        self.assertGreater(np.linalg.norm(velocity.c), 1e-6)
        self.assertGreater(np.linalg.norm(velocity.M), 1e-6)
        epsilon = 2e-6
        plus, minus = state.copy(), state.copy()
        for sign, copy in ((1, plus), (-1, minus)):
            copy.first.w += sign * epsilon * velocity.w
            copy.second.c += sign * epsilon * velocity.c
            copy.M += sign * epsilon * velocity.M
        derivative = (core.loss(plus, self.data) - core.loss(minus, self.data)) / (2 * epsilon)
        self.assertAlmostEqual(derivative, -core.velocity_squared_norm(state, velocity), delta=1e-10)

    def test_joint_frozen_current_observations_and_nested_actions(self):
        state = self.supplied_state()
        frozen = core.frozen_z20((1., 0.))
        current = core.action(core.unary("tanh", core.seed("w1")))
        values, probabilities = core.joint_observe(state, [frozen, current, core.seed("c")])
        np.testing.assert_array_equal(probabilities, state.second.probabilities)
        np.testing.assert_array_equal(values[:, 2], state.second.c)
        np.testing.assert_allclose(values[:, 0], core.observe(self.initial, frozen), atol=0, rtol=0)
        self.assertGreater(np.linalg.norm(values[:, 1] - values[:, 0]), 1e-5)
        nested = core.action(core.unary("sin", current))
        direct = core.apply_action(state, 2, np.sin(values[:, 1]))
        np.testing.assert_allclose(core.observe(state, nested), direct, atol=0, rtol=0)
        squared_c = core.multiply(core.seed("c"), core.seed("c"))
        np.testing.assert_allclose(core.observe(state, squared_c), state.second.c ** 2, atol=0, rtol=0)
        with self.assertRaises(ValueError):
            core.joint_observe(state, [])
        with self.assertRaises(ValueError):
            core.joint_observe(state, [core.seed("g1"), core.seed("c")])

    def test_one_algebraic_update_and_restart_without_history(self):
        state = self.supplied_state()
        velocity = core.rhs(state, self.data)
        updated = core.algebraic_update(state, velocity, 0.001)
        np.testing.assert_allclose(updated.first.w, state.first.w + 0.001 * velocity.w, atol=0, rtol=0)
        np.testing.assert_allclose(updated.second.c, state.second.c + 0.001 * velocity.c, atol=0, rtol=0)
        np.testing.assert_allclose(updated.M, state.M + 0.001 * velocity.M, atol=0, rtol=0)
        np.testing.assert_array_equal(updated.first.g, state.first.g)
        np.testing.assert_array_equal(updated.first.b, state.first.b)
        np.testing.assert_array_equal(updated.D, state.D)
        default_scratch = Path(__file__).resolve().parents[2] / "data/generated/observable_hierarchy/H2_prototype"
        scratch = Path(os.environ.get("H2_TEST_SCRATCH", str(default_scratch)))
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as temporary:
            path = Path(temporary) / "restart.npz"
            core.save_restart(path, updated, self.data)
            restored, data = core.load_restart(path)
            actual = core.rhs(updated, self.data)
            restarted = core.rhs(restored, data)
            for name in ("w", "c", "M"):
                np.testing.assert_array_equal(getattr(actual, name), getattr(restarted, name))
            np.testing.assert_array_equal(core.fields(restored, data.inputs)["f"], core.fields(updated, self.data.inputs)["f"])
            with np.load(path, allow_pickle=False) as raw:
                self.assertNotIn("time", raw.files)
                self.assertNotIn("history", raw.files)

    def test_supplied_state_restart_without_initialization_metadata(self):
        # A valid public State needs no GaussianProgram or private metadata tag.
        state = core.State(
            core.Population1([[1.]], [[0., 0.]], [[1., 0.]], [1.]),
            core.Population2([[1.]], [0.2], [1.]), [[0.3]], [[0.3]],
        )
        data = core.DataLaw([[1., 0.]], [1.], [1.])
        self.assertEqual(state.metadata, {})
        before = core.rhs(state, data)
        default_scratch = Path(__file__).resolve().parents[2] / "data/generated/observable_hierarchy/H2_prototype"
        scratch = Path(os.environ.get("H2_TEST_SCRATCH", str(default_scratch)))
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as temporary:
            for metadata in ({}, {"note": "supplied without initializer"}):
                state.metadata = metadata.copy()
                path = Path(temporary) / "supplied.npz"
                core.save_restart(path, state, data)
                self.assertEqual(state.metadata, metadata)
                restored, restored_data = core.load_restart(path)
                self.assertEqual(restored.metadata["format"], "C-H2-quadrature-v1")
                for key, value in metadata.items():
                    self.assertEqual(restored.metadata[key], value)
                after = core.rhs(restored, restored_data)
                for name in ("w", "c", "M"):
                    np.testing.assert_array_equal(getattr(before, name), getattr(after, name))
                self.assertEqual(core.loss(restored, restored_data), core.loss(state, data))
                np.testing.assert_array_equal(core.fields(restored, data.inputs)["f"],
                                              core.fields(state, data.inputs)["f"])

    def test_validation_ownership_and_empty_inputs(self):
        state = self.initial.copy()
        state.first.w[0, 0] += 1
        self.assertNotEqual(state.first.w[0, 0], self.initial.first.w[0, 0])
        with self.assertRaises(ValueError):
            core.DataLaw(np.empty((0, 2)), [], [])
        with self.assertRaises(ValueError):
            core.DataLaw([[2, 0]], [1], [1])
        with self.assertRaises(ValueError):
            core.DataLaw([[1, 0]], [1], [-1])
        with self.assertRaises(ValueError):
            core.Population1(np.empty((0, 2)), np.empty((0, 2)), np.empty((0, 2)), [])
        with self.assertRaises(ValueError):
            core.fields(state, np.empty((0, 2)))
        with self.assertRaises(ValueError):
            core.apply_action(state, 1, np.zeros(2))
        state.M[0, 0] = np.nan
        with self.assertRaises(ValueError):
            core.rhs(state, self.data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
