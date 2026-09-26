# p7 continuation: completed results

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

| Task | New p5 (38) | New p7 (72) | Old (45) | Gaussian (45) | Orthogonal (45) |
|---|---:|---:|---:|---:|---:|
| quadrant_grouped | 0.03070519 | 0.02725287 | 0.03672735 | 0.04418766 | 0.04471333 |
| quadrant_alternating | 0.12067594 | 0.40530702 | 1.28882736 | 2.46188230 | 2.48105459 |
| quadrant_pairs | 0.10499566 | 0.04376072 | 0.16538803 | 0.55072591 | 0.59915601 |
| quadrant_center_edges | 0.12747125 | 0.14221169 | 0.47144830 | 0.51207765 | 0.50274010 |
| equal_mixed_odd | 0.09083138 | 0.07219299 | 0.02618288 | 0.15287066 | 0.16710431 |
| near_equal_grouped | 0.02465622 | 0.01940866 | 0.02541825 | 0.00944488 | 0.00901433 |
| two_clusters_grouped | 0.01001970 | 0.00919420 | 0.00803639 | 0.01101796 | 0.01165378 |
| two_clusters_split | 0.03504632 | 0.05627131 | 0.07383407 | 0.07387152 | 0.07745613 |
| three_clusters_mixed | 0.05223699 | 0.04617003 | 0.06831373 | 0.09916355 | 0.09737275 |
| one_outlier_grouped | 0.02600230 | 0.02044273 | 0.03295062 | 0.04199333 | 0.04188530 |
| two_outliers_alternating | 0.86828715 | 0.75642404 | 0.54976160 | 1.37926665 | 1.30283289 |

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
the GPU allowance. Exact conservative charge is181.31988023594022 seconds,
including the independent check's failed sandbox-only CUDA startup.
Remaining inherited allowance is996.2095660865307 seconds.
All reservations released, all workers finished, no extra run eligible.
The checkout/index, earlier producer sources and results are preserved;
no promotion or Git write. P7_RUN_RECORD.md and p7_summary01/summary.json
record the complete accounting.
