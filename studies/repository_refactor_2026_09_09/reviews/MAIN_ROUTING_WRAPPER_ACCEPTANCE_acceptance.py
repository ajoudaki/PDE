"""Independent, inert, stdlib-only checks of the four explicitly scoped files."""
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
sys.path.insert(0, '/tmp/resnet-patch-acceptance.7tppNkr4')
from runtime import BASE, REPO, LONG, WRAPPER, MANIFEST, LINKS, TEST, install_audit

install_audit()
EXPECTED = {
    str(WRAPPER): 'b35270ea1e4bd01ab0e113b3ec6453f21af0f6d66933fb89c04b4adbc731a40e',
    str(TEST): 'eba91749ddc218299fb562ca5c78dcba1ce7702f4c4884c1777186fb24d0a2ce',
    str(MANIFEST): 'e59f6e8b1c10a4be98efa40fa286004ce40fe7cdf6ed5200d0cea36f362c6f41',
    str(LINKS): '8e67059e7083fcb5d230de92f1daa4387dba4da1c081e3f111180cef1e2cd02e',
}


def hashes():
    return {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in EXPECTED}


def inventory(root):
    rows = {}
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in dirs + files:
            p = Path(directory) / name
            info = p.lstat()
            row = {'mode': info.st_mode, 'inode': info.st_ino, 'nlink': info.st_nlink,
                   'size': info.st_size, 'mtime_ns': info.st_mtime_ns}
            if stat.S_ISLNK(info.st_mode):
                row['target'] = os.readlink(p)
            elif stat.S_ISREG(info.st_mode):
                row['sha256'] = hashlib.sha256(p.read_bytes()).hexdigest()
            rows[str(p.relative_to(root))] = row
    return rows


before = hashes()
assert before == EXPECTED, 'pinned inputs changed before execution'
assert stat.S_IMODE(BASE.stat().st_mode) == 0o700
(BASE / 'bin/python').chmod(0o700)
fixtures = BASE / 'fixtures'
fixtures.mkdir()
(BASE / 'logs').mkdir()
(BASE / 'launch elsewhere').mkdir()
occupied = fixtures / 'occupied ordinary output'
(occupied / 'nested').mkdir(parents=True)
(occupied / 'nested/result.txt').write_bytes(b'ordinary existing output\n')
(occupied / '.ordinary-hidden').write_bytes(b'ordinary hidden output\n')

retained = fixtures / 'retained-neighbor'
retained.mkdir()
(retained / 'input.txt').write_bytes(b'inert retained neighbor bytes\x00\n')
neighbor = fixtures / 'shorter-neighbor'
neighbor.symlink_to(retained, target_is_directory=True)
dangling = fixtures / 'dangling-root'
dangling.symlink_to(fixtures / 'missing-link-target', target_is_directory=True)
ancestor = fixtures / 'ancestor-link'
ancestor.symlink_to(occupied, target_is_directory=True)

links_bad = [
    ('symlink-root', neighbor),
    ('dangling-root', dangling),
    ('symlink-ancestor', ancestor / 'nonexistent/leaf'),
    ('symlink-dotdot-component', ancestor / '../escape-output'),
]
for name, target, is_dir in (
    ('child-file-link', retained / 'input.txt', False),
    ('child-directory-link', retained, True),
    ('child-dangling-link', fixtures / 'missing-child-target', False),
):
    root = fixtures / name
    root.mkdir()
    (root / 'alias').symlink_to(target, target_is_directory=is_dir)
    links_bad.append((name, root))
root = fixtures / 'nested-hidden-symlink'
(root / 'nested/.hidden').mkdir(parents=True)
(root / 'nested/.hidden/alias').symlink_to(retained, target_is_directory=True)
links_bad.append(('nested-hidden-symlink', root))

hard_source = fixtures / 'hardlink-original'
hard_source.write_bytes(b'private hardlink fixture\n')
hard_root = fixtures / 'hardlink-root'
os.link(hard_source, hard_root)
links_bad.append(('hardlink-root', hard_root))
for name, relative in (('child-hardlink', 'alias'), ('nested-hidden-hardlink', 'nested/.hidden/alias')):
    root = fixtures / name
    (root / Path(relative).parent).mkdir(parents=True)
    os.link(hard_source, root / relative)
    links_bad.append((name, root))

cases = []


def add(name, selection, accepted, expected=None):
    if accepted and expected is None:
        expected = str((LONG / Path(selection).expanduser()).resolve())
    cases.append({'name': name, 'selection': selection, 'accepted': accepted, 'expected': expected})


