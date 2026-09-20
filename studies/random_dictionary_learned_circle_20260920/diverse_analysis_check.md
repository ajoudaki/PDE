# Internal aggregation and selection check

2026-09-20. Read-only audit of `diverse_analyze.py`, restricted to this study.
This is internal validation, not a promotion review. No GPU work, source
changes, Git writes, or neural replay were performed.

**Finding:** no selection or aggregation defect was identified in the requested
scope. The initially checked source SHA256 is
`96151a4cfc209f53539d8e379e1cecf11e55744742f7186ea6a584b1b4a9a571`.

- **Latest two levels:** original primary/refined levels are always considered;
  each extra level is considered once its cell directory exists. Selection is
  `audited[-2:]`, independent of status, losses, or comparative performance.
  Existing incomplete extra attempts therefore remain selected and invalidate
  the cell; the code does not fall back to an older successful pair. Per-cell
  tolerances must strictly decrease, including across disjoint cohorts, and
  at most two extra levels are allowed.
- **Common configuration set:** every case contributes exactly nine closure
  rows. A row is valid only if both its closure and full reference fit, pass
  replay, and satisfy the selected-level endpoint discrepancy gate. The main
  aggregate uses the intersection where all nine rows are valid, giving every
  model the same cases. Separate method-specific summaries are explicitly
  labeled as potentially unmatched.
- **Metrics:** case RMS is `sqrt(mean(error**2))`; maximum error is
  `max(abs(error))` on the 8192-point circle grid. Aggregation takes the
  arithmetic mean and maximum of each case metric. The description correctly
  distinguishes mean case RMS from pooled RMS and sampled maxima from
  continuous-circle suprema.
- **Failure retention:** all available levels remain in `trajectories` and
  each cell's `all_levels` validation record, including superseded failures.
  Missing summaries/arrays, ordinary failed statuses, and replay failures make
  a selected cell invalid. Terminal diagnostic errors are stored separately
  from eligible learned-function errors.

CPU-only in-memory checks, run through the existing Python interpreter with
bytecode disabled, passed: zero/one/two extras select primary→refined,
refined→fine, and fine→finer; error vector `(3,-4,0)` gives RMS
`2.886751345948129`, MSE `8.333333333333334`, and maximum `4`; a single failed
model excludes its case from every model's common aggregate; retained case
values `2,4` give mean `3` and maximum `4` for all nine models; missing cell
artifacts return an explicit invalid record. No test fixture files were
created. Producer metadata was inspected only for attempted/incomplete
directories and configuration tolerances. Final scientific aggregates were
not checked because the bounded numerical runs were still completing.

**Robustness limit:** malformed `summary.json` is parsed outside the cell's
exception handler, and a corrupt NPZ may raise an uncaught `BadZipFile`.
Those corruptions would abort analysis instead of becoming invalid cell rows;
they would not silently recover an older favorable result. The lead reports
atomic summary writes and will wait for all producers before final analysis,
so no change was requested for the declared completed-writer workflow.

## Narrow follow-up: descriptive all-fitted summary

The added helper, common-case selection, CSV/JSON emission, and report section
were checked at source SHA256
`d2e7361dfc4143623220a4262e72f27b491abd0f0917aff5aa4f713711107ebc`.
The original common-valid selection and aggregation are unchanged.

The new descriptive set includes a case only if all nine closure rows satisfy
`fitted_for_descriptive_summary`. Each row still requires fitting and replay
for its closure and full reference at both selected levels. Both levels'
metrics must be present and finite; those metrics are populated only after
full/closure angle-grid agreement. Finite closure and full-reference
refinement discrepancies additionally require matching grids across levels.
The only removed gate is the upper bound of 0.01 on those discrepancies.

Every model uses the same descriptive case set. The JSON and CSV identify the
summary as not accuracy-validated and list unresolved cases; JSON retains
their failure details. The report gives the same explicit label and warning.
The primary validated summary and failure records remain intact.

An independent standard-library, in-memory test of the helper passed: a finite
discrepancy of 0.2 is admitted, either false fitting/replay flag rejects the
row, and `None`, infinity, or NaN in any required metric or discrepancy rejects
the row. No GPU work, generated-result reads, or source/Git changes occurred.
No defect was found in this narrow addition.

## Final independent numerical aggregation check

After the final analysis arrays and tables were available, an independent
CUDA 1 audit reconstructed all **108** closure/full pointwise errors at both
selected numerical levels from the saved endpoint predictions. It checked
the stored signed and absolute error arrays, then independently reduced L1,
RMS, MSE, and maximum error. It also independently recomputed the mean and
maximum of each case metric for all nine models in both the common-valid and
descriptive summaries. **All 2,496 scalar comparisons passed; the maximum
absolute difference was zero in every category.** No producer simulation or
training was run.

Evidence is retained in
`data/generated/random_dictionary_learned_circle_20260920/diverse_independent_analysis_check01/checks.json`
with a short README in that directory. The JSON contains input hashes, GPU
and library information, recomputed aggregates, exact exclusions, and the
checked analysis-source hash. CUDA required the authorized elevated execution;
the numerical audit and report creation took approximately 0.81 seconds after
Python imports.

The independent selection check examined all 120 full/closure cells, compared
selected producer summaries with their retained validation records, verified
strictly decreasing per-cell tolerances, and confirmed the latest-two rule.
There are 101 cells with two available levels, 11 with three, and 8 with four;
all available attempts remain in their validation histories.

The validated common set has **11 cases**. Its sole excluded configuration is
`quadrant_alternating`, because the selected endpoint discrepancies are
**0.010127009631221817** for `gaussian_p1` and **0.04146386790700052** for
`orthogonal_p5`, exceeding the fixed 0.01 cutoff. Both otherwise pass the
retained fit/replay gates. The descriptive common set correctly contains all
**12 cases** and remains explicitly not accuracy-validated.

This final audit independently validates the numerical reductions, selection,
and exclusions. It inherits the previously completed neural checkpoint-replay
records rather than repeating that replay. Sampled-circle maxima remain grid
statistics, and the all-fitted descriptive summary does not resolve the two
remaining refinement failures.
