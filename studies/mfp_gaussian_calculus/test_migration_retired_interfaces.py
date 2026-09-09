"""Tiny routing and refusal checks; no recurrence or scientific checks run."""
from __future__ import annotations

from contextlib import ExitStack, redirect_stdout
from fractions import Fraction
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RETIRED = (
    ("depth_order5_scalar/independent/forward_contraction.py", "emit", ("transition",)),
    ("depth_order5_scalar/independent/reverse_contraction.py", "emit", ("transition",)),
    ("depth_order5_scalar/independent/moving_contraction.py", "emit", ("transitions",)),
    ("depth_order5_scalar/multi_observable/independent_route_a/gamma04_contraction.py", "emit", ("transitions",)),
    ("depth_order5_observables/independent/gamma04_contraction.py", "emit", ("transitions", "local_audit")),
    ("depth_order5_scalar/independent/build_full_report.py", "build", ("equation_appendix",)),
    ("depth_order5_observables/independent/reduce_frozen_head.py", "main", ("reduce",)),
    ("depth_order5/primary/build_self_contained_report.py", "build", ("build_bytes",)),
    ("order5/run_checks.py", "run", ("run_finite_width", "run_compiler", "run_hostile")),
    ("order5/audit_hostile.py", "run", ("test_universal_six_family_identity",)),
)


class RetiredInterfaceTests(unittest.TestCase):
    def test_clis_refuse_from_external_cwd_without_site_dependencies(self):
        with tempfile.TemporaryDirectory() as cwd:
            for relative, _entry, _work in RETIRED:
                with self.subTest(source=relative):
                    result = subprocess.run(
                        [sys.executable, "-B", "-I", "-S", str(HERE / relative)],
                        cwd=cwd, capture_output=True, text=True, timeout=10,
                    )
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("RuntimeError: archive-only", result.stderr)
                    self.assertNotIn("ImportError", result.stderr)
                    self.assertNotIn("ModuleNotFoundError", result.stderr)
                    self.assertEqual(result.stdout, "")
            self.assertEqual(list(Path(cwd).iterdir()), [])

    def test_imported_writers_and_runners_refuse_before_work_or_io(self):
        for relative, entry, work in RETIRED:
            name = "studies.mfp_gaussian_calculus." + relative[:-3].replace("/", ".")
            module = importlib.import_module(name)
            with self.subTest(source=relative), ExitStack() as stack:
                tripwires = [
                    stack.enter_context(mock.patch.object(
                        module, function, side_effect=AssertionError("scientific work reached")
                    )) for function in work
                ]
                for operation in ("resolve", "read_text", "read_bytes", "write_text", "write_bytes", "mkdir"):
                    stack.enter_context(mock.patch.object(
                        Path, operation, side_effect=AssertionError("filesystem work reached")
                    ))
                with self.assertRaisesRegex(RuntimeError, "archive-only"):
                    getattr(module, entry)()
                if entry == "emit":
                    with self.assertRaisesRegex(RuntimeError, "archive-only"):
                        module.emit(Path("unused-scratch"))
                for tripwire in tripwires:
                    tripwire.assert_not_called()

    def test_pure_modules_and_individual_tests_remain_importable(self):
        from studies.mfp_gaussian_calculus.depth_order5_scalar.independent import forward_contraction
        from studies.mfp_gaussian_calculus.order5 import audit_hostile
        from studies.mfp_gaussian_calculus.depth_order5_observables.independent import reduce_frozen_head
        from studies.mfp_gaussian_calculus.depth_order5.primary import build_self_contained_report
        self.assertTrue(callable(forward_contraction.transition))
        self.assertTrue(callable(audit_hostile.test_universal_six_family_identity))
        self.assertTrue(callable(reduce_frozen_head.reduce))
        self.assertTrue(callable(build_self_contained_report.build_bytes))


class FrozenComparisonInputTests(unittest.TestCase):
    def test_compiler_package_dispatches_retained_gate_before_science(self):
        from studies.mfp_gaussian_calculus.order5.compiler import run_checks as runner
        from studies.mfp_gaussian_calculus.study_paths import HISTORICAL_ROOT

        gate_name = 'test_all_frozen_coefficient_comparisons_report_zero_discrepancies'
        gate = getattr(runner.test_population_jet, gate_name)
        paths = []
        read_text = Path.read_text

        def read(path, *args, **kwargs):
            paths.append(path)
            return read_text(path, *args, **kwargs)

        with ExitStack() as stack:
            selected = stack.enter_context(mock.patch.object(runner.test_population_jet, gate_name, wraps=gate))
            selected.__name__ = gate_name
            for name in dir(runner.test_population_jet):
                if name.startswith('test_') and name != gate_name:
                    stack.enter_context(mock.patch.object(
                        runner.test_population_jet, name, side_effect=RuntimeError('stop before science')
                    ))
            stack.enter_context(mock.patch.object(Path, 'read_text', read))
            stack.enter_context(redirect_stdout(io.StringIO()))
            with self.assertRaisesRegex(RuntimeError, 'stop before science'):
                runner.run()
            selected.assert_called_once_with()
        self.assertEqual(paths, [
            HISTORICAL_ROOT / 'order5/compiler/INDEPENDENT_COMPARISON.json',
            HISTORICAL_ROOT / 'order5/independent/SYMBOLIC_Q0_PRIMARY_COMPARISON.json',
        ])

    def test_historical_paths_and_both_retained_map_schemas(self):
        from studies.mfp_gaussian_calculus.depth_order5_scalar.independent import depth_assembler as assembler
        expected = {name: {("M010000",): Fraction(3, 2)} for name in "ABC"}
        for depth in (2, 3, 4):
            relative = ("order5/compiler/PRIMARY_UNIT_COEFFICIENT_MAP.json" if depth == 2
                        else f"depth_order5/primary/H{depth}_UNIT_COEFFICIENTS.json")
            path = REPO / "data/historical/studies/mfp_gaussian_calculus" / relative
            entries = [{"atoms": ["M_010000"], "coefficient": "1"},
                       {"atoms": ["M_010000"], "coefficient": "1/2"}]
            if depth == 2:
                payload = {"unit_gram": {name: entries for name in "ABC"}}
            else:
                payload = {"roots": {name: [[row["atoms"], row["coefficient"]] for row in entries]
                                     for name in "ABC"}}
            with self.subTest(depth=depth), \
                 mock.patch.object(Path, "read_text", autospec=True, return_value=json.dumps(payload)) as read, \
                 mock.patch.object(assembler, "compile_depth", return_value=expected) as compile_depth:
                self.assertEqual(assembler._read_accepted(depth), expected)
                read.assert_called_once_with(path)
                compile_depth.assert_not_called()
                comparison = assembler.compare_accepted(depth)
                compile_depth.assert_called_once_with(depth)
                self.assertTrue(all(row["discrepancies"] == 0 for row in comparison["roots"].values()))
                self.assertEqual(read.call_args, mock.call(path))

    def test_missing_or_malformed_retained_inputs_do_not_fall_back(self):
        from studies.mfp_gaussian_calculus.depth_order5_scalar.independent import depth_assembler as assembler
        with mock.patch.object(Path, "read_text", side_effect=FileNotFoundError("missing retained map")) as read:
            with self.assertRaises(FileNotFoundError):
                assembler._read_accepted(2)
            read.assert_called_once()
        with mock.patch.object(Path, "read_text", return_value="{}"):
            with self.assertRaises(KeyError):
                assembler._read_accepted(3)


if __name__ == "__main__":
    unittest.main()
