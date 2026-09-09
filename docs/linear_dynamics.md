# Linear dynamics and exact-capture comparisons

Sections 1–7 show that, for one input, three hidden linear layers admit a global autonomous operator
population, a compact-time joint width/gradient-descent limit, and population
fitting. The same dynamics have no state-universal scalar or local PDE closure
in the uniform bounded-contraction class defined below. These assertions
concern different state spaces: one operator field can retain infinitely many
scalar coordinates.

Sections 8–12 supply three distinct one-input GF comparisons: nonlinear
shallow marked characteristics, a two-hidden-layer linear spectral system,
and an operator construction at every separately fixed linear depth. They
retain their order-one stored readout and exact observable scopes. The new
GF statements do not acquire a raw-GD or arbitrary-data extension from the
three-layer result. Lemma 2.A provides the operator-space foundations.

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

### 2.A. Compact operators and the complete trace-norm space

The following foundations apply to the separable real Hilbert spaces in this
chapter, including finite-dimensional spaces. They also apply to the complex
Hilbert spaces below by taking real and imaginary variations where needed.
For vectors in the output and input spaces, respectively, write
\((u\otimes v)x=u\langle v,x\rangle\). An operator is compact if the image
of its unit ball has compact closure. All operator norms below are ordinary
Hilbert operator norms.

**Lemma 2.A.** A compact operator \(T:H\to K\) has an expansion
\[
 T=\sum_{j\ge1}s_j u_j\otimes v_j,
 \qquad s_1\ge s_2\ge\cdots>0,
 \tag{2.A.1}
\]
with orthonormal vector lists and operator-norm convergence; the list can
terminate. Its singular values are these numbers, padded by zeros as needed.
They satisfy
\[
 s_j(T)=\inf_{\operatorname{rank}R<j}\|T-R\|,
 \qquad |s_j(T)-s_j(S)|\le\|T-S\|.                 \tag{2.A.2}
\]
The compact operators with \(\|T\|_1=\sum_j s_j(T)<\infty\) form a Banach
space. Finite-rank truncations converge in this norm, and
\[
 \|T\|\le\|T\|_1,\qquad
 \|ATB\|_1\le\|A\|\|T\|_1\|B\|,
 \qquad \|u\otimes v\|_1=\|u\|\|v\|.             \tag{2.A.3}
\]
For square trace-class operators the trace is independent of the orthonormal
basis, is linear, obeys \(|\operatorname{Tr}T|\le\|T\|_1\), and satisfies
\(\operatorname{Tr}(AT)=\operatorname{Tr}(TA)\) for bounded \(A\).
Also \(\|T\|_{\mathrm{HS}}=(\sum_j s_j(T)^2)^{1/2}\le\|T\|_1\).

**Proof of the singular expansion.** A bounded sequence in a separable
Hilbert space has a weakly convergent subsequence: choose a countable
orthonormal basis, successively select subsequences on which each coordinate
converges, and take the diagonal subsequence. The sum of squares of the
limiting coordinates is bounded by the common squared norm, by passing to
the limit in every finite partial sum. The resulting Hilbert vector is the
weak limit, because finite-coordinate tests converge and their orthogonal
tails have uniformly small pairings with any fixed test vector. This argument
also covers finite dimension.

If \(T\ne0\) is compact, choose unit vectors with image norms tending to
\(\|T\|\). Pass to a weakly convergent subsequence and then, by compactness,
to a subsequence whose images converge in norm. The image limit is \(Tv\):
testing against \(w\) gives \(\langle w,Tv_i\rangle=\langle T^*w,v_i\rangle\).
Consequently \(\|Tv\|=\|T\|\) and \(\|v\|=1\); a smaller norm would
contradict the definition of \(\|T\|\). Differentiating
\(\|T(v+th)/\|v+th\|\|^2\) at zero for \(h\perp v\) shows
\(T^*Tv=\|T\|^2v\). In the complex case also replace \(h\) by \(ih\).
Set \(s_1=\|T\|\), \(v_1=v\), and \(u_1=Tv_1/s_1\).

The restriction of \(T\) to \(v_1^\perp\) has image in \(u_1^\perp\),
since \(\langle u_1,Th\rangle=s_1\langle v_1,h\rangle\).
Repeat the construction on the successive orthogonal complements. The
restrictions remain compact, and their norms give a nonincreasing sequence
\(s_j\). If infinitely many \(s_j\) were bounded below by \(b>0\), the
images \(Tv_j=s_ju_j\) would be mutually at distance at least \(\sqrt2 b\),
contradicting compactness. Thus \(s_j\to0\). The remainder after \(N\)
terms has norm \(s_{N+1}\), by its construction as the next restriction,
which proves (2.A.1). If a restriction is zero, the series terminates there.

Truncation before term \(j\) proves the upper bound in (2.A.2). Conversely,
if \(\operatorname{rank}R<j\) and \(s_j>0\), some unit vector in
\(\operatorname{span}(v_1,\ldots,v_j)\) lies in \(\ker R\); on this span
\(\|Tx\|\ge s_j\|x\|\). This gives the lower bound. If \(s_j=0\)
the lower bound is automatic. Applying the infimum formula to \(T-R\)
and \(S-R\), then exchanging \(T,S\), proves its Lipschitz assertion.

**The norm and completeness.** For \(m\) not exceeding either Hilbert-space
dimension, the singular expansion gives
\[
 \sum_{j=1}^m s_j(T)
 =\sup_{(e_i),(f_i)}
       \left|\sum_{i=1}^m\langle f_i,Te_i\rangle\right|,   \tag{2.A.4}
\]
where both lists are orthonormal in their respective spaces. To check the
upper bound without a trace theorem, substitute (2.A.1). The coefficient
\(c_j\) of \(s_j\) then satisfies
\[
 |c_j|\le
 \left(\sum_i|\langle f_i,u_j\rangle|^2\right)^{1/2}
 \left(\sum_i|\langle v_j,e_i\rangle|^2\right)^{1/2}\le1,
 \qquad \sum_j|c_j|\le m.
\]
The last inequality is Cauchy--Schwarz in \(j\) followed by Bessel in each
list. A decreasing nonnegative sequence \(s_j\) therefore has
\(\sum_j s_j|c_j|\le\sum_{j\le m}s_j\): move any weight on indices
above \(m\) into unused capacity among the first \(m\) indices.
Equivalently, bound the tail by \(s_m\sum_{j>m}|c_j|\) and use
\(s_j\ge s_m\) for \(j\le m\). The series is absolutely convergent
because \(s_j\le\|T\|\) and \(\sum_j|c_j|\le m\).
Equality is attained by singular vectors, filling a terminated list with
orthonormal vectors in the orthogonal complements. This proves (2.A.4).

Its supremum expression gives the triangle inequality for partial singular
value sums and hence for \(\|\cdot\|_1\) on letting \(m\) increase to the
smaller dimension, or to infinity. Homogeneity and definiteness follow from
(2.A.1) and \(s_1=\|T\|\). Finite-rank operators are compact, and compact
operators are closed in operator norm: for every tolerance, a nearby compact
operator supplies a finite net for the image of the unit ball. The latter
image is consequently totally bounded; its closure is compact in the complete
Hilbert space (successively select subsequences in nets of radii tending to
zero to obtain a Cauchy subsequence).

Let \(T_n\) be trace-norm Cauchy. It is operator-norm Cauchy, so it converges
to a bounded operator \(T\): define \(Tx=\lim_nT_nx\) in the complete
output Hilbert space, and the uniform Cauchy bound gives operator-norm
convergence. The limit is compact by the preceding paragraph. Given
\(\varepsilon>0\), choose \(N\) with \(\|T_n-T_k\|_1\le\varepsilon\)
for \(n,k\ge N\). For each fixed \(m,n\), (2.A.2) lets \(k\to\infty\)
in the finite partial sum to give
\(\sum_{j\le m}s_j(T-T_n)\le\varepsilon\) whenever \(n\ge N\).
Letting \(m\) increase proves \(\|T-T_n\|_1\le\varepsilon\).
In particular \(T-T_N\) and then \(T\) are trace class. This proves
completeness. The tail in (2.A.1) has exactly the remaining singular values,
so its trace norm is \(\sum_{j>N}s_j\), proving finite-rank density.

**Ideals, trace and Hilbert--Schmidt norm.** A rank-one map has just one
nonzero singular value, \(\|u\|\|v\|\), by direct evaluation on
\(v/\|v\|\); zero vectors cause no exception. For a trace-class \(T\),
apply bounded \(A,B\) termwise to (2.A.1). The resulting rank-one norms
sum to at most \(\|A\|\|B\|\sum_j s_j\). Completeness makes this series
converge in trace norm, and its operator-norm limit is \(ATB\). This proves
the ideal inequality, including rectangular compatible spaces.

For square operators and any orthonormal basis \((e_k)\),
\[
 \sum_k|\langle e_k,Te_k\rangle|
 \le\sum_j s_j\sum_k
       |\langle e_k,u_j\rangle\langle v_j,e_k\rangle|
 \le\sum_j s_j.
\]
Cauchy--Schwarz and Parseval justify the last inequality. Absolute summation
permits exchange of \(k,j\), giving
\(\sum_k\langle e_k,Te_k\rangle=\sum_js_j\langle v_j,u_j\rangle\),
independent of the basis. Define this common sum to be \(\operatorname{Tr}T\).
The basis expression proves linearity; the displayed bound gives continuity.
The rank-one formula and the trace-norm convergent series give
\[
 \operatorname{Tr}(AT)
 =\sum_js_j\langle v_j,Au_j\rangle
 =\operatorname{Tr}(TA).
\]
Likewise Parseval and nonnegative summation give
\(\sum_k\|Te_k\|^2=\sum_js_j^2\); this is independent of the basis.
It identifies the Hilbert--Schmidt norm with the norm of the square-summable
column list, so its triangle and Cauchy--Schwarz inequalities are the Hilbert
ones. The inequality \((\sum_js_j^2)^{1/2}\le\sum_js_j\) completes (2.A.3)
and the stated Hilbert--Schmidt bound.

