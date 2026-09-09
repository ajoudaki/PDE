"""Private path-only acceptance: no scientific module imports or seal verification."""
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
from types import ModuleType, SimpleNamespace
import unittest
from unittest import mock

REPO = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).resolve().parent
os.chdir(PRIVATE)
tempfile.tempdir = str(PRIVATE)
G = REPO / 'studies/resnet_generalization/analyze_generalization.py'
A = REPO / 'studies/resnet_activation_controls/analyze_activation.py'
W = REPO / 'studies/resnet_activation_controls/run_experiment.py'
EXPECTED = {
    G: 'b989f077294a9e19c0ccd0eecb22a4eece2f2af8299426dd71815ea8aac39005',
    A: 'ae29dac3ee9ac9a9796d8a75a9a2d14dea4aea1bfe74bf040a969cc567fdf5de',
    W: '8f4db13f1a5102978ee8166a9df47988ddbdbaed744e1f74941e79de2771e62d',
    G.parent / 'tests/test_writer_boundaries.py': '68513deb326e99895b7f9a047ecff9db1b7930a4324c23be2761f2ce8d25cc97',
    A.parent / 'tests/test_migration_boundaries.py': '542b38c681217f5847168cce49da2ccedb3652af49abe35d753afea91d3362e9',
    G.parent / 'generalization_paths.py': 'ccc364726bdce39dccd5fcc12559e1d628aa25db93e57ee9e511fa5176927b70',
    A.parent / 'output_paths.py': 'dbd1ee0dac8b349b34fa32846ef637db0c4259cceeb9a0a75bffdde83191da91',
    REPO / 'studies/_output_paths.py': '8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def guard_event(event, args):
    if event in ('subprocess.Popen', 'os.system', 'os.fork', 'os.posix_spawn', 'socket.connect'):
        raise AssertionError(f'forbidden execution: {event}')
    if event == 'open' and isinstance(args[0], (str, bytes, os.PathLike)):
        path = Path(os.fsdecode(args[0])).absolute()
        mode = args[1] or ''
        flags = args[2] or 0
        writing = any(c in mode for c in 'wax+') or flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)
        if path.is_relative_to(REPO):
            if writing or path not in EXPECTED:
                raise AssertionError(f'out-of-scope repository open: {path}')
        if writing and not path.is_relative_to(PRIVATE):
            raise AssertionError(f'write outside private directory: {path}')
    if event in ('os.mkdir', 'os.link', 'os.symlink', 'os.rename', 'os.remove', 'os.rmdir'):
        targets = args[:2] if event == 'os.rename' else (args[1],) if event in ('os.link', 'os.symlink') else args[:1]
        for value in targets:
            if isinstance(value, (str, bytes, os.PathLike)):
                path = Path(os.fsdecode(value))
                if path.is_absolute() and not path.is_relative_to(PRIVATE):
                    raise AssertionError(f'mutation outside private directory: {event}: {path}')


sys.addaudithook(guard_event)
BEFORE = {str(p.relative_to(REPO)): digest(p) for p in EXPECTED}
assert all(BEFORE[str(p.relative_to(REPO))] == expected for p, expected in EXPECTED.items())


def module(name, path):
    value = ModuleType(name)
    value.__file__ = str(path)
    sys.modules[name] = value
    # Execute only permitted path-helper modules; no package initializers.
    exec(compile(path.read_text(), str(path), 'exec'), value.__dict__)
    return value


shared = module('studies._output_paths', REPO / 'studies/_output_paths.py')
gp = module('private_generalization_paths', G.parent / 'generalization_paths.py')
ap = module('private_activation_paths', A.parent / 'output_paths.py')


def extract(path, names, env, classes=False):
    types = (ast.FunctionDef, ast.ClassDef) if classes else (ast.FunctionDef,)
    nodes = [n for n in ast.parse(path.read_text()).body if isinstance(n, types) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), 'exec'), env)
    return env


