# Abstract moment and analytic-rank route

Status: frozen independent attempt, 2026-09-19. This document uses only the neutral prompt and the required mathematical skills. It does not use repository scientific sources, other attempts, or experiments. Its conclusions are internally derived, not independently reviewed.

The full assertion that every local minimum has zero loss remains **open in this attempt**. What is proved below is an exact reduction of the lower population layer to locally free finite moments, exact interpolation, and an analytic characterization of where any positive-loss local minimum must occur. The unresolved step is specifically the exclusion of singular local minima of the upper factorization. A general example shows why density of interpolation points cannot supply that step.

## 1. Fixed contract

Write \(s_i=x_i/\sqrt d\), with \(\|s_i\|=1\), and assume \(s_i\ne\pm s_j\) for \(i\ne j\). There are finitely many samples, with arbitrary sample count \(n\), positive weights \(\mu_i\), and real labels \(y_i\). The two probability carriers are fixed and nonatomic. The fixed marks \(b_1\in\mathbb R^k\), \(b_2\in\mathbb R^\ell\) are bounded and may have linear redundancies. Trainable parameters are

\[
w\in L^2(\Omega_1;\mathbb R^d),\qquad
c\in L^2(\Omega_2),\qquad M\in\mathbb R^{\ell\times k}.
\]

The moments, features, outputs, and loss are

\[
a_i(w)=\mathbb E[b_1\tanh(w\cdot s_i)],\quad
h_i(A,M)=\tanh(b_2^TMa_i),\quad
f_i=\langle c,h_i\rangle_{L^2},\quad
L=\sum_i\mu_i(f_i-y_i)^2,
\]

where \(A=[a_1\ \cdots\ a_n]\). Locality is in the physical product norm \(L^2\times L^2\times\) Frobenius. No extra width, varying marks, distributional optimization, or change of topology is permitted. No parity condition is imposed. Signed-compatible duplicate/antipodal groups can first be combined with their weights; this reduces to the displayed input assumption.

The lower conclusions below need bounded \(b_1\) and nonatomicity; the retained Gaussian lower coordinates are not needed. For interpolation and generic upper rank, the upper mark list must contain one coordinate \(g\) whose essential range contains an interval, as is true of a continuously distributed \(\tanh\)-Gaussian coordinate. No independence from any other upper mark is needed.

## 2. Exact lower moment geometry

Let \(B\subseteq\mathbb R^k\) be the linear span of the essential range of \(b_1\), and set

\[
\mathcal C=\{A(w):w\in L^2(\Omega_1;\mathbb R^d)\}\subseteq B^n.
\]

**Proposition.** The set \(\mathcal C\) is convex, has affine hull \(B^n\), and every one of its points is an interior point relative to \(B^n\). More precisely, for every \(w_0\) there are \(\rho,C>0\) such that every \(A\in B^n\) with \(\|A-A(w_0)\|_F<\rho\) has a realization \(w_A\) satisfying

\[
A(w_A)=A,\qquad
\|w_A-w_0\|_{L^2}\le C\|A-A(w_0)\|_F^{1/2}.
\]

This is a local existence statement, not a claim of a continuous or differentiable choice of \(w_A\).

### 2.1 Exact mixing on a nonatomic carrier

We use this finite-dimensional form of Lyapunov's convexity theorem: if \(D:\Omega\to\mathbb R^m\) is integrable on a nonatomic finite measure space, then \(\{\int_E D:E\text{ measurable}\}\) is compact and convex. Since this set contains \(0\) and \(\int_\Omega D\), for every \(t\in[0,1]\) it contains \(t\int_\Omega D\).

For two \(L^2\) controls \(u,v\), apply this theorem to the vector consisting of the entries of

\[
b_1\big(\tanh(u\cdot s_i)-\tanh(v\cdot s_i)\big),\quad i=1,\ldots,n,
\]

and, if desired, the additional scalar

