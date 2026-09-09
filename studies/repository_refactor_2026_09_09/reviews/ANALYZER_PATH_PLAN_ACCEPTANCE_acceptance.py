"""Private, inert acceptance harness. Reads only the four permitted sources."""
import argparse
import ast
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock
from itertools import chain

PRIVATE = Path(__file__).resolve().parent
REPO = Path('/home/amir/Codes/PDE')
ANALYSIS = REPO / 'studies/resnet_generalization/analyze_generalization.py'
HELPER = REPO / 'studies/resnet_generalization/generalization_paths.py'
SHARED = REPO / 'studies/_output_paths.py'
TESTS = REPO / 'studies/resnet_generalization/tests/test_writer_boundaries.py'
FILES = (ANALYSIS, HELPER, SHARED, TESTS)
EXPECTED = {
    ANALYSIS: 'a9a5385d8cb9482b35763c123ddae3c8adb2915a6f92ccd8304605e08b63199b',
    HELPER: 'ccc364726bdce39dccd5fcc12559e1d628aa25db93e57ee9e511fa5176927b70',
    SHARED: '8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e',
    TESTS: 'caa46839e81ebcc05cfc650b045c48abe31b0634af55df6a3d79376372b4f91f',
}
before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES}
assert before == EXPECTED, 'Frozen source changed before execution'
tempfile.tempdir = str(PRIVATE)


def execute_nodes(nodes, filename, env):
    # In-memory AST execution only: no module import/build or bytecode files.
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    module = ast.fix_missing_locations(ast.Module(body=[future, *copy.deepcopy(nodes)], type_ignores=[]))
    exec(compile(module, str(filename), 'exec'), env)
    return env


shared_tree = ast.parse(SHARED.read_text())
link_node = next(n for n in shared_tree.body if isinstance(n, ast.FunctionDef) and n.name == 'reject_output_links')
shared_env = execute_nodes([link_node], SHARED, {'Path': Path, 'chain': chain})
helper_tree = ast.parse(HELPER.read_text())
constant_names = {'STUDY_ROOT', 'REPO_ROOT', 'GENERATED_ROOT', 'RESULTS', 'HISTORICAL_RESULTS'}
helper_nodes = [n for n in helper_tree.body if (
    isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in constant_names for t in n.targets)
) or (isinstance(n, ast.FunctionDef) and n.name == 'require_output')]
helper_env = execute_nodes(helper_nodes, HELPER, {
    'Path': Path, '__file__': str(HELPER), 'reject_output_links': shared_env['reject_output_links'],
})
paths = SimpleNamespace(**{k: v for k, v in helper_env.items() if not k.startswith('__')})
tree = ast.parse(ANALYSIS.read_text())
nodes = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
run_node = nodes['run_analysis']
guard_indices = [i for i, n in enumerate(run_node.body) if (
    isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)
    and isinstance(n.value.func, ast.Name) and n.value.func.id == '_preflight_analysis_outputs'
)]
assert len(guard_indices) == 2
first_guard, second_guard = guard_indices
suffix = copy.deepcopy(run_node)
suffix.name = 'publication_suffix'
suffix.body = suffix.body[second_guard:]


class ReachedBoundary(RuntimeError):
    pass


def reached_ingestion(*args, **kwargs):
    raise ReachedBoundary('ingestion')


def reached_publication(*args, **kwargs):
    raise ReachedBoundary('publication')


env = execute_nodes([nodes['_preflight_analysis_outputs'], run_node, suffix], ANALYSIS, {
    'Path': Path, '__file__': str(ANALYSIS), 'require_output': paths.require_output,
    '_json': reached_ingestion, '_figures': reached_publication,
})


def defaults(root):
    return SimpleNamespace(root=root/'source', results_dir=root/'results/generalization',
                           output_dir=root/'processed', figures_dir=root/'figures',
                           report=root/'REPORT.md', bootstrap_replicates=2000)


def finals(a):
    # Independent contract inventory, not extracted from the guard under test.
    return [a.output_dir/n for n in ('summary.json', 'case_metrics.csv', 'numerical_metrics.csv', 'plateau_metrics.csv')] + [
        a.figures_dir/n for n in ('all_case_errors.png', 'loss_curves.png', 'gram_motion_curves.png')
    ] + [a.report, a.results_dir/'PROCESSED_STAGE_SEAL.json']


