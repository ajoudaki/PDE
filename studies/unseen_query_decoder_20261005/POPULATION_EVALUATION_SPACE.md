# A counted evaluator for a finite capped Gaussian program

2026-10-06. Constructive numerical result, conditional on the specified
finite Gaussian program. No dense-width identification or experiment.

A finite causal scalar Gaussian program with explicit smooth caps has a
deterministic expectation evaluator whose total retained coefficients,
precision and scratch use polynomial space in program size and
$\log(1/\varepsilon)$. Singular covariance matrices are permitted. The proof
uses weak covariance interpolation for error propagation and a small ridge
only inside numerical Gaussian integration. It does not propagate a
square-root covariance error from stage to stage.

The caps are a specified change to the candidate numerical program. Their
identity on the intended population trajectory, or agreement of the capped
program with the actual dense network, is not established here. Unregularized
history-Gram inverses are not covered by a hidden conditioning assumption.
These distinctions are essential to the result's scope.

## 1. Finite program and computational contract

Let $R\ge2$ bound the number of scalar nodes in each integrand DAG and the
dimension of each Gaussian integral. Let the number of retained scalar
coefficients and their causal evaluation stages be at most $R^b$, for a
fixed absolute integer $b$. A covariance matrix counts all its entries;
its dimension is at most $R$. The instruction schema is explicit and also
has polynomial size in $R$. Coefficients at a stage depend only on earlier
coefficients, through arithmetic or a Gaussian expectation. There is no
solution-map or integration oracle.

The scalar instructions are affine combinations, products, activations and
activation derivatives, and the explicit smooth cap defined below. Let
$J$ be the largest activation derivative order directly requested by an
instruction. Response integrands may request a specified partial derivative
of a scalar DAG output of total order at most $q$. Covariance integrands are
products of two bounded scalar fields. Such a terminal product counts as
an additional ordinary node. The retained Gaussian covariance at every
exact stage is positive semidefinite; for Gram expectations of bounded
fields this is an identity, not an eigenvalue-gap hypothesis.

Response derivatives refer to the declared ambient Gaussian arguments of
the explicit scalar function, including off the support of a singular
Gaussian law. An almost-sure equivalence class does not determine those
derivatives. Raw operations and their subsequent caps each count toward
the node bound $R$.

Every scalar field node, including Gaussian input nodes, is capped. Raw
arithmetic inside a node has bounded arity and is followed by a cap; an
affine sum can instead have at most $R$ arguments. Every deterministic
response coefficient is capped as well. Covariance entries are computed
as actual expectations of products of capped fields and are not clipped
entry by entry, which could destroy positive semidefiniteness. The resulting
coefficient magnitudes are bounded by $C_B=4B^2+2$, where $B\ge1$ is the
cap scale. Fixed Gaussian means can be included as earlier bounded
coefficients. Gaussian coordinates enter their first cap before being
multiplied by a variable coefficient.

An ordinary matrix inverse is not an allowed primitive unless an effective
derivative/conditioning certificate is supplied. An explicitly regularized
inverse can be included if its regularization parameter has polynomial bit
length and its derivative bounds are included. The main theorem below uses
an inverse-free coefficient program; it imposes no positive history-Gram
gap. Whether that program correctly describes the dense reused matrices
is a separate identification question.

Activations are real on the real axis and holomorphic on
$|\operatorname{Im}z|<a$, with
$|\phi(0)|\le S$ and $\sup|\phi'|\le S$, where $S\ge1$ and
$a>0$ are supplied numerical bounds. On rational real arguments, each
activation has a deterministic evaluation algorithm using a fixed
polynomial amount of space in requested precision and input bit length.
All layer activations share that polynomial exponent $c$. Higher
derivatives are computed below; no additional derivative oracle is assumed.
Data and cap parameters are rational or have repeatable precision access
with the same counted polynomial-space property.
All fixed program descriptions and numerical bounds are counted in the
fixed-input bit length below. A supplied bound means an ordinary binary
numerical bound, not a compressed tower with uncounted expansion length.

Write

