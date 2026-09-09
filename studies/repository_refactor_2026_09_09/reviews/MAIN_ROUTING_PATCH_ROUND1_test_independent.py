"""Independent acceptance probes; no use of supplied test helper implementations."""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest.mock import Mock, patch

REPO = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).resolve().parent
QROOT = REPO / 'studies/mfp_quadratic_compiler'
LONG = REPO / 'studies/resnet_dense_long_horizon'
sys.path.insert(0, str(REPO))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

@contextlib.contextmanager
def imported(root, centered=False):
    external = {}
    for name, names in {
        'identity_order13_stieltjes_audit': ['enumerate_accessible_hankel_minors', 'matrix_label'],
        'identity_stieltjes_audit': ['audit_hankels', 'fraction_string', 'load_reversion_route',
                                    'moments_from_triangular_identity', 'signed_record'],
        'run_search': ['algebraic_candidates', 'recurrence_candidates'],
    }.items():
        external[name] = ModuleType(name)
        for symbol in names:
            setattr(external[name], symbol, Mock(side_effect=AssertionError('unmocked external science')))
    old_cwd = Path.cwd()
    with patch.object(sys, 'path', list(sys.path)), patch.dict(sys.modules, external), patch.dict(os.environ, {
        'PDE_QUADRATIC_INPUT_ROOT': str(root / 'input'),
        'PDE_QUADRATIC_OUTPUT_ROOT': str(root / 'output'),
    }):
        sys.modules.pop('campaign_paths', None)
        try:
            os.chdir(root)
            relative = ('centered_depth1_order13/centered_h2_exact.py' if centered
                        else 'campaign1/run_graded_campaign.py')
            yield load(QROOT / relative, 'independent_' + ('centered' if centered else 'graded'))
        finally:
            os.chdir(old_cwd)

