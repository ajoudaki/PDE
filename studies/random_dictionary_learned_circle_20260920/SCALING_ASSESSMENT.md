# Error versus dictionary budget: assessment and next discriminator

2026-09-20. Continuation of this study, following the user's request to
understand an increasing approximation-efficiency advantage over Gaussian and
orthogonal dictionaries. This is a post hoc assessment of the completed runs
and a proposed follow-up, not a new training experiment or a proven rate.
No new training runs were launched for this assessment.

## Target

For a fixed dataset S, width n and network initialization, compare the circle
RMS discrepancy E_M(K1,K2;S) between method M's fitted predictor and the same
full network's fitted predictor, each at its own first MSE1e-3 crossing.
Retain maximum absolute error as a second observable. Along one declared
nested dictionary schedule, study the smallest tested budget K1+K2 achieving
a common error tolerance epsilon. The important question is whether the
random/observable budget ratio increases as epsilon decreases, rather than
whether one equal-budget error ratio is merely greater than one.

Budget pairs, K1*K2 coefficient counts, effective ranks, conditioning and actual
runtime must accompany total feature counts. A dictionary-item ratio is not a
ratio of complete model state or computational cost: full first rows/readout
still evolve. Nonmonotonicity precludes claiming that every untested smaller
budget fails merely because a larger tested budget fails.

## Current evidence

All entries below use saved reported-primary RMS values; `refined_ratio` in
the reproduction snippet provides the tighter-level check. The ratio uses the
better of the two random controls in each cell, so it is a descriptive
best-control envelope, not a distribution over random seeds.

| Configuration | p | Ours RMS | Gaussian RMS | Orthogonal RMS | Better-random / ours | Refined ratio | All three comparisons pass |
|---|---:|---:|---:|---:|---:|---:|---|
| quadrant_pairs | 1 | 0.28505 | 0.65802 | 0.63253 | 2.219 | 2.216 | True |
| quadrant_pairs | 3 | 0.16563 | 0.55031 | 0.59815 | 3.322 | 3.330 | True |
| quadrant_pairs | 5 | 0.09425 | 0.48733 | 0.45519 | 4.830 | 4.831 | True |
| two_outliers_alternating | 1 | 1.03824 | 1.56292 | 1.58670 | 1.505 | 1.506 | True |
| two_outliers_alternating | 3 | 0.54986 | 1.37997 | 1.30339 | 2.370 | 2.370 | True |
| two_outliers_alternating | 5 | 0.37820 | 1.20440 | 1.17742 | 3.113 | 3.083 | True |
| quadrant_alternating | 1 | 2.28517 | 2.95928 | 2.89593 | 1.267 | 1.269 | False |
| quadrant_alternating | 3 | 1.28976 | 2.46012 | 2.47847 | 1.907 | 1.910 | True |
| quadrant_alternating | 5 | 1.11331 | 2.33100 | 2.33753 | 2.094 | 2.091 | False |
| quadrant_center_edges | 1 | 0.60507 | 0.53704 | 0.53034 | 0.876 | 0.878 | True |
| quadrant_center_edges | 3 | 0.47105 | 0.51159 | 0.50260 | 1.067 | 1.066 | True |
| quadrant_center_edges | 5 | 0.15835 | 0.27208 | 0.47560 | 1.718 | 1.708 | True |

On both `quadrant_pairs` and `two_outliers_alternating`, ours at(5,3)
already beats both random controls at(128,21). These are8 versus149 dictionary
items, not a proved18.6-fold minimal-budget lower bound or an18.6-fold speedup.
The RMS advantage grows at all three measured orders in these two cases and
is stable under the saved refinement checks. The strictest alternating arc
is harder in absolute terms but has a weaker growing separation and two
unresolved numerical cells. It should not automatically be the main test.

The full12-case table and contrary evidence remain authoritative: random
controls outperform ours at all three orders on the regular and nearly
regular grouped-label circles. No whole-suite universal dominance is inferred.
Three orders at one initialization cannot distinguish a transient improvement
from a persistent rate difference or later error floor. There is no
numerical or mathematical guarantee of an asymptotic rate here.