GN = ('summary.json', 'case_metrics.csv', 'numerical_metrics.csv', 'plateau_metrics.csv')
GF = ('all_case_errors.png', 'loss_curves.png', 'gram_motion_curves.png')
AN = ('summary.json', 'metrics.csv', 'figure_time_curves.csv', 'figure_gram_depth_curves.csv',
      'figure_activation_evidence.csv', 'figure_progress_gram_paths.csv',
      'figure_depth_width_controls.csv', 'figure_bootstrap_intervals.csv', 'figure_cross_prediction.csv')


def arguments(study, root):
    if study == 'g':
        return SimpleNamespace(root=root / 'source', results_dir=root / 'evidence/results/generalization',
                               output_dir=root / 'products', figures_dir=root / 'figures', report=root / 'REPORT.md')
    return SimpleNamespace(root=root / 'source', protocol=root / 'explicit/protocol.dat',
                           cases=root / 'explicit/cases.dat', pde_dir=root / 'pde-selection/evidence',
                           dense_dir=root / 'separate-dense/evidence', output_dir=root / 'products')


def outputs(study, args):
    if study == 'a':
        return [args.output_dir / n for n in AN]
    return [*(args.output_dir / n for n in GN), *(args.figures_dir / n for n in GF),
            args.report, args.results_dir / 'PROCESSED_STAGE_SEAL.json']


class StopIngestion(Exception):
    pass


def entry(study, source=None):
    path = G if study == 'g' else A
    loader = mock.Mock(side_effect=StopIngestion('first ingestion tripwire'))
    env = dict(Path=Path, require_output=gp.require_output if study == 'g' else ap.require_output,
               _json=loader, __file__=str(source or path))
    extract(path, {'run_analysis', '_preflight_analysis_outputs'}, env)
    return env, loader


def retain(path, payload=b'inert bytes; not a protocol, archive, or seal'):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


