# Coupled instability of zero-row, zero-readout population equilibria

Status: internally derived, not independently reviewed or promoted. Frozen
route report, 2026-09-19.

## Result and scope

Fix one of the canonical orders \(p=1,2,3\), its exact Gaussian mark laws,
its prescribed ridge, and its frozen mark columns \(b_1,b_2\). Let

\[
 \mathcal H=L^2(\lambda_1;\mathbb R^2)\times L^2(\lambda_2)
                  \times\mathbb R^{r_2\times r_1},
 \qquad
 \|(w,c,M)\|_{\mathcal H}^2=\|w\|_2^2+\|c\|_2^2+\|M\|_F^2.
\]

The order of the blocks throughout this report is \((w,c,M)\). The first
population includes the frozen Gaussian seeds and marks, exactly as in
(H40.C5). Fields remain arbitrary measurable population fields in these
spaces; they are not restricted to the finite mark span. Both directions
of the middle action use the same matrix and its actual transpose. Time
is the unhalved-loss physical time.

Let \(\mu\) be any probability law on \(S^1\times[-Y,Y]\), with \(Y<\infty\),
and suppose

\[
 m=\int yu\,d\mu(u,y)\ne0.                                      \tag{1}
\]

For every nonzero \(M_0\), the state

\[
 e_{M_0}=(0,0,M_0)                                               \tag{2}
\]

is a suboptimal equilibrium of the exact population closure. Its loss is
\(\int y^2d\mu>0\). It has \(k=\operatorname{rank}M_0\) linearly unstable
directions, as many strictly stable directions, and an infinite-dimensional
zero eigenspace. More substantively:

1. A sufficiently small closed physical-norm ball around (2) has a
   forward-trapped set contained in a 1-Lipschitz graph over the orthogonal
   complement of the \(k\)-dimensional unstable subspace. The graph is
   over a subset; existence of a graph point for every complementary
   coordinate is not asserted.
2. Every nonzero initial displacement in the strict unstable cone leaves
   that ball in a quantitatively bounded time.
3. The basin consisting of all states whose full trajectories converge in
   \(\mathcal H\) to **some** equilibrium (2), with \(M_0\ne0\), is meagre
   in \(\mathcal H\). In particular this entire family has no open
   attracting basin.
4. Locally, after fixing the complementary coordinate, the trapped set
   contains at most one unstable coordinate. It consequently has zero
   measure for any law whose unstable-coordinate conditional laws have
   densities with respect to \(k\)-dimensional Lebesgue measure.

These conclusions are about the full coupled population dynamics. They
are not obtained from a scalar restriction or from nearby lower losses
alone. No Hilbert-space smooth stable-manifold theorem is used. The result
does not settle general equilibria outside the two families analyzed here,
the fully zero state, convergence without a limiting equilibrium, or the fate
of the prescribed single initialization \((g,0,D_p)\). Meagreness is not a
claim of zero probability for an arbitrary Gaussian law on \(\mathcal H\).

Scientific inputs read: the complete assigned portions of
`docs/global_nonlinear.md`, C.4.7.10.B, C.1, and D.3, and
`docs/NOTATION.md`. No other study or prior landscape result was used.
This is theoretical analysis; no numerical experiment was run.

## 1. Exact equations and a global population flow

Write \(U_\ell v=b_\ell^Tv\), so \(U_\ell^*h=E_\ell[b_\ell h]\).
The bounded marks satisfy \(\|U_\ell\|\le1\). With

\[
 \begin{split}
 a(u)&=U_1^*\tanh(w\cdot u),\qquad Z(u)=U_2Ma(u),\\
 H(u)&=\tanh Z(u),\qquad f(u)=E_2[cH(u)],\\
 d(u)&=U_2^*[c\operatorname{sech}^2Z(u)],\qquad
 q(u)=U_1M^Td(u),
 \end{split}
\]

the canonical equations are precisely

\[
 \begin{split}
 F_w&=2\int(y-f)\operatorname{sech}^2(w\cdot u)q(u)u\,d\mu,\\
 F_c&=2\int(y-f)H(u)\,d\mu,\\
 F_M&=2\int(y-f)d(u)a(u)^T\,d\mu.                 \tag{3}
 \end{split}
\]

