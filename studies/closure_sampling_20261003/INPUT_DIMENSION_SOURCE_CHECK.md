# Check of the dimension obstruction for the current source interface

2026-10-04. Coordinator reconstruction of the complete frozen
DIMENSION_FREE_REPRESENTATION_ROUTE.md, SHA-256
`daa25ee23fb36c87e06e8f6e1102d21eef2d6c5e836695ea07a88259e5b92ec9`.
This is an internal check, not an isolated promotion review. The coordinator
had developed a related conditional-symmetry idea before receiving this
report; the harmonic lower-bound argument was new in the report. No prior
verdict or other study was used to check that argument.

## Exact claim checked

Fix input dimension d>=2. Let the rows g_i of the initialized first-layer
matrix be independent standard Gaussian vectors in R^d and put
h_n(v)_i=sin(g_i^T v), for v on the unit sphere. With probability tending
to one, every initialization-dependent linear subspace S of R^n that
approximates these vectors with uniform normalized Euclidean error at
most C/sqrt(n) has dimension at least

\[
 c_d\left(\frac{\log n}{\log\log(en)}\right)^{d-1}.
\]

The source interface in the existing compression proof requires a stronger
coordinatewise error n^-1, so it is covered. Sine is bounded and holomorphic
on every fixed horizontal strip, hence belongs to the theorem's activation
class. The result concerns source vectors, not the trained scalar output.

## Reconstruction

The Gaussian identity E cos(g^T a)=exp(-||a||^2/2), obtained by completing
the square in the Gaussian Fourier integral, gives
K(v,u)=E sin(g^T v)sin(g^T u)=exp(-1)sinh(v^T u).
Every monomial kernel (v^T u)^j is positive semidefinite through its tensor
feature v^{tensor j}. The harmonic spaces of different degrees are
orthogonal; contraction of trace-free symmetric tensors proves this
directly and gives the scalar action of each monomial kernel.

For a degree-j homogeneous harmonic polynomial p, the jth monomial term
acts by

\[
 \int (v^\top u)^j p(u)\,d\sigma(u)
 =\frac{j!}{d(d+2)\cdots(d+2j-2)}p(v).
\]

Indeed, in the Gaussian product of (v^T G)^j and p(G), only the j!
pairings joining a tensor index to a v factor survive. All tensor-internal
pairings vanish by the trace-free condition. Gaussian radial integration
divides by E||G||^{2j}=d(d+2)...(d+2j-2). This verifies normalization
against probability surface measure, including d=2.

On the direct sum E_J of odd harmonic degrees at most J, the covariance
therefore dominates a_J I with a_J=exp(-1)(d+2J)^(-J). The dimension
D_J is at least c_d J^(d-1), by subtracting degree-(j-2) from degree-j
homogeneous polynomial dimensions and summing odd degrees. For d=2 each
positive harmonic degree contributes two dimensions. Parity removes only
a fixed fraction of directions; it does not change the exponent.

Let b_i be the coefficients of sin(g_i^T v) in an orthonormal basis of
E_J. Bessel gives ||b_i||^2<=1 independently of D_J. Consequently the
empirical coefficient covariance C_n obeys

\[
 E\|C_n-E C_n\|_F^2\le n^{-1},\qquad
 P\{C_n\not\succeq a_J I/2\}\le 4/(n a_J^2).
\]

This calculation uses independence of the rows but does not assume that
the subsequently chosen approximating subspace is independent of them.
Choose J=floor(log(n)/(8 log log(en))). At fixed d and sufficiently
large n, a_J>=n^(-1/4), and the event has probability at least
1-4n^(-1/2). It controls all subspaces simultaneously.

For the n-by-D_J coefficient matrix B and an orthogonal projection P_S,
integrating the squared feature residual over the sphere gives

\[
 \sup_v n^{-1}\|(I-P_S)h_n(v)\|^2
 \ge n^{-1}\|(I-P_S)B\|_F^2
 \ge (D_J-\dim S)_+ a_J/2.
\]

The first inequality is vector-valued Bessel and integration. The second
uses the D_J singular values squared of B/sqrt(n), all at least a_J/2:
a rank-R orthogonal projection removes at most R such directions.
If dim S<D_J, the lower bound n^(-1/4)/2 contradicts C^2/n.
This proves the claimed result without an external spectral theorem beyond
finite-dimensional diagonalization.

## Boundary of the conclusion

For any fixed exponent p independent of dimension, choosing fixed d>p+1
makes this source lower bound larger than C_d log^p(n). It rules out
removing dimension from the exponent solely by improving the linear basis
or sampler while retaining the current whole-feature approximation
interface. It does not determine the optimal exponent, force quadratic
storage for every representation, or give a lower bound for arbitrary
autonomous learned predictors. In particular f_n(0,v)=0 because w_0=0;
the output does not inherit this initial hidden-feature obstruction.

The report's training-span identity was also reconstructed. The exact
gradient update gives A(t)P_{V^perp}=A_0P_{V^perp}, where V spans the
training inputs. Orthogonal Gaussian projections make this passive block
independent of the entire training path. Conditional output means depend
on a query only through P_V v and ||P_{V^perp}v||. The chain rule gives
||grad_G f_n||_F<=C_data/sqrt(n) on the stated training-parameter event,
so the proved conditional pointwise variance is O(1/n). This does not
interchange a supremum over queries or training time with expectation.

**Verdict:** the source-space lower bound and conditional identities pass
this complete internal reconstruction. The uniform-output and autonomous
conditional-mean constructions remain open exactly as stated by the
author. They are not promoted to impossibility or compression theorems.
