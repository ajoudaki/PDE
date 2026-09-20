# An exact canonical p=1 counterexample to the straight-line claim

**Independent refinement with informed corrections, 2026-09-19.** Author:
scoped agent `all_bad_local_geometry`. The original scientific inputs were
the complete `docs/observable_p1.md`, `docs/NOTATION.md`, the neutral
assignments, and this agent's frozen `general_bad_geometry_route.md`. This
revision additionally reads and incorporates the complete informed internal
review `review_straight_line_counterexample.md`, including its separately
checked balanced-label extension. No other candidate, study, experiment, or
external source was consumed. The earlier `general_bad_geometry_route.md`
is unchanged.

The original counterexample passed that informed internal review, with the
normalization and differentiability clarifications incorporated below. This
was not a fresh isolated review or promotion. Both data constructions are
specified by exact finite prescriptions; decimal coordinates have not been
computed. Section 10 records the original frozen and review hashes.

Source SHA-256:

```
docs/observable_p1.md
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba
docs/NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
general_bad_geometry_route.md
7c88c617b0ace8bd59332fa0e124a4fb2c77cb5b88790b9410cb50f1aa877a37
```

## 1. Claim disproved

There exist d=3, at most 24 pairwise nonparallel/nonantiparallel unit
normalized input directions, positive weights of total mass one, mixed
binary labels, and a bounded odd canonical population equilibrium with loss
one such that:

- Every state direction whose lower-weight component is nonzero has a
  **strictly positive quadratic loss coefficient**.
- Every direction with zero lower-weight component is **identically flat**,
  even when its readout and full 3-by-6 matrix components are arbitrary.

The expansion holds for every finite L2 state direction. Along bounded
directions the loss is real analytic, so its first nonzero Taylor coefficient
is exactly the positive quadratic coefficient displayed below.

The equilibrium is nevertheless not a local minimum in the product L2 and
Frobenius topology. Thus this is an actual p=1 instance of the distinction
between local-minimum geometry and the behavior along each fixed line. It
refutes the full ambient straight-line conjecture and its bounded-direction
version. No claim is made that the prescribed initialized flow can reach it.
Section 8 retains this original construction and supplies a separate version
with at most 26 input directions and total weight exactly one half on each
binary label.

## 2. Data construction: two strict maxima with cancelling activations

For \(x\in(0,1/10)\), define

\[
t(x)=\operatorname{arctanh}x,\qquad
s(x)=-\operatorname{arctanh}(2x),\qquad
\rho(x)=\sqrt{1-t(x)^2-s(x)^2},
\]
\[
u_\pm(x)=(t(x),s(x),\pm\rho(x))\in\mathbb R^3.
\tag{1}
\]

The physical samples are \(x_a=\sqrt3\,u_a\). Consequently
\(x_a\cdot x_a/3=1\), and their first-layer arguments are
\(w\cdot x_a/\sqrt3=w\cdot u_a\). The unindexed x in (1) is a scalar
construction parameter; it is distinct from these vector-valued physical
samples.

The square root is positive. Indeed,
\(\operatorname{arctanh}r\le r/(1-r^2)\) for \(0<r<1\), as follows by
integrating \((1-z^2)^{-1}\le(1-r^2)^{-1}\) over \([0,r]\). Thus
\(t<1/8\), \(|s|<1/4\), and \(t^2+s^2<5/64<1\) on this interval.
Every u in (1) is a unit vector.

Let \(v_1=e_1\), \(v_2=e_2\) be the first two input-coordinate vectors.
For every input in (1),

\[
\tanh(u_\pm\cdot v_1)=x,
\qquad \tanh(u_\pm\cdot v_2)=-2x.
\tag{2}
\]

We will choose finitely many xj and real coefficients lambdaj so that

\[
\widetilde R(v)=\sum_{j=1}^{12}\frac{\lambda_j}{2}
 \{\tanh(u_+(x_j)\cdot v)+\tanh(u_-(x_j)\cdot v)\}
\tag{3}
\]

satisfies the exact interpolation conditions

