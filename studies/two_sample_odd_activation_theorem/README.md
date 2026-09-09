# Odd activation for two separated inputs

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

The proved theorem in [PROOF.md](PROOF.md) covers two RMS-unit inputs
with `|rho| <= 1-delta`, `0 < delta <= 1`, and every binary label pair.
One small coefficient selected from delta alone works for all such data
and all finite physical horizons of the original three-hidden-layer
raw GF/GD model.

The activation can be a genuine convex mixture
`(1-theta) z + theta arctan(z)`. A positive mixture normalized to have
unit Gaussian second moment is also covered. The normalized coefficients
do not sum to one; a nontrivial literal convex mixture has Gaussian
second moment below one.

The proof has three companion lemmas:

- [AFFINE_CORE.md](AFFINE_CORE.md): label folding, both label sectors,
  bounded affine feature interval, frozen inactive Gaussian fields,
  uniform variance and the nonlinear regression margin.
- [SOURCE_AND_LIMIT_BRIDGE.md](SOURCE_AND_LIMIT_BRIDGE.md): source
  responses for zero offset and gains in `[1/2,1]`, cap removal,
  global physical flow, uniqueness/restart, full-sequence raw GF/GD,
  kernel, path and velocity observables.
- [INITIAL_MOTION_AND_NORMALIZATION.md](INITIAL_MOTION_AND_NORMALIZATION.md):
  both reused-transpose responses, every initial hidden block and
  sample/layer acceleration, kernel change, and coefficient normalization.

[CONTRACT.md](CONTRACT.md) fixes the authorized scope.
[EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md) tracks the claims and earlier
results. Three fresh independent complete-proof reviews pass the final
files; [REVIEW_STATUS.md](REVIEW_STATUS.md) links their reports and
[REVIEW_CERTIFICATE.json](REVIEW_CERTIFICATE.json) records exact hashes.
The mathematical source files are immutable copies identified by
[SOURCE_HASHES.json](SOURCE_HASHES.json).

This result does not cover three inputs, include either incompatible
correlation endpoint, or assert width convergence uniformly over the
infinite time interval. Unit Gaussian energy refers to the activation
and initial Gaussian propagation, not conservation of trained variance.
