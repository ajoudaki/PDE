"""Verify source syntax, protected bodies, payloads and digest literals."""
import ast
import hashlib
import json
from pathlib import Path

BASE = Path('/home/amir/Codes/PDE')
OUT = Path(__file__).parent
before = json.loads((OUT / 'before.json').read_text())
after = json.loads((OUT / 'after.json').read_text())
proof = json.loads((OUT / 'preservation.json').read_text())
expected = {
    'studies/mfp_gaussian_calculus/depth_order5/primary/build_self_contained_report.py': ['build'],
    'studies/mfp_gaussian_calculus/order5/compiler/test_population_jet.py': ['test_all_frozen_coefficient_comparisons_report_zero_discrepancies'],
    'studies/mfp_gaussian_calculus/study_paths.py': ['require_output'],
    'studies/stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py': ['validate_source'],
}
assert proof['changed_existing_functions'] == expected
assert proof['historical_files_unchanged']
assert proof['non_python_files_unchanged']
assert not proof['changed_existing_digest_literals']
name = 'studies/mfp_gaussian_calculus/depth_order5/primary/build_self_contained_report.py'
tree = ast.parse((BASE / name).read_text())
build = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'build')
assert isinstance(build.body[0], ast.Raise)
build.body = build.body[1:]
stripped = hashlib.sha256(ast.dump(build, include_attributes=False).encode()).hexdigest()
assert stripped == before['functions'][name]['build']
reducer = 'studies/mfp_gaussian_calculus/depth_order5_observables/independent/reduce_frozen_head.py'
assert before['functions'][reducer]['reduce'] == after['functions'][reducer]['reduce']
count = 0
for relative, record in after['files'].items():
    if record['group'] == 'source' and relative.endswith('.py'):
        compile((BASE / relative).read_bytes(), relative, 'exec')
        count += 1
summary = {
    'python_files_syntax_checked': count,
    'existing_top_level_functions_compared': proof['existing_functions_compared'],
    'unchanged_existing_top_level_functions': proof['existing_functions_compared'] - 4,
    'changed_functions_limited_to_interfaces': True,
    'report_build_body_identical_after_removing_new_guard': True,
    'pure_reduce_ast_sha256': after['functions'][reducer]['reduce'],
    'frozen_digest_literals_unchanged': True,
    'historical_files_unchanged': True,
    'formula_report_manifest_and_other_non_python_payloads_unchanged': True,
}
(OUT / 'verification.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
