"""Real routing/I/O with fixed arrays or figure mocks; no scientific execution."""
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
from types import SimpleNamespace
import unittest
from unittest import mock

import numpy as np

from studies.resnet_generalization import generalization_paths as paths

ROOT = Path(__file__).resolve().parents[1]


def functions(filename, names, env):
    nodes = [n for n in ast.parse((ROOT/filename).read_text()).body
             if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])),
                 str(ROOT/filename), 'exec'), env)
    return env


class WriterBoundaryTests(unittest.TestCase):
    def writers(self):
        return functions('analyze_generalization.py', ['_atomic_bytes', '_atomic_figure'],
                         dict(Path=Path, os=os, require_output=paths.require_output, plt=mock.Mock()))

    def test_both_raw_entry_guards_refuse_links_before_any_calculation(self):
        for filename in ('run_pde.py', 'run_exact_reference.py'):
            for kind in ('symlink', 'hardlink'):
                with self.subTest(filename=filename, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    retained = root/'input'
                    retained.write_bytes(b'unchanged')
                    output = root/'output'
                    output.mkdir()
                    alias = output/'raw.npz.partial'
                    os.link(retained, alias) if kind == 'hardlink' else alias.symlink_to(retained)
                    # Only routing globals supplied: reaching computation would
                    # fail this test, even before a numerical call were possible.
                    env = functions(filename, ['run'], dict(Path=Path, require_output=paths.require_output))
                    with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaises(ValueError):
                        env['run'](SimpleNamespace(output_dir=output))
                    mkdir.assert_not_called()
                    self.assertEqual(retained.read_bytes(), b'unchanged')

    def test_raw_intermediates_are_exclusive_even_after_precheck(self):
        for filename in ('run_pde.py', 'run_exact_reference.py'):
            tree = ast.parse((ROOT/filename).read_text())
            writer = next(n for n in ast.walk(tree) if isinstance(n, ast.With)
                          and ast.unparse(n.items[0].context_expr).startswith('partial.open('))
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                partial = Path(tmp)/'raw.npz.partial'
                partial.write_bytes(b'late collision')
                with self.assertRaises(FileExistsError):
                    exec(compile(ast.Module(body=[writer], type_ignores=[]), str(ROOT/filename), 'exec'),
                         dict(partial=partial))
                self.assertEqual(partial.read_bytes(), b'late collision')

    def test_pde_publication_refuses_identical_restart_input(self):
        run = next(n for n in ast.parse((ROOT/'run_pde.py').read_text()).body
                   if isinstance(n, ast.FunctionDef) and n.name == 'run')
        start = next(i for i, n in enumerate(run.body) if isinstance(n, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == 'path' for t in n.targets))
        with tempfile.TemporaryDirectory() as tmp:
            retained = Path(tmp)/'restart.npz'
            retained.write_bytes(b'restart input')
            env = dict(Path=Path, output_dir=Path(tmp), name=retained.name,
                       require_output=paths.require_output, args=SimpleNamespace(restart_from=retained))
            with self.assertRaisesRegex(ValueError, 'restart input'):
                exec(compile(ast.Module(body=run.body[start:start+2], type_ignores=[]), 'publication', 'exec'), env)
            self.assertEqual(retained.read_bytes(), b'restart input')

    def test_exact_default_writer_with_fixed_arrays_then_alias_refusal(self):
        with tempfile.TemporaryDirectory() as tmp:
            generated = Path(tmp)/'generated'
            seed = mock.Mock(side_effect=lambda p: dict(seed=p['seed'], times=np.array([0.]),
                f=np.zeros((1, 3)), grams=np.zeros((1, 2, 3, 3)), theta=np.zeros((1, 3, 3))))
            env = functions('run_exact_reference.py', ['parse_args', 'run'], dict(
                argparse=argparse, Path=Path, np=np, hashlib=hashlib, json=json, os=os,
                GENERATED_ROOT=generated, require_output=paths.require_output,
                time=SimpleNamespace(perf_counter=lambda: 0.), _one_seed=seed))
            with mock.patch.object(sys, 'argv', ['raw', '--n', '1', '--depth', '1', '--seeds', '2',
                                                '--workers', '1', '--duration', '0']), \
                 contextlib.redirect_stdout(io.StringIO()):
                args = env['parse_args']()
                result = env['run'](args)
                self.assertEqual(result.parent, generated/'results/raw')
                with np.load(result) as data:
                    self.assertEqual(data['f'].shape, (2, 1, 3))
                    self.assertEqual(data['seeds'].tolist(), [1000, 1001])
                retained = Path(tmp)/'retained'
                retained.write_bytes(b'unchanged')
                result.with_suffix('.npz.partial').symlink_to(retained)
                seed.reset_mock()
                with self.assertRaises(ValueError):
                    env['run'](args)
                seed.assert_not_called()
                self.assertEqual(retained.read_bytes(), b'unchanged')

    def test_analysis_writers_preserve_colliding_intermediates_and_targets(self):
        env = self.writers()
        for writer in ('_atomic_bytes', '_atomic_figure'):
            for kind in ('ordinary', 'symlink', 'hardlink', 'dangling'):
                with self.subTest(writer=writer, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    output, retained = root/'output', root/'input'
                    retained.write_bytes(b'unchanged')
                    partial = root/'output.partial'
                    if kind == 'ordinary':
                        partial.write_bytes(b'collision')
                    elif kind == 'hardlink':
                        os.link(retained, partial)
                    else:
                        partial.symlink_to(root/'absent' if kind == 'dangling' else retained)
                    payload = b'fresh' if writer == '_atomic_bytes' else mock.Mock()
                    with self.assertRaises(FileExistsError):
                        env[writer](output, payload)
                    self.assertEqual(retained.read_bytes(), b'unchanged')
                    self.assertFalse(output.exists())
                    if kind == 'ordinary':
                        self.assertEqual(partial.read_bytes(), b'collision')

    def test_analysis_writers_validate_before_mkdir_and_accept_regular_replacement(self):
        env = self.writers()
        for writer in ('_atomic_bytes', '_atomic_figure'):
            payload = b'fresh' if writer == '_atomic_bytes' else mock.Mock()
            for root in (paths.STUDY_ROOT, paths.HISTORICAL_RESULTS,
                         paths.REPO_ROOT/'data/generated/another_study'):
                with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaises(ValueError):
                    env[writer](root/'unwritten', payload)
                mkdir.assert_not_called()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)/'fresh/output'
            env['_atomic_bytes'](output, b'first')
            env['_atomic_bytes'](output, b'second')
            self.assertEqual(output.read_bytes(), b'second')
            figure = mock.Mock()
            figure.savefig.side_effect = lambda handle, **kw: handle.write(b'figure fixture')
            env['_atomic_figure'](output, figure)
            self.assertEqual(output.read_bytes(), b'figure fixture')
            self.assertEqual(figure.savefig.call_args.kwargs, dict(format='png', dpi=150, bbox_inches='tight'))
            env['plt'].close.assert_called_once_with(figure)
            self.assertFalse(output.with_name(output.name+'.partial').exists())


if __name__ == '__main__':
    unittest.main()
