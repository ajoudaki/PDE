# Rank-one completion of the finite critical-point index bound

2026-10-11. Internally checked theorem; the complete check and the
convergence-or-escape assembly are recorded in
[GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md](GAUSSIAN_RANK_ONE_COMPLETION_CHECK.md).
This is an internal mathematical check, not a promotion review.
This is an explicitly authorized continuation in the same study, not a
fresh independent attempt. Its assigned scientific source is the complete
GAUSSIAN_SADDLE_INDEX.md. No experiment or Git operation was used.

The new algebraic result is that every finite critical point with
nonzero readout, nonzero residual, and rank-one residual-weighted backward
matrix has at least \(n\) negative Hessian eigenvalues. Combining it with
the existing rank-\(g\) calculation removes the rank-one exception from
finite-bad-limit avoidance whenever
\[
                 n\ge\max\{1,\,2m-4\}.
\]
This does not prove bounded trajectories, fitting, or avoidance of escape
to infinity. The Gaussian avoidance corollary uses the same classical
local center-stable-manifold fact as GAUSSIAN_SADDLE_INDEX.md, Section 4;
the new contribution here is the completed Hessian index bound.

## 1. Model and finite critical-point identities

Let \(X=(x_1,\ldots,x_m)\in\mathbb R^{d\times m}\) have linearly
independent unit columns, and let \(y\in\mathbb R^m\setminus\{0\}\).
For \(A\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\), define
\[
U=\tanh(AX),\qquad z_a=Wu_a,\qquad
h_a=\tanh z_a,\qquad H=(h_1,\ldots,h_m),\qquad
f=\frac1nH^\top w,\qquad r=f-y,\qquad
\mathcal L=\frac1m\|r\|_2^2.
\]
Here \(u_a=U_{:,a}\), and tanh acts entrywise. Define
\[
E_{ia}=\operatorname{sech}^2(z_{ia})>0,\qquad
b_a=w\odot E_{:,a},\qquad
T=(r_1b_1,\ldots,r_mb_m)
  =\operatorname{diag}(w)E\operatorname{diag}(r).
\]

Because \(X\) has column rank \(m\), the coordinates \(AX\) can be
varied arbitrarily by varying \(A\). Complete them with the unused
input coordinates to obtain linear coordinates on \(A\).
Entrywise tanh is a diffeomorphism from these preactivations to
\((-1,1)^{n\times m}\), so \(U\) is a free local coordinate at every
finite parameter state. At a critical point, Hessian inertia is
preserved under this coordinate change: the second-derivative
chain-rule term is multiplied by the zero loss gradient.

At a finite critical point, stationarity in \(w,W,U\), respectively,
gives
\[
                    Hr=0,\qquad TU^\top=0,\qquad W^\top T=0.
                                                               \tag{1}
\]
We consider
\[
                    0<\mathcal L<\frac1m\|y\|_2^2.              \tag{2}
\]
The first inequality implies \(r\ne0\). The second implies
\(w\ne0\), since zero readout produces \(f=0\) and the initial loss.
Since all entries of \(E\) are strictly positive, \(w\ne0\) and
\(r\ne0\) imply \(T\ne0\). Thus \(g=\operatorname{rank}T\ge1\).

## 2. Rank one supplies an \(n\)-dimensional zero Hessian block

Suppose \(g=1\). Write
\[
\mathcal S=\{a:r_a\ne0\}.
\]
Choose \(a_0\in\mathcal S\) and put \(t=b_{a_0}\ne0\). Every
column \(b_a\), \(a\in\mathcal S\), is proportional to \(t\).
Moreover its proportionality factor is positive:
\[
                     b_a=\beta_a t,\qquad \beta_a>0 .
                                                               \tag{3}
\]
To verify positivity, choose any \(i\) with \(w_i\ne0\).
The ratio \(b_{ia}/b_{ia_0}=E_{ia}/E_{ia_0}\) is positive and
equals the proportionality factor. Equation (1), applied to column
\(a_0\), implies \(W^\top t=0\).

Define a fixed sample vector \(s\in\mathbb R^m\) and a positive scalar
\(C\) at this critical point by
\[
s_a=
\begin{cases}
\operatorname{sgn}(r_a)/\sqrt{\beta_a},&a\in\mathcal S,\\
0,&a\notin\mathcal S,
\end{cases}
\qquad
C=\sum_{a\in\mathcal S}|r_a|\sqrt{\beta_a}>0.                  \tag{4}
\]
For arbitrary \(v\in\mathbb R^n\), consider the first-feature variation
\[
                         \Delta U(v)=v s^\top.               \tag{5}
\]
These variations form an \(n\)-dimensional subspace, because \(s\ne0\).
Their first prediction variation vanishes. Indeed, for
\(a\in\mathcal S\),
\[
\delta f_a=\frac{s_a}{n}b_a^\top Wv
          =\frac{s_a\beta_a}{n}t^\top Wv=0,
\]
and outside \(\mathcal S\) the corresponding column variation is zero.

