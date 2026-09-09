# Independent global closure pass: no closed estimate obtained

This bounded pass did **not** obtain a closed canonical continuation
estimate with finite width/mesh/cap-independent coefficients on every
finite physical horizon. It also did **not** transfer the certified
angle-specific theorem to one data-independent activation. The universal
two-sample contract remains open; the certified intermediate theorem is
unchanged.

The best attempt was continuation in the activation amplitude, keeping
the data, original Gaussian initialization, all trained blocks, and
physical two-residual gradient flow fixed. Its exact unresolved middle
term is (8) below. This is a record of where the attempted global transfer
stopped, not a new conditional continuation theorem or a promoted lemma.

## Scope and sources actually read

The target is

    one fixed genuinely nonlinear phi;
    every fixed allowed two-sample dataset D, including rho = -1;
    every finite physical T;
    the full uncut MF/GF/exact-GD and observable contract,
    with finite constants allowed to depend on D and T.

Only the activation must be data independent. A divergent constant as
rho tends to 1 is not an obstruction. The analysis used no agents,
experiments, alternative initialization, or external theorem transfer.
This report is the only file written.

Read completely:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/etc/codex/skills/investigate-conjectures/SKILL.md` and its four
  applicable references `research-contract.md`, `evidence-ledger.md`,
  `adversarial-audit.md`, and `proof-search-orchestration.md`;
- this directory's `CONTRACT.md`,
  `DATA_DEPENDENT_CONSTANTS_CLARIFICATION.md`, `READ_ME_FIRST.md`, and
  `RESEARCH_STATUS.md`;
- `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/CONTINUATION_ROUTE_REGISTRY.md`;
- `ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md`,
  `NONLINEAR_RESPONSE_PERTURBATION.md`, and
  `BOUNDED_QUARTIC_ACTUAL_FEEDBACK_TEST.md`;
- the recovered directory's `ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md` and
  `JOINT_MIDDLE_QUERY_ENERGY_AUDIT.md`.

The restart note's history definitions and final propagation obstruction
were also inspected. The skills governed the contract, route exclusions,
and claim-level separation; they did not supply a mathematical estimate.
The registry's exhausted routes were not reopened as purported progress.
In particular, this pass obtained no new result from a scalar prescribed
driver, logarithmic singular values, primal energy, an initial coefficient,
or a noncanonical example.

## The amplitude transfer tested

Take the fixed proposed endpoint
\(\phi_{\alpha_*}(z)=1+z+\alpha_*\arctan z\), \(\alpha_*=1/10\).
For a fixed dataset choose a certified starting amplitude
\(0<\alpha_0\le\min\{\epsilon_*(D)/2,\alpha_*/2\}\).
The transfer question is whether the actual flow can be controlled while
\(\alpha\) moves from \(\alpha_0\) to \(\alpha_*\), without changing
anything else in the contract.

The existing perturbation proof does not already do this. Its (65) fixes
\(A=A_0+1\), \(M=M_0+1\), obtains a constant \(K\) under those trial
coefficient bounds, and requires, among other restrictions,
\[
 \alpha\le\frac{1}{2K e^{KS}}.
\]
Here \(S\) is the certified affine feature interval and the constants
depend on its data-dependent bounds. Increasing the trial bounds changes
the constants used to prove that the trial bounds hold. Thus (64) cannot
be read as a globally closed inequality with a previously controlled
\(K\) at \(\alpha_*\). Allowing data-dependent final constants does not
discharge this internal assumption. This observation is about that proof,
not a claim that its threshold must be sharp.

To test a transfer directly, let \(\Theta_\alpha(t)\) be the actual
finite-width physical GF, coupled for all amplitudes by exactly the same
original Gaussian initial parameters. Write
\(V=\partial_\alpha\Theta_\alpha=(V_1,V_2,V_3,V_C)\).
At fixed width these derivatives exist on finite horizons: the vector
field is smooth, and the loss identity prevents finite-time escape of
the parameters. This only licenses the finite-width calculation. It
does not license a limit of the derivatives.

Use \(\langle u,v\rangle_n=u^Tv/n\) and the contract's parameter norm
\[
 \|V\|_{\mathrm{raw}}^2
 =\frac dn\|V_1\|_F^2+\|V_2\|_F^2+\|V_3\|_F^2+\|V_C\|_n^2.
\]
All quantities below are at \((\Theta_\alpha(t),\alpha)\), and each
formula retains the sample index \(a=1,2\). Put
\[
 \psi(z)=\arctan z,\quad g(z)=\psi'(z)=(1+z^2)^{-1},
 \quad d_{\ell,a}=\phi_\alpha'(z_{\ell,a}),
\]
\[
 q_{3,a}=C,\quad \delta_{\ell,a}=d_{\ell,a}q_{\ell,a},\quad
 q_{2,a}=W_3^T\delta_{3,a},\quad q_{1,a}=W_2^T\delta_{2,a}.
\]
Products of vectors are coordinatewise unless an action or inner product
is displayed. No independent copy replaces either transpose.

Separate the parameter-induced and direct activation-induced forward
variations. Define \(p_{\ell,a}=D_\Theta z_{\ell,a}[V]\) at fixed
activation, and \(u_{\ell,a}=\partial_\alpha z_{\ell,a}\) at fixed
parameters. Their exact recursions are
\[
\begin{aligned}
 p_{1,a}&=V_1x_a,&u_{1,a}&=0,\\
 p_{2,a}&=V_2h_{1,a}+W_2(d_{1,a}p_{1,a}),&
 u_{2,a}&=W_2\psi(z_{1,a}),\\
 p_{3,a}&=V_3h_{2,a}+W_3(d_{2,a}p_{2,a}),&
 u_{3,a}&=W_3\{d_{2,a}u_{2,a}+\psi(z_{2,a})\}.
\end{aligned}                                                    \tag{1}
\]
Set \(v_{\ell,a}=d_{\ell,a}u_{\ell,a}+\psi(z_{\ell,a})\).
The total preactivation variation is \(p_{\ell,a}+u_{\ell,a}\).
Consequently the exact differentiated backward gate contains
\[
 \frac d{d\alpha}\delta_{\ell,a}
 =d_{\ell,a}\frac d{d\alpha}q_{\ell,a}
  +q_{\ell,a}\big\{g(z_{\ell,a})+
       \phi_\alpha''(z_{\ell,a})(p_{\ell,a}+u_{\ell,a})\big\}.
                                                               \tag{2}
\]
In particular, changing activation does not generate only a bounded
additive \(gq\) term. It also changes the inputs of the existing nonlinear
gates through the full trained operators in (1).

## Exact physical response work and the retained term

All gradients in this paragraph use the raw metric. Partial activation
derivatives of functions of parameters keep those parameters fixed;
the derivatives in (2) are total derivatives along the amplitude family.
Differentiating
\(\dot\Theta=-\sum_a r_a\nabla f_a\), with
\(V(0)=0\), gives
\[
 \dot V=-\sum_a\left[
   (D_\Theta f_a[V]+\partial_\alpha f_a)\nabla f_a
   +r_a\{D_\Theta^2f_a V+\partial_\alpha\nabla f_a\}\right].
                                                               \tag{3}
\]
This is the actual two-residual physical equation. No population
exchange symmetry or scalar feature clock has been imposed at finite
width.

For clarity, the complete second differential appearing in its energy
is
\[
 D_\Theta^2f_a[V,V]+D_\Theta\partial_\alpha f_a[V]
 =R_a+\sum_{\ell=1}^3
  \left\langle q_{\ell,a}\phi_\alpha''(z_{\ell,a}),
          p_{\ell,a}(p_{\ell,a}+u_{\ell,a})\right\rangle_n,
                                                               \tag{4}
\]
where the remaining terms are explicitly
\[
\begin{aligned}
 R_a={}&2\langle V_C,d_{3,a}p_{3,a}\rangle_n
        +\langle V_C,v_{3,a}\rangle_n\\
 &+\sum_{\ell=2}^3
   \left\langle\delta_{\ell,a},
      V_\ell(2d_{\ell-1,a}p_{\ell-1,a}+v_{\ell-1,a})\right\rangle_n\\
 &+\sum_{\ell=1}^3
       \langle q_{\ell,a},g(z_{\ell,a})p_{\ell,a}\rangle_n.
\end{aligned}                                                    \tag{5}
\]
One can verify (4) directly by differentiating each \(Wh\) twice:
the parameter second differential gives \(2V_\ell dh\); the mixed
activation differential gives \(V_\ell v\). Moving the remaining
\(W_\ell\) actions backwards produces exactly the three local curvature
terms and the three \(g\)-terms. Differentiating the readout gives the
first line of (5). Thus the operator variations and activation source
have not been omitted.

On a common bound for the initial operator/primal sizes, loss dissipation
gives finite primal bounds on \([0,T]\), uniform in width and
\(\alpha\in[0,1/10]\). These are used here only to estimate regular
terms. Here \(C_T\) denotes a finite constant depending on the fixed
data, \(T\), and that initial bound, but not on width or amplitude.
Bounded \(\psi,g,d\), the RMS input normalization, and (1) give
\[
 \|p_{\ell,a}\|_n\le C_T\|V\|_{\mathrm{raw}},\qquad
 \|u_{\ell,a}\|_n+\|v_{\ell,a}\|_n+\|q_{\ell,a}\|_n\le C_T.
\]
Also \(\partial_\alpha f_a=\langle C,v_{3,a}\rangle_n\).
Every term in (5) is therefore bounded in absolute value by
\(C_T(\|V\|_{\mathrm{raw}}^2+\|V\|_{\mathrm{raw}})\).
Taking the inner product of (3) with \(V\) yields the unclosed inequality
\[
 \frac12\frac d{dt}\|V\|_{\mathrm{raw}}^2
       +\sum_a(D_\Theta f_a[V])^2
 \le C_T(1+\|V\|_{\mathrm{raw}}^2)+\mathcal T(t),                 \tag{6}
\]
where the entire unestimated curvature work is
\[
 \mathcal T(t)=-\sum_{a=1}^2\sum_{\ell=1}^3 r_a
  \left\langle q_{\ell,a}\phi_\alpha''(z_{\ell,a}),
       p_{\ell,a}(p_{\ell,a}+u_{\ell,a})\right\rangle_n.          \tag{7}
\]
The top and bottom summands have not been silently absorbed in \(C_T\).
Already the middle summand is unresolved. With the exact activation it is
\[
 \mathcal T_2(t)=2\alpha\sum_{a=1}^2 r_a(t)
 \left\langle
  \frac{z_{2,a}(t)}{(1+z_{2,a}(t)^2)^2}
  W_3(t)^T\!\left[C(t)\phi_\alpha'(z_{3,a}(t))\right],
  p_{2,a}(t)\left[p_{2,a}(t)+W_2(t)\arctan(z_{1,a}(t))\right]
 \right\rangle_n.                                               \tag{8}
\]
Every factor belongs to the actual canonical trajectory or its actual
amplitude derivative. In particular, \(p_2\) includes both trained
matrix variation and first-layer response in (1).

The initialized-return component is present: integrating the
actual \(W_3\) update gives
\[
 q_{2,a}(t)=W_{3,0}^T\delta_{3,a}(t)
 -\sum_b\int_0^t r_b(s)h_{2,b}(s)
       \langle\delta_{3,b}(s),\delta_{3,a}(t)\rangle_n\,ds.        \tag{9}
\]
The first term in (9) is not a fresh Gaussian independent of the other
factors in (8). The second term is retained, with its actual sign and
both sample histories. No separate estimate of either term, nor a
cancellation between them, was obtained for (8).

The immediate absolute estimate for a middle summand in (7) is only
\[
 |r_a|\,\|\phi_\alpha''\|_\infty\|q_{2,a}\|_n
       \|p_{2,a}(p_{2,a}+u_{2,a})\|_n.                            \tag{10}
\]
The last norm is not controlled by the displayed RMS bounds. A direct
Hölder estimate would introduce
\(\|p_{2,a}\|_{4,n}^2+
\|p_{2,a}\|_{4,n}\|u_{2,a}\|_{4,n}\), with
\(\|x\|_{4,n}=(n^{-1}\sum_i|x_i|^4)^{1/4}\).
No width-independent bound on these actual factors, or on their signed
pairing in (8), was proved in this pass. Decay of the curvature as
\(|z_2|\) increases does not itself relate that factor to the other
three actual factors. I obtained no such relation from the full equations.

The calculation therefore stops before a controlled transfer in
amplitude. Differentiability at each finite width is not the missing
uniform estimate. Likewise, an amplitude sensitivity estimate alone
would still need an identification argument for the new population and
the contract's derivative observables; neither is claimed here.

## Bounded candidate and final disposition

I also checked whether the bounded-quartic candidate already provides
the missing input for this global attempt. Its bounded readout and
regular upper response estimates do not control the initialized
transpose-weighted middle response. The actual terms \(\mathcal S_2^0\)
and \(\mathcal S_1^0\) in (18)--(21) of
`BOUNDED_QUARTIC_ACTUAL_FEEDBACK_TEST.md` remain exactly as recorded in
the current research status. No new estimate for either was obtained.
The old full-backprop primitive already removes the ordinary weighted
source; its remaining signed response/return work was not resolved by
this inspection either.

Thus the result of this bounded independent search is
**NO_NEW_CLOSED_ESTIMATE**. The specific failed transfer retains (8),
inside the full signed work (7), rather than a finite coefficient in
(6). No prescribed-driver theorem, primal-energy closure, log-moment
upgrade, initial jet, conditional criterion, or counterexample is offered
as a substitute. No activation is certified for all data by this pass,
and no claim that the universal theorem is false follows. All frozen
proofs, reviews, and the main task's ongoing work are untouched.
