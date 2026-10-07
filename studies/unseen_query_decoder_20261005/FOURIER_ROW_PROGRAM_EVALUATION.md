# Counted-space expectation evaluation for finite row-interaction programs

2026-10-06. Scoped theoretical result, awaiting separate reconstruction.
No experiment, promotion, maintained-source change, or Git operation.

A finite causal program whose shared state consists of few empirical
row averages has a deterministic expectation algorithm whose workspace
is polynomial in the number of summaries, the dimension of one row,
the logarithms of its bounds and Lipschitz constants, and the requested
accuracy. The number of rows enters through its logarithm. The algorithm
does not retain the rows or their Gaussian initialization and does not
use an expectation or dense-matrix oracle.

The mechanism is exact Gaussian smoothing of the scalar updates followed
by Fourier inversion. After conditioning on the scalar summaries, row
independence replaces the entire row array by a single-row characteristic
function raised to the number of rows. All integrals then have dimension
at most twice the summary count plus one row dimension. Small workspace
comes with potentially enormous deterministic quadrature time.

The theorem below concerns a specified row-interaction program. Proving
that the desired trained-network observable has such a representation
with the stated quantitative bounds is a separate obligation. In
particular, no covariance-inverse or Gaussian-conditioning stability
claim is hidden in the result.

## 1. Program, assumptions, and computational contracts

Let $n,R,D$ be positive integers. The independent rows
$Z_1,\ldots,Z_n$ have law $N(0,I_D)$. Starting with no summaries, define
real scalars recursively by

\[
 C_r=\frac1n\sum_{i=1}^n F_r(Z_i;C_1,\ldots,C_{r-1}),
                  \qquad 1\leq r\leq R.
\tag{1}
\]

The same row $Z_i$ is reused at every step. The target is

\[
 \mathbb E\,\psi(C_1,\ldots,C_R).
\tag{2}
\]

An output that is another empirical average must be included as one
additional summary in (1), rather than left as an unrepresented row
dependence in (2).

Assume known numerical bounds $B,H,\Lambda,K\geq1$ such that, globally,

\[
 |F_r(z;c)|\leq B,\qquad |\psi(c)|\leq H,
\tag{3}
\]
\[
 |F_r(z;c)-F_r(\widetilde z;\widetilde c)|
 \leq\Lambda\bigl(\|z-\widetilde z\|_\infty
                         +\|c-\widetilde c\|_\infty\bigr),
 \qquad
 |\psi(c)-\psi(\widetilde c)|
                         \leq K\|c-\widetilde c\|_\infty.
\tag{4}
\]

Global bounds can be supplied by explicitly clipping input arguments to
a box on which these bounds hold. Clipping is nonexpansive. If (3) holds
on $[-B,B]^{r-1}$, all noiseless summaries are in $[-B,B]$; clipping
the summary arguments therefore leaves (1) unchanged. It defines the
function outside that box for the smoothing construction below.

Let $I$ count the retained description of the scalar instructions and
their numerical certificates. Fixed original activations may appear as
primitives in those instructions. An explicit straight-line instruction
list of length $I$ uses at most $I$ intermediate scalar registers beyond
its primitive evaluators. If a more succinct looping evaluator is used,
its actual workspace must instead be supplied and counted. There are
two distinct computational conclusions.

1. **Real-arithmetic conclusion.** Given exact evaluations of the stated
   scalar instructions, including the original activation primitives,
   the proof gives a finite deterministic algorithm with $O(R+D)$
   additional scalar registers beyond that instruction evaluator and
   polynomially many counter bits in the parameters below. Thus its
   register count is polynomial for the explicit instruction lists just
   described. It invokes no new solution-map or integration
   primitive. No computability assumption on an arbitrary allowed
   activation is added to this statement.
2. **Finite-bit conclusion.** Suppose the actual instruction code can
   evaluate every $F_r$ and $\psi$ on dyadic inputs, to absolute error
   $2^{-b}$, using at most $S_{\rm eval}(b,A,I,R,D)$ bits when argument
   magnitudes are at most $2^A$. This space includes the activation,
   fixed-data, and constant-precision interfaces and their scratch.
   It is a counted subroutine, not a free function oracle. Under this
   hypothesis the bit bound in (6) holds.

For $0<\varepsilon\leq1/4$, set

