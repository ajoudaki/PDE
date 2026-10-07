# Constructive route: serial Gaussian integration and short time programs

Independent route, frozen 2026-10-05 and subsequently corrected after an
internal cross-check of its norm and tolerance assumptions. The independent
draft was completed without reading the other routes. Its scientific inputs
were the assignment, this study's
README, the maintained notation contract, and selected passages of Chapter 8
concerning finite Gaussian programs and storage. No experiment was run and no
external theorem is required for the proved lemmas below. The custom notation
skill was inaccessible at its configured path; the explicit user instructions
and maintained notation contract were applied.

## Result and scope

I do not obtain an unconditional compressor for the stated dense network.
I obtain a rigorous storage lemma showing that a high-dimensional Gaussian
expectation does **not** by itself force a dimension-dependent power of
`log(1/epsilon)` in retained storage. Tensor quadrature nodes can be generated,
used, and discarded serially. The arithmetic cost can be enormous while the
space cost is polynomial in the Gaussian source dimension and accuracy bits.

This suggests a distinct constructive mechanism: retain a short chronological
Gaussian computation for the nonlinear training flow, and recompute its
integrals with serial quadrature. The decisive missing bridge is a quantitative
short-program approximation for the actual deep feature-learning flow, with
uniform whole-sphere and all-time control. Analytic activation alone is not a
proof of that bridge. In particular, I do not substitute a frozen kernel or
assume that a finite-order Gaussian calculation establishes a growing-order
width theorem.

The storage statement is relevant only if unrestricted arithmetic work is
allowed. It does not promise an efficient numerical method. Its workspace,
precision, fixed data, and decoder instructions are counted.

## Exact finite dynamics and the temporal stopping mechanism

Let `L` count hidden layers, `m` samples, `d` input coordinates, and `n` hidden
width. For `x` on the radius-`sqrt(d)` sphere define

\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi(z^{(\ell)}(x)),\qquad
 f_n(x)=\frac{(W^{(L+1)})^Th^{(L)}(x)}n.
\]

The first matrix has iid `N(0,1)` entries, each subsequent hidden matrix has iid
`N(0,1/n)` entries, and `W^(L+1)(0)=0`. Different initialized blocks are
independent. With `r_a=f_n(x_a)-y_a`, the loss is
`m^(-1) sum_a r_a^2`. Let `D_n` be the diagonal mobility matrix with block
mobilities `(n,1,...,1,n)`. The complete parameter vector `theta` follows
`theta'=-D_n grad_theta L_n`.

Define the backward vectors by

\[
 \delta_a^{(L)}=W^{(L+1)}\odot\phi'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
                    (W^{(\ell+1)})^T\delta_a^{(\ell+1)}.
\]

Differentiation of the loss gives the exact equations

\[
 \begin{split}
 (W^{(1)})'&=-\frac2{m\sqrt d}\sum_a r_a\delta_a^{(1)}x_a^T,\\
 (W^{(\ell)})'&=-\frac2{mn}\sum_a
             r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T,
             \quad 2\le\ell\le L,\\
 (W^{(L+1)})'&=-\frac2m\sum_a r_ah_a^{(L)}.
 \end{split}
\]

These equations preserve correlated data and evolving hidden features. For
example, at zero readout the hidden velocities vanish, but, writing
`v=(2/m) sum_b y_b h_b^(L)(0)`, the top hidden acceleration is

