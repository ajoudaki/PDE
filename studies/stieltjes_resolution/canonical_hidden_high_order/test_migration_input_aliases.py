"""Tiny routing/source-record fixtures; never evaluate a recurrence or audit."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from . import hidden_moment_hankel_audit as hankel
from . import independent_hidden_scalar_audit as scalar


def source_record(role, style='basename', field='file'):
    filename = role + '_hidden_recurrence.py'
    label = {
        'basename': filename,
        'current': 'studies/stieltjes_resolution/canonical_hidden_high_order/' + filename,
        'legacy': 'studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/' + filename,
    }[style]
    return {'source': {field: label, 'sha256': hashlib.sha256((hankel.HERE / filename).read_bytes()).hexdigest()}}


class SourceSlotTests(unittest.TestCase):
    def test_swapped_and_duplicate_roles_refuse_before_derivatives(self):
        for production_role, independent_role in (('production', 'production'), ('independent', 'independent'), ('independent', 'production')):
            for style in ('basename', 'current', 'legacy'):
                with self.subTest(production=production_role, independent=independent_role, style=style), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    paths = (root / 'production.json', root / 'independent.json')
                    for path, role in zip(paths, (production_role, independent_role)):
                        path.write_text(json.dumps(source_record(role, style)))
                    before = [path.read_bytes() for path in paths]
                    with mock.patch.object(hankel, 'exact_derivatives', side_effect=AssertionError('science reached')) as work:
                        with self.assertRaisesRegex(ValueError, 'source role'):
                            hankel.build_audit(*paths)
                        work.assert_not_called()
                    self.assertEqual(before, [path.read_bytes() for path in paths])

    def test_correct_roles_and_all_accepted_labels_reach_only_derivative_tripwire(self):
        for style in ('basename', 'current', 'legacy'):
            for field in ('file', 'path'):
                with self.subTest(style=style, field=field), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    paths = (root / 'production.json', root / 'independent.json')
                    for path, role in zip(paths, ('production', 'independent')):
                        path.write_text(json.dumps(source_record(role, style, field)))
                    with mock.patch.object(hankel, 'exact_derivatives', side_effect=RuntimeError('stop before science')):
                        with self.assertRaisesRegex(RuntimeError, 'stop before science'):
                            hankel.build_audit(*paths)

    def test_exact_hash_failure_is_not_replaced_by_role_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selected = root / 'selected.json'
            document = source_record('independent')
            document['source']['sha256'] = '0' * 64
            selected.write_text(json.dumps(document))
            with mock.patch.object(hankel, 'exact_derivatives', side_effect=AssertionError('science reached')):
                with self.assertRaisesRegex(AssertionError, 'source hash mismatch'):
                    hankel.build_audit(selected, selected)
            self.assertEqual(json.loads(selected.read_text()), document)


class OutputAliasTests(unittest.TestCase):
    def test_both_clis_protect_both_inputs_before_audit(self):
        for target, entry in ((hankel, 'build_audit'), (scalar, 'audit_documents')):
            for role in ('production', 'independent'):
                for kind in ('same', 'symlink', 'hardlink', 'input-symlink'):
                    with self.subTest(module=target.__name__, role=role, kind=kind), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        inputs = {name: root / (name + '.json') for name in ('production', 'independent')}
                        for path in inputs.values():
                            path.write_bytes(b'untouched metadata fixture')
                        output = root / 'result.json'
                        if kind == 'same':
                            output = inputs[role]
                        elif kind == 'symlink':
                            output.symlink_to(inputs[role])
                        elif kind == 'hardlink':
                            output.hardlink_to(inputs[role])
                        else:
                            output.write_bytes(b'untouched metadata fixture')
                            inputs[role] = root / 'input-link.json'
                            inputs[role].symlink_to(output)
                        argv = [target.__file__, '--production', str(inputs['production']), '--independent', str(inputs['independent']), '--output', str(output)]
                        with mock.patch.object(sys, 'argv', argv), mock.patch.object(target, entry, side_effect=AssertionError('audit reached')) as work:
                            with self.assertRaises(ValueError):
                                target.main()
                            work.assert_not_called()
                        self.assertTrue(all(path.read_bytes() == b'untouched metadata fixture' for path in inputs.values()))

    def test_stdout_and_disjoint_destinations_still_dispatch(self):
        for target, entry in ((hankel, 'build_audit'), (scalar, 'audit_documents')):
            with tempfile.TemporaryDirectory() as tmp:
                for output in ([], ['--output', str(Path(tmp) / 'fresh.json')]):
                    with mock.patch.object(sys, 'argv', [target.__file__, *output]), mock.patch.object(target, entry, side_effect=RuntimeError('stop before science')):
                        with self.assertRaisesRegex(RuntimeError, 'stop before science'):
                            target.main()
                self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_direct_script_help_from_external_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            for target in (hankel, scalar):
                result = subprocess.run([sys.executable, '-B', target.__file__, '--help'], cwd=tmp,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == '__main__':
    unittest.main()
