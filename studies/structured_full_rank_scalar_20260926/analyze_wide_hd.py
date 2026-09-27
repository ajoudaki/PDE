"""Absolute fitted-function RMS comparisons for the width2048 campaign."""
import argparse,hashlib,json,csv
from pathlib import Path
import numpy as np
from circle_tasks import TASKS


def digest(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def rms(x):return float(np.sqrt(np.mean(x*x)))

def read(root, *, seeds=None, allow_stopped=False):
 root=Path(root);manifest=json.loads((root/'manifest.json').read_text())
 if (root/'completion.json').exists():
  complete=json.loads((root/'completion.json').read_text())
  if complete['completed']!=complete['total']:raise ValueError('incomplete campaign')
 elif not (allow_stopped and (root/'STOPPED.json').exists()):
  raise ValueError('campaign incomplete without explicit stopped-run selection')
 index=json.loads((root/'artifact_hashes.json').read_text());records={}
 for p in sorted(root.glob('*__n*__s*.json')):
  if digest(p)!=index[p.name]:raise ValueError('JSON hash mismatch')
  d=json.loads(p.read_text());ident=(d['task'],d['seed'],d['method'])
  if seeds is not None and d['seed'] not in seeds:continue
  if d['status']=='ok':
   q=root/d['data_file']
   if digest(q)!=d['data_sha256'] or d['data_sha256']!=index[q.name]:raise ValueError('data hash mismatch')
   with np.load(q) as a:
    d['prediction']=a['prediction'].copy()
    loss=float(np.mean((a['train_prediction']-a['train_labels'])**2))
    if not np.isclose(loss,d['train_mse'],rtol=1e-8,atol=1e-12):raise ValueError('MSE mismatch')
  records[ident]=d
 if seeds is not None:
  manifest=dict(manifest,seeds=seeds)
  for task in manifest['tasks']:
   for seed in seeds:
    for method in manifest['methods']:
     if (task,seed,method) not in records:raise ValueError('selected comparison set is incomplete')
 return manifest,records

def main():
 p=argparse.ArgumentParser();p.add_argument('--base',required=True)
 p.add_argument('--refinement',nargs='*',default=[]);p.add_argument('--output',required=True)
 p.add_argument('--seeds',nargs='+',type=int);p.add_argument('--allow-stopped',action='store_true')
 a=p.parse_args();out=Path(a.output);out.mkdir(parents=True,exist_ok=False)
 manifest,runs=read(a.base,seeds=a.seeds,allow_stopped=a.allow_stopped);refinement=[];bad=set()
 for name in a.refinement:
  fm,rr=read(name)
  for field in ('width','target','grid'):
   if fm[field]!=manifest[field]:raise ValueError('refinement '+field+' differs')
  if not set(fm['tasks']).issubset(manifest['tasks']) or not set(fm['seeds']).issubset(manifest['seeds']):raise ValueError('refinement task/seed mismatch')
  for key,fine in rr.items():
   coarse=runs.get(key);ok=bool(coarse and coarse['status']=='ok' and fine['status']=='ok' and coarse['fitted'] and fine['fitted'])
   delta=rms(coarse['prediction']-fine['prediction']) if ok else None
   row={'task':key[0],'seed':key[1],'method':key[2],'both_fitted':ok,'function_rms_change':delta,'passed':bool(ok and delta<=1e-3)}
   refinement.append(row)
   if not row['passed']:bad.add(key)
 per_seed=[];summary=[];rng=np.random.default_rng(0)
 for task in manifest['tasks']:
  rows=[]
  for seed in manifest['seeds']:
   keys=[(task,seed,m) for m in ('gaussian','gaussian_control','hd')]
   rs=[runs.get(k) for k in keys]
   fit=all(r and r['status']=='ok' and r['fitted'] for r in rs)
   row={'task':task,'seed':seed,'all_fitted':fit}
   if fit:
    g,g2,hd=[r['prediction'] for r in rs]
    ds=[rms(hd-g),rms(g2-g)]
    grid=max(abs(ds[0]-rms((hd-g)[::2])),abs(ds[1]-rms((g2-g)[::2])))
    valid=grid<=1e-4 and all(r['max_loss_rise']<=1e-7 for r in rs) and not any(k in bad for k in keys)
    row.update(HD_G=ds[0],G2_G=ds[1],paired_difference=ds[0]-ds[1],
      grid_delta=grid,numerically_valid=valid,hd_grid_max=float(np.max(abs(hd-g))),
      gaussian_time=rs[0]['time'],control_time=rs[1]['time'],hd_time=rs[2]['time'],
      max_train_mse=max(r['train_mse'] for r in rs))
    rows.append(row)
   per_seed.append(row)
  s={'task':task,'expected_seeds':len(manifest['seeds']),'fitted_pairs':len(rows),
     'numerically_valid_pairs':sum(x['numerically_valid'] for x in rows)}
  if rows:
   for field in ('HD_G','G2_G','paired_difference'):
    vals=np.array([r[field] for r in rows]);s[field+'_mean']=float(vals.mean())
    s[field+'_std']=float(vals.std(ddof=1)) if len(vals)>1 else None
    s[field+'_min']=float(vals.min());s[field+'_max']=float(vals.max())
    idx=rng.integers(len(vals),size=(20000,len(vals)))
    lo,hi=np.quantile(vals[idx].mean(1),[.025,.975]);s[field+'_ci']=[float(lo),float(hi)] if len(vals)>1 else None
  summary.append(s)
 result={'metric':'sqrt((1/(2pi))*integral_circle (f_candidate-f_Gaussian)^2)',
  'width':manifest['width'],'seeds':manifest['seeds'],'selected_stopped_campaign':a.allow_stopped,'target_train_mse':manifest['target'],
  'refinements':refinement,'task_summary':summary,'per_seed':per_seed,
  'all_runs':len(runs),'fit_runs':sum(r.get('fitted',False) for r in runs.values()),
  'failed_runs':sum(r['status']!='ok' for r in runs.values()),
  'max_loss_rise':max((r.get('max_loss_rise',0) for r in runs.values()),default=0),
  'source_manifest_sha256':digest(Path(a.base)/'manifest.json')}
 (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
 keys=list(dict.fromkeys(k for r in per_seed for k in r))
 with (out/'per_seed.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(per_seed)
 lines=[f"# Width{manifest['width']} fitted circle-function comparison",'',
 'Absolute RMS of the predicted-function difference around the circle. No signal-amplitude normalization. Means over paired seeds; both networks reach the user-specified MSE<=1e-4. Gaussian control changes only the middle draw.','',
 '| Task | HD–Gaussian mean | Gaussian–Gaussian mean | Mean paired difference [95% CI] | Fitted / expected | Numerically valid |',
 '|---|---:|---:|---|---:|---:|']
 for s in summary:
  if 'HD_G_mean' in s:
   interval=s['paired_difference_ci']
   ci=f'[{interval[0]:.6f}, {interval[1]:.6f}]' if interval else '(one paired seed; no CI)'
   values=f"{s['HD_G_mean']:.6f} | {s['G2_G_mean']:.6f} | {s['paired_difference_mean']:.6f} {ci}"
  else:values='unresolved | unresolved | unresolved'
  lines.append(f"| {s['task']} | {values} | {s['fitted_pairs']}/{s['expected_seeds']} | {s['numerically_valid_pairs']} |")
 lines+=['','Intervals are per-task paired-seed bootstrap intervals, not simultaneous guarantees. Any missing fitted pair or numerical warning is retained explicitly. Means including a numerically flagged triple are descriptive and unvalidated; see the valid-count column. This is a finite-width experiment, not a proof identifying the infinite-width limit.','',f'Numerical refinement records: {len(refinement)}; failed checks: {sum(not x["passed"] for x in refinement)}.','']
 (out/'report.md').write_text('\n'.join(lines))
 print(json.dumps({k:result[k] for k in ['width','all_runs','fit_runs','failed_runs','max_loss_rise']},indent=2))

if __name__=='__main__':main()