These equations extend uniquely to a forward-global continuous flow
\(\Phi_t\) on the full \(\mathcal H\). Here is the needed verification,
since the stated source continuation class uses bounded \(w-g,c\).

For states in any bounded \(\mathcal H\)-ball, subtraction in \(a\)
uses the Lipschitz bound for tanh and Cauchy--Schwarz. Bounded \(b_2\)
then controls \(Z\) and its difference in \(L^\infty(\lambda_2)\),
uniformly in \(u\). This controls \(H\), \(d\), and \(f\). Bounded
\(b_1\) controls \(q\) in \(L^\infty(\lambda_1)\). In the row equation,
subtract the gate using
\(\|\operatorname{sech}^2(w\cdot u)-
\operatorname{sech}^2(\widetilde w\cdot u)\|_2
\le2\|w-\widetilde w\|_2\), and subtract its bounded coefficient
separately. These estimates show that \(F\) is Lipschitz on every bounded
\(\mathcal H\)-ball. The integral-map contraction therefore supplies
local existence, uniqueness and continuous dependence in this Hilbert
norm.

The prediction map is continuously Fréchet differentiable in this norm.
For its only non-pointwise scalar contraction, the Taylor remainder
\(\left|\tanh(s+h)-\tanh s-\operatorname{sech}^2(s)h\right|
\le C|h|^2\) gives the required integrated \(O(\|\delta w\|_2^2)\)
bound. Its derivative is continuous by the displayed gate estimate;
the other operations are finite-dimensional smooth maps or bounded
linear pairings. Thus the loss is \(C^1\), (3) is its negative physical
gradient, and

\[
 \mathcal L'(t)=-\|F_w\|_2^2-\|F_c\|_2^2-\|F_M\|_F^2.           \tag{4}
\]

Put \(\ell=\sqrt{\mathcal L(0)}\). As long as a solution exists,

\[
 \|F_c\|_2\le2\ell,\qquad
 \|F_M\|_F\le2\ell\|c\|_2,\qquad
 \|F_w\|_2\le2\ell\|M\|_{\rm op}\|c\|_2.                     \tag{5}
\]

Indeed \(\int|y-f|d\mu\le\ell\), \(|a|\le1\),
\(|d|\le\|c\|_2\), and the \(U_\ell\) are contractions. Integrating
(5) first for \(c\), then \(M\), then \(w\), bounds the state and its
speed on each finite interval. A finite maximal time would have a
strong limit by the speed bound, from which local existence continues
the solution. This proves the asserted forward-global flow.

## 2. The full linearization and its spectrum

At (2), \(a=H=f=d=q=0\), so every block of (3) vanishes, even for each
single training example separately. The linearization at (2), on a
displacement \(x=(v,z,B)\), is

\[
 \begin{split}
 (A x)_w&=2[U_1M_0^TU_2^*z]m,\\
 (A x)_c&=2U_2M_0U_1^*(v\cdot m),\\
 (A x)_M&=0.                                           \tag{6}
 \end{split}
\]

The matrix displacement therefore participates in the nonlinear
equations; it is a center direction at first order, not a frozen
parameter of the nonlinear argument.

For \(p=1,2,3\), the retained features are exactly the polynomial cores
with dimensions \((5,3),(15,6),(35,10)\). Their raw Gram matrices are
positive definite: the core coordinates have positive densities on
their open cubes, and their Chebyshev products are linearly independent
polynomials. Consequently

\[
 S_\ell=U_\ell^*U_\ell=L_\ell^{-1}G_\ell L_\ell^{-T}>0.          \tag{7}
\]

Define \(T:L^2(\lambda_2)\to L^2(\lambda_1;\mathbb R^2)\) by

\[
 Tz=2[U_1M_0^TU_2^*z]m.
\]

Its actual Hilbert adjoint is \(T^*v=2U_2M_0U_1^*(v\cdot m)\),
so (6) is the selfadjoint finite-rank block
\(\left(\begin{smallmatrix}0&T\\T^*&0\end{smallmatrix}\right)\)
plus the zero matrix block. To identify its rank and nonzero spectrum,
write \(U_\ell=V_\ell S_\ell^{1/2}\), where \(V_\ell\) is an
isometry, and use the isometry \(h\mapsto h m/|m|\) in the lower
population. The nonzero singular values of \(T\) are exactly

