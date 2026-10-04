# A finite-width bottleneck compression benchmark

2026-10-03. Scoped theoretical route. This file proves direct compression
of a fixed-second-width architecture and gives an exact equal-width lift
with structured initialization. It makes no claim for the canonical iid
Gaussian ensemble. No experiments or Git operations were performed.

## 1. Frozen benchmark derivation

Let the first width be n and the second width be a fixed k>=2. Put
v_a=x_a/sqrt(d), with |v_a|<=1, and use tanh at both hidden layers:

\[
 h_{i,a}=\tanh(a_i^\top v_a),\quad
 z_a=\frac1n\sum_i b_i h_{i,a}\in\mathbb R^k,\quad
 g_a=\tanh z_a,\quad f_a=w^\top g_a/k.
\]

Here a_i is in R^d, b_i in R^k, and w in R^k. The physical second
matrix has columns b_i/n. For the loss m^{-1} sum_a(f_a-y_a)^2, take
mobilities n for a_i, nk for b_i, and k for w. Equivalently the physical
second matrix has mobility k/n. Writing r_a=f_a-y_a and
delta_a=w odot sech^2(z_a), the exact equations are

\[
 \dot a_i=-\frac2{mk}\sum_a r_a\operatorname{sech}^2(a_i^\top v_a)
                  (b_i^\top\delta_a)v_a,\quad
 \dot b_i=-\frac2m\sum_a r_a\delta_a h_{i,a},\quad
 \dot w=-\frac2m\sum_a r_ag_a.
\]

They train every edge and both hidden layers. However, fixed k and compact
order-one b initialization are material departures from the canonical
equal-width Gaussian mixer. They must remain explicit.

The exact residual equation is dot r=-(2/m)Kr, with

\[
 K_{ab}=\frac{g_a^\top g_b}{k}
 +\frac{\delta_a^\top\delta_b}{k}\mathbb E_n[h_a h_b]
 +\frac{v_a^\top v_b}{k^2}\mathbb E_n\left[
 \operatorname{sech}^2(a^\top v_a)\operatorname{sech}^2(a^\top v_b)
 (b^\top\delta_a)(b^\top\delta_b)\right].
\]

All three summands are Gram matrices. Suppose |a_i(0)|<=A,
|b_i(0)|<=B, w(0)=0, and the initial first summand has eigenvalue at
least kappa>0. The following bootstrap has constants independent of n.
Define D(t)=max_i max(|a_i(t)-a_i(0)|,|b_i(t)-b_i(0)|), with ordinary
Euclidean norms in the two blocks. While D is at most one, changing the
features changes the first summand in operator norm by at most
2m(1+B)D (enlarging this constant is harmless). Set
D_0=min(1,kappa/[4m(1+B)]). On D<=D_0, K>=kappa I/2, so

\[
 |r(t)|\le Y e^{-\kappa t/m},\qquad
 \int_0^\infty |r(t)|dt\le mY/\kappa,\qquad Y=|y|.
\]

The update formulas imply

\[
 |w(t)|\le C_wY,\quad C_w=2\sqrt{km}/\kappa,
 \qquad D(t)\le C_DY^2,
\]

where one may take
C_D=(2 sqrt(m)/kappa) C_w max(1,(B+1)/k).
Choose the fixed label threshold so C_wY<=1/2 and C_DY^2<=D_0/2.
The strict inequalities close the bootstrap by continuity, prove global
existence, exponential fitting, finite total variation and endpoints.
The proof applies verbatim to arbitrary positive empirical weights.

A concrete correlated two-input example has d=k=m=2,
v_1=(1,0), v_2=(1,1)/sqrt(2). Begin with the equiprobable seed atoms
(a,b)=((1,0),(2,1)) and ((0,1),(1,2)). The second-layer feature matrix is

\[
 G_* =\begin{pmatrix}u&v\\h&h\end{pmatrix},\quad
 u=\tanh(\tanh1),\ v=\tanh(\tfrac12\tanh1),\quad
 h=\tanh(\tfrac32\tanh(1/\sqrt2)).
\]