\[
 P=2+R+D+I+
 \left\lceil\log_2(2+n+B+H+\Lambda+K+\varepsilon^{-1})\right\rceil.
\tag{5}
\]

There is a universal constant $C_0$ for which the algorithm returns a
real number within $\varepsilon$ of (2), using at most

\[
 C_0P^8+
 S_{\rm eval}(C_0P^4,C_0P^2,I,R,D)
\tag{6}
\]

bits in the finite-bit model. The power eight is deliberately
conservative. If $R,D,I$ and all logarithms in (5) are absolute powers
of $\log(en)$, and the stated scalar-evaluation interface has polynomial
space dependence with an activation-only exponent, (6) is an absolute
polylogarithmic workspace bound. All retained instruction data and peak
live arrays are counted. There is no retained $n$-row array.

## 2. Gaussian update noise: exact density and approximation bias

Let $E_1,\ldots,E_R$ be independent standard normals, independent of
all rows. Define a noisy causal program by

\[
 C_r^\eta=\frac1n\sum_i F_r(Z_i;C_{<r}^\eta)+\eta E_r.
\tag{7}
\]

Couple it with (1) using the same rows. With
$e_r=\max_{j\leq r}|C_j^\eta-C_j|$ and $e_0=0$, (4) gives
$e_r\leq\Lambda e_{r-1}+\eta|E_r|$, because $\Lambda\geq1$.
Iteration and $\mathbb E|E_r|\leq1$ imply

\[
 \left|\mathbb E\psi(C^\eta)-\mathbb E\psi(C)\right|
 \leq K\eta\sum_{r=1}^R\Lambda^{R-r}
 \leq K\eta R(1+\Lambda)^R.
\tag{8}
\]

Choose a positive dyadic $\eta$ no larger than

\[
 \min\left\{\frac12,
 \frac{\varepsilon}{64KR(1+\Lambda)^R},
 \bigl[2\log(128HR/\varepsilon)\bigr]^{-1/2}\right\}.
\tag{9}
\]

A dyadic choice within a fixed factor of this minimum suffices. Then
(8) is at most $\varepsilon/64$, and
$\log\eta^{-1}=O(P^2)$.

Condition on the complete row array. At step $r$, the earlier summaries
have already been generated and the only fresh random variable is $E_r$.
Thus the exact conditional joint density of $C^\eta=c$ is

\[
 \prod_{r=1}^R\kappa_\eta\left(
 c_r-\frac1n\sum_iF_r(Z_i;c_{<r})\right),
 \qquad
 \kappa_\eta(x)=\frac{e^{-x^2/(2\eta^2)}}{\sqrt{2\pi}\eta}.
\tag{10}
\]

This follows by multiplying sequential conditional densities. It does
not require differentiability of the clipped functions or a formal
delta-function change of variables. When derivatives exist, the
corresponding triangular transformation has diagonal entries one, in
agreement with (10).

## 3. Truncate summaries before Fourier inversion

Take $M=B+1$, or a computable dyadic upper bound within a fixed factor,
and let $\mathcal C=[-M,M]^R$. The global cap in (3) gives
$|C_r^\eta|\leq B+\eta|E_r|$, regardless of the earlier summaries.
Consequently

\[
 \mathbb P\{C^\eta\notin\mathcal C\}
       \leq2R e^{-1/(2\eta^2)},
\tag{11}
\]

and (9) makes the contribution of this event to the expectation at
most $\varepsilon/64$.

Define the single-row characteristic function

\[
 \chi(c,\xi)=\mathbb E_Z\exp\left(
       -\frac{i}{n}\sum_{r=1}^R\xi_rF_r(Z;c_{<r})\right),
              \qquad Z\sim N(0,I_D).
\tag{12}
\]

It always satisfies $|\chi|\leq1$. The elementary Fourier identity

\[
 \kappa_\eta(x)=\frac1{2\pi}
       \int_{\mathbb R}e^{-\eta^2\xi^2/2+i\xi x}\,d\xi
\tag{13}
\]

follows by the Gaussian Fourier integral. Apply (13) to (10). Since
$c$ is now in a finite box, the absolute integrand is bounded by
$H e^{-\eta^2\|\xi\|_2^2/2}$, integrable in $(c,\xi)$ and under
the row probability law. Fubini is therefore justified before using
row independence. The result is the exact identity

