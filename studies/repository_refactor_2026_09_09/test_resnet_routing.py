"""Bounded path/metadata checks; never run a training experiment."""

import ast
import hashlib
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
OPERATOR = REPO / "studies/resnet_operator_core"
LONG = REPO / "studies/resnet_dense_long_horizon"


def load(path):
    spec = importlib.util.spec_from_file_location("routing_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RoutingTests(unittest.TestCase):
    def test_operator_default(self):
        with patch.dict(os.environ, {}, clear=True):
            module = load(OPERATOR / "runtime_paths.py")
        self.assertEqual(module.OUTPUT_ROOT, REPO / "data/generated/resnet_operator_core")
        self.assertEqual(module.INPUT_ROOT, module.OUTPUT_ROOT)

    def test_operator_selected_evidence_does_not_write_on_import(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            env = {"PDE_OPERATOR_OUTPUT_ROOT": str(base / "fresh"),
                   "PDE_OPERATOR_INPUT_ROOT": str(base / "evidence")}
            with patch.dict(os.environ, env, clear=True):
                module = load(OPERATOR / "runtime_paths.py")
            self.assertEqual(module.INPUT_ROOT, base / "evidence")
            self.assertEqual(module.OUTPUT_ROOT, base / "fresh")
            self.assertEqual(list(base.iterdir()), [])

    def test_operator_protected_destinations(self):
        for suffix in ("", "studies/resnet_operator_core", "docs", "code", ".git",
                       "data/historical/example", "data/original_backups/example"):
            with self.subTest(suffix=suffix), patch.dict(os.environ, {
                "PDE_OPERATOR_OUTPUT_ROOT": str(REPO / suffix),
            }, clear=True), self.assertRaises(ValueError):
                load(OPERATOR / "runtime_paths.py")

    def test_operator_consumers_and_imports(self):
        # Inspect only routing statements: optional plotting/scientific packages
        # are deliberately not imported by this refactor test.
        text = (OPERATOR / "analyze.py").read_text()
        tree = ast.parse(text)
        self.assertFalse(any(isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
                             and isinstance(node.value.func, ast.Attribute)
                             and node.value.func.attr == "mkdir" for node in tree.body))
        self.assertEqual(text.count('INPUT_PROCESSED / "exact_combined_'), 4)
        for name in ("analyze.py", "reference_noise_update.py", "ordered_limit_update.py"):
            text = (OPERATOR / "audits/statistical_audit" / name).read_text()
            self.assertIn('RAW = INPUT_ROOT / "results" / "raw"', text)
            self.assertIn('OUT = OUTPUT_ROOT / "audits" / "statistical_audit"', text)

    def test_reproduction_paths_and_syntax(self):
        for script in (OPERATOR / "protocol/reproduce_full.sh", LONG / "reproduce.sh"):
            subprocess.run(["bash", "-n", str(script)], check=True)
        text = (OPERATOR / "protocol/reproduce_full.sh").read_text()
        self.assertNotIn("--restart-from results/", text)
        self.assertNotIn("--output results/", text)
        self.assertEqual(text.count('export PDE_OPERATOR_'), 2)
        text = (LONG / "reproduce.sh").read_text()
        self.assertEqual(text.count('--output-root "$run_dir"'), 2)

    def test_long_manifest_roundtrip(self):
        module = load(LONG / "make_manifest.py")
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            source, output = base / "source", base / "output"
            source.mkdir()
            output.mkdir()
            (source / "program.txt").write_text("fixture source")
            (output / "result.txt").write_text("fixture result")
            module.ROOT = source
            with patch.object(sys, "argv", ["make_manifest", "--output-root", str(output)]):
                module.main()
            manifest = json.loads((output / "metadata/manifest.json").read_text())
            self.assertEqual(manifest["schema"], 2)
            self.assertEqual({row["root"] for row in manifest["files"]}, {"source", "run"})
            self.assertEqual(len(manifest["files"]), 2)
            for row in manifest["files"]:
                path = Path(manifest["roots"][row["root"]]) / row["path"]
                self.assertEqual(row["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertFalse((source / "metadata").exists())

    def test_long_analysis_explicit_report(self):
        text = (LONG / "run_all.py").read_text()
        self.assertIn('report_path=output_root / "REPORT.md"', text)
        self.assertIn('figures_dir=output_root / "figures"', text)
        self.assertIn('metadata_dir = output_root / "metadata"', text)


if __name__ == "__main__":
    unittest.main()
