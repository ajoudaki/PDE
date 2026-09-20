# Bounded internal check of the endpoint comparison

2026-09-20. Reviewer: scoped agent `/root/endpoint_internal_check`.
This is an internal mathematical check, not a promotion review, a new
research campaign, or a numerical training experiment.

**Verdict: accepted for the stated exact-population, single-input scope.**
No substantive correctness objection remains to the endpoint identity,
coefficient-metric kernel, tail bound, or frozen-state source identity.
The conclusion is an exact identity and a conditional endpoint certificate;
it is not an a priori closure-order rate or a finite-width all-time result.

## Inputs, coverage, and independence

The scientific assignment permitted only `ENDPOINT_ROUTE.md`,
`ROUTE_DYNAMICS.md`, `docs/NOTATION.md`, and the needed arguments in
`docs/global_nonlinear.md` B.1, C.4.5.1, and C.4.7.10.B. The supervisor
subsequently permitted the small exact-arithmetic `validate_endpoint.py`.
The complete original candidate (318 lines), complete dynamics dependency
(523 lines), complete notation contract (98 lines), and complete validation
script (44 lines) were read. The first amended candidate's lines 204–241
were reread; that version had 321 lines and clarified three boundary/
interpretation points described below without changing a formula. The
supervisor then added the bounded physical-time corollaries (11a)–(11b).
The final candidate's lines 204–278 and the complete final validation script
(56 lines) were read, and that script was rerun. The final candidate has
346 lines.
The initially truncated aggregate dynamics read was repaired by complete
reads of lines 1–265 and 266–523.

The following maintained-source intervals were read completely:

- `docs/global_nonlinear.md:1903–2221`: B.1 theorem/model normalization,
  scalar transform, and the full local/global existence and uniqueness
  argument needed here. Its later finite-width/GD proofs were not reread.
- `docs/global_nonlinear.md:5475–5782`: C.4.5.1 §§1–3, including raw metric,
  strong-curve chain rule, readout norm convexity, fitting, and endpoint
  arguments. The two-input symmetry is not imported into the one-input model.
- `docs/global_nonlinear.md:5999–6103`: C.4.5.1 §5, including the complete
  rational Gaussian certificate and its source code. The unrelated §4
  feature-motion argument was not read or needed.
- `docs/global_nonlinear.md:13161–13430`: complete C.4.7.10.B, including
  initialization, H3 dictionary/ridge, actual adjunction, positive filters,
  Frobenius invariance under whitening, and the stated compatibility scope.

Required process instructions `AGENTS.md`, `RESEARCH_WORKFLOW.md`, and the
complete `solve-math-rigorously/SKILL.md` were read. No study README, other
study artifact, other review, chat/history, or Git data was read. No candidate
or dependency was edited. The only written artifact is this report.

The candidate's references to `RESULT.md`, other studies, and their
nullspace/trapping constructions were not followed. They are motivational
or scope discussions rather than dependencies of equations (1)–(13). Their
individual historical claims, including the last paragraph's p=1 families,
are outside this check. No scientific input is missing for the endpoint
result under the supplied single-input dynamics.

SHA-256 input records:

```text
ENDPOINT_ROUTE.md, original fully read version
336b53958fd31444764f05f0a94fce1536f44385d956f772b88a5af181074f76
ENDPOINT_ROUTE.md, intermediate boundary-wording amendment checked here
d1b7e470d358cf1047d250671faf35851d2da0e96264850d88da4135222cb42a
ENDPOINT_ROUTE.md, final version including (11a)–(11b)
e57fb40981905bdbcd7cf632f7a71761b2016bebe440fae8b59289ce4e5cea52
ROUTE_DYNAMICS.md
f84da8b5a840079a239ae8b2ffd4c12359f8abab08f27d831e0534f2ac2fa755
validate_endpoint.py, original checked version
de196ad1b1c5542aec3f46c6c0e6dd62de29732a6be9a2574d671edb347e2892
validate_endpoint.py, final checked and rerun version
b999fc58208cfd14283607332af7e472b1ead2d19db6e49c4b630737eb7cb1d8
docs/NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
docs/global_nonlinear.md, whole-file version marker, not whole-file coverage
81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c
docs/global_nonlinear.md:1903–2221, exact line bytes with line endings
ed6e1527b6adb85d802a4d16c7290f104bed3e1afc7e64f866711ef2547cde87
docs/global_nonlinear.md:5475–5782
662a76beba7ab61e669600b76edacf2845358dd89fd970f2153dbbb8545eed79
docs/global_nonlinear.md:5999–6103
630c6d0105132f667d834a72f7fde1aec7f96f6ac23b7b2523d61709e9c2513b
docs/global_nonlinear.md:13161–13430
b77fb96abfbf592faa64e401d4456f52c087723737df667abe834f6eea217380
AGENTS.md
7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747
RESEARCH_WORKFLOW.md
0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85
/etc/codex/skills/solve-math-rigorously/SKILL.md
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
```

