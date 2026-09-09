"""Bounded routing/provenance checks, not a compiler or campaign rerun."""

import ast
import argparse
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

REPO = Path(__file__).resolve().parents[2]
STUDY = REPO / "studies/mfp_quadratic_compiler"


def paths():
    spec = importlib.util.spec_from_file_location("quadratic_routing_fixture", STUDY / "campaign_paths.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RoutingTests(unittest.TestCase):
    def test_postprocessors_refuse_input_aliases_before_computation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "input.json"
            source.write_text("retained sentinel")
            linked = root / "linked.json"
            linked.symlink_to(source)
            hardlinked = root / "hardlinked.json"
            os.link(source, hardlinked)
            with patch.dict(os.environ, {}, clear=True):
                helper = paths()
            for relative, arguments in (
                ("campaign1/analyze_hankel.py", [str(source)]),
                ("campaign1/parametric_stieltjes_postprocess.py", [str(source)]),
                ("campaign2/postprocess.py", ["--plus", str(source), "--minus", str(source)]),
                ("campaign3/postprocess.py", ["--input", str(source)]),
                ("campaign4/postprocess.py", ["--input", str(source)]),
            ):
                path = STUDY / relative
                tree = ast.parse(path.read_text())
                main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
                compute = Mock(side_effect=AssertionError("computed before guard"))
                namespace = dict(argparse=argparse, Path=Path, INPUT_ROOT=helper.INPUT_ROOT,
                                 OUTPUT_ROOT=helper.OUTPUT_ROOT, require_new_output=helper.require_new_output,
                                 compute=compute, analyze=compute, load_jets=compute)
                exec(compile(ast.Module(body=[main], type_ignores=[]), str(path), "exec"), namespace)
                for output in (source, linked, hardlinked):
                    with patch.object(sys, "argv", [relative, *arguments, "--output", str(output)]):
                        with self.assertRaises(ValueError):
                            namespace["main"]()
                compute.assert_not_called()
            self.assertEqual(source.read_text(), "retained sentinel")

    def test_all_selected_evidence_bindings(self):
        selected = {
            "campaign1/test_order9_q2_order8.py": {"RAW", "COMPACT", "PROVENANCE"},
            "campaign1/test_hankel_analysis.py": {"RAW_PATH", "CERTIFICATE_PATH"},
            "campaign5_b3/postprocess_lower_moments.py": {"DATA", "STAGE_A", "STAGE_B"},
            "campaign5_b3/test_b2_order5_gate.py": {"ACCEPTED_RAW"},
            "campaign5_b3/test_stage_c_sector.py": {"DENSE"},
            "depth3_gaussian_program/depth3_stieltjes_audit.py": {"INPUT"},
            "depth3_gaussian_program/depth3_order13_stieltjes_audit.py": {"INPUT"},
            "depth3_gaussian_program/test_depth3_order13_stieltjes.py": {"RESULT"},
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "missing selected evidence"
            with patch.dict(os.environ, {"PDE_QUADRATIC_INPUT_ROOT": str(root)}, clear=True):
                helper = paths()
                for relative, names in selected.items():
                    path = STUDY / relative
                    tree = ast.parse(path.read_text())
                    bindings = [node for node in tree.body if isinstance(node, ast.Assign)
                                and any(isinstance(target, ast.Name) and target.id in names
                                        for target in node.targets)]
                    namespace = dict(INPUT_ROOT=helper.INPUT_ROOT, certificate_path=helper.certificate_path)
                    exec(compile(ast.Module(body=bindings, type_ignores=[]), str(path), "exec"), namespace)
                    for name in names:
                        self.assertTrue(namespace[name].is_relative_to(root), (relative, name, namespace[name]))
                lower = (STUDY / "campaign5_b3/test_lower_moment_certificate.py").read_text()
                self.assertIn('certificate_path("campaign5_b3/certificates_lower_moments.json")', lower)
            self.assertFalse(root.exists())
        for path in STUDY.rglob("*.py"):
            if path.name != "campaign_paths.py":
                self.assertNotIn("data/historical/studies/mfp_quadratic_compiler/", path.read_text(), str(path))

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

    def test_campaign6_documented_build_routes(self):
        text = (STUDY / "campaign6_f13_threshold/CAMPAIGN_REPORT.md").read_text()
        block = next(block for block in re.findall(r"```bash\n(.*?)```", text, re.S)
                     if "g++" in block)
        result = subprocess.run(["bash", "-n"], input=block, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("from studies.mfp_quadratic_compiler.campaign_paths import OUTPUT_ROOT", block)
        self.assertIn('OUTPUT_ROOT / "campaign6_f13_threshold/build"', block)
        commands = [shlex.split(line) for line in block.replace("\\\n", " ").splitlines()
                    if line.startswith("g++ ")]
        self.assertEqual(len(commands), 2)
        for command, name in zip(commands, ("peeling_lower_bound_checked",
                                            "hybrid_component_interval_checked")):
            self.assertEqual(command[command.index("-o") + 1],
                             "$PDE_QUADRATIC_BUILD_DIR/" + name)
            sources = [arg for arg in command if arg.endswith(".cpp")]
            self.assertEqual(len(sources), 1)
            self.assertTrue((REPO / sources[0]).is_file())
        # Syntax/path inspection only: neither mkdir nor the compiler is run.

    def test_sector_guide_uses_current_sources_and_generated_products(self):
        text = (STUDY / "SECTOR_ENGINE.md").read_text()
        fence = chr(96) * 3
        block = next(block for block in re.findall(fence + r"sh\n(.*?)" + fence, text, re.S)
                     if "g++" in block)
        result = subprocess.run(["bash", "-n"], input=block, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("studies/mean_field_peeling/", block)
        self.assertIn('OUTPUT_ROOT / "sector_engine"', block)
        commands = [shlex.split(line) for line in block.replace("\\\n", " ").splitlines()
                    if line.startswith("g++ ")]
        self.assertEqual(len(commands), 2)
        for command in commands:
            self.assertTrue(command[command.index("-o") + 1].startswith("$PDE_QUADRATIC_SECTOR_DIR/"))
            for source in (arg for arg in command if arg.endswith(".cpp")):
                self.assertTrue((REPO / source).is_file())
        self.assertIn("authorization to repeat", text)

    def test_stdout_only_boundary_diagnostic_rejects_output_before_solves(self):
        path = STUDY / "operator_ide_closure/finite_width_boundary_layer.py"
        tree = ast.parse(path.read_text())
        main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
        seen = []
        def solve(*args, **kwargs):
            seen.append((args, kwargs))
            return SimpleNamespace(event_time=0)
        namespace = dict(argparse=argparse, solve_one=solve, asdict=lambda _: {"fixture": True}, json=json)
        exec(compile(ast.Module(body=[main], type_ignores=[]), str(path), "exec"), namespace)
        with patch.object(sys, "argv", ["diagnostic", "--widths", "32", "--seeds", "1",
                                       "--output", "never-created.json"]):
            with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                namespace["main"]()
            self.assertEqual(error.exception.code, 2)
        self.assertEqual(seen, [])
        with patch.object(sys, "argv", ["diagnostic", "--widths", "32", "--seeds", "1"]):
            output = io.StringIO()
            with redirect_stdout(output):
                namespace["main"]()
        self.assertEqual(len(seen), 3)
        self.assertEqual(json.loads(output.getvalue())["results"], [{"fixture": True}])


if __name__ == "__main__":
    unittest.main()
