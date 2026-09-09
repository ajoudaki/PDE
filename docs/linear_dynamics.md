# Three hidden linear layers: population dynamics and contraction closure

For one input, three hidden linear layers admit a global autonomous operator
population, a compact-time joint width/gradient-descent limit, and population
fitting. The same dynamics have no state-universal scalar or local PDE closure
in the uniform bounded-contraction class defined below. These assertions
concern different state spaces: one operator field can retain infinitely many
scalar coordinates.

The conventions in [NOTATION.md](NOTATION.md) apply. All source constructions
and proof estimates needed here are given in this chapter.

## 1. Model and population theorem

Fix hidden depth \(L=3\), one datum \(x=1\), a label \(y\in\mathbb R\),
and a mobility \(\kappa>0\). Every activation is the identity. The canonical
finite weights are

\[
W^{(1)},W^{(4)}\in\mathbb R^n,\qquad
W^{(2)},W^{(3)}\in\mathbb R^{n\times n},
\]

\[
z^{(1)}=W^{(1)},\qquad z^{(2)}=W^{(2)}z^{(1)},\qquad
z^{(3)}=W^{(3)}z^{(2)},\qquad
f_n=\frac{(W^{(4)})^Tz^{(3)}}n,\qquad
r_n=f_n-y,\qquad \mathcal L_n=r_n^2.
\tag{1.1}
\]

At initialization, the endpoint entries \(W^{(1)}_i,W^{(4)}_i\) are
\(N(0,1)\), and the two hidden-matrix entries are \(N(0,1/n)\), all mutually
independent. In particular, the **stored readout has variance one**. This is a
different initialization from the small-readout convention.

The four block mobilities for \(\mathcal L_n\) are
\(n\kappa,\kappa,\kappa,n\kappa\). Physical gradient flow is exactly

\[
\begin{aligned}
\dot W^{(1)}&=-2\kappa r_n(W^{(2)})^T(W^{(3)})^TW^{(4)},\\
\dot W^{(2)}&=-\frac{2\kappa r_n}{n}
 ((W^{(3)})^TW^{(4)})(W^{(1)})^T,\\
\dot W^{(3)}&=-\frac{2\kappa r_n}{n}
 W^{(4)}(W^{(2)}W^{(1)})^T,\\
\dot W^{(4)}&=-2\kappa r_nW^{(3)}W^{(2)}W^{(1)}.
\end{aligned}
\tag{1.2}
\]

Exact simultaneous GD replaces these derivatives by increments divided by
the physical step \(\eta_n>0\), using the old weights in every right-hand
side. Between steps the weights are linearly interpolated and all hidden
quantities, the prediction, and the residual are recomputed.

Introduce the normalized proof embeddings and middle-factor aliases

\[
u_n=W^{(1)}/\sqrt n,\qquad v_n=W^{(4)}/\sqrt n,\qquad
B_n=W^{(2)},\qquad R_n=W^{(3)}.
\tag{1.3}
\]

Thus \(f_n=v_n^TR_nB_nu_n\), and every entry of these four proof factors
initially has variance \(1/n\). Their norms are ordinary Euclidean or
operator norms; (1.3) does not change the stored-weight convention. Define
the unit-mobility kernel

\[
\begin{aligned}
K_n={}&\|R_nB_nu_n\|^2+
 \|v_n\|^2\|B_nu_n\|^2+
 \|R_n^Tv_n\|^2\|u_n\|^2+
 \|B_n^TR_n^Tv_n\|^2.
\end{aligned}
\tag{1.4}
\]

The common mobility \(\kappa\) is outside \(K_n\). For example its first
term is \(\|z^{(3)}\|_2^2/n\), and its second term is
\(\|W^{(4)}\|_2^2\|z^{(2)}\|_2^2/n^2\).

**Theorem 1 (global population and joint limit).** There are a fixed real
separable Hilbert space \(\mathscr H_\infty\), an explicit bounded source
\(\mathcal C_0\), and a unique global cyclic trace-class increment \(Q(t)\)
solving the autonomous equation

\[
\begin{gathered}
\mathcal C(t)=\mathcal C_0+Q(t),\qquad
f(t)=\tfrac14\operatorname{Tr}\mathcal C(t)^4,\qquad r(t)=f(t)-y,\\
\dot Q=-2\kappa r(t)(\mathcal C_0^*+Q^*)^3,\qquad Q(0)=0,\\
K(t)=\operatorname{Tr}[\mathcal C(t)^3(\mathcal C(t)^*)^3],\qquad
\mathcal L(t)=r(t)^2.
\end{gathered}
\tag{1.5}
\]

Here \(f(0)=0\), \(r(0)=-y\), and \(K(0)=4\). The solution is
restartable from every cyclic trace-class state in this affine source space.
It satisfies

\[
\dot r=-2\kappa rK,\qquad
\dot{\mathcal L}=-4\kappa\mathcal L K,\qquad
\|Q(t)\|_1\le2|y|\sqrt{\kappa t}.
\tag{1.6}
\]

For every fixed \(T<\infty\), finite gradient flow obeys

\[
\sup_{0\le t\le T}
\bigl(|f_n(t)-f(t)|+|K_n(t)-K(t)|+
 |\mathcal L_n(t)-\mathcal L(t)|\bigr)
\xrightarrow{\mathbb P}0.
\tag{1.7}
\]

The same conclusion holds for recomputed readouts of exact GD for **every**
deterministic sequence \(\eta_n\to0\), with no additional width/step
relation. Convergence also holds jointly, uniformly on \([0,T]\), for
every fixed finite family of the following scalar observables: Gram
pairings of typed words in the current middle factors and their adjoints
applied to the current endpoint vectors; contractions of finite-rank maps
formed from these vectors; and their ordinary finite-rank Schatten norms.
This statement identifies current operator actions through their rooted
geometry. It does not assert operator-norm convergence between different
ambient spaces or convergence of empirical neuron-coordinate laws.

If \(y\ne0\), then \(f(t)\to y\) and \(\mathcal L(t)\to0\), with an
exponential residual bound after any time at which \(f\ne0\). If \(y=0\),
the initialized population is stationary. All width approximations above
are on fixed compact time intervals; no growing-horizon or uniform-in-time
finite-width assertion is made.

The proof first packages the finite factors in one cyclic operator. A
colored word space supplies its limiting Gaussian source. A trace-norm
energy estimate gives global existence, finite-word Picard approximation
gives the width limit, and a dimension-independent Euler estimate gives
the exact-GD bridge.

## 2. Cyclic algebra and the Gaussian source

Temporarily omit \(n\) from the normalized factors. Define the feature
derivation \(\mathscr D\) by

