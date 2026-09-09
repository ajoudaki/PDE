# Broad bounded nonlinear perturbations: initialization and persistent nonaffinity

This note treats only Parts G and N of the specified three-sample manuscript. It proves the new initialization and nonaffinity lemmas directly. Transfer of the existing source-response and cap-removal arguments under the derivative bounds below is a separate obligation; nothing here presumes those arguments have already been audited.

Fix a nonconstant function `psi` in C_b^3(R), normalized so that

\[
 \|\psi\|_\infty,\ \|\psi'\|_\infty,
 \ \|\psi''\|_\infty,\ \|\psi'''\|_\infty\le1.
\]

Use

\[
 \phi(z)=a(1+z)+e\psi(z),\qquad a\ge2,\quad0<e\le1.
\]

In particular

\[
 a/2\le a-e\le\phi'(z)\le a+e\le2a.
\]

No parity, sign, or monotonicity condition is imposed on `psi`. Bounded nonconstant `psi` is necessarily nonaffine, and its second derivative is not identically zero. General finite C_b^3 bounds reduce to this normalization: for the original function `psi_orig`, take

\[
 M=\max\{1,\|\psi_{\rm orig}\|_\infty,
 \|\psi_{\rm orig}'\|_\infty,\|\psi_{\rm orig}''\|_\infty,
 \|\psi_{\rm orig}'''\|_\infty\},\quad
 \psi=\psi_{\rm orig}/M,\quad e=M e_{\rm orig}.
\]

## 1. Initial Gaussian feature coercivity without oddness

Let Z be a centered Gaussian three-vector with covariance Q and common positive marginal variance v. A singular Q is allowed. Write Z=Q^{1/2}G_3 with independent standard Gaussian coordinates. Put

\[
 \mu_v=E\psi(\sqrt vG),\qquad
 \nu_v=E\psi'(\sqrt vG),\qquad
 m_v=a+e\mu_v,\qquad b_v=a+e\nu_v.
\]

Integration by parts against each independent coordinate of G_3 gives

\[
 E[G_{3,k}\psi(Z_i)]=(Q^{1/2})_{ik}\nu_v.
\]

The projection of phi(Z_i) onto constants and all Gaussian linear functions of G_3 is therefore m_v+b_v Z_i. If r_i is its residual, then E r_i=0 and E[r_i G_{3,k}]=0 for every k. Consequently

\[
 E[\phi(Z)\phi(Z)^T]
 =m_v^2\mathbf1\mathbf1^T+b_v^2Q+(E[r_ir_j])_{ij}
 \succeq\frac{a^2}{4}(\mathbf1\mathbf1^T+Q).       \tag{A.1}
\]

The Gaussian integration by parts is justified by bounded psi and psi'; singularity of Q introduces no difficulty because it is performed in the independent coordinates. The residual Gram is positive semidefinite because its quadratic form is E(sum_i u_i r_i)^2. Since |mu_v|,|nu_v|≤1 and a≥2,e≤1, both m_v,b_v are at least a/2, proving the last inequality.

Let Q_0=Gamma, Q_l=(E[h_i^l h_j^l])_{ij}. Initialization has a fresh centered Gaussian forward field at each layer, with covariance Q_{l-1}; common marginal variances propagate because all inputs have equal norm. Iterating (A.1), with c=a²/4, gives

\[
 Q_1\succeq c(\Gamma+J),\qquad
 Q_2\succeq c^2\Gamma+(c^2+c)J,
\]
\[
 Q_3\succeq c^3\Gamma+(c^3+c^2+c)J
 \succeq\frac{a^6}{64}(\Gamma+J),\quad J=\mathbf1\mathbf1^T.
\]

The manuscript's elementary augmented-Gram inequality is Gamma+J≽(delta²/4)I. Thus, defining

\[
 \lambda=\delta^2/256,
\]

one has

\[
 K^4(0)=Q_3\succeq\lambda a^6I,
 \qquad Q_2\succeq4\lambda a^4I.                 \tag{A.2}
\]

This establishes full support of the initialized top Gaussian vector even when Gamma is singular.

## 2. Initial marginal standard deviations

