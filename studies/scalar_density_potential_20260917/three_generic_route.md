# Independent three-input route: stationary gap and escape obstruction

This is an internal bounded proof-route report, not promoted theory. Its scientific inputs are only the supervisor's scalar-flow assignment, the exact coefficient target in `docs/observable_p1.md`, and `docs/global_nonlinear.md` C.4.7.10.C.1/C.3. No other study artifacts or routes were read. The research and rigorous-math skills were applied. There are no simulations.

## Contract and notation

Let `u_i=x_i/sqrt(2)` be three unit vectors, `p_i>0`, `sum p_i=1`, and `y_i in {-1,1}`. Both populations and the exact initialized marks are those in the assignment. Write `B_1=(nu+eta)^(-1/2)`, `B_2=(tau+eta)^(-1/2)`, so `|b_1|<=B_1`, `|b|<=B_2`. Set

\[
a_i=E_1[b_1\tanh(w\cdot u_i)],\quad s_i=Ma_i,
\quad H_i(b)=\tanh(bs_i),\quad F(s)=E_2[c\tanh(bs)],
\quad d_i=F'(s_i),\quad r_i=F(s_i)-y_i.
\]

The state metric is `L2(lambda_1;R2) x L2(lambda_2) x R`. Time is physical time and the loss is unhalved: `L=sum p_i r_i^2`. Global existence on every finite horizon and the exact energy identity are available from the assigned established source. The requested all-time exponential theorem is not assumed.

## 1. Uniform positivity of the lower derivative Gram on increment balls

Suppose the directions are pairwise nonparallel: `u_i != +/- u_j` for `i!=j`. For any measurable lower state `w(g)=g+xi(g)` with `|xi(g)|<=R` almost everywhere, define

\[
L_{ij}(w)=(u_i\cdot u_j)
 E_1[b_1^2\operatorname{sech}^2(w\cdot u_i)
                       \operatorname{sech}^2(w\cdot u_j)].
\]

**Proposition 1.** There is an explicit `ell_R>0`, depending only on the three directions, `R`, and the fixed mark normalization, such that `L(w)>=ell_R I_3` for every such measurable state.

**Proof.** Choose unit `v_j` perpendicular to `u_j`, and put

\[
\delta=\min_{j\ne k}|v_j\cdot u_k|>0,
\qquad q_R=\operatorname{sech}^2(R+3),
\qquad
T_R=\frac{R+3+\frac12\log(16/q_R)}{\delta}.
\]

Let `sigma_j` equal the sign of the first coordinate of `v_j`, with value `1` if that coordinate is zero, and set `z_j=T_R v_j+2 sigma_j e_1`. On the Euclidean open unit ball `A_j=B(z_j,1)`,

\[
|g_1|\ge1,\qquad |w\cdot u_j|\le R+3,
\qquad |w\cdot u_k|\ge T_R\delta-R-3\quad(k\ne j).
\]

Consequently, using `sech^2(x)<=4 exp(-2|x|)`, the `j`-th gate is at least `q_R`, and every other gate is at most `q_R/4`. For any `alpha in R3`, take `j` with `|alpha_j|=max_k|alpha_k|`. The reverse triangle inequality gives throughout `A_j`, outside the null set defining the increment bound,

\[
\left|\sum_k\alpha_k\operatorname{sech}^2(w\cdot u_k)u_k\right|
\ge |\alpha_j|q_R-\sum_{k\ne j}|\alpha_k|q_R/4
\ge |\alpha_j|q_R/2.
\]

The standard two-dimensional Gaussian density on `A_j` is at least `(2pi)^(-1) exp(-(T_R+3)^2/2)`. Since the ball area is `pi` and `|b_1|>=tanh(1)/sqrt(nu+eta)` there,

\[
\begin{aligned}
\alpha^T L(w)\alpha
&=E_1\left[b_1^2\left|\sum_k\alpha_k
                  \operatorname{sech}^2(w\cdot u_k)u_k\right|^2\right]\\
&\ge \frac{\tanh^2(1)}{\nu+\eta}\,
       \frac{q_R^2}{24}\exp(-(T_R+3)^2/2)\,|\alpha|^2.
\end{aligned}
\]

