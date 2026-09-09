# Entropy, Large-Deviation, and Weak Transport Machinery Audit

## Verdict

A localized Gaussian relative-entropy comparison has an exact and useful
Stein cancellation.  It can respect rare events without assuming false
square-exponential moments of adaptive Gaussian mixtures.  It nevertheless
does **not** replace the missing reachable-flow stability:

- the standard diffeomorphism/Jacobian route requires ambient tangent
  control that diverges already at depth two;
- an averaged log-determinant repair requires the full tangent spectral
  distribution and near-singular-value control, a stronger unresolved
  theorem;
- entropy-to-observable transfer needs a speed-`n` concentration or LDP
  estimate whose proof again differentiates the adaptive flow;
- even the complete one-time law of the ordinary node fields is not
  restartable, by an exact transverse-matrix witness.

Thus entropy is retained as an audit identity and possible wrapper around a
future stability theorem, but rejected as an easier proof engine.

## 1. Natural Gaussian geometry

On parameter perturbations `H=(H_A,H_u,H_{G_1},...,H_{G_{D-1}})`, use the
Cameron metric of the initialization:

\[
 \|H\|_{\gamma,n}^{2}
 =\|H_A\|_2^2+\|H_u\|_2^2
  +n\sum_{l=1}^{D-1}\|H_{G_l}\|_F^2.                              \tag{1}
\]

For the normalized predictor `f=n^{-1}A^Tx_D`, the stated flow vector field
`V_n` obeys the exact identity

\[
 V_n=n\nabla_{\gamma,n}f.                                          \tag{2}
\]

Consequently

\[
 \dot f
 =\frac{\|x_D\|_2^2}{n}+\frac{\|b_1\|_2^2}{n}
  +\sum_{l=1}^{D-1}
   \frac{\|b_{l+1}\|_2^2\|x_l\|_2^2}{n^2}\ge0.                  \tag{3}
\]

Equation (3) explains the geometry, but supplies no contraction: the flow is
gradient ascent for an indefinite nonlinear function.

The rank-one parameter updates yield the exact Volterra formulas

\[
 \begin{aligned}
 G_l(t)&=G_l^0+\frac1n\int_0^t b_{l+1}(s)x_l(s)^T\,ds,\\
 z_{l+1}(t)&=G_l^0x_l(t)+\int_0^t b_{l+1}(s)C_l(s,t)\,ds,\\
 r_l(t)&=(G_l^0)^Tb_{l+1}(t)+\int_0^t x_l(s)B_{l+1}(s,t)\,ds,
 \end{aligned}                                                     \tag{4}
\]

where `C_l(s,t)=<x_l(s),x_l(t)>_n` and
`B_{l+1}(s,t)=<b_{l+1}(s),b_{l+1}(t)>_n`.  Two-time quantities therefore
arise in exact finite-width identities; merely hiding them in an entropy
functional does not create a one-time closure.

## 2. Arctangent's useful logarithmic-derivative cancellation

For `phi=arctan`,

