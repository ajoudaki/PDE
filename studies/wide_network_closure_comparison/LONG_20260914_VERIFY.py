#!/usr/bin/env python3
"""Final bounded artifact verification; does not evolve any trajectory."""
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / 'studies/wide_network_closure_comparison'
BASE = ROOT / 'data/generated/wide_network_closure_comparison/LONG_20260914_v1'
CACHE = {}


def sha(path):
    path = path.resolve()
    if path not in CACHE:
        h = hashlib.sha256()
        with path.open('rb') as f:
            for block in iter(lambda: f.read(4 * 1024 * 1024), b''):
                h.update(block)
        CACHE[path] = h.hexdigest()
    return CACHE[path]


def read(path):
    return json.loads(path.read_text())


def check_hashes(mapping, root):
    for path, expected in mapping.items():
        assert sha(root / path) == expected, path


def main():
    campaign = read(BASE / 'long_campaign.json')
    check_hashes(campaign['old_preservation'], ROOT)
    check_hashes(campaign['producer_hashes'], ROOT)
    assert len(campaign['old_preservation']) == 445
    assert sha(BASE / 'inputs.npz') == campaign['inputs_sha256']
    analyses = []
    stage_hashes = {}
    for target in (40, 80, 160, 320, 640):
        path = BASE / f'stage_analysis_{target:06}.json'
        a = read(path)
        stage_hashes[path.name] = sha(path)
        assert a['status'] == 'complete' and a['validation_pass']
        assert a['completed_run_count'] == 16
        assert a['source_sha256'] == sha(STUDY / 'LONG_20260914_ANALYSIS.py')
        for run in a['runs']:
            folder = BASE / run['family'] / run['name'] / f'stage_{target:06}'
            assert sha(folder / 'record.json') == run['record_sha256']
            r = read(folder / 'record.json')
            assert r['status'] == 'complete' and float(r['last_time']) == target
            for filename, key in [('observations.npz', 'observations_sha256'),
                                  ('gram.npy', 'gram_sha256'),
                                  (r['checkpoint_file'], 'checkpoint_sha256')]:
                assert sha(folder / filename) == r[key] == run[key]
            check_hashes(r['source_hashes'], ROOT)
            if target == 40:
                assert run['validation']['replay']['exact_observations_and_grams']
        analyses.append(a)

    independent = read(BASE / 'independent_final_check.json')
    assert sha(BASE / 'independent_final_check.json') == 'b72c1f5ba2d991c1180d29fcde17bc9d2d0a411bf15d3167258b41c99e833f2a'
    assert independent['checker_source_sha256'] == sha(STUDY / 'LONG_20260914_CHECK.py')
    check_hashes(independent['input_hashes'], ROOT)
    a = analyses[-1]
    differences = []

    def compare(x, y):
        differences.append(abs(x - y))
        assert differences[-1] <= 2e-12, (x, y)

    for r in a['loss_curves']:
        if r['name'].endswith('_mean'):
            width = r['name'].split('_')[1][1:]
            values = independent['network_three_seed_mean_losses'][width]
        else:
            values = independent['runs'][f"{r['family']}/{r['name']}"]['loss_320_480_640']
        for i, value in zip((0, 10, 20), values):
            compare(r['curve'][i], value)
    for r in a['comparisons']:
        if r['observable'] != 'G':
            continue
        panel = 'training' if r['panel'] == 'data' else 'circle'
        values = independent['closure_gram_error_320_480_640'][r['closure'][7:]][str(r['width'])][panel]
        for i, value in zip((0, 10, 20), values):
            compare(r['curve'][i], value[r['layer'] - 1])
    for r in a['frozen_initial_baselines']:
        if r['name'] == 'arcs30_n8192_mean':
            panel = 'training' if r['panel'] == 'data' else 'circle'
            compare(r['terminal'], independent['frozen_width8192_endpoint_error'][panel][r['layer'] - 1])
    for r in a['settling']['gram_windows']:
        if r['window'] == 2:
            panel = 'training' if r['panel'] == 'data' else 'circle'
            value = independent['runs'][f"{r['family']}/{r['name']}"]['gram_rms_change_480_to_640'][panel][r['layer'] - 1]
            compare(r['endpoint_change'], value)
    assert len(differences) == 314

    figures = {}
    for target in (160, 640):
        folder = BASE / f'figures_T{target:06}'
        f = read(folder / 'figures.json')
        assert f['source_sha256'] == sha(STUDY / 'LONG_20260914_PLOTS.py')
        check_hashes(f['analysis_sha256'], BASE)
        check_hashes(f['raw_gram_sha256'], BASE)
        for product in f['products']:
            assert sha(BASE / product['path']) == product['sha256']
            figures[product['path']] = product['sha256']
    f = read(BASE / 'figures_T000640/sanity_linear_time.json')
    assert f['source_sha256'] == sha(STUDY / 'LONG_20260914_SANITY_PLOT.py')
    check_hashes(f['analyses'], BASE)
    for product in f['products']:
        path = 'figures_T000640/' + product['path']
        assert sha(BASE / path) == product['sha256']
        figures[path] = product['sha256']
    assert len(figures) == 26

    supervisor = read(BASE / 'supervisor.json')
    assert sha(BASE / 'supervisor.json') == campaign['supervisor_sha256']
    assert supervisor['status'] == campaign['status'] == 'stopped'
    assert supervisor['last_complete_target'] == campaign['last_complete_target'] == 640
    assert [s['target'] for s in supervisor['completed_stages']] == [40, 80, 160, 320, 640]
    assert len([w for w in supervisor['workers'] if w['exit_code'] == 0]) == 80
    cancelled = read(BASE / 'cancelled_stage_001280.json')
    assert len(cancelled['cancelled_workers']) == 4
    assert not list(BASE.glob('*/*/stage_001280/observations.npz'))
    assert not list(BASE.glob('*/*/stage_001280/gram.npy'))
    for path in cancelled['updated_records']:
        r = read(BASE / path)
        assert r['status'] == 'cancelled_by_user_scope'
        assert r['steps_completed'] == r['completed_observations'] == 0
        assert sha((BASE / path).with_name('record_interrupted.json')) == r['original_record_sha256']
    assert read(BASE / 'supervisor_progress.json')['active'] == []
    total_bytes = sum(p.stat().st_size for p in BASE.rglob('*') if p.is_file())
    free_bytes = shutil.disk_usage(BASE).free
    assert total_bytes < 14 * 1024 ** 3 and free_bytes > 3 * 1024 ** 3
    assert supervisor['scientific_elapsed_seconds'] < 7200
    links = 0
    for name in ('README.md', 'LONG_20260914_REPORT.md'):
        for destination in re.findall(r'\]\(([^)]+)\)', (STUDY / name).read_text()):
            if '://' in destination:
                continue
            path = (STUDY / destination.split('#')[0]).resolve()
            assert path.exists() or path == BASE / 'final_verification.json', str(path)
            links += 1
    result = {
        'status': 'passed', 'created_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Artifact integrity and comparison of independently frozen arithmetic; no new trajectories.',
        'source_sha256': sha(Path(__file__)), 'completed_stages': [40, 80, 160, 320, 640],
        'completed_run_segments': 80, 'exact_bootstrap_replays': 16,
        'earlier_files_preserved': 445, 'producer_hash_count': len(campaign['producer_hashes']),
        'stage_analysis_hashes': stage_hashes, 'independent_statistics_compared': len(differences),
        'maximum_independent_difference': max(differences), 'figure_hashes': figures,
        'resolved_local_links': links, 'excluded_next_stage_launches': 4,
        'strict_settling_passed': a['settling']['passed'],
        'strict_settling_failed_conditions': a['settling']['failed_condition_count'],
        'numerical_controls_passed': a['numerical_gates']['passed'],
        'quadrature_resolved': False,
        'scientific_elapsed_seconds': supervisor['scientific_elapsed_seconds'],
        'generated_bytes_before_verification': total_bytes, 'disk_free_bytes': free_bytes,
        'report_sha256': sha(STUDY / 'LONG_20260914_REPORT.md'),
        'readme_sha256': sha(STUDY / 'README.md'),
    }
    with (BASE / 'final_verification.json').open('x') as f:
        json.dump(result, f, indent=2); f.write('\n')
    print(json.dumps({k: v for k, v in result.items() if 'hash' not in k}, indent=2))


if __name__ == '__main__':
    main()
