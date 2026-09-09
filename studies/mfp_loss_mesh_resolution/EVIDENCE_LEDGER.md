# Evidence ledger: loss-gradient mesh removal

### C-1: fixed-schedule normalized-quadratic loss program

- Statement: At every fixed finite loss-step schedule, output and loss have deterministic width-first limits in every finite moment.
- Claim-ladder rung: exact finite program plus width identification.
- Status: Proved.
- Scope and assumptions: `q=1`, `L=2`, `phi(x)=x^2/sqrt(3)`, half-square loss.
- Supporting evidence: polynomial `NETSOR^T+Moment` closure and `temporary_quadratic_l2_order5/FIXED_H_QUADRATIC_WIDTH_LEMMA.md`.

### C-2: quadratic compact-time classical mesh limit

- Statement: The width-first loss Euler interpolants converge uniformly on compact time intervals to a continuous trace with initialized output zero and loss one half.
- Claim-ladder rung: compact-horizon identification.
- Status: Falsified.
- Supporting evidence: `temporary_quadratic_loss_initial_layer/INITIAL_LAYER_THEOREM.md` and the independent reconstruction in `FINAL_X2_RELU_MESH_VERDICT.md`.
- Mechanism: every fixed sub-label output level is hit at physical time tending to zero.
- Scope boundary: terminal paired loss at one positive time is not decided.

### C-3: terminal normalized-quadratic paired loss

- Statement: `ell_(2t)(h)-ell_t(2h)` converges to zero at `h=T/(2t)`.
- Claim-ladder rung: scalar successive-mesh convergence at one terminal time.
- Status: Open.
- Contrary/supporting evidence: the initial layer invalidates its use as a sufficient continuous-flow criterion but does not determine its terminal value; signed post-hit schedules remain uncontrolled.

### C-4: classical fixed-convention ReLU gradient flow

- Statement: A fixed value of `phi'(0)` defines a globally well-posed classical random loss-gradient dynamics.
- Claim-ladder rung: well-posedness.
- Status: Falsified.
- Supporting evidence: the explicit width-two attracting-gate construction in `FINAL_X2_RELU_MESH_VERDICT.md` and `temporary_loss_time_doubling/RELU_COMPACT_TIME_AUDIT.md`.
- Scope boundary: this does not falsify an Euler-selected Filippov/Young-measure limit.

### C-5: width-first generalized ReLU Euler mesh limit

- Statement: Hard-ReLU width-first Euler losses converge on compact time intervals to a unique restartable generalized flow.
- Claim-ladder rung: fixed-step identification, mesh convergence, uniqueness, and intended-limit identification.
- Status: Open.
- Supporting evidence: positive-homogeneity energy and norm bounds; exact frozen-gate Euler occupation law.
- Missing dependencies: hard-indicator fixed-mesh state evolution, occupation-augmented reused-adjoint OMFP, compact-time tail sewing, and uniqueness of the loss readout.
- Concrete falsifier: two vanishing mesh sequences with different limiting occupation-dependent tangent kernels or loss traces.

### Update U-1

- New evidence: normalized quadratic has a width-first initial layer; hard ReLU has an explicit classical attracting-gate obstruction but a canonical frozen Euler occupation.
- Claims upgraded: C-2 and C-4 to falsified.
- Claims unchanged: C-3 and C-5 remain open because terminal post-hit dynamics and the hard-gate population sewing theorem are independent obligations.
- Superseded conclusion: finite order paired coefficients being `O(1/t)` at physical scaling are no longer treated as evidence of compact-time mesh convergence.

### C-6: normalized-quadratic simultaneous width--mesh limit

- Statement: An Euler-consistent diagonal can restore a continuous initialized joint mean-field/loss-gradient-flow limit for normalized `x^2`.
- Claim-ladder rung: simultaneous finite-width Euler/ODE/width limit.
- Status: Falsified for an explicit nonempty class of ODE-resolving diagonals; unresolved for deliberately under-resolved diagonals.
- Proved class: with `L_n=sqrt(log n)`,
  `h_n n^14 exp(6e11 n^9/L_n) -> 0`.
- Supporting evidence: `temporary_joint_width_mesh_quadratic/JOINT_SCALING_VERDICT.md`.
- Mechanism: Euler shadows the actual finite-width ODE through a fixed output/loss change occurring by time `2/L_n -> 0`.
- Scope boundary: the natural candidate CFL scale
  `h_n=o((log n)^(1/4)/sqrt(n))` is diagnostic only; it has not been proved sufficient.

### C-7: normalized-ReLU simultaneous width--mesh limit

- Statement: Some explicit deterministic `h_n -> 0` is known to make the actual hard-ReLU Euler paths converge to a unique canonical generalized mean-field gradient flow.
- Claim-ladder rung: simultaneous hard-indicator growing-program identification and mesh removal.
- Status: Open.
- Supporting evidence: `temporary_loss_time_doubling/RELU_JOINT_WIDTH_MESH_AUDIT.md`.
- Exact partial result: at initialization, `n h_n` is the spatial gate-slab self-averaging scale; this is neither a proved necessary nor a proved sufficient pathwise criterion.
- Missing dependencies: adaptive hard-indicator reused-adjoint conditioning, growing-history concentration, joint multigate Young measures, square-tail control, and uniqueness/restartability.

### Update U-2

- New evidence: an explicit ultra-fine quadratic Euler--ODE comparison closes one simultaneous-limit regime; exact ReLU gate-slab and frozen-occupation laws isolate why a scalar `n h_n` rule is insufficient.
- Claims upgraded: quadratic joint no-go is proved for the explicit ODE-consistent class in C-6.
- Claims unchanged: arbitrary under-resolved quadratic diagonals and every canonical hard-ReLU diagonal remain open.

### C-8: local scalar ReLU joint compactness

- Statement: For every deterministic `h_n -> 0`, the actual hard-ReLU Euler predictor and loss have continuous initialized subsequential limits on a width-independent positive interval.
- Claim-ladder rung: scalar path tightness and correct initial trace, not identification or uniqueness.
- Status: Proved.
- Explicit interval: `[0,T_0]`, with `T_0=1/(384*6^4)`.
- Supporting evidence: `temporary_loss_time_doubling/RELU_NO_CONTINUOUS_LIMIT_TEST.md`.
- Mechanism: the pathwise recursion `R^+ <= R+6 h R^5` gives a uniform state bound, followed by a width-independent output Lipschitz bound and Arzela--Ascoli; `E f_n(0)^2=1/n`.
- Scope boundary: the theorem does not give a deterministic limit, a unique generalized state, or arbitrary-horizon continuation.

### Update U-3

- New evidence: ReLU cannot be assigned the quadratic instantaneous-jump verdict at the scalar level; every mesh sequence is locally precompact with the correct trace.
- Claim refined: C-7 remains open at the uniqueness/identification rung, while C-8 settles local scalar compactness positively.
