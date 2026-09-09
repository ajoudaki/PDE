"""Stage-V routing/timeout fixtures only; no torch, launch, or authorizations.

Execute selected actual functions with an in-memory point registry and dummy
binding tokens. This tests failure publication, not execution authorization.
"""
import argparse
import ast
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

from studies._output_paths import StudyPaths

HERE = Path(__file__).resolve().parent
POINT = 'v_n8192_h1e5'


def fixture(root):
    names = {'checked_point_dir', 'atomic_json', 'finalize_timeout', 'main'}
    source = HERE/'run_stage_v_point.py'
    nodes = [n for n in ast.parse(source.read_text()).body if isinstance(n, ast.FunctionDef) and n.name in names]
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    generated = root/'generated'
    config, lock, unlock = (root/name for name in ('unread-config', 'unread-lock', 'unread-unlock'))
    def read(path):
        return {'points': [{'id': POINT}, {'id': 'v_n8192_h5e6'}]} if path == config else json.loads(path.read_text())
    env = dict(Path=Path, os=os, json=json, argparse=argparse, PATHS=StudyPaths(__file__),
               CONFIG=config, LOCK=lock, UNLOCK=unlock, OUTPUT_ROOT=generated,
               RUN_ROOT=generated/'runs/stage_v', LEDGER=generated/'.runtime/attempts.json',
               load_json=read, sha256=lambda p: 'fixture-binding-'+p.name, utc_now=lambda: 'fixture-time',
               resource=SimpleNamespace(RUSAGE_CHILDREN=0, getrusage=lambda _: SimpleNamespace(ru_maxrss=0)))
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(source), 'exec'), env)
    return env


def existing_attempt(env):
    manifest = env['RUN_ROOT']/POINT/'manifest.json'
    manifest.parent.mkdir(parents=True)
    record = dict(point_id=POINT, status='running', scientific_evidence_admissible=False,
                  config_sha256=env['sha256'](env['CONFIG']),
                  frozen_manifest_sha256=env['sha256'](env['LOCK']),
                  unlock_sha256=env['sha256'](env['UNLOCK']))
    manifest.write_text(json.dumps(record))
    env['LEDGER'].parent.mkdir(parents=True)
    env['LEDGER'].write_text(json.dumps({'attempts': {POINT: {'reserved_utc': 'fixture'}}}))
    return manifest


class StageVOutputBoundaryTests(unittest.TestCase):
    def test_absolute_traversal_and_unknown_points_refuse_before_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env = fixture(root)
            retained = root/'retained/manifest.json'
            retained.parent.mkdir()
            retained.write_text('{"status":"running"}')
            for point in (str(retained.parent), '../retained', '..', '.', 'unknown', POINT+'/../'+POINT):
                with self.subTest(point=point), mock.patch.object(Path, 'mkdir') as mkdir, \
                     mock.patch.object(sys, 'argv', ['stage-v', '--point', point, '--finalize-timeout']), \
                     self.assertRaises(ValueError):
                    env['main']()
                mkdir.assert_not_called()
                self.assertEqual(retained.read_text(), '{"status":"running"}')
            self.assertFalse(env['OUTPUT_ROOT'].exists())

    def test_missing_named_attempt_is_a_no_write_no_op(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = fixture(Path(tmp))
            with mock.patch.object(Path, 'mkdir') as mkdir:
                self.assertEqual(env['finalize_timeout'](POINT), 0)
            mkdir.assert_not_called()
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_reserved_matching_running_attempt_can_be_finalized(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = fixture(Path(tmp))
            manifest = existing_attempt(env)
            ledger = env['LEDGER'].read_bytes()
            self.assertEqual(env['finalize_timeout'](POINT), 0)
            record = json.loads(manifest.read_text())
            self.assertEqual(record['status'], 'failed_inconclusive_external_timeout')
            self.assertFalse(record['scientific_evidence_admissible'])
            self.assertEqual(record['point_id'], POINT)
            self.assertEqual(env['LEDGER'].read_bytes(), ledger)
            final = manifest.read_bytes()
            self.assertEqual(env['finalize_timeout'](POINT), 0)
            self.assertEqual(manifest.read_bytes(), final)
            self.assertFalse(manifest.with_suffix('.json.tmp').exists())

    def test_manifest_binding_and_reservation_mismatches_preserve_attempt(self):
        for field in ('point_id', 'config_sha256', 'frozen_manifest_sha256', 'unlock_sha256', 'reservation'):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as tmp:
                env = fixture(Path(tmp))
                manifest = existing_attempt(env)
                if field == 'reservation':
                    env['LEDGER'].write_text('{"attempts":{}}')
                else:
                    value = json.loads(manifest.read_text())
                    value[field] = 'mismatch'
                    manifest.write_text(json.dumps(value))
                before = manifest.read_bytes()
                with self.assertRaises(RuntimeError):
                    env['finalize_timeout'](POINT)
                self.assertEqual(manifest.read_bytes(), before)

    def test_linked_manifest_or_point_directory_cannot_redirect_finalization(self):
        for kind in ('symlink', 'hardlink', 'directory', 'dangling'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                env = fixture(root)
                retained = root/'retained/manifest.json'
                retained.parent.mkdir()
                retained.write_text('{"status":"running"}')
                point_dir = env['RUN_ROOT']/POINT
                point_dir.parent.mkdir(parents=True)
                if kind == 'directory':
                    point_dir.symlink_to(retained.parent)
                else:
                    point_dir.mkdir()
                    alias = point_dir/'manifest.json'
                    if kind == 'hardlink':
                        os.link(retained, alias)
                    else:
                        alias.symlink_to(root/'absent' if kind == 'dangling' else retained)
                with self.assertRaises(ValueError):
                    env['finalize_timeout'](POINT)
                self.assertEqual(retained.read_text(), '{"status":"running"}')

    def test_timeout_writer_preserves_existing_temporary(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = fixture(Path(tmp))
            manifest = existing_attempt(env)
            before = manifest.read_bytes()
            temporary = manifest.with_suffix('.json.tmp')
            temporary.write_bytes(b'existing temporary')
            with self.assertRaises(FileExistsError):
                env['finalize_timeout'](POINT)
            self.assertEqual(temporary.read_bytes(), b'existing temporary')
            self.assertEqual(manifest.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
