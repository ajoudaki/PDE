# Finite deterministic reduction for endpoint curvature certificates

Author: /root/energy_route, 2026-09-12.
Status: **proved approximation/error reduction; no curvature sign evaluated;
no E₀ population theorem**. This continuation leaves the frozen route files
and task families unchanged.

The endpoint derivative and cubic can be reduced to finitely many deterministic
Gaussian-program integrals with an explicit, checkable error bound. The useful
error bound is a posteriori: it includes soft tails of two derivative fields
of the finite approximation. These tails themselves have finite Gaussian
integral certificates. No ambient L² Hessian, Lᵖ boundedness of the initialized
action, refreshed source, or training experiment is needed. This is not an
evaluated certificate, and it does not determine the sign of the cubic.

## 1. Scope and exact object

Scientific inputs: the neutral contract, the frozen ROUTE_GEOMETRY.md, the
author's frozen ROUTE_ENERGY.md, and the previously allowed established source
sections listed in §10. No other current follow-up was read. The earlier
internal cross-check of COMPARISON_TRANSFER.md is part of this agent's prior
context, but supplies no scientific ingredient to this reduction.

Use exactly the original-start two-hidden-layer tanh GF and selected episode
of the contract. All following endpoint constructions are analysis of its
established fitted two-anchor reference, not a restart of an actual network.
The complete first row, raw metric, actual initialized action A_0, true
adjoint, readout, all source history, and both anchor constraints are retained.

At the endpoint let r=F_*-q, v=integral r g p d rho,
beta=M^(-1)G* v and b=Pi v. Geometry (G12)–(G14) gives

\[
\mathcal C_p(r)=
\left\langle b,\int r(u)\dot g_b(u)p(u)d\rho(u)-\dot G_b\beta\right\rangle,
\tag{C1}
\]
\[
\mathsf D'_0 a=-2\int a(u)\dot d_b(u)p(u)d\rho(u),\quad
\dot d_b=\Pi\dot g_b+\dot\Pi_b g,\quad
\langle r,\mathsf K'_0r\rangle_p=-4\mathcal C_p(r).
\tag{C2}
\]

A dot with subscript b is differentiation at the fixed endpoint in that
admissible controlled direction; it does not differentiate the residual in
(C1). The actual initial velocity is -2b, accounting for (C2)'s factor -2.
The finite approximations below can use any bounded fixed r, including
polarization probes. Such probes are algebraic directions at the same
reference; they are not alternative trained tasks.

## 2. A finite reference approximation with explicit raw error

There is an elementary deterministic approximation independent of task
performance: the established two-anchor feature-clock Euler program.

Use S=10, m_0=1/10, and the clock coordinates X with w_a=J(X_a,g_a),
J_X=sech²J. On 0<=s<=S, the exact clock path and its unforced Euler
program obey c∞<=10, ||K||_HS<=50, and ||A||<=52. Enlarge the action and
readout-L² bounds to

\[
a=53,\quad c=11,\quad H=10,\quad
L=\sqrt{1+c^2(1+a^2)},\quad V=595,\quad \Lambda=28674.
\tag{C3}
\]

Here and below L is this deliberately coarse certificate bound, not a
replacement value for the sharper L of C.4.10.

For completeness, in the clock sum metric
sum_a||delta X_a||_2+||delta K||_HS+||delta c||_2,
the three velocity estimates C.4.5.2 R10 have summed coefficients at most

\[
s\,a(a+1)+(c+a)/2=2862s+32,\quad
c+1+2s(a+1)=12+108s,\quad a+1=54.
\]

They are all at most Lambda on [0,10]. The speed is at most
a c+c+1=595. Since J is one-Lipschitz in X, this metric bounds raw
state distance. Integrating the exact equation over each Euler step and
summing its Lipschitz defect gives, for maximal feature step h,

\[
\delta_h=\tfrac12\Lambda V S h\,e^{\Lambda S},
\qquad
\max_j\|\theta_j^h-\theta(s_j)\|_{raw}\le\delta_h.
\tag{C4}
\]

The proof is the scalar discrepancy recurrence with one-step defect
Lambda V h_j²/2. No unknown smoothness constant enters (C4).

