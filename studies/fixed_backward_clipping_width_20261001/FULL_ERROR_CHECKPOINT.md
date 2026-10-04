# Full population error: a quantitative bound with a nonvanishing label remainder

2026-10-01. Continuation requested by the user after the distinction between centered fluctuations and population error was explained. This note bounds the previously unquantified bias, but **does not prove the requested root-width theorem for fixed labels**. Its remainder is cubic in label RMS, not a proved decreasing function of width. All statements concern the actual fixed-positive-hard-cap q=1 closure and its own clipped population limit.

Scientific inputs are this study's complete fitting, concentration and population notes and the current manuscript definitions. No other study is a proof dependency. The new cavity, dimension-comparison and exceptional-initialization routes were assigned independently; their separate obligations are recorded below. No numerical experiment, manuscript edit or Git mutation was performed.

## 1. Setup and the precise outcome

Use exactly the equations in [FITTING_AND_THRESHOLD.md](FITTING_AND_THRESHOLD.md). In particular, the normalized keys and values are k=bar(h)/tau and v=-2bar(delta), the residual-RMS clock starts at one, and the only initialized middle operator is W_0. The derived action B=W_0+sum_a v_a k_a^T/(mn) is never trained independently. Both post-gate backward signals are recursively hard clipped at a fixed M>0 before residual multiplication. Width is n; sample count is m.

Write Y=||y||_2/sqrt(m), u_x=x/sqrt(d), and assume the limiting initial readout Gram Gamma_* has Gamma_* >= 2 lambda I. Fix K_0 sufficiently large, for example K_0=8. Let

\[
\mathcal G_n=\{\|W_0\|_{\rm op}\le K_0,
\quad \Gamma_n:=G_0^TG_0/(mn)\succeq\lambda I\}.
\]

Take Y below the width-independent fitting threshold in the fitting note (and below the possibly smaller stability threshold when invoking centered concentration). The Gaussian initialization satisfies

\[
p_n:=\Pr(\mathcal G_n^c)\le C e^{-cn}.                 \tag{1}
\]

A complete elementary proof, including the choice of operator threshold, is in [UNCONDITIONAL_TAIL_ROUTE.md](UNCONDITIONAL_TAIL_ROUTE.md). Section 3 below also specifies the bounded covariance statistics needed for its Gram part.

For any fixed probability law mu with finite second input moment, put

\[
\|F\|_{\mu,T}=\left(\int\sup_{0\le t\le T}|F(t,x)|^2d\mu(x)\right)^{1/2},
\qquad \|F\|_{\mu,\infty}=\left(\int\sup_{t\ge0}|F(t,x)|^2d\mu(x)\right)^{1/2}.
\]

Let f_{n,M} be the finite-width prediction, f_M the own population prediction, and

\[
\bar f_{n,M}(t,x)=\mathbb E[f_{n,M}(t,x)\mid\mathcal G_n].
\]

The bar is used to avoid confusing the finite-width mean with the sample count m. The bounds proved in Sections 2–5 are

\[
\boxed{\|\bar f_{n,M}-f_M\|_{\mu,\infty}
\le C_\mu\left(Y/n+Y^3\right),}                       \tag{2}
\]

\[
\boxed{\left(\mathbb E[\|f_{n,M}-f_M\|_{\mu,\infty}^2
\mid\mathcal G_n]\right)^{1/2}
\le C_\mu\left(Y/\sqrt n+Y^3\right),}                 \tag{3}
\]

and, without conditioning, for every finite T,

\[
\boxed{\left(\mathbb E\|f_{n,M}-f_M\|_{\mu,T}^2\right)^{1/2}
\le C_\mu\left(Y/\sqrt n+Y^3\right)
 +C Y\sqrt{T+1}\,e^{-cn/2}.}                          \tag{4}
\]

The statements hold for sufficiently large n, so that Pr(G_n)>=1/2. Constants depend on the fixed data and Gram margin, not on n, T or sufficiently small Y. They can be taken independent of the clipping threshold for these three bounds: only the pointwise contraction of clipping enters the comparison below. No conditional statement is made at a width where G_n has probability zero; in particular its positive Gram condition is impossible when n<m.