This proves the claim with the displayed constant. No injectivity, continuity, density, or support property of the transported `w` law was assumed. The argument works directly in the fixed Gaussian root law. The constant deteriorates strongly with `R`; it is not an all-time bound. ∎

The differential of the map `w -> (a_1,a_2,a_3)` has adjoint

\[
\alpha\longmapsto b_1\sum_i\alpha_i
                    \operatorname{sech}^2(w\cdot u_i)u_i,
\]

whose squared norm is `alpha^T L alpha`. Proposition 1 therefore also proves that this differential is onto `R3`. In particular the three lower feature coordinates are locally independent, even when some current scalar values coincide.

## 2. Readout independence and the exact kernel nullspace

The law of `b=tanh(sqrt(nu)Z)/sqrt(tau+eta)` has a strictly positive smooth density on `(-B_2,B_2)`. If `sigma_1,...,sigma_q` are distinct positive numbers, `q<=3`, then the functions `tanh(b sigma_j)` are linearly independent in `L2(lambda_2)`. Indeed an almost-everywhere linear identity is an identity on this open interval by continuity. Its first, third, and fifth derivatives at zero give the equations

\[
\sum_j\gamma_j\sigma_j^{2k+1}=0,\qquad k=0,...,q-1.
\]

The nonzero Taylor coefficients used are `1,-1/3,2/15`; the resulting matrix is an invertible diagonal matrix times the Vandermonde matrix in `sigma_j^2`. This proves independence without a total-positivity claim.

For `M!=0`, the tangent kernel on the training inputs is

\[
K_{ij}=E_2[H_iH_j]+d_i a_i d_j a_j+M^2d_id_jL_{ij}.
\]

Each summand is positive semidefinite. Proposition 1 gives the following exact nullspace criterion:

\[
v\in\ker K
\quad\Longleftrightarrow\quad
v_i d_i=0\text{ for every }i,
\quad \sum_i v_iH_i=0\text{ in }L^2(\lambda_2).
\]

The middle-matrix term then vanishes automatically. The last identity can be grouped by nonzero `|s_i|`: in each group `C`, `sum_{i in C}v_i sign(s_i)=0`, while zero `s_i` contribute no constraint. Thus distinct nonzero magnitudes already make `K_c` positive definite. Colliding magnitudes can be resolved by the lower contribution when the relevant `d_i` are nonzero.

At a stationary state with `M!=0` and bounded increments, the lower gradient equation and Proposition 1 imply `p_i r_i d_i=0` separately for each `i`. This statement does not by itself exclude stationary positive loss.

## 3. A discrete positive-loss gap for all finite stationary states

This proposition does not require pairwise nonparallel inputs or Proposition 1.

**Proposition 2.** Every finite stationary state has either zero loss or loss at least `p_min=min_i p_i`. More precisely, a state stationary only with respect to the readout already has the following loss formula. Let `C_0={i:s_i=0}`. Partition the remaining indices into groups `C` with the same positive `|s_i|`, and write

\[
P_C=\sum_{i\in C}p_i,\qquad
Y_C=\sum_{i\in C}p_i\varepsilon_i y_i,
\qquad \varepsilon_i=\operatorname{sign}(s_i).
\]

Then

\[
\mathcal L=\sum_{i\in C_0}p_i+
             \sum_C\left(P_C-\frac{Y_C^2}{P_C}\right).
\tag{1}
\]

**Proof.** Readout stationarity says `sum_i p_i r_i H_i=0`. Independence of the distinct positive-magnitude functions gives, group by group, `sum_{i in C}p_i epsilon_i r_i=0`. If `sigma_C=|s_i|` and `F_C=F(sigma_C)`, oddness gives `f_i=epsilon_i F_C`, so `P_C F_C=Y_C`. Substitution into the loss gives (1). A zero feature has `f_i=0`, hence cost `p_i`. In a nonzero group, let `P_+` and `P_-` be the total masses with `epsilon_i y_i=+1` and `-1`. Its loss is

