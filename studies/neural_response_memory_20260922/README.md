# Evolving response states for neural memory

New theory-only study, 2026-09-22. The user discards trainable dictionaries and
asks whether neuron forward/backward histories admit a small evolving state,
analogous to position and velocity, capable of saturation and compatible with
a zero-radius population Taylor expansion. No experiment or GPU use is
requested. Earlier compute budgets are not reopened.

## Contract

Target: canonical bias-free two-hidden-layer tanh network, Gaussian hidden
initialization, actual reused middle matrix and transpose, all blocks trained,
probability MSE and physical mobilities(n,1,n). Distinguish finite-width
identities, population flows and proposed compressed approximations.

Desired state: present neuron responses and finitely many evolving memory
variables, with coefficients derived from the model and retained state.
The initialized middle matrix W0 and its actual transpose may be retained
under the user's current authorization. No learned dense matrix, full
trajectory, unknown exact response kernel or future target trajectory may
be hidden as an oracle. Fixed input dimension differs
from fixed sample count; sample-wise fields do not solve sample-independent
compression. Immediate output is explanation and a grounded formulation,
not a claimed finite closure or efficiency theorem.

Accept the user's zero-radius population-observable statement as a premise;
do not search for that book theorem. Examine its implications for ODEs,
plateaus and population expectations. No old study's unpromoted results are
inputs. Allowed sources: this study, established docs/code and primary
external literature. Examples are analytic, not training experiments.

## Ownership and startup

Root owns README and synthesis. Fresh prompt-only agents memory_state_route
and neural_response_route own MEMORY_STATE_ROUTE.md and
NEURAL_RESPONSE_ROUTE.md. Each receives only its self-contained assignment
and required skills/process, not another route. These are internal checks,
not promotion reviews. Root verifies premises against canonical equations.

Shared instructions and research/rigorous-math skills read. Previously fully
read docs/README.md and docs/NOTATION.md are hash-verified unchanged. No
maintained file, old scientific result or Git index will be altered. New
notes remain in this flat study folder. Existing work is preserved.

## Status

Theory assessment complete; no experiment was launched. See
`RESPONSE_STATE_SYNTHESIS.md` for the canonical response identities, an explicit
Gaussian population with zero Taylor radius and one scalar ODE per member,
and the precise auxiliary-state memory formulation. The scoped derivations
are `NEURAL_RESPONSE_ROUTE.md` and `MEMORY_STATE_ROUTE.md`.

Internally checked: finite response transport, adjoint constraints, the
Gaussian example, exact linear memory realization including initialization,
and conditional approximation statements. Not established: a closed,
efficient finite response-memory model for canonical neural training, its
population convergence, a useful approximation rate, or superiority to any
dictionary. The next theoretical obligation is a model-derived nonzero
terminal law and an estimate of its omitted-response defect. No promotion,
Git write, additional tuning or compute budget was requested.

The two scoped routes also checked the root synthesis within their assigned
mathematical scopes. No blocking errors were found; clarifications about
population analyticity, transform domain, normalized contractions and reuse
of Gaussian weights were incorporated. These are internal checks, not
independent promotion reviews.

## Concrete plateau-capable population history construction

The user clarified that the desired object is forward/backward ODE states in
both neuron populations, joined by a condensed matrix. The continuation is
recorded in `PLATEAU_HISTORY_POPULATIONS.md`: an explicit Legendre history
encoder, driven by a residual-activity clock, reconstructs the learned middle
weight increment through a finite core. Its free modes are rational powers
of the learning clock, and its finite reconstruction has an explicit
outer-product defect. This is constrained history evolution, not free factor
training. The encoder is a known HiPPO construction; the neural coupling and
clock adaptation are derived in this study.

Exact/conditional results: history identities, finite-width well-posedness
with the initial dense operator retained, a plateau theorem conditional on
integrable RMS residual, and passive history approximation bounds. Open:
compression of the reused initial Gaussian operator, self-consistent accuracy
and stability, a useful width-uniform error rate, and sample-independent
state size. No experiment is authorized by this theory discussion.

Fresh prompt-only routes own `NEURON_RELAXATION_ROUTE.md` and
`RESPONSE_COUPLING_ROUTE.md`; root subsequently supplied the encoder and
activity-clock candidate for scoped algebraic checking. The resulting checks
are collaborative internal checks, not blind reviews of that candidate.

Both scoped agents checked the completed root construction in their assigned
sections and reported no blocking errors. Root read both full reports and
verified normalization, dummy-history correction, endpoint-defect identity,
and the distinction between passive history error and closed-loop accuracy.
The canonical coefficients use the normalized rank-one operator uv^T/n.
The external encoder attribution was verified by root against the primary
paper's definition, theorem and complete relevant derivation. No claim of
fully compressed canonical dynamics is made.

## Current direction: derive from the full Gaussian history law

The user rejects selecting an external history encoder as the research
answer and requests a first-principles DMFT-like reduction. No external
research was consulted for this continuation. `FIRST_PRINCIPLES_DMFT_CLOSURE.md`
starts from the exact learned operator history and the established Gaussian
source-response rule (complete `docs/special_data_limits.md` III.F read).
It identifies the needed forward/backward correlation and causal response
statistics, derives conditional finite-state memory/source equations, and
states their coefficient-provenance requirements. The earlier history
encoder is preserved as a scoped mathematical construction, not the adopted
solution of the canonical compression problem.

The central proposed assumption is small joint predictive state complexity
of covariance and response, with an autonomous present-law coefficient rule.
It is unproved for the canonical model. Finite invariant observable spans
would return to a fixed dictionary, and an exact nonsingular smooth finite
Gaussian Markov lift has no observable innovation; both restrictions are
made explicit. No arbitrary damping law, separate coupling training, or
population closure theorem is claimed.

Fresh prompt-scoped routes own `DMFT_PRESENT_STATE_ROUTE.md` and
`INTERACTION_FIRST_PRINCIPLES_ROUTE.md`. Their initial inputs were only the
canonical equations and the user's constraints; root subsequently supplied
the established finite-program source rule as an additional explicit input.
They did not consult other studies or external literature. No computation
or experiment was requested or run.

Both routes subsequently checked the completed root derivation within their
assigned scopes. They found no blocking algebraic error. Clarifications were
incorporated about fixed-program infinite-width status, causal query timing,
joint initialization of Gaussian realizations, named-source derivatives,
fixed-coefficient predictive rank, and the conditional invariant-space claim.
These are collaborative internal checks, not independent promotion reviews.
The missing explicit autonomous coefficient law remains unresolved; this
turn does not deliver a closed small canonical model or an efficiency bound.

## Current scope: one-sample reversible states and aggregate learned interaction

