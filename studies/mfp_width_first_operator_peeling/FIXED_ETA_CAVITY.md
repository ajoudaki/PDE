# Fixed-step dynamic cavity for the two-step operator DAG

## Status and scope

This note proves the exact alternating Gaussian regression formulas and the
two necessary response cancellations.  It does **not** yet prove identification
of the four-stage DAG at each fixed nonzero step size.  The localized
high-moment empirical-LLN section is a proof blueprint: a stopped
stage-indexed coupling, a joint innovation-block construction, a tangent-field
induction for \(\rho,\sigma\), and complete bad-event removal remain to be
written.  Thus fixed-step network identification is open under the strong
activation class below.

Assume

$$
\phi\in C^8(\mathbb R),
$$

$$
\phi',\ldots,\phi^{(8)}\text{ are bounded},
\qquad
|\phi(x)|\le C(1+|x|),
$$

and

$$
\mathbb E[\phi(G)^2]=1.
$$

The polynomial-growth extension requires a truncation and uniform
high-moment argument and is not asserted here.

## Alternating Gaussian conditioning lemma

Let \(W\in\mathbb R^{n\times n}\) have independent standard Gaussian entries.
Suppose a finite adaptive program has already revealed

$$
\frac1{\sqrt n}WH
\qquad\text{and}\qquad
\frac1{\sqrt n}W^\top C,
$$

where the columns of \(H\) and \(C\) were measurable before their respective
matrix queries.  Conditional on the revealed sigma-field,

$$
\boxed{
W
=
P_CW+WP_H-P_CWP_H
+P_C^\perp\widetilde W P_H^\perp,
}
$$

where \(\widetilde W\) is an independent standard Gaussian matrix.  This is
ordinary Gaussian regression on the revealed linear subspace, applied
sequentially to adaptive queries.

For a new residual query, replacing \(P_H^\perp g\) by an independent
\(g\sim\mathcal N(0,I_n)\) costs

$$
\mathbb E\|P_Hg\|_n^2
=
\frac{\operatorname{rank}(H)}n,
\qquad
\|x\|_n^2=\frac1n\sum_i x_i^2.
$$

Because the number of queries is fixed, this is
\(O(n^{-1})\) in squared normalized norm.  The analogous row projection has
the same bound.

Under a fixed positive lower bound on the population Gram eigenvalues, the
regression coefficients are locally Lipschitz functions of finitely many
empirical inner products on the corresponding good event.  The required
adaptive empirical-LLN induction is proved below.  A one-line appeal to
Gaussian Poincaré would be insufficient, because the coordinates share random
empirical coefficients and the required quadratic observables are not
globally Lipschitz.

## Chronological filtration

Use the base Gaussian matrix \(W\); the learned rank-one updates are kept
explicit.  Reveal

$$
z^0=Wh^0/\sqrt n,
$$

then

$$
b^0=W^\top c^0/\sqrt n,
$$

then

$$
y^1=Wh^1/\sqrt n,
$$

and finally

$$
g^1=W^\top c^1/\sqrt n.
$$

At each point the new feature or cotangent vector is measurable with respect
to the previous filtration.  The exact learned-matrix terms are added only
after the corresponding base-matrix query is peeled.

## Initial forward and transpose queries

Conditional on \(h^0\), the first forward field is exactly Gaussian with
empirical variance \(\|h^0\|_n^2\), which converges to one.  Thus

$$
z^0\Longrightarrow\xi_0.
$$

For

$$
c_i^0=a_i\phi'(z_i^0),
$$

the possible transpose response is proportional to

$$
\mathbb E[A\phi''(Z)]=0.
$$

Consequently,

$$
\frac1{\sqrt n}W^\top c^0
=
\chi_0+O_{L^2}(n^{-1/2}),
$$

with

$$
\mathbb E[\chi_0^2]=d.
$$

## Reused row: construction of \(z^1\)

Conditioning on the first forward and transpose queries and applying the row
version of the lemma gives

$$
\frac1{\sqrt n}Wh^1
=
\xi_1+\rho_{10}c^0+O_{L^2}(n^{-1/2}).
$$

The coefficient is identified by Stein's identity in \(\chi_0\):

$$
\rho_{10}
=
\mathbb E[\partial_{\chi_0}h_1].
$$

The first learned rank-one matrix update adds exactly

$$
hQ_{01}c^0.
$$

Hence

$$
z^1
\Longrightarrow
\xi_1+(\rho_{10}+hQ_{01})c_0.
$$

## Critical reused column: construction of \(b^1\)

Let

$$
H=[h^0,h^1],
\qquad
Y=[z^0,y^1]=\frac1{\sqrt n}WH,
$$

and define

$$
q_n=\frac1nH^\top H,
\qquad
k_{rs}^{(n)}=\frac1n(c^r)^\top c^s,
$$

$$
r_s^{(n)}=\frac1nY^\top c^s.
$$

Gaussian regression, first along \(c^0\) and then along the span of \(H\),
gives exactly

