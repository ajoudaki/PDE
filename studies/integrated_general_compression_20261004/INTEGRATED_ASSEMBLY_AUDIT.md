# Integrated assembly audit

Date: 2026-10-06.

## Scope and version

This was a fresh, isolated audit of the interfaces in `RESULT.md`: headline
claims, exact statements, proof conclusions, label allowances, structural
parameters, probability and width quantifiers, all-time extensions, storage,
and scalar accuracy inversions. The entire supplied document was read.
Detailed local proofs were permitted to serve as stated dependencies for this
assembly audit. Consequently this report is not a fresh independent proof of
every source-insertion, dense, Legendre, or compact estimate.

The only scientific inputs read were this study's `RESULT.md` and
`docs/notation.qmd`. The repository `AGENTS.md` and
`/etc/codex/skills/solve-math-rigorously/SKILL.md` were read. The required
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned
permission denied. A filename-only search of the accessible skill roots found
no replacement. The explicit notation requirements in `AGENTS.md` and the
maintained notation contract were applied, but compliance with the inaccessible
additional skill cannot be claimed. No other study, author history, earlier
audit, or other reviewer's findings was read.

Initial candidate: 6052 lines, SHA-256
`1afe164bc6bc2aba3c655d9b3012e867ff42a9288c403d3a1dfb01d0dc142d01`.

During this audit the assigned author inserted the explicit source-space
definition and corrected a fragment link. The inserted passage was read in
full and checked against its downstream uses. The version currently covered
by the findings below has 6108 lines and SHA-256
`6491e6ed5a4d619c6f2507c77c4ccb9b0daa8fa6ca81108a61b37744e2f4b36b`.
The two notation repairs below were subsequently read and verified in the
candidate with SHA-256
`5debff3f8f49bd586e3408b214eea6dc9fb0a10ddee8cd99d2051c1f5fabc1b0`.
Final audited candidate: 6154 lines, SHA-256
`e24e2f519bd597159f1745ce46e9f9ad27c8772e9ef80807907b63557401c562`.
The subsequent changes were the clarified “mean squared loss” wording and
the final audit/provenance appendix. Both were read and checked. They do not
change the mathematical interfaces reviewed here. The PASS below binds to
this final candidate hash; there are no unresolved findings in this scope.

## Outcome

PASS for the assigned assembly scope. No mathematical assembly blocker was
found. The headline claims follow the stated exact interfaces and preserve
their qualifications. The two minor notation findings below have been
resolved and rechecked; neither changes a theorem or a numerical coefficient.

1. In source subsection S.3, around lines 2442–2455, the expression
   \(\|k_a^{(j)}\|_{p,n}\) denotes an empirical vector \(L^p\) norm, but
   the only supplied definition is
   \(\|M\|_{p,n}=n^{-1/p}\|M\|_{S_p}\), a normalized matrix Schatten
   norm. The latter applied literally to a column vector would give
   \(n^{-1/p}\|k_a^{(j)}\|_2\), not the intended empirical \(L^p\)
   quantity. The corrected version writes the vector quantity explicitly as
   \((n^{-1}\sum_i|k_{a,i}^{(j)}|^p)^{1/p}\), retaining the separate
   matrix definition for the Hessian estimate and defines its singular values.
   Resolved.
2. In the compact budget-inversion proof, around line 5805, the activation-only
   rate calculation starts using \(X\) without defining it within that
   subsection. The previous subsection introduced \(X=\beta^L\) with the
   restriction “only in this calculation.” The corrected version locally
   reintroduces \(X=\beta^L\) at the start of the new rate calculation.
   Resolved.

## Checked interfaces

- **Common assumptions and labels.** The normalized input variable
  \(v=x/\sqrt d\) preserves the stated sphere supremum. The proof gap
  \(\lambda=\gamma/m\) is explicit and never silently substituted for
  the unweighted global gap \(\gamma\). The four-term common label
  allowance is the intersection of the dense, Legendre, compact-runtime and
  source allowances. The headline dense and Legendre numerical envelopes
  explicitly use the smaller sufficient cap; compact preserves the complete
  recurrence interval. The zero-label case is separated before formulas
  requiring division by \(Y\).
