import hashlib, json, math, time
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path
import numpy as np

started = time.process_time()
root = Path('/home/amir/Codes/PDE')
edition = root/'data/generated/observable_hierarchy/H3_v2_edition_v2'
scratch = Path(__file__).resolve().parent
runs = edition/'data/established/independent_v2_runs'
reproducer = root/'data/generated/observable_hierarchy/H3_v2_reproducer_v2'
result = {'status':'pass','constant_margins':{},'ridge':{},'runs':[], 'hash_metadata':{}}
T,C,R,B=F(1,200),F(101,10000),F(10101,10000),F(1,32)
D=B+2*R*C*C*T
Aupper=4*R*F(1000,999)
d0=2*R*T+2*C
margins={
 'readout_R':R-F(60401,59800),
 'HS_cap':F(1,1000)-2*T*R*C,
 'operator_cap':F(201,100)-(2+2*T*R*C),
 'row_cap_using_sqrt2_lt_10_over_7':2-F(10,7)-2*T*R*(2+2*T*R*C)*C,
 'speed_cap':3-2*R*((2+2*T*R*C)*C+C+1),
 'D_cap':F(1,31)-D,
 'first_exponent':F(1,1000)-(6*R*D*T+8*R*R*T*T*C*C),
 'A_cap':F(41,10)-Aupper,
 'Aplus2R_cap':F(31,5)-(Aupper+2*R),
 'second_exponent':F(1,1000)-d0*T*F(31,5),
 'Psi_cap':B-d0*F(1000,999),
}
assert all(v>0 for v in margins.values())
result['constant_margins']={k:{'exact':str(v),'float':float(v)} for k,v in margins.items()}
# The third and fourth columns are respectively a duplicate and a zero.
S=np.array([[1.,2.,1.,0.],[-1.,.5,-1.,0.],[.2,-.7,.2,0.]])
U=np.array([[1.,-.4,1.],[.3,1.2,.3]])
A=np.array([[.6,-.4,.1],[-.2,.7,.5]])
eta=F(1,1024*36)
G1=S.T@S;G2=U.T@U
L1=np.linalg.cholesky(G1+float(eta)*np.eye(4));L2=np.linalg.cholesky(G2+float(eta)*np.eye(3))
B1=np.linalg.solve(L1,S.T).T; B2=np.linalg.solve(L2,U.T).T
raw=U.T@A@S
Dridge=np.linalg.solve(L2,np.linalg.solve(L1,raw.T).T)
Q1=S@np.linalg.solve(G1+float(eta)*np.eye(4),S.T)
Q2=U@np.linalg.solve(G2+float(eta)*np.eye(3),U.T)
forward=B2@Dridge@B1.T
oracle=Q2@A@Q1
err=float(np.max(np.abs(forward-oracle)))
adjerr=float(np.max(np.abs(B1@Dridge.T@B2.T-oracle.T)))
ev1=np.linalg.eigvalsh(Q1);ev2=np.linalg.eigvalsh(Q2)
assert max(err,adjerr)<1e-10
assert min(ev1.min(),ev2.min())>-1e-10 and max(ev1.max(),ev2.max())<1+1e-10
result['ridge']={'forward_error':err,'adjoint_error':adjerr,'eigenvalues_1':ev1.tolist(),'eigenvalues_2':ev2.tolist(),'raw_rank_1':int(np.linalg.matrix_rank(G1)),'raw_rank_2':int(np.linalg.matrix_rank(G2))}

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((edition/'review/manifest.json').read_text())
evidence=json.loads((root/'studies/observable_hierarchy/H3_v2_evidence_v3.json').read_text())
allowed={str((edition/p).resolve()):h for p,h in manifest['edition_hashes'].items()}
allowed.update({str((root/p).resolve()):v['sha256'] for p,v in evidence['files'].items()})
allowed[str((edition/'review/manifest.json').resolve())]=evidence['edition_manifest_sha256']

def verify_hashmap(d):
    for name,h in d.items():
        p=Path(name); p=p if p.is_absolute() else edition/p
        assert str(p.resolve()) in allowed, str(p)
        assert digest(p)==h==allowed[str(p.resolve())],str(p)
    return len(d)

for name in ('immutable_raw_evidence_hashes.json','immutable_reproducer_files.json'):
    d=json.loads((reproducer/name).read_text());result['hash_metadata'][name]=verify_hashmap(d)
for name in ('entry_hashes.json','post_execution_hashes.json'):
    d=json.loads((reproducer/name).read_text());rows=d if isinstance(d,list) else d['files']
    for row in rows: assert row['expected']==row['actual']==digest(edition/row['path'])
    result['hash_metadata'][name]=len(rows)
d=json.loads((reproducer/'exit_hashes.json').read_text())
result['hash_metadata']['exit_keys']=list(d)
for key,value in d.items():
    if key=='manifest_sha256': assert value==digest(edition/'review/manifest.json')
    elif key=='auxiliary_source_identity':
        for row in value:
            assert digest(Path(row['executed_source']))==digest(Path(row['retained_source']))==row['sha256']
        result['hash_metadata']['exit_'+key]=value
    elif isinstance(value,list):
        for row in value: assert row['expected']==row['actual']==digest(edition/row['path'])
        result['hash_metadata']['exit_'+key]=len(value)
    elif isinstance(value,dict):result['hash_metadata']['exit_'+key]=verify_hashmap(value)
    else: result['hash_metadata']['exit_'+key]=value
