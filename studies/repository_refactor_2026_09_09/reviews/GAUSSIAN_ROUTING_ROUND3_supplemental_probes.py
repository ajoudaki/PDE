"""Additional private, bounded interface witnesses; no scientific evaluation."""
import ast
from contextlib import redirect_stdout
import hashlib
import importlib
import io
import json
from pathlib import Path
import sys
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
FIX = OUT / 'supplemental-fixtures'
FIX.mkdir()
sys.path.insert(0, str(ROOT))
records = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

tail = importlib.import_module('studies.causal_flow_peeling_calculus.experiments.analyze_d3_reachable_tail')
for role in ('primary', 'step', 'metadata'):
    directory = FIX / ('reachable-tail-' + role)
    directory.mkdir()
    primary, step, metadata = (directory / leaf for leaf in ('primary.csv', 'step.csv', 'metadata.json'))
    primary.write_text('width,trial,time,clip\n')
    step.write_text('width,trial,time,clip\n')
    metadata.write_text('{"dt":0.01}\n')
    selected = {'primary': primary, 'step': step, 'metadata': metadata}[role]
    before = sha(selected)
    with mock.patch.object(sys, 'argv', [tail.__file__, '--primary', str(primary), '--step', str(step), '--output', str(selected)]), redirect_stdout(io.StringIO()):
        tail.main()
    records.append(dict(name='reachable-tail-input-alias', role=role, input=str(selected), output=str(selected), before=before, after=sha(selected), overwritten=before != sha(selected), science='empty rows; analytics not reached'))

first = importlib.import_module('studies.d3_arctan_closure_program.analyze_first_passage_cooperative')
for kind in ('same', 'symlink', 'hardlink'):
    directory = FIX / ('first-passage-' + kind)
    directory.mkdir()
    selected = directory / 'first_passage_fixture.npz'
    selected.write_bytes(b'private routing fixture; not an NPZ panel\n')
    destination = selected if kind == 'same' else directory / 'summary.json'
    if kind == 'symlink':
        destination.symlink_to(selected)
    elif kind == 'hardlink':
        destination.hardlink_to(selected)
    before = sha(selected)
    with mock.patch.object(sys, 'argv', [first.__file__, '--input-dir', str(directory), '--output', str(destination)]), mock.patch.object(first, 'summarize', return_value={'path': str(selected), 'width': 1}) as summarize, redirect_stdout(io.StringIO()):
        first.main()
        summarize.assert_called_once_with(selected)
    records.append(dict(name='first-passage-input-alias', kind=kind, input=str(selected), output=str(destination), before=before, after=sha(selected), overwritten=before != sha(selected), science='summarize mocked; no panel decoding'))

# Complete bodies were inspected. Record concrete selections and original write
# statements, without executing any NPZ analysis, statistics or bootstrap.
static = []
for filename, input_leaf, output_fields in (
    ('analyze_gpu_forward_query_budget.py', 'forward_query_main_n256.npz', ('output',)),
    ('analyze_gpu_middle_saturation.py', 'middle_saturation_main_n512.npz', ('output_json', 'output_md')),
    ('analyze_gpu_paired_cavity_product.py', 'paired_product_main_h001_fp32_n128.npz', ('output',)),
    ('analyze_gpu_susceptibility_trace.py', 'susceptibility_main_n128_h0.02_T1.npz', ('json_output', 'md_output')),
):
    source = ROOT / 'studies/d3_arctan_closure_program' / filename
    content = source.read_text()
    tree = ast.parse(content)
    main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'main')
    writers = []
    for node in ast.walk(main):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'write_text':
            base = node.func.value
            if isinstance(base, ast.Attribute) and isinstance(base.value, ast.Name) and base.value.id == 'args' and base.attr in output_fields:
                writers.append({'field': base.attr, 'line': node.lineno, 'statement': ast.get_source_segment(content, node)})
    assert {item['field'] for item in writers} == set(output_fields)
    calls = [ast.unparse(node.func) for node in ast.walk(main) if isinstance(node, ast.Call)]
    assert not any('require_output' in call or 'samefile' in call or 'reject_output_links' in call for call in calls)
    static.append({'source': str(source), 'main_start': main.lineno, 'main_end': main.end_lineno, 'selected_input_leaf': input_leaf, 'writers': writers, 'witness': 'Set the stated output argument to this selected input inside --input-dir; the completed main writes unconditionally after analysis.', 'evidence_level': 'complete-body static inspection; scientific stages not executed'})

# Read only retained source metadata for exact original hash-gate evidence.
hidden = importlib.import_module('studies.stieltjes_resolution.canonical_hidden_high_order.hidden_moment_hankel_audit')
limits = []
for path, name in ((hidden.PRODUCTION_RESULT, 'production_hidden_recurrence.py'), (hidden.INDEPENDENT_RESULT, 'independent_hidden_recurrence.py')):
    before = sha(path)
    document = json.loads(path.read_text())
    try:
        hidden.validate_source(document, path)
    except AssertionError as exc:
        failure = str(exc)
    else:
        raise AssertionError('original retained source failure unexpectedly disappeared')
    limits.append({'result_path': str(path), 'result_sha256_before': before, 'result_sha256_after': sha(path), 'recorded_source': document['source'], 'current_source_path': str(hidden.HERE / name), 'current_source_sha256': sha(hidden.HERE / name), 'original_failure': failure, 'reset_or_authorization_change': False})

assert all(record['overwritten'] for record in records)
(OUT / 'supplemental-probes.json').write_text(json.dumps(records, indent=2) + '\n')
(OUT / 'static-alias-witnesses.json').write_text(json.dumps(static, indent=2) + '\n')
(OUT / 'preserved-hash-limits.json').write_text(json.dumps(limits, indent=2) + '\n')
print(json.dumps({'private_alias_witnesses': len(records), 'static_analyzer_witnesses': len(static), 'original_source_hash_failures_preserved': len(limits)}, indent=2))
