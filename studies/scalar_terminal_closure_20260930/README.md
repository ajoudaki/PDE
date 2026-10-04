# Scalar terminal closure — MISSED THE REQUESTED OBJECTIVE

> [!WARNING]
> **STATUS CORRECTION — 2026-10-01: THIS STUDY MISSED THE MARK.**
>
> The user requested a finite autonomous scalar ODE that starts from
> initialization, captures feature learning, and reaches its terminal regime
> through its own dynamics, with a meaningful accuracy-versus-total-state-size
> tradeoff and the intended sublinear-width compression.
>
> **The assistant substituted a different problem:** run the full
> response-memory closure until a late training state, extract its learned
> response coefficients, and only then switch to a small scalar ODE. The user
> did not authorize replacing the requested construction with this approach.
> Their terminal-stability argument was intended to help control errors of
> the scalar system throughout training, not to supply it with a state learned
> by the full closure. This substitution bypassed the central difficulty.
>
> **Do not cite this study as demonstrating scalar compression from
> initialization or as satisfying the original request.** Its scalar–closure
> RMS errors measure continuation from supplied full-closure training states.
> The advertised 729-number evaluator excludes the preceding full training
> and the cost of producing its learned coefficients. The q=2/q=3 experiments
> and the newer memory-transport construction retain that same dependency;
> they do not repair the mismatch.
>
> **No proved or tested construction meeting the original objective was
> delivered.** Internal PASS reports concern their stated mathematical or
> numerical checks; they are not evidence that the requested task was solved.
> The assistant's presentation of this work as the requested deliverable was
> misleading. The proofs, code, and data remain as a historical record, not
> as a successful answer to that request.
>
> This notice supersedes any earlier success framing or continuation language
> in this study and its synthesis. Do not resume the terminal-switch campaign
> as fulfillment of the original objective based on an old next-step note.

Study started 2026-09-30 for the user's requested new compression direction;
the terminal-switch substitution was the assistant's decision.
This study does not use any unpromoted result or proof from earlier studies,
including earlier work in the same conversation. The current paper is the
scientific source for the q=1 response-memory system; maintained docs are
available as established context. No manuscript/book/code edits or Git writes
are planned.

## Historical research contract and scope

Target: a finite autonomous, restartable scalar ODE approximating the loss
curve of the actual two-hidden-layer tanh q=1 response-memory flow, retaining
correlated finite training inputs, nonlinear learned features, and the fixed
Gaussian mixer with its true transpose/adjoint. Finite-width formulas serve
as exact algebra; claims about a population target must state its existence
and convergence assumptions separately. The paper's fixed-q population limit
is a conjecture, not an available general theorem.

Use m fixed normalized inputs and binary labels, residual r=f-y, loss
L=m^{-1}||r||^2, rho=sqrt(L), and zero stored initial readout. The q=1 paper
coordinates are k_a=bar h_(a,0)/tau, v_a=-2 bar delta_(a,0), tau_0=1:

    h(x)=tanh(Ax/sqrt(d)), B=W0+sum_a v_a k_a^T/(mn),
    g(x)=tanh(Bh(x)), f(x)=w^Tg(x)/n,
    d_a=w odot (1-g_a^2), ell_a=(1-h_a^2) odot B^T d_a,
    wdot=-2 mean_a r_a g_a,
    Adot=-2 mean_a r_a ell_a x_a^T/sqrt(d),
    vdot_a=-2 r_a d_a, kdot_a=(rho/tau)(h_a-k_a), taudot=rho.

Initialization A_ij~N(0,1), W0_ij~N(0,1/n), independent; w=v=0,
k_a=h_a, tau=1. B is derived, never independently trained.
At population level, neuron averages become expectations and W0 has one
specified action and its adjoint. No independent-Gaussian replacement on reuse.

Requested primary metric: absolute loss error at equal physical times,
ideally sup over t>=0. Additional aggregate observables need their own
tail-motion bounds. Desired complexity: S(epsilon)=o(epsilon^{-2}), so at
a stipulated root-width accuracy epsilon~n^{-1/2}, moving state is o(n).
This conversion is conditional on a matched dense/root-width error estimate;
the paper does not establish that estimate in general. Report fixed coefficient
storage, coefficient provenance, evaluation work and initialization cost too.
No hidden population oracle, future training trace, growing history or
width-sized moving dictionary is allowed. Scalar moments are not called
velocities. Initialization matching and forced decay alone do not count as
trajectory approximation.

