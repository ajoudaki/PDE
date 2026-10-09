# A numerical terminal predictor in a nonlinear shallow special case

Status: internally derived, not independently reviewed or promoted. This is one
independent constructive round and its focused numerical/variability repair.
It does **not** prove the requested general deep-network compression theorem.

The useful positive result is a genuinely nonlinear, all-parameter-trained,
one-hidden-layer, one-training-sample theorem. It retains a numerical
two-variable polynomial evaluator that accepts queries after compilation.
Its coefficient count is $O((\log n)^3)$, its coefficient-bit count is
$O((\log n)^4)$, and its RMS prediction error is eventually no larger than
the actual RMS discrepancy between two independent trained dense networks.
The activation is restricted here to a positive bounded nonconstant member
of the stipulated holomorphic class. The general number of samples, depth,
unbounded-activation class, and fixed-confidence comparison remain open.

The user subsequently clarified that the $O(1)$ unlabeled query inputs are
available at initialization. The theorem below solves the stricter
post-compilation query interface in its restricted architecture. Merely
training a dense model and retaining its answers on a predeclared panel is
excluded as a success criterion: that is an output cache, not the requested
faithful numerical TP/population program.

## 1. Contract and canonical shallow model

Let $m=L=1$, let $x_0\in\mathbb R^d$ satisfy
$\|x_0\|_2^2=d$, and let the training label be $y>0$. Put
$u_0=x_0/\sqrt d$, so $\|u_0\|_2=1$. The first weight matrix is
$W^{(1)}\in\mathbb R^{n\times d}$, with independent standard Gaussian
entries; $W_i^{(1)}\in\mathbb R^d$ denotes the transpose of its $i$th row.
The stored readout is $w=W^{(2)}\in\mathbb R^n$, initialized
exactly at zero. For a query $x$, write $u=x/\sqrt d$. The network and
loss are

\[
z_i(x)=W_i^{(1)\top}u,\qquad
f_n(x)=\frac1n\sum_{i=1}^n w_i\phi(z_i(x)),\qquad
\mathcal L_n=(f_n(x_0)-y)^2.
\]

Both blocks have mobility $n$, exactly as the canonical
$(n,1,\ldots,1,n)$ rule specializes to $L=1$. Thus

\[
\dot w_i=2(y-f_n(x_0))\phi(z_i(x_0)),\qquad
\dot W_i^{(1)}
=2(y-f_n(x_0))w_i\phi'(z_i(x_0))u_0.
\tag{1}
\]

Assume that a fixed, effectively computable activation is holomorphic on
$\{z:|\operatorname{Im}z|<\sigma\}$, with a known bound
$|\phi'(z)|\le M$ there, and that on the real line

\[
0<a\le\phi(t)\le b<\infty.
\tag{2}
\]

Assume also that $\phi$ is nonconstant. Bounds for real higher derivatives
follow by applying Cauchy's formula to $\phi'$ on a circle of radius
$\sigma/2$; for example $|\phi''(t)|\le 2M/\sigma$.
Effective computability means that evaluations of $\phi,\phi'$ to requested
precision and the displayed constants are available. Holomorphy alone would
not imply this numerical premise. A concrete member is
$\phi(t)=1+c\tanh(t)$, $0<c<1$, on any fixed strip strictly inside its
nearest poles.

Fix $R>0$ and $\tau_0>0$. The post-compilation query domain is

\[
\mathcal X=\{x:\|x\|_2/\sqrt d\le R,
\quad \|u-(u_0^\top u)u_0\|_2\ge\tau_0\}.
\tag{3}
\]

This domain is nonempty only when the input dimension and constants permit
an orthogonal component. The restriction in (3) is needed for the variability
lower bound, not for numerical approximation of the population predictor.

For a fixed query $x$, let $f_n^\infty(x)$ be the dense GF endpoint and let
$\widetilde f_n^\infty(x)$ be the endpoint from an independent Gaussian
initialization. Define the **actual ensemble RMS dense-pair discrepancy** by

