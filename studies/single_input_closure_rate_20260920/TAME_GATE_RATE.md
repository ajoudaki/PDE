# Polynomial conditioning of the single-input inverse gate

2026-09-20. Author: supervising task. This supplements, without changing the
model or runtime closure, the quantitative source construction in
`ROUTE_DICTIONARY.md`. Its complete witness, Gaussian-moment, ridge and code
arguments remain dependencies. The resulting order-rate inversion is in
`ORDER_RATE_INVERSION.md`. Internal research, not a promoted result.

## 1. The conditioning estimate

For the canonical two-hidden-layer tanh flow trained only on normalized input
e1, define

\[
 F(z)=z/2+\sinh(2z)/4,\qquad J(g,V)=F^{-1}(F(g)+V).
\]

Since `F'=cosh²>=1`, the inverse is globally defined and smooth. The single
input clock is `V`; the trained row is `(J(g1,V),g2)`. Direct differentiation
gives

\[
 J_V=\frac1{\cosh^2J}\le1,\qquad
 J_g=\frac{\cosh^2g}{\cosh^2J}>0.
\]

The earlier compiler used the loose bound `J_g<=exp(2R)` on a box. Instead
put `a(v)=cosh²(F^{-1}(v))`. Its derivative is

\[
 a'(v)=\frac{\sinh(2F^{-1}(v))}{\cosh^2(F^{-1}(v))}
       =2\tanh(F^{-1}(v)),\qquad |a'|\le2.
\]

Thus `|cosh²g-cosh²J|<=2|V|`, and division by `cosh²J>=1` proves the global
estimate

\[
                   0<J_g(g,V)\le1+2|V|.                 \tag{1}
\]

It is uniform in the Gaussian initial coordinate g. No Gaussian tail estimate,
analytic time expansion, small hidden displacement, or bounded raw g is used.
For `|V|<=R`, integration of the derivatives along a coordinatewise path gives

\[
 |J(g,V)-J(\widetilde g,\widetilde V)|
 \le (1+2R)|g-\widetilde g|+|V-\widetilde V|,
\]

when both clock values are in `[-R,R]`. This is a conditioning estimate for
the exact scalar representation, not a modification of its gradient metric.

## 2. Replace one estimate in the bounded-word compiler

Let `0<lambda<=1` be dyadic and retain the original cutoff

\[
 R=2^{16}/\lambda.
\]

For `|u1|,|u2|<=1`, set

\[
 \Psi_u(g_1,g_2,V)=\tanh(u_1J(g_1,V)+u_2g_2).
\]

On the clock box its three coordinate derivative magnitudes are bounded by
`1+2R,1,1`. As before define
`r_R(x)=R artanh(clamp(x,-tanh(1),tanh(1)))`; its global Lipschitz constant
is `R cosh²(1)<4R`, and its range is `[-R,R]`. The function

\[
 (x_1,x_2,x_3)\longmapsto
 \Psi_u(r_R(x_1),r_R(x_2),r_R(x_3))
\]

is therefore Lipschitz for the sum-coordinate metric with constant
`4R(1+2R)<=12R²`. Its coordinate-degree-n tensor Bernstein polynomial has
uniform error at most `36R²/sqrt(n)`: interpret its weights as three
independent binomial probabilities, use the coordinate variance bound `1/n`
on the rescaled cube, and then Cauchy--Schwarz in each coordinate.

Choose the **new compiler degree**

\[
 n=(2^{10}R^2/\lambda)^2=2^{84}\lambda^{-6}.           \tag{2}
\]

The Bernstein error is then `(36/1024)lambda<lambda/16`. Rationalizing
each sample to denominator `16/lambda` adds at most `lambda/16`, because
the weights are nonnegative and sum to one. Substitution of
`x=(tanh(g1/R),tanh(g2/R),tanh(V/R))` gives a bounded initialized word.
When `||V||2<=1500`, clipping changes its target by at most

\[
 2\sqrt{\Pr\{|g_1|>R\text{ or }|g_2|>R\text{ or }|V|>R\}}
 \le 2\sqrt{2+1500^2}/R<3002/R<\lambda/16
\]

in L2, by Markov and the union bound. No independence of the three fields is
required. The compiler's total error is therefore below lambda and its
output has absolute value at most `1+lambda/16`, exactly as required in the
original source proof.

The node count `P=100(n+1)^4` and coefficient bound
`Acoef=2^(3n+10) R/lambda²` follow from the same explicit Bernstein expansion:
there are `(n+1)^3` terms, at most `3n` powers per term, and each product of
binomial coefficients is at most `2^(3n)`. Sampling the scalar function uses
only g,V,u arguments of the compiler and the fixed elementary inverse F,
never any exact trained trajectory.

## 3. Consequence for actual closure order

Use this new n in the **same** integer recipe of `ROUTE_DICTIONARY.md`:
`lambda=2^(-(k+400000))`, `Jstep=6/lambda`, `m_grid=2^(k+20)`,
`W=100(Jstep+1)^2(m_grid+1)^2(P+1)`, followed by its E, saturation,
coefficient and M-code recursions. Call the resulting threshold
`N_tame(k)`. Every later source and stability estimate depends only on
the verified compiler error, boundedness, node count and coefficient size;
none uses the discarded exponential derivative bound separately. Thus

\[
 N\ge N_{\rm tame}(k)\quad\Longrightarrow\quad
 \rho_N(6)\le13\,2^{-k}.                              \tag{3}
\]

In particular, for `j>=1`, `N>=N_tame(j+62004)` implies

\[
 \sup_{t\ge0,u\in S^1}|f_N(t,u)-f(t,u)|\le2^{-j},      \tag{4}
\]

by the already proved single-input dynamics/clock estimate
`C_*<2^62000`. Its small-source condition follows because the right side
of (3) is then below `1/100`. The whole-circle fitted endpoint is included.
This is the actual maintained H3 degree-plus-word-prefix order N, with its
unchanged ridge and gradient equations, not a new approximation family.

The improvement is substantive in asymptotic order: the old compiler degree
was exponential in `1/lambda`, whereas (2) is polynomial. For example,
`P<=2^347 lambda^-24` and `W<=2^370 lambda^-28` follow by elementary bounds
on `(n+1)`, `(Jstep+1)` and `(m_grid+1)`. The remaining moment and literal
code recursions still incur two exponentials. Their complete inversion,
including constants and the distinction from retained dimension, is stated
and proved separately in `ORDER_RATE_INVERSION.md`.

The result is an improved worst-case asymptotic bound. It does not prove
optimality, monotonic errors, practical low-order accuracy, finite quadrature
accuracy, or a finite-neural-width all-time theorem. Increasing polynomial
degree while keeping the initialized action information fixed remains the
different, obstructed construction of `CORE_OBSTRUCTION.md`.
