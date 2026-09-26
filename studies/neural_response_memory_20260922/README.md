# Evolving response states for neural memory

## Current experiment entry point (2026-09-26)

The requested consolidation is now the three-file suite documented in
[CANONICAL_FLOW.md](CANONICAL_FLOW.md): `compact_flow.py` supplies the common
MLP/trainer, `frozen_dictionary.py` supplies frozen initialization bases, and
`run_compact_flow.py` runs [saved experiment configs](experiment_configs.json).
Methods are dense flow, evolving response-memory closure, old frozen circle
dictionary, frozen gradient-flow dictionary, and Gaussian/orthogonal controls.
Toy circle/sphere tasks, partial-support/high-frequency settings, MNIST and
arbitrary NPZ data share this interface. No normalization is enabled.

The historical dictionaries retain their two-hidden-layer tanh/2D scope and
initialization. The old circle implementation is Chebyshev/action-word based;
it is not renamed Hermite. Other MLP settings use dense, response memory, or
random bases with explicit ranks. No new dictionary derivation is claimed.

Implementation checks: 2,136 CPU assertions, maximum error 1.33e-15; exact
reproduction of the original 1,000/1,984-row MNIST panel; width-2048 CUDA graph
updates identical to eager updates; all supported historical dictionary orders
and Gaussian/orthogonal controls checked against their original producers.
Evidence is under `data/generated/neural_response_memory_20260922/unified_suite01/`.
These are consolidation checks, not a new fitting campaign or proof of closure
accuracy. The previously reported underfit/divergent cases remain unresolved.

65 retired scripts, plus the previous canonical files, are preserved byte-for-byte
in `legacy_experiments.zip` with checksums. Historical Markdown commands reference
that source archive; the Git rollback checkpoint is `87cade22a12323227d076e92f8801a1bdb7c21c0`.
Scalar compression, including concurrent exploratory work, is untouched. Root owns
only this consolidation's core/config/check/archive and this README/guide update.
No established code or theory was changed or promoted. Earlier sections below
remain the historical research record.

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

### Selected Fourier circle readout for scalar dynamics (2026-09-25)

The user first asks whether the fitted scalar closure can recover a whole
circle function/RMS without an evolving passive query mesh, then explicitly
selects the Fourier route. The completed
[design and derivations](SCALAR_CIRCLE_FUNCTION_READOUT.md) retain angularly
integrated contraction coordinates with Fourier test weights. Correlations
sharing the same angle stay inside one integral; only components disconnected
in both neuron and angle indices factor. This yields a finite-template exact
hierarchy and a scalar compiler, not a Fourier-coefficients-only closed ODE.

The selected solver has one autonomous training block and 2J+1 passive
angular blocks. With the same diagram list and a static weight tag in every
copy, plus pure angular constants as zero-derivative coordinates, every
unclipped block has the same matrix law Q_w_dot=A_K(q_train,L)Q_w.
The stabilized version uses clipped inputs in that law, so it is nonlinear
in the raw angular coordinates. The matrix and coefficient table are shared
across modes; training residuals still use the original training coordinates,
with their dictionary and caps unchanged. No angular function, query mesh
or neuron state is hidden in a runtime scalar.

The preceding saturated finite-horizon proof extends to these integrated
contractions: normalized angular integration preserves product bounds;
query replacements have bounded size/factor increase; and row coefficients
grow at most linearly in grade. Fourier readouts have grade 5 and the tagged
output-energy readout has grade 8 under the common convention. The explicit
cutoff bound therefore uses maximum readout grade 8. At fixed n,P,J,T all
included coefficients and energy converge as K increases.

The finite Fourier sum is an O(J) arbitrary-angle evaluator. Parseval gives
its whole-circle RMS without a runtime evaluation mesh. A separate energy
A=integral f_P^2 accounts for the target network's omitted spectral energy:
A-sum_(|k|<=J)|c_k|^2 is exactly its squared Fourier tail. The approximate
difference needs the proved coordinate-error margin to become a certificate.
For a bandlimited reference g, A and only its supported coefficient band
give the parent network's full RMS without a learned-function tail term.
No Fourier support is assumed for the actual reference without its definition.
The RMS of the returned polynomial and the estimated parent-network RMS
remain distinct finite-cutoff readouts.

Angular H1 bounds yield an explicit inverse-bandwidth error. A further
elementary complex-tanh argument derives a positive common strip from
finite-time weight row-sum bounds, giving exponential Fourier tails for this
finite three-hidden-layer tanh target. Combining these with the scalar K
error and old history P error gives whole-circle dense-function accuracy on
a common prescribed finite interval. Strip width and all practical constants
can be poor and need not be uniform in neural width.

This is a mathematical design, not an implemented or benchmarked solver.
Preprocessing still needs integrals of initialized contractions and may use
quadrature. Scalar storage grows with the auxiliary pattern count as well as
2J+1; no small-state or speedup claim follows. Missing mode blocks cannot be
initialized at a late training time without additional information or a
rerun. Training endpoint and unlimited-time accuracy remain separate claims.

The independent [decoder assessment](SCALAR_DECODER_LIMITS.md) also constructs
an alternative polynomial-to-Fourier terminal readout from sufficiently rich
training-only contractions. It prevents a blanket claim that every new-angle
readout requires passive query augmentation, but adds an activation-polynomial
approximation and does not recover labelled weights. A precise deterministic
finite-cutoff collision limits exact universal decoding on its stated broad
family, without asserting a no-go result for the prescribed Gaussian orbit.

Root owns the synthesis and this entry. Fresh scoped routes froze first
reports before exchange: the decoder assessment,
[Fourier construction](SCALAR_FOURIER_READOUT.md), and
[integrated RMS construction](SCALAR_RMS_OBSERVABLE.md). Their full arguments
and post-freeze checks are retained. The Fourier route read the entire final
552-line synthesis at SHA256
c771be0dee6d4672fb9a6db7f3c64295bf63a0760e884285dd04a67ee1918a77,
with no required mathematical correction. Root read all route arguments and
the subsequent checks. The integrated-RMS route also read the complete same
552-line version and recorded no required correction, including the explicit
complex strip and energy-tail certificate. These are collaborative internal
checks; no promotion,
experiment, solver implementation, maintained-code edit or Git-index write
occurred.

### Compact practical implementation (2026-09-25)

The user requests a short, fast replacement implementation and a quick fitting
check. The pre-change study source is snapshotted at commit
`915fdcda684a945ace8024ea77c5ad1fa8a93fa6`; generated evidence remains in data/.
`compact_flow.py` is the new single study-local entry point for dense dynamics
and the original residual-activity Legendre population closure at arbitrary
positive hidden depth, with scalar output and common width. It uses already
scaled input coordinates, preserving the earlier circle convention.
The initial practical choice is float32 and fixed simultaneous Euler step
0.0625 shared across ReLU/GELU/SELU, with complete GPU update blocks and loss
checks only between blocks. Custom activation/value-derivative pairs and
float64 remain available. This is a practical finite-step solver, without a
claim of numerically resolved continuous-gradient-flow predictions.

The quick check uses width 2048, depth 3, seed 20260920, the two existing
8-sample hard circle tasks, and dense/P1/P2/P3 for all three activations.
Success means training RMS near 0.05 (0.065 is acceptable per the user).
Both GPUs are authorized. Each task worker has a 115-second total budget;
each individual fit has an 8-second budget and at most 12000 updates.
There are no automatic step refinements or repeat campaigns. Results,
source hashes and training predictions go into a fresh
`data/generated/neural_response_memory_20260922/compact_quick01/` directory.
Root owns the driver and this README section; activation_engine owns the
module; activation_audit owns a short CPU comparison with the original
implementation and an independent dense-gradient check. This is study code,
not a promotion into maintained code/ or established theory.

Quick-check outcome: all **24/24** fits reached RMS <=0.05 using the same
step 0.0625, with no retries or refinements. Task-worker elapsed times were
9.42 seconds (outliers) and 11.68 seconds (quadrant), including model
initialization, capture, fitting and result writes, excluding Python/CUDA
process startup. Individual model times were 0.59–1.36 seconds.
SELU/quadrant/P1 reached RMS 0.038735 in 0.997 seconds including initialization.

