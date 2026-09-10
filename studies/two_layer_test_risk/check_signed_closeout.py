"""Coordinator integrity check; no numerical integration or training.

Run from this study's checkout with --output a fresh generated directory.
This checks frozen correspondence and retained review evidence, not proof
correctness. Complete proof/report reading is recorded separately.
"""
import argparse
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    study = Path(__file__).resolve().parent
    root = study.parents[1]
    runs = root / 'data/generated/two_layer_test_risk'
    out = args.output.resolve()
    assert out.is_relative_to(runs)
    out.mkdir(parents=True, exist_ok=False)
    frozen = runs / 'signed_promotion_v1'
    assert sha(frozen / 'manifest.json') == 'bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3'
    manifest = json.loads((frozen / 'manifest.json').read_text())
    counts = {}
    for group in ('packet', 'edition', 'evidence'):
        actual = {str(p.relative_to(frozen / group)): sha(p)
                  for p in (frozen / group).rglob('*') if p.is_file()}
        assert actual == manifest[group + '_sha256'], group
        counts[group] = len(actual)
    for path, digest in manifest['source_sha256'].items():
        assert sha(study / path) == digest, path
    for path, digest in manifest['copied_base_sha256'].items():
        assert sha(root / path) == digest, path
    assert sha(study / 'assemble_signed_promotion.py') == manifest['assembler_sha256']
    chapter = (root / 'docs/global_nonlinear.md').read_bytes()
    addition = (study / 'PROMOTION_SIGN_C4_V2.md').read_bytes()
    assert (frozen / 'edition/docs/global_nonlinear.md').read_bytes() == chapter + b'\n' + addition
    result_a = runs / 'certificate_20260910_01/result.json'
    result_b = runs / 'certificate_reproduction_20260910_01/result.json'
    assert sha(result_a) == sha(result_b) == '89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d'
    result = json.loads(result_a.read_text())
    chi = result['chi']
    assert Fraction(27, 100000) < Fraction(chi['lo']) <= Fraction(chi['hi']) < Fraction(273, 1000000)
    beta = result['beta_intersection']
    assert Fraction(35309, 1000000) < Fraction(beta['lo']) <= Fraction(beta['hi']) < Fraction(35311, 1000000)
    reports = ['SIGN_REVIEW_A_V1.md', 'SIGN_REVIEW_B_V1.md',
               'SIGNED_PROMOTION_REVIEW_A_V1.md', 'SIGNED_PROMOTION_REVIEW_B_V1.md',
               'SIGNED_PROMOTION_INTEGRATION_V1.md']
    report_hashes = {name: sha(study / name) for name in reports}
    assert report_hashes['SIGNED_PROMOTION_REVIEW_A_V1.md'] == 'c7ba5ec25282590789f43ca6b7751fa602c95ab2cbbedea3bd6f0578a3395ec5'
    assert report_hashes['SIGNED_PROMOTION_REVIEW_B_V1.md'] == '326b84743805a2b37cdef861588c3b8179138b2858a2e220d4c5230bb4e82962'
    assert report_hashes['SIGNED_PROMOTION_INTEGRATION_V1.md'] == '9005a15bba85f0dbee96222ef3ae8651cbe3197a6334ffe0e5a06a6bcb901af2'
    artifact_hashes = json.loads((frozen / 'integration/artifact_hashes.json').read_text())
    for path, digest in artifact_hashes.items():
        assert sha(frozen / 'integration' / path) == digest, path
    b_artifacts = json.loads((frozen / 'reviewer_b/artifact_hashes.json').read_text())
    for path, digest in b_artifacts.items():
        assert sha(frozen / 'reviewer_b' / path) == digest, path
    a_report = (study / 'SIGNED_PROMOTION_REVIEW_A_V1.md').read_text()
    a_artifacts = re.findall(r'- `([^`]+)`: `([a-f0-9]{64})`\.',
                            a_report.split('### Output artifact hashes')[1])
    assert len(a_artifacts) == 6
    for path, digest in a_artifacts:
        assert sha(frozen / 'reviewer_a' / path) == digest, path
    # Preserve unique embedded reviewer source and verify against executed source.
    embedded = {}
    for report, subdir in [('SIGNED_PROMOTION_REVIEW_A_V1.md', 'reviewer_a'),
                           ('SIGNED_PROMOTION_REVIEW_B_V1.md', 'reviewer_b')]:
        body = (study / report).read_text()
        for name, source in re.findall(r'### ([\w.-]+\.py)\n.*?```python\n(.*?)```', body, re.S):
            path = frozen / subdir / name
            assert path.is_file(), (report, name)
            assert source.encode() == path.read_bytes(), (report, name)
            embedded[subdir + '/' + name] = sha(path)
    b_source = re.findall(r'```python\n(.*?)```',
                         (study / 'SIGNED_PROMOTION_REVIEW_B_V1.md').read_text(), re.S)
    assert len(b_source) == 1
    b_path = frozen / 'reviewer_b/review_b_checks.py'
    assert b_source[0].encode() == b_path.read_bytes()
    embedded['reviewer_b/review_b_checks.py'] = sha(b_path)
    assert len(embedded) == 4
    python_files = sorted(study.glob('*.py'))
    for path in python_files:
        ast.parse(path.read_text(), filename=str(path))
    links = []
    for name in ('README.md', 'SIGNED_PROMOTION_PROPOSAL.md'):
        for target in re.findall(r'\]\(([^)]+)\)', (study / name).read_text()):
            assert (study / target.partition('#')[0]).resolve().is_file(), (name, target)
            links.append([name, target])
    payload = dict(status='PASS', source_sha256=sha(Path(__file__)),
                   manifest_sha256=sha(frozen / 'manifest.json'),
                   frozen_payload_counts=counts, current_sources_match=True,
                   old_chapter_preserved=True, report_sha256=report_hashes,
                   embedded_reviewer_source_sha256=embedded,
                   python_sources_parsed=len(python_files), checked_record_links=links,
                   chi=chi, beta=beta,
                   scope='Integrity/structure only; no proof substitute or new coefficient run')
    (out / 'result.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps({k: v for k, v in payload.items() if k != 'checked_record_links'}, indent=2))


if __name__ == '__main__':
    main()
