# Passive point diagnostic for the finite scalar closure

2026-09-25. User-authorized continuation of the scalar implementation test.
Frozen before implementation or scientific runs. The question is whether the
scalar compression itself predicts a passive test input accurately when Fourier
readout and angular quadrature are entirely removed.

Use the same canonical network and literal two-input task as the preceding
Fourier test: width 16, three hidden tanh layers, seed 20260920, normalized circle
training angles 10 and 125 degrees with labels +1,-1, mobilities (n,1,1,n),
mean squared training loss, and P=1 original residual-activity history closure.
The single passive input is fixed in advance at 60 degrees. It has no label or
loss contribution; M remains 2 and the activity clock and all history A/B sources
use the two training residuals only. This test direction was not selected from
a new point/seed search. It is an interior nontraining point.

Implement an ordinary connected-tree scalar dictionary seeded with both training
outputs and the passive output, all of grade 3. The appended input gets passive
activation species at each layer; its first-layer velocity uses its input Gram
against the training inputs. No query histories, angle vertices, Fourier tags,
Fourier blocks or quadrature are present. Initialized matrices enter exact
initial contraction values. Runtime contains scalar states/coefficient tables
only. Reuse the previously checked exact response templates and whole-monomial
cutoff rule. This remains the unsaturated practical truncation.

H1: the direct point scalar predictor agrees with the matched dense fitted
predictor to absolute error <=0.05. H0: aggregate truncation itself still gives
error >=0.10 or fails to fit. Intermediate error or a numerical/resource failure
is inconclusive. A point success does not establish whole-circle accuracy.

Fit fresh dense and population-P1 references and scalar cutoffs K=5,7, in that
order. Larger K is attempted only if K=5 compiles. Maximum per dictionary:
6000 patterns, 2000000 retained terms, 120s compilation, 2 GiB process RSS.
These larger limits permit a fair point diagnostic without the old 200000-term
cap; all capped outcomes are retained. No additional orders or task/seed search.
Each solve has 120s wall limit, horizon40, target training MSE0.001, float64
DOP853 with rtol1e-7, atol1e-9; stop excessive/nonfinite states (>1e8 absolute).
Budget for all integration/compilation phases is 10 minutes. Algebra checks
have a separate 120 CPU-second budget.

Primary score compares each fitted model's point prediction at its own first
training-target crossing with the dense reference's own fitted point prediction.
Also report matched-physical-time errors against dense and population reference,
training output vectors, fit times, largest training-trajectory discrepancy,
state/term counts, preparation/integration times and all failures. References
continue through40 so no time extrapolation is used. Save full scalar checkpoints
and a fixed temporal panel of training and point outputs.

Before training check: exact passive template versus direct population chain
rule at nonzero histories; whole-monomial truncation/evaluation; same-input
passive readout versus corresponding training-output coordinate under relabeling;
training equations unchanged when the point is added; label/clock exclusion;
zero-residual stationarity and runtime autonomy. Numerical same-input control
can use derivative tests, without an extra training campaign.

For the highest successfully fitted scalar order, repeat at rtol1e-9,atol1e-11
in a fresh cell; refine both references once. Required final point change<=0.002.
Reproduce the K5 training-only scalar system once (no query root) to the primary
K5 stopping time, comparing training outputs to K5-with-query on a common time
panel (difference gate1e-5). This is the causal no-feedback control and has the
same resource caps. No Fourier solver is run in this experiment.

Stop after the stated runs/branches. A low-order failure does not disprove the
aggregate identities or the separate saturated convergence theorem. Report it
without presenting a fitted loss as evidence for a fitted test function.

Source goes in this study's flat directory, products in the fresh
data/generated/neural_response_memory_20260922/scalar_point01/ namespace.
Record source/configuration hashes, failures, raw arrays, check results and
reproduction instructions. Root owns protocol, runner and report; point_probe
owns scalar_point_engine.py; point_audit owns check_scalar_point.py and its
audit report. Existing Fourier/source artifacts are read-only inputs.