\[
\mathscr Du=B^TR^Tv,\qquad
\mathscr DB=(R^Tv)u^T,\qquad
\mathscr DR=v(Bu)^T,\qquad
\mathscr Dv=RBu.
\tag{2.1}
\]

The physical derivation is \(-2\kappa r\mathscr D\). The feature
derivation is an algebraic vector field; using it does not presume a
globally increasing feature clock for every label. On
\(\mathscr H_n=\mathbb R\oplus(\mathbb R^n)^{\oplus3}\), set

\[
\mathcal C_n=
\begin{pmatrix}
0&0&0&v^T\\
u&0&0&0\\
0&B&0&0\\
0&0&R&0
\end{pmatrix}.
\tag{2.2}
\]

Multiplication of the four blocks gives

\[
\mathscr D\mathcal C_n=(\mathcal C_n^T)^3,\qquad
\operatorname{rank}\mathcal C_n^3\le4,\qquad
f_n=\tfrac14\operatorname{Tr}\mathcal C_n^4,
\tag{2.3}
\]

\[
\mathscr D f_n=K_n=\|(\mathcal C_n^T)^3\|_{\mathrm{HS}}^2,
\qquad
\dot f_n=-2\kappa r_nK_n,\qquad
\dot{\mathcal L}_n=-4\kappa r_n^2K_n.
\tag{2.4}
\]

Indeed, each of the four length-three paths crosses an endpoint block of
rank at most one. Each diagonal block of \(\mathcal C_n^4\) has trace
\(v^TRBu\); differentiating this scalar gives exactly the four squares
in (1.4). These arguments also apply to bounded operators between three
Hilbert spaces and a one-dimensional endpoint, with actual adjoints.

For the source construction, use the real full word Hilbert space

\[
\mathcal F=\mathbb R\Omega\oplus
 \bigoplus_{j\ge1}(\mathbb R^6)^{\otimes j}.
\tag{2.5}
\]

Its orthonormal basis consists of finite words in six letters, including
the empty word \(\Omega\). The left creation isometry \(\ell_i\) prepends
letter \(i\); its adjoint deletes that letter when present and is zero
otherwise. Define

\[
b_2=\ell_1+\ell_2^*,\qquad b_3=\ell_3+\ell_4^*,\qquad
\xi_u=\ell_5\Omega,\qquad \xi_v=\ell_6\Omega.
\tag{2.6}
\]

Every operator here has real matrix entries, and \(\|b_2\|,\|b_3\|\le2\).
Words in the first four letters cannot change or remove the final letter
of a word generated from \(\xi_u\) or \(\xi_v\). For every polynomial
\(P\) in \(b_2,b_3,b_2^*,b_3^*\), therefore,

\[
\langle\xi_u,P\xi_u\rangle=\langle\xi_v,P\xi_v\rangle
 =\langle\Omega,P\Omega\rangle,\qquad
\langle\xi_v,P\xi_u\rangle=0.
\tag{2.7}
\]

This is the colored Fock source, given explicitly without an additional
probabilistic representation theorem.

**Lemma 2 (Gaussian fixed words and rooted Gram matrices).** For the
independent Gaussian initialization in (1.3), every fixed finite family of
Gram entries

\[
\langle P_i(B_n,R_n)g_{\alpha,n},
 P_j(B_n,R_n)g_{\beta,n}\rangle,
\qquad g_{u,n}=u_n,\quad g_{v,n}=v_n,
\tag{2.8}
\]

where words may contain transposes, converges in probability to the
corresponding entry with \(B_n,R_n,g_{u,n},g_{v,n}\) replaced by
\(b_2,b_3,\xi_u,\xi_v\). Also there is a deterministic \(M_0<\infty\)
such that

\[
\mathbb P\{\|B_n\|+\|R_n\|+\|u_n\|+\|v_n\|\le M_0\}\longrightarrow1.
\tag{2.9}
\]

**Proof.** For a fixed trace word of even length \(2q\), expand all matrix
entries and apply the Gaussian pairing identity. That identity follows by
differentiating the Gaussian moment-generating function
\(\exp(t^T\Sigma t/2)\): odd moments vanish and each even moment is the sum
over pairings of the covariances. A nonzero pair has the same matrix color,
contributes \(1/n\), and identifies the row indices and the column indices
of its two entries, respecting transpose markers.

The trace is a closed walk with one side per matrix occurrence. After these
identifications, regard each paired side as one edge of a quotient
multigraph. The graph is connected, has \(q\) edges and some number \(v\)
of free index vertices, and the pairing contribution to the normalized
trace is \(n^{v-q-1}\). A connected graph with \(q\) edges has at most
\(q+1\) vertices: building a spanning tree needs \(v-1\) distinct edges.
Thus all contributions are bounded, and only \(v=q+1\) can survive.

Equality means the quotient graph is a tree. The original closed walk
traverses every edge twice. In a tree it must traverse that edge once in
each direction, since removing the edge separates the two components of
the walk. Hence its paired occurrences have opposite transpose orientation.
At a leaf the walk immediately returns across the same edge, giving an
adjacent removable pair. Removing the leaf and its pair reduces both \(v\)
and \(q\) by one; repetition proves that the pairing is noncrossing.
Conversely, repeatedly removing adjacent pairs of a noncrossing,
equal-colored, oppositely oriented pairing leaves one free index and
restores one new free index at each insertion. Thus precisely these
pairings attain \(v=q+1\). This also proves directly that every other
pairing loses at least one power of \(n\).

Expanding the operators in (2.6), a vacuum expectation is nonzero exactly
when creations and annihilations match in this nested order. For \(b_2\)
the annihilator is \(\ell_2^*\), and for \(b_2^*\) it is \(\ell_1^*\);
the analogous colors for \(b_3,b_3^*\) are four and three. Each successful
matching has value one. These are exactly the surviving trace pairings.
Odd words have both zero Gaussian mean and zero vacuum expectation.

The variance uses two trace walks. Pairings with no pair joining the two
walks cancel against the product of the means. For a joining pairing the
combined quotient graph is connected, has \(q\) paired edges in total,
and at most \(q+1\) free vertices. Its two trace normalizations give
\(n^{v-q-2}=O(n^{-1})\). At fixed word lengths there are finitely many
pairings, so this bound proves

\[
\frac1n\operatorname{Tr}P(B_n,R_n)
\xrightarrow{L^2}\langle\Omega,P(b_2,b_3)\Omega\rangle.
\tag{2.10}
\]