The entire \(U,U\) Hessian block on (5) also vanishes. The
Gauss--Newton term vanishes by the preceding calculation. For
\(v,v'\in\mathbb R^n\), its residual term is
\[
\frac{2}{mn}\sum_{a\in\mathcal S}r_a s_a^2
(Wv)^\top\operatorname{diag}\bigl(w\odot\tanh''(z_a)\bigr)Wv'.
                                                               \tag{6}
\]
For tanh, \(\tanh'' z=-2\tanh z\,\operatorname{sech}^2z\).
Using (3) and \(\beta_a s_a^2=1\), the diagonal coefficient in
(6) is therefore
\[
\begin{aligned}
\sum_{a\in\mathcal S}r_as_a^2
 \operatorname{diag}\bigl(w\odot\tanh''(z_a)\bigr)
 &=-2\operatorname{diag}\left(
       t\odot\sum_{a\in\mathcal S}r_a\beta_a s_a^2h_a\right)\\
 &=-2\operatorname{diag}(t\odot Hr)=0 .
\end{aligned}                                                   \tag{7}
\]
This proves a zero Hessian block, not an assertion that predictions
remain constant along a finite displacement in (5).

## 3. Readout variations make the mixed block surjective

Let \(\Delta W\) and \(\delta w\) be arbitrary middle-weight and
readout variations. Define
\[
\begin{aligned}
q(\Delta W)
 &=\sum_{a\in\mathcal S}r_as_a
       \operatorname{diag}\bigl(w\odot\tanh''(z_a)\bigr)
       \Delta W u_a \in\mathbb R^n,\\
G_i
 &=\sum_{a\in\mathcal S}r_as_a E_{ia}
   =\sum_{a\in\mathcal S}
        \frac{|r_a|E_{ia}}{\sqrt{\beta_a}}>0,\qquad 1\le i\le n.
\end{aligned}                                                   \tag{8}
\]
Strict positivity of \(G_i\) holds even when \(w_i=0\).
The mixed loss Hessian against (5) is exactly
\[
D^2\mathcal L[\Delta U(v),(\Delta W,\delta w)]
=\frac{2}{mn}v^\top\!
 \left[C\Delta W^\top t
       +W^\top\{q(\Delta W)+G\odot\delta w\}\right].
                                                               \tag{9}
\]

To verify (9), the Gauss--Newton mixed term vanishes because the
prediction differential in the \(\Delta U(v)\) direction is zero.
The mixed prediction derivative on sample \(a\in\mathcal S\)
has three terms: differentiating \(Wv\), the outer activation
derivative, and the readout gives, respectively,
\[
\frac{s_a}{n}\left[
b_a^\top\Delta Wv
+(Wv)^\top\operatorname{diag}
       \bigl(w\odot\tanh''(z_a)\bigr)\Delta Wu_a
+(Wv)^\top\operatorname{diag}(E_{:,a})\delta w
\right].
\]
Multiplication by \(2r_a/m\), summation, and
\(\sum_{a\in\mathcal S}r_as_ab_a=Ct\) give (9).

For each \(\Delta W\), choose
\[
                       \delta w_i=-q_i(\Delta W)/G_i.         \tag{10}
\]
There is no zero denominator. This cancels the entire term inside
\(W^\top\) in (9). The remaining mixed coefficient is
\(C\Delta W^\top t\), which ranges over all \(\mathbb R^n\).
Explicitly, to obtain \(d\in\mathbb R^n\), choose
\[
                    \Delta W=\frac{t d^\top}{C\|t\|_2^2}
\]
and then choose (10). Thus the mixed Hessian block against the
\(n\)-dimensional space (5) has row rank \(n\).

Combining (7) and (9), a restriction of the Hessian has block form
\[
                      \begin{pmatrix}0&B\\ B^\top&D\end{pmatrix},
                      \qquad \operatorname{rank}B=n.
\]
Choose a right inverse \(R_B\) of \(B\). On the \(n\)-dimensional
subspace \((v,-\varepsilon R_Bv)\), the quadratic form is
\[
       -2\varepsilon\|v\|_2^2
       +\varepsilon^2(R_Bv)^\top D(R_Bv).
\]
It is strictly negative for every \(v\ne0\) once
\(\varepsilon>0\) is sufficiently small. Consequently the full Hessian
has at least \(n\) negative eigenvalues.

This proves the rank-one result at every finite width, without any
future kernel gap, width limit, sign assumption on the weights, or
restriction on label ratios.

## 4. Combination with the rank-\(g\) bound

For completeness, the other-rank argument is reproduced here.
Let \(g=\operatorname{rank}T\ge1\) and
\(h=n-\operatorname{rank}U\). Choose an \(n\times h\) matrix
\(Q\) whose columns form an orthonormal basis of \(\ker U^\top\).
The middle-weight subspace
\[
                         \Delta W=VQ^\top,
                         \qquad V\in\mathbb R^{n\times h},
\]
has \(\Delta WU=0\); the loss is constant along it when the other
parameters are fixed. Its pure Hessian block is zero. Its mixed block
against arbitrary \(\Delta U\) is
\[
\frac{2}{mn}\langle T,\Delta W\Delta U\rangle_F
=\frac{2}{mn}\langle QV^\top T,\Delta U\rangle_F .
                                                               \tag{11}
\]
The map \(V\mapsto V^\top T\) has rank \(hg\), and left
multiplication by \(Q\) is injective. The same block-matrix argument
therefore gives at least \(hg\) negative eigenvalues.

By \(TU^\top=0\), the row spaces of \(T\) and \(U\) are
orthogonal subspaces of \(\mathbb R^m\). Hence
\[
\operatorname{rank}U+g\le m,\qquad
hg\ge g(n-m+g).                                               \tag{12}
\]
If \(g=1\), Sections 2--3 supply \(n\) negative directions
regardless of (12). If \(g\ge2\), necessarily \(m\ge2\).
For \(n\ge\max\{1,2m-4\}\), one has \(n-m+2>0\) and
\[
g(n-m+g)\ge2(n-m+2)\ge n.                                    \tag{13}
\]
For \(m=2\), the first assertion follows from \(n\ge1\);
for \(m\ge3\), it follows from
\(n-m+2\ge m-2>0\). The final inequality is equivalent to
\(n\ge2m-4\). When \(m=1\), \(g\ge2\) cannot occur.

**Finite critical-point theorem.** If \(X\) has full column rank and
\(n\ge\max\{1,2m-4\}\), then every finite critical point satisfying
(2) has at least \(n\) strictly negative Hessian eigenvalues.

The coordinate change from \(A\) to \(U\) preserves this index at
critical points. The prescribed positive mobilities \((n,1,n)\)
also preserve the unstable index: minus the mobility matrix times the
Hessian is similar to minus a positive-definite congruence of the
Hessian. Therefore every such critical point has at least \(n\)
unstable linearized training directions.

## 5. Canonical zero-readout consequence and its precise scope

Initialize \(A_{ij}\) iid \(N(0,1)\), \(W_{ij}\) iid \(N(0,1/n)\),
independently, and \(w=0\) exactly. Then, under the width condition in
Section 4,
\[
\mathbb P\!\left[
(A(t),W(t),w(t))\longrightarrow\theta_*
\text{ at a finite critical point with }\mathcal L(\theta_*)>0
\right]=0.                                                   \tag{14}
\]

Here is the reduction to the same local center-stable fact used in the
assigned source. For a \(C^2\) vector field, a finite equilibrium with
at least \(n\) unstable eigenvalues has a local \(C^1\) center-stable
manifold of dimension at most \(N-n\), where
\(N=nd+n^2+n\), containing every forward trajectory that remains in
an appropriate neighborhood. The manifold is locally flow invariant;
zero eigenvalues belong to its center-stable part.

The zero-readout initialization slice
\(M_0=\{(A,W,w):w=0\}\) has dimension \(N-n\). On this slice the
training vector is
\[
                  (0,0,2Hy/m).
\]
Whenever \(Hy\ne0\), it is not tangent to \(M_0\).
Finite-time inverse images of the local center-stable manifolds have
the same dimension and have the vector field in their tangent spaces
at relevant locally invariant points. Their tangents cannot contain
\(TM_0\): dimension equality would then force equality with \(TM_0\),
contradicting the non-tangency of the vector field.

Locally express such an inverse-image manifold as the zero set of a
\(C^1\) submersion. At least one component has a nonzero differential
when restricted to \(M_0\). The implicit-function theorem places its
intersection with \(M_0\) inside a hypersurface of that slice. Thus the
intersection is Lebesgue null on the part of \(M_0\) where \(Hy\ne0\).
Countably many local charts, a countable cover of the relevant critical
neighborhoods, and integer entrance times cover all trajectories with
such a finite limit.

Finally \(Hy\ne0\) almost surely under the prescribed Gaussian law.
Conditional on invertible \(W\), the matrix \(AX\) has a density because
\(X\) has column rank \(m\). Entrywise tanh, left multiplication by
\(W\), and entrywise tanh again are diffeomorphisms onto open images.
Thus \(H\) has a density, and \(Hy=0\) is null for \(y\ne0\).
The Gaussian law of \((A,W)\) is absolutely continuous on \(M_0\).
Also \(\dot w(0)=2Hy/m\ne0\) implies a strict initial loss decrease,
so any finite bad limit satisfies (2). These observations yield (14).

No finite-time blowup obstructs this reasoning. The exact identity
\[
-\dot{\mathcal L}
=\frac1n\|\dot A\|_F^2+\|\dot W\|_F^2+\frac1n\|\dot w\|_2^2
\]
bounds the parameter path length on \([0,T]\), in the corresponding
mobility metric, by \(\sqrt{T\mathcal L(0)}\). The smooth finite
dimensional vector field therefore has a global forward solution.

Equation (14) is not an all-time fitting theorem. It excludes finite
bad critical limits; it does not exclude a nonconvergent or unbounded
trajectory with positive limiting loss. Any stronger analytic-gradient
convergence-or-escape corollary requires its own stated theorem and
hypothesis check. Full-column-rank \(X\) remains essential throughout:
for dependent inputs, the \(U\) variations in (5) need not be
accessible by varying \(A\), so their Hessian index cannot be silently
transferred to the original network.
