import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[key]='1'
import pathlib,json,time,resource,sys
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
from fractions import Fraction
from decimal import Decimal
import numpy as np
start=time.process_time();root=pathlib.Path('/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2');out=pathlib.Path(__file__).parent
runroot=root/'data/established/independent_v2_runs'; summary=json.loads((root/'data/established/independent_v2_analysis/summary.json').read_text())
names=('b1','g','w','p1','b2','c','p2','M','D'); frozen=('b1','g','p1','b2','p2','D')
def decode(record,group):
    p=record['digits'];backend=record['backend'];result={}
    for key,a in record[group].items():
        assert len(a['values'])==math_prod(a['shape'])
        if p is None: values=[float.fromhex(x) for x in a['values']]
        elif backend=='rational': values=[float(Fraction(int(x,16),10**p)) for x in a['values']]
        else: values=[float(Decimal(x)) for x in a['values']]
        result[key]=np.array(values).reshape(a['shape'])
        assert np.isfinite(result[key]).all()
    return result
def math_prod(shape):
    ans=1
    for n in shape:ans*=n
    return ans
def maxerr(a,b):return float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
records=[];predictions={};losses={};rmsvalues={}
for r in summary['runs']:
    name=r['id'];dir=runroot/name
    mid=json.loads((dir/'midpoint_restart.json').read_text());fin=json.loads((dir/'final_restart.json').read_text())
    assert set(mid['state'])==set(names)==set(fin['state'])
    for key in frozen:assert mid['state'][key]==fin['state'][key],(name,key)
    assert mid['data']==fin['data']
    # Both checkpoints are fully decoded, although only the final one supplies observations.
    ms=decode(mid,'state');md=decode(mid,'data');s=decode(fin,'state');d=decode(fin,'data')
    count=sum(a.size for a in s.values()); P1=len(s['p1']);P2=len(s['p2']);d1=s['b1'].shape[1];d2=s['b2'].shape[1]
    assert count==P1*(d1+5)+P2*(d2+2)+2*d1*d2==r['state_scalars']
    assert sum(a.size for a in ms.values())==count
    assert all(s[k].shape==ms[k].shape for k in names)
    data=d['inputs'];h10=np.tanh(s['g']@data.T);h1=np.tanh(s['w']@data.T)
    # Contract the upper basis with the action first, then the lower means.
    current_kernel_factor=s['b2']@s['M'];initial_kernel_factor=s['b2']@s['D']
    z20=initial_kernel_factor@(s['b1'].T@(s['p1'][:,None]*h10))
    z2=current_kernel_factor@(s['b1'].T@(s['p1'][:,None]*h1))
    h20=np.tanh(z20);h2=np.tanh(z2)
    pairs1=np.stack((h10,h1),axis=-1);pairs2=np.stack((h20,h2),axis=-1)
    rr1=float(np.sqrt(np.sum(s['p1'][:,None]*d['probabilities'][None,:]*(h1-h10)**2)))
    rr2=float(np.sqrt(np.sum(s['p2'][:,None]*d['probabilities'][None,:]*(h2-h20)**2)))
    with np.load(dir/'observations.npz',allow_pickle=False) as saved:
        circle=saved['circle'];h1c=np.tanh(s['w']@circle.T)
        h2c=np.tanh(current_kernel_factor@(s['b1'].T@(s['p1'][:,None]*h1c)))
        prediction=(s['p2']*s['c'])@h2c
        errors={'first_pairs':maxerr(pairs1,saved['first_pairs']),'second_pairs':maxerr(pairs2,saved['second_pairs']),'prediction':maxerr(prediction,saved['prediction']),'first_weights':maxerr(s['p1'],saved['first_weights']),'second_weights':maxerr(s['p2'],saved['second_weights']),'input_weights':maxerr(d['probabilities'],saved['input_weights']),'inputs':maxerr(data,saved['inputs']),'rms1':abs(rr1-float(saved['rms1'])),'rms2':abs(rr2-float(saved['rms2']))}
        predictions[name]=saved['prediction'].copy()
    loss=float(d['probabilities']@(((s['p2']*s['c'])@h2-d['labels'])**2));errors['loss']=abs(loss-r['loss_final'])
    assert max(errors.values())<2e-12,(name,errors)
    changes={'row_max_abs':float(np.max(np.abs(s['w']-s['g']))),'readout_max_abs':float(np.max(np.abs(s['c']))),'matrix_frobenius':float(np.linalg.norm(s['M']-s['D']))}
    assert min(changes.values())>0
    for k in changes:assert abs(changes[k]-r['dynamic_changes'][k])<2e-12
    records.append({'id':name,'all_checkpoint_values_decoded':True,'unchanged_frozen_marks_exact':True,'state_scalars':count,'checkpoint_shapes_constant':True,'errors':errors,'dynamic_changes':changes})
    losses[name]=loss;rmsvalues[name]=(rr1,rr2)
comparisons=[]
for c in summary['comparisons']:
    l,r=c['left'],c['right'];delta=predictions[l]-predictions[r]
    error=max(abs(float(np.max(np.abs(delta)))-c['final_panel_max_abs_prediction_difference']),abs(float(np.sqrt(np.mean(delta**2)))-c['final_panel_rms_prediction_difference']))
    assert error<2e-12
    comparisons.append({'left':l,'right':r,'recalculation_error':error})
result={'status':'pass','runs':records,'comparisons':comparisons,'maximum_error':max(max(r['errors'].values()) for r in records),'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,'trajectory_calls':0,'initializer_calls':0}
(out/'checkpoint_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
