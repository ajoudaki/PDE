# Stochastic escape and fitting in the p=1 population closure

## Current checkpoint: 2026-09-19

The strongest current result is an internally checked, unconditional
**no-suboptimal-local-minimum theorem** for the exact odd canonical p=1
population state space in its physical L2/L2/Frobenius topology. Every
local minimum attains the exact architectural loss floor for arbitrary
finite weighted sphere data in d>=2, including linearly dependent inputs.
For consistent signed labels this floor is zero. See
[no_bad_local_minima.md](no_bad_local_minima.md) for the complete proof.
Every neighborhood of a suboptimal equilibrium contains initial states
whose exact GF cannot converge to that equilibrium, because their loss
starts strictly lower. This excludes a full local point basin, not all
positive-measure or one-sided basins.

The stronger proposed criterion based on a descending fixed straight
direction is **false**. An exactly constructed ambient equilibrium has
loss one, every nonflat fixed direction has positive quadratic leading
coefficient, and other directions are identically flat. It nevertheless
has smaller-loss states arbitrarily close in the physical norm. The
balanced-label variant needs at most 26 nonparallel/nonantipodal samples
in dimension three. See
[straight_line_geometry_attempt.md](straight_line_geometry_attempt.md)
and its informed internal review. The second-directional quadratic form
is not a Frechet Hessian; small-set population variations expose the
failure of a uniform second-order expansion.

No canonical trajectory is proved to reach this example. Neither result
proves global GF/SGD fitting, zero-measure bad basins, or a training rate.
The exact landscape distinction is resolved; the stochastic-dynamics
bridge remains open. No promotion or numerical experiment is claimed.

## Question and scientific boundary

Investigate whether fresh gradient perturbations or iid minibatches,
especially batches of size three, remove positive-loss traps and yield
zero-loss learning for finite data in the exact p=1 population closure.
This changes the optimizer and is a new research direction. Repository
inputs are established docs/ and code/ only, plus this study's own files.
No unpromoted proof, construction, or result from another study is an
input. References in the user's question are motivation to rederive or
test claims, not imported theorems.

Keep canonical tanh, Gaussian-derived correlated frozen marks, dictionary
normalization, initialization w=g,c=0,M=D, complete trainable matrix and
actual transpose, physical population-L2/Frobenius metric, and unhalved
probability-weighted square loss. The target is the closure itself,
not a finite-width neural-network or closure-order limit. Physical
inputs x have norm sqrt(d). All population expectations remain exact.

Distinguish discrete iid minibatch SGD, any stated continuous-time
stochastic process, and artificial additive field noise. The noise law,
step/temperature schedule, state topology and almost-sure/expected
conclusions must be explicit. Escape from one neighborhood, exclusion of
point-convergent bad limits, and actual loss convergence are separate.
An invariant/noise-degenerate state is not a canonical initialized failure.
Fresh minibatches at vanishing step do not automatically create a
nonvanishing diffusion in physical time.

## Current authorized work and ownership

Lead owns this README, integration and lead proof files. Independent
fresh scoped routes used the complete established p=1 chapter and
NOTATION.md, and their explicit prompt assignments only. The minibatch
route owns sgd_geometry.md; the additive-noise route owns noise_escape.md.
Both froze before comparison. The lead separately derived the four-input
example and local fitting theorem. The minibatch author's later mixed-label
strengthening is explicitly informed by lead feedback after the freeze.
No route read another route before freezing.
Theory only in this round. No training simulation or parameter sweep.
No modifications to maintained docs/code, staging, commit or promotion.

Startup read current AGENTS.md and workflow Part 1, docs/README.md and
NOTATION.md, investigate-conjectures and solve-math-rigorously skills and
required research-contract, evidence-ledger and adversarial-audit
references. Exact model source: docs/observable_p1.md, supplemented only
by explicitly selected complete canonical closure sections as needed.

HEAD at startup: 019e3630237e33f58b9636c0aa67a039bebf0182. Index empty.
Unrelated modified files and untracked study directories preserved.

## Results and scientific scope

The integrated report is [RESULTS.md](RESULTS.md). It separates exact
identities, explicit ambient examples, proved local stochastic fitting,
and the still-open canonical initialization question.

The central open question is actual all-time canonical minibatch fitting
for general compatible finite data. The following complete candidates
give a sharper positive/negative division.

* [local_minibatch_fitting.md](local_minibatch_fitting.md): explicit exact
  fit for every finite odd-compatible sphere dataset, allowing arbitrary
  sample count and linear dependencies; an explicit open local starting
  region for iid constant-step population SGD, any batch size, gives
  finite zero-loss state convergence with probability at least 1-delta.
  Conditional expected loss on its successful event decays geometrically.
  All constants and regions are defined from the data and canonical
  Gaussian expectations. Canonical entry into these regions is unproved.
