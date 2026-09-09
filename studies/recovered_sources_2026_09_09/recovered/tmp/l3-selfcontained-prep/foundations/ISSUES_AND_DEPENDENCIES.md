# Foundations preparation: exact issues and dependencies

This is an author/auditor preparation record, not an isolated final review. The standalone text is `FOUNDATIONS_CHAPTER.md`. No earlier or sibling review or status document was used.

## Mathematical source coverage

Read the finite model and intended conclusions in `/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_separated_angle_theorem/PROOF.md`; reconstructed the generic source theorem, singular-query argument, common action spaces, and fixed-cap local-flow material in `sources/L3_LOCAL_COMPLETE_PROOF.md`, lines 211–730; reconstructed the scalar-gradient and strong-chain arguments in the same source, lines 1748–2095. Checked the three-sample controlled source indices against `CONTROLLED_RESPONSE_LEMMA.md`, Section 3.1, lines 37–76. No experiments were performed.

## Issues found and disposition

1. **The older specialized finite-mesh statement has different dynamics.** Its arctangent activation and transformed first coordinate are not the gain-network raw Euler system. The replacement proves a generic finite-program theorem and separately derives the gain-network raw equations (F.18)–(F.23), with all three sample slots and coefficients in their actual positions.

2. **An adaptive Gaussian conditional formula needs a filtration argument.** Merely saying that a final transcript imposes linear constraints is insufficient without explaining adaptivity. Section 3 gives a successive conditional-law induction: inputs are measurable at query time, each answer conditions only one current Gaussian factor, and other residual matrix factors remain conditionally independent.

3. **Singular Grams cannot be treated by an unsupported pseudoinverse limit.** Section 5 perturbs each individual query with a freshly revealed independent Gaussian input, proves a strictly positive limiting Schur complement at fixed noise, gives a width-uniform finite-program L2 comparison, and separately proves continuity of the scalar recursion and expected formal derivatives through positive square-root coupling. No rank-stability conclusion is assumed.

4. **Expected derivative entries are representation-dependent on singular supports.** Section 5 proves that only the contracted response is invariant. The chosen formal expression, with all deterministic contractions and control values frozen, specifies the individual coefficients. A claim that the pseudoinverse prescription always agrees entry by entry with the formal derivative would be too strong.

5. **The gain top gate must be clipped in the same nonlinear part as the lower gates.** The bound on derivatives is valid for D_R(z,q)=aq+e g(z)tau_R(q), including incoming q=C. The uncut product C phi'(z) is not globally Lipschitz on an unrestricted L2 ball. The replacement verifies the actual fixed-cap gates in (F.17), and treats uncut velocity/backward observables by bounded-multiplier truncation where necessary.

6. **The common-space construction must retain enough probes and the full first-layer root.** Section 7 includes a countable dense coordinate language and both orientations of every initialized action. It retains the full d-dimensional Gaussian root w_0, so the raw first block exists even when the sample Gram is singular. Boundedness, well-definedness under L2 identification, density, completion, and adjunction are each explained.

7. **A bounded initial operator is not a Hilbert–Schmidt initial operator.** Section 8 distinguishes the two and verifies that finite normalized-vector Hilbert–Schmidt norm equals the ordinary matrix Frobenius norm. The factor d in the raw first-block metric is retained. This yields the exact raw gradient and kernel formulas in (F.39)–(F.44).

8. **Strong curve differentiation and Fréchet differentiation of the scalar predictor are separate claims.** Sections 9–10 prove both. No unrestricted L2-to-L2 Fréchet differentiability of the activation map is used. The scalar predictor's Taylor remainder is tested against each fixed backward L2 coefficient with a truncation argument.

9. **Measurable controlled paths need not be C1.** Section 11 proves absolute continuity with the equation almost everywhere for measurable controls. The autonomous physical capped field is continuous, so its solution is strong C1. This distinction should remain explicit in the assembled manuscript.

10. **The finite theorem is not a growing-program theorem.** The replacement states fixed length and fixed cap throughout. Direct application to the width-dependent n^{-2} raw-GD program is unavailable; the bounded-ball Euler comparison and the separate velocity/uncapping bridge must complete that argument.

11. **Finite polynomial expectation calculations need uniform integrability.** Equations (F.4a)–(F.4c) supply all fixed-order initialized Gaussian operator norm moments and an independent Gaussian-probe normalized-trace comparison. This avoids importing Gaussian Poincaré or a random-matrix master theorem into an initial-motion Wick calculation.

No contradiction in the requested finite-program foundations was found after these explicit arguments. This is not a certification of the controlled-response bootstrap, global unclipping, full raw-GD limit, or nontriviality arguments, which lie outside this task's authoring responsibility.

## Actual dependency inventory

The foundations chapter invokes no Tensor Programs theorem or other external nonclassical theorem. Its probabilistic inputs are Gaussian exponential moments, orthogonal invariance/independence of Gaussian coordinates, elementary conditional expectation, and the finite-second-moment weak law of large numbers. The required Gaussian conditioning, Stein identity, operator norm bound, singular Gaussian extension, covariance square-root continuity, W2 criterion, and trace-probe estimate are proved in the chapter.

Its measure and Hilbert-space background consists of ordinary countable product probability spaces, Fubini/Tonelli, continuity of measures, the monotone-class construction of generated sigma-fields, Cauchy–Schwarz/Hölder, completeness of L2, finite-dimensional orthogonal diagonalization, orthonormal bases and Parseval. The chapter gives the particular density/completion, Hilbert–Schmidt, integral, and contraction arguments used. These classical foundations are not replaced by claims about the literature audit.

Outputs available for the assembled theorem: F.1 fixed finite Gaussian empirical limits; F.3 source rule; F.4 singular regularization; F.21–F.23 exact gain/sample source coefficients; F.26–F.27 bounded canonical actions and actual adjoints; F.29–F.33 raw Hilbert structure; F.5–F.7 multiplier, curve-chain, and predictor C1 results; F.45 fixed-cap bounded-ball Euler estimate; F.4a–F.4c operator moments and trace concentration.

Obligations still external to this chapter: a mesh- and cap-uniform controlled-response bound; its affine finite-array premise and perturbation bootstrap; cap-uniform reference tails; asymmetric physical comparison and its linear cap loss; global primal and residual-clock bounds; compact-interval finite-GF/raw-GD bridge including all velocity/path observables; positive affine approximation errors and initial-motion/kernel-change calculations. These must be included as actual proofs in the other manuscript parts.

