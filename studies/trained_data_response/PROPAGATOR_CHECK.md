# Author-side reconstruction of the trained propagator

Checker: `/root/propagator_reconstruct`, 2026-09-11. This is an independent
author-side reconstruction, with inherited project context. It is **not** one
of the fresh isolated scientific reviews required by the study or promotion
workflow. Scope: the homogeneous population equation and its generic forcing
and whole-circle observation estimates. No training or parameter sweep was
run. Only this report is owned by this checker; no Git write was performed.

## Result and exact scope

The argument in `PROPAGATOR.md` proves a bounded homogeneous propagator in the
requested reference-weighted tangent norm, for every physical time and every
starting time. It also proves a bounded observation operator on the entire
circle, and the variation-of-constants estimate for every integrable forcing
in the clock Hilbert space. These results do not depend on an off-support
source estimate or finite-width derivative identification.

No mathematical correction to that core argument was found. Two presentation
corrections are recommended before a fresh review packet:

1. Reserve `K` for the learned Hilbert–Schmidt increment in `A=A_0+K`, and
   rename the two-by-two weighted training Gram to `Gamma` throughout.
2. After (31), state explicitly that `G Gamma^+ G*` is the orthogonal
   projection **onto** `ran G`, whereas `I-G Gamma^+ G*` is the projection
   onto its orthogonal complement. The current sentence switches between
   these two operators without identifying the switch.

The forcing assertion for every bounded-label law remains conditional on the
separate weighted passive-source estimate. A bounded homogeneous propagator
cannot supply that estimate. The finite-network derivative limit is also a
separate claim and was not audited here.

## Inputs and read coverage

The reconstruction read the complete `PROPAGATOR.md`, the study README,
`AGENTS.md`, workflow Part 1, `docs/README.md`, and `docs/NOTATION.md`. It used
the `solve-math-rigorously` and `investigate-conjectures` skills, including the
research-contract, evidence-ledger, adversarial-audit and proof-search
references. Maintained scientific inputs read completely over their relevant
proof units were:

- `global_nonlinear.md` A.1–A.4; all of B.1; C.4.1 §1 (the full-row raw
  field and normalization); C.4.5.1 §§1–3 (feature equation, fitting,
  endpoint), §5 (complete rational certificate); all of C.4.5.2 (the active
  Gaussian-source construction and endpoint passage).
- `special_data_limits.md` III.F.1–III.F.10 (complete adaptive conditioning,
  source identities, singular queries, common spaces, actual adjoints,
  Hilbert–Schmidt increments and strong/scalar differentiation).

The hidden-activity proof C.4.5.1 §4 and perturbed-law transfer proof C.4.5.3
are not dependencies of this propagator argument and were not reconstructed.
No outside theorem was imported: the needed Gaussian construction, scalar
chain rules and Gaussian moments have contained proofs in the read units.

SHA-256 inputs at check time:

| File | SHA-256 |
|---|---|
| `PROPAGATOR.md` | `0f803ef07553d6ad3c618b5d83c06af4de74393c939493f5e003509330da363c` |
| `docs/global_nonlinear.md` | `d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `AGENTS.md` | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| `RESEARCH_WORKFLOW.md` | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |

Startup HEAD was `e111b632b5a6da7fe8ccf54eb6e286422f50af96`. Other dirty
paths and the common index were preserved. The algebra-check implementation
`check_identities.py` was read, including its nonzero-readout derivative,
raw-metric and singular nonnormal factorization examples; this checker did
not execute or claim a new run of it.

## Reconstruction of the essential implications

Write `a(z)=tanh'(z)` only in this report, let `theta_*(t)` be the actual
opposite-label reference, and use the fixed Hilbert space

\[
 V=L^2(\Omega_1;\mathbb R^2)\oplus
       \mathcal S_2(H_1,H_2)\oplus H_2.
\]

For `v=(V_1,V_2,B,d)`, set
`R(t)v=((a(w_{*,j})V_j)_j,B,d)`. This map is injective and has norm at most
one. Its image, equipped with `||R(t)^{-1}·||_V`, is exactly the requested
weighted tangent domain. No lower positive bound for `a(w)` is used.
Thus the norm of the raw propagator between the time-dependent weighted
domains equals the norm of the clock propagator on `V`.

