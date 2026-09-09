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