audit=json.loads((reproducer/'read_only_audit.json').read_text())
result['hash_metadata']['read_only_audit_raw_checks']=verify_hashmap(audit['raw_immutable_checks'])
summary=json.loads((edition/'data/established/independent_v2_analysis/summary.json').read_text())
supervisor=json.loads((runs/'supervisor.json').read_text())
assert summary['supervisor']['all_records']==supervisor['configurations']
assert summary['supervisor']['sha256']==digest(runs/'supervisor.json')
assert summary['supervisor']['charged_total_cpu_seconds']==supervisor['total_cpu_seconds']

keys={'b1','g','w','p1','b2','c','p2','M','D'}
data_keys={'inputs','labels','probabilities'}
def decoded(record,area):
    def scalar(v):
        if record['digits'] is None:return float.fromhex(v)
        if record['backend']=='rational':return float(F(int(v,16),10**record['digits']))
        return float(Decimal(v))
    return {k:np.array([scalar(v) for v in a['values']]).reshape(a['shape']) for k,a in record[area].items()}
observations={}
for row in summary['runs']:
    name=row['id'];folder=runs/name
    mid=json.loads((folder/'midpoint_restart.json').read_text());final=json.loads((folder/'final_restart.json').read_text())
    assert set(mid)==set(final)=={'format','digits','backend','metadata','data_metadata','state','data'}
    assert set(mid['state'])==set(final['state'])==keys
    assert set(mid['data'])==set(final['data'])==data_keys
    assert all(mid['state'][k]==final['state'][k] for k in ['b1','g','p1','b2','p2','D'])
    assert mid['data']==final['data']
    for k in keys:assert mid['state'][k]['shape']==final['state'][k]['shape']
    a=decoded(final,'state');data=decoded(final,'data');u=data['inputs']
    assert all(np.isfinite(x).all() for x in list(a.values())+list(data.values()))
    h0=np.tanh(np.einsum('ik,jk->ij',a['g'],u));ht=np.tanh(np.einsum('ik,jk->ij',a['w'],u))
    def second(h,mat):
        small=np.einsum('pk,p,pa->ka',a['b1'],a['p1'],h)
        return np.tanh(np.einsum('qd,dk,ka->qa',a['b2'],mat,small,optimize=False))
    z0=second(h0,a['D']);zt=second(ht,a['M'])
    with np.load(folder/'observations.npz',allow_pickle=False) as z: saved={k:z[k] for k in z.files}
    observations[name]=saved
    errors={'first_pairs':float(np.max(np.abs(saved['first_pairs']-np.stack([h0,ht],axis=-1)))),'second_pairs':float(np.max(np.abs(saved['second_pairs']-np.stack([z0,zt],axis=-1))))}
    hc=np.tanh(np.einsum('ik,jk->ij',a['w'],saved['circle']));hc2=second(hc,a['M'])
    pred=np.einsum('p,p,pa->a',a['p2'],a['c'],hc2)
    errors['prediction']=float(np.max(np.abs(pred-saved['prediction'])))
    for n,prior,current in [(1,h0,ht),(2,z0,zt)]:
        rms=math.sqrt(float(np.einsum('p,pa,a->',a['p'+str(n)],(current-prior)**2,data['probabilities'])))
        errors['rms'+str(n)]=abs(rms-row['rms'+str(n)])
    assert max(errors.values())<1e-12
    P=len(a['g']);d1=a['b1'].shape[1];d2=a['b2'].shape[1]
    S=P*(d1+d2+7)+2*d1*d2
    assert S==sum(x.size for x in a.values())==row['state_scalars']
    rec=json.loads((folder/'record.json').read_text())
    assert row['record_sha256']==digest(folder/'record.json')
    for k,h in rec['source_hashes'].items():assert h==manifest['edition_hashes']['code/pde/'+k]
    for k,h in rec['outputs'].items():assert h==digest(folder/k)
    assert rec['producer_sha256']==manifest['edition_hashes']['code/scripts/validate_observable_solver.py']
    assert all(v>0 for v in rec['dynamic_changes'].values())
    result['runs'].append({'id':name,'schema':sorted(final),'state_shapes':{k:list(v.shape) for k,v in a.items()},'npz_shapes':{k:list(v.shape) for k,v in saved.items()},'state_scalars':S,'reconstruction_errors':errors,'frozen_marks_exact':True})
result['comparisons']=[]
for c in summary['comparisons']:
    diff=observations[c['left']]['prediction']-observations[c['right']]['prediction']
    actual=float(np.max(np.abs(diff)))
    assert actual==c['final_panel_max_abs_prediction_difference']
    result['comparisons'].append({'left':c['left'],'right':c['right'],'panel_max':actual})
result['cpu_seconds']=time.process_time()-started
(scratch/'independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'runs':len(result['runs']),'comparisons':len(result['comparisons']),'maximum_error':max(v for r in result['runs'] for v in r['reconstruction_errors'].values()),'cpu_seconds':result['cpu_seconds'],'hash_metadata':result['hash_metadata'],'constant_margins':result['constant_margins'],'ridge':result['ridge']},indent=2))
