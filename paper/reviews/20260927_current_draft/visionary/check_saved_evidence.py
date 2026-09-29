"""Bounded, read-only array checks; no training and no submitted-code imports."""
from pathlib import Path
import json
import numpy as np

BASE = Path(__file__).resolve().parent
INPUT = BASE.parent / 'inputs' / 'figures'
def rms(x): return float(np.sqrt(np.mean(np.asarray(x)**2)))
out = {}
with np.load(INPUT/'radial_source_data.npz', allow_pickle=False) as z:
    out['circle'] = {family: [[rms(z[f'{family}_{i}_P{p}']-z[f'{family}_{i}_P0'])
                    for p in orders] for i in range(5)]
                    for family, orders in [('deep',(1,2,3)),('shallow',(1,3,7))]}
with np.load(INPUT/'response_memory_source.npz', allow_pickle=False) as z:
    meta = json.loads(str(z['metadata_json']))
    out['mnist'] = {p:rms(z[f'mnist_{p}']-z['mnist_dense']) for p in (1,2,3)}
    out['trajectory'] = {}
    for p in (1,3,7):
        actual = np.sqrt(np.mean((z[f'common_memory_{p}']-z['common_dense'])**2,axis=1))
        sensitivity = np.sqrt(np.mean((z['common_dense']-z['common_dense_coarse'])**2,axis=1))
        sensitivity += np.sqrt(np.mean((z[f'common_memory_{p}']-z[f'common_memory_{p}_coarse'])**2,axis=1))
        assert np.allclose(actual,z[f'common_rms_{p}'],rtol=1e-13,atol=1e-15)
        assert np.allclose(sensitivity,z[f'common_sensitivity_{p}'],rtol=1e-13,atol=1e-15)
        out['trajectory'][p] = dict(checkpoints=len(actual),max_rms=float(actual.max()),final_rms=float(actual[-1]),
            initial_rms=float(actual[0]),positive_times_above_sensitivity=int(np.sum(actual[1:]>sensitivity[1:])))
    wins = []
    for row in meta['factor_direct']:
        if not row['valid']: continue
        match = next(x for x in meta['factor_memory'] if x['case']==row['case'] and x['P']==row['P'])
        if match['valid']: wins.append(row['circle_rms']/match['circle_rms'])
    out['factor_metadata_check'] = dict(comparisons=len(wins),wins=sum(x>1 for x in wins),wins_over_two=sum(x>2 for x in wins),minimum_ratio=min(wins))
with np.load(INPUT/'learning_controls_source.npz', allow_pickle=False) as z:
    meta = json.loads(str(z['metadata_json']))
    out['controls'] = []
    for i,task in enumerate(meta['tasks']):
        key = f'case_{i}_';dense=z[key+'dense']
        measured = dict(frozen_ntk=rms(z[key+'frozen_ntk']-dense),memory=rms(z[key+'memory']-dense),
                        factors=[rms(v-dense) for v in z[key+'factors']])
        for k,v in measured.items(): assert np.allclose(v,task['rms_vs_dense'][k],rtol=1e-12)
        err=float(np.max(np.abs(z['initial_prediction']+z[key+'cross_kernel']@z[key+'alpha']-z[key+'frozen_ntk'])))
        assert err<1e-7
        K=z[key+'train_kernel']; assert np.allclose(K,z[key+'kernel_blocks'].sum(axis=0))
        eig=np.linalg.eigvalsh((K+K.T)/2)
        out['controls'].append(dict(case=task['case'],**measured,spectral_reconstruction_error=err,
            condition=float(eig[-1]/eig[0]),block_traces=np.trace(z[key+'kernel_blocks'],axis1=1,axis2=2).tolist(),
            frozen_fit_time=task['frozen']['fit_time'],memory_fit_time=task['memory_fit_time']))
with np.load(INPUT/'sphere_source_data.npz', allow_pickle=False) as z:
    out['sphere'] = {p:dict(rms=rms(z[f'P{p}']-z['dense']),train_rms=rms(z[f'P{p}_train']-z['labels'])) for p in (1,2,3)}
    out['sphere']['dense_train_rms'] = rms(z['dense_train']-z['labels'])

# Independent polynomial-identity check on a fine deterministic quadrature.
from numpy.polynomial.legendre import Legendre,leggauss
x = np.linspace(0,1,31)
out['legendre_identity_max_error'] = max(float(np.max(np.abs(
    x*2*Legendre.basis(k).deriv()(2*x-1)-k*Legendre.basis(k)(2*x-1)
    -sum((2*j+1)*Legendre.basis(j)(2*x-1) for j in range(k))))) for k in range(1,9))
q,w=leggauss(64);u=(q+1)/2;w=w/2;P=4
h=np.column_stack((np.sin(u),u**3));b=np.column_stack((np.cos(2*u),np.exp(u)))
V=np.column_stack([Legendre.basis(k)(q) for k in range(P)])
hp=V@((2*np.arange(P)+1)[:,None]*(V.T@(w[:,None]*h)))
bp=V@((2*np.arange(P)+1)[:,None]*(V.T@(w[:,None]*b)))
direct=b.T@(w[:,None]*h)-bp.T@(w[:,None]*hp)
tail=(b-bp).T@(w[:,None]*(h-hp))
out['product_defect_max_error']=float(np.max(np.abs(direct-tail)))
(BASE/'saved_evidence_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
