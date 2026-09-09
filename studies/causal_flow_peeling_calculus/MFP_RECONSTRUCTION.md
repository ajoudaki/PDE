# MFP Reconstruction for the Causal-Flow Program

## Claim level

This document is a reconstruction of the maintained Mean Field Peeling (MFP) machinery from the permitted source tree.  It records established MFP mechanisms and the precise gap between fixed finite programs and positive-time dynamics.  It does not yet assert a Causal Flow Peeling theorem.

## 1. What MFP actually computes

MFP starts from a width-normalized **scalar contraction** obtained by exact finite-width differentiation.  A term is scalarized into explicit neuron indices, Gaussian parameter entries, preactivation functions, equality constraints, and width powers.  It then eliminates the highest active layer by conditioning on all lower layers and applying exact Gaussian Wick--Stein identities.

For a current Gaussian matrix entry, an unmatched occurrence is not discarded.  It is attached by Stein differentiation to every current preactivation channel on which the remaining integrand depends.  The covariance inserts a lower-layer activation, which becomes part of the boundary state for the next peel.  Paired occurrences give Wick branches.  Thus the local elimination invariant is:

> no current-layer Gaussian parameter remains, and every dependence it created has been converted into an explicit lower-layer boundary factor or a fresh jointly Gaussian channel with all covariances registered.

This is fundamentally different from treating a reused matrix and its transpose as independent.

## 2. The three pieces of the fixed-program calculus

### 2.1 Algebraic scalarization

Chain, product, and Faà di Bruno rules are applied before the width limit.  The observable is represented by a finite syntax tree or DAG.  The raw/effective parameter convention, optimizer metric, readout normalization, and requested width order are part of the type of the expression.

### 2.2 Layerwise Gaussian elimination

For each raw matrix, actual use chronology matters.  A new forward use consists of a fresh Gaussian channel plus responses to every earlier transpose use.  A new transpose use consists of a fresh Gaussian channel plus responses to every earlier forward use.  Same-orientation fresh channels are jointly Gaussian, with covariance given by empirical inner products of their sources.  Response coefficients are syntactic derivatives of the already constructed coordinate program.

### 2.3 Equality partitions and global valuation

Top-row indices are split into exact equality partitions before averaging.  Width order is counted globally: free index blocks, covariance powers, optimizer factors, normalizations, and all downstream sums created by response attachments are included.  A branch is removable only after its entire lower boundary signature is known.  In particular, a row-distinct family with zero one-copy mean can survive in a two-copy contraction as a fresh Gaussian fluctuation field.

## 3. Probability layer at fixed program size

For a fixed depth, batch, derivative order, and finite number of program lines, the exact contraction can be encoded as one NETSOR-transpose-plus/Tensor Program.  The unrestricted transpose rule supplies the complete joint fresh/response semantics, including singular covariance cases.  Under the maintained polynomial-smooth activation envelope, the cited finite-program theorem yields almost-sure and every-finite-`L^p` convergence of each scalar line.  This simultaneously discharges deterministic covariance replacement and uniform integrability for that fixed program.

This theorem is pointwise in program size.  Its constants and hypotheses are not uniform in the number of training steps or derivative order.

## 4. What the depth recursions establish

For the order-three directional feature coefficient, MFP has a response-aware recursion at every separately fixed depth and batch.  A layer carries forward covariance blocks, reverse covariances, and response matrices; in the one-sample contraction these reduce to a fixed scalar state.  The important structural features are:

- every raw matrix has a finite chronological registry of forward and transpose uses;
- parity eliminates branches only after a joint-program involution is proved;
- one layer transition has a fixed state type independent of width;
- inverse-free Wick--Stein contraction removes auxiliary Gaussian coordinates;
- exact base-depth and nonlinear higher-depth controls audit the local rule.

At order five, the unit-Gram one-sample construction needs six alternating sweeps

\[
F1\to R1\to F2\to R2\to F3\to R3,
\]

with 29 propagated scalar coordinate types.  This is decisive evidence about causality: later moving-feature jets depend on reverse information that is unavailable in the first forward pass.  A compact recursion can therefore require alternating causal sweeps even when every local map is finite.  Flattened formula size and compact state size are distinct notions.

## 5. The precise positive-time gap

For any **fixed** number of Euler steps, unrolling the update produces a finite causal tensor program.  MFP/Tensor-Program semantics can in principle register every fresh field, covariance, and response for that finite program.  This does not imply a continuous-time theorem because the number of lines, response channels, and theorem constants grow as the mesh `h` decreases and the number of steps `T/h` increases.

The missing result is not another fixed-program Gaussian normal form.  It is a completion theorem for a family of increasingly long adaptive programs.  Such a theorem must prove all of the following:

1. a uniform envelope for reachable signals and response objects;
2. a stability modulus for one-step composition and for the limiting vector field;
3. a local consistency defect of order `O(h^2)` for a first-order Euler method (or the corresponding order for another integrator);
4. controlled accumulation of local defects on `[0,T]`;
5. projective consistency of the Gaussian/response semantics across different meshes;
6. closure of the resulting completed source action on the continuously generated signal class;
7. continuity of the predictor and raw-kernel observables in the completed state.

An `O(h)` statement “per step” is insufficient: accumulated over `T/h` steps it can remain order one.

## 6. Why merely adding nonlinear DAG nodes fails

Allowing a node to hold a recursive nonlinear transformation does not itself control:

- growth of its response registry;
- tails or moments of adaptive transpose inputs;
- continuity of multiplication by activation gates in the chosen state norm;
- consistency of fresh Gaussian innovations when the mesh changes;
- the passage from a fixed finite program to infinitely many causal steps.

Without quantitative certificates for those properties, the proposed extension is the original positive-time convergence problem represented as a node.

## 7. The promising extension pattern

The MFP invariant suggests a two-tier successor.

### Tier A: causal peeling at a fixed mesh

Represent every trained matrix as its immutable Gaussian source plus the accumulated low-rank update.  A step compiler exposes source forward/transpose uses, deterministic low-rank actions, equality sectors, and response directions.  Each node carries its value semantics and quantitative certificates, rather than only an explicit Gaussian atom.

### Tier B: certified causal completion

Complete the compatible fixed-mesh programs in a normed reachable-signal space.  The completion must make the source action and its adjoint closed on that space and must propagate a tail/moment envelope strong enough for activation-gated backward products.  A deterministic consistency--stability theorem then removes the mesh.

The likely state certificates are:

- normalized size and higher-moment/tail envelopes;
- forward and transpose response/influence grades;
- a copy/cumulant grade distinguishing means from fluctuation sectors;
- a mesh grade distinguishing values, first variations, and local defects;
- a local stability or Osgood modulus;
- a width-convergence claim level and a complete dependency list.

Whether these certificates close without hiding the original theorem is the central design question.

## 8. Immediate design tests

A proposed calculus will be rejected unless it can answer, by reusable rules rather than model-specific identities:

1. why a fixed-mesh adaptive matrix program has a complete response registry;
2. why the relevant signal envelope is preserved under forward action, transpose action, activation, activation-gated multiplication, and low-rank update;
3. why the per-step flow defect is truly second order in the mesh;
4. why the stability constants or moduli remain usable over `T/h` steps;
5. why limits from two different mesh sequences live on one consistent source;
6. why its completed state is restartable and does not encode the entire past under a new name.

These tests precede any attempt at the three-hidden-layer arctangent target.
