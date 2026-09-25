# Shared-operator consistency checks for motion-state laws

## Scope and status

This note is a scoped, prompt-only derivation for the canonical one-sample,
two-hidden-layer network specified below. No external scientific sources,
other study artifacts, numerical experiments, or initialization assumptions
were used. All results below are exact algebraic statements under their stated
regularity assumptions. They provide tests for a proposed history-free law;
they do not assert that a particular finite state closes the network dynamics.

The finite source lists are diagnostic choices. Their use makes no low-rank
assumption about the actual weight matrix. Passing a finite collection of
these tests does not establish state sufficiency, the correct initialization
law, or validity over a positive time interval.

## 1. Exact direct and indirect effects of the middle matrix

Let both hidden layers have width n. All vectors below are real column
vectors. Set

\[
\langle a,b\rangle_n=\frac{a^\top b}{n},\qquad
\|a\|_n^2=\langle a,a\rangle_n,
\]

and consider a fixed input x in R^d and fixed target y, with

\[
\begin{aligned}
z_1&=W_1x/\sqrt d,&h_1&=\phi(z_1),\\
z_2&=W_2h_1,&h_2&=\phi(z_2),\\
f&=\langle W_3,h_2\rangle_n,&r&=f-y,\\
\delta_2&=W_3\odot\phi'(z_2),&
b_1&=W_2^\top\delta_2,\\
\delta_1&=\phi'(z_1)\odot b_1,&
\chi&=\|x\|^2/d.
\end{aligned}
\]

The square-loss dynamics at learning-rate multipliers (n,1,n) are

\[
\dot z_1=-2r\chi\delta_1,\qquad
\dot W_3=-2r h_2,\qquad
\dot W_2=-\frac{2r}{n}\delta_2h_1^\top.
\tag{1}
\]

Assume phi is C^2 on the ranges under consideration. Applying the product
rule to z_2 and b_1, then substituting (1), gives

\[
\dot z_2
=-2r\|h_1\|_n^2\delta_2+W_2\dot h_1,
\tag{2}
\]

\[
\dot b_1
=-2r\|\delta_2\|_n^2h_1+W_2^\top\dot\delta_2.
\tag{3}
\]

The source derivatives appearing here are

\[
\dot h_1
=\phi'(z_1)\odot\dot z_1
=-2r\chi\,\phi'(z_1)^2\odot b_1,
\tag{4}
\]

\[
\dot\delta_2
=-2r h_2\odot\phi'(z_2)
 +W_3\odot\phi''(z_2)\odot\dot z_2.
\tag{5}
\]

The first term in (2) is the direct effect of changing W_2 at fixed h_1;
the second is W_2 acting on the motion of its forward input. Equation (3)
has the corresponding direct and indirect reverse effects. The indirect
terms are present even when the current forward and reverse actions z_2
and b_1 are retained.

Although dot W_2 has rank at most one at each instant, integration gives

\[
W_2(t)-W_2(0)
=-2\int_0^t r(s)\delta_2(s)h_1(s)^\top/n\,ds.
\]

The integrand directions move. Rank one of each instantaneous update does
not give a width-independent finite-rank bound on the integral, or justify dropping the
indirect terms in (2) and (3).

## 2. Exact finite instantaneous realization, including singular sources

Write W for an unspecified n-by-n matrix. Retain k forward sources and l
reverse sources, and proposed images, as column matrices

\[
Q=(q_1,\ldots,q_k),\quad U=(u_1,\ldots,u_k),\qquad
P=(p_1,\ldots,p_l),\quad V=(v_1,\ldots,v_l).
\]

The question is whether one W can satisfy

\[
WQ=U,\qquad W^\top P=V.
\tag{6}
\]

There is such a matrix if and only if

\[
\ker Q\subseteq\ker U,\qquad
\ker P\subseteq\ker V,\qquad
P^\top U=V^\top Q.
\tag{7}
\]

The kernel conditions mean that every exact linear relation among retained
sources must also hold among their proposed images. They include zero and
repeated sources and make no nonsingularity assumption. The last condition
is the shared forward/reverse pairing identity

