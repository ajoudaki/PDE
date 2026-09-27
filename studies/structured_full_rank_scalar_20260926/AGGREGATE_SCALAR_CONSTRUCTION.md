# Historical histogram construction for the Gaussian-block memory system

2026-09-27. **Superseded as an answer to the user's scalar-compression
request.** The user requires effective dynamics of aggregate statistics,
not a representation of the joint population distribution. The histogram
below is a distribution representation, and its formal independence from
original width does not answer that request. Sections 1–2 still define the
Gaussian-block population model used by the subsequent aggregate analyses.
The remaining sections preserve the earlier histogram derivation; they are
not evidence of effective aggregate-only compression.

The construction is conservative Eulerian transport of a joint block-state
law. Its states are cell masses. No cell is an independently evolving
representative neuron or block. The generic construction has prohibitive
dimension. It establishes a width-independent approximation mechanism, not
the efficient polynomial accuracy/cost result originally sought.

## 1. Target and the single-order convention

Inputs u_a lie in the unit disk in R^2, labels y_a are fixed and bounded,
and activation is tanh. The first preactivation is w u; u includes the
canonical input normalization. There are two hidden layers and scalar
readout. At width n=bk, initialize the middle matrix with independent
k-by-k Gaussian blocks G, whose entries have variance 1/k. Learned middle
connections remain unrestricted except for the stipulated memory closure.

For clarity use H for memory order during the derivation. The final hierarchy
sets H=P and prescribes every grid/cutoff parameter as a function of P alone.
There is no additional free representative count or resolution parameter in
that final family. Equivalently one can keep the tested memory order H=8
fixed and use P solely to refine the additional aggregate approximation.

The population initial readout is c=0, the limit of the canonical finite-width
initialization with standard deviation 1/n. The Gaussian block G and first
weights w(0) are independent. First weights have iid standard Gaussian entries.

The theorem compares the aggregate system with the Gaussian-block memory
closure at the SAME H. It does not identify the block population with the
canonical fully dense Gaussian population, nor prove the memory-order limit.

## 2. Exact finite-dimensional state of one block

One possible block state is

    z = (G,w,c,A_0,...,A_{H-1},B_0,...,B_{H-1}).

G is k by k, w is k by 2, c is k, and A_j,B_j are k by m. Thus

\[
s_H=k^2+k(3+2mH).
\]

Let mu be a probability measure on this space. It is a law of blocks, not
an ODE coordinate. A separate shared clock is L>=1. For any query input u,
including an input absent from training, compute in the following order:

\[
\begin{aligned}
h_1(z,u)&=\tanh(wu),\\
S_j(u)&=\int k^{-1}B_j^T h_1(z,u)\,d\mu(z),\\
z_2(z,u)&=G h_1(z,u)-\frac2{mL}\sum_{j<H}(2j+1)A_j S_j(u),\\
h_2(z,u)&=\tanh z_2(z,u),\\
f(u)&=\int k^{-1}c^T h_2(z,u)\,d\mu(z),\\
\delta_2(z,u)&=c\odot(1-h_2(z,u)^2),\\
V_j(u)&=\int k^{-1}A_j^T\delta_2(z,u)\,d\mu(z),\\
\delta_1(z,u)&=(1-h_1(z,u)^2)\odot
\left[G^T\delta_2(z,u)-\frac2{mL}\sum_{j<H}(2j+1)B_j V_j(u)\right].
\end{aligned}
\tag{1}
\]

Put r_a=f(u_a)-y_a and rho=(m^{-1}sum_a r_a^2)^{1/2}. The local velocity
b(z,mu,L) consists of