\[
P_C-\frac{Y_C^2}{P_C}
=\frac{4P_+P_-}{P_++P_-}.
\]

This vanishes if either class is empty. Otherwise both masses are at least `p_min`, and `4P_+P_-/(P_++P_-)>=2 min(P_+,P_-)>=2p_min`. Therefore any positive total loss is at least `p_min`. This includes `M=0`, when every feature is zero and the loss equals `1`. ∎

Only finitely many signed partitions of three indices occur, so the possible readout-stationary losses form a finite set determined by the weights. The bound `p_min` is a convenient universal lower bound, not a claim that every displayed value is attainable by a full stationary state.

If at some time `T` one has `L(T)<p_min`, loss monotonicity therefore rules out convergence to any finite positive-loss stationary state. It also yields explicit pointwise barriers. Set `epsilon=sqrt(L(T)/p_min)<1`. For `t>=T`,

\[
y_i f_i(t)\ge1-\epsilon>0.
\tag{2}
\]

Hence `M(t)!=0`, `a_i(t)!=0`, and each `s_i` retains its sign after `T`. Opposite values of `sign(s_i)y_i` cannot share an exact magnitude. These facts rule out certain finite degeneracies. They do not yet rule out approach to degeneracy at infinity, because the readout norm may grow.

## 4. Below the gap, bounded readout subsequences suffice for zero loss

There is a stronger reduction than requiring full-state compactness.

**Proposition 3.** Suppose `L(T)<p_min` at some finite time. If

\[
\liminf_{t\to\infty}\|c(t)\|_{L^2(\lambda_2)}<\infty,
\]

then `L(t)->0`. Equivalently, if `0<L_infinity<p_min`, then necessarily `||c(t)||_2 -> infinity`. No bound on `w`, `M`, or their increments is assumed.

**Proof.** Compactify the scalar parameter to `[-infinity,infinity]` and define

\[
H_s(b)=\tanh(bs)\quad(s\in\mathbb R),\qquad
H_{+\infty}(b)=\operatorname{sign}(b),\qquad
H_{-\infty}(b)=-\operatorname{sign}(b).
\]

This map is continuous into `L2(lambda_2)`, including at infinity, by pointwise convergence outside `b=0` and the uniform bound `|H_s|<=1`. The measure of `b=0` is zero. Distinct finite positive-magnitude features, together with `sign(b)` if present, are linearly independent. For a putative identity, the limit `b downarrow 0` first forces the coefficient of `sign(b)` to vanish; the finite-parameter independence proved above handles the remaining terms.

Assume a sequence `t_n->infinity` has bounded `||c(t_n)||_2`. The energy identity gives

\[
e_n=\int_{t_n}^{t_n+1}\|\dot c(t)\|_2^2dt\longrightarrow0.
\]

Choose `t_n' in [t_n,t_n+1]` with `||dot c(t_n')||_2^2 <= 2e_n` (the harmless factor `2` avoids any attainment issue). Cauchy--Schwarz gives `||c(t_n')-c(t_n)||_2<=sqrt(e_n)`, so this new sequence also has bounded readout norm. Pass to a subsequence on which each `s_i(t_n')` converges in the compactified scalar line, and each residual converges in `R`; residuals are bounded because `p_i r_i^2<=L(0)=1`.

Let the limiting features be `H_i^*` and residuals `r_i^*`. The readout gradient converges in `L2` to `-2 sum_i p_i r_i^* H_i^*`, so this sum is zero. Bounded readout norm also preserves all limiting feature relations in the outputs: if `H_i^*=0`, then `f_i(t_n')->0`; if `H_i^*=epsilon H_j^*`, `epsilon in {-1,1}`, then