\[
\langle p_b,u_a\rangle_n=\langle v_b,q_a\rangle_n
\quad\text{for all }a,b.
\tag{8}
\]

**Necessity.** If Qc=0, then Uc=WQc=0; the reverse statement is identical.
Also P^T U=P^T WQ=(W^T P)^T Q=V^T Q.

**Sufficiency.** Let Q^dagger and P^dagger denote the Moore-Penrose
pseudoinverses. The matrices

\[
E_Q=QQ^\dagger,\qquad E_P=PP^\dagger
\]

are orthogonal projections onto the column spaces of Q and P. The kernel
conditions imply

\[
UQ^\dagger Q=U,\qquad VP^\dagger P=V.
\tag{9}
\]

Define

\[
W_*=UQ^\dagger+(P^\dagger)^\top V^\top(I-E_Q).
\tag{10}
\]

Since (I-E_Q)Q=0, equation (9) gives W_*Q=U. The mixed condition in (7)
gives P^T UQ^dagger=V^T E_Q. In addition,

\[
P^\top(P^\dagger)^\top V^\top
=(P^\dagger P)^\top V^\top=V^\top
\]

by (9). Therefore

\[
P^\top W_*
=V^\top E_Q+V^\top(I-E_Q)=V^\top,
\]

which proves (6).

All solutions are exactly

\[
W=W_*+(I-E_P)Z(I-E_Q),\qquad Z\in\mathbb R^{n\times n}.
\tag{11}
\]

Indeed, the displayed extra term annihilates Q and has transpose
annihilating P. Conversely, if a difference M between two solutions
satisfies MQ=0 and M^T P=0, then ME_Q=0 and E_P M=0, so
M=(I-E_P)M(I-E_Q). The free block in (11) is precisely the information
not tested by the retained actions. Formula (10) is an existence witness,
not an assertion that the actual W equals this witness.

## 3. Exact consistency of proposed first derivatives

Suppose Q,U,P,V and their proposed first derivatives are given at a single
instant. Prescribe the actual middle-matrix derivative

\[
D=-2r\delta_2h_1^\top/n.
\]

The product rule requires

\[
WQ=U,\quad W^\top P=V,\quad
W\dot Q=\dot U-DQ,\quad
W^\top\dot P=\dot V-D^\top P.
\tag{12}
\]

Define A=dot U-DQ and B=dot V-D^T P. Conditions (12) are feasible if
and only if criterion (7) holds for the augmented lists

\[
\widetilde Q=(Q,\dot Q),\quad\widetilde U=(U,A),\qquad
\widetilde P=(P,\dot P),\quad\widetilde V=(V,B).
\tag{13}
\]

This follows by applying the complete proof above to the augmented
matrices. Thus (13) handles all linear dependencies, including dependencies
between sources and their derivatives. It is an exact necessary and
sufficient test for instantaneous values and first derivatives to have
some realizing matrix W with the prescribed derivative D.

The augmented mixed-pairing condition consists of four blocks:

\[
\begin{aligned}
P^\top U&=V^\top Q,&
P^\top A&=V^\top\dot Q,\\
\dot P^\top U&=B^\top Q,&
\dot P^\top A&=B^\top\dot Q.
\end{aligned}
\tag{14}
\]

For one source pair, the middle two blocks read

\[
\langle p,\dot u\rangle_n-\langle v,\dot q\rangle_n
=-2r\langle p,\delta_2\rangle_n\langle h_1,q\rangle_n,
\tag{15}
\]

\[
\langle\dot p,u\rangle_n-\langle\dot v,q\rangle_n
=2r\langle p,\delta_2\rangle_n\langle h_1,q\rangle_n.
\tag{16}
\]

Adding them differentiates (8); demanding only that sum loses the two
individual transport constraints. The final block in (14) supplies an
additional pairing of the derivative sources, and the augmented kernel
conditions supply further constraints when those sources are dependent.

For q=h_1, u=z_2, p=delta_2, and v=b_1, (15)--(16) specialize to

\[
\langle\delta_2,\dot z_2\rangle_n
-\langle b_1,\dot h_1\rangle_n
=-2r\|\delta_2\|_n^2\|h_1\|_n^2,
\tag{17}
\]

