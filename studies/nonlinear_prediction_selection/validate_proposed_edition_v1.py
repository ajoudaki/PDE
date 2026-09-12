"""Build and validate a standalone proposed edition; never edit established files."""
from pathlib import Path
import difflib, hashlib, json, re, shutil, subprocess, sys, platform
STUDY=Path(__file__).resolve().parent
REPO=STUDY.parents[1]
OUT=REPO/'data/generated/nonlinear_prediction_selection/standalone_v1'
if OUT.exists():
    raise SystemExit('Fresh output required; existing standalone_v1 preserved.')
OUT.mkdir(parents=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
review=json.loads((STUDY/'REVIEW_MANIFEST_v1.json').read_text())
for name,meta in review.items():
    assert sha(STUDY/name)==meta['sha256'],name
manifest=json.loads((STUDY/'DEPENDENCY_MANIFEST_v1.json').read_text())
for name,meta in manifest.items():
    assert sha(STUDY/name)==meta['sha256'],name
    if 'source_sha256' in meta:
        assert sha(REPO/meta['source'])==meta['source_sha256'],meta['source']
    else:
        assert sha(REPO/meta['source'])==meta['sha256'],meta['source']
# Copy only the established documentation tree into a non-Git validation edition.
# Its unreviewed complement is used only for byte preservation and link targets.
shutil.copytree(REPO/'docs',OUT/'docs')
base=(REPO/'docs/global_nonlinear.md').read_text()
proposal=json.loads((STUDY/'PROPOSED_EDITS_v1.json').read_text())
edit=proposal['docs/global_nonlinear.md']['replace_once']
assert base.count(edit['old'])==1
canonical=(STUDY/proposal['docs/global_nonlinear.md']['append_file']).read_text()
updated=base.replace(edit['old'],edit['new'],1).rstrip()+'\n\n'+canonical
(OUT/'docs/global_nonlinear.md').write_text(updated)
guide=(STUDY/proposal['docs/README.md']['replacement_file']).read_text()
(OUT/'docs/README.md').write_text(guide)
assert (OUT/'docs/NOTATION.md').read_bytes()==(REPO/'docs/NOTATION.md').read_bytes()
# Reversing the one scope insertion and removing the append recovers the old text.
prefix=updated[:-len(canonical)].rstrip()
assert prefix.replace(edit['new'],edit['old'],1)==base.rstrip()
# Every other documentation file is preserved byte for byte.
preserved=[]
for p in (REPO/'docs').rglob('*'):
    if p.is_file() and p.relative_to(REPO/'docs').as_posix() not in {'README.md','global_nonlinear.md'}:
        q=OUT/'docs'/p.relative_to(REPO/'docs')
        assert p.read_bytes()==q.read_bytes(),str(p)
        preserved.append(p.relative_to(REPO).as_posix())
# Validate every new Markdown link. Unchanged links are preserved, not reclassified.
linkpat=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
def slug(s):
    s=re.sub(r'<[^>]+>','',s).lower()
    s=re.sub(r'[^\w\- ]','',s)
    return s.replace(' ','-')
def anchors(text):
    return {slug(m[1].strip()) for m in re.finditer(r'^#{1,6}\s+(.+)$',text,re.M)}
checked_links=[]
for relative,newtext,oldtext in [('docs/global_nonlinear.md',updated,base),('docs/README.md',guide,(REPO/'docs/README.md').read_text())]:
    oldlinks=set(linkpat.findall(oldtext))
    for link in sorted(set(linkpat.findall(newtext))-oldlinks):
        assert not re.match(r'\w+://',link),('unexpected new remote link',link)
        path,sep,fragment=link.partition('#')
        target=(OUT/relative).parent/path if path else OUT/relative
        assert target.is_file(),str(target)
        if sep: assert fragment in anchors(target.read_text()),(link,'missing anchor')
        checked_links.append({'from':relative,'target':link})
assert checked_links
for i in range(1,10): assert canonical.count('\\tag{NS'+str(i)+'}')==1,i
assert canonical.count('\\[')==canonical.count('\\]')
assert canonical.count('\\(')==canonical.count('\\)')
for forbidden in ['studies/','ROUTE_','coordinator','CONTINUATION_CONTROL_TUBE.md','SLOW_SELECTION.md','when proved']:
    assert forbidden not in canonical,forbidden
# Run the exact upstream numerical certificate in this standalone edition.
checks=OUT/'checks'; checks.mkdir()
shutil.copyfile(STUDY/'verify_reference_certificate.py',checks/'verify_reference_certificate.py')
run=subprocess.run([sys.executable,'checks/verify_reference_certificate.py'],cwd=OUT,text=True,capture_output=True)
(checks/'certificate_stdout.txt').write_text(run.stdout)
(checks/'certificate_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
# Save the concrete proposed patch as study-owned source, not only generated data.
diffs=[]
for relative,newtext in [('docs/global_nonlinear.md',updated),('docs/README.md',guide)]:
    oldtext=(REPO/relative).read_text()
    diffs.extend(difflib.unified_diff(oldtext.splitlines(True),newtext.splitlines(True),fromfile='a/'+relative,tofile='b/'+relative))
(STUDY/'PROPOSED_EDITION_v1.patch').write_text(''.join(diffs))
result={'python':platform.python_version(),'command':'python studies/nonlinear_prediction_selection/validate_proposed_edition_v1.py','output_directory':str(OUT),'candidate_sha256':sha(STUDY/'CANONICAL_ADDITION_v1.md'),'proposed_global_sha256':sha(OUT/'docs/global_nonlinear.md'),'proposed_guide_sha256':sha(OUT/'docs/README.md'),'notation_sha256':sha(OUT/'docs/NOTATION.md'),'preserved_other_documentation_files':len(preserved),'new_links_checked':checked_links,'certificate_exit':run.returncode,'certificate_output':run.stdout.strip(),'certificate_stdout_sha256':sha(checks/'certificate_stdout.txt'),'patch_sha256':sha(STUDY/'PROPOSED_EDITION_v1.patch'),'limitations':['No new training experiment or empirical claim.','No full-book mathematical audit of the unchanged complement.','No whole-book link audit: newly introduced links checked and older files/links preserved.','No changes applied to established book or code.']}
(OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
(STUDY/'STANDALONE_VALIDATION_v1.md').write_text('# Standalone proposed-edition validation\n\nCoordinator validation, not an independent review. A fresh documentation-only\nstandalone edition was built without changing established files. Every frozen\nreview input hash and its established source hash matched. The entire older\nglobal chapter was recovered by reversing the one scope insertion and removing\nthe append; every other documentation file except the proposed guide was\npreserved byte for byte. New chapter links, equation labels and math delimiter\nbalance passed, and the exact upstream rational certificate passed again.\n\nExact run record:\n\n```json\n'+json.dumps(result,indent=2)+'\n```\n')
print(json.dumps(result,indent=2))
