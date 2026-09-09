"""Bounded routing/provenance checks, not a compiler or campaign rerun."""

import ast
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[2]
STUDY = REPO / "studies/mfp_quadratic_compiler"


def paths():
    spec = importlib.util.spec_from_file_location("quadratic_routing_fixture", STUDY / "campaign_paths.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RoutingTests(unittest.TestCase):
    def test_default_roles(self):
        with patch.dict(os.environ, {}, clear=True):
            module = paths()
            self.assertEqual(module.OUTPUT_ROOT, REPO / "data/generated/mfp_quadratic_compiler")
            self.assertEqual(module.INPUT_ROOT, REPO / "data/historical/studies/mfp_quadratic_compiler")
            for name in ("campaign2/certificates_order7.json", "campaign3/certificates_order7.json",
                         "campaign4/certificates_order9.json"):
                self.assertTrue(module.certificate_path(name).is_file())

    def test_explicit_roles_no_import_write(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            with patch.dict(os.environ, {"PDE_QUADRATIC_INPUT_ROOT": str(base / "in"),
                                         "PDE_QUADRATIC_OUTPUT_ROOT": str(base / "out")}, clear=True):
                module = paths()
                self.assertEqual(module.certificate_path("campaign2/certificates_order7.json"),
                                 base / "in/campaign2/certificates_order7.json")
            self.assertEqual(list(base.iterdir()), [])

    def test_protected_output(self):
        for suffix in ("studies", "data/historical/run", "data/original_backups/run"):
            with patch.dict(os.environ, {"PDE_QUADRATIC_OUTPUT_ROOT": str(REPO / suffix)}, clear=True):
                with self.assertRaises(ValueError):
                    paths()

    def test_all_historical_sector_labels_resolve(self):
        with patch.dict(os.environ, {}, clear=True):
            module = paths()
            result = json.loads((module.INPUT_ROOT / "campaign4/results_order9.json").read_text())
            self.assertEqual(len(result["sector_manifest"]), 125)
            import hashlib
            for record in result["sector_manifest"]:
                path = module.recorded_sector_path(record["path"])
                self.assertTrue(path.is_file(), str(path))
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record["sha256"])

    def test_retired_campaign_refuses_before_work(self):
        for name in ("run_sectors.py", "make_provenance.py"):
            path = STUDY / "campaign4" / name
            tree = ast.parse(path.read_text())
            main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
            self.assertIsInstance(main.body[0], ast.Raise)
            with tempfile.TemporaryDirectory() as temp:
                result = subprocess.run([sys.executable, "-B", str(path)], cwd=temp,
                                        text=True, capture_output=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Archive-only", result.stderr)
                self.assertEqual(list(Path(temp).iterdir()), [])

    def test_producer_default_bindings(self):
        for campaign, filename in (("campaign2", "certificates_order7.json"),
                                   ("campaign3", "certificates_order7.json"),
                                   ("campaign4", "certificates_order9.json")):
            text = (STUDY / campaign / "postprocess.py").read_text()
            self.assertIn(f'default=OUTPUT_ROOT / "{campaign}/{filename}"', text)
        text = (STUDY / "campaign6_f13_threshold/run_benchmark.py").read_text()
        self.assertIn("cwd=output_dir", text)
        self.assertIn('output = output_dir / f"{ns.name}.benchmark.json"', text)


if __name__ == "__main__":
    unittest.main()
