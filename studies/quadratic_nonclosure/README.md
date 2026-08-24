# Quadratic nonclosure laboratory

This is the analytical negative laboratory for the prescribed quadratic
Taylor/Wick closure. It is intentionally a flat collection of reports; there
was historically no coherent numerical pipeline to force into code and
results directories. The later preregistered CPU and GPU campaigns are kept
here beside those reports because they test the same canonical model and
claim boundary.

Suggested reading order:

1. [`approximate_single_source_conjecture_resolution.md`](approximate_single_source_conjecture_resolution.md)
2. [`approximate_single_source_stability.md`](approximate_single_source_stability.md)
3. [`adversarial_audit_report.md`](adversarial_audit_report.md)
4. [`mean_field_single_source_conjecture_audited_resolution.md`](mean_field_single_source_conjecture_audited_resolution.md) — conditional tagged-site comparison, not a derived DMFT
5. [`normalized_mean_field_taylor_closure_audit.md`](normalized_mean_field_taylor_closure_audit.md)
6. [`QUADRATIC_MUP_NONCLOSURE_MASTER_REPORT.md`](QUADRATIC_MUP_NONCLOSURE_MASTER_REPORT.md)

The exact special quadratic forest compiler establishes the **formal
annealed** fixed-order jet and its factorial lower bound, so the prescribed
positive Wick–Taylor closure family has zero radius and is not uniformly
Cauchy.  Those Taylor/DMFT reports alone did not identify an actual
positive-time width-first trajectory.  The later covariant-Schur theorem
nevertheless resolves the frozen canonical conjecture negatively: with high
probability the predictor makes a fixed increase in vanishing physical time,
contradicting compact-time convergence to any continuous readout.  See
[`CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md`](../mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md).

The tagged-site Volterra/DMFT equation in item 4 is postulated rather than
derived.  Its no-positive-delay comparison is exact under the asserted
representation and response hypotheses (the hitting time is zero if defined);
the step loss additionally assumes a monotone, no-overshoot relaxed selection.
It is therefore not an established result about the canonical network.  The
normalized results are exact for the
displayed frozen monomial cutoffs, not a general full-system no-compression
theorem.  None of these results rules out every singular, signed,
operator/integro-differential, or otherwise non-Taylor finite causal PDE.

## Preregistered finite-width campaigns

The 23 August 2026 numerical campaigns and their frozen protocols are:

1. [`QUADRATIC_L2_JOINT_LIMIT_PREREGISTRATION_2026-08-23.md`](QUADRATIC_L2_JOINT_LIMIT_PREREGISTRATION_2026-08-23.md)
2. [`QUADRATIC_L2_JOINT_LIMIT_RESULTS_2026-08-23.md`](QUADRATIC_L2_JOINT_LIMIT_RESULTS_2026-08-23.md)
3. [`QUADRATIC_L2_GPU_LARGE_WIDTH_PREREGISTRATION_2026-08-23.md`](QUADRATIC_L2_GPU_LARGE_WIDTH_PREREGISTRATION_2026-08-23.md)
4. [`QUADRATIC_L2_GPU_LARGE_WIDTH_RESULTS_2026-08-23.md`](QUADRATIC_L2_GPU_LARGE_WIDTH_RESULTS_2026-08-23.md)

Across the tested CPU widths \(128\)--\(2048\) and GPU widths
\(2048\)--\(32768\), the registered diagnostics found a resolved positive
time scale and no polynomially visible collapse toward zero. This is valid
finite-width evidence, not a positive limiting theorem and not a refutation
of the covariant-Schur result. The theorem's boundary layer occurs on a
vanishing logarithmic time scale and may therefore remain invisible on every
polynomially accessible width ladder used by these experiments.