class Independent(unittest.TestCase):
    def refuse(self, study, args, source=None, error=ValueError):
        env, loader = entry(study, source)
        with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaises(error):
            env['run_analysis'](args)
        loader.assert_not_called()
        mkdir.assert_not_called()

    def test_generalization_input_roles_cross_all_finals_and_partials(self):
        roles = [('root', 'protocol/' + n) for n in (
            'generalization_protocol.json', 'analysis_plan.json', 'cases.json',
            'FROZEN_DYNAMICS_MANIFEST.json', 'run_grid.py')]
        roles += [('root', 'pde_precheck.py')]
        roles += [('results_dir', n) for n in ('PDE_STAGE_SEAL.json', 'DENSE_STAGE_SEAL.json', 'pde_numerical_decision.json')]
        roles += [('results_dir', n + '/inert.npz') for n in (
            'pde_primary', 'pde_scramble', 'pde_audits', 'pde_fallback', 'dense_screen', 'dense_confirm', 'dense_depth')]
        for role, name in roles:
            for i in range(9):
                for suffix in ('', '.partial'):
                    with self.subTest(role=name, output=i, suffix=suffix), tempfile.TemporaryDirectory() as tmp:
                        args = arguments('g', Path(tmp))
                        target = outputs('g', args)[i]
                        target = target.with_name(target.name + suffix)
                        retain(target)
                        before = digest(target)
                        selected = getattr(args, role) / name
                        selected.parent.mkdir(parents=True, exist_ok=True)
                        selected.symlink_to(target)
                        self.refuse('g', args)
                        self.assertEqual(digest(target), before)

    def test_activation_seals_use_pde_parent_even_with_separate_dense_parent(self):
        for role in ('PDE_STAGE_SEAL.json', 'DENSE_STAGE_SEAL.json', 'pde-archive', 'dense-archive'):
            for i in range(9):
                for suffix in ('', '.partial'):
                    with self.subTest(role=role, output=i, suffix=suffix), tempfile.TemporaryDirectory() as tmp:
                        args = arguments('a', Path(tmp))
                        target = outputs('a', args)[i]
                        target = target.with_name(target.name + suffix)
                        retain(target)
                        before = digest(target)
                        source = args.pde_dir / 'inert.npz' if role == 'pde-archive' else args.dense_dir / 'inert.npz' if role == 'dense-archive' else args.pde_dir.parent / role
                        source.parent.mkdir(parents=True, exist_ok=True)
                        source.symlink_to(target)
                        self.refuse('a', args)
                        self.assertEqual(digest(target), before)

    def test_analyzer_source_role_uses_file_global_for_every_destination(self):
        for study in ('g', 'a'):
            for i in range(9):
                for suffix in ('', '.partial'):
                    with self.subTest(study=study, output=i, suffix=suffix), tempfile.TemporaryDirectory() as tmp:
                        args = arguments(study, Path(tmp))
                        target = outputs(study, args)[i]
                        target = target.with_name(target.name + suffix)
                        retain(target)
                        before = digest(target)
                        # Inert __file__ stand-in exercises this declaration role without touching source inodes.
                        self.refuse(study, args, source=target)
                        self.assertEqual(digest(target), before)

    def test_absent_selected_input_identity_still_refuses(self):
        for study in ('g', 'a'):
            for suffix in ('', '.partial'):
                with self.subTest(study=study, suffix=suffix), tempfile.TemporaryDirectory() as tmp:
                    args = arguments(study, Path(tmp))
                    if study == 'g':
                        args.report = args.root / 'protocol/cases.json'
                    else:
                        args.cases = args.output_dir / ('summary.json' + suffix)
                    self.refuse(study, args)
                    self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_original_spelling_survives_parent_dotdot_link(self):
        for study, fields in (('g', ('results_dir', 'output_dir', 'figures_dir', 'report')), ('a', ('output_dir',))):
            for field in fields:
                with self.subTest(study=study, field=field), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    args = arguments(study, root)
                    (root / 'actual').mkdir()
                    (root / 'alias').symlink_to(root / 'actual', target_is_directory=True)
                    setattr(args, field, root / 'alias' / '..' / getattr(args, field).name)
                    self.refuse(study, args)

    def test_all_named_link_occupancy_kinds(self):
        for study in ('g', 'a'):
            for i in range(9):
                for suffix in ('', '.partial'):
                    for kind in ('symlink', 'dangling', 'hardlink'):
                        with self.subTest(study=study, output=i, suffix=suffix, kind=kind), tempfile.TemporaryDirectory() as tmp:
                            args = arguments(study, Path(tmp))
                            source = Path(tmp) / 'retained'
                            retain(source)
                            before = digest(source)
                            target = outputs(study, args)[i]
                            target = target.with_name(target.name + suffix)
                            target.parent.mkdir(parents=True, exist_ok=True)
                            if kind == 'hardlink':
                                os.link(source, target)
                            else:
                                target.symlink_to(Path(tmp) / 'absent' if kind == 'dangling' else source)
                            self.refuse(study, args)
                            self.assertEqual(digest(source), before)

    def test_all_generalization_report_endpoint_collisions(self):
        for i in (*range(7), 8):
            for suffix in ('', '.partial'):
                with self.subTest(output=i, suffix=suffix), tempfile.TemporaryDirectory() as tmp:
                    args = arguments('g', Path(tmp))
                    target = outputs('g', args)[i]
                    args.report = target.with_name(target.name + suffix)
                    self.refuse('g', args)
                    self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_generalization_named_file_destinations_cannot_be_ancestors(self):
        for layout in ('report-is-output-parent', 'report-below-summary', 'figures-below-summary', 'output-below-report-partial'):
            with self.subTest(layout=layout), tempfile.TemporaryDirectory() as tmp:
                args = arguments('g', Path(tmp))
                if layout == 'report-is-output-parent':
                    args.report = args.output_dir
                elif layout == 'report-below-summary':
                    args.report = args.output_dir / 'summary.json' / 'report.md'
                elif layout == 'figures-below-summary':
                    args.figures_dir = args.output_dir / 'summary.json'
                else:
                    args.output_dir = args.report.with_name(args.report.name + '.partial') / 'products'
                self.refuse('g', args)
                self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_mapped_input_spellings_and_link_identity_both_stages(self):
        for stage in (0, 1):
            for field in ('source_files', 'protocol_files', 'execution_files'):
                for i in range(9):
                    for suffix in ('', '.partial'):
                        for spelling in ('absolute', 'parent-relative', 'source-symlink'):
                            with self.subTest(stage=stage, field=field, output=i, suffix=suffix, spelling=spelling), tempfile.TemporaryDirectory() as tmp:
                                args = arguments('a', Path(tmp))
                                target = outputs('a', args)[i]
                                target = target.with_name(target.name + suffix)
                                retain(target)
                                before = digest(target)
                                key = str(target) if spelling == 'absolute' else '../products/' + target.name
                                if spelling == 'source-symlink':
                                    selected = args.root / 'mapped-source'
                                    selected.parent.mkdir(parents=True, exist_ok=True)
                                    selected.symlink_to(target)
                                    key = 'mapped-source'
                                records = [{}, {}]
                                records[stage][field] = {key: 'INERT; NOT A DIGEST'}
                                env, loader = entry('a')
                                with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaises(ValueError):
                                    env['_preflight_analysis_outputs'](args, records)
                                mkdir.assert_not_called()
                                loader.assert_not_called()
                                self.assertEqual(digest(target), before)

    def test_guards_recheck_changed_private_paths(self):
        for study in ('g', 'a'):
            for i in range(9):
                with self.subTest(study=study, output=i), tempfile.TemporaryDirectory() as tmp:
                    args = arguments(study, Path(tmp))
                    env, loader = entry(study)
                    env['_preflight_analysis_outputs'](args)
                    target = outputs(study, args)[i]
                    partial = target.with_name(target.name + '.partial')
                    retain(partial, b'occupied after previous guard')
                    with self.assertRaises(FileExistsError):
                        env['_preflight_analysis_outputs'](args)
                    loader.assert_not_called()
                    self.assertEqual(partial.read_bytes(), b'occupied after previous guard')
                    self.assertFalse(target.exists())

    def test_ordinary_distinct_products_reach_first_read_and_preserve_bytes(self):
        for study in ('g', 'a'):
            with self.subTest(study=study), tempfile.TemporaryDirectory() as tmp:
                args = arguments(study, Path(tmp))
                targets = outputs(study, args)
                for path in targets:
                    retain(path, b'old ordinary product')
                before = {str(p): digest(p) for p in targets}
                env, loader = entry(study)
                with mock.patch.object(Path, 'mkdir') as mkdir, self.assertRaises(StopIngestion):
                    env['run_analysis'](args)
                loader.assert_called_once_with(args.root / 'protocol/generalization_protocol.json' if study == 'g' else args.protocol)
                mkdir.assert_not_called()
                self.assertEqual(before, {str(p): digest(p) for p in targets})

    def test_real_refresh_writers_and_write_once_changed_final(self):
        gen = extract(G, {'_atomic_bytes', '_atomic_figure'}, dict(Path=Path, os=os, require_output=gp.require_output, plt=mock.Mock()))
        act = extract(A, {'_atomic_text'}, dict(Path=Path, os=os, require_output=ap.require_output))
        once = extract(W, {'_write_once', '_encoded'}, dict(Path=Path, os=os, json=json, require_output=ap.require_output, IntegrityError=RuntimeError))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'ordinary.dat'
            for writer, first, second in ((gen['_atomic_bytes'], b'first', b'second'), (act['_atomic_text'], 'first', 'second')):
                writer(path, first)
                writer(path, second)
                self.assertEqual(path.read_bytes(), b'second')
            fig = mock.Mock()
            fig.savefig.side_effect = lambda handle, **kw: handle.write(b'inert figure bytes')
            gen['_atomic_figure'](path, fig)
            self.assertEqual(path.read_bytes(), b'inert figure bytes')
            out = Path(tmp) / 'once.json'
            once['_write_once'](out, {'inert': 1})
            state = (out.read_bytes(), out.stat().st_ino, out.stat().st_mtime_ns)
            once['_write_once'](out, {'inert': 1})
            self.assertEqual((out.read_bytes(), out.stat().st_ino, out.stat().st_mtime_ns), state)
            with self.assertRaisesRegex(RuntimeError, 'changed record'):
                once['_write_once'](out, {'inert': 2})
            self.assertEqual((out.read_bytes(), out.stat().st_ino, out.stat().st_mtime_ns), state)
            self.assertFalse(out.with_suffix('.json.partial').exists())

    def test_identical_final_with_occupied_partial_refuses_before_final_read(self):
        env = extract(W, {'_write_once', '_encoded'}, dict(Path=Path, os=os, json=json, require_output=ap.require_output, IntegrityError=RuntimeError))
        for kind in ('ordinary', 'directory', 'symlink', 'dangling', 'hardlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp) / 'record.json'
                env['_write_once'](path, {'inert': True})
                before = digest(path)
                partial = path.with_suffix('.json.partial')
                source = Path(tmp) / 'retained'
                retain(source)
                if kind == 'ordinary':
                    retain(partial, b'stale')
                elif kind == 'directory':
                    partial.mkdir()
                elif kind == 'hardlink':
                    os.link(source, partial)
                else:
                    partial.symlink_to(Path(tmp) / 'absent' if kind == 'dangling' else source)
                with mock.patch.object(Path, 'read_text', side_effect=AssertionError('final read before partial refusal')), self.assertRaises((ValueError, RuntimeError)):
                    env['_write_once'](path, {'inert': True})
                self.assertEqual(digest(path), before)


def focused_suite():
    env = dict(globals(), ROOT=G.parent, paths=gp)
    extract(G.parent / 'tests/test_writer_boundaries.py', {'functions', 'WriterBoundaryTests', 'AnalysisRoutingTests'}, env, classes=True)
    suite = unittest.TestSuite()
    for name in ('test_analysis_writers_preserve_colliding_intermediates_and_targets',
                 'test_analysis_writers_validate_before_mkdir_and_accept_regular_replacement'):
        suite.addTest(env['WriterBoundaryTests'](name))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(env['AnalysisRoutingTests']))
    env = dict(globals(), ROOT=A.parent, require_output=ap.require_output)
    extract(A.parent / 'tests/test_migration_boundaries.py', {'functions', 'MigrationBoundaryTests', 'AnalysisRoutingTests'}, env, classes=True)
    for name in unittest.defaultTestLoader.getTestCaseNames(env['MigrationBoundaryTests']):
        if name != 'test_seal_label_consumer_uses_producers_generated_evidence_root':
            suite.addTest(env['MigrationBoundaryTests'](name))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(env['AnalysisRoutingTests']))
    return suite


class CountingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subtests = 0

    def addSubTest(self, test, subtest, err):
        self.subtests += 1
        super().addSubTest(test, subtest, err)


if __name__ == '__main__':
    suite = focused_suite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Independent))
    log_path = PRIVATE / 'test-results.txt'
    with log_path.open('x') as log, contextlib.redirect_stdout(log), contextlib.redirect_stderr(log):
        print('PRIVATE_DIRECTORY', PRIVATE)
        print('BEFORE_SHA256', json.dumps(BEFORE, sort_keys=True))
        result = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=CountingResult).run(suite)
        AFTER = {str(p.relative_to(REPO)): digest(p) for p in EXPECTED}
        print('AFTER_SHA256', json.dumps(AFTER, sort_keys=True))
        summary = dict(tests=result.testsRun, subtests=result.subtests,
                       failures=len(result.failures), errors=len(result.errors), unchanged=BEFORE == AFTER)
        print('RESULT', json.dumps(summary))
    print('LOG', log_path)
    print('RESULT', json.dumps(summary))
    for test, trace in result.failures + result.errors:
        print('FAILURE', str(test), trace[-900:])
    assert BEFORE == AFTER
    sys.exit(0 if result.wasSuccessful() else 1)
