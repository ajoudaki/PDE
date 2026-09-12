# Observable hierarchy — milestone C-H1

**C-H1 promoted with user approval.** The exact reviewed theorem is established
in `docs/global_nonlinear.md` C.4.7.8, and `docs/README.md` records its scope.
Two fresh complete scientific reviews and the independent integration review
pass. Approval and final correspondence are retained in
[promotion_v3.md](promotion_v3.md).
Promotion commit: `48555cc76d52619d3a1927aef4739c7fdb928512`.

The target is an exact, predictively sufficient current observable hierarchy
for canonical two-hidden-layer tanh population physical gradient flow, with
stored Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual `f-y`
and unhalved mean-square loss. The law family is a fixed positive Wasserstein
neighborhood of the opposite-label orthogonal reference on
`sqrt(2) S^1 × [-Y,Y]`; it must admit correlated and nonatomic laws. The positive
time interval and law neighborhood must not shrink with hierarchy order.

Required results: finite-type nested observable populations with full same-layer
joint information and Gaussian initialization; exact finite-dependency weak or
strong evolution at each separately fixed level; and predictive sufficiency at
precisely specified realizable reached restarts. Finite closures, convergence
rates and solver cost belong to C-H2 and later milestones. No training experiments
are authorized. Deterministic mathematical checks are allowed.

Finite states must not contain or query a raw dense operator, full parameter law,
elapsed-time history, or future data. Explicit current action observations are
allowed; the complete hierarchy may determine the dynamically relevant action.
Neither moment determinacy nor temporal analyticity is assumed.

## Ownership and inputs

- Coordinator `/root`: README, main proof, dependency packet, review assignments,
  promotion preparation, and the only Git writer for this study.
- `/root/route_observable`: `route_observable.md`, independent prompt-only route.
- `/root/route_weak`: `route_weak.md`, independent prompt-only route.
- Generated products and scratch: `data/generated/observable_hierarchy/`.

Both exploratory agents receive self-contained model equations and the common
representation contract, no other route's argument and no project history.
They read the required mathematical skills. Their scoped inputs replace ordinary
author startup. Other studies and their unpromoted findings are excluded.

Established inputs being read: `docs/README.md`, `docs/NOTATION.md`, population
equations and Gaussian action/adjoint construction in `docs/global_nonlinear.md`,
C.4.7 flow/restart and C.4.8.1 source calculus with relevant complete dependencies,
and the obstructions in `docs/gaussian_calculus.md` §§6 and 10.

## Checks and next action

Initial HEAD: `dbc4ffda9a57b063dfd2a6895621af554d06157b`; index initially empty.
Concurrent changes outside this study were observed and are preserved. Git
transactions use the shared nonblocking `pde-writer.lock` and explicit owned paths.

The promoted source is [candidate_v3.md](candidate_v3.md), the exact
approved C.4.7.8 subsection. Earlier versions are retained. It uses a finite
typed alphabet and finite-dimensional scalar/input
marks, joint populations, and a weak reverse-adjoint compiler whose cutoff limit
stays inside a fixed higher level. The all-order joint state reconstructs reducing
observable spaces; a restarted Euler comparison supplies invariance, and transport
plus one-reference uniqueness gives reached restart for matching realizations.

The prompt-only attempts are [route_observable.md](route_observable.md) and
[route_weak.md](route_weak.md). They remain partial for their original inputs.
Their source/restart gaps are supplied in the assembled candidate, and their
integrability and representation objections remain part of the audit.

Complete selected established dependency proofs are frozen in
[dependencies_v1.md](dependencies_v1.md); source hashes are in
[source_hashes_v1.json](source_hashes_v1.json). The parent read the complete
relevant source chain, C.4.8.1 source calculus, and the designated obstruction
sections, without importing other studies. The reference certificate and a
static deterministic three-way identity check passed; see
[checks_and_corrections.md](checks_and_corrections.md) for commands, outputs,
corrections, limitations and generated locations.

The two scoped internal audits are [internal_weak_v1.md](internal_weak_v1.md)
and [internal_representation_v1.md](internal_representation_v1.md); their complete
reports retain source-verification limitations. The independent nonauthor
selector accepted narrow assembly; see [selection_v1.md](selection_v1.md).
The exact guide proposal is [README_proposed_v3.md](README_proposed_v3.md).

Fresh isolated reviewers `/root/review_v3_a` and `/root/review_v3_b` received only
the [neutral assignment](review_assignment_v3.md), its frozen full inputs and
required skills. [review_inputs_v3.json](review_inputs_v3.json) records hashes
and author/assembler identities. They received no prior findings. The standalone
edition is generated by [assemble_edition_v3.py](assemble_edition_v3.py) under
`data/generated/observable_hierarchy/edition_v3/`; it edits no live book file.

