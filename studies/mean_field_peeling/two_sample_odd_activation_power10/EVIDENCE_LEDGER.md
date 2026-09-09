# Exponent-ten research ledger

2026-09-07. Complete exponent-ten theorem proved in the assembled
documents. Three fresh independent complete-proof adversarial reviews
returned PASS at the final hashes.

| Claim | Level | Status and evidence |
|---|---|---|
| The original full theorem holds for the explicit c_poly delta^800 selection | Complete previously audited theorem | Unchanged dependency: ../two_sample_odd_activation_quantitative/PROOF.md |
| Whitening and normalized feature time give exact gain-free affine equations | Exact change of coordinates | Derived in NORMALIZED_GATES_AND_PRIMALS.md; independent affine route checking source form |
| Normalized gate errors cost at most C e delta^-1/2 | Deterministic capped estimate | Derived in NORMALIZED_GATES_AND_PRIMALS.md |
| Active positive affine supersolutions absorb arbitrary backward row defects q<=c M^-32 | Deterministic coefficient theorem | POSITIVE_SUPERSOLUTION.md, including signed coefficients and current diagonals; complete audits PASS |
| The actual nonlinear derivative and moment defects satisfy q<=H^30 e M^43 on the proposed box | Necessary source estimate | REFINED_RESPONSE.md, including exact backward resolvent identity and numerical ledger; complete audits PASS |
| e<=c M^-80 closes the full source construction | Complete construction theorem | POSITIVE_SUPERSOLUTION.md: 43+max(32,22+12)=77<80, all interfaces supplied; complete audits PASS |
| The same explicit c_poly with theta<=c_poly delta^10 gives the full original theorem | User's target | PROOF.md; three fresh complete-proof audits PASS |

Here M is the actual affine envelope
(3/(sqrt(2) a^3 sqrt(v)))^(1/4), not its dataset-uniform upper bound.
The conversion M<=24^(1/4)delta^-1/8 has the correct direction for
e<=c delta^10 to imply a sufficient bound of order M^-80.

## Route registry

| Route | Mechanism | Deliverable | Status |
|---|---|---|---|
| affine | Exact sample/time normalization and direct finite-program probes | Safe original-time bounds for all required affine transfer kernels, including enlarged initialization | AFFINE_SOURCE_CERTIFICATE.md complete; full audits PASS |
| response | Apply both forward and backward affine resolvents before estimating nonlinear derivatives | q<=H^30 e M^43 with current returns and cap/mesh-uniform tails | REFINED_RESPONSE.md complete; full audits PASS |
| weighted | Positive enlarged affine reference as a supersolution | Full four-coefficient comparison and two-scale homotopy closure | POSITIVE_SUPERSOLUTION.md complete; all companion interfaces supplied |
| root normalization | Normalize scalar nonlinear maps and use the raw metric for whitened first roots | Gate bounds and learned-moment differences without spurious inverse input variance | Written auxiliary component |

The current strongest route uses original feature time for response
estimates and normalized coordinates only to certify affine probes.
It does not require changing the actual model. The generic coupled
inverse and quadratic Taylor bootstrap of the delta^800 proof are
replaced by a positive supersolution. This supersedes a proof method,
not the validity of the previous theorem.

The main hostile checks are: exact probe/source identification; both
signs of coefficients in a positive majorant; random sample-gate mixing;
arbitrary temporal backward rows and current diagonal returns; forward
scale slack versus the active variance; and strict homotopy interior
without a smallest-step assumption.

The first final-audit finding was a missing printed plus in main
PROOF.md equation (8). The additive learned-moment equation was already
correct in both companion proofs. The main display was corrected and
the local feature symbol H was renamed h to avoid collision with the
numerical constant. All reviewers were notified and asked to verify the
new PROOF.md hash. No mathematical argument was changed.

Two reviewers also identified the response note's overbroad assertion
that all affine table bounds persist on the outer box. This was narrowed
to the forward strict-density and causal row bounds actually used;
backward strict-density bounds are explicitly excluded for arbitrary
row errors. Every reviewer verified the final response hash and confirmed
that no downstream estimate had used the stronger assertion.

The final mathematical proof, 19 unchanged dependencies and three
complete review reports are identified in REVIEW_CERTIFICATE.json.
The new sufficient interval is larger than the previous one by
delta^-790 for 0<delta<1, with the same prefactor. Neither sharpness
of the new power nor an improved practical prefactor has been proved.
