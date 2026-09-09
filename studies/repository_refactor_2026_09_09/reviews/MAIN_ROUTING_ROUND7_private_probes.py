import argparse
import ast
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import time
from contextlib import redirect_stdout, redirect_stderr
from types import SimpleNamespace, ModuleType
from unittest.mock import Mock, patch

PRIVATE = Path(__file__).parent
REPO = Path('/home/amir/Codes/PDE')
LONG = REPO / 'studies/resnet_dense_long_horizon'
EARLY = REPO / 'studies/resnet_dense_early_audit'
OPERATOR = REPO / 'studies/resnet_operator_core'
QUADRATIC = REPO / 'studies/mfp_quadratic_compiler'
for name in ('tmp', 'cache', 'mpl', 'probes'):
    (PRIVATE / name).mkdir(exist_ok=True)
CASES = Path(tempfile.mkdtemp(prefix='probe-run-', dir=PRIVATE))
os.environ.update(TMPDIR=str(PRIVATE / 'tmp'), XDG_CACHE_HOME=str(PRIVATE / 'cache'), MPLCONFIGDIR=str(PRIVATE / 'mpl'), PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
for key in tuple(os.environ):
    if key.startswith(('PDE_OPERATOR_', 'PDE_QUADRATIC_', 'PDE_LONG_HORIZON_')) or key == 'GALERKIN_OUT':
        os.environ.pop(key)
os.environ.update(PDE_OPERATOR_OUTPUT_ROOT=str(CASES / 'operator'), PDE_OPERATOR_INPUT_ROOT=str(CASES / 'selected'), PDE_QUADRATIC_OUTPUT_ROOT=str(CASES / 'quadratic'), PDE_QUADRATIC_INPUT_ROOT=str(CASES / 'selected'))
sys.dont_write_bytecode = True
sys.path[:0] = [str(REPO), str(OPERATOR), str(OPERATOR / 'src'), str(EARLY), str(LONG), str(LONG / 'src')]
import numpy as np
matplotlib = ModuleType('matplotlib')
matplotlib.use = lambda *args, **kwargs: None
pyplot = ModuleType('matplotlib.pyplot')
matplotlib.pyplot = pyplot
sys.modules.update({'matplotlib': matplotlib, 'matplotlib.pyplot': pyplot})

records = []
def record(name, **details):
    records.append(dict(name=name, **details))
    (PRIVATE / 'private_probe_results.json').write_text(json.dumps(records, indent=2) + '\n')
    print(json.dumps(records[-1]), flush=True)

def load(path):
    # Use the actual complete module and its bootstrap imports.
    return runpy.run_path(str(path), run_name='isolated_acceptance_import')

def extracted(path, names, **bindings):
    tree = ast.parse(path.read_text())
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names or isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in n.targets)]
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    ns = dict(argparse=argparse, Path=Path, json=json, __file__=str(path), __doc__='private transport fixture', **bindings)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), 'exec'), ns)
    return ns

# Capture all additional current source inputs before subprocess imports.
prior = json.loads((PRIVATE / 'before_hashes.json').read_text())
extra_paths = [p for base in (LONG, EARLY, OPERATOR, QUADRATIC) for p in base.rglob('*.py') if '__pycache__' not in p.parts]
extra_before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in extra_paths}
(PRIVATE / 'extra_before_hashes.json').write_text(json.dumps(extra_before, indent=2) + '\n')

# Help stops before main work, using real script bootstrap and private caches.
help_paths = [EARLY / 'run_dense_resnet_audit.py', EARLY / 'run_response_galerkin_projection.py', LONG / 'run_all.py', LONG / 'make_manifest.py', OPERATOR / 'run_pde.py', OPERATOR / 'run_exact_reference.py', OPERATOR / 'combine_references.py', OPERATOR / 'audits/numerics/paired_w_variance.py']
help_paths += [QUADRATIC / name for name in ('exact_graph_wick.py', 'campaign1/run_graded_campaign.py', 'campaign1/analyze_hankel.py', 'campaign1/parametric_stieltjes_postprocess.py', 'campaign2/postprocess.py', 'campaign3/postprocess.py', 'campaign4/postprocess.py', 'campaign6_f13_threshold/run_benchmark.py', 'operator_ide_closure/finite_width_boundary_layer.py')]
help_passes = []
help_limited = []
for path in help_paths:
    proc = subprocess.run([sys.executable, '-B', str(path), '--help'], cwd=PRIVATE / 'probes', env=os.environ.copy(), text=True, capture_output=True, timeout=20)
    if "No module named 'sympy'" in proc.stderr:
        help_limited.append({'path': str(path), 'missing': 'sympy'})
        continue
    if "No module named 'matplotlib'" in proc.stderr:
        help_limited.append({'path': str(path), 'missing': 'matplotlib', 'bootstrap_probe': 'real complete script with plotting-import-only stub'})
        proc = subprocess.run([sys.executable, '-B', str(PRIVATE / 'bootstrap.py'), str(path), '--help'], cwd=PRIVATE / 'probes', env=os.environ.copy(), text=True, capture_output=True, timeout=20)
    assert proc.returncode == 0 and 'usage:' in proc.stdout, (path, proc.stderr)
    help_passes.append(str(path))
