import argparse,json
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('root');p.add_argument('--out');p.add_argument('--repeated',action='store_true');a=p.parse_args();root=Path(a.root);rows=[]
for folder in sorted(root.iterdir()):
    if not (folder/'summary.json').exists():continue
    s=json.loads((folder/'summary.json').read_text());ref=root/f'dense_s{s["seed"]}'/'predictions.npz'
    if not ref.exists():continue
    z=np.load(folder/'predictions.npz');d=np.load(ref);times=[t for t in (list(range(16,257,16)) if a.repeated else [8,16,32,64,128,256]) if t in z['times'] and t in d['times']]
    errs=[float(np.sqrt(np.mean((z['predictions'][np.where(z['times']==t)[0][0]]-d['predictions'][np.where(d['times']==t)[0][0]])**2))) for t in times]
    rows.append(dict(name=folder.name,seed=s['seed'],method=s['method'],mean_grid_discrepancy=float(np.mean(errs)),errors=dict(zip(map(str,times),errs)),train_rms=s['snapshots'][-1]['train_rms'],accuracy=s['snapshots'][-1]['accuracy'],writes=s['dense_write_events'],seconds=s['seconds'],materialization_flops=s['materialization_flops'],status=s['status']))
for r in rows:print(f'{r["name"]:28s} err={r["mean_grid_discrepancy"]:.6g} rms={r["train_rms"]:.4g} acc={r["accuracy"]:.3f} writes={r["writes"]} sec={r["seconds"]:.2f}')
if a.out:Path(a.out).write_text(json.dumps(rows,indent=2))