Write sigma_l for the common standard deviation of the initialized preactivation at layer l. Then sigma_1=1. The linear Gaussian projection above shows

\[
 \sigma_{l+1}^2=E[\phi(\sigma_lG)^2]
 \ge b_{\sigma_l^2}^2\sigma_l^2
 \ge(a^2/4)\sigma_l^2.
\]

Hence every sigma_l for l=1,2,3 is at least one. Minkowski's inequality and |psi|≤1 give

\[
 \sigma_2\le a(1+\|G\|_2)+e\le2a+1\le3a,
\]
\[
 \sigma_3\le a(1+\sigma_2)+e
 \le a+3a^2+1\le5a^2.
\]

Therefore all initialized scalar preactivation laws lie in the explicit variance range

\[
              1\le\sigma_l\le5a^2.                         \tag{A.3}
\]

In particular, the covariance in the top layer also satisfies Q_2≼75a^4 I, since its trace is 3 sigma_3².

## 3. A universal inverse-scale residual lower bound

For a square-integrable real random variable Z of positive variance define

\[
 \mathcal R_\psi(Z)=\inf_{\alpha,\beta\in\mathbb R}
                  E[\psi(Z)-\alpha-\beta Z]^2.
\]

There exists an integer R≥1 for which

\[
 J_R=\inf_{\alpha,\beta}\int_{-R}^R
          [\psi(x)-\alpha-\beta x]^2\,dx>0.                 \tag{A.4}
\]

Indeed, the span of 1 and x is finite dimensional and closed in L²([-R,R]); if J_R=0, continuity makes psi affine on that interval. If J_R=0 for every positive integer R, the affine functions agree on nested intervals and psi is globally affine. A globally affine bounded function is constant, contradicting the assumption. The number J_R is directly computable from three integrals:

\[
 J_R=\int_{-R}^R\psi^2
 -\frac1{2R}\left(\int_{-R}^R\psi\right)^2
 -\frac3{2R^3}\left(\int_{-R}^Rx\psi(x)\,dx\right)^2.
\]

Define the positive shape constant

\[
 c_\psi=\min\left\{1,
      \frac{e^{-R^2/2}}{\sqrt{2\pi}}J_R\right\}>0.           \tag{A.5}
\]

For every sigma≥1 the N(0,sigma²) density on [-R,R] is at least exp(-R²/2)/(sigma sqrt(2pi)). Thus, for each affine predictor,

\[
 E[\psi(\sigma G)-\alpha-\beta\sigma G]^2
 \ge\frac{e^{-R^2/2}}{\sigma\sqrt{2\pi}}
        \int_{-R}^R[\psi(x)-\alpha-\beta x]^2\,dx.
\]

Taking the infimum gives the fully uniform lower bound

\[
              \mathcal R_\psi(\sigma G)\ge c_\psi/\sigma,
                         \qquad\sigma\ge1.                \tag{A.6}
\]

Combining (A.3) and (A.6), every initialized preactivation obeys

\[
 \mathcal R_\psi(Z_i^l)\ge\eta_a,
 \qquad\eta_a=\frac{c_\psi}{5a^2}>0.                        \tag{A.7}
\]

This dependence on a is what allows bounded localized perturbations, for which the arctangent proof's infimum over all scales is zero.

## 4. Stability under arbitrary L² perturbations

Suppose sd(Z_0)≥1, R_psi(Z_0)≥eta_a, and ||Z-Z_0||_2≤1/2. Centering is an orthogonal projection, so standard deviation is 1-Lipschitz and sd(Z)≥1/2. The optimal affine regression slope is

\[
 \beta_Z=\frac{\operatorname{Cov}(Z,\psi(Z))}
                        {\operatorname{Var}(Z)},\qquad
 |\beta_Z|\le\frac{\operatorname{sd}(\psi(Z))}
                         {\operatorname{sd}(Z)}\le2.
\]

Let alpha_Z be the corresponding intercept. Testing this same affine function at Z_0 gives

\[
 \sqrt{\mathcal R_\psi(Z_0)}
 \le\|\psi(Z_0)-\alpha_Z-\beta_Z Z_0\|_2
 \le\sqrt{\mathcal R_\psi(Z)}+3\|Z-Z_0\|_2.                \tag{A.8}
\]