The first term of (3) is a genuine root-width sampling term. The Y^3 term is a bound on the contribution of feature learning to the prediction and to its bias. For **fixed positive Y**, it does not vanish as n grows. Hence (2)–(4) do not establish the requested root-width population approximation, nor do they contradict the already proved qualitative convergence. Shrinking Y with n would change the task and is not used as a resolution.

## 2. A comparison that retains the full actual dynamics

Introduce an auxiliary readout-only trajectory using the actual initialized features G_0=[g_{0,a}], solely as a comparison in the proof:

\[
\dot w^{\rm fr}=-\frac2mG_0r^{\rm fr},\qquad
r^{\rm fr}=G_0^Tw^{\rm fr}/n-y,\qquad w^{\rm fr}(0)=0.
\]

Let f_n^{fr}(t,x)=(w^{fr})^Tg_0(x)/n. This auxiliary trajectory does not replace the training model; its discrepancy from the actual feature-learning trajectory is explicitly bounded next. Define its population analogue f_*^{fr} using the initial population features. Both initial Gram matrices have a strictly positive margin on their respective spaces.

The complete fitting proof gives, on G_n and identically on the population spaces,

\[
\rho(t)\le Ye^{-\lambda t},\quad S_\infty\le Y/\lambda,
\quad \|w\|_\infty\le 2Y/\lambda,
\]
\[
\|A-A_0\|_F/\sqrt n+\|B-W_0\|_{\rm op}\le CY^2,
\quad \max_a\|g_a-g_{0,a}\|_2/\sqrt n\le CY^2,
\]
\[
\|\Gamma(t)-\Gamma_n\|_{\rm op}\le CY^2,
\qquad \|e(t)\|_m\le CY^2\rho(t),
\quad \dot r=-2\Gamma(t)r+e(t).                     \tag{5}
\]

Here ||.||_m denotes sample RMS. Since dot r^{fr}=-2 Gamma_n r^{fr}, the difference q=r-r^{fr}, initially zero, satisfies

\[
\dot q=-2\Gamma_nq+F(t),\qquad
F=-2(\Gamma(t)-\Gamma_n)r+e,
\quad \|F(t)\|_m\le CY^2\rho(t).
\]

The matrix exponential bound ||exp(-2 Gamma_n t)||op<=exp(-2 lambda t) gives

\[
\int_0^\infty\|q(t)\|_m dt
\le (2\lambda)^{-1}\int_0^\infty\|F(t)\|_m dt
\le CY^3.                                         \tag{6}
\]

Subtract the two readout updates, writing G(t)r-G_0r^{fr}=G_0q+(G(t)-G_0)r. Cauchy–Schwarz over the samples and (5)–(6) imply

\[
\sup_t\|w(t)-w^{fr}(t)\|_2/\sqrt n\le CY^3.          \tag{7}
\]

For every passive query, tanh is 1-Lipschitz and ||h_0(x)||_2/sqrt(n)<=1, so

\[
\begin{aligned}
\|g(t,x)-g_0(x)\|_2/\sqrt n
&\le \|B\|_{\rm op}\|[\tanh(Au_x)-\tanh(A_0u_x)]\|_2/\sqrt n
 +\|B-W_0\|_{\rm op}\\
&\le C(1+\|u_x\|)Y^2.
\end{aligned}
\]

Using f_n-f_n^{fr}=<w-w^{fr},g_0(x)>_n+<w,g(t,x)-g_0(x)>_n therefore proves

\[
\sup_t|f_{n,M}(t,x)-f_n^{fr}(t,x)|
\le C(1+\|u_x\|)Y^3.                               \tag{8}
\]

The same proof with population pairings proves

\[
\sup_t|f_M(t,x)-f_*^{fr}(t,x)|
\le C(1+\|u_x\|)Y^3.                               \tag{9}
\]

No independence of trained neurons, fresh matrix, or learned dense layer is used in (5)–(9).

## 3. Initial covariance errors, including their means

Append a fixed query x to the training list. The list length is m+1, fixed independently of n. Let Q_{1,n} be the empirical covariance of its first-layer initial features. Its entries are averages of bounded independent identically distributed variables, so