\[
\nabla\widetilde R(v_1)=\nabla\widetilde R(v_2)=0,
\qquad
\nabla^2\widetilde R(v_1)=\nabla^2\widetilde R(v_2)=-I_3.
\tag{4}
\]

These are both strict local maxima. They need not be global maxima, and their
values need not agree.

### The explicit linear system

Put

\[
B(x)=\begin{pmatrix}
t^2&ts&0\\ ts&s^2&0\\0&0&\rho^2
\end{pmatrix}
=\tfrac12(u_+u_+^T+u_-u_-^T).
\]

Choose the coefficients to satisfy

\[
\sum_j\lambda_j t_j
=\sum_j\lambda_j s_j
=\sum_j\lambda_j x_j^2t_j
=\sum_j\lambda_j x_j^2s_j=0,
\tag{5}
\]
\[
\sum_j\lambda_j x_jB(x_j)=\tfrac34I_3,
\qquad
\sum_j\lambda_j x_j^3B(x_j)=\tfrac14I_3.
\tag{6}
\]

There are exactly 12 scalar equations: four in (5) and four independent
entries of each matrix in (6). Their coefficient column at x is

\[
\Phi(x)=
(t,s,x^2t,x^2s,
xt^2,xts,xs^2,x\rho^2,
x^3t^2,x^3ts,x^3s^2,x^3\rho^2)^T.
\tag{7}
\]

The target column is

\[
b=(0,0,0,0,
\tfrac34,0,\tfrac34,\tfrac34,
\tfrac14,0,\tfrac14,\tfrac14)^T.
\tag{8}
\]

Section 3 proves that the 12 component functions of Phi are linearly
independent and that the following integer is finite:

\[
N=\min\{n\in\mathbb N:n\ge121,
\det[\Phi(1/n)\ \Phi(2/n)\ \cdots\ \Phi(12/n)]\ne0\}.
\tag{9}
\]

This fixes the counterexample without a numerical search: set \(x_j=j/N\)
and

\[
(\lambda_1,\ldots,\lambda_{12})^T
=[\Phi(x_1)\ \cdots\ \Phi(x_{12})]^{-1}b.
\tag{10}
\]

Equations (1), (7)--(10) are exact definitions using elementary functions and
a single well-defined positive integer. The existence proof for N is given
below; no observed numerical determinant is a premise.

To verify (4), at v1 the paired gradient is
\((1-x^2)(t,s,0)\), while at v2 it is
\((1-4x^2)(t,s,0)\). Equation (5) makes both gradients vanish. The paired
Hessians are respectively

\[
-2x(1-x^2)B(x),\qquad 4x(1-4x^2)B(x).
\]

Consequently (6) gives

\[
-2(\tfrac34I_3-\tfrac14I_3)=-I_3,
\qquad
4(\tfrac34I_3-4\tfrac14I_3)=-I_3,
\]

as required.

### Positive weights and mixed binary labels

The solution lambda is nonzero, since b is nonzero. Equation (5) and
\(t_j>0\) show that lambda has both positive and negative entries. Set

\[
Q=\sum_j|\lambda_j|>0.
\]

For each nonzero lambdaj include the two inputs \(u_\pm(x_j)\), each with

\[
\mu_{j,\pm}=\frac{|\lambda_j|}{2Q}>0,
\qquad y_{j,\pm}=\operatorname{sign}\lambda_j\in\{-1,1\}.
\tag{11}
\]

Omit the pair if lambdaj is zero. The weights have total mass one, and both
labels occur. The resulting label potential is

\[
R(v)=\sum_a\mu_a y_a\tanh(u_a\cdot v)
=\widetilde R(v)/Q.
\tag{12}
\]

All included inputs are pairwise neither parallel nor antiparallel. They are
unit vectors with positive first coordinate, so antiparallel pairs cannot
occur. Equality of two first coordinates forces the same xj; the two signs
then give distinct inputs because rho is positive. Unit parallel vectors
would have to be equal.

## 3. Proof that the finite interpolation system is solvable