| Task | Activation | Dense RMS | P1 RMS | P2 RMS | P3 RMS |
|---|---|---:|---:|---:|---:|
| two_outliers | relu | 0.03730 | 0.04717 | 0.00857 | 0.04504 |
| two_outliers | gelu | 0.04413 | 0.04400 | 0.04672 | 0.04695 |
| two_outliers | selu | 0.04926 | 0.04412 | 0.04682 | 0.03336 |
| quadrant | relu | 0.02213 | 0.02062 | 0.01392 | 0.01587 |
| quadrant | gelu | 0.04729 | 0.04755 | 0.04688 | 0.03250 |
| quadrant | selu | 0.04206 | 0.03873 | 0.04801 | 0.04720 |

The tiny CPU check passed 1122 assertions against the original equations
and independent autograd gradients (depths 1,2,3,4 and a custom activation);
maximum absolute discrepancy was 2.22e-16. A separate GPU graph/eager check
at width 16, depth 4, SELU, dense/P1/P3, float64 and 64 steps of 0.001
gave exact equality for every stored state tensor. These are implementation
and fitting checks. Coarse float32 fitted predictors are not certified to
match the earlier fine-step float64 circle predictions. The default step is
a useful tested starting point, not a universal stability guarantee for
arbitrary depth/data/activation. Generated tables, predictions, source hashes
and check results are in `compact_quick01/`.

Minimal use:

```python
from compact_flow import Flow
model = Flow(inputs, labels, width=2048, depth=3, activation="selu",
             order=1, device="cuda:0")  # order=None selects dense
result = model.fit()  # step=0.0625, target RMS=0.05
prediction = model.predict(test_inputs)
```

Reproduce (use a fresh output directory; the task runs may run concurrently):

```text
python -B studies/neural_response_memory_20260922/check_compact_flow.py
python -B studies/neural_response_memory_20260922/quick_compact_flow.py --task two_outliers_alternating --device cuda:0 --out data/generated/neural_response_memory_20260922/compact_quick02/two_outliers
python -B studies/neural_response_memory_20260922/quick_compact_flow.py --task quadrant_alternating --device cuda:1 --out data/generated/neural_response_memory_20260922/compact_quick02/quadrant
```

The user next requests closure-versus-dense test RMS over the full circle for
this fast configuration. Repeat the same 24 short fits, with unchanged seed,
step, precision, stopping target and budgets; evaluate 8192 equally spaced
circle angles in batches of 512. Compare each closure with the dense fit of
its activation/task, at their respective RMS<=0.05 stopping blocks. Save all
circle predictions and scores under `compact_circle01/`, with no step search
or extra refinements. This measures finite-step fitted-predictor agreement;
small training RMS alone does not ensure small circle discrepancy. Root owns
this small driver extension and reporting.

Whole-circle result: all 24 reproduced training prediction vectors match
the preceding quick check exactly. Independent rescoring of the saved 8192
query arrays reproduces every reported RMS. The task workers took 9.52 and
11.80 seconds including query evaluation and saving (excluding process startup).

| Task | Activation | P1 circle RMS | P2 circle RMS | P3 circle RMS |
|---|---|---:|---:|---:|
| two_outliers | relu | 0.223247 | 0.156155 | 0.097738 |
| two_outliers | gelu | 0.316418 | 0.194117 | 0.146945 |
| two_outliers | selu | 0.330222 | 0.233538 | 0.210953 |
| quadrant | relu | 2.678329 | 2.145159 | 1.700237 |
| quadrant | gelu | 3.905899 | 1.690744 | 1.530945 |
| quadrant | selu | 2.874368 | 1.647355 | 3.223783 |

The fast configuration fits, but does not preserve close dense/closure
whole-circle agreement on the quadrant task. Step size, stopping accuracy
and precision differ from the older fine-flow comparison; this quick check
does not separate those numerical effects from closure approximation error.
Reproduce by adding `--circle 8192` to the quick driver commands above, with
a fresh output directory. Source and configuration hashes, predictions and
training RMS are in each task’s results.json and NPZ files.

A single bounded practical follow-up tests shared step 1/128 and training
RMS target 0.01 with the same float32 compact solver and 8192-circle score.
Purpose: see whether this one cheap adjustment reduces fitted dense/closure
circle discrepancies while retaining short runtime. All 24 cases are retained;
no order is selected after observing the scores. Each task worker has 115s,
each fit at most 12s/40000 updates; two workers run on the two GPUs. No sweep
or further automatic refinement is authorized by this check. Results go to
`compact_circle_practical01/`. A failure to improve a cell is retained and
reported; finite-P error need not improve with numerical refinement. Root
owns this bounded check and the small driver argument extension.

The one-setting follow-up completed all 24 fits below training RMS 0.01.
Task-worker elapsed times: 42.86s outliers and 59.92s quadrant, including
setup, capture, fitting, queries and saving, excluding process startup.
Independent rescoring from saved circle arrays matches all recorded scores.

| Task | Activation | P1 RMS | P2 RMS | P3 RMS |
|---|---|---:|---:|---:|
| two_outliers | relu | 0.179862 | 0.071926 | 0.004553 |
| two_outliers | gelu | 1.309716 | 0.207878 | 0.031848 |
| two_outliers | selu | 0.159029 | 0.062084 | 0.053636 |
| quadrant | relu | 0.609629 | 0.206658 | 0.159418 |
| quadrant | gelu | 5.665547 | 0.876013 | 0.321156 |
| quadrant | selu | 0.394943 | 0.412078 | 0.206584 |

15/18 closure scores decreased; all six P3 scores decreased, by factors
3.93–21.47. The three increases are GELU/outliers/P1 and P2, and
GELU/quadrant/P1. Thus smaller steps/tighter fitting do not guarantee a
smaller finite-order closure error. Practical recommendation: keep float32
and GPU blocks, use step 1/128, target RMS 0.01, and P3 where a single
useful closure order is wanted. The quadrant P3 discrepancies remain
0.159/0.321/0.207; these are improvements, not universally tiny errors.
No further sweep was run. This combined intervention does not isolate
step-size versus stopping effects or certify the continuous-flow limit.
Reproduce with the quick driver using --circle 8192 --step .0078125
--target-rms .01 --fit-seconds 12 --max-steps 40000 and fresh task outputs.

### Four-hidden-layer practical comparison (2026-09-25)

The user requests the same practical batch with one additional hidden layer.
Use the existing compact solver at depth 4 (three internal dense links), width
2048, seed 20260920, float32, shared Euler step 1/128, and training RMS target
0.01. ReLU/GELU/SELU, both literal 8-sample circle tasks, dense and P1/P2/P3
are unchanged. Compare each closure to its matching independently fitted
FOUR-layer dense predictor on 8192 circle angles at their own stopping blocks.
The only driver change exposes --depth; core equations and execution remain
unchanged and already have small depth-4 CPU and CUDA checks.
One worker per GPU, each with 115s total, 12s per fit and 40000 updates, without
sweeps/retries. A capped/nonfinite fit remains labelled and is not presented
as a successful target-RMS comparison. New results use `compact_depth4_01/`.
Root owns this continuation, driver and reporting; no promotion or Git write.

Depth-4 outcome: all 24 fits reached training RMS <=0.01. Training RMS
ranged from 0.006404 to 0.009848. Task-worker elapsed times were 44.19s (outliers)
and 63.54s (quadrant), including initialization, capture, fitting, 8192-point
circle evaluation and saving, excluding Python/CUDA process startup.
Individual model elapsed times were 2.47–9.11s. Independent rescoring from
the saved circle arrays agrees with all recorded RMS values.

| Task | Activation | P1 circle RMS | P2 circle RMS | P3 circle RMS |
|---|---|---:|---:|---:|
| two_outliers | relu | 0.197722 | 0.086208 | 0.028751 |
| two_outliers | gelu | 2.418437 | 0.733321 | 0.078736 |
| two_outliers | selu | 0.171561 | 0.095145 | 0.077838 |
| quadrant | relu | 0.452403 | 0.344536 | 0.260755 |
| quadrant | gelu | 6.856610 | 1.843187 | 0.166443 |
| quadrant | selu | 0.289389 | 0.088998 | 0.116327 |

