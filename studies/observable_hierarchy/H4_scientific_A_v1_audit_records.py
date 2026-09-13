"""Independent static inspection of every frozen empirical value; no evolution."""
from collections import Counter
from decimal import Decimal
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from pde import observable_solver as solver
from pde.observable_fixed import Fixed
from scripts import validate_observable_horizon as producer

ROOT = Path('/home/amir/Codes/PDE')
OUT = ROOT/'data/generated/observable_hierarchy/H4_scientific_A_v1'
EDITION = ROOT/'data/generated/observable_hierarchy/H4_candidate_v1'
RUNS = ROOT/'data/generated/observable_hierarchy/H4_author_runs_v1'
manifest_path = ROOT/'studies/observable_hierarchy/H4_review_manifest_v1.json'
manifest = json.loads(manifest_path.read_text())
assert hashlib.sha256(manifest_path.read_bytes()).hexdigest() == '8b5808b02fb14e6f134b3c188cdd540aff09b557213779e716fbd011217c5648'
def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
hashes = []
for f in manifest['files']:
    p = ROOT/f['path']
    b = p.read_bytes()
    assert len(b) == f['bytes'] and hashlib.sha256(b).hexdigest() == f['sha256'], str(p)
    hashes.append(dict(path=f['path'], sha256=f['sha256'], bytes=len(b)))

counts = Counter()
def visit(value):
    counts[type(value).__name__] += 1
    if isinstance(value, dict):
        assert all(isinstance(k,str) for k in value)
        for item in value.values(): visit(item)
    elif isinstance(value, list):
        for item in value: visit(item)
    elif isinstance(value, float): assert np.isfinite(value)
    else: assert value is None or isinstance(value,(str,int,bool))

plan_path = EDITION/'code/validation/observable_horizon_plan.json'
plan = json.loads(plan_path.read_text())
supervisor = json.loads((RUNS/'supervisor.json').read_text())
visit(supervisor)
assert supervisor['plan_sha256'] == digest(plan_path)
assert supervisor['supervisor_sha256'] == digest(EDITION/'code/scripts/run_observable_validation.py')
assert supervisor['worker_sha256'] == digest(EDITION/'code/scripts/validate_observable_horizon.py')
assert supervisor['status'] == 'operational_pass'
assert supervisor['budget'] == plan['budget']
assert [x['id'] for x in supervisor['configurations']] == [x['id'] for x in plan['configurations']]

def decode(item, digits, backend):
    if digits is None: values = [float.fromhex(x) for x in item['values']]
    elif backend == 'rational': values = [Fixed.from_units(int(x,16),digits) for x in item['values']]
    else: values = [Decimal(x) for x in item['values']]
    assert np.prod(item['shape'],dtype=int) == len(values)
    return np.asarray(values,dtype=float if digits is None else object).reshape(item['shape'])

maxdiff = Counter()
def close(a,b,label):
    a,b = np.asarray(a,float), np.asarray(b,float)
    assert a.shape == b.shape, label
    assert np.isfinite(a).all() and np.isfinite(b).all(), label
    diff = float(np.max(np.abs(a-b), initial=0))
    maxdiff[label] = max(maxdiff[label],diff)
    assert np.allclose(a,b,rtol=2e-12,atol=2e-12), (label,diff)

