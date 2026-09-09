# Fourth-power odd activation theorem

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

The [complete proof](PROOF.md) establishes the sufficient interval
0 < theta <= c_poly delta^4 for the full original odd two-input theorem.
It retains the explicit prefactor previously used with delta^10 and
delta^800. The choice c_poly delta^8 is included as well.

The argument combines [affine propagation and source probes](AFFINE_PROPAGATOR.md),
[source response using raw L2 bounds](PRIMAL_L2_RESPONSE.md), and
[positive closure with separate sample-sector bounds](SECTOR_SUPERSOLUTION.md).
The intrinsic size obeys M <= 24^(1/4) delta^(-1/8). The response forcing
costs e M^19 and the coefficient closure costs M^12. Their total exponent
31 is below the 32 supplied by delta^4.

The original global flow, nonsymmetric uniqueness and reached-state
restart, finite-interval GF/raw-GD population limits, all original
observables, nonaffinity and initial feature motion are preserved.
The universal prefactor remains extremely small; its decimal logarithm
is approximately -1004171.5712636513. Exponent four is sufficient;
optimality and a larger numerical prefactor remain open.

Three fresh independent complete-proof audits returned PASS. Their reports are linked from [REVIEW_STATUS.md](REVIEW_STATUS.md), with exact hashes in the [review certificate](REVIEW_CERTIFICATE.json). The [contract](CONTRACT.md) fixes the
research scope and the [evidence ledger](EVIDENCE_LEDGER.md) records the
claim status. [CANDIDATE_HASHES.json](CANDIDATE_HASHES.json) fixes the four
mathematical files. [DEPENDENCY_HASHES.json](DEPENDENCY_HASHES.json)
identifies 23 unchanged mathematical dependencies relative to the parent
directory.

Earlier sources referred to by basename in the companions are:

- [AFFINE_SOURCE_CERTIFICATE.md](../two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md)
- [REFINED_RESPONSE.md](../two_sample_odd_activation_power10/REFINED_RESPONSE.md)
- [POSITIVE_SUPERSOLUTION.md](../two_sample_odd_activation_power10/POSITIVE_SUPERSOLUTION.md)
- [the precise original theorem](../two_sample_odd_activation_theorem/PROOF.md)
- [the original source and limit bridge](../two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md)
- [the polynomial primal estimates and explicit constants](../two_sample_odd_activation_quantitative/PROOF.md)

Review status files and prior review opinions are not mathematical premises.
