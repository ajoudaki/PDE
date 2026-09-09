# Research state

2026-09-08. Current status: broad-class perturbative extension proved
and independently reviewed; practical-amplitude global theorem open.
See [RESULT.md](RESULT.md) and [REVIEW_STATUS.md](REVIEW_STATUS.md).

| Route | Mechanism | Deliverable | Status |
| --- | --- | --- | --- |
| Shape obligations | Typed sample symmetry, direct raw moments, bounded first two derivatives, compact Gaussian regression interval | Theorems A/B for linearly growing C2 shapes, without oddness | Proved; three independent PASS reviews |
| Quantitative constants | Existing response powers 19+12 and intrinsic scale M=O(delta^(-1/8)) | Universal sufficient c_dyn delta^(31/8); log10(c_dyn) approximately -230954.3591 | Proved; sufficient, neither practical nor sharp |
| Affine positivity | Independent Gaussian source groups and entrywise positive covariance bound actual response rows | Algebraic affine certificate without the old exponential propagator estimate | Conditional affine lemma proved; improved nonlinear closure provisional |
| Bounded activation | Physical loss feedback bounds the readout and learned reverse memories pointwise | Isolate the uncontrolled tails to reused initial Gaussian adjoints | Bounds proved on existing trajectories; global population construction open |
| Scale and margin audit | Independent-copy variance inequalities | Distribution-independent bound on relative nonlinearity | Proved; increasing affine gain does not resolve the practical issue |
| Moderate sine design | Gaussian orthogonalization and variance calibration | Unit initialized variance, approximately 6.4 percent nonlinear fraction, correlation contraction, top Gram at least delta | Initialization theorem proved; global trained theorem open |

Existing state recovered from mathematical sources:

- The earlier separated-angle result uses 1+z+e atan(z) and a small
  separation-dependent coefficient.
- Later odd-family sources prove a sufficient c_poly delta^4 rule, with
  a very small tracked prefactor. Polynomial dependence alone does not
  establish practical coefficients.
- Later large-gain C_b^2 shape results cover broad classes and permit e=1,
  but their relative nonlinearity remains small under the given gain rule.
- A separate practical-limit assessment records the moderate-activation
  canonical population identification as open; energy does not supply
  strong compactness or control the curvature-times-incoming-field term.

These are locators and scope records. New proofs must discharge actual
source hypotheses rather than cite research-status assertions.

## Causal changes in the new proof

1. Sample exchange, with a readout sign for opposite labels, replaces
   activation oddness. Distinct forward/backward sample bases preserve
   the typed current-return identities.
2. A direct raw-moment estimate replaces the invalid intrinsic-scale
   inference involving division by the inactive sample variance.
3. Explicit value-growth estimates remove the bounded-shape hypothesis.
   The dynamics cutoff is uniform over the entire normalized shape class.
4. Delta-independent actual affine marginal variances replace
   arctangent-specific nonaffinity arguments by a compact Gaussian
   regression obligation. Nonaffinity is separate from global existence.
5. The old response proof supplies the complete source closure. The new
   affine positivity lemma is not substituted into that nonlinear proof
   without the missing estimates.

## Remaining obligation

For a moderate coefficient, establish compact-time stability and tail
control for the actual source fields under physical loss feedback,
retaining their causal dependence on the reused Gaussian matrices.
Energy and bounded inputs alone are insufficient for this step, as the
adaptive-query counterexample shows. That example is not a counterexample
to neural gradient flow. No necessity of microscopic coefficients has
been proved.

All new mathematical files and their dependencies are frozen by the
manifests. No training experiment was performed. The three final reviews
found no required repair; their reports and version record are linked
from REVIEW_STATUS.md.
