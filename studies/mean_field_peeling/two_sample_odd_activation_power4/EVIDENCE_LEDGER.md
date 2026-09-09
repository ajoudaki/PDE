# Exponent-four evidence ledger

2026-09-07. The complete theorem has passed three fresh independent full-proof audits. All final mathematical and dependency hashes match; the written reports and integrity certificate are recorded in REVIEW_STATUS.md and REVIEW_CERTIFICATE.json.

| Claim | Status | Mathematical evidence |
|---|---|---|
| Full theorem for c_poly delta^10 | Previously proved; sufficient exponent improved here | ../two_sample_odd_activation_power10/PROOF.md |
| Full raw affine propagator is bounded by C M^3 | Proved | AFFINE_PROPAGATOR.md §§1–2: all four gradient contributions, exact balances, integrated radius-one Hessian |
| Actual affine source arrays obey the sharper active-sector bounds | Proved | AFFINE_PROPAGATOR.md §§3–4: independent-root probe identity, beta positivity, exact original-time conversion |
| Cap/mesh-uniform nonlinear forcing is at most H^30 e M^19 | Proved on the stated source box | PRIMAL_L2_RESPONSE.md: subGaussian bounds control the exponential; actual primal L2 bounds control its single incoming-field multiplier |
| Signed coefficient system closes at q <= H^-16 M^-12 | Proved | SECTOR_SUPERSOLUTION.md: distinct active/inactive backward radii, positive beta slack, exact backward reconstruction and strict/row/strict sandwiches |
| Full theorem for c_poly delta^4, hence also delta^8 | Proved; three final independent complete-proof PASS reports | PROOF.md: 19+12=31<32, with M <= 24^(1/4) delta^(-1/8); all original downstream bridge premises checked |
| Exponent four is optimal | Open; not asserted | The proof gives a sufficient coefficient only |
| A practical-size universal prefactor works | Open | c_poly remains unchanged and extremely small |
| The analogous polynomial result for three inputs | Not established in this work | The present proof uses the two-input sector structure |

## Supersession and unused routes

The delta^4 sufficient interval contains the previously established
delta^10 and delta^800 intervals with the same prefactor. Their proofs
remain valid and unchanged. The safer intermediate delta^8 route is
subsumed by the complete delta^4 result.

A Gaussian covariance-majorization approach was considered as an
alternative route. No conclusion here relies on such a lemma. The
raw-L2 Holder estimate supplies the required improvement directly.
No failed or unused route is evidence that a smaller exponent is
impossible.

## Hostile audit and revisions

Three fresh reviewers read all four mathematical files, checked their
hashes and the 23 unchanged mathematical dependencies, and inspected
the needed original source proofs. Each audited the complete theorem,
with different emphasis on affine propagation/probes, source response,
and sector supersolutions. Historical and sibling reviews were excluded
from their proof evidence.

Two points were corrected before the final reviews:

1. The affine numerical product was safely rounded to 10^30 exp(2100),
   which is still smaller than the existing envelope H. The prior
   displayed 10^29 rounding did not dominate the full rounded product.
2. The expected backward-row estimate now explicitly means
   max_k E[sum_j |defect_kj|]. The maximum is outside expectation.
   The deterministic L-row expansion and uniform-in-time Holder bound
   prove exactly this quantity, which controls the deterministic
   coefficient row norm. No random temporal maximum is claimed.

The audits checked current backward diagonals, random sample-gate
mixing, absence of a smallest-mesh-step hypothesis, finite initialized
readout, fixed-program limit order, asymmetric physical comparison,
reached-state restart, and ordered velocity/product truncation. They
found no additional old exponent-ten amplitude restriction in the
remaining bridges. These are mathematical agent audits, not a
machine-checked formalization.
