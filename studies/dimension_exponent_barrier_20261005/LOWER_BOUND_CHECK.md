# Reconstruction of the lower-bound route

Reviewer: lead agent, after the independent route was frozen.
Date: 2026-10-05. Reviewed the complete 547-line LOWER_BOUND_ROUTE.md with
SHA256 700f8ae41847c7a847bab02eefc64a1622deec51505dee96ad19b9bb80a95feb.
This is an internal reconstruction, not promotion or a formal proof check.

## Scope and method

Read every line and reconstructed each displayed inequality from its stated
hypotheses. Compared the architecture, loss factor, normalization, initialization
override and mobility factors against docs/notation.qmd. The review uses this
study's contract, elementary algebra/probability and the complete route; no
other study or numerical experiment is an input. The external Lipschitz-width
paper is only context and is not needed by any proof.

## Findings

1. Finite-code packing: the triangle inequality and union bound give the stated
   2-epsilon separation and small-ball bounds. The independence qualification
   on public randomness is necessary and is present.
2. Bounded Lipschitz decoder: the cube endpoint grid has at most
   (2+2 R Lambda/epsilon)^p elements. Rounding adds epsilon to the original
   approximation, producing radius 2 epsilon, hence separation 4 epsilon.
   Degenerate R=0 and Lambda=0 are handled separately. These are restrictions
   on a representation class, not assumptions already established for all
   autonomous models.
3. Sphere polynomial dimension: polynomial division by the sphere equation
   preserves total degree. Evaluating the linear remainder at the two sphere
   heights gives the exact kernel and the binomial dimension formula, including
   degrees zero and one with the stated conventions.
4. Conditional reachable ball: normalized L2 projection is a contraction from
   the sphere supremum norm. The separated-set volume argument yields the
   displayed logarithmic packing. Taking k=floor(log(1/epsilon)/(2 alpha_d))
   gives radius at least sqrt(epsilon), and the explicit lower constant follows
   using k >= log(1/epsilon)/(4 alpha_d) and a remaining logarithmic factor at
   least log(1/epsilon)/4. The threshold qualifications are essential and present.
5. High probability is not inferred from the preceding worst-case inclusion.
   The separate small-ball requirement is explicitly unproved. This is the
   central missing bridge; no actual neural storage lower bound follows.
6. Tight fluctuations: a finite cover of a fixed-confidence compact set gives
   the positive n-independent lower bound on maximal small-ball mass at the
   normalized root-width scale. Centers need not have inexpensive descriptions;
   no positive autonomous construction is implied.
7. Actual initial derivatives: zero readout eliminates every initial hidden
   velocity. The readout mobility cancels its 1/n derivative factor. Substituting
   the readout velocity gives equation (12); differentiating once more yields
   equation (13), with factor -4/m^2. Terms involving hidden accelerations are
   multiplied by the zero readout at this order. Positive-time hidden dynamics
   are not frozen.
8. Sine example: the Gaussian cosine identity gives exp(-q) sinh(s). Conditional
   independence of rows and bounded sine give variance at most 1/n per layer.
   Continuity of the covariance formula yields only the stated finite-set
   convergence. Distinct non-antipodal training frequencies are linearly
   independent by restricting to a generic line and differentiating a finite
   exponential sum. This proves the claimed positive initial Gram without
   asserting a uniform gap, full-sphere rate or trained-flow closure.
9. Derivative-to-prediction transfer: two individual second-derivative bounds B
   yield remainder at most B t^2 in their difference. Optimizing t gives
   a^2/(4B), not a root-scale prediction lower bound. This limitation is correct.

## Outcome and limitations

PASS for the exact auxiliary and explicitly conditional propositions as stated.
The requested autonomous sublinear-exponent construction and high-probability
neural impossibility theorem remain OPEN. No whole-time neural central limit
theorem, normalized tightness, growing-dimensional Gaussian approximation,
reachable polynomial ball or efficient deterministic-center representation was
verified. The check supports the route's negative conclusion about what has
not been proved; it does not turn its sufficient hypotheses into facts.