Its determinant h(u-v)>0. Let sigma_* be its smallest singular value.
Replace each atom by a continuous distribution within distance eta in
each a,b block, where eta=sigma_*/64. This gives genuinely diverse
particles and nonzero dense edges. If the empirical cluster proportion
p satisfies |p-1/2|<=alpha=sigma_*/64, then each z coordinate differs
from its ideal value by at most 3eta+2alpha. Consequently
||G-G_*||_op<=2(3eta+2alpha)<sigma_*/2, giving initial gap
kappa=sigma_*^2/8. For iid cluster labels this event has probability at
least 1-2 exp(-2n alpha^2), by the elementary bounded Bernoulli tail bound.

For labels (epsilon,0), put gamma=g_1 odot sech^2(z_1)>0 at zero.
Since m=2, dot w(0)=epsilon g_1. The hidden velocities initially vanish,
but their exact accelerations satisfy

\[
 \ddot a_i(0)=\frac{\epsilon^2}{k}
  \operatorname{sech}^2(a_i^\top v_1)(b_i^\top\gamma)v_1,
 \qquad \ddot b_i(0)=\epsilon^2\gamma h_{i,1},
\]

\[
 \ddot h_{i,1}(0)=\frac{\epsilon^2}{k}
  \operatorname{sech}^4(a_i^\top v_1)b_i^\top\gamma>0,
\]

\[
 \ddot z_{j,1}(0)=\epsilon^2\left[
  \gamma_j\mathbb E_n h_1^2+\frac1k\mathbb E_n
  b_j\operatorname{sech}^4(a^\top v_1)(b^\top\gamma)\right]>0.
\]

The positivity is uniform over the compact seed neighborhoods and the
stated cluster event. Also ddot g_{j,1}=sech^2(z_{j,1})ddot z_{j,1}>0.
On a fixed short interval, the compact state bounds and the equations
give |w|<=C epsilon, |r|+|dot r|+|ddot r|<=C epsilon, and uniformly
bounded derivatives of the fixed normalized averages; differentiating
the hidden updates twice therefore bounds their third derivatives by
C epsilon^2, independently of n. Taylor's formula then gives
positive feature displacement of order epsilon^2 at a fixed positive
time, with constants independent of n. Both nonlinear layers therefore
learn at a width-independent scale for a fixed small nonzero label.
The first-layer law contains a neighborhood of preactivation one, and
the second-layer preactivations are positive and bounded away from zero;
tanh's second derivative is nonzero there. At the exact atomic example
the second preactivations across the training samples include the three
distinct positive numbers tanh(1)/2, tanh(1), and
(3/2)tanh(1/sqrt(2)). Strict concavity of tanh on the positive axis means
its values at these three points cannot agree with an affine function.
The strict noncollinearity persists after sufficiently small neighborhood
and cluster-proportion perturbations, reducing eta and alpha if needed.

For a fixed realized trajectory, the seed-to-particle flow extends
holomorphically to a fixed complex neighborhood of the compact initial
seed support, uniformly for all physical times and at its endpoint.
Indeed the particle vector field is analytic as long as the imaginary
first preactivation remains below pi/2. On a smaller tube its spatial
derivative is bounded by C |r(t)| |w(t)|; its integral is O(Y^2).
A complex perturbation of size rho therefore remains at most
rho exp(CY^2). Choose rho so this stays below a fixed half-strip margin.
Picard iteration gives holomorphic dependence on the seed, and the
integrable bound gives uniform convergence at the endpoint. Thus every
source b_j(t) tanh(a(t)^T v), uniformly for |v|<=1, has a fixed analytic
seed neighborhood and bound. This statement uses the realized common
controls only in its proof; it is not an initialization algorithm.

The initial version of this section froze the benchmark setup before the
direct comparison below was completed. The architecture differs from the
canonical target as explicitly stated above.

