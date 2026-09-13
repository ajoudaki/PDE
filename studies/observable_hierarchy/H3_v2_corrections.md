# Revised H3 internal corrections

Original sources and evidence are preserved. These are author checks, not
independent promotion verdicts.

## 2026-09-13: arithmetic conversion

The first arithmetic draft rounded public `real(Fraction(...))` at the ambient
Decimal precision if the caller had not entered its context. Public conversion
now enters its own context. Integer conversion also bypasses decimal string
conversion. The solver static test verifies an 80-digit third outside a context.
These corrections preceded all trajectories.

A rational fixed-point backend was added before trajectories so the arithmetic
refinement does not rely on Decimal's fixed library maximum precision. It uses
integer multiples of 10^-p, rounded basic operations and finite rational series.
Decimal remains a useful finite-range practical backend. The rational24 and
rational36 configurations exercise the alternative through initialization,
evolution, prediction, paired observations and restart.

## 2026-09-13: validation and memory accounting after the initial runs

Commit `bb78603` preserves the sources used by the twelve predeclared author
configurations in `H3_v2_author_validation_20260913`. All completed; each source
hash is retained in its record.

A code audit found that P rounded population weights could have aggregate
rounding error proportional to P, while the validation threshold was independent
of P. At some large P this could reject arbitrarily high precisions. Validation
now includes the coordinate count in its rounding allowance. This is a numerical
input check, not a mathematical probability relaxation: the limiting laws have
unit mass. Data validation also checks and preserves supplied probabilities,
instead of repeatedly normalizing them inside the vector field. This prevents
the input law itself from acquiring step-dependent rounding changes.

The first resulting static test failed because its synthetic rational-backend
data used binary floats .3 and .7 as supposedly exact probabilities; their exact
binary values do not sum to one. The fixture now declares those weights as exact
fractions. The seven-test suite then passed (0.074 seconds). No trajectory was
run during this correction. Every original trajectory used powers-of-two input
and population weights, which have exact representations in all three selected
backends; the correction does not change those weights.

Retained-array accounting initially counted a rational scalar object but not
its referenced numerator and scale integers. `state_bytes` now includes both
integer objects. Original operating-system peak RSS measurements remain valid;
the earlier rational retained-byte fields are incomplete and must not be quoted
as total retained storage. Reanalysis of exact restart files can recover the
corrected accounting without rerunning a trajectory.

The maintained word helper's floating envelope/scalar conversion was also
identified as an avoidable ceiling for the new hierarchy. A separate exact
initialized-word implementation is being prepared in this study, with identical
natural-number grammar and no established helper edits. Its correspondence and
integration checks must pass before the final candidate is frozen.

## 2026-09-13: matrix association

The resource audit found that Python's left association in `b2 @ M @ a`
formed a population-by-feature temporary and repeated more matrix work than
needed. The solver now computes `b2 @ (M @ a)`, and similarly groups the
reverse and frozen observation products. Exact equations are identical;
finite floating-point last bits may differ. This lowers the per-input-block
work from an unnecessary population-times-feature-product term to the
coefficient contraction followed by feature evaluation. The original measured
runs used the earlier association and remain labelled accordingly. Final
candidate performance and restart will be independently reproduced from the
frozen corrected producer, under a fresh finite reproduction plan.

## 2026-09-13: first standalone assembly

The first standalone edition passed all 46 deterministic tests. An assembly
audit found that its equation-reference rewriter also changed layer superscripts
such as `W^{(3)}` and the constant in `o_{P}(1)`. That draft and its manifest
remain preserved as edition v1; it was not sent for scientific review.
The assembler now excludes TeX-brace contexts from reference rewriting and
shifts all guide headings consistently. A portable budget supervisor and
canonical reproduction recipe are included before the next freeze.