\[
\begin{aligned}
\dot G&=0,\\
\dot w&=-\frac2m\sum_a r_a\delta_1(z,u_a)u_a^T,&
\dot c&=-\frac2m\sum_a r_a h_2(z,u_a),\\
\dot A_{j,a}&=r_a\delta_2(z,u_a)-\frac\rho L
\left[jA_{j,a}+\sum_{i<j}(2i+1)A_{i,a}\right],\\
\dot B_{j,a}&=\rho h_1(z,u_a)-\frac\rho L
\left[jB_{j,a}+\sum_{i<j}(2i+1)B_{i,a}\right],&
\dot L&=\rho.
\end{aligned}
\tag{2}
\]

Initially A=0, B_0 has columns tanh(w(0)u_a), all higher B_j=0, and L=1.
The exact law satisfies partial_t mu + div_z(b mu)=0. With an empirical
law of b original blocks, its characteristic equations reproduce the finite
block memory system. Every original 1/n neuron average is exactly the
1/b block average of the 1/k contraction in (1).

In particular, G and its ACTUAL transpose remain attached to the same state
z. The joint law retains their correlations with w,c,A,B. Separate marginal
means would not suffice.

## 3. The finite aggregate ODE

Fix a box [-B,B]^{s_H} and a Cartesian grid with spacing h dividing B.
Let z_i denote its fixed nodes. Keep one scalar p_i for each node, and L:

\[
\mu_h=\sum_i p_i\delta_{z_i},\qquad p_i\ge0,\quad \sum_i p_i=1.
\]

Every integral in (1) is now a finite weighted sum. The grid nodes never
move. What moves is their probability mass, according to (2).

For each dynamic coordinate j multiply the original velocity by

\[
\chi_B((z_i)_j)=\min\{1,\max\{0,3-4|(z_i)_j|/B\}\}.
\]

This equals one in the inner half-box and vanishes outside the inner
three-quarter box. Write the tapered velocity as v_i=b_B(z_i,mu_h,L).
Static G coordinates still have zero velocity. Define nearest-neighbor rates

\[
q_{i,i+e_j}=(v_{i,j})^+/h,\qquad
q_{i,i-e_j}=(-v_{i,j})^+/h.
\]

Absent-neighbor rates are zero; the taper already sets their drift to zero.
The complete autonomous scalar ODE is

\[
\dot p_i=\sum_{v\sim i}p_vq_{v,i}
-p_i\sum_{v\sim i}q_{i,v},\qquad
\dot L=\left[\frac1m\sum_a(f(u_a)-y_a)^2\right]^{1/2}.
\tag{3}
\]

Rates depend only on the current p,L, the dataset and fixed grid values.
There is no retained neuron array, external population, history tape,
trajectory forcing or fitted-reference oracle. Summing the equations proves
mass conservation; at p_i=0 the derivative is nonnegative, proving positivity.
All rates are locally Lipschitz, including at zero residual. Since p stays
in the simplex and rho<=B+max|y_a|, (3) has a unique global solution.

Initialize p_i with cell probabilities of the prescribed initial Gaussian
law after a stated seed cutoff and nearest-node rounding. These probabilities
depend only on initialization and training inputs, not on future training.
For a finite realized network they are empirical cell frequencies and can be
accumulated in one pass, after which the original blocks are discarded.
Approximate initial integration introduces an explicit initial-mass error;
it is not treated as free exact numerical quadrature.

Here is a deterministic initialization algorithm that does not require
integrating discontinuous lifted cell indicators. Partition the independent
standard Gaussian seed coordinates on a finite cube, using the product of
one-dimensional Gaussian CDF differences as each rectangle's probability.
Place that probability at its center and send the omitted Gaussian tail
mass to the origin. Choose the cube and seed mesh so that the resulting
seed law has W1 error at most h/(1+sqrt(m)); Gaussian first-moment tail
bounds and the rectangle diameter give this finite, computable choice.
The radial clipping maps are 1-Lipschitz. The initial lift into w,G,B_0 is
at most (1+sqrt(m))-Lipschitz for unit inputs, with the Gaussian G scaling
only reducing the constant. Thus the lifted initialization error is at
most h. Round each lifted seed node to the state grid and ADD its weight
to that cell. Total initial W1 error is at most (1+sqrt(s_H))h.
The temporary quadrature nodes are discarded; none are evolved. Finite
precision CDF evaluation can be assigned a further W1 budget of h by
bounding total mass error times the finite box diameter. This may take
enormous initialization work, but depends only on the stated approximation
parameters and known initial law, never on a trained reference or width.

