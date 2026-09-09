"""Private interface diagnostics: AST-isolated functions; no science imports/work."""
import argparse
import ast
import copy
import hashlib
import io
import json
import os
import pickle
import sys
import tempfile
import time
from contextlib import redirect_stdout
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

ROOT = Path('/home/amir/Codes/PDE/studies')
PRIVATE = Path(__file__).resolve().parent
RESULTS = []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(relative, names, namespace=None, constants=()):
    path = ROOT / relative
    tree = ast.parse(path.read_text())
    selected = [ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)]
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            selected.append(node)
        elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in constants for t in node.targets):
            selected.append(node)
    ns = dict(__file__=str(path), argparse=argparse, Path=Path, hashlib=hashlib,
              json=json, os=os, pickle=pickle, copy=copy, time=time)
    ns.update(namespace or {})
    exec(compile(ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[])), str(path), 'exec'), ns)
    return ns


def call_main(ns, args):
    saved = sys.argv
    sys.argv = ['private-diagnostic', *map(str, args)]
    try:
        with redirect_stdout(io.StringIO()):
            return ns['main']()
    finally:
        sys.argv = saved


def alias(source, target, kind):
    if kind == 'same':
        return source
    if kind == 'symlink':
        target.symlink_to(source)
    else:
        os.link(source, target)
    return target


def record(label, source, before, **extra):
    after = digest(source)
    RESULTS.append(dict(case=label, input=str(source), before_sha256=before,
                        after_sha256=after, input_changed=before != after, **extra))


def graph_checkpoint_cases(base):
    for kind in ('same', 'symlink', 'hardlink'):
        directory = base / ('graph-' + kind)
        directory.mkdir()
        checkpoint = directory / 'checkpoint.pkl'
        checkpoint.write_bytes(pickle.dumps({'order': 0, 'poly': {}, 'derivatives': []}))
        output = alias(checkpoint, directory / 'output.json', kind)
        forbidden = Mock(side_effect=AssertionError('coefficient work must not run'))
        ns = extract('mfp_quadratic_compiler/exact_graph_wick.py', ('main', 'run'),
                     dict(initial_observable=forbidden, expected_large_n=forbidden,
                          differentiate=forbidden, save_checkpoint=forbidden))
        before = digest(checkpoint)
        call_main(ns, ['--max-order', '0', '--resume', '--checkpoint', checkpoint, '--output', output])
        forbidden.assert_not_called()
        record('graph checkpoint/output ' + kind, checkpoint, before,
               output=str(output), science_calls=0, reproduced=True)
        assert digest(checkpoint) != before


def graded_cases(base):
    for kind in ('same', 'symlink', 'hardlink'):
        directory = base / ('graded-' + kind)
        directory.mkdir()
        lower = directory / 'lower.json'
        fixture = dict(parent_source_sha256='fixture-parent', cache={}, misses_by_remaining_order={},
                       observables={root: dict(jets=[{'lambda_coefficients': ['0']} for _ in range(8)],
                                              seconds=0, cache_before={}, cache_after={})
                                    for root in ('f', 'q1', 'q2')})
        lower.write_text(json.dumps(fixture))
        output = alias(lower, directory / 'upper.json', kind)
        ns = extract('mfp_quadratic_compiler/campaign1/run_graded_campaign.py', ('main', 'jet_record'),
                     constants=('EXPECTED_LOWER_SHA', 'EXPECTED_PARENT_SHA', 'EXPECTED_F9'))
        ns['time'] = SimpleNamespace(monotonic=lambda: 1.)
        original_expected = ns['EXPECTED_LOWER_SHA']
        ns['sha256'] = lambda p: original_expected if p == lower else digest(p)
        work = Mock(side_effect=[([ns['EXPECTED_F9']], []), ([0], [])])
        ns['run_order'] = work
        before = digest(lower)
        call_main(ns, ['--binary', directory / 'never-executed', '--lower-result', lower, '--output', output])
        assert work.call_count == 2
        record('graded lower/output ' + kind, lower, before,
               output=str(output), mocked_sector_calls=work.call_count,
               valid_frozen_input_hash_mocked=True, reproduced=True)
        assert digest(lower) != before
    # Real frozen hash mismatch, with no sector dispatch or output write.
    bad = base / 'bad-lower.json'
    bad.write_text('{}')
    ns = extract('mfp_quadratic_compiler/campaign1/run_graded_campaign.py', ('main', 'sha256'),
                 constants=('EXPECTED_LOWER_SHA', 'EXPECTED_PARENT_SHA', 'EXPECTED_F9'))
    forbidden = Mock(side_effect=AssertionError('sector work must not run'))
    ns['run_order'] = forbidden
    before = digest(bad)
    try:
        call_main(ns, ['--binary', base / 'never-executed', '--lower-result', bad, '--output', base / 'never-written'])
    except AssertionError as error:
        assert 'lower-order input hash' in str(error)
        record('graded frozen hash fails closed', bad, before, error=str(error), reproduced=True)
    else:
        raise AssertionError('hash gate did not fail')
    forbidden.assert_not_called()


