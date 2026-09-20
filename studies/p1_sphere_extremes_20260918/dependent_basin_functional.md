# Dependent inputs: coefficient cancellation and Hilbert basin nullity

Frozen independent scoped route, 2026-09-18. Status: internally proved
candidate, not promoted material. No experiment was run. Scientific inputs
were the supervisor's scoped assignment and clarifications, together with
exactly `basin_spectral_route.md`, `basin_continuous_carrier.md`,
Sections 1--5 of `basin_probability_route.md`,
`basin_hilbert_null_extension.md`, `plateau_finite_critical.md`, and
`docs/observable_p1.md`. No other study, current route, reviewer report, or
external scientific conversation was read. The investigate-conjectures and rigorous-math skills,
with their research-contract, evidence-ledger, and adversarial-audit process
references, were applied. This is the only file written by this route.

## 1. Result and exact contract

For basins whose equilibrium endpoints have bounded lower displacement,
the independence restriction in the preceding basin theorem is a proof
artifact for three distinct unoriented input directions. The missing
individual coefficient cancellation also holds for a dependent nonparallel
triple. It uses bounded lower displacement, the full-dimensional lower-mark
law, and Gaussian support. It needs neither loss below one nor upper or
matrix stationarity.

Retain the exact canonical dimension-three, order-one model, its correlated
Gaussian-derived marks, ridge `eta=1/4096`, full middle matrix, actual
transpose, all trained blocks, and unhalved weighted square loss. Work in
the initialized odd sector, removing inactive constants, with `b_1 in R6`,
`b_2 in R3`, and `M in R^(3 x 6)`. Inputs `u_i` are unit vectors,
weights `mu_i>0` sum to one, and labels are binary. Merge repeated or
antipodal atoms with compatible labels first. There are at most three
active representatives, pairwise distinct modulo sign. They need not be
linearly independent.

On the exact Gaussian carriers put

\[
\mathcal H=L^2_{\rm odd}(\Omega_1;\mathbb R^3)
 \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6},
\quad
X=L^\infty_{\rm odd}(\Omega_1;\mathbb R^3)
 \oplus L^\infty_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6}.
\tag{1}
\]

Write `theta=(v,c,M)`, `w=g+v`, using the physical L2/Frobenius metric
on H. Let S denote finite bad equilibria: zeros of the exact field in X
with positive loss and `M!=0`.

**Theorem.** At every point of S the flow Jacobian exists as a bounded
Fréchet derivative on H, is finite rank and self-adjoint, and has a
nonzero unstable subspace of dimension at most 48. There is a closed
Lipschitz graph of positive finite codimension containing every orbit
trapped in a sufficiently small H-neighborhood of that equilibrium.
The complete basin

\[
\mathcal B=\{\theta_0\in\mathcal H:
  \Phi_t(\theta_0)\to\theta_*\text{ in }\mathcal H
  \text{ for some }\theta_*\in S\}
\tag{2}
\]

lies in a countable union of closed Lipschitz hypersurfaces in H. It is
meagre and has a shy Borel hull. An explicit full-support Gaussian law
on H, its translations, and its positive rescalings annihilate that hull.
The Gaussian perturbation can have bounded fields almost surely.
Moreover `B intersect X` is meagre in X, despite only requiring
H-convergence in (2).

The theorem permits arbitrary H initial states but restricts its
equilibrium endpoints to S. It is not a theorem about every H-equilibrium.
Section 7 separately extends the endpoint class to `v_* in L-infinity`,
`c_* in L2`, with the same lower-displacement restriction, and gives the
finite-sample corollary for at most one independent input relation.

For `0<L(theta_*)<1`, the Jacobian also has a nonzero stable subspace.
The theorem neither excludes the deterministic canonical state from (2)
nor asserts convergence, compactness, or absence of escape.

## 2. Coefficient cancellation with one input relation

For the current state put

\[
\begin{gathered}
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad z_i=Ma_i,
 \quad h_i=\tanh(b_2\cdot z_i),\quad f_i=E_2[ch_i],\\
 \rho_i=\mu_i(f_i-y_i),\quad
 d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot z_i)],\quad
 T_i=\rho_iM^Td_i.
\end{gathered}
\tag{3}
\]

Lower stationarity is exactly

\[
 \sum_i\operatorname{sech}^2(w\cdot u_i)
                 (b_1\cdot T_i)u_i=0\quad\text{a.s.}
\tag{4}
\]

