"""Scalar report and exact budget accounting from final checked p7 artifacts."""
import json
from pathlib import Path
import hashlib

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/'data/generated/gradient_flow_probe_dictionary_20260921'


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    out = DATA/'p7_summary01'
    out.mkdir(exist_ok=False)
    source = DATA/'p7_analysis_final01'
    rows = read(source/'metrics.json')
    comparisons = [r for r in read(source/'comparisons.json') if r.get('new_p')==7]
    cases = list(read(HERE/'SUITE_MANIFEST.json')['cases'])
    lookup = {(r['case'],r['method']):r for r in rows}
    methods = ['new_p5','new_p7','old_p3','gaussian_p3','orthogonal_p3']
    assert all(lookup[c,m]['valid'] for c in cases for m in methods)
    means = {m:{level:sum(lookup[c,m][level+'_rms'] for c in cases)/len(cases)
                for level in ('primary','refined')} for m in methods}
    counts = {}
    for m in ('new_p5','old_p3','gaussian_p3','orthogonal_p3'):
        selected = [r for r in comparisons if r['baseline_method']==m]
        assert len(selected)==11 and all(r['valid'] and r['ordering_agrees'] for r in selected)
        counts[m] = dict(wins=sum(r['verdict']=='new_p7' for r in selected),
                         losses=sum(r['verdict']==m for r in selected),
                         losing_cases=[r['case'] for r in selected if r['verdict']==m])
    charges = []
    for directory,names in [('p7_preflight01',['completion.json']),
        ('p7_primary01',['completion_worker0.json','completion_worker1.json']),
        ('p7_refined01',['completion_worker0.json','completion_worker1.json']),
        ('p7_progress01',['progress.json']),('p7_analysis01',['completion.json']),
        ('p7_independent01',['completion_001.json','completion_002.json'])]:
        for name in names:
            path=DATA/directory/name
            charges.append(dict(path=str(path),seconds=read(path)['seconds'],sha256=sha(path)))
    total = sum(r['seconds'] for r in charges)
    assert total<=1150
    record = dict(cases=cases,means=means,p7_comparisons=counts,charges=charges,
        total_gpu_worker_seconds=total,remaining_inherited_gpu_worker_seconds=1177.529446322471-total,
        unused_p7_ceiling=1150-total,no_outstanding_reservations=True,
        all_p7_valid=True,extra_attempts=0,metrics_sha256=sha(source/'metrics.json'),
        comparisons_sha256=sha(source/'comparisons.json'),source_sha256=sha(Path(__file__)))
    (out/'summary.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    table=['| Task | New p5 (38) | New p7 (72) | Old (45) | Gaussian (45) | Orthogonal (45) |',
           '|---|---:|---:|---:|---:|---:|']
    for case in cases:
        table.append('| '+case+' | '+' | '.join(f"{lookup[case,m]['refined_rms']:.8f}" for m in methods)+' |')
    text = '''# p7 continuation: completed results

The new p7 construction has26 lower and46 upper frozen generators (72 total),
1196 trainable middle entries, and7340 total trainable coefficients at n2048.
It retains the complete p5 prefix and the four p6 feedback generators; the
full W2 expansion through time power8 includes lower label-degree residual
feedback. The p6 list is(14,28), not the presumed p5 duplicate. Counts are
sufficient generator counts, not a theorem of minimal Gaussian dimension.
The complete factor definitions and pre-training scales are frozen in
P7_DERIVATION.md and P7_DICTIONARY_SPEC.md.

All22 new trajectories fitted on the same11 original tasks, at both fixed
tolerances. No negative control, rotated case, earlier-order rerun, new seed
or baseline retraining. Gaussian and orthogonal remain separate. The metric
is8192-angle RMS against the same task-specific dense learned function,
at each model's own first detected unhalved training-MSE0.001 crossing.
This measures agreement with the learned dense function, not error against
an independently specified ground-truth function around the whole circle.

P7 improves over newp5 on8/11 tasks, worsens on3/11, with the same ordering
at both tolerances. The worsened cases are quadrant_alternating,
quadrant_center_edges and two_clusters_split. Paired quadrants improve
0.104996 ->0.043761 (58.3% lower), while alternating quadrants worsen
0.120676 ->0.405307 (3.36 times as large).

The mean per-task refined RMS rises from0.1355389183 at38 vectors to
0.1453305678 at72 vectors (7.22% higher). Thus adding dictionary vectors
helps most tasks at this step but does not improve every task or the
unweighted mean. These finite experiments establish no asymptotic rate,
universal monotonicity, or positive-time hierarchy-convergence theorem.

Against the nearest available archived size,45 vectors, p7 wins8/11 versus
the old closure and10/11 versus each random control. The three old-closure
losses are equal_mixed_odd,two_clusters_grouped,two_outliers_alternating;
the sole loss to each random control is near_equal_grouped. Among available
archived totals8,45,149,45 is closest to72. This is not an exact size or
parameter match: old45 has6494 trainable coefficients versus7340 fornew72.
All149-vector results remain in the plots as well.

All55 cells in the following finer-level table pass numerical validation.
The common reference pair and primary/finer ordering are unchanged.

'''+ '\n'.join(table)+'''

## Checks and retained limitations

All11 p7 pairs pass source/config/init/dimension/state/loss and numerical
gates. Largest own endpoint refinement difference is0.00169019619,
below0.01, so no extra branch is eligible. The final combined suite keeps
all143 method rows,140 valid, with the same three pre-existing unresolved
quadrant-alternating rows explicitly marked. No invalid row is deleted or
used to declare a favorable comparison.

Independent checks separately cover full finite jets (maximum1.943e-16),
Gaussian contractions (192/256 consistency4.923e-12), and463 CPU field,
normalization,prediction and gradient checks. The original128/256 moment
resolution failed1e-9 and remains recorded; a pre-training resolution
refinement passed without changing the gate or using any task score.
Formal population coefficients do not establish eighth-order strong-flow
regularity; the finite carrier retains its actual nonzero random readout.

Independent saved-state reconstruction passed all22 p7 trajectories and
200 snapshots, with maximum endpoint replay4.45e-15. Previously checked
110 relevant archived trajectories were rebound to their source/data and
endpoint identities. Recomputed metrics agree on55 rows within2.665e-15.
The main audit source-replays the dense references; merger checks require
their actual array hashes and all historical reused artifact hashes to
match. See P7_INDEPENDENT_CHECK.md and P7_REPORTING_REVIEW.md.

The raw p7 upper ridge condition is5.2163e9, below the fixed1e10 limit;
two upper directions have ridge-filter eigenvalues about0.0234 and0.0259.
All72 raw columns are retained, with no performance-based rescaling or
rank deletion. Finite numerical full rank is not a minimal Gaussian-span
proof. The simultaneous canonical gradient field and adaptive Heun settings
are unchanged; finite numerical integration approximates gradient flow.

## Artifacts and bounded execution

Final merged metrics, validation, comparison rows and endpoint curves:
data/generated/gradient_flow_probe_dictionary_20260921/p7_analysis_final01.
Updated11-panel linear-vector/log-RMS figure and nearest-size table:
data/generated/gradient_flow_probe_dictionary_20260921/p7_plots01,
inPNG,PDF,SVG. Artist checks verify143 curve points and55 table values;
root visually inspected both figures. The previous interactive radial
viewer was not changed in this RMS-plot continuation.

Both GPUs ran concurrently. CPU-only reporting and figures do not debit
the GPU allowance. Exact conservative charge is'''+str(total)+''' seconds,
including the independent check's failed sandbox-only CUDA startup.
Remaining inherited allowance is'''+str(1177.529446322471-total)+''' seconds.
All reservations released, all workers finished, no extra run eligible.
The checkout/index, earlier producer sources and results are preserved;
no promotion or Git write. P7_RUN_RECORD.md and p7_summary01/summary.json
record the complete accounting.
'''
    (HERE/'P7_RESULTS.md').write_text(text)
    print(json.dumps(dict(total=total,remaining=1177.529446322471-total,counts=counts)))


if __name__=='__main__':
    main()
