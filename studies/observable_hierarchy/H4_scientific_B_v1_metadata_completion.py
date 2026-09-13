import json,hashlib,sys,resource,time
from pathlib import Path
import numpy as np
from pde.observable_solver import load_restart,state_bytes
from scripts.validate_observable_horizon import encode_array
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.process_time(); root=Path('/home/amir/Codes/PDE')
here=Path(__file__).resolve().parent
runs=root/'data/generated/observable_hierarchy/H4_author_runs_v1'
plan=json.loads((root/'data/generated/observable_hierarchy/H4_candidate_v1/code/validation/observable_horizon_plan.json').read_text())
def hash_json(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
maximum_svd_error=0
for config in plan['configurations']:
    folder=runs/config['id'];record=json.loads((folder/'record.json').read_text());s,d=load_restart(folder/'final_restart.json'); ar=s.arithmetic
    sig=record['frozen_signature_final']
    for key in ('b1','g','p1','b2','p2','D'): assert hash_json(encode_array(getattr(s,key),ar))==sig['state'][key]
    for key in ('inputs','labels','probabilities'): assert hash_json(encode_array(getattr(d,key),ar))==sig['data'][key]
    assert hash_json(s.metadata)==sig['state_metadata'] and hash_json(d.metadata)==sig['data_metadata']
    for pop in ('1','2'):
        b=np.asarray(getattr(s,'b'+pop),float);p=np.asarray(getattr(s,'p'+pop),float)
        singular=np.linalg.svd(b.T@(p[:,None]*b),compute_uv=False)
        expected=np.array(record['conditioning_diagnostics']['population_'+pop]['singular_values'])
        maximum_svd_error=max(maximum_svd_error,float(np.max(np.abs(singular-expected))))
        assert np.allclose(singular,expected,rtol=1e-12,atol=1e-14)
    P1,P2,d1,d2,A=len(s.b1),len(s.b2),s.b1.shape[1],s.b2.shape[1],len(d.inputs)
    state_count=P1*(d1+5)+P2*(d2+2)+2*d1*d2; moving=2*P1+P2+d1*d2;B=min(16,A)
    block=32*(P1+P2)*B+12*(d1+d2)*B+8*d1*d2
    w=record['workspace_final']
    assert (w['state_scalars'],w['dynamic_scalars'],w['data_scalars'],w['block_workspace_scalar_allowance'],w['evolution_scalar_slot_allowance'],w['final_pair_scalars'])==(state_count,moving,4*A,block,6*state_count+8*moving+12*A+block,2*(P1+P2)*A)
    initial=s.dynamic_copy(s.g.copy(),ar.zeros(s.c.shape),s.D.copy())
    assert state_bytes(initial)==record['state_bytes_initial']
    assert record['checkpoint_bytes']==(folder/'midpoint_restart.json').stat().st_size
    assert record['final_checkpoint_bytes']==(folder/'final_restart.json').stat().st_size
manifest=json.loads((root/'studies/observable_hierarchy/H4_review_manifest_v1.json').read_text())
for entry in manifest['files']:
    raw=(root/entry['path']).read_bytes()
    assert len(raw)==entry['bytes'] and hashlib.sha256(raw).hexdigest()==entry['sha256']
result=dict(status='pass',runs=14,all_final_signatures_match_decoded_values=True,all_conditioning_singular_values_recomputed=True,maximum_svd_error=maximum_svd_error,all_workspace_scalar_counts_match=True,initial_state_bytes_match=True,input_hashes_unchanged=True,cpu_seconds=time.process_time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
(here/'metadata_completion.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
