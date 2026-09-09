# Evidence ledger

Statuses apply only to the narrow statements below.

### C-001: canonical finite-width syntax

- Statement: Equations (1.1)--(1.2) in the research contract are the exact
  mixed-metric feature and physical MSE equations for every fixed hidden
  depth.
- Claim-ladder rung: G0.
- Status: Proved.
- Scope and assumptions: one sample, equal width, no biases, all blocks
  trained, scalar coordinate activation.
- Supporting evidence: direct Hilbert-gradient chain rule; existing finite
  identities at (H=2,3).
- Contrary evidence: none.
- Dependencies: none.
- Cheapest decisive resolver: independent symbolic/finite-difference audit
  of the compiler.
- Concrete falsifier: any missing block, factor of (n), transpose, or raw
  energy term.
- Authoritative sources: `RESEARCH_CONTRACT.md`; upstream frozen contracts.

### C-001a: block-metric ambiguity

- Statement: a literal all-block Euclidean interpretation of
  \(n\nabla f_n\) is incompatible with the intended order-one kernel; the
  canonical endpoint-Hilbert/matrix-Frobenius product metric gives (1.1).
- Claim-ladder rung: G0.
- Status: Proved; wording repaired after clean-slate hostile audit.
- Supporting evidence: for a matrix block,
  \(\nabla_Gf=n^{-1}b x^{\mathsf T}=b\otimes_nx\); multiplying this again by
  (n) makes its kernel contribution order (n).
- Contrary evidence: none.
- Consequence: all prompts and proofs must state the product metric rather
  than the shorthand (n\nabla f\) on effective coordinates.
- Authoritative source: `RESEARCH_CONTRACT.md`, Section 1.

### C-002: common polynomial-action theorem for linear fixed depth

- Statement: one generic pointed-action/trace-class theorem proves G0--G5
  for identity activation at every separately fixed depth, hence for
  (H=1,2,3), without the old depth-specific invariants.
- Claim-ladder rung: G0--G5.
- Status: Proved in autonomous physical time after three hostile
  reconstructions.
- Scope and assumptions: fixed depth, iid Gaussian source, compact physical
  time.
- Supporting evidence: exact source split, rooted-word closure of every fixed
  Picard iterate, and the dimension-free loss-action estimate.
- Contrary evidence: the first audit rejected the original complex/merely
  orthogonal Fock roots, an almost-sure inference from \(O(1/n)\) variance,
  the \(|y_\star|\) finite-width energy constant, a cross-width state-norm
  comparison, and a Bochner-only nuclear-tail argument. All five were
  repaired using a real two-cyclic-sector Fock source, convergence in
  probability, \(|e_n(0)|\), a three-term scalar-signature comparison, and
  a uniform time-Lipschitz Riemann estimate. The second audit proved a new
  negative result: the unit feature-gradient Fock flow blows up at finite
  feature time for \(H\ge2\). The retained theorem is instead the autonomous
  physical residual flow, whose exact path-length estimate gives global
  continuation without a feature clock.
- Dependencies: polynomial pointed-source lemma and current-action stability,
  both reconstructed in the theorem and accepted by the final audit.
- Cheapest decisive resolver: complete.
- Concrete falsifier: a fixed-depth rooted word or raw kernel signature not
  controlled by the proposed topology.
- Authoritative sources: `linear_fixed_depth/LINEAR_FIXED_DEPTH_THEOREM.md`
  and `audits/LINEAR_PHYSICAL_FINAL_AUDIT_03.md`.

### C-003: generic shallow activation theorem

- Statement: for every \(\phi\in\mathcal A_{\rm sh}\), the (H=1) particle
  system converges uniformly on compact physical time to one autonomous
  mark-space IDE by a common characteristic/Wasserstein argument.
