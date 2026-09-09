import ast
import difflib
import hashlib
import json
from pathlib import Path

PRIVATE = Path(__file__).parent
REPO = Path('/home/amir/Codes/PDE')
before = json.loads((PRIVATE / 'before.json').read_text())
graded = 'studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py'
centered = 'studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py'
wrapper = 'studies/resnet_dense_long_horizon/reproduce.sh'

expected = {}
expected[graded] = before[graded]['text'].replace(
    '    args.output = require_distinct_output(args.output, (args.lower_result, args.binary))\n',
    '    args.output = require_distinct_output(\n'
    '        args.output,\n'
    '        (args.lower_result, args.binary, Path(__file__).with_name("graded_sector.cpp")),\n'
    '    )\n', 1)
expected[centered] = before[centered]['text'].replace(
    'from campaign_paths import INPUT_ROOT, OUTPUT_ROOT, recorded_sector_path\n',
    'from campaign_paths import INPUT_ROOT, OUTPUT_ROOT, recorded_sector_path, require_distinct_output\n', 1
).replace(
    '    args = parser.parse_args()\n',
    '    args = parser.parse_args()\n'
    '    output = require_distinct_output(\n'
    '        OUTPUT_ROOT / "centered_depth1_order13/RESULTS.json",\n'
    '        (Path(__file__), HERE / "PROTOCOL.md"),\n'
    '    )\n', 1
).replace('    output = OUTPUT_ROOT / "centered_depth1_order13/RESULTS.json"\n', '', 1)
expected[wrapper] = before[wrapper]['text'].replace(
    'cd "$study_dir"\n\n',
    'cd "$study_dir"\n\n'
    '# Validate and normalize once before dispatching tests or scientific work.\n'
    'run_dir="$(python -B -c \\\n'
    "  'import sys; from pathlib import Path; from make_manifest import validate_output_root; print(validate_output_root(Path(sys.argv[1])))' \\\n"
    '  "$run_dir")"\n\n', 1)
for name, text in expected.items():
    assert (REPO / name).read_text() == text, name

functions = {}
for name in (graded, centered):
    old_tree = ast.parse(before[name]['text'])
    new_tree = ast.parse((REPO / name).read_text())
    old_nodes = {n.name: n for n in old_tree.body if isinstance(n, ast.FunctionDef)}
    new_nodes = {n.name: n for n in new_tree.body if isinstance(n, ast.FunctionDef)}
    assert old_nodes.keys() == new_nodes.keys()
    functions[name] = {}
    for function, node in old_nodes.items():
        if function == 'main':
            continue
        old = ast.get_source_segment(before[name]['text'], node)
        new = ast.get_source_segment((REPO / name).read_text(), new_nodes[function])
        assert old == new
        functions[name][function] = hashlib.sha256(old.encode()).hexdigest()

changes = []
diff = []
hashes = {}
for name, previous in before.items():
    text = (REPO / name).read_text()
    digest = hashlib.sha256((REPO / name).read_bytes()).hexdigest()
    hashes[name] = {'before': previous['sha256'], 'after': digest}
    if text != previous['text']:
        changes.append(name)
        diff.extend(difflib.unified_diff(previous['text'].splitlines(keepends=True), text.splitlines(keepends=True), fromfile=name + ' (before this repair)', tofile=name))
assert set(changes) == set(expected) | {
    'studies/repository_refactor_2026_09_09/test_resnet_routing.py',
    'studies/repository_refactor_2026_09_09/test_quadratic_routing.py',
}
summary = {'changed_files': changes, 'exact_allowed_source_replacements_only': True, 'unchanged_calculation_functions': functions, 'file_hashes': hashes}
(PRIVATE / 'preservation.json').write_text(json.dumps(summary, indent=2) + '\n')
(PRIVATE / 'repair.diff').write_text(''.join(diff))
print(json.dumps({'changed_files': changes, 'exact_allowed_source_replacements_only': True, 'unchanged_non_main_functions': sum(len(v) for v in functions.values())}, indent=2))
