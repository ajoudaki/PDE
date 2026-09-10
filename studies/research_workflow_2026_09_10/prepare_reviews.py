"""Prepare only explicit workflow-review inputs; never a checkout copy."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[2];b=Path(__file__).resolve().parent
files=['AGENTS.md','RESEARCH_WORKFLOW.md','README.md','studies/README.md','data/README.md','studies/_workflow.py','studies/research_workflow_2026_09_10/tests/test_workflow.py']
inputs=[]
for name in files:
 p=root/name;inputs.append({'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'lines':len(p.read_text().splitlines())})
round_name='r1';permanent=b/'reviews'/round_name/'inputs';permanent.mkdir(parents=True,exist_ok=False)
for x in inputs:
 dst=permanent/x['path'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((root/x['path']).read_bytes());dst.chmod(0o444)
(b/'reviews'/round_name/'INPUTS.json').write_text(json.dumps(inputs,indent=2)+'\n')
for label in ['a','b']:
 target=root/'data/generated/research_workflow_2026_09_10'/('review_'+round_name+'_'+label);target.mkdir(parents=True,exist_ok=False)
 for x in inputs:
  dst=target/x['path'];dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((root/x['path']).read_bytes());dst.chmod(0o444)
 (target/'INPUTS.json').write_text(json.dumps(inputs,indent=2)+'\n');(target/'INPUTS.json').chmod(0o444)
 print(label,target)
print('Frozen',len(inputs),'files;',sum(x['lines'] for x in inputs),'lines.')
