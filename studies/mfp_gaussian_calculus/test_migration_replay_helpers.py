"""Retired replay entrypoints refuse; helpers import without evidence reads."""
import ast
from contextlib import ExitStack
import hashlib
import importlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


HERE = Path(__file__).resolve().parent
CASES = (
    ('depth_order5_scalar/multi_observable/audit/run_hostile_checks.py',
     ('main', 'run_json'), ('parse_term', 'parse_expression', 'all_zero', 'sha256', 'load')),
    ('depth_order5/primary/run_lightweight_checks.py', ('main',), ('sha256', 'require')),
    ('depth_order5/audit/run_checks.py',
     ('main', 'verify_primary_freeze', 'verify_independent_freeze', 'verify_exact_certificates', 'verify_numerical_certificates'),
     ('digest', 'require')),
)


class ReplayHelperTests(unittest.TestCase):
    def test_source_import_has_no_input_reads_or_subprocess_work(self):
        for relative, _entries, helpers in CASES:
            path = HERE / relative
            code = compile(path.read_text(), str(path), 'exec')
            namespace = {'__name__': 'private_import_fixture', '__file__': str(path)}
            with self.subTest(source=relative), ExitStack() as stack:
                for name in ('read_text', 'read_bytes', 'write_text', 'write_bytes', 'mkdir'):
                    stack.enter_context(mock.patch.object(Path, name, side_effect=AssertionError('I/O reached')))
                stack.enter_context(mock.patch.object(subprocess, 'check_output', side_effect=AssertionError('subprocess reached')))
                exec(code, namespace)
                for name in helpers:
                    self.assertTrue(callable(namespace[name]))
                self.assertNotIn('checks', namespace)
                self.assertNotIn('result', namespace)

    def test_all_replay_and_subprocess_callables_refuse_before_work(self):
        for relative, entries, _helpers in CASES:
            module = importlib.import_module('studies.mfp_gaussian_calculus.' + relative[:-3].replace('/', '.'))
            for name in entries:
                with self.subTest(source=relative, entry=name), ExitStack() as stack:
                    for operation in ('resolve', 'read_text', 'read_bytes', 'write_text', 'write_bytes', 'mkdir'):
                        stack.enter_context(mock.patch.object(Path, operation, side_effect=AssertionError('I/O reached')))
                    stack.enter_context(mock.patch.object(subprocess, 'check_output', side_effect=AssertionError('subprocess reached')))
                    with self.assertRaisesRegex(RuntimeError, 'archive-only'):
                        getattr(module, name)(*(['unused_fixture'] if name == 'run_json' else []))

    def test_cli_refuses_before_package_dependencies_from_external_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            for relative, _entries, _helpers in CASES:
                with self.subTest(source=relative):
                    result = subprocess.run([sys.executable, '-B', '-I', '-S', str(HERE / relative)],
                                            cwd=directory, capture_output=True, text=True, timeout=10)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('RuntimeError: archive-only', result.stderr)
                    self.assertNotIn('ImportError', result.stderr)
                    self.assertNotIn('ModuleNotFoundError', result.stderr)
                    self.assertEqual(result.stdout, '')
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_read_only_hash_helpers_preserve_private_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / 'input.txt'
            fixture.write_bytes(b'private read-only helper fixture')
            expected = hashlib.sha256(fixture.read_bytes()).hexdigest()
            for relative, _entries, helpers in CASES:
                module = importlib.import_module('studies.mfp_gaussian_calculus.' + relative[:-3].replace('/', '.'))
                helper = 'sha256' if 'sha256' in helpers else 'digest'
                with self.subTest(source=relative):
                    self.assertEqual(getattr(module, helper)(fixture), expected)
                    self.assertEqual(hashlib.sha256(fixture.read_bytes()).hexdigest(), expected)

    def test_every_replay_callable_begins_with_archival_refusal(self):
        for relative, entries, _helpers in CASES:
            tree = ast.parse((HERE / relative).read_text())
            functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
            for name in entries:
                with self.subTest(source=relative, entry=name):
                    self.assertIsInstance(functions[name].body[0], ast.Raise)


if __name__ == '__main__':
    unittest.main()
