"""Predeclared deterministic checks of the H4 law interface; no trajectories.

Frozen local test budget before execution: 120 CPU seconds, 180 wall seconds,
512 MiB expected peak RSS, one numerical thread. The repository envelope is
600 CPU seconds per frozen edition; these checks consume part of it. A failed
or timed-out test remains failure and never authorizes a training experiment.

Command from repository root (fresh study-owned H4_TEST_RUN directory):
  timeout 180s env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 \
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
    H4_LAW_TEST_SCRATCH=$H4_TEST_RUN python -B \
    studies/observable_hierarchy/H4_laws_tests.py

Checks: bounded symbolic integer evaluation and resource rejection; exact
quarter-turn parametrization and nonatomic/atomic distinction; midpoint
transport algebra; strict exact-input typing; metadata and all-backend restart;
explicit collapse and eventual fixed-radius resolution as precision increases;
exact probability/coordinate rounding accounting. No initializer/RHS/evolve is
called. Logs, environment, exit code and source hashes belong in H4_TEST_RUN.
"""
from fractions import Fraction
import json
import os
from pathlib import Path
import resource
import tempfile
import unittest

import numpy as np

from pde.observable_arithmetic import Arithmetic
from pde.observable_solver import State, save_restart, load_restart
from H4_laws import (IntegerExpression as E, DyadicRadius, RationalRadius,
                     OrthogonalArcLaw, LawLimits, LawResourceLimit,
                     radius_from_record, _fraction_from_record, _working_fraction,
                     supported_radius, supported_law)


def U(z):
    z = Fraction(z)
    return ((1-z*z)/(1+z*z), 2*z/(1+z*z))


class SymbolicIntegerChecks(unittest.TestCase):
    def test_bounded_evaluation_matches_direct_small_integers(self):
        expressions = [(E.integer(7), 7), (E.pow2(4), 16),
                       (E.add(E.pow2(4), 5), 21),
                       (E.multiply(E.add(2, 3), E.pow2(3)), 40),
                       (E.pow2(E.pow2(4)), 65536)]
        for expression, actual in expressions:
            for cap in (0, 1, 2, 7, 15, 16, 20, 21, 39, 40, 100, 65535, 65536):
                with self.subTest(actual=actual, cap=cap):
                    self.assertEqual(expression.bounded_value(cap), min(actual, cap+1))

    def test_huge_tower_is_compact_and_compared_without_expansion(self):
        exponent = E.pow2(E.pow2(E.pow2(16)))
        self.assertEqual(exponent.bounded_value(1000), 1001)
        payload = json.dumps(exponent.to_record())
        self.assertLess(len(payload), 256)
        self.assertEqual(E.from_record(json.loads(payload)), exponent)
        law = OrthogonalArcLaw(DyadicRadius(exponent))
        rule = law.quadrature(3, Arithmetic(40))
        self.assertTrue(rule.metadata["collapsed_to_reference"])
        self.assertEqual(rule.metadata["exact_law"]["radius"], law.radius.to_record())
        self.assertLess(len(json.dumps(rule.metadata)), 10000)

    def test_positive_expression_validation_and_limits(self):
        for value in (True, 0, -1, 1.0, "4"):
            with self.assertRaises(ValueError):
                E.integer(value)
        for expression in (E("pow2", args=(E.integer(1),)), E.add(2, 3)):
            self.assertEqual(E.from_record(expression.to_record()), expression)
        for record in ({"op": "integer", "value": "0x0"},
                       {"op": "integer", "value": 3},
                       {"op": "pow2", "args": []}, {"op": "unknown", "args": []}):
            with self.assertRaises(ValueError):
                E.from_record(record)
        with self.assertRaises(LawResourceLimit):
            E.pow2(E.pow2(2)).bounded_value(7, limits=LawLimits(max_expression_depth=2))
        with self.assertRaises(LawResourceLimit):
            E.integer(1 << 20).to_record(limits=LawLimits(max_literal_bits=8))
        with self.assertRaises(LawResourceLimit):
            DyadicRadius(E.pow2(10)).materialize(limits=LawLimits(max_exact_scalar_bits=100))

    def test_materialization_and_exact_radius_roundtrip(self):
        for radius in (DyadicRadius(E.add(3, 4)), RationalRadius("3/17")):
            restored = radius_from_record(json.loads(json.dumps(radius.to_record())))
            self.assertEqual(restored, radius)
            self.assertEqual(restored.materialize(), radius.materialize())
        self.assertEqual(DyadicRadius(7).materialize(), Fraction(1, 128))
        self.assertFalse(DyadicRadius(7).below_binary(7))
        self.assertTrue(DyadicRadius(8).below_binary(7))


