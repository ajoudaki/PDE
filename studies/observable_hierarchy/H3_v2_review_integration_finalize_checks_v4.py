import datetime, hashlib, json, resource, time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
started=time.process_time()
scratch=Path(__file__).resolve().parent
repo=scratch.parents[3]
entry=json.loads((scratch/'entry_hashes.json').read_text())
files={}
for name,prior in entry['files'].items():
    p=repo/name
    content=p.read_bytes();sha=hashlib.sha256(content).hexdigest()
    assert sha==prior['sha256']==prior['expected'],name
    assert len(content)==prior['bytes'],name
    files[name]=dict(sha256=sha,bytes=len(content),matches_entry=True,matches_expected=True)
assert len(files)==157
aux=[]
for executed,retained in [('bounded_command.py','H3_v2_reproduction_budget_wrapper_v2.py'),
                          ('guide_example.py','H3_v2_reproduction_guide_example_v2.py'),
                          ('read_only_audit.py','H3_v2_reproduction_read_only_audit_v2.py')]:
    a=scratch.parent/'H3_v2_reproducer_v2'/executed
    b=repo/'studies/observable_hierarchy'/retained
    assert a.read_bytes()==b.read_bytes()
    aux.append(dict(executed=str(a),fully_read_source=str(b),sha256=hashlib.sha256(a.read_bytes()).hexdigest()))
result=dict(identity='/root/h3v2_integration_v4',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            count=len(files),files=files,auxiliary_byte_correspondence=aux,
            cpu_seconds=time.process_time()-started)
(scratch/'exit_hashes.json').write_text(json.dumps(result,indent=2)+'\n')
# Preserve the initial failed checker exactly from the sole two-line removal.
source=(scratch/'static_checks.py').read_text()
marker='# Obtain exact inserted bytes, without allowing whitespace changes elsewhere.\n'
failed="without=chapter.replace(section,'',1)\nassert without==oldchapter or without.replace('\\n\\n\\n','\\n\\n',1)==oldchapter\n"
(scratch/'static_checks_failed_v1.py').write_text(source.replace(marker,failed+marker,1))
artifacts={str(p.relative_to(scratch)):dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)
           for p in sorted(scratch.rglob('*')) if p.is_file() and p.name!='artifact_hashes.json'}
(scratch/'artifact_hashes.json').write_text(json.dumps(dict(utc=result['utc'],files=artifacts),indent=2)+'\n')
print(json.dumps(dict(utc=result['utc'],input_count=len(files),cpu_seconds=result['cpu_seconds'],artifacts=artifacts),indent=2))
