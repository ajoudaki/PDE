# A polynomially vanishing dense-pair benchmark for the nonlinear witness

Status: author-derived and internally checked in SINE_CHECK.md and
ASSEMBLY_CHECK.md. This is a deliberately
nonsharp benchmark, not an assertion of a new sharp dense concentration rate.
It supplies the comparison needed if the growing-order lower-bound route in
`NONLINEAR_WITNESS.md` closes. It concerns the ordinary dense gradient flow,
not a replacement for frozen-top NTH. No other study is an input.

## Statement and normalization

Use two hidden layers, two inputs \(x_a=\sqrt2e_a\), labels \(y=(\eta,0)\),
and \(0<\eta\le10^{-62}\) fixed independently of width. The first activation
is \(\phi(z)=z+\varepsilon\sin z\), with any fixed

\[
1/8\le\varepsilon\le1/4,
\]

and the second activation is the identity. Initialization, mobilities, zero
readout, and loss are exactly those of `NONLINEAR_WITNESS.md`: first weights
have variance one, second weights variance \(1/n\), and

\[
f(v)=c^\top W\frac{\phi(\sqrt n Bv)}{\sqrt n},\qquad
B=W^{(1)}/\sqrt n,\quad W=W^{(2)},\quad c=u/\sqrt n,
\qquad \mathcal L=\frac14\sum_{a=1}^2(f(e_a)-y_a)^2.
\]

There is an absolute finite constant \(C\), uniform in the displayed
activation interval and label range, such that two independent dense runs
satisfy

\[
\Pr\!\left\{
\sup_{t\in[0,\infty]}\sup_{\|v\|=1}
 |f_n(t,v)-\widetilde f_n(t,v)|
 \le C n^{-1/64000}
\right\}\longrightarrow1.
\tag{1}
\]

The exponent is intentionally wasteful. Its only purpose is to distinguish
a polynomially vanishing dense-pair discrepancy from a proposed NTH error
lower bound \(n^{-o(1)}\). This proof does not use an unproved population
limit, the other studies' dense upper bounds, or a width-dependent label.

## Real coordinates and an initialization event

Set

\[
T(z)=\int_0^z\frac{dr}{1+\varepsilon\cos r},\qquad
\zeta_a=T(\sqrt n Be_a)/\sqrt n,\qquad
a_a=\phi(T^{-1}(\sqrt n\zeta_a))/\sqrt n.
\]

All scalar maps act coordinatewise. Their real derivative bounds are

\[
3/4\le\phi'\le5/4,\quad
4/5\le T'\le4/3,\quad
|(T^{-1})'|\le5/4,\quad
9/16\le(\phi\circ T^{-1})'\le25/16<2.
\tag{2}
\]

Write \(b_a=(y_a-f_a)/2\). The exact physical equations are

\[
\dot\zeta_a=b_aW^\top c,\qquad
\dot W=c\Big(\sum_a b_aa_a\Big)^\top,\qquad
\dot c=W\sum_a b_aa_a.
\tag{3}
\]

There is an event with probability at least \(1-Ce^{-cn}\) on which

\[
\|\zeta(0)\|_F\le4,\qquad
\max_a\|a_a(0)\|_2\le2,\qquad
\|W_0\|_{\rm op}\le4,\qquad
\lambda_{\min}\big[(W_0a_a(0))^\top W_0a_b(0)\big]_{a,b=1}^2\ge1/4.
\tag{4}
\]

