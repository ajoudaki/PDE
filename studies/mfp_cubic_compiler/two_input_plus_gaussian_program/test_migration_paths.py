"""Read-only input binding tests; never compile the cubic programs."""
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).with_name('audit_symbolic_order5.py')
spec = importlib.util.spec_from_file_location('cubic_migration_audit', PATH)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class CubicInputPathsTests(unittest.TestCase):
    def test_three_retained_input_hashes_are_exact(self):
        for key in ('result', 'order3_result', 'one_input_order9_result'):
            with self.subTest(key=key):
                self.assertTrue(audit.FILES[key].is_relative_to(audit.HISTORICAL_CUBIC))
                self.assertEqual(audit.sha256(audit.FILES[key]), audit.EXPECTED_SHA256[key])

    def test_load_document_does_not_require_compilation(self):
        self.assertIn('derivatives', audit.load_document())


if __name__ == '__main__':
    unittest.main()
