"""Bounded review checks; no training, network, or writes outside reviewer scratch."""
from pathlib import Path
import hashlib
import importlib.util
import json
import platform
import sys
import numpy as np
import scipy
from scipy.linalg import expm

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2] / 'inputs'
OUT = Path(__file__).resolve().parent
rms = lambda x: float(np.sqrt(np.mean(np.asarray(x)**2)))
report = {'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__}}
manifest = json.loads((ROOT/'manifest.json').read_text())
report['hashes'] = {k: hashlib.sha256((ROOT/k).read_bytes()).hexdigest() == v['sha256'] for k,v in manifest['files'].items()}
assert all(report['hashes'].values())

def bundle(name):
    with np.load(ROOT/'figures'/f'{name}.npz', allow_pickle=False) as z:
        return {k:z[k] for k in z.files}

a=bundle('response_memory_source'); meta=json.loads(str(a['metadata_json']))
report['trajectory']={}
for p in (1,3,7):
    err=np.sqrt(np.mean((a[f'common_memory_{p}']-a['common_dense'])**2,axis=1))
    sen=np.sqrt(np.mean((a['common_dense']-a['common_dense_coarse'])**2,axis=1))+np.sqrt(np.mean((a[f'common_memory_{p}']-a[f'common_memory_{p}_coarse'])**2,axis=1))
    assert np.allclose(err,a[f'common_rms_{p}'],rtol=1e-13,atol=1e-15)
    assert np.allclose(sen,a[f'common_sensitivity_{p}'],rtol=1e-13,atol=1e-15)
    report['trajectory'][p]={'saved_times':len(err),'max_saved_rms':float(err.max()),'final_rms':float(err[-1]),'positive_times_error_le_sensitivity':int(np.sum(err[1:]<=sen[1:]))}
report['mnist']={p:{'rms':rms(a[f'mnist_{p}']-a['mnist_dense']), 'sign_agreement_with_dense':float(np.mean((a[f'mnist_{p}']>0)==(a['mnist_dense']>0)))} for p in (1,2,3)}
report['mnist_metadata']=meta['mnist']
resolved=[]
for f in meta['factor_direct']:
    if not f['valid']: continue
    m=next(r for r in meta['factor_memory'] if r['case']==f['case'] and r['rank']==f['rank'])
    if m['valid']: resolved.append(f['circle_rms']/m['circle_rms'])
report['factor_metadata']={'resolved':len(resolved),'memory_wins':sum(r>1 for r in resolved),'over_factor_two':sum(r>2 for r in resolved),'excluded':meta['factor_excluded']}
b=bundle('radial_source_data')
report['circle_rms']={kind:[[rms(b[f'{kind}_{i}_P{p}']-b[f'{kind}_{i}_P0']) for p in ps] for i in range(5)] for kind,ps in [('shallow',(1,3,7)),('deep',(1,2,3))]}
c=bundle('learning_controls_source'); cm=json.loads(str(c['metadata_json']))
report['controls']=[]
for i in range(5):
    prefix=f'case_{i}_'; row=cm['tasks'][i]
    K=c[prefix+'train_kernel']; y=c[prefix+'represented_labels']; alpha=c[prefix+'alpha']
    # Reconstruct initial training output from source coefficient and endpoint spectral solution.
    eig,V=np.linalg.eigh((K+K.T)/2)
    t=row['frozen']['fit_time']; rates=2*eig/len(y)
    v=V.T@alpha
    direction=v*eig/(-np.expm1(-rates*t))
    f0=y-V@direction
    fitted=y-V@(np.exp(-rates*t)*direction)
    matrix_exp=y+expm(-2*K*(t/7)/len(y))@(f0-y)
    spectral_at_check=y-V@(np.exp(-rates*t/7)*direction)
    expected=c['initial_prediction']+c[prefix+'cross_kernel']@alpha
    assert np.allclose(expected,c[prefix+'frozen_ntk'],atol=1e-13)
    actual={'frozen_ntk':rms(c[prefix+'frozen_ntk']-c[prefix+'dense']), 'memory':rms(c[prefix+'memory']-c[prefix+'dense']), 'factors':[rms(f-c[prefix+'dense']) for f in c[prefix+'factors']]}
    assert np.isclose(actual['frozen_ntk'],row['rms_vs_dense']['frozen_ntk'],rtol=1e-13)
    assert np.isclose(actual['memory'],row['rms_vs_dense']['memory'],rtol=1e-13)
    assert np.allclose(actual['factors'],row['rms_vs_dense']['factors'],rtol=1e-13)
    report['controls'].append({'case':row['case'],'rms':actual,'frozen_mse':rms(fitted-y)**2,'time':t,'condition':float(eig[-1]/eig[0]),'cross_training_max_error':float(np.max(np.abs(f0+K@alpha-fitted))),'expm_check_max_error':float(np.max(np.abs(matrix_exp-spectral_at_check)))})
s=bundle('sphere_source_data')
report['sphere']={p:{'rms':rms(s[f'P{p}']-s['dense']),'training_rms':rms(s[f'P{p}_train']-s['labels'])} for p in (1,2,3)}

# Independent finite-difference check of the submitted empirical-NTK block formula.
spec=importlib.util.spec_from_file_location('review_frozen_ntk',ROOT/'figures/frozen_ntk.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
rng=np.random.default_rng(782); n=5
weights=list(mod.initial(n,813)); weights[2]*=n
X=rng.normal(size=(4,2)); Q=rng.normal(size=(3,2)); eps=1e-5
def jac(inputs):
    blocks=[]
    for j,W in enumerate(weights):
        J=[]
        for index in np.ndindex(W.shape):
            old=W[index];W[index]=old+eps;fp=mod.fields(weights,inputs)[-1]
            W[index]=old-eps;fm=mod.fields(weights,inputs)[-1]
            W[index]=old;J.append((fp-fm)/(2*eps))
        blocks.append(np.stack(J,axis=1))
    return blocks
J,Jq=jac(X),jac(Q)
actual=mod.blocks(mod.fields(weights,Q),mod.fields(weights,X),Q,X,n)
expected=np.stack([mob*(u@v.T) for mob,u,v in zip((n,1,n),Jq,J)])
report['kernel_finite_difference_max_error']=float(np.max(np.abs(actual-expected)))
assert report['kernel_finite_difference_max_error']<1e-8

# Algebra-only weighted reconstruction derivative: arbitrary well-conditioned raw state.
P=4; d=3; rho=.7; g=2.3; tau=1.8
H=rng.normal(size=(d,P));B=rng.normal(size=(d,P));A=rng.normal(size=(P,P));G=A@A.T+np.eye(P)
h=rng.normal(size=d);b=rng.normal(size=d);e=np.ones(P)
T=np.diag(np.arange(P))
for k in range(P):
    for j in range(k): T[k,j]=2*j+1
Hi=rho*np.outer(h,e)-(g/tau)*H@T.T
Bi=rho*np.outer(b,e)-(g/tau)*B@T.T
Gi=rho*np.outer(e,e)-(g/tau)*(T@G+G@T.T)
I=np.linalg.inv(G)
derivative=Bi@I@H.T+B@I@Hi.T-B@I@Gi@I@H.T
hs=H@I@e;bs=B@I@e
formula=rho*(np.outer(b,h)-np.outer(b-bs,h-hs))
report['joint_reconstruction_identity_max_error']=float(np.max(np.abs(derivative-formula)))
assert report['joint_reconstruction_identity_max_error']<1e-10
(OUT/'check_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('hashes','mnist_metadata')},indent=2))
