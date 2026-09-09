"""Final tiny-suite recheck after archiving source snapshots of old imports.

One lexical rg assertion in the original fixture now matches the fixture's own
archived string literal. Replace only that assertion's method with the same
mechanical importer checks plus an AST check for actual forbidden imports.
The original report/harness/failed repeat are not edited or relabeled.
"""
import ast
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

SOURCE = Path('/tmp/pde-frozen-reference-fix-slZtav/test_connected_reference.py')
spec = importlib.util.spec_from_file_location('recorded_shared_checks', SOURCE)
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class CurrentExtensionTests(checks.CurrentExtensionTests):
    def test_all_existing_live_import_updates_are_mechanical(self):
        before = json.loads((checks.previous_tests.PRIVATE / 'BEFORE.json').read_text())
        old_module = 'studies.repository_refactor_2026_09_09.output_paths'
        for relative in before['importers']:
            expected = before['targets'][relative]['source'].replace(
                'from ' + old_module + ' import StudyPaths',
                'from studies._output_paths import StudyPaths')
            self.assertEqual((checks.ROOT / relative).read_text(), expected)
        found = subprocess.run(['rg', '-l', old_module, 'studies', '-g', '*.py'],
                               cwd=checks.ROOT, capture_output=True, text=True)
        self.assertIn(found.returncode, (0, 1), found.stderr)
        for relative in found.stdout.splitlines():
            tree = ast.parse((checks.ROOT / relative).read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    self.assertFalse((node.module or '').startswith(old_module), relative)
                elif isinstance(node, ast.Import):
                    self.assertFalse(any(a.name.startswith(old_module) for a in node.names), relative)


if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.defaultTestLoader.loadTestsFromTestCase(CurrentExtensionTests),
        unittest.defaultTestLoader.loadTestsFromTestCase(checks.FrozenReferenceTests),
    ])
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