record('direct_help_and_bootstrap', passed=len(help_passes), dependency_limits=help_limited)

# Guarded main and all public directory callables must retain actual imports.
early = load(EARLY / 'run_dense_resnet_audit.py')
folder = CASES / 'early'
folder.mkdir(exist_ok=True)
sentinel = folder / 'sentinel'
sentinel.write_bytes(b'retained input')
linked = folder / 'output'
linked.mkdir(exist_ok=True)
(linked / 'nested.csv').symlink_to(sentinel)
names = ('finite_difference_scaling_audit', 'iid_depth_self_averaging', 'depth_resolution_experiment', 'response_snapshot_audit', 'truncated_training_experiment', 'restart_and_horizon_experiment', 'parameter_grid_experiment', 'summarize')
for name in names:
    kwargs = dict(out_dir=linked)
    if name == 'response_snapshot_audit':
        kwargs.update(state=None, X=None, y=None, orders=(), tag='fixture')
    if name == 'summarize':
        kwargs['payload'] = {'fixture': True}
    try:
        early[name](**kwargs)
    except ValueError as error:
        assert 'symlink' in str(error)
    else:
        raise AssertionError(name)
record('real_early_callable_guard_bootstrap', passed=len(names))
for path, arguments, env_extra in ((EARLY / 'run_dense_resnet_audit.py', ['--out', str(linked)], {}), (EARLY / 'run_response_galerkin_projection.py', [], {'GALERKIN_OUT': str(linked)}), (OPERATOR / 'run_pde.py', [], {'PDE_OPERATOR_OUTPUT_ROOT': str(linked)}), (OPERATOR / 'run_exact_reference.py', [], {'PDE_OPERATOR_OUTPUT_ROOT': str(linked)})):
    proc = subprocess.run([sys.executable, '-B', str(PRIVATE / 'bootstrap.py'), str(path), *arguments], cwd=PRIVATE / 'probes', env={**os.environ, **env_extra}, text=True, capture_output=True, timeout=20)
    assert proc.returncode != 0 and 'symlink' in proc.stderr and 'NameError' not in proc.stderr, (path, proc.stderr)
assert sentinel.read_bytes() == b'retained input'
record('real_direct_script_alias_refusal', passed=4)

# Execute the whole orchestration function, mocking every experiment dispatch.
fresh = folder / 'ordinary-refresh'
fresh.mkdir(exist_ok=True)
(fresh / 'summary.json').write_text('old ordinary summary')
glob = early['main'].__globals__
patches = {name: Mock(return_value={'fixture': name}) for name in names if name not in {'summarize', 'response_snapshot_audit', 'restart_and_horizon_experiment'}}
patches['restart_and_horizon_experiment'] = Mock(return_value=({'horizon': True}, {'restart': True}))
with patch.dict(glob, patches), patch.object(sys, 'argv', ['early', '--out', str(fresh)]), redirect_stdout(io.StringIO()):
    early['main']()
assert len(json.loads((fresh / 'summary.json').read_text())) == 7
assert all(m.call_count == 1 for m in patches.values())
record('whole_early_main_refresh', dispatches=len(patches), output='summary.json', science='mocked')