\[
\|u-w_0\|^2-\|v-w_0\|^2.
\]

These functions are integrable: the marks and \(\tanh\) are bounded, and the controls have finite second moment. Select the resulting measurable set \(E\) and put \(\widetilde w=u\) on \(E\), \(v\) off \(E\). This produces exactly

\[
A(\widetilde w)=tA(u)+(1-t)A(v),
\]

and exactly the same convex combination of squared distances from \(w_0\). The switched control remains \(L^2\). Iterating this construction gives any finite convex combination, with its prescribed average squared distance. This proves convexity without requiring independent spare randomness on the carrier.

### 2.2 A finite ridge vector never maximizes a nonzero linear functional

Set \(H(v)=(\tanh(v\cdot s_i))_{i=1}^n\). We first prove

\[
q\ne0\quad\Longrightarrow\quad
q\cdot H(v)<\sup_{u\in\mathbb R^d}q\cdot H(u)
\qquad\text{for every finite }v.
\tag{1}
\]

Here is an explicit isotropic smoothing representation, including the positivity needed for strictness. Use the classical product identity

\[
\cosh t=\prod_{m=0}^{\infty}\left(1+\frac{t^2}{a_m^2}\right),
\qquad a_m=(m+\tfrac12)\pi.
\]

The product converges on compact sets because \(\sum_m a_m^{-2}<\infty\). Take independent gamma variables \(X_m\) with shape \(2\) and scale \(a_m^{-2}\), and put \(T=\sum_mX_m\). Since \(\sum_m\mathbb E X_m<\infty\), one has \(0<T<\infty\) almost surely. Their Laplace transforms give

\[
\mathbb E e^{-Tt^2}=\prod_m(1+t^2/a_m^2)^{-2}=\operatorname{sech}^2t.
\]

Tonelli's theorem, applied to nonnegative integrands, gives

\[
\mathbb E\frac{\sqrt\pi}{2\sqrt T}
=\int_0^\infty\mathbb E e^{-Tu^2}\,du
=\int_0^\infty\operatorname{sech}^2u\,du=1.
\]

Tilt the distribution of \(T\) by the positive density \(\sqrt\pi/(2\sqrt T)\); call the resulting variable \(\widetilde T\). Integration of the preceding Laplace identity gives, for every real \(t\),

\[
\tanh t=\mathbb E\operatorname{erf}(\sqrt{\widetilde T}\,t).
\]

If \(G\) is an independent standard Gaussian in \(\mathbb R^d\) and \(Z=G/\sqrt{2\widetilde T}\), this says

\[
\tanh(v\cdot s_i)=\mathbb E\operatorname{sign}((v+Z)\cdot s_i).
\tag{2}
\]

The unit norm assumption makes the same isotropic \(Z\) work for every \(i\). The law of \(Z\) assigns positive mass to every nonempty open set, because each conditional Gaussian does.

Consider the finite set of sign vectors

\[
S=\{(\operatorname{sign}(u\cdot s_i))_i:
u\cdot s_i\ne0\text{ for every }i\}.
\]

Its span is \(\mathbb R^n\). Indeed, if \(\sum_iq_i\operatorname{sign}(u\cdot s_i)=0\) on every chamber, cross the hyperplane \(s_i^\perp\) at a point lying on no other sample hyperplane. Only the \(i\)-th sign changes, so \(q_i=0\). Such a point exists because the finitely many hyperplanes are distinct. In \(d=1\), the input assumption permits at most one sample, and the assertion is immediate. Also \(S=-S\), so its convex hull \(P\) is full-dimensional.

Equation (2) expresses \(H(v)\) as a convex combination assigning positive weight to every vector in \(S\), because each sign chamber is nonempty and open. Thus \(H(v)\in\operatorname{int}P\). Moreover, \(H(Ru)\) tends to the sign vector of \(u\) as \(R\to\infty\). Therefore

