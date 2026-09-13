"""Static initialized-program tests; no trajectories or repository paths."""
from dataclasses import replace
from types import SimpleNamespace
import unittest

import numpy as np

from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_compiler import (
    GaussianCompiler, CompilerLimits, CompilerResourceLimit,
    CompilerNumericalError, compile_raw_dictionary,
)
from pde import observable_words as words


def sine_pilot():
    """A small explicit program with analytic covariance/response checks."""
    g1, g2 = words.seed("g1"), words.seed("g2")
    h1, h2 = words.unary("sin", g1), words.unary("sin", g2)
    z1, z2 = words.action(h1), words.action(h2)
    s1, s2 = words.unary("sin", z1), words.unary("sin", z2)
    p1, p2 = words.action(s1), words.action(s2)
    return dict(one1=words.constant(1), g1=g1, g2=g2, h1=h1, h2=h2,
                z1=z1, z2=z2, s1=s1, s2=s2, p1=p1, p2=p2,
                t1=words.unary("tanh", p1), t2=words.unary("tanh", p2),
                one2=words.constant(2))


class JointGaussianCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pilot = sine_pilot()
        cls.forward = words.action(cls.pilot["t1"])
        cls.mixed = words.multiply(words.unary("sin", cls.forward),
                                   words.unary("cos", cls.pilot["z2"]))
        cls.reverse = words.action(cls.mixed)
        cls.terminal = words.multiply(words.unary("tanh", cls.reverse), cls.pilot["t1"])
        cls.targets = list(cls.pilot.values())+[cls.forward, cls.mixed, cls.reverse, cls.terminal]
        cls.program = GaussianCompiler(Arithmetic(), gaussian_points, 257, 0.001).compile(
            cls.targets, population_nodes=131)

    def test_nested_full_gram_and_persistent_old_values(self):
        for population in (1, 2):
            source = self.program.source_lists[population]
            inputs = np.column_stack([self.program._values[s.operand] for s in source])
            expected = inputs.T@inputs/257+0.001*np.eye(len(source))
            factor = self.program.factors[population]
            np.testing.assert_allclose(factor@factor.T, expected, rtol=0, atol=2e-14)
        prefix = GaussianCompiler(Arithmetic(), gaussian_points, 257, 0.001).compile(self.pilot.values())
        for word in self.pilot.values():
            np.testing.assert_array_equal(prefix.evaluate(word), self.program.evaluate(word))

    def test_nested_named_derivatives_by_formal_coordinate_perturbation(self):
        program = self.program
        _, normals = program._at_count(131)
        gaussian = {pop: normals[pop][:, 2 if pop == 1 else 0:]@program.factors[pop].T
                    for pop in (1, 2)}
        for word in (self.forward, self.mixed, self.reverse, self.terminal):
            index = program._word(word, False)
            _, derivative = program.evaluate(word, 131, True)
            for coordinate in range(derivative.shape[1]):
                outputs = []
                for sign in (1, -1):
                    perturbed = {pop: g.copy() for pop, g in gaussian.items()}
                    perturbed[word.population][:, coordinate] += sign*1e-6
                    result = []
                    for node in range(len(program.nodes)):
                        result.append(program._value(node, result, normals, perturbed))
                    outputs.append(result[index])
                estimate = (outputs[0]-outputs[1])/2e-6
                np.testing.assert_allclose(estimate, derivative[:, coordinate], rtol=0, atol=3e-9)

    def test_replay_freezes_coefficients_and_keeps_joint_coordinates(self):
        old = [d["response_coefficients"].copy() for d in self.program.diagnostics]
        first = self.program.evaluate(self.terminal, 131)
        second = self.program.evaluate(self.terminal, 131)
        np.testing.assert_array_equal(first, second)
        for before, diagnostic in zip(old, self.program.diagnostics):
            np.testing.assert_array_equal(before, diagnostic["response_coefficients"])
        expected = np.tanh(self.program.evaluate(self.reverse, 131))*self.program.evaluate(self.pilot["t1"], 131)
        np.testing.assert_allclose(first, expected, rtol=0, atol=0)

    def test_dependent_and_zero_queries_keep_named_coordinates(self):
        one = words.constant(1)
        requests = [words.action(words.scale(0, one)), words.action(one),
                    words.action(words.scale(2, one))]
        program = GaussianCompiler(Arithmetic(), gaussian_points, 31, 0.0001).compile(requests)
        self.assertEqual(len(program.source_lists[2]), 3)
        _, partials = program.evaluate(requests[2], derivative=True)
        np.testing.assert_array_equal(partials, np.tile([0., 0., 1.], (31, 1)))
        self.assertTrue(all(d["innovation_variance"] > 0 for d in program.diagnostics))

    def test_complete_word_grammar_and_initialization_aliases(self):
        grammar = [word for n in range(100) if (word := words.decode_word(n)) is not None]
        aliases = [SimpleNamespace(op="w1", population=1), SimpleNamespace(op="w2", population=1),
                   SimpleNamespace(op="c", population=2),
                   SimpleNamespace(op="frozen_z20", population=2, mark=(0.6, 0.8))]
        program = GaussianCompiler(Arithmetic(), gaussian_points, 61, 0.001).compile(grammar+aliases)
        for word in grammar+aliases:
            value, partials = program.evaluate(word, 47, True)
            self.assertTrue(np.all(np.isfinite(value)))
            self.assertTrue(np.all(np.isfinite(partials)))
        np.testing.assert_array_equal(program.evaluate(aliases[2]), 0)
        np.testing.assert_array_equal(program.evaluate(aliases[0]), program.evaluate(words.seed("g1")))

    def test_raw_dictionary_uses_one_complete_union_and_forward_contraction(self):
        p = self.pilot
        first = [p[k] for k in ("one1", "h1", "h2", "t1", "t2", "one1")]
        second = [p[k] for k in ("s1", "s2", "one2", "one2")]
        raw = compile_raw_dictionary(first, second, arithmetic=Arithmetic(), gaussian_points=gaussian_points,
                                    initialization_nodes=257, population_nodes=131, epsilon_cov=0.001)
        self.assertEqual(raw.psi1.shape, (131, 6))
        self.assertEqual(raw.psi2.shape, (131, 4))
        q1, q2 = raw.program.table(first), raw.program.table(second)
        np.testing.assert_allclose(raw.gram1, q1.T@q1/257, rtol=0, atol=3e-15)
        forward = raw.program.table([words.action(word) for word in first])
        reverse = raw.program.table([words.action(word) for word in second])
        np.testing.assert_allclose(raw.C, q2.T@forward/257, rtol=0, atol=3e-15)
        np.testing.assert_allclose(raw.C_reverse, reverse.T@q1/257, rtol=0, atol=3e-15)
        np.testing.assert_array_equal(raw.psi1[:, 0], raw.psi1[:, -1])

    def test_resource_limits_fail_before_gaussian_allocation(self):
        configurations = [replace(CompilerLimits(), **change) for change in
                          ({"max_nodes": 2}, {"max_sources": 1}, {"max_points": 4},
                           {"max_working_bytes": 64}, {"max_work_units": 1})]
        for limits in configurations:
            with self.subTest(limits=limits):
                def forbidden(*args):
                    self.fail("allocated Gaussian cloud before rejecting resource limit")
                with self.assertRaises(CompilerResourceLimit):
                    GaussianCompiler(Arithmetic(), forbidden, 31, 0.001, limits).compile(
                        self.pilot.values(), population_nodes=47)

    def test_decimal_and_rational_backend_values_and_derivatives(self):
        tiny = [self.pilot[k] for k in ("h1", "z1", "s1", "p1", "t1")]
        base = GaussianCompiler(Arithmetic(), gaussian_points, 11, 0.001).compile(tiny)
        for backend in ("decimal", "rational"):
            with self.subTest(backend=backend):
                precise = GaussianCompiler(Arithmetic(40, backend=backend), gaussian_points, 11, "0.001").compile(tiny)
                for word in tiny:
                    actual, derivative = precise.evaluate(word, 13, True)
                    expected, expected_derivative = base.evaluate(word, 13, True)
                    np.testing.assert_allclose(np.asarray(actual, dtype=float), expected, rtol=0, atol=2e-12)
                    np.testing.assert_allclose(np.asarray(derivative, dtype=float), expected_derivative, rtol=0, atol=2e-12)

    def test_unresolved_pivot_raises_and_precision_resolves_it(self):
        one = words.constant(1)
        requests = [words.action(one), words.action(words.scale(2, one))]
        with self.assertRaises(CompilerNumericalError):
            GaussianCompiler(Arithmetic(), gaussian_points, 7, 1e-100).compile(requests)
        resolved = GaussianCompiler(Arithmetic(120), gaussian_points, 7, "1e-100").compile(requests)
        self.assertEqual(len(resolved.sources), 2)
        self.assertGreater(resolved.diagnostics[-1]["innovation_variance"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
