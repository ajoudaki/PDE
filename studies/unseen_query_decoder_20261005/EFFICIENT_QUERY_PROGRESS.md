# Efficient unseen-input decoding: current proof status

2026-10-06. **The efficient full decoder remains open.** This continuation
improves the numerical implementation and proves new structural estimates,
but does not turn the existing low-memory decoder into a fast one. No
experiment or promotion is claimed.

## Contract retained

Use exactly the model, label allowance, feature-Gram assumption, confidence,
sufficient-width qualification, and whole-sphere, complete-training error
benchmark in [RESULT.md](RESULT.md). This includes nonlinear feature
learning at arbitrary fixed depth, possibly unbounded activation values,
unseen inputs without test labels, and the fitted endpoint. All retained
arrays, precision, and peak decoding workspace count. A query must use the
present compressed state, without replaying the scalar training updates or
accessing discarded dense weights.

The user explicitly confirmed query time polynomial in the compact model's
size. The target is therefore a fixed-degree polynomial in the counted
compact description and logarithmic requested precision, hence an absolute
power of `log(en)`, with fixed-problem constants as in the storage theorem.
Polynomial-in-dense-width or dense-forward-pass time is **not** an accepted
substitute, even with compact memory. Expensive source preprocessing remains
allowed, but is not renamed efficient training.

Runtime relative to the original activation primitives and actual bit time
are separate. The existing polynomial-space precision interface does not
imply polynomial-time activation evaluation. The matrix improvement below
is a bit-time result; it does not upgrade external activation interfaces.

## Completed improvements

### Polynomial-time small-matrix arithmetic

[FAST_SMALL_MATRIX_FUNCTIONS.md](FAST_SMALL_MATRIX_FUNCTIONS.md) replaces
inverse-gap-length series by exact rational inversion and a rounded Newton
square-root iteration. Their bit time and workspace are polynomial in
matrix dimension, input precision, and the logarithms of magnitude,
inverse gap, and requested inverse error. The proof explicitly controls
noncommuting rounding errors, positive-semidefinite buffers, exact caps,
Kronecker dimensions, and precision across the coefficient graph.

This is an unconditional replacement within the existing matrix interface:
no stronger neural assumption or larger asymptotic memory class is needed.
It preserves the current prediction guarantee when the same local error
budgets are used. The original proof's frozen header predates the
[independent numerical reconstruction](FAST_SMALL_MATRIX_FUNCTIONS_CHECK.md),
which passed without requiring a correction.

The improvement makes the matrix work at each integration point polynomial
in the counted compact parameters. The number of integration points is
unchanged and can still be enormous. Thus it does not establish reasonable
total query time.

### A short expansion of the actual nonlinear response

[EFFICIENT_QUERY_DIRECT.md](EFFICIENT_QUERY_DIRECT.md) treats the
contractive Gauss--Newton part of the actual variational dynamics exactly
and expands only the residual-weighted curvature. Under the inherited
all-time residual integral and carrier bounds, the curvature has total
operator action at most a fixed constant times `sqrt(log(en))`. The
ordered expansion consequently has a factorial tail. In particular,

\[
\text{response truncation error}\le n^{-2}
\quad\text{using order}\quad
O\!\left(\frac{\log(en)}{\log\log(e^e n)}\right).
\]

This is uniform over finite physical times; no derivative at the fitted
endpoint is asserted. The response-trace normalization loses no extra
power of width. These are statements about the actual nonlinear flow,
not a frozen-feature approximation or a smaller label regime.

The positive part also has a scalar, two-time training resolvent with
`O(log(en)^5)` coefficients, under the stated common complex-time extension
and complex RMS bounds. This is **not** a new `log(n)^5` decoder theorem:
it counts that one scalar object, does not acquire its coefficients, and
does not evaluate the remaining curvature contractions.

The [scoped independent check](EFFICIENT_QUERY_DIRECT_CHECK.md) reconstructs
these claims under their displayed inherited interfaces. It does not
review the original dense certificates or certify a full decoder.

### Information control without an inverse-noise penalty

[EFFICIENT_QUERY_INFORMATION.md](EFFICIENT_QUERY_INFORMATION.md) proves
that the noisy current history contains only absolute-polylogarithmic
information about the independent Gaussian row packets. A posterior
entropy maximal inequality gives one event covering every acquired prefix.
On that event, conditional empirical averages of each bounded row function
are close to its prior average, including functions selected using the
current state and an unseen input. The lead reconstructed the entropy,
maximal-inequality, and change-of-measure arguments.

The quantifier is important: the same event gives an estimate for every
test's conditional expected discrepancy. It does not bound the expectation
of the supremum over all bounded measurable tests.

The note also gives a counterexample to naive population substitution:
two occurrences of one empirical moment must agree, whereas replacing only
the query occurrence by its population mean breaks that identity. A large
intermediate gain can then create order-one output error. This is a
generic row-program counterexample, not a neural-decoder lower bound.

