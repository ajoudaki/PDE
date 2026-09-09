# Evidence ledger: depth-three autonomous closure search

## Current research state

| Category | Contents |
|---|---|
| Established | Exact finite-width four-map feature equations; three conserved adjacent Gram differences; exact product-map reduction; exact cyclic block identity and self-commutator invariant; exact scalar MSE clock. |
| Supported | The independent Haar bridge is the concrete obstruction to every natural depth-two-style spectral construction examined here. |
| Falsified | The particular witnesses based only on marginal outer spectra, one conserved endpoint operator, the cyclic self-commutator spectrum, or a fixed finite scalar-Gram list. |
| Open | Existence of any admissible compressed autonomous closure; an explicit fixed classical initialization source; continuum well-posedness and compact-time width-limit identification for such a closure. |
| Not tested | No derivative artifact was opened and no exact comparison through \(F^{(13)}(0)\) was run, because no admissible candidate was frozen. |
| Superseded | None. |

### C-1: exact four-map feature flow

- Statement: Equation (1.1) in INDEPENDENT_DERIVATION.md is the exact
  feature-ascent flow of \(f_n=n^{-2}A^TVWu\) after normalization.
- Claim-ladder rung: A1.
- Status: Proved.
- Scope and assumptions: One unit-norm sample, equal width, identity
  activation, all four maps trained with unit metric.
- Supporting evidence: Direct differentiation of every parameter block.
- Contrary evidence: None.
- Dependencies: None beyond differentiability.
- Cheapest decisive resolver: Differentiate the four blocks independently.
- Concrete falsifier: A missing factor, transpose, or block contribution in
  the direct gradient.
- Supersedes: None.
- Superseded by: None.
- Authoritative source: INDEPENDENT_DERIVATION.md, Section 1.

### C-2: balanced-Gram invariants

- Statement: \(C_L,C_M,C_R\) in (2.1), and \(a-b\), are exactly conserved.
- Claim-ladder rung: A2.
- Status: Proved.
- Scope and assumptions: Every finite width under C-1.
- Supporting evidence: Each derivative cancels term by term.
- Contrary evidence: None.
- Dependencies: C-1.
- Cheapest decisive resolver: Substitute (1.1) into all four derivatives.
- Concrete falsifier: One nonzero derivative.
- Supersedes: None.
- Superseded by: None.
- Authoritative source: INDEPENDENT_DERIVATION.md, Section 2.

### C-3: exact product-map reduction

- Statement: The complete output-relevant finite-width trajectory is
  projected exactly by (3.2) using \(x,y,P=DB\) and the two constant outer
  invariants.
- Claim-ladder rung: A2.
- Status: Proved.
- Scope and assumptions: Every finite width under C-1.
- Supporting evidence: Product rule plus
  \(DD^T=C_L+xx^T\), \(B^TB=C_R+yy^T\).
