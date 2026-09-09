# Intermediate two-sample theorem: assembly, not final certification

STATUS: complete candidate assembly submitted for isolated adversarial
review. The universal-activation user goal remains OPEN. This candidate
has only the intermediate angle-specific quantifier below. Its proof is
the composition of the explicitly supplied mathematical dependencies;
no external review outcome is a premise.

The intended intermediate conclusion is as follows. For every fixed
rho in [-1,1), there exists epsilon_*(rho)>0 such that, for each fixed
0<epsilon<=epsilon_*(rho), phi(z)=1+z+epsilon arctan z in all three
hidden layers satisfies the complete two-sample contract on every
finite physical interval, for both choices of relative label sign.
The activation coefficient is chosen once, before width/time limits.
The first-layer field, two population operators with their adjoints,
and readout form a finite collection of autonomous state objects.
No width-dependent activation, clipping in the final dynamics, frozen
hidden layer, or effective affine limiting activation is permitted.

This is ONLY an intermediate quantifier, explicitly authorized by the
latest user clarification. The ultimate quantifier is one identical
activation for every rho<1; the present assembly does not establish it.

## Proof dependencies and assembly order

1. CONTRACT.md defines the finite architecture, independent Gaussian
   initialization, average loss, eta_n=n^-2, RMS-input first-layer
   learning normalization, and all observables. Population operators
   act between three separate neuron spaces. Finite transpose is ^T;
   population adjoint is ^*. Fixed finite-program convergence is joint
   empirical-average convergence after matrix reuse, not an iid claim.

2. SYMMETRY_RADIAL_CLOCK.md (hash
   40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4)
   proves deterministic population symmetry from the finite-program
   construction. It also constructs the affine scalar-feature baseline
   through projected prediction g=3/2, with finite feature time and
   raw Hilbert primal bound, for every permitted rho and label sector.
   Both positive hidden Gaussian variances and positive arctangent
   affine-approximation errors hold throughout this compact interval.

3. TWO_SAMPLE_SOURCE_BASELINE.md (hash
   a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f)
   identifies the full two-sample response equations and derives
   mesh-uniform affine coefficient bounds from that primal premise.
   The Gaussian-probe identity supplies the actual response control.
   The affine primal premise required by the source note is therefore
   discharged by the preceding radial/affine construction.

4. NONLINEAR_RESPONSE_PERTURBATION.md (final hash
   ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568)
   proves uniform mesh/cap bounds
   for actual nonlinear source coefficients and subGaussian C,q^(2),
   q^(1), for sufficiently small fixed epsilon depending on the
   bounded affine interval. It includes all current-source terms and
   closes the four-stage causal recursion. Its comparison uses clips
   ONLY on the epsilon part of phi'(z)q. The affine part q remains
   uncut. This is the main new nonlinear continuation input.

5. PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md gives direct strong
   O(epsilon) state comparison and preserves a margin g_R(S)>5/4.
   Actual subGaussian tails from item 4 defeat the linear-in-R
   asymmetric comparison cost, constructing the uncut C1 autonomous
   population path through that feature interval. The same estimate
   gives uniqueness against arbitrary bounded-primal competing strong
   paths and uniqueness after reached-state restart, without assuming
   their own tails. Radial coercivity and symmetry then supply the
   physical clock on every finite [0,T].

6. The same bridge compares the GENUINE two-residual finite-width
   GF and exact raw GD to their same-width fixed-cap physical reference.
   Population symmetry is never imposed on finite predictions. Fixed
   finite-program limits plus dimension-independent fixed-cap Euler
   errors supply the reference convergence; learned matrix operator
   bounds are certified by rank-update lengths, not assumed operator-
   norm convergence. The asymmetric tail comparison removes the cap.
   Raw GD is exact Euler in these coordinates, so no one-sample F
   coordinate defect is imported. This gives the proposed full-sequence
   joint mean-field/GF/GD path convergence in probability.

7. FIXED_CAP_VELOCITY_BRIDGE.md (hash
   a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0)
   establishes
   uniform-time empirical integrability and convergence of the
   RECOMPUTED hidden velocities for the fixed-cap reference. Its primal,
   local-Lipschitz, and fixed-program premises are supplied by items
   2--6. Strong raw state convergence alone is not a substitute.
   The continuation bridge additionally supplies the ordered R/M
   truncation limit for uncut velocities and W_2(C([0,T])) convergence
   of the hidden preactivation/feature path laws. All four 2-by-2 raw
   kernel blocks, both hidden
   matrix orientations, predictions/loss, and same-layer joint sample/
   time laws then follow with the stated right/terminal-left derivative
   conventions. The whole composition, including all observable and
   nontriviality clauses, is the subject of the requested review.

8. INITIAL_FEATURE_LEARNING.md (hash
   bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351)
   proves that for every fixed epsilon>0 and allowed angle,
   the exact initial transpose laws give nonzero accelerations of all
   three hidden parameter blocks and of each sample's hidden features.
   If V denotes this raw hidden acceleration and kappa the label-
   projected total kernel, then

       kappa(s)=kappa(0)+2s^2 ||V||^2+o(s^2),  ||V||>0.

   Thus the limiting model is not frozen or a constant-kernel limit.
   All-time nonaffinity uses item 2's Gaussian approximation-error
   margin and item 5's O(epsilon) comparison: the best affine error of
   phi_e(Z) is epsilon^2 times that of arctan(Z), and stays positive
   throughout the full compact feature interval after shrinking the
   fixed epsilon once. This shrinkage is independent of physical T.

Only finitely many label patterns occur. Taking the minimum of their
positive epsilon thresholds selects a coefficient depending on rho
alone, if desired, not on the labels. Opposite overall label signs
also have the readout sign symmetry. The antipodal case uses no inverse
of the input Gram, and the proofs explicitly include it.

## Remaining universal-angle research obligation

The affine initial projected contrast kernel is (1-rho)/2. Present
proof constants depend on the associated feature duration and primal
bound; their positive threshold has no proved positive infimum over
rho<1. It is invalid to choose epsilon tending to zero along a width
limit, or to call this family one activation.

UNIVERSAL_ANGLE_ROUTE.md provides new exact common/contrast identities,
an instantaneous signed curvature cancellation, and a lower bound
showing why a single short interpolation feature window cannot cover
near-coincident opposite-label inputs for any fixed Lipschitz activation.
Its bounds do not control the full lower-layer causal response. The
required next estimate concerns actual reached Gaussian fields and
their source derivatives, not an arbitrary L2 product bound or a false
pointwise sign condition. Failure of those methods is not a theorem
counterexample. No universal activation has yet been certified.