\[
\langle\dot\delta_2,z_2\rangle_n
-\langle\dot b_1,h_1\rangle_n
=2r\|\delta_2\|_n^2\|h_1\|_n^2.
\tag{18}
\]

These checks are available to laws whose retained state includes population
aggregates: each scalar product is an aggregate, but its value must obey
the common-operator identities.

## 4. Population formulation using finite Gram matrices

Let H_1=L^2(mu_1) and H_2=L^2(mu_2) be real Hilbert spaces describing two
neuron populations. Assume all listed variables are square integrable,
with q_a,v_b in H_1 and p_b,u_a in H_2. The two population spaces need not
be identified or coupled with each other. Pairings below are taken only
within the indicated population.

Define the finite Gram matrices

\[
G_Q=(\mathbb E_1[q_aq_{a'}]),\quad
G_U=(\mathbb E_2[u_au_{a'}]),\quad
G_P=(\mathbb E_2[p_bp_{b'}]),\quad
G_V=(\mathbb E_1[v_bv_{b'}]).
\]

There exists a bounded linear operator T:H_1 to H_2 with

\[
Tq_a=u_a,\qquad T^*p_b=v_b
\tag{19}
\]

if and only if

\[
\ker G_Q\subseteq\ker G_U,\qquad
\ker G_P\subseteq\ker G_V,
\tag{20}
\]

and

\[
\mathbb E_2[p_bu_a]=\mathbb E_1[v_bq_a]
\quad\text{for all }a,b.
\tag{21}
\]

To prove this, view Q:R^k to H_1 as the synthesis map
Qc=sum_a c_a q_a, and define U,P,V in the same way. Then
c^T G_Q c=||Qc||^2, so ker G_Q=ker Q; the other identities are
identical. Each synthesis map has finite-dimensional range, hence its
pseudoinverse is bounded on its range and zero on the orthogonal
complement. The proof (9)--(10), with transpose replaced by Hilbert
adjoint, constructs a bounded operator

\[
T_*=UQ^\dagger+(P^\dagger)^*V^*(I-QQ^\dagger).
\]

It satisfies (19). Conversely, any bounded T satisfying (19) preserves
source relations and satisfies (21) by the adjoint identity. This proves
the population statement, including singular Gram matrices.

Equivalently, (20) requires every source combination with zero L^2 norm
to have an image combination with zero L^2 norm. For example,

\[
\mathbb E_1[(\textstyle\sum_a c_aq_a)^2]=0
\ \Longrightarrow\
\mathbb E_2[(\textstyle\sum_a c_au_a)^2]=0.
\]

If only proposed second moments are supplied, rather than actual random
variables, their within-population Gram matrices must also be positive
semidefinite. Writing C_ba for the common value in (21), these matrices are

\[
\begin{pmatrix}G_Q&C^\top\\ C&G_V\end{pmatrix}\succeq0,
\qquad
\begin{pmatrix}G_P&C\\ C^\top&G_U\end{pmatrix}\succeq0.
\tag{22}
\]

Conversely, (22) realizes the proposed moments as vectors in two finite
Euclidean spaces: factor each positive semidefinite matrix as B^T B and
take its columns as the required vectors. Under (20), the preceding
operator construction then applies. These are sufficient conditions for
an abstract vector-and-operator realization of the finite moments. They
do not enforce an otherwise specified neuron distribution or nonlinear
relations such as h=phi(z). For realization in prescribed finite
dimensions, the two Gram ranks must also fit those dimensions.

The same population test applies to the augmented lists in (13), provided
their derivatives are square integrable. It checks finitely many second
moments and mixed moments; it does not posit a finite-rank real network.

There is a necessary qualification when using this formulation for
width limits. Mixed identities and positive semidefiniteness pass to a
limit whenever all the relevant Gram entries converge. Source-relation
preservation in (20) need not do so without control of the matrices on
nearly dependent source directions. For example, take

\[
W_n=\sqrt n I_n,\qquad q_n=n^{-1/2}\mathbf1_n,
\qquad u_n=W_nq_n=\mathbf1_n.
\]

Then ||q_n||_n^2=1/n tends to zero, whereas ||u_n||_n^2=1. Thus the
limiting source Gram matrix has a kernel that its image Gram matrix does
not share, despite exact finite-width actions. A uniform operator bound
||W_n||_op<=M prevents this issue because

\[
G_{U,n}\preceq M^2G_{Q,n},\qquad
G_{V,n}\preceq M^2G_{P,n}.
\tag{23}
\]

Taking limits in (23) gives (20). A suitable continuity bound restricted
to the retained source spans also suffices. No such bound or particular
weight normalization is assumed in this note. Existence of an abstract
bounded T in (19) also does not identify T with a particular random-matrix
limit or its initialization law.

## 5. Quantitative defects as falsifiers

For a given actual matrix W, let proposed forward and reverse actions have
errors

\[
e_F=u-Wq,\qquad e_R=v-W^\top p.
\]

The adjoint identity gives the exact defect formula

\[
\langle p,u\rangle_n-\langle v,q\rangle_n
=\langle p,e_F\rangle_n-\langle e_R,q\rangle_n.
\]

Applying Cauchy--Schwarz to the two terms gives

\[
\left|\langle p,u\rangle_n-\langle v,q\rangle_n\right|
\leq\|p\|_n\|e_F\|_n+\|q\|_n\|e_R\|_n.
\tag{24}
\]

Thus a nonzero limiting mixed defect with bounded source norms rules out
vanishing L^2 errors for both proposed actions. This conclusion is an
obstruction to the particular proposed law and observables, not a
nonexistence theorem for every history-free state.

There is an analogous velocity certificate when the current q,p,u,v and
D are exact. Define proposed-velocity errors by

\[
e_{\dot u}=\widehat{\dot u}-\dot u,\qquad
e_{\dot q}=\widehat{\dot q}-\dot q.
\]

Subtracting the exact transport identity from the proposed one yields

\[
\begin{aligned}
R&=\langle p,\widehat{\dot u}\rangle_n
-\langle v,\widehat{\dot q}\rangle_n-\langle p,Dq\rangle_n\\
&=\langle p,e_{\dot u}\rangle_n
-\langle v,e_{\dot q}\rangle_n,
\end{aligned}
\]

and therefore

\[
|R|\leq\|p\|_n\|e_{\dot u}\|_n
+\|v\|_n\|e_{\dot q}\|_n.
\tag{25}
\]

The same bounds hold in the population Hilbert spaces. Computing any
candidate defect at initialization, for instance by Gaussian calculus
under separately specified assumptions, can certify an initial mismatch.
An initially vanishing defect alone gives no positive-time guarantee.

## 6. Why instantaneous tests do not certify a single matrix path

The realization theorem and its augmented version are existential at one
instant. Applying them at every time can select a different realizing
matrix at each time. This does not ensure that those matrices form a path
whose derivative is the prescribed D.

A two-dimensional example makes this distinction exact. Prescribe D=0
and take one forward source and image

\[
q(t)=\begin{pmatrix}\cos t\\\sin t\end{pmatrix},\qquad
u(t)=\begin{pmatrix}\cos 2t\\\sin 2t\end{pmatrix}.
\]

There are no reverse sources. The two columns q(t),dot q(t) form an
orthonormal basis. Hence, at every time, the augmented assignments
Wq=u and W dot q=dot u have the realizing matrix

\[
W_t=u(t)q(t)^\top+\dot u(t)\dot q(t)^\top.
\]

Thus the complete instantaneous first-derivative test passes for all t.
But a path with dot W=0 must have one constant matrix W. Such a matrix
would imply u''=Wq''=-Wq=-u, whereas the displayed u satisfies u''=-4u.
Since u is never zero, no such constant matrix exists on any open time
interval. This is an operator-consistency counterexample, not an asserted
trajectory of the canonical neural network.

The missing requirement is temporal consistency with the same underlying
operator, or an independent proof that the retained current state
determines its own derivative. The diagnostics above expose violations
of necessary shared-operator structure, including violations hidden by
separately plausible velocity or moment equations. They do not replace
that state-sufficiency requirement.