P3 has the smallest observed error in five of the six cases; SELU quadrant
is best at P2. Relative to the depth-3 practical batch, P3 errors rise on all
outlier cases and ReLU quadrant, and fall on GELU/SELU quadrant. These are
one-seed finite-step comparisons, not depth/order monotonicity claims or
certified continuous-flow errors. The dense reference is depth 4 in every
new comparison. No retries, changed steps or other extra runs were performed.
Reproduce using the quick driver with --depth 4 --circle 8192 --step .0078125
--target-rms .01 --fit-seconds 12 --max-steps 40000, the same task/device
arguments, and a fresh output directory. Full scores: compact_depth4_01/circle_rms.csv.

### Implemented scalar Fourier closure (2026-09-25)

The user explicitly requests implementation of the selected scalar Fourier
route and a fitted whole-circle comparison on a small training set. The
frozen protocol is [SCALAR_FOURIER_EXPERIMENT_PROTOCOL.md](SCALAR_FOURIER_EXPERIMENT_PROTOCOL.md).
The study-local implementation uses three hidden tanh layers, width 16,
seed 20260920, the original activity clock and P=1 history order. Training
angles are 10 and 125 degrees, labels +1 and -1, a two-point subset of the
study's two_clusters_grouped task. No other study supplied research inputs.

[scalar_fourier_engine.py](scalar_fourier_engine.py) implements exact lifted
response templates, a reachable tree/shared-angle-forest compiler, finite
whole-monomial deletion, initialization by contraction evaluation and angular
quadrature, and a scalar-only runtime with a shared operator for all Fourier
blocks. This first practical witness is unsaturated and omits the optional
energy observable. The saturated convergence theorem does not certify it.

**Outcome: the tested K=5 scalar witness fails the prescribed accuracy target.**
All three solvers reach internal training RMS 0.0316228. Their fitted outputs
on 4096 circle angles give population-P1 versus dense RMS **0.0182228**, but
scalar-K5/J8 versus dense RMS **0.2109774** (25.11% relative; maximum sampled
error 0.3774303). The scalar Fourier function itself has training RMS
**0.1692530**: finite truncation fails to preserve agreement between passive
Fourier readout and the separately evolved training-output coordinates.

K=5 has 331 training patterns, 17 angular patterns repeated across 17 real
weights, and one clock: 621 evolving scalars with 133,358 retained equation
terms. Dense width-16 training has 560 moving parameters. Scalar compilation
took 6.69s, initialization 0.009s and integration 3.39s. K=7 stopped at the
predeclared 200,000-term cap before its dictionary was complete; K=9/11 were
therefore not attempted. This is a limitation of the tested computation,
not a claim that higher cutoffs cannot succeed or that Fourier readout is
intrinsically inadequate.

Tighter integration and doubled initial quadrature change the scalar final
curve by only 1.36e-8 RMS; dense/population refinement changes are below
7.2e-10. Dense and parent Fourier tails above J=8 are 0.00531 and 0.00485,
below the bandwidth-follow-up trigger. The failure is numerically resolved
for this finite test and predominantly concerns aggregate dynamics.

The independent study algebra audit passes exact primitive and retained-output
checks to about 2e-15, including nonzero histories, inverse-clock derivatives,
initialized transposes, same-angle factorization, zero-residual stationarity,
runtime autonomy and width-independent dictionary counts. See
[SCALAR_FOURIER_IMPLEMENTATION_AUDIT.md](SCALAR_FOURIER_IMPLEMENTATION_AUDIT.md)
and [check_scalar_fourier.py](check_scalar_fourier.py). This is collaborative
internal checking, not promotion review. The numerical refinement reproduces
the primary failure within the prescribed tolerance.

Full interpretation, method, reproducible commands and cost accounting are in
[SCALAR_FOURIER_IMPLEMENTATION_REPORT.md](SCALAR_FOURIER_IMPLEMENTATION_REPORT.md).
[run_scalar_fourier.py](run_scalar_fourier.py) produces matched references,
scalar fits and analysis; [plot_scalar_fourier.py](plot_scalar_fourier.py)
plots saved predictions. Raw states, failed compilation metadata, checks,
scores, source hashes, PNG/PDF comparison and a portable terminal Fourier
coefficient JSON are under `data/generated/neural_response_memory_20260922/scalar_fourier01/`.
The returned Fourier model evaluates arbitrary circle angles without network
weights or a mesh, with the measured error stated above.

Contributors: root owned protocol, experiment runner, plots, synthesis and this
README append; scalar_compiler owned the compiler; scalar_reference owned the
independent dense/population reference module; scalar_audit owned the checks
and audit report. No maintained code/book or Git-index changes were made.
The bounded implementation/test request is complete. Practical higher-order
accuracy and more economical aggregate dictionaries remain open; no further
campaign was launched after the declared stopping condition.

### Four additional circle tasks with the practical depth-4 solver

The user requests four other non-trivial earlier tasks. Select the four with
literal definitions already retained in this study: quadrant_pairs,
quadrant_center_edges, equal_mixed_odd, and two_clusters_grouped. The first
three extend the earlier five-task set; the fourth is the earlier separated-
cluster task (historically easier, but not the excluded semicircle control).
Definitions and source references are in compact_extra_circle_cases.json.
Use all EIGHT original equal_mixed_odd samples: the old four-point antipodal
quotient was exact for odd tanh and is inapplicable to ReLU/GELU/SELU.
No labels, angles or initial scales are changed otherwise.

Run the same 48 combinations: four tasks, ReLU/GELU/SELU, dense/P1/P2/P3,
depth 4, width 2048, seed 20260920, float32, simultaneous Euler step 1/128,
training RMS target 0.01, 32-update GPU blocks and 8192 uniform circle queries.
A task has 115s; a fit has 12s and 40000 steps. At most one worker per GPU,
no automatic retries or refinement; report every cap/failure as such.
Compare each closure against the matching dense activation/task/depth at
its own target stopping block. Root owns the small generic-case driver
extension, task file and report. New products use compact_depth4_extra01/.

Completed all 48 fits. 36 reached training RMS <=0.01; all 48
were below 0.04 (maximum 0.03971994). Twelve fits hit a time cap;
no retries were run. The per-task worker times, including prediction, were
quadrant_pairs: 52.47s, quadrant_center_edges: 115.23s, equal_mixed_odd: 14.27s, two_clusters_grouped: 115.24s.
These worker times overlap and should not be summed as wall-clock time.

Whole-circle RMS versus each matching dense endpoint, recomputed in float64
from the saved 8192-point predictions and checked against all 36 saved scores:

| Task | Activation | P=1 | P=2 | P=3 |
|---|---|---:|---:|---:|
| Quadrant paired labels | RELU | 0.16761 | 0.05269 | 0.01956 |
| Quadrant paired labels | GELU | 0.07951 | 0.03174 | 0.01038 |
| Quadrant paired labels | SELU | 0.06619 | 0.04139 | 0.01445 |
| Quadrant center/edges | RELU | 0.03281† | 0.01992† | 0.02731† |
| Quadrant center/edges | GELU | 0.06670 | 0.02315 | 0.01471 |
| Quadrant center/edges | SELU | 0.16277 | 0.04349 | 0.07252† |
| Equally spaced mixed labels | RELU | 0.00312 | 0.00397 | 0.00109 |
| Equally spaced mixed labels | GELU | 0.00782 | 0.01483 | 0.01007 |
| Equally spaced mixed labels | SELU | 0.02206 | 0.00188 | 0.00065 |
| Two separated clusters | RELU | 0.01201† | 0.00599† | 0.00348† |
| Two separated clusters | GELU | 0.00605† | 0.00699† | 0.00666† |
| Two separated clusters | SELU | 0.00071 | 0.00045 | 0.01582† |

† At least one compared fit stopped at a time cap before the 0.01 target.
Thus these are achieved endpoint comparisons, not matched-loss or matched-time
comparisons. In particular, SELU P3 on center/edges and separated clusters had
only 7.36s and 2.17s integration respectively because of the task-level cap;
their higher errors cannot establish deterioration with closure order.

Capped endpoints:

- quadrant_center_edges/relu/P1: training RMS 0.01953192, 12.016s integration
- quadrant_center_edges/relu/P2: training RMS 0.01316301, 12.004s integration
- quadrant_center_edges/relu/P3: training RMS 0.01248814, 12.006s integration
- quadrant_center_edges/selu/P3: training RMS 0.03971994, 7.361s integration
- two_clusters_grouped/relu/P1: training RMS 0.01088928, 12.001s integration
- two_clusters_grouped/relu/P2: training RMS 0.01064022, 12.013s integration
- two_clusters_grouped/relu/P3: training RMS 0.01082020, 12.001s integration
- two_clusters_grouped/gelu/dense: training RMS 0.01509159, 12.005s integration
- two_clusters_grouped/gelu/P1: training RMS 0.01717422, 12.008s integration
- two_clusters_grouped/gelu/P2: training RMS 0.01720660, 12.020s integration
- two_clusters_grouped/gelu/P3: training RMS 0.01714025, 12.006s integration
- two_clusters_grouped/selu/P3: training RMS 0.01729020, 2.165s integration

All P3 test RMS values are below 0.028 except SELU center/edges (0.07252).
Order improves agreement strongly on paired labels, but is not uniformly
monotone across tasks. This is a single-seed practical finite-step comparison,
not a gradient-flow convergence certificate. No solver equations were changed.
The full score table, training errors and stopping statuses are in
`data/generated/neural_response_memory_20260922/compact_depth4_extra01/circle_rms.csv`;
per-task JSON and NPZ files retain metadata and predictions.

### Direct passive-point scalar diagnostic (2026-09-25)

The user requests a single passive test input to isolate aggregate compression
from the Fourier readout. [SCALAR_POINT_PROTOCOL.md](SCALAR_POINT_PROTOCOL.md)
freezes the same width-16 three-hidden tanh task, two active points at10°/125°,
labels+1/-1, P=1 and seed20260920; the passive point is60°. It enters neither
the residuals, gradient denominator nor clock/history sources. The new
[scalar_point_engine.py](scalar_point_engine.py) uses ordinary connected-tree
coordinates with identical grade3 training/passive output roots, without
Fourier variables or angular quadrature.

**The K=5 scalar closure fails this direct-point test as well.** At each model's
first training RMS0.0316228, dense predicts0.6431604545, population P1 predicts
0.6163626931, and scalar K5 predicts0.2064426036. Scalar absolute error is
0.4367178509; matched-time error remains0.3693628213. Tightening integration
changes the scalar prediction by2.78e-9. A separate training-only control agrees
with the passive-point run's training outputs within7.41e-8 on the common panel,
confirming the point does not influence learning. The observed failure concerns
aggregate truncation itself, not solely Fourier extraction.

Independent exact-template checks pass at nonzero histories within2.09e-15.
All193 passive rows map exactly onto training rows when the passive input
duplicates a training input. This establishes consistent duplicate-input
bookkeeping, not accuracy for unseen inputs. See [SCALAR_POINT_AUDIT.md](SCALAR_POINT_AUDIT.md)
and [check_scalar_point.py](check_scalar_point.py).

K5 has525 evolving scalars and271606 retained terms; compilation/solve take
13.10s/7.78s. K7 was allowed2000000 retained terms, ten times the preceding
Fourier limit, but stopped at2000185 terms before finishing. No higher-order
accuracy result is available. Total recorded numerical phases are108.78s within
the600s campaign budget, plus27.08CPU seconds for independent algebra checks.
This tests the unsaturated reference truncation; it does not contradict the
separate saturated hierarchy theorem or establish practical compression.

[SCALAR_POINT_REPORT.md](SCALAR_POINT_REPORT.md) gives interpretation, controls,
resource accounting, reproduction commands and the existing terminal-polynomial
whole-function alternative. [run_scalar_point.py](run_scalar_point.py) runs
the experiment and [plot_scalar_point.py](plot_scalar_point.py) renders saved
solutions. Products, source hashes, raw states, scores and PNG/PDF plot are in
`data/generated/neural_response_memory_20260922/scalar_point01/`.
Root owns protocol, runner and synthesis; point_probe owns the engine;
point_audit owns independent checks; point_whole_function assessed the existing
decoder construction. No maintained code/book or Git-index edits occurred.

The user now explicitly authorizes theoretical and empirical improvements,
including several predeclared passive angles and alternative scalar closures.
That is the next active continuation; the negative diagnostic above remains
recorded and is not replaced by a later selected success.

### Three-dimensional inputs and larger training sets (2026-09-25)

Before this continuation, all current study source/notes were checkpointed at
`a0a058499c1748f9f100c31588ea770f611f6f4d`. Unrelated checkout changes and generated
data were outside that study checkpoint. The user requests the same practical
closure comparison with three input coordinates and more training samples.
This is a validation extension of the same dense/history-closure investigation.

Root owns quick_sphere_flow.py and this README append. The unchanged compact
solver uses four hidden layers, width 2048, Gaussian small-readout initialization
seed 20260920, float32, mobilities (n,1,1,1,n), probability MSE and fixed
simultaneous Euler step 1/128. Unit 3D directions enter directly, preserving
unit first-preactivation variance from the prior unit-circle convention.
Both GPUs are authorized, with at most one worker per GPU.

Predeclared batch: targets sqrt(15)*x*y and sqrt(105)*x*y*z on the unit sphere,
32 and 64 iid uniform training directions (normalized Gaussian seed 20260925,
nested sets), ReLU/GELU/SELU and dense/P1/P2/P3: 48 fits. These continuous
nonlinear targets have unit sphere RMS. Evaluate 8192 separate equal-area
Fibonacci directions. Primary metric is closure-versus-matching-dense test RMS;
also report training RMS and test RMS against the known target, so prediction
agreement is not confused with task generalization. Endpoints are independently
stopped, not necessarily matched physical times or exact losses.

Every fit receives its own 12s integration budget, at most 40000 updates,
and target training RMS 0.01 (0.05 remains practically acceptable). There is
no task-level budget that shortens a later fit. Stop after this one batch;
no automatic retries, seed selection, step search or refinement. Finite/capped
fits remain visible. Closure test RMS <=0.05 is a descriptive good-agreement
threshold; target test RMS <=0.1 is a descriptive strong-generalization
threshold (10% of unit target RMS), not a required gate used to select runs.
This is single-seed finite-step evidence, not a population/GF certificate.

The CPU generator check verifies unit norms, nested samples, and sphere target
RMS 1 to 1e-5 on the test grid. Existing compact-solver checks remain applicable;
no model equations change. Products use compact_sphere01/{xy,xyz}_m{32,64}/,
retaining input/query arrays, source hashes, exact commands, environment and
all model predictions. Reproduce using quick_sphere_flow.py --task xy --samples
32 --device cuda:0 --out <fresh-output>, and analogously for the other three
combinations. This bounded experiment is authorized by the current user request.

Completed the 48 predeclared fits, all with training RMS <=0.01 and no capped,
nonfinite, retry or refinement runs. Maximum training RMS was 0.00999955.
Each model took 1.50–8.35s including initialization, fitting and sphere queries.
Worker elapsed times were 35.61s/41.44s for the two 32-sample tasks and
57.33s/60.43s for the two 64-sample tasks. The two tasks ran concurrently on
the two GPUs at each sample size; worker times exclude process startup.
All four worker processes exited with status 0.

The unchanged source hashes and saved input-file hashes were verified after
execution. summarize_sphere_flow.py independently recomputes all 144 scalar
training/target/dense RMS values from the saved predictions, matching the
producer within 1e-12. This checks scoring, not discretization convergence.
Reproduce analysis with:
`python -B studies/neural_response_memory_20260922/summarize_sphere_flow.py data/generated/neural_response_memory_20260922/compact_sphere01`.

