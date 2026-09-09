"""Bounded path/metadata checks; never run a training experiment."""

import ast
import argparse
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import importlib.util
import json
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from typing import Any, Iterable
from unittest.mock import Mock, patch

import numpy as np

REPO = Path(__file__).resolve().parents[2]
OPERATOR = REPO / "studies/resnet_operator_core"
LONG = REPO / "studies/resnet_dense_long_horizon"


def load(path):
    spec = importlib.util.spec_from_file_location("routing_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class RoutingTests(unittest.TestCase):
    def test_restart_output_aliases_refuse_before_quadrature_or_training(self):
        source_path = OPERATOR / "run_pde.py"
        tree = ast.parse(source_path.read_text())
        nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name in {"_tag", "archive_paths", "run"}]
        helper = load(OPERATOR / "runtime_paths.py")
        for target_kind in ("final", "partial"):
            for alias_kind in ("same", "symlink", "hardlink"):
                with self.subTest(target=target_kind, alias=alias_kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    source = root / "restart.npz"
                    np.savez(source, times=np.array([0.]))
                    before = source.read_bytes()
                    args = SimpleNamespace(quadrature="sobol", M=1, R=1, P=1, N=1, seed=1,
                                           dt=1., duration=1., integrator="rk4", restart_from=source)
                    science = Mock(side_effect=RuntimeError("stop before quadrature"))
                    namespace = dict(argparse=argparse, Path=Path, np=np, OUTPUT_ROOT=root,
                                     require_new_archive=helper.require_new_archive, PDESpec=science)
                    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source_path), "exec"), namespace)
                    final, partial = namespace["archive_paths"](args, 1, 1, 0.)
                    target = final if target_kind == "final" else partial
                    target.parent.mkdir(parents=True)
                    if alias_kind == "same":
                        target.write_bytes(before)
                        args.restart_from = target
                    elif alias_kind == "symlink":
                        target.symlink_to(source)
                    else:
                        os.link(source, target)
                    with self.assertRaises((ValueError, FileExistsError)):
                        namespace["run"](args)
                    science.assert_not_called()
                    self.assertEqual(Path(args.restart_from).read_bytes(), before)
                    self.assertEqual(source.read_bytes(), before)

    def test_long_analysis_guards_every_deliverable_before_reading_traces(self):
        source = LONG / "src/dense_mup/analysis.py"
        tree = ast.parse(source.read_text())
        nodes = [node for node in tree.body if (
            isinstance(node, ast.FunctionDef) and node.name in {
                "_check_input_aliases", "analyze_directory", "_plot_representative"}
        ) or (isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "REPRESENTATIVE_FIGURES"
            for target in node.targets))]
        load_trace = Mock(side_effect=RuntimeError("stop before analysis"))
        namespace = dict(Path=Path, Any=Any, Iterable=Iterable, load_trace=load_trace)
        exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), "exec"), namespace)
        names = [("processed", name) for name in (
            "per_run.csv", "errors_by_horizon.csv", "required_order.csv", "refinement.csv",
            "per_run.json", "aggregate.json", "analysis_manifest.json",
        )] + [("figures", name) for name in (
            *namespace["REPRESENTATIVE_FIGURES"], "order_convergence.png",
        )] + [("report", "report.md")]
        for directory, name in names:
            for kind in ("symlink", "hardlink"):
                with self.subTest(output=name, alias=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    raw = root / "raw"
                    raw.mkdir()
                    trace = raw / "run.npz"
                    trace.write_bytes(b"retained trace")
                    target = root / directory / name
                    target.parent.mkdir(parents=True)
                    if kind == "symlink":
                        target.symlink_to(trace)
                    else:
                        os.link(trace, target)
                    with self.assertRaisesRegex(ValueError, "aliases.*trace"):
                        namespace["analyze_directory"](raw, root / "processed", root / "figures",
                            {}, "run", [{"id": "run"}], root / "report/report.md")
                    if directory == "figures" and name in namespace["REPRESENTATIVE_FIGURES"]:
                        with self.assertRaisesRegex(ValueError, "aliases.*trace"):
                            namespace["_plot_representative"]({"path": str(trace)}, root / "figures")
                    load_trace.assert_not_called()
                    self.assertEqual(trace.read_bytes(), b"retained trace")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            trace = root / "run.npz"
            trace.write_bytes(b"retained trace")
            with self.assertRaisesRegex(ValueError, "aliases.*trace"):
                namespace["analyze_directory"](root, root / "processed", root / "figures",
                                               {}, "run", [{"id": "run"}], trace)
            with self.assertRaisesRegex(RuntimeError, "stop before analysis"):
                namespace["analyze_directory"](root, root / "processed", root / "figures",
                                               {}, "run", [{"id": "run"}], root / "new-report.md")
            self.assertEqual(list(root.iterdir()), [trace])

    def test_galerkin_help_and_unknown_flags_stop_before_work(self):
        path = REPO / "studies/resnet_dense_early_audit/run_response_galerkin_projection.py"
        tree = ast.parse(path.read_text())
        main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "main")
        scientific = Mock(side_effect=AssertionError("scientific work dispatched"))
        namespace = dict(argparse=argparse, __doc__="routing fixture", Path=Path, os=os,
                         __file__=str(path), make_data=scientific)
        exec(compile(ast.Module(body=[main], type_ignores=[]), str(path), "exec"), namespace)
        for arguments, code in ((["--help"], 0), (["--out", "not-created"], 2),
                                (["--unknown"], 2)):
            with patch.object(sys, "argv", ["galerkin", *arguments]):
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as failure:
                        namespace["main"]()
                self.assertEqual(failure.exception.code, code)
        scientific.assert_not_called()

    def test_operator_merge_refuses_aliases_before_load_and_pools_tiny_fixture(self):
        module = load(OPERATOR / "combine_references.py")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "raw.npz"
            source.write_bytes(b"retained sentinel")
            linked = root / "linked.npz"
            hardlinked = root / "hardlinked.npz"
            linked.symlink_to(source)
            os.link(source, hardlinked)
            dangling = root / "dangling.npz"
            dangling.symlink_to(root / "absent")
            output = root / "summary.npz"
            partial = output.with_suffix(".npz.partial")
            partial.write_bytes(b"partial input sentinel")
            with patch.object(module, "load_raw", side_effect=AssertionError("loaded before guard")):
                for inputs, target in (([source], source), ([source], linked),
                                       ([source], hardlinked), ([source], dangling),
                                       ([partial], output)):
                    with patch.object(sys, "argv", ["combine", *map(str, inputs), "--output", str(target)]):
                        with self.assertRaises((ValueError, FileExistsError)):
                            module.main()
            self.assertEqual(source.read_bytes(), b"retained sentinel")
            self.assertEqual(partial.read_bytes(), b"partial input sentinel")
            archives = []
            for index in range(2):
                archive = root / f"tiny-{index}.npz"
                np.savez(archive, times=np.array([0., 1.]), seeds=np.array([2*index, 2*index+1]),
                         f=np.ones((2, 2))*index, grams=np.ones((2, 2, 1, 1))*index,
                         theta=np.ones((2, 2, 1, 1))*index,
                         metadata_json=np.array(json.dumps({"n": 1, "depth": 1})))
                archives.append(archive)
            hashes = [hashlib.sha256(path.read_bytes()).hexdigest() for path in archives]
            pooled = root / "tiny-pooled.npz"
            with patch.object(sys, "argv", ["combine", *map(str, archives), "--output", str(pooled)]):
                with redirect_stdout(io.StringIO()):
                    module.main()
            with np.load(pooled) as data:
                np.testing.assert_array_equal(data["f_mean"], [.5, .5])
                self.assertEqual(data["seeds"].size, 4)
            self.assertEqual(hashes, [hashlib.sha256(path.read_bytes()).hexdigest() for path in archives])

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
