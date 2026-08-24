# Evidence ledger: depth-three linear network with frozen Gaussian readout

## Current state

| Category | Contents |
|---|---|
| Established | Contracting the frozen readout with the adjacent trainable matrix gives one exact active vector.  After a scalar norm/time change, the finite-width active dynamics and initialized law are the depth-two scalar-output system. |
| Established | The width-first physical MSE limit is the same autonomous single-source IDE as at depth two; compact-time convergence and global limiting loss follow by reduction. |
| Established | The frozen-readout feature jet and output-kernel moments equal the depth-two limits, not the fully trainable depth-three limits. |
| Open | A comparable O(1) closure for fully trainable depth three; training the readout creates an extra evolving \(R^TR\) term. |
| Superseded | None.  This is a new restricted-architecture theorem, not a revision of the fully trainable depth-three jet. |

### C-1: exact contraction

- Statement: For frozen \(a=A/\sqrt n\), the variables
  \(p=R^Ta,B,x\) form a closed finite-width subsystem.
- Claim-ladder rung: exact finite construction.
- Status: Proved.
- Scope and assumptions: Standard depth-three scaling, one sample, identity
  activation, \(A\) frozen and \(V,W,u\) trained.
- Supporting evidence: Direct normalized gradient equations (2.1)--(2.3).
- Contrary evidence: None.
- Dependencies: Differentiability only.
- Concrete falsifier: Feedback from a component of \(R\) orthogonal to \(a\)
  into \(p,B,x\).
- Authoritative source: THEOREM_AND_PROOF.md, Section 2.

### C-2: pathwise depth-two equivalence

- Statement: With \(q=p/\sqrt{\alpha_n}\),
  \(\alpha_n=\lVert a\rVert^2\), and
  \(\tau=\sqrt{\alpha_n}s\), the active characteristic is exactly the
  depth-two scalar characteristic, with
  \(f_n=\sqrt{\alpha_n}F_n\) and
  \(K_{3,\mathrm{fr},n}=\alpha_nK_{2,n}\).
- Claim-ladder rung: exact identification.
- Status: Proved.
- Supporting evidence: Algebraic substitution and the invariants (2.4).
- Contrary evidence: None.
- Dependencies: C-1 and \(\alpha_n>0\), which holds almost surely.
- Concrete falsifier: Any residual finite-width term after the displayed
  normalization.
- Authoritative source: THEOREM_AND_PROOF.md, Sections 1--2.

### C-3: identical initialized source

- Statement: Conditional on the frozen readout, \(q(0)\) has iid
  \(N(0,1/n)\) coordinates independently of the lower network, while
  \(\alpha_n\to1\) almost surely.
- Claim-ladder rung: source identification.
- Status: Proved.
- Supporting evidence: Conditional Gaussian covariance and the law of large
  numbers.
- Contrary evidence: None.
- Dependencies: Gaussian initialization and independence of the blocks.
- Concrete falsifier: A non-isotropic conditional covariance or surviving
  dependence of \(q(0)\) on the readout orientation.
- Authoritative source: THEOREM_AND_PROOF.md, Sections 1--2.

### C-4: autonomous positive-time MSE closure

- Statement: The same deterministic source IDE as at depth two gives the
  width-first frozen-readout depth-three output and full-MSE loss uniformly
  in probability on every compact physical horizon; its limiting physical
  solution is global and has loss tending to zero.
- Claim-ladder rung: compact-time identification and global limiting
  dynamics.
- Status: Proved by exact reduction.
- Supporting evidence: C-2/C-3, \(\alpha_n\to1\), and the established
  depth-two positive-time theorem.
- Contrary evidence: None.
- Dependencies: The prior depth-two theorem.
- Concrete falsifier: Failure of compact-time output convergence despite the
  conditional pathwise equivalence.
- Authoritative sources: THEOREM_AND_PROOF.md, Section 3; parent
  depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md.

### C-5: fully trainable depth-three boundary

- Statement: Freezing the readout is essential to this reduction.  If it is
  trained, \(p_s=\lVert a\rVert^2Bx+R^TRBx\), so the scalar contraction no
  longer closes.
- Claim-ladder rung: exact obstruction to this witness, not a no-go theorem
  for all O(1) closures.
- Status: Proved as a scope distinction; existence of another closure is
  open.
- Supporting evidence: Product-rule differentiation of \(p=R^Ta\).
- Contrary evidence: None.
- Dependencies: None beyond the full trainable equations.
- Concrete resolver: Find a conserved operator or operator-valued source
  that autonomously evolves the additional \(R^TR\) contribution.
- Authoritative source: THEOREM_AND_PROOF.md, Section 5.

### Update U-1

- New evidence: The frozen-readout jet obeys
  \(f_n^{(k)}(0)=\alpha_n^{(k+1)/2}F_{2,n}^{(k)}(0)\), so its limiting prefix
  is \((0,3,0,48,0,1464,\ldots)\).
- Validity scope: Frozen readout only.
- Mechanism affected: Effective trainable depth.
- Claims upgraded: C-2 receives an all-fixed-order derivative consequence.
- Claims unchanged and why: The fully trainable depth-three jet begins
  \((0,4,0,160,0,13888,\ldots)\); it is not superseded because it concerns a
  different architecture.
- Newly exposed dependency: The extra unit in the fully trainable initial
  kernel is exactly the readout-gradient block.
