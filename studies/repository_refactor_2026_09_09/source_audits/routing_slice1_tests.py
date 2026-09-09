"""Tiny routing/guard fixtures only: no study campaigns or scientific imports.

Functions are compiled from their actual AST with computation boundaries
stubbed out. Only the routing helper and NumPy for two tiny checkpoint fixtures
are imported normally. All writes are inside TemporaryDirectory under /tmp.
"""
from __future__ import annotations

import argparse
import ast
from contextlib import redirect_stdout
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path("/home/amir/Codes/PDE")
sys.path.insert(0, str(ROOT))
from studies._output_paths import StudyPaths

GAUSS = "studies/mfp_gaussian_calculus/"


class Boundary(Exception):
    pass


def source_functions(relative, *names, **extra):
    path = ROOT / relative
    tree = ast.parse(path.read_text(), filename=str(path))
    nodes = [ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)]
    nodes += [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    assert len(nodes) == 1 + len(names), (relative, names)
    scope = dict(__file__=str(path), __name__="routing_fixture", Path=Path, PATHS=StudyPaths(path),
                 argparse=argparse, sys=sys, json=json, csv=csv, time=time,
                 HERE=path.parent, hashlib=hashlib, sha256=lambda p: hashlib.sha256(p.read_bytes()).hexdigest())
    scope.update(extra)
    exec(compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])), str(path), "exec"), scope)
    return scope


def cli_main(scope, arguments):
    with patch.object(sys, "argv", [scope["__file__"], *map(str, arguments)]), redirect_stdout(io.StringIO()):
        return scope["main"]()


class RoutingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pde-routing-test-", dir="/tmp")
        self.addCleanup(self.temporary.cleanup)
        self.tmp = Path(self.temporary.name)

    def test_changed_sources_parse_and_compile(self):
        matches = subprocess.check_output([
            "rg", "-l", "studies\\._output_paths|from \\.map_inputs|from map_inputs|IDENTITY_SEARCH_INPUT_DIR|archive-only (artifact/seal writer|depth-map freeze|reduced-recurrence freeze)",
            "studies", "-g", "*.py"], cwd=ROOT, text=True).splitlines()
        self.assertGreaterEqual(len(matches), 45)
        for relative in matches:
            with self.subTest(file=relative):
                compile((ROOT / relative).read_text(), str(ROOT / relative), "exec")
                paths = StudyPaths(ROOT / relative)
                self.assertEqual(paths.parse([]).output_dir, paths.generated / paths.relative)

    def test_defaults_and_explicit_historical_inputs(self):
        paths = StudyPaths(ROOT / GAUSS / "depth_order5/audit/run_normalized_sine_experiment.py")
        fresh = paths.parse([], inputs=True, input_relative="depth_order5")
        old = paths.parse(["--historical-inputs"], inputs=True, input_relative="depth_order5")
        self.assertEqual(fresh.input_dir, paths.generated / "depth_order5")
        self.assertEqual(old.input_dir, paths.historical / "depth_order5")
        self.assertEqual(fresh.output_dir, old.output_dir)
        self.assertEqual(fresh.output_dir, paths.generated / "depth_order5/audit")
        selected = paths.parse(["--input-dir", str(self.tmp / "in"), "--output-dir", str(self.tmp / "out")], inputs=True)
        self.assertEqual(selected.input_dir, self.tmp / "in")
        self.assertEqual(selected.output_dir, self.tmp / "out")
        self.assertFalse(selected.output_dir.exists())

    def test_output_rejects_source_history_other_study_and_symlinks(self):
        paths = StudyPaths(ROOT / "studies/d3_arctan_closure_program/analyze_gpu_gauge_block_gradient.py")
        for destination in (ROOT / "studies/x", ROOT / "docs/x", ROOT / "data/historical/x", ROOT / "data/generated/other"):
            with self.subTest(destination=destination), self.assertRaises(ValueError):
                paths.require_output(destination)
        link = self.tmp / "redirect"
        link.symlink_to(paths.historical, target_is_directory=True)
        with self.assertRaises(ValueError):
            paths.require_output(link)
        out = self.tmp / "out"
        out.mkdir()
        (out / "summary.json").symlink_to(paths.historical / "summary.json")
        with self.assertRaises(ValueError):
            paths.require_output(out)

    def test_causal_actual_writer_with_stubbed_trial(self):
        sequence = SimpleNamespace(spawn=lambda n: [None] * n)
        fake_np = SimpleNamespace(random=SimpleNamespace(SeedSequence=lambda seed: sequence, default_rng=lambda seed: None))
        scope = source_functions("studies/causal_flow_peeling_calculus/experiments/adaptive_query_probe.py", "main",
            np=fake_np, WIDTHS=(1,), REPLICATES={1: 1}, BASE_SEED=1, HUTCHINSON_PROBES=1,
            one_trial=lambda *args: {"n": 1, "fixture": 2}, summarize=lambda rows: {"fixture_count": len(rows)})
        out = self.tmp / "causal"
        cli_main(scope, ["--output-dir", out])
        self.assertTrue((out / "raw.csv").is_file())
        self.assertEqual(json.loads((out / "summary.json").read_text())["summary"], {"fixture_count": 1})

    def test_d3_analyzer_input_boundary(self):
        studies = [
            ("analyze_gpu_gauge_block_gradient.py", "gpu_gauge_gradient_results"),
            ("analyze_gpu_high_moment_tail.py", "gpu_tail_results"),
            ("analyze_gpu_weighted_offcolumn_response.py", "gpu_weighted_response_results"),
        ]
        for filename, suffix in studies:
            seen = []
            def load(path):
                seen.append(path)
                raise Boundary()
            scope = source_functions("studies/d3_arctan_closure_program/" + filename, "main", load=load,
                WIDTHS=(1,), BOOTSTRAP_SEED=1, np=SimpleNamespace(random=SimpleNamespace(default_rng=lambda n: None)))
            with self.subTest(file=filename), self.assertRaises(Boundary):
                cli_main(scope, ["--historical-inputs", "--output-dir", self.tmp / filename])
            self.assertEqual(seen[0].parent, scope["PATHS"].historical / suffix)

    def test_activation_output_guard_precedes_computation(self):
        for filename in ("run_pde.py", "run_exact_reference.py"):
            scope = source_functions("studies/resnet_activation_controls/source/" + filename, "run")
            with self.subTest(file=filename), self.assertRaises(ValueError):
                scope["run"](SimpleNamespace(output_dir=ROOT / "data/historical/forbidden"))

    def test_identity_hankel_io_with_stubbed_audit(self):
        relative = "studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search/audit_hankel40.py"
        inputs = self.tmp / "inputs"
        inputs.mkdir()
        (inputs / "RESULTS.json").write_text(json.dumps({"moments": ["1"] * 40}))
        scope = source_functions(relative, "main", Q=int, sha256=lambda p: "fixture",
            audit_family=lambda m, s: {"all_positive_definite": True, "leading_determinant_signs": ["positive"], "leading_determinants": ["1"]})
        output = self.tmp / "output"
        cli_main(scope, ["--input-dir", inputs, "--output-dir", output])
        self.assertTrue((output / "HANKEL40_RESULTS.json").is_file())
        self.assertEqual(json.loads((inputs / "RESULTS.json").read_text())["moments"], ["1"] * 40)

    def test_linear_map_input_fixture_and_no_import_time_payload(self):
        scope = source_functions("studies/mfp_linear_growth_uniform_counterexample/map_inputs.py", "parse_map_path", "load_map",
                                 NAME="FULL_L2_PAIRED_ORDER5_MAP.json")
        path = self.tmp / "map.json"
        path.write_text('{"paired_map": []}')
        self.assertEqual(scope["load_map"](scope["parse_map_path"](["--map-path", str(path)])), {"paired_map": []})
        self.assertEqual(scope["parse_map_path"](["--historical-inputs"]), scope["PATHS"].historical / scope["NAME"])
        for file in ("audit_paired_excess.py", "audit_old_new_transition_subsets.py", "audit_full_l2_paired_transition.py", "bump_full_newton_certificate.py"):
            tree = ast.parse((ROOT / "studies/mfp_linear_growth_uniform_counterexample" / file).read_text())
            for node in tree.body:
                if isinstance(node, ast.Assign):
                    self.assertFalse(any(isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) and call.func.attr == "read_text" for call in ast.walk(node)))

    def test_gaussian_checkpoint_resume_only_selected_output(self):
        import numpy as np
        first = source_functions(GAUSS + "depth_order5/audit/run_normalized_sine_experiment.py", "collect_cell", np=np,
            one_jet=lambda *a: (_ for _ in ()).throw(AssertionError("no simulation")), seed_for=lambda *a: 0)
        out = self.tmp / "depth"
        out.mkdir()
        expected = np.asarray([[1., 2., 3.]])
        np.save(out / "normalized_sine_H3_n1.npy", expected)
        np.testing.assert_array_equal(first["collect_cell"](3, 1, 1, 0, output_dir=out), expected)
        second = source_functions(GAUSS + "depth_order5_observables/independent/run_sine_experiment.py", "collect", np=np,
            one_observation=lambda *a: (_ for _ in ()).throw(AssertionError("no simulation")), seed_for=lambda *a: 0)
        np.save(out / "gamma04_H2_n1.npy", np.asarray([4.]))
        np.testing.assert_array_equal(second["collect"](1, 1, 0, output_dir=out), [4.])
        for scope, function, args in ((first, "collect_cell", (3, 1, 1, 0)), (second, "collect", (1, 1, 0))):
            with self.assertRaises(ValueError):
                scope[function](*args, output_dir=scope["PATHS"].historical)

    def test_archive_guards_before_any_computation(self):
        cases = [
            ("depth_order5/independent/freeze_depth_maps.py", "main", ()),
            ("depth_order5/independent/freeze_depth_maps.py", "exact_write", (self.tmp / "seal", {})),
            ("depth_order5_scalar/multi_observable/independent_route_a/reduce_gamma04.py", "emit", ()),
            ("depth_order5/primary/generate_frozen_artifacts.py", "main", ()),
            ("order5/compiler/generate_artifacts.py", "main", ()),
        ]
        for filename, function, args in cases:
            scope = source_functions(GAUSS + filename, function)
            with self.subTest(file=filename), self.assertRaisesRegex(RuntimeError, "archive-only"):
                scope[function](*args)
        self.assertEqual(list(self.tmp.iterdir()), [])

    def test_frozen_comparison_resolves_data_and_preserved_formula_source(self):
        scope = source_functions(GAUSS + "depth_order5/audit/compare_frozen.py", "_artifact_path")
        source = self.tmp / "source"
        data = self.tmp / "data"
        self.assertEqual(scope["_artifact_path"](source, data, "H3_UNIT_COEFFICIENTS.json"), data / "H3_UNIT_COEFFICIENTS.json")
        self.assertEqual(scope["_artifact_path"](source, data, "H3_UNIT_ABC.cse.txt"), source / "H3_UNIT_ABC.cse.txt")

    def test_loewner_legacy_cli_rejects_historical_output(self):
        scope = source_functions("studies/stieltjes_direct_loewner/simulate_loewner.py", "main",
                                 parse_args=lambda: SimpleNamespace(output=ROOT / "data/historical/reject"))
        with self.assertRaises(ValueError):
            scope["main"]()
        scope = source_functions("studies/stieltjes_direct_loewner/diagnose_blowup.py", "main")
        with self.assertRaises(ValueError):
            cli_main(scope, ["--output", ROOT / "data/historical/reject"])

    def test_proxy_guard_before_configuration_or_device_work(self):
        scope = source_functions("studies/stieltjes_proxy_campaign/reference/run_reference.py", "main",
                                 parse_args=lambda: SimpleNamespace(output_root=ROOT / "data/historical/reject"))
        with self.assertRaises(ValueError):
            scope["main"]()

    def test_proxy_shard_parser_and_merge_input_boundary(self):
        scope = source_functions("studies/stieltjes_proxy_campaign/reference/side_checks/gd_n16384_eight_pair_shard.py", "parse_args")
        with patch.object(sys, "argv", ["shard", "--shard", "0", "--device", "cuda:0", "--output-dir", str(self.tmp / "out")]):
            self.assertEqual(scope["parse_args"]().output_dir, self.tmp / "out")
        scope = source_functions("studies/stieltjes_proxy_campaign/reference/side_checks/merge_gd_n16384_eight_pair.py", "main")
        seen = []
        def read(path, *args, **kwargs):
            seen.append(path)
            raise Boundary()
        with patch.object(Path, "read_text", read), self.assertRaises(Boundary):
            cli_main(scope, ["--input-dir", self.tmp / "in", "--output-dir", self.tmp / "out"])
        self.assertEqual(seen[0], self.tmp / "in/gd-n16384-eight-pair-shard0.json")

    def test_real_help_entrypoints_from_external_working_directory(self):
        # These inspected entrypoints parse before any numerical work and use
        # dependencies already installed. --help terminates before mkdir/writes.
        scripts = [
            "studies/causal_flow_peeling_calculus/experiments/adaptive_query_probe.py",
            "studies/causal_flow_peeling_calculus/experiments/hermite_tail_probe.py",
            "studies/causal_flow_peeling_calculus/experiments/koopman_taylor_probe.py",
            "studies/causal_flow_peeling_calculus/experiments/l1_koopman_obstruction.py",
            "studies/d3_arctan_closure_program/analyze_gpu_gauge_block_gradient.py",
            "studies/d3_arctan_closure_program/analyze_gpu_high_moment_tail.py",
            "studies/d3_arctan_closure_program/analyze_gpu_weighted_offcolumn_response.py",
            GAUSS + "depth_order5/common/sine_prediction.py",
            GAUSS + "depth_order5/audit/compare_frozen.py",
            GAUSS + "depth_order5_scalar/multi_observable/independent_route_a/f7_tree_roadmap.py",
            "studies/stieltjes_proxy_campaign/reference/side_checks/merge_gd_n16384_eight_pair.py",
        ]
        for script in scripts:
            with self.subTest(file=script):
                result = subprocess.run([sys.executable, "-B", str(ROOT / script), "--help"], cwd=self.tmp,
                                        text=True, capture_output=True, timeout=20)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("--output-dir", result.stdout)
        self.assertEqual(list(self.tmp.iterdir()), [])


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(RoutingTests)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    report = stream.getvalue()
    (Path(__file__).parent / "TEST_RESULTS.txt").write_text(report)
    print(report)
    raise SystemExit(not result.wasSuccessful())
