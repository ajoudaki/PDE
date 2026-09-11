"""Standalone validation of P1 assembly and exact rational constants."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,sys,platform
p=argparse.ArgumentParser()
p.add_argument("--inputs",type=Path,required=True)
p.add_argument("--output",type=Path,required=True)
args=p.parse_args()
inp=args.inputs.resolve();out=args.output.resolve()
out.mkdir(parents=True,exist_ok=False)
def sha(b): return hashlib.sha256(b).hexdigest()
manifest=json.loads((inp/"P1_MANIFEST.json").read_text())
for name,digest in manifest["inputs"].items():
    assert sha((inp/name).read_bytes())==digest,name
edits=json.loads((inp/"P1_EDITS.json").read_text())
chapter=(inp/"P1_GLOBAL_BASELINE.md").read_text()
for change in edits["chapter_replacements"]:
    assert chapter.count(change["old"])==1
    chapter=chapter.replace(change["old"],change["new"])
addition=(inp/"P1_ADDITION.md").read_text()
chapter=chapter.rstrip()+"\n\n"+addition
assert chapter==(inp/"P1_GLOBAL_EDITION.md").read_text()
guide=(inp/"P1_DOCS_README_BASELINE.md").read_text()
for change in edits["guide_replacements"]:
    assert guide.count(change["old"])==1
    guide=guide.replace(change["old"],change["new"])
assert guide==(inp/"P1_DOCS_README.md").read_text()
assert addition.count(r"\[")==addition.count(r"\]")
assert addition.count(r"\begin{")==addition.count(r"\end{")
assert not re.search(r"studies/|data/generated/|/root/|REFERENCE\.md|RESPONSE\.md|TRANSFER\.md",addition)
fence=chr(96)*3
blocks=re.findall(fence+r"python\n(.*?)\n"+fence,addition,re.S)
assert len(blocks)==1
certificate=(inp/"P1_CERTIFY_REFERENCE.py").read_text().split("\n",2)[2]
assert blocks[0].strip()==certificate.strip(),"embedded certificate differs"
docs=out/"docs";docs.mkdir()
(docs/"global_nonlinear.md").write_text(chapter)
(docs/"README.md").write_text(guide)
dependencies=(inp/"P1_DEPENDENCIES.md").read_text()
parts=re.split(r"(?m)^# Frozen source: (.*?) lines ([0-9]+)–([0-9]+)\n\n",dependencies)
collected={}
for i in range(1,len(parts),4):
    path,lo,hi,body=parts[i:i+4]
    candidates=[v for v in manifest["dependency_spans"] if v["path"]==path and v["start_line"]==int(lo)]
    assert len(candidates)==1
    info=candidates[0];matched=None
    for k in range(5):
        candidate=body if k==0 else body[:-k]
        if sha(candidate.encode())==info["excerpt_sha256"]:
            matched=candidate;break
    assert matched is not None,(path,lo)
    collected.setdefault(path,[]).append(matched)
for path,spans in collected.items():
    if path=="docs/global_nonlinear.md": continue
    dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text("\n\n".join(spans))
checks=[]
for name in ["P1_CERTIFY_REFERENCE.py","P1_CERTIFY_TRANSFER.py"]:
    source=(inp/name).read_bytes()
    target=out/name;target.write_bytes(source)
    result=subprocess.run([sys.executable,str(target)],cwd=out,text=True,capture_output=True)
    (out/(name+".stdout")).write_text(result.stdout)
    (out/(name+".stderr")).write_text(result.stderr)
    checks.append({"name":name,"sha256":sha(source),"command":[sys.executable,str(target)],
                  "exit_code":result.returncode,"stdout":result.stdout,"stderr":result.stderr})
    assert result.returncode==0,name
record={"status":"PASS","python":platform.python_version(),"input_directory":str(inp),
 "output_directory":str(out),"manifest_sha256":sha((inp/"P1_MANIFEST.json").read_bytes()),
 "addition_lines":len(addition.splitlines()),"dependency_lines":len(dependencies.splitlines()),
 "checks":checks,"outputs":{str(f.relative_to(out)):sha(f.read_bytes()) for f in sorted(docs.glob("*.md"))},
 "limits":"Exact assembly/preservation, source hashes, simple markup balance, rational constants; no formal proof assistant, training experiment, finite-width rate or unchanged-chapter audit."}
(out/"validation.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))