## 2. Direct comparison to the realized empirical network

This argument compares two finite empirical systems, with no population
replacement. Let mu=n^{-1} sum_i delta_{theta_i} be the actual finite
initialization, theta_i=(a_i(0),b_i(0)). Let nu be any positive probability
measure supported on selected original theta_i. The reduced flow uses
exactly the equations in Section 1 with every empirical average replaced
by its nu-weighted average. Its readout, residual and second preactivations
are its own. No full-width state is consulted after initialization.

For each model, extend its particle flow to every real seed theta in a
fixed box containing all initial seeds, using that model's common
controls r,w,z. These off-support particles are proof devices, not stored
state. Their b motion obeys |dot b|<=C|r||w|, so the previous estimates
bound it by CY^2 on the entire box; their a motion is then bounded by
CY^2 as well. Thus the analytic seed-tube argument applies to the entire
box, with constants independent of either empirical measure.

For the original mu-flow define the following seed functions at time t:

\[
 F_{j,v}(t,\theta)=b_j(t,\theta)\tanh(a(t,\theta)^\top v),
 \quad |v|\le1,
\]

\[
 P_{ab}(t,\theta)=\tanh(a(t,\theta)^\top v_a)
                   \tanh(a(t,\theta)^\top v_b),
\]

\[
 Q_{abjl}(t,\theta)=b_j(t,\theta)b_l(t,\theta)
  \operatorname{sech}^2(a(t,\theta)^\top v_a)
  \operatorname{sech}^2(a(t,\theta)^\top v_b).
\]

Suppose the absolute mu-minus-nu integration error of every displayed
function is at most epsilon, uniformly in t>=0 and in the displayed
indices and v. This condition will be obtained from initial polynomial
moment matching below; it does not require observing the trained path.
Take epsilon below a fixed threshold so the reduced initial readout Gram
keeps a fixed positive gap. Both systems then satisfy the same small-label
fitting bounds, after lowering the allowed fixed Y once if necessary.

Write E(t)=|r_nu(t)-r_mu(t)|, W(t)=|w_nu(t)-w_mu(t)|, and let D(t)
be the supremum over the seed box of the sum of their a and b differences.
For every training or passive v, subtracting its forward integrals gives

\[
 |z_\nu(t,v)-z_\mu(t,v)|\le C[D(t)+\epsilon].                 \tag{26}
\]

All constants in this section depend only on the fixed box, input list,
k,m and initial Gram gap. Since both readouts are bounded by CY, the
three explicit terms of K in Section 1 give

\[
 \|K_\nu(t)-K_\mu(t)\|_{\rm op}
   \le C[D(t)+Y W(t)+\epsilon].                            \tag{27}
\]

For the readout term this is the Lipschitz bound on g. For the second
term use the P-source defect, |delta|<=CY, and
|delta_nu-delta_mu|<=W+CY(D+epsilon). For the third term use Q and the
same delta bound. All integrations have positive mass one, so none of
these estimates divides by the smallest cubature weight.

Let R(t)=|r_mu(t)|<=Y exp(-gamma t), where gamma>0 is the common
fitting rate. Residual subtraction and the positive reduced Gram yield

\[
 D^+E\le-\gamma E+CR[D+YW+\epsilon],\qquad E(0)=0.           \tag{28}
\]

At E=0 the inequality follows by first differentiating
sqrt(|r_nu-r_mu|^2+zeta^2), then taking zeta down to zero. In particular,
for every terminal time T,

\[
 \int_0^T E(t)dt\le CY[D_T+YW_T+\epsilon],                  \tag{29}
\]

where D_T and W_T are the corresponding suprema up to T. Directly
subtracting the w equation, with the residual difference put on the
nu-feature, gives

\[
 W_T\le C\int_0^T E+C\int_0^T R(D+\epsilon)
       \le CYD_T+CY^2W_T+CY\epsilon.                      \tag{30}
\]

Similarly the a,b updates are linear in the residual and in delta. Their
differences, using their bounded a,b and tanh derivatives, give