$$
\begin{aligned}
\frac1{\sqrt n}W^\top c^1
={}&
\frac{k_{01}^{(n)}}{k_{00}^{(n)}}b^0\\
&+Hq_n^{-1}
\left(
r_1^{(n)}
-\frac{k_{01}^{(n)}}{k_{00}^{(n)}}r_0^{(n)}
\right)\\
&+\tau_nP_H^\perp g,
\end{aligned}
$$

where

$$
\tau_n^2
=
k_{11}^{(n)}
-\frac{(k_{01}^{(n)})^2}{k_{00}^{(n)}}.
$$

The cancellation in the deterministic coefficient is essential.  In the
limiting first-row peel,

$$
y^1=\xi_1+\rho_{10}c_0,
$$

so

$$
r_0
=
\mathbb E[Yc_0]
=
\begin{pmatrix}
0\\
\rho_{10}d
\end{pmatrix},
$$

not zero.  On the other hand, multivariate Stein differentiation of \(c_1\)
in the fresh Gaussian coordinates gives

$$
r_1
=
Q
\begin{pmatrix}
\sigma_{10}\\
\sigma_{11}
\end{pmatrix}
+
\begin{pmatrix}
0\\
\rho_{10}K_{01}
\end{pmatrix}.
$$

Since \(k_{00}\to d\),

$$
r_1-\frac{K_{01}}d r_0
=
Q
\begin{pmatrix}
\sigma_{10}\\
\sigma_{11}
\end{pmatrix}.
$$

Thus the inverse \(Q^{-1}\) cancels and the regression coefficient is exactly
\((\sigma_{10},\sigma_{11})\).  Coupling the residual with a centered Gaussian
pair \((\chi_0,\chi_1)\) of covariance \(K\) gives

$$
\frac1{\sqrt n}W^\top c^1
=
\chi_1+\sigma_{10}h^0+\sigma_{11}h^1
+O_{L^2}(n^{-1/2}).
$$

The existing learned matrix contains only the first update, which contributes

$$
hK_{01}h^0.
$$

Therefore

$$
\boxed{
b^1
=
\chi_1
+(\sigma_{10}+hK_{01})h^0
+\sigma_{11}h^1
+O_{L^2}(n^{-1/2}).
}
$$

There is no \(hK_{11}h^1\) term before the second matrix update.

## Terminal reused row

Apply the row version of the same conditioning lemma with the two cotangent
queries.  The response cancellation is the transpose analogue of the one
above.  In block notation write

$$
Y=\xi+CA,
\qquad
B=\chi+H\Sigma,
$$

and set

$$
q=\mathbb E[H^\top h_2],
\qquad
\rho=\mathbb E[\nabla_\chi h_2].
$$

Stein and compatibility give

$$
\mathbb E[B^\top h_2]
=K\rho+\Sigma^\top q,
$$

$$
R:=\mathbb E[C^\top Y]
=\Sigma^\top Q+KA.
$$

The direct cotangent-regression coefficient is therefore

$$
K^{-1}
\left(
\mathbb E[B^\top h_2]-RQ^{-1}q
\right)
=\rho-AQ^{-1}q.
$$

The row-projection term \(YQ^{-1}q\) already contributes
\(CAQ^{-1}q\), so the total response is exactly \(C\rho\).  Thus

$$
\frac1{\sqrt n}Wh^2
=
\xi_2+\rho_{20}c^0+\rho_{21}c^1
+O_{L^2}(n^{-1/2}).
$$

The two exact learned-matrix terms are

$$
hQ_{02}c^0+hQ_{12}c^1.
$$

Consequently,

$$
z^2
\Longrightarrow
\xi_2
+(\rho_{20}+hQ_{02})c_0
+(\rho_{21}+hQ_{12})c_1.
$$

This is the terminal node of the four-stage operator DAG.

## Rank stability at fixed nonzero step size

Let

