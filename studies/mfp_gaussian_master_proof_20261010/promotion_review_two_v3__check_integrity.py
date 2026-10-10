"""Verify exact frozen bytes and metadata; no scientific reading of complement."""
from pathlib import Path
import hashlib
import json
import re

run = Path(__file__).resolve().parent.parent
scratch = run/'reviewer_two'
edition = run/'edition'
packet = run/'review_packet'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
data = {}
for name in ('candidate_manifest.json','changed_manifest.json','review_packet/manifest.json'):
    data[name] = sha(run/name)
    manifest = json.loads((run/name).read_text())
    entries = manifest['packet_sha256'] if name.startswith('review') else manifest
    root = packet if name.startswith('review') else edition
    mismatches = [key for key,value in entries.items() if sha(root/key)!=value]
    assert not mismatches, (name,mismatches)
    print(name,data[name],len(entries),'entries: verified')
initial=json.loads((scratch/'initial_manifest_hashes.json').read_text())
assert data==initial
(scratch/'final_manifest_hashes.json').write_text(json.dumps(data,indent=2)+'\n')

# Exact reconstruction verifies the three replacements and single insertion
# without consulting or scientifically reading the unassigned book complement.
chapter=(edition/'docs/02-gaussian-reuse.qmd').read_text()
theory=(packet/'promotion_theory.qmd').read_text().rstrip()+'\n\n'
assert chapter.count(theory)==1
chapter=chapter.replace(theory,'',1)
for patch in reversed(json.loads((packet/'promotion_book_patches.json').read_text())):
    assert chapter.count(patch['new'])==patch.get('count',1)
    chapter=chapter.replace(patch['new'],patch['old'],patch.get('count',1))
assert hashlib.sha256(chapter.encode()).hexdigest()=='c79a204fbf7fbb36d9886b94cb5f7f046e5a589be689f9d1d8156ba8f75aa723'
for name in ('dependency_chapter2_opening','dependency_chapter2_finite_jets','dependency_chapter2_specialization','dependency_finite_gaussian_law'):
    origin=json.loads((packet/(name+'.qmd.origin.json')).read_text())
    original=chapter if 'chapter2' in name else (edition/origin['source']).read_text()
    assert hashlib.sha256(original.encode()).hexdigest()==origin['source_sha256']
    a,b=origin['lines']
    assert ''.join(original.splitlines(keepends=True)[a-1:b])==(packet/(name+'.qmd')).read_text()
    print(name,'exact original excerpt',a,b,'verified')
assert json.loads((run/'candidate_mapping.json').read_text())==json.loads((packet/'promotion_code_mapping.json').read_text())
ids=re.findall(r'\{#([^}\s]+)',(packet/'promotion_theory.qmd').read_text())
full=(edition/'docs/02-gaussian-reuse.qmd').read_text()
for identifier in ids:
    assert len(re.findall(r'\{#'+re.escape(identifier)+r'(?:\}|\s)',full))==1,identifier
print(len(ids),'new native identifiers occur exactly once')

for file in (scratch/'produced_kernel_jets').iterdir():
    if file.suffix=='.json' and file.name!='manifest.json':
        dags=json.loads(file.read_text())
        for dag in dags.values():
            known=set()
            for atom in dag['expectations']:
                refs=set(re.findall(r'\bI_[0-9]+\b',atom['integrand']+repr(atom['covariance'])))
                assert refs<=known, (file,atom['name'],refs-known)
                known.add(atom['name'])
            assert set(re.findall(r'\bI_[0-9]+\b',dag['output']))<=known
print('all regenerated expectation graphs are causal')
producer=scratch/'produced_kernel_jets'
manifest=json.loads((producer/'manifest.json').read_text())
assert all(sha(producer/name)==expected for name,expected in manifest['output_sha256'].items())
assert manifest['source_sha256']=={
    'example_mfp_kernel_jets.py':sha(edition/'code/scripts/example_mfp_kernel_jets.py'),
    'mfp_compiler.py':sha(edition/'code/pde/mfp_compiler.py'),
    'mfp_expr.py':sha(edition/'code/pde/mfp_expr.py')}
print('producer source and output hashes verified')

inputs={name:sha(run/name) for name in ('candidate_manifest.json','changed_manifest.json','candidate_mapping.json','review_packet/manifest.json')}
inputs.update({'edition/'+key:value for key,value in json.loads((run/'candidate_manifest.json').read_text()).items()})
inputs.update({'review_packet/'+key:value for key,value in json.loads((packet/'manifest.json').read_text())['packet_sha256'].items()})
(scratch/'verified_frozen_inputs.json').write_text(json.dumps(inputs,indent=2)+'\n')
print('FROZEN BYTE INTEGRITY AND ASSEMBLY CORRESPONDENCE: PASS')