def long_analysis_cases(base):
    for kind in ('same', 'symlink', 'hardlink'):
        directory = base / ('long-' + kind)
        raw = directory / 'raw'
        raw.mkdir(parents=True)
        trace = raw / 'trace.npz'
        trace.write_bytes(b'private mock trace bytes')
        report = alias(trace, directory / 'report.md', kind)
        metadata = dict(id='trace', config_sha256='fixture-config', code_sha256='fixture-code')
        ns = extract('resnet_dense_long_horizon/src/dense_mup/analysis.py', ('analyze_directory',), dict(
            load_trace=Mock(return_value=(metadata, {})), summarize_trace=Mock(return_value={'run_id': 'trace'}),
            _flatten_rows=Mock(return_value=[]), _horizon_rows=Mock(return_value=[]),
            _required_order_rows=Mock(return_value=[]), _refinement_comparison=Mock(return_value=[]),
            _aggregate=Mock(return_value=[]), _write_csv=Mock(), _plot_representative=Mock(),
            _plot_aggregate=Mock(), _build_report=Mock(return_value='private mock report')))
        before = digest(trace)
        ns['analyze_directory'](raw, directory / 'processed', directory / 'figures',
                                {'accuracy_levels': []}, 'trace', [metadata], report_path=report)
        record('long analysis report/input ' + kind, trace, before,
               output=str(report), science_and_plots_mocked=True, reproduced=True)
        assert digest(trace) != before


class Array:
    def __init__(self, shape=(), value=0):
        self.shape = shape
        self.size = 3 if shape == (3,) else 1
        self.value = value
    def tolist(self):
        return self.value
    def copy(self):
        return self
    def __getitem__(self, key):
        return 0.0
    def __setitem__(self, key, value):
        pass


def pde_namespace(output_root, restart_path, bad_hash=False):
    args = SimpleNamespace(P=1, N=1, M=1, R=1, seed=1, quadrature='sobol', base_order=1,
                           fast_order=1, sigma_w=.65, A=1., gamma=1., restart_from=str(restart_path),
                           duration=.04, dt=.02, sample_dt=.04, integrator='rk4')
    meta = dict(quadrature='sobol', basis_size_P=1, depth_nodes_N=1,
                base_quadrature_M=1, fast_quadrature_R=1, quadrature_seed=1,
                sigma_w=.65, A=1., gamma=1., X=[[1,0,0],[0,1,0],[0,0,1]],
                y=[.8,-.55,.35], multi_indices=[])
    if bad_hash:
        meta['static_compiler_sha256'] = 'bad-hash'
    restart = dict(metadata_json=json.dumps(meta), times=[8.], final_B=Array((1,3)),
                   final_a=Array((1,)), final_c=Array((1,1,1,1)))
    loaded = []
    def load(path):
        assert Path(path) == restart_path
        loaded.append(digest(restart_path))
        return restart
    np = SimpleNamespace(eye=lambda _: Array((3,3), meta['X']),
                         array=lambda x: Array((len(x),), x) if isinstance(x, list) else Array((), x),
                         empty=lambda s: Array(s if isinstance(s, tuple) else (s,)),
                         load=load, min=lambda _: 0.,
                         savez_compressed=lambda stream, **kwargs: stream.write(b'private mock PDE result'))
    fields = ('raw_basis_gram_error', 'raw_basis_min_eigenvalue', 'raw_basis_max_eigenvalue',
              'raw_basis_condition', 'whitened_basis_gram_error', 'fast_mean_error',
              'raw_fast_min_eigenvalue', 'raw_fast_max_eigenvalue', 'raw_fast_condition', 'fast_cov_error')
    quadrature = SimpleNamespace(**{k: 0. for k in fields}, multi_indices=[],
                                 **{k: Array() for k in ('base_latent', 'base_weights', 'phi', 'epsilon', 'fast_weights')})
    observation = SimpleNamespace(**{k: 0. for k in ('f', 'loss', 'grams', 'theta', 'theta_min',
                                                   'residual_norm', 'loss_dot', 'projected_energy')})
    ns = extract('resnet_operator_core/run_pde.py', ('run', '_tag'), dict(
        OUTPUT_ROOT=output_root, np=np, PDESpec=SimpleNamespace, PDEState=SimpleNamespace,
        build_quadrature=Mock(return_value=quadrature), _array_sha256=Mock(return_value='fixture-array-hash'),
        observe=Mock(return_value=observation), rk4_step=Mock(side_effect=lambda state, *a: state),
        initialize=Mock(side_effect=AssertionError('initialize not expected on restart'))))
    return ns, args, loaded


