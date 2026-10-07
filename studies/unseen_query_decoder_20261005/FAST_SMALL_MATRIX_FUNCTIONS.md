# Polynomial-time small-matrix operations for the query circuit

2026-10-06. Author proof, awaiting independent reconstruction. This removes
one source of excessive decoder time, not the high-dimensional query
integral. The scientific input is the complete
[counted small-matrix interface](SMALL_MATRIX_FUNCTION_EVALUATION.md).
No additional assumption on neural activations, labels, or data is used.

## 1. Claim and scope

Let a symmetric dyadic matrix \(A\) have dimension \(r\), input
fractional precision \(p\), and
\(aI\preceq A\preceq MI\), where \(0<a\le1\le M\).
Let \(0<\varepsilon\le1\). Its inverse and positive square root
can be approximated to Frobenius error \(\varepsilon\) in bit time
and space bounded by universal polynomials in

\[
r+p+\log(2+M)+\log(1/a)+\log(1/\varepsilon).
\tag{1}
\]

The positive part of a symmetric dyadic matrix with norm at most \(M\)
has the same conclusion without an original lower spectral gap. The
output can be certified exactly positive semidefinite. Small Sylvester
equations, conservative radial caps, and the finite coefficient graphs
in the existing interface consequently have polynomial time as well as
polynomial space in their counted dimensions, instruction counts and
logarithmic bounds.

This is a replacement for the previous Neumann/binomial implementation,
whose truncation degree could grow like the condition number itself.
It preserves an absolute-polylogarithmic workspace class when inserted
into the decoder; no claim is made here to preserve an optimized numerical
space exponent. Original activation/input evaluation costs remain separate.

## 2. Exact rational inversion has polynomial bit cost

Clear the common dyadic denominator. Every entry of the resulting integer
matrix has at most
\(C[p+\log(2+M)]\) bits. A determinant of order at most \(r\)
is a sum of at most \(r!\) products of at most \(r\) such entries.
Its bit length is therefore at most

\[
C r[p+\log(2+M)+\log(r+1)].
\tag{2}
\]

Compute determinants by rational Gaussian elimination with exact nonzero
pivot search, swapping rows as needed and reducing fractions after each
arithmetic operation. If no pivot exists, the determinant is zero. At
any stage with invertible pivot block \(B\), each remaining Schur entry
equals the determinant of its bordered block divided by \(\det B\):

\[
d-c^TB^{-1}e
=\frac{\det\begin{pmatrix}B&e\\c^T&d\end{pmatrix}}{\det B}.
\]

This identity follows by left multiplication of the bordered block by
\(\begin{psmallmatrix}I&0\\-c^TB^{-1}&1\end{psmallmatrix}\), whose
determinant is one. Thus the reduced numerator and denominator of every
Schur entry satisfy (2); intermediate multiplication, subtraction and
division before reduction enlarge that bound by only a constant factor.
The product of completed pivots is a leading minor, up to the recorded
row-swap sign, and has the same bound. Integer arithmetic, long division
and the Euclidean greatest-common-divisor algorithm take polynomial bit
time and space in these lengths. For the latter, every two remainder
steps at least halve the larger positive argument, so the number of long
divisions is linear in its bit length.

Compute the determinant and all cofactors by this procedure, then use
the adjugate formula for the inverse. There are at most \(r^2+1\)
determinant calculations, each with \(O(r^3)\) rational operations.
The total cost is polynomial. Since \(A\) is positive definite, its
determinant is nonzero. Round the resulting exact rational entries to a
common grid with error at most \(\varepsilon/r\) per entry, using
identical rounded values in transposed positions. This gives the desired
Frobenius error. Exact rational inversion itself requires no reciprocal
gap-sized number of iterations.

This deliberately slow polynomial algorithm suffices. Faster matrix
factorizations are unnecessary for the claim.

## 3. Square root by a short Newton iteration

Replace \(M\) by a dyadic power of two upper bound within a factor of
two; retain the notation \(M\). Define the exact reference iteration

\[
X_0=MI,\qquad X_{j+1}=\tfrac12(X_j+AX_j^{-1}).
\tag{3}
\]

Every exact \(X_j\) commutes with \(A\). For an eigenvalue
\(\lambda\in[a,M]\), its scalar iterate starts at
\(x_0=M\ge\sqrt\lambda\). If \(x\ge\sqrt\lambda\), then

\[
\frac{x+\lambda/x}{2}-\sqrt\lambda
=\frac{(x-\sqrt\lambda)^2}{2x}
\le\frac{x-\sqrt\lambda}{2}.
\tag{4}
\]

Induction proves \(aI\preceq\sqrt A\preceq X_j\preceq MI\)
and
\(\|X_j-\sqrt A\|_F\le\sqrt r\,M2^{-j}\).
Choose the integer

\[
J=\left\lceil\log_2(8rM/\varepsilon)\right\rceil.
\tag{5}
\]

This is only logarithmically many iterations. The weaker halving bound
already suffices; no quadratic-convergence estimate is needed.

### Rounded iterates need not commute