Two consequences used in the width comparisons also follow directly.
If \(V,W\) are finite column maps and \(D\) is a finite coefficient matrix,
the nonzero singular values of \(VDW^*\) are those of
\[
 (V^*V)^{1/2}D(W^*W)^{1/2}.                          \tag{2.A.5}
\]
Indeed the rule \((V^*V)^{1/2}x\mapsto Vx\) is well-defined and isometric
on its range, because both squared norms equal \(x^*V^*Vx\). Extend it
by zero on the orthogonal complement to obtain a partial isometry \(U_V\),
and do the same for \(W\). Then \(V=U_V(V^*V)^{1/2}\), and the middle
matrix in (2.A.5) maps between precisely these isometric support spaces.
Adding zero directions changes no nonzero singular value. No Gram inverse
is involved. In finite dimension positive square roots are continuous:
bounded roots have convergent subsequences; any subsequential limit is
positive and squares to the limiting matrix, whose positive square root is
unique by finite-dimensional diagonalization. This, (2.A.2), and finiteness
of the matrix dimension prove continuity of the trace norm in (2.A.5).

Finally, if \(R\) has rank at most \(m\), adding it to a rank-\(<j\)
approximation of \(T-R\) and using (2.A.2) gives
\(s_{j+m}(T)\le s_j(T-R)\). Thus
\[
 \sum_{j>m}s_j(T)\le\|T-R\|_1.                     \tag{2.A.6}
\]
This controls the full trace-norm tail, not only finitely many singular
values. All completeness and operator-ideal facts needed for the subsequent
integral contractions and continuation arguments have now been proved.

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

## 8. Comparison: the shallow characteristic population

This is a one-hidden-layer nonlinear comparison, not an extension of the
three-hidden-layer linear theorem to nonlinear activations. Take one datum
\(m=d=1,x_1=1,y_1=y\in\mathbb R\), a common mobility \(\kappa\ge0\),
and full squared loss \(\mathcal L_n=(f_n-y)^2\). Assume

\[
\phi\in C^2(\mathbb R),\qquad
\|\phi'\|_\infty+\|\phi''\|_\infty<\infty,\qquad
|\phi(z)|\le C(1+|z|).
\tag{EC8.1}
\]

There is no condition \(\mathbb E\phi(G)^2=1\). Write
\(a_i=W_i^{(2)},u_i=W_i^{(1)}\), with all initial coordinates independent
\(N(0,1)\). Thus the stored readout has variance one. The two mobilities
are \(n\kappa,n\kappa\), and the exact finite equations are