**Cancellation lemma.** In any positive integer dimension d, suppose
the unit directions `u_1,...,u_m` are pairwise distinct modulo sign and
the matrix U with these columns has `dim ker U<=1`. Use the canonical
odd mark `b_1 in R^(2d)` and fixed vectors `T_i in R^(2d)`.
If `w-g` is essentially bounded and (4) holds, then every `T_i=0`.

The canonical mark law is absolutely continuous with positive density
on an open neighborhood of zero. Indeed, before the invertible linear
Cholesky normalization, each pair is

\[
 h_j=\tanh G_j,\qquad
 k_j=\tanh(\sqrt\tau Z_j+\alpha h_j),\qquad\tau>0.
\]

This is a smooth bijection from R2 to `(-1,1)^2` with Jacobian
`sqrt(tau)(1-h_j^2)(1-k_j^2)>0`. Independent Gaussian coordinate pairs
give a positive density throughout `(-1,1)^(2d)`. Applying the invertible
normalization proves the claim, including probability zero for every
proper linear hyperplane. All correlations between b_1 and g are retained.

If U has independent columns, (4) and positivity of every gate give
`b_1 dot T_i=0` almost surely. Absolute continuity then gives `T_i=0`.

Otherwise write `ker U=span{alpha}`, let `J={i:alpha_i!=0}`, and put
`s_i=sech^2(w dot u_i)>0`. There is a measurable scalar lambda with

\[
                   s_i(b_1\cdot T_i)=\lambda\alpha_i.
\tag{5}
\]

For i outside J this directly forces `T_i=0`. For i in J put
`V_i=T_i/alpha_i`. If any V_i vanishes, (5) forces lambda to vanish
almost surely and hence all T_i vanish. Otherwise, for every pair in J,

\[
 (b_1\cdot V_i)(b_1\cdot V_j)
                    =\lambda^2/(s_i s_j)\ge0\quad\text{a.s.}
\tag{6}
\]

Two nonzero real linear forms whose product is nonnegative on a
neighborhood of zero must be positive multiples of each other. If their
coefficient vectors were independent, the map to their two values would
be onto R2. A preimage of `(1,-1)`, rescaled into that neighborhood,
would have negative product. A negative proportionality factor would
also give a negative product off their common kernel. These exhaust
the alternatives. The a.s. inequality in (6) holds throughout the mark
neighborhood: a negative value would yield, by continuity, a negative
open set of positive probability. Therefore

\[
              V_i=\beta_i V\quad(i\in J),\qquad
              V\ne0,\quad\beta_i>0.
\tag{7}
\]

The event `b_1 dot V=0` has probability zero. Dividing (5) by this
common form gives, for any two distinct i,j in J,

\[
 \frac{\operatorname{sech}^2(w\cdot u_j)}
      {\operatorname{sech}^2(w\cdot u_i)}
                =\frac{\beta_i}{\beta_j}>0\quad\text{a.s.}
\tag{8}
\]

There are at least two such indices, since a single nonzero column
cannot support a dependence. Since the directions are nonparallel,
choose a unit e perpendicular to u_i with `a=|e dot u_j|>0`.
Put `C=1+||w-g||_infty`. On the positive-probability Gaussian event
`|g-te|<1`, outside the common null sets,

\[
       |w\cdot u_i|\le C,\qquad |w\cdot u_j|\ge ta-C.
\]

The bounds `exp(-2|r|)<=sech^2(r)<=4exp(-2|r|)` yield

\[
 \frac{\operatorname{sech}^2(w\cdot u_j)}
      {\operatorname{sech}^2(w\cdot u_i)}
                  \le4e^{4C}e^{-2ta}.
\tag{9}
\]

Choose a finite t making the right side smaller than the positive
constant in (8). This contradicts the a.s. identity on an event of
positive probability, proving the lemma. Neither independence between
g and b_1 nor a conditional tail-density claim was used.

For at most three distinct unoriented inputs in dimension three, either
the columns are independent or exactly three have rank two. Thus the
lemma covers the stated triple class. At every finite critical state,

\[
                         \rho_iM^Td_i=0\quad\text{for all }i.
\tag{10}
\]

This is stronger than the requested low-loss cancellation: no loss
condition, residual sign assumption, upper stationarity, or matrix
stationarity entered the proof.

## 3. Exact Hilbert field and the vanishing remainder bound

With `phi=tanh`, the exact field is

