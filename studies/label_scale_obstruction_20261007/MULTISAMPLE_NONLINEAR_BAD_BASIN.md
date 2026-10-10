# Non-fitting basins with many correlated inputs and two nonlinear hidden layers

2026-10-10. Continuation of the bad-basin construction in
`TWO_LAYER_PERSISTENCE.md`. This note gives a self-contained extension, not
a wide-Gaussian failure theorem or an incompressibility result. Both hidden
activations are now nonlinear, both hidden representations move on the
certified perturbed trajectories, and the inputs need not be orthogonal or
linearly independent.

## 1. Statement and model

Let `d>=2`, `m>=2`, and `n>=m`. Fix sphere inputs
`x_1,...,x_m` in `R^d`, of norm `sqrt(d)`, with
`x_j != x_k` and `x_j != -x_k` for `j != k`. They may be arbitrarily
correlated; in particular, `m` may exceed `d`. Fix any `a>0` and labels

\[
y=a(m+1,-1,\ldots,-1).
\tag{1}
\]

Use two width-`n` hidden layers, with all parameters trainable:

\[
\begin{aligned}
h_j^{(1)}&=\tanh(Ax_j/\sqrt d),\\
z_j^{(2)}&=Wh_j^{(1)},\qquad
h_j^{(2)}=(3+\cos z_j^{(2)})/2,\\
f_j&=w^\top h_j^{(2)}/n,\qquad
r=f-y,\qquad \mathcal L=\|r\|_2^2/m.
\end{aligned}
\tag{2}
\]

Here `A=W^(1)` is `n by d`, `W=W^(2)` is `n by n`, and
`w=W^(3)` is the stored readout in the maintained notation contract.
Activations act coordinatewise. Initialization has independent
`A_ik ~ N(0,1)`, independent `W_ik ~ N(0,1/n)`, and exactly `w(0)=0`.
Gradient flow has block mobilities `(n,1,n)` and physical time `t`.
Write `H^(ell)=[h_1^(ell),...,h_m^(ell)]` for the finite sample-feature
matrix, not a population random variable.

**Theorem.** For each such fixed dataset, width, and `a`, there is a
nonempty open set of hidden initial parameters `(A(0),W(0))` with all of
the following properties, on the exact zero-readout slice:

1. Both initial empirical feature Grams
   `H^(ell)(0)^T H^(ell)(0)/n` are positive definite.
2. The loss decreases strictly at every finite time. Both hidden weight
   blocks and both hidden sample representations move: they have nonzero
   second time derivatives at zero. Their first derivatives at zero vanish
   because the readout starts at zero.
3. Parameters converge to finite limits, but the predictions do not fit:

   \[
   f(\infty)=a(2,1,\ldots,1),\qquad
   r(\infty)=a(-(m-1),2,\ldots,2),
   \tag{3}
   \]

   \[
   \mathcal L(0)=a^2(m+3),\qquad
   \mathcal L(\infty)=\frac{a^2(m-1)(m+3)}m>0.
   \tag{4}
   \]

4. The first-layer empirical Gram stays uniformly positive definite for
   all `t>=0`. Its lower bound depends on the constructed neighborhood,
   dataset, and width; it is not a typical-Gaussian uniform estimate.
5. At the endpoint, the nonzero residual is in the nullspace of both the
   top-feature Gram and the full parameter-tangent Gram.

The initialization law assigns this open set strictly positive probability
at each fixed width. Both Gaussian population feature Grams are positive
definite for these inputs and activations. No lower bound on the basin
probability as `n` tends to infinity is claimed. The empirical initial gap
in this basin need not approximate the population gap.

The network can interpolate the same labels: full column rank of the
initial top-feature matrix already permits an exactly fitting signed
readout with the hidden parameters held fixed. Thus (3) is an optimization
failure, not insufficient expressive capacity.

The proof first constructs an exactly solvable rank-one reference path,
then proves a full-dimensional attracting neighborhood of its endpoint.
Small perturbations inside the pulled-back basin supply full initial rank
and actual feature motion. The rank-one reference alone is not the theorem.

## 2. Equations, regularity, and finite-time existence

