# Part G. Uniform geometry, total control time, and all-time nonaffinity

Throughout this part \(F_*=32^L\) is a numerical norm bound, distinct
from the three normalized predictors \(F_i\). All estimates apply
at each separately fixed finite \(L\ge2\). The sufficient conditions
on \(a\) will not depend on \(L\).

## G.1. The initialized Gram loses only a summable amount with depth

First we prove the elementary three-input geometric bound
\[
                  \Gamma+\mathbf1\mathbf1^T\succeq
                           \delta^2 I_3/4.                 \tag{G.1}
\]
For \(v\in\mathbb R^3\), the left quadratic form is
\((\sum v_i)^2+\|\sum v_iu_i\|^2\). If the nonzero \(v_i\) have
one sign, its first term is at least \(\|v\|^2\), which suffices
as \(\delta<1\). Otherwise change the overall sign and permute
to write \(v=(r_1,r_2,-b)\), \(r_1,r_2\ge0\), \(A=r_1+r_2>0\),
\(b>0\). Set
\[
 D=\frac{r_1(1-\Gamma_{13})+r_2(1-\Gamma_{23})}{A}
                         \in[\delta,2].
\]
Projection of \(\sum v_i u_i\) onto the unit vector \(u_3\)
gives the lower bound
\[
                    (A-b)^2+((1-D)A-b)^2.
\]
The matrix of this two-variable quadratic form has determinant
\(D^2\), trace \(D^2-2D+4\le4\), and positive eigenvalues.
Its smaller eigenvalue is at least determinant/trace, hence
\(\delta^2/4\). Finally \(A^2+b^2\ge r_1^2+r_2^2+b^2\).
This proves (G.1), without requiring an invertible \(\Gamma\).

At initialization the raw preactivation tuple at each layer is
centered Gaussian, with a common marginal standard deviation
\(\sigma_\ell\), where \(\sigma_1=1\) and
\(\sigma_{\ell+1}^2=E[\phi(\sigma_\ell G)^2]\).
This follows either directly by the forward-only case of Part F
or by conditioning each fresh Gaussian matrix on its inputs.
For a centered Gaussian tuple \(Z\) with equal marginal variance
\(\sigma^2\), Gaussian integration by parts gives
\[
 m_\sigma=E\phi(\sigma G)=a+eE\psi(\sigma G),\qquad
 \beta_\sigma=E\phi'(\sigma G)=a+eE\psi'(\sigma G).
\]
Its residual coordinates
\(\phi(Z_i)-m_\sigma-\beta_\sigma Z_i\) are orthogonal to
constants and every \(Z_j\). Indeed
\(E[Z_j\mid Z_i]=\operatorname{Cov}(Z_j,Z_i)Z_i/\sigma^2\);
this identity follows by subtracting the correlated linear
Gaussian component, and is valid for singular tuples. Integration
by parts against a Gaussian density proves the remaining
one-coordinate identity; linear growth makes its boundary term
zero. Consequently
\[
 (E[\phi(Z_i)\phi(Z_j)])_{ij}
 \succeq m_\sigma^2\mathbf1\mathbf1^T+
                   \beta_\sigma^2\operatorname{Cov}(Z).
                                                               \tag{G.2}
\]
In particular, \(m_\sigma,\beta_\sigma\ge a-e\ge a/2\), and
\[
 (a/2)^{\ell-1}\le\sigma_\ell\le4a^{\ell-1}.             \tag{G.3}
\]
For the lower bound use the diagonal of the linear projection
in (G.2). For the upper bound, Minkowski and \(|\psi|\le1\)
give \(\sigma_{\ell+1}\le a\sigma_\ell+2a\). Dividing by
\(a^\ell\) and summing the geometric series yields
\(\sigma_\ell/a^{\ell-1}\le1+2\sum_{j=0}^{\ell-2}a^{-j}
\le1+2a/(a-1)<4\) for \(a\ge4\).