\[
 D_T\le CY\int_0^T E+C\int_0^T RW
                       +CY\int_0^T R(D+\epsilon)
       \le CYW_T+CY^2D_T+CY^2\epsilon.                    \tag{31}
\]

The constants in (29)--(31) are fixed before Y is selected. Choose Y
small enough to absorb the CY^2 terms. Substituting (30) into (31) and
absorbing once more yields, uniformly in T,

\[
 W_T\le CY\epsilon,\qquad D_T\le CY^2\epsilon.              \tag{32}
\]

Equations (26) and (32) now give the same-physical-time, whole-input bound

\[
 \sup_{t\ge0}\sup_{|v|\le1}|f_\nu(t,v)-f_\mu(t,v)|
     \le CY\epsilon.                                    \tag{33}
\]

Each model has finite total parameter variation, so its endpoint exists;
continuity includes both fitted endpoints in (33). This proof never
identifies the models' residuals or clocks, or selects weights using a
trained path.

## 3. Initial polynomial cubature supplies the required source defect

Let D=d+k be the fixed seed dimension. The analytic argument supplies
rho>0 and M<infinity such that every F,P,Q above extends holomorphically
to the complex maximum-coordinate-distance rho-neighborhood of the real
seed box and is bounded by M,
uniformly for all t and |v|<=1. To justify the tube uniformly, compare a
complex particle to its nearest real initial seed under the same real
controls. On a fixed complex tube, the derivative of its particle vector
field is bounded by C|r||w|. The integrated derivative is <=CY^2. A
perturbation of maximum coordinate size rho has Euclidean size at most
sqrt(D) rho and remains at most sqrt(D) rho exp(CY^2); choose rho
smaller than the fixed allowed Euclidean tube width times
exp(-CY^2)/sqrt(D). The tanh
arguments then stay strictly inside their pole-free strip. Picard
iteration and the uniform integrable speed prove holomorphic dependence
for every finite t and locally uniform convergence at the endpoint.

Partition the seed box into a fixed finite number L of cells, each inside
a coordinate polydisc centered at c with radii rho, and with
|theta_j-c_j|<=rho/(4D) on the cell. Cauchy's coefficient estimate bounds
the coefficient of multiindex alpha by M rho^{-|alpha|}. The Taylor
polynomial through total degree p therefore has uniform error at most

\[
 M\sum_{s>p}\binom{s+D-1}{D-1}(4D)^{-s}\le C M 2^{-p}.       \tag{34}
\]

The last inequality follows by bounding the binomial factor by a fixed
polynomial in s and summing the remaining geometric tail; its constant
depends on D alone. All these polynomials are used only as an error
argument. Their coefficients need not be computed.

Within each cell, match the mass and all initial seed monomials of total
degree <=p with positive weights on original seeds. There are
J=binom(D+p,D) such monomials, including the constant. Starting with the
original positive weights, any support exceeding J is linearly dependent
in R^J. Move weights along a dependence, which has both signs because the
constant is included, until one weight first reaches zero. This preserves
all moments and nonnegativity. Repeat to obtain at most J nodes in that
cell. Empty cells need no nodes. Thus the complete support has

\[
 N\le L\binom{D+p}{D}=O((p+1)^D).                          \tag{35}
\]

Apply (34) on each cell and use exact polynomial matching. The two positive
measures have the same cell masses, so the total source defect is at most
epsilon=CM2^{-p}, simultaneously for every source F,P,Q. The construction
uses only the original finite initialization and a prescribed p. Combining
with (33), choose p=ceil((1/2)log_2 n)+p_0, with p_0 a fixed sufficiently
large integer, to obtain

\[
 \sup_{t\in[0,\infty]}\sup_{|x|\le\sqrt d}
 |f_\nu(t,x)-f_n(t,x)|\le C Y n^{-1/2},\qquad
 N=O((\log(e+n))^{d+k}).                                  \tag{36}
\]

