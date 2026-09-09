"""Synthetic routing/integrity fixtures; no symbolic compilation or campaigns."""
from __future__ import annotations

import argparse
import ast
from collections import defaultdict
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path("/home/amir/Codes/PDE")
PRIVATE = Path(__file__).resolve().parent
GAUSSIAN = ROOT / "studies/mfp_gaussian_calculus"
SCALAR = GAUSSIAN / "depth_order5_scalar/primary/audit_full_scalar_recurrence.py"
sys.path.insert(0, str(ROOT))
from studies._output_paths import StudyPaths, REPO_ROOT


def scalar_functions():
    """Use actual function bodies and actual frozen-reference constants."""
    names = {"sha256", "selected_input_root", "input_label", "selected_reference", "load_selected_reference",
             "companion_controls", "nonpolynomial_regression", "run_audit", "main"}
    tree = ast.parse(SCALAR.read_text())
    before = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    nodes = [before] + [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    ns = dict(__file__=str(SCALAR), Path=Path, PATHS=StudyPaths(SCALAR), ROOT=GAUSSIAN,
              json=json, hashlib=hashlib, argparse=argparse)
    reference_source = GAUSSIAN / "depth_order5_scalar/audit/reference_maps.py"
    reference_tree = ast.parse(reference_source.read_text())
    ref_nodes = [before] + [node for node in reference_tree.body
                           if (isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id in {"REFERENCE", "EXPECTED_COUNTS"} for target in node.targets))
                           or (isinstance(node, ast.FunctionDef) and node.name in {"_fraction", "canonical_polynomial"})]
    ref_ns = dict(ROOT=GAUSSIAN, Fraction=Fraction, defaultdict=defaultdict)
    exec(compile(ast.fix_missing_locations(ast.Module(body=ref_nodes, type_ignores=[])), str(reference_source), "exec"), ref_ns)
    ns.update({name: ref_ns[name] for name in ("REFERENCE", "EXPECTED_COUNTS", "canonical_polynomial")})
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "EXPECTED_FREEZE_HASH" for target in node.targets):
            ns["EXPECTED_FREEZE_HASH"] = ast.literal_eval(node.value)
    ns["CANDIDATE_FREEZE"] = SCALAR.parent / "FULL_SCALAR_CANDIDATE_FREEZE.json"
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])), str(SCALAR), "exec"), ns)
    return ns


class SharedConsumerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pde-shared-test-", dir="/tmp")
        self.addCleanup(self.temporary.cleanup)
        self.tmp = Path(self.temporary.name)
        self.ns = scalar_functions()

    def test_archive_refusal_before_imports_for_import_and_direct_execution(self):
        for relative in ("depth_order5/audit/run_checks.py", "depth_order5/primary/run_lightweight_checks.py"):
            source = (GAUSSIAN / relative).read_text()
            tree = ast.parse(source)
            self.assertIsInstance(tree.body[1], ast.Raise)
            compiled = compile(source, str(GAUSSIAN / relative), "exec")
            for name in ("__main__", "imported_archive"):
                with self.subTest(file=relative, mode=name), patch("builtins.__import__", side_effect=AssertionError("imports forbidden")):
                    with self.assertRaisesRegex(RuntimeError, "archive-only"):
                        exec(compiled, {"__name__": name})

    def test_stable_helper_move_is_exact_except_repository_anchor(self):
        before = json.loads((PRIVATE / "BEFORE.json").read_text())
        old = "studies/repository_refactor_2026_09_09/output_paths.py"
        expected = before["targets"][old]["source"].replace("REPO_ROOT = Path(__file__).resolve().parents[2]", "REPO_ROOT = Path(__file__).resolve().parents[1]")
        self.assertEqual((ROOT / "studies/_output_paths.py").read_text(), expected)
        self.assertFalse((ROOT / old).exists())
        self.assertEqual(REPO_ROOT, ROOT)

    def test_all_existing_live_import_updates_are_mechanical(self):
        before = json.loads((PRIVATE / "BEFORE.json").read_text())
        for relative in before["importers"]:
            with self.subTest(file=relative):
                expected = before["targets"][relative]["source"].replace(
                    "from studies.repository_refactor_2026_09_09.output_paths import StudyPaths",
                    "from studies._output_paths import StudyPaths")
                self.assertEqual((ROOT / relative).read_text(), expected)
                compile(expected, str(ROOT / relative), "exec")
        result = subprocess.run(["rg", "-n", "from studies.repository_refactor_2026_09_09.output_paths|import studies.repository_refactor_2026_09_09.output_paths", "studies", "-g", "*.py"], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_protected_source_evidence_history_and_seals_unchanged(self):
        before = json.loads((PRIVATE / "BEFORE.json").read_text())
        for name, expected in before["protected"].items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), expected)

    def test_scientific_function_bodies_and_expected_freeze_hash_unchanged(self):
        before = json.loads((PRIVATE / "BEFORE.json").read_text())
        relative = str(SCALAR.relative_to(ROOT))
        old = ast.parse(before["targets"][relative]["source"])
        new = ast.parse(SCALAR.read_text())
        for name in ("candidate_maps", "terminal_alphabet", "exact_controls", "scaled_activation_value"):
            old_function = next(node for node in old.body if isinstance(node, ast.FunctionDef) and node.name == name)
            new_function = next(node for node in new.body if isinstance(node, ast.FunctionDef) and node.name == name)
            self.assertEqual(ast.dump(old_function), ast.dump(new_function))
        self.assertEqual(self.ns["sha256"](self.ns["CANDIDATE_FREEZE"]), self.ns["EXPECTED_FREEZE_HASH"])

    def test_selected_roots_and_label_roundtrip(self):
        fresh = self.ns["selected_input_root"]()
        historical = self.ns["selected_input_root"](historical_inputs=True)
        self.assertEqual(fresh, ROOT / "data/generated/mfp_gaussian_calculus")
        self.assertEqual(historical, ROOT / "data/historical/studies/mfp_gaussian_calculus")
        with self.assertRaises(ValueError):
            self.ns["selected_input_root"](self.tmp, historical_inputs=True)
        for inputs in (fresh, historical, self.tmp):
            roots = {"source": GAUSSIAN, "inputs": inputs}
            for path in (GAUSSIAN / "order5/compiler/MANIFEST.json", inputs / "depth_order5/independent/CONTROL_AUDIT.json"):
                label = self.ns["input_label"](path, inputs)
                kind, suffix = label.split("/", 1)
                self.assertEqual(roots[kind] / suffix, path.resolve())

    def test_explicit_input_control_and_experiment_fixtures(self):
        source = self.tmp / "source"
        inputs = self.tmp / "inputs"
        manifest = source / "order5/compiler/MANIFEST.json"
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({"controls": {"quadratic": {"A": "111", "B": "1685184", "C": "77400633120"}}}))
        controls = inputs / "depth_order5/independent/CONTROL_AUDIT.json"
        controls.parent.mkdir(parents=True)
        controls.write_text(json.dumps({"depths": {
            "3": {"quadratic": {"A": "14175", "B": "139445032896", "C": "4298284752832899360"}},
            "4": {"quadratic": {"A": "138351807", "B": "59385566223611232192", "C": "81427352525619060193821492876576"}}}}))
        self.ns["ROOT"] = source
        got = self.ns["companion_controls"](inputs)
        self.assertEqual(set(got["files"]), {"source/order5/compiler/MANIFEST.json", "inputs/depth_order5/independent/CONTROL_AUDIT.json"})
        experiment = inputs / "depth_order5/audit/NORMALIZED_SINE_EXPERIMENT.json"
        experiment.parent.mkdir(parents=True)
        experiment.write_text(json.dumps({"decision": "pass", "total_networks": 7700, "fits": {}}))
        result = self.ns["nonpolynomial_regression"](inputs)
        self.assertEqual(result["path"], "inputs/depth_order5/audit/NORMALIZED_SINE_EXPERIMENT.json")
        self.assertEqual(result["sha256"], hashlib.sha256(experiment.read_bytes()).hexdigest())

    def test_historical_selection_reads_retained_controls_and_experiment_without_writes(self):
        inputs = self.ns["selected_input_root"](historical_inputs=True)
        controls = self.ns["companion_controls"](inputs, historical_inputs=True)
        self.assertIn("source/depth_order5/independent/CONTROL_AUDIT.json", controls["files"])
        result = self.ns["nonpolynomial_regression"](inputs)
        self.assertEqual(result["decision"], "pass")
        for depth in (2, 3, 4):
            path, expected = self.ns["selected_reference"](depth, inputs)
            # Hash only; do not expand/canonicalize real scientific maps.
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)

    def test_fresh_inputs_do_not_silently_fall_back_to_historical_evidence(self):
        with self.assertRaises(FileNotFoundError):
            self.ns["companion_controls"](self.tmp)
        with self.assertRaises(FileNotFoundError):
            self.ns["nonpolynomial_regression"](self.tmp)

    def test_selected_reference_keeps_digest_schema_and_count_checks(self):
        reference = self.tmp / "reference.json"
        for schema in ("unit_gram", "roots"):
            payload = {schema: {"A": [{"atoms": ["M_020000"], "coefficient": "1"}]}}
            reference.write_text(json.dumps(payload))
            digest = hashlib.sha256(reference.read_bytes()).hexdigest()
            self.ns["selected_reference"] = lambda depth, root: (reference, digest)
            self.ns["EXPECTED_COUNTS"] = {2: {"A": 1}}
            result = self.ns["load_selected_reference"](2, self.tmp)
            self.assertEqual(result, {"A": {("M_020000",): Fraction(1)}})
            self.ns["EXPECTED_COUNTS"] = {2: {"A": 2}}
            with self.assertRaisesRegex(RuntimeError, "count drift"):
                self.ns["load_selected_reference"](2, self.tmp)
        reference.write_text("{}")
        with self.assertRaisesRegex(RuntimeError, "hash drift"):
            self.ns["load_selected_reference"](2, self.tmp)
        digest = hashlib.sha256(reference.read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError, "unrecognized reference schema"):
            self.ns["load_selected_reference"](2, self.tmp)

    def test_cli_routes_selection_without_calling_science(self):
        seen = []
        self.ns["run_audit"] = lambda **kwargs: seen.append(kwargs) or {"fixture": True}
        with patch.object(sys, "argv", ["audit", "--input-dir", str(self.tmp)]), redirect_stdout(io.StringIO()):
            self.ns["main"]()
        self.assertEqual(seen[-1], {"input_dir": self.tmp, "historical_inputs": False})
        with patch.object(sys, "argv", ["audit", "--historical-inputs"]), redirect_stdout(io.StringIO()):
            self.ns["main"]()
        self.assertEqual(seen[-1], {"input_dir": None, "historical_inputs": True})

    def test_candidate_seal_refusal_still_precedes_computation(self):
        self.ns["sha256"] = lambda path: "incorrect"
        self.ns["projection_audit"] = lambda: self.fail("projection must not execute")
        with self.assertRaisesRegex(RuntimeError, "candidate freeze hash drift"):
            self.ns["run_audit"](input_dir=self.tmp)

    def test_full_audit_threads_selected_root_with_scientific_boundaries_stubbed(self):
        seen = []
        linear = {2: {"A": "3", "B": "48", "C": "1464"},
                  3: {"A": "4", "B": "160", "C": "13888"},
                  4: {"A": "5", "B": "400", "C": "73240"}}
        recurrence = SimpleNamespace(frozen=SimpleNamespace(straight5=None, gram31=None),
                                     B_m2=None, m2_norm=None, A_m3=None)
        self.ns.update(
            projection_audit=lambda: {},
            companion_controls=lambda root, **kw: seen.append(root) or {"fixture": True},
            nonpolynomial_regression=lambda root: seen.append(root) or {"fixture": True},
            candidate_maps=lambda depth: (recurrence, {}, {name: depth for name in "ABC"}),
            load_selected_reference=lambda depth, root: seen.append(root) or {name: {} for name in "ABC"},
            difference=lambda a, b: {"discrepancy_count": 0},
            terminal_alphabet=lambda roots: {"residual_symbols": [], "bad_atom_arities": [], "derivative_ceiling": 5},
            exact_controls=lambda maps: {"constant_1": {"A": "1", "B": "0", "C": "0"}, "linear": linear[maps["A"]]},
            expand_coefficient_map=lambda expression: {},
        )
        result = self.ns["run_audit"](input_dir=self.tmp)
        self.assertEqual(seen, [self.tmp] * 5)
        self.assertEqual(result["input_roots"], {"source": str(GAUSSIAN), "inputs": str(self.tmp)})
        self.assertEqual(result["input_mode"], "explicit")
        for depth, record in result["depths"].items():
            kind, suffix = record["reference"]["path"].split("/", 1)
            self.assertEqual(kind, "inputs")
            selected, digest = self.ns["selected_reference"](int(depth), self.tmp)
            self.assertEqual(self.tmp / suffix, selected)
            self.assertEqual(record["reference"]["sha256"], digest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