The user now explicitly permits retention of the initialized W0 and its
actual transpose. The target is to replace the learned dense increment and
its history, not to eliminate that fixed operator. This supersedes the older
no-dense-initialization requirement for this continuation. The user also
correctly rejects any implication from finite per-neuron state to low rank.
The finite-factor formulation discussed in the conversation is only a
special readout assumption, not the general response-state model.

For one sample, assume the reversible state laws are supplied. The new
derivation in `REVERSIBLE_STATE_AGGREGATION.md` converts accumulated rank-one
learning into a forward transport PDE for one interaction function on the
product of current neuron-state spaces. Its population integrals give the
learned forward and transpose fields. Differentiating those integrals gives
an explicit message/moment hierarchy generated by the assumed state motion.
No low rank, time Taylor expansion, or stored sequence of past responses is
required. The pair field remains a function; no small finite-statistic or
computational-efficiency theorem is claimed.

Fresh prompt-only routes own `PAIR_STATE_TRANSPORT_ROUTE.md` and
`PAIR_FLOW_POTENTIAL_ROUTE.md`. Root owns the synthesis and README. Inputs
were the one-sample equations, the current user assumptions, and required
skills; the transport route later received root's moment-hierarchy identity
for audit. No other studies or external research were consulted. No training
experiment, GPU work, maintained-source change, or Git-index write occurred.

Root read both complete route reports and checked the canonical scaling and
population contractions. Both routes checked the completed synthesis within
their scopes; no blocking errors were found, and residual continuity was
made explicit. The transport and message identities are internally checked
under their stated assumptions, not promoted results. The canonical finite
state law, tractable pair-field representation, finite moment closure, and
efficiency bounds remain open.

## Current correction: collective states and explicit mixing

The user emphasizes that reversibility concerns the full coupled state, not
independent neuron flows. `COUPLED_CURRENT_STATE_SYNTHESIS.md` derives exact
one-sample motion equations and a learned-action hierarchy whose interactions
are explicit: actual W0/transpose fields, current population contractions,
and learned actions on differentiated source observables. The assumed finite
particle law must retain all these dependencies in its arguments.

The previous pair transport remains a conditional identity for an environment
path. A universal current-state readout K(t,b,a,Q) must include the evolving
population environment Q and its chain-rule term D_Q K[Qdot]. This is already
inside the partial-time derivative if one instead uses the path-conditioned
field k_t(b,a); it must not be counted twice. Two marginal state laws alone
do not automatically retain the initialized operator's indexed coupling.

Fresh prompt-only routes own `COUPLED_STATE_GENERATOR_ROUTE.md` and
`ONE_SAMPLE_ACTION_HIERARCHY.md`. Root owns synthesis/README. No experiments,
external literature, other-study scientific inputs, or Git writes are used.
No finite closure or low-rank consequence is claimed.

Root read both complete route reports and verified the derivations. The
action route checked synthesis sections 1–4 and the generator route checked
sections 5–7; no blocking mathematical errors were found. Precision edits
on mobility ordering, regularity, conditional invertibility and adaptive
Gaussian query scaling were incorporated. These internal checks establish
the displayed interaction identities under their stated hypotheses, not a
finite closure, population limit, or efficiency theorem.

## Explicit autonomous hypothetical action closure

The user now explicitly requests choosing a hypothetical ODE for the learned
forward/backward actions and deriving the remaining one-sample system. The
previous illustrative response accelerations did not close their learned
interaction readout. `AUTONOMOUS_ONE_SAMPLE_ACTION_CLOSURE.md` supplies an
actual autonomous approximate system with 4n evolving coordinates and the
retained W0. Its one closure choice discards the velocity-action components
orthogonal to the current opposite-layer response, while preserving the
scalar forward/transpose pairings. All output/readout, canonical outer-layer
updates, population averages and response derivatives are explicit.

Internally checked by root and a fresh prompt-only scoped algebraic checker:
sequential autonomy on the stated nondegenerate domain, consistent zero-action
initialization, the scalar adjoint invariant, non-increasing squared loss,
and stationarity at zero residual. This is a hypothetical response model,
not exact canonical compression: further simultaneous matrix-action
pairings need not hold. No accuracy, rational-time solution, global regularity,
population limit or efficiency result is claimed. No experiment was run.

## Current direction: self-consistency before choosing a motion law

On 2026-09-24 the user asks for a criterion that any proposed history-free
population motion law must satisfy, including the learned interaction and
Gaussian initialization checks. This refines the same response-memory
objective; it does not adopt the earlier projection toy. Root's
`SELF_CONSISTENCY_CRITERIA.md` separates exact direct/indirect weight effects,
shared-operator and derivative compatibility, collective state sufficiency,
and Gaussian mean-square initialization certificates. It identifies
constraint preservation as the proof step beyond initial jets, without
assuming a convergent time Taylor series.

Fresh prompt-only routes own `SHARED_OPERATOR_CONSISTENCY_CHECK.md` and
`GAUSSIAN_INITIAL_CONSISTENCY_CHECK.md`. No new closure, experiment, or proof
of efficient finite sufficiency is claimed. The finite operator tests and
conditional-variance/projectability statements are mathematical criteria;
their evaluation for a specified proposed motion law remains separate.

Root read both full route reports and checked their derivations. The operator
route audited synthesis sections 1–3 and the Gaussian route sections 4–6;
precision corrections were incorporated. The resulting criteria are
internally checked under their stated regularity and population-limit
assumptions. No particular finite motion law has yet passed these tests,
and preservation of a sufficient set of consistency relations remains the
positive-time proof obligation.

## Autonomous closure, one defect, and global tracking criteria

The current request removes explicit time from the learned interaction and
asks for a precise closure, its approximation step, a global sufficient
condition, and a broad Gaussian necessary certificate. The continuation is
`AUTONOMOUS_CLOSURE_CERTIFICATES.md`. A fixed current-state readout kappa_P,
autonomous collective F_P, exact outer-block equations and consistent
population readouts reduce the entire physical approximation to one
middle-weight tangency defect. Vanishing of this defect on reachable states,
matching initialization and ODE uniqueness give a precise exactness iff.

A conditional all-time approximation theorem is proved using the one-sample
gradient structure: a relative defect bound epsilon|r|, a nondegenerate
learning kernel, and controlled prediction gradient/Hessian make both the
forcing and error amplification integrable. This gives a uniform O(epsilon)
full-state tracking bound if the stated constants are uniform. It is not
merely a finite-horizon exponential-in-time estimate. These assumptions have
not been established for a finite efficient candidate or a width-uniform
Gaussian population family.

The easy necessary screen is the Gaussian mean squared initial tangency
defect, with conditional variance as a broader information obstruction.
Positive defect rejects exactness of that candidate; zero is insufficient
without preservation. All finite derivative checks remain compatible with
nonanalytic population motion. A direct tanh initialization calculation is
included as an illustrative rejection, not a test of an adopted model.