class ExactLawChecks(unittest.TestCase):
    def test_supported_constructor_has_the_fixed_proved_tower(self):
        expression = supported_radius().exponent
        for _ in range(10):
            self.assertEqual(expression.op, "pow2")
            expression = expression.args[0]
        self.assertEqual(expression, E.integer(8192))
        atom = supported_law(a=0, b=0, c=1, d=1)
        arc = supported_law()
        self.assertEqual(atom.radius, arc.radius)
        self.assertEqual(atom.scope_tag, "H4_explicit_supported_T40")
        self.assertEqual(atom.quadrature(1, Arithmetic()).metadata["component_is_nonatomic"], [False, False])
        self.assertEqual(arc.quadrature(8, Arithmetic()).metadata["component_is_nonatomic"], [True, True])
        self.assertEqual(atom.exact_description()["radius"], arc.exact_description()["radius"])

    def test_nonorthogonal_atom_has_exact_quarter_turn_and_labels(self):
        law = OrthogonalArcLaw(RationalRadius("1/2"), a=1, b=1, c=0, d=0)
        rule = law.quadrature(11, Arithmetic(40))
        self.assertEqual(rule.inputs.shape, (2, 2))
        actual = [[_working_fraction(value) for value in row] for row in rule.inputs]
        self.assertEqual(actual, [[Fraction(3, 5), Fraction(4, 5)], [Fraction(0), Fraction(1)]])
        self.assertEqual(actual[0][0]*actual[1][0]+actual[0][1]*actual[1][1], Fraction(4, 5))
        self.assertEqual(list(rule.labels), [1, -1])
        self.assertEqual(list(rule.probabilities), [Fraction(1, 2)]*2)
        self.assertEqual(rule.metadata["component_is_nonatomic"], [False, False])

    def test_nonatomic_rule_exact_description_and_independent_refinement(self):
        law = OrthogonalArcLaw(DyadicRadius(3), a="-3/4", b="1/2", c="-1/3", d="2/3")
        description = law.exact_description()
        restored = OrthogonalArcLaw.from_description(json.loads(json.dumps(description)))
        self.assertEqual(restored, law)
        coarse, fine = law.quadrature(3, Arithmetic(50)), law.quadrature(6, Arithmetic(50))
        self.assertEqual(coarse.metadata["exact_law"], fine.metadata["exact_law"])
        self.assertEqual(coarse.inputs.shape, (6, 2))
        self.assertEqual(fine.inputs.shape, (12, 2))
        self.assertEqual(coarse.metadata["component_is_nonatomic"], [True, True])
        self.assertEqual(len({tuple(row) for row in coarse.inputs[:3]}), 3)
        first_bound = _fraction_from_record(coarse.metadata["exact_midpoint_transport_coefficient"])
        second_bound = _fraction_from_record(fine.metadata["exact_midpoint_transport_coefficient"])
        self.assertEqual(first_bound, 2*second_bound)

    def test_transport_bounds_from_exact_chord_identity_and_cell_integrals(self):
        r, a, b, m = Fraction(3, 7), Fraction(-3, 4), Fraction(2, 3), 7
        mean_parameter_error = Fraction(0)
        for j in range(m):
            left, right = a+(b-a)*Fraction(j, m), a+(b-a)*Fraction(j+1, m)
            midpoint = (left+right)/2
            # Integral of |s-midpoint| on a cell is length**2/4.
            mean_parameter_error += (right-left)**2/(4*(b-a))
            for s in (left, midpoint, right):
                actual, reference = U(r*s), U(r*midpoint)
                squared = sum((u-v)**2 for u, v in zip(actual, reference))
                oracle = 4*r*r*(s-midpoint)**2/((1+r*r*s*s)*(1+r*r*midpoint*midpoint))
                self.assertEqual(squared, oracle)
                self.assertLessEqual(squared, (2*r*abs(s-midpoint))**2)
        self.assertEqual(mean_parameter_error, (b-a)/(4*m))
        law = OrthogonalArcLaw(RationalRadius(r), a=a, b=b, c="-1/2", d="1/2")
        rule = law.quadrature(m, Arithmetic(40))
        bound = _fraction_from_record(rule.metadata["exact_midpoint_transport_coefficient"])*r
        self.assertEqual(bound, r*((b-a)+1)/(4*m))

    def test_collapse_is_explicit_and_fixed_radius_eventually_resolves(self):
        law = OrthogonalArcLaw(DyadicRadius(200))
        low = law.quadrature(2, Arithmetic(20, "rational"))
        high = law.quadrature(2, Arithmetic(80, "rational"))
        self.assertTrue(low.metadata["collapsed_to_reference"])
        self.assertFalse(high.metadata["collapsed_to_reference"])
        self.assertEqual(low.metadata["exact_law"], high.metadata["exact_law"])
        self.assertEqual(list(low.inputs[0]), [1, 0])
        self.assertNotEqual(high.inputs[0, 1], 0)
        bound = low.metadata["exact_rule_transport_bound"]
        self.assertEqual(bound["radius"], law.radius.to_record())
        self.assertEqual(_fraction_from_record(bound["coefficient"]), Fraction(5, 2))
        self.assertEqual(_fraction_from_record(low.metadata["maximum_coordinate_rounding_l1"]), 0)

    def test_disabling_collapse_rejects_unmaterializable_exponent(self):
        law = OrthogonalArcLaw(DyadicRadius(E.pow2(E.pow2(16))))
        with self.assertRaises(LawResourceLimit):
            law.quadrature(2, Arithmetic(30), allow_collapse=False)
        resolved_but_over_budget = OrthogonalArcLaw(DyadicRadius(200))
        with self.assertRaises(LawResourceLimit):
            resolved_but_over_budget.quadrature(2, Arithmetic(80), limits=LawLimits(max_exact_scalar_bits=100))
        with self.assertRaises(LawResourceLimit):
            resolved_but_over_budget.quadrature(5, Arithmetic(20), limits=LawLimits(max_rule_nodes=9))

    def test_coordinate_rounding_collapse_is_disclosed_without_replacement(self):
        law = OrthogonalArcLaw(DyadicRadius(100))
        data = law.quadrature(2, Arithmetic(20, "rational"))
        self.assertFalse(data.metadata["radius_replaced_by_zero"])
        self.assertTrue(data.metadata["dyadic_denominator_materialized"])
        self.assertTrue(data.metadata["exact_midpoint_rule_collapsed_by_rounding"])
        self.assertTrue(data.metadata["collapsed_to_reference"])
        self.assertGreater(data.metadata["reference_coordinate_rounding_count"], 0)
        self.assertGreater(_fraction_from_record(data.metadata["maximum_coordinate_rounding_l1"]), 0)
        self.assertEqual(_fraction_from_record(data.metadata["radius_replacement_transport_coefficient"]), 0)

    def test_exact_input_typing_bounds_and_exploratory_scope(self):
        for radius in (0, -1, True, 0.01, np.float64(0.01)):
            with self.assertRaises(ValueError):
                RationalRadius(radius)
        for argument in (dict(a=-1.0), dict(b=True), dict(a="-2"), dict(c=1, d=0)):
            with self.assertRaises(ValueError):
                OrthogonalArcLaw(DyadicRadius(10), **argument)
        exploratory = OrthogonalArcLaw(RationalRadius("1/10"), scope_tag="caller_claims_proved")
        self.assertEqual(exploratory.scope_tag, "exploratory_rational_radius_no_T40_guarantee")
        with self.assertRaises(ValueError):
            OrthogonalArcLaw.from_description({"format": "unrecognized"})

    def test_exact_rounding_accounting_all_backends(self):
        law = OrthogonalArcLaw(RationalRadius("1/7"), a="-1/2", b="1/3", c=0, d=0)
        for arithmetic in (Arithmetic(), Arithmetic(40), Arithmetic(24, "rational")):
            rule = law.quadrature(3, arithmetic)
            intended = []
            for j in range(3):
                s = law.a+(law.b-law.a)*Fraction(2*j+1, 6)
                intended.append(U(Fraction(1, 7)*s))
            intended.append((Fraction(0), Fraction(1)))
            coordinate_error = max(sum(abs(_working_fraction(x)-y) for x, y in zip(row, target))
                                   for row, target in zip(rule.inputs, intended))
            mass_error = sum(abs(_working_fraction(x)-y) for x, y in
                             zip(rule.probabilities, [Fraction(1, 6)]*3+[Fraction(1, 2)]))
            self.assertEqual(coordinate_error, _fraction_from_record(rule.metadata["maximum_coordinate_rounding_l1"]))
            self.assertEqual(mass_error, _fraction_from_record(rule.metadata["total_probability_rounding_l1"]))
            self.assertEqual(coordinate_error+8*mass_error,
                             _fraction_from_record(rule.metadata["rounded_rule_normalized_transport_addition"]))

    def test_exact_law_and_collapse_metadata_survive_all_backend_restart(self):
        scratch = os.environ.get("H4_LAW_TEST_SCRATCH")
        if not scratch:
            self.fail("set H4_LAW_TEST_SCRATCH to the fresh study-owned run directory")
        Path(scratch).mkdir(parents=True, exist_ok=True)
        for arithmetic in (Arithmetic(), Arithmetic(40), Arithmetic(24, "rational")):
            law = OrthogonalArcLaw(DyadicRadius(E.pow2(E.pow2(16))))
            data = law.quadrature(3, arithmetic)
            A = arithmetic.array
            state = State(A([[1]]), A([[0, 0]]), A([[0, 0]]), A([1]),
                          A([[1]]), A([0]), A([1]), A([[0]]), A([[0]]), arithmetic).validate()
            with tempfile.TemporaryDirectory(prefix="restart_", dir=scratch) as temporary:
                path = Path(temporary)/"restart.json"
                save_restart(path, state, data)
                restored, restored_data = load_restart(path)
                self.assertLess(path.stat().st_size, 20000)
            self.assertEqual(restored_data.metadata, data.metadata)
            self.assertEqual(OrthogonalArcLaw.from_description(restored_data.metadata["exact_law"]), law)
            for key in ("inputs", "labels", "probabilities"):
                np.testing.assert_array_equal(getattr(data, key), getattr(restored_data, key))
            for key in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"):
                np.testing.assert_array_equal(getattr(state, key), getattr(restored, key))


if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    unittest.main(verbosity=2)