\[
 \mathbb E\bigl[\psi(C^\eta)\mathbf 1_{C^\eta\in\mathcal C}\bigr]
 =\frac1{(2\pi)^R}\int_{\mathcal C}\int_{\mathbb R^R}
   \psi(c)e^{-\eta^2\|\xi\|_2^2/2+i\xi\cdot c}
                       \chi(c,\xi)^n\,d\xi\,dc.
\tag{14}
\]

Indeed the phase containing the rows is a product of $n$ identical-law
single-row factors. Conditioning on the summaries means that all
$F_r(Z_i;c_{<r})$ in this factorization have fixed scalar arguments;
it does not assert independence of the actual summaries and rows.

Truncating the summary box first is essential for this particular
absolute-integrability argument. No interchange over an unbounded
$c$ domain is being justified by oscillatory cancellation.

## 4. Fourier tails and the effect of oscillation

Restrict the frequency integral to $\mathcal X=[-V,V]^R$. Gaussian
integration and a coordinate union bound give

\[
 \frac1{(2\pi)^R}\int_{\mathbb R^R\setminus\mathcal X}
             e^{-\eta^2\|\xi\|_2^2/2}\,d\xi
 \leq(\sqrt{2\pi}\eta)^{-R}
                     2R e^{-\eta^2V^2/2}.
\tag{15}
\]

The absolute error in (14) is therefore at most
$H(2M)^R$ times the right side of (15). Choose $V\geq1$ such that

\[
 \frac{\eta^2V^2}{2}\geq
 \log\left(\frac{128HR}{\varepsilon}
       (2M)^R(\sqrt{2\pi}\eta)^{-R}\right).
\tag{16}
\]

A dyadic upper bound within a constant factor of the resulting $V$
is enough. The Fourier-tail error is at most $\varepsilon/64$, and
$\log V=O(P^2)$. Put

\[
 \mathcal V=(2M)^R(2V)^R.
\tag{17}
\]

Then $\log\mathcal V=O(P^3)$. This volume is large and must appear
in every numerical accuracy allocation below; it is not treated as one.

Write the integrand in (14), without its constant prefactor, as
$G(c,\xi)$. From $|e^{ix}-e^{iy}|\leq|x-y|$, (3)--(4), and
$|z^n-w^n|\leq n|z-w|$ for $|z|,|w|\leq1$, we obtain

\[
 |\chi(c,\xi)-\chi(\widetilde c,\xi)|
       \leq\frac{RV\Lambda}{n}\|c-\widetilde c\|_\infty,
\]
\[
 |\chi(c,\xi)-\chi(c,\widetilde\xi)|
       \leq\frac{RB}{n}\|\xi-\widetilde\xi\|_\infty.
\tag{18}
\]

The factors of $n$ cancel when these estimates are applied to
$\chi^n$. Bounding the other three factors separately yields

\[
 |G(c,\xi)-G(\widetilde c,\widetilde\xi)|
 \leq L_c\|c-\widetilde c\|_\infty
          +L_\xi\|\xi-\widetilde\xi\|_\infty,
\]
\[
 L_c=K+HRV(1+\Lambda),\qquad
 L_\xi=HR(M+B+\eta^2V).
\tag{19}
\]

Thus oscillation costs a frequency-dependent Lipschitz constant whose
logarithm is $O(P^2)$, not an unspecified contour condition. No
deformation of the real Fourier contour, positivity of $G$, or
stationary-phase approximation is used.

## 5. Counted evaluation of the single-row characteristic function

It suffices to compute $\chi$ uniformly on the outer boxes to accuracy

\[
 \delta=\frac{\varepsilon}{128nH\mathcal V}.
\tag{20}
\]

Truncate $Z$ to the integration box $[-A,A]^D$, with

\[
 A\geq1,\qquad A^2\geq2\log(16D/\delta).
\tag{21}
\]

The omitted Gaussian probability is at most $\delta/8$, because the
phase has modulus one. Here $A=O(P^{3/2})$ is sufficient. The truncated
integrand is

\[
 e^{-i\sum_r\xi_rF_r(z;c_{<r})/n}
                     (2\pi)^{-D/2}e^{-\|z\|_2^2/2}.
\tag{22}
\]

It is Lipschitz in the sup norm, with a valid bound