\[
 U=R+J+q+\log(2+B)+\log(2+S)+\log(2+a^{-1})
       +\text{fixed-input bit length}+\log(\varepsilon^{-1}).       \tag{1}
\]

**Theorem.** For the capped finite program just specified, every requested
scalar coefficient and output can be evaluated deterministically to
absolute error at most $\varepsilon\in(0,1)$ with total space polynomial
in $U$. The exponent depends only on the fixed coefficient-count exponent
$b$, the scalar-evaluation exponent $c$, and the fixed primitive types.
It is independent of the original network depth $L$, sample count $m$ and
input dimension $d$. Runtime is unrestricted. No initialized dense array,
random root oracle, covariance spectral gap or exact integral oracle is
used.

In particular, if $R,J,q,\log B$ and the other input quantities in (1)
are bounded by fixed powers of $\log n$ with absolute exponents, the
evaluator uses an absolute power of $\log n$ bits. This is a numerical
theorem for the explicitly defined program, not a claim that the original
population candidate already has the same caps or a proved dense-width
comparison.

The proof first certifies all needed derivatives, then constructs a single
Gaussian integral evaluator, and finally propagates coefficient errors
linearly through the chronology.

## 2. Explicit smooth caps and derivative growth

Put $Q=q+3$ and choose $k=Q$. Define

\[
 c_k=\left(\int_0^1 t^k(1-t)^k\,dt\right)^{-1}
     =\frac{(2k+1)!}{(k!)^2},\qquad
 s_k(t)=1-c_k\int_0^t u^k(1-u)^k\,du.
\]

For $x\ge0$, define

\[
 \sigma_B(x)=
 \begin{cases}
 x,&0\le x\le B,\\
 B+B\displaystyle\int_0^{(x-B)/B}s_k(t)\,dt,&B<x<2B,\\
 3B/2,&x\ge2B,
 \end{cases}                                                     \tag{2}
\]

and extend it oddly. The symmetry $s_k(1-t)=1-s_k(t)$ gives
$\int_0^1s_k=1/2$, so the pieces meet. Since $s_k(0)=1$,
$s_k(1)=0$ and its derivatives through order $k$ vanish at the matching
endpoints whenever required by the adjacent constant derivatives,
$\sigma_B$ is $C^{k+1}$. It is the identity on $[-B,B]$, has magnitude
at most $3B/2$, and $0\le\sigma_B'\le1$.

All transition pieces are explicit rational polynomials when $B$ is rational.
Expanding $u^k(1-u)^k$ shows that its coefficient absolute sum is $2^k$.
Also $c_k\le(2k+1)4^k$. Consequently, for $1\le j\le k+1$,

\[
 \sup_x|\sigma_B^{(j)}(x)|
 \le B^{1-j}\exp\{Ck\log(k+2)\},                              \tag{3}
\]

after enlarging a universal $C$. Polynomial differentiation and the
endpoint matching prove this on every piece. Evaluating these derivatives
uses polynomial space in $k$, $\log B$ and the requested precision.
Near a piece boundary the next bounded derivative controls input-rounding
error; a discontinuous derivative test is not being used.

Cauchy's formula applied to $\phi'$ on a circle of radius $a/2$ gives,
for every integer $j\ge1$ and real $x$,

\[
 |\phi^{(j)}(x)|\le S(j-1)!(2/a)^{j-1},
 \qquad |\phi(x)|\le S(1+|x|).                                 \tag{4}
\]

Thus the primitive derivatives through order $Q$ require activation
derivatives only through order $J+Q$. Their logarithmic bounds are
polynomial in $J+Q,\log S,\log(2+a^{-1})$. All operands at an arithmetic
node are bounded by a fixed polynomial in $B$ and $R$; its raw output
before capping has the same type of bound. Raw activation-derivative values
instead have the possibly larger bound (4), whose logarithm is still
polynomial in the stated parameters; their following cap restores the
field range.

### Composition does not require an exponential derivative order

Here is a derivative estimate that avoids repeatedly raising the preceding
derivative bound to the power $Q$. For each primitive, uniformly over its
permitted coefficient range and input range, bound the sum of absolute
normalized Taylor coefficients of degree $j$ by $A^j$, $1\le j\le Q$.
Equations (3)–(4), the product rule and the bounded affine coefficients
allow an $A\ge2$ with

