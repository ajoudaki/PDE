# Author validation, 2026-09-17

Author: the current primary Codex agent. No delegated or independent reviewer.
Status: internally checked; not promoted. Shared HEAD at start and completion
checks: 379ede09d8bcc53a8efedfac53672e3d0711ade2. The shared index was empty at
startup; unrelated tracked and untracked work was preserved.

## Analytical checks

Read the complete proof in exact_reduction.md after writing it and checked:

- The p=1 tanh-core dictionary, eta=1/4096, inverse-lower-Cholesky
  normalization, raw response term tau*gamma, and right transpose against
  docs/observable_p1.md and C.4.7.10.B's initialized contraction derivation.
- Constant-coordinate removal by independent population sign symmetries;
  arbitrary data need not share these symmetries. Canonical initialized
  paths are included, but arbitrary supplied states need not be.
- Kernel reduction by substituting the original c velocity. The derivative
  at a moving v includes grad F dot v_dot. Derivative kernel sections lie
  in the declared closed feature span, so invisible readout components do
  not affect reverse contractions. The map is isometric on the initialized
  readout's space and retains restart information.
- Independent gradient-block derivation of all three terms in Kfull,
  retaining both M and M^T and the population-L2/Frobenius metric.
- Initial accelerations by differentiating the vector field and separately
  as twice the hidden-metric gradient of the label-weighted feature norm.
- Infinite kernel rank through the nonzero odd tanh coefficients and the
  Vandermonde determinant; its limitation is to a universal finite linear
  feature span, not every possible nonlinear or data-specific reduction.
- Time analyticity using uniform complex strips, an explicit bounded
  complex Banach ball, Cauchy's derivative bound, and a contracting Picard
  map. The unbounded real g is an affine base field, not an L-infinity
  variable. No Gaussian product algebra or infinite neural Taylor series
  is assumed. The bound gives local expansions, not a globally convergent
  series centered at zero.
- Coincident inputs, antipodal inputs, zero or contradictory labels, zero
  training weights, and degenerate kernel Grams: no step divides by any
  input Gram or training kernel eigenvalue. A vanished initial hidden
  acceleration is permitted. Kernel information alone is not asserted to
  determine the lower gated tensors.

## Deterministic execution

Before execution, the checker declared a 30-second, one-thread, 256-MB cap
and stopping at the first failed assertion. No training experiment, parameter
search, quadrature-accuracy estimate, or monotonicity experiment was run.

From /home/amir/Codes/PDE:

```bash
mkdir -p data/generated/closure_gaussian_reduction_p1_20260917/check_01
ulimit -v 262144
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 30s python studies/closure_gaussian_reduction_p1_20260917/check_reduction.py > data/generated/closure_gaussian_reduction_p1_20260917/check_01/check.json
```

Environment: Python 3.10.12, NumPy 1.26.4, float64. Deterministic 7-node
Gauss--Hermite tensor rules; lower four-dimensional carrier and upper
two-dimensional carrier remain separate. Three nonsymmetric input angles
(0.17,1.08,2.43), labels (+1,-1,+1), weights (0.2,0.5,0.3); a supplied
odd noninitial lower field, a full off-diagonal M, and a three-section upper
readout test the positive-time algebra without claiming a reached state.

Observed: exit 0, PASS, tool wall time approximately 0.034 seconds.
Dictionary/initialization checks agreed within 7.55e-15. Direct versus
reduced drift and contraction identities agreed within 1.67e-16.
The independent centered prediction derivative differed by 8.69e-12;
the independent directional check of the initial acceleration identity
differed by 6.95e-13. Declared tolerances were 2e-11 times max(1,scale)
for identities and 2e-8 for centered derivative checks.

The full output is in
../../data/generated/closure_gaussian_reduction_p1_20260917/check_01/check.json.
All comparisons use the same finite integration rule. They check algebra
and implementation signs; they do not certify Gaussian quadrature error,
the infinite-dimensional theorems, or long-time numerical accuracy.

## Provenance and limits

manifest.sha256 records the shared instructions, scientific inputs, this
study's proof/checker/README/validation, and the actual check output. No
other study's scientific content was read. No established files were edited.
The analytical results remain author-checked pending any separate promotion
process. No finite scalar closure or convergence-to-fitting conclusion is
claimed.
