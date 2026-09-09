"""Bounded migration-interface checks. No scientific producer is executed."""
from __future__ import annotations
import ast
import contextlib
import hashlib
import importlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import ModuleType, SimpleNamespace
import unittest
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path('/tmp/pde-gaussian-routing-final.bJLzzv91')
manifest = json.loads((PRIVATE / 'input_manifest.json').read_text())
allowed = {str(ROOT / row['path']) for row in manifest['files']}
reads = set()
blocked = []
def boundary(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes)):
        path = Path(os.fsdecode(args[0])).absolute()
        mode = args[1] or ''
        flags = args[2] or 0
        writing = any(c in mode for c in 'wax+') or flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC)
        if writing and not path.is_relative_to(PRIVATE):
            raise PermissionError(f'diagnostic write boundary: {path}')
        if not writing and path.is_relative_to(ROOT):
            if str(path) not in allowed:
                # Missing source-side data must fail honestly without reading.
                if not path.exists():
                    raise FileNotFoundError(str(path))
                blocked.append(str(path))
                raise PermissionError(f'diagnostic read boundary: {path}')
            reads.add(str(path))
    if event == 'os.mkdir' and not Path(args[0]).absolute().is_relative_to(PRIVATE):
        raise PermissionError(f'diagnostic mkdir boundary: {args[0]}')
    if event in ('subprocess.Popen', 'os.system'):
        raise PermissionError('subprocess forbidden inside diagnostic')
sys.addaudithook(boundary)
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
tempfile.tempdir = str(PRIVATE)
results = {}

from studies._output_paths import StudyPaths
from studies.mfp_gaussian_calculus import study_paths
sample = ROOT / 'studies/mfp_gaussian_calculus/depth_order5/audit/compare_frozen.py'
p = StudyPaths(sample)
results['shared_defaults'] = {k: str(v) for k, v in vars(p.parse([], inputs=True)).items()}
results['shared_historical'] = {k: str(v) for k, v in vars(p.parse(['--historical-inputs'], inputs=True)).items()}
results['output_rejections'] = []
for target in (ROOT/'studies/mfp_gaussian_calculus', p.historical, ROOT/'data/generated/mfp_identity_compiler'):
    row = {'target': str(target)}
    for name, function in [('shared', p.require_output), ('gaussian', study_paths.require_output)]:
        try:
            row[name] = str(function(target))
        except ValueError:
            row[name] = 'rejected'
    results['output_rejections'].append(row)

# Actual map reader, with only file contents mocked; record the selected file.
from studies.mfp_linear_growth_uniform_counterexample import map_inputs
from studies.mfp_linear_growth_uniform_counterexample import evaluate_full_l2_transition as linear_reader
linear_paths = []
def tiny_map(path, *a, **kw):
    linear_paths.append(str(path))
    return '{"paired_map": []}'
with mock.patch.object(Path, 'read_text', tiny_map):
    linear_reader.load_collapsed_map()
    linear_reader.load_collapsed_map(map_inputs.parse_map_path(['--historical-inputs']))
    linear_reader.load_collapsed_map(map_inputs.parse_map_path(['--map-path', str(PRIVATE/'selected.json')]))
results['linear_reader_selected_paths'] = linear_paths

# Import and call the real producer entrypoint; replace compilers with tripwires.
from studies.mfp_linear_growth_uniform_counterexample import full_l2_paired_transition as linear_producer
with mock.patch.object(linear_producer, 'compile_paired_map', side_effect=AssertionError('scientific work forbidden')) as comp:
    try:
        linear_producer.main()
    except Exception as error:
        results['linear_producer'] = {'type': type(error).__name__, 'message': str(error), 'compiler_calls': comp.call_count}

# Identity and D3: stop exactly at the first actual input read.
class FirstRead(Exception):
    pass
def capture_read(path, *a, **kw):
    raise FirstRead(str(path))
sys.modules['sympy'] = ModuleType('sympy')  # parser/import stub only, no mathematics
results['consumer_first_reads'] = []
for name, input_relative in [
    ('studies.mfp_identity_compiler.linear_gaussian_program.depth2_all_order_search.audit_hankel40', ''),
    ('studies.mfp_identity_compiler.linear_gaussian_program.depth2_all_order_search.spectral_closure', ''),
    ('studies.d3_arctan_closure_program.analyze_gpu_gauge_block_gradient', 'gpu_gauge_gradient_results'),
    ('studies.d3_arctan_closure_program.analyze_gpu_high_moment_tail', 'gpu_tail_results'),
    ('studies.d3_arctan_closure_program.analyze_gpu_weighted_offcolumn_response', 'gpu_weighted_response_results'),
]:
    module = importlib.import_module(name)
    for argv in ([], ['--historical-inputs'], ['--input-dir', str(PRIVATE/'selected')]):
        with mock.patch.object(sys, 'argv', [name, *argv]), mock.patch.object(Path, 'mkdir'), mock.patch.object(Path, 'read_text', capture_read):
            if hasattr(module, 'load'):
                loader_patch = mock.patch.object(module, 'load', capture_read)
            else:
                loader_patch = contextlib.nullcontext()
            with loader_patch:
                try:
                    module.main()
                except FirstRead as error:
                    results['consumer_first_reads'].append({'module': name, 'argv': argv, 'read': str(error)})

