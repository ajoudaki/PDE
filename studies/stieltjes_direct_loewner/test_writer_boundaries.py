"""Corrected-clock routing only; never import or run the numerical engine."""
import ast
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from studies._output_paths import StudyPaths

SOURCE = Path(__file__).with_name("run_corrected_clock_test.py")


def functions(names, **extra):
    env = dict(Path=Path, PATHS=StudyPaths(SOURCE))
    env.update(extra)
    nodes = [n for n in ast.parse(SOURCE.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(SOURCE), "exec"), env)
    return env


class CorrectedClockBoundaryTests(unittest.TestCase):
    def test_named_log_aliases_refuse_before_main_or_callable_truncation(self):
        for kind in ("hardlink", "symlink", "directory"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                output = root / "generated"
                source = root / "retained/run.log"
                source.parent.mkdir()
                source.write_bytes(b"private corrected-clock input")
                before = hashlib.sha256(source.read_bytes()).hexdigest()
                if kind == "directory":
                    output.symlink_to(source.parent, target_is_directory=True)
                else:
                    output.mkdir()
                    target = output / "run.log"
                    os.link(source, target) if kind == "hardlink" else target.symlink_to(source)
                env = functions({"main", "log_factory"}, OUTPUT=output)
                for function, args in ((env["main"], ()), (env["log_factory"], (output / "run.log",))):
                    with mock.patch.object(Path, "mkdir") as mkdir, self.assertRaises(ValueError):
                        function(*args)
                    mkdir.assert_not_called()
                after = hashlib.sha256(source.read_bytes()).hexdigest()
                self.assertEqual(before, after)
                print("FIXTURE_SHA256", json.dumps(dict(case=f"corrected-clock/{kind}", before=before, after=after)))

    def test_normal_log_remains_usable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "run.log"
            log, handle = functions({"log_factory"})["log_factory"](path)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    log("private log line")
            finally:
                handle.close()
            self.assertEqual(path.read_text(), "private log line\n")

    def test_clean_main_reaches_log_without_running_science(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "fresh"
            logger = mock.Mock(side_effect=LookupError("stop before science"))
            env = functions({"main"}, OUTPUT=output, log_factory=logger)
            with self.assertRaisesRegex(LookupError, "stop before science"):
                env["main"]()
            logger.assert_called_once_with(output / "run.log")


if __name__ == "__main__":
    unittest.main()