The needed operator-norm bound is elementary. A maximal \(1/4\)-separated
subset of the unit sphere is a \(1/4\)-net with at most \(9^n\) points,
by comparing disjoint radius-\(1/8\) balls inside the radius-\(9/8\) ball.
Approximating both unit vectors in a bilinear form gives
\(\|G\|\le2\max_{a,b\text{ in the net}}|a^TGb|\).
For a normalized Gaussian matrix each such form is \(N(0,1/n)\).
The exponential-moment bound for a Gaussian and a union bound imply

\[
\mathbb P\{\|G\|>12\}\le2\,81^ne^{-18n}\longrightarrow0.
\tag{2.11}
\]

For a normalized Gaussian vector, its squared norm has mean one and
variance \(2/n\). This proves (2.9).

Finally, conditional on a real matrix \(T\) independent of
\(g,h\sim N(0,I_n/n)\), the same pairing identity gives

\[
\begin{aligned}
\mathbb E[g^TTg\mid T]&=\operatorname{Tr}T/n,\\
\operatorname{Var}(g^TTg\mid T)&\le2\|T\|^2/n,\\
\mathbb E[|g^TTh|^2\mid T]&\le\|T\|^2/n.
\end{aligned}
\tag{2.12}
\]

For the second bound use the symmetric part of \(T\) and
\(\|T\|_{\mathrm{HS}}^2\le n\|T\|^2\). Take \(T=P_i^TP_j\).
Its norm is bounded when the two source matrix norms are bounded, since
its degree is fixed. Condition on the matrices, apply Chebyshev on that
matrix-measurable event, and use (2.11) for its complement. Together with
(2.10) this proves (2.8), including zero cross-root limits. A finite union
gives joint convergence. No word degree grows with \(n\). \(\square\)

Let \(\mathcal F_1,\mathcal F_2,\mathcal F_3\) be typed copies of
\(\mathcal F\), and put

\[
\mathscr H_\infty=\mathbb R\oplus\mathcal F_1\oplus\mathcal F_2
 \oplus\mathcal F_3,\qquad
\mathcal C_0=
\begin{pmatrix}
0&0&0&\langle\xi_v,\cdot\rangle\\
\xi_u&0&0&0\\
0&b_2&0&0\\
0&0&b_3&0
\end{pmatrix}.
\tag{2.13}
\]

Here the middle maps act between the indicated copies, and the endpoint
columns are maps from \(\mathbb R\). We have \(\|\mathcal C_0\|\le2\).
The rank argument in (2.3) and (2.7) give

\[
\operatorname{rank}\mathcal C_0^3\le4,\qquad
\tfrac14\operatorname{Tr}\mathcal C_0^4=0,\qquad
\|\mathcal C_0^{*3}\|_{\mathrm{HS}}^2=4.
\tag{2.14}
\]

For the last equality, the four squared block norms are
\(\|b_3b_2\xi_u\|^2\), \(\|\xi_v\|^2\|b_2\xi_u\|^2\),
\(\|b_3^*\xi_v\|^2\|\xi_u\|^2\), and
\(\|b_2^*b_3^*\xi_v\|^2\). Each vector displayed is a single word of
norm one, so each contribution is one.

## 3. Global flow and fitting

Write \(\mathfrak S_1\) for the trace-class operators on
\(\mathscr H_\infty\), with norm \(\|A\|_1\) equal to the sum of singular
values; \(\|A\|_{\mathrm{HS}}\) is the square root of the sum of their
squares. The cyclic state space \(\mathcal E\) is the closed real subspace
of \(\mathfrak S_1\) supported on the four block positions in (2.13).
In particular \(\mathcal C_0+Q\) has the same cyclic form for every
\(Q\in\mathcal E\). Its middle blocks are bounded operators with
trace-class trained increments; the fixed middle sources need not be
Hilbert--Schmidt.

We use the trace-ideal inequalities

\[
\|ATB\|_1\le\|A\|\|T\|_1\|B\|,\qquad
\|T\|_{\mathrm{HS}}\le\|T\|_1,\qquad
|\operatorname{Tr}T|\le\|T\|_1.
\tag{3.1}
\]

For example, expand \(T\) into its singular-value rank-one series and
sum the bounds for \(A u\otimes B^*v\); the remaining inequalities follow
from the corresponding inequalities for singular values. Finite-rank
approximation also gives \(\operatorname{Tr}(AT)=\operatorname{Tr}(TA)\)
for bounded \(A\) and trace-class \(T\). A rank-at-most-four operator
satisfies \(\|T\|_1\le2\|T\|_{\mathrm{HS}}\) by Cauchy--Schwarz.
These facts justify all traces below.

For \(Q\in\mathcal E\), set \(\mathcal C=\mathcal C_0+Q\) and use the
readouts (1.5). Both \(\mathcal C^3\) and \(\mathcal C^4\) have rank at
most four. The vector field

\[
V(Q)=-2\kappa\left[\tfrac14\operatorname{Tr}
 (\mathcal C_0+Q)^4-y\right](\mathcal C_0^*+Q^*)^3
\tag{3.2}
\]

maps \(\mathcal E\) into itself. The cubic has the required cyclic block
positions, and it is trace class either by its rank bound or by expanding
around the finite-rank operator \(\mathcal C_0^{*3}\).

For two states in the same affine source space with
\(\|\mathcal C\|,\|\widetilde{\mathcal C}\|\le A\), telescoping powers
and (3.1) give

\[
\begin{aligned}
\|\mathcal C^{*3}-\widetilde{\mathcal C}^{*3}\|_1
 &\le3A^2\|Q-\widetilde Q\|_1,\\
|f(Q)-f(\widetilde Q)|&\le A^3\|Q-\widetilde Q\|_1,\\
|K(Q)-K(\widetilde Q)|&\le12A^5\|Q-\widetilde Q\|_1.
\end{aligned}
\tag{3.3}
\]

The first inequality uses, without commutation,
\(A_1^3-A_2^3=A_1^2(A_1-A_2)+A_1(A_1-A_2)A_2+(A_1-A_2)A_2^2\).
For the last inequality use
\(|\|S\|_{\mathrm{HS}}^2-\|T\|_{\mathrm{HS}}^2|
\le(\|S\|_{\mathrm{HS}}+\|T\|_{\mathrm{HS}})\|S-T\|_{\mathrm{HS}}\)
and \(\|\mathcal C^{*3}\|_{\mathrm{HS}}\le2A^3\).
Also \(|f|\le A^4\), \(K\le4A^6\), and
\(\|\mathcal C^{*3}\|_1\le4A^3\). Thus \(V\) is bounded and Lipschitz
on each trace-norm ball, with bounds depending only on its radius,
\(\|\mathcal C_0\|,\kappa,y\), not the Hilbert-space dimension.

