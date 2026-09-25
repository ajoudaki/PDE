### Executed scalar-only aggregate test (2026-09-25)

The user authorizes implementing and testing the aggregate-only idea. The
[new derivation](SCALAR_AGGREGATE_CANDIDATE_THEORY.md) constructs scalar
output/kernel derivative tensors directly from dense gradient flow, with a
frozen highest derivative. It is a new observable closure, not an exact
collapse of the P-history population model. After a one-time initialized
network calculation, its RHS retains no neurons or dense matrices. Order 4
uses 84 evolving scalars plus 256 fixed coefficients for four samples, or
584 plus 4096 for eight samples; initialization copies and labels are counted
separately. Root owns the protocol, runner, reproduction, results and this entry;
aggregate_criterion_check owns engine/tests, scalar_candidate_theory owns
derivation/analysis, and scalar_execution_design owns independent checks.

The [frozen protocol](SCALAR_AGGREGATE_PROTOCOL.md) tests three hidden tanh
layers on the four-input mixed and eight-input alternating circle tasks,
widths 128/256 and two seeds, against fresh dense dynamics at identical physical
times through 128. All 64 primary runs finish and numerical gates pass; no
conditional refinement or horizon extension is triggered. Nevertheless,
order 4 fails the practical-accuracy criterion in all 8 configurations:
maximum sampled prediction RMS errors are 0.414--0.895, versus a 0.1 agreement
threshold. Early-time agreement and final fitting on the four-input cases
do not repair the incorrect training trajectories. Dense hidden features
move substantially. The scalar kernel becomes indefinite in 6 of 8 cases.

[Full results](SCALAR_AGGREGATE_RESULTS.md) retain all cases, error definitions,
costs, limitations, commands and artifacts. Seven unit tests, 82 independent
derivative checks and 2294 saved-run/reproduction checks pass. Recomputed scalar
coefficients and repeated trajectories agree bitwise; own-state restart
prediction RMS differs by at most 4.63e-8. These checks validate the implemented
candidate and its adverse empirical result, not general scalar compressibility.
The primary campaign takes 66.565 measured wall seconds on one CPU worker;
new products use this study's scalar_aggregate_* namespaces. No further model
tuning was run, and no maintained source, promotion or Git index was changed.

### Scalar closure as a full-circle endpoint predictor (2026-09-25)

The user replaces the training-trajectory criterion with agreement of final
functions across the entire circle. The [endpoint protocol](SCALAR_CIRCLE_ENDPOINT_PROTOCOL.md)
preserves the same scalar training closure and adds passive probe outputs:
training-only cross derivatives and a finite scalar integral state give an
every-angle readout. Mode-64 Fourier coefficients store its angle dependence;
neuron populations are absent after initialization. The
[mathematical check](SCALAR_CIRCLE_ENDPOINT_THEORY_CHECK.md) derives the ordered
readout and separates finite Fourier accuracy from the training closure.

The [completed results](SCALAR_CIRCLE_ENDPOINT_RESULTS.md) compare each model
at its own detected training-MSE 1e-6 crossing, capped at physical time 2048.
All four mixed-label configurations fit, but order-four full-circle RMS
differences are 0.1778--0.2053, about 20--23% relative to dense-function RMS.
No cell meets the predeclared 0.1 agreement threshold; three are intermediate
and one is adverse under the protocol. On the four alternating-label cases,
dense fits but both scalar models hit the time cap. Order-four training losses
remain 0.626--0.731, so these cases have no matched fitted-endpoint verdict.

All 48 primary trajectories finish with a fitting event or declared time cap.
Integration, angular-quadrature and Fourier checks pass without conditional
refinement. Ten deterministic probe-engine tests pass; independent analysis
checks 645 metrics/receipts/Fourier/reproduction items. One fresh six-trajectory
configuration reproduces its saved scientific arrays. The
[audit](SCALAR_CIRCLE_ENDPOINT_AUDIT.md) retains independent implementation,
state reconstruction, cancellation and reproduction checks. The primary
campaign takes 116.687 seconds and reproduction 2.412 seconds on one CPU worker.
Generated products use scalar_circle_endpoint_* namespaces; final figures
are in scalar_circle_endpoint_analysis01. Prior trajectory findings remain
valid for that earlier observable and do not by themselves imply the endpoint
result. Tolerance-defined stops are not claimed as infinite-time limits.

Root owns protocol/runner/report/this entry; circle_probe_engine owns the
passive engine/tests; circle_probe_theory_check owns theory and independent
audit (1194 checks passed); circle_endpoint_analysis owns analysis/figures. The bounded continuation
is complete. No additional model tuning, maintained-source edit, promotion
or Git-index action occurred. Concurrent activation work remains separate.

### Efficient long-time scalar training (2026-09-25)

The user requests diagnosing and countering slow scalar training computation
so final circle functions can be compared at similarly low training loss.
The [protocol](SCALAR_LONG_TIME_PROTOCOL.md) preserves the original frozen-Q
flow and initialized coefficients, extends physical time to a maximum1e9,
uses an implicit solver with an exact sparse Jacobian, and resets local
scalar integral coordinates with exact passive coefficient transport.
No neuron populations, dense trajectory refresh or preconditioned training
law is introduced. The frozen-kernel control is evaluated analytically.

