from pathlib import Path
import re,json,hashlib,collections
R=Path(__file__).resolve().parent.parent;S=R/'integration_reviewer';E=R/'edition'
texpath=R/'rendered_latex/book-latex/DTDL.tex';text=texpath.read_text()
labels=re.findall(r'\\label\{([^}]+)\}',text);targets=set(labels)|set(re.findall(r'\\hypertarget\{([^}]+)\}',text));dups={k:v for k,v in collections.Counter(labels).items() if v>1}
refs=set(re.findall(r'\\(?:ref|eqref|autoref)\{([^}]+)\}',text))|set(re.findall(r'\\hyperref\[([^]]+)\]',text));missing=sorted(refs-targets)
new=text[text.index('\\section{Fixed finite Gaussian derivative'):text.index('\\section{7. Reusable finite calculus')]
imgs=re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',text);missing_images=[p for p in imgs if not (texpath.parent/p).exists()]
links=re.findall(r'\\href\{(code/[^}]+)\}',text);missing_code=[p for p in links if not (texpath.parent/p).is_file()]
newids=re.findall(r'\{#([^}]+)\}',(R/'review_packet/promotion_theory.qmd').read_text());newids+=re.findall(r'\[\]\{#([^}]+)\}',(R/'review_packet/promotion_theory.qmd').read_text())
missing_new=[x for x in set(newids) if x not in targets]
logs={}
for f in ['html','pdf','latex']:
 d=json.loads((R/f'render_logs/{f}.json').read_text()); logs[f]=d
summary={k:{a:v for a,v in d.items() if a not in ('manifest','source_manifest','output_sha256','hashes')} for k,d in logs.items()}
for out in [R/'rendered_html',R/'rendered_pdf',R/'rendered_latex/book-latex']:
 # Packaged code and docs inputs must correspond to frozen edition sources.
 manifest=json.loads((R/'candidate_manifest.json').read_text());bad=[];count=0
 for f,h in manifest.items():
  if f.startswith(('docs/','code/')):
   path=out/f
   if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=h:bad.append(f)
   count+=1
 summary[str(out.relative_to(R))]=dict(checked_source_bundle=count,bad=bad)
report=dict(label_count=len(labels),duplicate_labels=dups,missing_references=missing,missing_new_ids=missing_new,missing_images=missing_images,missing_code_links=missing_code,new_proof_environments=new.count('\\begin{proof}'),new_formal_environments={n:new.count('\\begin{'+n+'}') for n in ['theorem','lemma','proposition','definition']},counter_configuration='\\counterwithout{definition}{section}' in text,logs=summary)
(S/'export_checks.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='logs'},indent=2));print('BUNDLES',{k:v for k,v in summary.items() if k.startswith('rendered')})