\[
 F_v=-2\sum_i\phi'(w\cdot u_i)(b_1\cdot T_i)u_i,
 \quad F_c=-2\sum_i\rho_i h_i,
 \quad F_M=-2\sum_i\rho_i d_i a_i^T.
\tag{11}
\]

Bounded marks, bounded gate derivatives, and Cauchy--Schwarz imply
local Lipschitzness on H. For example,
`|a_i(v)-a_i(v')|<=C||v-v'||_2`; subsequent finite-vector operations
and upper pairings with c preserve local Lipschitzness. Subtraction of
the lower gate and coefficient factors proves the lower field estimate.
The loss is C1 on H with `grad L=-F`. If `R=sqrt(L(theta_0))`, the
energy identity gives `sum |rho_i(t)|<=R` and

\[
 \|c(t)\|_2\le\|c(0)\|_2+2Rt,\quad
 \|M'(t)\|_F\le CR\|c(t)\|_2,\quad
 \|v'(t)\|_2\le CR\|M(t)\|_F\|c(t)\|_2.
\tag{12}
\]

These polynomial bounds prevent finite-time escape; the local
contraction construction therefore gives a global positive-time flow.
Supremum-norm velocity bounds give X preservation on finite intervals.
Local reverse existence along each finite trajectory segment makes
each time map open and locally bi-Lipschitz onto its image in either
space. None of these facts uses input independence.

The finite moment map has the stronger estimates

