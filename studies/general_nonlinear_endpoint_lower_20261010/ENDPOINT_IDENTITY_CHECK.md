# Independent check of the exact endpoint identity

Verdict: the identity and deterministic cubic estimate in
ENDPOINT_IDENTITY.md are correct on the initialization/fitting event stated
in the supplied canonical source. No sign, mobility, normalization, or
sample-count error was found. The note correctly leaves the requested
endpoint fluctuation lower bound unproved and does not misrepresent that gap
as a counterexample.

This bounded check read the complete ENDPOINT_IDENTITY.md,
paper/compact.tex, and paper/compact_fitting.tex. It did not read other
routes or studies and did not run experiments.

## Kernel and endpoint algebra

For the paper's prediction \(f_n=n^{-1}w^\top h^{(L)}\), the parameter
derivatives are

\[
\nabla_w f_n=\frac{h^{(L)}}n,\qquad
\nabla_{W^{(1)}}f_n=\frac{\delta^{(1)}v^\top}n,\qquad
\nabla_{W^{(\ell)}}f_n
 =\frac{\delta^{(\ell)}h^{(\ell-1)\top}}n
 \quad(2\le\ell\le L).
\]

The readout and first-layer mobilities are \(n\); the other hidden-layer
mobilities are one. Their weighted derivative inner products therefore give
exactly the kernel displayed in the checked note. In particular, the
first-layer term has denominator \(n\) and factor \(v^\top u\), while each
later hidden-layer term has denominator \(n^2\).

Write \(e(t)=y-f_n(t,X)\). The loss normalization gives
\(\partial_t f_n(t,x)=(2/m)K_t(x,X)e(t)\), with the positive sign used in
the note. Since \(w(0)=0\), all \(\delta^{(\ell)}(0)\) vanish and \(K_0\)
is the readout feature Gram. The fitting event gives
\(\lambda_{\min}(K_0(X,X))\ge\gamma/2\), so its inverse exists.

The fitting bounds imply a uniform bound on every kernel term over time and
the sphere: forward responses are bounded by \(2H\sqrt n\), the readout by
\(2Y\sqrt{n/\lambda}\), and backward responses by
\(2D_\ell Y\sqrt{n/\lambda}\), where \(\lambda=\gamma/m\).
Together with
\[
\|e(t)\|_2\le\sqrt mY e^{-\lambda t/2},
\]
this verifies absolute convergence of all integrals in the note.
Integration gives
\[
f_n(\infty,x)=\frac2m\int_0^\infty K_t(x,X)e(t)\,dt,\qquad
y=\frac2m\int_0^\infty K_t(X,X)e(t)\,dt.
\]
Multiplying the second identity by
\(K_0(x,X)K_0(X,X)^{-1}\) and subtracting proves equation (1) with its
stated sign. Its bracket is zero at \(t=0\).

## Constants and the cubic estimate

The input norm condition makes the population diagonal at each layer
independent of the training directions. Thus \(H,s,D_\ell,F\), and the
note's \(B\) depend only on activations and depth. The source includes
\(Q^{(0)}_{11}=1\), so \(H\ge1\), and its assumption \(m/\gamma\ge1\)
gives \(0<\lambda\le1\).

The explicit expression for \(F\) agrees with the source recursion:
\[
F_1=sD_1,\qquad
F_j=s(4H^2D_j+9F_{j-1}),\qquad
D_j=s(9s)^{L-j}.
\]
Iterating it yields
\[
F=F_L=s^2\left[(9s)^{2L-2}
       +4H^2\sum_{j=0}^{L-2}(9s)^{2j}\right].
\]
The displacement bound used in the note is precisely the source's
\(8FY^2\lambda^{-3/2}\) bound, and applies uniformly over the sphere.

The readout kernel difference obeys
\[
\left|\frac{h_t(x)^\top h_t(z)-h_0(x)^\top h_0(z)}n\right|
\le (2H+3H/2)\,8FY^2\lambda^{-3/2}
=28HFY^2\lambda^{-3/2}.
\]
Here \(h_t=h^{(L)}(t,\cdot)\). The first-layer hidden term is at most
\(4D_1^2Y^2/\lambda\), and the later terms sum to at most
\[
16H^2Y^2\lambda^{-1}\sum_{\ell=2}^L D_\ell^2.
\]
Since \(\lambda^{-1}\le\lambda^{-3/2}\), equation (2) follows with
exactly the note's
\[
B=28HF+4\left(D_1^2+4H^2\sum_{\ell=2}^LD_\ell^2\right).
\]

To check every factor of \(m\), temporarily put
\(b=BY^2\lambda^{-3/2}\) and
\(a(x)=K_0(x,X)K_0(X,X)^{-1}\). The initialized sphere bound gives
\[
\|a(x)\|_2
\le\frac{2}{\gamma}\sqrt m\,\frac{9H^2}{4}
=\frac{9H^2\sqrt m}{2\gamma}.
\]
The row and matrix differences are bounded by \(\sqrt m\,b\) and \(mb\),
respectively. Hence the bracket in equation (1) is bounded in Euclidean
norm by
\[
\sqrt m\,b\left(1+\frac{9H^2}{2\lambda}\right).
\]
The residual integral is
\(\int_0^\infty\|e(t)\|_2dt\le2\sqrt mY/\lambda\).
Multiplication by the flow prefactor \(2/m\) therefore gives
\[
\sup_{\|x\|=\sqrt d}|f_n(\infty,x)-f_{\rm RF}(x)|
\le4B\left(1+\frac{9H^2}{2\lambda}\right)
      Y^3\lambda^{-5/2},
\]
exactly equation (3).

The source's use of the small-label cap is consistent with this bound.
Its sufficient bootstrap inequality
\(Y\le\lambda/(8H\sqrt F)\) follows from the stronger stated cap, and its
stopped-flow estimates give strict operator, feature, and training-Gram
margins. The parameter-length estimate and exponential residual decay
justify convergence in parameters and interpolation. Nothing in the
checked endpoint argument calls for a stronger label restriction or an
input-rank assumption.

## Logical scope

Equation (3) is uniform in width, but does not decrease with width. For fixed
positive \(Y\), it cannot be subtracted from a comparator lower bound of
order \(Y/\sqrt n\) to obtain a positive asymptotic lower bound. It also
does not control the variance or covariance of the remainder.

The warning about a merely order-\(Y/\sqrt n\) bound for the difference of
remainders is correct: without a sufficiently small constant relative to
the comparator lower bound, or a separate covariance/nondegeneracy argument,
the two contributions could cancel. This is a missing proof obligation,
not evidence that they do cancel and not a counterexample to the endpoint
claim.

A scalar endpoint central limit theorem with positive variance at one fixed
separated query would already suffice for the requested supremum lower
bound. A functional central limit theorem, mentioned in the checked note,
is sufficient but stronger than needed.

## Superseded time-uniform clarification

An intermediate request briefly asked for a positive lower bound at every
training time. That different requirement is impossible because both
readouts are zero at time zero. Even after deleting time zero, at each fixed
finite width continuity of the readouts and uniform boundedness of the
features on a short time interval imply
\[
\sup_{\|v\|=1}|f_n(t,\sqrt d\,v)-\widetilde f_n(t,\sqrt d\,v)|
\longrightarrow0\quad(t\downarrow0).
\]
Thus a simultaneous positive lower bound for all \(t>0\), or marginal
probability lower bounds with one common width threshold for all \(t>0\),
cannot hold. A threshold depending separately on each positive time has
different quantifiers and is not refuted by that continuity argument alone.
The user restored the endpoint-only target immediately; this observation
does not answer or refute the restored question.