For the locally defined backward vectors
`delta_j=w odot phi_2'(z_j^(2))`, where
`phi_2(z)=(3+cos z)/2`, the equations are

\[
\begin{aligned}
\dot w&=-\frac2m\sum_j r_jh_j^{(2)},\\
\dot W&=-\frac2{mn}\sum_j r_j\delta_jh_j^{(1)\top},\\
\dot A&=-\frac2m\sum_jr_j
 \bigl[(1-(h_j^{(1)})^2)\odot W^\top\delta_j\bigr]
 x_j^\top/\sqrt d.
\end{aligned}
\tag{5}
\]

The square in the last line is componentwise. Both activations are in the
bounded strip-analytic subclass of the original activation class. For
example, `tanh` is holomorphic on `|Im z|<pi/2`, and bounded by one on
`|Im z|<=pi/4`; this follows from

\[
|\tanh(x+iy)|^2
=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}.
\]

Cauchy's formula on disks of radius `pi/8` gives uniform derivative
bounds on `|Im z|<=pi/8`. Cosine and its derivatives are bounded on each
fixed horizontal strip as well. Neither hidden activation is affine.

For parameters `theta=(A,W,w)` define, only for the energy argument,

\[
\|\theta\|_{M^{-1}}^2
=\|A\|_F^2/n+\|W\|_F^2+\|w\|_2^2/n,
\qquad M=\operatorname{diag}(n,1,n).
\]

Equation (5) is `dot theta=-M grad L`, and hence

\[
\dot{\mathcal L}=-\|\dot\theta\|_{M^{-1}}^2,
\qquad
\|\theta(t)-\theta(s)\|_{M^{-1}}
\le\sqrt{\mathcal L(0)}\sqrt{t-s}\quad(0\le s\le t).
\tag{6}
\]

The second assertion follows by integrating the first and applying
Cauchy--Schwarz. At a hypothetical finite maximal time it makes the
parameters Cauchy. The vector field is smooth at their finite limit, so
local existence there extends the trajectory, a contradiction. All
solutions in this note therefore exist for every finite time, and smooth
finite-time continuous dependence on the initial parameters applies.

## 3. Correlated data still allow full first-layer rank

We prove that the vectors

\[
\bigl(\tanh(g^\top x_j/\sqrt d)\bigr)_{j=1}^m,
\qquad g\in\mathbb R^d,
\tag{7}
\]

span `R^m`. Choose `b` outside the finitely many hyperplanes perpendicular
to `x_j` and `x_j +/- x_k`. Each is a proper hyperplane under the data
assumptions. Thus the numbers `p_j=b^T x_j/sqrt(d)` are nonzero and have
distinct absolute values.

If a linear relation with coefficients `c_j` annihilates (7), restrict to
`g=t b`. Letting `t` tend to positive infinity gives
`sum_j c_j sign(p_j)=0`. Order the absolute values increasingly. The
identity

\[
\tanh(tp_j)-\operatorname{sign}(p_j)
=\frac{-2\operatorname{sign}(p_j)}{e^{2|p_j|t}+1}
\]

shows that multiplying the subtracted relation by `exp(2|p_1|t)` and
letting `t` tend to infinity gives `c_1=0`. Remove that term and repeat
with the next smallest absolute value. Every coefficient is zero.
This proves the span assertion without any linear independence assumption
on the input vectors themselves.

Choose `m` rows `g^T` giving independent vectors (7), place them in `A_*`,
and pad to `n` rows if necessary. The finite matrix

\[
U_*:=\tanh(A_*[x_1,\ldots,x_m]/\sqrt d)
\]

has full column rank. This notation is used only for the constructed
first-layer feature matrix and nearby matrices `U(A)` in the proof.

This also verifies the population-gap qualification. Define

\[
Q^{(1)}=\mathbb E\bigl[h(g)h(g)^\top\bigr],\quad
h(g)=(\tanh(g^\top x_j/\sqrt d))_{j=1}^m,
\quad g\sim N(0,I_d).
\]