\[
D_n(x)=
\left(\mathbb E|f_n^\infty(x)-\widetilde f_n^\infty(x)|^2\right)^{1/2}
=\sqrt{2\operatorname{Var}(f_n^\infty(x))}.
\tag{4}
\]

All expectations in this note are over the stated Gaussian initialization.
The theorem is pointwise in each deterministic query, uniformly in its
constants over (3). It also holds for the mean squared error over any fixed
finite panel by summing the pointwise bounds. It is not a theorem for queries
chosen adversarially after inspecting the discarded dense arrays, nor a
comparison to the random realized difference of one particular dense pair.

## 2. Exact feature-time reduction and endpoint

For $g\in\mathbb R$, define two scalar functions $z_s(g),w_s(g)$ by

\[
\frac{d z_s(g)}{ds}=w_s(g)\phi'(z_s(g)),\qquad
\frac{d w_s(g)}{ds}=\phi(z_s(g)),\qquad
z_0(g)=g,\quad w_0(g)=0.
\tag{5}
\]

Let $S=y/a^2$. On $0\le s\le S$, (2) implies

\[
as\le w_s(g)\le bs,\qquad
|z_s(g)-g|\le \frac{Mb s^2}{2}.
\tag{6}
\]

These bounds prevent finite-time escape. Local uniqueness follows from the
continuous bounded derivatives on each reached strip in $(z,w)$; hence (5)
exists uniquely on the whole required interval for every $g$.

For the finite network, let $g_i=W_i^{(1)}(0)^\top u_0$, independently
standard Gaussian. Set

\[
\psi_s(g)=w_s(g)\phi(z_s(g)),\qquad
F_n(s)=\frac1n\sum_i\psi_s(g_i),\qquad
F(s)=\mathbb E\psi_s(G),\quad G\sim N(0,1).
\tag{7}
\]

Differentiating (5) gives the exact identity

\[
\partial_s\psi_s(g)=
\phi(z_s(g))^2+w_s(g)^2\phi'(z_s(g))^2\ge a^2.
\tag{8}
\]

Consequently $F_n(0)=F(0)=0$, and both equations $F_n(s_n)=y$ and
$F(s_*)=y$ have unique roots in $[0,S]$. In fact

\[
\frac y{b^2}\le s_n,s_*\le\frac y{a^2},
\tag{9}
\]

because $\psi_s\le b^2s$. The derivative and second derivative of
$\psi_s$ are bounded uniformly in $g,s\in[0,S]$, justifying all the
expectation derivatives used here.

Define physical feature time by

\[
\frac{ds}{dt}=2(y-F_n(s)),\qquad s(0)=0.
\tag{10}
\]

For $s<s_n$, the right side is positive. The residual satisfies
$d(y-F_n(s(t)))/dt=-2F_n'(s(t))(y-F_n(s(t)))$; therefore

\[
0\le y-F_n(s(t))\le y e^{-2a^2t}.
\tag{11}
\]

The substitution of (5) into (1) proves that (10), (5) reconstruct the actual
finite GF exactly. They also prove convergence to its parameter endpoint
at $s_n$. Replacing $F_n$ by $F$ gives the explicitly defined population
endpoint at $s_*$. No general tensor-program limit theorem is being assumed.

For $\phi=1+c\tanh$, $z_s(g)>g$ at every $s>0$, since $w_s>0$ and
$\phi'>0$. In particular the hidden weights genuinely learn. At zero,
$\partial_s^2z_0(g)=\phi(g)\phi'(g)>0$. This verifies nonzero hidden motion
in the example, without claiming a depth-uniform relative motion lower bound.

## 3. Exact two-Gaussian query formula

For any $x$, define

\[
\rho=u_0^\top u,\qquad
\tau=\|u-\rho u_0\|_2.
\tag{12}
\]