\[
 \sigma_j=2|m|\,s_j(S_2^{1/2}M_0S_1^{1/2}),
 \qquad 1\le j\le k=\operatorname{rank}M_0.                     \tag{8}
\]

Each singular pair supplies eigenvectors with eigenvalues \(+\sigma_j\)
and \(-\sigma_j\). On the orthogonal complement of these finite
subspaces \(A=0\). In particular \(k\ge1\). Let
\(\mathcal H_+\) be its positive eigenspace,
\(\mathcal H_- =\mathcal H_+^\perp\), and \(P_+,P_-\) their
orthogonal projections. The minus subscript here includes center
directions. Set \(\lambda=\min_{1\le j\le k}\sigma_j>0\). Then

\[
 \langle x_+,Ax_+\rangle\ge\lambda\|x_+\|^2,
 \qquad \langle x_-,Ax_-\rangle\le0.                            \tag{9}
\]

The sign pairing in (6)--(8) depends on using the actual transpose and
the physical population metric. Replacing the reverse map independently
would invalidate this calculation.

## 3. A small Lipschitz remainder in the physical topology

There exist \(C<\infty\) and \(r_0>0\), depending on the fixed order,
marks, \(M_0\), and \(Y\), such that for every \(0<r\le r_0\),

\[
 F(e_{M_0}+x)=Ax+R(x),\qquad R(0)=0,
 \quad
 \|R(x)-R(\widetilde x)\|_{\mathcal H}
       \le Cr\|x-\widetilde x\|_{\mathcal H}
 \quad(\|x\|,\|\widetilde x\|\le r).                            \tag{10}
\]

This estimate is stronger than pointwise differentiability at the
equilibrium and is the regularity needed below. It avoids asserting
\(C^1\) regularity of the row Nemytskii operator on an \(L^2\)
neighborhood.

For details, put \(a^{\rm lin}_v(u)=U_1^*(v\cdot u)\). Bounded
\(b_1\), the bound
\(|\operatorname{sech}^2s-1|\le2|s|\), and Cauchy--Schwarz give,
uniformly in \(u\),

\[
 \begin{split}
 |[a_v-a^{\rm lin}_v]-[a_{\widetilde v}-a^{\rm lin}_{\widetilde v}]|
   &\le C(\|v\|_2+\|\widetilde v\|_2)\|v-\widetilde v\|_2,\\
 \|\operatorname{sech}^2(v\cdot u)-1\|_2&\le2\|v\|_2,\\
 \|\operatorname{sech}^2(v\cdot u)
       -\operatorname{sech}^2(\widetilde v\cdot u)\|_2
   &\le2\|v-\widetilde v\|_2.                                  \tag{11}
 \end{split}
\]

On the radius-\(r\) ball, \(a=O(r)\) and \(Z=O(r)\) in the upper
supremum norm, whereas \(c=O(r)\) in \(L^2\). Repeatedly using
\(XY-\widetilde X\widetilde Y=(X-\widetilde X)Y+
\widetilde X(Y-\widetilde Y)\), (11), and bounded derivatives of
tanh gives decompositions

\[
 \begin{split}
 H&=U_2M_0a^{\rm lin}_v+R_H,\\
 d&=U_2^*z+R_d,\\
 q&=U_1M_0^TU_2^*z+R_q,
 \end{split}                                                   \tag{12}
\]

where each remainder vanishes at zero and has Lipschitz constant
\(Cr\), respectively in \(L^\infty(\lambda_2)\), the finite coefficient
norm, and \(L^\infty(\lambda_1)\). For instance the middle-matrix
correction in \(H\) is \(U_2B a\), a product of two \(O(r)\) factors;
the other lower-layer correction is covered by the first line of (11).
The correction in \(d\) is \(U_2^*[z(\operatorname{sech}^2Z-1)]\);
bounded upper marks and the supremum bound on \(Z\) control both terms
of its difference. The correction in \(q\) additionally includes
\(U_1B^Td\). These facts establish the stated bounds for every term
in (12), including changes in \(B\).

