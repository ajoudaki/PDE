"""Independent frozen-input checks; no evolution call or research trajectory."""
import hashlib
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import resource
import time

import numpy as np
from pde import observable_solver as sol
from pde.observable_arithmetic import Arithmetic
from pde.observable_laws import IntegerExpression as E, OrthogonalArcLaw, DyadicRadius
from scripts import analyze_observable_horizon as analyzer
from scripts import validate_observable_horizon as worker

ROOT = Path('/home/amir/Codes/PDE')
EDITION = ROOT/'data/generated/observable_hierarchy/H4_candidate_v3'
OUT = ROOT/'data/generated/observable_hierarchy/H4_scientific_E_v3'
RUNS = ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text())

def decoded_float(record, digits, backend):
    if digits is None:
        values = [float.fromhex(x) for x in record['values']]
    elif backend == 'rational':
        values = [float(F(int(x,16),10**digits)) for x in record['values']]
    else:
        values = [float(F(x)) for x in record['values']]
    return np.asarray(values).reshape(record['shape'])

started = time.process_time()
result = dict(check='E complete frozen audit', checks=[])
manifest_path = ROOT/'studies/observable_hierarchy/H4_review_manifest_v3.json'
assert sha(manifest_path) == '06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02'
manifest = read(manifest_path)
coverage = []
for entry in manifest['files']:
    path = ROOT/entry['path']
    assert path.stat().st_size == entry['bytes'], entry['path']
    assert sha(path) == entry['sha256'], entry['path']
    coverage.append(dict(**entry, verified=True))