For clarity, local existence needs only the integral map
\(Q\mapsto Q_*+\int_0^tV(Q(s))\,ds\) on continuous paths in a small
closed ball. If the vector field bound is \(M\) and Lipschitz bound is
\(H\), choose time \(h\) with \(Mh\) below the ball radius and
\(Hh<1\). The map preserves the ball and is a contraction in the supremum
trace norm. Its successive iterates are Cauchy, yield a differentiable
solution, and the same contraction gives uniqueness and continuation.

Along this solution, differentiating the fourth-power trace gives

\[
\dot f=\operatorname{Tr}(\mathcal C^3\dot Q)
 =-2\kappa r\operatorname{Tr}[\mathcal C^3(\mathcal C^*)^3]
 =-2\kappa rK.
\tag{3.4}
\]

All differentiated terms contain the trace-class factor \(\dot Q\), so
cyclicity in (3.1) applies. Consequently \(\dot r=-2\kappa rK\), and
on every existence interval

\[
r(t)=r(0)\exp\!\left(-2\kappa\int_0^tK(s)\,ds\right),\qquad
\int_0^T r(t)^2K(t)\,dt\le\frac{r(0)^2}{4\kappa}.
\tag{3.5}
\]

Using the rank-four trace bound and Cauchy--Schwarz in time,

\[
\begin{aligned}
\|Q(T)-Q(0)\|_1
&\le4\kappa\int_0^T|r|\sqrt K\,dt\\
&\le4\kappa\sqrt T
 \left(\int_0^T r^2K\,dt\right)^{1/2}
\le2|r(0)|\sqrt{\kappa T}.
\end{aligned}
\tag{3.6}
\]

For the prescribed initialization \(r(0)=-y\), this is (1.6). A finite
maximal existence time would place the whole solution in a bounded
trace-norm ball. On that ball \(V\) is bounded, so the solution has a
trace-norm limit at that time; the local construction extends it. This
contradiction proves global existence. The same proof starts at any
\(Q_*\in\mathcal E\) with residual recomputed from that state, and gives
global forward existence and uniqueness there. Uniqueness gives the
autonomous restart identity. The argument also proves global finite-width
physical flow for every finite initial state, without a Gaussian premise.

To express the population weights, write the four current blocks as
\(W^{(1)}\in\mathcal F_1\), \(W^{(2)}:\mathcal F_1\to\mathcal F_2\),
\(W^{(3)}:\mathcal F_2\to\mathcal F_3\), and
\(W^{(4)}\in\mathcal F_3\). In the following calculation only, abbreviate
them by \(u,B,R,v\). These are Hilbert representatives of the normalized
finite geometry (1.3), not coordinate random variables for individual
neurons. Their equations are (2.1) multiplied by \(-2\kappa r\), with
adjoints and Hilbert rank-one maps \((a\otimes b)h=a\langle b,h\rangle\).
This also explains how one kernel \(Q\) stores the whole current population
state: choose a fixed orthonormal word basis of \(\mathscr H_\infty\), and
its matrix coefficients are a scalar kernel on a fixed countable set
times itself. Operator multiplication in (1.5) is the corresponding
convergent Hilbert-space summation; its definition does not require
pointwise absolute summability of arbitrary matrix products.

**Corollary 3 (fitting).** The fitting assertion of Theorem 1 holds using
only these cyclic factors.

**Proof.** In \(\mathcal F_2\), put

\[
z=Bu,\qquad p=R^*v,\qquad
A=BB^*+\|u\|^2I,\qquad M=R^*R+\|v\|^2I.
\tag{3.7}
\]

Here \(z,p\) are auxiliary Hilbert vectors. The product rule in (2.1)
gives \(\mathscr Dz=Ap\), \(\mathscr Dp=Mz\), and hence

\[
f=\langle z,p\rangle,\qquad
K=\langle p,Ap\rangle+\langle z,Mz\rangle.
\tag{3.8}
\]

Both endpoint squared norms start at one, and their physical derivatives
are \(-4\kappa rf\). By (3.5), \(r=-y\exp(-2\kappa\int_0^tK)\) and
\(f=y[1-\exp(-2\kappa\int_0^tK)]\), so \(rf\le0\). Their common
squared norm \(q(t)\) therefore satisfies \(q(t)\ge1\), and

\[
K\ge q(\|z\|^2+\|p\|^2)\ge2|\langle z,p\rangle|=2|f|.
\tag{3.9}
\]

The middle inequality is Cauchy--Schwarz followed by
\(2ab\le a^2+b^2\). If \(y\ne0\), (2.14) and (3.4) give
\(\dot f(0)=8\kappa y\), so choose \(t_1>0\) with \(|f(t_1)|>0\).
Formula (3.5) makes \(|f(t)|\) nondecreasing. Thus, for \(t\ge t_1\),

\[
|r(t)|\le |r(t_1)|
 \exp[-4\kappa|f(t_1)|(t-t_1)].
\tag{3.10}
\]

This proves fitting and loss decay. If \(y=0\), then \(V(0)=0\);
uniqueness makes \(Q=0\) the initialized solution. \(\square\)

## 4. Finite gradient flow and exact GD

Let \(\mathcal C_{0,n}\) be (2.2) at initialization and
\(Q_n(t)=\mathcal C_n(t)-\mathcal C_{0,n}\). Finite physical flow is
exactly (3.2) on the finite cyclic trace-class space, with transpose in
place of adjoint. Lemma 2 implies \(f_n(0)\to0\), \(K_n(0)\to4\), and
convergence of every fixed initial rooted Gram matrix.

Fix \(T<\infty\). With probability tending to one,
\(\|\mathcal C_{0,n}\|\le M_0\) and \(|f_n(0)|\le1\). On this event,
(3.6) bounds both finite and population flows on \([0,T+1]\) by

\[
\|Q_n(t)\|_1,\ \|Q(t)\|_1\le
R_T:=2(|y|+1)\sqrt{\kappa(T+1)}.
\tag{4.1}
\]

Choose a Lipschitz function \(\chi:[0,\infty)\to[0,1]\) equal to one
on \([0,R_T+1]\), decreasing linearly to zero on
\([R_T+1,R_T+2]\), and zero thereafter. In every dimension use the
**Q-space cutoff field**

\[
\widetilde V_n(Q)=\chi(\|Q\|_1)V_n(Q),
\qquad \widetilde V(Q)=\chi(\|Q\|_1)V(Q).
\tag{4.2}
\]

The radius is strictly larger than the energy bound. The estimates (3.3)
give a common global vector-field bound \(M_T\) and Lipschitz bound
\(H_T\) for (4.2), independent of dimension on the stated event. To check
global Lipschitz continuity across the support boundary, compare an inside
point with the first point of the connecting line on that boundary; the
cutoff vanishes there and its Lipschitz constant controls the remaining
factor. These cutoff flows equal the actual flows by (4.1).