rows = []
observations_count = checkpoint_count = array_count = scalar_count = 0
records = []
for config, entry in zip(plan['configurations'],supervisor['configurations']):
    folder = RUNS/config['id']
    record_path = folder/'record.json'
    record = json.loads(record_path.read_text()); visit(record); records.append(record)
    assert record['configuration'] == config and record['id'] == config['id']
    assert record['plan_sha256'] == digest(plan_path)
    assert record['producer_sha256'] == digest(EDITION/'code/scripts/validate_observable_horizon.py')
    for name, h in record['source_hashes'].items(): assert digest(EDITION/'code/pde'/name) == h
    assert record['status'] == entry['status'] == entry['worker_status'] == 'operational_pass'
    assert entry['exit_code'] == 0 and entry['stopped'] is None and not entry['log_truncated']
    assert entry['record_sha256'] == digest(record_path)
    assert entry['worker_reported_cpu_seconds'] == record['total_seconds']['cpu']
    assert entry['worker_reported_peak_rss'] == record['peak_rss_bytes']
    assert entry['cpu_seconds'] == max(entry['reaped_cpu_seconds'],entry['sampled_cpu_seconds'],entry['worker_reported_cpu_seconds'])
    assert entry['cpu_seconds'] < plan['budget']['cpu_seconds_per_configuration']
    assert record['peak_rss_bytes'] < plan['budget']['rss_bytes_per_process']
    assert set(record['thread_environment'].values()) == {'1'}
    assert record['restart_exact'] and record['restart_prediction_exact'] and all(record['restart_comparison'].values())
    assert record['frozen_signature_initial'] == record['frozen_signature_final']
    assert Fraction(record['restart_contract']['step_size'])*config['steps'] == 40
    assert record['restart_contract']['steps_before']+record['restart_contract']['steps_after'] == config['steps']
    for name,h in record['outputs'].items(): assert digest(folder/name) == h
    log=json.loads((RUNS/(config['id']+'.log')).read_text()); visit(log)
    for key in ('id','status','total_seconds','peak_rss_bytes'): assert log[key] == record[key]
    assert log['error'] is None
    dims=record['dimensions']; p=config['population_nodes']
    assert dims['first_nodes'] == dims['second_nodes'] == p
    assert dims['action_matrix'] == [dims['second_features'],dims['first_features']]
    assert record['initialization_metadata']['feature_dimensions'] == [dims['first_features'],dims['second_features']]
    checkpoints={}
    for name in ('midpoint_restart.json','final_restart.json'):
        original = json.loads((folder/name).read_text()); visit(original)
        state,data=solver.load_restart(folder/name); checkpoint_count+=1
        assert state.metadata == record['initialization_metadata'] and data.metadata == record['law_metadata']
        assert producer.frozen_signature(state,data) == record['frozen_signature_initial']
        assert state.M.shape == tuple(dims['action_matrix'])
        assert state.b1.shape == (p,dims['first_features']) and state.b2.shape == (p,dims['second_features'])
        assert len(data.inputs) == dims['input_nodes']
        assert solver.state_bytes(state)['arrays'] == record['state_bytes_final']['arrays']
        for key in producer.STATE_KEYS:
            assert producer.encode_array(getattr(state,key),state.arithmetic) == original['state'][key]
        for key in producer.DATA_KEYS:
            assert producer.encode_array(getattr(data,key),state.arithmetic) == original['data'][key]
        checkpoint_scalars=sum(getattr(state,k).size for k in producer.STATE_KEYS)
        assert checkpoint_scalars == record['workspace_final']['state_scalars']
        checkpoints['20' if name.startswith('midpoint') else '40']=(state,data)
        array_count+=12; scalar_count+=sum(len(v['values']) for group in ('state','data') for v in original[group].values())
    assert record['checkpoint_bytes'] == (folder/'midpoint_restart.json').stat().st_size
    assert record['final_checkpoint_bytes'] == (folder/'final_restart.json').stat().st_size
    samples=[]; initial=None
    for item,expected_time in zip(record['observations'],plan['common']['observation_times']):
        assert Fraction(item['time']) == Fraction(expected_time)
        exact=json.loads((folder/item['exact_json']).read_text()); visit(exact)
        assert exact['time'] == item['time'] and exact['digits'] == config['digits'] and exact['backend'] == config['backend']
        assert exact['format'] == producer.OBSERVATION_FORMAT
        arrays={k:decode(v,exact['digits'],exact['backend']) for k,v in exact['arrays'].items()}
        with np.load(folder/item['npz'],allow_pickle=False) as z:
            assert set(arrays) == set(z.files)
            for key,a in arrays.items():
                view=np.asarray(a,float)
                assert np.isfinite(view).all()
                assert view.shape == z[key].shape and view.tobytes() == z[key].tobytes(), key
        array_count+=len(arrays); scalar_count+=sum(a.size for a in arrays.values()); observations_count+=1
        assert item['exact_bytes'] == (folder/item['exact_json']).stat().st_size
        assert item['npz_bytes'] == (folder/item['npz']).stat().st_size
        assert item['float_view_payload_bytes'] == sum(np.asarray(a,float).nbytes for a in arrays.values())
        v={k:np.asarray(a,float) for k,a in arrays.items()}
        if initial is None: initial=v
        for key in ('inputs','labels','input_weights','circle','first_weights','second_weights'):
            assert np.array_equal(v[key],initial[key])
        for key in ('first_weights','second_weights','input_weights'):
            assert np.all(v[key]>=0) and abs(sum(v[key])-1)<2e-12
        for key in ('inputs','circle'): close(np.sum(v[key]**2,axis=1),np.ones(len(v[key])),'circle_norm')
        close(v['input_weights'] @ ((v['training_prediction']-v['labels'])**2),v['loss'],'loss_algebra')
        for prefix,number in (('first',1),('second',2)):
            a=v[prefix+'_pairs']; assert a.shape==(p,dims['input_nodes'],2) and np.max(abs(a))<=1
            assert np.array_equal(a[:,:,0],initial[prefix+'_pairs'][:,:,0])
            rms=np.sqrt(np.sum(v[prefix+'_weights'][:,None]*v['input_weights'][None,:]*(a[:,:,1]-a[:,:,0])**2))
            close(rms,v['rms'+str(number)],'rms_algebra')
            if item['time']=='0': assert rms==0
        for key in ('loss','rms1','rms2'): close(v[key],item[key],'record_scalar')
        if item['time'] in checkpoints:
            state,data=checkpoints[item['time']]
            actual=producer.collect_observation(state,data,arrays['circle'],block_size=plan['common']['block_size'])
            for key,a in actual.items():
                assert producer.encode_array(a,state.arithmetic)==exact['arrays'][key], (config['id'],item['time'],key)
            # Independently assemble the finite matrix prediction on the saved marks.
            b1,b2,M,w,c,p1,p2=[np.asarray(getattr(state,k),float) for k in ('b1','b2','M','w','c','p1','p2')]
            pred=p2 @ (c[:,None]*np.tanh(b2 @ M @ (b1.T @ (p1[:,None]*np.tanh(w @ v['circle'].T)))))
            close(pred,v['prediction'],'independent_matrix_prediction')
        samples.append(dict(time=item['time'],loss=float(v['loss']),rms1=float(v['rms1']),rms2=float(v['rms2']),prediction_max=float(abs(v['prediction']).max())))
    assert len(samples)==6
    assert record['loss_initial']==samples[0]['loss'] and record['loss_final']==samples[-1]['loss']
    for k in ('rms1','rms2'): assert record[k]==samples[-1][k]
    rows.append(dict(id=config['id'],configuration=config,dimensions=dims,
                     law_metadata=record['law_metadata'],initialization_metadata=record['initialization_metadata'],
                     observations=samples,conditioning_diagnostics=record['conditioning_diagnostics'],
                     total_seconds=record['total_seconds'],peak_rss_bytes=record['peak_rss_bytes'],
                     workspace_final=record['workspace_final'],restart_exact=record['restart_exact']))

