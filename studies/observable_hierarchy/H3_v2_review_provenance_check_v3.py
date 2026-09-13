"""Static archival check only: hash frozen bytes and copy retained review sources.

No review or candidate source is imported or executed. Run from the checkout root:
python3 -B studies/observable_hierarchy/H3_v2_review_provenance_check_v3.py
"""
from pathlib import Path
from collections import defaultdict
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
data = root / 'data/generated/observable_hierarchy'
tags = ('scientific_a', 'scientific_b', 'integration')
directories = {tag: data / f'H3_v2_{tag}_v3' for tag in tags}
reports = {tag: study / f'H3_v2_{tag}_v3.md' for tag in tags}
sha_re = re.compile(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])')
cache = {}
checks = []
limitations = []


def relative(path):
    return str(path.relative_to(root))


def path_for(name):
    p = Path(name)
    return p if p.is_absolute() else root / p


def digest(path):
    if path not in cache:
        h = hashlib.sha256()
        size = 0
        with path.open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                size += len(chunk)
                h.update(chunk)
        cache[path] = (h.hexdigest(), size)
    return cache[path]


def check(path, expected, origin, field, expected_bytes=None):
    item = dict(path=relative(path), origin=origin, field=field, expected=expected)
    try:
        actual, size = digest(path)
        item.update(actual=actual, bytes=size, match=actual == expected)
        if expected_bytes is not None:
            item['expected_bytes'] = expected_bytes
            item['bytes_match'] = size == expected_bytes
            item['match'] = item['match'] and item['bytes_match']
    except OSError as error:
        item.update(match=False, error=str(error))
    checks.append(item)
    return item


def records(obj):
    if isinstance(obj, list):
        return obj
    if 'files' in obj:
        return obj['files']
    return [dict(path=path, **row) for path, row in obj.items()]


ledger_counts = {}
ledger_paths = {}
allowed = set(reports.values())
original_map = study / 'H3_v2_review_sources_v3.json'
allowed.add(original_map)
for directory in directories.values():
    allowed.update(p for p in directory.rglob('*') if p.is_file())
original_inventory = sorted(allowed)
ledgers = {}
for tag, directory in directories.items():
    ledger_paths[tag] = {}
    for boundary in ('entry', 'exit'):
        path = directory / f'{boundary}_hashes.json'
        obj = json.loads(path.read_text())
        rows = records(obj)
        ledgers[(tag, boundary)] = obj
        ledger_counts[f'{tag}_{boundary}'] = len(rows)
        ledger_paths[tag][boundary] = {path_for(row['path']) for row in rows}
        allowed.update(ledger_paths[tag][boundary])
        for row in rows:
            target = path_for(row['path'])
            for key, value in row.items():
                if isinstance(value, str) and sha_re.fullmatch(value):
                    check(target, value, relative(path), key, row.get('bytes'))
    if ledger_paths[tag]['entry'] != ledger_paths[tag]['exit']:
        limitations.append(f'{tag}: entry and exit path sets differ.')

assignment = study / 'H3_v2_scientific_assignment_v3.md'
check(assignment, ledgers[('scientific_b', 'exit')]['assignment_sha256'],
      relative(directories['scientific_b'] / 'exit_hashes.json'), 'assignment_sha256')

# Resolve report hashes to the exact authorized inputs, using explicit table
# paths where available and unique frozen digests for descriptive labels.
paths_by_digest = defaultdict(list)
for path in sorted(allowed):
    try:
        paths_by_digest[digest(path)[0]].append(path)
    except OSError:
        pass
report_hash_counts = {}
for tag, report in reports.items():
    count = 0
    for line_number, line in enumerate(report.read_text().splitlines(), 1):
        hashes = sha_re.findall(line)
        for expected in hashes:
            targets = []
            if line.startswith('|'):
                label = line.split('|')[1]
                path_tokens = re.findall(r'`([^`]+)`', label)
                if path_tokens:
                    token = path_tokens[0]
                    if token.startswith('E/'):
                        target = data / 'H3_v2_edition_v2' / token[2:]
                    elif token.startswith('R/'):
                        target = data / 'H3_v2_reproducer_v2' / token[2:]
                    elif token.startswith(('studies/', 'data/', '/')):
                        target = path_for(token)
                    elif token.startswith('review/'):
                        target = data / 'H3_v2_edition_v2' / token
                    elif token.startswith('H3_'):
                        target = study / token
                    else:
                        target = directories[tag] / token
                    if target in allowed:
                        targets = [target]
            if not targets:
                targets = paths_by_digest[expected]
            if not targets:
                limitations.append(f'Unresolved report hash: {relative(report)}:{line_number} {expected}')
            for target in targets:
                check(target, expected, f'{relative(report)}:{line_number}', 'report_hash')
            count += 1
    report_hash_counts[tag] = count