\[
\mathbb E Q_{1,n}=Q_1,
\qquad \mathbb E\|Q_{1,n}-Q_1\|_F^2\le C/n.         \tag{10}
\]

Given A_0, the upper preactivation rows are independent centered Gaussian vectors of covariance Q_{1,n}. Let

\[
\mathcal T_{ab}(Q)=\mathbb E[\tanh Z_a\tanh Z_b],
\qquad Z\sim N(0,Q).
\]

Write Q_{2,n} for the empirical upper-feature covariance on this list. Conditional independence gives

\[
\mathbb E[Q_{2,n}\mid A_0]=\mathcal T(Q_{1,n}),
\quad \mathbb E[\|Q_{2,n}-\mathcal T(Q_{1,n})\|_F^2\mid A_0]
\le C/n.                                           \tag{11}
\]

The map T has uniformly bounded first and second derivatives along positive-semidefinite covariance segments. Indeed, for Phi(z)=tanh(z_a)tanh(z_b), Gaussian density differentiation followed by two integrations by parts gives

\[
D\mathcal T(Q)[H]=\frac12\sum_{ij}H_{ij}\mathbb E[\partial_{ij}\Phi(Z)],
\]

and a second differentiation gives

\[
D^2\mathcal T(Q)[H,J]=\frac14\sum_{ij,kl}H_{ij}J_{kl}
\mathbb E[\partial_{ijkl}\Phi(Z)].                  \tag{12}
\]

All displayed derivatives of Phi are bounded. One first proves these identities for positive-definite Q, then adds epsilon I on the whole segment and lets epsilon decrease to zero by bounded convergence. Thus the Taylor remainder is bounded uniformly even at singular covariances. From (10), the linear Taylor term has expectation zero; therefore, with Q_2=T(Q_1),

\[
\|\mathbb E Q_{2,n}-Q_2\|_F\le C/n,
\qquad \mathbb E\|Q_{2,n}-Q_2\|_F^2\le C/n.         \tag{13}
\]

These constants are uniform in the query x: every first-layer feature and every derivative of Phi is bounded, regardless of the input's norm. Conditioning on G_n changes either mean of a bounded covariance statistic by at most C p_n/(1-p_n). For large n, (1) and (13) consequently hold with expectation conditioned on G_n as well.

The training-only version of (10)–(11), with bounded-variable exponential concentration instead of variance estimates, proves exponential concentration of the initial readout Gram. Gaussian covariance interpolation supplies the Lipschitz transfer through T. This gives the Gram part of (1), with fixed m and lambda.

## 4. All-time width estimates for the auxiliary trajectory

Let kappa_n(x)=(g_{0,a}^Tg_0(x)/n)_a and let kappa_*(x) denote its population counterpart. Put

\[
J_t(H)=\int_0^t e^{-2Hs}\,ds.
\]

The exact readout-only solution is

\[
f_n^{fr}(t,x)=\frac2m\kappa_n(x)^TJ_t(\Gamma_n)y,
\quad f_*^{fr}(t,x)=\frac2m\kappa_*(x)^TJ_t(\Gamma_*)y. \tag{14}
\]

On H>=lambda I, J_t and its first two matrix derivatives are bounded uniformly over t>=0. To check this, Duhamel differentiation gives a first derivative integrand bounded by 2s exp(-2 lambda s)||Delta||, and a second derivative integrand bounded by 4s^2 exp(-2 lambda s)||Delta_1||||Delta_2||. Their integrals over [0,infinity) are finite. The same bounds hold on every segment joining Gamma_n and Gamma_*, since that segment has the same lower margin.

Consequently the function in (14) is uniformly Lipschitz, and has a uniformly bounded second derivative, in (Gamma,kappa), with bounds CY. Its linear Taylor part at (Gamma_*,kappa_*) has conditional expectation O(Y/n) by (13), and its remainder has conditional expected magnitude O(Y/n) by the mean-square part of (13). Thus

\[
\sup_{t\ge0}|\mathbb E[f_n^{fr}(t,x)\mid G_n]-f_*^{fr}(t,x)|
\le CY/n,                                          \tag{15}
\]