\[
 \log A\le C\bigl[
 (J+Q+1)\log(J+Q+2)
 +(J+Q+1)\log(2+a^{-1})+\log(2+S)
 +Q\log(Q+2)+\log(2+B)+\log(R+2)\bigr].                         \tag{5}
\]

Gaussian coordinates themselves are unbounded arguments only of the first
cap, whose derivative bounds are global. Coefficient interpolation is taken
in the enlarged box of magnitude at most $2C_B$; (5) covers that box too.

For formal increments whose coordinate absolute values are at most $t$,
the absolute Taylor series of a primitive increment is dominated through
order $Q$ by

\[
 T(u)=\frac{Au}{1-Au}.
\]

Starting from input increment $t$, and taking the largest majorant over all
preceding nodes, each new node is bounded by one further composition with
$T$. Direct substitution gives

\[
 T^{\circ j}(t)=
 \frac{A^jt}{1-(A+A^2+\cdots+A^j)t}.
\]

Its degree-$r$ coefficient is at most $(2A)^{jr}$. Taylor coefficients of
a $C^Q$ composition through degree $Q$ depend only on the corresponding
finite jets, so this formal majorization does not assume complex analyticity
of the cap. At every scalar DAG node and for every multi-index $\alpha$
in Gaussian coordinates and coefficient parameters, $1\le|\alpha|\le Q$,

\[
 |\partial^\alpha F|\le |\alpha|!(2A)^{R|\alpha|}.              \tag{6}
\]

The same statement includes a terminal product when that product is counted
among the nodes. Products and caps of finitely many requested scalar outputs
are handled by adding their stated nodes. One may therefore use the common
bound

\[
 E=(1+4B^2)\,Q!\,(2A)^{RQ}                                    \tag{7}
\]

for a base integrand and all its derivatives through $Q$. The logarithm
of $E$ is polynomial in the parameters in (1). In particular a response
integrand $g=\partial^\beta F$, $|\beta|\le q$, has globally bounded
value, two spatial derivatives, and one coefficient derivative, each at
most $E$. No derivative order doubles with the number of covariance stages.

### Evaluating derivatives without a derivative oracle

For a multi-index $\beta$ of order $r\le q$, represent it by a list of
coordinate directions $i_1,\ldots,i_r$, with repetitions allowed. Order
zero is direct scalar-DAG evaluation. For $r\ge1$, iterated
forward differences obey the repeated fundamental-theorem identity

\[
 h^{-r}\Delta_{he_{i_1}}\cdots\Delta_{he_{i_r}}F(x)
 =\int_{[0,1]^r}
   \partial^\beta F\left(x+h\sum_{j=1}^r t_je_{i_j}\right)dt.
\]

Its error from $\partial^\beta F(x)$ is at most $rhE$, using the next
derivative in (7). To attain error $\delta$, choose
$h\le\delta/(2rE)$, enumerate the $2^r$ difference terms using an
$r$-bit counter, and evaluate each underlying $F$ to error at most
$\delta h^r/2^{r+1}$. The required precision is
$O(r\log(\delta^{-1})+r\log E+r\log(r+2))$, polynomial in the
stated parameters. Store the shifted coordinate vector and one accumulator,
not the difference table.

The identical one-dimensional construction computes $\phi^{(j)}$ from
the permitted activation evaluator, using (4) at order $j+1$ to select
the step. Its requested precision is polynomial in $j$ and the output
precision. The extra activation derivative order is available from strip
holomorphy. Error propagation through the $R$ scalar nodes uses their
first-derivative bounds from (5)–(6), adding only a polynomial number of
precision bits. Thus (7) is accompanied by an actual evaluator.

## 3. One singular Gaussian expectation

