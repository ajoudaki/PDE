# A direct compact initializer by certified finite-width Gaussian integration

Author development, 2026-10-06. This is a constructive finite-width reduction,
not a population-limit argument. Its neural corollary inherits the paired
compact and independent-dense estimates explicitly identified below. Those
inputs are internally checked research results, not promoted book theorems.
The resulting rate is the inherited dense-variability upper bound, not a
new strict constant-times-root-width bound. Initialization is effective but
may be extraordinarily expensive.

## 1. Setup and statement

Let the fixed data be `(x_a,y_a)`, `1 <= a <= m`, with
`||x_a|| = sqrt(d)`, and set `v_a=x_a/sqrt(d)`. All displayed neural
equations below use unit queries `v`. The canonical reference is

\[
h_n(v)=\tanh(A_nv),\quad g_n(v)=\tanh(W_nh_n(v)),\quad
f_n(v)=w_n^Tg_n(v)/n.
\]

Initialize the entries of `A_n` and `sqrt(n) W_n` independently as standard
Gaussians, and `w_n=0`. Train the squared mean loss with block mobilities
`(n,1,n)`. The comparison norm is

\[
\|f-\widetilde f\|_*
=\sup_{t\in[0,\infty]}\sup_{\|v\|=1}|f(t,v)-\widetilde f(t,v)|,
\]

including the fitted endpoints when they exist. The algorithm's inputs are
the data, reference width `n`, compact width budget `1 <= q < n`, tolerance
`epsilon>0`, and `0<delta<1`. It does not receive a dense initialization.
For implementation, numerical inputs have computable-real presentations;
alternatively all computation is relative to the supplied data coordinates.
This is an arithmetic/real-coordinate storage model, not a bit-storage claim.

Here is the precise sufficient condition for termination. At this fixed
width, suppose the existing paired compact construction supplies a measurable
model of widths at most `q` such that, except with probability
`delta/100`, it has bounded convergent parameters, a uniformly positive
training-feature Gram, and paired error at most `e`. Suppose also that

\[
\Pr(\|f_n-\widetilde f_n\|_*>v)\le\delta/100,
\qquad e+v\le\varepsilon/16,
\tag{1}
\]

and that a fresh dense path has bounded convergent parameters, a uniform
positive feature-Gram gap, and residual tending to zero, except with
probability `delta/100`. The local symbols `e,v` in (1) denote the two
input error certificates only; they are not additional model parameters.

**Constructive transfer theorem.** Under these conditions, the search in
Section 4 terminates and returns rational initial hidden weights and
rational positive-definite metrics for an autonomous compact model with
widths at most `q`, zero raw readout, and initial deficit equal to `y`.
Its evolution is specified in Section 2. It satisfies

\[
\Pr\left[\|f_C-f_n\|_*\le\varepsilon\right]\ge1-\delta
\tag{2}
\]

against an independent fresh canonical dense initialization. The returned
compact model itself is deterministic. The probability is solely over the
fresh reference. The search never constructs or evaluates a realized
width-`n` network, and needs no population-response oracle. It does perform
symbolic finite-width Gaussian integration and can use very large temporary
memory and time. It is not claimed to be an efficient initializer.

Without the sufficient conditions, the search is a sound partial algorithm:
any accepted output still satisfies (2), but termination is not asserted.
Thus an unquantified inherited width threshold is not converted into a
computable a priori threshold.

## 2. The actual small model and its autonomous optimizer

Choose integers `q_1,q_2 <= q`. Store fixed positive-definite symmetric
matrices `H_1,H_2`, and moving `A,B,w,c` of shapes
`q_1 x d`, `q_2 x q_1`, `q_2`, `m`. Initialize `w=0,c=y`.
The forward pass and corrected readout are

\[
h(v)=\tanh(Av),\quad g(v)=\tanh(Bh(v)),\quad
F=[g(v_1)\ \cdots\ g(v_m)],\quad Q=F^TH_2F,
\]
\[
\widehat w=w+FQ^{-1}(y-c-F^TH_2w),\qquad
f_C(v)=\widehat w^TH_2g(v).
\tag{3}
\]

