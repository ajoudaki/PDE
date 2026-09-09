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
