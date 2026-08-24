# Evidence ledger: autonomous depth-two linear MSE closure

## Current research state

| Category | Contents |
|---|---|
| Established | Exact finite-width invariant/spectral reduction; deterministic one-source continuum limit; locally well-posed and restartable physical-time IDE; compact-physical-time convergence in probability; global limiting MSE trajectory with loss tending to zero. |
| Independently checked | The source moments and induced formal feature jet match the existing Gaussian-program calculation through \(F^{(81)}(0)\) and all 40 previously computed output-kernel moments. |
| Not required | Any all-order Stieltjes representation or Hankel-positivity theorem. |
| Open | Whether the continuum closure admits an elementary finite-dimensional ODE, whether it is minimal among autonomous closures, and whether the output-kernel moment sequence is Stieltjes at every order. |
| Superseded | The earlier classification of the spectral construction as only an all-fixed-order formal closure. That classification was correct for the evidence then available; the positive-time bridge is now supplied by source-measure convergence and ODE stability. |

### C-1: exact finite-width reduction

- Statement: The one-sample depth-two identity feature flow conserves
  \(C_n=BB^T-xx^T\) and
  \(\delta_n=\lVert x\rVert^2-\lVert y\rVert^2\), and is exactly equivalent
  to the matrix-measure oscillator in Section 3 of the proof.
- Claim-ladder rung: exact finite-dimensional algebra.
- Status: Proved.
- Scope and assumptions: Equal width, identity activation, one
  unit-normalized sample, all three effective parameter blocks trained with
  the frozen unit metric.
- Supporting evidence: Direct differentiation and spectral functional
  calculus.
- Contrary evidence: None.
- Dependencies: Differentiability and the real symmetric spectral theorem.
- Concrete falsifier: A displayed finite-width solution for which either
  invariant changes or the spectral norm identity fails.
- Authoritative sources: THEOREM_AND_PROOF.md, Sections 3 and 5; parent
  PROTOCOL.md and DERIVATION.md.

### C-2: deterministic single source

- Statement: The random matrix-valued sources converge entrywise weakly in
  probability to \(\operatorname{diag}(\rho_x,\rho_v)\), with zero cross
  measure, and this is exactly encoded by the scalar measure \(\nu\) and the
  initial profiles in (1.3)--(1.4).
- Claim-ladder rung: positive-width-limit theorem for initialization data.
- Status: Proved, using standard random-matrix inputs.
- Scope and assumptions: Independent Gaussian initialization with variance
  \(1/n\) in normalized coordinates.
- Supporting evidence: Marchenko--Pastur convergence, the Bai--Yin edge
  limit, Sherman--Morrison, conditional Gaussian quadratic-form
  concentration, and polynomial approximation.
- Contrary evidence: None. The negative atom at \(-1/2\) is required rather
  than anomalous.
- Dependencies: The two cited random-matrix theorems.
- Concrete falsifier: A bounded continuous spectral test function whose
  corresponding source entry does not converge to (4.3)--(4.5).
- Authoritative sources: THEOREM_AND_PROOF.md, Section 4;
  Marchenko--Pastur (1967); Bai--Yin (1993).

### C-3: autonomous IDE and loss readout

- Statement: Equations (1.5)--(1.8) define a locally Lipschitz autonomous
  vector field on a fixed Hilbert space times \(\mathbb R\), preserve
  \(f+e=y_\star\), and have loss \(L=e^2\).
- Claim-ladder rung: continuum well-posedness and observable identification.
- Status: Proved.
- Scope and assumptions: The explicit compactly supported source \(\nu\);
  the full-MSE convention gives the factor \(2\eta\).
- Supporting evidence: Bounded multiplication by \(\lambda\), continuity of
  the quadratic integral maps, Picard--Lindelof, and the internal derivative
  identity for \(\operatorname{Re}\int\overline\psi\pi\,d\nu+e\).
- Contrary evidence: None.
- Dependencies: C-2.
- Concrete falsifier: Two solutions from one state, dependence on prior
  history, or failure of the preserved output/residual identity.
- Authoritative source: THEOREM_AND_PROOF.md, Sections 1 and 5.

### C-4: positive-time mean-field identification

- Statement: For each finite physical horizon, the finite-width outputs and
  full-MSE losses converge uniformly in probability to the IDE readouts.
