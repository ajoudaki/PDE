# Time-doubling comparison: research contract and claim ledger

## Contract

- Object: the exact two-hidden-layer width-\(n\) network and simultaneous
  ascent update already fixed in the quantitative width-first proofs.
- Activation: \(\phi\in C^{12}\), derivatives \(1,\ldots,12\) bounded,
  \(\phi\) of at most linear growth, and
  \(\mathbb E\phi(G)^2=1\).
- Observable: the annealed output \(F_{k,n}(h)\) after \(k\) recomputed
  steps.
- Limit order:
  \[
  F_k(h)=\lim_{n\to\infty}F_{k,n}(h)
  \quad\text{at each fixed }h,
  \qquad\text{then }h\to0.
  \]
- Main comparison:
  \[
  D_t(h)=F_t(2h)-F_{2t}(h),\qquad t\in\mathbb N.
  \]
- Requested error: a cubic leading term and an explicit fifth-order
  remainder, with coefficients derived only from Gaussian activation
  integrals and a stated activation envelope.
- Forbidden: finite-width Taylor/width interchange, output-defined
  constants, an unproved dynamic-cavity identification, and a radius chosen
  from continuity of the unknown output.
- General-\(t\) uniformity question: determine whether one fixed
  activation-only learning-rate interval and a quadratic-in-\(t\) bound are
  valid.  A shrinking explicit interval must be stated if it is necessary.

## Claim ledger

The fixed-\(t\) proof dependencies below have now been closed and
independently audited.  See FINAL_AUDIT.md, together with
WIDTH_CONCENTRATION_CLOSURE.md, REGULARITY_SUPPLEMENT.md, and
CUBIC_JET_COMPLETE_LEDGER.md.

### C1: universal cubic coefficient

- Statement:
  \[
  D_t'''(0)/6=-\frac{t(2t-1)}2\,(S_\phi+4H_\phi).
  \]
- Status: proved algebraically for the Gaussian operator DAG.
- Dependency: direct width-first nodewise cubic law for \(F_N'''(0)\).

### C2: concrete four-versus-two theorem

- Statement: an explicit \(C^{12}\) width-first bound for
  \(F_2(2h)-F_4(h)\).
- Status: proved.
- Decisive evidence: the arbitrary-finite-time conditional-innovation rank
  lemma, the nine-action response ledger, and the finite \(C^5\) compiler.

### C3: fixed-\(t\) theorem

- Statement: for every fixed integer \(t\), explicit
  \(B_{\phi,t}<\infty\), \(h_{\phi,t}>0\) give
  \[
  |D_t(h)-\kappa_{\phi,t}h^3|
  \le B_{\phi,t}|h|^5.
  \]
- Status: proved for every fixed integer \(t\).
- Constants:
  \[
  B_{\phi,t}
  =\frac{32\overline{\mathcal J}_{t,5}
  +\overline{\mathcal J}_{2t,5}}{120},
  \qquad h_{\phi,t}=1/2.
  \]
- Dependencies closed by the \(2N+1\)-action fixed-step identification,
  all-finite-time Gram-rank lemma, and terminating \(C^5\) compiler.

### C4: shared-constant all-\(t\) theorem

- Candidate statement:
  \[
  |D_t(h)-\kappa_{\phi,t}h^3|
  \le C_\phi t^4|h|^5
  \quad\text{for }|h|\le c_\phi/t.
  \]
- Status: conditional/open for the actual network.
- Falsifier: a fifth derivative or a fixed-h trajectory family growing
  faster than the displayed dependence on the claimed interval.
- Strongest obstruction: the Gram-rank and arbitrary-finite-time width bridge
  are now proved.  The remaining missing bridge is a single autonomous
  population-state/Banach stability theorem with uniform \(C^5\) bounds.

### C5: fixed interval with purely quadratic \(t\)-growth

- Candidate statement:
  \[
  |D_t(h)|\le C_\phi t^2|h|^3
  \quad\text{for all }t,\ |h|\le h_\phi
  \]
  with \(h_\phi\) independent of \(t\).
- Status: not proved and not implied by the fixed-time compiler.
- Structural concern: total training time \(2t|h|\) is unbounded; local
  activation envelopes do not by themselves control the trained trajectory.

### C6: quadratic fifth-order remainder

- Candidate statement:
  \[
  |D_t(h)-\kappa_{\phi,t}h^3|
  \le C_\phi t^2|h|^5.
  \]
- Status: false.
- Falsifier: for the admissible activation \(\phi(x)=x\),
  \[
  [h^5]D_t
  =-\frac{2452}{3}t^4+1896t^3
   -\frac{4403}{3}t^2+369t.
  \]
- Correct candidate scale: \(t^4|h|^5\), on a total-time window
  \(|h|\le c_\phi/t\); this remains conditional for the actual network.
