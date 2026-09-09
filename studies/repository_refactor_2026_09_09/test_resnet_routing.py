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
        for script in (OPERATOR / "protocol/reproduce_full.sh", OPERATOR / "protocol/verify_bundle.sh",
                       LONG / "reproduce.sh"):
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
            # Verification is read-only, resolves both roots, and detects tampering.
            before = (output / "metadata/manifest.json").read_bytes()
            with patch.object(sys, "argv", ["make_manifest", "--output-root", str(output), "--verify"]):
                module.main()
            self.assertEqual((output / "metadata/manifest.json").read_bytes(), before)
            (output / "result.txt").write_text("tampered")
            with self.assertRaisesRegex(ValueError, "Checksum mismatch"):
                module.verify_manifest(output / "metadata/manifest.json")

    def test_operator_wrapper_normalizes_before_any_work(self):
        # Delegate only the exact stdlib path query; record, never dispatch,
        # all 42 test/scientific/analysis invocations.
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            recorder = base / "record-python"
            recorder.write_text("#!" + sys.executable + "\n" + """
import json, os, sys
from pathlib import Path
args = sys.argv[1:]
if args == ['-B', '-c', 'from runtime_paths import OUTPUT_ROOT; print(OUTPUT_ROOT)']:
    os.execv(sys.executable, [sys.executable, *args])
with Path(os.environ['ROUTING_RECORD']).open('a') as stream:
    stream.write(json.dumps({'args': args, 'output': os.environ.get('PDE_OPERATOR_OUTPUT_ROOT'),
                            'input': os.environ.get('PDE_OPERATOR_INPUT_ROOT')}) + '\\n')
""")
            recorder.chmod(0o700)
            selections = ("~/pde-routing-never-created", str(base / "out with spaces"),
                          str(REPO / "studies"))
            for index, selection in enumerate(selections):
                log = base / f"calls-{index}.jsonl"
                env = dict(os.environ, PYTHON_BIN=str(recorder), ROUTING_RECORD=str(log),
                           PDE_OPERATOR_OUTPUT_ROOT=selection, PYTHONDONTWRITEBYTECODE="1")
                result = subprocess.run(["bash", str(OPERATOR / "protocol/reproduce_full.sh")],
                                        env=env, cwd=base, capture_output=True, text=True)
                if index == 2:
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(log.exists())
                    continue
                self.assertEqual(result.returncode, 0, result.stderr)
                expected = str(Path(selection).expanduser().resolve())
                calls = [json.loads(line) for line in log.read_text().splitlines()]
                self.assertEqual(len(calls), 42)
                for call in calls:
                    self.assertEqual(call["output"], expected)
                    self.assertEqual(call["input"], expected)
                    args = call["args"]
                    if "--restart-from" in args:
                        self.assertTrue(args[args.index("--restart-from") + 1].startswith(expected + "/"))
                    if args[0] == "combine_references.py":
                        paths = args[1:args.index("--output")] + [args[args.index("--output") + 1]]
                        self.assertTrue(all(path.startswith(expected + "/") for path in paths))

    def test_operator_verifier_uses_selected_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.dict(os.environ, {"PDE_OPERATOR_INPUT_ROOT": temp}, clear=True):
                helper = load(OPERATOR / "runtime_paths.py")
            with patch.dict(sys.modules, {"runtime_paths": helper}):
                verifier = load(OPERATOR / "verify_evidence.py")
            self.assertEqual(verifier.RAW, Path(temp) / "results/raw")
            self.assertEqual(verifier.PROCESSED, Path(temp) / "results/processed")
            self.assertEqual(verifier.AGENT_OUTPUTS, Path(temp) / "audits")
            self.assertEqual(verifier.verify_all_npz(), 0)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_operator_shell_missing_evidence_uses_selected_root(self):
        with tempfile.TemporaryDirectory() as temp:
            env = dict(os.environ, PDE_OPERATOR_INPUT_ROOT=temp,
                       PYTHON_BIN=sys.executable, PYTHONDONTWRITEBYTECODE="1")
            result = subprocess.run(["bash", str(OPERATOR / "protocol/verify_bundle.sh"), "evidence"],
                                    env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn(temp, result.stderr)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_reproduction_guides_select_fresh_artifacts(self):
        early = (REPO / "studies/resnet_dense_early_audit/REPRODUCE.md").read_text()
        self.assertNotIn("--out results/", early)
        self.assertNotIn("GALERKIN_OUT=results/", early)
        long = (LONG / "REPRODUCE.md").read_text()
        self.assertNotIn("sha256sum -c metadata/", long)
        self.assertIn("python make_manifest.py --verify", long)
        self.assertIn("../../data/generated/resnet_dense_long_horizon", long)

    def test_long_analysis_explicit_report(self):
        text = (LONG / "run_all.py").read_text()
        self.assertIn('report_path=output_root / "REPORT.md"', text)
        self.assertIn('figures_dir=output_root / "figures"', text)
        self.assertIn('metadata_dir = output_root / "metadata"', text)


if __name__ == "__main__":
    unittest.main()
