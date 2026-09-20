# Width4096: the two original configurations

Our dictionary has lower **measured** whole-circle RMS than both Gaussian and
orthogonal controls at every requested p in both configurations, at both
selected numerical levels. The direct advantage is substantial and grows
strongly with p for paired labels. The outlier configuration also favors ours,
but our error is nonmonotone between p3 and p5 and changes little from p3 to p7.
These are finite tested-budget observations, with one unresolved numerical cell
explicitly retained below; no asymptotic rate is claimed.

All55 executed trajectories fitted:52 planned plus3 numerical-resolution
attempts. **23/24 closure comparisons pass all declared numerical gates.**
The outlier orthogonal p5 control remains tolerance-sensitive: its selected
endpoint maximum discrepancy is0.0537122 against the0.01 limit. Its RMS is still
larger than ours at both levels, but this particular comparison remains a
qualified measured diagnostic, not a numerically validated comparison.

## Requested design

Only the original paired-label and alternating-label/two-outlier geometries are
used. No rotated/perturbed confirmation case or negative control was run.
Width4096 in both hidden tanh layers; original network seed20260920 and random
dictionary seed7319; p1,3,5,7. Ours, Gaussian and orthogonal remain separate,
matched in nominal dictionary dimensions. Every model trains all its prescribed
blocks and reaches its own training-MSE0.001 crossing. The full4096 network at
its own crossing is the common reference within each case and numerical level.
See [SCALING_WIDTH4096_PROTOCOL.md](SCALING_WIDTH4096_PROTOCOL.md) for the frozen
model, metric, validity criteria and resource bounds.

This continuation was explicitly requested after the earlier campaign closed.
It is independent of the earlier conditional StageD gate. These two geometries
were selected from previous results; they are not new independent problem-family
replicates. Equal seed integers across widths do not preserve identical finite
network arrays.

## Selected-finer RMS against the full network

Errors use the saved8192-angle circle grid, not training labels or the downsampled
viewer. The complete coarser/finer values are in the linked final analysis and
plot CSV; the figures show both selected levels.

| Configuration | p | Dictionary vectors | Ours | Gaussian | Orthogonal |
|---|---:|---:|---:|---:|---:|
| Paired labels | 1 | 8 | 0.266726 | 0.707265 | 0.675511 |
| Paired labels | 3 | 45 | 0.138019 | 0.626333 | 0.665137 |
| Paired labels | 5 | 149 | 0.0676996 | 0.503742 | 0.569550 |
| Paired labels | 7 | 369 | 0.0363218 | 0.401323 | 0.463392 |
| Alternating labels + outliers | 1 | 8 | 1.098322 | 1.569897 | 1.690063 |
| Alternating labels + outliers | 3 | 45 | 0.497921 | 1.342203 | 1.336221 |
| Alternating labels + outliers | 5 | 149 | 0.531256 | 1.143076 | 1.161139† |
| Alternating labels + outliers | 7 | 369 | 0.483736 | 1.044267 | 1.009153 |

† Fitted and replayed, but endpoint tolerance check unresolved. Selected coarser
RMS1.15318696 and finer RMS1.16113923 are both retained. The0.0537122 discrepancy
is a pointwise maximum difference between this model's selected endpoints,
not its RMS error against the full network.

At p7, Gaussian/ours and orthogonal/ours RMS ratios are respectively11.0491
and12.7580 for paired labels;2.15875 and2.08616 for outliers. These comparisons
pass the numerical gates. Each ratio uses its named control, with no
minimum-of-two baseline. Nominal vectors count K1+K2 and are not a whole-model
storage or wall-time measure.

## Checks and provenance

Final analysis:
[scaling_width4096_analysis02/tables.md](../../data/generated/random_dictionary_learned_circle_20260920/scaling_width4096_analysis02/tables.md),
with metrics/validation/provenance JSON, CSV and pointwise prediction/error NPZ
alongside it. Raw roots are scaling_width4096_primary01/refined01/extra01.
Analysis01 and every earlier attempt remain intact.

[Independent audit](scaling_width4096_independent_check.md) recomputed all48
selected-level metric records in CUDA float64 with zero discrepancies from the
analysis. All3231 technical checks passed, including initial/endpoint replay,
grids, actual dictionary metadata/algebra, execution declarations and75 producer
hash checks. A separate53-check structural audit confirms26 predictors,
55 attempts, exact orders/dimensions and no historical inputs. Numerical
endpoint validity remains23/24, as reported above. The metadata supplement
`scaling_width4096_logs01/metadata_gate_final.json` has no problems.

Three allowed tighter-resolution runs were selected solely by numerical
discrepancy. Outlier Gaussianp1 and orthogonalp1 then pass with endpoint maxima
0.00188598 and0.00984023. Outlier orthogonalp5 changes by0.0537122, exceeding
its earlier0.043743 discrepancy, and remains unresolved. The predeclared
one-extra-attempt-per-cell limit ends this branch; no outcome-dependent
additional seed, geometry, p, or tolerance search was performed.

The extension used886.3587973192334 timed training-worker seconds. Including
the earlier campaign, total2894.574399381876 of6000 seconds;3105.425600618124
remain unused and no training reservation remains. This new request totals55
trajectories; old+new230 is recorded under the new authorization, not mislabeled
as the old protocol's198-trajectory maximum. Exact commands and budget entries
are in [SCALING_WIDTH4096_RUN_RECORD.md](SCALING_WIDTH4096_RUN_RECORD.md).

## Figures and interactive view

`scaling_width4096_plots01` contains individual RMS-vs-vector plots with linear
x/log y, and four-p-panel training-MSE-vs-physical-time plots with log y for
each configuration. Traces use every saved accepted step and stop at their own
crossings; both selected numerical levels are retained. The unresolved control
is explicitly marked. CSV and source/input/output hash provenance accompany
the PNG/PDF/SVG products and combined PDF.

`scaling_width4096_radial01` contains the26 displayed endpoint curves, exact24
saved RMS values, explicit validity flags, the compressed inline viewer and
provenance. The viewer uses1024 uniformly sampled angles rounded to six decimal
places; its displayed RMS values still come from all8192 angles. Signed output
is a displacement from a positive zero-output radius. Scale stays fixed across
p within a configuration. Only these two configurations and p1,3,5,7 appear.
The outlier orthogonalp5 trace carries a visible unresolved-tolerance marker.

Scoped independent export checking confirmed all24 RMS rows,52 selected
trajectories and111776 saved loss samples exactly, including all three extra
selection paths and the sole unresolved flag. All112 plot input,16 output and
one source hashes match; the combined PDF has four pages. All26 radial curves,
24 RMS values and validity/endpoint metadata match final sources; its compressed
payload equals its JSON byte for byte, with all source/input/output hashes
matching. Representative static and radial views were visually inspected.
Browser checks exercised all eight experiment/p selections, curve and tooltip
toggles, state restoration, correct unresolved-cell annotation, and736/360/320px
layouts with no JavaScript errors or horizontal overflow. Browser evidence is
retained in`scaling_width4096_preview01`.

All findings remain study-owned empirical evidence, not promoted theory.