from studies.mfp_gaussian_calculus.depth_order5_scalar.independent import depth_assembler
results['scalar_accepted_loader'] = []
for depth in (2, 3, 4):
    try:
        depth_assembler._read_accepted(depth)
    except FileNotFoundError as error:
        results['scalar_accepted_loader'].append({'depth': depth, 'error': str(error)})

# Run AST-extracted emitter bodies with tiny transitions and an in-memory Path.
# This preserves destination decisions and serialization calls; no original
# transition, coefficient generation, report input, or filesystem write runs.
class MemoryPath:
    files = {}
    events = []
    def __init__(self, path): self.path = Path(path)
    def __truediv__(self, child): return MemoryPath(self.path / child)
    def resolve(self): return self
    @property
    def parent(self): return MemoryPath(self.path.parent)
    @property
    def name(self): return self.path.name
    def __str__(self): return str(self.path)
    def write_text(self, value): self.files[str(self)] = value.encode(); self.events.append(str(self))
    def write_bytes(self, value): self.files[str(self)] = value; self.events.append(str(self))
    def read_bytes(self): return self.files[str(self)]
    def read_text(self): return self.files.get(str(self), b'private mock preamble').decode()

from fractions import Fraction
results['unguarded_emitters'] = []
for relative in [
    'depth_order5_scalar/independent/forward_contraction.py',
    'depth_order5_scalar/independent/reverse_contraction.py',
    'depth_order5_scalar/independent/moving_contraction.py',
    'depth_order5_scalar/multi_observable/independent_route_a/gamma04_contraction.py',
    'depth_order5_observables/independent/gamma04_contraction.py',
]:
    source = ROOT/'studies/mfp_gaussian_calculus'/relative
    tree = ast.parse(source.read_text())
    function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'emit')
    tiny = {'v': {('M010000',): Fraction(1)}}
    if relative.endswith('moving_contraction.py'):
        tiny = {'feature2': tiny}
    env = {'Path': MemoryPath, '__file__': str(source), 'json': json, 'hashlib': hashlib,
           'transition': lambda: tiny, 'transitions': lambda: tiny,
           'serialise': lambda x: {'M010000': '1'}, 'format_poly': lambda x: 'M010000',
           'local_audit': lambda: {}}
    MemoryPath.events = []
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(source), 'exec'), env)
    env['emit']()
    results['unguarded_emitters'].append({'source': relative, 'would_write': MemoryPath.events[:]})

source = ROOT/'studies/mfp_gaussian_calculus/depth_order5_scalar/independent/build_full_report.py'
tree = ast.parse(source.read_text())
function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'build')
env = {'Path': MemoryPath, 'ROOT': MemoryPath(source.parent), 'hashlib': hashlib, 'equation_appendix': lambda *a: 'mock appendix'}
MemoryPath.events = []
exec(compile(ast.Module(body=[function], type_ignores=[]), str(source), 'exec'), env)
env['build']()
results['scalar_report_would_write'] = MemoryPath.events[:]

# Newly frozen shared references: distinguish selected live inputs from the
# immutable reference consumer without evaluating any recurrence.
from studies.mfp_gaussian_calculus.depth_order5_scalar.primary import audit_full_scalar_recurrence as scalar_audit
from studies.mfp_gaussian_calculus.depth_order5_scalar.audit import reference_maps
results['postfreeze_scalar_routing'] = []
reference_snapshot = dict(reference_maps.REFERENCE)
for root in (scalar_audit.selected_input_root(), scalar_audit.selected_input_root(historical_inputs=True), PRIVATE/'selected'):
    for depth in (2, 3, 4):
        with mock.patch.object(Path, 'read_bytes', capture_read):
            try:
                scalar_audit.load_selected_reference(depth, root)
            except FirstRead as error:
                results['postfreeze_scalar_routing'].append({'depth': depth, 'selected_root': str(root), 'read': str(error)})
results['fixed_reference_read_paths'] = {str(depth): str(reference_maps.historical_reference_path(depth)) for depth in (2,3,4)}
results['shared_reference_unchanged'] = reference_snapshot == reference_maps.REFERENCE
results['postfreeze_early_archive_refusals'] = []
for relative in ('depth_order5/audit/run_checks.py', 'depth_order5/primary/run_lightweight_checks.py'):
    source = ROOT/'studies/mfp_gaussian_calculus'/relative
    tree = ast.parse(source.read_text())
    first = tree.body[1]  # after module docstring, before all imports/work
    assert isinstance(first, ast.Raise)
    try:
        exec(compile(ast.Module(body=[first], type_ignores=[]), str(source), 'exec'), {})
    except RuntimeError as error:
        results['postfreeze_early_archive_refusals'].append({'source': relative, 'message': str(error)})

# Supplied tests are supplementary evidence, after independent source inspection.
suite_module = importlib.import_module('studies.mfp_gaussian_calculus.test_migration_paths')
stream = io.StringIO()
with contextlib.redirect_stdout(io.StringIO()):
    outcome = unittest.TextTestRunner(stream=stream, verbosity=1).run(unittest.defaultTestLoader.loadTestsFromModule(suite_module))
results['supplied_tests'] = {'tests': outcome.testsRun, 'failures': len(outcome.failures), 'errors': len(outcome.errors), 'log': stream.getvalue()}
results['repository_reads'] = sorted(reads)
results['blocked_existing_reads'] = blocked
print(json.dumps(results, indent=2))
