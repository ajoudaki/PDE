# Coordination review correction and bounded offline calibration

This addendum corrects two P3 findings reported by the independent reviewer.
All files and hashes in STAGE2_COORD_FROZEN_MANIFEST.json remain unchanged.
The original random-direction controls used the raw Q returned by Gaussian QR,
without correcting the signs of R's diagonal. Their norms and singular spectra
were correctly matched, but calling those orientations isotropic was inaccurate.
They should be called Gaussian-QR orientation controls. The stronger singular-mode
sign controls preserve both matrix Grams exactly and are unaffected. Neither
registered positive gate uses the affected random-direction controls.

## Precise history-Gram statement

Let Y be the N by p matrix whose rows are recorded history vectors, and let P be
an N by N permutation matrix. Since P^T P=I, the permuted history Y'=PY satisfies

    Y'^T Y' = Y^T P^T P Y = Y^T Y,
    Y' Y'^T = P YY^T P^T.

Thus the coordinate Gram Y^T Y is unchanged, while the time Gram YY^T is
permutation-conjugate. The latter has unchanged eigenvalues, not generally
unchanged entries. The empirical row distribution and all empirical coordinate
moments are unchanged because the rows are only reordered. Centered coordinate
covariances are also unchanged because the mean is unchanged. References to
unchanged unpaired history Grams in the frozen theory mean coordinate Grams;
this addendum disambiguates the stronger and false time-Gram interpretation.

## Corrected Gaussian-QR orientation construction

For an n by n matrix A with independent standard-normal entries, compute any
orthogonal QR decomposition A=QR. Let D be diagonal with D_ii=sign(R_ii), and
put Q_+=QD and R_+=DR. Then A=Q_+R_+, Q_+ is orthogonal, R_+ is upper triangular,
and every diagonal entry of R_+ is positive. The singular event R_ii=0 has
probability zero: conditioned on the preceding independent Gaussian columns,
the next column lies in their proper linear span with probability zero. The
implementation rejects a zero diagonal rather than pretending it is a generic
full-rank draw.

The positive-diagonal QR factorization is unique. If A=Q_1 R_1=Q_2 R_2 with
both positive-diagonal triangular factors, then Q_2^T Q_1=R_2 R_1^(-1) is both
orthogonal and upper triangular. Its first column has only a positive first
entry, which must equal1; orthogonality forces the other entries of the first
row to vanish. Induction on the remaining block gives the identity matrix.
Consequently the two Q and R factors coincide.

For every fixed orthogonal O, OA has the same Gaussian law as A: the joint
column density is proportional to exp(-||A||_F^2/2), preserved by O and its
unit absolute Jacobian. Uniqueness gives Q_+(OA)=OQ_+(A), since
OA=(OQ_+(A))R_+(A) is already a positive-diagonal QR factorization. Therefore
the distribution of Q_+ is invariant under every fixed left orthogonal action;
this is the uniform (Haar) orthogonal orientation construction. No claim of
novelty is attached to it. Independently sampling Q_L,Q_R this way gives
E_new=Q_L diag(s) Q_R^T, where s is the original edit's singular spectrum.
For fixed orthogonal U,V, UE_new V has the same law, using left invariance of
Q_L and of V^T Q_R. Thus the resulting edit distribution is isotropic under
independent left and right rotations, conditional on its prescribed spectrum.

E_new preserves the norm and singular spectrum, including the spectra of
both Grams. It generally does not preserve the two Gram matrices themselves.
Instead E_new E_new^T=Q_L diag(s^2) Q_L^T and
E_new^T E_new=Q_R diag(s^2) Q_R^T. These identities and orthogonality are checked.
The old singular-mode sign controls preserve the complete two Grams and remain
the stronger nuisance control throughout the original inference.

## Calibration protocol, fixed before execution

Use only the12 fixed-support confirmation endpoints and48 primary curriculum
endpoints, all already frozen. Generate five corrected random orientations for
the former reversal edits and one for each of the latter swap/within edits,
matching the original control counts exactly:156 corrected directions total.
Reuse each original deterministic control seed and the exact same Gaussian
matrices. Consume the preceding unused sign draw to align the generator stream
with the old controls; correct only the two QR diagonal-sign conventions.
No target, score or direction is selected. Recover the old random control from
those same Gaussian draws and verify its saved score before comparing the new
one. All training fits, stronger sign controls and primary gate values remain
unchanged; this calibration performs no training.

Use float64, one CPU thread, TF32 off, GPU1, at most5 GPU-process minutes.
Require relative orthogonality, QR reconstruction, norm, spectrum and Gram-form
identity errors <=1e-9; old-control replay score discrepancy <=1e-10. Check
history-coordinate/time-Gram statements and positive-QR orthogonal equivariance
with deterministic small oracles. Save all new train/validation/test metrics,
predictions, input/source hashes and completion status in the fresh generated
namespace stage2_coord_haar_calibration01. Report old/new signed effects as a
control calibration; no changed random-control effect can upgrade a primary
gate whose defining statistics are untouched.