Here and below \(c,C\) in probabilities are absolute positive constants.
To verify (4), the independent coordinate pairs of \(a_1,a_2\) are centered,
are bounded in absolute value by \(5|G|/(4\sqrt n)\), and have population
Gram \(\mathbb E\phi(G)^2 I_2\succeq(9/16)I_2\). Their empirical Gram
therefore differs from this matrix by at most \(1/16\) with exponentially
small failure: each centered product has a moment generating function in
a fixed neighborhood of zero, by its Gaussian-square upper bound, and
Chernoff's inequality applies to the independent coordinates. Conditional
on these two vectors, the independent rows of \(W_0(a_1,a_2)\) are Gaussian
with covariance equal to their empirical Gram divided by \(n\). The same
two-dimensional Gaussian-square argument proves that this second Gram
differs from the first by at most \(1/8\). These two estimates imply the
last inequality in (4). The vector bounds follow from (2) and the same
Gaussian-square tails. For the operator bound use
\(\Pr(\|W_0\|_{\rm op}>2+t)\le2e^{-nt^2/2}\), obtained by setting both
dimensions to \(n\) and dividing by \(\sqrt n\) in Corollary 5.35 of
[Vershynin's random-matrix notes](https://arxiv.org/pdf/1011.3027).
Taking \(t=2\) gives the required event.
No dependence on \(\varepsilon\) enters these bounds.

## Fitting, bounded states, and an exponential tail

Let \(Y=\eta/\sqrt2\) and

\[
\rho(t)=\|(f_1(t),f_2(t))-y\|_2/\sqrt2.
\]

Energy decay gives \(\rho\le Y\) and \(\sum_a|b_a|\le\rho\). Bootstrap the
three inequalities \(\|W\|_{\rm op}<5\), \(\max_a\|a_a\|_2<3\), and final
feature Gram gap greater than \(1/8\). The readout contribution alone to
the prediction tangent kernel is this feature Gram. Since the loss has
the factor \(1/4\),

\[
\rho(t)\le Ye^{-t/16},\qquad \int_0^\infty\rho(t)\,dt\le16Y
\tag{5}
\]

on every stopped bootstrap interval. Equation (3) then gives

\[
\begin{aligned}
\|c\|_2&\le240Y,\\
\sum_a\|\zeta_a-\zeta_a(0)\|_2&\le19200Y^2,\\
\|W-W_0\|_F&\le11520Y^2,\\
\max_a\|a_a-a_a(0)\|_2&\le38400Y^2.
\end{aligned}
\tag{6}
\]

The change in each final feature \(Wa_a\) is at most \(230000Y^2\).
Its initial norm is at most eight, so the operator change of the two by
two final feature Gram is at most \(8\cdot10^6Y^2<1/8\). The other
bootstrap inequalities also improve strictly. Standard continuation of
the finite-dimensional smooth real ODE now proves (5)--(6) globally;
the integrated derivative bounds give convergent parameters and fitting.

For any unit \(v\in\mathbb R^2\), reconstruct \(B\) columnwise from
\(B e_a=T^{-1}(\sqrt n\zeta_a)/\sqrt n\). Thus

\[
\|B\|_{\rm op}\le(5/4)\|\zeta\|_F<25/4,\qquad
\left\|\frac{\phi(\sqrt n Bv)}{\sqrt n}\right\|_2<8.
\]

Integrating (3) from \(t\) onward, using (5), gives the bounds in (6)
with an additional factor \(e^{-t/16}\), with the first line interpreted
as \(\|c(\infty)-c(t)\|\). Expanding the three factors in the output,
using (2), and \(Y\le10^{-62}\), yields the convenient uniform tail

\[
\sup_{\|v\|=1}|f(t,v)-f(\infty,v)|\le20000Y e^{-t/16}.
\tag{7}
\]

## Width-independent real stability on finite intervals

Compare two solutions whose initializations both satisfy (4). Define their
state difference norm by

\[
D(t)=\|\zeta-\widetilde\zeta\|_F+
       \|W-\widetilde W\|_F+\|c-\widetilde c\|_2.
\]

On the bounded region just proved, (2) and \(\|c\|\le1\) imply

\[
\max_a|f_a-\widetilde f_a|\le15D,\qquad
\sum_a|b_a-\widetilde b_a|\le15D.
\]

Expand each product in (3), one factor at a time. The sums of the bounds
for the \(\zeta,W,c\) blocks are at most \(81D,50D,238D\), respectively.
For example, the \(c\) block has the bounds \(3D+225D+10D\); the
normalization of the residual controls is included. Consequently

\[
D(t)\le e^{400t}D(0).
\tag{8}
\]

No bound on the Frobenius norm of the initialized dense matrix is used:
only its operator norm and the Frobenius norm of a *difference* occur.
The normalized initial Gaussian coordinates are \((B_0,W_0)\), all with
variance \(1/n\). The map from them to \(\zeta(0),W_0\) has Lipschitz
constant at most two into the difference norm. A passive query output
has Lipschitz constant at most forty in that norm, by its factorization
and (2). Thus, on the initialization event (4), each real \(f(t,v)\) is

\[
80e^{400t}\text{-Lipschitz in }(B_0,W_0).
\tag{9}
\]

On the same event, direct differentiation of the query formula and (3)
shows that \(f(t,v)\) is \(20000\)-Lipschitz in \(t\) and in the angular
coordinate of \(v\). The small fixed label range makes this deliberately
coarse numerical constant sufficient. These are real estimates; there
is no complex continuation of the true dynamics in this argument.

## Gaussian concentration and the complete-trajectory comparison

Extend each real observable in (9) from the event (4) to the entire
Gaussian coordinate space with the same Lipschitz constant, using

\[
F(x)=\inf_{z\text{ satisfying }(4)}
       \{f(t,v;z)+80e^{400t}\|x-z\|_2\}.
\]

The triangle inequality proves this is a same-constant Lipschitz extension.
For an \(A\)-Lipschitz function of independent \(N(0,1/n)\) coordinates,
Gaussian concentration gives

\[
\Pr\{|F-\mathbb EF|>s\}\le2\exp[-ns^2/(2A^2)].
\tag{10}
\]

This is Proposition 5.34 of
[the same notes](https://arxiv.org/pdf/1011.3027), applied to both \(F\)
and \(-F\), with Gaussian coordinates rescaled by \(1/\sqrt n\).
Its hypothesis holds by the extension's Euclidean Lipschitz bound;
the ambient dimension is finite, namely \(n^2+2n\).
Only this finite-dimensional Gaussian inequality is used, not an
infinite-width neural-network theorem. Two independent copies are within
\(2s\) of one another outside twice this failure event; their common
mean cancels. Add the exponentially small failure of (4).

Take \(T=(\log n)/4000\), so (9) is at most \(80n^{1/10}\). A grid with
spacing \(n^{-1/4}\) in time and angle has at most
\(C(1+\log n)n^{1/2}\) nodes on \([0,T]\times[0,2\pi]\).
Use \(s=n^{-1/4}\) in (10), and take a union bound over these nodes.
Its failure tends to zero, since the exponent is at least
\(n^{3/10}/12800\). The Lipschitz interpolation following (9) gives

\[
\sup_{0\le t\le T,\ \|v\|=1}
 |f_n(t,v)-\widetilde f_n(t,v)|\le C n^{-1/4}
\tag{11}
\]

with probability tending to one. For \(t>T\), compare each predictor
to its own value at \(T\) through its fitted endpoint and use (7).
The additional error is at most \(80000Y e^{-T/16}\), which equals
\(80000Y n^{-1/64000}\). Together with (11) this proves (1), including
the fitted endpoint and every query on the circle.

## Use and limitation

This is an actual independent-dense-run benchmark in the same complete
trajectory norm. If an original-NTH lower bound is \(n^{-o(1)}\) on any
one training input and short positive time, then its ratio to this dense
benchmark diverges in probability. The short-time lower witness need not
approximate the endpoint or the rest of the sphere. The argument does not
assert that the exponent \(1/64000\) is sharp. The completed combination
with the nonlinear growing-order NTH lower bound is NONLINEAR_RESULT.md.