Consider $\mathbb E g(X;c)$ with $X\sim N(\mu,Q_0)$,
$Q_0\succeq0$, dimension $r\le R$, and the derivative bounds (7).
The earlier coefficients are denoted $c$. The means, covariance entries
and coefficients have certified bounds; in the capped program covariance
entries of Gram fields are at most $4B^2$. Fixed larger numerical bounds
can be supplied as part of (1).
Dimension zero is deterministic evaluation; the formulas below treat
$1\le r\le R$.

For positive-semidefinite $Q_0,Q_1$, the weak interpolation identity is

\[
 \mathbb E g(N(\mu,Q_1);c)-\mathbb E g(N(\mu,Q_0);c)
 =\frac12\int_0^1\sum_{i,j}(Q_1-Q_0)_{ij}
              \mathbb E\partial_{ij}g(N(\mu,Q_s);c)\,ds,
 \quad Q_s=(1-s)Q_0+sQ_1.                                      \tag{8}
\]

For completeness, add $\nu I$ to both endpoints, differentiate the
Gaussian density along the covariance segment and integrate by parts twice.
The bounded derivatives justify both integrations. Couple the regularized
laws by adding $\sqrt\nu Z$ and let $\nu\downarrow0$; boundedness
and continuity give (8) by dominated convergence. This is precisely the
singular-covariance weak identity from the assigned source, with all its
growth hypotheses satisfied here globally. Hence

\[
 |\Delta\mathbb E g|\le(E/2)\sum_{i,j}|(Q_1-Q_0)_{ij}|.          \tag{9}
\]

Mean and coefficient perturbations have the ordinary first-derivative
bound, with the sums of coordinate errors times $E$.

Suppose rational entry approximations form a symmetric matrix $\widetilde Q$
with a certified entrywise error at most $e$ from $Q_0$. Set

\[
 \widehat Q=\widetilde Q+(re+h)I,
 \qquad h>0.                                                     \tag{10}
\]

Since the operator error is at most $re$, $\widehat Q\succeq hI$.
Its entrywise distance from $Q_0$ is at most $(r+1)e+h$, and (9)
controls this perturbation linearly. The ridge will be chosen so small
that $Er^2h$ fits the local error budget. No lower bound on an eigenvalue
of $Q_0$ is required.

### Numerical Cholesky with a counted precision bound

Let $V\ge1$ be a known upper bound for $\|\widehat Q\|_{\rm op}$.
The Cholesky formulas compute a lower triangular matrix $C$ with
$CC^T=\widehat Q$. Every exact squared pivot is at least $h$: it
is a diagonal entry of a Schur complement, and that complement is
at least $hI$ by minimizing the quadratic form of $\widehat Q$ over
the eliminated variables. Each exact factor entry has magnitude at most
$\sqrt V$.

The scalar formulas use sums/products, square roots at arguments at least
$h$, and division by numbers at least $\sqrt h$. On a neighborhood in
which pivots remain at least $h/2$ and factor entries at most
$2\sqrt V$, their Lipschitz constants are bounded by a fixed power of
$r,V,h^{-1}$. There are $O(r^3)$ scalar operations. Induction through
them therefore bounds arithmetic amplification by
$[C r(1+V)(1+h^{-1})]^{C r^3}$. Choosing

\[
 p_C\ge C r^3\log\bigl(Cr(1+V)(1+h^{-1})\bigr)
             +\log(\delta_C^{-1})                              \tag{11}
\]

bits, with an enlarged constant, gives entrywise factor error at most
$\delta_C$ and keeps the pivots in the stated neighborhood. This closes
the induction rather than assuming stability at a zero pivot. All $r^2$
factor entries may be stored; that is polynomial in $R$.

An approximate factor $\widetilde C$ defines the positive-semidefinite
covariance $\widetilde C\widetilde C^T$. Its distance from
$CC^T$ is bounded by the elementary product subtraction, so selecting
$\delta_C$ a polynomial factor smaller than the covariance tolerance
controls it by (9). Equation (11) has polynomial length in
$R,\log V,\log(h^{-1})$ and the requested error bits. This factorization
is an internal numerical device; none of its square-root perturbation
bounds are passed as the next causal stage's error.

### Streamed deterministic quadrature