For a new test input u, use (1) with the current p_i,L. No test inputs have
to be included in training, and no Fourier or circle-grid representation
is needed by the model.

## 4. Why this approximates dynamics on every finite interval

Here are the estimates needed for the convergence statement, including
Gaussian tails. The more detailed good/bad-label subtraction is recorded in
AGGREGATE_TRANSPORT_AUDIT.md; the complete model is (1)-(3) above.

### 4.1 Reachable-state bounds

Write Y=max|y_a|. With initial |c|<=C_0, comparison of
|dot c_i|<=2(max|c|+Y) gives

\[
|c(t)|\le C_T=(C_0+Y)e^{2T}-Y,\quad
|r_a|,\rho\le R_T=C_T+Y,\quad 1\le L\le1+TR_T.
\]

These constants are independent of H and block count. If L_j denotes the
ordinary Legendre polynomial, the triangular memory equations give exactly

\[
A_{j,a}(t)=\int_0^t
L_j(2L(s)/L(t)-1)r_a(s)\delta_2(s,u_a)\,ds,
\]

\[
B_{j,a}(t)=h_1(0,u_a)\int_0^1L_j(2v/L(t)-1)\,dv
+\int_0^tL_j(2L(s)/L(t)-1)\rho(s)h_1(s,u_a)\,ds.
\]

Differentiation verifies these formulas using
x d[L_j(2x-1)]/dx=jL_j(2x-1)+sum_{i<j}(2i+1)L_i(2x-1).
Their initial conditions are the prescribed ones. Since |L_j|<=1 on
[-1,1], every coordinate obeys

\[
|A_j|\le TC_TR_T,\qquad |B_j|\le1+TR_T.
\tag{4}
\]

No H-dependent exponential is needed here. Since sum_{j<H}(2j+1)=H^2,
the first-layer equation also gives

\[
|w(t)-w(0)|\le C_{k,m,Y,T,C_0}(1+\|G\|_F+H^2).
\tag{5}
\]

### 4.2 Gaussian law and removal of a seed cutoff

Radially project G and w(0), separately, into Frobenius balls of radius r.
For the displayed population constants below specialize to C_0=0, as in
the stated target. Bounded nonzero readouts add dependence on C_0; an
empirical exponential seed-moment bound adds dependence on that bound and
its exponent. Call the resulting exact H-memory flow f_H^{[r]}. Coupling all cutoffs through
the same initial Gaussian labels and using (4)-(5) gives

\[
\sup_{t\le T,\ |u|\le1}
|f_H^{[r]}(t,u)-f_H(t,u)|
\le C_{k,m,Y,T}(1+H)^8
\exp\{-c_k r^2\exp[-C_{k,m,Y,T}(1+H)^8]\}.
\tag{6}
\]

Constants can be enlarged without changing the stated dependence. The
unbounded-law flow f_H is constructed by the same estimate, not assumed.
For completeness, the comparison argument is as follows.

The initial Gaussian labels satisfy E exp[a(||G||F^2+||w0||F^2)]<infinity
for 0<a<min(k/2,1/2), by the elementary Gaussian integral. Compare two
cutoff flows under that coupling, using
e=E[min(1,||X-X'||infinity)]+|L-L'|, where X=(w,c,A,B).
Split labels at an auxiliary radius s below both cutoffs. On the good set,
G is the same in both flows. Subtract (1) in the order S,z2,f,V,delta1.
The differences of z2,delta2,V cost at most a constant times
1+s+H^2; the second transpose and residual products cost its square.
The triangular memory terms cost at most H^2(1+s+H^2). Thus, after harmless
coordinate-count factors, a valid bound is C_T(1+H)^8(1+s^2).

Bad-label field integrands are bounded by (4); their velocity contribution
is at most C_T(1+H)^8(1+||G||F). Gaussian exponential tails therefore give,
almost everywhere,

    e' <= C_T(1+H)^8 [(1+s^2)e + M exp(-a' s^2)].

