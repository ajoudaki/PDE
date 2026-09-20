# Numerical tests of dictionary structure and efficiency

Opened 2026-09-20 at the user's request to add experimental packages comparing
the initialized dictionary hierarchy with random, orthogonal, PCA/POD,
Fourier, Galerkin and other simple alternatives. This is a new investigation
of empirical compression value, separate from proving depth continuation.

## Question and current status

At matched information, retained dimension and measured computational cost,
does the initialized forward/adjoint dictionary produce more faithful
autonomous nonlinear training dynamics than simpler dictionary choices?
If it does, which ingredient explains the advantage? If it does not, record
the simplest successful replacement without treating a tie as failure of
the mathematical convergence theorem.

The concrete design is [PACKAGES.md](PACKAGES.md):

- **C-N1:** generic dictionary comparisons inside the same autonomous closure.
- **C-N2:** forward/adjoint PCA/POD and learned low-rank explanations, with
  initialization, past-snapshot and future-oracle information separated.
- **C-N3:** attribution through same-span, adjoint, symmetry/pruning and
  initialization-alignment tests.
- **C-N4:** complete efficiency accounting, simpler output/subnetwork controls,
  transfer, and optional evaluation-cost reductions.

The package contract is the integrated design and governs where the scoped
proposal memos suggest different pilot sizes, baseline groupings or budgets.
No comparative training campaign, performance result or empirical superiority
claim has been produced. Its proposed 30-dense/240-reduced trajectory envelope
and time/memory caps are planning bounds, not results or automatic execution.

The primary first test is a six-method initialization comparison at three
actual dictionary budgets, plus a metric-correct same-span invariance check.
The plan explicitly permits a random, POD, Krylov or landmark method to match
or beat the candidate. A theorem of hierarchy convergence is not evidence of
practical superiority, and a useful empirical tie does not invalidate it.

## Scientific scope and inputs

Use the maintained `docs/` and `code/`, primary external methods references,
and artifacts generated in this study. No other study's proofs, code,
reports or numerical outcomes are scientific inputs. Earlier conversation
motivates the question but supplies no comparative evidence. In particular,
the unpromoted depth proof and its operational runs are not imported.

The maintained two-hidden-layer tanh hierarchy is the initial fully specified
candidate. Depth-three and deeper finite projection benchmarks may be
specified afresh from the maintained network equations; their empirical
comparison will not assume an unpromoted long-time or depth-limit theorem.
An exact implementation of a separately developed candidate requires a
permitted, versioned baseline source before being labelled that candidate.

Model: normalized inputs u=x/sqrt(d), d=2 initially; L fully trained tanh
hidden layers, no biases; independent Gaussian first weights of variance 1,
hidden entries of variance 1/n, stored readout of variance 1/n^2; output
c^T h_L/n; unhalved probability-weighted squared loss; block mobilities
(n,1,...,1,n). Preserve actual matrix transposes and complete joint marks.
Distinguish fixed finite-carrier projections, width-independent population
closures, and input-space predictors in every comparison.

## Ownership and checks

- Supervisor: README, package contract, integration of baseline and audit
  proposals, maintained-source checks and any Git transaction.
- Fresh prompt-only baseline agent: conceptual baseline proposal; no inherited
  study results and no scientific retrieval beyond its assignment.
- Fresh prompt-only experiment agent: experimental validity/decision proposal;
  no inherited study results and no scientific retrieval beyond its assignment.
- Fresh external-methods agent: primary-source method survey only; no repository
  study inputs. Relevant method descriptions must be read before use.

The scoped source reports are:

- [BASELINE_DESIGN.md](BASELINE_DESIGN.md), frozen SHA-256
  `9adb4ac430dfd8c2545da24aae62a20ebd704ce9ab0daad22af5c357d008170b`.
- [EXPERIMENT_DESIGN.md](EXPERIMENT_DESIGN.md), frozen SHA-256
  `fe6fe7deb3268e5b664d199d020eafd84cf39688b1a25d6308a0de66d6f7cf1f`.
- [METHOD_SOURCES.md](METHOD_SOURCES.md), frozen SHA-256
  `2d458172de19a6dcf76230bef4184cace1376dfbf80095949f28b1c92be08e23`.

The supervisor read all three reports completely. The baseline and experiment
agents started in fresh prompt-only scientific contexts; the methods agent
read only the assigned primary external method sources. Supervisor follow-ups
supplied the zero-readout and ridge/metric distinctions explicitly. These are
collaborative author designs, not independent empirical evidence.

An additional scoped review of the integrated contract is recorded in
[PACKAGE_CHECK.md](PACKAGE_CHECK.md). It is an internal design audit, not a
promotion review or validation that any method meets an error threshold.
Its original five findings are retained. Revision 2 of PACKAGES.md addresses
them: admissible frozen random columns, a common physical observable space,
one primary depth within the execution caps, the legitimate P_tau initialization,
and separate native-ridge versus common-filter/metric comparisons. The original
reviewed contract remains in [PACKAGES_V1.md](PACKAGES_V1.md), SHA-256
`806ef79fc6bd3ee7f299c8db9402dd0e559cfa4508027c9ac34cced619379eac`.
The revised contract hash is
`03b564f38962794eb6de5e98f1c3ea47af63f621f48a2ff01d9cc4d4f4ff75fd`.
The focused revision check found all five findings addressed at the design
level. The full report, retaining its original findings and appended check,
has SHA-256 `289c6dc7d4da74329755025b97f6eead5de3aa86fdfa1d9c1a815816b95ab1b0`.
The supervisor read the complete original review and its correction check.
The package design is internally checked for the stated scope; adapters,
numerical settings and empirical claims remain unimplemented/unvalidated.

Important integration choices: retain one full joint population per layer;
separate finite-carrier and population implementations; compare neural
backpropagation POD separately from dynamical balanced POD; do not call
same-span rotations new dictionaries; account for the native positive ridge
filter as well as the span; handle zero initial backward fields explicitly;
and keep the short-time signal gate separate from a stronger feature-learning
arm. The integrated first screen avoids counting Gaussian/QR or equivalent
polynomial coordinates as independent representation families.

Maintained reading for this design: complete docs/README.md and NOTATION.md,
the complete C.4.7.9 (C-H2) unit, complete C.4.7.10 B dictionary construction,
and the C.1 finite-state/metric definitions in global_nonlinear.md. The work
imports no new external convergence theorem and uses no maintained code API.
METHOD_SOURCES records precise method-section coverage of six accessible
primary papers; it does not claim full-paper proof reviews.

Source SHA-256 values checked during design:

- AGENTS.md: `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747`.
- RESEARCH_WORKFLOW.md: `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85`.
- docs/README.md: `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad`.
- docs/NOTATION.md: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- docs/global_nonlinear.md: `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.

Opening shared HEAD: `8a15e0f196ed31af54160c651bdfbf2f109eecf7`.
The shared index was empty and unrelated untracked work was preserved.
This task does not stage, commit, modify established files, or run promotion.
Final repository checks found the same HEAD and empty tracked/index diffs;
only this study's new files were written by this task. No training or
comparative numerical experiment was executed.

## Execution boundary and next step

The requested design is persisted. Before a comparative run, instantiate the
versioned candidate/baseline adapters, exact datasets and rank lists, solver
and quadrature settings, and run manifest within the stated envelope. Validate
adjoints, gradients, coordinate equivalence, and own-state restart, then run
the signal/resolution pilot. This design task does not execute that campaign.
