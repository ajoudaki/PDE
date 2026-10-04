# Deterministic assessment before another exponent campaign

2026-10-04. Continuation requested by the user: use the new error-prefactor
theorem and completed multi-dataset tests to determine how to scale the
compressed representation with less trial and error, and whether a practical
optimal logarithmic exponent is identifiable.

This first bounded stage performs no new scientific training or neuron
selection. It reads only the theorem sources and this study's archived
configurations, source singular values and prediction measurements. Its two
calculations are (1) converged Gaussian quadrature of the theorem's initialized
feature covariance and (2) exact tail arithmetic for the archived finite
source matrices. A source-rank diagnostic is not a prediction certificate.

Compute Q^(0)=U U^T and the two tanh covariance updates using deterministic
product Gauss--Hermite quadrature. Use orders 64,128,256. The symmetric
two-Gaussian representation handles correlation endpoints. Check symmetry,
equal diagonals and positive semidefiniteness numerically; compare final gaps
at the last two orders and require relative change below 1e-4 and covariance
entry change below 1e-7 before quoting their digits. If this fails, preserve
the values as unresolved rather than tuning orders. Report Y/(gamma/m), the
relevant theorem's label-to-gap ratio, and distinguish this numerical check
from a rigorous quadrature error certificate. These ratios do not determine
the unknown structural smallness constant c.

For each valid baseline witness, read the singular values of the weighted
source remainder after projecting out the complete training-priority space.
The sampler's group normalization gives squared source Frobenius norm
n times the sum of squared nonempty group weights. For relative source
Frobenius targets .1,.03,.01, and 1/sqrt(n), compute the minimum number of
extra singular directions whose discarded squared singular-value sum is
below target^2 times that known norm. Verify that no resolved priority
direction was omitted in the archived computation. This optimum is only
within the fixed-priority linear approximation problem on the finite
initial source list; it is not an optimum over autonomous predictors.

Use all 70 successfully constructed baseline witnesses; preserve the two
missing witnesses as missing. Pool medians only descriptively. Fit no law to
successful-state minima: the old budget is a supplied schedule, not an
observed minimum. Do not interpret the fixed 32-probe source list as a
uniform-sphere source theorem. Its finite column count itself eventually
limits any inferred rank growth.

Hard limit: 120 seconds process CPU and 120 seconds wall for the analysis,
single BLAS thread, no GPU training or modified sampler. Fresh generated root
`data/generated/closure_sampling_20261003/practical_exponent_assessment_20261004/`.
Retain source/config hashes, quadrature results, all rank rows and exact command.
Stop after this diagnostic stage. Any subsequent new training campaign needs
a separate predeclared decision test, numerical gates and bounded budget;
the completed earlier campaign is not reopened by this calculation.
