# Necessary geometry of finite positive-loss tanh equilibria

Status: a scoped theoretical derivation, with complete proofs below, awaiting
supervisor and independent checking. This is a study artifact, not promoted
material. No experiment or external scientific source was used.

Input scope: the supervisor's self-contained model and question only, together
with required process and mathematical-presentation instructions. Existing
examples, other study artifacts, and the maintained book were not scientific
inputs to this scoped route. The results therefore do not reconstruct or certify
any pre-existing bad example.

The strongest conclusion is conditional on the data: if the input matrix has
full column rank and the width is at least the sample count, every local minimum
fits. For linearly dependent inputs, the results give restrictive necessary
conditions and an exact Hessian test; they do not classify all local minima.
Nonnegative Hessian, local minimality, attraction, and convergence from the
zero-readout initialization remain distinct notions throughout.

## 1. Model and stationary equations

There are \(m\geq1\) samples and width \(n\geq m\). The fixed input matrix

\[
X=[x_1/\sqrt d,\ldots,x_m/\sqrt d]\in\mathbb R^{d\times m}
\]

has unit columns. Whenever explicitly used below, the columns are distinct
and no two are antipodal. They need not be linearly independent. With parameters

\[
A\in\mathbb R^{n\times d},\qquad W\in\mathbb R^{n\times n},
\qquad w\in\mathbb R^n,
\]

define the exact forward pass, residual, and loss by

\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=\frac1nH^\top w,\qquad r=f-y,\qquad
\mathcal L=\frac1m\|r\|^2.
\]

Here \(y\in\mathbb R^m\) is the label vector and all nonlinear functions and
powers of matrices are entrywise. Write

\[
E=1-U^2,\qquad D=1-H^2.
\]

Every entry of \(E,D\) is strictly positive at finite parameters. For row
indices \(j,i\in\{1,\ldots,n\}\), respectively, let

\[
u_j=U_{j,:}^\top,\quad e_j=E_{j,:}^\top,\quad
h_i=H_{i,:}^\top,\quad d_i=D_{i,:}^\top\in\mathbb R^m.
\]

The vectors \(e_j,d_i\) are derivative values, not coordinate unit vectors.
Coordinate unit vectors will be denoted \(\varepsilon_i\).

The gradient flow has mobilities \((n,1,n)\):

\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L,
\qquad w(0)=0.
\]

The positive mobilities make a finite equilibrium equivalent to a stationary
point of \(\mathcal L\). The initialization does not restrict the algebraic
results to equilibria actually reached by that flow.

Direct differentiation gives

\[
\begin{aligned}
\nabla_w\mathcal L
 &=\frac{2}{mn}Hr,\\
\nabla_W\mathcal L
 &=\frac{2}{mn}\operatorname{diag}(w)D
       \operatorname{diag}(r)U^\top,\\
\nabla_A\mathcal L
 &=\frac{2}{mn}
   \left[E\odot\left(W^\top\operatorname{diag}(w)D
       \operatorname{diag}(r)\right)\right]X^\top.
\end{aligned}
\tag{1}
\]

For example, varying only row \(i\) of \(W\) by \(c^\top\) changes the output
by \(w_i\operatorname{diag}(d_i)U^\top c/n\). Pairing this with \(2r/m\)
gives the second equation. Varying \(A\) first changes \(U\) by

\[
\delta U=E\odot(\delta A X),
\tag{2}
\]

which gives the third equation after applying \(W\), multiplying entrywise by
\(D\), and pairing with \(w\) and \(r\).

Thus stationarity is exactly

\[
Hr=0,\qquad
w_iU(d_i\odot r)=0\quad\text{for every }i,
\tag{3}
\]

together with the vanishing of the last line of (1). In particular, \(f\)
belongs to the row space of \(H\), while \(r\) is perpendicular to that space.
Consequently \(f\) is the orthogonal projection of \(y\) onto that row space,
and \(r^\top f=0\). This does not impose second-order stability.

