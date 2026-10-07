# Counted evaluation of the small matrix functions

Date: 2026-10-06. Status: internally proved numerical sublemma, not a
decoder theorem or a review of the full current-state candidate.

## 1. Scope and computational contract

This note removes a matrix-function oracle from the finite noisy
two-orientation formulas. Its scientific inputs are the complete
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`, frozen SHA-256
`0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac`,
and the earlier counted-evaluation question in `RECOMPUTATION_SPACE.md`.
No external matrix-function algorithm is assumed. The proof below uses
only scalar series and elementary finite-precision matrix arithmetic.

For a real matrix \(A\), write \(\|A\|\) for its Euclidean operator norm
and \(\|A\|_F\) for its Frobenius norm. A symmetric positive semidefinite
matrix is abbreviated PSD. For symmetric \(A\), \(A_+\) is its positive
part: its eigenvalues are replaced by their positive parts, in the same
orthonormal eigenbasis. All output errors below are Frobenius errors.

Small input matrices are actually read and stored. A dyadic input entry
has a finite signed binary description; input fractional precision is
denoted \(p\). The input description, matrix storage, loop counters,
accumulators, arithmetic scratch, and output storage all count toward
peak workspace. Repeated evaluation takes time, not free memory.

If an input is specified by a precision interface rather than by a
dyadic array, that interface must return entry approximations with a
certified absolute error and counted workspace. Its cost is additional
to the bound below. In particular, the present lemma neither makes the
original activation computable nor provides free access to the original
dense initialization. Exact-real activation primitives and finite-bit
activation precision interfaces remain distinct contracts.

The same requirement applies to data, a passive query, and physical
time whenever they enter matrix coefficients through a scalar program:
the interface must supply the precision selected by that program's
proved sensitivity bound, and its storage and working memory count.
This lemma supplies no free exact-real input digits. It adds no new
restriction to the activation class in an exact-real primitive model;
its finite-bit conclusion is conditional on the stated interfaces.

The complete notation skill at its required custom filesystem path was
unavailable because of read permission. The available rigorous-proof
and research skills, the supplied canonical-notation rules, and the
previously read maintained notation contract were applied instead.

## 2. Small-matrix theorem

Let \(r\geq1\), \(0<\varepsilon\leq1\), \(M\geq1\), and \(0<a\leq1\).
The bounds \(M,a,\varepsilon\) may be replaced by outward dyadic bounds,
at a constant-factor change. There are explicit deterministic algorithms
with the following properties.

1. Given a symmetric dyadic \(r\times r\) matrix \(A\) with
   \(aI\preceq A\preceq MI\), compute symmetric approximations to
   \(A^{-1}\) and \(A^{1/2}\), each with error at most \(\varepsilon\).
2. Given a symmetric dyadic \(A\) with \(\|A\|\leq M\), compute a
   symmetric dyadic PSD matrix \(P\) such that
   \(\|P-A_+\|_F\leq\varepsilon\).
3. Compose these operations, additions, products, transpose,
   symmetrization, and scalar divisions in an explicitly given finite
   arithmetic graph. Suppose its exact inputs and intermediate values
   have a known magnitude bound \(U\geq1\), every inverse and square
   root has a known positive spectral gap at least \(\alpha\leq1\),
   and every scalar divisor has absolute value at least \(\alpha\).
   A graph of \(N\) operations can be evaluated to error
   \(\varepsilon\) in space polynomial in

   \[
   N+r+p+\log(2+U)+\log(1/\alpha)+\log(1/\varepsilon),
   \tag{1}
   \]

   in addition to its counted input interfaces and instruction
   description. A supplied operator-dimension bound \(r\) includes
   Kronecker matrices, not just the original source Grams.

For the first two operations alone, a sufficient maximum arithmetic-word
length is

\[
 w\leq C\left[p+\log(r+1)+\log(2+M)
                 +\log(1/a)+\log(1/\varepsilon)+1\right],
 \tag{2}
\]

where the positive-part operation omits the original input-gap term.
Its internally introduced gap is already covered by
\(\log(r+1)+\log(1/\varepsilon)\).
Their peak space is at most

\[
 C(r^2w+w^2)
 \tag{3}
\]

bits, using elementary integer arithmetic. The constants are absolute.
Runtime can be exponentially large in the logarithmic conditioning
parameters. No polynomial-time claim is made.

If the entries of \(A\) are not already dyadic, the sufficient input
precision is also polynomial in the parameters in (2); the explicit
perturbation bounds are given in Section 5.

## 3. Inverse and square root by contraction series

Replace the upper bound by a power of four \(m\geq\max(1,M)\), with

\[
 m<4\max(1,M),\qquad \sqrt m\text{ a power of two},
\]

and replace the lower bound by a power of two
\(0<\underline a\leq a<2\underline a\).
For the exact dyadic input define

\[
 X=I-A/m,\qquad q=1-\underline a/m<1.
 \tag{4}
\]

Then \(0\preceq X\preceq qI\). Scaling by \(m\) is an exact binary
shift, so \(X\) is stored exactly, not recomputed with a different
precision at every iteration.

The inverse series is

\[
 A^{-1}=m^{-1}\sum_{k=0}^{\infty}X^k.
 \tag{5}
\]

For the square root use

\[
 A^{1/2}=\sqrt m\left[I-\sum_{k=1}^{\infty}b_kX^k\right],
 \qquad
 b_1=\frac12,\quad
 b_{k+1}=b_k\frac{2k-1}{2k+2}.
 \tag{6}
\]

The scalar binomial series for \(\sqrt{1-x}\) gives \(b_k>0\) and
\(\sum_{k\geq1}b_k=1\). For completeness, the recurrence is obtained
by comparing adjacent coefficients of \((1-x)^{1/2}\). The power series
solves \(y^2=1-x\), with \(y(0)=1\), on \(|x|<1\); positivity of the
\(b_k\) and monotone convergence as \(x\uparrow1\) give their total
mass one. The finite-dimensional spectral theorem then proves (5)–(6).

Truncating both series before power \(D\) gives operator-norm tails

\[
 \left\|A^{-1}-m^{-1}\sum_{k<D}X^k\right\|
 \leq\underline a^{-1}q^D,
 \qquad
 \left\|A^{1/2}-\sqrt m
       \left[I-\sum_{1\leq k<D}b_kX^k\right]\right\|
 \leq\sqrt m\,q^D.
 \tag{7}
\]

To obtain a Frobenius tail at most \(\varepsilon/4\), choose integers

\[
 K=\left\lceil\log_2
 \frac{8r(1+\sqrt m)}{\underline a\varepsilon}\right\rceil,
 \qquad
 D=(m/\underline a)K.
 \tag{8}
\]

The ratio \(m/\underline a\) is an integer power of two. Since
\(q^D\leq\exp(-D\underline a/m)=e^{-K}\leq2^{-K}\), (7) implies the
claim, using \(\|B\|_F\leq\sqrt r\|B\|\). In particular,

\[
 \log(D+1)\leq C\left[
 \log(r+1)+\log(2+M)+\log(1/a)+\log(1/\varepsilon)+1\right].
 \tag{9}
\]

Thus an enormous degree still has a short loop counter.
The ceiling in (8) is computable by binary comparisons on the dyadic
inputs; no logarithm oracle is needed.

### Rounded evaluation does not cost \(D\) bits

Use a fixed binary fractional grid with step \(u=2^{-b}\). Let
\(\widehat P_0=I\), and form \(\widehat P_{k+1}\) by multiplying
\(\widehat P_k\) by the exact fixed \(X\), symmetrizing, and rounding
each scalar operation with absolute error at most \(u\). A matrix
product and symmetrization have local Frobenius error at most

\[
 \mu=C r^2u.
\]

Symmetrization is Frobenius nonexpansive, and the exact comparison power
\(X^k\) is symmetric. Therefore

\[
 \|\widehat P_k-X^k\|_F\leq k\mu,
 \tag{10}
\]

by induction from
\(\|(\widehat P_k-X^k)X\|_F\leq\|\widehat P_k-X^k\|_F\).
Choosing \(D\mu\leq1\) keeps every computed power's operator norm at
most two. It is essential here that \(X\) is fixed and exactly a
contraction; no general unconstrained matrix-power stability claim is
being used.

Compute the coefficient recurrence in (6) on the same grid. Its exact
multiplicative factor belongs to \([0,1]\). Rounding that factor and the
subsequent multiplication introduces at most \(Cu\) local error while
the computed coefficient stays bounded by two. Induction gives

\[
 |\widehat b_k-b_k|\leq Cku,
 \tag{11}
\]

provided \(CDu\leq1\). The numerator and denominator in the factor
use only \(O(\log(D+1))\) bits. No exponentially long rational
coefficient numerator is retained.

Accumulate the inverse and square-root sums while retaining only the
current power, current coefficient, and a constant number of matrices.
Equations (10)–(11), the triangle inequality, and
\(\sum b_k\leq1\) give the deliberately generous bound

\[
 \text{total Frobenius rounding error}
 \leq C r^3(1+\sqrt m)D^2u.
 \tag{12}
\]

This includes scalar summation, coefficient products, final scaling,
and final symmetric rounding. For example, the inverse power errors
sum to at most \(m^{-1}\mu D^2\), while the square-root coefficient
errors contribute at most
\(C\sqrt{rm}\,u\sum_{k<D}k\). These are covered by (12).

Choose

\[
 b\geq p+\log_2m+C,
 \qquad
 2^{-b}\leq
 \frac{\varepsilon}{C r^3(1+\sqrt m)D^2}.
 \tag{13}
\]

The first condition retains \(X\) exactly. The second makes all errors
in (10)–(12) small and gives total output error below
\(\varepsilon\), including (7). By (9), \(b\) has the size in (2).

Exact partial inverse sums have norm at most \(m/\underline a\), and
exact square-root partial bracket sums have norm at most one. The
computed quantities remain within one of their exact counterparts
after (13) is tightened by an absolute factor. Products and intermediate
dot-product sums need only
\(O(\log(r+1)+\log m+\log(1/\underline a))\) integer bits.
The loop counter and coefficient divisors need \(O(\log D)\) bits.
All these are included in \(w\).

Schoolbook signed integer multiplication and long division can be
performed with \(O(w^2)\) scratch bits; the constant number of matrix
arrays uses \(O(r^2w)\) bits. This proves (3). A sufficient time bound
is \(O(D r^3\operatorname{poly}(w))\); only its finiteness and space
bound are used here.

## 4. PSD projection without an eigenvector oracle

For a symmetric input \(A\), choose a positive dyadic number \(v\) with

\[
 \frac{\varepsilon}{64r}<v\leq\frac{\varepsilon}{32r},
 \qquad h=v^2.
 \tag{14}
\]

The symmetric matrix

\[
 B=A^2+hI
 \tag{15}
\]

can be formed exactly from dyadic \(A\): each entry is a sum of \(r\)
dyadic products. This doubles fractional precision and adds
\(O(\log(r+1))\) integer bits, both covered by (2). It satisfies

\[
 hI\preceq B\preceq(M^2+h)I.
\]

Apply Section 3 with lower gap \(h\), obtaining a symmetric dyadic \(Y\)
such that \(\|Y-B^{1/2}\|_F\leq v\), including its final rounding.
Return the exactly dyadic matrix

\[
 P=\frac{A+Y}{2}+vI.
 \tag{16}
\]

Only binary shifts and exact additions are needed in (16).
On each eigenvalue \(\lambda\) of \(A\),

\[
 0\leq\frac{\lambda+\sqrt{\lambda^2+h}}2-\max(\lambda,0)
 \leq\frac{\sqrt h}{2}=\frac v2.
 \tag{17}
\]

Thus \((A+B^{1/2})/2\succeq0\), and the error in \(Y\) has operator
norm at most \(v\). Equation (16) implies \(P\succeq(v/2)I\), so its
PSD property is certified, not inferred from a nearly PSD floating-point
array. Moreover,

\[
 \|P-A_+\|_F
 \leq\frac{\sqrt r\,v}{2}+\frac v2+\sqrt r\,v
 \leq2rv<\varepsilon.
 \tag{18}
\]

The internal gap obeys
\(\log(1/h)=O(\log(r+1)+\log(1/\varepsilon))\).
Therefore the positive-part algorithm obeys (2)–(3) without a gap for
the original \(A\). There is no discontinuous eigenvector selection.

## 5. Input approximation and noncommuting perturbations

Suppose \(A\) is supplied through an entry-precision interface, and
the symmetric dyadic array \(A_0\) satisfies
\(\|A_0-A\|_F\leq\tau\). Entry error at most \(\tau/r\) suffices.

For PSD projection, the Frobenius estimate is

\[
 \|(A_0)_+-A_+\|_F\leq\tau.
 \tag{19}
\]

Indeed, the positive part is the metric projection onto the closed
convex cone of PSD matrices. Its variational inequality, applied in
both directions to the two projections and added, gives
\(\|P-Q\|_F^2\leq\langle P-Q,A_0-A\rangle_F\), proving (19).
The projection formula itself follows by diagonalizing \(A\) and
minimizing the Frobenius distance over PSD matrices.

If \(A\succeq aI\) and \(\tau\leq a/2\), then

\[
 A_0\succeq(a/2)I,
 \qquad
 \|A_0^{-1}-A^{-1}\|_F\leq2a^{-2}\tau.
 \tag{20}
\]

The latter uses the exact identity
\(A_0^{-1}-A^{-1}=A_0^{-1}(A-A_0)A^{-1}\).
For square roots, put \(Z=A_0^{1/2}-A^{1/2}\). Even when the two
matrices do not commute,

\[
 A_0^{1/2}Z+ZA^{1/2}=A_0-A.
\]

Taking its Frobenius inner product with \(Z\) proves

\[
 \|A_0^{1/2}-A^{1/2}\|_F
 \leq\frac{\tau}{\sqrt{a/2}+\sqrt a}
 \leq\frac{\tau}{\sqrt a}.
 \tag{21}
\]

For example, \(\tau\leq\varepsilon a^2/16\), followed by numerical
error at most \(\varepsilon/2\), suffices simultaneously for (20)–(21)
when \(a,\varepsilon\leq1\). Its required entry precision is
\(O(\log(r+1)+\log(1/a)+\log(1/\varepsilon))\) fractional bits.
Use lower gap \(a/2\) and upper norm bound \(M+\tau\) for the rounded
input \(A_0\).
For positive parts, take \(\tau\leq\varepsilon/2\).
These requirements count the actual matrix-input interface.

## 6. Radial caps, Sylvester equations, and finite graphs

### Radial Frobenius cap

The exact cap of a symmetric PSD \(G\), at radius \(C_0\geq1\), is

\[
 \mathcal R_{C_0}(G)
 =\min\{1,C_0/\|G\|_F\}\,G,
 \qquad \mathcal R_{C_0}(0)=0.
 \tag{22}
\]

For dyadic \(G\), compute \(\|G\|_F^2\) exactly and compare it with
\(C_0^2\), taking \(C_0\) dyadic. Below the threshold return \(G\)
exactly. Above it, put \(s=\|G\|_F>C_0\). The scalar square root is
gapped by \(C_0\geq1\), so Section 3 with \(r=1\) supplies a dyadic
upper bound \(t\) with

\[
 s\leq t\leq s+2\eta_0.
\]

For example, compute the square root to certified error \(\eta_0\)
and add the dyadic error bound. Compute \(C_0/t\) to absolute error
\(\zeta\), obtaining a dyadic \(c_0\), and set

\[
 c=\max\{0,c_0-\zeta\}.
\]

Then \(0\leq c\leq C_0/t\leq C_0/s\). Return \(cG\), performing this
last dyadic multiplication exactly and retaining its full finite
precision. It adds input word lengths, rather than introducing any
entrywise rounding. The returned matrix is therefore exactly PSD
and satisfies the exact bound \(\|cG\|_F\leq C_0\).

If \(U_F\geq s\) is a known Frobenius bound, its error relative to
(22) is at most

\[
 \|cG-(C_0/s)G\|_F
 \leq 2\eta_0+2\zeta U_F.
\]

Choose \(\eta_0\leq\varepsilon/8\) and
\(\zeta\leq\varepsilon/(8U_F)\). Their required logarithmic precision
is covered by the existing norm and tolerance parameters. Thus PSD
projection with the tiny buffer in (16), followed by this conservative
dyadic scaling, preserves nonnegativity and the cap, not just proximity
to the corresponding exact projection.

Metric projection onto the Frobenius ball is nonexpansive, so composing
the approximations to positive part and radial cap adds their errors
without a conditioning singularity at the cap's branch boundary.

### Sylvester equations

If \(S\succeq aI\), \(T\succeq bI\), then the equation

\[
 SE+ET=H
\]

is a positive definite linear system on vectorized \(E\), with matrix
\(I\otimes S+T^T\otimes I\) and gap \(a+b\). Construct that small
Kronecker matrix explicitly and use its inverse from Section 3.
An \(s\times t\) unknown produces an \(st\times st\) system; storing
its inverse costs \(O(s^2t^2w)\), not \(O((s+t)^2w)\). This increased
dimension is still counted and polynomial in the transcript length.

### Error propagation through an explicit graph

On bounded sets, addition, multiplication, transpose and
symmetrization are locally Lipschitz, with constants polynomial in
dimension and the magnitude cap. Equations (19)–(21) provide the
necessary matrix-function constants. Scalar reciprocal has derivative
bounded by the inverse square of its divisor gap. Thus a graph of \(N\)
operations with magnitude bound \(U\) and positive gaps \(\alpha\)
has a common one-step error-amplification bound

\[
 L=[C(r+1)(U+1)(1+\alpha^{-1})]^C\geq2.
 \tag{23}
\]

Enlarge \(U\) by one and shrink certified gaps by a factor of two for
the numerical neighborhood. If every elementary numerical subroutine
and every input approximation has absolute error at most

\[
 \eta\leq
 \frac{\min\{\varepsilon,\alpha,1\}}
      {C(N+1)L^{N+1}},
 \tag{24}
\]

a direct induction over the graph bounds each accumulated error by
\(\eta\sum_{j\leq N}L^j\). In particular all approximate inverse and
square-root inputs retain at least half their exact gap, and the final
error is at most \(\varepsilon\). At interfaces that are theoretically
symmetric, symmetrize before invoking a spectral subroutine.

The logarithm of the required local precision is at most

\[
 C\left[\log(1/\varepsilon)+\log(1/\alpha)
 +(N+1)\log\{C(r+1)(U+1)(1+\alpha^{-1})\}\right].
 \tag{25}
\]

Applying Sections 3–4 at precision (24), and retaining at most \(N\)
small matrices if convenient, proves the polynomial-space graph claim.
For this composition, fix one common operand grid in advance, with
fractional precision

\[
 p_*=
 O\!\left(\log(r+1)+\log(U+1)+\log(1/\alpha)
                    +\log(1/\eta)+1\right).
\]

Round each matrix operand to that grid before entering its numerical
subroutine, charging this error to the local budget in (24). This is
not a recursive request for increasingly many input digits. Gapped
inputs retain their half-gap. If an operand must be exactly PSD for
the radial-cap construction, symmetric entry rounding changes its
operator norm by at most \(r2^{-p_*}\); adding
\(r2^{-p_*}I\) restores PSD and changes the Frobenius error by only
a further polynomial-in-\(r\) multiple of \(2^{-p_*}\). Increase \(p_*\)
by \(O(\log(r+1))\) to include that buffer in the same budget.

Exact products in (15) and in the final conservative cap multiply
word lengths only by a constant within their respective subroutines.
Their outputs are rounded to the fixed operand grid before later
subroutines, with the preceding gap or PSD safeguards. They are not
fed through an unbounded chain of exact dyadic products. Thus the
precision does not double \(N\) times. A final PSD/capped output is
retained at its finite subroutine precision, without a later
uncertified entrywise rounding.

This is conservative; reuse of registers may reduce space, but is not
needed. The graph's instruction encoding and its numerical cap/gap
certificates count as part of the input.

## 7. Application to the noisy two-orientation coefficient formulas

The audited transcript note uses PSD source Grams \(Q,K\), the noise
variance \(\delta=\sigma^2>0\), and small inverses such as

\[
 (\delta I+Q)^{-1},\qquad
 (\delta I+K)^{-1},\qquad
 (\delta I+K\otimes I+I\otimes Q)^{-1}.
\]

Their spectral gaps are at least \(\delta\). Its covariance formula
has \(F\succeq0\), \(\beta\geq\delta\), and denominator

\[
 (\delta I+F)^{1/2}+\sqrt\beta I\succeq2\sigma I.
\]

All these functions are covered by the present algorithms. A numerical
approximation to \(F\) need not remain exactly PSD merely because its
exact formula is PSD; symmetrization and error below \(\delta/4\)
give a sufficient certified gap for the shifted square root. The same
gap margin is used for all approximate intermediate matrices. Complete
typed-Gram projection can instead use the PSD-buffered procedure of
Section 4 before block extraction.

For at most \(R\) source vectors in each orientation, the largest
Kronecker dimension is at most \(R^2\). The covariance and posterior
mean use a finite graph with size polynomial in \(R\), not in \(n\).
If every amplitude is at most \(\exp(\operatorname{polylog}n)\), every
positive gap is at least \(\exp(-\operatorname{polylog}n)\), the target
error is at least \(\exp(-\operatorname{polylog}n)\), and \(R\) is a
fixed absolute power of \(\log n\), then (1) is an absolute-polylogarithmic
workspace bound. The exponent is determined by the supplied graph-size
and input-interface bounds, not by an uncounted matrix-function oracle.

The numerical result does not establish those amplitude, gap,
transcript-length, or activation-interface hypotheses for an entire
neural decoder. It does not identify an aggregate derivative trace with
individual causal coefficients, prove a late-query law, replay training,
or eliminate any remaining probabilistic approximation obligation. It
only supplies a complete counted implementation once the specified
small coefficient matrices and their certified bounds are available.