Choose a grid index minimizing the absolute *reference* fitting residual
|b_j^h-1|, where b_j^h=(f_j^h(e_1)-f_j^h(e_2))/2.
The exact reference has b'(s)>=m_0 and first b=1 at s_dagger<=10.
It also has raw speed at most L and b'<=L² on this interval.
A grid point within h of s_dagger therefore has exact fitting error <=L²h.
Prediction error at a grid point is <=L delta_h, because the line segment
between the two bounded states preserves the bounds in (C3).
Thus the chosen index has exact reference fitting error at most
L²h+2L delta_h. Monotonicity of b yields

\[
\delta_{\rm end}(h)=
(1+2L^2/m_0)\delta_h+L^3h/m_0,\qquad
\|\theta_j^h-\theta_\dagger\|_{raw}\le\delta_{\rm end}(h).
\tag{C5}
\]

If each computed b_j^h has certified error at most epsilon_b, minimizing
computed absolute residual adds at most 2epsilon_b to the bound for
|b_j^h-1|. Add 2L epsilon_b/m_0 to (C5). This fitting criterion depends
only on the fixed reference; it never selects a task by advantage.

All inequalities concern exact finite Gaussian programs on the retained
common carrier. Numerical quadrature, if later undertaken, encloses their
scalar integrals. A numerical covariance approximation is an integration
device; it is not asserted to be a new exact neural initialized action.

## 3. Explicit uniform moments needed by the certificate

The reference clock proof also gives uniform Gaussian-plus-bounded
representations for current passive Q(u) queries of these Euler programs,
including the retained history. An explicit coarse specialization of the
fresh-pulse proof C.4.5.2 R10–R16 is

\[
E=\exp(54S+1431S^2),\quad
P=(a+1)S+1/2,\quad K_q=\max(1,2Sa),
\]
\[
B_Q=2S P K_q E+S c^2+2S,\qquad
Q(u)=\zeta(u)+B(u),\quad
\operatorname{Var}\zeta(u)\le c^2,\quad |B(u)|\le B_Q.
\tag{C6}
\]

To see the constants, the preceding clock Lipschitz coefficients are bounded
by 54+2862s. Their integrated amplification is E. A reverse-answer pulse
changes a clock coordinate by h_j/2 times its amplitude. A forward-answer
pulse has immediate clock/action/readout discrepancy at most h_j P times
its amplitude, and a subsequent passive delta query is K_q-Lipschitz in
that sum metric. The resulting old beta coefficients are bounded by
h_j P K_q E. Summing two anchor slots over length S gives 2S P K_q E.
The learned rank terms cost S c²; the current response costs at most 2S.
The small-forcing argument is legitimate on the enlarged bounds a=53,c=11,
because the unforced bounds are 52 and 10. The readout supremum survives
forcing, as every readout increment is bounded tanh. Source extraction takes
width first at a fixed forced program and then forcing to zero, exactly as in
the contained proof; no derivative of a singular unforced value law is inferred.

The same proof applies to a passive u: its lower clock-feature derivative has
norm at most one, and its upper gate subtraction has the same bound.
Consequently define, for the few even orders needed,

\[
Q_j=c\bigl(\mathbb E|G|^j\bigr)^{1/j}+B_Q
\quad(j=2,4,8),\qquad
W_j=\|g\|_{L^j(\mathbb R^2)}+S Q_j.
\tag{C7}
\]

Gaussian moments here are explicit finite products; for example
E G^8=105 and E|g|^8=384. These bound Q queries and full rows in the
reference and Euler programs, uniformly in input and mesh. Passing to the
reference flow follows by the strong clock completion already established.
They are enormous but numerically specified constants.