\[
\sup_u q\cdot H(u)=\max_{s\in S}q\cdot s,
\]

and strict interior membership proves (1).

### 2.3 Full affine hull and absence of boundary points

Suppose a linear functional \(Q\in B^n\) vanishes on all attainable moments. The zero control realizes the zero matrix. Switching from zero to a fixed vector \(v\) on an arbitrary measurable set shows

\[
(Q^Tb_1(\omega))\cdot H(v)=0\quad\text{almost everywhere}.
\]

First take the countable set of rational \(v\), then use continuity in \(v\). Since \(H(v)\) spans \(\mathbb R^n\), this implies \(Q^Tb_1=0\) almost everywhere. The definition of \(B\) then gives \(Q=0\). Hence the affine hull of \(\mathcal C\) is \(B^n\).

If \(A(w_0)\) were on the relative boundary of \(\overline{\mathcal C}\), the finite-dimensional supporting-hyperplane theorem would give a nonzero \(Q\in B^n\) with

\[
\langle Q,A(w)\rangle_F\le\langle Q,A(w_0)\rangle_F
\quad\text{for every }w.
\]

Set \(q(\omega)=Q^Tb_1(\omega)\). This is nonzero on a set of positive measure. On that set, (1) shows that the finite value \(w_0(\omega)\) is not a maximizer of \(q(\omega)\cdot H(v)\). By continuity, some rational vector gives a strict improvement at each such point. Countability implies that one rational vector gives a strict improvement on a measurable set of positive measure. Replacing \(w_0\) by this fixed vector on that set is an admissible \(L^2\) control and strictly increases the supporting functional, a contradiction.

Thus \(A(w_0)\in\operatorname{int}_{B^n}\overline{\mathcal C}\). For a finite-dimensional convex set with full affine hull, its interior equals the interior of its closure, so this point is interior to \(\mathcal C\) itself. One way to verify the last fact is to approximate the vertices of a small simplex in the closure by points of the convex set: their convex hull still contains a neighborhood of the original interior point.

### 2.4 Quantitative local lifting

Choose finitely many controls \(w_j\) whose moment matrices form a polytope containing a relative ball of radius \(\rho>0\) around \(A_0=A(w_0)\). Let \(K=\max_j\|w_j-w_0\|_{L^2}^2\). For \(\delta=\|A-A_0\|_F<\rho\), write

\[
A=(1-t)A_0+tA_*,\qquad t=\delta/\rho,
\]

where \(A_*\) lies in that polytope. Finite exact mixing realizes \(A_*\) with a control \(u\) satisfying \(\|u-w_0\|_{L^2}^2\le K\). Mixing \(u\) with \(w_0\), including squared distance in the finite vector measure, realizes \(A\) with

\[
\|w_A-w_0\|_{L^2}^2\le tK=(K/\rho)\delta.
\]

This completes the proposition.

## 3. Consequence: an exact local-minimum reduction

The original point \((w_0,M_0,c_0)\) is a local minimum if and only if \((A(w_0),M_0,c_0)\) is a local minimum of the reduced loss, with \(A\) free in the open subset \(\mathcal C\subset B^n\).

For the forward direction, any sufficiently small reduced perturbation lifts to a sufficiently small physical perturbation by the preceding proposition. For the reverse direction, use continuity of the moment map; explicitly, with \(\|b_1\|\le K_1\) almost surely,

\[
\|A(w)-A(w_0)\|_F\le K_1\sqrt n\,\|w-w_0\|_{L^2},
\]

because \(\tanh\) is 1-Lipschitz and the input directions are unit vectors. The other parameter maps are continuous as well. Directions of \(M\) orthogonal to \(B\) are redundant and do not change this equivalence.

This reduction preserves the fixed finite mark spaces, the finite matrix factorization, and the physical topology. It does not replace the model by an unrestricted two-layer network.

## 4. Interpolation and generic upper rank without a density assumption