summary=json.loads((ROOT/'data/generated/observable_hierarchy/H4_author_analysis_v1/summary.json').read_text()); visit(summary)
assert summary['problems']==[]
assert summary['aggregate']['declared']==summary['aggregate']['successful']==14
assert summary['aggregate']['sum_worker_cpu_seconds']==sum(r['total_seconds']['cpu'] for r in records)
assert summary['aggregate']['maximum_peak_rss_bytes']==max(r['peak_rss_bytes'] for r in records)
assert supervisor['total_cpu_seconds']==sum(e['cpu_seconds'] for e in supervisor['configurations'])
assert supervisor['total_cpu_seconds']<plan['budget']['total_cpu_seconds']

# The complete assembly transformations and imported-file identities are hash-checked.
assembly=json.loads((EDITION/'edition_manifest.json').read_text())
assigned_paths={f['path'] for f in manifest['files']}
assembly_provenance=[]
for entry in assembly['files']:
    assert digest(EDITION/entry['destination'])==entry['destination_sha256']
    if entry['source'] not in assigned_paths:
        assembly_provenance.append(dict(destination=entry['destination'],source_read=False,
                                      reason='Original assembly source is not an assigned frozen input; complete canonical edition reviewed.'))
        continue
    assert digest(ROOT/entry['source'])==entry['source_sha256']
    src=(ROOT/entry['source']).read_bytes(); dst=(EDITION/entry['destination']).read_bytes()
    if entry['transform']=='identity': assert src==dst
    elif entry['transform']=='canonical import rename only': assert src.replace(b'from H4_laws import',b'from pde.observable_laws import')==dst
    elif entry['transform'].startswith('append complete'):
        old=(ROOT/entry['destination']).read_bytes()
        assert old.rstrip()+b'\n\n'+src==dst
    else: raise AssertionError(entry)

result=dict(status='pass',files_hash_verified=len(hashes),runs=len(rows),observations=observations_count,
            checkpoints=checkpoint_count,decoded_arrays=array_count,decoded_scalars=scalar_count,
            all_json_value_type_counts=dict(counts),maximum_absolute_discrepancies=dict(maxdiff),
            aggregate=summary['aggregate'],supervisor_cpu_seconds=supervisor['total_cpu_seconds'],
            comparisons=summary['comparisons'],rows=rows,assembly_provenance=assembly_provenance,
            exact_observation_archive_float_views_bitwise_identical=True,
            saved_midpoint_final_recomputed_observations_exact=True,
            note='No initialization, RHS, evolution or research trajectory invoked; exact saved-state observation evaluation only.')
(OUT/'record_audit.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'verified_inputs.json').write_text(json.dumps(hashes,indent=2)+'\n')
# Preserve every record field in a lossless base-and-difference reading view.
def difference(a,b):
    if isinstance(a,dict) and isinstance(b,dict):
        return {k:difference(a.get(k),v) for k,v in b.items() if k not in a or a[k]!=v}
    return b
view={'base':records[0],'differences':[{r['id']:difference(records[0],r)} for r in records[1:]],
      'supervisor':supervisor,'summary_top_level':{k:v for k,v in summary.items() if k not in ('runs','comparisons','supervisor')},
      'summary_new_fields':[{'id':r['id'],**{k:v for k,v in r.items() if k not in records[i]}} for i,r in enumerate(summary['runs'])]}
(OUT/'record_reading_view.json').write_text(json.dumps(view,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('rows','comparisons')}))
