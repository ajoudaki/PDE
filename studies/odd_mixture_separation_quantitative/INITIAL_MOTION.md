# Appendix B. Initial motion for two inputs

The raw model is Theorem T.1. The Gaussian-program and derivative-valid initialization observations used here are proved in Appendix C, Parts F and V.I; the source specialization is checked in the main text.

Fix
\[
 \phi(z)=az+e\arctan z,\qquad \tfrac12\le a\le1,\quad e>0,
 \qquad |\rho|\le1-\delta,\quad 0<\delta\le1.
\]
Use the raw model and metric (T.3)--(T.7), two labels \(y_i\in\{-1,1\}\), and put \(p_i=y_i/2\), \(\tau=y_1y_2\). The restriction \(\delta\le1\) is the nonvacuous range for this symmetric separation. All second derivatives are identified by their time coordinate below.

## 1. Forward nondegeneracy and a useful initial kernel bound

The first preactivation pair is nondegenerate centered Gaussian. For any nondegenerate centered Gaussian pair \((U,V)\) with equal marginal variance and any \((u_1,u_2)\ne0\), a zero \(L^2\) norm of \(u_1\phi(U)+u_2\phi(V)\) would, by positive Gaussian density and continuity, give the identity
\[
 u_1\phi(s)+u_2\phi(t)=0\quad\text{for every }s,t\in\mathbb R.
\]
Differentiating separately, and using \(\phi'>0\), forces both coefficients to vanish. Thus the feature Gram is positive definite. Induction through the two fresh forward calls makes every initialized preactivation pair nondegenerate Gaussian and every initialized feature Gram positive definite.

Here is a uniform lower bound, which does not require a Gram inverse. Let \(q_0=1,c_0=\rho\) and let \(q_\ell,c_\ell\) be the common feature second moment and cross moment after layer \(\ell\). Since \(\phi'\ge a\) and \(\phi\) is odd,
\[
 |\phi(u)-\phi(v)|\ge a|u-v|,\qquad
 |\phi(u)+\phi(v)|\ge a|u+v|.
\]
Each initialized Gaussian pair is exchangeable, so
\[
 q_\ell\pm c_\ell
 =\tfrac12E[\phi(U)\pm\phi(V)]^2
 \ge a^2(q_{\ell-1}\pm c_{\ell-1}).
\]
Consequently
\[
 q_\ell\pm c_\ell\ge a^{2\ell}(1\pm\rho),\qquad
 \kappa_0:=\left\|\sum_i p_i h^3_{i,0}\right\|_3^2
 =\frac{q_3+\tau c_3}{2}
 \ge\frac{a^6\delta}{2}\ge\frac\delta{128}>0.
\]
These bounds hold for both label sectors. They are lower bounds, not formulas for a shifted activation. For the odd affine reference \(\phi(z)=az\), the exact formula is
\[
 \kappa_{0,\mathrm{aff}}=a^6(1+\tau\rho)/2.
\]

## 2. Full transpose covariances survive oddness

Write \(H_0=\sum_i p_i h^3_{i,0}\), \(D_i^\ell=\phi'(Z^\ell_{i,0})\), and
\[
 \beta_i^3=H_0D_i^3,\qquad S_3=E_3[\beta^3(\beta^3)^T].
\]
The matrix \(S_3\) is strictly positive definite even in the same-label sector. Indeed, a zero quadratic form would imply the everywhere identity
\[
 [p_1\phi(z_1)+p_2\phi(z_2)]
 [u_1\phi'(z_1)+u_2\phi'(z_2)]=0.
\]
For each fixed \(z_2\), the first factor has at most one zero as a function of \(z_1\), because \(p_1\ne0\) and \(\phi'>0\). The second factor vanishes off that point and hence everywhere by continuity. Differentiating it in \(z_1\) gives \(u_1\phi''(z_1)=0\) for every \(z_1\). Since
\[
 \phi''(z)=-2ez/(1+z^2)^2
\]
is not identically zero, \(u_1=0\); positivity of \(\phi'\) then gives \(u_2=0\).

Let \(B_0:H_2\to H_3\) be the initialized top action. The fixed finite-program transpose identity is
\[
 B_0^*\beta_i^3
 =G_i^2+\sum_jh^2_{j,0}\,T_{ij},\qquad
 T_{ij}=E_3[\partial_{z_j}\beta_i^3],
\]
where the joint Gaussian pair \(G^2\) has covariance **\(S_3\) itself**, and is independent of the initialized population-two forward sources. Explicitly,
\[
 \partial_{z_j}\beta_i^3
 =p_j\phi'(z_j)\phi'(z_i)
 +\mathbf1_{i=j}\Big(\sum_kp_k\phi(z_k)\Big)\phi''(z_i).
\]
Replacing \(S_3\) by the covariance remaining after regression on the forward features is incorrect. The finite-rank source-space projection from Gaussian matrix conditioning has negligible normalized coordinate effect in the infinite-width limit; the deterministic response above remains, and the coordinate Gaussian innovation has the full second-moment covariance.

Define
\[
 \beta_i^2=D_i^2\left(G_i^2+\sum_jh^2_{j,0}T_{ij}\right),
 \qquad S_2=E_2[\beta^2(\beta^2)^T].
\]
Conditionally on the initial population-two forward pair,
\[
 \operatorname{Cov}(\beta^2\mid Z^2_0)
 =\operatorname{diag}(D^2)S_3\operatorname{diag}(D^2)
 \succeq a^2\lambda_{\min}(S_3)I.
\]
Thus \(S_2\succeq a^2\lambda_{\min}(S_3)I>0\). The second initialized transpose has the form
\[
 A_0^*\beta_i^2
 =G_i^1+\sum_jh^1_{j,0}E_2[\partial_{\xi_j^2}\beta_i^2],
 \qquad \operatorname{Cov}(G^1)=S_2,
\]
with \(G^1\) independent of the population-one root pair. In this derivative the deterministic coefficients \(T\) and Gaussian covariances are held fixed, and \(G^2\) is an independent named source. The derivative includes the actual \(h^2\)-dependence of the response term. Finally,
\[
 \beta_i^1=D_i^1A_0^*\beta_i^2.
\]
All derivative expectations are finite: the activation grows at most linearly, all positive-order derivatives used here are bounded, and the source variables have Gaussian moments. The derivative-valid single-transcript truncation proof in Appendix C, V.I, therefore applies without a new mesh-uniform assertion. Oddness changes no step of these identities.

## 3. Every hidden block has nonzero feature-time acceleration

Define, in the raw hidden metric,
\[
 V^1=\frac1d\sum_i p_i\beta_i^1x_i,\qquad
 V^2=\sum_i p_i\beta_i^2\otimes h^1_{i,0},\qquad
 V^3=\sum_i p_i\beta_i^3\otimes h^2_{i,0}.
\]
If \(F\) is the relevant initial feature Gram and \(S\) the corresponding beta Gram, then
\[
 \|V^\ell\|_{\mathrm{HS}}^2
 =\operatorname{tr}(S\operatorname{diag}(p)F\operatorname{diag}(p))>0
 \quad(\ell=2,3),
\]
since both matrices in this trace product are positive definite. For the first block, condition on the first forward pair and use the Gaussian innovation of covariance \(S_2\). This gives
\[
 dE_1\|V^1\|_{\mathbb R^d}^2
 \ge a^2\lambda_{\min}(S_2)
       \sum_i p_i^2\frac{\|x_i\|^2}{d}
 =\frac{a^2\lambda_{\min}(S_2)}2>0.
\]
The deterministic conditional means contribute a nonnegative term. No input Gram inverse is used.

On a strong feature-time solution \(\Theta'=\nabla g\) with the stated chain rule and bounded gates,
\[
 C(s)=sH_0+o_{L^2}(s),\qquad
 b_i^\ell(s)=s\beta_i^\ell+o_{L^2}(s).
\]
For example, propagate \(C(s)/s\to H_0\) backwards, using operator-norm continuity of trained actions, bounded gates, and convergence of a bounded multiplier acting on each fixed \(L^2\) factor. The hidden vector field divided by \(s\) tends to \(V\), so integration yields
\[
 \vartheta(s)=\vartheta(0)+\tfrac12s^2V+o_{\mathrm{raw}}(s^2).
\]
Every hidden parameter **block** therefore has nonzero second derivative. This does not claim that every scalar first-layer coordinate changes: directions orthogonal to the input span are unchanged by the raw update.

## 4. Every sample in every hidden layer has nonzero acceleration

Let \(U_i^\ell\) be the initial feature-time preactivation acceleration obtained by applying the forward linearization to \(V\). At the bottom,
\[
 U_i^1=\sum_j\Gamma_{ij}p_j\beta_j^1.
\]
Its conditional variance is bounded below by
\[
 \operatorname{Var}(U_i^1\mid Z^1_0)
 \ge a^2\lambda_{\min}(S_2)\sum_j\Gamma_{ij}^2p_j^2
 \ge a^2\lambda_{\min}(S_2)/4>0.
\]
For the upper layers, product rules and actual adjoints give
\[
 \sum_i p_i\langle\beta_i^2,U_i^2\rangle_2
 =dE\|V^1\|^2+\|V^2\|_{\mathrm{HS}}^2>0,
\]
\[
 \sum_i p_i\langle\beta_i^3,U_i^3\rangle_3
 =\|V\|_{\mathrm{hidden}}^2>0.
\]
For instance \(U_i^2=V^2h_i^1+A_0(D_i^1U_i^1)\); pairing the first term produces \(\|V^2\|^2\), and moving \(A_0\) to its actual adjoint in the second produces the first-block norm. The next layer adds \(\|V^3\|^2\).

Hence at least one sample has nonzero acceleration in each upper layer. To obtain **each** sample, use the existing input reflection \(Qx_1=x_2\), \(Qx_2=x_1\) and the raw isometry
\[
 (w,A,B,C)\longmapsto(Qw,A,B,\tau C).
\]
Its initialization law is invariant, and it preserves the scalar objective. It sends \(\beta_i^\ell\) to \(\tau\beta_{\pi i}^\ell\), \(V^1\) to \(QV^1\), leaves \(V^2,V^3\) unchanged, and sends \(U_i^\ell\) to \(U_{\pi i}^\ell\). Thus the two \(U\)-fields have equal squared population norms. Both must be nonzero. Since \(D_i^\ell\ge a>0\), the feature acceleration \(D_i^\ell U_i^\ell\) is nonzero for every layer and sample as well. This symmetry works for both \(\tau=1\) and \(\tau=-1\); no even component of the activation is used.

## 5. Kernel change and the physical-time factors

Writing \(J_0\) for the bounded directional linearization of \(H\), adjunction gives \(V=J_0^*H_0\). Therefore
\[
 \kappa_4(s)=\|H(s)\|^2
 =\kappa_0+s^2\|V\|^2+o(s^2),
\]
\[
 \kappa(s)=\frac14y^TK(s)y
 =\kappa_0+2s^2\|V\|^2+o(s^2).
\]
The first coefficient follows from \(H(s)=H_0+(s^2/2)J_0V+o(s^2)\). The projected sum of hidden kernel blocks is \(s^2\|V\|^2+o(s^2)\). The total projected kernel thus changes strictly near zero.

The exact population reduction has \(ds/dt=2(1-g)\). Since \(g(0)=0\) and \(g'_s(0)=\kappa_0\),
\[
 s'(0)=2,\qquad s''(0)=-4\kappa_0.
\]
Consequently the physical hidden acceleration is \(4V\), the physical sample preactivation/feature accelerations are respectively \(4U_i^\ell\) and \(4D_i^\ell U_i^\ell\), and
\[
 \kappa_4(t)=\kappa_0+4t^2\|V\|^2+o(t^2),\qquad
 \kappa(t)=\kappa_0+8t^2\|V\|^2+o(t^2).
\]
For the readout, \(C_s'(0)=H_0\ne0\) and \(C_s''(0)=0\), but physical time gives
\[
 \dot C(0)=2H_0,\qquad \ddot C(0)=-4\kappa_0H_0\ne0.
\]
The latter follows directly by differentiating \(\dot C=2(1-g)H\), because the initial hidden velocity and hence \(\dot H(0)\) vanish. Thus **all four parameter blocks have nonzero physical initial acceleration**, while only the three hidden blocks have nonzero feature-time initial acceleration. The finite random readout remains the original one; these statements concern its population-zero initial limit.