- Claim-ladder rung: positive-time mean-field theorem.
- Status: Proved.
- Scope and assumptions: Width first; any fixed finite physical time; fixed
  real label and positive learning rate.
- Supporting evidence: Weak source convergence, stopped bounded-solution
  estimates, uniform weak-integral convergence over the compact family of
  limiting mode products, Gronwall stability, and stability of the exact
  scalar MSE clock.
- Contrary evidence: None.
- Dependencies: C-1--C-3.
- Concrete falsifier: A finite time and positive-probability subsequence on
  which the supremum output/loss error stays bounded away from zero.
- Authoritative source: THEOREM_AND_PROOF.md, Section 5.

### C-5: global physical-time loss dynamics

- Statement: Feature time has a finite blow-up at each end, but its output is
  a strictly increasing bijection onto \(\mathbb R\); the physical MSE clock
  approaches the finite feature coordinate matching the label and never
  reaches it at finite physical time. Consequently the limiting loss is
  global and tends to zero.
- Claim-ladder rung: global analysis of the limiting IDE.
- Status: Proved.
- Scope and assumptions: Every fixed real label and \(\eta>0\).
- Supporting evidence:
  \(K\ge2r^2-r/2\), \(r_{ss}\ge3r^2\) for positive feature time,
  time-reversal/channel symmetry, and logarithmic divergence of the clock
  integral at the target.
- Contrary evidence: None.
- Dependencies: C-3.
- Concrete falsifier: A finite target not reached by the feature output,
  finite physical-time escape, residual sign change, or nonzero limiting
  residual.
- Authoritative source: THEOREM_AND_PROOF.md, Section 6.

### C-6: O(1), single-source, non-vacuous classification

- Statement: The closure uses one fixed one-dimensional spectral domain, one
  scalar measure, one complex field/velocity pair, and one scalar residual,
  independent of width and derivative order. It contains no trajectory
  playback, growing moment list, or external time forcing.
- Claim-ladder rung: requested representation theorem.
- Status: Proved by construction.
- Scope and assumptions: O(1) means fixed field/domain complexity, as frozen
  in PROTOCOL.md; it does not mean a finite-dimensional state with no
  continuum coordinate.
- Supporting evidence: The explicit formulas (1.3)--(1.8), restartability in
  C-3, and finite-width identification in C-4.
- Contrary evidence: None.
- Dependencies: C-1--C-4.
- Concrete falsifier: Any hidden \(n\)-dependent source, required stored
  history, or loss readout not determined by the current IDE state.
- Authoritative sources: PROTOCOL.md; THEOREM_AND_PROOF.md, Sections 1 and 8.

### C-7: relation to the Stieltjes conjecture

- Statement: The IDE determines the entire output-coordinate kernel
  \(\mathcal K(f)\) independently of an all-order Stieltjes representation;
  that conjecture is a further specialization about a transformed moment
  expansion.
- Claim-ladder rung: scope separation.
- Status: Proved for the logical implication and construction; all-order
  Stieltjes positivity remains open.
- Supporting evidence: Strict invertibility of the feature output and (7.1);
  the integral source retains all spectral moments without truncation.
- Contrary evidence: None. Existing \(H_d,H_d^+\) tests through \(d=19\)
  support but do not prove the specialization.
- Dependencies: C-5.
- Concrete falsifier: Dependence of IDE existence or MSE identification on
  an unproved Hankel inequality.
- Authoritative sources: THEOREM_AND_PROOF.md, Section 7; parent
  depth2_all_order_search/RESULTS.md.

### Verification update U-1

- New evidence: test_autonomous_mse_closure.py verifies the scalar-source
  density decomposition, the exact initial readouts
  \((r,F,K)=(1,0,3)\), and the formal derivative prefix through order 13.
- Independent inherited evidence: The parent spectral-closure test verifies
  the source moment sequences and the independent spectral recurrence
  against the accepted derivative and forty-moment artifacts; the production
  comparison reaches order 81. A fresh read-only recomputation reproduced
  every derivative entry through order 81 exactly.
- Claim impact: These are regression and normalization checks for C-2/C-3.
  The proof of C-4 is analytic and does not rely on finite jet agreement.
- Test result: Both three-test suites pass when run from their respective
  directories.
- Newly exposed dependency: None.
- Authorized next branch: A numerical quadrature implementation may be added
  for plotting loss curves, but is not needed for the theorem.
