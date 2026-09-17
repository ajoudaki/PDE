# Validation of the potential-design continuation

2026-09-16. Internal analytical checks. No experiment or promotion.

## Author-side reconstruction and comparison

Root read the complete frozen correction_matrix.md, correction_flow.md
and correction_design.md after their independent authors froze them.
The explicit inputs for each fresh author excluded other routes' current
findings and all other studies. The root normal-form construction was
developed separately before reading those reports. Their independent
agreements and differences are recorded in correction_synthesis.md.

The matrix formula was checked directly using p'=-2K xi, q'=-4xi.p,
and the inverse derivative for Gamma0+p p^T. The three matrix-product
orders in the derivative are correct; no sign is inferred from the
product of two positive matrices. The mean/disagreement completion and
the interpolation-normalization Schur complement were independently
reconstructed. The initialization-rate comparison must change the rate
as well as the prefactor; the synthesis explicitly says that it does not
repair the defect at the unchanged rate 4C0. A smaller trial rate can also
repair an initial defect, so that calculation alone is not a broad theorem.

For the normal-form construction, root checked the formal error variable
is held fixed in coefficient derivatives, every inverse uses the current
Gram, and differentiating a coefficient also differentiates its direction
fields. The resulting telescoping identity cancels cubic and quartic
defects exactly. The stated local positivity thresholds, rate and physical
length estimate were reconstructed before independent review. This proof
does not establish initialized entry into that region or a better loss
decay rate than its assumed physical coercivity already gives.

The two singular-response routes independently obtain the same rank-one
limiting state operator, exponentially decaying first input forcing, neutral
state limit, normal limiting second forcing and centered quadratic output
limit. Their different normalized/unweighted residual conventions were
compared, including every factor of sqrt(3). The explicit ambient quartic
path uses bounded directions with the same frozen marks and actual matrix.
Its nonreachability from perturbed initialization is kept as a scope
limitation, not silently assumed away.

## Fresh isolated reviews

Each reviewer started without author history, README, other reviews or
parallel current findings, with a neutral assignment and complete specified
scientific inputs. Each wrote only its assigned report. Root read all
three complete reports and their applicable addenda.

1. correction_matrix_review.md gives PASS for correction_matrix.md,
   frozen SHA256 cec95a18660aa562ed2914d8c2de2d3d0cba7c78822ba6366252d5439b4454aa,
   and the separately authorized correction_initial_rank.md,
   SHA256 17c835025d60ba332860f87d5331edd0136959a12c7b06354eced88eb1efd9d5.
   Both remain unchanged. Its checks include the full derivative and
   first/second trained recurrence, matrix anticommutator in the all-time
   tail argument, all initialized-rank premises and the generic-rank
   Vandermonde addendum. Minor notation ambiguities are identified in the
   review; the synthesis uses xi for normalized error and states the
   initialization-rate qualification explicitly. The generic definition
   domain is not represented as generic convergence.

2. correction_normal_form_review.md gives PASS for the original frozen
   normal-form proof, SHA256
   0344d4526096580cb994b99dddb5b7ab4af8db3049ec7c34fc6abe1fccd4383e.
   Two formal clarifications were applied: inverse degree m>=1; explicit
   L(X0)<=ell and stationarity at zero loss. Its versioned addendum verifies
   that only these edits produced the current hash
   381cf0cc0339e0d87408e3328b6c14c295de1a58841f439d0d170c0d5b0a0d72.
   The review includes an explicit closed-expression induction for
   physical-space coefficient bounds despite the unbounded Gaussian mark.
   Its theorem scope is the current-state certificate, not which prior
   initialized data families have regular endpoints.

3. correction_singular_review.md gives PASS for the stated conditional
   first/second response limits, possible third-order secular coefficient,
   and ambient residual-quadratic obstruction in the two frozen reports.
   Original correction_flow.md hash:
   8c14dfa7337cf573f26a8f4ecc0c7af8a4c368e63835a2949533dc2964f20169.
   Original correction_design.md hash:
   d93ea65f2a6fe5b1929a6b7877bb06e3752319e9e449cb3da8e7bad0fc718cf7.
   Three wording repairs distinguish output decay from a possibly nonzero
   neutral state limit, avoid implying exhibited nonzero actual quadratic
   disagreement, and identify the Hilbert differentiation topology rather
   than sharp response-envelope norms. Current hashes are respectively
   8602bc182425614c916908cb6e5aa791221e204b428b504c51e04c383261da9f and
   3d09ecb900e902f3b1e42b6c74fe57f7da9dbf40dce33b6825222e297efd9efe.
   The report preserves the original proof provenance and identifies the
   verified scope; its versioned follow-up checks the wording repairs.

No blocking mathematical defect remained within those scopes. The reviews
are internal checks, not the separate promotion procedure.

## Additional root corollary and interpretation

Equation (6) of correction_synthesis.md follows directly by applying
Cauchy--Schwarz to Gamma0^(-1/2)n and Gamma0^(1/2)z. Along signed data
approaching (v,v,-v), the fixed vector z=(1,0,1) has nonzero target pairing
but vanishing initialized feature energy. Thus mu0 tends to zero by that
inequality and initialization continuity. Root checked this short
corollary; it is not separately claimed as covered by the isolated review.
It describes a necessary geometry-sensitive coefficient, not an all-time
rate proof.

The authoritative synthesis distinguishes an explicit admissible formula,
exact defect identities, local-residual cancellation, all-time current-state
certification, known initialized neighborhoods, and the unresolved broad
initialized theorem. No third-order secular coefficient or quadratic
output discrepancy has been shown nonzero for an actual canonical seed.

## Workspace integrity

The current canonical and instruction hashes are checked against the
unchanged inputs recorded in rho_hessian_validation.md and the previous
manifest. Only this study's flat source artifacts were written. No
established docs/code, Git index or Git history was changed. Existing
unrelated modifications were preserved. There were no experiments, new
generated trajectories or reopened numerical campaigns.

correction_manifest.sha256 records final current artifacts and their
dependencies, including README. Older manifests retain their historical
README hashes. No approval or promotion is requested for this research.