We next justify convergence of the cutoff flows from finite words. Start
Picard iteration at \(Q^{[0]}=0\), and recursively integrate (4.2) at the
previous iterate. At each fixed iteration index \(j\), every iterate is
a finite sum

\[
Q_n^{[j]}(t)=\sum_{a,b=1}^{N_j}c_{ab,n}^{[j]}(t)
 |w_{a,n}\rangle\langle w_{b,n}|,
\tag{4.3}
\]

with a word list independent of \(n,t\). Include the unit vector in the
one-dimensional summand and the typed source words in
\(B_n(0),R_n(0)\) and their transposes applied to \(u_n(0),v_n(0)\).
At the first iteration, \((\mathcal C_{0,n}^{T})^3\) has exactly such four
rank-one blocks. At every subsequent iteration, a source map acting on a
rank-one factor appends a letter, and a product of two rank-one factors
contracts adjacent vectors to a Gram entry. The pure source cube is again
finite rank. A trace readout closes the last two vectors, while time
integration changes only the scalar coefficients. This proves (4.3)
inductively.

The cutoff norm also depends continuously on these finite Gram matrices.
Indeed, for \(A_*=\sum_{a,b}c_{ab}|u_a\rangle\langle v_b|\), let
\(G_u=(\langle u_a,u_b\rangle)\), \(G_v=(\langle v_a,v_b\rangle)\).
Writing the column maps as a partial isometry times their Gram square
root shows that the nonzero singular values of \(A_*\) are those of

\[
G_u^{1/2}(c_{ab})G_v^{1/2}.
\tag{4.4}
\]

The coefficient matrix in (4.4) acts between the supports of the two Gram
matrices; zero singular values account for their null spaces. Square roots
of finite positive semidefinite matrices are continuous: for a convergent
sequence \(G_h\to G\), the roots are bounded, and any subsequential limit
is positive semidefinite and squares to \(G\). The spectral decomposition
gives a unique such root, so the whole sequence converges. Likewise, from
any sequence of finite-matrix singular-value decompositions with bounded
matrices, compactness of the orthogonal factors and boundedness of the
ordered singular values give a convergent subsequence whose limit is a
decomposition of the limiting matrix. Uniqueness of its ordered singular
values proves their continuity, and that of every fixed Schatten norm.
Thus no inverse Gram matrix or nonsingularity assumption is needed.

At fixed \(j\), all coefficients in (4.3) and all its trace and rooted
readouts are consequently continuous functions of finitely many initial
Gram entries. The continuity is uniform in \(t\in[0,T+1]\): induction
uses continuous operations on bounded coefficient paths, and integration
has norm at most \(T+1\) in the supremum norm. Lemma 2 proves convergence
in probability of these paths and readouts at each fixed iteration index.
This is convergence of their numerical descriptions, not subtraction of
operators on different Hilbert spaces.

For completeness, the dimension-independent error of successive
approximation for a bounded \(H_T\)-Lipschitz field is

\[
\sup_{t\le T}\|Q(t)-Q^{[j]}(t)\|_1
\le M_TT e^{H_TT}\frac{(H_TT)^j}{(j+1)!}.
\tag{4.5}
\]

The first Picard increment has norm at most \(M_Tt\). Induction bounds
the \(h\)-th increment by \(M_TH_T^{h-1}t^h/h!\); summing the tail
gives (4.5), which holds in every dimension. Every Picard path is bounded
by \(M_TT\), so the readout Lipschitz constants in (3.3) apply on one
common larger ball. First choose \(j\) to make (4.5) small, then pass to
large \(n\) in (4.3), and finally let \(j\to\infty\). This proves
(1.7); on the common ball the loss readout is Lipschitz as the square of
a bounded residual.

For a fixed current rooted word, substituting \(\mathcal C_0+Q^{[j]}\)
expands it into finitely many source words and rank-one contractions.
Telescoping its factors bounds its change by a constant times
\(\|Q-Q^{[j]}\|_1\) on the common ball: endpoint block changes are
bounded in Hilbert norm and middle block changes in operator norm by this
trace norm. Pairings and finite-rank norms have the same continuity, using
(4.4) where needed. This proves the additional observable assertions of
Theorem 1 by exactly the preceding finite-iteration argument.

At mesh points, simultaneous exact GD for the canonical weights is,
after the linear embedding (1.3), precisely

\[
\begin{aligned}
Q_{n,k+1}&=Q_{n,k}-2\kappa\eta_n r_{n,k}
 (\mathcal C_{0,n}^T+Q_{n,k}^T)^3,\\
r_{n,k}&=\tfrac14\operatorname{Tr}(\mathcal C_{0,n}+Q_{n,k})^4-y.
\end{aligned}
\tag{4.6}
\]

This is Euler for \(Q\) alone. The residual is recomputed from the new
weights at each step; it is not advanced by an independent Euler equation
for \(\dot r=-2\kappa rK\). Indeed, the latter equation is a product-rule
identity for continuous flow, whereas a finite simultaneous parameter
step has additional cross terms in its prediction.

For a bounded \(H_T\)-Lipschitz vector field with bound \(M_T\), an exact
solution has one-step defect at most

\[
\left\|Q(t+h)-Q(t)-h\widetilde V_n(Q(t))\right\|_1
\le\tfrac12H_TM_Th^2.
\tag{4.7}
\]

This follows by integrating
\(\|\widetilde V_n(Q(t+s))-\widetilde V_n(Q(t))\|_1
\le H_TM_Ts\). The nodal error of Euler with the same initial state
satisfies
\(E_{k+1}\le(1+H_Th)E_k+\tfrac12H_TM_Th^2\). Summing the geometric
series yields

\[
\max_{kh\le T+1}E_k
\le\tfrac12M_T(e^{H_T(T+1)}-1)h.
\tag{4.8}
\]

The case \(H_T=0\) follows directly with zero nodal error. Linear
interpolation adds at most \(2M_Th\). For all sufficiently small \(h\)
these errors are less than the unit margin in (4.2), so the cutoff Euler
nodes and interpolants stay where \(\chi=1\). Induction in (4.6) then
identifies them with actual exact GD. The extra unit of horizon includes
the final interval intersecting \([0,T]\).

Take \(h=\eta_n\). On the event used in (4.1), all constants in (4.8)
are independent of \(n\); its complement has probability tending to zero.
Combining the \(O(\eta_n)\) comparison with (1.7) and the readout estimates
proves the claimed joint limit for any \(\eta_n\to0\). The linear
embedding of weights into \(Q\) commutes with parameter interpolation,
so the readouts compared are exactly those stipulated in the theorem.