# Operator analysis startup with real imports and frozen complete function bodies.
for relative, reader in (('analyze.py', 'load'), ('audits/statistical_audit/analyze.py', 'load_archive'), ('audits/statistical_audit/reference_noise_update.py', 'load_block'), ('audits/statistical_audit/ordered_limit_update.py', 'load_exact')):
    ns = load(OPERATOR / relative)
    fn = ns['main']
    good = CASES / relative.replace('/', '_')
    good.mkdir(exist_ok=True)
    (good / 'summary.json').write_text('previous report')
    stop = Mock(side_effect=RuntimeError('stop before science'))
    raw_fixture = good / 'selected-raw'
    raw_fixture.mkdir()
    (raw_fixture / 'fixture.npz').write_bytes(b'inert input; load is mocked')
    with patch.dict(fn.__globals__, {reader: stop, 'OUT': good, 'PROCESSED': good, 'FIGURES': good, 'RAW': raw_fixture}):
        try:
            fn()
        except RuntimeError as error:
            assert str(error) == 'stop before science'
        else:
            raise AssertionError(relative)
    assert stop.call_count == 1
record('real_operator_analysis_import_and_refresh', passed=4)

# Complete reference archive publication using inert arrays from a mocked worker.
ns = load(OPERATOR / 'run_exact_reference.py')
root = CASES / 'reference-transport'
args = SimpleNamespace(n=1, depth=1, seed_start=10, seeds=2, duration=1, dt=1, sample_dt=1, sigma_w=1, workers=1)
def inert_seed(payload):
    return dict(seed=payload[2], times=np.array([0., 1.]), f=np.zeros((2, 3)), grams=np.zeros((2, 2, 3, 3)), theta=np.zeros((2, 3, 3)))
with patch.dict(ns['run'].__globals__, {'OUTPUT_ROOT': root, '_one_seed': Mock(side_effect=inert_seed)}), redirect_stdout(io.StringIO()):
    first = ns['run'](args)
    second = ns['run'](args)
assert first == second and second.is_file() and not second.with_suffix('.npz.partial').exists()
with np.load(second, allow_pickle=False) as archive:
    assert archive['seeds'].tolist() == [10, 11]
record('whole_reference_publication_and_distinct_refresh', passed=2, science='mocked worker; inert arrays only')

# Whole long analysis boundary through all publications, with analysis/plots mocked.
import dense_mup.analysis as analysis
case = CASES / 'long-transport'
raw = case / 'selected'
raw.mkdir(parents=True, exist_ok=True)
trace = raw / 'fixture.npz'
trace.write_bytes(b'inert trace transport')
before = hashlib.sha256(trace.read_bytes()).hexdigest()
meta = {'id': 'fixture', 'config_sha256': 'config', 'code_sha256': 'source'}
summary = {'run_id': 'fixture', 'path': str(trace)}
bindings = {'load_trace': Mock(return_value=(meta, {})), 'summarize_trace': Mock(return_value=summary), '_flatten_rows': Mock(return_value=[]), '_horizon_rows': Mock(return_value=[]), '_required_order_rows': Mock(return_value=[]), '_refinement_comparison': Mock(return_value=[]), '_aggregate': Mock(return_value=[]), '_plot_representative': Mock(), '_plot_aggregate': Mock(), '_build_report': Mock(return_value='fixture report\n')}
for repetition in range(2):
    with patch.multiple(analysis, **bindings):
        result = analysis.analyze_directory(raw, case / 'generated/processed', case / 'generated/figures', {'accuracy_levels': []}, 'fixture', [meta], case / 'generated/report.md')
    assert result['traces'] == 1 and result['actual_compiled_liouville_pde_runs'] == 0
assert hashlib.sha256(trace.read_bytes()).hexdigest() == before
assert (case / 'generated/processed/analysis_manifest.json').is_file()
record('whole_long_analysis_publication_and_refresh', passed=2, science='all analysis and plots mocked; selected bytes preserved')