* [four_input_noise_geometry.md](four_input_noise_geometry.md): a fresh
  balanced four-input nonparallel, nonantipodal example with exact fits,
  a rank-one PSD bad Hessian and explicit cubic descent. At that bad state
  batch-three noise acts only in the positive-curvature readout direction.
  Every first step raises full loss, but every second step moves both
  hidden trainable blocks under the stated step bound. These are exact
  finite-step statements about an ambient state, not canonical failure.
* [sgd_geometry.md](sgd_geometry.md): exact physical sample gradients and
  covariance C_B=C_1/B, full common-sample-stationarity classification,
  almost-sure local exit and point-limit exclusion for nonvanishing
  steps, and the precise weaker consequence for square-summable steps.
  Its mixed +1/-1 three-input example is exactly fittable but has an
  absorbing cubic bad state with all sample gradients zero. Canonical
  reachability of that state is not claimed.
* [noise_escape.md](noise_escape.md): coherent Gaussian kicks in a cubic
  subspace, additive trace-class Hilbert diffusion and local ball exit,
  distinct independent-population-mark noise with exact cancellation,
  and the fixed-noise obstruction near finite fitting states. Loss
  convergence is not inferred from spatial exit. The noise semantics
  and noncanonical counterexample starts are explicit.

Fresh isolated reviewers use complete frozen scientific candidates and
canonical definitions only. Their outputs are
[review_stochastic.md](review_stochastic.md), for the four-input example
and separately supplied local fitting theorem, and
[review_noise_routes.md](review_noise_routes.md), for the two independent
routes. Reviews are internal mathematical checks, not promotion. Final
versions and disposition are now frozen: both reports PASS their exact
scopes. The first reviewed all 915 scientific input lines across the
complete canonical definitions and both lead candidates; the second
reviewed all 1472 scientific input lines across the same definitions and
the two independent routes, including the binary-label extension and
final corrections. The lead read both complete reports and all complete
proofs, and checked the integrated report against them.

Final review hashes:

* review_stochastic.md:
  `9b07ccab17038bc7694487f6c31d0fa02ba626ec6738f6f82ec385e7bf82ee73`
* review_noise_routes.md:
  `3605e808cc4f2b79f1f757ed0a2a028cb66ad340ec2d16aedb83aeca10455adb`

The general-data local fitting proof has SHA256
`28ec016758d0cbfbf3316652b00ac2b6e70f504ba5075537ac2a8ce219daebd6`;
the integrated report has SHA256
`ca8d3f41d54c0d19269e01956dc434340881f07fc8a30fbdd69ca70886f50b57`.
All other final input hashes are recorded in the complete reviews.
The reviewers found two localized wording/proof mismatches, both corrected
and rechecked: summable-step confinement proves positive loss without
proving a nonstationary limit, and a nonzero label first moment proves
cubic descent without proving representability for arbitrary data.
Representability is separately constructed in the stated examples and
in the general local fitting theorem. Original frozen versions and
correction provenance remain recorded in the respective route files.
No required mathematical correction remains open within the claimed
scopes. Control-byte and display-delimiter checks passed on every study
Markdown file. No numerical validation is substituted for the proofs.

The noise author disclosed that a metadata-only agent-list query included
an unrelated completed summary. No source from that study was retrieved
or used. Its mathematical packet is independently reviewed from scratch.
The author froze its route before seeing this study's other arguments.

No theorem for three training examples can simply be applied successively
to freshly drawn triples: each update uses the current state, and the
objective and sampled vector field change. Minibatch noise has rank at
most the sample count minus one and need not excite a cubic direction.
Persistent additive noise also disturbs fitting states; annealing changes
the required escape estimates. The unproved global bridge is avoidance
of reachable collapsed sample-stationary sets and adverse behavior at
infinity, together with entry from (g,0,D) into a successful fitting region.

No simulation was run. The study crossed midnight into 2026-09-19; its
creation-date namespace is retained. Shared book/code and Git index remain
untouched, with no staging, commit or promotion.

## Continuation: which bad states actually have cubic descent?

The user's next question narrows the stochastic escape argument to its
landscape premise: whether all the bad equilibria have a nonzero cubic
descending direction. This is a continuation and validation of the same
investigation. The two specifically constructed cubic saddles retain their
proofs, but the common-sample-stationary family contains higher-order saddles.

