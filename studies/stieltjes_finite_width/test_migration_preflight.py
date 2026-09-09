"""Trace provenance routing in both mains with every scientific dependency mocked."""
import ast
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace as NS
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parent


class MigratedRecurrenceTests(unittest.TestCase):
    def test_both_mains_hash_the_current_declared_compiler_path(self):
        for filename, target_name in (("run_fresh_order13_median.py", "exact_targets"),
                                      ("run_fresh_calibrated_ratio.py", "exact_values")):
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                path = ROOT / filename
                tree = ast.parse(path.read_text())
                main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
                self.assertNotIn("PEELING", {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)})
                compiler = next(n.value for n in tree.body if isinstance(n, ast.Assign)
                                and any(isinstance(t, ast.Name) and t.id == "MFP_COMPILER" for t in n.targets))
                location = eval(compile(ast.Expression(compiler), str(path), "eval"), {"HERE": ROOT})
                hashes = mock.Mock(return_value="inert digest")
                stop = mock.Mock(side_effect=LookupError("stop before scientific work"))
                env = dict(Path=Path, __file__=str(path), os=os, OUT=Path(tmp) / "output",
                           parse_paths=lambda _: NS(output_dir=Path(tmp) / "output"),
                           resource=NS(RLIMIT_AS=0, setrlimit=mock.Mock()), ADDRESS_CAP=1,
                           WIDTHS=(1,), COUNT=1, SEED_BASE=1, BOOTSTRAPS=1, BOOTSTRAP_BASE=1,
                           PROTOCOL=ROOT / "unread-protocol", CERTIFICATE=ROOT / "unread-certificate",
                           MFP_COMPILER=location, sha256=hashes, platform=NS(python_version=lambda: "mock"),
                           np=NS(__version__="mock", empty=stop, float64=None), adjacent_ratios=stop)
                env[target_name] = lambda: (NS(tolist=lambda: []), 0)
                exec(compile(ast.Module(body=[main], type_ignores=[]), str(path), "exec"), env)
                with self.assertRaisesRegex(LookupError, "stop before scientific work"):
                    env["main"]()
                self.assertIn(mock.call(ROOT.parent / "mfp_quadratic_compiler/finite_width_jet_reference.py"), hashes.call_args_list)
                stop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
