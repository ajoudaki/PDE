"""Private source/AST comparison only; no compiler, campaign, or seal renewal."""
import ast
import hashlib
import json
from pathlib import Path

root = Path('/tmp/pde-quadratic-worker-7eUHn2')
study = Path('/home/amir/Codes/PDE/studies/mfp_quadratic_compiler')
before = json.loads((root / 'before.json').read_text())
after = json.loads((root / 'after.json').read_text())
digest = lambda value: hashlib.sha256(value).hexdigest()
records = {}
changes = [path for path in sorted(set(before['hashes']) | set(after['hashes']))
           if before['hashes'].get(path) != after['hashes'].get(path)]
expected = {'README.md', 'campaign1/run_graded_campaign.py',
            'campaign5_b3/test_stage_a_provenance.py', 'campaign5_b3/test_stage_c_closed.py',
            'campaign6_f13_threshold/run_benchmark.py', 'campaign_paths.py', 'checkpoint_paths.h',
            'component_parallel.cpp', 'exact_graph_wick.py', 'sector_parallel.cpp', 'sector_parallel_reuse.cpp'}
assert set(changes) == {str(study / path) for path in expected} | {
    '/home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/test_quadratic_routing.py'}
records['changed_only_owned_interfaces_and_requested_readme'] = changes
historical = [path for path in before['hashes'] if '/data/historical/' in path]
assert all(before['hashes'][path] == after['hashes'][path] for path in historical)
records['historical_unchanged_count'] = len(historical)
assert not any('__pycache__' in path or path.endswith('.pyc') for path in after['hashes'])
records['source_bytecode_absent'] = True

# Reversing just the new include and pre-discovery identity guards must recover
# each complete native driver byte-for-byte. No evaluator/discovery code differs.
for name in ('component_parallel.cpp', 'sector_parallel.cpp', 'sector_parallel_reuse.cpp'):
    text = (study / name).read_text()
    text = text.replace('#include "checkpoint_paths.h"\n', '', 1)
    if name == 'sector_parallel_reuse.cpp':
        guard = ('  if (!distinct_checkpoint_output(sparse_checkpoint, source_checkpoint) ||\n'
                 '      (!target_prefix.empty() &&\n'
                 '       !distinct_checkpoint_output(sparse_checkpoint, target_prefix))) return 2;\n\n')
    else:
        guard = ('  if (!checkpoint.empty() &&\n'
                 '      !distinct_checkpoint_output(checkpoint + ".tmp", checkpoint)) return 2;\n')
        if name == 'sector_parallel.cpp':
            guard += '\n'
    assert text.count(guard) == 1
    restored = digest(text.replace(guard, '', 1).encode())
    assert restored == before['hashes'][str(study / name)]['sha256'], name
    records[name + '_only_interface_insertions'] = restored

changed_functions = {}
for path, functions in before['python_functions'].items():
    changed_names = [name for name, value in functions.items()
                     if after['python_functions'][path].get(name) != value]
    if changed_names:
        changed_functions[str(Path(path).relative_to(study))] = changed_names
assert changed_functions == {
    'campaign1/run_graded_campaign.py': ['main'],
    'campaign5_b3/test_stage_a_provenance.py': ['test_stage_a_durable_hashes_and_status',
                                             'test_stage_b_durable_hashes_caps_and_novelty'],
    'campaign5_b3/test_stage_c_closed.py': ['test_projection_is_terminally_unauthorized'],
    'campaign6_f13_threshold/run_benchmark.py': ['main'],
    'campaign_paths.py': ['require_new_output'],
    'exact_graph_wick.py': ['main'],
}
records['changed_python_functions_only'] = changed_functions

class RestoreEvidenceName(ast.NodeTransformer):
    def visit_Name(self, node):
        if node.id == 'DATA':
            node.id = 'HERE'
        return node

for name in ('campaign5_b3/test_stage_a_provenance.py', 'campaign5_b3/test_stage_c_closed.py'):
    path = study / name
    tree = RestoreEvidenceName().visit(ast.parse(path.read_text()))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            assert digest(ast.dump(node, include_attributes=False).encode()) == before['python_functions'][str(path)][node.name]
    records[name + '_assertions_preserved_except_evidence_root'] = True

for name in ('exact_graph_wick.py', 'campaign1/run_graded_campaign.py'):
    path = study / name
    tree = ast.parse(path.read_text())
    main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'main')
    # Remove only the newly inserted output-identity statement to compare the
    # complete original CLI body, including all authorization/hash/math gates.
    removed = [node for node in main.body if 'require_distinct_output' in ast.dump(node)]
    assert len(removed) == 1
    main.body.remove(removed[0])
    assert digest(ast.dump(main, include_attributes=False).encode()) == before['python_functions'][str(path)]['main']
    records[name + '_main_otherwise_ast_identical'] = True

for name in ('campaign5_b3/run_stage_c.py', 'campaign1/graded_sector.cpp',
             'campaign5_b3/b3_connected.cpp', 'campaign5_b3/b3_reference.py',
             'campaign5_b3/stage_c_sector.cpp', 'export_evaluator_reference.cpp',
             'CURRENT_SOURCE_SHA256.txt', 'HISTORICAL_SOURCE_HASHES.txt',
             'campaign6_f13_threshold/FROZEN_PROTOCOL_SHA256.txt'):
    path = str(study / name)
    assert before['hashes'][path] == after['hashes'][path]
    records[name + '_byte_unchanged_sha256'] = after['hashes'][path]['sha256']

readme_note = ('Current CLI limitation (static inspection only): `export_evaluator_reference.cpp`\n'
              'applies the requested power filter only for `terms.txt power` (`argc == 3`).\n'
              'The advertised extra-argument forms `terms.txt power term_limit` and\n'
              '`terms.txt power start length` leave that filter disabled. This known legacy\n'
              'limitation is unchanged and outside the migration interface repair; it is not\n'
              'a numerical validation result. Do not interpret those extra-argument forms as\n'
              'power-filtered evaluations.\n\n')
text = (study / 'README.md').read_text()
assert text.count(readme_note) == 1
assert digest(text.replace(readme_note, '', 1).encode()) == before['hashes'][str(study / 'README.md')]['sha256']
records['readme_only_requested_current_limits_note'] = True
records['native_validation_limit'] = 'Source inspection only; no compilation or native execution.'
print(json.dumps(records, indent=2, sort_keys=True))
