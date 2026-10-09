# What can be proved about a small terminal tensor program?

## Answer and scope

With a fixed number of query inputs supplied at initialization, the
authorized response-compression results yield an executable numerical
program with polylogarithmic **retained real-coordinate state**, including
its prediction and update workspace. A new stopping argument below shows
that this remains true when the numerical model and dense gradient flow
each stop using their own training loss. The program need not store past
Euler steps.

This is not yet the corresponding theorem for a standard population
tensor program. Three notions must not be conflated:

| Meaning of size/accuracy | Current conclusion |
|---|---|
| Retained real state of the response-compressed numerical program, compared with the paper's whole-trajectory dense-variability benchmark | Positive, using the authorized compression theorem and the stopping/compiler lemmas proved here |
| Fully unrolled standard-TP computation through stopping, or its total numerical work and bits | Not proved polylogarithmic in the full neural scope |
| Relative error measured against actual variability of the stopped query outputs alone | Not proved in the full scope; proved in a restricted shallow RMS example below |

The positive result is more than a short source-code description of a
dense simulator or a cache of the final query answers: its current neural
state, fixed matrices, prediction evaluator and RHS workspace are small.
Its numerical execution can continue using the same stored state. It is
less than a small-bit, cheap-setup or short-unrolled-computation theorem.

These are internally checked research results, not promoted book or paper
claims. The imported neural source theorem has a prior scoped internal
reconstruction; this investigation checks its relevant interfaces rather
than claiming a new independent review of every inherited lemma.

## 1. General retained-state result

Use the canonical Gaussian zero-readout network with width `n`, hidden
depth `L`, `m` labelled inputs in dimension `d`, and `p=O(1)` passive
query inputs declared at initialization. Their labels are not supplied.
Let `gamma>0` be the initial population feature-Gram gap,
`Y=||y||_2/sqrt(m)>0` the label RMS, and `beta` the existing activation
envelope. The full original small-label allowance and strip-analytic
activation class remain in force, **including unbounded activation
values**. For numerical statements the activation backend is the same
one available to evaluate the dense model and its derivatives.

For every fixed admissible problem and confidence `1-delta`, and every
sufficiently large individual width, the following sufficient retained
real-coordinate inventory is available:

\[
\begin{split}
C\beta^{CL}(m+p)^2\bigg[
 &\left(\frac{Ym}{\gamma}\right)^4[\log(en)]^3\\
 &+\left(\frac m\gamma\right)^2[\log(en)]^2
               [\log(e+\log(en))]^2\bigg]
 +C(m+p)d+D_{\rm alg}.
\end{split}
\tag{1}
\]

`C` is absolute, and `D_alg` explicitly charges the scalar activation
program/workspace. This bound includes fixed coefficients, learned
coordinates, metric caches, input data and ordinary runtime buffers.
The explicit powers of `Y` are not removed using the label condition.
For fixed problem parameters its leading width dependence is
`[log(en)]^3`; it is polynomial in `m,d,gamma^{-1}` at fixed depth and
activation. The width onset can depend on all fixed problem parameters
and confidence, is not quantified polynomially, and is not a uniform
joint-growth guarantee.

For example, stop each model at its first training MSE at most `Y^2/n`.
The compressed model uses sufficiently fine streamed Euler steps; the
reference uses exact gradient flow. With the same source-event
probability, the resulting query predictions satisfy

\[
\max_{i\le p}
|f_{\rm num}(\tau_{\rm num},x_{m+i})
                    -f_n(\tau_n,x_{m+i})|\le Y/n.
\tag{2}
\]

The labels do not shrink with `n`: `Y^2/n` is a chosen stopping loss.
A fixed positive stopping loss below the initial one also works. The
complete proof and treatment of other positive thresholds, zero labels,
initial stopping and exact-zero endpoints are in
[STREAMED_STOPPING.md](STREAMED_STOPPING.md).

For `m>=2`, the previously proved early-time training-input witness gives
a lower bound of order `Y sqrt(gamma)/(sqrt(n)log(en)^{5/2})` on the
independent dense-pair **whole-trajectory panel** discrepancy. Thus the
stopped-output error in (2) is negligible relative to that benchmark in
probability. This use of the existing benchmark is legitimate even
though the output is requested only at stopping. It must not be restated
as a lower bound on the two stopped outputs' own discrepancy.

### Why stopping does not destroy the accuracy

Locally in this paragraph write `rho` for the dense training RMS and
`lambda=gamma/m`. The fitting and gradient bounds give

\[
-\rho'\ge\lambda\rho/2,\qquad
|\partial_t f_n(t,x)|\le2\beta^{14L}\rho(t).
\]

Integrating the ratio of these two bounds shows that changing the RMS
level by `e` moves a query prediction by at most
`4 beta^{14L}e/lambda`. Consequently same-time prediction error `e`
and a final Euler RMS decrement at most `e` yield stopped-output error
at most

\[
e\left(1+8\beta^{14L}\frac m\gamma\right).
\tag{3}
\]

There is no inverse stopping-loss factor. Asking the source compiler for
the corresponding fixed-factor tighter tolerance changes an eventual
degree/width gate, not the logarithmic power in (1). A finite Euler
step exists by a compact-tube error bound, and one state/derivative
buffer is reused. [STOPPING_CHECK.md](STOPPING_CHECK.md) reconstructs
this argument independently from its mathematical hypotheses.