For each active input `e_j`, the full tangent fields are

\[
 h_j=a(w_j)^2V_j,\quad z_j=BH_j^1+A h_j,
\]
\[
 d_j=d\,a(Z_j^2)+c\,\tanh''(Z_j^2)z_j,
 \qquad q_j=B^*\delta_j+A^*d_j,
\]
\[
 \ell_j(v)=\langle d,H_j^2\rangle+\langle\delta_j,z_j\rangle.
\]

In particular the middle-action variation occurs in both orientations,
and `B*` is the actual adjoint variation. All these maps are bounded on
`V` because `||c||infty<=10`; no multiplication of two arbitrary varying
L2 fields appears. The exact transformed first update is
`X_j'=-2p_j r_j Q_j`. Differentiating it gives the row term
`-2p_j(ell_j Q_j+r_j q_j)`. The term obtained by differentiating the
first raw gate cancels exactly against differentiating
`delta w_j=a(w_j)V_j` in time. This confirms the generator in (11),
including the factor two for the unhalved mean loss.

These directional operations are strong directional derivatives if that
interpretation is desired: along `X+epsilon V`, the scalar clock inverse
has derivative `a(w)V`; truncating the fixed `V` and using bounded
multiplier convergence proves the L2 difference-quotient limit. Along
`c+epsilon d` and `A+epsilon B`, product subtraction then proves the other
displayed limits. This does not assert ambient Frechet differentiability.

Let `S` synthesize the two `sqrt(p_j)`-weighted columns
`(e_j Q_j,delta_j tensor H_j^1,H_j^2)` and let `(Ev)_j=sqrt(p_j)ell_j(v)`.
The rank-one Hilbert–Schmidt identity and actual adjunction give

\[
 D=R^*R,\qquad E=S^*D,\qquad
 \Gamma=ES=(RS)^*(RS)\succeq0.
\]

This identity uses `a(w)^2` in `D`, not `a(w)` or its inverse. Since
`a(w)>0` almost surely, `R` and `D` are injective. For every `alpha` in
`R^2`, `alpha^T Gamma alpha=||RS alpha||^2`; hence

\[
 \ker\Gamma=\ker S=\ker E^*,\qquad
 \operatorname{ran}E=\operatorname{ran}\Gamma.
\]

No positive lower bound for `D` follows or is needed. The finite-dimensional
range equality follows by taking orthogonal complements of the displayed
kernel equality. It removes every zero-mode obstruction to the next step.

At the endpoint, powers satisfy `(SE)^k=S Gamma^(k-1)E` for `k>=1`.
Since `E` takes values in `ran Gamma`, summing the norm-convergent series
gives, also for singular `Gamma`,

\[
 e^{-2\tau S_\infty E_\infty}
 =I+S_\infty\Gamma_\infty^+
           (e^{-2\tau\Gamma_\infty}-I)E_\infty.
\]

Diagonalization of the two-by-two nonnegative matrix bounds the last
matrix exponential difference by one. Therefore its norm is at most
`B_infty=1+L0^2||Gamma_infty^+||`, uniformly for `tau>=0`. If the Gram is
zero, its kernel identity forces `S=0`, and the propagator is the identity.
The dependence on the inverse of the smallest **positive** eigenvalue is
explicit; no continuity of pseudoinverses in time or full-rank assumption
is used. A general factorization with `ES>=0` would not suffice: for
`S=(1,0)^T`, `E=(0,1)`, one has `ES=0` but `exp(-2tSE)=I-2tSE` is unbounded.
The metric compatibility is the substantive extra fact.

The exact reference feature energy yields
`||theta(t)-theta_infty||raw<=sqrt(10)e(t)` and `e(t)<=exp(-t/5)`.
The active-source proof gives the actual endpoint decomposition
`Q_j=zeta_j+D_j`, with Gaussian variance at most ten and `|D_j|<=B_Q`.
Consequently `||Q_j||4<=3^(1/4)sqrt(10)+B_Q=M4`. This is a statement on
the same generated action spaces as the endpoint, not a marginal substitute
or finite-width higher-moment inference.

