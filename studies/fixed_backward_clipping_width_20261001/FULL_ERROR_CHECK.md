# Internal check of the full-error bounds

2026-10-01. Isolated reconstruction of claims (2)–(4) in FULL_ERROR_CHECKPOINT.md.

**Verdict:** the three estimates follow with the stated powers of \(Y\) and \(n\), for all sufficiently large \(n\), from the exact clipped dynamics and the own population flow supplied in CLIPPED_POPULATION_ROUTE.md. No quantitative theorem for trained Gaussian programs, centered-concentration theorem, or independent-neuron approximation is needed. The \(Y^3\) remainder remains a label-size bound and does not establish a width rate at fixed positive \(Y\).

**Resolved correction:** a larger constant cannot repair a conditional expectation on a null event. In particular, \(n<m\) forces \(\operatorname{rank}\Gamma_n<m\), so \(\Pr(\mathcal G_n)=0\). During this check, the coordinator amended the checkpoint to restrict the statements to sufficiently large \(n\), with \(\Pr(\mathcal G_n)\ge1/2\), and explicitly exclude conditioning on a null event. I verified that amendment. There is no remaining blocker to (2)–(4) within the stated population dependency.

## Scope and dependencies

Read completely: FULL_ERROR_CHECKPOINT.md, FITTING_AND_THRESHOLD.md, CLIPPED_POPULATION_ROUTE.md, and UNCONDITIONAL_TAIL_ROUTE.md. Also read the required solve-math-rigorously and investigate-conjectures skills, its adversarial-audit reference, and root AGENTS.md. No other study, review, route report, manuscript, or Git history was read. No numerical computation, code change, or Git operation was performed.

The population dependency is precisely the object described in Section 4 of CLIPPED_POPULATION_ROUTE.md: two \(L^2\) spaces, the bounded initialized common action and its actual adjoint, the same clipped equations and initialization, and the initial feature covariances obtained from the two Gaussian initialization layers. This check verifies that the new estimates use only those properties. It does not independently re-review the cited common-action/Gaussian-program construction, whose underlying sources are outside the frozen input scope. In particular, no mesh-uniform quantitative Gaussian-program theorem is assumed.

Fix the sample list and dimension, \(K_0=8\), \(\lambda>0\), and \(M>0\). Assume \(\Gamma_*\succeq2\lambda I_m\) and the fitting note's condition \(0\le Y\le\lambda s_*/2\), with \(s_*\) computed using \(K_0\). All constants below depend only on the fixed data and Gram margin; the estimate constants and this label threshold can be chosen independently of \(M\). The proof does not invoke centered concentration, so its separate smaller stability threshold is unnecessary here.

## 1. Normalization and the cubic comparison

Use normalized Euclidean norms \(\|z\|_n=\|z\|_2/\sqrt n\) and \(\|r\|_m=\|r\|_2/\sqrt m\). The exact equations are

\[
B=W_0+\frac1{mn}\sum_a v_ak_a^T,\quad
\dot v_a=-2r_ad_a,\quad
\dot k_a=\frac\rho\tau(h_a-k_a),\quad
\dot\tau=\rho,
\]
\[
\dot w=-\frac2mGr,\qquad
\dot A=-\frac2m\sum_a r_a\ell_au_a^T,\quad
d_a=C_M(w\odot\operatorname{sech}^2 z_a),\quad
\ell_a=C_M(\operatorname{sech}^2(Au_a)\odot B^Td_a).
\]

Here \(k_a=\bar h_a/\tau\), \(v_a=-2\bar\delta_a\), \(\tau(0)=1\), and \(w(0)=v_a(0)=0\). There is no missing factor of \(\tau\) or \(n\), and the clipped \(d_a\) is used by the actual transpose. The readout Gram is \(\Gamma=G^TG/(mn)\), which gives exactly

\[
\dot r=-2\Gamma r+e,\qquad e_a=\langle w,\dot g_a\rangle_n.
\]

The fitting estimates can be reconstructed using only contraction of clipping. The exact key formula gives \(\|k_a\|_\infty\le1\). If \(S=\int_0^t\rho\), then

\[
\|w\|_\infty,\|d_a\|_\infty\le2S,\quad
\frac1m\sum_a\|v_a\|_\infty\le2S^2,\quad
\|B-W_0\|_{\rm op}\le2S^2.
\]

On \(S\le1\), set \(D=K_0+2\). Contraction by both gates and clips gives \(\|\ell_a\|_n\le2DS\), hence \(\|\dot A\|_F/\sqrt n\le4XD S\rho\). Direct differentiation of the derived action gives \(\|\dot B\|_{\rm op}\le8S\rho\). Therefore \(\|\dot g_a\|_n\le C_hS\rho\), with \(C_h=8+4X^2D^2\). These imply