In particular `f_C(v_a)=y_a-c_a` exactly. Define, for each training sample,

\[
b_{2,a}=(1-g(v_a)^2)\odot\widehat w,\qquad
b_{1,a}=(1-h(v_a)^2)\odot H_1^{-1}B^TH_2b_{2,a}.
\]

Squares and products inside the gates are coordinatewise. Let

\[
K_{ab}=g(v_a)^TH_2g(v_b)
 +(b_{2,a}^TH_2b_{2,b})(h(v_a)^TH_1h(v_b))
 +(b_{1,a}^TH_1b_{1,b})(v_a^Tv_b).
\]

The runtime equations, in the original physical time, are

\[
\dot A=\frac2m\sum_a c_ab_{1,a}v_a^T,\quad
\dot B=\frac2m\sum_a c_ab_{2,a}h(v_a)^TH_1,
\]
\[
\dot w=\frac2m\sum_a c_ag(v_a),\qquad
\dot c=-\frac2mKc.
\tag{4}
\]

All hidden weights train. This is the existing corrected-readout optimizer,
not ordinary gradient flow in a non-diagonal metric, and not trajectory
playback. The search changes how its initial weights and metrics are
obtained. It does not change its runtime equations.

Only strict positive definiteness of the metrics and the initial training
Gram is imposed on search candidates. The stronger metric inequalities of
the old coordinate-selection proof are not imposed as exact identities on
rational candidates. The certificate below proves their actual fitting and
comparison directly. Rational perturbations therefore do not need to
preserve an exact source-isometry equality.

## 3. Three effective ingredients

### 3.1 Finite-time bounds without a dense realization

Write `Y=||y||/sqrt(m)` and truncate every standard Gaussian coordinate to
`[-B,B]`. There are `nd+n^2` such coordinates. The union bound gives

\[
\Pr(\text{outside the box})\le2(nd+n^2)e^{-B^2/2}.
\tag{5}
\]

Choose a computable rational `B` making (5) less than `delta/32`.
For the dense flow use the parameter norm

\[
\|(A,W,w)\|_{\rm par}^2
=\|A\|_F^2/n+\|W\|_F^2+\|w\|_2^2/n.
\]

The gradient-flow energy identity gives path length at most `Y sqrt(T)`
on `[0,T]`. Thus a valid bound for the parameter norm is
`P=B sqrt(d+n)+Y sqrt(T)`. The readout norm is at most `Y sqrt(T)`.
On this box and interval, valid sphere and time Lipschitz bounds are

\[
|\nabla_v f_n|\le Y\sqrt T\,P^2,\qquad
|\partial_t f_n|\le2Y(1+P+P^2)^2.
\tag{6}
\]

Indeed the three parameter-gradient blocks have norms at most
`1`, `P`, and `P^2`; the residual RMS stays at most `Y`. These estimates
are deliberately coarse. They need no probabilistic fitting theorem and
ensure global existence on every finite real interval. They also supply
a bounded parameter tube for certified ODE approximation.

For a rational compact candidate, validated integration on its open
Gram-positive domain either certifies existence through a specified finite
`T`, with a positive Gram lower bound and finite parameter bounds, or leaves
that computation unfinished. On a successful certificate its vector field,
predictions and their derivatives are uniformly computable on a compact
tube. This gives finite-time prediction moduli analogous to (6). An
explicit bounded tube with positive Gram margin can be searched by rational
boxes and step sizes: the vector field is analytic there, derivative bounds
follow from the displayed formulas, and strict Picard/Euler error
inequalities eventually certify any true compact trajectory with a positive
minimum gap on `[0,T]`. No assertion about a failed candidate is necessary.

### 3.2 Computable tails and openness

The complete local certificate is proved in
[COMPUTABLE_TAIL_CERTIFICATES.md](COMPUTABLE_TAIL_CERTIFICATES.md).
Its mechanism is the exact identity

