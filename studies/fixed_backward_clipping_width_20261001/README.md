# Fixed backward clipping and width error

Started 2026-10-01. User asks whether some fixed positive backward-clipping threshold makes a root-width error theorem possible. This changes the training rule and is a separate investigation from the unclipped width theorem and the intrinsic q=1 learning study.

Latest result: [explicit cap dependence permits growing smooth clipping
levels](M_LOG_SCALE_RESULT.md), with a
[combined internal proof check](M_LOG_SCALE_CHECK.md). One fixed small
label vector works for all M>=1. The full all-time population RMS bound
on the initialized fitting event is C exp(CM)/sqrt(n), for
n>=C exp(CM), and gives the corresponding unconditional fixed-confidence
statement. In particular M(n)=sqrt(log(e+n)) gives n^(-1/2+o(1)).
The target is the own population at the same cap. A cap-independent
C/sqrt(n) constant and comparison with one unclipped target remain open.
The earlier [fixed-cap theorem](SMOOTH_RESULT.md) and its
[check](SMOOTH_THEOREM_CHECK.md) are retained. The hard-clip rate question
and all-initialization all-time mean-square formulation remain unresolved.

## Contract

Primary model: the current paper's two-hidden-layer tanh q=1 closure, canonical independent Gaussian read-in and fixed mixer, zero readout and value memories, constant initial forward prefix, residual-RMS clock. Clip backward responses coordinatewise at a deterministic fixed M>0, before multiplication by the residual; define any alternative clipping location explicitly. Keep the actual mixer and its transpose. The principal desired result is all-time prediction error to the clipped system's own population predictor of order n^(-1/2), at fixed confidence, or in a stated RMS sense. Establishing only concentration around a width-dependent mean does not meet that target. Comparison to the original unclipped target is a distinct question with clipping bias. M=0 freezing of feature learning is excluded as a solution to the intended question.

The paper's fixed-depth finite-data small-label setting and positive initial Gram margin are the initial sufficient regime. Do not claim a result for unscaled ±1 labels without proving it. q=1 fixed-order population identification is itself part of the proof obligation. Dense-flow statements may be used only as explicit comparisons and cannot substitute for the closure target.

## Inputs and process

Scientific proof inputs are the current manuscript and its included mathematical material, maintained docs/ and their complete relevant dependencies, and this study's own derivations. Other studies are not proof inputs. The coordinator had reviewed the unclipped width study before creating this new investigation; no theorem from that study is assumed here. Fresh delegated attempts receive only the current paper, selected maintained sources, and the exact assignment.

HEAD at start: 690e3d4f56ca7ecbad37bb6bacb757b8cfff7682. Existing dirty PDF and concurrent files are preserved. No manuscript edits, Git mutations, training experiments, or promotion are authorized or planned. Required mathematical proof and conjecture-investigation skills apply.

## Work assignments and evidence

The coordinator owns this README, [RESULT.md](RESULT.md), and [FITTING_AND_THRESHOLD.md](FITTING_AND_THRESHOLD.md). Fresh scoped routes produced [CLIPPED_POPULATION_ROUTE.md](CLIPPED_POPULATION_ROUTE.md), [CONCENTRATION_ROUTE.md](CONCENTRATION_ROUTE.md), and [THRESHOLD_ROUTE.md](THRESHOLD_ROUTE.md). Routes started without each other's derivations; later coordinator messages and threshold cross-check exposure are disclosed in the notes. A fresh scoped reviewer completed the main three proof checks in [REVIEW_CHECK.md](REVIEW_CHECK.md), supporting the partial results with the population-rate gap explicitly retained.

## Result for hard clipping

For every fixed hard backward clipping threshold M>0, including M=1, sufficiently small fixed labels and a positive initial readout-Gram margin give:

- Global finite-width fitting and convergent states, with explicit cap-independent sufficient conditions.
- A unique own clipped population evolution and qualitative all-time prediction convergence.
- All-time root-width fluctuations around the finite-width conditional mean on an initialization event with failure at most C/n. The squared integrated time-sup error is at most C_M,mu/n for a fixed query law with finite fourth moment; circles and spheres are included.

The exact q=1 normalization is k=bar(h)/tau and v=-2bar(delta). Clipping is recursive hard clipping of the post-gate backward signals before residual multiplication. No learned dense middle matrix has been introduced. An initial soft-clipping mismatch in the concentration draft was corrected before final checking.

The complete requested root-width bound to one fixed population predictor remains **open**. The remaining term is the deterministic difference between the finite-width conditional mean and the unique clipped population predictor. It converges to zero, but its root-width rate is not established. The continuation below now bounds it by C_mu(Y/n+Y^3), which has a nonvanishing remainder at fixed label RMS Y. Concentration alone cannot replace the missing width estimate. No positive clipping bias relative to the original system, or counterexample to the own-population root-width conjecture, is asserted.