Replacing the entries involving \(\rho^2=1-t^2-s^2\), invertibly, shows that
the components in (7) span the same 12-dimensional candidate space as

\[
t,s,x^2t,x^2s,x,x^3,
xt^2,x^3t^2,xts,x^3ts,xs^2,x^3s^2.
\tag{13}
\]

To prove independence, a proposed dependence among (13) can be written

\[
A(x)t+B(x)s+xC(x)+xD(x)t^2+xE(x)ts+xF(x)s^2=0,
\tag{14}
\]

where A,B,C,D,E,F are polynomials of the form \(a_0+a_2x^2\).

Here

\[
t=\tfrac12[\log(1+x)-\log(1-x)],\qquad
s=-\tfrac12[\log(1+2x)-\log(1-2x)].
\]

The real identity analytically continues along paths avoiding
\(\{-1,-1/2,1/2,1\}\). A loop around 1/2, with zero winding around the
other three points, leaves t unchanged and adds a nonzero integer multiple
of \(\pi i\) to s. This follows directly by integrating the logarithmic
derivative around its one enclosed simple zero. Repeating the loop n times
in (14) gives a degree-at-most-two polynomial in n that vanishes for every
integer n. Its quadratic and linear coefficients give

\[
F=0,\qquad B+xEt=0.
\]

A loop around 1 leaves s unchanged and adds a nonzero multiple of \(\pi i\)
to t. Applied to the latter relation it gives E=0 and then B=0. Applying
repeated loops around 1 to the remaining relation
\(At+xC+xDt^2=0\) gives D=0, A=0, C=0. Every coefficient in (14) vanishes.
Thus the 12 functions are linearly independent. The argument uses only the
elementary logarithm continuation; no approximation or special independence
theorem is assumed.

It remains to prove that the particular equally spaced selection (9)
eventually has nonzero determinant. All functions in (7) are analytic near
zero. In any finite-dimensional independent space of analytic germs one can
choose a basis g1,...,g12 with distinct increasing orders of vanishing
\(n_1<\cdots<n_{12}\): choose a germ with the smallest nonzero Taylor
order, then restrict to the kernel of its leading coefficient and repeat.
No nonzero analytic germ has infinite order of vanishing. Write

\[
g_i(x)=a_i x^{n_i}+O(x^{n_i+1}),\qquad a_i\ne0.
\]

It follows that

\[
\det[g_i(jh)]_{i,j=1}^{12}
=\left(\prod_i a_i\right)h^{\sum_i n_i}
 \det[j^{n_i}]_{i,j=1}^{12}
+O(h^{1+\sum_i n_i}).
\tag{15}
\]

The generalized Vandermonde determinant in (15) is nonzero. Otherwise a
nonzero linear combination of the 12 monomials would have the 12 distinct
positive zeros 1,...,12. A nonzero combination of k monomials of distinct
nonnegative powers has at most k-1 positive zeros: divide by its lowest
power and apply Rolle's theorem, reducing the number of monomials by one
after differentiation; induction proves the assertion. This contradicts
12 zeros.

Since changing from Phi to g is an invertible constant row transformation,
(15) proves that the determinant in (9) is nonzero for all sufficiently large
n. Therefore N is finite, and (10) solves (5)--(6) exactly.

## 4. Place the data in the fixed canonical population carriers

Use d=3 with the exact lower and upper Gaussian carriers from
`observable_p1.md`, omitting only the inactive constant features. Write

\[
b_1:\Omega_1\to\mathbb R^6,
\qquad b_2:\Omega_2\to\mathbb R^3.
\]

In particular, the first lower carrier is
\(b_{1,1}=\tanh(G_1)/\sqrt{v+\eta}\), with
\(\eta=1/4096\). Coordinate pairs \((G_i,Z_i)\) are independent for
i=1,2,3. All other carrier components and the full joint carrier law are
unchanged.

Let a positive q satisfy \(P(|G_3|\le q)=2/3\). Such a q exists and is
unique by continuity and strict positivity of the standard normal density.
Define the bounded odd lower state by