| Target | Samples | Activation | P1 vs dense | P2 vs dense | P3 vs dense | Dense vs target | P3 vs target |
|---|---:|---|---:|---:|---:|---:|---:|
| xy | 32 | RELU | 0.01311 | 0.01346 | 0.00520 | 0.07825 | 0.07851 |
| xy | 32 | GELU | 0.01434 | 0.01201 | 0.00548 | 0.08240 | 0.08488 |
| xy | 32 | SELU | 0.00562 | 0.00408 | 0.00129 | 0.09993 | 0.10030 |
| xy | 64 | RELU | 0.00857 | 0.00852 | 0.00351 | 0.05886 | 0.06037 |
| xy | 64 | GELU | 0.00870 | 0.00662 | 0.00267 | 0.04425 | 0.04499 |
| xy | 64 | SELU | 0.00260 | 0.00168 | 0.00063 | 0.07227 | 0.07245 |
| xyz | 32 | RELU | 0.02697 | 0.01498 | 0.00396 | 0.54853 | 0.54845 |
| xyz | 32 | GELU | 0.03181 | 0.02258 | 0.00687 | 0.44645 | 0.44570 |
| xyz | 32 | SELU | 0.01211 | 0.00593 | 0.00184 | 0.44454 | 0.44467 |
| xyz | 64 | RELU | 0.02193 | 0.01280 | 0.00454 | 0.27065 | 0.26828 |
| xyz | 64 | GELU | 0.01893 | 0.01845 | 0.00931 | 0.16146 | 0.16684 |
| xyz | 64 | SELU | 0.00875 | 0.00301 | 0.00132 | 0.16360 | 0.16430 |

Here xy/xyz denote the normalized target functions specified above. All 36
closure-versus-dense sphere errors are below 0.032; all 12 P3 errors are
below 0.01. P3 is best in every activation/task/sample-size comparison, although
P2 is slightly worse than P1 for ReLU xy at 32 samples. Increasing sample count
improves dense and P3 target RMS in all six activation/task pairs. It does not
uniformly reduce closure discrepancy (ReLU/GELU xyz P3 increase slightly).

The quadratic target generalizes well at 64 samples: dense target RMS
0.04425–0.07227 and P3 target RMS 0.04499–0.07245. The cubic target improves
substantially with more samples but retains appreciable error: dense target
RMS 0.16146–0.27065 and P3 target RMS 0.16430–0.26828 at 64 samples.
Those residual generalization errors also occur in the dense networks;
closure error is much smaller. This separates accurate dense approximation
from near-perfect recovery of the unknown target between training samples.
The evidence is one initialization and one nested data sample, with fixed
practical step/precision, not a broad statistical or continuous-flow claim.

Full 48-row metrics: compact_sphere01/sphere_rms.csv; compact summary and table:
summary.json and table.md in the same generated directory. The bounded user
request is complete, with no further runs queued. New sphere driver/analysis
sources and this result append are subsequent to the pre-experiment checkpoint.

## Scalar prediction alternatives and terminal decoding, 2026-09-25

The explicitly requested continuation after the single-passive-point failure
is complete. [SCALAR_VARIANTS_REPORT.md](SCALAR_VARIANTS_REPORT.md) records all
12 predeclared variants from [SCALAR_VARIANTS_PROTOCOL.md](SCALAR_VARIANTS_PROTOCOL.md),
the algebra checks, tolerance refinements, additional-angle validation and
unchanged-width branch. Products are in
`data/generated/neural_response_memory_20260922/scalar_variants01/`;
`scores_final.json` and `validation.json` are the authoritative scores.

The successful width-16 witness is a new response-basis scalar ODE with
12 modes per layer, selected solely from initial active responses and their
derivatives/products. Runtime uses modal scalars and fixed scalar tensors;
initial matrices/bases are detached into a terminal decoder. Its primary
passive RMS is 0.032077, decoded primary RMS 0.022075, and decoded whole-circle
RMS 0.016993 (4096-angle evaluation, sampled max 0.031275). The five additional
angles pass, with the report identifying their antipodal redundancy. No circle
mesh is evolved to obtain the terminal decoded function.

At width 32 the unchanged rank gives circle RMS 0.035234, but primary internal
RMS 0.070541 and decoded RMS 0.057436 miss the frozen 0.05 gate. This nonpass
remains explicit; pooling additional angles cannot change the primary rule.
Width-16 decoded training RMS is 0.041847 versus the scalar stopping target
0.031623. Training and decoder readouts are scored separately.

Frozen/tangent boundary K3 variants remain inaccurate; both K5 variants reach
the 50000-boundary cap. Four tiny polynomial-potential models also fail the
accuracy gates, including one that never fits by T=40. Full rank agrees with
dense outputs to 1.13e-8 but is an implementation control. Required refinements
change outputs by at most 3.68e-6. All recorded preparation/solver wall times
sum to 55.859 seconds. Raw failures, provenance and coefficients are retained.

[SCALAR_RESPONSE_BASIS_THEORY.md](SCALAR_RESPONSE_BASIS_THEORY.md) derives exact
internal loss dissipation at every rank and a conditional finite-time defect
bound. Small discarded-correlation errors, decoder consistency and width-
uniform accuracy remain open. The new result does not repair the old aggregate
cutoff or establish an unconditional scalar convergence theorem. Its moving
dimension is independent of width at fixed rank/query count, but static tables
and the decoder prevent a total-memory advantage at the tested sizes.
[SCALAR_VARIANTS_AUDIT.md](SCALAR_VARIANTS_AUDIT.md) independently recomputes
endpoint scores within its stated scope. These are internal study results;
no book/API promotion or additional search is implied.

### Restricted-support/high-frequency and normalized deep stress test (2026-09-25)

The user explicitly extends the same closure investigation to restricted input
support, rapidly changing labels, depths 10/15/20, and normalization while
preserving muP feature-learning scaling. Root owns the compact_flow.py extension,
check_normalized_flow.py, quick_normalized_stress.py, analysis and this append.
No subagents, maintained-code edits or new Git transaction are used.

LayerNorm has no affine parameters and uses epsilon=1e-5, independently for
each sample across neurons. Both phi(LN(z)) and LN(phi(z)) are implemented.
For u=(z-mean(z))/sqrt(mean((z-mean(z))^2)+eps), its exact Jacobian action is
Jg=(g-mean(g)-u*mean(u*g))/sqrt(var(z)+eps). Backpropagation differentiates both
mean and variance. The pre-activation placement applies J to phi' times g;
the post-activation placement multiplies Jg by phi'. There are no detached
statistics, frozen hidden layers or test-batch statistics.

With delta_l=n*d f/d z_l including this Jacobian, the gradient still factors
as r_a delta_l,a h_(l-1),a^T. Thus all hidden-link history states, sources,
activity clock and Legendre reconstruction keep their existing equations;
B's initial prefix now contains the normalized initial hidden features.
The learned dense increment remains replaced by the original P-order moment
closure; initialized matrices remain explicit and reused with their transposes.
Normalization does not convert this implementation into finite scalar closure.

The preserved width scaling is: first weights O(1), hidden initialized entries
O(n^-1/2), output c^T h/n, and probability-MSE mobilities (n,1,...,1,n).
Equivalently effective readout a=c/n has mobility 1/n. For O(1) neuron signals,
LayerNorm's mean and variance are O(1), and its Jacobian has width-independent
scale when variance stays nondegenerate; eps prevents a literal zero divisor.
Coherent hidden weight updates remain O(1/n) per entry and can produce O(1)
feature changes after contraction over n neurons. Applying ordinary constant
SGD learning rate to all stored blocks would instead change this regime.
The earlier c_i(0)~N(0,n^-2) small-readout initialization is retained (a
vanishing/zero-readout muP variant, not a claim of nonzero feature movement
on the very first infinitesimal step). Depth is fixed when width is varied;
no joint depth-width or arbitrary-depth stability theorem is asserted.

Primary references inspected: official MuSGD scaling and coordinate checks,
https://github.com/microsoft/mup/blob/main/mup/optim.py and
https://github.com/microsoft/mup#checking-correctness-of-parametrization;
LayerNorm definition https://arxiv.org/abs/1607.06450. The derivation above
and width-motion diagnostic are specific to this study's stored coordinates.

