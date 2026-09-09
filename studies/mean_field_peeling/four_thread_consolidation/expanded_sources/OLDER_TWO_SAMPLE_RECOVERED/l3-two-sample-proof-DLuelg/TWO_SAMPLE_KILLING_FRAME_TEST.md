# Two-sample Killing-frame test

Date: 2026-09-06. Status: elementary structural obstruction proved below;
no experiments, delegation, or independent review. This is not a proof
or disproof of the full two-sample learning theorem.

For every fixed \(0<\lvert\rho\rvert<1\), every smooth nonaffine activation with
positive bounded derivative fails the proposed mechanism: there is no
smooth positive definite Riemannian metric on all of \(\mathbb R^2\)
for which both raw controlled fields are Killing. No uniform metric
comparison hypothesis is needed for this conclusion. For each of the
two named activations, a stronger local obstruction holds: no such
metric exists on any nonempty open subset of \(\mathbb R^2\).

The argument permits nonzero brackets and arbitrary curvature. It uses
the derivative of a Killing field at one of its zeros, not the existence
of a chart that makes the controlled fields constant.

## 1. Contract, inputs, and exact object

The explicit inputs, read in full, are:

- [CONTRACT_AND_LEDGER.md](/tmp/l3-two-sample-proof-DLuelg/CONTRACT_AND_LEDGER.md),
  SHA256 `e1f04d537a7650962f60c2eb33b305e7ad604813c2ee6a937d283ea11aa43b40`.
- [EXACT_TWO_SAMPLE_REDUCTION.md](/tmp/l3-two-sample-proof-DLuelg/EXACT_TWO_SAMPLE_REDUCTION.md),
  SHA256 `432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60`.

The reduction supplies the raw first-neuron geometry and its separate
no-flattening lemma. The ledger supplies the unchanged full-network
target and its scope. No other mathematical report or external theorem
is a proof dependency here.

The requested `solve-math-rigorously` and `investigate-conjectures`
skills were read directly, together with the latter's required
`research-contract.md`, `evidence-ledger.md`, and `adversarial-audit.md`
references. The authorization is a bounded theoretical discrimination
of this one metric mechanism. No experiment or multi-route orchestration
reference is applicable. Only this new file is written.