\[
w(\omega)=\begin{cases}
\operatorname{sign}(G_1)v_1,&|G_3|\le q,\\
\operatorname{sign}(G_1)v_2,&|G_3|>q.
\end{cases}
\tag{16}
\]

Values on \(G_1=0\) are irrelevant. The branch event is unchanged by mark
negation, so w is odd. Let

\[
c=b_{2,1},\qquad
M=e_1\widehat e_1^T\in\mathbb R^{3\times6},
\tag{17}
\]

where e1 is the first upper coordinate vector and ehat1 the first lower
carrier coordinate vector. A rank-one current matrix is permitted in the
full state class; perturbations below may use every matrix entry.

For an input from the jth pair, (2) and (16) give

\[
\tanh(w\cdot u_a)=\operatorname{sign}(G_1)K(G_3)x_j,
\]

where K is 1 on the first branch and -2 on the second, so \(E K=0\).
For lower carrier components belonging to coordinate pair 1, independence
from G3 makes the expectation of \(b_1\tanh(w\cdot u_a)\) zero. For
components belonging to coordinate pairs 2 or 3, the independent factor
\(\operatorname{sign}(G_1)\) has mean zero. Consequently

\[
a_a=E_1[b_1\tanh(w\cdot u_a)]=0
\quad\text{for every sample }a.
\tag{18}
\]

Thus every upper preactivation and activation is zero, every prediction is
zero, and the loss is

\[
\mathcal L=\sum_a\mu_a y_a^2=1.
\tag{19}
\]

The upper carrier covariance is diagonal with equal positive diagonal
entries. Hence

\[
\gamma=E_2[c b_2]=\kappa e_1,
\qquad\kappa=E_2[b_{2,1}^2]>0,
\]
\[
b_1^TM^T\gamma=\kappa b_{1,1}.
\tag{20}
\]

By (4), (12), and oddness of R,

\[
\nabla R(w)=0,
\qquad
\nabla^2 R(w)=-\frac{\operatorname{sign}(G_1)}{Q}I_3
\quad\text{almost surely}.
\tag{21}
\]

The c gradient is zero because all upper activations vanish; the M gradient
is zero because all a's vanish. The lower gradient is
\(-2\kappa b_{1,1}\nabla R(w)\), and is zero by (21).
This verifies that (16)--(17) is an exact equilibrium of all three canonical
population gradient equations.

## 5. Every nonflat line has a positive quadratic coefficient

Take any fixed direction

\[
(V,h,N)\in
L^2_{\rm odd}(\Omega_1;\mathbb R^3)
\times L^2_{\rm odd}(\Omega_2)
\times\mathbb R^{3\times6},
\]

and set \((w_\varepsilon,c_\varepsilon,M_\varepsilon)
=(w+\varepsilon V,c+\varepsilon h,M+\varepsilon N)\).
Use the names

\[
A_a=E_1[b_1\operatorname{sech}^2(w\cdot u_a)(V\cdot u_a)],
\]
\[
B_a=E_1[b_1\tanh''(w\cdot u_a)(V\cdot u_a)^2],
\qquad \delta\gamma=E_2[h b_2].
\]

Bounded b1 and bounded first and second derivatives of tanh give

\[
a_a(\varepsilon)=\varepsilon A_a+\tfrac12\varepsilon^2B_a
+o(\varepsilon^2).
\tag{22}
\]

For finite L2 V, the quadratic remainder follows by the integral Taylor
formula and dominated convergence, dominated by a constant times \(|V|^2\).
No higher moment is required. Since tanh has zero second derivative at zero,
and the upper carrier is bounded,

\[
f_a(\varepsilon)
=\varepsilon F_a
+\varepsilon^2\left(
 \gamma^TNA_a+\delta\gamma^TMA_a+\tfrac12\gamma^TMB_a
\right)+o(\varepsilon^2),
\quad F_a=\gamma^TMA_a.
\tag{23}
\]

The weighted label sum of A vanishes as a vector:

\[
\sum_a\mu_a y_a A_a
=E_1[b_1\nabla R(w)\cdot V]=0.
\tag{24}
\]