## Executed calibration and consequences

The full offline calibration completed in51.036 GPU-process seconds, with
zero new training fits. All156 corrected directions on60 frozen endpoints
passed. Replaying each original Gaussian-QR control from its original random
stream reproduced every checked saved train/validation/test MSE exactly
(maximum difference0). Thus the calibration isolates QR sign normalization,
rather than an endpoint, data, seed, precision or implementation mismatch.
The maximum norm/spectrum/orthogonality/Gram-form relative error is1.30e-13.
The deterministic history-coordinate/time-Gram and positive-QR equivariance
checks have errors below8.26e-16.

The following entries are percentage changes in held-out MSE relative to the
same frozen untouched endpoint. Negative means improvement. For fixed support,
aggregate by the median of five orientations at each endpoint, then the median
of the four seeds. For each curriculum schedule/edit there is one orientation
per endpoint, followed by the median over four seeds, preserving the original
control counts. These small samples are a calibration, not a high-precision
estimate over all orthogonal orientations.

| Fixed-support domain | Original Gaussian QR | Corrected Haar |
|---|---:|---:|
| Fashion | -0.001581% | +0.003128% |
| Housing | +0.001108% | -0.000189% |
| HAR | +0.012764% | +0.031568% |

| Curriculum/domain | Swap: original -> Haar | Within: original -> Haar |
|---|---:|---:|
| Fashion joint | +0.03924% -> +0.02069% | +0.00174% -> -0.00311% |
| Fashion AB | +0.04630% -> +0.01462% | +0.03342% -> -0.03272% |
| Fashion BA | -0.02195% -> +0.05541% | -0.05103% -> +0.01950% |
| Fashion alternating | +0.05193% -> +0.00947% | +0.01947% -> -0.01510% |
| Housing joint | +0.00887% -> +0.00248% | -0.00013% -> -0.00199% |
| Housing AB | -0.02680% -> -0.06308% | -0.01535% -> +0.00486% |
| Housing BA | -0.03066% -> -0.01544% | +0.00710% -> -0.01284% |
| Housing alternating | +0.01062% -> -0.00804% | -0.00557% -> -0.00456% |
| HAR joint | +0.09423% -> +0.11339% | -0.05750% -> +0.01175% |
| HAR AB | +0.09751% -> +0.09284% | -0.06620% -> +0.01669% |
| HAR BA | +0.08302% -> +0.09103% | -0.01946% -> +0.00700% |
| HAR alternating | +0.09370% -> +0.10482% | -0.06930% -> +0.01437% |

Several signs change, so the original orientation distribution should not be
silently treated as equivalent. Across curriculum domain/schedule aggregates,
the largest corrected absolute median is0.11339%. The largest change between
old and corrected signed effects for an individual direction is0.77403 percentage
points; aggregate smallness does not imply every draw was identical or negligible.
The new controls remain much weaker than the originally preserved learned-axis
sign controls in the salient comparisons. This is consistent with the earlier
warning that random singular directions are insufficient to identify coordination.

All registered primary gate values are mathematically unchanged: fixed-support
success depends on reversal, the exact-Gram sign controls and nonlinear gradient
remainder; curriculum success depends on swap/within exact-Gram contrasts,
centered residual and phasewise q1. None uses these affected random-direction
scores. No primary claim was rerun, upgraded or rescued by this calibration.
The existing negative conclusions remain in force. This correction supersedes
the word “isotropic” and its associated random-control numerical interpretation
in the old reports, while preserving their valid matrix-spectrum matching and
stronger-control conclusions.

## New evidence and preservation

Source: stage2_coord_haar_calibration.py, SHA256
`ff20bd36ecaeeebc68e40b96cc4ac11134fd0864a131f3be2d0c0f847e0fc819`.
The fresh generated stage2_coord_haar_calibration01 directory contains the
pre-execution correction/protocol snapshot, source snapshot, manifest, all156
old/new score pairs, all new and replayed test predictions, checks, input hashes,
summary and completion record. Summary SHA256 is
`7215aa48c8ee7b0c89b36cc5b644ee6be8f50d0c5cdd771295341717184c1dd9`.
The exact command is retained in its manifest; choose a fresh output path to
repeat it. Current addendum results were appended after that protocol snapshot.

Every file listed in the original freeze was verified before and after execution.
The original freeze SHA256 remains
`44f42c0fa58dfeb0600a23d1cc55c06c83d4342aaabd9cadb9a64b5dd6fc0359`.
No frozen source, theory, protocol, report, endpoint, primary summary or data
array was rewritten. This is an author-checked repair/calibration responding
to the two reviewer findings, not a new independent review or a promotion.
GPU1 is released. No training is authorized by this addendum.