The second inequality uses the 1-Lipschitz property of psi and the slope bound. Thus

\[
 t_a=\min\{1/2,\sqrt{\eta_a}/6\},\qquad
 \|Z-Z_0\|_2\le t_a
 \quad\Longrightarrow\quad
 \mathcal R_\psi(Z)\ge\eta_a/4.                             \tag{A.9}
\]

No Gaussian assumption on the perturbed Z is used. Finally, absorbing a(1+Z) into the free affine predictor yields the exact identity

\[
 \inf_{\alpha,\beta}E[\phi(Z)-\alpha-\beta Z]^2
                         =e^2\mathcal R_\psi(Z).           \tag{A.10}
\]

## 5. An explicit noncircular large-a rule

Retain the numerical controlled estimates G.14--G.20, replacing the old coercivity parameter by lambda=delta²/256. These numerical estimates continue to use only |psi|≤2, |psi'|≤1 and e≤1, so the present normalized bounds are sufficient. Their hidden displacement bound is

\[
 S=12/(\lambda a^6),\qquad
 D_S=1.44\cdot10^8/(\lambda^2a^6),
\]

and the maximum scalar preactivation displacement is bounded by

\[
 615a^2D_S=8.856\cdot10^{10}/(\lambda^2a^4).                 \tag{A.11}
\]

Set

\[
 \tau=\min\{1/2,\sqrt{c_\psi/5}/6\}>0.
\]

For every a≥1, t_a≥tau/a: both 1/2 and sqrt(c_psi/5)/(6a) are at least tau/a. Choose

\[
 a\ge\max\left\{2,\frac{2000}{\sqrt\lambda},
             \left(\frac{10^{12}}{\lambda^2\tau}\right)^{1/3}
        \right\}.                                        \tag{A.12}
\]

Then the manuscript's purely geometric stopped-flow inequalities hold with lambda, and

\[
 615a^2D_S
 \le0.08856\frac\tau a<t_a.                               \tag{A.13}
\]

After the remaining response threshold and cap-transfer obligations have been established for psi, the same global near-initial-state argument therefore proves

\[
 \inf_{t\ge0}\inf_{\alpha,\beta}
 E[\phi(z_i^l(t))-\alpha-\beta z_i^l(t)]^2
 \ge\frac{e^2c_\psi}{20a^2}>0
 \quad\text{for every }i,l.                               \tag{A.14}
\]

There is no circular definition: c_psi and tau depend only on the prescribed shape, lambda depends only on separation, and then (A.12) fixes a. The amplitude e is subsequently chosen below the positive source-response and initial-motion thresholds. For unnormalized psi_orig, apply the normalization at the start and translate the resulting amplitude bound by e_orig=e/M.

## 6. Initial backward Grams and hidden directions

Use the manuscript's definitions p_i=y_i/3, H=sum_i p_i phi(Z_i^3), d_i^l=phi'(Z_i^l), beta_i^3=Hd_i^3, and S_l=(E beta_i^l beta_j^l)_{ij}.

Since Q_2≻0, Z^3 has a strictly positive density on R³. If v^T S_3 v=0, continuity and full support imply

