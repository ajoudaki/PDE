# Protocol: genuine compressed IDE for three hidden linear layers

Status: frozen before the direct derivation, 20 August 2026.

## Canonical model

There is one unit input and one scalar label.  In normalized coordinates the
three-hidden-layer identity network is

\[
f_n=v_n^{\mathsf T}C_nB_nu_n,
\]

where (u_n,v_n\in\mathbb R^n), (B_n,C_n\in\mathbb R^{n\times n}), and
all normalized entries are initially independent (N(0,1/n)).  Every layer
is trained by full-MSE \(\mu\)P gradient flow.  Width tends to infinity first,
with depth fixed at three.

## Required meaning of compression

An admissible answer has:

1. a fixed finite list of scalar real or complex fields on an explicit
   finite-dimensional classical continuum \(\Omega\subset\mathbb R^d\);
2. one explicit deterministic source measure or density, computable from the
   Gaussian initialization law before training;
3. evolution through pointwise differential terms and finitely many explicit
   integrals over that source;
4. a scalar residual among the state variables, or a direct finite-integral
   readout of the output and loss;
5. an autonomous, restartable current state; and
6. state and source complexity independent of width, Taylor order, and the
   realized future trajectory.

A two-variable scalar kernel is admissible only when it is displayed as an
ordinary field on an explicit fixed domain with an explicit source and
regularity class.  Calling an arbitrary matrix, Hilbert vector, operator,
path space, word algebra, or countably branching coordinate a single object
does not count as compression.

Raw playback of the history from time zero is not autonomous.  A memory
formulation is admissible only if it is converted into a fixed-domain field
equation whose present state is demonstrably sufficient for restart.

## Target theorem

The desired theorem gives a well-posed physical-time IDE satisfying, for
every finite (T),

\[
\sup_{0\le t\le T}
\left(|f_n(t)-f(t)|+|(y-f_n(t))^2-L(t)|\right)
\xrightarrow{\mathbb P}0,
\]

with (L(t)=(y-f(t))^2).  Global physical-time existence and convergence of
the loss to zero are stronger final rungs, not assumptions.

## Claim ladder

- C1: exact finite-width feature-time identities and conserved quantities;
- C2: an explicit low-dimensional continuum source and scalar field system;
- C3: internal closure, autonomy, and well-posedness of that system;
- C4: agreement with every exact fixed-order width-limit jet;
- C5: compact-positive-time finite-width identification;
- C6: global physical-time behavior.

No rung may be inferred merely from the next lower one.

## Forbidden substitutions and falsifiers

The target is not met by:

- the earlier rooted-path Hilbert ODE;
- an (n\)-dimensional vector or matrix renamed as a field;
- a source learned from the loss curve;
- a nonrestartable Volterra playback of the entire past;
- coefficient agreement without a positive-time bridge;
- replacing the three-hidden-layer network by the two-hidden-layer model.

A candidate is falsified if it fails the exact feature-time controls

\[
f'(0)=4,qquad f^{(3)}(0)=160,qquad f^{(5)}(0)=13888,
\]

or if two finite-width initializations with the same proposed source data
produce distinct limiting readouts not represented by its fields.

## Proof routes

The direct routes under consideration are:

1. a conserved spectral or Lax reduction;
2. a product-singular-value or free-resolvent continuum reduction;
3. a scalar correlation/response IDE, accepted only if autonomy can be made
   non-vacuous.

External path-space theory is a hostile comparison only; it is not an
admissible witness for this protocol.
