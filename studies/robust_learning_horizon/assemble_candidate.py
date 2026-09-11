"""Assemble frozen review inputs without editing maintained files."""
from pathlib import Path
import hashlib,json
study=Path(__file__).resolve().parent
repo=study.parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return (repo/p).read_text()
def write(name,text):
    p=study/name
    if p.exists(): raise RuntimeError("Refusing to overwrite: "+name)
    p.write_text(text)
replacements={"REFERENCE.md":"Section C.4.5.1","RESPONSE.md":"Section C.4.5.2",
 "TRANSFER.md":"Section C.4.5.3","THEOREM.md":"the theorem above"}
def clean(s):
    for old,new in replacements.items(): s=s.replace(old,new)
    bt=chr(96)
    s=s.replace(bt+"docs/special_data_limits.md"+bt,
        "[special-data limits](special_data_limits.md)")
    s=s.replace(bt+"docs/global_nonlinear.md"+bt,
        "[global nonlinear learning](global_nonlinear.md)")
    return s
theorem=(study/"THEOREM.md").read_text()
theorem=clean(theorem[theorem.index("## Exact statement"):].replace("## ","##### "))
pieces=["#### C.4.5. Robust whole-circle prediction after substantial learning\n\n"
 "This theorem extends the prediction and risk scope of the local C.4 "
 "result by comparison with one fitted reference. It does not extend "
 "the local population-flow theorem for arbitrary laws. Equation numbers "
 "are local to each of the statement and three proof units below.\n\n"+theorem]
for source,title in [
 ("REFERENCE.md","##### C.4.5.1. The opposite-label reference and its endpoint"),
 ("RESPONSE.md","##### C.4.5.2. Quantitative reference response tails"),
 ("TRANSFER.md","##### C.4.5.3. Transfer to actual raw GD")]:
    s=(study/source).read_text()
    s=s[s.index("## 1."):].replace("## ","###### ")
    if source=="REFERENCE.md":
        pos=s.index("The maintained study source is")
        s=s[:pos]+("The displayed standard-library Python program is the complete "
          "reproduction procedure. Its exact rational comparisons certify the "
          "weaker bounds m>=.1, a0>.3 and r0>.6 used above. No numerical "
          "training solver is needed.\n")
    pieces.append(title+"\n\n"+clean(s))
addition="\n\n".join(pieces).rstrip()+"\n"
assert not any(x in addition for x in ["studies/","data/generated/","REFERENCE.md",
 "RESPONSE.md","TRANSFER.md","THEOREM.md","/root/","certify_reference.py"])
baseline=read("docs/global_nonlinear.md")
guide=read("docs/README.md")
old="and an open nonlazy family. |"
new=("and an open nonlazy family. A separate fitted-reference transfer gives "
 "whole-circle endpoint approximation and risk at most 1/4 at T=40 for "
 "an explicit, extremely small binary-law neighborhood, with early "
 "paired hidden activity; it does not construct global perturbed-law "
 "population dynamics. |")
assert guide.count(old)==1
newguide=guide.replace(old,new)
old2=("proves an input-population limit and bounds the absolute value of the expected\n"
 "train–test gap, with the time supremum outside the expectation. It does not\n"
 "bound the expected absolute gap, excess risk or useful-risk improvement.")
new2=("proves a local input-population limit and bounds the absolute value of the expected\n"
 "train–test gap, with the time supremum outside the expectation. Its local theorem\n"
 "does not bound the expected absolute gap or excess risk. Section C.4.5 separately\n"
 "proves useful-risk reduction and whole-circle robustness at a fixed time near\n"
 "one fitted opposite-label reference. Its certified neighborhood is extraordinarily\n"
 "small; it supplies neither a global perturbed-law population flow nor evidence\n"
 "that feature learning outperforms frozen or linear models.")
