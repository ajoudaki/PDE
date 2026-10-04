"""Turn frozen branch rules and saved analysis into explicit follow-up configs."""
from pathlib import Path
import argparse
import copy
import json

HERE=Path(__file__).resolve().parent
BASE=[json.loads((HERE/f'gpu_multidata_baseline_{i}.json').read_text()) for i in (0,1)]
DATA={k:v for c in BASE for k,v in c['datasets'].items()}


def write(stage, suffix, cases, samplers, budget_seconds, dataset_overrides=None, **changes):
    config=copy.deepcopy(BASE[0])
    config.update(stage=stage, description=f'Prespecified {stage} branch, {suffix}',
                  cases=cases, samplers=samplers, budget_seconds=budget_seconds, **changes)
    config['datasets']={c['dataset_id']:copy.deepcopy(DATA[c['dataset_id']]) for c in cases}
    if dataset_overrides:
        config['datasets'].update(dataset_overrides)
    config['source_files'].append('studies/closure_sampling_20261003/make_gpu_multidata_followups.py')
    target=HERE/f'gpu_multidata_{stage}_{suffix}.json'
    if target.exists():raise FileExistsError(target)
    target.write_text(json.dumps(config,indent=2,allow_nan=False)+'\n')
    print(target)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stage',choices=['diagnostic','confirmation','refinement'],required=True)
    parser.add_argument('--analysis',required=True)
    parser.add_argument('--budget-seconds',type=float,default=400.)
    args=parser.parse_args()
    summary=json.loads(Path(args.analysis).read_text())
    if args.stage=='diagnostic':
        groups=[g for g in summary['group_recommendations'] if g['diagnostic_case']]
        if not summary['baseline_complete_cases']==72:
            raise ValueError('diagnostic selection requires complete baseline')
        samplers=[dict(name='budget2_rank16',coefficient_multiplier=2.,rank=16),
                  dict(name='budget2_rank24',coefficient_multiplier=2.,rank=24),
                  dict(name='budget4_rank32',coefficient_multiplier=4.,rank=32)]
        for i in (0,1):
            cases=[g['diagnostic_case'] for g in groups[i::2]]
            if cases:write(args.stage,str(i),cases,samplers,args.budget_seconds)
    elif args.stage=='confirmation':
        for g in summary['group_recommendations']:
            candidate=g['selected_candidate']
            if not candidate or not g['confirmation_required']:continue
            samplers=[dict(name=f"budget{candidate['factor']:g}_rank{candidate['rank']}",
                coefficient_multiplier=candidate['factor'],rank=candidate['rank'])]
            write(args.stage,g['group'],g['confirmation_required'],samplers,args.budget_seconds)
    else:
        from make_gpu_multidata_configs import query_panel
        for row in summary['required_refinement_cases']:
            case={key:row[key] for key in ('dataset_id','n','seed')}
            dataset=copy.deepcopy(DATA[row['dataset_id']])
            dataset['query_panel']=query_panel(len(dataset['U'][0]),refined=True).tolist()
            samplers=[dict(name=row['model'],coefficient_multiplier=row['factor'],rank=row['rank'])]
            write(args.stage,row['domain'],[case],samplers,args.budget_seconds,
                  dataset_overrides={row['dataset_id']:dataset},dt=.1,observe_every=.5,
                  horizon=row['last_time'],max_horizon=row['last_time'])


if __name__=='__main__':main()
