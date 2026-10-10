# Non-affinity of finite spherical Gaussian-kernel expansions

This is an internally derived study lemma, not promoted book material. Its origin is a prompt-only scoped mathematical derivation: the supplied inputs were the spherical Gaussian covariance recursion, the activation assumptions, and the finite dataset assumptions below. No repository scientific sources or other studies were retrieved. The argument uses Gaussian Hermite expansions and an elementary tensor-feature projection; it does not invoke a spherical-harmonic strict-positive-definiteness theorem.

## Setup and conclusion

Let \(d\ge 2\), let \(S^{d-1}=\{v\in\mathbb R^d:\|v\|=1\}\), and let \(m\ge1\). Fix inputs \(v_1,\ldots,v_m\in S^{d-1}\) satisfying

\[
v_a\ne v_b\quad\text{and}\quad v_a\ne -v_b\qquad(a\ne b),
\]

and a nonzero label vector \(y=(y_1,\ldots,y_m)^\top\in\mathbb R^m\). Thus distinct inputs are nonparallel, equivalently \(|v_a\cdot v_b|<1\) for \(a\ne b\).

Consider \(L\ge1\) Gaussian covariance layers with positive initial variance \(q_0>0\):

\[
F_0(s)=q_0s,\qquad
q_\ell=F_\ell(1),\qquad -1\le s\le1,
\]