The initial request authorized theoretical research and bounded deterministic
checks. The subsequent explicit request to test the scalar construction against
dense width-1024 training on the circle authorizes the campaign described in
[CIRCLE_EXPERIMENT_PLAN.md](CIRCLE_EXPERIMENT_PLAN.md). That plan was frozen
before implementation and training. This supersedes the initial no-training
scope for this specific experiment.
No claim of exact finite closure impossibility or universal fitting will be
assumed merely from intuition. Claims are exact, conditional, conjectural or
open, separately from their check status.

## Results retained for the record — not fulfillment of the objective

The 2026-10-01 question about retaining lower modes is developed in
[MEMORY_TRANSPORT_SCALAR.md](MEMORY_TRANSPORT_SCALAR.md). The existing
q-independent scalar size results from freezing aggregate response
coefficients; the full closure's state grows with q. A newly derived
alternative freezes the neural fields at the handoff while transporting
all memory modes under its own residual and clock. It uses qm+1 moving
controls, plus q-dependent fixed training and query data. The q2 formulas
match the full output and its first velocity at the handoff, stop at zero
residual, and have unique solutions at every finite physical time. An
explicit arbitrary-restart example demonstrates a local benefit, without
claiming reachability from the prescribed initialization. The clarified
candidate passed the cooperative internal mathematical check in
[MEMORY_TRANSPORT_SCALAR_CHECK.md](MEMORY_TRANSPORT_SCALAR_CHECK.md).
No new numerical experiment has been run: improved
accuracy on the initialized circle tasks, a favorable total storage/error
tradeoff, fitting, and an initialization-only scalar model remain unproved.
Lower modes within a q2 trajectory are distinguished from a separately
trained q1 trajectory; combining the latter has no automatic guarantee.

The user's q=2/q=3 continuation is recorded in
[HIGHER_ORDER_EXPERIMENT_PLAN.md](HIGHER_ORDER_EXPERIMENT_PLAN.md).
It tested both higher orders on the two alternating-label circle tasks
against the original matched dense references, then tested their terminal
scalar continuations. [HIGHER_ORDER_SCALAR.md](HIGHER_ORDER_SCALAR.md)
derives the exact finite-order response identity and conditional transfer
of the terminal theorem. The completed results are in
[HIGHER_ORDER_RESULTS.md](HIGHER_ORDER_RESULTS.md): q2 meets the preset
dense endpoint criterion on both tasks (circle RMS 0.02969 and 0.04121).
q3 improves the dense loss curve further but has larger final circle RMS
errors (0.07214 and 0.05247), failing that RMS criterion. All four primary
scalarizations pass scalar/closure fidelity (RMS 0.00298--0.00670), with
the same 729-number evaluator. All full closures fit and all numerical
refinement checks pass. The Fourier query functions retain small training
errors; full pre-switch training is still required. Four standalone
higher-order scalar models were exported and independently evaluated.

Read [SYNTHESIS.md](SYNTHESIS.md) for the mathematical conclusion and its
limits. The strongest result is a **conditional, internally checked terminal
compression theorem for the actual finite-width model**, first proved
for q=1 and now transferred to every fixed finite q by an exact mode
identity. It is not a complete sublinear-state population theorem.

The subsequent authorized circle experiment is complete; see
[CIRCLE_RESULTS.md](CIRCLE_RESULTS.md). Five manuscript tasks were compared
against dense width 1024 on identical initial arrays, with 8192 unseen-circle
queries and independently checked time-step refinement. All five full-model
pairs fit; center/edges required a separately recorded continuation from
time 512 to 950. The terminal model has 17 moving and 712 fixed scalar
coordinates, and five standalone exports were checked. At the primary
0.01-loss switch, scalar-versus-dense circle RMS ranges from 0.0140 to 0.3823;
scalar-versus-q=1 RMS ranges from 0.000654 to 0.03349. The result supports
useful terminal continuation on some tasks, not a successful generic dense
replacement. Initial q=1 training still produces the handoff, and the
finite Fourier readout can retain training error after its internal residual
has nearly vanished. Raw original and supplemental comparisons are preserved.

Exactly, the residual has the finite aggregate form

    rdot=-C(X)r+||r|| b(X).

The current-key cross term can make C nonsymmetric. The activity-driven key
motion produces b, which can be first order in residual size even at a
fitted full state. At a reached sufficiently small terminal state with a
certified contraction margin, freezing both C and b gives an autonomous
system with m moving residual scalars, optional clock/observables, and
O(m^2) fixed coefficients. It has uniform-in-physical-time loss error O(R^3)
and clock error O(R^2), where R is the handoff residual norm. Precise tube
conditions and all constants are in the theorem; no width uniformity is
inferred from finite-dimensional smoothness.

An approximate handoff needs residual precision O(R^2) and response
coefficient precision O(R) to retain that cubic loss error. A quadratic
metric extension admits nonnormal terminal generators and transient
Euclidean loss increase. Neither result proves initialized entry into
such a region.

