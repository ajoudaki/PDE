"""Processed-output boundaries with inert payloads; no evidence analysis."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace as NS
import unittest
from unittest import mock

from studies._output_paths import StudyPaths

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/analyze_results.py"


def functions(names, **extra):
    env = dict(Path=Path, os=os, tempfile=tempfile, argparse=argparse, AnalysisError=RuntimeError,
               PATHS=StudyPaths(SOURCE), AUDIT_ROOT=ROOT,
               GENERATED_ROOT=StudyPaths(SOURCE).generated,
               _sha256_file=lambda p: hashlib.sha256(p.read_bytes()).hexdigest())
    env.update(extra)
    nodes = [n for n in ast.parse(SOURCE.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(SOURCE), "exec"), env)
    return env


class ProcessedBoundaryTests(unittest.TestCase):
    def test_processed_directory_alias_refuses_before_any_payload_write(self):
        env = functions({"write_processed", "_atomic_write"})
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            source.mkdir()
            retained = source / "summary.json"
            retained.write_bytes(b"private protected source fixture")
            before = hashlib.sha256(retained.read_bytes()).hexdigest()
            output = root / "generated/historical_review/processed"
            output.parent.mkdir(parents=True)
            output.symlink_to(source, target_is_directory=True)
            with self.assertRaises(ValueError):
                env["write_processed"](NS(processed_root=output), {})
            after = hashlib.sha256(retained.read_bytes()).hexdigest()
            self.assertEqual(before, after)
            self.assertEqual(list(source.iterdir()), [retained])
            print("FIXTURE_SHA256", json.dumps(dict(case="proof-directory", before=before, after=after)))

    def test_atomic_callable_guards_targets_and_intermediates(self):
        writer = functions({"_atomic_write"})["_atomic_write"]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "input"
            source.write_bytes(b"keep")
            for suffix in ("", ".partial"):
                output = root / ("result" + str(len(suffix)))
                output.with_name(output.name + suffix).symlink_to(source)
                with mock.patch.object(Path, "mkdir") as mkdir, self.assertRaises(ValueError):
                    writer(output, b"fresh")
                mkdir.assert_not_called()
            self.assertEqual(source.read_bytes(), b"keep")

    def test_cli_output_refusal_precedes_discovery_and_no_write_stays_read_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "results/processed"
            output.parent.mkdir(parents=True)
            output.symlink_to(root, target_is_directory=True)
            discovery = mock.Mock(side_effect=LookupError("stop before evidence"))
            env = functions({"main", "build_parser", "_processed_output_root"}, discover_evidence=discovery)
            with self.assertRaises(ValueError):
                env["main"](["--audit-root", str(root)])
            discovery.assert_not_called()
            with self.assertRaisesRegex(LookupError, "stop before evidence"):
                env["main"](["--audit-root", str(root), "--no-write"])
            discovery.assert_called_once()

    def test_regular_publication_and_failed_replace_preserve_old_target(self):
        env = functions({"write_processed", "_atomic_write"})
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "processed"
            payloads = {name: b"private payload" for name in ("gates.csv", "metrics.csv", "archive_inventory.csv", "summary.json")}
            hashes = env["write_processed"](NS(processed_root=output), payloads)
            self.assertEqual(set(hashes), set(payloads))
            with mock.patch.object(os, "replace", side_effect=OSError("private failure")):
                with self.assertRaises(OSError):
                    env["_atomic_write"](output / "summary.json", b"new")
            self.assertEqual((output / "summary.json").read_bytes(), b"private payload")
            self.assertEqual(sorted(p.name for p in output.iterdir()), sorted(payloads))


if __name__ == "__main__":
    unittest.main()