\[
F_\ell(s)=\mathbb E[\phi_\ell(Z)\phi_\ell(Z')],
\qquad
\begin{pmatrix}Z\\Z'\end{pmatrix}
\sim N\!\left(0,
\begin{pmatrix}
q_{\ell-1}&F_{\ell-1}(s)\\
F_{\ell-1}(s)&q_{\ell-1}
\end{pmatrix}\right).
\]

Each activation \(\phi_\ell:\mathbb R\to\mathbb R\) is non-affine and differentiable with globally bounded derivative. The requested real-analytic activation class satisfies these assumptions; analyticity is not needed for this lemma. Degenerate jointly Gaussian pairs at correlation \(\pm1\) are included in the definition.

Then the continuous function

\[
g(v)=\sum_{a=1}^m y_aF_L(v\cdot v_a),\qquad v\in S^{d-1},
\]

cannot equal \(\beta+w\cdot v\) on the sphere for any \(\beta\in\mathbb R\) and \(w\in\mathbb R^d\).

The proof first verifies a positive power-series property of the Gaussian recursion. It then removes the constant and linear components from each monomial kernel. Those residual kernels are positive semidefinite, and their finite Gram matrices approach the identity at high monomial degree. Unbounded positive coefficient support therefore prevents every nonzero finite kernel-section sum from being affine.

## Gaussian recursion and the positive power series

For a standard Gaussian scalar \(G\), use the normalized probabilists' Hermite convention

\[
\operatorname{He}_n(x)=(-1)^n e^{x^2/2}
\frac{d^n}{dx^n}e^{-x^2/2},\qquad
H_n(x)=\frac{\operatorname{He}_n(x)}{\sqrt{n!}},\qquad n\ge0.
\]

The precise Hermite facts used here are that \((H_n)_{n\ge0}\) is a complete orthonormal basis of \(L^2(N(0,1))\), and that jointly standard Gaussian \(G,G'\) of correlation \(r\in[-1,1]\) satisfy

\[
\mathbb E[H_n(G)H_k(G')]=\mathbf1_{\{n=k\}}r^n.
\]

For \(|r|<1\), the latter identity follows by comparing coefficients in

\[
\mathbb E\!\left[e^{tG-t^2/2}e^{uG'-u^2/2}\right]=e^{rtu},
\qquad
e^{tx-t^2/2}=\sum_{n=0}^{\infty}\operatorname{He}_n(x)\frac{t^n}{n!}.
\]

At \(r=1\), use \(G'=G\) and orthonormality. At \(r=-1\), use \(G'=-G\) and \(H_n(-x)=(-1)^nH_n(x)\).

For an activation \(\phi\) in the stated class and \(q>0\), bounded derivative gives

\[
|\phi(x)|\le |\phi(0)|+\|\phi'\|_\infty |x|.
\]

Consequently \(\phi(\sqrt q\,G)\in L^2\), so define its Hermite coefficients by

\[
\alpha_n=\mathbb E[\phi(\sqrt q\,G)H_n(G)],\qquad
\phi(\sqrt q\,G)=\sum_{n=0}^{\infty}\alpha_nH_n(G)
\quad\text{in }L^2.
\]

Parseval's identity and the covariance identity give

\[
A(r):=\mathbb E[\phi(\sqrt q\,G)\phi(\sqrt q\,G')]
=\sum_{n=0}^{\infty}\alpha_n^2r^n,
\qquad
\sum_{n=0}^{\infty}\alpha_n^2=\mathbb E[\phi(\sqrt q\,G)^2]<\infty.
\]

The passage from finite Hermite sums to the expectation is justified by Cauchy--Schwarz using the two fixed standard Gaussian marginals. The series is uniformly absolutely convergent for \(-1\le r\le1\), including both endpoints.

Its positive coefficient support is unbounded. Otherwise \(\phi(\sqrt q\,x)\) would equal a polynomial for Gaussian-almost every \(x\). Both functions are continuous and Gaussian measure gives positive mass to every nonempty open interval, so equality holds for every real \(x\). Thus \(\phi\) is a polynomial. Its bounded derivative forces its degree to be at most one, contradicting non-affinity. Also \(A(1)>0\), since zero would force the same continuous activation to vanish everywhere.

We now justify composition, including when the preceding kernel has a nonzero constant term. Suppose

\[
B(s)=\sum_{k=0}^{\infty}b_ks^k,\qquad b_k\ge0,\qquad
q=B(1)=\sum_k b_k\in(0,\infty),
\]

and \(A(r)=\sum_{n\ge0}a_nr^n\) with \(a_n\ge0\) and \(\sum_n a_n<\infty\). For each integer \(n\ge0\), the finite-product Cauchy expansion gives

\[
B(s)^n=\sum_{j=0}^{\infty}b_j^{[n]}s^j,
\qquad b_j^{[n]}\ge0,\qquad \sum_j b_j^{[n]}=q^n,
\]

where \(B(s)^0=1\). These product expansions are absolutely convergent on \([-1,1]\). Define

\[
c_j=\sum_{n=0}^{\infty}a_nq^{-n}b_j^{[n]}.
\]

Tonelli's theorem for nonnegative series gives

\[
\sum_jc_j
=\sum_n a_nq^{-n}\sum_jb_j^{[n]}
=\sum_na_n<\infty.
\]

In particular every \(c_j\) is finite. For any \(|s|\le1\), the sum of the absolute values of all expanded terms is at most \(\sum_n a_n\). Rearrangement is therefore valid even for negative \(s\), and

\[
A(B(s)/q)=\sum_{j=0}^{\infty}c_js^j.
\]

The last series is uniformly absolutely convergent on \([-1,1]\). This argument permits \(b_0>0\); it does not rely on the rule for formal power-series composition with zero constant term.

If some \(b_k>0\) with \(k\ge1\), then \(b_{kn}^{[n]}\ge b_k^n\). Hence

\[
c_{kn}\ge a_nq^{-n}b_k^n>0
\qquad\text{whenever }a_n>0.
\]

Unbounded positive support of \(A\) thus implies unbounded positive support of its composition with this nonconstant \(B\).

Apply this argument at layer \(\ell\), with \(B=F_{\ell-1}\), \(q=q_{\ell-1}\), and \(A\) the dual activation of \(\phi_\ell(\sqrt{q_{\ell-1}}\,G)\). Starting from \(F_0(s)=q_0s\), induction yields

\[
F_L(s)=\sum_{n=0}^{\infty}c_ns^n,\qquad
c_n\ge0,\qquad \sum_nc_n=F_L(1)<\infty,
\]

with unbounded positive coefficient support. Each intermediate marginal variance is positive. The bound \(|F_\ell(s)|\le F_\ell(1)\) ensures that the next jointly Gaussian covariance matrix is valid. Uniform convergence proves continuity on the full closed interval and therefore continuity of the spherical kernel and of \(g\).

## Removing affine components while preserving positivity

Let \(\sigma\) denote normalized surface measure on \(S^{d-1}\). The restrictions of affine functions form the space

\[
\mathcal A=\{v\mapsto\beta+w\cdot v:\beta\in\mathbb R,\ w\in\mathbb R^d\}.
\]

Because \(\int v\,d\sigma(v)=0\) and \(\int vv^\top d\sigma(v)=I_d/d\), the \(L^2(\sigma)\) orthogonal projection onto \(\mathcal A\) is

\[
(Ph)(v)=\int h(w)\,d\sigma(w)
+d\,v\cdot\int w h(w)\,d\sigma(w).
\]

This formula also defines a bounded operator on continuous functions with the uniform norm: \(\|Ph\|_\infty\le(1+d)\|h\|_\infty\). Write \(Q=I-P\).

For \(n\ge0\) and any unit vector \(u\), define

\[
a_n=\int(w\cdot u)^n\,d\sigma(w),\qquad
b_n=d\int(w\cdot u)^{n+1}\,d\sigma(w).
\]

Rotational invariance makes these numbers independent of the choice of \(u\). The vector \(\int w(w\cdot u)^n\,d\sigma(w)\) has no component perpendicular to \(u\), by reflection symmetry in each perpendicular direction, and its component along \(u\) is \(\int(w\cdot u)^{n+1}\,d\sigma(w)\). Thus, for the monomial kernel \(k_n(v,u)=(v\cdot u)^n\),

\[
P_vk_n(v,u)=a_n+b_n v\cdot u=P_uk_n(v,u).
\]

The right-hand side is already affine in either variable, so

\[
Q_vQ_uk_n(v,u)=Q_vk_n(v,u)=R_n(v,u),
\qquad
R_n(v,u)=(v\cdot u)^n-a_n-b_n v\cdot u.
\]

Each \(R_n\) is positive semidefinite. Indeed, in the Euclidean tensor space \((\mathbb R^d)^{\otimes n}\), with \(v^{\otimes0}=1\), let \(\Phi_n(v)=v^{\otimes n}\). Then

\[
k_n(v,u)=\langle\Phi_n(v),\Phi_n(u)\rangle.
\]

Apply \(Q\) to each scalar coordinate of this finite-dimensional feature map and denote the result by \(Q\Phi_n\). Linearity in each argument gives

\[
R_n(v,u)=\langle(Q\Phi_n)(v),(Q\Phi_n)(u)\rangle.
\]

Consequently, for arbitrary real coefficients \(z_1,\ldots,z_m\),

\[
\sum_{a,b=1}^m z_az_bR_n(v_a,v_b)
=\left\|\sum_{a=1}^m z_a(Q\Phi_n)(v_a)\right\|^2\ge0.
\]

Define the \(m\times m\) matrix \(\mathbf R_n\) by \((\mathbf R_n)_{ab}=R_n(v_a,v_b)\). Since \(d\ge2\), \(|w\cdot u|<1\) for \(\sigma\)-almost every \(w\). Dominated convergence gives

\[
a_n\longrightarrow0,\qquad b_n\longrightarrow0.
\]

On the finite input set, \((v_a\cdot v_a)^n=1\), while \((v_a\cdot v_b)^n\to0\) whenever \(a\ne b\), by nonparallelness. Therefore

\[
\mathbf R_n\longrightarrow I_m
\]

entrywise and hence in operator norm. There is an integer \(N\) such that

\[
z^\top\mathbf R_nz\ge\tfrac12\|z\|_2^2
\qquad(n\ge N,\ z\in\mathbb R^m).
\]

## Contradiction to affine representability

Uniform absolute convergence of the kernel series and boundedness of \(Q\) permit termwise projection. Thus

\[
(Qg)(v)=\sum_{n=0}^{\infty}c_n\sum_{b=1}^m y_bR_n(v,v_b).
\]

All the exchanges below are absolutely convergent, since \(|a_n|\le1\), \(|b_n|\le d\), \(|R_n(v,u)|\le d+2\), and \(\sum_nc_n<\infty\). If \(g\in\mathcal A\), then \(Qg=0\), so

\[
0=\sum_{a=1}^m y_a(Qg)(v_a)
=\sum_{n=0}^{\infty}c_n\,y^\top\mathbf R_ny.
\]

Every summand is nonnegative. The positive coefficient support is unbounded, so choose \(n\ge N\) with \(c_n>0\). Because \(y\ne0\), this single summand satisfies

\[
c_ny^\top\mathbf R_ny\ge\tfrac12c_n\|y\|_2^2>0,
\]

contradicting the displayed equality. This proves the claimed non-affinity.

The projection argument establishes the slightly more general statement: any continuous dot-product kernel with a nonnegative, summable power series of unbounded positive support has the same conclusion on every finite nonparallel subset of \(S^{d-1}\).

## Precise small-time consequence

Suppose a limiting output trajectory satisfies

\[
f_t=f_0+t g+o(t)\quad\text{in }C(S^{d-1})\text{ as }t\downarrow0,
\qquad f_0\in\mathcal A.
\]

The finite-dimensional subspace \(\mathcal A\) is closed in the uniform norm. The lemma therefore gives

\[
\delta:=\operatorname{dist}_{\infty}(g,\mathcal A)>0.
\]

Translation by \(f_0\in\mathcal A\), positive scaling, and the triangle inequality imply

\[
\operatorname{dist}_{\infty}(f_t,\mathcal A)
\ge t\delta-\|f_t-f_0-tg\|_\infty>0
\]

for every sufficiently small \(t>0\). Thus the limiting predictor is non-affine at each fixed time in some interval \((0,t_*)\). At any such fixed time, uniform convergence of approximating outputs to \(f_t\) transfers a positive lower bound on their distance to every affine predictor.

Finite evaluation convergence can suffice instead. Choose \(d+1\) affinely independent points on the sphere and the unique affine function agreeing with \(g\) there. Since \(g\) is non-affine, there is another sphere point where the functions differ. Affine interpolation then supplies a linear functional \(\Lambda\), formed from evaluations at these \(d+2\) points, such that

\[
\Lambda(h)=0\quad(h\in\mathcal A),\qquad \Lambda(g)\ne0.
\]

If the small-time expansion holds at these finitely many points, then \(\Lambda(f_t)=t\Lambda(g)+o(t)\ne0\) for all sufficiently small positive times. Convergence at those points transfers the same nonzero witness, and hence a positive approximation gap on that finite set, to the approximating outputs. Convergence in probability transfers the gap with probability tending to one.

This consequence excludes all input-linear predictors, including outputs of a composition of linear layers, because their restrictions lie in \(\mathcal A\). It also excludes affine predictors. Initial velocity alone does not prove non-affinity at every arbitrarily prescribed later positive time, and non-affinity alone does not distinguish feature learning from training a nonlinear feature map held fixed at initialization.