\[
 L_z=RV\Lambda/n+DA.
\tag{23}
\]

For the Gaussian density term, sum the absolute coordinate derivatives
on the box and bound each by $A$; for the phase use (4). Hence a tensor
midpoint rule with $Q_z$ subdivisions on each axis has error at most
$(2A)^D L_z A/Q_z$. Choose

\[
 Q_z\geq 32(2A)^D(1+L_z)A/\delta.
\tag{24}
\]

Then $\log Q_z=O(P^3)$. The quadrature loops retain only one $D$-tuple
of indices, one row point, the fixed $(c,\xi)$, and a complex
accumulator. The values $F_r(z;c_{<r})$ are computed by executing their
specified scalar instructions; they are not looked up in a dense row
table. Allocate a further $\delta/8$ each to function evaluation and
arithmetic. For example, a uniform integrand-evaluation error
$\delta/[8(2A)^D]$ suffices for its integral contribution.

The approximate quadrature need not lie in the unit disk. Project it
onto that disk before taking a power; denote the result by
$\widehat\chi$. Euclidean projection onto a closed convex set is
nonexpansive and fixes $\chi$, which is in the disk. This follows from
the two nearest-point variational inequalities, added together. Thus
projection does not increase the error, and the preceding allocations
give $|\widehat\chi-\chi|\leq\delta$. Consequently

\[
 |\widehat\chi^n-\chi^n|\leq n\delta.
\tag{25}
\]

Repeated squaring computes the integer power using $O(\log n)$ steps
and a fixed number of complex registers. In the finite-bit model,
projecting each approximate product onto the unit disk preserves a
bound $C n\rho$ when individual arithmetic errors are at most $\rho$:
a squaring doubles the propagated error and a product adds the two
input errors, so induction on its addition chain gives that estimate.
Requesting $O(\log n)$ further precision bits is sufficient. An
approximate numerical disk projection is given its own error budget;
no exact finite-bit norm comparison is assumed.

Equations (20) and (25) make the contribution to the outer integral at
most $\varepsilon/128$, before its separately allocated power-arithmetic
error. A raw approximation with uncontrolled modulus $1+\delta$ would
instead give an avoidable amplification factor $(1+\delta)^{n-1}$;
the disk projection makes the estimate explicit and uniform.

## 6. Outer quadrature, total error, and peak workspace

Use a tensor midpoint grid with $Q$ subdivisions per coordinate of
$\mathcal C\times\mathcal X$. By (19), the exact-grid integration
error is at most

\[
 \mathcal V(L_c+L_\xi)\max(M,V)/Q.
\tag{26}
\]

The prefactor $(2\pi)^{-R}\leq1$ only reduces this bound. Choose

\[
 Q\geq128\mathcal V(1+L_c+L_\xi)\max(M,V)/\varepsilon.
\tag{27}
\]

Again $\log Q=O(P^3)$. At each outer grid point evaluate $\psi$,
the elementary exponential factors, and the approximate power in
Section 5, at sufficient absolute precision that the additional
integral error is at most $\varepsilon/16$. Every bound required for
this allocation has already been displayed: $H$, $\mathcal V$, $n$,
and the elementary factor magnitudes. Negative and complex summands
are accumulated with absolute, not relative, error control. Take the
real part at the end; the exact quantity is real.

The bias (8), summary tail (11), Fourier tail (15), row tail and row
quadrature, power approximation, outer quadrature, and remaining
arithmetic budgets sum to less than $\varepsilon$. Increasing the
fixed numerical constants in (20), (24), or (27) leaves slack for
dyadic parameter bounds and routine rounding.

Here is the explicit space accounting. The estimates above give

\[
 \log\eta^{-1},\log V=O(P^2),\quad
 \log\mathcal V,\log\delta^{-1},\log Q,\log Q_z=O(P^3),
\]
\[
 \log(Q^{2R}),\log(Q_z^D)=O(P^4).
\tag{28}
\]

Sequential summation must include the last two quantities in its
roundoff budget: there are that many summands, even though the
integration volumes have smaller logarithms. With $b=C_0P^4$
working precision, the roundoff per summand can be at most the allotted
absolute error divided by the number of summands. Accumulating weighted
cell contributions keeps the absolute sum bounded by the integration
volume times the integrand cap; no large unweighted sum is necessary.

