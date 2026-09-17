#!/usr/bin/env python3
"""Separate raw-array arithmetic; never reads the main analysis or plotting code."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm

ROOT=Path(__file__).resolve().parents[2]


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()


def curve_rms(a):
    return np.sqrt(np.sum(a*a,axis=(-2,-1)))/a.shape[-1]


def main(output):
    manifest=json.loads((output/'manifest.json').read_text())
    hashes={'manifest.json':sha(output/'manifest.json'),'inputs.npz':sha(output/'inputs.npz')}
    assert hashes['inputs.npz']==manifest['inputs_sha256']
    assert sha(ROOT/'studies/xor_network_closure/EXPERIMENT_PLAN.md')==manifest['plan_sha256']
    with np.load(output/'inputs.npz') as z:
        y=z['labels']; weights=z['weights']; times=z['times']
    records={}; obs={}; grams={}; validation={}
    for family in ('network','closure'):
        for config in manifest[family+'_runs']:
            name=config['name'];folder=output/family/name
            r=json.loads((folder/'record.json').read_text())
            assert r['status'] in ('success','complete') and r['config']==config
            hashes[str((folder/'record.json').relative_to(output))]=sha(folder/'record.json')
            for file,value in r['output_hashes'].items():
                digest=value if isinstance(value,str) else value['sha256']
                assert sha(folder/file)==digest,(name,file)
                hashes[str((folder/file).relative_to(output))]=digest
            for file,digest in r['source_hashes'].items():assert sha(ROOT/file)==digest,file
            with np.load(folder/'observations.npz') as z:o={k:z[k] for k in z.files}
            g=np.load(folder/'gram.npy',mmap_mode='r')
            assert np.array_equal(o['times'],times) and g.shape==(201,2,144,144)
            assert all(np.isfinite(v).all() for v in o.values()) and np.isfinite(g).all()
            asym=float(np.max(np.abs(g-g.swapaxes(-1,-2))))
            assert asym<=2e-10 and np.abs(g).max()<=1+2e-10
            minimum=min(float(np.linalg.eigvalsh(g[-1,l])[0]) for l in (0,1))
            assert minimum>=-2e-10
            loss_gap=float(np.max(np.abs(o['loss']-((o['predictions'][:,:16]-y)**2*weights).sum(axis=1))))
            diagonal=(np.diagonal(g[:,:,:16,:16],axis1=-2,axis2=-1)*weights).sum(axis=-1)
            diagonal_gap=float(np.max(np.abs(diagonal-o['raw_rms']**2)))
            tol=3e-6 if config.get('dtype')=='float32' else 2e-10
            assert loss_gap<=tol and diagonal_gap<=tol and np.max(np.abs(o['movement_rms'][0]))<=tol
            validation[name]={'loss_identity_error':loss_gap,'diagonal_identity_error':diagonal_gap,
                              'asymmetry':asym,'minimum_endpoint_eigenvalue':minimum}
            records[name]=r;obs[name]=o;grams[name]=g
    assert records['n8192_s11']['initial_float64_arrays']==records['n8192_s11_half']['initial_float64_arrays']
    assert records['n2048_s11']['initial_float64_arrays']==records['n2048_s11_float64']['initial_float64_arrays']
    for left,right in [('N3_base','N3_base_half'),('N5_fine','N5_fine_half')]:
        assert records[left]['initialization_state_hashes']==records[right]['initialization_state_hashes']
    means={n:np.mean([grams[f'n{n}_s{s}'] for s in (11,29,47)],axis=0) for n in (2048,8192)}
    losses={str(n):np.mean([obs[f'n{n}_s{s}']['loss'] for s in (11,29,47)],axis=0).tolist() for n in means}
    errors=[];frozen=[];controls=[]
    for n,g in means.items():
        for panel,sl in [('training',slice(0,16)),('circle',slice(16,144))]:
            for layer in (0,1):
                reference=g[:,layer,sl,sl]
                base=curve_rms(reference-reference[0]);frozen.append({'width':n,'panel':panel,'layer':layer+1,'curve':base.tolist(),'maximum':float(base.max()),'terminal':float(base[-1])})
                for config in manifest['closure_runs']:
                    name=config['name'];pred=grams[name][:,layer,sl,sl]
                    for quantity,diff in [('G',pred-reference),('DeltaG',(pred-pred[0])-(reference-reference[0]))]:
                        values=curve_rms(diff)
                        errors.append({'closure':name,'width':n,'panel':panel,'layer':layer+1,'observable':quantity,
                                       'maximum':float(values.max()),'terminal':float(values[-1]),'curve':values.tolist()})
    for kind,pairs in [('numerical',[('n8192_s11','n8192_s11_half'),('n2048_s11','n2048_s11_float64'),('N3_base','N3_base_half'),('N5_fine','N5_fine_half')]),
                       ('quadrature',[(f'N{n}_base',f'N{n}_fine') for n in (1,3,5)])]:
        for left,right in pairs:
            values={'loss':float(np.max(np.abs(obs[left]['loss']-obs[right]['loss'])))}
            for panel,sl in [('training',slice(0,16)),('circle',slice(16,144))]:
                for l in (0,1):
                    a=grams[left][:,l,sl,sl];b=grams[right][:,l,sl,sl]
                    values[f'{panel}_G{l+1}']=float(curve_rms(a-b).max())
                    values[f'{panel}_DeltaG{l+1}']=float(curve_rms((a-a[0])-(b-b[0])).max())
            controls.append({'kind':kind,'left':left,'right':right,'maxima':values,'maximum':max(values.values()),'passed':max(values.values())<=.002})
    frozen_readout={}
    for n in (2048,8192):
        curves=[]
        for seed in (11,29,47):
            name=f'n{n}_s{seed}';K=grams[name][0,1,:16,:16]
            initial_residual=obs[name]['predictions'][0,:16]-y
            values=[]
            for t in times:
                residual=expm((-2*t/16)*K)@initial_residual
                values.append(float(np.mean(residual**2)))
            frozen_readout[name]=values;curves.append(values)
        frozen_readout[f'n{n}_mean']=np.mean(curves,axis=0).tolist()
    result={'status':'passed','scope':'Independent saved-array arithmetic; no main analysis read, no new trajectories.',
            'source_sha256':sha(__file__),'inputs_and_outputs_sha256':hashes,'validation':validation,
            'network_mean_loss':losses,'closure_loss':{c['name']:obs[c['name']]['loss'].tolist() for c in manifest['closure_runs']},
            'gram_errors':errors,'frozen_gram':frozen,'controls':controls,'frozen_readout_loss':frozen_readout,
            'times':times.tolist(),'numpy_version':np.__version__,'scipy_version':scipy.__version__,
            'frozen_readout_method':'scipy.linalg.expm on the original Gram; independent of eigendecomposition analysis',
            'command':['python','studies/xor_network_closure/CHECK.py','--output',str(output)]}
    with (output/'independent_check.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':'passed','runs':len(obs),'gram_error_curves':len(errors),'terminal_network_loss':losses['8192'][-1],
                      'terminal_frozen_loss':frozen_readout['n8192_mean'][-1]}))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    main(p.parse_args().output.resolve())
