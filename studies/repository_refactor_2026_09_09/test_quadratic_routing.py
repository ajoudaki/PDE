"""Bounded routing/provenance checks, not a compiler or campaign rerun."""

import ast
import argparse
from collections import defaultdict
import copy
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import hashlib
import json
import os
from pathlib import Path
import pickle
import re
import shlex
import subprocess
import sys
import tempfile
import time
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


def interface(relative, names, **namespace):
    """Extract complete interface functions/constants; never import science code."""
    path = STUDY / relative
    tree = ast.parse(path.read_text())
    selected = [node for node in tree.body
                if (isinstance(node, ast.FunctionDef) and node.name in names)
                or (isinstance(node, ast.Assign)
                    and any(isinstance(target, ast.Name) and target.id in names
                            for target in node.targets))]
    namespace.update(__file__=str(path), argparse=argparse, Path=Path, json=json)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    module = ast.fix_missing_locations(ast.Module(body=[future, *selected], type_ignores=[]))
    exec(compile(module, str(path), "exec"), namespace)
    return namespace


def aliases(source):
    """Existing name, symlink, hardlink, and parent-directory alias."""
    symbolic = source.with_name(source.name + ".symlink")
    symbolic.symlink_to(source)
    hard = source.with_name(source.name + ".hardlink")
    os.link(source, hard)
    directory = source.parent / (source.name + ".directory")
    directory.symlink_to(source.parent, target_is_directory=True)
    return source, symbolic, hard, directory / source.name


