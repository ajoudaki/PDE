# Bounded static review of p7 execution and reporting

Scope: `p7_run.py`, `p7_analyze.py`, `p7_merge.py`, `p7_plots.py`, and
their directly referenced current-study suite helpers. The review read
code only. It did not execute a producer, analyzer, merger, or plotter,
read other studies' scientific contents, inspect live numerical outcomes,
or change any source recorded by a running producer.

## Finding: complete the historical-reference provenance check (resolved)

**P2, reporting validation.** In the reviewed `p7_merge.py`, lines 45--50
read the historical metrics, validation, comparisons, gates, and endpoint
prediction archive directly. Unlike the new p7 analysis chunks, this
historical base is not checked against its saved provenance manifest hash
or its output hashes. The final provenance at line 78 records only the
historical metrics hash. Therefore an altered historical validation,
comparison, gate, or prediction artifact could be merged without being
detected by this code.

There is a second part of the same identity requirement: line 57 checks
that the new and historical primary/refined dense-reference paths agree,
but does not compare the reference array hashes retained in each audit's
attempt records. A changed archive at the same path could otherwise be
used for fresh p7 metrics while the old methods' metrics retain an earlier
reference function.

Before publication, the merger should:

1. Verify the historical base completion and manifest hash.
2. Require every reused historical artifact's actual hash to match the
   base provenance's declared hash, and record these checked hashes.
3. Match the selected primary/refined full-reference `arrays_sha256`
   values, as well as their paths, between each selected p7 chunk and
   the historical base validation.

These checks belong in the reporting merger and do not require modifying
the frozen training producer. This review found a missing validation
condition; it did **not** find or infer an actual changed artifact.

## Scientific checks that passed static inspection

- The producer constructs only `new_p7`, with 26 lower and 46 upper
  vectors, and preflight requires the actual p5 prefix and nonzero finite
  readout to remain unchanged.
- The total-vector count is 72 and the middle coefficient count is 1196.
  Among archived totals 8, 45, and 149, the nearest to 72 is 45. The
  preceding derivative count 38 is compared separately.
- Each current row uses the manifest-selected dense endpoint pair; the
  merged rows require matching reference paths. Both numerical levels
  participate in a verdict, and disagreement or invalidity yields an
  inconclusive verdict.
- Numerical refinement selects the latest pair after the single
  eligible extra attempt, with the old attempt paths preserved; it does
  not choose the pair by the best discrepancy score.
- The merge requires all eleven cases. Coverage counts are consistent:
  132 historical rows plus eleven p7 rows give 143 metric rows; 143
  historical validation cells plus eleven give 154; 99 historical
  comparisons plus 44 give 143 comparisons.
- Plots place each method at its actual total-vector count, keep
  unvalidated diagnostics explicitly marked, and label the 72-versus-45
  comparison as a nearest available size rather than an exact size match.
  Artist-coordinate and table-text checks compare rendered values with
  source metrics. The endpoint caption correctly specifies each model's
  own first detected training-MSE crossing.
- The p7 analyzer imports the saved-state audit and independent forward
  arithmetic, not the candidate producer or builder. Its added source
  audit requires the p7 builder, Gaussian contractions, runner, protocol,
  specification, and derivations to match the recorded hashes.

No other actionable scientific comparison, dimension, selection, or
plot-coordinate flaw was found within this static scope. Running results,
plot appearance, and source/data hashes were not executed or independently
verified by this review.

## Resolution check

The supervisor subsequently changed only the reporting merger. The
reviewed `p7_merge.py` now requires the historical provenance manifest
hash to equal the current manifest hash, and checks the actual hashes of
all six reused historical artifacts (`metrics`, `validation`,
`comparisons`, `gates`, `endpoint_predictions`, and `completion`) against
the historical provenance declarations. The final provenance retains
all six checked hashes and the historical provenance file's hash.

For every case it also requires both selected dense-reference paths and
the `arrays_sha256` values of their last two attempts to agree between
the historical validation and fresh p7 validation. This closes the
same-path/different-reference loophole identified above.

The saved `p7_analysis_final01/provenance.json` contains these six
historical artifact hashes, the historical provenance hash, and eleven
selected p7 cases. Its executed merger hash matches the source inspected
for this resolution. The historical base completion says `complete`,
and the new merge completion records eleven valid p7 rows among 143
total rows. This resolution check inspected source and saved metadata;
it did not rerun the merger, scientific analysis, plotting, or GPU work.

**The reporting-provenance finding is resolved. No finding remains open
within this bounded review.** Plot appearance and the independent raw
audit were handled separately by the supervisor, not re-reviewed here.
