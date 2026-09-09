# Three hidden linear layers: finite-moment no-go and operator IDE

Status: corrected, self-contained theorem and proof.  The negative theorem is
deliberately narrower than the informal phrase “no finite PDE”: it rules out a
fixed finite list of state-universal contraction moments.  The positive theorem
gives a fixed-domain, one-kernel IDE and a simultaneous width/mesh limit.

## 1. The result

Fix one scalar input and one scalar label \(y\in\mathbb R\).  At width \(n\),
write the four trainable linear maps as

\[
x,a\in\mathbb R^n,
\qquad B,R\in\mathbb R^{n\times n},
\qquad f_n=a^{\mathsf T}RBx.
\tag{1.1}
\]

Initially all entries of \(a,x,B,R\) are mutually independent
\(N(0,n^{-1})\).  Put \(e_n=y-f_n\) and
\(\mathcal L_n=e_n^2\).  For a fixed mobility \(\eta>0\), physical gradient
flow is

\[
\begin{aligned}
\dot a&=2\eta e_n RBx,
&\dot R&=2\eta e_n\,a(Bx)^{\mathsf T},\\
\dot B&=2\eta e_n\,(R^{\mathsf T}a)x^{\mathsf T},
&\dot x&=2\eta e_n B^{\mathsf T}R^{\mathsf T}a.
\end{aligned}
\tag{1.2}
\]

Equivalently, take raw standard-normal factors
\(\widetilde a,\widetilde x,\widetilde B,\widetilde R\), put every normalized
factor equal to its raw counterpart divided by \(\sqrt n\), and use the raw
feature \(n^{-2}\widetilde a^{\mathsf T}\widetilde R\widetilde B
\widetilde x\).  Raw Euclidean gradient flow with common mobility
\(n\eta\) becomes exactly (1.2) after division by \(\sqrt n\).  Thus the
normalization and the \(\mu\)P clock are explicit.  If one separately
requires the raw discrete multiplier \(n\eta\delta_n\) to vanish, one may
take \(\delta_n=o(n^{-1})\); Theorem 1 below proves the normalized joint
limit for the larger class \(\delta_n\to0\).

The simultaneous exact-GD step with physical mesh \(\delta>0\) is obtained
by replacing every time derivative in (1.2) by the corresponding increment
divided by \(\delta\), with all right-hand sides evaluated at the old state.

### Theorem 1 (sharp joint statement)

The following two assertions hold.

1. **Finite scalar contraction no-go.**  There do not exist integers
   \(k,D<\infty\), independent of \(n\), scalar coordinates
   \(g_1^{(n)},\ldots,g_k^{(n)}\), and a fixed polynomial vector field
   \(V:\mathbb R^k\to\mathbb R^k\) such that:

   - every \(g_j^{(n)}\) is given, uniformly in \(n\), by a finite linear
     combination of typed same-time complete-contraction graphs of total
     tensor degree at most \(D\);
   - \(g_1^{(n)}=f_n\);
   - for every sufficiently large \(n\) and every state,
     \(\mathscr D_n g^{(n)}=V(g^{(n)})\), where \(\mathscr D_n\) is the
     feature-ascent derivation obtained from (1.2) after deleting the scalar
     factor \(2\eta e_n\).

   The same conclusion holds for an ambient real-analytic germ \(V\) if the
   identity is required on a full neighborhood of the zero state.  It does
   **not** rule out a fixed number of continuum fields, an orbit-fitted scalar
   equation, a width-dependent closure, or an arbitrary non-contraction
   encoding.

2. **Positive operator-IDE and joint diagonal limit.**  There is an explicit
   fixed separable Hilbert space \(\mathscr H_\infty\), a fixed bounded source
   \(\mathcal C_0\), one evolving trace-class kernel \(Q(t)\), and one scalar
   \(e(t)\) satisfying

   \[
   \begin{aligned}
   \dot Q&=2\eta e(\mathcal C_0^*+Q^*)^3,\\
   K&=\operatorname {Tr}
      [(\mathcal C_0+Q)^3(\mathcal C_0^*+Q^*)^3],\\
   \dot e&=-2\eta eK,
   \qquad Q(0)=0,
   \qquad e(0)=y.
   \end{aligned}
   \tag{1.3}
   \]

   This system has a unique global solution, is autonomous and restartable,
   and

   \[
   f(t)=\frac14\operatorname {Tr}(\mathcal C_0+Q(t))^4=y-e(t),
   \qquad \mathcal L(t)=e(t)^2.
   \tag{1.4}
   \]

   If \(\delta_n\downarrow0\) is arbitrary and the exact-GD iterates are
   linearly interpolated in the parameters, then for every \(T<\infty\),

   \[
   \sup_{0\le t\le T}
   \bigl(
   |f_{n,\delta_n}(t)-f(t)|
   +|K_{n,\delta_n}(t)-K(t)|
   +|\mathcal L_{n,\delta_n}(t)-\mathcal L(t)|
   \bigr)
   \xrightarrow{\mathbb P}0.
   \tag{1.5}
   \]

   The same argument identifies every fixed finite family of current rooted
   word/finite-rank observables.  Thus (1.3) is the mean-field state, not only
   an equation fitted to the output.  No relation between \(\delta_n\) and
   \(n\), beyond \(\delta_n\to0\), is needed.

