"""Read-only provenance/correspondence audit; writes only its own fresh result."""
from pathlib import Path
import ast
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path('/home/amir/Codes/PDE')
STUDY = ROOT / 'studies/trained_prediction_sampling'
DATA = ROOT / 'data/generated/trained_prediction_sampling'
HERE = Path(__file__).resolve().parent
FRESH = HERE / 'standalone'
RESULT = HERE / 'record_audit.json'
assert not RESULT.exists()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

aliases = {
    'Frozen assembled global chapter': DATA/'standalone_v2/docs/global_nonlinear.md',
    'Frozen assembled README': DATA/'standalone_v2/docs/README.md',
    'Frozen assembled NOTATION': DATA/'standalone_v2/docs/NOTATION.md',
    'Original global chapter': ROOT/'docs/global_nonlinear.md',
    'Original README': ROOT/'docs/README.md',
    'Original NOTATION': ROOT/'docs/NOTATION.md',
    'Original finite dynamics': ROOT/'docs/finite_dynamics.md',
}
claims = []
unresolved = []
for name in ['review_packet_v1.md','review_packet_v2.md','integration_packet_v1.md',
             'integration_packet_v2.md','review_v2_A.md','review_v2_B.md',
             'integration_v2.md','review_resolution.md','selection_report.md']:
    for number,line in enumerate((STUDY/name).read_text().splitlines(), 1):
        if not line.startswith('|'):
            continue
        fields = [x.strip().strip('`') for x in line.strip('|').split('|')]
        hashes = [x for x in fields if re.fullmatch('[a-f0-9]{64}',x)]
        if not hashes:
            continue
        label = fields[0]
        matches = [p for p in [aliases.get(label),ROOT/label,STUDY/label,DATA/label]
                   if p is not None and p.is_file()]
        matches = list(dict.fromkeys(matches))
        if len(matches) != 1:
            unresolved.append({'report':name,'line':number,'label':label})
            continue
        path = matches[0]
        claims.append({'report':name,'line':number,'path':str(path),
                       'expected':hashes[0],'actual':sha(path),'match':sha(path)==hashes[0]})

# Prose hashes in the resolution record, not represented by table rows.
prose = {
 'standalone_v2/validation_report.json':'a43fbd60d00c8891c62d289d1f3c1846722192781c1dde3118b40c7cf2483ec9',
 'integration_v2_edition/validation_report.json':'ae03966c6a78003dad5675ed69a63ddedcfea02bf3eaeee51350601d2e9f92d7',
 'integration_v2/independent_report.json':'d6a9a19b443313827e8f232b9d51a71017aeb28985657582898871e8ef331b14',
 'standalone_v2/docs/global_nonlinear.md':'bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05',
 'standalone_v2/docs/README.md':'5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f',
}
for path,expected in prose.items():
    claims.append({'report':'review_resolution.md prose','path':str(DATA/path),
                   'expected':expected,'actual':sha(DATA/path),'match':sha(DATA/path)==expected})

# Reconstruct all seven documented corrections in memory. Never run assembler.
tree = ast.parse((STUDY/'assemble_proposal_v2.py').read_text())
literals = {n.targets[0].id:ast.literal_eval(n.value) for n in tree.body
            if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)
            and n.targets[0].id in {'ORIGINAL','CHANGES','FINITE_PARAGRAPH'}}
v1 = (STUDY/'proposal_C4_8.md').read_text()
v2 = (STUDY/'proposal_C4_8_v2.md').read_text()
assert sha(STUDY/'proposal_C4_8.md') == literals['ORIGINAL']
first = v1.index('For every finite labeled law and every finite initialized array,')
last = v1.index('Fix \\(m\\), and condition',first)
corrections = literals['CHANGES'] + [(v1[first:last],literals['FINITE_PARAGRAPH'])]
reconstructed = v1
mapping = []
for old,new in corrections:
    assert reconstructed.count(old) == 1
    mapping.append({'old_first_line':v1[:v1.index(old)].count('\n')+1,
                    'new_first_line':v2[:v2.index(new)].count('\n')+1,
                    'old_lines':len(old.splitlines()),'new_lines':len(new.splitlines())})
    reconstructed = reconstructed.replace(old,new,1)
assert reconstructed == v2
restored = reconstructed
for old,new in reversed(corrections):
    assert restored.count(new) == 1
    restored = restored.replace(new,old,1)
assert restored == v1
edits1 = json.loads((STUDY/'promotion_edits.json').read_text())
edits2 = json.loads((STUDY/'promotion_edits_v2.json').read_text())
edits1['append']['source'] = 'proposal_C4_8_v2.md'
assert edits1 == edits2

preservation = {}
for name in ['docs/global_nonlinear.md','docs/README.md','docs/NOTATION.md']:
    live = (ROOT/name).read_bytes()
    fresh = (FRESH/name).read_bytes()
    old = fresh
    if name == 'docs/global_nonlinear.md':
        suffix = b'\n\n'+v2.encode()
        assert old.endswith(suffix)
        assert b''.join(old.splitlines(True)[11439:12991]) == v2.encode()
        old = old[:-len(suffix)]
    counts = []
    for edit in reversed(edits2['replacements']):
        if edit['path'] == name:
            counts.append(live.count(edit['old'].encode()))
            assert counts[-1] == 1 and old.count(edit['new'].encode()) == 1
            old = old.replace(edit['new'].encode(),edit['old'].encode(),1)
    assert old == live
    assert fresh == (DATA/'standalone_v2'/name).read_bytes()
    assert fresh == (DATA/'integration_v2_edition'/name).read_bytes()
    preservation[name] = {'raw_byte_inverse':True,'matches_both_prior_v2_editions':True,
                         'old_text_occurrences':counts,'sha256':sha(FRESH/name)}

