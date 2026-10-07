# Integrated-results audit

2026-10-07. Venue-neutral, unscored internal audit requested by the author.
The theorem document and README were not edited. No commit or promotion.

## 1. Summary

**Not yet fully harmonized, and not yet independently certified as a fully
self-contained proof.** The checked downstream calculations support the
existing headline rates, conditional on their source inputs. No counterexample
to the principal compression theorems was found. Two proof-completeness
concerns prevent a blanket endorsement; several localized interface errors
also need correction.

Reviewed [RESULT.md](RESULT.md), 13,187 lines, SHA-256
`5aae8d6de7d73cd3b2ddc081d3e45796438480878cc0dbf50f66ab0c66df8f23`.
All locations below refer to this unchanged version. Full evidence and coverage
are in [evidence_log.md](evidence_log.md); claim-level verdicts are in
[claim_ledger.md](claim_ledger.md).

## 2. Main contributions

The document combines dense upper and transient lower variability bounds,
Legendre memory compression, Harmonic compression with two efficient
initializers, and finite-word Logarithmic decoder compression. It gives
forward-order and inverse-accuracy interfaces, storage inventories, and setup,
training and query costs.

## 3. Strengths

The deterministic signed comparisons, Harmonic metric construction,
supplied-budget inversion, and adaptive Gaussian execution survived targeted
reconstruction. The finite-horizon and late-time source-domain statements
match the hypotheses used by the efficient initializers. The resource
substitutions are consistent, including the extra word-precision factor for
the Logarithmic decoder. The document appropriately distinguishes fresh
implicit references from conversion of supplied dense matrices.

Under the fixed-label convention, this audit supports retaining the current
sample/gap powers: cubic for the displayed Legendre learned-state envelope
and quartic for Harmonic retained storage. It finds no basis for claiming a
new reduction. The Logarithmic resource ledger supports six logarithmic
powers with an extra log-log factor in words, seven in bits, not five.

## 4. Weaknesses and claim-level concerns

### M1. The shared source bridge still needs an explicit reconstruction

At RESULT lines 4071–4074, bounds for the forward/backward/query derivative
graphs are asserted without their complete recurrences. Lines 4116–4156 give
nonlinear remainder scales without the complete remainder equation. The
control-uniform map bounds, reverse-probe estimate, and complete nonlinear
remainder induction were not independently reconstructed in this audit.

The mechanism and exponent margins are plausible. The audit did not derive
every omitted contribution, so this is **an unresolved proof-completeness
concern, not a demonstrated false theorem**. It propagates to the dense
upper bound, derivative-to-trajectory lower bound, Legendre approximation,
Harmonic approximation, and setup accuracy insofar as they require this
source event. Initialization/fitting, initialized fluctuation calculations,
and the conditional deterministic results remain independently useful.
The caveat at lines 1581–1591 is appropriately cautious; the blanket
self-containment assurances elsewhere are stronger than this audit supports.

A second targeted reconstruction recovered the principal direct and
integrated scalar traces and found no evident incorrect coefficient. It
also identified the residual-gradient rank-one trace, which needs to be
explicitly assigned to the vanishing remainder. This narrows the scalar
trace concern to an omitted derivation; it does not independently establish
the earlier control-uniform derivative graphs and nonlinear remainder.
The scalar bridge is therefore a minor localized omission (L9), whereas M1
concerns the upstream completeness/coverage limitation. Neither is a verified
failure of the source theorem.

### M2. The Logarithmic decoder section is a composition, not the promised complete construction

Lines 7853–8150 summarize the finite source, finite transcript transfer,
query coupling, and resource ledger. They do not contain the full finite
program, common source/query precision schedule, metric replay proof,
physical input/time coding construction, or finite arithmetic backends.
For example, lines 8046–8054 give the conditional query schematic but not
its finite coefficient definitions; lines 8058–8066 invoke the numerical
coupling rather than deriving it.

These ingredients have named dependency notes; their omission is not evidence
that they cannot be supplied. However, README's “No other note is needed”
and RESULT's complete-proof claim are not met. The word-RAM primitives and
tiny-label Gaussian-RMS inequality should also be imported explicitly.
The current source notes were inspected selectively; the entire transitive
finite-implementation chain was not freshly reconstructed in this audit.

### Localized corrections

