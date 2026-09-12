"""Metadata/correspondence assessment only; no analytic certification or Git."""
from pathlib import Path
from hashlib import sha256
from difflib import unified_diff, SequenceMatcher
from datetime import datetime, timezone
import json
import platform
import re

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/nonlinear_selection_generalization'
DATA = ROOT / 'data/generated/nonlinear_selection_generalization'
OUT = Path(__file__).resolve().parent
checked = {}

def digest(data):
    return sha256(data).hexdigest()

def verify(path, expected, label=None):
    data = path.read_bytes()
    assert digest(data) == expected, str(path)
    checked[label or str(path.relative_to(ROOT))] = {'sha256':expected, 'bytes':len(data), 'lines':len(data.splitlines())}
    return data

versions = {}
for version in (1, 2):
    manifest_path = STUDY / f'scientific_manifest_v{version}.json'
    manifest = json.loads(manifest_path.read_text())
    im = json.loads((STUDY / f'integration_manifest_v{version}.json').read_text())
    verify(manifest_path, im['scientific_manifest_sha256'])
    verify(STUDY / f'integration_assignment_v{version}.md', im['integration_assignment_sha256'])
    for name, expected in manifest['files'].items():
        data = verify(STUDY/name, expected['sha256'])
        assert len(data) == expected['bytes'] and len(data.splitlines()) == expected['lines']
    for name, expected in manifest['assembly_unit_hashes'].items():
        verify(STUDY/name, expected)
    units = [STUDY/name for name in manifest['assembly_unit_hashes']]
    rebuilt = ('\n\n'.join(p.read_text().rstrip() for p in units)+'\n').encode()
    assert rebuilt == (STUDY/f'candidate_addition_v{version}.md').read_bytes()
    for name, meta in manifest['source_slices'].items():
        source = verify(ROOT/meta['source'], meta['full_source_sha256'])
        lines = source.decode().splitlines(keepends=True)
        chunks = [f"# Frozen established dependencies from {meta['source']}\n\n"
                  f"Source SHA-256: `{digest(source)}`.\n"
                  'Only the exact complete sections listed below are included.\n']
        for first, last, scope in meta['ranges']:
            chunks += [f"\n<!-- SOURCE {meta['source']}:{first}-{last}; {scope} -->\n\n", ''.join(lines[first-1:last])]
        assert ''.join(chunks).encode() == (STUDY/name).read_bytes()
    edition = Path(im['edition'])
    assert sorted(str(p.relative_to(edition)) for p in edition.rglob('*') if p.is_file()) == sorted(im['edition_files'])
    for name, expected in im['edition_files'].items():
        verify(edition/name, expected)
    old = (ROOT/'docs/global_nonlinear.md').read_bytes()
    addition = (STUDY/f'candidate_addition_v{version}.md').read_bytes()
    assert (edition/'docs/global_nonlinear.md').read_bytes() == old+b'\n'+addition
    assert (edition/'docs/README.md').read_bytes() == (STUDY/f'candidate_docs_README_v{version}.md').read_bytes()
    versions[str(version)] = {'files':len(manifest['files']), 'assembly_units':len(units), 'source_slices':len(manifest['source_slices']), 'edition_files':len(im['edition_files'])}

expected_reports = {
 'scientific_review_v1_a.md':'bf9101c05ee509de7faf2851db55f738e21eeef6a34861207a73154ed2043b90',
 'scientific_review_v1_b.md':'35c16b392928ced4b07d15ffb02163fb9cb381c284189fc536d33cec3e7a40b5',
 'integration_review_v1.md':'784cdb2d937293f76047ef01481178726b2c616ffe486e518d4c81710194ae25',
 'scientific_review_v2_c.md':'8480318dc6bc5d98e7cbc35abd15d0884bd88b3310736cbc244ff4319d884507',
 'scientific_review_v2_d.md':'b26902b104bec3dd5dba1259a3071f24c9eae3142a19ba1119fd3f900040a92e',
 'integration_review_v2.md':'21ed7e7cdfb4a3ea3a07a2ddfd6dfde101daf269077a521adf2d75f7979ce715',
 'scientific_manifest_v2.json':'cb8b6827db6b24ba2c7c6bf00320cce82c66e687ae4ffe268b02a01bef3336c7',
 'integration_manifest_v2.json':'b5fcdf928d4bcc964f626a176bd129c84662c9a66a900501b1143c7b2fb25b9a',
}
for name, expected in expected_reports.items():
    verify(STUDY/name, expected)

for current, frozen in [('AGENTS.md','frozen_AGENTS_v2.md'), ('RESEARCH_WORKFLOW.md','frozen_WORKFLOW_v2.md'), ('docs/NOTATION.md','frozen_NOTATION_v2.md'), ('docs/README.md','frozen_docs_README_v2.md')]:
    verify(ROOT/current, digest((STUDY/frozen).read_bytes()))

# Verify every hash in the complete relevance input table without reading its
# earlier research bodies as new scientific arguments.
relevance = (STUDY/'relevance_report.md').read_text()
for line in relevance.splitlines():
    match = re.match(r'\| ([^|]+?) \| `([a-f0-9]{64})` \|$',line)
    if not match:
        continue
    name, expected = match.groups()
    path = Path('/etc/codex/skills')/name if name.startswith(('investigate-conjectures/','solve-math-rigorously/')) else ROOT/name if '/' in name or name in ['AGENTS.md','RESEARCH_WORKFLOW.md'] else STUDY/name
    verify(path, expected, name)

