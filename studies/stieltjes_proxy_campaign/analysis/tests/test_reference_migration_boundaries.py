"""Side-check preflight and explicit config routing, without torch or analysis."""
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

ROOT = Path(__file__).resolve().parents[2]


def functions(path, names, env):
    nodes = [n for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), "exec"), env)
    return env


class ReferenceMigrationTests(unittest.TestCase):
    def side_environment(self, filename, root, output, reference):
        path = ROOT / "reference/side_checks" / filename
        load = mock.Mock(return_value={})
        device = mock.Mock(side_effect=LookupError("stop before CUDA"))
        cuda = NS(is_available=mock.Mock(side_effect=LookupError("stop before CUDA")))
        env = functions(path, {"main"}, dict(
            PATHS=StudyPaths(path), OUTPUT_JSON=output, OUTPUT_ROOT=output.parent,
            REFERENCE_NPZ=reference, np=NS(load=load), torch=NS(device=device, cuda=cuda),
            parse_args=lambda: NS(step=5.0e-6, device="cuda:0")))
        return env, load, device, cuda

    def test_named_outputs_reject_own_reference_aliases_before_loading_or_cuda(self):
        for filename, output_name in (("gd_vs_rk4_n4096.py", "gd-vs-rk4-n4096-result.json"),
                                      ("gd_vs_rk4_n8192_point.py", "gd-vs-rk4-n8192-h5e-6.json")):
            for kind in ("hardlink", "symlink", "directory"):
                with self.subTest(filename=filename, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    reference = root / "reference.npz"
                    reference.write_bytes(b"private historical-only reference")
                    before = hashlib.sha256(reference.read_bytes()).hexdigest()
                    directory = root / "output"
                    if kind == "directory":
                        directory.symlink_to(root, target_is_directory=True)
                    else:
                        directory.mkdir()
                        target = directory / output_name
                        os.link(reference, target) if kind == "hardlink" else target.symlink_to(reference)
                    env, load, device, cuda = self.side_environment(filename, root, directory / output_name, reference)
                    with self.assertRaises(ValueError):
                        env["main"]()
                    load.assert_not_called()
                    device.assert_not_called()
                    cuda.is_available.assert_not_called()
                    after = hashlib.sha256(reference.read_bytes()).hexdigest()
                    self.assertEqual(before, after)
                    print("FIXTURE_SHA256", json.dumps(dict(case=f"{filename}/{kind}", before=before, after=after)))

    def test_both_sidechecks_refuse_missing_reference_before_cuda_or_output_creation(self):
        for filename in ("gd_vs_rk4_n4096.py", "gd_vs_rk4_n8192_point.py"):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                env, load, device, cuda = self.side_environment(filename, root, root / "new/output.json", root / "absent.npz")
                with self.assertRaises(FileNotFoundError):
                    env["main"]()
                load.assert_not_called()
                device.assert_not_called()
                cuda.is_available.assert_not_called()
                self.assertFalse((root / "new").exists())

    def test_both_sidechecks_load_reference_before_cuda_and_fail_read_only(self):
        for filename in ("gd_vs_rk4_n4096.py", "gd_vs_rk4_n8192_point.py"):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                reference = root / "reference.npz"
                reference.write_bytes(b"inert fixture; loader mocked")
                env, load, device, cuda = self.side_environment(filename, root, root / "new/output.json", reference)
                with self.assertRaisesRegex(LookupError, "stop before CUDA"):
                    env["main"]()
                load.assert_called_once_with(reference)
                self.assertFalse((root / "new").exists())
                device.reset_mock()
                cuda.is_available.reset_mock()
                load.side_effect = OSError("unreadable private reference")
                with self.assertRaisesRegex(OSError, "unreadable"):
                    env["main"]()
                device.assert_not_called()
                cuda.is_available.assert_not_called()
                self.assertEqual(reference.read_bytes(), b"inert fixture; loader mocked")

    def test_omitted_config_refuses_before_summary_read(self):
        source = ROOT / "analysis/reference_data.py"
        env = functions(source, {"load_reference_run"}, dict(Path=Path, json=json))
        with mock.patch.object(Path, "read_text") as read, self.assertRaisesRegex(ValueError, "config_path is required"):
            env["load_reference_run"](Path("unread-summary.json"))
        read.assert_not_called()

    def test_explicit_config_accepts_generated_and_historical_named_summary(self):
        source = ROOT / "analysis/reference_data.py"
        env = functions(source, {"load_reference_run"}, dict(Path=Path, json=json, ReferenceRun=NS))
        for location in ("generated", "historical"):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                summary = root / location / "reference/runs/private/summary.json"
                summary.parent.mkdir(parents=True)
                summary.write_text('{"points":[],"status":"private_fixture"}')
                config = root / "source-config.json"
                config.write_text('{"points":[]}')
                before = hashlib.sha256(summary.read_bytes()).hexdigest()
                result = env["load_reference_run"](summary, config_path=config)
                self.assertEqual(result.config_path, config)
                self.assertEqual(result.points, ())
                after = hashlib.sha256(summary.read_bytes()).hexdigest()
                self.assertEqual(before, after)
                print("FIXTURE_SHA256", json.dumps(dict(case=f"explicit-config/{location}", before=before, after=after)))


if __name__ == "__main__":
    unittest.main()
