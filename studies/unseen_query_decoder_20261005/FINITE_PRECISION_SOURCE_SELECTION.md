# Constructive finite-precision selection of the training row packets

2026-10-06. Numerical supplement to the candidate current-state decoder.
Author proof; no claim of an efficient preprocessing runtime or memory
bound. The purpose is to avoid an exact-rank decision or an arbitrarily
ill-conditioned selection weight in the construction.

## 1. Quantized moment vectors suffice

Use the finite scalar update program and the bounded Lipschitz row
functions in `NOISY_SCALAR_HISTORY_ACQUISITION.md`. There are \(P\)
updates and \(n\) original Gaussian packets. At the ideal realized
history, let

\[
 a_i=(F_r(Z_i;C_{<r}))_{r=1}^P\in\mathbb R^P,
                      \qquad \|a_i\|_\infty\le B.
\]

Choose rational vectors \(\widehat a_i\) with coordinate error at
most \(\epsilon\), all on a common dyadic grid. Their needed bit
length is \(O(\log(B+2)+\log(\epsilon^{-1}))\). Computing these
vectors requires an approximation of the ideal history as well as of
the packet marks and scalar instructions. The explicit causal
Lipschitz recurrence in the acquisition note provides this accuracy:
choose each local error smaller than
\(\epsilon/[C P(1+L)^P]\), where \(L\ge1\) bounds the row
functions' history and mark Lipschitz constants. Its logarithmic
precision is polynomial in \(P,\log L,\log(B+2),\log(\epsilon^{-1})\).
The same recurrence applies to the full \(n\)-row empirical updates,
since averaging does not enlarge a uniform evaluation error.

Exact rational convex elimination selects \(q\le P+1\) of these
quantized vectors and nonnegative rational weights summing to one such
that

\[
 \sum_{j=1}^q p_j\widehat a_{i_j}
                        =\frac1n\sum_{i=1}^n\widehat a_i.
                                                               \tag{1}
\]

Comparing the two sides to the unquantized vectors gives, without any
condition-number assumption,

\[
 \left\|\sum_jp_j a_{i_j}-\frac1n\sum_i a_i\right\|_\infty
                                                        \le2\epsilon.
                                                               \tag{2}
\]

Run the compact scalar program with these selected packets and weights,
and with the same scalar-noise marks as the ideal source. If its prefix
error is \(e_{r-1}\), then (2), applied at the ideal prefix, and
Lipschitz subtraction at the actually computed prefix give

\[
 e_r\le(1+L)e_{r-1}+2\epsilon.
\]

Thus the error of every compact prefix is at most
\(2\epsilon P(1+L)^P\), before the additional packet/weight/arithmetic
rounding errors already bounded in the acquisition note. Assigning half
of the desired history budget to this term is sufficient. Exact moment
preservation of the ideal transcendental source is therefore unnecessary.

## 2. The rational selection is an explicit finite algorithm

Initially (1) holds with all \(n\) uniform weights. If more than
\(P+1\) are positive, the rational vectors \((1,\widehat a_i)\)
on their support are linearly dependent. Rational Gaussian elimination
finds a nonzero dependence. Its coefficients sum to zero and therefore
have both signs. Move the weights along that dependence until at least
one positive weight is zero. The minimum of the finitely many rational
ratios is computable exactly, all weights remain nonnegative, and (1)
is preserved. Repeat finitely.

For a direct bound on final weight descriptions, one can instead
enumerate subsets of at most \(P+1\) columns and test rational
feasibility of (1). There is a feasible subset by the preceding argument.
Choose an affinely independent feasible support by further eliminating
dependencies. Its weights are determined by a nonsingular square minor
of order at most \(P+1\). Multiplying by the common dyadic denominator
and by \(n\), that minor and its right side are integer arrays with
entry bit length at most

\[
 b=C[\log(B+2)+\log(\epsilon^{-1})+\log(en)].
\]

The determinant expansion has at most \((P+1)!\) terms, each a product
of at most \(P+1\) such entries. Cramer's rule therefore bounds the
numerator and denominator bit lengths of every nonzero weight by

\[
 C(P+1)[b+\log(P+2)].                                    \tag{3}
\]

This also gives an explicit exhaustive selection algorithm, with no
undecidable test of whether an activation-generated real determinant
vanishes. Preprocessing is permitted to retain and inspect the quantized
source table; its cost is not hidden inside the online memory claim.

Alternatively, after any exact rational selection the weights may be
rounded by the acquisition note's nonnegative common-grid construction.
That proof never divides by a selection weight. Hence neither route
requires retaining the digits of an arbitrarily tiny positive weight.

## 3. Packet marks, scalar noise and bad-event handling

The row functions use explicitly clipped packet arguments. The selected
packet can therefore be stored in its clipped form, with exactly the
same row-function values. Its magnitude cap has a logarithm polynomial
in the finite-program parameters. Quantizing those marks to an assigned
error adds the certified row-function Lipschitz error, already included
in the acquisition recurrence.

The scalar Gaussian update marks are not clipped in the ideal law.
For implementation, choose a finite cap \(T\) with the required
Gaussian tail bound, and allow a preprocessing failure flag if a mark
exceeds it. On that flag the implementation may return a specified
bounded dummy model. The failure probability is charged explicitly.
On the good event all marks have \(O(\log(T+2)+\log(\epsilon^{-1}))\)
bit descriptions at the desired precision. There is no claim that a
hard-clipped update has the same continuous transition density.

All probabilistic posterior statements are made for the ideal Gaussian
update law. The constructed, quantized compact history is compared to
that ideal history by the deterministic error bound. The conditional
Fourier note supplies posterior continuity at histories with the stated
lower density bound. This is why finite precision does not require
pretending that a rounded history has a continuous density.

## 4. Consequence and boundary

If \(P\), packet dimension, \(\log B\), \(\log L\), and the
required logarithmic history precision are absolute powers of
\(\log(en)\), then the selected row marks, weights, scalar-noise
marks and current summaries have an absolute-polylogarithmic total bit
description. Selection uses only the training source program; no test
input or label enters it. Its selected support still has \(q\le P+1\).

This is a construction with potentially very expensive source
preprocessing. It does not assert that the weights can be chosen before
examining the finite source history, or that the source table itself has
small preprocessing memory. It establishes that exact-rank decisions and
hidden infinite-precision weights are unnecessary for the stated online
compression interface.
