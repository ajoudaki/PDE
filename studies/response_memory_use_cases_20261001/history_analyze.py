"""Produce repair tables/figure from every frozen confirmation and control."""
import csv
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'data/generated/response_memory_use_cases_20261001'
OUT=BASE/'history_summary'
OUT.mkdir(exist_ok=False)
rows=[]
controls={r['seed']:r for r in json.loads((BASE/'history_controls01/results.json').read_text())}
for p in sorted((BASE/'history_confirm01').glob('seed*_repair.json')):
    d=json.loads(p.read_text());r=d['repair'];seed=d['seed'];base=r['no_edit']['after_clean']['test_mse']
    row={'seed':seed,**{k:v['after_clean']['test_mse'] for k,v in r.items()}}
    row['q4_reduction']=1-row['moment_q4']/base
    row['q4_vs_exact_difference']=row['moment_q4']-row['exact_history']
    row['q4_operator_relative_error']=next(v['bad_relative_error'] for v in d['projection'] if v['q']==4)
    row['online_offline_error']=d['online_offline_memory_relative_error']
    c=controls[seed]
    row['line_history']=c['history']['selected']['after_clean']['test_mse']
    row['line_gradient']=c['current_gradient']['selected']['after_clean']['test_mse']
    row['extra_cleanup']=c['extra_cleanup']['after_clean']['test_mse']
    rows.append(row)
with (OUT/'results.csv').open('w') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
summary={'seeds':[r['seed'] for r in rows],
         'median_q4_reduction':float(np.median([r['q4_reduction'] for r in rows])),
         'range_q4_reduction':[min(r['q4_reduction'] for r in rows),max(r['q4_reduction'] for r in rows)],
         'q4_positive':sum(r['q4_reduction']>0 for r in rows),
         'q4_over_10_percent':sum(r['q4_reduction']>=.1 for r in rows),
         'max_q4_exact_test_mse_difference':max(abs(r['q4_vs_exact_difference']) for r in rows),
         'max_q4_operator_relative_error':max(r['q4_operator_relative_error'] for r in rows),
         'max_online_offline_error':max(r['online_offline_error'] for r in rows),
         'line_history_beats_line_gradient':sum(r['line_history']<r['line_gradient'] for r in rows),
         'line_history_beats_extra_cleanup':sum(r['line_history']<r['extra_cleanup'] for r in rows)}
(OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
fig,axes=plt.subplots(1,2,figsize=(10,3.7),constrained_layout=True)
names=['no_edit','current_gradient','moment_q1','moment_q4','exact_history']
labels=['Clean training','Current gradient\n+ clean training','History q=1\n+ clean training','History q=4\n+ clean training','Exact history\n+ clean training']
for r in rows:axes[0].plot(range(5),[r[n]/r['no_edit'] for n in names],'-o',alpha=.7,lw=1)
axes[0].axhline(1,color='grey',ls=':',lw=1)
axes[0].set_xticks(range(5),labels,fontsize=8)
axes[0].set_ylabel('Test MSE / clean-training MSE')
axes[0].set_title('Historical repair: five fresh initializations')
names2=['line_gradient','line_history','extra_cleanup']
labels2=['Gradient line search\n+ T=2 cleanup','History line search\n+ T=2 cleanup','No edit\n+ T=2.5 cleanup']
for r in rows:axes[1].plot(range(3),[r[n]/r['no_edit'] for n in names2],'-o',alpha=.7,lw=1)
axes[1].axhline(1,color='grey',ls=':',lw=1)
axes[1].set_xticks(range(3),labels2,fontsize=8)
axes[1].set_title('Stronger controls qualify the practical benefit')
axes[1].set_ylabel('Test MSE / T=2 clean-training MSE')
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=.2)
fig.savefig(OUT/'history_repair.pdf');fig.savefig(OUT/'history_repair.png',dpi=180)
inputs=list((BASE/'history_confirm01').glob('seed*_repair.json'))+[BASE/'history_controls01/results.json']
(OUT/'manifest.json').write_text(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
   'outputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.iterdir() if p.is_file()}},indent=2)+'\n')
print(json.dumps(summary,indent=2))