## 5. The bounded-contraction closure class

The negative result concerns identities on an open set of **all current
states**, uniformly in width. It does not impose a Gaussian initialization.
Use the normalized finite factors \(\theta=(u,B,R,v)\) from (1.3), and
write \(\Theta_n\) for their full real vector space. The feature and
physical derivations are

\[
\mathscr D_n\text{ as in (2.1)},\qquad
\mathscr X_n=-2\kappa(f_n-y)\mathscr D_n.
\tag{5.1}
\]

A typed complete-contraction graph is a scalar tensor network made from
copies of \(u,B,R,v\), with each layer index paired and summed. Tensor
slots retain their layer types, and a transpose reverses how the slots
are displayed, not the identity of the underlying tensor. Graphs are
identified by type- and slot-preserving isomorphisms; there are no isolated
index vertices. Let \(P_G^{(n)}(\theta)\) be the contraction polynomial.
Its tensor degree is its number of tensor copies. The empty graph has
value one, and multiplication is disjoint union:

\[
P_G^{(n)}P_H^{(n)}=P_{G\sqcup H}^{(n)}.
\tag{5.2}
\]

For each fixed \(D\), there are finitely many such graphs of degree at
most \(D\): at most \(2D\) typed slots must be paired in finitely many
ways among a finite list of tensor types. Denote this finite set by
\(\mathcal G_D\).

Fix, independently of \(n\), a spatial domain
\(\mathcal O\subset\mathbb R^\nu\), a finite number \(q\) of real scalar
fields, differential order \(\sigma\), readout order \(\rho\), degree
bound \(D\), and finitely many readout points
\(\zeta_1,\ldots,\zeta_s\). A boundary is allowed if coefficients and
the required derivatives extend smoothly to it. A **uniform
bounded-contraction encoder** has the form

\[
U_{\alpha,n}(\zeta;\theta)
 =\sum_{G\in\mathcal G_D}c_{\alpha,G,n}(\zeta)P_G^{(n)}(\theta),
\qquad 1\le\alpha\le q,
\tag{5.3}
\]

where the coefficient functions are smooth and may depend on \(n\).
Thus the same finite graph alphabet controls the whole spatial profile,
including all mixed derivatives, not just its values at the readout points.
Written in canonical weights, a graph with \(a\) endpoint occurrences
acquires the factor \(n^{-a/2}\) from (1.3). Allowing width-dependent
coefficients makes (5.3) exactly equivalent under that normalization.

A local differential-polynomial closure for a derivation
\(\mathscr Y_n\in\{\mathscr D_n,\mathscr X_n\}\) consists of fixed
polynomials \(F_\alpha\) in their finite jet arguments, with smooth fixed
spatial coefficients, and a fixed polynomial \(G\), such that

\[
\mathscr Y_nU_{\alpha,n}(\zeta;\theta)
 =F_\alpha\!\left(\zeta,
 (\partial_\zeta^\beta U_{\gamma,n}(\zeta;\theta))_
 {1\le\gamma\le q,\ |\beta|\le\sigma}\right),
\tag{5.4}
\]

\[
f_n(\theta)=G\!\left(
 (\partial_\zeta^\beta U_{\alpha,n}(\zeta_j;\theta))_
 {\alpha,j,\ |\beta|\le\rho}\right).
\tag{5.5}
\]

The expressions \(F_\alpha,G\) are independent of width and state. The
identities are required, for every sufficiently large \(n\), on a
nonempty open set in \(\Theta_n\) and at every required spatial point.
For physical flow the fixed expressions may depend on the fixed label
and mobility.

In the analytic variant, the differential expressions and readout are
smooth in the spatial variables and real analytic in their finite jet
arguments on open domains containing their realized zero-network jet
tuples. The identities hold on a full state neighborhood of
\(\theta=0\), with all compositions remaining in those domains. This
condition includes the actual basepoints
\((\partial^\beta U_{\alpha,n}(\zeta;0))\), which need not be zero
because of the empty-graph term. Smoothness here includes the mixed
derivatives used in finite prolongations.

**Theorem 4 (restricted scalar and PDE nonclosure).** No encoder and
closure satisfying (5.3)--(5.5) exists for \(\mathscr D_n\), either in
the polynomial open-state class or in the analytic zero-neighborhood
class just specified. The same assertions hold for \(\mathscr X_n\),
for every fixed \(y\in\mathbb R\) and \(\kappa>0\), including \(y=0\).

In particular there is no fixed finite scalar list of bounded-degree
contractions with a polynomial autonomous ODE and polynomial output
readout in this state-universal sense. This is the case with no spatial
variables and zero differential/readout orders. It includes the usual
requirement that the first scalar coordinate itself be \(f_n\); the
analytic statement uses the same zero-neighborhood condition.

The theorem allows arbitrary width-dependent encoder coefficients but
requires a width-uniform degree bound. It concerns local finite-order
differential expressions and finite-jet readouts. It asserts neither
nonclosure for arbitrary encoders nor nonclosure along only the single
Gaussian-initialized trajectory.

## 6. Graph independence and the nonclosure proof

**Lemma 5 (stable independence).** Every fixed finite family of pairwise
nonisomorphic typed complete-contraction graphs has linearly independent
contraction polynomials for every sufficiently large width.

**Proof.** Treat all tensor entries as independent commuting
indeterminates. For this proof enlarge the graph class to typed incidence
networks in which an index vertex can have arbitrary valence. Take the
finite closure of the chosen graphs under all type-compatible quotients
of index vertices. For any network \(H\) in that closure, let
\(I_H^{(n)}\) be its injective contraction, in which distinct index
vertices of the same layer receive distinct indices. Partitioning all
index assignments by their equality relation gives

\[
P_G^{(n)}=\sum_\pi I_{G/\pi}^{(n)}.
\tag{6.1}
\]

The quotient may have index valence greater than two; this is precisely
why the auxiliary incidence networks are needed in (6.1).

For width at least the number of vertices of each type in every network
under consideration, an injective labeling of one network produces a
tensor-entry monomial recording every tensor type and its incident typed
indices. It can occur in another injective contraction only when the
networks are isomorphic. Commutativity of entries forgets only the order
of identical tensor occurrences, already allowed by graph isomorphism.
There are no invisible isolated indices. Hence the injective contractions
of pairwise nonisomorphic auxiliary networks are linearly independent.