The explicit fitting proof gives ||w||_infinity<=2Y/lambda. Therefore M>=2Y/lambda makes the top clip inactive; M=1 suffices under its displayed small-label condition. The lower cap can be active. M=0 freezing is excluded as a substantive answer.

## Checks and remaining work

The coordinator read the complete route notes and checked model normalization, residual kernels, activity bounds, the all-time velocity-extension concentration argument, and the distinction between conditional means and the population target. The threshold route independently checked the complete fitting proof and constants. The fresh main-proof review is linked above; results are internally checked research material, not promoted book or manuscript claims.

No experiments, code, numerical reproduction, Git writes, or manuscript edits were performed. The primary current manuscript hashes remain unchanged. The next decisive mathematical obligation is a root-width bias estimate for the fixed clipped population construction that remains uniform under time-mesh refinement and actual Gaussian matrix reuse; merely choosing a larger clipping constant does not provide it.

## Continuation: full error, including bias

The user explicitly requested control of the omitted finite-width/population bias and an unconditional result. The same investigation was continued in this folder. Three fresh scoped attempts produced [BIAS_CAVITY_ROUTE.md](BIAS_CAVITY_ROUTE.md), [BIAS_DIMENSION_ROUTE.md](BIAS_DIMENSION_ROUTE.md), and [UNCONDITIONAL_TAIL_ROUTE.md](UNCONDITIONAL_TAIL_ROUTE.md). They began without each other's findings; coordinator follow-ups suggested small-activity absorption and a hard-clip remainder test. No other study was used. A targeted external theorem search supplied no proof dependency and was not expanded into a literature audit.

The coordinator's [FULL_ERROR_CHECKPOINT.md](FULL_ERROR_CHECKPOINT.md) gives explicit full-error bounds for sufficiently large widths and finite-second-moment query laws:

- The all-time bias of the conditional finite-width mean is at most C_mu(Y/n+Y^3).
- The full all-time RMS population error, conditional on the initialized fitting event, is at most C_mu(Y/sqrt(n)+Y^3).
- On every finite horizon T, the actual all-initialization RMS error has the same bound plus C Y sqrt(T+1) exp(-cn/2).

The proof compares the actual evolving features to an auxiliary frozen-feature trajectory, bounding the difference by O(Y^3); it does not substitute frozen features for the trained model. The auxiliary mean bias is O(Y/n), including its nonlinear initial covariance bias. The exceptional-initialization route improves failure probability to Ce^(-cn) and proves the exact universal bound |f_n(t,x)|^2<=Y^2 t. These remove conditioning on finite horizons but not on the all-time supremum.

For fixed Y>0 the Y^3 remainder does not decrease with n. Thus these bounds control the previously unspecified term but **do not make the requested root-width theorem unconditional or complete**. No shrinking-label resolution is claimed. The missing estimate concerns the finite-width bias of the accumulated feature-learning contribution; an all-initialization all-time RMS claim additionally needs a predictor moment on exceptional initializations.

The new routes isolate two ways to attack the bias: a causal Gaussian response-trace comparison and a signed within-block/cross-block Gaussian interpolation trace. Small activity controls error amplification in both but has not supplied a closed root-width source estimate. The scoped [FULL_ERROR_CHECK.md](FULL_ERROR_CHECK.md) reconstructed the full-error checkpoint separately and supports its three partial bounds. Its correction restricting conditional claims to sufficiently large widths was applied. The coordinator read the complete check and all route notes. These are internal research checks, not promotion reviews.

## Continuation: attempted decisive hard-clip rate resolution

The user requested either the complete fixed-label root-width theorem or an actual slower-rate lower bound. The hard-clip [resolution record](RESOLUTION_STATUS.md) states that neither has been proved for that rule. The Y^3 estimate remainder is not evidence of a bias floor: the previously established qualitative convergence already rules out a positive constant limiting error on the fitting event.

Three fresh scoped attempts produced [RESOLUTION_UPPER_ROUTE.md](RESOLUTION_UPPER_ROUTE.md), [RESOLUTION_LOWER_ROUTE.md](RESOLUTION_LOWER_ROUTE.md), and [RESOLUTION_INTERPOLATION_ROUTE.md). Their internally proved advances are an actual all-time root-width theorem for queries orthogonal to the training span; an actual-carrier near-cap probability bound; adaptive linear-response trace approximation at root width; and O(1/n) variance-profile cancellation for every separately fixed polynomial matrix-action program. None supplies the general population bias rate. No actual-flow slower-rate counterexample was found.