class RoutingTests(unittest.TestCase):
    def test_distinct_output_preserves_legitimate_updates(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            helper = paths()
            source = root / "input"
            source.write_text("sentinel")
            for output in aliases(source):
                with self.subTest(output=output), self.assertRaises(ValueError):
                    helper.require_distinct_output(output, (source,))
            missing = root / "not-created"
            dangling = root / "dangling"
            dangling.symlink_to(missing)
            with self.assertRaises(ValueError):
                helper.require_distinct_output(dangling, (missing,))
            output = root / "existing-distinct-output"
            output.write_text("old output")
            self.assertEqual(helper.require_distinct_output(output, (source,)), output)
            with self.assertRaises(FileExistsError):
                helper.require_new_output(output, (source,))
            self.assertEqual(source.read_text(), "sentinel")
            self.assertEqual(output.read_text(), "old output")
            self.assertFalse(missing.exists())

    def test_graph_export_rejects_checkpoint_alias_before_run(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            checkpoint = root / "checkpoint"
            checkpoint.write_bytes(b"opaque checkpoint: must not be loaded")
            compute = Mock(side_effect=AssertionError("graph work before guard"))
            ns = interface("exact_graph_wick.py", {"main"}, run=compute,
                           require_distinct_output=paths().require_distinct_output)
            for output in (*aliases(checkpoint), root / "missing"):
                selected = checkpoint if output.exists() else output
                for resume in ([], ["--resume"]):
                    with self.subTest(output=output, resume=resume), patch.object(
                            sys, "argv", ["graph", "--checkpoint", str(selected),
                                          "--output", str(output), *resume]):
                        with self.assertRaises(ValueError):
                            ns["main"]()
            compute.assert_not_called()
            self.assertEqual(checkpoint.read_bytes(), b"opaque checkpoint: must not be loaded")
            self.assertFalse((root / "missing").exists())

    def test_graph_checkpoint_updates_and_modes_remain_available(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            checkpoint, output = root / "checkpoint", root / "export.json"
            checkpoint.write_bytes(pickle.dumps({"order": 0, "poly": {}, "derivatives": [17]}))
            output.write_text("previous separate export")
            cache = SimpleNamespace(cache_info=lambda: SimpleNamespace(_asdict=lambda: {}))
            ns = interface("exact_graph_wick.py", {"main", "run", "save_checkpoint"},
                           require_distinct_output=paths().require_distinct_output,
                           pickle=pickle, hashlib=hashlib, differentiate=Mock(return_value={}),
                           expected_large_n=Mock(return_value=17), canonical_key=cache, wick_leading=cache)
            with patch.object(sys, "argv", ["graph", "--checkpoint", str(checkpoint), "--resume",
                                            "--max-order", "1", "--output", str(output)]), redirect_stdout(io.StringIO()):
                ns["main"]()
            self.assertEqual(pickle.loads(checkpoint.read_bytes())["order"], 1)
            self.assertEqual(json.loads(output.read_text())["derivatives"], ["17", "17"])
            with patch.object(sys, "argv", ["graph", "--checkpoint", str(checkpoint), "--resume",
                                            "--max-order", "2", "--differentiate-only"]), redirect_stdout(io.StringIO()):
                ns["main"]()
            self.assertEqual(pickle.loads(checkpoint.read_bytes())["order"], 2)
            before = checkpoint.read_bytes()
            with patch.object(sys, "argv", ["graph", "--checkpoint", str(checkpoint),
                                            "--evaluate-only"]), redirect_stdout(io.StringIO()):
                ns["main"]()
            self.assertEqual(checkpoint.read_bytes(), before)
            self.assertEqual(ns["differentiate"].call_count, 2)

    def test_graded_aliases_and_frozen_hash_fail_before_sectors(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            lower, binary = root / "lower.json", root / "binary"
            lower.write_text("not the frozen result")
            binary.write_text("never executed")
            compute = Mock(side_effect=AssertionError("sector execution before guard"))
            ns = interface("campaign1/run_graded_campaign.py", {"main", "sha256", "EXPECTED_LOWER_SHA"},
                           hashlib=hashlib, run_order=compute,
                           require_distinct_output=paths().require_distinct_output)
            for source in (lower, binary):
                for output in aliases(source):
                    with self.subTest(source=source, output=output), patch.object(
                            sys, "argv", ["graded", "--binary", str(binary), "--lower-result", str(lower),
                                          "--output", str(output)]):
                        with self.assertRaises(ValueError):
                            ns["main"]()
            with patch.object(sys, "argv", ["graded", "--binary", str(binary), "--lower-result", str(lower),
                                            "--output", str(root / "output.json")]):
                with self.assertRaisesRegex(AssertionError, "differs from frozen result"):
                    ns["main"]()
            compute.assert_not_called()
            self.assertEqual(lower.read_text(), "not the frozen result")
            self.assertEqual(binary.read_text(), "never executed")
            self.assertFalse((root / "output.json").exists())

    def test_graded_distinct_export_with_mocked_sectors(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            lower, output = root / "lower.json", root / "output.json"
            fixture = {"parent_source_sha256": "fixture", "cache": {}, "misses_by_remaining_order": {},
                       "observables": {name: {"jets": [{"lambda_coefficients": ["0"]} for _ in range(8)],
                                              "seconds": 0, "cache_before": {}, "cache_after": {}}
                                       for name in ("f", "q1", "q2")}}
            lower.write_text(json.dumps(fixture))
            before = lower.read_bytes()
            output.write_text("previous distinct output")
            ns = interface("campaign1/run_graded_campaign.py",
                           {"main", "jet_record", "EXPECTED_F9", "EXPECTED_LOWER_SHA", "EXPECTED_PARENT_SHA"},
                           copy=copy, hashlib=hashlib, time=time,
                           require_distinct_output=paths().require_distinct_output)
            # Synthetic transport fixture: no frozen production hash is changed.
            ns["sha256"] = Mock(return_value=ns["EXPECTED_LOWER_SHA"])
            ns["run_order"] = Mock(side_effect=[([ns["EXPECTED_F9"]], []), ([0], [])])
            with patch.object(sys, "argv", ["graded", "--binary", str(root / "unused-binary"),
                                            "--lower-result", str(lower), "--output", str(output)]), redirect_stdout(io.StringIO()):
                ns["main"]()
            self.assertEqual(ns["run_order"].call_count, 2)
            self.assertEqual(lower.read_bytes(), before)
            self.assertTrue(json.loads(output.read_text())["regression_gates_passed"])

    def test_graded_parent_hash_gate_is_unchanged(self):
        child = SimpleNamespace(stdout=json.dumps({"parent_source_sha256": "wrong-parent"}))
        subprocess_mock = Mock(run=Mock(return_value=child), PIPE=subprocess.PIPE)
        ns = interface("campaign1/run_graded_campaign.py", {"run_order", "EXPECTED_PARENT_SHA"},
                       defaultdict=defaultdict, subprocess=subprocess_mock,
                       memory_limiter=Mock(return_value=None), time=time)
        with self.assertRaisesRegex(AssertionError, "unexpected parent source"):
            ns["run_order"](Path("never-executed"), "f", 0, time.monotonic() + 60, 1)
        subprocess_mock.run.assert_called_once()

    def test_campaign5_evidence_and_live_source_roles_with_mocked_documents(self):
        with tempfile.TemporaryDirectory() as temporary:
            data = Path(temporary) / "selected/campaign5_b3"
            here = STUDY / "campaign5_b3"
            digest = lambda path: "fixture:" + str(path)
            connected = lambda raw: {"source_sha256": digest(here / "b3_connected.cpp"),
                                     "raw_output_sha256": digest(data / raw), "peak_rss_kib": 1, "wall_seconds": 1}
            documents = {
                data / "provenance_stage_a.json": {
                    "protocol_sha256": digest(here / "PROTOCOL.md"),
                    "reference": {"source_sha256": digest(here / "b3_reference.py"),
                                  "raw_output_sha256": digest(data / "frozen/stage_a_reference_order3.json"),
                                  "peak_rss_kib": 1, "wall_seconds": 1},
                    "connected": connected("frozen/stage_a_connected_order3.json"),
                    "classification": "Stage A passed", "next_branch": "Stage C remains unauthorized"},
                data / "provenance_stage_b.json": {
                    "protocol_sha256": digest(here / "PROTOCOL.md"),
                    "connected": connected("frozen/stage_b_connected_order5.json"),
                    "validation": {"scale_invariant_I_nonconstant": True,
                                   "I_at_minus_half": "a", "I_at_zero": "b", "I_at_one": "c"},
                    "stage_c_status": "unauthorized"},
                data / "provenance_stage_c_projection.json": {
                    "status": "failed_closed_unauthorized", "authorization_conditions": {"stage_c_authorized": False},
                    "fresh_final_source_pilots": [{"completed_order_seven": False}]},
            }
            for relative, functions in (
                ("test_stage_a_provenance.py", ("test_stage_a_durable_hashes_and_status",
                                                "test_stage_b_durable_hashes_caps_and_novelty")),
                ("test_stage_c_closed.py", ("test_projection_is_terminally_unauthorized",)),
            ):
                ns = interface("campaign5_b3/" + relative, {"HERE", "DATA", *functions},
                               INPUT_ROOT=data.parent, sha256=Mock(side_effect=digest))
                self.assertEqual(ns["HERE"], here)
                self.assertEqual(ns["DATA"], data)
                with patch.object(Path, "read_text", lambda path: json.dumps(documents[path])):
                    for function in functions:
                        ns[function]()
                    if relative == "test_stage_a_provenance.py":
                        documents[data / "provenance_stage_a.json"]["protocol_sha256"] = "old-mismatch"
                        with self.assertRaises(AssertionError):
                            ns[functions[0]]()
                # Missing explicitly selected evidence must not fall back to retained/source data.
                with self.assertRaises(FileNotFoundError):
                    ns[functions[0]]()
            self.assertFalse(data.parent.exists())

    def test_stage_c_remains_closed_before_hashes_or_launch(self):
        forbidden = Mock(side_effect=AssertionError("work after closed authorization"))
        ns = interface("campaign5_b3/run_stage_c.py", {"main", "STAGE_C_AUTHORIZED"},
                       sha256=forbidden, subprocess=Mock(run=forbidden))
        self.assertIs(ns["STAGE_C_AUTHORIZED"], False)
        with self.assertRaisesRegex(SystemExit, "closed unauthorized"):
            ns["main"]()
        forbidden.assert_not_called()

    def test_benchmark_output_must_not_alias_selected_executable(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            folder = root / "campaign6_f13_threshold"
            folder.mkdir()
            executable = folder / "fixture.benchmark.json"
            executable.write_text("never executed")
            launch = Mock(side_effect=AssertionError("launch before alias guard"))
            ns = interface("campaign6_f13_threshold/run_benchmark.py", {"main"}, OUTPUT_ROOT=root,
                           require_distinct_output=paths().require_distinct_output, subprocess=Mock(run=launch))
            for selected in aliases(executable):
                with self.subTest(selected=selected), patch.object(sys, "argv", ["benchmark", "fixture", str(selected)]):
                    with self.assertRaises(ValueError):
                        ns["main"]()
            launch.assert_not_called()
            self.assertEqual(executable.read_text(), "never executed")

    def test_benchmark_distinct_output_with_mocked_child(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            root = Path(temporary)
            executable = root / "binary"
            executable.write_text("mock executable, never run")
            before = executable.read_bytes()
            folder = root / "campaign6_f13_threshold"
            folder.mkdir()
            output = folder / "fixture.benchmark.json"
            output.write_text("previous separate report")
            usage = SimpleNamespace(ru_utime=0, ru_stime=0, ru_maxrss=0)
            child = SimpleNamespace(returncode=0, stdout="fixture", stderr="")
            launch = Mock(return_value=child)
            ns = interface("campaign6_f13_threshold/run_benchmark.py",
                           {"main", "sha256", "MEMORY_BYTES", "CPU_SECONDS", "WALL_SECONDS"},
                           OUTPUT_ROOT=root, require_distinct_output=paths().require_distinct_output,
                           subprocess=SimpleNamespace(run=launch, TimeoutExpired=subprocess.TimeoutExpired),
                           resource=SimpleNamespace(RUSAGE_CHILDREN=0, getrusage=lambda _: usage),
                           time=time, hashlib=hashlib)
            with patch.object(sys, "argv", ["benchmark", "fixture", str(executable)]), redirect_stdout(io.StringIO()):
                ns["main"]()
            launch.assert_called_once()
            self.assertEqual(launch.call_args.kwargs["cwd"], folder)
            self.assertEqual(json.loads(output.read_text())["executable_sha256"], hashlib.sha256(before).hexdigest())
            self.assertEqual(executable.read_bytes(), before)

    def test_repaired_cli_imports_and_help_do_not_create_products(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1",
                           "PDE_QUADRATIC_INPUT_ROOT": str(root / "missing-input"),
                           "PDE_QUADRATIC_OUTPUT_ROOT": str(root / "missing-output")}
            for relative in ("exact_graph_wick.py", "campaign1/run_graded_campaign.py",
                             "campaign6_f13_threshold/run_benchmark.py"):
                result = subprocess.run([sys.executable, "-B", str(STUDY / relative), "--help"],
                                        cwd=root, env=environment, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("usage:", result.stdout)
            # Also exercise the package import branch of the shared graph helper.
            result = subprocess.run([sys.executable, "-B", "-c",
                                     "from studies.mfp_quadratic_compiler import exact_graph_wick"],
                                    cwd=REPO, env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(list(root.iterdir()), [])

    def test_native_checkpoint_identity_guards_source_only(self):
        # Deliberately no C++ compiler or native numerical execution.
        helper = (STUDY / "checkpoint_paths.h").read_text()
        for check in ("weakly_canonical(std::filesystem::absolute(output))",
                      "weakly_canonical(std::filesystem::absolute(input))",
                      "std::filesystem::exists(output)", "std::filesystem::exists(input)",
                      "std::filesystem::equivalent(output, input)",
                      "catch (const std::filesystem::filesystem_error &error)"):
            self.assertIn(check, helper)
        self.assertEqual(helper.count("return false;"), 2)
        self.assertIn("return true;", helper)
        for name in ("sector_parallel_reuse.cpp", "sector_parallel.cpp", "component_parallel.cpp"):
            text = (STUDY / name).read_text()
            main = text[text.index("int main(int argc, char **argv)"):]
            guard = main[main.index("if (!distinct_checkpoint_output" if name == "sector_parallel_reuse.cpp"
                                    else "if (!checkpoint.empty() &&"):main.index("  Tree root;")]
            self.assertIn("return 2;", guard)
            self.assertIn('#include "checkpoint_paths.h"', text)
            if name == "sector_parallel_reuse.cpp":
                self.assertIn("!distinct_checkpoint_output(sparse_checkpoint, source_checkpoint)", guard)
                self.assertIn("!target_prefix.empty() &&", guard)
                self.assertIn("!distinct_checkpoint_output(sparse_checkpoint, target_prefix)", guard)
                self.assertIn("std::ifstream in(sparse_checkpoint);", main)
                self.assertIn("std::ofstream checkpoint_out(sparse_checkpoint, std::ios::app);", main)
            else:
                self.assertIn('!distinct_checkpoint_output(checkpoint + ".tmp", checkpoint)', guard)
                self.assertIn("std::ifstream in(checkpoint);", main)
                self.assertIn("std::filesystem::rename(temporary, checkpoint);", main)
            self.assertLess(main.index(guard), main.index(".visit("))
            self.assertLess(main.index(guard), main.index("std::ifstream"))
            self.assertLess(main.index(guard), main.index("std::ofstream"))

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
            "campaign5_b3/test_stage_a_provenance.py": {"DATA"},
            "campaign5_b3/test_stage_c_closed.py": {"DATA"},
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