Write $X=\mu+\widetilde C Z$, with $Z$ standard Gaussian in $r$
dimensions. The integrand magnitude is at most $E$. A union bound gives
$\Pr(\|Z\|_\infty>T)\le2r e^{-T^2/2}$; choose

\[
 T^2\ge2\log(8rE/\eta)                                        \tag{12}
\]

for a local target error $\eta$. The omitted tail is at most $\eta/4$.
On the cube $[-T,T]^r$, let
$u(z)=g(\mu+\widetilde C z;c)(2\pi)^{-r/2}e^{-\|z\|^2/2}$.
Its coordinate derivatives have magnitude at most
$L_u=E(Cr\sqrt V+T+1)$, by the chain and product rules, allowing the
small factorization error in the constant.

A tensor midpoint rule with $N$ equal subintervals per coordinate has
error at most

\[
 (2T)^r\,r L_u T/N.
\]

Thus choose $N\ge4(2T)^r rL_uT/\eta$. Its logarithm obeys

\[
 \log N\le C\bigl[\log(\eta^{-1})+\log E
        +r\log(T+2)+\log(V+2)+\log(r+2)\bigr].                 \tag{13}
\]

Enumerate the $N^r$ nodes with $r$ counters, retain their $r$ coordinates,
evaluate one scalar DAG, multiply by the quadrature weight, and accumulate.
Allocate at most $\eta/(4N^r)$ rounding error to each contribution.
The integrand evaluation tolerance includes the quadrature weight; allowing
an additional $O(r\log(2T))$ bits covers any weight larger than one.
The accumulator and counters need only
$O(r\log N+\log E+\log(\eta^{-1}))$ bits each up to fixed polynomial
factors. Gaussian density evaluation uses elementary square-root,
exponential and $\pi$ algorithms at this same polynomial precision.
Explicitly, bisection computes square roots; the alternating arctangent
series and $\pi=16\arctan(1/5)-4\arctan(1/239)$ compute $\pi$ with
a geometric remainder bound. On this cube, the exponential argument has
magnitude at most $rT^2/2$, polynomial in the stated parameters. Its
Taylor series, with factorial remainder bounded by
$e^{rT^2/2}(rT^2/2)^{M+1}/(M+1)!$, needs only polynomially many terms
in $rT^2$ and the requested bits. One running term and accumulator suffice.
The finite-difference evaluator in Section 2 supplies response integrands
to the required absolute tolerance. Equations (11)–(13) therefore describe
a finite, deterministic, polynomial-space integral algorithm.

## 4. Causal coefficient errors remain linear

Let $s\le R^b$ be the number of coefficient stages and let $e_j$ be a
certified maximum coordinate error after stage $j$. Each expectation's
integrand depends on at most polynomially many earlier coefficients, and
its first coefficient derivatives are bounded by $E$. Its covariance and
mean are earlier entries or specified bounded arithmetic functions of
them. Their numerical Lipschitz bounds must be included in the primitive
certificate; for direct Gram entries and means they are one.

Use the PSD repair (10) with the certified preceding covariance error, not
an estimated smallest eigenvalue. Equations (9)–(10) and the coefficient
derivative bounds give one uniform scalar constant $A_*\ge2$, with
$\log A_*$ polynomial in (1), such that

\[
 e_{j+1}\le A_*e_j+\tau.                                        \tag{14}
\]

For example, the covariance repair contributes at most a constant times
$Er^3e_j$ when its entries are previous coefficients, and coefficient
substitution contributes at most $Es e_j$. Smooth capping of a response
coefficient has Lipschitz constant one. Covariance entries remain genuine
Gram expectations; only the numerical integration law receives the ridge.

Choose every local quadrature, arithmetic and coefficient-rounding budget
as a sufficiently small fixed fraction of

\[
 \tau=\frac{\varepsilon}{4s(1+A_*)^s},
 \qquad h\le\frac{\tau}{C E R^2}.                              \tag{15}
\]

Quantize external input coefficients with the corresponding initial error
budget. Then (14) gives final error at most $\varepsilon$, with

\[
 \log(\tau^{-1})
 \le\log(\varepsilon^{-1})+C s\log(1+A_*)+C\log(s+2),           \tag{16}
\]

