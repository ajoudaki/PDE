# Internal reconstruction of the neuron-reduction continuation

2026-10-03. Coordinator check, not an isolated promotion review. The
coordinator proposed the joint lower/upper cubature strengthening and
discussed the weighted block construction. These are collaborative internal
checks, not author-independent verdicts.

## Joint source and initialized cubature result

Read the complete original source, then the complete added joint-population
section and all revised scope/count passages of JOINT_SOURCE_SAMPLING.md.
Final checked SHA-256:
`6e8c856fb9c79e106cf3e75580019cdb0d07b0873ef745ea7700b82d23a65f87`.

**PASS for the exact Gaussian identities, initialization-only cubature
theorems, finite weighted construction, and stated restricted obstructions.**
There is no all-time neuron approximation theorem in that source.

1. At zero readout, all hidden velocities vanish. Direct differentiation
   of the actual memory reconstruction gives its second mixer derivative
   \(2yu h^\top/n\), independently of q. The first feature acceleration
   is \(2y\operatorname{diag}(\operatorname{sech}^4a)W_0^\top u\).
   Thus both acceleration formulas are for the actual closure.
2. Conditioning on \(W_0h=z\) and then \(W_0^\top u=k\), with u fixed
   by z, is legitimate adaptive Gaussian conditioning. The two prescribed
   projections satisfy their consistency identity. The remaining random
   matrix is \((I-P_u)G(I-P_h)/\sqrt n\); applying it to the now fixed
   feature acceleration gives the stated covariance. Expanding the Gaussian
   lower response yields every term in (7); the final subtraction removes
   precisely the projection on h. The positive variance term survives.
3. The tanh power-series recurrence has alternating nonzero coefficients.
   Each odd angular Fourier mode is therefore present for an open set of
   Gaussian radii. Averaging the random phase gives infinitely many positive
   covariance eigenvalues. The finite-dimensional locally Lipschitz
   representation exclusion follows from its lower-dimensional image having
   zero Lebesgue measure. It is not an effective-rank or prediction lower bound.
4. The complex-strip proof uses the Gaussian mixer only at initialization.
   The root row bound is O(sqrt(log n)), and each fixed complex query has
   Gaussian variance at most one. The operator norm is used only to extend
   a polynomial-size net, where the intentionally crude derivative bound
   O(sqrt(n) sqrt(log n)) is harmless. Cauchy's bound then yields a common
   upper-feature strip of width at least c/log n. Tanh is bounded by one
   when the imaginary part of its argument is at most pi/8. There is no
   unjustified cancellation assumed after learning.
5. Contour shifting gives Fourier coefficients bounded by
   exp(-s times the frequency l1 norm). The product geometric-series tail
   is at most C s^(-d) exp(-s p). Evenness in each angular coordinate turns
   the truncated series into tensor Chebyshev polynomials. At root-width
   accuracy their common dimension is O((log n)^(2d)).
6. Finite convex elimination preserves mass and the coefficient averages
   with at most dimension-plus-one positive weights. Returning from the
   polynomial approximants costs at most epsilon on each side because the
   weights are positive and sum to one. This controls the original empirical
   kernel, not a limiting population.
7. In the joint construction, the lower space includes both polynomial
   coefficient columns and exact training feature columns. Its RMS-
   orthonormal basis V has r=O((log n)^(3d/2)) columns. Lower cubature
   exactly preserves its Gram; upper cubature preserves the Gram of W0 V,
   the query-kernel polynomial moments and the exact training-kernel entries.
8. The reduced matrix \(B_0=U_JV_I^\top D_1\) has weighted operator norm
   at most the original matrix norm. The adjoint is exactly
   \(V_IU_J^\top D_2\), as verified by both weighted inner products.
   Exact training columns imply exact selected training preactivations and
   hence exact full weighted training kernel. Query errors are bounded by
   \(K(1+\sqrt n)\varepsilon_1\); taking epsilon1=1/n and epsilon2=1/sqrt(n)
   gives the displayed root-width result. No conditioned Gaussian estimate
   is applied to adaptively chosen selected rows here: the remainder uses
   a simultaneous deterministic bound on every row.
9. Both supports have O((log n)^(3d)) nodes. All original large arrays and
   polynomial coefficient arrays are setup inputs. The runtime fixed mixer,
   retained read-in rows, weights and moments do not evaluate discarded
   neurons. The fixed matrix is a computed projection of W0, not its raw
   submatrix. Its missing actions remain genuine approximation errors.
