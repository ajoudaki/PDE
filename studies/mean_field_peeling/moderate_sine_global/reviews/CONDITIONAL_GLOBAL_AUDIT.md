# Independent audit of the stopped L3 sine population implication

2026-09-08. Audited `/tmp/sine_adversarial_route.md`, especially Sections 3--4, and checked the ambient constructions in Sections 5--7. This audit concerns the conditional population implication. It does not turn its exponential-tail hypothesis into a theorem for the actual sine flow, and it does not certify the full finite-algorithm/observable reassembly.

Verdict: **PASS for the stated conditional population implication, with the explanatory details below supplied. No blocking mathematical defect found.** The unconditional global theorem remains open because (ET) is unproved.

## 1. The asymmetric comparison has only one truncation factor

The gate decomposition is valid. For R1,R2>=u, first changing q inside D_R1 costs at most L|q-qbar|. Replacing either clip at qbar by tau_u(qbar) has zero cost for |qbar|<=u and cost at most 2|qbar| otherwise. The cosine difference times tau_u is at most 8B u |z-zbar|. Every tail is therefore a reference tail.

Descending through the actual recomputed incoming fields gives

`backward_difference_l <= C state_difference + C backward_difference_(l+1) + C u forward_difference_l + C reference_tail_l`.

The coefficient of the preceding backward discrepancy has no u. After three layers the result remains C(1+u) times the raw state difference, plus the sum of reference tails. The rank-one HS update inequalities use products of L2 norms. Bounded raw increments imply bounded action norms and bounded forward/backward L2 factors. Residual differences are controlled by forward differences, so they introduce no extra truncation factor. Section 3's estimate is correct for both capped states and an arbitrary uncut reference competitor at infinite cap.

## 2. The scalar raw cutoff is a legitimate canonical fixed-program operation

The cutoff is applied to the norm of the increments, not the Hilbert--Schmidt norm of an initialized Gaussian action. Thus it never asks for an infinite initial HS norm. For fixed cap, the raw vector field is uniformly locally Lipschitz on every raw ball: (bounded) derivatives of the capped gate provide the required estimate, forward maps have linear growth and bounded derivative, and rank-one products are controlled in HS norm.

Multiplying by a smooth scalar cutoff of the squared raw increment norm produces a globally bounded, globally Lipschitz field, after its support is placed inside a bounded ball. This supplies a unique global fixed-cap Hilbert ODE. The common generated Gaussian action construction can include the countable family of caps, meshes, cutoffs and integer horizons used in the proof.

The cutoff is also visible in the finite-program scalar contractions. For example, at a fixed Euler transcript a learned middle increment has the form

`Delta W = sum_j gamma_j u_j tensor v_j`,

and its squared HS norm is exactly

`sum_(j,k) gamma_j gamma_k <u_j,u_k> <v_j,v_k>`.

The first-weight increment norm is a corresponding finite contraction with the input Gram, and the readout norm is a same-layer second moment. Their cutoff values therefore belong to the causal scalar coefficients of the existing fixed-program construction. No unavailable operator-norm or cross-width operator convergence is needed.

## 3. Exponential tails suffice for the Osgood limit

Under (ET), for R=min(R1,R2), the estimate

`D^+ a <= C[(1+u)a+exp(-c u)]`, 0<=u<=R,

is valid with constants independent of R. Let eta=exp(-cR), z=a+eta. While z<=1 the choice u=c^{-1}log(1/z) is admissible because z>=eta. This yields

`D^+ z <= C1 z log(e/z)`.

Integrating gives

`z(t) <= exp[1-(1+cR)exp(-C1 t)]`,

which implies the displayed weaker bound (4.2). For sufficiently large R the right side is less than one on the entire fixed interval, closing the stopping argument for z<=1.

This is stronger than the fixed-u Gronwall estimate. It does not require that c exceed a stability constant depending on T. The decay exponent can become very small as T increases, but is positive for each fixed T and independent of R.

Raw velocity differences also vanish uniformly: set u equal to a sufficiently small positive multiple of R exp(-C1T) in (3.3). The resulting term (1+u)a is polynomial in R times an exponentially decaying term; the reference tail is another exponentially decaying term. Hence the capped paths and their velocities are uniformly Cauchy on each fixed horizon.

## 4. Identification and energy are in the correct order