Fresh prompt-only routes own `AUTONOMOUS_TRACKING_CHECK.md` and
`GAUSSIAN_AUTONOMY_CHECK.md`. Root read both complete derivations and they
subsequently audited synthesis sections 1–5 and 6–7 respectively; precision
corrections were incorporated. This is internal checking, not promotion.
No experiments, external research, other-study inputs, maintained-source
edits or Git writes were used. A concrete efficient closure with a proved
small defect remains the outstanding scientific construction.

## Concrete rational moments and authorized empirical tests (2026-09-24)

The user now authorizes constructing a principled autonomous candidate and
testing it on earlier compatible circle configurations, especially the hard
dictionary case. This supersedes earlier theory-only restrictions for this
continuation. The narrow empirical input exception covers earlier benchmark
definitions, reproduction code and selected results; it does not import
other studies' unpromoted mathematical conclusions. HARD_BENCHMARK_INPUTS.md
freezes those inputs. RATIONAL_CANDIDATE_ROUTE.md derives response-moment
dynamics, exact derivative-memory coordinates, one covariance defect and a
conditional all-time argument. MOMENT_EXPERIMENT_PROTOCOL.md freezes the
bounded two-GPU experiment and numerical validity gates before execution.
No compatibility-only global theorem or width-uniform efficiency is claimed.

### Executed construction and expanded campaign

MOMENT_CONSTRUCTION.md now specifies the autonomous rational response-moment
closure in the agreed m,Q,F,K,E notation. Its exact moment transport and sole
cross-history product approximation give an explicit defect. An independent
algebraic check validates the conditional inverse-square-root-order defect
estimate and conditional all-time convergence argument. Compatibility alone
and width-uniform global efficiency remain unproved.

The user additionally authorized next-hard original configurations. Selection
and an exact antipodal quotient are frozen in ADDITIONAL_BENCHMARK_INPUTS.md.
The completed campaign has34 closure runs over5 cases atP=1,3,7, with numerical
refinements, and8 fresh dense reference runs where archival accuracy was
limiting. All selected closure refinements pass the prescribed empirical
numerical gates; initial drift failures remain recorded. MOMENT_RESULTS.md
states the outcomes, storage distinctions, fresh-reference precision limits,
and proof status. The reproducible analysis and figures are under
`data/generated/neural_response_memory_20260922/analysis01/`.

Errors decrease acrossP=1,3,7 on all5 tested cases. Hardest-case RMS against
the original dense target is0.2363,0.0730,0.00466. This supports the usefulness
of this history-moment representation on these cases. It is neither a
width-independent efficiency theorem nor a rate inferred from finite data.
The initialized W0 remains dense and retained; only the evolving learned
correction is represented by response moments. No external literature,
maintained-source changes, promotion, or Git write occurred in this campaign.

### Authorized matched-rank factor control (2026-09-24)

The user requests a directly trained W2=W0+AB comparison, keeping correction
rank equal to the existing response-moment rank at P=1,3,7. The observable
remains final full-circle RMS difference from the dense trained predictor;
training loss only fixes the matched stopping threshold. This tests the same
investigation's alternative explanation, not a new target or a claim that
the response moments are optimally efficient among all possible methods.

FACTOR_CONTROL_PROTOCOL.md freezes all five cases, two separately reported
factor seeds, exact zero initial correction and the factor gradient metric,
numerical refinement gates, and the 60-primary/15-conditional trajectory,
3600-integration-second cap. The earlier campaign is complete and untouched.
Root owns protocol and synthesis; factor_control_impl owns the new engine,
runner and tests; factor_comparison_analysis owns the new analysis script;
factor_control_audit owns the separate internal check. Generated outputs use
factor_control01 and factor_analysis01 in this study's generated namespace.
No QR/SVD comparator or factor learning-rate tuning is included.

The control campaign is complete: 60 trajectories (two tolerance levels for
all five cases, three ranks and two factor seeds), 2153.56 recorded GPU
integration-seconds, no conditional extra runs. All 29 fitted and numerically
valid factor cells have larger full-circle error than the matched response
moments. The hard outlier P=1, seed 20260925 cell reached its wall cap at both
tolerances and is excluded from matched-endpoint claims. At P=3 on the hardest
case, moment RMS is 0.07295 versus factor RMS 0.46546 and 0.46091; at P=7 it is
0.004663 versus 0.51621 and 0.25103. Both seeds are reported separately.

FACTOR_CONTROL_RESULTS.md gives the interpretation and reproduction recipe.
FACTOR_CONTROL_CHECK.md records the independent raw-gradient checks, replay
of all 60 saved states, common-reference rescoring, and agreement with the
final analysis. All fitted pairs pass the numerical gates and resolve the
score ordering; the capped cell remains unresolved. The result supports the
specific moment evolution over the specified directly trained factor flow,
without testing QR/SVD truncation or asserting optimality or a population
convergence theorem. The prior conditional theory is unchanged.

The source is factor_control_engine.py, run_factor_control.py,
test_factor_control.py and analyze_factor_control.py; independent check
sources are check_factor_control_engine.py and check_factor_control_endpoints.py.
Full tables and rank/function plots are in the generated factor_analysis01
directory. No further training is authorized by an unused conditional budget.
No promotion or Git write was performed, and concurrent checkout changes
were preserved.

### Authorized MNIST extension (2026-09-24)

The user requests the same moment closure on two MNIST digits with 1000
training samples, P=1,2,3 and validation scatter plots/RMS against a freshly
trained dense reference. MNIST_PROTOCOL.md freezes digits 3/8, 500 training
images each, 1984 official test images used as a held-out validation panel,
image-wise length normalization, canonical model, matched-loss endpoints,
two numerical resolutions and bounded two-GPU compute. This continues the
current method's empirical test; it does not import other studies' unpromoted
MNIST results or reopen prior campaigns. No maintained recipe was found,
so the precise new configuration is explicit rather than presented as an
exact replication of an unspecified older run.

Root owns protocol/data preparation/README/results. mnist_engine_plan owns
mnist_moment_run.py and its tests; mnist_analysis owns the new analyzer;
mnist_audit owns an independent check script/report. Prepared data and
raw-file provenance are in the study's generated mnist_data01 namespace.
The campaign is complete: all 12 trajectories (four models at three numerical
tolerances) reached training MSE .001. At the finest tolerance, validation
RMS differences from dense are .01877195, .00191819 and .00123214 for P1, P2, P3.
The observed predictions agree closely. P1 passes the strict primary numerical
gate; P2/P3 remain precision-limited under its 10%-relative requirement, and
their mutual ordering is not resolved by the observed refinement sensitivities.
No order-convergence rate or population theorem follows. State storage at
1000 samples and n=1024 exceeds dense storage for these implementations, so
this does not establish a memory or speed improvement on MNIST.

