from pathlib import Path
import re,json,hashlib,sys,platform
import numpy
root=Path(__file__).resolve().parents[1];scratch=root/'reviewer_one'
initial=json.loads((scratch/'initial_hashes.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source_hashes={};checks={}
for name,base,key in [('candidate_manifest.json',root/'edition',None),('changed_manifest.json',root/'edition',None),('review_packet/manifest.json',root/'review_packet','packet_sha256')]:
 d=json.loads((root/name).read_text());d=d[key] if key else d
 mismatch=[p for p,h in d.items() if sha(base/p)!=h]
 checks[name]={'sha256':sha(root/name),'files':len(d),'mismatches':mismatch}
 assert not mismatch
 assert checks[name]['sha256']==initial[name]['sha256']
 for p in d:source_hashes[str((base/p).relative_to(root))]=sha(base/p)
assert all(initial['all_input_hashes'][p]==h for p,h in source_hashes.items())
coverage={str(p.relative_to(root)):len(p.read_text().splitlines()) for p in sorted((root/'review_packet').iterdir()) if p.is_file()}
for name in json.loads((root/'review_packet/manifest.json').read_text())['required_edition_reads']:
 coverage['edition/'+name]=len((root/'edition'/name).read_text().splitlines())
coverage['candidate_mapping.json']=len((root/'candidate_mapping.json').read_text().splitlines())
(scratch/'read_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
all_ids=set()
for p in (root/'edition/docs').glob('*.qmd'):
 all_ids.update(re.findall(r'\{#([A-Za-z][A-Za-z0-9_-]*)',p.read_text()))
text=(root/'review_packet/promotion_theory.qmd').read_text()
refs=set(re.findall(r'@((?:sec|eq|thm|lem|prp|cor|def|rem|proof)-[A-Za-z0-9_-]+)',text))
missing=sorted(refs-all_ids);ids=re.findall(r'\{#([A-Za-z][A-Za-z0-9_-]*)',text)
assert not missing
assert len(set(ids))==len(ids)
record={'python':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'manifest_checks':checks,'new_theory_refs':len(refs),'missing_ref_identifiers':missing,'new_theory_ids':len(ids),'manifest_source_hashes_identical':True,'read_coverage':coverage,'source_integrity':'Every manifest-listed source is unchanged. Unlisted concurrent Quarto outputs/caches are excluded from scientific input scope.'}
(scratch/'verification_summary.json').write_text(json.dumps(record,indent=2)+'\n')
(scratch/'final_hashes.json').write_text(json.dumps({'checks':checks,'all_manifest_input_hashes':source_hashes},indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='read_coverage'},indent=2))