\[
-\frac d{dt}\frac{\|c\|^2}{m}
=\|\dot A,\dot B,\dot w\|_{\rm par}^2,
\quad K\succeq Q,
\]

in the metric
`tr(A^T H_1 A)+||H_2^(1/2) B H_1^(-1/2)||_F^2+w^T H_2w`.
A positive Gram at time `T` persists if the energy-controlled remaining
parameter path is shorter than the distance needed to close that gap.
Explicit local derivative bounds also control the corrected readout in
(3). All inequalities are strict and computably checkable.

The resulting facts needed here are:

1. A finite-time certificate can prove global existence, convergence to a
   fitted endpoint, and `sup_{t>=T,v}|f(t,v)-f(T,v)| < eta`.
2. On every bounded trajectory with a uniformly positive feature Gram and
   residual tending to zero, such a certificate eventually succeeds for
   every `eta>0`.
3. At each such compact initialization, the map from initial hidden weights
   and positive-definite metrics to the entire prediction trajectory is
   continuous in `||.||_*`, with the raw readout held zero and `c(0)=y`.

For completeness, the last assertion is stronger than finite-time ODE
continuity. First choose `T` so that the reference tail is tiny and its
certificate has a strict margin. Nearby initializations remain close on
`[0,T]`, and the same strict local certificate controls their tails
uniformly. The triangle inequality proves all-time continuity, including
the endpoint. This is why rational initial weights suffice.

For the dense model there is a particularly convenient bounded continuous
tail gate. At time `T` let, locally in this paragraph,

\[
\lambda=\lambda_{\min}(F^TF/(nm)),\quad
\rho=\|f_n(v_a)-y_a\|_2/\sqrt m,\quad
u=\|w_n\|_2/\sqrt n,
\]
\[
L=\sqrt{1+(\|W_n\|_F+1)^2},\quad
R=\min\{1,\sqrt{\max(0,\lambda)}/(2L)\},\quad
\chi(s)=\min\{1,\max\{0,s\}\}.
\]

For a chosen tail tolerance `eta`, set

\[
G_T=\chi\big((1+T)[\sqrt{\lambda_+}R-2\rho]\big)
\chi\big((1+T)[\eta\sqrt{\lambda_+}
       -4\rho(1+(u+R)L)]\big),\quad \lambda_+=\max(0,\lambda).
\tag{7}
\]

This gate is continuous everywhere, including singular Grams. If `G_T>0`,
the dense tail certificate is valid with tail smaller than `eta`.
On every bounded uniformly gapped fitting path `G_T=1` for all sufficiently
large `T`. Replacing the mixer operator norm by its Frobenius upper bound
only makes the certificate more conservative. Every input to (7) is a
scalar contraction or the eigenvalue of the fixed-size `m x m` Gram.
No width-`n` eigendecomposition is needed.

### 3.3 Exact finite-width Gaussian integration, not a response oracle

[FINITE_WIDTH_EXPECTATION_COMPILER.md](FINITE_WIDTH_EXPECTATION_COMPILER.md)
proves the following constructive fact. A bounded continuous, effectively
computable score of finitely many dense predictions and terminal scalar
contractions on `[0,T]` has a computable integral over the Gaussian box in
(5), with certified arbitrarily small absolute error. The computation does
not instantiate a dense array.

Here is why the width dependence is not hidden. Replace real tanh and its
derivative on the certified finite tube by polynomials with certified
uniform error, and discretize the dense ODE with a certified error bound.
Every scalar observable becomes a finite polynomial tensor expression in
formal Gaussian coordinates. Expand each expression as indexed monomials.
For each neuron type, partition the abstract indices according to equality.
A partition with `k` distinct indices contributes the explicit scalar
falling factorial `(n)_k`. Independent Gaussian entries contribute products
of one-dimensional truncated Gaussian moments. Repeated use of `W` and
`W^T` uses the same coordinate keys; it is not replaced by independent
matrices. Nonforest contraction graphs are included.

