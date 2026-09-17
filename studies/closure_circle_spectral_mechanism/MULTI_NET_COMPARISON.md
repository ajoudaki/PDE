# Actual networks on all six three-/four-point circle cases

The new 48-network campaign shows that N3 is closer than N1 in every tested
case. N5 further reduces the error in three cases and increases the measured
error in the other three. This ordering agrees at widths 1024 and 4096. The
four-point 30° case passes the full available numerical-control improvement
checks for both order transitions. Other cases retain missing or failed
closure quadrature qualifications; the experiment does not establish general
convergence with closure order.

All 48 runs trained the actual dense, bias-free, two-hidden-layer tanh network
from the frozen plan: six geometries × two widths × three seeds, plus six
same-seed half-step and six float 64 controls. Every run reached the fixed
physical T120 and met the mild finite settling diagnostic. No clock, gain,
phase, template, or off-training teacher labels were fitted for comparison.

## Primary comparison at common physical T100

The reference is the pointwise mean of the three width 4096 network outputs
at T100. Each closure is also evaluated at T100, on the exact aligned 720-angle
subset. Relative RMS is RMS(closure − reference) / RMS(reference), so the
table measures agreement with actual networks across the circle. It is not
prediction error against a known off-training target function.

| Case | N1 error | N3 error | N5 error | Smallest measured error | Mean reference RMS | Network seed SD / mean RMS |
|---|---:|---:|---:|---|---:|---:|
| Three points, spacing 20° | 23.68% | 10.95% | 7.18% | N5 | 0.95430 | 1.56% |
| Three points, spacing 40° | 33.29% | 3.97% | 4.69% | N3 | 0.82106 | 0.81% |
| Three points, spacing 60° | 13.67% | 4.81% | 7.26% | N3 | 0.77760 | 0.89% |
| Four points, spacing 15° | 46.46% | 32.12% | 21.79% | N5 | 1.30647 | 0.85% |
| Four points, spacing 30° | 7.46% | 3.89% | 2.08% | N5 | 1.16652 | 0.19% |
| Four points, spacing 45° | 9.04% | 3.02% | 3.14% | N3 | 0.89485 | 0.35% |

Seed SD is the circle RMS of the pointwise sample standard deviation across
the three networks. The estimated mean standard error is that quantity
divided by sqrt(3); neither quantity bounds infinite-width bias.

The width 1024 comparisons are:

| Case | N1 error | N3 error | N5 error | Width 1024→4096 network-mean drift |
|---|---:|---:|---:|---:|
| Three points, spacing 20° | 23.57% | 10.87% | 7.21% | 0.37% |
| Three points, spacing 40° | 33.78% | 4.08% | 4.38% | 0.61% |
| Three points, spacing 60° | 13.98% | 4.93% | 7.25% | 0.47% |
| Four points, spacing 15° | 46.39% | 32.07% | 21.74% | 0.65% |
| Four points, spacing 30° | 8.50% | 4.92% | 2.91% | 1.09% |
| Four points, spacing 45° | 9.37% | 3.24% | 3.36% | 0.49% |

Each width 1024 error uses its own three-seed network mean as the reference.
Width drift uses the width 4096 mean as denominator; seeds carrying the same
number at different widths are not asserted to be paired network samples.
The four-point 15° N5 error remains 21.79% at width 4096 despite its substantial
improvement over the lower orders.

## Order changes and numerical qualifications

The frozen gain discriminator uses each seed's squared circle error. A
resolved improvement requires at least 10% reduction of its three-seed mean,
a paired mean gain exceeding twice its seed standard error and twice the
measured numerical effects, and passing numerical controls. The seed
dispersion contribution is the same for every closure order, but is retained
in this paired squared-error test.

