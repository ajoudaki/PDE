# Structured full-rank initialization and scalar response-memory closure

User-authorized proof investigation, 2026-09-26. This is a new study because
replacing the initialization law is a distinct research direction. No source,
proof or evidence from another study is imported. The mathematical model below
is a self-contained definition of the object to be compressed.

## Completed bounded continuation: current correlations, 2026-09-30

The user explicitly authorized taking over this study. Two new autonomous
current-correlation closures were derived, frozen and tested on the hard
close pair, hard cluster and smooth-label cluster control. **Neither closes
the gap.** All models reached training MSE 0.001; raw circle RMS against
the reused canonical Gaussian n=1024, seed=1 dense outputs was:

| Model | near_pair_sin9 | cluster_triple_cos9 | cluster_triple_cos1 |
|---|---:|---:|---:|
| Previous bounded Gram, reused |0.240264|0.252676|0.010079|
| A: projected current feature/readout gate |0.151161|0.708189|0.014764|
| B: current Gaussian covariance/transport |0.342895|0.831930|0.008819|

A evolves 6/10 training states and 1038/1305 states with the circle and
training-alias queries. An exact transport identity reduces B to **m²+m
total evolving aggregates (6/12 here), with no query ODE states**. Its
training coefficients are O(m²), query coefficients O(Qm), and initialization
still uses the full network. This is a useful compact decoder construction,
but the Gaussian closure is empirically inaccurate on both hard tasks.

The exact weighted-gate evolution was derived, exposing the mixed moments
needed to close it. Both candidates supply explicit approximations and exact
surrogate loss/energy/positivity identities; no dense-fidelity theorem follows.
Saved-state tests reveal a separate substantial defect: even the **exact
current weighted gate Gram**, combined with the candidates' frozen isotropic
hidden response, underestimates lower-layer response along the current
residual by 71% / 84% at the hard dense endpoints. These conditional operator
errors do not establish trajectory-error lower bounds. Current directional
hidden response and output-relevant readout dependence remain unresolved.

The [frozen protocol](CURRENT_CORRELATION_PROTOCOL_20260930.md) produced six
primary fits and two predeclared close-pair refinements, totaling 1.435 seconds
of scalar integration with one BLAS thread. Tighter integration changes
close-pair predictions by at most 1.15e-10 RMS. Saved-state replay, aliases,
passive-query independence and declared invariant checks pass; cluster and
smooth trajectories were not independently rerun. Neither candidate opened
the transfer branch. No dense training was repeated and no further runs are
queued. The previous bounded-Gram model remains the best tested joint repair.

[Full results, equations, cost accounting and reproduction](CURRENT_CORRELATION_RESULTS_20260930.md),
[current-correlation diagnostic](CURRENT_CORRELATION_DIAGNOSTIC_20260930.md),
[same-state tests and exact-gate decomposition](CURRENT_CORRELATION_SAME_STATE_20260930.md),
[scoped internal audit](CURRENT_CORRELATION_RESULT_AUDIT_20260930.md).
All findings remain study-local. No other study was read, no maintained
scientific material was changed or promoted, and no Git write occurred.

## Previous: diagnosing and partially repairing scalar feedback

2026-09-30. The user requested a small number of missing feedback terms,
without restoring population-sized state. A controlled diagnosis and four
bounded rounds identify two substantive faults: the initial-kernel test
extension of the positivity completion becomes large, and the finite
feature expansion leaves the tanh regime. Consistently removing the
completion reduces but does not fix error. Self-consistent readout feedback
and bounded moving-Gram evolution improve further.

The best joint model reduces close-pair circle RMS from **1.20563 to
0.24026**, oscillating-cluster RMS from **1.33777 to 0.25268**, and the
smooth-label control from **0.04256 to 0.01008**. It improves eight of the
nine tasks; the mixed quartet slightly worsens. These remain partial
repairs, not attainment of the frozen 0.05 target on the hard cases.
All fits use the same n=1024 Gaussian reference and MSE0.001 threshold;
tighter integration changes focus predictions by at most5.21e-9 RMS.

The bounded-Gram model has m+m(m+1)/2 training states and exact surrogate
loss, energy, Gram-positivity and saturation identities. Each passive input
adds m+1 dynamic states: the 256-point circle panel uses779–1861 states,
so this is **not** a fixed O(m²)-state decoder of the entire function.
Width-dependent initialization and O(m^4) static training contractions
remain explicit costs. No dense trajectory supplies its coefficients.

An exact hidden-feature Hessian correction was also derived and tested
with6–16 dynamic states and no passive query states. It fails the joint
accuracy gate. At its fitted scalar endpoints, the exact tanh network at
the same lifted weights has training MSE0.49/1.47 on the hard cases,
versus the scalar's0.001; the smooth case has no comparable discrepancy.
This directly exposes failure of the low-order feature map at large
motion, rather than an integration or clock issue. One additional derived
readout mode does not resolve it. These results reject the tested repairs
as general accurate replacements, not scalar compression in principle.

[Full diagnosis, all comparisons, costs, figure and unresolved correlations](CUBIC_FEEDBACK_REPAIR_RESULTS_20260930.md),
[bounded-Gram equations and exact internal guarantees](CUBIC_ENERGY_REPAIR_ROUTE_20260930.md),
[quadratic-feature equations and checks](CUBIC_QUADRATIC_FEATURE_ROUTE_20260930.md).
No new global dense-fidelity theorem is claimed; no further runs are queued.

## Previous experiment: cubic scalar ODE versus dense n=1024

2026-09-30. The proposed response ODE is now implemented and tested on nine
existing circle tasks against verified fitted dense Gaussian n=1024
references. Initial aggregate coefficients use the same full Gaussian
initialization, so this comparison does not also introduce a block replacement.
All scalar models reach training MSE0.001 with only 13–243 evolving states,
including shared test-decoder integrals. The whole primary panel takes1.782s.

The test-function outcome is mixed: circle RMS(scalar−dense) is below0.05
on five tasks, between0.05 and0.15 on two, but1.20563 on the close
opposite-label pair and1.33777 on the oscillating cluster. The correction
improves over the frozen initial kernel on seven of eight matched fitted
controls; the ninth frozen control does not reach the training target. Its stable
loss and accurate training fit therefore do not establish faithful unseen
outputs under strong feature learning. This particular low-order model
fails as a general replacement in the tested regime; arbitrary scalar
compression is not ruled out.

[Complete results, function plots, costs and numerical controls](CUBIC_SCALAR_CIRCLE_RESULTS_20260930.md)
include the fixed task panel, saved artifacts and reproduction commands.
[Implementation](cubic_scalar_ode.py) and
[independent audit](CUBIC_DECODER_IMPLEMENTATION_AUDIT_20260930.md) retain
the distinction between dynamic state, static coefficient storage and
width-dependent coefficient initialization. No neuron states, Fourier modes
or reference forcing enter the scalar RHS.

## Theory: small response compression and terminal stability

2026-09-30. The [new assessment](ACTIVITY_SCALAR_ASSESSMENT_20260930.md)
addresses the stronger requirement of useful sub-width scalar state at
matched accuracy. It contains two internally checked advances. A
[terminal replacement theorem](TERMINAL_FREEZE_THEOREM_20260930.md) gives
an all-remaining-time output error proportional to handoff MSE, conditional
on explicit residual stability and coefficient-variation bounds. A
[small moving-kernel construction](KERNEL_SCALAR_ROUTE_20260930.md) captures
the first feature-learning correction with m(m−1)/2+2m training states,
plus at most m^3 states for an arbitrary-input decoder. Under a positive
initial Gram and sufficiently small label amplitude a, its P1 output error
is O(a^5) uniformly over all time and the unit input disk. The decoder
agrees exactly with training outputs at training inputs.
The Gaussian population existence proof and bounded-C² activation extension
are included and separately checked in the linked assessment.

This is a restricted response-expansion result, not a solution for the
previous unit-label strong-learning tasks or an arbitrary-accuracy family
at fixed amplitude. Static coefficients cost O(m^4), their initialization
and query integration costs remain material, and identification with dense
iid-Gaussian training is separate. The previous selective truncations
already stopped at zero residual; the new advance is a derived small
error source plus terminal stability. Complete proofs, independent internal
audits and a finite-array algebra check are linked in the assessment.
The theory continuation itself ran no network training experiments; the
subsequent direct numerical test is reported above.

## Previous reassessment: constructive existence, unresolved useful compression

2026-09-27. The [new assessment](NEXT_AGGREGATE_ASSESSMENT.md) supersedes the
earlier absence of a Gaussian-block/full-circle existence proof, while
retaining the warning that an effective small aggregate closure has not been
established. All statements here concern the stipulated fixed-k block target;
identification with canonical dense iid-Gaussian training remains separate.

The current output-depth J refinement has a permanent feedback omission.
[A canonical-orbit calculation](NEXT_OBSTRUCTION_ROUTE.md) proves a positive
J-independent error floor for eleven retained moments plus the clock. It is
not an output-only or universal scalar-impossibility theorem. The proof and
exact symbolic row received separate internal checks, recorded in
[the audit](NEXT_OBSTRUCTION_AUDIT.md).

A [complete-feedback dependency family](NEXT_BOUNDARY_ROUTE.md) repairs that
nonexhaustion. Its first level was implemented in
[next_dependency_closure.py](next_dependency_closure.py) and tested on two
matched pair tasks. Both fitted to MSE 0.001 in under a second, with 69,501
full-panel scalars instead of J2's 188,367. However, scalar-block circle RMS
was 0.25247 on the opposite-label pair and 0.08173 on the orthogonal pair;
the latter was 0.05006 under fitted J2. Thus the first-level repair is faster
but still not an accurate replacement. No larger sweep followed. The
[results](NEXT_DEPENDENCY_RESULTS.md) include exact common-initial-moment,
saved-output, reference and hash checks.

The [Gaussian extension](NEXT_GAUSSIAN_ROUTE.md) controls cutoff feedback by
an Osgood stability estimate and shares training moments across separate
passive-query families. It yields a genuine aggregate hierarchy converging
uniformly on every finite time interval and the whole circle for unbounded
Gaussian blocks. A [further construction](NEXT_POLYNOMIAL_ROUTE.md), using
observable-generated current-coordinate monomials and a fixed collection of
mark cutoffs, gives a formal algebraic error/state-size bound at fixed
k,m,P. An [analytic initializer](NEXT_POLYNOMIAL_INITIALIZATION.md) also
gives polynomial fixed-parameter initialization work. These exponents have
severe dimension and time dependence; no practical small-order advantage
or polynomial numerical-integration guarantee follows. These are internally cross-checked study
proofs, not promoted book results or a numerical convergence demonstration.

The decision is to continue the constructive route while abandoning J-only
refinement as the proposed convergence mechanism. The user-requested useful
accuracy/size tradeoff remains unresolved.

## Latest correction: aggregate statistics, not population representations

2026-09-27. The user has explicitly rejected the histogram as an answer to
the scalar-compression request. That rejection is correct: a fixed grid of
joint-state probability masses still represents the population distribution,
with a prohibitive dimension. The earlier moving-block construction is a
smaller sampled population. Neither establishes the requested additional
compression. Their numerical results remain records of those methods only.

The current target is an autonomous ODE of observable-relevant aggregate
statistics (mixed moments, correlations and contracted response products),
on top of the Gaussian-block memory closure. Its state and evaluation cost
must be independent of original width, with a useful error-versus-size bound
on every prescribed finite interval. Particles, histograms, density grids,
fields indexed by initial random labels, and replay of a precomputed target
trajectory are not admissible solutions. Merely being finite does not meet
this requirement. A complete joint-law expansion with no justified reduction
in cost would not establish effective compression either.

No effective construction for the actual Gaussian model or general
impossibility theorem has yet been established. The theory-only correction
does obtain a genuine bounded-moment contraction hierarchy with a restricted
finite-time convergence theorem. The Gaussian efficiency gap is explicit;
the restricted theorem is not presented as the requested completed result.
No additional training experiments are part of this correction. The older
sections below retain their historical wording and are superseded wherever
they call population or histogram representations a solution to this target.