The outer indices, $c,\xi$, inner row indices and $z$, and all
accumulators occupy $O(P^5)$ bits at this conservative precision.
The scalar instruction subroutine uses the additional term in (6).
Elementary real/complex arithmetic, square roots, exponentials and
trigonometric functions have direct $O(b^2)$-space implementations:
use integer arithmetic, bisection, argument reduction and convergent
Taylor series, with integer-part bits included. All relevant input
magnitudes have logarithm $O(P^2)$, already covered by $b$.
This proves the safe $O(P^8)$ overhead in (6).

In particular, the tensor grids are never materialized. Their indices
are incremented like mixed-radix counters. The $n$ independent rows
are also never materialized: $n$ appears only in the phase denominator,
the integer power, and their precision requirements. Neither an
arbitrary-real encoding of the row array nor a random-access Gaussian
root tape is retained.

In the real-arithmetic version, the same finite grids and loops use
$O(R+D)$ scalar registers beyond the workspace of the supplied scalar
instruction evaluator, plus the polynomial-size integer counters in
(28). Values at quadrature nodes are obtained by actual finite calls
to those instructions and their activation primitives. The separate
finite-bit hypothesis is necessary because a holomorphic activation
may contain noncomputable constants; the real-arithmetic theorem does
not silently rule such activations out.

## 7. Root clipping and smooth threshold tests

If boundedness and Lipschitz certificates are available only when row
marks satisfy $\|Z_i\|_\infty\leq A_0$, replace marks in the scalar
instructions by coordinatewise clipping at $A_0$. The clipped program
agrees with the original one except on an event of probability at most
$2nD e^{-A_0^2/2}$. For bounded output $H$, this changes its expectation
by at most $4HnD e^{-A_0^2/2}$. Therefore a cap with

\[
 A_0^2\geq2\log(64HnD/\varepsilon)
\tag{29}
\]

costs only a further small error budget. The clipped instructions must
still have the stated summary-argument bounds and a quantitative
Lipschitz certificate. Clipping alone does not bound an inverse of a
nearly singular empirical Gram matrix.

For approximate distribution functions, take a bounded Lipschitz
threshold function. For example, a ramp with transition interval
$[a-\sigma,a+\sigma]$ has Lipschitz constant $1/(2\sigma)$ and
satisfies

\[
 \mathbb P\{C_R\geq a+\sigma\}
 \leq\mathbb E\psi_{a,\sigma}(C_R)
 \leq\mathbb P\{C_R>a-\sigma\}.
\tag{30}
\]

Thus inverse-polynomial $\sigma$ contributes only $O(\log n)$ to
$\log K$. Constant final expectation accuracy is permitted in the
theorem even when $\sigma$ is very small; the smaller internal update
noise in (9) absorbs the threshold sensitivity. No anti-concentration
assumption is needed for the bracket (30). Identifying an exact CDF
value at an atom would be a different claim.

## 8. Conditional decoding from retained noisy training summaries

There is a conditional version which holds the present historical
summaries fixed instead of solving their scalar recursion during a
query. Let the retained training state be the noisy-update summaries
$C=C^{\eta_{\rm tr}}$ of (7), with a fixed known
$0<\eta_{\rm tr}\leq1$. For a realized value $c$, define the likelihood

\[
 L_c(Z_1,\ldots,Z_n)=\prod_{r=1}^R\kappa_{\eta_{\rm tr}}
 \left(c_r-\frac1n\sum_iF_r(Z_i;c_{<r})\right),
 \qquad p(c)=\mathbb E L_c.
\tag{31}
\]

Thus $p$ is the actual density of the retained training state.
In particular it is not the density obtained by adding noise only
after the noiseless training program has finished. That different
observation model would generally require integration over latent
training summaries.

Suppose a passive query is represented, with $c$ held fixed, by $S$
further scalar summaries

\[
 Q_s=\frac1n\sum_i G_s(Z_i;c,Q_{<s}),\qquad 1\leq s\leq S,
\tag{32}
\]

with global caps and joint Lipschitz bounds of the same form as (3)--(4).
Any extra independent query Gaussian marks can be included in $Z_i$;
the training functions ignore them. The quantity to evaluate is
$\mathbb E[\psi(Q)\mid C=c]$. Add independent update noise of scale
$\eta_{\rm q}$ only to (32), chosen as in (9) with its own summary
count and sensitivity constants. For every fixed row array and $c$,
the coupling proof (8) bounds this query-noise bias. Averaging under
the conditional row law preserves that bound: conditioning introduces
no factor $1/p(c)$ into this uniform coupling estimate.

