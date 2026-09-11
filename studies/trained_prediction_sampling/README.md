# Sampling fluctuations of the whole trained prediction

Status: active theoretical study; A–C open. No established files changed.

## Contract

For the exact two-hidden-layer tanh model, Gaussian initialization, physical
gradient flow and nearby-law population construction of C.4.7, fix T=40.
Find a positive smaller Wasserstein neighborhood in which every separately
fixed Borel training law has an actual centered whole-circle influence field,
an empirical sampling-scale nonlinear remainder, and an H=L2(circle) Gaussian
fluctuation limit with its spatial covariance. Retain both trained hidden
layers, the learned middle increment, initialized Gaussian action and actual
adjoint. No atom-weight/rank/density restriction is allowed. Width precedes
sample count in the requested finite-network fluctuation bridge.

The separate secondary target is a mean-square remainder sufficient for the
trace-covariance asymptotic. Bad empirical-law events must be handled explicitly.
No training experiments, sweeps, finite-width rate or GD extension are authorized.

## Inputs and ownership

Scientific inputs: this study and established docs/code only; other studies are
excluded. Initial HEAD: b45c022eaf364e4839e87ff86a82e82b90a3004d. Concurrent changes
in maintenance files were observed as metadata and are not owned or inspected.
The root coordinator owns this README, synthesis, checks, review packets and is
the sole Git writer for this study, using the shared pde-writer.lock.

Fresh independent routes (no inherited conversation and no mutual exposure):

| Route | Mechanism / permitted inputs | Owned output | Status |
|---|---|---|---|
| weak_topology_route | Analytic weak-law differentiation; C.4 and explicit established dependencies | route_weak_topology.md | active |
| statistical_route | Probabilistic empirical forcing / leave-one-out; self-contained assignment only | route_statistical.md | active |
| coordinator | Complete established proof reading, raw response and synthesis | remaining study files | active |

All generated products and scratch belong under
`data/generated/trained_prediction_sampling/`. No shared code API is currently used.

## Current evidence and gaps

C.4.7 constructs the actual nearby-law trajectories, their passive-query tails,
reached weighted moments and finite-GF capture. Its first-order contamination
expansion is at the two-point reference only. Extending that derivative to
arbitrary laws and controlling empirical remainders are separate open obligations;
total variation does not approximate a nonatomic law by its empirical measures.

## Checks and next action

Required workflow and both math skills read by the coordinator; applicable skill
references read. Complete source/dependency reading and independent route work
are underway. No proof is yet marked internally checked. No experiments run.
On success prepare a canonical proposal and complete the workflow's independent
selection, paired adversarial reviews and standalone/integration validation.
Explicit user approval of the reviewed package is required before book/code edits.