Assume \(B\ne\{0\}\), which follows from retention of the lower constant feature. Since \(\mathcal C\) is open, choose an attainable \(A\) with every column nonzero and \(a_i\ne\pm a_j\). The excluded conditions are finitely many proper linear subspaces of \(B^n\).

There is \(v\in B\) such that \(\alpha_i=v\cdot a_i\) are all nonzero and their absolute values are pairwise distinct: avoid the finitely many hyperplanes orthogonal to \(a_i\) and \(a_i\pm a_j\). Let \(e_g\) pick a retained upper mark \(g\) with interval essential range, and set \(M=e_gv^T\). Then

\[
h_i=\tanh(\alpha_i g).
\]

These functions are linearly independent in \(L^2(\Omega_2)\). To see this, an almost-sure identity \(\sum_i\beta_i\tanh(\alpha_i g)=0\) gives an analytic identity on an interval, hence on the real line. The Taylor coefficients of \(\tanh t\) at its odd powers are all nonzero: the coefficients of \(\tan t\) are strictly positive by the recurrence from \((\tan t)'=1+(\tan t)^2\), and \(\tanh t=-i\tan(it)\). Comparing the first \(n\) odd coefficients gives

\[
\sum_i\beta_i\alpha_i(\alpha_i^2)^m=0,
\qquad m=0,\ldots,n-1.
\]

The Vandermonde matrix in the distinct \(\alpha_i^2\) is invertible, so every \(\beta_i=0\).

Consequently the Gram matrix \(G_{ij}=\langle h_i,h_j\rangle\) is positive definite, and

\[
c=\sum_j(G^{-1}y)_j h_j
\]

interpolates every label vector exactly. This \(c\) is a finite linear combination of bounded functions and therefore lies in \(L^2\). This proves attainability of zero loss for every finite sample count without requiring joint upper density or independence of the extra marks.

For each fixed separated \(A\), the function

\[
D_A(M)=\det\big(\mathbb E[h_i(A,M)h_j(A,M)]\big)
\]

is real analytic in the entries of \(M\). Bounded marks give, near every real matrix, a common complex neighborhood avoiding the poles of \(\tanh\), which justifies integration of the analytic power series. The preceding rank-one matrix is a point with \(D_A(M)>0\). A nonzero real analytic function on connected Euclidean space cannot vanish on an open set. Therefore full Gram rank is open and dense in \(M\) for this fixed \(A\). Perturbing \(A\) first to a separated matrix proves that full Gram rank is also dense in the entire reduced feasible parameter space.

At any local minimum, differentiation in the unrestricted \(c\) direction gives the exact identity

\[
\sum_i\mu_i(f_i-y_i)h_i=0\quad\text{in }L^2(\Omega_2).
\tag{3}
\]

Hence a local minimum with full Gram rank has zero loss. Every hypothetical positive-loss local minimum must belong to the Gram-rank discriminant \(D=0\), which has empty interior. This localization is exact but does not exclude such a minimum.

## 5. Why arbitrary correlations obstruct a simpler independence argument

Even retaining a continuous Gaussian coordinate and the constant does not make distinct upper linear forms automatically independent after \(\tanh\). For instance, let \(g=\tanh G\), choose \(0<\lambda<1\), and retain the bounded smooth extra mark

\[
q(g)=\operatorname{arctanh}(\lambda\tanh g).
\]

With \(b_2=(1,g,q(g))\), the two distinct linear forms \(z_1=g\), \(z_2=q(g)\) satisfy

\[
\tanh z_2=\lambda\tanh z_1
\]

identically, although they are neither equal nor negatives of each other. This example respects the bounded smooth correlated-mark allowance. It refutes a pointwise feature-independence lemma, not the no-bad-minimum conjecture.

Likewise, dense nearby full rank does not alone rule out a positive-loss local minimum when the linear output parameter is required to remain close. The following finite-dimensional analytic example isolates that logical issue:

\[
f_1=c_1,\qquad f_2=t^2c_1+t^3c_2,\qquad y=(1,-1).
\]

At \((t,c_1,c_2)=(0,1,0)\), the squared loss is \(1\). In a sufficiently small neighborhood, \(c_1+t c_2>0\), so \(f_2=t^2(c_1+t c_2)\ge0\). Therefore the loss is at least \(1\) throughout that neighborhood. Yet for every \(t\ne0\) the map from \((c_1,c_2)\) to the two outputs has full rank and can interpolate. The interpolating \(c_2\) diverges as \(t\to0\). This is not a counterexample to the stipulated tanh model; it decisively invalidates the proposed inference from dense rank to benign landscape by itself.

## 6. A necessary tangent condition and the remaining bottleneck

Let a reduced local minimum have residuals \(r_i=\mu_i(f_i-y_i)\), and write \(H=\operatorname{span}\{h_i\}\subset L^2(\Omega_2)\). For any sufficiently small \(q\in H^\perp\), replacing \(c\) by \(c+q\) leaves every output unchanged. The new point is itself a local minimum, since it has the same loss and lies inside a neighborhood witnessing minimality of the original point.

Differentiate the loss at all these nearby points. If \(r_i\ne0\), independent perturbations of the free moment column \(a_i\) imply

\[
(u^TM^Tb_2)\operatorname{sech}^2(b_2^TMa_i)\in H
\quad\text{for every }u\in B.
\tag{4}
\]

Indeed the corresponding derivative paired with every small \(q\in H^\perp\) is zero, and scalar multiplication extends this to all \(q\in H^\perp\). Finite-dimensional \(H\) is closed, giving membership. Matrix variations similarly imply, entry by entry,

\[
(b_2)_\alpha\sum_i r_i(a_i)_\beta
\operatorname{sech}^2(b_2^TMa_i)\in H.
\tag{5}
\]

All derivatives here are justified by bounded marks, finite matrices, and \(c,q\in L^2\subset L^1\) on a probability space. The exact residual identity (3) and tangent conditions (4)–(5) are considerably stronger than mere Gram singularity.

The remaining proof obligation is to show that (3)–(5), together with higher-order local minimality, force \(r=0\) under the allowed arbitrary smooth correlations; or to construct admissible marks and parameters satisfying the full local-minimum inequalities with \(r\ne0\). No argument in this report supplies that implication. In particular, one cannot infer closure of \(H\) under all higher parameter derivatives merely from (4), and one cannot assume that added retained features preserve a previously proved landscape theorem.

## 7. Claim ledger

| Claim | Status | Scope / dependency |
|---|---|---|
| Exact convex mixing of lower moments with prescribed squared-distance cost | Proved internally | Nonatomic carrier, bounded marks, finite sample count |
| Every finite lower control gives an interior moment matrix | Proved internally | Equal unit input norms, no duplicate/antipodal directions |
| Physical local minima are exactly reduced moment local minima | Proved internally | Local lifting plus moment continuity |
| Every finite label vector is attainable | Proved internally | One nontrivial lower mark direction; one continuous upper scalar mark |
| Full upper Gram rank is open and dense | Proved internally | Same upper scalar witness; analyticity |
| Positive-loss local minima must satisfy (3)–(5) on the rank discriminant | Proved internally | Original fixed-mark architecture |
| Distinct upper linear forms automatically give independent activations | Falsified | Explicit smooth correlated-mark identity above |
| Dense interpolation points exclude local minima at rank loss | Falsified as a general inference | Explicit analytic two-output example above |
| Every local minimum of the stated full model has zero loss | Open in this attempt | Singular upper-feature geometry remains decisive |

No parity restriction, full-dimensional upper density assumption, or special polynomial representation was used. No experiment was run. This frozen attempt is ready for comparison, with the open implication stated explicitly rather than absorbed into an analyticity claim.
