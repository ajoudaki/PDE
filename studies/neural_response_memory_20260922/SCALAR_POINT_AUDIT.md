# Passive-point scalar implementation: scoped algebra audit

2026-09-25. Collaborative implementation audit by `/root/point_audit`.
This is not an independent promotion review or an accuracy certification.
Inputs were restricted to scalar_fourier_engine.py, scalar_fourier_reference.py,
the preceding scalar implementation report and audit, the frozen
SCALAR_POINT_PROTOCOL.md and the new scalar_point_engine.py. No other study
was used. The direct physical oracle in check_scalar_point.py is newly written
from the P=1 response equations rather than calling the reference solver.

## Verdict and checked construction

**PASS for the specified passive-point construction and its K=5 algebra.**
The implementation adds response species for one fixed input to the ordinary
connected-tree hierarchy. Training and passive output roots both have grade 3.
The passive input has no residual, loss weight or history source. The number
of training inputs remains M=2 in all gradient factors and in the RMS residual
clock. There is no Fourier block, angular quadrature or angle grading.

The runtime evolves scalar coordinates using fixed coefficient tables only.
Neuron arrays and initialized matrices are used during initialization. The
cutoff is the same unsaturated whole-monomial deletion rule as the preceding
experiment. Passing the algebra checks does not make its discarded terms small
or transfer the separate saturated hierarchy's convergence theorem to this run.

## Executed checks

Command, from the repository root:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/neural_response_memory_20260922/check_scalar_point.py --output data/generated/neural_response_memory_20260922/scalar_point01/algebra_checks.json
```

The complete check used 27.08 CPU seconds, below the separate 120-second audit
budget. Two dictionaries were compiled: the 60-degree passive point and the
same point placed at the first training input, 10 degrees. Both have 524
ordinary scalar coordinates plus the clock, including 331 training-only
patterns and 193 passive patterns, and 271606 retained equation terms.

The direct oracle uses width 5, nonzero A and B histories, L=1.7 and nonzero
readout weights. It differentiates both reconstructed internal matrices,
including the inverse-clock-length derivative, then propagates physical
velocities through all three hidden layers at the training and passive inputs.
Thus the checks include terms that vanish at initialization.

| Check | Maximum absolute discrepancy |
|---|---:|
| All 18 exact primitive templates versus direct oracle | 2.09e-15 |
| All compiled scalar rows versus direct monomial arithmetic | 0 |
| Complete output product rules versus direct physical derivative | 2.06e-15 |
| Independently retained output rules versus compiled output rows | 2.23e-16 |
| Initial passive output versus directly initialized network | 1.74e-18 |
| Training cone after arbitrary passive-coordinate perturbation | 0 |
| Entire scalar velocity at zero training residual | 0 |
| Runtime after removing diagrams, templates and physical inputs | 0 |
| All 193 duplicate-point rows after sample-label substitution | 0 |
| Duplicate-point initial output versus training-output coordinate | 0 |

For the output-rule check, each product-rule term was independently merged,
its disconnected scalar factors evaluated on neuron fields, and the same
whole-term cutoff criterion applied without calling the row compiler. At the
generic checked state, 7046 omitted terms in each training-output equation and
8214 in the passive-output equation are individually nonzero. Their existence
is expected and cautions against treating a small retained dictionary as exact
feature learning.

Training-cone independence is also checked structurally: every retained row
without passive fields depends only on coordinates without passive fields,
and its drive is a training residual or the training clock. The direct
perturbation test confirms this after table packing. The separate matched
training-only integration specified by the protocol remains the root runner's
causal control, not a second fitting campaign run by this auditor.

## Why the duplicate-input identity matters

Replacing every passive activation species by the first training activation
species maps each passive pattern to an existing training-only pattern. When
the two input vectors agree, the 193 corresponding polynomial rows agree
exactly after collecting factors, and the initialized coordinates agree. On
any interval on which the scalar ODE exists, uniqueness therefore preserves
these equalities. In particular, the passive prediction at a duplicate training
input equals that training-output coordinate throughout the evolution, apart
from numerical integration error.

This fixes the structural unequal-grading issue in the preceding Fourier
prototype. It provides a consistency check at identical inputs; it is not an
accuracy theorem at the distinct 60-degree input. Agreement with dense training
there, numerical refinement, and resource-limited higher cutoffs are empirical
obligations of the preregistered experiment.

## Checked source versions

| File | SHA256 |
|---|---|
| scalar_fourier_engine.py | e7c117bc0d2a47742fc5758faba457d4f8582e0020a8afa2a346bac7a6195b4d |
| scalar_point_engine.py | 2674f8fd664b5d6654a50988a5c28d8753f19efdf24c20c0ffe1785e51cad394 |
| check_scalar_point.py | a12529c17ca241748e6a6a866bd07d68fd1aa794db697e7aea2314be35b1a687 |

The checker refuses an existing evidence path before executing, to preserve
recorded checks. Changes to template, cutoff, initialization or table logic
require the affected checks to be replayed. Solver tolerances and empirical
accuracy are outside this algebra verdict.
