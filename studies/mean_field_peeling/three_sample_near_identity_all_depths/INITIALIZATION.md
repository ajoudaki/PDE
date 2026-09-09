# Initialization at every depth for the accepted unit-sum activation

2026-09-08. Independently checked by `/root/three_depth_review_geometry`.

**Verdict: PROVED INITIALIZATION RESULT ONLY.** The activation is within the accepted constraint. No overall gain, modified metric, changed algorithm, or small-offset assumption is used. The result does not prove global population fitting, bounded trained trajectories, cap removal, or a uniform-in-time trained nonaffinity bound.

Fix `0<theta<=1/2` and

\[
\phi_\theta(z)=(1-\theta)z+\theta\arctan z.
\]

Let three normalized inputs have Gram `Gamma`, with `Gamma_ii=1` and `|Gamma_ij|<=1-delta`, `0<delta<=1`. Singular `Gamma` is allowed. Define the initialized Gaussian forward recursion by `Q_0=Gamma`, a centered Gaussian triple `Z^k` of covariance `Q_(k-1)`, and

\[
(Q_k)_{ij}=E[\phi_\theta(Z_i^k)\phi_\theta(Z_j^k)].
\]

This is the canonical initialized covariance recursion for independent square Gaussian hidden matrices. Set `q_0=1`; all diagonal entries of `Q_k` equal

\[
q_{k+1}=E[\phi_\theta(\sqrt{q_k}G)^2],\qquad G\sim N(0,1).
\]

Then, for every integer `k>=0`,

\[
\frac1{1+(5/2)\theta k}\le q_k\le\frac1{1+\theta k/6}.
\tag{1}
\]

With `eta0=1/(108 pi e)`, every integer `L>=1` satisfies

\[
Q_L\succeq
\frac{\eta_0\theta^2\delta^2}
 {3[1+(5/2)\theta L]}I_3.
\tag{2}
\]

In fact the variance-normalized Grams `C_k=Q_k/q_k` satisfy

\[
\lambda_{\min}(C_{k+1})\ge\lambda_{\min}(C_k),\qquad
\lambda_{\max}(C_{k+1})\le\lambda_{\max}(C_k).
\tag{2a}
\]

Thus no factor is lost in normalized spectral coercivity after the first layer. For fixed positive `theta,delta`, the smallest initial feature-Gram eigenvalue has order `1/L` as depth grows, with constants uniform over the stated three-input class. This order follows from (2) and `lambda_min(Q_L)<=tr(Q_L)/3=q_L` together with (1).

## 1. Variance lower bound

For real z, interpreting ratios continuously at zero,

\[
\frac{\arctan z}{z}
=\int_0^1\frac{dt}{1+t^2z^2}
\ge\frac1{1+z^2/3}.
\]

This is Jensen's inequality for the convex function `x -> (1+x)^(-1)`. Applying the same convexity to weights `1-theta,theta` gives

\[
\frac{\phi_\theta(z)}z
\ge (1-\theta)+\frac{\theta}{1+z^2/3}
\ge\frac1{1+\theta z^2/3}.
\]

All these ratios are nonnegative. Consequently, for `q>0`,

\[
q_{\rm new}\ge q E\!\left[
\frac{G^2}{(1+\theta qG^2/3)^2}\right]
\ge\frac q{(1+\theta q)^2}.
\tag{3}
\]

For the second inequality use the probability measure with density `G^2` relative to the standard Gaussian law: it has total mass one and expectation of `G^2` equal to `E G^4=3`. The function `x -> (1+theta q x/3)^(-2)` is convex, so weighted Jensen applies.

Since `|phi_theta(z)|<=|z|`, one has `0<q_k<=1`. Equation (3) therefore implies

\[
\frac1{q_{k+1}}
\le\frac1{q_k}+2\theta+\theta^2q_k
\le\frac1{q_k}+\frac52\theta.
\]

Iteration proves the left side of (1).

## 2. Variance upper bound

Write

\[
h(z)=1-\frac{\arctan z}z
=\int_0^1\frac{t^2z^2}{1+t^2z^2}\,dt.
\]

Then `0<=h(z)<=1` and

\[
h(z)\ge\frac{z^2}{3(1+z^2)},\qquad
1-[1-\theta h(z)]^2\ge\theta h(z).
\]

It follows, for `0<q<=1`, that

\[
q-q_{\rm new}
\ge\frac{\theta q^2}{3}
 E\frac{G^4}{1+qG^2}
\ge\frac{\theta q^2}{3}
 E\frac{G^4}{1+G^2}
\ge\frac{\theta q^2}{6}.
\tag{4}
\]