The first row moves only along $u_0$. Gaussian orthogonal decomposition
therefore gives, for a fixed query, independent $G_i,Z_i\sim N(0,1)$ such
that its exact finite terminal prediction has the law

\[
f_n^\infty(x)=\frac1n\sum_{i=1}^n
w_{s_n}(G_i)
\phi\bigl(\rho z_{s_n}(G_i)+\tau Z_i\bigr).
\tag{13}
\]

The $G_i$'s determine $s_n$, and the $Z_i$'s are independent of all
training quantities. If $\tau=0$, the $Z_i$ term is simply absent. The
corresponding population predictor is the actual numerical target

\[
K(\rho,\tau)=
\mathbb E_{G,Z}\left[
w_{s_*}(G)\phi\bigl(\rho z_{s_*}(G)+\tau Z\bigr)
\right].
\tag{14}
\]

Equation (14), by itself, is an expectation formula, not a finite numerical
representation. Section 6 constructs that representation and counts it.

## 4. The population predictor is within $O(n^{-1})$ of the dense mean

The following proof supplies the finite-width bias estimate rather than
assuming an endpoint limit theorem. All constants in this section depend
only on $a,b,M,\sigma,S,R$.

Write $\Delta=s_n-s_*$. From (8) and $F_n(s_n)=F(s_*)=y$,

\[
|\Delta|\le a^{-2}|F_n(s_*)-F(s_*)|,
\qquad
\mathbb E\Delta^2\le\frac{V}{n},
\quad V=\frac{b^4S^2}{a^4}.
\tag{15}
\]

Uniform derivative bounds that will suffice are

\[
|\psi_s'|\le D_1=b^2+b^2S^2M^2,
\qquad
|\psi_s''|\le D_2
=4b^2SM^2+2b^3S^3M^2(2M/\sigma).
\tag{16}
\]

For the second identity, differentiating (8) gives
$\psi_s''=4w_s\phi(z_s)\phi'(z_s)^2
+2w_s^3\phi'(z_s)^2\phi''(z_s)$, which proves the bound.

Taylor expansion at $s_*$, followed by adding and subtracting $F'(s_*)$,
gives

\[
0=F_n(s_*)-F(s_*)+F'(s_*)\Delta
+[F_n'(s_*)-F'(s_*)]\Delta+R_n,
\qquad |R_n|\le D_2\Delta^2/2.
\]

The first term has mean zero. Since the variance of the empirical derivative
is at most $D_1^2/n$, Cauchy–Schwarz and (15) imply

\[
|\mathbb E\Delta|\le\frac{C_s}{n},
\qquad
C_s=a^{-2}\left(D_1\sqrt V+\frac{D_2V}{2}\right).
\tag{17}
\]

For fixed $|\rho|,\tau\le R$, put

\[
k_s(g,z)=w_s(g)\phi(\rho z_s(g)+\tau z),\qquad
K_n(s)=\frac1n\sum_i k_s(G_i,Z_i).
\]

The bounds (6) and the bounded derivatives of $\phi$ show that
$|\partial_s k_s|\le K_1$ and $|\partial_s^2k_s|\le K_2$ uniformly in
$g,z,s$. One may take

\[
K_1=b^2+R b^2S^2M^2.
\]

For an explicit $K_2$, use

