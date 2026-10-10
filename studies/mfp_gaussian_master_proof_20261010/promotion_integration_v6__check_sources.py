from pathlib import Path
import json,hashlib,re,collections,sys
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
R=Path(__file__).resolve().parent.parent; E=R/'edition'; P=R/'review_packet'; B=R.parent/'promotion_baseline_v4/edition'; S=R/'integration_reviewer'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((R/'candidate_manifest.json').read_text()); actual={f:sha(E/f) for f in m}; mismatch={f:[h,actual[f]] for f,h in m.items() if actual[f]!=h}
(S/'initial_source_hashes.json').write_text(json.dumps(actual,indent=2))
assert not mismatch,mismatch
pm=json.loads((P/'manifest.json').read_text())['packet_sha256']; assert all(sha(P/f)==h for f,h in pm.items())
# Reconstruct baseline without writing any candidate/baseline file.
new=(E/'docs/02-gaussian-reuse.qmd').read_text(); theory=(P/'promotion_theory.qmd').read_text().rstrip()+'\n\n'; assert new.count(theory)==1
restored=new.replace(theory,'',1)
for patch in json.loads((P/'promotion_book_patches.json').read_text()):
 assert restored.count(patch['new'])==1
 restored=restored.replace(patch['new'],patch['old'],1)
assert restored==(B/'docs/02-gaussian-reuse.qmd').read_text()
for name,patchfile in [('code/README.md','promotion_code_readme_patches.json'),('docs/_quarto.yml','promotion_quarto_patches.json')]:
 restored=(E/name).read_text()
 for p in json.loads((P/patchfile).read_text()):
  count=p.get('count',1); assert restored.count(p['new'])==count
  restored=restored.replace(p['new'],p['old'],count)
 assert restored==(B/name).read_text(),name
bib=(B/'docs/references.bib').read_text().rstrip()+'\n\n'+(P/'promotion_bibliography.bib').read_text(); assert bib==(E/'docs/references.bib').read_text()
changed=json.loads((R/'changed_manifest.json').read_text()); bm=json.loads((R/'baseline_manifest.json').read_text())
assert all(sha(E/f)==sha(B/f) for f in bm if f not in changed)
for origin in P.glob('*.origin.json'):
 o=json.loads(origin.read_text()); source=B/o['source']; lines=source.read_text().splitlines(True); piece=''.join(lines[o['lines'][0]-1:o['lines'][1]])
 assert piece==(P/origin.name.removesuffix('.origin.json')).read_text()
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.bad=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='a' and 'href' in a:self.links.append(a['href'])
  if 'quarto-xref' in a.get('class','') and 'unresolved' in a.get('class',''):self.bad.append(a)
html=R/'rendered_html'; pages={}
for path in html.glob('*.html'):
 p=Parse();p.feed(path.read_text());pages[path]=p
errors=[]
for path,p in pages.items():
 for ident,c in collections.Counter(p.ids).items():
  if c>1:errors.append(['duplicate',str(path.name),ident,c])
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc or not u.path and not u.fragment:continue
  target=(path.parent/unquote(u.path)).resolve() if u.path else path
  if not target.exists():errors.append(['missing-file',path.name,link]);continue
  if u.fragment and target.suffix=='.html':
   q=pages.get(target)
   if q is None:q=Parse();q.feed(target.read_text())
   if unquote(u.fragment) not in q.ids:errors.append(['missing-fragment',path.name,link])
 errors.extend(['unresolved',path.name,a] for a in p.bad)
# Structural information only for the unassigned old scientific complement.
headings={p.name:[x for x in p.read_text().splitlines() if re.match(r'^#{1,2} ',x)] for p in (E/'docs').glob('*.qmd')}
(S/'headings.json').write_text(json.dumps(headings,indent=2))
report=dict(source_files=len(m),changed_files=list(changed),packet_files=len(pm),source_mismatches=mismatch,baseline_exact_restoration=True,older_excerpts_match=True,html_pages=len(pages),html_link_errors=errors,new_section_lines=len(theory.splitlines()),chapter_lines=len(new.splitlines()))
(S/'source_link_results.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
