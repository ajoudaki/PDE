"""Produce report tables and static research figures from frozen route JSON."""
import csv,datetime,hashlib,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
DATA=HERE.parents[1]/'data/generated/response_memory_use_cases_20261001'
OUT=DATA/'hypergradient_summary';OUT.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text())
main=[]
for dirname in ['hypergradient_pilot101','hypergradient_pilot102_103','hypergradient_confirm201_205','hypergradient_second301']:
 for p in sorted((DATA/dirname).glob('seed*_summary.json')):
    s=read(p);s['source_directory']=dirname;main.append(s)
main.sort(key=lambda s:s['seed'])
convex={r['seed']:r for path in [DATA/'hypergradient_convex128/convex.json',DATA/'hypergradient_convex512/convex.json'] for r in read(path)['rows']}
rows=[];table=['| Phase / n / seed | Original | Dense design | q1 design | Frozen Adam design | Frozen convex design | Dense benefit retained | h1 / h2 movement | Dense–frozen RMS |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for s in main:
 d={a['kind']:a for a in s['designs']};base=s['original_dense_test_mse'];dense=d['dense']['dense_test_mse'];q=d['q1']['dense_test_mse'];frozen=d['frozen']['dense_test_mse'];ret=(base-q)/(base-dense);phase='pilot' if s['seed']<200 else ('confirm' if s['seed']<300 else 'stress')
 row=dict(phase=phase,width=s['width'],seed=s['seed'],original_dense_mse=base,dense_design_mse=dense,q1_design_mse=q,frozen_adam_design_mse=frozen,frozen_convex_design_mse=convex.get(s['seed'],{}).get('dense_test_mse'),benefit_retained=ret,feature_movement_h1=s['feature_movement'][0],feature_movement_h2=s['feature_movement'][1],dense_frozen_rms=s['dense_frozen_prediction_rms'],q1_error_ratio=q/base,q1_frozen_ratio=q/frozen,source_directory=s['source_directory'])
 row['pass']=q/base<=.8 and ret>=.8 and q/frozen<=.9 and min(s['feature_movement'])>=.05 and s['dense_frozen_prediction_rms']>=.05
 row['q1_refined_mse']=d['q1']['refined_dense_test_mse'];row['original_refined_mse']=d['q1']['refined_original_dense_test_mse'];row['q1_refinement_effect_over_benefit']=abs(row['q1_refined_mse']-q)/(base-q)
 rows.append(row);c='—' if row['frozen_convex_design_mse'] is None else f"{row['frozen_convex_design_mse']:.5f}"
 table.append(f"| {phase} / {s['width']} / {s['seed']} | {base:.5f} | {dense:.5f} | {q:.5f} | {frozen:.5f} | {c} | {100*ret:.2f}% | {s['feature_movement'][0]:.3f} / {s['feature_movement'][1]:.3f} | {s['dense_frozen_prediction_rms']:.3f} |")
with (OUT/'results.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
(OUT/'results_table.md').write_text('\n'.join(table)+'\n')
mem=read(DATA/'hypergradient_memory_warm/memory.json')['rows']
mt=['| Width | Method | Reverse strategy | Total peak MiB | Incremental peak MiB | Seconds / gradient | Moving scalars | Fixed matrix scalars |','|---:|---|---|---:|---:|---:|---:|---:|']
for r in mem:mt.append(f"| {r['width']} | {r['kind']} | {r['strategy']} | {r['peak_allocated_bytes']/2**20:.2f} | {r['incremental_peak_bytes']/2**20:.2f} | {r['seconds']:.3f} | {r['moving_coordinates']} | {r['fixed_source_coordinates']} |")
(OUT/'memory_table.md').write_text('\n'.join(mt)+'\n')
conf=[r for r in rows if r['phase']=='confirm'];stats=dict(confirm_passes=sum(r['pass'] for r in conf),confirm_median_retained=float(np.median([r['benefit_retained'] for r in conf])),confirm_median_q1_error_ratio=float(np.median([r['q1_error_ratio'] for r in conf])),confirm_median_frozen_ratio=float(np.median([r['q1_frozen_ratio'] for r in conf])),max_q1_refinement_effect_over_benefit=max(r['q1_refinement_effect_over_benefit'] for r in rows),designs=sum(len(s['designs']) for s in main),outer_optimization_solves=24*sum(len(s['designs']) for s in main),conservative_all_inner_solves=1095)
mainseconds=sum(read(DATA/name/'run.json')['seconds'] for name in ['hypergradient_pilot101','hypergradient_pilot102_103','hypergradient_confirm201_205','hypergradient_second301'])
otherseconds=0
for name,file in [('hypergradient_check_01','checks.json'),('hypergradient_gate_01','gate.json'),('hypergradient_validation_02','validation.json'),('hypergradient_convex128','convex.json'),('hypergradient_convex512','convex.json'),('hypergradient_memory','memory.json'),('hypergradient_memory_warm','memory.json')]:
 r=read(DATA/name/file);otherseconds+=(datetime.datetime.fromisoformat(r['end_utc'])-datetime.datetime.fromisoformat(r['start_utc'])).total_seconds()
stats.update(recorded_main_seconds=mainseconds,recorded_audit_seconds=otherseconds,recorded_compute_minutes=(mainseconds+otherseconds)/60)
(OUT/'summary.json').write_text(json.dumps(dict(statistics=stats,rows=rows),indent=2))
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
fig,axes=plt.subplots(1,3,figsize=(13.3,3.8))
ax=axes[0]
for s in main[:3]:
 d={a['kind']:a for a in s['designs']};base=s['original_dense_test_mse'];ax.plot([1,2,4,8],[d[f'q{q}']['dense_test_mse']/base for q in [1,2,4,8]],'o-',lw=1.2,label=f"seed {s['seed']}")
ax.set(xlabel='Memory order q',ylabel='Dense test MSE / original-label MSE',title='Label design: width 128 pilots',xticks=[1,2,4,8]);ax.legend(frameon=False,fontsize=8)
ax=axes[1];x=np.arange(5)
for key,label,color,offset in [('original_dense_mse','Original labels','#777777',-.27),('dense_design_mse','Dense design','#242424',-.09),('q1_design_mse','Memory q=1 design','#247A9E',.09),('frozen_adam_design_mse','Frozen design','#BC6D32',.27)]:
 ax.bar(x+offset,[r[key] for r in conf],width=.17,label=label,color=color)
ax.set(xticks=x,xticklabels=[str(r['seed']) for r in conf],xlabel='Fresh initialization seed',ylabel='Dense retraining test MSE',title='Confirmation: width 512');ax.legend(frameon=False,fontsize=7)
ax=axes[2];m=[r for r in mem if r['width']==512];labels=['Dense\nfull','Dense\ncheckpoint16','Memory q=1\nfull','Memory q=1\ncheckpoint16'];colors=['#777777','#242424','#77B5CF','#247A9E']
ax.bar(np.arange(4),[r['peak_allocated_bytes']/2**20 for r in m],color=colors);ax.set(xticks=np.arange(4),xticklabels=labels,ylabel='Measured peak CUDA allocation (MiB)',title='One hypergradient: width 512');ax.tick_params(axis='x',labelsize=8)
fig.tight_layout();fig.savefig(OUT/'hypergradient_results.pdf',bbox_inches='tight');fig.savefig(OUT/'hypergradient_results.png',bbox_inches='tight');plt.close(fig)
print(json.dumps(stats,indent=2))
print('\n'.join(mt))
