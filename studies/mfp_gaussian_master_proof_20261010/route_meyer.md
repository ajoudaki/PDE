# Uniform moments by Gaussian divergence

This route was developed from the prompt alone. Its sole non-elementary dependency is the dimension-free Gaussian divergence inequality stated below. That dependency has **not been source-verified** within this route. The algebraic reduction is complete; no rank or inverse-Gram assumption is used.

## Setup and dependency

The program has finitely many vector and scalar nodes, independent of the width \(n\). Gaussian root tuples have fixed laws, are independent across neurons and layers, and are independent of the matrices. Matrix entries are independent \(N(0,1/n)\), with exact reuse allowed. Coordinate and scalar maps are smooth and all their derivatives have polynomial growth. Scalar averages are normalized by \(1/n\).

Represent each root tuple by a fixed affine map of standard Gaussian coordinates, allowing a singular covariance square root. Let \(G\) collect these coordinates and \(G^{(a)}_{ij}=\sqrt n\,W^{(a)}_{ij}\). For every fixed \(n\), the program and every derivative have polynomial growth in this finite Gaussian vector, hence all Gaussian Sobolev norms below are finite without any uniform estimate.

The needed external result is the following finite-dimensional Meyer divergence inequality: for \(p\ge2\), standard Gaussian \(G\in\mathbb R^N\), and smooth polynomial-growth \(U:\mathbb R^N\to\mathbb R^N\),

\[
\|\delta U\|_{L^p}\le C_p\bigl(\|U\|_{L^p(\ell^2)}+\|DU\|_{L^p(\mathrm{HS})}\bigr),
\qquad \delta U=G\cdot U-\operatorname{div}U,
\tag{1}
\]

with \(C_p\) independent of \(N\). Source verification of precisely this statement remains outstanding.

## Inductive derivative estimates

Define

\[
\|x\|_{r,n}=\left(n^{-1}\sum_i|x_i|^r\right)^{1/r},
\qquad
\|A\|_{S_r,n}=\left(n^{-1}\operatorname{tr}|A|^r\right)^{1/r}.
\]

Induct over nodes, proving every coordinate moment uniformly in \(n\) and the coordinate, and every scalar moment. Coordinate maps preserve these assertions by polynomial growth and Hölder. Normalized averages preserve them by Jensen. Scalar feedback then preserves them by polynomial growth. Only a matrix action remains.

For any earlier vector \(v\), its differentiation paths contain vector-to-vector factors of the following forms: \(W^{(a)}\), \(W^{(a)\top}\), diagonals of partial derivatives, scalar multiples of the identity, and normalized rank-one factors \(ab^\top/n\). The last form results from a path passing through a normalized scalar average and subsequently returning to a vector. All derivative entries and coefficients have moments of every order by the induction hypothesis.

These factors have uniformly bounded moments of every normalized Schatten norm. For a rank-one factor,

\[
\|ab^\top/n\|_{S_r,n}=n^{-1/r}\|a\|_{2,n}\|b\|_{2,n}
\le\|a\|_{2,n}\|b\|_{2,n}.
\tag{2}
\]

Gaussian operator-norm moments are uniform: a sphere \(1/4\)-net of cardinality at most \(9^n\) gives

\[
\mathbb P(\|W\|_{\mathrm{op}}>2t)\le2\,9^{2n}e^{-nt^2/2},
\]

which has an integrable uniform tail above a sufficiently large fixed \(t\). For a product of \(m\) factors, normalized Schatten Hölder gives

\[
\|A_1\cdots A_m\|_{S_r,n}\le\prod_{\nu=1}^m\|A_\nu\|_{S_{mr},n}.
\tag{3}
\]

Ordinary Hölder handles dependence between factors. Thus every path Jacobian and every finite sum \(A\) of path Jacobians obeys

\[
\sup_n\mathbb E\|A\|_{S_r,n}^p<\infty
\quad(r\ge1,\ p<\infty).
\tag{4}
\]

For a particular reused matrix, graph differentiation gives exactly

\[
D_{G^{(a)}}v[H]
=n^{-1/2}\sum_{r\text{ forward}}A_rHb_r
+n^{-1/2}\sum_{r\text{ transpose}}A_rH^\top b_r.
\tag{5}
\]

Here \(b_r\) is the input at occurrence \(r\), and \(A_r\) is the subsequent output-to-\(v\) Jacobian. Each occurrence is counted. The Hilbert–Schmidt norm of \(H\mapsto AHb\), from matrix Frobenius space to vector Euclidean space, equals \(\|A\|_F\|b\|_2\), and the transpose map has the same norm. Consequently,

\[
n^{-1/2}\|D_{G^{(a)}}v\|_{\mathrm{HS}}
\le\sum_r\|A_r\|_{S_2,n}\|b_r\|_{2,n}.
\tag{6}
\]

Root derivatives are finite sums of path Jacobians times fixed covariance-square-root coefficients. Summing over the finitely many Gaussian input blocks therefore yields

\[
\sup_n\mathbb E\left(n^{-1/2}\|Dv\|_{\mathrm{HS}}\right)^p<\infty.
\tag{7}
\]

All quantities on the right arise before the matrix action currently being proved.

## Matrix action

For \(y=W^{(a)}v\) and a fixed coordinate \(i\), define a vector field on the entire Gaussian input space by

\[
(U_i)_{G^{(a)}_{kl}}=n^{-1/2}\mathbf1_{\{k=i\}}v_l,
\]

and zero in all other coordinates. Then

\[
\|U_i\|_{\ell^2}=\|v\|_{2,n},
\qquad
\|DU_i\|_{\mathrm{HS}}=n^{-1/2}\|Dv\|_{\mathrm{HS}},
\]

and the exact divergence identity is

\[
y_i=\delta U_i+n^{-1/2}\sum_j\frac{\partial v_j}{\partial G^{(a)}_{ij}}.
\tag{8}
\]

The external inequality (1) and (7) bound all moments of \(\delta U_i\) uniformly. Using (5), each forward occurrence contributes \((A_r^\top b_r)_i/n\) to the correction in (8), and each transpose occurrence contributes \((\operatorname{tr}A_r/n)(b_r)_i\). The deterministic estimates

\[
\frac{|(A^\top b)_i|}{n}\le\|A\|_{S_2,n}\|b\|_{2,n},
\qquad
\left|\frac{\operatorname{tr}A}{n}b_i\right|\le\|A\|_{S_2,n}|b_i|
\tag{9}
\]

bound all their moments by (4), earlier vector moments, and Hölder. This proves the coordinate moments for \(W^{(a)}v\). For \(W^{(a)\top}v\), support \(U_i\) on column \(i\); the two correction formulas interchange and the bounds are identical.

This completes the program induction, conditional only on (1). No output moment is used to bound itself, and dependence caused by matrix reuse requires no additional assumption.

Finally, for \(q\ge1\),

\[
\mathbb E\left(n^{-1}\sum_i|v_i|^p\right)^q
\le n^{-1}\sum_i\mathbb E|v_i|^{pq}.
\]

For \(0<q<1\), Jensen in probability reduces to \(q=1\). Hence all required empirical moments follow.
