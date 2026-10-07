# Independent check of polynomial-time small-matrix operations

2026-10-06. **PASS for the stated numerical sublemma; no required correction.**
This is a bounded mathematical reconstruction of the supplied finite-matrix
algorithms. It is not a full decoder review, an empirical test, or promotion.

## 1. Assignment, inputs, and actual checks

The assignment was to check polynomial bit time for exact rational inversion,
rounded Newton square roots including noncommuting errors, positive-part
buffers, conservative caps, Sylvester systems, and finite-graph composition.
Only the two assigned scientific inputs were read for this check, in full:

```text
3f2a2edb247853d55a64bb3812828d2e57f0ceca2f5effbce56cb31bfdbab47c  FAST_SMALL_MATRIX_FUNCTIONS.md
466316e156faaef58f8574876466ef513c34c45258370b046d35383eb8b28b33  SMALL_MATRIX_FUNCTION_EVALUATION.md
```

The hashes were verified with `sha256sum`; `wc -l` returned 234 and 578
lines respectively. Both complete files were returned without truncation.
No other route output, review, source dependency, or experiment was inspected
for this assignment. The reviewer authored the separately frozen compilation
route but did not author either matrix input or receive another checker's
findings. This is an independent numerical-sublemma reconstruction, not a
claim of a fresh isolated review of the entire scientific program.

The rigorous-math and conjecture-investigation instructions remained current.
The canonical-notation skill had returned `Permission denied` earlier in this
agent's work; the authorized explicit notation/rigor fallback remains in force.
The actual checking consisted of the algebraic, spectral, bit-length, error,
and interface derivations below. No numerical experiment or software
implementation was requested or executed.

## 2. Rational inversion: operation count and bit lengths

Let the symmetric dyadic input be \(A\in\mathbb R^{r\times r}\), with
fractional precision \(p\), \(aI\preceq A\preceq MI\),
\(0<a\leq1\leq M\). Clearing its common denominator gives the integer
matrix \(Q=2^p A\). Since \(|A_{ij}|\leq\|A\|\leq M\), the input
integer lengths are bounded by

\[
 B=O(p+\log(2+M)).
\]

For any \(k\times k\) minor, \(k\leq r\), expansion by permutations
bounds its magnitude by \(k!2^{kB}\). Thus every signed minor has
\(O(r[B+\log(r+1)])\) bits. This estimate applies to all row-permuted
submatrices too; row pivoting does not invalidate it.

After eliminating an invertible pivot block \(D\), a Schur entry is

\[
 u-v^T D^{-1}w
   =\frac{\det\begin{pmatrix}D&w\\v^T&u\end{pmatrix}}{\det D}.
\]

Multiplying the bordered matrix on the left by a unit-determinant block
elimination matrix proves the identity. Its reduced numerator and denominator
therefore have the minor bound. Temporary products, quotients and differences
before fraction reduction multiply this bit bound by at most a constant at
each update; reduction returns the new Schur entry to the minor bound.
Completed pivot products are determinants of the corresponding pivot blocks,
up to the tracked row signs. Exact zero-pivot search is a finite integer
comparison, not a numerical condition-number test. A remaining pivot column
that is identically zero certifies a zero determinant.

Gaussian elimination uses \(O(r^3)\) rational arithmetic operations per
determinant. At most \(r^2+1\) such calculations compute a determinant and
all cofactors. Schoolbook integer multiplication, long division and reduction
by the Euclidean algorithm take polynomial time and space in the displayed
lengths. A direct Euclidean bound is enough: in every two nonterminal
remainder steps the larger operand at least halves, giving linearly many
divisions in its original bit length.

The adjugate formula gives \(Q^{-1}\), and
\(A^{-1}=2^pQ^{-1}\). This extra binary scale is counted. Since the input
is positive definite, its determinant is nonzero. Symmetric entry rounding
with error at most \(\varepsilon/r\) gives Frobenius error at most
\(r(\varepsilon/r)=\varepsilon\). The precision needed for this rounding
has the claimed logarithmic dependence. There is no iteration count of
order \(1/a\). Indeed the exact rational arithmetic cost already follows
from the dyadic input lengths; the gap is relevant to stability and the
subsequent approximate interfaces, not to an inverse-length enumeration.

**Verdict:** the determinant/cofactor implementation is slow but polynomial
in all of the stated parameters. Singular cofactors, row swaps, and the
restoration of the input's dyadic scale do not create a missing case.

## 3. Exact Newton reference and rounded noncommuting iteration

Replace \(M\) by an outward power-of-two upper bound within a factor two.
For

\[
 X_0=MI,\qquad X_{j+1}=\tfrac12(X_j+AX_j^{-1}),
\]

the exact iterates commute with \(A\): the initial matrix does, and the
recurrence preserves that property. In an eigenbasis of \(A\), an eigenvalue
\(\lambda\in[a,M]\) has scalar iterates beginning at
\(M\geq\sqrt\lambda\), because \(M\geq1\). For
\(x\geq\sqrt\lambda\),

