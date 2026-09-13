"""Hash approved frozen inputs and verify unified patch bytes without live files.

No candidate source is imported; no Git, test, trajectory, or live file is used.
Run from the checkout root. The output directory must not already exist.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
started = time.process_time()
root = Path(__file__).resolve().parents[2]
study = root / 'studies/observable_hierarchy'
edition = root / 'data/generated/observable_hierarchy/H3_v2_edition_v3'
out = root / 'data/generated/observable_hierarchy/H3_v2_promotion_integrity'
out.mkdir(exist_ok=False)
paths = {
    'proposal': study / 'H3_v2_promotion_proposal_v4.md',
    'mapping': study / 'H3_v2_promotion_mapping_v4.json',
    'patch': study / 'H3_v2_proposed_changes_v4.patch',
    'acceptance': study / 'H3_v2_review_acceptance_v4.md',
    'study_manifest': study / 'H3_v2_edition_v3_manifest.json',
    'frozen_manifest': edition / 'review/manifest.json',
    'scientific_a': study / 'H3_v2_scientific_a_v3.md',
    'scientific_b': study / 'H3_v2_scientific_b_v3.md',
    'integration': study / 'H3_v2_integration_v4.md',
}
allowed = set(paths.values())
opened = {}
comparisons = []
scope_checks = []


def rel(path):
    return str(path.relative_to(root))


def read(path):
    assert path in allowed, f'Outside authorized frozen inputs: {path}'
    if path not in opened:
        opened[path] = path.read_bytes()
    return opened[path]


def sha(value):
    return hashlib.sha256(value).hexdigest()


def match(path, expected, role):
    actual = sha(read(path))
    comparisons.append(dict(path=rel(path), role=role, expected=expected,
                            actual=actual, match=expected == actual))


def scope(name, condition, details=None):
    scope_checks.append(dict(check=name, match=bool(condition), details=details))


manifest = json.loads(read(paths['frozen_manifest']))
study_manifest = json.loads(read(paths['study_manifest']))
mapping = json.loads(read(paths['mapping']))
acceptance = read(paths['acceptance']).decode()
proposal = read(paths['proposal']).decode()
scope('identical study and frozen manifest bytes',
      read(paths['study_manifest']) == read(paths['frozen_manifest']))
scope('edition version and root', manifest['version'] == 'v3' and manifest['output'] == str(edition))
scope('27 frozen edition records', len(manifest['edition_hashes']) == 27)
for name, expected in manifest['edition_hashes'].items():
    assert not Path(name).is_absolute() and '..' not in Path(name).parts
    frozen = edition / name
    allowed.add(frozen)
    match(frozen, expected, 'frozen edition manifest')
    match(frozen, study_manifest['edition_hashes'][name], 'study edition manifest')
for name in ('frozen_manifest', 'study_manifest'):
    match(paths[name], mapping['edition_manifest_sha256'], 'approved mapping manifest identity')
accepted_manifest = re.search(r'The corrected edition manifest is\s*`([0-9a-f]{64})`', acceptance).group(1)
match(paths['frozen_manifest'], accepted_manifest, 'acceptance corrected edition identity')

# Exact destinations transcribed from the proposal's destination list, expanding
# its explicitly grouped directory shorthand. No mutable destination is opened.
declared = {
    'docs/global_nonlinear.md', 'docs/README.md', 'code/README.md',
    *('code/pde/observable_' + x + '.py' for x in
      ('fixed', 'arithmetic', 'words', 'compiler', 'initialization', 'solver')),
    *('code/tests/test_observable_' + x + '.py' for x in
      ('compiler', 'initialization', 'solver', 'validation')),
    'code/scripts/validate_observable_solver.py',
    'code/scripts/analyze_observable_solver.py',
    'code/scripts/run_observable_validation.py',
    'code/validation/observable_solver_plan.json',
}
scope('proposal, mapping and requested count agree',
      len(mapping['files']) == 17 and set(mapping['files']) == declared and
      'specify seventeen\nestablished paths' in proposal)
for name, row in mapping['files'].items():
    assert root / row['candidate_path'] == edition / name
    scope('mapped candidate path and manifest digest: ' + name,
          row['proposed_sha256'] == manifest['edition_hashes'][name])
    match(edition / name, row['proposed_sha256'], 'approved destination candidate')
scope('14 additions and three edits',
      sum(x['action'] == 'add' for x in mapping['files'].values()) == 14 and
      sum(x['action'] == 'edit' for x in mapping['files'].values()) == 3)
match(paths['patch'], mapping['patch_sha256'], 'approved mapping patch')
accepted_patch = re.search(r'its hash is `([0-9a-f]{64})`', acceptance).group(1)
match(paths['patch'], accepted_patch, 'acceptance patch identity')

report_patterns = {
    'scientific_a': r"Scientific A's report hash is\s*`([0-9a-f]{64})`",
    'scientific_b': r"scientific B's is\s*`([0-9a-f]{64})`",
    'integration': r'original `H3_v2_integration_v4.md`, whose hash is\s*`([0-9a-f]{64})`',
}
for name, pattern in report_patterns.items():
    expected = re.search(pattern, acceptance).group(1)
    match(paths[name], expected, 'accepted original report')

# Reverse each exact unified patch in memory from its frozen candidate. This
# validates new/context bytes and reconstructs the declared old bytes without
# touching live files, invoking patch/git, or writing candidate/base copies.
patch_lines = read(paths['patch']).splitlines(keepends=True)
blocks = []
index = 0
while index < len(patch_lines):
    assert patch_lines[index].startswith(b'--- ')
    old_name = patch_lines[index][4:].strip().decode()
    assert patch_lines[index + 1].startswith(b'+++ b/')
    name = patch_lines[index + 1][6:].strip().decode()
    index += 2
    hunks = []
    while index < len(patch_lines) and not patch_lines[index].startswith(b'--- '):
        header = re.fullmatch(rb'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@[^\n]*\n', patch_lines[index])
        assert header, patch_lines[index]
        old_start, old_count, new_start, new_count = (
            int(x) if x is not None else 1 for x in header.groups())
        index += 1
        old_bytes = []
        new_bytes = []
        while index < len(patch_lines) and not patch_lines[index].startswith((b'@@ ', b'--- ')):
            line = patch_lines[index]
            assert line[:1] in (b' ', b'+', b'-'), 'Unsupported patch encoding'
            if line[:1] in (b' ', b'-'):
                old_bytes.append(line[1:])
            if line[:1] in (b' ', b'+'):
                new_bytes.append(line[1:])
            index += 1
        assert len(old_bytes) == old_count and len(new_bytes) == new_count
        hunks.append((old_start, old_count, new_start, new_count, old_bytes, new_bytes))
    candidate = read(edition / name).splitlines(keepends=True)
    restored = []
    cursor = 0
    for old_start, old_count, new_start, new_count, old_bytes, new_bytes in hunks:
        position = new_start - 1 if new_count else new_start
        assert position >= cursor
        assert candidate[position:position + new_count] == new_bytes
        restored.extend(candidate[cursor:position])
        assert len(restored) == (old_start - 1 if old_count else old_start)
        restored.extend(old_bytes)
        cursor = position + new_count
    restored.extend(candidate[cursor:])
    base_bytes = b''.join(restored)
    row = mapping['files'][name]
    if row['action'] == 'add':
        scope('patch creates exact candidate: ' + name,
              old_name == '/dev/null' and row['base_sha256'] is None and base_bytes == b'')
    else:
        scope('patch reverses to declared base: ' + name,
              old_name == 'a/' + name and sha(base_bytes) == row['base_sha256'],
              dict(reconstructed_base_sha256=sha(base_bytes), expected_base_sha256=row['base_sha256']))
    blocks.append(name)
scope('patch has exactly the 17 unique approved destinations',
      len(blocks) == 17 and len(set(blocks)) == 17 and set(blocks) == declared)

unchanged = []
for path, before in opened.items():
    unchanged.append(dict(path=rel(path), sha256=sha(before), bytes=len(before),
                          unchanged=path.read_bytes() == before))
result = dict(actor='/root/h3v2_review_provenance',
              checked_at_utc=datetime.now(timezone.utc).isoformat(),
              method='Read-only frozen hashes and in-memory unified-patch reversal; no live file, Git, test, or trajectory.',
              limits=dict(cpu_seconds=60, address_space_bytes=1024**3),
              approval='Supervisor reports user approved the exact seventeen-file package: yes I approve.',
              comparisons=comparisons, scope_checks=scope_checks, input_inventory=unchanged,
              primary_counts=dict(frozen_edition_files=27, approved_destination_candidates=17,
                                  accepted_reports=3, approved_patch=1),
              hash_comparisons=len(comparisons), scope_check_count=len(scope_checks),
              passed=all(x['match'] for x in comparisons + scope_checks) and all(x['unchanged'] for x in unchanged),
              source=dict(path=rel(Path(__file__).resolve()), sha256=sha(Path(__file__).read_bytes())),
              cpu_seconds=time.process_time() - started,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
              limitations=[
                  'No mutable live book/code file or Git state was read; actual application and live correspondence remain the coordinator responsibility.',
                  'Approval is supplied by the supervisor; preapproval status wording in immutable archival inputs is retained as historical wording.',
                  'Scientific A/B reports remain bound to edition v2 and integration v4 to edition v3, as expressly explained in acceptance; this byte check does not adjudicate scientific gate reuse.',
                  'No fresh scientific review, scientific isolation claim, test rerun, or reproduction is made.',
              ])
result_path = out / 'result.json'
result_path.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(dict(passed=result['passed'], hash_comparisons=len(comparisons),
                      scope_checks=len(scope_checks), inputs=len(unchanged),
                      failures=[x for x in comparisons + scope_checks if not x['match']],
                      source=result['source'], result=rel(result_path),
                      result_sha256=sha(result_path.read_bytes()),
                      cpu_seconds=result['cpu_seconds'], peak_rss_bytes=result['peak_rss_bytes']), indent=2))