def pde_cases(base):
    for kind in ('symlink', 'hardlink', 'same-partial'):
        directory = base / ('pde-' + kind)
        raw = directory / 'results/raw'
        raw.mkdir(parents=True)
        output = raw / 'pde_QMC_P1_N1_M1_R1_s1_dt0p02_T0p04_from8_to8p04.npz'
        partial = output.with_suffix('.npz.partial')
        restart = partial if kind == 'same-partial' else directory / 'restart.npz'
        restart.write_bytes(b'private mock retained restart')
        if kind != 'same-partial':
            alias(restart, partial, kind)
        before = digest(restart)
        ns, args, loaded = pde_namespace(directory, restart)
        with redirect_stdout(io.StringIO()):
            ns['run'](args)
        assert loaded == [before]
        if kind == 'same-partial':
            RESULTS.append(dict(case='PDE selected restart equals automatic partial', input=str(restart),
                                before_sha256=before, after_sha256=None, input_removed=not restart.exists(),
                                output=str(output), science_and_serialization_mocked=True, reproduced=True))
            assert not restart.exists()
        else:
            record('PDE automatic partial/input ' + kind, restart, before, output=str(output),
                   science_and_serialization_mocked=True, reproduced=True)
            assert digest(restart) != before
    directory = base / 'pde-bad-hash'
    directory.mkdir()
    restart = directory / 'restart.npz'
    restart.write_bytes(b'private bad-hash fixture')
    ns, args, loaded = pde_namespace(directory, restart, bad_hash=True)
    before = digest(restart)
    try:
        ns['run'](args)
    except ValueError as error:
        assert 'restart static compiler/quadrature hash mismatch' in str(error)
        ns['observe'].assert_not_called()
        record('PDE restart hash fails closed', restart, before, error=str(error), reproduced=True)
    else:
        raise AssertionError('restart hash gate did not fail')


def closed_gates():
    for rel, constants in (
        ('mfp_quadratic_compiler/campaign4/run_sectors.py', ()),
        ('mfp_quadratic_compiler/campaign4/make_provenance.py', ()),
        ('mfp_quadratic_compiler/campaign5_b3/run_stage_c.py', ('STAGE_C_AUTHORIZED',)),
    ):
        ns = extract(rel, ('main',), constants=constants)
        try:
            ns['main']()
        except SystemExit as error:
            RESULTS.append(dict(case=rel + ' callable authorization gate', error=str(error), reproduced=True))
        else:
            raise AssertionError('closed gate did not reject')


def depth3_hash_gates():
    for filename, order in (('depth3_stieltjes_audit.py', 9), ('depth3_order13_stieltjes_audit.py', 13)):
        relative = 'mfp_quadratic_compiler/depth3_gaussian_program/' + filename
        ns = extract(relative, ('main',), constants=('EXPECTED_SHA256',))
        expected = ns['EXPECTED_SHA256']
        here = (ROOT / relative).parent
        paths = {'input': ROOT.parent / f'data/historical/studies/mfp_quadratic_compiler/depth3_gaussian_program/results_order{order}.json',
                 'protocol': here / ('STIELTJES_PROTOCOL.md' if order == 9 else 'ORDER13_STIELTJES_PROTOCOL.md'),
                 'exact_series_route': 'OUT_OF_SCOPE_MOCK'}
        if order == 13:
            paths.update(derivative_engine=here / 'depth3_exact_jet.py', moment_audit_primitives=here / 'depth3_stieltjes_audit.py')
        actual = {key: expected[key] if key == 'exact_series_route' else digest(path) for key, path in paths.items()}
        reverse = {str(path): actual[key] for key, path in paths.items()}
        ns.update(INPUT=paths['input'], PROTOCOL=paths['protocol'], EXACT_SERIES=paths['exact_series_route'],
                  sha256=lambda p: reverse[str(p)])
        if order == 13:
            ns.update(DERIVATIVE_ENGINE=paths['derivative_engine'], MOMENT_AUDIT_PRIMITIVES=paths['moment_audit_primitives'])
        try:
            ns['main']()
        except AssertionError as error:
            assert 'SHA-256 gate failed' in str(error)
            RESULTS.append(dict(case=filename + ' old seal fails closed',
                                scoped_actual=actual, expected=expected,
                                out_of_scope_route_hash_mocked_as_matching=True, error=str(error), reproduced=True))
        else:
            raise AssertionError('old seal unexpectedly passed; do not run downstream work')