Suppose \(\sum_Ga_GP_G^{(n)}=0\). Among graphs with \(a_G\ne0\), choose
one with a maximal number of index vertices. Its discrete partition in
(6.1) contributes \(I_G\); a nontrivial quotient has fewer vertices, and
no graph with nonzero coefficient has more vertices. No other graph of
the same maximal size contributes this injective type. Its coefficient
cannot cancel, contradicting the preceding independence. Descending in
vertex count proves every \(a_G=0\). \(\square\)

This is a stable-width statement. At any one fixed width, sufficiently
large contraction families can satisfy dimension-specific identities.

To produce contractions of unbounded connected complexity, set

\[
A=RB,\qquad H=A^TA=B^TR^TRB.
\tag{6.2}
\]

Retain only endpoint differentiation in the feature derivation:
\(\mathscr D_{0,n}v=Au\), \(\mathscr D_{0,n}u=A^Tv\), and
\(\mathscr D_{0,n}A=0\). For \(j\ge0\), put

\[
U_j=v^TAH^ju,\qquad X_j=u^TH^{j+1}u,\qquad
Y_j=v^T(AA^T)^{j+1}v.
\tag{6.3}
\]

These \(U_j\) are scalar auxiliary contractions, distinct from the
encoded fields with indices \(\alpha,n\). The identities
\(AH^jA^T=(AA^T)^{j+1}\) and
\((AA^T)^{j+1}A=AH^{j+1}\) give, by differentiating the two endpoints,

\[
\mathscr D_{0,n}U_j=X_j+Y_j,\qquad
\mathscr D_{0,n}X_j=\mathscr D_{0,n}Y_j=2U_{j+1}.
\tag{6.4}
\]

Since \(U_0=f_n\), induction yields, for every integer \(j\ge1\),

\[
\mathscr D_{0,n}^{2j-1}f_n
 =4^{j-1}\bigl[u^TH^ju+v^T(AA^T)^jv\bigr].
\tag{6.5}
\]

Every tensor replacement in the full feature field (2.1) is a sum of
monomials with coefficient \(+1\). The product rule therefore gives
nonnegative coefficients for every contraction graph in every full
derivative of \(f_n\). The endpoint-only differentiation histories in
(6.5) are among those histories. Consequently

\[
\mathscr D_n^{2j-1}f_n\quad\text{has coefficient at least }4^{j-1}
\text{ on }\quad
\Gamma_j=u^T(B^TR^TRB)^ju.
\tag{6.6}
\]

Here \(\Gamma_j\) also denotes its graph. It is a connected path of
tensor degree \(4j+2\). These graph types are pairwise nonisomorphic.

Let \(\mathcal S\) be the finite set of connected graph types occurring
in \(\mathcal G_D\), and let

\[
\mathcal A_{\mathcal S}^{(n)}
 =\operatorname{span}\{P_H^{(n)}:
 \text{every connected component of }H\text{ lies in }\mathcal S\}.
\tag{6.7}
\]

This is a unital algebra by (5.2). Every spatial derivative of (5.3), of
arbitrarily high order, remains a linear combination of the same graphs,
since it differentiates only the coefficient functions. Thus every field
jet belongs to \(\mathcal A_{\mathcal S}^{(n)}\).

We make explicit why a finite-order PDE forces all output time
derivatives into that same algebra. Introduce formal jet variables
\(u_{\alpha,\beta}\), where \(\beta\) is a spatial multi-index, and total
spatial derivatives

\[
D_i^{\mathrm{tot}}=\frac{\partial}{\partial\zeta_i}
 +\sum_{\alpha,\beta}u_{\alpha,\beta+e_i}
   \frac{\partial}{\partial u_{\alpha,\beta}},\qquad
D_{\mathrm{tot}}^\beta=\prod_i(D_i^{\mathrm{tot}})^{\beta_i}.
\tag{6.8}
\]

Here \(e_i\) is the spatial multi-index unit vector. Each expression
involves finitely many jets, so only finitely many summands act on it.
Use independent jet copies at the finitely many readout points and define
the evolutionary derivative of a differential expression \(J\) by

\[
\mathbf T_FJ=\sum_{j,\alpha,\beta}
 \frac{\partial J}{\partial u_{\alpha,\beta}^{(j)}}
 (D_{\mathrm{tot}}^\beta F_\alpha)(\zeta_j,u^{(j)}).
\tag{6.9}
\]

The state derivation and spatial derivatives commute because they act on
different variables. The chain rule and (5.4) consequently imply

\[
\mathscr Y_nJ(j^\infty U_n)
 =(\mathbf T_FJ)(j^\infty U_n),\qquad
\mathscr Y_n^kf_n=(\mathbf T_F^kG)(j^\infty U_n).
\tag{6.10}
\]

The symbol \(j^\infty U_n\) means substitution of the entire spatial jet;
each finite expression uses only finitely many of its entries.
For fixed \(k\) only jets through order at most \(\rho+k\sigma\) occur.
In the polynomial case the last expression is a finite polynomial in
those jets and belongs to \(\mathcal A_{\mathcal S}^{(n)}\).

First take \(\mathscr Y_n=\mathscr D_n\). Choose \(j\) with
\(4j+2>D\), so \(\Gamma_j\notin\mathcal S\). Equation (6.10) would
express \(\mathscr D_n^{2j-1}f_n\) using graphs whose components all lie
in \(\mathcal S\), while (6.6) gives a positive coefficient of the
connected graph \(\Gamma_j\). At this fixed iteration order only
finitely many graph types occur, uniformly in \(n\), regardless of the
encoder coefficient values. Lemma 5 makes coefficient comparison valid
for sufficiently large \(n\), a contradiction. If the starting identities
hold only on a nonempty open state set, each substituted identity is a
polynomial in the tensor entries. Such a polynomial vanishing on an open
set vanishes identically: restrict to coordinate lines through a small
open box and successively apply the fact that a one-variable polynomial
with an interval of zeros is zero. Thus the same argument applies.

For the analytic case, scale all four factors by a common scalar
\(\lambda\) and recenter each field jet at its actual zero-state value:

\[
\partial^\beta U_{\alpha,n}(\zeta;\lambda\theta)
 -\partial^\beta U_{\alpha,n}(\zeta;0).
\tag{6.11}
\]

Every nonzero centered jet has positive \(\lambda\)-order. At any fixed
power \(\lambda^N\), only finitely many monomials in the Taylor
expansion of a composed finite-jet expression can contribute. Each such
coefficient is a product of graph coefficients from (5.3), and so has
components only in \(\mathcal S\). The smooth mixed derivatives stipulated
above justify finite spatial prolongations and extraction of these Taylor
coefficients. All expansions are at realized zero-state tuples within
the specified analytic domains.