Also \(f=O(r^2)\) and has Lipschitz constant \(Cr\). The matrix
velocity is a product of \(d=O(r)\) and \(a=O(r)\), so has Lipschitz
constant \(Cr\). The only remaining population-valued product is the
row gate times the linear part of \(q\). Subtracting this product and
using the last two lines of (11) bounds

\[
 \big\|[\operatorname{sech}^2(v\cdot u)-1]q^{\rm lin}(z)
  -[\operatorname{sech}^2(\widetilde v\cdot u)-1]
           q^{\rm lin}(\widetilde z)\big\|_2
 \le Cr\|x-\widetilde x\|_{\mathcal H}.                         \tag{13}
\]

The remaining factors in (3) are bounded or already have small
Lipschitz constants. Integration against the bounded labels now proves
(10). In particular, the first-order term is exactly (6).

Integrating the gradient along a line from \(e_{M_0}\), (10) also gives

\[
 \mathcal L(e_{M_0}+x)=\mathcal L(e_{M_0})
       -\tfrac12\langle x,Ax\rangle+O(\|x\|^3).                \tag{14}
\]

A sufficiently small nonzero positive-eigenvector displacement lowers
loss, proving suboptimality. The following argument supplies the
stronger dynamical statement.

## 4. Difference cones, escape, and local thinness

Choose \(r>0\) small enough in (10) that \(Cr\le\lambda/8\).
Consider two solutions while both stay in
\(\overline B(e_{M_0},r)\). For their difference \(\delta\), write

\[
 \alpha=\|P_+\delta\|,\qquad \beta=\|P_-\delta\|,
 \qquad \delta'=A\delta+\rho,
 \quad \|\rho\|\le\varepsilon(\alpha+\beta),
 \quad\varepsilon=Cr\le\lambda/8.                             \tag{15}
\]

By (9), whenever \(\alpha>0\),

\[
 \alpha'\ge\lambda\alpha-\varepsilon(\alpha+\beta).             \tag{16}
\]

The squared-norm difference has an ordinary derivative, even at
\(\beta=0\), and satisfies

\[
 (\alpha^2-\beta^2)'
   \ge2\lambda\alpha^2-2\varepsilon(\alpha+\beta)^2.             \tag{17}
\]

At a nonzero boundary point \(\alpha=\beta\), the right side is at
least \(\lambda\alpha^2>0\). Uniqueness prevents two distinct
solutions from meeting. Thus a difference starting with
\(\alpha>\beta\) cannot first cross the cone boundary: at a first
crossing the derivative in (17) would be nonpositive. Inside the cone,
(16) yields

\[
 \alpha(t)\ge e^{\lambda t/2}\alpha(0).                         \tag{18}
\]

Define the closed local forward-trapped set

\[
 \mathcal T_{M_0,r}=\{x\in\overline B(e_{M_0},r):
       \Phi_t(x)\in\overline B(e_{M_0},r)\text{ for all }t\ge0\}.
                                                                    \tag{19}
\]

It is closed because it is the intersection of the closed preimages
of the ball at nonnegative rational times, and trajectories are time
continuous. If two points of (19) had \(\alpha(0)>\beta(0)\), (18)
would contradict \(\alpha(t)\le2r\). Hence every pair satisfies

\[
 \|P_+(x-\widetilde x)\|\le\|P_-(x-\widetilde x)\|.             \tag{20}
\]

This is the claimed 1-Lipschitz graph property. Since
\(\dim\mathcal H_+=k\ge1\), the graph cannot contain an open ball:
two sufficiently close points separated only in an unstable direction
would violate (20). Together with closedness, this makes (19) nowhere
dense.

For the one-trajectory escape assertion, compare a trajectory to the
constant equilibrium solution. An initial displacement with
\(\|P_+(x-e_{M_0})\|>\|P_-(x-e_{M_0})\|\) must leave the radius-\(r\)
ball no later than

\[
 \frac{2}{\lambda}\log\frac{r}{\|P_+(x-e_{M_0})\|}.              \tag{21}
\]

