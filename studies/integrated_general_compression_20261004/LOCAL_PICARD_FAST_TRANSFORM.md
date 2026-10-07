# Fast real-node integration transforms for local Picard setup

2026-10-06. Root-derived implementation refinement of the frozen real-node
Picard candidate. This changes only its exact arithmetic execution, not its
nodes, fixed-point iteration, continuous defect or retained source space.
The scientific inputs are `LOCAL_CONTINUATION_ALTERNATIVE.md` at SHA-256
`a41c246981d22abe002a5870934690ac254e2f427984661bfef048650f1a9e34`
and its cited source/quadrature/stability notes. No external FFT theorem is
needed: the finite identities and operation recurrence are proved below.

## 1. Choose a convenient degree without changing the proof

Let \(K_0\ge4\) be the sufficient degree from equation (23) of the
Picard candidate, and set, locally in this note,

\[
Q=2^{\lceil\log_2(K_0+1)\rceil},\qquad K=Q-1.
\tag{1}
\]

Thus \(K\ge K_0\) and \(K+1<2(K_0+1)\). The error expression
\((2K+2)2^{-K}\) decreases for \(K\ge1\), so the degree remains
sufficient. Recompute the prescribed iteration count with this \(K\).
The local-panel count, degree and iteration count remain respectively
\(O(\log(en)^{3/2})\), \(O(\log(en))\), \(O(\log(en))\)
at fixed admissible parameters and polynomial accuracy. The new local
letter \(Q\) is a transform length, not a feature Gram or source bound.

Write \(x_j=\cos\theta_j\), \(\theta_j=(2j+1)\pi/(2Q)\),
for the same Gauss--Chebyshev nodes, and let \(v_j\) be one scalar
component of the vector-field values there. The interpolant is

\[
p(x)=a_0+\sum_{k=1}^{Q-1}a_kT_k(x),\quad
a_0=\frac1Q\sum_jv_j,\quad
a_k=\frac2Q\sum_jv_j\cos(k\theta_j).
\tag{2}
\]

These formulas are exact by the discrete cosine orthogonality used in the
candidate's interpolation proof.

## 2. An explicit fast analysis and synthesis

Set an array of length \(4Q\) to zero, then assign

\[
y_{2j+1}=y_{4Q-(2j+1)}=v_j,\qquad 0\le j<Q.
\]

Its Fourier transform \(\widehat y_k=\sum_{s=0}^{4Q-1}
y_s e^{-2\pi i ks/(4Q)}\) obeys

\[
\widehat y_k=2\sum_{j=0}^{Q-1}v_j\cos(k\theta_j).
\]

Consequently (2) is recovered by
\(a_0=\widehat y_0/(2Q)\), \(a_k=\widehat y_k/Q\) for
\(1\le k<Q\). All final coefficients are real.

For completeness, a transform of even length \(M\) splits its defining
sum into even and odd input indices. Compute their length-\(M/2\)
transforms \(E_k,O_k\); then

\[
\widehat y_k=E_k+e^{-2\pi i k/M}O_k,\qquad
\widehat y_{k+M/2}=E_k-e^{-2\pi i k/M}O_k
\quad(0\le k<M/2).
\]

At every level there are \(O(M)\) real scalar operations, and there
are \(\log_2M\) levels down to length one. Thus the work is
\(O(M\log M)\), with \(O(M)\) live scratch by depth-first recursion
and reusable output buffers. The inverse transform has the identical
recursion with the conjugate signs and a final division by \(M\).
Geometric-sum orthogonality verifies that it is the inverse. Twiddle
factors need \(O(M)\) storage and elementary sine/cosine evaluations,
once for this common transform size; their scalar cost follows the
existing elementary-function convention.

Integrating (2) costs only \(O(Q)\) additional operations, using

\[
\int T_0(x)\,dx=T_1(x),\qquad
\int T_1(x)\,dx=T_2(x)/4,
\]
\[
\int T_k(x)\,dx=
\frac{T_{k+1}(x)}{2(k+1)}-\frac{T_{k-1}(x)}{2(k-1)}
\quad(k\ge2).
\tag{3}
\]

Differentiate the last identity using
\(T_k(\cos\theta)=\cos(k\theta)\) and the angle-addition identities
to verify it; the first two cases follow directly. Set the integration
constant so that the primitive is zero at \(x=-1\), evaluating
\(T_k(-1)=(-1)^k\) in \(O(Q)\) operations. Multiplication by
half the physical panel length and addition of the anchor give exactly
the next Picard polynomial, including its degree-\(Q\) coefficient.

For evaluating a Chebyshev polynomial with coefficients
\(b_0,\ldots,b_{Q-1}\) at these nodes, set Fourier coefficients
\(c_0=b_0\), \(c_k=c_{4Q-k}=b_k/2\) for \(1\le k<Q\),
with all other coefficients zero. The unnormalized inverse Fourier sum at
index \(2j+1\) is exactly \(\sum_{k=0}^{Q-1}b_kT_k(x_j)\).
Its computation therefore also costs \(O(Q\log Q)\).

