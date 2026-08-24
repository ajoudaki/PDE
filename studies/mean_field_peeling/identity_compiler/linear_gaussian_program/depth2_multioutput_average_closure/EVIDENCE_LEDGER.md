# Evidence ledger: multi-output fixed-aggregate closure

## Current state

| Category | Contents |
|---|---|
| Established | A fixed output aggregate selects one exact active head; after scaling by \(\gamma=\lVert c\rVert^2\), its finite-width characteristic is the scalar-output characteristic. The prior single-source positive-time theorem therefore transfers directly. |
| Established | For fixed output count, every individual output has the rank-one deterministic limit \(f_a=(c_a/\gamma)g_c\). |
| Open | Identification of ordinary vector-MSE training with the arithmetic-average orbit from generic finite-width initialization. |
| Out of scope | Simultaneously growing output dimension without an output-count/time normalization and generic time-dependent output directions. |

### C-1: one active output-head direction

- Statement: Under feature ascent of \(g_c=\sum_ac_af_a\), the aggregate
  head \(x_c=\sum_ac_ax_a\) and shared variables form a closed finite-width
  subsystem; every head direction orthogonal to \(c\) is frozen.
- Claim-ladder rung: exact finite construction.
- Status: Proved.
- Supporting evidence: Direct differentiation, equations (1.1)--(1.2).
- Concrete falsifier: An orthogonal head combination with nonzero derivative
  or feedback into \(x_c,B,y\).
- Authoritative source: RESULTS.md, Section 1.

### C-2: exact scalar-output equivalence

- Statement: With \(\widehat x=x_c/\sqrt\gamma\) and
  \(\tau=\sqrt\gamma s\), the active finite-width flow and initialized law are
  exactly those of the scalar-output model.
- Claim-ladder rung: exact identification.
- Status: Proved.
- Supporting evidence: Equation (1.4); Gaussian linear-combination law.
- Concrete falsifier: Any remaining dependence on \(m\) or \(c\) beyond
  \(\gamma\) after the displayed transformation.
- Authoritative source: RESULTS.md, Section 1.

### C-3: inherited autonomous physical-time IDE

- Statement: The same scalar source measure and field pair, with the factors
  \(\sqrt\gamma\) and \(\gamma\) in (2.4), give the compact-time width limit
  and global limiting scalar-aggregate MSE loss.
- Claim-ladder rung: positive-time and all-physical-time identification.
- Status: Proved by exact reduction to the prior theorem.
- Supporting evidence: C-2 and the established scalar-output closure; the
  residual/output conservation identity in Section 2.
- Concrete falsifier: Failure of the transformed physical clock or loss
  readout despite the pathwise feature-flow equivalence.
- Authoritative sources: RESULTS.md, Section 2; parent
  depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md.

### C-4: individual-output rank-one limit

- Statement: For fixed \(m\), uniformly on compact physical-time intervals,
  \(f_a-(c_a/\gamma)g_c\to0\) in probability.
- Claim-ladder rung: observable identification beyond the aggregate.
- Status: Proved.
- Supporting evidence: The exact frozen remainder (4.1), its Gaussian
  independence from the active state, and conditional variance (4.3).
- Concrete falsifier: A fixed head whose orthogonal remainder has an
  order-one output on a compact interval.
- Authoritative source: RESULTS.md, Section 4.

### C-5: ordinary vector MSE

- Statement: Generic vector MSE is not yet identified with this fixed-average
  closure; its residual-weighted output direction is time dependent off the
  symmetric orbit.
- Claim-ladder rung: scope/next bridge.
- Status: Open.
- Supporting evidence: Direct vector-loss gradient; the fixed-direction
  hypothesis used in C-1.
- Concrete resolver: Prove propagation of the equal-output orbit in the
  deterministic width limit and compact-time convergence to it, or exhibit a
  surviving transverse mode.
- Authoritative source: RESULTS.md, Section 5.