assert guide.count(old2)==1
newguide=newguide.replace(old2,new2)
chapter_edits=[
 {"old":"Section C.4 separately proves local training-law stability and an\ninput-population limit for two hidden tanh layers on the normalized input\ncircle, with the precise statistical and nonlazy conclusions stated there.",
  "new":"Sections C.4.1–C.4.4 separately prove local training-law stability and an\ninput-population limit for two hidden tanh layers on the normalized input\ncircle. Section C.4.5 proves fixed-time risk reduction and whole-circle\nrobustness near one fitted reference, with an explicit extremely small radius."},
 {"old":"C.4 proves its stated simultaneous sampling/width/GD-step limit for the fixed two-hidden-tanh circle-input model on a common local interval.",
  "new":"C.4.1–C.4.4 prove their stated simultaneous sampling/width/GD-step limit for the fixed two-hidden-tanh circle-input model on a common local interval. C.4.5 separately transfers a fitted reference's predictions and useful risk to a fixed-time finite-network guarantee in an explicit small law neighborhood."},
 {"old":"| C.4 | Training-law stability and input-population limit | Global nonlinear: two hidden tanh layers, normalized circle inputs and bounded labels; arbitrary laws, quantitative law/replacement stability, the stated expected-gap bound, simultaneous sampling/width/GD-step consistency, and an open nonlazy family, all on a common local interval. |",
  "new":"| C.4 | Training-law stability, local input-population limit and fitted-reference transfer | Two hidden tanh layers: C.4.1–C.4.4 give arbitrary bounded-label laws, quantitative local stability and simultaneous limits. C.4.5 gives whole-circle endpoint approximation, risk at most 1/4 at T=40, and early paired hidden activity for binary laws in an explicit extremely small neighborhood; no global perturbed-law population flow. |"},
 {"old":"This section proves a local quantitative statement about the actual nonlinear\nlearning algorithm.",
  "new":"Sections C.4.1–C.4.4 prove a local quantitative statement about the actual nonlinear\nlearning algorithm. The separate fixed-accuracy extension is in C.4.5."},
 {"old":"The conclusion concerns finite-time training-law stability with genuine\nnonlinear hidden learning. It does not assert activity for every law,",
  "new":"The preceding local theorem concerns finite-time training-law stability with genuine\nnonlinear hidden learning. It does not assert activity for every law,"}]
chapter=baseline
for edit in chapter_edits:
    assert chapter.count(edit['old'])==1
    chapter=chapter.replace(edit['old'],edit['new'])
edition=chapter.rstrip()+"\n\n"+addition
specs=[
 ("docs/NOTATION.md",None,None),
 ("docs/global_nonlinear.md","### A.1.","## C. A local"),
 ("docs/global_nonlinear.md","### C.4.",None),
 ("docs/special_data_limits.md","## I. Opposite labels","### I.4."),
 ("docs/special_data_limits.md","### III.F.","### III.S."),
 ("docs/finite_dynamics.md",None,"## 5."),
 ("docs/finite_optimization_and_controls.md",None,"## 4."),
 ("docs/global_nonlinear.md","### C.2.","### C.3.")]
deps=[]; spans=[]
for path,start,end in specs:
    full=read(path)
    a=0 if start is None else full.index(start)
    b=len(full) if end is None else full.index(end,a+1)
    piece=full[a:b]
    lo=full[:a].count("\n")+1
    hi=lo+piece.count("\n")-1
    deps.append("# Frozen source: "+path+" lines "+str(lo)+"–"+str(hi)+"\n\n"+piece)
    spans.append({"path":path,"start_line":lo,"end_line":hi,
      "file_sha256":sha((repo/path).read_bytes()),"excerpt_sha256":sha(piece.encode())})
dependency=("# Complete frozen mathematical dependencies\n\n"
 "The new proof uses the stated specializations of these complete units. "
 "Older arctangent and equal-label scopes remain as stated; their different "
 "architectures are not silently substituted. Their proofs are supplied "
 "to expose the dependencies and adaptations.\n\n"+"\n\n".join(deps))
write("P1_ADDITION.md",addition)
write("P1_GLOBAL_BASELINE.md",baseline)
write("P1_GLOBAL_EDITION.md",edition)
write("P1_DOCS_README_BASELINE.md",guide)
write("P1_DOCS_README.md",newguide)
write("P1_DEPENDENCIES.md",dependency)
write("P1_CERTIFY_REFERENCE.py",(study/"certify_reference.py").read_text())
write("P1_CERTIFY_TRANSFER.py",(study/"certify_transfer.py").read_text())
write("P1_EDITS.json",json.dumps({"destinations":["docs/global_nonlinear.md","docs/README.md"],
 "chapter_replacements":chapter_edits,
 "chapter_operation":"apply replacements, then append P1_ADDITION.md after rstrip and two newlines",
 "guide_replacements":[{"old":old,"new":new},{"old":old2,"new":new2}]},indent=2)+"\n")
inputs=["P1_ADDITION.md","P1_GLOBAL_BASELINE.md","P1_GLOBAL_EDITION.md",
 "P1_DOCS_README_BASELINE.md","P1_DOCS_README.md","P1_DEPENDENCIES.md",
 "P1_CERTIFY_REFERENCE.py","P1_CERTIFY_TRANSFER.py","P1_EDITS.json"]
manifest={"version":"P1","authors":["/root","/root/reference","/root/response"],
 "assembler":"/root","selector":"/root/selector","dependency_spans":spans,
 "inputs":{p:sha((study/p).read_bytes()) for p in inputs},
 "source_components":{p:sha((study/p).read_bytes()) for p in
 ["THEOREM.md","REFERENCE.md","RESPONSE.md","TRANSFER.md"]}}
write("P1_MANIFEST.json",json.dumps(manifest,indent=2)+"\n")
print(json.dumps({"addition_lines":len(addition.splitlines()),
 "dependency_lines":len(dependency.splitlines()),"inputs":manifest["inputs"]},indent=2))
