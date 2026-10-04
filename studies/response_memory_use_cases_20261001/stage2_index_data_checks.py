"""No-training audit of dataset normalization and actual float32 PCA functions."""
import argparse
import json
from pathlib import Path
import numpy as np
import torch
from stage2_index_experiment import pca, sha


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=False);torch.set_num_threads(1)
    manifest=json.loads((args.data/'manifest.json').read_text());results=[]
    for domain in ['fashion','har','housing']:
        path=args.data/(domain+'.npz');data=dict(np.load(path))
        assert sha(path)==manifest['datasets'][domain]['sha256']
        for split in ['train','val','test']:
            assert np.isfinite(data['X_'+split]).all() and np.isfinite(data['y_'+split]).all()
            assert np.max(np.abs(np.linalg.norm(data['X_'+split],axis=1)-1))<1e-12
        if domain=='har':
            groups=[set(data['subject_'+split].tolist()) for split in ['train','val','test']]
            assert all(not groups[i]&groups[j] for i in range(3) for j in range(i))
        x=torch.tensor(data['X_train'],dtype=torch.float32)
        for seed in [101,201,202,203,204]:
            rng=np.random.default_rng(seed)
            w=torch.tensor(rng.standard_normal((128,x.shape[1])),dtype=torch.float32)
            h=torch.tanh(w@x.T)
            for count in [8,24]:
                basis,v,values,_=pca(h,count)
                error=float((basis.T@basis/len(x)-torch.eye(count)).abs().max())
                assert error<1e-5
                results.append(dict(domain=domain,seed=seed,C=count,float32_gram_error=error,
                                    selected_eigenvalue_ratio=float(values[-1]/values[0])))
    out=dict(status='pass',checks=len(results),maximum_float32_gram_error=max(r['float32_gram_error'] for r in results),
             minimum_selected_eigenvalue_ratio=min(r['selected_eigenvalue_ratio'] for r in results),results=results,
             sources={Path(__file__).name:sha(__file__)},manifest_sha256=sha(args.data/'manifest.json'))
    (args.out/'checks.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))


if __name__=='__main__':main()
