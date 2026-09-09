"""Named validation writers and archived attempt APIs; inert private fixtures only."""
import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

from studies._output_paths import StudyPaths
from studies.stieltjes_hybrid_campaign.breadth_panel.fp64_successor.legacy_runtime import require_current_authorization

ROOT = Path(__file__).resolve().parent


def functions(path, names, env):
    nodes = [n for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), "exec"), env)
    return env


class AcceptanceBoundaryTests(unittest.TestCase):
    def test_validation_named_output_alias_refuses_callable_and_cli_before_analysis(self):
        path = ROOT / "validation_analysis.py"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "retained-input"
            source.write_bytes(b"private retained validation input")
            before = hashlib.sha256(source.read_bytes()).hexdigest()
            output = root / "generated/validation_analysis"
            output.mkdir(parents=True)
            os.link(source, output / "VALIDATION_RESULT.json")
            analysis = mock.Mock(side_effect=AssertionError("analysis prohibited"))
            env = functions(path, {"write_outputs", "main"}, dict(
                PATHS=StudyPaths(path), OUTPUT_ROOT=output, argparse=argparse, analyze=analysis))
            with self.assertRaises(ValueError):
                env["write_outputs"]({})
            with mock.patch.object(sys, "argv", ["validation", "--write"]), self.assertRaises(ValueError):
                env["main"]()
            analysis.assert_not_called()
            after = hashlib.sha256(source.read_bytes()).hexdigest()
            self.assertEqual(before, after)
            print("FIXTURE_SHA256", json.dumps(dict(case="validation-named-output", before=before, after=after)))

    def test_validation_regular_outputs_keep_historical_review_label(self):
        path = ROOT / "validation_analysis.py"
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "fresh"
            env = functions(path, {"write_outputs", "_json_bytes"}, dict(
                PATHS=StudyPaths(path), OUTPUT_ROOT=output, json=json, hashlib=hashlib,
                render_report=lambda *a: "private mock report"))
            env["write_outputs"]({"fixture": True})
            self.assertEqual(json.loads((output / "VALIDATION_RESULT.json").read_text()), {"fixture": True})
            self.assertTrue((output / "RESULTS.md").read_text().startswith("Historical review only; not current execution authorization."))

    def test_claim_and_finish_refuse_before_lock_or_ledger_access(self):
        path = ROOT / "fp64_successor/run_local_qualification.py"
        for name, arguments in (("claim_canonical_attempt", (None, {}, "A", "cuda:0", {})),
                                ("finish_canonical_attempt", (None, "A", {"status": "failed", "gpu_seconds": 0}))):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                ledger = Path(tmp) / "private-ledger.json"
                ledger.write_bytes(b'{"fixture":"not an attempt authorization","consumed_gpu_seconds":7}\n')
                before = hashlib.sha256(ledger.read_bytes()).hexdigest()
                args = arguments if name == "claim_canonical_attempt" else (ledger, *arguments[1:])
                env = functions(path, {name}, {"require_current_authorization": require_current_authorization})
                with mock.patch.object(Path, "open") as opened, self.assertRaisesRegex(RuntimeError, "archive-only"):
                    env[name](*args)
                opened.assert_not_called()
                self.assertEqual(list(Path(tmp).iterdir()), [ledger])
                after = hashlib.sha256(ledger.read_bytes()).hexdigest()
                self.assertEqual(before, after)
                print("FIXTURE_SHA256", json.dumps(dict(case=name, before=before, after=after)))


if __name__ == "__main__":
    unittest.main()
