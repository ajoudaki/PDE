# Proof dependencies of the activation-class theorem

The delivered [manuscript](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_activation_class/MANUSCRIPT.md) contains the complete generalized argument. It invokes no unproved nonclassical external theorem. It neither assumes an external activation-universality theorem nor infers the result merely from continuity of an existing theorem's statement.

## Specialized ingredients proved internally

| Obligation | Internal proof | Activation hypotheses checked |
| --- | --- | --- |
| Fixed adaptive Gaussian calculations, transpose responses, singular query Grams | Part F, F.1–F.23 | C¹ coordinate maps with bounded first derivatives; the activation and each fixed capped gate satisfy these bounds |
| Canonical common action spaces and genuine adjoints | Part F, F.24–F.28 | Fixed-program consistency, finite operator norm bounds, generated-space density |
| Strong chain rules and scalar prediction differentiability in the raw metric | Part F, F.29–F.45 | Bounded continuous first derivative, bounded second derivative, weighted scalar Taylor remainder |
| Controlled response bounds with constants independent of mesh, cap and input covariance | Part R, full finite chain through R.90 | Absolute bounds on ψ, ψ′ and ψ″; no parity or derivative-sign assumption |
| Uniform initialized feature coercivity, including singular input Gram | Part G, G.1–G.5a | Correct constant and linear Gaussian projections for nonodd ψ; positive affine slope dominates perturbation |
| Nonaffinity for localized and oscillatory shapes | Part G, G.6–G.8 | Positive distance from affine functions on one finite interval, Gaussian density lower bound, L² regression stability |
| A noncircular gain choice and global capped flow | Part G, G.9–G.27 | Explicit cubic gain selection and residual-clock slack |
| Global uncut flow, competitor uniqueness and continuation | Parts G and V | Uniform incoming reference tails and a cap comparison with one cap factor |
| Actual finite GF/raw GD, full true kernels, velocities, path laws and probes | Part V | Ordered fixed-transcript, mesh, width, cap and observation truncation limits |
| Derivative-valid initial backward observations | Part V.I | Bounded ψ′ and ψ″, ordered truncations and integrable derivative envelopes |
| Every hidden block and every sample/layer initial motion; kernel variation | Part N | Positive initialized feature and backward Grams, strictly positive full gate, nonzero ψ″ somewhere, explicit affine perturbation bounds |
| Uniform infinite-dimensional function classes | Part A | Elementary Hilbert-space projection-distance inequalities and bounded convergence |

## New analytic content and exact dependency changes

The Gaussian projection includes the generally nonzero mean of ψ. Its constant coefficient and linear coefficient are each bounded below by a/2. Three layers give the coercivity constant λ=δ²/256. The lower bound on the full activation derivative is also a/2; the backward positivity arguments use its square a²/4. The response and initial upper-perturbation constants retain their numerical values because the normalized absolute bounds are at least as strong as those used in their proofs.

For arbitrary bounded nonconstant C² shapes, a scale-uniform Gaussian regression margin is not assumed. A finite-interval residual gives Rψ(σG)≥cψ/σ for σ≥1; initialized standard deviations lie in [1,5a²]. Hence the permitted L² displacement is proportional to a⁻¹ while the controlled displacement bound is proportional to a⁻⁴. The displayed cubic gain condition closes this comparison before any training trajectory is used. Part A separately proves a uniform positive margin for an infinite-dimensional neighborhood, yielding a common recipe depending only on separation for that fixed class.

Three preparatory audits independently examined the source machinery, shape-dependent geometry/nonaffinity, and all activation-specific obligations. Their complete derivations are preserved in `preparation/`. They were authoring material, not the fresh isolated final reviews, and were not supplied to the final reviewers.

## External literature and classical background

The new arguments require no external paper. The manuscript supplies all specialized Gaussian-program and dynamical proofs on which it relies. Remaining background consists of elementary linear algebra, Gaussian integration by parts (also derived in the needed forms), classical integration/convergence facts and Hilbert-space completeness; hypotheses are checked where used.

The preceding study preserved a separate full-text cross-check of Greg Yang's 87-page Tensor Programs III, including every proof appendix. That existing PDF, complete extraction and reading record remain available in [the earlier literature audit](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_self_contained/EXTERNAL_DEPENDENCY_AUDIT.md). No statement of that paper is an unproved premise of this extension, and no new reading of it is claimed here. No recursive external proof obligation is introduced by the new activation class.
