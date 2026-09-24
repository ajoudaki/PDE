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

