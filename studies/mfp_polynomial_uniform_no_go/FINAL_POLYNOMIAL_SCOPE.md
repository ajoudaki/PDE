# Polynomial activations: rigorous scope of the uniform no-go

## Setup

Let

\[
 P(x)=\sum_{j=0}^dc_jx^j,\qquad d\ge2,qquad c_d>0,
 \qquad \mathbb EP(G)^2=1,
\]

and let \(\Delta_t(h)=F_{2t}(h)-F_t(2h)\) for the established width-first
two-hidden-layer network.  Let \(\kappa_t=[h^3]\Delta_t(h)\).

The restriction \(d\ge2\) is essential.  If degree one is allowed, the
normalized identity activation has positive leading coefficient and is the
already known linear exception, so no universal nonlinear-tail lower bound
can hold under the literal phrase “arbitrary polynomial.”

There are two different theorems.  They must not be conflated.

## Theorem A: full network for sign-coherent polynomials

If one of \(\varepsilon P(\sigma x)\),
\(\varepsilon,\sigma\in\{\pm1\}\), has nonnegative coefficients, then for
every \(\rho>0\),

\[
 \Delta_t(\rho/t)\longrightarrow+\infty
\]

after the corresponding exact orthogonal conjugacy.  Hence

\[
 \sup_{0<|h|\le\rho/t}
 \frac{|\Delta_t(h)-\kappa_th^3|}{t^4|h|^5}
\longrightarrow\infty.
\]

More explicitly, put \(s=d^{2t}\) and
\(M=(d+1)(s-1)/(d-1)\).  After applying the conjugacy and writing the
positive leading coefficient as \(c_d\), coefficientwise positivity gives,
at \(H=\rho/t\),

\[
 \Delta_t(H)-\kappa_tH^3\ge
 \begin{cases}
 c_d^{M+1}H^M\,\mathbb EG^s\,\mathbb EG^{ds},&d\text{ even},\\[1mm]
 c_d^MH^{M-1}\,\mathbb EG^{s+1}\,
                    \mathbb EG^{d(s-1)},&d\text{ odd}.
 \end{cases}
\]

Omitted integer factors are at least one.  The logarithm of either retained
term is \((d+1)s\,t\log d-O_{P,\rho}(s\log t)\), and hence tends to
\(+\infty\).

The proof is coefficientwise.  The full paired defect is a positive
polynomial, deletion of the bottom update is monotone, and the retained
frozen branch has Gaussian factorial growth.  It covers nonnegative
polynomials, pure monomials of every degree, the exact sign/reflection
conjugates, and shifted powers by their separate affine/sign conjugacy.

## Theorem B: every signed polynomial in the frozen scalar block

For independent standard Gaussians \(A_0,Z_0\), define

\[
 A^+=A+hP(Z),\qquad Z^+=Z+hAP'(Z),\qquad
 Q_N(h)=\mathbb E[A_NP(Z_N)],
\]

and \(D_t(h)=Q_{2t}(h)-Q_t(2h)\).  Put

\[
 s=d^{2t},\qquad r=d^{2t-1},\qquad
 M_t=\frac{d+1}{d-1}(s-1).
\]

Let

\[
 C_N=c_d^{((d+1)d^{N-1}-2)/(d-1)}
     d^{d(d^{N-1}-1)/(d-1)}.
\]

If \(d\) is even, define

\[
 k_t=M_t,
 \qquad
 b_t=C_{2t}\,\mathbb EG^s\,
 \mathbb E[P(G)^rP'(G)^s].
\]

Then \(b_t>0\).  If \(d\) is odd, put
\(a=c_{d-1}/c_d\), set \(k_t=M_t-1\), and define

\[
 b_t=sC_{2t}\mathbb EG^{s-1}
 \mathbb E\!\left[
 P(G)^{r-1}P'(G)^{s-1}
 \{rP'(G)+(G+a/d)P(G)\}
 \right].
\]

An explicit tail-versus-compact estimate proves \(b_t>0\) for all
sufficiently large \(t\).  In both parities, \(k_t\) is the exact degree of
\(D_t\), and subtracting a cubic does not change its leading coefficient.
The Chebyshev extremal inequality therefore gives the strict lower bound

\[
 \boxed{
 \sup_{0\le h\le\rho/t}|D_t(h)-\kappa_th^3|
 \ge 2^{1-2k_t}b_t(\rho/t)^{k_t}.}
\]

Moreover, for an explicit activation-defined \(C_{P,\rho}<\infty\),

\[
 \log\!\left(2^{1-2k_t}b_t(\rho/t)^{k_t}\right)
 \ge (d+1)s\,t\log d
 -\frac{d+1}{d-1}s\log t-C_{P,\rho}s.
\]

Consequently the right side tends to infinity, and

\[
 \sup_{0<h\le\rho/t}
 \frac{|D_t(h)-\kappa_th^3|}{t^4h^5}\longrightarrow\infty.
\]

This theorem permits arbitrary signs because Chebyshev prevents cancellation
among powers of \(h\).  For odd degree, translating
\(Y=Z+c_{d-1}/(dc_d)\) removes the unique degree-\((d-1)\) deficit source;
the resulting noncentral-Gaussian formula is exactly equivalent to the
displayed coefficient.

## Why Theorem B does not imply the requested full-network theorem

For arbitrary signed coefficients, the positive-polynomial deletion order
used in Theorem A is unavailable.  Chebyshev controls cancellation inside
the scalar polynomial \(D_t(h)\), but it cannot transfer a scalar
coefficient to the unrelated full polynomial \(\Delta_t(h)\).

Positive leading coefficient alone does not repair this.  For example,

\[
 P_K(x)=\frac{x^2-K}{\sqrt{K^2-2K+3}}
\]

is normalized and has positive leading coefficient, but the one-step frozen
top coefficient equals

\[
 [h^3]Q_1(h)=\frac{4(3-K)}{(K^2-2K+3)^2},
\]

which vanishes at \(K=3\) and is negative for \(K>3\).  Thus neither the
sign nor nonvanishing of an integrated high sector follows merely from
\(c_d>0\).  The same failure occurs in the actual width-first \(L=2\)
network: its exact one-step maximal coefficient is

\[
 [h^7]F_1(h)=1024,q_K^{16}(3-K)^3.
\]

It vanishes at \(K=3\) and changes sign across that value.  This formula
uses the RMS-normalized activation; it must not be confused with the
unnormalized polynomial \(x^2-K\), for which the hidden variance is not one.
Thus full-DAG maximal bidegree sectors can cancel after Gaussian contraction
in the width limit.

Therefore the universal assertion

\[
 \text{“every signed polynomial with }c_d>0\text{ violates the full }L=2
 \text{ uniform remainder bound”}
\]

is currently open.  Proving it requires a new quantitative theorem for the
complete signed, width-first OMFP contraction ledger; the frozen theorem and
finite-width degree counting do not supply that bridge.