The current synthesis is [TRUE_AGGREGATE_ASSESSMENT.md](TRUE_AGGREGATE_ASSESSMENT.md).
Its supporting derivations are:

- [TRUE_AGGREGATE_CONSTRUCTIVE.md](TRUE_AGGREGATE_CONSTRUCTIVE.md): direct
  evolution of normalized tree-contraction moments, with bounded approximate
  moments and finite propagation of truncation error through their degrees.
  For bounded G, fully Gaussian initial first weights, and a fixed finite
  query panel, the proof gives exponential error versus contraction order
  and algebraic error versus scalar count at fixed parameters. Normalizing
  by the existing clock gives one unchanged hierarchy for every finite
  horizon. The constants need not be useful.
- [TRUE_AGGREGATE_CONSTRUCTIVE_AUDIT.md](TRUE_AGGREGATE_CONSTRUCTIVE_AUDIT.md):
  internal checks of the gate lift, G/G-transpose normalization, index
  collisions, boundedness, and finite-horizon error propagation. Gaussian
  cutoff removal with useful cost and whole-circle decoding remain open.
- [TRUE_AGGREGATE_GAUSSIAN.md](TRUE_AGGREGATE_GAUSSIAN.md): an order-one
  feature-learning response from matrix reuse, and a strictly negative
  initial fourth-cumulant coefficient for every nonzero input, uniformly
  in block size. Gaussian initialization does not justify treating current
  preactivations as Gaussian throughout training. This is not an output-error
  lower bound against all richer aggregate closures.
- [TRUE_AGGREGATE_OBSTRUCTION.md](TRUE_AGGREGATE_OBSTRUCTION.md): quantitative
  conditions needed for a genuine approximation lower bound, a restricted
  first-mean limitation, and why arbitrary-law moment matching does not
  establish impossibility on the canonical Gaussian orbit.

These are author derivations with internal cross-checks, not independent
promotion reviews or maintained-book results. No empirical claim is made
for the new contraction ODE; the earlier block-subsampling and histogram
experiments did not test it.

The user subsequently authorized a quick implementation screen of the direct
aggregate ODE against canonical Gaussian networks at n=1024 and training
MSE 0.01. [TRUE_AGGREGATE_QUICK_PROTOCOL.md](TRUE_AGGREGATE_QUICK_PROTOCOL.md)
fixes three tasks, initial order checks, direct scalar-state requirements,
passive circle outputs, matched references, and short stopping budgets. This
screen starts with measured compilation feasibility; a population or density
method must not be substituted if the contraction system is too large.

The [quick implementation results](TRUE_AGGREGATE_QUICK_RESULTS.md) are now
available. The actual aggregate-only k4/P1/R9 system fitted the two-input
task to MSE 0.01 in 12.8 seconds, but its training dynamics differed sharply
from the matched population closure: threshold flow times 0.822 versus
4.628, with fitted training-output RMS difference 0.0718. It required
37,996 contractions plus the clock. R11, a passive-query extension, and
both three-input tasks exceeded the stated compilation limits. No
scalar-versus-Gaussian circle RMS or decreasing error-versus-order curve was
obtained. The control's circle RMS 0.00417 belongs to the block population
model, not this scalar ODE. This screen does not establish useful further
compression; the earlier theory-only status above is superseded by these
specific implementation and feasibility measurements.

The user then directed a smarter selective cutoff. The subsequent
[selective-cutoff tests](SELECTIVE_AGGREGATE_RESULTS.md) reduce the pair-task
training core to 526 contractions (98.6% fewer), preserving the exact immediate
output, feedback and hidden-Gram derivatives. Scalar passive circle outputs
are now measured: Gaussian RMS 0.0774 on the pair and 0.0494 on the mixed
three-input task; a richer pair selection reaches 0.0712. A gate-product
boundary worsens pair RMS to 0.1183. The clustered task fails to fit in its
45-second budget. The passive decoder also disagrees with the training
state at a coincident input. Thus the new cutoff is much smaller and
executable but still does not establish a small-error scalar replacement.
The full 64-query state costs and consistency defects are explicit in the
report. All five selective runs are stopped; their total training time
was 56.92 seconds. These results supersede only the earlier absence of scalar
circle measurements, not its recorded degree-9 observations.

The user has now authorized a fixed-method expansion to eight new input
configurations, with the same n=1024 and MSE0.01 stopping target.
[SELECTIVE_GEOMETRY_PROTOCOL.md](SELECTIVE_GEOMETRY_PROTOCOL.md) freezes
the tasks, runtime limits, circle comparisons and passive copies of every
training input. The latter measure the input-consistency defect on every
task. This campaign changes geometry and sample count, not the scientific
cutoff; an exactly equivalent compiler optimization is checked separately.

The [eight-configuration results](SELECTIVE_GEOMETRY_RESULTS.md) are complete.
Four scalar runs fitted to MSE 0.01, with Gaussian circle RMS 0.0429,
0.0613, 0.0768 and 0.2118; four hit the 45-second limit. All sixteen
Gaussian/block controls fitted. The opposite-label pair is a new clear
off-training discrepancy: core training predictions agree with Gaussian
to RMS 0.00107, yet circle RMS is 0.21179. The smooth-label cluster fits,
unlike the earlier cosine-9 labels on the same geometry. Every task now
includes passive training-input copies; the consistency defect persists.
The exact compiler shortcut was checked bitwise against the old compiler.
All raw records passed independent metric/hash checks. Total scalar training
was 205.18 seconds; the campaign is closed with no further runs pending.

The user subsequently requested a scalarization-order test on the three
fitted low-error cases: orthogonal cosine pair, smooth clustered triple,
and spread-out mixed triple. [SELECTIVE_ORDER_PROTOCOL.md](SELECTIVE_ORDER_PROTOCOL.md)
fixes output-dependency depth J=1 versus J=2 while keeping k4/P1 and the
matched initialization fixed. The saved J=1 runs and controls are reused
read-only; three new J=2 runs have a 45-second training cap each. The primary
metric is now scalar versus matched block-population circle RMS, isolating
scalarization from the block-versus-Gaussian discrepancy. Root owns the
protocol/report and README; the runner owns `run_selective_order.py` and
new run records; a separate checker audits the saved moments and metrics.
This is one extra generation of output-moment dependencies, not a proof of
exact second time derivatives or convergence of this selective family.

The [J1/J2 comparison](SELECTIVE_ORDER_RESULTS.md) is complete: at MSE0.01,
matched-block circle RMS changes were25.20% lower on the orthogonal pair,
3.29% higher on the smooth cluster, and0.017% lower on the wide mixed triple.
All three fitted; full query-panel state sizes increased about8–10 times.
Every common initial scalar matched bit for bit and all saved-state metric
checks passed. The result is mixed rather than a consistent accuracy trend.
The campaign used35.39seconds of training plus188.47seconds of initialization.

The user's subsequent [tighter-stop continuation](SELECTIVE_TIGHTER_PROTOCOL.md)
resumes the six saved scalar endpoints and six references at MSE0.001
(RMSE approximately0.03162), preserving all previous evidence. Initial
contractions and template compilation are not repeated. This asks whether
the coarse earlier fit threshold obscured the scalar-order comparison.

The [tighter-stop results](SELECTIVE_TIGHTER_RESULTS.md) are complete. All
six scalar and six reference continuations reached MSE0.001. Scalar–block
RMS J1→J2 is0.07118→0.05006 for the orthogonal pair,0.08766→0.09060 for
the smooth cluster, and0.03501→0.03409 for the wide mixed triple. The order
benefit remains mixed; tightening the stop reduces the wide-triple errors
but increases the pair/cluster errors. Additional training took26.05seconds
for all scalar runs and1.97seconds for all controls, without reinitializing
or recompiling. The passive/core identification defect persists. Source,
resume-state and raw-metric checks are retained with the new evidence.
Both requested order/threshold campaigns are now closed.

The user next requested broader J2 coverage and then narrowed the execution
to efficient, distinct stress cases without retries or nearly duplicate
rotations. The [coverage inventory](SELECTIVE_ALL_TASKS_COVERAGE.md) contains
17 distinct tasks; only three had J2/MSE0.001 results. The new
[representative-screen protocol](SELECTIVE_ALL_TASKS_PROTOCOL.md) selects
six additional cases (two opposite-label separations, sharp three-point
cluster, mixed quartet, smooth six-point ridge, alternating six-point task)
and leaves eight others explicitly untested at this setting. The new exact
setup and shared-core RHS shortcuts match all tested previous initialization
and velocity values bit for bit; they do not change the scalar equations.
Root owns protocol/runtime shortcut/report, runner owns initialization
shortcut/scalar records, reference agent owns matched controls, checker
owns coverage and saved-result audits. The generated namespace is
`all_tasks_j2_20260927`; per-case training remains capped at45seconds.

The [representative J2 results](SELECTIVE_ALL_TASKS_RESULTS.md) are complete.
Four new trajectories reached the45-second limit above the MSE0.001 target:
opposite-label pairs at60/20degrees ended at MSE0.01356/1.10781, the sharp
cluster at1.03854, and the mixed quartet at0.07660. Their last-state Gaussian
circle RMS values are0.2090,0.3823,0.9189 and0.1702; these are explicitly
partial comparisons. All four have passive/core inconsistencies above0.05.
The two six-input attempts failed while reporting an early compiler limit,
with no usable ODE or accuracy result; logs are retained and there were no
retries. All18 selected/reused controls fitted. Full query-panel size reaches
1,113,509 scalars at four inputs. New scalar training totaled179.10seconds;
all new control training totaled7.53seconds. Independent saved-artifact and
exact-shortcut checks pass with these limitations. The current J2 cutoff is
not robust on this representative suite; no general impossibility theorem
or convergence claim follows. Nine cases were attempted/carried forward;
eight others remain untested. This bounded campaign is closed.

## Target and scope

For a fixed finite dataset, two tanh hidden layers and fixed response-memory
order P, replace the initialized middle matrix by normalized signed
D1 H D2 H D3, with H the symmetric Walsh transform and independent sign
diagonals. Seek a finite autonomous scalar approximation to the same realized
population closure, uniformly on every [0,T], with complexity and constants
independent of width n and preferably polynomial error versus stored size.
Include training outputs, loss and outputs on all unit-circle inputs.
Coefficients and initial state must come from initial information; no future
reference forcing, hidden neuron arrays, or matrix oracle is admissible.
Probability guarantees for random initialization must be stated explicitly.

The primary candidate has genuinely independent central signs. A construction
with only a fixed number of exceptional central signs is a restricted result,
not a resolution of this primary target. Gaussian similarity must be tested
at repeated forward/transpose actions, not inferred from individual entries.

## Model definition

Use normalized inputs u_a, residual r_a=f_a-y_a, and output f_a=c^T h2_a/n.
Set h1_a=tanh(w u_a), h2_a=tanh(W h1_a), delta2_a=c*(1-h2_a^2),
delta1_a=(1-h1_a^2)*(W^T delta2_a), rho=sqrt(mean_a r_a^2).
The original-clock population state has w,c,L and A_k,B_k (n by m), k<P:

    W = W0 - 2/(m n L) sum_k (2k+1) A_k B_k^T
    wdot = -2/m sum_a r_a delta1_a u_a^T
    cdot = -2/m sum_a r_a h2_a
    Ldot = rho
    Adot_k = [r_a delta2_a]_a
              -rho/L [k A_k + sum_{j<k}(2j+1) A_j]
    Bdot_k = rho [h1_a]_a
              -rho/L [k B_k + sum_{j<k}(2j+1) B_j].

Initially L=1, all A=0, B_0=[h1_a(0)] and B_k=0 for k>0. First weights
are independent N(0,1); stored readouts are N(0,1/n^2). The canonical block
mobilities are n,1,n and loss is unhalved mean squared error. No biases.

## Proof search and ownership