MNIST_RESULTS.md gives design, exact scope, full resource/precision accounting,
reproduction commands and figures. Final plots and metrics are in generated
mnist_analysis02; MNIST_CHECK.md records the independent raw-data, gradient,
checkpoint-reconstruction and analysis checks. Twelve runs used 2513.42 pure
integration seconds, plus 7.01 for successful feasibility pilots. All four
predeclared optional numerical refinements were used; no training remains.
The earlier MNIST analysis and pre-training pilot failure are preserved.
No promotion, maintained-source edit or Git write occurred.

### Authorized 100-image, width4096 MNIST continuation (2026-09-24)

The user requests the same dense/P1/P2/P3 comparison with100 total training
images and n4096, so the learned-correction rank bounds become100,200,300.
MNIST100_PROTOCOL.md freezes a balanced nested subset of the earlier training
panel, unchanged1984 held-out images, shared canonical initialization,
matched-loss endpoints, tighter numerical resolutions and bounded two-GPU
execution. This continues the same empirical investigation; prior campaigns
and the separately retrieved old dictionary result are not training inputs.

Root owns protocol, launcher, runs and synthesis. mnist100_data_analysis owns
prepare_mnist100_moments.py and the explicit backwards-compatible mnist100
mode in analyze_mnist_moments.py. mnist100_audit owns the independent checker
and MNIST100_CHECK.md. New products use the generated mnist100_* namespaces.
The unchanged runner/engines passed the five MNIST deterministic tests.
Both30-step feasibility pilots completed at4096 without a memory failure,
using2.83s dense and2.23s P3 integration and identical initialization hashes.
The campaign is complete: all eight primary trajectories at rtol1.25e-5 and
3.125e-6 reached training MSE .001. Held-out RMS against dense is .00324756,
.00108443 and .00119922 for P1/P2/P3; all15 numerical gates across the five
loss milestones pass, so no conditional refinement is triggered. P2 is
slightly better than P3; the primary order trend is not monotone. Independent
NumPy reconstruction checks all56 observations and40 crossing checkpoints,
and dense/P3 repetitions on swapped GPUs reproduce every scientific saved
array and checkpoint state bit-for-bit. MNIST100_CHECK.md retains the audit.

History factors contain819200,1638400,2457600 coordinates, respectively
20.48x,10.24x,6.83x fewer than an unrestricted4096-square learned correction.
Fixed W0 remains dense. MNIST100_RESULTS.md separates moving state, total
moving-plus-fixed state, retained copies, measured peak allocation and runtime.
The measured implementations use less peak GPU memory but take longer at
the stated tolerances; no universal efficiency or asymptotic-rate claim follows.
Final metrics and scatter/rank/loss plots are in generated mnist100_analysis01.
Two pilots, eight primary runs and two repeats used1086.17 summed pure GPU
integration seconds (1115.79 with in-loop observations), below the8460 cap.
No further training remains. No maintained-source change or Git write.

### Authorized three-hidden-layer circle continuation (2026-09-24)

The user explicitly returned to this study's five circle tasks and requested
three hidden layers, two dense internal matrices, width 4096, and dense versus
P=1,2,3 response closures. The [derivation](DEEP_CIRCLE_DERIVATION.md) gives two
coupled history operators and their exact covariance defects; the
[context digest](DEEP_CIRCLE_CONTEXT_DIGEST.md) reconciles the relevant prior
constructions and corrections. The [protocol](DEEP_CIRCLE_PROTOCOL.md) and
[literal tasks](deep_circle_cases.json) were frozen before execution.

The campaign is complete. All 40 primary trajectories reached training MSE
.001, and all 75 matched-milestone comparisons pass the frozen numerical
gates. No conditional tolerance refinement was needed. At the final
milestone, P2 is best on the two alternating-label tasks; P3 is best on the
other three. Both improve on P1 for all five tasks. The
[numerical decision record](DEEP_CIRCLE_NUMERICAL_DECISIONS.md) retains the
branch decisions. [Full results](DEEP_CIRCLE_RESULTS.md) give the RMS table,
feature movement, memory/runtime accounting, figures and reproduction
commands. Final metrics and PNG/PDF figures are in
[deep_circle_analysis01](../../data/generated/neural_response_memory_20260922/deep_circle_analysis01/).

Nine deterministic implementation tests and the independent gradient,
transpose, derivative/defect, moment-transport, controller and oddness checks
pass. Both opposite-GPU repetitions reproduce every saved scientific array
and checkpoint field bit-for-bit. Independent replay covers all 42 full
trajectories, 294 observations and 210 checkpoint states, with maximum
prediction difference 3.39e-13. A scan of 252 archives found one flipped bit
in one endpoint checkpoint. The redundant valid final state restores that
exact bit and the original recorded CRC. The damaged original is preserved;
the [recovery manifest](../../data/generated/neural_response_memory_20260922/deep_circle_recovery01/repair_manifest.json)
records the verified copy. No prediction, metric or training configuration
changed. The [implementation and replay audit](DEEP_CIRCLE_CHECK.md) and
[bounded report check](DEEP_CIRCLE_REPORT_CHECK.md) retain methods and scope.

Features move substantially in every hidden layer. The P2/P3 history arrays
use 2/3 MiB for eight samples, but both initial dense matrices remain
(256 MiB). Measured peak GPU memory is lower while runtime is modestly
longer. This one-initialization, finite-width result establishes neither
whole-network compression nor a universal order-convergence law.
Two pilots, 40 primary trajectories and two repeats used 3114.516 summed
integration-wall seconds including observations, below the 12600 cap.

Root owned protocol, cases, execution, analysis and this record;
deep_derivation authored derivation/context and analysis code; deep_engine
authored the engine, runner, tests and launcher; deep_audit authored the
independent checker, audit and archive-recovery source; deep_report_check
performed the bounded final-report consistency check. New products use
this study's deep_circle_* namespaces. Earlier campaigns remain complete
and untouched. No further training remains. These results remain internal
to this study; no promotion or Git write occurred.

### Aggregate-only assessment (2026-09-25)

The user explicitly asks whether the current response-memory populations can
be replaced by finitely many scalar aggregate ODEs when only loss or sample
outputs are requested. The [assessment](AGGREGATE_OBSERVABLE_CLOSURE.md)
derives the required aggregate projection criterion, the first unclosed
nonlinear overlap, and the exact output/loss identities including the
history-projection defects at two and three hidden layers.

Observable-only closure is weaker than reconstructing neurons, but the current
finite history order does not establish it. Exact finite aggregate closure
requires additional preserved statistical structure; approximate aggregate
closure needs a separate controlled defect. The earlier zero-Taylor-radius
premise also conditionally excludes exact nonsingular analytic scalar ODEs
with analytic readouts for that particular target observable. This is not
a general impossibility result for nonlinear or approximate aggregate laws.

