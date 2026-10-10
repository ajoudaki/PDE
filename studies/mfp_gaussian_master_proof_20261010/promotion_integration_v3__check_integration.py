from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
from urllib.parse import urlsplit,unquote
import json,re,hashlib
R=Path(__file__).resolve().parents[1]; E=R/'edition'; S=R/'integration_reviewer'; B=R.parent/'promotion_baseline_v1/edition'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
class Page(HTMLParser):
 def __init__(self,p):
  super().__init__();self.ids=[];self.links=[];self.resources=[];self.tags=[];self.text=[];self.feed(p.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs); self.tags.append((tag,a))
  if 'id' in a:self.ids.append(a['id'])
  if 'href' in a:self.links.append(a['href'])
  if 'src' in a:self.resources.append(a['src'])
 def handle_data(self,data):self.text.append(data)
result={}
for fmt in ('html','pdf','latex'):
 base=R/f'rendered_{fmt}'; pages={p.resolve():Page(p) for p in base.glob('*.html')};bad=[]; duplicates=[];external=set(); link_count=0
 for path,page in pages.items():
  duplicates.extend((path.name,k,n) for k,n in Counter(page.ids).items() if n>1)
  for link in page.links+page.resources:
   u=urlsplit(link)
   if u.scheme or u.netloc:external.add(link);continue
   target=(path.parent/unquote(u.path)).resolve() if u.path else path
   if not u.path and not u.fragment:continue
   link_count+=1
   if not target.exists():bad.append((path.name,link,'missing file'));continue
   if u.fragment and target.suffix=='.html':
    tp=pages.get(target) or Page(target)
    if unquote(u.fragment) not in tp.ids:bad.append((path.name,link,'missing fragment'))
 result[fmt]={'pages':len(pages),'local_links_resources':link_count,'broken':bad,'duplicate_ids':duplicates,'external_resource_count':len(external)}
 if fmt=='html':
  chapter=pages[(base/'02-gaussian-reuse.html').resolve()]
  result['new_formals']=[(tag,attrs) for tag,attrs in chapter.tags if re.match(r'(def|thm|lem|prp|proof|eq)-mfp-',attrs.get('id',''))]
  result['html_unresolved']={p.name:re.findall(r'(?:@(?:eq|sec|thm|lem|prp|cor|def)-[\w-]+|\?\?)',' '.join(page.text)) for p,page in pages.items()}
  result['html_unresolved']={k:v for k,v in result['html_unresolved'].items() if v}
# Exact assembly and preservation, without writing candidate sources.
for file,patch in [('docs/02-gaussian-reuse.qmd','promotion_book_patches.json'),('code/README.md','promotion_code_readme_patches.json'),('docs/_quarto.yml','promotion_quarto_patches.json')]:
 text=(B/file).read_text()
 for p in json.loads((R/'review_packet'/patch).read_text()):
  assert text.count(p['old'])==p.get('count',1),(file,p['old'][:80]);text=text.replace(p['old'],p['new'],p.get('count',1))
 if file.endswith('02-gaussian-reuse.qmd'):
  anchor='## 7. Reusable finite calculus and forest factorization {#sec-docs-gaussian-calculus-l1824}'
  text=text.replace(anchor,(R/'review_packet/promotion_theory.qmd').read_text().rstrip()+'\n\n'+anchor)
 result[file+'_exact_assembly']=text==(E/file).read_text()
oldids={f.name:re.findall(r'\{#([\w-]+)',f.read_text()) for f in (B/'docs').glob('*.qmd')}
newids={f.name:re.findall(r'\{#([\w-]+)',f.read_text()) for f in (E/'docs').glob('*.qmd')}
result['old_anchors_missing']={k:list(set(v)-set(newids[k])) for k,v in oldids.items() if set(v)-set(newids[k])}
ids=[a for v in newids.values() for a in v];result['source_duplicate_ids']=[(k,n) for k,n in Counter(ids).items() if n>1]
result['source_id_count']=len(ids);result['old_id_count']=sum(map(len,oldids.values()))
bm=json.loads((R/'baseline_manifest.json').read_text()); cm=json.loads((R/'candidate_manifest.json').read_text());result['changed_old_files']=[k for k,v in bm.items() if cm.get(k)!=v];result['new_files']=list(sorted(set(cm)-set(bm)))
result['bibliography_append_exact']=(B/'docs/references.bib').read_text().rstrip()+'\n\n'+(R/'review_packet/promotion_bibliography.bib').read_text()==(E/'docs/references.bib').read_text()
result['new_section_lines']=len((R/'review_packet/promotion_theory.qmd').read_text().splitlines());result['chapter_lines']=len((E/'docs/02-gaussian-reuse.qmd').read_text().splitlines())
tex=(R/'rendered_latex/book-latex/DTDL.tex').read_text();labels=re.findall(r'\\label\{([^}]+)\}',tex);refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
result['latex']|={'labels':len(labels),'duplicate_labels':[(k,n) for k,n in Counter(labels).items() if n>1],'unresolved_native_refs':list(set(refs)-set(labels)),'new_formal_environments':re.findall(r'\\begin\{(definition|theorem|lemma|proposition|proof)\}',tex[tex.index('\\section{Fixed finite Gaussian derivative programs}'):tex.index('\\section{7. Reusable finite calculus')]) if '\\section{Fixed finite Gaussian derivative programs}' in tex else 'find heading separately','graphics':re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',tex)}
result['packaged_source_mismatches']={fmt:[k for k,v in cm.items() if k.startswith(('code/','docs/')) and sha(R/f'rendered_{fmt}'/k)!=v] for fmt in ('html','pdf','latex')}
(S/'integration_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('new_formals','html_unresolved')},indent=2));print('new formal ID count',len(result['new_formals']));print('unresolved HTML',result['html_unresolved'])
headings={p.name:[l for l in p.read_text().splitlines() if re.match(r'^#{1,2} ',l)] for p in (E/'docs').glob('*.qmd')};(S/'chapter_headings.json').write_text(json.dumps(headings,indent=2)+'\n')