## Substantive checks

### Dynamics, metric, and scalar chain rule

The setting is the bias-free two-hidden-layer tanh population network,
normalized training input `u=e_1`, label one, zero limiting readout,
`||A_0||op<=2`, actual adjoint, unhalved loss, and unit population block
mobilities corresponding to finite mobilities `(n,1,n)`. These agree with
the notation contract. The factor `ds/dt=2(1-b)` is correct for one atom.
The single-input initial value is `m=v>1/5`; the two-input reference's
`v/2` is not copied into the new argument.

The transformed equations in `ROUTE_DYNAMICS.md` give a global feature
curve and strong C1 raw rows and HS increments on every bounded feature
interval. Bounded tanh derivatives and the readout supremum bound suffice
for their integral contraction. Closure existence follows by the same
argument with fixed bounded coefficient maps, and does not need the
two-arc law or short-time domain of the earlier comparison theorem.

For a strongly C1 L2 curve `z(s)`, put
`v_h=(z(s+h)-z(s))/h -> z_s` in L2. The scalar fundamental theorem gives
the difference quotient of tanh as `a_h v_h`, where `|a_h|<=1` and
`a_h -> tanh'(z(s))` in probability. Multiplication of a fixed L2 vector
by these bounded multipliers converges strongly, by truncating that vector
and then using bounded convergence in probability. The contribution of
`v_h-z_s` is at most its L2 norm. This proves the asserted strong-curve
chain rule without unrestricted L2 Frechet differentiability. The product
rule for `AH_u` holds because its action curve is C1 in operator norm
(the learned part is C1 in HS). Scalar prediction differentiation then
uses the continuous L2 pairing with `c`.

Writing the hidden differential as `J`, the feature dynamics imply
`c_ss=JJ*c` and `b_s=||h||²+||J*c||²`. For `g=||c||`, the identity
`g_ss=(||h||²-g_s²+||J*c||²)/g>=0`, its initial slope `sqrt(m)`, and
`g_s<=||h||` prove `||h||²>=m` and `b_s>=m`. The same proof holds in
row L2 plus coefficient Frobenius metric for the closure, with `m_N>0`.
It would not justify replacing that metric by the HS norm of `K_N`.

### Matched training levels and the endpoint identity

Since `b_s>=m>0`, there is one level-one feature time, with a C1 inverse
`s(z)` on `[0,1]`, using one-sided derivatives at endpoints. The closure
has its own inverse because `m_N>0`. Bounded `b_s` near the level-one
feature time makes physical time diverge there. Consequently both levels
one are the original physical-flow endpoints.

The passive raw gradient blocks are
`(tanh'(w.u)p_u u, delta_u tensor H_u, h_u)`. For the closure the middle
block is `(U_2*delta_u)(U_1*H_u)^T`; the other blocks use its actual
current action. Their pairings with the training gradient give precisely
(6) and (7), including the factor `u_1` from `u.e_1`. In particular the
closure's middle term is
`<delta_u,Q_2 delta_e1><H_u,Q_1 H_e1>`.
Pairing two filtered increment velocities instead would produce `Q_2²`
and `Q_1²` and is wrong unless special idempotence identities happen to hold.

Division by the positive training derivative gives `F_z=kappa/k` and
`(F_N)_z=kappa_N/k_N`. All fields and gradient blocks are jointly
continuous in `(z,u)` in their stated Hilbert spaces, using bounded
multipliers and the strong raw curves. Thus the ratios are continuous
on the compact level/circle domain and their integrals define elements
of `C(S^1)`. Both initial readouts are zero. Integrating gives (3), and
common-denominator subtraction gives exactly
`R_N-R=(Delta kappa-R Delta k)/k_N`. The supremum/integral inequality
in (5) is in the correct direction and retains signed cancellation only
in (3). Common positive rescaling of the kernel column cancels exactly.
At `e_1` the two ratios equal one; oddness gives ratio minus one at
`-e_1`. No identification of the two state metrics is required.

### Path length, constants, and stopping certificate

The length identity is exact:
`integral ||theta_s|| ds = integral dz/sqrt(k(z))`.
Its upper bound `(z_1-z_0)/sqrt(m)` controls each parameter displacement
from its initial value. For the closure it controls `M_N-D_N` in
Frobenius norm, and contraction of `U_1,U_2` gives the stated action bound.
The three passive gradient bounds are consequently `||A||||c||`,
`||c||`, and one in the appropriate metric. Cauchy–Schwarz gives
`|kappa|/k<=||G_u||/sqrt(k)<=C(m)/sqrt(m)` and its closure analogue.
This proves (10), and splitting the signed integral at `1-alpha`
proves (11) for every `alpha in [0,1]`.

