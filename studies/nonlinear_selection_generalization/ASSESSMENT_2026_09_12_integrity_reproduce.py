"""Rerun inspected deterministic checks in fresh, explicitly redirected folders."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import platform
import subprocess
import sys

ROOT=Path('/home/amir/Codes/PDE')
DATA=ROOT/'data/generated/nonlinear_selection_generalization'
STUDY=ROOT/'studies/nonlinear_selection_generalization'
OUT=Path(__file__).resolve().parent
digest=lambda data:sha256(data).hexdigest()

# Preserve originals, including every pre-existing reviewer-generated artifact.
originals={str(p):digest(p.read_bytes()) for p in DATA.rglob('*') if p.is_file() and not p.is_relative_to(DATA/'assessment_20260912')}
originals.update({str(p):digest(p.read_bytes()) for p in STUDY.iterdir() if p.is_file() and not p.name.startswith('ASSESSMENT_')})
results=[]
def execute(command,label):
    run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True)
    (OUT/(label+'.stdout.txt')).write_text(run.stdout)
    (OUT/(label+'.stderr.txt')).write_text(run.stderr)
    record={'label':label,'command':command,'cwd':str(ROOT),'exit_code':run.returncode,'stdout_sha256':digest(run.stdout.encode()),'stderr_sha256':digest(run.stderr.encode())}
    results.append(record)
    assert run.returncode==0,(label,run.stderr)

execute([sys.executable,str(STUDY/'validate_edition_v2.py'),str(OUT/'edition_validation')],'edition_validation')
for label,source_name in [('reviewer_c','scientific_review_v2_c/checks.py'),('reviewer_d','scientific_review_v2_d/checks.py'),('integration','integration_review_v2/check_integration.py')]:
    original=DATA/source_name
    source=original.read_text()
    destination=OUT/label
    destination.mkdir(exist_ok=False)
    if label!='reviewer_c':
        previous="OUT = ROOT / 'data/generated/nonlinear_selection_generalization/"+('scientific_review_v2_d' if label=='reviewer_d' else 'integration_review_v2')+"'"
        assert source.count(previous)==1
        source=source.replace(previous,"OUT = Path(__file__).resolve().parent")
    adapted=destination/original.name
    adapted.write_text(source)
    execute([sys.executable,str(adapted)],label)
    results[-1].update({'original_source':str(original),'original_source_sha256':digest(original.read_bytes()),'reproduction_source_sha256':digest(adapted.read_bytes()),'adaptation':'none; OUT is script directory' if label=='reviewer_c' else 'Only OUT assignment redirected to reproduction script directory'})

old_validation=json.loads((DATA/'edition_validation_v2_20260912_01/validation.json').read_text())
new_validation=json.loads((OUT/'edition_validation/validation.json').read_text())
assert new_validation==old_validation
for label,old_rel in [('reviewer_c','scientific_review_v2_c'),('reviewer_d','scientific_review_v2_d')]:
    assert (OUT/label/'checks.json').read_bytes()==(DATA/old_rel/'checks.json').read_bytes()
old_integration=json.loads((DATA/'integration_review_v2/deterministic_checks.json').read_text())
new_integration=json.loads((OUT/'integration/deterministic_checks.json').read_text())
old_integration.pop('script_sha256');new_integration.pop('script_sha256')
assert old_integration==new_integration
assert (OUT/'integration/guide_diff.txt').read_bytes()==(DATA/'integration_review_v2/guide_diff.txt').read_bytes()
for path,expected in originals.items():
    assert digest(Path(path).read_bytes())==expected,path
result={'result':'PASS: all four deterministic reproductions; originals unchanged', 'completed_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'platform':platform.platform(),'runs':results,'original_files_unchanged':len(originals),'equivalence':'Validator and reviewer C/D JSON outputs exactly identical. Integration JSON identical after removing only adapted script hash; guide diff identical.','limits':'Copied reviewer-specific statements describe original check scope; these reruns are not new independent scientific reviews. No training or maintained-code edits.'}
(OUT/'reproduction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
