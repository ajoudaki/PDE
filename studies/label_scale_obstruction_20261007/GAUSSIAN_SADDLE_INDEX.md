# Negative curvature and canonical zero-readout avoidance

2026-10-11. Internally checked theoretical strengthening; see
[GAUSSIAN_SADDLE_INDEX_CHECK.md](GAUSSIAN_SADDLE_INDEX_CHECK.md).
This is not an independent promotion review.
This continues the same Gaussian label-scale investigation. It does not
construct a positive-probability failure event or prove arbitrary-data
fitting. No experiment or Git operation was used.

Scientific inputs: the canonical model in the maintained notation contract;
the complete UNCONDITIONAL_NEGATIVE_ROUTE.md, particularly its two-input
zero-readout transversality argument; and the classical local center-stable
manifold theorem, whose required form is stated below. No other study is a
source.

## 1. Model and result

Let \(X\in\mathbb R^{d\times m}\) have linearly independent unit columns.
The fully trained two-hidden-layer tanh network is
\[
 U=\tanh(AX),\qquad H=\tanh(WU),\qquad
 f=H^\top w/n,\qquad r=f-y,\qquad
 \mathcal L=\|r\|_2^2/m.
\]
The mobilities of \(A,W,w\) are \(n,1,n\). Initially \(A_{ij}\) are
independent \(N(0,1)\), \(W_{ij}\) are independent \(N(0,1/n)\), the two
arrays are independent, and \(w=0\) exactly. The label vector \(y\ne0\)
is fixed independently of these draws.

At a finite critical point define the residual-weighted backward matrix
\[
 T=\operatorname{diag}(w)
       [1-\tanh^2(WU)]\operatorname{diag}(r)\in\mathbb R^{n\times m}.
 \tag{1}
\]
The bracket is entrywise. Locally write \(g=\operatorname{rank}T\).
If \(0<\mathcal L<\|y\|_2^2/m\), then \(g\ge1\), and the loss Hessian
has at least
\[
       g\,[\,n-\operatorname{rank}U\,]
       \ \ge\ g(n-m+g)
 \tag{2}
\]
strictly negative eigenvalues. The second inequality is useful when its
right side is positive.

Consequently, for \(m\ge3\) and \(n\ge\max\{1,2m-4\}\), the exact
canonical initialization has probability zero of convergence to a finite
positive-loss critical point for which \(\operatorname{rank}T\ge2\).
Any remaining finite bad limit must have \(\operatorname{rank}T=1\).
This is a restriction on the failure mechanism, not a proof that all
such rank-one limits are avoided.

The input independence assumption matters: the previous stable bad basins
on rank-deficient datasets are not contradicted by this result.

## 2. First features are valid local coordinates

Because \(X\) has column rank \(m\), the map
\(A\mapsto AX\) is onto \(\mathbb R^{n\times m}\). Complete \(AX\) with
the components of \(A\) on the orthogonal complement of the input span
to obtain linear coordinates on \(A\). Entrywise tanh is a smooth
diffeomorphism from the preactivation coordinates to
\((-1,1)^{n\times m}\). Thus \(U\), together with the unused coordinates,
forms a local coordinate system at every finite state.

At a critical point, the Hessian in different smooth coordinates is
related by an invertible congruence: the extra chain-rule term contains
the first derivative of the loss and vanishes there. Hence its number of
negative directions is unchanged. The unused input coordinates do not
affect the loss and can be omitted.

Stationarity with respect to \(W\) and \(U\) gives
\[
        TU^\top=0,\qquad W^\top T=0.
 \tag{3}
\]
Since the finite tanh derivative is strictly positive, nonzero \(w\)
and \(r\) imply \(T\ne0\). The stated loss interval forces \(w\ne0\),
because \(w=0\) would give the initial loss. Also \(r\ne0\).
The row spaces of \(T\) and \(U\) in \(\mathbb R^m\) are orthogonal
by (3), so
\[
             \operatorname{rank}U+g\le m.
 \tag{4}
\]

## 3. A large flat block with a nondegenerate mixed block

Set \(h=n-\operatorname{rank}U\), and choose an \(n\times h\) matrix
\(Q\) whose columns are an orthonormal basis of \(\ker U^\top\).
For any \(V\in\mathbb R^{n\times h}\), the perturbation
\(\Delta W=VQ^\top\) satisfies \(\Delta WU=0\). Varying \(W\) in
this whole subspace, with \(U,w\) fixed, leaves the predictions exactly
unchanged. The \(W,W\) Hessian block on this subspace is therefore zero.

For arbitrary \(\Delta U\in\mathbb R^{n\times m}\), the mixed derivative
of the preactivation is \(\Delta W\Delta U\). Its first derivative in
the \(\Delta W\) direction vanishes. Both the loss Gauss--Newton mixed
term and the outer activation's second-derivative term consequently
vanish, leaving exactly
\[
 D^2\mathcal L[\Delta W,\Delta U]
       =\frac{2}{mn}\langle T,\Delta W\Delta U\rangle_F
       =\frac{2}{mn}\langle QV^\top T,\Delta U\rangle_F.
 \tag{5}
\]
The map \(V\mapsto V^\top T\) has rank \(hg\): each of its \(h\) rows
can be chosen independently in the \(g\)-dimensional row space of \(T\).
Left multiplication by \(Q\) is injective. Thus the mixed block (5)
has rank exactly \(hg\).

