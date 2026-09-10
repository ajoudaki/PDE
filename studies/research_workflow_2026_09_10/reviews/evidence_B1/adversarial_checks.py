from pathlib import Path
import contextlib
import importlib.util
import io
import json
import os
import shutil
import stat
import subprocess
import tempfile
import unittest
from unittest import mock

ROOT = Path.cwd()
AREA = ROOT / 'data/generated/research_workflow_2026_09_10/reviewer_b1'
spec = importlib.util.spec_from_file_location('reviewed_workflow', ROOT / 'studies/_workflow.py')
wf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wf)

class IndependentAttacks(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix='attack-', dir=AREA))
        for name in ('studies', 'data'):
            (self.root / name).mkdir()
        (self.root / 'README.md').write_text('Synthetic standalone root.\n')
        self.study = self.root / 'studies/demo'
        self.package = self.study / 'promotion/proposal'
        self.round = self.package / 'rounds/r1'
        self.baseline_patch = mock.patch.object(wf, 'baseline', return_value=None)
        self.baseline_patch.start()

    def tearDown(self):
        self.baseline_patch.stop()
        for p in self.root.rglob('*'):
            if p.is_dir() and not p.is_symlink():
                p.chmod(0o755)
        shutil.rmtree(self.root)

    def call(self, *args):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
            code = wf.main(list(args), root=self.root)
        return code, stream.getvalue()

    def start(self):
        self.assertEqual(self.call('start', 'demo', '--question', 'Synthetic gate experiment', '--owner', 'owner')[0], 0)

    def prepare(self):
        self.start()
        (self.package / 'candidate').mkdir(parents=True)
        (self.package / 'dependencies').mkdir()
        (self.package / 'candidate/result.md').write_bytes(b'A complete synthetic input.\nFinal unterminated line')
        (self.package / 'dependencies/definition.md').write_text('Synthetic dependency.\n')

    def dump(self, name, value):
        p = self.round / name
        p.chmod(0o644) if p.exists() else None
        p.write_bytes(wf.encoded(value))

    def complete(self):
        self.prepare()
        self.assertEqual(self.call('freeze', 'demo', 'proposal', 'r1', '--author-session', 'author', '--author-session', 'assembler')[0], 0)
        self.manifest = json.loads((self.round / 'inputs/INPUTS.json').read_text())
        common = {'schema': 1, 'input_digest': self.manifest['input_digest']}
        for name, text in [('selection.md', 'Selector independent full fixture.'), ('a.md', 'Reviewer A independent full fixture.'), ('b.md', 'Reviewer B independent full fixture.')]:
            (self.round / name).write_text(text)
        def report(name):
            return {'path': name, 'sha256': wf.digest((self.round / name).read_bytes())}
        self.dump('selection.json', dict(common, reviewer_session='selector', decision='accept', nonduplicate=True, relevant=True, useful=True, reason='Fixture is useful to tests.', report=report('selection.md')))
        for label in ('A', 'B'):
            self.dump('review_' + label + '.json', dict(common, reviewer_session='reviewer-' + label, full_input_read=True, isolated=True, verdict='clean', unresolved=[], completion_evidence='Synthetic fixture, not scientific review.', report=report(label.lower() + '.md')))
        self.assertEqual(self.check()[0], 0)

    def check(self):
        return self.call('check', 'demo', '--package', 'proposal', '--round', 'r1')

    def test_relative_control_paths_and_special_files_fail_closed(self):
        for value in ('', '.', '..', 'a//b', 'a/../b', '/a', 'a\\b', 'a\x00b', 'a\x7fb', 'a\nb'):
            with self.subTest(value=repr(value)), self.assertRaises(wf.WorkflowError):
                wf.safe(self.root, value, missing=True)
        fifo = self.root / 'special'
        os.mkfifo(fifo)
        with self.assertRaises(wf.WorkflowError):
            wf.safe(self.root, 'special', 'file')
        fifo.unlink()

    def test_manifest_duplicate_keys_and_typed_counts_rejected(self):
        self.complete()
        path = self.round / 'inputs/INPUTS.json'
        original = path.read_bytes()
        path.chmod(0o644)
        path.write_text('{"schema": 1, "schema": 1}')
        self.assertIn('duplicate JSON key', self.check()[1])
        for field, val in [('schema', True), ('package', 'wrong')]:
            bad = dict(self.manifest, **{field: val})
            bad['input_digest'] = wf.digest(wf.canonical({k: v for k, v in bad.items() if k != 'input_digest'}))
            path.write_bytes(wf.encoded(bad))
            self.assertEqual(self.check()[0], 1)
        bad = json.loads(original)
        bad['files']['candidate/result.md']['lines'] = True
        bad['input_digest'] = wf.digest(wf.canonical({k: v for k, v in bad.items() if k != 'input_digest'}))
        path.write_bytes(wf.encoded(bad))
        self.assertIn('invalid manifest hash, size or line count', self.check()[1])
        path.write_bytes(original)
        self.assertEqual(self.check()[0], 0)
        self.assertEqual(self.manifest['files']['candidate/result.md']['lines'], 2)

    def test_missing_dependency_and_same_hash_report_copy_rejected(self):
        self.complete()
        dep = self.package / 'dependencies/definition.md'
        saved = dep.read_bytes()
        dep.unlink()
        self.assertIn('current candidate/dependencies differ', self.check()[1])
        dep.write_bytes(saved)
        receipt = json.loads((self.round / 'review_B.json').read_text())
        copy = self.round / 'different-name.md'
        copy.write_bytes((self.round / 'a.md').read_bytes())
        receipt['report'] = {'path': copy.name, 'sha256': wf.digest(copy.read_bytes())}
        self.dump('review_B.json', receipt)
        self.assertIn('distinct full reports', self.check()[1])

    def test_receipt_identity_and_boolean_lookalikes_rejected(self):
        self.complete()
        for name, field, bad in [('selection.json', 'reviewer_session', 'assembler'), ('review_A.json', 'reviewer_session', 'selector'), ('review_B.json', 'reviewer_session', 'reviewer-A'), ('review_A.json', 'reviewer_session', ' reviewer-A'), ('review_A.json', 'full_input_read', 1), ('review_B.json', 'isolated', 'true'), ('review_A.json', 'completion_evidence', '   ')]:
            p = self.round / name
            original = p.read_bytes()
            value = json.loads(original)
            value[field] = bad
            self.dump(name, value)
            self.assertEqual(self.check()[0], 1, (name, field, bad))
            p.write_bytes(original)
        self.assertEqual(self.check()[0], 0)

    def test_partial_start_and_adopt_failures_preserve_existing_bytes(self):
        actual = wf.write_new
        count = 0
        def fail_third(path, content):
            nonlocal count
            count += 1
            if count == 3:
                raise OSError('independent injected third-write failure')
            return actual(path, content)
        with mock.patch.object(wf, 'write_new', side_effect=fail_third):
            self.assertEqual(self.call('start', 'demo', '--question', 'q', '--owner', 'o')[0], 1)
        self.assertFalse(self.study.exists())
        self.study.mkdir()
        original = b'Original README bytes\x00\xff'
        (self.study / 'README.md').write_bytes(original)
        count = 0
        with mock.patch.object(wf, 'write_new', side_effect=fail_third):
            self.assertEqual(self.call('adopt', 'demo', '--question', 'q', '--owner', 'o')[0], 1)
        self.assertEqual({p.name for p in self.study.iterdir()}, {'README.md'})
        self.assertEqual((self.study / 'README.md').read_bytes(), original)

    def test_partial_freeze_failure_preserves_source_and_allows_new_attempt(self):
        self.prepare()
        original = wf.sources(self.package)
        actual = wf.write_new
        count = 0
        def fail_fourth(path, content):
            nonlocal count
            count += 1
            if count == 4:
                raise OSError('independent injected fourth-write failure')
            return actual(path, content)
        with mock.patch.object(wf, 'write_new', side_effect=fail_fourth):
            self.assertEqual(self.call('freeze', 'demo', 'proposal', 'r1', '--author-session', 'author')[0], 1)
        self.assertFalse(self.round.exists())
        self.assertEqual(wf.sources(self.package), original)
        self.assertEqual(self.call('freeze', 'demo', 'proposal', 'r1', '--author-session', 'author')[0], 0)

    def test_baseline_result_validation_without_accessing_git(self):
        self.baseline_patch.stop()
        for stdout, code, expected in [('a' * 40 + '\n', 0, 'a' * 40), ('b' * 64 + '\n', 0, 'b' * 64), ('not-a-hash', 0, None), ('a' * 40, 1, None)]:
            with mock.patch.object(wf.subprocess, 'run', return_value=subprocess.CompletedProcess(['git'], code, stdout, '')):
                self.assertEqual(wf.baseline(self.root), expected)
        with mock.patch.object(wf.subprocess, 'run', side_effect=OSError('unavailable executable')):
            self.assertIsNone(wf.baseline(self.root))
        self.baseline_patch.start()

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(IndependentAttacks)
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    text = stream.getvalue()
    (AREA / 'adversarial_tests.log').write_text(text)
    print(text)
    raise SystemExit(not result.wasSuccessful())