Predeclared stress batch: 64 samples, width2048, float32, seed20260920,
Euler step1/128, target training RMS0.01, 10 seconds per fit, 20000-update cap,
8-update GPU blocks, 8192 whole-manifold queries. No automatic retries or
step/seed searches. Each fit gets the full budget. Both GPUs, one worker each.
Four task/distribution pairs from quick_normalized_stress.py:
- circle_full: midpoint-spaced training over the whole circle; sqrt(2)sin(24theta).
- circle_patch: all points in a 90-degree arc; identical target (six cycles in arc).
- sphere_full: uniform-sphere samples; normalized sin(6pi x)sin(6pi y).
- sphere_patch: uniform northern cap z>=0.5 (quarter of sphere); same target.
The sphere tasks share azimuth/random quantiles (data seed20260926). Target
normalization uses the fixed full-sphere quadrature, independently of fitted
models. Labels are continuous regression values with frequent sign changes,
not randomized noise or binary classification. Data/query generation checks
verify unit norms, support, count and unit test-target RMS.

The main sweep is GELU, depths10/15/20, normalization AFTER activation,
dense/P1/P2/P3, all four tasks:48 fits. Depth20 GELU with normalization BEFORE
activation adds16 fits. Depth20 post-normalized ReLU and SELU on the two
restricted-support cases add16 fits. Two depth20 unnormalized GELU dense
controls complete the82-fit batch. This is a bounded design, not a full
activation/depth/normalization factorial. No residual connections or gain
rescaling are added to the unnormalized controls.

Primary question H1: fitted P3 still tracks matching normalized dense on the
whole manifold to RMS<=0.05; H0: challenging data/depth causes >0.1 errors.
Intermediate errors are mixed evidence. Training RMS>0.05, nonfinite states
or missing counterparts make fitted-model comparison inconclusive. Report
all achieved endpoints regardless. Separately report against-target errors,
and within-region/outside-region errors; for patch tasks the outside region
was completely unlabeled. Dense and closure stop independently, so capped
pairs are not matched-loss/time comparisons. Fixed-step results alone cannot
attribute a discrepancy to continuous-flow closure truncation.

Checks: the unchanged non-normalized path passes1122 prior CPU assertions
(max error2.22e-16). The new independent CPU oracle uses native PyTorch
layer_norm and autograd for both placements, all three activations,
depths1/3/10, dense and nonzero P1/P3 reconstructed states; it also checks
query-batch independence. Before the stress batch, one bounded coordinate
check tests GELU widths256/512/1024, depths10/20, both placements, at fixed
physical time2 (256 steps), on32 smooth sphere-xy samples. All hidden feature
RMS and movement are saved, so constant normalized norms alone cannot be
mistaken for feature learning. Maximum12 such probes, 10 seconds each;
no tuning from them. Their interpretation is a width-scaling diagnostic,
not a theorem. Numerical nonfiniteness in a probe stops scientific runs for
that normalization until a reported implementation issue is resolved.

Total primary integration cap820 summed GPU seconds; coordinate cap120,
plus CPU algebra verification and small post-fit query evaluation. Stop after
the declared batch. Outputs use compact_normalized_stress01/, retaining exact
commands, source/input hashes, environment, endpoint predictions and motion.
Previous empirical results remain valid for their original architectures;
small-error evidence from depth4 does not establish the new stress claim.

Stress batch complete:82/82 attempted,39 training RMS<=0.05,16<=0.01;
all other endpoints capped, none nonfinite. [NORMALIZED_STRESS_RESULTS.md](NORMALIZED_STRESS_RESULTS.md)
contains all20 model-group score rows, exact task definitions, normalization/
muP checks, resource accounting and qualifications. Generated evidence is in
compact_normalized_stress01/, especially stress_rms.csv and coordinates.json.

Evidence update: the exact finite normalization gradients and hidden-link
factorization pass independent autograd/reconstruction checks (282 comparisons,
max9.95e-14); the unchanged path still passes1122 checks. All12 width probes
retain nonvanishing hidden movement; four GPU graph/eager checks match exactly.
This supports the requested width scaling empirically, not a population-limit
or normalization-extended hierarchy theorem. All574 saved scalar RMS values
were rescored successfully, and source/input hashes match their producers.

The broader small-error expectation is disfavored for the current fast settings.
Fitted GELU circle cases at depths10/15 have P3 errors0.1201/0.2054 with no
monotone order improvement. ReLU after-normalization/depth20/sphere-cap has
training RMS0.0258/0.0370 (dense/P3) but test discrepancy0.8188, dominated by
outside-cap discrepancy0.9256. GELU full-sphere P3 errors0.0078/0.0276/0.1017
show a more favorable order trend. The failed-training rows remain
inconclusive as fitted comparisons. Under the cap, after-normalization is
generally preferable to before-normalization in this batch. Both agree with
muP width scaling; poor task fitting is not evidence of a lazy parameterization.

Target generalization is poor on these sparse high-frequency sphere samples,
including dense models with small training error. Closure agreement does not
repair that. No attribution to an intrinsic positive loss or exact-flow closure
floor is justified: the fixed step, different stopping times and width/seed
scope remain limitations. No old result is superseded beyond its original
smooth/shallow tested scope. Root completed the requested bounded continuation;
no additional tuning, refinement or promotion is running or queued.

### Fit-first focused high-frequency comparison (2026-09-25)

The user requests meaningful fitted dense/P1/P2/P3 comparisons on the four new
stress tasks, only width2048, with a small practical adjustment and no extended
optimization campaign. Root fixes one existing setup: ten hidden GELU layers,
after-activation non-affine LayerNorm, unchanged muP scaling and exact original
64-sample inputs/labels for circle_full, circle_patch, sphere_full, sphere_patch.
No normalization, depth or activation sweep is repeated. This narrowed setup
was stated to the user before execution and focuses the four data configurations.

The first adjustment is stopping at training RMS0.04 with up to30s per fit,
instead of cutting off at10s while pursuing0.01. Keep float32, shared Euler
step1/128, seed20260920 and8192 whole-manifold queries. First run dense and P3
on circle_patch, the known fitting bottleneck, in parallel. These are retained
and reused as final runs if both fit. Then execute the other14 combinations.
If either does not attain0.04, one bounded alternative uses the same data and
model with step1/512 and at most40s per bottleneck fit. This addresses possible
coarse-step oscillation without an open-ended sweep. If that succeeds, use its
step for the full final batch, retaining earlier failed attempts separately.
No further automatic branch, seed selection or change of labels is planned.
Primary metric is all-space RMS against the matching dense fit; training RMS
must be <=0.05 for all four models to call a task's comparison fitted.
The0.04 stopping margin avoids borderline reporting. Also retain target and
inside/outside-region errors. These remain finite-step, one-seed endpoints;
no claim of continuous-flow accuracy or improved generalization follows.

Maximum initial16 fits at30s, or2 pilots plus16 fits at40s if the single step
fallback is needed:700 summed GPU integration seconds at most, two GPUs, one
worker each. No new solver equations or repeated correctness campaign. Root
owns the focused driver/analysis and README append. Outputs use
compact_stress_fitted01/ with immutable attempt subdirectories, source/input
hashes, exact commands, environment and predictions. Scientific core and task
generator stay unchanged. Existing negative/capped results remain retained.

The first setting succeeded: all16/16 models reached training RMS<=0.04
(maximum0.03997976, MSE<=0.00159839). No fallback, smaller step, restart,
label/input change or additional fitting attempt was needed. Dense and P3
arc pilots are reused in the final batch. Model elapsed times including
initialization and test queries were3.56–28.35 seconds; the difficult arc
models took13.86–28.35 seconds. Total integration was 148.87 summed GPU
seconds, well below the declared cap. Every worker exited0.

| Task | Dense train | P1 train | P2 train | P3 train | P1 test | P2 test | P3 test |
|---|---:|---:|---:|---:|---:|---:|---:|
| circle_full | 0.03975 | 0.03958 | 0.03892 | 0.03935 | 0.10028 | 0.10342 | 0.11992 |
| circle_patch | 0.03911 | 0.03998 | 0.03958 | 0.03991 | 0.09362 | 0.12272 | 0.14049 |
| sphere_full | 0.03998 | 0.03971 | 0.03995 | 0.03988 | 0.02139 | 0.01206 | 0.00712 |
| sphere_patch | 0.03996 | 0.03981 | 0.03928 | 0.03992 | 0.07355 | 0.07551 | 0.09693 |