An endpoint equality can be read as reaching the boundary; any
slightly larger time forces departure. Arbitrarily small positive
eigenvector perturbations therefore establish Lyapunov instability.

For the measure statement, use the orthogonal product coordinates
\(\mathcal H_-\times\mathbb R^k\). A section of (19) at any fixed
\(\mathcal H_-\) coordinate contains at most one point by (20).
Its \(k\)-dimensional Lebesgue measure is zero. Since (19) is Borel,
integration of these zero sections proves the asserted nullity for
arbitrary complementary-coordinate distributions and absolutely
continuous unstable-coordinate conditional distributions. This is a
specified local measure statement, not an unspecified infinite-dimensional
Lebesgue measure.

## 5. A global Baire-category basin statement

Every finite-time map \(\Phi_t\) is injective and open on
\(\mathcal H\). Injectivity follows by local uniqueness backwards
along an existing finite trajectory. For openness, fix a trajectory
segment and a bounded ball strictly containing it. The vector field is
Lipschitz on that ball. Starting close enough to the segment's final
point, the backwards integral equation and the bound
\(\|\delta(s)\|\le e^{L(t-s)}\|\delta(t)\|\) keep the perturbed
backwards solution inside the ball throughout the finite segment.
Choosing the final discrepancy smaller still makes its initial point
belong to any prescribed neighborhood of the reference initial point.
Thus the forward image of that neighborhood contains a neighborhood
of the reference final point. This requires no global backwards
existence.

For every \(M_0\ne0\), choose one radius \(r(M_0)\) as above. The
balls \(B(e_{M_0},r(M_0)/2)\) cover the equilibrium family (2).
This family is homeomorphic to a subset of a finite-dimensional matrix
space and hence has a countable base. Choosing, for each basic set
contained in a member of the cover, one such member produces a
countable subcover, with centers \(e_j\) and radii \(r_j/2\).
Let \(\mathcal T_j\) be the corresponding radius-\(r_j\) sets (19).

If \(\Phi_t(x)\to e_{M_\infty}\) for some \(M_\infty\ne0\), choose
a covering half-radius ball containing this limit. Convergence implies
that, for some integer \(n\), the complete tail starting at time \(n\)
lies in its full-radius closed ball. Therefore

\[
 \{x:\exists M_\infty\ne0,\ \Phi_t(x)\to e_{M_\infty}\}
 \subseteq\bigcup_{j=1}^{\infty}\bigcup_{n=0}^{\infty}
                          \Phi_n^{-1}(\mathcal T_j).             \tag{22}
\]

Each set on the right is closed by continuity. It has empty interior
because \(\Phi_n\) is open and \(\mathcal T_j\) has empty interior.
Thus (22) is meagre. The Baire theorem in the needed form says that
in a complete metric space, a countable union of closed sets of empty
interior contains no nonempty open set. The space \(\mathcal H\) is a
finite product of Hilbert spaces and is complete, so the theorem
applies and rules out an open attracting basin for the whole family.

No passage from local conditional nullity to global Gaussian nullity
is made: a nonlinear flow map does not automatically preserve a chosen
infinite-dimensional probability law or its null sets.

## 6. Concrete scope and remaining obstruction

Condition (1) holds for the equally weighted binary two-point law

\[
 (u,y)=(e_1,+1),(e_2,-1),\qquad m=(e_1-e_2)/2.
\]

It also holds for the genuinely three-point, mixed-label law with
equal weights at

\[
 (e_1,+1),\quad ((3/5,4/5),+1),\quad(e_2,-1),
 \qquad m=(8/15,-1/15).
\]

Both use distinct circle inputs without conflicting labels. More
generally every law in the source's class \(V_\rho\) has
\(\|m-(e_1-e_2)/2\|\le2\rho\), so has \(m\ne0\). The proof itself
does not need a support cap, atomicity, or a bound on the atom count.

The hypothesis \(M_0\ne0\) cannot simply be removed from this argument.
At \(w=c=M=0\), (6) is zero and (8) supplies no positive spectral gap;
the leading prediction is trilinear. Likewise, when \(m=0\), this
particular linearization vanishes. Neither case is proved attractive
or repulsive here. Other positive-loss critical points may also have
different geometry. The established obstruction is exactly that the
nonzero-middle, zero-row, zero-readout family cannot provide a
topologically substantial deterministic basin in the stated physical
population topology.