At initialization, a separate checked theorem for one input and arbitrary
width shows a strictly evolving decay rate: `(log L)''(0)=0` but
`(log L)'''(0)<0` whenever the initial second-layer feature is nonzero.
A positive mixture of fixed exponential rates cannot match the first three
loss derivatives. This is an exact early-learning restriction, not a
multi-input fitting or approximation theorem.

| Artifact | Claim and current check status |
|---|---|
| [TERMINAL_SCALAR_THEOREM.md](TERMINAL_SCALAR_THEOREM.md) | Exact residual equation; conditional all-time terminal approximation and passive observables. Internally checked in [TERMINAL_SCALAR_CHECK.md](TERMINAL_SCALAR_CHECK.md), including amended self-contained model. |
| [TERMINAL_HANDOFF.md](TERMINAL_HANDOFF.md) | Certified inaccurate coefficients/residuals; explicit loss and clock error allocation; non-differentiability of the frozen residual map if b is nonzero. Internally checked in [TERMINAL_HANDOFF_CHECK.md](TERMINAL_HANDOFF_CHECK.md). |
| [TERMINAL_METRIC_EXTENSION.md](TERMINAL_METRIC_EXTENSION.md) | Quadratic contraction certificates, explicit norm constants and nonnormal coverage. Internally checked in [TERMINAL_METRIC_CHECK.md](TERMINAL_METRIC_CHECK.md); its original unchecked header records its pre-check status. |
| [INITIAL_RATE_CURVATURE.md](INITIAL_RATE_CURVATURE.md) | Exact arbitrary-width one-input onset and restricted positive-spectrum obstruction. Internally checked in [INITIAL_RATE_CURVATURE_CHECK.md](INITIAL_RATE_CURVATURE_CHECK.md), with a root-verified title-only clarification. |
| [AGGREGATE_ROUTE.md](AGGREGATE_ROUTE.md) | Exact aggregate equations and dissipation certificate; same-source current-state Gram obstruction. Internally checked, then clarified and rechecked in [AGGREGATE_CHECK.md](AGGREGATE_CHECK.md). No initialized reachability or population no-go claim. |
| [CONTROL_ROUTE.md](CONTROL_ROUTE.md) | Conditional scalar signature realization, stability transfer and explicit rate/count threshold. Author-derived; root reconstructed the proof and audited admissible control scope. No complete independent review or actual q=1 source-rate certificate. |
| [INFORMATION_ROUTE.md](INFORMATION_ROUTE.md) | Dataset-Gram sufficiency for path law; sharp linear-information radius; stable analytic matching-jet counterexample; conditional scalar coefficient construction. Author-derived and root-read; no separate complete independent check. |
| [CIRCLE_RESULTS.md](CIRCLE_RESULTS.md) | Executed width-1024 dense/q=1/scalar comparisons on all five circle tasks and all three switches; original and supplemental endpoints, query/loss errors, controls, numerical validity and scope. |
| [CIRCLE_QUERY_CHECK.md](CIRCLE_QUERY_CHECK.md) | Exact frozen query observer, odd Fourier representation, 729-scalar accounting and frozen-producer source audit. |
| [CIRCLE_EMPIRICAL_CHECK.md](CIRCLE_EMPIRICAL_CHECK.md) | Independent reconstruction of all original states/handoffs and the supplemental endpoint pair; original history and coefficient preservation checks. |
| [CIRCLE_PORTABLE_MODEL.md](CIRCLE_PORTABLE_MODEL.md) | Standalone scalar export and evaluator; endpoint consistency and the retained extra trajectory diagnostic. Final exports for all five cases are in `data/generated/scalar_terminal_closure_20260930/circle_portable_final_01/`. |
| [HIGHER_ORDER_SCALAR.md](HIGHER_ORDER_SCALAR.md) | Exact finite-order endpoint-memory identity, q2/q3 scalar responses and conditional theorem transfer; checked in [HIGHER_ORDER_SCALAR_CHECK.md](HIGHER_ORDER_SCALAR_CHECK.md). |
| [HIGHER_ORDER_SOURCE_CHECK.md](HIGHER_ORDER_SOURCE_CHECK.md) | Complete source audit of the frozen q2/q3 producer, exact model and query formulas, initialization, matched comparisons and numerical protocol. |
| [HIGHER_ORDER_RESULTS.md](HIGHER_ORDER_RESULTS.md) | Completed two-task q2/q3 dense and scalar comparisons: all switches, error separation, threshold failures, 414 analysis checks, 16 raw-state reconstructions and four checked standalone exports. |
| [MEMORY_TRANSPORT_SCALAR.md](MEMORY_TRANSPORT_SCALAR.md) | New scalar continuation retaining each mode's memory transport under frozen neural fields; exact handoff matching, finite-time well-posedness, arbitrary-restart local benefit and qm+1 moving controls. Internally checked in [MEMORY_TRANSPORT_SCALAR_CHECK.md](MEMORY_TRANSPORT_SCALAR_CHECK.md); no numerical test or initialized accuracy improvement claimed. |