\[
|f_i(t_n')-\varepsilon f_j(t_n')|
\le \|c(t_n')\|_2\,
       \|H_i(t_n')-\varepsilon H_j(t_n')\|_2\longrightarrow0.
\]

Consequently the signed-partition derivation of (1) applies to the limiting outputs, with the infinite-magnitude group allowed. It gives `L_infinity=0` or `L_infinity>=p_min`. Monotonicity and `L(T)<p_min` exclude the latter. This proves the proposition. ∎

This is a convergence reduction, not an exponential rate or full-state convergence theorem. A bound on the readout norm along the prescribed trajectory remains unproved. The elementary estimates do not supply it: the exact identity

\[
\frac{d}{dt}\|c\|_2^2
=-4\sum_i p_i r_i f_i
=4\bigl(\langle y,f\rangle_p-\|f\|_p^2\bigr)
\le1
\]

only gives `||c(t)||_2^2<=t`. The last inequality follows by completing the square, since `||y||_p^2=1`. The energy identity gives finite squared speed but not finite path length.

## 5. An explicit failure of a below-gap compactness inference

The following construction shows that low loss and a vanishing full gradient do not alone bound the state. It is **not** a counterexample trajectory from the canonical initialization.

Take the three pairwise nonparallel directions of angles `0`, `pi/6`, and `pi/3`, all with label `+1`, and arbitrary positive weights. These have three distinct initialized scalar feature values. Let

\[
S(z)=\frac{1+\tanh z}{2},\qquad
\theta_q(g_2)=-\frac{5\pi}{12}S(g_2^2-q),\qquad
V_q(g_2)=(\cos\theta_q(g_2),\sin\theta_q(g_2)).
\]

Fix sufficiently large finite `q`. For `R>=1` define the smooth lower state

\[
w_R(g)=g+R\tanh(g_1)V_q(g_2).
\tag{3}
\]

It has bounded increment `||w_R-g||_infinity<=R`, obeys the canonical full-root oddness `w_R(-g)=-w_R(g)`, and fixes every root with `g_1=0`. For almost every `g`, each `w_R(g) dot u_i` tends to a signed infinity, because the finitely many root levels at which `V_q dot u_i=0`, and the level `g_1=0`, have zero Gaussian measure. Dominated convergence gives

\[
a_{i,R}\longrightarrow a_i^\infty,\qquad
(a_1^\infty,a_2^\infty,a_3^\infty)
=\kappa(1,1-2\varepsilon_2,1-2\varepsilon_3),
\]

where

\[
\kappa=E_1|b_1|>0,\quad
\varepsilon_2=\Pr\{G^2>q+\log2\},\quad
\varepsilon_3=\Pr\{G^2>q+\tfrac12\log(2/3)\}.
\]

Indeed `V_q dot u_1` is always positive; `V_q dot u_2` changes sign at `S=4/5`, and `V_q dot u_3` at `S=2/5`. Independence of `g_1` and `g_2` factors the expectation. For large finite `q`, `0<epsilon_2<epsilon_3<1/2`, so all three limiting scalar feature values are positive and distinct.

Set

\[
\beta_2=E_2 b^2=\frac\tau{\tau+\eta}>0,\qquad
\alpha_R=\frac{\sum_i p_i a_{i,R}}{\sum_i p_i a_{i,R}^2},
\qquad M_R=R^{-1},\qquad
c_R(b)=\frac{R\alpha_R}{\beta_2}\,b.
\tag{4}
\]

The denominator in `alpha_R` is bounded away from zero for sufficiently large `R`, and `alpha_R` tends to a positive finite value. The upper state is odd, smooth, and bounded for each finite `R`. Bounded marks and the Taylor estimates `tanh z=z+O(z^3)` and `sech^2 z=1+O(z^2)` give, uniformly in `i`,

\[
f_{i,R}=\alpha_R a_{i,R}+O(R^{-2}),\qquad
d_{i,R}=R\alpha_R+O(R^{-1}).
\tag{5}
\]

Hence the losses tend to

\[
\ell_q
=1-\frac{(\sum_i p_i a_i^\infty)^2}
          {\sum_i p_i(a_i^\infty)^2}>0.
\tag{6}
\]

Strict positivity follows from strict weighted Cauchy--Schwarz, since the three limiting feature values differ. As `q->infinity`, they all tend to `kappa`, so `ell_q->0`. Thus `q` can be fixed so that `0<ell_q<p_min`.

Evaluate the **actual scalar gradient vector field** at these states. The defining least-squares choice of `alpha_R` gives the exact cancellation

\[
\sum_i p_i(\alpha_R a_{i,R}-1)a_{i,R}=0.
\tag{7}
\]

Equations (5)--(7) imply `sum_i p_i r_{i,R}a_{i,R}=O(R^{-2})`. Expanding the actual readout gradient therefore gives `||dot c||_2=O(R^{-3})`; the middle gradient is `dot M=O(R^{-1})`. Finally

\[
\dot w(g)
=-2b_1(g)\sum_i p_i r_{i,R}
 [\alpha_R+O(R^{-2})]
 \operatorname{sech}^2(w_R(g)\cdot u_i)u_i.
\]

All coefficients in this expression are uniformly bounded, and every gate tends to zero almost everywhere. Dominated convergence yields `||dot w||_2->0`. Thus

\[
\mathcal L(w_R,c_R,M_R)\longrightarrow\ell_q\in(0,p_{\min}),
\qquad \|\nabla\mathcal L(w_R,c_R,M_R)\|\longrightarrow0.
\tag{8}
\]

Nevertheless `||w_R-g||_2=R sqrt(nu)`, `||c_R||_2=R alpha_R/sqrt(beta_2)`, and `M_R->0`. The three `|M_R a_{i,R}|` are distinct and nonzero for sufficiently large `R`, so even strict positive definiteness of every individual readout Gram does not repair this failure. Its smallest eigenvalue degenerates.

Consequences must be kept separate:

* This disproves a general Palais--Smale assertion below the finite stationary gap in the stated scalar state class, including the canonical parity constraints.
* It disproves any uniform positive Polyak--Lojasiewicz constant on that entire low-loss state set.
* It does **not** prove that the canonical gradient trajectory escapes or approaches these states. The construction is a family of states, not a solution curve. A special dynamical invariant or monotonicity theorem could still exclude this escape route.

## 6. A finite local certificate does give exponential loss and state convergence

The target can be closed once a sufficiently good regular finite state is reached. This requires no assumed all-time kernel bound.

Let `z=(w,c,M)` in the fixed Hilbert state metric, and let `J(z)` be the derivative of the weighted output vector `(sqrt(p_i) f_i)_{i=1}^3`. Suppose at a finite time `T` the smallest eigenvalue of `J(z_T)J(z_T)^*` is `lambda_T>0`. On a Hilbert ball of radius `rho` around `z_T`, the output derivative is Lipschitz with some finite constant `A`: `||J(z)-J(z_T)||<=A ||z-z_T||`. Such an `A` can be bounded from `B_1,B_2,||c_T||_2+rho,|M_T|+rho`; bounded first and second derivatives of tanh control all the required products. No bound on the fixed Gaussian root is needed.

For an explicit choice, put `C=||c_T||_2+rho`, `m=|M_T|+rho`, and `S_0=B_1 sqrt(1+m^2)`. One may take

\[
A=2B_2S_0+2B_2^2CS_0^2+2B_1B_2C(1+m).
\]

Indeed `||Da_i||<=B_1`, `||D^2a_i||<=2B_1`, `||Ds_i||<=S_0`, and the bilinear variation of `Ds_i` is bounded by `2B_1(1+m)`. Differentiating `f_i=<c,H_{s_i}>` gives two readout/feature cross terms, bounded together by `2B_2S_0`, one term using `|tanh''|<=2`, bounded by `2B_2^2CS_0^2`, and the second-variation term for `s_i`, bounded by `2B_1B_2C(1+m)`. These bounds can first be verified for bounded directions and integrated along line segments, then extended by density to the Hilbert norm. The probability weights sum to one, so the same bound controls the stacked weighted derivative.

If

\[
A\rho\le\frac{\sqrt{\lambda_T}}2,
\qquad \frac{2\sqrt{\mathcal L(T)}}{\sqrt{\lambda_T}}<\rho,
\tag{9}
\]

then the trajectory stays in this ball and

\[
\mathcal L(t)\le\mathcal L(T)e^{-\lambda_T(t-T)},
\qquad
\|z(t)-z_\infty\|
\le\frac{2\sqrt{\mathcal L(T)}}{\sqrt{\lambda_T}}
       e^{-\lambda_T(t-T)/2}.
\tag{10}
\]

To verify the bootstrap, inside the ball the smallest singular value of `J` is at least `sqrt(lambda_T)/2`, by the triangle inequality for `||J^*v||`. Thus `||grad L||>=sqrt(lambda_T) sqrt(L)` and `L'<=-lambda_T L`. Before any first exit, the path length is bounded by

\[
\int_T^t\|\dot z\|ds
=\int_T^t\frac{-\dot{\mathcal L}}{\|\nabla\mathcal L\|}ds
\le\frac{2}{\sqrt{\lambda_T}}
       (\sqrt{\mathcal L(T)}-\sqrt{\mathcal L(t)})<\rho.
\]

This excludes first exit. The same estimate from any later time proves finite length and the state convergence bound. If the loss reaches zero at finite time, the gradient vanishes and the conclusion remains valid. The limiting state interpolates by continuity of the output map.

This is a concrete finite-state criterion. What is unproved is that a prescribed genuinely three-constraint trajectory from the canonical initialization reaches (9). Initial kernel positivity alone does not imply this small-loss certificate.

The subsequent scoped audit in `three_generic_audit.md` supplies a direct
first-derivative difference proof of the same constant `A`. On the Hilbert
space, the second-variation expressions above refer to bounded directional
variations; only `C^{1,1}` is needed or asserted for the local certificate.
Twice Frechet differentiability on the whole `L2` space is not an additional
premise. This clarification preserves the frozen route's bounds and conclusions.

## 7. Non-vacuity of a three-constraint initialization

For the explicit angles `0,pi/6,pi/3`, the initialized scalar values are distinct and positive. To verify this, write

\[
Q(\rho)=E[\tanh(G_1)\tanh(\rho G_1+\sqrt{1-\rho^2}G_2)].
\]

For `|rho|<1`, Gaussian integration by parts in the two independent roots gives

\[
Q'(\rho)=E[\operatorname{sech}^2(G_1)
\operatorname{sech}^2(\rho G_1+\sqrt{1-\rho^2}G_2)]>0.
\]

