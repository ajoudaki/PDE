"""Read-only retained-map tests plus the existing extension fixtures."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

PRIVATE = Path(__file__).resolve().parent
ROOT = Path("/home/amir/Codes/PDE")
sys.path.insert(0, "/tmp/pde-shared-consumers-ulZD7W")
import test_shared_consumers as previous_tests

FILE = ROOT / "studies/mfp_gaussian_calculus/depth_order5_scalar/audit/reference_maps.py"
spec = importlib.util.spec_from_file_location("bounded_frozen_reference_maps", FILE)
loader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loader)  # Definitions and stdlib only; no producer imports.


class CurrentExtensionTests(previous_tests.SharedConsumerTests):
    def test_protected_source_evidence_history_and_seals_unchanged(self):
        # Only reference_maps.py is newly authorized. Check its unchanged logic
        # separately below; all other prior protected files must stay exact.
        before = json.loads((PRIVATE / "BEFORE.json").read_text())
        for record in before["protected"] + before["unchanged_extension"]:
            with self.subTest(file=record["file"]):
                self.assertEqual(hashlib.sha256((ROOT / record["file"]).read_bytes()).hexdigest(), record["sha256"])


class FrozenReferenceTests(unittest.TestCase):
    def test_retained_paths_reads_hashes_and_existing_counts(self):
        expected_root = ROOT / "data/historical/studies/mfp_gaussian_calculus"
        self.assertEqual(loader.HISTORICAL_ROOT, expected_root)
        original_read = Path.read_bytes
        for depth, (logical_path, expected_hash) in loader.REFERENCE.items():
            with self.subTest(depth=depth):
                path = loader.historical_reference_path(depth)
                self.assertEqual(path, expected_root / logical_path.relative_to(loader.ROOT))
                self.assertTrue(path.is_file())
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected_hash)
                reads = []
                def read(selected):
                    reads.append(selected)
                    return original_read(selected)
                with patch.object(Path, "read_bytes", read):
                    maps = loader.load_reference(depth)
                self.assertEqual(reads, [path])
                self.assertEqual({name: len(poly) for name, poly in maps.items()}, loader.EXPECTED_COUNTS[depth])
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected_hash)

    def test_logical_labels_expected_digests_counts_and_formula_helpers_unchanged(self):
        before = json.loads((PRIVATE / "BEFORE.json").read_text())
        original = ast.parse(before["source"])
        current = ast.parse(FILE.read_text())
        for name in ("REFERENCE", "EXPECTED_COUNTS"):
            def assignment(tree):
                return next(node for node in tree.body if isinstance(node, ast.Assign)
                            and any(isinstance(target, ast.Name) and target.id == name for target in node.targets))
            self.assertEqual(ast.dump(assignment(original)), ast.dump(assignment(current)))
        for name in ("_fraction", "canonical_polynomial", "difference"):
            def function(tree):
                return next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name)
            self.assertEqual(ast.dump(function(original)), ast.dump(function(current)))
        def load_body(tree):
            function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "load_reference")
            start = next(index for index, node in enumerate(function.body)
                         if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "payload" for target in node.targets))
            return [ast.dump(node) for node in function.body[start:]]
        self.assertEqual(load_body(original), load_body(current))

    def test_bad_digest_schema_and_counts_still_refuse(self):
        with tempfile.TemporaryDirectory(prefix="pde-reference-fixture-", dir="/tmp") as directory:
            historical = Path(directory)
            fixture = historical / "tiny.json"
            logical = loader.ROOT / "tiny.json"
            for schema in ("unit_gram", "roots"):
                fixture.write_text(json.dumps({schema: {"A": [{"atoms": [], "coefficient": "1"}]}}))
                digest = hashlib.sha256(fixture.read_bytes()).hexdigest()
                with patch.object(loader, "HISTORICAL_ROOT", historical), patch.dict(loader.REFERENCE, {2: (logical, digest)}), patch.dict(loader.EXPECTED_COUNTS, {2: {"A": 1}}):
                    self.assertEqual(len(loader.load_reference(2)["A"]), 1)
                    with patch.dict(loader.EXPECTED_COUNTS, {2: {"A": 2}}), self.assertRaisesRegex(RuntimeError, "count drift"):
                        loader.load_reference(2)
                    fixture.write_text("{}")
                    with self.assertRaisesRegex(RuntimeError, "hash drift"):
                        loader.load_reference(2)
                    digest = hashlib.sha256(fixture.read_bytes()).hexdigest()
                    with patch.dict(loader.REFERENCE, {2: (logical, digest)}), self.assertRaisesRegex(ValueError, "unrecognized reference schema"):
                        loader.load_reference(2)

    def test_missing_retained_input_has_no_source_or_fresh_fallback(self):
        with tempfile.TemporaryDirectory(prefix="pde-reference-missing-", dir="/tmp") as directory:
            historical = Path(directory)
            with patch.object(loader, "HISTORICAL_ROOT", historical), self.assertRaises(FileNotFoundError):
                loader.load_reference(2)
            self.assertEqual(list(historical.iterdir()), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
