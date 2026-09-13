"""Read-only follow-up packaging checks, within the predeclared test envelope."""
from pathlib import Path
import hashlib
import json
import resource
import time
import markdown

resource.setrlimit(resource.RLIMIT_CPU,(30,)*2)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,)*2)
started=time.process_time()
root=Path('/home/amir/Codes/PDE')
out=root/'data/generated/observable_hierarchy/H4_integration_v1'
edition=root/'data/generated/observable_hierarchy/H4_candidate_v1'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
missing=[]
for row in json.loads((out/'links.json').read_text()):
    if not row['exists_in_edition']:
        missing.append(dict(source=row['source'],target=row['target'],
            exists_in_established=(root/row['source']).parent.joinpath(row['target']).is_file()))
bad=[]
records=json.loads((out/'producer_records.json').read_text())
for row in records:
    for name,value in row['source_hashes'].items():
        if sha(edition/'code/pde'/name)!=value:bad.append([row['id'],name])
    if row['producer_sha256']!=sha(edition/'code/scripts/validate_observable_horizon.py'):
        bad.append([row['id'],'producer'])
section=(root/'studies/observable_hierarchy/H4_proposed_section.md').read_text()
render=markdown.markdown(section,extensions=['tables','fenced_code','toc'])
(out/'section_structure.html').write_text(render)
literal_bold={line:line in render for line in
    ('**3.1 Field and gate constants','**3.2 Lower pulse difference','**3.3 Upper row difference')}
report=dict(missing_in_edition=missing,producer_source_mismatches=bad,
    markdown_package_version=markdown.__version__,rendering_scope='ATX heading and inline emphasis structure only; no TeX renderer or full-book PDF audit',
    literal_unclosed_bold=literal_bold,section_render_sha256=sha(out/'section_structure.html'),
    source_sha256=sha(Path(__file__)),cpu_seconds=time.process_time()-started)
(out/'supplement.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
