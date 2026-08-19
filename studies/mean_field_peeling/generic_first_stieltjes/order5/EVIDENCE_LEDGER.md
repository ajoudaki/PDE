# Evidence ledger: generic H=2, B=1 order five

Status values: open, candidate, algebraically-audited, theorem-level, failed.

| ID | Claim | Required evidence | Current status |
|---|---|---|---|
| O5-1 | Six-family finite-width identity for \(D_n^5f_n\) | independent tensor differentiation and raw-coordinate jet equality | algebraically-audited |
| O5-2 | Complete leading-width peel | equality partitions, width valuation, Wick--Stein and transpose-response ledger | algebraically-audited |
| O5-3 | Fully flattened unit-Gram moment polynomial for \(C\) | explicit sparse expression using only declared \(M_\nu\) atoms | algebraically-audited |
| O5-4 | Independent atomwise agreement | separately generated coefficient maps and exact diff | algebraically-audited |
| O5-5 | Parity through order four | exact finite-width readout involution and symbolic zero checks | algebraically-audited |
| O5-6 | Linear and quadratic certificates | exact substitution yielding prescribed triples and \(\mu_0,\mu_1\) | algebraically-audited |
| O5-7 | Constant, affine, nonpolynomial controls | exact controls and preregistered finite-width regression | algebraically-audited |
| O5-8 | Annealed large-width limit | exact fixed-program encoding plus theorem hypotheses and \(L^p\)/UI bridge | theorem-level |
| O5-9 | Padé-induced loss curve | algebra from accepted \(A,B,C\), with domain/singularity caveats | algebraically-audited |

## Promotion rule

Empirical agreement cannot promote O5-2, O5-3, O5-4, or O5-8.  A failed
mandatory control demotes the affected formula to failed.  If O5-3 or O5-4
remains open, the final report must enumerate the exact unresolved peeling
branches and may not present a response recursion as the requested answer.

## Final evidence summary

- The finite-width six-family identity passed direct product rules, exact
  rational polynomial equality, two seedwise derivative routes, and raw
  tensor contraction checks.
- The unit maps have 3/46/974 monomials for \(A/B/C\); independent exact
  rational comparison has zero discrepancies.
- The layer-tagged and fully symbolic-\(Q^0\) maps have 3/50/1045 graded
  terms; the six-point exact interpolation, unused \(Q^0=7/2\) holdout, and
  post-freeze literal comparison all have zero discrepancies.  The frozen
  independent symbolic map SHA-256 is
  `e682c708fedadc577b7446a7b9c07b79262c945fbae5726918436153876f889a`.
- Constant, linear, affine, quadratic, parity, and normalized-sine gates all
  pass.  The normalized-sine width extrapolation differs from theory by
  1.2873 standard errors under the preregistered rule.
- The theorem-level label is conditional on the polynomial-smooth fixed-
  program hypotheses in the self-contained report.  In a weaker convergence
  tier, a separate uniform \(L^{1+\epsilon}\) moment bound is required for
  uniform integrability and expectation convergence.
