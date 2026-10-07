# Separate construction confidence from reference confidence

2026-10-07. Bounded author refinement of the already composed source-seeded
decoder. This note changes only the per-member confidence allocation. It does
not replace the physical source theorem, finite-transcript generator theorem,
metric replay lemma, or dense comparison. It is not a promotion review.

## Statement

Keep the complete model, label interval, independent width-n dense reference,
whole-sphere/all-physical-time norm, endpoint, finite arithmetic, external
interfaces, and offline setup of `TWO_GAP_CLOSURE_RESULT.md`. Write
`n,m,d,L,gamma,Y,beta,delta` for its parameters and use its resource logarithm

\[
 Z=\log(en)+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right).
\]

The actual compact source members may all use the moment order

\[
 p=\max\left\{1,\left\lceil
 \frac{\log(2^{22}emL)}{\log(64e^2)}\right\rceil\right\}.
 \tag{1}
\]

It no longer contains `delta`. In every resource formula in
`CLOSURE_COMPOSITION_COSTS.md`, use (1) for the implemented field-count
factor. Leave `Z`, the external-code count, and the whole-source ensemble
confidence unchanged. Thus the explicit moment-order factors `p^2`, `p^5`,
and `p^4` in memory, setup/training, and query work need no dependence on
the final confidence. This never enlarges the former bounds.

The independent dense reference still uses failure `2^(-20) delta` and
therefore its proof uses

\[
 \max\left\{1,\left\lceil
 \frac{\log(2^{22}emL/\delta)}{\log(64e^2)}\right\rceil\right\}.
 \tag{2}
\]

Retain (2), not (1), in the enclosing scientific width condition. This
refinement does not reduce the reference's width requirement or assert
one high-probability event for every member separately.

## Proof

1. **One source experiment.** Invoke the finite physical source theorem
   at the fixed failure `2^(-20)`. Substitution into its stated moment
   order gives (1). Choose the common source/query numerical schedule,
   finite metric replay, and inner finite-transcript transfer with fixed
   absolute failure allocations whose sum, together with that scientific
   failure, is below `1/16`. These are precisely the fixed-query component
   interfaces of `SOURCE_SEED_EXACT_QUERY.md`, Sections 2--4. Its output
   is within the same dense-center certificate plus allocated numerical
   error for each fixed external input/time code with probability at least
   `15/16`. In particular no source failure must be divided by the number
   of external codes. All member randomness, including source success or
   failure, is included in this one experiment.

2. **Amplify complete experiments.** For an odd number `J` of independent
   complete experiments with bad probability at most `1/16`, a bad
   majority has probability at most
   \(2^J(1/16)^{J/2}=2^{-J}\). Use the same outer block generator
   and bad-majority verifier as Section 5 of that note, with generator
   error at most `delta/(16 N_ext)` for each fixed code. The number of
   codes obeys `log N_ext <= C(d+1)Z`. Choosing
   `J >= C log(16 N_ext/delta)` and summing the per-code probabilities
   establishes the same simultaneous coded event. This argument never
   conditions on all sources being good and never treats regenerated
   members as statistically independent after the generator substitution.

3. **Compare the independent reference.** The separate physical good-set
   and Gaussian-concentration event for the independent dense reference
   is unchanged. Its source probability is controlled at
   `2^(-20) delta`, which gives (2). The corresponding width requirement
   dominates the member requirement because `delta<1`, its reciprocal
   confidence factor is larger, and (2) is at least (1). The deterministic
   good-set center used by the member comparison can be chosen to be the
   same one as in the original composition: the reference's smaller
   failure allowance is obtained by a larger sufficient width for the
   same physical bounds, not by supplying different decoder advice.

4. **No other interface changes.** Physical rounding from finite codes,
   the fitted tail, and absorption of the preallocated `Y n^(-10)`
   numerical remainder are the original ones. Their confidence shares
   remain available after the fixed per-member allocation in step 1,
   since that allocation is paid by whole-source amplification rather
   than added once to the final failure. Smaller moment order enlarges
   the source analytic radius, so the same field-count construction uses
   fewer, not more, time patches. The original common `Z` remains a safe
   precision and code-length envelope.

Consequently the final comparison remains `3 b_n` with probability at least
`1-delta`, with all original qualifications. Only construction resource
factors depending algebraically on the moment order improve. The
unexpanded leading dense coefficients in `b_n` are not quantified by
this argument.

## Boundary and inputs

This is the explicit proof of the fixed-member-confidence option already
identified in Section 1 of `CLOSURE_COMPOSITION_COSTS.md`. It does not
replace a polynomial dependence of the source coordinate event on
`delta^(-1)` by a logarithmic one. That event for the independent reference
still uses (2).

Complete directly used inputs: `SOURCE_SEED_EXACT_QUERY.md`,
`CLOSURE_COMPOSITION_COSTS.md`, `TWO_GAP_CLOSURE_RESULT.md`,
`TWO_GAP_CLOSURE_CHECK.md`, and `FULL_FINITE_SOURCE_PROBABILITY.md`.
Shared notation, research, and rigorous-proof instructions were applied.
No experiment, original-source edit, Git mutation, or external result is
introduced by this refinement.