The compiler naturally computes the conditional integral on the box.
Multiplying by
`(integral_{-B}^B exp(-s^2/2)/sqrt(2 pi) ds)^(nd+n^2)` gives the
unnormalized box integral used in the acceptance test. This scalar
probability is computable to certified precision; no additional neural
object is involved.

Approximate the continuous score on its bounded observable range by a
polynomial, also with a certified error. Summing all graph/partition terms
and the approximation error gives an interval for its exact integral.
Uniform approximation, rather than termwise convergence of an infinite
expected Taylor series, justifies this procedure. It uses the finite-`n`
law exactly at every requested precision, so there is no population-bias
remainder.

## 4. The explicit initialization algorithm

Enumerate rational `A,B,H_1,H_2` in all shapes `q_1,q_2 <= q`, rational
positive-definite metrics, positive integer horizons `T`, and numerical
precision levels. Keep `w=0,c=y`. Dovetail finite computations, so a
singular or uncertifiable candidate never prevents a later one from being
examined. Rational matrices can be enumerated by increasing bounds on
integer numerators and positive denominators. Strict positive definiteness
is checked by interval eigenvalue bounds or principal minors.

For a candidate/horizon pair:

1. Certify its trajectory through `T` and then its compact fitting tail
   with tolerance `epsilon/8`, using Section 3.2. Skip any unfinished
   verification while dovetailing the other jobs.
2. From (6) and the compact finite-time bounds, construct finite time and
   sphere grids, including times `0,T`, such that their joint prediction
   discrepancy misses the continuous supremum on `[0,T]` by at most
   `epsilon/8`. Rational sphere nets can be built by normalizing a fine
   rational grid away from zero; for `d=1` use the two points. All compact
   nodal values are computed by certified small-model integration.
3. Let `D` be the maximum absolute prediction discrepancy on this finite
   grid, considered as a random function of the formal dense Gaussian
   initialization. Form the bounded continuous score

   \[
   S=1-G_T\chi(2-4D/\varepsilon),
   \tag{8}
   \]

   where the dense tail gate uses `eta=epsilon/8`. Compute a certified
   upper bound for the integral of `S` over the Gaussian box, using the
   compiler. Refine precision until this bound plus (5) is strictly less
   than `delta`, or leave the job unfinished and continue dovetailing.
4. Once the strict inequality succeeds, output this candidate's rational
   initial weights and metrics. Discard the search history, all grids,
   formal contraction graphs, moment tables and certificates. Initialize
   a fresh copy of the accepted small model with `w=0,c=y` and run (4).

All operations are specified by elementary formulas, finite enumeration,
certified ODE approximation, and one-dimensional Gaussian integration.
The latter moments are ordinary definite integrals of polynomials times
the known Gaussian density, not dense-network responses. No intermediate
realized dense network is selected, generated or queried. Setup is allowed
to train candidate *small* networks for certification; the returned runtime
does not access those setup trajectories.

## 5. Proof of soundness and termination

### Soundness of every accepted output

Inside the Gaussian box, `S<1` implies both a positive dense tail gate and
`D<epsilon/2`. The compact tail is already certified. The finite grid
therefore bounds the discrepancy on `[0,T]` by `5 epsilon/8`. At later
times, including infinity, compare both paths to their values at `T`.
The grid approximation at `T` and the two tails give a bound smaller than

\[
\varepsilon/2+\varepsilon/8+2\varepsilon/8
=7\varepsilon/8<\varepsilon.
\]

Consequently failure of (2), or failure of the asserted fitted dense
endpoint on this event, implies `S=1` inside the box. Since `0<=S<=1`,
the total failure probability is bounded by the computed integral plus
the outside-box probability. The strict acceptance test proves (2).
There is no union bound over candidates: the selected candidate and its
certificate are deterministic functions of the law and the data, not of
the fresh reference. All interval bounds are deterministic valid bounds.

### Existence of a good rational candidate