- Claim-ladder rung: G0--G5.
- Status: Proved after hostile reconstruction.
- Scope and assumptions: exactly the class frozen in the research contract.
- Supporting evidence: global feature characteristics, exact monotone
  finite and limiting clocks, a compact-parameter uniform strong law for
  \(F_n,K_n\), and the audited cubic envelope for \(K_s'\).
- Contrary evidence: the first draft underspecified \(\eta\ge0\) and the
  restart state. The repaired theorem retains the full marked population
  state and residual invariant; \((f,K,e)\) alone is not a restart state.
- Dependencies: none beyond the explicit iid strong law and elementary ODE
  theory proved in the theorem.
- Cheapest decisive resolver: complete.
- Concrete falsifier: finite-time escape or a residual coupling not
  Lipschitz in the chosen moment topology.
- Authoritative source: generic_l1/GENERIC_L1_THEOREM.md, including its
  recorded independent promotion audit.

### C-004: nonlinear one-action calculus

- Statement: generic rules, rather than an arctan-specific proof script,
  establish G0--G5 for arctangent at (H=2).
- Claim-ladder rung: G0--G5.
- Status: Proved after three hostile reconstructions.
- Scope and assumptions: exact unscaled arctangent and the canonical model.
- Supporting evidence: the new theorem is quantified over a nontrivial
  activation class and contains every
  \(\phi_m(x)=\int_0^x(1+u^{2m})^{-1}du\), \(m\ge1\).
  Its proof modules are NaturalCoordinate, the audited fixed-program source,
  Gaussian-envelope Osgood stability, dimension-free cutoff Euler
  comparison, raw-square uniform integrability, and Gaussian cutoff removal.
- Contrary evidence: the first draft falsely asserted local Lipschitzness of
  \((A,Z)\mapsto A d(Z)\) on \(L^2\times L^2\). A shrinking-support
  counterexample refuted it. The repaired proof clips the current multiplier
  on a fixed invariant slab and proves that the auxiliary clip is inactive. The
  audit also required a concrete probability algebra, marked-class restart,
  linear-in-cutoff stability exponent, uniform-time Euler control of \(Q\),
  and an explicit cutoff/mesh/tail limit order; all are now stated.
- Dependencies: the projective fixed-program source lemma,
  invariant-envelope ODE, two-mesh UI lemma, and cutoff/Osgood passage, all
  accepted by the final audit.
- Cheapest decisive resolver: complete.
- Concrete falsifier: a proof step whose hypothesis encodes the arctan orbit
  or uses a closed-form identity unavailable from the generic rule.
- Authoritative sources: `arctan_l2/` and
  `audits/TAME_GATE_H2_HOSTILE_AUDIT_01.md`,
  `audits/TAME_GATE_H2_REPAIRED_AUDIT_02.md`, and
  `audits/TAME_GATE_H2_FINAL_AUDIT_03.md`.

### C-005a: global second-order reduction as a claimed shortcut

- Statement: state/first-two-variation fields are uniformly Cauchy across
  meshes, with a \(p>4\) envelope, and this is used as the missing D3
  uniformization lemma.
- Claim-ladder rung: proposed G4 reduction.
- Status: Falsified as a meaningful reduction (not proved mathematically
  false). The cross-mesh Cauchy clause is already the original hard
  width/time interchange for a stronger augmented state.
- Supporting evidence: with fixed-grid identification in hand, that clause
  supplies both missing sides of the standard Euler triangle immediately.
  A fixed \(p>4\) envelope gives only a non-Osgood Hölder multiplier modulus
  and does not derive the clause.
- Consequence: C-005a may not be cited as a lemma or progress claim.
- Authoritative source:
  `arctan_l3/SECOND_ORDER_REDUCTION_HOSTILE_AUDIT.md`.

### C-005b: local correlated-multiplier/gluing theorem

- Statement: for two same-source admissible D3 configurations, a discrepancy
  augmented by the finite required two-copy tangent susceptibilities obeys
  one synchronized Euler-step estimate
  \[
   \mathcal E^+\le(1+Ca)\mathcal E
      +Ca\,\omega_{\rm loc}(|\pi|+|\pi'|)+a r_n,
  \]
  where \(\omega_{\rm loc}\) is linear or Osgood, \(r_n\to0\), and all
  constants are width/mesh independent.
- Claim-ladder rung: G4.
- Status: Open; this is the smallest presently noncircular make-or-break
  machinery theorem. An all-word traffic theorem remains a fallback only if
  a finite susceptibility closure is falsified.
- Scope and assumptions: it must control the correlated multiplier
  \(Q_2[d(Z_2)-d(\widetilde Z_2)]\), every required N-type gluing, and a
  step-summable width defect, without assuming mesh Cauchy convergence.
- Supporting evidence: exact action bounds, fixed-grid semantics, and the
  representation of the first nontrivial gluing by a two-copy first-tangent
  susceptibility. The source split isolates the only unbounded multiplier
  to the dependent action \(\Gamma_3^*B_3\); the learned term
  \(q_3^*B_3\) is coordinatewise bounded on compact time. A uniform
  subexponential tail would yield the required Osgood modulus
  \(s\log(e/s)\).
- Contrary evidence: bare \(L^2\) stability is false by a shrinking-support
  spike, and every fixed \(L^p\) ball yields only a non-Osgood Hölder
  modulus. An unrestricted source-dependent \(L^p\) action topology is also
  impossible: one Gaussian row reused as the input produces an output norm
  growing as \(n^{1/2-1/p}\). Passive cavity, innovation-mass, PSD-energy,
  and Hilbert--Schmidt-only shortcuts are already falsified.
- Dependencies: exact one-step response differentiation, derivative-count
  closure, mesh-independent moment/time-increment bounds, summable causal
  tree weights, and concentration with the factor \(a r_n\).
- Cheapest decisive resolver: prove or refute this one-step theorem for the
  exact finite raw list before attempting a global traffic law.
- Concrete falsifier: an unavoidable third-or-higher response hierarchy, a
  merely non-Osgood modulus, a width remainder without the step-size factor,
  or a susceptibility that cannot be removed from the final current state.
- Authoritative sources: `CALCULUS_SPECIFICATION.md`,
  `arctan_l3/TWO_COLOUR_FRONTIER_AUDIT.md`, and
  `arctan_l3/SECOND_ORDER_REDUCTION_HOSTILE_AUDIT.md`. A concrete sufficient
  analytic subtarget and its failed first blueprint are recorded in
  `arctan_l3/D3_CALCULUS_EXECUTION.md` and
  `arctan_l3/STOPPED_CAVITY_HOSTILE_AUDIT.md`.

### C-006: depth-three arctangent resolution by the calculus

- Statement: the promoted calculus decides every rung of the frozen D3
  contract.
- Claim-ladder rung: G0--G5 plus the D3 current-action/nuclear topology.
- Status: Not promoted. All validation gates now pass, so the D3 attempt is
  open on its merits and is blocked exactly at C-005b; C-005a has been
  rejected as circular.
- Supporting evidence: exact one-time pointed-action operator equations,
  finite-width nonexplosion, and fixed-grid semantics all compile. One
  isolated compiler emitted the nested two-colour operator (N3); another
  isolated design reduced uniformization to a mixed two-channel response
  hierarchy. A third audit proved that N3 is generically order one in
  normalized Hilbert--Schmidt scale, while also showing that this fact alone
  does not compel a new traffic state. Direct execution of every promoted
  rule then failed exactly at the middle multiplier and proved that neither
  \(L^2\), square UI, nor any one fixed \(L^p\) envelope supplies an Osgood
  stability modulus. None supplied the missing local theorem.
- Dependencies: all preceding validation gates, especially C-005b.
- Concrete falsifier: a canonical iid-Gaussian non-tight orbit or an audited
  failure of the calculus's structural class to include the exact D3 flow.
- Authoritative sources: `arctan_l3/README.md`,
  `arctan_l3/TWO_COLOUR_FRONTIER_AUDIT.md`,
  `arctan_l3/D3_CALCULUS_EXECUTION.md`, and the frozen D3 contract.

### C-007: unrestricted fixed-mesh Tensor Program backend

- Statement: after exact elimination of trained matrices into finite
  rank-one histories, every fixed-cutoff, fixed-Euler-mesh validation
  program is covered by a rigorous theorem retaining arbitrary
  forward/transpose reuse and empirical moment scalars.
- Claim-ladder rung: G3 only.
- Status: Proved as an invocation.
- Supporting evidence: Tensor Programs III, Theorem E.15, under Setup E.2
  and pseudo-Lipschitz nonlinearities/tests, removes the rank-stability
  assumption for one fixed NETSOR-transpose-plus program.
- Contrary evidence: the theorem fixes the complete program and supplies no
  constants uniform in the number of Euler lines, mesh, cutoff, or response
  order.
- Dependencies: exact SourceSplit compilation.
- Concrete falsifier: a fixed-mesh operation outside MatMul,
  coordinatewise Nonlin+, or empirical Moment, or a non-pseudo-Lipschitz
  test left untruncated.
- Authoritative source:
  audits/TENSOR_PROGRAM_FIXED_MESH_AUDIT.md.

## Current state summary

| Category | Contents |
|---|---|
| Established | Exact canonical finite-width syntax; common fixed-depth linear theorem; generic shallow theorem; tame-natural-gate H2 theorem; fixed-mesh TP backend |
| Supported | Exact D3 current-state compilation, nonexplosion, fixed-grid semantics, and the order-one two-colour frontier witness |
| Falsified | Global unit feature time at linear \(H\ge2\); ambient \(L^2\) multiplier stability; every fixed-\(L^p\) Osgood shortcut; global augmented-state Cauchy as a purported reduction; fixed-mesh or passive-cavity shortcuts |
| Open | Restartable empirical \(\psi_1\) propagation for the dependent middle action; local gluing stability; D3 raw-kernel convergence |
| Not promoted | Arctan (H=3) compact-time theorem; only formal/current-state compilation and fixed grids pass |