Thus the linear loss coefficient and both mixed terms involving N and h
vanish. Expanding the squared loss using (23)--(24) yields

\[
\mathcal L(\varepsilon)-1
=\varepsilon^2\left[
 \sum_a\mu_aF_a^2
 -E_1[\kappa b_{1,1}V^T\nabla^2R(w)V]
\right]+o(\varepsilon^2).
\]

Using (21), its quadratic coefficient is exactly

\[
\sum_a\mu_aF_a^2
+\frac{\kappa}{Q}E_1[|b_{1,1}|\,|V|^2].
\tag{25}
\]

It is finite and strictly positive whenever V is nonzero in L2, because
\(\kappa,Q>0\), \(b_{1,1}\ne0\) almost surely, and the first term is
nonnegative. This conclusion holds for arbitrary h,N, without a rank or
coordinate restriction on N.

If V=0, the lower state remains fixed, so (18) holds for every epsilon.
Then every prediction stays zero regardless of c+epsilon h and M+epsilon N.
The entire line is identically flat.

For bounded V, the lower integrands are uniformly analytic for epsilon in a
complex neighborhood of zero because w,V,b1 are bounded and tanh has no
poles in a sufficiently small strip. The same holds for the upper finite
arguments, with the integrable multiplier c+epsilon h. Hence the loss is real
analytic along every bounded state direction. Formula (25) is then literally
the first nonzero Taylor coefficient for every nonflat line, and its degree
is two with positive sign.

## 6. Direct check that this is not a local minimum

Equation (2) implies \(R(v_2)=-2R(v_1)\). At least one of these two values
is nonpositive. Call that point vj. If \(R(v_j)<0\), oddness gives
\(R(-v_j)>R(v_j)\). If \(R(v_j)=0\), the negative definite Hessian in
(4) gives a nearby point with negative R, whose negative has positive R.
In either case there is a finite vnew with \(R(v_{\rm new})>R(v_j)\).

The set of lower marks with \(G_1>0\) and branch j has positive measure.
Choose a positive-measure subset on which \(b_{1,1}\) is bounded below by a
positive constant. On an arbitrarily small measurable subset E, replace w by
vnew, and make the opposite replacement on -E. The L2 displacement tends to
zero with the measure of E. The first change of the loss, as a smooth
function of the finite retained activations, is

\[
-4\kappa\int_E b_{1,1}
 [R(v_{\rm new})-R(v_j)]\,dP_1+O(P_1(E)^2)<0
\]

for sufficiently small positive measure. Thus lower-loss states exist in
every L2 neighborhood, in agreement with the earlier weaker theorem.

These replacements have finite pointwise displacement on sets that shrink
with the neighborhood. They do not produce a single fixed direction with a
negative leading coefficient. The next section identifies precisely why the
directional quadratic expansion gives no uniform neighborhood conclusion.

## 7. The directional quadratic form is noncoercive and is not a Fréchet Hessian

Write \(q_2(V)\) for (25). It is a bounded quadratic form on the lower L2
space: each Fa is a bounded linear functional of V, and the multiplication
weight \(|b_{1,1}|\) is bounded. It is strictly positive for every nonzero
lower direction. These statements concern fixed-direction coefficients;
they do not assert a uniform second-order expansion in the Hilbert norm.

### Normalized directions proving noncoercivity

Let

\[
E_n=\{|G_1|<1/n\},\qquad p_n=P_1(E_n)>0,\qquad
V_n=\frac{\operatorname{sign}(G_1)1_{E_n}}{\sqrt{p_n}}e_1.
\tag{26}
\]

Every Vn is odd and bounded, and \(\|V_n\|_{L^2}=1\). Since
\(b_{1,1}=\tanh(G_1)/\sqrt{v+\eta}\), on En its absolute value is at
most \(C/n\), with the fixed constant \(C=1/\sqrt{v+\eta}\). Therefore

\[
E_1[|b_{1,1}|\,|V_n|^2]\le C/n.
\]

The finite sum of squared functionals in (25) also tends to zero, rather
than restoring coercivity. Indeed, (17), (20), and the definition of Aa give

