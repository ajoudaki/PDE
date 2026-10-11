# Actual-network positive-time crossing bridge

Author: uniform_time_scope, 2026-10-11. This is a new, internally derived
candidate proof for independent checking; it is not promoted material.
It continues the frozen-comparator route in TEST_PANEL_DENSE_ROUTE.md,
but changes the first activation to remove a sensitivity obstruction.
No experiment, manuscript edit, or Git write is used.

## 1. Claim, scope, and fixed admissible example

Take the canonical network and physical-time gradient flow in
paper/compact.tex, with two hidden layers, two training samples, and input
dimension two. Set
\[
 v_1=e_1,\qquad v_2=e_2,\qquad v_*=(e_1+e_2)/\sqrt2,\qquad
 x_a=\sqrt2v_a,\quad x_*=\sqrt2v_*,
 \qquad y=Y(1,-1)^\top .
 \tag{1}
\]
The only passive test input is \(x_*\). It is not parallel to either
training input, and the training inputs span the whole input space.
Use the layerwise activations
\[
 \phi(z)=z+\tanh z,\qquad \psi(z)=\tanh z.
 \tag{2}
\]
Both are odd, nonaffine, holomorphic on a common sufficiently small strip,
with bounded first derivative there and bounded real derivatives of every
positive order. Unbounded activation values are expressly allowed by the
paper. On the real line, \(1\le\phi'\le2\).

**Claim proved below.** There is a fixed \(Y>0\), independent of width and
satisfying the paper's unchanged small-label cap, and a fixed \(\eta>0\),
such that two independently initialized, actually trained canonical networks
obey
\[
 \liminf_{n\to\infty}\Pr\{
   f_n(1,x_*)>\widetilde f_n(1,x_*),\
   f_n(2,x_*)<\widetilde f_n(2,x_*)\}\ge\eta .
 \tag{3}
\]
Both inequalities in fact have fixed positive margins times \(Y/\sqrt n\).
Consequently the two actual predictions agree at some time in \((1,2)\)
with a probability bounded away from zero. For this single-test panel,
the same-time dense denominator is zero at that interior time.

This disproves a universal positive simultaneous lower profile on the
revised test-only Taylor domain, even with nonparallel queries and full-span
training. Under a ratio convention that treats any zero denominator as
failure, it also defeats the requested uniform ratio conclusion.
Without that convention, (3) alone does **not** prove failure of a ratio
defined only where its denominator is positive: the compressor numerator
at the random crossing has not been analyzed here. Nor does a crossing
at one query make a whole-sphere spatial supremum zero.

The proof needs only a fixed horizon \(T=2\). Since
\(t_*=(2m/\gamma)\log(en)\to\infty\), this is inside the requested interval
eventually. The fitted endpoint is immaterial to the obstruction.

## 2. Exact flow and a coordinate change

Write \(A=W^{(1)}\in\mathbb R^{n\times2}\), \(B=W^{(2)}\), and
\(w\in\mathbb R^n\). For a query \(v\), define lower features, second
preactivations, upper features, and output by
\[
 P_v=\phi(Av),\qquad Z_v=BP_v,\qquad H_v=\psi(Z_v),\qquad
 f_v=n^{-1}w^\top H_v .
 \tag{4}
\]
An activation applied to a vector acts coordinatewise. For training indices
\(a=1,2\), put \(c_a=y_a-f_a\); thus \(c=-r\) in the paper.
Because \(2/m=1\), the exact flow is
\[
\begin{aligned}
 \dot A_{:a}&=c_a\,\phi'(A_{:a})\odot
                 B^\top[w\odot\psi'(Z_a)],\\
 \dot B&=\frac1n\sum_{a=1}^2
                 c_a[w\odot\psi'(Z_a)]P_a^\top,\\
 \dot w&=\sum_{a=1}^2c_aH_a .
\end{aligned}
 \tag{5}
\]
The initial entries of \(A\) are independent \(N(0,1)\), those of \(B\)
are independent \(N(0,1/n)\), all blocks are independent, and \(w(0)=0\).
Nothing is frozen in (5).

Introduce the odd real diffeomorphism
\[
 \tau(z)=\int_0^z\frac{ds}{\phi'(s)},\qquad
 \Gamma=\tau^{-1},\qquad U_{ia}=\tau(A_{ia}).
 \tag{6}
\]
Here \(1/2\le\tau'\le1\), \(1\le\Gamma'\le2\), and \(\Gamma''\)
is bounded. Define the scalar row function for every fixed query by
\[
 F_v(u_1,u_2)
 =\phi\bigl(v_1\Gamma(u_1)+v_2\Gamma(u_2)\bigr).
 \tag{7}
\]
For the three queries in (1), \(F_v\) has linear growth, bounded first and
second derivatives, and is odd under \((u_1,u_2)\mapsto(-u_1,-u_2)\).
In these coordinates \(P_v=F_v(U)\), acting row by row, and the first
equation in (5) is exactly
\[
 \dot U_{:a}=c_a B^\top[w\odot\psi'(Z_a)] .
 \tag{8}
\]
Thus this is a coordinate change of the original flow, not a new optimizer.
It removes the first-layer derivative gate from the hidden vector field.

Use normalized hidden and readout coordinates
\[
 \theta=(U/\sqrt n,B),\qquad \zeta=w/\sqrt n,
 \quad
 \|(\dot U/\sqrt n,\dot B)\|^2
 =n^{-1}\|\dot U\|_{\rm F}^2+\|\dot B\|_{\rm F}^2.
 \tag{9}
\]
All state-space derivatives below are Euclidean derivatives in these
coordinates. For vectors, \(\|b\|_n=\|b\|_2/\sqrt n\).
Constants denoted \(C_T\) may depend on the fixed three queries, the
activations, a fixed initial norm radius, and \(T\), but not on \(n\)
or \(0<Y\le Y_0(T)\). No explicit optimization of these constants is needed.

## 3. A deterministic finite-time tube and first sensitivities

Assume initially
\[
 \|A(0)\|_{\rm op}/\sqrt n\le8,\qquad \|B(0)\|_{\rm op}\le8.
 \tag{10}
\]
There are \(Y_0(T)>0\) and \(C_T<\infty\), uniform in \(n\), such that
on \(0\le t\le T\), for \(0<Y\le Y_0(T)\),
\[
\begin{gathered}
 \|c(t)\|_2\le\sqrt2Y,\quad
 \sum_a|c_a(t)|\le2Y,\quad
 \|w(t)\|_\infty\le2Yt,\\
 \|\theta(t)-\theta(0)\|\le C_TY^2,\quad
 \|B(t)\|_{\rm op}\le9,\quad
 \max_{v\in\{v_1,v_2,v_*\}}\|P_v(t)\|_n\le20.
 \tag{11}
\end{gathered}
\]
The loss decreases along the original gradient flow, proving the first
two bounds. The upper feature is bounded by one coordinatewise, proving
the readout bound directly from (5). Initially
\(\|P_v(0)\|_n\le2\|A(0)v\|_n\le16\).
Within the stated tube,
\[
 \|\dot U\|_{\rm F}/\sqrt n
 \le \sum_a|c_a|\|B\|_{\rm op}\|w\|_n\le36Y^2t,
 \qquad
 \|\dot B\|_{\rm F}\le80Y^2t .
 \tag{12}
\]
Bounded first derivatives of (7) turn small normalized \(U\)-movement
into small lower-feature RMS movement. Choose \(Y_0(T)\) so that the
integrated bounds in (12) are strictly below the tube margins.
The usual first-exit argument proves (11), and local existence extends to
\(T\) because all finite-dimensional parameters remain bounded.
One can shrink \(Y_0(T)\) freely below one.

Let \(G_\theta,G_\zeta\) be the right sides of the ODE in coordinates
(9). Along every trajectory satisfying (11), their derivative blocks obey
\[
 \|D_\theta G_\theta\|\le C_TY^2,\quad
 \|D_\zeta G_\theta\|\le C_TY,\quad
 \|D_\theta G_\zeta\|\le C_TY,\quad
 \|D_\zeta G_\zeta\|\le C_T .
 \tag{13}
\]
Here and below an operator norm acts on the Euclidean/Frobenius direct sum.

For completeness, the dimension-free differentiations behind (13) are as
follows. A unit hidden perturbation satisfies
\[
 \|dP_v\|_n+\|dZ_v\|_n+\|dH_v\|_n\le C_T.
 \tag{14}
\]
The \(B\)-part of \(dZ_v\) uses
\(\|dB\,P_v\|_n\le\|dB\|_{\rm F}\|P_v\|_n\);
the \(U\)-part uses bounded \(DF_v\).
Writing \(D_a=w\odot\psi'(Z_a)\), one has
\[
 \|D_a\|_n\le C_TY,\quad
 \|d_\theta D_a\|_n\le C_TY\|d\theta\|,\quad
 \|d_\zeta D_a\|_n\le C_T\|d\zeta\|,
 \tag{15}
\]
where the middle estimate uses the actual bound \(\|w\|_\infty\le2YT\).
Also \(\|D_\theta c_a\|\le C_TY\) and
\(\|D_\zeta c_a\|\le1\).
Apply the product rule to (8), the second equation of (5), and
\(G_\zeta=\sum_a c_aH_a/\sqrt n\).
For outer products use
\(\|bc^\top/n\|_{\rm F}=\|b\|_n\|c\|_n\).
Each hidden-hidden term consequently contains two factors \(Y\);
each mixed block one; and the readout-readout block none.
The potentially large coordinatewise lower backpropagation multiplier
does not occur in (8).

Keep the initial readout fixed at zero. The derivatives of the trajectory
with respect to its initial hidden coordinates are
\[
 J_\theta(t)=D_{\theta_0}\theta(t),\qquad
 J_\zeta(t)=D_{\theta_0}\zeta(t).
\]
Their initial values are \(I,0\). The variational ODE and (13), followed by
Gronwall on the fixed interval, give
\[
 \|J_\theta(t)\|\le C_T,\qquad
 \|J_\zeta(t)\|\le C_TY,\qquad
 \|J_\theta(t)-I\|\le C_TY^2 .
 \tag{16}
\]
For example first bound the two blocks jointly; the second block is then
\(O(Y)\) by its integral equation, and substituting that bound in the first
block gives the last estimate. Equations (14), (16), and \(w=O(Y)\) in RMS
also show
\[
 \|D_{\theta_0} f_v(t)\|\le C_TY
 \tag{17}
\]
for each of the three queries. These bounds are deterministic for all initial
points in (10). They require only first variational equations.

## 4. Gaussian clipping and two coordinate fourth-moment estimates

Conditioning a Gaussian Poincare inequality on (10) would be invalid.
Instead make the following auxiliary global construction, coupled to the
original initialization. Let \(G_A,G_B\) have independent standard Gaussian
entries of sizes \(n\times2,n\times n\), respectively. Let \(\Pi_8\) be
Euclidean/Frobenius projection onto the closed convex operator-norm ball
of radius eight, of the appropriate matrix size. Set
\[
 A_0^{\,c}=\sqrt n\,\Pi_8(G_A/\sqrt n),\qquad
 B_0^{\,c}=\Pi_8(G_B/\sqrt n).
 \tag{18}
\]
Euclidean projection onto a closed convex set is nonexpansive: its two
variational projection inequalities give
\(\|Px-Py\|^2\le\langle Px-Py,x-y\rangle\).
It also commutes with left and right orthogonal transformations, by uniqueness
and invariance of both the constraint and distance. In particular it respects
the neuron sign symmetries used below.

The map from the raw Gaussian vector \(G=(G_A,G_B)\) to
\[
 \theta_0^{\,c}=(\tau(A_0^{\,c})/\sqrt n,B_0^{\,c})
 \tag{19}
\]
is \(1/\sqrt n\)-Lipschitz, since \(\tau\) is one-Lipschitz.
Every such initial point satisfies (10), so the deterministic results above
hold for all raw Gaussian values.

The clipping is inactive with probability tending to one. One elementary
verification is a fixed \(1/4\)-net on both unit spheres:
\(\|M\|_{\rm op}\le2\max_{u,v\ {\rm in\ nets}}|u^\top Mv|\).
For \(G_B/\sqrt n\), each net bilinear form has variance \(1/n\), so the
probability its operator norm exceeds eight is at most
\(2\,9^{2n}e^{-8n}\), which tends to zero.
For \(G_A/\sqrt n\) the same bound is
\(2\,9^{n+2}e^{-8n}\). Thus (18) agrees with the canonical initialization
outside an event of probability tending to zero.

All random variables in this section refer to the clipped flow. For each
first-layer neuron \(i\), reflect the \(i\)-th row of \(G_A\) and the
\(i\)-th column of \(G_B\) simultaneously. This preserves the raw Gaussian
law. Since \(\phi\) is odd, it negates row \(i\) of \(U(t)\) and column
\(i\) of \(B(t)\), while leaving every \(Z_v(t),H_v(t),w(t),c(t)\)
unchanged. This follows either from (5) and uniqueness or directly from
(8). The projection construction has the same equivariance.

Put \(\Delta U_{ia}(t)=U_{ia}(t)-U_{ia}(0)\).
Equation (16), including the factors \(\sqrt n\) in (9) and
\(1/\sqrt n\) in (19), shows that this is a globally \(C_TY^2\)-Lipschitz
function of \(G\). It is odd under the preceding reflection, so its mean
is zero. Consequently
\[
 \mathbb E|\Delta U_{ia}(t)|^4\le C_TY^8 .
 \tag{20}
\]
Here is the elementary moment implication being used. If a mean-zero function
\(X(G)\) is \(L\)-Lipschitz under standard Gaussian measure, Gaussian
Poincare gives \(\mathbb EX^2\le L^2\). Apply it also to \(X^2\), by
truncation if necessary, to obtain
\[
 \mathbb EX^4
 =\operatorname{Var}(X^2)+(\mathbb EX^2)^2
 \le4L^2\mathbb EX^2+(\mathbb EX^2)^2\le5L^4 .
 \tag{21}
\]
The Gaussian Poincare inequality is the one already established in the
authorized projected-scalar source; all its Lipschitz/Sobolev hypotheses are
verified here.

We need one further initial coordinate estimate. For any ordered pair of
the three queries define
\[
 C_i^0(v,v')
 =\left[B_0^\top
   \{\psi'(Z_v(0))\odot H_{v'}(0)\}\right]_i .
 \tag{22}
\]
As a function of normalized initial hidden coordinates its gradient norm is
at most \(C_T\sqrt n\). Indeed the direct \(B\)-column derivative has norm
at most \(\sqrt n\), because the braced vector is bounded coordinatewise.
The indirect term is bounded by \(\|B_{0,:i}\|\le8\), bounded first and
second derivatives of \(\psi\), and
\(\|dZ_v(0)\|\le C_T\sqrt n\|d\theta_0\|\).
After composition with (19), \(C_i^0\) is globally \(C_T\)-Lipschitz in
\(G\). The same neuron reflection makes it odd. Thus (21) gives
\[
 \mathbb E|C_i^0(v,v')|^4\le C_T .
 \tag{23}
\]
No independence between (20) and (23) is asserted or needed.

The word globally in these Lipschitz claims is justified as follows.
The clipping maps are Lipschitz and differentiable almost everywhere;
the smooth flow exists on a neighborhood of each clipped initial point
with the uniform finite-time estimates above (enlarge the fixed initial
radius slightly if necessary). The a.e. chain-rule derivative bounds are
uniform, and integrating along raw-Gaussian Euclidean line segments gives
the asserted Lipschitz bounds. Equivalently one can approximate the
nonexpansive projections by smooth nonexpansive maps and pass to the limit.

## 5. Two-time feature-kernel gradient estimate

Define the cross-time top-feature kernel and its initialization by
\[
 K_{ab}(s,t)=\frac1nH_a(s)^\top H_b(t),\qquad
 K^0_{ab}=\frac1nH_a(0)^\top H_b(0),\qquad
 \Delta K_{ab}(s,t)=K_{ab}(s,t)-K^0_{ab},
 \tag{24}
\]
where \(a,b\) range over the two training inputs and the single test input.
Equations (11), (14), and the Lipschitz upper activation imply, pathwise,
\[
 |\Delta K_{ab}(s,t)|\le C_TY^2,\quad
 \|P_a(s)-P_a(0)\|_n+
 \|Z_a(s)-Z_a(0)\|_n+
 \|H_a(s)-H_a(0)\|_n\le C_TY^2.
 \tag{25}
\]
These bounds hold uniformly over \(s,t\in[0,T]\).

Regard \(K_{ab}\) first as a function of two independent hidden states.
At its first argument set
\[
 \xi=\psi'(Z_a(s))\odot H_b(t),\qquad C=B(s)^\top\xi .
\]
Its partial gradients with respect to normalized \(U\) and to \(B\) are
\[
 (\partial_1 K_{ab})_{U,i:}
 =\frac1{\sqrt n}\,C_i\,DF_a(U_{i:}(s)),
 \qquad
 (\partial_1 K_{ab})_B=\frac1n\,\xi P_a(s)^\top .
 \tag{26}
\]
Both have norm at most \(C_T\). The other partial gradient has the same
form with the two endpoints exchanged.

Write \(C^0=C^0(a,b)\) from (22) and
\(\xi^0=\psi'(Z_a(0))\odot H_b(0)\).
Bounded coordinates of \(\xi\), (25), and the operator norm bounds give
\[
 \|\xi-\xi^0\|_n\le C_TY^2,\qquad
 \|C-C^0\|_n\le C_TY^2 .
 \tag{27}
\]
For the second inequality split
\(C-C^0=(B(s)-B_0)^\top\xi+B_0^\top(\xi-\xi^0)\).

The \(B\)-gradient difference in (26) is \(O(Y^2)\) in Frobenius norm,
deterministically, by splitting the outer product and using (25), (27).
For the \(U\)-gradient difference, split the row product as
\[
 C_i DF_a(U_i(s))-C_i^0DF_a(U_i(0))
 =(C_i-C_i^0)DF_a(U_i(s))
 +C_i^0[DF_a(U_i(s))-DF_a(U_i(0))].
 \tag{28}
\]
The first term has normalized Euclidean norm \(O(Y^2)\) by (27).
For the second, bounded \(D^2F_a\), (20), (23), and Cauchy--Schwarz give
\[
 \frac1n\sum_{i=1}^n
 \mathbb E\!\left[
 |C_i^0|^2\,
 \|DF_a(U_i(s))-DF_a(U_i(0))\|^2\right]
 \le \frac{C_T}{n}\sum_{i=1}^n
 (\mathbb E|C_i^0|^4)^{1/2}
 (\mathbb E\|\Delta U_i(s)\|^4)^{1/2}
 \le C_TY^4 .
 \tag{29}
\]
The row vector has just two coordinates, so (20) bounds its fourth moment
with another fixed factor. The same argument applies to the other endpoint.

Compose these two partial derivatives with \(J_\theta(s),J_\theta(t)\).
For \(K^0_{ab}\) both endpoint Jacobians are \(I\). Equations (16) and
(26)--(29), using the deterministic \(C_T\) bound on each partial gradient,
prove the essential estimate
\[
 \mathbb E\|D_{\theta_0}\Delta K_{ab}(s,t)\|^2
 \le C_TY^4 ,
 \qquad
 \|D_{\theta_0}K^0_{ab}\|\le C_T .
 \tag{30}
\]
This is uniform over the finite query set and \(s,t\in[0,T]\).
It avoids any assertion that
\(\max_i|\Delta U_i|\), or the operator norm of the diagonal lower-gate
difference, is \(O(Y^2)\). Those unjustified assertions are not used.

## 6. Exact Volterra comparison and the centered cubic remainder

Let \(f_{{\rm RF},a}\) be the readout-only gradient-flow predictor with the
same initialized hidden features, keeping both hidden layers fixed.
The full and frozen predictors have exact integral representations
\[
\begin{aligned}
 f_a(t)&=\sum_{b=1}^2\int_0^t c_b(s)K_{ba}(s,t)\,ds,\\
 f_{{\rm RF},a}(t)&=
 \sum_{b=1}^2\int_0^t c_{{\rm RF},b}(s)K^0_{ba}\,ds,
 \qquad c_{{\rm RF},b}=y_b-f_{{\rm RF},b}.
\end{aligned}
 \tag{31}
\]
The first identity integrates the exact equation for \(w\) in (5),
then takes its inner product with the *current* test feature.
It remains valid when \(a\) is the passive input.

Define \(e_a=f_a-f_{{\rm RF},a}\) for training \(a=1,2\), and
\(R=f_*-f_{{\rm RF},*}\). Since \(c_b-c_{{\rm RF},b}=-e_b\),
\[
 e_a(t)=\sum_{b=1}^2\int_0^t
 [-e_b(s)K^0_{ba}+c_b(s)\Delta K_{ba}(s,t)]\,ds .
 \tag{32}
\]
The same right side, with \(a=*\), is \(R(t)\).
As \(|K^0_{ba}|\le1\), \(|c_b|\le\sqrt2Y\), and (25) holds,
finite-dimensional integral Gronwall gives
\[
 \max_{a=1,2}\sup_{t\le T}|e_a(t)|
 +\sup_{t\le T}|R(t)|\le C_TY^3 .
 \tag{33}
\]
This absolute estimate is only an intermediate step, not the crossing bridge.

Differentiate (32) with respect to normalized initial hidden coordinates:
\[
\begin{aligned}
 D_{\theta_0}e_a(t)=\sum_{b=1}^2\int_0^t[
 &-K^0_{ba}D_{\theta_0}e_b(s)
   -e_b(s)D_{\theta_0}K^0_{ba}\\
 &+\Delta K_{ba}(s,t)D_{\theta_0}c_b(s)
   +c_b(s)D_{\theta_0}\Delta K_{ba}(s,t)]\,ds .
\end{aligned}
 \tag{34}
\]
All quantities are smooth functions of their finite-dimensional initial
hidden state on the tube; thus differentiation under the finite-time
integral is justified. In this identity,
\(\|D_{\theta_0}c_b(s)\|\le C_TY\) by (17).

Take the \(L^2\) norm over the raw Gaussian initialization, with values in
the Euclidean gradient space. Minkowski's inequality, (25), (30), (33),
and the preceding derivative bound show
\[
 A(t)\le C_T\int_0^t A(s)\,ds+C_TY^3,
 \qquad
 A(t)=\max_{a=1,2}
  \bigl(\mathbb E\|D_{\theta_0}e_a(t)\|^2\bigr)^{1/2}.
 \tag{35}
\]
Gronwall gives \(A(t)\le C_TY^3\). Apply (34) with \(a=*\) and the
training errors on its right side to conclude
\[
 \mathbb E\|D_{\theta_0}R(t)\|^2\le C_TY^6,
 \qquad 0\le t\le T .
 \tag{36}
\]
All expectations in (30)--(36) use the clipped initial points from (19).

Finally compose with the \(1/\sqrt n\)-Lipschitz map (19), and use Gaussian
Poincare on the original standard Gaussian vector:
\[
 \operatorname{Var}(R^{\,c}_n(t))
 \le \mathbb E\|\nabla_G R^{\,c}_n(t)\|^2
 \le \frac{C_TY^6}{n}.
 \tag{37}
\]
The function is globally Lipschitz, for example with the coarser bound
\(C_TY/\sqrt n\) obtained directly from (17) and the analogous frozen
bound, so the required Gaussian Sobolev integrability is automatic.
The sharper estimate (36) is used only after taking expectation.

For two independent initializations the mean of their remainder difference
cancels, regardless of the value of \(\mathbb ER^{\,c}_n(t)\). Thus
\[
 \mathbb E|R^{\,c}_n(t)-\widetilde R^{\,c}_n(t)|^2
 \le \frac{2C_TY^6}{n}.
 \tag{38}
\]
On the event that both clippings are inactive, these are precisely the
actual-minus-frozen remainders for the canonical Gaussian networks.
Chebyshev and the vanishing clipping failure therefore imply, for every
fixed \(b>0\) and fixed \(t\le T\),
\[
 \limsup_{n\to\infty}
 \Pr\{\sqrt n\,|R_n(t)-\widetilde R_n(t)|>bY\}
 \le \frac{2C_TY^4}{b^2}.
 \tag{39}
\]
This is the required width-uniform centered \(O(Y^3/\sqrt n)\) bridge.
It is not the false assertion that a fixed nonzero \(Y\) makes the
root-width remainder tend to zero in probability.

## 7. Admissibility and nondegenerate two-time frozen fluctuations

The frozen fluctuation argument of TEST_PANEL_DENSE_ROUTE.md, Section 3,
extends to (2). Details for the changed activation are supplied here.

The first-layer augmented population Gram on \(v_1,v_2,v_*\) is positive
definite. Indeed, a zero second moment of a linear combination implies,
by Gaussian full support and continuity,
\[
 a\phi(g_1)+b\phi(g_2)
       +c\phi((g_1+g_2)/\sqrt2)=0
 \quad\hbox{for all }(g_1,g_2)\in\mathbb R^2 .
\]
The mixed derivative is
\((c/2)\phi''((g_1+g_2)/\sqrt2)=0\).
Since \(\phi''=\tanh''\) is not identically zero, \(c=0\);
varying the remaining coordinates then gives \(a=b=0\).
Consequently the second-layer preactivation triple has a nondegenerate
Gaussian law. Its tanh feature triple has full support on \((-1,1)^3\).

Oddness and symmetry give the top population training Gram and test column
\[
 Q=qI_2,\qquad k=r(1,1)^\top,\qquad 0<q<1,\quad r>0.
 \tag{40}
\]
To check the strict positivity of \(r\), the covariance of two strictly
increasing centered Gaussian transforms is positive at positive input
correlation. In this case it follows directly by differentiating the
Gaussian covariance expectation in its cross-covariance: Gaussian integration
by parts gives derivative \(\mathbb E[g'(Z_1)g'(Z_2)]>0\) for
\(g=\phi\), and then for \(g=\psi\); at zero correlation the covariance
is zero by oddness. Both derivative products are strictly positive.
The initial training-test correlation is \(1/\sqrt2>0\).
The two training coordinates are independent at each population Gaussian
layer, and the activations are centered, so their cross-covariance stays
zero. Thus the paper's gap is \(\gamma=q>0\) and \(m/\gamma=2/q\ge1\).

Let \(Q_n,k_n\) be the top initialized empirical training Gram and test
column for the *unclipped canonical* network. Set \(u=(1,-1)^\top\) and
\[
 A_n=\sqrt n(k_n-k)^\top u,\qquad
 B_n=\sqrt n k^\top(Q_n-qI_2)u .
 \tag{41}
\]
This pair converges to a centered Gaussian \((A,B)\) with positive-definite
covariance. Here is the full finite-depth argument needed in this example.
The first augmented empirical Gram is an average of iid row-products with
finite moments of every order, since \(\phi\) has linear growth under
Gaussian input. The multivariate iid CLT therefore applies. Conditional
on this Gram, the second-layer preactivation rows are iid Gaussian with
that covariance. On a compact positive-definite neighborhood of its limit,
the map
\[
 S\longmapsto\mathbb E[\psi(Z)\psi(Z)^\top],\qquad Z\sim N(0,S),
\]
is continuously differentiable: derivatives of the Gaussian density are
an integrable polynomial times a Gaussian, uniformly on the neighborhood,
and the activation products are bounded. The conditional empirical row
noise has a Gaussian CLT uniformly on this neighborhood; expand its
conditional characteristic function, whose cubic remainder is uniformly
bounded because \(\psi\) is bounded. That characteristic function
converges in probability to a deterministic Gaussian characteristic function.
Multiplying by bounded characteristic functions of the first-layer
fluctuation shows that the new Gaussian noise is independent of the
first-layer limit. The delta method for the displayed covariance map
then gives a centered Gaussian final Gram fluctuation, whose covariance
includes the final conditional noise covariance as an additive
positive-semidefinite term.

For the pair (41), the corresponding final row-noise variables are
\[
 H_*(H_1-H_2),\qquad r(H_1^2-H_2^2).
 \tag{42}
\]
Their covariance is positive definite. A constant linear combination would
be constant on the whole open cube, by full support and continuity.
Setting \(H_1=H_2\) makes the constant zero. Fixing \(H_1\ne H_2\)
and varying \(H_*\) makes the first coefficient zero, after which varying
\(H_1^2-H_2^2\) makes the second coefficient zero because \(r>0\).
Earlier-layer Gaussian covariance contributions cannot cancel this
strictly positive contribution.

For \(h_t(s)=(1-e^{-ts})/s\), with its entire continuation at zero, the
frozen readout solution is exactly
\[
 f_{{\rm RF},n}(t,x_*)=Y k_n^\top h_t(Q_n)u .
 \tag{43}
\]
Since \(k^\top u=0\), expansion at the scalar matrix \(qI_2\) gives,
jointly at finitely many fixed positive times,
\[
 \frac{\sqrt n}{Y}f_{{\rm RF},n}(t,x_*)
 \ \Longrightarrow\ h_t(q)A+h_t'(q)B .
 \tag{44}
\]
The quadratic matrix-expansion remainder is \(o_{\mathbb P}(1)\) after
multiplication by \(\sqrt n\), because the Gram fluctuations are tight.
For independent initializations the Gaussian pair in the limit is
replaced by its independent-copy difference, doubling its covariance.

The coefficient vectors at times one and two are linearly independent:
\[
 -\frac{h_t'(q)}{h_t(q)}
 =\frac1q-\frac{t}{e^{qt}-1}
 \tag{45}
\]
is strictly increasing in \(t>0\). Its derivative is positive because
\((qt-1)e^{qt}+1>0\), whose derivative as a function of \(qt>0\)
is \(qt\,e^{qt}>0\) and whose value at zero is zero.
Therefore the two-time independent frozen difference
\(g_{{\rm RF},n}=f_{{\rm RF},n}-\widetilde f_{{\rm RF},n}\) has a
nondegenerate two-dimensional Gaussian limit after normalization by
\(\sqrt n/Y\). For any fixed \(b>0\) this gives
\[
 \Pr\{\sqrt n\,g_{{\rm RF},n}(1)>2bY,\
          \sqrt n\,g_{{\rm RF},n}(2)<-2bY\}
 \longrightarrow p_b>0 ,
 \tag{46}
\]
where \(p_b\) is independent of \(Y\). The limiting Gaussian density is
everywhere positive and the event boundary has zero probability.

## 8. Transfer, label choice, and precise conclusion

Fix \(T=2\) and, for example, \(b=1\). Fix once and for all a strictly
positive label amplitude satisfying
\[
 Y\le Y_0(2),\qquad
 Y\le\frac q2\,\beta^{-60},\qquad
 \frac{4C_2Y^4}{b^2}<\frac{p_b}{2}.
 \tag{47}
\]
Such a choice exists. The second condition is exactly the paper's
small-label cap for \(L=2,m=2,\gamma=q\), with \(\beta\) determined
only by the fixed activations. All of (1), (2), and (47) are fixed before
width tends to infinity.

Apply (39) at times one and two and take a union bound. With limiting
probability at least \(p_b-4C_2Y^4/b^2>p_b/2\), the event in (46) holds
and both actual-minus-frozen independent-copy corrections have magnitude
at most \(bY/\sqrt n\). On that event the actual difference
\(g_n(t)=f_n(t,x_*)-\widetilde f_n(t,x_*)\) satisfies
\[
 g_n(1)>bY/\sqrt n,\qquad g_n(2)<-bY/\sqrt n.
 \tag{48}
\]
Continuity of the actual finite-dimensional flow gives a zero of \(g_n\)
in \((1,2)\). This proves (3) with any \(\eta<p_b/2\).

The canonical small-label fitting theorem, if required as part of the
background setting, holds on an event tending to one and can be intersected
with this event without changing its positive limiting probability.
The proof itself used no frozen substitution for the actual flow:
freezing appears only in the exactly coupled reference predictor, and
(37)--(39) control the centered difference on the root-width scale.

**What this does and does not settle.** The fully trained crossing bridge is
closed for this particular admissible two-layer example, with a lower
strictly monotone odd activation and a bounded odd upper activation.
The original all-tanh example in TEST_PANEL_DENSE_ROUTE.md is not separately
claimed to have this bridge. The result supplies no theorem for arbitrary
full-span endpoint anti-concentration, no all-activation temporal CLT,
and no proof about the compressor numerator at a crossing.

## 9. Scope and direct checks

Scientific inputs were restricted to the authorized joint-study route,
time-comparison and early-error notes; the canonical compact-paper setup;
and the authorized prior-study Gaussian/Poincare and frozen-route chain.
The new bridge is derived explicitly above. No other active route note or
independent-review report was read.

Direct checks cover the mobility factors in (5), exact coordinate change,
finite-time tube, all four first-Jacobian blocks, clipping equivariance and
probability, the two coordinate fourth moments, normalized factors in
kernel gradients, differentiation of the exact Volterra equation, positive
final row covariance, and the fixed rather than width-dependent label choice.
The unresolved ratio-numerator issue is expressly retained in Sections 1
and 8. Independent checking remains separate from these author checks.

Source HEAD: ef8362764b4eb8144d7af8d6f8db080fdaaf82ca.