which is polynomial in (1). Store all $s$ coefficients on this counted
grid, the covariance and Cholesky matrices, one scalar-node value array,
and the quadrature/difference counters. Their dimensions and precision
are polynomial in (1); the activation evaluator has the stated fixed
space exponent. This proves the theorem.

Had (14) instead used $\sqrt{e_j}$ at every covariance stage, tolerances
could require $\log(\tau^{-1})$ of order $2^s$. The use of (9) prevents
that loss. The ridge in (15) also has polynomial bit length, despite
allowing exactly singular covariances in the original program.

## 5. Shared-parameter sensitivity and a uniform empirical bound

The numerical theorem exposes the following finite parameter counts and
global bounds. Here $s\le R^b$ counts shared coefficients, and $r\le R$
is the Gaussian dimension. The response row below concerns the integrand
before any post-expectation coefficient cap.

| Quantity | Count or magnitude bound |
| --- | --- |
| Shared coefficient coordinates | $s\le R^b$ |
| Shared coefficient range | $|c_j|\le C_B=4B^2+2$ |
| Additional Gaussian factor coordinates | $r^2\le R^2$ |
| Factor entry range when covariance norm is at most $V$ | $|C_{ij}|\le\sqrt V$ |
| Capped field integrand | $3B/2$ |
| Covariance product integrand | $9B^2/4$ |
| Raw response integrand | $E$ from (7) |
| First parameter and spatial derivatives of any listed integrand | $E$, after enlarging it for stated mean maps |

The last row applies to coefficient parameters and the Gaussian argument,
before composing with the Gaussian factor. The logarithm of $E$ is
polynomial in the counted quantities. For bounded arithmetic mean maps,
their supplied derivative bounds are absorbed into $E$.

Suppose, as a separate probabilistic hypothesis, that
$Z_1,\ldots,Z_n$ are independent standard Gaussian vectors in
$\mathbb R^r$. Let

\[
 H_\theta(z)=g(\mu(c)+Cz;c),\qquad \theta=(c,C),\qquad
 p=s+r^2,                                                     \tag{17}
\]

where the parameter domain is a box with coordinate magnitude at most
$D\ge1$, all functions in that box satisfy $|H_\theta|\le M$, and
the coefficient/spatial first derivative bounds are at most $E$. Enlarge
$D$ to cover the factor range and $C_B$. Means may be coordinates of $c$;
the stated mean-map derivatives are included in $E$ as above. This is a
family defined for every matrix $C$ in the box, not merely those chosen
by a possibly ill-conditioned covariance factorization routine. Thus no
Lipschitz dependence of $Q^{1/2}$ on $Q$ is required.

For $0<\delta<1$, put

\[
 T_n=\max\{1,\sqrt{2\log(4nr/\delta)}\},\qquad
 L_*=2Ep(1+T_n),\qquad \alpha=(nL_*)^{-1}.
\]

On the event $\max_i\|Z_i\|_\infty\le T_n$, whose probability
is at least $1-\delta/2$, the empirical mean is $L_*$-Lipschitz
in the parameter maximum norm: a factor-coordinate derivative is
$\partial_{x_a}g\,z_b$, while an ordinary coefficient derivative
is bounded by the coefficient and mean-map bounds. The population mean
has the same Lipschitz bound since $\mathbb E|Z_b|\le1$.

A coordinate grid of mesh at most $\alpha$ has at most
$(3+2DnL_*)^p$ elements and covers the box to maximum-norm error
$\alpha$. For a fixed grid point, boundedness in $[-M,M]$ gives

\[
 \Pr\!\left(\left|\frac1n\sum_iH_\theta(Z_i)
           -\mathbb EH_\theta(Z)\right|>t\right)
 \le2\exp\{-nt^2/(2M^2)\}.
\]

One direct proof is to differentiate the centered log moment-generating
function twice. Its second derivative is a tilted variance, at most
$M^2$ for a variable in an interval of length $2M$. Integrating twice
and applying the exponential Markov inequality gives the displayed bound.
A union bound on the grid, followed by the two Lipschitz interpolation
errors, proves that with probability at least $1-\delta$,

