"""Verify final Gram evidence, provenance, resource bounds and preservation."""
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
BASE = ROOT / 'data/generated/wide_network_closure_comparison/GRAM_20260914_v1'
HISTORICAL = BASE.parent / 'WIDE_GPU_20260914_202109Z'


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024**2), b''):
            result.update(block)
    return result.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def main():
    destination = BASE / 'gram_verification.json'
    if destination.exists():
        raise FileExistsError('Final verification is immutable; choose a new check record if needed')
    comparison = read(BASE / 'gram_comparison.json')
    campaign = read(BASE / 'gram_campaign.json')
    network = read(BASE / 'gram_network_campaign.json')
    closure = read(BASE / 'closure_campaign.json')
    spot = read(BASE / 'gram_spotcheck.json')
    preparation = read(BASE / 'gram_prepare_check.json')
    figures = read(BASE / 'figures/gram_figures.json')
    relocation = read(STUDY / 'RELOCATION.json')
    gates = {}
    gates['complete_26_runs'] = comparison['completed_run_count'] == 26 and comparison['status'] == 'complete'
    gates['all_matrix_validations_pass'] = comparison['validation_pass']
    gates['all_24_scalar_replays_exact'] = comparison['replay_consistency_pass'] and all(
        r['maximum_absolute_difference'] == 0 for r in comparison['replay_checks'] if r['status'] == 'compared')
    gates['campaign_hash_matches_analysis'] = sha(BASE/'gram_campaign.json') == comparison['campaign_sha256']
    gates['plan_hash_matches_analysis'] = sha(STUDY/'GRAM_20260914_PLAN.md') == comparison['plan_sha256']
    gates['analysis_source_hash_matches'] = sha(STUDY/'GRAM_20260914_ANALYSIS.py') == comparison['source_sha256']
    gates['spotcheck_source_hash_matches'] = sha(STUDY/'GRAM_20260914_SPOTCHECK.py') == spot['source_sha256']
    gates['spotcheck_pass'] = spot['status'] == 'passed' and spot['maximum_metric_report_discrepancy'] < 1e-12
    gates['preparation_check_pass'] = preparation['status'] == 'passed' and preparation['scientific_trajectories_started'] == 0
    gates['preparation_source_hash_matches'] = sha(STUDY/'GRAM_20260914_PREPARE.py') == preparation['source_sha256']
    gates['plot_source_hash_matches'] = sha(STUDY/'GRAM_20260914_PLOTS.py') == figures['source_sha256']
    gates['plotted_analysis_hash_matches'] = sha(BASE/'gram_comparison.json') == figures['comparison_sha256']
    gates['all_14_figure_files_match'] = len(figures['products']) == 14 and all(
        sha(BASE / row['path']) == row['sha256'] for row in figures['products'])
    preserved = {name: sha(HISTORICAL / name) == value for name, value in relocation['original_generated_sha256'].items()}
    gates['all_97_historical_generated_files_unchanged'] = len(preserved) == 97 and all(preserved.values())
    old_sources = {name: sha(STUDY / name) == value for name, value in relocation['current_study_artifacts_sha256'].items()
                   if name != 'README.md'}
    gates['original_study_sources_and_report_unchanged'] = all(old_sources.values())
    current_runs = []
    for row in comparison['runs']:
        directory = BASE / row['family'] / row['name']
        record = read(directory/'record.json')
        checks = dict(record=sha(directory/'record.json') == row['record_sha256'],
                      gram=sha(directory/'gram.npy') == row['gram_sha256'],
                      observations=sha(directory/'observations.npz') == row['observations_sha256'],
                      complete=record['status'] == 'complete' and record['gram_completed_observations'] == 206)
        current_runs.append(dict(family=row['family'], name=row['name'], checks=checks,
            peak_allocated_bytes=record.get('peak_allocated_bytes'), wall_seconds=record.get('wall_seconds')))
    gates['all_current_run_hashes_and_counts_match'] = all(all(r['checks'].values()) for r in current_runs)
    resources = dict(network_worker_seconds=network['worker_wall_seconds'],
        closure_worker_seconds=closure['worker_wall_seconds'],
        network_longest_worker_seconds=max(r['wall_seconds'] for r in network['results']),
        closure_longest_worker_seconds=max(r['wall_seconds'] for r in closure['runs']),
        campaign_completion_upper_bound_seconds=campaign['completion_recorded_epoch']-campaign['experiment_started_epoch'],
        network_peak_allocated_bytes=max(r['peak_allocated_bytes'] or 0 for r in current_runs),
        generated_bytes_before_this_record=sum(p.stat().st_size for p in BASE.rglob('*') if p.is_file()))
    gates['resource_caps_pass'] = (resources['network_worker_seconds'] < 3600 and
        resources['closure_worker_seconds'] < 1200 and resources['network_longest_worker_seconds'] < 600 and
        resources['closure_longest_worker_seconds'] < 300 and resources['campaign_completion_upper_bound_seconds'] < 2400 and
        resources['network_peak_allocated_bytes'] < 18*1024**3 and resources['generated_bytes_before_this_record'] < 4*1024**3)
    gates['no_worker_failures_or_extra_branches'] = (network['status'] == closure['status'] == 'complete' and
        len(network['results']) == 16 and len(closure['runs']) == 10 and not network['unstarted'] and
        all(r['exit_code'] == 0 and not r['budget_stop'] for r in network['results']) and
        all(r['returncode'] == 0 for r in closure['runs']))
    gates['study_is_flat'] = not any(path.is_dir() for path in STUDY.iterdir())
    for path in STUDY.glob('GRAM_20260914*.py'):
        ast.parse(path.read_text(), filename=str(path))
    gates['all_gram_source_syntax_passes'] = True
    links = []
    for path in (STUDY/'README.md', STUDY/'GRAM_20260914_REPORT.md'):
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            target = match.group(1).split('#')[0]
            if not target or '://' in target:
                continue
            resolved = (path.parent / target).resolve()
            links.append(dict(source=path.name, target=target, exists=resolved.exists() or resolved == destination))
    gates['report_and_readme_links_resolve'] = all(r['exists'] for r in links)
    result = dict(status='passed' if all(gates.values()) else 'failed', created_utc=datetime.now(timezone.utc).isoformat(),
        command=sys.argv, source_sha256=sha(__file__), gates=gates, resources=resources,
        historical_generated_preservation=preserved, historical_source_preservation=old_sources,
        current_runs=current_runs, links=links,
        study_source_hashes={p.name: sha(p) for p in sorted(STUDY.glob('GRAM_20260914*')) if p.is_file()},
        README_sha256=sha(STUDY/'README.md'),
        key_output_hashes={name: sha(BASE/name) for name in ('gram_comparison.json', 'gram_spotcheck.json',
            'gram_prepare_check.json', 'gram_campaign.json', 'figures/gram_figures.json')},
        scientific_limitations='Checks verify this finite experiment; layer-2 quadrature gate remains unresolved. No promotion or asymptotic certification.')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(status=result['status'], failed_gates=[k for k,v in gates.items() if not v], resources=resources), indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
