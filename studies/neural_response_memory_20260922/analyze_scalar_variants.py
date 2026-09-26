"""Post-fit validation and circle evaluation; never fits or changes coefficients."""
from pathlib import Path
import argparse
import hashlib
import json
import pickle
import time
import numpy as np
from run_scalar_variants import circle, rms, physical_outputs, consumed, write_json


def record(root, name):
    return json.loads((root/name/'result.json').read_text())


def physical(root, name, decoded=False):
    path=root/name/('decoded_physical.npz' if decoded else 'physical_final.npz')
    with np.load(path) as z:
        return dict(z)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args(); root=args.out
    started=time.monotonic()
    result={'refinements':{},'circle':{},'same_time_trajectories':{}}
    for name in ['dense','parent_P1','tail_tangent_K3','potential_h_d2','basis_r12']:
        a=record(root,name); b=record(root,name+'_refined')
        result['refinements'][name]={
            'output_max_change':float(np.max(np.abs(np.array(a['outputs'])-b['outputs']))),
            'fit_time_change':abs(a['fit_time']-b['fit_time'])}
        if 'decoded_outputs' in a:
            result['refinements'][name]['decoded_max_change']=float(np.max(np.abs(np.array(a['decoded_outputs'])-b['decoded_outputs'])))
    angles=np.arange(4096)*360/4096
    inputs=circle(angles)
    curves={'degrees':angles}
    for width,suffix,variant in [(16,'','basis_r12'),(32,'_n32_extended','basis_r12_n32_extended')]:
        dense=physical_outputs(physical(root,'dense'+suffix),inputs)
        parent=physical_outputs(physical(root,'parent_P1'+suffix),inputs)
        decoded=physical_outputs(physical(root,variant,True),inputs)
        result['circle'][str(width)]={
            'decoded_dense_rms':rms(decoded-dense),
            'decoded_dense_max':float(np.max(np.abs(decoded-dense))),
            'max_error_angle':float(angles[np.argmax(np.abs(decoded-dense))]),
            'parent_dense_rms':rms(parent-dense),
            'parent_dense_max':float(np.max(np.abs(parent-dense))),
            'quadrature_points':len(angles), 'selected_cell':variant}
        for key,array in [('dense',dense),('parent',parent),('decoded',decoded)]:
            curves[f'n{width}_{key}']=array
    a=record(root,'basis_r12');b=record(root,'basis_r12_extended')
    result['passive_extension_control']={
        'training_output_change':float(np.max(np.abs(np.array(a['outputs'][:2])-b['outputs'][:2]))),
        'primary_output_change':float(np.max(np.abs(np.array(a['outputs'][2:5])-b['outputs'][2:5]))),
        'fit_time_change':abs(a['fit_time']-b['fit_time']),
        'decoded_primary_change':float(np.max(np.abs(np.array(a['decoded_outputs'][:5])-b['decoded_outputs'][:5])))}
    dense_full=record(root,'basis_r16');dense=record(root,'dense')
    result['full_rank_control_max_error']=float(np.max(np.abs(np.array(dense_full['outputs'])-dense['outputs'])))
    # Same-time comparisons use saved interpolation only within both time domains.
    from scalar_fourier_reference import DenseReference,initialize
    dense_model=DenseReference(circle([10,125]).T,np.array([1.,-1.]),initialize(16,20260920))
    with (root/'dense/solution.pkl').open('rb') as f: ref_sol=pickle.load(f)
    for name in ['tail_frozen_K3','tail_tangent_K3','potential_g_d1','potential_g_d2',
                 'potential_h_d2','potential_h_d3','basis_r4','basis_r8','basis_r12']:
        with (root/name/'runtime.pkl').open('rb') as f: model=pickle.load(f)
        with (root/name/'solution.pkl').open('rb') as f: sol=pickle.load(f)
        t=np.linspace(0,min(sol.t[-1],ref_sol.t[-1]),401)
        pred=np.array([model.outputs(sol.sol(s)) for s in t])
        target=np.array([dense_model.predict(ref_sol.sol(s),circle([10,125,30,60,90]).T) for s in t])
        result['same_time_trajectories'][name]={
            'time_end':float(t[-1]),'time_points':len(t),
            'training_max_error':float(np.max(np.abs(pred[:,:2]-target[:,:2]))),
            'passive_max_error':float(np.max(np.abs(pred[:,2:]-target[:,2:]))),
            'passive_time_rms':rms(pred[:,2:]-target[:,2:])}
    result['scientific_solver_preparation_seconds']=consumed(root)
    result['postfit_analysis_seconds']=time.monotonic()-started
    result['analysis_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    np.savez_compressed(root/'circle_predictions.npz',**curves)
    write_json(root/'validation.json',result)
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
