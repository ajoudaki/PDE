import hashlib,json,math,resource,sys,time
from fractions import Fraction
from decimal import Decimal
from pathlib import Path
import numpy as np
from scripts import analyze_observable_horizon as analyzer
from pde import observable_solver as solver
from pde.observable_arithmetic import Arithmetic
from pde.observable_laws import OrthogonalArcLaw
from pde.observable_fixed import Fixed

ROOT=Path('/home/amir/Codes/PDE'); HERE=Path(__file__).resolve().parent
ED=ROOT/'data/generated/observable_hierarchy/H4_candidate_v1'
RUNS=ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'
PLAN=ED/'code/validation/observable_horizon_plan.json'
started=time.process_time()
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def forbidden(*a,**k): raise AssertionError('No initialization or trajectory is allowed in archive audit')
solver.initialize=solver.evolve=solver.rhs=forbidden
manifest=json.loads((ROOT/'studies/observable_hierarchy/H4_review_manifest_v1.json').read_text())
inventory=[]
for e in manifest['files']:
    p=ROOT/e['path']; b=p.read_bytes()
    assert digest(p)==e['sha256'] and len(b)==e['bytes'],p
    inventory.append(dict(path=e['path'],sha256=e['sha256'],bytes=len(b),lines=b.count(b'\n')))
(HERE/'verified_inputs.json').write_text(json.dumps(inventory,indent=2)+'\n')
edition=json.loads((ED/'edition_manifest.json').read_text())
for e in edition['files']: assert digest(ED/e['destination'])==e['destination_sha256']
proposal=(ROOT/'studies/observable_hierarchy/H4_proposed_section.md').read_bytes()
chapter=(ED/'docs/global_nonlinear.md').read_bytes()
assert chapter.endswith(b'\n\n'+proposal)
oldchapter=chapter[:-len(proposal)-2]+b'\n'
assert hashlib.sha256(oldchapter).hexdigest()=='77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932'
codeguide=(ROOT/'studies/observable_hierarchy/H4_code_guide.md').read_bytes()
assert (ED/'code/README.md').read_bytes().endswith(b'\n\n'+codeguide)
assert (ED/'docs/README.md').read_bytes()==(ROOT/'studies/observable_hierarchy/H4_docs_readme.md').read_bytes()
dependencies=(ROOT/'studies/observable_hierarchy/H4_dependencies.md').read_bytes()
depmanifest=json.loads((ROOT/'studies/observable_hierarchy/H4_dependency_manifest.json').read_text())
for unit in depmanifest['units']:
    source=oldchapter if unit['source']=='docs/global_nonlinear.md' else (ED/unit['source']).read_bytes()
    assert hashlib.sha256(source).hexdigest()==unit['source_sha256']
    excerpt=b''.join(source.splitlines(keepends=True)[unit['first_line']-1:unit['last_line']])
    assert hashlib.sha256(excerpt).hexdigest()==unit['excerpt_sha256']
    assert excerpt.rstrip() in dependencies
certificate=(ROOT/'data/generated/observable_hierarchy/H4_full_tests_v1/reference_certificate.py').read_bytes()
assert certificate.rstrip() in dependencies

