"""Supervisor's predeclared wider-network gate; never launches training."""
import hashlib,json,time,shutil
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[2]

def decide(campaign):
    c=Path(campaign).resolve();a=c.parent/'campaign_001/analysis_final';hashes={}
    def load(p,key):
        hashes[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
        with np.load(p,allow_pickle=False) as z:return z[key].copy()
    nets={n:np.stack([load(c/f'pair_d30_n{n}_s{s}_main/observations.npz','dense_predictions') for s in [1729,2718,3141]]) for n in [1024,4096]}
    means={n:v.mean(0) for n,v in nets.items()}
    shift=float(np.linalg.norm(means[1024]-means[4096])/np.linalg.norm(means[4096]))
    closures={N:load(a/f'pair_d30_r45_N{N}_main.npz','learned_final') for N in [1,3,5]}
    mse={N:np.mean((nets[4096]-f)**2,axis=1) for N,f in closures.items()}
    low,high=3,5;gain=mse[low]-mse[high]
    # If the raw >=10% improvement requirement already fails, the stronger
    # seed/control gate necessarily fails too. No missing control is invented.
    failed_improvement=float(gain.mean())<.1*float(mse[low].mean())
    recommendation=shift>.01 or failed_improvement
    elapsed=time.time()-json.loads((c/'clock.json').read_text())['start'];remaining=1200-elapsed
    used=sum(p.stat().st_size for p in c.rglob('*') if p.is_file());free=shutil.disk_usage(c).free
    # Branch retains one8192 float32 matrix (~256MiB) and three curve records.
    reserve=280*2**20
    all_main_complete=json.loads((c/'main_batch.json').read_text())['missing']==[]
    allowed=recommendation and remaining>=480 and used+reserve<650*2**20 and free-reserve>=1.5*2**30 and all_main_complete
    result=dict(widen_recommended=recommendation,launch_allowed=allowed,width_mean_relative_rms=shift,
        failed_N3_to_N5_10percent_improvement=failed_improvement,per_seed_MSE={str(k):v.tolist() for k,v in mse.items()},
        mean_MSE_gain_N3_to_N5=float(gain.mean()),remaining_scientific_seconds=remaining,used_MiB=used/2**20,free_GiB=free/2**30,
        branch_expected_reserve_MiB=280,input_hashes=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        interpretation='Negative/insufficient raw gain already fails the full improvement gate; branch fixed in NET_PLAN before training.')
    p=c/'wide_decision.json'
    with p.open('x') as f:json.dump(result,f,indent=2)
    return result

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);args=p.parse_args();print(json.dumps(decide(args.campaign)))
