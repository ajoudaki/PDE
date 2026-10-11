# Extension to independent Gaussian readout initialization

2026-10-10. Scoped follow-up to `GAUSSIAN_NONLINEAR_TOP_POSITIVE.md`. That frozen proof is unchanged. This note uses its Gaussian first-invariant geometry lemma, stated explicitly below, and proves the additional initialization steps and all subsequent estimates for a nonzero initial readout. No simulations are used.

## Statement and scope

Fix a matrix \(X\in\mathbb R^{d\times m}\) with linearly independent unit columns, \(m\ge2\), and a deterministic label vector \(y\in\mathbb R^m\), independently of width. Consider

\[
 U=AX,\quad Z=WU,\quad H=\phi(Z),\quad
 f=H^\top w/n,\quad r=f-y,\quad
 \mathcal L=\|r\|^2/m.
\]

The dimensions of \(A,W,w\) are \(n\times d,n\times n,n\), respectively. All three blocks train by gradient flow with mobilities \(n,1,n\). Assume that the real-analytic activation satisfies

\[
 0<c_\phi\le\phi'(z)\le L_\phi<\infty,
 \qquad
 |\phi(z)-z\phi'(z)|\le M_\phi<\infty
 \quad(z\in\mathbb R).
\tag{1}
\]

The value \(\phi(0)\) need not vanish. Examples include \(z+\varepsilon\arctan z\) and \(z+\varepsilon\tanh z\), with \(\varepsilon>0\). The first activation is exactly linear; this is not a tanh/tanh result.

Initialize independently

\[
 A_{ij}(0)\sim N(0,1),\qquad W_{ij}(0)\sim N(0,1/n),\qquad
 w_i(0)\sim N(0,\sigma_n^2),
 \qquad 0\le\sigma_n\le\sigma_*<\infty.
\tag{2}
\]

The case \(\sigma_n=0\) means a deterministically zero readout. Thus (2) includes zero readout, stored variance \(1/n^2\), and bounded order-one stored variance, with the forward normalization \(1/n\) kept fixed.

**Theorem.** For every fixed label vector \(y\), the probability that the finite-width trajectory converges to finite parameters and fits \(y\) tends to one as \(n\to\infty\). Moreover, there exist deterministic positive decay constants, independent of width, giving eventual exponential loss decay on events whose probabilities tend to one. For \(y\ne0\), one may choose deterministic \(t_*>0\) and \(\gamma>0\) such that

\[
 \mathbb P\!\left\{
 \mathcal L(t)\le \frac{\|y\|^2}{m}
             e^{-\gamma(t-t_*)}\quad\hbox{for every }t\ge t_*
 \right\}\longrightarrow1.
\tag{3}
\]

For \(y=0\), the bound instead has the initial loss as its prefactor and holds from time zero on a probability-tending-to-one event. The theorem is for each fixed label vector, not one event asserted simultaneously for every label vector. Constants may depend on the fixed data, activation, labels, and \(\sigma_*\).

## Exact identities with nonzero readout