\[
\begin{aligned}
w_s''&=w_s\phi'(z_s)^2,\\
z_s''&=\phi(z_s)\phi'(z_s)
+w_s^2\phi''(z_s)\phi'(z_s),\\
k_s''&=w_s''\phi(v_s)
+2w_s'\phi'(v_s)\rho z_s'
+w_s\phi''(v_s)(\rho z_s')^2
+w_s\phi'(v_s)\rho z_s'',
\quad v_s=\rho z_s+\tau z.
\end{aligned}
\tag{18}
\]

Substitution of $w_s\le bS$, $|z_s'|\le bSM$ and
$|\phi''|\le2M/\sigma$ in (18) is a finite polynomial bound $K_2$.

Taylor expansion of $K_n(s_n)$ at $s_*$ gives a mean-zero zeroth-order
empirical error. For its linear term,

\[
\mathbb E[K_n'(s_*)\Delta]
=\mathbb E K_n'(s_*)\,\mathbb E\Delta
+\mathbb E[(K_n'(s_*)-\mathbb E K_n'(s_*))\Delta].
\]

The second term is at most $K_1\sqrt V/n$, because the pairs
$(G_i,Z_i)$ are iid before their common clock is substituted. The quadratic
remainder is at most $K_2V/(2n)$. Hence

\[
\sup_{|\rho|,\tau\le R}
|\mathbb E f_n^\infty(x)-K(\rho,\tau)|
\le \frac{C_{b}}n,
\quad C_{b}=K_1C_s+K_1\sqrt V+K_2V/2.
\tag{19}
\]

In particular, this is a bias estimate against the actual dense endpoint,
not an estimate against another approximate solver. At fixed $a,b,M,\sigma,R$
and bounded $y$, the displayed constants imply $C_{b}/y$ is bounded by
a polynomial in $S$, $a^{-1}$, and the stated regularity constants.

## 5. A nondegenerate actual dense-variance lower bound

Fix any $B_0>0$, let $p_0=\mathbb P(|G|\le B_0)>0$, and put
$C_0=MbS^2/2$. For $G_i\in[-B_0,B_0]$, (6) yields
$|\rho z_{s_n}(G_i)|\le R(B_0+C_0)$. Define

\[
v_0=
\min_{|v|\le R(B_0+C_0),\;\tau_0\le t\le R}
\operatorname{Var}\bigl(\phi(v+tZ)\bigr).
\tag{20}
\]

If (3) is nonempty, then $v_0>0$. To prove this, boundedness and dominated
convergence make the variance continuous in $(v,t)$. A zero variance at
$t>0$ would make the continuous function $\phi$ constant almost surely
under a Gaussian law with full real support, hence constant on all of
$\mathbb R$, contrary to the assumption. Positivity on the compact
parameter rectangle then gives a strictly positive minimum.

Condition on $G_1,\ldots,G_n$. The summands in (13) have independent query
Gaussians, so

\[
\operatorname{Var}(f_n^\infty(x)\mid G_1,\ldots,G_n)
=\frac1{n^2}\sum_i w_{s_n}(G_i)^2
\operatorname{Var}_Z\phi(\rho z_{s_n}(G_i)+\tau Z).
\]

By (6), (9), and (20), the expectation of this conditional variance is at
least

\[
\operatorname{Var}(f_n^\infty(x))
\ge\frac{c_vy^2}{n},
\qquad c_v=\frac{a^2p_0v_0}{b^4}>0,
\quad x\in\mathcal X.
\tag{21}
\]

No independence between $s_n$ and the $G_i$'s was used: the lower bound
$w_{s_n}(G_i)\ge ay/b^2$ holds for every training realization.

This is a pointwise variance lower bound, not a small-ball theorem for a
realized dense-pair difference. It excludes the training direction, where
the training point itself has zero endpoint variance. One cannot silently
use it at such a point.

There is also a matching upper order bound. Writing
$f_n^\infty(x)-K=[K_n(s_*)-K]+[K_n(s_n)-K_n(s_*)]$ and using
independence at the fixed clock and the Lipschitz bound $K_1$ gives

\[
\operatorname{Var}(f_n^\infty(x))
\le \mathbb E|f_n^\infty(x)-K|^2
\le \frac{2b^4S^2+2K_1^2V}{n}.
\]

Thus the actual ensemble discrepancy in (4) is of order $n^{-1/2}$ on
the stated nondegenerate query domain, with explicit dependence through
the constants already defined.

## 6. Numerical compiler, representation, and cost

Here is an explicit finite compiler for (14). It uses only the Gaussian
initialization law, $x_0,y$, and the given activation. It does not observe a
dense training trajectory or future query outputs. Its retained state is
the training direction, a scale, and a finite coefficient array.

For $0<\varepsilon<1/2$, target absolute error $y\varepsilon$. Normalize
the function by $y$, so constants need not grow as $y\downarrow0$. Fix
$S=y/a^2$. For real $g,z$, $|k_{s_*}(g,z)|/y\le b^2/a^2$.
Truncate both standard Gaussian roots to $[-B,B]$, where

\[
B=\max\left(1,\sqrt{2\log\frac{C b^2}{a^2\varepsilon}}\right).
\tag{22}
\]

The elementary Gaussian tail bound $\mathbb P(|G|>B)\le2e^{-B^2/2}$
implies that the discarded contribution is at most $y\varepsilon/8$,
for a suitable absolute $C$. Denote the retained integral by
$K_B(\rho,\tau)$.

For complex $\rho,\tau$ with imaginary parts at most

\[
h=\min\left(1,\frac{\sigma}{4(2B+C_0)}\right),
\tag{23}
\]

the argument $\rho z_{s_*}(g)+\tau z$ has imaginary part at most
$\sigma/4$ on the truncated roots. The complex derivative assumption and
the real bound give $|\phi(v+it)|\le b+M|t|$. Thus $K_B/y$ is
holomorphic in this two-variable tube and bounded there by

\[
M_K=\frac b{a^2}(b+M\sigma/4).
\tag{24}
\]

Map the real rectangle $[-R,R]\times[0,R]$ to $[-1,1]^2$. Let

\[
\alpha=\min(1,h/(2R)),
\]

with the zero-radius case omitted since (3) would then be empty. A Bernstein
ellipse with parameter $e^\alpha$ has imaginary semiaxis
$\sinh\alpha\le2\alpha$; hence the product of the mapped ellipses lies
in the tube. Expand $K_B/y$ in tensor Chebyshev polynomials,

\[
\frac{K_B(\rho,\tau)}y
=\sum_{j,k\ge0} c_{jk}
T_j(\rho/R)T_k(2\tau/R-1).
\tag{25}
\]

For completeness, substitute $u=(\zeta+\zeta^{-1})/2$ in each coordinate.
The resulting function is analytic on the product annuli
$e^{-\alpha}<|\zeta_1|,|\zeta_2|<e^\alpha$, is invariant under each
inversion, and is bounded by $M_K$. Cauchy's integral formula for its
Laurent coefficients gives
$|c_{jk}|\le4M_K e^{-\alpha(j+k)}$, with harmless smaller factors when an
index is zero. This derivation supplies the precise analytic approximation
fact used here. Summing the geometric tails gives

\[
\left|\frac{K_B}y-\sum_{0\le j,k\le p}c_{jk}T_jT_k\right|
\le\frac{8M_K e^{-\alpha(p+1)}}{(1-e^{-\alpha})^2}.
\tag{26}
\]

Choose $p$ large enough that (26) is at most $\varepsilon/8$. Since
$1-e^{-\alpha}\ge\alpha/2$ for $0<\alpha\le1$, it suffices to take

\[
p\ge\alpha^{-1}
\log\frac{256M_K}{\varepsilon\alpha^2}.
\tag{27}
\]

At fixed problem constants, (22)–(27) give

\[
p=O((\log(1/\varepsilon))^{3/2}),\qquad
(p+1)^2=O((\log(1/\varepsilon))^3).
\tag{28}
\]

The roots $s_*,z_s(g),w_s(g)$ and the coefficients are not unit-cost
oracles. The following setup procedure makes their numerical provenance
explicit.

1. To evaluate $F(s)$, truncate its one Gaussian root by the same bounded
   tail estimate, solve the two-dimensional ODE (5) at quadrature nodes,
   and integrate on the resulting compact interval. Bounds on the real
   derivatives of the ODE vector field give an effective Lipschitz constant
   on $0\le s\le S$. Gronwall's inequality then bounds forward-Euler
   error by a known constant times the step. Refining a finite step mesh
   and a rectangle quadrature therefore achieves any prescribed error.
2. Since $F'\ge a^2$, interval bisection with increasingly accurate
   evaluations locates $s_*$ to any prescribed tolerance. For example,
   when the certified interval for $F(s)-y$ contains zero, its width
   divided by $a^2$ supplies a bound on the root's distance from $s$.
   This avoids assuming that an inexact sign test always succeeds.
3. The coefficients in (25) are two cosine integrals of $K_B/y$. After
   inserting its definition, they are four-dimensional integrals over
   compact intervals: two real Gaussian roots and two cosine angles.
   All their integrands are continuous with effective derivative bounds.
   Indeed differentiating (5) with respect to $g$ is a bounded linear
   variational ODE on the reached region, so a computable exponential
   Gronwall bound supplies the needed derivative bound. Rectangle
   quadrature, with the ODE solved at its nodes, computes every
   coefficient to $\varepsilon/[16(p+1)^2]$. The ODE-discretization,
   quadrature, activation-evaluation, and arithmetic errors jointly fit
   this per-coefficient budget; each receives a fixed fraction of it.
4. The same derivative bounds control changing $s_*$ to its numerical
   approximation. Taking its error at most
   $y\varepsilon/[128K_1(p+1)^2]$ bounds the resulting sum of normalized
   coefficient errors by $\varepsilon/32$, and hence the final predictor
   error by $y\varepsilon/32$. Round and store each coefficient at accuracy
   $\varepsilon/[16(p+1)^2]$.

This setup is finite and fully determined by initialization law and data.
At fixed activation constants it uses polynomially many arithmetic
operations and activation-backend calls in $\varepsilon^{-1}$, with
fixed-dimensional quadrature and first-order ODE integration. The
requested numerical precision is $O(\log(1/\varepsilon))$ bits, with
guards for the fixed constants. The constants can be very large and include
exponentials of the reached ODE Lipschitz bound times $S$. More explicitly,
a compact $q$-dimensional rectangle rule with mesh $h$ has error at
most its volume times a derivative bound times $q h$; here $q\le4$.
Taking $h$ proportional to the required coefficient error, and an ODE
time step proportional to that error after its Gronwall factor, gives a
finite polynomial upper bound on those operation and call counts.
The work of the activation backend at requested precision is additional
and must be counted. A merely computable activation can have arbitrarily
large evaluation cost; polynomial total setup work requires a corresponding
complexity assumption on that backend. No low setup-cost claim,
polynomial gap dependence of setup, or practical speed claim is made.

The retained evaluator computes $\rho,\tau$ by (12) and the finite sum

\[
P_{n}(x)=y\sum_{0\le j,k\le p}
\widehat c_{jk}T_j(\rho/R)T_k(2\tau/R-1).
\tag{29}
\]

This is executable arithmetic; it contains no unevaluated expectations.
At query time it needs neither the dense arrays nor Gaussian quadrature.
The recurrence $T_{j+1}(u)=2uT_j(u)-T_{j-1}(u)$ evaluates the factors.
On $[-1,1]$, $|T_j|\le1$. A per-operation error $\delta$ in that
recurrence accumulates at most $O(p^2\delta)$: the forced recurrence
solution uses second-kind Chebyshev factors bounded by their index plus
one. Also $\sup|T_j'|\le j^2$, which controls argument rounding. Taking
working precision with $O(\log(1/\varepsilon)+\log p)$ fractional bits,
with a sufficiently large fixed multiplier and guards for the stated
constants and $d$, therefore keeps arithmetic and coefficient errors
below the remaining budget. The lower bound $\tau\ge\tau_0$ makes
computing the square root in (12) uniformly well conditioned. Training
direction and query coordinates need corresponding numerical precision.
Rounded arguments can be clamped to their known intervals; this cannot
increase their errors and keeps every recurrence argument in $[-1,1]$.

In particular, after assigning each error source its displayed budget,

\[
\sup_{x\in\mathcal X}|P_n(x)-K(\rho,\tau)|\le y\varepsilon.
\tag{30}
\]

Set $\varepsilon=1/n$ for $n\ge3$. The resulting retained and evaluation
costs are:

| Resource | Bound at fixed activation, label and query-domain constants |
|---|---|
| Stored numerical coefficients | $O((\log n)^3)$ |
| Bits per coefficient/working number | $O(\log n+\log d)$ |
| Stored training direction and scalar data | $O(d)$ working numbers |
| Total retained bits | $O((d+(\log n)^3)(\log n+\log d))$ |
| Query arithmetic operations | $O(d+(\log n)^3)$ |
| Additional workspace | $O(d+p)$ working numbers, or $O(p)$ with streamed input |
| Setup | Polynomially many arithmetic operations and backend calls in $n$, at $O(\log n)$ precision; backend evaluation work is additional |

Input bit length and output precision are part of these costs. Arbitrary
real data or arbitrary-precision coefficients are not treated as single
unit-cost storage cells. Constants in the retained-state bound obtained
from (22)–(27) are polynomial in the indicated strip, radius, $S$, and
$a^{-1}$ parameters, up to logarithms. The canonical initial one-sample
feature Gram is the scalar $\gamma=\mathbb E\phi(G)^2\ge a^2$.
The proof uses the lower bound $a^2$; it does not establish complexity
in $\gamma^{-1}$ alone or dependence on a general multi-sample feature gap.

## 7. Proven scoped RMS theorem

Combining (19) and (30) with $\varepsilon=1/n$ gives

\[
|P_n(x)-\mathbb E f_n^\infty(x)|
\le \frac{C_{b}+y}{n}.
\]

Since $P_n(x)$ is deterministic, the elementary bias–variance identity is
exact:

\[
\mathbb E|P_n(x)-f_n^\infty(x)|^2
=\operatorname{Var}(f_n^\infty(x))
+|P_n(x)-\mathbb E f_n^\infty(x)|^2.
\tag{31}
\]

Using (4) and (21),

\[
\frac{\mathbb E|P_n(x)-f_n^\infty(x)|^2}{D_n(x)^2}
\le\frac12+
\frac{(C_{b}/y+1)^2}{2c_v n},\qquad x\in\mathcal X.
\tag{32}
\]

Thus for all sufficiently large $n$, uniformly in each fixed query from
(3), the RMS surrogate error is at most the **actual** RMS dense-pair
discrepancy. Its ratio tends to $1/\sqrt2$. The representation has an
absolute polylogarithmic exponent and polynomial $d$-dependence. It
faithfully approximates the nonlinear population predictor generated by
the exact shallow all-layer GF, rather than freezing its features.

The asymptotic threshold in (32) depends on the actual nondegeneracy
constant $v_0$. No polynomial lower bound for $v_0$ in a general feature
gap is claimed. The result does not turn an upper width-concentration
bound into an actual variability lower bound: (21) supplied the latter
directly. It also does not imply a fixed-confidence bound normalized to
one observed pair, a pathwise guarantee, or a theorem for the entire
unbounded activation class.

For a specified positive stopping residual $\delta<y$, the same scalar
construction applies with $s_n$ defined by $F_n(s_n)=y-\delta$, and
$s_*$ by $F(s_*)=y-\delta$. The proofs replace the positive target $y$
by $y-\delta$ where it defines the terminal feature interval and its
variance bound. This is a prescribed loss-based terminal rule, not a
terminal time secretly chosen from query predictions.

## 8. Why this does not settle general $m,L$

For a shallow network with training vectors spanning an $r$-dimensional
subspace of $\mathbb R^d$, every first-weight increment remains in that
subspace. Choose an orthonormal basis $V\in\mathbb R^{d\times r}$.
Conditional on the existence of the relevant population endpoint, a
particle's learned training projection and readout are functions
$U_\infty(G)\in\mathbb R^r$, $W_\infty(G)\in\mathbb R$ of an
$r$-dimensional initial Gaussian root. A passive query, with
$q=V^\top u$ and $\tau=\|u-Vq\|_2$, has the representation

\[
\mathbb E_{G\in\mathbb R^r,Z\in\mathbb R}
\left[W_\infty(G)\phi(q^\top U_\infty(G)+\tau Z)\right].
\tag{33}
\]

This observation identifies a structural reduction in the number of query
coordinates. It does not prove that the endpoint exists or is efficiently
computable for general data. Tensor polynomial approximation in these
$r+1$ query coordinates requires $(p+1)^{r+1}$ coefficients. Even if
the same degree bound holds, the result is
$(\log n)^{O(r)}$, **not** a polylogarithm with an absolute exponent and
polynomial dependence on $m,d$. This is failure of that representation
to meet the requested complexity contract, not a neural-network lower
bound.

At depth $L\ge2$, (5) is unavailable: training reuses the initialized
hidden Gaussian matrix and its transpose. A low-rank trained increment
does not replace that initialized action by finitely many scalar sources.
An affirmative extension needs a proved, numerically evaluable compressed
description of the terminal observable's dependence on these reused
actions. Holomorphy in a large number of coordinates does not supply a
dimension-independent circuit or separation-rank bound. Nor does a
symbolic expectation node establish low evaluation workspace.

For a predeclared query panel, the query-dimension problem can disappear
from the **output representation**, but the high-dimensional numerical
expectations and their evolving training coefficients remain part of the
required faithful executable program. Predeclaring the panel therefore
does not by itself prove the full program-size theorem. Computing the
dense terminal answers in setup and discarding everything else is only
the excluded output-table construction.

## 9. Adversarial audit and route status

| Claim | Status and limitation |
|---|---|
| Exact shallow scalar reduction | Proved by substitution into the canonical GF |
| Endpoint and finite loss-based stop | Proved from the positive derivative in (8) |
| Numerical expectation elimination | Explicit finite quadrature compiler and finite polynomial evaluator |
| Absolute polylog retained size | Proved for fixed two-coordinate query structure only |
| Dense mean bias $O(n^{-1})$ | Proved by empirical-root expansion, (15)–(19) |
| Actual variability floor | Proved in RMS for (3), by untouched query Gaussian randomness |
| High-probability realized-pair comparison | Not proved and not substituted for RMS |
| Full unbounded holomorphic activation class | Not covered by the bounded-positive hypothesis (2) |
| General sample count and reused deep matrices | Open; no absolute-exponent numerical closure established |
| Generic cubature lower bound as neural no-go | Not asserted |
| Predeclared output cache as a solution | Explicitly excluded |

The strongest surviving obstruction to this route is structural: no
dimension-independent numerical representation has been shown for the
terminal predictor with growing training rank and deep matrix reuse.
The strongest counterinterpretation of the positive result is its narrow
architecture; it cannot be used as evidence that the deep Gaussian-action
problem is solved. Bounded-positive activation assumptions are visible
and are not silently imported into the broad request.

Recommended registry status: **complete as a restricted constructive
lemma; blocked as a route to the full theorem**. Reopen the general route
only with a proved dimension-independent terminal circuit/separation
mechanism or another estimate that bounds all numerical expectation
state, constants, and workspace by the requested polynomial. A mere
symbolic TP endpoint formula is not that missing bridge.

Inputs used: the neutral task assignment, the current shared notation and
book orientation, and the required process/presentation skills. No other
study's research or another live route's arguments were read. The initial
index search in the current predictor chapter was not used as a theorem
dependency. All mathematical dependencies needed for the scoped theorem
are derived above; no empirical computation, code edits, book edits, or Git
operations were performed.
