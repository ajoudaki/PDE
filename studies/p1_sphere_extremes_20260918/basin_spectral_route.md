# Spectral and graph route for finite bad population equilibria

Status: internally derived candidate, frozen on 2026-09-18 before reading
another current basin route or a review. No experiment was run. This is
study-owned material, not a promoted theorem.

Scientific input scope: `docs/observable_p1.md` in full; the complete
state/equations/existence sections C.4.7.9.3--4 and C.4.7.10.D.3 in
`docs/global_nonlinear.md`; this study's `plateau_finite_critical.md`,
`terminal_geometry.md`, and `rank_one_nonlinear_obstruction.md` in full.
No README, study history, other study, current basin route, or review was
read. Required investigation and rigorous-math skills, including the
research-contract, evidence-ledger, adversarial-audit, and proof-search
process references, were read. The supervisor requested a strong-stable
extension after the initial spectral mechanism was reported; its proof
is included below. No external stable-manifold theorem is invoked.

## 1. Exact contract and results

Fix at most three linearly independent normalized inputs in R3, positive
probability weights, and binary labels. Use the exact dimension-three,
order-one population model and canonical Gaussian-derived marks, ridge,
full trainable middle matrix, actual transpose, all three trained blocks,
and unhalved square loss from the assigned sources. Antipodal/repeated
consistent atoms may first be merged. Independence refers to the active
representatives after that merge. This is an explicit restriction: the
prior strict-saddle theorem itself covers more dependent geometries.

Use the invariant odd-mark sector, remove its inactive constants, and
write `b_1 in R6`, `b_2 in R3`, and `M in R^(3 x 6)`. The fixed lower
Gaussian vector is `g`. On their exact Gaussian probability carriers let

\[
 \mathcal H=L^2_{\rm odd}(\Omega_1;\mathbb R^3)
       \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6},
 \qquad
 X=L^\infty_{\rm odd}(\Omega_1;\mathbb R^3)
       \oplus L^\infty_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6}.
 \tag{1}
\]

The state coordinates are `theta=(v,c,M)` with `w=g+v`. The norm of H is
exactly the physical population L2/Frobenius norm; use the sum of the two
supremum norms and the Frobenius norm on X. The Gaussian carriers are
standard finite-dimensional Gaussian spaces, so H is a separable Hilbert
space. X is a Banach space and need not be separable. No population law
or Gaussian correlation is changed by using these characteristic spaces.

A *finite bad equilibrium* means a zero of the exact vector field in X
with positive loss and `M!=0`. Denote their set by S. The bounded field
condition is the same finite-state condition as the assigned landscape
report; it does not assert an all-time bound.

**Theorem A: local finite-codimension obstruction.** At every `theta_*`
in S, the flow Jacobian in H exists at that point, is finite rank and
self-adjoint, and has `k>=1` strictly positive eigenvalues counted with
multiplicity. In H there is a closed Lipschitz graph of codimension k
containing every orbit that stays in a sufficiently small H-neighborhood
of `theta_*` for all positive time. Its intersection with X is a closed
codimension-k Lipschitz graph in X. In particular both graphs are nowhere
dense in their respective topologies. One may take `k<=48`.

**Theorem B: the complete point-convergence basin is meagre.** The set

\[
 \mathcal B_{\rm fin}=
 \{\theta_0\in\mathcal H:
      \Phi_t(\theta_0)\longrightarrow\theta_*\text{ in }\mathcal H
      \text{ for some }\theta_*\in S\}
 \tag{2}
\]

is contained in a countable union of closed nowhere-dense sets in H.
Its intersection with X is likewise meagre in X. The latter conclusion
includes convergence in H from bounded-field initial states and is
therefore stronger than a conclusion requiring X-convergence. S may be
uncountable and unbounded. This conclusion uses separability of H and
local graphs proved in H; it does not assume separability of X.

**Theorem C: nonstationary positive-loss limiting trajectories exist.**
If `theta_*` is a finite equilibrium with `0<L(theta_*)<1`, then its
negative-flow-Jacobian eigenspace has dimension `ell>=1`, in addition to
the unstable eigenspace in Theorem A. There is a local ell-dimensional
strong stable Lipschitz graph in X through this equilibrium. Every
sufficiently small nonzero point on it gives an exact, nonstationary
population trajectory, stays finite, converges exponentially in X to
`theta_*`, and has strictly decreasing loss tending to the positive
number `L(theta_*)`. Its initial loss can also be chosen below one.
These initial states differ from the prescribed canonical state.