For every nonzero `c`, (7) makes `c^T h(g)` a continuous function that is
nonzero somewhere, hence on a nonempty open set. Gaussian density is
positive there, so `c^T Q^(1)c>0`. A Gaussian `Z` with covariance
`Q^(1)` consequently has positive density on all of `R^m`. Coordinatewise
`phi_2` maps this space onto `[1,2]^m`. A nonzero linear functional cannot
vanish on the interior of this cube; continuity and positive Gaussian
density therefore imply

\[
Q^{(2)}:=\mathbb E[\phi_2(Z)\phi_2(Z)^\top]\succ0,
\qquad Z\sim N(0,Q^{(1)}).
\tag{8}
\]

All expectations are finite because the activations are bounded. These
are the canonical Gaussian population feature Grams, not the specially
chosen empirical initial Grams.

## 4. The exact learning path and its non-fitting endpoint

Write `v=(2,1,...,1)` and choose a matrix `Z_*` with every row equal to
`(0,pi,...,pi)`. Since `U_*` has full column rank, set

\[
W_*=Z_*(U_*^\top U_*)^{-1}U_*^\top.
\tag{9}
\]

Then `W_* U_*=Z_*`, every top feature row is `v`, and every top activation
derivative vanishes. Starting at `(A_*,W_*,0)`, equation (5) leaves both
hidden blocks fixed. The readouts remain equal to a scalar `s(t)`.
Since `||v||^2=m+3` and `v^T y=a(m+3)`,

\[
\dot s=\frac{2(m+3)}m(a-s),\quad s(0)=0,
\qquad
w(t)=a(1-e^{-2(m+3)t/m})\mathbf1.
\tag{10}
\]

In particular, learning starts immediately and approaches (3). Its exact
loss is

\[
\mathcal L(t)
=\frac{a^2(m+3)}m\left(m-1+e^{-4(m+3)t/m}\right).
\tag{11}
\]

Let `L_*` denote the value in (4) at infinity. The endpoint is a local
minimum for the full network, not only for the reference path. Whenever
all readouts are positive, `1<=phi_2<=2` gives `f_1<=2f_j` for every
`j>=2`. With `f_*=a v` and `r_*=f_*-y`,

\[
r_*^\top(f-f_*)
=a\sum_{j=2}^m(2f_j-f_1)\ge0,
\]

and therefore

\[
\mathcal L-\mathcal L_*
=\frac{\|f-f_*\|^2+2r_*^\top(f-f_*)}{m}\ge0.
\tag{12}
\]

The network is not constrained to positive readouts globally. This local
cone obstruction does not rule out the fitting signed readouts described
in Section 1.

## 5. A full-dimensional attracting neighborhood

To turn the reference path into an open basin, choose `m` row indices `I`
such that the square matrix `U_*(I,:)` is invertible. In a neighborhood
where `U(A)(I,:)` remains invertible, the exact identity

\[
W_{:I}=
\bigl(Z-W_{:I^c}U(A)_{I^c:}\bigr)U(A)_{I:}^{-1}
\tag{13}
\]

shows that `(Z,A,W_:I^c,w)` are smooth local coordinates on the original
parameter space. There is no need for `W_*` to be invertible, or for the
input vectors to be linearly independent. If `n=m`, the complementary
blocks in (13) are empty.

Near `(A_*,W_*,a 1)`, write locally

\[
Z=Z_*+\zeta,\qquad
e=\mathbf1^\top w/n-a,\qquad
u=w-(a+e)\mathbf1,\quad\mathbf1^\top u=0.
\]

The transverse coordinates are `(zeta,e)`; `A,W_:I^c,u` are complementary
coordinates. The set `zeta=0,e=0` consists of equilibria of loss `L_*`.
Restrict the complementary coordinates to a small compact neighborhood
where `a+u_i>=a/2` for every `i`. Taylor expansion gives

\[
\begin{aligned}
\mathcal L-\mathcal L_*
={}&\frac{m+3}{m}e^2
 +\frac{a(m-1)}{2mn}\sum_i(a+u_i)\zeta_{i1}^2\\
&+\frac{a}{mn}\sum_i(a+u_i)\sum_{j=2}^m\zeta_{ij}^2
 +O\bigl((\|\zeta\|_F+|e|)^3\bigr).
\end{aligned}
\tag{14}
\]

