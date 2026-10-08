# Kinetic observable route

Status: frozen independent candidate, 2026-10-07. This route proves exact shallow identities and a shallow all-time comparison theorem; it does not prove a finite autonomous spectral closure or the arbitrary-depth target. The arguments below have been checked by their author, but have not received independent review or promotion.

Input scope: the supervisor's self-contained model assignment only. No book, code, other study, other route, scientific literature, experiment, or Git history was consulted. Required process and proof/presentation skills were read. This file is the sole assigned output. Constants below are independent of width, and no coefficient is obtained from a trained target trajectory.

## 1. Model and precise scope

There are \(p\) fixed unit input vectors \(v_a\in\mathbb R^d\), with the first \(m\le p\) used for training. Set \(Q_{ab}=v_a^\top v_b\). For neuron \(i\le n\), its state on the panel is \(z_i=(z_{1i},\ldots,z_{pi})\in\mathbb R^p\), together with its scalar readout \(w_i\). The forward pass, residual, and loss are

\[
h_{ai}=\phi(z_{ai}),\qquad
f_{n,a}=\frac1n\sum_i w_i\phi(z_{ai}),\qquad
c_{n,b}=y_b-f_{n,b},\qquad
\mathcal L_n=\frac1m\sum_{b=1}^m c_{n,b}^2.
\]

The physical clock is exactly the one in the assignment:

\[
\begin{aligned}
\dot w_i&=\frac2m\sum_{b=1}^m c_{n,b}\phi(z_{bi}),\\
\dot z_{ai}&=\frac2m\sum_{b=1}^m c_{n,b}Q_{ab}w_i\phi'(z_{bi}).
\end{aligned} \tag{1}
\]

Initially \(w_i=0\), and \(z_i\) are independent centered Gaussian vectors with covariance \(Q\). Factor \(Q=CC^\top\), where \(C\in\mathbb R^{p\times r}\) and \(r=\operatorname{rank}Q\); write \(z_i(0)=C\xi_i\), with independent \(\xi_i\sim\gamma_r=N(0,I_r)\). Singular \(Q\) is allowed.

