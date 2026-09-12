# Independent computation of population feature learning

**Milestone C is unresolved.** The study contains an independent finite causal
source solver, bounded nonlinear trajectory diagnostics through physical time
40, and checked mathematical components. A practical certified approximation
of the requested population flow remains missing. Read the complete
[assessment and gap analysis](resolution.md) before interpreting any result.

Opened 2026-09-12 by the task in Codex thread
`01a09563-faa5-7c90-a8d1-fe92761af0cf`. The study and generated namespace did
not exist at ownership check. Initial HEAD:
`c709b6f292dc58a73e8dd300e9a8217d5646af45`; the index was empty and unrelated
working changes were present. Those paths are not owned by this study.

## Contract

Construct, prove, implement and validate a finite causal approximation of the
C.4.7 physical population GF on [0,40], with whole-circle prediction and joint
hidden/reused-action observations, arbitrary accuracy and an evaluated feasible
resource bound. Use exactly bias-free two-hidden-layer tanh, inputs sqrt(2) S1,
stored variances (1,1/n,1/n^2), mobilities (n,1,n), output /n, unhalved loss,
and the original small finite Gaussian readout. The population starts at
(w,K,c)=(g,0,0) and retains A0 and its actual adjoint.

The admitted family must be fixed independently of accuracy, finite-described,
nontrivial and include genuinely nonatomic correlated laws. One approximation
mechanism must also be naturally defined on a broader declared family. No raw
dense hidden training, target oracle, fitted closure or uncosted Gaussian
integration is admissible. Reached restart includes histories and numerical RNG.

Research inputs: this study and established docs/code only. No other study,
including milestone B, is an input. Source, configuration, tests and reports
remain flat here; all generated products go under
`data/generated/population_flow_computation/`.

## Scientific coverage and ownership

The coordinator owns this README, synthesis and sole Git-writing role. Required
skills solve-math-rigorously and investigate-conjectures and their required
references were read. Complete required C.4.7/C.4.9 units, necessary established
dependencies, observation contracts and integrated-query packages were digested.
The [source record](source_scope.json) gives reading scopes and whole-file hashes.
Coordinator coverage is not imputed to agents; their original reports record
their narrower inputs. No other study or scientific Git history was read.

Independent routes used fresh contexts and remained separate until frozen.
Contributors: causal_sampling_route, spectral_route, admission_route,
admission_check, directional_implementation, generated_error_proof,
practical_certificate_route, solver_code_check and its storage audit,
generated_theorem_check, and passive_quadrature_bound. The coordinator assembled
current notes and performs scoped study commits under the common writer lock.

## Results and implementation

The [finite specification](directional_solver_spec.md) and
[solver](directional_solver.py) use separate statistical populations, weighted
directional response estimates, finite Gaussian covariance factors and every
saved source/history term. No dense hidden parameter matrix is trained.
The [API notes](implementation_notes.md) give configuration, predictions,
paired hidden D/Q observations, diagnostics and complete reached restart.
The same equations accept broader fixed finite circle laws and longer finite
horizons where the numerical process remains defined. No broader population
existence or convergence theorem is inferred.

| Component | Status and evidence |
|---|---|
| Effective admission and fixed nonatomic correlated laws | Conservative proof, internally checked: [route](admission_route.md), [fresh scoped check](admission_check.md), [frozen family](fixed_law_family.md). The literal tiny scale is not materialized. |
| Weighted source-response identities | [Frozen-program identity and variance](random_direction_route.md); adaptive unbiasedness is not assumed. |
| Actual empirical solver at fixed graph and positive noise | Exact-arithmetic consistency: [proof](generated_error_proof.md), [fresh scoped check](generated_theorem_check.md), [passive coupling corrections](proof_corrections.md). |
| Noise-to-clean action comparison | [Coordinator proof draft](noise_and_limit_analysis.md); practical constants and full assembly remain open. |
| Passive Gaussian integration | [One-dimensional transport bound](passive_quadrature.md), [sharper analytic bound](analytic_passive_quadrature.md) and retained-state evaluation; certified floating arithmetic is not implemented. |
| Finite recurrence, Gaussian reuse and restart | Five [author tests](test_directional_solver.py) and a fresh independent [code/algebra check](solver_code_check.md). |
| Requested internal observations | [Typed contract and exact gaps](observation_contract.md); fixed-graph joint laws are narrower than the full population/time target. |

