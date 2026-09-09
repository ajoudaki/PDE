"""Both migrated raw-writer families: AST/mocks only, never a trajectory."""
import ast
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace as NS
import unittest
from unittest import mock

from studies._output_paths import StudyPaths
from studies.resnet_generalization import generalization_paths as generalization
from studies.resnet_activation_controls import output_paths as activation

REPO = Path(__file__).resolve().parents[3]
FAMILIES = (("resnet_generalization", generalization),
            ("resnet_activation_controls/source", activation))


def functions(path, names, env):
    nodes = [n for n in ast.parse(path.read_text()).body
             if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])),
                 str(path), "exec"), env)
    return env


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def array(value=None):
    result = mock.MagicMock()
    result.tolist.return_value = [] if value is None else value
    result.__getitem__.return_value.tolist.return_value = []
    result.shape, result.size = (3, 3), 3
    return result


class RawPreflightTests(unittest.TestCase):
    def test_both_families_refuse_final_partial_and_registry_inputs(self):
        for name, paths in FAMILIES:
            for part in ("final", "partial"):
                for input_role in ("seal", "restart", "registry"):
                    with self.subTest(name=name, part=part, input_role=input_role), tempfile.TemporaryDirectory() as tmp:
                        output = Path(tmp) / "raw.npz"
                        source = output if part == "final" else output.with_suffix(".npz.partial")
                        source.write_bytes(b"private raw input")
                        before = digest(source)
                        with self.assertRaisesRegex(ValueError, "aliases an input"):
                            paths.require_raw_output(output, (None, source))
                        self.assertEqual(before, digest(source))
                        print("FIXTURE_SHA256", json.dumps(dict(case=f"{name}/{input_role}/{part}", before=before, after=digest(source))))

    def test_raw_guard_allows_distinct_restart_in_output_directory(self):
        for _, paths in FAMILIES:
            with tempfile.TemporaryDirectory() as tmp:
                source, output = Path(tmp) / "restart.npz", Path(tmp) / "new.npz"
                source.write_bytes(b"keep")
                self.assertEqual(paths.require_raw_output(output, (source,)), output)
                self.assertFalse(output.exists())

    def test_all_four_entrypoints_refuse_output_aliases_before_setup(self):
        for family, paths in FAMILIES:
            for filename in ("run_pde.py", "run_exact_reference.py"):
                with self.subTest(family=family, filename=filename), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    source = root / "input"
                    source.write_bytes(b"keep")
                    output = root / "output"
                    output.mkdir()
                    os.link(source, output / "raw.npz.partial")
                    path = REPO / "studies" / family / filename
                    env = functions(path, {"run"}, dict(Path=Path, require_output=paths.require_output,
                                                       PATHS=StudyPaths(path)))
                    with self.assertRaises(ValueError):
                        env["run"](NS(output_dir=output))
                    self.assertEqual(source.read_bytes(), b"keep")

    def exact_env(self, path, paths):
        numeric = NS(eye=lambda _: array(), array=array, stack=lambda _: array(),
                     mean=lambda *a, **kw: array(), std=lambda *a, **kw: array(),
                     sqrt=lambda _: 1, max=lambda *a, **kw: 0,
                     linalg=NS(norm=lambda *a, **kw: array()),
                     savez_compressed=lambda handle, **kw: handle.write(b"private output; no arrays\n"))
        seed = mock.Mock(side_effect=lambda p: dict(seed=p["seed"], times=[], f=[], grams=[], theta=[]))
        env = functions(path, {"run", "_file_sha256"}, dict(
            Path=Path, hashlib=hashlib, json=json, os=os, np=numeric,
            time=NS(perf_counter=lambda: 0), _one_seed=seed, PATHS=StudyPaths(path),
            require_output=paths.require_output, require_raw_output=paths.require_raw_output))
        return env, seed

    def test_exact_full_callable_refuses_own_content_derived_name_before_worker(self):
        for family, paths in FAMILIES:
            for part in ("final", "partial"):
                with self.subTest(family=family, part=part), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    source = root / "inert.json"
                    source.write_text('{"dynamics_sha256":"inert fixture; no authorization"}\n')
                    before = digest(source)
                    env, seed = self.exact_env(REPO / "studies" / family / "run_exact_reference.py", paths)
                    args = NS(output_dir=root / "output", pde_seal=source, case_id=None,
                              case_registry=None, activation=None, sigma_w=None, A=None, gamma=None,
                              n=1, depth=1, seeds=2, seed_start=1, workers=1,
                              duration=0.0, dt=1.0, sample_dt=1.0)
                    with contextlib.redirect_stdout(io.StringIO()):
                        output = env["run"](args)
                    self.assertEqual(seed.call_count, 2)
                    output.rename(root / "first-output")
                    target = output if part == "final" else output.with_suffix(".npz.partial")
                    source.rename(target)
                    args.pde_seal = target
                    seed.reset_mock()
                    with self.assertRaisesRegex(ValueError, "aliases an input"):
                        env["run"](args)
                    seed.assert_not_called()
                    self.assertEqual(before, digest(target))
                    print("FIXTURE_SHA256", json.dumps(dict(case=f"{family}/exact/{part}", before=before, after=digest(target))))

    def test_pde_identity_preflight_precedes_samples_and_preserves_both_inputs(self):
        for family, paths in FAMILIES:
            path = REPO / "studies" / family / "run_pde.py"
            run = next(n for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef) and n.name == "run")
            start = next(i for i, n in enumerate(run.body) if isinstance(n, ast.Assign)
                         and any(isinstance(t, ast.Name) and t.id == "path" for t in n.targets))
            code = ast.Module(body=run.body[start:start + 2], type_ignores=[])
            self.assertIn("require_raw_output", ast.unparse(code.body[-1]))
            self.assertLess(code.body[-1].lineno, next(n.lineno for n in ast.walk(run)
                if isinstance(n, ast.Call) and ast.unparse(n.func) == "np.empty"))
            for part in ("final", "partial"):
                for role in ("restart_from", "case_registry"):
                    with self.subTest(family=family, part=part, role=role), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        output = root / "raw.npz"
                        source = output if part == "final" else output.with_suffix(".npz.partial")
                        source.write_bytes(b"private PDE input")
                        before = digest(source)
                        args = NS(restart_from=None, case_registry=None)
                        setattr(args, role, source)
                        with self.assertRaisesRegex(ValueError, "aliases an input"):
                            exec(compile(code, str(path), "exec"), dict(Path=Path, output_dir=root,
                                name=output.name, args=args, require_output=paths.require_output,
                                require_raw_output=paths.require_raw_output))
                        self.assertEqual(before, digest(source))
                        print("FIXTURE_SHA256", json.dumps(dict(case=f"{family}/pde/{role}/{part}", before=before, after=digest(source))))

    def test_all_raw_intermediate_opens_are_exclusive(self):
        for family, _ in FAMILIES:
            for filename in ("run_pde.py", "run_exact_reference.py"):
                tree = ast.parse((REPO / "studies" / family / filename).read_text())
                writer = next(n for n in ast.walk(tree) if isinstance(n, ast.With)
                              and ast.unparse(n.items[0].context_expr).startswith("partial.open("))
                with tempfile.TemporaryDirectory() as tmp:
                    partial = Path(tmp) / "raw.npz.partial"
                    partial.write_bytes(b"keep stale partial")
                    with self.assertRaises(FileExistsError):
                        exec(compile(ast.Module(body=[writer], type_ignores=[]), filename, "exec"), {"partial": partial})
                    self.assertEqual(partial.read_bytes(), b"keep stale partial")

    def test_failed_exact_publication_keeps_old_final_and_blocks_retry_before_worker(self):
        for family, paths in FAMILIES:
            with self.subTest(family=family), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source = root / "input.json"
                source.write_text('{"dynamics_sha256":"private fixture; no authorization"}')
                before_input = digest(source)
                env, seed = self.exact_env(REPO / "studies" / family / "run_exact_reference.py", paths)
                args = NS(output_dir=root / "output", pde_seal=source, case_id=None,
                          case_registry=None, activation=None, sigma_w=None, A=None, gamma=None,
                          n=1, depth=1, seeds=2, seed_start=1, workers=1,
                          duration=0.0, dt=1.0, sample_dt=1.0)
                with contextlib.redirect_stdout(io.StringIO()):
                    output = env["run"](args)
                before_output = digest(output)
                def failed_serializer(handle, **payload):
                    handle.write(b"incomplete private fixture")
                    raise OSError("private serializer failure")
                env["np"].savez_compressed = failed_serializer
                with self.assertRaisesRegex(OSError, "private serializer failure"):
                    env["run"](args)
                self.assertEqual(digest(source), before_input)
                self.assertEqual(digest(output), before_output)
                partial = output.with_suffix(".npz.partial")
                self.assertEqual(partial.read_bytes(), b"incomplete private fixture")
                seed.reset_mock()
                with self.assertRaisesRegex(FileExistsError, "stale partial"):
                    env["run"](args)
                seed.assert_not_called()
                print("FIXTURE_SHA256", json.dumps(dict(case=f"{family}/publication-failure/input", before=before_input, after=digest(source))))
                print("FIXTURE_SHA256", json.dumps(dict(case=f"{family}/publication-failure/final", before=before_output, after=digest(output))))


if __name__ == "__main__":
    unittest.main()