The integrated polynomial may have a degree-\(Q\) term, but
\(T_Q(x_j)=\cos((2j+1)\pi/2)=0\) at all iteration nodes.
That term is retained in the stored polynomial and in its endpoint and
query evaluations, not discarded from the path. Its vanishing at the
iteration nodes is why the same transform length suffices for the next
vector-field evaluation. Endpoint evaluation uses \(T_k(1)=1\).
Arbitrary interior times use the three-term Chebyshev recurrence in
\(O(Q)\) work per parameter coordinate. No dense monomial conversion
or cubic preprocessing is needed.

Applying the preceding scalar transforms to every parameter coordinate
gives \(O(PK\log(2+K))\) work per Picard iteration, where
\(P=(L-1)n^2+n(d+1)\). Scratch stays \(O(PK)\): stream coordinates
through a reusable length-\(4Q\) transform buffer while retaining the
nodal and coefficient arrays. All complex arithmetic here is just an
implementation of real linear maps; activations are still evaluated only
at real arguments, using only values and first derivatives.

## 3. Complete revised cost, not just the transform cost

Use \(N_{\rm pan},I,K\) for the Picard panel, iteration and degree
choices, and \(N_t,N_x,p,H_{\rm harm},R_{\rm src},r,q\) for its
unchanged source/quadrature counts. With numerical big-O constants, a
complete non-activation work envelope is

\[
\begin{split}
O\big(&P+K\log(2+K)
 +N_{\rm pan}IPK[m+\log(2+K)] +PN_t(K+N_x)\\
 &+LnN_x(p+1)(N_t+H_{\rm harm})+\mathcal G_{\rm time}\\
 &+LnR_{\rm src}r+Lnr^3+Ln^2r+Lq^2r\big).
\end{split}
\tag{4}
\]

There are additionally

\[
O\big(Ln[mN_{\rm pan}IK+N_tN_x+m]\big)
\tag{5}
\]

real activation-value and first-derivative calls, plus the initialized
Gaussian draws. The \(m\) term allows exact initialized training
features. Add the chosen routines' actual work and scratch. Analyticity
alone implies neither a unit-cost scalar oracle nor a bit-complexity bound.

A sufficient peak-word count is

\[
O\big(PK+LmnK+LnN_x(p+1)+LnR_{\rm src}+Lq^2
 +m(d+1)+\mathcal G_{\rm memory}\big).
\tag{6}
\]

Every term of the original Picard envelope has been retained except its
direct \(K^2\) integration transforms and \(K^3\) transform setup,
which are replaced by the proved fast transforms. Thus (4) is not a
claim that projection, original-matrix images or coordinate selection
are free. Accuracy, complex continuation, global defect and exact
source-pair identities are unchanged because the computed finite sums
are unchanged in exact arithmetic.

## 4. Width asymptotics and comparison

Fix separately an admissible dataset, \(m,d,L,\gamma,Y\), activations
and confidence. Take the original \(T=32(m/\gamma)\log(en)\),
source tolerance \(1/n\), and a polylogarithmic selected width.
All asymptotic constants in this section may depend on those fixed
parameters; (4)--(6) do not hide them in their numerical cost constants.
The existing cutoffs and the proved Picard orders give a sufficient bound

\[
O\!\left(
P\{[m+\log\log(e^e n)]\log(en)^{7/2}
       +\log(en)^{3d/2+1}\}
 +Ln\log(en)^{9d/2+3}
 +\operatorname{polylog}(n)\right).
\tag{7}
\]

The last term consists only of fixed-dimensional scalar geometry and
polylogarithmic model assembly terms; their full forms remain in (4).
The \(n\)-proportional term covers the conservative selector and
coefficient transforms. For each fixed \(d\) it is eventually
dominated by the \(n^2\) terms. Thus for \(d\ge2\) the total
non-activation arithmetic simplifies to

\[
O\!\left(n^2\log(en)^{3d/2+1}\right)=n^{2+o(1)}.
\tag{8}
\]

For \(d=1\), a sufficient bound is
\(O(n^2\log(en)^{7/2}\log\log(e^e n))\).
The common peak-memory specialization is \(O(n^2\log(en))\)
words. These are eventual-width statements, not uniform bounds when
dimension, depth or data conditioning grow with width. With unit-cost
scalar activations the calls in (5) fit these arithmetic bounds; otherwise
they stay separately charged.

For the user's Euler benchmark, divide (4), including the actual scalar
and sampling costs, by \(mPT/h\). At fixed parameters with bounded-cost
scalar calls, (8) yields the sufficient ratio bound

\[
O\!\left(h\log(en)^{3d/2}\right)\quad(d\ge2),
\tag{9}
\]

and in dimension one
\(O(h\log(en)^{5/2}\log\log(e^e n))\).
Consequently every \(h=n^{-\alpha}\), fixed \(\alpha>0\), gives
a ratio tending to zero. This does not prove that Euler requires that
step, nor that setup beats a dense solver using the same high-order
integration algorithm. The statement is exactly the specified numerical
baseline comparison.