\[
 \left(\sum_i p_i\phi(z_i)\right)
 \left(\sum_i v_i\phi'(z_i)\right)=0
                           \quad\text{for every }z\in\mathbb R^3.
\]

The first factor cannot vanish on an open set: each coordinate derivative is p_i phi'(z_i)≠0. Its nonzero set is therefore dense, so the second factor vanishes everywhere. Differentiating the second factor in coordinate i gives v_i e psi''(z_i)=0 for every z_i. Because e>0 and psi'' is not identically zero, v_i=0 for each i. Hence S_3≻0.

Assuming the exact derivative-valid transpose decompositions N.13--N.14 have been extended to this psi, their fresh reverse covariance argument gives

\[
 S_2\succeq\frac{a^2}{4}\lambda_{\min}(S_3)I,
\]
\[
 \operatorname{Cov}(\beta^1\mid Z^1)
 \succeq\frac{a^2}{4}\lambda_{\min}(S_2)I.                  \tag{A.15}
\]

Every statement in N.17--N.19 then follows with its lower factor a² replaced by a²/4; the trace argument for the matrix directions needs no other change. In particular all hidden parameter directions and every bottom-sample preactivation direction are nonzero, including singular Gamma. Multiplication by phi'≥a/2 preserves nonzeroness of every feature direction. The upper-sample affine perturbation bounds N.40--N.53 use |psi|≤2 and |psi'|≤1, so their numerical error bounds are unchanged under the normalization here.

An optional fully explicit lower bound for S_3 is available. Choose z_0 with psi''(z_0)≠0 and phi(z_0)≠0; such a point exists because the first condition holds on an open set whereas strictly increasing phi has at most one zero. Choose r,rho>0 so that on I=[z_0-r,z_0+r], |psi''|≥rho and

\[
                    (a+1)r\le|\phi(z_0)|/6.
\]

The sign of psi'' on I is constant by continuity. For z∈I³ and every permitted label vector, |sum_i p_i|≥1/3 and sum_i|p_i|=1 imply

\[
 \left|\sum_i p_i\phi(z_i)\right|
 \ge\frac{|\phi(z_0)|}{3}-(a+1)r
 \ge\frac{|\phi(z_0)|}{6}.
\]

Let q_-=4lambda a^4 and q_+=75a^4. Since q_- I≼Q_2≼q_+ I, the density of N(0,Q_2) on I³ is at least

\[
 d_0=(2\pi)^{-3/2}q_+^{-3/2}
       \exp\{-3(|z_0|+r)^2/(2q_-)\}>0.
\]

For U uniform on I, the independent-coordinate integral is exactly

\[
 \int_{I^3}\left(\sum_i v_i\phi'(z_i)\right)^2dz
 =(2r)^3\left[
 e^2\operatorname{Var}(\psi'(U))\|v\|^2
 +(E\phi'(U))^2\left(\sum_i v_i\right)^2\right].
\]

For independent U,V uniform on I, the derivative lower bound gives |psi'(U)-psi'(V)|≥rho|U-V|. Hence Var(psi'(U))=E(psi'(U)-psi'(V))²/2≥rho² Var(U)=rho²r²/3. Integrating over this cube proves

\[
 S_3\succeq e^2\kappa I,\qquad
 \kappa=\frac{\phi(z_0)^2d_0(2r)^3\rho^2r^2}{108}>0.        \tag{A.16}
\]

The constants z_0,r,rho may depend on the fixed a,e,psi, but never on the input geometry or labels. No positive S_3 lower bound uniform as e decreases to zero should be asserted: at e=0 all three top backward vectors coincide.

## 7. Limits of the generalization

1. The arctangent quantity inf_{sigma≥1} R_psi(sigma G) need not be positive. For a nonzero smooth compactly supported psi, E psi(sigma G)²→0 by dominated convergence under the coupling sigma G, so R_psi(sigma G)→0. The inverse-scale estimate (A.6), together with the finite initialized scale bound, resolves precisely this issue.

2. The scale exponent is sharp for compactly supported nonzero shapes. The regression identity gives

   R_psi(sigma G)=E psi(sigma G)²-(E psi(sigma G))²-(E[G psi(sigma G)])².

   Changing variables on its compact support yields

   sigma R_psi(sigma G)→(1/sqrt(2pi))∫ psi(x)² dx>0.

   Here the mean is O(sigma^{-1}) and the G-weighted mean is O(sigma^{-2}), so their squares do not affect the displayed limit.

3. For the simpler subclass with finite distinct limits L_± at ±infinity, the original scale-uniform argument does extend. Dominated convergence yields

   R_psi(sigma G)→((L_+-L_-)²/4)(1-2/pi)>0.

   Continuity and strict positivity at each finite sigma then yield a positive infimum over sigma≥1. Equal limits instead give zero limiting residual. Neither limit condition is needed for (A.6)--(A.14).

4. No shape-independent positive margin can hold over every normalized nonconstant psi: arbitrarily small positive scalar multiples remain in the class and their residuals scale quadratically. The theorem must permit the activation-selection and nonaffinity constants to depend on psi, or impose an explicit positive lower bound on the local residual J_R.