def targets(a):
    return [t for p in finals(a) for t in (p, p.with_name(p.name+'.partial'))]


def snapshot(root):
    answer = {}
    for p in sorted(root.rglob('*')):
        s = p.lstat()
        kind = stat.S_IFMT(s.st_mode)
        payload = os.readlink(p) if stat.S_ISLNK(s.st_mode) else (
            hashlib.sha256(p.read_bytes()).hexdigest() if stat.S_ISREG(s.st_mode) else None)
        answer[str(p.relative_to(root))] = (kind, s.st_mode, s.st_ino, s.st_nlink, payload)
    return answer


def invoke(mode, a):
    if mode == 'preflight':
        return env['_preflight_analysis_outputs'](a)
    if mode == 'entry':
        return env['run_analysis'](a)
    env.update(root=a.root.resolve(), results=a.results_dir.resolve(), output=a.output_dir.resolve(),
               figures_dir=a.figures_dir.resolve(), report_path=a.report.resolve(), records={}, curves={})
    return env['publication_suffix'](a)


records = []


def probe(label, setup=lambda a, r: None, valid=False, error=None):
    with tempfile.TemporaryDirectory(prefix='probe-', dir=PRIVATE) as d:
        root = Path(d)
        a = defaults(root)
        cleanup = setup(a, root)
        saved = snapshot(root)
        outcomes = {}
        try:
            for mode in ('preflight', 'entry', 'publication'):
                with contextlib.ExitStack() as stack:
                    for name in ('mkdir', 'open', 'write_bytes', 'write_text', 'touch', 'unlink', 'rename', 'replace'):
                        stack.enter_context(mock.patch.object(Path, name, side_effect=AssertionError('filesystem write/read tripwire: '+name)))
                    stack.enter_context(mock.patch('builtins.open', side_effect=AssertionError('file ingestion/publication tripwire')))
                    stack.enter_context(mock.patch.object(os, 'replace', side_effect=AssertionError('publication tripwire')))
                    try:
                        invoke(mode, a)
                    except ReachedBoundary as exc:
                        expected = 'ingestion' if mode == 'entry' else 'publication'
                        assert valid and mode != 'preflight' and str(exc) == expected, (label, mode, str(exc))
                        outcomes[mode] = 'reached '+str(exc)+' tripwire'
                    except (ValueError, FileExistsError) as exc:
                        assert not valid, (label, mode, str(exc))
                        if error is not None:
                            assert isinstance(exc, error), (label, mode, type(exc).__name__)
                        outcomes[mode] = type(exc).__name__+': '+str(exc)
                    else:
                        assert valid and mode == 'preflight', (label, mode, 'unexpected acceptance')
                        outcomes[mode] = 'accepted'
                assert snapshot(root) == saved, (label, mode, 'fixture changed')
            records.append({'label': label, 'expected': 'accept' if valid else 'reject', 'outcomes': outcomes,
                            'all_fixture_metadata_and_regular_file_hashes_unchanged': True})
        finally:
            if cleanup:
                cleanup()


# Four specified invalid layouts, including the reverse-order partial ancestor.
probe('representative/report=output_dir', lambda a, r: setattr(a, 'report', a.output_dir))
probe('representative/report=output_dir/summary.json/report.md', lambda a, r: setattr(a, 'report', a.output_dir/'summary.json/report.md'))
probe('representative/figures_dir=output_dir/summary.json', lambda a, r: setattr(a, 'figures_dir', a.output_dir/'summary.json'))
probe('representative/output_dir=report.partial/products', lambda a, r: setattr(a, 'output_dir', a.report.with_name(a.report.name+'.partial')/'products'))

# All other named files and partials against the independently selectable report.
for index in (*range(7), 8):
    for partial in (False, True):
        for relation in ('equal', 'descendant', 'ancestor'):
            def setup(a, r, index=index, partial=partial, relation=relation):
                t = finals(a)[index]
                if partial:
                    t = t.with_name(t.name+'.partial')
                a.report = t if relation == 'equal' else (t/'report.md' if relation == 'descendant' else t.parent)
            probe(f'prefix/report-{relation}-target-{index}-partial-{partial}', setup)