Indeed `G^4/(1+G^2)=G^2-1+(1+G^2)^(-1)`, so the middle expectation equals `E(1+G^2)^(-1)>=1/2` by Jensen. Because `theta q/6<1`, (4) gives

\[
\frac1{q_{k+1}}
\ge\frac1{q_k(1-\theta q_k/6)}
\ge\frac1{q_k}+\frac\theta6.
\]

Iteration proves the right side of (1).

## 3. A third-derivative bound on the non-linear Gaussian regression

Let `F(G)=phi_theta(sqrt(q) G)` and let `b_m` be its coefficients in the orthonormal probabilists' Hermite basis `H_m/sqrt(m!)`. The function is odd, so even coefficients vanish. Its linear coefficient is

\[
b_1=\sqrt q\,c(q),\qquad
c(q)=E[\phi_\theta'(\sqrt q G)]\ge1-\theta\ge\frac12.
\]

Put

\[
V(q)=E[F(G)^2]-c(q)^2q=\sum_{m\ge3}b_m^2.
\]

Three Gaussian integrations by parts identify the Hermite coefficient of `F'''` in degree `m-3` as `sqrt(m(m-1)(m-2)) b_m`. The integrations are valid because `F` has at most linear growth and its first three derivatives are bounded. Bessel's inequality, followed by `m(m-1)(m-2)>=6`, therefore gives

\[
6V(q)\le E|F'''(G)|^2
=q^3 E|\phi_\theta'''(\sqrt qG)|^2
\le4\theta^2 q^3.
\tag{5}
\]

The last step uses `atan'''(z)=2(3z^2-1)/(1+z^2)^3`, whose absolute value is at most two. Thus `V(q)<=(2/3)theta^2 q^3`.

The function's linear Gaussian regression coefficient is `c(q)`, so `V(q)` is also its absolute squared error after optimal affine regression. We retain (5) for the nonaffinity estimate below. Normalized spectral propagation admits the stronger exact argument in the next subsection.

### Exact normalized spectral monotonicity

Let Q be the covariance of a centered Gaussian triple with common variance `q>0`, and write `R=Q/q`. Its diagonal entries are one. The Hermite coefficients `b_m` above give

\[
Q_{\rm new}=\sum_{m\text{ odd},\,m\ge1} b_m^2 R^{\circ m},
\qquad q_{\rm new}=\sum_{m\text{ odd},\,m\ge1}b_m^2.
\]

Indeed jointly standard Gaussian variables of correlation rho satisfy

\[
E[H_m(G_i)H_n(G_j)]=\mathbf1_{m=n}m!\rho^m.
\]

This follows by comparing coefficients in the Gaussian generating-function identity
`E[exp(sG_i-s^2/2) exp(tG_j-t^2/2)]=exp(rho s t)`.
The identity includes singular pairs with `rho=1` or `rho=-1`. Hermite partial sums converge in Gaussian `L2`, so Cauchy--Schwarz passes their pairwise products to the limit. Since `sum_m b_m^2=q_new<infinity` and `|R_ij|<=1`, each displayed series converges absolutely entrywise, hence in matrix norm in this fixed dimension. Oddness excludes degree zero and every even degree.

\[
R_{\rm new}=\frac{Q_{\rm new}}{q_{\rm new}}
=\sum_{m\text{ odd},\,m\ge1} w_m R^{\circ m},
\qquad w_m=\frac{b_m^2}{q_{\rm new}}\ge0,
\quad\sum_m w_m=1.
\]

Put `lambda=lambda_min(R)` and `Lambda=lambda_max(R)`. For any integer `m>=1`, the matrix `S=R^(circ(m-1))` is positive semidefinite and has diagonal one; for `m=1` it is the all-ones matrix. Positive semidefiniteness follows from a tensor Gram representation: if `R_ij=<v_i,v_j>`, then `S_ij=<v_i^tensor(m-1),v_j^tensor(m-1)>`.

The entrywise product of two positive semidefinite matrices is positive semidefinite by the same tensor Gram construction. Apply this fact to `R-lambda I` and S, and then to `Lambda I-R` and S. Because `I circ S=I`,

\[
\lambda I\preceq R^{\circ m}\preceq\Lambda I.
\]

Convex combination and the matrix-norm limit give

\[
\lambda_{\min}(R)I\preceq R_{\rm new}
\preceq\lambda_{\max}(R)I.
\tag{6}
\]

This proves (2a), including singular R. It controls the spectral extrema; it does not assert the generally different matrix inequality `R_new>=R`.

## 4. Initial cubic separation and propagation

Represent `Gamma_ij=<u_i,u_j>` with unit vectors. For each i and the other indices j,k let

\[
v_{ij}=\frac{u_i-\Gamma_{ij}u_j}{\sqrt{1-\Gamma_{ij}^2}},
\qquad R_i=u_i\otimes v_{ij}\otimes v_{ik}.
\]

The tensor `R_i` is unit, annihilates `u_j^tensor3` and `u_k^tensor3`, and pairs with `u_i^tensor3` by at least `delta(2-delta)`. Applying Cauchy--Schwarz to `sum_i c_i u_i^tensor3` and summing the three squared inequalities proves

\[
\Gamma^{\circ3}\succeq
\frac{\delta^2(2-\delta)^2}{3}I_3
\succeq\frac{\delta^2}{3}I_3.
\tag{7}
\]

The cubic Hermite coefficient of `atan(G)` has square at least `eta0=1/(108 pi e)`. One direct verification is

\[
b_3(\sigma)=\frac{E[\arctan(\sigma G)(G^3-3G)]}{\sqrt6}
=-\frac{2\sigma^3}{\sqrt6}
 E\frac{G^2}{(1+\sigma^2G^2)^2}.
\]

For `sigma>=1`, substituting `x=sigma G` and restricting to `|x|<=1` gives

\[
|b_3(\sigma)|\ge
\frac2{\sqrt{12\pi}}e^{-1/2}\frac16,
\qquad b_3(\sigma)^2\ge\eta_0.
\]

Only `sigma=1` is required here. The linear part of `phi_theta` has zero cubic coefficient. Orthogonality of Gaussian chaoses gives

\[
Q_1\succeq\theta^2 b_3(1)^2\Gamma^{\circ3}
\succeq\frac{\eta_0\theta^2\delta^2}{3}I_3.
\tag{8}
\]

For completeness, the relevant cross identities are `E[H_3(G_i)H_3(G_j)]=6 Gamma_ij^3` and `E[H_3(G_j)|G_i]=Gamma_ij^3 H_3(G_i)`. Thus subtracting the cubic projection leaves a positive semidefinite residual Gram, also when `Gamma` is singular.

Apply (6) to layers 2 through L. Its normalized spectral monotonicity and (8) give the sharper intermediate bound

\[
Q_L\succeq q_L\lambda_{\min}(Q_1/q_1)I_3
\succeq\frac{q_L}{q_1}
 \frac{\theta^2 b_3(1)^2\delta^2(2-\delta)^2}{3}I_3.
\]

Using `b_3(1)^2>=eta0`, `q_1<=1`, `(2-delta)^2>=1`, and the lower bound for `q_L` in (1) proves (2), including `L=1`. No cumulative exponential factor is needed.

## 5. Precise nonaffinity at initialization and a depth-uniform limitation

There is a useful accompanying estimate. For `0<q<=1`, define the absolute affine-regression residual

\[
\mathcal R_\theta(q)=
\inf_{\alpha,\beta\in\mathbb R}
 E[\phi_\theta(\sqrt qG)-\alpha-\beta\sqrt qG]^2.
\]

Oddness makes the optimal intercept zero, and the linear Gaussian regression above gives `R_theta(q)=V(q)`. Equation (5) is therefore an upper bound. The cubic coefficient and weighted Jensen give a matching lower power:

\[
E\frac{G^2}{(1+qG^2)^2}
\ge\frac1{(1+3q)^2},
\]

\[
\frac{\theta^2 q^3}{384}
\le\frac{2\theta^2q^3}{3(1+3q)^4}
\le\mathcal R_\theta(q)
\le\frac23\theta^2q^3.
\tag{9}
\]

The marginal raw preactivation at hidden layer ell has variance `q_(ell-1)`. Combining (1) and (9) shows its activation regression residual has order `ell^-3` for fixed theta. Therefore this exact unit-sum family cannot have a strictly positive absolute regression gap uniform over every depth, even at time zero. A lower bound uniform in time for each fixed depth is a different claim and is not ruled out.

## 6. Remaining global obligation

These are initialized-network statements. They prove quantitative nonlinear separation at all fixed depths and exact improvement of the normalized spectral extrema with depth. The Gaussian Hermite and entrywise-product argument applies to initialization; trained preactivation laws are not assumed Gaussian. It does not provide a barrier for the trained feature Gram, a finite total residual-clock estimate, uniform source-response bounds along the trained path, or a global nonlinear perturbation argument. The gain-based short-clock proof cannot be reused with gain set to one: it loses its small factor on hidden displacement. A global theorem within the accepted activation constraint must resolve that separate dynamical obstruction.
