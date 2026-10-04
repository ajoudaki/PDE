"""Stronger repair controls, selected using corrected training loss only."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
import torch
from history_probe import new_flow, edit_score, interaction

HERE=Path(__file__).resolve().parent


@torch.no_grad()
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=False)
    manifest={'command':sys.argv,'python':sys.executable,'torch':torch.__version__,
              'source_hashes':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ['history_controls.py','history_probe.py','baseline_compact_flow.py',
                                            'HISTORY_CONTROL_PROTOCOL.md']},'inputs':{},
              'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
    rows=[]
    for path in sorted(a.input.glob('seed*_repair.npz')):
        manifest['inputs'][str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
        z=np.load(path);seed=int(path.stem.split('_')[0][4:]);n=z['first'].shape[0]
        model=new_flow(z['x'],z['clean_labels'],n,seed,'cpu')
        model.w.copy_(torch.from_numpy(z['first']));model.matrices[0].copy_(torch.from_numpy(z['hidden']))
        model.c.copy_(torch.from_numpy(z['readout']))
        h=torch.from_numpy(z['h_coeff_4']);b=torch.from_numpy(z['b_coeff_4'])
        history=-interaction(h[:,:,[1,7]],b[:,:,[1,7]],n,model.M)
        gradient=model.rhs()[1];gradient=gradient*(history.norm()/gradient.norm())
        row={'seed':seed}
        for name,edit in [('history',history),('current_gradient',gradient)]:
            candidates=[]
            for alpha in (0.,.25,.5,1.,2.,4.):
                score=edit_score(model,alpha*edit,z['query'],z['truth'],z['clean_labels'],2.)
                candidates.append({'alpha':alpha,**score})
            chosen=min(candidates,key=lambda r:r['immediate']['train_mse'])
            row[name]={'selected':chosen,'candidates':candidates}
        row['extra_cleanup']=edit_score(model,torch.zeros_like(history),z['query'],z['truth'],
                                       z['clean_labels'],2.5)
        rows.append(row)
        print(json.dumps({'seed':seed,'history':row['history']['selected'],
                          'gradient':row['current_gradient']['selected'],
                          'extra':row['extra_cleanup']}),flush=True)
    (a.out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (a.out/'results.json').write_text(json.dumps(rows,indent=2)+'\n')
    (a.out/'completion.json').write_text(json.dumps({'exit_status':0,'cases':len(rows)})+'\n')


if __name__=='__main__':main()