\[
 \kappa(z)=\frac{\phi''(z)}{\phi'(z)}
 =-\frac{2z}{1+z^2},\qquad |\kappa(z)|\le1.                        \tag{5}
\]

Thus backpropagate variations should be grouped as

\[
 \delta b_D=D_D\delta A+\kappa_D b_D\odot\delta z_D,
\]

and

\[
 \delta b_l=D_l\delta r_l+\kappa_l b_l\odot\delta z_l.            \tag{6}
\]

Splitting `r_l phi''(z_l)` or `A phi''(z_D)` before applying (5) loses a
real rare-coordinate cancellation.  This grouping should be kept in every
future tangent estimate.

## 3. Exact Gaussian entropy cancellation

Let `gamma_n` be the initialization Gaussian measure in the Cameron
coordinates (1).  For an orientation-preserving `C^1` diffeomorphism
`T=I+e`, change of variables gives

\[
 H(T_\#\gamma_n\mid\gamma_n)
 =\mathbb E\left[
 \frac12(\|T(W)\|_{\gamma,n}^2-\|W\|_{\gamma,n}^2)
 -\log\det DT(W)\right].                                          \tag{7}
\]

Gaussian integration by parts cancels the complete linear displacement:

\[
 H(T_\#\gamma_n\mid\gamma_n)
 =\frac12\mathbb E\|e\|_{\gamma,n}^2
 +\mathbb E\{\operatorname{tr}De-\log\det(I+De)\}.               \tag{8}
\]

If `Phi_t^n` is the exact flow and `Psi_{t,h}^n` an Euler approximation,
the formal comparison map is

\[
 T=(\Psi_{t,h}^n)^{-1}\Phi_t^n.                                   \tag{9}
\]

Rare events can be handled without conditioning.  On an initial good set
`K_R`, choose a smooth cutoff `chi_R` supported in `K_{R+1}` and set
`bar T=I+chi_R(T-I)`.  Then the modified comparison agrees with the exact
one on `K_R` and is the identity outside `K_{R+1}`; (8) retains its bulk
Stein cancellation.  The modification costs at most
`gamma_n(K_R^c)` at the law level.

## 4. Exact tangent and acceleration calibration

At depth two, for `h=(a,g,w)`, define

\[
 \begin{aligned}
 y_1&=D_1w,\\
 v_2&=gx_1+Gy_1,\qquad y_2=D_2v_2,\\
 c_2&=D_2a+\kappa_2b_2\odot v_2,\\
 s_1&=g^Tb_2+G^Tc_2,\\
 c_1&=D_1s_1+\kappa_1b_1\odot w.
 \end{aligned}                                                     \tag{10}
\]

Then

\[
 DV_n[h]=\left(y_2,
 \frac{c_2x_1^T+b_2y_1^T}{n},c_1\right).                          \tag{11}
\]

At arbitrary fixed depth the same untailored rule is

\[
 \begin{aligned}
 v_1&=w,\quad y_l=D_lv_l,\\
 v_{l+1}&=g_lx_l+G_ly_l,\\
 c_D&=D_Da+\kappa_Db_D\odot v_D,\\
 s_l&=g_l^Tb_{l+1}+G_l^Tc_{l+1},\\
 c_l&=D_ls_l+\kappa_lb_l\odot v_l,
 \end{aligned}                                                     \tag{12}
\]

with

\[
 DV_n[h]=\left(y_D,
 \left(\frac{c_{l+1}x_l^T+b_{l+1}y_l^T}{n}\right)_{l=1}^{D-1},
 c_1\right).                                                       \tag{13}
\]

Inserting `h=V_n` into (12)--(13) gives the exact local acceleration.  It
exposes weighted terms `b_l^2 v_l^2`; these are the same response occupations
that defeat naive deterministic stability.

## 5. Ambient-Jacobian obstruction at depth two

At initialization, restrict a perturbation to row `i` of `G`, with

\[
 g_i=\frac{x_1^T}{\|x_1\|_2^2},\qquad g_j=0\quad(j\ne i).
\]

Then `delta z_{2,i}=1`, and direct substitution into (11) gives the Cameron
Rayleigh quotient

\[
 \frac{\langle g,DV_ng\rangle_{\gamma,n}}
      {\|g\|_{\gamma,n}^2}
 =q_1 A_i\phi''(z_{2,i}),
 \qquad q_1=\frac{\|x_1\|_2^2}{n}.                                \tag{14}
\]

A positive fraction of the `z_{2,i}` lie in an interval where
`|phi''|` is bounded below, independently of the Gaussian `A_i`.  Extreme
values therefore imply

\[
 \|DV_n(\Theta_0)\|_{\mathrm{op},\gamma}
 \gtrsim\sqrt{\log n}                                              \tag{15}
\]

with high probability.  Hence no fixed high-probability localization makes
the ambient tangent operator uniformly bounded.  In particular, an inverse
map proof based on `h||DV_n||_op<1` fails when width is sent to infinity
before the mesh.

Actual Euler defects may occupy a much smaller correlated cone, but entropy
Jacobians see all ambient Gaussian directions.  Replacing the operator bound
by direct control of

\[
 \operatorname{tr}De-\log\det(I+De)
\]

requires the whole tangent singular-value distribution and control near
zero.  That is stronger, not weaker, than the current reachable-direction
problem.

## 6. Exact failure of nodewise one-time closure

At depth two, choose a rank-one perturbation

\[
 H=wq^T,\qquad w\perp b_2,\qquad q\perp x_1,\qquad
 q^TD_1b_1\ne0.                                                     \tag{16}
\]

Replacing `G` by `G+H` leaves all current ordinary node fields

\[
 u,x_1,z_2,x_2,A,b_2,r_1,b_1
\]

exactly unchanged, because `Hx_1=0` and `H^Tb_2=0`.  Yet

\[
 \dot z_2=q_1b_2+GD_1b_1
\]

changes by `HD_1b_1`, which is nonzero by (16).  Therefore even the complete
joint one-time law of the ordinary node fields does not determine its own
future.  A restartable state must retain transverse matrix-action
observables.  Retaining every such action either scales like the full matrix
or requires a restricted typed response calculus with a proved completion.

## 7. What a successful entropy theorem would have to prove

Whiten the matrix coordinates using

\[
 S_n(A,u,G_1,G_2)=(A,u,\sqrt nG_1,\sqrt nG_2)
\]

and let

\[
 \widehat e_{t,h}=S_n\big((\Psi_{t,h}^n)^{-1}\Phi_t^n-I\big)S_n^{-1}.
\]

A strong sufficient estimate is

\[
 \sup_{t\le T}\left[
 \frac1n\mathbb E\|\chi_R\widehat e_{t,h}\|_2^2
 +\frac1n\mathbb E\|D(\chi_R\widehat e_{t,h})\|_{HS}^2
 \right]\le C_{R,T}h^2,                                          \tag{17}
\]

together with an orientation/invertibility bound and

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \mathbb P(K_R^c)=0.                                               \tag{18}
\]

Equations (8), (17), and (18) would yield a normalized entropy comparison.
The leaf audit is:

1. **Primal/backpropagate envelope:** obtainable by deterministic triangular
   norm inequalities and Gaussian initial tails.
2. **Local defect:** the `kappa` grouping removes a false curvature loss, but
   remaining products require uniform integrability along the actual flow.
3. **Hilbert--Schmidt tangent estimate:** Gaussian randomization converts it
   to an averaged tangent, but the energy contains precisely
   `b_l^2v_l^2`.  Gaussian Poincare or Malliavin bounds differentiate the
   same flow and are circular.
4. **Ambient operator/inverse estimate:** falsified by (15).
5. **Localized conjugacy:** elementary once 2--4 are available.
6. **Entropy-to-observable transfer:** normalized entropy alone is
   insufficient by Pinsker.  A speed-`n` concentration/LDP for the
   fixed-mesh observable is additionally required; a Gaussian-gradient proof
   again needs tangent stability.
7. **Autonomous identification:** falsified for the ordinary nodewise state
   by (16); a restricted transverse-action state remains to be constructed.

For a nonlinear cumulant generating functional

\[
 \Lambda_n(t,F)=\frac1n\log\mathbb E e^{nF(\Theta_t)},
 \qquad L_n=V_n\cdot\nabla,
\]

one has exactly

\[
 \partial_t\Lambda_n=\langle L_nF\rangle_F,
 \quad
 \partial_t^2\Lambda_n
 =\langle L_n^2F\rangle_F+n\operatorname{Var}_F(L_nF).             \tag{19}
\]

Already (19) creates a new speed-`n` tilted covariance, so a finite cumulant
EGF does not close automatically.

## 8. Kill-gate decision

Modulated energy, martingale revealment, nonlinear-semigroup comparison, and
large-deviation exponential equivalence all meet the same obstruction:
their error term is an actual or averaged tangent of the adaptive tied-source
flow.  The entropy identity (8) is exact and potentially useful after such a
tangent theorem exists.  It does not prove that theorem.

The authoritative claim levels are therefore:

- Cameron gradient geometry, (3)--(8), tangent recursion (10)--(13), the
  divergence witness (14)--(15), and transverse nonclosure (16) are
  **established exact statements**;
- localized entropy comparison is **conditional** on stronger tangent,
  spectral, and concentration leaves;
- ordinary nodewise one-time law closure and a width-uniform ambient
  Jacobian route are **falsified**;
- entropy/LDP is **killed as an easier machinery**, though its Stein
  cancellation and `kappa` grouping should be reused as audit tools.
