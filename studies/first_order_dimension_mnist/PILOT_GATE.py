"""Reconstruct the checked final numerical gate from retained pilot trajectories."""
import argparse
import json
from pathlib import Path
import numpy as np

BASE=Path(__file__).resolve().parents[2]/'data/generated/first_order_dimension_mnist'

def build():
    result={}
    for model,step in (('network',.25),('closure',.125)):
        def read(dtype,h):
            with np.load(BASE/f'pilot_wave/{model}_{dtype}_h{h}/observations.npz',allow_pickle=False) as a:
                return a['val_predictions'][-1].astype(np.float64),a['val_y'].astype(np.float64)
        full,y=read('float64',step);half,yh=read('float64',step/2)
        assert np.array_equal(y,yh)
        # The retained precision pilot uses .25 for both models; record this explicitly.
        single,ys=read('float32',.25);double,yd=read('float64',.25)
        assert np.array_equal(y,ys) and np.array_equal(y,yd)
        rms=float(np.sqrt(np.mean((full-half)**2)))
        loss=float(abs(np.mean((full-y)**2)-np.mean((half-y)**2)))
        roundoff=float(np.sqrt(np.mean((single-double)**2)))
        result[model]={'step':step,'refinement_reference':step/2,'timestep_rms':rms,
                       'timestep_loss_difference':loss,'float32_rms':roundoff,'precision_source_step':.25,
                       'float64_halfstep_reference':True,'step_gate_pass':rms<=.002 and loss<=.002,
                       'precision_pass':roundoff<=1e-4}
    assert all(r['step_gate_pass'] and r['precision_pass'] for r in result.values())
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='pilot_gate_reconstructed.json');a=p.parse_args()
    result=build()
    with (BASE/a.output).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))
