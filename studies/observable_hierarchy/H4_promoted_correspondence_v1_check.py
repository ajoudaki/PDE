"""Read-only/static H4 v3 installation correspondence; executes no candidate code."""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import posixpath
import re
import resource
import time
from urllib.parse import unquote

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
started_cpu = time.process_time()
ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/observable_hierarchy'
PREFIX = STUDY / 'H4_promoted_correspondence_v1'
EDITION = ROOT / 'data/generated/observable_hierarchy/H4_candidate_v3'
sources = {}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path, purpose):
    data = path.read_bytes()
    sources[str(path.relative_to(ROOT))] = {
        'sha256': digest(data), 'bytes': len(data), 'purpose': purpose,
    }
    return data


checks = []


def check(name, condition, **evidence):
    checks.append({'name': name, 'status': 'PASS' if condition else 'FAIL', **evidence})


mapping_raw = read(STUDY / 'H4_promotion_mapping_v3_final.json', 'approved mapping identity and destination metadata')
mapping = json.loads(mapping_raw)
review_raw = read(STUDY / 'H4_review_manifest_v3.json', 'identity only; no named non-edition contents opened')
edition_raw = read(EDITION / 'edition_manifest.json', 'edition file identities and correspondence metadata')
edition = json.loads(edition_raw)
for name in ('AGENTS.md', 'RESEARCH_WORKFLOW.md'):
    read(ROOT / name, 'shared process instructions')
check('frozen manifest identities',
      digest(review_raw) == mapping['review_manifest_sha256']
      and digest(edition_raw) == mapping['edition_manifest_sha256'],
      mapping_sha256=digest(mapping_raw), review_manifest_sha256=digest(review_raw),
      edition_manifest_sha256=digest(edition_raw))

destinations = {row['destination']: row for row in mapping['destinations']}
edition_files = {row['destination']: row for row in edition['files']}
inherited = {name for name, row in edition_files.items() if row['kind'] == 'unchanged dependency'}
check('approved scope partitions complete edition',
      len(destinations) == len(mapping['destinations']) == 11
      and len(edition_files) == len(edition['files']) == 31
      and len(inherited) == 20
      and set(destinations).isdisjoint(inherited)
      and set(destinations) | inherited == set(edition_files),
      installed_destination_count=len(destinations), inherited_dependency_count=len(inherited),
      edition_destination_count=len(edition_files))
check('approved and edition destination hashes agree',
      all(row['destination_sha256'] == edition_files[name]['destination_sha256']
          for name, row in destinations.items()))

file_records = []
live_files = {}
for name, row in edition_files.items():
    candidate = read(EDITION / name, 'complete byte hash; frozen edition file')
    live = read(ROOT / name, 'complete byte hash; installed destination')
    live_files[name] = live
    record = {
        'destination': name,
        'role': 'inherited dependency' if name in inherited else 'approved installation',
        'expected_sha256': row['destination_sha256'],
        'candidate_sha256': digest(candidate), 'live_sha256': digest(live),
        'candidate_bytes': len(candidate), 'live_bytes': len(live),
        'byte_identical': candidate == live,
    }
    record['status'] = 'PASS' if candidate == live and digest(live) == row['destination_sha256'] else 'FAIL'
    file_records.append(record)
check('all 31 live destinations equal frozen edition and declared hashes',
      all(row['status'] == 'PASS' for row in file_records), files=file_records)
check('all 20 inherited dependencies preserved',
      all(row['status'] == 'PASS' for row in file_records if row['role'] == 'inherited dependency'))

chapter = live_files['docs/global_nonlinear.md']
d_heading = b'###### D.1. Computation through physical time 40: fixed family and target\n'
c48_heading = b'#### C.4.8. Sampling fluctuations of the trained prediction\n'
c4710_heading = b'##### C.4.7.10. Finite numerical autonomous observable closure\n'
start = chapter.index(d_heading)
end = chapter.index(c48_heading)
insertion = chapter[start:end]
source_section = insertion[:-1]
restored = chapter[:start] + chapter[end:]
chapter_mapping = destinations['docs/global_nonlinear.md']
check('exact D source and separator removal restores every old chapter byte',
      insertion.endswith(b'\n')
      and digest(source_section) == chapter_mapping['source_sha256']
      and digest(restored) == chapter_mapping['current_live_sha256'],
      start_byte_zero_based=start, end_byte_exclusive=end,
      insertion_bytes=len(insertion), insertion_sha256=digest(insertion),
      source_section_bytes=len(source_section), source_section_sha256=digest(source_section),
      added_separator='one LF after the exact source section',
      restored_old_chapter_bytes=len(restored), restored_old_chapter_sha256=digest(restored),
      expected_old_chapter_sha256=chapter_mapping['current_live_sha256'])