The initial proof turn authorized theoretical derivation and source verification,
not a training campaign. Three bounded independent
routes and a synthesis/audit pass are planned; one continuation per concrete
new lemma. Terminal outcomes are a complete audited proof or an explicit
account of the remaining theorem-strength gap. No imposed user budget exists;
the working search budget is approximately 30 minutes, extendable only for a
specific candidate proof audit.

- Root: this README, target synthesis and final proof/report.
- Generic structured route: independent-sign candidate and width-uniform bounds.
- Constructive restricted route: explicit finite ODE and error certificate for
  a declared easier full-rank subfamily, without calling it the primary result.
- Gaussian comparison route: precise initialization and reuse tests; no inference
  of observable incompressibility from an operator-norm distinction.

Permitted inputs are this study, established docs/code, externally verified
primary sources, and the explicit mathematical assignment. No other study is
a dependency. Root has read docs/index.qmd, docs/notation.qmd and workflow Part 1.

## Current status

The primary multi-input independent-sign theorem remains **unproved**. No
claim of impossibility, Gaussian universality, practical efficiency, or
uniform-in-infinite-time accuracy is made. All global statements below mean
every prescribed finite interval `[0,T]`.

Completed artifacts:

- [RESTRICTED_THEOREM.md](RESTRICTED_THEOREM.md): a complete construction and
  proof for `W0 = diag(s) + U V^T/n`, with bounded marks and fixed rank. This
  includes full-rank orthogonal Walsh products with a fixed number of
  exceptional central signs. Weighted moving representatives give an
  autonomous finite scalar ODE, exact forward/transpose treatment, and
  width-independent stability. Gaussian outer initialization gives a
  polynomial scalar-size error bound with prescribed high probability.
  Whole-circle outputs and training loss are controlled simultaneously.
- [GENERIC_ROUTE.md](GENERIC_ROUTE.md): exact sign-gauge reduction and global
  bounds for the independent-sign candidate; a precise sufficient but
  unproved adaptive backward-field tail hypothesis; a conditional scalar
  existence construction. A complete unconditional one-training-input
  theorem follows from a change of coordinates and is proved separately.
  The generic construction has enormous tabulation
  complexity and proves no polynomial rate versus stored size.
- [GAUSSIAN_COMPARISON.md](GAUSSIAN_COMPARISON.md): an elementary repeated-action
  statistic rigorously separates orthogonal sign products from iid Gaussian
  initialization. A second calculation shows that the restricted fixed-rank
  case is close to diagonal mixing on typical initial responses. These are
  initialization comparisons, not observable incompressibility theorems.

The restricted proof has been read and algebraically checked by the root.
The generic draft's multi-sample residual bound was corrected to include
`sqrt(m)`. The one-input scalar construction and Gaussian comparisons were
also checked by another member of the author team; minor normalization and
independence clarifications were incorporated. Cross-checking within this
author team is internal validation, not an independent promotion review.
No training experiment, maintained-book change, or promotion was performed.

The restricted theorem approximates the population closure at fixed `P`.
Any further claim about dense training requires a separately proved
population-to-dense error term. Bounds proved only at each fixed width
cannot be silently upgraded to uniformity in width when adding that term.

## Authorized dense empirical continuation

The user's subsequent request explicitly authorizes comparing Gaussian and
full-rank structured middle initialization under unrestricted dense training,
before any further scalar compression. This is validation of the same
initialization-substitution question. The frozen campaign is
[DENSE_PROTOCOL.md](DENSE_PROTOCOL.md), with an internal
[design review](DENSE_PROTOCOL_REVIEW.md).

It uses twelve precisely specified odd circle teachers/designs, widths128/256,
twelve paired seeds, and seven initialization controls. Every matrix entry
trains densely. This is the declared suite, not a claim to have reconstructed
every historical study configuration. The maintained Chapter14 correlated
three-point cosine example is included. No other study's code or findings
are dependencies.

Implementation: [dense_compare.py](dense_compare.py), [circle_tasks.py](circle_tasks.py),
and [run_dense_comparison.py](run_dense_comparison.py). Root owns the protocol,
tasks, driver, numerical refinement check, plots and this README. The generic
route author owns the dense core and analysis script. The restricted route
author owns the protocol review and independent deterministic checker.

The [deterministic checks](check_dense_compare.py) pass against the maintained
finite-network oracle, including initialization factors, transpose use,
canonical gradients, loss dissipation, oddness, unrestricted dense updates,
Heun order and stopping semantics. The retained report is
`data/generated/structured_full_rank_scalar_20260926/dense_check_results.json`.

A42-pair time-step check across all seven candidates, both widths and three
preselected task cases passes. Halving0.05 to0.025 changes saved circle
predictions by at most3.411e-5 target RMS, and test RMS by at most2.958e-5
target RMS. See [check_dense_refinement.py](check_dense_refinement.py) and
`data/generated/structured_full_rank_scalar_20260926/dense_numeric_comparison_20260926.json`.

The principal2016-trajectory run completed in
`data/generated/structured_full_rank_scalar_20260926/dense_main_20260926`.
Its manifest records exact commands, source hashes, seeds, numerical settings
and environment. See [DENSE_RESULTS.md](DENSE_RESULTS.md) for the completed
function comparison. HD and the independent-sign Walsh product are close on
several easy tasks but do not preserve the canonical fitted function across
the suite. Three slow tasks remain unresolved at the fitted endpoint. The user
requested reporting immediately, so extensions were stopped and excluded.
No scalar-closure training or maintained-code/book change is part of this campaign.

The user clarified during the principal run that the target is the **same
predicted function around the circle as the canonical Gaussian dense network**,
not comparable error against a teacher. This supersedes the original risk-based
decision criterion. Saved full-circle predictions already support the corrected
comparison. Function RMS discrepancy, relative function discrepancy, maximum
sampled discrepancy and seed variability now determine the conclusion.
Gaussian-versus-Gaussian variation is context, not permission to relax fidelity
to the specified Gaussian reference.

## Authorized width2048 HD rerun

The user requested the same circle tasks at n=2048, with HD as the only
structured candidate. [WIDE_HD_PROTOCOL.md](WIDE_HD_PROTOCOL.md) freezes the
comparison against dense Gaussian and independent-middle Gaussian control.
The primary metric is now explicitly absolute RMS of the fitted-function
difference around the circle; relative-amplitude screens are superseded.
Gaussian variability supplies the comparison baseline. All middle entries
train unrestricted. The user set the fitting tolerance to MSE1e-4 before
the principal run. The selected rerun is complete; see
[WIDE_HD_RESULTS.md](WIDE_HD_RESULTS.md).

The user subsequently prohibited reruns: the principal2048 campaign was
not restarted and already uses MSE1e-4. Additional tolerance-refinement runs
were cancelled. No further refinement or slow-task repetition will run.
Completed prelaunch numerical validation remains available; no blanket
all-task refinement certification is claimed.

Before inspecting any2048 comparative outputs, the user’s instruction to avoid
waiting and prohibit reruns narrows reporting to the first complete seed set
across all12 tasks and three methods. Main jobs already running are not
restarted. Queued/repeated seeds will not delay reporting; the campaign will
be interrupted after that complete set is saved. Any other completed outputs
remain retained but no12-seed confidence claim is made from a partial set.

Completed2048 result: all12 tasks and36 selected seed0 networks fit to
MSE1e-4. The report gives absolute HD–Gaussian and Gaussian-control RMS
differences; no amplitude normalization or teacher-risk criterion is used.
The clustered-three-point values are0.045780 versus0.013199; alternating9
is0.024136 versus0.034503. All selected runs pass loss-monotonicity and
circle-quadrature checks. Only the documented prelaunch numerical refinement
is available. One paired seed is not a statistical population-limit result.
All outstanding main/refinement processes were stopped; no further runs are
authorized by these notes.

Quick width plots from saved data only: [HD and Gaussian-control log-log RMS figures](../../data/generated/structured_full_rank_scalar_20260926/width_error_plots_20260926_ready/width_errors.png), generated by [plot_width_errors.py](plot_width_errors.py). Lower widths use12-seed means and MSE1e-6;2048 uses one paired seed and MSE1e-4. Median endpoint slopes across nine common fitted tasks are−0.361 (HD) and−0.496 (Gaussian control); these are descriptive, not proved asymptotic rates. No new training was run.

## Authorized single clustered-task check at width4096

The user explicitly authorizes one further width point for clustered cosine9:
only cluster_triple_cos9, n=4096, seed0, with HD, Gaussian reference and
independent-middle Gaussian control. This supersedes the earlier no-further-runs
note only for this specific check. Same unrestricted dense model and solver,
rtol1e-5/atol1e-8, stop at first MSE1e-4 crossing. Compare absolute whole-circle
RMS discrepancies against the saved2048 seed0 values, never teacher risk or
Gaussian-amplitude-normalized errors. Evaluate4096 angles and check the nested
2048-point quadrature difference<=1e-4. Loss rises>1e-7, nonfinite output or
missing fitted endpoints prevent a clean numerical interpretation.
Exactly3 training trajectories,3 workers with1 BLAS thread each,30 wall minutes,
target memory below12GiB. No additional seeds, tasks, refinement reruns, or
scientific selection. A decrease supports the observed finite-width trend;
a flat/increasing discrepancy is adverse to that trend but a single seed
cannot determine the infinite-width limit. Existing source core is unchanged.
Root owns execution and results; a scoped agent independently checks the
saved2048 comparison values. Generated run: wide_hd_cluster4096_20260926.

Completed single width4096 check: all three seed0 networks reached MSE1e-4,
with no accepted-step loss rise. Absolute HD–Gaussian circle RMS is
0.04417320285935848, versus0.04577976680578513 at2048 (3.51% lower).
Gaussian-control RMS is0.010607160764797459, versus0.013199408679544547
at2048 (19.64% lower). The HD/control ratio increases from3.47 to4.16.
Thus both discrepancies decrease, but HD is nearly flat over this doubling;
this point does not establish decay to zero. Both widths use seed0 and the
same stopping tolerance. Nested quadrature changes the4096 discrepancy by
at most4.17e-17. No extra training or refinement was run. Full saved states,
source snapshots and hashes are in the authorized run directory; analysis is
[the width4096 report](../../data/generated/structured_full_rank_scalar_20260926/wide_hd_cluster4096_analysis_20260926/report.md).

## Authorized two-task width8192 continuation

The user requests the same comparison at 8k for clustered cosine9 and the
bright pink plot curve, Alternating9. Use n=8192 (power of two for HD), seed0,
tasks cluster_triple_cos9 and alternating9, and exactly Gaussian reference,
independent-middle Gaussian control, and HD: six unrestricted dense trajectories.
All use the existing canonical model, initialization streams, adaptive RK45
with rtol1e-5/atol1e-8, and first training-MSE1e-4 crossing. No additional
seeds, tasks or numerical-refinement reruns. A scoped read-only agent independently
verified the pink task and its saved2048 baseline; root owns execution/report.

Primary metrics remain absolute circle RMS(f_HD-f_G) and RMS(f_G2-f_G),
using4096 uniformly spaced angles. Compare clustered with saved2048/4096
and Alternating9 with saved2048. Decrease supports the observed finite-width
trend; flat/increase is adverse to that trend, not proof about population limits.
A decrease smaller than1e-4 is numerically inconclusive at the reporting scale.
Require all fitted endpoints, finite predictions, loss rises<=1e-7 and nested
2048-point quadrature difference<=1e-4. One paired seed yields no confidence
interval. No new solver-refinement certificate is claimed.

Budget: six trajectories, three workers with one BLAS thread each, at most
120 wall minutes, expected peak memory below40GiB. Physical-time caps and
same-state continuation follow the existing driver (3000 then10000 if needed).
Stop each trajectory at MSE1e-4; no scientific-result-dependent branches.
Fresh generated output: wide_hd_two_tasks8192_20260926. Source/configuration
snapshots, full final weights, predictions, histories and hashes are retained.