The orthogonal-query theorem and its dependencies were checked separately in [ORTHOGONAL_QUERY_CHECK.md](ORTHOGONAL_QUERY_CHECK.md). The near-cap and linear-response proofs were checked separately in [CAP_ANTICONCENTRATION_CHECK.md](CAP_ANTICONCENTRATION_CHECK.md); the operator-cutoff and activity/domain corrections were applied. A proof-method counterexample in the interpolation route is explicitly not a closure-output counterexample.

The subsequent [WEIGHTED_REMAINDER_ROUTE.md](WEIGHTED_REMAINDER_ROUTE.md) proves the all-time L1 nonlinear row-weighted Taylor remainder at root width with scalar histories fixed at the actual cavity values, uniformly over bounded adaptive row paths. Its [independent internal check](WEIGHTED_REMAINDER_CHECK.md) supports the proof; the actual-row envelope qualification was applied. The key step uses the squared ordinary remainder norm, of order n^(-1/2), instead of taking its square root and losing a factor. This closes the L1 version of the upper route's local equation (20), not the full population comparison.

The upper route also isolates the linear scalar-history correction and the still-open mixed nonlinear correction. A mesh-uniform comparison of the joint covariance/response law remains necessary. Abstract counterexamples to intermediary proof claims in these reports are explicitly not slower-rate neural prediction examples. The coordinator read the complete reports and checks. No manuscript changes, experiments, Git mutations, or promotion were performed.

## Continuation: smooth clipping

The user explicitly requested the fixed smooth rule c_M(s)=M tanh(s/M),
with complete root-width population error rather than centered fluctuations
alone. The exact model and stronger-versus-weaker probability formulations
are fixed in [SMOOTH_SETUP.md](SMOOTH_SETUP.md). Both recursive backward
signals use this smooth clip; the true prediction derivative remains
unclipped. Hard-clip inactivity is not transferred to this model.

The coordinator's [SMOOTH_RESULT.md](SMOOTH_RESULT.md) establishes an internally checked
all-time root-width theorem for the full error against the own smooth
population, including mean bias, conditional on the initialized fitting
event and hence unconditionally at fixed confidence. It has no additive
fixed-label remainder. A fresh complete
[end-to-end audit](SMOOTH_THEOREM_CHECK.md) passed the combined theorem,
including finite-width mean bias and identification with the own population.
Its scope is q=1, two hidden tanh layers, any fixed M>0, finite data with a
positive initial population feature Gram, fixed sufficiently small labels,
and bounded query support. The stronger all-initialization all-time mean
square remains a distinct unresolved exceptional-event question. In precise
terms, the conditional expectation of the squared integrated time-sup error
is at most C/n, and the unconditional probability that its square root
exceeds sqrt(C/delta)/sqrt(n) is at most delta+C exp(-cn). This distinction
is part of the result, not a claim that the stronger expectation is proved.

The proof uses [SMOOTH_CAVITY_ROUTE.md](SMOOTH_CAVITY_ROUTE.md) for actual
Gaussian row/column reinsertion, tagged response errors, and a passive
feature-velocity source; [SMOOTH_MEAN_MAP_ROUTE.md](SMOOTH_MEAN_MAP_ROUTE.md)
for a contractive covariance/response law including instantaneous atoms,
singular histories, and deterministic entrywise derivative majorants; and
[SMOOTH_FEEDBACK_COMPLETION.md](SMOOTH_FEEDBACK_COMPLETION.md) for restoring
autonomous residual, clock, and memory feedback. The latter retains its
statistical hypotheses explicitly. [SMOOTH_RESTORATION.md](SMOOTH_RESTORATION.md)
records the elementary all-time damping implication.

Separate scoped checks support the [local estimates](SMOOTH_LOCAL_CHECK.md),
the [combined statistical bridge](SMOOTH_BRIDGE_CHECK.md), and the
[conditional feedback implication](SMOOTH_FEEDBACK_CHECK.md). The two
bridge domain corrections are recorded explicitly: empirical initial
covariances belong to an enlarged input domain, and comparable actual
activity paths justify the cubic bound on the frozen mean value contraction.
Statistical constants for passive queries are required and verified uniformly
on bounded sets. These are internal checks, not promotion reviews.

The fresh alternative [interpolation route](SMOOTH_INTERPOLATION_ROUTE.md)
also proves O(1/n) mean error in the first actual nonlinear initial output
coefficient and checks why scalar smoothness alone does not justify an
infinite response-series summation. The [all-initialization route](SMOOTH_ALLINIT_ROUTE.md)
transfers fitting and finite-time energy estimates, checks the true
output-derivative discrepancy, and solves the one-sample one-neuron smooth
monotonicity case. Their [auxiliary check](SMOOTH_AUXILIARY_CHECK.md) supports
these limited results. Neither supplies the missing exceptional-event
all-time second moment.