Expanding the square gives
`T(a)^2=a^-1+5a^-2+4a^(-5/2)+a^-3`, which is strictly decreasing for
`a>0`. Substitution yields both displayed exact expressions for
`T(1/5)^2` and `T(9/50)^2`. The rational upper bounds for the square
roots prove `T(m)<22`, `T(m_N)<25` whenever `m>1/5`, `m_N>=9/50`.

In the original candidate, “below 47 alpha” was not strictly true at
`alpha=0`; the formulas themselves were valid. Also finite physical
stopping applies to `alpha>0`, whereas `alpha=0` denotes the limiting
physical endpoints. The final amendment correctly states both facts.
It also makes explicit that (11) uses the actual whole-circle population
discrepancy. That discrepancy remains unknown until independently bounded
or evaluated with justified errors. Matching the training predictions
does not certify it. A finite mesh, numerical integration, or finite-width
estimate is not supplied. For positive tolerance, `alpha=epsilon/94<=1`
reserves at most half the tolerance for the two endpoint tails.

The final addition (11a) is also valid: use (10) for each trajectory's
own residual `1-b(t)` or `1-b_N(t)`, then insert the two physical residual
decay bounds and apply the triangle inequality at the same physical time.
At `t=40`, `2mt>16` and `2m_Nt>=72/5`, so its tail is bounded above by
`22 exp(-16)+25 exp(-72/5)<17/10^6`, proving (11b). The final script
certifies the latter strict inequality using exact rational positive
exponential partial sums through degree 80: each partial sum is below
the exponential, hence its reciprocal is an upper bound for the negative
exponential. This is a finite-horizon-to-endpoint population transfer.
The same-time whole-circle discrepancy at time 40 still needs its own bound.

### Frozen-state omitted-rank source

For rank-one operators, self-adjointness of the positive filters gives
`<J_u,Q_2 J_e1 Q_1>HS=<delta_u,Q_2 delta_e1><H_u,Q_1 H_e1>`.
Subtracting the unfiltered pairing proves the first identity in §4 with
`E=Q_2 J_e1 Q_1-J_e1`. This is exactly the signed middle source inside
`ROUTE_DYNAMICS.md` (15), since `K_s=J_e1` in feature time.
The modified diagonal remains at least `||h||²>=m`: its row term is
nonnegative and its middle term is a product of nonnegative quadratic
forms. Applying the quotient identity with this positive denominator
proves (12); Hilbert-space Cauchy–Schwarz proves (13).

This diagnostic freezes the exact action and all fields and modifies only
the middle tangent pairing. It does not compare the two trained states.
Therefore it cannot replace their full kernel difference in (4), and it
does not control initialized-action error or subsequent feature feedback.
The candidate expressly preserves this distinction.

## Executed check and limits

Working directory: `/home/amir/Codes/PDE`. Python 3.10.12. Command:

```sh
python3 studies/single_input_closure_rate_20260920/validate_endpoint.py
```

Exit status zero. Observed output:

```text
PASS: rational tail constants, nonprojector metric, defect identity, speed cancellation
```

Both versions of the script were read before execution and exited zero
with the displayed output. The final version additionally checks the
time-40 exponential tail. It uses exact Fractions for the tail margins,
a non-idempotent positive-filter example, the source identity, and speed
cancellation. These tiny checks support the hand derivations;
they are not a substitute for the general Hilbert-space argument. The
maintained Gaussian quadrature certificate was inspected, not rerun.
No training, quadrature, optimizer modification, or Git operation occurred.

No rate in dictionary degree/order `N` (or `p`) follows from this result.
No stability-free estimate from the accumulated H3 source alone follows.
No arbitrary two-input scalar reduction is proved. The all-physical-time
statements concern the population flows; the separately fixed-horizon
finite-width/GD limits are not upgraded. `m_N=0` is excluded, and the
constants deteriorate as positive `m_N` tends to zero. Numerical arithmetic,
quadrature, and mesh errors remain separate. Subject to these explicit
limits, the final candidate has passed this bounded internal check.

## Final-version follow-up

The original check applied to `336b5395…` and the boundary-wording amendment
`d1b7e470…`; both records and their original read coverage are retained above.
The follow-up applied only to the new (11a)–(11b) material in candidate
`e57fb409…` and the updated arithmetic script `b999fc58…`, with complete
hashes recorded above. Separate residual tails, same-physical-time triangle
inequality, and the exact reciprocal-series arithmetic all pass. The final
script rerun exited zero. No new objection or broader claim was introduced.
The bounded internal check is complete for this final candidate.
