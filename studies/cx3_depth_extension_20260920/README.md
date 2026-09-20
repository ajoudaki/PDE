# C-X3: depth extension of the nonlinear observable closure

Opened 2026-09-20 at the user's request to formulate and pursue a clean
extension of maintained C-H3 and C-H4 from two tanh hidden layers to three,
then every separately fixed finite depth if possible. Initial HEAD:
`bcee9782651c34ae1204d37186e5c57e9282b273`; tracked files and the shared index
were clean. Unrelated untracked studies are preserved.

## Scope and current status

**The C-H3 branch now has a complete author proof and an internally checked
implementation for three and every separately fixed finite tanh hidden depth.**
The theorem and proof assembly are in [CH3_THEOREM.md](CH3_THEOREM.md).
This status supersedes the initial local gaps in the source-assessment files.
The contract remains [CONTRACT.md](CONTRACT.md), unchanged. The C-H4 branch
through substantial training remains open; C-X3 as a whole is not complete.

The user's subsequent request to complete the substantial-training branch
led to three initially separate proof routes and focused second-round checks.
They did not close the required continuation estimate, already at L=3.
[CH4_PROOF_STATUS.md](CH4_PROOF_STATUS.md) records the resulting partial
theorems and exact remaining gap. In particular, the reference would attain
loss at most exp(-4) at physical time 2(1+3L), if its unique strong flow were
continued to that time. The fitting implication and its unconditional
initialization bound are proved; the continuation premise and fixed positive
supported-law fitting radius remain open. This does not weaken the contract
or reinterpret the local result as a substantial-training theorem.

The new reports also prove global raw Euler/GD bounds, a sufficient
exponential-tail comparison criterion and a weaker sufficient integrated
response estimate. They exhibit exact obstructions to deriving the required
tails from raw energy or ambient raw closeness alone. Those counterexamples
are to proposed implications, not to the prescribed training trajectory.
Each route used only its explicitly assigned study/maintained sources.
No new experiment or finite-network training run was conducted in this round.

The user then requested a renewed proof attempt using the established
orthogonal and near-reference population-flow proofs explicitly. That round
extended the C.4.7 source equations and C.4.6.3's one-column-deletion argument,
but did not close the three-layer continuation estimate.
[CH4_BOOK_RENEWAL_STATUS.md](CH4_BOOK_RENEWAL_STATUS.md) records the new
partial deductions and their exact scope. In particular, a uniform
deleted-column sensitivity bound for actual finite GF would construct the
orthogonal population reference without first assuming Euler source caps.
That sensitivity bound, and the alternative top-source cap, remain unproved.
The source calculation retains the new current transpose-return term and
rules out a pointwise dissipative simplification already near initialization.
These are further attempts on the same continuation obligation; the contract,
the completed local author result, and the open C-X3 status are unchanged.

The local result preserves the broad data domain, full raw state, actual
GF/raw-GD identification, same-law reached-state restart, whole-input and
paired observations, and a convergent autonomous numerical hierarchy. It also
proves per-input motion and genuine nonaffinity in every hidden layer for the
original nonparallel/antiparallel-excluding finite-data activity class with
positive weights and nonzero labels. Its convergence time T_L>0 is fixed
before width, sampling and numerical limits; its strict-activity interval may
depend on the finite dataset. No depth-uniform or growing-depth assertion is
made. Existence itself does not require the activity exclusions. An open
Borel family with all-layer activity contains nonatomic original ArcLaw
members. Arbitrary fixed bounded finite labels are included by the explicit
Y-dependent estimates in the master proof.

This is an author result with disclosed internal cross-checks. It has not
undergone fresh complete independent promotion reviews and is not established
book material. The maintained two-layer C-H3 interval 1/200 is preserved;
the new positive time is depth-dependent and is not asserted to equal 1/200.

Scientific inputs are this study and established `docs/` and `code/`, with
their designated reproduction inputs. C-X1 and C-X2 are not dependencies;
their unpromoted proofs, code, and conclusions may not enter this study.
The supervisor's earlier read-only orientation to those studies is disclosed;
new scoped agents start in fresh contexts with maintained inputs only.

