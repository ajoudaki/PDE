"""Original/PCA compute and per-image prediction comparisons, without refitting."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import time

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from VALIDATION_ANALYSIS import error_metrics

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1] / 'data/generated/first_order_dimension_mnist'
SEEDS = (1729, 2718, 3141)
MODELS = ('network', 'closure')
REPRESENTATIONS = ('original', 'pca')
GROUP = {'original': 'main4096', 'pca': 'pca4096'}
DATA = {'original': 'data_3_5', 'pca': 'data_pca98'}


def read_json(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def benchmark():
    rows = []
    for representation in REPRESENTATIONS:
        for model in MODELS:
            for repetition in (1, 2):
                directory = BASE / f'pca_speed/{representation}_{model}_r{repetition}'
                summary = read_json(directory / 'summary.json')
                cfg = summary['configuration']
                assert summary['final_time'] == 100 and cfg['width'] == 4096
                assert cfg['model'] == model and cfg['dtype'] == 'float32'
                assert not cfg['environment']['tf32']
                assert cfg['seed'] == 1729 and cfg['block'] == 2048
                assert cfg['step'] == (.25 if model == 'network' else .125)
                assert cfg['horizon'] == 100 and summary['stop_reason'] == 'horizon'
                expected_gpu = MODELS.index(model) if repetition == 1 else 1 - MODELS.index(model)
                assert cfg['gpu'] == expected_gpu
                assert cfg['dataset'] == DATA[representation]
                data_path = BASE / DATA[representation] / 'dataset.npz'
                assert summary['data']['metadata']['dataset_sha256'] == sha(data_path)
                for source in ('RUN.py', 'NETWORK_ENGINE.py', 'P1_ENGINE.py', 'P1_INITIALIZATION.py'):
                    assert cfg['source_sha256'][source] == sha(HERE / source)
                assert summary['steps'] == (400 if model == 'network' else 800)
                rows.append({
                    'representation': representation, 'model': model,
                    'repetition': repetition, 'gpu': cfg['gpu'],
                    'dimension': summary['data']['metadata']['dimension'],
                    'integration_seconds': summary['integration_seconds'],
                    'training_wall_seconds': summary['training_wall_seconds'],
                    'initialization_seconds': summary['initialization_seconds'],
                    'peak_allocated_MiB': summary['peak_allocated_bytes'] / 2**20,
                    'moving_state_MiB': summary['moving_state_bytes'] / 2**20,
                    'retained_model_MiB': summary['retained_model_bytes'] / 2**20,
                    'summary_sha256': sha(directory / 'summary.json'),
                })
    per_gpu = []
    for gpu in (0, 1):
        by = {(r['representation'], r['model']): r for r in rows if r['gpu'] == gpu}
        assert len(by) == 4
        comparisons = {}
        for name, reference, candidate in (
            ('original_closure_vs_original_network', ('original', 'network'), ('original', 'closure')),
            ('pca_closure_vs_pca_network', ('pca', 'network'), ('pca', 'closure')),
            ('pca_closure_vs_original_network', ('original', 'network'), ('pca', 'closure')),
            ('pca_closure_vs_original_closure', ('original', 'closure'), ('pca', 'closure')),
            ('pca_network_vs_original_network', ('original', 'network'), ('pca', 'network')),
        ):
            a, b = by[reference], by[candidate]
            comparisons[name] = {
                'integration_speedup': a['integration_seconds'] / b['integration_seconds'],
                'training_loop_speedup': a['training_wall_seconds'] / b['training_wall_seconds'],
                'peak_memory_reduction_fraction': 1 - b['peak_allocated_MiB'] / a['peak_allocated_MiB'],
            }
        per_gpu.append({'gpu': gpu, 'comparisons': comparisons})
    aggregate = {}
    for representation in REPRESENTATIONS:
        aggregate[representation] = {}
        for model in MODELS:
            selected = [r for r in rows if (r['representation'], r['model']) == (representation, model)]
            times = [r['integration_seconds'] for r in selected]
            peaks = [r['peak_allocated_MiB'] for r in selected]
            aggregate[representation][model] = {
                'integration_seconds_range': [min(times), max(times)],
                'mean_integration_seconds': float(np.mean(times)),
                'peak_allocated_MiB_range': [min(peaks), max(peaks)],
                'relative_timing_range': float((max(times) - min(times)) / np.mean(times)),
                'timing_variation_exceeds_15_percent': bool((max(times) - min(times)) / np.mean(times) > .15),
            }
    return {'physical_horizon': 100, 'rows': rows, 'aggregate': aggregate,
            'same_gpu_comparisons': per_gpu,
            'timing_scope': 'Synchronized full-batch integration; initialization, observations and serialization excluded. Training-loop time reported separately. Two RTX3090 devices; crossed model assignments and reversed representation order.'}


def metric(prediction, reference, labels):
    return {**error_metrics(prediction, reference),
            'within_class': {str(digit): error_metrics(prediction[labels == sign], reference[labels == sign])
                             for digit, sign in ((3, 1), (5, -1))}}


def load_main():
    runs, arrays, provenance = {}, {}, {}
    for representation in REPRESENTATIONS:
        with np.load(BASE / DATA[representation] / 'dataset.npz', allow_pickle=False) as data:
            arrays[representation] = {k: data[k].copy() for k in ('train_y', 'val_y', 'val_ids', 'test_y')}
        data_hash = sha(BASE / DATA[representation] / 'dataset.npz')
        runs[representation] = {}
        for model in MODELS:
            runs[representation][model] = []
            for seed in SEEDS:
                directory = BASE / GROUP[representation] / f'{model}_{seed}'
                summary = read_json(directory / 'summary.json')
                with np.load(directory / 'observations.npz', allow_pickle=False) as archive:
                    run = {k: archive[k].copy() for k in archive.files}
                run['summary'] = summary
                assert summary['final_time'] == 600 and summary['configuration']['width'] == 4096
                assert summary['data']['metadata']['dataset_sha256'] == data_hash
                assert np.array_equal(run['val_y'], arrays[representation]['val_y'])
                assert np.array_equal(run['train_y'], arrays[representation]['train_y'])
                assert np.array_equal(run['times'], np.arange(0, 601, 10))
                run['loss'] = np.mean((run['train_predictions'].astype(np.float64) - run['train_y'])**2, axis=1)
                runs[representation][model].append(run)
                provenance[f'{representation}_{model}_{seed}'] = {
                    'observations_sha256': sha(directory / 'observations.npz'),
                    'summary_sha256': sha(directory / 'summary.json'),
                }
    for key in arrays['original']:
        assert np.array_equal(arrays['original'][key], arrays['pca'][key])
    return runs, arrays['original'], provenance


def comparison(candidate_runs, reference_runs, labels):
    reference_outputs = np.array([r['val_predictions'][-1] for r in reference_runs], dtype=np.float64)
    reference = reference_outputs.mean(axis=0)
    target = float(np.mean([r['loss'][-1] for r in reference_runs]))
    rows, saved, pairs = [], [], []
    for seed, run in zip(SEEDS, candidate_runs):
        available = bool(run['loss'].min() <= target <= run['loss'].max())
        idx = int(np.argmin(abs(run['loss'] - target)))
        final = run['val_predictions'][-1].astype(np.float64)
        chosen = run['val_predictions'][idx].astype(np.float64)
        rows.append({'seed': seed, 'same_time': metric(final, reference, labels),
                     'selected_time': float(run['times'][idx]),
                     'target_in_saved_loss_range': available,
                     'selected_training_mse': float(run['loss'][idx]),
                     'relative_loss_mismatch': float(run['loss'][idx] / target - 1),
                     'matched_loss': metric(chosen, reference, labels) if available else None})
        saved.append((final, chosen))
        for k, ref_seed in enumerate(SEEDS):
            pairs.append({'candidate_seed': seed, 'reference_seed': ref_seed,
                          'same_time': metric(final, reference_outputs[k], labels),
                          'matched_loss': metric(chosen, reference_outputs[k], labels) if available else None})
    return ({'reference_time': 600, 'target_training_mse': target,
             'target_definition': 'Mean individual reference-network final training MSE, not ensemble loss',
             'rows': rows, 'all_individual_pairs': pairs,
             'mean_same_time_rms': float(np.mean([r['same_time']['rms'] for r in rows])),
             'mean_matched_loss_rms': float(np.mean([r['matched_loss']['rms'] for r in rows]))
                  if all(r['matched_loss'] is not None for r in rows) else None,
             'reference_network_pairwise_rms': [error_metrics(reference_outputs[i], reference_outputs[j])['rms']
                  for i, j in itertools.combinations(range(3), 2)]}, reference,
            np.array([x[0] for x in saved]), np.array([x[1] for x in saved]))


def scatter_panel(ax, reference, values, labels, title):
    colors = np.where(labels > 0, '#ce654a', '#3377a1')
    for prediction in values:
        ax.scatter(reference, prediction, c=colors, alpha=.25, s=7, linewidths=0, rasterized=True)
    limit = 1.18
    limit = max(limit, 1.04 * float(max(abs(reference).max(), abs(values).max())))
    ax.plot([-limit, limit], [-limit, limit], '--', c='#333333', lw=1)
    ax.set(xlim=(-limit, limit), ylim=(-limit, limit), aspect='equal', title=title)
    ax.grid(alpha=.12)


def common_loss_comparison(runs, labels):
    """One target attainable by every trajectory, fixed without validation."""
    target = max(float(run['loss'][-1]) for rep in runs.values()
                 for group in rep.values() for run in group)
    selected, choices = {}, {}
    for representation in REPRESENTATIONS:
        selected[representation], choices[representation] = {}, {}
        for model in MODELS:
            predictions, rows = [], []
            for seed, run in zip(SEEDS, runs[representation][model]):
                assert run['loss'].min() <= target <= run['loss'].max()
                i = int(np.argmin(abs(run['loss'] - target)))
                predictions.append(run['val_predictions'][i].astype(np.float64))
                rows.append({'seed': seed, 'time': float(run['times'][i]),
                             'training_mse': float(run['loss'][i]),
                             'relative_loss_mismatch': float(run['loss'][i] / target - 1),
                             'validation_accuracy': float(np.mean((predictions[-1] >= 0) == (labels >= 0))),
                             'validation_mse': float(np.mean((predictions[-1] - labels)**2))})
            selected[representation][model] = np.array(predictions)
            choices[representation][model] = rows
    definitions = {
        'original_closure_vs_original_network': ('original', 'closure', 'original'),
        'pca_closure_vs_pca_network': ('pca', 'closure', 'pca'),
        'pca_closure_vs_original_network': ('pca', 'closure', 'original'),
        'pca_network_vs_original_network': ('pca', 'network', 'original'),
    }
    comparisons = {}
    for name, (rep, model, ref_rep) in definitions.items():
        values = selected[rep][model]
        refs = selected[ref_rep]['network']
        reference = refs.mean(axis=0)
        individual = [metric(pred, reference, labels) for pred in values]
        pairs = [{'candidate_seed': s, 'reference_seed': n,
                  **metric(values[i], refs[j], labels)}
                 for i, s in enumerate(SEEDS) for j, n in enumerate(SEEDS)]
        comparisons[name] = {'individual': individual, 'all_individual_pairs': pairs,
                            'mean_individual_rms': float(np.mean([x['rms'] for x in individual]))}
    return ({'target_training_mse': target,
             'target_definition': 'Largest individual terminal training MSE across all twelve original/PCA network/closure runs',
             'choices': choices, 'comparisons': comparisons}, selected)


def analyze(output, benchmark_only=False):
    started = time.perf_counter()
    dest = BASE / output
    dest.mkdir(parents=True, exist_ok=False)
    source = dest / 'source'
    source.mkdir()
    for name in ('PCA_ANALYZE.py', 'VALIDATION_ANALYSIS.py', 'DATA.py', 'PCA_PLAN.md'):
        (source / name).write_bytes((HERE / name).read_bytes())
    timings = benchmark()
    pca = read_json(BASE / 'data_pca98/metadata.json')
    report = {'benchmark': timings, 'pca': pca,
              'analysis_source_sha256': sha(Path(__file__)),
              'metric_source_sha256': sha(HERE / 'VALIDATION_ANALYSIS.py'),
              'python': platform.python_version(), 'numpy': np.__version__}
    if benchmark_only:
        (dest / 'summary.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(timings['aggregate'], indent=2))
        return
    runs, data, provenance = load_main()
    labels = data['val_y']
    definitions = {
        'original_closure_vs_original_network': (runs['original']['closure'], runs['original']['network']),
        'pca_closure_vs_pca_network': (runs['pca']['closure'], runs['pca']['network']),
        'pca_closure_vs_original_network': (runs['pca']['closure'], runs['original']['network']),
        'pca_network_vs_original_network': (runs['pca']['network'], runs['original']['network']),
    }
    comparisons = {name: comparison(*value, labels) for name, value in definitions.items()}
    report['comparisons'] = {name: value[0] for name, value in comparisons.items()}
    report['run_provenance'] = provenance
    common_report, common_predictions = common_loss_comparison(runs, labels)
    report['common_training_loss'] = common_report
    report['main'] = {}
    exports = {'official_train_ids': data['val_ids'], 'labels': labels}
    csv_columns = [data['val_ids'], labels]
    csv_names = ['official_train_id', 'label']
    for representation in REPRESENTATIONS:
        report['main'][representation] = {}
        for model in MODELS:
            rows = []
            for seed, run in zip(SEEDS, runs[representation][model]):
                s = run['summary']
                final = run['val_predictions'][-1].astype(np.float64)
                rows.append({'seed': seed, 'final_time': 600, 'selected_time': s['selected_time'],
                    'final_training_mse': float(run['loss'][-1]),
                    'final_validation_mse': float(np.mean((final - labels)**2)),
                    'final_validation_accuracy': float(np.mean((final >= 0) == (labels >= 0))),
                    'selected_test_accuracy': s['test']['selected']['accuracy'],
                    'final_test_accuracy': s['test']['terminal']['accuracy'],
                    'integration_seconds': s['integration_seconds'],
                    'training_wall_seconds': s['training_wall_seconds'],
                    'peak_allocated_MiB': s['peak_allocated_bytes'] / 2**20,
                    'moving_state_MiB': s['moving_state_bytes'] / 2**20,
                    'retained_model_MiB': s['retained_model_bytes'] / 2**20})
                key = f'{representation}_{model}_{seed}_T600'
                exports[key] = final
                csv_columns.append(final)
                csv_names.append(key)
            report['main'][representation][model] = rows
    for name, (summary, reference, same, matched) in comparisons.items():
        exports[name + '_reference'] = reference
        exports[name + '_same_time'] = same
        exports[name + '_selected'] = matched
        exports[name + '_selected_times'] = np.array([r['selected_time'] for r in summary['rows']])
        for seed, prediction in zip(SEEDS, matched):
            csv_columns.append(prediction)
            csv_names.append(f'{name}_{seed}_selected_by_train_loss')
    for representation in REPRESENTATIONS:
        for model in MODELS:
            key = f'common_loss_{representation}_{model}'
            exports[key] = common_predictions[representation][model]
            exports[key + '_times'] = np.array([r['time'] for r in common_report['choices'][representation][model]])
            for seed, prediction in zip(SEEDS, exports[key]):
                csv_columns.append(prediction)
                csv_names.append(f'{key}_{seed}')
    np.savez_compressed(dest / 'sample_predictions.npz', **exports)
    np.savetxt(dest / 'validation_samples.csv', np.column_stack(csv_columns), delimiter=',',
               header=','.join(csv_names), comments='')

    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(2, 2, figsize=(11, 10), layout='constrained')
    for col, (representation, name) in enumerate(zip(REPRESENTATIONS, tuple(definitions)[:2])):
        summary, reference, same, matched = comparisons[name]
        d = 784 if representation == 'original' else pca['dimension']
        label = f'Original inputs · d = {d}' if representation == 'original' else f'PCA98 inputs · d = {d}'
        scatter_panel(axes[0, col], reference, same, labels,
                      f'{label}\nEqual T = 600 · RMS {summary["mean_same_time_rms"]:.5f}')
        if summary['mean_matched_loss_rms'] is not None:
            times_text = ', '.join(f'{r["selected_time"]:g}' for r in summary['rows'])
            scatter_panel(axes[1, col], reference, matched, labels,
                          f'Matched training loss · closure T = {times_text}\nRMS {summary["mean_matched_loss_rms"]:.5f}')
        else:
            axes[1, col].text(.5, .5, 'Reference loss not reached by every closure\nwithin the recorded horizon', ha='center')
        for ax in axes[:, col]:
            ax.set_xlabel('Actual network mean output on the same inputs')
            ax.set_ylabel('p = 1 closure output')
    fig.suptitle('Validation prediction fidelity · n = P = 4,096\n1,000 images · three seeds · orange: 3, blue: 5', fontsize=14)
    fig.savefig(dest / 'pca_validation_comparison.png', dpi=180)
    fig.savefig(dest / 'pca_validation_comparison.pdf')
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), layout='constrained')
    for ax, name, title in zip(axes, tuple(definitions)[2:], ('PCA closure', 'PCA actual network')):
        summary, reference, same, _ = comparisons[name]
        scatter_panel(ax, reference, same, labels, f'{title} vs original actual network\nEqual T = 600 · RMS {summary["mean_same_time_rms"]:.5f}')
        ax.set_xlabel('Original-input actual network mean output')
        ax.set_ylabel(f'{title} output')
    fig.suptitle('Total change relative to the original-input network · same validation image IDs', fontsize=13)
    fig.savefig(dest / 'pca_vs_original_predictions.png', dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(2, 2, figsize=(11, 10), layout='constrained')
    common_specs = (
        ('original_closure_vs_original_network', 'original', 'closure', 'original', 'Original closure versus original network'),
        ('pca_closure_vs_pca_network', 'pca', 'closure', 'pca', 'PCA closure versus PCA network'),
        ('pca_closure_vs_original_network', 'pca', 'closure', 'original', 'PCA closure versus original network'),
        ('pca_network_vs_original_network', 'pca', 'network', 'original', 'PCA network versus original network'),
    )
    for ax, (name, rep, model, ref_rep, title) in zip(axes.flat, common_specs):
        refs = common_predictions[ref_rep]['network'].mean(axis=0)
        values = common_predictions[rep][model]
        rms = common_report['comparisons'][name]['mean_individual_rms']
        scatter_panel(ax, refs, values, labels, f'{title}\nMean individual RMS = {rms:.5f}')
        ax.set_xlabel(f'{ref_rep.title()}-input network mean output')
        ax.set_ylabel(f'{rep.title()}-input {model} output')
    fig.suptitle(f'All four systems at one attainable training loss\nTarget MSE = {common_report["target_training_mse"]:.6f} · nearest saved snapshots', fontsize=14)
    fig.savefig(dest / 'pca_common_training_loss.png', dpi=180)
    fig.savefig(dest / 'pca_common_training_loss.pdf')
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), layout='constrained')
    colors = {'network': '#333333', 'closure': '#2864b4'}
    for ax, representation in zip(axes, REPRESENTATIONS):
        for model in MODELS:
            for index, run in enumerate(runs[representation][model]):
                ax.semilogy(run['times'], run['loss'], c=colors[model], alpha=.65,
                            label=('Actual network' if model == 'network' else 'p = 1 closure') if index == 0 else None)
        ax.set(title=f'{representation.title()} inputs', xlabel='Physical training time', ylabel='Training MSE')
        ax.legend()
    fig.savefig(dest / 'pca_training_losses.png', dpi=180)
    plt.close(fig)
    report['analysis_wall_seconds'] = time.perf_counter() - started
    report['scope'] = 'Finite three-seed PCA98 versus original-input experiment; raw predictions, no calibration. PCA includes centering. Same physical horizon and distinct matched-training-loss diagnostics; no convergence claim.'
    (dest / 'summary.json').write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps({name: {'equal_time_rms': value[0]['mean_same_time_rms'],
                             'matched_loss_rms': value[0]['mean_matched_loss_rms']}
                      for name, value in comparisons.items()}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--benchmark-only', action='store_true')
    args = parser.parse_args()
    analyze(args.output, args.benchmark_only)