For clarity, “analytic strip with bounded derivative” is taken to mean that \(\phi\) is real on the real axis, extends holomorphically to \(\{\zeta:|\operatorname{Im}\zeta|<\rho\}\), and satisfies \(\sup|\phi'(\zeta)|\le L\) there, for fixed \(\rho,L>0\). Its values may be unbounded. This implies

\[
|\phi(x)|\le |\phi(0)|+L|x|,\qquad
\sup_{x\in\mathbb R}|\phi''(x)|\le 2L/\rho. \tag{2}
\]

The second bound follows by applying the Cauchy derivative formula to \(\phi'\) on a circle of radius \(\rho/2\). The kinetic and stability results below actually need only the two real derivative bounds in (2). If the assignment meant a bounded derivative only on the real axis, the bound on \(\phi''\) must be added or separately proved; analyticity without a complex growth bound does not imply it.

Assume that the initial training feature Gram matrix

\[
G_{0,ab}=\mathbb E_{\xi\sim\gamma_r}
 [\phi((C\xi)_a)\phi((C\xi)_b)],\qquad a,b\le m,
\]

has \(\lambda_0=\lambda_{\min}(G_0)>0\). All constants may depend on \(p,m,Q,\phi(0),L,\rho,\lambda_0\), but not on \(n\).

The proved observable comparison is to the deterministic Gaussian kinetic evolution on the complete panel, uniformly over physical time. It gives error of order \(n^{-1/2}\) in probability. It does not reconstruct the realized leading fluctuation at order \(n^{-1/2}\), nor does it compress the kinetic state to polylogarithmically many real coordinates.

## 2. Exact autonomous kinetic equation

For a probability measure \(\mu\) on \(\mathbb R\times\mathbb R^p\), define

\[
f_a[\mu]=\int w\phi(z_a)\,d\mu(w,z),\qquad
c_b[\mu]=y_b-f_b[\mu].
\]

Define the vector field, with its first coordinate acting on \(w\), by

\[
V_b(w,z)=
\left(\phi(z_b),\;w\phi'(z_b)Q_{:b}\right),
\qquad
b[\mu]=\frac2m\sum_{b=1}^m c_b[\mu]V_b. \tag{3}
\]

The empirical measure \(\mu_{n,t}=n^{-1}\sum_i\delta_{(w_i(t),z_i(t))}\) satisfies, exactly, for every compactly supported continuously differentiable test function \(\psi\),

\[
\frac d{dt}\int\psi\,d\mu_{n,t}
=\int \nabla\psi\cdot b[\mu_{n,t}]\,d\mu_{n,t}. \tag{4}
\]

Indeed, differentiating each summand and substituting (1) gives (4). Thus its transport equation is

\[
\partial_t\mu+\operatorname{div}_{(w,z)}(b[\mu]\mu)=0. \tag{5}
\]

The deterministic model uses the same equation with
\(\mu_0=\delta_0(dw)\otimes N(0,Q)(dz)\). Equivalently, evolve the characteristic functions
\(w(t,\xi),z(t,\xi)\) from \((0,C\xi)\), evaluate \(f_a(t)=\mathbb E[w(t,\xi)\phi(z_a(t,\xi))]\), and use \(c=y-f_{1:m}\) in (3). This is an autonomous distributional model with prescribed Gaussian initialization.

An ordinary density in \(p+1\) variables is usually the wrong object: the initial law is supported on an \(r\)-dimensional set, and deterministic transport retains that intrinsic dimension. The weak measure equation or the Gaussian-coordinate characteristic functions avoid assuming a nonexistent full-dimensional density.

The current response matrix on the panel has the explicit representation

\[
\begin{aligned}
K_{ab}[\mu]&=G_{ab}[\mu]+H_{ab}[\mu],\\
G_{ab}[\mu]&=\int\phi(z_a)\phi(z_b)\,d\mu,\\
H_{ab}[\mu]&=Q_{ab}\int w^2\phi'(z_a)\phi'(z_b)\,d\mu.
\end{aligned} \tag{6}
\]

Differentiating \(w\phi(z_a)\) along (3) gives

\[
\dot f_a=\frac2m\sum_{b=1}^m K_{ab}c_b,
\qquad
\dot c=-\frac2m K_{1:m,1:m}c. \tag{7}
\]

Both terms of the training block in (6) are positive semidefinite. For the second term, for any \(q\in\mathbb R^m\),

\[
q^\top Hq=\int w^2
\left|\sum_{a=1}^m q_a\phi'(z_a)v_a\right|^2d\mu\ge0.
\]

Consequently \(d|c|^2/dt=-(4/m)c^\top Kc\le0\). In particular, residuals stay bounded by \(|y|\). These identities hold for empirical and deterministic measures. Polynomially growing observables in (6)–(7) are justified by the moment bounds proved next, using cutoff test functions and dominated convergence.

The model is not a frozen-feature limit. At initialization, \(\dot z_{ai}(0)=0\), but

\[
\ddot z_{ai}(0)=\frac4{m^2}
\left(\sum_{c=1}^m y_c\phi(z_{ci}(0))\right)
\left(\sum_{b=1}^m y_bQ_{ab}\phi'(z_{bi}(0))\right). \tag{8}
\]

Unless this expression vanishes for the particular data and labels, feature motion occurs at order \(|y|^2\) independently of width. Small labels restrict its amplitude; they do not make it vanish as \(n\to\infty\).

## 3. Controlled characteristics and stability envelopes

It is useful to absorb the loss normalization into the control \(u(t)=(2/m)c(t)\). For arbitrary integrable \(u:[0,T]\to\mathbb R^m\), define \(X^u=(w^u,z^u)\) by

\[
\dot w^u=u\cdot\phi(z^u_{1:m}),\qquad
\dot z^u=w^uQ_{:1:m}\operatorname{diag}(\phi'(z^u_{1:m}))u,
\qquad X^u(0,\xi)=(0,C\xi). \tag{9}
\]

Write \(S_u(t)=\int_0^t|u(s)|ds\) and \(R(\xi)=1+|C\xi|\). Directly from (2),

\[
\begin{aligned}
1+|w^u(t)|+|z^u(t)|&\le R(\xi)e^{A S_u(t)},\\
|w^u(t)|&\le A S_u(t)e^{A S_u(t)}R(\xi),\\
|z^u(t)-C\xi|&\le A S_u(t)^2e^{A S_u(t)}R(\xi),
\end{aligned} \tag{10}
\]

after increasing a fixed constant \(A\). To verify these bounds, bound \(|\dot w|\) by \(|u|(|\phi(0)|\sqrt m+L|z|)\) and \(|\dot z|\) by \(|u|\|Q_{:1:m}\|L|w|\). The first estimate is the integral form of this scalar differential inequality; integrate it once for \(w\), and then once more for \(z-C\xi\). The latter integral uses \(\int_0^t |u|S_u= S_u(t)^2/2\).

There exists an explicitly bounded envelope

\[
P(\xi)=A R(\xi)^4e^{A R(\xi)},\qquad P\ge1, \tag{11}
\]

with \(A\) depending only on the fixed model quantities, such that the following estimates all hold whenever \(S_u(T),S_v(T)\le1\). Set
\(D(t)=\int_0^t|u(s)-v(s)|ds\), and define the scalar observables

\[
o_a(w,z)=w\phi(z_a),\qquad
k_{ab}(w,z)=\phi(z_a)\phi(z_b)+Q_{ab}w^2\phi'(z_a)\phi'(z_b).
\]

After enlarging \(A\) to absorb finite matrix dimensions,

\[
\begin{aligned}
\|k(X^u(t,\xi))-k(X^v(t,\xi))\|_F&\le P(\xi)D(t),\\
|o(X^u(t,\xi))-o(X^v(t,\xi))|&\le P(\xi)D(t),\\
\left\|\frac d{dt}k(X^u(t,\xi))\right\|_F
+\left|\frac d{dt}o(X^u(t,\xi))\right|&\le P(\xi)|u(t)|,\\
\|\phi(z^u_{1:m})\phi(z^u_{1:m})^\top
-\phi((C\xi)_{1:m})\phi((C\xi)_{1:m})^\top\|_F
&\le P(\xi)S_u(t)^2.
\end{aligned} \tag{12}
\]

Here the first two lines use the full panel; the last line uses the training block. The same envelope can bound \(\|k(X^u)\|_F+|o(X^u)|\).

For completeness, subtract (9) for the two controls. The state difference satisfies

\[
|X^u(t)-X^v(t)|
\le\int_0^t A|u(s)|(1+R(\xi))|X^u(s)-X^v(s)|ds
+A R(\xi)D(t).
\]

This uses the bounded real second derivative in (2) for the factor \(w\phi'(z)\). Iterating this integral inequality yields
\(|X^u-X^v|\le A R e^{A R}D\). On the real trajectories in (10), the gradients of \(o\) and \(k\) are bounded by a constant times \(R^2\). Multiplying these bounds proves the first two lines of (12). Their time derivatives use the same gradients and \(|\dot X^u|\le A R|u|\). Finally, apply \(|\phi(z)-\phi(C\xi)|\le L|z-C\xi|\) and (10) to the outer product to obtain the last line. Formula (11) dominates every resulting expression.

All moments of \(P\) are finite under \(\gamma_r\): for every fixed \(a,k\), \((1+|\xi|)^k e^{a|\xi|}\) is Gaussian integrable, as follows by completing the square in \(-|\xi|^2/2+a|\xi|\). In particular, let

\[
M=\mathbb E P(\xi),\qquad V=\mathbb E P(\xi)^2<\infty. \tag{13}
\]

This proves finite-time well-posedness as well. For an externally supplied bounded residual, (9) has a unique global real flow by local Lipschitz continuity and (10). On a short interval, mapping a candidate residual to \(y-\mathbb E o(X^u)\) is a contraction in the uniform norm: the first two lines of (12), with their analogous envelope for any fixed total-control bound, contribute a factor equal to the interval length. Iterate this construction. The energy identity (7) bounds the residual by \(|y|\), so (10) prevents finite-time escape and permits continuation to every finite time. The same reasoning with finite averages applies to the finite network. This constructs the unique characteristic solution in the Gaussian-pushforward class; no claim about all possible weak solutions without moment/characteristic assumptions is needed.

## 4. Small fixed labels give an all-time shallow theorem

**Theorem.** Under Section 1's assumptions, there is \(y_*>0\), independent of \(n\), such that for every fixed \(|y|\le y_*\), the deterministic Gaussian kinetic solution and the network (1) obey

\[
\sup_{t\ge0}|f_n(t)-f(t)|=O_{\mathbb P}(n^{-1/2}). \tag{14}
\]

More precisely, constants \(C_0,C_1\) independent of \(n,y\) can be chosen such that, for every \(0<\delta<1\),

\[
\mathbb P\left\{\sup_{t\ge0}|f_n(t)-f(t)|>
\frac{C_1}{\delta\sqrt n}\right\}\le\delta+\frac{C_0}{n}. \tag{15}
\]

On an event of probability at least \(1-C_0/n\), both training residuals decay at least as \(|y|e^{-2\lambda t/m}\), where \(\lambda=\lambda_0/2\). Thus fitting and the comparison include the entire infinite training interval. Equation (14) controls the panel outputs, not a full measure metric.

**Proof.** The proof has three distinct parts: retain the Gram gap using small total movement; establish sampling error uniformly in time along the deterministic flow; and propagate that error through the interacting empirical dynamics.

Choose

\[
\bar S=\min\left\{1,\sqrt{\frac{\lambda_0}{8M}},\frac{\lambda}{4M}\right\},
\qquad y_* =\frac{\lambda\bar S}{2}. \tag{16}
\]

Let \(\mathcal E_n\) be the event

\[
\left\|\frac1n\sum_i\phi((C\xi_i)_{1:m})
\phi((C\xi_i)_{1:m})^\top-G_0\right\|_{\rm op}\le\lambda_0/4,
\qquad \frac1n\sum_iP(\xi_i)\le2M. \tag{17}
\]

Independence gives a variance of order \(1/n\) for every Gram entry and for the average of \(P\). Bounding the operator norm by the Frobenius norm and applying the scalar second-moment inequality therefore gives \(\mathbb P(\mathcal E_n^c)\le C_0/n\). No dimension-dependent empirical Wasserstein rate is being used.

On any interval where \(S_u(t)\le\bar S\), the last line of (12) bounds the continuum Gram change by \(M\bar S^2\). On \(\mathcal E_n\), it bounds the empirical Gram change by \(2M\bar S^2\). The initial empirical Gram is at least \(3\lambda_0 I/4\), so (16) implies that the training response matrices of both systems are at least \(\lambda I\) throughout such intervals. Positivity of \(H\) is essential here.

Equation (7) then gives \(|c(t)|\le|y|e^{-2\lambda t/m}\), and hence

\[
S_u(t)=\frac2m\int_0^t|c(s)|ds\le\frac{|y|}{\lambda}
\le\bar S/2. \tag{18}
\]

Continuity rules out a first time at which \(S_u\) reaches \(\bar S\). Thus the Gram gap and (18) hold for all time, for the continuum and, on \(\mathcal E_n\), the empirical system.

Next use the deterministic continuum control \(u=(2/m)c\), and define its sampling discrepancies

\[
\begin{aligned}
\zeta_n(t)&=\frac1n\sum_i k(X^u(t,\xi_i))-
\mathbb E k(X^u(t,\xi)),\\
\eta_n(t)&=\frac1n\sum_i o(X^u(t,\xi_i))-
\mathbb E o(X^u(t,\xi)).
\end{aligned} \tag{19}
\]

These are empirical averages of independent functions of the Gaussian initial points. The continuum control is deterministic, so no independence is lost in (19). By absolute continuity,

\[
\sup_{t\ge0}\|\zeta_n(t)\|_F
\le\|\zeta_n(0)\|_F+\int_0^\infty\|\dot\zeta_n(t)\|_Fdt.
\]

The second moment of a centered average of independent vector-valued variables is its single-variable variance divided by \(n\). Apply this identity, the bound \(P|u(t)|\) in (12), and integration of expectations to obtain

\[
\mathbb E\sup_{t\ge0}\|\zeta_n(t)\|_F
\le\frac{\sqrt V(1+\bar S)}{\sqrt n},\qquad
\mathbb E\sup_{t\ge0}|\eta_n(t)|
\le\frac{\sqrt V\bar S}{\sqrt n}. \tag{20}
\]

The second bound uses \(o(X^u(0,\xi))=0\). This is the needed uniform-in-time concentration estimate. Compact-time pointwise concentration alone would not establish it. Here it is proved by finite total variation in the residual-controlled clock.

Finally let \(u_n=(2/m)c_n\), and set

\[
D_T=\int_0^T|u_n(t)-u(t)|dt,
\qquad Z_n=\sup_{t\ge0}\|\zeta_n(t)\|_F.
\]

On \(\mathcal E_n\), splitting a kernel difference into its characteristic perturbation and (19) gives

\[
\|K_n(t)-K(t)\|_{\rm op}\le2M D_t+Z_n. \tag{21}
\]

Put \(d=c_n-c\), with \(d(0)=0\), and \(\kappa=2/m\). Subtracting (7) yields

\[
\dot d=-\kappa K_n d-\kappa(K_n-K)c.
\]

The lower bound \(K_n\ge\lambda I\) implies

\[
|d(t)|\le\kappa\int_0^t e^{-\kappa\lambda(t-s)}
\|K_n(s)-K(s)\|_{\rm op}|c(s)|ds. \tag{22}
\]

This follows by differentiating \(|d|\) where it is nonzero and using the upper right derivative at zero; multiplication by \(e^{\kappa\lambda t}\) then integrates the scalar inequality. Integrate (22) up to \(T\), multiply by \(\kappa\), and change integration order. The integral of the exponential is at most \((\kappa\lambda)^{-1}\), so (18)–(21) imply

\[
D_T\le\frac{\bar S}{\lambda}(2M D_T+Z_n).
\]

By (16), \(2M\bar S/\lambda\le1/2\). Therefore

\[
D_\infty\le\frac{2\bar S}{\lambda}Z_n,
\qquad
\sup_{t\ge0}|f_n(t)-f(t)|
\le\frac{4M\bar S}{\lambda}Z_n+
\sup_{t\ge0}|\eta_n(t)| \quad\hbox{on }\mathcal E_n. \tag{23}
\]

The output bound uses the second line of (12). Taking expectations of the right side, using (20), and then the scalar first-moment inequality proves (15), with the additional failure probability from (17). This completes the proof.

The same proof gives uniform comparison for any fixed family of observables whose value differences and time derivatives admit an envelope of the form (11). The smallness restriction is quantitative and independent of width, although the constants above are intentionally conservative.

## 5. What is retained at the fluctuation scale

The deterministic Gaussian law provides an approximation at the size of ordinary empirical fluctuations. It cannot encode their realization. For example, the exact random initial slope is

\[
\dot f_{n,a}(0)=\frac2m\frac1n\sum_i
\phi((C\xi_i)_a)\sum_{b=1}^m y_b\phi((C\xi_i)_b).
\]

Its variance is

\[
\operatorname{Var}(\dot f_{n,a}(0))
=\frac4{m^2n}\operatorname{Var}\left[
\phi((C\xi)_a)\sum_b y_b\phi((C\xi)_b)\right]. \tag{24}
\]

When the variance on the right is positive, deterministic initialization discards a real leading-order random observable. Equation (24) is an exact mean-square statement about the slope, not a claimed output lower bound at an arbitrary later time.

A meaningful response state is the fluctuation measure

\[
\nu_{n,t}=\sqrt n(\mu_{n,t}-\mu_t),\qquad
F_{n,a}(t)=\int o_a\,d\nu_{n,t}=
\sqrt n(f_{n,a}-f_a).
\]

Subtracting the two weak equations, without approximation, gives

\[
\begin{aligned}
\frac d{dt}\int\psi\,d\nu_n
={}&\int \nabla\psi\cdot b[\mu]\,d\nu_n
-\frac2m\sum_{b=1}^m F_{n,b}
\int V_b\cdot\nabla\psi\,d\mu\\
&-\frac2{m\sqrt n}\sum_{b=1}^m F_{n,b}
\int V_b\cdot\nabla\psi\,d\nu_n. 
\end{aligned} \tag{25}
\]

The leading linearized kinetic equation results from dropping the final term, but convergence to that equation needs a remainder estimate in a specified test-function topology. It is not asserted here. Equation (25) identifies the response state needed to retain actual initialization fluctuations; it is more informative than merely declaring the Gaussian law sufficient at every meaning of the fluctuation scale.

## 6. Finite moments: a concrete candidate and the closure gap

The exact weak equation evolves moments \(\int\psi_j\,d\mu\). Its derivative involves \(\int V_b\cdot\nabla\psi_j\,d\mu\), which generally lies outside any chosen finite span. Even polynomial test functions do not close for a general analytic activation. Taylor expansion about zero is not justified on Gaussian tails when the activation is only holomorphic in a strip.

A genuine finite spectral candidate uses coefficients of the characteristic functions in a fixed basis \(\{H_\alpha\}\) orthonormal for \(\gamma_r\). For total degree at most \(q\), set

\[
w_q(\xi)=\sum_{|\alpha|\le q}W_\alpha H_\alpha(\xi),\qquad
z_{q,a}(\xi)=\sum_{|\alpha|\le q}Z_{a,\alpha}H_\alpha(\xi).
\]

With \(\Pi_q\) the orthogonal projection onto this polynomial span, define

\[
\begin{aligned}
f_{q,a}&=\mathbb E[w_q\phi(z_{q,a})],\qquad
c_{q,b}=y_b-f_{q,b},\\
\dot w_q&=\Pi_q\left[\frac2m\sum_b c_{q,b}\phi(z_{q,b})\right],\\
\dot z_{q,a}&=\Pi_q\left[\frac2m\sum_b c_{q,b}Q_{ab}
w_q\phi'(z_{q,b})\right].
\end{aligned} \tag{26}
\]

For \(q\ge1\), initialize \(w_q=0,z_q=C\xi\). All coefficients come from the Gaussian initial law, the fixed data, labels, activation, and current coefficient state. The moving state has
\((p+1)\binom{r+q}{q}\) real coordinates. It is autonomous and restartable. Its projected response matrix is explicitly

\[
\begin{aligned}
K_{q,ab}={}&\mathbb E[(\Pi_q\phi(z_{q,a}))(\Pi_q\phi(z_{q,b}))]\\
&+Q_{ab}\mathbb E[(\Pi_q[w_q\phi'(z_{q,a})])
(\Pi_q[w_q\phi'(z_{q,b})])].
\end{aligned} \tag{26a}
\]

To derive this formula, differentiate \(f_{q,a}\), substitute (26), and move each orthogonal projection to the other factor in the Gaussian inner product. Both training-block terms in (26a) are positive semidefinite by the same Gram argument as in Section 2. Therefore the projected residual satisfies \(\dot c_q=-(2/m)K_qc_q\), and its norm is nonincreasing. Orthogonal projection is an \(L^2(\gamma_r)\) contraction, so

\[
\|\dot w_q\|_2\le |u_q|(|\phi(0)|\sqrt m+L\|z_q\|_2),\qquad
\|\dot z_q\|_2\le A|u_q|\|w_q\|_2,
\quad u_q=(2/m)c_q.
\]

These inequalities prevent finite-time blowup of the coefficient norm. The finite vector field is locally Lipschitz: on bounded coefficient sets, bounded \(\phi'\) and \(\phi''\), polynomial Gaussian moments, and the finite basis control each derivative of its Gaussian integrals. Thus (26) is globally well posed for every fixed \(q\).

If the initial projected feature Gram, the first term of (26a) at \(z_q=C\xi\), has a specified positive lower bound, the small-label fitting bootstrap also survives. Indeed, the displayed \(L^2\) inequalities give \(\|w_q\|_2\le ASe^{AS}\) and \(\|z_q-C\xi\|_2\le AS^2e^{AS}\), with \(S=\int|u_q|\). The projected feature Gram changes by at most \(AS^2e^{AS}\), because projection contracts \(L^2\) and \(\phi\) is Lipschitz. The argument in (18) then closes for sufficiently small labels. The required smallness depends on that initial projected gap; no rate for achieving a gap with increasing \(q\) is asserted here.

Equation (26) is therefore a globally defined model with an exact dissipative structure. It is still not a proved all-time approximation to the kinetic law. Its unresolved obligations are:

1. Control the discarded spectral tail of the evolving characteristic fields and nonlinear products, uniformly over all time.
2. Prove stability of the comparison between the projected and exact flows. Their separate dissipation identities do not bound error production or amplification between them.
3. Replace every Gaussian integral by a computable quadrature rule with a proved error and cost bound; an exact integration oracle cannot be hidden in a coefficient update.
4. If realized \(n^{-1/2}\) variability must be matched, also truncate the fluctuation response in (25), initialize its retained statistics from the actual sample, and control omitted feedback.

Changing basis and using exactly as many collocation nodes as coefficients can be an invertible rewriting of weighted particles. That does not meet the intended conceptual compression by itself. Projection with controlled unresolved modes is the substantive requirement. A quadrature particle system may approximate the kinetic measure, but calling its nodes “moments” adds no theorem.

## 7. The analytic radius is a real obstacle

On a truncated initial Gaussian box \(|\xi_j|\le R\), the real characteristic size is \(O(1+R)\), but the derivative of its vector field contains \(w\phi''(z)\). For total control at most a fixed constant, the direct complex-trajectory comparison therefore certifies only a tube whose radius can be as small as

\[
\delta_R\ge c\rho\exp[-A(1+R)]. \tag{27}
\]

This is a conservative *lower bound on a guaranteed admissible radius*, not an upper bound on the true radius. To obtain it, start a complex trajectory a distance \(\delta_R\) from a real trajectory, apply the same differential inequality as in Section 3 while every preactivation remains in the half-strip, and choose \(\delta_R\) so that its amplified distance stays below \(\rho/2\). The relevant integrated Lipschitz bound is \(A(1+R)\); complex existence continues as long as this half-strip condition holds.

There is a concrete reason one cannot silently replace this estimate by a fixed strip with a polynomial growth envelope. Take \(m=p=1\), \(Q=1\), and

\[
\phi(x)=x+a\sin x,\qquad a>1.
\]

This activation has bounded derivative on every fixed complex strip and satisfies the admissible linear-growth condition. Use the cumulative scalar control \(s\) in place of physical time, so the characteristic equations are

\[
\frac{dw}{ds}=\phi(z),\qquad \frac{dz}{ds}=w\phi'(z),
\qquad (w,z)|_{s=0}=(0,x). \tag{28}
\]

Choose a real \(\theta\) with \(\cos\theta=-1/a\) and \(\sin\theta<0\), and let \(x_k=2\pi k+\theta\). Then \(\phi'(x_k)=0\), \(\phi''(x_k)>0\), and for large positive \(k\), \(\phi(x_k)>0\). The characteristic from \(x_k\) is exactly

\[
z(s,x_k)=x_k,\qquad w(s,x_k)=s\phi(x_k).
\]

Differentiate (28) with respect to its initial coordinate. At this special trajectory, the variation of \(w\) is zero, and

\[
\partial_x z(s,x_k)=
\exp\left[\frac{s^2}{2}\phi(x_k)\phi''(x_k)\right]. \tag{29}
\]

For every fixed \(s>0\), this grows exponentially in \(x_k\). If \(z(s,\zeta)\) extended to a fixed-width strip with a bound \(|z(s,\zeta)|\le B(1+|\operatorname{Re}\zeta|)^j\), the Cauchy formula on a fixed-radius circle centered at \(x_k\) would bound \(|\partial_xz(s,x_k)|\) by a polynomial in \(x_k\), contradicting (29). Therefore a fixed analytic strip *and* a polynomial complex growth envelope do not follow from the activation assumption, even in the shallow scalar system. This does not prove that every spectral representation needs super-polylogarithmic size.

The consequence for a common proposed complexity proof is explicit. Gaussian tails with polynomially growing observables can be reduced below \(\varepsilon\) by taking \(R=O(\sqrt{\log(1/\varepsilon)})\). On a box of radius \(R\), a holomorphic continuation of width \(\delta\) and controlled supremum gives a Chebyshev truncation error bounded by a geometric tail of the form

\[
\text{prefactor}\times\exp[-c q\delta/R]. \tag{30}
\]

To see the exponent, map the interval to \([-1,1]\), choose a Bernstein ellipse with parameter \(1+c\delta/R\), and apply the contour coefficient formula; its degree-\(k\) coefficient is bounded by the contour supremum times this parameter to the power \(-k\). Summing the geometric tail gives (30), with explicit polynomial factors in \(R/\delta\) for a fixed number of coordinates.

If \(\delta\) were independent of \(R\) and time, with polynomial prefactors, \(q=O((\log(1/\varepsilon))^{3/2})\) would suffice for approximating the characteristic *functions*. With only (27), this reasoning instead permits a factor \(\exp[O(\sqrt{\log(1/\varepsilon)})]\) in the degree. At \(\varepsilon\asymp n^{-1/2}\), that factor is subpolynomial in \(n\) but larger than every fixed power of \(\log n\).

Even the favorable function-approximation bound would not by itself establish convergence of the autonomous projected dynamics (26). Stability of truncation and quadrature remains a separate obligation. The scalar construction (29) exposes a failure of the simplest analytic-radius proof, not an impossibility theorem for all finite descriptions.

## 8. Why two layers require another correlation state

Here is a precise obstruction to extending a single-neuron forward law independently through depth. Consider two hidden layers with equal width:

\[
z^1_a=Av_a,\quad h^1_a=\phi(z^1_a),\quad
z^2_a=Wh^1_a,\quad h^2_a=\phi(z^2_a),\quad
f_a=\frac1n w^\top h^2_a,
\]

and \(W_{ji}(0)\sim N(0,1/n)\). To make the displayed calculation unambiguous, use the illustrative feature-clock mobilities

\[
\begin{aligned}
\delta^2_a&=w\odot\phi'(z^2_a),\\
\dot w&=\frac2m\sum_b c_bh^2_b,\\
\dot W&=\frac2{mn}\sum_b c_b\delta^2_b h^{1\top}_b,\\
\dot z^1_a&=\frac2m\sum_b c_bQ_{ab}
\bigl(\phi'(z^1_b)\odot W^\top\delta^2_b\bigr).
\end{aligned} \tag{31}
\]

Other mobilities change factors, not the correlation issue. The prompt does not specify a complete deep training metric, so (31) is an explicit example rather than an identification of an unspecified deep system.

Differentiate the second forward map in (31). With
\(G^1_{ba}=n^{-1}h_b^{1\top}h^1_a\),

\[
\dot z^2_a=\frac2m\sum_b c_b\left[
G^1_{ba}\delta^2_b+
Q_{ab}W\operatorname{diag}(\phi'(z^1_a)\odot\phi'(z^1_b))
W^\top\delta^2_b\right]. \tag{32}
\]

The distribution of the forward representations in layer 1, and the joint distribution of \((w_j,z^2_{1j},\ldots,z^2_{pj})\) in layer 2, do not determine the last term. They do not even determine the backward signal \(W^\top\delta^2_b\) in (31).

This is an algebraic lack of closure, not just a counting complaint. If \(v\) is orthogonal to the span of all current \(h^1_a\), replace \(W\) by \(W+uv^\top\). Every current forward preactivation on the panel is unchanged. However,

\[
(W+uv^\top)^\top\delta^2_b-W^\top\delta^2_b
=v(u^\top\delta^2_b), \tag{33}
\]

which is generically nonzero. Thus even the complete labeled current forward arrays can agree while their forward time derivatives differ. This example concerns possible states; it does not prove that two such states lie on the same specified training ensemble. A closure restricted to reachable random states must prove the extra conditional-law assertion, rather than bypassing (33).

A minimally enriched current law must include backward fields
\(r_{b,i}=(W^\top\delta^2_b)_i\), jointly with the first-layer representation. But differentiating them introduces
\(\dot W^\top\delta^2_b+W^\top\dot\delta^2_b\), including new weighted products involving \(W\) and \(W^\top\). Consequently this enrichment starts a response hierarchy; it does not close it.

The exact integrated matrix update identifies the needed temporal correlations:

\[
W(t)=W(0)+\frac2{mn}\sum_b\int_0^t
c_b(s)\delta^2_b(s)h_b^{1\top}(s)ds. \tag{34}
\]

Define the two-time pairings, with the order of their roles retained,

\[
G^1_{ba}(s,t)=\frac1n h_b^{1\top}(s)h^1_a(t),\qquad
B^2_{ba}(s,t)=\frac1n\delta_b^{2\top}(s)\delta^2_a(t).
\]

Then

\[
\begin{aligned}
W(t)h^1_a(t)&=W(0)h^1_a(t)+\frac2m\sum_b\int_0^t
c_b(s)\delta^2_b(s)G^1_{ba}(s,t)ds,\\
W(t)^\top\delta^2_a(t)&=W(0)^\top\delta^2_a(t)+\frac2m\sum_b\int_0^t
c_b(s)h^1_b(s)B^2_{ba}(s,t)ds.
\end{aligned} \tag{35}
\]

These are exact forward/backward memory identities. The frozen Gaussian matrix in the remaining terms is reused in both directions, while its arguments depend on that same matrix through training. Its effects therefore cannot be supplied by independent fresh Gaussian draws with the correct marginal covariance. An adequate limiting description needs joint forward/backward conditional laws or response operators, in addition to the two-time covariances. Establishing precisely such a law at every layer is an additional theorem.

Storing an edge measure with test pairings
\(n^{-1}\sum_{ij}W_{ji}\alpha_i\beta_j\) can retain these correlations, but its uncompressed representation has \(n^2\) entries. Replacing it by \(n^{-2}\)-normalized edge statistics changes the scale. Naming either object a neuron distribution does not supply an ambient-independent model.

At arbitrary depth, (34)–(35) occur at each trainable dense layer and the backward recursion couples adjacent hierarchies. The shallow law avoids this issue because its fixed input Gram \(Q\) already contains every interaction between initial input directions; there is no learned intermediate random matrix that is traversed in both directions.

## 9. Route verdict and remaining implication

| Claim | Status and exact scope |
|---|---|
| Exact autonomous weak kinetic law | Proved for the one-hidden-layer model, including singular Gaussian initial covariance. |
| Well-posed characteristic kinetic flow | Proved with Gaussian moments and bounded first and second real derivatives. |
| All-time shallow fitting and deterministic replacement | Proved for a fixed positive initial feature Gram and sufficiently small fixed labels, with panel error \(O_{\mathbb P}(n^{-1/2})\). |
| Uniform concentration | Proved here along the deterministic shallow flow using finite total residual variation. Uniform concentration over arbitrary controls or a growing spectral class is not proved. |
| Preservation of realized leading width fluctuations | Exact fluctuation identity (25); finite approximation and limiting remainder theorem open. |
| Finite autonomous spectral model | Candidate (26) is globally well posed and dissipative; small-label fitting follows if its projected initial feature Gram has a positive gap. |
| Polylogarithmic spectral approximation | Analytic-radius, nonlinear truncation stability, and computable quadrature estimates unresolved. |
| Fixed-strip analytic argument | Its needed polynomially controlled flow extension is disproved by (29), even for an admissible entire activation. This does not disprove every polylogarithmic representation. |
| Independent layerwise kinetic extension | Algebraically incomplete: (32)–(35) require forward/backward and temporal correlations. A reachable-state closure remains open. |
| Arbitrary-depth dense target | Not solved by this route. |

The highest-leverage next theoretical obligation for this route is an autonomous approximation theorem for (26), or another true moment model, in a weighted analytic class that survives the amplification in (29). A proof only of shallow concentration, a quadrature particle relabeling, or a deep Gaussian marginal recursion would not discharge that obligation or the separate deep correlation problem.
