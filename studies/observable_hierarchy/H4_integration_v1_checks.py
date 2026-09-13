"""Independent bounded H4 integration checks; no research trajectories.

Run the identical copy in data/generated/observable_hierarchy/H4_integration_v1.
Only hashes are read from manifests' files outside the explicit content scope.
The plan was saved before execution. Aggregate process budget: 600 CPU s,
4 GiB per process, one numerical thread; deterministic synthetic steps only.
"""
from pathlib import Path
import difflib
import hashlib
import json
import math
import os
import re
import resource
import shutil
import subprocess
import sys
import time

ROOT = Path('/home/amir/Codes/PDE')
EDITION = ROOT/'data/generated/observable_hierarchy/H4_candidate_v1'
OUT = ROOT/'data/generated/observable_hierarchy/H4_integration_v1'
MANIFEST = ROOT/'studies/observable_hierarchy/H4_review_manifest_v1.json'
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (600,)*2)
started = time.process_time()
commands = []
def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
def snapshot():
    manifest=json.loads(MANIFEST.read_text())
    return dict(manifest_sha256=sha(MANIFEST), entries=len(manifest['files']),
                mismatches=[x['path'] for x in manifest['files'] if sha(ROOT/x['path'])!=x['sha256']])
save('hashes_before.json', snapshot())
env=dict(os.environ)
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    env[name]='1'
for name in ('H4_LAW_TEST_SCRATCH','H4_VALIDATION_TEST_SCRATCH'):
    env.pop(name,None)
env.update(PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(EDITION/'code'),TMPDIR=str(OUT))
def cpu_used():
    use=resource.getrusage(resource.RUSAGE_CHILDREN)
    return use.ru_utime+use.ru_stime+time.process_time()-started
def run(name, args, extra=None):
    left=math.floor(600-cpu_used())
    if left<1: raise RuntimeError('aggregate test CPU budget exhausted')
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(min(120,left),)*2)
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,)*2)
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    began=time.monotonic()
    result=subprocess.run(args,cwd=EDITION,env=env|dict(extra or {}),capture_output=True,
                          timeout=min(180,left+20),preexec_fn=limits)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    (OUT/(name+'.log')).write_bytes(result.stdout+result.stderr)
    record=dict(name=name,args=args,cwd=str(EDITION),environment={k:env[k] for k in
        ('PYTHONPATH','PYTHONDONTWRITEBYTECODE','TMPDIR','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')},
        extra_environment=extra,exit_code=result.returncode,wall_seconds=time.monotonic()-began,
        child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        cumulative_child_peak_rss_bytes=after.ru_maxrss*1024,log_sha256=sha(OUT/(name+'.log')))
    commands.append(record)
    save('commands.json',commands)
    print(json.dumps({k:record[k] for k in ('name','exit_code','wall_seconds','child_cpu_seconds')}),flush=True)
    return result

edition_manifest=json.loads((EDITION/'edition_manifest.json').read_text())
mapping=[]
for item in edition_manifest['files']:
    source,destination=ROOT/item['source'],EDITION/item['destination']
    payload=source.read_bytes()
    if item['transform']=='canonical import rename only':
        payload=payload.replace(b'from H4_laws import',b'from pde.observable_laws import')
    elif item['transform'].startswith('append complete'):
        payload=(ROOT/item['destination']).read_bytes().rstrip()+b'\n\n'+payload
    mapping.append(dict(source=item['source'],destination=item['destination'],
        source_hash_matches=sha(source)==item['source_sha256'],
        destination_hash_matches=sha(destination)==item['destination_sha256'],
        transformed_bytes_match=payload==destination.read_bytes()))
save('mapping.json',mapping)
for target in ('docs/README.md','code/scripts/run_observable_validation.py'):
    diff=''.join(difflib.unified_diff((ROOT/target).read_text().splitlines(keepends=True),
        (EDITION/target).read_text().splitlines(keepends=True),fromfile='established/'+target,tofile='candidate/'+target))
    (OUT/(target.replace('/','_')+'.diff')).write_text(diff)

section=(ROOT/'studies/observable_hierarchy/H4_proposed_section.md').read_text()
chapter=(EDITION/'docs/global_nonlinear.md').read_text()
offset=chapter.index(section)
start_line=chapter[:offset].count('\n')+1
tags=re.findall(r'\\tag\{([^}]+)\}',section)
all_tags=re.findall(r'\\tag\{([^}]+)\}',chapter)
old_heading_metadata=[dict(line=i+1,text=line) for i,line in enumerate(chapter.splitlines())
    if line.startswith('#') and ('C.4.7.10.' in line or 'C.4.8.' in line or line.startswith('#### C.5.') or line.startswith('### C.5.'))]