Fresh routes began with explicitly scoped inputs. Later coordinator
messages suggested scalar freezing, tagged variations, response-map
contraction, deterministic entrywise majorants, passive velocity, and
the domain repairs; this collaboration is disclosed in the notes.
The coordinator read the complete routes and checks. Current paper source
hashes are unchanged; the pre-existing dirty PDF and concurrent other-study
README were preserved. No numerical experiments, manuscript edits, Git
mutations, or promotion were performed.

## Follow-up: removing small labels

[SMALL_LABEL_ROLE.md](SMALL_LABEL_ROLE.md) separates the whole-activity
response-map contraction from the all-time fitting and residual-stability
requirements. A causal extension of the law comparison may be possible,
but it must preserve the complete past dependence. Bounded total activity
alone does not imply root-width integrated residual error. The general
all-time width theorem for arbitrary labels at the original fixed cap
remains open; failure of the small-activity estimates is not a counterexample.

The note proves a concrete fitting extension: for any fixed label RMS Y,
initial mixer bound K and readout-Gram gap lambda, set
H=6+2X^2(K+2), where X is the maximum normalized training-input norm.
If the fixed positive cap satisfies
2MY/lambda <= min(1,lambda/(6H)), then the actual smooth closure fits
exponentially, all states converge, and total activity is at most Y/lambda.
This permits unit labels after choosing a sufficiently small cap independent
of width. It trades label smallness for cap smallness and small accumulated
feature movement; it does not yet extend the full population error theorem.
The complete proof and scoped internal check are recorded in that note.

## Follow-up: clipping levels growing with width

The user requested control of the M dependence while retaining one fixed
nonzero small label vector, with the principal goal of permitting M(n)
to tend to infinity. This continuation remains in the same study and
changes neither the training rule nor its own-population reference.

[M_LOG_SCALE_RESULT.md](M_LOG_SCALE_RESULT.md) gives the resulting
internally checked theorem for M>=1. Under the same two-layer tanh q=1,
positive initial population Gram, and bounded-query assumptions, a
positive label threshold can be chosen independently of M. Both the RMS
prefactor and minimum-width threshold are bounded by C exp(CM). The time
supremum is inside the integrated prediction error, including the fitted
endpoint and the finite-width/population mean bias. The corresponding
fixed-confidence bound is unconditional over initialization, with failure
at most delta+C exp(-cn); an unconditioned all-time second moment remains
a different unresolved claim.

Consequently every M(n)=[log(e+n)]^alpha with 0<alpha<1 gives full
all-time error n^(-1/2+o(1)). A sufficiently small positive constant
multiple of log(n) also works, with a slower decaying power rate. This
does not retain a strictly cap-independent root-width constant, prove
M=sqrt(n), or control the separate cap-removal error to one unclipped
population. The constants are sufficient upper bounds, not lower bounds
on the actual error.

The proof ingredients are [explicit finite-vector/cavity constants](M_UNIFORM_CAVITY_ROUTE.md),
[population law estimates](M_UNIFORM_LAW_ROUTE.md),
[deterministic stability and valid schedules](M_CAP_SCHEDULE_ROUTE.md),
[strong covariance and response-row concentration](M_ROW_CAVITY_ROUTE.md),
and [population comparison using integrated response rows](M_ROW_DOMAIN_ROUTE.md).
The last two notes avoid the large cost of bounding every response density
uniformly: localize the random cavity rows, discard exceptional
environments using actual finite-vector moments, and rule out the first
exit of the deterministic expected rows from a common small domain.
The lower and upper Gaussian actions remain the original mixer and its
actual transpose.

The combined [check](M_LOG_SCALE_CHECK.md) identified and checked two
necessary repairs. Products of upper feature velocities need coordinate
fourth moments of the reused Gaussian action, obtained from the direct
passive cavity identity before any law comparison; operator norms alone
do not give the required root-width gradient bound. Also, passive
velocity comparison is performed at a fixed target time before integrating
its residual envelope, and a specified-source upper response retains its
possible exp(CM) forcing cost. No stronger unproved temporal supremum or
density bound is substituted.

The earlier conservative [triple-exponential theorem](M_SCALE_RESULT.md)
and its [separate check](M_SCALE_CHECK.md) are preserved as an intermediate
result; the single-exponential theorem supersedes its quantitative cap
schedule. The coordinator read all new routes and both complete checks.
Scoped routes began independently, then received the causal comparison
and response-row localization strategies and exchanged interface
clarifications. These are internal research checks, not independent
promotion reviews. No other study was used, no numerical experiments
were run, and no manuscript or Git changes were made.
