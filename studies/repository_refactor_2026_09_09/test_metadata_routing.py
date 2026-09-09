"""Private metadata fixtures; no numerical runs or historical-input writes."""

import argparse
import ast
from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch


REPO = Path(__file__).resolve().parents[2]
LONG = REPO / "studies/resnet_dense_long_horizon"


def manifest_module():
    spec = importlib.util.spec_from_file_location("metadata_fixture", LONG / "make_manifest.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def runner(module, source):
    path = LONG / "run_all.py"
    tree = ast.parse(path.read_text())
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    namespace = dict(argparse=argparse, Path=Path, json=json, Any=object,
                     ROOT=source, OUTPUT_ROOT=source / "unused",
                     source_hash=Mock(return_value="fixture-source-hash"),
                     expand_config=Mock(return_value=[{"id": "fixture", "group": "g"}]),
                     config_hash=Mock(return_value="fixture-config-hash"),
                     load_trace=Mock(return_value=({"config_sha256": "fixture-config-hash"}, None)),
                     run_trace=Mock(side_effect=AssertionError("research run attempted")),
                     environment_record=Mock(return_value={"fixture": True}),
                     analyze_directory=Mock(side_effect=AssertionError("analysis attempted")))
    exec(compile(ast.Module(body=[main], type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def alias(source, target, kind):
    target.parent.mkdir(parents=True, exist_ok=True)
    if kind == "symlink":
        target.symlink_to(source)
    else:
        os.link(source, target)


class MetadataRoutingTests(unittest.TestCase):
    def test_run_metadata_links_refuse_before_trace_reuse(self):
        module = manifest_module()
        for name in ("environment.json", "run_manifest.json", "source_sha256.txt"):
            for kind in ("symlink", "hardlink"):
                with self.subTest(name=name, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    config = root / "config.json"
                    config.write_text("{}")
                    output = root / "output"
                    trace = output / "results/raw/fixture.npz"
                    trace.parent.mkdir(parents=True)
                    trace.write_bytes(b"retained trace")
                    alias(trace, output / "metadata" / name, kind)
                    ns = runner(module, root)
                    with patch.dict(sys.modules, {"make_manifest": module}), patch.object(
                        sys, "argv", ["run_all", "--config", str(config), "--output-root", str(output), "--skip-analysis"]
                    ), self.assertRaises(ValueError):
                        ns["main"]()
                    ns["load_trace"].assert_not_called()
                    ns["run_trace"].assert_not_called()
                    self.assertEqual(trace.read_bytes(), b"retained trace")
                    self.assertEqual(config.read_text(), "{}")

    def test_manifest_links_preserve_hashed_source_and_run_inputs(self):
        for name in ("manifest.json", "SHA256SUMS"):
            for kind in ("symlink", "hardlink"):
                for source_kind in ("source", "run"):
                    with self.subTest(name=name, kind=kind, source=source_kind), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        module = manifest_module()
                        module.ROOT = root / "source"
                        module.ROOT.mkdir()
                        output = root / "output"
                        output.mkdir()
                        source = (module.ROOT if source_kind == "source" else output) / "input.txt"
                        source.write_bytes(b"retained input")
                        alias(source, output / "metadata" / name, kind)
                        with patch.object(sys, "argv", ["make_manifest", "--output-root", str(output)]), self.assertRaises(ValueError):
                            module.main()
                        self.assertEqual(source.read_bytes(), b"retained input")

    def test_run_reuses_separate_trace_and_refreshes_ordinary_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            module = manifest_module()
            config = root / "config.json"
            config.write_text("{}")
            output = root / "output"
            trace = output / "results/raw/fixture.npz"
            trace.parent.mkdir(parents=True)
            trace.write_bytes(b"retained trace")
            ns = runner(module, root)
            with patch.dict(sys.modules, {"make_manifest": module}), patch.object(
                sys, "argv", ["run_all", "--config", str(config), "--output-root", str(output), "--skip-analysis"]
            ), redirect_stdout(io.StringIO()):
                ns["main"]()
                ns["main"]()
            self.assertEqual(ns["load_trace"].call_count, 2)
            ns["run_trace"].assert_not_called()
            ns["analyze_directory"].assert_not_called()
            self.assertEqual(trace.read_bytes(), b"retained trace")
            self.assertEqual(json.loads((output / "metadata/environment.json").read_text()), {"fixture": True})
            self.assertEqual(config.read_text(), "{}")

    def test_input_configuration_cannot_be_a_mutable_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            module = manifest_module()
            output = root / "output"
            config = output / "metadata/environment.json"
            config.parent.mkdir(parents=True)
            config.write_text("{}")
            ns = runner(module, root)
            with patch.dict(sys.modules, {"make_manifest": module}), patch.object(
                sys, "argv", ["run_all", "--config", str(config), "--output-root", str(output), "--skip-analysis"]
            ), self.assertRaisesRegex(ValueError, "configuration outside"):
                ns["main"]()
            ns["load_trace"].assert_not_called()
            ns["run_trace"].assert_not_called()
            self.assertEqual(config.read_text(), "{}")
            self.assertFalse((output / "results").exists())

    def test_manifest_refresh_and_read_only_verification(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            module = manifest_module()
            module.ROOT = root / "source"
            module.ROOT.mkdir()
            (module.ROOT / "fixture.py").write_text("# source fixture\n")
            output = root / "output"
            output.mkdir()
            (output / "trace.txt").write_text("inert trace fixture\n")
            with patch.object(sys, "argv", ["make_manifest", "--output-root", str(output)]), redirect_stdout(io.StringIO()):
                module.main()
                module.main()
            before = {p: p.read_bytes() for p in output.rglob("*") if p.is_file()}
            with patch.object(sys, "argv", ["make_manifest", "--output-root", str(output), "--verify"]), redirect_stdout(io.StringIO()):
                module.main()
            self.assertEqual(before, {p: p.read_bytes() for p in output.rglob("*") if p.is_file()})


if __name__ == "__main__":
    unittest.main()