- **Probability and width.** The common confidence convention splits failure
  budgets and takes the union of the finitely many width gates. It does not
  require independence between compression events. The source and CLT onset
  remain explicitly unquantified. The dense scalar inversion is consequently
  an eventual prescription, while compressed-order prescriptions are effective
  conditional on an admissible reference width. The document does not infer
  simultaneous success over infinitely many independently initialized widths.
- **All orders and horizons.** Legendre fitting is independent of order.
  Above its absorption threshold the signed comparison applies; below it the
  fitting bound closes the exact all-order certificate. The simple-cap proof
  retains sufficient actual-label powers to use its single stated coefficient
  in both regions. Compact starts from one finite-horizon source event and
  extends the source analyticity and real training-carrier bound
  deterministically. Its two additional extension gates are independent of
  supplied budget, source tolerance, and extended horizon. Thus neither family
  introduces a concealed order-dependent stochastic event.
- **Compact source and dimension.** The added definition specifies the four
  possible vector families and their layer endpoints, the passive backward
  recursion, the finite computed coefficient span, and the exact initialized
  additions. The additions have dimension at most \(B=2m+d+1\).
  Applying identical scalar setup operations to each initialized-image pair
  makes the paired source memberships exact. The counts \(B+4N\) for
  \(d\ge2\) and \(B+8N_1\) for \(d=1\) match the harmonic/temporal
  argument and the selection factor nine. The variable rank bound implies
  the stated supplied-budget construction without rounding a real rank bound
  upward before using the integer dimension. Small budgets in the stated
  domain use exact initialization and independent fitting. Full-coordinate
  selection at \(q\ge n\) recovers the dense flow.
- **Storage.** Dense and Legendre counts consistently separate moving state,
  fixed mixers, ordinary data, and reconstructed evaluation objects. Compact's
  moving count includes the label deficit; its all-retained inventory includes
  metrics, copies, data and named caches. Its source arrays and setup jets are
  discarded. The simplification to \(O(Lq^2)\) is supported by the compact
  baseline \(q\ge18(2m+d+9)\), and the full-width branch is separately
  handled. Legendre makes no false exactness assertion at \(q=n\).
- **Forward and inverse interfaces.** The exact Legendre envelopes are
  decreasing in the allowed integer order and tend to zero. Their stated
  sufficient inverses cover loose targets and retain the full-range second
  summand. Compact's budget certificate, baseline branch, analytic branch and
  full-width fallback supply every positive target. Its use of “exact” refers
  to unsuppressed formulas for sufficient certificates, not an optimal
  compression theorem. The headline polynomial-accuracy simplifications
  explicitly fix structural parameters and confidence. Their storage powers
  follow by substitution at the same reference width; no equality or ordering
  between \(m,d,L,1/\gamma\) is assumed.
- **Dense lower bound and comparison corollaries.** The positive coefficient
  retains its activation, depth and confidence dependence. The hypotheses
  \(m\ge2\), \(Y>0\), and the positive-time witness remain visible in
  the headline. Its independent-dense storage necessity uses confidence below
  one half and is not transferred to arbitrary representations. The final
  relative-error limit splits fixed failure budgets, compares complete
  trajectory norms, and then lets the failure tolerance decrease. It does not
  infer an endpoint lower bound or a confidence-uniform lower coefficient.

## Claim boundary

This audit supports the assembly of the stated local results. It does not
remove the source theorem's inherited proof obligations or produce a numerical
stochastic sufficient width. It does not establish minimax compression,
bounded-precision storage, efficient setup, generalization risk, or ordinary
gradient training of the compact architecture. No promotion to the maintained
book is certified here.
