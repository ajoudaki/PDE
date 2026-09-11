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
| weak_topology_route | Analytic weak-law differentiation; C.4 and explicit established dependencies | route_weak_topology.md | first round frozen; second-phase audit |
| statistical_route | Probabilistic empirical forcing / leave-one-out; self-contained assignment only | route_statistical.md | first round frozen; replacement argument in progress |
| source_response_route | Exact finite Gaussian source calculus; selected C.4.7/III.F inputs | route_source_response.md | first round frozen; second sensitivity proof in progress |
| coordinator | Complete established proof reading, raw response and synthesis | remaining study files | active |

All generated products and scratch belong under
`data/generated/trained_prediction_sampling/`. No shared code API is currently used.

## Current evidence and gaps

C.4.7 constructs the actual nearby-law trajectories, their passive-query tails,
reached weighted moments and finite-GF capture. Its first-order contamination
expansion is at the two-point reference only. Extending that derivative to
arbitrary laws and controlling empirical remainders are separate open obligations;
total variation does not approximate a nonatomic law by its empirical measures.

The coordinator has read the complete C.4.5--C.4.7 proofs, C.4.1--C.4.3,
Gaussian-action construction III.F.1--10, and the earlier action/dynamics
dependencies used here, as well as `code/README.md`. Source versions are recorded
below. No scientific material from another study was read.

First-round comparison (all three complete reports read by the coordinator):

- [Weak-topology route](route_weak_topology.md): a negative-Sobolev law norm has
  the sample scale for arbitrary Borel laws; actual trajectory stability and
  observable remainders improve substantially. A closed tangent propagation
  estimate remains missing. The report explains why arbitrary bounded L2 actions
  plus Gaussian tails do not suffice for that estimate.
- [Integrated-forcing route](route_statistical.md): conditional sampling theorem
  using a doubly centered two-observation interaction kernel, including its
  separate diagonal obligation. It still needs actual dynamic response estimates.
- [Source-calculus route](route_source_response.md): fixed-order frozen-source
  tensor sums and rank-independent Gaussian covariance differentiation. Full
  law differentiation must also control feedback of covariances and coefficients.
- [Coordinator candidate](source_calculus_candidate.md): construct the actual
  output derivative through differentiated exact population Euler programs.
  A uniform second law-response estimate is the precise outstanding analytic
  requirement. A short-physical-time closure is under independent attack.

These are partial research results, not a claim that A--C are resolved. In the
second phase the routes may compare their frozen first-round findings. The
probability route is checking whether replacement differences and a smooth law
cutoff suffice for the L2 remainder without any empirical total-variation limit.

Frozen first-round SHA256 hashes:

```
route_weak_topology.md   6da7885de6e6f701954525f13bfe6039c9570f82736b2fbf7d0758cb05946295
route_statistical.md     715877198a4b2231a854d841d9ffa1f6d0cb514ca489467bc90557b03eb33b61
route_source_response.md 51eac24d314a529af831194c09efc8552e6c2be823396571ae09acf710c9f17c
docs/global_nonlinear.md 9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226
docs/special_data_limits.md 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
docs/finite_dynamics.md  a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a
```

## Checks and next action

Required workflow and both math skills read by the coordinator; applicable skill
references read. First-round reports have been compared against the established
inputs; the combined response proof is still under construction. No proof is yet
marked internally checked. No experiments run. The first scoped commit is
`94f776842874fa9b497cba9d5b0cc313cc019970` (initial study contract).
On success prepare a canonical proposal and complete the workflow's independent
selection, paired adversarial reviews and standalone/integration validation.
Explicit user approval of the reviewed package is required before book/code edits.
