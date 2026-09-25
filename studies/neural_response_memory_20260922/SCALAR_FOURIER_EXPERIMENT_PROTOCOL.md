# First implemented scalar Fourier experiment

2026-09-25. Frozen before implementation and experiments. Continuation explicitly
requested by the user. This tests the construction in SCALAR_CIRCLE_FUNCTION_READOUT.md;
it does not assume that its convergence theorem implies a useful small cutoff.

## Decision and model

Can a finite autonomous aggregate ODE learn a whole-circle Fourier predictor close
to the matched dense network, with no neuron population or angular grid during
its time evolution? H1: a computationally accessible aggregate cutoff succeeds.
H0: discarded aggregate interactions prevent useful agreement or fitting. A
resource ceiling or unresolved numerical error is an inconclusive outcome.

Use three hidden tanh layers, width 16, normalized circle input U=(cos theta,sin
theta), no biases, seed 20260920, and canonical mean-squared-loss gradient flow
with mobilities (n,1,1,n). The two training angles are 10 and 125 degrees, labels
+1 and -1: a two-point subset of this study's two_clusters_grouped task. There
is no specified whole-circle target; the dense fitted output is the reference.
This small width preserves trainable internal matrices, initialized-matrix
correlations, history truncation, nonlinear gates, and angular generalization.
It does not test a wide-network limit or computational speedup.

Use the original residual-activity clock, parent history order P=1. Scalar
compilation uses exact product-rule templates, normalized initialized edges,
connected training trees and common-angle forests, and whole-monomial deletion
at size cutoff K. Retain training outputs and circle Fourier output. The energy
observable is optional when K>=8; omit it from the first runtime dictionary if
it causes a resource limit, and report that choice. This experiment uses the
unsaturated reference truncation, stopping on excessive states, rather than
claiming the theorem's globally bounded saturated implementation.

Fourier bandwidth J=8 (17 real weight blocks); all blocks share one pattern list
and generator. Initial angular integrals use 256 uniform nodes. These nodes are
preprocessing only. Training feedback uses the training-output aggregates, not
evaluations of the truncated Fourier series. No dense trajectory, parent
trajectory or neuron array may be accessed by the scalar RHS.

## Runs and controls

Compile reachable scalar dictionaries in the predeclared order K=5,7,9,11.
Stop larger-K compilation after a size or time cap is reached. Preserve each
failure. Maximum per dictionary: 4000 training plus angular patterns, 200000
retained generator terms, 120 seconds compilation, and 2 GiB working memory.
Do not fit a different dictionary to the dense answer. Exact zero initial fields
are not a license to delete variables whose derivatives may be nonzero.

Fit dense, parent P=1 and every successfully compiled scalar system. Use float64
adaptive integration, physical horizon T=40, target training MSE=0.001, rtol=1e-7
and atol=1e-9. Each fit has a 120-second wall budget. A scalar state exceeding
1e8 in absolute value or nonfinite state stops that run and is reported. Primary
comparison uses each model's first target crossing; also report matched-time
scores if a fit fails or the crossing times differ appreciably. Save solutions
at diagnostic times and final states, not only summary metrics.

Evaluate dense and parent predictors on 4096 uniform angles solely for scoring.
Evaluate the scalar Fourier polynomial on that same grid. Report absolute RMS
and maximum discrepancy, normalized RMS using the dense circle RMS, training
RMS, Fourier-versus-training-readout discrepancy, fitting times, scalar state
counts, retained/dropped term counts, compilation/initialization/solver time.
Compare parent against dense separately to expose history-order error.

Pass: both models reach training RMS <=sqrt(0.001), scalar-versus-dense circle
RMS <=0.05, and all numerical gates pass. Fail: the fit is numerically resolved
but fails to fit by T or has circle RMS >=0.10. Intermediate errors and invalid
numerical gates are inconclusive. These thresholds concern labels of magnitude
one and this witness only; no hierarchy convergence or universal claim follows.

## Validation and branches

Before training, verify template derivatives against the population reference
at small nonzero states, including initialized-edge transpose actions and
same-angle factorization. Test the compiled truncated derivative against a
direct evaluation of the exact retained terms. Check scalar RHS autonomy by
ensuring it has no runtime neuron arrays or angular query fields.

For the highest successfully fitted cutoff only, repeat initialization with
512 nodes and integration with rtol=1e-9, atol=1e-11. Refine the dense and parent
reference integrations similarly. Changes in final circle RMS/predictions must
be <=0.002 to call the primary outcome resolved. Score the dense/parent final
Fourier tail beyond J to distinguish spectral and dynamical errors. If that
tail RMS exceeds 0.01, evaluate the SAME hierarchy with J=16 once; this changes
readout resolution only. No other seed, geometry, label, architecture or cutoff
search is part of this experiment.

Total numerical campaign budget: 20 minutes of process wall time, maximum four
primary scalar fits, three numerical refinements and one bandwidth follow-up.
Compiler/debug algebra checks are limited to 10 additional CPU minutes. Stop
after this protocol regardless of result. Correct implementation bugs, preserve
invalidated run metadata, and rerun affected protocol cells only; do not treat
bug repair as a new scientific search.

## Artifacts and interpretation

Implementation stays in this flat study folder. Fresh generated products go
under data/generated/neural_response_memory_20260922/scalar_fourier01/ and
subsequent explicitly named validation directories. Record configuration,
commands, source hashes, raw predictions, failures and numerical diagnostics.
Update the study README and write a report distinguishing exact implemented
identities, finite-cutoff empirical accuracy and remaining theoretical claims.
