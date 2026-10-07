# Small-exponent unseen-query compression: current proof-search result

2026-10-06. Current-study research, not a promoted theorem. This report
separates improvements to individual constructions from the still-open
complete fourth- or fifth-power decoder. All checks below are bounded
internal reconstructions, conditional on their stated source interfaces.

The strongest new direction combines a logarithmic-power `5/2` causal
training source with a quadratic-size coordinate metric for its pair
data. Both ingredients have survived separate bounded reconstruction.
Their full noisy unseen-query composition, including precision and peak
query memory, remains open. There is no completed `log^5` decoder theorem.

## Target and common qualifications

The target remains the original nonlinear, all-layer-trained dense network:
width `n`, fixed hidden depth `L >= 2`, independent Gaussian initial matrices,
zero readout, mean squared loss and block mobilities `(n,1,...,1,n)`.
There are `m >= d` training inputs of norm `sqrt(d)` spanning `R^d`.
The population feature-Gram gap is `gamma > 0`, and
`Y = ||y||_2/sqrt(m)` obeys the full original small-label intersection.
Activations are strip analytic with bounded derivatives; their values need
not be bounded. The case `Y=0` has the stationary zero predictor.

A query is a previously unseen sphere input. The target is one success
event giving accuracy over the entire sphere and physical trajectory,
including the endpoint, at the independent-dense upper-certificate scale.
It is not silently replaced by fixed-query probability, frozen features,
near-`1/n` fidelity to a specified dense realization, or actual-discrepancy
comparison. Retained descriptions and peak query memory count. Setup may
inspect its finite source, but its work and memory count. Querying may not
replay training, retrieve discarded dense arrays, or call an uncharged
integration or activation oracle.

Exact-real coordinate counts and finite-bit counts remain distinct.
In particular, the old panel's fifth-power real-coordinate result is not
an already proved fifth-power bit-complexity theorem.

For the parameter-explicit source bounds below, keep the existing activation
envelope

\[
 \beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
 \max_{j,\,1\le k\le2}\sup_{|\operatorname{Im}z|<a/2}
                         |\phi_j^{(k)}(z)|\right\},
\]

where `a` is the supplied strip width. Write

\[
 \ell=\log(en),\qquad
 Z=11\ell+\log\!\left(e+\beta^{100L}(1+m/\gamma)\right).
\]

The fixed integer ten is the normalized numerical prediction-accuracy
exponent, not an additional order parameter. Every unnamed constant in
the displayed source bounds is numerical. Evaluator, input-description
and certificate costs are not included in such a constant.

## Checked improvements

### A shorter, stable physical training computation

The first improvement controls the *integrated* Chebyshev interpolant,
not its pointwise interpolation norm. Its norm is at most
`pi/(2 sqrt(2))`, independently of polynomial degree. This permits a
larger stable collocation patch without an implicit-solve oracle.
The proof and bounded reconstruction are
[SANE_INTEGRATED_COLLOCATION.md](SANE_INTEGRATED_COLLOCATION.md) and
[its check](SANE_INTEGRATED_COLLOCATION_CHECK.md).

The second improvement preserves the decay of the training residual in
the numerical stability estimate. On each patch, cap the numerical
residual at a predetermined, decreasing radius that still contains the
true residual. The cap leaves the reference trajectory unchanged.
The nondecaying derivative of the residual map is retained in the bound;
only the other terms become summable in time.

Together these give a causal dense source with at most

\[
 C\left[d+mL\beta^{300L}(1+m/\gamma)^3 Z^3\sqrt\ell\right]
\]

initialized matrix actions and principal row fields, approximating the
physical predictions uniformly over the sphere and all time within
`Y n^(-10)` on the inherited fitting/source event. Physical matrix-answer
noise needs at most `C beta^(100L)(1+m/gamma) Z` exponent bits under
the supplied perturbation interface. These are source-program results,
not compact-model storage bounds. The vectors still have width `n`.

The complete new argument and reconstruction are
[SANE_ADAPTIVE_TIME.md](SANE_ADAPTIVE_TIME.md) and
[its check](SANE_ADAPTIVE_TIME_CHECK.md). A stronger passive-coefficient
accuracy allocation and compact noisy-source compilation remain separate
handoffs. No effective stochastic width threshold was proved.

### A substantially smaller decoder implementation

[SANE_DECODER_CORE.md](SANE_DECODER_CORE.md) replaces materialized
Kronecker systems by ordinary spectral calculations, prepares shared
coefficients once, uses the actual causal depth for numerical sensitivity,
and applies the random-generator theorem to small one-pass median-failure
tests rather than the full decoder workspace. Matrix arithmetic, Gaussian
generation and retained seeds are counted explicitly.

[The isolated check](SANE_DECODER_CORE_CHECK.md) reconstructed these
improvements and found one scale factor missing from a spectral residual
argument. That factor has been restored and the correction rechecked.
The improved bounds still have large logarithmic powers; this is not the
requested economical decoder. The old exact support-selection cost also
remains in that particular implementation.