All four eight-input order-four cases now fit to MSE1e-6 at physical times
51,729--79,016, about348--467 times their dense fitting times. Fine scalar
continuations from2048 take5.93--11.75 seconds each; one fresh scalar run from
timezero takes12.32 seconds. These timings exclude original coefficient
initialization and are not an accuracy-matched speed benchmark. Poor kernel
conditioning and residual alignment with its weakest direction explain the
slow physical learning; implicit stepping makes that evolution practical.
The earlier time2048 caps do not indicate permanent inability to fit.

The [results](SCALAR_LONG_TIME_RESULTS.md) separate this successful fitting
from function accuracy. Direct full-circle RMS discrepancies are60.77--99.44
after matched training loss. All integration and quadrature gates pass; one
case has a fully qualified adverse endpoint verdict, while three retain
numerically inconclusive encoded-function verdicts because the strict
Fourier readout gate fails. Encoding errors are tiny relative to the direct
disagreement. The order-two control also fits at much longer physical times,
with worse circle errors. This result concerns the tested scalar candidate,
not all possible aggregate closures.

Six deterministic engine tests and2,903 independent implementation/replay
checks pass. Required first-case Radau and fresh-from-zero BDF checks agree.
The [audit](SCALAR_LONG_TIME_AUDIT.md) retains all qualifications and numerical
diagnostics. All ten research integrations fit; no conditional trajectory or
quadrature refinement is needed. The campaign takes116.89 seconds below the
1800-second budget. New products use scalar_long_time_* namespaces; final
figures and the endpoint table are in scalar_long_time_analysis01.
Root owns protocol/runner/results/this entry, long_time_scalar_design owns
engine/tests/analysis, and eight_input_fitting_check owns independent audit.
The bounded continuation is complete; no maintained-source edit, promotion
or Git-index write occurred. Concurrent activation work remains separate.

### Authorized width-2048 scalar comparison (2026-09-25)

The user requires dense width at least2048 and explicitly requests GPU dense
training. The [protocol](SCALAR_WIDE_PROTOCOL.md) freezes a corrected-scale
repeat of the same two scalar tasks and two seeds, all three hidden layers
at width2048, unchanged canonical dynamics and matched MSE1e-6 endpoints.
The previous widths128/256 remain finite-width implementation diagnostics;
they do not decide the intended large-width question. A single larger width
also does not establish convergence to a population limit.

The completed [results](SCALAR_WIDE_RESULTS.md) give order4 circle RMS
.17476/.17047 on the four-input task and39.274/63.811 on the eight-input task.
All models fit MSE1e-6; both solver refinements, passive checks, circle
quadrature and mode64 Fourier readouts pass. Fresh first-hard-case coefficient,
dense and scalar reproduction agrees exactly. Order4 improves over order2
by4.09x/3.03x on eight inputs but remains far from the dense learned function.
The [audit](SCALAR_WIDE_AUDIT.md) retains independent implementation and replay
checks. Generated tables and three figure pairs are in scalar_wide_analysis01.

Root owns protocol/campaign/results/this entry; long_time_scalar_design owns
the exact initialization optimization/tests/analysis; scalar_wide_dense_gpu
owns the GPU dense adapter and tests; eight_input_fitting_check owns independent
checks. This bounded stage is complete. No population-limit, accuracy-matched
speedup, maintained-source or promotion claim is made.

### Authorized scalar orders five and six (2026-09-25)

The user requests orders5/6 on the eight-input experiment to test whether
whole-circle accuracy improves further with closure order. The frozen
[protocol](SCALAR_HIGH_ORDER_PROTOCOL.md) retains both width2048 seeds, the
same audited GPU dense endpoints and MSE1e-6 comparison, and exact ordered
initialized derivative coefficients. It sets numerical, reproduction and
resource gates before higher-order research runs. Training remains a scalar
ODE without neuron populations. Higher orders increase sample-index tensor
size; no monotone accuracy or convergence claim is assumed.

The bounded higher-order campaign is complete; see
[results](SCALAR_HIGH_ORDER_RESULTS.md). Both order5 seeds fit MSE1e-6.
Their circle RMS values are40.63438 and63.35941, compared with order4's
39.27422 and63.81087. The first direct-grid comparison passes refinement
and consistency gates and is3.46% worse. The second remains diagnostic:
its passive-training gap1.6321e-4 exceeds the1e-4 gate, so its nominal0.71%
gain is not qualified. Strict Fourier encoding is a separate reported gate.

Order6 develops loss growth and then solver failure in both seeds, with
no matched-loss test endpoint. Earlier negative effective kernel rates
agree across tolerances; terminal losses are not converged. This supports
a failure of these executions, not a finite-time blowup or general
impossibility theorem. Fresh original coefficients and first-seed order5
fit/order6 failure reproduce exactly. Both predeclared order5 additional
tolerance runs were used; no further numerical or scientific branch is open.
The [audit](SCALAR_HIGH_ORDER_AUDIT.md) passes3,671 independent implementation
and saved-data checks; scalar_high_order_analysis01 contains the full table
and four figure pairs. The recorded active-work subtotal is579.50 seconds. The
[parity note](SCALAR_HIGH_ORDER_PARITY.md) proves exact order5-to-order4
reduction at zero readout; small nonzero initial odd tensors alone supply
no long-time error guarantee.

Root owns protocol/runner/results/this entry; scalar_wide_dense_gpu owns
exact ordered GPU initialization, its independent small multijet oracle
and parity note; long_time_scalar_design owns the generic hierarchy,
structured implicit solver and analysis; eight_input_fitting_check owns
the scoped internal audit. New generated products use scalar_high_order_*
namespaces. No maintained-source, promotion or Git-index write occurred.
Concurrent activation work below is preserved.

