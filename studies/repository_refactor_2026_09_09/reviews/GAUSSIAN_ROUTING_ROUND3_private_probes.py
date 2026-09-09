"""Private routing probes. All real writes stay below this directory.

No recurrence, coefficient generation, simulation, fitting, compilation or
training is executed. Existing digest constants are never patched.
"""
import ast
from contextlib import ExitStack, redirect_stdout
import hashlib
import importlib
import io
import json
from pathlib import Path
import shutil
import sys
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
FIX = OUT / 'private-fixtures'
FIX.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT))
records = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def case_dir(name):
    path = FIX / name
    path.mkdir()
    return path

def record(name, **fields):
    item = dict(name=name, **fields)
    records.append(item)
    print(json.dumps(item), flush=True)

def alias(path, target, kind):
    if kind == 'same':
        return target
    if kind == 'symlink':
        path.symlink_to(target)
    else:
        path.hardlink_to(target)
    return path

class StopBeforeScience(RuntimeError):
    pass

# No analytics are reached for an empty CSV. The complete actual main runs.
g2 = importlib.import_module('studies.causal_flow_peeling_calculus.experiments.analyze_g2_gate_defect')
for kind in ('same', 'symlink', 'hardlink'):
    directory = case_dir('g2-' + kind)
    source = directory / 'raw.csv'
    source.write_text('alpha,width,base_time,trial\n')
    output = alias(directory / 'summary.json', source, kind)
    before = sha(source)
    with mock.patch.object(sys, 'argv', [g2.__file__, '--input', str(source), '--output', str(output)]), redirect_stdout(io.StringIO()):
        g2.main()
    record('g2-input-alias', kind=kind, input=str(source), output=str(output), before=before, after=sha(source), overwritten=before != sha(source))

# Complete actual mains, only analytic functions mocked; input I/O is real.
for module_name, flag, patch_values in (
    ('analyze_middle_response', '--main', {'aggregate_runs': {}, 'interpretation': {}}),
    ('analyze_response_leverage', '--coarse', {'summarize': {}, 'verdict': {}}),
):
    module = importlib.import_module('studies.d3_arctan_closure_program.' + module_name)
    for kind in ('same', 'symlink', 'hardlink'):
        directory = case_dir(module_name + '-' + kind)
        source = directory / 'selected.jsonl'
        source.write_text('{"kind":"metadata"}\n')
        output = alias(directory / 'summary.json', source, kind)
        before = sha(source)
        with ExitStack() as stack:
            stack.enter_context(mock.patch.object(sys, 'argv', [module.__file__, flag, str(source), '--output', str(output)]))
            stack.enter_context(redirect_stdout(io.StringIO()))
            for function, value in patch_values.items():
                stack.enter_context(mock.patch.object(module, function, return_value=value))
            module.main()
        record(module_name + '-input-alias', kind=kind, input=str(source), output=str(output), before=before, after=sha(source), overwritten=before != sha(source))

marked = importlib.import_module('studies.causal_flow_peeling_calculus.experiments.analyze_marked_column_cavity')
directory = case_dir('marked-input-alias')
source_dir, output = directory / 'selected', directory / 'fresh'
source_dir.mkdir()
output.mkdir()
source = source_dir / 'raw_replacement.csv'
source.write_text('width,trial,time\n')
(output / 'summary.json').symlink_to(source)
before = sha(source)
with mock.patch.object(sys, 'argv', [marked.__file__, '--primary', str(source_dir), '--output', str(output)]), \
     mock.patch.object(marked, 'scaling_summary', return_value=[]), \
     mock.patch.object(marked, 'primary_decision', return_value={'decision': 'fixture'}), \
     mock.patch.object(marked, 'exact_sanity', return_value={'pass': True}), redirect_stdout(io.StringIO()):
    marked.main()
record('marked-summary-alias', input=str(source), output=str(output / 'summary.json'), before=before, after=sha(source), overwritten=before != sha(source))

# Full report main, real tiny input/rendering; compiler and PDF verification mocked.
report = importlib.import_module('studies.mfp_program_history.report.build_report')
directory = case_dir('history-report-alias')
source = directory / 'maintained.md'
source.write_text('Private interface fixture.\n')
output = directory / 'MEAN_FIELD_PEELING_REPORT.pdf'
output.symlink_to(source)
built = directory / 'mock-compiled.pdf'
built.write_bytes(b'private mock PDF bytes\n')
before = sha(source)
with mock.patch.object(report, 'SOURCES', (source,)), \
     mock.patch.object(report, 'BUILD_DIR', directory / 'build'), \
     mock.patch.object(report, 'MARKDOWN_DIR', directory / 'build/markdown'), \
     mock.patch.object(report, 'REPORT_PDF', output), \
     mock.patch.object(report, 'compile_report', return_value=built), \
     mock.patch.object(report, 'verify_pdf'), redirect_stdout(io.StringIO()):
    report.main()
record('history-report-publication-alias', input=str(source), output=str(output), before=before, after=sha(source), overwritten=before != sha(source), compilation='mock only')