| ID | Location in RESULT | Required correction |
|---|---|---|
| L1 | 87–93, 122–123, 189–198 | Add `m >= 2` and positive labels to claims of error negligible relative to actual dense variability. The detailed ratio theorem already does so. With one sample and a nonzero constant final activation, dense variability can be exactly zero (5927–5945). |
| L2 | 101–104, 156–160, 195–196 | Replace equality of learned and total retained state by a common asymptotic upper bound. Harmonic fixed metrics, data and caches are additional to the exact moving count at 2529–2550; decoder seeds and metrics are likewise not all evolving coordinates. |
| L3 | 295–301, 320–323, 978–1039 | Scope the shared setup correctly. Logarithmic uses an independent reference and spanning inputs; it is not covered by the unrestricted-input/shared-initialization wording. Extend the joint-confidence recipe if all five assertions, including dense lower, are claimed together. Do not impose decoder restrictions on the original methods. |
| L4 | 892–896, 941–944, 1032–1039 | Restrict real-coordinate, exact-real arithmetic and “no precision/training-step bound” disclaimers to the original models. Logarithmic uses finite words and a complete prescribed training schedule. |
| L5 | 189–198, 901–903 | Do not suppress all decoder structural factors in a table that exposes them for the other methods without saying so. Do not call its logarithmic exponent always smallest: at permitted dimension one, Harmonic's displayed coordinate exponent is five, versus six plus log-log for the decoder, in different storage units. |
| L6 | 12–17, 2652–2687, 2701 | Replace the claim that generic constants occur only in headlines. The detailed decoder retains universal constants and inherited structural leading coefficients; it is parameter-explicit, not numerically instantiated throughout. |
| L7 | 6557–6563 | The displayed factors give the sixth power directly, not the fifth followed by the sixth. Correct the intermediate multiplication; the final Legendre certificate is unchanged. |
| L8 | 2371, 2659, 2673, 2682, 8073–8077 | Only the two all-time Harmonic bounds include the endpoint. Restore the three missing backslashes before `qquad`. Give the median ensemble a lower bound, not just an upper bound: the smallest odd integer at least `log_2(16 N_ext / delta)` suffices for the displayed union estimate. |
| L9 | 4448–4453 | Display the source-to-observable contractions leading to (S.15), including the vanishing residual-gradient trace. A second reconstruction recovers the stated coefficients; this local omission does not require changing them. |

The confidence correction in L3 can simply allocate failure input
`delta/5` to each of dense upper, dense lower, Legendre, Harmonic and
Logarithmic when all are asserted, and retain the union of their width
conditions. It changes no standalone theorem.

## 5. Questions for the authors

1. Can the source insertion identity and complete trace/remainder ledger be
   written out so that (S.15) follows without an undescribed graph expansion?
2. Should the Logarithmic section import its finite construction in full, or
   explicitly present itself as a theorem composed from identified lemmas?
3. Should “learned state” mean evolving coordinates consistently, with fixed
   compression metadata reported separately, or should the headline use the
   more accurate phrase “retained model” for Harmonic and Logarithmic?

These are follow-up decisions, not assumptions adopted by this audit.

## 6. Reproducibility and code

The existing mechanical checker, deterministic cost-algebra checks, and all
five exact decoder-kernel tests pass. See [code_audit.md](code_audit.md).
They do not verify the probability theorems. The mechanical checker in
particular passes despite the three malformed `qquad` commands.
No end-to-end neural run, timing benchmark or full mathematical render was
performed.

## 7. Limitations and ethical considerations

This is an author-authorized internal research audit, not a confidential
conference submission or promotion review. No data, external service or
maintained scientific book was changed. Qualitative widths, fixed-parameter
asymptotics, real-word versus finite-word costs, offline setup, and the lack
of a practical timing guarantee remain material limitations.

## 8. Overall scientific assessment

The core conditional mechanisms and resource arithmetic remain supported.
The available evidence does **not** justify saying every result is fully
closed and self-contained. Resolve M1 and M2, then apply the localized
corrections before labeling the integration fully audited. This assessment
does not retract the headline rates or claim a counterexample to them.

## 9. Confidence and verification coverage

High confidence in the identified interface errors, local arithmetic
corrections, resource substitutions and test outcomes. Moderate confidence
in the conditional downstream proof reconstructions. No unconditional
soundness verdict for the source-dependent theorem chain. Every section of
RESULT was read across the lead and three scoped reviewers; full reading is
not equivalent to formal verification or complete reconstruction of every
external dependency. Historical PASS reports were not substituted for fresh
checks.