### What was imported, and what is new

The third-power source rank comes from the authorized adaptive-clock
study. Its complex-time domain widens as residuals decay, reducing the
number of temporal panels. Coordinate selection and the corrected
autonomous nonlinear optimizer are unchanged. The detailed dependencies
and exact rank/inventory are in
[TP_REPRESENTATION.md, Section 4](TP_REPRESENTATION.md).

The new additions are the streamed arithmetic execution and own-loss
stopping transfer, not a new stochastic compression or TP master
theorem. Initial jets compute the retained coefficients using only the
dense initialization and training data. This is finite information
provenance, not a cheap setup theorem. Dense arrays, jet arrays and
temporal source arrays are all discarded before the small-state run.

## 2. Ordinary population TP: exact representation versus efficient evaluation

For a fixed Euler step count, the trained matrices can be expanded as
their initialized Gaussian action plus sums of past outer products.
The exact population TP then tracks Gaussian covariances and response
derivatives accounting for reuse of each matrix and its transpose.
These are not independent newly sampled Gaussian actions.

The finite shared expression graph avoids exponential tree expansion,
but its usual stored covariance/response table grows quadratically in
the number of source calls. An unevaluated Gaussian expectation is not
a numerical instruction of unit cost. Conversely, this history count is
not a universal memory lower bound: a compact generator can recompute
coefficients, trading space for time.

[TP_REPRESENTATION.md](TP_REPRESENTATION.md) gives the actual recursions,
their graph/table counts, and a finite quadrature compiler. The compiler
handles singular covariance matrices by a proved square-root continuity
bound, so it does not require a fabricated minimum history-Gram gap.
However, its precision and integration costs are not polylogarithmically
bounded for a growing program. The fixed-program TP master theorem also
does not itself provide a finite-width error rate uniform through a
width-dependent stopping computation. See Yang and Hu's
[TP IV supplement, Sections G--H](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf).

Thus neither an affirmative standard-TP complexity theorem nor an
impossibility theorem is established in the general scope. A fully
unrolled graph has a different size from the reused loop in Section 1.
Its increasing step count cannot be erased by referring to the small
loop body.

## 3. A restricted, genuinely numerical population result

A separate constructive route does eliminate all expectation oracles
and count bits. It covers one hidden layer and one training sample,
with a positive, bounded, nonconstant strip-analytic activation such as
`1+c tanh`, `0<c<1`. Hidden weights train nontrivially. Queries have a
fixed positive orthogonal component to the training direction.

The exact dynamics reduce to a scalar feature clock and a two-dimensional
neuron ODE. The population terminal predictor is a two-Gaussian
expectation. Truncating those roots and approximating the two query
coordinates by Chebyshev polynomials gives a numerical evaluator with

\[
O([\log n]^3)\ \text{coefficients},\qquad
O\big((d+[\log n]^3)(\log n+\log d)\big)\ \text{retained bits}.
\tag{4}
\]

Its mean bias against the finite dense endpoint is `O(1/n)`, while
the actual dense endpoint variance is bounded above and below by
positive constants times `1/n`. A direct bias--variance calculation
then gives

\[
\frac{\text{population evaluator--dense RMS error}}
     {\text{independent dense--dense RMS discrepancy}}
\longrightarrow\frac1{\sqrt2}.
\tag{5}
\]

This is an ensemble RMS statement at the endpoint, not a high-probability
ratio to a particular realized dense pair. It has a finite, explicitly
described quadrature/ODE setup; setup can be polynomial in `n` with
large fixed-parameter constants and separately charged activation
evaluation. The decoder can even receive a query after compilation in
this restricted case. See
[TERMINAL_APPROXIMATION.md](TERMINAL_APPROXIMATION.md) for the complete
proof, constants and cost model.
The focused reconstruction is recorded in
[TERMINAL_CHECK.md](TERMINAL_CHECK.md).

The result does **not** close the full request: it restricts sample
count, depth, activation values and the comparison norm. Generalizing
its tensor polynomial in the training-span coordinates gives an
exponent depending on that span dimension, not the desired absolute
logarithmic exponent. It cannot be silently substituted for Section 1's
full activation/data scope.

## 4. Exact remaining obligations

For the strongest reading of the original request, the open bridge is
a numerically evaluated, growing population-TP representation whose
state/precision is polynomial in the data parameters and polylogarithmic
in width, together with a finite-width comparison at the desired
stopping scale. A small symbolic formula does not supply that bridge.

If the denominator is specifically stopped-query variability, one must
also prove a relative comparison there, not borrow an early-training
witness. Stopped variability can vanish: for one training observation,
the first positive loss-threshold prediction is exactly
`y-sqrt(threshold)` when starting below the label, independent of the
initial weights. This observation diagnoses the inference, not a
compression impossibility; that particular output is easy to compute.

The bounded investigation therefore stops with a general retained-real-
state extension, a restricted fully numerical population theorem, and
these explicit unresolved stronger claims. No experiments, paper
changes, promotion, Git commits or pushes were performed.