\[
 \sup_\theta\left|\frac1n\sum_iH_\theta(Z_i)
                    -\mathbb EH_\theta(Z)\right|
 \le M\sqrt{\frac{2\{p\log(3+2DnL_*)+\log(4/\delta)\}}{n}}
       +\frac2n.                                               \tag{18}
\]

On this event, $\theta$ may be selected using the entire sample. This
uses uniformity over deterministic parameters; it does not assert that
the rows remain independent conditional on the selected coefficients.
All shared factor entries are included in the parameter count, so singular
covariances do not conceal extra information or conditioning in (18).

For capped fields, take $M=3B/2$; for their covariance products, take
$M=9B^2/4$. If $p,\log E,\log D$ are absolute powers of $\log n$
and $B$ is polylogarithmic, (18) has a root-$n$ error times an absolute
polylogarithmic factor. If $B=\exp(C\sqrt{\log n})$, it instead has
the corresponding subpolynomial envelope, squared for covariance products.
Whether that envelope meets a particular decoder's stipulated constant is
a separate comparison, not an automatic conclusion of (18).

For an uncapped response integrand, only $M=E$ has been proved.
Capping the coefficient after its expectation does not reduce this
integrand range and does not give the favorable field prefactor in (18).
One may define a further surrogate by capping the response *integrand*,
$g_{\rm cap}=\sigma_B(\partial^\beta F)$, before averaging. It then
has $M=3B/2$. Its first two spatial derivatives and first coefficient
derivatives are bounded by a quantity with logarithm polynomial in
$\log E$, $q$ and $\log B$: the second spatial derivative consists
of $\sigma_B''(g)\partial_i g\partial_j g+
\sigma_B'(g)\partial_{ij}g$. Thus the same weak-covariance and numerical
proof applies to this further surrogate. It is another semantic change,
whose fidelity requires its own range or tail certificate.

No representation of trained dense neuron rows as (17) with independent
innovations is established here. The empirical corollary is conditional on
that exact representation, the declared coefficient box, and the chosen
integrand caps; numerical evaluability alone implies none of them.

## 6. Relation to the proposed temporal-jet program

The uncapped program in `POPULATION_DECODER.md` has not been proved to
satisfy the global envelopes used here. Bounded-strip activation derivatives
alone do not suffice for a general arithmetic DAG: repeated squaring sends
a Gaussian input to $G^{2^R}$. Its moment growth has an exponentially large
logarithm in $R$. This diagnoses an insufficient envelope argument, not a
memory lower bound for every specialized integration algorithm.

For temporal jets, a similar conservative growth certificate arises from
the exact product formula. If all base fields at one patch have polynomial
Gaussian growth degree at most $D_h$, a product of up to $K+1$ such jet
fields can have degree at most $(K+1)D_h$. Reusing those fields at the next
patch therefore permits the bound $D_H\le(K+1)^H D_0$. This bound may be
very loose for the actual evolution, but it is not a polynomial-space
certificate. The smooth caps eliminate that particular numerical issue in
the newly specified surrogate.

The precise derivative-order requirement of the capped evaluator is modest:
if the scalar instructions use activation derivatives through order $J$
and responses through order $q$, weak covariance propagation needs activation
derivatives through order $J+q+2$. The proof uses one additional order for
finite-difference evaluation and matching smoothness. Cauchy's bound (4)
has logarithm $O((J+q)\log(J+q+2)+(J+q)\log(2+a^{-1})+\log S)$.
There is no doubling of derivative order across $s$ covariance stages.
Thus $J,q$ polynomial in the transcript size are acceptable numerically.

### What an identity-on-range certificate would establish

For a fixed finite deterministic arithmetic computation, if every uncapped
scalar node and every response coefficient lies in $[-B,B]$, inserting
(2) at those locations preserves its output exactly. Induction through the
chronology proves this statement. Products before summation and response
coefficients must be included, not only the final fields.