default = str(REPO / 'data/generated/resnet_dense_long_horizon')
add('default-unset', None, True, default)
add('default-empty', '', True, default)
add('fresh-absolute', str(fixtures / 'fresh-output'), True)
add('spaces-and-dotdot', str(fixtures / 'unused with spaces/../normalized output'), True)
add('relative', os.path.relpath(fixtures / 'relative output', LONG), True)
add('home-expansion', '~/' + os.path.relpath(fixtures / 'home output', Path.home()), True)
add('occupied-ordinary', str(occupied), True)
for name, suffix in (
    ('embedded-newline', 'embedded\nnewline'),
    ('one-trailing-newline', 'trailing\n'),
    ('two-trailing-newlines', 'trailing\n\n'),
    ('many-trailing-newlines', 'trailing' + '\n' * 12),
    ('newline-dot', 'literal-newline\n.'),
    ('newline-dot-newline', 'literal-newline\n.\n'),
    ('trailing-spaces', 'trailing spaces  '),
    ('tab-cr-newline', 'tab\tand\rcarriage\n'),
    ('newline-component', 'component\n/leaf\n\n'),
    ('unicode', 'résultat λ'),
    ('shell-metacharacters', 'literal-$()-`printf INERT`-*?[quote]"\'\\'),
    ('leading-dash-basename', '-output'),
):
    add(name, str(fixtures / suffix), True)
add('relative-trailing-newlines', os.path.relpath(fixtures / 'relative\n\n', LONG), True)
add('home-trailing-newlines', '~/' + os.path.relpath(fixtures / 'home\n\n', Path.home()), True)
add('newline-stripped-symlink-neighbor', str(neighbor) + '\n\n', True)
add('newline-stripped-hardlink-neighbor', str(hard_root) + '\n\n', True)

for name, path in links_bad:
    add(name, str(path), False)
for name, path in (
    ('protected-repository', REPO),
    ('protected-ancestor', REPO.parent),
    ('protected-filesystem-root', Path('/')),
    ('protected-studies', REPO / 'studies'),
    ('protected-long-study', LONG),
    ('protected-wrapper-file', WRAPPER),
    ('protected-docs', REPO / 'docs'),
    ('protected-code', REPO / 'code'),
    ('protected-git', REPO / '.git'),
    ('protected-data-parent', REPO / 'data'),
    ('protected-historical', REPO / 'data/historical'),
    ('protected-historical-long', REPO / 'data/historical/studies/resnet_dense_long_horizon'),
    ('protected-backups', REPO / 'data/original_backups'),
    ('protected-cache', REPO / 'data/runtime_cache'),
):
    add(name, str(path), False)
add('protected-relative-dot', '.', False)
add('protected-relative-docs', '../../docs', False)

snapshot_before = inventory(fixtures)
env_base = dict(os.environ)
for key in ('PDE_LONG_HORIZON_OUTPUT_ROOT', 'PYTHONPATH', 'PYTHONHOME', 'PYTHONSTARTUP',
            'BASH_ENV', 'ENV', 'PATCH_FORCED_STATUS', 'PATCH_FORCED_STDOUT', 'PATCH_EVENT_LOG'):
    env_base.pop(key, None)
env_base.update(PYTHONDONTWRITEBYTECODE='1', PATH=str(BASE / 'bin') + ':/usr/bin:/bin')
results = []


def invoke(name, command, cwd, extra):
    log = BASE / 'logs' / (name + '.jsonl')
    env = dict(env_base, PATCH_EVENT_LOG=str(log), **extra)
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, timeout=20)
    events = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
    row = {'name': name, 'command': command, 'cwd': str(cwd), 'returncode': result.returncode,
           'stdout_hex': result.stdout.hex(), 'stderr': result.stderr.decode(errors='backslashreplace'),
           'events': events, 'checks': []}
    results.append(row)
    return row, result, events


def check(row, condition, message):
    row['checks'].append({'pass': bool(condition), 'claim': message})