# B's contemporaneous completion inventory binds its original report and every
# other original scratch artifact. A records its artifact hashes in the report.
completion_path = directories['scientific_b'] / 'completion.json'
completion = json.loads(completion_path.read_text())
check(path_for(completion['report']), completion['report_sha256'],
      relative(completion_path), 'report_sha256', completion['bytes'])
for name, expected in completion['scratch_artifacts'].items():
    check(directories['scientific_b'] / name, expected,
          relative(completion_path), f'scratch_artifacts.{name}')
tests_result = directories['scientific_a'] / 'tests_result.json'
check(directories['scientific_a'] / 'tests.log',
      json.loads(tests_result.read_text())['log_sha256'], relative(tests_result), 'log_sha256')
render_result = directories['integration'] / 'render_check.json'
render = json.loads(render_result.read_text())
check(path_for(render['source']), render['source_sha256'], relative(render_result), 'source_sha256')

sources = []


def preserve(source, destination, reviewer, role, expected=None, copy=True):
    original_bytes = source.read_bytes()
    sha = hashlib.sha256(original_bytes).hexdigest()
    existed = destination.exists()
    if not existed and copy:
        with destination.open('xb') as stream:
            stream.write(original_bytes)
    copied_bytes = destination.read_bytes()
    equal = original_bytes == copied_bytes
    if not equal:
        raise RuntimeError(f'Refusing to overwrite nonidentical existing destination: {destination}')
    if expected is not None:
        check(source, expected, relative(original_map), 'sha256')
        check(destination, expected, relative(original_map), 'retained_sha256')
    sources.append(dict(original_path=relative(source), flat_copy=relative(destination),
                        sha256=sha, bytes=len(original_bytes), role=role, reviewer=reviewer,
                        byte_identical=equal, already_present=existed))


roles_a = {
    'checkpoint_checks': 'Independent read-only saved-checkpoint and observation reconstruction source.',
    'exit_hashes': 'Exit frozen-input immutability checker.',
    'finish_report': 'Original review report assembly source; retained as an archival source, not executed.',
    'run_tests': 'Bounded frozen-suite launch and recording source.',
    'scalar_checks': 'Independent scalar, arithmetic, kernel, law, and boundary check source.',
    'source_correspondence': 'Frozen dependency and proposal text-correspondence source.',
}
for source in sorted(directories['scientific_a'].glob('*.py')):
    preserve(source, study / f'H3_v2_review_a_{source.stem}_v3.py',
             '/root/h3v2_scientific_a_v3', roles_a[source.stem])

for source in sorted(directories['integration'].glob('*.py')):
    role = ('Preserved failed static link-audit attempt; exact original variant.'
            if '_attempt' in source.stem else {
                'bounded_command': 'Bounded launch wrapper; byte-identical to the frozen reproduction wrapper.',
                'render_check': 'Exact Markdown rendering witness for the original integration objection.',
                'static_evidence_audit': 'Final complete static/evidence audit source; records the rendering objection.',
            }[source.stem])
    preserve(source, study / f'H3_v2_review_integration_{source.stem}_v3.py',
             '/root/h3v2_integration_v3', role)
preserve(directories['integration'] / 'predeclared.md',
         study / 'H3_v2_review_integration_predeclared_v3.md',
         '/root/h3v2_integration_v3', 'Original integration preregistration.')

for row in json.loads(original_map.read_text())['sources']:
    preserve(path_for(row['executed_or_recorded_source']), path_for(row['retained_source']),
             row['reviewer'], 'Previously preserved scientific B review source or preregistration.',
             row['sha256'], copy=False)