The original complete reports are [review_v3_a.md](review_v3_a.md),
[review_v3_b.md](review_v3_b.md), and [integration_v3.md](integration_v3.md).
All are PASS with no required correction. The parent read them completely and
verified input/output hashes, complete source extraction, execution status,
isolation and read coverage. Both scientific reviewers independently reran the
static identity and exact rational certificate; the integration reviewer reran
both from standalone copied source in Python isolated mode. Full acceptance
provenance and optional editorial notes are in
[review_acceptance_v3.json](review_acceptance_v3.json). All frozen scientific
inputs remain unchanged. The two approved live document hashes now match the
reviewed edition; all other dependency hashes are unchanged.

The theorem fixes `T0=1/200` and one positive law ball independently of level.
It provides Gaussian initialization, exact finite upward weak evolution using
the explicit within-level cutoff limit, and complete-hierarchy predictive
sufficiency/reached restart for matching realizations under the reference law.
Both hidden layers move and remain nonaffine at one common positive time.
Finite levels are marked families of laws, not finite scalar compression.

The user approved the exact [promotion proposal](promotion_proposal_v3.md).
The approved C.4.7.8 and guide changes are applied without scientific alteration.
[check_promoted_v3.py](check_promoted_v3.py) verifies the actual live mapping,
dependencies, links and equation definitions and reruns the two static checks
in a fresh generated directory. It passed, with outputs identical to the
reviewed edition. Use this checker after promotion; the frozen assembly recipe
deliberately expects pre-promotion source hashes.

This milestone is complete. C-H2 finite autonomous closure and its convergence
remain open, as do effective cutoff, quadrature and solver costs. No C-H2
campaign or training experiment has been started, and no maintained code changed.

## C-H2 continuation — 2026-09-12

The user has now authorized theoretical work on a convergent finite autonomous
closure, a minimal executable prototype, static deterministic checks, isolated
research routes and independent review. No training experiments are authorized.
The frozen C-H1 package above is preserved. Its candidate is byte-identical to
the maintained C.4.7.8 subsection (verified at this continuation's startup).

Current ownership: coordinator `/root` in task
`01a0966c-d650-7512-91e9-5fd0298c2ad4` owns new `H2_*` coordinator files and
this appended README section, and is the only Git writer for this continuation.
Fresh isolated route agents own only `H2_route_prompt.md`,
`H2_route_hierarchy.md`, and `H2_route_regularized.md`, respectively. They do
not read one another's approaches before their first candidates are frozen.
The first and third receive self-contained scientific prompts only; the second
receives the frozen C-H1 candidate/dependencies, notation and designated
established obstruction sections. No other studies are scientific inputs.
Generated output stays under `data/generated/observable_hierarchy/H2_*/`.

Startup HEAD: `d1f808a56f4b3ea010a42f1fc1f6bc165d383aa4`; index empty.
Concurrent changes outside this study are preserved. All short Git transactions
use the common nonblocking `pde-writer.lock` and explicit owned paths.

The fixed research contract and route registry are in
[H2_contract.md](H2_contract.md). The requested C-H2 theorem now has an
internally checked construction; fresh independent gates are still pending.

C-H2 checkpoint: all three isolated first routes are frozen and retained in
[H2_route_prompt.md](H2_route_prompt.md),
[H2_route_hierarchy.md](H2_route_hierarchy.md), and
[H2_route_regularized.md](H2_route_regularized.md). The selected
[H2_candidate_v2.md](H2_candidate_v2.md) keeps two current joint populations
and a finite initialized-observable action coefficient block, with an explicit
ridge schedule and direct comparison to canonical GF. Its complete internal
theorem audit [H2_internal_v2.md](H2_internal_v2.md) found no blocking defect;
the coordinator read that report completely. See [H2_checks.md](H2_checks.md).
The first candidate remains preserved.

The concrete [prototype](H2_prototype.py), [13 static tests](H2_test_prototype.py)
and [API/limitations](H2_prototype_notes.md) are frozen. The coordinator read
them completely and independently reran all tests successfully. These use
deterministic prescribed states and analytic identities; no training or
convergence experiment ran. The implementation author was the prompt-route
agent, owning only those three files after its first route was frozen.

The proposed canonical addition is [H2_proposed_section_v1.md](H2_proposed_section_v1.md),
with separate full [book guide](H2_docs_README_v1.md) and
[code guide](H2_code_README_v1.md) proposals. The independent theory relevance
selector accepted assembly in [H2_selection.md](H2_selection.md). A fresh
code relevance selector owns only H2_selection_code.md. Two fresh complete
scientific reviews and a separate integration review remain required before
presenting the concrete promotion decision to the user. No maintained file
or frozen C-H1 file has been edited.