Put `a=delta/100` in this paragraph. Let the good paired event have
probability at least `1-a`. For a dense initialization `z`, let `p(z)` be
the probability that an independent dense copy is more than `v` away
from its trajectory. By (1), `E p <= a`. Conditional averaging over the
good paired event gives some initialization `z_*` on that event with

\[
p(z_*)\le a/(1-a)<2a.
\]

This selects a witness only in the proof; the algorithm does not compute
`z_*` or its compressed model. Its compact trajectory has error at most
`e+v <= epsilon/16` against a fresh reference except with probability
`2a`. By the all-time continuity of Section 3.2, there is a rational
candidate of the same shapes and with positive-definite rational metrics,
zero raw readout and initial deficit `y`, within `epsilon/16` of that
compact witness in `||.||_*`. It is bounded, uniformly gapped and fits.
Thus this rational candidate is within `epsilon/8` of a fresh reference
except with probability `2a`.

### The finite certificate eventually accepts it

For this fixed rational candidate, its compact tail test succeeds for
all sufficiently large integer `T`. On the event of error at most
`epsilon/8`, every grid discrepancy is at most `epsilon/8`, regardless
of how fine the grids become. Hence the prediction factor in (8) is one.
For every bounded uniformly gapped fitting dense path, the gate `G_T`
tends to one and is eventually exactly one. Such paths fail with
probability at most `a`. Bounded convergence therefore gives

\[
\limsup_{T\to\infty}\mathbb E S\le3a.
\]

The expectation over the box is no larger than the full expectation.
For some finite integer horizon it is therefore less than `delta/10`.
Adding (5), which is less than `delta/32`, still leaves strict slack
below `delta`. Finite precision eventually certifies this strict
inequality. The dovetailed search eventually reaches that finite
candidate, horizon, integration and compiler computation, and terminates.

This completes the constructive transfer proof. Its probability and tail
arguments are finite-width arguments. They make no inference from
dense-copy agreement to convergence to a population trajectory.

## 6. Instantiation at the existing compact storage order

Use the full common label allowance and eventual width qualifications in
the authorized integrated result. No new label cap or target-dependent
smallness condition is imposed by the transfer. Orthogonality is not
needed by this reduction: any fixed sphere dataset with the required
positive initial-feature Gram gap is permitted by the inherited inputs.
For zero labels the identically zero predictor handles the question
directly.

The inherited compact theorem with source tolerance `1/n` supplies, with
failure budget `delta/100`, widths

\[
q=O\big(\log(en)^{3d/2+1}\big)
\]

and paired error `n^{-1+o(1)}`. The complete finite integer choice is
`q=9[B+4N(T_0,1/n)]` for `d>=2`, or
`q=9[B+8N_1(T_0,1/n)]` for `d=1`, with `B=2m+d+1`,
`T_0=32(m/gamma) log(en)` and the explicitly defined source-count
functions in the integrated result. These local references reproduce
the original budget, rather than adding any new logarithmic exponent.
For sufficiently large `n` it is less than `n`.
For a finite-precision implementation, use certified integer upper bounds
on these counts: approximate each finite scalar cutoff from above and
round its upper endpoint upward. This avoids having to decide whether a
computable real cutoff is exactly an integer. Equivalently use the
explicit simplex upper bound with a safely rounded integer ceiling.
The fixed enlargement preserves the displayed storage order. The same
upper-enclosure convention supplies a computable positive tolerance from
the error certificates below.

Take `epsilon` to be sixteen times the sum of its exact paired certificate
and the integrated independent-dense certificate, both evaluated at
failure probability `delta/100`. The direct search then yields

\[
\|f_C-f_n\|_*
\le C_{\mathrm{data},\delta}
\frac{\log(en)\exp(C_{\mathrm{data}}\sqrt{\log(en)})}{\sqrt n}
\quad\text{with probability at least }1-\delta,
\tag{9}
\]