Lead candidate [cubic_and_higher_descent.md](cubic_and_higher_descent.md)
classifies the quadratic/cubic behavior at every state (w,c,M)=(0,0,M_*).
Every cubic coefficient vanishes when the label-weighted first input moment
vanishes. The same balanced four-point data admit a quartic descending
direction at (0,0,D) and a quintic one at (0,0,0), with no cubic directions.
A further complete candidate proves finite-order straight-line descent at
every such collapsed state for arbitrary finite nonparallel/nonantipodal
sphere data with nonzero labels: some even order at most 2m when M_* is
nonzero, and some odd order at most 4m-1 when M_*=0. This is not a
classification of all p=1 equilibria or a canonical reachability theorem.

Fresh independent scoped route `/root/cubic_order_check`, with no inherited
conversation, read complete canonical definitions and this study's two
original example/SGD files only. It independently proved the exact cubic
criterion at (0,0,0) and a fifth-order counterexample, in
[cubic_order_independent.md](cubic_order_independent.md). It froze at SHA256
`4f1f42cf2550d8503bd27ac6419c6d70d95c400968665e0d7ffca9b13394a66e`
before comparison. The lead read the complete result and checked its bounds
and signs; its origin criterion and higher-order example agree with the
lead's separate argument. This is independent derivation, not isolated review.

The lead candidate froze at SHA256
`d469d54a466fb60464f6c3c9e79d831718f333b09e98de20a9d7ff7fc78b9fe1`.
Fresh isolated reviewer `/root/review_cubic_higher` received only this full
candidate and the complete canonical p=1/notation sources; its report path
is [review_cubic_higher.md](review_cubic_higher.md). Its full review passed
all substantive claims and required one wording correction: the Hessian
evaluation is twice the quadratic Taylor coefficient. The lead read the
complete review, applied that correction, and appended the review-verified
unfolded cancellation note and the iff cubic criterion for all reduced
collapsed matrices. Final lead candidate SHA256:
`6c88051f539e1e3c7603be122c8d9fb5538e37b02db26513188ec645cbf720b4`.
Review SHA256:
`b873d8de14e8dd8cc1669e0262647a3401ec86de38d0a11ade90eb94728acb54`.
Earlier proof files remain unchanged. No simulation, shared-source edit,
staging, commit, or promotion is part of this continuation.

## Further continuation: genuine bad local minima

The user broadened the local-descent premise to equilibria with only
positive even leading terms and exactly flat directions, then explicitly
authorized continued work. The literal straight-line condition is stronger
than local minimality: a curved path can descend when every straight line
has positive leading order. This distinction is retained explicitly.

At its first freeze, lead candidate [no_bad_local_minima.md](no_bad_local_minima.md) claimed that
every local minimum in the odd canonical p=1 physical Hilbert state space
has zero loss, for arbitrary finite pairwise nonparallel/nonantipodal
sphere inputs, positive weights and binary labels. No m<=d or linear
independence condition is imposed. It uses paired changes on small
population subsets, matrix stationarity, and exactly flat readout
directions. The proof excludes genuine local minima, not every possible
straight-line Taylor pattern, and does not prove stochastic fitting.
Frozen candidate SHA256:
`702ef38dbb7c03c5d09979d7247f3c9eab1b35da30f98d9159bdf948b2cdedb4`.

Fresh independent route `/root/all_bad_local_geometry` initially had only complete
canonical p=1/notation sources and the neutral general-equilibrium
assignment; it had not received the lead method or candidate. Its assigned
file is `general_bad_geometry_route.md`. An attempt to spawn a fresh
isolated reviewer was blocked by the agent thread limit. Therefore the
earlier independent origin-route agent `/root/cubic_order_check` now has
an explicitly informed internal review assignment for the complete frozen
new proof and canonical definitions only, to write
`review_no_bad_local_minima.md`. Its prior context is disclosed; it is not
an isolated promotion review. The completed informed review PASS found no
mathematical correction in the central theorem. The lead read it completely
and applied its three presentation/self-containment requests: clarify the
straight-direction quantifier, include the review's direct exact-fit
construction, and record the actual review provenance. Final theorem file:
`42682d778b39f568f878f221348bfcd1f8fc7d8af139d7107343dae4d544f29c`.
Review:
`9f1796c95b2fab5a80d74df046ec4312fe394f628dfa64cd856f6511629c453c`.
This is now an internally checked no-bad-local-minimum theorem, not a
promotion or initialized-convergence result.

The independent general route froze before comparison at
`7c88c617b0ace8bd59332fa0e124a4fb2c77cb5b88790b9410cb50f1aa877a37`.
The lead read its complete 466-line report. It reaches the same theorem
using a different first-layer argument, including a separately proved
equal-norm ridge lemma. That additional lemma is not a dependency of the
lead proof and has not received a separate isolated review. After freezing,
the route was told the lead also obtained the theorem using matrix
stationarity plus oddness, and received a bounded follow-up to investigate
the remaining literal straight-line claim. That follow-up is therefore
post-comparison work, assigned to `straight_line_geometry_attempt.md`.

