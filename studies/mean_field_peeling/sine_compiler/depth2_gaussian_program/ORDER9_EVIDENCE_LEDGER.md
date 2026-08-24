# Evidence ledger: depth-2 sine through order nine

### C-S9-1: frozen sine model and coefficient protocol

- Statement: `ORDER9_PROTOCOL.md` fixes the raw and unit-variance sine
  activations, the equal-width two-hidden-layer model, all-block parameter
  metric, width-first limit, coefficient convention, and forbidden
  substitutions through order nine.
- Claim-ladder rung: exact finite construction.
- Status: Exact-under-assumptions.
- Scope and assumptions: the frozen Gaussian initialization and width-limit
  Gaussian-program/detransposition rules.
- Supporting evidence: protocol SHA-256
  `366ae94d52a4b4aa7d741f807f4afe4e05a4a014e2f408837c4301ff0402bb37`.
- Contrary evidence: none identified.
- Dependencies: accepted width-limit causal skeleton.
- Cheapest decisive resolver: a theorem-level audit of that skeleton if its
  status is disputed.
- Concrete falsifier: a mismatch between the stated model and the recurrence.
- Supersedes: none.
- Superseded by: none.
- Authoritative sources: `ORDER9_PROTOCOL.md`.

### C-S9-2: derivative jets through order nine

- Statement: the raw and unit-variance sine jets in `results_order9.json` are
  the order-zero through order-nine outputs of the frozen recurrence.
- Claim-ladder rung: verified finite computation.
- Status: Exact-under-assumptions, numerically evaluated to the recorded
  precision.
- Scope and assumptions: C-S9-1 and high-precision arithmetic.
- Supporting evidence: independent Taylor and derivative-normalized
  assemblers agree in 80 serialized significant digits; 80/100-digit runs
  differ by at most (4.54\times10^{-80}) relatively; the accepted
  order-five prefix is reproduced; all even parity sectors vanish.
- Contrary evidence: none found in the frozen checks.
- Dependencies: C-S9-1 and the tilted-Wick evaluator.
- Cheapest decisive resolver: an independent implementation of the full
  order-nine detransposition recurrence.
- Concrete falsifier: a gate-valid independent implementation returning a
  different odd derivative.
- Supersedes: none; extends the prior order-five sine calculation.
- Superseded by: none.
- Authoritative sources: `sine_order9_fourier_jet.py`, `results_order9.json`,
  and `test_sine_order9.py`.

### C-S9-3: four output-coordinate coefficients

- Statement: under
  (K(y)=F'(F^{-1}(y))=F'(0)+\sum_r(-1)^r\mu_r y^{2r+2}), the order-nine
  jets determine the four recorded coefficients
  (mu_0,\mu_1,\mu_2,\mu_3).