check('D is inside C.4.7.10 immediately before C.4.8',
      chapter.count(d_heading) == chapter.count(c48_heading) == chapter.count(c4710_heading) == 1
      and chapter.index(c4710_heading) < start < end
      and [line for line in insertion.splitlines() if line.startswith(b'###### D.')] == [
          b'###### D.1. Computation through physical time 40: fixed family and target',
          b'###### D.2. Explicit supported time-40 construction',
          b'###### D.3. Compatible closure on the explicit time-40 domain',
          b'###### D.4. Finite numerical limits and whole-circle evaluation',
          b'###### D.5. Executable representation, storage and bounded validation'],
      c4710_line=chapter[:chapter.index(c4710_heading)].count(b'\n') + 1,
      d1_line=chapter[:start].count(b'\n') + 1,
      c48_line=chapter[:end].count(b'\n') + 1)

runtime_names = [
    'code/pde/observable_laws.py', 'code/scripts/validate_observable_horizon.py',
    'code/scripts/run_observable_validation.py', 'code/scripts/analyze_observable_horizon.py',
]
runtime_records = []
trees = {}
for name in runtime_names:
    text = live_files[name].decode()
    tree = ast.parse(text, filename=name)
    trees[name] = tree
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend({'line': node.lineno, 'module': alias.name} for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append({'line': node.lineno, 'module': node.module, 'level': node.level})
    hits = [{'line': i, 'text': line} for i, line in enumerate(text.splitlines(), 1)
            if re.search(r'\bstudies\b|data/generated|sys\.path|importlib|__import__', line)]
    runtime_records.append({'path': name, 'imports': imports, 'forbidden_path_or_dynamic_import_hits': hits})
check('new runtime files parse and have no study imports or path dependence',
      not any(row['forbidden_path_or_dynamic_import_hits'] for row in runtime_records)
      and not any((item['module'] or '').startswith('studies')
                  for row in runtime_records for item in row['imports']),
      runtime_files=runtime_records,
      method='AST parse plus full-file static search; no imports or runtime execution')


def flags(tree):
    return sorted({arg.value for node in ast.walk(tree)
                   if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                   and node.func.attr == 'add_argument'
                   for arg in node.args if isinstance(arg, ast.Constant)
                   and isinstance(arg.value, str) and arg.value.startswith('--')})


guide = live_files['code/README.md'].decode()
guide_section = guide.split('## Observable computation through physical time 40\n', 1)[1]
recipe = re.search(r'### Maintained bounded recipe\n.*?```text\n(.*?)```', guide_section, re.S).group(1)
runner_flags = flags(trees['code/scripts/run_observable_validation.py'])
worker_flags = flags(trees['code/scripts/validate_observable_horizon.py'])
analyzer_flags = flags(trees['code/scripts/analyze_observable_horizon.py'])
plan = json.loads(live_files['code/validation/observable_horizon_plan.json'])
ids = [row['id'] for row in plan['configurations']]
check('affected guide recipe names installed plan scripts and supported CLI flags',
      all(token in recipe for token in [
          'code/scripts/run_observable_validation.py', 'code/validation/observable_horizon_plan.json',
          '--worker validate_observable_horizon.py', 'code/scripts/analyze_observable_horizon.py',
          'data/established/observable_horizon_check', 'data/established/observable_horizon_analysis',
          'H4_LAW_TEST_SCRATCH="$observable_test_scratch"',
          'H4_VALIDATION_TEST_SCRATCH="$observable_test_scratch"',
          'TMPDIR="$observable_test_scratch"'])
      and set(['--plan', '--worker', '--output-dir']) <= set(runner_flags)
      and set(['--plan', '--id', '--output']) <= set(worker_flags)
      and set(['--plan', '--runs', '--output']) <= set(analyzer_flags)
      and len(ids) == len(set(ids)) == 14,
      recipe=recipe, runner_cli_flags=runner_flags, worker_cli_flags=worker_flags,
      analyzer_cli_flags=analyzer_flags, plan_configuration_ids=ids,
      execution='not run: assignment prohibits tests and training')
runner = live_files['code/scripts/run_observable_validation.py'].decode()
check('guide-selected worker is resolved beside the supervisor and receives code import path',
      'worker = (selected if selected.is_absolute() else here / selected).resolve()' in runner
      and 'here = Path(__file__).resolve().parent' in runner
      and 'code_root = here.parent' in runner
      and 'environment["PYTHONPATH"] = str(code_root)' in runner
      and 'Path("validate_observable_solver.py") if worker is None else Path(worker)' in runner)


def anchors(data):
    result = set()
    for line in data.decode().splitlines():
        match = re.match(r'^#{1,6} +(.*?)(?: +#+)?$', line)
        if match:
            title = re.sub(r'<[^>]+>', '', match.group(1)).lower()
            result.add(re.sub(r'[^\w\- ]', '', title).replace(' ', '-'))
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', data.decode()))
    return result


link_records = []
outside_scope_count = 0
for name in ['code/README.md', 'docs/README.md']:
    for match in re.finditer(r'\]\(([^)\s]+)\)', live_files[name].decode()):
        target = unquote(match.group(1))
        if '://' in target or target.startswith('mailto:'):
            continue
        path, _, fragment = target.partition('#')
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
        if resolved not in live_files:
            outside_scope_count += 1
            continue
        link_records.append({'guide': name, 'target': target, 'resolved_path': resolved,
                             'fragment': fragment or None,
                             'status': 'PASS' if not fragment or fragment in anchors(live_files[resolved]) else 'FAIL'})
check('guide file and fragment references within the edition resolve',
      bool(link_records) and all(row['status'] == 'PASS' for row in link_records),
      links=link_records, unrelated_links_outside_assigned_destination_scope=outside_scope_count)
check('H4 guide and chapter cross-references identify the installed addition',
      'C.4.7.10 part D extends' in guide_section
      and '**C-H4 established scope.** C.4.7.10 part D extends' in live_files['docs/README.md'].decode()
      and b'`code/validation/observable_horizon_plan.json`' in insertion
      and b'`code/README.md`' in insertion)

read(Path(__file__).resolve(), 'checker source identity')
cpu = time.process_time() - started_cpu
record = {
    'format': 'H4-promoted-correspondence-v1',
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS' if all(c['status'] == 'PASS' for c in checks) else 'FAIL',
    'identity': '/root/h4_promoted_correspondence',
    'scope': 'Independent installation correspondence and static integration; not a new scientific review',
    'authorization': 'Supervisor states user approved exact H4 v3 final proposal; installation complete message received before live checks',
    'checks': checks,
    'sources': sources,
    'resources': {'cpu_limit_seconds': 60, 'address_space_limit_bytes': 4 * 1024**3,
                  'checker_cpu_seconds': cpu, 'peak_rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024},
    'limits': [
        'No tests, imports of candidate code, numerical experiments, training, Git commands or established-file edits.',
        'Full bytes hashed for all 31 frozen/live pairs; scientific bodies were not rereviewed.',
        'No prior reviewer report was opened; verdict labels embedded in permitted mapping were visible but unused.',
        'Review manifest was accessed for identity metadata only; its named non-edition sources were not opened.',
        'Static CLI and path checks do not establish runtime behavior or independently reproduce reported empirical results.',
        'Guide links outside the 31 assigned edition destinations were not checked.',
        'Pre-install state was not independently captured: original chapter and dependency identity use the approved frozen hashes.',
        'No commit correspondence is claimed; the supervisor owns Git integration.',
    ],
}
record_path = Path(str(PREFIX) + '_checks.json')
record_path.write_text(json.dumps(record, indent=2) + '\n')
lines = [
    '# H4 v3 promoted installation correspondence', '',
    f"**{record['status']} — independent static installation check.** Checked {record['checked_utc']}.", '',
    'All 11 approved installations and 20 inherited dependencies match the frozen edition byte for byte and match every declared SHA-256. No tests or training were run.', '',
    '## Checks', '',
]
lines += [f"- **{item['status']}**: {item['name']}." for item in checks]
lines += ['',
    f'The D insertion occupies zero-based bytes [{start}, {end}), starts at line {chapter[:start].count(bytes([10])) + 1}, and contains {len(source_section):,} source bytes plus one LF. Its source SHA-256 is `{digest(source_section)}`; the inserted-byte SHA-256 is `{digest(insertion)}`. Removing these exact bytes restores `{digest(restored)}`, the approved original chapter SHA-256. C.4.8 begins immediately afterward at line {chapter[:end].count(bytes([10])) + 1}.', '',
    f'The guide check resolved {len(link_records)} file/fragment links within the permitted edition, confirmed the 14-configuration plan and CLI argument names, and checked all four new/changed runtime files for study imports and path dependence. These checks parsed text only.', '',
    '## Exact input identities', '',
    f'- Final mapping: `{digest(mapping_raw)}`.',
    f'- Review manifest, identity only: `{digest(review_raw)}`.',
    f'- Edition manifest: `{digest(edition_raw)}`.', '',
    '## All final destination hashes', '',
    '| Destination | Role | SHA-256, frozen = live = expected |',
    '|---|---|---|',
]
lines += [f"| `{row['destination']}` | {row['role']} | `{row['live_sha256']}` |" for row in file_records]
lines += ['', '## Coverage, method and limits', '',
    f'Checker: `python -B studies/observable_hierarchy/H4_promoted_correspondence_v1_check.py`, working directory `/home/amir/Codes/PDE`. CPU use {cpu:.6f} seconds; peak RSS {record["resources"]["peak_rss_bytes"]:,} bytes; enforced limits 60 CPU seconds and 4 GiB address space.', '',
    'Only shared instructions, the permitted mapping/manifests, frozen edition files and corresponding live destinations were used. All file-byte identities and detailed static evidence are in `H4_promoted_correspondence_v1_checks.json`; the reusable checker is `H4_promoted_correspondence_v1_check.py`.', '',
]
lines += [f'- {limit}' for limit in record['limits']]
lines += ['', 'The supervisor should retain this report with the exact installation mapping and final commit record. This report does not replace the earlier promotion review or reproduction gates.', '']
Path(str(PREFIX) + '.md').write_text('\n'.join(lines))
print(json.dumps({'status': record['status'], 'checks': [{'name': c['name'], 'status': c['status']} for c in checks],
                  'report': str(PREFIX) + '.md', 'record': str(record_path), 'resources': record['resources']}, indent=2))