Here and below local constants depend on this fixed dataset, width, label
scale, and compact coordinate neighborhood; no width-uniform rate is
claimed. To verify (14), the output expansions are

\[
\begin{aligned}
f_1&=2(a+e)-\frac1{4n}\sum_iw_i\zeta_{i1}^2
       +O(\|\zeta\|_F^4),\\
f_j&=(a+e)+\frac1{4n}\sum_iw_i\zeta_{ij}^2
       +O(\|\zeta\|_F^4),\quad j\ge2.
\end{aligned}
\]

Substitute these into the squared loss. The term linear in `e` vanishes
because `v^T r_*=0`. The second-order feature terms come from
`2 r_*^T(f-f_*)/m`, using `r_*1=-(m-1)a` and `r_*j=2a` for `j>=2`.
Replacing `w_i` by `a+u_i` changes only terms of order three.

The transverse Hessian at `zeta=0,e=0` is diagonal with entries

\[
\frac{2(m+3)}m,\qquad
\frac{a(m-1)(a+u_i)}{mn},\qquad
\frac{2a(a+u_i)}{mn}
\tag{15}
\]

for `e`, each `zeta_i1`, and each `zeta_ij` with `j>=2`, respectively.
They are uniformly positive on that compact complementary neighborhood.
By continuity the transverse Hessian remains uniformly positive on a
sufficiently small full coordinate box.

For this paragraph let `E=L-L_*` and let `xi=(zeta,e)` in Euclidean
coordinates. Taylor's integral formula at fixed complementary coordinates
and smooth coordinate norm equivalence give positive local constants
`c_1,c_2,c_3` with

\[
c_1\|\xi\|^2\le E\le c_2\|\xi\|^2,
\qquad
\|\nabla\mathcal L\|_M\ge c_3\sqrt E.
\tag{16}
\]

For the last inequality, integrate the transverse Hessian along the line
from `0` to `xi`. Its average is uniformly positive definite, so the
transverse derivative has norm bounded below by a positive multiple of
`||xi||`. The physical parameter gradient controls that derivative because
the coordinate map and its inverse have bounded derivatives on the box,
and the mobility is fixed and positive definite.

While the solution remains in this box, (6) and (16) give
`E'<=-c_3^2 E`. Moreover,

\[
\int_{t_0}^t\|\dot\theta\|_{M^{-1}}\,ds
\le\frac{2}{c_3}\left(\sqrt{E(t_0)}-\sqrt{E(t)}\right).
\tag{17}
\]

Indeed, where `E>0`, the speed equals `-E'/speed`, which is at most
`-E'/(c_3 sqrt(E))`; integrate. If `E=0`, (16) puts the state on the
equilibrium manifold, so it stays there and no division is needed.

Choose a smaller neighborhood of the reference endpoint separated from
the outer boundary, and with `2 sqrt(E)/c_3` less than that separation in
the parameter metric. A first-exit argument using (17) traps every such
trajectory. Exponential decay of `E`, (17), and completeness of finite
dimensional parameter space prove convergence to a finite point with
`zeta=0,e=0`. The resulting attracting neighborhood is genuinely open in
all parameter directions, including the complementary ones.

The exact path (10) enters it at some finite time `T`. Finite-time
continuous dependence pulls it back to a nonempty open neighborhood of
`(A_*,W_*)` on the exact slice `w(0)=0`. All those trajectories have the
same limiting predictions (3), though their limiting hidden factors and
individual readouts may differ.

We can also retain a first-layer gap throughout. Write
`sigma_*=sigma_min(U_*)>0` just in this argument. Choose the outer trapping
box so that `||U(A)-U_*||_op<sigma_*/2` throughout. Shrink the pulled-back
initial neighborhood so that the same inequality holds on `[0,T]`, using
continuous dependence and the fact that the reference `A_*` is constant.
For every trajectory in this neighborhood, all times then satisfy

\[
\frac{H^{(1)}(t)^\top H^{(1)}(t)}n
\succeq\frac{\sigma_*^2}{4n}I_m.
\tag{18}
\]

This is a local-basin conclusion, not the linear-layer balance invariant
from the earlier note, and not a Gaussian-typical lower bound.

