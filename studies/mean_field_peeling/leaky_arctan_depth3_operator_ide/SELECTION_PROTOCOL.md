# Activation-selection protocol: three-hidden-layer autonomous IDE

Status: provisional investigation contract; no activation is frozen yet.

## Canonical target

For each width `n`, use the normalized Hilbert spaces

\[
H_{j,n}=(\mathbb R^n,\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w).
\]

The mutually independent initialization is

\[
u_{0,i},A_{0,i}\sim N(0,1),\qquad
(G_{\ell,0})_{ij}\sim N(0,1/n),\quad \ell=1,2.
\]

For one input and one label, the fully trained network is

\[
X_1=\phi(u),\quad Z_2=G_1X_1,\quad X_2=\phi(Z_2),
\quad Z_3=G_2X_2,\quad X_3=\phi(Z_3),
\quad f_n=\langle A,X_3\rangle_n.
\]

All four parameter blocks follow physical gradient flow for
`(y-f_n)^2`, with the normalized vector metrics and ordinary Frobenius
matrix metrics.  No layer may be frozen and no transpose may be replaced by
an independent Gaussian action.

## Non-negotiable closure contract

An admissible limit must use a width-independent, absolutely constant number
of current vector/operator/scalar fields, plus immutable joint Gaussian
actions and their genuine adjoints.  Every current field has exactly one
training-time coordinate.  The equations are autonomous and restartable from
the current state and the same immutable source.  Predictor, raw tangent
kernel, residual, and loss are direct current-state readouts.

Forbidden: DMFT, two-training-time kernels or covariances as state, response
history, stored paths, a time-labelled rank-one decomposition, future
trajectory playback, fresh independent transpose proxies, or a number/type of
state variables growing with width, time, mesh depth, or requested accuracy.

The convergence target is, for every fixed physical horizon `T`, uniform on
`[0,T]` convergence in probability of finite-width predictor, raw tangent
kernel, residual, and loss.

## Selection question

The principal candidate is

\[
\phi_\alpha(x)=\alpha x+(1-\alpha)\arctan x,
\qquad 0<\alpha<1.
\]

It must be compared against at least the genuinely different residual class
`x+lambda*tanh(x)` (up to harmless gain normalization) and a smooth
identity perturbation with compactly supported curvature.  Pure arctangent
and identity are controls, not eligible nonlinear winners.

The winner must minimize the combined difficulty of:

1. exact current-state algebra and a tame global natural coordinate;
2. admissibility under fixed finite transpose-reusing Gaussian programs;
3. compact-physical-time a-priori bounds;
4. restart-stable well-posedness in a named width-independent class;
5. mesh/cutoff removal and square-tail identification of every raw kernel
   term; and
6. a non-circular finite-width convergence proof.

## Claim ladder

| Level | Obligation |
|---|---|
| S0 | Exact finite equations, natural-coordinate identities, and `f'_n=K_n` |
| S1 | One immutable two-matrix source with actual adjoints and fixed-program convergence |
| S2 | Exact O(1)-species autonomous current-state IDE and direct readouts |
| S3 | Compact-horizon well-posedness and restartability in a named class |
| S4 | Fixed-cutoff, fixed-mesh finite-width identification |
| S5 | Mesh and all cutoffs removed; raw kernel identified uniformly on compact physical time |
| S6 | Uniform compact-time convergence of predictor, kernel, residual, and loss |

No activation is selected unless a hostile audit finds no witness-fatal
obstruction before S3--S5, and the precise remaining proof obligations are
strictly easier than for pure arctangent at depth three.

## Concrete falsifiers

- A canonical iid-reachable coordinate concentration carrying nonvanishing
  raw-kernel energy falsifies S5--S6 for the proposed topology.
- A finite-width nonexistence/nonuniqueness example falsifies the activation
  as a canonical smooth-flow witness.
- Failure of a natural coordinate or transformed seed to lie in the finite
  Gaussian-program class is witness-fatal for the proposed source proof.
- An unbounded-forward cutoff comparison whose stability loss cannot be
  beaten by the initialization tail is witness-fatal for that cutoff route,
  but not automatically for the activation.
- A proof that only closes after storing a second training time or a growing
  response hierarchy violates the contract and is rejected, even if correct
  for a different formulation.