\[
 \frac{x+\lambda/x}{2}-\sqrt\lambda
   =\frac{(x-\sqrt\lambda)^2}{2x}
   \in[0,(x-\sqrt\lambda)/2].
\]

The iterate also cannot exceed \(x\), since \(\lambda/x\leq x\).
Consequently

\[
 aI\preceq\sqrt A\preceq X_j\preceq MI,
 \qquad \|X_j-\sqrt A\|_F\leq\sqrt r M2^{-j}.
\]

The first lower bound uses \(\sqrt a\geq a\), valid for \(a\leq1\).
With \(J=\lceil\log_2(8rM/\varepsilon)\rceil\), the final exact
error is at most \(\varepsilon/(8\sqrt r)\leq\varepsilon/8\).
Neither a quadratic-convergence theorem nor a condition-number-sized
initial phase is needed.

For the implemented symmetric dyadic iterate \(\widehat X_j\), set
\(e_j=\|\widehat X_j-X_j\|_F\) and define

\[
 F(X)=\tfrac12\operatorname{sym}(X+AX^{-1}).
\]

Assume inductively \(e_j\leq a/4\). Operator error is no larger than
Frobenius error, so \(\widehat X_j\succeq3aI/4\), in particular
\(\widehat X_j\succeq aI/2\). The exact inverse identity yields

\[
 \|\widehat X_j^{-1}-X_j^{-1}\|_F
 \leq\|\widehat X_j^{-1}\|\,e_j\,\|X_j^{-1}\|
 \leq2a^{-2}e_j.
\]

Symmetrization is Frobenius nonexpansive. Therefore

\[
 \|F(\widehat X_j)-F(X_j)\|_F
 \leq(1/2+Ma^{-2})e_j.
\]

This calculation does not assume that \(\widehat X_j\) commutes with
\(A\). The reference value \(F(X_j)=X_{j+1}\) does, which is enough.

Exact rational evaluation of \(F(\widehat X_j)\), followed by symmetric
rounding at grid step \(2^{-b}\), has local Frobenius error at most
\(r2^{-b}\). For the supplied power of two \(K\geq2+2M/a^2\),

\[
 e_{j+1}\leq Ke_j+r2^{-b},\quad e_0=0,
 \qquad e_j\leq r2^{-b}\sum_{i=0}^{j-1}K^i
                 \leq r2^{-b}JK^J.
\]

Choosing the final quantity at most
\(\min\{a/4,\varepsilon/4\}\) closes the induction before each next
inverse is invoked. Thus the gap assumption is not circular. Final error is
at most \(\varepsilon/8+\varepsilon/4<\varepsilon\).

Taking binary logarithms in the precision requirement gives

\[
 b=O\!\left(\log(r+1)+\log J+J\log K
                   +\log(1/a)+\log(1/\varepsilon)\right).
\]

Here \(J=O(\log(r+1)+\log(2+M)+\log(1/\varepsilon))\) and
\(\log K=O(1+\log(2+M)+\log(1/a))\), so the bound in the candidate
is valid after absorbing \(\log J\) into \(J\log K\).
Every iterate has norm below \(M+1\) and is reset to this single grid.
Its exact rational inverse and its multiplication by the original finite
matrix \(A\) therefore have polynomially bounded intermediate bit lengths.
The precision of the original \(A\) remains \(p\), while that of the current
iterate remains \(b\); no exact rational denominator is propagated into the
next iteration without rounding. Multiplying the polynomial per-step cost
by \(J\) still gives polynomial bit time and space.

**Verdict:** exact convergence, rounded stability, positive-gap induction,
noncommuting errors, and total bit complexity all pass. The scalar case
\(r=1\), smallest allowed magnitude bound \(M=1\), and arbitrarily small
positive \(a\) obey the same inequalities.

## 4. Positive parts, conservative caps, and Sylvester systems

For arbitrary symmetric \(A\) with \(\|A\|\leq M\), take the specified
dyadic \(\varepsilon/(64r)<v\leq\varepsilon/(32r)\). Forming
\(B=A^2+v^2I\) is an exact dyadic operation with at most doubled fractional
precision and logarithmic summation overhead. The spectral interval is
\([v^2,M^2+v^2]\), so both its logarithmic gap and logarithmic magnitude
remain polynomial in the original input size and requested accuracy.

Let \(\|Y-\sqrt B\|_F\leq v\) with \(Y\) symmetric, and return
\(P=(A+Y)/2+vI\) using exact additions and binary shifts. Eigenvaluewise,

\[
 0\leq (\lambda+\sqrt{\lambda^2+v^2})/2-\max\{\lambda,0\}
 \leq v/2.
\]

Thus the exact smoothed positive part is PSD, the error caused by \(Y\)
has operator norm at most \(v/2\), and the added \(vI\) proves the
*exact* certificate \(P\succeq vI/2\). The Frobenius error is at most
\((3\sqrt r/2+1/2)v\leq2rv<\varepsilon\). Zero and negative input
eigenvalues pose no gap problem; the algorithm itself supplies the gap.