All test columns are RMS differences from the matching dense endpoint on8192
points across the ENTIRE circle/sphere, including the unlabeled complement of
the arc/cap. They are not errors against the true regression target. All four
models now satisfy the fitting gate in every task; there are no capped scores
in this table. Endpoints still have independently attained loss thresholds,
not exactly matched loss or physical time.

The earlier depth10 arc P3 discrepancy0.9942 at unfinished endpoints decreases
to0.14049 once both predictors fit to0.04; P1 falls0.9406->0.09362.
This directly shows why the underfit arc scores were not clean approximation
evidence. Meaningful nonzero errors remain: P1/P2/P3 do not improve monotonically
on either circle case or the cap; the full sphere improves0.02139->0.00712.
No inference about continuous-flow closure error or asymptotic order convergence
is made without step refinement. Target generalization remains separate:
dense/P3 full-sphere target RMS is1.25040/1.25057 despite their small mutual
error; dense/P3 arc target RMS is0.87030/0.86814.

All16 saved input, label, query and region arrays were checked bit-for-bit
against the original compact_normalized_stress01 task arrays. Used source
hashes match the current files. summarize_fitted_stress.py rescored every
training/target score within1e-12, verified common reference configurations,
input/query equality and archive checksums, and generated the final test scores.
No numerical core equations changed. All training in this continuation uses
only width2048. The focused fixed-depth/fixed-activation scope was explicitly
stated before execution; it does not replace the earlier depth/activation sweep.

Sources: fit_stress_tasks.py and summarize_fitted_stress.py. Reproduce a task
with `python -B studies/neural_response_memory_20260922/fit_stress_tasks.py
--task circle_full --device cuda:0 --out <fresh-root>` (one shell line), using
circle_patch/sphere_full/sphere_patch analogously. The --models option permits
the split arc schedule; exact commands are in each result.json. Analyze with
`python -B studies/neural_response_memory_20260922/summarize_fitted_stress.py
<root>` (one line). Final evidence:
`data/generated/neural_response_memory_20260922/compact_stress_fitted01/step128/rms.csv`,
`table.md`, `summary.json`, and the16 model subdirectories. The requested
fit-first comparison is complete; no further runs or tuning are queued.

### Fitted stress tasks: ReLU and SELU extension (2026-09-25)

The user requests the other activations and P=1,2,3 test RMS. Before running,
freeze the same four tasks, 64 samples, width2048, depth10, non-affine
LayerNorm after activation, seed20260920, float32, Euler step1/128 and
training RMS target0.04. Only the activation changes from the fitted GELU
batch. Run dense/P1/P2/P3 for ReLU and SELU: 32 primary fits, each capped
at30 integration seconds and60000 steps. At most one worker per GPU.
No task, labels, initialization convention or closure equations change.
The driver now exposes its existing activation argument. Save each activation
under compact_stress_activations01/<activation>/step128 and independently
rescore saved predictions on all8192 whole-manifold query points. Report
all training RMS and label any unfinished fit; do not count an underfit
endpoint as clean closure evidence. If the 30-second cap alone prevents a
fit, at most the two arc quartets may receive one extension run at60 seconds
per model with the same step, in separate retained attempt directories.
No further sweeps or refinement studies are part of this quick extension.

Bounded amendment after primary results: ReLU's three arc closures all reached
0.04 in the single extension (34–49 integration seconds). SELU closures also
fail on the full sphere, where its dense model fits quickly; merely extending
the arc does not address the common numerical setting. While the existing
bounded worker finishes, use the free GPU for one SELU/full-sphere/P1 pilot
at step1/512, 30 seconds, with every other setting unchanged. If its training
RMS reaches0.065 or lower, run the remaining SELU quartet comparisons at this
one smaller step (30 seconds each, 60 for the arc), retaining the pilot.
Otherwise stop this check. No further steps, seeds or architectures are tried.
This is an evidence-driven amendment before observing the smaller-step result;
all primary and extension results remain saved and explicitly distinguished.

The activation extension is complete. ReLU reached the0.04 training target in
all16/16 selected models; the three arc closures needed34–49 integration
seconds, with no change of step or task. Whole-space P1/P2/P3 errors are
0.05131/0.07427/0.06831 (full circle),0.77476/0.83307/0.77708 (arc),
0.05711/0.06814/0.05721 (full sphere),0.08382/0.15356/0.07333 (cap).
The large arc discrepancy persists after fitting and lies mostly outside the
observed arc (inside RMS0.0444–0.0460; outside0.894–0.962).

SELU did not transfer successfully under the same step: only3/16 models fit
(all dense except full circle). Dense full-circle train RMS0.31958;
closure train RMS0.71687–1.05046, even including the single arc extension.
These underfit endpoints must not be interpreted as clean closure accuracy.
The one step1/512 full-sphere/P1 pilot ended at train RMS0.23658 within30
seconds, above the declared0.065 gate; no follow-on sweep was launched.
Neither a fundamental SELU representation obstruction nor a positive closure
loss floor is established. All32 primary runs, six extensions and one pilot
are retained. The numerical core and all tasks remain unchanged, at width2048.

Full training and P1/P2/P3 test RMS table, caveats and reproduction instructions:
[COMPACT_STRESS_ACTIVATIONS_RESULTS.md](COMPACT_STRESS_ACTIVATIONS_RESULTS.md).
Machine-readable scores and selection manifests:
`data/generated/neural_response_memory_20260922/compact_stress_activations01/`.
All39 completed records passed source/input/archive checks; all selected scores
were independently recomputed from saved predictions. No further runs queued.

### Low-cost SELU fitting correction (2026-09-26)

The user explicitly reopens fitting of the underfit settings and requests a
very small fix. Keep the four tasks,64 samples,width2048,depth10,after-activation
LayerNorm,initialization,seed20260920,float32 and all dense/closure equations
unchanged. Test one smaller fixed Euler step1/1024 (eight times smaller than
the failed default) on full-circle/P1 and arc/P3,60 seconds per pilot, target
training RMS0.04 (<=0.05 is a fitted comparison; <=0.065 is acceptable partial
progress). If successful, reuse the pilots and run matching dense/P1/P2/P3
at this step on all four tasks, at most60 seconds per model initially. Allow
one bounded correction or extension if pilots identify the need, declared
before expansion; no optimizer, architecture, task or seed search. Preserve
all attempts in compact_selu_fix01/, including failed fits. Recompute training
and whole-manifold closure-versus-dense RMS from saved predictions and retain
matched solver settings in each comparison. This is a numerical fitting fix,
not a claim of convergence to continuous gradient flow.

The step1/1024 pilots failed the fitting gate within60 seconds: full-circle/P1
RMS0.98368 and arc/P3 RMS0.65459. Do not expand that setting. The single bounded
correction now tests readout initialization with std(c)=1 instead of1/n, while
keeping f=c@h/n, all layer mobilities, hidden weights, data and closure equations
unchanged. Thus the initial output remains O(n^-1/2) for centered random c,
and initial feature velocities are O(1) rather than suppressed by the vanishing
head. This preserves the muP feature-learning scaling but changes the initial
law; any successful comparison must rerun matching dense and all closures.
Use Euler step1/512 and two30-second pilots (full-circle/P1 and arc/P3). If they
fit at<=0.05, run the remaining14 models at the same settings, up to60 seconds
each. The only driver change is --readout-std and its recorded configuration;
its default preserves the previous initialization. The analyzer checks matching
readout initialization, treating old records as std(c)=1/n. No optimizer or
closure-core changes. Save under compact_selu_fix01/readout1_step512/.

The std(c)=1 pilots also failed within30 seconds: full-circle/P1 RMS0.91663,
arc/P3 RMS0.71116. No expansion of that setting. Final bounded configuration
check, explicitly disclosed to the user before running: move the existing
non-affine LayerNorm before SELU, restore the original std(c)=1/n, and use
step1/128. This is an architecture-placement change, not an unchanged-model
solver repair. Test the same full-circle/P1 and arc/P3 cases for30 seconds.
If they fit at<=0.05, run matching dense/P1/P2/P3 on all four tasks under this
placement; otherwise close the quick search and report that the requested
all-fit correction has not been achieved. No further configurations are tried.
The driver exposes the existing Flow normalization argument; default remains
after activation. Save under compact_selu_fix01/before_step128/.