for case in cases:
    name, selection, accepted, expected = (case[k] for k in ('name', 'selection', 'accepted', 'expected'))
    raw = str(LONG / '../../data/generated/resnet_dense_long_horizon') if selection in (None, '') else selection
    row, result, events = invoke('direct-' + name,
        [sys.executable, '-I', '-B', str(BASE / 'direct.py'), 'validate', raw], LONG, {})
    check(row, type(result.returncode) is int and result.returncode == (0 if accepted else 1), 'direct real validator scalar exit status')
    check(row, sum(e['kind'] == 'validate_call' for e in events) == 1, 'direct real validator entered exactly once')
    if accepted and result.returncode == 0:
        check(row, json.loads(result.stdout)['normalized'] == expected, 'direct real validator normalized root')
    elif not accepted:
        check(row, b'ValueError:' in result.stderr, 'real guard rejected selection with ValueError')

    extra = {} if selection is None else {'PDE_LONG_HORIZON_OUTPUT_ROOT': selection}
    row, result, events = invoke('wrapper-' + name,
        ['/usr/bin/bash', '--noprofile', '--norc', str(WRAPPER)], BASE / 'launch elsewhere', extra)
    kinds = [e['kind'] for e in events]
    validation = [e for e in events if e['kind'] == 'validation_command']
    calls = [e for e in events if e['kind'] == 'dispatch_recorded']
    check(row, type(result.returncode) is int and result.returncode == (0 if accepted else 1), 'wrapper scalar exit status')
    check(row, len(validation) == 1 and validation[0]['argv'][-1] == raw, 'one preflight query receives exact unstripped selection')
    check(row, kinds.count('validate_call') == 1, 'wrapper enters real validator exactly once')
    check(row, kinds.count('validation_exit') == 1, 'real validator process completes once')
    check(row, 'unexpected_command' not in kinds, 'all commands matched inert recorder allowlist')
    if accepted:
        expected_calls = [
            ['-m', 'unittest', 'discover', '-s', 'tests', '-v'],
            ['run_all.py', '--config', 'config/protocol.json', '--output-root', expected],
            ['make_manifest.py', '--output-root', expected],
        ]
        check(row, [e['argv'] for e in calls] == expected_calls, 'three inert dispatches in exact order, normalized root losslessly forwarded')
        check(row, kinds == ['validation_command', 'validate_call', 'link_guard_call', 'validation_exit'] + ['dispatch_recorded'] * 3,
              'all guard work completed before any dispatch')
        for call in calls[1:]:
            check(row, call['argv_hex'][-1] == os.fsencode(expected).hex(), 'output-root bytes preserved')
        check(row, all(e.get('cwd') == str(LONG) for e in validation + calls), 'wrapper resolves and dispatches from study directory')
    else:
        check(row, not calls, 'validator failure prevents every test/science/manifest dispatch')

# Exercise the actual imported low-level guard independently of the manifest guard.
for name, path in [('ordinary-occupied', occupied), *links_bad]:
    row, result, events = invoke('links-only-' + name,
        [sys.executable, '-I', '-B', str(BASE / 'direct.py'), 'links', str(path)], LONG, {})
    check(row, result.returncode == (0 if name == 'ordinary-occupied' else 1), 'direct unchanged link guard accept/refuse contract')
    check(row, [e['kind'] for e in events] == ['link_guard_call'], 'only actual low-level guard entered')

# Test scalar shell status, including partial validator stdout before failure.
for status, partial in ((1, ''), (2, ''), (17, ''), (42, str(neighbor) + '\n\n\n'), (127, 'partial\n.\n')):
    row, result, events = invoke('forced-status-' + str(status),
        ['/usr/bin/bash', '--noprofile', '--norc', str(WRAPPER)], BASE / 'launch elsewhere',
        {'PDE_LONG_HORIZON_OUTPUT_ROOT': str(fixtures / 'forced-valid-output'),
         'PATCH_FORCED_STATUS': str(status), 'PATCH_FORCED_STDOUT': partial})
    check(row, type(result.returncode) is int and result.returncode == status, 'exact scalar validator status propagated by Bash assignment')
    check(row, [e['kind'] for e in events] == ['validation_command', 'validation_injected_exit'],
          'failure including partial stdout causes zero dispatches')

snapshot_after = inventory(fixtures)
after = hashes()
checks = [c for r in results for c in r['checks']]
failures = [{'name': r['name'], 'claim': c['claim']} for r in results for c in r['checks'] if not c['pass']]
if snapshot_before != snapshot_after:
    failures.append({'name': 'fixture-preservation', 'claim': 'private fixture inventory changed'})
if before != after:
    failures.append({'name': 'source-preservation', 'claim': 'scoped source hashes changed'})
evidence = {'verdict': 'NOT CLEAN' if failures else 'CLEAN', 'private_directory': str(BASE),
            'before_hashes': before, 'after_hashes': after, 'cases': cases, 'invocations': results,
            'invocation_count': len(results), 'assertion_count': len(checks) + 2, 'failures': failures,
            'fixtures_before': snapshot_before, 'fixtures_after': snapshot_after,
            'fixtures_unchanged': snapshot_before == snapshot_after, 'sources_unchanged': before == after}
(BASE / 'evidence.json').write_text(json.dumps(evidence, indent=2, ensure_ascii=True) + '\n')
(BASE / 'after.sha256').write_text(''.join(f'{digest}  {path}\n' for path, digest in after.items()))
print(json.dumps({k: evidence[k] for k in ('verdict', 'invocation_count', 'assertion_count', 'failures', 'fixtures_unchanged', 'sources_unchanged')}, indent=2))
raise SystemExit(bool(failures))
