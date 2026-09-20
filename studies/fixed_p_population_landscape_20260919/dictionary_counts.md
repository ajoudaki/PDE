# Effective dimensions of the full fixed-order dictionary

Post-freeze counting check, 2026-09-19. Scientific input: the full dictionary and core independence statements in docs/global_nonlinear.md C.4.7.10.B, C.1, D.3, already read for dictionary_route.md. This is a bounded follow-up check, not a fresh isolated attempt. No other route artifact was read.

Let \(p\ge1\). Write \(d_\ell\) for the raw retained list length on population \(\ell\), including every appended valid bounded initialized-word code through \(p\) prescribed by the canonical dictionary. Let

\[
 q_\ell=\dim\operatorname{span}_{L^2(\lambda_\ell)}
              \{\psi_{\ell,j}:1\le j\le d_\ell\}
        =\operatorname{rank}G_\ell
\]

be its effective feature dimension. Positive-ridge Cholesky normalization is invertible as a coefficient transformation, so using \(b_\ell=L_\ell^{-1}\psi_\ell\) gives exactly the same effective dimension.

For every order,

\[
 q_1>d_2\ge q_2\ge {p+2\choose2}.
\]

The lower core alone gives

\[
 q_1\ge {p+4\choose4}.
\]

Indeed the four lower core coordinates have a positive density on the open four-cube. A polynomial vanishing almost surely therefore vanishes throughout that cube by continuity. Applying the one-variable root property successively to its four variables makes it the zero polynomial. The total-degree-at-most-\(p\) tensor Chebyshev products have distinct leading monomials and are consequently independent. Counting their exponent vectors gives \({p+4\choose4}\). The identical two-variable argument gives \(q_2\ge {p+2\choose2}\). Adding any initialized-word features cannot reduce either span.

The upper raw list has \({p+2\choose2}\) polynomial-core entries. There are only \(p+1\) code indices \(0,\ldots,p\), so at most \(p+1\) tail entries can be appended to that upper list:

\[
 d_2\le {p+2\choose2}+p+1.
\]

This deliberately loose bound allows every code to contribute an upper feature; type rejection, unbounded outputs, and literal duplicate sharing can only reduce the count. Dependencies compiled to construct a retained word are not retained features unless the stated dictionary rule independently retains them.

For \(p\ge2\), direct subtraction gives

\[
 {p+4\choose4}-{p+2\choose2}-(p+1)
 =\frac{p+1}{24}\bigl[p(p+2)(p+7)-24\bigr]>0,
\]

because \(p(p+2)(p+7)\ge2\cdot4\cdot9=72>24\). Hence \(q_1>d_2\) in this range.

For \(p=1\), codes 0 and 1 are precisely the already retained lower and upper constants. No tail entry is added. The core independence statement gives \(q_1=d_1=5\), \(q_2=d_2=3\), so strict inequality also holds. Finally \(q_2\le d_2\) is the elementary rank bound.

Consequently, a theorem requiring \(m\le q_2\) automatically has \(m<q_1\) for this exact full dictionary. The explicit sufficient input-count condition \(m\le {p+2\choose2}\) guarantees \(m\le q_2\). This counting result does not establish \(m\le q_2\) for an arbitrary number of data representatives at a fixed order, and does not itself establish a landscape theorem.