A worst-case lower derivative bound at each layer would lose
a fixed factor at every layer. Boundedness of \(\psi\) improves
this estimate. Another integration by parts gives
\[
 |E\psi'(\sigma G)|=
       \frac{|E[G\psi(\sigma G)]|}{\sigma}\le\frac1{\sigma}.
                                                               \tag{G.4}
\]
Define \(d_\ell=a^{-1}(2/a)^{\ell-1}\). Let \(Q_\ell(0)\)
be the Gram of the normalized initialized features \(X_i^\ell\).
The normalized linear projection coefficient at layer \(\ell\)
is \(\beta_{\sigma_\ell}/a\ge1-d_\ell\); the normalized
constant coefficient at layer 1 is at least \(1-d_1\).
Equation (G.2), after dividing the feature Gram by \(a^{2\ell}\),
therefore gives
\[
 Q_1(0)\succeq(1-d_1)^2(\Gamma+\mathbf1\mathbf1^T),\qquad
 Q_\ell(0)\succeq(1-d_\ell)^2Q_{\ell-1}(0)\quad(\ell\ge2).
\]
For numbers in \([0,1]\), induction gives
\(\prod_{j=1}^m(1-d_j)\ge1-\sum_{j=1}^m d_j\). Since
\(\sum_{\ell\ge1}d_\ell=1/(a-2)\le1/2\), (G.1) proves
\[
                  Q_L(0)\succeq
             \tfrac14(\Gamma+\mathbf1\mathbf1^T)
                          \succeq\lambda I_3,\qquad
                  \lambda=\delta^2/16,                    \tag{G.5}
\]
uniformly in all finite depths.

## G.2. Controlled primal estimates and their exact scale

