# Author-side check of the substantial-training proof attempt

2026-09-20. Supervisor check of the new C-H4 reports in this study.
**The complete C-H4/C-X3 claim does not pass: its reached-source continuation
and supported-law transfer obligations remain open.** The scoped partial
results and implications below have been checked. This is not a fresh complete
independent review, formal verification, or a promotion recommendation.

## 1. Checked revisions and author relationships

The three route authors initially worked from separately assigned inputs,
without reading each other's reports. The supervisor then read their complete
reports, requested corrections and focused second rounds, and wrote the
fitting-constants theorem and synthesis. The geometry author subsequently
checked the complete fitting-constants theorem; that relationship and read
scope are disclosed in CH4_FITTING_CHECK.md. These are author contributions
and internal checks. No claim of a fully independent C-X3 review is made.

Exact SHA-256 values of the checked frozen files:

| File | SHA-256 |
|---|---|
| CONTRACT.md | ab0b818cc82ac709f32f44e26d2760d79c153dad6a631b48e62a12015018ca6b |
| CH4_FITTING_CONSTANTS.md | d9e305c82f65860c010a922ae5d016732acadb3010852822488759971a1d8e96 |
| CH4_FITTING_CHECK.md | 192184507e5f93980e94a1052e86cda272afab5eb0c36d32186e1dd14fda0ab3 |
| CH4_REFERENCE_GEOMETRY.md | 9ac93da7173a1d12e81a0f01e97e656baa2bd7ec060f7be714099b3e3317bb64 |
| CH4_REFERENCE_SOURCES.md | e68f50322e19a1b3946b291e136e1e570c86494401abd70fdd80b5e1e18382f0 |
| CH4_REACHED_ESTIMATES.md | 978ab0958297da3553de36ea5b976bbb8fece710ec8a93b63a0bbeef33f17b74 |
| CH4_PROOF_STATUS.md | 3b02441aa3b8620f294e2b7eb4e04351a5ce2eafaf1218d13dc1f90801cb9158 |

The unchanged local inputs used here include CH3_LOCAL_PROOF.md at
`8d044f2e56c8d5be30a9739cea7aef52aa565b89b21e266061b41db921a4568b`
and CH3_HIERARCHY_PROOF.md at
`e7caf06e3b52d68b54a044efa78cfc3ed26efee12a079f0eb9a681d7e66d19c7`.
Those remain internally checked author results, as disclosed by the README.

The supervisor's scientific reading for this round covered the complete new
reports, including both second-round appendices and the reached-estimates
amendments, the contract and local proof, maintained C.1–C.2, complete
C.4.5.1 and C-H4 D.1–D.3. Existing unchanged study/maintained input checks
remain as recorded in the README; no new audit of every transitive dependency
is claimed. Each route records its own complete input scope. Required skills
and shared guides were read. A limited primary-source abstract screen imported
no theorem and is disclosed in CH4_PROOF_STATUS.md.

## 2. Fitting and endpoint implications

The elementary tanh inequality, Gaussian fourth moment and Cauchy–Schwarz
give q_l>=q_(l-1)/(1+3q_(l-1)); reciprocation gives q_L>=1/(1+3L).
Initialized orthogonal Gaussian covariance gives m_L=q_L/2. This part is
unconditional and needs no numerical quadrature.

The hidden directional map J is bounded at every bounded raw state and its
adjoint uses the actual adjoints of each separately labelled initialized
action. The curve chain rule proves c_ss=JJ*c without a derivative of J.
The radial calculation has the correct minus sign on g_s squared and gives
g_ss>=0. The nonzero initial slope prevents a later zero of g on the existing
solution interval. Thus b_s>=m_L is valid wherever that solution exists.

The physical clock has coefficient 2(1-b) for the contract's unhalved,
probability-weighted loss. Positivity of 1-b at every finite time is derived
from a bounded scalar coefficient on a compact strong path, not assumed.
Consequently loss<=exp(-4m_L t) and the conditional time 2(1+3L) are correct.
The separately stated feature-continuation hypothesis supplies the stronger
endpoint implications; it is not inferred from the physical finite-horizon
hypothesis. The row, middle-edge and readout gradient squares sum to the
displayed whole-input constant with no missing dimension factor.

CH4_FITTING_CHECK.md independently reconstructs these calculations within
its disclosed author-side scope. Its PASS is confined to the stated
unconditional bound and conditional implications.

## 3. Raw bounds and conditional comparison

The raw Euler/GD induction is triangular: readout first, then hidden edges
from top to bottom, then the full first row. Only higher action norms enter
each next estimate. It applies to arbitrary positive Euler steps of bounded
total duration and recomputed affine interpolants, without assuming loss
descent. The prescribed finite Gaussian readout is retained; its supremum
exceeds one with probability at most 2n exp(-n^2/2). These facts justify the
unconditional fixed-horizon raw bounds, not population continuation.

The one-reference subtraction uses one factor 1+R, not one per layer.
The Osgood criterion is proved for that scalar comparison inequality. Its
necessity statement is confined to deductions from the inequality; it is
not a necessary condition for existence of the neural dynamics. The
exponential-tail and time-integrated-prefactor moduli have the correct
signs and exponents. A finite chronological partition propagates the current
error and does not restart from initialization.