The final before-SELU LayerNorm pilots also failed: full-circle/P1 train
RMS0.99794 and arc/P3 RMS1.01680 within30 seconds. The quick fitting-fix attempt
is closed without achieving the all-fit objective. Six pilots were run; no
candidate passed0.05 and no16-model expansion occurred. No positive-loss floor
or fundamental obstruction is claimed from these finite-duration tests.

[SELU_FITTING_FIX_RESULTS.md](SELU_FITTING_FIX_RESULTS.md) records all settings,
results,scope and reproduction details. Evidence is in
`data/generated/neural_response_memory_20260922/compact_selu_fix01/`, including
`pilots.csv` and `summary.json`. All six saved scores were independently
recomputed within1e-12; archive checksums, unchanged core/task source hashes and
exact input/query equality passed. The driver now exposes optional readout
initialization and normalization placement, with old defaults preserved;
the analyzer checks matching readout initialization. No further runs queued.

User scope correction: “fix” means training configuration, not architecture.
The before-SELU LayerNorm trial was outside that intended scope and is rejected
as a candidate fix. Return to the original after-SELU LayerNorm and std(c)=1/n;
all architecture,initialization and muP equations stay fixed. The sole remaining
training-configuration check is a three-stage Euler learning-rate decay:
step1/128 until RMS0.8 or30 seconds; step1/512 until RMS0.2 or30 seconds;
step1/2048 until RMS0.04 or30 seconds. Each stage has a20000-step cap and retains
the same state; no restarts, optimizer changes, rollback or error-control search.
The existing graph fitter supplies each stage; all phase endpoints and actual
physical times are recorded. Test only full-circle/P1 and arc/P3 first, then
expand to matched comparisons only if both fit to<=0.05. This restores the
user's requested scope; the prior architecture test is not a proposed change.
Save under compact_selu_fix01/original_decay/.

### Canonical implementation scope restored (2026-09-26)

The user's latest instruction supersedes the normalized fitting repair:
use ONE global implementation of full population/dense dynamics and population
closure for arbitrary hidden depth,activation and supplied data; no task-specific
model/solver fixes; put normalization aside. The two original-architecture decay
pilots ended at train RMS0.96424 (full-circle/P1) and0.26211 (arc/P3), so did not
establish an all-fit configuration. Those and the earlier normalized trials are
historical evidence, not defaults or proposed architecture changes.

compact_flow.Flow remains the sole numerical engine. Its forward/backward,
muP mobilities,closure equations and fixed-Euler stepping are unchanged.
run_compact_flow.py is the new task-independent front end: arbitrary NPZ inputs,
labels and query points; explicit width,depth,activation,order and one solver
configuration; normalization is always none. Historical task drivers also use
the same engine but are not the entry point for new work. No task name or data-
specific fitting branch enters the engine or this new front end.

Two initialization settings now belong to the engine instead of post-construction
mutation: hidden_gain and readout_std. Defaults preserve the old initialization.
The optional global unit_moment rule sets each hidden-link Gaussian gain to
1/sqrt(E[phi(Z)^2]) using128-node Gaussian quadrature, Z~N(0,1), for its preceding
activation. It is independent of task and depth and only changes initialization,
not the activation or architecture. Together with std(c)=1 and f=c@h/n this
retains muP feature-learning scaling. No normalization layer is used.

Bounded validation: existing CPU equation/gradient oracles, plus independent
checks of the new initialization configuration; then one shared configuration
on all four unchanged stress tasks with SELU,width2048,depth10,unit_moment,
std(c)=1,step1/64,target RMS0.04 and20 seconds per model. Dense/P1/P2/P3 use the
same settings throughout,16 fits total,one worker per GPU. Save under
canonical_unnormalized01/. No per-task adjustment or automatic follow-up sweep.
The current aim is one correct common implementation and an honest fixed-config
fitting check; no assertion that one step guarantees fitting every possible task.

The shared unnormalized batch completed: all four dense SELU models reached
RMS0.03884–0.03996 in4.56–16.05 model seconds. All twelve closures stopped with
nonfinite float32 loss. In particular full-sphere/P1 failed at physical time8.5
with step1/64. Before interpreting this as a closure issue rather than coarse
Euler instability, perform only a bounded numerical verification of this one
failure: same engine,data,initialization and model,step1/256 and1/1024,30 seconds
per run, no fitting or architecture changes. Save under
canonical_unnormalized01/refine256 and refine1024. This is a failure diagnosis,
not a task-specific replacement configuration or another full fitting sweep.

Refinement outcome changes the diagnosis: full-sphere/P1 still became nonfinite
at step1/256 (physical time16.3125), but step1/1024 reached train RMS0.0399852
at physical time9.83594 in16.81 model seconds. Thus the coarse-step failures
are not evidence of an unavoidable closure blow-up. Apply the one common
step1/1024 configuration to ALL four tasks and dense/P1/P2/P3, still width2048,
depth10,SELU,no normalization,unit_moment initialization,std(c)=1,seed20260920.
Use a common60-second cap and60000-step cap; retain the already fitted P1 pilot
as the sphere_full/P1 result. No task-specific exceptions, architecture changes
or optimizer modifications. This single global configuration check supersedes
the earlier coarse-step setting; record any remaining underfit cases honestly.
Outputs: canonical_unnormalized01/step1024/ (worker subdirectories).

The common implementation work is complete; the all-fit goal is NOT achieved.
Use [CANONICAL_FLOW.md](CANONICAL_FLOW.md), compact_flow.Flow, and
run_compact_flow.py for current work. The runner has arbitrary data inputs,
explicit depth/activation/order/configuration and no normalization or task-specific
solver branches. Initialization controls now belong to the same engine; defaults
preserve the older law. No forward/backward,muP mobility,closure or Euler equation
changed. The extended independent checks passed1416 assertions,max1.33e-15.

[CANONICAL_UNNORMALIZED_RESULTS.md](CANONICAL_UNNORMALIZED_RESULTS.md) records the
single shared SELU/depth10/width2048 setting. Coarse step1/64 fits all four dense
models but destabilizes closures; step1/1024 fits the full-sphere quartet, whose
P1/P2/P3 query RMS against dense is0.09103/0.09444/0.08967. The other task groups
remain underfit or divergent. Only6/16 selected models reached0.04; three closures
had nonfinite loss. No global fast-fitting configuration is claimed. All33 raw
records passed data/source/archive checks and independent rescoring; the actual
commands and selected endpoints are saved under canonical_unnormalized01/.
No normalized model or task-specific exception is adopted. All workers finished;
no further experiments are queued.


### Scalar implementation consolidated; stress campaign cancelled (2026-09-26)

The current response-basis scalar ODE, initialization, passive outputs,
detached network decoder, bounded fitter, prediction helper, and dense/population
references now live in [scalar_ode.py](scalar_ode.py), with NumPy/SciPy and no
local runtime imports. [SCALAR_STANDALONE.md](SCALAR_STANDALONE.md) documents the
interfaces, preserved three-hidden-layer tanh scope, decoder storage, and checks.
The old split sources remain historical comparison inputs.

[SCALAR_DICTIONARY_COMPARISON.md](SCALAR_DICTIONARY_COMPARISON.md) establishes the
fixed-span limitation: changing scalar coefficients cannot create learned
matrix directions outside the initialized response spaces. Nonlinear motion
inside those spaces remains possible; this is not a claim that learning is
impossible. Internal and decoded outputs also need not coincide at reduced rank.

The user explicitly cancelled further experiments once this dictionary
restriction was identified. No new neural training runs were launched.
[SCALAR_STANDALONE_PROTOCOL.md](SCALAR_STANDALONE_PROTOCOL.md) is an unexecuted,
cancelled plan, and no automatic campaign command remains. Both the isolated
standalone self-check and independent migration/algebra audit passed. Checked
initializer/coefficient/RHS/decoder migrations agree exactly; full-rank
identities agree to 1.81e-16. These checks perform no neural integrations and
provide no new accuracy evidence. Source hashes and results are saved under
scalar_standalone01/checks/independent_algebra.json in this study's generated data.