The moving state is N(d+k)+k real coordinates. Fixed retained initialization
and cubature-weight storage are O(N(d+k)); there is no hidden n-sized
array after setup. Setup can inspect and use all n seeds, and no setup-time
complexity or numerical conditioning bound is asserted. The system is an
autonomous weighted interacting-particle ODE, restartable from its stored
state. The actual finite empirical target remains unchanged.

For the concrete iid compact mixture of Section 1, the Gram event has
probability at least 1-2 exp(-2n alpha^2). Thus, for each confidence delta,
(36) holds with probability at least 1-delta for all sufficiently large n.
The constants are independent of n and physical time. The construction is
a proved positive benchmark for two nonlinear learning hidden layers,
widths (n,2), and compact correlated initialization. It makes no claim for
the canonical equal-width iid Gaussian ensemble or its response-memory
closure. Section 4 gives a separate exact equal-width realization with
structured initialization.

## 4. Exact equal-width lift with disclosed structured initialization

The preceding realized finite-n benchmark has an exact realization inside
the original two-hidden-layer width-n dense architecture and its original
block mobilities. This lift changes the initialization, which remains a
substantive restriction. It does not establish a theorem for the canonical
iid Gaussian initialization.

Assume k divides n and partition the n upper neurons into k groups, each
of size n/k. Keep the n independently sampled, continuously heterogeneous
lower seed vectors a_i. For every upper neuron j in group ell initialize

\[
 W^{(2)}_{ji}(0)=b_{\ell i}(0)/n,\qquad w_j(0)=0.
\]

Train all entries of W^(1), W^(2), and w with the original mobilities
n,1,n, respectively, and the loss m^{-1} sum_a r_a^2. Permuting upper
neurons inside a group preserves both the initialized state and the
vector field. Local uniqueness therefore preserves equality of their
entire rows and their readout coordinates. Write the common evolving row
as W^(2)_{ji}=b_{ell i}/n and common readout as w_ell.

The forward equations reduce exactly to Section 1. In particular,

\[
 f=\frac1n\sum_{j=1}^n w_jg_j
   =\frac1k\sum_{\ell=1}^k w_\ell g_\ell,
\quad
 (W^{(2)\top}\delta^{(2)})_i
   =\frac1k\sum_{\ell=1}^k b_{\ell i}\delta_\ell.
\]

The original gradient flow has

\[
 \dot W^{(2)}_{ji}=-\frac2{mn}\sum_a r_a\delta_{\ell,a}h_{i,a},
 \quad
 \dot W^{(1)}_{i,:}=-\frac2{mk}\sum_a
     r_a\operatorname{sech}^2(a_i^\top v_a)
                   (b_i^\top\delta_a)v_a^\top,
 \quad
 \dot w_\ell=-\frac2m\sum_a r_ag_{\ell,a}.
\]

Multiplying the first equation by n gives exactly the b equation of
Section 1. Thus the benchmark's physical time is the original dense
model's physical time. No learning-rate change is needed in the lifted
full network. For the two-input example k=2, take even n.

The dense lifted mixer has rank at most k at initialization and throughout
this symmetric trajectory. Its n-by-n entries are nevertheless all
trainable, nonzero at initialization in the compact example, and evolve
through their prescribed gradient equations. Both nonlinear hidden
representations have the positive learning certificate above. The upper
clone reduction alone leaves n(d+k)+k moving coordinates: the n lower
particles and their edge columns remain continuously diverse and learn.
Initial polynomial cubature is what compresses this remaining population
to O((log n)^(d+k)) moving coordinates at the stated realized-network,
all-time root-n prediction error.

Accordingly, (36) also holds against this actual equal-width dense network
with its structured initialization. The phrase "equal-width" must always
be accompanied here by that initialization restriction. This is neither
the ordinary iid Gaussian dense ensemble nor a theorem about its original
response-memory closure. It demonstrates one genuine finite-width
compression mechanism under a specific admissible architecture and
initialization; it does not settle the general canonical case.
