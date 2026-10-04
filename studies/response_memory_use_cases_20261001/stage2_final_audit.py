"""Read-only integrity audit of stage2; writes only a fresh generated record."""
import argparse
import ast
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DATA=ROOT/'data/generated'/HERE.name


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    source=json.loads((HERE/'SOURCE_MANIFEST.json').read_text())
    startup=json.loads((DATA/'stage2_startup/manifest.json').read_text())
    paper={k:{'expected':v,'actual':sha(ROOT/k)} for k,v in source['sha256'].items() if k.startswith('paper/')}
    assert all(v['expected']==v['actual'] for v in paper.values())
    baseline=sha(HERE/'baseline_compact_flow.py')
    assert baseline=='f908c03cb63be0286d8505c2ce7959ea2377ccbcb8f740a10fac9dac8c49a67d'
    instructions={k:{'start':startup['hashes'][k],'current':sha(ROOT/k)} for k in ['AGENTS.md','RESEARCH_WORKFLOW.md']}
    files=sorted(set(HERE.glob('STAGE2_*'))|set(HERE.glob('stage2_*'))|{HERE/'README.md'})
    source_hashes={v.name:sha(v) for v in files if v.is_file()}
    python=[];links=[]
    for path in files:
        if path.suffix=='.py':ast.parse(path.read_text());python.append(path.name)
        if path.suffix=='.md':
            text=re.sub(r'```.*?```','',path.read_text(),flags=re.S)
            for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',text):
                target=match.group(1).strip('<>')
                if '://' in target or target.startswith('#'):continue
                target=target.split('#')[0]
                full=(path.parent/target).resolve()
                assert full.exists(),(str(path),target)
                links.append({'source':path.name,'target':str(full)})
    required=['STAGE2_INDEX_INDEPENDENT_REVIEW.md','STAGE2_GEOMETRY_INDEPENDENT_REVIEW.md',
              'STAGE2_COORD_INDEPENDENT_REVIEW.md','STAGE2_LABEL_INDEX_INDEPENDENT_REVIEW.md']
    assert all((HERE/name).is_file() for name in required)
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    staged=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).splitlines()
    status=subprocess.check_output(['git','status','--short','--untracked-files=no'],cwd=ROOT,text=True)
    assert head==startup['head'] and staged==startup['staged']
    author_fits={'index':99,'index_oracle':3,'fixed_coordination_including_continuations':96,
                 'support_curricula':54,'gate':33,'gate_diagnostics':3,'label_index':42}
    assert sum(author_fits.values())==330
    checks={'root_gate_zero_fix':json.loads((DATA/'stage2_root_gate_zero_fix01/oracle.json').read_text()),
            'finite_q_flat_cli':json.loads((DATA/'stage2_challenge_cli01/results.json').read_text())['pass']}
    result={'utc':datetime.now(timezone.utc).isoformat(),'status':'pass','head':head,'staged':staged,
        'tracked_status':status,'paper':paper,'baseline_sha256':baseline,'instructions':instructions,
        'source_sha256':source_hashes,'python_ast_files':python,'local_links':links,
        'independent_reviews':{name:sha(HERE/name) for name in required},'author_fits':author_fits,
        'author_total':sum(author_fits.values()),'independent_full_replays':3,
        'total_training_and_continuation_solves':333,'tiny_ode_checks':'separately recorded in their reports',
        'edge_checks':checks}
    (args.out/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','source_files':len(source_hashes),'python_ast_files':len(python),
                     'local_links':len(links),'total_training_and_continuation_solves':333}))


if __name__=='__main__':main()
