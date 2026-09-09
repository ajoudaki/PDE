"""Path-only owning-study checks; no legacy engines or attempts."""
import ast
import csv
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies.stieltjes_hybrid_campaign.breadth_panel.successive_paths import (
    GENERATED_PANEL, REPO, parse_analysis_paths, require_output,
)


class OutputBoundaryTests(unittest.TestCase):
    def test_linked_children_are_rejected_without_writes(self):
        for kind in ('symlink', 'hardlink', 'dangling', 'directory'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                output = root/'output'
                output.mkdir()
                retained = root/'input'
                retained.write_bytes(b'unchanged')
                alias = output/'analysis.json.tmp'
                if kind == 'hardlink':
                    os.link(retained, alias)
                else:
                    alias.symlink_to(root if kind == 'directory' else
                                     root/'absent' if kind == 'dangling' else retained)
                with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaises(ValueError):
                    parse_analysis_paths('successive_n4096', ['--output-dir', str(output)])
                mkdir.assert_not_called()
                self.assertEqual(retained.read_bytes(), b'unchanged')

    def test_both_analysis_json_csv_writers_use_exclusive_temporaries(self):
        # Compile just the actual I/O functions; no analyzer imports or math.
        for relative in ('successive_n4096/analyze.py', 'successive_n8192/compare_with_n4096.py'):
            source = Path(__file__).parent/relative
            nodes = [n for n in ast.parse(source.read_text()).body if isinstance(n, ast.FunctionDef)
                     and n.name in ('write_json_atomic', 'write_csv_atomic')]
            future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
            env = dict(require_output=require_output, json=json, csv=csv, os=os, require=lambda *a: None)
            exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])),
                         str(source), 'exec'), env)
            for name, value in (('write_json_atomic', {'fixture': 1}), ('write_csv_atomic', [{'fixture': 1}])):
                with self.subTest(source=source, writer=name), tempfile.TemporaryDirectory() as tmp:
                    output = Path(tmp)/'output'
                    env[name](output, value)
                    expected = output.read_bytes()
                    # Ordinary prior products can still be refreshed.
                    env[name](output, value)
                    self.assertEqual(output.read_bytes(), expected)
                    temporary = Path(tmp)/'output.tmp'
                    temporary.write_bytes(b'preserve collision')
                    with self.assertRaises(FileExistsError):
                        env[name](output, value)
                    self.assertEqual(output.read_bytes(), expected)
                    self.assertEqual(temporary.read_bytes(), b'preserve collision')

    def test_source_history_and_foreign_generated_are_rejected_without_writes(self):
        for target in (REPO/'studies/stieltjes_hybrid_campaign',
                       REPO/'data/historical/studies/stieltjes_hybrid_campaign',
                       REPO/'data/generated/resnet_activation_controls',
                       REPO/'data/generated/stieltjes_hybrid_campaign_other',
                       REPO/'data/generated'):
            with self.subTest(target=target), mock.patch.object(Path, 'mkdir') as mkdir:
                with self.assertRaises(ValueError):
                    require_output(target)
                with self.assertRaises(ValueError):
                    parse_analysis_paths('successive_n4096', ['--output-dir', str(target)])
                mkdir.assert_not_called()

    def test_own_study_and_scratch_remain_valid_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(Path, 'mkdir') as mkdir:
            for target in (GENERATED_PANEL/'successive_n4096', GENERATED_PANEL.parent/'other-output', Path(tmp)/'fresh'):
                self.assertEqual(require_output(target), target.resolve())
                self.assertEqual(parse_analysis_paths('successive_n4096', ['--output-dir', str(target)]).output_dir,
                                 target.resolve())
            mkdir.assert_not_called()


if __name__ == '__main__':
    unittest.main()