## Proposed smallest next discriminator

1. Extend the existing paired-cluster and alternating-with-outlier curves,
   keeping all dynamics, initialization conventions and threshold unchanged.
   Add p6 and p7, with p8/p9 a conditional extension if numerical validity and
   conditioning permit. Match both population counts for every method. Freeze
   genuinely nested random columns; increasing the current maximal random draw
   shape silently changes old prefixes, so do not splice those into old curves.
2. If the advantage continues increasing, confirm on a small predeclared family
   of nearby arc widths, angular offsets/jitter and outlier positions, using
   fresh paired network and random-dictionary seeds. The current cases are
   discovery data, not independent confirmation. Retain an easy grouped-label
   case where random controls worked well as a negative control.
3. Report error versus actual features, and tested features required for common
   accuracy thresholds, for both norms. Separate Gaussian and orthogonal curves;
   use orthogonal as the main span comparison because Gaussian frame conditioning
   changes with budget. Do not repair a poor control with future-trajectory data.
4. Before interpreting an apparent rate, verify the useful error range exceeds
   integration/grid uncertainty, avoid a window chosen after seeing the curves,
   and check whether the advantage survives at a second width with the same
   budgets. At fixed n the orthogonal family has finite rank and ultimately
   spans the carrier; the question concerns a useful sub-full-rank range and,
   for a population claim, a separately specified growing-width limit.

This is a design recommendation, not an authorized unbounded campaign. A fresh
bounded run plan must specify exact cases, seeds, numerical gates, training
budget and stop branches before execution. The completed phase2 budget is closed.

## Mechanism and implementation qualifications

Many alternating labels and large unobserved arcs are sensible stresses. They
force a complicated fitted input-output map but do not prove a high-rank
middle-layer update: first-layer weights and readout train, and initialization
already supplies a full matrix. If needed, use the saved full-network states
to measure how much relevant forward/backward action each fixed dictionary
misses. Such an analysis is diagnostic only; never refit the dictionaries to
those trajectories or substitute a fitted surrogate as a control.

The maintained schedule in code/pde/observable_initialization.py has polynomial
core counts binom(p+4,4) and binom(p+2,2), plus explicitly retained word tails.
Exact counts are p5:(128,21), p6:(213,28), p7:(333,36), p8:(499,45),
p9:(720,55), p12:(1826,92), p13:(2386,107). Thus p9 already uses35.2% of
n2048 in its lower dictionary; p13 cannot have a matching orthogonal frame.
Conditioning at the unrun larger orders remains unmeasured.

Through the proposed p6–p9 window the extension refines polynomials of the
same four lower/two upper initialized coordinates; it does not add independent
new action queries. The exhaustive word tail provides completeness eventually,
but its enumeration is much slower than polynomial growth. A polynomial-window
error floor would not alone refute the full hierarchy. Conversely, an observed
polynomial-window gain cannot establish the full hierarchy's asymptotic rate.
The ridge schedule also varies with p, so empirical curves describe the actual
combined dictionary/regularization construction, not span enlargement alone.

Independent random spans do not use W2(0), whereas the observable dictionary
explicitly uses initialization actions. A growing advantage may reflect useful
retention of this information; it is not automatically evidence of high-rank
nonlinear training. These are compatible interpretations of dictionary utility
that a mechanism diagnostic can distinguish.

## Evidence and reproduction

Read `diverse_analysis01/metrics.json`, `selected_levels.json` and
`validation.json` in this study's generated namespace. For each named case
and order, select `ours_p<p>`, `gaussian_p<p>`, `orthogonal_p<p>` and compute
`min(gaussian['l2'], orthogonal['l2']) / ours['l2']`; repeat with `refined_l2`.
No network simulation or new empirical sample is involved in these reductions.
The existing full tables, independent2496-check audit and limitations remain
unchanged. This assessment introduces no new theorem or promoted result.

Scoped assistance: a prompt-only design challenger assessed mechanisms and
asymptotic interpretation; a separate reader checked the maintained dictionary
construction and this study's initialization code. Neither used other studies,
ran training, or supplied an independent review acceptance.
