"""Assemble only canonical docs/code plus the study-owned proposed source."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[2]
SOURCE=Path(__file__).resolve().parent
MAPPING={
    'PROMOTION_check_library.py':'code/tools/check_library.py',
    'PROMOTION_observable_torch_circle.py':'code/pde/observable_torch_circle.py',
    'PROMOTION_test_observable_torch_circle.py':'code/tests/test_observable_torch_circle.py',
    'PROMOTION_validate_torch_circle.py':'code/scripts/validate_torch_circle.py',
}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',required=True); a=p.parse_args()
    target=Path(a.output).resolve(); target.mkdir(parents=True,exist_ok=False)
    for directory in ('docs','code'):
        shutil.copytree(ROOT/directory,target/directory,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    for name,destination in MAPPING.items(): shutil.copyfile(SOURCE/name,target/destination)
    guide=target/'code/README.md'
    guide.write_text(guide.read_text()+'\n'+(SOURCE/'PROMOTION_CIRCLE_GUIDE.md').read_text())
    for name in ('AGENTS.md','RESEARCH_WORKFLOW.md'): shutil.copyfile(ROOT/name,target/name)
    manifest={str(f.relative_to(target)):hashlib.sha256(f.read_bytes()).hexdigest()
              for directory in ('docs','code') for f in sorted((target/directory).rglob('*')) if f.is_file()}
    for name in ('AGENTS.md','RESEARCH_WORKFLOW.md'): manifest[name]=hashlib.sha256((target/name).read_bytes()).hexdigest()
    (target/'FROZEN_SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(target)
if __name__=='__main__': main()