$$
e=\mathbb E[\phi'(G)^4].
$$

The direct width-first jets give

$$
\det Q(h)=de\,h^2+O(h^4).
$$

For the cotangent Gram,

$$
\det K(h)=d\tau h^2+O(h^4),
$$

where

$$
\tau
=
\ell+2cm+3c^2s+edt.
$$

This number is nonnegative for structural reasons.  If \(A,B,G\) are
independent standard Gaussians and

$$
V
=
\phi(G)\phi'(G)
+\sqrt{de}\,AB\phi''(G)
+cA^2\phi'(G)\phi''(G),
$$

then

$$
\tau=\mathbb E[V^2].
$$

If \(d>0\), then \(e>0\) and \(\tau>0\).  Indeed, if
\(\mathbb E[\phi''(G)^2]>0\), the independent-\(B\) component gives
\(\tau\ge de\,\mathbb E[\phi''(G)^2]>0\).  If that moment vanishes, \(\phi\)
is affine, and RMS normalization gives \(\tau=\ell=d>0\).

It follows that \(Q(h)\) and \(K(h)\) are invertible for every sufficiently
small fixed \(h\ne0\).  Their inverse norms can diverge as \(h\to0\); this
does not affect the pointwise-fixed-\(h\) width limit.

If \(d=0\), smoothness forces \(\phi\) to be constant.  This is the separate
readout-only case and the comparison error is exactly zero.

## Adaptive empirical-LLN lemma

Fix the finite number of alternating queries and a nonzero step size \(h\).
Assume every population Gram used by the regression has smallest nonzero
eigenvalue at least \(\gamma(h)>0\).  Couple each actual field \(X_n^s\) to
the corresponding iid state-evolution field \(\bar X^s\).  For every fixed
moment order \(p\), the induction maintains

$$
\left(
\mathbb E\|X_n^s-\bar X^s\|_{n,2}^p
\right)^{1/p}
\le C_{p,h}n^{-1/2},
$$

uniform moments of every required order, and

$$
\|A_n-A\|_{L^p}
\le C_{p,h}n^{-1/2}
$$

for every Gram, cross-moment, and response statistic.

### Innovation step

Conditionally on the chronological filtration, a new residual query has the
form

$$
\tau_nP_H^\perp g.
$$

Use the same fresh iid Gaussian \(g\) for the ideal innovation \(\tau g\).
Since the query rank is bounded by a fixed constant,

$$
\left(
\mathbb E[
\|P_Hg\|_{n,2}^p
\mid\mathcal F]
\right)^{1/p}
\le C_pn^{-1/2}.
$$

On the rank-stable event, the Schur complement \(\tau_n\) is a smooth
function of the empirical Grams, so

$$
\|\tau_n-\tau\|_{L^p}
=O(n^{-1/2}).
$$

Thus the new Gaussian action couples to its iid state-evolution action with
the required rate.  The row case is identical.

### Coordinate maps and empirical observables

Every coordinate map used here satisfies, for some fixed \(r\),

$$
|\Psi(x;\theta)-\Psi(y;\vartheta)|
\le
C(1+|x|^r+|y|^r)
\bigl(|x-y|+|\theta-\vartheta|\bigr).
$$

Hölder's inequality and the high-moment induction transfer the field coupling
through each map.  For the ideal iid array, Rosenthal's inequality gives

$$
\left\|
\frac1n\sum_i\Psi(\bar X_i)
-\mathbb E[\Psi(\bar X)]
\right\|_{L^p}
\le C_pn^{-1/2}.
$$

Comparing actual and ideal coordinates first, and then applying this iid
bound, gives the same rate for every required quadratic observable.  Rational
regression coefficients are locally Lipschitz functions of these finitely
many observables on the good event, so their errors also have this rate.

### Rank localization

Let \(\mathcal G_s\) be the event that every population-rank direction exposed
through stage \(s\) has empirical eigenvalue at least \(\gamma(h)/2\).  By
Weyl's inequality and the preceding estimates at arbitrarily high fixed
moments,

$$
\mathbb P(\mathcal G_s^c)
\le C_{M,h}n^{-M}
$$

for any prescribed \(M\).  On \(\mathcal G_s\), all regression maps have
bounded derivatives depending only on \(h\).  On its complement, retain the
exact projector/Moore--Penrose representation rather than bounding an inverse.
The original network dynamics contains no Gram inverse, so its uniform raw
field moments and Hölder's inequality make the bad-event contribution
\(o(n^{-1/2})\) after choosing \(M\) sufficiently large.

Uniform inverse-Gram moments are neither needed nor generally true.  For
example, a smooth compactly supported activation has positive probability
that all sampled initial features vanish, making the empirical Gram singular
at every finite \(n\), even though the population Gram is positive definite.

### Moment induction

Fresh terms are Gaussian with variances given by empirical second moments;
all projection ranks are fixed; \(\phi\) has at most linear growth; and its
derivatives are bounded.  Consequently every new field has each fixed moment
bounded by finitely many earlier moments.  The induction begins with Gaussian
marks and therefore closes for all fixed moment orders.  If a crude global
matrix bound is needed on a bad event, the standard Gaussian estimate

$$
\mathbb P
\left(
\|W\|_{\mathrm{op}}>2\sqrt n+t
\right)
\le2e^{-t^2/2}
$$

supplies uniform moments of \(\|W\|_{\mathrm{op}}/\sqrt n\).

Completing the omitted stopped value-and-tangent coupling would prove the
adaptive empirical-LLN lemma by induction over the fixed four queries.
Applying such a completed lemma to the exact response algebra above would give
joint empirical convergence of

$$
(u^0,u^1,u^2,z^0,z^1,z^2,a^0,a^1,a^2)
$$

to the four-stage Gaussian DAG, together with convergence of every empirical
\(Q,K,\rho,\sigma\) coefficient.  One would then still need proved
linear-growth moment bounds to obtain uniform integrability of the terminal
output and conclude

$$
\lim_{n\to\infty}\mathbb E[f_{n,1}(h)]
=\mathsf F_1(h),
$$

$$
\lim_{n\to\infty}\mathbb E[f_{n,2}(h)]
=\mathsf F_2(h).
$$

These two limits are therefore targets, not established conclusions of this
note.  They are only pointwise in \(h\); no estimate uniform as \(h\to0\) is
proposed.
