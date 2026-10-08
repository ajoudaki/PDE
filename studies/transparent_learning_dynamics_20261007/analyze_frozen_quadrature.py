"""Frozen local-circuit diagnostic, not accuracy of a new coupled model."""
from pathlib import Path
import csv
import hashlib
import json
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np

ROOT = Path('data/generated/transparent_learning_dynamics_20261007')
OUT = ROOT / 'frozen_quadrature_v1' / 'analysis'


def block(a, name):
    if name == 'TT_offdiag':
        return a[..., :16, :16][..., ~np.eye(16, dtype=bool)]
    a = a[..., :16, :16] if name == 'TT' else a[..., :16, 16:]
    return a.reshape(*a.shape[:-2], -1)


def rms(a):
    return np.sqrt(np.mean(np.asarray(a)**2, axis=-1))


def norms(a):
    return dict(max_entry=float(np.max(abs(a))), max_rms=float(np.max(rms(a))))


def load(path):
    with np.load(path) as source:
        return {key: source[key] for key in source.files}


def analysis():
    fresh = [load(ROOT / 'frozen_quadrature_v1' /
             f'source{s}_fresh{s+6400}_n32768/trajectory.npz')
             for s in (1701, 1702, 1703)]
    dense = [load(ROOT / 'residual_filter_v1' /
             f'dense_m16_n1024_s{s}_h0.2_filtered/trajectory.npz')
             for s in (101, 202, 303)]
    rows, curves = [], {'normalized_time': fresh[0]['normalized_time']}
    for layer in (1, 2):
        key = f'c{layer}'
        for name in ('TT', 'TT_offdiag', 'TP'):
            dense_absolute = np.mean([block(r[key], name) for r in dense], axis=0)
            dd = dense_absolute-dense_absolute[:1]
            scale = float(np.max(rms(dd)))
            old = np.array([block(r['source_'+key], name) for r in fresh])
            batches = np.array([block(r['batch_'+key], name) for r in fresh])
            assert batches.shape[1] == 32
            old_delta = old-old[:, :1]
            batch_delta = batches-batches[:, :, :1]
            for scope, ids in [('ensemble', [0, 1, 2]),
                               ('source1701', [0]), ('source1702', [1]),
                               ('source1703', [2])]:
                old_mean = old_delta[ids].mean(axis=0)
                selected = batch_delta[ids]
                fresh_mean = selected.mean(axis=(0, 1))
                correction = fresh_mean-old_mean
                # Conditional only: saved coefficient sets and dense draws
                # are fixed. Source-to-source variability is separate.
                se = np.sqrt(selected.var(axis=1, ddof=1).sum(axis=0)
                             / (32*len(ids)**2))
                halves = selected[:, :16].mean(axis=(0, 1)) - selected[:, 16:].mean(axis=(0, 1))
                three_se = float(np.max(rms(3*se)))
                half_size = float(np.max(rms(halves)))
                original_error, replay_error = old_mean-dd, fresh_mean-dd
                original_size = float(np.max(rms(original_error)))
                replay_size = float(np.max(rms(replay_error)))
                maximum = int(np.argmax(rms(correction)))
                resolved = three_se < .05*scale and half_size < .05*scale
                material = (float(rms(correction[maximum])) > .2*scale
                            and float(rms(correction[maximum])) > float(rms(3*se[maximum])))
                explains = material and resolved and replay_size <= .5*original_size
                denom = np.linalg.norm(original_error)*np.linalg.norm(correction)
                # Post-test explanatory diagnostic, not a replacement for the
                # preregistered max-time accuracy/resolution gates. The old
                # error direction is fixed independently of these fresh draws.
                old_squared = np.sum(original_error**2)
                projection_batches = np.sum(
                    (selected-old_delta[ids, None])*original_error,
                    axis=(-2, -1))/old_squared
                projection_se = float(np.sqrt(projection_batches.var(axis=1, ddof=1).sum()
                                               / (32*len(ids)**2)))
                row = dict(scope=scope, layer=layer, block=name,
                    dense_change_scale=scale, correction=norms(correction),
                    relative_correction=float(np.max(rms(correction)))/scale,
                    original_dense_error=norms(original_error),
                    replay_dense_error=norms(replay_error),
                    relative_original_error=original_size/scale,
                    relative_replay_error=replay_size/scale,
                    remaining_error_ratio=replay_size/original_size,
                    correction_error_cosine=float(np.sum(original_error*correction)/denom) if denom else None,
                    stacked_error_direction_correction=float(projection_batches.mean()),
                    stacked_error_direction_correction_se=projection_se,
                    three_conditional_se_max_rms=three_se,
                    two_half_difference=norms(halves), quadrature_resolved=resolved,
                    material_measured_defect=material,
                    negligible_measured_defect=float(np.max(rms(correction))) < .05*scale,
                    material_resolved_defect=material and resolved,
                    negligible_resolved_defect=resolved and float(np.max(rms(correction))) < .05*scale,
                    explains_at_least_half=explains,
                    absolute_self_consistency_error=norms(batches[ids].mean(axis=(0, 1))-old[ids].mean(axis=0)),
                    original_absolute_dense_error=norms(old[ids].mean(axis=0)-dense_absolute),
                    replay_absolute_dense_error=norms(batches[ids].mean(axis=(0, 1))-dense_absolute),
                    nested_changes={str(count): norms(selected[:, :count//1024].mean(axis=(0, 1))-fresh_mean)
                                    for count in (8192, 16384)})
                rows.append(row)
                if scope == 'ensemble':
                    for label, array in [('original_error', original_error),
                            ('replay_error', replay_error), ('correction', correction),
                            ('conditional_three_se', 3*se)]:
                        curves[f'l{layer}_{name}_{label}'] = rms(array)
                    source_corrections = batch_delta.mean(axis=1)-old_delta
                    row['source_correction_standard_error_max_rms'] = float(np.max(
                        rms(source_corrections.std(axis=0, ddof=1)/np.sqrt(3))))
    extras = {}
    for key in ('f', 'd1', 'd2', 'motion1', 'motion2'):
        current = np.mean([r[key] for r in fresh], axis=0)
        source = np.mean([r['source_'+key] for r in fresh], axis=0)
        difference = current-source
        extras[key] = dict(max_entry=float(np.max(abs(difference))),
                           endpoint_max_entry=float(np.max(abs(difference[-1]))))
    extras['motion_difference_convention'] = 'motion1/2 differences above are squared displacement, not RMS displacement.'
    extras['rms_individual_displacement'] = []
    for layer in (1, 2):
        current = np.mean([r[f'motion{layer}'] for r in fresh], axis=0)
        source = np.mean([r[f'source_motion{layer}'] for r in fresh], axis=0)
        for panel, sl in (('training', slice(0, 16)), ('passive', slice(16, None))):
            current_rms = np.sqrt(np.maximum(0, current[:, sl].mean(axis=1)))
            source_rms = np.sqrt(np.maximum(0, source[:, sl].mean(axis=1)))
            extras['rms_individual_displacement'].append(dict(layer=layer, panel=panel,
                endpoint_source=float(source_rms[-1]), endpoint_fresh=float(current_rms[-1]),
                maximum_difference=float(np.max(abs(current_rms-source_rms)))))
            curves[f'l{layer}_{panel}_source_displacement'] = source_rms
            curves[f'l{layer}_{panel}_fresh_displacement'] = current_rms
    current_f = np.mean([r['f'] for r in fresh], axis=0)
    source_f = np.mean([r['source_f'] for r in fresh], axis=0)
    labels = fresh[0]['labels']
    extras['mean_prediction_relative_loss'] = dict(
        source_endpoint=float(np.mean((labels-source_f[-1,:16])**2)/np.mean(labels**2)),
        fresh_endpoint=float(np.mean((labels-current_f[-1,:16])**2)/np.mean(labels**2)),
        convention='Loss of the ensemble-mean prediction; not average loss across source runs.')
    return rows, curves, extras, fresh


def figure(curves):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new('RGB', (1320, 930), 'white')
    draw = ImageDraw.Draw(im)
    fontfile = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    font = ImageFont.truetype(fontfile, 18)
    small = ImageFont.truetype(fontfile, 14)
    title = ImageFont.truetype(fontfile, 23)
    draw.text((28, 18), 'Fresh quadrature of frozen causal histories', font=title, fill='black')
    draw.text((28, 53), 'A diagnostic, not a new trained model. Three source paths; 32,768 fresh samples per path.',
              font=font, fill='black')
    styles = (('original_error', 'Original vs dense', (30, 105, 175), False),
              ('replay_error', 'Frozen replay vs dense', (198, 83, 40), False),
              ('correction', 'Fresh minus original', (100, 90, 150), True),
              ('conditional_three_se', 'Fresh integration: 3 SE', (45, 135, 95), True))
    for row, layer in enumerate((1, 2)):
        for col, name in enumerate(('TT', 'TP')):
            left, top, width, height = 83+col*650, 155+row*340, 510, 235
            heading = f'Layer {layer}: '+('training–training' if name=='TT' else 'training–passive')
            draw.text((left, top-34), heading, font=font, fill='black')
            maximum = 1.08*max(float(curves[f'l{layer}_{name}_{label}'].max()) for label, *_ in styles)
            draw.line((left, top, left, top+height, left+width, top+height), fill='black')
            for j in range(5):
                y = top+height*(1-j/4)
                draw.line((left, y, left+width, y), fill=(225, 225, 225))
                draw.text((left-60, y-8), f'{maximum*j/4:.3f}', font=small, fill='black')
            for label, _, color, dashed in styles:
                values = curves[f'l{layer}_{name}_{label}']
                points = [(left+i*width/(len(values)-1), top+height*(1-float(v)/maximum))
                          for i, v in enumerate(values)]
                if dashed:
                    for k in range(0, len(points)-1, 3):
                        draw.line(points[k:k+2], fill=color, width=2)
                else:
                    draw.line(points, fill=color, width=3)
            for value in (0, 9.6, 19.2):
                draw.text((left+value/19.2*width-12, top+height+8), str(value), font=small, fill='black')
    for i, (_, label, color, _) in enumerate(styles):
        x, y = 45+(i%2)*635, 807+(i//2)*33
        draw.line((x, y+9, x+40, y+9), fill=color, width=3)
        draw.text((x+50, y), label, font=font, fill='black')
    draw.text((45, 892), 'Vertical: similarity-change discrepancy RMS. Horizontal: normalized time 2t/m. SE is conditional on source paths.',
              font=small, fill='black')
    im.save(OUT / 'self_consistency.png')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    records = [json.loads(p.read_text()) for p in sorted((ROOT/'frozen_quadrature_v1').glob('*/record.json'))]
    assert len(records) == 4 and all(r['exit_status'] == 0 for r in records)
    rows, curves, extras, fresh = analysis()
    repeated = load(ROOT/'frozen_quadrature_v1/source1701_fresh8101_n32768_repeat/trajectory.npz')
    deterministic = [key for key in fresh[0] if key not in ('batch_seconds',)]
    reproduction = {key: float(np.max(abs(fresh[0][key]-repeated[key]))) for key in deterministic}
    assert all(value == 0 for value in reproduction.values())
    summary = dict(rows=rows, additional_observables=extras, reproduction=reproduction,
        metadata=dict(count=4, wall_seconds=sum(r['wall_seconds'] for r in records),
                      peak_rss_kib=max(r['peak_rss_kib'] for r in records)),
        analysis_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        interpretation='Fresh quadrature of frozen coefficients; not an autonomous trajectory improvement.')
    (OUT/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    np.savez_compressed(OUT/'curves.npz', **curves)
    with (OUT/'curves.csv').open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(curves)
        writer.writerows(zip(*curves.values()))
    figure(curves)
    print(json.dumps(dict(metadata=summary['metadata'], rows=[r for r in rows if r['scope']=='ensemble']), indent=2))


if __name__ == '__main__':
    main()