## 6. Full initial rank and actual motion in both hidden representations

Keep `A=A_*`. Perturb `Z_*` only in entries `(j,j)`, `2<=j<=m`, by
replacing `pi` with `pi+epsilon_j`, with nonzero sufficiently small
`epsilon_j`. Realize the resulting matrix by (9) with the perturbed `Z`
in place of `Z_*`. The change in `W` can be arbitrarily small.
Set locally `delta_j=(1-cos epsilon_j)/2>0`. The first `m` rows of the
top feature matrix are

\[
v^\top,\quad v^\top+\delta_2 e_2^\top,\quad\ldots,\quad
v^\top+\delta_m e_m^\top,
\]

where `e_j` in this display is the `j`th sample-coordinate vector.
Subtracting the first row from each later row gives determinant

\[
2\prod_{j=2}^m\delta_j\ne0.
\tag{19}
\]

Thus the initial top feature Gram is positive definite, and the start
remains in the basin when the perturbation is small enough.

It remains to exclude a merely frozen-feature interpretation. The
following derivatives are evaluated at initialization. Put locally

\[
X=[x_1,\ldots,x_m]/\sqrt d,\quad U=\tanh(AX),\quad
Z=WU,\quad H=\phi_2(Z),\quad D=1-U^2,
\qquad R_{:j}=y_j[(Hy)\odot\phi_2'(Z_{:j})].
\]

Zero readout and (5) give

\[
\dot w=\frac2mHy,\qquad \dot A=\dot W=0,\qquad
\ddot W=\frac4{m^2n}RU^\top,\qquad
\ddot A=\frac4{m^2}(D\odot W^\top R)X^\top.
\tag{20}
\]

First perturb only `(2,2)` by a small positive `epsilon_2`. Then
`R=c e_2 e_2^T`, with the first `e_2` indexing neurons and the second
indexing samples, and

\[
c=y_2(Hy)_2\phi_2'(Z_{22})
=-\frac{a^2}{2}(m+3-\delta_2)\sin\epsilon_2\ne0.
\]

Let `D_2=diag(1-U_:2^2)` and `q_2=x_2/sqrt(d)` just for this
calculation. Its diagonal entries are strictly positive, `||q_2||=1`,
and `W_2:` is nonzero because `W_2: U=Z_2:` is nonzero. Equation (20)
therefore yields

\[
\ddot A=\frac{4c}{m^2}D_2W_{2:}^\top q_2^\top\ne0,
\qquad
\ddot h_2^{(1)}=\frac{4c}{m^2}D_2^2W_{2:}^\top\ne0.
\tag{21}
\]

Also `ddot W=(4c/(m^2 n)) e_2 U_:2^T` is nonzero since `U` has full
column rank. Differentiating `Z=WU` gives

\[
\ddot Z_{22}
=\frac{4c}{m^2}\left(
\frac{\|U_{:2}\|^2}{n}+\|D_2W_{2:}^\top\|^2\right)\ne0,
\qquad
\ddot H_{22}=\phi_2'(Z_{22})\ddot Z_{22}\ne0.
\tag{22}
\]

The last equality uses `dot Z(0)=0`. In fact this last second derivative
is negative: the perturbed feature initially moves back toward its
minimum. No independence or orthogonality of `X` was used.

For `m>2`, now choose the other nonzero `epsilon_j` sufficiently smaller
so that these strict nonzero derivative statements persist by continuity.
Equation (19) simultaneously supplies rank `m`. Nonzero acceleration,
positive initial feature gaps, and membership in the pulled-back basin
are open conditions. A small ambient hidden-parameter neighborhood of
this perturbed point therefore retains all of them. This proves the
open-set part of the theorem, with actual motion in both hidden layers.
It does not assert a width-uniform lower bound on feature-motion amplitude.

## 7. Strict loss decrease, endpoint cancellation, and Gaussian probability

Every row of `Hy` at the reference is `a(m+3)>0`; the same remains true
at sufficiently close starts. Thus the initial gradient is nonzero and

\[
\dot{\mathcal L}(0)=-\frac4{m^2n}\|Hy\|^2<0.
\tag{23}
\]

A nonstationary trajectory of this smooth autonomous vector field cannot
reach an equilibrium at a finite time: local uniqueness applied backward
from such a point would identify it with the constant solution, and
continuation would make it stationary from the start. Consequently the
gradient never vanishes at a finite time, and (6) gives strict loss
decrease for every finite `t`. Stalling here means convergence to a
non-fitting equilibrium as `t` tends to infinity, not a sudden finite-time
stop.

At every basin endpoint, `H^(2)=1 v^T`, and `phi_2'(z_j^(2))=0` for all
neurons and samples. The latter makes every hidden-parameter derivative
of the predictions vanish. For the full tangent Gram, defined by

\[
K_{jk}=\nabla_\theta f_j^\top M\nabla_\theta f_k,
\]

only the readout block remains, giving

\[
K(\infty)=\frac{H^{(2)}(\infty)^\top H^{(2)}(\infty)}n
=vv^\top,\qquad
v^\top r(\infty)=0.
\tag{24}
\]

Thus it is the actual learned residual, not an arbitrarily chosen test
direction, that ends in a vanishing tangent direction. The preceding
feature Gram remains positive by (18).

For an additional normalization check, (5) implies
`dot r=-2Kr/m`, and therefore

\[
\int_0^\infty\frac{r(t)^\top K(t)r(t)}{\|r(t)\|^2}\,dt
=\frac m4\log\frac{m}{m-1}<\infty.
\tag{25}
\]

Indeed `-d log L/dt=(4/m)r^T K r/||r||^2`, and (4) gives the loss ratio.
There is no division by zero because the limiting loss is positive.

The joint Gaussian density of all hidden coordinates is strictly positive
at every finite `(A,W)`. The nonempty open neighborhood from Section 6
therefore has positive probability, for each fixed `n,m,d,a` and dataset.
No lower estimate uniform in any of these parameters was used or proved.
In particular, positive finite-width probability does not contradict a
sufficiently-large-width high-probability fitting theorem.

The construction works for every positive `a`; the label RMS is
`Y=a sqrt(m+3)`. If desired, any prescribed fixed `Y>0` is obtained by
`a=Y/sqrt(m+3)`. This is not evidence of a critical large-label threshold.
It also establishes no trajectory-compression lower bound.

## 8. A three-sample circle example

Take `d=2`, any `n>=3`, and

\[
x_j=\sqrt2(\cos\theta_j,\sin\theta_j),\qquad
(\theta_1,\theta_2,\theta_3)=(0,\pi/6,\pi/3).
\]

Their normalized pairwise inner products are `sqrt(3)/2,1/2,sqrt(3)/2`:
every pair is nonorthogonal. The three inputs are necessarily linearly
dependent in `R^2`, but Section 3 still supplies full-rank nonlinear first
features. Choose

\[
y=(4a,-a,-a).
\]

The open basin above starts at zero prediction, learns with moving hidden
features, and converges to

\[
f(\infty)=(2a,a,a),\qquad r(\infty)=(-2a,2a,2a),
\qquad \mathcal L(0)=6a^2,\quad \mathcal L(\infty)=4a^2.
\]

For the unperturbed reference path alone, the exact formulas simplify to

\[
f(t)=a(1-e^{-4t})(2,1,1),\qquad
\mathcal L(t)=4a^2+2a^2e^{-8t}.
\]

These finite-time formulas are not claimed for the full-rank perturbed
starts; those starts share the limiting predictions and loss, and the
strict loss decrease and hidden-motion properties proved above.

## 9. Provenance and check boundary

The lead constructed and assembled this extension using the canonical
model, the previous within-study basin argument, and prompt-scoped
calculations by the existing `feature_adaptation_route` and
`two_layer_persistence` agents. These agents were reused; their checks are
not independent blind attempts. All nonlinear-rank, local-stability,
probability, and motion arguments needed for this result are written out
here. No theorem from another study or an external neural-network paper
is a dependency. No simulation or numerical training experiment is used.

This result concerns one explicit activation pair and label family, and
finite-width positive-probability bad basins. It does not settle the
arbitrary-label wide-Gaussian fitting or compression question.