for field in ('output_dir', 'figures_dir', 'results_dir'):
    for partial in (False, True):
        def setup(a, r, field=field, partial=partial):
            t = a.report.with_name(a.report.name+'.partial') if partial else a.report
            setattr(a, field, t/'products')
        probe(f'prefix/{field}-below-report-partial-{partial}', setup)

# Every final/partial must have a file role; directories and FIFOs are inert.
for index in range(18):
    for kind in ('directory', 'fifo'):
        def setup(a, r, index=index, kind=kind):
            t = targets(a)[index]
            t.parent.mkdir(parents=True, exist_ok=True)
            if kind == 'directory':
                t.mkdir()
                (t/'retained').write_bytes(b'unchanged directory contents')
            elif kind == 'fifo':
                os.mkfifo(t)
        probe(f'role/{kind}-target-{index}', setup)

for field in ('output_dir', 'figures_dir', 'results_dir', 'report'):
    for kind in ('file', 'fifo'):
        for depth in (0, 2):
            def setup(a, r, field=field, kind=kind, depth=depth):
                blocker = r/'blocker'
                cleanup = None
                if kind == 'file':
                    blocker.write_bytes(b'unchanged blocking file')
                elif kind == 'fifo':
                    os.mkfifo(blocker)
                setattr(a, field, blocker.joinpath(*(['missing']*depth), 'selected'))
                return cleanup
            probe(f'parent/{field}-{kind}-depth-{depth}', setup)

# Links in the original spelling, including '..', dangling links, and hardlinks.
for field in ('output_dir', 'figures_dir', 'results_dir', 'report'):
    for variant in ('live', 'dangling', 'dotdot'):
        def setup(a, r, field=field, variant=variant):
            real = r/'real'
            real.mkdir()
            alias = r/'alias'
            alias.symlink_to(real if variant != 'dangling' else r/'absent', target_is_directory=True)
            setattr(a, field, alias/('..' if variant == 'dotdot' else 'child')/'selected')
        probe(f'selected-link/{field}-{variant}', setup)

for index in range(18):
    for kind in ('symlink', 'dangling', 'hardlink'):
        def setup(a, r, index=index, kind=kind):
            t = targets(a)[index]
            t.parent.mkdir(parents=True, exist_ok=True)
            source = r/'inert-link-target'
            if kind != 'dangling':
                source.write_bytes(b'unchanged linked data')
            if kind == 'hardlink':
                os.link(source, t)
            else:
                t.symlink_to(source)
        probe(f'link/{kind}-target-{index}', setup)

for index in range(9):
    def setup(a, r, index=index):
        t = finals(a)[index]
        p = t.with_name(t.name+'.partial')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b'retained occupied partial')
    probe(f'occupied-partial/{index}', setup, error=FileExistsError)

# Independent source identity probes (both present and absent named inputs).
inputs = [('root', n) for n in ('protocol/generalization_protocol.json', 'protocol/analysis_plan.json',
          'protocol/cases.json', 'protocol/FROZEN_DYNAMICS_MANIFEST.json', 'protocol/run_grid.py', 'pde_precheck.py')]
inputs += [('results_dir', n) for n in ('PDE_STAGE_SEAL.json', 'DENSE_STAGE_SEAL.json', 'pde_numerical_decision.json')]
for field, name in inputs:
    for present in (False, True):
        def setup(a, r, field=field, name=name, present=present):
            source = getattr(a, field)/name
            if present:
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_bytes(b'inert input, never ingested')
            a.report = source
        probe(f'input/{field}/{name}/present-{present}', setup)

for index in range(18):
    def setup(a, r, index=index):
        t = targets(a)[index]
        t.parent.mkdir(parents=True, exist_ok=True)
        t.write_bytes(b'inert input identity')
        source = a.root/'protocol/cases.json'
        source.parent.mkdir(parents=True, exist_ok=True)
        source.symlink_to(t)
    probe(f'input/resolved-source-equals-target-{index}', setup)

