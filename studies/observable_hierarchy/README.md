# Observable hierarchy — milestone C-H1

Complete candidate written; internal audits and promotion gates are in progress.
No result is promoted.

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

The current complete candidate is [theorem_v2.md](theorem_v2.md); version 1 is
retained. It uses a finite typed alphabet and finite-dimensional scalar/input
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

Next: finish internal representation checking and independent relevance selection,
assemble the concrete addition, and obtain two fresh complete isolated adversarial
reviews plus independent integration review. Any promotion proposal stays in this
study until the user's approval of the concrete reviewed addition. Theorem and
finite dependency are exact; finite closure convergence and effective cutoff,
quadrature and solver costs remain open for C-H2 and later milestones.