for every sufficiently large individual width. All constants in (9) are
independent of `n` and time; their exact computable certificates are the
finite source/comparison recurrences in the integrated input. The
sufficient width remains unquantified. The displayed error is
`n^{-1/2+o(1)}`, **not** `C_data,delta/sqrt(n)`.

The integration/search theorem is fully quantitative at its supplied
`q,epsilon,delta`: every accepted model comes with (2). The asymptotic
instantiation only inherits, and does not improve, the available dense
concentration rate. If a strict root-width dense-copy estimate is proved
under the same assumptions, the same construction and retained count
immediately give the user's strict target, since the paired compact error
is already `o(n^{-1/2})`. This last sentence is a conditional implication,
not a claim that the required concentration estimate has been established.

## 7. Moving state, fixed storage, precision and work

The exact moving count is

\[
dq_1+q_1q_2+q_2+m\le q^2+q(d+1)+m.
\]

The two fixed packed symmetric metrics take
`q_1(q_1+1)/2+q_2(q_2+1)/2` real entries. Data cost `m(d+1)`.
Optional inverse metrics and runtime feature/Gram caches add
`O(q^2+mq+m^2)` entries. Thus the retained order is exactly the old

\[
O\big(\log(en)^{3d+2}\big)
\]

at fixed data. Rational parameters may need many bits. Neither a
polylogarithmic bit count nor bounded weight magnitude/conditioning is
claimed. That qualification matches the original real-coordinate
storage comparison; it must not be concealed as numerical efficiency.

With inverse metrics precomputed, one direct evaluation of (3)--(4) costs
`O(mq^2+mqd+m^2(q+d)+m^3)` arithmetic operations by matrix-vector
products, rank-one sums and an `m x m` solve. A passive query after the
current effective readout is formed costs `O(q^2+qd)`. No term involves
`n` except through the retained compact budget and chosen numeric
precision. These are vector-field/evaluation costs, not the number of
steps of an accuracy-certified ODE solver.

Setup is much more costly. If one compiler job expands into `M` monomial
graphs, each with at most `V` abstract neuron indices and random-factor
occurrences in total, equality partitions can
be enumerated in at most `V^V` choices per graph; their contractions use
finite one-dimensional moments and polynomial work in `V`, together with
the requested scalar precision. A conservative operation accounting is
`O(M V^V poly(V))` scalar operations after the symbolic expansion, plus
moment evaluation and precision costs. The counts `M,V` grow with the
ODE discretization, polynomial degrees, horizon, grid and score accuracy;
they can be enormous functions of `n`. The rational enumeration and
candidate integration add their actual finite search costs. There is no
useful a priori polynomial bound on these costs in this theorem, nor a
proved computable bound on the successful search stage from the inherited
stochastic width statement.

In particular, setup can exceed the work and temporary storage of a dense
network by an arbitrary factor. What has been removed is the *need for
a realized dense network as scientific input or intermediate object*, not
the general possibility of expensive preprocessing. This is a meaningful
direct-construction result at the old retained size, but it is not yet an
efficient practical method for obtaining a wide network's predictor.

## 8. Dependencies and boundaries

The three new proof pieces are the finite-width expectation compiler,
local tail certificate, and selection/termination argument above. The
neural existence inputs are the authorized integrated result's exact
dense independent-copy certificate, original-tolerance compact
specialization, and compact fitting proof. The relevant current passages
are in `integrated_general_compression_20261004/RESULT.md`, sections
"Explicit independent-dense upper certificates", "Every supplied budget
and its exact inverse", and "Independent fitting and endpoint control".
The runtime agrees with the explicitly authorized
`closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`.

This construction uses the training inputs and labels during initialization.
It does not settle the separate stronger dataset-blind initialization
question. It requires no frozen features, no small-label limit taken with
`n`, no favorable exceptional realized dense reference, and no population
trajectory or expected-jet analyticity assumption.

The unresolved strict root-width rate and the lack of an efficient setup
bound must remain visible in every synthesis. A complete conditional
reduction and a complete theorem at a weaker rate are not a complete proof
of the stricter original target.
