"""Compare all common saved J1/J2 initial contractions, without initialization."""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import json
import time
import numpy as np
from check_selective_order import TASKS,OLD,NEW,read,records,load_template,sha


def audit():
    rows=[];errors=[]
    for task in TASKS:
        old=records(OLD,task);new=records(NEW,task)
        if len(old)!=1 or len(new)!=1:continue
        old_meta=read(old[0]);new_meta=read(new[0])
        if not old_meta.get('data_file') or not new_meta.get('data_file'):
            rows.append({'task':task,'status':'no_saved_initial_comparison','passed':not new_meta.get('fitted',False)});continue
        try:
            a,_,_=load_template(old_meta);b,_,_=load_template(new_meta)
            with np.load(old[0].parent/old_meta['data_file'],allow_pickle=False) as da,np.load(new[0].parent/new_meta['data_file'],allow_pickle=False) as db:
                q1=da['initial_state'];q2=db['initial_state'];c1=da['core_ids'];c2=db['core_ids'];p1=da['passive_ids'];p2=db['passive_ids']
                core2={int(v):i for i,v in enumerate(c2)};passive2={int(v):i for i,v in enumerate(p2)}
                map_core=np.array([core2[b.tree_ids[a.trees[int(v)]]] for v in c1])
                map_passive=np.array([passive2[b.tree_ids[a.trees[int(v)]]] for v in p1])
                panel1=q1[len(c1):-1].reshape(-1,len(p1));panel2=q2[len(c2):-1].reshape(-1,len(p2))
                initial_core2=q2[map_core];initial_passive2=panel2[:,map_passive]
                core_error=float(np.max(np.abs(q1[:len(c1)]-initial_core2)))
                passive_error=float(np.max(np.abs(panel1-initial_passive2)))
                clock_error=float(abs(q1[-1]-q2[-1]));angles_equal=np.array_equal(da['all_query_angles'],db['all_query_angles'])
                checks={'all_q1_trees_present':set(a.trees)<=set(b.trees),'all_common_core_and_passive_classifications_preserved':len(map_core)==len(c1) and len(map_passive)==len(p1),'query_panels_identical':angles_equal,'all_common_core_initial_values_match':core_error<=1e-13,'all_common_passive_initial_values_match':passive_error<=1e-13,'clock_initial_values_match':clock_error<=1e-13}
                rows.append({'task':task,'passed':all(checks.values()),'checks':checks,'compared_core_entries':len(c1),'compared_passive_entries':int(panel1.size),'compared_passive_queries':len(panel1),'compared_total_initial_entries':len(c1)+int(panel1.size)+1,'core_max_absolute_error':core_error,'passive_max_absolute_error':passive_error,'clock_absolute_error':clock_error,'core_bitwise_equal':np.array_equal(q1[:len(c1)],initial_core2),'passive_bitwise_equal':np.array_equal(panel1,initial_passive2),'clock_bitwise_equal':bool(q1[-1]==q2[-1]),'tolerance':1e-13})
        except Exception as exc:errors.append({'task':task,'error':repr(exc)})
    return {'audited_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(__file__),'scope':'Every common saved initial scalar, including all64circle queries and trainingaliases; no initialization orODE rerun','recorded_tasks':len(rows),'complete':len(rows)==3,'passed':not errors and all(r['passed'] for r in rows),'errors':errors,'results':rows}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--watch',action='store_true');parser.add_argument('--deadline',type=float,default=time.time()+720);args=parser.parse_args()
    output=NEW/'checks';output.mkdir(parents=True,exist_ok=True)
    while True:
        result=audit();(output/'common_initialization_audit.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:result[k] for k in ('audited_utc','recorded_tasks','complete','passed','errors')}),flush=True)
        if not args.watch or result['complete'] or time.time()>=args.deadline:break
        time.sleep(30.)