class Acceptance(unittest.TestCase):
    maxDiff = None

    def graded_alias(self, consumed, kind):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root) as module:
                module.__file__ = str(root / 'run_graded_campaign.py')
                inputs = {'lower': root / 'lower.json', 'binary': root / 'binary',
                          'provenance': root / 'graded_sector.cpp'}
                for path in inputs.values():
                    path.write_bytes(b'inert retained input')
                source = inputs[consumed]
                output = root / 'export.json'
                if kind == 'same':
                    output = source
                elif kind == 'symlink':
                    output.symlink_to(source)
                elif kind == 'hardlink':
                    os.link(source, output)
                elif kind == 'parent-symlink':
                    alias = root / 'parent-alias'
                    alias.symlink_to(root, target_is_directory=True)
                    output = alias / source.name
                elif kind == 'dotdot':
                    (root / 'nested').mkdir()
                    output = root / 'nested' / '..' / source.name
                elif kind == 'dangling':
                    source.unlink()
                    output.symlink_to(source)
                elif kind == 'source-symlink':
                    real = root / 'real-input'
                    source.rename(real)
                    source.symlink_to(real)
                    output = real
                before = {str(p): digest(p) for p in inputs.values() if p.exists()}
                stop = Mock(side_effect=AssertionError('work happened before refusal'))
                module.sha256 = stop
                module.run_order = stop
                with patch.object(sys, 'argv', ['graded', '--binary', str(inputs['binary']),
                                  '--lower-result', str(inputs['lower']), '--output', str(output)]):
                    with self.assertRaisesRegex(ValueError, 'aliases an input'):
                        module.main()
                stop.assert_not_called()
                self.assertEqual(before, {str(p): digest(p) for p in inputs.values() if p.exists()})

    def centered_alias(self, consumed, kind, long_search):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root, centered=True) as module:
                here = root / 'source'
                here.mkdir()
                source, protocol = here / 'centered_h2_exact.py', here / 'PROTOCOL.md'
                for path in (source, protocol):
                    path.write_bytes(b'inert retained provenance')
                selected = source if consumed == 'source' else protocol
                module.__file__, module.HERE = str(source), here
                output = root / 'output/centered_depth1_order13/RESULTS.json'
                output.parent.mkdir(parents=True)
                if kind == 'hardlink':
                    os.link(selected, output)
                elif kind == 'dangling':
                    selected.unlink()
                    output.symlink_to(selected)
                elif kind == 'parent-symlink':
                    alias = root / 'source-alias'
                    alias.symlink_to(here, target_is_directory=True)
                    output.symlink_to(alias / selected.name)
                else:
                    output.symlink_to(selected)
                before = {str(p): digest(p) for p in (source, protocol) if p.exists()}
                stop = Mock(side_effect=AssertionError('science or hashing before refusal'))
                module.lie_jet = module.taylor_jet = module.sha256 = stop
                with patch.object(sys, 'argv', ['centered', *(['--long-search'] if long_search else [])]):
                    with self.assertRaisesRegex(ValueError, 'aliases an input'):
                        module.main()
                stop.assert_not_called()
                self.assertEqual(before, {str(p): digest(p) for p in (source, protocol) if p.exists()})

    def centered_refresh(self, long_search):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root, centered=True) as module:
                here = root / 'output/centered_depth1_order13'
                here.mkdir(parents=True)
                source, protocol = here / 'centered_h2_exact.py', here / 'PROTOCOL.md'
                source.write_bytes(b'inert source fixture')
                protocol.write_bytes(b'inert protocol fixture')
                module.__file__, module.HERE = str(source), here
                before = {str(p): digest(p) for p in (source, protocol)}
                order = module.SEARCH_ORDER if long_search else module.DECISION_ORDER
                module.lie_jet = Mock(return_value=([0] * (order + 1), []))
                module.taylor_jet = Mock(return_value=([0] * 14, {}))
                module.moments_from_triangular_identity = Mock(return_value=(0, (0,) * 6))
                module.load_reversion_route = Mock(return_value=Mock(return_value=(0, (0,) * 6)))
                module.serialize_minors = Mock(return_value={'all_positive': False, 'negative_labels': []})
                module.audit_hankels = Mock(return_value={})
                module.fraction_string = str
                module.signed_record = lambda value: {'exact': str(value)}
                module.algebraic_candidates = Mock(return_value=[])
                module.recurrence_candidates = Mock(return_value=[])
                output = here / 'RESULTS.json'
                output.write_text('old distinct export')
                for repeat in range(2):
                    with patch.object(sys, 'argv', ['centered', *(['--long-search'] if long_search else [])]), contextlib.redirect_stdout(io.StringIO()):
                        self.assertEqual(module.main(), 0)
                    payload = json.loads(output.read_text())
                    self.assertEqual(payload['sha256'], {'source': before[str(source)], 'protocol': before[str(protocol)]})
                self.assertEqual(before, {str(p): digest(p) for p in (source, protocol)})
                self.assertEqual(module.algebraic_candidates.call_count, 2 if long_search else 0)

    def test_graded_refresh_complete_main_real_provenance_digest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root) as module:
                module.__file__ = str(root / 'run_graded_campaign.py')
                lower, binary, source, output = [root / name for name in ('lower.json', 'binary', 'graded_sector.cpp', 'export.json')]
                fixture = {'parent_source_sha256': 'inert-parent', 'cache': {}, 'misses_by_remaining_order': {},
                    'observables': {key: {'jets': [{'lambda_coefficients': ['0']} for _ in range(8)],
                      'seconds': 0, 'cache_before': {}, 'cache_after': {}} for key in ('f', 'q1', 'q2')}}
                lower.write_text(json.dumps(fixture))
                binary.write_bytes(b'never executed')
                source.write_bytes(b'inert provenance')
                before = {str(p): digest(p) for p in (lower, binary, source)}
                real_sha = module.sha256
                module.sha256 = lambda p: module.EXPECTED_LOWER_SHA if p == lower else real_sha(p)
                output.write_text('previous separate export')
                for repeat in range(2):
                    module.run_order = Mock(side_effect=[([module.EXPECTED_F9], []), ([0], [])])
                    with patch.object(sys, 'argv', ['graded', '--binary', str(binary), '--lower-result', str(lower), '--output', str(output)]), contextlib.redirect_stdout(io.StringIO()):
                        module.main()
                    self.assertEqual(json.loads(output.read_text())['graded_sector_source_sha256'], before[str(source)])
                    self.assertEqual(module.run_order.call_count, 2)
                self.assertEqual(before, {str(p): digest(p) for p in (lower, binary, source)})

    def test_graded_real_lower_hash_gate_prevents_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root) as module:
                lower = root / 'lower.json'
                lower.write_text('inert nonfrozen fixture')
                before = digest(lower)
                module.run_order = Mock(side_effect=AssertionError('science'))
                with patch.object(sys, 'argv', ['graded', '--binary', str(root / 'none'), '--lower-result', str(lower), '--output', str(root / 'new/export')]):
                    with self.assertRaisesRegex(AssertionError, 'differs from frozen result'):
                        module.main()
                module.run_order.assert_not_called()
                self.assertEqual(digest(lower), before)
                self.assertFalse((root / 'new').exists())

    def test_graded_parent_gate_and_resource_caps(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root) as module:
                runner = Mock(return_value=SimpleNamespace(stdout=json.dumps({'parent_source_sha256': 'wrong'})))
                with patch.object(module.time, 'monotonic', return_value=10), patch.object(module.subprocess, 'run', runner), patch.object(module.resource, 'setrlimit') as limit:
                    with self.assertRaisesRegex(TimeoutError, 'wall-clock cap'):
                        module.run_order(root / 'unused', 'f', 0, 10, 321)
                    runner.assert_not_called()
                    with self.assertRaisesRegex(AssertionError, 'unexpected parent source'):
                        module.run_order(root / 'unused', 'f', 0, 19, 321)
                    self.assertEqual(runner.call_args.kwargs['timeout'], 9)
                    runner.call_args.kwargs['preexec_fn']()
                    limit.assert_called_once_with(module.resource.RLIMIT_AS, (321, 321))

    def test_graded_f9_gate_prevents_second_dispatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with imported(root) as module:
                lower = root / 'lower.json'
                lower.write_text('{}')
                module.sha256 = Mock(return_value=module.EXPECTED_LOWER_SHA)
                module.run_order = Mock(return_value=([0], []))
                with patch.object(sys, 'argv', ['graded', '--binary', str(root / 'none'), '--lower-result', str(lower), '--output', str(root / 'out')]):
                    with self.assertRaisesRegex(AssertionError, 'F9 regression failed'):
                        module.main()
                module.run_order.assert_called_once()
                self.assertFalse((root / 'out').exists())

    def wrapper(self, kind):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bin_dir = root / 'bin'
            bin_dir.mkdir()
            (bin_dir / 'python').symlink_to(PRIVATE / 'record-python')
            selected = root / 'fresh root'
            accepted = True
            if kind == 'default':
                selected = None
            elif kind == 'empty':
                selected = ''
            elif kind == 'relative':
                selected = os.path.relpath(selected, LONG)
            elif kind == 'dotdot':
                selected = root / 'absent/../normalized root'
            elif kind == 'tilde':
                selected = '~/patch-acceptance-never-created'
            elif kind == 'embedded-newline':
                selected = root / 'line\ninside'
            elif kind == 'ordinary-refresh':
                selected.mkdir()
                (selected / 'REPORT.md').write_text('old separate report')
            elif kind in ('root-symlink', 'parent-symlink'):
                real = root / 'real'
                real.mkdir()
                selected.symlink_to(real, target_is_directory=True)
                if kind == 'parent-symlink':
                    selected = selected / 'new-child'
                accepted = False
            elif kind in ('child-symlink', 'dangling-child', 'hardlink'):
                source = root / 'retained'
                source.write_bytes(b'retained fixture')
                selected.mkdir()
                child = selected / 'metadata'
                child.mkdir()
                if kind == 'hardlink':
                    os.link(source, child / 'manifest.json')
                else:
                    (child / 'manifest.json').symlink_to(source if kind == 'child-symlink' else root / 'missing')
                accepted = False
            elif kind.startswith('protected-'):
                selected = REPO / kind.removeprefix('protected-')
                accepted = False
            elif kind in ('trailing-newline', 'trailing-newline-unsafe-neighbor'):
                if kind.endswith('unsafe-neighbor'):
                    real = root / 'retained-tree'
                    real.mkdir()
                    selected.symlink_to(real, target_is_directory=True)
                selected = Path(str(selected) + '\n')
            elif kind != 'test-failure':
                raise AssertionError(kind)
            log = root / 'commands.jsonl'
            env = dict(os.environ, PATH=str(bin_dir) + os.pathsep + os.environ['PATH'], PATCH_RECORD=str(log))
            env.pop('PDE_LONG_HORIZON_OUTPUT_ROOT', None)
            if selected is not None:
                env['PDE_LONG_HORIZON_OUTPUT_ROOT'] = str(selected)
            if kind == 'test-failure':
                env['PATCH_FAIL_COMMAND'] = '-m'
            result = subprocess.run(['bash', str(LONG / 'reproduce.sh')], cwd=root, env=env,
                                    capture_output=True, text=True, timeout=15)
            events = [json.loads(row) for row in log.read_text().splitlines()]
            (PRIVATE / ('wrapper-' + kind.replace('/', '_') + '.json')).write_text(json.dumps(
                {'selection': str(selected), 'returncode': result.returncode, 'events': events,
                 'stderr': result.stderr}, indent=2) + '\n')
            self.assertEqual(sum(e['event'] == 'validate' for e in events), 1)
            calls = [e for e in events if e['event'] == 'dispatch']
            if not accepted:
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(calls, [])
                return
            if kind == 'test-failure':
                self.assertEqual(result.returncode, 17)
                self.assertEqual(len(calls), 1)
                return
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(calls), 3)
            self.assertEqual(events[0]['event'], 'validate')
            self.assertEqual(events[1]['event'], 'normalized')
            normalized = events[1]['path']
            expected = str(REPO / 'data/generated/resnet_dense_long_horizon') if selected is None or selected == '' else str((LONG / Path(selected).expanduser()).resolve())
            self.assertEqual(normalized, expected)
            self.assertEqual(calls[0]['args'], ['-m', 'unittest', 'discover', '-s', 'tests', '-v'])
            for call, program in zip(calls[1:], ('run_all.py', 'make_manifest.py')):
                self.assertEqual(call['args'][0], program)
                args = call['args']
                self.assertEqual(args[args.index('--output-root') + 1], normalized)

