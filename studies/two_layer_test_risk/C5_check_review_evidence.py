"""Audit retained v1 review identity and current dependency correspondence.

This is an evidence audit, not a scientific review or a numerical integration.
It reads only this study, its generated inputs, and maintained docs/code.
The output directory must be fresh and in the assigned evidence namespace.
"""
import argparse
import difflib
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import re
import sys


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(blob):
    return hashlib.sha256(blob).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    root = study.parents[1]
    generated = root / 'data/generated/two_layer_test_risk'
    allowed = generated / 'c5_evidence_check_20260912'
    output = args.output.resolve()
    if not output.is_relative_to(allowed):
        raise ValueError('Output outside assigned scratch namespace')
    output.mkdir(parents=True, exist_ok=False)
    frozen = generated / 'signed_promotion_v1'
    failures = []
    checks = []

    def check(label, actual, expected):
        good = actual == expected
        checks.append(dict(label=label, actual=actual, expected=expected, matches=good))
        if not good:
            failures.append(label)

    check('frozen manifest', sha(frozen / 'manifest.json'),
          'bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3')
    manifest = read(frozen / 'manifest.json')
    counts = {}
    for group in ('packet', 'edition', 'evidence'):
        table = manifest[group + '_sha256']
        paths = {str(p.relative_to(frozen / group)) for p in (frozen / group).rglob('*') if p.is_file()}
        check(group + ' exact file inventory', sorted(paths), sorted(table))
        for name, wanted in table.items():
            path = frozen / group / name
            check(group + '/' + name, sha(path) if path.is_file() else None, wanted)
        counts[group] = len(table)
    for name, wanted in manifest['source_sha256'].items():
        check('study source/' + name, sha(study / name), wanted)
    check('study assembler', sha(study / 'assemble_signed_promotion.py'), manifest['assembler_sha256'])

    expected_reports = {
        'SIGNED_PROMOTION_REVIEW_A_V1.md': 'c7ba5ec25282590789f43ca6b7751fa602c95ab2cbbedea3bd6f0578a3395ec5',
        'SIGNED_PROMOTION_REVIEW_B_V1.md': '326b84743805a2b37cdef861588c3b8179138b2858a2e220d4c5230bb4e82962',
        'SIGNED_PROMOTION_INTEGRATION_V1.md': '9005a15bba85f0dbee96222ef3ae8651cbe3197a6334ffe0e5a06a6bcb901af2',
    }
    for name, wanted in expected_reports.items():
        check('report/' + name, sha(study / name), wanted)
    for subdir, name in [('reviewer_a', 'SIGNED_PROMOTION_REVIEW_A_V1.md'),
                         ('reviewer_b', 'SIGNED_PROMOTION_REVIEW_B_V1.md')]:
        check(subdir + ' report hash record', (frozen / subdir / 'report.sha256').read_text().split()[0],
              sha(study / name))
    for subdir in ('reviewer_b', 'integration'):
        for name, wanted in read(frozen / subdir / 'artifact_hashes.json').items():
            check(subdir + ' output/' + name, sha(frozen / subdir / name), wanted)
    a_text = (study / 'SIGNED_PROMOTION_REVIEW_A_V1.md').read_text()
    a_outputs = re.findall(r'- `([^`]+)`: `([a-f0-9]{64})`\.', a_text.split('### Output artifact hashes')[1])
    check('reviewer A output count', len(a_outputs), 6)
    for name, wanted in a_outputs:
        check('reviewer_a output/' + name, sha(frozen / 'reviewer_a' / name), wanted)
    embedded = {}
    for name, source in re.findall(r'### ([\w.-]+\.py)\n.*?```python\n(.*?)```', a_text, re.S):
        path = frozen / 'reviewer_a' / name
        check('reviewer_a embedded source/' + name, digest(source.encode()), sha(path))
        embedded['reviewer_a/' + name] = sha(path)
    b_text = (study / 'SIGNED_PROMOTION_REVIEW_B_V1.md').read_text()
    b_source = re.findall(r'```python\n(.*?)```', b_text, re.S)
    check('reviewer B source block count', len(b_source), 1)
    b_path = frozen / 'reviewer_b/review_b_checks.py'
    check('reviewer B embedded source', digest(b_source[0].encode()), sha(b_path))
    embedded['reviewer_b/review_b_checks.py'] = sha(b_path)
    check('integration unique checker', sha(study / 'check_signed_integration.py'),
          '4573f1e9f262f8a0caddfb6dfb617271ee2a073144f3b60ac95ea355a7d848cf')

    run_records = []
    for run in ('certificate_20260910_01', 'certificate_reproduction_20260910_01'):
        folder = frozen / 'evidence' / run
        meta = read(folder / 'metadata.json')
        result = read(folder / 'result.json')
        check(run + ' completed', meta['status'], 'completed')
        check(run + ' exit', meta['exit_status'], 0)
        check(run + ' result hash', sha(folder / 'result.json'), meta['result_sha256'])
        check(run + ' original retained result', sha(generated / run / 'result.json'), sha(folder / 'result.json'))
        historical_sources = {}
        for name, wanted in meta['source_sha256'].items():
            actual = sha(study / name) if (study / name).is_file() else None
            historical_sources[name] = dict(recorded=wanted, current=actual, matches=(actual == wanted))
            if name in ('certificate_driver.py', 'certificate_kernel.cpp', 'angle_error_bound.py'):
                check(run + ' numerical source/' + name, actual, wanted)
        chi, beta = result['chi'], result['beta_intersection']
        check(run + ' strict chi bounds', Fraction(27, 100000) < Fraction(chi['lo']) <=
              Fraction(chi['hi']) < Fraction(273, 1000000), True)
        check(run + ' strict beta bounds', Fraction(35309, 1000000) < Fraction(beta['lo']) <=
              Fraction(beta['hi']) < Fraction(35311, 1000000), True)
        run_records.append(dict(run=run, command=meta['command'], cpu_seconds_recorded=meta['cpu_seconds'],
                                historical_source_correspondence=historical_sources, chi=chi, beta=beta))

    # Recover the old base solely from the complete frozen edition and suffix.
    candidate = (frozen / 'packet/candidate.md').read_bytes()
    edition = (frozen / 'edition/docs/global_nonlinear.md').read_bytes()
    suffix = b'\n' + candidate.rstrip() + b'\n'
    check('edition candidate suffix', edition.endswith(suffix), True)
    old = edition[:-len(suffix)]
    check('recovered frozen old base', digest(old), manifest['copied_base_sha256']['docs/global_nonlinear.md'])
    old_lines = old.decode().splitlines(keepends=True)
    current = (root / 'docs/global_nonlinear.md').read_bytes()
    current_text = current.decode()
    marker = '\n### C.4. Training-law stability for two hidden tanh layers'
    check('one established C.4 heading', current_text.count(marker), 1)
    current_prefix = current_text.split(marker, 1)[0].rstrip() + '\n'
    prefix_diff = ''.join(difflib.unified_diff(old.decode().splitlines(True), current_prefix.splitlines(True),
                                            fromfile='frozen_original_global_prefix',
                                            tofile='current_global_prefix', n=3))
    (output / 'older_prefix_changes.diff').write_text(prefix_diff)

    units = []
    # The C preamble has an updated placement summary. The complete proof text
    # begins again at old line 2453 and remains an exact contiguous byte block.
    for title, first, last in [('Sections 2--3', 181, 500), ('A.1--A.4', 1835, 1893),
                               ('C proof units and weighted correction', 2453, 3829)]:
        text = ''.join(old_lines[first-1:last])
        occurrences = current_text.count(text)
        check('operative unit identity/' + title, occurrences, 1)
        first_now = current_text[:current_text.index(text)].count('\n') + 1 if occurrences == 1 else None
        units.append(dict(title=title, frozen_lines=[first,last], current_lines=[first_now, first_now+last-first]
                          if first_now else None, sha256=digest(text.encode()), exact_contiguous_occurrences=occurrences))
    dep = ['# Complete operative dependencies\n\n',
           'Unchanged full proof units of global_nonlinear.md. Legacy III.F\n'
           'denotes the contained Section 3 conditioning/response proof.\n'
           'C.4 retains its own activation and normalization hypotheses.\n\n']
    for first, last in ((181,500),(1835,1893),(2449,3829)):
        dep += [f'\n<!-- Original lines {first}--{last}. -->\n\n', ''.join(old_lines[first-1:last])]
    check('complete original dependency extraction', digest(''.join(dep).encode()),
          sha(frozen / 'packet/dependencies.md'))
    current_bases = {}
    for name, wanted in manifest['copied_base_sha256'].items():
        actual = sha(root / name)
        current_bases[name] = dict(frozen=wanted, current=actual, unchanged=(actual == wanted))
    named_reviewers = ['signed_promotion_a', 'signed_promotion_b', 'signed_integration']
    check('declared reviewer identifiers distinct', len(set(named_reviewers)), 3)
    check('declared reviewers distinct from manifest authors and selector',
          set(named_reviewers).isdisjoint(set(manifest['authors_assemblers']) | {manifest['selector']}), True)
    payload = dict(status='PASS' if not failures else 'FAIL', failures=failures, frozen_counts=counts,
                   manifest_sha256=sha(frozen/'manifest.json'), checks=checks,
                   reports_sha256={name:sha(study/name) for name in expected_reports},
                   embedded_checker_sha256=embedded, operative_dependency_units=units,
                   changed_current_base_files=[n for n,v in current_bases.items() if not v['unchanged']],
                   current_bases=current_bases, original_runs=run_records,
                   authors_assemblers=manifest['authors_assemblers'], selector=manifest['selector'],
                   declared_reviewers=named_reviewers,
                   isolation_limit='Original assignments and signed self-reports retained; no launcher/context transcript authenticated.',
                   command=sys.argv, environment=dict(python=sys.version, platform=platform.platform()),
                   checker_sha256=sha(Path(__file__)),
                   process_guides_sha256={n:sha(root/n) for n in ['AGENTS.md','RESEARCH_WORKFLOW.md']},
                   scope='Identity and evidence only. No scientific review, no new edition acceptance, no numerical integration.')
    (output/'result.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:v for k,v in payload.items() if k not in ('checks','original_runs','current_bases')},indent=2))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