Subtraction of the finitely many `S` columns gives
`||S(t)-S_infty||<=a_* Delta(t)`. The only additional issue for `E` is
`[a(w_j)^2-a(w_j,infty)^2]Q_j,infty`. Put the multiplier difference equal
to `b`. The pointwise bound `|b|<=min(1,4|w-w_infty|)` gives
`||b||4<=2||w-w_infty||2^(1/2)`. Holder then gives

\[
 \|E(t)-E_\infty\|
 \le a_*\Delta(t)+2M_4\Delta(t)^{1/2}.
\]

This is convergence of finitely many representing vectors, hence operator
norm convergence of their finite-rank evaluation map. It does not assert
operator norm convergence for an arbitrary L2 multiplier. Residual curvature
has norm at most `2a_*e(t)`. Thus, with `L=-2SE+C`,

\[
 \int_0^\infty\|L(t)+2S_\infty E_\infty\|\,dt\le J_0<\infty,
\]

with exactly the `J0` displayed in (22): the `e(t)` term integrates to at
most five, and the `sqrt(e(t))` term to at most ten. The constants in
(12), (18)–(22) were checked by factor subtraction and square-sum bounds.

Strong continuity of `L(t)` follows by bounded multiplier continuity on
each fixed vector; separability makes its operator norm measurable. The
iterated integral series constructs a unique strong propagator on every
compact interval. Variation of constants about the bounded endpoint
semigroup and the scalar ordered-integral series give

\[
 \sup_{0\le s\le t<\infty}\|U(t,s)\|
 \le B_\infty\exp(B_\infty J_0)=C_U<\infty.
\]

This establishes the required all-physical-time propagation conclusion at
the population reference. It makes no uniform-in-time finite-width claim.

## Forcing and whole-circle conclusion that survives independently

For every strongly measurable `F in L1_loc([0,infty);V)`, the unique zero
initial solution is `v(t)=integral_0^t U(t,s)F(s) ds`, and

\[
 \sup_{t\le T}\|v(t)\|_V\le C_U\int_0^T\|F(s)\|_V\,ds.
\]

For each circle input `u`, the raw prediction gradient has block norms at
most `MC,C,1`, with `M=2+sqrt(10)` and `C=sqrt(10)`. Composing with `R(t)`
therefore gives the observation bound `sup_u|ell(t,u)v|<=L0||v||V`.
The same bounded-multiplier argument proves continuity in `u`. It follows
that the observation map is bounded into `C(S^1)`, uniformly in all time,
and that the forced response has bound
`sup_(t<=T,u)|ell(t,u)v(t)|<=L0 C_U integral_0^T||F(s)||V ds`.

For the actual signed data source, the row integrand is
`u_j a(w·u)Q(u)/a(w_j)`. For arbitrary circle inputs, neither
`||A||op<infty` nor the active-query L4 lemma alone bounds this product.
The weighted passive-source estimate must establish its uniform L2 norm
and Bochner measurability. Once it gives
`sup_t||F_sigma(t)||V<=C_source,Y||sigma||TV`, the requested linear-in-T
state and prediction estimates follow immediately from the preceding two
displays. Their constant would be `C_U C_source,Y` and `L0` times that,
respectively. This report does not replace that source obligation by an
ambient bounded-action assumption.

As a narrower unconditional example, if the input projection of `sigma`
is supported on `{+e1,-e1,+e2,-e2}`, the ratio cancels its own gate because
`a` is even; each source column has norm at most `L0` and the residual is
at most `C+Y`. Thus
`||F_sigma(t)||V<=2(C+Y)L0||sigma||TV` for all time. This permits arbitrary
label measures at those inputs and needs no minimum atom mass. It is only
a scoped consequence, not a resolution of the full-circle source problem.

The core propagation route is therefore complete at the author-check level.
Fresh complete isolated reviews and the actual passive-source/capture
components remain outside this report's acceptance scope.