\[
\begin{split}
 Da_i(v)\zeta&=E_1[b_1\phi'(w\cdot u_i)(\zeta\cdot u_i)],\\
 |a_i(v+\zeta)-a_i(v)-Da_i(v)\zeta|&\le C\|\zeta\|_2^2,\\
 \|Da_i(v)-Da_i(\widetilde v)\|_{L^2\to\mathbb R^6}
                    &\le C\|v-\widetilde v\|_2.
\end{split}
\tag{13}
\]

Scalar Taylor expansion followed by integration proves the second line;
the Lipschitz derivative gate and Cauchy--Schwarz prove the third.
Upper gates depend smoothly on finite vectors into L-infinity, and
pairing with c is continuous bilinear. Hence T_i and `F_c,F_M` are
locally C^(1,1) on H.

Set `G_i(v)t=phi'(w dot u_i)(b_1 dot t)u_i`. These operators from R6
to lower L2 are uniformly bounded and satisfy

\[
             \|G_i(v)-G_i(\widetilde v)\|
                         \le C\|v-\widetilde v\|_2.
\tag{14}
\]

At a finite critical point, put `x=theta-theta_*`. By (10) the lower
linear part is `A_v x=-2 sum G_i(v_*) DT_i(theta_*)x`. Its remainder
is -2 times the sum of

\[
 [G_i(v)-G_i(v_*)]T_i(\theta)
 +G_i(v_*)[T_i(\theta)-DT_i(\theta_*)x].
\tag{15}
\]

On a radius-r H-ball, both factors in the first product have size O(r)
and bounded Lipschitz constants; subtracting products gives Lipschitz
constant O(r). The second bracket has this bound by C^(1,1) regularity.
The other two field components obey it as well. Thus

\[
 F(\theta_*+x)=Ax+N(x),\quad N(0)=0,\quad
 \|N(x)-N(y)\|_{\mathcal H}\le Cr\|x-y\|_{\mathcal H}
       \quad(\|x\|,\|y\|\le r).
\tag{16}
\]

This verifies the actual Fréchet derivative at the equilibrium and
the precise vanishing local Lipschitz constant used below. No claim
that the field is Fréchet C1 on an H-neighborhood is made.

## 4. Spectral splitting and a concrete trapping graph

The usual lower multiplier in the derivative is

\[
 \zeta\longmapsto-2\sum_i(b_1\cdot T_i)
       \phi''(w\cdot u_i)(\zeta\cdot u_i)u_i.
\tag{17}
\]

Equation (10) makes it zero. Every remaining term factors through
finitely many moments. The range of A lies in the span of lower
functions `b_(1,j) phi'(w_* dot u_i)u_i`, upper functions `h_(i,*)`
and `b_(2,j) phi'(b_2 dot z_(i,*))`, and the 18 matrix directions.
That space V lies in X and has dimension at most `10m+18<=48`.
Symmetry of the physical loss second differential on X, whose bilinear
form is bounded in H, extends to H by density. Thus A is self-adjoint;
it vanishes on the orthogonal complement of V. Finite symmetric
diagonalization gives

\[
                 \mathcal H=E_u\oplus E_s\oplus E_0,
\tag{18}
\]

the positive, negative, and zero spectral spaces of A. Nonzero
eigenvectors lie in V. Spectral projections onto E_u and E_s are
finite sums of H-pairings against bounded eigenvectors, so they
preserve X and are bounded there.

The strict-saddle theorem in `plateau_finite_critical.md`, Sections
3--4, already covers dependent triples. All its hypotheses hold:
positive loss, nonzero M, bounded displacement and readout, and distinct
unoriented directions. It gives bounded odd q with `D^2L[q,q]<0`.
Hence `<Aq,q>_H>0` and `dim E_u>=1`. If loss is below one, some h_j
is nonzero; varying only c by h_j gives

\[
             D^2L[(0,h_j,0),(0,h_j,0)]
                    =2\sum_i\mu_i\langle h_j,h_i\rangle^2>0.
\tag{19}
\]

So E_s is nonzero too. Loss below one also forces `M!=0`.

For the graph let `E_cs=E_s+E_0` and let lambda be the smallest
positive eigenvalue on E_u. In the sum of the component Hilbert norms,

\[
 \|e^{A_{cs}t}\|\le1,\qquad
 \|e^{-A_ut}\|\le e^{-\lambda t}\quad(t\ge0).
\tag{20}
\]

The radial retraction `R_r x=x min(1,r/||x||)` is 2-Lipschitz.
By (16), `N_hat=N composed with R_r` is globally epsilon-Lipschitz
with epsilon arbitrarily small. Take `gamma=lambda/2`. In the Banach
space of continuous paths with norm
`sup_(t>=0) exp(-gamma t)(||x_cs(t)||+||x_u(t)||)`, for each
`eta in E_cs` solve

\[
\begin{split}
 x_{cs}(t)&=e^{A_{cs}t}\eta+
   \int_0^t e^{A_{cs}(t-s)}\widehat N_{cs}(x(s))\,ds,\\
 x_u(t)&=-\int_t^\infty e^{A_u(t-s)}\widehat N_u(x(s))\,ds.
\end{split}
\tag{21}
\]

The integral Lipschitz constants sum to
`epsilon/gamma+epsilon/(lambda-gamma)=4epsilon/lambda`. Choose r
so this number q is below one half. Iteration is a contraction; its
unique fixed path has norm at most `||eta||/(1-q)` and depends
Lipschitzly on eta. Put `h(eta)=x_u(0)` and
`G_*={eta+h(eta):eta in E_cs}`. This is a closed Lipschitz graph of
positive finite codimension. The homeomorphism
`eta+u -> eta+u-h(eta)` sends it to E_cs, proving empty interior.

An original orbit trapped in the small ball is bounded and satisfies
the modified equation. Backward variation of constants from time T
in the unstable component has terminal term
`exp(A_u(t-T))x_u(T)`, tending to zero as T tends to infinity.
Therefore the orbit solves (21), and uniqueness places its initial
state in G_*. This covers all trapped orbits, including those tending
to a different equilibrium in the same neighborhood.

Because E_u lies in X, the intersection of G_* with X is the graph
of the restricted h over `E_cs intersect X`. The embedding `X->H`
and finite-dimensional norm equivalence on E_u make it Lipschitz in
X. It is closed nowhere dense there as well.

## 5. Time-map pullbacks and the complete null basin

No new independence assumption enters this step. The exact needed
regularity, geometric implication, and probability law are supplied
here; complete directional proofs are also in the allowed
`basin_hilbert_null_extension.md`.

At an arbitrary H-state, the derivative of (11) exists in the norm
Gâteaux sense. Its lower component is the multiplier (17) plus
`-2 sum G_i(v) DT_i(theta) delta theta`; the other components
differentiate through the C^(1,1) moments. For a fixed lower direction
zeta, the lower-gate difference quotient is bounded by
`||phi''||_infty |zeta dot u_i|`. Dominated convergence of its squared
error proves L2 convergence. This gives a bounded linear directional
derivative. On every H-ball, `||DF(theta)||<=C_R`.

The derivative is continuous in theta on each fixed direction. For the
only delicate term, if `v_n->v` in L2, split the integral of
`|[phi''(w_n dot u_i)-phi''(w dot u_i)](zeta dot u_i)|^2` at
`|zeta dot u_i|=A`. The large-direction part is bounded by
`4||phi''||_infty^2 integral_(|zeta dot u_i|>A)|zeta dot u_i|^2`,
uniformly in n. The other part is bounded by
`A^2||phi'''||_infty^2||v_n-v||_2^2`. First send n to infinity,
then A to infinity. Every finite-coefficient term is continuous by
(13)--(14). This proves strong continuity of DF.

For a finite trajectory segment, difference quotients of its integral
equation converge to the unique solution of

\[
 V'(t)=DF(\Phi_t(\theta))V(t),\qquad V(0)=h.
\tag{22}
\]

To verify this, the derivatives are uniformly bounded near the segment.
Evaluation `(theta,h)->DF(theta)h` is jointly continuous by that bound
and strong continuity. The reference linear solution V has compact
trajectory image, so the directional error in the difference-quotient
equation tends uniformly to zero; Gronwall bounds the remaining unknown
error. Comparing (22) at nearby initial states proves strong continuity
of the time-map derivative by the same compactness argument. Solving
(22) backward gives its bounded inverse. Thus every finite time map
is locally Lipschitz with invertible, strongly continuous bounded
linear Gâteaux derivatives. No operator-norm continuity is assumed.

A positive-codimension Lipschitz graph lies in a scalar Lipschitz
hypersurface. Select one nonzero direction e in its complementary
space and delete that coordinate. The original base coordinate is
recovered by its bounded projection, so the scalar coordinate is
Lipschitz on the projected domain. The scalar extension
`h_ext(w)=inf_d[h(d)+L||w-d||]` extends it to the entire hyperplane.

For a hypersurface `Gamma={w+h(w)e:w in W}`, let `ell(e)=1`,
`W=ker ell`, and `P=I-e ell`. At x_0 and for a time map Psi choose
`v=D Psi(x_0)^(-1)e`. Strong directional continuity provides a
neighborhood and constants a,b with

\[
 \ell(D\Psi(x)v)\ge a>0,\qquad
 \|PD\Psi(x)v\|\le b,\qquad a-Lb>0.
\tag{23}
\]

On a small product cylinder `x=x_0+w+tv`, with w in a closed
complement to `Rv`, define
`q(w,t)=ell(Psi(x))-h(P Psi(x))`. Integration of the continuous
directional derivative along each line gives
`q(w,t)-q(w,s)>=(a-Lb)(t-s)` for t>s. At fixed t its Lipschitz
constant in w is at most `Lip(Psi)(||ell||+L||P||)`. Comparing
two roots through their cross point in the cylinder gives

\[
 |t-\widetilde t|\le
 \frac{\operatorname{Lip}(\Psi)(\|\ell\|+L\|P\|)}{a-Lb}
                  \|w-\widetilde w\|.
\tag{24}
\]

Thus the local pullback has at most one root over each w and is
contained in a scalar Lipschitz graph. The preceding extension makes
it a subset of a global closed Lipschitz hypersurface. This proves
the geometric pullback property directly, with no differentiation of
the Lipschitz graph function.

H is separable. From the smaller trapping neighborhoods covering S,
whose closures lie inside their larger trapping neighborhoods, choose
a countable subcover. If an orbit converges to any point in S, its
entire sufficiently late tail lies in one of the larger neighborhoods.
At some integer n its state therefore lies in that neighborhood's
graph. The limit need not be the selected graph's center. Hence the
basin lies in countably many integer-time preimages of the selected
graphs. Equation (24) and second countability cover each preimage by
countably many scalar Lipschitz hypersurfaces. There is a Borel hull

\[
                  \mathcal B\subset A=\bigcup_{j\ge1}\Gamma_j.
\tag{25}
\]

Each hypersurface is closed and has empty interior, so A is meagre.
For the X-category assertion use instead the original trapping graphs
intersected with X and the open X-time maps. These inverse images
are closed with empty interior. The countable selection was made in
H, so nonseparability of X causes no problem.

Choose `(e_n)` in X dense in the H-unit sphere and define

\[
 a_n=\frac{2^{-n}}{1+\|e_n\|_X},\qquad
 G=\sum_{n\ge1}a_ng_ne_n,
 \qquad g_n\text{ independent }N(0,1).
\tag{26}
\]

This series converges absolutely in X almost surely because the
expected sum of its X-norms is finite. Each continuous H-linear
functional is a normal variable with variance
`sum a_n^2 ell(e_n)^2`, so this is a Gaussian law. Its support is
all of H. Indeed, finite linear combinations of the e_n approximate
any target. A finite block of normal coefficients can approximate
their prescribed values with positive probability, and an independent
sufficiently late tail has arbitrarily small expected H-norm and
positive probability to be small. Increasing that finite block while
prescribing zero extra coefficients does not change the target.

For each scalar hypersurface its open transverse cone is
`{d:|ell(d)|>L||Pd||}`. By density it contains some e_n. Every
affine line parallel to that e_n meets any translate of the
hypersurface at most once; two intersections would contradict the
Lipschitz inequality. Condition on all coefficients in (26) except
g_n. Atomlessness and Fubini give zero probability of this translated
hypersurface. Countable subadditivity proves

\[
                  \mathbb P(G\in x+A)=0
                              \quad(x\in\mathcal H).
\tag{27}
\]

Positive rescaling has the same proof. Replacing g_n by independent
uniform variables on `[-1,1]` gives uniform convergence on the compact
coefficient product, hence a compactly supported probability with the
same translation-null property. This is the explicit shyness witness.
If the basin itself is not Borel specified, (25) proves its outer
probability is zero. There is no infinite-dimensional Lebesgue measure
in this statement and no Gaussian law on the nonseparable X topology
with asserted full X-support.

## 6. Continuous carriers and strong-stable trajectories

The compact continuous-carrier construction also extends to dependent
triples. Put
`K_1=supp Law(b_1,tanh(g dot u_1),...,tanh(g dot u_m))` and
`K_2=supp Law(b_2)`, retaining the exact pushforward measures. For
`r_i=tanh(g dot u_i)`, the identity

\[
 \tanh((g+v)\cdot u_i)
       =\frac{r_i+\tanh(v\cdot u_i)}
              {1+r_i\tanh(v\cdot u_i)}
\tag{28}
\]

has the same positive denominator and uniform derivative bounds for
bounded v, independently of any input relation. The odd continuous
function product space is separable and invariant with a smooth exact
flow. At critical points (10) gives a finite-rank Hessian with continuous
eigenvectors. The basin conclusion therefore also holds in that
supremum-norm topology. The H result above additionally covers bounded
measurable endpoint fields and the weaker H-convergence topology.

At a given finite equilibrium with `0<L<1`, equation (19) gives a
nonzero stable subspace. In X the field is smooth. Split into E_s
and `E_cu=E_0+E_u`, and let beta be the smallest absolute stable
eigenvalue. Use stable integration from zero and center-unstable
integration from infinity, as in (21), now in the decaying path norm
`sup_(t>=0) exp(beta t/2)||x(t)||_X`. The two integral Lipschitz
constants sum to `4epsilon/beta`. The resulting contraction gives
a small strong-stable graph through the equilibrium, whose nonzero
points converge exponentially in X. Such a trajectory cannot reach
an equilibrium at finite time by uniqueness. The exact energy
identity therefore gives strictly decreasing loss tending to the
positive equilibrium loss. Small enough points have initial loss below
one. This is conditional on a given equilibrium; it does not construct
one for every dependent law or intersect this graph with the canonical
initial state.

## 7. Separately stated extensions and endpoint restrictions

### Square-integrable endpoint readouts

Replace S by

\[
 S_2=\{\theta_*\in\mathcal H:F(\theta_*)=0,
    \ v_*\in L^\infty,\quad L(\theta_*)>0,\quad M_*\ne0\}.
\tag{29}
\]

Here the readout c_* is only required to lie in L2. The conclusions
about H-local graphs, the H point-convergent basin's meagre/shy
hull, and the explicit bounded randomization remain valid for S_2.
All coefficient and derivative estimates in Sections 2--5 already use
only c_* in L2. The strict-saddle proof also extends: its lower
perturbation, upper perturbation, and all differentiated gates are
bounded, so every remaining pairing with c_* is finite by
Cauchy--Schwarz. The complete variation argument is included below.
Thus no bounded readout is needed to produce negative curvature or the
finite-rank spectral split.

The X-category conclusion also persists even if a graph is centered
outside X. If p is the center and P_cs,P_u its bounded projections,
the translated graph is `p+eta+h(eta)`. For `xi in E_cs intersect X`
its intersection with X has the parametrization

\[
          \xi+P_up+h(\xi-P_{cs}p).
\tag{30}
\]

The last two terms lie in the bounded finite-dimensional E_u. This is
an X-Lipschitz graph over `E_cs intersect X`, proving that it is
closed nowhere dense in X. The countable-cover proof is unchanged.

The restriction `v_* in L-infinity` in (29) is substantive. For an
equilateral planar triple with `sum u_i=0`, equal weights and all labels
+1, take `w=0`, so `v=-g in L2` but not in L-infinity. Set
`c=b_2 dot q` and choose M,q with
`M^T E_2[b_2b_2^T]q!=0`. Then `a_i=z_i=h_i=f_i=0`; readout and
matrix velocities vanish. The lower velocity is proportional to
`sum u_i=0`. This H-equilibrium has loss one and equal nonzero T_i.
It lies outside S_2 and shows that the cancellation conclusion cannot
be extended to all H-equilibria merely by removing bounded displacement.
It is not a counterexample to any low-loss all-H basin theorem.

### Finite samples with at most one independent relation

For the exact general-dimensional p=1 population equations supplied
by `docs/observable_p1.md`, fix any positive integer d, any finite
number m of pairwise distinct unoriented unit directions, positive
probability weights, and compatible binary labels. Use canonical
marks in R^(2d) and R^d and full M in R^(d x 2d). Assume
`dim ker U<=1`. Define H,X,S_2 by replacing 3,6 with d,2d.
Then the preceding basin result holds, with rank bound

\[
                       \operatorname{rank}A
                              \le(3d+1)m+2d^2.
\tag{31}
\]

This is a theorem about the exact autonomous population system. The
source explicitly does not establish identification with a general-d
trained-network limit, and no such identification is added here.

Cancellation is exactly the arbitrary-d lemma in Section 2. The lower
range has at most `2dm` generators, the upper range at most `(d+1)m`,
and the matrix block dimension is `2d^2`, proving (31). All norm,
graph, and probability estimates are dimension-finite and unchanged.
It remains to verify strict saddles beyond the three-input statement
in the prior landscape report; the needed proof extends as follows.

Partition the nonzero effective vectors z_i into signed-equality
groups, with representatives `z_G!=0` distinct modulo sign, and let
Z be the zero-vector group. Positive loss gives some `rho_i!=0`.
Choose one group J with a nonzero residual, and put

\[
                 R(w)=\sum_{i\in J}\rho_i
                                  \phi'(w\cdot u_i)u_i.
\tag{32}
\]

Discard zero coefficients in this sum. Choose a unit e for which all
`|e dot u_i|` in it are nonzero and pairwise distinct, avoiding finitely
many proper hyperplanes. There is a unique smallest one. On the
positive-probability event `|g-te|<1`, bounded displacement makes every
other gate divided by that smallest gate tend to zero uniformly as
t tends to infinity, by the same exponential bounds as (9). Thus R
is nonzero on a set of positive probability. Since `M!=0` and the
mark law is absolutely continuous, `Mb_1!=0` almost surely. For some
coordinate k the bounded odd direction

\[
                \delta w=(Mb_1)_kR(w)
\tag{33}
\]

gives a nonzero residual-weighted effective-vector variation in J:

\[
 \left[\sum_{i\in J}\rho_iM\delta a_i\right]_k
                   =E_1[(Mb_1)_k^2|R(w)|^2]>0.
\tag{34}
\]

Write `q_G=sum_(i in G)rho_i M delta a_i` for every group, including
q_Z for the zero group. The residual-weighted upper feature variation is

\[
 S(b)=b\cdot q_Z+\sum_G(b\cdot q_G)\phi'(b\cdot z_G).
\tag{35}
\]

At least one q is nonzero by (34). For any finite number of groups,
S does not belong to the span of the current features
`phi(b dot z_G)`. Here is the full finite-family separation argument.
The upper mark law has positive density on an open neighborhood of zero.
A putative a.s. identity is therefore an identity there by continuity.
Choose a vector e so the numbers `a_G=e dot z_G` have distinct
nonzero absolute values and at least one `e dot q_G` or `e dot q_Z`
is nonzero, again avoiding finitely many hyperplanes. Restrict to
`b=t e` and extend the real-analytic identity from an interval about
zero to the real line. It has the form

\[
 t\beta_Z+\sum_G t\beta_G\operatorname{sech}^2(a_Gt)
                        =\sum_G A_G\tanh(a_Gt).
\tag{36}
\]

As t tends to positive infinity, boundedness of the right side gives
`beta_Z=0`; its constant limit must then vanish. Order groups by
increasing `|a_G|`. Multiply the remaining identity by the exponential
`exp(2|a_G|t)` for the smallest remaining group. Divide by t to get
`beta_G=0`, using
`sech^2(a t)=4exp(-2|a|t)+O(exp(-4|a|t))`. Then take the undivided
limit to get `A_G=0`, using
`tanh(a t)=sign(a)[1-2exp(-2|a|t)+O(exp(-4|a|t))]` and the zero
constant sum. Remove this group exactly and repeat finitely many times.
All coefficients beta vanish, contradicting their choice. Higher
exponential-harmonic coincidences cause no problem because each group
is eliminated before proceeding. If there are no nonzero groups,
(36) simply says `t beta_Z=0`, the same contradiction.

Let `H_0=span{h_i}` and `k=S-P_(H_0)S`. It is bounded, odd, and
nonzero. Also `D_c f_i[k]=0` for every i, and

\[
             \sum_i\rho_iD^2_{cw}f_i[k,\delta w]
                        =\langle k,S\rangle=\|k\|_2^2>0.
\tag{37}
\]

For the unhalved square loss, linearity in c and these orthogonality
identities give exactly

\[
 D^2L[(\delta w,sk,0),(\delta w,sk,0)]
      =D^2L[(\delta w,0,0),(\delta w,0,0)]+4s\|k\|_2^2.
\tag{38}
\]

The fixed term is finite even with c_* only in L2: all perturbations,
marks, and differentiated gates are bounded and every factor of c_*
occurs in an integrable pairing. Choose a finite negative s of large
enough magnitude. This proves strict negative curvature for arbitrary
finite m and d at every positive-loss equilibrium with `M!=0` and
bounded lower displacement. In this subsection the extra condition
`dim ker U<=1` is used only for cancellation and the basin theorem,
not for the strict-saddle variation itself.

## 8. Scope, adversarial checks, and supersession

| Claim | Status | Exact evidence or limitation |
|---|---|---|
| Dependent nonparallel triple has individual critical cancellation | Proved here | One-dimensional input kernel, mark sign rigidity, Gaussian-tail contradiction |
| Cancellation requires loss below one | Not required | Only lower stationarity and bounded displacement enter Section 2 |
| Hilbert trapping graphs and null basin extend to all triples with bounded lower endpoint displacement | Proved here using the assigned strict-saddle result | Equations (10), (13)--(27) verify all functional hypotheses |
| Endpoint readout may be only L2 | Proved here | All derivative pairings are finite; variation (38) and translated graph (30) |
| Arbitrary-d finite samples with at most one input relation | Proved here | Section 2 cancellation, finite-family strict-saddle proof, rank bound (31) |
| Arbitrary finite sample dependence with input-kernel dimension greater than one | Open in this route | A single common scalar in (5) is unavailable |
| Every H-equilibrium satisfies the cancellation lemma | False | Loss-one H-only example in Section 7 |
| Deterministic canonical initialization avoids bad convergence | Open | Nullity does not exclude one specified state |
| Positive-loss escape or approach to an arbitrary equilibrium continuum is excluded | Open | No compactness or global set-level trapping argument |

The main new argument survives three concrete adversarial checks.
Correlation of g and b_1 is harmless: the sign argument uses only the
mark marginal and the tail argument only the Gaussian marginal; they
are never multiplied as independent events. The finite union of
exceptional null sets cannot exhaust any positive-probability Gaussian
tail ball. Finally, residual signs are absorbed into alpha and V_i;
no positivity of the residuals is used.

The canonical state `(v,c,M)=(0,0,D)` is deterministic. The random
population marks inside a state are not the random initial-state law
(26). A translated/scaled version of (26) is a different initialization
experiment. Matrix-only randomization or a slice with c fixed at zero
needs a separate transversality proof. Neither meagreness nor shyness
decides membership of the canonical state in (25).

The route does not treat input-kernel dimension greater than one:
stationarity then allows several independent scalar coefficients, and
the common-sign reduction (6) need not follow. This limits the proof,
not the truth of a broader basin theorem. A new cancellation lemma or
a verified multiplier-plus-finite-rank graph argument remains necessary
there. Likewise, the counterexample outside bounded displacement only
defeats unrestricted coefficient cancellation; it does not establish a
large basin or refute a possible full-H low-loss theorem.

For basins with bounded lower endpoint displacement, this result
supersedes the dependent-triple gap in the earlier spectral and
Hilbert-null reports. It leaves their deterministic-initialization,
nonconvergent-limit-set, and escape limitations unchanged.
