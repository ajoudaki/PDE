"""Tiny CSV/metadata routing fixtures; no scientific analysis is executed."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from .experiments import analyze_g2_gate_defect as g2
from .experiments import analyze_d3_reachable_tail as tail
from .experiments import analyze_marked_column_cavity as marked


class InputAliasTests(unittest.TestCase):
    def assert_refused(self, module, argv, paths):
        before = {path: path.read_bytes() for path in paths}
        with mock.patch.object(sys, 'argv', [module.__file__, *map(str, argv)]), \
             mock.patch.object(Path, 'open', side_effect=AssertionError('input read reached')):
            with self.assertRaises(ValueError):
                module.main()
        self.assertEqual(before, {path: path.read_bytes() for path in paths})

    def test_g2_all_alias_forms_refuse_before_read(self):
        for kind in ('same', 'symlink', 'hardlink', 'input-symlink', 'parent-symlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                raw = root / 'raw.csv'
                raw.write_bytes(b'untouched CSV fixture\n')
                output = root / 'result.json'
                if kind == 'same':
                    output = raw
                elif kind == 'symlink':
                    output.symlink_to(raw)
                elif kind == 'hardlink':
                    output.hardlink_to(raw)
                elif kind == 'input-symlink':
                    output.write_bytes(raw.read_bytes())
                    raw = root / 'selected.csv'
                    raw.symlink_to(output)
                else:
                    (root / 'alias').symlink_to(root, target_is_directory=True)
                    output = root / 'alias/raw.csv'
                self.assert_refused(g2, ['--input', raw, '--output', output], [raw])

    def test_tail_protects_every_primary_step_and_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            primary = [root / f'primary-{i}.csv' for i in range(2)]
            step = [root / f'step-{i}/raw.csv' for i in range(2)]
            metadata = [path.with_name('metadata.json') for path in step]
            for path in (*primary, *step, *metadata):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b'untouched selected input\n')
            for selected in (*primary, *step, *metadata):
                with self.subTest(input=selected):
                    self.assert_refused(tail, ['--primary', *primary, '--step', *step, '--output', selected], [*primary, *step, *metadata])

    def test_marked_both_outputs_protect_every_consumed_group(self):
        for leaf in ('summary.json', 'width_scaling.csv'):
            for group, name in (('primary', 'raw_replacement.csv'), ('primary', 'raw_jvp.csv'),
                                ('refined', 'raw_replacement.csv'), ('float64-coarse', 'raw_replacement.csv'),
                                ('float64-fine', 'raw_replacement.csv')):
                with self.subTest(output=leaf, group=group, input=name), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    selected = root / group / name
                    selected.parent.mkdir()
                    selected.write_bytes(b'untouched selected CSV\n')
                    output = root / 'fresh'
                    output.mkdir()
                    (output / leaf).symlink_to(selected)
                    argv = ['--primary', root / 'primary', '--output', output]
                    if group != 'primary':
                        argv += ['--' + group, selected.parent]
                    self.assert_refused(marked, argv, [selected])

    def test_named_source_guard_precedes_read(self):
        self.assert_refused(g2, ['--input', '/missing-input', '--output', g2.__file__], [Path(g2.__file__)])

    def test_empty_valid_fresh_workflows_preserve_selected_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw, metadata = root / 'raw.csv', root / 'metadata.json'
            raw.write_text('width,trial,time,clip\n')
            metadata.write_text('{"dt":0.01}\n')
            before = raw.read_bytes(), metadata.read_bytes()
            for module, argv in (
                (g2, ['--input', raw, '--output', root / 'fresh/g2.json']),
                (tail, ['--primary', raw, '--step', raw, '--output', root / 'fresh/tail.json']),
            ):
                with mock.patch.object(sys, 'argv', [module.__file__, *map(str, argv)]), redirect_stdout(io.StringIO()):
                    module.main()
            self.assertEqual(before, (raw.read_bytes(), metadata.read_bytes()))
            self.assertTrue((root / 'fresh/g2.json').is_file())
            self.assertTrue((root / 'fresh/tail.json').is_file())

    def test_direct_script_help_from_external_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            for module in (g2, tail, marked):
                result = subprocess.run([sys.executable, '-B', module.__file__, '--help'], cwd=tmp,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == '__main__':
    unittest.main()
