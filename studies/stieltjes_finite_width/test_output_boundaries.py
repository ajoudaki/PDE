"""Path-only owning-study checks; no campaign modules imported."""
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies.stieltjes_finite_width.run_paths import GENERATED_ROOT, REPO_ROOT, parse_paths


class OutputBoundaryTests(unittest.TestCase):
    def test_source_history_and_foreign_generated_are_rejected_without_writes(self):
        for target in (REPO_ROOT/'studies/stieltjes_finite_width',
                       REPO_ROOT/'data/historical/studies/stieltjes_finite_width',
                       REPO_ROOT/'data/generated/resnet_activation_controls',
                       REPO_ROOT/'data/generated/stieltjes_finite_width_other',
                       REPO_ROOT/'data/generated'):
            with self.subTest(target=target), mock.patch.object(Path, 'mkdir') as mkdir, \
                 contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    parse_paths(GENERATED_ROOT/'runs/test', ['--output-dir', str(target)])
                mkdir.assert_not_called()

    def test_own_generated_and_scratch_remain_valid_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(Path, 'mkdir') as mkdir:
            for target in (GENERATED_ROOT/'runs/test', Path(tmp)/'fresh'):
                self.assertEqual(parse_paths(GENERATED_ROOT/'runs/test', ['--output-dir', str(target)]).output_dir,
                                 target.resolve())
            mkdir.assert_not_called()


if __name__ == '__main__':
    unittest.main()
