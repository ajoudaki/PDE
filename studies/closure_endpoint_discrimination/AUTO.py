"""Continue the fixed trajectories in common 100-unit blocks within the budget."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

import ADVANCE
from ANALYZE import analyze_confirmation
from VERIFY import verify
import RETIRE

HERE=Path(__file__).resolve().parent


def write(path,value):
    with Path(path).open('x') as f:json.dump(value,f,indent=2,allow_nan=False)


def retire_authorized(campaign,previous,current,old_report,new_report):
    authorization=campaign/'stage_05/continuing_cleanup_authorization.json'
    if not authorization.exists():raise RuntimeError('Ongoing cleanup authorization is required')
    receipts=[]
    for name,path in previous['jobs'].items():
        if json.loads((Path(path)/'record.json').read_text())['config']['kind']!='network':continue
        prepared=RETIRE.prepare(Path(path)/'state.pt',Path(current['jobs'][name])/'state.pt',old_report,new_report)
        receipts.append(RETIRE.execute(prepared['descriptor']))
    return receipts


def analyze(manifest,report_path):
    outputs={}
    for pair in ([1,3],[3,5]):
        item=dict(manifest,pair=pair,correctness=str(report_path))
        result=analyze_confirmation(item)
        outputs['-'.join(map(str,pair))]=result
    return outputs


def run(campaign,previous_path,verification_path):
    campaign=Path(campaign).resolve();previous_path=Path(previous_path).resolve();verification_path=Path(verification_path).resolve()
    start=json.loads((campaign/'compute_start.json').read_text())['unix_time']
    budget=json.loads((campaign/'manifest.json').read_text())['budget']['scientific_seconds']
    outcome='unresolved';reason=None;latest=previous_path
    while True:
        previous=json.loads(previous_path.read_text());now=float(previous['common_time'])
        if now>=1600:reason='horizon_cap';break
        if time.time()-start>budget-120:reason='insufficient_time_for_another_complete_validated_block';break
        target=now+100;profile=f'common_{int(target):04d}'
        ADVANCE.advance(campaign,5,previous_path,target,profile)
        folder=campaign/'stage_05'/profile
        write(folder/'supervisor.json',dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    command=[sys.executable,*sys.argv],previous=str(previous_path)))
        command=[sys.executable,'-B',str(HERE/'BATCH.py'),'--campaign',str(campaign),'--jobs',str(folder/'jobs.json')]
        print(json.dumps(dict(event='common_block',time=target)),flush=True)
        with (folder/'dispatcher.log').open('x') as log:
            result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
        if result.returncode:reason='dispatcher_failed_or_budget_exhausted';break
        next_path=campaign/'stage_05'/f'manifest_{int(target):04d}.json'
        current=ADVANCE.collect(campaign,5,[profile],next_path,previous_path)
        report_path=campaign/'stage_05'/f'verification_{int(target):04d}.json'
        report=verify(next_path,replay='all',device='cuda:0');write(report_path,report)
        if not report['passed']:reason='verification_failure';break
        results=analyze(current,report_path)
        result_path=campaign/'stage_05'/f'analysis_{int(target):04d}.json';write(result_path,results)
        summary={key:dict(validated=value['validated_separation'],settled=value['all_settled'],
                    numerical_passed=value['numerical_passed'],
                    selected=value['adjacent_pairs'][key],uncertainty=value['uncertainty']) for key,value in results.items()}
        print(json.dumps(dict(event='checkpoint_analysis',time=target,results=summary)),flush=True)
        latest=next_path
        # The user subsequently explicitly authorized ongoing verified cleanup.
        write(folder/'retirement_results.json',retire_authorized(campaign,previous,current,verification_path,report_path))
        focused=None
        if (HERE/'FOCUSED.py').exists():
            from FOCUSED import evaluate_focus
            focused=evaluate_focus(current,report_path)
            write(campaign/'stage_05'/f'focused_{int(target):04d}.json',focused)
            print(json.dumps(dict(event='focused_pair',time=target,passed=focused['focused_separation'],
                  settled=focused['all_compared_settled'],uncertainty=focused['uncertainty'])),flush=True)
            if focused['focused_separation']:outcome='adaptive_focused_pair_success';reason=None;break
        if any(value['validated_separation'] for value in results.values()):outcome='validated_success';reason=None;break
        if all(value['all_settled'] for value in results.values()):reason='settled_but_separation_or_numerical_gates_failed';break
        if 'cl_N5_finest' not in current['jobs'] and results['3-5']['numerical_controls']['quadrature_N5']['circle_max']>.025:
            reason='permitted_N5_final_quadrature_refinement_required';break
        previous_path,verification_path=next_path,report_path
    result=dict(outcome=outcome,reason=reason,latest_complete_manifest=str(latest),elapsed_seconds=time.time()-start)
    path=campaign/'stage_05'/f'auto_result_after_{int(json.loads(latest.read_text())["common_time"]):04d}.json'
    write(path,result);print(json.dumps(dict(event='auto_finished',**result)),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--campaign',required=True);p.add_argument('--previous',required=True);p.add_argument('--verification',required=True)
    a=p.parse_args();run(a.campaign,a.previous,a.verification)