for consumed in ('lower', 'binary', 'provenance'):
    for kind in ('same', 'symlink', 'hardlink', 'parent-symlink', 'dotdot', 'dangling', 'source-symlink'):
        setattr(Acceptance, f'test_graded_alias_{consumed}_{kind}',
                lambda self, c=consumed, k=kind: self.graded_alias(c, k))
for consumed in ('source', 'protocol'):
    for kind in ('symlink', 'hardlink', 'parent-symlink', 'dangling'):
        for long_search in (False, True):
            setattr(Acceptance, f'test_centered_alias_{consumed}_{kind}_long{long_search}',
                    lambda self, c=consumed, k=kind, l=long_search: self.centered_alias(c, k, l))
for long_search in (False, True):
    setattr(Acceptance, f'test_centered_same_directory_refresh_long{long_search}',
            lambda self, l=long_search: self.centered_refresh(l))
for kind in ('default', 'empty', 'relative', 'dotdot', 'tilde', 'embedded-newline', 'ordinary-refresh',
             'root-symlink', 'parent-symlink', 'child-symlink', 'dangling-child', 'hardlink',
             'protected-studies', 'protected-docs', 'protected-code', 'protected-.git',
             'protected-data/historical', 'protected-data/original_backups', 'protected-data/runtime_cache',
             'test-failure', 'trailing-newline', 'trailing-newline-unsafe-neighbor'):
    setattr(Acceptance, 'test_wrapper_' + kind.replace('/', '_'), lambda self, k=kind: self.wrapper(k))

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Acceptance)
    with (PRIVATE / 'independent-tests.log').open('w') as stream:
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    summary = dict(total=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                   skipped=len(result.skipped), failing_tests=[test.id() for test, _ in result.failures])
    (PRIVATE / 'independent-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary))
    sys.exit(not result.wasSuccessful())