Specifically, differentiating in `rho` gives a multiplier `G_1-rho G_2/sqrt(1-rho^2)`; the terms containing the derivative of the second gate cancel under the two integrations by parts, leaving the displayed positive expectation. Bounded gates and Gaussian moments justify these operations. Since `Q(0)=0` and continuity also holds at `rho=1`, `a_i(0)=Q(cos(theta_i))/sqrt(nu+eta)` are distinct positive numbers. The prescribed `D` is positive, so their initialized upper features are independent by Section 2, and the three-dimensional readout Gram is strictly positive definite.

Thus these three constraints are independent even in the frozen readout system, irrespective of whether the labels are all equal or, for example, `(+1,-1,+1)`. The gap and compactification arguments cover both choices. The escape example uses all positive labels but has distinct scalar representations; it does not replace a third constraint by a duplicate representation.

## Current strongest conclusion and decisive gap

The stationary-loss gap is proved, and convergence below that gap reduces to a bound on the readout norm alone. A finite local certificate yields exponential loss decay and full-state convergence. However, no unconditional theorem establishing either readout boundedness or attainment of that certificate for a genuinely independent three-input family has been proved here. The explicit small-gradient sequences show why finite stationary classification plus energy dissipation cannot fill this gap by themselves. The next decisive obligation is a trajectory-specific non-escape estimate, or a quantitative canonical-initialization argument reaching the finite certificate (9).