save('markdown_checks.json',dict(section_start_line=start_line,old_heading_metadata=old_heading_metadata,
    unclosed_bold_lines=[dict(section_line=i+1,text=line) for i,line in enumerate(section.splitlines()) if line.startswith('**') and line.count('**')%2],
    new_tags=tags,duplicate_new_tags={tag:all_tags.count(tag) for tag in tags if all_tags.count(tag)!=1},
    section_heading=section.splitlines()[0],section_lines=len(section.splitlines())))

def slug(text):
    text=re.sub(r'<[^>]*>','',text).strip().lower()
    text=re.sub(r'[^\w\- ]','',text)
    return text.replace(' ','-')
link_checks=[]
for rel in ('docs/README.md','code/README.md'):
    path=EDITION/rel
    source_text=path.read_text()
    old_text=(ROOT/rel).read_text()
    old_links=set(re.findall(r'\]\(([^)]+)\)',old_text))
    for link in re.findall(r'\]\(([^)]+)\)',source_text):
        if '://' in link: continue
        target,_,fragment=link.partition('#')
        dest=(path.parent/target).resolve() if target else path
        exists=dest.is_file()
        fragment_ok=None
        if exists and fragment:
            headers=[slug(line.lstrip('#').strip()) for line in dest.read_text().splitlines() if re.match(r'^#{1,6} ',line)]
            fragment_ok=fragment in headers
        link_checks.append(dict(source=rel,target=link,new=link not in old_links,exists_in_edition=exists,fragment_ok=fragment_ok))
save('links.json',link_checks)

guide=(EDITION/'code/README.md').read_text().split('## Observable computation through physical time 40',1)[1]
example=re.search(r'```python\n(.*?)```',guide,re.S).group(1)
(OUT/'public_law_example.txt').write_text(example)
run('public_law_example',[sys.executable,'-B','-c',example])
test_command=[sys.executable,'-B','-m','unittest','discover','-s','code/tests','-p','test_observable*.py','-v']
run('guide_recipe_literal',test_command)
run('suite_with_scratch',test_command,{'H4_LAW_TEST_SCRATCH':str(OUT),'H4_VALIDATION_TEST_SCRATCH':str(OUT)})
for script in ('run_observable_validation.py','validate_observable_horizon.py','analyze_observable_horizon.py'):
    run('help_'+script,[sys.executable,'-B','code/scripts/'+script,'--help'])
run('archive_analysis',[sys.executable,'-B','code/scripts/analyze_observable_horizon.py',
    '--plan','code/validation/observable_horizon_plan.json','--runs',str(ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'),
    '--output',str(OUT/'archive_analysis')])

# Read producer records and exact working observations, not any reviewer report.
import numpy as np
from decimal import Decimal
from fractions import Fraction
plan=json.loads((EDITION/'code/validation/observable_horizon_plan.json').read_text())
producer=[]
exact_checks=[]
for configuration in plan['configurations']:
    folder=ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'/configuration['id']
    record=json.loads((folder/'record.json').read_text())
    producer.append(dict(id=configuration['id'],configuration=record['configuration'],
        configuration_matches=record['configuration']==configuration,plan_hash_matches=record['plan_sha256']==sha(EDITION/'code/validation/observable_horizon_plan.json'),
        status=record['status'],restart_exact=record['restart_exact'],law_metadata=record['law_metadata'],
        source_hashes=record['source_hashes'],producer_sha256=record['producer_sha256'],
        total_seconds=record['total_seconds'],peak_rss_bytes=record['peak_rss_bytes'],
        restart_contract=record['restart_contract'],dimensions=record['dimensions']))
    for item in record['observations']:
        exact=json.loads((folder/item['exact_json']).read_text())
        with np.load(folder/item['npz'],allow_pickle=False) as floating:
            assert set(exact['arrays'])==set(floating.files)
            for name,array in exact['arrays'].items():
                if exact['digits'] is None: values=[float.fromhex(x) for x in array['values']]
                elif exact['backend']=='rational': values=[float(Fraction(int(x,16),10**exact['digits'])) for x in array['values']]
                else: values=[float(Decimal(x)) for x in array['values']]
                expected=np.asarray(values).reshape(array['shape'])
                assert np.array_equal(expected,floating[name]),(configuration['id'],item['time'],name)
        exact_checks.append(dict(id=configuration['id'],time=item['time'],fields=len(exact['arrays']),all_float_views_match=True))
save('producer_records.json',producer)
save('exact_observation_checks.json',exact_checks)
save('hashes_after.json',snapshot())
save('execution_summary.json',dict(cpu_seconds_total=cpu_used(),source_sha256=sha(__file__),
    python=sys.version,numpy=np.__version__,research_trajectories=0,commands=len(commands),
    exact_observations=len(exact_checks),all_source_mappings_match=all(all(x[k] for k in ('source_hash_matches','destination_hash_matches','transformed_bytes_match')) for x in mapping)))