A **second-order stationary point** in this note means a stationary point
whose full Euclidean Hessian is positive semidefinite. Every local minimum
has this property. The converse will explicitly fail below.

## 2. Exact second variation and an exact Hessian criterion

For a direction \((B,C,v)\) in the variables \((A,W,w)\), define

\[
\begin{aligned}
\xi&=E\odot(BX),&
\eta&=-2U\odot E\odot(BX)^2,\\
\zeta&=CU+W\xi,&
\kappa&=2C\xi+W\eta,\\
\delta H&=D\odot\zeta,&
\delta^2H&=D\odot\kappa-2H\odot D\odot\zeta^2.
\end{aligned}
\tag{4}
\]

These are the first and second derivatives along the affine parameter line.
The \(2C\xi\) term is the mixed derivative of the matrix product \(WU\).
The identities \(\tanh'=1-\tanh^2\) and
\(\tanh''=-2\tanh(1-\tanh^2)\) give all remaining terms. Hence

\[
\delta f=\frac{H^\top v+(\delta H)^\top w}{n},\qquad
\delta^2 f=\frac{2(\delta H)^\top v+(\delta^2H)^\top w}{n},
\tag{5}
\]

and

\[
\nabla^2\mathcal L[(B,C,v),(B,C,v)]
=\frac2m\left(\|\delta f\|^2+r^\top\delta^2 f\right).
\tag{6}
\]

Equations (4)--(6), tested on every direction, are already an exact
second-order criterion. The following form eliminates the readout direction
and isolates an additional nullspace compatibility requirement.

Identify the hidden parameter pair \(\theta=(A,W)\) with a Euclidean vector
of dimension \(p=nd+n^2\), using Frobenius inner products. At the point under
consideration define

\[
F=H^\top/n\in\mathbb R^{m\times n},\qquad
J\delta\theta=(\delta H)^\top w/n,
\]

and define \(C_0\in\mathbb R^{p\times n}\) and the symmetric
\(Q\in\mathbb R^{p\times p}\) by their bilinear and quadratic forms:

\[
\delta\theta^\top C_0v
 =r^\top(\delta H)^\top v/n,\qquad
\delta\theta^\top Q\delta\theta
 =r^\top(\delta^2H)^\top w/n.
\]

In the second definition, \(\delta^2H\) is computed with hidden direction
\(\delta\theta\) and no readout variation. Set

\[
G=F^\top F,\qquad K=J^\top F+C_0.
\]

Then the Hessian, divided by the positive factor \(2/m\), is

\[
\begin{pmatrix}
J^\top J+Q&K\\ K^\top&G
\end{pmatrix}.
\tag{7}
\]

It is positive semidefinite if and only if both

\[
C_0v=0\quad\text{for every }v\in\ker F,
\tag{8}
\]

and

\[
J^\top J+Q-KG^\dagger K^\top\succeq0
\tag{9}
\]

hold. Here \(G^\dagger\) is the inverse of \(G\) on its range and zero
on its kernel. Together with (1), this is an exact, finite-dimensional
classification of second-order stationarity for arbitrary data. It remains
a pointwise derivative test, not a structural enumeration of local minima.

To prove the equivalence, first note the elementary fact that a symmetric
positive-semidefinite quadratic form \(q\) satisfies \(q(a,b)=0\) for
every \(b\) whenever \(q(a,a)=0\): otherwise
\(q(b+ta,b+ta)=q(b,b)+2tq(a,b)\) is negative for one sufficiently large
signed \(t\). Applying this to \((0,v)\) with \(v\in\ker G=\ker F\)
forces \(Kv=0\), which is (8). Under this compatibility condition,
\(K^\top\delta\theta\) lies in the range of \(G\), and completing the
square in (7) gives

\[
\begin{aligned}
&\delta\theta^\top(J^\top J+Q)\delta\theta
 +2\delta\theta^\top Kv+v^\top Gv\\
&\quad=
\delta\theta^\top(J^\top J+Q-KG^\dagger K^\top)\delta\theta
 +(v+G^\dagger K^\top\delta\theta)^\top
   G(v+G^\dagger K^\top\delta\theta).
\end{aligned}
\]

Taking \(v=-G^\dagger K^\top\delta\theta\) proves necessity of (9);
the displayed identity proves sufficiency.

One explicit consequence of (8), beyond the conditions proved next, is

\[
\sum_i v_iW_{ij}X(e_j\odot d_i\odot r)=0
\quad\text{for every }j\text{ and every }v\in\ker H^\top.
\tag{10}
\]

Indeed, varying only row \(j\) of \(A\) in the definition of \(C_0\)
gives this equation by the arbitrariness of that row variation.

## 3. A universal augmented feature nullspace

**Proposition 1.** At every second-order stationary point,

\[
Hr=0,\qquad U(d_i\odot r)=0\quad\text{for all }i,
\tag{11}
\]

including all rows with \(w_i=0\). Thus the explicitly constructed matrix

\[
\mathcal K(A,W)=
\begin{pmatrix}
H\\ U\operatorname{diag}(d_1)\\ \vdots\\
U\operatorname{diag}(d_n)
\end{pmatrix}
\tag{12}
\]

satisfies \(\mathcal K(A,W)r=0\). Positive loss therefore requires

\[
\operatorname{rank}\mathcal K<m,\qquad
\operatorname{rank}H<m,\qquad\operatorname{rank}U<m.
\tag{13}
\]

*Proof.* The case \(w_i\ne0\) follows from (3). If \(w_i=0\), vary
only row \(i\) of \(W\). The output is exactly constant under this
variation, so its pure Hessian quadratic form is zero. Positive
semidefiniteness forces its Hessian pairing with every readout variation
to vanish. Pairing specifically with \(v=\varepsilon_i\), (5)--(6)
give

\[
\frac{2}{mn}c^\top U(d_i\odot r)=0
\quad\text{for every }c\in\mathbb R^n.
\]

This proves (11). At positive loss \(r\ne0\), so (12) has a nontrivial
kernel and \(H\) has deficient column rank. Since
\(\operatorname{diag}(d_i)\) is invertible, any equation
\(U\operatorname{diag}(d_i)r=0\) with \(r\ne0\) also forces
\(\operatorname{rank}U<m\). \(\square\)

In particular, if \(\operatorname{rank}U=m\), every nonzero-residual
stationary point has a negative Hessian eigenvalue. Stationarity already
forces \(w=0\) in that case; the mixed readout/second-layer directions
then reveal the negative curvature.

## 4. Redundant first-layer rows force derivative annihilation

Define the set of redundant row indices by

\[
\mathcal R(U)=
\{j:\text{there exists }b\in\ker U^\top\text{ with }b_j\ne0\}.
\tag{14}
\]

Equivalently, row \(j\) of \(U\) belongs to the span of its other rows.
For a zero row this condition holds as well. Define the matrix

\[
\mathcal T_U=
\begin{pmatrix}
U\\
X\operatorname{diag}(e_j),\quad j\in\mathcal R(U)
\end{pmatrix},
\tag{15}
\]

where the lower blocks are vertically stacked in any order.

**Proposition 2.** At every second-order stationary point, for each
\(i\) with \(w_i\ne0\) and every \(j\in\mathcal R(U)\),

\[
X(e_j\odot d_i\odot r)=0.
\tag{16}
\]

Consequently, if \(r\ne0\) and \(w\ne0\), then

\[
\mathcal T_U(d_i\odot r)=0\quad\text{for every active }i,
\qquad \operatorname{rank}\mathcal T_U<m.
\tag{17}
\]

*Proof.* Fix an active \(i\) and \(b\in\ker U^\top\). Consider the
parameter direction with only

\[
\delta W=\varepsilon_i b^\top.
\]

It has \(\delta WU=0\), so the output is exactly unchanged along
that affine line. Its pure Hessian quadratic form is zero. The Hessian
pairing with an arbitrary variation \(B\) of \(A\) must therefore vanish.
The first output derivative in the \(\delta W\) direction is zero,
so the squared-Jacobian part of the pairing vanishes. Its mixed output
derivative comes only from \(\delta W\delta U\), and (4)--(6) give

\[
0=\frac{2w_i}{mn}\sum_j b_j
   B_{j,:}X(e_j\odot d_i\odot r).
\tag{18}
\]

The rows of \(B\) are arbitrary. If \(b_j\ne0\), the facts
\(w_i\ne0\) and (18) yield (16). The definition of \(\mathcal R(U)\)
permits a separate choice of \(b\) for each such \(j\). Equation (11)
and (16) give the first assertion of (17). The vector
\(d_i\odot r\) is nonzero, because all entries of \(d_i\) are positive,
so \(\mathcal T_U\) has deficient column rank. \(\square\)

Under the standing width assumption \(n\geq m\), positive-loss
second-order stationarity gives \(\operatorname{rank}U<m\leq n\).
Thus \(\ker U^\top\ne\{0\}\) and \(\mathcal R(U)\) is nonempty.
The derivative constraint is therefore substantive whenever \(w\ne0\).

There is a direct description in terms of critical zeros. At the fixed
configuration define, for each second-layer row \(i\), the scalar function

\[
\Phi_i(v)=\sum_{a=1}^m r_a d_{i,a}
              \tanh(v^\top X_{:,a}),\qquad v\in\mathbb R^d.
\tag{18a}
\]

Here \(r\) and \(d_i\) remain fixed while \(v\) varies. Proposition 1
says that every first-layer row satisfies
\(\Phi_i(A_{j,:}^\top)=0\). Moreover,

\[
\nabla\Phi_i(A_{j,:}^\top)
  =X(e_j\odot d_i\odot r).
\tag{18b}
\]

Thus every redundant row is a simultaneous critical zero of all the
functions \(\Phi_i\) for active indices \(i\). The nonredundant rows
are linearly independent as vectors in \(\mathbb R^m\): any nontrivial
linear dependence among them would express one as a combination of
other rows, contradicting nonredundancy. There are therefore at most
\(\operatorname{rank}U\) nonredundant rows, and at least
\(n-\operatorname{rank}U\) first-layer neurons must satisfy these
simultaneous critical-zero conditions.

For distinct nonantipodal input columns and \(r\ne0\), each \(\Phi_i\)
is a nonzero real-analytic function. Indeed, all entries of \(d_i\)
are positive, so its coefficient vector \(d_i\odot r\) is nonzero;
Lemma 4 below proves that no such vector annihilates every tanh ridge
feature on these inputs. This describes necessary singular geometry
without claiming that the first-layer rows must coincide, or that
critical zeros are sufficient for local minimality.

## 5. Zero readout: exact second-order test and no positive local minimum

**Proposition 3.** At \(w=0\), so \(r=-y\), second-order stationarity
is equivalent to all of

\[
Hr=0,\qquad U(d_i\odot r)=0\quad\text{for every }i,
\tag{19}
\]

and

\[
W_{ij}X(e_j\odot d_i\odot r)=0
\quad\text{for every }i,j.
\tag{20}
\]

When these hold, the only nonzero Hessian block that can remain is the
readout block \(2HH^\top/(mn^2)\).

*Proof.* At \(w=0\), all hidden-only loss derivatives up to second order
vanish, because keeping \(w=0\) keeps \(f=0\) exactly. Stationarity
requires only \(Hr=0\). The Hessian is positive semidefinite exactly
when all hidden/readout mixed blocks vanish: necessity follows from the
zero-quadratic-direction argument, and sufficiency follows because the
readout block is a Gram matrix. Pairing row \(i\) of \(W\) with readout
coordinate \(i\) yields \(U(d_i\odot r)\). Pairing row \(j\) of \(A\)
with readout coordinate \(i\) yields
\(W_{ij}X(e_j\odot d_i\odot r)\). These are all mixed blocks, proving
the claim. \(\square\)

The second-order criterion does not make these points local minima. The
following elementary separation lemma will give a higher-order conclusion.

**Lemma 4 (tanh separates distinct nonantipodal vectors).** Let
\(z_1,\ldots,z_m\in\mathbb R^q\) be nonzero, pairwise distinct, and
satisfy \(z_a\ne-z_b\) for \(a\ne b\). The vectors

\[
\left(\tanh(v^\top z_a)\right)_{a=1}^m,
\qquad v\in\mathbb R^q,
\]

span \(\mathbb R^m\).

*Proof.* Choose \(v_0\) outside the finite union of hyperplanes
orthogonal to \(z_a\), \(z_a-z_b\), and \(z_a+z_b\). Such a vector
exists because every normal is nonzero, and a finite collection of proper
hyperplanes cannot fill \(\mathbb R^q\); for example their defining
nonzero linear polynomials have a nonzero product. The numbers
\(s_a=v_0^\top z_a\) are nonzero with distinct absolute values.

Suppose \(\sum_a c_a\tanh(ts_a)=0\) for all real \(t\). Let
\(\lambda_a=|s_a|\), order them increasingly, and set
\(b_a=c_a\operatorname{sign}(s_a)\). Since

\[
\tanh(t\lambda_a)=1-2e^{-2\lambda_a t}
  +O(e^{-4\lambda_a t})\qquad(t\to+\infty),
\]

taking the limit gives \(\sum_a b_a=0\). After subtracting this
constant and dividing by \(e^{-2\lambda_1t}\), the limit gives
\(-2b_1=0\). Removing that zero coefficient and repeating proves
every \(b_a\), and hence every \(c_a\), is zero. No nonzero vector
annihilates the stated family, proving the spanning assertion. \(\square\)

We also use the real-analytic identity principle in the following elementary
form: a real-analytic function on all of a Euclidean space that vanishes on
a nonempty open set vanishes everywhere. To see this, join an interior point
of that set to an arbitrary target point by an affine line. Restriction to
the line is real analytic and vanishes on an interval. It remains zero along
the line: at a boundary of an interval of vanishing, every derivative is zero
by continuity, so its convergent Taylor series extends the zero interval.
This proves the required continuation to the target.

**Proposition 5.** For distinct nonantipodal nonzero input columns, no
positive-loss point with \(w=0\) is a local minimum, for any width
\(n\geq1\). Linear independence of the input columns is unnecessary.

*Proof.* Suppose \((A_0,W_0,0)\) is a local minimum. There is a
neighborhood of \((A_0,W_0)\) in which, for every hidden-parameter pair,
all sufficiently small readout vectors must have loss at least
\(\|y\|^2/m\). Fixing such a hidden pair and varying just readout
coordinate \(i\), this loss is

\[
\frac{\|y\|^2}{m}
 -\frac{2t}{mn}y^\top h_i
 +\frac{t^2}{mn^2}\|h_i\|^2.
\tag{21}
\]

If \(y^\top h_i\ne0\), choosing a sufficiently small \(t\) with
the same sign lowers the loss. Thus \(y^\top h_i(A,W)=0\) throughout
that hidden-parameter neighborhood. This is a real-analytic function of all
entries of \((A,W)\), so the identity principle makes it zero for
every \((A,W)\).

Choose \(a\in\mathbb R^d\) such that the numbers
\(a^\top X_{:,b}\) are nonzero with distinct absolute values; the
hyperplane argument in Lemma 4 applies to the input columns. Put \(a^\top\)
in the first row of \(A\), and put \(t\varepsilon_1^\top\) in row
\(i\) of \(W\). The identity just established gives

\[
\sum_b y_b\tanh\!\left(t\tanh(a^\top X_{:,b})\right)=0
\quad\text{for every }t\in\mathbb R.
\]

The inner tanh values are nonzero and have distinct absolute values,
because tanh is odd and strictly increasing. The scalar independence
argument in Lemma 4 therefore gives \(y=0\). At \(w=0\) this means
zero loss, proving the proposition. \(\square\)

There is also a useful condition for a *single* zero readout coordinate.

**Proposition 6.** At a local minimum with \(w_i=0\), write
\(U_{:,a}=z_a\). Partition the nonzero feature columns into classes
modulo sign, so in each class \(z_a=\sigma_a z_*\),
\(\sigma_a\in\{-1,1\}\). Necessarily

\[
\sum_{a\text{ in each class}}\sigma_a r_a=0.
\tag{22}
\]

In particular, if the columns of \(U\) are nonzero, distinct, and
nonantipodal, then \(r=0\).

*Proof.* Changing only row \(i\) of \(W\), while keeping \(w_i=0\),
does not change \(f\), \(r\), or the loss. Every sufficiently nearby
point obtained this way is itself a local minimum, because a small ball
around it remains within the original minimizing neighborhood. Its readout
gradient must vanish. Consequently

\[
r^\top\tanh(v^\top U)=0
\]

for \(v\) in a neighborhood of the original row, and then for every
\(v\) by analyticity. Zero feature columns contribute zero; grouping
the remaining terms modulo sign turns this identity into one over distinct
nonantipodal representatives. Lemma 4 says that every grouped coefficient
must vanish, which is (22). \(\square\)

Because tanh is injective and odd, feature collisions can equivalently
be written as \(A(X_{:,a}-X_{:,b})=0\) or
\(A(X_{:,a}+X_{:,b})=0\), and a zero feature column means
\(AX_{:,a}=0\). Thus Proposition 6 is a concrete necessary condition,
not a claim that input linear dependence alone forces such collisions.

**Proposition 6a.** For distinct nonantipodal nonzero input columns,
every positive-loss local minimum has every column of \(W\) nonzero.

*Proof.* Suppose column \(j\) of \(W\) is zero. Varying row \(j\)
of \(A\) then leaves \(WU\), \(H\), \(f\), \(D\), and \(r\)
exactly fixed. As in Proposition 6, every sufficiently nearby point
on this flat set is itself a local minimum and hence stationary.
Proposition 5 excludes \(w=0\) at a positive-loss local minimum,
so choose an index \(i\) with \(w_i\ne0\). The \((i,j)\) entry
of the \(W\) gradient must vanish at every such nearby point:

\[
\sum_a r_a d_{i,a}\tanh(v^\top X_{:,a})=0
\]

for \(v\) in a neighborhood of the original row of \(A\).
Analyticity extends the identity to every \(v\in\mathbb R^d\).
Lemma 4 then gives \(d_i\odot r=0\), and the strict positivity
of \(d_i\) gives \(r=0\), a contradiction. \(\square\)

## 6. Complete second-order classification for full-column-rank data

**Theorem 7.** Assume \(\operatorname{rank}X=m\), \(n\geq m\),
and \(y\ne0\). A positive-loss second-order stationary point is
exactly a configuration satisfying

\[
w=0,\qquad W=0,\qquad Uy=0.
\tag{23}
\]

At every such point the entire Hessian vanishes, and there is a cubic
descent direction. Hence every positive-loss stationary point either has
a negative Hessian eigenvalue or has a zero Hessian and a cubic descent
direction. Every local minimum has zero loss.

*Proof of the classification.* Let a positive-loss second-order stationary
point be given. Proposition 1 gives \(\operatorname{rank}U<m\),
so \(\mathcal R(U)\ne\varnothing\) because \(n\geq m\).
For every \(j\), the matrix \(X\operatorname{diag}(e_j)\) has
column rank \(m\), since \(X\) does and \(e_j\) has strictly
positive entries. Thus \(\mathcal T_U\) has column rank \(m\).
Proposition 2 rules out \(w\ne0\), so \(w=0\) and \(r=-y\ne0\).

Equation (20) now gives

\[
W_{ij}X(e_j\odot d_i\odot r)=0.
\]

The vector inside \(X\) is nonzero; full column rank makes its image
nonzero. Therefore every \(W_{ij}=0\). This gives \(H=0\),
\(D=1\), and (19) reduces to \(Ur=-Uy=0\).
Conversely, (23) gives stationarity from (1) and satisfies (19)--(20).
The surviving readout Hessian block is zero because \(H=0\), so the
entire Hessian is zero. The loss is \(\|y\|^2/m>0\).

*Proof of cubic descent.* Fix a point (23), any first-layer index \(j\),
and any second-layer index \(i\). The linear map

\[
B\longmapsto \xi=E\odot(BX)
\]

is onto \(\mathbb R^{n\times m}\): multiplication by \(X\)
maps each row onto \(\mathbb R^m\), and multiplication entrywise
by \(E\) is invertible. Choose \(B\) with only row \(j\) nonzero
so that \(\xi_{j,:}=y^\top\). Concretely, if
\(q^\top=y^\top\oslash e_j^\top\), then

\[
B_{j,:}=q^\top(X^\top X)^{-1}X^\top
\]

has the required property. The symbol \(\oslash\) denotes entrywise
division, with positive denominators here. Along the affine path

\[
A(t)=A+tB,\qquad
W(t)=t\varepsilon_i\varepsilon_j^\top,\qquad
w(t)=t\varepsilon_i,
\tag{24}
\]

Taylor expansion gives

\[
U(t)=U+t\xi+O(t^2),\qquad
f(t)=\frac{t^2}{n}u_j+\frac{t^3}{n}y+O(t^4).
\]

Indeed, the active second-layer preactivation is
\(t u_j+t^2y+O(t^3)\); its tanh equals that expression up to
an \(O(t^3)\) error, and the readout contributes one more factor \(t/n\).
Since \(Uy=0\), the term \(y^\top u_j\) vanishes. Therefore

\[
\mathcal L(t)-\mathcal L(0)
=-\frac{2\|y\|^2}{mn}t^3+O(t^4).
\tag{25}
\]

The loss is smaller for all sufficiently small positive \(t\), and
larger for all sufficiently small negative \(t\). Thus these points
are not local minima despite their zero Hessian. Every local minimum
is second-order stationary, so the classification excludes all
positive-loss local minima. \(\square\)

If \(y=0\), every stationary point already fits: readout stationarity
gives \(0=w^\top Hr=n\|f\|^2\), since \(r=f\). This covers the
excluded label edge case without needing any rank assumption.

## 7. Scope of what is and is not resolved

For distinct nonantipodal sphere data with arbitrary linear dependence,
every positive-loss local minimum necessarily has \(w\ne0\),
\(\operatorname{rank}\mathcal K<m\), and
\(\operatorname{rank}\mathcal T_U<m\), with no zero column of \(W\).
It also satisfies the exact
stationarity equations, the readout-nullspace compatibility (8), and
the Hessian inequality (9). These are proved necessary conditions;
neither rank deficiency nor a positive-semidefinite Hessian is asserted
to be sufficient for local minimality.

For full-column-rank data, Theorem 7 completely identifies the positive-loss
second-order stationary set and eliminates positive-loss local minima.
For dependent data, a structural classification of all positive-loss local
minima remains open in this note. Higher-order behavior at singular points
is not captured by (8)--(9).

No result here proves attraction, convergence to a finite point, exclusion
of parameter escape, convergence of loss to zero, or avoidance of bad sets
from the prescribed slice \(w(0)=0\). In particular, a necessary
rank-deficient condition for a limiting equilibrium does not imply that
a trajectory started away from that set cannot approach it.