# Demonstrate that a specifically consumed provenance source is missing from the
# Campaign 1 destination guard, without unfreezing any production inputs.
helper = load(QUADRATIC / 'campaign_paths.py')
case = CASES / 'graded-consumed-source'
case.mkdir(exist_ok=True)
lower, binary = case / 'lower.json', case / 'binary'
fixture = {'parent_source_sha256': 'fixture', 'cache': {}, 'misses_by_remaining_order': {}, 'observables': {name: {'jets': [{'lambda_coefficients': ['0']} for _ in range(8)], 'seconds': 0, 'cache_before': {}, 'cache_after': {}} for name in ('f', 'q1', 'q2')}}
lower.write_text(json.dumps(fixture))
binary.write_text('inert executable, never launched')
for kind in ('same', 'symlink', 'hardlink'):
    source = case / kind / 'graded_sector.cpp'
    source.parent.mkdir()
    source.write_bytes(b'private stand-in for consumed graded source')
    output = source if kind == 'same' else source.with_name('export.json')
    if kind == 'symlink':
        output.symlink_to(source)
    elif kind == 'hardlink':
        os.link(source, output)
    ns = extracted(QUADRATIC / 'campaign1/run_graded_campaign.py', {'main', 'jet_record', 'EXPECTED_LOWER_SHA', 'EXPECTED_PARENT_SHA', 'EXPECTED_F9'}, copy=copy, hashlib=hashlib, time=time, require_distinct_output=helper['require_distinct_output'])
    ns['__file__'] = str(source.with_name('run_graded_campaign.py'))
    observed = []
    def fixture_digest(path):
        observed.append(str(path))
        # Same synthetic lower-result seam as the supplied transport test.
        # Production EXPECTED_LOWER_SHA and all real files remain untouched.
        return ns['EXPECTED_LOWER_SHA'] if path == lower else hashlib.sha256(path.read_bytes()).hexdigest()
    ns['sha256'] = fixture_digest
    ns['run_order'] = Mock(side_effect=[([ns['EXPECTED_F9']], []), ([0], [])])
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    with patch.object(sys, 'argv', ['graded', '--binary', str(binary), '--lower-result', str(lower), '--output', str(output)]), redirect_stdout(io.StringIO()):
        ns['main']()
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    payload = json.loads(source.read_text())
    assert str(source) in observed and payload['graded_sector_source_sha256'] == before and before != after
    record('BLOCKER_graded_consumed_source_overwritten', kind=kind, before=before, after=after, source=str(source), computed_sectors='mocked', reported_source_digest=payload['graded_sector_source_sha256'])

# Centered-depth publisher: all scientific routines replaced by transport stubs;
# the whole main, input hashing and actual write remain unchanged.
case = CASES / 'centered-consumed-source'
case.mkdir(exist_ok=True)
for kind in ('symlink', 'hardlink'):
    here = case / kind / 'source'
    here.mkdir(parents=True)
    source = here / 'centered_h2_exact.py'
    source.write_bytes(b'private consumed source stand-in')
    (here / 'PROTOCOL.md').write_bytes(b'private protocol fixture')
    generated = case / kind / 'generated'
    output = generated / 'centered_depth1_order13/RESULTS.json'
    output.parent.mkdir(parents=True)
    if kind == 'symlink':
        output.symlink_to(source)
    else:
        os.link(source, output)
    ns = extracted(QUADRATIC / 'centered_depth1_order13/centered_h2_exact.py', {'main'}, HERE=here, OUTPUT_ROOT=generated, SEARCH_ORDER=81, DECISION_ORDER=13, time=time, lie_jet=Mock(return_value=([0] * 14, [])), taylor_jet=Mock(return_value=([0] * 14, [])), load_reversion_route=Mock(return_value=Mock(return_value=(0, (0,) * 6))), moments_from_triangular_identity=Mock(return_value=(0, (0,) * 6)), serialize_minors=Mock(return_value={'all_positive': False, 'negative_labels': []}), audit_hankels=Mock(return_value={}), fraction_string=str, signed_record=lambda value: {'exact': str(value)}, sha256=lambda path: hashlib.sha256(path.read_bytes()).hexdigest())
    ns['__file__'] = str(source)
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    with patch.object(sys, 'argv', ['centered']), redirect_stdout(io.StringIO()):
        assert ns['main']() == 0
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    payload = json.loads(source.read_text())
    assert before != after and payload['sha256']['source'] == before
    record('BLOCKER_centered_consumed_source_overwritten', kind=kind, before=before, after=after, source=str(source), science='all routines mocked', reported_source_digest=payload['sha256']['source'])

extra_after = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in extra_before}
(PRIVATE / 'extra_after_hashes.json').write_text(json.dumps(extra_after, indent=2) + '\n')
assert extra_before == extra_after
(PRIVATE / 'private_probe_results.json').write_text(json.dumps(records, indent=2) + '\n')
record('extra_source_hashes_unchanged', count=len(extra_before))