\[
\|\Gamma(t)-\Gamma_n\|_{\rm op}\le C_hS^2,\qquad
\|e\|_m\le2C_hS^2\rho.
\]

The fitting note's stopping argument gives \(\rho(t)\le Ye^{-\lambda t}\), \(S_\infty\le Y/\lambda\). Thus checkpoint (5), including the \(O(Y^2)\) feature motion and \(O(Y^2\rho)\) hidden-motion forcing, has the claimed normalization and constants.

Let \(q=r-r^{\rm fr}\). Since the frozen residual obeys \(\dot r^{\rm fr}=-2\Gamma_nr^{\rm fr}\) with the same initial residual \(-y\),

\[
q(t)=\int_0^t e^{-2\Gamma_n(t-s)}F(s)\,ds,\qquad
\|F(s)\|_m\le CY^2\rho(s).
\]

The positive Gram margin gives \(\|e^{-2\Gamma_nt}\|_{\rm op}\le e^{-2\lambda t}\). Integrating the nonnegative norm bound in both time variables yields

\[
\int_0^\infty\|q(t)\|_m\,dt
\le\frac1{2\lambda}\int_0^\infty\|F(s)\|_m\,ds
\le CY^3.
\]

The readout difference has derivative \(-2[G_0q+(G-G_0)r]/m\). Since \(\|g_{0,a}\|_n\le1\) and \(\max_a\|g_a-g_{0,a}\|_n\le CY^2\),

\[
\|\dot w-\dot w^{\rm fr}\|_n\le2\|q\|_m+CY^2\rho.
\]

Integration gives \(\sup_t\|w-w^{\rm fr}\|_n\le CY^3\). For each query, with \(u_x=x/\sqrt d\),

\[
\sup_t\|g(t,x)-g_0(x)\|_n
\le\sup_t\left(\|B\|_{\rm op}\frac{\|A-A_0\|_F}{\sqrt n}\|u_x\|
+\|B-W_0\|_{\rm op}\right)
\le C(1+\|u_x\|)Y^2.
\]

Using the exact decomposition

\[
f_{n,M}-f_n^{\rm fr}
=\langle w-w^{\rm fr},g_0(x)\rangle_n
+\langle w,g(t,x)-g_0(x)\rangle_n
\]

and \(\|w\|_n\le2Y/\lambda\) proves checkpoint (8). Every displayed inequality also holds in the supplied population \(L^2\) spaces, with \(m^{-1}\sum_a v_a\otimes k_a\) replacing the finite-rank action. The common operator norm bound, contraction of activation and clipping, and initial population Gram margin verify the required hypotheses. This proves checkpoint (9) for the own population flow. No feature learning has been removed from either actual trajectory.

## 2. Initial covariance bias, including singular covariances

Append any fixed query to the sample list and let \(p=m+1\). Both empirical covariance matrices have \(p^2\) entries bounded by one. Independence of the first-layer Gaussian rows gives

\[
\mathbb E(Q_{1,n}-Q_1)=0,\qquad
\mathbb E\|Q_{1,n}-Q_1\|_F^2\le p^2/n.
\]

Conditional on \(A_0\), distinct rows of \(W_0H_0\) are independent Gaussian vectors with covariance \(Q_{1,n}\). This uses the specified variance \(1/n\) and independence of \(W_0\) from \(A_0\). Consequently

\[
\mathbb E[Q_{2,n}\mid A_0]=\mathcal T(Q_{1,n}),\qquad
\mathbb E[\|Q_{2,n}-\mathcal T(Q_{1,n})\|_F^2\mid A_0]\le p^2/n.
\]

The covariance differentiation formula does not require a lower eigenvalue bound. For positive definite \(Q\), its Gaussian density satisfies

\[
D p_Q[H]
=\tfrac12[z^TQ^{-1}HQ^{-1}z-\operatorname{tr}(Q^{-1}H)]p_Q
=\tfrac12\sum_{ij}H_{ij}\partial_{ij}p_Q.
\]

Integrating by parts twice is valid for \(\Phi(z)=\tanh z_a\tanh z_b\): its derivatives are bounded and the density has Gaussian decay. This gives the first formula in checkpoint (12). Applying the same identity to \(\partial_{ij}\Phi\) gives the second formula. All derivatives through order four are bounded, so

\[
|D\mathcal T_{ab}(Q)[H]|\le C_p\|H\|_F,\qquad
|D^2\mathcal T_{ab}(Q)[H,J]|\le C_p\|H\|_F\|J\|_F
\]

