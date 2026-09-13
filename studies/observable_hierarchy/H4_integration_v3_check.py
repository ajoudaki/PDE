"""Independent H4 v3 integration checks; no research trajectories or Git writes.

Predeclared ceiling: 600 cumulative CPU seconds, 4 GiB, one numerical thread.
The test subprocess receives 420 CPU seconds; checks and analysis receive 120.
All generated outputs stay in the review-owned scratch directory.
"""
from pathlib import Path
import hashlib
import json
import os
import resource
import subprocess
import sys
import time

ROOT = Path('/home/amir/Codes/PDE')
EDITION = ROOT / 'data/generated/observable_hierarchy/H4_candidate_v3'
SCRATCH = ROOT / 'data/generated/observable_hierarchy/H4_integration_v3'
MANIFEST = ROOT / 'studies/observable_hierarchy/H4_review_manifest_v3.json'
THREADS = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'BLIS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (420, 420))
    resource.setrlimit(resource.RLIMIT_AS, (4*1024**3, 4*1024**3))


def run(name, command, *, cwd=EDITION):
    env = dict(os.environ)
    env.update({key: '1' for key in THREADS})
    env.update(PYTHONPATH=str(EDITION/'code'), PYTHONDONTWRITEBYTECODE='1',
               H4_LAW_TEST_SCRATCH=str(SCRATCH/'tests'),
               H4_VALIDATION_TEST_SCRATCH=str(SCRATCH/'tests'),
               TMPDIR=str(SCRATCH/'tests'), OMP_DYNAMIC='FALSE', MKL_DYNAMIC='FALSE')
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with (SCRATCH/(name+'.log')).open('w') as stream:
        completed = subprocess.run(command, cwd=cwd, env=env, stdout=stream,
                                   stderr=subprocess.STDOUT, timeout=540,
                                   preexec_fn=limits)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    row = dict(name=name, command=command, cwd=str(cwd), returncode=completed.returncode,
               wall_seconds=time.monotonic()-start,
               cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
               peak_rss_bytes=after.ru_maxrss*1024,
               environment={key: env[key] for key in (*THREADS, 'PYTHONPATH', 'PYTHONDONTWRITEBYTECODE',
                                                      'H4_LAW_TEST_SCRATCH','H4_VALIDATION_TEST_SCRATCH','TMPDIR')})
    (SCRATCH/(name+'.json')).write_text(json.dumps(row, indent=2)+'\n')
    print(json.dumps(row), flush=True)
    return row


def hashes():
    manifest=json.loads(MANIFEST.read_text())
    assert digest(MANIFEST)=='06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02'
    rows=[]
    for row in manifest['files']:
        p=ROOT/row['path']
        assert digest(p)==row['sha256'] and p.stat().st_size==row['bytes'], str(p)
        rows.append(row)
    edition=json.loads((EDITION/'edition_manifest.json').read_text())
    correspondence=[]
    for row in edition['files']:
        data=(EDITION/row['destination']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==row['destination_sha256']
        if row['transform']=='identity':
            assert row['source_sha256']==row['destination_sha256']
        elif row['transform']=='canonical import rename only':
            original=data.replace(b'from pde.observable_laws import',b'from H4_laws import')
            assert hashlib.sha256(original).hexdigest()==row['source_sha256']
        elif row['kind']=='insert after C.4.7.10':
            original=(ROOT/row['source']).read_bytes()
            insertion=b'\n\n'+original.rstrip()
            assert data.count(insertion)==1
            baseline=data.replace(insertion,b'',1)
            assert hashlib.sha256(baseline).hexdigest()=='77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932'
            assert data.index(insertion)>data.index(b'##### C.4.7.10.')
            assert data.index(insertion)<data.index(b'#### C.4.8.')
        correspondence.append(row)
    result=dict(manifest_sha256=digest(MANIFEST), files_verified=len(rows),
                edition_sha256=digest(EDITION/'edition_manifest.json'),
                correspondence=correspondence)
    (SCRATCH/'hashes.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Verified',len(rows),'frozen files and',len(correspondence),'edition destinations.')


if __name__=='__main__':
    SCRATCH.mkdir(parents=True,exist_ok=True)
    (SCRATCH/'tests').mkdir(exist_ok=True)
    hashes()
    if sys.argv[1:] == ['tests']:
        run('deterministic_tests',[sys.executable,'-B','-m','unittest','discover','-s','code/tests','-p','test_observable*.py','-v'])