\[
F_a(V_n)=\kappa E_1[
b_{1,1}\operatorname{sech}^2(w\cdot u_a)(V_n\cdot u_a)],
\]

so, using \(|u_a|=1\),

\[
|F_a(V_n)|\le\frac{\kappa C\sqrt{p_n}}n,
\qquad
0<q_2(V_n)\le\frac{\kappa^2C^2p_n}{n^2}
+\frac{\kappa C}{Qn}\longrightarrow0.
\tag{27}
\]

Thus no positive constant lower bound by \(\|V\|_{L^2}^2\) holds, even
after restricting to lower-weight directions. This argument includes the
finite-rank nonnegative term; essential infimum zero of the multiplier alone
would not suffice for an arbitrary sum of positive forms.

### Failure of a second-order Fréchet expansion

There is a stronger distinction. Suppose the loss had a second-order
Fréchet Taylor expansion at this equilibrium in the product L2/Frobenius
norm. Its linear term would vanish by stationarity. Evaluation along every
fixed direction would force its quadratic term to equal q2 on the lower
component and to be independent of the upper and matrix components, by
(25) and exact flatness. In particular, for lower increments H tending to
zero it would require

\[
\mathcal L(w+H,c,M)-1=q_2(H)+o(\|H\|_{L^2}^2).
\tag{28}
\]

Use the shrinking-set replacement from Section 6. Write
\(\Delta v=v_{\rm new}-v_j\ne0\),
\(\Delta R=R(v_{\rm new})-R(v_j)>0\), and choose the sets E within a fixed
positive-measure region on which \(b_{1,1}\ge\beta>0\). Let HE be the
increment equal to Delta v on E, minus Delta v on -E, and zero elsewhere.
For \(\varepsilon=P_1(E)\),

\[
\|H_E\|_{L^2}^2=2\varepsilon|\Delta v|^2,
\qquad
q_2(H_E)\ge\frac{2\kappa\beta}{Q}
                 \varepsilon|\Delta v|^2.
\]

The actual loss change from Section 6 satisfies

\[
\mathcal L(w+H_E,c,M)-1
\le-4\kappa\Delta R\,\beta\varepsilon+O(\varepsilon^2).
\]

Subtracting q2 and dividing by the squared norm gives a strictly negative
upper bound separated from zero as epsilon tends to zero. This contradicts
(28). Hence the loss has no second-order Fréchet expansion at this state;
in particular it has no Fréchet Hilbert Hessian, and its physical L2
gradient is not Fréchet differentiable there.

Formula (25) is nevertheless a well-defined bounded quadratic form giving
every fixed-direction second coefficient. The finite-dimensional input-space
Hessians of R in (4) and (21) are ordinary genuine Hessians. Neither their
existence nor the directional form should be confused with a Fréchet Hessian
of the population-state loss.

## 8. A separately checked balanced-label extension with at most 26 inputs

The original at-most-24-input construction in Sections 2--6 is unchanged.
To force equal total positive-label and negative-label weight, append one
interpolation condition:

\[
\sum_j\lambda_j=0.
\tag{29}
\]

Define the 13-component column and target by

\[
\Phi_{13}(x)=(\Phi(x)^T,1)^T,
\qquad b_{13}=(b^T,0)^T.
\]

These 13 analytic functions are independent. Every component of Phi
vanishes at zero, so evaluation at zero of a proposed dependence first
eliminates the constant coefficient; Section 3 then eliminates the other
twelve coefficients. The distinct-vanishing-order and generalized-Vandermonde
proof in Section 3 applies with thirteen functions, now including order zero.
It proves that

\[
N_{13}=\min\{n\in\mathbb N:n\ge131,
\det[\Phi_{13}(1/n)\ \cdots\ \Phi_{13}(13/n)]\ne0\}
\tag{30}
\]

is finite. All thirteen nodes \(x_j=j/N_{13}\) still lie in \((0,1/10)\).
Set

