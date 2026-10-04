# Large fixed labels: what changes, and a one-sample exception

This is a bounded continuation of the dense width-rate investigation. The multi-sample root-width concentration theorem and the conditional population theorem currently retain small fixed labels. This note does not remove that assumption for general finite datasets. It proves that the assumption can be removed from fitting and scalar feedback stability with one training sample, and from whole-time finite-network concentration for one sample and two tanh layers. It does not prove the remaining population mean-bias rate.

Scientific inputs are the current dense equations in `paper/main.tex`, this study's complete FINITE_TAIL_ROUTE, PASSIVE_QUERY_FLUCTUATIONS, CONTROLLED_FEEDBACK_STABILITY, and AUTONOMOUS_SELF_AVERAGING derivations, and required skills/instructions. No other study or numerical experiment is used.

For a fixed probability law \(\mu\) supported on \(\|x\|/\sqrt d\le B\), the prediction norm used below is
\[
\mathcal E_\mu(f,g)=\left(\int\sup_{t\ge0}|f(t,x)-g(t,x)|^2d\mu(x)\right)^{1/2}.
\]
It includes the full physical-time supremum inside the input integral.

## 1. Label rescaling changes the feature-learning problem

Write the labels as \(y_a=c\widetilde y_a\), with \(c>0\), and write the readout as \(w=c\widetilde w\). Keep all hidden weights unchanged. Then \(f=c\widetilde f\), \(r=c\widetilde r\), and each residual-free backward field is \(\delta^{(\ell)}=c\widetilde\delta^{(\ell)}\). The canonical dense equations become
\[
\dot{\widetilde w}=-\frac2m\sum_a\widetilde r_a h_a^{(L)},
\]
\[
\dot W^{(1)}=-\frac{2c^2}{m}\sum_a\widetilde r_a\widetilde\delta_a^{(1)}x_a^\top/\sqrt d,
\quad
\dot W^{(\ell)}=-\frac{2c^2}{nm}\sum_a\widetilde r_a\widetilde\delta_a^{(\ell)}h_a^{(\ell-1)\top}.
\tag{1}
\]
Thus normalization of the target magnitude changes hidden-layer learning rates relative to the readout by \(c^2\). A common time rescaling cannot remove this relative factor. The small-label theorem is not an arbitrary-label theorem in different units.

For the multi-sample proof, small labels supplied both a finite residual-activity bound and a perturbative feedback estimate. Its last absorption has the form
\[
\|b_n-b_*\|_\infty
\le C S^2\|b_n-b_*\|_\infty+C\|\eta_n(X)\|_\infty,
\tag{2}
\]
where \(S\) bounds total integrated residual variation and \(\eta_n\) is the prescribed-control comparison error. Losing \(CS^2<1\) invalidates this absorption. It does not itself prove instability or a slower rate.

A constant growing rapidly with a fixed label magnitude does not change a width exponent: \(C(Y)/\sqrt n\) is still root width for each fixed \(Y\). A genuinely worse exponent needs an amplification or bias that worsens as width grows, or an endpoint response that fails to be Lipschitz. Near a loss of stability this is possible in smooth gradient systems; its occurrence in the canonical dense model remains unproved.

## 2. One training sample: global fitting for every fixed label

Consider any fixed depth \(L\), width \(n\), one nonzero normalized input \(x_0\), zero initial readout, and the manuscript's canonical dense flow. Use bounded smooth activations with locally Lipschitz vector field; tanh satisfies these assumptions. No Gaussian assumption is needed for this deterministic result. Let \(h^{(L)}(u)\in\mathbb R^n\) be its last hidden feature on the training input under the controlled equations
\[
\frac{dw}{du}=h^{(L)},\quad
\frac{dW^{(1)}}{du}=\delta^{(1)}x_0^\top/\sqrt d,\quad
\frac{dW^{(\ell)}}{du}=\delta^{(\ell)}h^{(\ell-1)\top}/n.
\tag{3}
\]
These are the actual dense equations with the scalar factor \(2(y-f)dt\) replaced by \(du\). Define
\[
P(u)=w(u)^\top h^{(L)}(u)/n,\quad
R(u)=\|w(u)\|_2/\sqrt n,\quad
Q_0=\|h^{(L)}(0)\|_2^2/n>0.
\tag{4}
\]
The derivative below is with respect to \(u\), not physical time.

