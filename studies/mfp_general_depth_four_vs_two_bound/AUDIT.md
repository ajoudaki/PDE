# Independent audit record

## Scope

The authoritative quantitative claim is `THEOREM.md`, supported by
`WIDTH_AND_RANK.md` and `COMPILER_AND_CONSTANTS.md`.  The optional
factorization in `CUBIC_COEFFICIENT.md` and `TEMPORAL_CUBIC_LAW.md` is a
separate claim and is not a theorem dependency.

## Audit outcomes

| Audit | Independently reconstructed | Verdict |
|---|---|---|
| Fixed-width audit | finite updates, \(9(L-1)\) action chronology, adaptive row/column conditioning, reused-column response cancellation, ranks, concentration, stopping removal, UI | Pass |
| Compiler audit | singular Price identity, exact signed ledger, absolute envelope ledger, \(C^{12}\) count, call count, constants, Taylor factor, epsilon corollary | Pass |
| Full hostile audit | every implication from the actual finite network to the final quantitative inequality | Pass |
| Coefficient-factor audit A | candidate \(\kappa_{42}=6\kappa_{21}\) marked-response intertwining | Fail/open |
| Coefficient-factor audit B | same candidate, with an explicit missing-source counterexample to the displayed adjoint sum | Fail/open |

## Defects found and disposition

1. Early coefficient drafts conflated exact signed jets with absolute
   envelope bars.  They were split into the signed ledger
   (2.10a)--(2.10g) and the dominating recursion (2.11)--(2.16).
2. The first call lacked an explicit response initialization.  The compiler
   now states and proves \(\sigma_{\ell,00}=0\), alongside the initial
   feature and cotangent Grams.
3. The fixed-step interval was implicit in the theorem statement.  It now
   explicitly states \(|h|\le1/(8\sqrt{\mathcal S_{4,L}})\), which contains
   both the fine argument \(\eta\) and coarse argument \(2\eta\).
4. The compact coefficient description did not point explicitly to the
   signed ledger.  It now does.
5. A proposed proof of \(\kappa_{42}=6\kappa_{21}\) matched covariance jets
   but did not enlarge the response sums to all marked source histories.
   Both candidate files now label this bridge open, and the result was not
   inserted into the theorem.
6. All detected equation-rendering defects were repaired; a final literal
   and control-character scan is clean.

## Requirement matrix

| Required bridge | Location | Status |
|---|---|---|
| Exact finite-width network and updates | `THEOREM.md` (0.1)--(0.4) | Pass |
| Pointwise fixed-\(h\) width limit | `WIDTH_AND_RANK.md`, Sections 4--5 | Pass |
| Adaptive reused-matrix conditioning | `WIDTH_AND_RANK.md`, Section 4 | Pass |
| Gram/response concentration and UI | `WIDTH_AND_RANK.md`, Section 5 | Pass |
| Explicit rank interval | `WIDTH_AND_RANK.md`, Lemma 3.1 | Pass |
| Singular-covariance \(C^5\) regularity | `COMPILER_AND_CONSTANTS.md`, Section 2 | Pass |
| Direct Gaussian-integral cubic coefficient | signed ledger (2.10a)--(2.10g), output rule (4.1) | Pass |
| Activation-envelope fifth remainder | `COMPILER_AND_CONSTANTS.md`, Sections 3--4 | Pass |
| Explicit depth factors | equations (3.10)--(3.14) there | Pass |

## Final verdict

The quantitative theorem

\[
 |F_{4,L}(\eta)-F_{2,L}(2\eta)-\kappa_{42,\phi,L}\eta^3|
 \le B_{\phi,42}(L)|\eta|^5
\]

passes the three independent audits above.  The stronger closed-form
factorization \(\kappa_{42}=6\kappa_{21}\) remains open and is not needed
for this verdict.

