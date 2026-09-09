"""Path-only owning-study checks; no campaign modules imported."""
import contextlib
import ast
import io
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

from studies.stieltjes_finite_width import run_paths
from studies.stieltjes_finite_width.run_paths import GENERATED_ROOT, REPO_ROOT, parse_paths


class OutputBoundaryTests(unittest.TestCase):
    def test_jet_child_aliases_refuse_before_reading_or_regenerating(self):
        source = Path(__file__).with_name('jet_control_variate.py')
        main = next(n for n in ast.parse(source.read_text()).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'main')
        for kind in ('symlink', 'hardlink', 'dangling', 'directory'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                inputs, output = root/'inputs', root/'generated'
                inputs.mkdir()
                output.mkdir()
                retained = inputs/'raw_width_64.npz'
                retained.write_bytes(b'retained raw fixture; never read as an array')
                alias = output/'jets_and_cv_width_64.npz'
                if kind == 'hardlink':
                    os.link(retained, alias)
                else:
                    alias.symlink_to(inputs if kind == 'directory' else
                                     root/'absent' if kind == 'dangling' else retained)
                load, jets = mock.Mock(), mock.Mock()
                env = dict(OUT=output, RUN=inputs, HISTORICAL_RUN=inputs,
                           parse_paths=run_paths.parse_paths, regenerate_pair_jets=jets,
                           np=mock.Mock(load=load))
                exec(compile(ast.Module(body=[main], type_ignores=[]), str(source), 'exec'), env)
                with mock.patch.object(sys, 'argv', ['jet']), mock.patch.object(Path, 'mkdir') as mkdir, \
                     contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    env['main']()
                load.assert_not_called()
                jets.assert_not_called()
                mkdir.assert_not_called()
                self.assertEqual(retained.read_bytes(), b'retained raw fixture; never read as an array')

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