**Exact theorem.** The controlled solution exists on every finite \(u\ge0\), and
\[
R''(u)\ge0\ (u>0),\qquad
P'(u)\ge Q_0,\qquad P(u)\ge Q_0u.
\tag{5}
\]
For every fixed real label \(y\), the actual gradient flow converges to a fitted parameter state and satisfies
\[
|f_n(t,x_0)-y|\le |y|e^{-2Q_0t},\qquad
\mathcal L_n(t)\le y^2e^{-4Q_0t},\qquad
2\int_0^\infty|f_n(t,x_0)-y|dt\le |y|/Q_0.
\tag{6}
\]

### Proof of existence and convexity

Let \(\theta\) collect all weights and \(M\) be the constant positive block mobility: \(n\) on read-in/readout and 1 on each hidden matrix. Equation (3) is exactly \(\theta'=M\nabla_\theta P\). Thus
\[
P'=\|\theta'\|_{M^{-1}}^2
\ge\|h^{(L)}\|_2^2/n,
\tag{7}
\]
where the squared norm sums read-in and readout Euclidean/Frobenius squares divided by \(n\), and unscaled hidden-matrix Frobenius squares. This includes all trained hidden layers.

If the top activation is bounded by \(B_\phi\), then \(\|w(u)\|_\infty\le B_\phi u\) and \(|P(u)|\le B_\phi^2u\) on any local solution. For \(U\) in its interval of existence,
\[
\int_0^U\|\theta'(u)\|_{M^{-1}}^2du=P(U)\le B_\phi^2U.
\]
Cauchy--Schwarz bounds its parameter path length by \(B_\phi U\). If a maximal interval ended at finite \(U_*\), the same estimate gives a finite limiting state: the remaining path length on \([s,t]\subset[0,U_*)\) is at most \(\sqrt{(t-s)B_\phi^2U_*}\). Local existence at that limit extends the solution, a contradiction. This proves global existence in the control coordinate without a small-label assumption.

Where \(R>0\), \(w'=h^{(L)}\) gives \(R'=P/R\). By Cauchy--Schwarz and (7),
\[
P'\ge\|h^{(L)}\|_2^2/n\ge P^2/R^2=(R')^2,
\quad
R''=\frac{P'-(R')^2}{R}\ge0.
\tag{8}
\]
At zero, \(w(u)=u h^{(L)}(0)+o(u)\), so \(R'(0+)=\sqrt{Q_0}\). On its initial positive interval, convexity gives \(R'\ge\sqrt{Q_0}\), hence \(R\ge u\sqrt{Q_0}\). Therefore \(R\) cannot return to zero; this argument extends to every \(u>0\). Equations (7)--(8) give \(P'\ge Q_0\), and integration gives (5). In fact the last-layer training feature energy itself stays at least \(Q_0\), though its monotonicity is not asserted.

For \(y>0\), strict increase and \(P(u)\ge Q_0u\) give a unique \(u_*\in(0,y/Q_0]\) with \(P(u_*)=y\). Solve
\[
\dot u=2[y-P(u)],\qquad u(0)=0.
\tag{9}
\]
It remains in \([0,u_*]\), and substituting (9) into (3) recovers the physical dense flow. Its nonnegative error \(e=y-P(u)\) obeys \(\dot e=-2P'(u)e\le-2Q_0e\), proving (6). The only possible limit is \(u_*\); the finite controlled state at \(u_*\) is the fitted parameter limit. The total residual integral equals \(u_*/2\).

For negative \(y\), replacing \(w\) by \(-w\) and the label by \(-y\) leaves the hidden physical dynamics unchanged and reverses the output. Apply the positive-label proof. For \(y=0\), the zero-readout initialization is stationary. This also shows that label magnitude chooses a stopping point on the same controlled feature-learning curve; its sign only reverses the readout. \(\square\)

## 3. Scalar feedback needs no small-activity absorption

Let \(P_n(u)\) be the training prediction of a fixed finite controlled initialization, with \(Q_0\ge q>0\). Let \(P_*(u)\) be a deterministic reference training function with \(P_*(0)=0\), \(P_*'\ge q\), and define physical clocks by
\[
\dot u_n=2[Y-P_n(u_n)],\qquad
\dot u_*=2[Y-P_*(u_*)],\qquad u_n(0)=u_*(0)=0,
\]
where \(Y=|y|\). Both clocks stay in \([0,S]\) for \(S=Y/q\). Set \(\eta(u)=P_n(u)-P_*(u)\). Their difference \(e=u_n-u_*\) satisfies
\[
\dot e=-2a(t)e-2\eta(u_*(t)),\qquad
a(t)=\int_0^1 P_n'(u_*(t)+s e(t))ds\ge q.
\]
Integrating the damped scalar equation yields
\[
\sup_{t\ge0}|u_n(t)-u_*(t)|\le q^{-1}\sup_{u\le S}|\eta(u)|.
\tag{10}
\]
This compares equal physical times. The interval may be large but fixed. It does not require a small coefficient \(CS^2\).

If the finite controlled query prediction is Lipschitz in \(u\) with constant \(C_{B,S}\) on a bounded query domain, its actual prediction error is consequently bounded by its prescribed-control query error plus \(C_{B,S}/q\) times the prescribed-control training error. The latter Lipschitz estimate follows from the deterministic controlled state bounds for two tanh layers with bounded initial hidden operator norm. Constants may grow with \(S\) but not with width or physical time.

## 4. Two tanh layers: the finite fluctuation proof extends to every fixed activity interval

Here retain one normalized input, two tanh layers, Gaussian initialization, and a bounded query domain. The prescribed-control result in PASSIVE_QUERY_FLUCTUATIONS.md extends from \(S\le1\) to any fixed \(S<\infty\), in the form
\[
\mathbb E\int\sup_{u\le S}|f_n^u(x)-\mathbb E f_n^u(x)|^2d\mu(x)\le C_{B,S}/n.
\tag{11}
\]
The control here is just \(b(u)=u\). The assertion includes each fixed training query. The following checks specify all uses of the old restriction \(S\le1\); no smallness absorption is used in that prescribed-control proof.

1. **Finite controlled bounds.** Keep \(\|w\|_\infty\le S\), \(\|W-W_0\|_F\le S^2\), and \(\|W\|_{\mathrm{op}}\le K+S^2\). In the transformed first coordinate, \(\psi=\tanh\circ F^{-1}\) remains globally 1-Lipschitz, with \(F(z)=z/2+\sinh(2z)/4\). Vector-field and difference constants are now finite functions of \(K,S\). The control-state Gronwall factor is \(e^{C_{K,S}S}\), which is width independent.
2. **Finite Gaussian cavity moments.** Deleting one first-layer column changes retained normalized states by at most \(C_{K,S}q_i/\sqrt n\), where \(q_i=\|W_{0,i}\|+S^2/\sqrt n\). On the operator event the backward carrier is its independent Gaussian-column cavity pairing plus a remainder bounded by \(C_{K,S}\). The cavity pairing has variance at most \(S^2\), and its time increment standard deviation is at most \(C_{K,S}|u-v|\). Covering \([0,S]\) by dyadic nets gives a summable Gaussian increment bound, and hence moments of every order and square-exponential tails with constants depending on \(K,S\). There is no need for the larger class of arbitrary drivers in this scalar application.
3. **Projection and coordinate weights.** Project \(W_0\) onto the fixed operator ball only inside the proof. Off its Gaussian good event, carrier coordinates are bounded by \(C_{K,S}\sqrt n\). Their fourth-moment contribution is at most \(C_{K,S}n^2e^{-cn}\). Transformed-coordinate increments are at most \(C_{K,S}\sqrt n\) there, so every fixed linear-exponential moment is bounded by a constant depending on \(S,p\), since \(e^{C_{K,S,p}\sqrt n-cn}\) is bounded uniformly in \(n\). On the good event those moments follow from the cavity tail. They are uniform in deterministic first roots.
4. **Response products and variance.** All matrix-response and root-response estimates in the passive-query proof now have constants \(C_{B,S}\). The root weights \(e^{2|U|}\) and \(e^{4|U|}\), for transformed increments \(U\), are integrable by step 3. The same fourth-carrier moments control the gate-response products. The two Gaussian variance inequalities therefore give \(\operatorname{Var}(\partial_u f_n^{\Pi,u}(x))\le C_{B,S}/n\).
5. **Full interval and projection removal.** Integrating the centered derivative over \([0,S]\) gives squared supremum error \(C_{B,S}/n\). Both projected and unprojected controlled predictions are bounded by \(S\); removing the projection costs at most \(C S^2e^{-cn}\). Tonelli supplies the input-integrated norm. This proves (11).

The constants are not uniform as \(Y\to\infty\). Arbitrary fixed labels do not require that stronger uniformity.

## 5. Consequence: all-time autonomous fluctuations for one sample and arbitrary fixed label

Let \(P_{n,\Pi}(u)\) be the projected-initialization training prediction, and set \(\bar P_n(u)=\mathbb E P_{n,\Pi}(u)\). By (5), \(\bar P_n'(u)\ge\mathbb E Q_{0,\Pi}\), with differentiation justified by finite-interval deterministic bounds. The expected initial energy has a fixed positive lower bound for sufficiently large \(n\), from Gaussian initial feature convergence and the exponentially rare operator projection. Choose a fixed \(q>0\) below that bound and below the limiting initial energy. The original initial event
\[
G_n=\{\|W_0\|_{\mathrm{op}}\le K,\ Q_0\ge q\}
\]
has probability tending to one, without using small-label fitting. Define \(\bar u_n\) by \(\dot{\bar u}_n=2[Y-\bar P_n(\bar u_n)]\), and define the deterministic query predictor
\[
\bar f_n(t,x)=\operatorname{sign}(y)\,\mathbb E f_{n,\Pi}^{\bar u_n(t)}(x).
\]
The zero-label case is stationary. For nonzero labels, both actual and reference clocks remain in \([0,Y/q]\) on \(G_n\). Projection changes the prescribed-control mean by at most \(2S\Pr(\|W_0\|_{\mathrm{op}}>K)\), uniformly over control and query. Apply (11), then the scalar feedback estimate (10) and its query consequence, to obtain
\[
\mathbb E[\mathbf1_{G_n}\mathcal E_\mu(f_n,\bar f_n)^2]\le C_{B,Y,q}/n.
\]
Markov's inequality and \(\Pr(G_n^c)\to0\) give, for each fixed confidence and sufficiently large width,
\[
\mathcal E_\mu(f_n,\bar f_n)\le C_{\delta,B,Y,q}/\sqrt n
\]
with probability at least \(1-\delta\). Two independent actual runs at the same width therefore differ at root width in the same all-time norm, by comparison with their common deterministic center. No small-label assumption or local response hypothesis H is used in this consequence.

This is still concentration about a finite-width deterministic center, not a full population-rate theorem. The quantitative bias remains unproved, and identifying an arbitrary-label global population flow is a separate extension beyond the manuscript's small-label theorem. This note does not silently invoke that theorem outside its hypotheses.

## 6. What a real slower-rate mechanism would require

The following diagnostic is a smooth least-squares gradient flow, **not a canonical dense-network counterexample**. It exhibits why stability at large labels is a mathematical issue and why poor constants alone are insufficient evidence.

For a scalar parameter \(a\), fixed target magnitude \(Y\), and a small perturbation \(\varepsilon\) of the prediction map, consider
\[
\mathcal L_\varepsilon(a)=\frac14(a^2-Y)^2+\frac12(a-\varepsilon)^2,
\quad \dot a=-\mathcal L_\varepsilon'(a)=(Y-1)a-a^3+\varepsilon,
\quad a(0)=0.
\tag{12}
\]
At \(Y<1\), the equilibrium response to \(\varepsilon\) near zero is Lipschitz, with derivative \((1-Y)^{-1}\). At the fixed critical label \(Y=1\), the perturbed trajectory increases to \(a_\infty=\varepsilon^{1/3}\) for \(\varepsilon>0\), while the unperturbed trajectory stays zero. Setting \(\varepsilon=n^{-1/2}\) gives endpoint displacement \(n^{-1/6}\). At fixed \(Y>1\), the positive perturbed equilibrium tends to \(\sqrt{Y-1}\) as \(\varepsilon\downarrow0\), while the unperturbed path remains at the unstable zero equilibrium. Thus an entire-time comparison can even fail to vanish, although every fixed-time perturbation vanishes.

These facts follow directly from the scalar vector-field signs and roots. They demonstrate critical slowing and symmetry breaking in a different smooth gradient system. The diagnostic does not meet the dense architecture, Gaussian width law, zero-readout, or positive initial feature-Gram hypotheses; it is not evidence that our canonical dense trajectories actually undergo this transition. A negative width theorem would have to construct such a reachable mechanism within those hypotheses and show its effect on predictions at fixed test inputs.

For multiple training samples, the scalar convexity proof does not extend by treating each residual separately: \(dw=\sum_a h_a\,db_a\) has competing directions, and there is no single monotone training prediction \(P(u)\). Whether the trained feature Gram and transverse prediction responses retain sufficient stability for arbitrary fixed labels is open here. No slower-than-root canonical dense construction has been proved.