- Contrary evidence: None.
- Dependencies: C-1--C-2.
- Cheapest decisive resolver: Expand \(P'=D'B+DB'\).
- Concrete falsifier: Two four-map states with the same reduced data but
  different reduced derivatives.
- Supersedes: None.
- Superseded by: None.
- Authoritative source: INDEPENDENT_DERIVATION.md, Section 3.

### C-4: explicit initialization source

- Statement: The two marginal outer spectral sources are explicit, but a
  complete admissible joint source has not been constructed.  In their
  eigenbases, \(P(0)\) contains the independent Haar bridge (4.4).
- Claim-ladder rung: A3.
- Status: Open for the admissible complete source; the finite-width polar
  decomposition is proved.
- Scope and assumptions: Iid square Gaussian initialization.
- Supporting evidence: Orthogonal invariance and polar decomposition;
  individual bridge entries vanish while its norm-preserving action remains.
- Contrary evidence: Some as-yet-unknown finite classical transform of the
  typical Haar bridge might resum its mixed moments; no argument here
  excludes it.
- Dependencies: C-2--C-3 and the depth-two marginal spectral result supplied
  in the chat.
- Cheapest decisive resolver: An explicit classical-source transform whose
  finite fields reproduce arbitrary alternating bridge compositions.
- Concrete falsifier for the marginal-only witness: Two relative orthogonal
  orientations with the same marginal spectra but different mixed
  contractions.
- Supersedes: None.
- Superseded by: None.
- Authoritative source: INDEPENDENT_DERIVATION.md, Sections 4.1--4.2.

### C-5: admissible autonomous closure

- Statement: There exists a fixed finite scalar-field, one-time,
  restartable closure satisfying PROTOCOL.md.
- Claim-ladder rungs: B1, W1, H1.
- Status: Open.
- Scope and assumptions: The complete frozen contract.
- Supporting evidence: Exact finite-width reductions identify plausible
  structure, but no admissible witness.
- Contrary evidence: Every natural witness in APPROACH_REGISTRY.md either
  retains a forbidden operator/matrix or generates an unbounded word list.
- Dependencies: C-4.
- Cheapest decisive resolver: The construction stated at the end of
  APPROACH_REGISTRY.md.
- Concrete falsifier: Only a theorem excluding every permitted source/field
  construction would falsify H1; no such theorem is claimed.
- Supersedes: None.
- Superseded by: None.
- Authoritative sources: PROTOCOL.md; APPROACH_REGISTRY.md.

### C-6: physical MSE readouts

- Statement: Any valid feature-time closure converts exactly to full-MSE
  time through (8.1), with prediction \(F(s(t))\) and squared residual loss.
- Claim-ladder rung: exact conditional readout.
- Status: Proved, conditional only on having the feature trajectory.
- Scope and assumptions: One sample and full-MSE gradient flow.
- Supporting evidence: The MSE vector field is
  \(2\eta(y_\star-f)\) times the feature vector field.
- Contrary evidence: None.
- Dependencies: C-1.
- Cheapest decisive resolver: Direct chain rule.
- Concrete falsifier: A component of the MSE parameter velocity not sharing
  the common scalar multiplier.
- Supersedes: None.
- Superseded by: None.
- Authoritative source: INDEPENDENT_DERIVATION.md, Section 8.

### C-7: well-posedness and compact-time identification

- Statement: An admissible continuum closure is well posed and equals the
  width-first limit uniformly on compact physical-time intervals.
- Claim-ladder rungs: B1, E1, F1.
- Status: Open because no admissible continuum vector field/source exists
  yet to analyze.
- Scope and assumptions: Frozen contract.
- Supporting evidence: None beyond exact finite-width polynomial
  well-posedness on its maximal interval.
- Contrary evidence: None; lack of a witness is not evidence of divergence.
- Dependencies: C-4--C-5.
- Cheapest decisive resolver: First resolve C-5, then prove source
  convergence and a stopped continuous-dependence estimate.
- Concrete falsifier: A frozen candidate whose source does not converge or
  whose current-time vector field is nonunique.
- Supersedes: None.
- Superseded by: None.
- Authoritative sources: PROTOCOL.md; APPROACH_REGISTRY.md.

### C-8: derivative comparison

- Statement: A frozen candidate reproduces the independent exact
  \(F^{(k)}(0)\), \(0\le k\le13\).
- Claim-ladder rung: C/W1 coefficient check.
- Status: Not tested.
- Scope and assumptions: The preregistration in PROTOCOL.md.
- Supporting evidence: None, because there is no candidate hash.
- Contrary evidence: None.
- Dependencies: A fully explicit W1 candidate.
- Cheapest decisive resolver: Freeze such a candidate, hash it, then run the
  exact comparison once.
- Concrete falsifier: One exact coefficient mismatch.
- Supersedes: None.
- Superseded by: None.
- Authoritative source: PROTOCOL.md, Section 9.
