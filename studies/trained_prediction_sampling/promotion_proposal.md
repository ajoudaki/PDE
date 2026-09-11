# Proposed C.4.8: sampling fluctuations of the trained prediction

Status: complete reviewed version-2 addition; both fresh complete proof reviews,
standalone validation and the fresh integration review PASS with no unresolved
objection. Version-1 integration corrections are fully resolved. Explicit user
approval of this exact package is the remaining promotion gate; this proposal
does not itself authorize established book/code edits.

## Concrete addition

Append [proposal_C4_8_v2.md](proposal_C4_8_v2.md) as C.4.8 of
`docs/global_nonlinear.md`, and apply only the three exact coverage-summary
replacements in [promotion_edits_v2.json](promotion_edits_v2.json): one in that
chapter's C.4 introduction, and two in `docs/README.md`. No maintained code API
or experiment is proposed. The unchanged established sections remain the
canonical dependencies.

The frozen mathematical addition has SHA256
`98fa7614b6449b58b07c65df047b68a3484bf0760b36a3a25052f67d72692928`.
The edit specification has SHA256
`50a95f4576c56c1438974a76da25a793ebe188e39c00e2f98f79bd79cb294f2c`.

## Scientific result

Use exactly C.4.7's actual two-hidden-layer tanh model, initialization,
population carrier and physical GF, at T=40. The smaller radius is
delta'_Y=delta_Y/4, independent of width and sample count. For every separately
fixed Borel training law in this ball, including correlated and nonatomic laws,
the addition proves the requested A--C and the separate mean-square strengthening.

The signed observation influence is a bounded continuous function of the
labeled observation with values in continuous circle predictions. It is the
actual contamination derivative and is centered under the training law. Its
usable characterization differentiates the exact population Gaussian Euler
recursion, including both trained hidden layers, the middle increment, residuals,
both Gaussian covariance families, and the actual forward/adjoint response
coefficients. The derivative limit is independent of meshes and finite-law
quantizations. It agrees with the existing C.4.6 response at the reference law.

Let H be L2 of normalized circle arc length. With the explicit extension
Fbar(Q)=F(Q) on U_Y and zero outside U_Y, the theorem proves

\[
 \overline F(\mu_m)-F(\mu)
     =\frac1m\sum_{i=1}^m I_\mu(Z_i)+r_m,
 \qquad m\,\mathbb E\|r_m\|_H^2\longrightarrow0.
\]

Thus the limiting fluctuation is the centered H-valued Gaussian with covariance

\[
 \Sigma_\mu=\int I_\mu(z)\otimes I_\mu(z)\,d\mu(z),
 \quad
 \langle\Sigma_\mu g,h\rangle
 =\int\langle I_\mu(z),g\rangle\langle I_\mu(z),h\rangle\,d\mu(z).
\]

The mean square of the entire prediction error equals
Tr(Sigma_mu)/m+o(1/m). The requested width-first finite-GF distributional bridge
also holds with sampling independent of the actual random initialization.
Empirical laws outside the construction neighborhood have exponentially small
probability; the finite-width bridge never assumes a width limit on that event.

The new analytic estimate is a uniform bound on first and mixed second
observation-weight derivatives of finite population Euler predictions. Its
short-time proof subtracts the old lower feature before contracting covariance
changes involving new source coordinates. The resulting interval-length factor
closes feedback uniformly in mesh, support size, minimum mass and covariance
rank. Replacement differences then control the higher Hoeffding terms without
an empirical total-variation approximation.

## Scope and limits

The model and physical horizon remain exactly those of C.4.7. The radius is
positive but no practical numerical lower bound is claimed. Statistical
conclusions are for each fixed admitted law; there is no asserted uniform
sampling rate, finite-width rate, simultaneous scaled width/sample limit,
finite-network tangent theorem, GD extension, infinite-time endpoint, or
nondegeneracy of the covariance. The Gaussian limit is in H, not the circle
supremum norm. The test-circle measure introduces no teacher labels.

## Checks and review record

- Independent relevance/placement selection: accept for assembly as C.4.8;
  [full report](selection_report.md).
- Internal proof checks: [complete record](internal_checks.md), including the
  independent source-feedback reconstruction and exact Borel-kernel passage.
- Fresh paired proof reviews: [review A](review_v2_A.md) and
  [review B](review_v2_B.md) both PASS for the complete frozen
  [version-2 packet](review_packet_v2.md), with no required corrections or
  missing inputs. The coordinator read both complete reports and verified their
  frozen sources and check outputs. Earlier reports and all correction resolutions
  are preserved in the [resolution record](review_resolution.md).
- Standalone edition: PASS. Exact inverse preservation, 88 unique equation
  tags, new navigation link, six Gaussian-calculus identities including rank
  loss, and 748 exact sampling identities passed. Full report:
  `data/generated/trained_prediction_sampling/standalone_v2/validation_report.json`.
- Fresh integration review: [complete report](integration_v2.md), PASS for the
  precise [version-2 integration scope](integration_packet_v2.md), with no
  required correction. The coordinator read it completely, verified its frozen
  inputs, fresh assembled edition and independent deterministic checks. The
  finite normalization check covered all 18 velocity components of one fixed
  network state; no training trajectory was computed.

The standalone proposed documents are under
`data/generated/trained_prediction_sampling/standalone_v2/docs/`.
Validation uses only necessary documents, complete required dependency excerpts,
and isolated standard-library checks. It does not claim a whole-book proof,
exporter, old-link, or unrelated-code audit. No training experiments were run.

I recommend approving this exact addition. It resolves the sampling fluctuation
milestone beyond the book's existing nearby-law trajectories and reference-law
response, includes the stronger population mean-square conclusion, and preserves
the requested model and limit order. The substantial proof includes its own
source-response and statistical arguments so the theorem does not depend on
unpromoted study material.

The remaining step is the user's explicit approval of this exact reviewed
package under Part 2 of RESEARCH_WORKFLOW.md. Approval covers only the appended
C.4.8 and the three specified summary replacements in the two destination
documents. No code change is proposed. The live established files have not been
changed, and no approval has yet been received.