The limit is C1 because the derivatives converge uniformly along with the states. To identify its uncut field, compare the uncut vector field evaluated at the limit state against a capped reference by (3.3), first at fixed truncation u. Send the cap to infinity, then send u to infinity. All tails still belong to the reference. Equivalently, bounded-multiplier continuity passes each recursively defined uncut backward field once the relevant L2 factors converge.

The scalar loss is continuously Frechet differentiable on this raw Hilbert state space. This follows even though the L2-to-L2 activation map need not be Frechet differentiable: when differentiating the scalar loss, truncate the fixed L2 adjoint multiplier; on its bounded part the activation Taylor remainder is quadratic, while its L2 tail contributes arbitrarily little times the perturbation norm. Rank-one and operator-product remainders are quadratic. Continuity of the gradient follows from strong continuity of bounded Nemytskii multipliers against fixed L2 factors. This is the same regularity argument used in the cited radial/gradient source proof.

Consequently the exact chain rule applies to the already constructed uncut cutoff flow:

`E'=-chi ||grad E||^2` and `||X'||^2=chi^2||grad E||^2<=chi||grad E||^2`.

The initial population loss is one, so the raw displacement is at most sqrt(T). Choosing the cutoff to equal one on a strictly larger radius makes it inactive on this limit. The proof does not assume a dissipative identity for the capped gates.

The required tail hypothesis is for the cap family with this chosen cutoff radius. This is a legitimate conditional hypothesis: choose the radius first, assume (ET) for that fixed family, and only then use the energy argument to remove the cutoff. Nothing in this argument proves (ET).

## 5. Uniqueness, restart and horizon consistency

One explanatory point should be made explicit when presenting the argument: an arbitrary bounded-primal strong uncut competitor also obeys the true chain-rule energy identity. It therefore remains in the radius sqrt(T) ball and satisfies the same scalar-cutoff equation. The reference-only estimate can then compare it to the capped family without any tail estimate for that competitor.

At a reached time, concatenate a proposed strong continuation with the already constructed earlier path. The vector field agrees at the joining state, and the concatenated path has the same total energy bound. The initial discrepancy against the cap reference decays exponentially in R by (4.2). Applying Osgood with that vanishing discrepancy still gives equality. Thus restart uniqueness and consistency of the integer-horizon constructions are justified.

This proves the conditional global canonical strong population statement. The finite GF/GD, generated-probe, velocity and path-Wasserstein bridges have not been independently reassembled in this audit; the source report correctly leaves that separate work explicit.

## 6. The sine-specific ambient counterexamples are correctly limited

The Section 5 focusing construction has bounded raw increments: the top correction is rank one with norm ||z-Gh||_n/||h||_n=O_P(1). Its selected-column immutable transpose term has limit 2B sqrt(2/pi) after division by sqrt(n). The initialized tiny readout correction vanishes, and the learned correction is a bounded scalar times h_J/sqrt(n), which tends to zero. The same two-sample model is retained. The tail lower bound 8B^2/pi and its middle-gate lower bound using Phi'>=m are therefore correct. This is an ambient finite-width construction and does not demonstrate GF reachability.

The Section 6 weak-lower-semicontinuity counterexample is also valid. The initialized pair's positive Gram supplies dual fields; a Rademacher sequence gives weakly vanishing rank-one HS perturbations while its exact cosine average annihilates the sine contribution. The perturbed losses are zero and the limit loss is positive. The needed nonatomic top probability space is available from its nondegenerate initialized Gaussian coordinate. This rules out the stated ambient weak-compactness inference, not compactness of actual GF approximants.

Section 7's restricted-gradient and semiconvexity calculations are valid. The tail-supported perturbations yield an unbounded gradient/state difference quotient; the Gaussian square-tail bound makes the residual-change term negligible. The second directional derivatives along normalized negative Gaussian tails tend to minus infinity. The dual-field embedding preserves norms up to fixed factors, so these are full raw-Hilbert obstructions. They remain ambient examples.

## 7. Final scope

The best conclusion supported by this route is:

**For the exact moderate sine activation, the exponential-tail hypothesis (ET) for its actual recursively capped, scalar-stopped physical source family implies a unique global canonical strong population flow.**

There is no proof here that (ET) holds, no reached-state counterexample to the actual target, and no certified full observable convergence theorem beyond the stated conditional core and the existing bridges awaiting reassembly.
