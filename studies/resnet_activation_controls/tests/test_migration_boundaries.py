"""Private bytes and extracted interfaces only; no activation analysis or seals."""
import ast
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies.resnet_activation_controls.output_paths import require_output

ROOT = Path(__file__).resolve().parents[1]


def functions(filename, names, env):
    path = ROOT / filename
    nodes = [n for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), "exec"), env)
    return env


class MigrationBoundaryTests(unittest.TestCase):
    def writers(self):
        base = dict(Path=Path, os=os, json=json, require_output=require_output, IntegrityError=RuntimeError)
        return ((functions("analyze_activation.py", {"_atomic_text"}, dict(base))["_atomic_text"], "fresh"),
                (functions("run_experiment.py", {"_write_once", "_encoded"}, dict(base))["_write_once"], {"fixture": True}))

    def test_intermediate_aliases_and_stale_files_preserve_inputs(self):
        for writer, payload in self.writers():
            for kind in ("ordinary", "hardlink", "symlink", "dangling"):
                with self.subTest(writer=writer.__name__, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    source, output = root / "input", root / "result.json"
                    source.write_bytes(b"private activation input")
                    before = hashlib.sha256(source.read_bytes()).hexdigest()
                    partial = output.with_suffix(".json.partial")
                    if kind == "ordinary":
                        partial.write_bytes(b"stale")
                    elif kind == "hardlink":
                        os.link(source, partial)
                    else:
                        partial.symlink_to(root / "missing" if kind == "dangling" else source)
                    with self.assertRaises((ValueError, FileExistsError, RuntimeError)):
                        writer(output, payload)
                    self.assertFalse(output.exists())
                    after = hashlib.sha256(source.read_bytes()).hexdigest()
                    self.assertEqual(before, after)
                    print("FIXTURE_SHA256", json.dumps(dict(case=f"{writer.__name__}/{kind}", before=before, after=after)))

    def test_named_directory_and_final_aliases_refuse_before_mkdir(self):
        for writer, payload in self.writers():
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / "input"
                source.write_bytes(b"keep")
                output = root / "result"
                output.symlink_to(source)
                alias = root / "alias"
                alias.symlink_to(root, target_is_directory=True)
                for target in (output, alias / "result2", ROOT / "unwritten"):
                    with mock.patch.object(Path, "mkdir") as mkdir, self.assertRaises(ValueError):
                        writer(target, payload)
                    mkdir.assert_not_called()
                self.assertEqual(source.read_bytes(), b"keep")

    def test_regular_writes_and_write_once_idempotence_remain_available(self):
        for writer, payload in self.writers():
            with tempfile.TemporaryDirectory() as tmp:
                output = Path(tmp) / "fresh/result.json"
                writer(output, payload)
                before = output.read_bytes()
                writer(output, payload)
                self.assertEqual(output.read_bytes(), before)
                self.assertFalse(output.with_suffix(".json.partial").exists())

    def test_matching_final_does_not_hide_an_occupied_partial(self):
        writer, payload = self.writers()[1]
        for kind in ("ordinary", "hardlink", "symlink", "dangling"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                output = root / "inert-record.json"
                writer(output, payload)
                before = output.read_bytes()
                retained = root / "retained"
                retained.write_bytes(b"keep")
                partial = output.with_suffix(".json.partial")
                if kind == "ordinary":
                    partial.write_bytes(b"stale")
                elif kind == "hardlink":
                    os.link(retained, partial)
                else:
                    partial.symlink_to(root / "absent" if kind == "dangling" else retained)
                with self.assertRaises((ValueError, RuntimeError)):
                    writer(output, payload)
                self.assertEqual(output.read_bytes(), before)
                self.assertEqual(retained.read_bytes(), b"keep")
                if kind == "ordinary":
                    self.assertEqual(partial.read_bytes(), b"stale")

    def test_analysis_refuses_output_alias_before_loading_inputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            alias = root / "linked"
            alias.symlink_to(root, target_is_directory=True)
            loader = mock.Mock(side_effect=AssertionError("input must not be read"))
            env = functions("analyze_activation.py", {"run_analysis"}, dict(
                Path=Path, require_output=require_output, _json=loader))
            args = mock.Mock(root=root, protocol=root / "p", cases=root / "c",
                             pde_dir=root / "pde", dense_dir=root / "dense", output_dir=alias)
            with self.assertRaises(ValueError):
                env["run_analysis"](args)
            loader.assert_not_called()

    def test_seal_label_consumer_uses_producers_generated_evidence_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            results = root / "generated/results"
            source = results / "pde/input.bin"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"private evidence fixture; no trajectory")
            manifest = root / "inert-input.dat"
            manifest.write_bytes(b"no authorization")
            fields = ("dynamics_sha256", "source_sha256", "source_files", "protocol_sha256",
                      "protocol_files", "execution_sha256", "execution_files", "parent_source_lineage", "inference_roles")
            inputs = dict.fromkeys(fields, "inert")
            env = functions("run_experiment.py", {"_evidence_relative", "_require_seal_common", "_sha256"}, dict(
                Path=Path, os=os, hashlib=hashlib, ROOT=root / "source", RESULTS=results,
                INPUT_MANIFEST_PATH=manifest, __file__=str(ROOT / "run_experiment.py"),
                IntegrityError=RuntimeError, _require_input_manifest=mock.Mock(return_value=inputs)))
            label = env["_evidence_relative"](source)
            self.assertEqual(label, "results/pde/input.bin")
            before = env["_sha256"](source)
            record = dict(inputs, schema_version=1, stage="fixture",
                          input_manifest_sha256=env["_sha256"](manifest),
                          orchestrator_sha256=env["_sha256"](ROOT / "run_experiment.py"),
                          files={label: before})
            env["_require_seal_common"](record, "fixture")
            self.assertEqual(before, env["_sha256"](source))
            self.assertFalse((root / "source/results/pde/input.bin").exists())
            print("FIXTURE_SHA256", json.dumps(dict(case="seal-root", before=before, after=env["_sha256"](source))))


class AnalysisRoutingTests(unittest.TestCase):
    NAMES = (
        "summary.json", "metrics.csv", "figure_time_curves.csv", "figure_gram_depth_curves.csv",
        "figure_activation_evidence.csv", "figure_progress_gram_paths.csv",
        "figure_depth_width_controls.csv", "figure_bootstrap_intervals.csv", "figure_cross_prediction.csv",
    )

    def args(self, root):
        return mock.Mock(root=root, protocol=root / "protocol.json", cases=root / "cases.json",
                         pde_dir=root / "results/pde", dense_dir=root / "results/dense",
                         output_dir=root / "processed")

    def interfaces(self):
        loader = mock.Mock(side_effect=RuntimeError("stop before ingestion"))
        env = functions("analyze_activation.py", {"run_analysis", "_preflight_analysis_outputs"}, dict(
            Path=Path, require_output=require_output, _json=loader,
            __file__=str(ROOT / "analyze_activation.py")))
        return env, loader

    def refused(self, args, error=ValueError):
        env, loader = self.interfaces()
        with mock.patch.object(Path, "mkdir") as mkdir, self.assertRaises(error):
            env["run_analysis"](args)
        loader.assert_not_called()
        mkdir.assert_not_called()

    def test_all_named_finals_and_partials_protect_explicit_protocol_and_cases(self):
        for field in ("protocol", "cases"):
            for name in self.NAMES:
                for suffix in ("", ".partial"):
                    for alias in (False, True):
                        with self.subTest(field=field, name=name, suffix=suffix, alias=alias), \
                             tempfile.TemporaryDirectory() as tmp:
                            args = self.args(Path(tmp))
                            target = args.output_dir / (name + suffix)
                            target.parent.mkdir()
                            target.write_bytes(b"inert selected input")
                            if alias:
                                getattr(args, field).symlink_to(target)
                            else:
                                setattr(args, field, target)
                            self.refused(args)
                            self.assertEqual(target.read_bytes(), b"inert selected input")

    def test_selected_seal_and_archive_paths_protect_all_named_outputs(self):
        for role in ("PDE_STAGE_SEAL.json", "DENSE_STAGE_SEAL.json", "pde/inert.npz", "dense/inert.npz"):
            for name in self.NAMES:
                for suffix in ("", ".partial"):
                    with self.subTest(role=role, name=name, suffix=suffix), \
                         tempfile.TemporaryDirectory() as tmp:
                        args = self.args(Path(tmp))
                        target = args.output_dir / (name + suffix)
                        target.parent.mkdir()
                        target.write_bytes(b"path-only fixture; not an archive or seal")
                        source = args.pde_dir.parent / role
                        source.parent.mkdir(parents=True)
                        source.symlink_to(target)
                        self.refused(args)
                        self.assertEqual(target.read_bytes(), b"path-only fixture; not an archive or seal")

    def test_each_frozen_map_role_protects_finals_and_partials_in_both_seals(self):
        env, loader = self.interfaces()
        for stage in (0, 1):
            for field in ("source_files", "protocol_files", "execution_files"):
                for name in self.NAMES:
                    for suffix in ("", ".partial"):
                        with self.subTest(stage=stage, field=field, name=name, suffix=suffix), \
                             tempfile.TemporaryDirectory() as tmp:
                            args = self.args(Path(tmp))
                            target = args.output_dir / (name + suffix)
                            target.parent.mkdir()
                            target.write_bytes(b"inert mapped input")
                            # Path-only dictionaries are passed directly to the guard;
                            # no seal is created and no verifier is mocked or bypassed.
                            records = [{}, {}]
                            records[stage][field] = {str(target.relative_to(args.root)): "not a digest"}
                            with mock.patch.object(Path, "mkdir") as mkdir, self.assertRaises(ValueError):
                                env["_preflight_analysis_outputs"](args, records)
                            mkdir.assert_not_called()
                            loader.assert_not_called()
                            self.assertEqual(target.read_bytes(), b"inert mapped input")

    def test_original_output_links_and_named_aliases_refuse_before_ingestion(self):
        for name in self.NAMES:
            for suffix in ("", ".partial"):
                for kind in ("symlink", "hardlink", "dangling"):
                    with self.subTest(name=name, suffix=suffix, kind=kind), tempfile.TemporaryDirectory() as tmp:
                        args = self.args(Path(tmp))
                        target = args.output_dir / (name + suffix)
                        target.parent.mkdir()
                        source = Path(tmp) / "retained"
                        source.write_bytes(b"keep")
                        if kind == "hardlink":
                            os.link(source, target)
                        else:
                            target.symlink_to(Path(tmp) / "absent" if kind == "dangling" else source)
                        self.refused(args)
                        self.assertEqual(source.read_bytes(), b"keep")
        with tempfile.TemporaryDirectory() as tmp:
            args = self.args(Path(tmp))
            alias = Path(tmp) / "linked"
            alias.symlink_to(Path(tmp), target_is_directory=True)
            args.output_dir = alias / "unwritten"
            self.refused(args)

    def test_each_stale_partial_refuses_before_loading_or_publication(self):
        for name in self.NAMES:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                args = self.args(Path(tmp))
                partial = args.output_dir / (name + ".partial")
                partial.parent.mkdir()
                partial.write_bytes(b"stale")
                self.refused(args, FileExistsError)
                self.assertEqual(partial.read_bytes(), b"stale")
                self.assertFalse((args.output_dir / name).exists())

    def test_distinct_regular_products_and_sibling_inputs_remain_usable(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = self.args(Path(tmp))
            args.output_dir.mkdir()
            args.protocol = args.output_dir / "selected-protocol.json"
            args.cases = args.output_dir / "selected-cases.json"
            targets = [args.protocol, args.cases, *(args.output_dir / name for name in self.NAMES)]
            for target in targets:
                target.write_bytes(b"existing ordinary file")
            env, loader = self.interfaces()
            with mock.patch.object(Path, "mkdir") as mkdir, \
                 self.assertRaisesRegex(RuntimeError, "stop before ingestion"):
                env["run_analysis"](args)
            loader.assert_called_once_with(args.protocol)
            mkdir.assert_not_called()
            for target in targets:
                self.assertEqual(target.read_bytes(), b"existing ordinary file")

    def test_preflight_names_and_guard_order_match_actual_publication_ast(self):
        nodes = {n.name: n for n in ast.parse((ROOT / "analyze_activation.py").read_text()).body
                 if isinstance(n, ast.FunctionDef)}
        run = nodes["run_analysis"]
        returned = next(n.value for n in nodes["_figure_rows"].body if isinstance(n, ast.Return))
        actual = {n.value for n in returned.keys}
        actual |= {n.slice.value for n in ast.walk(run) if isinstance(n, ast.Subscript)
                   and isinstance(n.ctx, ast.Store) and isinstance(n.value, ast.Name)
                   and n.value.id == "figure_rows" and isinstance(n.slice, ast.Constant)}
        actual |= {n.right.value for n in ast.walk(run) if isinstance(n, ast.BinOp)
                   and isinstance(n.left, ast.Name) and n.left.id == "output_dir"
                   and isinstance(n.right, ast.Constant)}
        destinations = next(n.value for n in nodes["_preflight_analysis_outputs"].body
                            if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
                            and t.id == "destinations" for t in n.targets))
        self.assertEqual({n.right.value for n in destinations.elts}, actual)
        self.assertEqual(actual, set(self.NAMES))
        statements = [ast.unparse(n) for n in run.body]
        guards = [i for i, n in enumerate(statements) if n.startswith("_preflight_analysis_outputs(")]
        self.assertEqual(len(guards), 3)
        self.assertTrue(statements[guards[0]+1].startswith("protocol = _json"))
        self.assertTrue(statements[guards[1]-1].startswith("dense_seal = _verify_seal"))
        self.assertTrue(statements[guards[1]+1].startswith("_verify_frozen_maps(pde_seal"))
        self.assertEqual(statements[guards[2]+1], "output_dir.mkdir(parents=True, exist_ok=True)")


if __name__ == "__main__":
    unittest.main()
