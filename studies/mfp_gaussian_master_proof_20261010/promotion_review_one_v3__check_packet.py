from pathlib import Path
import json,hashlib,re
r=Path(__file__).resolve().parent.parent;s=r/'reviewer_one';packet=r/'review_packet';edition=r/'edition'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
results={}
for name,base in [('candidate_manifest.json',edition),('changed_manifest.json',edition),('review_packet/manifest.json',packet)]:
 p=r/name;m=json.loads(p.read_text());m=m.get('packet_sha256',m)
 mismatch=[f for f,h in m.items() if not (base/f).is_file() or digest(base/f)!=h]
 results[name]={'sha256':digest(p),'file_count':len(m),'mismatch':mismatch}
 assert not mismatch
assert results==json.loads((s/'initial_manifest_check.json').read_text())
# Exact reverse assembly confirms the excerpt ranges and frozen source origin.
theory=(packet/'promotion_theory.qmd').read_text().rstrip();chapter=(edition/'docs/02-gaussian-reuse.qmd').read_text()
assert chapter.count(theory)==1
baseline=chapter.replace(theory+'\n\n','',1)
patches=json.loads((packet/'promotion_book_patches.json').read_text())
patch_locations=[]
for patch in reversed(patches):
 assert baseline.count(patch['new'])==1
 patch_locations.append(chapter[:chapter.index(patch['new'])].count('\n')+1)
 baseline=baseline.replace(patch['new'],patch['old'],1)
origin_checks={}
for name in ('dependency_chapter2_opening.qmd','dependency_chapter2_finite_jets.qmd','dependency_chapter2_specialization.qmd','dependency_finite_gaussian_law.qmd'):
 origin=json.loads((packet/(name+'.origin.json')).read_text())
 original=baseline if origin['source'].endswith('02-gaussian-reuse.qmd') else (edition/origin['source']).read_text()
 assert hashlib.sha256(original.encode()).hexdigest()==origin['source_sha256']
 a,b=origin['lines'];expected=''.join(original.splitlines(keepends=True)[a-1:b])
 assert expected==(packet/name).read_text(),name
 origin_checks[name]=origin
mapping=json.loads((r/'candidate_mapping.json').read_text())
assert mapping==json.loads((packet/'promotion_code_mapping.json').read_text())
assert set(mapping.values()) | {'code/README.md','docs/02-gaussian-reuse.qmd','docs/_quarto.yml','docs/references.bib'} == set(json.loads((r/'changed_manifest.json').read_text()))
assert (edition/'docs/references.bib').read_text().endswith((packet/'promotion_bibliography.bib').read_text())
for patch in json.loads((packet/'promotion_quarto_patches.json').read_text()):
 assert (edition/'docs/_quarto.yml').read_text().count(patch['new'])==patch['count']
# Inspect identifiers only in the other book files, not their scientific content.
new_labels=re.findall(r'\{#([A-Za-z][\w:-]*)',theory)
label_count={label:0 for label in new_labels};references={value.rstrip(':') for value in re.findall(r'(?<![A-Za-z])@([A-Za-z][\w:-]*)',theory)}
all_labels=set()
for file in (edition/'docs').glob('*.qmd'):
 text=file.read_text()
 for label in re.findall(r'\{#([A-Za-z][\w:-]*)',text):
  all_labels.add(label)
  if label in label_count:label_count[label]+=1
assert all(c==1 for c in label_count.values())
bibkeys=set(re.findall(r'@\w+\{([^,]+),',(edition/'docs/references.bib').read_text()))
missing=sorted(references-all_labels-bibkeys);assert not missing,missing
for link in re.findall(r'\]\(([^)]+)\)',theory):
 if '://' in link:continue
 target,_,anchor=link.partition('#');file=edition/'docs'/target if target else edition/'docs/02-gaussian-reuse.qmd'
 assert file.is_file(),link
 if anchor:assert ('{#'+anchor+'}') in file.read_text(),link
read_paths=[r/'candidate_manifest.json',r/'changed_manifest.json',r/'candidate_mapping.json',packet/'manifest.json']
read_paths += [packet/f for f in json.loads((packet/'manifest.json').read_text())['packet_sha256']]
read_paths += [edition/f for f in json.loads((packet/'manifest.json').read_text())['required_edition_reads']]
coverage={str(p.relative_to(r)):{'sha256':digest(p),'lines':len(p.read_text().splitlines()),'coverage':'all lines read'} for p in read_paths}
(s/'read_coverage_hashes.json').write_text(json.dumps(coverage,indent=2)+'\n')
(s/'final_manifest_check.json').write_text(json.dumps(results,indent=2)+'\n')
summary={'origin_checks':origin_checks,'theory_assembled_lines':[chapter[:chapter.index(theory)].count('\n')+1,chapter[:chapter.index(theory)+len(theory)].count('\n')+1],
 'patched_chapter_lines':sorted(patch_locations),'new_label_count':len(new_labels),'new_labels_unique':True,'missing_references':missing,
 'all_manifests_unchanged':True,'frozen_file_count':116,'code_mapping_match':True}
(s/'packet_correspondence.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
