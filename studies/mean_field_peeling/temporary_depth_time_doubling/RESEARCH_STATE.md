# Research state: depth--time doubling

## Proved

For every fixed finite hidden depth (L\ge1) and integer (t\ge1), with
the width limit taken first at each fixed step size,

\[
 D_{t,L}(\eta)=F_{t,L}(2\eta)-F_{2t,L}(\eta)
\]

satisfies

\[
 \left|D_{t,L}(\eta)
 +\frac{t(2t-1)}2J_{\phi,L}\eta^3\right|
 \le B_\phi^{E_{L,2t}}|\eta|^5,
 \qquad |\eta|\le\frac12.
\]

Here (J_{\phi,L}) is the terminating nine-moment, two-depth-pass
recursion in `PROOF.md`, (C.1)--(C.9), (B_\phi=\max\{4,M_\phi\}), and
(E_{L,2t}) is the completely numerical terminating recursion
(T.8)--(T.15).  The shared activation base
(A_\phi=\max\{4,4M_\phi^4\}) and the two-pass numerical recursion
(M.2)--(M.4) give

\[
 |J_{\phi,L}|\le\overline J_L(A_\phi).
\]

Thus the leading time dependence is exactly quadratic and all remaining
depth/time dependence in the proved fifth-order bound is explicit.

At three hidden layers,

\[
 E_{3,2t}=6p_{2t}^{8t+2}
 +r_{2t}\frac{p_{2t}^{8t+2}-1}{p_{2t}-1},
\]

and

\[
 J_{\phi,3}=T_3+3M_3
 +4\{V_3+\beta_1+\beta_2+d^2V_1+\beta_3+dV_2\}.
\]

## Closed bridges

1. `WIDTH_DEPTH_TIME.md`: pointwise fixed-step finite-width identification,
   including adaptive reuse, response terms, rank, concentration, stopping
   removal, and terminal uniform integrability.
2. `COMPILER_DEPTH_TIME.md`: singular-covariance (C^5) Price compiler and
   explicit activation-envelope remainder.
3. `CUBIC_DEPTH_TIME.md`: fixed bounded Gaussian operators
   (W_{a,0}=I_a+J_a^*\), exact moving-query responses, generated-core
   (C^3) regularity, temporal/Euler intertwining, and the compact cubic
   law.

Independent hostile audits are recorded in `AUDIT_WIDTH.md`,
`AUDIT_COMPILER.md`, `AUDIT_UNCONDITIONAL.md`, and
`AUDIT_CUBIC_REAUDIT.md`.  The first finite-list cubic construction failed
and is retained in `AUDIT_CUBIC.md` as a superseded negative result.

## Still open

The stronger time-uniform estimate

\[
 |D_{t,L}(\eta)-\kappa_{\phi,L,t}\eta^3|
 \le C_{\phi,L}t^4|\eta|^5,
 \qquad |\eta|\le c_{\phi,L}/t,
\]

is not proved.  The fixed-(t) compiler does not imply it.  The linear
activation calculation shows that a general exponent below (t^4) is
impossible, so (t^4) is the first plausible uniform scale.

The exact time-combinatorial reduction is now proved in
`UNIFORM_BSERIES.md` and independently in `UNIFORM_DIRECT.md`: a paired
Euler macro-defect factors as \(h^2\), and oddness reduces the fifth-order
remainder to three derivatives of the transported defect, producing
exactly \(t^4\).  `AUDIT_UNIFORM_BSERIES.md` records the hostile audit.

The remaining bridge is the horizon-independent generated-core estimate
\(\mathrm{UGC}_4(\phi,L)\).  Neither fixed-horizon all-moment membership
nor the fixed-horizon Price compiler supplies it.  Ambient \(L^2\)
Banach smoothness cannot replace it because the activation Nemytskii map
need not be twice Frechet differentiable on \(L^2\), and the adjoint
response operator has no general \(L^q\to L^p\) bound for \(p>2\).

## Low-depth resolution

`UNIFORM_L1.md` proves the uniform estimate unconditionally at one hidden
layer:

\[
\left|F_{t,1}(2h)-F_{2t,1}(h)
+\frac{t(2t-1)}2J_{\phi,1}h^3\right|
\le B_{\phi,1}t^4|h|^5,
\qquad |h|\le(16M_\phi t)^{-1}.
\]

Here \(B_{\phi,1}\) is a terminating activation-envelope/Gaussian-integral
recursion.  `AUDIT_UNIFORM_L1.md` gives a hostile PASS.  The identity
activation shows that the exponent \(t^4\) is sharp.

At \(L=2\), `UNIFORM_L2.md` proves causal source-time divisibility of
strictly historical responses and a horizon-uniform \(L^2\) state-energy
bound.  It does not prove the mixed high-moment response-jet estimate
needed for the remainder.  At \(L=3\), the same unresolved connector
block occurs twice.  `AUDIT_UNIFORM_L23.md` independently concludes:
\(L=1\) proved, \(L=2\) open, \(L=3\) open.

The prospective general-depth induction is now sharper: it requires an
intrinsic causal Gaussian--Sobolev layer-transfer lemma whose base case is
the one-connector \(L=2\) system.  Step divisibility supplies the Volterra
time weights, but the required horizon-uniform mixed-moment resolvent has
not been constructed.