Checks of the new reports found no control-byte corruption or unpaired
display-math delimiters. No numerical experiment was run. The remaining
substantive gaps at that checkpoint were a fixed descending straight
direction at every bad equilibrium (or a p=1 counterexample), and the
dynamical connection from local descent to actual stochastic avoidance
and fitting. No conditional compactness or future-trajectory estimate
was being asserted as proved.

The reviewer subsequently verified the real-label extension and exact
grouping of duplicate/antipodal observations. The main theorem now says
that every local minimum attains the exact architectural floor for
arbitrary finite weighted sphere data. The floor is the within-group
weighted variance of signed labels after grouping inputs modulo sign.
It is zero exactly for consistent signed labels. This includes all finite
nonparallel datasets and removes any generic-position requirement from
the global-minimum formulation. Updated theorem file SHA256:
`a535ba6f0aacbb35a946937dc6c3d4e5317d73a70f4682459e36b61917ef2f43`.
Supplemented informed review SHA256:
`9dd2903a6f658f101f322ac939ee4624f06e07800029ec56347a71304d3ebfc2`.
The original review prefix is preserved and its original hash remains
recorded above. The lead read the complete supplement before integration.

The focused straight-line refinement then produced a concrete p=1
counterexample candidate in
[straight_line_geometry_attempt.md](straight_line_geometry_attempt.md),
frozen at
`51279663fe402d16e979b9fa9af646453ac307707563f501c164f89ee9a703ec`.
It uses at most 24 nonparallel/nonantipodal normalized directions in d=3,
mixed binary labels, and exactly the canonical carriers. Its proposed
equilibrium has loss one; all directions with a nonzero lower-weight
component have strictly positive quadratic loss coefficient, while the
remaining directions are exactly flat. A separate paired small-set
variation decreases loss. The construction uses a proved 12-function
interpolation system, not numerical search. The separate informed review
[review_straight_line_counterexample.md](review_straight_line_counterexample.md)
passed its complete construction and additionally checked a balanced-label
version with at most 26 inputs. Its SHA256 is
`82214ae2329e03bf5662709fe91ead6cc3c98a879ae96b88cff8c1b7fba1fc24`.
The lead read the complete review. The author incorporated the physical
input scaling x=sqrt(3)u, the complete noncoercivity argument, the proof
that no Frechet Hessian exists, and the separately checked balanced
extension. The lead then read the complete revised 740-line proof and
checked those additions against the review. The positive directional form
must not be identified with an
unrestricted Frechet Hilbert Hessian. No initialized reachability claim
is made. This disproves the universal fixed-straight-line descent claim
that was still open at the earlier checkpoint above.

The no-local-minimum review also checked the direct GF consequence recorded
at this README's current checkpoint. Its Supplement 2 preserves all earlier
report bytes and proves that no suboptimal equilibrium's point basin can
contain a neighborhood of that equilibrium. The lead read the supplement
completely and inserted its argument in the main proof. Earlier proof and
review hashes above identify their respective checkpoints, not the final
files. Current completed proof/report hashes are:

* no_bad_local_minima.md:
  `e852a52f7a9af83daa570e021170b857e6cc7e309c5549cbdc2ac72ef441f8ed`
* review_no_bad_local_minima.md:
  `3751b9583c69b232f3f0910ceddc19eac6f1766505738b3d8782df59df8aeb33`
* straight_line_geometry_attempt.md:
  `bb0aa0900b17069db3ae469207493328bdcacd93e7a643a64610dd197437cacf`
* review_straight_line_counterexample.md:
  `82214ae2329e03bf5662709fe91ead6cc3c98a879ae96b88cff8c1b7fba1fc24`

The mathematical checking consisted of complete proof reading, separate
derivations of the local-minimum result before comparison, and the disclosed
informed reviews and supplements. No empirical evidence is used. The
current bounded landscape investigation is complete: absence of suboptimal
local minima is proved, while the universal fixed-line descent claim is
disproved. A further stochastic-fitting argument would still have to show
that the chosen noise law can exploit nearby descent and control behavior
at infinity; neither obligation is replaced by these landscape results.
The earlier stochastic reports remain intact with their original scopes.
Final structural checks covered all 16 study Markdown artifacts: no control
bytes, unmatched display delimiters, or missing local Markdown links were
found. The four current proof/report hashes above were rechecked. These
are document checks, not substitutes for the mathematical reviews. The
shared index remains empty; no maintained source, commit, or promotion was
changed by this work.
