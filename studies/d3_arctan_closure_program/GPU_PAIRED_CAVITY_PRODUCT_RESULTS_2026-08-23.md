# Genuine paired-cavity product: GPU results

**Run date:** 23 August 2026.  **Claim level:** preregistered empirical route
evidence only.  The frozen design and decision rule are in
PAIRED_CAVITY_PRODUCT_PREREGISTRATION_2026-08-23.md; the complete aggregation
is GPU_PAIRED_CAVITY_PRODUCT_RESULTS_2026-08-23.json.

## Frozen verdict

The experiment gives **formal empirical support** for the genuine-rerun joint
cavity scaling
\[
 \mathbb E\left\langle
 |R_2^{\rm cav}\{Z_2-Z_2^{\rm cav}\}|^q
 \right\rangle_n=O(n^{-q/2})
\]
for the tested moments and horizons.  It gives no evidence against that scaling.
This verdict is not a theorem and does not upgrade the open proof rung.

Every main cell, step-halving cell, arithmetic cell, and cavity-zero identity
passed its frozen threshold.

## Main width scaling

The recorded statistic was
\[
 J_q(n,s)=\sqrt n\,
 \|R_2^{\rm cav}(s)\{Z_2(s)-Z_2^{\rm cav}(s)\}\|_{q,n}.
\]
The fitted median width slopes and 95-percent replica-bootstrap intervals were:

| feature time | \(q\) | slope | 95% interval | median ratio \(2048/256\) |
|---:|---:|---:|---:|---:|
| 1 | 2 | 0.0054 | [-0.0637, 0.0702] | 1.042 |
| 1 | 4 | 0.0240 | [-0.0536, 0.0864] | 1.085 |
| 1 | 6 | 0.0534 | [-0.0207, 0.1183] | 1.165 |
| 1 | 8 | 0.0692 | [0.0031, 0.1464] | 1.206 |
| 2 | 2 | -0.0007 | [-0.0487, 0.0739] | 1.065 |
| 2 | 4 | 0.0117 | [-0.0399, 0.0860] | 1.077 |
| 2 | 6 | 0.0371 | [-0.0211, 0.0960] | 1.107 |
| 2 | 8 | 0.0656 | [-0.0050, 0.1185] | 1.186 |
| 4 | 2 | 0.0128 | [-0.0523, 0.0852] | 1.051 |
| 4 | 4 | 0.0186 | [-0.0456, 0.0839] | 1.046 |
| 4 | 6 | 0.0272 | [-0.0390, 0.1031] | 1.065 |
| 4 | 8 | 0.0300 | [-0.0277, 0.1237] | 1.064 |

All upper endpoints are below the frozen \(0.15\) threshold, and every ratio is
below \(1.60\).  The modest positive slopes at high \(q\) and time \(1\) are
compatible with finite-width/high-moment bias; the experiment is not large enough
to exclude a rarer asymptotic tail mechanism.

## Numerical audits

- The largest median symmetric relative step-halving discrepancy, over
  \(n=256,512\), all three horizons, and all four moments, was
  \(2.42\times10^{-5}\).
- The largest common-draw float32/float64 discrepancy, over \(n=128,256\), was
  \(5.51\times10^{-6}\).
- In both arithmetic modes, the cavity identities
  \(Z_{2,j}^{\rm cav}=R_{2,j}^{\rm cav}=0\) held exactly in the recorded arrays.

The calculation used a genuine rerun: both the raw incoming row and outgoing
column were zeroed at initialization, and the full cavity learned trajectory was
then recomputed.  It did not reuse learned matrices from the full orbit.

## Evidentiary consequence

The data make a deterministic localization counterexample to the actual canonical
paired cavity less plausible: the unweighted cavity perturbation and its product
with the cavity query retain the predicted \(n^{-1/2}\) scale through \(q=8\).
They do not identify the cancellation that proves this behavior.  In particular,
they cannot distinguish a true signed characteristic estimate from a rare-event
failure beyond the sampled replica count.  The exact learned-history two-time
leaf remains a proof obligation.