A useful conditional cap-size calculation comes from analytic temporal jets.
Suppose a source curve has modulus at most $M$ on a time disk of radius $r$.
For its factorial-normalized coefficients $U[j]=\partial_t^jU/j!$,
Cauchy's estimate gives $|r^jU[j]|\le M$. A degree-$K$ activation-jet
calculation multiplies at most $K$ such factors. The number of positive
compositions of an index is at most $2^K$, and the raw activation
derivatives contribute at most the factorial/strip factors in (4).
Consequently every intermediate in a straightforward jet convolution has
logarithmic magnitude bounded by

\[
 C K\bigl[\log(M+2)+\log(K+2)+\log(2+r^{-1})
                    +\log(2+a^{-1})+\log(S+2)\bigr],             \tag{19}
\]

after including the finite affine-coefficient bounds. Thus a certified
$M\le C\sqrt n$ or any polynomial-in-$n$ bound can lead to a cap
$B=\exp(\operatorname{poly}(R,\log n))$, which is numerically affordable.
This statement is conditional on the displayed source range and on bounded
affine/response coefficients. A small history-Gram eigenvalue can make
individual inverse-based coefficients large even when the represented
field is small; equation (19) does not certify those coefficients.

Finally, identity on finitely many dense neuron values does not prove
identity of Gaussian expectations. A Gaussian integral sees values outside
any finite cap, and changing an earlier expectation changes later coefficients.
One still needs a tail/fidelity estimate for the capped population program,
or a width-identification theorem directly for it. A certified finite dense
computation can agree with its capped counterpart on a good event without
providing either population assertion. No such fidelity, autonomous
continuation or dense-width theorem is claimed in this note.

## 7. Status and provenance

Established here: an explicit smooth cap; a derivative majorant with
polynomial logarithmic size; streamed derivative evaluation; weak singular
covariance stability; a ridge-Cholesky precision bound; finite deterministic
tensor quadrature; and linear causal propagation yielding polynomial total
space for the specified capped finite program. The proof counts coefficients,
Gaussian coordinates, matrix factors, counters and precision. It uses neither
the original dense random initialization nor uncounted population functions.
The shared-parameter uniform empirical bound (18) is also proved, separately
conditional on independent Gaussian innovations and the indicated output
range. Its parameter count includes an arbitrary bounded Gaussian factor.

Open for the original decoder: construction/identification of the correct
inverse-free population DAG, cap fidelity at the original label allowance,
growing-program width errors, and the original all-time/model-continuation
requirements. A finite valid DAG and a numerically evaluable DAG are distinct
claims; this result concerns the latter for the explicit capped construction.

Scientific inputs read in this pass: `POPULATION_DECODER.md` completely,
SHA-256 `9d7ac82eed17036686cef3d679022a8df4404e78212e87e5df83d0503733f54d`;
and only Sections 1 and 12 of `GROWING_PROGRAM_STABILITY.md`, whose full-file
hash at the read was
`a3ef83a059912c93c451d065d23d269f3607d2c64b15cd5b7e4bcc558e1c7215`.
Section 1 supplies the weak covariance identity, reproduced with its proof
above. Section 12's Ornstein–Uhlenbeck formula confirms the distinction
between covariance weak regularity and square-root coupling, but is not
needed as an external theorem here. Its earlier numbered dependencies were
not fetched. No other new study/source or other route findings were read.
Previously read own notes, the maintained notation contract and required
skills remain in context; the canonical-notation skill's access failure and
explicit fallback are recorded in those notes.

After the initial derivative/growth analysis was reported, the supervisor
suggested explicitly smooth-capping scalar nodes and supplied the conditional
analytic-range idea used in Section 6. The supervisor subsequently proposed
a uniform empirical bound over shared coefficients; Section 5 develops it
with the Gaussian factor counted and distinguishes response-integrand caps
from post-expectation caps. The actual cap, majorant, quadrature and
precision proofs were developed here. This is therefore a supervised
continuation, not an isolated proof attempt. No experiments were run.
The author checked the algebra and workspace estimates; no independent
review has yet been performed. Only this assigned file was created, with no
Git index mutation. HEAD before writing was
`3834145d910202a84824d943fe7d7f65714d96f2`, and the shared index was empty.