| Case, width 4096 | N1→N3 mean squared error | N3→N5 mean squared error | Interpretation |
|---|---|---|---|
| Three points, spacing 20° | 78.4% reduction | 56.2% reduction | Both gain tests pass; matched closure controls missing |
| Three points, spacing 40° | 98.5% reduction | 38.5% increase | N5 deterioration measured; closure quadrature fails |
| Three points, spacing 60° | 87.4% reduction | 125.2% increase | N5 deterioration measured; matched closure controls missing |
| Four points, spacing 15° | 52.2% reduction | 53.9% reduction | Both gain tests pass; matched closure controls missing |
| Four points, spacing 30° | 72.8% reduction | 71.2% reduction | Both improvements pass all available control checks |
| Four points, spacing 45° | 88.7% reduction | 8.1% increase | Small N5 deterioration measured; matched closure controls missing |

“Measured deterioration” describes these saved numerical witnesses; it is not
a claim of robust deterioration after resolving missing closure controls.
Detailed gains, standard errors, individual-seed changes, and control effects
are preserved in the analysis summary.

The largest same-case network half-step/precision discrepancy is 0.00802%
relative RMS, below the 0.2% gate. Half-step controls use width 4096 and
precision controls width 1024, both seed 1729; both control axes were not run at
both widths. The 1440-versus 720 relative bandwidth discrepancy is at most
1.34e-8, below its 0.005 gate.

Existing closure quadrature/step controls cover only the three-point 40° and
four-point 30° geometries. Doubling quadrature at three-point 40° changes N1 by
4.18%, N3 by 1.51%, and N5 by 2.57%: N1 and N5 fail the 2% tolerance. The
four-point 30° quadrature changes are 0.50–0.53% and pass. The other four
geometries have no matched closure controls. No fresh high-precision closure
campaign was requested; missing control effects remain unknown rather than
being treated as zero.

## Secondary endpoints and verification

Secondary comparisons use the exact 1440-angle network T120 outputs against
each closure's saved mildly settled endpoint at T100–120. They are explicitly
different clocks when a closure stopped at T100. All six width 4096 endpoint
error triples round to the same two-decimal percentages as the primary table.
The largest network T100→120 relative RMS drift across all 48 runs is 0.000237%.
The largest T100 training MSE is 1.15e-9; every run satisfies the T120 settling
diagnostic, which is not a proof of an infinite-time limit.

Independent verification passed for all 48 configurations and all 48 retained
parameter sets. It checks frozen manifest/source/input/output digests, exact
case identity, independently regenerated seeded initialization digests,
parameter shapes/dtypes/finiteness, reconstructed losses, recorded loss
monotonicity, clocks, Gram symmetry/PSD, oddness, and settling flags. Direct
NumPy float 64 equations replay every final network at the fixed dense-grid
indices 0,10,…,1430 and its training angles. Maximum circle replay error is
3.806e-7, maximum training-angle replay error 1.269e-7, and maximum oddness
discrepancy 2.385e-7; all pass the dtype-specific tolerances. This audits saved
endpoints and observations without rerunning training or independently
replaying the unretained T100 parameter states.

Analysis used 0.818 CPU seconds and verification 9.015 CPU seconds, each within
its 180-second limit with one BLAS thread. The fixed 48-run training campaign
completed in 212.766 wall seconds.

Reproducible outputs are under
`data/generated/closure_circle_spectral_mechanism/network_comparison_multi_001/`:

- `analysis_final/summary.json`: per-seed and mean-reference RMS/max/shape
  errors, both clocks, seed/width uncertainty, paired gains and control effects.
- `analysis_final/curves.npz`: unmodified closure/network curves and means/SDs.
- `verification_final/verification.json` and `independent_replay.npz`:
  individual checks, exact replay indices, predictions and provenance.

Frozen manifest SHA256:
`b60d905b3a1fda224a8ec708b5e02dcf5b6edea841ba2f99a68041f146263426`.
Analyzer SHA256:
`abb679c71905ae55cc418603bf2ec47c7c4e21e31958d3b461278a18f3361ce3`.
Verifier SHA256:
`116ca26e072b6ceb1db0b3808dddde2d80f25b9eb8afb9a8fc1258047cd3de2a`.

This study-owned empirical evidence leaves the established algebra unchanged
and makes no theorem claim as network width, closure order, or time increases.
