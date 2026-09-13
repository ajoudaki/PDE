"""Read-only archive/interface checks for the frozen H4 v3 integration review."""
from pathlib import Path
from decimal import Decimal
from fractions import Fraction
import ast
import hashlib
import json
import re
import sys
import time
from urllib.parse import unquote

import numpy as np

ROOT=Path('/home/amir/Codes/PDE')
EDITION=ROOT/'data/generated/observable_hierarchy/H4_candidate_v3'
SCRATCH=ROOT/'data/generated/observable_hierarchy/H4_integration_v3'
RUNS=ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'
sys.path.insert(0,str(EDITION/'code'))
from pde.observable_arithmetic import Arithmetic
from pde.observable_laws import supported_law, OrthogonalArcLaw
from scripts import analyze_observable_horizon as analyzer
from scripts import validate_observable_horizon as worker
from pde import observable_solver as solver
from pde.observable_fixed import Fixed


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def public_example():
    law=supported_law(a='-1',b='1',c='-1/2',d='1')
    description=law.exact_description()
    assert OrthogonalArcLaw.from_description(description).exact_description()==description
    data=law.quadrature(8,Arithmetic())
    assert len(data.labels)==16
    assert data.metadata['radius_replaced_by_zero']
    return dict(nodes=len(data.labels),scope=data.metadata['scientific_scope'],
                exact_description=description,collapse=data.metadata['collapse_reason'])