Theorem B applies in particular to point convergence to any compact
subset of S. More generally the local graph contains all orbits
eventually trapped in its neighborhood, even if they do not converge.
For an arbitrary compact K contained in S, mere `dist_H(theta(t),K)->0`
with a nonsingleton omega-limit is not resolved here; Section 8 states
exactly what does follow. No theorem here excludes the one deterministic
canonical initialization from (2), and no theorem supplies all-time
boundedness or precompactness of that trajectory.

## 2. The exact vector field extends to H

For the active inputs write, with `phi=tanh`,

\[
\begin{gathered}
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad
 z_i=Ma_i,\quad h_i=\phi(b_2\cdot z_i),\quad
 f_i=E_2[ch_i],\quad \rho_i=\mu_i(f_i-y_i),\\
 d_i=E_2[b_2c\phi'(b_2\cdot z_i)],\quad
 T_i=\rho_i M^Td_i\in\mathbb R^6,\\
 F_w=-2\sum_i\phi'(w\cdot u_i)(b_1\cdot T_i)u_i,
 \qquad F_c=-2\sum_i\rho_i h_i,\qquad
 F_M=-2\sum_i\rho_i d_i a_i^T.
\end{gathered}
\tag{3}
\]

These are the supplied physical equations; `v'=w'`. All marks are
bounded, tanh and its derivatives are bounded, and the probability
spaces have mass one. Therefore (3) is meaningful at every point of H.
In particular `a_i` is bounded independently of w, `|d_i|<=C||c||_2`,
and both population components of F are bounded functions, even when
v or c themselves are merely square-integrable.

For completeness, F is locally Lipschitz on H. The estimate
`|a_i(w)-a_i(tilde w)|<=C||w-tilde w||_2` follows from the Lipschitz
tanh gate and Cauchy--Schwarz. Matrix multiplication and the upper tanh
map then control `z_i,h_i`; subtraction inside the c pairings controls
`f_i,d_i` on H-balls. The lower gate is Lipschitz in L2, while its
coefficient `b_1 dot T_i` is bounded pointwise and depends locally
Lipschitzly on the state. Subtracting its two factors proves the lower
estimate. These estimates also show continuity of F into X when its
argument varies in X. In fact F is smooth on X, since all gate
Taylor remainders are uniform for bounded perturbations; the unbounded
frozen g occurs only inside gates with bounded derivatives.

The loss is continuously Frechet differentiable on H, with `grad_H L=-F`.
One potentially delicate component is the finite moment map `a_i`:

\[
 Da_i(w)[\zeta]
 =E_1[b_1\phi'(w\cdot u_i)(\zeta\cdot u_i)],
 \qquad
 |a_i(w+\zeta)-a_i(w)-Da_i(w)[\zeta]|
 \le C\|\zeta\|_2^2.
 \tag{4}
\]

The uniform bound on `phi''` proves the remainder by integration.
Moreover

\[
 \|Da_i(w)-Da_i(\widetilde w)\|_{L^2\to\mathbb R^6}
 \le C\|w-\widetilde w\|_2,
 \tag{5}
\]

using the Lipschitz gate and Cauchy--Schwarz. Thus `a_i` is C^(1,1),
a stronger fact than the differentiability needed for the loss.
The upper operations involve a finite vector and an L2 pairing with c,
so ordinary product differentiation gives `grad_H L=-F` from (4).
Along each strong solution,

\[
 L(t)+\int_0^t\|F(\theta(s))\|_{\mathcal H}^2ds=L(0).
 \tag{6}
\]

The local contraction argument in the assigned existence source now
works on H as well. It gives global positive-time solutions from every
H-state. Indeed let `R=sqrt(L(0))`; the weighted Cauchy--Schwarz
inequality gives `sum_i |rho_i(t)|<=R`. Consequently

\[
 \|c(t)\|_2\le\|c(0)\|_2+2Rt,
 \quad \|M'(t)\|_F\le C R\|c(t)\|_2,
 \quad \|v'(t)\|_2\le C R\|M(t)\|_F\|c(t)\|_2.
 \tag{7}
\]

These polynomial bounds preclude finite-time escape. On every bounded
finite interval the field is bounded, giving a Cauchy endpoint and local
continuation. If the initial state belongs to X, the same bounds for
`||c(t)-c(0)||_infty` and `||v'(t)||_infty` show it remains in X at every
finite time and agrees with the canonical bounded-field solution.

For each finite t, `Phi_t:H->H` is continuous, injective, and open, and
has a locally Lipschitz inverse on its open image. To verify the
potentially relevant last two assertions without assuming negative-time
completeness, cover the compact trajectory segment `[0,t]` by finitely
many local existence balls for the reversed equation `x'=-F(x)`.
Nearby terminal points can be solved backward through the same finite
sequence of balls, with Lipschitz dependence from the contraction and
Gronwall estimates. They therefore lie in the image of a neighborhood
of the original initial point. Uniqueness supplies the inverse. The
same statement holds for `Phi_t:X->X`, using the X equation and norms.

## 3. Exactly where H differentiability becomes sufficient

We do **not** assume F is C1 on an H-neighborhood. For a nonlinear scalar
gate, its L2 Nemytskii map can fail to be Frechet differentiable because
small L2 perturbations may have order-one amplitude on small sets. A
pointwise derivative formula alone would not justify a Hilbert
center-stable manifold theorem here.

Instead stationarity supplies the missing estimate. At a critical point
with independent inputs, the first equation in (3) is zero pointwise.
Independence separates its scalar coefficients, so

\[
 \rho_i\phi'(w_*\cdot u_i)(b_1\cdot M_*^Td_{i,*})=0
 \quad\text{a.s. for every }i.
\]

The finite lower gate is strictly positive. The lower feature Gram is
positive definite, by the assigned source's full-dimensional mark-density
argument. Hence

\[
 T_i(\theta_*)=\rho_{i,*}M_*^Td_{i,*}=0
 \quad\text{for every }i.
 \tag{8}
\]

Each coefficient map `T_i:H->R6` is locally C^(1,1). This follows from
(4)--(5): a_i is C^(1,1), all subsequent finite-vector gate maps have
locally bounded first and second derivatives into L-infinity, and their
c dependence is linear in a continuous L2 pairing. Finite sums and
products preserve local C^(1,1). The same argument makes `F_c,F_M`
locally C^(1,1) as maps from H into their respective H components.

Put

\[
 G_i(w)t=\phi'(w\cdot u_i)(b_1\cdot t)u_i,
 \quad t\in\mathbb R^6.
\]

As operators into the lower L2 space, G_i is uniformly bounded and

\[
 \|G_i(w)-G_i(\widetilde w)\|_{\mathbb R^6\to L^2}
 \le C\|w-\widetilde w\|_2.
 \tag{9}
\]

Write `x=theta-theta_*`. Equations (8)--(9) show that the derivative
of the lower component at zero is

\[
 A_w x=-2\sum_i G_i(w_*)DT_i(\theta_*)x.
 \tag{10}
\]

More strongly, its remainder is locally Lipschitz with a constant that
vanishes with the radius. Its i-th summand, apart from -2, is

\[
 [G_i(w)-G_i(w_*)]T_i(\theta)
 +G_i(w_*)[T_i(\theta)-DT_i(\theta_*)x].
 \tag{11}
\]

On an H-ball of radius r centered at theta_*, the first factor difference
in (11) has size `O(r)` and Lipschitz constant O(1); its second factor
has size O(r), because `T_i(theta_*)=0`, and Lipschitz constant O(1).
The product subtraction therefore has Lipschitz constant O(r). The
bracketed Taylor remainder in the second term has Lipschitz constant
O(r) by local C^(1,1) of T_i. The upper and matrix Taylor remainders
have the same bound. Thus, for sufficiently small r, there is one C
independent of r such that

\[
 F(\theta_*+x)=Ax+N(x),\qquad N(0)=0,
 \quad \|N(x)-N(y)\|_{\mathcal H}
       \le Cr\|x-y\|_{\mathcal H}
 \quad(\|x\|,\|y\|\le r).
 \tag{12}
\]

In particular `N(x)=O(||x||_H^2)` and A is the actual Frechet derivative
of F at the equilibrium. Estimate (12), rather than unproved C1
regularity on a neighborhood, is the exact hypothesis used below.

## 4. Finite-rank self-adjoint Jacobian and both signs

On X, differentiating the lower gradient usually creates the
multiplication operator

\[
 \delta w\longmapsto
 -2\sum_i\rho_i(b_1^TM^Td_i)
       \phi''(w\cdot u_i)(\delta w\cdot u_i)u_i.
 \tag{13}
\]

It vanishes at this equilibrium by (8). Every other derivative is a
finite moment contraction or a finite-vector operation. More explicitly,
the range of A is contained in the finite-dimensional subspace V whose
lower component is spanned by

\[
 b_{1,j}\phi'(w_*\cdot u_i)u_i
 \quad(1\le j\le6,\ 1\le i\le m),
\]

whose upper component is spanned by

\[
 h_{i,*},\qquad b_{2,j}\phi'(b_2\cdot z_{i,*})
 \quad(1\le j\le3,\ 1\le i\le m),
\]

and whose matrix component is all of R^(3 x 6). These functions are
bounded and odd. Therefore

\[
 V\subset X,\qquad\operatorname{rank}A\le\dim V
           \le6m+4m+18\le48.
 \tag{14}
\]

The second differential of L on X is symmetric, and `A=-D grad_H L`
there. Since the corresponding bilinear expression is bounded in the
H-norm, symmetry extends from the dense subspace X to H. Equivalently,
(12) and `grad_H L=-F` directly give the second Frechet differential at
the equilibrium. Thus A is bounded and self-adjoint on H. Since
`range A subset V`, self-adjointness implies `A=0` on `V^perp`.
Diagonalizing its finite symmetric restriction to V consequently gives
an orthogonal decomposition

\[
 \mathcal H=E_u\oplus E_s\oplus E_0,
 \tag{15}
\]

where A is strictly positive on E_u, strictly negative on E_s, and zero
on E_0. The first two spaces are finite-dimensional and consist of
bounded fields. Each spectral projection preserves X and is bounded
there: it is a finite sum of H-pairings against bounded eigenvectors;
the zero projection is the identity minus those finite sums. In
particular there is no unverified equivalence of L2 and L-infinity
spectra. The diagonal polynomial identity for A holds in both spaces.

The strict-saddle theorem in `plateau_finite_critical.md`, applied with
independent representatives, supplies an admissible bounded odd direction
q with `D^2 L(theta_*)[q,q]<0`. Hence `<Aq,q>_H>0`, so
`k=dim E_u>=1`. This uses the prior proved landscape result, not a
finite-particle Hessian.

If additionally `L(theta_*)<1`, at least one h_i is nonzero: otherwise
all predictions vanish and binary labels give loss one. Choose a bounded
odd readout direction `delta c=h_i`. Linearity of f in c yields

\[
 D^2L[\delta c,\delta c]
 =2\sum_j\mu_j\langle h_i,h_j\rangle^2>0,
 \tag{16}
\]

because its j=i term is positive. Consequently `<A delta c,delta c><0`
and `ell=dim E_s>=1`. Since `M=0` implies zero predictions and loss one,
any equilibrium with `0<L<1` automatically has `M!=0` and belongs to S.

## 5. A contained center-stable graph argument

Here is the complete graph construction needed for Theorem A. It works
on H with (12), and the same construction works directly on X.

Let `E_cs=E_s+E_0` and let lambda be the smallest positive eigenvalue
of `A|E_u`. Choose an equivalent product norm for the splitting
`E_cs+E_u` such that

\[
 \|e^{A_{cs}t}\|\le1\ (t\ge0),\qquad
 \|e^{-A_ut}\|\le e^{-\lambda t}\ (t\ge0).
 \tag{17}
\]

In H this follows from orthogonality; one can use the sum of component
Hilbert norms. In X decompose the finite eigenspaces with their Euclidean
norms and the zero eigenspace with its inherited X-norm. Equivalence
only changes the constant in (12).

We need a global small-Lipschitz remainder, not a differentiable Banach
bump function. For a small radius r, let
`R_r x=x min(1,r/||x||)` be radial retraction onto the closed r-ball in
the chosen norm. It is 2-Lipschitz: subtract the scalar factors, using
`| ||x||-||y|| |<=||x-y||`, and consider whether each point is inside
the ball. Define `N_hat=N composed with R_r`. It agrees with N inside
the ball, vanishes at zero, and its global Lipschitz constant epsilon
can be made arbitrarily small by (12). A harmless reduction of r ensures
that the entire closed ball is inside the estimate's domain.

Set `gamma=lambda/2`. On the Banach space of continuous paths with norm

\[
 \|x\|_\gamma=\sup_{t\ge0}e^{-\gamma t}
       (\|x_{cs}(t)\|+\|x_u(t)\|),
 \tag{18}
\]

fix `eta in E_cs` and use the integral map

\[
\begin{split}
 x_{cs}(t)&=e^{A_{cs}t}\eta+
       \int_0^t e^{A_{cs}(t-s)}\widehat N_{cs}(x(s))ds,\\
 x_u(t)&=-\int_t^\infty e^{A_u(t-s)}
                                  \widehat N_u(x(s))ds.
\end{split}
\tag{19}
\]

The two integral operator norms in (18) are at most
`epsilon/gamma` and `epsilon/(lambda-gamma)`. Their sum is
`q=4 epsilon/lambda`. Choose epsilon so q<1/2. The map is a contraction,
and its affine term has norm at most `||eta||`. The geometric-series
estimate for successive iterates proves that there is one fixed path
`x_eta`, with `||x_eta||_gamma<=||eta||/(1-q)`. Subtracting the fixed
point equations proves Lipschitz dependence on eta. Differentiating the
integrals verifies the modified ODE. Define

\[
 h(\eta)=x_{\eta,u}(0),\qquad
 \mathcal G_*=\{\eta+h(\eta):\eta\in E_{cs}\}.
 \tag{20}
\]

This is a closed Lipschitz graph of codimension k. In detail, its inverse
parametrization is the bounded projection onto E_cs, and the coordinate
change `eta+u -> eta+[u-h(eta)]` is a homeomorphism with a Lipschitz
inverse. It maps the graph to E_cs. Since E_u has positive dimension,
no open ball lies in E_cs or in the graph. The graph is therefore closed
and nowhere dense.

Every original orbit staying in the closed r-ball for t>=0 is on this
graph. Such an orbit solves the modified ODE and is bounded, so it belongs
to (18). Variation of constants on its unstable component, solved from
a terminal time T back to t, is

\[
 x_u(t)=e^{A_u(t-T)}x_u(T)
       -\int_t^T e^{A_u(t-s)}\widehat N_u(x(s))ds.
\]

The first term tends to zero as T tends to infinity by boundedness and
(17). The integral converges by (18) and `gamma<lambda`. Hence the
orbit satisfies (19), whose fixed point is unique for its initial
center-stable coordinate. This proves the trapping assertion.

The H-graph in (20) also supplies the X-graph asserted in Theorem A.
Indeed its target E_u consists of bounded fields, and the spectral
projections preserve X, so

\[
 \mathcal G_*\cap X
 =\{\eta+h(\eta):\eta\in E_{cs}\cap X\}.
 \tag{21}
\]

The map h is Lipschitz from H into the finite-dimensional E_u, where
H and X norms are equivalent. The continuous embedding `X -> H` then
makes its restriction X-Lipschitz. Its graph is closed and nowhere dense
in X by the same coordinate change. This conclusion does not follow
merely by intersecting an arbitrary H-nowhere-dense set with X; it uses
the graph structure and the bounded unstable eigenvectors.

## 6. Countable coverage and the global basin theorem

For every theta_* in S choose a radius r_* for the preceding trapping
argument, and translate its graph back to that equilibrium. Choose open
H-balls `B_H(theta_*,r_*/2)`, reducing by norm-equivalence constants if
needed so their closures lie strictly inside the trapping neighborhoods.
They cover S. As a subspace of the separable metric space H, S is
second countable and hence Lindelof: a countable base lets one select,
for each base element contained in a cover member, one such member;
those selected members cover S. Thus choose a countable subcover with
centers theta_j, radii r_j and translated graphs G_j.

If `Phi_t(theta_0)->theta_* in S` in H, theta_* belongs to one of these
smaller balls. By convergence there is an integer n such that every
`Phi_t(theta_0)` for t>=n lies in the associated larger trapping
neighborhood of theta_j. The limiting equilibrium need not equal the
chosen center theta_j. The trapping property gives `Phi_n(theta_0) in
G_j`, and therefore

\[
 \mathcal B_{\rm fin}\subset
     \bigcup_{j=1}^{\infty}\bigcup_{n=0}^{\infty}\Phi_n^{-1}(G_j).
 \tag{22}
\]

Each G_j is closed nowhere dense in H. Its inverse image is closed by
continuity of Phi_n and has empty interior because Phi_n is open: an
open subset of the inverse image would have a nonempty open image
contained in G_j. Hence (22) proves Theorem B on H.

For initial states in X, all Phi_n(theta_0) remain in X. Replace G_j by
`G_j intersect X` in (22). Equation (21) makes these closed nowhere
dense in X, and the X flow maps are open. This proves the X conclusion
without any countable covering assumption on X itself. The countable
cover was obtained from H, in exactly the topology where the local
trapping graphs were constructed.

The conclusion is category-theoretic, not an assertion of Lebesgue
measure zero in an infinite-dimensional space. Locally the graph has
one point on each fiber parallel to E_u, so it has zero conditional
k-dimensional Lebesgue measure under any specified distribution with
absolutely continuous conditional laws on those fibers. Such a
transversality assumption would need to be checked for any chosen
random initialization. There is no random initial state in the
canonical exact population problem, and no probabilistic avoidance
claim is used here.

## 7. Strong stable trajectories with positive limiting loss

Fix `0<L(theta_*)<1`. Section 4 gives `ell=dim E_s>=1`. Work now in X,
where the flow is smooth and hence its translated remainder satisfies
(12) in the X norm as well. Split `X=E_s+(E_0+E_u)` and write
`E_cu=E_0+E_u`. Let beta be the smallest absolute value of the negative
eigenvalues. Choose the equivalent split norm so

\[
 \|e^{A_s t}\|\le e^{-\beta t},\qquad
 \|e^{-A_{cu}t}\|\le1\qquad(t\ge0).
\]

Make a radial-retraction remainder as in Section 5 and take
`gamma=beta/2`. This time use decaying paths with norm
`sup_(t>=0) e^(gamma t)(||x_s(t)||+||x_cu(t)||)`. For `xi in E_s`, solve

\[
\begin{split}
 x_s(t)&=e^{A_s t}\xi+
       \int_0^t e^{A_s(t-s)}\widehat N_s(x(s))ds,\\
 x_{cu}(t)&=-\int_t^\infty e^{A_{cu}(t-s)}
                                      \widehat N_{cu}(x(s))ds.
\end{split}
\tag{23}
\]

The two Lipschitz bounds are `epsilon/(beta-gamma)` and
`epsilon/gamma`; choose their sum below one half. The same complete
contraction proof gives a unique path with

\[
 \sup_{t\ge0}e^{\gamma t}\|x_\xi(t)\|_X\le C\|\xi\|_X.
 \tag{24}
\]

Set `h_ss(xi)=x_(xi,cu)(0)`. It is Lipschitz, and its graph over a
small ball in the finite-dimensional E_s has dimension ell. For xi
small enough, (24) keeps the whole path in the region where the cutoff
is inactive. It is therefore a trajectory of the original exact flow
and converges exponentially in X to theta_*.

The graph is tangent to E_s at zero in the explicit sense
`||h_ss(xi)||_X<=C||xi||_X^2`. Indeed smoothness of F on X gives
`||N(x)||_X<=C||x||_X^2` locally; substitute (24) into the second
integral of (23) at zero and integrate `exp(-2 gamma s)`. No general
smooth-manifold theorem is required for this statement.

For xi!=0 the initial point is not theta_*, since its stable projection
is xi. The trajectory cannot pass through an equilibrium at a finite
time: uniqueness would make it constant thereafter, its limiting point
would then have to be theta_*, and backward local uniqueness would
force its initial point to be theta_* as well. Thus its physical speed
is nonzero at every finite time. Equation (6) yields

\[
 L(\theta_*+x_\xi(t))-L(\theta_*)
      =\int_t^\infty\|F(\theta_*+x_\xi(s))\|_{\mathcal H}^2ds>0.
 \tag{25}
\]

The identity follows first on finite intervals, then by X-convergence,
which implies continuity of L. The integrand is continuous and positive
at every finite time. Hence the loss is strictly decreasing and tends
to the strictly positive equilibrium loss. Taking xi small makes its
initial loss less than one by continuity and `L(theta_*)<1`.

The stationary constructions in `rank_one_nonlinear_obstruction.md`
provide an actual theta_* with `0<L<1` for every independent triple,
all positive weights, and binary labels. Applying this section there
therefore gives nonstationary, exact, finite-state positive-plateau
trajectories for each such fixed law. This is a conclusion about other
initial states on the local strong stable graph. It supplies no
intersection between that graph and `(v,c,M)=(0,0,D)`.

## 8. Compact bad sets, extensions, and exact limitations

Several notions of approaching a bad set must remain distinct.

1. **Point convergence into any bad set:** Theorem B covers convergence
   in H to any finite bad equilibrium, including any compact subset K.
   It does not require that the limit be specified in advance.
2. **Eventual trapping:** The same countable union in (22) also covers
   any orbit eventually trapped in one of the countably chosen local
   neighborhoods. If a compact K lies strictly inside one such
   neighborhood, `dist_H(theta(t),K)->0` has this property even without
   point convergence.
3. **Totally disconnected compact K:** If K is compact and totally
   disconnected and `dist_H(theta(t),K)->0`, point convergence follows.
   Indeed the orbit tail is totally bounded: for every epsilon, a
   sufficiently late tail lies within epsilon of a finite epsilon-net
   for K, and the earlier finite segment is compact. Completeness gives
   precompactness of the whole orbit. The omega-limit is nonempty and
   compact. Each closed tail of the continuous orbit is connected, and
   the omega-limit is the nested intersection of these connected
   compact tails, so it is connected. It lies in K, whose only connected
   subsets are singletons. Precompactness then forces convergence to
   that one point. Therefore this compact-set basin is meagre by
   Theorem B. Finite compact sets are included.
4. **An arbitrary compact continuum K of bad equilibria:** Distance
   convergence gives precompactness and a connected omega-limit in K,
   but not a singleton or eventual trapping in one prescribed local
   graph neighborhood. This report supplies neither a gradient
   convergence inequality nor a global invariant graph around such K.
   It therefore does not claim thinness of that larger basin.

Independent inputs are used at the exact point (8). With dependent
inputs, the pointwise lower critical equation need not separate into
individual coefficients, so multiplication operator (13) may survive.
The prior negative-curvature theorem alone then does not provide the
finite-rank spectral split or estimate (12). A proof that (8) still
holds, or an alternative verified spectral/dichotomy argument for the
nonzero multiplier, would be required to extend this route.

Theorems A--C do not upgrade finite-horizon existence to an all-time
bound. Neither bounded H norm nor finite energy dissipation gives
compactness of the infinite-dimensional populations. Escaping positive
loss trajectories remain outside this theorem unless they nevertheless
converge in H to a finite bad equilibrium, which (2) already covers.

For the prescribed canonical trajectory, the assigned landscape report
proves strict initial descent and `L(t)<1` for t>0 for a compatible law.
Therefore any finite positive-loss limiting equilibrium has `M!=0` and
falls under this theorem for independent inputs. A meagre basin can
contain that one deterministic initial state. The strongest unresolved
canonical implication is precisely whether `(0,0,D)` belongs to (22),
together with the separate issue of positive-loss behavior having no
finite bad limit. The strong stable construction proves that exact
nonstationary bad convergence is possible from other states; it cannot
be excluded by a genericity slogan.

## 9. Claim/dependency record

| Claim | Status in this candidate | Exact dependency |
|---|---|---|
| Global exact H flow; agreement with finite-state X flow | Proved here | Bounded marks, exact field, C1 loss and energy; Sections 2--3 |
| Small-Lipschitz linear remainder at a bad equilibrium | Proved here | Independent inputs, positive lower Gram, moment C^(1,1); (8)--(12) |
| Finite-rank self-adjoint Jacobian, unstable dimension >=1 | Proved here using prior candidate | (8), finite ranges, prior strict-saddle theorem |
| Local codimension-k Lipschitz graph | Proved here | Contained radial-retraction and contraction construction |
| Meagre basin of H point-convergence to any finite bad equilibrium | Proved here | Local H graphs, separability of H, open flow maps |
| Same basin meagre relative to bounded-field X | Proved here | Bounded unstable eigenvectors and graph intersection (21) |
| Nonstationary finite-state positive limiting loss from other initial states | Proved here | Positive pure-readout curvature, contained strong-stable contraction; prior bad equilibria supply examples |
| Canonical deterministic initialization avoids bad basins | Open | Requires a direct initialized transversality/invariant argument |
| Arbitrary compact continuum bad-set distance basin is meagre | Open in this route | Requires convergence or a global set-level trapping argument |
| Dependent-input extension | Open in this route | Missing separated critical coefficients or replacement spectral argument |
| All-time compactness and exclusion of positive-loss escape | Open | No such estimate supplied |

All graph and category claims concern the exact population equations,
not finite quadrature, finite neural width, or a discretized optimizer.