Width8192 interim checkpoint (superseded by the stopped-run status below): clustered cosine9 is complete (all three seed0
networks reach MSE1e-4, zero recorded loss rises). Saved-prediction RMS values
are HD-G=0.043380591983378236 and G2-G=0.0023870772522722244. Against4096,
HD decreases1.79% while the Gaussian control decreases77.50%. Nested quadrature
changes are below3.5e-17, and NPZ hashes match producer metadata. This supports
an almost flat HD discrepancy on these three wide points, not a proved nonzero
infinite-width limit. Alternating9 remains in progress in the same six-job run;
no rerun or additional task was launched.

### Width8192 stopped-run result

At the user's explicit request, the remaining Alternating9 jobs were stopped
rather than waiting for convergence. Exec exited130 after interruption. The
existing driver lacked an interruption checkpoint: no partial Alternating9
weights, outputs or loss values were saved, and none are reported as fitted.
All three completed clustered cosine9 files remain intact. No additional
training or restart is authorized. The stopped campaign is explicitly marked
by STOPPED.json with a new artifact hash index, preserving the original manifest.

For clustered cosine9, absolute circle-function RMS values are:

| Width | HD-Gaussian | Independent-middle Gaussian-Gaussian |
|---:|---:|---:|
| 2048 | 0.04577976680578513 | 0.013199408679544547 |
| 4096 | 0.04417320285935848 | 0.010607160764797459 |
| 8192 | 0.043380591983378236 | 0.0023870772522722244 |

Every listed network uses seed0, identical outer initialization within each
width and MSE1e-4 stopping. The last width doubling reduces HD discrepancy1.79%
and the Gaussian baseline77.50%; HD/Gaussian-baseline ratio is18.17 at8192.
This is adverse finite-width evidence for HD function agreement on this task,
not a proof of distinct population limits. The pink Alternating9 curve has
no usable8192 point; its saved2048 values remain HD-G=0.02413591289201196 and
G2-G=0.03450258118306089.

[Stopped-run analysis](../../data/generated/structured_full_rank_scalar_20260926/wide_hd_two_tasks8192_stopped_analysis_20260926/report.md).
Root checked saved-array hashes, MSE, loss monotonicity and nested circle
quadrature; the scoped baseline agent independently checked the pink-task
mapping and2048 numbers and produced the completed clustered-task plot.

Completed-data plot: [clustered cosine9 widths2048/4096/8192](../../data/generated/structured_full_rank_scalar_20260926/cluster_wide_stopped8192_plot_20260926/cluster_width_errors.png), produced by [plot_cluster_wide_check.py](plot_cluster_wide_check.py), without new training.

## Authorized third Gaussian draw at width8192

User requests one additional independent Gaussian run to test whether the
small0.0023870772522722244 Gaussian-pair discrepancy was atypical. Continue
cluster_triple_cos9 at n=8192. Preserve outer initialization seed0 (streams1/2)
and draw the new Gaussian middle with SeedSequence([1,101]), distinct from
both existing [0,101] and [0,102]. This measures the same conditional middle-
initialization variability as the original control, not full-network seed
variability. No other task or repetition is authorized.

Use the unchanged canonical dense RHS and adaptive RK45 at rtol1e-5,
atol1e-8, first MSE1e-4 crossing;4096 circle angles and nested2048-point check.
Report all three Gaussian pairwise absolute circle RMS values, and the new
Gaussian versus existing HD if useful. Values near the original discrepancy
support low variability for these three draws; substantially larger new
pairwise discrepancies show the original pair was unusually close within
this set. No population variance estimate or confidence guarantee follows
from three draws. Numerical differences<=1e-4 are inconclusive. Require fitted
endpoints, no loss rise>1e-7, finite predictions, and grid difference<=1e-4.

Exactly one trajectory, one BLAS thread,40-minute training budget, expected
memory below12GiB. Existing physical cap3000 then10000 if needed. No automatic
refinement/rerun. A small separate driver adds live loss reporting and a STOP
file/signal handler that saves the last accepted state, without changing the
solver. Interrupted states remain explicitly partial. New run directory:
wide_gaussian_third8192_20260926. Root owns driver/run/report; scoped agent
checks initialization, solver equivalence and stop behavior before launch.

### Third Gaussian completed result

The single new Gaussian finished in14.1927 wall minutes at training
MSE9.99999999999886e-5, physical time31.7939655410, with81 accepted RK45
steps and zero recorded loss rise. No interruption or further run was needed.
Absolute circle-function RMS differences are G1-G2=0.0023870772522722244,
G3-G1=0.006015538748869226, and G3-G2=0.006943684698449176. The new
comparisons are2.52 and2.91 times the original pair's distance. Thus the
original pair was particularly close within these three matched-outer draws;
it should not by itself represent the typical Gaussian variability scale.
Three draws do not establish an outlier probability or a reliable population
variance. All pairwise values remain well below the saved HD-G1 value0.04338.

Validation: the scoped third_gaussian_check agent verified RNG streams,
matched outer initialization, canonical RHS equality in a tiny non-training
check, unchanged RK45 settings, and cooperative stop logic. Root verified
exact core/solver/task source-hash equality with the original campaign;
the analysis verifies saved NPZ hashes, common grids, recomputed training
losses, loss-monotonicity flags and nested quadrature (maximum3.34e-17).
These are internal checks; no new tolerance-refinement or promotion occurred.
Source snapshots and actual configuration are preserved with the run.

Reproduction: [run_extra_gaussian.py](run_extra_gaussian.py) with output
wide_gaussian_third8192_20260926, width8192, outer-seed0, middle-seed1,
wall-minutes40; [analyze_extra_gaussian.py](analyze_extra_gaussian.py) compares
that run with wide_hd_two_tasks8192_20260926. Full exact commands are in the
run manifest and the conversation; neither command authorizes additional
training. [Result report](../../data/generated/structured_full_rank_scalar_20260926/wide_gaussian_third8192_analysis_20260926/report.md).
Only the requested one new trajectory was run. No further experiments remain
authorized by this request.

## Gaussian-faithful hierarchy: theoretical continuation

The user asks whether full-rank initialization can admit an efficient finite
scalar approximation while approaching the canonical Gaussian trained output,
with a polynomial accuracy–cost relation. This continuation is theoretical;
no new training was authorized or performed. The corrected synthesis is
[GAUSSIAN_HIERARCHY_ASSESSMENT.md](GAUSSIAN_HIERARCHY_ASSESSMENT.md).

Three fresh bounded routes used the supplied canonical equations, required
skills, and explicitly authorized primary-source lookup where relevant:
[BLOCK_HIERARCHY_ROUTE.md](BLOCK_HIERARCHY_ROUTE.md),
[FAST_HIERARCHY_ROUTE.md](FAST_HIERARCHY_ROUTE.md), and
[EFFICIENT_HIERARCHY_AUDIT.md](EFFICIENT_HIERARCHY_AUDIT.md).
No other study was a scientific input. Root read the complete frozen notes
and checked the algebra and scope; these are author-team checks, not promotion
reviews. The relevant existing restricted/generic/comparison notes in this
study were read completely. HEAD remained
86f85d30f03811e7791a4b317cee85296efcafb2, with an empty index; unrelated shared
modifications were left untouched.

The concrete new candidate uses independent k-by-k Gaussian initialization
blocks and retains the original globally coupled learned correction. A
q-block approximation to its block population uses
1+qk(d+1+2mP) evolving scalars and qk² stored matrix coefficients, independent
of ambient width. This is an exact causal block representation followed by
moving representative approximation; it is not an exact low-order aggregate
closure. Cross-block learning and nonlinear features remain present.