plan=json.loads(PLAN.read_text()); parent=json.loads((RUNS/'supervisor.json').read_text())
records=[]; panels={}; exact_scalars=checkpoint_scalars=0; maximum_discrepancy=0.0
for config,parentrow in zip(plan['configurations'],parent['configurations']):
    name=config['id']; folder=RUNS/name; record=json.loads((folder/'record.json').read_text())
    assert record['configuration']==config and record['id']==name and parentrow['id']==name
    assert record['plan_sha256']==digest(PLAN)==parent['plan_sha256']
    assert record['plan_version']==plan['version'] and record['status']==parentrow['status']=='operational_pass'
    assert parentrow['record_sha256']==digest(folder/'record.json')
    assert set(record['thread_environment'].values())=={'1'}
    for filename,value in record['source_hashes'].items(): assert digest(ED/'code/pde'/filename)==value
    assert record['producer_sha256']==digest(ED/'code/scripts/validate_observable_horizon.py')
    for filename,value in record['outputs'].items(): assert digest(folder/filename)==value
    log=json.loads((RUNS/(name+'.log')).read_text())
    for key in ('id','status','total_seconds','peak_rss_bytes'): assert log[key]==record[key]
    assert record['restart_exact'] and record['restart_prediction_exact'] and all(record['restart_comparison'].values())
    assert record['frozen_signature_initial']==record['frozen_signature_final']
    assert Fraction(record['restart_contract']['step_size'])*config['steps']==40
    assert record['restart_contract']['steps_before']+record['restart_contract']['steps_after']==config['steps']
    assert Fraction(record['restart_contract']['step_size'])*record['restart_contract']['steps_before']==20
    snapshots={}; midjson=finaljson=None
    for checkpoint,instant in [('midpoint_restart.json','20'),('final_restart.json','40')]:
        raw=json.loads((folder/checkpoint).read_text())
        state,data=solver.load_restart(folder/checkpoint)
        checkpoint_scalars+=sum(v.size for v in [getattr(state,k) for k in ('b1','g','w','p1','b2','c','p2','M','D')]+[data.inputs,data.labels,data.probabilities])
        if instant=='20': midjson=raw
        else: finaljson=raw
        assert state.metadata==record['initialization_metadata'] and data.metadata==record['law_metadata']
        assert raw['digits']==config['digits'] and raw['backend']==config['backend']
        assert OrthogonalArcLaw.from_description(data.metadata['exact_law']).exact_description()==data.metadata['exact_law']
        if instant=='40':
            assert solver.state_bytes(state)==record['state_bytes_final']
            d=record['dimensions']; P1,P2,d1,d2,A=(d[k] for k in ('first_nodes','second_nodes','first_features','second_features','input_nodes'))
            assert P1*(d1+5)+P2*(d2+2)+2*d1*d2==record['workspace_final']['state_scalars']
            assert record['workspace_final']['data_scalars']==4*A
        snapshots[instant]=(state,data)
    for key in ('b1','g','p1','b2','p2','D'): assert midjson['state'][key]==finaljson['state'][key]
    assert midjson['data']==finaljson['data'] and midjson['metadata']==finaljson['metadata'] and midjson['data_metadata']==finaljson['data_metadata']
    runpanels={}; checks=[]
    for item in record['observations']:
        exact=json.loads((folder/item['exact_json']).read_text())
        assert exact['time']==item['time'] and exact['digits']==config['digits'] and exact['backend']==config['backend']
        ar=Arithmetic(exact['digits'],exact['backend'])
        arrays={}
        for key,value in exact['arrays'].items():
            assert math.prod(value['shape'])==len(value['values'])
            if ar.digits is None: decoded=[float.fromhex(x) for x in value['values']]
            elif ar.backend=='rational': decoded=[Fixed.from_units(int(x,16),ar.digits) for x in value['values']]
            else: decoded=[Decimal(x) for x in value['values']]
            array=np.asarray(decoded,dtype=ar.dtype).reshape(value['shape'])
            assert ar.finite(array)
            arrays[key]=array;exact_scalars+=array.size
        with np.load(folder/item['npz'],allow_pickle=False) as npz:
            assert set(npz.files)==set(arrays)
            for key,value in arrays.items():
                floating=np.asarray(value,dtype=float)
                assert npz[key].shape==floating.shape
                assert npz[key].tobytes()==floating.tobytes(),(name,item['time'],key)
        floating={k:np.asarray(v,float) for k,v in arrays.items()}
        q=floating['input_weights']; errors={}
        risk=float(np.sum(q*(floating['training_prediction']-floating['labels'])**2))
        errors['loss']=max(abs(risk-item['loss']),abs(risk-float(floating['loss'])))
        for ell,prefix in [(1,'first'),(2,'second')]:
            pairs=floating[prefix+'_pairs']; pw=floating[prefix+'_weights']
            squared=float(np.sum((pw[:,None]*q[None,:])*(pairs[:,:,1]-pairs[:,:,0])**2))
            errors['rms'+str(ell)]=max(abs(math.sqrt(squared)-item['rms'+str(ell)]),abs(math.sqrt(squared)-float(floating['rms'+str(ell)])))
            assert np.max(np.abs(pairs))<=1+1e-14
        assert max(errors.values())<2e-11
        maximum_discrepancy=max(maximum_discrepancy,*errors.values())
        if item['time']=='0':
            assert risk==1 and item['rms1']==item['rms2']==0
            assert np.array_equal(floating['first_pairs'][:,:,0],floating['first_pairs'][:,:,1])
            assert np.array_equal(floating['second_pairs'][:,:,0],floating['second_pairs'][:,:,1])
        if item['time'] in snapshots:
            state,data=snapshots[item['time']]
            # Direct independent formulas from the saved arrays: no source program or step.
            b1,b2,w,g,c,M,D,p1,p2=(np.asarray(getattr(state,k),float) for k in ('b1','b2','w','g','c','M','D','p1','p2'))
            inputs=np.asarray(data.inputs,float)
            initial1=np.tanh(g@inputs.T); current1=np.tanh(w@inputs.T)
            initial2=np.tanh(b2@D@(b1.T@(p1[:,None]*initial1)))
            current2=np.tanh(b2@M@(b1.T@(p1[:,None]*current1)))
            for prefix,initial,current in [('first',initial1,current1),('second',initial2,current2)]:
                assert np.max(np.abs(floating[prefix+'_pairs']-np.stack([initial,current],axis=-1)))<2e-12
            query=floating['circle']; h1=np.tanh(w@query.T)
            prediction=p2@(c[:,None]*np.tanh(b2@M@(b1.T@(p1[:,None]*h1))))
            assert np.max(np.abs(prediction-floating['prediction']))<2e-12
        checks.append(dict(time=item['time'],loss=risk,rms1=item['rms1'],rms2=item['rms2'],algebra_errors=errors))
        runpanels[item['time']]=floating
    panels[name]=runpanels
    # Preserve complete non-array metadata for the review evidence, with all fields parsed above.
    records.append(dict(id=name,record_keys=sorted(record),configuration=config,dimensions=record['dimensions'],law_metadata=record['law_metadata'],initialization_metadata=record['initialization_metadata'],conditioning_diagnostics=record['conditioning_diagnostics'],workspace_initial=record['workspace_initial'],workspace_final=record['workspace_final'],state_bytes_initial=record['state_bytes_initial'],state_bytes_final=record['state_bytes_final'],data_bytes=record['data_bytes'],dynamic_changes=record['dynamic_changes'],timings={k:v for k,v in record.items() if k.endswith('_seconds')},peak_rss_bytes=record['peak_rss_bytes'],observations=checks))
    print(json.dumps(dict(id=name,dimensions=record['dimensions'],collapsed=record['law_metadata']['collapsed_to_reference'],times=checks,cpu=record['total_seconds']['cpu'],rss=record['peak_rss_bytes'],state_scalars=record['workspace_final']['state_scalars'],condition=[record['conditioning_diagnostics']['population_'+k]['condition_2'] for k in ('1','2')])),flush=True)
fresh=analyzer.analyze(PLAN,RUNS)
saved=json.loads((ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.json').read_text())
saved.pop('analysis_cpu_seconds')
assert fresh==saved,'Full saved analysis JSON differs from read-only recomputation'
assert analyzer.markdown(fresh)==(ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.md').read_text()
(HERE/'regenerated_summary.json').write_text(json.dumps(fresh,indent=2)+'\n')
(HERE/'regenerated_summary.md').write_text(analyzer.markdown(fresh))
(HERE/'complete_record_audit.json').write_text(json.dumps(records,indent=2)+'\n')
result=dict(status='pass',files_hashed=len(inventory),dependency_units_verified=len(depmanifest['units']),runs=len(records),observations=sum(len(r['observations']) for r in records),exact_observation_scalars_decoded=exact_scalars,checkpoint_scalars_decoded=checkpoint_scalars,maximum_algebra_discrepancy=maximum_discrepancy,summary_all_fields_equal=True,summary_markdown_byte_equal=True,aggregate=fresh['aggregate'],comparisons=fresh['comparisons'],cpu_seconds=time.process_time()-started,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
(HERE/'archive_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='comparisons'}),flush=True)
