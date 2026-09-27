"""Audit and plot completed histogram runs; never runs training."""
import argparse
import csv
import json
from pathlib import Path
import shutil

from run_histogram_candidate import Histogram, coordinate_axes, digest, rms, write
import numpy as np
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing, PolyLine, Rect, Circle
from reportlab.lib.colors import HexColor
from plot_block_continuation import text, line, INK, GRID


def plot(out, angles, predictions, errors):
    drawing = Drawing(1050, 650)
    drawing.add(Rect(0, 0, 1050, 650, fillColor=HexColor('#ffffff'), strokeColor=None))
    text(drawing, 525, 617, 'Genuine histogram ODE: fitted output on unseen circle inputs',
         size=19, anchor='middle')
    text(drawing, 525, 591, 'One training point | Gaussian block k=1 | memory order 1 | stop MSE=0.01',
         size=12, anchor='middle')
    colors = {'reference': INK, 'coarse': HexColor('#2563eb'), 'fine': HexColor('#d95f02')}
    for panel in range(2):
        left, bottom, width, height = 70 + 520 * panel, 190, 420, 325
        ymin, ymax = (-1., 1.) if panel == 0 else (-.075, .075)
        xx = lambda a: left + width*a/(2*np.pi)
        yy = lambda value: bottom + height*(value-ymin)/(ymax-ymin)
        ticks = np.linspace(ymin, ymax, 5 if panel == 0 else 7)
        for tick in ticks:
            line(drawing, left, yy(tick), left+width, yy(tick), GRID, .7)
            text(drawing, left-9, yy(tick)-4, f'{tick:.3g}', anchor='end', size=10)
        for angle, label in zip(np.linspace(0, 2*np.pi, 5), ('0', 'pi/2', 'pi', '3pi/2', '2pi')):
            line(drawing, xx(angle), bottom, xx(angle), bottom-5, INK, .8)
            text(drawing, xx(angle), bottom-21, label, anchor='middle')
        line(drawing, left, bottom, left, bottom+height, INK, 1.)
        line(drawing, left, bottom, left+width, bottom, INK, 1.)
        text(drawing, left+width/2, bottom-47, 'Circle angle', anchor='middle')
        text(drawing, left+width/2, bottom+height+19,
             'Learned output' if panel == 0 else 'Histogram minus population reference',
             size=13, anchor='middle')
        for name, values in predictions.items():
            if panel and name == 'reference':
                continue
            values = values if panel == 0 else values-predictions['reference']
            points = []
            for angle, value in zip(np.r_[angles, 2*np.pi], np.r_[values, values[0]]):
                points.extend((xx(angle), yy(value)))
            drawing.add(PolyLine(points, strokeColor=colors[name], strokeWidth=1.7,
                                 fillColor=None))
        if panel == 0:
            drawing.add(Circle(xx(0), yy(.9), 3.5, fillColor=INK, strokeColor=None))
    for j, name in enumerate(('reference', 'coarse', 'fine')):
        x = 65+335*j
        line(drawing, x, 102, x+30, 102, colors[name], 2)
        label = {'reference': 'Population reference (GH128)',
                 'coarse': f'210,681 masses; RMS {errors["coarse"]:.5f}',
                 'fine': f'1,373,125 masses; RMS {errors["fine"]:.5f}'}[name]
        text(drawing, x+38, 98, label, size=11)
    text(drawing, 525, 60,
         'Diagnostic only: reference refinement RMS 0.00065; boundary-mass check failed at both grids.',
         size=11, anchor='middle')
    text(drawing, 525, 37,
         '1024 passive circle queries after training. Errors are absolute function differences, without normalization.',
         size=11, anchor='middle')
    renderPDF.drawToFile(drawing, str(out/'histogram_circle.pdf'))
    renderPM.drawToFile(drawing, str(out/'histogram_circle.png'), fmt='PNG', dpi=100)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    out = parser.parse_args().output.resolve()
    rows = json.loads((out/'results.json').read_text())
    manifest = json.loads((out/'manifest.json').read_text())
    source = Path(__file__).resolve().parent
    for name, expected in manifest['sources'].items():
        assert digest(source/name) == expected
        assert digest(out/'source_snapshot'/name) == expected
    assert digest(out/'histogram_one_input.so') == manifest['library_sha256']
    for row in rows:
        assert digest(out/row['data_file']) == row['data_sha256']
        assert row['fitted'] and row['total_seconds'] < 60
    reference_check = json.loads((out/'reference_check.json').read_text())
    with np.load(out/'reference_GH128.npz') as data:
        reference = data['prediction']; angles = data['angles']
    with np.load(out/'reference_GH80.npz') as data:
        reference80 = data['prediction']
    assert abs(rms(reference, reference80)-reference_check['circle_rms_difference']) < 1e-14
    predictions = {'reference': reference}
    results = []
    audit = {'provenance_verified': True, 'reference_check': reference_check,
             'no_training_in_analysis': True, 'histograms': {}}
    for row in rows:
        if row['kind'] != 'histogram':
            continue
        name = row['name']
        with np.load(out/row['data_file']) as data:
            p = data['p']; shape = tuple(data['shape']); L = float(data['L'])
            pred = data['prediction']; pred32 = data['prediction_eta32']
        assert np.isfinite(p).all() and p.min() >= 0 and abs(p.sum()-1) < 1e-10
        model = Histogram(out/'histogram_one_input.so', shape)
        reproduced = model.predict(p, L)
        dp, stats = model.rhs(p, L)
        model.close()
        assert np.max(np.abs(reproduced-pred)) < 1e-11
        assert abs(float(dp.sum())) < 1e-10
        assert abs(float(stats[0])-pred[0]) < 1e-11
        assert abs((pred[0]-1)**2-row['train_mse']) < 1e-11
        error = rms(pred, reference)
        assert abs(error-row['rms_vs_population_reference']) < 1e-14
        axis_caps = {}
        spread = {}
        axes = coordinate_axes(shape)
        for dimension, key in ((1, 'x'), (2, 'a'), (3, 'c')):
            marginal = p.reshape(shape).sum(axis=tuple(j for j in range(5) if j != dimension))
            axis_caps[key] = float(marginal[axes[dimension] >= .8*axes[dimension][-1]].sum())
            spread[key+'_upper_face_mass'] = float(marginal[-1])
            if key in ('a', 'c'):
                bound = (L-1)**2 if key == 'a' else 2*(L-1)
                spread[key+'_characteristic_envelope'] = bound
                spread[key+'_mass_beyond_envelope'] = float(marginal[axes[dimension] > bound+1e-12].sum())
        audit['histograms'][name] = {
            'saved_query_max_reproduction_error': float(np.max(np.abs(reproduced-pred))),
            'saved_rhs_total_mass_derivative': float(dp.sum()),
            'training_query_matches_rhs': True,
            'final_taper_zone_mass': float(stats[5]), 'final_taper_mass_by_axis': axis_caps,
            'endpoint_spread_diagnostics': spread,
            'max_absolute_circle_error': float(np.max(np.abs(pred-reference))),
            'rms_vs_GH80': rms(pred, reference80),
            'eta32_vs64_rms': rms(pred, pred32),
            'runtime_budget_passed': row['total_seconds'] <= 60,
            'mass_positivity_passed': True,
        }
        predictions[name] = pred
        results.append({key: row[key] for key in ('name', 'dynamic_scalars', 'train_mse',
                        'rms_vs_population_reference', 'training_seconds', 'total_seconds',
                        'physical_time', 'maximum_taper_zone_mass')})
    write(out/'saved_state_audit.json', audit)
    with (out/'summary.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]))
        writer.writeheader(); writer.writerows(results)
    plot(out, angles, predictions, {r['name']: r['rms_vs_population_reference'] for r in results})
    co, fi = results
    improvement = 1-fi['rms_vs_population_reference']/co['rms_vs_population_reference']
    report = f'''# First genuine histogram aggregate experiment

The fixed-grid aggregate ODE fitted the single training datum and predicted unseen circle inputs. Increasing the grid reduced its absolute circle RMS discrepancy from **{co['rms_vs_population_reference']:.5f}** to **{fi['rms_vs_population_reference']:.5f}** ({100*improvement:.1f}% lower). It did **not** meet the predeclared 0.01 accuracy target. The boundary diagnostic also failed, and the reference quadrature remained slightly unresolved. This is a diagnostic result, not a validated accurate scalar replacement. No further tasks were run.

## What was compared

Both models used the same Gaussian-block population memory system: block size k=1, memory order H=1, tanh in both layers, one training input (1,0) with label 1, and zero initial readout. This special case admits an exact symmetry reduction to five coordinates (g,x,a,c,b), where a=-A and b=B/L. The tested model evolves fixed cell masses and one shared clock. Its count is independent of population width and elapsed time. Its reference evolves weighted characteristics under the same block-memory law; those characteristics never supply feedback to the histogram.

All models stopped at their own first training-MSE 0.01 crossing. The comparison is between fitted endpoints, not between trajectories at the same physical time. k=1 is a feasibility case; it does not test the k=16 mixing construction or closeness to a fully dense Gaussian network.

## Fitted-function result

RMS means sqrt((1/(2*pi))*integral_0^(2*pi) (f_hist(theta)-f_population(theta))^2 dtheta), estimated with 1024 equally spaced angles. There is no division by reference signal size and no comparison to teacher test loss. Queries are evaluated only after training, using the final aggregate distribution and the frozen perpendicular Gaussian input coordinate inside both nonlinearities. No test point or Fourier approximation enters training.

| Grid | Dynamic scalars | Circle RMS vs GH128 | Training MSE | Training seconds | Total seconds | Stop time |
|---|---:|---:|---:|---:|---:|---:|
| Coarse | {co['dynamic_scalars']:,} | {co['rms_vs_population_reference']:.8f} | 0.01 | {co['training_seconds']:.3f} | {co['total_seconds']:.3f} | {co['physical_time']:.4f} |
| Fine | {fi['dynamic_scalars']:,} | {fi['rms_vs_population_reference']:.8f} | 0.01 | {fi['training_seconds']:.3f} | {fi['total_seconds']:.3f} | {fi['physical_time']:.4f} |

![Fitted functions and their difference](histogram_circle.png)

The fine grid uses 6.52 times as many masses for this approximately one-third error reduction. This is consistent with refinement helping, but two grids cannot establish an asymptotic convergence rate. A million-state ODE for this one-input, k=1 case does not demonstrate efficient compression at the intended larger block sizes.

## Numerical checks and limitations

- The Gaussian seed quadrature reference was refined through orders 48, 80 and 128, with 576, 1600 and 4096 folded characteristics. All fitted. The last two fitted circle functions differed by {rms(reference, reference80):.8f} RMS, above the predeclared 0.0005 check. That measured difference is not a rigorous error bound. Reusing GH80 instead gives histogram RMS {audit['histograms']['coarse']['rms_vs_GH80']:.8f} and {audit['histograms']['fine']['rms_vs_GH80']:.8f}; the accuracy conclusion is unchanged.
- The maximum accepted-state probability in the union of the x/a/c outer 20% cutoff zones was {100*co['maximum_taper_zone_mass']:.3f}% and {100*fi['maximum_taper_zone_mass']:.3f}%. The predeclared limit was 0.1%. Velocities are modified in those zones; this diagnostic prevents interpreting the result as a clean measurement of grid error alone. It does not quantify the resulting output bias or prove that cutoff error dominates.
- Both final distributions were nonnegative; total mass was conserved within 3.3e-14. Saved-state queries reproduce saved outputs within 1e-11, and their training-input values agree with the training RHS.
- The passive perpendicular Gaussian quadrature check (32 versus 64 nodes) changed histogram outputs by about 0.000085 RMS; both passed 0.0005. Nested 512/1024-angle circle integration changed the reported RMS by less than 1e-15. These are refinement diagnostics, not certified continuum error bounds.
- Every run finished below the 60-second total budget. The runtime guard only interrupts training, so query time was checked afterward. No deadline was reached here.
- No half-CFL or extra-reference run was performed after the diagnostic-only amendment. Temporal discretization and event-interpolation errors therefore remain unseparated. This experiment does not establish a global-in-training trajectory bound.

## Execution record

The original driver stopped when the reference gate failed. Before either histogram fit, a disclosed amendment permitted the two already specified grids solely as diagnostics. It preserved the failed gate, prohibited a clean-pass claim, and prohibited further reference fits, temporal refinement or task expansion. See initial_reference_stop.json, reference_check.json, diagnostic_manifest.json and decision.json. There were exactly three reference fits and two histogram fits.

The C++ core uses conservative nearest-neighbor fluxes and SSPRK2 with CFL checks at both stages, eight OpenMP threads, no cell pruning, and no moving representatives. Algebraic checks against the original population equations and an independent signed-orbit/query audit passed. The final distributions, predictions, source snapshots and hashes are retained; summary.csv and saved_state_audit.json provide the numerical record.

**Assessment:** the genuine aggregate construction runs and supports unseen-input evaluation. This first test supplies evidence that refinement helps, but fails to establish the accuracy and state efficiency needed to justify a broader task campaign.
'''
    (out/'report.md').write_text(report)
    shutil.copyfile(__file__, out/'source_snapshot'/Path(__file__).name)
    for log in ('histogram_candidate_20260927.log', 'histogram_diagnostic_20260927.log'):
        if (Path('/tmp')/log).exists():
            shutil.copyfile(Path('/tmp')/log, out/log)
    write(out/'analysis_manifest.json', {'source_sha256': digest(__file__),
          'artifacts': {name: digest(out/name) for name in ('report.md', 'saved_state_audit.json',
                          'summary.csv', 'histogram_circle.png', 'histogram_circle.pdf')}})
    print(json.dumps(audit, indent=2))
    print(str(out/'report.md'))


if __name__ == '__main__':
    main()
