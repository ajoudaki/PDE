"""Fixed paired comparison for the final population-index candidate."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    rows=json.loads((args.input/'results.json').read_text())
    out={'input_sha256':hashlib.sha256((args.input/'results.json').read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'fits':len(rows),'seconds':sum(v['seconds'] for v in rows),'domains':{},'refinements':[]}
    for domain in ['fashion','har','housing']:
        rr=[v for v in rows if v['domain']==domain and v['dt']==1/64]
        by={(v['seed'],v['kind']):v for v in rr};entry={}
        for kind in ['population_q1','population_matched','factor']:
            vv=[v for v in rr if v['kind']==kind]
            entry[kind]={'median_test_rmse':float(np.median([v['selected']['test'] for v in vv])),
                         'per_seed_test_rmse':[v['selected']['test'] for v in vv]}
        for kind in ['population_q1','population_matched']:
            ratios=[by[(s,kind)]['selected']['test']/by[(s,'factor')]['selected']['test'] for s in [4501,4502,4503,4504]]
            entry[kind].update({'paired_ratios':ratios,'median_ratio':float(np.median(ratios)),
                               'wins':sum(v<1 for v in ratios)})
        e=entry['population_matched'];entry['domain_pass']=e['median_ratio']<=.95 and e['wins']>=3
        out['domains'][domain]=entry
        for kind in ['population_matched','factor']:
            a=by[(4501,kind)];b=next(v for v in rows if v['domain']==domain and v['dt']==1/128 and v['kind']==kind)
            out['refinements'].append({'domain':domain,'kind':kind,'rmse_change':abs(a['selected']['test']-b['selected']['test']),
                                      'times':[a['selected']['time'],b['selected']['time']]})
    out['practical_gate']=sum(v['domain_pass'] for v in out['domains'].values())>=2 and all(
        v['population_matched']['median_ratio']<=1.05 for v in out['domains'].values())
    (args.out/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'fits':len(rows),'gate':out['practical_gate'],'seconds':out['seconds']}))


if __name__=='__main__':main()
