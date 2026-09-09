# Evidence ledger: one-sample loss-gradient time doubling

### C-1: finite-width potential reduction

- Statement: half-MSE descent is exactly Euler ascent for
  `P=f-f^2/2`, and `ell=1/2-P`.
- Status: Proved.
- Evidence: algebraic identity in `LOSS_TIMECHANGE_ANALYSIS.md` Section 1.
- Dependencies: none.

### C-2: smooth order-five width-first expansion

- Statement: conditional on fixed-step DAG identification, flat population
  metric/adjoint intertwining, `C^6` segment regularity, and UI, equation
  (2.4) of `LOSS_ORDER5_AND_MESH_STATUS.md` is the exact expansion.
- Status: Exact-under-assumptions.
- Evidence: pullback binomial proof; independent audit of every rational
  coefficient in `LOSS_ORDER5_INDEPENDENT_AUDIT.md`.
- Concrete falsifier: failure of the stated DAG regularity or metric
  identification.

### C-3: hard ReLU/leaky leading coefficient

- Statement: if the two open hard-kink OMFP bridges hold, then
  `D_t^ell(h)=9t h^2-tD_(a,b)h|h|+o_t(h^2)`.
- Status: Exact-under-assumptions; actual-network claim open.
- Supporting evidence: exact scalar boundary identity, reused-field candidate,
  and observable-sign reduction.
- Missing dependencies: indicator-valued fixed-step width identification and
  complete marked-source response intertwining.

### C-4: finite jets decide continuous time

- Statement: some finite Taylor order, including order five, proves or
  disproves mesh removal.
- Status: Falsified as a logical implication.
- Evidence: every order-`m` paired temporal coefficient has degree at most
  `m-1` in `t`, so every fixed order is `O(1/t)` at `h=T/(2t)`, while the
  all-order remainder remains uncontrolled.

### C-5: reachable Lipschitz sewing

- Statement: activation-envelope-derived reachable bounds
  `||v||<=M_T`, `Lip(v)<=L_T`, and `Lip(ell)<=R_T` imply
  `|D_t^ell(h)|<=R_TL_TM_T t h^2 exp(2L_Tt|h|)` and dyadic convergence.
- Status: Proved conditional implication.
- Remaining obligation: establish the bounds noncircularly for nonlinear
  reused-matrix OMFP, or prove an Osgood/BV replacement.

### C-6: normalized pure-quadratic width-first initial layer

- Statement: for `phi(x)=x^2/sqrt(3)`, the first time at which the
  width-first loss-Euler output reaches any fixed `delta in (0,1)` tends to
  zero as the mesh tends to zero.
- Status: Proved.
- Evidence: `QUADRATIC_RELU_CT_HOSTILE_AUDIT.md`, Theorem 3.1.  Before the
  hit, every adaptive loss step is at least `(1-delta)h`; annealed
  positive-polynomial monotonicity compares it from below with constant-step
  feature ascent, whose width-first output diverges on every positive
  feature-time interval by the audited all-order quadratic theorem.
- Limit order: every finite loss/feature program is first taken to its width
  limit; only afterward is the mesh removed.
- Consequence: no uniform compact-time output limit with a continuous
  initialization trace.  The natural continuous Euler interpolation of the
  squared loss is not equicontinuous at zero either.
- Boundary: a discontinuous post-initial-layer limit and convergence of the
  terminal loss at each fixed positive time are not excluded.

## Current bottom line

For smooth bounded-envelope activations, the finite loss jets have ordinary
first-order Euler scaling but do not decide mesh removal.  The normalized
pure quadratic has a proved all-order width-first initial-layer obstruction,
so it has no classical continuous initial-trace flow.  The actual exact
ReLU/leaky-ReLU width-first loss-gradient flow remains open/undefined under
the current hard-kink contract.