- Claim-ladder rung: exact algebraic transformation of C-S9-2.
- Status: Exact-under-assumptions.
- Scope and assumptions: local formal series with nonzero (F'(0)); no
  positive-radius convergence claim is required.
- Supporting evidence: formal reversion/composition and the independent
  triangular identity (F'(t)=K(F(t))) agree below
  (9\times10^{-121}) relatively; 80/100-digit signs and values are stable.
- Contrary evidence: none found.
- Dependencies: C-S9-2.
- Cheapest decisive resolver: symbolic closed-form substitution in the five
  odd derivative variables.
- Concrete falsifier: disagreement of either transformation after a verified
  coefficient/index correction.
- Supersedes: none; extends the prior (mu_0,\mu_1) calculation.
- Superseded by: none.
- Authoritative sources: `sine_order9_stieltjes_audit.py` and
  `stieltjes_order9_audit.json`.

### C-S9-4: accessible Stieltjes compatibility for raw sine

- Statement: the raw-sine coefficient sequence fails every Stieltjes PSD
  condition accessible from (mu_0,\ldots,\mu_3).
- Claim-ladder rung: finite falsification of compatibility.
- Status: Falsified (the compatible-with-all-accessible-conditions claim).
- Scope and assumptions: raw (sin x), frozen model, order-nine information
  only.
- Supporting evidence: all four (mu_r) and both determinants
  (mu_0\mu_2-\mu_1^2), (mu_1\mu_3-\mu_2^2) are strictly negative with
  large precision margins; (H_0,H_0^+,H_1,H_1^+) are all non-PSD.
- Contrary evidence: none at this scope.
- Dependencies: C-S9-3.
- Cheapest decisive resolver: none needed for this finite-order statement;
  only an upstream model or coefficient correction could reopen it.
- Concrete falsifier: a verified upstream correction that makes any stored
  jet coefficient wrong enough to reverse the audit.
- Supersedes: the weaker order-five observation that only (mu_0,mu_1) are
  negative.
- Superseded by: none.
- Authoritative sources: `ORDER9_RESULTS.md` and
  `stieltjes_order9_audit.json`.

### C-S9-5: accessible Stieltjes compatibility for unit sine

- Statement: the unit-variance sine coefficient sequence fails every
  Stieltjes PSD condition accessible from (mu_0,\ldots,\mu_3).
- Claim-ladder rung: finite falsification of compatibility.
- Status: Falsified (the compatible-with-all-accessible-conditions claim).
- Scope and assumptions: (sqrt{2/(1-e^{-2})}\sin x), frozen model,
  order-nine information only.
- Supporting evidence: all four (mu_r) and both accessible Hankel
  determinants are strictly negative with stable 80/100-digit signs;
  (H_0,H_0^+,H_1,H_1^+) are all non-PSD.
- Contrary evidence: none at this scope.
- Dependencies: C-S9-3.
- Cheapest decisive resolver: none needed for this finite-order statement;
  only an upstream correction could reopen it.
- Concrete falsifier: a verified upstream correction reversing the audit.
- Supersedes: the weaker order-five observation that only (mu_0,mu_1) are
  negative.
- Superseded by: none.
- Authoritative sources: `ORDER9_RESULTS.md` and
  `stieltjes_order9_audit.json`.

### C-S9-6: arbitrary-order sine Stieltjes claim

- Statement: the finite order-nine calculation decides arbitrary-order
  moment closure, series convergence, or positive-time behavior.
- Claim-ladder rung: hierarchy convergence and limit identification.
- Status: Open; not implied by C-S9-4 or C-S9-5.
- Scope and assumptions: orders above nine or any nonlocal-in-time claim.
- Supporting evidence: none supplied here.
- Contrary evidence: the present calculation is deliberately finite-order.
- Dependencies: (F^{(11)}(0)) for (mu_4,H_2) and (F^{(13)}(0)) for
  (mu_5,H_2^+), plus separate convergence arguments for nonformal claims.
- Cheapest decisive resolver: compute the next requested finite conditions,
  or formulate a separate convergence theorem question.
- Concrete falsifier: depends on the sharper future statement.
- Supersedes: none.
- Superseded by: none.
- Authoritative sources: claim boundary in `ORDER9_PROTOCOL.md` and
  `ORDER9_RESULTS.md`.

## Causal update U-S9-1

- New evidence: order-seven/order-nine sine derivatives and
  (mu_2,\mu_3) for both scalings.
- Validity scope: the frozen two-hidden-layer width-limit model through order
  nine.
- Mechanism affected: output-coordinate Stieltjes moment compatibility.
- Claims upgraded: the earlier two-moment sign failure is strengthened to
  failure of all six scalar PSD conditions accessible at four moments.
- Claims downgraded: finite-order Stieltjes compatibility for either sine
  scaling is falsified.
- Claims unchanged and why: arbitrary-order and positive-time behavior remain
  open because finite coefficient correctness gives no convergence bridge.
- Superseded conclusion: only the weaker order-five evidence statement.
- Newly exposed dependency: (F^{(11)}(0)) and (F^{(13)}(0)) are needed for
  the next Hankel matrices.
- Authorized next branch, if any: none inferred beyond the user's order-nine
  request.