The full \(L^2\) neighborhood is material. The equilibrium \(w=0\)
does not satisfy a uniform bound on \(w-g\) for the unbounded Gaussian
seed \(g\). Section 1 explicitly verifies the actual closure equations
on the broader physical Hilbert state space; no claim of finite-time
reachability from the prescribed initialization is substituted for this
state-space basin result.

## 7. The complementary zero-middle, zero-readout family

The same elementary cone argument also applies when the first field is
arbitrary and the middle matrix and readout vanish. Fix
\(w_*\in L^2(\lambda_1;\mathbb R^2)\), set

\[
 a_*(u)=U_1^*\tanh(w_*\cdot u),\qquad
 v_*=\int ya_*(u)\,d\mu(u,y),
 \qquad v_*\ne0,                                                \tag{23}
\]

and put \(e_*=(w_*,0,0)\). This is again an equilibrium with zero
prediction and loss \(\int y^2d\mu\). Every individual-example gradient
vanishes there. For a displacement \(x=(h,z,B)\), the exact
linearization is

\[
 (A_*x)_w=0,\qquad
 (A_*x)_c=2U_2Bv_*,
 \qquad
 (A_*x)_M=2(U_2^*z)v_*^T.                                      \tag{24}
\]

To check the physical adjoint, the map \(T_*B=2U_2Bv_*\) obeys

\[
 \langle T_*B,z\rangle_{L^2}
   =2(U_2^*z)^TBv_*
   =\langle B,2(U_2^*z)v_*^T\rangle_F.
\]

The nonzero singular values of \(T_*\) are
\(2|v_*|\sqrt{\lambda_j(S_2)}\), one for each
\(1\le j\le r_2\). Thus (24) has exactly \(r_2\) positive and \(r_2\)
negative eigenvalues. The row directions and the remaining coefficient
directions are center directions. In particular the unstable dimension
is \(3,6,10\) at orders \(1,2,3\), respectively.

The small Lipschitz remainder (10) holds at \(e_*\) as well. Indeed
\(a(w)-a_*=O(\|h\|_2)\) with a uniform Lipschitz bound. On a small
displacement ball, the upper preactivation is \(Z=U_2B a_*=O(r)\)
plus a correction with Lipschitz constant \(Cr\). Hence
\[
 H=U_2B a_*+R_H,\qquad d=U_2^*z+R_d,\qquad f=O(r^2),
\]
with the same small Lipschitz remainder bounds as before. The row
coefficient \(q=U_1B^Td\) is quadratic in the small variables.
Subtracting its product with the gate gives a term with Lipschitz
constant \(Cr\); subtracting the gate itself costs at most
\(2\|h-\widetilde h\|_2\) and multiplies an \(O(r^2)\) coefficient.
The first-order parts of the readout and middle equations are precisely
(24). No differentiability of the pointwise gate as an \(L^2\)-valued
map is needed.

Consequently all local graph, conditional-nullity, finite-time escape,
and suboptimality conclusions of Sections 3--4 hold at every state
satisfying (23), with this new unstable dimension and spectral gap.
This conclusion can apply even when \(m=0\); its condition is (23),
not (1).

There is also a global family basin statement. The population laws
\(\lambda_1,\lambda_2\) are Borel probability laws on the finite
dimensional mark/seed spaces in (H40.C5). Simple functions from the
countable algebra of rational rectangles are dense in their \(L^2\)
spaces, so \(\mathcal H\) is separable. A separable metric space has a
countable base: balls centered at a countable dense set with positive
rational radii suffice. Its subsets inherit a countable base.
The half-radius neighborhoods supplied above therefore admit a
countable subcover of the family

\[
 \{(w_*,0,0):v_*\ne0\}.
\]

Repeating (22) and the openness argument proves that the basin of
strong convergence to any member of this family is meagre in the
full physical Hilbert space. This remains a topological assertion
globally and the stated conditional measure assertion locally.
No assertion is made about the degenerate members with \(v_*=0\).