All check reports preserve candidate hashes, input scopes, proof attacks,
outcomes and limitations. These are study results, not established book
theorems or promotion reviews. No external priority/novelty claim is made.

## Unresolved original objective — no automatic continuation

The decisive missing result is a finite evaluator of the evolving response
coefficients from initialization, accurate under its own feedback, with a
quantified source-error/storage rate. It must approximate the preceding loss
curve and supply the certified terminal data without a population oracle
or a future training trace. A convergence proof for the derivative/control
hierarchy, or density of some dictionary without a rate, is insufficient.
The independent control route makes this explicit: geometric order error
exp(-beta p) with (m+1)^p coordinates beats epsilon^-2 by that construction
only if beta>log(m+1)/2; no such bound is proved for q=1.

Actual fitting, a terminal certificate on reached initialized states,
width-uniform constants, the population q=1 target, and the stipulated
dense/root-width comparison are separate open dependencies. The single
highest-value next question is an initialization-computable approximation
rate for the response coefficients on the relevant forced reachable family.
No initialized scalar construction meeting the original request was delivered.
The user's correction rejects treating the terminal-switch approach as that
deliverable; earlier continuation language does not authorize resuming this
campaign as fulfillment of the request. The circle campaign tests only the
terminal continuation and its unseen-input observer; it does not supply the
missing initialization-computable response evaluator.
The original campaign and the supplemental horizon extension followed
[CIRCLE_EXPERIMENT_PLAN.md](CIRCLE_EXPERIMENT_PLAN.md) and
[CIRCLE_ENDPOINT_EXTENSION_PLAN.md](CIRCLE_ENDPOINT_EXTENSION_PLAN.md),
respectively. The second plan was recorded after slow convergence was observed
and before extension implementation/execution; it did not alter the original
model, switches, coefficients, or numerical methods.

## Contributors, checks and reproduction

Root owns README, synthesis, terminal theorem, handoff extension and initial
rate derivation. Fresh scoped independent routes were `scalar_aggregate`,
`scalar_control` and `scalar_information`; their notes were frozen before
cross-route comparison. `terminal_check` independently checked the terminal
theorem and extensions. After freezing its own route, `scalar_information`
checked the aggregate counterexample and the initial-rate theorem. Root
read all complete routes and check reports, resolved the aggregate wording
issues, and verified the revised statements. Each agent's allowed scope
and actual sources are recorded in its note/report.

The initial evidence was analytic. Reproduction of those results consists of
substituting the displayed q=1 velocities into the residual equation and
following the persisted differentiations, contraction estimates and norm
bounds. The original theoretical checks used bounded exact arithmetic for
static identities, without ODE training. The subsequently authorized circle
campaign uses [circle_terminal_experiment.py](circle_terminal_experiment.py),
the exact inputs in [circle_task_inputs.json](circle_task_inputs.json), and
the independent analysis script
[analyze_circle_experiment.py](analyze_circle_experiment.py). Input provenance
and the observer/source audit are recorded in
[CIRCLE_TASK_INPUTS.md](CIRCLE_TASK_INPUTS.md) and
[CIRCLE_QUERY_CHECK.md](CIRCLE_QUERY_CHECK.md). The dense RHS was checked
against the maintained finite-network API; no maintained API was changed.
No manuscript, maintained-book or maintained-code edits,
Git staging, commit or push were performed by this study. Concurrent work
outside this study was left untouched.

Startup metadata: HEAD 7fce699a7decf2239dc3eb50486eca661783b535; empty staged
index. Other untracked directories are preserved and are not scientific inputs.
Current manuscript SHA256 fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605.
Root reread current instructions, docs/index.qmd and docs/notation.qmd, and
the manuscript's complete setting and q=1 construction. Earlier complete
manuscript reading is unchanged by hashes; no earlier study findings transfer.
The complete manuscript read includes both included appendices and figure
captions. Maintained context inspected here includes the complete specific
quadratic-jet and finite-linear-moment obstruction passages in
`docs/07-observable-closure.qmd`; their different model scopes were retained.
An initial portion of `docs/08-autonomous-computation.qmd` was inspected for
context only and is not used as a theorem dependency.