An elementary comparison proves, for one sample with zero population initial
readout, an initial output-velocity discrepancy at most |y|/k from canonical
Gaussian initialization. It does not prove a trained-time bound. Root and
the scoped audit agent checked the Gaussian heat identity, centered Taylor
remainder, and derivative constant ||(tanh²)''''||infinity=16.

Fixed-k bounded-block sampling admits a q^{-1/2} coupling estimate, but
operator-norm control alone only gives a conservative stability constant
exp(C_T sqrt(k)). A preliminary dimension-free claim was rejected and
corrected: the first-layer gate multiplies an adaptively correlated backward
field whose coordinate maximum is not bounded by normalized L2 control.
Polynomial sampling stability and identification of the large-block trained
law with the Gaussian trained law remain open. Response order P is a separate
axis; a dense-network conclusion also needs a width-uniform memory error.

A verified primary source supplies stronger fixed-program universality for
independently scrambled fast bases with a Gaussian-matched singular-value
law. It supports a credible alternative to plain HD, but neither its AMP
theorem nor fast multiplication proves the desired tanh scalar-ODE theorem.
The current belief favors a possible randomized hierarchy for bounded tasks
and finite horizons; a polynomial global guarantee is not established, and
no general impossibility result is claimed. No implementation, experiment,
maintained-book edit, or promotion is authorized by this theoretical update.

## Authorized quick Gaussian-block check at width1024

The user now authorizes a quick empirical comparison of Gaussian blocks with
HD at n=1024, stopping at training MSE 0.01, with less than one minute per run.
Freeze two tasks: cluster_triple_cos9 (3 samples) and alternating5 (10 samples).
Use seed0 with matched outer initialization, and Gaussian, independent-middle
Gaussian control, HD, and Gaussian block sizes8,32,128: exactly12 trajectories.
Every middle matrix is trained densely without any structural constraint.
This isolates initialization replacement; it does not test a scalar closure.

Primary metric is absolute RMS(f_method-f_Gaussian) around2048 circle angles,
with a nested1024 check. Gaussian-control discrepancy measures conditional
initialization variability. For each task, block128 improves on HD if the
RMS is lower by more than1e-3, worsens if higher by more than1e-3, otherwise
is inconclusive at this reporting resolution. Orders8/32/128 show the saved
trend without establishing convergence from one draw. Block8/32 differences
are reported regardless of their direction. No selection, new seeds or
additional tasks follow from the outcome.

Reuse the exact canonical dense RHS and block-error-norm RK45 at rtol1e-5,
atol1e-8. Require finite predictions, successful common MSE 0.01 crossings,
loss rises<=1e-7, and nested quadrature discrepancy<=1e-4. No tolerance
refinement is claimed. Three worker processes each use one BLAS thread;
solver deadline50sec and training interrupt55sec reserve time for evaluation
and saving, with a target end-to-end bound60sec per trajectory. Save the last
accepted state on interruption and label it partial. No run is extended past
its budget. Exactly12 runs, no result-dependent followups.

Root owns [quick_block_compare.py](quick_block_compare.py), execution and
reporting. Scoped quick_block_check independently checks canonical equations,
block scaling, matched initialization, metrics and stopping; no training by
that agent. Fresh generated directory quick_blocks1024_20260926 stores source
snapshots, configuration and environment, full final states, predictions,
histories, file hashes, runtime and comparisons. This is a quick empirical
check, not a population-limit or scalar-compression guarantee.

### Quick block result

Completed exactly12 trajectories in39.06 wall seconds with three workers.
Every model reached the MSE 0.01 threshold, with zero recorded loss rise;
training took7.05–12.42sec and the maximum including evaluation/save was12.58sec.
No trajectory restart, extension, or additional training occurred. One initial
launch failed on an optional metadata import before creating the output
directory or starting training; removing that dependency resolved startup.

Absolute circle RMS against the Gaussian reference:

| Initialization | Clustered cosine9 (3 samples) | Alternating cosine5 (10 samples) |
|---|---:|---:|
| Independent Gaussian control | 0.01075653 | 0.00576148 |
| HD | 0.04403217 | 0.00689001 |
| Gaussian blocks8 | 0.03545822 | 0.01474128 |
| Gaussian blocks32 | 0.02511956 | 0.00981942 |
| Gaussian blocks128 | 0.04309199 | 0.00665543 |

Block32 improves the clustered-task discrepancy by43% relative to HD, but
block128 loses that improvement. Alternating5 improves as block size increases,
with block128 close to HD and the Gaussian control scale. Under the frozen
1e-3 discriminator, block128 versus HD is inconclusive on both tasks. The
results do not show a reliable general advantage or monotone hierarchy on
clustered9. Different block sizes use independent streams and only one draw;
this is not a rate estimate or infinite-population conclusion.

Root verified current/source-snapshot hash equality, all saved-state hashes,
successful endpoints, monotonicity, and all per-run budgets. Nested2048/1024
quadrature changes are at most2.43e-17. Scoped audit checks the canonical RHS
against the existing implementation, nonzero off-block learned velocities,
matched outer initialization, block scaling and independent saved metrics.
See [QUICK_BLOCK_CHECK.md](QUICK_BLOCK_CHECK.md) for its exact scope/results.
No tolerance-refinement certificate or scalar-closure validation is claimed.

Reproduction command, from the repository root, using a fresh output path:
`python studies/structured_full_rank_scalar_20260926/quick_block_compare.py --output data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_20260926`.
The named directory now exists and must not be overwritten.
[Saved report](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_20260926/report.md).
The requested quick comparison is complete; no follow-up experiment is queued.

## Authorized stopping-threshold continuation

The user accepts suggestion1: continue the saved twelve width1024 networks
from MSE 0.01 to MSE0.001, with no restart, new seed, width change, solver
change, or additional threshold. Root extends quick_block_compare.py to load
the exact saved w,W,c; verify input-state hashes and unchanged canonical
source hashes; and preserve physical-time offsets. Same two tasks, six
methods, RK45 rtol1e-5/atol1e-8, 2048 circle angles and three single-thread
workers. Per-trajectory deadline50sec/interrupt55sec and under60sec total
budget persist. Partial states remain labelled; no budget extensions.

Question: does reducing stopping loss remove the nonmonotone block-order
trend? Report every before/after absolute circle RMS vs its same-threshold
Gaussian reference, and RMS change of the entire method-minus-Gaussian
function. Define the block trend's upward excursion as the sum of positive
increases from k8 to32 to128. A reduction greater than1e-3 supports a less
erratic trend; changes within1e-3 are unresolved at this reporting scale.
This does not isolate seed noise or establish an order rate. Require successful
MSE0.001 endpoints, finite predictions, loss rises<=1e-7, nested grid changes
<=1e-4, and identical continuation start predictions. No tolerance refinement
is claimed.

Fresh output: quick_blocks1024_loss001_20260926. Root owns driver/run/README;
scoped quick_block_check owns plot_block_continuation.py and
QUICK_BLOCK_CONTINUATION_CHECK.md, performing read-only result checks and
plotting without training. Exactly12 checkpoint continuations; no further
branch follows from their outcomes.

### Stopping-threshold result

All12 continuations reached MSE0.001 in1.02–2.01sec training each,2.20sec
maximum including evaluation/save,7.12sec total batch wall time. No model
was reinitialized. Every start checkpoint hash, start MSE and physical-time
offset matches the saved MSE 0.01 state exactly; all source/snapshot/output
hashes passed. Zero loss rises, with nested grid discrepancy<=2.09e-17.

Absolute circle RMS versus each threshold's Gaussian reference:

| Initialization | Cluster9: MSE 0.01 → 0.001 | Alternating5: MSE 0.01 → 0.001 |
|---|---:|---:|
| Gaussian control | 0.01075653 → 0.01213003 | 0.00576148 → 0.00730941 |
| HD | 0.04403217 → 0.04591039 | 0.00689001 → 0.00881456 |
| Block8 | 0.03545822 → 0.03558447 | 0.01474128 → 0.01777108 |
| Block32 | 0.02511956 → 0.02589839 | 0.00981942 → 0.01354010 |
| Block128 | 0.04309199 → 0.04144820 | 0.00665543 → 0.00955656 |

The cluster block32-to128 upward excursion falls from0.01797243 to0.01554981,
a13.48% reduction. It passes the frozen1e-3 reduction criterion but leaves a
large nonmonotone trend and unchanged block ranking. Alternating5 was and
remains monotone in block size, while all discrepancies increase. The lower
stopping loss therefore does not explain away the irregular cluster curve.
It changes the small HD/block128 ordering on alternating5, so small gaps
remain threshold-sensitive. No population or seed-variance conclusion follows.

The full method-minus-Gaussian circle function changes by0.00094–0.00318
RMS for cluster block/HD methods and0.00334–0.00610 for alternating5. Thus
the threshold is more consequential relative to the smaller alternating5
differences. Root validated exact state provenance and saved metrics; the
scoped continuation audit independently checks the driver/results and plots.

Reproduction command (choose a fresh destination for any authorized repeat):
`python studies/structured_full_rank_scalar_20260926/quick_block_compare.py --resume data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_20260926 --target 0.001 --output data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_loss001_20260926`.
[Report](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_loss001_20260926/report.md).
Before/after figure: [block_continuation.png](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_loss001_20260926/block_continuation.png),
produced by [plot_block_continuation.py](plot_block_continuation.py); root
visually checked axes, threshold legends, and reference-line interpretation.
Only the requested first suggestion was executed. No new seeds, width sweep,
tolerance-refinement run, or further-loss continuation is queued.

## Authorized width2048 clustered-task seed check

User requests n2048 on the cluster task to test whether the block-order V
shape weakens, and suggests a new random seed. Freeze exactly12 trajectories:
cluster_triple_cos9, width2048, seeds0 and1, each with Gaussian, independent
Gaussian control, HD, block8, block32 and block128. Each seed matches both
outer layers across its six methods; seed1 redraws all layers. Stop every
trajectory at MSE0.001 for comparability with saved1024 seed0 endpoints.
No new task, block order, seed or solver refinement follows from the results.

Use unchanged canonical unrestricted dense RHS and RK45 rtol1e-5/atol1e-8.
Two worker processes, each with one BLAS thread, reduce memory-bandwidth
contention at doubled width. Per-run solver deadline50sec/interrupt55sec and
under60sec end-to-end goal remain. Runs hitting a budget save accepted partial
states and are not extended or silently treated as fitted. The two seed
campaigns execute sequentially; no more than two training workers at a time.

Primary metric remains absolute circle RMS vs each seed's Gaussian reference
at2048 angles with a nested1024 check. Compare the three block-order curves
(1024 seed0,2048 seed0,2048 seed1). Sum positive successive increases from
k8 to32 to128 to measure failure of monotone improvement. A reduction>1e-3
supports a weaker upturn for that realization; monotonicity in both2048 draws
is stronger evidence against the V being stable. Two seeds do not establish
a variance estimate or an order law. Require successful common thresholds,
finite predictions, loss rises<=1e-7 and grid discrepancy<=1e-4.

Root owns generalized quick_block_compare.py/run/README. Scoped quick_block_check
owns plot_block_width_seed.py and QUICK_BLOCK_WIDTH_CHECK.md; its reads are
limited to this study's assigned sources and exact baseline/new run folders,
and it performs no training. Outputs are fresh directories
quick_blocks2048_cluster_seed0_20260926 and
quick_blocks2048_cluster_seed1_20260926, with full states and provenance.

Runtime correction before finishing the width2048 campaign: two concurrent
workers reached the conservative50sec soft cutoff on several seed0 models.
The original user ceiling is60sec per trajectory. Preserve every accepted
checkpoint and finish serially using only the remaining cumulative allowance,
with2sec reserved for saving and an explicit cumulative-time field. This
supersedes the internal50sec-no-extension scheduling rule; it does not extend
the user's60sec ceiling or authorize new trajectories. Fresh completion
directory: quick_blocks2048_cluster_seed0_finished_20260926. Original partial
states and source snapshots remain intact. Seed1 uses one worker from the
start. No solver tolerance, vector field, seed, or target is changed.

### Width2048 seed-check result

The matched-MSE0.001 block32-to128 upward bend is0.01554980 at1024 seed0,
0.01172925 at2048 seed0, and0.00501411 at2048 seed1. The same-seed width
doubling reduces this bend24.57%; the new seed has a still smaller bend,
but remains nonmonotone. Both2048 seeds put block32 and block128 substantially
closer to Gaussian than HD. This supports a softer V on the tested configurations,
not a monotone order law or a critical square-root-width block size.

Absolute circle RMS against the corresponding Gaussian reference:

| Initialization | 1024 seed0 | 2048 seed0 | 2048 seed1 |
|---|---:|---:|---:|
| Gaussian control | 0.01213003 | 0.01345149 | 0.02140953 |
| HD | 0.04591039 | 0.04521394 | 0.05254072 |
| Block8 | 0.03558447 | not fitted to target | 0.04751698 |
| Block32 | 0.02589839 | 0.01677709 | 0.01969807 |
| Block128 | 0.04144820 | 0.02850633 | 0.02471218 |

Seed0 block8 reached MSE0.0017236789 at58.55sec cumulative and is excluded
from matched-target curves. Its partial diagnostic RMS0.04450845 must not
be presented as a MSE0.001 endpoint. Five seed0 trajectories reached target
within50.11–56.46sec cumulative (including checkpoint completion); all six
seed1 trajectories reached target in34.51–45.30sec including output saving.
No trajectory exceeded the user's60sec bound, no model was restarted from
initialization, and no further continuation is queued. Seed1 was serial from
the start; its six-model batch took224.26sec. Thus eleven of twelve new
trajectories have valid target endpoints and the remaining one stays partial.

Root verified source/snapshot and state hashes, checkpoint continuity for
seed0, recomputed saved MSE/RMS, zero recorded loss rises, and cumulative
budgets. Maximum nested-grid change is3.30e-17. Scoped quick_block_check
independently audits sources/results and creates the width/seed figure;
see QUICK_BLOCK_WIDTH_CHECK.md. No solver-refinement certificate is claimed.
New seed1 varies all initial blocks, while matching outer weights across
methods within that seed. It is not isolated middle-matrix resampling.

The driver commands use `--width 2048 --tasks cluster_triple_cos9 --target 0.001`
with `--seed 0 --workers 2` for the preserved first stage, then
`--seed 0 --workers 1 --resume <first-stage directory> --finish-partials`
for the cumulative-budget completion, and `--seed 1 --workers 1` for the new
seed. Exact commands and source snapshots are in each manifest. Outputs:
[seed0 matched/partial status](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_cluster_seed0_finished_20260926/report.md),
[seed1 report](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_cluster_seed1_20260926/report.md).
Plot source: [plot_block_width_seed.py](plot_block_width_seed.py).

## Authorized intermediate block-size plot

User requests a denser one-seed block-size curve up to128 at width2048 on
clustered cosine9. Interpret the requested sizes as doubling from8:
8,16,32,64,128, stated explicitly in commentary. Reuse the complete seed1
Gaussian/Gaussian-control/HD/block8/block32/block128 states at MSE0.001.
Run exactly two new trajectories, block16 and block64, with identical outer
seed1 and the existing size-specific middle streams [1,316] and [1,364].
Distinct block-size streams mean this does not rule out initialization noise.

Unchanged canonical dense RHS/RK45 rtol1e-5/atol1e-8, one single-thread
worker, target0.001, soft deadline50sec/interrupt55sec, per-run ceiling60sec.
No existing trajectory is rerun. Validity gates remain finite predictions,
matched successful target stops, zero loss rises above1e-7, input/source/state
hash agreement and2048/1024 quadrature difference<=1e-4. Report all five
points and classify successive rises>1e-3 as departures from a decreasing
trend; smaller differences are unresolved at this reporting scale. No new
seed, extra block size, lower loss or width follows from the outcome.

Root owns fill_block_sizes.py and runs; scoped quick_block_check owns
plot_block_sizes.py and QUICK_BLOCK_SIZE_CHECK.md, with only assigned study
code, the exact seed1 baseline, and the new run as scientific inputs. New
output: quick_blocks2048_seed1_fill_20260926. Source snapshots, full new
states and explicit provenance of reused reference files are preserved.

### Intermediate-size result

Exactly block16 and block64 were newly trained, both reaching MSE0.001
with zero loss rises. They took38.11sec and35.63sec including evaluation/save;
all previously fitted states and references were reused without retraining.

| Block size k | Absolute circle RMS vs Gaussian |
|---:|---:|
| 8 | 0.04751698 |
| 16 | 0.02869703 |
| 32 | 0.01969807 |
| 64 | 0.01795165 |
| 128 | 0.02471218 |

The seed1 curve decreases at every tested doubling from8 through64, then
rises at128. The32→64 improvement is0.00174642 and the64→128 rise0.00676053.
Thus64 is the lowest observed point in this realization; this is not an
ensemble-optimal block size. The Gaussian control is0.02140953 and HD is
0.05254072. Distinct block-size streams and one realization per size do not
rule out seed effects, despite the denser curve's pattern.

Root checked source/snapshot and new/reused state hashes, exact saved RMS
and MSE recomputation, successful endpoints, monotone recorded losses and
the60sec budget. The scoped checker audits the producer and creates the
figure without training. No solver refinement, additional seed, block size,
or task was run. See [QUICK_BLOCK_SIZE_CHECK.md](QUICK_BLOCK_SIZE_CHECK.md).

Reproduction: `python studies/structured_full_rank_scalar_20260926/fill_block_sizes.py --baseline data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_cluster_seed1_20260926 --output data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_seed1_fill_20260926` (output must be fresh).
[Report](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_seed1_fill_20260926/report.md).
Plot source: [plot_block_sizes.py](plot_block_sizes.py). The authorized
two-run extension is complete; no further experiment is queued.

## Authorized width1024 overlay

User requests the same five-point curve at width1024 overlaid on width2048.
Use seed1, cluster_triple_cos9, block sizes8/16/32/64/128, MSE0.001, unchanged
canonical dense training and RK45 rtol1e-5/atol1e-8. Existing width1024 block
results use seed0, so none match this protocol. Freeze exactly seven fresh
trajectories: the five blocks, Gaussian reference and Gaussian control. Reuse
the entire saved width2048 seed1 curve without training. Matched seed denotes
matching stream rules across widths, not identical or fully nested matrices.

Primary metric remains absolute RMS of each fitted circle function minus its
same-width Gaussian reference, on2048 angles with a nested1024 grid check.
Report all points; decreases/rises larger than1e-3 describe the curve shape,
smaller differences remain unresolved at the reporting scale. Compare observed
minima and upturns without claiming a population rate or seed independence.
Validity gates: successful MSE0.001 endpoints, finite outputs, loss rises<=1e-7,
quadrature change<=1e-4, and source/data hash agreement. One single-thread
worker,50sec soft deadline/55sec interrupt,60sec maximum per trajectory;
save and label partials, with no extension or rerun. No new task, seed, block
size or lower threshold follows from the results.

Root owns run_block_overlay.py, execution and README; scoped width_overlay_plot
owns plot_block_width_overlay.py and QUICK_BLOCK_OVERLAY_CHECK.md, with no
training authority. Fresh output quick_blocks1024_seed1_overlay_20260926
records source snapshots, full final states, metrics, timings and provenance.
Overlay baseline is quick_blocks2048_seed1_fill_20260926 and its explicit
quick_blocks2048_cluster_seed1_20260926 reference. The authorized study scope
is unchanged; no other study or maintained scientific source is modified.

### Width1024 overlay result

All seven new width1024 seed1 trajectories reached MSE0.001, with no loss
rises; each took6.68–8.40sec including evaluation and saving. The five block
points at both widths are:

| Block size k | Width1024 RMS vs Gaussian | Width2048 RMS vs Gaussian |
|---:|---:|---:|
| 8 | 0.06656544 | 0.04751698 |
| 16 | 0.03210559 | 0.02869703 |
| 32 | 0.02571373 | 0.01969807 |
| 64 | 0.03545403 | 0.01795165 |
| 128 | 0.06303078 | 0.02471218 |

Width1024 decreases through32 then rises at64 and128; width2048 decreases
through64 then rises at128. The observed minimum therefore shifts from32 to64
for this seed. Width2048 has a lower discrepancy at every tested block size,
but its Gaussian-control discrepancy is0.02140953 versus0.01291856 at1024.
One reference/draw per size remains insufficient to identify an asymptotic
optimum, a square-root-width scaling or a population-limit rate. All2048
outputs were reused unchanged. No additional runs or solver refinement occurred.

Root verified exact source/snapshot agreement, hashes of all new saved states,
successful fitted status, loss monotonicity and runtime ceilings. The scoped
plot/check agent independently recomputes saved predictions and metrics;
see [QUICK_BLOCK_OVERLAY_CHECK.md](QUICK_BLOCK_OVERLAY_CHECK.md).

Reproduction: `python studies/structured_full_rank_scalar_20260926/run_block_overlay.py --baseline data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_seed1_fill_20260926 --output data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_seed1_overlay_20260926` (use a fresh destination for any authorized repeat).
[Report](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks1024_seed1_overlay_20260926/report.md).
Plot source: [plot_block_width_overlay.py](plot_block_width_overlay.py).
The requested overlay is complete; no further experiment is queued.

## Authorized all-task block curves at MSE 0.01

User requests width2048, stopping loss0.01, and block sizes8/16/32 for all
circle tasks. Freeze the twelve existing circle_tasks.TASKS, seed1, with
Gaussian reference, independent-middle Gaussian control, block8, block16,
and block32 on each: exactly60 trajectories. No saved manifest matches this
width/seed/threshold, so all are new. Earlier lower-loss endpoints cannot be
substituted for first MSE 0.01 crossings. No HD, extra seed, block order,
task or threshold is added. All matrix entries train without constraints.

Use unchanged quick_block_compare.run_one and canonical RK45 settings
rtol1e-5/atol1e-8. One serial worker with one BLAS thread prevents the
contention seen in the earlier2048 run. Each trajectory has50sec training
deadline,55sec interrupt and60sec total ceiling; partial accepted states
remain saved and are excluded from fitted curves. No budget extensions,
restarts, result-dependent followups or tolerance-refinement runs.

Primary metric is absolute circle RMS(f_block-f_Gaussian), with Gaussian
variability control;2048-angle evaluation and nested1024 check. Each panel
uses its own task's reference. Compare k8→16→32: decreases/rises>1e-3 are
descriptive improvements/worsening; changes within1e-3 are inconclusive at
that reporting scale. Require finite outputs, target MSE reached, loss
rises<=1e-7, quadrature change<=1e-4 and source/state hashes. Report all12
tasks, including missing fitted points. One seed gives no rate theorem or
task-uniform accuracy guarantee. This changes initialization only, not a
memory/scalar closure or teacher-risk comparison.

Root owns run_all_task_blocks.py, execution and README. Scoped
all_tasks_block_plot owns plot_all_task_blocks.py and
QUICK_ALL_TASK_BLOCK_CHECK.md; no training authority. Fresh output is
quick_blocks2048_all_tasks_loss01_20260926, with snapshots, settings,
full states, per-run timing/status, live comparisons and final12-panel plot.

### All-task block-curve result

Executed exactly60 trajectories, exit0, in1087.3sec (18.1min) serial batch
time. Eleven tasks have all five fits at MSE 0.01:55 fitted trajectories,
each6.27–42.34sec including circle evaluation and saving. All five
alternating9 trajectories stopped at the50sec training deadline and remain
partial, with total times50.55–50.59sec. Their MSEs were Gaussian0.23658,
control0.22718, block8 0.55752, block16 0.50803, block32 0.33331. Since the
Gaussian reference did not fit, alternating9 has no matched-target curve.
No partial run was extended, restarted or represented as fitted.

Absolute circle RMS versus the fitted Gaussian at MSE 0.01:

| Task | Gaussian control | Block8 | Block16 | Block32 |
|---|---:|---:|---:|---:|
| pair_cos1 | 0.01271429 | 0.00549032 | 0.00552247 | 0.00273561 |
| pair_cos3 | 0.00317927 | 0.00333623 | 0.00172532 | 0.00228571 |
| near_pair_sin9 | 0.00166608 | 0.01312792 | 0.00692856 | 0.00315474 |
| triple_cos3 | 0.00236319 | 0.01283131 | 0.00632927 | 0.00524029 |
| triple_mixed | 0.00184649 | 0.00160134 | 0.00156179 | 0.00156218 |
| cluster_triple_cos9 | 0.02274340 | 0.04648031 | 0.02867908 | 0.02014407 |
| broad_ridge6 | 0.00443706 | 0.00188723 | 0.00294109 | 0.00111120 |
| sharp_ridge8 | 0.00068610 | 0.00139716 | 0.00093339 | 0.00115791 |
| alternating3 | 0.00333807 | 0.00543681 | 0.00416897 | 0.00256373 |
| alternating5 | 0.00681567 | 0.01456660 | 0.00766276 | 0.00690433 |
| alternating9 | not fitted | not fitted | not fitted | not fitted |
| multiscale12 | 0.00140693 | 0.00565881 | 0.00456558 | 0.00167582 |

For all11 completed tasks, block32 is closer to Gaussian than block8 in
this draw. Six curves decrease at both steps; five have an intermediate
fluctuation, only the broad-ridge8→16 rise exceeding the predeclared1e-3
descriptive threshold. Eight endpoint8→32 improvements exceed1e-3, while
the other three are smaller. Block32 is below the single Gaussian-control
discrepancy on6/11 completed tasks. These are one-seed empirical comparisons;
they do not establish a population approximation rate or remove seed effects.

Root checked all60 source/snapshot/state hashes, exact expected task/method
coverage, monotone recorded losses, quadrature diagnostics and runtime
ceilings. The scoped checker independently audits saved metrics and selected
weight-forward evaluations and creates the12-panel figure and CSV. Source:
[plot_all_task_blocks.py](plot_all_task_blocks.py); check report:
[QUICK_ALL_TASK_BLOCK_CHECK.md](QUICK_ALL_TASK_BLOCK_CHECK.md).

Reproduction: `python studies/structured_full_rank_scalar_20260926/run_all_task_blocks.py --output data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_all_tasks_loss01_20260926` (destination must be fresh).
[Saved report](../../data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_all_tasks_loss01_20260926/report.md).
All requested configurations were attempted; alternating9 remains unresolved
at the fitted endpoint under the per-run budget. No further run is queued.

## Authorized moving representative-block closure implementation

User requests implementing the proposed autonomous scalar hierarchy and testing
whole-circle RMS on a few tasks. This continues the block-initialization and
compression investigation. Freeze near_pair_sin9, cluster_triple_cos9 and
alternating5, block size16, original width2048 (128 blocks), outer/middle seed1,
and first training-MSE 0.01 crossing. Primary error is fitted circle RMS against
the full128-block memory closure at the same history order. Separately report
history error against the saved unrestricted dense block16 model and total
error against the saved dense Gaussian model. Teacher RMS is not the metric.

Retain q=8,32,64 whole initial blocks from nested random subsets of the128
original blocks; use three predetermined subset streams1001,1002,1003. All
retained blocks evolve and share residuals/global history contractions. The
original seed1 readout values (standard deviation1/2048) are retained; do not
replace them by1/(qk) or zero. This targets a specific finite population
closure, not yet its infinite-width limit. No test inputs enter training.

Numerical calibration precedes the representative runs: run all three full
references at history order8. If any fitted reference differs from its saved
dense block16 endpoint by more than0.003 RMS, run all three at order16 and
use16 for every representative. If an order8 reference fails to fit within
budget, the same order16 branch is allowed, but no further order is tried.
If order16 still fails the accuracy screen, report it explicitly; compression
can still be measured against the matching full closure where fitted.
This permits27 representative fits and at most6 full-reference fits. Three
small deterministic integration checks and no more than three full-reference
tolerance checks (rtol1e-6 versus1e-5, error<=2e-4) are numerical validation,
not scientific replications. No result-dependent sampling seeds or tasks.

Use original residual-RMS activity clock, float64 adaptive RK45 with maximum
per-state-block scaled RMS error, rtol1e-5/atol1e-8, max_step10, and first
refined loss crossing.50sec training deadline/55sec interrupt,60sec total per
fit, one BLAS thread and serial scheduling. Save partial accepted states and
exclude them from fitted comparisons. No extensions or restarts. For closure
loss, record increases rather than assuming exact gradient-flow dissipation;
nonfinite states, clock below1, missed stops or solver-refinement error above
2e-4 invalidate clean interpretation. Circle grid2048 with nested1024 error
check<=1e-4. Tests verify materialized forward/transpose actions, canonical
outer velocities, initialization provenance and moment integral definitions.

Report RMS mean/range over the three subset draws; improvement fromq8 toq64
of more than1e-3 is descriptive evidence for useful compression on that task.
Smaller changes remain unresolved at this reporting scale. A finite-width,
finite-order endpoint experiment does not prove population or global-in-time
convergence. Root owns all new code, checks, plots and README; no subagent is
used. Source files stay in this study, output under
data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926.

### Moving-block result

Implemented [block_scalar_closure.py](block_scalar_closure.py): only the q
retained Gaussian blocks, first weights, readouts, history moments and clock
enter the autonomous RHS. Low-rank contractions transmit learned interactions
between all retained blocks, using both G and its actual transpose. Arbitrary
circle inputs are evaluated after training without adding passive training
states. The benchmark driver retains the original initial pool to construct
multiple comparisons; the saved individual model and its RHS do not need it.

All three order8 full references match the corresponding saved dense block16
models: circle RMS9.23e-8 (close pair),9.26e-7 (cluster),1.60e-7 (alternating5).
These include both history and numerical error. The order16 branch was not
needed or executed. The clustered reference at rtol1e-6 differs from rtol1e-5
by1.49e-7, well below the2e-4 numerical screen.

Completed exactly27 representative fits,3 full references and1 full-reference
numerical check in41.99sec. All31 reached MSE 0.01, with zero recorded loss
rises and clock>=1. Representative fits took0.138–3.250sec including final
circle evaluation and saving. Full references took1.443–7.959sec. No fit hit
a budget and no extra order, task, subset seed or continuation was run.

Mean absolute circle RMS over the three nested subset draws:

| Task | q8 vs full closure | q32 vs full closure | q64 vs full closure | q64 vs dense Gaussian |
|---|---:|---:|---:|---:|
| near_pair_sin9 | 0.012024 | 0.006462 | 0.003115 | 0.005202 |
| cluster_triple_cos9 | 0.050829 | 0.042707 | 0.031298 | 0.040484 |
| alternating5 | 0.047514 | 0.019208 | 0.007206 | 0.011179 |

The mean compression error decreases at both q increments on all three tasks,
with q8→64 improvements above the predeclared1e-3 threshold. Individual
subsets are not uniformly monotone: e.g. clustered subset1003 has errors
0.03983/0.07840/0.05124. Atq64, ranges are0.00130–0.00495 (close pair),
0.02112–0.05124 (cluster), and0.00435–0.01198 (alternating5). Clustered
predictors therefore remain sensitive to population reduction even when
half the blocks are retained. This is encouraging finite-population evidence
for the hierarchy, not evidence that aggressive compression is uniformly
accurate or a proof of its population rate.

Keeping q8/q32/q64 of128 blocks reduces both dynamic population storage and
fixed block coefficients by approximately16x/4x/2x; the single clock is
unchanged. Effective representative widths are128/512/1024. History order,
block size and training samples remain fixed. Total Gaussian discrepancy
also includes initialization replacement; it need not decrease monotonically
when sampling errors cancel or reinforce that difference. The present
reference is finite width2048 and every model has its own first-loss crossing;
there is no common-time trajectory or infinite-population validation here.

[check_block_scalar_closure.py](check_block_scalar_closure.py) passed exact
initialization provenance, materialized dense forward/transpose/adjoint
comparisons, canonical outer gradients, nonzero learned off-block interaction,
and independent defining Legendre-history integrals (max error2.25e-13).
Two small endpoint-integration checks differ by8.52e-9 circle RMS.
[analyze_block_scalar_closure.py](analyze_block_scalar_closure.py) verifies
all31 saved state hashes, exact initial subsets, source snapshots, baseline
hashes and scalar counts. Restoring each model from its retained G/vector
alone reproduces every saved circle prediction and training MSE exactly.
All stored RMS metrics recompute exactly; nested-grid changes<=1.33e-16.
No independent reviewer or promotion is claimed.

Reproduction commands (use fresh destinations for authorized repeats):

```
python studies/structured_full_rank_scalar_20260926/check_block_scalar_closure.py --output data/generated/structured_full_rank_scalar_20260926/moving_blocks_checks_20260926
python studies/structured_full_rank_scalar_20260926/run_block_scalar_closure.py --baseline data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_all_tasks_loss01_20260926 --output data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926
python studies/structured_full_rank_scalar_20260926/analyze_block_scalar_closure.py --output data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926
```

[Report](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926/report.md),
[figure](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926/moving_block_errors.png),
[audit](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926/audit.json).
The authorized first implementation/test is complete. No further experiment
is queued; identifying an efficient Gaussian-population scalar limit remains
separate from these finite-reference endpoint results.

### Remaining-task scalar validation, 2026-09-27 (precommitted)

The user authorized all remaining tasks. Continue the exact moving-block
construction, without changing its equations or rerunning the first three
tasks. Test pair_cos1, pair_cos3, triple_cos3, triple_mixed, broad_ridge6,
sharp_ridge8, alternating3, alternating9, multiscale12. Keep k16, P8,
width2048 reference (128 blocks), initialization seed 1, q8/32/64 and nested
subset streams1001/1002/1003. Run one full reference plus nine representative
fits per task: exactly90 trajectories. No P sweep, new seed, dense rerun,
restart or budget extension. The first campaign's solver refinement remains
the numerical calibration; saved-state reconstruction is checked again.

H1: the compression improvement observed on the first three tasks persists
on the remaining tasks. H0: it is task-specific or sampling fluctuations
dominate. Primary metric remains absolute RMS of circle prediction difference
against the full128-block closure, at each model's first MSE 0.01 crossing.
Report all three draws and means, including reversals; q8-to-q64 reduction
above0.001 is descriptive support, a rise above0.001 is contrary evidence,
and smaller differences are unresolved. These are endpoint observations,
not claims of global trajectory or population-limit convergence.

Same float64 RK45 tolerances1e-5/1e-8, first_step0.01, max_step10,
time_cap3000, 50sec training/55sec interrupt/60sec total per fit, serial
one-thread BLAS; maximum90min total fit budget, stop after90 trajectories.
Retain partial accepted states and exclude nonfitted endpoints from fitted
comparisons. All fitted-pair group sizes must be disclosed. Finite states,
clock>=1, saved MSE reproduction and nested2048/1024 circle RMS change<=1e-4
are validity gates; record loss rises. Full-reference discrepancies versus
fitted dense block16 above0.003 flag history error, without changing P.
Alternating9 lacks fitted dense Gaussian/block16 references: record their
status and leave those comparison metrics unavailable, even if the new full
closure fits. Do not use the old partial endpoints as fitted baselines.

Outputs: data/generated/structured_full_rank_scalar_20260926/
moving_blocks_remaining_20260927. Reuse the first campaign only for an
all12-task summary, explicitly recording source provenance. Root alone owns
the driver, generated checks/report/plots and README update.

### Remaining-task results (completed)

All90 new trajectories reached their first MSE 0.01 crossing:9 full
references and81 representative fits. Total campaign137.31sec. Representative
fits took0.086–12.487sec including circle evaluation and saving; the longest
full reference was alternating9 at26.998sec. No budget exits, retries,
extensions, new orders or dense reruns occurred. The core equations and
solver source hashes match the first campaign exactly.

Mean absolute circle prediction RMS, three subset draws per q:

| Remaining task | q8 vs full closure | q32 vs full closure | q64 vs full closure | q64 vs dense Gaussian |
|---|---:|---:|---:|---:|
| pair_cos1 | 0.024715 | 0.023359 | 0.009800 | 0.008558 |
| pair_cos3 | 0.007850 | 0.004045 | 0.003239 | 0.003998 |
| triple_cos3 | 0.016512 | 0.011467 | 0.006237 | 0.007976 |
| triple_mixed | 0.017164 | 0.006961 | 0.005048 | 0.004914 |
| broad_ridge6 | 0.007113 | 0.005195 | 0.002466 | 0.004000 |
| sharp_ridge8 | 0.002411 | 0.001153 | 0.000711 | 0.001156 |
| alternating3 | 0.025717 | 0.011023 | 0.006552 | 0.007523 |
| alternating9 | 0.129386 | 0.040042 | 0.033018 | unavailable |
| multiscale12 | 0.005277 | 0.001406 | 0.001037 | 0.004825 |

Every remaining task has a decreasing mean at both q increments and a
q8-to-q64 reduction above0.001. Including the first campaign, all12 mean
compression curves have this property. This supports the usefulness of this
particular moving-block reduction across the tested suite, not just the
original three tasks. It does not establish a rate from three q values or
guarantee monotonicity for individual subsets. The samples are three subset
draws of one initial population, not independent width2048 initializations.

Alternating9 remains demanding: atq64 its subset RMS range is
0.021982–0.054810 (mean0.033018); atq8 it is0.065018–0.234404.
Together with the original clustered-task q64 mean0.031298, this limits any
claim of uniformly accurate aggressive compression. q64 retains half the
population (2x reduction); q32 andq8 give4x and16x reductions respectively.

All eight new full references with fitted dense block16 controls differ
from them by at most4.53e-6 circle RMS. Thus those discrepancies are much
smaller than the observed representative errors. Alternating9 has no fitted
dense control: its P8 population-compression comparison is valid, but its
history error versus dense block16 and total discrepancy versus Gaussian
remain unmeasured. The old partial endpoints were not used or rerun.

Saved-state audit independently restored all121 models across both campaigns
and reproduced every stored circle prediction and training MSE exactly;
source/data hashes and exact initial subsets passed. New-run loss rises were
zero, clocks>=1, and nested-grid changes<=1.14e-15. The first campaign's
solver-refinement check is reused; there was no new tolerance sweep.
The comparison concerns separately stopped endpoints of a finite-width
reference, not common-time or infinite-population convergence.

Implementation and saved-result analysis:
[run_remaining_block_scalar.py](run_remaining_block_scalar.py),
[analyze_remaining_block_scalar.py](analyze_remaining_block_scalar.py).

```
python studies/structured_full_rank_scalar_20260926/run_remaining_block_scalar.py --baseline data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_all_tasks_loss01_20260926 --previous data/generated/structured_full_rank_scalar_20260926/moving_blocks_20260926 --output data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927
python studies/structured_full_rank_scalar_20260926/analyze_remaining_block_scalar.py --output data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927
```

[All-task report](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927/report.md),
[compression figure](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927/all_tasks_compression.png),
[Gaussian comparison figure](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927/all_tasks_gaussian.png),
[summary CSV with ranges](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927/all_tasks_summary.csv),
[audit](../../data/generated/structured_full_rank_scalar_20260926/moving_blocks_remaining_20260927/audit.json).
The all-task request is complete; no further experiments are queued.

## Genuine aggregate scalar closure: corrected target, 2026-09-27

The user explicitly distinguishes a fixed-size aggregate ODE in the width
limit from keeping a smaller population of moving neurons. The earlier
q-block experiments establish finite-reference subsampling performance;
they do not establish that stronger compression result. Calling those tests
an achieved elimination of population width was too strong. Their stored
numerical results remain valid for the comparisons actually performed.

The current request permits state size to depend only on Gaussian block
size k, sample count m and one approximation order P (circle input dimension
2 and depth fixed). It must not grow with width or elapsed time. Theory only
was carried out; no additional training campaign was authorized or run.

[AGGREGATE_SCALAR_CONSTRUCTION.md](AGGREGATE_SCALAR_CONSTRUCTION.md) specifies
a genuine Eulerian aggregate ODE. Its coordinates are masses in fixed cells
of the joint (G,w,c,A,B) block-state space, plus the shared clock. Conservative
nearest-neighbor mass flux is obtained from the original block velocity.
The output and forward/backward overlaps are finite weighted sums over
these masses. No representative neurons, original-width arrays or dense
matrix actions enter runtime, and test inputs need not enter training.

The derivation proves positivity, mass conservation, autonomous global
well-posedness of each finite aggregate ODE, finite-box convergence via a
compensated jump-process comparison, and Gaussian-tail removal via an
Osgood stability estimate. Exact Legendre integral identities bound every
history coordinate independently of memory order; the remaining stability
constants grow polynomially in that order before feedback amplification.

A deliberately excessive single-order schedule ties memory order to P and
prescribes box radius, seed cutoff and grid spacing using P alone. If J(P)
is the prescribed number of nodes per coordinate, the stored dynamic count is

    1 + J(P) ** [k*k + k*(3 + 2*m*P)].

For every fixed finite T, its aggregate output converges uniformly over
t in [0,T] and every input in the unit disk to the Gaussian-block population
memory closure at the matching order P. Fixed-memory-order refinement is
also covered. The state count never changes with elapsed time. This does
not assert a small uniform error over infinite training time at a fixed P.

The generic cell count is astronomically large. At k16,m3 and memory8 the
joint state dimension is1072 even before selecting a grid. This construction
therefore meets the mathematical width-independent aggregate requirement
but does NOT resolve efficient compression. Its proof also leaves separate
the memory-to-unrestricted-training and block-to-dense-Gaussian limits.

Root owns the construction and current README. Scoped internal analyses:
[AGGREGATE_TRANSPORT_AUDIT.md](AGGREGATE_TRANSPORT_AUDIT.md) derives the
Eulerian and Gaussian-tail estimates; [AGGREGATE_LABEL_ROUTE_AUDIT.md](AGGREGATE_LABEL_ROUTE_AUDIT.md)
examines Gaussian-label Galerkin as a possible alternative. The latter has
separate regularization and quadrature costs and is not a validated efficient
replacement. These are internal proof derivations and cross-checks, not
independent promotion reviews or established-book additions. No empirical
performance claim is made for either aggregate construction.

## Authorized first histogram experiment, 2026-09-27

The user requests one genuine aggregate-ODE candidate test and expansion
only if its circle RMS is good, with continuing reports. Full k16/H8
histograms are infeasible. The first diagnostic therefore explicitly uses
k1, memory H1, and one circle datum u=(1,0), y=1. This preserves two nonlinear
layers, feature/readout learning, moment feedback and unseen-input evaluation,
but does not validate inter-neuron mixing inside k16 blocks or multi-input
geometry. It is not counted as another test of the earlier k16 construction.

Exact symmetries reduce the one-input law to a five-axis histogram
(g,x,a,c,b): g and x are initially independent half-normal variables,
a=-A>=0, c>=0, b=B/L in[0,1]. First-weight motion is parallel to the training
input; its independent perpendicular Gaussian component remains frozen and
is integrated only during passive-circle queries. It must pass through both
nonlinearities in that query integral. The symmetry folding and B/L change
are exact; the finite histogram remains the extra approximation under test.

H1: a feasible fixed histogram gives circle RMS<=0.01 against a resolved
Gaussian-block population memory reference. H0: state-grid diffusion or
truncation prevents that accuracy at affordable resolutions. The reference
is deterministic Gaussian quadrature of the characteristic flow, used only
as a control; the tested solver evolves cell masses only, with no pruning,
moving representatives or reference feedback. All models start c=A=0.

Freeze axes g[0,5], x[0,6], a[0,3], c[0,4], b[0,1]. Use uniform nodes with
counts (9,17,9,17,9) and (13,25,13,25,13) in that axis order, giving210681
and1373125 scalar masses plus one clock. Initial g,x mass uses half-normal
CDF cells (upper tails placed at the last node); B/L=tanh(x) is deposited
between adjacent b nodes. Positive x,a,c velocities taper linearly from80%
of the upper bound to zero at the bound; b uses its naturally inward drift.
Record mass in the tapered region; above0.001 prevents a clean accuracy pass.

Integrate the autonomous mass ODE by positive conservative SSPRK2, CFL0.7,
first MSE 0.01 crossing with convex state interpolation, physical-time cap20.
Eight OpenMP threads, at most50sec training and60sec per complete trajectory;
save partial accepted states without restarts or extensions. Use1024 circle
angles and64-node Gauss-Hermite integration for the frozen perpendicular
coordinate; check nested512-angle RMS and32-vs64-node passive integration.
The passive quadrature discrepancy must be<=0.0005, and circle-grid RMS
change<=0.0001. Mass error<=1e-10 and minimum mass>=-1e-14 are validity gates.

Population reference uses folded48- and80-node Gaussian-Hermite seed rules
and RK45 rtol1e-9/atol1e-11. If their circle predictions differ by more than
0.0005, allow one128-node seed-rule check; unresolved reference differences
make the candidate result inconclusive. No finite random-width sample is
treated as the exact population. No dense Gaussian comparison is added here.

One fine-histogram CFL0.35 validation run is allowed if the fine model fits
and its provisional RMS<=0.025; its fitted-function difference from CFL0.7
must be<=0.002. A clean candidate pass requires both histogram resolutions
to fit, fine RMS<=0.01, no resolved worsening versus coarse (>0.002), and all
validity gates. A failure/inconclusive outcome stops the campaign. Only a
clean pass authorizes trying the nonparallel pair_cos1 and then pair_cos3,
still k1/H1, with separately frozen feasible grid details before execution;
the pair stage must not be replaced by rotations of the single-input task.
At most3 reference fits and3 histogram fits in this first stage; no extra
grid search. Initial engineering compilation and algebraic checks are not
training runs. Generated namespace: histogram_candidate_20260927.

Root owns the Python driver, reference, checks, report and current README.
The scoped histogram_feasibility agent owns histogram_one_input.cpp and its
feasibility note. No other study or old reference outputs are imported.

Execution amendment, disclosed before either histogram fit: the48/80/128
reference ladder completed but80-vs128 circle RMS was0.0006483, exceeding
the0.0005 reference gate. The initial driver stopped before testing the
requested construction. Preserve that failed check and original stop record.
To complete the user's requested candidate measurement, execute only the
two already specified coarse/fine histograms, explicitly as diagnostics
against an unresolved reference. Do not change the accuracy gate, add
reference fits, trigger the half-CFL branch, claim a clean pass, or expand
to additional tasks. This is a disclosed workflow amendment, not a
predeclared branch or successful validation. Run count remains within the
original first-stage budget; all earlier reference trajectories are reused.

First-candidate outcome: coarse/fine absolute circle RMS against GH128 was
0.030938/0.020779, with210682/1373126 dynamic scalars and0.54/4.75sec total
runtime. Both fitted MSE 0.01, but the0.01 accuracy target and0.001 taper-mass
gate failed. Maximum accepted-state taper mass was4.153%/1.519%; the reference
check also remained unresolved. This demonstrates a running genuine aggregate
ODE and passive input queries, not efficient validated compression. See
[candidate report](../../data/generated/structured_full_rank_scalar_20260926/histogram_candidate_20260927/report.md).

## User-directed breadth test, 2026-09-27

The user then explicitly prioritized distinct tasks over further refinement
of one case. This supersedes the previous conditional expansion restriction;
the failed first-candidate validation remains unchanged. The next campaign
is a bounded diagnostic screen, not a claim that the candidate passed.

Test the six existing two/three-input tasks pair_cos1, pair_cos3,
near_pair_sin9, triple_cos3, triple_mixed, and cluster_triple_cos9. Preserve
the genuine fixed-cell aggregate dynamics with k1/H1 and c=A=0. With multiple
nonparallel inputs both first-weight coordinates evolve, so the special
one-input reduction is not reused. Only the exact fixed-g sign folding is
retained. The axes are(g,wx,wy,c,A[1:m],B[1:m]/L), dimension4+2m. Full signed
joint distributions preserve current forward/backward and memory correlations.

Freeze bounds g[0,5], w[-4,4]^2,c[-4,4],A[-3,3]^m,b[-1,1]^m. Use
(5,9,9,9,5,5,5,5) for m2 (2278125 masses) and
(5,9,9,9,3,3,3,3,3,3) for m3 (2657205 masses). Initial g,w probability is
Gaussian CDF cell mass; c=A=0; deposit b=tanh(w.u) multilinearly. Outward
w,c,A drift tapers over the last20% of each signed bound. Use SSPRK2 CFL0.7,
training MSE 0.01, physical cap100, and50sec training ceiling per trajectory.
No grid search, no per-task tuning, no restarts/extensions. Evaluate1024
passive circle queries after each run and retain partially fitted endpoints.

The matched control is the same k1/H1 characteristic population law using
fixed tensor Gaussian seed quadrature. For each task run orders16 and24,
2048 and6912 folded seed atoms, rtol1e-7/atol1e-9/maxstep0.25 and the same
stopping criteria. These reference atoms are exclusively controls and never
enter the histogram RHS. Report their circle-function difference explicitly;
do not present the numerical reference as certified exact population truth.

H1: the aggregate screen attains circle RMS<=0.01 on more than the single
input case. H0: affordable fixed-cell resolution loses relevant correlations
or introduces excessive diffusion/truncation and misses that accuracy.
Primary metric is absolute fitted-circle RMS versus order24, no signal
normalization. Report loss, fitted status, time, state size and cutoff mass.
A clean per-task pass additionally needs both fits, reference16-vs24 RMS
<=0.005, circle-grid diagnostic<=0.0001, mass error<=1e-10, nonnegative
masses and maximum taper mass<=0.001. Unmet validity gates mean diagnostic
only; an unfitted endpoint is never called a fitted-function comparison.
This screen has no temporal-refinement branch and cannot establish a fully
resolved continuous-time error. All six tasks run regardless of earlier
accuracy failures, as requested. Total budget:18 trajectories, no further
branches, stop after all six or an implementation failure. Retain/reuse all
completed results; no reruns to make a better table. Output namespace
histogram_breadth_20260927. Scope remains k1/H1, not larger mixing blocks or
canonical dense Gaussian equivalence.

Breadth screen completed: exactly18 trajectories across all six tasks, no
restarts or extensions. Both population-reference quadratures fitted on
every task. Four genuine histograms fitted; two reached their50sec training
deadline and retained their last accepted state.

| Task | Histogram training MSE | Circle RMS vs GH24 | Histogram status |
|---|---:|---:|---|
| pair_cos1 |0.0100|0.030323|fitted|
| pair_cos3 |0.0100|0.048431|fitted|
| near_pair_sin9 |0.0100|0.125092|fitted|
| triple_cos3 |0.151792|0.208281|partial at deadline|
| triple_mixed |0.0100|0.011045|fitted|
| cluster_triple_cos9 |0.882702|0.628904|partial at deadline|

The two partial rows compare an unfinished histogram with a fitted reference
at a different physical time; they do not measure a fitted-function or
common-time approximation error. Fitted cases span0.0110–0.1251 absolute
circle RMS. All grids retained nonnegative masses and conserved mass within
8e-14. Reference16-vs24 discrepancies ranged0.00184–0.02287, and maximum
taper-zone masses ranged14.0%–32.2%; no case passed all screen gates. These
reference differences are sensitivity diagnostics, not certified error bars.
The m3 histogram uses coarser memory axes than m2 to keep state count feasible,
so sample count, geometry and resolution effects are not isolated.

This supports implementation correctness and queryability of a width-independent
aggregate ODE, but does not establish a practically accurate replacement at
these affordable grids. It does not rule out eventual histogram convergence
or other scalar representations. The stronger k16/dense-Gaussian target has
not been tested with this aggregate solver. No further runs are queued.

Implementation: [run_histogram_breadth.py](run_histogram_breadth.py),
[histogram_multi_input.cpp](histogram_multi_input.cpp),
[histogram_multi_reference.py](histogram_multi_reference.py).
Saved-data analysis: [analyze_histogram_breadth.py](analyze_histogram_breadth.py).
[Full report](../../data/generated/structured_full_rank_scalar_20260926/histogram_breadth_20260927/report.md),
[six-task plot](../../data/generated/structured_full_rank_scalar_20260926/histogram_breadth_20260927/histogram_breadth.png),
[numerical table](../../data/generated/structured_full_rank_scalar_20260926/histogram_breadth_20260927/summary.csv).