\[
\mathbb E[\sup_{t\ge0}|f_n^{fr}(t,x)-f_*^{fr}(t,x)|^2\mid G_n]
\le CY^2/n.                                        \tag{16}
\]

The bounds are uniform in x. Applying Minkowski to (8), (9) and (16) proves (3), with only the second input moment for the two feature-learning remainders. Applying the mean and then (15) instead proves (2). This proves an explicit bias bound, but its Y^3 term has not been turned into a width error.

More precisely, write R_n=f_{n,M}-f_n^{fr} and R_*=f_M-f_*^{fr}. Then

\[
\bar f_{n,M}-f_M
=\{\mathbb E[f_n^{fr}\mid G_n]-f_*^{fr}\}
 +\{\mathbb E[R_n\mid G_n]-R_*\}.                   \tag{17}
\]

The first brace is O(Y/n); the second is bounded by C_mu Y^3 and converges qualitatively to zero. A root-width estimate for the second brace, for fixed Y, is still unproved. This is the feature-learning bias obligation, now separated from the initial random-feature statistics.

## 5. Removing initialization conditioning on a finite horizon

For every initialization, put U(t)=||w(t)||_2^2/n. The unchanged readout equation gives the exact identity

\[
\dot U=-4\|f_{\rm train}\|_m^2+4\langle y,f_{\rm train}\rangle_m
=Y^2-4\|f_{\rm train}-y/2\|_m^2\le Y^2.
\]

Since U(0)=0 and tanh is bounded,

\[
|f_{n,M}(t,x)|^2\le U(t)\le Y^2t                 \tag{18}
\]

for every query, regardless of the initial Gram or matrix norm. Finite-time global existence follows, for example, by combining this bound with rho<=sqrt(U)+Y, the bounded clips and keys, and tau>=1. The complete tail note supplies further activity and state bounds.

The population fitting estimate gives |f_M(t,x)|<=2Y/lambda uniformly in both time and input. On the bad event, therefore,

\[
\|f_{n,M}-f_M\|_{\mu,T}^2\le 2Y^2T+8Y^2/\lambda^2.
\]

Multiplication by p_n and (1), combined with (3) on the good event, proves (4). This argument applies to every finite T, including a specified T=T_n; it does not pass to T=infinity. Rare bad initializations require a separate all-time moment estimate if the desired theorem is an all-initialization RMS theorem rather than a high-probability theorem.

## 6. What the independent routes resolve and leave open

The cavity route retains the actual transpose response when a row is removed and reinserted. A small normalized change in the lower population can produce an order-one returned scalar field, so a proof that simply declares the row independent would change the limiting model. The route isolates inverse-free response traces; their finite-width bias is a remaining quantitative obligation.

The dimension-comparison route interpolates a full width-2n Gaussian mixer with a block mixer consisting of two width-n copies. The block system still shares residuals and memory contractions. Comparing that coupled union to two separate copies is distinct from comparing the full mixer to the block mixer. The latter comparison requires cancellation in a signed Gaussian response trace; ordinary Lipschitz concentration does not bound it at the required order.

The exceptional-initialization route proves (1) and (18). It has not proved a width-uniform all-time moment on G_n^c, and has not found an admissible counterexample showing that such a moment is impossible.

These are bounded research attempts, not a proof that the root-width target is false. The fixed positive cap certifies stable feedback and root-width centered fluctuations. The present continuation adds the explicit full-error bounds (2)–(4), while preserving the open quantitative feature-learning bias and all-time exceptional-event obligations.

## Check status

The scoped [FULL_ERROR_CHECK.md](FULL_ERROR_CHECK.md) independently reconstructed (2)–(4) and found no mathematical blocker. Its width-domain correction was applied: conditional claims are restricted to sufficiently large n, and no conditional expectation on a null good event is asserted. The checker used the supplied own-population construction as an explicit dependency and did not re-review its underlying Gaussian-program sources. The coordinator read the complete reconstruction and all three new route reports. This is internally checked research material, not a promoted book or manuscript result. The unfinished cavity and interpolation steps are not used to assert (2)–(4).
