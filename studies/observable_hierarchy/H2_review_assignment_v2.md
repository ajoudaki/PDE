# Neutral assignment: complete adversarial C-H2 review, version 2

You are an independent isolated scientific reviewer of a proposed mathematical
and software addition. You did not author, assemble or select it. Start with
no inherited project history. Do not read study history, route reports,
internal verdicts, another reviewer's findings, chats, Git history, or other
studies. Your assignment, the exact files in H2_review_inputs_v2.json, and
required skills are your complete input scope. The manifest distinguishes
complete-read scientific inputs from correspondence-only full source files.
Report any missing dependency before fetching anything further. The supervisor
must supply missing scientific inputs in a new complete packet.

Read both required skills yourself: solve-math-rigorously and
investigate-conjectures, including their applicable required references. The
full root instructions, workflow, notation contract and book/code guides are
included in H2_guides_v1.md. Independent-review scope replaces ordinary author
startup: do not read the study README or other author notes. Do not modify
inputs. Write only your assigned H2_review_v2_a.md or H2_review_v2_b.md and
scratch in the correspondingly named study generated directory. Do not commit.

Read every scientific line in the complete-read packet, including proofs,
dependency bodies, implementation, tests, numerical limitations and recipes.
Repair truncated reads. Inspect the source-correspondence checks against their
specified full source files; you need not audit their unreferenced complement.
Keep the two reviews isolated. No earlier verdict is supplied or relevant.

## Required mathematical result

Construct increasing finite autonomous population systems for the canonical
bias-free two-hidden-layer tanh model

  f_n(x) = (W3)^T tanh(W2 tanh(W1 x/sqrt(2)))/n.

Independent stored Gaussian variances are (1,1/n,1/n^2); mobilities are
(n,1,n); residual is f-y; physical GF uses unhalved mean-square loss.
Finite-network invocations must preserve the actual random finite readout,
both orientations, and reuse of the same Gaussian middle action.

For each fixed Y>=1 the data laws lie on sqrt(2) S1 × [-Y,Y], measured with
normalized-input-plus-label transport cost, in one fixed positive neighborhood
of the equally weighted law at (sqrt(2)e1,+1) and (sqrt(2)e2,-1). Choose one
fixed positive radius and one 0<T<=1/200, independent of order. The family must
include nonorthogonal and nonatomic laws and share a positive activity time
at which the paired displacements of both hidden representations are nonzero.

At each order specify all retained current populations, same-population joint
statistics, auxiliary coordinates, mark domains and fixed inputs, including
every finite matrix and all correlation information. Initialize explicitly
from canonical finite Gaussian programs and permitted fixed inputs. Give a
closed autonomous vector field and observation maps, well-posedness through T,
and restart from its own reached state using only saved current information.
The number of field types and all coordinate/mark dimensions must be finite;
they may depend on order and the declared horizon, but not on elapsed time,
update count or numerical time mesh. Finite population fields and explicitly
defined integrals are allowed; practical quadrature costs belong to C-H3.

The operational vector field cannot query omitted hierarchy levels, unresolved
cutoff limits, an arbitrary-vector Gaussian-action oracle or the exact target
trajectory. Schedules must use admissible information. Excluded substitutes:
representative dense neural network, full parameter-space density, stored
history, preallocated trajectory replay, fitted surrogate, or a mere coordinate
change of the original trainable middle matrix. Finite matrices of explicit
observable coefficients/contractions are allowed when their role and provenance
are proved. Test this boundary substantively.

One common construction must satisfy, for every separately fixed admitted mu,

  sup_{0<=t<=T} sup_{x in sqrt(2)S1}|f_mu,N(t,x)-f_mu(t,x)| -> 0.

For every separately fixed admissible finite C-H1 same-layer joint observation
tuple, reconstruct and prove convergence uniformly in t in its declared W2
sense, including paired initial/current hidden observations, both action
directions, needed second moments and quadratic contractions. No uniform rate
over all laws is required. The limit must be the actual canonical nonlinear GF;
matching-realization uniqueness for reached complete hierarchies is insufficient
to identify arbitrary formal solutions. Any infinite-hierarchy route needs
admissibility and dynamic identification, beyond static realizability.

