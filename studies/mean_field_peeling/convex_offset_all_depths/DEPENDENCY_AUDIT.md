# Dependency audit

REPORT.md supplies a standalone initialized-conditioning proof.
It invokes no unproved specialized external theorem:

- The initialized covariance recursion is derived by conditioning
  independent Gaussian matrix rows on their input features.
- The variance interval follows from the activation mean and a
  scalar affine upper recurrence.
- The strict contraction constant follows from bounded derivatives,
  full Gaussian support and compactness.
- The covariance differentiation identity is obtained by explicitly
  differentiating the bivariate Gaussian density, with the boundary
  and singular-endpoint arguments included.
- The raw kernel normalization and its actual finite initialization
  limit are derived using the stated raw metric.
- The required square Gaussian matrix norm bound is proved with
  a finite net and a scalar exponential-moment estimate.

The final isolated reviews certify only these proved initialization
and conditioning statements and their limited consequences.
They do not certify a global trained-dynamics theorem, which this
report explicitly leaves unresolved.