The two conclusions are compatible: one kernel on a fixed infinite spatial
domain is an \(O(1)\) **field count**, but it contains infinitely many scalar
coordinates.  The first assertion concerns an \(O(1)\) **numerical state
dimension**.

## 2. Exact finite-width cyclic algebra

Feature time \(s\) is defined by deleting \(2\eta e_n\) from (1.2):

\[
\begin{aligned}
a'&=RBx,&R'&=a(Bx)^{\mathsf T},\\
B'&=(R^{\mathsf T}a)x^{\mathsf T},&
x'&=B^{\mathsf T}R^{\mathsf T}a.
\end{aligned}
\tag{2.1}
\]

On \(\mathscr H_n=\mathbb R\oplus(\mathbb R^n)^{\oplus3}\), set

\[
\mathcal C_n=
\begin{pmatrix}
0&0&0&a^{\mathsf T}\\
x&0&0&0\\
0&B&0&0\\
0&0&R&0
\end{pmatrix}.
\tag{2.2}
\]

The four nonzero blocks of \((\mathcal C_n^{\mathsf T})^3\) are exactly the
four right-hand sides of (2.1), with the orientations shown in (2.2).  Hence

\[
\mathcal C_n'=(\mathcal C_n^{\mathsf T})^3.
\tag{2.3}
\]

Every length-three path around the four-cycle contains at least one of the
two rank-one endpoint blocks.  Thus

\[
\operatorname {rank}\mathcal C_n^3\le4.
\tag{2.4}
\]

The four diagonal blocks of \(\mathcal C_n^4\) have trace
\(a^{\mathsf T}RBx\).  Therefore

\[
f_n=\frac14\operatorname {Tr}\mathcal C_n^4.
\tag{2.5}
\]

Taking the squared Hilbert--Schmidt norm in (2.3) gives

\[
\begin{aligned}
K_n
&=\|RBx\|^2+\|a\|^2\|Bx\|^2
  +\|R^{\mathsf T}a\|^2\|x\|^2
  +\|B^{\mathsf T}R^{\mathsf T}a\|^2\\
&=\operatorname {Tr}
  [\mathcal C_n^3(\mathcal C_n^{\mathsf T})^3]
=f_n'.
\end{aligned}
\tag{2.6}
\]

The final equality follows either by the product rule in (1.1), or by
cyclicity of the finite-dimensional trace in (2.5).  In physical time,

\[
\dot f_n=2\eta e_nK_n,
\qquad
\frac d{dt}e_n^2=-4\eta e_n^2K_n.
\tag{2.7}
\]

Finally,

\[
\mathcal C_n^{\mathsf T}\mathcal C_n
-\mathcal C_n\mathcal C_n^{\mathsf T}
\tag{2.8}
\]

is constant: differentiating either Gram matrix with (2.3) gives
\(\mathcal C_n^4+(\mathcal C_n^{\mathsf T})^4\).  This invariant explains the
balancedness structure, but it does not make the two middle sources commute.

## 3. The finite-scalar no-go

### 3.1 Contraction graphs and their stable independence

A typed contraction graph is a finite tensor network built from copies of
\(a,x,B,R\) and their transposes, with every layer index paired and summed.
Two graphs are identified only by a type-preserving graph isomorphism.  Write
\(P_G^{(n)}(a,R,B,x)\) for its scalar contraction.  Multiplication obeys

\[
P_G^{(n)}P_H^{(n)}=P_{G\sqcup H}^{(n)}.
\tag{3.1}
\]

We need the following stable-range fact.

### Lemma 2 (stable graph independence)

For every finite family of pairwise nonisomorphic typed contraction graphs,
their contraction polynomials are linearly independent when the layer
dimensions are sufficiently large.

#### Proof

Regard all entries of the four tensors as independent commuting
indeterminates.  Besides \(P_G\), introduce the injective contraction
\(I_G\), in which distinct graph-index vertices must receive distinct layer
indices.  Splitting all index maps according to their equality partition
gives a finite triangular relation

\[
P_G=\sum_{\pi} I_{G/\pi}.
\tag{3.2}
\]

Here \(\pi\) ranges over type-compatible partitions and \(G/\pi\) is the
corresponding quotient graph.  Möbius inversion on the finite partition
lattice expresses every \(I_G\) as a linear combination of the \(P_H\).

Suppose a finite linear combination of the \(I_G\)'s vanished in every
sufficiently large dimension.  Choose a graph \(G_0\) with nonzero
coefficient and a maximal number of typed vertices.  Use exactly that many
indices in each layer.  In the polynomial expansion, the monomial obtained
from one bijective labeling of \(G_0\) can occur in \(I_H\) only when \(H\)
is type-preservingly isomorphic to \(G_0\); injectivity and the independent
edge/vector indeterminates recover every incidence.  Its coefficient cannot
cancel.  Hence all coefficients are zero.  The invertible triangular
change (3.2) proves the same assertion for the \(P_G\)'s.  \(\square\)