def archives():
    plan_path=EDITION/'code/validation/observable_horizon_plan.json'
    summary=analyzer.analyze(plan_path,RUNS)
    old=json.loads((ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.json').read_text())
    for key in ('aggregate','comparisons','runs','problems','supervisor'):
        assert summary.get(key)==old.get(key),key
    checked=[]
    checkpoint_checks=[]
    plan=json.loads(plan_path.read_text())
    for row in summary['runs']:
        record=json.loads((RUNS/row['id']/'record.json').read_text())
        for name,sha in record['source_hashes'].items():
            assert digest(EDITION/'code/pde'/name)==sha,(row['id'],name)
        assert record['producer_sha256']==digest(EDITION/'code/scripts/validate_observable_horizon.py')
        assert record['frozen_signature_initial']==record['frozen_signature_final']
        assert all(record['restart_comparison'].values()) and record['restart_prediction_exact']
        assert set(record['thread_environment'].values())=={'1'}
        for item in record['observations']:
            folder=RUNS/row['id']
            exact=json.loads((folder/item['exact_json']).read_text())
            assert exact['time']==item['time']
            assert exact['format']=='observable-horizon-observations-v1'
            def decode(x):
                if exact['digits'] is None:
                    return float.fromhex(x)
                if exact['backend']=='rational':
                    return float(Fraction(int(x,16),10**exact['digits']))
                return float(Decimal(x))
            with np.load(folder/item['npz'],allow_pickle=False) as floating:
                assert set(exact['arrays'])==set(floating.files)
                for key,value in exact['arrays'].items():
                    arr=np.asarray([decode(x) for x in value['values']],float).reshape(value['shape'])
                    assert np.array_equal(arr,floating[key]),(row['id'],item['time'],key)
            checked.append(dict(id=row['id'],time=item['time'],exact_sha256=digest(folder/item['exact_json'])))
        for checkpoint in ('midpoint_restart.json','final_restart.json'):
            state,data=solver.load_restart(RUNS/row['id']/checkpoint)
            assert worker.frozen_signature(state,data)==record['frozen_signature_initial']
            workspace=worker.workspace_accounting(state,data,plan['common']['block_size'])
            assert workspace['state_scalars']==row['state_scalars']
            assert workspace['data_scalars']==row['data_scalars']
            law,limits=worker.build_law(plan,record['configuration'])
            expected=law.quadrature(record['configuration']['nodes_per_arc'],state.arithmetic,limits=limits,
                                    allow_collapse=plan['common']['allow_radius_collapse'])
            assert expected.metadata==data.metadata
            for key in worker.DATA_KEYS:
                assert worker.encode_array(getattr(data,key),state.arithmetic)==worker.encode_array(getattr(expected,key),state.arithmetic)
            if checkpoint=='final_restart.json':
                exact=json.loads((RUNS/row['id']/record['observations'][-1]['exact_json']).read_text())
                circle_record=exact['arrays']['circle']
                ar=state.arithmetic
                if ar.digits is None:
                    circle_values=[float.fromhex(x) for x in circle_record['values']]
                elif ar.backend=='rational':
                    circle_values=[Fixed.from_units(int(x,16),ar.digits) for x in circle_record['values']]
                else:
                    circle_values=[Decimal(x) for x in circle_record['values']]
                circle=np.asarray(circle_values,dtype=ar.dtype).reshape(circle_record['shape'])
                observations=worker.collect_observation(state,data,circle,block_size=plan['common']['block_size'])
                for key,values in observations.items():
                    assert worker.encode_array(values,ar)==exact['arrays'][key],(row['id'],key)
                assert solver.state_bytes(state)==record['state_bytes_final']
            checkpoint_checks.append(dict(id=row['id'],checkpoint=checkpoint,sha256=digest(RUNS/row['id']/checkpoint)))
    return dict(aggregate=summary['aggregate'],comparisons=summary['comparisons'],
                problems=summary['problems'],exact_archive_count=len(checked),checked=checked,
                checkpoint_checks=checkpoint_checks,final_observations_recomputed_exactly=14,
                source_hashes_all_match_edition=True,stored_analysis_recomputed_identically=True)


def structure():
    section=(ROOT/'studies/observable_hierarchy/H4_proposed_section_v2.md').read_text()
    chapter=(EDITION/'docs/global_nonlinear.md').read_text()
    append=(ROOT/'studies/observable_hierarchy/H4_code_guide_v2.md').read_text()
    code=(EDITION/'code/README.md').read_text()
    assert code.endswith(append)
    assert chapter.count(section.rstrip())==1
    tags=re.findall(r'\\tag\{(H40\.[^}]+)\}',section)
    assert len(tags)==len(set(tags))
    assert all(chapter.count('\\tag{'+tag+'}')==1 for tag in tags)
    guide_files=[EDITION/'docs/README.md',EDITION/'code/README.md',EDITION/'docs/NOTATION.md']
    links=[]
    for p in guide_files:
        data=p.read_text()
        assert len(re.findall(r'^```',data,re.M))%2==0,str(p)
        for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',data):
            if '://' in target:
                continue
            filename,_,fragment=target.partition('#')
            q=p.parent/unquote(filename)
            row=dict(source=str(p.relative_to(EDITION)),label=label,target=target,file_present=q.is_file())
            if q.is_file() and fragment:
                headings=[]
                # GitHub-style basic heading normalization, adequate for the
                # actual ASCII chapter headings referenced by these guides.
                for line in q.read_text().splitlines():
                    if re.match(r'^#{1,6} ',line):
                        heading=re.sub(r'^#+\s*','',line).lower()
                        headings.append(re.sub(r'[^\w\- ]','',heading).replace(' ','-'))
                row['fragment_present']=unquote(fragment) in headings
            links.append(row)
    imports=[]
    for p in (EDITION/'code').rglob('*.py'):
        tree=ast.parse(p.read_text())
        for node in ast.walk(tree):
            if isinstance(node,ast.ImportFrom) and node.module:
                assert not node.module.startswith(('studies','H4_')),(str(p),node.module)
        imports.append(dict(path=str(p.relative_to(EDITION)),sha256=digest(p)))
    return dict(unique_new_equation_tags=len(tags),new_heading_lines=[l for l in section.splitlines() if l.startswith('#')],
                chapter_insertion_exact=True,code_guide_append_exact=True,balanced_guide_fences=True,
                links=links,parsed_python=imports)


if __name__=='__main__':
    start=time.process_time()
    result=dict(public_law_example=public_example(),archives=archives(),structure=structure())
    result['cpu_seconds']=time.process_time()-start
    (SCRATCH/'interface_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(cpu_seconds=result['cpu_seconds'],public_example_nodes=result['public_law_example']['nodes'],
                         archives=result['archives']['exact_archive_count'],aggregate=result['archives']['aggregate'],
                         tags=result['structure']['unique_new_equation_tags'],
                         missing_files=[r for r in result['structure']['links'] if not r['file_present']],
                         missing_fragments=[r for r in result['structure']['links'] if r.get('fragment_present') is False]),indent=2))
