"""Deterministic algebraic checks, not training or hierarchy accuracy evidence."""
from fractions import Fraction
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(HERE))

from pde.observable_arithmetic import Arithmetic
from pde import observable_solver as maintained
import depth_closure as closure


def fixture(depth=3, dimension=3, arithmetic=None):
    ar = arithmetic or Arithmetic()
    populations = [3, 4, 2, 5, 3][:depth]
    features = [2, 3, 2, 2, 3][:depth]
    b, pi = [], []
    for l, (n, k) in enumerate(zip(populations, features)):
        b.append(ar.array([[1 if j == 0 else Fraction(((i+2)*(j+1)+l)%7-3, 5)
                            for j in range(k)] for i in range(n)]))
        pi.append(ar.array([Fraction(2*(i+1), n*(n+1)) for i in range(n)]))
    g = ar.array([[Fraction((i+2)*(j+1)%7-3, 7) for j in range(dimension)]
                  for i in range(populations[0])])
    D = [ar.array([[Fraction((i+1)*(j+2)+l, 11)
                    for j in range(features[l])] for i in range(features[l+1])])
         for l in range(depth-1)]
    initial = dict(b=b, pi=pi, g=g, D=D, arithmetic=ar,
                   metadata={"fixture": "independent deterministic algebra", "depth": depth})
    state = closure.from_initialization(initial)
    with ar.context():
        state.w += ar.real("0.13")
        state.c = ar.array([Fraction(i+1, 9) for i in range(populations[-1])])
        state.M = [v+ar.real("0.07") for v in state.M]
    inputs = [[1]+[0]*(dimension-1), [0, 1]+[0]*(dimension-2)]
    third = [Fraction(3, 5)]+[0]*(dimension-1)
    third[-1] = Fraction(4, 5)
    inputs.append(third)
    data = closure.DataLaw(ar.array(inputs), ar.array([1, Fraction(-1, 2), Fraction(1, 4)]),
                           ar.array([Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)]),
                           {"law": "three fixed directions"}).validate(ar, dimension)
    return state.validate(), data


def dense_fields(state, inputs):
    """Independent neuron-space matrices with explicit weighted adjoints."""
    matrices = [(state.b[l+1] @ state.M[l] @ state.b[l].T)*state.pi[l][None, :]
                for l in range(state.depth-1)]
    z, h = [], []
    z.append(state.w @ inputs.T)
    h.append(np.tanh(z[-1]))
    for matrix in matrices:
        z.append(matrix @ h[-1])
        h.append(np.tanh(z[-1]))
    prediction = (state.pi[-1]*state.c) @ h[-1]
    delta = [None]*state.depth
    delta[-1] = state.c[:, None]*(1-h[-1]**2)
    for l in range(state.depth-2, -1, -1):
        adjoint = matrices[l].T*state.pi[l+1][None, :]/state.pi[l][:, None]
        delta[l] = (1-h[l]**2)*(adjoint @ delta[l+1])
    return z, h, prediction, delta, matrices


def dense_loss(state, data):
    residual = dense_fields(state, data.inputs)[2]-data.labels
    return float(data.probabilities @ (residual**2))


class DepthClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = Path(os.environ.get("DEPTH_CLOSURE_TEST_SCRATCH",
                                   ROOT / "data/generated/cx3_depth_extension_20260920/code_checks_closure_local"))
        base.mkdir(parents=True, exist_ok=True)
        cls.temp = tempfile.TemporaryDirectory(prefix="restart_", dir=base)
        cls.scratch = Path(cls.temp.name)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def assert_state_equal(self, left, right):
        self.assertEqual((left.arithmetic.digits, left.arithmetic.backend),
                         (right.arithmetic.digits, right.arithmetic.backend))
        for name in ("g", "w", "c"):
            np.testing.assert_array_equal(getattr(left, name), getattr(right, name))
        for name in ("b", "pi", "M", "D"):
            self.assertEqual(len(getattr(left, name)), len(getattr(right, name)))
            for a, b in zip(getattr(left, name), getattr(right, name)):
                np.testing.assert_array_equal(a, b)
        self.assertEqual(left.metadata, right.metadata)

    def test_depth_three_dense_actions_and_all_block_gradient(self):
        state, data = fixture()
        z, h, f, delta, _ = dense_fields(state, data.inputs)
        actual = closure.fields(state, data.inputs)
        for l in range(3):
            np.testing.assert_allclose(actual["z"][l], z[l], atol=1e-15, rtol=1e-13)
            np.testing.assert_allclose(actual["h"][l], h[l], atol=1e-15, rtol=1e-13)
            np.testing.assert_allclose(actual["delta"][l], delta[l], atol=1e-15, rtol=1e-13)
        np.testing.assert_allclose(actual["f"], f, atol=1e-15)
        velocity = closure.rhs(state, data, block_size=1)
        blocks = [(state.w, velocity[0], state.pi[0][:, None]),
                  (state.c, velocity[1], state.pi[-1])]
        blocks += [(matrix, v, np.ones_like(matrix)) for matrix, v in zip(state.M, velocity[2])]
        epsilon = 2e-6
        for block, v, weights in blocks:
            numeric = np.zeros_like(block)
            for index in np.ndindex(block.shape):
                before = block[index]
                block[index] = before+epsilon
                plus = dense_loss(state, data)
                block[index] = before-epsilon
                minus = dense_loss(state, data)
                block[index] = before
                numeric[index] = -(plus-minus)/(2*epsilon)
            np.testing.assert_allclose(v*weights, numeric, atol=3e-11, rtol=3e-6)
            self.assertGreater(np.linalg.norm(v), 0)
        all_at_once = closure.rhs(state, data, block_size=99)
        for a, b in zip([velocity[0], velocity[1]]+velocity[2], [all_at_once[0], all_at_once[1]]+all_at_once[2]):
            np.testing.assert_allclose(a, b, atol=1e-15, rtol=1e-13)

    def test_two_layer_parity_with_maintained_solver(self):
        state, data = fixture(depth=2, dimension=2)
        old = maintained.State(state.b[0], state.g, state.w, state.pi[0], state.b[1], state.c,
                               state.pi[1], state.M[0], state.D[0], state.arithmetic, state.metadata)
        expected, actual = maintained.rhs(old, data), closure.rhs(state, data)
        for a, b in zip(expected, (actual[0], actual[1], actual[2][0])):
            np.testing.assert_allclose(a, b, atol=1e-15, rtol=1e-13)
        a = maintained.evolve(old, data, steps=3, step_size="0.001")
        b = closure.evolve(state, data, steps=3, step_size="0.001")
        for x, y in ((a.w, b.w), (a.c, b.c), (a.M, b.M[0])):
            np.testing.assert_allclose(x, y, atol=1e-15, rtol=1e-13)
        np.testing.assert_allclose(maintained.predict(a, data.inputs), closure.predict(b, data.inputs), atol=1e-15)
        obs = maintained.paired_observations(a, data)
        depth_obs = closure.paired_observations(b, data)
        np.testing.assert_allclose([obs["rms1"], obs["rms2"]], depth_obs["rms"], atol=1e-15)

    def test_weighted_adjunction_and_population_feature_permutations(self):
        state, data = fixture()
        _, _, _, _, matrices = dense_fields(state, data.inputs)
        for l, matrix in enumerate(matrices):
            v = np.arange(len(state.b[l]), dtype=float)+1
            u = np.arange(len(state.b[l+1]), dtype=float)/3-1
            forward = matrix @ v
            backward = state.b[l] @ state.M[l].T @ state.b[l+1].T @ (state.pi[l+1]*u)
            np.testing.assert_allclose(closure.apply_action(state, l+2, v), forward, atol=1e-15)
            np.testing.assert_allclose(closure.apply_action(state, l+2, u, transpose=True), backward, atol=1e-15)
            np.testing.assert_allclose(closure.apply_action(state, l+2, np.column_stack((v, 2*v))),
                                       matrix @ np.column_stack((v, 2*v)), atol=1e-15)
            initial_matrix = (state.b[l+1] @ state.D[l] @ state.b[l].T)*state.pi[l][None, :]
            np.testing.assert_allclose(closure.apply_action(state, l+2, v, initial=True),
                                       initial_matrix @ v, atol=1e-15)
            self.assertAlmostEqual(float(state.pi[l+1] @ (u*forward)),
                                   float(state.pi[l] @ (v*backward)), places=13)
        changed = state.copy()
        row_perms = [np.arange(len(b))[::-1] for b in state.b]
        column_perms = [np.arange(b.shape[1])[::-1] for b in state.b]
        for l in range(state.depth):
            changed.b[l] = state.b[l][row_perms[l]][:, column_perms[l]]
            changed.pi[l] = state.pi[l][row_perms[l]]
        changed.g, changed.w = state.g[row_perms[0]], state.w[row_perms[0]]
        changed.c = state.c[row_perms[-1]]
        for l in range(state.depth-1):
            changed.M[l] = state.M[l][np.ix_(column_perms[l+1], column_perms[l])]
            changed.D[l] = state.D[l][np.ix_(column_perms[l+1], column_perms[l])]
        np.testing.assert_allclose(closure.predict(state, data.inputs), closure.predict(changed, data.inputs), atol=1e-15)
        original, permuted = closure.rhs(state, data), closure.rhs(changed, data)
        np.testing.assert_allclose(permuted[0], original[0][row_perms[0]], atol=1e-15)
        np.testing.assert_allclose(permuted[1], original[1][row_perms[-1]], atol=1e-15)
        for l in range(state.depth-1):
            np.testing.assert_allclose(permuted[2][l], original[2][l][np.ix_(column_perms[l+1], column_perms[l])], atol=1e-15)

    def test_simultaneous_heun_and_no_input_state_mutation(self):
        state, data = fixture()
        before = state.copy()
        h = 0.007
        k = closure.rhs(state, data)
        stage = state.copy()
        stage.w = state.w+h*k[0]
        stage.c = state.c+h*k[1]
        stage.M = [a+h*v for a, v in zip(state.M, k[2])]
        q = closure.rhs(stage, data)
        result = closure.evolve(state, data, steps=1, step_size=h)
        for x, base, v, u in zip([result.w, result.c]+result.M,
                                 [state.w, state.c]+state.M, [k[0], k[1]]+k[2], [q[0], q[1]]+q[2]):
            np.testing.assert_array_equal(x, base+(h/2)*(v+u))
        self.assert_state_equal(state, before)
        middle = closure.interpolate_state(state, result, 0.5)
        np.testing.assert_array_equal(middle.w, (state.w+result.w)/2)
        altered = result.copy()
        altered.D[0][0, 0] += 1
        with self.assertRaises(ValueError):
            closure.interpolate_state(state, altered, 0.5)

    def test_exact_own_state_restart_all_backends(self):
        for ar in (Arithmetic(), Arithmetic(24), Arithmetic(20, "rational")):
            with self.subTest(digits=ar.digits, backend=ar.backend):
                state, data = fixture(arithmetic=ar)
                whole = closure.evolve(state, data, steps=2, step_size="0.001")
                first = closure.evolve(state, data, steps=1, step_size="0.001")
                path = self.scratch / (str(ar.digits)+ar.backend+".json")
                closure.save_restart(path, first, data)
                loaded, restored_data = closure.load_restart(path)
                self.assert_state_equal(first, loaded)
                for key in ("inputs", "labels", "probabilities"):
                    np.testing.assert_array_equal(getattr(data, key), getattr(restored_data, key))
                self.assertEqual(data.metadata, restored_data.metadata)
                resumed = closure.evolve(loaded, restored_data, steps=1, step_size="0.001")
                self.assert_state_equal(whole, resumed)
                storage = closure.state_bytes(resumed, restored_data)
                self.assertGreater(storage["arrays"], 0)
                self.assertGreater(storage["data_arrays"], 0)

    def test_paired_observations_every_layer_and_depth_four(self):
        state, data = fixture(depth=4)
        current = dense_fields(state, data.inputs)[1]
        initial = state.dynamic_copy(state.g, np.zeros_like(state.c), state.D)
        before = dense_fields(initial, data.inputs)[1]
        observed = closure.paired_observations(state, data, block_size=1)
        compact = closure.paired_observations(state, data, include_pairs=False)
        for l in range(state.depth):
            np.testing.assert_allclose(observed["pairs"][l][..., 0], before[l], atol=1e-15)
            np.testing.assert_allclose(observed["pairs"][l][..., 1], current[l], atol=1e-15)
            expected = state.pi[l] @ ((current[l]-before[l])**2) @ data.probabilities
            self.assertAlmostEqual(float(observed["squared_motion"][l]), float(expected), places=15)
            self.assertAlmostEqual(float(observed["rms"][l]), float(np.sqrt(expected)), places=15)
            self.assertIsNone(compact["pairs"][l])
        np.testing.assert_allclose(observed["rms"], compact["rms"], atol=1e-15)

    def test_real_initializer_connects_without_retaining_transcript(self):
        state = closure.initialize(1, depth=3, dimension=2, initialization_nodes=12,
                                   population_nodes=8, epsilon_cov="0.01")
        self.assertEqual(state.depth, 3)
        self.assertEqual(set(state.__dict__), {"b", "pi", "g", "w", "c", "M", "D", "arithmetic", "metadata"})
        data = closure.DataLaw(np.eye(2), np.array([1., -1.]), np.array([.5, .5]))
        np.testing.assert_array_equal(closure.predict(state, data.inputs), [0., 0.])
        observed = closure.paired_observations(state, data)
        np.testing.assert_array_equal(observed["rms"], [0., 0., 0.])
        for actual, original in zip(state.M, state.D):
            np.testing.assert_array_equal(actual, original)
            self.assertIsNot(actual, original)

    def test_validation_rejects_wrong_dimension_weights_and_restart_schema(self):
        state, data = fixture()
        # The admissible working-precision dot-product tolerance scales with d.
        near_unit = np.array([[np.sqrt(1+4e-12), 0, 0]])
        self.assertEqual(closure.predict(state, near_unit).shape, (1,))
        with self.assertRaises(ValueError):
            closure.predict(state, np.eye(2))
        with self.assertRaises(ValueError):
            closure.apply_action(state, 1, np.zeros(len(state.b[0])))
        with self.assertRaises(ValueError):
            closure.apply_action(state, 2, np.zeros(len(state.b[1])))
        data.probabilities[0] = 0
        with self.assertRaises(ValueError):
            closure.rhs(state, data)
        state, data = fixture()
        bad = state.copy()
        bad.M[0] = bad.M[0].T
        with self.assertRaises(ValueError):
            bad.validate()
        path = self.scratch / "invalid.json"
        path.write_text(json.dumps({"format": "wrong"}), encoding="utf-8")
        with self.assertRaises(ValueError):
            closure.load_restart(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