The qualification “sufficiently large” is essential: at fixed \(n\),
Cayley--Hamilton identities create relations among long words.

### 3.2 An unbounded connected path ladder

Put \(A=RB\) and \(C=A^{\mathsf T}A=B^{\mathsf T}R^{\mathsf T}RB\).  Let
\(\mathscr D_0\) be the branch of the feature derivation which differentiates
only the endpoint vectors:

\[
\mathscr D_0a=Ax,
\qquad
\mathscr D_0x=A^{\mathsf T}a,
\qquad
\mathscr D_0A=0.
\tag{3.3}
\]

For \(j\ge0\), define

\[
U_j=a^{\mathsf T}AC^jx,
\quad
X_j=x^{\mathsf T}C^{j+1}x,
\quad
Y_j=a^{\mathsf T}(AA^{\mathsf T})^{j+1}a.
\tag{3.4}
\]

Since \(AC^jA^{\mathsf T}=(AA^{\mathsf T})^{j+1}\), direct differentiation
gives

\[
\mathscr D_0U_j=X_j+Y_j,
\qquad
\mathscr D_0X_j=\mathscr D_0Y_j=2U_{j+1}.
\tag{3.5}
\]

Starting with \(U_0=f_n\), induction in (3.5) yields

\[
\mathscr D_0^{\,2m-1}f_n
=4^{m-1}
\left[
x^{\mathsf T}C^mx
+a^{\mathsf T}(AA^{\mathsf T})^ma
\right].
\tag{3.6}
\]

Every product-rule coefficient in the full feature derivation
\(\mathscr D_n\) is nonnegative.  One of its differentiation histories is
the endpoint-only history (3.3).  Consequently

\[
\mathscr D_n^{\,2m-1}f_n
\quad\hbox{contains}\quad
4^{m-1}x^{\mathsf T}
(B^{\mathsf T}R^{\mathsf T}RB)^mx
\tag{3.7}
\]

with a positive coefficient; no other history can cancel it.  The graph in
(3.7) is connected, and its length tends to infinity with \(m\).

### 3.3 Contradiction to a finite polynomial closure

Let \(\mathcal S\) be the finite set of connected component types occurring
in the graph expansions of \(g_1,\ldots,g_k\).  By (3.1), every polynomial
in the \(g_j\)'s is a linear combination of graphs whose connected
components belong to \(\mathcal S\).

If \(\mathscr D_ng=V(g)\), repeated differentiation gives

\[
\mathscr D_n^rf_n=H_r(g_1^{(n)},\ldots,g_k^{(n)})
\tag{3.8}
\]

for a polynomial \(H_r\): start with \(H_0(u)=u_1\) and set

\[
H_{r+1}(u)=\sum_{j=1}^k
\frac{\partial H_r}{\partial u_j}(u)V_j(u).
\tag{3.9}
\]

Choose \(m\) so large that the connected path in (3.7) is not in
\(\mathcal S\).  Equation (3.8) says its coefficient is zero, while (3.7)
says it is positive.  Lemma 2 makes this a genuine polynomial
contradiction in sufficiently large dimension.

For an analytic germ, subtract the constants \(g_j(0)\), expand \(V\) at
that point, and scale the raw tensors by a common scalar \(\lambda\).  At
each fixed tensor degree only finitely many Taylor monomials contribute.
Their graph components still lie in \(\mathcal S\), so comparison of the
coefficient of the finite degree in (3.7) gives the same contradiction.
This proves assertion 1 of Theorem 1.  \(\square\)