Crucially, (C6)–(C7) do **not** imply that A_0 acts boundedly on L⁴ or L⁸.
Derivative answers such as A_0[phi'(w.u)b_w.u] therefore are treated below
through L² and certified tails, not an invented Lᵖ operator estimate.

## 4. Base state, force and projection error bounds

Let theta be the endpoint and bar theta an exact finite reference program
with raw distance at most delta<=1. All estimates are on the same retained
carrier and use (C3),(C7). Put

\[
Z_1=1+a,\quad D_1=1+2HZ_1,\quad Q_1=c+aD_1,
\]
\[
e_Z^0=Z_1\delta,\quad e_\delta^0=D_1\delta,\quad
e_Q^0=Q_1\delta,
\]
\[
e_g=(Q_1+D_1+c+Z_1)\delta+\sqrt2 Q_4\sqrt\delta.
\tag{C8}
\]

Direct factor subtraction gives the errors for Z², upper delta and Q in L²
shown above, and sup_u||g(u)-bar g(u)||<=e_g.
The only extra product is a changed first gate times bar Q:
its L⁴ norm is at most sqrt(2) sqrt(delta), paired with Q_4.
Also interpolation gives

\[
e_{Q,4}\le(e_Q^0)^{1/3}(2Q_8)^{2/3},\qquad
e_{g_w,4}\le e_{Q,4}+2^{1/4}Q_8\delta^{1/4}.
\tag{C9}
\]

The interpolation exponent satisfies 1/4=(1/3)/2+(2/3)/8.
For the other term use the bounded first-gate difference in L⁸ and bar Q
in L⁸. These quantitative estimates are stronger than merely saying the
direction belongs to L⁴.

Let e_v be a certified raw error between v and bar v, including task
quadrature, and V_* an upper bound on both raw force norms. The state part
of e_v is at most L² delta+B_0 e_g, with B_0=sqrt(10)+1.
The finite spatial quadrature contribution is discussed in §7.
For the anchors

\[
e_G=\sqrt2 e_g,\qquad e_M=4L e_g.
\]

A finite Gram computation can certify a common positive lower bound gamma
for M and bar M: it suffices that a certified lower eigenvalue for bar M
exceeds e_M+gamma. No numerical value of the established k is presumed.
Since M>0 and e_g→0, this test eventually succeeds under refinement.

With both gaps at least gamma, define

\[
e_\Pi=2\sqrt2 e_g/\sqrt\gamma,\qquad
B_\beta=\sqrt2L V_*/\gamma,
\]
\[
e_\beta=
\frac{\sqrt2L}{\gamma}e_v+
\frac{\sqrt2e_g}{\gamma}V_*+
\frac{4L e_g}{\gamma^2}\sqrt2L V_*,
\qquad e_b=e_v+e_\Pi V_*.
\tag{C10}
\]

These follow from the exact projection difference identity and
M^(-1)-bar M^(-1)=M^(-1)(bar M-M)bar M^(-1).
Use any common bound

\[
U\ge \|r p\|_{L^1(\rho)}+\sqrt2|\beta|,
\quad
U\ge \|\bar r\,\bar p_{\rm quad}\|_{\rm TV}+\sqrt2|\bar\beta|.
\tag{C11}
\]

For example U=2(c+1)+sqrt(2)B_beta is sufficient for nonnegative
midpoint density weights on the stipulated class, and for positive normalized
density nets whose maximum is at most two. Then both b and
bar b have row-Lʲ norm at most U Q_j, middle-HS norm at most Uc and
readout supremum at most U.

The row-L⁴ direction error is separately controlled. If e_(v_w,4) bounds
the force row error, then

\[
e_{b_w,4}\le e_{v_w,4}+\sqrt2 Q_4e_\beta+
                         \sqrt2 B_\beta e_{g_w,4}.
\tag{C12}
\]

The state part of e_(v_w,4) is bounded by L delta Q_4+B_0e_(g_w,4).
Thus the stronger direction norm needed for curvature is obtained from
available moments, not from raw-L² convergence alone.

## 5. Explicit derivative comparison: the two necessary tail terms

The following bound is a reusable local certificate. It is stated for a
direction z and approximation bar z; use z=b and bar z=bar b in this task.
Assume certified bounds

\[
\|z-\bar z\|_{raw}\le e_z,\quad
\|z_w-\bar z_w\|_4\le e_{z,4},
\]
\[
\|z_w\|_j,\|\bar z_w\|_j\le Z_j\ (j=2,4,8),\quad
\|z_K\|,\|\bar z_K\|\le Z_K,\quad
\|z_c\|_\infty,\|\bar z_c\|_\infty\le Z_c.
\]

For b one may take e_z=e_b, e_(z,4) from (C12),
Z_j=UQ_j, Z_K=Uc and Z_c=U.

Define the exact fields, all at the same passive input,

\[
a_z=\phi'(w.u)(z_w.u),\quad B_z=z_K H^1+A a_z,
\]
\[
\delta_z=z_c\phi'(Z^2)+c\phi''(Z^2)B_z,\quad
Q_z=z_K^*\delta+A^*\delta_z,
\]
\[
(\dot g_z)_w=\{\phi''(w.u)(z_w.u)Q+\phi'(w.u)Q_z\}u,
\quad
(\dot g_z)_K=\delta_z\otimes H^1+\delta\otimes a_z,
\quad
(\dot g_z)_c=\phi'(Z^2)B_z.
\tag{C13}
\]

The symbols B_z and Q_z here are derivative fields, not the network
increment or the base Q query. Their barred versions are formed using the
exact finite program and its true adjoint.

Set the norm bounds

\[
B_* =Z_K+aZ_2,\quad D_* =Z_c+2HB_*,
\quad Q_*=cZ_K+aD_*,
\]
\[
G_* =2Z_4Q_4+Q_*+D_*+cZ_2+B_*.
\tag{C14}
\]

They bound B_z, delta_z, Q_z and dot g_z in L²/raw norm. For a cutoff R>=1
let tau_R(X)=||X 1_(|X|>R)||_2 and use certified upper bounds on the two
finite-program tails tau_R(bar B_z) and tau_R(bar Q_z). Define

\[
e_a=e_z+\sqrt2 Z_4\sqrt\delta,\quad
e_B=e_z+Z_K\delta+\delta Z_2+a e_a,
\]
\[
e_D=e_z+2Z_c e_Z^0+2H e_B+
        R(2\delta+6H e_Z^0)+4H\tau_R(\bar B_z),
\]
\[
e_{Q_z}=c e_z+Z_K e_\delta^0+\delta D_*+a e_D,
\]
\[
e_{\rm row}=2Q_4 e_{z,4}+2Z_4e_{Q,4}
 +\sqrt{24}Z_8Q_8\sqrt\delta+e_{Q_z}
 +2R\delta+\tau_R(\bar Q_z),
\]
\[
e_{\rm middle}=e_D+D_*\delta+e_\delta^0 Z_2+c e_a,
\quad
e_{\rm readout}=e_B+2R e_Z^0+\tau_R(\bar B_z),
\]
\[
e_{\dot g}=e_{\rm row}+e_{\rm middle}+e_{\rm readout}.
\tag{C15}
\]

Then ||dot g_z(u)-dot bar g_(bar z)(u)||_raw<=e_(dot g).

Here is the product audit establishing all terms. Derivatives of tanh obey
|phi'|<=1, |phi''|<=2, |phi'''|<=6; the last bound follows from
phi'''=-2sech⁴+4tanh²sech². The first two lines of (C13) give e_a,e_B
by action/rank subtraction. In delta_z, subtract the varying derivative
field first. The remaining coefficient
c phi''(Z²)-bar c phi''(bar Z²) has L² norm at most
2delta+6H e_Z^0 and supremum at most 4H. Splitting bar B_z at R gives
the last two terms in e_D. The actual adjoint gives e_(Q_z) without
any Lᵖ claim.

In the differentiated lower product, the direction and Q changes cost
2Q_4e_(z,4) and 2Z_4e_(Q,4). Its gate difference has L⁴ norm at most
sqrt(24)sqrt(delta), while bar z_w bar Q is bounded in L⁴ by Z_8Q_8.
The remaining first-gate multiplier times bar Q_z is split at R, giving
2Rdelta+tau_R(bar Q_z). Rank subtraction proves the middle line.
Finally the upper gate times bar B_z is split at R for the readout line.

This exposes the real missing moment if one tries to use only an a priori
power-law continuity bound: (C7) alone gives neither an L⁴ bound on B_z
nor on Q_z. The explicit tail terms in (C15) are needed. Raw-state
convergence plus a bound on derivative norms is not a quantitative
replacement for them.

## 6. Projection derivative, full D'_0, and the cubic error

Let dot G have columns dot g_b(e_a). Then
||dot G||<=sqrt(2)G_* and its error is at most sqrt(2)e_(dot g).
Put

\[
e_{B_G}=\sqrt2e_g/\gamma+\sqrt2L e_M/\gamma^2,
\]
\[
e_{\dot\Pi}=2\left[
e_\Pi\sqrt2G_*/\sqrt\gamma+
\sqrt2e_{\dot g}/\sqrt\gamma+\sqrt2G_* e_{B_G}\right].
\]

Subtract the factors in dot Pi=-Pi dot G B_G* -B_G dot G* Pi.
Since ||B_G||<=1/sqrt(gamma), this proves the displayed error.
Consequently the projected derivative error is

\[
e_{\dot d}=e_\Pi G_*+e_{\dot g}+L e_{\dot\Pi}
                    +(2\sqrt2G_*/\sqrt\gamma)e_g.
\tag{C16}
\]

After spatial discretization error e_x is added, (C2) yields
||D'_0-D'_(certificate)||<=2(e_(dot d)+e_x).
For example represent the finite approximation by a cellwise constant
raw feature map dot bar d(u_i) and integrate input functions against p on
each cell; this is a finite-rank operator on the actual prediction space.
Its output vectors are finite Gaussian-program vectors. An operator-norm
error follows from the L²(p rho) norm of their feature-map errors, in
particular from their uniform error. No finite-rank operator-norm
approximation to A_0 itself is required or asserted.

If errors e_D0 and e_Dprime are certified for D_0 and D'_0, and their
norms are bounded by L and L_prime (enlarged to cover both approximations),
factor subtraction gives

\[
\|\mathsf K'_0-\widetilde{\mathsf K'_0}\|
\le2(L e_{Dprime}+L_{prime}e_{D0}).
\tag{C17}
\]

For the cubic, let
a=integral r dot g_b p -dot G_b beta and compute its finite counterpart
bar a with the same chosen reference and task quadrature. If e_r bounds
the endpoint residual approximation and e_I bounds the remaining spatial
integration error for r dot g_b, then

\[
e_{a}\le G_*e_r+(B_0+\sqrt2B_\beta)e_{\dot g}
                         +\sqrt2G_*e_\beta+e_I,
\]
\[
|\mathcal C_p(r)-\langle\bar b,\bar a\rangle|
\le e_b\|\bar a\|+(\|\bar b\|+e_b)e_a.
\tag{C18}
\]

For e_r one may use L delta. All norms or contractions on the right can
be enclosed by finite Gaussian integrals, or replaced by (C11),(C14).
The anchor subtraction and true adjoint remain present. Dropping either
would certify a different curvature.

## 7. Spatial integration with checkable errors

The required integral errors do not require a hidden continuum oracle.
The base fields have explicit input-Lipschitz bounds. With W_j,Q_j from
(C7), a possible bound for g in raw norm is

\[
L_x=ac+2Ha^2W_2+2W_4Q_4+2HaW_2+cW_2+aW_2.
\tag{C19}
\]

This is the same factor subtraction as NSC18–NSC19 on the coarse ball.
Prediction Lipschitz constant is at most caW_2.
The task's q and p have declared finite Lipschitz bounds. A midpoint
angular mesh of radius ell therefore has raw force quadrature error at most
ell times the Lipschitz bound of (bar f-q)bar g p.

For the force row in L⁴, use Q input difference in L² bounded by
2Ha²W_2|u-v|, interpolate with 2Q_8, and bound the changed first gate
using W_8 Q_8. This gives the explicit modulus

\[
\omega_{g_w,4}(\ell)=
(2Ha^2W_2\ell)^{1/3}(2Q_8)^{2/3}
 +(2W_8Q_8+Q_4)\ell .
\tag{C20}
\]

Subtracting the scalar residual and density factors supplies the row
quadrature error needed in (C12).

For derivative fields, the two tails can likewise be controlled by a finite
spatial net. First

\[
\operatorname{Lip}_{L^2}(B_z)
\le Z_KW_2+a(Z_2+2W_4Z_4)=:L_B.
\tag{C21}
\]

At net radius ell, the elementary inequality

\[
\tau_R(X)\le2\|X-Y\|_2+2\tau_{R/2}(Y)
\tag{C22}
\]

bounds the supremum of bar B_z tails by 2L_B ell plus twice the maximum
net tail. It is deliberately loose: split {|X|>R} according to
|Y|<=R/2 and its complement and use the triangle inequality.

For Q_z use Q_z=z_K*delta+A*delta_z and the same cutoff product rule as
(C15). An explicit spatial modulus is

\[
\omega_{Q_z}(\ell;R)=
2HZ_K aW_2\ell+
a\{2Z_c aW_2\ell+2HL_B\ell+
                6HR aW_2\ell+4H t_B(R)\},
\tag{C23}
\]

where t_B(R) is any uniform upper bound on tau_R(bar B_z).
The coefficient difference of phi'' has bound 6aW_2ell in L²;
its supremum is at most four. Formula (C23) follows by subtracting
delta_z at the paired inputs. Apply (C22) again to Q_z using this
modulus and finite net tails.

These formulas provide uniformly valid tails for (C15). For a spatial error
on dot g itself, repeat its three-factor subtractions in (C13):
a_z has L² modulus (Z_2+2W_4Z_4)ell; B_z uses (C21);
delta_z and Q_z use the displayed cutoff bounds; the lower triple product
uses z_w in L⁸, Q in L⁸, w in L⁴/L⁸ and (C20). The extra explicit
input vector contributes G_*ell. Every operation is a sum, product,
Hölder estimate or one of the two cutoff rules already quantified above.
One may compute an error by this finite list of rules, rather than
asserting an unspecified Lipschitz constant for dot g.

To be explicit about the lower triple product, its spatial difference is
bounded by

\[
2Z_4\,\omega_{Q,4}(\ell)
+2Q_4Z_4\ell+6W_4Z_8Q_8\ell,
\quad
\omega_{Q,4}(\ell)=(2Ha^2W_2\ell)^{1/3}(2Q_8)^{2/3}.
\]

For phi'(w.u)Q_z add omega_(Q_z)(ell;R), plus
2R W_2ell+tau_R(Q_z at the comparison input).
For phi'(Z²)B_z add L_Bell+2R aW_2ell+tau_R(B_z).
For the middle rank block add the delta_z modulus, D_*W_2ell,
2HaW_2ell Z_2 and c(Z_2+2W_4Z_4)ell.
Thus e_x and e_I in §6 can be bounded without leaving an undefined
derivative modulus.

## 8. Deterministic evaluation of each fixed finite certificate

At every fixed reference/time/input mesh, append to the *same* finite
source program its gradients, the finite signed force/rank sums, the
direction fields in (C13), and the required actual forward/transpose calls.
The initialized source groups remain those of the original graph; every
new answer includes all response contractions with earlier opposite
orientation calls. The graph is finite before any integration accuracy is
chosen. A_0 and A_0* are not replaced by independent maps.

The fixed-program source formulas reduce the required scalar contractions to
finite-dimensional Gaussian expectations, recursively in graph order.
The clock J is a computable monotone inverse of
F(z)=z/2+sinh(2z)/4; bisection gives interval values because F'>=1.
At a fixed graph, values and the finitely many named derivatives required
by action response have computable polynomial envelopes in the finite
Gaussian root/source list. Bounded tanh derivatives, bounded readout,
finite rank expansions and a finite number of products give those envelopes
by induction. Root derivatives of J are unnecessary for source extraction;
on compact root sets its needed numerical sensitivity is bounded by exp(2|g|).
This is a fixed-graph calculation, not a claim uniform in derivative order
or a growing finite-width transcript.

Singular source covariances do not defeat certified evaluation. For positive
semidefinite m-by-m matrices A,B and delta=||A-B||_F, one elementary bound is

\[
\|A^{1/2}-B^{1/2}\|_F
\le(2\sqrt m+1/2)\sqrt\delta.
\tag{C24}
\]

For delta>0, insert A+delta I and B+delta I. Each regularization changes
its square root by at most sqrt(delta) in operator norm. The difference X
of the regularized square roots solves
(A+delta I)^(1/2)X+X(B+delta I)^(1/2)=A-B.
Diagonalizing the two factors separately bounds its Frobenius norm by
delta/(2sqrt(delta)); the triangle inequality proves (C24).
At delta=0 the statement is exact. Thus covariance errors and expected
response coefficient errors can be propagated causally even at rank loss.
An approximate covariance may be projected onto the positive semidefinite
cone; its Frobenius discrepancy from the true covariance is at most twice
its original discrepancy, by the minimizing property of the projection.
This is solely an error-controlled Gaussian integral representation.

Here is a concrete integration bound. If a fixed integrand has envelope
C(1+|G|)^d on k independent standard Gaussians, its expectation outside
the cube |G_i|<=R is at most

\[
C[\mathbb E(1+|G|)^{2d}]^{1/2}(2k)^{1/2}e^{-R^2/4}.
\tag{C25}
\]

This follows from Cauchy–Schwarz and the Gaussian coordinate tail union bound.
The moment is explicitly bounded using
E|G|^(2d)=product_(j=0)^(d-1)(k+2j), proved by Gaussian integration by parts.
On the cube, a computed Lipschitz bound and cell diameter give the usual
weighted Riemann error. Gaussian cell probabilities can themselves be
enclosed by integrating the exponential series with its explicit remainder.
All coefficients and square-root errors are propagated through the finite
graph before accepting the interval.

For tails use a continuous integrand:

\[
\tau_R(X)\le2\left(\mathbb E[(|X|-R/2)_+^2]\right)^{1/2}.
\tag{C26}
\]

The right side is a finite Gaussian expectation with the same polynomial
envelope, and can be enclosed by (C25) and compact quadrature. No discontinuous
hard-cutoff integration or random simulation is needed.

## 9. Completion, uniform families, and the exact remaining limitation

A refinement procedure is now fully specified at the level of certified
errors: choose a reference mesh and fitting error, compute (C5), certify a
Gram gap by (C8)–(C10), choose task/spatial meshes and cutoffs, enclose all
finite Gaussian contractions and soft tails, then use (C15)–(C18).
Accept an approximation only when its displayed error is below the requested
tolerance. Enumerating finer meshes, larger cutoffs and higher integration
accuracies avoids presuming a useful numerical rate.

Why can this procedure reach arbitrary tolerance? The raw endpoint error
tends to zero explicitly by (C5). Base Q converges in L⁴ by (C9);
b_w converges in L⁴ by (C12). Therefore a_b and B_b converge strongly
in L² by their first two equations in (C13).
For delta_b the bounded multiplier
c phi''(Z²) converges in probability, with a fixed uniform supremum.
Split against one fixed limiting B_b in L² and then remove that tail;
this proves strong L² convergence of delta_b. Actual bounded adjunction
then gives Q_b convergence in L². The lower product converges by its L⁴
factors and bounded-multiplier continuity. This proves the derivative
convergence rather than assuming it.

Strongly convergent L² families have uniformly small L² tails: split a
late member against its limit, using (C22), and cover the finitely many
early members separately. Consequently a cutoff can first make the two
limiting tail errors arbitrarily small, after which sufficiently fine meshes
make the cutoff-amplified algebraic errors small. The exact finite
expectations can be enclosed to arbitrary accuracy by §8. A dovetailed
search over these choices therefore terminates. This proves existence of
an effective certificate procedure, but supplies no practical operation count
or modest a priori cutoff. Every accepted finite output has the explicit
error bound above.

Uniformity over the *unchanged* geometry family can be handled by deterministic
finite nets rather than outcome-based target selection. At the fixed endpoint
write a signed input density h=r p. The map h↦b_h is linear, as are its
anchor coefficients. For ||h||_1<=H_1 let

\[
U_h\le C_{\rm proj}\|h\|_1,\qquad
C_{\rm proj}=1+2L^2/\gamma.
\]

The direction bound (C14) has form ||dot g_(b_h)||<=J_1 U_h, with J_1
obtained by substituting Z_j=Q_j,Z_K=c,Z_c=1 into that formula.
The trilinear expression underlying (C1) is therefore bounded by

\[
M_{\rm cub}\prod_{i=1}^3\|h_i\|_1,\qquad
M_{\rm cub}=LJ_1 C_{\rm proj}^3.
\]

Telescoping its three arguments gives

\[
|\mathcal C(h)-\mathcal C(\tilde h)|
\le3M_{\rm cub}H_1^2\|h-\tilde h\|_1
\tag{C27}
\]

when both norms are at most H_1. The derivative feature map
h↦dot d_(b_h)(u) is linear, with uniform raw norm at most
J_1 C_proj(1+2sqrt(2)L/sqrt(gamma)) times ||h||_1.
For fixed p, h↦D'_0(h) is therefore linear with twice that bound.
When p changes, compare operators on the common L²(rho) space instead:
conjugation makes their feature map -2 sqrt(p(u)) dot d_(b_h)(u).
For densities at least p_min>0 and at most p_max, feature-map error is
bounded by twice sqrt(p_max) times the dot-d error, plus
sup_u||dot d_(b_tilde_h)(u)|| times
||p-tilde p||_infty/sqrt(p_min). This follows from the scalar square-root
identity and treats the change of prediction metric explicitly.
For density and target perturbations,
||h-tilde h||_1<=B_0||p-tilde p||_1+(5/4)||q-tilde q||_infty.
The given compact Lipschitz classes admit explicitly constructible finite
uniform nets by angular grids and quantized function values, followed by
normalization for densities and odd symmetrization for the factorized target
perturbations. Their covering errors follow from the declared Lipschitz
bounds. Net representatives may lie in a small enlarged bounding class:
choose resolution so their densities lie between 1/2 and two and their
factorized target perturbations retain |q|<=1. These properties are finite
checks from the existing strict target margin. The constants above cover
that harmless bounding class, with H_1 enlarged if necessary. The net
still covers every member of the unchanged family; no favorable region is
chosen after computing signs.

For a fixed density and finite coefficient dictionary, the cubic is a finite
polynomial in task coefficients. Its symmetric tensor can instead be
enclosed by the polarization identity
c(x,y,z)=48^(-1) sum_(eps_i=±1) eps_1 eps_2 eps_3
C(eps_1x+eps_2y+eps_3z). Propagate the finite scalar interval errors and the
prescribed coefficient ranges. These are endpoint tensor evaluations, not
network-training experiments.

What remains: no reference mesh, Gaussian integral or sign bound was evaluated
in this task. The reduction makes a finite deterministic sign certificate
possible **if** a sufficiently negative actual cubic exists on the fixed family.
It does not say that the interval will be negative; arbitrary-accuracy
approximation may certify zero or positive curvature instead. A small-stop
E₀ proof would still need a finite-time derivative modulus, beneficial
component signs, and the stipulated sampling/finite-network transfers.
The present result is narrower: complete finite approximation/error control
for the endpoint derivative and cubic, with no signed conclusion.

## 10. Read coverage and provenance

Read ROUTE_GEOMETRY.md completely in this continuation, including the
directional formula, projector subtraction, symmetry, component construction,
remainder discussion and all limitations. Its hash is
e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04.
The contract and own energy report were unchanged from their previously
complete reads; hashes were rechecked.

Previously complete established coverage used here:
global_nonlinear.md 12994–17016 (C.4.9–C.4.10), 1840–1902 (A.1–A.4),
5475–5782 (reference §§1–3), 5999–6103 (rational constant certificate),
6104–6521 (reference source §§1–4); special_data_limits.md 3785–4326
(complete III.F). No unread complement is claimed audited. Skills/process
coverage is recorded in ROUTE_ENERGY.md §9 and remains applicable.

Hashes at continuation start:

* RESEARCH_CONTRACT.md:
  0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f.
* ROUTE_ENERGY.md:
  01779adf6e60fde92fb6979c3e421b3bc5061850bc3051399714b7d4aa58993b.
* docs/global_nonlinear.md:
  5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483.
* docs/special_data_limits.md:
  5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489.
* RESEARCH_WORKFLOW.md:
  8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12.

Actual checks were algebraic reconstruction of the clock constants, moment
interpolation exponents, cutoff products, projector factors, cubic signs and
Gaussian square-root bound. No training, quadrature, random simulation, or
performance-based task selection was performed. This is a research
approximation lemma, not an evaluated numerical certificate or promotion review.
