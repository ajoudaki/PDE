"""Final provenance and artifact checks for the completed thirty-degree run."""
import ast
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from ARC30_20260914_PREPARE import sha,ROOT,STUDY,GENERATED


def read(path):
    return json.loads(path.read_text())


def main(output):
    output=output.resolve()
    if output.parent!=GENERATED.resolve() or not output.name.startswith('ARC30_'):
        raise ValueError('Expected this study\'s ARC30 generated namespace')
    destination=output/'final_verification.json'
    if destination.exists():raise FileExistsError('Final verification already exists')
    campaign=read(output/'arc30_campaign.json');analysis=read(output/'arc30_comparison.json')
    network=read(output/'network_campaign.json');closure=read(output/'closure_campaign.json')
    figures=read(output/'figures/figures.json');independent=read(output/'independent_check.json')
    gates={}
    gates['all_16_runs_complete']=campaign['status']==analysis['status']==network['status']==closure['status']=='complete' and analysis['completed_run_count']==16
    gates['all_matrix_and_scalar_checks_pass']=analysis['validation_pass']
    gates['campaign_analysis_hash_match']=sha(output/'arc30_campaign.json')==analysis['campaign_sha256']
    gates['analysis_source_hash_match']=sha(STUDY/'ARC30_20260914_ANALYSIS.py')==analysis['source_sha256']
    gates['all_frozen_producer_sources_unchanged']=all(sha(STUDY/name)==value for name,value in campaign['launch_source_hashes'].items())
    gates['all_old_study_sources_preserved']=all(sha(STUDY/name)==value for name,value in campaign['old_study_sources'].items())
    gates['all_262_prior_generated_files_preserved']=len(campaign['preservation_manifest'])==262 and all(sha(ROOT/path)==value for path,value in campaign['preservation_manifest'].items())
    gates['figure_source_hash_match']=sha(STUDY/'ARC30_20260914_PLOTS.py')==figures['source_sha256']
    gates['figure_analysis_hash_match']=sha(output/'arc30_comparison.json')==figures['comparison_sha256']
    gates['all_14_figures_match']=len(figures['products'])==14 and all(sha(output/row['path'])==row['sha256'] for row in figures['products'])
    gates['independent_check_pass']=independent.get('status')=='passed'
    frozen=json.dumps(independent['frozen_calculation'],sort_keys=True,separators=(',',':'),allow_nan=False)
    gates['independent_calculation_still_frozen']=hashlib.sha256(frozen.encode()).hexdigest()==independent['frozen_calculation_sha256']
    comparison=independent['main_analysis_comparison']
    gates['independent_analysis_and_source_match']=(comparison['analysis_sha256']==sha(output/'arc30_comparison.json') and
        comparison['source_sha256']==sha(STUDY/'ARC30_20260914_CHECK.py') and comparison['status']=='passed' and comparison['scalar_value_count']==180)
    gates['figure_raw_sources_match']=all(sha(output/path)==value for path,value in figures['raw_gram_sha256'].items()) and sha(output/'inputs.npz')==figures['inputs_sha256']
    rows=[]
    for item in analysis['runs']:
        directory=output/item['family']/item['name'];record=read(directory/'record.json')
        checks=dict(record=sha(directory/'record.json')==item['record_sha256'],
                    gram=sha(directory/'gram.npy')==item['gram_sha256'],
                    scalars=sha(directory/'observations.npz')==item['observations_sha256'],
                    counts=record['gram_completed_observations']==206)
        rows.append(dict(family=item['family'],name=item['name'],checks=checks,
                         peak_allocated_bytes=record.get('peak_allocated_bytes',0)))
    gates['all_current_raw_hashes_match']=all(all(r['checks'].values()) for r in rows)
    resources=dict(network_worker_seconds=network['worker_wall_seconds'],closure_worker_seconds=closure['worker_wall_seconds'],
        longest_network_worker=max(r['wall_seconds'] for r in network['results']),
        longest_closure_worker=max(r['wall_seconds'] for r in closure['runs']),
        total_science_completion_upper_bound=campaign['scientific_completion_recorded_epoch']-campaign['experiment_started_epoch'],
        peak_gpu_allocated_bytes=max(r['peak_allocated_bytes'] for r in rows),
        generated_bytes_before_this_record=sum(p.stat().st_size for p in output.rglob('*') if p.is_file()))
    gates['resource_caps_pass']=(max(resources['network_worker_seconds'],resources['closure_worker_seconds'],resources['total_science_completion_upper_bound'])<2400 and
        max(resources['longest_network_worker'],resources['longest_closure_worker'])<600 and
        resources['peak_gpu_allocated_bytes']<18*1024**3 and resources['generated_bytes_before_this_record']<4*1024**3)
    gates['fixed_run_menu_no_failures']=len(network['results'])==len(closure['runs'])==8 and not network['unstarted'] and all(r['exit_code']==0 and not r['budget_stop'] for r in network['results']) and all(r['returncode']==0 for r in closure['runs'])
    gates['study_remains_flat']=not any(p.is_dir() for p in STUDY.iterdir())
    for path in STUDY.glob('ARC30_*.py'):ast.parse(path.read_text(),filename=str(path))
    gates['source_syntax_valid']=True
    links=[]
    for path in (STUDY/'README.md',STUDY/'ARC30_20260914_REPORT.md'):
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',path.read_text()):
            target=match.group(1).split('#')[0]
            if not target or '://' in target:continue
            resolved=(path.parent/target).resolve()
            links.append(dict(source=path.name,target=target,exists=resolved.exists() or resolved==destination))
    gates['all_report_readme_links_resolve']=all(r['exists'] for r in links)
    result=dict(status='passed' if all(gates.values()) else 'failed',created_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__),command=sys.argv,gates=gates,resources=resources,runs=rows,links=links,
        source_hashes={p.name:sha(p) for p in STUDY.glob('ARC30_*') if p.is_file()},
        readme_sha256=sha(STUDY/'README.md'),analysis_sha256=sha(output/'arc30_comparison.json'),
        independent_check_sha256=sha(output/'independent_check.json'),figures_sha256=sha(output/'figures/figures.json'),
        scientific_scope='Internally checked finite numerical comparison; refinement diagnostics are not error bounds and no H4 theorem applies to these broad arcs.')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],failed_gates=[k for k,v in gates.items() if not v],resources=resources),indent=2))
    if not all(gates.values()):raise SystemExit(1)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    main(parser.parse_args().output)