The state-universal hypothesis cannot be deleted.  On a single strictly
monotone analytic feature orbit, one may define
\(\kappa(u)=K(f^{-1}(u))\), giving the orbit-fitted scalar equation
\(f'=\kappa(f)\).  It contains the trajectory in its definition and is not a
state-universal moment closure.

## 4. A self-contained Gaussian pointed-source limit

The width proof needs less than strong random-matrix convergence: fixed-word
moments, Gaussian-root concentration, and a uniform bound on the two matrix
norms suffice.  We prove exactly those facts here.

Let

\[
\mathcal F=\mathbb C\Omega\oplus
\bigoplus_{q\ge1}(\mathbb C^6)^{\otimes q}
\tag{4.1}
\]

be full Fock space.  For the left creation isometries
\(\ell_1,\ldots,\ell_6\), set

\[
b=\ell_1+\ell_2^*,
\qquad
r=\ell_3+\ell_4^*,
\qquad
\xi_x=\ell_5\Omega,
\qquad
\xi_a=\ell_6\Omega.
\tag{4.2}
\]

Let \(J\) be coordinatewise complex conjugation in the word basis.
Every \(\ell_j\) commutes with \(J\), so the fixed real Hilbert space
\(\operatorname {Fix}(J)\) is invariant under all displayed operators.
All dynamics below start in that real form and remain there by uniqueness;
the complex notation is only a convenient Fock representation of real
transposes.

The last tensor letter of a word generated from \(\xi_x\) or \(\xi_a\) by
the first four colors cannot change.  Therefore, for every
\(*\)-polynomial \(P\) in \(b,r\),

\[
\begin{aligned}
\langle\xi_x,P(b,r)\xi_x\rangle
&=\langle\Omega,P(b,r)\Omega\rangle,\\
\langle\xi_a,P(b,r)\xi_a\rangle
&=\langle\Omega,P(b,r)\Omega\rangle,\\
\langle\xi_a,P(b,r)\xi_x\rangle&=0.
\end{aligned}
\tag{4.3}
\]

### Lemma 3 (pointed Gaussian-word convergence)

Let \(B_n,R_n\) be independent real matrices with iid \(N(0,n^{-1})\)
entries, and let \(x_n,a_n\) be independent \(N(0,n^{-1}I_n)\) vectors,
independent of both matrices.  For every fixed finite list of words
\(P_1,\ldots,P_N\) in \(B_n,R_n,B_n^{\mathsf T},R_n^{\mathsf T}\), all Gram
entries

\[
\langle P_ig_{\alpha,n},P_jg_{\beta,n}\rangle,
\qquad \alpha,\beta\in\{x,a\},
\tag{4.4}
\]

converge in probability to the corresponding quantities in (4.3), with
\(B_n,R_n\) replaced by \(b,r\).  Moreover, for one deterministic constant
\(L<\infty\),

\[
\mathbb P\{
\|B_n\|+\|R_n\|+\|x_n\|+\|a_n\|\le L
\}\longrightarrow1.
\tag{4.5}
\]

#### Proof

We divide the proof into three elementary parts.

**Fixed trace words.**  Expand a normalized trace of a fixed word in
\(B_n,R_n\) and their transposes.  Wick's identity follows by differentiating
the Gaussian moment-generating function and says that an even Gaussian
moment is the sum over pairings of products of covariances; odd moments
vanish.  A nonzero pairing must match equal matrix colors.  Each pair
contributes \(n^{-1}\), and the covariance identifies its two row/column
indices, with the orientation determined by the transpose marker.

Draw the trace as an oriented polygon whose sides are the matrix
occurrences and glue paired equal-colored sides with the covariance
orientation.  If the word has \(2q\) random entries and the quotient has
\(v\) free indices, its contribution is \(n^{v-q-1}\).  Cutting one paired
edge at a time shows \(v\le q+1\).  Equality is possible exactly for the
noncrossing, orientation-compatible pairings: a crossing or a twisted
identification loses at least one free index.  These equality pairings are
also exactly the vacuum contractions obtained by successively applying the
appropriate annihilation parts: \(\ell_2^*,\ell_4^*\) for \(b,r\), and
\(\ell_1^*,\ell_3^*\) for \(b^*,r^*\).  Hence

\[
\frac1n\operatorname {Tr}W(B_n,R_n)
\xrightarrow{L^2}
\langle\Omega,W(b,r)\Omega\rangle.
\tag{4.6}
\]

For completeness, the variance is the same pairing count with two trace
polygons.  Pairings that do not join the polygons cancel against the square
of the mean.  A pairing that joins them has at most \(q+1\), rather than
\(q+2\), free indices after the two normalizations, and is \(O(n^{-1})\).
There are finitely many pairings at fixed word degree, so the variance tends
to zero.  This proves (4.6).  No degree is allowed to grow with \(n\).

**The Gaussian roots.**  Conditional on a matrix \(T_n\) independent of
\(g_n,h_n\sim N(0,n^{-1}I)\),

\[
\begin{aligned}
\mathbb E[g_n^{\mathsf T}T_ng_n\mid T_n]
 &=n^{-1}\operatorname {Tr}T_n,\\
\operatorname {Var}(g_n^{\mathsf T}T_ng_n\mid T_n)
 &\le 2n^{-1}\|T_n\|^2,\\
\mathbb E[|g_n^{\mathsf T}T_nh_n|^2\mid T_n]
 &\le n^{-1}\|T_n\|^2.
\end{aligned}
\tag{4.7}
\]

The first two formulas use the symmetric part of \(T_n\); the bounds follow
from \(\|T_n\|_{\mathrm{HS}}^2\le n\|T_n\|^2\).  Take
\(T_n=P_i^{\mathsf T}P_j\) and use the norm bound below.  Equations
(4.6)--(4.7) give (4.4), including the zero cross-root limit.

**Uniform norm bounds.**  A \(1/4\)-net of the unit sphere in
\(\mathbb R^n\) can be chosen with at most \(9^n\) points.  For every matrix
\(G\),

\[
\|G\|\le2\max_{u,v\text{ in the net}}|u^{\mathsf T}Gv|.
\tag{4.8}
\]

For normalized Gaussian \(G\), each fixed bilinear form in (4.8) is
\(N(0,n^{-1})\).  A union bound gives

\[
\mathbb P\{\|G\|>12\}
\le2\,81^n e^{-18n}\longrightarrow0.
\tag{4.9}
\]

Finally, \(\|g_n\|^2=n^{-1}\sum_{i=1}^nZ_i^2\to1\) in \(L^2\), because its
variance is \(2/n\).  Apply these estimates to the four independent
objects.  This proves (4.5) and the lemma.  \(\square\)

The polygon language in the first part is only bookkeeping for the explicit
index equalities.  Its two needed inequalities can equivalently be proved by
induction: removing an adjacent covariance pair changes both the number of
pairs and the number of free indices by one; if no adjacent removable pair
exists, the identification loses a free index.  For two polygons, a joining
pair first merges the components and causes the same one-index loss.

## 5. Construction and well-posedness of the IDE

On

\[
\mathscr H_\infty=\mathbb C\oplus\mathcal F^{\oplus3}
\tag{5.1}
\]

define

\[
\mathcal C_0=
\begin{pmatrix}
0&0&0&\langle\xi_a,\cdot\rangle\\
|\xi_x\rangle&0&0&0\\
0&b&0&0\\
0&0&r&0
\end{pmatrix}.
\tag{5.2}
\]

Since each creation or annihilation operator has norm one,
\(\|\mathcal C_0\|\le2\).  As at finite width,

\[
\operatorname {rank}\mathcal C_0^3\le4,
\qquad
\frac14\operatorname {Tr}\mathcal C_0^4=0,
\qquad
\operatorname {Tr}[\mathcal C_0^3(\mathcal C_0^*)^3]=4.
\tag{5.3}
\]

The first trace is zero by the orthogonality of the two root sectors.  In
the last trace, each of the four cyclic parameter blocks contributes one.

Let \(\mathfrak S_1(\mathscr H_\infty)\) be the trace-class ideal.  For
\(Q\in\mathfrak S_1\), put \(\mathcal C=\mathcal C_0+Q\).  The right-hand
side of (1.3) is trace class: \(\mathcal C_0^{*3}\) is finite rank and every
other term in the cubic expansion contains \(Q^*\).  On a trace-norm ball,

\[
\|A^3-B^3\|_1
\le
(\|A\|^2+\|A\|\|B\|+\|B\|^2)\|A-B\|_1.
\tag{5.4}
\]

This follows from the noncommutative telescoping identity and
\(\|UVW\|_1\le\|U\|\|V\|_1\|W\|\).  The functional

\[
K(Q)=\|\mathcal C^{*3}\|_{\mathrm{HS}}^2
\tag{5.5}
\]

is locally Lipschitz there because

\[
|\|U\|_{\mathrm{HS}}^2-\|V\|_{\mathrm{HS}}^2|
\le(\|U\|_{\mathrm{HS}}+\|V\|_{\mathrm{HS}})
\|U-V\|_{\mathrm{HS}}
\tag{5.6}
\]

and \(\|T\|_{\mathrm{HS}}\le\|T\|_1\).  Thus Picard iteration gives a
unique local solution of (1.3).  The block-cyclic subspace is invariant, so
\(\operatorname {rank}\mathcal C^3\le4\) along the solution.

Ordinary trace cyclicity is legitimate below because \(\mathcal C^3\) is
finite rank and \(\dot Q\) is trace class.  Differentiating gives

\[
\frac d{dt}\frac14\operatorname {Tr}\mathcal C^4
=2\eta e\operatorname {Tr}
[\mathcal C^3(\mathcal C^*)^3]
=2\eta eK.
\tag{5.7}
\]

Together with \(\dot e=-2\eta eK\) and (5.3), this proves (1.4).  Moreover,

\[
\frac d{dt}e^2=-4\eta e^2K,
\qquad
\int_0^T e(t)^2K(t)\,dt\le\frac{y^2}{4\eta}.
\tag{5.8}
\]

Since a rank-four operator has trace norm at most twice its
Hilbert--Schmidt norm,

\[
\begin{aligned}
\|Q(T)\|_1
&\le4\eta\int_0^T|e|\sqrt K\,dt\\
&\le4\eta\sqrt T
\left(\int_0^Te^2K\,dt\right)^{1/2}
\le2|y|\sqrt{\eta T}.
\end{aligned}
\tag{5.9}
\]

Thus no finite-time trace-norm escape is possible.  Local existence extends
globally, uniqueness gives restartability, and (1.3)--(1.4) are proved.

## 6. Identification of the width limit

Let \(\mathcal C_{0,n}\) be (2.2) at Gaussian initialization and write

\[
\mathcal C_n(t)=\mathcal C_{0,n}+Q_n(t).
\tag{6.1}
\]

The finite physical flow is exactly

\[
\dot Q_n=2\eta e_n(\mathcal C_{0,n}^{\mathsf T}+Q_n^{\mathsf T})^3,
\qquad
e_n=y-\frac14\operatorname {Tr}
(\mathcal C_{0,n}+Q_n)^4.
\tag{6.2}
\]

Lemma 3 gives \(f_n(0)\to0\), \(K_n(0)\to4\), convergence of every fixed
rooted source Gram matrix, and a deterministic high-probability bound on
\(\|\mathcal C_{0,n}\|\).

We now prove compact-time convergence rather than infer it from finite jets.
On the event \(|f_n(0)|\le1\), the finite analogue of (5.9) gives

\[
\sup_{t\le T}\|Q_n(t)\|_1
\le2(|y|+1)\sqrt{\eta T}.
\tag{6.3}
\]

Together with the source-norm bound, this places the finite and limiting
solutions in one deterministic operator/trace-norm ball with probability
tending to one.  Multiply both vector fields by a Lipschitz cutoff which is
one on that ball and zero outside a slightly larger ball.  Explicitly, use
the product norm
\[
\|(Q,e)\|_{\mathcal X}=\|Q\|_1+|e|
\tag{6.3a}
\]
and multiply by
\(\chi(\|(Q,e)\|_{\mathcal X})\), where \(\chi=1\) on the common ball,
\(\chi=0\) outside its radius plus one, and \(\operatorname {Lip}\chi\le2\).
Equations
(5.4)--(5.6) give a common bound \(M_T\) and a common Lipschitz constant
\(H_T\), independent of dimension.

Consider Picard iteration for the cutoff equations.  At every fixed Picard
depth \(m\),

\[
Q_n^{[m]}(t)=
\sum_{\alpha,\beta=1}^{N_m}
c_{\alpha\beta,n}^{[m]}(t)
|w_{\alpha,n}\rangle\langle w_{\beta,n}|,
\tag{6.4}
\]

where \(N_m<\infty\) is independent of \(n,t\), and each \(w_{\alpha,n}\)
is a fixed word in \(B_n(0),R_n(0)\) and their transposes applied to one of
the two endpoint roots.

This representation follows by induction.  It holds at the first Picard
step because \(\mathcal C_{0,n}^{\mathsf T\,3}\) has four rank-one blocks.
In the cubic at the next step, multiplying a rank-one map by a source matrix
appends one letter to a rooted word; multiplying two rank-one maps contracts
two adjacent roots to one Gram entry.  A trace readout contracts the last
two roots.  Time integration changes only scalar coefficients.  Thus the
word list remains finite at each fixed \(m\), and every coefficient is a
continuous function of one finite rooted Gram matrix.

Lemma 3 therefore implies, for each fixed \(m\), uniform convergence on
\([0,T]\) of all coefficients and trace readouts in (6.4).  Trace-norm
convergence does not require an identification of the ambient spaces.  If

\[
A=\sum_{i,j}c_{ij}|u_i\rangle\langle v_j|,
\tag{6.5}
\]

then its nonzero singular values are those of
\(G_u^{1/2}CG_v^{1/2}\) after quotienting the null spaces, where
\((G_u)_{ij}=\langle u_i,u_j\rangle\) and similarly for \(G_v\).
Hence \(\|A\|_1\) is a continuous function of the two finite Gram matrices
and the coefficient matrix.

For a bounded \(H_T\)-Lipschitz vector field, successive approximation gives

\[
\sup_{t\le T}\|z(t)-z^{[m]}(t)\|
\le
M_TT e^{H_TT}\frac{(H_TT)^m}{(m+1)!},
\tag{6.6}
\]

Indeed, the \(j\)-th Picard increment is bounded by
\(M_TH_T^{j-1}t^j/j!\), and summing the tail proves (6.6).  The bound is
dimension-free.

Choose \(m\) so that (6.6) is small, then take \(n\to\infty\), and finally
let \(m\to\infty\).  The cutoff is inactive by (5.9) and (6.3).
For the readouts, telescoping gives on the common ball

\[
\left|\operatorname {Tr}\mathcal C^4-
\operatorname {Tr}\widetilde{\mathcal C}^{\,4}\right|
\le4\max(\|\mathcal C\|,\|\widetilde{\mathcal C}\|)^3
\|\mathcal C-\widetilde{\mathcal C}\|_1,
\tag{6.7}
\]

and (5.6) gives the analogous bound for \(K\).  We obtain

\[
\sup_{t\le T}
\bigl(|f_n(t)-f(t)|+|K_n(t)-K(t)|+|e_n(t)^2-e(t)^2|\bigr)
\xrightarrow{\mathbb P}0.
\tag{6.8}
\]

The same finite-word/Picard argument applies after adjoining any fixed
finite family of current rooted-word contractions.  This is the announced
action-state identification.

## 7. The simultaneous exact-GD limit

At the mesh points, simultaneous exact GD is exactly explicit Euler for the
single cyclic equation:

\[
Q_{n,k+1}
=Q_{n,k}
+2\eta\delta_n e_{n,k}
(\mathcal C_{0,n}^{\mathsf T}+Q_{n,k}^{\mathsf T})^3,
\quad
e_{n,k}=y-\frac14\operatorname {Tr}
(\mathcal C_{0,n}+Q_{n,k})^4.
\tag{7.1}
\]

No Taylor approximation was used in (7.1); it is just the four simultaneous
parameter updates packaged by (2.2).

Use the same cutoff as in Section 6.  If a vector field is bounded by \(M_T\)
and Lipschitz with constant \(H_T\), its exact solution obeys

\[
\|z(t+\delta)-z(t)-\delta V(z(t))\|
\le\frac12H_TM_T\delta^2.
\tag{7.2}
\]

Subtracting Euler from the exact solution, applying (7.2), and iterating
\(E_{k+1}\le(1+H_T\delta)E_k+\frac12H_TM_T\delta^2\) gives

\[
\max_{k\delta\le T}\|z_k-z(k\delta)\|
\le\frac12M_T(e^{H_TT}-1)\delta.
\tag{7.3}
\]

Linear interpolation adds at most \(2M_T\delta\).  These bounds are
dimension-free.  For small enough \(\delta\), the cutoff Euler path remains
inside the region where the cutoff is one, so it is the actual GD path.

Apply (7.3) with \(\delta=\delta_n\), then combine it with (6.8) and the
readout Lipschitz bounds (5.6), (6.7).  This proves (1.5) for every
\(\delta_n\to0\), with no further width/mesh relation.

## 8. The equivalent free-Wishart IDE

The cyclic IDE is already a scalar-kernel equation after an orthonormal
basis of Fock space is chosen.  A central reduction gives a smaller spatial
source and makes the noncommutativity explicit.

At finite width put

\[
z=Bx,\qquad p=R^{\mathsf T}a,\qquad
L=BB^{\mathsf T}+\|x\|^2I,\qquad
M=R^{\mathsf T}R+\|a\|^2I.
\tag{8.1}
\]

Substitution of (2.1) gives exactly

\[
\begin{aligned}
z'&=Lp,&p'&=Mz,\\
L'&=zp^{\mathsf T}+pz^{\mathsf T}
+2\langle z,p\rangle I,
&M'&=zp^{\mathsf T}+pz^{\mathsf T}
+2\langle z,p\rangle I,
\end{aligned}
\tag{8.2}
\]

and

\[
f=\langle z,p\rangle,
\qquad
K=\langle p,Lp\rangle+\langle z,Mz\rangle.
\tag{8.3}
\]

Let \(X,Y\) be freely independent Marchenko--Pastur elements of parameter
one, represented by left multiplication on the reduced free-product GNS
space \(\mathcal G=L^2(\mathcal A,\tau)\).  Use two orthogonal root copies
\(\mathcal H=\mathcal G\oplus\mathcal G\) and initialize

\[
z_0=(X^{1/2}\Omega,0),
\qquad
p_0=(0,Y^{1/2}\Omega).
\tag{8.4}
\]

The identities

\[
\begin{aligned}
\langle z_0,P(X,Y)z_0\rangle&=\tau(P(X,Y)X),\\
\langle p_0,P(X,Y)p_0\rangle&=\tau(P(X,Y)Y),\\
\langle z_0,P(X,Y)p_0\rangle&=0
\end{aligned}
\tag{8.5}
\]

are the central form of Lemma 3.  Write

\[
L=I+X+hI+S,
\qquad
M=I+Y+hI+S.
\tag{8.6}
\]

Then feature time closes as

\[
\begin{aligned}
z'&=(I+X+hI+S)p,\\
p'&=(I+Y+hI+S)z,\\
h'&=2\langle z,p\rangle,\\
S'&=|z\rangle\langle p|+|p\rangle\langle z|,
\end{aligned}
\qquad h(0)=0,\quad S(0)=0,
\tag{8.7}
\]

with \(S(t)\) self-adjoint trace class.  Multiplying the four right-hand
sides by \(2\eta e\) and adding

\[
\dot e=-2\eta eK
\tag{8.8}
\]

gives the physical-time IDE.  Equations (8.3), (8.6) are its current-state
readouts.

To see positivity without assuming it, lift (8.7) to four factors by taking
\(x_0=(\Omega,0)\), \(a_0=(0,\Omega)\),
\(B_0=X^{1/2}\), and \(R_0=Y^{1/2}\), and evolve (2.1) on
\(\mathcal H\).  Its reduced variables solve (8.7), so uniqueness identifies
the lift.  Therefore

\[
L=BB^*+\|x\|^2I\ge(1+h)I,
\qquad
M=R^*R+\|a\|^2I\ge(1+h)I.
\tag{8.9}
\]

Both endpoint squared norms start at one and have feature derivative
\(2f\), hence equal \(1+h\).

Choose any fixed orthonormal basis of the free-product word space.  The
vectors \(z,p\) become two scalar fields \(Z(w),P(w)\), the trace-class
operator becomes one scalar kernel \(S(w,w')\), and the fixed operators
\(X,Y\) become fixed sparse integral kernels.  Thus (8.7) is literally an
IDE on a fixed countable spatial domain.  The domain and number of fields do
not grow with width, time, or expansion order.

If \(y\ne0\), the limiting loss tends to zero.  Indeed \(e\) retains the sign
of \(y\), \(f=y-e\) has the same sign, and \(h\ge0\).  By (8.9),

\[
K\ge(1+h)(\|z\|^2+\|p\|^2)\ge2|f|.
\tag{8.10}
\]

Since \(\dot f(0)=2\eta yK(0)=8\eta y\), \(|f|\) is positive immediately.
After any such time, (8.10) compares \(|f|\) with the logistic equation and
forces \(f(t)\to y\), hence \(e(t)^2\to0\).  For \(y=0\), the state is
stationary.

## 9. Exact compression boundary

Three elementary tests show why ordinary spectra are insufficient.

First, if \(X,Y\) are free MP(1) variables, freeness and
\(\tau(X)=\tau(Y)=1\), \(\tau(X^2)=\tau(Y^2)=2\) give

\[
\tau(X^2Y^2)=4,
\qquad
\tau(XYXY)=3,
\qquad
\tau([X,Y]^*[X,Y])=2.
\tag{9.1}
\]

For commuting classically independent variables with the same marginals,
both ordered fourth moments would be four.

Second, at width one the states

\[
(a,R,B,x)=(1,1,1,1),
\qquad
(a,R,B,x)=(2,1,1,\tfrac12)
\tag{9.2}
\]

have the same cyclic characteristic polynomial \(\lambda^4-1\), but (2.6)
gives kernels \(4\) and \(25/4\).

Third, let \(a=x=e_1\), \(R=\operatorname {diag}(1,2,3)\), and rotate \(B\)
through the same nonzero angle \(\theta\) either in the \(1\)-\(2\) plane or
in the \(1\)-\(3\) plane.  All separate Gram spectra and the output
\(\cos\theta\) agree, while

\[
K_{12}=3+\cos^2\theta+4\sin^2\theta,
\qquad
K_{13}=3+\cos^2\theta+9\sin^2\theta.
\tag{9.3}
\]

These examples rule out the named spectral summaries even for the
instantaneous vector field.  They are not substitutes for Theorem 1(1),
whose exact state-universal graph hypotheses are needed.

The broad sentence “no \(O(1)\)-scalar PDE exists” would be false.  System
(8.7) is already a fixed finite list of scalar **fields**.  It evades the
no-go because the word coordinate \(w\) carries infinitely many numerical
degrees of freedom.  At fixed \(n=1\), a finite polynomial closure also
exists: with

\[
A=a^2,\quad U=R^2,\quad V=B^2,\quad X=x^2,
\tag{9.4}
\]

feature time satisfies

\[
A'=U'=V'=X'=2f,
\qquad
f'=UVX+AVX+AUX+AUV.
\tag{9.5}
\]

Thus width-uniformity is also indispensable.

## 10. Audit of the original external invocation

The superseded manuscript cited Yanjin Xiang and Zhihua Zhang,
[“Strong Convergence for a General Class of Random Matrix
Models,” Theorem 3.3](https://arxiv.org/html/2608.04824v1#S3).
The exact theorem assumes a fixed number of mutually independent iid entry
arrays, centered entries with fixed variance and finite fourth moment, and
\(n^{-1/2}\) normalization.  It concludes joint almost-sure convergence of
every fixed \(*\)-polynomial in normalized trace and operator norm to a free
circular family, including real entries and fixed matrix coefficients.

The invocation is valid: here there are two colors, the unnormalized entries
are independent \(N(0,1)\), real pseudo-variance is explicitly allowed, and
only fixed words are used.  The nested-corner coupling in that theorem is
needed only for its almost-sure formulation; the present convergence in
probability depends only on the finite-\(n\) laws.

The theorem's proof was checked against its operative primary inputs:

- Brailovskaya--van Handel,
  [“Universality and sharp matrix concentration
  inequalities”](https://arxiv.org/html/2201.05142v3), Theorems 2.6 and
  2.9, Proposition 9.18, and Lemma 9.20;
- Anderson,
  [“Convergence of the largest singular value of a polynomial in
  independent Wigner matrices”](https://arxiv.org/abs/1103.4825v3),
  Theorems 1--2 and Corollary 1;
- the Bai--Yin finite-fourth-moment operator-norm bound used for fixed-level
  tail removal.

The dimensions, bounded-summand parameter, variance parameter, weak
variance parameter, fixed amplification, independence, fourth moments, and
real/imaginary-coordinate hypotheses match in every use.  A possible
text-extraction ambiguity is worth recording: Brailovskaya--van Handel
Lemma 9.20 is a **two-sided absolute-deviation** bound for the even-moment
root.  Its absolute-value bars can disappear in some PDF text extraction.
With \(t=4\log(qn)\), its error is \(o(1)\) and its failure probabilities
are summable, so the lower tail is controlled as well as the upper tail.

Nevertheless, the proof of Theorem 1 above does not use this recent
research theorem or any of its dependencies.  Lemma 3 supplies exactly the
weaker Gaussian facts required by the Picard bridge, directly from Wick
pairing, conditional Gaussian concentration, and a finite net.

## 11. Logical verdict

The recovered positive result survives correction and strengthens to the
joint exact-GD diagonal (1.5).  The recovered negative result also survives,
but only in the precise form of Theorem 1(1).  It is not an impossibility
theorem for every PDE, every finite family of continuum fields, or the
single Gaussian-initialized orbit.

The complete relationship is therefore:

\[
\boxed{\text{no finite state-universal contraction-moment ODE}}
\quad\text{but}\quad
\boxed{\text{one fixed noncommutative source plus one current kernel IDE}.}
\tag{11.1}
\]

This is the sharp resolution rather than a contradiction: the IDE is the
Markovian compression of the infinite ordered-word hierarchy that defeats
finite scalar moment lists.