One substantive limit-passage clarification was requested and incorporated
before freezing the reached-estimates report: program-dependent integrated
response envelopes may not be assumed to converge to an envelope of the
target. Its §7 now uses soft cutoff tails, the supremum over rational cutoffs,
and Fatou on log M to construct the target envelope, with a halved exponential
rate and an explicit change of constants. This supplies an almost-everywhere
certificate, which is sufficient for the integral comparisons.

The finite-width version keeps the reference graph and cutoffs fixed before
the width limit. Scalar distance equicontinuity and a countable-cutoff
subsequence justify optimization only after this limit; no exponential bound
at a width-dependent cutoff is assumed. The hierarchy alternatively compares
to fixed exact reference Euler paths before refining the reference mesh.
These are conditional extensions of the earlier fixed-program bridges, not
an application of their theorem to a growing transcript. The vanishing-step
condition eta_n->0 is consequently retained only with the source premise.
The explicit positive radius formula also remains conditional on a source
certificate for the required class of nearby laws.

## 4. Geometry, Gaussian reuse and second-round checks

The autonomous cutoff construction preserves every initialized action and
uses actual adjoints. Its global raw bounds and local Lipschitz constants
are checked for each fixed cutoff. Removal still needs the uniform or
integrated exponential tails explicitly hypothesized there.

The Hessian calculation localizes a symmetric HS direction on large values
of a nondegenerate reused Gaussian adjoint field times the intermediate
tanh second derivative. The lower feature Gram normalizes that direction
to unit HS norm, while the other Hessian term stays uniformly bounded.
This excludes the stated ambient one-sided Lipschitz estimate, including
the metric that changes only the first row. It does not exclude uniqueness
on the reached subset.

The exact cutoff chain rule is db[G_N]=||G_N||^2+<G-G_N,G_N>.
The readout-scaling example checks that the last term cannot be dropped as
a structural identity even inside the reference symmetry class. Bounding
it introduces the same unproved integrated tails. No dissipative sign for
that defect has been assumed.

The symmetric HS perturbation in geometry §9 annihilates both initialized
anchor features by oddness and independence. Its recomputed reverse field
contains a nonzero multiple of exp(G^2/8) minus its mean, together with an
independent Gaussian and bounded terms. Restricting the other independent
coordinates gives probability at least c R^-4 (log R)^-1/2 above a multiple
of R, and hence the RMS-tail lower bound c' R^-1 (log R)^-1/4. The perturbation
can be arbitrarily small with finite raw energy quantities. No assertion
that it is reached by the specified optimizer follows or is made.

The source report's bounded-operand Gaussian example retains the response
along the original queried feature, rather than replacing the reverse action
by a fresh Gaussian. Its rare-event scaling proves the claimed failure of a
general uniform-tail implication. The later combined-response identity uses
Gaussian integration by parts and an L2 covariance isometry, without a Gram
inverse. The time derivative and temporal envelope bounds follow because
the actual top readout and its velocity are pointwise bounded. The Gaussian
innovation envelope uses time Cauchy–Schwarz and Jensen; no independence
between times is required. The learned-rank contribution is bounded directly.

The second-round source derivative holds with deterministic response
coefficients and covariances frozen, as required for the named-source
derivative. The causal inverse is finite for each fixed program. Its C3=0
bound is explicitly for an easier conditional system; the actual middle-layer
response contributes correlated E[B C3 Y] terms. The signed initial response
expansion follows by projecting its O_L2(s^3) remainder, and is not an
exponential-moment statement. The parity calculation and the early occurrence
of both signs in the top gate derivative do not establish averaged
dissipation. Their limited conclusions are stated correctly.

Finally, the reached-estimates report's generic HS perturbation uses a field
in L2 but not L4, orthogonal to all active bounded features. It preserves
their forward values exactly while destroying the fourth backward moment.
Both this example and the stronger symmetric example concern arbitrary
nearby states, not breakdown along the canonical reached flow.

## 5. Disposition and execution boundary

The initialization bound, raw Euler/GD bounds and displayed conditional
comparison/fitting statements pass this author-side check. The failed
absolute-cap systems and counterexamples invalidate only the specified
proof shortcuts. They do not falsify the depth-extension conjecture.

The unproved chain is still:

1. Construct and uniquely continue the actual three-layer reference through
   the fixed fitting horizon, with sufficient reached backward/source control.
2. Prove a quantitative source continuation/transfer bound for an explicitly
   positive supported-law neighborhood, including its nonatomic members.
3. Discharge, rather than assume, the long-horizon actual GF/raw-GD and
   common-hierarchy premises, and the additional reference endpoint targets.

No numerical experiment, training run or formal machine proof was conducted.
Existing C-H3 implementation checks were not rerun, because no code changed.
No existing proof, contract, maintained book or maintained API was changed.
Only new files in this study and its README were written. No files were
staged or committed, and no promotion was performed. The unchanged source
hashes and shared Git state were checked separately from the mathematics.