def campaign5_selected_paths(base):
    selected = base / 'selected-evidence'
    campaign = selected / 'campaign5_b3'
    campaign.mkdir(parents=True)
    for filename in ('test_stage_a_provenance.py', 'test_stage_c_closed.py'):
        path = ROOT / 'mfp_quadratic_compiler/campaign5_b3' / filename
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                    and node.func.attr == 'read_text' and isinstance(node.func.value, ast.BinOp)
                    and isinstance(node.func.value.left, ast.Name) and node.func.value.left.id == 'HERE'
                    and isinstance(node.func.value.right, ast.Constant)
                    and str(node.func.value.right.value).startswith('provenance_')):
                label = node.func.value.right.value
                chosen = campaign / label
                chosen.write_text('private selected evidence sentinel')
                expr = ast.Expression(body=node.func.value)
                actual = eval(compile(expr, str(path), 'eval'), {'HERE': path.parent, 'INPUT_ROOT': selected})
                historical = ROOT.parent / 'data/historical/studies/mfp_quadratic_compiler/campaign5_b3' / label
                assert not actual.exists()
                assert historical.is_file()
                assert chosen.is_file()
                RESULTS.append(dict(case='Campaign5 evidence path ignores selection', source=str(path),
                                    line=node.lineno, actual_lookup=str(actual), actual_exists=False,
                                    selected_root=str(selected), selected_exists=True,
                                    historical_path=str(historical), historical_sha256=digest(historical),
                                    diagnostic='AST path expression only; test function not executed', reproduced=True))


def long_hash_gates(base):
    directory = base / 'long-stale'
    raw = directory / 'raw'
    raw.mkdir(parents=True)
    trace = raw / 'trace.npz'
    trace.write_bytes(b'private unchanged stale trace')
    expected = dict(id='trace', config_sha256='config', code_sha256='code')
    for key in ('config_sha256', 'code_sha256'):
        metadata = {**expected, key: 'stale'}
        forbidden = Mock(side_effect=AssertionError('analysis work must not run'))
        ns = extract('resnet_dense_long_horizon/src/dense_mup/analysis.py', ('analyze_directory',),
                     dict(load_trace=Mock(return_value=(metadata, {})), summarize_trace=forbidden))
        before = digest(trace)
        try:
            ns['analyze_directory'](raw, directory / 'processed', directory / 'figures', {}, 'trace', [expected])
        except ValueError as error:
            assert 'stale' in str(error)
            record('long ' + key + ' fails closed', trace, before, error=str(error), reproduced=True)
        else:
            raise AssertionError('long stale hash gate did not reject')
        forbidden.assert_not_called()
        assert not (directory / 'processed').exists()


def native_alias_static(base):
    source = ROOT / 'mfp_quadratic_compiler/sector_parallel_reuse.cpp'
    text = source.read_text()
    assert 'std::string source_checkpoint = argv[3];' in text
    assert 'std::string sparse_checkpoint = argv[5];' in text
    assert 'std::ofstream checkpoint_out(sparse_checkpoint, std::ios::app);' in text
    assert "checkpoint_out << '\\n';" in text
    directory = base / 'native-alias-identities'
    directory.mkdir()
    checkpoint = directory / 'source-values.chk'
    checkpoint.write_text('1\n')
    for kind in ('same', 'symlink', 'hardlink'):
        output = alias(checkpoint, directory / (kind + '.sparse'), kind)
        assert output.samefile(checkpoint)
        RESULTS.append(dict(case='native sparse/source alias ' + kind, source=str(source),
                            source_checkpoint=str(checkpoint), sparse_checkpoint=str(output),
                            samefile=True, native_execution=False,
                            evidence='Complete main inspection: unconditional append newline at lines 143-146; no identity guard.'))


with tempfile.TemporaryDirectory(prefix='fixtures-', dir=PRIVATE) as directory:
    base = Path(directory)
    graph_checkpoint_cases(base)
    graded_cases(base)
    long_analysis_cases(base)
    pde_cases(base)
    closed_gates()
    depth3_hash_gates()
    campaign5_selected_paths(base)
    long_hash_gates(base)
    native_alias_static(base)
print(json.dumps(RESULTS, indent=2, sort_keys=True))