The actual algorithm symmetrizes every result and rounds it to a common
dyadic grid. We do not assume the rounded matrices commute with \(A\).
Put

\[
F(X)=\tfrac12\operatorname{sym}(X+AX^{-1}),
\qquad \operatorname{sym}(B)=(B+B^T)/2.
\]

If a symmetric \(X\) has Frobenius distance at most \(a/4\) from
the corresponding exact \(X_j\), then \(X\succeq(a/2)I\).
The inverse difference identity gives

\[
\|X^{-1}-X_j^{-1}\|_F\le2a^{-2}\|X-X_j\|_F.
\]

Consequently

\[
\|F(X)-F(X_j)\|_F
\le (\tfrac12+Ma^{-2})\|X-X_j\|_F.
\tag{6}
\]

Choose the smallest power of two \(K\ge2+2M/a^2\), with a
logarithmic-size description, and choose the smallest nonnegative grid
precision \(b\) satisfying

\[
r2^{-b}J K^J\le\min\{a/4,\varepsilon/4\}.
\tag{7}
\]

At each step use Section 2 to invert the current dyadic iterate exactly
as a rational matrix, evaluate \(F\) by rational arithmetic, and round
symmetrically to that grid. This has local Frobenius rounding error at
most \(r2^{-b}\). The recurrence
\(e_{j+1}\le Ke_j+r2^{-b}\), \(e_0=0\), proves
\(e_j\le r2^{-b}J K^J\) for all \(j\le J\).
This both verifies the positive-gap premise of each next inverse and
bounds final rounding error by \(\varepsilon/4\). Equations (4)--(5)
bound the exact-iteration error by \(\varepsilon/8\).

The needed precision satisfies

\[
b\le C\bigl[\log(r+1)+\log(1/a)+\log(1/\varepsilon)
 +J\{\log(2+M)+\log(1/a)+1\}\bigr].
\tag{8}
\]

This is polynomial in (1). The input matrix \(A\) keeps its original
finite representation. Each current iterate is reset to the same grid,
so its precision does not double at every step. Its norm stays below
\(M+1\). Exact rational inversion and multiplication at that step use
only polynomially many bits in \(r,p,b,\log(2+M)\), by Section 2.
With \(J\) given by (5), the complete square-root computation therefore
has polynomial bit time and space. No exact matrix-function oracle or
commutativity assumption on rounded iterates was used.

## 4. Positive parts, caps, Sylvester systems and composition

For symmetric \(A\) with \(\|A\|\le M\), use the existing
positive-part construction. Choose positive dyadic
\(\varepsilon/(64r)<v\le\varepsilon/(32r)\); form
\(B=A^2+v^2I\) exactly, and compute a symmetric dyadic \(Y\) with
\(\|Y-\sqrt B\|_F\le v\) by Section 3. Then

\[
P=(A+Y)/2+vI
\]

is exactly dyadic, satisfies \(P\succeq(v/2)I\), and has
\(\|P-A_+\|_F\le2rv<\varepsilon\). The scalar eigenvalue
inequality proving this is
\(0\le(\lambda+\sqrt{\lambda^2+v^2})/2-\max(\lambda,0)\le v/2\).
The new spectral gap is \(v^2\), so its logarithmic reciprocal is
\(O(\log(r+1)+\log(1/\varepsilon))\). Section 3 remains polynomial
in the original parameters, without an original gap for \(A\).

The conservative radial-cap algorithm in the existing interface only
adds scalar roots, rational arithmetic and exactly stored dyadic scaling.
Replacing its root routine by Section 3 preserves its PSD and exact-cap
guarantees in polynomial time. Sylvester equations are vectorized into
their counted positive Kronecker systems and solved by Section 2; all
Kronecker entries and increased dimensions count.

For a coefficient graph of \(N\) operations, retain the existing common
operand grid and local error allocation. Its logarithmic local accuracy
is at most a polynomial in \(N\), the matrix dimension, the logarithms
of amplitude/inverse-gap bounds and the requested final accuracy.
Input rounding, symmetric interfaces, PSD buffers and half-gap margins
are unchanged. Applying Sections 2--3 at those requested local tolerances
therefore yields polynomial time and space for the full matrix graph.
There is no chain of exact rational outputs passed through arbitrarily
many macros without resetting to the prescribed dyadic operand grid.

## 5. What this improves in the decoder, and what it does not

At any fixed Fourier quadrature point, the small conditioning-matrix
arithmetic can now be performed in polynomial time in its description
and logarithmic accuracy. The noise gap may be exponentially small in a
power of \(\log n\); this costs a polynomial in its logarithm, not an
inverse-gap-length series. It is a genuine improvement over the previously
specified matrix implementation, with the same approximation interface.

The outer and inner tensor-grid point counts are unchanged. Evaluating
each point efficiently does not make an exponentially large collection
of points efficient. This lemma therefore does not establish an efficient
whole-query decoder, alter the current prediction-error theorem, change
the small-label allowance, or resolve the dimension-independent storage
and fast-evaluation tradeoff for the conditional integral itself.
