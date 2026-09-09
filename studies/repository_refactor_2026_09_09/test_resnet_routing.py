"""Bounded path/metadata checks; never run a training experiment."""

import ast
import argparse
import csv
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
EARLY = REPO / "studies/resnet_dense_early_audit"


def load(path):
    spec = importlib.util.spec_from_file_location("routing_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def output_interface(path, name, **bindings):
    """Execute a complete boundary with real stdlib guards and mocked science."""
    tree = ast.parse(path.read_text())
    node = next(node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == name)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    namespace = dict(Path=Path, argparse=argparse, csv=csv, json=json, os=os,
                     __file__=str(path), __doc__="private routing fixture",
                     reject_output_links=load(REPO / "studies/_output_paths.py").reject_output_links)
    namespace.update(bindings)
    module = ast.fix_missing_locations(ast.Module(body=[future, node], type_ignores=[]))
    exec(compile(module, str(path), "exec"), namespace)
    return namespace[name]


class OutputBoundaryTests(unittest.TestCase):
    def alias_directory(self, root, kind, child):
        source = root / "consumed-input"
        source.write_bytes(b"retained input sentinel")
        output = root / "generated"
        if kind == "root-symlink":
            real = root / "real-output"
            real.mkdir()
            output.symlink_to(real, target_is_directory=True)
        elif kind == "parent-symlink":
            real = root / "real-output"
            real.mkdir()
            output.symlink_to(real, target_is_directory=True)
            output = output / "child-not-created"
        else:
            output.mkdir()
            target = output / child
            target.parent.mkdir(parents=True, exist_ok=True)
            if kind == "hardlink":
                os.link(source, target)
            else:
                target.symlink_to(source if kind == "symlink" else root / "missing-input")
        return source, output

    def test_operator_directory_boundaries_refuse_all_child_kinds_before_work(self):
        cases = [("analyze.py", key) for key in ("PROCESSED", "FIGURES")]
        cases += [("audits/statistical_audit/" + name, "OUT") for name in (
            "analyze.py", "reference_noise_update.py", "ordered_limit_update.py")]
        cases += [("run_exact_reference.py", "RAW"), ("run_pde.py", "RAW")]
        children = ("inventory.csv", "summary.json", "plot.png", "bootstrap.npz",
                    "nested/future-metadata.json")
        for relative, selected in cases:
            for kind in ("symlink", "hardlink", "dangling", "root-symlink", "parent-symlink"):
                for child in children:
                    with self.subTest(file=relative, root=selected, kind=kind, child=child), \
                         tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        source, output = self.alias_directory(root, kind, child)
                        stop = Mock(side_effect=AssertionError("work dispatched before rejection"))
                        bindings = dict(PROCESSED=root / "processed", FIGURES=root / "figures",
                                        OUT=root / "statistics", RAW=root / "raw", NUM=root / "numerics",
                                        OUTPUT_ROOT=root / "run", load=stop, load_archive=stop,
                                        load_block=stop, load_exact=stop, BLOCK_FILES=["fixture"],
                                        EXACT_FILES={"fixture": None}, np=SimpleNamespace(eye=stop))
                        if selected == "RAW":
                            # The public runner fixes results/raw below OUTPUT_ROOT.
                            bindings["OUTPUT_ROOT"] = output
                            target = output / "results/raw"
                            if kind not in ("root-symlink", "parent-symlink"):
                                target.mkdir(parents=True)
                                (output / child).rename(target / Path(child).name)
                        else:
                            bindings[selected] = output
                        name = "run" if selected == "RAW" else "main"
                        boundary = output_interface(OPERATOR / relative, name, **bindings)
                        with self.assertRaisesRegex(ValueError, "symlink|hardlink"):
                            boundary(SimpleNamespace()) if name == "run" else boundary()
                        stop.assert_not_called()
                        self.assertEqual(source.read_bytes(), b"retained input sentinel")

    def test_operator_analysis_allows_distinct_existing_outputs(self):
        cases = (("analyze.py", "load"),
                 ("audits/statistical_audit/analyze.py", "load_archive"),
                 ("audits/statistical_audit/reference_noise_update.py", "load_block"),
                 ("audits/statistical_audit/ordered_limit_update.py", "load_exact"))
        for relative, reader in cases:
            with self.subTest(file=relative), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                raw = root / "selected/raw"
                raw.mkdir(parents=True)
                (raw / "fixture.npz").write_bytes(b"selected input")
                output = root / "generated"
                output.mkdir()
                prior = output / "summary.json"
                prior.write_text("old distinct report")
                stop = Mock(side_effect=RuntimeError("stop before science"))
                boundary = output_interface(OPERATOR / relative, "main", PROCESSED=output,
                    FIGURES=output, OUT=output, RAW=raw, NUM=root / "selected/numerics",
                    BLOCK_FILES=["fixture.npz"], EXACT_FILES={"fixture": None}, **{reader: stop})
                with self.assertRaisesRegex(RuntimeError, "stop before science"):
                    boundary()
                stop.assert_called_once()
                self.assertEqual(prior.read_text(), "old distinct report")

    def test_early_public_directory_callables_guard_plots_tables_and_intermediates(self):
        names = ("finite_difference_scaling_audit", "iid_depth_self_averaging",
                 "depth_resolution_experiment", "response_snapshot_audit",
                 "truncated_training_experiment", "restart_and_horizon_experiment",
                 "parameter_grid_experiment", "summarize")
        children = ("response_singular_value_decay.png", "summary.json", "truncated_training.csv",
                    "response_singular_values_smooth_generic.npy", "nested/future-output.csv")
        for name in names:
            for kind in ("symlink", "hardlink", "dangling", "root-symlink", "parent-symlink"):
                for child in children:
                    with self.subTest(callable=name, kind=kind, child=child), tempfile.TemporaryDirectory() as tmp:
                        source, output = self.alias_directory(Path(tmp), kind, child)
                        stop = Mock(side_effect=AssertionError("science dispatched before rejection"))
                        boundary = output_interface(EARLY / "run_dense_resnet_audit.py", name,
                                                    make_data=stop, forward_and_adjoint=stop)
                        kwargs = {"out_dir": output}
                        if name == "response_snapshot_audit":
                            kwargs.update(state=None, X=None, y=None, orders=(), tag="fixture")
                        if name == "summarize":
                            kwargs["payload"] = {"fixture": True}
                        with self.assertRaisesRegex(ValueError, "symlink|hardlink"):
                            boundary(**kwargs)
                        stop.assert_not_called()
                        self.assertEqual(source.read_bytes(), b"retained input sentinel")

    def test_early_cli_preserves_unresolved_aliases_until_guard(self):
        for filename in ("run_dense_resnet_audit.py", "run_response_galerkin_projection.py"):
            for kind in ("symlink", "hardlink", "dangling", "root-symlink", "parent-symlink"):
                with self.subTest(file=filename, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    source, output = self.alias_directory(Path(tmp), kind, "nested/plot.png")
                    stop = Mock(side_effect=AssertionError("science dispatched before rejection"))
                    main = output_interface(EARLY / filename, "main", make_data=stop,
                                            finite_difference_scaling_audit=stop)
                    argv = [filename] if "projection" in filename else [filename, "--out", str(output)]
                    with patch.object(sys, "argv", argv), patch.dict(os.environ, {"GALERKIN_OUT": str(output)}):
                        with self.assertRaisesRegex(ValueError, "symlink|hardlink"):
                            main()
                    stop.assert_not_called()
                    self.assertEqual(source.read_bytes(), b"retained input sentinel")

    def test_early_boundaries_allow_distinct_refresh_and_fresh_cli_roots(self):
        names = ("finite_difference_scaling_audit", "iid_depth_self_averaging",
                 "depth_resolution_experiment", "response_snapshot_audit",
                 "truncated_training_experiment", "restart_and_horizon_experiment",
                 "parameter_grid_experiment")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "generated"
            output.mkdir()
            prior = output / "response_singular_value_decay.png"
            prior.write_bytes(b"previous ordinary plot")
            for name in names:
                with self.subTest(callable=name):
                    stop = Mock(side_effect=RuntimeError("stop before science"))
                    boundary = output_interface(EARLY / "run_dense_resnet_audit.py", name,
                                                make_data=stop, forward_and_adjoint=stop)
                    kwargs = {"out_dir": output}
                    if name == "response_snapshot_audit":
                        kwargs.update(state=None, X=None, y=None, orders=(), tag="fixture")
                    with self.assertRaisesRegex(RuntimeError, "stop before science"):
                        boundary(**kwargs)
                    stop.assert_called_once()
                    self.assertEqual(prior.read_bytes(), b"previous ordinary plot")
            for filename in ("run_dense_resnet_audit.py", "run_response_galerkin_projection.py"):
                with self.subTest(cli=filename):
                    fresh = root / filename / "not-created-yet"
                    stop = Mock(side_effect=RuntimeError("stop before science"))
                    main = output_interface(EARLY / filename, "main", make_data=stop,
                                            finite_difference_scaling_audit=stop)
                    argv = [filename] if "projection" in filename else [filename, "--out", str(fresh)]
                    with patch.object(sys, "argv", argv), patch.dict(os.environ, {"GALERKIN_OUT": str(fresh)}):
                        with self.assertRaisesRegex(RuntimeError, "stop before science"):
                            main()
                    stop.assert_called_once()
                    self.assertEqual(list(fresh.iterdir()), [])

    def test_reference_refresh_and_pde_preflight_accept_unlinked_output_tree(self):
        for filename in ("run_exact_reference.py", "run_pde.py"):
            with self.subTest(file=filename), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                raw = root / "results/raw"
                raw.mkdir(parents=True)
                prior = raw / "exact_ensemble_n1_L1_S1_seed1_dt1_T1.npz"
                prior.write_bytes(b"previous ordinary reference")
                stop = Mock(side_effect=RuntimeError("stop before science"))
                boundary = output_interface(OPERATOR / filename, "run", OUTPUT_ROOT=root,
                    np=SimpleNamespace(eye=stop), _one_seed=stop,
                    time=SimpleNamespace(perf_counter=lambda: 0))
                args = SimpleNamespace(n=1, depth=1, seed_start=1, seeds=1, duration=1,
                                       dt=1, sample_dt=1, sigma_w=1, workers=1)
                with self.assertRaisesRegex(RuntimeError, "stop before science"):
                    boundary(args)
                stop.assert_called_once()
                self.assertEqual(prior.read_bytes(), b"previous ordinary reference")

    def test_standalone_writers_reject_aliases_and_refresh_distinct_outputs(self):
        cases = [(OPERATOR / "audits/statistical_audit" / name, "write_csv") for name in (
            "analyze.py", "reference_noise_update.py", "ordered_limit_update.py")]
        cases += [(EARLY / "run_dense_resnet_audit.py", "write_csv"),
                  (EARLY / "run_response_galerkin_projection.py", "write_rows")]
        for path, name in cases:
            for kind in ("symlink", "hardlink", "dangling", "root-symlink", "parent-symlink"):
                with self.subTest(file=path, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    source, directory = self.alias_directory(Path(tmp), kind, "table.csv")
                    writer = output_interface(path, name)
                    with self.assertRaisesRegex(ValueError, "symlink|hardlink"):
                        writer(directory / "table.csv", [{"fixture": "new"}])
                    self.assertEqual(source.read_bytes(), b"retained input sentinel")
            with self.subTest(file=path, kind="distinct-refresh"), tempfile.TemporaryDirectory() as tmp:
                output = Path(tmp) / "table.csv"
                output.write_text("old distinct output")
                output_interface(path, name)(output, [{"fixture": "new"}])
                self.assertEqual(output.read_text(), "fixture\nnew\n")
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            (output / "summary.json").write_text("old distinct output")
            output_interface(EARLY / "run_dense_resnet_audit.py", "summarize")(output, {"fixture": True})
            self.assertEqual(json.loads((output / "summary.json").read_text()), {"fixture": True})

    def test_operator_root_and_explicit_variance_destination_reject_links(self):
        for kind in ("symlink", "hardlink", "dangling", "root-symlink", "parent-symlink"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                source, output = self.alias_directory(Path(tmp), kind, "variance.csv")
                with patch.dict(os.environ, {"PDE_OPERATOR_OUTPUT_ROOT": str(output)}):
                    with self.assertRaisesRegex(ValueError, "symlink|hardlink"):
                        load(OPERATOR / "runtime_paths.py")
                main = output_interface(OPERATOR / "audits/numerics/paired_w_variance.py", "main",
                                        OUTPUT_ROOT=Path(tmp) / "unused")
                with patch.object(sys, "argv", ["variance", "--output", str(output / "variance.csv")]):
                    with self.assertRaisesRegex(ValueError, "symlink|hardlink"):
                        main()
                self.assertEqual(source.read_bytes(), b"retained input sentinel")


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
                                     reject_output_links=helper.reject_output_links,
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