The inherited radial cap uses only exact norms squared, one certified scalar
square root, a scalar division, and a conservative dyadic scale. Above the
cap radius \(C_0\), its values satisfy
\(s\leq t\leq s+2\eta_0\),
\(0\leq c\leq C_0/t\leq C_0/s\). Exact retention of \(cG\) consequently
preserves PSD and the exact Frobenius cap. Its error bound

\[
 \|cG-(C_0/s)G\|_F\leq2\eta_0+2\zeta U_F
\]

follows from \(C_0(t-s)/t\leq2\eta_0\) and an underestimation error
at most \(2\zeta\) in the scale. The case in which the clipped scale is
zero has the same bound: then \(C_0/t\leq2\zeta\). Below the cap the
exact branch returns \(G\). Replacing the scalar-root implementation by
the new algorithm preserves all these arguments and makes their cost
polynomial in the counted parameters. Final entrywise rounding is correctly
forbidden unless another certified buffer/cap step follows.

For \(SE+ET=H\), with symmetric \(S\succeq aI\) and
\(T\succeq bI\), the vectorized matrix is
\(I\otimes S+T^T\otimes I\). Its gap is at least \(a+b\), because
the two Kronecker terms each have the respective positive quadratic-form
bound. An \(s\times t\) unknown produces an \(st\times st\) system.
All of its entries, inverse storage, and multiplication by the vectorized
right side are counted. Exact rational inversion and controlled final
rounding therefore give the claimed polynomial time; no small-system size
is hidden by referring only to \(s+t\).

**Verdict:** PSD buffering, exact-cap retention, nongapped positive parts,
and the counted Sylvester dimension pass.

## 5. Input perturbations and full-graph composition

The inherited input-interface estimates remain applicable to the new
algorithms because they concern the exact functions, not a particular
iteration. If \(\|A_0-A\|_F\leq u\leq a/2\), then
\(A_0\succeq aI/2\) and
\(\|A_0^{-1}-A^{-1}\|_F\leq2a^{-2}u\). For square roots, even without
commutativity, putting \(Z=\sqrt{A_0}-\sqrt A\) gives

\[
 \sqrt{A_0}\,Z+Z\sqrt A=A_0-A.
\]

Taking its Frobenius inner product with \(Z\) gives the denominator
\(\sqrt{a/2}+\sqrt a\), hence the stated bound at most \(u/\sqrt a\).
For positive parts, metric projection onto the PSD cone is Frobenius
nonexpansive. These estimates validate the existing local accuracy allocation.

In a graph of \(N\) counted operations, the exact magnitude cap \(U\)
and gaps \(\alpha\) give a local amplification factor polynomial in
\(r,U,\alpha^{-1}\), after enlarging the neighborhood and halving the
gap. The allocation proportional to

\[
 \frac{\min\{\varepsilon,\alpha,1\}}
             {(N+1)L^{N+1}}
\]

has logarithmic reciprocal polynomial in \(N,r,\log U,\log\alpha^{-1}\)
and \(\log\varepsilon^{-1}\). Induction over graph nodes keeps every
approximate gapped operand within its half-gap margin and bounds the final
error. Binary operation arity can be absorbed into \(L\).

The common operand grid is essential and is explicitly supplied by the
inherited interface. Exact products inside positive-part and cap routines
increase word lengths only a bounded number of times before that reset.
If a rounded operand must remain PSD, the prescribed diagonal buffer
dominates its operator rounding error, with polynomial dimension factors
absorbed into the grid precision. A final capped output is retained at
its certified subroutine precision. Thus there is neither a chain of
unbounded exact rational denominators nor precision doubling across all
\(N\) nodes.

Each macro's new cost is a fixed-degree polynomial in its dimension, operand
precision, logarithmic magnitude/gap bounds, and logarithmic tolerance.
These arguments are polynomial in the global graph parameters, and there
are only \(N\) macros. Composition therefore gives polynomial bit time
and space for this explicitly bounded graph. Costs of external activation,
input, and constant-precision interfaces remain additional, exactly as
stated; polynomial-space interfaces alone have not been upgraded to
polynomial-time interfaces.

**Verdict:** full-graph composition passes for the stated certified inputs,
gaps, instruction counts, and finite dyadic interfaces.

## 6. Scoped conclusion

No correction is required for the frozen candidate. It establishes the
claimed polynomial-time replacement for the specified small-matrix
subroutines and their certified finite graphs. The proof counts inverse-gap
dependence through precision and bit lengths, rather than through a series
with inverse-gap-sized length.

This conclusion neither certifies the origin of every graph bound in the
neural construction nor changes the number of Fourier or Gaussian quadrature
points. Efficient evaluation at one integration point does not establish
efficient unseen-input decoding. No full decoder verdict is given here.