\[
 (W^{(L)})''(0)=\frac2{mn}\sum_a y_a
    [v\odot\phi'(z_a^{(L)}(0))]
    (h_a^{(L-1)}(0))^T.
\]

There is no identity setting this acceleration to zero. Discarding these and
later hidden updates would be a change of the target, even though the first
prediction derivative only uses the initialized top-feature Gram.

For the complete parameter vector define the mobility kernel

\[
 K_n(t;x,x')=
  \nabla_\theta f_n(t,x)^TD_n\nabla_\theta f_n(t,x').
\]

Let `K_n^tr(t)` be its `m by m` training matrix. The chain rule yields

\[
 r'(t)=-\frac2mK_n^{\mathrm{tr}}(t)r(t),\qquad
 \partial_tf_n(t,x)=-\frac2m\sum_aK_n(t;x,x_a)r_a(t).
\]

**Conditional all-time tail lemma.** Suppose throughout the exact trajectory

\[
 K_n^{\mathrm{tr}}(t)\succeq\lambda I_m,\qquad
 \sup_{t\ge0,x}\left(\sum_a|K_n(t;x,x_a)|^2\right)^{1/2}\le B
\]

for positive `lambda,B`. Then

\[
 \|r(t)\|_2\le\|y\|_2e^{-2\lambda t/m},\qquad
 \sup_x\sup_{t\ge T}|f_n(t,x)-f_n(T,x)|
 \le\frac{B\|y\|_2}{\lambda}e^{-2\lambda T/m}.
\]

Indeed, `(||r||_2^2)'=-(4/m)r^TK_n^tr r` gives the first estimate. The
Cauchy--Schwarz inequality in the prediction equation bounds its speed by
`(2B/m)||r||_2`; integration from `T` to infinity gives the second estimate.
When `||y||_2>0`, an error-`epsilon` approximation through

\[
 T\ge\frac m{2\lambda}
       \max\left\{0,\log\frac{B\|y\|_2}{\lambda\epsilon}\right\}
\]

can be stopped at its own computed terminal state, at an additional error of
at most `epsilon`. For `y=0`, zero initial readout is stationary and one may
take `T=0`. This is causal stopping, not future-trajectory playback.
The initial positive Gram gap alone does not prove the two displayed uniform
hypotheses. Their persistence needs the small-label stability argument.

## A finite-space Gaussian integration lemma

Fix `0<epsilon<1`. Let `G` be a standard Gaussian vector in `R^s`, with
`s>=1`. Let `g_x:R^s -> R`
be an integrand depending on a query `x` in a fixed compact set `X`. Assume:

1. `sup_x E|g_x(G)|^2 <= M^2` for a supplied finite `M`.
2. For every integer `R>=1`, the function
   `q_x(z)=g_x(z)(2 pi)^(-s/2) exp(-||z||_2^2/2)` is uniformly bounded by
   `B_R` and uniformly Lipschitz in `z` with constant `K_R` on `[-R,R]^s`.
3. A finite evaluator computes `q_x(z)` to requested absolute accuracy using
   `Q` bits of working memory. Its fixed description, coefficients, input
   representation, and elementary-function workspaces are included in `Q`.
   The evaluation guarantee is uniform over the stated query set.

Then `E g_x(G)` can be approximated uniformly over `x` to absolute error
`epsilon`, using `Q` plus

\[
 O\left(s\log(N+1)+s\log(R+1)+
          \log\frac{1+(2R)^s(B_R+1)}\epsilon\right)
\]

bits, apart from the fixed descriptions of the supplied bounds. In every
total-space corollary those bounds must be computable upper bounds, and
their descriptions and evaluation workspace must be included in `Q`;
`Q` is evaluated at the actual required integrand accuracy
`epsilon/[4(2R)^s]`, including the error and space cost of representing the
query. Bounds on `log M`, `log B_R`, and `log K_R` alone do not bound the
description length of algorithms supplying them. One may take

\[
 \begin{split}
 R&=\left\lceil\max\left\{1,
       2\sqrt{\max\{0,\log(4M\sqrt{2s}/\epsilon)\}}\right\}\right\rceil,\\
 N&=\left\lceil\max\left\{1,
       \frac{2(2R)^{s+1}K_R\sqrt s}{\epsilon}\right\}\right\rceil.
 \end{split}
\]

If `M=0`, return zero and omit the logarithmic formula for `R`.

**Proof.** For a scalar standard Gaussian, the exponential-moment bound
`P(G_i>=R)<=exp(-R^2/2)` follows from
`E exp(R G_i)=exp(R^2/2)` and Markov's inequality. Apply it also to `-G_i`
and take the union bound over coordinates. Cauchy--Schwarz then gives

\[
 \left|\mathbb E[g_x(G)1_{\{G\notin[-R,R]^s\}}]\right|
 \le M\sqrt{2s}\,e^{-R^2/4}\le\epsilon/4.
\]

Partition `[-R,R]^s` into `N^s` cubes of side `2R/N` and use their midpoints.
Every point of a cube is at distance at most `R sqrt(s)/N` from its midpoint.
Thus the integral error is at most

\[
 (2R)^sK_R\frac{R\sqrt s}{N}
 =\frac{(2R)^{s+1}K_R\sqrt s}{2N}\le\epsilon/4.
\]

At each midpoint evaluate `q_x` to absolute error at most
`epsilon/[4(2R)^s]`. After multiplication by the cell volume and summation,
these errors total at most `epsilon/4`. Round each weighted summand and
accumulator update with combined error at most `epsilon/(4N^s)`, allocating
the fixed-point spacing accordingly. The cumulative rounding error is at
most `epsilon/4`. A signed accumulator needs magnitude at most
`(2R)^s(B_R+1)` plus a fixed margin, and its fractional bits are bounded by
`O(log(1/epsilon)+s log N)`. The midpoint coordinates are rationals with
numerator and denominator lengths `O(log(R+1)+log(N+1))`.

Store just `s` loop indices, the current midpoint, one accumulator, and the
integrand evaluator. Incrementing the indices generates the whole tensor
grid without retaining its nodes or function values. The displayed bit
bound follows. The four errors sum to at most `epsilon`. All estimates are
uniform over `x`, so a finite test panel is not used to infer a supremum.

The work is at least `N^s` evaluations. Large work is admitted explicitly;
the lemma only controls storage. For example, when

\[
 s,\ Q,\ \log(1+M),\ \log(1+B_R),\ \log(1+K_R)
 \le C(d,m,L)(\log(1/\epsilon))^c
\]

with a fixed exponent `c` independent of both `d` and `m`, the total space is
bounded by a power of `log(1/epsilon)` whose exponent is independent of both
`d` and `m`. The
constant `C(d,m,L)` may still be very large. Tensor node count must not be
mistaken for necessary retained storage.

For an unbounded activation, condition 1 is a genuine moment requirement;
bounded first derivatives give at most linear growth of each activation,
but do not automatically bound every entire growing computation uniformly.
For finite-precision computation, a computable activation evaluator must
also be supplied. Merely postulating an arbitrary analytic function does
not supply its finite algorithmic description.

## How a short Gaussian program would use the lemma

A chronological Gaussian program has a finite list of Gaussian sources,
their covariance or square-root factors, scalar expectation coefficients,
and a finite evaluation graph using them. Covariance and source-response
coefficients are generated by preceding parts of the computation. The two
orientations of an initialized hidden matrix must belong to the same program;
an independent backward Gaussian replacement is inadmissible.

Suppose such a program has `J` named sources and `P(J,m,L)` scalar graph nodes
and coefficients. Retaining its covariance factors costs `O(J^2)` scalars,
and direct evaluation of its graph costs at most its graph size in scalar
workspace. Every finite Gaussian expectation in the program can use the
serial evaluator above. Its temporary source vector and quadrature indices
are discarded after each call. To treat singular Gaussian covariance, a
specified covariance square root may be used directly in `g_x`; the lemma
does not require a covariance inverse. Quantitatively computing and updating
that root, and controlling the effect of coefficient errors on later calls,
remain part of the program's finite-precision contract.

This is an implementation statement for a supplied finite program, not a
theorem identifying any arbitrary program with trained dense networks. It
does not license an uncounted Gaussian-integral oracle, population table,
function-valued coordinate, or dense initialization oracle. The integrand's
graph, fixed coefficients, current program transcript, activation evaluator,
and all precision costs count.

If the program is extended causally as the numerical training method runs,
its present transcript is state and can be serialized for restart. Computing
an entire future trajectory first and then replaying it is excluded. A
numerical algorithm with a clock and step events is an autonomous hybrid
representation; it is not automatically a smooth finite-dimensional ODE.
An admissible-class requirement of the latter would need an additional
construction rather than a change of terminology.

## Quantitative temporal regularity: the missing constructive bridge

Here is a sufficient quantitative route. It deliberately exposes assumptions
that have **not** been verified for the requested Gaussian feature-learning
model.

The ordinary finite parameter vector `theta` used above cannot satisfy the
proposed width-independent derivative bound; the exact obstruction is
recorded below. Introduce instead a **hypothetical population proof state**
`S(t)`. For probability spaces `Omega_l`, put `H_l=L^2(Omega_l)` and define

\[
 \mathcal B=L^2(\Omega_1;\mathbb R^d)
  \times\prod_{\ell=2}^{L}\operatorname{HS}(H_{\ell-1},H_\ell)
  \times L^2(\Omega_L),
 \qquad
 S=(U^{(1)},K^{(2)},\ldots,K^{(L)},c),
\]

with the explicit norm

\[
 \|S\|_{\mathcal B}
 =\|U^{(1)}\|_{L^2(\Omega_1;\mathbb R^d)}
  +\sum_{\ell=2}^{L}\|K^{(\ell)}\|_{\mathrm{HS}}
  +\|c\|_{L^2(\Omega_L)}.
\]

Here `U^(1)` denotes the first population row, `K^(ell)` the trained hidden
operator increment from initialization, and `c` the population readout.
The initialized hidden actions themselves are not assumed Hilbert--Schmidt.
Their hypothetical availability as operators in a proof is not permission
to retain them as runtime oracles: a finite compiler must replace every
needed action using counted data and workspace. This infinite-dimensional
proof state is not itself an admissible finite compressed representation.
Neither its existence and identification for the requested model nor the
regularity estimates below are established here.

Suppose `S` has an autonomous vector field on a common reached-state tube in
`B`, with exact flows from every required numerical starting state, and
suppose

\[
 \|S^{(k)}(t)\|_{\mathcal B}\le M A^k(k!)^\sigma,
 \qquad k\ge1,
\]

where the Gevrey order `sigma>=1` depends at most on the fixed hidden depth `L`,
not on `d,m,n`, and nearby numerical states remain in that tube. Suppose also
that the exact flow is Lipschitz in this same `B` norm there, with
amplification at most `exp(Ct)`.
Constants `M,A,C` may depend on the fixed data, activation, dimension, depth,
Gram gap, and small-label bound, but not on width or requested accuracy.

The order-`p` Taylor method has one-step error bounded by the integral Taylor
remainder:

\[
 \frac{h^{p+1}}{(p+1)!}
     \sup\|S^{(p+1)}\|_{\mathcal B}
 \le M(Ah)^{p+1}((p+1)!)^{\sigma-1}.
\]

Choose `h = q/[A(p+1)^(sigma-1)]` for a fixed `0<q<1`, shortening only the
terminal step if necessary. Since
`(p+1)! <= (p+1)^(p+1)`, the remainder is at most `M q^(p+1)`.
Comparing each numerical step with the exact flow from that numerical
state yields, after at most `ceil(T/h)` steps,

\[
 \|e(T)\|_{\mathcal B}\le
 M\lceil T/h\rceil e^{CT}q^{p+1},
\]

with the same bound at intermediate nodes; a local Taylor polynomial gives
the corresponding between-node estimate. This comparison uses stability of
the exact flow and the stated derivative bound at numerical starts. It
does not assume that the high-order Taylor update has a separate
width-uniform stability theorem.

When `T=O(log(1/epsilon))`, taking `p=O(log(1/epsilon))` with a sufficiently
large constant makes this error at most `epsilon`. The number of steps is
`O((log(1/epsilon))^sigma)`. If automatic differentiation through the neural
equations can compile each order-`p` step using `O(C(d,m,L) p^b)` Gaussian
sources and a polynomial-size graph, with both polynomial degrees
independent of both `d` and `m`, the complete source count is

\[
 J=O(C(d,m,L)(\log(1/\epsilon))^{\sigma+b}).
\]

Further require polynomial bounds on all program graph sizes, logarithms of
integrand bounds, conditioning costs, activation-evaluation space, and
precision requirements, **with every polynomial degree independent of both
d and m**. This includes every exponent appearing in logarithmic storage
bounds; allowing it to depend on `m` would permit hidden dimension dependence
when `m=m(d)`.
Coefficients in those bounds may depend on the fixed dimension, data, and
depth. Under all these hypotheses, the serial integration lemma would give total space
`C'(d,m,L) (log(1/epsilon))^a`, with `a` independent of both `d` and `m`.

For a **prescribed permitted tolerance** `epsilon_n` satisfying
`log(1/epsilon_n)=Theta(log n)`, substituting that logarithm gives the
requested form of scalar/bit complexity. This substitution is not a dense
approximation theorem. One must separately prove the finite-width comparison
and every numerical error at that specified tolerance. For example, if the
contract allows `epsilon_n=C n^(-1/2)(log n)^b` for a fixed `b`, a generic
`n^(-1/2+o(1))` estimate does not suffice: its loss could be
`exp(sqrt(log n))`, which exceeds every fixed logarithmic power. If the
reference is actual independent-run discrepancy, a probabilistic comparison
to that discrepancy is needed instead of selecting a larger envelope.
The data alone cost `md+m` real scalar slots. If each coordinate and label
uses `b_data` bits, their finite-bit storage is `(md+m)b_data`, not merely
`md+m`. This precision factor and its effect on the prediction error must be
included; `b_data` must obey the same precision contract with exponents
independent of `d,m`. Fixed dimension-dependent coefficients may be included
in `C'`, but an accuracy-dependent bit count may not be hidden in that constant.

This implication still requires all of the following missing statements:

- Identification of the hypothetical population state with the actual
  trained Gaussian system, followed by the quantitative Gevrey bound in
  the explicit `B` norm and a stable common tube, with Gevrey order
  independent of both `d` and `m`.
- A polynomial-size chronological Gaussian compiler for these high-order
  steps, including reused forward and backward actions, together with
  controlled Gaussian moments and finite-precision error propagation. Every
  polynomial degree in this compiler, graph, integrand-bound, conditioning,
  and precision contract must be independent of both `d` and `m`.
- Whole-sphere output estimates from the chosen state norm, uniformly at
  every stage and at the fitted endpoint.
- A quantitative comparison to the actual initialized finite network at
  the explicitly prescribed tolerance `epsilon_n`, valid when the program
  order and time horizon grow as prescribed. A fixed-program width limit
  does not provide this statement; a larger subpolynomial error envelope
  cannot silently replace the permitted tolerance.
- If the target is the actual independent-run discrepancy rather than a
  proved upper envelope, a comparison between that discrepancy and the
  deterministic-limit approximation error.

These are major proof obligations, not small implementation details. The
first two may fail; this report does not claim that the proposed short
program exists.

## Failed arguments and adversarial checks

**Ordinary finite-parameter Gevrey bounds fail already at the first
derivative.** The original independent draft incorrectly wrote the
width-independent regularity hypothesis using the complete finite vector
`theta`. Let `H` be the `n by m` matrix with columns `h_a^(L)(0)`, and let
`y` be the label vector. Zero initial readout makes every hidden contribution
to the mobility kernel vanish initially, so

\[
 K_n^{\mathrm{tr}}(0)=H^TH/n,\qquad
 (W^{(L+1)})'(0)=2Hy/m,
\]

and consequently

\[
 \|(W^{(L+1)})'(0)\|_2^2
 =\frac{4n}{m^2}y^TK_n^{\mathrm{tr}}(0)y
 \ge\frac{4n\lambda_0}{m^2}\|y\|_2^2
\]

whenever the initialized Gram gap is at least `lambda_0>0`. For fixed
nonzero labels this diverges linearly in squared norm. Hence the ordinary
Euclidean norm of `theta'(0)` is at least of order `sqrt(n)`, contradicting
width-independent `M,A` already for derivative order one. The corrected
conditional subsection uses a distinctly typed population norm, whose
finite analog would scale the first matrix and readout by their RMS factors
and use Frobenius norms only for trained hidden increments. No Gevrey bound
in that norm is asserted or inferred from this change of norm. For zero
labels the trajectory is stationary, which does not rescue the proposed
ordinary-norm bound in the stipulated nontrivial learning regime.

**Strip analyticity does not by itself prove time analyticity in a population
norm.** Even the map `t -> tanh(t G)` with one Gaussian `G` illustrates the
problem with a naive complex-neighborhood argument: for every nonzero
imaginary `t`, its complex poles occur on the real `G` axis. The real-time
map can have derivatives of all orders, but a width-independent bounded
holomorphic tube in a Gaussian `L^p` space cannot be inferred by applying
pointwise strip analyticity without a tail argument. This example does not
disprove a finite-order Gevrey estimate, nor does it assert that a particular
network trajectory has the same singularities.

**Low-rank increments alone do not remove width.** A time quadrature writes
each hidden increment as a sum of rank-one terms from the exact equations.
Keeping `r` such terms still stores `O(nr)` vector entries per layer, as well
as access to the initialized matrix unless its actions are separately
compiled. This is not a polylogarithmic retained representation.

**One-dimensional time does not make a query decoder scalar-valued.** Taylor
coefficients of `t -> f(t,.)` are functions on the sphere. Counting one
coefficient as one stored scalar hides the spatial decoder. The Gaussian
program proposal explicitly counts its graph and integration workspace.

**Causal history is not automatically cheap.** A first-order time method may
need a number of calls proportional to a power of `1/epsilon`, and storing
its covariance/response history then violates the target. The high-order
regularity bound is needed to make the history short.

**Expectation is not the realized initialization.** The proposed compiler
would naturally approximate a deterministic Gaussian population quantity.
It may discard the initialization only after a valid probabilistic
comparison proves the permitted tolerance. Matching an upper envelope is
not automatically matching the actual discrepancy of two runs.

**A spatial entropy bound does not refute this computational route.** The
output is not represented as an unconstrained table of all analytic spatial
coefficients. Conversely, the existence of a low-memory integration routine
does not prove that a short graph generates the neural trajectory.

**Fixed dimension is separate from uniform dimension control.** The
conditional exponent would be independent of both `d` and `m`, but all constants can
depend on the data Gram gap, label scale, activation, `d,m,L`, and evaluator
conditioning. No joint `n,d` asymptotic or useful numerical performance
would follow without bounds on those constants.

## Route status

| Claim | Status | Smallest missing bridge |
|---|---|---|
| Exact finite GF and zero-readout hidden acceleration | Proved algebraically | None |
| Exponential prediction tail under a persistent kernel gap and uniform cross-kernel bound | Proved conditional lemma | Verify its uniform hypotheses in the stipulated regime |
| Uniform Gaussian quadrature with polynomial retained space under explicit effective bounds | Proved | Supply bounds and finite evaluator for the actual program |
| Sublinear dimension exponent via high-order Gaussian programs | Conditional construction only | Dimension-independent Gevrey order and quantitative compiler control |
| Matching actual all-time dense self-variability | Open | Quantitative finite-width and scale comparisons |

The highest-leverage next theoretical check for this route is the temporal
regularity estimate on a reached small-label tube. If its derivative growth
has a fixed finite Gevrey order with adequately controlled Gaussian programs,
serial integration removes spatial tensor storage as an automatic obstacle.
If the derivative/program bounds grow too quickly, this witness fails; no
general impossibility theorem follows.
