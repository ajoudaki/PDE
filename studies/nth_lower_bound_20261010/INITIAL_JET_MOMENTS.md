# Initialized derivative bounds for a sinusoidal first layer and linear second layer

This scoped lemma concerns the supervisor's specified continuation with
$m=d=2$, orthogonal normalized inputs, labels $(\eta,0)$, first activation
$\phi(x)=x+\varepsilon\sin x$, $1/8\le\varepsilon\le1/4$, and second
activation equal to the identity. It does not assert a growing-order NTH
accuracy theorem. It supplies initial derivative bounds for the original
network, including all sample words, without changing its frozen-top closure.

Inputs are the supervisor's explicit model and target, the required proof and
canonical-notation instructions, and the same-study averaged-upper author's
requested transformed-state quantities. No other study, experiment, or
external theorem is used. All Gaussian counting needed below is proved.

## Exact model and differentiation rules

Take $v_1=e_1,v_2=e_2\in\mathbb R^2$. Let $z_a=W^{(1)}v_a\in\mathbb R^n$,
$W=W^{(2)}\in\mathbb R^{n\times n}$, and $u\in\mathbb R^n$. Then

\[
h_a=\phi(z_a),\qquad f_a=\frac{u^\top Wh_a}{n},\qquad
\rho_a=\frac{y_a-f_a}{2},\qquad (y_1,y_2)=(\eta,0).
\tag{1}
\]

Initialization has independent standard Gaussian coordinates of $z_1,z_2$,
independent $W_{ij}\sim N(0,1/n)$, and $u=0$. Mobilities are $(n,1,n)$
and the loss is $(1/4)\sum_a(f_a-y_a)^2$. Physical gradient flow is

\[
\dot z_a=\rho_a\,\phi'(z_a)\odot W^\top u,\qquad
\dot u=W\sum_b\rho_bh_b,\qquad
\dot W=\frac1n u\left(\sum_b\rho_bh_b\right)^\top.
\tag{2}
\]

For the sample direction $V_b=M\nabla f_b$, write
$D_b A=DA[V_b]$. The exact rules are

\[
D_bz_a=\delta_{ab}\phi'(z_a)\odot W^\top u,\quad
D_bu=Wh_b,\quad D_bW=uh_b^\top/n.
\tag{3}
\]

In particular, if $\langle v,w\rangle_n=v^\top w/n$ for vectors in
the same layer, then

\[
\begin{aligned}
D_b(Wv)&=u\langle h_b,v\rangle_n+W D_bv,\\
D_b(W^\top v)&=h_b\langle u,v\rangle_n+W^\top D_bv,\\
D_b\phi^{(j)}(z_a)
&=\delta_{ab}\phi^{(j+1)}(z_a)\odot\phi'(z_a)\odot W^\top u.
\end{aligned}
\tag{4}
\]

The last rule holds for $j\ge0$, with $\phi^{(0)}=\phi$. Products and
normalized pairings obey the ordinary Leibniz rule. The physical derivative
operator is $D=\sum_b\rho_bD_b$; in using it, expand each $\rho_b$ by
(1). These are explicit finite rewrite rules, including the derivatives of
the residual. They do not freeze or prescribe the residual.

For comparison with the transformed coordinates used in the remainder
argument, define

\[
T_\varepsilon(x)=\int_0^x\frac{dz}{1+\varepsilon\cos z},\qquad
\zeta_a=T_\varepsilon(z_a).
\tag{5}
\]

Since $3/4\le\phi'(x)\le5/4$ on the real line,
$|T_\varepsilon(x)|\le4|x|/3$. Its first derivative extends
holomorphically to $|\operatorname{Im}z|<1$, with modulus at most
$[1-\cosh(1)/4]^{-1}<2$. Cauchy's formula on radius-$1/2$ disks gives

\[
\sup_{x\in\mathbb R}|T_\varepsilon^{(j)}(x)|
\le 2^j(j-1)!,\qquad j\ge1.
\tag{6}
\]

The vectors $\zeta_a\in\mathbb R^n$ store the raw transformed coordinates,
without an additional width normalization. Their directional rule is
$D_b\zeta_a=\delta_{ab}W^\top u$.
The bounds below can either differentiate this rule and (4), or compose
the original-coordinate derivatives with the gates in (6).

## A Gaussian expression grammar and its moment bound

Condition on the initialized $z_1,z_2$, and suppose
$\max_{a,j}|z_{a,j}|\le R_0$. A vector expression belongs to the
grammar if it is constructed using:

- deterministic coordinatewise vector leaves;
- $W_0$ or $W_0^\top$ applied to a vector in the corresponding layer;
- coordinatewise products of vectors in one layer;
- normalized pairings $\langle v,w\rangle_n$;
- products of scalars and scalar multiplication of vectors.