The joint training/query density is represented using

\[
 \chi(c,q;\xi,\zeta)=\mathbb E_Z\exp\left\{-\frac{i}{n}
 \left[\sum_{r=1}^R\xi_rF_r(Z;c_{<r})
       +\sum_{s=1}^S\zeta_sG_s(Z;c,q_{<s})\right]\right\}.
\tag{33}
\]

For fixed $c$, integrate the numerator only over a bounded query box
$q\in[-M_{\rm q},M_{\rm q}]^S$ and the Fourier variables:

\[
 \begin{split}
 N(c)=\frac1{(2\pi)^{R+S}}\int dq\int d\xi\,d\zeta\,
 &\psi(q)\exp\left[-\frac{\eta_{\rm tr}^2\|\xi\|^2}{2}
                  -\frac{\eta_{\rm q}^2\|\zeta\|^2}{2}
                  +i\xi\cdot c+i\zeta\cdot q\right]\\
 &\hspace{20mm}\cdot\chi(c,q;\xi,\zeta)^n.
 \end{split}
\tag{34}
\]

Before frequency truncation this is the exact numerator for the noisy
query expectation restricted to that query box. The denominator is
the same Fourier formula with no query variables or query factor.
Absolute integrability follows exactly as in Section 3, since $c$ is
fixed and the $q$ domain is bounded. There is **no training-$c$
integration in (34)**. Evaluating a row function uses the supplied
values $c_{<r}$ as fixed coefficients; it does not recompute an empirical
training average or update the stored training state.

The two frequency-tail contributions in (34) are bounded by

\[
 H(2M_{\rm q})^S
 (\sqrt{2\pi}\eta_{\rm tr})^{-R}
 (\sqrt{2\pi}\eta_{\rm q})^{-S}
 \left[2R e^{-\eta_{\rm tr}^2V_{\rm tr}^2/2}
        +2S e^{-\eta_{\rm q}^2V_{\rm q}^2/2}\right].
\tag{35}
\]

The denominator has the corresponding training-only bound. The query
box tail, after division by the exact denominator, is at most
$2HS e^{-1/(2\eta_{\rm q}^2)}$ when $M_{\rm q}=B_{\rm q}+1$.
These formulas give explicit cutoffs and error budgets; no conditional
row independence is asserted. It is Fourier factorization of the
unconditioned iid row measure with its likelihood that yields (33).

There is a distribution-free lower density bound at the observed state.
For any training box $\mathcal C$ of volume $V_{\rm tr}$ and any
$0<\rho<1$,

\[
 \mathbb P\{C\in\mathcal C,\ p(C)<\rho/V_{\rm tr}\}
 =\int_{\mathcal C\cap\{p<\rho/V_{\rm tr}\}}p(c)\,dc
 \leq\rho.
\tag{36}
\]

For $\mathcal C=[-M,M]^R$, its outside probability is bounded by
(11). Thus, except on probability at most that tail plus $\rho$, the
actual denominator obeys

\[
 p(C)\geq d_*:=\rho/(2M)^R.
\tag{37}
\]

If $p\geq d_*$, $|\widehat p-p|\leq d_*/2$, and $|N|\leq Hp$,
then elementary division gives

\[
 \left|\frac{\widehat N}{\widehat p}-\frac Np\right|
 \leq\frac{2}{d_*}
           (|\widehat N-N|+H|\widehat p-p|).
\tag{38}
\]

Take both absolute integration errors at most
$\varepsilon d_*/[32(1+H)]$, and add the already uniform query-noise
and query-tail budgets. The conditional result has error at most
$\varepsilon$. Its precision depends on
$\log d_*^{-1}=\log\rho^{-1}+R\log(2M)$, not on a reciprocal
denominator stored at unit cost.

To define the decoder outside this density event as well, return zero
whenever the computed real denominator $\widehat p$ is below $d_*/4$;
otherwise form the quotient. Use the same absolute integration tolerance
at a rounded state $\widetilde c$. On the rounded-density event proved
below, $p(\widetilde c)\geq d_*/2$, so the tolerance
$\varepsilon d_*/[32(1+H)]<d_*/4$ ensures that this fallback is
inactive.