assert len(coverage) == 271
(OUT/'hash_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
edition = read(EDITION/'edition_manifest.json')
for entry in edition['files']:
    assert sha(EDITION/entry['destination']) == entry['destination_sha256']
candidate = (ROOT/'studies/observable_hierarchy/H4_proposed_section_v2.md').read_bytes()
chapter = (EDITION/'docs/global_nonlinear.md').read_bytes()
insertion = b'\n\n'+candidate.rstrip()
assert chapter.count(insertion) == 1
old_chapter = chapter.replace(insertion,b'',1)
assert hashlib.sha256(old_chapter).hexdigest() == '77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932'
dependencies = read(ROOT/'studies/observable_hierarchy/H4_dependency_manifest.json')
for entry in dependencies['units']:
    source = old_chapter if entry['source']=='docs/global_nonlinear.md' else (EDITION/entry['source']).read_bytes()
    assert hashlib.sha256(source).hexdigest() == entry['source_sha256']
    excerpt = b''.join(source.splitlines(keepends=True)[entry['first_line']-1:entry['last_line']])
    assert hashlib.sha256(excerpt).hexdigest() == entry['excerpt_sha256']
    assert excerpt in (ROOT/'studies/observable_hierarchy/H4_dependencies.md').read_bytes()
result['checks'].append('271 hashes, all edition destinations, exact insertion and all nine source excerpt hashes')

planpath = EDITION/'code/validation/observable_horizon_plan.json'
plan = read(planpath)
supervisor = read(RUNS/'supervisor.json')
assert supervisor['status']=='operational_pass'
assert supervisor['plan_sha256']==sha(planpath)
assert supervisor['worker_sha256']==sha(EDITION/'code/scripts/validate_observable_horizon.py')
assert supervisor['supervisor_sha256']==sha(EDITION/'code/scripts/run_observable_validation.py')
assert len(supervisor['configurations'])==14
assert sum(x['cpu_seconds'] for x in supervisor['configurations']) == supervisor['total_cpu_seconds']
all_rows=[]
scalar_count=0
for config, supervision in zip(plan['configurations'],supervisor['configurations']):
    folder = RUNS/config['id']
    record = read(folder/'record.json')
    assert config == record['configuration']
    assert record['id']==supervision['id']==config['id']
    assert record['status']==supervision['status']=='operational_pass'
    assert supervision['record_sha256']==sha(folder/'record.json')
    assert record['plan_sha256']==sha(planpath)
    assert record['producer_sha256']==sha(EDITION/'code/scripts/validate_observable_horizon.py')
    for name, expected in record['source_hashes'].items():
        assert sha(EDITION/'code/pde'/name)==expected
    assert set(record['thread_environment'].values())=={'1'}
    assert record['restart_exact'] and all(record['restart_comparison'].values())
    assert record['frozen_signature_initial']==record['frozen_signature_final']
    for name, expected in record['outputs'].items():
        assert sha(folder/name)==expected
    # Read and reconcile the complete supervisor worker log, without executing it.
    log=read(RUNS/(config['id']+'.log'))
    assert log['status']==record['status'] and log['total_seconds']==record['total_seconds']
    assert log['peak_rss_bytes']==record['peak_rss_bytes']
    assert record['total_seconds']['cpu']<=plan['budget']['cpu_seconds_per_configuration']
    assert record['peak_rss_bytes']<=plan['budget']['rss_bytes_per_process']
    assert record['restart_contract']['steps_before']+record['restart_contract']['steps_after']==config['steps']
    assert F(record['restart_contract']['step_size'])*config['steps']==40
    law,limits=worker.build_law(plan,config)
    static_rule=law.quadrature(config['nodes_per_arc'],Arithmetic(config['digits'],config['backend']),limits=limits)
    assert static_rule.metadata==record['law_metadata']
    panels={}
    exact_count=0
    for item in record['observations']:
        exact=read(folder/item['exact_json'])
        assert exact['format']==worker.OBSERVATION_FORMAT
        assert exact['time']==item['time']
        assert (exact['digits'],exact['backend'])==(config['digits'],config['backend'])
        with np.load(folder/item['npz'],allow_pickle=False) as archive:
            assert set(archive.files)==set(exact['arrays'])
            arrays={key:archive[key].copy() for key in archive.files}
        for key,encoded in exact['arrays'].items():
            values=decoded_float(encoded,exact['digits'],exact['backend'])
            np.testing.assert_array_equal(values,arrays[key])
            scalar_count+=values.size
            exact_count+=values.size
        for layer in ('first','second'):
            pair=arrays[layer+'_pairs']
            motion=arrays[layer+'_weights']@((pair[:,:,1]-pair[:,:,0])**2)@arrays['input_weights']
            name='rms1' if layer=='first' else 'rms2'
            assert abs(float(motion)-float(arrays[name])**2)<2e-14
            assert abs(float(arrays[name])-item[name])<1e-15
            assert np.max(np.abs(pair))<=1+1e-15
        loss=arrays['input_weights']@((arrays['training_prediction']-arrays['labels'])**2)
        assert abs(loss-float(arrays['loss']))<2e-14
        assert abs(float(arrays['loss'])-item['loss'])<1e-15
        if F(item['time'])==0:
            assert float(arrays['rms1'])==float(arrays['rms2'])==0
        panels[item['time']]=(exact,arrays)
    endpoint_checks=[]
    for restart_name,instant in [('midpoint_restart.json','20'),('final_restart.json','40')]:
        raw=read(folder/restart_name)
        for group in ('state','data'):
            for encoded in raw[group].values():
                converted=decoded_float(encoded,raw['digits'],raw['backend'])
                assert np.isfinite(converted).all()
                scalar_count+=converted.size
        state,data=sol.load_restart(folder/restart_name)
        assert worker.frozen_signature(state,data)==record['frozen_signature_final']
        assert data.metadata==static_rule.metadata
        for key in worker.DATA_KEYS:
            assert worker.encode_array(getattr(data,key),state.arithmetic)==worker.encode_array(getattr(static_rule,key),state.arithmetic)
        exact,arrays=panels[instant]
        # Pure observation from a frozen saved state, zero evolution calls.
        circle=sol.circle_inputs(plan['common']['circle_directions'],state.arithmetic)
        observed=worker.collect_observation(state,data,circle,block_size=plan['common']['block_size'])
        assert {k:worker.encode_array(v,state.arithmetic) for k,v in observed.items()}==exact['arrays']
        assert sum(getattr(state,k).size for k in worker.STATE_KEYS)==record['workspace_final']['state_scalars']
        if instant=='40':
            assert sol.state_bytes(state)==record['state_bytes_final']
            assert worker.workspace_accounting(state,data,plan['common']['block_size'])==record['workspace_final']
        endpoint_checks.append(dict(time=instant,all_exact=True))
    all_rows.append(dict(id=config['id'],status='pass',observations=6,exact_observation_scalars=exact_count,
                         endpoint_checks=endpoint_checks,loss40=float(panels['40'][1]['loss']),
                         cpu=record['total_seconds']['cpu'],rss=record['peak_rss_bytes'],
                         collapsed=record['law_metadata']['collapsed_to_reference']))
result['artifact_checks']=all_rows
result['all_decoded_scalar_count']=scalar_count
result['checks'].append('All 14 records/logs, 84 complete JSON/NPZ observations, 28 complete restarts; both saved endpoint observations exact')
fresh=analyzer.analyze(planpath,RUNS)
stored=read(ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.json')
stored.pop('analysis_cpu_seconds')
assert fresh==stored
assert analyzer.markdown(fresh)==(ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.md').read_text()
result['aggregate']=fresh['aggregate']
result['comparisons']=[dict(left=x['left'],right=x['right'],maximum=x['maximum_over_saved_times_and_panel']) for x in fresh['comparisons']]
result['checks'].append('Full independent analysis JSON/Markdown recomputation, all 12 comparable pairs, all resource records')

# Manufactured unequal populations, nonunit literal masses within API tolerance.
ar=Arithmetic()
state=sol.State(np.array([[1.,.2],[1.,-.4],[.7,.9]]),np.array([[.1,.2],[-.3,.5],[.8,-.2]]),
                np.array([[.2,.1],[-.2,.7],[.6,-.1]]),np.array([.2,.3,.5])*(1+1e-12),
                np.array([[1.,-.3],[.4,.8]]),np.array([.2,-.1]),np.array([.4,.6])*(1-1e-12),
                np.array([[.3,-.2],[.1,.5]]),np.array([[.2,-.1],[.05,.3]]),ar).validate()
data=sol.DataLaw(np.array([[1.,0.],[.6,.8],[0.,1.]]),np.array([1.,-1.,1.]),np.array([.25,.35,.4])*(1+1e-12)).validate(ar)
before=[x.copy() for x in (state.p1,state.p2,data.probabilities)]
velocity=sol.rhs(state,data,block_size=2)
errors=[]
for block,v in zip(('w','c','M'),velocity):
    for index in np.ndindex(v.shape):
        plus,minus=state.copy(),state.copy()
        getattr(plus,block)[index]+=1e-6
        getattr(minus,block)[index]-=1e-6
        derivative=(sol.loss(plus,data)-sol.loss(minus,data))/2e-6
        metric=state.p1[index[0]] if block=='w' else state.p2[index[0]] if block=='c' else 1
        errors.append(abs(derivative+metric*v[index]))
assert max(errors)<3e-10
for x,y in zip(before,(state.p1,state.p2,data.probabilities)):
    np.testing.assert_array_equal(x,y)
x=np.array([.1,.7,-.4]); y=np.array([.8,-.3])
forward=state.b2@state.M@(state.b1.T@(state.p1*x))
reverse=state.b1@state.M.T@(state.b2.T@(state.p2*y))
assert abs(state.p2@(y*forward)-state.p1@(x*reverse))<1e-15
good=sol.paired_observations(state,data)
bad=state.copy(); bad.g=bad.g[::-1].copy()
changed=sol.paired_observations(bad,data)
assert abs(float(good['rms1'])-float(changed['rms1']))>1e-3
assert abs(float(good['rms2'])-float(changed['rms2']))>1e-3
result['gradient_max_absolute_error']=max(errors)
result['checks'].append('Every manufactured w/c/M gradient entry, literal mass retention, adjoint duality, paired-mark permutation detection')
for s,t,r in itertools.product([F(-1),F(-2,7),F(0),F(3,5),F(1)],repeat=3):
    def u(z): return ((1-z*z)/(1+z*z),2*z/(1+z*z))
    difference=sum((a-b)**2 for a,b in zip(u(r*s),u(r*t)))
    assert difference==4*r*r*(s-t)**2/((1+r*r*s*s)*(1+r*r*t*t))
for digits in (20,24,36,80):
    cutoff=4*(digits+8)+2
    for exponent in (cutoff-1,cutoff,cutoff+1):
        rule=OrthogonalArcLaw(DyadicRadius(E.integer(exponent))).quadrature(2,Arithmetic(digits,'rational'))
        assert rule.metadata['radius_replaced_by_zero']==(exponent>cutoff)
result['checks'].append('125 exact chord identities and 12 exact cutoff boundary tests')
result['cpu_seconds']=time.process_time()-started
result['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
result['status']='pass'
(OUT/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
