"""Check producer argument routing without compiling coefficient maps."""
from __future__ import annotations

from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from studies.mfp_linear_growth_uniform_counterexample import full_l2_paired_transition as producer


class ProducerPathTests(unittest.TestCase):
    def test_actual_help_from_external_cwd(self):
        with tempfile.TemporaryDirectory() as cwd:
            result = subprocess.run(
                [sys.executable, "-B", "-I", "-S", producer.__file__, "--help"],
                cwd=cwd, capture_output=True, text=True, timeout=10,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("--output-dir", result.stdout)
            self.assertEqual(list(Path(cwd).iterdir()), [])

    def test_help_exits_before_either_compiler(self):
        with mock.patch.object(sys, "argv", [producer.__file__, "--help"]), \
             mock.patch.object(producer, "compile_paired_map") as order5, \
             mock.patch.object(producer, "compile_paired_cubic_map") as order3, \
             redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                producer.main()
        self.assertEqual(raised.exception.code, 0)
        order5.assert_not_called()
        order3.assert_not_called()

    def test_default_output_is_study_generated_data(self):
        repo = Path(producer.__file__).resolve().parents[2]
        args = producer.STUDY_PATHS.parse([])
        self.assertEqual(args.output_dir, repo / "data/generated/mfp_linear_growth_uniform_counterexample")


if __name__ == "__main__":
    unittest.main()