\[
\lambda^{(13)}
=[\Phi_{13}(1/N_{13})\ \cdots\ \Phi_{13}(13/N_{13})]^{-1}b_{13},
\qquad Q_{13}=\sum_{j=1}^{13}|\lambda_j^{(13)}|.
\tag{31}
\]

The nonzero target ensures a nonzero coefficient vector. Its first twelve
equations preserve (5)--(6), while its last equation is (29). Consequently

\[
\sum_{\lambda_j^{(13)}>0}\lambda_j^{(13)}
=-\sum_{\lambda_j^{(13)}<0}\lambda_j^{(13)}=Q_{13}/2>0.
\]

For each nonzero coefficient use the paired normalized directions (1), the
physical samples \(x_a=\sqrt3u_a\), and the labels and weights from (11)
with lambda and Q replaced by \(\lambda^{(13)}\) and Q13. After omitting
zero pairs there are at most 26 samples, with

\[
\sum_{a:y_a=1}\mu_a
=\sum_{a:y_a=-1}\mu_a=\tfrac12.
\tag{32}
\]

All gradient and input-space Hessian constraints remain valid, with the
normalization Q13. The identity (2), the same 2/3 versus 1/3 population
branch, and all carrier cancellations are unchanged. Thus the state
(16)--(17) is again an equilibrium of loss one, every line with a nonzero
lower component again has the strictly positive coefficient (25) with Q13,
and every line with zero lower component is identically flat. Sections 6--7
likewise give nearby smaller losses, noncoercivity, and failure of a Fréchet
Hessian. This extension establishes the same counterexample with exactly
balanced binary-label weight; it does not claim that the original 24-input
version was balanced.

## 9. Scope and checks

- This is an ambient population state with the exact canonical d=3 frozen
  carriers, bounded odd w and c, and the permitted full matrix state space.
  The initial matrix D is not altered or reinterpreted; the current M need
  not equal its initialized value. No reachability assertion is made.
- The data are finite, their normalized directions have norm one, and their
  physical samples are \(x_a=\sqrt3u_a\). Labels are exactly binary and
  mixed, and all retained weights are strictly positive. The loss convention
  is the unhalved weighted square sum. Only the separate 26-input extension
  asserts exactly balanced total label weights.
- The matrix used at the equilibrium has rank one, but every entry is
  allowed to vary in the straight-line calculation.
- The original data interpolation uses an exact invertible 12-by-12 system;
  the balanced-label extension uses the proved 13-by-13 enlargement. Both
  integer existence prescriptions are proved, rather than inferred from a
  floating-point computation.
- The construction was checked algebraically at both critical points, in
  both lower-population branches, at every gradient block, and in the full
  mixed second-order loss expansion. The positive coefficient in (25)
  covers even unbounded finite L2 directions; analyticity is asserted only
  for bounded lower directions.
- No experiment was performed. The original construction, the explanatory
  corrections, and the separate balanced-label extension passed the informed
  internal check identified below. There has been no fresh isolated review
  or promotion.

## 10. Provenance and informed internal check

The original complete candidate was frozen at SHA-256
`51279663fe402d16e979b9fa9af646453ac307707563f501c164f89ee9a703ec`.
The complete informed review
[review_straight_line_counterexample.md](review_straight_line_counterexample.md)
has SHA-256
`82214ae2329e03bf5662709fe91ead6cc3c98a879ae96b88cff8c1b7fba1fc24`.
Its reviewer was the study's scoped `cubic_order_check` route, which disclosed
prior relevant study context; it was not a fresh isolated reviewer.

The review checked the full interpolation proof, physical carrier
cancellation, every gradient block, all finite-L2 fixed-direction expansions,
and direct nearby descent. Its verdict passed those mathematical claims
while requiring explicit physical input scaling, a complete noncoercivity
argument, and the distinction between a directional quadratic form and a
Fréchet Hessian. It also separately verified the supervisor-proposed
13-function balanced-label extension. This revision incorporates those
specific checked changes and preserves the original 24-input construction.
The author rechecked the displayed constants and factors in (26)--(32) and
the dependency on Q versus Q13. No new numerical claim or promotion status
is inferred from this informed internal check.
