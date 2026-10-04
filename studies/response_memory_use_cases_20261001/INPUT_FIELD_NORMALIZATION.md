# Normalization reconciliation and fixed correction

The original input-field implementation divided circle rows by sqrt(2),
although the source `Flow` API already expects x/sqrt(d). The common study
circle convention has raw inputs x=sqrt(2)*(cos(theta),sin(theta)); its API
rows must be the unit vectors (cos(theta),sin(theta)).

With source first-layer entries N(0,1), the original API rows give
preactivation variance 1/2 at each fixed angle; canonical rows give variance
1. This is a model change, not an innocuous reformatting or an integration
error. All models within the original comparisons shared the smaller input
scale, so those comparisons remain valid for that explicitly labeled variant.
They do not establish the common canonical-model result.

Before the canonical rerun, exact original source/report/protocol/derivation
copies were saved as `*_INPUT_SCALED_V1.*`. Original generated directories
`input_field_deterministic`, `input_field_stream_pilot`,
`input_field_stream_confirmation`, `input_field_refinement`,
`input_field_checks`, `input_field_checks_restart`, and `input_field_analysis`
remain unchanged apart from supplemental normalization classification metadata.
Their exact run-time source snapshots also remain in each GPU run directory.

The amended protocol was written before implementation and rerun. It freezes
all 81 original configurations, seeds, controls, numerical refinements, and
teacher B/C5/q3 streaming choice, forbidding reselection from the corrected
pilots. The only dynamics change is `circle(theta)` returning unit API rows.
The CPU audit now explicitly checks both unit row norm and equivalence to raw
x/sqrt(d), in addition to indicator parity, projection identity, Euler
refinement and restartability. It passes 146 assertions with maximum error
6.66e-16 and short Euler difference ratio 2.0030.

Corrected evidence belongs to new `input_field_canonical_*` directories.
The main report now uses those canonical results and retains a direct
before/after normalization table. All 81 canonical fits completed and every
validity gate passed. Canonical median RMSE is 0.01802376 for field,
0.01219253 for dense, 0.38138953 for readout-only, 0.02054809 for
frozen-internal and 0.01014190 for rank15 factors. The field now improves on
frozen-internal training on all five seeds, with a 12.3% median reduction,
while factors still beat it on all five. This strengthens only the modest
internal-connection benefit; it does not establish competitiveness against
the stronger factor control. The route cap is explicitly extended to
180 cumulative fits (81 original + 81 corrected = 162), with its original
20 GPU-minute ceiling. No input from another route's research outcomes was
used to select a new task or parameter setting.