# The archive's exposed writer is invoked with no roots, so expansion is never run.
writer = importlib.import_module('studies.mfp_gaussian_calculus.depth_order5.primary.generate_frozen_artifacts')
directory = case_dir('archive-helper')
source = directory / 'retained-input.json'
source.write_text('private retained fixture\n')
destination = directory / 'H3_UNIT_COEFFICIENTS.json'
destination.with_suffix('.json.tmp').symlink_to(source)
before = sha(source)
with mock.patch.object(writer, 'expand_coefficient_map', side_effect=StopBeforeScience('expansion forbidden')) as expansion:
    result = writer.write_coefficient_json(destination, 3, 'unit-Gram-M200000=1', {})
    expansion.assert_not_called()
record('archive-writer-temp-input-alias', input=str(source), output=str(destination), before=before, after=sha(source), overwritten=before != sha(source), refused=False, result=result)

# Bind a real accepted raw-input digest without ever decoding its scientific data.
post = importlib.import_module('studies.mfp_gaussian_calculus.depth_order5_scalar.multi_observable.audit.postprocess_h3_sine_regression')
curvature = importlib.import_module('studies.mfp_gaussian_calculus.depth_order5_scalar.multi_observable.audit.run_h3_curvature_extension')
historical_raw = ROOT / 'data/historical/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/H3_NORMALIZED_SINE_RAW.npz'
raw_before = sha(historical_raw) if historical_raw.is_file() else None
(OUT / 'raw-historical-before.json').write_text(json.dumps({str(historical_raw): raw_before}, indent=2) + '\n')
if raw_before != post.EXPECTED_RAW_SHA256:
    record('gaussian-selected-raw-alias-limit', expected=post.EXPECTED_RAW_SHA256, actual=raw_before, action='original failure preserved; dependent probe not run')
else:
    directory = case_dir('gaussian-postprocess-same-file')
    source = directory / 'H3_NORMALIZED_SINE_RESULT.json'
    shutil.copyfile(historical_raw, source)
    before = sha(source)
    import numpy as np
    small = {'widths': np.array([1, 2, 3]),
             'names': np.array(['layer2_gamma04', 'layer2_q4', 'layer3_gamma04', 'layer3_q4']),
             'values': np.zeros((3, 2, 4))}
    prediction = {'layers': {2: {'Gamma04': 0., 'Q4': 0.}, 3: {'Gamma04': 0., 'Q4': 0.}}}
    with mock.patch.object(post.np, 'load', return_value=small), \
         mock.patch.object(post, 'compile_numeric', return_value=prediction), \
         mock.patch.object(post, 'normalized_sine_moment', return_value=None), \
         mock.patch.object(post, 'affine_fit', return_value={'intercept': 0., 'intercept_se': 1.}):
        post.run(source, directory)
    record('gaussian-postprocess-same-input-output', input=str(source), before=before, after=sha(source), overwritten=before != sha(source), original_expected_digest=post.EXPECTED_RAW_SHA256, science='mocked')
    for leaf in ('H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RAW.npz', 'H3_NORMALIZED_SINE_CURVATURE_EXTENSION_RESULT.json'):
        directory = case_dir('curvature-' + leaf)
        source = directory / leaf
        shutil.copyfile(historical_raw, source)
        reached = False
        with mock.patch.object(curvature.np, 'load', side_effect=StopBeforeScience('stop before raw decode')):
            try:
                curvature.run(source, directory)
            except StopBeforeScience:
                reached = True
        record('curvature-named-output-is-input', input=str(source), output=str(directory / leaf), guard_and_original_digest_accepted=reached, input_preserved=sha(source) == raw_before, scope='stopped before decoding; later write evidenced in complete source body')
raw_after = sha(historical_raw) if historical_raw.is_file() else None
(OUT / 'raw-historical-after.json').write_text(json.dumps({str(historical_raw): raw_after}, indent=2) + '\n')
assert raw_before == raw_after

# Verify role binding only; no coefficients or mathematical document created.
hidden = importlib.import_module('studies.stieltjes_resolution.canonical_hidden_high_order.hidden_moment_hankel_audit')
for filename in ('production_hidden_recurrence.py', 'independent_hidden_recurrence.py'):
    directory = case_dir('duplicate-role-' + filename)
    document = {'source': {'file': filename, 'sha256': sha(hidden.HERE / filename)}}
    selected = directory / 'selected.json'
    selected.write_text(json.dumps(document))
    reached = False
    with mock.patch.object(hidden, 'exact_derivatives', side_effect=StopBeforeScience('stop after provenance')):
        try:
            hidden.build_audit(selected, selected)
        except StopBeforeScience:
            reached = True
    record('duplicate-hidden-source-role', source_role=filename, selected=str(selected), production_equals_independent=True, provenance_accepted=reached, scope='stopped before scientific fields')

(OUT / 'private-probes.json').write_text(json.dumps(records, indent=2) + '\n')
assert all(item.get('overwritten', True) for item in records)
