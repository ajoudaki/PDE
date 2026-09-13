"""Isolated integration checks; no initializer or evolution calls."""
import ast
import difflib
import hashlib
import importlib
import json
import re
import sys
from pathlib import Path

import numpy as np

root = Path.cwd().resolve()
scratch = Path(__file__).resolve().parent
repo = root.parents[3]
base = root.parent / 'H3_v2_integration_inputs_v3'
manifest = json.loads((root / 'review/manifest.json').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
result = {'status': 'pass', 'ast': [], 'imports': {}, 'new_links': [], 'runs': []}

chapter = (root / 'docs/global_nonlinear.md').read_bytes()
old = (base / 'base_global_nonlinear.md').read_bytes()
section = (root / 'review/proposed_section.md').read_bytes()
assert chapter.count(section) == 1
pos = chapter.index(section)
assert chapter == old[:pos] + section + b'\n' + old[pos:]
assert old[pos:].startswith(b'#### C.4.8.')
result['chapter'] = {'section_occurrences': 1, 'base_bytes_unchanged': True,
                     'insertion_byte_offset': pos, 'separator_bytes': 1,
                     'new_section_first_line': chapter[:pos].count(b'\n') + 1}
code_old = (base / 'base_code_README.md').read_text()
code_new = (root / 'code/README.md').read_text()
guide = (root / 'review/library_guide.md').read_text()
shifted_guide = '\n'.join('#' + line if line.startswith('#') else line
                          for line in guide.split('\n'))
assert code_new == code_old + '\n\n' + shifted_guide
result['code_guide_base_preserved_and_exact_append'] = True
doc_old = (base / 'base_docs_README.md').read_text()
doc_new = (root / 'docs/README.md').read_text()
diff = ''.join(difflib.unified_diff(doc_old.splitlines(True), doc_new.splitlines(True)))
(scratch / 'roadmap.diff').write_text(diff)
added = '\n'.join(line[1:] for line in diff.splitlines()
                  if line.startswith('+') and not line.startswith('+++'))
link_text = section.decode() + '\n' + shifted_guide + '\n' + added
# Remove LaTeX math before identifying actual Markdown links.
link_text = re.sub(r'\\\[.*?\\\]', '', link_text, flags=re.S)
link_text = re.sub(r'\\\(.*?\\\)', '', link_text, flags=re.S)
for label, target in re.findall(r'\[([^\[\]\n]+)\]\(([^)\n]+)\)', link_text):
    path, sep, fragment = target.partition('#')
    assert not path.startswith(('http:', 'https:'))
    target_path = root / 'docs' / path
    assert target_path.exists()
    if sep:
        headings = [re.sub(r'[^\w\- ]', '', line.lstrip('#').strip().lower()).replace(' ', '-')
                    for line in target_path.read_text().splitlines() if line.startswith('#')]
        assert fragment in headings
    result['new_links'].append({'label': label, 'target': target, 'resolved': True})
for rel in manifest['edition_hashes']:
    if not rel.endswith('.py'):
        continue
    body = (root / rel).read_text()
    tree = ast.parse(body, filename=rel)
    result['ast'].append(rel)
    if rel.startswith('code/pde/'):
        name = 'pde' if rel.endswith('__init__.py') else 'pde.' + Path(rel).stem
        module = importlib.import_module(name)
        assert Path(module.__file__).resolve() == (root / rel).resolve()
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports += [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                imports.append('.' * node.level + (node.module or ''))
        result['imports'][name] = {'path': str(Path(module.__file__).resolve()), 'imports': imports}
        assert not any(token in body for token in ('studies/', 'data/generated/', 'data/established/'))
for i, block in enumerate(re.findall(r'```python\n(.*?)```', guide, flags=re.S)):
    ast.parse(block, filename=f'library_guide_example_{i}')
result['guide_examples_parsed'] = i + 1

from pde.observable_solver import load_restart
runs = root / 'data/established/independent_v2_runs'
summary_path = root / 'data/established/independent_v2_analysis/summary.json'
summary = json.loads(summary_path.read_text())
fresh = json.loads((scratch / 'analysis/summary.json').read_text())
different = [k for k in summary if summary[k] != fresh[k]]
assert different == ['postprocessing_cpu_seconds']
assert (scratch / 'analysis/summary.md').read_bytes() == summary_path.with_suffix('.md').read_bytes()
result['regenerated_summary_differences'] = different
plan_path = root / 'code/validation/observable_solver_plan.json'
plan = json.loads(plan_path.read_text())
supervisor = json.loads((runs / 'supervisor.json').read_text())
assert summary['supervisor']['all_records'] == supervisor['configurations']
assert summary['supervisor']['sha256'] == sha(runs / 'supervisor.json')
assert summary['supervisor']['charged_total_cpu_seconds'] == supervisor['total_cpu_seconds']
assert [c['id'] for c in plan['configurations']] == [r['id'] for r in summary['runs']]
for config, row in zip(plan['configurations'], summary['runs']):
    folder = runs / config['id']
    record = json.loads((folder / 'record.json').read_text())
    assert record['configuration'] == config
    assert record['plan_sha256'] == sha(plan_path)
    assert record['restart_exact'] and record['status'] == 'operational_pass'
    assert row['recorded_source_hashes'] == record['source_hashes']
    assert row['output_hashes_verified'] == record['outputs']
    assert row['record_sha256'] == sha(folder / 'record.json')
    assert row['recorded_state_bytes_initial'] == record['state_bytes_initial']
    assert row['recorded_state_bytes_final'] == record['state_bytes_final']
    for k in row.keys() & record.keys():
        assert row[k] == record[k], (config['id'], k)
    final, law = load_restart(folder / 'final_restart.json')
    mid, midlaw = load_restart(folder / 'midpoint_restart.json')
    keys = ('b1', 'g', 'w', 'p1', 'b2', 'c', 'p2', 'M', 'D')
    assert set(vars(final)) == set(keys) | {'arithmetic', 'metadata'}
    for k in ('b1', 'g', 'p1', 'b2', 'p2', 'D'):
        assert np.array_equal(getattr(final, k), getattr(mid, k))
    for k in ('inputs', 'labels', 'probabilities'):
        assert np.array_equal(getattr(law, k), getattr(midlaw, k))
    a = {k: np.asarray(getattr(final, k), float) for k in keys}
    u = np.asarray(law.inputs, float)
    with np.load(folder / 'observations.npz', allow_pickle=False) as z:
        h10 = np.tanh(a['g'] @ u.T)
        h1 = np.tanh(a['w'] @ u.T)
        act = lambda matrix, h: a['b2'] @ (matrix @ (a['b1'].T @ (a['p1'][:, None] * h)))
        h20 = np.tanh(act(a['D'], h10))
        h2 = np.tanh(act(a['M'], h1))
        pred = a['p2'] @ (a['c'][:, None] * np.tanh(act(a['M'], np.tanh(a['w'] @ z['circle'].T))))
        err = {'first_pairs': float(np.max(np.abs(z['first_pairs'] - np.stack([h10, h1], axis=2)))),
               'second_pairs': float(np.max(np.abs(z['second_pairs'] - np.stack([h20, h2], axis=2)))),
               'prediction': float(np.max(np.abs(z['prediction'] - pred)))}
        assert max(err.values()) < 1e-12
        array_shapes = {k: list(z[k].shape) for k in z.files}
    result['runs'].append({'id': config['id'], 'state_schema': sorted(vars(final)),
                           'array_shapes': array_shapes, 'reconstruction_errors': err,
                           'frozen_marks_and_law_unchanged': True})

reproducer = root.parent / 'H3_v2_reproducer_v2'
entry = json.loads((reproducer / 'entry_hashes.json').read_text())
post = json.loads((reproducer / 'post_execution_hashes.json').read_text())
end = json.loads((reproducer / 'exit_hashes.json').read_text())
assert entry['files'] == post == end['edition_files']
assert entry['manifest_sha256'] == end['manifest_sha256'] == sha(root / 'review/manifest.json')
for item in post:
    assert item['expected'] == item['actual'] == manifest['edition_hashes'][item['path']]
raw = json.loads((reproducer / 'immutable_raw_evidence_hashes.json').read_text())
audit = json.loads((reproducer / 'read_only_audit.json').read_text())
assert audit['raw_immutable_checks'] == raw
for p, h in raw.items():
    assert sha(root / p) == h
for p, h in json.loads((reproducer / 'immutable_reproducer_files.json').read_text()).items():
    assert sha(Path(p)) == h
result['reproducer_machine_provenance'] = {'edition_rows_identical': len(post),
                                         'raw_rows_verified': len(raw),
                                         'human_report_not_read': True}
result['loaded_pde_modules'] = {name: str(Path(module.__file__).resolve())
                                for name, module in sys.modules.items()
                                if name == 'pde' or name.startswith('pde.')}
assert all(Path(p).is_relative_to(root / 'code') for p in result['loaded_pde_modules'].values())
(scratch / 'static_evidence_audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'pass', 'ast_files': len(result['ast']),
                  'package_imports': len(result['imports']), 'new_links': result['new_links'],
                  'guide_examples_parsed': result['guide_examples_parsed'],
                  'record_reconstructions': len(result['runs']),
                  'regenerated_summary_differences': different}))
