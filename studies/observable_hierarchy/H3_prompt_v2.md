# C-H3 revised task prompt: efficient computation with qualitative convergence

Continue Milestone C-H3 in `/home/amir/Codes/PDE/studies/observable_hierarchy/`.
Build an efficient finite numerical implementation of the autonomous observable
closure, with a proof that its refinements converge to the same nonlinear
population GF. This revised target requires qualitative convergence and
practical computation at declared resolutions. It does not require error rates,
per-truncation numerical certificates, or automatic tolerance selection.

## Recover the foundation and the revised scope

Follow `/home/amir/Codes/PDE/AGENTS.md` and `RESEARCH_WORKFLOW.md`. Read
`docs/README.md` for the philosophy and revised C-H3/C-H4 roadmap,
`docs/NOTATION.md`, `code/README.md`, and this study's `README.md`.
Use `solve-math-rigorously` and `investigate-conjectures`, reading their required
instructions and applicable references yourself.

Read the complete maintained C.4.7.8 and C.4.7.9 in `docs/global_nonlinear.md`,
their complete necessary dependency proofs, and the maintained
`code/pde/observable_closure.py` with its tests and guide. The study's
`H2_proposed_section_v3.md`, `dependencies_v1.md`, `H2_prototype_notes_v3.md`,
and `H2_promotion_record_v3.json` provide the frozen source route and mapping.
Check current correspondence; later authorized roadmap edits do not by
themselves change the H2 theorem or implementation.

Read `H3_assessment.md`, `H3_portfolio_comparison.md`, and
`H3_residual_feasibility.md`; follow any proof, implementation or correction
you rely on completely. Candidate routes are not established theorems.
The earlier `H3_contract.md` and its failed full-milestone verdict belong to
the stronger certification task. Preserve them unchanged. Do not inherit their
automatic every-tolerance certificate, all-observation certification interface,
or numerical signal thresholds as requirements of this revised task. The old
bounded reference result does not already fulfill the revised objective.

## Scientific target

Retain H2's exact bias-free two-hidden-layer tanh model, Gaussian initialization,
mobilities `(n,1,n)`, unhalved squared loss, physical GF time, and both directions
of the same reused Gaussian action. Preserve the actual finite random readout
when invoking finite-network results. Use the fixed horizon `T=1/200` and a
fixed supported represented law family including nonorthogonal and nonatomic
examples. Neither family nor horizon may shrink with approximation order.
An existing supported family may be inherited, or the required short-time scope
may be proved directly on an explicit family for the same model. Specify the
input-law representation and numerical integration interface; arbitrary Borel
integration is not an executable oracle.

For closure order N, let f_N be the exact population closure prediction and
let fhat_(N,J) be the finite numerical prediction under a specified refinement J.
Prove, for each separately fixed supported law,

    fhat_(N,J) -> f_N as J -> infinity for every fixed N,
    f_N -> f_mu as N -> infinity,

uniformly over `[0,T]` and the full input circle. Here J must account for all
numerical approximations actually used: joint initialization, population and
input integration, time discretization, and finite arithmetic. State a valid
order of limits or a justified simultaneous refinement. An iterated limit is
acceptable; an arbitrary diagonal choice is not automatically valid. Randomized
methods and convergence in probability are allowed with explicit hypotheses.

Preserve and prove convergence of the declared internal observations, including
training-averaged same-population initial/current hidden activation pairs and
their RMS displacements in both layers. Retain the joint information needed
for both action directions and restart. A universally certified compiler for
every admissible observation graph is not required.

H2 may supply the outer convergence theorem. If the finite equations, dictionary,
regularization or initialization change, prove the necessary compatibility or
replacement convergence result to the identical population GF. Qualitative
convergence of exact equations alone does not prove numerical consistency.

## Computational deliverable

Deliver compact reusable initialization, evolution, whole-circle prediction,
paired-observation and own-state restart APIs. The implementation must operate
at multiple genuinely enriched closure orders, rather than repeatedly changing
redundant coordinates. It must retain the nonlinear feedback of the convergent
closure. A fixed-order initialized-kernel or Duhamel formula with an unremoved
dynamical remainder cannot substitute for this implementation.

Choose the numerical method freely. Sampling, quadrature and other consistent
representations are allowed. Do not freeze the old tensor grid, dictionary
enumeration, exponentially tied ridge or float64 ceiling as mandatory choices.
Conversely, rank deletion, independent replacement of reused Gaussian responses,
or separate sampling of coordinates whose joint law matters need justification.

Account for initialization as well as per-step and total runtime, all retained
joint coordinates, coefficient matrices, quadrature/particle storage, precision,
and workspace. Demonstrate feasible computation at declared resolutions within
recorded resource limits; finiteness alone is insufficient. No bound on the
cost needed for an unknown true-error tolerance is required. For a chosen
resolution, working state and solver workspace must stay bounded independently
of elapsed step count. Do not use a raw neuron-by-neuron middle matrix, fitted
surrogate, target trajectory, growing history, or runtime arbitrary-action oracle.

Run a small predeclared set of refinement and restart checks, with configurations,
seeds where relevant, timings, memory and numerical limitations recorded.
Predictions and paired hidden motions should be observable through the same
implementation. Numerical agreement is evidence about operation and refinement,
not an error certificate or a replacement for the convergence proof. The same
equations should admit broader exploratory inputs with their unproved scope
clearly labelled. No broad sweep or finite-network training campaign is needed.

## Work and acceptance

Use a small set of structurally different approaches if needed. Creative agents
start fresh with explicit prompt-only or selected-source scopes; do not expose
them to other routes before their candidates are ready. Required skills remain
mandatory. Complete independent reviewers receive the full candidate and all
necessary dependencies, without history or prior verdicts.

PDE and PDE-2 share this exact checkout and index. Preserve concurrent work,
coordinate one Git writer, use the common lock, and make progressive scoped
commits. Keep new source and records in separate flat `H3_v2_*` study files,
generated products in fresh `data/generated/observable_hierarchy/<run>/`, and
the existing README as the current record. Do not read other studies.

Implementation and bounded solver-validation runs are authorized by this task;
record finite run budgets and stopping criteria before execution. Do not start
the time-40 extension, broad experiments, or a new certificate campaign. H4
will be reassessed from the completed proof and may then be small or mergeable.

Complete the theory and implementation, meaningful tests, independent
reproduction, two fresh complete isolated scientific reviews, and separate
integration review under the normal relevance and promotion gates. Prepare a
self-contained canonical addition and obtain approval before established
book/code edits. Preserve all original findings and corrections.

If a persistent obstacle prevents completion, identify the exact unproved
implication and distinguish failure of one representation from failure of the
broader target. Do not rename a partial result as completion, or reintroduce
quantitative certification as a hidden prerequisite for this qualitative task.