# B's wrapper was copied from the same frozen source, so its complete durable
# mapping uses the verified identical integration copy without creating a duplicate.
preserve(directories['scientific_b'] / 'bounded_command.py',
         study / 'H3_v2_review_integration_bounded_command_v3.py',
         '/root/h3v2_scientific_b_v3', 'Shared bounded wrapper; exact identity with the integration copy.',
         copy=False)
wrapper = study / 'H3_v2_reproduction_budget_wrapper_v2.py'
for tag in ('scientific_b', 'integration'):
    check(directories[tag] / 'bounded_command.py', digest(wrapper)[0],
          relative(wrapper), 'copied_wrapper_sha256')

report_inventory = []
for tag, report in reports.items():
    sha, size = digest(report)
    report_inventory.append(dict(path=relative(report), sha256=sha, bytes=size,
                                 historical_report_digest_available=tag == 'scientific_b'))
limitations.extend([
    'Only B has a separate contemporaneous completion record of the original report digest; A and integration report digests are newly recorded here.',
    'B records an initial failed relative-path wrapper-copy setup in its report as transcript-only; no separate local command/result file for that prelaunch setup failure is present in the allowed scratch.',
    'Some ledger construction and source-correspondence operations were inline reviewer commands. No separate handwritten source file is present for those operations; retained ledgers/results and report descriptions are preserved, not reconstructed.',
    'The integration attempt commands all name static_evidence_audit.py; preserved attempt1 through attempt4 snapshots and tracebacks identify the variants, but the commands do not contain contemporaneous source digests.',
    'A preregistrations are embedded in the unchanged original flat scientific A report; there is no separate scratch preregistration file to copy.',
    'Byte identity verifies retained records and current inputs; it does not independently establish historical execution, complete scientific reading, reviewer isolation, or scientific correctness.',
])

outcomes = []
for tag, directory in directories.items():
    for path in sorted(directory.glob('*_result.json')):
        value = json.loads(path.read_text())
        if 'exit_code' in value:
            outcomes.append(dict(reviewer=tag, record=relative(path),
                                 exit_code=value['exit_code'], stopped=value.get('stopped'),
                                 cpu_seconds=value.get('reaped_cpu_seconds', value.get('cpu_seconds'))))

inventory = []
for path in original_inventory:
    sha, size = digest(path)
    # Re-read all original scratch/reports after archival copying, avoiding the
    # hash cache, to check this task did not modify any original evidence.
    current = hashlib.sha256(path.read_bytes()).hexdigest()
    inventory.append(dict(path=relative(path), sha256=sha, bytes=size,
                          unchanged_after_preservation=current == sha))

failures = [item for item in checks if not item['match']]
result = dict(schema='H3_v2_review_sources_complete_v3',
              checked_at_utc=datetime.now(timezone.utc).isoformat(),
              actor='/root/h3v2_review_provenance',
              method='SHA-256 streaming of exact ledger-assigned bytes; report hash association and byte-for-byte source preservation; no scientific code executed.',
              limits=dict(cpu_seconds=60, address_space_bytes=1024**3),
              sources=sources, original_reports=report_inventory,
              verification=dict(ledger_counts=ledger_counts,
                                unique_frozen_paths=len(set().union(*[v for p in ledger_paths.values() for v in p.values()])),
                                report_hash_occurrences=report_hash_counts,
                                comparisons=len(checks), failed_comparisons=len(failures),
                                all_originals_unchanged=all(x['unchanged_after_preservation'] for x in inventory),
                                checks=checks, original_artifact_inventory=inventory),
              historical_command_outcomes=outcomes, limitations=limitations,
              resource_usage=dict(cpu_seconds=time.process_time() - started,
                                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024))
destination = study / 'H3_v2_review_sources_complete_v3.json'
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(dict(output=relative(destination), sources=len(sources),
                      new_flat_copies=sum(not s['already_present'] for s in sources),
                      ledger_counts=ledger_counts,
                      unique_frozen_paths=result['verification']['unique_frozen_paths'],
                      report_hash_occurrences=report_hash_counts, comparisons=len(checks),
                      failures=failures, originals_unchanged=result['verification']['all_originals_unchanged'],
                      historical_command_outcomes=outcomes,
                      resource_usage=result['resource_usage']), indent=2))