Root owns only the new assessment and this entry. Scoped agents checked its
algebra, deeper extension and empirical claim scope; the
[algebraic check](AGGREGATE_CLOSURE_ALGEBRA_CHECK.md) retains the source versions,
corrections and limitations. Existing numerical campaigns test history
compression while retaining neuron populations and dense initialized actions;
they provide no separate scalar-aggregation test. No new experiment, maintained
source edit, promotion or Git write occurred for this assessment. The next
theoretical obligation is a specified finite aggregate map with a derived or
bounded observable-velocity defect. Concurrent activation work below remains
separate from this theory-only assessment.

### Archived direct-dense scalar experiment (2026-09-25)

At the user's request, the separate direct-dense scalar derivative hierarchy,
its implementation, protocols, tests and reports were removed from this active
study and pushed to the experimental branch
[`codex/experimental-direct-dense-scalar-20260925`](https://github.com/ajoudaki/PDE/tree/codex/experimental-direct-dense-scalar-20260925/studies/neural_response_memory_20260922),
commit `1f5084a501cafa5db524be6f06a1ac2c64a93ba4`. The archive contains all
55 retired source/report files, four unchanged support files and the original
experiment history. The branch is based on the existing remote main, so no
unrelated unpublished local commits were included. The active branch and
shared index were preserved.

All 1,166 generated files were checksum-verified and consolidated into
[one local archive](../../data/generated/neural_response_memory_20260922/archived_direct_dense_scalar_20260925/runs.tar.zst);
the branch includes their path/hash manifest, while the generated data remain
outside Git. This abandoned model was not derived from the Legendre population
closure and supplies no scalar-compression result for that closure. Current
work continues in this study by deriving aggregates directly from the fixed-P
population equations.

### Reduction of the population closure to scalar aggregates (2026-09-25)

The user corrects the research route: derive the scalar model from the tested
Legendre population closure, with its own explicit approximation step. The
[new synthesis](POPULATION_TO_AGGREGATES.md) fixes P and derives a concrete
width-independent list of global averages that determines all first training
and fixed-query output velocities. Differentiating that list exposes named
gate-weighted higher moments and initialized-operator/adjoint contractions.

The [aggregate equations](POPULATION_AGGREGATE_EQUATIONS_CHECK.md) are checked
against the existing population engine and an independent autograd chain-rule
oracle: 198 deterministic comparisons pass, maximum normalized error 3.33e-16.
Width 7 is used only for bounded algebra verification, with no training or
population-accuracy claim. Source: `check_population_aggregate_equations.py`;
evidence: generated `population_aggregate_algebra01/results.json`.

The [scalar construction](POPULATION_SCALAR_CONSTRUCTION_CHECK.md) supplies
a finite-width contraction hierarchy and an explicit finite reference
truncation. Its omitted generator terms are the precise new approximation.
The [finite-closure check](POPULATION_FINITE_CLOSURE_CHECK.md) distinguishes
exact projectability, closure by construction and conditional error control.
Its final collaborative audit reads the complete corrected synthesis and
reference construction, records their SHA256 values, and finds no remaining
mathematical correction within its declared scope. Root read the complete
reports, checker and numerical evidence; numerical evidence and archive
operations were outside that mathematical checker's verification scope.
The reference deletion rule is not an adopted practical solver; useful tail
control, stability, preprocessing cost and population-limit identification
remain open. The unpruned all-graph dictionary even includes initialized
contractions diverging with width, so a finite type count alone supplies no
population-limit theorem. Training loss, passive circle approximation, history
order P and scalar resolution have separate error and validity obligations.

Root owns synthesis and this record. Scoped agents own the equation/algebra
check, reference construction and finite-closure audit. The earlier direct-
dense hierarchy has been archived as requested; its empirical failures are
not evidence against this population-derived route. Work remains in this
study. No new training campaign, maintained scientific edit or promotion was
performed in this continuation.

### Authorized activation robustness continuation (2026-09-25)

The user's three-hidden-layer,width4096 activation continuation is complete.
The [protocol](ACTIVATION_CIRCLE_PROTOCOL.md), [literal cases](activation_circle_cases.json)
and [activation-general derivation](ACTIVATION_CIRCLE_DERIVATION.md) retain the
same eight literal circle inputs, shared initialization and canonical dynamics,
with ReLU, exact GELU, SELU and uncentered sigmoid on the two hardest tasks.
Dense and chronological P1/P2/P3 closures are compared at matched loss using
8192 circle directions. Root owns execution/results/this entry; activation_theory
owns the derivation, activation_engine the optional fast implementation, and
activation_audit the independent checks. No maintained-source or Git-index
change or promotion is part of this work.

All64 primary runs, two prescribed SELU refinements and eight cross-GPU
repetitions finished, in addition to eight pilots. The
[results](ACTIVATION_CIRCLE_RESULTS.md) give P1/P2/P3 circle RMS errors
1.43975/.24239/.024854 for GELU-outliers,5.78389/.66349/.260104 for GELU-quadrant,
and .66415/.26827/.241370 for sigmoid-outliers. All nine available fitted
comparisons pass their numerical gates. P3 is best at these endpoints, but
only GELU-outliers P3 meets the predeclared absolute RMS<=.1 criterion.
The corresponding P3 discrepancies relative to dense circle RMS are1.18%,4.77%
and17.10%; this descriptive normalization does not replace the original gate.

ReLU and SELU do not fit within the declared caps. Sigmoid-quadrant lacks a
fitted dense reference; at shared MSE .1 its P1/P2/P3 errors are
.26730/.20349/.15736, with passing gates. SELU's extra dense resolution stops
before .9, leaving the earlier relative-sensitivity failure unresolved rather
than passed. These missing comparisons are inconclusive. All72 available
shared-loss comparisons pass;15 of27 time diagnostics pass. Increasing P is
not uniformly better at every milestone: two resolved P2-to-P3 worsenings occur
at sigmoid MSE .5. No convergence or activation-optimized ranking is claimed.

The [final internal check](ACTIVATION_CIRCLE_FINAL_METRICS_CHECK.md) independently
rescores66 scientific trajectories with zero scalar discrepancy. All eight
cross-GPU repetitions pass. Physical reconstruction passes499 saved prediction
panels across82 runs. One initialization-hash check failed in the first batch,
although its predictions and reproduction passed; independent regeneration and
an unchanged isolated replay pass. The cause is unidentified, and the original
failure/controller status and recovery receipts remain separately visible.
The results report explains this qualification and links all evidence.
The campaign charges18424.84 summed integration seconds below33000, with83
attempts including the retained external interruption, below the113 ceiling.
There is no remaining authorized training or validation branch.

The [summary figure](../../data/generated/neural_response_memory_20260922/activation_circle_summary01/activation_circle_summary.png)
and [circle-function figure](../../data/generated/neural_response_memory_20260922/activation_circle_analysis_final03/function_curves.png)
show final scores, unavailable cases and the explicit intermediate-loss fallback.
Final metric tables, PDFs, hashes and selected-run provenance are in
`activation_circle_analysis_final03`; execution/repetition/resource records are
in `activation_circle_finish03`, physical replay in `activation_circle_audit03`,
and independent rescore/inventory receipts in `activation_circle_audit_final01`.
Earlier primary and continuation evidence is preserved unchanged.

The user's bounded [GPU optimization](ACTIVATION_GPU_OPTIMIZATION.md) produced
roughly2x faster closure execution with float64, model and solver controls
unchanged. Its complete GELU validation differs by at most3.8e-13 in saved
circle predictions. The temporary GPU0-only restriction was explicitly lifted;
both GPUs were used to finish the experiments. The user directed ending the
speedup search, and no further performance investigation was conducted.

The requested [RMS versus P plots by activation](../../data/generated/neural_response_memory_20260922/activation_circle_rms_by_activation02/rms_vs_P_common_mse_0p1.png)
show tanh, GELU and sigmoid in distinct colors with separate task panels.
Training MSE 0.1 is the deepest saved milestone shared by all three activations,
all three closure orders and both tasks. The separate
[fitted MSE 0.001 plots](../../data/generated/neural_response_memory_20260922/activation_circle_rms_by_activation02/rms_vs_P_fitted_mse_0p001.png)
explicitly omit the unavailable sigmoid-quadrant comparison. These are presentation
artifacts from the frozen deep-circle and final activation metrics, with no new
experiments or changed analysis. Root generated and visually checked them;
activation_audit independently checked the 33 available values, matching
initialization/data/query hashes and numerical gates. The output directory also
contains PDFs, the exact CSV values and a manifest with input/output hashes and
the reproduction command; [plot source](plot_circle_activation_orders.py).

### Response-adapted clocks and history regularity (2026-09-25)

The user asks whether the chronological coordinate can distribute forward and
backward changes evenly and give derivative bounds for efficient polynomial
compression. The theory-only [clock synthesis](RESPONSE_CLOCK_DESIGN.md)
derives a causal response-arclength clock, its exact Lipschitz and coordinate
caps, and its optimality for normalized unweighted first-derivative energy.
The original accumulated RMS-residual clock removes residual magnitude but
does not by itself equalize response speeds. Parameter-metric arclength has
rate sqrt(-loss derivative), a different quantity.

For the existing unweighted history reconstruction, changing clock rate to g
also changes the encoded backward history to r delta/g. The synthesis derives
its exact derivative and gives a concrete fourth-root-loss clock with bounded
encoded-history derivatives on bounded parameter regions, automatically on
each finite horizon of the finite tanh gradient flow. A conservative
polynomial state envelope supplies global derivative caps with potentially
large width-dependent clock length. A matching artificial prefix with a
known matrix subtraction repairs the original backward-prefix jump.

A separate derived variant retains the learning measure rho dt while adapting
the polynomial coordinate. Its finite Gram matrix replaces diagonal Legendre
normalization. Cancellation of coordinate-transport terms makes the response
derivatives, then a response-speed clock, explicitly computable from the
closure's own current state. This variant has not been implemented or tested.

Root read the full scoped [arclength](RESPONSE_CLOCK_ARCLENGTH_CHECK.md),
[encoded-history](RESPONSE_CLOCK_HISTORY_CHECK.md), and
[weighted-projection](RESPONSE_CLOCK_WEIGHTED_CHECK.md) reports. Their assigned
algebraic checks and root's derivation check support the stated finite-system
identities and conditional bounds; precision corrections were incorporated.
These are collaborative internal checks, not promotion reviews. Root owns the
synthesis and this entry; the three scoped agents own their separate reports.

Finite total variation, bounded normalized-interval complexity, useful
width/population control, Gram conditioning and closed-loop accuracy remain
distinct obligations. Geometric task compatibility alone has not supplied
them. No clock is proved most efficient for actual Legendre tails, and no new
training experiment, maintained-source change, promotion or Git write occurred.
The next mathematical bottleneck is simultaneous control of history
regularity and accumulated clock length.

The follow-up [complete closure explanation](RESPONSE_CLOCK_FULL_CLOSURE.md)
fixes the matching-prefix, unscaled Euclidean-monitor version and gives the
full multi-input initialization, matrix-free actions and derivative evaluation
order. Its elementary weighted-projection proof yields the same-history
Frobenius bound A L^2/(2n max(1,P-1)) for every P>=1, where A=G_00 is the
integration-measure mass. The P=1 case uses a constant comparator; for larger
orders a Bernstein comparator is used only in the proof. The bound does not
compare separately evolved network trajectories. Two bounded scoped checks
confirmed the proof constants/prefix subtraction and computational equations;
root read both complete responses. This clarification adds no implementation,
experiment, uniform-order length bound, or training-accuracy theorem.

### Width-2048 closure fitting transfer (2026-09-25)

The user explicitly returned to this study's original activation closure after
the temporary width-2048 dense fitting and step-halving investigation. This
continuation keeps the same three hidden layers, ReLU/GELU/SELU definitions,
eight samples of each hard circle task, initialization, mobilities, and original
residual-activity Legendre closure. It tests P=1,2,3 at training MSE <=1e-8,
using simultaneous fixed Euler and sufficient physical training time. It does
not implement the alternate response-clock variants above.

The [protocol](CLOSURE_TRANSFER_2048_PROTOCOL.md) freezes the comparisons,
finite budgets and conditional refinement branch. New study-local sources are
[the Euler runner](closure_transfer_euler.py),
[campaign controller](closure_transfer_campaign.py), and
[RMS analysis](closure_transfer_analysis.py). The
[independent check](CLOSURE_TRANSFER_2048_CHECK.md) reconstructs physical
matrices and rescores saved predictions without importing the producer.

Generated products use this study's `closure_transfer_2048_*` namespaces.
`closure_transfer_2048_inputs01` preserves the six finest fitted dense
references, their immediately preceding fitted predictions, exact producer
versions and provenance from the authorized temporary investigation.
`closure_transfer_2048_campaign01` retains every new attempt and raw endpoint.

All 18 closure combinations fitted to MSE <=1e-8 at both the initial and
half Euler step; all 36 endpoints passed independent replay. Two extra
refinements also fitted. Further runs were stopped at the user’s request.
The [final results](CLOSURE_TRANSFER_2048_RESULTS.md) report all 18 RMS scores
and remaining numerical qualifications; generated final tables and plots are
in `closure_transfer_2048_final01`.
These are internal one-seed finite-width experiments, not promoted theory or
maintained API changes. No Git write or promotion was requested.

### Accumulated-error comparison with dense training (2026-09-25)

The user supplies an oracle-comparison report and asks whether it closes an
actual closure-versus-dense error theorem. The new
[finite-horizon proof](ORACLE_FINITE_HORIZON_BOUND.md) establishes, for the
original zero-backward-prefix activity-clock closure, global existence for
every P>=1 and an explicit O_T(P^-1) bound on the full physical parameter
trajectory against the separately evolved dense tanh network. Width, data
and horizon are fixed. Arbitrary finite data and finite initial arrays are
allowed; fitting, compatibility and backward-history variation assumptions
are unnecessary for this finite-time conclusion.

The proof controls the signed accumulated middle-weight discrepancy, not
the time integral of the defect norm. Readout energy, projection
contractivity and exact raw-moment representations give bounds independent
of P for all physical weights and the original activity length. The forward
history alone has the required derivative bound. Its Legendre projection
error, paired with a bounded backward source, yields the accumulated error;
an explicit physical-vector-field Lipschitz constant then gives integral
Gronwall comparison. This resolves the earlier finite-horizon bounded-region
and uniform-source obligations for the original two-hidden-layer tanh
closure. It does not resolve the older conditional all-time theorem.

The newer response-speed/weighted-Gram clock still requires uniform
control of its accumulated response length and regular existence to obtain
the analogous order convergence. A bound valid uniformly over all physical
time remains open for both variants. The
[book-source assessment](ORACLE_BOOK_SCOPE_CHECK.md) verifies the oracle
analogy and derives a bounded-accumulated-forcing corollary for the particular
fitted reference's linear propagator; its nonlinear transfer is unproved.

Root owns the proof and this entry. The scoped original-clock checker owns
ORACLE_FINITE_HORIZON_CHECK.md; the separate book-source checker owns
ORACLE_BOOK_SCOPE_CHECK.md. Root read the complete scientific arguments and
both full check reports. The original-clock theorem is internally checked:
the [finite-horizon check](ORACLE_FINITE_HORIZON_CHECK.md) records PASS for
the complete frozen proof, including its explicit constants and zero-residual
handling, at SHA256 bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1.
Its excluded source-attribution checks are covered by root and the separate
book-source assessment. These are internal checks, not promotion reviews.
No experiment, implementation change, established-source edit or Git-index
write occurred. Quantitative practical efficiency and width-uniform bounds
are not implied by the conservative finite-time estimate.

The user's clock-comparison follow-up yields a
[sharper conditional response-clock bound](RESPONSE_CLOCK_QUADRATIC_ORDER_BOUND.md).
Because the new insertion measure satisfies dmu<=dxi, the ordinary
Legendre projection can serve as a comparator for weighted best
approximation. Both matching-prefix histories have a controlled first
derivative, giving accumulated matrix error at most
L_P^2(L_P-1)/(2n P(P+1)) for every P>=1. With regular existence and a
P-uniform finite clock length, integral comparison gives O_T(P^-2)
dense-trajectory tracking. Those hypotheses remain unproved for this
newer clock; the original clock retains the unconditional O_T(P^-1)
theorem. The new bound improves the earlier conditional estimate but
does not prove superiority, an optimal rate, or useful constants.
Root and the scoped mathematical checker verified the comparator argument
and constants; the note records exact scope and check provenance. No
algorithm, numerical experiment or earlier frozen proof was changed.

### Closing the response-clock finite-horizon gap (2026-09-25)

The user authorizes a theoretical attempt to remove the new clock's
regular-existence and uniform-length assumptions. The completed
[theorem and proof](RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md) establishes:
for every fixed finite dataset, width, finite initialization and physical
horizon T, every sufficiently large P has a unique regular response-clock
closure through T, a clock length bounded independently of P, and full
physical dense-trajectory error O_T(P^-2). Positive initial residual is
handled by the regular equations; zero initial residual uses the already
specified stationary return. The algorithm, unscaled monitor, insertion
measure and matching prefix are unchanged.

The decisive exact identity is D_f'=rho||f-fstar||^2, where D_f is the
squared weighted history-projection residual. Coordinate dilation cancels
from the fitted energy. This converts the polynomial error estimate into
an integral-of-norm bound on the middle velocity defect. A coarse version
of the same identity bounds physical path variation independently of P
and clock length. Away from zero residual it bounds the response clock;
the sharper error estimate and dense residual lower bound then close a
first-exit argument for sufficiently large P. The prefix Gram prevents
moment-state breakdown at each such fixed order. All threshold and error
constants are explicitly determined by the initial data and T.

This supersedes the previously open finite-horizon clock-length and
continuation obligations in the immediately preceding conditional bound,
with the precise quantifier P>=P0(T). It does not prove global regularity
of every fixed small order, uniform accuracy over all physical time,
width-uniform approximation, or useful numerical conditioning/complexity.
The theoretical P0 and constants may be extremely large.

Three fresh scoped routes initially used only the complete specified
closure and conditional quadratic bound. All independently derived the
energy identity before cross-pollination. Their full reports are
[endpoint route](RESPONSE_CLOCK_ENDPOINT_ROUTE.md),
[energy route](RESPONSE_CLOCK_ENERGY_ROUTE.md), and
[obstruction route](RESPONSE_CLOCK_OBSTRUCTION_ROUTE.md).
Root read all three complete derivations and independently checked the
merged proof. The endpoint and obstruction routes then read all 392 lines
of the frozen synthesis and appended full mathematical audits: both PASS,
with no blocking correction, at SHA256
dda4d7b386b13129f30a64e6012b553b6ba783c41ed932874d98a93788ca7027.
Root read both complete audits and rechecked the unchanged candidate hash.
This is an internally checked result, not a promotion review or addition
to established material. Root owns synthesis/this entry; each scoped route
owns its report. No experiment, implementation change, established-source
edit or Git-index write occurred in this theoretical continuation.

### Fixed-depth and activation extension of both clock theorems (2026-09-25)

The user requests generalizing the old/new error theorems to every fixed
finite hidden depth and the activations considered here. The completed
[theorem and full proof](DEEP_ACTIVATION_ERROR_THEOREM.md) extends the original
activity closure to layer-dependent C^{1,1}_loc activations with O_T(P^-1)
physical-weight tracking, and the new shared response clock to
C^{2,1}_loc internal activations (C^{1,1}_loc suffices in the first layer)
with O_T(P^-2) tracking. Each internal learned matrix is compressed, while
every initialized matrix and its actual transpose remain exact. The common
width, dataset, depth and physical horizon are fixed before P tends to infinity.

For arbitrary globally defined activations in these smooth classes, the
closure existence/tracking statements hold for every sufficiently large
P at each finite T. No global activation/derivative bound or task-fitting
assumption is imposed. Dense gradient energy gives an initial-data compact
ball; a stopping argument establishes closure continuation there. This covers
unbounded exact GELU as well as tanh and sigmoid. For globally bounded
activations with bounded slopes, a separate downward physical-bound induction
establishes old-clock global existence and its finite-horizon estimate for
EVERY P>=1 at any fixed depth, including tanh and sigmoid.

The new depth step in the old proof controls forward-history derivative
energy recursively: the possible P growth of a backward endpoint projection
cancels its preceding forward projection's P^-2 energy factor. The new-clock
proof uses the exact endpoint energy identity jointly across all links and
samples. Its unscaled shared monitor gives integrated defect at most
L^2(L-1)/(4nM P(P+1)), followed by a derived P-independent clock bound and
physical/residual continuation. Depth still enters the constants; no
depth-uniform, width-uniform or uniform all-time estimate is asserted.

Literal ReLU and standard SELU require a different nonsmooth conclusion.
Their selected backward responses can jump, and the continuous new clock
does not turn those jumps into absolutely continuous histories. The
[activation analysis](DEEP_ACTIVATION_SCOPE.md) gives explicit finite examples
of nonunique selected ReLU flow and nonexistence of selected SELU continuation.
Both smooth rates transfer conditionally on a positive preactivation margin
through the chosen dense horizon. A general theorem across switches,
including the appropriate nonsmooth solution/clock convention, remains open.
These theoretical examples do not reinterpret finite-step experimental runs
as solutions of a newly specified nonsmooth dynamics.

Root owns the synthesis and this entry. Fresh scoped routes own
[old-clock derivation](DEEP_OLD_CLOCK_ROUTE.md),
[new-clock derivation](DEEP_NEW_CLOCK_ROUTE.md), and the activation analysis.
Root read their complete original arguments. The new-clock and activation
routes then each read and checked all 565 lines of the final synthesis,
SHA256 57e6e16b9af6ea32dd3cbc266f1c5b9054ae63219ce8e191bffdb3b87f44d8dd:
both full mathematical checks PASS with no remaining required correction.
The old-clock route also checked all 565 final lines, confirming the distinct
endpoint estimate and bounded-activation corollary without a required correction.
Root read all three complete version-specific audits. The earlier request to
make the SELU boundary derivative explicit is preserved with the original
reviewed hash and resolved in the final version. These are collaborative
internal checks, not promotion reviews; the results remain study material.

The new deep closure is specified as an explicit autonomous finite ODE,
with 2MnP(H-1) moving history entries and one shared Gram for the new clock.
It has not been implemented or experimentally tested. No training campaign,
maintained-source change, promotion or Git-index write occurred. The earlier
two-layer proofs and empirical records remain unchanged. The unresolved
extension is nonsmooth crossing dynamics; practical constants and numerical
conditioning remain separate from the proved closure-order convergence.

### Scalar aggregate compression: cutoff error and a stabilized variant (2026-09-25)

The user asks whether the population-to-aggregate construction is principled
and whether the history-closure comparison can prove finite-horizon scalar
output accuracy. The [assessment and full proofs](SCALAR_COMPRESSION_BOUND_ASSESSMENT.md)
read the complete existing aggregate derivation and checks. The target is
specifically the finite-width, fixed-P, OLD-clock, three-hidden-layer tanh
population closure. The new weighted response clock does not yet have a
corresponding scalar compiler in this study.

The exact connected-diagram hierarchy and its finite zero-tail deletion rule
are algebraically principled. Accumulated-defect and output-propagator
comparisons transfer exactly. A new finite-template argument proves a common
positive interval of existence and convergence for the ORIGINAL scalar rule
at fixed n,P: total diagram-size growth is bounded, absolute row coefficients
grow at most linearly in size, and an error at the cutoff requires increasingly
many dependency steps to reach a fixed output. This gives an explicit
geometric-times-polynomial local error bound. Unconditional convergence of
that unmodified rule on every prescribed finite T remains open. Generic
connected-moment counterexamples show why bounded targets, small deleted
sources and exact residual/clock feedback alone cannot prove it; these
examples are not asserted to be neural instances.

There is now a separate positive finite-horizon theorem for an explicitly
SATURATED variant. Preprocessing derives R from the parent initial-data
bounds through T, so every true diagram obeys |q_H|<=R^size(H). Each scalar
RHS is evaluated using componentwise clipping at those thresholds, including
the reported output used in the residual; the clock stays unclipped. This
modifies the finite algorithm but leaves the target equations unchanged.
Bounded RHSs give global existence for every finite cutoff, and a uniform
exponential envelope for the scalar trajectories. The same graded error
recursion then proves uniform output convergence on any prescribed finite
T without a population refresh. The explicit bound is
2N R_T^3 4^(-floor(K/(delta 2^N))) once the retained grade is sufficiently
large, where N=max(1,ceil(16 C_T delta T)); every constant is derived from
initial bounds and finite generator templates, independent of K. The
constants and necessary cutoff can depend strongly on n and P.

Combining this stabilized scalar theorem with the old parent history theorem
gives dense-output error bounded by the scalar cutoff term plus
C_T/sqrt(P(P+1)). Thus, at fixed finite width and horizon, choosing P and
then K gives any prescribed accuracy for finitely many included training
or passive-query outputs and their losses. This is an existence/error
theorem, not a useful small-state, width-uniform, all-time, population-limit,
numerical-conditioning or computational-efficiency result. The sharper
new-clock P^-2 term requires a separately derived scalar compiler.

A structural pruning lemma also shows that the ordinary output/mean/Gram
starting observables generate forests under the current rooted substitutions.
Cyclic diagrams can therefore be removed without changing those finite-cutoff
output equations on their common existence interval. This removes the raw
parallel-edge divergence example from the output-generated subsystem, but
does not prove width limits or tree-tail decay.

Root owns the synthesis and this entry. Fresh scoped routes froze independent
derivations before mathematical exchange: [error transfer](SCALAR_ERROR_TRANSFER.md),
[positive convergence route](SCALAR_POSITIVE_ROUTE.md), and
[truncation obstructions](SCALAR_TAIL_OBSTRUCTION.md). Their post-freeze
addenda distinguish collaborative checks and the subsequently proposed
saturation repair from their initial conclusions. All work remains internal
study material. No scalar solver implementation, experiment, training run,
established-source edit, promotion or Git-index write occurred.

The positive and obstruction routes subsequently checked the complete final
706-line synthesis, SHA256
e80540f9052049ee6e805037af99a57a83aa9acd0d98a3ff1f42d2ff39cd5309.
Both collaborative mathematical audits PASS with no remaining required
correction, including the saturation repair and explicit grade-halving
certificate. The error-transfer route separately derived and checked the
saturation theorem and a computable recursive cutoff certificate. Root read
all original routes, subsequent derivations and version-specific audits.
These are internal checks, not independent promotion reviews.