The quadrature now has $R+2S$ outer variables and $D$ row variables.
Repeating Sections 4--6 gives (6) with a parameter $P$ enlarged by
$S$, $\log\eta_{\rm tr}^{-1}$, $\log\rho^{-1}$, and the query
instruction lengths and logarithmic bounds. In particular the same
polynomial-space conclusion holds when these are polylogarithmic.
It uses the retained historical coefficients as inputs and evaluates
their row functions. It does not run the nonlinear training scalar
recursion (1) at query time. The cost of evaluating those specified
history-dependent row functions is nevertheless counted; it can grow
with the finite history length $R$.

### Finite precision of the retained state

The density statement (36) is for the ideal continuous noisy state.
It must not be asserted for a rounded discrete state. Instead, posterior
continuity permits finite-bit retention. Put
$P_{\max}=(\sqrt{2\pi}\eta_{\rm tr})^{-R}$.
The one-dimensional Gaussian density derivative and a product
telescoping bound give, uniformly over every row array,

\[
 |L_c-L_{\widetilde c}|
 \leq L_{\rm den}\|c-\widetilde c\|_\infty,
 \qquad
 L_{\rm den}\leq
 C R(1+\Lambda)P_{\max}/\eta_{\rm tr}.
\tag{39}
\]

Let $g(z_1,\ldots,z_n;c)$ be the expected bounded noisy-query test
for fixed rows. If $\Lambda_{\rm q}\geq1$ bounds the joint Lipschitz
constants of the query functions, couple their noises at $c$ and
$\widetilde c$. Their summary differences satisfy
$e_s\leq\Lambda_{\rm q}(\|c-\widetilde c\|_\infty+e_{s-1})$.
Iteration gives, for example,
$L_g\leq KS\Lambda_{\rm q}(1+\Lambda_{\rm q})^S$.
Its logarithm is polynomial in the stated parameters. The full untruncated numerator
$\mathbb E[L_c g(c)]$ therefore has Lipschitz bound

\[
 L_N\leq P_{\max}L_g+H L_{\rm den}.
\tag{40}
\]

If $p(c)\geq d_*$ and the retained $\widetilde c$ obeys

\[
 \|c-\widetilde c\|_\infty\leq
 \min\left\{\frac{d_*}{2(1+L_{\rm den})},
 \frac{\varepsilon d_*}{16(1+L_N+H L_{\rm den})}\right\},
\tag{41}
\]

then $p(\widetilde c)\geq d_*/2$ and the posterior expectations at
$c$ and $\widetilde c$ differ by at most $\varepsilon/8$, using
the same ratio calculation as (38). The logarithm of the required
precision is polynomial in the stated parameters. Thus the ideal
state may be rounded before storage, provided its construction also
meets that accuracy. The decoder approximates the posterior function
at the ideal observed state; it is not claimed to compute exactly
the posterior conditioned on a quantization bin.

For finitely many historical prefixes, apply (36) at each prefix with
failure budget $\rho/R$. The additional precision cost is only
$O(\log R)$. This does not prove a statement for infinitely many
independently observed noisy states; a finite causal chronology is
part of the hypothesis.

## 9. Scope of the result

This theorem removes the dense row randomness from expectation
evaluation of (1) by exploiting its finite scalar-summary structure.
It does not follow merely from low workspace for an arbitrary random-
access computation. The decisive assumptions are the exact iid-row
representation, the finite causal summary count, bounded extensions,
quantitative Lipschitz bounds, and an explicit counted evaluator for
the row instructions.

If those parameters are absolute-polylogarithmic on their logarithmic
scales, the workspace conclusion is genuine. Singular regression
formulas, unbounded coefficient sensitivity, missing response terms,
or an output depending on unrepresented row information must be repaired
before applying the theorem. No such repair or dense-to-row identification
is claimed here.

Scientific input for this derivation was the supervisor's specified
finite row-interaction model. The conditional activation/data computation
interface is the already-authorized current-study recomputation interface.
All probability, Fourier, truncation and quadrature estimates needed
for the new result are derived above; no external integration theorem
is invoked. Required rigorous-math and conjecture-audit instructions
were applied. The previously reported canonical-skill access restriction
is unchanged.
