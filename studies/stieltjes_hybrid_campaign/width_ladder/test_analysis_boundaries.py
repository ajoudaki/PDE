"""Selected-input/output relationships; no archive ingestion or resampling."""
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

from studies._output_paths import StudyPaths

SOURCE = Path(__file__).with_name("width_analysis.py")


def environment(loader):
    env = dict(Path=Path, PATHS=StudyPaths(SOURCE), argparse=argparse, load_npz=loader)
    nodes = [n for n in ast.parse(SOURCE.read_text()).body if isinstance(n, ast.FunctionDef)
             and n.name in {"main", "require_analysis_output"}]
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(SOURCE), "exec"), env)
    return env


class WidthOutputTests(unittest.TestCase):
    def test_all_five_inputs_refuse_same_lexical_and_link_aliases_before_loading(self):
        flags = ("--n2048", "--n4096", "--n8192-shard0", "--n8192-shard1", "--n4096-halfstep")
        for selected in flags:
            for kind in ("same", "lexical", "hardlink", "symlink"):
                with self.subTest(selected=selected, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    inputs = {flag: root / (flag[2:] + ".npz") for flag in flags}
                    for path in inputs.values():
                        path.write_bytes(b"private width input")
                    source = inputs[selected]
                    before = hashlib.sha256(source.read_bytes()).hexdigest()
                    output = source
                    if kind == "lexical":
                        output = root / "sub/.." / source.name
                    elif kind in ("symlink", "hardlink"):
                        output = root / "alias.json"
                        os.link(source, output) if kind == "hardlink" else output.symlink_to(source)
                    argv = ["analysis", *[item for pair in inputs.items() for item in (pair[0], str(pair[1]))], "--output", str(output)]
                    loader = mock.Mock(side_effect=AssertionError("input loading prohibited"))
                    env = environment(loader)
                    with mock.patch.object(sys, "argv", argv), self.assertRaises(ValueError):
                        env["main"]()
                    loader.assert_not_called()
                    after = hashlib.sha256(source.read_bytes()).hexdigest()
                    self.assertEqual(before, after)
                    print("FIXTURE_SHA256", json.dumps(dict(case=f"width/{selected}/{kind}", before=before, after=after)))

    def test_distinct_output_reaches_loader_without_creating_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            loader = mock.Mock(side_effect=LookupError("stop before ingest"))
            env = environment(loader)
            flags = ("--n2048", "--n4096", "--n8192-shard0", "--n8192-shard1", "--n4096-halfstep")
            output = root / "new/result.json"
            argv = ["analysis", *[value for flag in flags for value in (flag, str(root / (flag[2:] + ".npz")))], "--output", str(output)]
            with mock.patch.object(sys, "argv", argv), self.assertRaisesRegex(LookupError, "stop before ingest"):
                env["main"]()
            loader.assert_called_once()
            self.assertFalse(output.parent.exists())


if __name__ == "__main__":
    unittest.main()
