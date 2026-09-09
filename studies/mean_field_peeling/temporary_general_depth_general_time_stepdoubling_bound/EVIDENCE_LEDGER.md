# Evidence ledger

### C-1: arbitrary fixed-horizon width-first identification

- Statement: For each fixed finite \((T,L)\) and each fixed nonzero step
  in the explicit rank interval, the expected finite-width output
  converges to the inverse-free Gaussian response DAG.
- Claim level: pointwise fixed-step theorem.
- Status: **Proved; independently audited.**
- Evidence: GENERAL_FIXED_H_IDENTIFICATION.md supplies the
  \((2T+1)(L-1)\)-action chronology, rank induction, adaptive
  row/column conditioning, compatible ideal array, quantified
  concentration induction, stopping removal, and uniform integrability.
- Limitation: neither the rank lower bound nor the compiler envelope is
  uniform in \(T\).

### C-2: quadratic cubic coefficient

- Statement:
  \[
  [\eta^3]\{F_{2t,L}(\eta)-F_{t,L}(2\eta)\}
  =t(2t-1)\kappa_{\phi,L}.
  \]
- Claim level: exact width-first singular-Price coefficient theorem.
- Status: **Proved; passed two independent adversarial re-audits.**
- Evidence: CUBIC_MARKED_BRIDGE.md constructs every order-three
  multiindex source mark, the complete \(\rho/\sigma\) binomial
  convolutions, the causal complementary-history adjoint, the singular
  Hilbert quotient, a truncated formal scalar potential, and a temporal
  coefficient induction.
- The repaired naturality proof is lexicographic in time, chronological
  action, and multiindex.  It matches every field, Gram, cross-time
  source covariance, response mark, learned contraction, and singular
  quotient before the state update.
- Important exclusion: the older compact nine-moment reduction of
  \(H_L,S_L\) is not used and remains separately unaudited.

### C-3: degree-four fifth coefficient

- Statement:
  \(F_{2t,L}^{(5)}(0)-32F_{t,L}^{(5)}(0)\) is a
  polynomial of degree at most four in \(t\).
- Claim level: exact local coefficient theorem.
- Status: **Universal formal-Euler statement proved.**  The analogous
  order-five marked-network lift is not used for an unconditional
  quantitative claim here.
- Evidence: autonomous formal Euler coefficients are polynomials of
  degree at most their order; the leading degree-five term cancels under
  step doubling.  Equivalently the universal time factors are
  \[
  d_{5,l}(t)={2t\choose l}-32{t\choose l},\qquad1\le l\le5.
  \]
- Limitation: a coefficient identity is not a uniform finite-step
  remainder.

### C-4: coupled abstract \(t^4\) remainder

- Statement: If an autonomous mixed-schedule output obeys a
  horizon-uniform fifth derivative bound \(Q\) in the \(\ell^1\)
  schedule norm, then
  \[
  |\Delta_t(\eta)-[\eta^3]\Delta_t\,\eta^3|
  \le\frac83Qt^4|\eta|^5,\qquad2t|\eta|\le\rho.
  \]
- Claim level: exact abstract theorem.
- Status: **Proved; independently audited.**
- Evidence: ABSTRACT_STEP_DOUBLING.md factors each split defect by
  \(\eta^2\), differentiates the remaining hybrid schedule three times,
  and sums the \(t\) local defects.  Its Bell recursion constructs \(Q\)
  from vector-field/observable envelopes without an output modulus.

### C-5: actual network, \(L=1\), uniform general time

- Statement: The requested sharp quadratic/quartic theorem holds with
  explicit activation-only \(B_{\phi,1},h_{\phi,1}\).
- Claim level: full quantitative theorem.
- Status: **Proved; hostile-audited.**
- Evidence: SCALAR_QUANTITATIVE_THEOREM.md gives a samplewise
  total-variation tube, terminating Bell recursion, integrable
  two-Gaussian envelope, exact oddness, and explicit activation
  coefficient.
- Sharpness: \(\phi(x)=x\) has a nonzero degree-four quintic
  coefficient.

### C-6: actual network, every fixed \((t,L)\)

- Statement:
  \[
  |\Delta_{t,L}(\eta)-t(2t-1)\kappa_{\phi,L}\eta^3|
  \le\overline{\mathcal S}_{t,L}|\eta|^5
  \]
  on the explicit fixed-horizon radius.
- Claim level: full quantitative theorem at a fixed integer time.
- Status: **Proved; independently audited.**
- Evidence: C-1, C-2, the arbitrary-horizon singular Price compiler,
  parity, and the fifth-order Taylor remainder.
- Limitation: \(\overline{\mathcal S}_{t,L}\) grows much faster than a
  polynomial in \(t\).

### C-7: actual reused-matrix network, uniform general time

- Statement:
  \[
  |\Delta_{t,L}(\eta)-t(2t-1)\kappa_{\phi,L}\eta^3|
  \le B_{\phi,L}t^4|\eta|^5,\qquad
  |\eta|\le h_{\phi,L}/t.
  \]
- Claim level: requested full theorem.
- Status: **Open for \(L\ge2\).**
- Supporting evidence: C-2 proves the cubic power, while C-4 and the
  exact \(L=1\) theorem prove the abstract remainder mechanism and its
  sharp power.
- Missing bridge: a restartable width-first mixed-schedule population
  response state, total-time Gram/moment stability, and a
  horizon-independent fifth \(\ell^1\)-schedule derivative envelope.
- Concrete falsifier: an admissible activation/depth whose coupled
  fifth remainder grows faster than \(t^4\) on a fixed total-time tube.
- Current contrary evidence: none; the obstruction is proof-theoretic,
  not a discovered counterexample.