The user first authorized depth-extension contract formulation, then explicitly
asked to prove the C-H3 branch under that contract. The bounded implementation
checks and finite closure operation below discharge its executable obligation.
No finite-neural-network training campaign or promotion was performed. All
source/proof/code artifacts are in this flat study; generated products and
scratch are in `data/generated/cx3_depth_extension_20260920/`.

## Ownership

- Supervisor: README, contract, theorem assembly, initializer, its tests,
  kernel corollary, validation plan/runner/analysis, evidence and any Git transaction.
- C-H3 scope audit: `CH3_SCOPE_AUDIT.md` only.
- C-H4 scope audit: `CH4_SCOPE_AUDIT.md` only.
- Fixed-depth foundations assessment: `DEPTH_FOUNDATIONS.md` only.
- Local-flow author: `CH3_LOCAL_PROOF.md`, followed by activity and assembly checks.
- Activity author: `CH3_ACTIVITY_PROOF.md`, followed by closure implementation/tests
  and the kernel-corollary check.
- Hierarchy author: `CH3_HIERARCHY_PROOF.md`, followed by initializer/local-target check.
- C-H4 source route: `CH4_REFERENCE_SOURCES.md`, including its focused second round.
- C-H4 geometry route: `CH4_REFERENCE_GEOMETRY.md`, followed by the scoped
  `CH4_FITTING_CHECK.md` check of the supervisor's constants.
- C-H4 reached-estimates route: `CH4_REACHED_ESTIMATES.md`.
- Supervisor's C-H4 synthesis: `CH4_FITTING_CONSTANTS.md`,
  `CH4_PROOF_STATUS.md`, `CH4_CHECK.md` and this README.
- Renewed book-proof route: `CH4_BOOK_SOURCE_EXTENSION.md`, followed by
  the scoped `CH4_BOOK_CAVITY_CHECK.md` check of the supervisor's route.
- Supervisor's renewed cavity route and synthesis:
  `CH4_BOOK_CAVITY_EXTENSION.md` and `CH4_BOOK_RENEWAL_STATUS.md`.

Assignments were scoped and separate file ownership was retained. These are
author contributions and internal checks, not independent complete scientific
reviews. No agent staged or committed. Promotion remains a separate reviewed
and user-approved action under RESEARCH_WORKFLOW.md.

## Proof and check disposition

- [CH3_LOCAL_PROOF.md](CH3_LOCAL_PROOF.md): strong full-row/HS flow, uniform
  local source tails including passive queries, broad-law completion,
  uniqueness/restart, actual GF/raw GD, and observations.
- [CH3_ACTIVITY_PROOF.md](CH3_ACTIVITY_PROOF.md): positive forward/backward
  Grams and an adaptive Gaussian innovation induction proving motion at every
  training input in every layer, plus variances and nonaffinity.
- [CH3_HIERARCHY_PROOF.md](CH3_HIERARCHY_PROOF.md): determining initialized
  word hierarchy, finite-feature laws and finite numerical arrays, global
  fixed-order flow, local order convergence, all inner limits and finite costs.
- [CH3_THEOREM.md](CH3_THEOREM.md): connects those results, discharges the
  hierarchy's local target hypotheses, proves the open Borel/nonatomic activity
  bridge, and states the full bounded-label extension.
- [CH3_KERNEL_COROLLARY.md](CH3_KERNEL_COROLLARY.md): retains the other
  strict finite-data C.3 conclusions: positive and nonconstant kernel blocks,
  nonconstant readout/total kernels, each learned action's motion, and local
  strict loss descent.

The supervisor read the complete proof units and checked their calculations
against the assigned maintained sources. The internal checks are:

- [CH3_ACTIVITY_CHECK.md](CH3_ACTIVITY_CHECK.md): PASS on every-layer
  noncancellation, including transpose reuse and within-batch dependencies.
- [CH3_HIERARCHY_CHECK.md](CH3_HIERARCHY_CHECK.md): PASS on the revised
  initializer and the local proof's discharge of hierarchy assumptions. Two
  implementation issues were repaired and regression-tested; a custom sparse
  compiler memory-estimate limitation remains explicitly scoped.
