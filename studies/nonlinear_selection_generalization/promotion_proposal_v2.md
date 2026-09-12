# Proposed C.4.10: finite-episode nonlinear generalization

Status: complete reviewed package, ready for user approval. Two fresh complete
scientific reviews and the separate fresh integration review passed with no
required corrections.
No established file has been changed. This proposal requests no broader theory,
model, optimizer, experiment or implementation addition.

## Concrete destination and package

Append [the complete proposed C.4.10](candidate_addition_v2.md) to
`docs/global_nonlinear.md`, after the existing C.4.9. Apply the three concise
coverage additions in [the proposed reading guide](candidate_docs_README_v2.md)
to `docs/README.md`. Preserve every existing chapter byte and every other
established file. There is no new maintained code, empirical result or API.

Exact new-section SHA-256:
`b676a2a446c0d492ad8fa15437a4105aa71cf883c6264392054183c01e09776d`.
Exact proposed full-guide SHA-256:
`d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c`.
The [scientific manifest](scientific_manifest_v2.json) freezes every complete
dependency and guide. The [integration manifest](integration_manifest_v2.json)
identifies the standalone proposed edition and its full-file hashes.

## Scientific result

The result links the selected nonlinear prediction to a target family defined
without the trained network. Input densities cover the entire circle, with
`1/2 <= p <= 2` and a fixed Lipschitz bound. The targets are odd, exactly
anchor-compatible cubic-plus-Fourier functions with a declared weighted
coefficient budget and complexity index. Labels have bounded, conditionally
centered noise. Only added observations are iid; the two known anchors retain
their exact weights.

The package proves:

1. A common positive constrained episode for every bounded Borel added law and
   every empirical law, with full retained Gaussian source history. Original
   fixed-mixture GF reaches this selection at physical time `tau/epsilon`.
2. Continuum residual detection by the projected middle gradient, followed by
   positive conditioning on specified finite target spaces. It does not infer
   whole-function-space coercivity from finite matrices.
3. The nonlinear population bound

   \[
   \mathcal E_\nu(P_\nu(\tau))\le
   e^{-\lambda_N\tau/2}\mathcal E_\nu(F_*)+
   2(1+2L_0^2/\lambda_N)(a_N+LVT)^2(1-e^{-\lambda_N\tau/2}),
   \qquad 0\le\tau\le T.
   \]

   Here `a_N=0` for a target of declared cap N, or
   `a_N <= R/(2N+3)^s` for the weighted infinite-series class. All other
   constants and the admissible duration are specified reference quantities.
   The hidden dynamics remain evolving and nonlinear.
4. Separate finite-sample input and centered-noise errors, followed by an
   explicit stability modulus. At a fixed episode and confidence, this error
   tends to zero as `m^(-1/2) exp(O(sqrt(log m)))`.
5. A class-determined positive stop and finite sample threshold that give
   strict unseen-risk improvement and nonvanishing paired second-hidden
   activation displacement on a robust finite-cap subfamily. The displacement
   observation combines uniform-circle and anchor values.
6. Transfer to actual finite Gaussian-initialized GF, including the actual
   finite Gaussian readout, with width first at fixed sample and positive
   contamination, contamination tending to zero next, and sample size last.
   Mixture and reference networks use the same initial arrays and physical time.

This addresses milestone B at its permitted finite-episode scope. It goes
beyond a positive training-atom gain or a fluctuation theorem, and its input
support is never concentrated near a favorable atom.

## Limits retained in the proposal

The target family is restricted to odd, anchor-compatible functions. The
guarantee has an explicit approximation floor and a finite positive slow
horizon. Conditioning constants are mathematically specified and proved
positive but unevaluated; the resulting stopping time, sample threshold and
margins need not be practically useful. Increasing target complexity can worsen
conditioning and shorten the permitted episode. No universal consistency,
arbitrary-accuracy fitting, all-time changed-law endpoint, simultaneous rate,
raw-GD result, circle-only hidden-motion lower bound, efficient solver or
architectural superiority is asserted.

## Review and deterministic evidence

The independent [relevance report](relevance_report.md) accepted this single
section and minimal guide scope. The original v1 scientific pair did not pass:
one reviewer required an explicit finite-cap hypothesis in the robust subfamily.
That condition is now written out; [the revision record](revision_v2.md)
preserves all original reports and the precise six-line correction. V1 PASS
reports are not used to approve v2.

Fresh complete v2 scientific reviews
[C](scientific_review_v2_c.md) and [D](scientific_review_v2_d.md) both passed,
as did the separate [integration review](integration_review_v2.md). Root read
all original reports in full and verified their provenance and hashes; the
[final review record](final_review_record_v2.md) records the exact accepted
packet and remaining approval boundary. The standalone v2 validation has passed
the exact established rational certificate, elementary algebra and inverse
modulus checks, new labels/fragments and exact preservation of old chapter
bytes. Full generated evidence is under
`data/generated/nonlinear_selection_generalization/edition_validation_v2_20260912_01/`.
These are deterministic checks, not training experiments or a replacement for
the proof audits. The frozen corrected packet and retained v1 reports are
committed as `b384475316cc0e18bab14438f0140f8f2ede6c9a`.

## Approval boundary

The user requested approval of the concrete reviewed addition before any
established file changes. RESEARCH_WORKFLOW.md Part 2.5 independently requires:
“Obtain and retain the user's approval for that reviewed package before
changing established book/code.” The requested approval is exactly the new
C.4.10 and three guide additions identified above. I recommend approving this
package at its declared scope.
After approval, current source hashes and concurrent changes must be rechecked,
the accepted edition applied, and exact candidate-to-live correspondence
verified under the shared Git writer procedure.