Finite sums are handled by summing the bounds for their monomials. A leaf
may be an initialized activation derivative, an initialized coordinate, or
a transformed-coordinate derivative. Its bound is recorded explicitly;
independence of different leaves is neither assumed nor needed.

**Grammar lemma.** Consider one monomial with $E$ occurrences of $W_0$
or $W_0^\top$ and deterministic leaf bounds whose product is $B_*$. For
every even integer $p\ge2$, each output coordinate, or the output scalar,
satisfies

\[
\|A\|_{L^p(W_0\mid z_1,z_2)}
\le B_*\max\{1,pE\}^{E/2}.
\tag{7}
\]

**Proof.** Replace $W_{0,ij}$ by $G_{ij}/\sqrt n$, where the $G_{ij}$
are independent standard Gaussians, and write out the finite index sums.
One vector monomial is represented by a forest with one tree having a
fixed output index and some unrooted trees; a scalar monomial has only
unrooted trees. If their number is $S$, the normalization is
$n^{-E/2-S}$.

This forest description follows inductively from the grammar. A vector
leaf is one vertex. A matrix action adds a new root joined to the previous
root by one Gaussian edge. A coordinatewise product identifies the roots
of two trees and otherwise uses separate summation indices, still giving
a tree. A normalized pairing identifies two vector roots, makes the shared
index a summed index, and contributes $1/n$, giving an unrooted tree.
Multiplication by a scalar appends its unrooted components. Copying an
expression creates separate dummy indices; reuse of the same Gaussian
matrix is retained in the edge variables and is handled by pairing below.

For a vector coordinate, take $p$ copies and identify their fixed roots
at that coordinate. For a scalar, take $p$ disjoint copies. Wick's formula
follows by differentiating
$\mathbb E e^{\sum t_{ij}G_{ij}}=e^{\sum t_{ij}^2/2}$: the expectation
is the sum over pairings of the $pE$ Gaussian occurrences, with each pair
requiring equality of its row and column indices. If $pE$ is odd the
expectation is zero; here $p$ is even.

Fix one pairing and quotient the index graph by these equalities. It has
at most $pE/2$ distinct edges. Identifications cannot increase the number
of unrooted connected components, so that number is at most $pS$.
Every connected graph has at most its number of edges plus one vertices:
start at one vertex and expose a spanning tree. The rooted component has
one fixed vertex. Therefore the number of free summed vertices is at most
$pE/2+pS$, for both scalar and vector outputs. Their index sums are at
most $n^{pE/2+pS}$, cancelling the full normalization
$n^{-pE/2-pS}$. Deterministic factors have absolute value at most $B_*^p$.

There are $(pE-1)!!\le(pE)^{pE/2}$ pairings when $E>0$. Taking absolute
values termwise and then the $p$th root proves (7). When $E=0$, each
normalized average of bounded deterministic leaves is bounded, giving
the stated convention. $\square$

The graph argument applies to both matrix orientations: a Gaussian pair
always identifies its original second-layer row and first-layer column,
including when one occurrence is written as a transpose. Repeated calls
to $W_0$ and $W_0^\top$ therefore do not require fresh independence.

## Explicit derivative-size bookkeeping

Take as starting expressions a coordinate of $z_a$, $u$, or
$\zeta_a$, a scalar output $f_a$, or a matrix derivative after
one application of (3). Count one unit for each vector/scalar operation
and each leaf occurrence; count derivative labels on gates separately.

Applying one $D_b$ to a monomial has at most a constant times its size
possible Leibniz sites. At any site the applicable rule in (3)--(4)
increases the size by at most an absolute constant. For a matrix action,
the first term of (4) replaces the differentiated matrix by a normalized
pairing, so no unrestricted matrix entry or unnormalized sum is created.
Differentiating a gate raises its derivative label by one and adds only
the three factors shown in (4). Applying the physical operator $D$
additionally multiplies by one of the finitely many monomials in
$(y_b-f_b)/2$, each of constant size.

It follows by induction that after $r$ differentiations:

1. each monomial has size at most $C(r+1)$, including at most $C(r+1)$
   Gaussian matrix occurrences;
2. its gate derivative labels have sum at most $C(r+1)$;
3. the total number of monomials, including coefficients from identical
   terms, is at most
   $\prod_{s=1}^{r}C(s+1)\le(C(r+1))^{C(r+1)}$.

These assertions apply equally to any prescribed sample word
$D_{a_r}\cdots D_{a_1}$, and to physical derivatives $D^r$. They follow
from local rewrites rather than an assumption about the size of a formal
diagram expansion.

At initialization, every surviving vector leaf is deterministic conditional
on $z_1,z_2$; leaves containing $u_0=0$ vanish. The elementary bounds are

\[
|z_{a,j}|\le R_0,\quad |\phi(z_{a,j})|\le R_0+1,\quad
|\phi'(z_{a,j})|\le5/4,\quad
|\phi^{(s)}(z_{a,j})|\le1/4\quad(s\ge2).
\]

