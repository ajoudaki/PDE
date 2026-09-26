"""CPU-only reporting from final audited scalar metrics; no model execution."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT/'data/generated/gradient_flow_probe_dictionary_20260921'


def main():
    path = DATA/'suite_analysis_final01/metrics.json'
    rows = json.loads(path.read_text())
    manifest = json.loads((HERE/'SUITE_MANIFEST.json').read_text())
    cases = list(manifest['cases'])
    lookup = {(r['case'],r['method']):r for r in rows}
    records = []
    for new_p, old_p in ((1,1),(3,1),(5,3)):
        for family in ('old','gaussian','orthogonal'):
            result = dict(new_p=new_p,baseline_p=old_p,baseline=family,
                          wins=[],losses=[],unresolved=[],reversals=[])
            for case in cases:
                a,b = lookup[case,f'new_p{new_p}'],lookup[case,f'{family}_p{old_p}']
                directions = [a[level+'_rms']<b[level+'_rms'] for level in ('primary','refined')]
                category = ('unresolved' if not(a['valid'] and b['valid']) else
                            'reversals' if directions[0]!=directions[1] else
                            'wins' if directions[1] else 'losses')
                result[category].append(case)
            records.append(result)
    growth = []
    for small,large in ((1,3),(3,5),(1,5)):
        result = dict(from_p=small,to_p=large,improved=[],worsened=[],unresolved=[])
        for case in cases:
            a,b = lookup[case,f'new_p{small}'],lookup[case,f'new_p{large}']
            direction = [b[level+'_rms']<a[level+'_rms'] for level in ('primary','refined')]
            key = ('unresolved' if not(a['valid'] and b['valid']) or direction[0]!=direction[1]
                   else 'improved' if direction[1] else 'worsened')
            result[key].append(case)
        growth.append(result)
    matched = {family:[lookup[case,f'{family}_p{p}'] for case in cases]
               for family,p in (('new',5),('old',3),('gaussian',3),('orthogonal',3))}
    assert all(r['valid'] for group in matched.values() for r in group)
    means = {family:sum(r['refined_rms'] for r in group)/len(group)
             for family,group in matched.items()}
    charges = []
    for name in ('suite_preflight01','suite_primary01','suite_refined01','suite_extra01',
                 'suite_analysis01a','suite_analysis01b','suite_analysis02a','suite_independent01'):
        for p in sorted((DATA/name).glob('completion*.json')):
            charges.append(dict(path=str(p.relative_to(ROOT)),seconds=json.loads(p.read_text())['seconds']))
    p = DATA/'suite_progress01/progress.json'
    charges.append(dict(path=str(p.relative_to(ROOT)),seconds=json.loads(p.read_text())['seconds']))
    spent = sum(r['seconds'] for r in charges)
    out = DATA/'suite_summary01'
    out.mkdir(exist_ok=False)
    result = dict(cases=cases,nearest_size_comparisons=records,growth=growth,
        mean_case_rms_38_vs_45=means,invalid_cells=[dict(case=r['case'],method=r['method'],reasons=r['reasons'])
                                               for r in rows if not r['valid']],
        gpu_charges=charges,gpu_seconds=spent,remaining_gpu_seconds=2028.182881616056-spent,
        source_metrics_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        summarizer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (out/'summary.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    table = ['| Task | New 38 | Old 45 | Gaussian 45 | Orthogonal 45 |','|---|---:|---:|---:|---:|']
    for case in cases:
        values = [lookup[case,f'{family}_p{p}']['refined_rms']
                  for family,p in (('new',5),('old',3),('gaussian',3),('orthogonal',3))]
        table.append('| '+case+' | '+' | '.join(f'{v:.6f}' for v in values)+' |')
    counts = ['| New / closest archived vectors | Old closure | Gaussian | Orthogonal |',
              '|---|---:|---:|---:|']
    for p,sizes in ((1,'6 / 8'),(3,'18 / 8'),(5,'38 / 45')):
        selected = [r for r in records if r['new_p']==p]
        counts.append('| '+sizes+' | '+' | '.join(f"{len(r['wins'])}/{len(r['wins'])+len(r['losses'])}"
                                                  for r in selected)+' |')
    report = '''# Derivative dictionary: eleven original width2048 tasks

The 38-vector derivative dictionary improves on the nearest archived45-vector
old closure in8/11 tasks, and on each random baseline in10/11. All44 endpoint
comparisons underlying this statement pass numerical gates and independent
raw-state checks. Both selected numerical levels agree on every direction.
Its mean per-task circle RMS is {new:.6f}, compared with {old:.6f} old closure,
{gaussian:.6f} Gaussian and {orthogonal:.6f} orthogonal. These are arithmetic
means over the same fixed eleven tasks, not repeated-seed estimates.

## Design and comparison

User-confirmed scope: all11 original n2048 qualitative tasks except the
equal_semicircles negative-control geometry; no fresh/rotated confirmations.
The earliest two n512-only tasks have no n2048 baseline archive and are outside
this width-matched suite. Reuse all old baselines and dense references. The
later dense-reference pair supersedes earlier references on quadrant_pairs
and two_outliers_alternating; every method uses the same pair for its task.

New p1,p3,p5 have6,18,38 frozen vectors and8,72,336 middle coefficients.
Archived p1,p3,p5 have8,45,149 vectors and15,350,2688 coefficients. All models
also train6144 read-in/readout parameters. Thus new38 and archived45 have
6480 and6494 trainable parameters, respectively. They have the same width,
seed, initialized read-in/readout, canonical tanh network, loss, flow and
stopping rule; frozen bases and compressed middle initializations differ.
There is no retained dense middle residual, task-label-dependent dictionary,
new seed, basis tuning or baseline retraining.

The user's reporting correction selects the nearest AVAILABLE total-vector
count, separately for every family. It supersedes the first live updates'
equal-order framing. There is no21-vector old p2 archive at this width, so
the18/8 comparison retains a substantial size difference. All archived8/45/149
and new6/18/38 points remain in the figures and complete metric table.

Mean unhalved training MSE stopping threshold0.001, at each model's own first
detected crossing. Reported RMS compares the resulting function with the
dense network's learned function on8192 uniform circle angles. This measures
approximation of that learned dense function, not unseen-label generalization.
Training is full-batch coefficient gradient flow numerically integrated with
the unchanged simultaneous adaptive Heun method, not Adam or SGD.

## Nearest-size results

Entries below count lower RMS at BOTH selected numerical levels, divided by
the number of numerically valid comparisons for that pair. Invalid cells are
excluded only from the affected denominator and remain explicitly reported.
No supported comparison reverses between numerical levels.

{counts}

For the most comparable38/45 sizes, the old closure wins on equal_mixed_odd,
two_clusters_grouped and two_outliers_alternating. Both random baselines win
only on near_equal_grouped. Every value in this next table is validated.

{table}

## Size trend and limitations

New6 to new38 improves RMS inall11 tasks at both numerical levels. The
successive increases are not monotone: among10 tasks where both endpoints
are valid,6 to18 improves9 and worsens1;18 to38 improves8 and worsens2.
The unresolved intermediate point is quadrant_alternating/newp3. A richer
dictionary is useful here, but finite results do not establish an asymptotic
approximation rate, arbitrary-accuracy convergence or universal superiority.

## Numerical checks and retained unresolved cells

All66 base trajectories plus the one permitted numerical extra fitted. New
base tolerances were6.25e-5/1.5625e-5 with atol=rtol/100. The sole extra used
rtol3.90625e-6 on quadrant_alternating/newp3 after its fitted base pair had
sampled maximum discrepancy0.02375835597. Its latest pair still differs by
0.01499866628, above0.01. Latest-pair RMS0.155262689 is retained as unresolved;
no further extra is allowed by the frozen protocol. Its favorable apparent
ranking is not counted as a validated win.

Inherited unresolved controls remain quadrant_alternating/Gaussianp1
(0.01012700963) and orthogonalp5(0.04146386791). These do not affect the
38-versus45 comparisons. Final coverage129/132 model rows valid,32/33 new
dictionary rows valid, all11 dense references valid.

Independent replay covers287 distinct trajectories and2672 saved snapshots,
with separately associated forward arithmetic, training losses, initial
states/projections, basis reconstruction, case/seed/grid and executed-source
checks. Final scalar agreement and detailed maxima are in
SUITE_INDEPENDENT_CHECK.md. All failures/earlier attempts remain preserved.
Four archived wrapper hashes were authenticated against exact files recovered
from their recorded commits; see SUITE_SOURCE_RECONCILIATION.md.

## Artifacts and resources

Authoritative metrics/validation/curves: generated suite_analysis_final01.
Figures: generated suite_plots02. Nearest-size counts, means, size trends,
explicit task lists and every compute charge: generated suite_summary01.
Exact schedule/configuration provenance: SUITE_RUN_RECORD.md and all raw
suite_primary01/suite_refined01/suite_extra01 configurations. Frozen inputs:
SUITE_PROTOCOL.md,SUITE_MANIFEST.json; report mapping amendment:
SUITE_REPORTING_AMENDMENT.md.

Both RTX3090 GPUs ran concurrent training workers and independent checks.
Charged new GPU-worker time{spent:.12f}s, remaining inherited allowance
{remaining:.12f}s, no outstanding reservations or further training branch.
The shared checkout, tracked files/index and previous runs were preserved.
These are internally checked study results; no established-source promotion.
'''.format(**means,counts='\n'.join(counts),table='\n'.join(table),spent=spent,
           remaining=2028.182881616056-spent)
    (HERE/'SUITE_RESULTS.md').write_text(report)
    print(json.dumps(dict(gpu_seconds=spent,remaining=2028.182881616056-spent,
                          means=means,nearest_counts=counts)))


if __name__=='__main__':
    main()