The cubic feature vector field raises homogeneous tensor degree by two.
Thus \(\mathscr D_n^{2j-1}f_n\) is homogeneous of degree \(4j+2\).
Comparing that power of \(\lambda\) in (6.10) gives the same contradiction
with (6.6). This proves the feature-flow assertions, including scalar
closures as a special case.

For physical flow with \(y\ne0\), decompose

\[
\mathscr X_n=2\kappa y\mathscr D_n-2\kappa f_n\mathscr D_n.
\tag{6.12}
\]

The first summand raises tensor degree by two and the second by six.
Therefore the lowest-degree homogeneous component of
\(\mathscr X_n^kf_n\) is exactly

\[
(2\kappa y)^k\mathscr D_n^kf_n.
\tag{6.13}
\]

Choosing \(k=2j-1\) again gives a nonzero \(\Gamma_j\) coefficient in
that homogeneous component. Both the polynomial identity argument and
the analytic Taylor argument contradict (6.10) degree by degree.

For \(y=0\), define homogeneous polynomials \(P_k\) by

\[
\mathscr X_n^kf_n=(-2\kappa)^kP_k,\qquad
P_0=f_n,\qquad P_{k+1}=f_n\mathscr D_nP_k.
\tag{6.14}
\]

Every graph coefficient in \(P_k\) is nonnegative. Induction shows it
contains \(f_n^k\mathscr D_n^kf_n\) with positive coefficient: applying
\(f_n\mathscr D_n\) to that term produces
\(f_n^{k+1}\mathscr D_n^{k+1}f_n\), and every other contribution is
nonnegative. At \(k=2j-1\) this includes a graph with \(k\) components
equal to the output path and one component \(\Gamma_j\). No product of
graphs from \(\mathcal S\) can supply that last component. The polynomial
has homogeneous degree \(4+6k\), so coefficient comparison at that
degree works in both classes. Lemma 5 again gives a contradiction. This
completes Theorem 4 for every label. The stationary initialized
population at \(y=0\) is consistent with this result, which quantifies
over an open set of current states. \(\square\)

## 7. What unrestricted fields can encode

Field count alone cannot imply the preceding obstruction. An exact
one-field transport construction illustrates the missing encoder
restriction without invoking a width limit.

Let \(\Phi_n^s\) denote the local feature flow (2.1). Define the germ at
\(s=0\) of the output profile of a current state by

\[
E_n(\theta)(s)=f_n(\Phi_n^s\theta).
\tag{7.1}
\]

The flow property gives, wherever the times are defined,

\[
U_n(\tau,s)=E_n(\Phi_n^\tau\theta)(s)=f_n(\Phi_n^{\tau+s}\theta),\qquad
\partial_\tau U_n=\partial_sU_n,\qquad
U_n(\tau,0)=f_n(\Phi_n^\tau\theta).
\tag{7.2}
\]

There is a common local interval on a common operator-norm neighborhood,
independent of width. For \(\|\mathcal C(0)\|\le\varepsilon\),
\(\varepsilon>0\), on the \(2\varepsilon\)-ball the feature field
\((\mathcal C^T)^3\) is bounded by \(8\varepsilon^3\) and Lipschitz
with constant \(12\varepsilon^2\), by telescoping. On
\(|s|\le(24\varepsilon^2)^{-1}\), the Picard integral map has contraction
constant at most \(1/2\) and image norm at most
\(\varepsilon+\varepsilon/3<2\varepsilon\). Thus (7.1) is a
state-universal local output realization. Repeated chain rules give

\[
\partial_s^kE_n(\theta)(0)=\mathscr D_n^kf_n(\theta).
\tag{7.3}
\]

Its \((2j-1)\)-st jet contains \(\Gamma_j\). It cannot satisfy (5.3),
even though the PDE is linear, first order, and uses one scalar field
and one spatial variable. This is a local statement for feature flow;
feature-time completeness is not needed or asserted.

For physical flow the construction is global on a fixed spatial domain.
Let \(\Psi_n^t\) be the global finite-width flow for arbitrary initial
states, proved by (3.6). Define

\[
\widehat E_n(\theta)(s)=f_n(\Psi_n^s\theta),\quad s\ge0,\qquad
(S_tu)(s)=u(s+t).
\tag{7.4}
\]

On \(C([0,\infty))\) with the topology of uniform convergence on compact
intervals, \(S_t\) is a continuous forward semigroup. For a compact
interval in \(s\), uniform continuity on a slightly larger interval
proves continuity in \(t\), and
\(\sup_{s\le S}|S_tu-S_tv|\le\sup_{s\le S+t}|u-v|\) proves
continuity in the profile. Its output profiles satisfy

\[
\widehat E_n(\Psi_n^t\theta)=S_t\widehat E_n(\theta),\qquad
\partial_tU=\partial_sU,\qquad U(t,0)=f_n(\Psi_n^t\theta).
\tag{7.5}
\]

For \(C^1\) initial profiles this PDE has the unique classical solution
\(U(t,s)=U(0,t+s)\). Along the characteristic
\(\tau\mapsto(t-\tau,s+\tau)\), its derivative is
\(-U_t+U_s=0\), proving the formula and uniqueness; no inflow boundary
datum at \(s=0\) is required. Continuous profiles give the same unique
translation evolution in the semigroup sense. Hence (7.5) is an
autonomous, restartable, global forward output realization on a fixed
domain for every width and current state.

This encoder uses the whole future output trajectory to initialize its
profile. It is an exact counterexample to an unrestricted prohibition of
PDE output realizations, not a method for constructing the population
from its Gaussian source. The population (1.5) has that additional
constructive content, established by Sections 2--4.

Two finite checks further delimit elementary compression claims. At
width one, the normalized states

\[
(v,R,B,u)=(1,1,1,1),\qquad (2,1,1,\tfrac12)
\tag{7.6}
\]

have the same output and cyclic characteristic polynomial
\(\lambda^4-1\). Formula (1.4) gives kernels \(4\) and \(25/4\),
respectively. Thus the cyclic eigenvalues alone do not determine the
instantaneous feature derivative, or the physical derivative when
\(y\ne1\). At that same fixed width a polynomial
scalar closure does exist: with \(a=v^2,b=R^2,c=B^2,d_0=u^2\),

\[
\mathscr D_1a=\mathscr D_1b=\mathscr D_1c=\mathscr D_1d_0=2f_1,
\qquad
\mathscr D_1f_1=bcd_0+acd_0+abd_0+abc.
\tag{7.7}
\]

These follow by differentiating the four scalar factors. Multiplication
by \(-2\kappa(f_1-y)\) gives a physical scalar closure as well.
This confirms why Theorem 4 requires identities for all sufficiently
large widths. Neither this example nor the transport profile is a
bounded-contraction closure in that theorem's width-uniform class.
