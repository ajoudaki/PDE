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


if __name__ == "__main__":
    unittest.main()