tags = re.findall(r'\\tag\{(C\.4\.8\.[^}]+)\}',v2)
expected_tags = {f'C.4.8.{kind}{i}' for kind,n in [('P',20),('S',43),('R',25)] for i in range(1,n+1)}
assert len(tags) == 88 and set(tags) == expected_tags
assert all(('\\tag{'+t+'}') not in (ROOT/'docs/global_nonlinear.md').read_text() for t in tags)
assert set(re.findall(r'C\.4\.8\.[PSR]\d+',v2)) <= expected_tags

reference = (DATA/'review_v2_B/reference_certificate.py').read_bytes()
reference_source = (ROOT/'docs/global_nonlinear.md').read_bytes()
assert reference_source.count(reference) == 1
reference_first = reference_source[:reference_source.index(reference)].count(b'\n')+1
archives = {}
for version in (1,2):
    stored = STUDY/f'integration_checks_v{version}_source.py'
    executed = DATA/f'integration_v{version}/independent_checks.py'
    assert stored.read_bytes() == executed.read_bytes()
    archives[str(stored.relative_to(ROOT))] = {'executed_copy_sha256':sha(executed),'byte_equal':True}

# Read every saved v2 numerical result. Assert all scientific JSON content
# matches the fresh run after deleting only execution metadata.
fresh_g = json.loads((FRESH/'verification/gaussian_report.json').read_text())
fresh_s = json.loads((FRESH/'data/generated/trained_prediction_sampling/statistical_checks/standalone/report.json').read_text())
meta = {'started_utc','completed_utc','source_path','working_directory'}
same_s = lambda v:{k:x for k,x in v.items() if k not in meta}
outcomes = {}
for base in ['review_v2_A','review_v2_B','standalone_v2','integration_v2_edition']:
    gp = DATA/base/('gaussian_report.json' if base.startswith('review_') else 'verification/gaussian_report.json')
    sp = DATA/('statistical_checks/'+base+'/report.json') if base.startswith('review_') else DATA/base/'data/generated/trained_prediction_sampling/statistical_checks/standalone/report.json'
    g,s = json.loads(gp.read_text()),json.loads(sp.read_text())
    assert g == fresh_g and same_s(s) == same_s(fresh_s)
    outcomes[base] = {'gaussian_sha256':sha(gp),'sampling_sha256':sha(sp),
                     'all_scientific_json_fields_equal_fresh_run':True,
                     'sampling_started_utc':s['started_utc'],'sampling_completed_utc':s['completed_utc']}

frozen_fresh = json.loads((FRESH/'validation_report.json').read_text())
prior_validations = {}
for name in ['standalone_v2','integration_v2_edition']:
    v = json.loads((DATA/name/'validation_report.json').read_text())
    assert {k:x for k,x in v.items() if k!='isolated_check_runs'} == {k:x for k,x in frozen_fresh.items() if k!='isolated_check_runs'}
    assert all(x['exit_code']==0 and x['stderr']=='' for x in v['isolated_check_runs'])
    assert all(sha(ROOT/p)==h for p,h in v['frozen_inputs'].items())
    prior_validations[name] = {'all_non_execution_fields_equal':True,'commands_exit_zero':True,'all_input_hashes_current':True}

before = json.loads((HERE/'hashes_before.json').read_text())['files']
after = {p:{'sha256':sha(ROOT/p),'lines':len((ROOT/p).read_bytes().splitlines())} for p in before}
changed = {p:after[p] for p in before if before[p]!=after[p]}
assert not changed
for name in ['hashes_before.json','hashes_after.json']:
    old = json.loads((DATA/'integration_v2'/name).read_text())
    assert all(v=={'sha256':sha(ROOT/p),'lines':len((ROOT/p).read_bytes().splitlines())} for p,v in old.items())
old = json.loads((DATA/'review_v2_B/input_integrity.json').read_text())

result = {'status':'PASS' if not unresolved and all(x['match'] for x in claims) else 'REQUIRES_INSPECTION',
          'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'hash_claims':claims,'unresolved_hash_labels':unresolved,
          'hash_mismatches':[x for x in claims if not x['match']],
          'correction_mapping':mapping,'seven_corrections_exactly_reproduce_v2':True,
          'v2_to_v1_inverse_exact':True,'edit_specs_differ_only_by_candidate_source_name':True,
          'preservation':preservation,'tag_count':len(tags),'old_tag_collisions':0,
          'candidate_assembled_lines':[11440,12991],'candidate_line_count':len(v2.splitlines()),
          'reference_certificate_exact_source_lines':[reference_first,reference_first+len(reference.splitlines())-1],
          'archived_reviewer_sources':archives,'saved_v2_numerical_evidence':outcomes,
          'prior_validation_correspondence':prior_validations,
          'unchanged_preserved_file_count':len(after),'changed_preserved_files':changed,
          'fresh_report_hashes':{str(p.relative_to(HERE)):sha(p) for p in [FRESH/'validation_report.json',FRESH/'verification/gaussian_report.json',FRESH/'data/generated/trained_prediction_sampling/statistical_checks/standalone/report.json']},
          'reviewer_isolation':'Self-declarations and coordinator statement present; no attributable launch/completion events available in permitted saved package. Independence unverified, not disproved.'}
RESULT.write_text(json.dumps(result,indent=2)+'\n')
(HERE/'hashes_after.json').write_text(json.dumps({'utc':result['utc'],'files':after},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'hash_claims'}},indent=2))
