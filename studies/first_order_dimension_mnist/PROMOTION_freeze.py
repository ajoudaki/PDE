"""Freeze complete neutral review inputs and their mapping/hashes."""
import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True

SOURCE=Path(__file__).resolve().parent
ROOT=SOURCE.parents[1]
RUN=ROOT/'data/generated/first_order_dimension_mnist/promotion_20260916'
spec=importlib.util.spec_from_file_location('assembly',SOURCE/'PROMOTION_assemble.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
EDITION=module.assemble(RUN/'edition_v6')
FROZEN=RUN/'frozen_v4';FROZEN.mkdir(exist_ok=False)
mapping={}
for name,target in module.MAPPING.items():
    path=FROZEN/target;path.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(SOURCE/name,path)
    mapping[name]=target
for name in ('docs/README.md','docs/NOTATION.md','code/README.md','code/pde/__init__.py','code/pde/finite_network.py','code/pde/gaussian_moments.py','code/pde/observable_initialization.py','code/pde/observable_words.py','code/pde/observable_arithmetic.py','code/pde/observable_fixed.py'):
    path=FROZEN/name;path.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(EDITION/name,path)
for name in ('AGENTS.md','RESEARCH_WORKFLOW.md'):
    path=FROZEN/'instructions'/name;path.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,path)
for name in ('PROMOTION_REVIEW_ASSIGNMENT.md','PROMOTION_PLACEMENT.md','PROMOTION_assemble.py'):
    shutil.copyfile(SOURCE/name,FROZEN/name)
for name in ('docs/README.md','code/README.md'):
    path=FROZEN/'dependencies'/('original_'+name.replace('/','_'));path.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,path)
lines=(ROOT/'docs/global_nonlinear.md').read_text().splitlines(keepends=True)
sections=[(185,504),(13276,13297),(13431,13468)]
text='# Complete required source units (unchanged established text)\n\n'
text+='Section 2 and Section 3 provide the complete finite Gaussian source proof and its elementary dependencies. The H3.1 unit supplies its initialized contraction proof; H3.N1/N2 supplies the full finite equations for placement. No circle population convergence proof is imported by the candidate.\n\n'
for first,last in sections:
    text+=f'## Source docs/global_nonlinear.md lines {first}–{last}\n\n'+''.join(lines[first-1:last])+'\n'
(FROZEN/'dependencies/global_nonlinear_source_units.md').write_text(text)
for skill in ('solve-math-rigorously','investigate-conjectures'):
    shutil.copytree(Path('/etc/codex/skills')/skill,FROZEN/'instructions'/skill)
files={str(p.relative_to(FROZEN)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(FROZEN.rglob('*')) if p.is_file()}
manifest=dict(format='general-p1-promotion-candidate-v4',frozen_root=str(FROZEN),edition_root=str(EDITION),
              authors=['/root/author_a','/root','historical study root author','historical scoped initializer author','historical scoped engine contributor'],
              selector='/root/select_a',mapping=mapping,files=files,
              original_global_nonlinear_sha256=hashlib.sha256((ROOT/'docs/global_nonlinear.md').read_bytes()).hexdigest(),
              scientific_dependency_sections=sections,
              excluded='other studies, study history/verdicts, historical numerical outputs, general-d trained-network theorem, MNIST/PCA numerical conclusions')
(SOURCE/'PROMOTION_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(RUN/'frozen_v4_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(frozen_root=str(FROZEN),edition_root=str(EDITION),file_count=len(files)),indent=2))