for directory in ('pde_primary', 'pde_scramble', 'pde_audits', 'pde_fallback', 'dense_screen', 'dense_confirm', 'dense_depth', 'extra/nested'):
    def setup(a, r, directory=directory):
        a.report = a.results_dir/directory/'inert.npz'
        a.report.parent.mkdir(parents=True, exist_ok=True)
        a.report.write_bytes(b'not an archive; never loaded')
    probe(f'input/archive/{directory}', setup)

probe('input/analyzer-source', lambda a, r: setattr(a, 'report', ANALYSIS))

# Compatibility: distinct file products may share/nest directories freely.
valid_layouts = {
    'default': lambda a, r: None,
    'all-share-directory': lambda a, r: (setattr(a, 'output_dir', a.results_dir), setattr(a, 'figures_dir', a.results_dir), setattr(a, 'report', a.results_dir/'REPORT.md')),
    'report-nested-under-output': lambda a, r: setattr(a, 'report', a.output_dir/'reports/review/REPORT.md'),
    'report-nested-under-figures': lambda a, r: setattr(a, 'report', a.figures_dir/'reports/review/REPORT.md'),
    'figures-nested-under-report-directory': lambda a, r: (setattr(a, 'report', a.output_dir/'reports/REPORT.md'), setattr(a, 'figures_dir', a.output_dir/'reports/images')),
    'sibling-string-prefixes': lambda a, r: (setattr(a, 'report', a.output_dir/'summary.json-report.md'), setattr(a, 'figures_dir', a.output_dir/'summary.json.partial-extra/images')),
    'report-inside-directory-with-partial-suffix': lambda a, r: setattr(a, 'report', a.output_dir/'notes.partial/review.md'),
    'report-partial-suffix-filename': lambda a, r: setattr(a, 'report', a.output_dir/'review.partial'),
    'ordinary-dotdot': lambda a, r: setattr(a, 'report', a.output_dir/'unused/../reports/REPORT.md'),
}
for label, layout in valid_layouts.items():
    for existing in (False, True):
        def setup(a, r, layout=layout, existing=existing):
            layout(a, r)
            if existing:
                for t in finals(a):
                    t.parent.mkdir(parents=True, exist_ok=True)
                    t.write_bytes(b'replaceable ordinary product')
        probe(f'compatible/{label}/existing-{existing}', setup, valid=True)

# Actual AST publications: independent file-name inventory and both boundaries.
calls = sorted([n for n in ast.walk(run_node) if isinstance(n, ast.Call)], key=lambda n: n.lineno)
guard_lines = [run_node.body[i].lineno for i in guard_indices]
assert guard_lines == [1470, 1841]
assert min(n.lineno for n in calls if isinstance(n.func, ast.Name) and n.func.id == '_json') == 1471
publication_names = {'_figures', '_atomic_text', '_atomic_csv', '_write_processed_seal'}
publication_calls = [n for n in calls if isinstance(n.func, ast.Name) and n.func.id in publication_names]
assert min(n.lineno for n in publication_calls) == 1842
assert isinstance(run_node.body[second_guard+1], ast.Assign)
assert ast.unparse(run_node.body[second_guard+1].value) == '_figures(records, curves, figures_dir)'
assert [ast.unparse(n.args[0]) for n in publication_calls if n.func.id in {'_atomic_text', '_atomic_csv'}] == [
    "output / 'summary.json'", "output / 'case_metrics.csv'", "output / 'numerical_metrics.csv'",
    "output / 'plateau_metrics.csv'", 'report_path']
figure_ast = ast.unparse(nodes['_figures'])
assert "error_path = output / 'all_case_errors.png'" in figure_ast
assert "path = output / f'{name}_curves.png'" in figure_ast
assert "loss_path = curve_grid('loss', 'loss of predictor')" in figure_ast
assert "gram_path = curve_grid('gram_motion', 'max-depth Gram increment norm')" in figure_ast
seal_calls = [n for n in ast.walk(nodes['_write_processed_seal']) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == '_atomic_text']
assert len(seal_calls) == 1 and ast.unparse(seal_calls[0].args[0]) == "results / 'PROCESSED_STAGE_SEAL.json'"
for writer in ('_atomic_bytes', '_atomic_figure'):
    text = ast.unparse(nodes[writer])
    assert "partial = path.with_name(path.name + '.partial')" in text
    assert "with partial.open('xb') as handle:" in text
    assert 'os.replace(partial, path)' in text