- [CH3_CONTRACT_CHECK.md](CH3_CONTRACT_CHECK.md): final mathematical assembly
  PASS in §8 for master SHA-256
  `954e13c50f5db87d15927eff296da839963677e7c2859351534d90ecf5f38c77`.
  Its earlier minor bounded-label issue is resolved by the master's explicit
  unchanged-equation Y-dependent energy estimates. The original finding is
  preserved as provenance.
- [CH3_KERNEL_CHECK.md](CH3_KERNEL_CHECK.md): PASS on the supplemental strict
  kernel/action/descent corollary.
- [CH3_IMPLEMENTATION_CHECK.md](CH3_IMPLEMENTATION_CHECK.md): supervisor's
  source/equation check, exact artifact hashes, 16 deterministic checks and
  all five predeclared operational cases, with interpretation and limitations.

The author relationships and exact checked hashes are disclosed in each report.
These checks are evidence about this study; they do not replace the repository's
fresh independent promotion process.

## Implementation and operational evidence

[depth_initialization.py](depth_initialization.py) and
[depth_closure.py](depth_closure.py) implement the generic fixed-depth
initializer and finite closure with complete current state. The 16 checks in
[test_depth_initialization.py](test_depth_initialization.py) and
[test_depth_closure.py](test_depth_closure.py) pass. They cover independent
dense actions, all-block gradients, matrix-specific Gaussian responses,
two-layer parity, four-layer operation, and exact own-state restart for
float64, Decimal and rational backends.

All five runs declared in [CH3_VALIDATION_PLAN.md](CH3_VALIDATION_PLAN.md)
passed, at L=3 and orders 1,3,5, including population/input/time refinements.
The complete saved state restarted exactly in every case. Total operational
CPU was 0.975630 seconds, peak RSS 51,212,288 bytes. The independent dense
checkpoint reconstruction in [analyze_ch3.py](analyze_ch3.py) reproduced all
saved observations within 3.89e-15 and verified all source/output hashes.
Evidence is in
`data/generated/cx3_depth_extension_20260920/operation_20260920_01/`, including
`provenance.json`, `summary.json`, `analysis.json`, reports, complete restart
states and paired-observation arrays. The check report links the separate
deterministic logs and resource records and gives reproduction commands.

These finite runs verify operation only. Coarse order-3/5 population Grams are
rank-deficient when feature count exceeds population size, and their condition
diagnostics are large. No modes were deleted and evolution never inverts
those Grams. No resolved accuracy, rate, arbitrary-diagonal convergence or
per-run error certificate is claimed. The operational horizon 1/200 is not
substituted for the theorem's independently chosen local T_L.

## Initial assessments and remaining research

- [CH3_SCOPE_AUDIT.md](CH3_SCOPE_AUDIT.md): broad Borel target versus represented
  numerical family, separate activity assumptions, exact observations/limits,
  and the subsequent scoped contract check.
- [CH4_SCOPE_AUDIT.md](CH4_SCOPE_AUDIT.md): supported Borel/nonatomic domain,
  substantial training, source-control dependencies and contract check.
- [DEPTH_FOUNDATIONS.md](DEPTH_FOUNDATIONS.md): maintained local all-depth
  foundation, preliminary local deductions, conditional fitting identities,
  and missing every-layer activity and long-horizon continuation bridges.

The supervisor read the complete three initial reports. Their contract checks prompted
clarifications of physical/normalized input laws, same-law reached restart,
exact law-valued versus finite scalar state, recovery of L=2 scope, and
successful finite operation/conditioning diagnostics. The local gaps in the
foundations note are superseded by the proof package above. Its longer-horizon
conditional deductions remain author-side and incomplete.

The remaining C-H4 research obligation is construction and unique continuation
of the three-hidden-layer tanh orthogonal opposite-label reference through
the required fitting interval, retaining all initialized actions and their
actual adjoints with sufficient reached response/tail control, then proving
robustness under a fixed positive perturbation. No conditional fitting estimate
or the completed local theorem counts as completion of that branch.