uniformly over positive definite \(Q\). For a possibly singular segment from \(Q\) to \(Q+H\), apply Taylor's integral remainder to \(Q+\varepsilon I+\theta H\). A Gaussian vector with covariance \(R+\varepsilon I\) can be represented as \(Z_R+\sqrt\varepsilon Z_I\); bounded continuous derivative expectations thus converge as \(\varepsilon\downarrow0\). Bounded convergence, also in \(\theta\), yields

\[
\mathcal T(Q+H)-\mathcal T(Q)=L_Q(H)+\mathcal R_Q(H),\qquad
\|\mathcal R_Q(H)\|_F\le C_p\|H\|_F^2,
\]

where \(L_Q\) is the linear Hessian-expectation formula. This is a Taylor statement along admissible positive-semidefinite segments; it does not posit a Gaussian distribution for indefinite covariances. It covers zero, repeated, and otherwise degenerate query inputs.

Apply it at deterministic \(Q_1\) with \(H=Q_{1,n}-Q_1\). The mean of \(L_{Q_1}(H)\) vanishes. The first derivative bound also gives the Lipschitz variance estimate. Therefore

\[
\|\mathbb E Q_{2,n}-\mathcal T(Q_1)\|_F\le C_p/n,\qquad
\mathbb E\|Q_{2,n}-\mathcal T(Q_1)\|_F^2\le C_p/n.
\]

All constants are uniform in the query because only bounded features and bounded activation derivatives enter.

For any bounded vector statistic \(Z\), writing \(p_n=\Pr(\mathcal G_n^c)\) gives

\[
\|\mathbb E[Z\mid\mathcal G_n]-\mathbb E Z\|
\le\frac{2\sup\|Z\|\,p_n}{1-p_n}.
\]

For the nonnegative squared covariance error, its conditional mean is at most the unconditional mean divided by \(1-p_n\). The tail proof gives \(p_n\le Ce^{-cn}\); choose \(n_0\) so \(p_n\le1/2\) for \(n\ge n_0\). Thus the conditional covariance bias and second moment are both \(O(1/n)\), relative to the same unconditional population covariance. No conditional independence of matrix rows is asserted or required.

## 3. Uniformity over all time

The frozen-predictor normalization is correct:

\[
r^{\rm fr}(t)=-e^{-2\Gamma_nt}y,\quad
w^{\rm fr}(t)=\frac2mG_0J_t(\Gamma_n)y,\quad
f_n^{\rm fr}(t,x)=\frac2m\kappa_n(x)^TJ_t(\Gamma_n)y.
\]

The training block of \(Q_{2,n}\) is \(m\Gamma_n\), while its query cross block is \(\kappa_n\), without a further factor of \(m\).

For symmetric \(H\succeq\lambda I\), Duhamel differentiation bounds the first derivative of \(e^{-2Hs}\) by \(2s e^{-2\lambda s}\|\Delta\|_{\rm op}\). The second derivative is the sum of two time-ordered integrals, each with factor four and simplex volume \(s^2/2\); its bound is thus \(4s^2e^{-2\lambda s}\|\Delta_1\|_{\rm op}\|\Delta_2\|_{\rm op}\). Integrating gives, for every \(t\ge0\),

\[
\|J_t(H)\|_{\rm op}\le\frac1{2\lambda},\quad
\|DJ_t(H)[\Delta]\|_{\rm op}\le\frac{\|\Delta\|_{\rm op}}{2\lambda^2},\quad
\|D^2J_t(H)[\Delta_1,\Delta_2]\|_{\rm op}
\le\frac{\|\Delta_1\|_{\rm op}\|\Delta_2\|_{\rm op}}{\lambda^3}.
\]

The segment between \(\Gamma_n\) on \(\mathcal G_n\) and \(\Gamma_*\) remains above \(\lambda I\). Cross-covariance vectors on their joining segment have norm at most \(\sqrt m\), and \(\|y\|_2=\sqrt mY\). Hence the first two derivatives of \((H,\kappa)\mapsto(2/m)\kappa^TJ_t(H)y\) are bounded by \(CY\), uniformly in time and query. The mixed derivatives in \(H,\kappa\) are covered by \(DJ_t\); the second derivative in \(\kappa\) is zero.

Set \(\delta=(\Gamma_n-\Gamma_*,\kappa_n-\kappa_*)\). The covariance estimates give

\[
\|\mathbb E[\delta\mid\mathcal G_n]\|\le C/n,\qquad
\mathbb E[\|\delta\|^2\mid\mathcal G_n]\le C/n.
\]

Taylor expansion at the deterministic population pair, followed by conditional expectation, yields

\[
\sup_{t\ge0}|\mathbb E[f_n^{\rm fr}(t,x)\mid\mathcal G_n]-f_*^{\rm fr}(t,x)|
\le CY/n.
\]

