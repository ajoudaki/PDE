"""Tiny source/evidence interface checks; no trajectories or seals generated."""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from generalization_paths import RESULTS, GENERATED_ROOT, evidence_label, evidence_path, evidence_root, precheck_command
import pde_precheck
import verify_study

spec = importlib.util.spec_from_file_location('migration_generalization_grid', ROOT/'protocol/run_grid.py')
grid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grid)


class EvidencePathTests(unittest.TestCase):
    def test_writer_precheck_verifier_defaults_agree(self):
        self.assertEqual(grid.RESULTS, pde_precheck.RESULTS)
        self.assertEqual(grid.RESULTS, verify_study.RESULTS)
        self.assertTrue(RESULTS.is_relative_to(ROOT.parents[1]/'data/generated/resnet_generalization'))

    def test_label_round_trip_and_escapes(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp)/'fresh/results/generalization'
            for suffix in ('pde_primary/a.npz', 'dense_confirm/b.npz', 'pde_numerical_decision.json'):
                path = results/suffix
                label = evidence_label(path, results)
                self.assertEqual(label, 'results/generalization/'+suffix)
                self.assertEqual(evidence_path(label, results), path)
            for label in ('', '.', '../outside', '/etc/passwd', 'results/../outside', 'a//b'):
                with self.assertRaises(ValueError):
                    evidence_path(label, results)
            with self.assertRaises(ValueError):
                evidence_label(Path(tmp)/'outside', results)

    def test_precheck_child_command_passes_its_input_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp)/'fresh/results/generalization'
            output = Path(tmp)/'decision.json'
            command = precheck_command(sys.executable, results, output)
            args = pde_precheck.parse_args(command[2:])
            self.assertEqual(args.results_dir, results)
            self.assertEqual(args.output, output)
            self.assertFalse(args.historical)

    def test_precheck_reads_selected_tiny_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp)/'fresh/results/generalization'
            path = results/'pde_primary/pde_C0_fixture.npz'
            path.parent.mkdir(parents=True)
            np.savez(path, metadata_json=json.dumps({'quadrature_seed': 7}), value=np.array([1.0]))
            selected = pde_precheck.find_one('pde_primary', 'C0', results_dir=results, quadrature_seed=7)
            self.assertEqual(selected, path)
            self.assertEqual(pde_precheck.load(selected)['value'].tolist(), [1.0])

    def test_historical_precheck_requires_explicit_selection_and_fresh_output(self):
        fresh = pde_precheck.parse_args([])
        historical = pde_precheck.parse_args(['--historical'])
        self.assertEqual(fresh.results_dir, RESULTS)
        self.assertNotEqual(fresh.results_dir, historical.results_dir)
        self.assertEqual(historical.output.parent, GENERATED_ROOT/'historical_review')
        with self.assertRaises(ValueError):
            pde_precheck.parse_args(['--output', str(ROOT/'forbidden.json')])

    def test_grid_and_verifier_read_the_same_synthetic_seal(self):
        with tempfile.TemporaryDirectory() as tmp:
            results = Path(tmp)/'fresh/results/generalization'
            archive = results/'pde_primary/tiny.npz'
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b'synthetic evidence, not a trajectory')
            record = {'dynamics_sha256': 'fixture', 'run_grid_sha256': grid._sha256(Path(grid.__file__)),
                      'files': {evidence_label(archive, results): grid._sha256(archive)}, 'file_count': 1}
            seal = results/'PDE_STAGE_SEAL.json'
            seal.write_text(json.dumps(record))
            with mock.patch.object(grid, 'RESULTS', results), mock.patch.object(grid, 'verify_frozen', return_value='fixture'):
                grid._require_pde_seal()
            self.assertEqual(verify_study.verify_seal(seal, results), record)
            archive.write_bytes(b'changed fixture')
            with self.assertRaises(RuntimeError):
                verify_study.verify_seal(seal, results)

    def test_analyzer_evidence_interface_without_optional_plot_import(self):
        # Extract only inspected path/hash functions; this is not a Matplotlib import pass.
        source = ast.parse((ROOT/'analyze_generalization.py').read_text())
        names = {'sha256_file', '_json', '_equal', 'require_metadata', '_inventory_archives', 'verify_dense_seal'}
        nodes = [n for n in source.body if isinstance(n, ast.FunctionDef) and n.name in names]
        future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
        tree = ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[]))
        env = dict(Path=Path, hashlib=hashlib, json=json, os=os, np=np, AnalysisIntegrityError=RuntimeError,
                   evidence_root=evidence_root, evidence_path=evidence_path,
                   ALLOWED_ARCHIVE_DIRS={'dense_screen'})
        exec(compile(tree, str(ROOT/'analyze_generalization.py'), 'exec'), env)
        with tempfile.TemporaryDirectory() as tmp:
            source_root = Path(tmp)/'source'
            runner = source_root/'protocol/run_grid.py'
            runner.parent.mkdir(parents=True)
            runner.write_text('fixture source')
            results = Path(tmp)/'fresh/results/generalization'
            archive = results/'dense_screen/tiny.npz'
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b'fixture')
            digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
            record = dict(dynamics_sha256='d', pde_seal_sha256='p', run_grid_sha256=digest(runner),
                          files={evidence_label(archive, results): digest(archive)}, file_count=1)
            (results/'DENSE_STAGE_SEAL.json').write_text(json.dumps(record))
            checked, _ = env['verify_dense_seal'](source_root, results, dynamics_hash='d', pde_seal_hash='p')
            self.assertEqual(checked, record)


if __name__ == '__main__':
    unittest.main()