Let \(\tau_R\) be an odd \(C^1\) clip, identity on \([-R,R]\),
with \(|\tau_R(q)|\le\min\{|q|,2R\}\), \(|\tau_R'|\le1\).
For example integrate a smooth even cutoff equal to one on
\([-R,R]\), between zero and one, and zero outside \([-2R,2R]\).
Set \(\epsilon=e/a\) and
\[
 D_{\ell,R}(Y,q)=q+\epsilon\psi'(K_\ell Y)\tau_R(q).
\]
The normalized controlled equations, for \(\|c(s)\|_1\le3\), are
\[
 \begin{split}
 C'&=\sum_i c_iX_i^L,&
 w'&=\sum_i c_i d_i^1u_i,&
 A_\ell'&=\sum_i c_i d_i^\ell\otimes X_i^{\ell-1},\\
 q_i^L&=C,&q_i^\ell&=A_{\ell+1}^*d_i^{\ell+1},&
 d_i^\ell&=D_{\ell,R}(Y_i^\ell,q_i^\ell).
 \end{split}                                                \tag{G.6}
\]
These use the raw metric. The cap acts only on the nonlinear
part of a backward gate. Its derivatives are bounded at fixed
\(R,L,a\), so Part F gives local controlled solutions.

Put \(S=T_0a^{-L}\) and stop at hidden raw displacement
\(\mathfrak D=1\). Then action norms are at most 11 and the
three first projection norms at most 2 (the looser bound 3
also suffices). Induction using
\(|\chi_\ell(Y)-Y|\le2/K_\ell\), \(|\chi_\ell'|\le2\), and
\(|D_{\ell,R}(Y,q)|\le2|q|\), gives
\[
 \|X_i^\ell\|_2\le32^\ell,\quad
 \|C(s)\|_2\le3F_*s,\quad
 \|q_i^\ell(s)\|_2\le32^{L-\ell}\|C(s)\|_2.
                                                               \tag{G.7}
\]
For the first step \(\|X_i^1\|\le3+2\le32\); each later
step is at most \(11\cdot32^{\ell-1}+2\le32^\ell\).
Backward action and gate growth is at most \(22\le32\).
Every hidden block speed is at most \(F_*\|C\|\): at a matrix
block its coefficient is at most
\(6\cdot32^{L-\ell}32^{\ell-1}=(3/16)F_*\), and the bottom
satisfies the same bound. There are \(L\) hidden blocks, so
\[
             \mathfrak D(s)\le3\sqrt L F_*^2s^2.           \tag{G.8}
\]
The factor 3 is deliberately larger than the integrated factor
\(3/2\). Positive Euler meshes obey the same estimate because
\(\sum_jh_js_j\le s_k^2/2\). Even the first proposed overshooting
node is bounded using only earlier stopped states, so the strict
bound \(\mathfrak D(S)<1/4\) proved below rules out overshooting.
This establishes (G.7)--(G.8) on the entire controlled interval,
independently of source estimates.

Here are the forward perturbation estimates relative to the
same initialized actions and roots. Write
\(\Delta Y_\ell=Y_\ell-Y_\ell(0)\) and similarly for \(X\).
The bottom norm is at most \(\mathfrak D\). At later layers
use
\[
 \Delta Y_\ell=(A_\ell-A_{\ell,0})X_{\ell-1}
                               +A_{\ell,0}\Delta X_{\ell-1}.
 \]
Thus
\(\|\Delta Y_\ell\|\le32^{\ell-1}\mathfrak D+
20\|\Delta Y_{\ell-1}\|\). Summing this geometric recurrence
gives
\[
 \|\Delta Y_\ell\|\le3\cdot32^{\ell-1}\mathfrak D,\qquad
 \|\Delta X_\ell\|\le32^\ell\mathfrak D.                  \tag{G.9}
\]
Indeed the first coefficient is at most
\(\sum_{j\ge0}(20/32)^j=8/3<3\), and \(6<32\).
The bottom also satisfies both inequalities.
In raw preactivation coordinates this implies, for all
samples and \(\ell\le L\),
\[
 \|z_i^\ell(s)-z_i^\ell(0)\|_2
 \le a^{L-1}F_*\mathfrak D(S)
 \le d_L:=\frac{3\sqrt L T_0^2}{a}
                         \left(\frac{32768}{a}\right)^L.
                                                               \tag{G.10}
\]
The harmless factor \(3\cdot32^{\ell-1}\) in (G.9) is at
most \(32^L\); this explains the first inequality.

The top Gram perturbation has every entry bounded by
\(2F_*^2\mathfrak D\). Its operator norm is bounded by the
maximum absolute row sum, hence
\[
 \|Q_L(s)-Q_L(0)\|_{\rm op}
 \le6F_*^2\mathfrak D(S)
 \le18\sqrt L\left(\frac{2^{20}}{a^2}\right)^LT_0^2.
                                                               \tag{G.11}
\]
Let \(J_h:\mathcal P_h\to\mathbb R^3\) be the true normalized
hidden predictor differential and \(U_{h,R}:\mathbb R^3\to
\mathcal P_h\) the normalized capped hidden direction map.
Their individual sample/block factors are bounded by
\(F_*\|C\|\) using the same backward induction, also for the
true gate. Taking the finite sum of squared factor norms gives
\[
 \|J_h\|,\|U_{h,R}\|\le\sqrt{3L}F_*\|C\|,\qquad
 \|J_hU_{h,R}\|\le27L F_*^4 S^2.                         \tag{G.12}
\]
There is no assertion that \(J_hU_{h,R}\) is symmetric.

All required strict inequalities follow from the single
depth-independent condition \(a\ge10^{12}(1+T_0)\).
For completeness, if \(0\le q\le1/4\) then
\(Lq^L\le2q^2\) for \(L\ge2\): the consecutive ratio is
\((L+1)q/L\le3/8<1\). Also \(\sqrt L\le L\).
Use \(q=2^{20}/a^2\). The largest of (G.11) and (G.12)
is at most
\[
                  54\,2^{40}T_0^2/a^4<\lambda/4.         \tag{G.13}
\]
Indeed \(a\ge10^{12}T_0\) and \(T_0=12/\lambda\) make
this at most \( (54\,2^{40}/(144\cdot10^{48}))\lambda^2
<4.13\cdot10^{-37}\lambda^2<\lambda/4\).
Use \(q=1024/a^2\) in (G.8) to obtain
\(\mathfrak D(S)\le6\cdot2^{20}T_0^2/a^4<1/4\).
Consequently
\[
 Q_L(s)\succeq3\lambda I_3/4,\qquad
                \|J_hU_{h,R}\|<\lambda/4.                \tag{G.14}
\]
The same controlled bounds hold for every cap.

## G.3. Capped physical paths and their finite total control time

The physical capped equations are
\[
             \dot\theta=-a^L\sum_i r_i\,G_{i,R},
                                                               \tag{G.15}
\]
where \(G_{i,R}\) has the normalized blocks in (G.6) with
unit control \(c_i=1\). Its readout block is \(X_i^L\).
Define the accumulated control time
\[
                    v(t)=a^L\int_0^t\|r(s)\|_1\,ds.
                                                               \tag{G.16}
\]
On portions where \(r\ne0\), reparametrization by \(v\)
turns (G.15) into (G.6) with \(c=-r/\|r\|_1\), of norm one.
If \(r=0\), the whole capped field is zero; fixed-cap uniqueness
makes its continuation stationary. Equivalently the integral
controlled estimates apply directly with the measure
\(dv=a^L\|r(t)\|_1dt\), so no inverse at zero is required.

While \(v\le S\), the scalar chain rule in Part F gives the
exact residual equation
\[
                  \dot r=-a^{2L}(Q_L+J_hU_{h,R})r.
                                                               \tag{G.17}
\]
Its readout term is the true positive Gram even under a cap.
Using the absolute operator bound for its possibly nonsymmetric
hidden term, (G.14) implies
\[
 \frac d{dt}\|r\|_2^2\le-\lambda a^{2L}\|r\|_2^2,\qquad
 \|r(t)\|_2\le\sqrt3 e^{-\lambda a^{2L}t/2}.             \tag{G.18}
\]
Here \(r(0)=-y\), since the population readout is zero.
Therefore
\[
 v(t)\le a^L\sqrt3\int_0^\infty
                  \sqrt3e^{-\lambda a^{2L}s/2}\,ds
        =\frac6{\lambda a^L}=\frac S2.                    \tag{G.19}
\]
This rules out a first exit at \(v=S\). A finite physical
endpoint has bounded raw speed by (G.7) and (G.15);
its state is strongly Cauchy there, and fixed-cap local
existence continues it. Thus all capped population paths
are global, with (G.7)--(G.19) independent of cap and horizon.

To apply Part S's Euler source estimates to these paths without
an implicit limit assumption, fix a cap and bounded deterministic
control on \([0,S]\). For a step-function control, fixed-cap
Euler convergence follows separately on its finitely many
constant intervals from Part F. For a general measurable bounded
control, choose bounded step controls converging in \(L^1\);
they exist by approximating each integrable coordinate by
simple interval step functions, and projecting onto the closed
\(\ell^1\) ball if needed. The integral difference of the fields
is bounded by \(C\|c-\bar c\|_{L^1}\), in addition to a
fixed-cap Lipschitz state term. Gronwall gives uniform strong
convergence of controlled paths. For each fixed time, an
almost-sure subsequence and Fatou pass Part S's moment bounds.
This argument does not sample an arbitrary measurable control
at Euler nodes. In particular it applies to the deterministic
control extracted from any capped population physical path.
The uniform result of Part S is
\[
 \sup_{R,t\ge0,\ell,i}\|q_{R,i}^\ell(t)\|_p
                            \le M_*\sqrt p,\qquad p\ge2, \tag{G.20}
\]
where \(M_*<\infty\) may depend on fixed \(L,a,\delta\) but
not on cap or physical time. The total interval is always
the same \([0,S]\). These are the sole nonclassical inputs
to cap removal, and Part S proves them explicitly.

Part V now applies: its one-cap-factor comparison uses
(G.20) only on the capped reference, constructs a strong
uncut limit, and proves uniqueness, restart and all actual
finite GF/GD and observation limits. Its fixed-cap
approximations depend only on the already established capped
paths and controlled moments, so the order is not circular.
The bounds (G.14), (G.18), (G.19) pass by strong convergence
to the uncut path and prove (M.15).

## G.4. Persistent nonaffinity for one activation at every depth

For a square-integrable real variable \(X\), define
\[
 \mathcal R_\psi(X)=\inf_{b,c\in\mathbb R}
                             E[\psi(X)-b-cX]^2.
\]
The following stability estimate avoids any variance lower
bound:
\[
 \left|\sqrt{\mathcal R_\psi(X)}
           -\sqrt{\mathcal R_\psi(\widetilde X)}\right|
                            \le2\|X-\widetilde X\|_2.     \tag{G.21}
\]
To prove it, if \(\operatorname{Var}X>0\), the optimal slope is
\(c_X=\operatorname{Cov}(X,\psi(X))/\operatorname{Var}X\).
For an independent copy \(X'\), the covariance numerator is
\(\tfrac12 E[(X-X')(\psi(X)-\psi(X'))]\), while the denominator
is \(\tfrac12E[(X-X')^2]\). Since \(\psi\) is 1-Lipschitz,
\(|c_X|\le1\). If \(X\) is constant choose \(c_X=0\) and
the matching intercept. Test the optimal affine fit for \(X\)
as a competitor for \(\widetilde X\), on the given coupling:
the difference of its residuals is at most
 \(2|X-\widetilde X|\). The triangle inequality gives one
direction of (G.21); interchanging the variables gives the
other. The best fit exists because the span of \(1,X\) is
finite dimensional and closed; the displayed covariance
calculation also constructs it.

There exists an \(r_\psi\) in (M.3). Otherwise \(\psi\) is
affine on every \([-r,r]\) for integer \(r\), since this
finite-dimensional affine subspace is closed in its interval
\(L^2\). Continuity makes each such equality pointwise.
Overlapping intervals force the same two affine coefficients,
so \(\psi\) is affine on \(\mathbb R\), and boundedness would
make it constant, a contradiction. The interval residual is
explicitly
\[
 J_\psi=\int_{-r}^{r}\psi(x)^2dx
       -\frac{(\int_{-r}^{r}\psi(x)dx)^2}{2r}
       -\frac{3(\int_{-r}^{r}x\psi(x)dx)^2}{2r^3}.
                                                               \tag{G.22}
\]
For \(\sigma\ge1\), its Gaussian density on \([-r,r]\) is
at least \(e^{-r^2/2}/(\sigma\sqrt{2\pi})\). Restricting
the regression integral to this interval proves
\[
                      \mathcal R_\psi(\sigma G)
                                      \ge c_\psi/\sigma.
                                                               \tag{G.23}
\]
In particular \(c_\psi\le\mathcal R_\psi(G)\le1\).
By (G.3), at every layer of a depth \(L\) network,
\[
         \mathcal R_\psi(z_i^\ell(0))
                       \ge\eta_L:=c_\psi/(4a^{L-1}).     \tag{G.24}
\]

The raw displacement in (G.10) is smaller than
\(\sqrt{\eta_L}/4\) simultaneously for every \(L\ge2\).
Here is the explicit check. The ratio is at most
\[
 \frac{24\sqrt L T_0^2}{\sqrt{c_\psi}a^{3/2}}
                    \left(\frac{32768}{\sqrt a}\right)^L.
\]
The first bound in (M.4) ensures
\(q=32768/\sqrt a\le1/2\). For \(L\ge2\),
\(\sqrt L q^L\le2q^2\): the ratio of consecutive terms is
at most \(\sqrt{3/2}/2<1\) and the initial coefficient is
\(\sqrt2\le2\). Thus the displayed ratio is at most
\[
 \frac{3\cdot2^{34}T_0^2}{\sqrt{c_\psi}a^{5/2}}
                         \le\frac34<1                  \tag{G.25}
\]
by the second bound in (M.4). Apply (G.21) to the common-space
coupling of a trained preactivation and its own initialization.
Equations (G.10), (G.24)--(G.25) give
\(\mathcal R_\psi(z_i^\ell(t))\ge\eta_L/4\).
Adding the affine part of \(\phi\) to a regression target has
no effect on its residual, and multiplying its nonaffine part
by \(e\) multiplies the residual by \(e^2\). Hence
\[
 \mathcal R_\phi(z_i^\ell(t))
   =e^2\mathcal R_\psi(z_i^\ell(t))
                       \ge e^2c_\psi/(16a^{L-1}),
\]
as claimed. This holds first for every capped path, then for
the uncut path by (G.21) and strong cap convergence.

Parts F, S, G and V prove statements 1, 2 and the regression
portion of statement 3 of Theorem M.1. Part N proves the
remaining motion and kernel assertions with only \(a>e>0\),
which the selected constants satisfy.