An explicit qualitative convergence theorem can suffice. An estimate conditional
on an unproved small tail, correct finite coefficients, or numerical agreement
cannot. Do not assume temporal analyticity, moment determinacy, positive
Stieltjes representation, or unrestricted same-norm product/derivative bounds.
The supplied obstruction sections state the exact established boundaries.
Equations must arise from current-observable dynamics and make sense beyond
the certified family wherever their ingredients remain defined.

## Required prototype and permitted checks

The concrete code must expose retained state, canonical finite-program
initialization, finite autonomous evolution rule, and observation maps. Audit
the Gaussian producer itself: uncentered input Grams, frozen named-source
response derivatives, correlated/singular sources, both orientations and reuse.
Check model conventions, coefficient-gradient metric, transpose contractions,
joint statistics, saved-state completeness, ridge and quadrature semantics.
The mathematical exact-real theorem and the floating quadrature prototype
must be clearly separated. A prototype need not have useful practical accuracy
or certified numerical cost; it must disclose unsupported ranges and errors.

Only deterministic static checks are authorized. No training trajectories,
training experiments, empirical campaigns, accuracy exploration or time-40
solver. Existing tests use prescribed states, algebraic finite differences,
analytic Gaussian identities and one algebraic update to test restart. You may
add bounded static adversarial checks in your own scratch without modifying
the frozen code. Run the supplied tests and source-correspondence check yourself;
record exact commands, cwd, environment, exits and outputs. Inspect the supplied
standalone assembly recipe and API examples, including relocation of the test
import. Static test success is not proof of the qualitative convergence theorem.

From /home/amir/Codes/PDE, run the tests with PYTHONDONTWRITEBYTECODE=1,
OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and H2_TEST_SCRATCH set to your own
assigned generated directory:

  python -B studies/observable_hierarchy/H2_test_prototype.py
  python -B studies/observable_hierarchy/H2_check_documents.py

You may assemble a fresh edition below your own generated directory using
H2_assemble_edition_v2.py --output PATH, then run its new test with PYTHONPATH
pointing only to that edition's code. Execute the new code-guide example there.
The full prototype notes refer to the earlier candidate filename for provenance;
the complete proposed scientific content to audit is H2_proposed_section_v1.md,
with its full listed dependencies. No author-history file is needed.

## Adversarial obligations and final report

Re-derive nontrivial steps. Test density of the concrete dictionary, increasing
orders, all dimensions, Gaussian initialization, filter identities, strong versus
operator-norm approximation, invariance on the actual initialized carrier,
well-posedness and restart, energy bounds, source decay, reference-tail use,
comparison constants and limit order, bounded products/powers and joint W2.
Audit dependence on N, mu, T and the law radius. Check canonical finite-network
identification, retained readout and physical-loss factors. Do not turn
compactness into uniqueness or assume a small error source without proof.

Return a complete original report, with:

- Your identity, isolation statement, actual input scope, exact hashes and
  complete read coverage, including every dependency body and repaired read.
- Actual adversarial derivations, counterexample attempts, boundary cases,
  commands, deterministic outcomes and limits of those checks.
- Separate verdicts for finite closure/nonvacuity, initialization, well-posedness
  and restart, convergence and dynamic identification, joint observations,
  activity/family, code producer/RHS/maps, reusable API and numerical limitations.
- All unresolved objections and whether each requires correction. Distinguish
  optional editorial suggestions from required changes. A required correction
  blocks acceptance and leads to a new frozen packet and two new complete reviews.
- A final overall PASS only if every required claim is proved at the stated
  scope, code claims are supported, and all complete-reading obligations are
  finished. Otherwise state the exact missing implication or defect.

Do not infer approval from any helper or prior status. This review is separate
from the later independent integration review and the user's promotion approval.