10. The source-space Gram identities and weighted moment reconstruction
    preserve one matrix and its adjoint. The exact-invariance obstruction
    uses the n-dimensional Krylov span of an independent nonzero vector
    for a Gaussian matrix with distinct singular values. Neither statement
    bounds approximate trajectory dimension. The final count arithmetic is
    explicitly conditional on an unproved all-order neuron theorem.

The small-label global fitting proof was not newly asserted for this joint
construction in the checked source. Its all-time unseen-input fidelity is
unproved even if a fitting transfer is supplied. Initial prediction matching
alone cannot identify its learned endpoint.

## Weighted block construction and source certificate

Read all mathematical sections of NEURON_CUBATURE_CONSTRUCTION.md,
including the explicit label-threshold qualification and retained backward
variation. The originally checked mathematical source has SHA-256
`7da3e804e36fe12db17ee58c2fb872547057e88ef090c6e1e3d04b15a5cf55d0`.
The author then corrected the exponent-boundary wording in Section 7.
Those changed passages were reread; the final source hash is
`d02322be2e58dd8462323c7dfbe85c51451eb4186ff030274a4cd28b47bb81cf`.
The correction distinguishes a strict power saving from possible
subpolynomial savings at exponent one. It changes no construction,
equation or source inequality, and the verdict applies to this version.

**PASS for the finite weighted equations and conditional deterministic
source estimate. No neuron sampling rate is proved.**

The raw masses give mobilities 1/mu_i, 1/nu_j and mu_i/nu_j; direct
differentiation of the weighted loss verifies all three update factors.
The block-average fixed mixer is a contraction of W0 between two isometric
weighted embeddings. Its weighted adjoint is the average of W0 transpose,
not an independently selected matrix. Rank-one increments have exactly
the same weighted Hilbert-Schmidt norm as their full-size lifts.

The fitting transfer uses only probability-space Hilbert norms, bounded
gates, operator bounds and the verified initial Gram. No inverse minimum
cell mass is introduced. Forward-only fixed-accuracy quantization preserves
a gap, but may require the smaller explicitly stated modified-model label
threshold. This cannot silently be presented as the user's entire existing
label range or as test-prediction fidelity.

The proof lift retains W0 exactly and lifts only its learned correction.
Multiplying this lift in the forward and reverse directions gives (17)
with exactly the two leakage vectors in (16). The weighted projection-
energy identity yields its integrated memory defect; the stated q^(-2)
bound is separately justified and does not borrow the newer original-
closure q^(-3) estimate without proof.

For the physical-time comparison, the two residual equations must use
their actual predictors, not the predictor of the lifted parameters.
The checked derivation does this: the coarse positive tangent Gram damps
the residual difference, while the remaining source is the dense residual
times the two leakage norms. Integrating the residual inequality then
the parameter inequality yields the stated Ce^(CYM) amplification and
includes the initial read-in projection error. Finiteness is known before
this estimate, so its use is not circular. The source is not assumed small.

At queries, the top readout and first derivative of tanh are block
constant, whereas the forward leakage is orthogonal to the block space.
The first Taylor contribution cancels exactly, leaving the stated squared
leakage term. Its retained backward variation is instead H^T D_block eF,
which need not vanish or be quadratic in the leakage norm. This verifies
the distinction between observable cubature and response accuracy.

Finally, the conditional Gaussian covariance trace for the first
read-in acceleration is at least sigma^2 times (tr D1^2 minus N minus 1).
For N=o(n) this is order n y^2. The noncentral Gaussian lower-tail
inequality (36) follows with t=1/(4||C||op) and gives the asserted
high-probability acceleration bound after multiplying by 2y. The
measurability restriction on the selected subspace is essential. This
does not give a prediction lower bound or rule out response-aware selection.

## Overall verdict

The complete EMPIRICAL_PATH_QUADRATURE_CHECK.md was also read and its
actual-reference Monte Carlo corollary reconstructed. Its variance
identity, time-variation bound and finite-second-moment query integration
are correct. The source hash it checks is
`9b92ba8cf4405d805a77661877118f13cdfe492d804d9f76b2747bb3ea1a80b9`.
Its MC corollary is uniform in constants for every chosen q; no simultaneous
sampling event over all q is claimed. The separate autonomous-dynamics
error has not been removed by this result.

The initialized joint-neuron cubature is a genuine positive sampling
result for both hidden populations. The full all-time approximation of the
original closure, including its unseen-input endpoint, is still open. None
of these checks upgrades a source inequality, initial kernel match, or
fitting guarantee into the requested trained-trajectory theorem.
