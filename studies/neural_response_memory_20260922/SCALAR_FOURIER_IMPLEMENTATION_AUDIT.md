# Scalar Fourier implementation: scoped algebra audit

2026-09-25. Scoped collaborative implementation audit by `/root/scalar_audit`.
This is not an independent promotion review. It checks the frozen protocol's
finite-width implementation, not its training accuracy or convergence rate.

Scientific inputs were restricted to the complete
SCALAR_CIRCLE_FUNCTION_READOUT.md, POPULATION_SCALAR_CONSTRUCTION_CHECK.md,
POPULATION_TO_AGGREGATES.md, SCALAR_COMPRESSION_BOUND_ASSESSMENT.md and
DEEP_CIRCLE_DERIVATION.md. The implementation assignment additionally authorized
SCALAR_FOURIER_EXPERIMENT_PROTOCOL.md, scalar_fourier_engine.py and
scalar_fourier_reference.py. No other study or scientific source was used.

## Verdict and implemented scope

**PASS for the checked algebra and finite-cutoff implementation.** The engine
implements the original activity-clock P=1, three-hidden-layer tanh hierarchy,
reachable training trees and shared-angle forests, and whole-monomial deletion.
It evolves global scalar contractions after initial preprocessing. Its Fourier
blocks are passive: training residuals use training-output coordinates only.
The tested implementation is the **unsaturated** reference truncation, as
declared in the frozen protocol. The arbitrary-finite-horizon convergence
theorem for the separately saturated construction does not certify this run.

The exact templates retain both orientations of each actual initialized matrix,
the derivative of the inverse history length, and forward propagation through
every evolving hidden layer. No dense or population trajectory forces the
scalar RHS. The source implements P=1 only, rather than a general P API.

## Executed checks

Command:

    python studies/neural_response_memory_20260922/check_scalar_fourier.py

Machine-readable evidence:

    data/generated/neural_response_memory_20260922/scalar_fourier01/algebra_checks.json

The complete recorded replay took 10.36 CPU seconds. Earlier incremental
development checks plus this replay stayed below the assigned 120 CPU-second
algebra budget. These are algebra checks; no training campaign was run by this
auditor.

The oracle at the beginning of check_scalar_fourier.py was independently coded
from the response-lift equations. Its generic states have nonzero A and B
histories, length L>1, nonzero readout, and nonsaturated activations. Thus the
checks exercise terms which vanish at initialization.

| Check | Observed maximum absolute discrepancy |
|---|---:|
| Reference versus independent P=1 primitive/physical/query derivatives | 5.56e-17 |
| Reconstructed physical velocity versus centered finite difference | 8.52e-11 |
| Initial dense versus population physical velocity | 6.94e-18 |
| All 18 exact compiler primitive templates versus independent oracle | 1.06e-15 |
| All compiled K=5 rows versus direct scalar monomial evaluation | 3.47e-17 |
| Independently rebuilt retained training/Fourier output rows | 2.23e-16 |
| Independently rebuilt complete output product rules | 1.95e-15 |
| Initialization, 256 versus 512 angular nodes, width 4 | 2.06e-16 |
| Forbidden even Fourier output modes and their initial velocities | 5.67e-17 |

The complete output product rules were rebuilt without calling the compiler's
row-generation method. Their component sizes were checked before evaluating
each entire term directly on neuron fields. This separately verified 7,046
omissions for each training-output row and 19,600 for the angular-output row.
No omitted factor was silently replaced by one.

Additional exact checks:

* The contraction with an initialized edge equals u-transpose W0 v/n.
* Two separate neuron factors sharing the angle give the integral of cos²,
  exactly 0.5 in the check; multiplying their separate angular means would
  instead give approximately 2.4e-33.
* Removing the compiler, diagrams, pattern maps and physical input array from
  a copied runtime object leaves its RHS identical. The initialization method
  retains neither its neuron arrays nor its angular nodes in the runtime.
* Setting training-output coordinates equal to the labels gives exactly zero
  velocity for every scalar, including the activity clock.
* Initialization at widths 4 and 7 produces identical state dimensions for
  the same dictionary. Width enters initialization values, not its type list.

The test uses K=5, J=2 for repeated-block checks; its state has 331 training
scalars, 17 angular patterns times five real weights, and one clock, totaling
417. The experiment's J=8 repeats precisely the same angular operator on 17
weights, giving 621 moving scalars. The K=5 dictionary contains 133,358
retained generator terms. These counts already caution against describing
this first witness as a demonstrated memory or speed improvement.

## Limitations relevant to interpretation

The minimum output grades, 3 for training and 5 for Fourier readout, do not
ensure faithful feature learning. At initialization, expansion of the complete
training backward Gram contractions R3, R2 and R1 needs grades through 7, 15
and 23 respectively. Their gate-constant branches first occur at grades 3, 7
and 11. A K=5 test consequently discards many nonzero feature terms even in
the first output derivative. Matching exact templates does not make those
discarded terms small.

The audit checks that the implemented approximation is the specified one.
It does not prove preservation of realizability, positivity, loss monotonicity,
or agreement between training-output scalars and evaluations of the approximate
Fourier function at training angles. Those are empirical diagnostics of the
resulting truncation. Integration refinement and the actual experiment-width
quadrature refinement remain the experiment runner's separate obligations.

## Checked versions

| File | SHA256 |
|---|---|
| scalar_fourier_engine.py | e7c117bc0d2a47742fc5758faba457d4f8582e0020a8afa2a346bac7a6195b4d |
| scalar_fourier_reference.py | cb94420dbac104e62afb01140cda3af6b11911ea30f25fa1eed0d9723593c671 |
| check_scalar_fourier.py | 7a36ad82f61558bbf46b0550663614cebe5ada67fce65436961b5405fcb876b3 |

Subsequent changes to scientific template, retention or evaluation logic need
the affected checks replayed. Solver-only changes require their numerical
checks rather than a new claim that this source hash was audited.

After this recorded algebra replay, the checker received an I/O-only change:
it refuses an existing output path before running any checks and creates its
evidence file exclusively. The refusal was verified against the existing
algebra_checks.json. No scientific, compilation, initialization or checking
logic changed; the hashes above continue to identify the recorded replay.