The pathwise uniform Lipschitz estimate instead yields

\[
\mathbb E[\sup_{t\ge0}|f_n^{\rm fr}(t,x)-f_*^{\rm fr}(t,x)|^2\mid\mathcal G_n]
\le CY^2/n.
\]

These steps do not exchange supremum and expectation as an equality. The bounds hold simultaneously for every time before taking either operation. Continuity in time permits each supremum to be taken over nonnegative rational times, ensuring measurability.

The two deterministic feature-learning remainders are bounded pointwise by \(C(1+\|x\|/\sqrt d)Y^3\). Thus only

\[
L_\mu=\left(\int(1+\|x\|/\sqrt d)^2\,d\mu(x)\right)^{1/2}<\infty
\]

is needed. Tonelli for nonnegative squared errors and the triangle inequality in the time-supremum/\(L^2\) norms give exactly (2) and (3), with \(C_\mu\le C(1+L_\mu)\). For the mean remainder use \(\sup_t|\mathbb E[R_n(t,x)\mid\mathcal G_n]|\le\mathbb E[\sup_t|R_n(t,x)|\mid\mathcal G_n]\). No fourth input moment or width-dependent label restriction appears.

## 4. Exceptional initializations and the finite-horizon conclusion

The exponential tail estimate in the assigned tail note is valid. Bounded-entry concentration at the first layer, the covariance map's entrywise Lipschitz constant three, and conditional bounded-entry concentration at the second layer give the training Gram failure bound \(4m^2e^{-n\lambda^2/72}\). A \(1/4\)-net with at most \(9^n\) points gives

\[
\Pr\{\|W_0\|_{\rm op}>K_0\}
\le2e^{-n(K_0^2/8-2\log9)}.
\]

For \(K_0=8\) the exponent is positive. The union bound requires no independence between operator and Gram events and has constants independent of \(Y,M,T\).

For every initialization, the unchanged readout equation gives

\[
\frac d{dt}\frac{\|w\|_2^2}{n}
=-4\langle f-y,f\rangle_m
=Y^2-4\|f-y/2\|_m^2\le Y^2.
\]

Since \(w(0)=0\) and every query feature has normalized norm at most one, \(|f_{n,M}(t,x)|^2\le Y^2t\). The bounded clips, exact bounded-key formula, \(\rho\le Y+\|w\|_n\), and \(\tau\ge1\) bound every finite-width state on each finite interval, so this identity applies to a global finite-time solution even off the good event. Population fitting gives \(|f_M(t,x)|\le2Y/\lambda\). Therefore

\[
\mathbb E[\mathbf1_{\mathcal G_n^c}\|f_{n,M}-f_M\|_{\mu,T}^2]
\le CY^2(T+1)e^{-cn}.
\]

On the good event use (3) and \(\|\cdot\|_{\mu,T}\le\|\cdot\|_{\mu,\infty}\). Splitting the second moment over the events and using \(\sqrt{a+b}\le\sqrt a+\sqrt b\) proves (4). Its constants are independent of finite \(T\), although the displayed right-hand side depends on \(T\). This also permits any specified finite \(T_n\). Sending \(T\) to infinity is unjustified by this bound.

## Final claim status

- Conditional mean bias (2): internally checked for sufficiently large width.
- Conditional all-time RMS population error (3): internally checked for sufficiently large width.
- Unconditional finite-horizon RMS population error (4): internally checked, with the stated exponential exceptional-event term.
- Fixed-label root-width full population error: remains unproved. The missing estimate is a width rate for \(\mathbb E[R_n\mid\mathcal G_n]-R_*\), not another bound on the initial covariances.
- Unconditional all-time RMS control: remains unproved because the exceptional-event contribution has only a finite-horizon envelope.

These are internal checks of partial bounds, not promotion approval or a claim that the broader root-width theorem is false.

## Frozen source hashes at completion

The checkpoint hash includes the resolved width-domain correction and its final check-status paragraph. Those were the only reported changes during this check.

| Source | SHA-256 |
| --- | --- |
| FULL_ERROR_CHECKPOINT.md | af838cc3ab2729de4c5785421eabe696d5775a728289eb79db63cd44b064eee3 |
| FITTING_AND_THRESHOLD.md | edb64134a5a4b5ce620586d0da0d3276ca542b1069b0a48801fa3f5d4cd4d1c2 |
| CLIPPED_POPULATION_ROUTE.md | 63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082 |
| UNCONDITIONAL_TAIL_ROUTE.md | 76400cfe15351b7c35305808958fd9df3cae4c918bbeab2f3172325d187bd6ed |
