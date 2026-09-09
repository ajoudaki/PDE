# Hostile validity addendum for the frozen nonpolynomial regression

**Freeze status:** fixed before any producer prediction is opened.

The experiment in
[`../common/NONPOLYNOMIAL_EXPERIMENT_CONTRACT.md`](../common/NONPOLYNOMIAL_EXPERIMENT_CONTRACT.md)
is mechanism-preserving: normalized sine keeps every forward variance equal
to one, is smooth and nonpolynomial, and activates all derivative channels.
The affine `1/n` fit is acceptable only as a preregistered finite-width
extrapolator; exact deep-linear controls already show that higher powers of
`1/n` generally exist.  The chi-square gate therefore remains mandatory and
a pass is empirical support, never an algebraic proof.

Before execution, the following numerical details are fixed:

1. use deterministic, nonoverlapping integer seeds for every `(H,n)` cell;
2. no seed may be removed unless its jet is nonfinite; any nonfinite value
   invalidates that cell and makes the experiment inconclusive;
3. compute each cell's mean and ordinary unbiased sample-variance standard
   error, then use weights `1/SE^2` in the declared affine fit;
4. report cell counts, means, standard errors, the fitted intercept and
   slope, intercept standard error, residual chi-square and its three-minus-
   two `=2` degrees of freedom, and every exclusion;
5. split every cell into four consecutive seed batches and require that no
   batch mean differs from its cell mean by more than five batch standard
   errors; violation is a heavy-tail/seed-instability invalidity gate, not a
   failure of the formula;
6. first compare the two independent moving-flow oracles seedwise at widths
   `1,2,5` and both depths.  Their worst scaled discrepancy must be at most
   `1e-10` before any population comparison is interpreted;
7. do not inspect, tune, or replace the affine fit using a quadratic fit after
   seeing the prediction.  Curvature that fails the declared chi-square gate
   yields `inconclusive`.

These clauses narrow numerical interpretation without changing the frozen
activation, widths, budget, fit, or decision thresholds.