For transformed-coordinate gates use (6). Their product is bounded by
$[C(1+R_0)]^{C(r+1)}[C(r+1)]^{C(r+1)}$, since the sum of their
derivative orders is $O(r+1)$ and a product of factorials is at most
the factorial of their sum. Applying (7) and summing monomials gives
the following uniform result.

**Initialized derivative theorem.** There is $C\ge1$, depending on the
fixed label magnitude $|\eta|$ but uniform for
$1/8\le\varepsilon\le1/4$, such that, for every $r\ge0$ and even
$p\ge2$, all of the following conditional $L^p(W_0)$ norms are at most

\[
M_{r,p,R_0}:=
\big[C(r+1)p(1+R_0)\big]^{C(r+1)}:
\tag{8}
\]

- every initialized coordinate of $d^r z_a/dt^r$,
  $d^r\zeta_a/dt^r$, and $d^ru/dt^r$;
- every initialized derivative $d^r f_a/dt^r$;
- every corresponding initialized state or output derivative along any
  sample word of length $r$;
- the Frobenius norm of $d^r(W-W_0)/dt^r$ for $r\ge1$, and the
  corresponding sample-word matrix derivatives.

The first three conclusions follow from the grammar proof directly. To
prove the matrix statement, its first derivative is a sum of rank-one
matrices $v w^\top/n$. Repeated differentiation keeps this form, with
vector factors built by the same grammar and total size $O(r+1)$.
For such a term,

\[
\|v w^\top/n\|_F
=\frac{\|v\|_2}{\sqrt n}\frac{\|w\|_2}{\sqrt n},\qquad
\left\|\frac{\|v\|_2}{\sqrt n}\right\|_{L^p}
\le\max_j\|v_j\|_{L^p}\quad(p\ge2).
\tag{9}
\]

The second inequality is Minkowski's inequality in $L^{p/2}$ applied to
$n^{-1}\sum_j|v_j|^2$. Hölder's inequality with $2p$ for the two
factors, followed by the monomial count, proves the last item after
enlarging $C$. No bound on $\|W_0\|_F$, which is of order $\sqrt n$,
is asserted or needed.

In particular, every initialized NTH entry through rank $R+1$ is covered:

\[
K^{(s)}_{a_1\ldots a_s}(0)
=\big(D_{a_s}\cdots D_{a_2}f_{a_1}\big)(0),\qquad s\le R+1.
\tag{10}
\]

There is no growth with the ambient width in (8), conditional on the
explicit initial-coordinate bound. The dependence on that bound is shown.

## Simultaneous high-probability bound at growing order

Fix $A>0$, an integer $R\ge1$, and one
$\varepsilon\in[1/8,1/4]$. All constants below are uniform in that
choice of $\varepsilon$; a single event simultaneous over the continuum
of activation parameters is not asserted. A Gaussian union bound gives
$\max_{a,j}|z_{a,j}(0)|\le R_0=C_A\sqrt{\log(en)}$ with probability
at least $1-n^{-A-2}$, for a suitable constant $C_A$.
The number of coordinates, scalar outputs, and matrix norms in the theorem
through order $R$, including every sample word, is at most
$N_R=Cn(R+1)2^{R+2}$ after increasing an absolute $C$.

Choose an even $p\ge\max\{2,\log(N_R n^{A+2})\}$ and at most two
larger than this maximum. Use the same $p$ for every order $r\le R$,
but apply conditional Markov bounds at their individual thresholds
$eM_{r,p,R_0}$. A union bound gives failure probability at most
$N_Re^{-p}\le n^{-A-2}$. Consequently, on one event of probability
at least $1-2n^{-A-2}$, every quantity of order $r$ in the theorem is
bounded by $eM_{r,p,R_0}$, simultaneously for all $0\le r\le R$ and
all sample words of those lengths. In particular its bound is

\[
\exp\!\left\{C_A(r+1)
\big[1+\log(r+1)+\log(\log(en)+R)\big]\right\},
\qquad 0\le r\le R.
\tag{11}
\]

The constants may depend on $|\eta|$ and $A$, but not on $n,r,R$.
Thus choosing $R=\lfloor\log(en)\rfloor$ does not force a low-order
derivative to use the much larger order-$R$ envelope: it retains
$\exp\{C_A(r+1)[1+\log(r+1)+\log\log(e^e n)]\}$ on the same event.

For each fixed $C_0<\infty$, the common event with
$R=\lfloor\log(en)\rfloor$ bounds every order
$r\le\min\{R,C_0\log\log(e^e n)\}$ by

\[
\exp\!\{C_{A,C_0}(\log\log(e^e n))^2\}.
\tag{12}
\]

This proves the requested growth control for initialized physical and
sample-word derivatives, including the original NTH initial data. A
finite Taylor remainder or an error lower bound still needs its own
argument; neither is inferred from initialized derivatives alone.