\[
\begin{gathered}
f_n=\frac1n\sum_i a_i\phi(u_i),\qquad r_n=f_n-y,\\
\dot a_i=-2\kappa r_n\phi(u_i),\qquad
\dot u_i=-2\kappa r_n a_i\phi'(u_i),\\
K_n=\frac1n\sum_i\{\phi(u_i)^2+a_i^2\phi'(u_i)^2\},\qquad
\dot r_n=-2\kappa r_nK_n.
\end{gathered}
\tag{EC8.2}
\]

On the fixed mark probability space \((\mathbb R^2,\gamma_2)\), let
\((a_0,u_0)\) be the two independent standard Gaussian coordinate maps.
The population fields \(A=W^{(2)}\), \(U=Z^{(1)}\) and the scalar residual
solve

\[
\begin{aligned}
\dot A&=-2\kappa r\phi(U),&\dot U&=-2\kappa r A\phi'(U),\\
K&=\mathbb E[\phi(U)^2+A^2\phi'(U)^2],&
\dot r&=-2\kappa rK,
\end{aligned}
\quad (A,U,r)(0)=(a_0,u_0,-y).
\tag{EC8.3}
\]

**Theorem EC8.** There is a unique global canonical marked solution of
(EC8.3). Its fields have every finite moment, uniformly on each compact
physical-time interval, and

\[
f=\mathbb E[A\phi(U)]=y+r,\qquad \mathcal L=r^2.
\tag{EC8.4}
\]

For every fixed \(T<\infty\),

\[
\sup_{0\le t\le T}
\bigl(|f_n-f|+|K_n-K|+|r_n-r|+|r_n^2-r^2|\bigr)
\xrightarrow{\mathbb P}0.
\tag{EC8.5}
\]

The two separate block energies in (EC8.2) also converge uniformly. Under
the nested coupling using one infinite iid mark sequence, these convergences
are almost sure. No empirical path-law convergence is needed or asserted.
The restart state is the full marked pair \((A,U)\) and \(r\), with
\(r=\mathbb E[A\phi(U)]-y\); the tuple \((f,K,r)\) is not specified
as a restart state. One admissible restart domain is marked pairs with
every finite moment and this consistency relation. This includes every
state reached from the canonical initialization.

**Proof.** First construct characteristics on both signs of feature time:

\[
\partial_s\widehat A_s=\phi(\widehat U_s),\qquad
\partial_s\widehat U_s=\widehat A_s\phi'(\widehat U_s),\qquad
(\widehat A_0,\widehat U_0)=(a_0,u_0).
\tag{EC8.6}
\]

The vector field is locally Lipschitz on \(\mathbb R^2\). The integral
equations and (EC8.1), followed by the elementary integral Grönwall bound,
give, for every finite \(S\),

\[
1+|\widehat A_s|+|\widehat U_s|
\le e^{C_\phi S}(1+|a_0|+|u_0|),\qquad |s|\le S.
\tag{EC8.7}
\]

Here the same estimate is applied to the reversed vector field for negative
times. It precludes finite-time escape in the finite-dimensional ODE and
therefore proves global characteristic existence and uniqueness. Local
existence itself follows from the integral-map contraction on a bounded
ball with time length smaller than the inverse of its Lipschitz constant.

Set

\[
F(s)=\mathbb E[\widehat A_s\phi(\widehat U_s)],\quad
H_s=\phi(\widehat U_s)^2+\widehat A_s^2\phi'(\widehat U_s)^2.
\tag{EC8.8}
\]

The integrands in (EC8.8) have a quadratic envelope in
\(J=1+|a_0|+|u_0|\), uniformly on \([-S,S]\). Differentiating along
(EC8.6) gives

\[
\partial_s[\widehat A_s\phi(\widehat U_s)]=H_s,\qquad
\partial_sH_s=4\widehat A_s\phi(\widehat U_s)
                 \phi'(\widehat U_s)^2
 +2\widehat A_s^3\phi'(\widehat U_s)^2\phi''(\widehat U_s).
\tag{EC8.9}
\]

The last expression is bounded by \(C_SJ^3\). Gaussian tails make all
powers of \(J\) integrable. Difference quotients may consequently be
integrated by the dominated convergence theorem, giving
\(F'(s)=\mathbb E H_s=:K(s)\ge0\), with continuous \(K\).
Independence and centering of \(a_0\) give \(F(0)=0\).

Solve the scalar physical clock

\[
\dot s=-2\kappa(F(s)-y),\qquad s(0)=0.
\tag{EC8.10}
\]

Along every local solution,
\(r(t)=F(s(t))-y\) obeys

\[
r(t)=-y\exp\left(-2\kappa\int_0^tK(s(v))\,dv\right),\qquad
|s(t)|\le2\kappa|y|t.
\tag{EC8.11}
\]

These identities follow by differentiating \(F(s)-y\) and solving its
scalar linear equation. They hold also when no root of \(F(s)=y\) exists.
The second bound prevents a finite-time escape of the clock. Setting
\((A,U)(t)=(\widehat A,\widehat U)_{s(t)}\) proves (EC8.3)--(EC8.4)
and all moment bounds. Conversely, for any classical marked solution in
this moment class, define \(s(t)=-2\kappa\int_0^t r(v)\,dv\).
For each mark, uniqueness of the nonautonomous equation with this scalar
coefficient identifies its fields with (EC8.6) evaluated at \(s(t)\).
Also differentiation under the expectation preserves (EC8.4). It must
therefore satisfy (EC8.10), proving uniqueness. This proof starts at any
of the stated consistent restart states: (EC8.7) then uses
\(1+|A_*|+|U_*|\), and the clock bound uses \(|r_*|\).

We give the uniform empirical step rather than assuming a continuous-time
law of large numbers. For any one of the integrands in (EC8.8), or either
summand of \(H_s\), there is an integrable random Lipschitz constant
\(C_SJ^3\) on \([-S,S]\). Indeed the derivatives of the two summands are
\(2\widehat A\phi(\widehat U)\phi'(\widehat U)^2\) and
\(2\widehat A\phi(\widehat U)\phi'(\widehat U)^2+
2\widehat A^3\phi'(\widehat U)^2\phi''(\widehat U)\).
All these variables have finite fourth moments. For centered iid \(X_i\)
with a finite fourth moment,

\[
\mathbb E\left|\frac1n\sum_{i=1}^n X_i\right|^4
=\frac{n\mathbb E X_1^4+3n(n-1)(\mathbb E X_1^2)^2}{n^4}
\le\frac{C}{n^2}.
\tag{EC8.12}
\]

Markov's inequality and the summability of \(n^{-2}\) imply almost-sure
convergence of the averages: the probability of an error exceeding
\(\varepsilon\) for some \(n\ge N\) is bounded by a tail of that
summable series. Apply this to a countable sequence of finite rational
nets and to the Lipschitz envelope. If \(g_s\) is one of our integrands,
a net of spacing at most \(\delta\) gives

\[
\sup_{|s|\le S}|\mathbb E_n g_s-\mathbb E g_s|
\le\max_{q\text{ in net}}|\mathbb E_n g_q-\mathbb E g_q|
 +\delta(\mathbb E_n C_SJ^3+\mathbb E C_SJ^3).
\tag{EC8.13}
\]

Here \(\mathbb E_n\) is the ordinary average over the first \(n\)
marks. First take \(n\to\infty\), then \(\delta\downarrow0\).
This proves almost-sure uniform convergence of \(F_n,K_n\) and both
block energies on every fixed compact feature interval.

At finite width the exact flow is the same set of characteristics at
the common clock \(s_n\), where
\(\dot s_n=-2\kappa(F_n(s_n)-y)\). Its true initial residual is
\(F_n(0)-y\). Since \(F_n'=K_n\ge0\), its residual equation gives
\(|s_n(t)|\le2\kappa|F_n(0)-y|t\) on every local interval;
this proves global finite flow as well. Eventually almost surely
\(|F_n(0)|\le1\). Both clocks then stay in
\([-S_T,S_T]\), with \(S_T=2\kappa(|y|+1)T+1\).
If \(M_T=\sup_{|s|\le S_T}|F'(s)|\) and
\(\epsilon_n=\sup_{|s|\le S_T}|F_n(s)-F(s)|\), subtracting the clock
integral equations gives

\[
\sup_{v\le t}|s_n(v)-s(v)|
\le2\kappa T\epsilon_n e^{2\kappa M_TT},\qquad t\le T.
\tag{EC8.14}
\]

The estimate follows by iteration of the inequality
\(E(t)\le2\kappa T\epsilon_n+2\kappa M_T\int_0^tE(v)dv\).
Uniform empirical convergence and uniform continuity of the deterministic
readouts now apply at these converging clocks. This proves (EC8.5) and
the block-energy assertion. Almost-sure convergence under this coupling
implies the stated intrinsic convergence in probability because each
coupled width has the prescribed law. If \(\kappa=0\), all clocks are
zero and the same empirical argument applies directly. \(\square\)

## Quantitative shallow continuous-flow comparison

This result uses exactly the one-hidden-layer model and characteristic
construction of linear-dynamics Section 8, specialized to label one.
The stored readout and effective first preactivation are independent
order-one standard Gaussians. There is one RMS-unit input, no hidden
connector, full square loss, and a common physical mobility multiplier
\(\kappa\ge0\). The activation satisfies
\(\phi\in C^2(\mathbb R)\) and
\(\|\phi'\|_\infty+\|\phi''\|_\infty<\infty\); it may grow linearly.
For iid marks \(\xi_i=(a_i^0,u_i^0)\sim N(0,I_2)\), the actual finite flow is
\[
 f_n=\frac1n\sum_i a_i\phi(u_i),\qquad
 \dot a_i=2\kappa(1-f_n)\phi(u_i),\qquad
 \dot u_i=2\kappa(1-f_n)a_i\phi'(u_i).
 \tag{SR.1}
\]
The effective raw metric is
\(n^{-1}(\|da\|_2^2+\|du\|_2^2)\).

**Theorem.** Let \(f\) be the deterministic characteristic-flow output
of Section 8. For every fixed \(T<\infty\), there is a finite constant
\(C_T\), depending only on the activation, mobility and horizon, such that
for every width \(n\ge1\),
\[
 E\sup_{t\le T}|f_n(t)-f(t)|^2\le C_T/n,
 \qquad E\sup_{t\le T}|f_n(t)-f(t)|^4\le C_T/n^2.
 \tag{SR.2}
\]
Consequently \(\sup_{t\le T}\operatorname{Var} f_n(t)\le C_T/n\), and
with \(\mathcal L_n=(1-f_n)^2\), \(\mathcal L=(1-f)^2\),
\[
 E\sup_{t\le T}|\mathcal L_n(t)-\mathcal L(t)|^2\le C_T/n.
 \tag{SR.3}
\]
If in addition \(\phi\) is bounded, let \(\bar X_i\) be the limiting
characteristic with the same initial mark \(\xi_i\), where
\(X_i^n=(a_i,u_i)\). Then
\[
 E\left[\frac1n\sum_i\sup_{t\le T}
       |X_i^n(t)-\bar X_i(t)|_{\mathbb R^2}^2\right]\le C_T/n.
 \tag{SR.4}
\]
The \(\bar X_i\) are independent because their common limiting clock is
deterministic. In particular each fixed finite set of actual particle paths
converges jointly to independent limiting paths under this coupling.
All assertions concern continuous gradient flow. No raw-GD rate, kernel
rate, growing-depth conclusion or population fitting claim is added.

*Proof.* Write \(c=2\kappa\),
\(H(a,u)=a\phi(u)\), and
\(V(a,u)=(\phi(u),a\phi'(u))\). Let \(\Psi_s\xi\) solve
\(\partial_s\Psi_s=V(\Psi_s)\). The global feature characteristics, the
physical clocks, and their exact identification with (SR.1) are proved in
Section 8. The estimates needed here can also be read directly from linear
growth of \(V\): on each fixed \([-S,S]\),
\[
 \sup_{|s|\le S}|\Psi_s\xi|\le C_S(1+|\xi|),\qquad
 Y_s(\xi)=H(\Psi_s\xi),\quad J_s(\xi)=|V(\Psi_s\xi)|^2,
\]
\[
 \partial_sY_s=J_s,\qquad
 \sup_{|s|\le S}(|Y_s|+|J_s|)\le C_S(1+|\xi|^2).
 \tag{SR.5}
\]
Thus all fixed moments of the envelope are finite. Put
\(F(s)=EY_s\), \(F_n(s)=n^{-1}\sum_iY_s(\xi_i)\).
Dominated differentiation gives \(F'=EJ_s\ge0\), \(F(0)=0\), and
\(F_n'=n^{-1}\sum_iJ_s(\xi_i)\ge0\).

Here is a quantitative continuum empirical bound. With \(P_n\) the
average over the marks and \(P\) their expectation, set
\(D_{n,S}=\sup_{|s|\le S}|F_n(s)-F(s)|\). The exact integral identity
in (SR.5) gives
\[
 D_{n,S}\le |(P_n-P)Y_0|
       +\int_{-S}^S|(P_n-P)J_v|\,dv.
 \tag{SR.6}
\]
For iid centered real \(Z_i\), direct expansion and independence give
\[
 E\left|\frac1n\sum_iZ_i\right|^2=EZ_1^2/n,\qquad
 E\left|\frac1n\sum_iZ_i\right|^4
 =\frac{nEZ_1^4+3n(n-1)(EZ_1^2)^2}{n^4}.
 \tag{SR.7}
\]
The same expansion at even order eight is at most \(C n^{-4}\) when
\(E|Z_1|^8<\infty\): terms with an index appearing once vanish, so each
surviving term has at most four distinct indices. There are at most
\(C n^4\) such terms, and Hölder bounds each by \(E|Z_1|^8\).
Applying (SR.7) to the centered \(Y_0,J_v\), then
\((\int_{-S}^S|g|)^p\le(2S)^{p-1}\int_{-S}^S|g|^p\), yields
\[
 ED_{n,S}^2\le C_S/n,\qquad ED_{n,S}^4\le C_S/n^2.
 \tag{SR.8}
\]
Take \(S>0\); the zero-length interval is covered by (SR.7).

The actual clocks satisfy
\[
 \dot s_n=c(1-F_n(s_n)),\quad \dot s=c(1-F(s)),\quad s_n(0)=s(0)=0.
\]
The residual equations and nonnegativity of \(F_n',F'\) give
\[
 |1-f_n(t)|\le |1-F_n(0)|,\quad 0\le f(t)\le1,\quad
 |s_n(t)|\le cT|1-F_n(0)|,\quad 0\le s(t)\le cT.
 \tag{SR.9}
\]
These also preclude finite physical-time escape. On
\(E_n=\{|F_n(0)|\le1\}\), both clocks lie in the deterministic interval
\([-S,S]\) with \(S=2cT+1\). Set
\(L_S=\sup_{|s|\le S}|F'(s)|<\infty\). Subtracting the clock integral
equations, using \(F\) for the Lipschitz term, and iterating gives
\[
 \sup_{t\le T}|s_n(t)-s(t)|\le cT e^{cL_ST}D_{n,S},\quad
 \sup_{t\le T}|f_n(t)-f(t)|\le(1+cTL_Se^{cL_ST})D_{n,S}.
 \tag{SR.10}
\]
The second inequality uses
\(F_n(s_n)-F(s)=[F_n(s_n)-F(s_n)]+[F(s_n)-F(s)]\).

The exceptional event is controlled by the actual loss flow, not by an
unbounded random clock. Write \(Z_n=F_n(0)\), a centered iid sample mean.
On \(E_n^c\), (SR.9) gives
\(\sup_{t\le T}|f_n-f|\le3+|Z_n|\le4|Z_n|\).
Thus its contributions to the second and fourth powers are bounded by
\(16E|Z_n|^4\) and \(256E|Z_n|^4\), respectively, both \(O(n^{-2})\).
Together with (SR.8)–(SR.10) this proves (SR.2), including \(\kappa=0\).
Variance is bounded by squared error from any deterministic number.
Finally, if \(\Delta=f_n-f\),
\(|\mathcal L_n-\mathcal L|\le2|\Delta|+|\Delta|^2\) by (SR.9).
Squaring and using (SR.2) proves (SR.3).

For (SR.4), assume \(\|\phi\|_\infty=M<\infty\) and write
\(B=\|\phi'\|_\infty\). Direct integration, for either sign of \(s\), gives
\[
 |A_s-a|\le M|s|,\qquad
 |U_s-u|\le B(|a||s|+Ms^2/2).
 \tag{SR.11}
\]
On \(E_n\), the speed on the fixed clock interval is at most
\(C_T(1+|a_i^0|)\). Equations (SR.10)–(SR.11) imply
\[
 \frac1n\sum_i\sup_{t\le T}|X_i^n-\bar X_i|^2\mathbf1_{E_n}
 \le C_T M_{2,n}D_{n,S}^2,
 \qquad M_{2,n}=\frac1n\sum_i(1+|a_i^0|^2).
\]
Jensen gives \(EM_{2,n}^2\le E(1+|a_1^0|^2)^2<\infty\).
Cauchy–Schwarz and (SR.8) bound this expectation by \(C_T/n\).
On the complement, apply (SR.11) at the two clocks and (SR.9) to get
\[
 \frac1n\sum_i\sup_{t\le T}|X_i^n-\bar X_i|^2\mathbf1_{E_n^c}
 \le C_T M_{2,n}(1+|Z_n|^4)\mathbf1_{|Z_n|>1}.
\]
Its expectation is at most
\(2C_T(EM_{2,n}^2)^{1/2}(E|Z_n|^8)^{1/2}=O(n^{-2})\), by the
order-eight expansion following (SR.7). This proves (SR.4).
Exchangeability makes each fixed particle's expected squared path error
bounded by the same average; a sum over finitely many particles proves
the last assertion. No independence between \(D_{n,S}\), \(Z_n\) and
an individual mark has been assumed. \(\square\)

## 9. A Gaussian source lemma with contained norm and Wick proofs

For the linear comparisons we need only fixed words in finitely many
independent Gaussian matrices, not a theorem about a growing adaptive
program. The following expands the proof of Lemma 2 in this chapter to an
arbitrary separately fixed finite number of matrix labels. No sharp spectral
edge estimate is needed.

Fix a nonnegative integer \(q\). Let \(B_{j,n}\), \(1\le j\le q\), have mutually
independent \(N(0,1/n)\) entries. Let \(g_{1,n},g_{2,n}\) be independent
\(N(0,I_n/n)\) vectors independent of these matrices. All norms here are
ordinary finite Euclidean or operator norms.
Empty maxima of nonnegative quantities and empty sums below mean zero.

Take the real full word Hilbert space

\[
\mathcal F_q=\mathbb R\Omega\oplus
 \bigoplus_{k\ge1}(\mathbb R^{2q})^{\otimes k}.
\tag{EC9.1}
\]

For \(q=0\) this means \(\mathbb R\Omega\). For \(q>0\), the left
creation operator \(\ell_{j,+}\) (respectively \(\ell_{j,-}\)) prepends
the indicated letter to a word. Its actual Hilbert adjoint deletes that
first letter when it matches and returns zero otherwise. Put

\[
c_j=\ell_{j,+}+\ell_{j,-}^*,\quad
\mathcal H=\mathcal F_q\oplus\mathcal F_q,\quad
\Gamma_j=c_j\oplus c_j,\quad
g_1=(\Omega,0),\quad g_2=(0,\Omega).
\tag{EC9.2}
\]

Creation is an isometry, so \(\|\Gamma_j\|\le2\); both roots have norm
one. For a word \(P\) with transpose letters, \(P(\Gamma)\) uses actual
adjoints at those letters. Set
\(\tau(P)=\langle\Omega,P(c)\Omega\rangle\).

**Lemma EC9.** Every fixed finite collection of rooted Gram entries obeys

\[
\langle P_n g_{i,n},Q_n g_{j,n}\rangle
\xrightarrow{\mathbb P}
\langle P(\Gamma)g_i,Q(\Gamma)g_j\rangle
=\mathbf1_{i=j}\tau(P^*Q).
\tag{EC9.3}
\]

The assertion also holds for typed compatible words between copies of
\(\mathcal H\). Moreover

\[
\mathbb P\{\max_j\|B_{j,n}\|\le12,
                 \|g_{1,n}\|\le2,\|g_{2,n}\|\le2\}\longrightarrow1.
\tag{EC9.4}
\]

**Proof.** A maximal \(1/4\)-separated subset \(\mathcal N\) of the
Euclidean unit sphere is a \(1/4\)-net. Disjoint balls of radius \(1/8\)
around its points fit in the radius-\(9/8\) ball, so
\(|\mathcal N|\le9^n\). Approximating each of the two unit vectors in
a bilinear form shows
\(\|B\|\le2\max_{a,b\in\mathcal N}|a^TBb|\).
Each form is \(N(0,1/n)\). For such a variable \(Z\),
\(\mathbb E e^{tZ}=e^{t^2/(2n)}\); minimizing
\(e^{-tu}\mathbb E e^{tZ}\) over \(t>0\) bounds its upper tail by
\(e^{-nu^2/2}\), and symmetry bounds both tails. Therefore

\[
\mathbb P\{\|B\|>12\}\le2\,81^ne^{-18n}.
\tag{EC9.5}
\]

For a normalized Gaussian vector its squared norm has mean one and
variance \(2/n\), so Chebyshev's inequality and a finite union prove
(EC9.4). This argument asserts boundedness in probability, not convergence
of the largest singular value to two.

For clarity we prove the word law as well. The Gaussian moment-generating
function is \(\exp(t^T\Sigma t/2)\). Differentiating at zero shows that
an even product of centered Gaussian coordinates has expectation equal
to the sum over pairings of covariance products; odd products have zero
mean. This is Wick's identity, including singular finite covariance.
Equivalently it follows by repeated Gaussian integration by parts, as in
Section 4 of `gaussian_calculus.md`.

Expand a normalized trace word of length \(2k\) into entries. Regard the
trace indices as vertices of a closed walk, with one side per matrix
occurrence. A nonzero Wick pair has the same matrix label, contributes
\(1/n\), and identifies the two raw row indices and the two raw column
indices. A transpose letter exchanges which endpoint of its side is the
raw row. After all identifications, the quotient multigraph is connected
and has \(k\) paired edges. If it has \(v\) free index vertices, its
contribution is exactly

\[
n^{v-k-1}.
\tag{EC9.6}
\]

A connected graph with \(k\) edges has at most \(k+1\) vertices, because
a spanning tree uses \(v-1\) edges. Equality holds exactly for a tree.
In that case the original walk uses every edge twice, once in each
direction: removing an edge separates the tree into two components and
a closed walk must enter and leave each component equally often. Since
the raw row and column of paired entries were identified in the same
order, this opposite traversal forces opposite transpose markers.
At a leaf the two occurrences are adjacent in the cyclic walk and can
be removed. Repeating this removal proves that the pairing is noncrossing.
Conversely any noncrossing pairing with matching labels and opposite
transpose markers can be reduced by adjacent-pair removal. Restoring
each removed pair introduces one free index; hence it has \(k+1\)
vertices. These and only these pairings survive as \(n\to\infty\).

Expanding each \(c_j\) and \(c_j^*\) in (EC9.2), an annihilator can
only remove the first currently present letter of its own color. A
vacuum contribution is therefore precisely a nested matching of
annihilators to creations. The two letters available for each label
permit a match exactly between opposite transpose markers of that label.
Every such matching contributes one. This identifies the surviving
pairings in (EC9.6) with \(\tau\) of the word. Odd words vanish on both
sides.

For the variance, use two copies of a trace walk. Pairings with no edge
joining the walks cancel against the product of expectations. Every
remaining quotient graph is connected. If there are \(k\) paired edges
in total, it has at most \(k+1\) vertices; the two trace normalizations
give \(n^{v-k-2}=O(n^{-1})\). There are finitely many pairings at fixed
length. Thus each normalized trace word converges in \(L^2\) to its
vacuum value. Linearity gives the same statement for any fixed polynomial.

Finally let \(T\) be a real matrix independent of the two normalized
Gaussian roots. Wick's identity gives

\[
\mathbb E[g^TTg\mid T]=\operatorname{Tr}T/n,\qquad
\operatorname{Var}(g^TTg\mid T)
=2\|\operatorname{sym}T\|_{\mathrm{HS}}^2/n^2
\le2\|T\|^2/n,
\tag{EC9.7}
\]
\[
\mathbb E[g^TTh\mid T]=0,\qquad
\mathbb E[|g^TTh|^2\mid T]
=\|T\|_{\mathrm{HS}}^2/n^2\le\|T\|^2/n
\quad(g,h\text{ independent}).
\tag{EC9.8}
\]

Use \(T=P_n^TQ_n\). On the matrix-measurable event
\(\max_j\|B_{j,n}\|\le12\),
its norm is bounded by a constant depending only on the fixed words.
Conditional Chebyshev, (EC9.5) for the complement, and the trace limit
give (EC9.3). A finite union gives joint convergence. The direct sum in
(EC9.2) makes the entire two rooted subspaces orthogonal; orthogonality
of just the two roots would not suffice. Typed words form a subset of
these word identities, so restricting to them proves the typed assertion.
\(\square\)

## 10. Every separately fixed hidden linear depth in physical time

Fix \(L\ge1\), one datum \(m=d=1,x_1=1,y_1=y\), and \(\kappa>0\).
Empty operator products for \(L=1\) are identities.
All activations are the identity and all blocks are trained. Initialize
\(W^{(1)},W^{(L+1)}\) with independent \(N(0,1)\) entries and every
\(W^{(\ell)}\), \(2\le\ell\le L\), with independent
\(N(0,1/n)\) entries, all blocks independent. Use full MSE \(r_n^2\)
with mobilities \(n\kappa,\kappa,\ldots,\kappa,n\kappa\).

For the proof embeddings only, write

\[
u_n=W^{(1)}/\sqrt n,\qquad a_n=W^{(L+1)}/\sqrt n,\qquad
B_{\ell,n}=W^{(\ell+1)}\quad(1\le\ell<L).
\tag{EC10.1}
\]

Let \(x_{1,n}=u_n\), \(x_{\ell+1,n}=B_{\ell,n}x_{\ell,n}\), and
\(b_{L,n}=a_n\), \(b_{\ell,n}=B_{\ell,n}^Tb_{\ell+1,n}\).
These are normalized finite vectors:
\(x_{\ell,n}=z^{(\ell)}/\sqrt n\) and
\(b_{\ell,n}=\delta^{(\ell)}/\sqrt n\).
All their norms and pairings below are ordinary Euclidean ones. Direct
differentiation of \(f_n=a_n^Tx_{L,n}\) gives

\[
\begin{aligned}
\dot a_n&=-2\kappa r_nx_{L,n},&
\dot u_n&=-2\kappa r_nb_{1,n},\\
\dot B_{\ell,n}&=-2\kappa r_n b_{\ell+1,n}x_{\ell,n}^T,
&r_n&=f_n-y.
\end{aligned}
\tag{EC10.2}
\]

For example, the matrix update in stored coordinates is
\(-2\kappa r_n\delta^{(\ell+1)}(z^{(\ell)})^T/n\).
The normalized outer product in (EC10.2) is its identical Euclidean
representative. The feature kernel is

\[
K_n=\|x_{L,n}\|^2+\|b_{1,n}\|^2+
\sum_{\ell=1}^{L-1}\|b_{\ell+1,n}\|^2\|x_{\ell,n}\|^2.
\tag{EC10.3}
\]

Use Lemma EC9 with \(q=L-1\), and let \(\mathcal H_\ell\) be typed
copies of its \(\mathcal H\). The initial endpoint vectors are
\(u_0=g_1\in\mathcal H_1\), \(a_0=g_2\in\mathcal H_L\);
\(\Gamma_\ell:\mathcal H_\ell\to\mathcal H_{\ell+1}\) is the
bounded source action of label \(\ell\). Denote a current operator by
\(B_\ell=\Gamma_\ell+P_\ell\), where
\(P_\ell\in\mathfrak S_1(\mathcal H_\ell,\mathcal H_{\ell+1})\)
is trace class. Write \(u=W^{(1)}\) and \(a=W^{(L+1)}\) for the
population endpoint Hilbert representatives and
\(W^{(\ell+1)}=B_\ell\) for the population operators. They represent
normalized rooted geometry, not a law of individual neuron coordinates.
Define \(x_1=u,x_{\ell+1}=B_\ell x_\ell\) and
\(b_L=a,b_\ell=B_\ell^*b_{\ell+1}\).

**Theorem EC10.** The autonomous system

\[
\begin{aligned}
\dot a&=-2\kappa r x_L,&\dot u&=-2\kappa r b_1,\\
\dot P_\ell&=-2\kappa r(b_{\ell+1}\otimes x_\ell),
&&1\le\ell<L,\\
K&=\|x_L\|^2+\|b_1\|^2+
 \sum_{\ell=1}^{L-1}\|b_{\ell+1}\|^2\|x_\ell\|^2,&
\dot r&=-2\kappa rK
\end{aligned}
\tag{EC10.4}
\]

with \((a,u,P_1,\ldots,P_{L-1},r)(0)=(a_0,u_0,0,\ldots,0,-y)\)
has a unique global solution in

\[
\mathcal X_L=\mathcal H_L\times\mathcal H_1\times
\prod_{\ell=1}^{L-1}\mathfrak S_1(\mathcal H_\ell,\mathcal H_{\ell+1})
\times\mathbb R.
\tag{EC10.5}
\]

Here \((v\otimes w)z=v\langle w,z\rangle\). The readouts satisfy
\(f=\langle a,x_L\rangle=y+r\), \(\mathcal L=r^2\),
\(f(0)=0\), \(K(0)=L+1\). For every fixed \(T<\infty\),

\[
\sup_{0\le t\le T}
\bigl(|f_n-f|+|K_n-K|+|r_n-r|+|r_n^2-r^2|\bigr)
\xrightarrow{\mathbb P}0.
\tag{EC10.6}
\]

This also holds jointly for any fixed finite collection of current typed
rooted-program scalar readouts. Such a program uses current endpoints,
current \(B_\ell,B_\ell^*\), finite sums, scalar multiplication, and
inner products, with a fixed finite number of operations. In particular,
all individual summands of \(K\) and finite Gram matrices of its fields
are included. Finite-rank maps made from a fixed field list have convergent
singular values and Schatten norms. For the current trained increments
\(P_{\ell,n}=B_{\ell,n}(t)-B_{\ell,n}(0)\), their trace norms and each
fixed singular value also converge uniformly in probability. For every
\(\varepsilon>0\), writing \(s_j(P)\) for the descending singular
values,

\[
\lim_{N\to\infty}\limsup_{n\to\infty}
\mathbb P\left\{\max_{\ell<L}\sup_{t\le T}
 \sum_{j>N}s_j(P_{\ell,n}(t))>\varepsilon\right\}=0.
\tag{EC10.7}
\]

The claim is about separately fixed depth and compact physical time.
It does not assert convergence of neuron-coordinate laws, subtraction
of operators on different width spaces, a scalar finite-dimensional
closure, or a constant uniform over depth. The full state (EC10.5) is
restartable on the consistency set \(r=\langle a,x_L\rangle-y\)
with the same immutable source.

**Proof: local equations and continuation.** Give (EC10.5) the norm
\(\|a\|+\|u\|+\sum_\ell\|P_\ell\|_1+|r|\). On a ball of radius
\(R\), with source norms at most \(M\), all current operator norms are
at most \(M+R\). Products telescope: the difference of two length-\(k\)
products is a sum of \(k\) terms with one differing factor. Since
\(\|P\|\le\|P\|_1\), this bounds every fixed forward/backward word
and its Lipschitz constant by a number depending only on \(L,M,R\).
For a rank-one map,

\[
\|v\otimes w\|_1=\|v\otimes w\|_{\mathrm{HS}}=\|v\|\|w\|,
\quad
\|v\otimes w-\widetilde v\otimes\widetilde w\|_1
\le\|v-\widetilde v\|\|w\|+
    \|\widetilde v\|\|w-\widetilde w\|.
\tag{EC10.8}
\]

The first identity follows by computing its sole possible nonzero
singular value; the second follows by subtracting one factor at a time.
Thus the vector field and \(K\) are bounded and Lipschitz on each state
ball, uniformly in dimension. The integral-map contraction used in
Section 8 gives local existence and uniqueness in this Banach space.

Differentiating \(f=\langle a,B_{L-1}\cdots B_1u\rangle\) inserts
one block velocity at a time. The two endpoint insertions yield the first
two squares in \(K\); the insertion at \(B_\ell\) gives
\(\|b_{\ell+1}\|^2\|x_\ell\|^2\). Consequently

\[
\dot f=-2\kappa rK=\dot r,\qquad
\frac d{dt}r^2=-4\kappa r^2K,\qquad
\int_0^T r^2K\,dt\le\frac{r(0)^2}{4\kappa}.
\tag{EC10.9}
\]

The source sectors in (EC9.2) give \(f(0)=0\), so consistency is
preserved. At time zero every forward product uses distinct creation
labels, and every backward product uses the opposite distinct labels;
the annihilation terms vanish at each such application. Each field in
(EC10.3) has norm one, giving \(K(0)=L+1\).

Each block's squared feature-velocity norm is a summand of \(K\).
For an operator block (EC10.8) equates that norm to its trace norm.
Cauchy--Schwarz in physical time therefore gives for each block
\(\theta\in\{a,u,P_1,\ldots,P_{L-1}\}\)

\[
\int_0^T\|\dot\theta(t)\|\,dt
\le2\kappa\sqrt T\left(\int_0^T r^2K\,dt\right)^{1/2}
\le |r(0)|\sqrt{\kappa T}.
\tag{EC10.10}
\]

The norm for an operator block in this display is the trace norm.
Also \(|r(t)|\le|r(0)|\), by its scalar equation. Hence the entire
state remains in a bounded ball on each finite interval. On such a ball
the vector field is bounded, so if a finite maximal time existed the
state would have a norm limit there; local existence from that limit
would extend it. This proves global existence. The identical argument
starts from every stated restart state and from every finite-dimensional
initial state. In finite dimensions consistency starts at
\(r_n(0)=f_n(0)-y\), not at \(-y\).

**Proof: transfer across varying width spaces.** Lemma EC9 supplies all
fixed initial rooted Grams and \(f_n(0)\to0\). On an event of probability
tending to one, source operators have norm at most 12, both roots have
norm at most 2, and \(|r_n(0)|\le|y|+1\). Equations (EC10.9)--(EC10.10)
then give one deterministic state radius \(R_T\) for every finite and
limiting trajectory on \([0,T]\); for example one may use

\[
R_T=4+(L+1)(|y|+1)\sqrt{\kappa T}+|y|+1.
\tag{EC10.11}
\]

Choose a scalar Lipschitz cutoff equal to one on \([0,R_T+1]\),
linear to zero on \([R_T+1,R_T+2]\), and zero above that interval.
Multiply the vector field by this cutoff evaluated at the state norm.
The resulting field is globally bounded and Lipschitz, with constants
\(M_T,H_T\) independent of dimension on the source event. Indeed, inside
the support this follows from the ball estimates; across its boundary,
the cutoff is bounded by its Lipschitz constant times the distance to
the boundary, while the original field is bounded there. Both outside
points have zero cutoff field. The true flows stay where the cutoff is
one, so their equations have not changed.

Start Picard iteration at the initial state in each of its own spaces:
\(S^{[0]}(t)=S_0\),
\(S^{[j+1]}(t)=S_0+\int_0^t\widetilde V(S^{[j]}(v))dv\).
For every fixed \(j\), each endpoint is a finite linear combination
of initial rooted words. Each \(P_\ell^{[j]}\) is a finite sum of
rank-one maps between such words, and the residual is a scalar continuous
function of finitely many initial Grams. To prove the induction, a source
action appends a letter, a product of rank-one maps contracts two factors
to a Gram entry, and the field formula uses only finitely many such
operations. Time integration changes coefficient functions, not the word
list.

The cutoff norm has the required same finite-Gram continuity. If
\(T=\sum_{i,j}c_{ij}v_i\otimes w_j\), let \(G_v,G_w\) be the Gram
matrices of those lists. The nonzero singular values of \(T\) are those of

\[
G_v^{1/2}(c_{ij})G_w^{1/2}.
\tag{EC10.12}
\]

This follows by factoring the column maps as a partial isometry times
their Gram square root, on the supports of the Gram matrices. Null spaces
only add zero singular values, so no inverse Gram is used. Square roots
are continuous even at singular positive semidefinite matrices: bounded
roots have subsequential limits, each limit is positive semidefinite and
squares to the limiting matrix, whose positive square root is unique.
For singular values, compactness of the orthogonal factors in finite
matrix singular-value decompositions proves the same continuity. Thus
the trace norms in the cutoff, endpoint norms, and the desired finite-rank
readouts all depend continuously on finitely many source Grams.

This induction is uniform in time on \([0,T]\). Continuous operations
on convergent bounded coefficient paths preserve uniform convergence,
and integration has norm at most \(T\) in the supremum norm. Equivalently,
restrict the finite Gram list to a compact neighborhood of its limiting
value, and induct on \(j\) using uniform continuity there. Lemma EC9
therefore proves uniform convergence in probability of every fixed
Picard iterate's numerical readouts.

There is also a uniform approximation of the true solution by these
iterates inside each individual state space. The first increment is
bounded by \(M_Tt\); integration and Lipschitz continuity bound the
\(h\)-th increment by \(M_TH_T^{h-1}t^h/h!\). Summing the tail gives

\[
\sup_{t\le T}\|S(t)-S^{[j]}(t)\|_{\mathcal X_L}
\le M_TT e^{H_TT}\frac{(H_TT)^j}{(j+1)!}.
\tag{EC10.13}
\]

All iterates stay in the common larger ball of radius
\(\|S_0\|+M_TT\). A current rooted polynomial readout is Lipschitz
on that ball by product telescoping. Trace norms of increments are
1-Lipschitz in trace norm. Ordered singular values satisfy
\(|s_k(A)-s_k(B)|\le\|A-B\|\le\|A-B\|_1\): one proof uses
\(s_k(A)=\inf_{\operatorname{rank}R<k}\|A-R\|\), obtained by
truncating a singular-value expansion and by testing the first \(k\)
right singular directions against any rank-\(<k\) map. These estimates
also control fixed best-rank tails
\(\sum_{k>N}s_k(P)=\|P\|_1-\sum_{k=1}^Ns_k(P)\).
Finite-rank readouts formed from field lists have the same within-space
control by their finite rank and (EC10.8).

For any named scalar readout \(\Sigma\), use the three terms

\[
|\Sigma(S_n)-\Sigma(S)|\le
 |\Sigma(S_n)-\Sigma(S_n^{[j]})|
 +|\Sigma(S_n^{[j]})-\Sigma(S^{[j]})|
 +|\Sigma(S^{[j]})-\Sigma(S)|.
\tag{EC10.14}
\]

The outer terms are estimated within their own spaces by (EC10.13).
For fixed \(j\), the middle term tends to zero by the finite-Gram
argument. Choosing \(j\) first and then \(n\) proves (EC10.6) and
all the stated fixed-readout convergences. This never subtracts states
from different spaces. The cutoff also avoids a restart induction across
uncontrolled polynomial iterates.

For completeness, trace tails are uniformly tight, not just pointwise
finite. On the same event, the field and its Lipschitz constant are
bounded on the actual state ball. Consequently
\(h_{\ell,n}(t)=\dot P_{\ell,n}(t)\) is Lipschitz in trace norm
with a deterministic constant \(C_T\), uniformly in \(n,\ell\):
combine time Lipschitz continuity of the state with (EC10.8) and the
polynomial field estimates. Approximate
\(P_{\ell,n}(t)=\int_0^t h_{\ell,n}(v)dv\) by its left Riemann sum
on \(N\) equal cells of \([0,T]\), including the last partial cell.
Every summand has rank at most one, and

\[
\sup_{t\le T}\|P_{\ell,n}(t)-P_{\ell,n}^{[N]}(t)\|_1
\le\frac{C_TT^2}{2N},\qquad
\operatorname{rank}P_{\ell,n}^{[N]}(t)\le N+1.
\tag{EC10.15}
\]

To see that this controls the nuclear tail, if \(R\) has rank at most
\(N+1\), the singular-value approximation formula above implies
\(s_{j+N+1}(P)\le s_j(P-R)\): approximate \(P-R\) by rank
\(<j\) and add \(R\). Summing over \(j\) gives
\(\sum_{j>N+1}s_j(P)\le\|P-R\|_1\). Apply this to (EC10.15), then
remove the source event. This proves (EC10.7); the same estimate holds
for the limiting increment. \(\square\)

## 11. Two hidden linear layers: a single spectral source

This comparison has \(L=2\), identity activation, and one unit-normalized
datum. More explicitly, \(m=1\), \(d\ge1\) is a fixed integer, and
\(x_1\in\mathbb R^d\) is fixed with
\(\|x_1\|^2/d=1\), and \(y_1=y\in\mathbb R\). The first matrix has
independent \(N(0,1)\) entries, the middle stored matrix has independent
\(N(0,1/n)\) entries, and the stored readout has independent
\(N(0,1)\) entries, all mutually independent. Mobilities for full MSE are
\(n\kappa,\kappa,n\kappa\), with \(\kappa>0\).

Put

\[
a_n=W^{(3)}/\sqrt n,\qquad
u_n=W^{(1)}x_1/\sqrt{dn},\qquad B_n=W^{(2)}.
\tag{EC11.1}
\]

The initial entries of these three proof factors are independent
\(N(0,1/n)\). Differentiating the first-layer projection multiplies its
backward velocity by \(x_1^Tx_1/d=1\); the components of \(W^{(1)}\)
orthogonal to this input remain fixed. Thus the exact projected equations
are (EC10.2) for \(L=2\), with
\(f_n=a_n^TB_nu_n\). Equivalently, if the middle matrix is written as
the raw matrix \(\mathsf A=\sqrt n B_n\) and the endpoints as
\(\sqrt n a_n,\sqrt n u_n\), all raw entries start as \(N(0,1)\),
\(f_n=n^{-3/2}(\sqrt n a_n)^T\mathsf A(\sqrt n u_n)\), and
all three raw blocks have mobility \(n\kappa\). This checks the
normalization of this equivalent unscaled storage. It does not whiten or
replace a multiple-sample Gram matrix.

Define the following fixed measures; \(\nu\) is the scalar source:

\[
\begin{aligned}
d\rho_0(\lambda)&=\frac1{2\pi}
 \sqrt{\frac{4-\lambda}{\lambda}}\,
 \mathbf1_{(0,4)}(\lambda)d\lambda,\\
d\rho_a(\lambda)&=\frac34\delta_{-1/2}(d\lambda)+
 \frac{\sqrt{\lambda(4-\lambda)}}{2\pi(1+2\lambda)}
 \mathbf1_{(0,4)}(\lambda)d\lambda,\\
d\rho_v(\lambda)&=\lambda\,d\rho_0(\lambda),\qquad
\nu=\rho_a+\rho_v.
\end{aligned}
\tag{EC11.2}
\]

In particular its explicit density and atom are

\[
d\nu(\lambda)=\frac34\delta_{-1/2}(d\lambda)+
\frac{(1+\lambda)\sqrt{\lambda(4-\lambda)}}{\pi(1+2\lambda)}
\mathbf1_{(0,4)}(\lambda)d\lambda.
\]

Thus \(\rho_a,\rho_v\) each have mass one, while \(\nu\) has mass
two; the scalar source is a finite measure, not a probability measure.
Its domain is \(\Lambda=\{-1/2\}\cup(0,4)\). Let

\[
\begin{array}{c|cc}
 &\alpha(\lambda)&\beta(\lambda)\\ \hline
\lambda=-1/2&1&0\\[1mm]
0<\lambda<4&[2(1+\lambda)]^{-1/2}&
 \bigl[(1+2\lambda)/(2(1+\lambda))\bigr]^{1/2}.
\end{array}
\tag{EC11.3}
\]

These satisfy \(\alpha^2\nu=\rho_a\), \(\beta^2\nu=\rho_v\).
For \(\psi,\pi\in L^2(\nu;\mathbb C)\) define real scalar readouts

\[
q=\int|\psi|^2d\nu,\qquad
F=\operatorname{Re}\int\overline\psi\,\pi\,d\nu,\qquad
K=\int\bigl\{|\pi|^2+(\lambda+2q)|\psi|^2\bigr\}d\nu.
\tag{EC11.4}
\]

Here \(q\) is a squared-field norm, and \(r\) below is always the
prediction-minus-label residual. The complex fields merely combine two
real channels each.

**Theorem EC11.** The autonomous physical-time equation

\[
\partial_t\psi=-2\kappa r\pi,\qquad
\partial_t\pi=-2\kappa r(\lambda+2q)\psi,\qquad
\dot r=-2\kappa rK,
\quad(\psi,\pi,r)(0)=(\alpha,i\beta,-y)
\tag{EC11.5}
\]

has a unique global solution in
\(L^2(\nu;\mathbb C)^2\times\mathbb R\). Its current triple is a
restart state along this initialized solution, and

\[
f=F=y+r,\quad \mathcal L=r^2,\quad q(0)=1,\quad K(0)=3,
\quad K(t)\ge\tfrac32,
\quad |r(t)|\le|y|e^{-3\kappa t}.
\tag{EC11.6}
\]

In particular the limiting loss tends to zero. The physical vector field
along this solution vanishes exactly when \(r=0\). If \(y=0\), the
initialized solution is stationary. For every fixed \(T<\infty\), the
finite flow at the initialization above satisfies

\[
\sup_{t\le T}\bigl(|f_n-f|+|K_n-K|+|r_n-r|+|r_n^2-r^2|\bigr)
\xrightarrow{\mathbb P}0,
\tag{EC11.7}
\]

where \(K_n=\|B_nu_n\|^2+\|B_n^Ta_n\|^2+
\|a_n\|^2\|u_n\|^2\). The proof also identifies its three separate
block energies. The fitting conclusion concerns the limiting system after
the width limit; (EC11.7) has a fixed physical horizon.

### 11.1. Exact finite reduction

Write \(g_n=-2\kappa r_n\), and temporarily omit \(n\) on factors.
Then \(\dot a=g_nBu,\dot u=g_nB^Ta,\dot B=g_nau^T\).
The product rule shows that

\[
C_n=B_nB_n^T-a_na_n^T,\qquad
\delta_n=\|a_n\|^2-\|u_n\|^2
\tag{EC11.8}
\]

are time independent: in \(\dot C_n\) the two terms
\(g_nau^TB^T+g_nBua^T\) cancel the derivative of \(aa^T\);
the two squared norms have the same derivative \(2g_nf_n\).
Set \(v_n=B_nu_n\), \(q_n=\|a_n\|^2\). Direct differentiation gives

\[
\dot a_n=g_nv_n,\qquad
\dot v_n=g_n[C_n+(2q_n-\delta_n)I]a_n,
\qquad f_n=a_n^Tv_n.
\tag{EC11.9}
\]

No inverse clock is used in this calculation. The scalar obtained by
differentiating \(a_n^Tv_n\) and removing its factor \(g_n\) is

\[
K_n=\|v_n\|^2+a_n^TC_na_n+(2q_n-\delta_n)q_n
=\|B_nu_n\|^2+\|B_n^Ta_n\|^2+q_n(q_n-\delta_n).
\tag{EC11.10}
\]

Let \(E_n\) be the spectral resolution of the fixed real symmetric
matrix \(C_n\), and define a positive matrix-valued measure

\[
\Sigma_n(S)=
\begin{pmatrix}
a_n(0)^TE_n(S)a_n(0)&a_n(0)^TE_n(S)v_n(0)\\
v_n(0)^TE_n(S)a_n(0)&v_n(0)^TE_n(S)v_n(0)
\end{pmatrix}.
\tag{EC11.11}
\]

For two real vector fields \(\mathbf c_n,\mathbf d_n\) of length two,
use

\[
\begin{aligned}
\dot{\mathbf c}_n&=g_n\mathbf d_n,&
\dot{\mathbf d}_n&=g_n(\lambda+2q_n-\delta_n)\mathbf c_n,\\
\mathbf c_n(\lambda,0)&=(1,0)^T,&
\mathbf d_n(\lambda,0)&=(0,1)^T.
\end{aligned}
\tag{EC11.12}
\]

Functional calculus and uniqueness for (EC11.9) give
\(a_n=c_{n,1}(C_n)a_n(0)+c_{n,2}(C_n)v_n(0)\), with the corresponding
formula for \(v_n\) using \(\mathbf d_n\). Consequently the reduction
closes exactly with

\[
\begin{aligned}
q_n&=\int\mathbf c_n^T\,d\Sigma_n\,\mathbf c_n,\\
f_n&=\int\mathbf c_n^T\,d\Sigma_n\,\mathbf d_n,\\
K_n&=\int\mathbf d_n^T\,d\Sigma_n\,\mathbf d_n+
 \int(\lambda+2q_n-\delta_n)\mathbf c_n^T\,d\Sigma_n\,\mathbf c_n,\\
\dot r_n&=g_nK_n,\qquad r_n(0)=f_n(0)-y.
\end{aligned}
\tag{EC11.13}
\]

Conversely, while the displayed mode equations exist, the functional-calculus
vectors solve (EC11.9) and have these readouts; local uniqueness identifies
them with the finite network. Its global physical existence was proved by
(EC10.9)--(EC10.10), which apply verbatim to these projected equations.

### 11.2. Derivation of the fixed spectral source

We prove

\[
\Sigma_n\Longrightarrow
\Sigma=\begin{pmatrix}\rho_a&0\\0&\rho_v\end{pmatrix}
\quad\text{entrywise weakly in probability},\qquad \delta_n\to0.
\tag{EC11.14}
\]

Every nontrivial random-matrix input will be obtained from Lemma EC9.
Let \(M_n=B_n(0)B_n(0)^T\). Applied to the trace word \((BB^T)^k\),
its Wick proof says that the limiting normalized moment is the number
\(C_k\) of noncrossing pairings of \(2k\) positions. Every such pairing
matches opposite parity positions, since the interval inside a pair has
even length; for this alternating word those positions have opposite
transpose markers. Pair the first position and split into the inside
and outside intervals to obtain

\[
C_0=1,\qquad C_k=\sum_{j=0}^{k-1}C_jC_{k-1-j},\qquad
\frac1n\operatorname{Tr}M_n^k\xrightarrow{L^2}C_k.
\tag{EC11.15}
\]

The density \(\rho_0\) in (EC11.2) has these same moments. In fact the
substitution \(\lambda=4t\) gives

\[
\int\lambda^k d\rho_0
=\frac{4^{k+1}}{2\pi}\int_0^1t^{k-1/2}(1-t)^{1/2}dt
=\frac{(2k)!}{k!(k+1)!}.
\tag{EC11.16}
\]

For the last equality, the integral at \(k=0\) is \(\pi/2\) by
\(t=\sin^2\theta\). Integrating the derivative of
\(t^{k+1/2}(1-t)^{3/2}\), whose boundary terms vanish, shows that
successive integrals have ratio \((k+1/2)/(k+2)\). This proves the
factorial expression by induction. The recursion in (EC11.15) gives
the formal series equation \(C(z)=1+zC(z)^2\); solving the quadratic
with constant term one and expanding \(\sqrt{1-4z}\) gives the same
factorial coefficients. Thus (EC11.16) identifies every moment.

On the event (EC9.4) all eigenvalues of \(M_n\) lie in \([0,144]\).
Moment convergence therefore gives weak convergence of its empirical
measure to \(\rho_0\). Here is an explicit approximation justification
used again below. On a compact interval, map a continuous test function
to \(h\in C([0,1])\), and use its Bernstein polynomial
\(p_N(t)=\sum_{j=0}^N h(j/N)\binom Nj t^j(1-t)^{N-j}\).
Writing the sum as \(\mathbb E h(Z/N)\) for a binomial \(Z\) gives

\[
\|p_N-h\|_\infty\le\omega_h(\varepsilon)
 +\frac{2\|h\|_\infty}{4N\varepsilon^2},
\tag{EC11.17}
\]

because \(\operatorname{Var}(Z/N)\le1/(4N)\). Choose \(\varepsilon\)
small and then \(N\) large. Polynomial tests thus approximate continuous
tests uniformly, with the error controlled by the measures' bounded
total variations. The complement of (EC9.4) has vanishing probability.

Define the scalar resolvent transform
\(\mathfrak m(z)=\int(z-\lambda)^{-1}d\rho_0(\lambda)\).
The moment recursion implies, initially for real \(z<-4\),

\[
\mathfrak m(z)=\frac{1-\sqrt{1-4/z}}2,\qquad
z\mathfrak m(z)(1-\mathfrak m(z))=1.
\tag{EC11.18}
\]

The square root is positive on the negative real axis. Its extension
to every \(z=-b<0\), including \(-1/2\), can be verified by elementary
integration. The substitution \(\lambda=4\sin^2\theta\) gives
\(d\rho_0=(4/\pi)\cos^2\theta\,d\theta\). Also

\[
I_b:=\int_0^{\pi/2}\frac{d\theta}{b+4\sin^2\theta}
=\int_0^\infty\frac{du}{b+(b+4)u^2}
=\frac{\pi}{2\sqrt{b(b+4)}}
\quad(b>0),
\]

using \(u=\tan\theta\). Since
\(\cos^2\theta/(b+4\sin^2\theta)
=(1+b/4)/(b+4\sin^2\theta)-1/4\), it follows that
\(\mathfrak m(-b)=-(4/\pi)[(1+b/4)I_b-\pi/8]
=(1-\sqrt{1+4/b})/2\). In particular
\(\mathfrak m(-1/2)=-1\), with no analytic inversion step.

Let \(a=a_n(0)\), independent of \(M_n\). For fixed real \(z<-4\),
set \(h_n(z)=a^T(z-M_n)^{-1}a\). Conditional variance (EC9.7), with
resolvent norm at most \(1/|z|\), and the weak empirical limit give
\(h_n(z)\to\mathfrak m(z)\) in probability. Since
\(z-C_n=z-M_n+aa^T\), solving this rank-one perturbation explicitly gives

\[
(z-C_n)^{-1}a=\frac{(z-M_n)^{-1}a}{1+h_n(z)},\qquad
a^T(z-C_n)^{-1}a\longrightarrow
\frac{\mathfrak m(z)}{1+\mathfrak m(z)}.
\tag{EC11.19}
\]

The formula is used where its inverse exists; on (EC9.4),
\(C_n\ge-4I\), so this holds for all \(z<-4\), and its limiting
denominator is nonzero there.

We verify the proposed \(\rho_a\) directly, including its negative
atom, rather than leaving an inversion claim implicit. Its continuous
part is \(\lambda(1+2\lambda)^{-1}d\rho_0\). From
\(\mathfrak m(-1/2)=-1\),
\(\int(1+2\lambda)^{-1}d\rho_0=1/2\), so this continuous part has
mass \(\tfrac12(1-1/2)=1/4\). For \(z<-4\), partial fractions give

\[
\begin{aligned}
\int\frac{d\rho_a(\lambda)}{z-\lambda}
&=\frac{3}{4(z+1/2)}+
 \frac{z\mathfrak m(z)-1/2}{1+2z}\\
&=\frac{z\mathfrak m(z)+1}{1+2z}
=\frac{\mathfrak m(z)}{1+\mathfrak m(z)}.
\end{aligned}
\tag{EC11.20}
\]

The final equality is exactly \(z\mathfrak m(1-\mathfrak m)=1\).
This proves the atom and density by an explicit transform computation.

For precision, convergence of the transforms here implies weak convergence
without presuming a spectral edge theorem or an unproved inversion rule.
The measures \(a^TE_n(\cdot)a\) have support in \(J=[-4,144]\) and
bounded mass on (EC9.4); their mass \(\|a\|^2\) converges to one.
For \(|z|>144\), expand

\[
\frac1{z-\lambda}=\sum_{j=0}^k\frac{\lambda^j}{z^{j+1}}
 +\frac{\lambda^{k+1}}{z^{k+1}(z-\lambda)}.
\tag{EC11.21}
\]

After multiplying the integrated remainder by \(|z|^{k+1}\), it is
bounded by the mass times \(144^{k+1}/(|z|-144)\). Induction on \(k\)
now proves convergence of every moment: take \(z< -144\) sufficiently
large in magnitude to make these remainder bounds small, then use
transform convergence and the already convergent lower moments at this
fixed \(z\). Finally (EC11.17) proves weak convergence of the first
diagonal entry of \(\Sigma_n\) to \(\rho_a\).

For the other entries, condition on \((B_n(0),a_n(0))\), so that
\(u_n(0)\sim N(0,I_n/n)\) is independent and
\(v_n(0)=B_n(0)u_n(0)\). For each fixed real polynomial \(p\), (EC9.7)
gives

\[
v_n(0)^Tp(C_n)v_n(0)-\frac1n\operatorname{Tr}[M_np(C_n)]
\xrightarrow{\mathbb P}0.
\tag{EC11.22}
\]

Indeed its conditional variance is bounded by
\(2\|B_n(0)\|^4\|p(C_n)\|^2/n\) on a norm event measurable from
the conditioning variables. Since \(C_n-M_n=-aa^T\), telescoping powers
gives
\(\|C_n^k-M_n^k\|_1\le kR^{k-1}\|a\|^2\) whenever both operator
norms are at most \(R\). Therefore

\[
\frac1n\operatorname{Tr}[M_np(C_n)]
-\frac1n\operatorname{Tr}[M_np(M_n)]\longrightarrow0
\tag{EC11.23}
\]

on that event, with an \(O(n^{-1})\) bound. Equations (EC11.15)--(EC11.16)
identify its limit as \(\int\lambda p(\lambda)d\rho_0\), giving
\(\rho_v=\lambda\rho_0\). Conditional centering in \(u_n(0)\) also gives

\[
\mathbb E[a^Tp(C_n)B_n(0)u_n(0)\mid B_n(0),a]=0,
\quad
\operatorname{Var}[a^Tp(C_n)B_n(0)u_n(0)\mid B_n(0),a]
\le\frac{\|B_n(0)\|^2\|p(C_n)\|^2\|a\|^2}{n}.
\tag{EC11.24}
\]

This makes every polynomial test of the cross entry tend to zero. Its
total variation is at most \(\|a\|\|v_n(0)\|\): for any spectral
partition sum the bounds
\(|a^TE_n(S)v|\le\sqrt{a^TE_n(S)a}\sqrt{v^TE_n(S)v}\) and apply
Cauchy--Schwarz. The diagonal masses are \(\|a\|^2,\|v_n(0)\|^2\),
bounded on (EC9.4). Thus (EC11.17) extends every polynomial convergence
above to continuous tests, proving (EC11.14). Also
\(\delta_n\to0\) by the two Gaussian squared-norm laws, and
\(\mathbb E f_n(0)^2=1/n\), by first averaging in \(u_n(0)\), then
in \(a_n(0),B_n(0)\); hence \(f_n(0)\to0\).

These calculations check all initial constants. In particular,
\(\int\lambda d\rho_a=0\): directly its continuous contribution is
\(\int\lambda^2/(1+2\lambda)d\rho_0=1/2-1/4+1/8=3/8\), which
cancels the atom's \(-3/8\). Since
\(\int d\rho_a=\int d\rho_v=1\), (EC11.4) gives
\(q(0)=1,F(0)=0,K(0)=1+0+2=3\).

### 11.3. Global physical spectral dynamics

Multiplication by \(\lambda\) is bounded on \(L^2(\nu)\), because
\(\operatorname{supp}\nu\subset[-1/2,4]\). The functionals in
(EC11.4) are continuous polynomials in Hilbert fields, with their real
and imaginary parts treated as real variables. Thus the vector field
(EC11.5) is locally Lipschitz on
\(L^2(\nu;\mathbb C)^2\times\mathbb R\), by Cauchy--Schwarz and
product telescoping. The integral contraction supplies a unique maximal
solution.

On that solution, differentiation of the Hilbert pairings gives

\[
\dot F=-2\kappa rK=\dot r,\qquad F=y+r,\qquad
\dot q=-4\kappa rF,
\tag{EC11.25}
\]
\[
K\ge2q^2-\tfrac12q.
\tag{EC11.26}
\]

The derivatives are justified by differentiability in Hilbert norm and
boundedness of multiplication by \(\lambda\). To handle the negative
atom explicitly, work initially on the interval where \(q>1/2\).
Then (EC11.26) is positive, and the scalar residual equation yields
\(r=-y\vartheta(t)\) with the scalar
\(\vartheta(t)=\exp(-2\kappa\int_0^tK)\in(0,1]\).
Consequently \(F=y(1-\vartheta)\), and

\[
0\le\dot q=4\kappa y^2\vartheta(1-\vartheta)\le\kappa y^2.
\tag{EC11.27}
\]

Starting at \(q=1\), it cannot exit through \(1/2\). This proves,
on the full maximal interval,
\(1\le q(t)\le1+\kappa y^2t\), \(|r|\le|y|\), and
\(K\ge3/2\). It follows that for each finite \(T\),

\[
\|\psi(t)\|_{L^2(\nu)}\le\sqrt{1+\kappa y^2T},\qquad
\|\dot\pi(t)\|_{L^2(\nu)}
\le2\kappa|y|[4+2(1+\kappa y^2T)]\sqrt{1+\kappa y^2T}.
\tag{EC11.28}
\]

Together with \(\|\pi(0)\|=1\), these bound the entire state on each
finite interval. Boundedness of the vector field on state balls gives
continuation by the norm-limit argument used in Theorem EC10. This proves
global existence and restart along the canonical trajectory directly in
physical time. The residual equation and \(K\ge3/2\) prove (EC11.6).
If \(r\ne0\), its own derivative is nonzero; if \(r=0\), all three
velocities vanish. At \(y=0\) the initialized triple is stationary by
uniqueness. No feature-time completeness, feature-time blow-up theorem,
or limiting-clock localization is required here.

### 11.4. Uniform finite-width identification in physical time

The diagonal source \(\Sigma\) has the scalar encoding
\(\psi=\alpha c_1+i\beta c_2\),
\(\pi=\alpha d_1+i\beta d_2\), where
\(\mathbf c,\mathbf d\) solve (EC11.12) with
\(g=-2\kappa r,\delta=0\). Their coefficients can be defined on the
whole fixed interval \(J=[-4,144]\). The global solution just proved
supplies continuous bounded \(r(t),q(t)\) on \([0,T]\); the resulting
linear mode equations have a unique solution continuous in
\((\lambda,t)\in J\times[0,T]\). Their integral equations bound
\(\sup_{\lambda}(|\mathbf c|+|\mathbf d|)\) by a constant times
its time integral plus its initial value; iteration gives a finite
exponential bound, and also continuity in \(\lambda\). Uniqueness of
the linear equations with these coefficients shows that the displayed
encoding equals the initialized \(\psi,\pi\) of (EC11.5). Thus the
mode integrals with \(\Sigma\) give exactly (EC11.4).

For finite \(n\), extend (EC11.12) off its spectral support in the same
way to all of \(J\). On (EC9.4) that support lies in \(J\), and all
entries of \(\Sigma_n\) have a common total-variation bound (for
example its diagonal masses are at most \(4\) and \(576\)). By
(EC11.14), the integrals against \(\Sigma_n-\Sigma\) of the functions

\[
c_i(\lambda,t)c_j(\lambda,t),\quad
c_i(\lambda,t)d_j(\lambda,t),\quad
d_i(\lambda,t)d_j(\lambda,t),\quad
\lambda c_i(\lambda,t)c_j(\lambda,t)
\tag{EC11.29}
\]

tend to zero in probability, uniformly in \(t\le T\), for
\(i,j\in\{1,2\}\). Indeed each family is the continuous image of
the compact time interval in \(C(J)\), hence has finite uniform nets.
Use weak convergence for the finitely many tests in a net; its remaining
error is bounded by the net tolerance times the common total variation.
Let \(\varepsilon_n(T)\) be the maximum of these uniform integral
errors, so \(\varepsilon_n(T)\to0\) in probability on the norm event.

Subtract the mode and residual equations, stopping when
\(E_n(t)=\sup_{v\le t}(\|\mathbf c_n-\mathbf c\|_\infty+
\|\mathbf d_n-\mathbf d\|_\infty+|r_n-r|)\) first reaches one.
Before that time all mode states lie in one fixed ball. Expanding one
factor at a time in (EC11.13) gives

\[
|q_n-q|+|f_n-F|+|K_n-K|
\le C_T\bigl(E_n(t)+\varepsilon_n(T)+|\delta_n|\bigr).
\tag{EC11.30}
\]

For example the \(q\) difference is the sum of a measure-test error
for \(\mathbf c^T\mathbf c\) and two differences of a single bounded
mode factor integrated against \(\Sigma_n\). The other quadratic terms
have the identical expansion. The factor \(2q_n-\delta_n\) in the
kernel adds the already bounded \(q\) difference and \(|\delta_n|\).
All bounds use only the common total variations and mode ball.
Subtracting the integral equations therefore yields

\[
E_n(t)\le |f_n(0)|+
C_T\int_0^t\bigl(E_n(v)+\varepsilon_n(T)+|\delta_n|\bigr)dv.
\tag{EC11.31}
\]

Iteration of this scalar inequality gives
\(E_n(T)\le C'_T(|f_n(0)|+\varepsilon_n(T)+|\delta_n|)\) before
stopping. With probability tending to one this is less than one, so a
first stopping time at or before \(T\) is impossible by continuity.
This proves (EC11.7) using (EC11.30) and boundedness of the residual
for the squared-loss readout. It also proves convergence of \(q_n\).

The three separate block energies have the formulas

\[
\begin{aligned}
\|B_nu_n\|^2&=\int\mathbf d_n^T\,d\Sigma_n\,\mathbf d_n,\\
\|B_n^Ta_n\|^2&=\int\lambda\mathbf c_n^T\,d\Sigma_n\,\mathbf c_n+q_n^2,\\
\|a_n\|^2\|u_n\|^2&=q_n(q_n-\delta_n).
\end{aligned}
\tag{EC11.32}
\]

The middle identity uses \(BB^T=C+aa^T\). Their limits are respectively
\(\int|\pi|^2d\nu\),
\(\int\lambda|\psi|^2d\nu+q^2\), and \(q^2\), by the same
estimates. They sum to (EC11.4). This finishes the theorem with all
normalizations and compact-time observables identified. \(\square\)

## 12. Exact agreement and the limits of the comparisons

At \(L=1\) with \(\phi(z)=z\), the characteristic equations are
\(A_s=U,U_s=A\). Their solutions are
\(A_s=a_0\cosh s+u_0\sinh s\) and
\(U_s=u_0\cosh s+a_0\sinh s\). Taking the two Gaussian moments gives
\(F(s)=\sinh(2s)\), \(K(s)=2\cosh(2s)\). In Theorem EC10 at
\(L=1\), the two orthonormal roots have exactly the same pairings,
and its Hilbert-vector equations give these same readouts. The scalar
physical clock is \(\dot s=-2\kappa(\sinh(2s)-y)\). Thus the linear
member of the shallow family and the first member of the fixed-depth
family coincide, while Section 8 also allows the stated nonlinear
activations at that shallow depth.

At \(L=2\) and \(x_1=1\), Theorems EC10 and EC11 describe the same
finite initialization and physical flow. Each proves convergence in
probability on every compact horizon, so their deterministic limits for
\(f,K,r,\mathcal L\) and the separate block energies agree. To see
uniqueness of this identification directly, their deterministic difference
is bounded by the sum of their two errors against the same finite
readout, and both errors tend to zero in probability. The spectral
description is a special reduction of those readouts; it does not assert
that all rooted operator signatures can be reconstructed from its fields.

At \(L=3\), the same normalization and uniqueness-of-limit argument
identify Theorem EC10's rooted readouts with the cyclic construction of
Sections 1--4. Lemma EC9's direct-sum source and the chapter's two final
root colors have identical rooted Grams: words in matrix colors preserve
the final root color. No additional independence of a transpose action
is introduced by either representation.

All three comparisons use stored readout entries of variance one. Equal
limiting initial predictions would not identify them with the small-readout
regime. Sections 8 and 10 have one scalar datum; Section 11 has the exact
one-normalized-datum projection stated there. None of these additions
asserts an arbitrary-data theorem, a raw-GD bridge, a depth-uniform
estimate, or a joint width/long-time limit. In particular, the GD result
already present for \(L=3\) in Section 4 is not being attached to these
new statements, and the fixed-program theorem of `gaussian_calculus.md`
is not used as a continuous-time theorem.