The substantial-training proof attempt is retained in:

- [CH4_FITTING_CONSTANTS.md](CH4_FITTING_CONSTANTS.md): unconditional
  q_L>=1/(1+3L), conditional fitting at T=2(1+3L), and conditional strong
  reference/whole-input endpoints. [CH4_FITTING_CHECK.md](CH4_FITTING_CHECK.md)
  verifies the stated implications at the recorded hash without discharging
  their continuation hypotheses.
- [CH4_REFERENCE_SOURCES.md](CH4_REFERENCE_SOURCES.md): exact reused source
  equations, the failure of a specific absolute-cap closure, and the remaining
  adaptive response problem.
- [CH4_REFERENCE_GEOMETRY.md](CH4_REFERENCE_GEOMETRY.md): autonomous cutoff
  construction and conditional removal, the raw Hessian obstruction, and the
  exact cutoff energy defect.
- [CH4_REACHED_ESTIMATES.md](CH4_REACHED_ESTIMATES.md): unconditional global
  raw bounds and conditional finite-horizon uniqueness/capture/hierarchy
  propagation under adequate tails, including integrated response envelopes.
- [CH4_PROOF_STATUS.md](CH4_PROOF_STATUS.md) and [CH4_CHECK.md](CH4_CHECK.md):
  the first substantial-training round's claim levels, remaining obligations,
  checked revisions and limits, retained at their frozen hashes.
- [CH4_BOOK_SOURCE_EXTENSION.md](CH4_BOOK_SOURCE_EXTENSION.md): renewed
  derivation from the complete book source proof, exact middle responses,
  conditional top-cap construction, and actual local sign tests.
- [CH4_BOOK_CAVITY_EXTENSION.md](CH4_BOOK_CAVITY_EXTENSION.md): actual
  finite-GF Gaussian probes and learned-memory bounds, the unproved
  susceptibility certificate, and its conditional reference construction.
- [CH4_BOOK_RENEWAL_STATUS.md](CH4_BOOK_RENEWAL_STATUS.md) and
  [CH4_BOOK_CAVITY_CHECK.md](CH4_BOOK_CAVITY_CHECK.md): synthesis and scoped
  internal checking of the renewed book-proof attempt.

The reference flow through fitting, its positive supported-law neighborhood,
the corresponding long-horizon actual GF/raw-GD limits and closure convergence,
and unconditional reference endpoints remain unproved. The new reports are
author research with scoped internal checks, not promotion reviews.

## Maintained input provenance

The supervisor personally read the complete maintained C-H3/C-H4 unit
(global_nonlinear.md lines 12555-16000), C.1-C.3 (2454-3835), probability/chain
specializations A.1-A.4 (1840-1898), and C.4.5's statement and complete
reference proof C.4.5.1 (5270-6103) in the initial assembly. The C-H3 proof work
also used the relevant complete C-H1/H2 units and Gaussian conditioning,
source/common-space/raw-metric and chain-rule units III.F.1-10. Assigned
maintained compiler/arithmetic/word code was read for implementation. This
is not a new audit of every transitive maintained dependency. Shared guides
were read and remain unchanged.

Current relevant source SHA256 values:

- AGENTS.md: `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747`.
- RESEARCH_WORKFLOW.md: `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85`.
- docs/global_nonlinear.md: `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
- docs/special_data_limits.md: `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489`.
- docs/README.md: `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad`.
- docs/NOTATION.md: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- code/README.md: `7aa3bc9700a75294f9f209a34e05af4033cd35dd5edb736846ff8bdfdc4bdbb6`.

Only this study and its generated namespace were written. The earlier-round
final checks found HEAD unchanged, no tracked diff and no index diff. During
the renewed book-proof round a concurrent writer advanced shared HEAD to
`80c5e50fadbe56063c25be12eb7a9b02ad0e9b3f`; the assigned maintained-source
hashes above stayed unchanged, and tracked/index diffs were empty at the
renewal check. Unrelated work was preserved. This task made no commit or
established-file change; promotion has not been requested or performed.