Write \(z=(x,y)\), \(f=\phi'>0\), and

\[
C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
v_1=Ce_1,\quad v_2=Ce_2,\qquad
X_1=f(x)v_1,\quad X_2=f(y)v_2.
\]

Here \(\phi:\mathbb R\to\mathbb R\) is smooth and fixed, and

\[
\dot z=q_1X_1(z)+q_2X_2(z)
       =C\operatorname{diag}(\phi'(x),\phi'(y))q.
\tag{1}
\]

This is precisely the controlled subsystem in the question. The
residual, label, and clock factors of the input reduction can be
included in the controls; no change to any raw network update is made.
The metric may depend on \(\phi,\rho\) and fixed configuration parameters,
but must be fixed independently of the control and its future path.
The exact cancellation is tested for arbitrary signed controls in
\(\mathbb R^2\). This tests a proposed structural identity, without
asserting that all these controls occur on trained network trajectories.

Represent a metric by a smooth symmetric positive definite matrix
\(G(z)\), with \(g_z(u,v)=u^TG(z)v\). Global uniform Euclidean equivalence
would mean

\[
m|v|^2\le v^TG(z)v\le M|v|^2
\quad\text{for every }z,v,
\qquad 0<m\le M<\infty,
\tag{2}
\]

where \(m,M\) may depend on the fixed configuration, including \(\rho\),
but not on \(z\) or control amplitude. Pointwise positive definiteness
is weaker: its comparison constants can vary with \(z\). Every smooth
positive definite metric has uniform comparison constants on each
compact subset of its domain, by continuity of the extremal eigenvalues.
The global obstruction below assumes only pointwise positive
definiteness, and therefore covers all of these global interpretations.

## 2. Killing fields and amplitude-independent expansion

For a vector field \(X\), define

\[
\mathcal L_XG=X\cdot\nabla G+(DX)^TG+GDX.
\tag{3}
\]

The field is Killing when this tensor vanishes. If nearby trajectories
use the same prescribed control \(q(t)\), their infinitesimal separation
\(\eta\) satisfies \(\dot\eta=\sum_aq_aDX_a\eta\). Differentiation gives

\[
\frac{d}{dt}\bigl(\eta^TG(z)\eta\bigr)
   =\sum_{a=1}^2q_a\eta^T(\mathcal L_{X_a}G)(z)\eta.
\tag{4}
\]

Thus both Killing equations cancel all terms proportional to the common
control amplitude. They preserve lengths of transported curves, hence
the induced distance when the common flow and its inverse are defined
on the relevant domain. Only local smooth flows are needed for (4).

Conversely, suppose the requested one-sided infinitesimal estimate is

\[
\sum_aq_a\eta^T(\mathcal L_{X_a}G)(z)\eta
       \le 2K(z)\eta^TG(z)\eta
\quad\text{for all }q\in\mathbb R^2,\ \eta\in\mathbb R^2,
\tag{5}
\]

with finite \(K(z)\) independent of \(q\). Fix \(z,\eta\) and set
\(q=se_a\) for arbitrarily large positive and negative \(s\). The
coefficient of \(s\) must be zero. A symmetric matrix whose quadratic
form vanishes for every \(\eta\) is zero: evaluate on the coordinate
vectors and their sums. Consequently (5) forces both Killing equations.
This remains true if \(K\) depends on other fixed configuration data.

This equivalence concerns the stated instantaneous one-sided expansion
bound and unrestricted signed controls. It does not assert an
equivalence for estimates with additional prefactors, restricted control
sets, or bounds only along particular trained trajectories. Variations
in the actual backward queries also produce terms involving
\(\delta q\), which (4) does not cancel.

## 3. Two elementary facts about Killing fields

We use the bracket convention

\[
[X,Y]=DY\,X-DX\,Y.
\]

First, the bracket of two Killing fields is Killing. Here is the needed
identity and its justification, so no isometry-group theorem is invoked.
For arbitrary auxiliary vector fields \(U,V\), equation (3) is equivalent
to

\[
(\mathcal L_Xg)(U,V)
 =X(g(U,V))-g([X,U],V)-g(U,[X,V]).
\]

Expand \(\mathcal L_X\mathcal L_Yg-\mathcal L_Y\mathcal L_Xg\)
using this formula. Terms differentiating one argument in each order
cancel; the remaining expression is

\[
[X,Y](g(U,V))
-g([X,[Y,U]]-[Y,[X,U]],V)
-g(U,[X,[Y,V]]-[Y,[X,V]]).
\]

The identity
\([X,[Y,U]]-[Y,[X,U]]=[[X,Y],U]\)
follows by expanding commutators of their differential operators on a
test function. Therefore the displayed expression equals
\((\mathcal L_{[X,Y]}g)(U,V)\). If both original Lie derivatives vanish,
so does the bracket's. Constant linear combinations are Killing by (3).

Second, if a Killing field \(K\) vanishes at \(p\), then \(A=DK(p)\)
satisfies

\[
A^TG(p)+G(p)A=0,
\tag{6}
\]

because the transport term \(K\cdot\nabla G\) in (3) is zero at \(p\).
Choose a \(G(p)\)-orthonormal basis by subtracting projections and
normalizing two independent vectors. In that basis, (6) says that
\(A\) is a real skew-symmetric \(2\times2\) matrix, of the form

\[
\begin{pmatrix}0&-\omega\\\omega&0\end{pmatrix}.
\]

Similarity preserves its determinant. Hence

\[
\det DK(p)=\omega^2\ge0,
\qquad \det DK(p)=0\ \Longrightarrow\ DK(p)=0.
\tag{7}
\]

These statements are pointwise and do not require flatness,
completeness, a global coordinate chart, or commuting controlled fields.

## 4. Diagonal compatibility and the global obstruction

Direct differentiation of the fields in (1) gives

\[
Z:=[X_1,X_2]
 =\rho f(x)f'(y)v_2-\rho f(y)f'(x)v_1.
\tag{8}
\]

Suppose both fields are Killing on a neighborhood of \(p=(t,t)\).
At this point, \(Z(p)=\rho f'(t)(X_2(p)-X_1(p))\). Thus the field

\[
K_t=Z+\rho f'(t)(X_1-X_2)
\tag{9}
\]

is Killing and vanishes at \(p\). In (9), \(t\) is fixed, so \(f'(t)\)
is a constant coefficient when differentiating the field.

For this fixed \(t\), put \(P=f'(t)^2\ge0\) and \(F=f(t)f''(t)\).
The coefficients of \(K_t\) in the fixed basis \(v_1,v_2\) are

\[
\rho\bigl(f'(t)f(x)-f(y)f'(x)\bigr),\qquad
\rho\bigl(f(x)f'(y)-f'(t)f(y)\bigr).
\]

Differentiating them with respect to \(x,y\) at \(p\) gives, in the
ordinary coordinate basis,

\[
DK_t(p)=\rho C
\begin{pmatrix}P-F&-P\\P&F-P\end{pmatrix}.
\tag{10}
\]

Since the determinant of the last matrix is
\(-(P-F)^2+P^2=F(2P-F)\), equation (7) implies

\[
0\le\det DK_t(p)
 =\rho^2(1-\rho^2)F(2P-F).
\tag{11}
\]

Our assumption \(0<\lvert\rho\rvert<1\) makes the prefactor positive. The
quadratic \(F(2P-F)\) is nonnegative exactly when \(0\le F\le2P\).
Since \(f(t)>0\), every diagonal point admitting such a metric satisfies

\[
f''(t)\ge0.
\tag{12}
\]

There is also a sharper necessary condition. Equality in (11) requires
\(DK_t(p)=0\) by (7). Because \(\rho C\) is invertible, (10) then forces
\(P=F=0\). Thus the full necessary alternative at any such diagonal
point is

\[
\begin{split}
&f'(t)=f''(t)=0,\quad\text{or}\\
&f'(t)\ne0\quad\text{and}\quad
  0<f(t)f''(t)<2f'(t)^2.
\end{split}
\tag{13}
\]

In particular, a nondegenerate critical point of \(f\), whether a
maximum or minimum, is forbidden on the diagonal.

If the metric exists on all of \(\mathbb R^2\), (12) holds for every
\(t\in\mathbb R\). Therefore \(f'\) is nondecreasing. Integrating this
monotonicity on either side of any \(t_0\) gives

\[
f(t)\ge f(t_0)+f'(t_0)(t-t_0)\quad(t\in\mathbb R).
\]

If \(f'(t_0)>0\), this contradicts boundedness above as \(t\to+\infty\).
If \(f'(t_0)<0\), it contradicts boundedness above as \(t\to-\infty\).
Hence \(f'(t_0)=0\) for every \(t_0\); \(f\) is constant and \(\phi\)
is affine. This proves the announced obstruction for every smooth
nonaffine activation with \(0<f\le M_f<\infty\), without any positive
lower bound on \(f\).

In fact the same argument rules out a common Killing metric even on an
open set containing the entire diagonal \(\{(t,t):t\in\mathbb R\}\).
The proof only used metric values and first derivatives at those points.

## 5. Independent area compatibility and the local question

The Killing equations also give a useful necessary condition away from
the diagonal. Let \(\mu=\sqrt{\det G}>0\) and \(w=\log\mu\).
Taking the trace of \(G^{-1}\mathcal L_XG=0\) yields

\[
Xw+\operatorname{div}X=0.
\tag{14}
\]

Indeed, differentiating the \(2\times2\) determinant gives
\(\partial_i\log\det G=\operatorname{tr}(G^{-1}\partial_iG)\);
the two derivative-of-\(X\) terms in (3) each contribute
\(\operatorname{div}X\). Thus (14) follows after dividing the trace
identity by two. It expresses preservation of the metric area element.

Set \(h=\log f\). Since the divergences of \(X_1,X_2\) are respectively
\(f'(x),f'(y)\), division by the positive gates gives

\[
w_x+\rho w_y=-h'(x),\qquad
\rho w_x+w_y=-h'(y).
\]

Solving this two-equation system,

\[
(1-\rho^2)w_x=-h'(x)+\rho h'(y),\qquad
(1-\rho^2)w_y=\rho h'(x)-h'(y).
\]

Equality of mixed partial derivatives, and \(\rho\ne0\), imply

\[
h''(x)=h''(y).
\tag{15}
\]

On any open rectangle \(I\times J\) in the metric's domain, fix one
coordinate and vary the other in (15). It follows that \(h''\) is
constant on both intervals, with the same constant. In particular,
if \(h''\) is nonconstant on every nonempty interval, there cannot be a
common Killing metric on any nonempty open set: every such set contains
an open rectangle.

For a metric on the whole plane, (15) requires \(h''\equiv\kappa\), hence

\[
f(t)=A\exp(\kappa t^2/2+\beta t),\qquad A>0.
\tag{16}
\]

Integrating the displayed equations for \(w\) also determines the area
density up to a positive factor:

\[
\mu(x,y)=B\exp\!\left[
-\frac{\kappa(x^2-2\rho xy+y^2)}{2(1-\rho^2)}
-\frac{\beta(x+y)}{1+\rho}\right],\qquad B>0.
\tag{17}
\]

Area preservation is only necessary. If \(\kappa\ne0\), (16) has a
critical point \(t_*=-\beta/\kappa\) with
\(f''(t_*)=\kappa f(t_*)\ne0\), contradicting (13). Consequently even
without assuming boundedness, a globally positive gate admitting a
global common Killing metric must have the form \(f(t)=Ae^{\beta t}\).
No sufficiency assertion about nonconstant exponential gates is made;
they are outside the bounded-gate class. Boundedness on the whole real
line would force \(\beta=0\).

## 6. The two proposed activations

For \(\phi(t)=1+\arctan(t)/10\),

\[
f(t)=\frac{1}{10(1+t^2)},\quad f'(0)=0,\quad f''(0)=-\frac15.
\]

Thus (13) already forbids a metric near \((0,0)\). To address all other
open regions as well, compute

\[
h''(t)=\frac{2(t^2-1)}{(1+t^2)^2},\qquad
h'''(t)=\frac{4t(3-t^2)}{(1+t^2)^3}.
\]

The latter vanishes only at \(0,\sqrt3,-\sqrt3\), so \(h''\) cannot
be constant on any nonempty interval. Condition (15) rules out a common
Killing metric on every nonempty open set.

For \(\phi(t)=t+1+\tanh(t)/2\),

\[
f(t)=1+\tfrac12\operatorname{sech}^2t,\quad
f'(0)=0,\quad f''(0)=-1.
\]

Again (13) forbids a metric near \((0,0)\), despite \(1<f(t)\le3/2\).
For the stronger local statement put \(u=\tanh t\), so
\(u'=1-u^2>0\) and \(f=(3-u^2)/2\). Differentiating \(h=\log f\) gives

\[
h'(t)=-\frac{2u(1-u^2)}{3-u^2},\qquad
h''(t)=\frac{-2(1-u^2)(3-8u^2+u^4)}{(3-u^2)^2}.
\]

If \(h''\equiv\kappa\) on a nonempty interval, the strictly increasing
map \(t\mapsto u\) gives the polynomial identity

\[
-2(1-u^2)(3-8u^2+u^4)=\kappa(3-u^2)^2
\]

on a nonempty interval in \((-1,1)\). The left side has a nonzero
\(2u^6\) term and the right side has degree at most four. Their
difference is a nonzero polynomial and cannot vanish on an interval
(successively factoring distinct roots bounds their number by its
degree). This contradiction again applies through (15) to every
nonempty open metric domain.

## 7. Boundary cases and limits of the conclusion

The correlation assumption matters. At \(\rho=0\), the smooth metric

\[
G(x,y)=\operatorname{diag}(f(x)^{-2},f(y)^{-2})
\]

makes both fields Killing for every smooth positive \(f\). For example,
the first component of its first Killing equation is
\(f\,\partial_x(f^{-2})+2f'f^{-2}=0\), and all other components vanish;
the second equation is identical with coordinates exchanged. For
bounded \(f\), this metric is globally uniformly Euclidean equivalent
exactly when \(f\) also has a positive lower bound. At \(\rho=\pm1\),
the frame is singular and the proof does not apply; the antiparallel
raw subsystem additionally satisfies \(z_2=-z_1\), as the input
reduction explains.

If \(f\) is a positive constant, the fields are constant and any
constant positive definite metric works for \(0<\lvert\rho\rvert<1\), including
the raw metric \(G=C^{-1}\). This is the affine activation case excluded
by the nonlinear target.

For a general smooth globally nonaffine activation, the global
obstruction must not be converted into a prohibition on every local
metric. For example, let

\[
b(t)=\begin{cases}
\exp\bigl(-1/[1-(t-3)^2]\bigr),&|t-3|<1,\\
0,&|t-3|\ge1,
\end{cases}
\qquad
f(t)=1+\tfrac12b(t),\quad
\phi(t)=1+\int_0^t f(s)\,ds.
\]

The exponential and all its derivatives tend to zero at the support
endpoints, so these are smooth; \(f\) is positive, bounded, and
nonconstant. On \((-1,1)^2\) both controlled fields are constant, and
\(G=I\) works locally. The theorem forbids extending a common Killing
metric to the whole plane. This example only distinguishes local from
global geometry; it is not a proposed full-network construction.

No sufficiency of either compatibility condition (13) or (15) has been
assumed. A metric with poor tail comparison cannot evade the global
proof. Nonzero brackets and nonflat metrics are admitted throughout;
the vanishing field (9) must satisfy the local skew-symmetry test
regardless of curvature.

## 8. Scoped claim update and stopping point

| Claim | Status and precise scope | Evidence |
|---|---|---|
| Diagonal Killing compatibility | Proved: (13) at every diagonal point of any open common metric domain, for positive smooth \(f\) and \(0<\lvert\rho\rvert<1\). | Equations (6)–(11). |
| Global bounded-gate mechanism | Ruled out for every nonconstant smooth \(0<f\le M_f\), even without uniform metric comparison. | Convexity argument after (12). |
| The two named activations, local mechanism | Ruled out on every nonempty open subset of the plane. | Area compatibility (15) and explicit scalar derivatives in section 6. |
| Uniform one-sided expansion for arbitrary signed amplitudes | Equivalent to the Killing requirement in the precise infinitesimal sense (5), hence ruled out under the global hypotheses. | Scaling each control through both signs in (5). |
| Full two-sample theorem and success of either activation | Unchanged by this note. The input ledger's full target remains open. | These claims require trained causal dynamics and further estimates absent from the controlled metric test. |

These are exact structural statements, not empirical evidence or
independently audited results. The existing no-flattening result remains
a separate valid obstruction. This note supplies the missing argument
against common Killing metrics; it does not reinterpret that older
lemma as having established it.

The rejection concerns a fixed smooth Riemannian metric that removes
arbitrary common-control amplitude through Killing cancellation, or
through the equivalent bound (5). It does not reject control-dependent
estimates, time-integrated cancellation, information from the actual
trained recursion, or other stability mechanisms. No impossibility of
the original learning theorem, and no failure of either activation for
that theorem, follows. The authorized structural discrimination is
complete; no broader search is undertaken.