### Preserve the acquired moments before approximating a query

[EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md](EFFICIENT_QUERY_PHYSICAL_SYNTHESIS.md)
provides two concrete repairs. At an ideal current prefix, a unique
minimum-relative-entropy row distribution matches every acquired moment
within a proved scalar-noise tolerance. It has an exponential-tilt
description using only as many multipliers as acquired moments. Strict
feasibility follows from an all-prefix posterior noise estimate, so no
new covariance gap is assumed. Multiplier rounding has an explicit total
variation bound and an absolute-polylogarithmic bit count. This does not
yet control perturbing the retained prefix itself.

Alternatively, reuse any component of the query integrand that is a known
linear combination of the stored training tests, and average only the
remaining component. The statistical error then depends on the remaining
component's oscillation, plus the original scalar noise times the reuse
coefficients. This exactly fixes the redundant-moment counterexample.
The lead reconstructed both arguments, and a
[separate scoped check](EFFICIENT_QUERY_PHYSICAL_SYNTHESIS_CHECK.md)
passed the noise, tilt, rounding, and fixed-test estimates. The actual
nonlinear query still needs a useful remainder bound and a stable multistep
propagation theorem. The check does not cover the conditional physical
forcing lemma or a full decoder.

Neither a short list of tilt multipliers nor this algebraic decomposition
provides fast normalization or fast integration. These are proved local
repairs, not a full decoder.

## What still prevents an efficient decoder

There are two distinct unsolved tasks, and neither follows just from the
small amount of retained information:

1. **Stable evaluation from the compressed state.** Preserve the training
   moment identities and bound the actual unseen-query output error on the
   dense-variability scale, without the artificial inverse-noise gains of
   the current row-coordinate formulas. The convergent response expansion
   does not yet provide a compact recurrence for all required contractions.
2. **Fast integration or an integration-free representation.** Even a
   stable population formula needs its row expectations evaluated. A
   high-dimensional Gaussian integral is not a unit-cost operation.

[EFFICIENT_QUERY_COMPILATION.md](EFFICIENT_QUERY_COMPILATION.md) gives a
precise conditional alternative: if uniformly accurate, polynomial-size,
stably evaluable query circuits exist, unlimited current-state compilation
can find and certify one using compact workspace. The lead reconstructed
this finite enumeration and net-certification argument. The required
small-circuit existence theorem is unproved; the compiler does not supply
it. Generic analyticity and universal polynomial cubature do not resolve
that missing structure. The note's representation-specific lower bounds
are not lower bounds for the actual neural decoder.

[EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md](EFFICIENT_QUERY_RANDOMIZED_INTEGRATION.md)
also proves a finite-seed, streamed Gaussian cubature lemma. A retained
limited-independence seed and a proof-only query net give one event over
all actual prefixes, sphere inputs, and time patches, with compact memory.
The lead reconstructed the moment estimate, seed construction, net argument,
and treatment of adaptively computed query summaries. Under additional
range and stability bounds this would give polynomial-in-dense-width
time. It is **not an accepted solution** after the user's runtime
clarification: ordinary sampling at root-width accuracy can require a
width-scale number of evaluations. Moreover, the needed actual-neural
range and stability bounds are themselves still unproved.

## Claim and route ledger

| Claim or route | Current status | Exact remaining bridge |
|---|---|---|
| Existing absolute-polylogarithmic memory decoder | Unchanged, internally checked under inherited certificates | No efficient query time was previously proved |
| Polynomial-time small-matrix implementation | Proved and independently reconstructed | Does not reduce integration point count |
| Short nonlinear response expansion | Proved under displayed inherited bounds; independently reconstructed | Compact acquisition and evaluation of its contractions |
| All-prefix posterior information bound | Proved; reconstructed by lead | Stable nonlinear moment-to-output map |
| Moment-consistent tilt and compensated query average | Proved local constructions; lead and scoped independent reconstruction | Actual neural remainder bounds, prefix-rounding stability, and efficient integrals |
| Offline circuit compilation | Conditional construction; reconstructed by lead | Existence of sufficiently small response circuits |
| Finite-seed streamed cubature | Proved conditional numerical lemma; reconstructed by lead | Its width-scale sampling cost does not meet the accepted query-time target |
| Efficient full decoder under the original contract | Open | Statistical/physical stability and counted query computation |

No route here proves impossibility. No special-case fast decoder has been
substituted for the original model. The numerical subroutine replacement
improves one implementation choice; it does not supersede or strengthen the
main theorem's error, storage exponent, or sufficient-width claim.

The highest-leverage continuation is a moment-consistent query reduction
whose residual has the required physical stability **and** an efficiently
evaluable representation. Recording a short list of coefficients without
accounting for the integrals they specify would not close that bridge.
