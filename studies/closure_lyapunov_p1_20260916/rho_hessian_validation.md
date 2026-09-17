# Checks of the broad-rho and second-order continuation

2026-09-16. Internal research validation; no promotion or experiment.

## Scope and independent derivations

The continuation contract is `rho_hessian_contract.md`. Three scoped
analytical authors started in fresh contexts, with specified established
and same-study inputs and separate output files. They did not receive
each other's approaches before freezing their reports. Root then read
all three complete reports, reconstructed the arguments, and compared
the normalizations. Root also developed the distinct singular-state
second-order calculation, which received a fresh isolated review.

Frozen independent outputs:

* `rho_endpoint_extension.md`:
  d8b6401195dbfe1b1f2e7e3f4177b318364c3cd8ec3f221b314c594a341933ef
* `sphere_second_variation.md`:
  8f8d25d84f6bbb41b09ad1f5900970bb5ccbd7ea266ac0c6179ef961752eb1a8
* `rho_hessian_geometry.md`:
  6262c7fc53df9252fd52fbd3cfac2e4a99e01fc07bf5e505912aedd668be871b

The two broad-family routes agree. The endpoint report's unweighted
transverse eigenvalue is THREE times the geometry report's probability-
normalized eigenvalue nu. Their zero conditions and positive quadratic
coefficients are consistent with this conversion. Pairwise nonparallel
input directions suffice for the row-gradient argument, so the linearly
dependent triple at rho=-1/2 is correctly covered. Neither route imports
an inverse input Gram there.

The preserved nonzero transverse middle-matrix component alone does not
prove a nonzero upper contrast. Both reports explicitly distinguish
these quantities. Their rank-loss criterion uses the whole current
transpose and all three physical gradient blocks. The common backward
derivative has nonzero pairing with the common upper coefficient vector,
which makes the quadratic rank-loss coefficient strictly positive.

Root checked the conditional tail theorem independently from the energy
identity: inside K>=kappa I, -d sqrt(L)/dt>=sqrt(kappa)||X'||, and
Phi'<=-4kappa Phi+2B sqrt(Lambda)L^(3/2). A sufficiently small entry loss
both prevents exit and absorbs the multiplier derivative. Strict seed
decay on a compact initial interval supplies a rate from time zero even
if the full tangent Gram vanished at an earlier seed time. The seed
endpoint enters the proof only and is not part of the potential's data.

## Fresh isolated checks

`rho_endpoint_extension_review.md` gives PASS for the unchanged frozen
endpoint candidate. Its reviewer read the entire candidate, the complete
three-coordinate, open-family and rate dependencies, and all required
canonical definitions and proofs. The review verified the exchange
identity directly rather than importing an out-of-scope report. It also
checked the uniform compact event count, local Lipschitz amplitude graphs,
both orientation branches, and the fixed-unit-amplitude limitation. In
particular, joint nullity in geometry/amplitude does not justify a claim
about the amplitude-one slice. Root read the complete review.

`sphere_second_variation_review.md` gives PASS for the unchanged frozen
707-line second-variation candidate. Its reviewer read the complete
candidate and declared dependencies, including the exact initialization
proof after explicit scope expansion. It checked the weighted E_k spaces,
Gaussian moments, first/second response continuity and the E_6 cubic
equation defect. Root also checked that the polynomial state approximation
need not stay in the original bounded-increment space: the Lipschitz
estimate used for comparison is valid in E_6 with bounded c and M. This
is essential to avoid an unsupported C2 Nemytskii claim on L2.

Every mixed product in the state, input, transpose, initialized C0 and
potential derivatives was audited. The symmetry calculation uses exactly
one invariant tangent direction and its five-dimensional averaging
kernel; it does not require all first derivatives to be nonzero on the
remaining line. The Hessian is intrinsic in the displayed chart, which
is normal to second order. A general chart would require the usual
first-derivative coordinate correction. The review's suggested local
reference and display improvements are optional presentation changes;
the frozen candidate was left unchanged. Root read the complete review.

`rho_singular_hessian_review.md` gives PASS for the root's conditional
current-state theorem. Its original frozen hash was
183ee92d471b1e5752136c5f6d58788e678dc6190edb92848fd320d97fe7ad1e.
The reviewer checked sphere curvature, cancellation against d_i=0,
the quadratic predictor coefficient, unhalved quartic loss factor 1/12,
all gradient-variation blocks and the projected Schur coefficient.
Two editorial repairs were applied: keep g for the frozen Gaussian mark
and g_* for the common gradient; explicitly permit either quadratic
coefficient to vanish. The revised candidate hash is
be854ef80b2ffb26d9624b04b637795790b5474f006c57e5468c59e2281b94f5.
The review addendum verifies that reversing only those repairs exactly
recovers the original hash. Root read the review and its addendum.

All isolated reviewers had fresh contexts, complete permitted scientific
inputs and no study README, prior verdicts, parallel findings or history.
Their reports state the actual reading scope. These are internal reviews,
not a promotion audit. No remaining mathematical objection was reported
within their stated scopes.

## Author-side new corollary and synthesis checks

`rho_global_rate_boundary.md` is an author-checked corollary, not separately
covered by the fresh review. Root verified the exact identity
L=(z-1/3)^2+8/9 at signed inputs (v,v,-v), and its finite-time continuity
extension to distinct non-antipodal, even linearly independent triples.
Together with uniform positive C0 on the compact sphere product, it rules
out a uniform all-data rate 4C0 for the old formula. It rules out no
geometry-dependent rate and supplies no fixed compatible failure example.

Root derived equation (6) of `rho_hessian_synthesis.md` directly from
L=(1-F)^2+sum(delta_i^2)/3 and Phi=L W. On the symmetry-averaging kernel,
DF=Dq=DC0=0, so the product cross terms vanish. The remaining terms agree
with the independently reviewed full Hessian and retain D2C0. The
quartic and metric-opening statements in that synthesis are limited to
the reviewed conditional current-state theorem.

The synthesis and README distinguish exact identities, conditionally
proved all-time extensions, previously unconditional neighborhoods and
the open all-rho unit-label claim. No assertion of almost-every-rho
regularity, globally semidefinite input Hessian, selected endpoint
derivative, or global decay of the inverse correction metric is made.

## Workspace and provenance

The canonical inputs and instructions retain the hashes recorded in
`resolution_validation.md`; they are rechecked in this continuation's
manifest. Established docs/code were not changed. Only this study's flat
files were written; the shared index and Git history were not mutated.
Existing unrelated modifications were preserved. No other study's
research, thread, or history was used. No numerical experiment ran, and
the earlier diagnostic campaign remains closed.

`rho_hessian_manifest.sha256` records current proof, review, synthesis,
README and source versions. Earlier manifests retain their historical
README hashes. No promotion to established material is requested here.