[SANE_CORE_COMPOSITION.md](SANE_CORE_COMPOSITION.md) additionally gives
an elementary positive dyadic-weight rounding argument and a conditional
resource composition with the first shorter source. Its full combined
ledger has not received a fresh end-to-end reconstruction. Its powers
are not substituted into the checked `COST_CONTRACT.md`.

## What the alternative routes actually establish

The predeclared-panel route identifies a cheap scalar Gaussian correction
for an unseen input. A one-dimensional convolution can be evaluated in
logarithmic-power `3/2` activation calls when its strip and variance
parameters are fixed. But the old selected-neuron theorem does not give
the uniform weak quadrature needed to apply this correction at every
unseen input and throughout nonlinear training. An actual admissible
depth-two cosine example has a nonvanishing initial-velocity bias if the
Gaussian innovation is simply dropped.

In particular, the old theorem does not license adding a new test input
after setup and only replaying the already selected tiny network: the
selection was certified for the original declared inputs. Rebuilding or
augmenting that selection needs its own argument and cost bound.

The response-memory route gives an exact quadratic-size state for the
positive gradient-Gram part of the response when its finite basis and
contractions are supplied. It also derives the exact omitted nonlinear
memory. An admissible depth-two, two-sample example has a nonvanishing
sample-gradient commutator: that nonlinear term cannot simply be declared
zero because width is large. This does not rule out compressing it.

The full arguments are
[SANE_PANEL_EXTENSION.md](SANE_PANEL_EXTENSION.md) and
[SANE_RESPONSE_MEMORY.md](SANE_RESPONSE_MEMORY.md), with a
[fresh bounded reconstruction](SANE_MEMORY_ROUTES_CHECK.md). Neither
example is an impossibility result for all unseen-query representations.

## Decision and unresolved target

The elementary panel-extension and truncated-response shortcuts stop at
genuine missing mechanisms. They are parked, not declared impossible.
The constructive source/decoder route has supplied concrete, checked cost
reductions, so the followup effort is concentrated there.

Two structural followups have now produced checked, scoped results.

1. [SANE_METRIC_PACKETS.md](SANE_METRIC_PACKETS.md) uses a small set of
   original row packets and a matrix to reproduce all training pair
   averages. Its finite-table theorem needs only as many packets as
   independent named fields, rather than as many as pair averages. A
   determinant-improvement algorithm avoids any unknown source-Gram gap.
   The initial independent reconstruction found a setup-memory scheduling
   issue in full-table elimination. A streamed small-basis implementation
   repaired it without changing the bounds, and the repair was rechecked
   in [SANE_METRIC_PACKETS_CHECK.md](SANE_METRIC_PACKETS_CHECK.md).
   This validates the finite-table algorithm and its conditional use in
   the existing pair-based source compiler, not the Taylor composition.
2. [SANE_TAYLOR_SOURCE.md](SANE_TAYLOR_SOURCE.md) replaces repeated
   collocation iterations by causal scaled Taylor coefficients. Its
   checked initialized-action count is

   \[
   C\left[d+mL\beta^{200L}(1+m/\gamma)^2Z^2\sqrt\ell\right].
   \]

   The reference remains the original nonlinear dense flow, with an
   explicit additional horizon gate
   `n >= max(1, exp(-1) sqrt(1+66 beta^(100L)m/gamma))`.
   The essential claim is stability at approximate Taylor anchors, not
   merely analyticity of the exact trajectory. Activation jets and their
   finite-value evaluation cost are explicit separate obligations.
   [SANE_TAYLOR_SOURCE_CHECK.md](SANE_TAYLOR_SOURCE_CHECK.md) reconstructed
   the source theorem under the original source/fitting interfaces. Its
   minor finite-difference-spacing clarification has been incorporated
   and rechecked.
   This check is explicitly not a blind promotion review.

These pieces explain why fifth-power *training-summary coordinate*
storage is a credible route: the Taylor source has logarithmic-power
`5/2` field count, and a coordinate metric stores pair information
quadratically. That observation is not yet their full noisy statistical
composition. In particular, higher-derivative precision, the retained
query seed, peak query scratch, and the error of the new noisy Taylor
source still need their own bounds. The existing decoder's seed and
scratch already exceed the proposed quadratic summary count.

The highest-leverage next obligation is therefore a stable noisy Taylor
source/metric composition with a genuinely economical query state, not
another loose substitution into the old large-exponent ledger.

The full target remains open: a fourth- or fifth-power retained-plus-peak
decoder, with civilized parameter dependence, charged setup/training/query
costs, and the original simultaneous sphere/time accuracy guarantee.
Numerical source call counts, finite training-summary size, decoder
randomness, scalar precision and prediction-transfer estimates are
different obligations. Satisfying one does not discharge the others.

No experiment, implementation benchmark, Git mutation or promotion was
performed in this proof-search round. Existing unrelated work was preserved.
The lead used the conjecture-investigation and rigorous-math workflows;
the inaccessible private notation skill was replaced by the explicit
user/repository notation requirements and maintained notation contract.