expected_scratch = {
 'scientific_review_v2_c/checks.py':'c56148b31008a34731b4db50a5f8ca7cac2f4a22d85b325ccf16f63407eddf16',
 'scientific_review_v2_c/checks.json':'7e8762e38201733f4652cb9e22b6b4112fa2dfc1f954119749f11c3d3a8d1836',
 'scientific_review_v2_d/checks.py':'ec10b114631398383441ec23b1b0fa61e224cc8575c5ccfe982df054fa02f13b',
 'scientific_review_v2_d/checks.json':'e59ee919ea3e7c5a3ab3f6a08f8da0d042abb88ab6a71a94f949cb5644c2ee62',
 'scientific_review_v2_d/reference_certificate.py':'112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e',
 'integration_review_v2/check_integration.py':'833e9a7f33098ca49522292a215fac5f5a82674bb5e61bd0c724fca0e6f5911a',
 'scientific_review_v1_a/input_hashes_start.json':'d8ce617c440b6471bc0ebb2f746c1629bb361e9bb48fe138548fc5e77c51a2c1',
 'scientific_review_v1_a/reference_certificate.py':'112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e',
 'scientific_review_v1_a/certificate_result.json':'df53a3071a35b1bb2db548f2d7faf58918ce539c93f0920f81fbc285cb8041cd',
 'scientific_review_v1_a/algebra_checks.py':'fb83d0ae150fead4afb631787b2520d395bba9cdac90d1f1da727099e0bdbc75',
 'scientific_review_v1_a/algebra_result_corrected.json':'2888d99b1ec9bbb911a5250375856ee8c3f26fac07888dfdbcf613a8cfcf35dc',
}
for name, expected in expected_scratch.items():
    verify(DATA/name, expected)
for reviewer in ['scientific_review_v2_c','scientific_review_v2_d']:
    meta=json.loads((DATA/reviewer/'completion.json').read_text())
    verify(STUDY/(reviewer+'.md'),meta['report_sha256'])
    for name, expected in meta.get('input_hashes',meta.get('input_sha256')).items():
        verify(STUDY/name,expected)
meta=json.loads((DATA/'integration_review_v2/completion_checks.json').read_text())
verify(Path(meta['report_path']),meta['report_sha256'])
for name,expected in meta['evidence'].items():
    verify(DATA/'integration_review_v2'/name,expected)

# The correction is exactly one six-line insertion, including zero coefficients
# beyond N; the rest of the candidate and all other scientific units are equal.
before=(STUDY/'candidate_addition_v1.md').read_text()
after=(STUDY/'candidate_addition_v2.md').read_text()
ops=[o for o in SequenceMatcher(None,before.splitlines(),after.splitlines()).get_opcodes() if o[0]!='equal']
assert len(ops)==1 and ops[0][0]=='insert' and ops[0][4]-ops[0][3]==6, ops
inserted='\n'.join(after.splitlines()[ops[0][3]:ops[0][4]])+'\n'
assert 'k=0}^N' in inserted and 'All coefficients above \\(N\\) are zero.' in inserted
for part in ['model','continuation','separation']:
    assert (STUDY/f'canonical_{part}_v1.md').read_bytes()==(STUDY/f'canonical_{part}_v2.md').read_bytes()
assert (STUDY/'candidate_docs_README_v1.md').read_bytes()==(STUDY/'candidate_docs_README_v2.md').read_bytes()
(OUT/'correction_v1_to_v2.diff').write_text(''.join(unified_diff(before.splitlines(keepends=True),after.splitlines(keepends=True),fromfile='candidate_addition_v1.md',tofile='candidate_addition_v2.md')))
old_guide=(ROOT/'docs/README.md').read_text()
new_guide=(STUDY/'candidate_docs_README_v2.md').read_text()
(OUT/'proposed_guide.diff').write_text(''.join(unified_diff(old_guide.splitlines(keepends=True),new_guide.splitlines(keepends=True),fromfile='docs/README.md',tofile='candidate_docs_README_v2.md')))
(OUT/'proposed_chapter.diff').write_text(''.join(unified_diff((ROOT/'docs/global_nonlinear.md').read_text().splitlines(keepends=True), ((ROOT/'docs/global_nonlinear.md').read_text()+'\n'+after).splitlines(keepends=True),fromfile='docs/global_nonlinear.md',tofile='proposed/docs/global_nonlinear.md')))
report={'result':'PASS: every asserted hash and byte correspondence checked', 'completed_utc':datetime.now(timezone.utc).isoformat(), 'python':platform.python_version(), 'platform':platform.platform(), 'versions':versions, 'checked_files':checked, 'correction_zero_based_opcodes':ops, 'correction_inserted_text':inserted, 'limits':'Hash/byte audit, not a fresh scientific review or independent observation of reviewer launch/read behavior. No Git or established changes.'}
(OUT/'hashes_and_correspondence.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checked_files'},indent=2))
print('Verified identities:',len(checked))
