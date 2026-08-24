# Protocol: autonomous depth-two linear MSE closure

Status: frozen before the positive-time proof, 20 August 2026.

## Model and limit

For one training example and two trainable linear hidden layers, use

\[
f_n(A,W,u)=n^{-3/2}A^T W u,
\qquad A,u\in\mathbb R^n,\quad W\in\mathbb R^{n\times n},
\]

with independent standard-Gaussian initialization.  Train every parameter
by the muP gradient flow

\[
\dot\theta=-\eta n\nabla_\theta (y_\star-f_n)^2.
\]

The claim concerns the width-first limit, uniformly on each compact interval
of physical training time, with convergence in probability.

## Non-vacuous meaning of the requested closure

An admissible closure must satisfy all of the following.

1. **Physical time:** it directly generates the actual MSE gradient-flow
   loss curve, not only feature-ascent time or its Taylor jet at zero.
2. **Autonomous and restartable:** its present state determines its future.
   Stored trajectory history, a precomputed loss curve, and time-dependent
   forcing obtained from the answer are forbidden.
3. **O(1):** the number of fields, scalar variables, and dimensions of the
   source domain do not grow with width, time, or requested derivative order.
   A field over one fixed spectral coordinate is allowed; a width-dependent
   atomic measure or an ever-growing moment hierarchy is not.
4. **Single source:** all initialization information is supplied by one fixed,
   explicit finite matrix-valued measure.  It is not updated during training.
5. **Simple loss readout:** the residual is a scalar state variable, so the
   full MSE is its square.
6. **Positive-time identification:** a formal coefficient match, even to all
   orders, is insufficient.  The continuum system must be derived from the
   finite-width flow and identified on compact physical-time intervals.

## Claim ladder

- C1: exact finite-width invariants reduce the feature characteristic to a
  self-consistent spectral oscillator.
- C2: the finite-width matrix spectral measure converges to one explicit,
  deterministic source measure.
- C3: the resulting autonomous integro-differential equation is locally
  well posed and restartable.
- C4: finite-width muP MSE flow converges to that equation uniformly on every
  compact physical-time interval.
- C5: the limiting MSE solution is global in physical time and converges to
  zero for every fixed real label.

## Falsifiers and adversarial checks

The conjecture fails in the stated form if any of the following occurs:

- the finite-width reduction requires spectral eigenvectors or additional
  state whose size grows with `n`;
- the two initialization spectral channels do not combine into a single
  fixed matrix-valued measure;
- the formal spectral solution has no positive-time mean-field limit;
- translating from feature time to physical MSE time requires trajectory
  memory or an externally supplied clock;
- the continuum vector field is not locally Lipschitz on a natural fixed
  Banach space, or the loss is not a state/readout of that flow.

The proof must also audit normalization (full versus half MSE), the random
initial output, norm imbalance, the negative spectral atom, negative labels,
and the order of the limits `n -> infinity` and `t -> infinity`.

## Proof routes

1. **Invariant/spectral route (primary):** conserve
   `BB^T-xx^T`, pass its two-vector spectral measure to a deterministic
   limit, and prove continuous dependence of the nonlinear oscillator on
   that measure.
2. **Direct Gaussian-program route (cross-check only):** compare the local
   Taylor jet with the independently compiled mean-field derivatives.
3. **No-go audit:** attempt to expose hidden width dependence, hidden memory,
   or a feature-time-only reparameterization in the proposed closure.

Route 1 must stand on its own.  Route 2 cannot upgrade a formal series to a
positive-time theorem.