This holds for every s below the smaller cutoff. Initial clipped-state
differences cost only a Gaussian tail. Set delta=M exp(-a' r^2),
d=e+delta and choose s^2=a'^{-1}log(M/d) when this lies in [0,r^2];
use the nearest endpoint otherwise. Enlarge M to exceed all bounded-metric
and clock differences on [0,T]. The result is

    d' <= C_T(1+H)^8 d [1+log(M/d)].

Integrating the differential inequality for log(M/d) yields a propagated
power exponent exp[-C_T(1+H)^8]. It proves Cauchy convergence as r grows
and uniqueness for equal initial labels. The uniform bounds (4)-(5) permit
passage through each local integral equation. Good/bad splitting in the
output formula, uniformly over |u|<=1, gives (6), after enlarging constants.
This avoids the invalid single estimate exp(C_T r^2)exp(-c r^2).

### 4.3 Grid error for a bounded flow

On the state box, let V_B bound the speed and K_B bound the joint Lipschitz
constant in state, W1 law distance and L. Directly from (1)-(2), one may use

\[
V_B\le C_{k,m,Y}(1+H)^8(1+B)^4,
\qquad K_B\le C_{k,m,Y}(1+H)^8(1+B)^6.
\tag{7}
\]

For example S=O(B), V=O(B^2), delta1=O(H^2 B^3), and dot w=O(H^2 B^4).
One variation through z2 and the reused transpose gives at most H^4 B^6;
coordinate-count and taper factors fit within (7). L>=1 bounds derivatives
of L^{-1}, independently of how large L becomes.

Represent (3) by a jump process Z_h having law mu_h. Its compensated drift
is exactly b_B, and its martingale remainder M_h satisfies

\[
E\|M_h(t)\|_2^2
=h\,E\int_0^t\sum_j|b_{B,j}|ds\le h s_H V_B T.
\]

Couple its initial state to a characteristic Z of the bounded continuous
law. The initial nearest-grid rounding error is at most sqrt(s_H)h.
Subtract the characteristic integral equations, use
W1(law(Z_h),law(Z))<=E||Z_h-Z||, and apply integral Gronwall. This proves

\[
\sup_{t\le T}
\{E\|Z_h(t)-Z(t)\|+|L_h(t)-L(t)|\}
\le e^{3K_BT}\{\sqrt{s_H}h+\sqrt{h s_H V_BT}\}.
\tag{8}
\]

This needs neither a smooth density nor independent empirical block
trajectories. Lipschitz continuity of the output calculation on the box
gives the same estimate times a finite polynomial factor for
sup_{t<=T,|u|<=1}|f_h-f_B|. An initialization Wasserstein error is simply
added inside braces. All constants are independent of original block count.
The deterministic Gaussian initialization algorithm in Section3 adds at
most another fixed multiple of h inside these braces and leaves the
convergence proof unchanged.

## 5. A strictly k,m,P-only family and its guarantee

The following deliberately excessive schedule makes every dependency explicit:

\[
H=P,\quad B_P=\exp(\exp P),\quad r_P=\sqrt{B_P},\quad
M_P=\left\lceil B_P\exp(B_P^8)\right\rceil,\quad
h_P=B_P/M_P.
\tag{9}
\]

Use the (2M_P+1) nodes from -B_P to B_P on each coordinate. Initialize
from the radially clipped Gaussian seeds at r_P. Grid generation, all
coefficients and the initial distribution use these fixed formulas.
They do not depend on elapsed training time, original width, or future
outputs. The number of stored evolving scalars is exactly

\[
N(k,m,P)=1+(2M_P+1)^{\,k^2+k(3+2mP)}.
\tag{10}
\]

One mass coordinate is redundant because their sum is one. Keeping it makes
the conservative equations simpler. Static grid coordinates can be generated
from indices; no original Gaussian matrix or neuron array is retained.

**Finite-horizon convergence.** Fix k,m and the bounded dataset. Let f_P be
the Gaussian-block population memory flow at order P, and let f_P^agg be
(3) with the schedule (9). Then for every finite T,

\[
\sup_{0\le t\le T,\ |u|\le1}
|f_P^{agg}(t,u)-f_P(t,u)|\longrightarrow0
\quad\text{as }P\longrightarrow\infty.
\tag{11}
\]

Proof: the cutoff term (6) tends to zero because its negative exponential
contains B_P exp[-C_T(1+P)^8], whose logarithm exp(P)-C_T(1+P)^8 tends
to infinity. By (4)-(5), the seed-capped exact trajectory lies strictly in
the inner half-box for all sufficiently large P (depending on T only in
this proof): B_P dominates C_T(1+r_P+P^2). Therefore the dynamic taper
does not change that capped exact trajectory. Finally (7)-(8) tend to zero:
the log discretization error is bounded above by

    -B_P^8/2 + C_{k,m,Y,T}(1+P)^8(1+B_P)^6
      + O(log B_P + log(1+P)),

which tends to minus infinity. The extra output Lipschitz factor is only
polynomial and is absorbed into the logarithmic remainder. The triangle
inequality proves (11). A fixed-memory-H version follows with H unchanged
and the same aggregate schedule. No time-dependent enlargement occurs in
either construction. Loss convergence follows from bounded target outputs
and the identity (f-y)^2-(g-y)^2=(f-g)(f+g-2y).

For finite empirical initial populations satisfying a common exponential
seed-moment bound and bounded initial readout, the same argument is uniform
in their block count. Gaussian initialization gives such bounds with
width-independent high probability by Markov's inequality for the empirical
exponential moment and the union bound for c_i(0)=g_i/n. This is not a
deterministic guarantee over arbitrarily bad Gaussian realizations.

## 6. What has and has not been achieved

This is actual aggregate compression: the ODE evolves distribution masses,
not sampled neurons. It preserves state correlations with G and G^T, dense
learned cross-block interactions, and evaluation at new inputs. A fixed
state-space mesh does not freeze features at initialization: mass moves
between weights and memories throughout training. The mesh covers possible
states, rather than prescribing a frozen span of initialized neuron responses.

Its size is independent of width and elapsed time. Its generic size is also
astronomical. Even without the excessive schedule (9), an isotropic grid
has a curse of dimensionality in s_H. Neither this proof nor the earlier
representative-block experiments establishes an efficient aggregate solver.
Sparse moments, structured tensor approximations or Gaussian-label Galerkin
may reduce cost, but require their own approximation and stability bounds.

The comparison in (11) is only the additional aggregate approximation to
the stipulated memory closure. Separate results are required for memory
order to approximate unrestricted training, for Gaussian blocks to identify
the dense Gaussian trained limit, and for separately stopped fitting
endpoints. A finite-dimensional state for all elapsed times does not mean
uniformly small error on [0,infinity) at a fixed order.

No numerical training was run for this construction. Root derived the finite
ODE and checked the transport and Gaussian-tail arguments against the scoped
transport audit. A separate scoped Gaussian-label Galerkin derivation is
retained in AGGREGATE_LABEL_ROUTE_AUDIT.md. These are internal research
arguments, not independent frozen-input promotion reviews or maintained-book
theorems.

Internal final cross-check: both scoped agents read this complete construction
and reported no material gap in its stated population comparison. Their
requested clarifications, now incorporated, were the C_0/tail-moment
dependence for empirical extensions and the finite Gaussian initialization
algorithm. This records an internal author-team check, not independent
certification of an efficient scalar closure.
