"""Frozen-input, selective assembly, snippets and production-integrity checks."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys

RUN = Path(__file__).resolve().parent.parent
EDITION = RUN/'edition'
PACKET = RUN/'review_packet'
OUT = RUN/'reviewer_two'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

checks = {}
for name, base in [('candidate_manifest.json', EDITION),('changed_manifest.json', EDITION)]:
    manifest = json.loads((RUN/name).read_text())
    mismatches = [str(base/path) for path, value in manifest.items() if digest(base/path) != value]
    assert not mismatches, mismatches
    checks[name] = dict(sha256=digest(RUN/name), file_count=len(manifest), mismatches=mismatches)
manifest = json.loads((PACKET/'manifest.json').read_text())
assert all(digest(PACKET/path)==value for path,value in manifest['packet_sha256'].items())
checks['review_packet/manifest.json'] = dict(sha256=digest(PACKET/'manifest.json'), file_count=len(manifest['packet_sha256']), mismatches=[])

chapter = (EDITION/'docs/02-gaussian-reuse.qmd').read_text()
theory = (PACKET/'promotion_theory.qmd').read_text().rstrip()+'\n\n'
assert chapter.count(theory)==1
assert theory+'## 7. Reusable finite calculus and forest factorization' in chapter
base_chapter = chapter.replace(theory,'',1)
for patch in reversed(json.loads((PACKET/'promotion_book_patches.json').read_text())):
    assert base_chapter.count(patch['new'])==1
    base_chapter = base_chapter.replace(patch['new'],patch['old'],1)
origin = json.loads((PACKET/'dependency_chapter2_opening.qmd.origin.json').read_text())
assert hashlib.sha256(base_chapter.encode()).hexdigest() == origin['source_sha256']
for path in PACKET.glob('dependency_*.qmd.origin.json'):
    origin = json.loads(path.read_text())
    source = base_chapter if origin['source']=='docs/02-gaussian-reuse.qmd' else (EDITION/origin['source']).read_text()
    assert hashlib.sha256(source.encode()).hexdigest()==origin['source_sha256']
    start,end = origin['lines']
    excerpt = '\n'.join(source.splitlines()[start-1:end])+'\n'
    assert excerpt==path.with_suffix('').with_suffix('').read_text()
checks['assembly'] = dict(chapter2_original_sha256=hashlib.sha256(base_chapter.encode()).hexdigest(),
                          exact_insertions=1, scoped_replacements=3, dependency_excerpt_correspondence=True)
assert json.loads((RUN/'candidate_mapping.json').read_text()) == json.loads((PACKET/'promotion_code_mapping.json').read_text())
checks['mapping_equal'] = True

guide = (EDITION/'code/MFP_CALCULUS.md').read_text()
snippets = re.findall(r'```python\n(.*?)```',guide,re.S)
environment = dict(os.environ,PYTHONPATH='code',PYTHONDONTWRITEBYTECODE='1')
for index, snippet in enumerate(snippets):
    path = OUT/f'guide_snippet_{index+1}.py'
    path.write_text(snippet)
    result = subprocess.run([sys.executable,'-B',str(path)],cwd=EDITION,env=environment,capture_output=True,text=True)
    (OUT/f'guide_snippet_{index+1}.log').write_text(result.stdout+result.stderr)
    assert result.returncode==0,(index,result.stderr)
checks['guide_python_snippets'] = len(snippets)

producer = OUT/'kernel_outputs'
output_manifest = json.loads((producer/'manifest.json').read_text())
assert all(digest(producer/path)==value for path,value in output_manifest['output_sha256'].items())
for path in producer.glob('*.json'):
    data=json.loads(path.read_text())
    if path.name!='manifest.json':
        for jet,dag in data.items():
            known=set()
            for atom in dag['expectations']:
                text=atom['integrand']+' '.join(x for row in atom['covariance'] for x in row)
                used=set(re.findall(r'\bI_\d+\b',text))
                assert used<=known,(path,jet,atom['name'],used-known)
                known.add(atom['name'])
            assert set(re.findall(r'\bI_\d+\b',dag['output']))<=known
checks['producer_outputs_verified'] = len(output_manifest['output_sha256'])
checks['expectation_dags_causal'] = True

# These are the assigned complete reads, not the unassigned surrounding edition.
coverage={}
for path in [PACKET/name for name in manifest['packet_sha256']]+[EDITION/name for name in manifest['required_edition_reads']]:
    coverage[str(path.relative_to(RUN))]=dict(lines=len(path.read_text().splitlines()),sha256=digest(path))
(OUT/'read_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
(OUT/'final_hashes.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
