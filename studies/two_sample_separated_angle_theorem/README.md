# Separated-angle two-sample L3 theorem

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

Current result (2026-09-07): **proved extension, with three independent
complete-proof adversarial agent reviews returning PASS and no required
repairs.** See [the proof](PROOF.md) and [the review record](REVIEW_STATUS.md).

Target: for each fixed 0<delta<=2, select one activation phi(z)=1+z+e_delta arctan(z) for every RMS-unit input pair with correlation rho<=1-delta, all +/-1 label choices, and every finite physical horizon. Retain the original Gaussian initialization, all trained blocks, raw GD step n^-2, autonomous population flow, and the full observable contract.

The coefficient may depend on delta only. It must not depend on actual input angle, labels, dimension, width, time mesh, horizon, clipping, or a realized trajectory. The new proof does not assert one coefficient for every delta>0, convergence uniformly over the infinite time half-line, or the identical bounded activation previously used for one sample.

Files:

- [PROOF.md](PROOF.md): full statement, explicit uniform bounds and amplitude construction, and verification of all inherited lemma premises.
- [REVIEW_STATUS.md](REVIEW_STATUS.md): current result classification, exact reviewed version, scope and verdicts.
- [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md): individual claims and their evidence.
- [REVIEW_CERTIFICATE.json](REVIEW_CERTIFICATE.json): exact proof, source-manifest and review hashes.
- [SOURCE_HASHES.json](SOURCE_HASHES.json): immutable supplied mathematical source versions.
- sources/: exact copies of the recovered source proofs. Their historical draft headers are preserved. Later claims within the sources and explicit dependency statements determine their mathematical scope.
- reviews/: fresh independent adversarial reports [A](reviews/REVIEW_A.md), [B](reviews/REVIEW_B.md), and [C](reviews/REVIEW_C.md).

Provenance: source task Resume L3 proof research (2), id 01a072d1-4473-7c93-99bd-55554583c906, PDE on black-chatgpt. Source content was recovered read-only from its recorded file changes. All recovered hashes match those recorded for the original mathematical versions. The local fixed-program dependency also matches its recorded hash. Original tasks and source files were not modified or resumed.

User authorization: new theoretical proof extension and adversarial agents. No experiment, optimizer change, remote task resumption, or Git commit is part of this work.
