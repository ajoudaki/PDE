# Isolated adversarial review of PLATEAU_CONFINEMENT.md

**Verdict: PASS.** No substantive objection remains to the deterministic confinement theorem or its explicitly conditional population consequences.

Scope: I read the complete supplied manuscript only. I did not consult linked documents, other reports, prior reviews, or external sources, and performed no experiments. This review assesses precisely the hypotheses, proofs, and conditional implications stated in that manuscript.

## Deterministic proof

The freezing argument is valid for the stipulated absolutely continuous paths and realized integrable controls. For fixed realized coefficients the spatial Lipschitz bound is integrable. Comparison with the constant path through a point where all retained gates vanish gives uniqueness both forward and backward in time. This remains a legitimate comparison when the original controls depend on the solution: the comparison fixes their realized values and does not assert uniqueness of a larger coupled system.

The planar switching argument is sound. Outside the closed union of double-strip intersections, a nonconstant path has exactly one strictly active strip. The index is locally constant and therefore constant on each connected component of the temporal complement. The integral equation then places every displacement on the corresponding unit direction, with its scalar displacement equal to the change in that strip coordinate and bounded by two. Continuity extends this bound to component endpoints. Whenever the path visits the intersection union, every complementary component has at least one boundary point in that union, including components adjoining the endpoints of the full time interval. This proves the stated bound without assuming finitely many switches. For two gates, visiting both closed strips while avoiding their intersection contradicts the fixed-index conclusion; constant paths satisfy the same assertion directly.

The double-strip estimate is correct: the least eigenvalue of the pair Gram is (1-|u_i\cdot u_j|>\delta), while the two constrained coordinates have squared sum at most two. In rank two every pair spans the same input plane, so (B_\delta=\sqrt{2/\delta}) uniformly bounds all such intersections. The fixed orthogonal component is restored without multiplying the initial norm, giving the claimed additive (D_\delta=B_\delta+2) bound. Pair separation excludes rank one, so no omitted singular rank remains.

In rank three, the last-activation construction is valid even if activation sets have infinitely many components or their suprema coincide. Continuity puts each last time in its corresponding closed strip. Choosing the earliest of these last times removes that gate on the entire subsequent open suffix; its value at the single starting endpoint does not affect the integral equation. The remaining two last times lie in the suffix. Projection onto the two remaining directions therefore visits both closed strips, and the planar lemma bounds the whole projected suffix by (D_\delta). When the suffix is a singleton the two closed constraints directly give the same bound.

The transverse coefficient on that suffix is constant. The removed gate's closed constraint at the starting point yields

\[
|r|\,\operatorname{dist}(u_k,\operatorname{span}(u_i,u_j))\leq 1+D_\delta.
\]

For every coefficient vector with its (k)-th entry equal to one, its Gram quadratic form is at least \(\kappa\) times its squared coefficient norm, hence at least \(\kappa\). Taking the infimum verifies the stated lower bound on the squared distance. Thus the claimed (R_\Gamma) follows with the correct inequality direction. If some gate never opens, the reduction to two gates directly supplies the smaller additive bound. Restoring the fixed component outside the input span completes the stated full-space estimate.

Restriction and time reversal preserve the required regularity and control integrability, establishing the subinterval and backward-time assertions.

## Adversarial cases and population consequence

The proof withstands zero gates, gates with additional interior zeros or changing sign, arbitrarily large integrable controls, trajectories touching support boundaries, constant suffixes, tied last times, and infinitely many switches. Near-singular rank-three configurations are covered by the expressly nonuniform constant; exactly rank-two configurations use the separate planar argument. None of these cases provides a counterexample.

The population implication is correctly conditional on one probability-one event supporting locally absolutely continuous row paths and their integral equations on every compact interval of existence. Applying the deterministic theorem to each such path gives all-time bounds on that event; it does not interchange time-indexed exceptional sets. Gaussian initialization is not needed for the pathwise inequality itself, but supplies finite moments, which transfer to the stated envelope by the displayed elementary inequality. No uniform bound on the realized control integrals is used.

The raw-flow and capped-flow applications are conditional on the asserted row equation and integrable realized coefficients. The manuscript expressly does not claim population existence, a construction of return fields, convergence, bounds on other row quantities, or general discrete-time confinement. Its Euler-step observation follows directly whenever a gate is nonzero at the chosen row.

**Required corrections: none.**
