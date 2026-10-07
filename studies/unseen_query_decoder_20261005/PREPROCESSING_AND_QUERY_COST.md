# Preprocessing, query cost, and the meaning of the logarithmic exponent

2026-10-06. Continuation of the current-state decoder investigation in
response to the user's three interface questions. The current theorem is
unchanged. A small denominator-caching improvement is proved below; a
reasonable-time whole-sphere decoder remains open. No experiment or
preprocessing/decoding benchmark was run.

## 1. The preprocessing qualification is substantially inherited

The authorized finite-panel theorem already constructs temporal source
coefficients from the dense initialization, inputs and training labels by
finite initial-jet continuation and quadrature. It then selects coordinates,
forms compact matrices/metrics, and discards the full-width working objects.
It explicitly proves no efficient preprocessing-time bound. See
[finite-panel RESULT, Section 3](../finite_panel_absolute_compression_20261005/RESULT.md)
and [the integrated source construction, Section 9](../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md).

The current construction instead executes a finite noisy source program,
forms each row's complete vector of realized scalar-moment contributions,
and positively selects a small subset preserving their average. Selection
can depend on the completed source computation; see
[scalar acquisition, Section 4](NOISY_SCALAR_HISTORY_ACQUISITION.md).

Thus both results permit expensive offline computation of information
about the finite training trajectory. The old setup did not require an
externally supplied future trajectory, and the new setup need not either:
its source is computed from the initialization, training data and its own
additional random marks. Neither proves cheap or streaming selection.
Autonomous execution after setup does not establish autonomous/online
construction of the selected initialization.

There is no proved preprocessing-cost ordering between these different
algorithms. Calling the new qualification entirely new would be misleading;
calling the procedures identical would also be inaccurate.

## 2. Why decoding can take so long

The old finite-panel decoder evaluates a small nonlinear network at a
declared input. The current unseen-input decoder evaluates conditional
distribution tests by Fourier inversion and returns an approximate median.
The retained scalar history is held fixed throughout this calculation;
training scalar updates are not replayed.

The explicit algorithm has an outer tensor grid over frequencies and passive
query summaries, and an inner Gaussian tensor grid for one row packet.
The grids are streamed rather than retained. Section 6 of
[the evaluator](FOURIER_ROW_PROGRAM_EVALUATION.md) bounds the logarithm of
the total number of grid points by a fixed polynomial in its numerical
input parameter. This proves polynomial memory, not polynomial time in
that parameter. Tiny smoothing scales and the possible small conditional
density also require high absolute precision. Those requirements are
counted, rather than ignored, in the theorem.

No lower bound on the time of every admissible neural decoder follows.
A faster method would need structure beyond the generic bounded/Lipschitz
integration argument used here. Naive conditional sampling also requires
an efficient sampler or a quantitative acceptance/mixing proof, neither
of which follows from the present construction.

## 3. A safe caching improvement, with its exact limitation

For a completed scalar-history prefix of length \(j\), write its retained
rounded value as \(c\), its ideal-law density evaluated at that value as
\(p_j(c)\), and the Fourier numerator for a bounded CDF test at query
\(x\), patch time \(t\), and threshold \(a\) as
\(N_j(c;x,t,a)\). These are precisely the denominator and numerator in
Section 8 of the evaluator, not a new probability law. Since the test is
between zero and one,

\[
0\le N_j(c;x,t,a)\le p_j(c).
\]

The density depends only on the acquired prefix, not on \(x,t,a\).
Let \(d_j>0\) be the certified density lower threshold of the main proof.
On its rounded-state success event, \(p_j(c)\ge d_j/2\).
Compute and retain once an approximation \(\widehat p_j\) with error
at most \(d_j/1024\). For any query, compute its numerator to error at
most \(d_j/1024\), denoting that approximation by \(\widehat N_j\).
Then \(\widehat p_j\ge d_j/4\), and direct subtraction gives

\[
\left|\frac{\widehat N_j}{\widehat p_j}
       -\frac{N_j}{p_j}\right|
\le \frac{4}{d_j}
       \bigl(|\widehat N_j-N_j|+|\widehat p_j-p_j|\bigr)
\le\frac1{128}.
\]

The same estimate holds simultaneously for all queries, patch times and
CDF thresholds because the denominator and its error are shared, and the
numerator routine has a uniform deterministic error budget. Fourier
truncation and quadrature are included in those absolute approximation
errors. The remaining query-box-tail, smoothing and history-continuity
errors retain their existing budgets; final division roundoff fits the
remaining slack. On a bad-density flag use the main theorem's bounded fallback.

This cache adds at most one scalar per retained prefix. The requested
number of precision bits is already bounded by an absolute power of
\(\log(en)\). Thus it preserves the storage, scope and probability
qualifications. Acquiring the cache from the current state is a finite
autonomous calculation; its runtime may be enormous and is not claimed
small. Its value is a deterministic function of retained information, so
it introduces no extra latent observation or altered conditioning law.

This eliminates repeated evaluation of the training-only denominator,
including across the median's threshold searches. It does **not** eliminate
the query-dependent numerator grids, and consequently does not prove a
reasonable-time decoder. Storing a table of those grids would generally
violate the retained-storage bound; storing only the denominator does not.

## 4. Five versus an unspecified absolute exponent

The old finite-panel proof has temporal source order
\(O(\log^{5/2}(en))\). Its compact network stores quadratic-size selected
matrices, giving the explicit exponent five in real-coordinate storage.
Only predeclared test inputs are covered. Its bit complexity is not part
of that exponent-five statement.

The current construction uses a different proof and representation:
\(O(\log^8(en))\) source calls, \(O(\log^{16}(en))\) scalar summaries
and selected packets, and \(O(\log^{24}(en))\) raw packet/history entries,
before the additional instruction, matrix and numerical workspace.
These are upper bounds, not lower bounds showing that such losses are
necessary. The full theorem has an absolute exponent \(k\); it is a
fixed complexity exponent of the construction, not a user-selectable
order or accuracy parameter.

The previously assembled proof does not state a numerical value of \(k\).
Its existence follows from fixed-degree polynomial compositions, but some
upstream polynomial degrees were not enumerated. The honest claim is
therefore an absolute-polylogarithmic bound, not a new sharp exponent-five
theorem. The bit-space version additionally depends on the stated fixed
activation/input evaluation exponent. The
[exponent accounting](EXPONENT_ACCOUNTING.md) identifies the unenumerated
physical-compiler and sensitivity degrees and gives explicit downstream
formulas conditional on those degrees. It does not assign an arbitrary
numerical value to \(k\).

## 5. Status and scope of this continuation

The preprocessing comparison is a read-only source reconciliation. The
caching calculation above is an elementary author proof, separately
reconstructed by `preprocessing_compare` against the complete Fourier
evaluator: the shared-denominator identity, ratio constants, precision,
memory and unchanged conditioning all passed. The check requested the
error-budget clarification incorporated above. This is not a full-chain
reaudit or an efficient-decoder theorem. The independent bounded
[query-time route](QUERY_TIME_ROUTE.md) and exponent audit have separate
notes. The query-time route gives explicit obstructions to particular
generic rejection and log-concavity arguments, not a neural decoding lower
bound. The lead read and reconstructed its acceptance identity, density
bound, Hessian example and small-frequency Taylor estimate. The strongest current result
remains the current-state storage/workspace theorem. Efficient decoding
under all its original qualifications, and recovering exponent five for
unseen inputs, remain unresolved.