Passive D/Q law convergence requires two conditional principal-root couplings.
The numerical eigenvector factors need not converge under identical raw query
seeds; exact restart of an identical saved state remains valid. Training
precision bounds are conditional on certified operation/primitive errors.
The implementation offers float32/64, not arbitrary certified precision.

Original alternative routes are preserved: [lazy finite conditioning](causal_sampling_route.md),
[spectral approximation](spectral_route.md), [regression draft](source_regression_route.md),
[regression audit](source_regression_audit.md), and
[practical propagation attempt](practical_certificate_route.md).
The lazy route is ineligible because it reproduces finite-network training.
The spectral route lacks a usable generated approximation bound. The inverse-
gate route improves the comparison topology but retains impractical constants.
These are route-specific failures, not an impossibility theorem for C.

## Executed validation and reproduction

The [budget and design](validation_plan.md) preceded execution. All twelve
allowed source trajectories were used, totaling 2490 training calls: three
small implementation trajectories, eight main cases and one combined
refinement. No finite-network training or broad sweep was run. Main evolution
and observations took about 33 seconds as recorded; the largest saved array
state was 172.3 MB and peak recorded process RSS 430,560 KiB. Exact versions,
commands and reporting limitations are in [validation_results.md](validation_results.md).

On nine times and 65 circle directions, baseline changes were .0647 for halving
the physical step, .0560 for quadrupling samples, and **.1100 when both changed**.
Noise and precision changes were smaller. Both hidden layers moved substantially
in the computed process. This is exploratory evidence, not a .1 error bound or
a convergence rate. The exploratory arc law is outside the tiny admitted family.

Producer/configuration and analysis are [run_validation.py](run_validation.py),
[validation_cases.json](validation_cases.json), and
[analyze_validation.py](analyze_validation.py). Fresh-output commands, seeds,
source hashes and software/thread versions are in the results note and each
run's provenance. The trajectory budget is spent; reproduction commands are
documentation, not authorization to execute more runs under that budget.

Generated evidence directories under this study's data root are
`implementation_tests_0188cbdb3759/`, `implementation_observation_check_20260912/`,
`main_validation_20260912_01/`, `combined_validation_20260912_01/`,
`validation_analysis_20260912_01/`, `checkpoint_metadata_check_20260912_01/`,
`solver_code_check/`, `archived_identity_check_20260912_01/`, and
`archived_reporting_check_20260912_01/`, plus
`analytic_quadrature_validation_20260912_01/`. No earlier output was overwritten.

The [analytic component evaluator](evaluate_quadrature_bound.py) used no new
trajectory or random draw. Its final-state q=16 whole-circle formula evaluates
to about 1.1e-11 and 5.1e-12 for the baseline and combined runs. This sharpens
one integration component; floating rounding and all dynamical/source errors
remain separate.

The independent synthetic checks are reusable source:
[check_solver_identities.py](check_solver_identities.py) and
[check_solver_reporting.py](check_solver_reporting.py). They were reproduced
after archiving without new trajectories. No unique proof or essential source
exists only in generated data. An [independent finite-network comparison
protocol](finite_network_comparison_protocol.md) is prepared but unexecuted;
those experiments require separate authorization.

## Remaining work and promotion status

The central gap is a useful **generated** adaptive Gaussian-response/covariance
error estimate and its propagation through [0,40], retaining both orientations
and the joint history. Fixed-program variance and fixed-graph convergence do
not supply a practical simultaneous refinement. Time/noise/law errors,
certified arbitrary precision and the full requested joint observation contract
also remain to be completed. A conditional one-sided stability certificate was
derived, but its useful-size hypothesis has not been verified for this process.

The next scientific target would be a weighted contracted adaptive-error bound
with moderate amplification depending on physical time and controlled source
densities. A target-trajectory oracle, empirical moments alone or a fitted
closure cannot discharge it. No more trajectories belong to the spent campaign.
The current work is preserved as partial research, not declared solved.

Scoped internal checks are not promotion reviews. Independent relevance
screening, two complete isolated scientific/code reviews and a separate
integration review have not been represented as complete. There is no complete
canonical C addition ready for approval. No established book/code files were
changed and no approval is requested for an unfinished C promotion.