For clarity, a symmetric block matrix
\[
       \begin{pmatrix}0&B\\ B^\top&C\end{pmatrix}
\]
with \(\operatorname{rank}B=k\) has at least \(k\) negative eigenvalues.
Choose a \(k\)-dimensional subspace of the first block on which
\(B^\top\) is injective. For vectors \((v,-\epsilon B^\top v)\),
the quadratic form is
\[
 -2\epsilon\|B^\top v\|_2^2
       +\epsilon^2(B^\top v)^\top C(B^\top v).
\]
Compactness of its unit sphere makes the first term uniformly negative
and dominant for sufficiently small \(\epsilon>0\). This proves the
claim, and with (4)--(5) proves (2).

For \(g\ge2\), the lower bound obeys
\[
 g(n-m+g)\ge 2(n-m+2)\ge n
 \quad\text{when } n\ge2m-4,\ m\ge3.
 \tag{6}
\]
Indeed \(n-m+2\ge m-2>0\) under this width assumption, and increasing
the integer \(g\ge2\) increases the first expression. This is the
unstable-dimension threshold needed for the singular initialization.

## 4. Why at least \(n\) unstable directions suffice

Let \(N=nd+n^2+n\) be the full parameter dimension and
\(M_0=\{w=0\}\), of dimension \(N-n\). We use the following precise
local center-stable fact. At an equilibrium of a \(C^2\) vector field
having \(k\) eigenvalues with strictly positive real part, there is a
local \(C^1\), locally flow-invariant manifold of dimension \(N-k\)
containing every forward orbit that remains in a sufficiently small
neighborhood. Zero eigenvalues belong to the center-stable block.
This follows from the cutoff/Perron construction; the relevant
spectral-split and regularity arguments are in
[Eldering, Sections 3 and 3.1](https://www.jaapeldering.nl/files/lect-ICMC-invarmflds.pdf).
The complete cutoff/Perron construction, including the required \(C^1\)
regularity in the presence of zero eigenvalues, is supplied in
[TWO_SAMPLE_AVOIDANCE_CHECK.md](TWO_SAMPLE_AVOIDANCE_CHECK.md), Section 5.
Thus no neural-network convergence theorem is assumed.

The linearized training field is minus the positive mobility matrix
times the loss Hessian. It is similar to the negative of a symmetric
congruence of that Hessian, so (6) gives at least \(n\) unstable
directions. Its local center-stable manifolds have dimension at most
\(N-n=\dim M_0\).

At an initialization point with \(Hy\ne0\), the vector field is
\[
        (\dot A,\dot W,\dot w)=(0,0,2Hy/m),
 \tag{7}
\]
which is not tangent to \(M_0\). A finite-time inverse image of a
locally invariant center-stable manifold is a \(C^1\) manifold of
the same dimension wherever the inverse flow is defined. Its tangent
contains the training vector field. At an intersection with \(M_0\)
where \(Hy\ne0\), its tangent therefore cannot contain \(T M_0\):
the dimension bound would force equality, in conflict with (7).

Writing the inverse-image manifold locally as the zero set of a
submersion, at least one component of that submersion has nonzero
derivative on \(M_0\). The implicit-function theorem contains its
intersection with \(M_0\) in a hypersurface of \(M_0\); that
intersection is Lebesgue null on \(M_0\). Countably many charts cover
it. A countable subcover of the relevant critical neighborhoods and
integer entrance times covers every trajectory converging to one of
the critical points under consideration. Their initial states are
therefore null on the nonstationary part of \(M_0\).

The Gaussian law has a density on \(M_0\). Moreover \(Hy\ne0\)
almost surely: condition on invertible \(W_0\), an almost-sure event.
Since \(X\) has full column rank, \(A_0X\) has a density in
\(\mathbb R^{n\times m}\). Entrywise tanh, left multiplication by
invertible \(W_0\), and entrywise tanh again are diffeomorphisms onto
open images. Thus \(H_0\) has a density. For \(y\ne0\), \(Hy=0\)
is a proper linear subspace and is null.

Consequently the initial loss strictly decreases, so any finite bad
limit has loss strictly below its initial value, and the preceding
argument applies. This proves the claimed Gaussian avoidance using the
center-stable construction above, not an assumed property of the future
neural trajectory.

## 5. Exact remaining boundary

This result does not prove avoidance of rank-one \(T\) at general
sample count, boundedness of trajectories, fitting, a convergence rate,
or any compression conclusion. For two inputs the stronger special
classification in UNCONDITIONAL_NEGATIVE_ROUTE.md provides the missing
\(n\)-direction bound even in its rank-one case. That separate argument
and its analytic-flow dependencies are checked in
[TWO_SAMPLE_AVOIDANCE_CHECK.md](TWO_SAMPLE_AVOIDANCE_CHECK.md).

For dependent inputs, \(U\) is not a free local coordinate and (5)
need not have the rank computed here. The proof does not silently
replace nonparallel inputs by linearly independent ones.