Set \(D=\phi'(Z)\). The exact equations remain

\[
\begin{aligned}
 \dot w&=-\frac2mHr,\\
 \dot W&=-\frac{2}{mn}\operatorname{diag}(w)D
                       \operatorname{diag}(r)X^\top A^\top,\\
 \dot A&=-\frac2mW^\top\operatorname{diag}(w)D
                       \operatorname{diag}(r)X^\top.
\end{aligned}
\tag{4}
\]

Write

\[
 \rho=\sqrt{\mathcal L},\quad Y=\|y\|/\sqrt m,\quad
 a^2=\|A\|_F^2/n,\quad q^2=\|w\|^2/n,\quad
 S(t)=\int_0^t q(s)\rho(s)\,ds.
\]

For \(\theta=(A,W,w)\), use the mobility norm

\[
 \|\theta\|_{M^{-1}}^2=\|A\|_F^2/n+\|W\|_F^2+\|w\|^2/n.
\]

Energy dissipation and Cauchy–Schwarz give

\[
 \dot{\mathcal L}=-\|\dot\theta\|_{M^{-1}}^2,
 \qquad
 \|\theta(t)-\theta(s)\|_{M^{-1}}
 \le\rho(0)\sqrt{t-s}.
\tag{5}
\]

Thus every finite-width trajectory exists at all finite times: at any hypothetical finite maximal time, (5) makes the parameters Cauchy with a finite limit, and smooth local existence at that limit extends the trajectory.

The first-layer invariant is unchanged:

\[
 W(t)^\top W(t)-A(t)A(t)^\top/n=C_0,
 \qquad C_0=W(0)^\top W(0)-A(0)A(0)^\top/n.
\tag{6}
\]

Define \(\psi(z)=\phi(z)-z\phi'(z)\) and \(\Psi_{ja}=\psi(Z_{ja})\). Taking traces in (6) and differentiating \(q^2\) gives

\[
 \frac d{dt}(a^2-q^2)=\frac4{mn}w^\top\Psi r,
 \qquad
 \left|\frac d{dt}(a^2-q^2)\right|\le4M_\phi q\rho.
\]

Consequently

\[
 a^2(t)\le q^2(t)+a^2(0)-q^2(0)+4M_\phi S(t)
 \le q^2(t)+a^2(0)+4M_\phi S(t).
\tag{7}
\]

The new initial term has a favorable sign. Setting

\[
 R_0=1+a^2(0)+\|C_0\|_{\mathrm{op}}+|\phi(0)|/L_\phi,
\]

equations (6)--(7) and \(|\phi(z)|\le|\phi(0)|+L_\phi|z|\) imply

\[
 \|f\|\le L_\phi\sqrt m\,q(q^2+R_0+4M_\phi S).
\tag{8}
\]

For completeness, \(\|A\|_{\mathrm{op}}^2/n\le a^2\), \(\|W\|_{\mathrm{op}}^2\le a^2+\|C_0\|_{\mathrm{op}}\), and therefore

\[
 \|WAX\|_F/\sqrt n
 \le\sqrt m\sqrt{a^2(a^2+\|C_0\|_{\mathrm{op}})}
 \le\sqrt m\left(a^2+\tfrac12\|C_0\|_{\mathrm{op}}\right).
\]

Apply the activation growth bound and then \(\|H^\top w/n\|\le q\|H\|_F/\sqrt n\) to obtain (8).

## Gaussian events and the initial predictor

The Gaussian geometry lemma proved in the frozen positive note states that, for \(n\ge d+1\), an event depending only on \(A(0),W(0)\), of probability at least

\[
 1-\frac{524304(d^2+d)}n
 -2\exp\bigl((2n-d)\log9-8n\bigr),
\tag{9}
\]

has the following property: \(C_0\) has \(d\) eigenvalues at most \(-1/512\). Its deterministic consequence from (6) is

\[
 A(t)^\top A(t)/n\succeq\kappa I_d,
 \qquad\kappa=1/512,
\tag{10}
\]

for every time and every readout initialization. Indeed, on the fixed \(d\)-dimensional negative spectral subspace of \(C_0\),
\(\|A(t)^\top v\|^2/n=\|W(t)v\|^2-v^\top C_0v\ge\kappa\|v\|^2\); applying this to an orthonormal basis of that subspace gives (10). Independence of the new readout leaves the probability in (9) unchanged.

The independent initial readout satisfies, conditionally on \(H(0)\),

\[
 \mathbb E[f(0)\mid H(0)]=0,
 \qquad
 \mathbb E[\|f(0)\|^2\mid H(0)]
 =\frac{\sigma_n^2}{n^2}\|H(0)\|_F^2.
\]

Each initial preactivation has second moment one, because the inputs have unit norm. Hence

\[
 \mathbb E\|f(0)\|^2
 \le\frac{2m\sigma_*^2}{n}
       \bigl(|\phi(0)|^2+L_\phi^2\bigr)
 \longrightarrow0.
\tag{11}
\]

It follows that \(f(0)\to0\) and \(\rho(0)\to Y\) in probability. Also

\[
 \mathbb E q^2(0)=\sigma_n^2,\qquad
 \operatorname{Var}(q^2(0))=2\sigma_n^4/n.
\]

Thus \(q(0)\le q_*:=\sqrt{\sigma_*^2+1}\) with probability tending to one, by Chebyshev's inequality.

Define

\[
 G_*=\mathbb E[\phi(Z)\phi(Z)^\top],\qquad
 Z\sim N(0,X^\top X),\qquad
 \lambda=\tfrac12\lambda_{\min}(G_*)>0.
\]

Positive definiteness follows because \(X^\top X\) is positive definite and the derivative floor makes \(\phi\) an increasing bijection; \(\phi(Z)\) therefore has full support in \(\mathbb R^m\). For fixed constants \(a_*,w_*\), chosen sufficiently large, the event

\[
 a(0)\le a_*,\quad\|W(0)\|_{\mathrm{op}}\le w_*,\quad
 H(0)^\top H(0)/n\succeq\lambda I_m,
 \quad q(0)\le q_*
\tag{12}
\]

has probability tending to one. The first two conditions follow from Gaussian moments and a sphere-net bound. For the third, condition on \(A(0)\): the preactivation rows are independent Gaussians with covariance \(X^\top A(0)^\top A(0)X/n\), which converges to \(X^\top X\). The activation has at most linear growth, so fourth moments are uniformly bounded when this covariance is bounded. Conditional variance estimates give convergence of the empirical Gram to its conditional expectation. The latter converges to \(G_*\) by the representation \(\Sigma^{1/2}g\), continuity of the covariance square root near a positive-definite matrix, and dominated convergence under the Gaussian second-moment bound. No independence among (9), (11), and (12) is needed: a union bound makes their intersection have probability tending to one.

## A deterministic loss drop when the labels are nonzero

Assume \(Y>0\), and put \(R_*=Y+1\). Work on the preceding events and \(\rho(0)\le R_*\). From (5), the activation Lipschitz bound, and factoring the difference of the two matrix products,

\[
 \frac{\|H(t)-H(0)\|_F}{\sqrt n}
 \le L_\phi\sqrt m\,R_*\sqrt t\,
                  (a_*+w_*+R_*\sqrt t).
\tag{13}
\]

Choose a deterministic \(t_*>0\) so small that the right side at \(t_*\) is at most \(\sqrt\lambda/2\). The smallest singular value of \(H(t)/\sqrt n\) then stays at least \(\sqrt\lambda/2\) for \(0\le t\le t_*\). Since the tangent kernel \(K\), normalized by \(\dot r=-2Kr/m\), includes \(H^\top H/n\),

\[
 \rho(t_*)\le\rho(0)e^{-g t_*},\qquad
 g=\lambda/(2m)>0.
\]

Restrict further to

\[
 \rho(0)\le\min\{R_*,Y e^{g t_*/2}\}.
\tag{14}
\]

Both upper bounds strictly exceed \(Y\), so (14) has probability tending to one by (11). Therefore

\[
 \rho(t_*)\le Y e^{-g t_*/2}<Y,
 \qquad
 \delta_*:=Y(1-e^{-g t_*/2})>0.
\tag{15}
\]

This is the required strict loss drop below the zero-predictor loss, despite a possibly larger initial loss. Moreover, (5) gives \(q(t)\le q(0)+\rho(0)\sqrt t\), and hence

\[
 S(t_*)\le S_*:=q_*R_*t_*+\frac23R_*^2t_*^{3/2}.
\tag{16}
\]

## All-time bootstrap, fitting, and parameter convergence

Set \(\lambda_X=\lambda_{\min}(X^\top X)>0\). On (10), the middle-layer kernel obeys

\[
\begin{aligned}
 K&\succeq K_W\\
 &=\frac1n\sum_j w_j^2\operatorname{diag}(D_{j,:})
              \frac{U^\top U}{n}\operatorname{diag}(D_{j,:})\\
 &\succeq\kappa\lambda_Xc_\phi^2 q^2I_m.
\end{aligned}
\]

Thus, while \(\rho>0\),

\[
 \dot\rho\le-bq^2\rho,\qquad
 b=2\kappa\lambda_Xc_\phi^2/m>0.
\tag{17}
\]

For all \(t\ge t_*\), (15) and the reverse triangle inequality give \(\|f(t)\|\ge\sqrt m\,\delta_*\). Bound

\[
 R_0\le\overline R:=1+2a_*^2+w_*^2+|\phi(0)|/L_\phi,
 \qquad
 c_*:=\min\left\{1,
 \frac{\delta_*}{L_\phi(1+\overline R+4M_\phi)}\right\}>0.
\]

Equation (8), considering separately \(q\le1\) and \(q>1\), yields

\[
 q(t)\ge\frac{c_*}{1+S(t)}\qquad(t\ge t_*).
\tag{18}
\]

If \(\rho\) reaches zero, all velocities vanish and fitting is complete. Otherwise \(S'=q\rho>0\) after \(t_*\). Dividing (17) by \(S'\), using (18), and integrating gives

\[
 0\le\rho(t)
 \le\rho(t_*)-bc_*\log\frac{1+S(t)}{1+S(t_*)}.
\]

Consequently

\[
 S(t)\le\overline S:=(1+S_*)e^{Y/(bc_*)}-1,
 \qquad q(t)\ge\overline q:=\frac{c_*}{1+\overline S}>0.
\]

Substitution in (17) proves (3) with the deterministic rate

\[
 \gamma=2b\overline q^{\,2}>0.
\tag{19}
\]

The same estimates give finite parameter convergence. After \(t_*\), \(\rho\le Y\), and

\[
 \frac d{dt}q^2=-\frac4m f^\top r,
 \qquad
 \left|\frac d{dt}q^2\right|\le8Y\rho.
\]

Exponential decay makes the right side integrable, so \(q\) is bounded. Equations (6)--(7) and bounded \(S\) then bound \(\|A\|_F/\sqrt n\) and \(\|W\|_{\mathrm{op}}\). The equations (4) and the derivative upper bound make each of \(\|\dot A\|_F/\sqrt n\), \(\|\dot W\|_F\), and \(\|\dot w\|/\sqrt n\) at most a finite constant times \(\rho\). These velocities are integrable, so all parameter blocks converge. Continuity identifies the limiting prediction as \(y\).

## Zero labels

When \(y=0\), asking for loss strictly below \(Y^2=0\) would be invalid. A separate argument resolves this case.

For every initialization, the exact identity is

\[
 \frac d{dt}q^2=-4\mathcal L.
\]

Therefore \(\int_0^\infty\mathcal L(t)\,dt\le q^2(0)/4\). Since the loss is nonnegative and nonincreasing, its limit is zero. This already proves fitting without a geometry event.

For exponential decay and finite parameter convergence with probability tending to one, use (12) and \(\rho(0)\to0\). Choose a deterministic radius \(\eta>0\) such that

\[
 L_\phi\sqrt m\,\eta(a_*+w_*+\eta)<\sqrt\lambda/2.
\]

Within mobility distance \(\eta\) of the initial state, the same product estimate as in (13) gives \(K\succeq\lambda I_m/4\). Write the mobility speed as \(v=\|\dot\theta\|_{M^{-1}}\). On this ball,

\[
 v^2=-\dot{\mathcal L}\ge(\lambda/m)\rho^2.
\]

Until a possible first exit, the path length is bounded by

\[
 \int_0^t v(s)\,ds
 =\int_0^t\frac{-\dot{\mathcal L}(s)}{v(s)}\,ds
 \le2\sqrt{m/\lambda}\,[\rho(0)-\rho(t)]
 \le2\sqrt{m/\lambda}\,\rho(0).
\]

At zero loss the state is stationary, so the displayed division is used only where the speed is positive. On the event

\[
 \rho(0)\le\frac\eta4\sqrt{\lambda/m},
\]

the path length is at most \(\eta/2\), preventing a first exit. This event has probability tending to one by (11). The gap persists for all time and gives

\[
 \mathcal L(t)\le\mathcal L(0)e^{-\lambda t/m}.
\]

The finite total path implies convergence to finite parameters. This completes the fixed-label theorem, including zero labels.

All infinite-time conclusions here hold for each finite-width trajectory on its stated initialization event. The large-width limit enters only through the probability of that event. The initialization extension does not relax the linear first activation, independent-input-column, derivative-floor, or bounded-homogeneity-defect hypotheses.