# Trace the unchanged publication suffix with inert writers; never publish files/seals.
with tempfile.TemporaryDirectory(prefix='publication-trace-', dir=PRIVATE) as d:
    a = defaults(Path(d))
    trace = []
    def fake_figures(records, curves, directory):
        found = [directory/n for n in ('all_case_errors.png', 'loss_curves.png', 'gram_motion_curves.png')]
        trace.extend(('figure', str(p)) for p in found)
        return [str(p) for p in found]
    def fake_atomic(path, value):
        trace.append(('file', str(path)))
    def fake_seal(**kwargs):
        trace.append(('seal', str(kwargs['results']/'PROCESSED_STAGE_SEAL.json')))
        assert {str(p) for p in kwargs['deliverables']} == {str(p) for p in finals(a)[:-1]}
    env.update(_figures=fake_figures, _atomic_text=fake_atomic, _atomic_csv=fake_atomic,
               _write_processed_seal=fake_seal, _report=lambda value: 'inert report',
               evidence_label=lambda path, results: str(path), json=json, summary={},
               rows=[], numerical_rows=[], plateau_rows=[], dynamics_hash='inert',
               seal_hash='inert', dense_seal_hash='inert')
    with mock.patch.object(Path, 'mkdir', side_effect=AssertionError('write tripwire')), \
         mock.patch.object(Path, 'open', side_effect=AssertionError('file tripwire')), \
         mock.patch('builtins.open', side_effect=AssertionError('file tripwire')), \
         mock.patch.object(os, 'replace', side_effect=AssertionError('publish tripwire')):
        invoke('publication', a)
    assert {p for kind, p in trace} == {str(p) for p in finals(a)}
    assert len(trace) == 9 and not list(Path(d).iterdir())

# Execute only frozen AnalysisRoutingTests and the necessary functions() scaffold.
# No numpy or analyzer module import; no WriterBoundaryTests loaded/executed.
test_lines = TESTS.read_text().splitlines(keepends=True)
selected_text = ''.join(test_lines[22:30] + test_lines[158:350])
selected_tree = ast.parse(selected_text)
test_nodes = [n for n in selected_tree.body if (
    isinstance(n, ast.FunctionDef) and n.name == 'functions'
) or (isinstance(n, ast.ClassDef) and n.name == 'AnalysisRoutingTests')]
assert len(test_nodes) == 2
test_env = execute_nodes(test_nodes, TESTS, dict(
    Path=Path, ast=ast, SimpleNamespace=SimpleNamespace, unittest=unittest,
    mock=mock, tempfile=tempfile, os=os, ROOT=ANALYSIS.parent, paths=paths,
))
stream = io.StringIO()
suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_env['AnalysisRoutingTests'])
routing = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
after = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES}
assert before == after, 'Source hash changed during acceptance'
assert routing.wasSuccessful(), stream.getvalue()
assert 'numpy' not in sys.modules and 'matplotlib' not in sys.modules
result = {
    'verdict': 'CLEAN',
    'hashes': {str(p): {'before': before[p], 'after': after[p]} for p in FILES},
    'independent_layout_count': len(records),
    'independent_boundary_invocation_count': len(records)*3,
    'independent_accepted_layouts': sum(r['expected']=='accept' for r in records),
    'independent_rejected_layouts': sum(r['expected']=='reject' for r in records),
    'guard_lines': guard_lines,
    'first_ingestion_line': 1471,
    'first_publication_line': 1842,
    'publication_trace': trace,
    'allowed_routing_test_count': routing.testsRun,
    'allowed_routing_test_output': stream.getvalue(),
    'scientific_modules_imported': False,
    'real_publication_executed': False,
    'independent_probes': records,
}
with (PRIVATE/'evidence.json').open('x') as handle:
    json.dump(result, handle, indent=2)
print(json.dumps({k: v for k, v in result.items() if k != 'independent_probes'}, indent=2))
