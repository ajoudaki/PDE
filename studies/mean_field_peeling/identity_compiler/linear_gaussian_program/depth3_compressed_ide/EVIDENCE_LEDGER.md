# Evidence ledger: three-hidden-layer compressed IDE

> **Superseded on 20 August 2026.**  The fixed free-source/trace-class closure
> and compact-positive-time identification are proved in
> `../depth3_unfrozen_readout_closure/`.  The entries below record the earlier
> classical-source search boundary.

## Current state

| Category | Contents |
|---|---|
| Established | Exact finite-width feature-time chain; exact central reduction recorded below; exact width-limit jets through order thirteen. |
| Supported | The output-kernel moments through \(\mu_5\) satisfy every accessible Stieltjes/Hankel test. |
| Open | A genuine low-dimensional autonomous continuum closure and its positive-time width identification. |
| Superseded | The rooted-path operator construction as an answer to the compression question.  It may encode the dynamics, but violates the frozen admissibility contract. |

### C1: exact central reduction

- Statement: with (p=Bu), (q=C^{\mathsf T}v),
  (A=BB^{\mathsf T}), and feature time (s), the finite network obeys
  
  \[
  u'=B^{\mathsf T}q,\quad v'=Cp,\quad
  p'=(A+\|u\|^2I)q,\quad
  q'=(A+D+\|v\|^2I)p,
  \]
  
  \[
  A'=pq^{\mathsf T}+qp^{\mathsf T},\qquad
  D=C^{\mathsf T}C-BB^{\mathsf T}=\text{constant}.
  \]
- Claim rung: exact identity.
- Status: Proved.
- Dependencies: none beyond direct differentiation.
- Falsifier: any finite-dimensional numerical trajectory violating one of
  the displayed identities.

### C2: scalar continuum closure

- Statement: the width limit admits the field closure required by
  `PROTOCOL.md`.
- Claim rung: existence of an admissible witness.
- Status: Open.
- Supporting evidence: depth-two precedent; exact Gaussian coordinate
  recursion; positive finite Stieltjes tests.
- Contrary evidence: the two initial Wishart operators in the central
  reduction do not commute, so a naive joint spectral density loses ordered
  mixed moments.
- Cheapest resolver: derive a closed conserved pencil or a scalar
  correlation/response system and test its first three nonzero jets.
- Concrete falsifier for a proposed witness: mismatch at orders one, three,
  or five, hidden path/matrix state, or nonrestartable history dependence.

### C3: positive-time identification

- Statement: an admissible field system is the compact-physical-time
  finite-width limit.
- Claim rung: limit identification.
- Status: Open and dependent on C2.
- Concrete falsifier: a compact horizon on which the finite-width output
  remains separated from the proposed readout with nonvanishing probability.
