"""Guard-only comparison fixtures, stopping before coefficient/identity work."""

import ast
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

from studies._output_paths import StudyPaths
from studies.mfp_gaussian_calculus.order5.compiler import compare_independent as comparison


REPO = Path(__file__).resolve().parents[2]
IDENTITY = REPO / "studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search"
INPUTS = (comparison.INDEPENDENT.name, comparison.INDEPENDENT_TAGGED.name,
          comparison.INDEPENDENT_SYMBOLIC_Q0.name)
OUTPUTS = ("PRIMARY_UNIT_COEFFICIENT_MAP.json", "PRIMARY_LAYER_TAGGED_COEFFICIENT_MAP.json",
           "PRIMARY_SYMBOLIC_Q0_COEFFICIENT_MAP.json", "INDEPENDENT_COMPARISON.json")


def identity_main(name):
    source = IDENTITY / name
    tree = ast.parse(source.read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    namespace = dict(PATHS=StudyPaths(source), HERE=IDENTITY, Path=Path, json=json, __file__=str(source))
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), "exec"), namespace)
    return namespace["main"]


class ConsumerInputTests(unittest.TestCase):
    def test_all_comparison_inputs_and_outputs_reject_input_side_aliases(self):
        for input_name in INPUTS:
            for output_name in OUTPUTS:
                for kind in ("input-symlink", "output-symlink", "hardlink"):
                    with self.subTest(input=input_name, output=output_name, kind=kind), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        selected, fresh = root / "selected", root / "fresh"
                        selected.mkdir()
                        fresh.mkdir()
                        for name in INPUTS:
                            if name != input_name:
                                (selected / name).write_bytes(b"inert selected input")
                        source, output = selected / input_name, fresh / output_name
                        if kind == "input-symlink":
                            output.write_bytes(b"inert selected input")
                            source.symlink_to(output)
                        else:
                            source.write_bytes(b"inert selected input")
                            if kind == "output-symlink":
                                output.symlink_to(source)
                            else:
                                output.hardlink_to(source)
                        science = Mock(side_effect=AssertionError("compiler dispatched"))
                        with patch.object(sys, "argv", ["compare", "--independent-dir", str(selected), "--output-dir", str(fresh)]), \
                             patch.object(comparison, "compile_factored", science), self.assertRaises(ValueError):
                            comparison.main()
                        science.assert_not_called()
                        self.assertTrue(all((selected / name).read_bytes() == b"inert selected input" for name in INPUTS))

    def test_comparison_allows_distinct_files_in_same_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in INPUTS:
                (root / name).write_bytes(b"inert selected input")
            for name in OUTPUTS:
                (root / name).write_bytes(b"ordinary old output")
            with patch.object(sys, "argv", ["compare", "--independent-dir", str(root), "--output-dir", str(root)]), \
                 patch.object(comparison, "compile_factored", side_effect=RuntimeError("stop before compiler")), \
                 self.assertRaisesRegex(RuntimeError, "stop before compiler"):
                comparison.main()
            self.assertTrue(all((root / name).read_bytes() == b"inert selected input" for name in INPUTS))
            self.assertTrue(all((root / name).read_bytes() == b"ordinary old output" for name in OUTPUTS))

    def test_identity_consumers_refuse_before_reading_selected_input(self):
        for filename, output_name in (("spectral_closure.py", "SPECTRAL_CLOSURE_RESULTS.json"),
                                      ("audit_hankel40.py", "HANKEL40_RESULTS.json")):
            main = identity_main(filename)
            for kind in ("input-symlink", "output-symlink", "hardlink"):
                with self.subTest(file=filename, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    selected, fresh = root / "selected", root / "fresh"
                    selected.mkdir()
                    fresh.mkdir()
                    source, output = selected / "RESULTS.json", fresh / output_name
                    if kind == "input-symlink":
                        output.write_bytes(b"inert selected input")
                        source.symlink_to(output)
                    else:
                        source.write_bytes(b"inert selected input")
                        if kind == "output-symlink":
                            output.symlink_to(source)
                        else:
                            output.hardlink_to(source)
                    with patch.object(sys, "argv", [filename, "--input-dir", str(selected), "--output-dir", str(fresh)]), \
                         patch.object(Path, "read_text", side_effect=AssertionError("input decoding reached")), \
                         self.assertRaises(ValueError):
                        main()
                    self.assertEqual(source.read_bytes(), b"inert selected input")

    def test_identity_consumers_keep_distinct_same_directory_refresh(self):
        for filename, output_name in (("spectral_closure.py", "SPECTRAL_CLOSURE_RESULTS.json"),
                                      ("audit_hankel40.py", "HANKEL40_RESULTS.json")):
            main = identity_main(filename)
            with self.subTest(file=filename), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "RESULTS.json").write_bytes(b"inert selected input")
                (root / output_name).write_bytes(b"ordinary old output")
                with patch.object(sys, "argv", [filename, "--input-dir", str(root), "--output-dir", str(root)]), \
                     patch.object(Path, "read_text", side_effect=RuntimeError("stop before input read")), \
                     self.assertRaisesRegex(RuntimeError, "stop before input read"):
                    main()
                self.assertEqual((root / "RESULTS.json").read_bytes(), b"inert selected input")
                self.assertEqual((root / output_name).read_bytes(), b"ordinary old output")


if __name__ == "__main__":
    unittest.main()
